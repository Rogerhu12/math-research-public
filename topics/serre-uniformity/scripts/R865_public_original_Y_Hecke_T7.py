#!/usr/bin/env python3
"""Standard-library transport for original Y Hecke T7; no core imports."""
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
REQUEST = TOPIC / 'notes/R865-original-Y-Hecke-T7-public-request.json'
REPOSITORY = 'Rogerhu12/math-research-public'
RESULT = 'R865-original-Y-Hecke-T7-and-spectral-projectors'
FINAL = 'p41-original-Y-Hecke-T7-certificate.json'
PREFIX = 'R865-'
CORE = 'R865_original_Y_Hecke_T7.py'
MANIFEST = 'full-outputs-manifest.json'
REFERENCE = 'full-outputs-manifest-reference.json'
BUNDLE = 'R865-retained-original-inputs.tar.gz'
INVENTORY = 'R865-original-source-inventory.json'
INPUT_RECEIPT = 'R865-retained-inputs-receipt.json'
META = ('public-actions-input.json', 'run-receipt.json', 'core-receipt.json')
BASE = ('result', 'run_id', 'source_commit', 'core_sha256', 'manifest_sha256')
LABELS = ('R786', 'R864', 'R866')
PROOF_KEYS = ('R865', 'R866', 'R864', 'R778', 'R802')
RANGE_FILE = 'R824_public_original_global_polar_generators.py'
RANGE_SHA = 'c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c'
SOURCE_COUNTS = {'R786':152, 'R864':9, 'R866':14}
IO = None
STRATEGY = {'scope': 'genuine_original_Y_T7_and_exact_single_operator_spectrum',
 'original_p': 41,
 'level': 82,
 'holomorphic_dimension': 127,
 'G': 'original_C3_times_nonsplit_Cartan_normalizer_mod41',
 'Gamma': 'inverse_image_of_original_G_intersection_SL2_mod82',
 'g7': [[1, -2], [2, 3]],
 'gamma0': [[1, -12], [2, -23]],
 'gamma_infinity': [[47, -2], [-70, 3]],
 'finite_representatives': 'gamma0 * [[1,82*b],[0,7]], b=0..6',
 'infinite_representative': 'gamma_infinity * diag(7,1)',
 'slash_normalization': 'det(A)*(c*tau+d)^(-2)',
 'first_galois_mod82': 47,
 'first_galois_mod41': 6,
 'second_galois_mod82': 7,
 'second_galois_mod41': 7,
 'coefficient_field': 'Q(xi41), with K=Q(s),s^2=-3 fixed by sigma_d',
 'original_twist': 'minus3; cY F(qY)=c0(F)(-qY); c0 fixes xi41',
 'qY': 'exp(2*pi*i*tau/82)',
 'xi82': '-xi41^21',
 'original_section_integer_scale': '6724',
 'new_scale_relative_to_original_e_i_coefficients': [1, 1],
 'differential_from_F': '82*F*dqY/qY',
 'target_qY_orders_inclusive': [0, 13],
 'maximum_original_qY_order_consumed': 91,
 'original_prefix_qY_bound': 128,
 'original_row_convention': '40*n+r',
 'full_coordinate_rows': 560,
 'source_H_J_inverse_reused_without_recomputation': True,
 'source_H_orders_0_to13_reused_without_new_basis_products': True,
 'coordinate_column_block_size': 8,
 'matrix_convention': 'T7(F_j)=sum_i F_i*M[i,j]',
 'Q_basis_matrix': 'K_J*U; unequal_selected_parity_entries_exactly_zero',
 'characteristic_polynomial': 'product_of_actual_even_and_odd_Q_basis_block_charpolys',
 'spectral_projectors': 'CRT_polynomials_in_true_T7; no_expanded_projector_matrices',
 'full_Hecke_isotypic_or_eta_support_claimed': False,
 'budget_resume_and_transport_excluded_from_mathematical_identity': True}


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
    entry = importlib.util.spec_from_file_location('R865_frozen_Range_IO', path)
    IO = importlib.util.module_from_spec(entry)
    entry.loader.exec_module(IO)


def expected_tag(item):
    return {'result':RESULT, 'source_sha256':item['core_sha256'], 'python_flint':'0.9.0', 'p':41,
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
    assert item['input_carrier']['source_label'] == 'R866'
    assert item['input_carrier']['original_member_count'] == 178
    assert item['input_carrier']['selected_original_groups'] == ['R786', 'R864']
    load_io()


def selected_names(label, source, directory):
    cert = read(bound(directory, source['certificate']))
    names = {MANIFEST, *META, source['certificate']['file']}
    if label == 'R786':
        names.add(cert['stages_manifest']['file'])
        names.update('R786-exact-power-1-row-%04d.json.gz' % i for i in range(146))
    elif label == 'R864':
        names.update(cert[key]['file'] for key in
                     ('source_audit', 'kernel_certificate', 'holomorphic_differential_basis', 'stage_manifest'))
    else:
        assert label == 'R866'
        names.update(cert[key]['file'] for key in ('source_audit', 'holomorphic_Fourier_matrix',
                     'selected_exact_inverse', 'semilinear_action', 'Q_fixed_holomorphic_basis', 'stage_manifest'))
        inverse = read(directory / cert['selected_exact_inverse']['file'])
        names.add(inverse['source_row_selection']['file'])
        names.update(('R866-original-source-inventory.json', 'R866-retained-inputs-receipt.json'))
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
    stage_ref = cert['stages_manifest'] if label == 'R786' else cert['stage_manifest']
    stage_index = read(bound(directory, stage_ref))
    assert stage_index['complete'] is True and stage_index['configuration'] == tag
    stages = {row['file']:plain(row) for row in stage_index['files']}
    assert len(stages) == len(stage_index['files'])
    for name in files:
        if not name.endswith('.json.gz'):
            continue
        data = read(directory/name)
        assert data['complete'] is True and data['configuration'] == tag
        if name != stage_ref['file']:
            assert stages[name] == files[name]
        if label != 'R786':
            assert data['result'] == source['result']
    if label == 'R786':
        assert cert['exact_K_basis_prefix_bound_qY'] == 128
        assert cert['all_original_R775_mod739_short_series_compared'] is True
        for i in range(146):
            data = read(directory / ('R786-exact-power-1-row-%04d.json.gz' % i))
            assert data['weight'] == 2 and data['integer_scale'] == '6724' and data['bound_qY'] == 128
            assert data['recipe']['kind'] == 'det_semilinear_E1_pair_trace'
            assert data['recipe']['exact_global_field'] == 'K'
            assert data['original_R775_finite_coefficients_verified'] is True
            assert len(data['integer_qY_xi_coefficients']) == 129
            assert all(len(row) == 40 for row in data['integer_qY_xi_coefficients'])
    elif label == 'R864':
        assert cert['complete_original_K_holomorphic_basis_certified'] is True
        assert cert['actual_cusp_evaluation_rank'] == 19 and cert['actual_kernel_dimension'] == 127
        basis = read(directory/cert['holomorphic_differential_basis']['file'])
        assert basis['actual_dimension_over_K'] == 127 and len(basis['basis']) == 127
        assert all(len(row['original_V1_coefficients']) == 146 for row in basis['basis'])
    else:
        assert cert['complete_original_Q_holomorphic_basis_certified'] is True
        assert cert['actual_original_c_Y_semilinear_action_certified'] is True
        assert cert['actual_holomorphic_dimension'] == 127 and cert['full_original_Fourier_coordinate_rows'] == 560
        H = read(directory/cert['holomorphic_Fourier_matrix']['file'])
        inverse = read(directory/cert['selected_exact_inverse']['file'])
        assert H['matrix_shape'] == [560,127] and H['matrix_integer_scale'] == '6724'
        assert H['new_scale_relative_to_original_e_i_coefficients'] == [1,1]
        assert H['differential_coefficients_equal_matrix_times_82'] is True
        assert inverse['source_H'] == cert['holomorphic_Fourier_matrix']
        assert inverse['both_exact_inverse_products_verified'] is True
        assert inverse['actual_exact_minor_determinant'][0] != '0'
        assert len(inverse['selected_rows']) == len(set(inverse['selected_rows'])) == 127
        assert all(40 <= r < 560 for r in inverse['selected_rows'])
    return cert


def cross_sources(item, retained):
    certs = {label:source_review(label,item['sources'][label],retained/label) for label in LABELS}
    c866 = certs['R866']
    for label in ('R786','R864'):
        assert c866['configuration']['sources'][label] == source_identity(item['sources'][label])
    H = read(retained/'R866'/c866['holomorphic_Fourier_matrix']['file'])
    assert H['source_original_holomorphic_basis'] == certs['R864']['holomorphic_differential_basis']
    assert H['source_original_prefixes'] == [item['sources']['R786']['files'][
        'R786-exact-power-1-row-%04d.json.gz'%i] for i in range(146)]
    assert H['source_audit'] == c866['source_audit']
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
    source=item['sources']['R866'];route=item['input_carrier']
    directory=retained/'R866';directory.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(source,out.parent/'download-R866-for-R865',whole=False)
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
        source_review('R866',source,directory)
        inventory=read(bound(directory,route['source_inventory']))
        receipt=read(bound(directory,route['input_receipt']))
        assert inventory['complete'] is receipt['complete'] is True
        assert inventory['result']==receipt['result']==source['result']
        assert plain(receipt['source_inventory'])==plain(route['source_inventory'])
        assert plain(receipt['source_bundle'])==plain(route['input_bundle'])
        assert receipt['minimal_bundle_member_count']==route['original_member_count']==178
        for label in ('R786','R864'):
            assert source_identity(inventory['sources'][label])==source_identity(item['sources'][label])
        bundle=out.parent/'original-R866-carrier'/route['input_bundle']['file']
        row=plain(route['input_bundle']);assert entries[row['file']]==row
        archive.extract_bound(row['file'],row['sha256'],bundle,row['bytes'])
        count,kept=unpack(bundle,inventory,retained,('R786','R864'))
        assert count==178 and kept==161
        cross_sources(item,retained)
        return {'original_R866_carrier':row,'original_carrier_members_hashed':178,
                'selected_unchanged_original_members':161,'range_transport':archive.receipt()}
    finally:
        archive.close()


def prepare_sources(item,out,allow_download=True):
    out=Path(out);retained=out.parent/'retained-original-R865'
    retained.mkdir(parents=True,exist_ok=True)
    if all((out/name).exists() for name in (INPUT_RECEIPT,INVENTORY,BUNDLE)):
        receipt,inventory=read(out/INPUT_RECEIPT),read(out/INVENTORY)
        assert receipt['result']==inventory['result']==RESULT and receipt['complete'] is inventory['complete'] is True
        assert inventory['sources']==item['sources']
        bound(out,receipt['source_inventory']);bound(out,receipt['source_bundle'])
        count,kept=unpack(out/BUNDLE,inventory,retained)
        assert count==kept==receipt['minimal_bundle_member_count']==175
        cross_sources(item,retained)
        return retained,receipt
    assert allow_download,'Missing completed input carrier; no source regeneration during verify.'
    transfer=download_sources(item,out,retained)
    save(out/INVENTORY,{'result':RESULT,'complete':True,'sources':item['sources'],
                        'all_selected_original_bytes_preserved':True})
    pack(retained,item['sources'],out/BUNDLE)
    receipt={'result':RESULT,'complete':True,'source_inventory':spec(out/INVENTORY),
             'source_bundle':spec(out/BUNDLE),'minimal_bundle_member_count':175,
             'source_mathematical_identities':{label:source_identity(item['sources'][label]) for label in LABELS},
             'source_transfer':transfer,'new_mathematics_executed_in_wrapper':False}
    save(out/INPUT_RECEIPT,receipt)
    print('R865_INPUT_REVIEW='+json.dumps(receipt,sort_keys=True),flush=True)
    return retained,receipt


def stable_job(item):
    answer={k:v for k,v in item.items() if k not in
            ('resume','budget_minutes','readme_sha256','rules_last_read_commit','session','sources','input_carrier')}
    answer['source_identities']={label:source_identity(item['sources'][label]) for label in LABELS}
    return answer


def restore(item,out):
    resume=item.get('resume')
    if resume is None:return
    assert resume['result']==RESULT and resume['core_sha256']==item['core_sha256']
    folder=out.parent/'R865-resume-metadata';folder.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(resume,out.parent/'R865-resume-download',whole=False)
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
    for key in ('genuine_original_Y_T7_matrix_certified','actual_original_Q_fixed_basis_matrix_certified',
                'full560_times127_original_Hecke_equations_verified','exact_single_operator_spectral_projectors_certified'):
        assert final[key] is True
    for key in ('old_Fourier_prefix_kernel_or_inverse_recomputed','new_Eisenstein_q_coefficients_or_original_q_tail_generated',
                'full_Hecke_isotypic_decomposition_computed','Y_active_eta_projector_computed',
                'original_torsion_clearing_N_computed','principal_Hecke_calibration_function_computed',
                'non_p_height_support_or_values_computed','period_or_height_computed','height_nonzero_proved'):
        assert final[key] is False
    inventory=stage(out,final['stage_manifest'],tag)
    indexed={row['file']:plain(row) for row in inventory['files']}
    assert len(indexed)==len(inventory['files'])==inventory['actual_complete_stage_count']
    for row in indexed.values():stage(out,row,tag)
    for key in ('source_audit','double_coset','target_index','matrix_in_original_K_basis',
                'matrix_in_original_Q_fixed_basis','characteristic_polynomial_and_factorization','spectral_projectors'):
        assert indexed[final[key]['file']]==plain(final[key])
    audit=stage(out,final['source_audit'],tag)
    assert audit['source_identities']==tag['sources'] and audit['new_rescaling_relative_to_original_e_i']==[1,1]
    assert audit['old_cusp_kernel_prefix_products_row_selection_or_inverse_recomputed'] is False
    double=stage(out,final['double_coset'],tag)
    assert len(double['alpha_infinity_then_b0_to6'])==8
    assert double['all_determinants_and_same_original_mod82_coset_verified'] is True
    assert (double['first_direction_mod82'],double['first_direction_mod41'],double['second_direction_mod41'])==(47,6,7)
    targets=stage(out,final['target_index'],tag)
    assert len(targets['order_blocks'])==13 and targets['maximum_original_order']==91
    for n,row in enumerate(targets['order_blocks'],1):
        value=stage(out,row,tag);assert value['qY_order']==n and value['matrix_shape']==[40,127]
        assert len(value['matrix'])==40 and all(len(r)==127 for r in value['matrix'])
    K=stage(out,final['matrix_in_original_K_basis'],tag)
    Q=stage(out,final['matrix_in_original_Q_fixed_basis'],tag)
    assert K['matrix_shape']==Q['matrix_shape']==[127,127]
    assert K['all560_times127_original_coordinates_verified'] is True
    assert Q['actual_original_Q_basis_matrix_certified'] is True
    assert len(K['matrix'])==len(Q['matrix_over_Q'])==127
    assert all(len(r)==127 for r in K['matrix']) and all(len(r)==127 for r in Q['matrix_over_Q'])
    for row in K['column_blocks']:
        value=stage(out,row,tag)
        assert value['full560_original_coordinate_rows_verified'] is True and value['new_inverse_computed'] is False
    for row in Q['column_blocks']:
        value=stage(out,row,tag)
        assert value['M_times_Ublock_equals_U_times_Nblock_verified'] is True
        assert value['all_unequal_parity_entries_exactly_zero'] is True
    spectrum=stage(out,final['characteristic_polynomial_and_factorization'],tag)
    assert len(spectrum['characteristic_polynomial_ascending'])==128
    assert spectrum['characteristic_polynomial_ascending'][-1]=='1'
    assert spectrum['all_factor_products_exactly_verified'] is True
    assert spectrum['minimal_polynomial_squarefree_from_original_Rosati_selfadjointness'] is True
    projectors=stage(out,final['spectral_projectors'],tag)
    assert len(projectors['projectors'])==len(spectrum['irreducible_factors'])
    assert projectors['sum_is_identity_mod_true_minimal_polynomial_verified'] is True
    assert projectors['dimensions_sum_to_127_verified'] is True
    for row in projectors['projectors']:
        value=stage(out,row,tag)
        assert value['exact_Bezout_idempotence_and_all_factor_residues_verified'] is True
        assert value['expanded_projector_matrix_or_fiber_product_computed'] is False
        assert value['Y_active_eta_projector_claimed'] is False
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
        config=out.parent/'R865-expanded-job.json';save(config,expanded)
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
            spectrum=read(out/final['characteristic_polynomial_and_factorization']['file'])
            matrix=read(out/final['matrix_in_original_Q_fixed_basis']['file'])
            summary.update(certificate=spec(out/FINAL),stage_manifest=final['stage_manifest'],
                seconds=final['seconds'],actual_even_dimension=matrix['actual_even_dimension'],
                actual_odd_dimension=matrix['actual_odd_dimension'],
                irreducible_factors=spectrum['irreducible_factors'],Y_active_eta_projector_computed=False)
        print('R865_RUN_RECEIPT='+json.dumps(summary,sort_keys=True),flush=True)
    return code


def verify(item,out,request):
    data=read(out/MANIFEST);assert data['result']==RESULT
    rows={row['file']:plain(row) for row in data['files']};assert len(rows)==len(data['files'])
    for row in rows.values():bound(out,row)
    assert plain(read(out/REFERENCE))==spec(out/MANIFEST)
    run=read(out/'run-receipt.json');assert run['result']==RESULT
    if 'public-actions-input.json' not in rows:
        assert run['complete'] is False and run['core_receipt_sha256'] is None
        print('R865_VERIFY=source_preparation_incomplete',flush=True);return 0
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
        print('R865_VERIFY=honest_partial_atomic_stages_preserved',flush=True);return 0
    final=review_math(item,out)
    assert core is not None and core['complete'] is True and core['error'] is None
    assert core['process_exit_code']==run['process_exit_code']==0
    assert core['certificate_sha256']==run['certificate_sha256']==sha(out/FINAL)
    print('R865_COMPLETE_IO_REVIEW='+json.dumps({'complete':True,'manifest_members':len(rows),
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

