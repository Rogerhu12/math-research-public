#!/usr/bin/env python3
"""Resume the actual completed physical/epigraph run without replaying its work.

Only the identified input loader and ancestry metadata are new.  The bound
scientific implementation keeps every original physical/metric/fine gate.
The last raw callback is a separate unqualified warm optimizer trial; the
actual fully scanned retained q remains the authoritative physical state.
"""
import hashlib
import json
from pathlib import Path
import sys

PARENT_SHA256 = 'c0c5c1c82808ea7b54ad68cc5bfee0a921726dc2bf8dfa2ac725600859133e02'
parent_path = Path(__file__).with_name('r582_physical_epigraph_continuation_20261127.py')
if hashlib.sha256(parent_path.read_bytes()).hexdigest() != PARENT_SHA256:
    raise RuntimeError('paid physical/epigraph scientific implementation changed')
import r582_physical_epigraph_continuation_20261127 as driver

SCHEMA = 'r582-actual243x1536-physical-epigraph-paid-resume-v1'
INPUT_SCHEMA = 'identified-physical-epigraph-terminal97q-with-new-warm-trial-v1'
original_load_input = driver.load_input
original_emit = driver.emit


def load_input(raw, digest):
    data = sys.stdin.buffer.read() if raw == '@stdin' else raw.encode()
    if hashlib.sha256(data).hexdigest() != digest:
        raise ValueError('new actual243 physical continuation input digest differs')
    incoming = json.loads(data)
    if incoming.get('schema') != INPUT_SCHEMA:
        raise ValueError('actual physical continuation input schema differs')
    origin = incoming['origin']
    required = {'run_id':45881470977,'job_id':140121595702,
        'source_commit':'fe523e5c0dc316df8b8434fe5aa446cbe8b98360',
        'runtime_public_pull_commit':'0720176a40c71fa09c20f668f4d610482342c2af',
        'source_driver_sha256':PARENT_SHA256,
        'original_raw_bytes':10934304,
        'original_raw_sha256':'f1b49317722553d2af94e1666610f02904f03a6b88ff3ce14c16622e6ce6dd66',
        'FINAL_JSON_bytes':470115,
        'FINAL_JSON_sha256':'6138076e84aacbbd24e7ad46b4cb9e8db576cf0f5a3fb22305666b878f3f6b4f',
        'source_state_sha256':'4311d0a03166ee5b75d51a4e918c073fece1d1c11a9e033b8d1b6bd0c6efea1d',
        'termination':'scientific_clock_checkpoint_not_complete'}
    if origin != required:
        raise ValueError('original physical/epigraph terminal identity differs')
    source,paid,oldfine = original_load_input(incoming['original_source_state_json'],
                                             origin['source_state_sha256'])
    state = incoming['resume97_state']
    actual = driver.np.asarray(state['actual_constraint_radial_nodes'],dtype=float)
    fine = driver.np.asarray(state['actual_fine_radial_nodes'],dtype=float)
    if (driver.identity(actual) != state['actual_constraint_radial_identity']
            or len(actual) != 243 or state['actual_constraint_theta_nodes'] != 1536
            or state['actual_constraint_radial_identity']['binary64_sha256'] !=
               '30008c5092c32a76d539b3c9ae7059af04cc1d49e4206fc42f157ca22bc7b735'
            or driver.identity(fine) != state['actual_fine_radial_identity']
            or len(fine) != 11025 or state['actual_fine_theta_nodes'] != 3072
            or state['actual_fine_radial_identity']['binary64_sha256'] !=
               '52fb28eafcee0110ac12d989a96f6f33871ab395b6b2c3bd448a73a90196fe4a'
            or not set(oldfine).issubset(set(fine))
            or not set(actual).issubset(set(fine))
            or not driver.np.all(driver.np.diff(actual)>0)
            or not driver.np.all(driver.np.diff(fine)>0)
            or actual[0] != 0 or actual[-1] != .9 or fine[0] != 0 or fine[-1] != .9
            or state['pending_radial_nodes'] or state['pending_angular_upgrade']
            or state['actual_backend_trust'] != 2. or state['proposed_next_trust'] != 2.):
        raise ValueError('actual243x1536/complete11025x3072/trust/pending differs')
    retained = state['actual_retained_state']
    if (retained['q_identity'] != driver.identity(retained['q'])
            or retained['q_identity']['binary64_sha256'] !=
               'f1c8298e0c7c576c1b2230b24146fbe2356e97d7ba0b7b3428dd9e87e53a52bf'
            or retained['p'] != .181 or not retained['qualified_on_this_fine_grid']
            or retained['accepted_as'] != 'complete_fine_feasible_metric_improvement'
            or retained['scan']['radial_grid_identity'] != driver.identity(fine)
            or retained['scan']['theta_nodes'] != 3072
            or not retained['scan']['complete_fine_scan']
            or retained['scan']['eta_max'] != 6.262308445465524e-05
            or retained['scan']['geometry_violation_max'] != 0.
            or retained['scan']['working_geometry_violation_max'] != 4.259917071869346e-13):
        raise ValueError('actual fully scanned retained state changed')
    warm = incoming['unqualified_warm_backend_trial']
    if (driver.identity(warm['q']) != warm['q_identity']
            or warm['q_identity']['binary64_sha256'] !=
               'c491ecf294e2447f44d7a4e844906c1843c1a1c4cee9bfad5c238f0c73ff3e90'
            or warm['actual_constraint_radial_identity'] != driver.identity(actual)
            or warm['actual_constraint_theta_nodes'] != 1536
            or warm['p'] != .181 or warm['backend_extra'] != 6.23866913861634e-05
            or warm['current_complete_backend_violation'] != 1.7849159615642546e-07
            or warm['complete_fine_assessment'] or warm['retained_by_this_raw_callback']
            or warm['current_complete_backend_feasible']):
        raise ValueError('unqualified source raw warm trial changed or was relabelled')
    ledger = incoming['new_paid_cost_ledger']
    if (ledger['new_scientific_seconds'] != 2370.210179923
            or ledger['counts']['completed_backend_Jacobians'] != 30
            or ledger['current_backend_cost_not_yet_folded_into_completed_outers']['complete_Jacobians'] != 2
            or ledger['counts']['accepted_metric'] != 17
            or ledger['counts']['accepted_geometry_restoration'] != 5
            or ledger['counts']['complete_fine_scans'] != 40):
        raise ValueError('original paid optimizer/fine/partial costs changed')
    state['proposed_constraint_radial_nodes'] = actual.tolist()
    state['paid_97q_directional_check'] = source['resume97_state']['paid_97q_directional_check']
    source['resume97_origin'],source['resume97_state'] = origin,state
    source['resume97_input_sha256'] = digest
    source['unqualified_warm_backend_trial'] = warm
    source['prior_cost_ledger']['physical_epigraph_original_terminal'] = ledger
    return source,paid,fine


def emit(tag,value):
    if tag == 'FINITE_LOCAL_TAIL_DEFINITION':
        value = dict(value)
        value.pop('source_49_backend_callbacks_are_not_replayed',None)
        value.pop('source_warm_trial_has_no_fine_or_geometry_qualification',None)
        value.update(schema=SCHEMA,
            original_source_actual_grid=[243,1536],first_new_grid=[243,1536],
            source32_Jacobians_and40_fine_scans_not_replayed=True,
            all11025_actual_fine_locations_and3072_angles_preserved=True,
            source_last_raw_trial_has_no_complete_fine_qualification=True,
            source_raw_current_physical_rows_are_not_a_complete_fine_certificate=True,
            source_actual_retained_q_is_the_new_f1c8298_state=True,
            scientific_functions_and_original_all_group_acceptance_unchanged=True)
    original_emit(tag,value)


def main():
    driver.load_input = load_input
    driver.emit = emit
    driver.SCHEMA = SCHEMA
    driver.main()


if __name__ == '__main__':
    main()
