#!/usr/bin/env python3
"""Pure source IO for a new half-coordinate continuation of the full dual."""
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

S = Path(__file__).resolve().parent
TOPIC = S.parent
REPO = TOPIC.parents[1]
REQUEST = TOPIC/'notes/R787-half-coordinate-dual-CM-value-public-request.json'
RESULT = 'R787-original-cleared-dual-CM-value-acceptance'
FINAL = 'p41-original-cleared-dual-CM-value-acceptance-certificate.json'
PREFIX = 'R787-cleared-dual-'
HALF = PREFIX+'half-'
MANIFEST = 'full-outputs-manifest.json'
REFERENCE = 'full-outputs-manifest-reference.json'
INPUT = 'retained-inputs-receipt.json'
BUNDLE = 'R787-cleared-dual-retained-inputs.tar.gz'
PAIRING_INPUT = 'completed-pairing-inputs-receipt.json'
PAIRING_BUNDLE = 'R787-cleared-dual-completed-pairing-inputs.tar.gz'
FULL_INPUT = 'completed-full-dual-inputs-receipt.json'
FULL_BUNDLE = 'R787-half-dual-completed-full-dual-inputs.tar.gz'
FULL_CORE = 'bad9741493b550b0d3543ec953642c2b2f11f30da4433c9346f0c3215d415323'
FULL_WRAPPER = '5388274c6425e66e6c3d2d8d1d41b5a4a59f7787479695970ede670e0091b32f'
ORIGINAL_CORE = '93d3d72b01b0ed5d48486a632b74c3470b15affdcb1bd03e21f1b5283fc82d04'
FIELD_CORE = 'd024a7a6f5febd4658e8b5b5e5e3659f3c5fcc0daa39d70569ac408ef83a8751'
PROOF = '281de249137d88da3c67a25261ca744bd513ecb15b49ffb0125d82f7fb6b7c6f'
NESTED_PROOF = 'eb5893ec0b8dcc4dd256648a96daa7a605d4cb96efc94a5c42544c0c6dea572b'
FULL_METHOD = 'c6ca7d3a8036c2c0b5cfca69fd66ca7108555fae9f90614d7e3618c3044288bd'
BASE = ('result','run_id','source_commit','core_sha256','manifest_sha256')
META = (MANIFEST,'run-receipt.json','public-actions-input.json')
H64 = re.compile(r'[0-9a-f]{64}')
FULL = None
IO = None


def sha(path):
    digest=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for part in iter(lambda:stream.read(1024*1024),b''):digest.update(part)
    return digest.hexdigest()


def read(path):
    path=Path(path)
    with (gzip.open if path.suffix=='.gz' else open)(path,'rt',encoding='utf-8') as stream:return json.load(stream)


def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temp=path.with_name(path.name+'.tmp')
    payload=(json.dumps(value,sort_keys=True,separators=(',',':'))+'\n').encode()
    if path.suffix=='.gz':
        with temp.open('wb') as raw:
            with gzip.GzipFile(fileobj=raw,mode='wb',mtime=0,compresslevel=2) as stream:stream.write(payload)
    else:temp.write_bytes(payload)
    temp.replace(path)


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


def bound(root,row):
    row=plain(row);path=Path(root)/row['file']
    assert spec(path)==row
    return path


def topic_path(relative):
    path=(TOPIC/relative).resolve()
    assert path.is_relative_to(TOPIC.resolve())
    return path


def static_strategy(path):
    for node in ast.parse(Path(path).read_text()).body:
        if isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name) and node.targets[0].id=='STRATEGY':
            value=ast.literal_eval(node.value);assert isinstance(value,dict);return value
    raise AssertionError('Pinned core has no literal strategy.')


def load_io(item):
    global FULL,IO
    path=S/safe(item['full_dual_wrapper'])
    assert path.name=='R787_cleared_dual_CM_value_public.py'
    assert sha(path)==item['full_dual_wrapper_sha256']==FULL_WRAPPER
    source=importlib.util.spec_from_file_location('frozen_full_dual_half_IO_only',path)
    FULL=importlib.util.module_from_spec(source);source.loader.exec_module(FULL)
    FULL.load_io(item);IO=FULL.IO


def guard(item,request):
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public':
        raise SystemExit('This continuation runs only in the public repository Actions.')
    assert request.resolve()==REQUEST.resolve()
    assert item['result']==RESULT and item['p']==41 and item['producer_inputs_pending'] is False
    assert item['completed_dual_source'] is not None and item['completed_pairing_source'] is not None
    assert item['core']=='R787_half_coordinate_dual_CM_value_acceptance.py'
    assert item['wrapper']=='R787_half_coordinate_dual_CM_value_public.py'
    assert item['workflow']=='.github/workflows/serre-R787-half-coordinate-dual-CM-value.yml'
    for key,pin in (('core',item['core_sha256']),('wrapper',item['wrapper_sha256']),
                    ('full_dual_core',FULL_CORE),('legacy_core',ORIGINAL_CORE),('field_core',FIELD_CORE)):
        assert sha(S/safe(item[key]))==pin==item[key+'_sha256']
    assert sha(topic_path(item['proof']))==item['proof_sha256']==PROOF
    assert sha(topic_path(item['nested_proof']))==item['nested_proof_sha256']==NESTED_PROOF
    assert sha(topic_path(item['method']))==item['method_sha256']
    assert item['full_dual_method_sha256']==FULL_METHOD
    assert sha(REPO/'README.md')==item['readme_sha256']['root']
    assert sha(TOPIC/'README.md')==item['readme_sha256']['topic']
    assert 0<item['budget_minutes']<=300
    assert item['completed_dual_source']['core_sha256']==FULL_CORE
    assert item['completed_dual_source']['wrapper_sha256']==FULL_WRAPPER
    assert item['completed_dual_source']['expected_conclusion']=='failure'
    assert isinstance(item['completed_dual_source']['source_dual_digits'],int)
    assert item['completed_dual_source']['source_dual_digits']>=1
    load_io(item)


def manifest_rows(root,item):
    path=Path(root)/MANIFEST
    assert spec(path)=={'file':MANIFEST,'bytes':item['manifest_bytes'],'sha256':item['manifest_sha256']}
    value=read(path);assert value['result']==item['result']
    rows={row['file']:plain(row) for row in value['files']}
    assert len(rows)==len(value['files'])==item['manifest_file_count']
    rows[MANIFEST]=spec(path)
    return rows


def copied(root,target,row):
    FULL.copied(root,target,plain(row))


def old_tag(item,expanded,retained):
    old=read(Path(retained)/'R787'/FULL.CHART)['configuration']
    return {'result':RESULT,'source_sha256':FULL_CORE,'python_flint':'0.9.0',
        'proof_sha256':NESTED_PROOF,'method_sha256':FULL_METHOD,
        'legacy_core_sha256':ORIGINAL_CORE,'field_core_sha256':FIELD_CORE,
        'original_configuration_sha256':FULL.OLD_TAG,
        'source_identities':{key:FULL.identity(value) for key,value in expanded.items()},
        'p':41,'auxiliary_prime':1000000753,'original_map_index':4,'original_map_degree':'1206',
        'field':old['field'],'normalization_free_column':1186,'unknown_shape':[128,280],
        'rational_unknown_dimension':35840,'square_L_output_shape':[1234,1186,140],
        'basis_integer_scale':'13744803133596058624',
        'strategy':static_strategy(S/item['full_dual_core']),
        'completed_pairing_source':item['completed_pairing_source']}


def completed_identity(source):
    result={key:source[key] for key in BASE}
    result.update(configuration_sha256=source['configuration_sha256'],
        selected_files_sha256=source['selected_files_sha256'],
        current=plain(source['current']),exact_target=plain(source['exact_target']),
        source_audit=plain(source['source_audit']),source_dual_digits=source['source_dual_digits'])
    return result


def expected_tag(item,expanded,source,retained):
    parent=old_tag(item,expanded,retained)
    return {'result':RESULT,'source_sha256':item['core_sha256'],'python_flint':'0.9.0',
        'proof_sha256':PROOF,'nested_proof_sha256':NESTED_PROOF,
        'method_sha256':item['method_sha256'],'full_dual_core_sha256':FULL_CORE,
        'full_dual_method_sha256':FULL_METHOD,'legacy_core_sha256':ORIGINAL_CORE,
        'field_core_sha256':FIELD_CORE,'original_configuration_sha256':FULL.OLD_TAG,
        'source_identities':parent['source_identities'],
        'completed_dual_source':completed_identity(source),
        'completed_pairing_source':item['completed_pairing_source'],
        'p':41,'auxiliary_prime':1000000753,'original_map_index':4,'original_map_degree':'1206',
        'field':parent['field'],'normalization_free_column':1186,
        'unknown_shape':[128,280],'retained_half_shape':[128,140],
        'rational_unknown_dimension':35840,'rational_reconstruction_dimension':17920,
        'square_L_output_shape':[1234,1186,140],'basis_integer_scale':'13744803133596058624',
        'strategy':static_strategy(S/item['core'])}


def review_completed_source(item,source,expanded,retained):
    root=Path(retained)/'FULL_DUAL'
    rows=manifest_rows(root,source)
    assert source['core_sha256']==FULL_CORE and source['wrapper_sha256']==FULL_WRAPPER
    files=source['files']
    assert fingerprint([files[name] for name in sorted(files)])==source['selected_files_sha256']
    for name,row in files.items():
        assert name==row['file'] and rows[name]==plain(row)
        bound(root,row)
    run,public=(read(root/name) for name in ('run-receipt.json','public-actions-input.json'))
    assert run['result']==public['result']==RESULT
    assert str(run['workflow_run_id'])==str(source['run_id'])
    assert run['source_commit']==public['source_commit']==source['source_commit']
    assert public['source_repository']=='Rogerhu12/math-research-public'
    assert public['core_sha256']==public['job']['core_sha256']==FULL_CORE
    assert public['wrapper_sha256']==public['job']['wrapper_sha256']==FULL_WRAPPER
    assert public['expanded_sources']==expanded
    assert public['job']['completed_pairing_source']==item['completed_pairing_source']
    assert public['job']['sources']==item['sources']
    assert public['root_readme_sha256']==source['original_readme_sha256']['root']
    assert public['topic_readme_sha256']==source['original_readme_sha256']['topic']
    assert run['complete'] is False and run['process_exit_code'] in source['accepted_checkpoint_exit_codes']
    tag=old_tag(item,expanded,retained)
    assert fingerprint(tag)==source['configuration_sha256']
    if 'core-receipt.json' in files:
        core=read(root/'core-receipt.json')
        assert run['core_receipt_sha256']==files['core-receipt.json']['sha256']
        assert core['result']==RESULT and core['source_sha256']==FULL_CORE and core['complete'] is False
        if core.get('configuration') is not None:assert core['configuration']==tag
    else:assert run['core_receipt_sha256'] is None
    current=read(bound(root,source['current']))
    assert current['complete'] is True and current['configuration']==tag
    assert current['prime']==1000000753 and current['digits']==source['source_dual_digits']>=1
    assert current['full_square_modular_identity_verified'] is True
    assert current['old_primal_precision_or_vector_reused_as_dual'] is False
    assert current['exact_target']==plain(source['exact_target']) and current['source_audit']==plain(source['source_audit'])
    assert len(current['chi_integer_coordinates'])==128 and all(len(row)==280 for row in current['chi_integer_coordinates'])
    target=read(bound(root,source['exact_target']))
    assert target['configuration']==tag and target['complete'] is True
    assert target['old_CM_values_or_eZ_recomputed'] is False
    assert target['original_scale_applied_once']=='13744803133596058624'
    assert len(target['target_integer_L_rows'])==2560 and all(len(row)==14 for row in target['target_integer_L_rows'])
    assert len(target['candidate_y'])==len(target['free_obstruction_addend_d_q_Ef'])==14
    audit=read(bound(root,source['source_audit']))
    assert audit['complete'] is True and audit['configuration']==tag
    assert audit['exact_target']==plain(source['exact_target'])
    assert audit['source_identities']==tag['source_identities']
    assert audit['old_prime_inverses_read_without_recomputation'] is True
    assert audit['old_primal_current_consumed'] is False
    assert audit['completed_original_pairing_reused_without_recomputation'] is True
    assert audit['pairing']=={'source_group':'PAIRING',**plain(item['completed_pairing_source']['pairing'])}
    receipt=read(root/INPUT)
    assert receipt['result']==RESULT and receipt['complete'] is True
    assert receipt['retained_sources']==expanded and receipt['input_bundle']==plain(source['input_bundle'])
    assert receipt['all_source_member_bytes_verified'] is True
    expected_names=set(META)|{INPUT,PAIRING_INPUT}
    if 'core-receipt.json' in rows:expected_names.add('core-receipt.json')
    if FINAL in rows:expected_names.add(FINAL)
    expected_names.update(name for name in rows if name.startswith(PREFIX) and name.endswith('.json.gz'))
    assert set(files)==expected_names
    numbers=[]
    for name in sorted(files):
        if not (name.startswith(PREFIX) and name.endswith('.json.gz')):continue
        stage=read(root/name);assert stage['configuration']==tag
        if stage.get('complete') is not True:
            assert name==PREFIX+'current-index.json.gz' and stage['complete'] is False
        match=re.fullmatch(re.escape(PREFIX)+r'current-(\d{8})\.json\.gz',name)
        if match:numbers.append((int(match.group(1)),name))
    assert max(numbers)==(source['source_dual_digits'],source['current']['file'])
    if FINAL in files:
        final=read(root/FINAL);assert final['configuration']==tag and final['complete'] is False
    # The current-index or historical false FINAL may precede an atomically
    # completed newer current. The manifest and maximal completed filename are
    # authoritative; no old snapshot is substituted for the actual new file.
    return {'source':completed_identity(source),'original_selected_files':len(files),
        'original_dual_digits':source['source_dual_digits'],
        'all_original_stage_bytes_and_configuration_verified':True,
        'original_completed_arithmetic_not_executed_in_IO':True,
        'missing_original_core_receipt':'core-receipt.json' not in files}


def write_full_bundle(out,retained,source,report):
    members=[{'relative_path':'FULL_DUAL/'+name,'bytes':row['bytes'],'sha256':row['sha256']}
             for name,row in sorted(source['files'].items())]
    target=out/FULL_BUNDLE;temp=target.with_name(target.name+'.tmp')
    with temp.open('wb') as raw:
        with gzip.GzipFile(fileobj=raw,mode='wb',mtime=0,compresslevel=2) as zipped:
            with tarfile.open(fileobj=zipped,mode='w|') as tar:
                for row in members:
                    path=Path(retained)/row['relative_path']
                    assert path.stat().st_size==row['bytes'] and sha(path)==row['sha256']
                    info=tarfile.TarInfo(row['relative_path']);info.size=row['bytes']
                    info.mode=0o644;info.mtime=0;info.uid=info.gid=0;info.uname=info.gname=''
                    with path.open('rb') as stream:tar.addfile(info,stream)
    temp.replace(target)
    receipt={'result':RESULT,'complete':True,'completed_dual_source':source,
        'members':members,'input_bundle':spec(target),'source_transfer':report,
        'all_original_stage_bytes_preserved':True,'old_configuration_not_rewritten':True,
        'mathematical_arithmetic_performed':False}
    save(out/FULL_INPUT,receipt)
    return receipt


def extract_full_bundle(bundle,receipt,retained):
    expected={row['relative_path']:row for row in receipt['members']}
    assert len(expected)==len(receipt['members'])
    seen=set()
    with tarfile.open(bundle,'r:gz') as tar:
        for member in tar:
            path=PurePosixPath(member.name)
            assert member.isfile() and not member.issym() and not member.islnk()
            assert not path.is_absolute() and len(path.parts)==2 and path.parts[0]=='FULL_DUAL' and '..' not in path.parts
            assert member.name in expected and member.name not in seen
            row=expected[member.name];assert member.size==row['bytes']
            dest=Path(retained)/member.name;dest.parent.mkdir(parents=True,exist_ok=True)
            temp=dest.with_name(dest.name+'.tmp');h,count=hashlib.sha256(),0
            with tar.extractfile(member) as src,temp.open('wb') as dst:
                for part in iter(lambda:src.read(4*1024*1024),b''):
                    h.update(part);count+=len(part);dst.write(part)
            assert count==row['bytes'] and h.hexdigest()==row['sha256']
            temp.replace(dest);seen.add(member.name)
    assert seen==set(expected)
    return receipt['completed_dual_source']


def initial(item,work,out,retained):
    source=item['completed_dual_source']
    ar=IO.Archive(source,work/'completed-full-dual-transfer',whole=False)
    root=work/'completed-full-dual-selected';root.mkdir(parents=True,exist_ok=True)
    try:
        ar.extract_bound(MANIFEST,source['manifest_sha256'],root/MANIFEST,source['manifest_bytes'])
        rows=manifest_rows(root,source)
        for key in ('current','exact_target','source_audit','input_bundle','pairing_input_bundle'):
            assert rows[source[key]['file']]==plain(source[key])
        assert source['input_bundle']['file']==BUNDLE and source['pairing_input_bundle']['file']==PAIRING_BUNDLE
        names=set(META)|{INPUT,PAIRING_INPUT}
        if 'core-receipt.json' in rows:names.add('core-receipt.json')
        if FINAL in rows:names.add(FINAL)
        names.update(name for name in rows if name.startswith(PREFIX) and name.endswith('.json.gz'))
        ar.extract_many([(name,rows[name]['sha256'],root/name,rows[name]['bytes']) for name in sorted(names) if name!=MANIFEST])
        for name in (BUNDLE,PAIRING_BUNDLE):
            ar.extract_bound(name,rows[name]['sha256'],out/name,rows[name]['bytes'])
        for name in (INPUT,PAIRING_INPUT):copied(root,out,rows[name])
        receipt=read(out/INPUT)
        assert receipt['result']==RESULT and receipt['complete'] is True
        assert receipt['input_bundle']==rows[BUNDLE]
        expanded=FULL.extract_new_bundle(out/BUNDLE,receipt,retained)
        FULL.review_retained(expanded,retained)
        public=read(root/'public-actions-input.json')
        oldjob=public['job']
        assert oldjob['completed_pairing_source']==item['completed_pairing_source']
        assert oldjob['sources']==item['sources']
        FULL.unpack_completed_pairing(oldjob,out,retained)
        FULL.review_completed_pairing(oldjob,retained,expanded)
        full_source=dict(source,files={name:rows[name] for name in sorted(names)})
        full_source['selected_files_sha256']=fingerprint([full_source['files'][name] for name in sorted(names)])
        destination=retained/'FULL_DUAL';destination.mkdir(parents=True,exist_ok=True)
        for name in sorted(names):copied(root,destination,rows[name])
        review=review_completed_source(item,full_source,expanded,retained)
        transport=ar.receipt()
        full_receipt=write_full_bundle(out,retained,full_source,transport)
        print('FULL_DUAL_SOURCE_REVIEW='+json.dumps(dict(review,source_transfer=transport,
            completed_full_dual_bundle=full_receipt['input_bundle']),sort_keys=True,separators=(',',':')),flush=True)
        return expanded,full_source
    finally:ar.close()


def stable_job(item):
    controls={'resume','budget_minutes','maximum_new_digits','reconstruct_every_digits','rules_last_read_commit'}
    return {key:value for key,value in item.items() if key not in controls}


def restore(item,work,out,retained):
    source=item['resume']
    ar=IO.Archive(source,work/'resume-transfer',whole=False)
    root=work/'resume-selected';root.mkdir(parents=True,exist_ok=True)
    try:
        ar.extract_bound(MANIFEST,source['manifest_sha256'],root/MANIFEST,source['manifest_bytes'])
        rows=manifest_rows(root,source)
        names={'run-receipt.json','public-actions-input.json',INPUT,PAIRING_INPUT,FULL_INPUT}
        if 'core-receipt.json' in rows:names.add('core-receipt.json')
        ar.extract_many([(name,rows[name]['sha256'],root/name,rows[name]['bytes']) for name in sorted(names)])
        run,public=(read(root/name) for name in ('run-receipt.json','public-actions-input.json'))
        assert run['result']==public['result']==source['result']==RESULT
        assert str(run['workflow_run_id'])==str(source['run_id'])
        assert run['source_commit']==public['source_commit']==source['source_commit']
        assert public['core_sha256']==source['core_sha256']==item['core_sha256']
        assert public['wrapper_sha256']==source['wrapper_sha256']==item['wrapper_sha256']
        assert stable_job(public['job'])==stable_job(item)
        core=None
        if 'core-receipt.json' in rows:
            core=read(root/'core-receipt.json')
            assert run['core_receipt_sha256']==rows['core-receipt.json']['sha256']
            assert core['source_sha256']==item['core_sha256'] and core['result']==RESULT
        else:assert run['core_receipt_sha256'] is None and run['complete'] is False
        for name in (BUNDLE,PAIRING_BUNDLE,FULL_BUNDLE):
            ar.extract_bound(name,rows[name]['sha256'],out/name,rows[name]['bytes'])
        for name in (INPUT,PAIRING_INPUT,FULL_INPUT):copied(root,out,rows[name])
        original_receipt=read(out/INPUT)
        assert original_receipt['input_bundle']==rows[BUNDLE]
        expanded=FULL.extract_new_bundle(out/BUNDLE,original_receipt,retained)
        previous_receipt=read(out/FULL_INPUT)
        assert previous_receipt['result']==RESULT and previous_receipt['complete'] is True
        assert previous_receipt['input_bundle']==rows[FULL_BUNDLE]
        completed=extract_full_bundle(out/FULL_BUNDLE,previous_receipt,retained)
        assert {key:value for key,value in completed.items() if key not in ('files','selected_files_sha256')}==item['completed_dual_source']
        oldpublic=read(retained/'FULL_DUAL'/'public-actions-input.json')
        FULL.unpack_completed_pairing(oldpublic['job'],out,retained)
        FULL.review_completed_pairing(oldpublic['job'],retained,expanded)
        FULL.review_retained(expanded,retained)
        review_completed_source(item,completed,expanded,retained)
        tag=expected_tag(item,expanded,completed,retained)
        if core is not None and core.get('configuration') is not None:assert core['configuration']==tag
        names={name for name in rows if name.startswith(PREFIX) and name.endswith('.json.gz')}
        if FINAL in rows:
            ar.extract_bound(FINAL,rows[FINAL]['sha256'],root/FINAL,rows[FINAL]['bytes'])
            final=read(root/FINAL);assert final['configuration']==tag
            if final.get('complete') is True:names.add(FINAL)
        ar.extract_many([(name,rows[name]['sha256'],root/name,rows[name]['bytes']) for name in sorted(names)])
        for name in sorted(names):
            data=read(root/name);assert data['configuration']==tag
            if data.get('complete') is not True:assert name==PREFIX+'current-index.json.gz'
            copied(root,out,rows[name])
        if FINAL in names:
            final=read(out/FINAL);inventory=read(bound(out,final['stage_manifest']))
            for row in inventory['files']+inventory['current_checkpoints']:bound(out,row)
        save(out/'resume-receipt.json',dict(ar.receipt(),restored_stages=len(names),
            all_complete_bytes_verified=True,incomplete_historical_FINAL_not_replayed=True,
            same_new_core_tag_and_original_dual_anchor=True))
        return expanded,completed
    finally:ar.close()


def output_manifest(out):
    FULL.output_manifest(out)


def prepare(item,request,work,out):
    out.mkdir(parents=True,exist_ok=True)
    retained=work/'retained';retained.mkdir(parents=True,exist_ok=True)
    expanded,source=restore(item,work,out,retained) if item.get('resume') else initial(item,work,out,retained)
    original_review=FULL.review_retained(expanded,retained)
    source_review=review_completed_source(item,source,expanded,retained)
    config=dict(item,retained_sources=expanded,completed_dual_source=source)
    save(work/'expanded-job.json',config)
    public={'result':RESULT,'source_repository':os.environ['GITHUB_REPOSITORY'],
        'source_commit':os.environ['GITHUB_SHA'],'job':item,'expanded_job_sha256':sha(work/'expanded-job.json'),
        'expanded_sources':expanded,'expanded_completed_dual_source':source,
        'request_sha256':sha(request),'core_sha256':item['core_sha256'],'wrapper_sha256':item['wrapper_sha256'],
        'proof_sha256':PROOF,'nested_proof_sha256':NESTED_PROOF,'method_sha256':item['method_sha256'],
        'root_readme_sha256':sha(REPO/'README.md'),'topic_readme_sha256':sha(TOPIC/'README.md'),
        'prepared_at_utc':dt.datetime.now(dt.timezone.utc).isoformat()}
    save(out/'public-actions-input.json',public);output_manifest(out)
    print('INPUT_REVIEW='+json.dumps(dict(original_review,completed_full_dual_source=source_review,
        old_target_pairing_or_dual_arithmetic_recomputed=False),sort_keys=True,separators=(',',':')),flush=True)


def compute(item,request,work,out):
    config=read(work/'expanded-job.json')
    expected=dict(item,retained_sources=config['retained_sources'],completed_dual_source=config['completed_dual_source'])
    assert stable_job(config)==stable_job(expected)
    command=[sys.executable,str(S/item['core']),'--config',str(work/'expanded-job.json'),
        '--proof',str(topic_path(item['proof'])),'--nested-proof',str(topic_path(item['nested_proof'])),
        '--method',str(topic_path(item['method'])),'--full-dual-core',str(S/item['full_dual_core']),
        '--legacy-core',str(S/item['legacy_core']),'--field-core',str(S/item['field_core']),
        '--retained',str(work/'retained'),'--output',str(out),'--budget-minutes',str(item['budget_minutes'])]
    error,code=None,1
    with (out/'core.log').open('w') as log:
        process=subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
        try:code=process.wait(timeout=item['budget_minutes']*60+900)
        except subprocess.TimeoutExpired:
            error='Outer timeout; committed stages preserved; no fictitious core receipt.'
            os.killpg(process.pid,signal.SIGTERM)
            try:process.wait(timeout=15)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid,signal.SIGKILL);process.wait()
            code=124
    core_path,final_path=out/'core-receipt.json',out/FINAL
    core=read(core_path) if core_path.exists() else None
    final=read(final_path) if final_path.exists() else None
    if core is not None:assert core['result']==RESULT and core['source_sha256']==item['core_sha256']
    complete=bool(code==0 and core and core['complete'] and final and final['complete'])
    run={'result':RESULT,'complete':complete,'process_exit_code':code,'error':error,
        'source_commit':os.environ['GITHUB_SHA'],'workflow_run_id':os.environ['GITHUB_RUN_ID'],
        'workflow_attempt':os.environ.get('GITHUB_RUN_ATTEMPT','1'),
        'execution_environment':'public-repository-github-actions',
        'core_receipt_sha256':sha(core_path) if core is not None else None,
        'decision_kind':final.get('decision_kind') if complete else None,
        'original_value_rowspace_zero_A1_proved':bool(complete and final['original_value_rowspace_zero_A1_proved']),
        'original_candidate_y_strictly_rejected':bool(complete and final['original_candidate_y_strictly_rejected']),
        'finished_at_utc':dt.datetime.now(dt.timezone.utc).isoformat()}
    save(out/'run-receipt.json',run);output_manifest(out)
    print('RUN_RECEIPT='+json.dumps(run,sort_keys=True,separators=(',',':')),flush=True)
    return code


def reference_source(retained,source,row):
    assert row.get('source_group')=='FULL_DUAL'
    assert source['files'][row['file']]==plain(row)
    return bound(Path(retained)/'FULL_DUAL',row)


def verify(item,work,out):
    manifest=read(out/MANIFEST)
    rows={row['file']:plain(row) for row in manifest['files']}
    assert manifest['result']==RESULT and len(rows)==len(manifest['files'])
    for row in rows.values():bound(out,row)
    receipt=read(bound(out,rows[INPUT]));assert receipt['input_bundle']==rows[BUNDLE]
    expanded=receipt['retained_sources']
    original_review=FULL.review_retained(expanded,work/'retained')
    source_receipt=read(bound(out,rows[FULL_INPUT]))
    assert source_receipt['complete'] is True and source_receipt['input_bundle']==rows[FULL_BUNDLE]
    source=source_receipt['completed_dual_source']
    assert {key:value for key,value in source.items() if key not in ('files','selected_files_sha256')}==item['completed_dual_source']
    source_review=review_completed_source(item,source,expanded,work/'retained')
    oldpublic=read(work/'retained'/'FULL_DUAL'/'public-actions-input.json')
    assert rows[PAIRING_BUNDLE]==plain(read(bound(out,rows[PAIRING_INPUT]))['input_bundle'])
    FULL.review_completed_pairing(oldpublic['job'],work/'retained',expanded)
    tag=expected_tag(item,expanded,source,work/'retained')
    run=read(bound(out,rows['run-receipt.json']))
    assert run['result']==RESULT
    for name,row in rows.items():
        if name.startswith(PREFIX) and name.endswith('.json.gz'):
            value=read(bound(out,row));assert value['configuration']==tag
            if value.get('complete') is not True:assert name==PREFIX+'current-index.json.gz'
            if 'completed_original_stage_source' in value:
                old=read(reference_source(work/'retained',source,value['completed_original_stage_source']))
                assert old['configuration']==old_tag(item,expanded,work/'retained') and old['complete'] is True
                assert value['previously_completed_exact_arithmetic_recomputed'] is False
    if 'core-receipt.json' not in rows:
        assert run['core_receipt_sha256'] is None and run['complete'] is False
        print('PARTIAL_IO_REVIEW='+json.dumps(dict(original_review,complete=False,missing_core_receipt=True)),flush=True)
        raise SystemExit(1)
    core=read(bound(out,rows['core-receipt.json']))
    assert run['core_receipt_sha256']==rows['core-receipt.json']['sha256']
    assert core['result']==RESULT and core['source_sha256']==item['core_sha256']
    if core.get('configuration') is not None:assert core['configuration']==tag
    if FINAL not in rows:
        assert run['complete'] is False
        raise SystemExit('No complete decision; every committed stage remains in this artifact.')
    final=read(bound(out,rows[FINAL]));assert final['configuration']==tag and final['result']==RESULT
    inventory=read(bound(out,final['stage_manifest']))
    assert inventory['complete'] is True and inventory['configuration']==tag
    for row in inventory['files']+inventory['current_checkpoints']:
        assert rows[row['file']]==plain(row);bound(out,row)
    audit=read(bound(out,final['source_audit']))
    assert audit['configuration']==tag and audit['complete'] is True
    assert audit['completed_dual_source']==completed_identity(source)
    assert audit['first_new_dual_digit']==source['source_dual_digits']+1
    assert audit['all_fourteen_original_unit_minors_and_denominators_preserved'] is True
    assert audit['candidate_q_anti_fixed_verified'] is True
    assert audit['old_RHS_Laurent_CM_inverse_and_completed_dual_digits_recomputed'] is False
    assert len(audit['representative_branch_pairs'])==7
    ids=[row[key] for row in audit['representative_branch_pairs'] for key in ('representative','paired')]
    assert sorted(ids)==list(range(14))
    target=read(bound(out,final['exact_target']))
    assert target['original_completed_target_source']=={'source_group':'FULL_DUAL',**plain(source['exact_target'])}
    assert target['original_target_and_denominator_recomputed'] is False
    assert target['candidate_anti_fixed_in_original_B_s_coordinates_verified'] is True
    assert final['source_CM_Dixon_digits']==518 and final['source_CM_Dixon_digits_used_as_dual_precision'] is False
    assert final['source_completed_full_dual_digits']==source['source_dual_digits']
    assert final['actual_new_dual_digits']>=source['source_dual_digits']
    assert final['newly_committed_dual_digits_in_this_source_chain']==final['actual_new_dual_digits']-source['source_dual_digits']
    assert final['rational_reconstruction_dimension']==17920 and final['original_full_rational_identity_dimension']==35840
    for flag in ('old_primal_inverse_Laurent_CM_or_function_Dixon_arithmetic_recomputed',
                 'old_completed_full_dual_digits_or_target_recomputed','old_primal_complete_function_recipe_produced',
                 'actual_eta_or_height_computed','original_expanded_x_and_derivative_accepted'):
        assert final[flag] is False
    if not final['complete']:
        assert not final['original_value_rowspace_zero_A1_proved'] and not final['original_candidate_y_strictly_rejected']
        assert final['decision_kind'] is None and not final['dual_linear_system_exactly_solved']
        print('PARTIAL_IO_REVIEW='+json.dumps(dict(original_review,complete=False,
            source_dual_digits=source['source_dual_digits'],actual_dual_digits=final['actual_new_dual_digits'],
            reason=final['reason']),sort_keys=True,separators=(',',':')),flush=True)
        raise SystemExit(1)
    assert run['complete'] is True and run['process_exit_code']==0 and core['complete'] is True
    assert bool(final['original_value_rowspace_zero_A1_proved'])!=bool(final['original_candidate_y_strictly_rejected'])
    kind=final['decision_kind']
    if kind=='original-full-exact-Theta-and-Delta':
        assert final['dual_linear_system_exactly_solved'] is True and final['strict_parity_rejection'] is None
        obstruction=read(bound(out,final['exact_value_obstruction']))
        assert obstruction['configuration']==tag and obstruction['complete'] is True
        exact=read(bound(out,obstruction['exact_transpose_certificate']))
        assert exact['all35840_rational_coordinates_verified'] is True
        assert exact['verified_L_coordinate_groups']==[1234,1186,140]
        delta=obstruction['Delta_original_L_coordinates'];assert len(delta)==14
        zero=all(value[0]=='0' for value in delta)
        assert zero==final['original_value_rowspace_zero_A1_proved']==obstruction['original_value_rowspace_zero_A1_proved']
        assert (not zero)==final['original_candidate_y_strictly_rejected']==obstruction['original_candidate_y_strictly_rejected']
    else:
        assert kind in ('original-complete-current','completed-seven-branch-correction')
        assert final['dual_linear_system_exactly_solved'] is False and final['exact_value_obstruction'] is None
        assert final['original_candidate_y_strictly_rejected'] is True and final['original_value_rowspace_zero_A1_proved'] is False
        decision=read(bound(out,final['strict_parity_rejection']))
        assert decision['configuration']==tag and decision['complete'] is True and decision['rejection_kind']==kind
        assert decision['original_candidate_y_strictly_rejected'] is True
        assert decision['ordinary_failed_RR_candidate_used_as_rejection'] is False
        assert decision['original_unit_square_operator_and_integral_target_certified'] is True
        assert decision['conditional_parity_derived_from_original_A1_and_full_row_uniqueness'] is True
        assert decision['dual_linear_system_exactly_solved'] is False
        assert decision['exact_target']==final['exact_target'] and decision['source_audit']==final['source_audit']
        if kind=='original-complete-current':
            assert decision['original_current']=={'source_group':'FULL_DUAL',**plain(source['current'])}
            assert decision['source_dual_digits']==source['source_dual_digits']
            assert decision['old_all35840_modular_equations_verified'] is True
            assert decision['old_equations_or_digits_recomputed'] is False
            position=decision['first_forbidden_nonzero_original_coordinate']
            assert len(position)==3 and 1<=position[0]<=128 and 0<=position[1]<280 and position[2]!='0'
            oldcurrent=read(reference_source(work/'retained',source,decision['original_current']))
            assert oldcurrent['chi_integer_coordinates'][position[0]-1][position[1]]==position[2]
            assert (position[0]%2==1 and position[1]>=140) or (position[0]%2==0 and position[1]<140)
        elif decision.get('completed_original_full_correction'):
            correction=read(reference_source(work/'retained',source,decision['completed_original_full_correction']))
            assert correction['all35840_prime_correction_coordinates_verified'] is True
            assert decision['source_full_correction_already_verifies_all_original_equations'] is True
            position=decision['first_forbidden_nonzero_original_coordinate']
            assert len(position)==3 and 1<=position[0]<=128 and 0<=position[1]<280 and position[2]!='0'
            assert str(correction['chi_prime_correction'][position[0]-1][position[1]])==position[2]
            assert (position[0]%2==1 and position[1]>=140) or (position[0]%2==0 and position[1]<140)
        else:
            candidate=read(bound(out,decision['completed_seven_branch_candidate']))
            assert candidate['configuration']==tag and candidate['complete'] is True
            assert candidate['original_seven_branch_solutions_verified'] is True
            assert candidate['necessary_half_coordinate_condition_verified'] is True
            assert candidate['all35840_prime_correction_coordinates_verified'] is False
            assert decision['full_original_Theta_completion_failed'] is True
            assert candidate['first_nonzero_original_residual']==decision['first_nonzero_original_residual']
            position=decision['first_nonzero_original_residual']
            assert len(position)==3 and 0<=position[0]<2560 and 0<=position[1]<14 and position[2]!='0'
            assert candidate['representative_branch_pairs']==audit['representative_branch_pairs']
            bound(out,decision['positive_residual'])
    assert final['exact_original_y_value_accepted']==final['original_value_rowspace_zero_A1_proved']
    print('COMPLETE_IO_REVIEW='+json.dumps(dict(original_review,completed=True,
        source_dual_digits=source['source_dual_digits'],actual_dual_digits=final['actual_new_dual_digits'],
        decision_kind=kind,dual_linear_system_exactly_solved=final['dual_linear_system_exactly_solved'],
        original_value_rowspace_zero_A1_proved=final['original_value_rowspace_zero_A1_proved'],
        original_candidate_y_strictly_rejected=final['original_candidate_y_strictly_rejected'],
        final=rows[FINAL],stage_manifest=final['stage_manifest'],seconds=final['seconds']),
        sort_keys=True,separators=(',',':')),flush=True)


def main():
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser()
    parser.add_argument('operation',choices=('prepare','compute','verify'))
    parser.add_argument('--request',type=Path,required=True)
    parser.add_argument('--work',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    request=read(args.request);assert request['schema']==1
    item=request['job'];guard(item,args.request)
    args.work.mkdir(parents=True,exist_ok=True);args.output.mkdir(parents=True,exist_ok=True)
    if args.operation=='prepare':prepare(item,args.request,args.work,args.output);return 0
    if args.operation=='compute':return compute(item,args.request,args.work,args.output)
    verify(item,args.work,args.output);return 0


if __name__=='__main__':sys.exit(main())
