#!/usr/bin/env python3
"""Continue actual 4883 on its 0d material, adopting only the five paid pending rows."""
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
PARENT_SOURCE = HERE/'r582_4354_original401_resume_20261128.py'
PARENT_REQUEST = HERE.parent/'computations/request-r582-4354-original401-20261128.json'
PARENT_SHA = '8b977a48c9237e29282c4b8c8b7ef7a45cf094231744fff601d79909c77d1890'
PARENT_REQUEST_SHA = 'bcc3c70155cc42849c8fe11d55299934ef6130a2196aa01201a07ad50efc0836'
INPUT_SHA = '9503f85ae818d3ada343dc282e03a595b7945e579e25b24a5b39d6a7ff50eb22'
MATERIAL_SHA = '0d222bd12ce8a61d0c88264c6fb5c82066f0ca058855b5bf7a670a53b483a991'
SCHEMA = 'r582-actual4883-material-qualified-original412-continuation-v1'
INPUT_SCHEMA = 'r582-4883-material-bound-original412-required-terminal-v1'
if hashlib.sha256(PARENT_SOURCE.read_bytes()).hexdigest()!=PARENT_SHA:
    raise RuntimeError('the completed original401 entry differs')
import r582_4354_original401_resume_20261128 as parent
import r582_material_qualified_resume_guard_20261128 as material_guard

driver = parent.driver
original_emit = driver.emit


def load_input(raw,digest):
    encoded = sys.stdin.buffer.read() if raw=='@stdin' else raw.encode()
    if len(encoded)!=332187 or hashlib.sha256(encoded).hexdigest()!=digest or digest!=INPUT_SHA:
        raise ValueError('the actual completed original401 continuation input differs')
    incoming = json.loads(encoded)
    if incoming['schema']!=INPUT_SCHEMA:
        raise ValueError('unexpected actual4883 source schema')
    parent_bytes = PARENT_REQUEST.read_bytes()
    if hashlib.sha256(parent_bytes).hexdigest()!=PARENT_REQUEST_SHA:
        raise ValueError('the actual completed original401 request differs')
    previous = json.loads(parent_bytes)['lanes']['actual4354-pendingc13d-original401']['source_state_json']
    source,paid,oldfine = parent.load_input(previous,hashlib.sha256(previous.encode()).hexdigest())
    state,origin = incoming['terminal_state'],incoming['origin']
    retained = state['actual_retained_state']
    actual = driver.np.asarray(state['actual_constraint_radial_nodes'],float)
    fine = driver.np.asarray(state['actual_fine_radial_nodes'],float)
    proposed = driver.np.asarray(state['proposed_constraint_radial_nodes'],float)
    if (origin['run_id']!=46132385483 or origin['job_id']!=140940176202
            or origin['source_commit']!='56c35c4ca2d36e03831702cf1a4a1ba9ebb8efeb'
            or origin['source_entry_sha256']!=PARENT_SHA
            or origin['FINAL_JSON_sha256']!='040d2a82005380d26ca61a629e7bf4ce634d67f8f138d5371e0b2880d1b5b0d0'
            or state['source_schema']!=parent.SCHEMA or state['stage']!=0
            or state['phase']!='metric' or state['stalled_outer_count']!=0
            or state['termination']!='scientific_clock_checkpoint_not_complete'):
        raise ValueError('the actual terminal or phase differs')
    if (len(actual)!=407 or len(proposed)!=412 or len(fine)!=16321
            or not set(actual).issubset(set(proposed))
            or set(proposed)-set(actual)!=set(state['pending_radial_nodes'])
            or len(state['pending_radial_nodes'])!=5
            or not set(oldfine).issubset(set(fine)) or not set(actual).issubset(set(fine))
            or state['actual_constraint_theta_nodes']!=1536
            or state['proposed_constraint_theta_nodes']!=1536
            or state['actual_fine_theta_nodes']!=3072
            or state['pending_angular_upgrade'] or state['pending_angular_upgrade_evidence']
            or state['actual_backend_trust']!=2. or state['proposed_next_trust']!=2.
            or retained['q_identity']!=driver.identity(retained['q'])
            or retained['q_identity']['binary64_sha256']!='4883c34e9ab70eb909274ad1fad7ed1e0f79fc51728aa6aa8cf5178306c81c17'
            or retained['p']!=.181 or not retained['qualified_on_this_fine_grid']
            or not retained['scan']['complete_fine_scan']
            or retained['scan']['radial_grid_identity']!=driver.identity(fine)
            or retained['scan']['theta_nodes']!=3072
            or retained['scan']['working_geometry_violation_max']>1.e-8
            or state['source_actual_material_mesh_sha256']!=MATERIAL_SHA):
        raise ValueError('the actual qualifying 4883 state or row library differs')
    raw_trial = incoming['last_raw_backend_callback']
    complete = incoming['last_completed_full_scan_trial']
    if (raw_trial['q_identity']!=driver.identity(raw_trial['q'])
            or raw_trial['q_identity']['binary64_sha256']!='b5f3d74f84d81dee726f0fbaf39036ddabcc538cb80dbb74ae204b6a4e13d1e4'
            or complete['q_identity']!=driver.identity(complete['q'])
            or complete['q_identity']['binary64_sha256']!='dd8445c85316fa9844839c4c26cb8a6aaed199049e13ea6fbef560703d31ebca'
            or not complete['complete_fine_assessment'] or not complete['scan']['complete_fine_scan']
            or complete['accepted_as']!='not_accepted'
            or complete['scan']['radial_grid_identity']!=driver.identity(fine)
            or complete['scan']['working_geometry_violation_max']<=1.e-8):
        raise ValueError('the fully evaluated rejected source half-step differs')
    state.update(actual_constraint_radial_identity=driver.identity(actual),
        actual_fine_radial_identity=driver.identity(fine),
        source_qualified_fine_identity=retained['scan']['radial_grid_identity'],
        paid_97q_directional_check=source['resume97_state']['paid_97q_directional_check'])
    source['resume97_origin'],source['resume97_state'] = origin,state
    source['resume97_input_sha256'] = digest
    source['prior_cost_ledger']['physical_original401_actual_terminal'] = incoming['new_terminal_cost_ledger']
    source['prior_cost_ledger']['original401_first_baseline_cache_defect'] = incoming['source_first_baseline_cache_defect']
    source['original_unclosed_f60_c13d'] = incoming['original_unclosed_f60_c13d']
    source['original401_last_completed_full_scan_trial'] = complete
    source['unqualified_warm_backend_trial'] = raw_trial
    # The actual source half-step was fully assessed and rejected. The
    # original solver starts at its actual retained point, not that old trial.
    source['skip_completed_source_warm_trial'] = True
    return source,paid,fine


def emit(tag,value):
    if tag=='FINITE_LOCAL_TAIL_DEFINITION':
        value = dict(value)
        for key in ('source_49_backend_callbacks_are_not_replayed',
                    'source_warm_trial_has_no_fine_or_geometry_qualification',
                    'original_source_unadopted_proposal'):
            value.pop(key,None)
        value.update(schema=SCHEMA,original_source_actual_grid=[407,1536],
            first_new_grid=[412,1536],actual_source_fine_grid=[16321,3072],
            new_scope='Actual 4883; five paid pending rows, complete fine with material identity, then original solver',
            source_last_dd8445_half_step_completed_rejection_not_replayed=True,
            source_raw_b5f3_not_a_qualified_initializer=True,
            source_four_acceptances_followed_actual_0d_baseline_scans=True,
            original_f60_c13d_fine_debt_not_closed_by_new_0d_scan=True,
            source_initial_f60_baseline_misuse_recorded_not_certified=True,
            actual_new_material_identity_recorded_without_relabelling=True,
            source10_complete_Jacobians_and130_blocks_not_restored_or_replayed=True,
            same_p_q_grid_alone_is_insufficient_for_fine_cache=True,
            original_physical_solver_and_all_acceptance_thresholds_unchanged=True)
    original_emit(tag,value)


def main():
    material_guard.run(driver,load_input,emit,SCHEMA,
                       qualified_source_material_sha256=MATERIAL_SHA)


if __name__=='__main__':
    main()
