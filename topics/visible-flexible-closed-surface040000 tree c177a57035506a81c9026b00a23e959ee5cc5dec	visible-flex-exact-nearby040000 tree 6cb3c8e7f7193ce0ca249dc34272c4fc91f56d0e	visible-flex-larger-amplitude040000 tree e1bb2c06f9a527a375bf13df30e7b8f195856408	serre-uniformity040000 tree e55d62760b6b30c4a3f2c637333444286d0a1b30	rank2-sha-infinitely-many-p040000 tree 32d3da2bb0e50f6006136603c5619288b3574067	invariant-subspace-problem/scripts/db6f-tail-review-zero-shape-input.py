#!/usr/bin/env python3
"""Read-only input audit: never imports or launches a solver."""
import argparse
import gzip
import hashlib
import json
import math
from pathlib import Path


def read(p):
    p = Path(p)
    b = p.read_bytes()
    return json.loads(gzip.decompress(b) if p.suffix == '.gz' else b)


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--launch', type=Path, required=True)
    ap.add_argument('--preparation', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    a = ap.parse_args()
    launch, prep = read(a.launch), read(a.preparation)
    assert launch['status'] == 'PREPARED_ONLY_NO_SOLVER_STARTED'
    assert prep['actual_solver_runs'] == 0
    assert prep['original_worker_or_controller_modified'] is False
    for row in launch['bound_files']:
        assert sha(row['path']) == row['sha256'], row['path']
        assert Path(row['path']).stat().st_size == row['bytes']
    for row in prep['inputs'] + prep['outputs']:
        assert sha(row['path']) == row['sha256'], row['path']
    cmd = launch['command']
    get = lambda option: cmd[cmd.index(option) + 1]
    cfgp, cpp = Path(get('--config')), Path(get('--checkpoint'))
    cfg, rec = read(cfgp), read(cpp)
    cp = rec['checkpoint']
    original = read(prep['inputs'][0]['path'])
    prior = read(rec['source_checkpoint'])['checkpoint']
    prefix = read(rec['source_target_prefix'])
    assert sha(rec['source_checkpoint']) == rec['source_checkpoint_sha256']
    assert sha(rec['source_target_prefix']) == rec['source_target_prefix_sha256']
    assert rec['status'] == 'UNCONVERGED_ZERO_SHAPE_FIXED_NONZERO_TARGET'
    assert rec['preparation_only'] is True and rec['actual_solver_runs'] == 0
    assert cp['parameters'] == prior['parameters']
    assert cp['rawNode'] == prior['rawNode']
    assert len(cp['states']) == len(prior['states']) == 865
    assert all(len(row) == 30 and all(type(v) in (int, float) and v == 0 for v in row)
               for row in cp['states'])
    assert cp['rawStates'] == [cp['states'][n] for n in cp['rawNode']]
    assert cp['cutHeight'] == prior['cutHeight']
    goal = prefix['predicted_cut_height']
    assert len(goal) == len(cp['cutHeight']) == 15
    assert all(cp['cutHeight'][j] == math.ldexp(goal[j], -2 * (j + 1)) for j in range(15))
    assert cp['cutHeight'][0] != 0 and all(math.isfinite(v) for v in cp['cutHeight'])
    assert cp['cutHeight'][0] / cp['cutHeight'][0] == 1
    assert cfg['correctInitialBoundary'] is False
    assert cfg['initialCheckpoint'] == str(cpp.resolve())
    assert cfg['maxIterations'] == int(get('--max-iterations')) == 8
    assert cfg['solveTolerance'] == original['solveTolerance'] == 2e-9
    p = cp['parameters']
    assert (p['modes'], p['quadrature'], p['physicalDepth'], p['shootingParts'], p['steps'], p['projectionFloor']) == (15, 256, 12, 8, 32, .05)
    changed = sorted(k for k in set(cfg) | set(original) if cfg.get(k) != original.get(k))
    allowed = {'initialCheckpoint', 'correctInitialBoundary', 'maxIterations', 'traceFile',
               'iterationCheckpointFile', 'trialDiagnosticFile', 'trialStatePrefix'}
    assert set(changed) <= allowed
    assert all(cfg[k] == original[k] for k in original if k not in allowed)
    target_q = [v / cfg['rCut']**4 for v in cp['cutHeight']]
    scale = max(1e-250, *map(abs, target_q))
    predicted_cut_norm = max(abs(v) / scale for v in target_q)
    assert predicted_cut_norm == 1
    result = dict(
        status='PASS_STATIC_INPUT_BINDING_ONLY', actual_root_calls=0, actual_solver_runs=0,
        launch_sha256=sha(a.launch), preparation_sha256=sha(a.preparation),
        script_sha256=sha(__file__), input_sha256=sha(cpp), config_sha256=sha(cfgp),
        checked_bound_files=len(launch['bound_files']), zero_shape_nodes=865, shape_dimension=30,
        raw_node_count=len(cp['rawNode']), cut_height_matches_source_request=True,
        quarter_scaling_checked_by_ldexp=True, warm_ratio=1, correct_initial_boundary=False,
        changed_config_keys=changed, predicted_cut_normalized_residual=predicted_cut_norm,
        measured_full_shooting_residual=None,
        scope='Pure JSON/hash/source-input audit. The full zero-shape/root/RK identity is a separate static proof. No solver or stage flow was executed.')
    if a.out.exists():
        raise FileExistsError(a.out)
    a.out.write_text(json.dumps(result, indent=2, allow_nan=False) + '\n')
    print(json.dumps({k: result[k] for k in ['status', 'checked_bound_files', 'zero_shape_nodes', 'shape_dimension', 'predicted_cut_normalized_residual', 'actual_solver_runs']}))


if __name__ == '__main__':
    main()
