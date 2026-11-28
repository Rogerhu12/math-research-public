#!/usr/bin/env python3
"""Continue the real e781 terminal on its proposed 383-row library.

Only the required terminal state and cost ledger are transported.  The raw
completed log/FINAL stay reproducible by their source run and hashes.
"""
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
PARENT_SHA256 = '18658269aaf15402aa43a30bacaadbf9b9b1ae72769bd9ed7df931e4f3f40766'
PARENT_REQUEST_SHA256 = 'd94760e7d31d6e621693fe2b6557689ab926253e19425aab2e1835bc2f383866'
INPUT_SHA256 = 'fc2d21c8bfb87aa8ad1030eef351bc5093e57534ca421b2e6421472a5f0f9318'
FINAL_SHA256 = '9bf02d91947d9d7773777b30a7837dedda7ff3c8fc5163f727c21f6b9de209fb'
if hashlib.sha256((HERE/'r582_complete_terminal_resume_20261128.py').read_bytes()).hexdigest() != PARENT_SHA256:
    raise RuntimeError('the published original369 source differs')
import r582_complete_terminal_resume_20261128 as parent

driver = parent.driver
SCHEMA = 'r582-actuale781-original383-continuation-v1'
INPUT_SCHEMA = 'r582-e781-required-terminal-input-v1'
original_emit = driver.emit


def load_input(raw, digest):
    encoded = sys.stdin.buffer.read() if raw == '@stdin' else raw.encode()
    if hashlib.sha256(encoded).hexdigest() != digest or digest != INPUT_SHA256:
        raise ValueError('the required actual terminal input differs')
    incoming = json.loads(encoded)
    if incoming['schema'] != INPUT_SCHEMA:
        raise ValueError('wrong actual terminal input schema')
    previous_path = HERE.parent/'computations/request-r582-complete-terminal369-20261128.json'
    previous_bytes = previous_path.read_bytes()
    if hashlib.sha256(previous_bytes).hexdigest() != PARENT_REQUEST_SHA256:
        raise ValueError('the published parent request differs')
    previous = json.loads(previous_bytes)['lanes']['actual83b0-original369']['source_state_json']
    source, paid, oldfine = parent.load_input(previous, hashlib.sha256(previous.encode()).hexdigest())
    state, origin = incoming['terminal_state'], incoming['origin']
    if (origin['run_id'] != 46117791268 or origin['job_id'] != 140895379882
            or origin['source_commit'] != '9afd9379dd81ebc3d096a38550498b2d6e40d365'
            or origin['source_entry_sha256'] != PARENT_SHA256
            or origin['FINAL_JSON_sha256'] != FINAL_SHA256
            or state['source_schema'] != parent.SCHEMA
            or state['stage'] != 0 or state['phase'] != 'metric'
            or state['termination'] != 'scientific_clock_checkpoint_not_complete'
            or state['stalled_outer_count'] != 0):
        raise ValueError('source terminal provenance or phase differs')
    actual = driver.np.asarray(state['actual_constraint_radial_nodes'], dtype=float)
    fine = driver.np.asarray(state['actual_fine_radial_nodes'], dtype=float)
    proposed = driver.np.asarray(state['proposed_constraint_radial_nodes'], dtype=float)
    pending = driver.np.asarray(state['pending_radial_nodes'], dtype=float)
    retained = state['actual_retained_state']
    if (len(actual) != 379 or len(fine) != 16280 or len(proposed) != 383
            or not set(actual).issubset(set(proposed))
            or set(proposed)-set(actual) != set(pending)
            or not set(oldfine).issubset(set(fine))
            or not set(actual).issubset(set(fine))
            or state['actual_constraint_theta_nodes'] != 1536
            or state['actual_fine_theta_nodes'] != 3072
            or state['proposed_constraint_theta_nodes'] != 1536
            or state['pending_angular_upgrade'] or state['pending_angular_upgrade_evidence']
            or state['actual_backend_trust'] != 2. or state['proposed_next_trust'] != 2.
            or retained['q_identity'] != driver.identity(retained['q'])
            or retained['q_identity']['binary64_sha256'] !=
                'e781bd6d67eeda31b9e724ad4b7d57031ef2a8db2e7003de3cba948266151830'
            or not retained['qualified_on_this_fine_grid'] or retained['p'] != .181
            or retained['scan']['radial_grid_identity'] != driver.identity(fine)
            or not retained['scan']['complete_fine_scan']
            or retained['scan']['geometry_violation_max'] != 0.
            or retained['scan']['working_geometry_violation_max'] != 0.
            or state['source_actual_material_mesh_sha256'] !=
                '0d222bd12ce8a61d0c88264c6fb5c82066f0ca058855b5bf7a670a53b483a991'):
        raise ValueError('actual accepted point or complete row library differs')
    warm = incoming['last_raw_backend_callback']
    if (warm['q_identity'] != driver.identity(warm['q'])
            or warm['q_identity'] != retained['q_identity']
            or warm['p'] != retained['p']
            or warm['current_complete_backend_feasible']
            or not warm['retained_from_separate_assessment']
            or warm['separate_assessment_q_identity'] != retained['q_identity']
            or warm['separate_assessment_fraction'] != 1.
            or not warm['separate_assessment_complete_fine_assessment']):
        raise ValueError('raw epigraph point and separately accepted physical q differ')
    state.update(actual_constraint_radial_identity=driver.identity(actual),
        actual_fine_radial_identity=driver.identity(fine),
        source_qualified_fine_identity=dict(retained['scan']['radial_grid_identity']),
        paid_97q_directional_check=source['resume97_state']['paid_97q_directional_check'])
    ledger = incoming['new_terminal_cost_ledger']
    if (ledger['new_scientific_seconds'] != 2386.166259383
            or ledger['counts']['accepted_metric'] != 3
            or ledger['counts']['accepted_geometry_restoration'] != 1
            or ledger['counts']['completed_backend_Jacobians'] != 7
            or ledger['current_backend_cost_not_yet_folded_into_completed_outers']['complete_Jacobians'] != 4
            or ledger['counts']['complete_fine_scans'] != 18):
        raise ValueError('complete and current unclosed terminal costs differ')
    source['resume97_origin'], source['resume97_state'] = origin, state
    source['resume97_input_sha256'] = digest
    source['unqualified_warm_backend_trial'] = warm
    source['prior_cost_ledger']['physical_original369_terminal'] = ledger
    return source, paid, fine


def emit(tag, value):
    if tag == 'FINITE_LOCAL_TAIL_DEFINITION':
        value = dict(value)
        for key in ('source_49_backend_callbacks_are_not_replayed',
                    'source_warm_trial_has_no_fine_or_geometry_qualification',
                    'original_source_unadopted_proposal'):
            value.pop(key, None)
        value.update(schema=SCHEMA, original_source_actual_grid=[379,1536],
            first_new_grid=[383,1536], all_source16280_fine_radial_locations_preserved=True,
            actual_e781_q_has_complete_source_fine_qualification=True,
            source_raw98_epigraph_point_still_requires_original_assessment=True,
            source11_complete_Jacobians_and143_direction_blocks_retained=True,
            source18_full_fine_scans_not_replayed_as_new_results=True,
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
