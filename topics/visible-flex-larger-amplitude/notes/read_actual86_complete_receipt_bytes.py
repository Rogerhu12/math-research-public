#!/usr/bin/env python3
"""Actual86 reader appendix: original bytes and JSON metadata only.

No scientific module is imported and no model, matrix, norm, derivative, root,
ODE, or optimization is evaluated. Large scientific payloads absent from the
small reader artifact are represented only by the actual Actions receipt.
"""
import ast
import gzip
import hashlib
import json
from pathlib import Path

ROOT = Path('/tmp/visible-larger-recovery-2207/actions-debug/visible-completed-readback-43671332524-1')
R = ROOT / 'request86-readback'
PRIMARY = Path('/tmp/visible-larger-actual86')
PUBLISHED = Path('/tmp/visible-larger-actual86-published')
PARENT = Path('/tmp/visible-larger-actual84-published')
REPO = Path('/workspace/scratch/visible-larger-recovered-20261114-1843/math-research-public')
COMP = REPO / 'topics/visible-flex-larger-amplitude/computations'
OUT = Path('/tmp/visible-larger-actual86-complete-reader')
READER = 'root_20261114_read_completed_twenty_five_prefix.py'
READER_SHA = '9239b31016fde72f55961bc33e36dd014d8cf051df8aaca1fb3f475f8494e8cb'
WARM = 'twenty-five-condensed-warm'
ORIGINAL_PIN = dict(run_id=43668743515, artifact_id=14143632174,
    artifact_name='visible-followup-condensedqp-43668743515-1',
    expected_size=668271416,
    expected_sha256='1fb22c28c479cd1132ead304d32642abfacb1d7149e0028ef5036f30a915bc75')
READER_PIN = dict(run_id=43671332524,
    source_commit='34d26d1e220a9222ee0559253eb3c61be855493b',
    job_id=132681821546, artifact_id=14144590986,
    artifact_name='visible-completed-readback-43671332524-1',
    bytes=1006464,
    sha256='2d373d6c3ca68fe486d6f5e391f20c121469824d3640978fa32a48b9db906185',
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
    (OUT/name).write_bytes(raw)
    return dict(file=name, bytes=len(raw), sha256=digest(raw))


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
    assert (ROOT/'.download-complete').is_file()
    OUT.mkdir(parents=True, exist_ok=True)
    primary_pin = {
        '2026-11-15-actual86-primary-identity-readback.json':
            (34862, '3e51322b494581a7e95cf59dde125cbff2d73ff349fce3a45f7956507fa59bd0'),
        '2026-11-15-actual86-original-readout.json.gz':
            (100555, '7a4ada8e9055b5d36505bb60809f4cb77af324cdd9831ca500b7f323832a96d0'),
        '2026-11-15-actual-request86-same-twenty-five-query-mid479-limit.md':
            (19035, '6d6884896e6699020259afc5e682abcfee027cbe79b7e19087af33192add04fe'),
    }
    prior = []
    for name, (size, sha) in primary_pin.items():
        verify(PRIMARY/name, dict(bytes=size, sha256=sha))
        prior.append(receipt(PRIMARY/name))
    p, _, _ = load(PRIMARY/'2026-11-15-actual86-primary-identity-readback.json')
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
    assert summary['original_source_commit'] == p['source_commit'] == '8d199eda5c1f1df162ded244e8dfd012e0c8d127'
    assert summary['source_sha256'] == READER_SHA
    assert request['separate_R276_diagnostic_requested'] is False
    assert transport['success'] and not transport['scientific_computation_performed']
    assert transport['zip_verified_before_extraction']
    assert transport['download']['actual_sha256'] == ORIGINAL_PIN['expected_sha256']
    assert transport['download']['actual_size'] == ORIGINAL_PIN['expected_size']
    ext = transport['extraction']
    assert ext['per_file_size_CRC_and_SHA256_verified']
    assert ext['zip_paths_checked_before_any_extraction']
    assert ext['traversal_symlinks_special_files_duplicates_and_encryption_rejected']
    inventory = {x['path']: x for x in ext['files']}
    assert len(inventory) == len(ext['files']) == ext['file_count'] == 402
    assert sum(x['bytes'] for x in ext['files']) == ext['total_extracted_bytes'] == 1022000889
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
    pw, pw_raw, _ = load(PARENT/f'{WARM}/warm-001.json.gz')
    ps, _, ps_decoded = load(PARENT/f'{WARM}/driver-status.json.gz')
    ph, psh = digest(pw_raw), digest(ps_decoded)
    warm_sha = digest((PUBLISHED/f'{WARM}/warm-001.json.gz').read_bytes())
    entries = [s['twenty_five_query_projection_entry'],
        m['twenty_five_query_projection_entry'], w['twenty_five_query_projection_entry']]
    accepted = [t for t in m['trials'] if t['accepted']]
    schema = 'exact-constraint-twenty-five-query-condensed-complete-H-warm-v1'
    checks = {
        'original_parent_warm_sha256':ph == 'fead4e7b8c1c78b62c8adef0d122a09ea12e7e3a94b0586ba2e59a63c3b429af' and s['identity']['resume_sha256'] == ph and all(e['actual_resume_sha256'] == ph for e in entries),
        'original_parent_status_sha256':psh == '8ad4ae64ccf4a84106a22db9f60c3abedfe4efae67d467b59aa6c06480b9bbde' and all(e['actual_parent_status_sha256'] == psh for e in entries),
        'parent_status_identity_is_parent_producer_subset':subset(ps['identity'],pw['optimization_warm']),
        'parent_status_binds_parent_warm':ps['latest_warm_sha256'] == ph,
        'complete_parent_producer_retained':w['optimization_warm']['resume_producer'] == pw['optimization_warm'],
        'actual_new_warm_bytes_match_status':s['latest_warm_sha256'] == warm_sha,
        'status_identity_is_new_producer_subset':subset(s['identity'],w['optimization_warm']),
        'status_iteration_is_original_model_subset':len(s['iterations']) == 1 and subset(s['iterations'][0],m),
        'FD_binds_actual_new_warm':f['prepared_sha256'] == warm_sha,
        'FD_whole_producer_matches_new_warm':f['optimization_warm'] == w['optimization_warm'],
        'mesh_preserved':w['mesh'] == pw['mesh'],
        'status_transparent_gzip_decode':digest(gzip.decompress((PUBLISHED/f'{WARM}/driver-status.json.gz').read_bytes())) == '7d6e7fa1fa3e92397d353f1e9b7c2a9c12d750f9714c2e79b1cfdfc40862a235',
        'FD_transparent_gzip_decode':digest(gzip.decompress((PUBLISHED/'physical-response/response-check.json.gz').read_bytes())) == '8c6df8ccb7c9b7e1ba983b6073de8d794a1c60600f016b2f6a1b482a1fb13acc',
        'current_schema_binds_all_reports':s['schema'] == w['optimization_warm']['schema'] == f['optimization_warm']['schema'] == schema and all(e['optimizer_schema'] == schema for e in entries),
        'original_scientific_unaccepted_flags':s['success'] is False and s['new_coupled_finite_acceptance'] is False and w['success'] is False and w['new_coupled_finite_acceptance'] is False and f['full_BVP_solved'] is False and f['nonlinear_native_at_current_H_solved'] is False,
        'readback_accepted_original_trial':len(accepted) == 1 and accepted[0] is m['trials'][-1] and accepted[0]['alpha'] == .0625 and s['accepted_warm_steps'] == 1 and accepted[0]['actual_fixed_weight_merit'] == w['optimization_warm']['actual_fixed_weight_merit'],
        'published_original_fetch_manifest_matches_actual_files':True,
    }
    assert len(checks) == 17 and all(checks.values())
    assert checks == p['parent_and_report_checks']
    assert summary['actual_new_warm']['sha256'] == warm_sha
    assert summary['parent_warm']['sha256'] == ph
    assert summary['original_parent_status_decoded_sha256'] == psh

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

    # Source crosswalk: every former FD source, plus ten observer wrappers.
    source_map = {x['source']:x for x in audit['source_files']}
    prior_map = {x['name']:x for x in p['verified_sources']}
    assert len(source_map) == len(audit['source_files']) == 74
    assert len(prior_map) == 64 and set(prior_map) <= set(source_map)
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
            original_FD64_member=name in prior_map,
            Actions_reader_verified=True, local_frozen_source_rehashed=True))
    extra = [x for x in sources if not x['original_FD64_member']]
    assert len(extra) == 10 and all(x['name'].endswith('_collocation_observer_warm.py') for x in extra)
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
    assert len(audit['domain']['files']) == audit['domain']['file_count'] == 224
    assert sum(len(x['arrays']) for x in audit['domain']['files']) == audit['domain']['array_count'] == 1454
    assert len(audit['domain']['complete_group_byte_combinations']) == 76
    assert len(audit['condensed']['files']) == audit['condensed']['file_count'] == 108
    assert len(audit['condensed']['complete_array_byte_combinations']) == audit['condensed']['unique_complete_arrays'] == 38
    assert audit['condensed']['reference_count'] == 42
    assert len(audit['root_raw']['files']) == audit['root_raw']['file_count'] == 14
    assert sum(x['bytes'] for x in audit['root_raw']['files']) == audit['root_raw']['bytes'] == 454456080
    assert audit['root_raw']['full_factor_file_byte_audit'] is False
    assert audit['root_raw']['original_complete_chain_factor_RAM_only'] is True
    obs = audit['observers']
    assert len(obs['collocation']) == 13 and len(obs['midpoint_descriptors']) == 8
    assert sorted(obs['midpoint_payloads_present']) == sorted(obs['midpoint_payloads_matched'])
    assert sorted(str(Path(x['file']).relative_to(WARM)) for x in obs['midpoint_descriptors']) == sorted(obs['midpoint_payloads_matched'])
    assert obs['every_midpoint_file_has_original_descriptor']
    assert obs['no_extra_evaluate_or_RHS_or_J_calls']
    assert audit['domain']['no_matrix_action_performed'] and audit['condensed']['no_model_action_performed']
    assert audit['root_raw']['no_scientific_computation_performed']
    assert audit['no_scientific_module_imported']

    # Individual links for the former 17 primary checks. The paired raw files
    # repeat those checks locally; reader receipts extend the same identities.
    anchors = {
        'original_parent_warm_sha256':'summary.parent_warm + requested_parent_warm_sha256; original transport parent84/warm-001.json.gz',
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
        'readback_accepted_original_trial':'summary.accepted_trial + all five original trials; no new trial executed',
        'published_original_fetch_manifest_matches_actual_files':'original published fetch manifest rechecked; four overlapping copied reports byte-equal; complete transport metadata binds originals',
    }
    crosswalk = [dict(primary_check=k, primary_recorded_value=p['parent_and_report_checks'][k],
        local_repeat_from_original_bytes=checks[k], completed_reader_evidence=anchors[k])
        for k in sorted(checks)]
    local_files = [receipt(path,ROOT) for path in sorted(ROOT.rglob('*')) if path.is_file()]
    assert all(not path.is_symlink() for path in ROOT.rglob('*'))
    scope = dict(schema='actual86-complete-reader-literal-scope-v1',
        reader_tuple=READER_PIN, original_tuple=ORIGINAL_PIN,
        original_source_commit=summary['original_source_commit'],
        original_request_identity=request,
        source_files=source_map,
        original_completed_reader_summary=summary,
        original_domain_capture_scalars={k:v for k,v in audit['domain']['capture'].items()
            if not isinstance(v,(dict,list))},
        original_domain_group_receipts=audit['domain']['complete_group_byte_combinations'],
        original_condensed_complete_array_receipts=audit['condensed']['complete_array_byte_combinations'],
        original_root_raw_receipts=audit['root_raw']['files'],
        original_observer_run_summary=obs['original_collocation_run_summary'],
        original_midpoint_receipts=obs['midpoint_descriptors'],
        original_transport_scope={k:v for k,v in ext.items() if k not in ('files','directories')},
        no_scientific_computation=True,
        absent_large_payloads_locally_rehashed=False,
        original_R276_requested=False,
        values_are_original_report_fields_not_new_scientific_diagnostics=True)
    scope_receipt = emit('2026-11-15-actual86-complete-reader-literal-scope.json',scope)
    output = dict(schema='actual86-complete-reader-primary17-source64-crosswalk-v1',
        reader_tuple=READER_PIN, original_tuple=ORIGINAL_PIN,
        earlier_primary_files=prior,
        no_scientific_computation=True, no_scientific_module_imported=True,
        no_download_performed=True, raw_scientific_ZIP_not_present_or_reprocessed_locally=True,
        byte_checks_completed=True, primary_relationship_count=17,
        primary_relationship_crosswalk=crosswalk,
        original_report_copies=copied,
        comparison_new_copy_matches_prior_QP_summary_except_declared_query_compaction=True,
        previous_source_count=64, completed_Actions_source_count=74,
        source_crosswalk=sources, ten_additional_sources=extra,
        current_wrapper_also_equals_primary_extra_wrapper=True,
        completed_status_duplicate_is_byte_identical=True,
        original_display_projections_match_full_original_JSON=True,
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
        no_extra_R276_invocation=True,
        scientific_arithmetic_performed_in_this_readback=False,
        original_accepted_step_and_scientific_unaccepted_flags_preserved=True,
        literal_scope=scope_receipt)
    audit_receipt = emit('2026-11-15-actual86-complete-reader-crosswalk-and-byte-audit.json',output)
    print(json.dumps(dict(completed=True, scope=scope_receipt, audit=audit_receipt,
        primary_checks=17, old_sources=64, full_reader_sources=74,
        local_small_artifact_files=len(local_files),
        metadata_only_raw_descriptor_crosslinks=len(linked)),indent=2))


if __name__ == '__main__':
    main()
