#!/usr/bin/env python3
"""Continue actual 6236, adopting its four paid rows and preserving material-qualified fine."""
import hashlib
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
PARENT_SOURCE=HERE/'r582_4883_material412_resume_20261128.py'
PARENT_REQUEST=HERE.parent/'computations/request-r582-4883-material412-20261128.json'
PARENT_SHA='775458b864bd5cebda2e7f62dcd6d96d9a073a692dd5960cf79762c900239657'
PARENT_REQUEST_SHA='0f983fd97bc275c8fe0b8e2afd03dff1bb1caed3ab12860c40bf5e8f6b213162'
INPUT_SHA='9d04e45865cb60f270eacbb5e70b2466c7ae41a18d0168a9a9d33eeec949bbcc'
MATERIAL_SHA='0d222bd12ce8a61d0c88264c6fb5c82066f0ca058855b5bf7a670a53b483a991'
SCHEMA='r582-actual6236-material-qualified-original416-continuation-v1'
INPUT_SCHEMA='r582-6236-material-bound-original416-required-terminal-v1'
STARTUP_FAILURE={
    'run_id':46143426419,'job_id':140974180250,
    'source_commit':'42a4318a391f68f763625a2f9e53495179d8537c',
    'original_raw_bytes':228176,
    'original_raw_sha256':'3242ddc88f7d45185e95e29035f9201fb55b1acc7d691805969369132b5223ca',
    'request_bytes':351114,
    'request_sha256':'c33b417f07431ad4ad83b7677ffd0ed50b48656841b3253f0fcd6f53599ca747',
    'runtime_public_pull_commit':'af42edb841feb677ef8469e83b703f622f8704f7',
    'runtime_private_pull_commit':'7441085bc8b89166859e67bfd149ea78e74d46da',
    'child_started_utc':'2026-11-28T12:12:09.276504Z',
    'child_finished_utc':'2026-11-28T12:12:10.016198Z',
    'child_wall_seconds':0.739694,'child_exit_code':1,
    'attempted_maximum_seconds':7200,'original_declared_maximum_seconds':2400,
    'failure':'ValueError: invalid declared finite-stage scope',
    'failed_before_load_input_and_scientific_clock':True,
    'scientific_FINAL_emitted':False,
    'field_Jacobian_or_fine_science_started':False,
}
if hashlib.sha256(PARENT_SOURCE.read_bytes()).hexdigest()!=PARENT_SHA:
    raise RuntimeError('the completed original412 entry differs')
import r582_4883_material412_resume_20261128 as parent
import r582_material_qualified_resume_guard_20261128 as material_guard
driver=parent.driver
original_emit=driver.emit


def load_input(raw,digest):
    encoded=sys.stdin.buffer.read() if raw=='@stdin' else raw.encode()
    if len(encoded)!=334561 or hashlib.sha256(encoded).hexdigest()!=digest or digest!=INPUT_SHA:
        raise ValueError('the actual completed original412 input differs')
    incoming=json.loads(encoded)
    if incoming['schema']!=INPUT_SCHEMA:
        raise ValueError('unexpected actual6236 input schema')
    previous_bytes=PARENT_REQUEST.read_bytes()
    if hashlib.sha256(previous_bytes).hexdigest()!=PARENT_REQUEST_SHA:
        raise ValueError('the actual completed original412 request differs')
    previous=json.loads(previous_bytes)['lanes']['actual4883-material412']['source_state_json']
    source,paid,oldfine=parent.load_input(previous,hashlib.sha256(previous.encode()).hexdigest())
    state,origin=incoming['terminal_state'],incoming['origin']
    retained=state['actual_retained_state']
    actual=driver.np.asarray(state['actual_constraint_radial_nodes'],float)
    fine=driver.np.asarray(state['actual_fine_radial_nodes'],float)
    proposed=driver.np.asarray(state['proposed_constraint_radial_nodes'],float)
    if (origin['run_id']!=46137473248 or origin['job_id']!=140955893343
            or origin['source_commit']!='5b0ab004f24f62b74d37587de6dbb2259a72419e'
            or origin['source_entry_sha256']!=PARENT_SHA or origin['request_sha256']!=PARENT_REQUEST_SHA
            or origin['FINAL_JSON_sha256']!='b7121f8b4402821dd94a0ad552cc2056fb2f0540d9e80931bda1cad1f28e37ec'
            or state['source_schema']!=parent.SCHEMA or state['stage']!=0 or state['outer']!=0
            or state['phase']!='metric' or state['stalled_outer_count']!=0
            or state['termination']!='scientific_clock_checkpoint_not_complete'):
        raise ValueError('actual original412 terminal or phase differs')
    if (len(actual)!=412 or len(proposed)!=416 or len(fine)!=16329
            or not set(actual).issubset(set(proposed))
            or set(proposed)-set(actual)!=set(state['pending_radial_nodes'])
            or len(state['pending_radial_nodes'])!=4
            or not set(oldfine).issubset(set(fine)) or not set(actual).issubset(set(fine))
            or state['actual_constraint_theta_nodes']!=1536
            or state['proposed_constraint_theta_nodes']!=1536 or state['actual_fine_theta_nodes']!=3072
            or state['pending_angular_upgrade'] or state['pending_angular_upgrade_evidence']
            or state['actual_backend_trust']!=2. or state['planned_current_trust']!=2.
            or state['proposed_next_trust']!=2.
            or retained['q_identity']!=driver.identity(retained['q'])
            or retained['q_identity']['binary64_sha256']!='6236b12db51ec3432097726e8dcbd889fbf280c18ae7b877d9d04fd637926b28'
            or retained['p']!=.181 or not retained['qualified_on_this_fine_grid']
            or not retained['scan']['complete_fine_scan']
            or retained['scan']['radial_grid_identity']!=driver.identity(fine)
            or retained['scan']['theta_nodes']!=3072
            or retained['scan']['working_geometry_violation_max']>1.e-8
            or retained['fine_qualification_material_knots_and_jets_sha256']!=MATERIAL_SHA
            or state['source_actual_material_mesh_sha256']!=MATERIAL_SHA):
        raise ValueError('actual retained6236 material qualification or row library differs')
    raw_trial=incoming['last_raw_backend_callback']
    complete=incoming['last_completed_full_scan_trial']
    if (raw_trial['q_identity']!=driver.identity(raw_trial['q'])
            or raw_trial['q_identity']['binary64_sha256']!='03cb0f338d515c0f891bd7cef0ed25dd53744a65bbfeb2afa5680cfe6a478ae5'
            or raw_trial['complete_fine_assessment'] or raw_trial['current_complete_backend_feasible']
            or not raw_trial['retained_from_separate_assessment']
            or complete['q_identity']!=retained['q_identity'] or complete['q']!=retained['q']
            or not complete['complete_fine_assessment'] or not complete['scan']['complete_fine_scan']
            or complete['accepted_as']!='complete_fine_feasible_metric_improvement'
            or complete['scan']['radial_grid_identity']!=driver.identity(fine)
            or complete['scan']['working_geometry_violation_max']>1.e-8
            or complete['physical_assessment_fraction']!=.5):
        raise ValueError('the completed accepted physical half-step differs')
    state.update(actual_constraint_radial_identity=driver.identity(actual),
        actual_fine_radial_identity=driver.identity(fine),
        source_qualified_fine_identity=retained['scan']['radial_grid_identity'],
        paid_97q_directional_check=source['resume97_state']['paid_97q_directional_check'])
    source['resume97_origin'],source['resume97_state']=origin,state
    source['resume97_input_sha256']=digest
    source['prior_cost_ledger']['physical_original412_actual_terminal']=incoming['new_terminal_cost_ledger']
    source['prior_cost_ledger']['actual6236_declared_scope_startup_failure']=STARTUP_FAILURE
    source['original412_last_completed_full_scan_trial']=complete
    source['unqualified_warm_backend_trial']=raw_trial
    # The accepted physical half-step is already the current retained point.
    # Its completed scan and the separate raw point must not be warm-replayed.
    source['skip_completed_source_warm_trial']=True
    return source,paid,fine


def emit(tag,value):
    if tag=='FINITE_LOCAL_TAIL_DEFINITION':
        value=dict(value)
        for key in ('source_49_backend_callbacks_are_not_replayed',
                    'source_warm_trial_has_no_fine_or_geometry_qualification',
                    'original_source_unadopted_proposal'):
            value.pop(key,None)
        value.update(schema=SCHEMA,original_source_actual_grid=[412,1536],
            first_new_grid=[416,1536],actual_source_fine_grid=[16329,3072],
            new_scope='Actual6236; four paid pending rows, same-material fine identity and original full solver',
            source_last_6236_half_step_completed_accepted_not_replayed=True,
            source_raw_03cb_not_a_qualified_initializer=True,
            source_nine_fine_scans_and_all_eight_raw_callbacks_recorded=True,
            source9_complete_Jacobians_and117_blocks_not_restored=True,
            necessary_new_current_J_and_missing_field_reconstruction_charged=True,
            original_f60_c13d_fine_debt_not_closed_by_new_0d_scans=True,
            same_p_q_grid_alone_is_insufficient_for_fine_cache=True,
            original_physical_solver_and_all_acceptance_thresholds_unchanged=True)
    original_emit(tag,value)


def main():
    material_guard.run(driver,load_input,emit,SCHEMA,qualified_source_material_sha256=MATERIAL_SHA)


if __name__=='__main__':
    main()
