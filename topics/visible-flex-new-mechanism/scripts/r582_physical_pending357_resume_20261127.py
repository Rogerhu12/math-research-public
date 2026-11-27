#!/usr/bin/env python3
"""Continue actual95de on its original proposed357 library and all16240 fine.

Retain the actual0d material source identity and the complete original costs.
The original driver adopts only the recorded one pending radial point;
any newly required fine grid or changed material receives its own full gates.
No native-H interface or new scientific diagnostic is introduced here.
"""
import hashlib
import json
from pathlib import Path
import sys

PARENT_SHA256='714bd52cb6b5267fd8b5fe43e9862eb17190648c27e33d35141695445e04e91c'
parent_path=Path(__file__).with_name('r582_physical_pending339_resume_20261127.py')
if hashlib.sha256(parent_path.read_bytes()).hexdigest()!=PARENT_SHA256:
    raise RuntimeError('actual completed pending339 source changed')
import r582_physical_pending339_resume_20261127 as parent

driver=parent.driver
SCHEMA='r582-actual-95de-0d-pending357-physical-resume-v1'
INPUT_SCHEMA='identified-95de-0d-terminal97q-pending357-v1'
original_emit=driver.emit


def load_input(raw,digest):
    encoded=sys.stdin.buffer.read() if raw=='@stdin' else raw.encode()
    if hashlib.sha256(encoded).hexdigest()!=digest:
        raise ValueError('actual95de pending357 complete stdin differs')
    incoming=json.loads(encoded)
    if incoming.get('schema')!=INPUT_SCHEMA:
        raise ValueError('wrong identified95de source schema')
    required={
        'run_id':45922821540,'job_id':140257301670,
        'source_commit':'57d834aab5440749f5f4fed6da2408511690cd57',
        'runtime_public_pull_commit':'2df687b45c139d13f90bb70007cf9080aca97509',
        'source_entry_sha256':PARENT_SHA256,
        'original_raw_bytes':8935172,
        'original_raw_sha256':'e20ba21e85f2e55dafaecac1dbe51eb2a54b9b84f219b7182a2d7eec145939e4',
        'FINAL_JSON_bytes':528339,
        'FINAL_JSON_sha256':'de42d35f563432bd0fc0324d0a6595d173c12cb8258a07559e749a2baa3a5067',
        'source_state_sha256':'c2ede476f04ec15408426786ce91f0da0652b6a39f70c6dfa79861c7a7983eb4',
        'termination':'scientific_clock_checkpoint_not_complete',
    }
    if incoming['origin']!=required:
        raise ValueError('unique pending339 source terminal differs')
    prior_path=Path(__file__).resolve().parents[3]/(
        'topics/visible-flex-new-mechanism/computations/'
        'request-r582-physical-pending339-resume-20261127.json')
    prior_bytes=prior_path.read_bytes()
    if (len(prior_bytes)!=548691 or hashlib.sha256(prior_bytes).hexdigest()!=
            'e6974a69e08c5bb69b8b37f057c9355bb90395bc3e992b9b2e6b4eb9b0bdeae9'):
        raise ValueError('actual source published request changed')
    prior_input=json.loads(prior_bytes)['lanes']['actual-4bd9-0d-pending339']['source_state_json']
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
            or driver.identity(actual)!={'entries':356,'binary64_sha256':
                'b903a6af3288f53b37b08d0978ed268f08be788c8e4af8c4a5301bda0601d1f6'}
            or driver.identity(fine)!={'entries':16240,'binary64_sha256':
                '6a5392a820dce7947570d2ab4abedd5740e70a68d3af5abbb3e276d6801f1233'}
            or driver.identity(proposed)!={'entries':357,'binary64_sha256':
                '86174de157b3174a636063c8023b4dec039bb2625888264295f261a926153a59'}
            or driver.identity(pending)!={'entries':1,'binary64_sha256':
                '3fdd1fd0a488e029ac5c1c82f27943b4fbe387b4422240d6f02ac9b9a3db7a66'}
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
        raise ValueError('actual356/fine16240/proposed357 or unchanged trust differs')
    retained=terminal['actual_retained_state']
    qsha='95deda51f4fbca906e14fce050e6c0d76035fb767b43906615be7fe0d8679d1e'
    if (retained['q_identity']!=driver.identity(retained['q'])
            or retained['q_identity']!={'entries':97,'binary64_sha256':qsha}
            or retained['p']!=.181 or retained['stage']!=0
            or retained['accepted_as']!='complete_fine_feasible_metric_improvement'
            or not retained['qualified_on_this_fine_grid']
            or retained['scan']['radial_grid_identity']!={'entries':16240,'binary64_sha256':
                '6a5392a820dce7947570d2ab4abedd5740e70a68d3af5abbb3e276d6801f1233'}
            or retained['scan']['theta_nodes']!=3072
            or not retained['scan']['complete_fine_scan']
            or retained['scan']['eta_max']!=3.448896113433797e-05
            or retained['scan']['geometry_violation_max']!=0.
            or retained['scan']['working_geometry_violation_max']!=0.
            or retained['scan']['radial_grid_identity']!=driver.identity(fine)):
        raise ValueError('actual95de complete16240 qualification differs')
    warm=terminal['last_backend_callback_candidate']
    trial=terminal['last_completed_full_scan_trial']
    warmsha='5a723c52bd3a9ffd9ad76bf4b1fe00ffdcf0dec962095eaee23c15eea47a4b25'
    if (warm['q_identity']!=driver.identity(warm['q'])
            or warm['q_identity']!={'entries':97,'binary64_sha256':warmsha}
            or warm['actual_constraint_radial_identity']!=driver.identity(actual)
            or warm['actual_constraint_theta_nodes']!=1536 or warm['p']!=.181
            or warm['backend_extra']!=3.386845410078112e-05
            or warm['current_complete_backend_violation']!=1.1615275008594425e-05
            or warm['current_complete_backend_feasible'] or warm['retained_by_this_raw_callback']
            or warm['complete_fine_assessment']
            or not warm['retained_from_separate_assessment']
            or warm['separate_assessment_q_identity']!=retained['q_identity']
            or not warm['separate_assessment_complete_fine_assessment']
            or not warm['separate_assessment_is_not_raw_backend_point']
            or warm['separate_assessment_fraction']!=.5
            or warm['separate_assessment_epigraph']!=3.448896113777967e-05
            or warm['separate_assessment_complete_row_violation']!=0.
            or warm['last_physical_backtrack_fraction']!=.5
            or warm['last_physical_backtrack_halvings']!=1
            or trial['q_identity']!=retained['q_identity']
            or driver.identity(trial['q'])!=retained['q_identity']
            or trial['accepted_as']!='complete_fine_feasible_metric_improvement'
            or trial['scan']!=retained['scan']
            or trial['physical_assessment_fraction']!=.5
            or trial['backend_extra']!=3.448896113777967e-05):
        raise ValueError('last unqualified raw candidate cannot replace actual95de')
    counts=terminal['counts']
    if (terminal['elapsed_seconds']!=2444.1902206679997
            or counts['accepted_metric']!=11 or counts['complete_fine_scans']!=22
            or counts.get('accepted_geometry_restoration',0)!=0
            or counts['completed_outers']!=4
            or counts['complete_fine_radial_blocks']!=2794
            or counts['fine_radial_points_evaluated']!=357021
            or counts['completed_backend_Jacobians']!=9
            or counts['completed_backend_direction_blocks']!=117
            or counts['completed_backend_value_evaluations']!=49
            or terminal['current_backend_cost_not_yet_folded_into_completed_outers']!=
                {'complete_Jacobians':8,'completed_direction_blocks':104,'value_evaluations':44}
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
    ledger.update(new_scientific_seconds=terminal['elapsed_seconds'],source_run=45922821540,
        source_job=140257301670,source17_complete_Jacobians_and22_full_scans_not_replayed=True,
        source_current_eight_Jacobians104_blocks44_values_and_all_unclosed_work_retained=True,
        source_backend_internal_work_arrays_not_available=True,
        source_actual_material_mesh_sha256=terminal['field_receipt']['material_mesh_binary64_sha256'],
        original_raw_sha256=required['original_raw_sha256'],original_FINAL_JSON_sha256=required['FINAL_JSON_sha256'])
    source['resume97_origin'],source['resume97_state']=required,state
    source['resume97_input_sha256']=digest
    source['unqualified_warm_backend_trial']=warm
    source['prior_cost_ledger']['physical_pending339_original_terminal']=ledger
    return source,paid,fine


def emit(tag,value):
    if tag=='FINITE_LOCAL_TAIL_DEFINITION':
        value=dict(value)
        for key in ('source_49_backend_callbacks_are_not_replayed',
                    'source_warm_trial_has_no_fine_or_geometry_qualification',
                    'original_source_unadopted_proposal'):
            value.pop(key,None)
        value.update(schema=SCHEMA,original_source_actual_grid=[356,1536],first_new_grid=[357,1536],
            source_original_proposed_grid=[357,1536],source17_complete_Jacobians_and22_scans_not_replayed=True,
            source11_actual_metric_acceptances_not_replayed=True,
            all16240_required_fine_locations_and3072_angles_preserved=True,
            source_true_qualified_fine_is_identical16240=True,
            actual_retained_q_is95de_not_unqualified_raw5a723=True,
            source_last_raw_trial_had_no_complete_fine_qualification=True,
            source_last_raw_separate_half_copy_is_exactly_retained95de=True,
            source_actual_material_mesh_is0d_and_its_identity_is_not_relabelled=True,
            newly_constructed_field_actual_identity_is_recorded_without_relabeling=True,
            recorded_pending357_adds_two_midpoints_and_forces_original_complete_new_baseline=True,
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
