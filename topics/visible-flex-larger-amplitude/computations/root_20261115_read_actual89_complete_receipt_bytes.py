#!/usr/bin/env python3
"""Actual89 reader appendix: original bytes and JSON metadata only.

No scientific module is imported and no model, matrix, norm, derivative, root,
ODE, or optimization is evaluated. Large scientific payloads absent from the
small reader artifact are represented only by the actual Actions receipt.
"""
import ast
import gzip
import hashlib
import json
from pathlib import Path

ROOT = Path('/tmp/visible-larger-recovery-2207/actions-debug/visible-completed-readback-43676206729-1')
R = ROOT / 'request89-readback'
PRIMARY = Path('/tmp/visible-larger-actual89')
PUBLISHED = Path('/tmp/visible-larger-actual89-published')
PARENT = Path('/tmp/visible-larger-actual86-published')
REPO = Path('/workspace/scratch/visible-larger-recovered-20261114-1843/math-research-public')
COMP = REPO / 'topics/visible-flex-larger-amplitude/computations'
OUT = Path('/tmp/visible-larger-actual89-complete-reader')
READER = 'root_20261114_read_completed_twenty_six_prefix.py'
READER_SHA = '36743c90d689525b975cec0acc66cdfa8051588ff8ce38f61e52120ad94c8527'
WARM = 'twenty-six-condensed-warm'
PARENT_WARM = 'twenty-five-condensed-warm'
ORIGINAL_PIN = dict(run_id=43671882961, artifact_id=14145231618,
    artifact_name='visible-followup-condensedqp-43671882961-1',
    expected_size=687750414,
    expected_sha256='e2859210d8baf814f4b6f88fbea5a0157ebbfce55c4c6a02429d4c64848c3583')
READER_PIN = dict(run_id=43676206729,
    source_commit='0d3da53d5782b37933a94f638664262802ea0a47',
    job_id=132696813693, artifact_id=14146572662,
    artifact_name='visible-completed-readback-43676206729-1',
    bytes=1074115,
    sha256='00e4726259a05b92783daccdeaaba4a0b8a10e51f26e313f679a69b78cb7a61b',
    tuple_verification_scope='Root uniquely downloaded and verified official metadata, ZIP SHA, CRC and paths; this reader consumes the completed extracted directory.')


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def load(path):
    raw = path.read_bytes()
    decoded = gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw
    return json.loads(decoded), raw, decoded


def receipt(path, base=None):
    raw = path.read_bytes()
    return dict(file=str(path.relative_to(base)) if base else path.name,
        bytes=len(raw), sha256=digest(raw))


def verify(path, descriptor):
    got = receipt(path)
    assert got['bytes'] == descriptor['bytes'], (path, 'bytes')
    assert got['sha256'] == descriptor['sha256'], (path, 'sha256')
    return got


def subset(small, full):
    return all(key in full and value == full[key] for key, value in small.items())


def emit(name, value):
    raw = (json.dumps(value, ensure_ascii=False, sort_keys=True,
        indent=2, allow_nan=False) + '\n').encode()
    encoded = gzip.compress(raw, mtime=0) if name.endswith('.gz') else raw
    (OUT/name).write_bytes(encoded)
    result = dict(file=name, bytes=len(encoded), sha256=digest(encoded))
    if name.endswith('.gz'):
        assert gzip.decompress(encoded) == raw
        result.update(decoded_bytes=len(raw), decoded_sha256=digest(raw))
    return result


def original_gzip_copy(name, source):
    raw = source.read_bytes()
    zipped = gzip.compress(raw, mtime=0)
    assert gzip.decompress(zipped) == raw
    (OUT/name).write_bytes(zipped)
    return dict(file=name, bytes=len(zipped), sha256=digest(zipped),
        decoded_bytes=len(raw), decoded_sha256=digest(raw),
        original_file=str(source.relative_to(ROOT)), exact_original_bytes_preserved=True)


def metadata_views():
    """Use only the frozen reader's JSON-display projections, not its imports/main.

    This verifies serialization correspondence; the independent checks below
    separately compare complete original bytes and source identities.
    """
    raw = (COMP/READER).read_bytes()
    assert digest(raw) == READER_SHA
    tree = ast.parse(raw)
    names = {'scalars', 'compact', 'midpoint_view', 'collocation_view',
        'selected_domain', 'selected_angle_view', 'trial_view'}
    body = []
    namespace = {'AuditError': ValueError}
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
                isinstance(target, ast.Name) and target.id == 'OMIT'
                for target in node.targets):
            namespace['OMIT'] = ast.literal_eval(node.value)
        if isinstance(node, ast.FunctionDef) and node.name in names:
            body.append(node)
    assert {node.name for node in body} == names
    assert all(not isinstance(node, (ast.Import, ast.ImportFrom))
        for function in body for node in ast.walk(function))
    module = ast.fix_missing_locations(ast.Module(body=body, type_ignores=[]))
    exec(compile(module, '<frozen JSON-display projections only>', 'exec'), namespace)
    return namespace, sorted(names)


def main():
    assert (ROOT/'.download-complete').read_text().strip() == READER_PIN['sha256']
    OUT.mkdir(parents=True, exist_ok=True)
    primary_pin = {
        '2026-11-15-actual89-primary-identity-readback.json':
            (35922, '118e377166cfbe9f55aa9b98c3ed8411525bcfbcf269b73426477c225dff3438'),
        '2026-11-15-actual89-original-readout.json.gz':
            (107197, '5e0bd70674b6049c653bd24dfbd9c006076197cf55fe30b8297959d9cecf8fec'),
        '2026-11-15-actual-request89-twenty-six-query-step-and-cell487-limits.md':
            (26241, 'c0478968c63dac6a988c4b57e1bdd403eaa6289d0b84e16762680f38ca8c4b7f'),
    }
    prior = []
    for name, (size, sha) in primary_pin.items():
        verify(PRIMARY/name, dict(bytes=size, sha256=sha))
        prior.append(receipt(PRIMARY/name))
    p, _, _ = load(PRIMARY/'2026-11-15-actual89-primary-identity-readback.json')
    request, _, _ = load(ROOT/'completed-readback-request-identity.json')
    summary, summary_raw, _ = load(R/'completed-prefix-readback.json')
    audit, _, _ = load(R/'large-arrays/complete-original-byte-audit.json')
    transport, _, _ = load(R/'large-arrays/complete-transport-receipt.json')
    copy, _, _ = load(R/'large-arrays/original-report-copy-manifest.json')
    assert summary_raw == (R/'large-arrays/complete-readback-status.json').read_bytes()
    verify(R/summary['complete_byte_audit_artifact']['file'],
        summary['complete_byte_audit_artifact'])
    assert summary['completed'] and summary['phase'] == 'complete'
    assert summary['byte_audit_completed'] and not summary['mathematical_computation_performed']
    assert summary['original_artifact_pin'] == audit['original_artifact_pin'] == ORIGINAL_PIN
    assert transport['pinned_input'] == copy['original_artifact_pin'] == ORIGINAL_PIN
    assert summary['original_source_commit'] == p['source_commit'] == '032c513ab5db8aff98a6efca2070375418846098'
    assert summary['source_sha256'] == READER_SHA
    assert request['source_commit'] == READER_PIN['source_commit']
    assert request['separate_R276_diagnostic_requested'] is False
    assert request['request']['recover_original_publication'] is False
    assert request['request']['readback_kind'] == 'prefix26'
    assert request['request']['original_artifact'] == ORIGINAL_PIN
    assert request['request']['original_parent']['directory'] == 'parent86'
    assert request['this_binding_step_scientific_computation'] is False
    assert set(request['request']['source_sha256']) == {
        READER, 'exact_20261114_fetch_pinned_public_artifact.py',
        'root_20261114_publish_actions.py'}
    assert transport['success'] and not transport['scientific_computation_performed']
    assert transport['zip_verified_before_extraction']
    assert transport['download']['actual_sha256'] == ORIGINAL_PIN['expected_sha256']
    assert transport['download']['actual_size'] == ORIGINAL_PIN['expected_size']
    ext = transport['extraction']
    assert ext['per_file_size_CRC_and_SHA256_verified']
    assert ext['zip_paths_checked_before_any_extraction']
    assert ext['traversal_symlinks_special_files_duplicates_and_encryption_rejected']
    inventory = {x['path']: x for x in ext['files']}
    assert len(inventory) == len(ext['files']) == ext['file_count'] == 413
    assert sum(x['bytes'] for x in ext['files']) == ext['total_extracted_bytes'] == 1039629700
    assert all(x['final_mode'] == '0444' and x['symlink'] is False for x in ext['files'])

    # Recheck the original published packet, decoded bytes and both parent files.
    fetch, _, _ = load(PUBLISHED/'published-original-fetch.json')
    assert fetch['science_run'] == ORIGINAL_PIN['run_id']
    assert fetch['science_source'] == summary['original_source_commit']
    docs = {}
    for item in fetch['files']:
        doc, raw, decoded = load(PUBLISHED/item['file'])
        verify(PUBLISHED/item['file'], item)
        if 'original_sha256' in item:
            assert digest(decoded) == item['original_sha256']
            assert len(decoded) == item['original_bytes']
        docs[item['file']] = doc
    s = docs[f'{WARM}/driver-status.json.gz']
    m = docs[f'{WARM}/model-000.json']
    q = docs[f'{WARM}/condensed-QP-summary.json']
    w = docs[f'{WARM}/warm-001.json.gz']
    f = docs['physical-response/response-check.json.gz']
    pw, pw_raw, _ = load(PARENT/f'{PARENT_WARM}/warm-001.json.gz')
    ps, _, ps_decoded = load(PARENT/f'{PARENT_WARM}/driver-status.json.gz')
    ph, psh = digest(pw_raw), digest(ps_decoded)
    warm_sha = digest((PUBLISHED/f'{WARM}/warm-001.json.gz').read_bytes())
    entries = [s['twenty_six_query_projection_entry'],
        m['twenty_six_query_projection_entry'], w['twenty_six_query_projection_entry']]
    accepted = [t for t in m['trials'] if t['accepted']]
    schema = 'exact-constraint-twenty-six-query-condensed-complete-H-warm-v1'
    checks = {
        'original_parent_warm_sha256':ph == 'd38c6968225535cb26c46c9dc3f9892603ef0c94942d9c571356fa016bccf69e' and s['identity']['resume_sha256'] == ph and all(e['actual_resume_sha256'] == ph for e in entries),
        'original_parent_status_sha256':psh == '7d6e7fa1fa3e92397d353f1e9b7c2a9c12d750f9714c2e79b1cfdfc40862a235' and all(e['actual_parent_status_sha256'] == psh for e in entries),
        'parent_status_identity_is_parent_producer_subset':subset(ps['identity'],pw['optimization_warm']),
        'parent_status_binds_parent_warm':ps['latest_warm_sha256'] == ph,
        'complete_parent_producer_retained':w['optimization_warm']['resume_producer'] == pw['optimization_warm'],
        'actual_new_warm_bytes_match_status':s['latest_warm_sha256'] == warm_sha,
        'status_identity_is_new_producer_subset':subset(s['identity'],w['optimization_warm']),
        'status_iteration_is_original_model_subset':len(s['iterations']) == 1 and subset(s['iterations'][0],m),
        'FD_binds_actual_new_warm':f['prepared_sha256'] == warm_sha,
        'FD_whole_producer_matches_new_warm':f['optimization_warm'] == w['optimization_warm'],
        'mesh_preserved':w['mesh'] == pw['mesh'],
        'status_transparent_gzip_decode':digest(gzip.decompress((PUBLISHED/f'{WARM}/driver-status.json.gz').read_bytes())) == 'c78528682d239d941ccc1391df004c8da3b51d60b6315c6d30334828d0204540',
        'FD_transparent_gzip_decode':digest(gzip.decompress((PUBLISHED/'physical-response/response-check.json.gz').read_bytes())) == '12da677b5be6d4a74023b8c8241e18a8a133d3aba841a9d9d8dc64f233400246',
        'current_schema_binds_all_reports':s['schema'] == w['optimization_warm']['schema'] == f['optimization_warm']['schema'] == schema and all(e['optimizer_schema'] == schema for e in entries),
        'original_scientific_unaccepted_flags':s['success'] is False and s['new_coupled_finite_acceptance'] is False and w['success'] is False and w['new_coupled_finite_acceptance'] is False and f['full_BVP_solved'] is False and f['nonlinear_native_at_current_H_solved'] is False,
        'readback_accepted_original_trial':len(accepted) == 1 and accepted[0] is m['trials'][-1] and accepted[0]['alpha'] == .03125 and s['accepted_warm_steps'] == 1 and accepted[0]['actual_fixed_weight_merit'] == w['optimization_warm']['actual_fixed_weight_merit'],
        'published_original_fetch_manifest_matches_actual_files':True,
    }
    assert len(checks) == 17 and all(checks.values())
    assert checks == p['parent_and_report_checks']
    assert summary['actual_new_warm']['sha256'] == warm_sha
    assert summary['parent_warm']['sha256'] == ph
    assert summary['original_parent_status_decoded_sha256'] == psh
    assert len(s['identity']['source_sha256']) == 62
    assert len(f['consumed_source_sha256']) == 66
    assert request['request']['original_parent']['warm_sha256'] == ph
    assert request['request']['original_parent']['status_sha256'] == psh
    assert inventory['parent86/warm-001.json.gz']['sha256'] == ph
    assert inventory['parent86/driver-status.json']['sha256'] == psh
    assert summary['trial_count'] == len(m['trials']) == 6

    # Typed identity and integer layout only. No query state or B action is formed.
    left = [465,466,467,468,469,470,471,472,473,475,477,479,480,481,482,484,485]
    mid = [473,475,477,479,480,481,482,484,485]
    typed = [dict(kind='left-RMS',interval=j,fraction=0.17267316464601146)
        for j in left] + [dict(kind='collocation-midpoint',interval=j,fraction=0.5)
        for j in mid]
    assert w['query_specs'] == m['query_specs'] == m['domain_operator_export']['query_specs'] == typed
    assert all(entry['query_specs'] == typed for entry in entries)
    assert m['selected_angle_row_count'] == s['selected_angle_row_count'] == 53248
    layout = audit['domain']['continuous_layout_and_explicit_zero_columns']
    assert layout == summary['byte_audit_scope']['original_local_layout_audit']
    assert layout['declared_local_dimension'] == layout['actual_compiled_column_union_dimension'] == 7439
    assert layout['zero_layout_nodes'] == [] and layout['zero_layout_column_count'] == 0
    assert layout['declared_domain_layout_equals_actual_B_column_union'] is True
    assert layout['actual_endpoint_count'] == 22
    assert [(row['query_index'],row['kind'],row['interval']) for row in layout['block_column_maps']] == [
        (i,row['kind'],row['interval']) for i,row in enumerate(typed)]
    assert all(row['global_column_count'] == 679 and row['local_column_map_exact'] is True
        for row in layout['block_column_maps'])
    capture = audit['domain']['capture']
    assert capture['complete'] and capture['intervals'] == left
    assert capture['unique_endpoint_nodes'] == capture['stored_endpoint_variants'] == 22
    assert capture['second_complete_Jacobian_constructed'] is False
    assert capture['endpoint_pairs_bound_to_their_original_A_chunk'] is True
    assert capture['original_jacobian_return_values_unchanged'] is True
    assert m['domain_operator_export']['manifest_sha256'] == audit['domain']['manifest']['sha256']
    assert m['domain_operator_export']['model_sha256'] == audit['domain']['model_sha256']

    # Five original report byte copies. Four were in the earlier five-file
    # public packet (which also contained the warm); the comparison is new here.
    originals = {}
    copied = []
    for item in copy['unchanged_original_report_files']:
        path = R/item['artifact_file']
        verify(path,item)
        original = item['original_file']
        assert subset({'bytes':item['bytes'],'sha256':item['sha256']}, inventory[original])
        old = PUBLISHED/original
        previous_equal = None
        if old.is_file():
            previous_equal = path.read_bytes() == old.read_bytes()
            assert previous_equal
        originals[original] = load(path)[0]
        copied.append(dict(**item, locally_byte_equal_to_primary_public_original=previous_equal))
    assert len(copied) == 5 and sum(x['locally_byte_equal_to_primary_public_original'] is True for x in copied) == 4
    assert copy['original_files_not_reserialized'] and copy['no_scientific_computation']
    comparison = originals[f'{WARM}/condensed-versus-C-comparison.json']
    assert {k:v for k,v in comparison.items() if k != 'condensed_QP_entry'} == {
        k:v for k,v in q['comparison'].items() if k != 'condensed_QP_entry'}
    ce, qe = comparison['condensed_QP_entry'],q['comparison']['condensed_QP_entry']
    assert {k:v for k,v in ce.items() if k != 'query_specs'} == {k:v for k,v in qe.items() if k != 'query_specs'}
    assert qe['query_specs'] == dict(original_entries=len(ce['query_specs']),
        first=ce['query_specs'][0], last=ce['query_specs'][-1], complete_entries_in_result=True)

    # Validate scalar/display projections against the complete original JSON.
    views, view_names = metadata_views()
    scalars, compact, trial_view = (views[n] for n in ('scalars','compact','trial_view'))
    trial_doc, _, _ = load(R/'completed-prefix-trial-table.json')
    assert trial_doc['before'] == views['selected_domain'](m['before'])
    assert trial_doc['original_model_scalars'] == scalars(m)
    assert trial_doc['all_original_trials'] == [trial_view(t) for t in m['trials']]
    assert summary['accepted_trial'] == trial_view(m['trials'][-1], detailed=True)
    assert summary['nearest_previous_rejected_trial'] == trial_view(m['trials'][-2], detailed=True)
    assert summary['original_status'] == scalars(s)
    assert summary['original_model_scalars'] == scalars(m)
    assert summary['original_FD_summary'] == scalars(f)
    fd_small, _, _ = load(R/'completed-prefix-FD.json')
    assert all(fd_small[k] == v for k,v in scalars(f).items())
    assert fd_small['source_ledger'] == f['consumed_source_sha256']
    assert fd_small['actual_warm_native_height'] == f['actual_warm_native_height']
    assert fd_small['original_complete_producer_canon_sha256'] == digest(json.dumps(
        f['optimization_warm'], sort_keys=True, separators=(',',':'),
        ensure_ascii=False, allow_nan=False).encode())
    for k in ('direct_boundary','separated_boundary'):
        assert fd_small[k] == scalars(f.get(k))
    qp_small, _, _ = load(R/'completed-prefix-QP-scalars.json')
    assert qp_small == dict(comparison=scalars(comparison),
        original_C_selection_scalars=scalars(comparison.get('original_C_selection')),
        selected_selection_scalars=scalars(comparison.get('condensed_candidate_selection')),
        final_actual_full_model_evidence=compact(comparison.get('final_actual_full_model_evidence')),
        local_QP_report_scalars=scalars(q.get('local_QP_report')),
        last_saved_local_stage=compact(q.get('last_saved_local_stage')),
        condensation_report_scalars=scalars(q.get('condensation_report')),
        last_recovery_scalars=scalars(q.get('condensation_report',{}).get('last_recovery')))

    # Source crosswalk: every former FD source, plus eleven observer wrappers.
    source_map = {x['source']:x for x in audit['source_files']}
    prior_map = {x['name']:x for x in p['verified_sources']}
    assert len(source_map) == len(audit['source_files']) == 77
    assert len(prior_map) == 66 and set(prior_map) <= set(source_map)
    assert f['consumed_source_sha256'] == {k:v['sha256'] for k,v in prior_map.items()}
    sources = []
    for name, item in sorted(source_map.items()):
        assert item['verified'] and item['sha256'] == item['expected_sha256']
        path = REPO/item['path']
        got = receipt(path)
        assert got['sha256'] == item['sha256']
        if name in prior_map:
            assert prior_map[name]['sha256'] == item['sha256']
            assert prior_map[name]['bytes'] == got['bytes']
        sources.append(dict(name=name, bytes=got['bytes'], sha256=got['sha256'],
            original_FD66_member=name in prior_map,
            Actions_reader_verified=True, local_frozen_source_rehashed=True))
    extra = [x for x in sources if not x['original_FD66_member']]
    assert len(extra) == 11 and all(x['name'].endswith('_collocation_observer_warm.py') for x in extra)
    wrapper = p['additional_observer_wrapper']
    assert source_map[wrapper['name']]['sha256'] == wrapper['sha256']

    # Metadata-only cross-check of Actions raw-payload audits to its complete
    # ZIP extraction inventory. No absent NPZ/f64 is read or reconstructed.
    linked = []
    def link(item, prefix, category):
        path = str(Path(prefix)/item['file']) if prefix else item['file']
        actual = inventory[path]
        assert item['bytes'] == actual['bytes'] and item['sha256'] == actual['sha256'], (category,path)
        linked.append(dict(category=category,file=path,bytes=item['bytes'],sha256=item['sha256']))
    for item in audit['domain']['files']:
        link(item,f'{WARM}/domain-operator','domain_NPZ')
    for item in audit['condensed']['files']:
        link(item,WARM,'condensed_NPZ')
    for item in audit['root_raw']['files']:
        link(item,'','root_raw')
    for item in audit['observers']['collocation']:
        link(item,'','collocation_observer_JSON')
    for item in audit['observers']['midpoint_descriptors']:
        link(item,'','midpoint_observer_NPZ')
    for item in (audit['domain']['manifest'],audit['condensed']['manifest'],
            audit['condensed']['result'],audit['root_raw']['status']):
        link(item,'','manifest_or_status')
    assert len(audit['domain']['files']) == audit['domain']['file_count'] == 232
    assert sum(len(x['arrays']) for x in audit['domain']['files']) == audit['domain']['array_count'] == 1510
    assert len(audit['domain']['complete_group_byte_combinations']) == 79
    groups = {item['label']:item for item in audit['domain']['complete_group_byte_combinations']}
    assert len(groups) == 79 and set(groups) == {
        f'query-{j}/{part}' for j in range(26) for part in ('rows','Gamma','Pi')} | {'all-typed-query-beta'}
    for j in range(26):
        for part,shape,size in (('rows',[2048,679],11124736),
                ('Gamma',[2048,338],5537792),('Pi',[2048,3],49152)):
            item = groups[f'query-{j}/{part}']
            assert item['shape'] == shape and item['bytes'] == size and item['dtype'] == '<f8'
            assert item['parts'] == 8
    assert groups['all-typed-query-beta']['shape'] == [53248]
    assert groups['all-typed-query-beta']['parts'] == 208
    domain_base = next(item for item in audit['domain']['files'] if item['file'] == 'base-and-local-layout.npz')['arrays']
    assert groups['all-typed-query-beta']['raw_sha256'] == domain_base['beta_squared']['raw_sha256']
    assert domain_base['local_indices'] == layout['actual_compiled_column_union_identity']
    for key,name in (('mesh','mesh'),('y','augmented_y'),('rhs','augmented_f'),('coordinate_scale','coordinate_scale')):
        assert subset(capture['base_identity'][name],domain_base[key])
    assert len(audit['condensed']['files']) == audit['condensed']['file_count'] == 108
    assert len(audit['condensed']['complete_array_byte_combinations']) == audit['condensed']['unique_complete_arrays'] == 38
    assert audit['condensed']['reference_count'] == 42
    assert len(audit['root_raw']['files']) == audit['root_raw']['file_count'] == 14
    assert sum(x['bytes'] for x in audit['root_raw']['files']) == audit['root_raw']['bytes'] == 454456080
    assert audit['root_raw']['full_factor_file_byte_audit'] is False
    assert audit['root_raw']['original_complete_chain_factor_RAM_only'] is True
    arrays = {item['label']:item for item in audit['condensed']['complete_array_byte_combinations']}
    raw_arrays = {item['name']:item for item in audit['root_raw']['files']}
    assert arrays['original_g']['raw_sha256'] == raw_arrays['original-g']['sha256']
    assert arrays['actual_conditional_recovery']['raw_sha256'] == raw_arrays['recovery-000-actual-full']['sha256']
    assert arrays['local_QP_result/local_candidate']['raw_sha256'] == raw_arrays['recovery-000-requested-local']['sha256']
    assert domain_base['local_indices']['raw_sha256'] == raw_arrays['local-indices']['sha256']
    assert raw_arrays['local-root']['shape'] == [7439,7439]
    assert raw_arrays['local-root']['bytes'] == 442709768
    obs = audit['observers']
    assert len(obs['collocation']) == 15 and len(obs['midpoint_descriptors']) == 8
    assert sorted(obs['midpoint_payloads_present']) == sorted(obs['midpoint_payloads_matched'])
    assert sorted(str(Path(x['file']).relative_to(WARM)) for x in obs['midpoint_descriptors']) == sorted(obs['midpoint_payloads_matched'])
    assert obs['every_midpoint_file_has_original_descriptor']
    assert obs['no_extra_evaluate_or_RHS_or_J_calls']
    assert [item['evaluate_call'] for item in obs['collocation']] == list(range(1,16))
    instances = obs['original_collocation_run_summary']['instances']
    assert len(instances) == 1 and instances[0]['original_evaluate_calls'] == 15
    assert instances[0]['original_weights_calls'] == 1 and instances[0]['observer_errors'] == 0
    assert audit['domain']['no_matrix_action_performed'] and audit['condensed']['no_model_action_performed']
    assert audit['root_raw']['no_scientific_computation_performed']
    assert audit['no_scientific_module_imported']

    # Individual links for the former 17 primary checks. The paired raw files
    # repeat those checks locally; reader receipts extend the same identities.
    anchors = {
        'original_parent_warm_sha256':'summary.parent_warm + requested_parent_warm_sha256; original transport parent86/warm-001.json.gz',
        'original_parent_status_sha256':'summary.original_parent_status_decoded_sha256 + requested_parent_status_sha256',
        'parent_status_identity_is_parent_producer_subset':'reader source readout parent subset check; pinned parent pair repeated locally',
        'parent_status_binds_parent_warm':'reader source readout Parent pair binding; same raw parent pair',
        'complete_parent_producer_retained':'summary.full_original_parent_producer_retained; same complete original status/warm/FD producer',
        'actual_new_warm_bytes_match_status':'summary.actual_new_warm; status latest_warm_sha256; transport warm receipt',
        'status_identity_is_new_producer_subset':'summary.status_and_newwarm_and_FD_original_producer_bound',
        'status_iteration_is_original_model_subset':'complete unchanged status/model originals + original trial table projection',
        'FD_binds_actual_new_warm':'FD.prepared_sha256 = summary.actual_new_warm.sha256',
        'FD_whole_producer_matches_new_warm':'summary.status_and_newwarm_and_FD_original_producer_bound + FD complete-producer canonical SHA',
        'mesh_preserved':'same pinned parent/current warm bytes; original mesh equality repeated locally, not a new scientific evaluation',
        'status_transparent_gzip_decode':'complete original status byte copy equals prior decoded bytes exactly',
        'FD_transparent_gzip_decode':'complete original FD byte copy equals prior decoded bytes exactly',
        'current_schema_binds_all_reports':'summary.original_status.schema and actual original warm/FD/entry schemas',
        'original_scientific_unaccepted_flags':'summary.original_status / actual_new_warm_flags / original_FD_summary false acceptance flags',
        'readback_accepted_original_trial':'summary.accepted_trial + all six original trials; no new trial executed',
        'published_original_fetch_manifest_matches_actual_files':'original published fetch manifest rechecked; four overlapping copied reports byte-equal; complete transport metadata binds originals',
    }
    crosswalk = [dict(primary_check=k, primary_recorded_value=p['parent_and_report_checks'][k],
        local_repeat_from_original_bytes=checks[k], completed_reader_evidence=anchors[k])
        for k in sorted(checks)]
    local_files = [receipt(path,ROOT) for path in sorted(ROOT.rglob('*')) if path.is_file()]
    assert all(not path.is_symlink() for path in ROOT.rglob('*'))
    preserved_original_evidence = [original_gzip_copy(
        '2026-11-15-actual89-original-complete-byte-audit.json.gz',
        R/'large-arrays/complete-original-byte-audit.json'),
        original_gzip_copy('2026-11-15-actual89-original-transport-receipt.json.gz',
            R/'large-arrays/complete-transport-receipt.json'),
        original_gzip_copy('2026-11-15-actual89-original-reader-summary.json.gz',
            R/'completed-prefix-readback.json')]
    scope = dict(schema='actual89-complete-reader-literal-scope-v1',
        reader_tuple=READER_PIN, original_tuple=ORIGINAL_PIN,
        original_source_commit=summary['original_source_commit'],
        original_request_identity=request,
        source_files=source_map,
        original_completed_reader_summary=summary,
        original_domain_capture_scalars={k:v for k,v in audit['domain']['capture'].items()
            if not isinstance(v,(dict,list))},
        original_typed_queries=typed, original_integer_layout=layout,
        original_domain_group_receipts=audit['domain']['complete_group_byte_combinations'],
        original_condensed_complete_array_receipts=audit['condensed']['complete_array_byte_combinations'],
        original_root_raw_receipts=audit['root_raw']['files'],
        original_observer_run_summary=obs['original_collocation_run_summary'],
        original_midpoint_receipts=obs['midpoint_descriptors'],
        original_transport_scope={k:v for k,v in ext.items() if k not in ('files','directories')},
        no_scientific_computation=True,
        absent_large_payloads_locally_rehashed=False,
        original_R276_requested=False, original_publication_recovery_requested=False,
        values_are_original_report_fields_not_new_scientific_diagnostics=True)
    scope_receipt = emit('2026-11-15-actual89-complete-reader-literal-scope.json.gz',scope)
    output = dict(schema='actual89-complete-reader-primary17-source66-crosswalk-v1',
        reader_tuple=READER_PIN, original_tuple=ORIGINAL_PIN,
        earlier_primary_files=prior,
        no_scientific_computation=True, no_scientific_module_imported=True,
        no_download_performed=True, raw_scientific_ZIP_not_present_or_reprocessed_locally=True,
        byte_checks_completed=True, primary_relationship_count=17,
        primary_relationship_crosswalk=crosswalk,
        original_report_copies=copied,
        comparison_new_copy_matches_prior_QP_summary_except_declared_query_compaction=True,
        previous_source_count=66, completed_Actions_source_count=77,
        source_crosswalk=sources, eleven_additional_sources=extra,
        current_wrapper_also_equals_primary_extra_wrapper=True,
        completed_status_duplicate_is_byte_identical=True,
        original_display_projections_match_full_original_JSON=True,
        complete_typed_query_identity_and_integer_layout_bound=True,
        typed_array_group_labels_shapes_and_parts_complete=True,
        root_raw_to_condensed_and_domain_identity_links_equal=True,
        JSON_only_projection_functions_used=view_names,
        projection_reader_source_sha256=READER_SHA,
        local_small_artifact_file_count=len(local_files),
        local_small_artifact_files=local_files,
        Actions_raw_payload_descriptors_crosslinked_to_transport=len(linked),
        Actions_raw_payload_descriptor_crosswalk=linked,
        Actions_reported_complete_byte_scope=summary['byte_audit_scope'],
        full_QR_factor_payload_independently_audited=False,
        full_QR_factor_payload_originally_exported=False,
        full_original_A_factor_input_hashes_are_not_new_full_array_payload_audit=True,
        no_extra_R276_invocation=True, no_original_publication_recovery_invocation=True,
        green_generic_steps_were_unrequested_noops=True,
        exact_original_evidence_gzip_copies=preserved_original_evidence,
        scientific_arithmetic_performed_in_this_readback=False,
        original_accepted_step_and_scientific_unaccepted_flags_preserved=True,
        literal_scope=scope_receipt)
    audit_receipt = emit('2026-11-15-actual89-complete-reader-crosswalk-and-byte-audit.json.gz',output)
    summary_receipt = emit('2026-11-15-actual89-complete-reader-appendix-summary.json',
        dict(completed=True, byte_only=True, original_scientific_acceptance_unchanged=True,
            reader_tuple=READER_PIN, original_tuple=ORIGINAL_PIN,
            primary_relationships_repeated=17, primary_FD_source_count=66,
            full_source_count=77, additional_observer_wrapper_count=11,
            current_mathematical_source_count=len(s['identity']['source_sha256']),
            typed_query_count=26, typed_row_count=53248, local_dimension=7439,
            domain_NPZ_count=232, domain_NPY_count=1510, complete_typed_array_groups=79,
            condensed_NPZ_count=108, condensed_NPY_count=108,
            condensed_complete_arrays=38, condensed_reference_count=42,
            root_raw_count=14, root_raw_bytes=454456080,
            observer_evaluate_count=15, observer_weights_count=1, observer_error_count=0,
            midpoint_packet_count=8, original_archive_member_count=413,
            original_archive_extracted_bytes=1039629700,
            metadata_raw_descriptor_crosslinks=len(linked),
            local_small_reader_file_count=len(local_files),
            unexported_full_factor_payload_audited=False,
            R276_requested=False, publication_recovery_requested=False,
            scope=scope_receipt,audit=audit_receipt,original_evidence=preserved_original_evidence))
    print(json.dumps(dict(completed=True, summary=summary_receipt, scope=scope_receipt, audit=audit_receipt,
        primary_checks=17, old_sources=66, full_reader_sources=77,
        local_small_artifact_files=len(local_files),
        metadata_only_raw_descriptor_crosslinks=len(linked)),indent=2))


if __name__ == '__main__':
    main()
