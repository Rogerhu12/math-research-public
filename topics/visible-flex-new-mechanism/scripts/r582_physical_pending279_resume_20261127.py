#!/usr/bin/env python3
"""Continue the real a237 state and its original pending279 physical library.

The bound scientific driver is unchanged.  All source pending binary64
coordinates remain in the full fine grid, including the two near pairs
merged by the already-defined coarse append rule.  Raw SLSQP and the
fully scanned physical best remain distinct; no backend work arrays are
invented.  A larger new fine grid requires its own original qualification.
"""
import hashlib
import json
from pathlib import Path
import sys

PARENT_SHA256 = 'fa104c10c344b681aff9fc840cfdbaf4a835b936e69fb087cecdc78080076085'
parent_path = Path(__file__).with_name('r582_physical_epigraph_paid_resume_20261127.py')
if hashlib.sha256(parent_path.read_bytes()).hexdigest() != PARENT_SHA256:
    raise RuntimeError('the actual source paid-resume entry changed')
import r582_physical_epigraph_paid_resume_20261127 as parent

driver = parent.driver
SCHEMA = 'r582-actual-a237-and-original-pending279-physical-resume-v1'
INPUT_SCHEMA = 'identified-a237-terminal97q-with-all-pending279-v1'
original_emit = driver.emit


def load_input(raw, digest):
    encoded = sys.stdin.buffer.read() if raw == '@stdin' else raw.encode()
    if hashlib.sha256(encoded).hexdigest() != digest:
        raise ValueError('new a237/pending279 exact stdin identity differs')
    incoming = json.loads(encoded)
    if incoming.get('schema') != INPUT_SCHEMA:
        raise ValueError('wrong identified a237 source schema')
    required = {
        'run_id':45887805731, 'job_id':140142780497,
        'source_commit':'0cce06dd57217f8b06af3a6eaf4018f445bda371',
        'runtime_public_pull_commit':'0cce06dd57217f8b06af3a6eaf4018f445bda371',
        'source_entry_sha256':PARENT_SHA256,
        'original_raw_bytes':6142044,
        'original_raw_sha256':'f7e67e989446d32c5c1331aace3e62dcaa2cf4e3160d859c7548d006391b7b21',
        'FINAL_JSON_bytes':364198,
        'FINAL_JSON_sha256':'e3371193ba4dcaa4df4d8298c856dce0663d2c4793d0cf205d625203af35ae47',
        'source_state_sha256':'fbad41027e6d653b2d5a8f26b3490b2db8596a6ae947aca2f56556e5ae286ee7',
        'termination':'scientific_clock_checkpoint_not_complete',
    }
    if incoming['origin'] != required:
        raise ValueError('actual a237 natural terminal identity differs')
    prior_path = Path(__file__).resolve().parents[3] / (
        'topics/visible-flex-new-mechanism/computations/'
        'request-r582-physical-paid-resume-20261127.json')
    prior_bytes = prior_path.read_bytes()
    if (len(prior_bytes) != 560396 or hashlib.sha256(prior_bytes).hexdigest() !=
            'bb6e575ecf55a5ef8ee1b1e3c3065039fd993bae3fcc87610468aeb0007057c8'):
        raise ValueError('published original paid ancestry request changed')
    prior_input = json.loads(prior_bytes)['lanes']['paid-physical97']['source_state_json']
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
            or terminal['stage'] != 0 or terminal['outer'] != 0 or terminal['phase'] != 'metric'
            or terminal['last_natural_OptimizeResult'] is not None
            or terminal['actual_grid_p'] != .181 or terminal['actual_retained_p'] != .181
            or terminal['proposed_or_current_p'] != .181
            or driver.identity(actual) != {'entries':243,'binary64_sha256':
                '30008c5092c32a76d539b3c9ae7059af04cc1d49e4206fc42f157ca22bc7b735'}
            or driver.identity(fine) != {'entries':11025,'binary64_sha256':
                '52fb28eafcee0110ac12d989a96f6f33871ab395b6b2c3bd448a73a90196fe4a'}
            or driver.identity(proposed) != {'entries':279,'binary64_sha256':
                'fe125fad53685c2fe214ba8a63a287218f54ea64d89a2a8d8dc67a2d84e77327'}
            or not driver.np.array_equal(driver.append_nodes(actual,pending),proposed)
            or not set(oldfine).issubset(set(fine))
            or not set(actual).issubset(set(fine)) or not set(pending).issubset(set(fine))
            or len(pending) != 38 or len(set(pending)) != 38
            or terminal['actual_constraint_theta_nodes'] != 1536
            or terminal['actual_fine_theta_nodes'] != 3072
            or terminal['proposed_constraint_theta_nodes'] != 1536
            or terminal['pending_angular_upgrade'] or terminal['pending_angular_upgrade_evidence']
            or terminal['actual_backend_trust'] != 2.
            or terminal['proposed_next_trust'] != 2. or terminal['planned_current_trust'] != 2.):
        raise ValueError('actual243/fine11025/pending38/proposed279 or true trust differs')
    retained = terminal['actual_retained_state']
    qsha = 'a2377220dacda9eefe63f25a2000441f0169a0db5de9bc23840f90e5037a895e'
    if (retained['q_identity'] != driver.identity(retained['q'])
            or retained['q_identity'] != {'entries':97,'binary64_sha256':qsha}
            or retained['p'] != .181 or retained['stage'] != 0
            or retained['accepted_as'] != 'complete_fine_feasible_metric_improvement'
            or not retained['qualified_on_this_fine_grid']
            or retained['scan']['radial_grid_identity'] != driver.identity(fine)
            or retained['scan']['theta_nodes'] != 3072
            or not retained['scan']['complete_fine_scan']
            or retained['scan']['eta_max'] != 4.8302220914394944e-05
            or retained['scan']['geometry_violation_max'] != 0.
            or retained['scan']['working_geometry_violation_max'] != 0.):
        raise ValueError('actual a237 full-fine physical qualification differs')
    warm = terminal['last_backend_callback_candidate']
    if (warm['q_identity'] != driver.identity(warm['q'])
            or warm['q_identity'] != {'entries':97,'binary64_sha256':
                'a14dedce9ecf12fb0337f4162e39b65bed931c816eaa1c19089c9f88585644c7'}
            or warm['actual_constraint_radial_identity'] != driver.identity(actual)
            or warm['actual_constraint_theta_nodes'] != 1536
            or warm['p'] != .181 or warm['backend_extra'] != 4.378993397866834e-05
            or warm['current_complete_backend_violation'] != 8.222251073122813e-06
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
    if (terminal['elapsed_seconds'] != 2371.7857200480003
            or counts['accepted_metric'] != 18 or counts['complete_fine_scans'] != 20
            or counts.get('accepted_geometry_restoration',0) != 0
            or counts.get('completed_outers',0) != 0
            or counts['complete_fine_radial_blocks'] != 1740
            or counts['fine_radial_points_evaluated'] != 220500
            or active != {'complete_Jacobians':19,'completed_direction_blocks':249,'value_evaluations':96}
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
        source_run=45887805731,source_job=140142780497,
        source_has19_complete_Jacobians_and2_further_completed_blocks=True,
        source20_complete_fine_scans_not_replayed=True,
        source_unclosed_backend_internal_work_arrays_not_available=True,
        original_raw_sha256=required['original_raw_sha256'],
        original_FINAL_JSON_sha256=required['FINAL_JSON_sha256'])
    source['resume97_origin'],source['resume97_state'] = required,state
    source['resume97_input_sha256'] = digest
    source['unqualified_warm_backend_trial'] = warm
    source['prior_cost_ledger']['physical_paid_resume_original_terminal'] = ledger
    return source,paid,fine


def emit(tag,value):
    if tag == 'FINITE_LOCAL_TAIL_DEFINITION':
        value = dict(value)
        for key in ('source_49_backend_callbacks_are_not_replayed',
                    'source_warm_trial_has_no_fine_or_geometry_qualification',
                    'original_source_unadopted_proposal'):
            value.pop(key,None)
        value.update(schema=SCHEMA,
            original_source_actual_grid=[243,1536],first_new_grid=[279,1536],
            source_original_proposed_grid=[279,1536],
            source19_complete_Jacobians_and2_further_direction_blocks_not_replayed=True,
            source18_actual_metric_acceptances_and20_complete_fine_scans_not_replayed=True,
            all11025_actual_fine_locations_and3072_angles_preserved=True,
            all38_original_pending_float_locations_remain_in_full_fine=True,
            original_coarse_append_rule_merges_two_near_pending_pairs=True,
            original_pending279_proposal_adopted_before_new_backend=True,
            new_midpoint_or_fine_grid_requires_original_complete_requalification=True,
            source_raw_a14_has_no_raw_complete_fine_or_raw_retained_qualification=True,
            source_raw_separate_halfstep_is_the_actual_fully_accepted_a237=True,
            actual_retained_q_is_a237_not_unqualified_raw_a14=True,
            scientific_functions_and_original_all_group_acceptance_unchanged=True)
    original_emit(tag,value)


def main():
    driver.load_input = load_input
    driver.emit = emit
    driver.SCHEMA = SCHEMA
    driver.main()


if __name__ == '__main__':
    main()
