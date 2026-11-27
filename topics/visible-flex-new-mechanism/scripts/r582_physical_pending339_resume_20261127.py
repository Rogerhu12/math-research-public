#!/usr/bin/env python3
"""Continue actual4bd9 on its original proposed339 library and all16203 fine.

Retain the actual0d material source identity and the complete original costs.
The original driver adopts only the recorded five pending radial points;
any newly required fine grid or changed material receives its own full gates.
No native-H interface or new scientific diagnostic is introduced here.
"""
import hashlib
import json
from pathlib import Path
import sys

PARENT_SHA256='fffe47880d413b52f9fabd4bd963e4ec9ea51af925444dd8eb42436894e5124d'
parent_path=Path(__file__).with_name('r582_physical_pending330_resume_20261127.py')
if hashlib.sha256(parent_path.read_bytes()).hexdigest()!=PARENT_SHA256:
    raise RuntimeError('actual completed pending330 source changed')
import r582_physical_pending330_resume_20261127 as parent

driver=parent.driver
SCHEMA='r582-actual-4bd9-0d-pending339-physical-resume-v1'
INPUT_SCHEMA='identified-4bd9-0d-terminal97q-pending339-v1'
original_emit=driver.emit


def load_input(raw,digest):
    encoded=sys.stdin.buffer.read() if raw=='@stdin' else raw.encode()
    if hashlib.sha256(encoded).hexdigest()!=digest:
        raise ValueError('actual4bd9 pending339 complete stdin differs')
    incoming=json.loads(encoded)
    if incoming.get('schema')!=INPUT_SCHEMA:
        raise ValueError('wrong identified4bd9 source schema')
    required={
        'run_id':45916249440,'job_id':140236066717,
        'source_commit':'b86ec60074123372cc774ad13629f412512c79f6',
        'runtime_public_pull_commit':'5777da76dbb3927ff9f4ec7c1a1b0d37b4237156',
        'source_entry_sha256':PARENT_SHA256,
        'original_raw_bytes':7572735,
        'original_raw_sha256':'69731f4c7ffa1529bc8bad76cf8a84949b94e1f58648fe1cfeccc0698949b7bd',
        'FINAL_JSON_bytes':522743,
        'FINAL_JSON_sha256':'772b22e0ac7b2079041c36c09e34490cf602f3f49da814efe769ef8c1aa99ab2',
        'source_state_sha256':'8f8d55778bce0d655b970ca004dbadcef9f8eaa3f9383a5ea56b30de7e174b94',
        'termination':'scientific_clock_checkpoint_not_complete',
    }
    if incoming['origin']!=required:
        raise ValueError('unique pending330 source terminal differs')
    prior_path=Path(__file__).resolve().parents[3]/(
        'topics/visible-flex-new-mechanism/computations/'
        'request-r582-physical-pending330-resume-20261127.json')
    prior_bytes=prior_path.read_bytes()
    if (len(prior_bytes)!=529785 or hashlib.sha256(prior_bytes).hexdigest()!=
            '7f518dcf0d11e0071615049087d9472ad46340e0f18c5629802191b38e327da4'):
        raise ValueError('actual source published request changed')
    prior_input=json.loads(prior_bytes)['lanes']['actual-3bc1-0d-pending330']['source_state_json']
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
            or terminal['stage']!=0 or terminal['outer']!=4 or terminal['phase']!='metric'
            or terminal['last_natural_OptimizeResult'] is not None
            or terminal['actual_grid_p']!=.181 or terminal['actual_retained_p']!=.181
            or terminal['proposed_or_current_p']!=.181
            or driver.identity(actual)!={'entries':334,'binary64_sha256':
                '74d43ced0bdef271c2c4fa65092c2fe39e32285998d02f5fecf2efa54a8394f8'}
            or driver.identity(fine)!={'entries':16203,'binary64_sha256':
                'f4770c7aab814ba2e9e47421f28c287e82e5c72e3c1eb9808cb2644576f3d129'}
            or driver.identity(proposed)!={'entries':339,'binary64_sha256':
                '005cdecbffc954799526aafbbb9547c089b34f850e880feaf05538bb6c000d03'}
            or driver.identity(pending)!={'entries':5,'binary64_sha256':
                'd9ec0078c586b9175002191da96ddf2d9b6c516843ca0ced41970ca470a537d9'}
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
        raise ValueError('actual334/fine16203/proposed339 or unchanged trust differs')
    retained=terminal['actual_retained_state']
    qsha='4bd9258b175c5d8e67140c0a7b6eeb68ee98cfe12479673c756a88e6ee8fea48'
    if (retained['q_identity']!=driver.identity(retained['q'])
            or retained['q_identity']!={'entries':97,'binary64_sha256':qsha}
            or retained['p']!=.181 or retained['stage']!=0
            or retained['accepted_as']!='complete_fine_feasible_metric_improvement'
            or not retained['qualified_on_this_fine_grid']
            or retained['scan']['radial_grid_identity']!={'entries':16203,'binary64_sha256':
                'f4770c7aab814ba2e9e47421f28c287e82e5c72e3c1eb9808cb2644576f3d129'}
            or retained['scan']['theta_nodes']!=3072
            or not retained['scan']['complete_fine_scan']
            or retained['scan']['eta_max']!=3.616136752215837e-05
            or retained['scan']['geometry_violation_max']!=0.
            or retained['scan']['working_geometry_violation_max']!=1.4877377021299543e-10
            or retained['scan']['radial_grid_identity']!=driver.identity(fine)):
        raise ValueError('actual4bd9 complete16203 qualification differs')
    warm=terminal['last_backend_callback_candidate']
    trial=terminal['last_completed_full_scan_trial']
    warmsha='c4b916999bf27d2565550b3afb3c05f40dcb1c658c20a4591d0af8e21adb2ca2'
    if (warm['q_identity']!=driver.identity(warm['q'])
            or warm['q_identity']!={'entries':97,'binary64_sha256':warmsha}
            or warm['actual_constraint_radial_identity']!=driver.identity(actual)
            or warm['actual_constraint_theta_nodes']!=1536 or warm['p']!=.181
            or warm['backend_extra']!=3.581566503571331e-05
            or warm['current_complete_backend_violation']!=3.412826463316756e-06
            or warm['current_complete_backend_feasible'] or warm['retained_by_this_raw_callback']
            or warm['complete_fine_assessment']
            or not warm['retained_from_separate_assessment']
            or warm['separate_assessment_q_identity']!=retained['q_identity']
            or not warm['separate_assessment_complete_fine_assessment']
            or not warm['separate_assessment_is_not_raw_backend_point']
            or warm['separate_assessment_fraction']!=.5
            or warm['separate_assessment_epigraph']!=3.609195544585496e-05
            or warm['separate_assessment_complete_row_violation']!=1.4877199385615603e-10
            or warm['last_physical_backtrack_fraction']!=.5
            or warm['last_physical_backtrack_halvings']!=1
            or trial['q_identity']!=retained['q_identity']
            or driver.identity(trial['q'])!=retained['q_identity']
            or trial['accepted_as']!='complete_fine_feasible_metric_improvement'
            or trial['scan']!=retained['scan']
            or trial['physical_assessment_fraction']!=.5
            or trial['backend_extra']!=3.609195544585496e-05):
        raise ValueError('last unqualified raw candidate cannot replace actual4bd9')
    counts=terminal['counts']
    if (terminal['elapsed_seconds']!=2408.826496151
            or counts['accepted_metric']!=8 or counts['complete_fine_scans']!=17
            or counts.get('accepted_geometry_restoration',0)!=1
            or counts['completed_outers']!=4
            or counts['complete_fine_radial_blocks']!=2159
            or counts['fine_radial_points_evaluated']!=275403
            or counts['completed_backend_Jacobians']!=6
            or counts['completed_backend_direction_blocks']!=78
            or counts['completed_backend_value_evaluations']!=62
            or terminal['current_backend_cost_not_yet_folded_into_completed_outers']!=
                {'complete_Jacobians':8,'completed_direction_blocks':104,'value_evaluations':36}
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
    ledger.update(new_scientific_seconds=terminal['elapsed_seconds'],source_run=45916249440,
        source_job=140236066717,source14_complete_Jacobians_and17_full_scans_not_replayed=True,
        source_current_eight_Jacobians104_blocks36_values_and_all_unclosed_work_retained=True,
        source_backend_internal_work_arrays_not_available=True,
        source_actual_material_mesh_sha256=terminal['field_receipt']['material_mesh_binary64_sha256'],
        original_raw_sha256=required['original_raw_sha256'],original_FINAL_JSON_sha256=required['FINAL_JSON_sha256'])
    source['resume97_origin'],source['resume97_state']=required,state
    source['resume97_input_sha256']=digest
    source['unqualified_warm_backend_trial']=warm
    source['prior_cost_ledger']['physical_pending330_original_terminal']=ledger
    return source,paid,fine


def emit(tag,value):
    if tag=='FINITE_LOCAL_TAIL_DEFINITION':
        value=dict(value)
        for key in ('source_49_backend_callbacks_are_not_replayed',
                    'source_warm_trial_has_no_fine_or_geometry_qualification',
                    'original_source_unadopted_proposal'):
            value.pop(key,None)
        value.update(schema=SCHEMA,original_source_actual_grid=[334,1536],first_new_grid=[339,1536],
            source_original_proposed_grid=[339,1536],source14_complete_Jacobians_and17_scans_not_replayed=True,
            source8_actual_metric_and1_restoration_acceptances_not_replayed=True,
            all16203_required_fine_locations_and3072_angles_preserved=True,
            source_true_qualified_fine_is_identical16203=True,
            actual_retained_q_is4bd9_not_unqualified_rawc4b9=True,
            source_last_raw_trial_had_no_complete_fine_qualification=True,
            source_last_raw_separate_half_copy_is_exactly_retained4bd9=True,
            source_actual_material_mesh_is0d_and_its_identity_is_not_relabelled=True,
            newly_constructed_field_actual_identity_is_recorded_without_relabeling=True,
            recorded_pending339_adds_eight_midpoints_and_forces_original_complete_new_baseline=True,
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
