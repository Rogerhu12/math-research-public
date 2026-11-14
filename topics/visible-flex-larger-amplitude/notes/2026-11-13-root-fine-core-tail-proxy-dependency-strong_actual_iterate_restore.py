"""Restore an unaccepted actual M+3 iterate under fresh output-only paths.

The original strict raw reader still verifies every field, coefficient,
chart, layout, tolerance and piece SHA.  This adapter permits precisely one
identity change: the tail-config SHA resulting from different output paths
or an explicit warm checkpoint.  Every other physical/numerical tail option
must be identical.  It never mutates an old manifest or accepts a solution.
"""
from __future__ import annotations
import gzip
import hashlib
import json
from pathlib import Path
from types import SimpleNamespace
import numpy as np
import root_raw_collocation as raw


IO_KEYS = {'traceFile', 'iterationCheckpointFile', 'trialDiagnosticFile', 'initialCheckpoint'}


def read(path):
    path = Path(path)
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def restore(path, prior_tail_config, current_tail_config, obj, tolerance):
    record = read(path)
    if (record.get('solver_success') is not False or record.get('physical_surface') is not False
            or record.get('raw_collocation_only') is not True):
        raise ValueError('This restoration accepts explicitly unaccepted raw states only')
    context = record['identity']['coupling_context']
    if not context.get('actual_augmented_three_control'):
        raise ValueError('The raw iterate is not the explicit actual M+3 layout')
    if sha(prior_tail_config) != context['tail_config_sha256']:
        raise ValueError('The prior tail-config bytes do not match the recovery point')
    old_cfg, new_cfg = read(prior_tail_config), read(current_tail_config)
    for key in (set(old_cfg) | set(new_cfg))-IO_KEYS:
        if old_cfg.get(key) != new_cfg.get(key):
            raise ValueError('An actual tail physical or numerical option changed on recovery: '+key)
    current_context = dict(obj.raw_recovery_context)
    if sha(current_tail_config) != current_context['tail_config_sha256']:
        raise ValueError('The live actual tail-config bytes do not match the object')
    expected_context = {**context, 'tail_config_sha256': current_context['tail_config_sha256']}
    if raw.canonical(expected_context) != raw.canonical(current_context):
        raise ValueError('Actual targets, coupling, baseline or another recovery context field changed')
    if len(record['parameter_state']) != obj.M+3:
        raise ValueError('The complete actual all-core plus control vector differs')
    obj.select(np.asarray(record['parameter_state']))
    current_identity = raw.identity(obj, SimpleNamespace(tol=tolerance))
    expected_identity = {**record['identity'], 'coupling_context': expected_context}
    if raw.canonical(current_identity) != raw.canonical(expected_identity):
        raise ValueError('The actual recovery changed physical profile, gauge, chart, layout or tolerance')
    # Run the original reader under the old context only for its strict
    # roundtrip checks, then restore the declared fresh I/O context.
    try:
        obj.raw_recovery_context = context
        solution, checked = raw.read(path, obj, SimpleNamespace(tol=tolerance))
    finally:
        obj.raw_recovery_context = current_context
    obj.select(solution.p)
    obj.initial(solution.p)
    info = dict(scope=__doc__, file=str(path), sha256=sha(path),
        prior_tail_config=str(prior_tail_config), prior_tail_config_sha256=sha(prior_tail_config),
        current_tail_config=str(current_tail_config), current_tail_config_sha256=sha(current_tail_config),
        output_or_warm_only_config_changes={k: dict(old=old_cfg.get(k), new=new_cfg.get(k))
            for k in IO_KEYS if old_cfg.get(k) != new_cfg.get(k)},
        complete_x_y_p_cubic_hashes_checked=True, previous_solver_success=False,
        physical_surface=False, physical_and_numerical_tail_options_identical=True,
        new_full_H_nonlinear_tail_acceptance_required=True,
        original_final_gates_bypassed=False,
        prior_phase=checked.get('provenance', {}).get('phase'),
        prior_iteration=checked.get('provenance', {}).get('iteration'))
    return solution.x.copy(), solution.y.copy(), solution.p.copy(), info
