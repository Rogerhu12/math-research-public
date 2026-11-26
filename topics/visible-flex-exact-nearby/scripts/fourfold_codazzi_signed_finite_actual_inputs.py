"""Metadata-only whole-input admission for actual SC/JF signed96 consumers.

Reuse the complete original TC validators and the original positive-chain
schema.  No numerical import, scalar evaluation, old target or future actual
is created.  The public owner also runs the original TC preflight on its
entire restored input tree, including the original full RW and NW admission.
"""
from __future__ import annotations
import hashlib, json

REPO = 'Rogerhu12/math-research-public'
WX_SHA256 = 'e9fc1611dc582e0264f0222069e03d8e9a1953616db540fc14896d4765abfb12'
TC_NAMES = ('state', 'matrix', 'negative', 'positive', 'prefix')


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def parse(raw):
    return json.loads(raw, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))


def check_bytes(raw, spec):
    require(len(raw) == spec['bytes'] and sha(raw) == spec['sha256'],
            'the whole immutable input bytes: '+spec['path'])
    if 'git_blob_sha' in spec:
        blob = hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        require(blob == spec['git_blob_sha'], 'the complete original Git blob')
    return parse(raw)


def published(actual_spec, execution):
    found = [value for value in execution['scientific_files']
             if value['path'] == actual_spec['path']]
    require(found == [{key: actual_spec[key] for key in ('path', 'bytes', 'sha256')}],
            'the execution binds exactly this complete scientific file')


def admit_positive_chain(contents, specs, original_reference, port_math):
    """Original strict full58/224/32 physical_pair and chain identity checks.

    The low inverse/PS/DP ancestry is retained by the whole actual physical
    gate's own accepted source/manifest/reference records, never replaced by
    six selected ports.  All224 records and both whole WPN32 rows are required.
    """
    pairs = {}
    for stage, count in (('gate', 58), ('ports', 224), ('wpn', 32)):
        ar, er, mr = (stage+'_'+suffix for suffix in ('actual', 'execution', 'manifest'))
        actual = check_bytes(contents[ar], specs[ar])
        execution = check_bytes(contents[er], specs[er])
        manifest = check_bytes(contents[mr], specs[mr])
        identity = actual['identity']
        require(actual['complete'] is True and actual['proved'] is True
                and actual['actual_returncode'] == 0 and actual['failure'] is None
                and execution['complete'] is True and execution['failure'] is None
                and execution['actual_child_returncode'] == 0
                and identity['kind'] == 'complete_actual_positive_physical_scalar_stage_v1'
                and identity['scalar_stage'] == stage
                and identity['manifest_sha256'] == execution['manifest_sha256'] == specs[mr]['sha256']
                and identity['run_id'] == execution['run_id']
                and identity['run_attempt'] == execution['run_attempt'] == '1',
                'the genuine completed original physical stage: '+stage)
        require(manifest['kind'] == 'actual_positive_physical_scalar_stage_inputs_v1'
                and manifest['stage'] == stage
                and sorted(actual) == manifest['allowed_scientific_fields']
                and actual['parameters'] == manifest['parameters']
                and actual['saved_record_count'] == count
                and actual['completed_targets'] == manifest['target_order']
                and set(actual['new_records']) == set(actual['completed_targets'])
                and count in manifest['complete_record_counts']
                and actual['stage'] == 'complete_'+stage+'_scalar_branch'
                and actual['result']['complete_new_record_order'] == actual['completed_targets']
                and actual['result']['topic_completion_proved'] is False,
                'the whole exact original fields and full record branch')
        require(execution['current_input_receipts'] == manifest['files']
                and identity['source_sha256'] == next(
                    item['sha256'] for item in manifest['files'] if item['role'] == 'science'),
                'the actual complete original numerical source and its execution')
        published(specs[ar], execution)
        for name in ('old_scientific_target_calls', 'new_arrays_published', 'new_artifacts', 'new_Releases'):
            require(actual[name] == 0, 'the original physical-stage scope: '+name)
        for record in actual['new_records'].values():
            require(isinstance(record, dict) and isinstance(record.get('ball'), str),
                    'every complete original saved physical scalar record')
        pairs[stage] = {'actual': actual, 'execution': execution, 'manifest': manifest}
    gate, ports, wpn = (pairs[stage]['actual'] for stage in ('gate', 'ports', 'wpn'))
    ref = gate['reference_identity']
    require(ref == original_reference
            and ports['reference_identity'] == wpn['reference_identity'] == ref
            and gate['result']['same_actual_internal_gate_passed'] is True
            and gate['result']['same_actual_physical_outer_gate_passed'] is True,
            'the same complete admitted true-root original low/high/physical inverse')
    for doc, roles in (
            (ports, ('gate_actual', 'gate_execution', 'gate_manifest')),
            (wpn, ('gate_actual', 'gate_execution', 'gate_manifest',
                   'ports_actual', 'ports_execution', 'ports_manifest'))):
        for role in roles:
            require(doc['whole_completed_inputs'][role]['file'] == specs[role],
                    'the same exact actual chain predecessor: '+role)
    for role in ('low_actual', 'low_execution', 'low_manifest', 'D_actual', 'D_execution',
                 'weighted_actual', 'weighted_execution'):
        require(gate['whole_completed_inputs'][role]
                == ports['whole_completed_inputs'][role]
                == wpn['whole_completed_inputs'][role],
                'the full unchanged low/reference/high input identity: '+role)
    p = ports['result']
    require(p['kind'] == port_math.KIND
            and p['reference_identity'] == ref
            and p['input_order'] == list(port_math.INPUT_ORDER)
            and p['output_order'] == list(port_math.OUTPUT_CODES)
            and p['output_qualifications'] == list(port_math.OUTPUT_QUALIFICATIONS)
            and p['complete_new_record_count'] == 224
            and p['complete_new_record_order'] == port_math.record_order(),
            'the entire original14 by16 table, physical units and qualifications')
    w = wpn['result']
    require(w['kind'] == 'complete_R141_WPN_both_rows_lifted_response_v1'
            and w['reference_identity'] == ref
            and w['input_order'] == ['finite', 'tail']
            and w['output_order'] == list(port_math.OUTPUT_CODES)
            and w['complete_new_record_count'] == 32
            and w['complete_new_record_order'] == [
                'wpn_%s_%s_upper'%(rhs, code)
                for rhs in ('finite', 'tail') for code in port_math.OUTPUT_CODES]
            and w['full_WOB_square_inverse_via_completed_physical_gate_and_exact_lifting'] is True
            and w['original193_coordinates_recovered_from_regular_w_not_arbitrary_a'] is True
            and w['independent_high_baseline_included_in_return_output'] is False,
            'both full original WPN rows and the exact lifted square inverse')
    return pairs


def admit_complete_TC(contents, specs, tc_owner):
    """Whole actual TC completion, NEVER a useful-looking subset or prefix."""
    manifest = check_bytes(contents['TC_manifest'], specs['TC_manifest'])
    execution = check_bytes(contents['TC_execution'], specs['TC_execution'])
    docs = {name: check_bytes(contents['TC_'+name], specs['TC_'+name]) for name in TC_NAMES}
    state = docs['state']
    require(manifest['kind'] == tc_owner.MANIFEST_KIND
            and manifest['scientific_kind'] == tc_owner.KIND
            and manifest['repository'] == REPO
            and manifest['parameters'] == tc_owner.PARAMETERS
            and manifest['runtime'] == tc_owner.RUNTIME
            and manifest['target_order'] == tc_owner.TARGETS
            and manifest['allowed_scientific_fields'] == tc_owner.STATE_FIELDS,
            'the complete original TC manifest and mathematical definition')
    require(sorted(state) == tc_owner.STATE_FIELDS
            and state['kind'] == tc_owner.KIND
            and state['complete'] is state['proved'] is True
            and state['actual_returncode'] == 0 and state['failure'] is None
            and state['parameters'] == tc_owner.PARAMETERS
            and state['completed_targets'] == tc_owner.TARGETS
            and state['stage'] == 'complete_finite_trial_only_mathematics'
            and state['old_scientific_target_calls'] == state['private_arrays_published'] == 0
            and state['input_identity']['manifest_sha256'] == specs['TC_manifest']['sha256'],
            'all three whole TC targets actually succeeded')
    require(execution['kind'] == 'R149_complete_true_root_finite_trial_execution_v1'
            and execution['repository'] == REPO
            and execution['complete'] is True and execution['failure'] is None
            and execution['actual_child_returncode'] == 0
            and execution['run_id'] == state['run_id']
            and execution['run_attempt'] == state['run_attempt'] == '1'
            and execution['manifest_sha256'] == specs['TC_manifest']['sha256']
            and execution['scientific_children'] == 1 and execution['scientific_started_utc']
            and execution['completed_natural_targets'] == tc_owner.TARGETS
            and execution['old_completed_targets_recomputed'] == 0
            and execution['new_arrays_published'] == execution['new_artifacts'] == execution['new_Releases'] == 0,
            'the whole successful actual TC numerical execution')
    # Exact input restoration is recorded separately from old scientific targets.
    old_calls = execution['old_numerical_producers_called']
    if old_calls:
        restoration = execution['necessary_input_reconstruction']
        require(old_calls == execution['necessary_input_reconstruction_children'] == 1
                and restoration['complete'] is True
                and restoration['necessary_input_reconstruction'] is True
                and restoration['actual_returncode'] == 0
                and restoration['old_QR_solve_called'] is False
                and restoration['old_residual_or_norm_targets_called'] == 0
                and restoration['whole_original_cubic_SHA_verified'] is True
                and len(restoration['complete_direction_input_receipts']) == 14,
                'one honestly counted exact original Hermite input restoration only')
    else:
        require(old_calls == 0, 'no unexplained original numerical producer calls')
    for name in TC_NAMES:
        published(specs['TC_'+name], execution)
    expected_files = {specs['TC_'+name]['path'] for name in TC_NAMES}
    require({item['path'] for item in execution['scientific_files']} == expected_files,
            'every whole TC scientific publication is retained')
    family = state['input_identity']['same_selected_family']
    manifest_specs = {item['path']: item for item in manifest['files']}
    for name in ('matrix', 'negative', 'positive'):
        doc = docs[name]
        origin = doc['input_manifest_sha256']
        if origin != specs['TC_manifest']['sha256']:
            prior_role = 'prior_'+name
            require(manifest.get('continuation') is not None
                    and prior_role in manifest['roles']
                    and all(manifest_specs[manifest['roles'][prior_role]][key]
                            == specs['TC_'+name][key] for key in ('bytes', 'sha256')),
                    'a verbatim inherited TC object retains its complete origin')
        tc_owner.validate_complete_result(doc, name, state['proposal'], origin, family)
        receipt = state[name+'_receipt']
        require(receipt == {'file': tc_owner.FILES[name], 'bytes': specs['TC_'+name]['bytes'],
                            'sha256': specs['TC_'+name]['sha256']},
                'the whole TC state identifies its exact complete natural object')
    require(docs['negative']['complete_waist_trial_norms'] == docs['matrix']['complete_waist_trial_norms'],
            'the negative target copies the same complete96 waist norms')
    prefix = docs['prefix']
    require(prefix['kind'] == 'R149_true_root_residual_full_cell_prefix_v1'
            and prefix['next_cell'] == prefix['complete_cell_count'] == prefix['total_cells']
            and prefix['whole_mathematical_target_complete'] is True
            and prefix['complete_cells_have_all_declared_sources'] is True
            and prefix['all96_columns_and_all_declared_source_components_retained'] is True
            and prefix['proposal_identity'] == state['proposal']
            and prefix['scientific_sources'] == state['input_identity']['scientific_sources'],
            'the complete all-cell/all96/all-source TC integration remains present')
    return {'manifest': manifest, 'execution': execution, **docs}


def admit_WX(raw, spec, true_root_interval):
    """The original complete selected left density receiver, including means."""
    require(spec['sha256'] == WX_SHA256, 'the same immutable complete WX result')
    execution = check_bytes(raw, spec)
    actual = execution['actual_scientific_receipt']
    require(execution['complete'] is True and execution['actual_returncode'] == 0
            and execution['actual_failure'] is None
            and execution['run_id'] == actual['run_id'] == '43763424840'
            and execution['run_attempt'] == actual['run_attempt'] == '1'
            and actual['kind'] == 'actual_true_waist_coordinates_from_saved_positive_products_v1'
            and actual['complete'] is actual['proved'] is True
            and actual['actual_returncode'] == 0 and actual['failure'] is None
            and len(actual['gates']) == 20 and all(x['passed'] is True for x in actual['gates'])
            and actual['arithmetic_bits'] == 320
            and execution['old_numerical_enclosures_recomputed'] == 0,
            'the whole original selected-coordinate successful execution')
    h = actual['complete_selected_H_coordinate_conclusion']
    common = actual['complete_selected_common_input_conclusion']
    require(h['only_same_selected_actual_conjugacy'] is True
            and h['all_density_Jacobians_and_normalized_measures_retained'] is True
            and h['independent_physical_mean_block_is_identity'] is True
            and common['no_projection_commuted_through_coordinate'] is True
            and common['rigid_rotation_isometry_does_not_change_norm'] is True
            and common['complete_inverse_H_output_L2_factor'] == h['complete_inverse_density_L2_upper']
            and actual['mathematical_parameters']['exact_root_interval'] == true_root_interval
            and actual['mathematical_parameters']['fixed_intrinsic_parameter'] == 'eta_0',
            'the full selected density Jacobian, original left order and both means')
    return h['complete_inverse_density_L2_upper']


def admit_JC(contents, specs, jc_owner, family, original_RW_manifest_sha):
    """Consume ALL seven actual JC scalars; never call its arithmetic again."""
    actual = check_bytes(contents['JC_actual'], specs['JC_actual'])
    execution = check_bytes(contents['JC_execution'], specs['JC_execution'])
    manifest = check_bytes(contents['JC_manifest'], specs['JC_manifest'])
    identity = actual['identity']
    require(manifest['kind'] == jc_owner.MANIFEST_KIND
            and manifest['scientific_kind'] == jc_owner.KIND
            and manifest['stage'] == jc_owner.STAGE
            and manifest['parameters'] == jc_owner.PARAMETERS
            and manifest['target_order'] == jc_owner.TARGETS
            and manifest['complete_record_counts'] == [7]
            and manifest['allowed_scientific_fields'] == jc_owner.SCI_FIELDS,
            'the whole unchanged JC seven-scalar definition')
    by_role = {item['role']: item for item in manifest['files']+manifest['historical_inputs']}
    require(actual['complete'] is actual['proved'] is True
            and actual['actual_returncode'] == 0 and actual['failure'] is None
            and actual['candidate_record'] is actual['current_target'] is None
            and actual['completed_targets'] == jc_owner.TARGETS
            and set(actual['new_records']) == set(jc_owner.TARGETS)
            and actual['saved_record_count'] == 7
            and sorted(actual) == jc_owner.SCI_FIELDS
            and actual['parameters'] == jc_owner.PARAMETERS
            and actual['stage'] == 'complete_'+jc_owner.STAGE+'_scalar_branch'
            and identity['kind'] == jc_owner.KIND
            and identity['scalar_stage'] == jc_owner.STAGE
            and identity['manifest_sha256'] == specs['JC_manifest']['sha256']
            and identity['source_sha256'] == by_role['science']['sha256']
            and identity['joint_math_sha256'] == by_role['joint_math']['sha256']
            and actual['whole_completed_inputs'] == by_role,
            'the complete original actual JC input/source/output identity')
    require(execution['kind'] == 'R149_complete_joint_compound_row_execution_v1'
            and execution['complete'] is True
            and execution['failure'] is None
            and execution['actual_child_returncode'] == 0
            and execution['original_scientific_complete'] is True
            and execution['original_scientific_failure'] is None
            and execution['run_id'] == identity['run_id']
            and execution['run_attempt'] == identity['run_attempt'] == '1'
            and execution['manifest_sha256'] == specs['JC_manifest']['sha256']
            and execution['old_completed_targets_recomputed'] == 0
            and execution['new_arrays_published'] == execution['new_artifacts'] == execution['new_Releases'] == 0,
            'the complete successful actual JC execution')
    published(specs['JC_actual'], execution)
    require(execution['scientific_files'] == [{key: specs['JC_actual'][key]
                                              for key in ('path', 'bytes', 'sha256')}],
            'the whole JC scientific publication is the single complete original file')
    require(actual['reference_identity'] == family
            and actual['selected_member_identity'] == {
                'run': '43588332723/1', 'loss': '1/250', 'physical_strip': '1/128',
                'original_RW_manifest_sha256': original_RW_manifest_sha,
                'all_old_true_and_false_loss_outcomes_preserved': True,
                'selected_parameter_replaced_by_a_numeric_point': False},
            'the same actual selected lift and SAME entire RW definition')
    for index, name in enumerate(jc_owner.TARGETS):
        record = actual['new_records'][name]
        require(set(record) == {'ball', 'bound'} and isinstance(record['ball'], str)
                and record['bound'] == ('lower' if index < 3 else 'upper'),
                'all seven actual directed JC records retained')
    result = actual['result']
    require(result['complete_new_record_count'] == 7
            and result['complete_new_record_order'] == jc_owner.TARGETS,
            'the complete JC target count and order')
    for name in ('complete_joint_row_operator_error_proved', 'strict_positive_saved_homotopy_lower',
                 'all_DFT_alias_and_infinite_compound_tails_paid',
                 'all_dependent_scalars_use_formal_readback_bounds', 'original_RW_trials_unchanged',
                 'true_target96_orthonormality_only', 'old_angle_nonunitarity_paid',
                 'both_physical_density_means_retained', 'full_incoming_row_requires_original_KW_factor',
                 'TC_trial_row_term_uses_original_fixed_Js_identity'):
        require(result[name] is True, 'the original complete JC qualification: '+name)
    for name in ('signed_PDE_columns_or_finite_inverse_proved', 'full_nu_phase_mean_Schur_proved',
                 'topic_completion_proved'):
        require(result[name] is False, 'the original JC scope is retained')
    for name in ('old_scientific_target_calls', 'new_arrays_published', 'new_artifacts', 'new_Releases'):
        require(actual[name] == 0, 'the original JC no-repeat scope: '+name)
    return {'actual': actual, 'execution': execution, 'manifest': manifest,
            'joint_row_error_record': actual['new_records'][jc_owner.TARGETS[-1]]}
