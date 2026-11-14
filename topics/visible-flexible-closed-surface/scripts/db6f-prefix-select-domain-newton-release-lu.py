#!/usr/bin/env python3
"""Explicit, opt-in identity selector for the one-statement LU lifetime change.

Import and both CLI modes install nothing and call no solver.  select_newton()
is a future runtime operation: it requires the original installed function,
shares its STATS object, and exposes a different function identity.  Existing
true-M14 selectors/auditors reject that identity and must not be bypassed.
"""
import argparse
import ast
import copy
import hashlib
import inspect
import json
from pathlib import Path
import sys
from types import ModuleType

HERE = Path(__file__).resolve().parent
DERIVED = HERE / 'db6f-prefix-domain-newton-release-lu.py'
ORIGINAL_SHA = '6cb269210e609e1f49c20004be0ce3f9f68e43e47ab57eaf16bb9e56fa3be654'
DERIVED_SHA = '23ec0f1fe25bc8f904b771f020449c7d95e071d2fc17b6daf4caa93ccd31880b'
BVP_SHA = '59afffb3607b272ae77f346d86428e43eca359fe90f2605da60a9571e60970d2'
PARAMETERS = ['n','m','h','col_fun','bc','jac','y','p','B','bvp_tol','bc_tol']


def require(ok, message):
    if not ok:
        raise ValueError(message)


def identity(path):
    path = Path(path).resolve()
    data = path.read_bytes()
    return {'path': str(path), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def function_definition(path, name):
    path = Path(path).resolve()
    text = path.read_text()
    found = [n for n in ast.parse(text).body
             if isinstance(n, ast.FunctionDef) and n.name == name]
    require(len(found) == 1 and not found[0].decorator_list,
            'Unexpected function definition: ' + name)
    node = found[0]
    source = ast.get_source_segment(text, node).rstrip()
    return node, {'file': identity(path), 'qualname': name,
                  'first_line': node.lineno,
                  'source_sha256_rstrip': hashlib.sha256(source.encode()).hexdigest()}


def definitions(original_path):
    original_path = Path(original_path).resolve()
    require(identity(original_path)['sha256'] == ORIGINAL_SHA, 'Original source hash changed')
    require(identity(DERIVED)['sha256'] == DERIVED_SHA, 'Derived source hash changed')
    old, old_info = function_definition(original_path, 'solve_newton')
    new, new_info = function_definition(DERIVED, 'solve_newton')
    expected = copy.deepcopy(old)
    loops = [n for n in expected.body if isinstance(n, ast.For)]
    require(len(loops) == 1, 'Original outer loop changed')
    refresh = [n for n in loops[0].body if isinstance(n, ast.If)
               and isinstance(n.test, ast.Name) and n.test.id == 'refresh']
    require(len(refresh) == 1, 'Original refresh branch changed')
    refresh[0].body.insert(1, ast.parse('factor=None').body[0])
    require(ast.dump(expected, include_attributes=False) == ast.dump(new, include_attributes=False),
            'Derived function differs beyond the one lifetime assignment')
    require([n.arg for n in old.args.args] == PARAMETERS, 'Original signature changed')
    return {'schema': 'db6f-newton-lu-lifetime-definitions-v1',
            'original_newton': old_info, 'derived_newton': new_info,
            'original_install': function_definition(original_path, 'install')[1],
            'selector': identity(__file__), 'statement_added': 'factor=None',
            'solver_calls': 0, 'installed': False}


def check_function(function, expected):
    require(inspect.isfunction(function) and function.__closure__ is None,
            'Unexpected running function object')
    require(Path(function.__code__.co_filename).resolve() == Path(expected['file']['path'])
            and function.__qualname__ == expected['qualname']
            and function.__code__.co_firstlineno == expected['first_line'],
            'Running function location or name differs')
    require(identity(expected['file']['path']) == expected['file'], 'Running source file changed')
    require(hashlib.sha256(inspect.getsource(function).rstrip().encode()).hexdigest()
            == expected['source_sha256_rstrip'], 'Running function source differs')
    return {**expected, 'runtime_module': function.__module__,
            'signature': str(inspect.signature(function))}


def original_runtime_gate(original, bvp):
    """Read-only. It does not call the original install() or a Newton function."""
    info = definitions(original.__file__)
    require(identity(bvp.__file__)['sha256'] == BVP_SHA, 'SciPy BVP layout changed')
    require(bvp.solve_newton is original.solve_newton,
            'Original domain-aware Newton is not installed; refusing selection')
    check_function(original.solve_newton, info['original_newton'])
    check_function(original.install, info['original_install'])
    require(list(inspect.signature(original.solve_newton).parameters) == PARAMETERS,
            'Original runtime signature changed')
    require(type(original.STATS) is dict, 'Original STATS object is not a dictionary')
    require(original.solve_newton.__globals__.get('STATS') is original.STATS,
            'Original function does not use its declared STATS object')
    return info


def load_definitions(path, name):
    """Compile exactly the verified bytes; no pycache and no install side effect."""
    path = Path(path).resolve()
    module = ModuleType(name)
    module.__file__ = str(path)
    exec(compile(path.read_bytes(), str(path), 'exec'), module.__dict__)
    return module


class Selection:
    """An explicit changed runtime identity; not a true-M14 launch or certificate."""
    def __init__(self, original, bvp, derived, info):
        self.original, self.bvp, self.derived, self.info = original, bvp, derived, info
        self.original_function = original.solve_newton
        self.stats = original.STATS
        self.active = True

    def check(self):
        require(self.active, 'Selection has already been restored')
        require(self.original.solve_newton is self.original_function,
                'Original exported Newton was changed')
        require(self.bvp.solve_newton is self.derived.solve_newton,
                'Selected Newton was changed or original install() ran again')
        require(self.original.STATS is self.stats and self.derived.STATS is self.stats
                and self.derived.solve_newton.__globals__.get('STATS') is self.stats,
                'Original STATS alias was lost')
        require(self.derived.np is self.original.np and self.derived.splu is self.original.splu,
                'NumPy or sparse factorization callable changed')
        require(identity(self.bvp.__file__)['sha256'] == BVP_SHA, 'SciPy source changed')
        check_function(self.original_function, self.info['original_newton'])
        check_function(self.original.install, self.info['original_install'])
        selected = check_function(self.derived.solve_newton, self.info['derived_newton'])
        return {'schema': 'db6f-newton-lu-lifetime-runtime-v1',
                'original_definition': self.info['original_newton'],
                'selected_runtime': selected, 'selector': identity(__file__),
                'scipy_bvp_source': identity(self.bvp.__file__),
                'original_STATS_alias': True, 'changed_runtime_identity': True,
                'scope': 'Only runtime identity; no BVP success or memory guarantee.'}

    def restore(self):
        self.check()
        self.bvp.solve_newton = self.original_function
        self.active = False


def select_newton(original, bvp):
    """Future explicit mutation, never called by import, CLI or the pure checks."""
    info = original_runtime_gate(original, bvp)
    derived = load_definitions(DERIVED, 'db6f_lu_lifetime_selected_definition_v1')
    check_function(derived.solve_newton, info['derived_newton'])
    require(derived.np is original.np and derived.splu is original.splu,
            'The factorization or array callable differs')
    # The original coupled main has already imported this exact dictionary.
    # Keep its counters observable; never reset or silently replace it.
    derived.STATS = original.STATS
    selection = Selection(original, bvp, derived, info)
    bvp.solve_newton = derived.solve_newton
    try:
        selection.check()
    except BaseException:
        if bvp.solve_newton is derived.solve_newton:
            bvp.solve_newton = selection.original_function
        selection.active = False
        raise
    return selection


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--original', type=Path, required=True)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--check-definitions', action='store_true')
    group.add_argument('--check-current-gate', action='store_true')
    args = parser.parse_args()
    info = definitions(args.original)
    if args.check_definitions:
        print(json.dumps(info, sort_keys=True))
        return 0
    # A fresh process normally has SciPy's own function and must be rejected.
    # Loading the original definitions does not run original.install().
    import scipy.integrate._bvp as bvp
    before = bvp.solve_newton
    original = load_definitions(args.original, 'db6f_original_definition_negative_gate')
    try:
        original_runtime_gate(original, bvp)
    except ValueError as error:
        require(bvp.solve_newton is before, 'Read-only gate changed the runtime function')
        print(json.dumps({'status': 'NOT_SELECTED', 'ready': False,
                          'reason': str(error), 'source_definitions': info,
                          'solver_calls': 0, 'install_calls': 0, 'runtime_unchanged': True}, sort_keys=True))
        return 2
    require(bvp.solve_newton is before, 'Read-only gate changed the runtime function')
    print(json.dumps({'status': 'ORIGINAL_RUNTIME_ONLY', 'ready': False,
                      'solver_calls': 0, 'install_calls': 0, 'runtime_unchanged': True}, sort_keys=True))
    return 0


if __name__ == '__main__':
    sys.exit(main())
