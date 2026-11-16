#!/usr/bin/env python3
"""Standard-library carrier and source runner for the original rigidified fibres."""
import argparse
import datetime as dt
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import signal
import subprocess
import sys
import tarfile
import traceback

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO/'topics/serre-uniformity'
REQUEST = TOPIC/'notes/R850-original-rigidified-fibres-public-request.json'
RESULT = 'R850-original-rigidified-Poincare-fibres-and-theta-section'
FINAL = 'p41-original-rigidified-Poincare-fibres-certificate.json'
PREFIX = 'R850-rigidified-fibres-'
MANIFEST = 'full-outputs-manifest.json'
REFERENCE = 'full-outputs-manifest-reference.json'
MATH_INVENTORY = PREFIX+'stage-manifest.json.gz'
INVENTORY = PREFIX+'original-source-inventory.json'
BUNDLE = PREFIX+'retained-original-inputs.tar.gz'
INPUT_RECEIPT = PREFIX+'retained-inputs-receipt.json'
HELPER = 'R824_public_original_global_polar_generators.py'
HELPER_SHA = 'c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c'
PARENT_CORE = 'R839_original_global_polar_DAG.py'
PARENT_SHA = '544241acf5f3451df34c779d513ea6494616d4d4caa26cd2531749edc895aea7'
LABELS = ['GLOBAL', 'C0', 'POINTS']
BASE_KEYS = ['result', 'run_id', 'source_commit', 'core_sha256', 'manifest_sha256', 'configuration_sha256']
META = [MANIFEST, REFERENCE, 'run-receipt.json', 'core-receipt.json', 'public-actions-input.json']
GLOBAL_INVENTORY = 'R839-global-polar-original-source-inventory.json'
GLOBAL_RECEIPT = 'R839-global-polar-retained-inputs-receipt.json'
GLOBAL_BUNDLE = 'R839-global-polar-retained-original-inputs.tar.gz'
POINT_RECEIPT = 'retained-inputs-receipt.json'
POINT_BUNDLE = 'R792-log-jet-padic-retained-inputs.tar.gz'
PQ = [(165,67),(93,67),(100,67),(168,67),(371,134)]
SCOPE = {
    'p':41, 'original_map_index':4, 'original_map_degree':1206,
    'original_pq':[list(x) for x in PQ],
    'source_and_target_curve_points':['c0','c1','P0=phi(c0)','P1=phi(c1)'],
    'original_c0_parameter':'t=a^3', 'original_c1_parameter':'z=a-1',
    'original_elliptic_parameter':'xi=-x/y', 'original_elliptic_differential':'dx/(2y)',
    'ideal_convention':'I_Z=O_Y(-Z), embedded in the original function field',
    'real_descent_ideal_identity':'I_ZR=R_j*I_Z^3',
    'Poincare_power_is_in_second_slot_with_first_point_fixed':True,
    'original_theta_square_factor':['1','2'],
    'original_C_h_not_replaced_or_numerically_recovered':True,
    'all_scalar_powers_are_exact_DAGs_without_large_power_expansion':True,
    'all_old_nodes_and_old_configuration_tags_remain_unchanged':True,
    'new_CM_Hensel_Dixon_point_addition_or_global_solve':False,
    'canonical_Poincare_logarithms_or_height_values_computed':False,
    'output_representation':'finite_exact_source_bound_line_bundle_fibre_and_scalar_DAG',
}
TRUE_FLAGS = [
    'all_five_original_rigidified_Poincare_fibres_constructed',
    'all_five_original_c0_normalized_full_sections_constructed',
    'all_five_original_theta_frame_constants_defined',
    'all_five_original_Q_threefold_theta_square_fibres_constructed',
    'original_full_Picard_correction_and_theta_torsion_transport_preserved',
]
FALSE_FLAGS = [
    'canonical_Poincare_logarithms_computed', 'original_height_values_computed',
    'original_height_nonzero_proved', 'eta_standard_Jacobian_coordinates_computed',
    'original_CM_candidate_A1_accepted', 'large_scalar_integer_powers_expanded',
    'old_mathematical_computations_repeated', 'all_p_uniformity_proved',
]
H64 = re.compile(r'[0-9a-f]{64}')
IO = None


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda:stream.read(4*1024*1024),b''):h.update(block)
    return h.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix=='.gz' else open)(path,'rt',encoding='utf-8') as stream:
        return json.load(stream)


def save(path,value):
    path = Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temporary = path.with_name(path.name+'.tmp')
    temporary.write_text(json.dumps(value,sort_keys=True,separators=(',',':'))+'\n',encoding='utf-8')
    temporary.replace(path)


def fingerprint(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def safe_name(name):
    assert isinstance(name,str) and Path(name).name==name and name not in ('.','..') and '\\' not in name
    return name


def plain(row):
    value = {key:row[key] for key in ('file','bytes','sha256')};safe_name(value['file'])
    assert isinstance(value['bytes'],int) and value['bytes']>=0 and H64.fullmatch(value['sha256'])
    return value


def file_spec(path):
    path = Path(path)
    return {'file':path.name,'bytes':path.stat().st_size,'sha256':sha(path)}


def bound(folder,row):
    row = plain(row);path = Path(folder)/row['file']
    assert file_spec(path)==row,('Original bytes changed',row['file'])
    return path


def identity(item):
    return {key:item[key] for key in BASE_KEYS}


def same_origin(a,b):
    for key in BASE_KEYS[:-1]:assert str(a[key])==str(b[key]),('Source mismatch',key)


def topic_path(name):
    path = PurePosixPath(name);assert not path.is_absolute() and '..' not in path.parts
    answer = (TOPIC/str(path)).resolve();assert answer.is_relative_to(TOPIC.resolve())
    return answer


def load_helper(item,helper_dir=None):
    global IO
    path = (S if helper_dir is None else Path(helper_dir))/HELPER
    assert item['io_helper_sha256']==HELPER_SHA and sha(path)==HELPER_SHA
    module = importlib.util.spec_from_file_location('R850_stdlib_Range_transport',path)
    IO = importlib.util.module_from_spec(module);module.loader.exec_module(IO)


def expected_tag(item):
    return {'result':RESULT,'source_sha256':item['core_sha256'],
        'proof_sha256':item['proof_sha256'],'method_sha256':item['method_sha256'],
        'source_identities':{k:{**identity(item['sources'][k]),
            'selected_files_sha256':item['sources'][k]['selected_files_sha256'],
            'selected_file_count':item['sources'][k]['selected_file_count']} for k in LABELS},
        'arithmetic':'symbolic composition of completed exact original fibres; no old arithmetic executed',
        **SCOPE}


def guard(item,path):
    assert os.environ.get('GITHUB_ACTIONS')=='true'
    assert os.environ.get('GITHUB_REPOSITORY')=='Rogerhu12/math-research-public'
    assert path.resolve()==REQUEST.resolve()
    assert item['result']==RESULT and item['p']==41 and item['producer_inputs_pending'] is False
    assert item['core']=='R850_original_rigidified_fibres.py'
    assert item['wrapper']=='R850_public_original_rigidified_fibres.py'
    assert sha(S/item['core'])==item['core_sha256'] and sha(__file__)==item['wrapper_sha256']
    assert item['composition_helper_core']==PARENT_CORE
    assert item['composition_helper_core_sha256']==PARENT_SHA and sha(S/PARENT_CORE)==PARENT_SHA
    assert 0<item['budget_minutes']<=300
    for key in ('proof','method'):assert sha(topic_path(item[key]))==item[key+'_sha256']
    assert sha(REPO/'README.md')==item['readme_sha256']['root']
    assert sha(TOPIC/'README.md')==item['readme_sha256']['topic']
    assert set(item['sources'])==set(LABELS)
    for source in item['sources'].values():
        for key in ('core_sha256','wrapper_sha256','manifest_sha256','configuration_sha256','selected_files_sha256'):
            assert H64.fullmatch(source[key])
        assert source['selected_file_count']>=8 and source['expected_conclusion']=='success'
        assert source['accepted_process_exit_codes']==[0]
        assert source['artifact_id']>0 and source['archive_bytes']>0 and H64.fullmatch(source['archive_sha256'])
        plain(source['reference'])
    load_helper(item)


def source_names(label,source,folder):
    names = set(META+[source['certificate_name']])
    certificate_path = Path(folder)/source['certificate_name']
    if not certificate_path.exists():return sorted(names)
    cert = read(certificate_path)
    names.add(plain(cert['source_audit'])['file'])
    if label=='GLOBAL':
        names.update((GLOBAL_INVENTORY,GLOBAL_RECEIPT,GLOBAL_BUNDLE))
        for key in ('exact_expression_DAG','stage_manifest'):names.add(plain(cert[key])['file'])
    elif label=='C0':
        names.add(plain(cert['stage_manifest'])['file'])
        assert set(cert['norm_and_trace'])==set(map(str,range(6)))
        assert set(cert['comparison_leading_jets'])==set(map(str,range(1,6)))
        for table in ('norm_and_trace','comparison_leading_jets'):
            names.update(plain(row)['file'] for row in cert[table].values())
    else:
        assert label=='POINTS';names.update((POINT_RECEIPT,POINT_BUNDLE))
    return sorted(names)


def manifest_entries(source,folder):
    folder = Path(folder)
    assert file_spec(folder/MANIFEST)=={'file':MANIFEST,'bytes':source['manifest_bytes'],'sha256':source['manifest_sha256']}
    manifest = read(folder/MANIFEST);assert manifest['result']==source['result']
    entries = {row['file']:plain(row) for row in manifest['files']}
    assert len(entries)==len(manifest['files'])==source['manifest_file_count']
    reference = read(bound(folder,source['reference']))
    assert reference['result']==source['result']
    if 'manifest' in reference:
        assert plain(reference['manifest'])==file_spec(folder/MANIFEST)
    else:
        assert reference['manifest_file']==MANIFEST and reference['manifest_sha256']==source['manifest_sha256']
        assert reference['manifest_bytes']==source['manifest_bytes'] and reference['file_count']==len(entries)
    assert MANIFEST not in entries and REFERENCE not in entries
    entries[MANIFEST]=file_spec(folder/MANIFEST);entries[REFERENCE]=plain(source['reference'])
    return entries


def selected_rows(label,source,folder):
    entries = manifest_entries(source,folder)
    selected = {name:entries[name] for name in source_names(label,source,folder)}
    assert len(selected)==source['selected_file_count']
    assert fingerprint([selected[name] for name in sorted(selected)])==source['selected_files_sha256']
    return selected


def review_source(label,source,folder,allow_missing_opaque=False):
    folder = Path(folder);selected = selected_rows(label,source,folder)
    for name,row in selected.items():
        if allow_missing_opaque and label=='GLOBAL' and name==GLOBAL_BUNDLE and not (folder/name).exists():continue
        bound(folder,row)
    run = read(folder/'run-receipt.json');core = read(folder/'core-receipt.json')
    initial = read(folder/'public-actions-input.json');cert = read(folder/source['certificate_name'])
    assert run['result']==core['result']==initial['result']==cert['result']==source['result']
    assert str(run['workflow_run_id'])==str(source['run_id'])
    assert run['source_commit']==initial['source_commit']==source['source_commit']
    assert run['process_exit_code']==0 and run['complete'] is True and core['complete'] is True
    assert run['error'] is None and core.get('error') is None
    assert initial['source_repository']=='Rogerhu12/math-research-public'
    assert initial['core_sha256']==initial['job']['core_sha256']==core['source_sha256']==source['core_sha256']
    driver_key = 'wrapper_sha256' if label=='POINTS' else 'driver_sha256'
    assert initial[driver_key]==initial['job']['wrapper_sha256']==source['wrapper_sha256']
    assert run['core_receipt_sha256']==selected['core-receipt.json']['sha256']
    assert core['certificate_sha256']==selected[source['certificate_name']]['sha256']
    exit_key = 'exit_code' if label=='POINTS' else 'process_exit_code'
    assert core[exit_key]==0 and cert['complete'] is True
    tag = cert['configuration']
    assert tag['result']==source['result'] and tag['source_sha256']==source['core_sha256']
    assert fingerprint(tag)==source['configuration_sha256']
    if 'configuration' in core:assert core['configuration']==tag
    if 'configuration_sha256' in core:assert core['configuration_sha256']==source['configuration_sha256']
    assert initial['root_readme_sha256']==source['original_readme_sha256']['root']
    assert initial['topic_readme_sha256']==source['original_readme_sha256']['topic']
    for name in selected:
        if name.endswith('.json.gz'):
            stage = read(folder/name)
            assert stage['complete'] is True and stage['configuration']==tag
            if 'result' in stage:assert stage['result']==source['result']
    if label=='GLOBAL':
        receipt = read(folder/GLOBAL_RECEIPT);inventory = read(folder/GLOBAL_INVENTORY)
        assert receipt['result']==inventory['result']==source['result']
        assert receipt['complete'] is True and inventory['complete'] is True
        assert plain(receipt['source_bundle'])==selected[GLOBAL_BUNDLE]
        assert plain(receipt['source_inventory'])==selected[GLOBAL_INVENTORY]==plain(initial['source_inventory'])
        assert fingerprint(inventory['sources'])==receipt['expanded_sources_sha256']==initial['job']['expanded_sources_sha256']
        assert receipt['source_requests']==initial['job']['sources']
        assert inventory['all_members_are_unchanged_original_producer_bytes'] is True
        count=0
        for child,group in inventory['sources'].items():
            same_origin(group,receipt['source_requests'][child])
            rows=[plain(group['files'][n]) for n in sorted(group['files'])]
            assert len(rows)==group['selected_file_count'] and fingerprint(rows)==group['selected_files_sha256']
            count+=len(rows)
        assert count==receipt['minimal_bundle_member_count']==2709
        assert cert['global_y_exact_unit_expression_defined'] is True
        assert cert['five_original_addition_pole_ideals_as_fractional_DAGs_certified'] is True
    elif label=='C0':
        assert cert['all_six_true_relative_norms_and_traces_computed'] is True
        assert cert['all_five_original_comparison_leading_constants_DAG_and_unit_jets_computed'] is True
    else:
        receipt = read(folder/POINT_RECEIPT)
        assert receipt['result']==source['result']
        assert receipt['all_source_bytes_and_original_parent_child_bindings_verified'] is True
        assert plain(receipt['input_bundle'])==selected[POINT_BUNDLE]
        assert receipt['expanded_sources']==initial['expanded_sources']
        assert receipt['selected_source_file_count']==270
        assert cert['all_five_logarithmic_jets_proved_nonzero'] is True
        assert cert['original_value_rowspace_zero_A1_proved'] is False
    return {**identity(source),'certificate_name':source['certificate_name'],
        'selected_file_count':len(selected),'selected_files_sha256':source['selected_files_sha256'],'files':selected}


def review_nested_points(point_folder,target):
    """Verify the original 270 members; no source core is imported."""
    point_folder,target = Path(point_folder),Path(target)
    receipt = read(point_folder/POINT_RECEIPT);groups = receipt['expanded_sources']
    assert set(groups)=={'CM','DAG','JETS','NONTORSION','POINTS','R791'}
    bundle = bound(point_folder,receipt['input_bundle'])
    count = unpack_groups(bundle,target,groups)
    assert count==receipt['selected_source_file_count']==270
    for label,source in groups.items():
        folder=target/label;files={name:plain(row) for name,row in source['files'].items()}
        assert len(files)==source['selected_file_count']
        assert fingerprint([files[n] for n in sorted(files)])==source['selected_files_sha256']
        assert files[MANIFEST]['sha256']==source['manifest_sha256']
        manifest=read(folder/MANIFEST);assert manifest['result']==source['result']
        original={row['file']:plain(row) for row in manifest['files']}
        assert len(original)==len(manifest['files'])
        for name,row in files.items():
            bound(folder,row)
            if name not in (MANIFEST,REFERENCE):assert original[name]==row
        cert=read(bound(folder,source['certificate']));tag=cert['configuration']
        assert cert['complete'] is True and cert['result']==source['result']
        assert tag['result']==source['result'] and tag['source_sha256']==source['core_sha256']
        assert fingerprint(tag)==source['configuration_sha256']
        if 'run-receipt.json' in files:
            run=read(folder/'run-receipt.json')
            assert str(run['workflow_run_id'])==str(source['run_id']) and run['source_commit']==source['source_commit']
            assert run['process_exit_code']==0
        if 'public-actions-input.json' in files:
            public=read(folder/'public-actions-input.json')
            assert public['source_commit']==source['source_commit']
            assert public['job']['core_sha256']==source['core_sha256']
            if label!='R791':assert public['core_sha256']==source['core_sha256']
        if 'core-receipt.json' in files:
            core=read(folder/'core-receipt.json');assert core['source_sha256']==source['core_sha256']
        for name in files:
            if name.endswith('.json.gz'):
                value=read(folder/name)
                assert value['complete'] is True and value['configuration']==tag
    return groups


def review_all(item,retained,allow_missing_opaque=False):
    retained=Path(retained)
    reviewed={label:review_source(label,item['sources'][label],retained/label,allow_missing_opaque) for label in LABELS}
    assert sum(x['selected_file_count'] for x in reviewed.values())==item['selected_original_file_count']
    assert fingerprint(reviewed)==item['expanded_sources_sha256']
    nested=review_nested_points(retained/'POINTS',retained.parent/'original-point-leaves')
    global_cert=read(retained/'GLOBAL'/reviewed['GLOBAL']['certificate_name'])
    c0_cert=read(retained/'C0'/reviewed['C0']['certificate_name'])
    same_origin(global_cert['configuration']['source_identities']['R791'],nested['R791'])
    same_origin(c0_cert['configuration']['sources']['R791'],nested['R791'])
    same_origin(global_cert['configuration']['source_identities']['R840'],nested['CM'])
    return reviewed


def fetch_direct(label,source,retained):
    folder=Path(retained)/label;folder.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(source,Path(retained).parent/('download-R850-'+label),whole=False)
    try:
        archive.extract_bound(MANIFEST,source['manifest_sha256'],folder/MANIFEST,source['manifest_bytes'])
        ref=plain(source['reference']);archive.extract_bound(ref['file'],ref['sha256'],folder/ref['file'],ref['bytes'])
        entries=manifest_entries(source,folder)
        assert set(archive.by_name)==set(entries)
        for name,row in entries.items():
            assert len(archive.by_name[name])==1 and archive.by_name[name][0].file_size==row['bytes']
        for _ in range(3):
            names=source_names(label,source,folder)
            need=[]
            for name in names:
                row=entries[name];path=folder/name
                if path.exists():bound(folder,row)
                else:need.append((name,row['sha256'],path,row['bytes']))
            archive.extract_many(need)
            if source_names(label,source,folder)==names:break
        else:raise AssertionError('Original selection did not close')
        review_source(label,source,folder)
        return archive.receipt()
    finally:archive.close()


def pack_sources(retained,sources,target):
    retained,target=Path(retained),Path(target);temporary=target.with_name(target.name+'.tmp')
    with temporary.open('wb') as raw:
        # Already compressed original carriers remain byte-identical opaque members.
        with gzip.GzipFile(fileobj=raw,mode='wb',mtime=0,filename='',compresslevel=0) as compressed:
            with tarfile.open(fileobj=compressed,mode='w|') as tar:
                for label in LABELS:
                    for name,row in sorted(sources[label]['files'].items()):
                        path=bound(retained/label,row);info=tar.gettarinfo(str(path),arcname=label+'/'+name)
                        info.uid=info.gid=info.mtime=0;info.uname=info.gname=''
                        with path.open('rb') as stream:tar.addfile(info,stream)
    temporary.replace(target)


def unpack_groups(bundle,retained,sources):
    retained=Path(retained)
    wanted={(label,name):plain(row) for label,source in sources.items() for name,row in source['files'].items()}
    seen=set()
    with tarfile.open(bundle,'r|gz') as tar:
        for member in tar:
            if member.isdir():continue
            path=PurePosixPath(member.name)
            assert member.isfile() and not path.is_absolute() and '..' not in path.parts and len(path.parts)==2
            key=tuple(path.parts);assert key in wanted and key not in seen;seen.add(key)
            row=wanted[key];assert member.size==row['bytes']
            destination=retained/key[0]/key[1];destination.parent.mkdir(parents=True,exist_ok=True)
            temporary=destination.with_name(destination.name+'.download')
            h=hashlib.sha256();count=0
            with tar.extractfile(member) as stream,temporary.open('wb') as sink:
                for block in iter(lambda:stream.read(4*1024*1024),b''):
                    h.update(block);count+=len(block);sink.write(block)
            assert count==row['bytes'] and h.hexdigest()==row['sha256']
            if destination.exists():bound(destination.parent,row);temporary.unlink()
            else:temporary.replace(destination)
    assert seen==set(wanted)
    return len(seen)


def prepare_sources(item,out,allow_download=True):
    out=Path(out);retained=out.parent/'retained-R850-rigidified-fibres';retained.mkdir(parents=True,exist_ok=True)
    existing=[(out/name).exists() for name in (INPUT_RECEIPT,INVENTORY,BUNDLE)]
    if all(existing):
        receipt,inventory=read(out/INPUT_RECEIPT),read(out/INVENTORY)
        assert receipt['result']==inventory['result']==RESULT
        assert receipt['complete'] is True and inventory['complete'] is True
        assert receipt['source_requests']==item['sources']
        assert receipt['expanded_sources_sha256']==item['expanded_sources_sha256']
        bound(out,receipt['source_inventory']);bound(out,receipt['source_bundle'])
        count=unpack_groups(out/BUNDLE,retained,inventory['sources'])
        reviewed=review_all(item,retained);assert reviewed==inventory['sources']
        assert count==receipt['minimal_bundle_member_count']==item['selected_original_file_count']
        return retained,receipt,reviewed
    assert allow_download,'Continuation lost its complete original source carrier.'
    transport={label:fetch_direct(label,item['sources'][label],retained) for label in LABELS}
    reviewed=review_all(item,retained)
    save(out/INVENTORY,{'result':RESULT,'complete':True,'sources':reviewed,
        'all_members_are_unchanged_original_producer_bytes':True})
    pack_sources(retained,reviewed,out/BUNDLE)
    receipt={'result':RESULT,'complete':True,'source_requests':item['sources'],
        'expanded_sources_sha256':item['expanded_sources_sha256'],
        'source_inventory':file_spec(out/INVENTORY),'source_bundle':file_spec(out/BUNDLE),
        'minimal_bundle_member_count':item['selected_original_file_count'],'range_transport':transport,
        'GLOBAL_opaque_carrier_and_original_2709_member_receipt_preserved':True,
        'POINTS_original_270_members_verified_against_original_manifests':True,
        'old_numeric_arithmetic_recomputed':False}
    save(out/INPUT_RECEIPT,receipt)
    print('R850_SOURCE_IO='+json.dumps({'source_inventory':receipt['source_inventory'],
        'source_bundle':receipt['source_bundle'],'selected_original_files':item['selected_original_file_count'],
        'nested_point_members':270,'opaque_global_original_members':2709,
        'opaque_global_members_expanded_or_recomputed':False,'new_mathematics_executed':False},sort_keys=True),flush=True)
    return retained,receipt,reviewed


def output_manifest(out):
    out=Path(out)
    rows=[dict(file_spec(path),included_in_git=False) for path in sorted(out.iterdir()) if path.is_file()
        and path.name not in (MANIFEST,REFERENCE) and not path.name.endswith(('.tmp','.download','.partial'))]
    save(out/MANIFEST,{'result':RESULT,'files':rows,'temporary_active_checkpoint_retention_days':1,
        'reproducible_data_in_git_or_release':False})
    save(out/REFERENCE,{'result':RESULT,'manifest_file':MANIFEST,'manifest_sha256':sha(out/MANIFEST),
        'manifest_bytes':(out/MANIFEST).stat().st_size,'file_count':len(rows)})


def stable_job(item):
    return {key:value for key,value in item.items() if key not in
        ('resume','budget_minutes','readme_sha256','rules_last_read_commit')}


def check_manifest(out):
    out=Path(out);manifest=read(out/MANIFEST);assert manifest['result']==RESULT
    entries={row['file']:plain(row) for row in manifest['files']}
    assert len(entries)==len(manifest['files'])
    for row in entries.values():bound(out,row)
    reference=read(out/REFERENCE)
    assert reference['manifest_file']==MANIFEST and reference['manifest_sha256']==sha(out/MANIFEST)
    assert reference['manifest_bytes']==(out/MANIFEST).stat().st_size and reference['file_count']==len(entries)
    return entries


def restore(item,out):
    resume=item.get('resume')
    if resume is None:return
    assert resume['result']==RESULT and resume['core_sha256']==item['core_sha256']
    out=Path(out);meta=out.parent/'resume-R850-metadata';meta.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(resume,out.parent/'download-R850-resume',whole=False)
    try:
        archive.extract_bound(MANIFEST,resume['manifest_sha256'],meta/MANIFEST,resume['manifest_bytes'])
        manifest=read(meta/MANIFEST);assert manifest['result']==RESULT
        entries={row['file']:plain(row) for row in manifest['files']}
        assert len(entries)==len(manifest['files'])==resume['manifest_file_count']
        assert set(archive.by_name)==set(entries)|{MANIFEST,REFERENCE}
        names=['run-receipt.json','public-actions-input.json',INPUT_RECEIPT,INVENTORY,BUNDLE]
        if 'core-receipt.json' in entries:names.append('core-receipt.json')
        for name in names:
            row=entries[name];destination=out/name if name in (INPUT_RECEIPT,INVENTORY,BUNDLE) else meta/name
            archive.extract_bound(name,row['sha256'],destination,row['bytes'])
        run,initial=read(meta/'run-receipt.json'),read(meta/'public-actions-input.json')
        assert run['result']==initial['result']==RESULT
        assert run['source_commit']==initial['source_commit']==resume['source_commit']
        assert str(run['workflow_run_id'])==str(resume['run_id'])
        assert initial['core_sha256']==item['core_sha256'] and initial['driver_sha256']==item['wrapper_sha256']
        assert stable_job(initial['job'])==stable_job(item)
        assert run['process_exit_code'] in resume['accepted_process_exit_codes']
        core=None
        if (meta/'core-receipt.json').exists():
            core=read(meta/'core-receipt.json')
            assert core['result']==RESULT and core['source_sha256']==item['core_sha256']
            assert run['core_receipt_sha256']==entries['core-receipt.json']['sha256']
        else:assert run.get('core_receipt_sha256') is None and run['complete'] is False
        prepare_sources(item,out,allow_download=False);tag=expected_tag(item)
        math_names=sorted(name for name in entries if name.startswith(PREFIX) and name.endswith('.json.gz'))
        archive.extract_many([(name,entries[name]['sha256'],out/name,entries[name]['bytes']) for name in math_names])
        for name in math_names:
            value=read(out/name)
            assert value['complete'] is True and value['configuration']==tag and value['result']==RESULT
        restored_final=False
        if FINAL in entries:
            row=entries[FINAL];archive.extract_bound(FINAL,row['sha256'],meta/FINAL,row['bytes'])
            final=read(meta/FINAL);assert final['result']==RESULT and final['configuration']==tag
            if final['complete'] is True:
                assert run['complete'] is True and run['process_exit_code']==0 and core and core['complete'] is True
                assert core['certificate_sha256']==row['sha256']
                assert all(final[key] is True for key in TRUE_FLAGS) and all(final[key] is False for key in FALSE_FLAGS)
                for key in ('source_audit','exact_expression_DAG','stage_manifest'):bound(out,final[key])
                shutil.copyfile(meta/FINAL,out/FINAL);restored_final=True
        save(out/'resume-inheritance-receipt.json',{'result':RESULT,'complete':True,'source_resume':resume,
            'original_manifest':file_spec(meta/MANIFEST),'range_transport':archive.receipt(),
            'all_restored_complete_stages':[entries[name] for name in math_names],
            'restored_successful_final':restored_final,
            'incomplete_final_not_used_to_override_newer_completed_stages':True})
    finally:archive.close()


def compute(item,out,request_path):
    out.mkdir(parents=True,exist_ok=True);process=None;exitcode=1;error=None;outer_timeout=False
    try:
        restore(item,out);retained,receipt,reviewed=prepare_sources(item,out)
        expanded=dict(item)
        expanded['sources']={label:{**reviewed[label],'directory':str((retained/label).resolve())} for label in LABELS}
        for key in ('proof','method'):expanded[key+'_absolute_path']=str(topic_path(item[key]))
        save(out/'public-actions-expanded-job.json',expanded)
        initial={'result':RESULT,'p':41,'source_repository':'Rogerhu12/math-research-public',
            'source_commit':os.environ['GITHUB_SHA'],'job':item,'request_sha256':sha(request_path),
            'driver_sha256':sha(__file__),'core_sha256':item['core_sha256'],
            'proof_sha256':item['proof_sha256'],'method_sha256':item['method_sha256'],
            'composition_helper_core_sha256':PARENT_SHA,'io_helper_sha256':HELPER_SHA,
            'workflow_sha256':sha(REPO/item['workflow']),
            'root_readme_sha256':sha(REPO/'README.md'),'topic_readme_sha256':sha(TOPIC/'README.md'),
            'source_inventory':receipt['source_inventory'],
            'prepared_at_utc':dt.datetime.now(dt.timezone.utc).isoformat(),
            'all_new_expression_assembly_runs_only_in_public_Actions_core':True}
        save(out/'public-actions-input.json',initial)
        command=[sys.executable,str(S/item['core']),'--config',str(out/'public-actions-expanded-job.json'),
            '--out',str(out),'--budget-minutes',str(item['budget_minutes'])]
        with (out/'public-actions-run.log').open('w',encoding='utf-8') as log:
            process=subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
            try:exitcode=process.wait(timeout=item['budget_minutes']*60+900)
            except subprocess.TimeoutExpired:
                outer_timeout=True;os.killpg(process.pid,signal.SIGTERM)
                try:process.wait(timeout=20)
                except subprocess.TimeoutExpired:os.killpg(process.pid,signal.SIGKILL);process.wait()
                exitcode=124
    except BaseException as exc:
        error={'type':type(exc).__name__,'message':str(exc)}
        traceback.print_exc();print(json.dumps({'wrapper_error':error},sort_keys=True),flush=True)
    finally:
        core=read(out/'core-receipt.json') if (out/'core-receipt.json').exists() else None
        final=read(out/FINAL) if (out/FINAL).exists() else None
        complete=bool(exitcode==0 and not error and core and core['complete'] and final and final['complete'])
        run={'result':RESULT,'p':41,'source_commit':os.environ.get('GITHUB_SHA'),
            'workflow_run_id':os.environ.get('GITHUB_RUN_ID'),'workflow_attempt':os.environ.get('GITHUB_RUN_ATTEMPT'),
            'process_exit_code':exitcode,'complete':complete,'error':error,'outer_timeout':outer_timeout,
            'core_receipt_sha256':sha(out/'core-receipt.json') if core else None,
            'finished_at_utc':dt.datetime.now(dt.timezone.utc).isoformat(),
            'old_mathematical_computations_repeated':False,'original_height_values_computed':False}
        save(out/'run-receipt.json',run);output_manifest(out)
    return 0 if complete else exitcode or 1


def check_source_ref(row,reviewed,nested):
    producer=row['producer']
    if row.get('nested_in')=='POINTS':
        assert producer in nested and nested[producer]['files'][row['file']]==plain(row)
    else:
        assert 'nested_in' not in row and producer in reviewed
        assert reviewed[producer]['files'][row['file']]==plain(row)


def verify(out):
    out=Path(out);initial=read(out/'public-actions-input.json');item=initial['job']
    entries=check_manifest(out)
    assert initial['result']==RESULT and initial['source_repository']=='Rogerhu12/math-research-public'
    assert initial['core_sha256']==item['core_sha256'] and initial['driver_sha256']==item['wrapper_sha256']
    assert sha(__file__)==item['wrapper_sha256']
    retained,receipt,reviewed=prepare_sources(item,out,allow_download=False);tag=expected_tag(item)
    nested=read(retained/'POINTS'/POINT_RECEIPT)['expanded_sources']
    run=read(out/'run-receipt.json');core=read(out/'core-receipt.json') if (out/'core-receipt.json').exists() else None
    assert run['result']==RESULT and run['source_commit']==initial['source_commit']
    if core:
        assert core['result']==RESULT and core['source_sha256']==item['core_sha256']
        assert run['core_receipt_sha256']==sha(out/'core-receipt.json')
    else:assert run['core_receipt_sha256'] is None and run['complete'] is False
    all_math={}
    for path in sorted(out.glob(PREFIX+'*.json.gz')):
        value=read(path)
        assert value['configuration']==tag and value['result']==RESULT and value['complete'] is True
        all_math[path.name]=file_spec(path)
    if not (out/FINAL).exists():
        assert run['complete'] is False
        print('R850_VERIFY='+json.dumps({'complete':False,'completed_math_files':len(all_math)}),flush=True)
        return False
    final=read(out/FINAL);assert final['result']==RESULT and final['configuration']==tag
    assert all(final[key] is False for key in FALSE_FLAGS)
    if final['complete'] is not True:
        assert run['complete'] is False
        print('R850_VERIFY='+json.dumps({'complete':False,'completed_math_files':len(all_math)}),flush=True)
        return False
    assert run['complete'] is True and run['process_exit_code']==0 and run['error'] is None
    assert core and core['complete'] is True and core['certificate_sha256']==sha(out/FINAL)
    assert core['old_mathematical_computations_repeated'] is False
    assert all(final[key] is True for key in TRUE_FLAGS)
    inventory=read(bound(out,final['stage_manifest']))
    assert inventory['configuration']==tag and inventory['complete'] is True
    assert {x['file']:plain(x) for x in inventory['stages']}=={k:v for k,v in all_math.items() if k!=MATH_INVENTORY}
    assert len(inventory['stages'])==2
    audit=read(bound(out,final['source_audit']));graph=read(bound(out,final['exact_expression_DAG']))
    assert audit['all_original_parent_child_identities_and_pq_directions_preserved'] is True
    assert audit['same_original_CM_unit_expression_and_R791_Hom_source_verified'] is True
    assert audit['six_completed_norms_are_nonzero_pure_s_elements'] is True
    assert audit['old_global_node_count']==523 and audit['old_point_node_count']==529
    assert audit['new_CM_Hensel_Dixon_global_solve_point_addition_or_norm_arithmetic'] is False
    assert graph['old_graph_nodes_rewritten_or_recomputed'] is False
    for key in ('all_frame_normalizations_and_true_norm_constants_preserved',
                'original_theta_two_torsion_representative_not_deleted',
                'all_new_Poincare_nodes_are_actual_fixed_original_fibres',
                'all_original_local_height_nodes_remain_unevaluated'):
        assert graph[key] is True
    for key in ('new_scalar_powers_expanded','exact_original_C_h_values_recovered','standard_Jacobian_coordinates_recovered'):
        assert graph[key] is False
    def refs(value):
        if isinstance(value,dict):
            if all(key in value for key in ('producer','file','bytes','sha256')):check_source_ref(value,reviewed,nested)
            for part in value.values():refs(part)
        elif isinstance(value,list):
            for part in value:refs(part)
    refs(graph);refs(audit)
    old_global=read(retained/'GLOBAL'/graph['original_global_program']['file'])
    old_point=read(retained.parent/'original-point-leaves/POINTS'/graph['original_point_program']['file'])
    original_ids={'GLOBAL':{n['id'] for n in old_global['graph_nodes']},
                  'POINTS':{n['id'] for n in old_point['nodes']}}
    seen=set();nodes={}
    for i,node in enumerate(graph['graph_nodes']):
        assert node['ordinal']==i and all(x in seen for x in node['inputs'])
        body={key:node[key] for key in ('operation','domain','inputs','data')}
        assert node['id']=='n'+fingerprint(body) and node['id'] not in seen
        seen.add(node['id']);nodes[node['id']]=node
        if 'denominator_nonzero_proof' in node['data']:
            assert node['data']['denominator_nonzero_proof'] in graph['nonzero_proof_obligations']
        if node['operation']=='completed_original_global_graph_node':
            assert node['data']['original_node_id'] in original_ids['GLOBAL']
        if node['operation']=='completed_original_point_graph_node':
            assert node['data']['original_node_id'] in original_ids['POINTS']
        if node['operation']=='original_full_theta_frame_normalization':
            assert node['data']['inputs_are_rational_coordinates_M_over_s'] is True
            for key in ('M_f_source','M_g_source'):check_source_ref(node['data'][key],reviewed,nested)
        if node['operation']=='original_Hom_pullback_theta_tensor':
            assert node['data']['Hom_source']['nested_in']=='POINTS'
    assert final['actual_graph_node_count']==graph['actual_graph_node_count']==len(seen)
    assert final['actual_nonzero_proof_obligation_count']==graph['actual_nonzero_proof_obligation_count']==len(graph['nonzero_proof_obligations'])
    rows=graph['five_original_fibre_and_section_outputs']
    assert len(rows)==final['completed_original_fibre_count']==5
    id_keys=('original_ideal','real_descent_ideal','xi','xiR','Poincare_v','Poincare_vR',
        'principal_line_isomorphism','rigidified_transport','global_R','R_at_P1','kappa',
        'nu_original_K_expression','nu_exact_Q_expression','full_scalar_nu_kappa_over_R',
        'S_j','u_j','actual_Q_threefold_theta_section','canonical_square_z_j_threefold',
        'complete_corrected_line','normalized_section','normalized_section_smaller_ideal_frame',
        'original_Nh_comparison','specified_original_local_height_expression')
    for j,(row,pq) in enumerate(zip(rows,PQ),1):
        assert row['j']==j and [row['p'],row['q']]==list(pq)
        assert all(row[key] in seen for key in id_keys)
        assert row['these_are_algebraic_frame_coefficients_not_height_jets'] is True
        for key in ('c0_first_unit_coefficient_in_original_real_descent_frame',
                    'c0_first_unit_coefficient_in_smaller_ideal_cubed_frame'):
            assert isinstance(row[key],list) and len(row[key])==2 and all(isinstance(x,str) for x in row[key])
        local=nodes[row['specified_original_local_height_expression']]
        assert local['data']['canonical_periods_evaluated'] is False
        assert local['data']['theta_coefficient']==['1','2']
    print('R850_VERIFY='+json.dumps({'complete':True,'actual_graph_node_count':len(seen),
        'actual_nonzero_proof_obligation_count':len(graph['nonzero_proof_obligations']),
        'completed_original_fibre_count':5,'completed_new_math_stages':len(inventory['stages']),
        'source_member_count':receipt['minimal_bundle_member_count'],'nested_original_point_members':270,
        'GLOBAL_opaque_original_carrier_preserved':True,
        'canonical_Poincare_logarithms_computed':False,'original_height_values_computed':False,
        'all_full_output_manifest_members_verified':len(entries)},sort_keys=True),flush=True)
    return True


def main():
    parser=argparse.ArgumentParser();parser.add_argument('mode',choices=['compute','verify'])
    parser.add_argument('--request',default=str(REQUEST));parser.add_argument('--out',required=True)
    args=parser.parse_args();out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    if args.mode=='verify':
        try:complete=verify(out)
        finally:output_manifest(out)
        raise SystemExit(0 if complete else 1)
    request=Path(args.request);item=read(request);guard(item,request)
    raise SystemExit(compute(item,out,request))


if __name__=='__main__':main()
