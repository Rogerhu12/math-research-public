#!/usr/bin/env python3
"""Continue the real 14d1 state and its original pending298 physical library.

The bound scientific driver is unchanged.  All source pending binary64
coordinates remain in the full fine grid, with the unchanged original coarse append rule.  Raw SLSQP and the
fully scanned physical best remain distinct; no backend work arrays are
invented.  A larger new fine grid requires its own original qualification.
"""
import hashlib
import json
from pathlib import Path
import sys

PARENT_SHA256 = '6122c313082e96eb2826beface953d963e82bb517a16bb1d3e14423ab5c3a03b'
parent_path = Path(__file__).with_name('r582_physical_pending279_resume_20261127.py')
if hashlib.sha256(parent_path.read_bytes()).hexdigest() != PARENT_SHA256:
    raise RuntimeError('the actual source paid-resume entry changed')
import r582_physical_pending279_resume_20261127 as parent

driver = parent.driver
SCHEMA = 'r582-actual-14d1-and-original-pending298-physical-resume-v1'
INPUT_SCHEMA = 'identified-14d1-terminal97q-with-all-pending298-v1'
original_emit = driver.emit


def load_input(raw, digest):
    encoded = sys.stdin.buffer.read() if raw == '@stdin' else raw.encode()
    if hashlib.sha256(encoded).hexdigest() != digest:
        raise ValueError('new 14d1/pending298 exact stdin identity differs')
    incoming = json.loads(encoded)
    if incoming.get('schema') != INPUT_SCHEMA:
        raise ValueError('wrong identified 14d1 source schema')
    required = {
        'run_id':45895078668, 'job_id':140166868607,
        'source_commit':'021c6d790ac7e6e2b163fe9db7870a28f3640ec1',
        'runtime_public_pull_commit':'021c6d790ac7e6e2b163fe9db7870a28f3640ec1',
        'source_entry_sha256':PARENT_SHA256,
        'original_raw_bytes':4790919,
        'original_raw_sha256':'a64bda0946806404c9a4d5777a0a57215061519cbf4bbab1dc9f5cb4ae6d7708',
        'FINAL_JSON_bytes':380450,
        'FINAL_JSON_sha256':'84707de70bbaf0cdb270f2363b112e33c32d2f810a0ee2f3055dfbfd1d9d43a7',
        'source_state_sha256':'1c6249edb3a98e28735869d63cbd629e313b0ef0673042484b72789b527395d0',
        'termination':'scientific_clock_checkpoint_not_complete',
    }
    if incoming['origin'] != required:
        raise ValueError('actual 14d1 natural terminal identity differs')
    prior_path = Path(__file__).resolve().parents[3] / (
        'topics/visible-flex-new-mechanism/computations/'
        'request-r582-physical-pending279-resume-20261127.json')
    prior_bytes = prior_path.read_bytes()
    if (len(prior_bytes) != 380989 or hashlib.sha256(prior_bytes).hexdigest() !=
            'c7ba6dcdacbe6982f9f09414d3275f26b8ffc8dfba509e6c1f54a76595186b05'):
        raise ValueError('published original paid ancestry request changed')
    prior_input = json.loads(prior_bytes)['lanes']['actual-a237-pending279']['source_state_json']
    source, paid, oldfine = parent.load_input(prior_input, required['source_state_sha256'])
    final_bytes = incoming['complete_original_FINAL_JSON'].encode()
    if (len(final_bytes) != required['FINAL_JSON_bytes'] or
            hashlib.sha256(final_bytes).hexdigest() != required['FINAL_JSON_sha256']):
        raise ValueError('complete original source FINAL bytes differ')
    terminal = json.loads(final_bytes)
    actual = driver.np.asarray(terminal['actual_constraint_radial_nodes'],dtype=float)
    fine = driver.np.asarray(terminal['actual_fine_radial_nodes'],dtype=float)
    proposed = driver.np.asarray(terminal['proposed_constraint_radial_nodes'],dtype=float)
    pending = driver.np.asarray(terminal['pending_radial_nodes'],dtype=float)
    if (terminal['schema'] != parent.SCHEMA or terminal['termination'] != required['termination']
            or terminal['stage'] != 0 or terminal['outer'] != 1 or terminal['phase'] != 'metric'
            or terminal['last_natural_OptimizeResult'] is not None
            or terminal['actual_grid_p'] != .181 or terminal['actual_retained_p'] != .181
            or terminal['proposed_or_current_p'] != .181
            or driver.identity(actual) != {'entries':296,'binary64_sha256':
                'fc6bb96e5ebfb8cf65c72ebce9cab8522236a2fc8d6a6236e7f4bf8b71f7ca73'}
            or driver.identity(fine) != {'entries':11100,'binary64_sha256':
                'd0d440392b18e0cda2277fc1756f62dffe3342286013b8b6852564b160d45004'}
            or driver.identity(proposed) != {'entries':298,'binary64_sha256':
                '766fddc2d159f0c70316aa64a6e14705d6b0add23333361e1bc846cb7f8b4dfd'}
            or not driver.np.array_equal(driver.append_nodes(actual,pending),proposed)
            or not set(oldfine).issubset(set(fine))
            or not set(actual).issubset(set(fine)) or not set(pending).issubset(set(fine))
            or len(pending) != 2 or len(set(pending)) != 2
            or terminal['actual_constraint_theta_nodes'] != 1536
            or terminal['actual_fine_theta_nodes'] != 3072
            or terminal['proposed_constraint_theta_nodes'] != 1536
            or terminal['pending_angular_upgrade'] or terminal['pending_angular_upgrade_evidence']
            or terminal['actual_backend_trust'] != 2.
            or terminal['proposed_next_trust'] != 2. or terminal['planned_current_trust'] != 2.):
        raise ValueError('actual296/fine11100/pending2/proposed298 or true trust differs')
    retained = terminal['actual_retained_state']
    qsha = '14d1a961e41fa87c152eb81f22837e5e54ba5014bdc5f92f05d70dc5fb5a4445'
    if (retained['q_identity'] != driver.identity(retained['q'])
            or retained['q_identity'] != {'entries':97,'binary64_sha256':qsha}
            or retained['p'] != .181 or retained['stage'] != 0
            or retained['accepted_as'] != 'complete_fine_feasible_metric_improvement'
            or not retained['qualified_on_this_fine_grid']
            or retained['scan']['radial_grid_identity'] != driver.identity(fine)
            or retained['scan']['theta_nodes'] != 3072
            or not retained['scan']['complete_fine_scan']
            or retained['scan']['eta_max'] != 4.2622659748238665e-05
            or retained['scan']['geometry_violation_max'] != 0.
            or retained['scan']['working_geometry_violation_max'] != 9.776581757700575e-10):
        raise ValueError('actual 14d1 full-fine physical qualification differs')
    warm = terminal['last_backend_callback_candidate']
    if (warm['q_identity'] != driver.identity(warm['q'])
            or warm['q_identity'] != {'entries':97,'binary64_sha256':
                '6f82fa536bca3ab27f014f152d4b7e38382d4ab9444d2f63bff3b32eb3cef1c0'}
            or warm['actual_constraint_radial_identity'] != driver.identity(actual)
            or warm['actual_constraint_theta_nodes'] != 1536
            or warm['p'] != .181 or warm['backend_extra'] != 4.2496748207922764e-05
            or warm['current_complete_backend_violation'] != 8.732223143831738e-07
            or warm['current_complete_backend_feasible'] or warm['complete_fine_assessment']
            or warm['retained_by_this_raw_callback']
            or not warm['retained_from_separate_assessment']
            or not warm['separate_assessment_complete_fine_assessment']
            or warm['separate_assessment_q_identity'] != retained['q_identity']
            or warm['separate_assessment_fraction'] != .5
            or terminal['last_completed_full_scan_trial']['q_identity'] != retained['q_identity']):
        raise ValueError('source raw warm and distinct true physical best were conflated')
    counts = terminal['counts']
    active = terminal['current_backend_cost_not_yet_folded_into_completed_outers']
    if (terminal['elapsed_seconds'] != 2375.001235837
            or counts['accepted_metric'] != 9 or counts['complete_fine_scans'] != 15
            or counts.get('accepted_geometry_restoration',0) != 0
            or counts.get('completed_outers',0) != 1
            or counts['complete_fine_radial_blocks'] != 1305
            or counts['fine_radial_points_evaluated'] != 166212
            or counts['completed_backend_Jacobians'] != 10
            or counts['completed_backend_direction_blocks'] != 130
            or counts['completed_backend_value_evaluations'] != 56
            or active != {'complete_Jacobians':2,'completed_direction_blocks':32,'value_evaluations':9}
            or terminal['new_directional_checks_this_run'] != 0
            or terminal['field_receipt']['material_mesh_binary64_sha256'] !=
                '0d222bd12ce8a61d0c88264c6fb5c82066f0ca058855b5bf7a670a53b483a991'):
        raise ValueError('source actual new costs, unclosed Jacobian, or field mesh differs')
    state = {name:terminal[name] for name in (
        'actual_retained_state','actual_constraint_radial_nodes','actual_constraint_theta_nodes',
        'actual_fine_radial_nodes','actual_fine_theta_nodes','proposed_constraint_radial_nodes',
        'proposed_constraint_theta_nodes','pending_radial_nodes','pending_angular_upgrade',
        'pending_angular_upgrade_evidence','actual_backend_trust','proposed_next_trust')}
    state.update(actual_constraint_radial_identity=driver.identity(actual),
        actual_fine_radial_identity=driver.identity(fine),
        paid_97q_directional_check=source['resume97_state']['paid_97q_directional_check'])
    ledger = {name:terminal[name] for name in (
        'counts','new_model_counts','R604_observation_counts',
        'current_backend_cost_not_yet_folded_into_completed_outers',
        'final_resonant_field_counts','final_stable_evaluator_counts','original_model_new_counts')}
    ledger.update(new_scientific_seconds=terminal['elapsed_seconds'],
        source_run=45895078668,source_job=140166868607,
        source_has12_complete_Jacobians_and6_further_completed_blocks=True,
        source15_complete_fine_scans_not_replayed=True,
        source_unclosed_backend_internal_work_arrays_not_available=True,
        original_raw_sha256=required['original_raw_sha256'],
        original_FINAL_JSON_sha256=required['FINAL_JSON_sha256'])
    source['resume97_origin'],source['resume97_state'] = required,state
    source['resume97_input_sha256'] = digest
    source['unqualified_warm_backend_trial'] = warm
    source['prior_cost_ledger']['physical_pending279_original_terminal'] = ledger
    return source,paid,fine


def emit(tag,value):
    if tag == 'FINITE_LOCAL_TAIL_DEFINITION':
        value = dict(value)
        for key in ('source_49_backend_callbacks_are_not_replayed',
                    'source_warm_trial_has_no_fine_or_geometry_qualification',
                    'original_source_unadopted_proposal'):
            value.pop(key,None)
        value.update(schema=SCHEMA,
            original_source_actual_grid=[296,1536],first_new_grid=[298,1536],
            source_original_proposed_grid=[298,1536],
            source12_complete_Jacobians_and6_further_direction_blocks_not_replayed=True,
            source9_actual_metric_acceptances_and15_complete_fine_scans_not_replayed=True,
            all11100_actual_fine_locations_and3072_angles_preserved=True,
            all2_original_pending_float_locations_remain_in_full_fine=True,
            original_coarse_append_rule_gives_both_new_pending_coordinates=True,
            original_pending298_proposal_adopted_before_new_backend=True,
            new_midpoint_or_fine_grid_requires_original_complete_requalification=True,
            source_raw_6f82_has_no_raw_complete_fine_or_raw_retained_qualification=True,
            source_raw_separate_halfstep_is_the_actual_fully_accepted_14d1=True,
            actual_retained_q_is_14d1_not_unqualified_raw_6f82=True,
            scientific_functions_and_original_all_group_acceptance_unchanged=True)
    original_emit(tag,value)


def main():
    driver.load_input = load_input
    driver.emit = emit
    driver.SCHEMA = SCHEMA
    driver.main()


if __name__ == '__main__':
    main()
