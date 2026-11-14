#!/usr/bin/env python3
"""Small real source/code checks; no mathematical callback or solver calls."""
import argparse
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import struct
import sys
import tempfile
from types import CodeType, FunctionType, ModuleType

HERE = Path(__file__).resolve().parent
CORE = HERE / '78718-canonical-runtime-code-v1.py'


def load(path):
    spec = importlib.util.spec_from_file_location('canonical_code_checked_v1', path)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def cell(value):
    return (lambda: value).__closure__[0]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    if args.out.exists():
        raise FileExistsError(args.out)
    c = load(CORE)
    rejected = []

    def negative(name, action):
        try:
            action()
        except (ValueError, TypeError) as error:
            rejected.append({'case': name, 'error_type': type(error).__name__, 'reason': str(error)})
        else:
            raise AssertionError('Changed identity was accepted: ' + name)

    with tempfile.TemporaryDirectory(prefix='78718-code-check-') as temporary:
        path = Path(temporary) / 'fixture.py'
        text = ('def outer(a, /, b=3, *args, k=4, **kwargs):\n'
                '    x = (0.0, -0.0, 7, True, None, Ellipsis, b"q", "q")\n'
                '    def inner(z):\n'
                '        return z + a\n'
                '    try:\n'
                '        return inner(b), x, args, kwargs, k\n'
                '    except ValueError:\n'
                '        return None\n')
        path.write_text(text)
        namespace = ModuleType('canonical_code_synthetic_fixture')
        namespace.__file__ = str(path)
        exec(compile(path.read_bytes(), str(path), 'exec', dont_inherit=True), vars(namespace))
        # exec only defines outer; neither outer nor inner is called.
        function = namespace.outer
        raw = c.raw_function(function)
        row = c.capture(function, raw)
        if not c.check_record(row, raw, path, 'outer', namespace.__name__):
            raise AssertionError('Baseline did not pass')
        base = function.__code__

        def reject_code(name, code):
            mutated = FunctionType(code, vars(namespace), closure=tuple(cell(None) for _ in code.co_freevars) or None)
            mutated.__module__ = namespace.__name__
            mutated.__qualname__ = code.co_qualname
            observed = c.raw_function(mutated)
            changed = {'schema': c.SCHEMA, 'runtime': observed, 'source': c.identity(path),
                       'canonical_code_sha256': c.code_digest(code), 'environment': c.environment()}
            negative(name, lambda: c.check_record(changed, observed, path, 'outer', namespace.__name__))

        replacements = {
            'co_argcount': base.co_argcount - 1,
            'co_posonlyargcount': 0,
            'co_kwonlyargcount': 0,
            'co_stacksize': base.co_stacksize + 1,
            'co_flags': base.co_flags ^ 0x08,
            'co_code': base.co_code + bytes((9, 0)),
            'co_consts': base.co_consts + (192837465,),
            'co_names': base.co_names + ('unused_name_change',),
            'co_varnames': ('different_a',) + base.co_varnames[1:],
            'co_filename': str(Path(temporary) / 'different.py'),
            'co_name': 'different_outer',
            'co_qualname': 'different_outer',
            'co_firstlineno': base.co_firstlineno + 1,
            'co_linetable': base.co_linetable + b'\x00',
            'co_exceptiontable': base.co_exceptiontable + b'\x00',
            'co_freevars': base.co_freevars + ('extra_freevar',),
            'co_cellvars': base.co_cellvars + ('extra_cellvar',),
        }
        for name, value in replacements.items():
            reject_code(name, base.replace(**{name: value}))
        reject_code('co_nlocals', base.replace(co_nlocals=base.co_nlocals + 1,
                                               co_varnames=base.co_varnames + ('extra_local',)))
        nested = next(item for item in base.co_consts if type(item) is CodeType)
        changed_nested = nested.replace(co_code=nested.co_code + bytes((9, 0)))
        reject_code('nested_code', base.replace(co_consts=tuple(
            changed_nested if item is nested else item for item in base.co_consts)))
        negative('unknown_constant_type', lambda: c.code_digest(base.replace(co_consts=base.co_consts + (object(),))))
        detached = copy.deepcopy(row)
        detached['runtime']['code_sha256'] = '0' * 64
        negative('detached_raw_runtime', lambda: c.check_record(detached, raw, path, 'outer', namespace.__name__))
        bad_environment = copy.deepcopy(row)
        bad_environment['environment']['sys_version'] += '-changed'
        negative('changed_environment', lambda: c.check_record(bad_environment, raw, path, 'outer', namespace.__name__))
        path.write_text(text + '# changed source bytes with equal function code\n')
        negative('source_bytes_only', lambda: c.check_record(row, raw, path, 'outer', namespace.__name__))
        path.write_text(text.replace('return None', 'return 1'))
        negative('source_body', lambda: c.capture(function, raw))

    float_bits = ['0000000000000000', '8000000000000000', '7ff8000000000001',
                  '7ff8000000000002', 'fff8000000000001', '7ff0000000000001']
    encodings = []
    for bits in float_bits:
        value = struct.unpack('>d', bytes.fromhex(bits))[0]
        encoded = c.value_tree(value)
        if encoded != ['float64', bits]:
            raise AssertionError('A float bit pattern was normalized')
        encodings.append(c.serial(encoded))
    if len(set(encodings)) != len(float_bits):
        raise AssertionError('Distinct float bits collided')
    if c.value_tree(True) == c.value_tree(1) or c.value_tree(1) == c.value_tree(1.0):
        raise AssertionError('Distinct constant types collided')
    if c.value_tree(frozenset([1, 'x', b'x'])) != c.value_tree(frozenset([b'x', 'x', 1])):
        raise AssertionError('Frozenset insertion order leaked into the encoding')

    import scipy.integrate._bvp as bvp
    source = Path(bvp.__file__)
    if c.identity(source)['sha256'] != '59afffb3607b272ae77f346d86428e43eca359fe90f2605da60a9571e60970d2':
        raise ValueError('Different pinned SciPy source')
    actual = []
    for name in ('prepare_sys', 'construct_global_jac', 'compute_jac_indices', 'solve_bvp'):
        live = getattr(bvp, name)
        captured = c.capture(live, c.raw_function(live))
        actual.append({'name': name, 'canonical_code_sha256': captured['canonical_code_sha256'],
                       'source_sha256': captured['source']['sha256'], 'live_matches_compiled': True})
    result = {'schema': '78718-canonical-runtime-code-check-v1',
              'status': 'PASS_TYPED_CODE_SOURCE_IDENTITY_ONLY',
              'checker': c.identity(__file__), 'core': c.identity(CORE),
              'environment': c.environment(), 'actual_scipy_functions': actual,
              'public_code_data_fields': list(c.FIELDS), 'rejections': rejected,
              'negative_cases_rejected': len(rejected),
              'float_bit_cases': len(float_bits), 'typed_constants_distinct': True,
              'frozenset_order_independent': True, 'nested_code_change_rejected': True,
              'code_objects_executed_as_functions': 0, 'math_callbacks': 0,
              'matrices_or_factories': 0, 'BVP_Newton_DN_calls': 0,
              'original_solver_or_gate_modified': False, 'coupled_success_claimed': False}
    data = (json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False) + '\n').encode()
    with args.out.open('xb') as output:
        output.write(data)
    print(json.dumps({'status': result['status'], 'negative_cases_rejected': len(rejected),
                      'actual_scipy_functions': len(actual), 'float_bit_cases': len(float_bits),
                      'report_bytes': len(data), 'report_sha256': hashlib.sha256(data).hexdigest(),
                      'BVP_Newton_DN_calls': 0}))


if __name__ == '__main__':
    main()
