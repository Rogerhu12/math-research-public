#!/usr/bin/env python3
"""Continue actual3bc1 on its original proposed330 library and all16189 fine.

Retain the actual0d material source identity and the complete original costs.
The original driver adopts only the recorded three pending radial points;
any newly required fine grid or changed material receives its own full gates.
No native-H interface or new scientific diagnostic is introduced here.
"""
import hashlib
import json
from pathlib import Path
import sys

PARENT_SHA256='2fc530a00a2a560ea2a85f33aa057ea3085c7850a568d855cc2271494b730c91'
parent_path=Path(__file__).with_name('r582_physical_normal311_resume_20261127.py')
if hashlib.sha256(parent_path.read_bytes()).hexdigest()!=PARENT_SHA256:
    raise RuntimeError('actual completed normal311 source changed')
import r582_physical_normal311_resume_20261127 as parent

driver=parent.driver
SCHEMA='r582-actual-3bc1-0d-pending330-physical-resume-v1'
INPUT_SCHEMA='identified-3bc1-0d-terminal97q-pending330-v1'
original_emit=driver.emit


def load_input(raw,digest):
    encoded=sys.stdin.buffer.read() if raw=='@stdin' else raw.encode()
    if hashlib.sha256(encoded).hexdigest()!=digest:
        raise ValueError('actual3bc1 pending330 complete stdin differs')
    incoming=json.loads(encoded)
    if incoming.get('schema')!=INPUT_SCHEMA:
        raise ValueError('wrong identified3bc1 source schema')
    required={
        'run_id':45909167191,'job_id':140213091600,
        'source_commit':'181de62c735dfa087cd62e842c191c7d226f4e0a',
        'runtime_public_pull_commit':'08e0b93016a795fd312f83db96ff07f444810bbd',
        'source_entry_sha256':PARENT_SHA256,
        'original_raw_bytes':7220660,
        'original_raw_sha256':'9726268200ac107dbd7c7c411e13b33cba913522bb1663b7930f66c0a4985d0a',
        'FINAL_JSON_bytes':506334,
        'FINAL_JSON_sha256':'23bef2fbc32807204c2ee2c3bebbb646ccd740642c95de117289809504b282d7',
        'source_state_sha256':'95f9118e0e196b7a5d8a992ffaba1ff335b73f329245b128543ad3c372dc82cd',
        'termination':'scientific_clock_checkpoint_not_complete',
    }
    if incoming['origin']!=required:
        raise ValueError('unique normal311 source terminal differs')
    prior_path=Path(__file__).resolve().parents[3]/(
        'topics/visible-flex-new-mechanism/computations/'
        'request-r582-physical-normal311-resume-20261127.json')
    prior_bytes=prior_path.read_bytes()
    if (len(prior_bytes)!=498680 or hashlib.sha256(prior_bytes).hexdigest()!=
            '28f8beb6c034ba934fb9e57b95aa7da516800d177255a43263027e6a33a1bb6a'):
        raise ValueError('actual source published request changed')
    prior_input=json.loads(prior_bytes)['lanes']['actual-59a4-f60-normal311']['source_state_json']
    source,paid,oldfine=parent.load_input(prior_input,required['source_state_sha256'])
    final_bytes=incoming['complete_original_FINAL_JSON'].encode()
    if (len(final_bytes)!=required['FINAL_JSON_bytes'] or
            hashlib.sha256(final_bytes).hexdigest()!=required['FINAL_JSON_sha256']):
        raise ValueError('complete actual natural FINAL changed')
    terminal=json.loads(final_bytes)
    actual=driver.np.asarray(terminal['actual_constraint_radial_nodes'],dtype=float)
    fine=driver.np.asarray(terminal['actual_fine_radial_nodes'],dtype=float)
    proposed=driver.np.asarray(terminal['proposed_constraint_radial_nodes'],dtype=float)
    pending=driver.np.asarray(terminal['pending_radial_nodes'],dtype=float)
    if (terminal['schema']!=parent.SCHEMA or terminal['termination']!=required['termination']
            or terminal['stage']!=0 or terminal['outer']!=3 or terminal['phase']!='metric'
            or terminal['last_natural_OptimizeResult'] is not None
            or terminal['actual_grid_p']!=.181 or terminal['actual_retained_p']!=.181
            or terminal['proposed_or_current_p']!=.181
            or driver.identity(actual)!={'entries':327,'binary64_sha256':
                '6c55a5e61e09146bd8972348a3176db35ee585985b46667128b041ef0e05b440'}
            or driver.identity(fine)!={'entries':16189,'binary64_sha256':
                'd6a0d6e71af4341f2ce4c64723c124835071ca1f7148fda7278c3dd053f17ccb'}
            or driver.identity(proposed)!={'entries':330,'binary64_sha256':
                'd67124b1f5d7e01959036ff617ba269dd1189373cc89c663cc87c3af88f3a0da'}
            or driver.identity(pending)!={'entries':3,'binary64_sha256':
                'd90110da13688d649219cad35861a18517a2455c6fa9eee4901e4ba018b68e71'}
            or not set(actual).issubset(set(proposed))
            or set(proposed)-set(actual)!=set(pending)
            or not set(oldfine).issubset(set(fine))
            or not set(actual).issubset(set(fine))
            or terminal['actual_constraint_theta_nodes']!=1536
            or terminal['actual_fine_theta_nodes']!=3072
            or terminal['proposed_constraint_theta_nodes']!=1536
            or terminal['pending_angular_upgrade'] or terminal['pending_angular_upgrade_evidence']
            or terminal['actual_backend_trust']!=2.
            or terminal['proposed_next_trust']!=2. or terminal['planned_current_trust']!=2.):
        raise ValueError('actual327/fine16189/proposed330 or unchanged trust differs')
    retained=terminal['actual_retained_state']
    qsha='3bc11a9c80696ad3ec54066a9bf0d5cee4436081dee79b9e22b61757fe507aa1'
    if (retained['q_identity']!=driver.identity(retained['q'])
            or retained['q_identity']!={'entries':97,'binary64_sha256':qsha}
            or retained['p']!=.181 or retained['stage']!=0
            or retained['accepted_as']!='complete_fine_feasible_metric_improvement'
            or not retained['qualified_on_this_fine_grid']
            or retained['scan']['radial_grid_identity']!={'entries':16189,'binary64_sha256':
                'd6a0d6e71af4341f2ce4c64723c124835071ca1f7148fda7278c3dd053f17ccb'}
            or retained['scan']['theta_nodes']!=3072
            or not retained['scan']['complete_fine_scan']
            or retained['scan']['eta_max']!=3.722676721935829e-05
            or retained['scan']['geometry_violation_max']!=0.
            or retained['scan']['working_geometry_violation_max']!=2.3094850684635126e-12
            or retained['scan']['radial_grid_identity']!=driver.identity(fine)):
        raise ValueError('actual3bc1 complete16189 qualification differs')
    warm=terminal['last_backend_callback_candidate']
    trial=terminal['last_completed_full_scan_trial']
    warmsha='135e3bccf8ee50fc816c3acad03a9928b67cfcc0323ea20035a4591dff064e72'
    if (warm['q_identity']!=driver.identity(warm['q'])
            or warm['q_identity']!={'entries':97,'binary64_sha256':warmsha}
            or warm['actual_constraint_radial_identity']!=driver.identity(actual)
            or warm['actual_constraint_theta_nodes']!=1536 or warm['p']!=.181
            or warm['backend_extra']!=3.7088351809257116e-05
            or warm['current_complete_backend_violation']!=1.428317347522942e-06
            or warm['current_complete_backend_feasible'] or warm['retained_by_this_raw_callback']
            or warm['complete_fine_assessment']
            or warm['last_physical_backtrack_fraction']!=1.52587890625e-05
            or warm['last_physical_backtrack_halvings']!=16
            or trial['q_identity']!=retained['q_identity']
            or driver.identity(trial['q'])!=retained['q_identity']
            or trial['accepted_as']!='complete_fine_feasible_metric_improvement'
            or trial['scan']!=retained['scan']
            or trial['physical_assessment_fraction']!=.5
            or trial['backend_extra']!=3.7226767222911544e-05):
        raise ValueError('last unqualified raw candidate cannot replace actual3bc1')
    counts=terminal['counts']
    if (terminal['elapsed_seconds']!=2427.43645062
            or counts['accepted_metric']!=8 or counts['complete_fine_scans']!=17
            or counts.get('accepted_geometry_restoration',0)!=0
            or counts['completed_outers']!=3
            or counts['complete_fine_radial_blocks']!=2159
            or counts['fine_radial_points_evaluated']!=275020
            or counts['completed_backend_Jacobians']!=10
            or counts['completed_backend_direction_blocks']!=130
            or counts['completed_backend_value_evaluations']!=53
            or terminal['current_backend_cost_not_yet_folded_into_completed_outers']!=
                {'complete_Jacobians':4,'completed_direction_blocks':52,'value_evaluations':44}
            or terminal['new_directional_checks_this_run']!=0
            or terminal['field_receipt']['material_mesh_binary64_sha256']!=
                '0d222bd12ce8a61d0c88264c6fb5c82066f0ca058855b5bf7a670a53b483a991'):
        raise ValueError('actual costs and source0d material identity differ')
    state={name:terminal[name] for name in (
        'actual_retained_state','actual_constraint_radial_nodes','actual_constraint_theta_nodes',
        'actual_fine_radial_nodes','actual_fine_theta_nodes','proposed_constraint_radial_nodes',
        'proposed_constraint_theta_nodes','pending_radial_nodes','pending_angular_upgrade',
        'pending_angular_upgrade_evidence','actual_backend_trust','proposed_next_trust')}
    state.update(actual_constraint_radial_identity=driver.identity(actual),
        actual_fine_radial_identity=driver.identity(fine),
        source_qualified_fine_identity=dict(retained['scan']['radial_grid_identity']),
        source_actual_material_mesh_sha256=terminal['field_receipt']['material_mesh_binary64_sha256'],
        paid_97q_directional_check=source['resume97_state']['paid_97q_directional_check'])
    ledger={name:terminal[name] for name in (
        'counts','new_model_counts','R604_observation_counts',
        'current_backend_cost_not_yet_folded_into_completed_outers',
        'final_resonant_field_counts','final_stable_evaluator_counts','original_model_new_counts')}
    ledger.update(new_scientific_seconds=terminal['elapsed_seconds'],source_run=45909167191,
        source_job=140213091600,source14_complete_Jacobians_and17_full_scans_not_replayed=True,
        source_current_four_Jacobians52_blocks44_values_and_all_unclosed_work_retained=True,
        source_backend_internal_work_arrays_not_available=True,
        source_actual_material_mesh_sha256=terminal['field_receipt']['material_mesh_binary64_sha256'],
        original_raw_sha256=required['original_raw_sha256'],original_FINAL_JSON_sha256=required['FINAL_JSON_sha256'])
    source['resume97_origin'],source['resume97_state']=required,state
    source['resume97_input_sha256']=digest
    source['unqualified_warm_backend_trial']=warm
    source['prior_cost_ledger']['physical_normal311_original_terminal']=ledger
    return source,paid,fine


def emit(tag,value):
    if tag=='FINITE_LOCAL_TAIL_DEFINITION':
        value=dict(value)
        for key in ('source_49_backend_callbacks_are_not_replayed',
                    'source_warm_trial_has_no_fine_or_geometry_qualification',
                    'original_source_unadopted_proposal'):
            value.pop(key,None)
        value.update(schema=SCHEMA,original_source_actual_grid=[327,1536],first_new_grid=[330,1536],
            source_original_proposed_grid=[330,1536],source14_complete_Jacobians_and17_scans_not_replayed=True,
            source8_actual_metric_acceptances_not_replayed=True,
            all16189_required_fine_locations_and3072_angles_preserved=True,
            source_true_qualified_fine_is_identical16189=True,
            actual_retained_q_is3bc1_not_unqualified_raw135e=True,
            source_last_raw_trial_had_no_complete_fine_or_strict_metric_promise=True,
            source_actual_material_mesh_is0d_and_its_identity_is_not_relabelled=True,
            newly_constructed_field_actual_identity_is_recorded_without_relabeling=True,
            recorded_pending330_adds_six_midpoints_and_forces_original_complete_new_baseline=True,
            same_single_constructed_field_used_for_every_new_scan_and_backend=True,
            original_native_backend_and_all_scientific_acceptance_functions_unchanged=True,
            new_native_curvature_adapter_not_applied_to_this_different98_dimensional_backend=True)

    original_emit(tag,value)


def main():
    driver.load_input=load_input
    driver.emit=emit
    driver.SCHEMA=SCHEMA
    driver.main()


if __name__=='__main__':
    main()
