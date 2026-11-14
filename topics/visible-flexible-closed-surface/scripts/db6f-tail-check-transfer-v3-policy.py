#!/usr/bin/env python3
"""Author checks of v3 metadata guards and unchanged transfer algebra; no grid/flow."""
import argparse
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def module(path):
    spec = importlib.util.spec_from_file_location('tail_transfer_v3_author_check', path)
    result = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = result
    spec.loader.exec_module(result)
    return result


def functions(path):
    return {x.name: x for x in ast.parse(Path(path).read_text()).body
            if isinstance(x, ast.FunctionDef)}


def transfer_block(fun):
    start = next(i for i, x in enumerate(fun.body)
                 if isinstance(x, ast.Expr) and isinstance(x.value, ast.Call)
                 and isinstance(x.value.func, ast.Name) and x.value.func.id == 'check'
                 and 'physical background domains differ' in ast.unparse(x))
    stop = next(i+1 for i, x in enumerate(fun.body)
                if isinstance(x, ast.Assign) and isinstance(x.value, ast.Call)
                and isinstance(x.value.func, ast.Name) and x.value.func.id == 'write_npz')
    return ast.dump(ast.Module(body=fun.body[start:stop], type_ignores=[]),
                    include_attributes=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--preflight', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    source = HERE/'db6f-tail-transfer-background-v3.py'
    base = HERE/'db6f-root-transfer-background.py'
    actual = module(source)
    assert sha(base) == actual.BASE_TRANSFER_SHA256
    before, after = functions(base), functions(source)
    unchanged = {name: ast.dump(before[name], include_attributes=False)
                 == ast.dump(after[name], include_attributes=False)
                 for name in ('grid', 'fraction_vectors', 'affine_coefficients',
                              'write_npz', 'check', 'sha')}
    assert all(unchanged.values())
    same_math = transfer_block(before['main']) == transfer_block(after['main'])
    assert same_math
    cases = [
        ('same dictionary', {'rCut': .6}, {'rCut': .6}, True),
        ('four reviewed keys', {'rCut': .6}, {'rCut': .6,
            'iterationCheckpointFile': 'a', 'sharedEngines': True,
            'trialDiagnosticFile': 'b', 'trialStatePrefix': 'c'}, True),
        ('unknown added null', {}, {'unreviewedKey': None}, False),
        ('unknown removed null', {'unreviewedKey': None}, {}, False),
        ('unknown changed', {'unreviewedKey': 'x'}, {'unreviewedKey': 'y'}, False),
        ('physical value changed', {'rCut': .6}, {'rCut': .5}, False),
        ('physical added null', {}, {'rCut': None}, False),
        ('sharedEngines string rejected', {}, {'sharedEngines': 'true'}, False),
        ('path boolean rejected', {}, {'iterationCheckpointFile': False}, False),
        ('approved null is explicit numerical metadata', {},
            {'iterationCheckpointFile': None}, True),
        ('unknown false to zero', {'x': False}, {'x': 0}, False),
        ('unknown true to one', {'x': True}, {'x': 1}, False),
        ('nested false to zero', {'x': {'a': [False]}}, {'x': {'a': [0]}}, False),
        ('nested true to one', {'x': [True]}, {'x': [1]}, False),
        ('int to float conservative rejection', {'x': 1}, {'x': 1.0}, False),
        ('nonfinite unchanged rejection', {'x': float('nan')},
            {'x': float('nan')}, False),
        ('dictionary order harmless', {'x': {'a': 1, 'b': 2}},
            {'x': {'b': 2, 'a': 1}}, True)]
    checks = []
    for name, old, new, expected in cases:
        try:
            different = actual.check_parameters(old, new)
            accepted, error = True, None
        except ValueError as exc:
            accepted, different, error = False, None, str(exc)
        assert accepted is expected, name
        checks.append(dict(name=name, expected_accept=expected, accepted=accepted,
                           different=different, error=error))
    pre = json.loads(args.preflight.read_text())
    assert pre['script_sha256'] == sha(source)
    assert pre['base_transfer_script_sha256'] == sha(base)
    assert pre['parameter_policy'] == actual.PARAMETER_POLICY
    assert pre['parameter_policy_sha256'] == actual.parameter_policy_sha256()
    assert pre['mode'] == 'parameter-only-preflight'
    assert pre['status'] == 'read-only-parameter-and-background-source-preflight'
    assert all(key not in pre for key in ('finished', 'new_manifest',
                                         'finite_tail_manifest_sha256'))
    assert pre['geometric_transfer_performed'] is False
    assert pre['finite_map_was_created'] is False
    assert pre['actual_new_root_flow_solver_calls'] == 0
    report = dict(status='AUTHOR_METADATA_GUARDS_PASS_NOT_INDEPENDENT_REVIEW',
        script=str(Path(__file__).resolve()), script_sha256=sha(__file__),
        transfer_script=str(source), transfer_script_sha256=sha(source),
        frozen_base_sha256=sha(base), parameter_policy=actual.PARAMETER_POLICY,
        parameter_policy_sha256=actual.parameter_policy_sha256(),
        unchanged_functions=unchanged, exact_transfer_geometry_block_unchanged=same_math,
        checks=checks, preflight=str(args.preflight), preflight_sha256=sha(args.preflight),
        actual_new_root_flow_solver_calls=0, geometric_transfer_performed=False)
    with args.out.open('x') as handle:
        json.dump(report, handle, indent=2, allow_nan=False)
        handle.write('\n')
    print(json.dumps(dict(guard_checks_passed=len(checks),
        transfer_script_sha256=sha(source), parameter_policy_sha256=actual.parameter_policy_sha256(),
        preflight_sha256=sha(args.preflight), report_sha256=sha(args.out),
        actual_new_root_flow_solver_calls=0)))


if __name__ == '__main__':
    main()
