#!/usr/bin/env python3
"""Resume the actual83b0 terminal on its proposed369 original row library.

The original physical solver, finite material, fine observer and stage gates
are reused. Only the saved terminal and its accumulated costs are advanced.
"""
import hashlib
import json
from pathlib import Path
import sys

PARENT_SHA256 = 'bb1dee6b1b15414dfb8c2baf449bbe28e4b48ac2262c5e8a027fd7fe852ec858'
PARENT_REQUEST_SHA256 = 'ca90b9175f4b53ed5e48495f15c3a932a7ea258f2440402f55f3c6bb81589c12'
PARENT_FINAL_SHA256 = '95296e93aed2c7abb4c19e30fb486d57d565068d353032dd1d52e2656ea6791c'
HERE = Path(__file__).resolve().parent
if hashlib.sha256((HERE/'r582_physical_pending357_resume_20261127.py').read_bytes()).hexdigest() != PARENT_SHA256:
    raise RuntimeError('published pending357 source differs')
import r582_physical_pending357_resume_20261127 as parent

driver = parent.driver
SCHEMA = 'r582-actual83b0-original369-continuation-v1'
INPUT_SCHEMA = 'r582-complete-pending357-terminal-input-v1'
original_emit = driver.emit


def load_input(raw, digest):
    encoded = sys.stdin.buffer.read() if raw == '@stdin' else raw.encode()
    if hashlib.sha256(encoded).hexdigest() != digest:
        raise ValueError('complete original terminal input differs')
    incoming = json.loads(encoded)
    if incoming['schema'] != INPUT_SCHEMA:
        raise ValueError('wrong terminal input schema')
    previous_path = HERE.parent/'computations/request-r582-physical-pending357-resume-20261127.json'
    previous_bytes = previous_path.read_bytes()
    if hashlib.sha256(previous_bytes).hexdigest() != PARENT_REQUEST_SHA256:
        raise ValueError('published parent request differs')
    previous = json.loads(previous_bytes)['lanes']['actual-95de-0d-pending357']['source_state_json']
    source, paid, oldfine = parent.load_input(previous, hashlib.sha256(previous.encode()).hexdigest())
    final_bytes = incoming['complete_original_FINAL_JSON'].encode()
    if len(final_bytes) != 564998 or hashlib.sha256(final_bytes).hexdigest() != PARENT_FINAL_SHA256:
        raise ValueError('unique actual pending357 terminal differs')
    final = json.loads(final_bytes)
    origin = incoming['origin']
    if (origin['run_id'] != 45929007792 or origin['job_id'] != 140277011834
            or origin['source_commit'] != '2fa9aa4ad410935f4a7d398b5023c3915c0b126d'
            or origin['source_entry_sha256'] != PARENT_SHA256
            or origin['FINAL_JSON_sha256'] != PARENT_FINAL_SHA256
            or final['schema'] != parent.SCHEMA or final['stage'] != 0
            or final['termination'] != 'scientific_clock_checkpoint_not_complete'
            or final['stalled_outer_count'] != 0 or final['phase'] != 'metric'):
        raise ValueError('actual source terminal or phase differs')
    actual = driver.np.asarray(final['actual_constraint_radial_nodes'], dtype=float)
    fine = driver.np.asarray(final['actual_fine_radial_nodes'], dtype=float)
    proposed = driver.np.asarray(final['proposed_constraint_radial_nodes'], dtype=float)
    pending = driver.np.asarray(final['pending_radial_nodes'], dtype=float)
    retained = final['actual_retained_state']
    if (len(actual) != 365 or len(fine) != 16256 or len(proposed) != 369
            or not set(actual).issubset(set(proposed))
            or set(proposed)-set(actual) != set(pending)
            or not set(oldfine).issubset(set(fine))
            or not set(actual).issubset(set(fine))
            or final['actual_constraint_theta_nodes'] != 1536
            or final['actual_fine_theta_nodes'] != 3072
            or final['proposed_constraint_theta_nodes'] != 1536
            or final['pending_angular_upgrade'] or final['pending_angular_upgrade_evidence']
            or final['actual_backend_trust'] != 2. or final['proposed_next_trust'] != 2.
            or retained['q_identity'] != driver.identity(retained['q'])
            or retained['q_identity']['binary64_sha256'] !=
                '83b0af72af30e2a19fa3ffe80d4e254adfe6037b3b12ec235ca4c11523c19725'
            or not retained['qualified_on_this_fine_grid'] or retained['p'] != .181
            or retained['scan']['radial_grid_identity'] != driver.identity(fine)
            or not retained['scan']['complete_fine_scan']
            or retained['scan']['geometry_violation_max'] != 0.
            or retained['scan']['working_geometry_violation_max'] != 0.):
        raise ValueError('actual accepted point or full row library differs')
    state = {name: final[name] for name in (
        'actual_retained_state','actual_constraint_radial_nodes','actual_constraint_theta_nodes',
        'actual_fine_radial_nodes','actual_fine_theta_nodes','proposed_constraint_radial_nodes',
        'proposed_constraint_theta_nodes','pending_radial_nodes','pending_angular_upgrade',
        'pending_angular_upgrade_evidence','actual_backend_trust','proposed_next_trust')}
    state.update(actual_constraint_radial_identity=driver.identity(actual),
        actual_fine_radial_identity=driver.identity(fine),
        source_qualified_fine_identity=dict(retained['scan']['radial_grid_identity']),
        source_actual_material_mesh_sha256=final['field_receipt']['material_mesh_binary64_sha256'],
        paid_97q_directional_check=source['resume97_state']['paid_97q_directional_check'])
    ledger = {name: final[name] for name in (
        'counts','new_model_counts','R604_observation_counts',
        'current_backend_cost_not_yet_folded_into_completed_outers',
        'final_resonant_field_counts','final_stable_evaluator_counts','original_model_new_counts')}
    ledger.update(new_scientific_seconds=final['elapsed_seconds'],source_run=origin['run_id'],
        source_job=origin['job_id'],original_raw_sha256=origin['original_raw_sha256'],
        original_FINAL_JSON_sha256=PARENT_FINAL_SHA256,
        completed_and_unclosed_source_work_all_retained=True,
        source_backend_internal_work_arrays_not_available=True)
    source['resume97_origin'], source['resume97_state'] = origin, state
    source['resume97_input_sha256'] = digest
    source['unqualified_warm_backend_trial'] = final['last_backend_callback_candidate']
    source['prior_cost_ledger']['physical_pending357_original_terminal'] = ledger
    return source, paid, fine


def emit(tag, value):
    if tag == 'FINITE_LOCAL_TAIL_DEFINITION':
        value = dict(value)
        for key in ('source_49_backend_callbacks_are_not_replayed',
                    'source_warm_trial_has_no_fine_or_geometry_qualification',
                    'original_source_unadopted_proposal'):
            value.pop(key, None)
        value.update(schema=SCHEMA, original_source_actual_grid=[365,1536],
            first_new_grid=[369,1536], all_source16256_fine_radial_locations_preserved=True,
            source_actual_retained83b0_not_unqualified_raw8fa82=True,
            source17_complete_Jacobians_and8_unclosed_blocks_retained=True,
            source24_full_fine_scans_not_replayed=True,
            actual_new_material_identity_recorded_without_relabelling=True,
            original_physical_solver_and_stage_acceptance_unchanged=True)
    original_emit(tag, value)


def main():
    driver.load_input = load_input
    driver.emit = emit
    driver.SCHEMA = SCHEMA
    driver.main()


if __name__ == '__main__':
    main()
