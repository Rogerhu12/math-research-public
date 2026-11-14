#!/usr/bin/env python3
"""Independent static AST and existing-input metadata check; never runs the wrapper."""
import argparse
import ast
import gzip
import hashlib
import json
import math
from pathlib import Path


TOPIC = Path(__file__).resolve().parent.parent
REPO = TOPIC.parents[1]
NOTES = TOPIC/'notes'
IO = {'initialCheckpoint', 'traceFile', 'iterationCheckpointFile',
      'trialDiagnosticFile', 'trialStatePrefix'}
RUN = IO | {'maxIterations'}
PINS = {
    'runner_v1': (TOPIC/'scripts/db6f-prefix-single-audited-target.py',
                  'e0c4792dc081bcd4c2082064f853d1b8a06e7ca03dba68742d3f066631cd43c7'),
    'runner_v2': (TOPIC/'scripts/db6f-prefix-single-audited-target-v2.py',
                  '173d03b8c02107349275ad58509cd24d09963c6e26a09e17458507db1e20c7c5'),
    'method_v2': (NOTES/'2026-11-09-db6f-prefix-single-audited-target-method-v2.md',
                  '6d52c8841c7d55ccc5fc12a5f746ec727c9f4c390eabf1f6bed355c309418197'),
    'authority': (NOTES/'2026-11-09-db6f-prefix-amplitude-resume02-launch.json',
                   'b2e7371a89906a5f1048077eb2040fef8f2c0a58a136ef3812ab6cbc36b5310e'),
    'authority_bindings': (NOTES/'2026-11-09-db6f-prefix-flat-v17v18-m15-amplitude-continuation-02-input-bindings.json',
                          'aa692dcd64d4b7c56235180babf074a3efe92c95ddbedc3e880d9657fd4996a4'),
    'warm': (NOTES/'2026-11-09-db6f-tail-harmonic-s1-from-call9-input.json.gz',
             'c6a4c0e504802885f358c340c1a23a34355476ee4d241e3ea6b14069b2b4f927'),
    'config': (NOTES/'2026-11-09-db6f-tail-harmonic-s1-from-call9-config.json',
               '6f1398220b3317c3e481b43950eea7b81d6de301a7047069e26821d83db22ac3'),
}


def read(path):
    data = Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if data[:2] == b'\x1f\x8b' else data)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def local(value):
    path = Path(value)
    return path if path.is_absolute() else REPO/path


def ident(path):
    path = Path(path).resolve()
    data = path.read_bytes()
    return {'path': path.relative_to(REPO).as_posix(),
            'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}


def finite(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def require(test, message):
    if not test:
        raise ValueError(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    require(not args.out.exists(), 'Refusing to overwrite review output')
    pinned = {}
    for name, (path, expected) in PINS.items():
        row = ident(path)
        require(row['sha256'] == expected, 'Frozen input changed: '+name)
        pinned[name] = row
    trees = [ast.parse(PINS[name][0].read_text()) for name in ('runner_v1', 'runner_v2')]
    functions = [{f.name: f for f in tree.body if isinstance(f, ast.FunctionDef)} for tree in trees]
    require(ast.dump(functions[0]['main']) == ast.dump(functions[1]['main']),
            'Execution path changed beyond the reviewed v2 identity fix')
    calls = [node for node in ast.walk(trees[1])
             if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
             and isinstance(node.func.value, ast.Name) and node.func.value.id == 'port'
             and node.func.attr == 'solve']
    require(len(calls) == 1, 'The wrapper must contain exactly one port.solve call')
    call = calls[0]
    require(len(call.args) == 1 and isinstance(call.args[0], ast.Call)
            and isinstance(call.args[0].func, ast.Attribute)
            and isinstance(call.args[0].func.value, ast.Name)
            and call.args[0].func.value.id == 'goal' and call.args[0].func.attr == 'copy'
            and not call.args[0].args and not call.args[0].keywords, 'Goal must be copied directly')
    flags = {k.arg: ast.literal_eval(k.value) for k in call.keywords}
    require(set(flags) == {'jacobian', 'audit'} and all(value is True for value in flags.values()),
            'Single call flags changed')
    authority, definitions = read(PINS['authority'][0]), read(PINS['authority_bindings'][0])
    require(len(authority['bound_files']) == 66, 'Wrong frozen source inventory')
    for row in authority['bound_files']:
        current = ident(local(row['path']))
        require(current['sha256'] == row['sha256'] and current['bytes'] == row['bytes'],
                'Authority binding changed')
    base_path, ref_path = local(definitions['config']), local(definitions['resume_record'])
    require(ident(base_path)['sha256'] == definitions['config_sha256'], 'Base config changed')
    require(ident(ref_path)['sha256'] == definitions['resume_record_sha256'], 'Reference changed')
    base, reference = read(base_path), read(ref_path)['response']['checkpoint']
    warm, cfg = read(PINS['warm'][0]), read(PINS['config'][0])
    cp = warm['checkpoint']
    strip = lambda obj, keys: {k:v for k,v in obj.items() if k not in keys}
    require(canonical(strip(cfg, IO)) == canonical(strip(base, IO)), 'Typed non-IO config differs')
    require(canonical(strip(cp['parameters'], RUN)) == canonical(strip(reference['parameters'], RUN)),
            'Typed non-run parameter signature differs')
    differences = {k for k in set(cp['parameters']) | set(reference['parameters'])
                   if k not in cp['parameters'] or k not in reference['parameters']
                   or canonical(cp['parameters'][k]) != canonical(reference['parameters'][k])}
    require(differences == RUN, 'Actual reference differences are not the six documented run keys')
    require(cfg['maxIterations'] == 36 and cp['parameters']['maxIterations'] == 36
            and reference['parameters']['maxIterations'] == 32, 'Iteration-budget distinction changed')
    require('correctInitialBoundary' not in cfg and 'projectionFloor' not in cfg,
            'Original defaults changed')
    require(canonical(cp['cutHeight']) == canonical(definitions['target_height']), 'Goal labels differ')
    states, raw_node, raw_states = cp['states'], cp['rawNode'], cp['rawStates']
    require(len(states) == 865 and all(len(row) == 30 and all(map(finite, row)) for row in states),
            'Invalid actual warm state dimensions or scalar types')
    require(canonical(raw_node) == canonical(reference['rawNode']) and len(raw_node) == 13
            and all(isinstance(n, int) and not isinstance(n, bool) for n in raw_node),
            'Raw node layout/type differs')
    require(len(raw_states) == 13 and all(len(row) == 30 and all(map(finite, row)) for row in raw_states)
            and canonical(raw_states) == canonical([states[n] for n in raw_node]),
            'Raw states are not the exact finite typed extraction')
    require(warm['status'] == 'UNSOLVED_HARMONIC_WARM_ONLY' and warm['actual_solver_runs'] == 0,
            'Input is not explicitly an untested warm')
    require(len(warm['definition_bindings']) == 77, 'Wrong seed definition count')
    for row in warm['definition_bindings']:
        require(ident(local(row['path'])) == row, 'Prepared seed binding changed')
    report = {
        'status': 'PASS_STATIC_RUNNER_V2_AND_REAL_PREPARED_INPUT_METADATA',
        'checker': ident(__file__), 'inputs': pinned,
        'v1_v2_main_ast_identical': True, 'single_port_solve_call_count': 1,
        'single_call_goal_copy_jacobian_true_audit_true': True,
        'authority_bindings_rehashed': 66, 'prepared_seed_bindings_rehashed': 77,
        'typed_nonio_configuration_equal': True, 'typed_nonrun_parameter_signature_equal': True,
        'exact_parameter_differences': sorted(differences),
        'reference_maxIterations': 32, 'actual_configuration_maxIterations': 36,
        'actual_warm_state_shape': [865, 30], 'actual_warm_raw_shape': [13, 30],
        'typed_raw_state_extraction_equal': True, 'typed_goal_equal': True,
        'wrapper_or_prepare_function_called': False, 'solver_client_module_imported': False,
        'root_flow_solver_backend_calls': 0, 'new_candidate_or_positive_response_created': False,
        'actual_future_response_validated': False,
        'independence_scope': 'The reviewer authored the prepared warm. This checker supplies '
                              'independent review of the other author\'s wrapper and actual interface '
                              'compatibility only; the warm construction itself has a separate peer review.',
        'README_complete': False}
    data = (json.dumps(report, indent=2, ensure_ascii=False, allow_nan=False)+'\n').encode()
    with args.out.open('xb') as stream:
        stream.write(data)
    print(json.dumps({'status':report['status'], 'out_sha256':hashlib.sha256(data).hexdigest(),
                      'root_flow_solver_backend_calls':0}))


if __name__ == '__main__':
    main()
