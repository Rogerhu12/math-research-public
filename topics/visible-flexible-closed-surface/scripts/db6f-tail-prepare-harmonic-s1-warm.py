#!/usr/bin/env python3
"""Construct an UNSOLVED s=1 harmonic warm from the closed s=13/16 call9.

Pure input construction: no solver, root, flow, geometry or client is imported
or called. Existing records and the active continuation are never modified.
"""
import argparse
import copy
import gzip
import hashlib
import json
import math
from pathlib import Path

import numpy as np


SCRIPT = Path(__file__).resolve()
TOPIC = SCRIPT.parent.parent
REPO = SCRIPT.parents[3]
OLD_REPO = Path('/workspace/scratch/db6f0b0e7462/math-research')
NOTE = 'topics/visible-flexible-closed-surface/notes/'
PINS = {
    'source': (NOTE+'2026-11-09-db6f-prefix-flat-v17v18-m15-amplitude-continuation-02_tail_0009.json.gz',
               '78d7e112d4823a717d0f46549b9f88d11872dbe390f40f70d295278ed50320e8'),
    'config': (NOTE+'2026-11-09-db6f-prefix-flat-v17v18-m15-amplitude-continuation-02-config.json',
               '1e5fc1ae3e6ecd2200891ce6b9d6694d1bb93d05061cde1d2397ff8b85f76614'),
    'target': (NOTE+'2026-11-09-db6f-prefix-flat-v17v18-m15-affine-cut-predictor-from14q512.json.gz',
               '4a13e13223047c995acd855db93007ed57bf0471214229c62adb5d7543425190'),
    'audit': (NOTE+'2026-11-09-db6f-root-continuation02-call009-closed-audit-v2.json',
              '8ae901094b155204c4ead255fd8222290d45ac6e7e4124f0f19832b076c6b12b'),
    'launch': (NOTE+'2026-11-09-db6f-prefix-amplitude-resume02-launch.json',
               'b2e7371a89906a5f1048077eb2040fef8f2c0a58a136ef3812ab6cbc36b5310e'),
    'method': (NOTE+'2026-11-09-db6f-tail-harmonic-warm-interface.md',
               '194b992a7f13d73138b1c288e6e3c6e84d81af3a3b2f3561c3452ce64fbca5aa'),
    'method_sources': (NOTE+'2026-11-09-db6f-tail-harmonic-warm-interface-sources.json',
                       '831a302577935be71794d822b9f84884a0f14463036ca7e9a9c83cbd0f416fa4'),
}
IO_KEYS = {'initialCheckpoint', 'traceFile', 'iterationCheckpointFile',
           'trialDiagnosticFile', 'trialStatePrefix'}


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'),
                      ensure_ascii=True, allow_nan=False)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    path = Path(path)
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)


def local_path(value):
    """Relocate only paths inside this exact saved repository, never arbitrary IO."""
    path = Path(value)
    if path.is_absolute():
        try:
            relative = path.relative_to(REPO)
        except ValueError:
            relative = path.relative_to(OLD_REPO)
        path = REPO / relative
    else:
        path = REPO / path
    path = path.resolve()
    path.relative_to(REPO)
    return path


def binding(path):
    path = local_path(path)
    data = path.read_bytes()
    return {'path': path.relative_to(REPO).as_posix(),
            'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}


def finite_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def payload(value, compressed=False):
    data = (json.dumps(value, ensure_ascii=False, allow_nan=False,
                       separators=(',', ':') if compressed else None,
                       indent=None if compressed else 2)+'\n').encode()
    if compressed:
        data = gzip.compress(data, mtime=0)
    require(len(data) < 5_000_000, 'Per-file size limit exceeded')
    require(compressed or len(data) <= 1_000_000, 'Large text must be compressed')
    return data


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out-prefix', type=Path, required=True)
    ap.add_argument('--pilot-prefix', type=Path, required=True,
                    help='Reserve fresh IO paths only; no pilot is started')
    a = ap.parse_args()
    out, pilot = a.out_prefix.resolve(), a.pilot_prefix.resolve()
    for path in (out, pilot):
        path.relative_to((TOPIC/'notes').resolve())
        require(path.parent.is_dir(), 'Output directory must already exist')
        require(not any(path.parent.glob(path.name+'*')), 'Output or pilot stem already used')
    require(out != pilot, 'Construction and future pilot stems must differ')

    source_files = {}
    inputs = {}

    def add_bound(path, expected_sha=None, expected_bytes=None):
        row = binding(path)
        require(expected_sha is None or row['sha256'] == expected_sha,
                'Changed source binding: '+row['path'])
        require(expected_bytes is None or row['bytes'] == expected_bytes,
                'Changed source size: '+row['path'])
        previous = source_files.get(row['path'])
        require(previous is None or previous == row, 'Conflicting source identity')
        source_files[row['path']] = row
        return row

    for key, (name, expected) in PINS.items():
        add_bound(name, expected)
        if key not in {'method', 'method_sources'}:
            inputs[key] = read(REPO/name)
    add_bound(SCRIPT)
    launch, audit = inputs['launch'], inputs['audit']
    require(len(launch['bound_files']) == 66, 'Unexpected full definition inventory')
    for row in launch['bound_files']:
        add_bound(row['path'], row['sha256'], row['bytes'])
    for row in audit['closed_files']:
        add_bound(row['path'], row['sha256'], row['bytes'])
    add_bound(audit['script']['path'], audit['script']['sha256'], audit['script']['bytes'])
    require(audit['status'] == 'PASS-closed-converged-finite-DN-provenance-and-request-audit',
            'Source closed audit did not pass')
    require(audit['call'] == 9 and audit['scale'] == 13/16,
            'Wrong closed source call or scale')

    record, cfg, target = inputs['source'], inputs['config'], inputs['target']
    response, cp = record['response'], record['response']['checkpoint']
    p = cp['parameters']
    require(canonical(record['config']) == canonical(cfg), 'Source configuration mismatch')
    require(response['converged'] is True and finite_number(response['residual'])
            and 0 <= response['residual'] < 2e-9, 'Source is not genuinely converged')
    require(record['request']['jacobian'] is False and record['request']['audit'] is False,
            'Unexpected source request semantics')
    require(canonical(response['residual']) == canonical(audit['residual']),
            'Source residual does not match its closed audit')
    require(set(cp) == {'parameters', 'states', 'rawNode', 'rawStates', 'cutHeight', 'scope'},
            'Unexpected source checkpoint schema')
    for name, expected in record['source_sha256'].items():
        require(Path(name).name == name, 'Source map is not a simple filename')
        add_bound(TOPIC/'scripts'/name, expected)
    require(len(record['source_sha256']) == 8, 'Unexpected response source map')

    native = {'modes': 15, 'spacing': 3, 'depth': 864, 'physicalDepth': 12,
              'shootingParts': 8, 'steps': 32, 'quadrature': 256,
              'projectionFloor': .05, 'linearFar': 32, 'linearSteps': 256,
              'linearMethod': 'stable-momentum-cusp-subdivision',
              'rhsEvaluation': 'split-linear-flux-v1', 'nodeIndex': 0}
    for key, expected in native.items():
        require(key in p and canonical(p[key]) == canonical(expected), 'Wrong native slot: '+key)
    cfg_native = {'modes': 15, 'spacing': 3, 'depth': 12, 'shootingParts': 8,
                  'steps': 32, 'quadrature': 256, 'linearFar': 32, 'linearSteps': 256,
                  'linearMethod': 'projective', 'solveTolerance': 2e-9, 'maxIterations': 36,
                  'harmonicAmplitudePredictor': True}
    for key, expected in cfg_native.items():
        require(key in cfg and canonical(cfg[key]) == canonical(expected), 'Wrong original config: '+key)
    require('correctInitialBoundary' not in cfg and 'projectionFloor' not in cfg,
            'Default boundary correction or floor was overridden')
    require(target['config']['modes'] == 15 and target['config']['actual_nonlinear_tail'] is False,
            'Wrong fixed auxiliary target')
    for key, value in target['physical_tail_parameters'].items():
        require(key in cfg and canonical(cfg[key]) == canonical(value),
                'Physical target/config mismatch: '+key)

    M, N = 15, 865
    old_states, raw_node = cp['states'], cp['rawNode']
    require(isinstance(old_states, list) and len(old_states) == N,
            'Expected 865 staged nodes')
    require(all(isinstance(row, list) and len(row) == 2*M and all(map(finite_number, row))
                for row in old_states), 'Wrong Q/Pi slots or nonfinite/bool state')
    require(isinstance(raw_node, list) and len(raw_node) == 13
            and all(isinstance(n, int) and not isinstance(n, bool) and n == 72*i
                    for i, n in enumerate(raw_node)), 'Wrong raw-node map')
    require(cp['rawStates'] == [old_states[n] for n in raw_node], 'Raw state/source state mismatch')
    goal_list = target['predicted_cut_height']
    require(isinstance(goal_list, list) and len(goal_list) == M
            and all(finite_number(v) and v != 0 for v in goal_list), 'Wrong physical target slots')
    goal = np.asarray(goal_list, dtype=np.float64)
    powers = np.arange(1, M+1)
    s0, s1 = np.float64(13/16), np.float64(1)
    expected_old = goal * s0**powers
    require(np.array_equal(np.asarray(record['request']['height']), expected_old),
            'Source request is not the exact original s=13/16 path')
    require(cp['cutHeight'] == record['request']['height'], 'Source target labels disagree')

    ratio = np.float64(s1/s0)
    factors = ratio**powers
    require(np.all(np.isfinite(factors)) and np.all(factors > 0), 'Invalid harmonic factors')
    original_state = np.asarray(old_states, dtype=np.float64)
    candidate = np.empty_like(original_state)
    with np.errstate(over='raise', invalid='raise'):
        candidate[:, :M] = original_state[:, :M] * factors[None, :]
        candidate[:, M:] = original_state[:, M:] * factors[None, :]
    require(np.all(np.isfinite(candidate)), 'Transformed state is not finite')
    states = candidate.tolist()
    new_height = goal.copy().tolist()
    require(new_height == goal_list, 's=1 target must be an exact goal copy')
    new_cp = {
        'parameters': copy.deepcopy(p), 'states': states, 'rawNode': raw_node.copy(),
        'rawStates': [states[n].copy() for n in raw_node], 'cutHeight': new_height,
        'scope': 'UNSOLVED HARMONIC WARM ONLY. Q_j and stored Pi_j were multiplied by '
                 '(1/(13/16))^j for j=1..15. cutHeight is the requested s=1 physical '
                 'height label, not a measured cut jet of this state. Original default '
                 'correctInitialBoundary must remain enabled. No root, flow or solve '
                 'has evaluated this state; all old convergence, jets, Jacobian and audit '
                 'results are invalid and were not copied.'}
    require(canonical(new_cp['parameters']) == canonical(p), 'Parameter copy changed')
    require(new_cp['rawStates'] == [new_cp['states'][n] for n in raw_node], 'New raw slots disagree')

    bindings = [source_files[key] for key in sorted(source_files)]
    for row in bindings:
        require(binding(row['path']) == row, 'Source changed while preparing')
    definitions_hash = hashlib.sha256(canonical(bindings).encode()).hexdigest()
    transform = {'coordinates': 'row[0:15]=Q_1..Q_15; row[15:30]=stored Pi_1..Pi_15',
                 'rule': 'gamma_j=(binary64(1)/binary64(13/16))**j; Q and Pi use the same gamma_j',
                 'mode_index': 'j=1..15, not the angular frequency 3*j',
                 'ratio_hex': float(ratio).hex(), 'factor_hex': [float(v).hex() for v in factors],
                 'numpy_version': np.__version__, 'target_rule': 'goal.copy(); no accumulated rescaling'}
    warm = {'status': 'UNSOLVED_HARMONIC_WARM_ONLY', 'preparation_only': True,
            'actual_solver_runs': 0, 'source_checkpoint': PINS['source'][0],
            'source_checkpoint_sha256': PINS['source'][1],
            'source_target_prefix': PINS['target'][0], 'source_target_prefix_sha256': PINS['target'][1],
            'source_scale': float(s0), 'target_scale': float(s1), 'transformation': transform,
            'definition_bindings': bindings, 'definition_bindings_sha256': definitions_hash,
            'checkpoint': new_cp}
    require(not {'response', 'request', 'seam', 'converged', 'residual', 'history', 'jets',
                 'heightJetJacobian', 'audit'}.intersection(warm), 'Stale result leaked into warm')

    cp_path, cfg_path = Path(str(out)+'-input.json.gz'), Path(str(out)+'-config.json')
    interface_path, prep_path = Path(str(out)+'-interface.json'), Path(str(out)+'-preparation.json')
    io = {'initialCheckpoint': str(cp_path), 'traceFile': str(pilot)+'-trace.jsonl',
          'iterationCheckpointFile': str(pilot)+'-iteration.json.gz',
          'trialDiagnosticFile': str(pilot)+'-trials.jsonl',
          'trialStatePrefix': str(pilot)+'-stage-input'}
    new_cfg = copy.deepcopy(cfg)
    new_cfg.update(io)
    differences = {key for key in set(cfg) | set(new_cfg)
                   if key not in cfg or key not in new_cfg or canonical(cfg[key]) != canonical(new_cfg[key])}
    require(differences == IO_KEYS, 'Only the five fresh IO fields may change')
    require('correctInitialBoundary' not in new_cfg and 'projectionFloor' not in new_cfg,
            'Preserve original default boundary/floor')
    encoded = {cp_path: payload(warm, True), cfg_path: payload(new_cfg)}
    output_bindings = [{'path': path.relative_to(REPO).as_posix(),
                        'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}
                       for path, data in encoded.items()]
    interface = {
        'status': 'PREPARED_INTERFACE_ONLY_NO_SOLVER_STARTED', 'configuration': str(cfg_path),
        'warm_input': str(cp_path), 'source_root': str(TOPIC/'repro/source-root'),
        'client': str(TOPIC/'scripts/db6f-prefix-tail-continuation-client.py'),
        'client_sha256': sha(TOPIC/'scripts/db6f-prefix-tail-continuation-client.py'),
        'class': 'WeightedTailPort', 'fresh_instance_required': True,
        'record_prefix': str(pilot)+'_tail', 'node_heap': 1536,
        'request': {'height_file': str(cp_path), 'height_key': 'checkpoint.cutHeight',
                    'height_equals_fixed_goal_copy': True, 'jacobian': True, 'audit': True},
        'call_count': 1, 'call_pattern': 'fresh WeightedTailPort; one solve(goal.copy(), jacobian=True, audit=True); finally close(); record actual process poll()',
        'no_solver_invoked': True, 'maxIterations': 36, 'solveTolerance': 2e-9,
        'projectionFloor': .05, 'correctInitialBoundary': 'original default enabled; key absent',
        'scope': 'A future standalone original finite-DN request only. This input is UNSOLVED; '
                 'even a successful future response is not a coupled prefix or geometry certificate. '
                 'Do not use this warm as continuation --resume-checkpoint. No active run is changed.',
        'source_bindings': bindings, 'input_output_bindings': output_bindings}
    encoded[interface_path] = payload(interface)
    outputs = [{'path': path.relative_to(REPO).as_posix(),
                'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}
               for path, data in encoded.items()]
    preparation = {
        'status': 'INPUTS_PREPARED_NO_SOLVER_EXECUTED', 'script': binding(SCRIPT),
        'inputs': {key: binding(REPO/name) for key, (name, _) in PINS.items()},
        'definition_bindings_count': len(bindings), 'definition_bindings_sha256': definitions_hash,
        'source_observed': {'call': 9, 'scale': float(s0), 'converged': True,
                            'residual': response['residual'], 'audit_requested': False},
        'candidate_status': 'UNSOLVED', 'transformation': transform,
        'states_shape': [N, 2*M], 'raw_states_shape': [13, 2*M],
        'raw_states_exactly_indexed': True, 'parameters_exact_source_copy': True,
        'target_exact_goal_copy': True, 'new_state_all_finite': True,
        'changed_configuration_keys': sorted(differences),
        'old_response_fields_not_copied': True, 'actual_solver_runs': 0,
        'root_flow_geometry_backend_calls': 0, 'active_files_modified': False,
        'outputs': outputs, 'README_complete': False}
    encoded[prep_path] = payload(preparation)
    require(all(not path.exists() for path in encoded), 'Refusing to overwrite construction output')
    for path, data in encoded.items():
        with path.open('xb') as stream:
            stream.write(data)
        require(path.read_bytes() == data, 'Written data do not match prepared bytes')
    print(json.dumps({'prepared_only': True, 'warm_input': str(cp_path),
                      'warm_sha256': sha(cp_path), 'config_sha256': sha(cfg_path),
                      'interface_sha256': sha(interface_path), 'preparation_sha256': sha(prep_path),
                      'definition_bindings_count': len(bindings), 'actual_solver_runs': 0}))


if __name__ == '__main__':
    main()
