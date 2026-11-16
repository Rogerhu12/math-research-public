#!/usr/bin/env python3
"""Standard-library source IO and continuation for the new cleared dual RHS."""
import argparse
import ast
import datetime as dt
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import re
import signal
import subprocess
import sys
import tarfile
import time

S = Path(__file__).resolve().parent
TOPIC = S.parent
REPO = TOPIC.parents[1]
REQUEST = TOPIC/'notes/R787-cleared-dual-CM-value-public-request.json'
RESULT = 'R787-original-cleared-dual-CM-value-acceptance'
FINAL = 'p41-original-cleared-dual-CM-value-acceptance-certificate.json'
PREFIX = 'R787-cleared-dual-'
BUNDLE = 'R787-cleared-dual-retained-inputs.tar.gz'
MANIFEST = 'full-outputs-manifest.json'
REFERENCE = 'full-outputs-manifest-reference.json'
INPUT = 'retained-inputs-receipt.json'
PAIRING_INPUT = 'completed-pairing-inputs-receipt.json'
PAIRING_BUNDLE = 'R787-cleared-dual-completed-pairing-inputs.tar.gz'
OLD_BUNDLE = 'R787-retained-producer-inputs.tar.gz'
CHART = 'R787-prime-1000000753-chart.json.gz'
BLOCKS = 'R787-prime-1000000753-rational-blocks.json.gz'
SELECTION = 'R787-prime-1000000753-selection.json.gz'
OLD_CORE = '93d3d72b01b0ed5d48486a632b74c3470b15affdcb1bd03e21f1b5283fc82d04'
FIELD_CORE = 'd024a7a6f5febd4658e8b5b5e5e3659f3c5fcc0daa39d70569ac408ef83a8751'
OLD_TAG = '71ea66416a42e024de61cf5927bc493fbc8422dc1b5970d75c51bd788d88529d'
CM_FINAL = 'p41-original-implicit-CM-value-certificate.json'
IO_SHA = 'c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c'
PROOF = 'eb5893ec0b8dcc4dd256648a96daa7a605d4cb96efc94a5c42544c0c6dea572b'
METHOD = 'c6ca7d3a8036c2c0b5cfca69fd66ca7108555fae9f90614d7e3618c3044288bd'
BASE = ('result','run_id','source_commit','core_sha256','manifest_sha256')
META = (MANIFEST,'run-receipt.json','core-receipt.json','public-actions-input.json')
H64 = re.compile(r'[0-9a-f]{64}')
IO = None


def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for part in iter(lambda:f.read(1024*1024),b''):h.update(part)
    return h.hexdigest()


def read(path):
    path=Path(path)
    with (gzip.open if path.suffix=='.gz' else open)(path,'rt',encoding='utf-8') as f:return json.load(f)


def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_name(path.name+'.tmp')
    payload=(json.dumps(value,sort_keys=True,separators=(',',':'))+'\n').encode()
    if path.suffix=='.gz':
        with temporary.open('wb') as raw:
            with gzip.GzipFile(fileobj=raw,mode='wb',mtime=0,compresslevel=2) as f:f.write(payload)
    else:temporary.write_bytes(payload)
    temporary.replace(path)


def fingerprint(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def safe(name):
    assert isinstance(name,str) and Path(name).name==name and name not in ('.','..') and '\\' not in name
    return name


def plain(row):
    result={key:row[key] for key in ('file','bytes','sha256')}
    safe(result['file'])
    assert isinstance(result['bytes'],int) and result['bytes']>=0 and H64.fullmatch(result['sha256'])
    return result


def spec(path):
    path=Path(path)
    return {'file':path.name,'bytes':path.stat().st_size,'sha256':sha(path)}


def bound(root,item):
    item=plain(item);path=Path(root)/item['file']
    assert spec(path)==item
    return path


def topic_path(relative):
    path=(TOPIC/relative).resolve()
    assert path.is_relative_to(TOPIC.resolve())
    return path


def static_strategy(core):
    for node in ast.parse(Path(core).read_text()).body:
        if isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name) and node.targets[0].id=='STRATEGY':
            value=ast.literal_eval(node.value)
            assert isinstance(value,dict)
            return value
    raise AssertionError('Pinned core has no literal strategy.')


def load_io(item):
    global IO
    path=S/safe(item['io_helper'])
    assert path.name=='R824_public_original_global_polar_generators.py'
    assert sha(path)==item['io_helper_sha256']==IO_SHA
    source=importlib.util.spec_from_file_location('frozen_R824_dual_IO_only',path)
    IO=importlib.util.module_from_spec(source);source.loader.exec_module(IO)


def guard(item,request):
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public':
        raise SystemExit('This source-bound consumer runs only in the public repository Actions.')
    assert request.resolve()==REQUEST.resolve()
    assert item['result']==RESULT and item['p']==41 and item['producer_inputs_pending'] is False
    assert item['core']=='R787_cleared_dual_CM_value_acceptance.py'
    assert item['wrapper']=='R787_cleared_dual_CM_value_public.py'
    assert item['workflow']=='.github/workflows/serre-R787-cleared-dual-CM-value.yml'
    for key,pin in (('core',item['core_sha256']),('wrapper',item['wrapper_sha256']),
                    ('legacy_core',OLD_CORE),('field_core',FIELD_CORE)):
        assert sha(S/safe(item[key]))==pin==item[key+'_sha256']
    assert sha(topic_path(item['proof']))==item['proof_sha256']==PROOF
    assert sha(topic_path(item['method']))==item['method_sha256']==METHOD
    assert sha(REPO/'README.md')==item['readme_sha256']['root']
    assert sha(TOPIC/'README.md')==item['readme_sha256']['topic']
    assert set(item['sources'])=={'R787','CM'} and 0<item['budget_minutes']<=300
    assert item['sources']['R787']['core_sha256']==OLD_CORE
    assert item['sources']['R787']['expected_conclusion']=='failure'
    assert item['sources']['CM']['expected_conclusion']=='success'
    load_io(item)


def manifest_rows(root,item):
    path=Path(root)/MANIFEST
    assert sha(path)==item['manifest_sha256']
    if item.get('manifest_bytes') is not None:assert path.stat().st_size==item['manifest_bytes']
    value=read(path)
    assert value['result']==item['result']
    rows={row['file']:plain(row) for row in value['files']}
    assert len(rows)==len(value['files'])
    if item.get('manifest_file_count') is not None:assert len(rows)==item['manifest_file_count']
    rows[MANIFEST]=spec(path)
    return rows


def archive_base(item,directory,allow_missing_core=False):
    ar=IO.Archive(item,Path(directory)/'archive',whole=False)
    root=Path(directory)/'files';root.mkdir(parents=True,exist_ok=True)
    ar.extract_bound(MANIFEST,item['manifest_sha256'],root/MANIFEST,item.get('manifest_bytes'))
    rows=manifest_rows(root,item)
    metadata=[name for name in META[1:] if not (allow_missing_core and name=='core-receipt.json' and name not in rows)]
    ar.extract_many([(name,rows[name]['sha256'],root/name,rows[name]['bytes']) for name in metadata])
    return ar,root,rows


def source_metadata(root,item,rows):
    run,core,public=(read(bound(root,rows[name])) for name in META[1:])
    assert run['result']==core['result']==public['result']==item['result']
    assert str(run['workflow_run_id'])==str(item['run_id'])
    assert run['source_commit']==public['source_commit']==item['source_commit']
    assert public['source_repository']=='Rogerhu12/math-research-public'
    assert public['core_sha256']==public['job']['core_sha256']==item['core_sha256']
    assert public['job']['wrapper_sha256']==item['wrapper_sha256']
    if 'wrapper_sha256' in public:assert public['wrapper_sha256']==item['wrapper_sha256']
    assert core['source_sha256']==item['core_sha256']
    assert run['core_receipt_sha256']==rows['core-receipt.json']['sha256']
    expected=item['original_readme_sha256']
    assert public['root_readme_sha256']==expected['root'] and public['topic_readme_sha256']==expected['topic']
    if item['expected_conclusion']=='success':
        assert run['process_exit_code']==0 and run['complete'] is True and run.get('error') is None
        assert core['complete'] is True and core.get('error') is None
    else:
        assert run['process_exit_code'] in item['accepted_checkpoint_exit_codes']
        assert run['complete'] is False and core['complete'] is False
        assert core['all_completed_stages_preserved'] is True
    return run,core,public


def source_spec(item,root,names,certificate=None):
    rows=manifest_rows(root,item)
    files={name:rows[name] for name in sorted(set(names))}
    for row in files.values():bound(root,row)
    if certificate:
        cert=read(bound(root,rows[certificate]))
        assert cert['complete'] is True and cert['result']==item['result']
        tag=cert['configuration']
    else:tag=read(bound(root,rows[CHART]))['configuration']
    assert tag['source_sha256']==item['core_sha256']
    result={key:item[key] for key in BASE}
    result.update(configuration_sha256=fingerprint(tag),files=files,
                  selected_files_sha256=fingerprint([files[name] for name in sorted(files)]))
    if item.get('configuration_sha256'):assert result['configuration_sha256']==item['configuration_sha256']
    if certificate:result['certificate']=rows[certificate]
    return result


def copied(source,target,row):
    path=bound(source,row);destination=Path(target)/row['file']
    destination.parent.mkdir(parents=True,exist_ok=True)
    if destination.exists():assert spec(destination)==plain(row);return
    temporary=destination.with_name(destination.name+'.tmp')
    with path.open('rb') as src,temporary.open('wb') as dst:
        for chunk in iter(lambda:src.read(4*1024*1024),b''):dst.write(chunk)
    assert spec(temporary)['bytes']==row['bytes'] and sha(temporary)==row['sha256']
    temporary.replace(destination)


def original_R787_names():
    return list(META)+[INPUT,CHART,BLOCKS,SELECTION]+[
        'R787-prime-1000000753-branch-'+str(i).zfill(2)+'.json.gz' for i in range(14)]+[
        'R787-real-power5-row-'+str(i).zfill(4)+'.json.gz' for i in range(1234)]


def child_from_bundle(bundle,label,item,root):
    """Legacy child cert/run/manifest binding; no nonexistent receipt is demanded."""
    root=Path(root);root.mkdir(parents=True,exist_ok=True)
    with tarfile.open(bundle,'r:gz') as tar:
        members={}
        for member in tar.getmembers():
            name=PurePosixPath(member.name)
            assert not name.is_absolute() and '..' not in name.parts and not member.issym() and not member.islnk()
            if member.isfile():members.setdefault(name.name,[]).append(member)

        def extract(name,digest,size=None):
            path=root/name
            if path.exists() and sha(path)==digest and (size is None or path.stat().st_size==size):return
            for member in members.get(name,[]):
                if size is not None and member.size!=size:continue
                temporary=path.with_name(path.name+'.tmp')
                h,count=hashlib.sha256(),0
                with tar.extractfile(member) as src,temporary.open('wb') as dst:
                    for chunk in iter(lambda:src.read(4*1024*1024),b''):
                        h.update(chunk);count+=len(chunk);dst.write(chunk)
                if h.hexdigest()==digest and (size is None or count==size):temporary.replace(path);return
                temporary.unlink()
            raise FileNotFoundError('Original bound child file not in carrier: '+label+'/'+name)

        extract(MANIFEST,item['manifest_sha256'])
        rows=manifest_rows(root,item)
        certname=item['certificate_name']
        names=[MANIFEST,certname,'run-receipt.json']
        if label=='R781':
            names+=['R781-original-real-field-input.json.gz']+[
                'R781-inverse-free-Laurent-'+str(i).zfill(3)+'.json.gz' for i in range(130)]
        else:
            assert label=='R786'
            names+=['R786-exact-power5-basis-index.json.gz']
        for name in names[1:]:extract(name,rows[name]['sha256'],rows[name]['bytes'])
    cert=read(root/certname)
    assert rows[certname]['sha256']==item['files'][certname]
    assert cert['complete'] and cert['result']==item['result'] and cert['configuration']['source_sha256']==item['core_sha256']
    run=read(root/'run-receipt.json')
    assert run['source_commit']==item['source_commit'] and str(run['workflow_run_id'])==str(item['run_id'])
    assert run['complete'] is True
    return source_spec(item,root,names,certname)


def verify_original_carrier(bundle,children,retained):
    inventories={label:manifest_rows(Path(retained)/label,item) for label,item in children.items()}
    seen=set()
    with tarfile.open(bundle,'r|gz') as tar:
        for member in tar:
            name=PurePosixPath(member.name)
            assert not name.is_absolute() and '..' not in name.parts and not member.issym() and not member.islnk()
            if member.isdir():continue
            assert member.isfile()
            labels=[part for part in name.parts[:-1] if part in children]
            assert len(labels)==1
            label=labels[0];key=(label,name.name)
            assert key not in seen
            row=inventories[label][name.name]
            assert member.size==row['bytes']
            h,count=hashlib.sha256(),0
            with tar.extractfile(member) as source:
                for chunk in iter(lambda:source.read(4*1024*1024),b''):
                    h.update(chunk);count+=len(chunk)
            assert count==row['bytes'] and h.hexdigest()==row['sha256']
            seen.add(key)
    return {'all_original_carrier_members_hashed_against_original_child_manifests':True,
            'original_carrier_member_count':len(seen)}


def cm_names(root,rows):
    cert=read(bound(root,rows[CM_FINAL]))
    names=list(META)+[CM_FINAL]
    for key in ('implicit_expression','coordinate_candidates','denominator_unit_witness','power5_CM_values_and_jets','exact_eZ'):
        item=plain(cert[key]);assert rows[item['file']]==item;names.append(item['file'])
    index=read(bound(root,cert['power5_CM_values_and_jets']))
    eblocks=[plain(row) for row in index['completed_blocks'] if row['file'].startswith('R787-implicit-CM-power-5-jets-block-')]
    ez=read(bound(root,cert['exact_eZ']))
    zblocks=[plain(row) for row in ez['blocks']]
    assert len(eblocks)==39 and len(zblocks)==38
    for row in eblocks+zblocks:
        assert rows[row['file']]==row
        names.append(row['file'])
    return names


def initial_sources(item,work,retained):
    reports={}
    ar,root,rows=archive_base(item['sources']['R787'],work/'download-R787')
    names=original_R787_names()
    ar.extract_many([(name,rows[name]['sha256'],root/name,rows[name]['bytes']) for name in names if name not in META])
    _,_,public=source_metadata(root,item['sources']['R787'],rows)
    chart=read(bound(root,rows[CHART]));assert fingerprint(chart['configuration'])==OLD_TAG
    bundle_item=plain(rows[OLD_BUNDLE])
    ar.extract_bound(OLD_BUNDLE,bundle_item['sha256'],root/OLD_BUNDLE,bundle_item['bytes'])
    assert public['job']['retained_artifacts']==chart['configuration']['retained_artifacts']
    for name in names:copied(root,retained/'R787',rows[name])
    expanded={'R787':source_spec(item['sources']['R787'],retained/'R787',names)}
    for label,child in chart['configuration']['retained_artifacts'].items():
        assert label in ('R781','R786')
        expanded[label]=child_from_bundle(root/OLD_BUNDLE,label,child,retained/label)
    carrier_review=verify_original_carrier(root/OLD_BUNDLE,chart['configuration']['retained_artifacts'],retained)
    reports['R787']=dict(ar.receipt(),original_input_bundle=bundle_item,**carrier_review)
    ar.close()
    ar,root,rows=archive_base(item['sources']['CM'],work/'download-CM')
    certitem=plain(item['sources']['CM']['certificate'])
    assert rows[CM_FINAL]==certitem
    ar.extract_bound(CM_FINAL,certitem['sha256'],root/CM_FINAL,certitem['bytes'])
    _,core,_=source_metadata(root,item['sources']['CM'],rows)
    assert core['certificate_sha256']==certitem['sha256']
    cert=read(root/CM_FINAL)
    base=[plain(cert[key]) for key in ('implicit_expression','coordinate_candidates','denominator_unit_witness','power5_CM_values_and_jets','exact_eZ')]
    ar.extract_many([(r['file'],r['sha256'],root/r['file'],r['bytes']) for r in base])
    names=cm_names(root,rows)
    ar.extract_many([(name,rows[name]['sha256'],root/name,rows[name]['bytes']) for name in names])
    for name in names:copied(root,retained/'CM',rows[name])
    expanded['CM']=source_spec(item['sources']['CM'],retained/'CM',names,CM_FINAL)
    reports['CM']=ar.receipt();ar.close()
    return expanded,reports


def identity(source):
    result={key:source[key] for key in BASE}
    result.update(configuration_sha256=source['configuration_sha256'],
                  selected_files_sha256=source['selected_files_sha256'])
    if source.get('certificate'):result['certificate']=plain(source['certificate'])
    return result


def review_retained(expanded,retained):
    assert set(expanded)=={'R787','R781','R786','CM'}
    for label,source in expanded.items():
        root=Path(retained)/label
        rows=manifest_rows(root,source)
        assert fingerprint([source['files'][name] for name in sorted(source['files'])])==source['selected_files_sha256']
        for name,row in source['files'].items():
            assert name==row['file'] and plain(row)==rows[name]
            bound(root,row)
        if source.get('certificate'):
            cert=read(bound(root,source['certificate']))
            assert cert['complete'] and cert['result']==source['result']
            tag=cert['configuration']
        else:tag=read(root/CHART)['configuration']
        assert tag['source_sha256']==source['core_sha256'] and fingerprint(tag)==source['configuration_sha256']
    old=read(Path(retained)/'R787'/CHART)['configuration']
    assert fingerprint(old)==OLD_TAG and old['source_sha256']==OLD_CORE
    for label in ('R781','R786'):
        for key in BASE:assert str(old['retained_artifacts'][label][key])==str(expanded[label][key])
        child=old['retained_artifacts'][label]
        assert child['files'][child['certificate_name']]==expanded[label]['certificate']['sha256']
    cmcert=read(Path(retained)/'CM'/CM_FINAL)
    assert cmcert['source_Dixon_digits']==518 and cmcert['new_Dixon_digits_computed']==0
    assert cmcert['characteristic_zero_B0_nonzero_certified'] and cmcert['all_14_branches_units']
    cmold=cmcert['configuration']['source_identities']['R787']
    for key in BASE:assert str(cmold[key])==str(expanded['R787'][key])
    assert cmold['configuration_sha256']==OLD_TAG
    assert len(expanded['R787']['files'])==1256 and len(expanded['R781']['files'])==134
    assert len(expanded['R786']['files'])==4 and len(expanded['CM']['files'])==87
    return {'files':sum(len(value['files']) for value in expanded.values()),
            'groups':{key:len(value['files']) for key,value in expanded.items()},
            'all_selected_original_source_SHA_verified':True,
            'old_prime_inverses_recomputed':False,'mathematics_imported_or_run_during_IO':False}


def build_bundle(out,retained,expanded,reports):
    members=[]
    for label,source in sorted(expanded.items()):
        for name,row in sorted(source['files'].items()):
            bound(Path(retained)/label,row)
            members.append({'relative_path':label+'/'+name,'bytes':row['bytes'],'sha256':row['sha256']})
    destination=out/BUNDLE;temporary=destination.with_name(destination.name+'.tmp')
    with temporary.open('wb') as raw:
        with gzip.GzipFile(fileobj=raw,mode='wb',mtime=0,compresslevel=2) as zipped:
            with tarfile.open(fileobj=zipped,mode='w|') as tar:
                for row in members:
                    path=Path(retained)/row['relative_path']
                    info=tarfile.TarInfo(row['relative_path']);info.size=row['bytes'];info.mtime=0
                    info.mode=0o644;info.uid=info.gid=0;info.uname=info.gname=''
                    with path.open('rb') as source:tar.addfile(info,source)
    temporary.replace(destination)
    receipt={'result':RESULT,'complete':True,'retained_sources':expanded,'members':members,
        'input_bundle':spec(destination),'source_transfer_reports':reports,
        'all_source_member_bytes_verified':True,'source_core_or_inverse_arithmetic_recomputed':False}
    save(out/INPUT,receipt)
    return receipt


def extract_new_bundle(bundle,receipt,retained):
    expected={row['relative_path']:row for row in receipt['members']}
    assert len(expected)==len(receipt['members'])
    seen=set()
    with tarfile.open(bundle,'r:gz') as tar:
        for member in tar:
            name=PurePosixPath(member.name)
            assert member.isfile() and not member.issym() and not member.islnk()
            assert not name.is_absolute() and len(name.parts)==2 and '..' not in name.parts
            relative=str(name);assert relative in expected and relative not in seen
            row=expected[relative];assert member.size==row['bytes']
            path=Path(retained)/relative;path.parent.mkdir(parents=True,exist_ok=True)
            temporary=path.with_name(path.name+'.tmp');h,count=hashlib.sha256(),0
            with tar.extractfile(member) as src,temporary.open('wb') as dst:
                for part in iter(lambda:src.read(4*1024*1024),b''):
                    h.update(part);count+=len(part);dst.write(part)
            assert count==row['bytes'] and h.hexdigest()==row['sha256']
            temporary.replace(path);seen.add(relative)
    assert seen==set(expected)
    return receipt['retained_sources']


def stable_job(item):
    controls={'resume','budget_minutes','maximum_new_digits','reconstruct_every_digits','try_reconstruction_at_start'}
    return {key:value for key,value in item.items() if key not in controls}


def expected_tag(item,expanded,retained):
    old=read(Path(retained)/'R787'/CHART)['configuration']
    return {'result':RESULT,'source_sha256':item['core_sha256'],'python_flint':'0.9.0',
        'proof_sha256':PROOF,'method_sha256':METHOD,'legacy_core_sha256':OLD_CORE,
        'field_core_sha256':FIELD_CORE,'original_configuration_sha256':OLD_TAG,
        'source_identities':{key:identity(value) for key,value in expanded.items()},
        'p':41,'auxiliary_prime':1000000753,'original_map_index':4,'original_map_degree':'1206',
        'field':old['field'],'normalization_free_column':1186,'unknown_shape':[128,280],
        'rational_unknown_dimension':35840,'square_L_output_shape':[1234,1186,140],
        'basis_integer_scale':'13744803133596058624','strategy':static_strategy(S/item['core']),
        'completed_pairing_source':item.get('completed_pairing_source')}



def review_completed_pairing(item,retained,expanded):
    previous=item.get('completed_pairing_source')
    if previous is None:return None
    assert previous['result']==RESULT
    assert previous['core_sha256']=='969201b943bf7591baee92c168546b9992e59b94e1b5b1b2304732b85c052407'
    assert previous['expected_conclusion']=='failure'
    root=Path(retained)/'PAIRING'
    rows=manifest_rows(root,previous)
    files=previous['files']
    expected_names=set(META)|{INPUT,previous['pairing']['file']}
    assert set(files)==expected_names and len(files)==6
    assert fingerprint([files[name] for name in sorted(files)])==previous['selected_files_sha256']
    for name,row in files.items():
        assert name==row['file'] and rows[name]==plain(row)
        bound(root,row)
    run,core,public=(read(root/name) for name in META[1:])
    assert run['result']==core['result']==public['result']==RESULT
    assert str(run['workflow_run_id'])==str(previous['run_id'])
    assert run['source_commit']==public['source_commit']==previous['source_commit']
    assert public['source_repository']=='Rogerhu12/math-research-public'
    assert public['core_sha256']==public['job']['core_sha256']==core['source_sha256']==previous['core_sha256']
    assert public['wrapper_sha256']==public['job']['wrapper_sha256']==previous['wrapper_sha256']
    assert run['core_receipt_sha256']==files['core-receipt.json']['sha256']
    assert run['complete'] is False and core['complete'] is False and run['process_exit_code']==core['exit_code']==1
    assert core['actual_new_dual_digits'] is None and core['configuration'] is None
    assert core['original_value_rowspace_zero_A1_proved'] is False
    assert public['root_readme_sha256']==previous['original_readme_sha256']['root']
    assert public['topic_readme_sha256']==previous['original_readme_sha256']['topic']
    assert public['expanded_sources']==expanded
    receipt=read(root/INPUT)
    assert receipt['complete'] and receipt['result']==RESULT and receipt['retained_sources']==expanded
    assert receipt['all_source_member_bytes_verified'] is True
    assert receipt['source_core_or_inverse_arithmetic_recomputed'] is False
    assert public['job']['sources']==item['sources']
    assert files[previous['pairing']['file']]==plain(previous['pairing'])
    data=read(bound(root,previous['pairing']))
    assert data['complete'] is True and fingerprint(data['configuration'])==previous['configuration_sha256']
    expected=expected_tag(item,expanded,retained)
    expected.pop('completed_pairing_source')
    expected['source_sha256']=previous['core_sha256']
    assert data['configuration']==expected
    for flag in ('ordinary_coefficient_transpose_not_trace_or_Hermitian',
                 'integer_unimodular_pairing_and_full_inverse_identity_verified'):
        assert data[flag] is True
    for key in ('J','J_inverse'):
        assert len(data[key])==20 and all(len(row)==20 for row in data[key])
    assert data['original_t_modulus']==expected['field']['real_cyclotomic_minimal_polynomial']
    return {'source':previous,'stage':{'source_group':'PAIRING',**plain(previous['pairing'])},
        'all_six_original_files_hashed':True,'old_complete_configuration_preserved':True,
        'new_pairing_or_inverse_arithmetic_performed':False}


def unpack_completed_pairing(item,out,retained):
    previous=item['completed_pairing_source']
    receipt=read(out/PAIRING_INPUT)
    assert receipt['result']==RESULT and receipt['source']==previous
    assert spec(out/PAIRING_BUNDLE)==plain(receipt['input_bundle'])
    expected={'PAIRING/'+name:plain(row) for name,row in previous['files'].items()}
    seen=set()
    with tarfile.open(out/PAIRING_BUNDLE,'r:gz') as tar:
        for member in tar:
            name=PurePosixPath(member.name)
            assert member.isfile() and not member.issym() and not member.islnk()
            assert not name.is_absolute() and '..' not in name.parts and len(name.parts)==2
            assert member.name in expected and member.name not in seen
            row=expected[member.name];assert member.size==row['bytes']
            path=Path(retained)/member.name;path.parent.mkdir(parents=True,exist_ok=True)
            temporary=path.with_name(path.name+'.tmp');digest,count=hashlib.sha256(),0
            with tar.extractfile(member) as source,temporary.open('wb') as target:
                for block in iter(lambda:source.read(1048576),b''):
                    target.write(block);digest.update(block);count+=len(block)
            assert count==row['bytes'] and digest.hexdigest()==row['sha256']
            temporary.replace(path);seen.add(member.name)
    assert seen==set(expected)


def prepare_completed_pairing(item,work,out,retained,expanded):
    previous=item.get('completed_pairing_source')
    if previous is None:return None
    if (out/PAIRING_INPUT).exists() and (out/PAIRING_BUNDLE).exists():
        unpack_completed_pairing(item,out,retained)
        return review_completed_pairing(item,retained,expanded)
    root=Path(retained)/'PAIRING';root.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(previous,work/'completed-pairing-source-transfer',whole=False)
    try:
        archive.extract_bound(MANIFEST,previous['manifest_sha256'],root/MANIFEST,previous['manifest_bytes'])
        rows=manifest_rows(root,previous)
        for name,row in previous['files'].items():
            assert rows[name]==plain(row)
        archive.extract_many([(name,row['sha256'],root/name,row['bytes'])
            for name,row in previous['files'].items() if name!=MANIFEST])
        review=review_completed_pairing(item,retained,expanded)
        temporary=out/(PAIRING_BUNDLE+'.tmp')
        with temporary.open('wb') as raw:
            with gzip.GzipFile(fileobj=raw,mode='wb',mtime=0,compresslevel=2) as zipped:
                with tarfile.open(fileobj=zipped,mode='w|') as tar:
                    for name,row in sorted(previous['files'].items()):
                        info=tarfile.TarInfo('PAIRING/'+name);info.size=row['bytes']
                        info.mode=0o644;info.mtime=0;info.uid=info.gid=0;info.uname=info.gname=''
                        with bound(root,row).open('rb') as source:tar.addfile(info,source)
        temporary.replace(out/PAIRING_BUNDLE)
        save(out/PAIRING_INPUT,{'result':RESULT,'source':previous,'input_bundle':spec(out/PAIRING_BUNDLE),
            'source_transport':archive.receipt(),'review':review,
            'original_331MB_carrier_not_downloaded_for_this_pairing_import':True})
        return review
    finally:archive.close()


def restore(item,work,out,retained):
    source=item['resume'];ar,root,rows=archive_base(source,work/'resume-download',allow_missing_core=True)
    # A hard outer timeout is allowed to lack a core receipt. The immutable
    # manifest decides whether it exists; no fictitious receipt is introduced.
    run,public=(read(bound(root,rows[name])) for name in ('run-receipt.json','public-actions-input.json'))
    assert run['result']==public['result']==source['result']==RESULT
    assert run['source_commit']==public['source_commit']==source['source_commit']
    assert str(run['workflow_run_id'])==str(source['run_id'])
    assert public['core_sha256']==source['core_sha256']==item['core_sha256']
    assert public['wrapper_sha256']==item['wrapper_sha256']
    assert stable_job(public['job'])==stable_job(item)
    if 'core-receipt.json' in rows:
        core=read(bound(root,rows['core-receipt.json']))
        assert run['core_receipt_sha256']==rows['core-receipt.json']['sha256']
        assert core['source_sha256']==item['core_sha256'] and core['result']==RESULT
    else:
        assert run['core_receipt_sha256'] is None and run['complete'] is False
    for name in (INPUT,BUNDLE):
        ar.extract_bound(name,rows[name]['sha256'],root/name,rows[name]['bytes'])
    receipt=read(root/INPUT)
    assert receipt['result']==RESULT and receipt['complete'] is True
    assert receipt['input_bundle']==rows[BUNDLE]
    expanded=extract_new_bundle(root/BUNDLE,receipt,retained)
    review_retained(expanded,retained)
    tag=expected_tag(item,expanded,retained)
    names=[name for name in rows if name.startswith(PREFIX) and name.endswith('.json.gz')]
    if FINAL in rows:
        ar.extract_bound(FINAL,rows[FINAL]['sha256'],root/FINAL,rows[FINAL]['bytes'])
        final=read(root/FINAL);assert final['configuration']==tag
        if final.get('complete') is True:names.append(FINAL)
    ar.extract_many([(name,rows[name]['sha256'],root/name,rows[name]['bytes']) for name in names])
    for name in names:
        data=read(root/name);assert data['configuration']==tag
        if data.get('complete') is not True:
            assert name==PREFIX+'current-index.json.gz' and data['complete'] is False
        copied(root,out,rows[name])
    for name in (INPUT,BUNDLE):copied(root,out,rows[name])
    if item.get('completed_pairing_source') is not None:
        for name in (PAIRING_INPUT,PAIRING_BUNDLE):
            ar.extract_bound(name,rows[name]['sha256'],root/name,rows[name]['bytes'])
            copied(root,out,rows[name])
    if FINAL in names:
        final=read(out/FINAL)
        inventory=read(bound(out,final['stage_manifest']))
        for row in inventory['files']+inventory['current_checkpoints']:bound(out,row)
    report=dict(ar.receipt(),restored_files=len(names),same_core_and_mathematical_sources=True,
        incomplete_historical_FINAL_not_replayed=True,all_restored_bytes_verified=True)
    save(out/'resume-receipt.json',report);ar.close()
    return expanded,receipt


def output_manifest(out):
    files=[spec(path) for path in sorted(out.iterdir()) if path.is_file() and
           path.name not in (MANIFEST,REFERENCE) and not path.name.endswith('.tmp')]
    save(out/MANIFEST,{'result':RESULT,'files':files,
        'temporary_active_checkpoint_retention_days':1,'reproducible_tables_in_git_or_release':False})
    save(out/REFERENCE,{'result':RESULT,'manifest':spec(out/MANIFEST)})


def prepare(item,request,work,out):
    out.mkdir(parents=True,exist_ok=True)
    retained=work/'retained';retained.mkdir(parents=True,exist_ok=True)
    if item.get('resume'):
        expanded,receipt=restore(item,work,out,retained)
    else:
        expanded,reports=initial_sources(item,work,retained)
        review_retained(expanded,retained)
        receipt=build_bundle(out,retained,expanded,reports)
    review=review_retained(expanded,retained)
    pairing_review=prepare_completed_pairing(item,work,out,retained,expanded)
    config=dict(item,retained_sources=expanded)
    save(work/'expanded-job.json',config)
    public={'result':RESULT,'source_repository':os.environ['GITHUB_REPOSITORY'],
        'source_commit':os.environ['GITHUB_SHA'],'job':item,'expanded_job_sha256':sha(work/'expanded-job.json'),
        'expanded_sources':expanded,'request_sha256':sha(request),'core_sha256':item['core_sha256'],
        'wrapper_sha256':item['wrapper_sha256'],'proof_sha256':PROOF,'method_sha256':METHOD,
        'root_readme_sha256':sha(REPO/'README.md'),'topic_readme_sha256':sha(TOPIC/'README.md'),
        'prepared_at_utc':dt.datetime.now(dt.timezone.utc).isoformat()}
    save(out/'public-actions-input.json',public)
    output_manifest(out)
    print('INPUT_REVIEW='+json.dumps(dict(review,input_bundle=receipt['input_bundle'],
        actual_new_dual_digits=0,old_primal_current_downloaded=False,
        completed_pairing_source_review=pairing_review),sort_keys=True,separators=(',',':')),flush=True)


def compute(item,request,work,out):
    config=read(work/'expanded-job.json')
    assert stable_job(config)==stable_job(dict(item,retained_sources=config['retained_sources']))
    command=[sys.executable,str(S/item['core']),'--config',str(work/'expanded-job.json'),
        '--proof',str(topic_path(item['proof'])),'--method',str(topic_path(item['method'])),
        '--legacy-core',str(S/item['legacy_core']),'--field-core',str(S/item['field_core']),
        '--retained',str(work/'retained'),'--output',str(out),'--budget-minutes',str(item['budget_minutes'])]
    error=None;code=1
    with (out/'core.log').open('w') as log:
        process=subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
        try:code=process.wait(timeout=item['budget_minutes']*60+900)
        except subprocess.TimeoutExpired:
            error='Outer timeout; completed stages preserved without a fictitious core receipt.'
            os.killpg(process.pid,signal.SIGTERM)
            try:process.wait(timeout=15)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid,signal.SIGKILL);process.wait()
            code=124
    core_path=out/'core-receipt.json';core=read(core_path) if core_path.exists() else None
    final_path=out/FINAL;final=read(final_path) if final_path.exists() else None
    if core is not None:
        assert core['result']==RESULT and core['source_sha256']==item['core_sha256']
    complete=bool(code==0 and core and core['complete'] and final and final['complete'])
    run={'result':RESULT,'complete':complete,'process_exit_code':code,'error':error,
        'source_commit':os.environ['GITHUB_SHA'],'workflow_run_id':os.environ['GITHUB_RUN_ID'],
        'workflow_attempt':os.environ.get('GITHUB_RUN_ATTEMPT','1'),
        'execution_environment':'public-repository-github-actions',
        'core_receipt_sha256':sha(core_path) if core is not None else None,
        'original_value_rowspace_zero_A1_proved':bool(complete and final['original_value_rowspace_zero_A1_proved']),
        'original_candidate_y_strictly_rejected':bool(complete and final['original_candidate_y_strictly_rejected']),
        'finished_at_utc':dt.datetime.now(dt.timezone.utc).isoformat()}
    save(out/'run-receipt.json',run);output_manifest(out)
    print('RUN_RECEIPT='+json.dumps(run,sort_keys=True,separators=(',',':')),flush=True)
    return code


def verify(item,work,out):
    rows={row['file']:plain(row) for row in read(out/MANIFEST)['files']}
    assert len(rows)==len(read(out/MANIFEST)['files'])
    for row in rows.values():bound(out,row)
    receipt=read(bound(out,rows[INPUT]));assert receipt['input_bundle']==rows[BUNDLE]
    review=review_retained(receipt['retained_sources'],work/'retained')
    tag=expected_tag(item,receipt['retained_sources'],work/'retained')
    if item.get('completed_pairing_source') is not None:
        assert rows[PAIRING_BUNDLE]==plain(read(bound(out,rows[PAIRING_INPUT]))['input_bundle'])
        unpack_completed_pairing(item,out,work/'retained')
        review_completed_pairing(item,work/'retained',receipt['retained_sources'])
    run=read(bound(out,rows['run-receipt.json']))
    assert run['result']==RESULT
    if 'core-receipt.json' not in rows:
        assert run['core_receipt_sha256'] is None and run['complete'] is False
        print('PARTIAL_IO_REVIEW='+json.dumps(dict(review,complete=False,missing_core_receipt=True)),flush=True)
        raise SystemExit(1)
    core=read(bound(out,rows['core-receipt.json']))
    assert run['core_receipt_sha256']==rows['core-receipt.json']['sha256']
    assert core['result']==RESULT and core['source_sha256']==item['core_sha256']
    if core.get('configuration') is not None:assert core['configuration']==tag
    for name,row in rows.items():
        if name.startswith(PREFIX) and name.endswith('.json.gz'):
            data=read(bound(out,row));assert data['configuration']==tag
    if FINAL not in rows:
        assert run['complete'] is False
        raise SystemExit('No final decision; all complete source-bound checkpoints remain in this artifact.')
    final=read(bound(out,rows[FINAL]));assert final['configuration']==tag
    source_audit=read(bound(out,final['source_audit']))
    assert source_audit['configuration']==tag and source_audit['complete'] is True
    if item.get('completed_pairing_source') is not None:
        assert source_audit['pairing']=={'source_group':'PAIRING',**plain(item['completed_pairing_source']['pairing'])}
        assert source_audit['completed_original_pairing_reused_without_recomputation'] is True
    inventory=read(bound(out,final['stage_manifest']))
    assert inventory['complete'] and inventory['configuration']==tag
    for row in inventory['files']+inventory['current_checkpoints']:
        assert rows[row['file']]==plain(row);bound(out,row)
    assert final['source_CM_Dixon_digits']==518 and final['source_CM_Dixon_digits_used_as_dual_precision'] is False
    assert final['old_primal_inverse_Laurent_CM_or_function_Dixon_arithmetic_recomputed'] is False
    assert final['original_expanded_x_and_derivative_accepted'] is False
    if not final['complete']:
        assert not final['dual_linear_system_exactly_solved'] and not final['original_value_rowspace_zero_A1_proved']
        assert not final['original_candidate_y_strictly_rejected']
        print('PARTIAL_IO_REVIEW='+json.dumps(dict(review,complete=False,
            actual_new_dual_digits=final['actual_new_dual_digits'],reason=final['reason'])),flush=True)
        raise SystemExit(1)
    assert run['complete'] and run['process_exit_code']==0 and core['complete']
    assert final['dual_linear_system_exactly_solved']
    obstruction=read(bound(out,final['exact_value_obstruction']))
    assert obstruction['complete'] and obstruction['configuration']==tag
    exact=read(bound(out,obstruction['exact_transpose_certificate']))
    assert exact['all35840_rational_coordinates_verified'] and exact['verified_L_coordinate_groups']==[1234,1186,140]
    delta=obstruction['Delta_original_L_coordinates'];assert len(delta)==14
    zero=all(row[0]=='0' for row in delta)
    assert zero==final['original_value_rowspace_zero_A1_proved']==obstruction['original_value_rowspace_zero_A1_proved']
    assert (not zero)==final['original_candidate_y_strictly_rejected']==obstruction['original_candidate_y_strictly_rejected']
    assert final['actual_eta_or_height_computed'] is False
    print('COMPLETE_IO_REVIEW='+json.dumps(dict(review,complete=True,
        actual_new_dual_digits=final['actual_new_dual_digits'],original_value_rowspace_zero_A1_proved=zero,
        original_candidate_y_strictly_rejected=not zero,seconds=final['seconds'],
        final=rows[FINAL],stage_manifest=final['stage_manifest']),sort_keys=True,separators=(',',':')),flush=True)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('mode',choices=('prepare','compute','verify'))
    parser.add_argument('--request',type=Path,default=REQUEST)
    parser.add_argument('--work',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();item=read(args.request)['job']
    guard(item,args.request)
    args.work.mkdir(parents=True,exist_ok=True);args.output.mkdir(parents=True,exist_ok=True)
    if args.mode=='prepare':prepare(item,args.request,args.work,args.output);return 0
    if args.mode=='compute':return compute(item,args.request,args.work,args.output)
    verify(item,args.work,args.output);return 0


if __name__=='__main__':sys.exit(main())
