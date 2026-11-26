#!/usr/bin/env python3
"""Continue actual59a4 on its already adopted311 library and full16167 fine.

The retained source has complete16149 qualification on actual material f60.
The larger required grid receives its own original full qualification on
one newly constructed field; no old material SHA or fine label is relabelled.
The original driver, full gates and raw/physical-best separation are retained.
"""
import hashlib
import json
from pathlib import Path
import sys

PARENT_SHA256='695104e5f0c664a06efac69bb461d6e1065c2d000cd99c591d8cf5c661ca5394'
parent_path=Path(__file__).with_name('r582_physical_pending298_resume_20261127.py')
if hashlib.sha256(parent_path.read_bytes()).hexdigest()!=PARENT_SHA256:
    raise RuntimeError('actual completed normal298 source changed')
import r582_physical_pending298_resume_20261127 as parent

driver=parent.driver
SCHEMA='r582-actual-59a4-f60-normal311-physical-resume-v1'
INPUT_SCHEMA='identified-59a4-f60-terminal97q-normal311-v1'
original_emit=driver.emit


def load_input(raw,digest):
    encoded=sys.stdin.buffer.read() if raw=='@stdin' else raw.encode()
    if hashlib.sha256(encoded).hexdigest()!=digest:
        raise ValueError('actual59a4 normal311 complete stdin differs')
    incoming=json.loads(encoded)
    if incoming.get('schema')!=INPUT_SCHEMA:
        raise ValueError('wrong identified59a4 source schema')
    required={
        'run_id':45901312947,'job_id':140187488430,
        'source_commit':'98ded25f6b56ef1899efec271406361453217575',
        'runtime_public_pull_commit':'f32fbfcb5884ab2d866f08641fe60b84ea45a38d',
        'source_entry_sha256':PARENT_SHA256,
        'original_raw_bytes':6455101,
        'original_raw_sha256':'bde7498af6ab06b89d32d4657ce79458ee70aa839f705869cc7a266ad0c401dd',
        'FINAL_JSON_bytes':479059,
        'FINAL_JSON_sha256':'8b6f57b0a4d0f212fe378c10ec563e350efa7ca2b0e7d958912715e25ce42e15',
        'source_state_sha256':'ca5dc60038fe6f143da4d18d09dce36eb7d02db921631e822d008887b2a4e788',
        'termination':'scientific_clock_checkpoint_not_complete',
    }
    if incoming['origin']!=required:
        raise ValueError('unique normal298 source terminal differs')
    prior_path=Path(__file__).resolve().parents[3]/(
        'topics/visible-flex-new-mechanism/computations/'
        'request-r582-physical-pending298-resume-20261127.json')
    prior_bytes=prior_path.read_bytes()
    if (len(prior_bytes)!=399393 or hashlib.sha256(prior_bytes).hexdigest()!=
            'dcf95705842e8dc00b5cca4b8f1ff7fa4733462a840833bbe410affc57ff582a'):
        raise ValueError('actual source published request changed')
    prior_input=json.loads(prior_bytes)['lanes']['actual-14d1-pending298']['source_state_json']
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
            or terminal['stage']!=0 or terminal['outer']!=1 or terminal['phase']!='metric'
            or terminal['last_natural_OptimizeResult'] is not None
            or terminal['actual_grid_p']!=.181 or terminal['actual_retained_p']!=.181
            or terminal['proposed_or_current_p']!=.181
            or driver.identity(actual)!={'entries':311,'binary64_sha256':
                'f9346fa13311a0fd0fc8bc17bfde0d3f30c08b93aeffb618bc037c2de7916736'}
            or driver.identity(fine)!={'entries':16167,'binary64_sha256':
                '4240c3ba1d2959ea4c5f81139ead8a1a6e1f218f6b903df1eca94156361c71fd'}
            or not driver.np.array_equal(actual,proposed) or len(pending)!=0
            or not set(oldfine).issubset(set(fine))
            or not set(actual).issubset(set(fine))
            or terminal['actual_constraint_theta_nodes']!=1536
            or terminal['actual_fine_theta_nodes']!=3072
            or terminal['proposed_constraint_theta_nodes']!=1536
            or terminal['pending_angular_upgrade'] or terminal['pending_angular_upgrade_evidence']
            or terminal['actual_backend_trust']!=2.
            or terminal['proposed_next_trust']!=2. or terminal['planned_current_trust']!=2.):
        raise ValueError('actual311/fine16167/empty pending or unchanged trust differs')
    retained=terminal['actual_retained_state']
    qsha='59a4ba766a9450509bcbd539639503e8a67d9dc0a98c6c3b63f59879c29a7b45'
    if (retained['q_identity']!=driver.identity(retained['q'])
            or retained['q_identity']!={'entries':97,'binary64_sha256':qsha}
            or retained['p']!=.181 or retained['stage']!=0
            or retained['accepted_as']!='complete_fine_feasible_metric_improvement'
            or not retained['qualified_on_this_fine_grid']
            or retained['scan']['radial_grid_identity']!={'entries':16149,'binary64_sha256':
                '2bfc3537692283311887978a96fba44fc95dfd6bb2fea6cdaae80440d1cd2e31'}
            or retained['scan']['theta_nodes']!=3072
            or not retained['scan']['complete_fine_scan']
            or retained['scan']['eta_max']!=3.838285782595128e-05
            or retained['scan']['geometry_violation_max']!=0.
            or retained['scan']['working_geometry_violation_max']!=0.
            or retained['scan']['radial_grid_identity']==driver.identity(fine)):
        raise ValueError('actual59a4 f60 qualification16149 is not required16167')
    warm=terminal['last_backend_callback_candidate']
    trial=terminal['last_completed_full_scan_trial']
    warmsha='d613ff403c21de80b2f4366214728467b9d1316b8695ecf96d17fb8e6d3e70ba'
    if (warm['q_identity']!=driver.identity(warm['q'])
            or warm['q_identity']!={'entries':97,'binary64_sha256':warmsha}
            or warm['actual_constraint_radial_identity']!={'entries':298,'binary64_sha256':
                '766fddc2d159f0c70316aa64a6e14705d6b0add23333361e1bc846cb7f8b4dfd'}
            or warm['actual_constraint_theta_nodes']!=1536 or warm['p']!=.181
            or warm['backend_extra']!=3.705887630822819e-05
            or warm['current_complete_backend_violation']!=4.596590863705126e-07
            or warm['current_complete_backend_feasible'] or warm['retained_by_this_raw_callback']
            or not warm['complete_fine_assessment']
            or not warm['separate_assessment_complete_fine_assessment']
            or warm['separate_assessment_q_identity']!=trial['q_identity']
            or warm['separate_assessment_fraction']!=1.
            or trial['q_identity']!={'entries':97,'binary64_sha256':warmsha}
            or trial['accepted_as']!='not_accepted'
            or trial['scan']['eta_max']!=3.776290107081685e-05
            or trial['scan']['working_geometry_violation_max']!=2.6502573901020753e-05):
        raise ValueError('last failed raw/physical trial cannot replace actual59a4')
    counts=terminal['counts']
    if (terminal['elapsed_seconds']!=2370.257524993
            or counts['accepted_metric']!=12 or counts['complete_fine_scans']!=15
            or counts.get('accepted_geometry_restoration',0)!=0
            or counts['completed_outers']!=1
            or counts['complete_fine_radial_blocks']!=1919
            or counts['fine_radial_points_evaluated']!=244027
            or counts['completed_backend_Jacobians']!=13
            or counts['completed_backend_direction_blocks']!=169
            or counts['completed_backend_value_evaluations']!=70
            or terminal['current_backend_cost_not_yet_folded_into_completed_outers'] is not None
            or terminal['new_directional_checks_this_run']!=0
            or terminal['field_receipt']['material_mesh_binary64_sha256']!=
                'f60be03b0af36d5d182f21860fe69cef80439c12bb23562d63dc2b57648bf52c'):
        raise ValueError('actual costs and source f60 material identity differ')
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
    ledger.update(new_scientific_seconds=terminal['elapsed_seconds'],source_run=45901312947,
        source_job=140187488430,source13_complete_Jacobians_and15_full_scans_not_replayed=True,
        source_unclosed_new_grid_work_kept_in_elapsed_and_model_counters=True,
        source_backend_internal_work_arrays_not_available=True,
        source_actual_material_mesh_sha256=terminal['field_receipt']['material_mesh_binary64_sha256'],
        original_raw_sha256=required['original_raw_sha256'],original_FINAL_JSON_sha256=required['FINAL_JSON_sha256'])
    source['resume97_origin'],source['resume97_state']=required,state
    source['resume97_input_sha256']=digest
    source['unqualified_warm_backend_trial']=warm
    source['prior_cost_ledger']['physical_pending298_original_terminal']=ledger
    return source,paid,fine


def emit(tag,value):
    if tag=='FINITE_LOCAL_TAIL_DEFINITION':
        value=dict(value)
        for key in ('source_49_backend_callbacks_are_not_replayed',
                    'source_warm_trial_has_no_fine_or_geometry_qualification',
                    'original_source_unadopted_proposal'):
            value.pop(key,None)
        value.update(schema=SCHEMA,original_source_actual_grid=[311,1536],first_new_grid=[311,1536],
            source_original_proposed_grid=[311,1536],source13_complete_Jacobians_and15_scans_not_replayed=True,
            source12_actual_metric_acceptances_not_replayed=True,
            all16167_required_fine_locations_and3072_angles_preserved=True,
            source_true_qualified_fine_is16149_not16167=True,
            actual_retained_q_is59a4_not_failed_raw_d613=True,
            source_d613_fine_metric_improved_but_physical_working_gate_failed=True,
            source_original_material_f60_is_not_old0d=True,
            newly_constructed_field_actual_identity_is_recorded_without_relabeling=True,
            different_required_fine_identity_forces_original_complete_new_baseline=True,
            same_single_constructed_field_used_for_every_new_scan_and_backend=True,
            original_all_group_acceptance_and_scientific_functions_unchanged=True)
    original_emit(tag,value)


def main():
    driver.load_input=load_input
    driver.emit=emit
    driver.SCHEMA=SCHEMA
    driver.main()


if __name__=='__main__':
    main()
