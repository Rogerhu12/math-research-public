#!/usr/bin/env python3
"""Standard-library source transport for original Y torsion and Picard inputs.

Only source bytes and certificate schemas are inspected here.  The public
Actions core performs the new integer arithmetic; this module never imports it.
"""
import argparse
import datetime as dt
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import signal
import subprocess
import sys
import tarfile
import traceback

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO / 'topics/serre-uniformity'
REQUEST = TOPIC / 'notes/R870-original-Y-torsion-Hecke-inputs-public-request.json'
REPOSITORY = 'Rogerhu12/math-research-public'
RESULT = 'R870-original-Y-rational-torsion-and-Hecke-support-inputs'
FINAL = 'p41-original-Y-rational-torsion-and-Hecke-support-inputs-certificate.json'
PREFIX = 'R870-'
CORE = 'R870_original_Y_torsion_Hecke_inputs.py'
MANIFEST = 'full-outputs-manifest.json'
REFERENCE = 'full-outputs-manifest-reference.json'
BUNDLE = 'R870-retained-original-inputs.tar.gz'
INVENTORY = 'R870-original-source-inventory.json'
INPUT_RECEIPT = 'R870-retained-inputs-receipt.json'
META = ('public-actions-input.json', 'run-receipt.json', 'core-receipt.json')
BASE = ('result', 'run_id', 'source_commit', 'core_sha256', 'manifest_sha256')
LABELS = ('R865', 'GLOBAL', 'FIBRES')
PROOF_KEYS = ('R870', 'R865', 'RF', 'YP')
RANGE_FILE = 'R824_public_original_global_polar_generators.py'
RANGE_SHA = 'c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c'
SOURCE_COUNTS = {'R865': 26, 'GLOBAL': 8, 'FIBRES': 8}
IO = None
STRATEGY = {
    'scope': 'exact_integer_torsion_bounds_and_source_bound_Picard_test_inputs',
    'original_curve': 'Y=W41; original minus3 twist of the level82 G curve',
    'p': 41, 'good_prime': 7, 'holomorphic_dimension': 127,
    'original_Hecke_operator': 'R865 genuine cyclic7-isogeny pull-push; scalar diamond7 is identity',
    'local_twist_character': 1,
    'point_field': 'Q, for the complete original norm divisors and frames',
    'torsion_test': '(T7-8)R=0 iff R is torsion in JY(Q)',
    'torsion_annihilator': 'm7(8), with m7 the actual source squarefree minimal polynomial',
    'finite_field_order': 'chi7(8)=#JY(F7)',
    'factor_annihilator': 'fi(8) on rational torsion in image of Pi(T7)',
    'integer_projector_multiple': 'retain each original di and Pi=di Ei',
    'uniform_correspondence_denominator': 'lcm of completed original di, not claimed minimal',
    'Picard_test_polynomial': '(X-8)Pi, unreduced in Z[X] to retain an actual correspondence recipe',
    'ideal_sign': 'I_Z=O(-Z), xi=-[I_Z], eta=xi/qj',
    'principal_calibration_direction': 'A/B=h O; rigidified A-to-B is c0/h; fibre scalar c0/c1',
    'all_full_Hecke_blocks_separated_only_if_all_source_multiplicities_one': True,
    'old_T7_matrix_charpoly_factorization_CRT_or_polar_ideal_recomputed': False,
    'large_opaque_producer_carriers_consumed': False,
    'budget_and_transport_excluded_from_mathematical_identity': True,
}


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(4*1024*1024), b''):
            h.update(block)
    return h.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == '.gz' else open)(path, 'rt', encoding='utf-8') as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + '.tmp')
    temporary.write_text(json.dumps(value, sort_keys=True, separators=(',', ':'))+'\n', encoding='utf-8')
    temporary.replace(path)


def plain(row):
    row = {k: row[k] for k in ('file', 'bytes', 'sha256')}
    name = PurePosixPath(row['file'])
    assert len(name.parts) == 1 and name.name not in ('', '.', '..') and '\\' not in row['file']
    assert isinstance(row['bytes'], int) and row['bytes'] >= 0
    assert len(row['sha256']) == 64 and all(c in '0123456789abcdef' for c in row['sha256'])
    return row


def spec(path):
    path = Path(path)
    return {'file':path.name, 'bytes':path.stat().st_size, 'sha256':sha(path)}


def bound(directory, row):
    row = plain(row)
    path = Path(directory) / row['file']
    assert spec(path) == row
    return path


def identity(source):
    return {key:source[key] for key in BASE}


def source_identity(source):
    return {**identity(source), 'certificate':plain(source['certificate']),
            'configuration_sha256':source['configuration_sha256'],
            'selected_files_sha256':fingerprint(source['files']),
            'selected_file_count':len(source['files'])}


def topic_path(name):
    name = PurePosixPath(name)
    assert not name.is_absolute() and '..' not in name.parts
    result = (TOPIC / str(name)).resolve()
    assert result.is_relative_to(TOPIC.resolve())
    return result


def load_io(directory=None):
    global IO
    path = (S if directory is None else Path(directory)) / RANGE_FILE
    assert sha(path) == RANGE_SHA
    entry = importlib.util.spec_from_file_location('R870_frozen_Range_IO', path)
    IO = importlib.util.module_from_spec(entry)
    entry.loader.exec_module(IO)


def expected_tag(item):
    return {'result':RESULT, 'source_sha256':item['core_sha256'],
            'arithmetic':'Python_stdlib_exact_integer_and_Fraction_polynomials', 'p':41,
            'proofs_sha256':{key:item['proofs'][key]['sha256'] for key in PROOF_KEYS},
            'method_sha256':item['method_sha256'],
            'sources':{label:source_identity(item['sources'][label]) for label in LABELS},
            'strategy':STRATEGY}


def guard(item, request):
    assert os.environ.get('GITHUB_ACTIONS') == 'true' and os.environ.get('GITHUB_REPOSITORY') == REPOSITORY
    assert request.resolve() == REQUEST.resolve()
    assert item['result'] == RESULT and item['p'] == 41 and item['producer_inputs_pending'] is False
    assert item['core'] == CORE and sha(S / CORE) == item['core_sha256']
    assert item['wrapper'] == Path(__file__).name and sha(__file__) == item['wrapper_sha256']
    assert 0 < item['budget_minutes'] <= 300
    assert item['io_helper'] == RANGE_FILE and item['io_helper_sha256'] == RANGE_SHA
    assert set(item['proofs']) == set(PROOF_KEYS)
    for row in item['proofs'].values():
        assert sha(topic_path(row['path'])) == row['sha256']
    assert sha(topic_path(item['method'])) == item['method_sha256']
    assert sha(REPO/'README.md') == item['readme_sha256']['root']
    assert sha(TOPIC/'README.md') == item['readme_sha256']['topic']
    assert set(item['sources']) == set(LABELS)
    for label in LABELS:
        source = item['sources'][label]
        assert source is not None and source['expected_conclusion'] == 'success'
        assert len(source['files']) == source['selected_file_count'] == SOURCE_COUNTS[label]
        assert fingerprint(source['files']) == source['selected_files_sha256']
        assert source['accepted_process_exit_codes'] == [0]
    assert item['large_original_carriers_required'] is False
    load_io()


def selected_names(label, source, directory):
    cert = read(bound(directory, source['certificate']))
    names = {MANIFEST, *META, source['certificate']['file']}
    names.update(cert[key]['file'] for key in ('source_audit', 'stage_manifest'))
    if label == 'R865':
        names.update(cert[key]['file'] for key in ('double_coset',
                     'characteristic_polynomial_and_factorization', 'spectral_projectors'))
        index = read(directory / cert['spectral_projectors']['file'])
        names.update(row['file'] for row in index['projectors'])
    else:
        assert label in ('GLOBAL', 'FIBRES')
        names.add(cert['exact_expression_DAG']['file'])
    assert len(names) == SOURCE_COUNTS[label]
    return names


def source_review(label, source, directory):
    directory = Path(directory)
    files = {name:plain(row) for name,row in source['files'].items()}
    assert len(files) == SOURCE_COUNTS[label] and all(k == v['file'] for k,v in files.items())
    assert fingerprint(files) == source['selected_files_sha256']
    for row in files.values():
        bound(directory, row)
    assert files[MANIFEST]['sha256'] == source['manifest_sha256']
    assert files[MANIFEST]['bytes'] == source['manifest_bytes']
    manifest = read(directory / MANIFEST)
    assert manifest['result'] == source['result']
    indexed = {row['file']:plain(row) for row in manifest['files']}
    assert len(indexed) == len(manifest['files']) == source['manifest_file_count']
    for name,row in files.items():
        if name != MANIFEST:
            assert indexed[name] == row
    assert set(files) == selected_names(label, source, directory)
    public,run,core = (read(directory/name) for name in META)
    assert public['result'] == run['result'] == core['result'] == source['result']
    assert public['source_commit'] == run['source_commit'] == source['source_commit']
    assert str(run['workflow_run_id']) == str(source['run_id'])
    assert public['core_sha256'] == core['source_sha256'] == source['core_sha256']
    driver = public.get('wrapper_sha256', public.get('driver_sha256'))
    assert driver == source['wrapper_sha256']
    assert public['root_readme_sha256'] == source['original_readme_sha256']['root']
    assert public['topic_readme_sha256'] == source['original_readme_sha256']['topic']
    assert run['complete'] is True and run['process_exit_code'] == 0
    assert run['error'] is None and core['complete'] is True
    assert run['core_receipt_sha256'] == files['core-receipt.json']['sha256']
    assert core['certificate_sha256'] == source['certificate']['sha256']
    cert = read(bound(directory, source['certificate']))
    assert cert['complete'] is True and cert['result'] == source['result']
    tag = cert['configuration']
    assert tag['result'] == source['result'] and tag['source_sha256'] == source['core_sha256']
    assert fingerprint(tag) == source['configuration_sha256']
    stage_ref = cert['stage_manifest']
    stage_index = read(bound(directory, stage_ref))
    assert stage_index['complete'] is True and stage_index['configuration'] == tag
    stage_rows = stage_index['stages'] if label == 'FIBRES' else stage_index['files']
    stages = {row['file']:plain(row) for row in stage_rows}
    assert len(stages) == len(stage_rows)
    for name in files:
        if not name.endswith('.json.gz'):
            continue
        data = read(directory/name)
        assert data['complete'] is True and data['configuration'] == tag
        if name != stage_ref['file']:
            assert stages[name] == files[name]
        assert data['result'] == source['result']
    if label == 'R865':
        assert cert['genuine_original_Y_T7_matrix_certified'] is True
        assert cert['actual_original_Q_fixed_basis_matrix_certified'] is True
        assert cert['full560_times127_original_Hecke_equations_verified'] is True
        assert cert['exact_single_operator_spectral_projectors_certified'] is True
        factorization=read(directory/cert['characteristic_polynomial_and_factorization']['file'])
        index=read(directory/cert['spectral_projectors']['file'])
        assert len(factorization['characteristic_polynomial_ascending'])==128
        assert factorization['all_factor_products_exactly_verified'] is True
        assert factorization['minimal_polynomial_squarefree_from_original_Rosati_selfadjointness'] is True
        assert index['source_factorization']==cert['characteristic_polynomial_and_factorization']
        assert index['dimensions_sum_to_127_verified'] is True
        assert index['sum_is_identity_mod_true_minimal_polynomial_verified'] is True
        assert len(index['projectors'])==len(factorization['irreducible_factors'])
        for i,row in enumerate(index['projectors']):
            data=read(directory/row['file'])
            assert data['factor_index']==i and data['factor']==factorization['irreducible_factors'][i]
            assert data['exact_Bezout_idempotence_and_all_factor_residues_verified'] is True
            assert data['expanded_projector_matrix_or_fiber_product_computed'] is False
    elif label == 'GLOBAL':
        assert cert['original_eta_Picard_input_DAGs_defined'] is True
        assert cert['original_eta_classes_proved_zero'] is False
        program=read(directory/cert['exact_expression_DAG']['file'])
        assert len(program['five_original_polar_and_eta_outputs'])==5
    else:
        assert cert['all_five_original_rigidified_Poincare_fibres_constructed'] is True
        assert cert['original_full_Picard_correction_and_theta_torsion_transport_preserved'] is True
        assert cert['original_height_values_computed'] is False
        program=read(directory/cert['exact_expression_DAG']['file'])
        assert len(program['five_original_fibre_and_section_outputs'])==5
    return cert


def cross_sources(item, retained):
    certs = {label:source_review(label,item['sources'][label],retained/label) for label in LABELS}
    assert certs['R865']['configuration']['proofs_sha256']['R865']==item['proofs']['R865']['sha256']
    assert certs['FIBRES']['configuration']['proof_sha256']==item['proofs']['RF']['sha256']
    parent=certs['FIBRES']['configuration']['source_identities']['GLOBAL']
    for key in BASE:
        assert parent[key]==item['sources']['GLOBAL'][key]
    assert parent['configuration_sha256']==item['sources']['GLOBAL']['configuration_sha256']
    program=read(retained/'FIBRES'/certs['FIBRES']['exact_expression_DAG']['file'])
    assert plain(program['original_global_program'])==certs['GLOBAL']['exact_expression_DAG']
    return certs


def unpack(bundle, inventory, retained, selected_labels=None):
    expected = {label+'/'+name:plain(row) for label,source in inventory['sources'].items()
                for name,row in source['files'].items()}
    labels = set(inventory['sources']) if selected_labels is None else set(selected_labels)
    seen,kept = set(),0
    retained = Path(retained)
    with tarfile.open(bundle,'r|gz') as archive:
        for member in archive:
            name = PurePosixPath(member.name)
            assert member.isfile() and len(name.parts)==2 and not name.is_absolute() and '..' not in name.parts
            assert member.name in expected and member.name not in seen and '\\' not in member.name
            row = expected[member.name]
            assert member.size == row['bytes']
            selected = name.parts[0] in labels
            target = retained/str(name)
            assert target.resolve().is_relative_to(retained.resolve())
            old = selected and target.exists()
            if old:
                bound(target.parent,row)
            temporary = target.with_name(target.name+'.transfer')
            if selected:
                target.parent.mkdir(parents=True,exist_ok=True)
            destination = temporary.open('wb') if selected and not old else None
            stream = archive.extractfile(member)
            assert stream is not None
            digest,total = hashlib.sha256(),0
            try:
                for block in iter(lambda:stream.read(4*1024*1024),b''):
                    total += len(block);digest.update(block)
                    if destination is not None:destination.write(block)
            finally:
                stream.close()
                if destination is not None:destination.close()
            assert total==row['bytes'] and digest.hexdigest()==row['sha256']
            if selected:
                kept+=1
                if not old:temporary.replace(target)
            seen.add(member.name)
    assert seen==set(expected)
    return len(seen),kept


def pack(retained,sources,target):
    target=Path(target);temporary=target.with_name(target.name+'.tmp')
    with temporary.open('wb') as raw:
        with gzip.GzipFile(filename='',mode='wb',fileobj=raw,mtime=0,compresslevel=0) as zipped:
            with tarfile.open(fileobj=zipped,mode='w|') as archive:
                for label,source in sorted(sources.items()):
                    for name,row in sorted(source['files'].items()):
                        path=bound(Path(retained)/label,row)
                        info=archive.gettarinfo(str(path),arcname=label+'/'+name)
                        info.uid=info.gid=info.mtime=0;info.uname=info.gname=''
                        with path.open('rb') as stream:archive.addfile(info,stream)
    temporary.replace(target)


def download_sources(item,out,retained):
    receipts={}
    for label in LABELS:
        source=item['sources'][label]
        directory=retained/label;directory.mkdir(parents=True,exist_ok=True)
        if all((directory/name).exists() for name in source['files']):
            source_review(label,source,directory)
            receipts[label]={'existing_selected_original_bytes_reused':True}
            continue
        archive=IO.Archive(source,out.parent/('download-'+label+'-for-R870'),whole=False)
        try:
            archive.extract_bound(MANIFEST,source['manifest_sha256'],directory/MANIFEST,source['manifest_bytes'])
            manifest=read(directory/MANIFEST)
            entries={row['file']:plain(row) for row in manifest['files']}
            assert len(entries)==len(manifest['files'])==source['manifest_file_count']
            assert set(archive.by_name)==set(entries)|{MANIFEST,REFERENCE}
            selected=[]
            for name,row in source['files'].items():
                if name==MANIFEST:continue
                assert entries[name]==plain(row)
                selected.append((name,row['sha256'],directory/name,row['bytes']))
            archive.extract_many(selected)
            source_review(label,source,directory)
            receipts[label]={'range_transport':archive.receipt(),
                             'selected_unchanged_original_members':len(source['files'])}
        finally:
            archive.close()
    cross_sources(item,retained)
    return {'source_transfers':receipts,'large_original_carriers_downloaded':False,
            'source_ZIP_digest_is_API_identity_not_a_claim_of_full_local_ZIP_hash':True}


def prepare_sources(item,out,allow_download=True):
    out=Path(out);retained=out.parent/'retained-original-R870'
    retained.mkdir(parents=True,exist_ok=True)
    if all((out/name).exists() for name in (INPUT_RECEIPT,INVENTORY,BUNDLE)):
        receipt,inventory=read(out/INPUT_RECEIPT),read(out/INVENTORY)
        assert receipt['result']==inventory['result']==RESULT and receipt['complete'] is inventory['complete'] is True
        assert inventory['sources']==item['sources']
        bound(out,receipt['source_inventory']);bound(out,receipt['source_bundle'])
        count,kept=unpack(out/BUNDLE,inventory,retained)
        assert count==kept==receipt['minimal_bundle_member_count']==42
        cross_sources(item,retained)
        return retained,receipt
    assert allow_download,'Missing completed input carrier; no source regeneration during verify.'
    transfer=download_sources(item,out,retained)
    save(out/INVENTORY,{'result':RESULT,'complete':True,'sources':item['sources'],
                        'all_selected_original_bytes_preserved':True})
    pack(retained,item['sources'],out/BUNDLE)
    receipt={'result':RESULT,'complete':True,'source_inventory':spec(out/INVENTORY),
             'source_bundle':spec(out/BUNDLE),'minimal_bundle_member_count':42,
             'source_mathematical_identities':{label:source_identity(item['sources'][label]) for label in LABELS},
             'source_transfer':transfer,'new_mathematics_executed_in_wrapper':False}
    save(out/INPUT_RECEIPT,receipt)
    print('R870_INPUT_REVIEW='+json.dumps(receipt,sort_keys=True),flush=True)
    return retained,receipt


def stable_job(item):
    answer={k:v for k,v in item.items() if k not in
            ('resume','budget_minutes','readme_sha256','rules_last_read_commit','session','sources')}
    answer['source_identities']={label:source_identity(item['sources'][label]) for label in LABELS}
    return answer


def restore(item,out):
    resume=item.get('resume')
    if resume is None:return
    assert resume['result']==RESULT and resume['core_sha256']==item['core_sha256']
    folder=out.parent/'R870-resume-metadata';folder.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(resume,out.parent/'R870-resume-download',whole=False)
    try:
        archive.extract_bound(MANIFEST,resume['manifest_sha256'],folder/MANIFEST,resume['manifest_bytes'])
        manifest=read(folder/MANIFEST);assert manifest['result']==RESULT
        entries={row['file']:plain(row) for row in manifest['files']}
        assert len(entries)==len(manifest['files'])==resume['manifest_file_count']
        assert set(archive.by_name)==set(entries)|{MANIFEST,REFERENCE}
        for name in (*META,INPUT_RECEIPT,INVENTORY,BUNDLE):
            if name=='core-receipt.json' and name not in entries:continue
            row=entries[name];destination=out/name if name in (INPUT_RECEIPT,INVENTORY,BUNDLE) else folder/name
            archive.extract_bound(name,row['sha256'],destination,row['bytes'])
        public,run=read(folder/META[0]),read(folder/META[1])
        assert public['source_commit']==run['source_commit']==resume['source_commit']
        assert str(run['workflow_run_id'])==str(resume['run_id'])
        assert public['core_sha256']==item['core_sha256'] and public['wrapper_sha256']==item['wrapper_sha256']
        assert stable_job(public['job'])==stable_job(item)
        assert run['process_exit_code'] in resume['accepted_process_exit_codes']
        if 'core-receipt.json' in entries:
            core=read(folder/META[2]);assert core['source_sha256']==item['core_sha256']
            assert run['core_receipt_sha256']==entries[META[2]]['sha256']
        else:assert run['complete'] is False and run['core_receipt_sha256'] is None
        tag=expected_tag(item)
        for name,row in entries.items():
            if name.startswith(PREFIX) and name.endswith('.json.gz'):
                archive.extract_bound(name,row['sha256'],out/name,row['bytes'])
                value=read(out/name)
                assert value['configuration']==tag and value['result']==RESULT
                assert value['complete'] is (name!=PREFIX+'current.json.gz')
        if FINAL in entries:
            row=entries[FINAL];archive.extract_bound(FINAL,row['sha256'],folder/FINAL,row['bytes'])
            final=read(folder/FINAL);assert final['configuration']==tag
            if final['complete']:
                assert run['complete'] is True
                for entry in read(bound(out,final['stage_manifest']))['files']:bound(out,entry)
                shutil.copyfile(folder/FINAL,out/FINAL)
        save(out/'resume-source-receipt.json',{'result':RESULT,'complete':True,
             'source':resume,'restored_original_stage_bytes_unchanged':True,
             'false_FINAL_not_used_to_constrain_new_current':True,'range_transport':archive.receipt()})
    finally:archive.close()


def output_manifest(out):
    files=[spec(path) for path in sorted(out.iterdir()) if path.is_file() and
           path.name not in (MANIFEST,REFERENCE) and not path.name.endswith(('.tmp','.transfer','.partial'))]
    save(out/MANIFEST,{'result':RESULT,'files':files,'temporary_active_checkpoint_retention_days':1,
                      'machine_outputs_in_git_or_release':False})
    save(out/REFERENCE,{'result':RESULT,**spec(out/MANIFEST)})


def stage(out,row,tag):
    value=read(bound(out,row))
    assert value['result']==RESULT and value['configuration']==tag and value['complete'] is True
    return value


def review_math(item,out):
    tag=expected_tag(item);final=read(out/FINAL)
    assert final['complete'] is True and final['result']==RESULT and final['configuration']==tag
    for key in ('rational_torsion_annihilator_certified','T7_minus_8_exact_torsion_test_certified',
                'uniform_spectral_integer_correspondence_denominator_certified'):
        assert final[key] is True
    for key in ('old_matrix_factorization_CRT_ideal_or_fibre_arithmetic_recomputed',
                'actual_eta_active_support_computed','actual_YP_e_eta_selected','actual_YP_specific_d_selected',
                'actual_principal_comparison_functions_computed','actual_non_p_local_heights_computed',
                'actual_original_height_computed','actual_height_nonzero_proved'):
        assert final[key] is False
    inventory=stage(out,final['stage_manifest'],tag)
    indexed={row['file']:plain(row) for row in inventory['files']}
    assert len(indexed)==len(inventory['files'])==inventory['actual_complete_stage_count']
    for row in indexed.values():stage(out,row,tag)
    for key in ('source_audit','universal_rational_torsion_integer',
                'uniform_integer_correspondence_denominator','original_Picard_equation_and_calibration_plan'):
        assert indexed[final[key]['file']]==plain(final[key])
    audit=stage(out,final['source_audit'],tag)
    assert audit['source_identities']==tag['sources']
    assert audit['no_old_matrix_factorization_CRT_norm_or_polar_ideal_recomputed'] is True
    assert audit['large_carrier_materialized_or_claimed_hashed'] is False
    assert len(audit['original_five_integral_Picard_inputs'])==5
    uni=stage(out,final['universal_rational_torsion_integer'],tag)
    assert uni['torsion_annihilator_N0']==final['rational_torsion_annihilator_N0']
    assert uni['finite_field_Jacobian_order']==final['finite_field_Jacobian_order']
    assert uni['identity_all_coefficients_exactly_verified'] is True
    assert uni['kills_all_original_JY_Q_torsion_including_7_primary'] is True
    assert (uni['good_prime'],uni['evaluation_point'])==(7,8)
    den=stage(out,final['uniform_integer_correspondence_denominator'],tag)
    assert den['uniform_denominator_d_star']==final['uniform_spectral_integer_denominator_d_star']
    assert den['every_d_star_Ei_coefficient_integral_verified'] is True
    assert den['denominator_is_lcm_of_actual_completed_source_denominators'] is True
    assert den['denominator_minimality_claimed'] is False
    assert den['actual_YP_e_eta_or_its_specific_d_selected'] is False
    factor_refs=final['factor_torsion_and_Picard_test_certificates']
    assert len(factor_refs)==final['actual_factor_count']==16
    assert len(den['integral_spectral_correspondences'])==16
    for i,row in enumerate(factor_refs):
        assert indexed[row['file']]==plain(row)
        value=stage(out,row,tag)
        assert value['factor_index']==i
        assert value['factor_division_identity_all_coefficients_verified'] is True
        assert value['factor_annihilates_original_integral_projector_image_certified'] is True
        assert value['Picard_test_polynomial_not_reduced_mod_minimal'] is True
        assert value['actual_eta_projection_zero_decisions']==[None]*5
        assert value['actual_norm_RR_or_principal_function_computed'] is False
    plan=stage(out,final['original_Picard_equation_and_calibration_plan'],tag)
    assert plan['original_five_integral_Picard_inputs']==audit['original_five_integral_Picard_inputs']
    assert len(plan['exact_Picard_equation_plans'])==final['actual_Picard_equation_plan_count']==80
    assert plan['actual_all_T7_blocks_isotypically_separated']==final['actual_all_T7_blocks_isotypically_separated']
    assert final['actual_all_T7_blocks_isotypically_separated'] is True
    assert plan['active_factor_indices'] is None
    for entry in plan['exact_Picard_equation_plans']:
        assert entry['actual_complete_RR_dimension'] is None
        assert entry['actual_principal_generator'] is None
    assert plan['rigidified_principal_transport']['A_to_B_zero_rigidification']=='multiply by c0/h'
    assert plan['rigidified_principal_transport']['principal_function_source'] is None
    return final


def compute(item,out,request):
    out.mkdir(parents=True,exist_ok=True)
    code,error,final=1,None,None
    started=dt.datetime.now(dt.timezone.utc).isoformat()
    try:
        restore(item,out)
        retained,receipt=prepare_sources(item,out)
        expanded={'result':RESULT,'p':41,'core_sha256':item['core_sha256'],
                  'proofs_sha256':{key:item['proofs'][key]['sha256'] for key in PROOF_KEYS},
                  'method_sha256':item['method_sha256'],
                  'sources':{label:dict(item['sources'][label],directory=str(retained/label)) for label in LABELS}}
        config=out.parent/'R870-expanded-job.json';save(config,expanded)
        save(out/'public-actions-input.json',{'result':RESULT,'source_repository':REPOSITORY,
             'source_commit':os.environ['GITHUB_SHA'],'job':item,'core_sha256':item['core_sha256'],
             'wrapper_sha256':sha(__file__),'request_sha256':sha(request),'expanded_config_sha256':sha(config),
             'root_readme_sha256':item['readme_sha256']['root'],'topic_readme_sha256':item['readme_sha256']['topic'],
             'source_inventory':receipt['source_inventory'],'actual_configuration':expected_tag(item),
             'new_mathematics_executed_in_wrapper':False})
        command=[sys.executable,str(S/CORE),'--config',str(config),'--output',str(out),
                 '--budget-minutes',str(item['budget_minutes'])]
        with (out/'core.log').open('wb') as log:
            process=subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
            try:code=process.wait(timeout=item['budget_minutes']*60+900)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid,signal.SIGTERM)
                try:process.wait(timeout=20)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid,signal.SIGKILL);process.wait()
                code,error=124,'outer_timeout; complete atomic stages preserved'
        print((out/'core.log').read_text(errors='replace')[-16000:],flush=True)
        if code==0:
            final=review_math(item,out)
            core=read(out/'core-receipt.json')
            assert core['source_sha256']==item['core_sha256'] and core['complete'] is True
            assert core['configuration']==expected_tag(item) and core['certificate_sha256']==sha(out/FINAL)
            assert core['process_exit_code']==0 and core['error'] is None
    except Exception:
        error,code=traceback.format_exc(),1;print(error,flush=True)
    finally:
        save(out/'run-receipt.json',{'result':RESULT,'source_commit':os.environ['GITHUB_SHA'],
             'workflow_run_id':os.environ['GITHUB_RUN_ID'],'workflow_attempt':os.environ.get('GITHUB_RUN_ATTEMPT','1'),
             'started_at_utc':started,'finished_at_utc':dt.datetime.now(dt.timezone.utc).isoformat(),
             'complete':code==0,'process_exit_code':code,'error':error,
             'core_receipt_sha256':sha(out/'core-receipt.json') if (out/'core-receipt.json').exists() else None,
             'certificate_sha256':sha(out/FINAL) if final is not None else None})
        output_manifest(out)
        summary={'result':RESULT,'complete':code==0,'process_exit_code':code,'error':error,'manifest':spec(out/MANIFEST)}
        if final is not None:
            summary.update(certificate=spec(out/FINAL),stage_manifest=final['stage_manifest'],
                seconds=final['seconds'],actual_factor_count=final['actual_factor_count'],
                rational_torsion_annihilator_N0=final['rational_torsion_annihilator_N0'],
                finite_field_Jacobian_order=final['finite_field_Jacobian_order'],
                uniform_spectral_integer_denominator_d_star=final['uniform_spectral_integer_denominator_d_star'],
                actual_all_T7_blocks_isotypically_separated=final['actual_all_T7_blocks_isotypically_separated'],
                actual_Picard_equation_plan_count=final['actual_Picard_equation_plan_count'],
                actual_eta_active_support_computed=False,actual_original_height_computed=False)
        print('R870_RUN_RECEIPT='+json.dumps(summary,sort_keys=True),flush=True)
    return code


def verify(item,out,request):
    data=read(out/MANIFEST);assert data['result']==RESULT
    rows={row['file']:plain(row) for row in data['files']};assert len(rows)==len(data['files'])
    for row in rows.values():bound(out,row)
    assert plain(read(out/REFERENCE))==spec(out/MANIFEST)
    run=read(out/'run-receipt.json');assert run['result']==RESULT
    if 'public-actions-input.json' not in rows:
        assert run['complete'] is False and run['core_receipt_sha256'] is None
        print('R870_VERIFY=source_preparation_incomplete',flush=True);return 0
    public=read(out/'public-actions-input.json')
    assert public['job']==item and public['request_sha256']==sha(request)
    assert public['wrapper_sha256']==item['wrapper_sha256'] and public['core_sha256']==item['core_sha256']
    assert public['source_commit']==run['source_commit']
    retained,receipt=prepare_sources(item,out,False)
    tag=expected_tag(item);assert public['actual_configuration']==tag
    assert public['source_inventory']==receipt['source_inventory']
    core=None
    if 'core-receipt.json' in rows:
        core=read(out/'core-receipt.json');assert core['source_sha256']==item['core_sha256']
        assert run['core_receipt_sha256']==rows['core-receipt.json']['sha256']
        if core['configuration'] is not None:assert core['configuration']==tag
    else:assert run['complete'] is False and run['core_receipt_sha256'] is None
    for name in rows:
        if name.startswith(PREFIX) and name.endswith('.json.gz'):
            value=read(out/name);assert value['result']==RESULT and value['configuration']==tag
            assert value['complete'] is (name!=PREFIX+'current.json.gz')
    if not run['complete']:
        if FINAL in rows:
            final=read(out/FINAL);assert final['configuration']==tag and final['complete'] is False
        print('R870_VERIFY=honest_partial_atomic_stages_preserved',flush=True);return 0
    final=review_math(item,out)
    assert core is not None and core['complete'] is True and core['error'] is None
    assert core['process_exit_code']==run['process_exit_code']==0
    assert core['certificate_sha256']==run['certificate_sha256']==sha(out/FINAL)
    print('R870_COMPLETE_IO_REVIEW='+json.dumps({'complete':True,'manifest_members':len(rows),
         'original_bundle_members':receipt['minimal_bundle_member_count'],'certificate':spec(out/FINAL),
         'all_source_and_output_bytes_verified':True,'mathematical_core_imported_or_executed':False},sort_keys=True),flush=True)
    return 0


def main():
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command',choices=('compute','verify'))
    parser.add_argument('--request',type=Path,default=REQUEST)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();item=read(args.request);guard(item,args.request)
    return compute(item,args.output,args.request) if args.command=='compute' else verify(item,args.output,args.request)


if __name__=='__main__':raise SystemExit(main())

