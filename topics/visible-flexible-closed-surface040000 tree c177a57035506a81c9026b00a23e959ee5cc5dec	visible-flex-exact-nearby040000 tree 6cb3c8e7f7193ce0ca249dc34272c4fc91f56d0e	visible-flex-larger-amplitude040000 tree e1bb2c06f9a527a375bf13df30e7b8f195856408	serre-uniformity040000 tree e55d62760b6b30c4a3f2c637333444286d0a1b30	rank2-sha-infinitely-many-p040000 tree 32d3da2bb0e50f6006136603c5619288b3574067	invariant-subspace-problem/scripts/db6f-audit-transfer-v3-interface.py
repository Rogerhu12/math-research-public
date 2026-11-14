#!/usr/bin/env python3
"""Independent metadata-only audit of the explicit background transfer v3.

This checks source equivalence, parameter rejection cases and the already
closed quarter-amplitude checkpoint. It never builds a radial grid, calls
the transfer path, evaluates a finite map or starts a root/flow/solver.
"""
import argparse
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
REPO = TOPIC.parent.parent
EXPECTED = {
    'db6f-root-transfer-background.py': '35aa82514ec2be4b78cf3670e97343d0ba50085a7a6a687273108fbb6eb09705',
    'db6f-tail-transfer-background-v2.py': '7e58e063788127e3f6f5ed609c4851d395436aa22da421e8e0d320eff527b184',
    'db6f-tail-transfer-background-v3.py': 'bdf6307fd93328b1ae70923caac2687fa19b0187ca9c723fe5d7072d7799a47b',
}
AUTHOR_PREFLIGHT_SHA = '1e5a70147345f2acb83c6d491df70e4843daeff685077b96dce59be28fd7a519'
POLICY_SHA = '2b4fd1d141d9116157037d05748ab2a019c9033441453ee8e6ab917eb355eae3'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def check(condition, message):
    if not condition:
        raise ValueError(message)


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


def function(tree, name):
    return next(node for node in tree.body
                if isinstance(node, ast.FunctionDef) and node.name == name)


def transfer_block(text):
    start = text.index('    left, right = [], []\n')
    endmark = '    data = write_npz(args.out_prefix, arrays)\n'
    end = text.index(endmark, start) + len(endmark)
    return ast.dump(ast.parse('def identical_transfer_math():\n' + text[start:end]),
                    include_attributes=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--author-preflight', type=Path, required=True)
    parser.add_argument('--replay-prefix', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    for path in (args.out, Path(str(args.replay_prefix)+'-preflight.json'),
                 Path(str(args.replay_prefix)+'.log'), Path(str(args.replay_prefix)+'.execution.json')):
        check(not path.exists(), 'Refusing to overwrite '+str(path))
    sources = {}
    for name, expected in EXPECTED.items():
        path = HERE/name
        check(sha(path) == expected, 'Changed frozen source '+name)
        sources[name] = {'file': str(path), 'sha256': expected}
    check(sha(args.author_preflight) == AUTHOR_PREFLIGHT_SHA, 'Changed author preflight')
    original_text = (HERE/'db6f-root-transfer-background.py').read_text()
    new_text = (HERE/'db6f-tail-transfer-background-v3.py').read_text()
    old_tree, new_tree = ast.parse(original_text), ast.parse(new_text)
    unchanged = []
    for name in ('check', 'sha', 'grid', 'fraction_vectors', 'affine_coefficients', 'write_npz'):
        check(ast.dump(function(old_tree, name), include_attributes=False) ==
              ast.dump(function(new_tree, name), include_attributes=False),
              'Changed mathematical helper '+name)
        unchanged.append(name)
    check(transfer_block(original_text) == transfer_block(new_text),
          'Changed physical intersections, affine coefficients or output-array arithmetic')
    before = module('independent_transfer_metadata_v2', HERE/'db6f-tail-transfer-background-v2.py')
    after = module('independent_transfer_metadata_v3', HERE/'db6f-tail-transfer-background-v3.py')
    original = module('independent_transfer_metadata_base', HERE/'db6f-root-transfer-background.py')
    expected_extra = {'iterationCheckpointFile', 'sharedEngines', 'trialDiagnosticFile', 'trialStatePrefix'}
    check(after.NUMERICAL_KEYS == original.NUMERICAL_KEYS | expected_extra,
          'The numerical-key set was changed beyond the four approved additions')
    check(after.parameter_policy_sha256() == POLICY_SHA, 'Policy canonical hash mismatch')
    # These are only dictionaries; no fake checkpoint, manifest or packet is saved.
    cases = [
        ('unchanged physical dictionary', {'rCut': .6}, {'rCut': .6}, True),
        ('four approved metadata keys', {'rCut': .6}, {'rCut': .6, 'iterationCheckpointFile': 'a',
             'sharedEngines': True, 'trialDiagnosticFile': 'b', 'trialStatePrefix': 'c'}, True),
        ('approved absent to null', {}, {'trialDiagnosticFile': None}, True),
        ('unknown added null', {}, {'unknownPhysical': None}, False),
        ('unknown removed null', {'unknownPhysical': None}, {}, False),
        ('unknown numeric change', {'unknownPhysical': 2}, {'unknownPhysical': 3}, False),
        ('physical radius change', {'rCut': .6}, {'rCut': .61}, False),
        ('source calibration integration count change', {'calibrationSteps': 512}, {'calibrationSteps': 1024}, False),
        ('physical cap change', {'wCut': .5}, {'wCut': .51}, False),
        ('nested physical controls change', {'valleyControls': [1., 2.]}, {'valleyControls': [1., 3.]}, False),
        ('false versus zero', {'unknownPhysical': False}, {'unknownPhysical': 0}, False),
        ('true versus one', {'unknownPhysical': True}, {'unknownPhysical': 1}, False),
        ('nested false versus zero', {'unknownPhysical': {'v': [False]}}, {'unknownPhysical': {'v': [0]}}, False),
        ('integer versus floating representation', {'unknownPhysical': 1}, {'unknownPhysical': 1.}, False),
        ('nonfinite value', {'unknownPhysical': float('nan')}, {'unknownPhysical': float('nan')}, False),
        ('shared flag integer', {}, {'sharedEngines': 1}, False),
        ('shared flag text', {}, {'sharedEngines': 'true'}, False),
        ('path boolean', {}, {'iterationCheckpointFile': False}, False),
        ('path array', {}, {'trialStatePrefix': []}, False),
    ]
    outcomes = []
    for label, old, new, expected in cases:
        error = None
        try:
            changed = after.check_parameters(old, new)
            accepted = True
        except (ValueError, TypeError) as exc:
            accepted, changed, error = False, None, str(exc)
        check(accepted is expected, 'Unexpected parameter result: '+label)
        outcomes.append({'case': label, 'accepted': accepted, 'expected': expected,
                         'changed_keys': changed, 'error': error})
    old_alias = before.check_parameters({'unknownPhysical': False}, {'unknownPhysical': 0})
    check(old_alias == [], 'The documented frozen-v2 type-alias example changed')
    try:
        after.bound_file(str(HERE/'db6f-root-transfer-background.py'), '0'*64, HERE)
    except ValueError:
        changed_bound_file_rejected = True
    else:
        raise ValueError('A wrong source-file digest was accepted')

    author = json.loads(args.author_preflight.read_text())
    command = [sys.executable, str(HERE/'db6f-tail-transfer-background-v3.py'),
               '--old-manifest', author['old_manifest'], '--packet', author['input_packet'],
               '--check-parameters-only', '--new-checkpoint', author['new_parameter_checkpoint'],
               '--out-prefix', str(args.replay_prefix.resolve())]
    started = time.time()
    run = subprocess.run(command, cwd=REPO, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                         text=True, check=False)
    elapsed = time.time()-started
    log = Path(str(args.replay_prefix)+'.log')
    log.write_text(run.stdout)
    replay = Path(str(args.replay_prefix)+'-preflight.json')
    execution = {'argv': command, 'cwd': str(REPO), 'exit_code': run.returncode,
                 'elapsed_seconds': elapsed,
                 'peak_child_rss_bytes': resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss*1024,
                 'log_file': str(log), 'log_sha256': sha(log),
                 'actual_new_root_flow_solver_calls': 0, 'geometric_transfer_performed': False}
    execution_path = Path(str(args.replay_prefix)+'.execution.json')
    execution_path.write_text(json.dumps(execution, indent=2)+'\n')
    check(run.returncode == 0, 'Independent parameter-only preflight failed')
    check(replay.read_bytes() == args.author_preflight.read_bytes(),
          'Independent preflight did not reproduce the author metadata byte for byte')
    check(not any(key in author for key in ('finished', 'new_manifest', 'new_manifest_sha256',
                                           'finite_tail_manifest_sha256', 'data_file')),
          'Parameter preflight unexpectedly asserts a new geometry')
    check(author['geometric_transfer_performed'] is False and
          author['finite_map_was_created'] is False and author['actual_new_root_flow_solver_calls'] == 0,
          'Preflight scope flags disagree')
    report = {'status': 'independent-transfer-v3-interface-audit-pass',
              'script_sha256': sha(__file__), 'frozen_sources': sources,
              'policy_sha256': POLICY_SHA, 'unchanged_helper_AST': unchanged,
              'complete_transfer_array_block_AST_identical': True,
              'added_numerical_keys': sorted(expected_extra), 'parameter_guard_cases': outcomes,
              'frozen_v2_unknown_false_to_zero_was_incorrectly_accepted': True,
              'frozen_v3_rejects_that_alias': True,
              'wrong_bound_file_sha256_rejected': changed_bound_file_rejected,
              'author_preflight': {'file': str(args.author_preflight), 'sha256': sha(args.author_preflight)},
              'independent_preflight': {'file': str(replay), 'sha256': sha(replay)},
              'preflight_bytes_identical': True,
              'observed_execution': {'file': str(execution_path), 'sha256': sha(execution_path)},
              'actual_new_root_flow_solver_calls': 0, 'geometric_transfer_performed': False,
              'finite_map_was_created': False,
              'scope': 'Source/parameter/identity interface only; analytic packet validity remains its reviewed input premise. No new transfer output or finite-map metric/curvature is certified.'}
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps({'status': report['status'], 'parameter_guard_cases': len(outcomes),
                      'preflight_bytes_identical': True, 'exit_code': run.returncode,
                      'geometric_transfer_performed': False}))


if __name__ == '__main__':
    main()
