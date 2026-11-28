#!/usr/bin/env python3
"""Resume the actual 401-row run at the interrupted physical half-step."""
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
PARENT_SOURCE = HERE / 'r582_6e91_original390_resume_20261128.py'
PARENT_REQUEST = HERE.parent / 'computations/request-r582-6e91-original390-20261128.json'
PARENT_SHA256 = '0b0bce610865bb44c892b8b3e847553bf84d528fb0c37276f2e342963a12be3b'
PARENT_REQUEST_SHA256 = '1d27199dbbd3fe017e3f90913f5da607610584d18f39f044ef574c8b7f6a82c0'
INPUT_SHA256 = '67ca5469144dc76dff4d19c8ee42550ad2cfb816105c09d9d2bf1d80803251f0'
if hashlib.sha256(PARENT_SOURCE.read_bytes()).hexdigest() != PARENT_SHA256:
    raise RuntimeError('the original390 continuation source differs')
import r582_6e91_original390_resume_20261128 as parent

driver = parent.driver
SCHEMA = 'r582-actual4354-pendingc13d-original401-continuation-v1'
INPUT_SCHEMA = 'r582-4354-pending-c13d-required-terminal-input-v1'
original_emit = driver.emit


def load_input(raw, digest):
    encoded = sys.stdin.buffer.read() if raw == '@stdin' else raw.encode()
    if hashlib.sha256(encoded).hexdigest() != digest or digest != INPUT_SHA256:
        raise ValueError('the original390 terminal input differs')
    incoming = json.loads(encoded)
    if incoming['schema'] != INPUT_SCHEMA:
        raise ValueError('unexpected original390 terminal schema')
    previous_bytes = PARENT_REQUEST.read_bytes()
    if hashlib.sha256(previous_bytes).hexdigest() != PARENT_REQUEST_SHA256:
        raise ValueError('the original390 request differs')
    previous = json.loads(previous_bytes)['lanes']['actual6e91-original390']['source_state_json']
    source, paid, oldfine = parent.load_input(previous, hashlib.sha256(previous.encode()).hexdigest())

    state = incoming['terminal_state']
    origin = incoming['origin']
    retained = state['actual_retained_state']
    fine = driver.np.asarray(state['actual_fine_radial_nodes'], dtype=float)
    coarse = state['actual_constraint_radial_nodes']
    coarse_id = driver.identity(coarse)
    fine_id = driver.identity(fine)
    if (origin['run_id'] != 46125750420 or origin['job_id'] != 140919842900
            or origin['source_commit'] != '4482fcc2f767581c9b0e09ff0b086c08a204038e'
            or origin['source_entry_sha256'] != PARENT_SHA256
            or origin['source_state_sha256'] != parent.INPUT_SHA256
            or origin['FINAL_JSON_sha256'] != 'a3dc4b6162bbe1849da3ba6356a20a5a74d768ba0147e661eac28053ed1dbf92'
            or state['source_schema'] != parent.SCHEMA
            or state['stage'] != 0 or state['phase'] != 'metric'
            or state['termination'] != 'scientific_clock_checkpoint_not_complete'):
        raise ValueError('the run or terminal phase differs')
    if (coarse != state['proposed_constraint_radial_nodes'] or state['pending_radial_nodes']
            or state['pending_angular_upgrade'] or state['pending_angular_upgrade_evidence']
            or coarse_id != {'entries': 401, 'binary64_sha256': '04650f567de37017689535096d75f1e6b68cb48970dc6022c5688b6b7565145a'}
            or fine_id != {'entries': 16312, 'binary64_sha256': 'bc08a5b4a84ab1af1b688a2e117da65d3efc3b5e1de0cc12c37994e71e7a5692'}
            or not set(oldfine).issubset(set(fine))
            or state['actual_constraint_theta_nodes'] != 1536
            or state['proposed_constraint_theta_nodes'] != 1536
            or state['actual_fine_theta_nodes'] != 3072
            or state['actual_backend_trust'] != 2. or state['proposed_next_trust'] != 2.
            or state['stalled_outer_count'] != 0 or retained['p'] != .181
            or retained['q_identity'] != driver.identity(retained['q'])
            or retained['q_identity']['binary64_sha256'] != '4354ee43ae0a98bbffac485c27f826b82507acd18d999a9cf4534cbda430c9f5'
            or not retained['qualified_on_this_fine_grid'] or not retained['scan']['complete_fine_scan']
            or retained['scan']['radial_grid_identity'] != fine_id or retained['scan']['theta_nodes'] != 3072
            or state['source_actual_material_mesh_sha256'] != 'f60be03b0af36d5d182f21860fe69cef80439c12bb23562d63dc2b57648bf52c'):
        raise ValueError('the accepted 4354 baseline or actual library differs')
    raw_trial = incoming['last_raw_backend_callback']
    pending = incoming['actual_pending_physical_half_step']
    if (raw_trial['q_identity'] != driver.identity(raw_trial['q'])
            or raw_trial['q_identity']['binary64_sha256'] != 'df3e0b3b152f3db73ff492c4457981d2a4cedd99034c5159fa32c2140c5770a9'
            or raw_trial['current_complete_backend_feasible'] or raw_trial['retained_by_this_raw_callback']
            or pending['q_identity'] != driver.identity(pending['q'])
            or pending['q_identity']['binary64_sha256'] != 'c13d4621694b8374853c1b50cf11b399c7e6b4e3c64fe675f1ff3468f5eac9c8'
            or pending['q_identity'] != raw_trial['separate_assessment_q_identity']
            or pending['p'] != retained['p'] or pending['source_retained_q_identity'] != retained['q_identity']
            or pending['source_raw_q_identity'] != raw_trial['q_identity']
            or pending['physical_assessment_fraction'] != .5
            or pending['backend_extra'] != raw_trial['separate_assessment_epigraph']
            or pending['source_current_coarse_radial_identity'] != coarse_id
            or pending['source_complete_fine_qualification'] or pending['source_accepted']
            or pending['is_previous_raw_backend_point']):
        raise ValueError('the unfinished original physical half-step differs')
    state.update(actual_constraint_radial_identity=coarse_id, actual_fine_radial_identity=fine_id,
                 source_qualified_fine_identity=retained['scan']['radial_grid_identity'],
                 paid_97q_directional_check=source['resume97_state']['paid_97q_directional_check'])
    source['resume97_origin'], source['resume97_state'] = origin, state
    source['resume97_input_sha256'] = digest
    source['prior_cost_ledger']['physical_original390_terminal'] = incoming['new_terminal_cost_ledger']
    source['original390_last_raw_backend_callback'] = raw_trial
    source['original390_last_completed_full_scan_trial'] = incoming['last_completed_full_scan_trial']
    source['unqualified_warm_backend_trial'] = pending
    return source, paid, fine


def emit(tag, value):
    if tag == 'FINITE_LOCAL_TAIL_DEFINITION':
        value = dict(value)
        for key in ('source_49_backend_callbacks_are_not_replayed',
                    'source_warm_trial_has_no_fine_or_geometry_qualification',
                    'original_source_unadopted_proposal'):
            value.pop(key, None)
        value.update(schema=SCHEMA, original_source_actual_grid=[401, 1536],
                     first_new_grid=[401, 1536], actual_source_fine_grid=[16312, 3072],
                     new_scope='Continue the unfinished physical c13d half-step before the normal original401 solve',
                     source_initializer_is_original_physical_half_step=True,
                     source_c13d_complete_coarse_paid=True, source_c13d_complete_fine_paid=False,
                     source_c13d_paid_prefix_blocks_without_serialized_fields_or_accumulator=115,
                     source_c13d_paid_prefix_radial_points=14720, source_c13d_unread_radial_points=1592,
                     source_4354_complete_fine_baseline_available_for_identical_p_q_grid=True,
                     original_physical_solver_and_stage_acceptance_unchanged=True)
    original_emit(tag, value)


def main():
    driver.load_input = load_input
    driver.emit = emit
    driver.SCHEMA = SCHEMA
    driver.main()


if __name__ == '__main__':
    main()
