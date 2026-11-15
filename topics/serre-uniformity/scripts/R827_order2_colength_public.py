#!/usr/bin/env python3
"""Read-only public IO for the original order-two colength sufficient certificate.

Only the separate core executes new mathematics.  The successful R835 source
transports completed columns and d0; no old derivative or determinant is rerun.
"""
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

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO/'topics/serre-uniformity'
REQUEST = TOPIC/'notes/R827-order2-colength-public-request.json'
RESULT = 'R827-original-order2-colength-certificate'
FINAL = 'p41-original-order2-colength-certificate.json'
MODE = 'order2_two_determinants_colength_395_and_original_infinity_minor'
PREFIX = 'R827-order2-'
SOURCE_RESULT = 'R827-original-global-modular-derivative-termination'
SOURCE_FINAL = 'p41-original-global-modular-derivative-termination-certificate.json'
MANIFEST = 'full-outputs-manifest.json'
REFERENCE = 'full-outputs-manifest-reference.json'
SOURCE_BUNDLE = 'R827-determinantal-completed-source.tar.gz'
SOURCE_INVENTORY = 'R827-determinantal-source-inventory.json'
PARENT_BUNDLE = 'R827-order2-retained-R835-source.tar.gz'
PARENT_INVENTORY = 'R827-order2-parent-source-inventory.json'
INPUT_RECEIPT = 'order2-retained-inputs-receipt.json'
OLD_DETERMINANT = 'R827-det-projection-000-exact-determinant-polynomial.json.gz'
OLD_CORE = '4f2dc1192d2f95f902f03c2b9f0e875af7b3e04df58b8ae5bbe86072fb5b35b3'
OLD_WRAPPER = '7715eeb902a576a2290cf318219aaa62d93d79737a7f1e4afaeb12234d93f0e6'
ORIGINAL_PROOF = '17e9c828e01e652b1a73281bf2249ae2b39133faae3cf22384a5fd6d6a3d4a71'
OLD_PROOF = '7e07f78eace749b130f0d1b7920f6c6a03c7f54a15b4e940749a69c060d89fbf'
RANGE_SHA = 'c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c'
PRIME,N,Q = 1000000753,272,2
EPS = [0]+[1]*144+[2]*127
BASE_KEYS = ('result','run_id','source_commit','core_sha256','manifest_sha256')
INFINITY = 'R827-sigma-infinity-order-0004-certificate.json.gz'
H64 = re.compile(r'[0-9a-f]{64}')
OLD = IO = None
STRATEGY = {'source_column_order': 'derivative_order=0..2, original_normal_basis_column=0..271', 'new_projection': 'G0+G1+G2; V=(I,I,I)^transpose', 'old_projection': 'det(G0) from the completed actual R835 source, never recomputed', 'ordered_integer_parameters': [1], 'block_projection_degree_bounds': [2428], 'determinant_nodes': 'all consecutive integers 0..2428; singular nodes retained', 'degree_formula': 'sum(9+eps)-398-20=2428', 'interpolation': 'exact forward differences and complete node multiplyback', 'success': 'exact gcd degree395 plus original sigma minor using only layers0and1', 'generic_inclusion': 'J2 subset I2, colength(I2)=415+epsilon, epsilon in {0,1}', 'length_transfer': 'finite proper cokernel over the original DVR; generic rank <= special length', 'old_column_Hermite_determinant_or_infinity_arithmetic_recomputed': False, 'budget_excluded_from_mathematical_identity': True}


def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda:f.read(4*1024*1024),b''):h.update(b)
    return h.hexdigest()

def read(path):
    path=Path(path)
    with (gzip.open if path.suffix=='.gz' else open)(path,'rt',encoding='utf-8') as f:return json.load(f)

def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+'.tmp')
    tmp.write_text(json.dumps(value,sort_keys=True,separators=(',',':'))+'\n')
    tmp.replace(path)

def fingerprint(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def safe(name):
    assert isinstance(name,str) and Path(name).name==name and name not in ('','.','..') and '\\' not in name

def plain(row):
    v={k:row[k] for k in ('file','bytes','sha256')};safe(v['file'])
    assert type(v['bytes']) is int and v['bytes']>=0 and H64.fullmatch(v['sha256'])
    return v

def spec(path):
    path=Path(path)
    return {'file':path.name,'bytes':path.stat().st_size,'sha256':sha(path)}

def bound(root,row):
    row=plain(row);path=Path(root)/row['file'];assert spec(path)==row;return path

def topic_path(value):
    rel=PurePosixPath(value);assert not rel.is_absolute() and '..' not in rel.parts
    path=(TOPIC/str(rel)).resolve();assert path.is_relative_to(TOPIC.resolve());return path

def identity(source):return {k:source[k] for k in BASE_KEYS}

def import_io(item):
    global OLD,IO
    path=S/item['source_io_framework']
    assert path.name=='R827_determinantal_Bezout_public.py'
    assert sha(path)==item['source_io_framework_sha256']==OLD_WRAPPER
    module=importlib.util.spec_from_file_location('R827_order2_frozen_original_IO',path)
    OLD=importlib.util.module_from_spec(module);module.loader.exec_module(OLD)
    OLD.import_io(item);IO=OLD.IO

def guard(item):
    assert os.environ.get('GITHUB_ACTIONS')=='true'
    assert os.environ.get('GITHUB_REPOSITORY')=='Rogerhu12/math-research-public'
    assert item['result']==RESULT and item['certification_mode']==MODE
    assert item['producer_inputs_pending'] is False and item['derivative_order']==2
    assert item['p']==41 and item['auxiliary_prime']==PRIME
    assert 0<item['budget_minutes']<=300
    assert sha(__file__)==item['wrapper_sha256']
    assert sha(S/item['core'])==item['core_sha256']
    assert sha(topic_path(item['proof']))==item['order2_proof_sha256']
    assert sha(topic_path(item['original_proof']))==item['R827_proof_sha256']==ORIGINAL_PROOF
    assert sha(REPO/'README.md')==item['readme_sha256']['root']
    assert sha(TOPIC/'README.md')==item['readme_sha256']['topic']
    assert item['completed_determinantal_source']['core_sha256']==OLD_CORE
    assert item['completed_determinantal_source']['expected_conclusion']=='success'
    assert item['source_io_framework_sha256']==OLD_WRAPPER
    assert item['io_helper_sha256']==RANGE_SHA
    import_io(item)

def manifest_files(source,root):
    root=Path(root)
    assert sha(root/MANIFEST)==source['manifest_sha256']
    assert (root/MANIFEST).stat().st_size==source['manifest_bytes']
    value=read(root/MANIFEST);reference=read(root/REFERENCE)
    assert value['result']==reference['result']==source['result']
    assert value['temporary_active_checkpoint_retention_days']==1
    assert value['reproducible_data_in_git_or_release'] is False
    rows={r['file']:plain(r) for r in value['files']}
    assert len(rows)==len(value['files'])==source['manifest_file_count']
    assert reference['manifest_file']==MANIFEST and reference['manifest_bytes']==source['manifest_bytes']
    assert reference['manifest_sha256']==source['manifest_sha256'] and reference['file_count']==len(rows)
    return rows

def parent_names(source):
    return sorted({MANIFEST,REFERENCE,'run-receipt.json','core-receipt.json','public-actions-input.json',
                   SOURCE_FINAL,OLD_DETERMINANT,source['stage_manifest']['file']})

def parent_review(item,root):
    root=Path(root);source=item['completed_determinantal_source'];rows=manifest_files(source,root)
    selected=[]
    for name in parent_names(source):
        entry=({'file':MANIFEST,'bytes':source['manifest_bytes'],'sha256':source['manifest_sha256']}
               if name==MANIFEST else plain(source['manifest_reference']) if name==REFERENCE else rows[name])
        bound(root,entry);selected.append(entry)
    run,core,initial=[read(root/n) for n in ('run-receipt.json','core-receipt.json','public-actions-input.json')]
    assert run['result']==core['result']==initial['result']==SOURCE_RESULT
    assert run['complete'] is True and core['complete'] is True and run['process_exit_code']==0 and run['error'] is None
    assert str(run['workflow_run_id'])==str(source['run_id'])
    assert run['source_commit']==initial['source_commit']==source['source_commit']
    assert run['core_receipt_sha256']==rows['core-receipt.json']['sha256']
    assert core['source_sha256']==initial['core_sha256']==initial['job']['core_sha256']==OLD_CORE
    assert initial['driver_sha256']==initial['job']['wrapper_sha256']==OLD_WRAPPER
    assert initial['proof_sha256']==initial['job']['determinantal_proof_sha256']==OLD_PROOF
    assert initial['original_proof_sha256']==ORIGINAL_PROOF
    assert initial['job']['source']==item['source']
    assert initial['job']['source_configuration_sha256']==item['source_configuration_sha256']
    assert initial['job']['source_inventory_sha256']==item['source_inventory_sha256']
    assert rows[SOURCE_BUNDLE]==plain(source['source_bundle'])
    assert initial['source_inventory']==plain(source['source_inventory'])
    final=read(bound(root,source['certificate']))
    assert rows[SOURCE_FINAL]==plain(source['certificate'])
    assert core['certificate_sha256']==source['certificate']['sha256']
    assert final['result']==SOURCE_RESULT and final['complete'] is True
    tag=final['configuration'];assert tag['source_sha256']==OLD_CORE
    assert tag['source_identity']==identity(item['source'])
    assert tag['source_configuration_sha256']==item['source_configuration_sha256']
    assert tag['source_inventory_sha256']==item['source_inventory_sha256']
    assert final['original_characteristic_zero_Iq_equals_C'] is True and final['safe_D_multiplicity_bound']==1
    assert final['actual_derivative_order']==4 and final['actual_completed_projection_count']==2
    assert final['stage_manifest']==plain(source['stage_manifest'])
    inventory=read(bound(root,source['stage_manifest']))
    assert inventory['configuration']==tag and inventory['complete'] is True
    stage_rows={r['file']:plain(r) for r in inventory['files']}
    assert final['source_determinant_polynomials'][0]==plain(source['old_determinant'])
    assert stage_rows[OLD_DETERMINANT]==rows[OLD_DETERMINANT]==plain(source['old_determinant'])
    d0=read(bound(root,source['old_determinant']))
    assert d0['configuration']==tag and d0['complete'] is True
    assert d0['projection_number']==0 and d0['integer_parameter']==0 and d0['prime']==PRIME
    assert d0['proven_determinant_degree_bound']==1340 and d0['actual_determinant_degree']==1320
    assert d0['all_degree_bound_plus_one_nodes_exactly_verified'] is True
    assert d0['exact_interpolant_is_the_entire_determinant_by_proven_degree_bound'] is True
    assert len(d0['determinant_coefficients_mod_prime'])==1321
    return selected,{'original_successful_determinantal_source':identity(source),
                     'original_I4_equals_C_and_reduced_D_source':True,
                     'original_d0':plain(source['old_determinant']),
                     'all_selected_parent_bytes_verified':True}

def pack_parent(root,out,rows):
    root=Path(root);out=Path(out)
    inventory={'result':RESULT,'files':rows}
    save(root/PARENT_INVENTORY,inventory);allrows=rows+[spec(root/PARENT_INVENTORY)]
    temp=out.with_name(out.name+'.tmp')
    with temp.open('wb') as raw:
        with gzip.GzipFile(fileobj=raw,mode='wb',mtime=0,compresslevel=2) as compressed:
            with tarfile.open(fileobj=compressed,mode='w|') as archive:
                for row in allrows:
                    path=bound(root,row);info=archive.gettarinfo(str(path),arcname=path.name)
                    info.uid=info.gid=0;info.uname=info.gname='';info.mtime=0
                    with path.open('rb') as f:archive.addfile(info,f)
    temp.replace(out)
    return spec(root/PARENT_INVENTORY)

def unpack_parent(path,root,inventory_spec):
    root=Path(root);root.mkdir(parents=True,exist_ok=True);records={}
    with tarfile.open(path,'r:gz') as archive:
        for member in archive:
            assert member.isfile() and not member.issym() and not member.islnk();safe(member.name)
            assert member.name not in records
            target=root/member.name;temp=target.with_name(target.name+'.tmp');h=hashlib.sha256();size=0
            with archive.extractfile(member) as f,temp.open('wb') as g:
                for block in iter(lambda:f.read(4*1024*1024),b''):g.write(block);h.update(block);size+=len(block)
            assert size==member.size;temp.replace(target)
            records[member.name]={'file':member.name,'bytes':size,'sha256':h.hexdigest()}
    assert records[PARENT_INVENTORY]==plain(inventory_spec)
    inv=read(root/PARENT_INVENTORY);assert inv['result']==RESULT
    expected={r['file']:plain(r) for r in inv['files']};expected[PARENT_INVENTORY]=plain(inventory_spec)
    assert records==expected
    return len(records)

def prepare_inputs(item,out,allow_download=True):
    out=Path(out);original=out.parent/'retained-original-R827';parent=out.parent/'retained-R835'
    original.mkdir(parents=True,exist_ok=True);parent.mkdir(parents=True,exist_ok=True)
    receipt_path=out/INPUT_RECEIPT
    if receipt_path.exists() and (out/SOURCE_BUNDLE).exists() and (out/PARENT_BUNDLE).exists():
        receipt=read(receipt_path)
        assert receipt['result']==RESULT and receipt['complete'] is True
        assert receipt['completed_determinantal_source']==item['completed_determinantal_source']
        bound(out,receipt['source_bundle']);bound(out,receipt['parent_bundle'])
        n=OLD.unpack_source(out/SOURCE_BUNDLE,original,receipt['source_inventory'],extract=True)
        m=unpack_parent(out/PARENT_BUNDLE,parent,receipt['parent_inventory'])
        review=OLD.source_review(item,original)
        _,parent_check=parent_review(item,parent)
        assert review==receipt['original_source_review'] and parent_check==receipt['parent_review']
        assert (n,m)==(receipt['source_bundle_members'],receipt['parent_bundle_members'])
        return original,parent,receipt
    assert allow_download,'Missing retained one-day source carriers.'
    source=item['completed_determinantal_source']
    archive=IO.Archive(source,out.parent/'download-completed-R835',whole=False)
    try:
        archive.extract_bound(MANIFEST,source['manifest_sha256'],parent/MANIFEST,source['manifest_bytes'])
        archive.extract_bound(REFERENCE,source['manifest_reference']['sha256'],parent/REFERENCE,source['manifest_reference']['bytes'])
        rows=manifest_files(source,parent)
        assert set(archive.by_name)==set(rows)|{MANIFEST,REFERENCE}
        for name,row in rows.items():
            assert len(archive.by_name[name])==1 and archive.by_name[name][0].file_size==row['bytes']
        names=parent_names(source)
        archive.extract_many([(n,rows[n]['sha256'],parent/n,rows[n]['bytes']) for n in names if n not in (MANIFEST,REFERENCE)])
        selected,parent_check=parent_review(item,parent)
        bundle=plain(source['source_bundle']);assert rows[SOURCE_BUNDLE]==bundle
        archive.extract_bound(SOURCE_BUNDLE,bundle['sha256'],out/SOURCE_BUNDLE,bundle['bytes'])
        n=OLD.unpack_source(out/SOURCE_BUNDLE,original,source['source_inventory'],extract=True)
        review=OLD.source_review(item,original)
        parent_inventory=pack_parent(parent,out/PARENT_BUNDLE,selected)
        m=unpack_parent(out/PARENT_BUNDLE,parent,parent_inventory)
        receipt={'result':RESULT,'complete':True,'completed_determinantal_source':source,
                 'source_bundle':spec(out/SOURCE_BUNDLE),'source_inventory':plain(source['source_inventory']),
                 'parent_bundle':spec(out/PARENT_BUNDLE),'parent_inventory':parent_inventory,
                 'source_bundle_members':n,'parent_bundle_members':m,
                 'original_source_review':review,'parent_review':parent_check,'range_transport':archive.receipt(),
                 'all_five_original_C_layers_retained_for_next_consumers':True,
                 'mathematical_input_layers':[0,1,2],
                 'upstream_large_math_carrier_not_redownloaded_or_reconstructed':True,
                 'all_new_math_only_in_separate_core':True}
        save(receipt_path,receipt)
        print('ORDER2_INPUT_REVIEW='+json.dumps({'source':identity(source),'original_C_layers_retained':5,
              'mathematical_C_columns':816,'source_bundle_members':n,'parent_bundle_members':m,
              'original_d0':source['old_determinant'],'all_original_selected_bytes_verified':True},sort_keys=True),flush=True)
        return original,parent,receipt
    finally:archive.close()

def expected_tag(item,original):
    inventory=read(Path(original)/SOURCE_INVENTORY)
    rows={r['file']:plain(r) for r in inventory['selected_files']}
    return {'result':RESULT,'source_sha256':item['core_sha256'],'python_flint':'0.9.0','p':41,
            'auxiliary_prime':PRIME,'derivative_order':2,'certification_mode':MODE,
            'normal_basis_rank':N,'normal_basis_degrees':EPS,'source_column_count':816,
            'order2_proof_sha256':item['order2_proof_sha256'],'R827_proof_sha256':ORIGINAL_PROOF,
            'source_identity':identity(item['source']),'source_configuration_sha256':item['source_configuration_sha256'],
            'source_inventory_sha256':item['source_inventory_sha256'],
            'source_sigma_infinity_certificate':rows[INFINITY],
            'completed_determinantal_source':item['completed_determinantal_source'],'strategy':STRATEGY}

def stable_job(item):
    return {k:v for k,v in item.items() if k not in ('resume','budget_minutes','readme_sha256','rules_last_read_commit')}

def restore(item,out):
    source=item.get('resume')
    if not source:return
    prior=out.parent/'resume-original';prior.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(source,out.parent/'download-order2-resume',whole=False)
    try:
        archive.extract_bound(MANIFEST,source['manifest_sha256'],prior/MANIFEST,source['manifest_bytes'])
        archive.extract_bound(REFERENCE,source['manifest_reference']['sha256'],prior/REFERENCE,source['manifest_reference']['bytes'])
        rows=manifest_files(source,prior)
        names=['run-receipt.json','public-actions-input.json']
        if 'core-receipt.json' in rows:names.append('core-receipt.json')
        archive.extract_many([(n,rows[n]['sha256'],prior/n,rows[n]['bytes']) for n in names])
        run,initial=[read(prior/n) for n in names[:2]]
        assert run['result']==initial['result']==RESULT
        assert str(run['workflow_run_id'])==str(source['run_id']) and run['source_commit']==source['source_commit']==initial['source_commit']
        assert initial['core_sha256']==item['core_sha256'] and initial['driver_sha256']==item['wrapper_sha256']
        assert stable_job(initial['job'])==stable_job(item)
        if 'core-receipt.json' in rows:
            assert run['core_receipt_sha256']==rows['core-receipt.json']['sha256']
            core=read(prior/'core-receipt.json');assert core['source_sha256']==item['core_sha256'] and core['result']==RESULT
        else:assert run['core_receipt_sha256'] is None and run['complete'] is False
        for n in (SOURCE_BUNDLE,PARENT_BUNDLE,INPUT_RECEIPT):
            archive.extract_bound(n,rows[n]['sha256'],out/n,rows[n]['bytes'])
        original,parent,_=prepare_inputs(item,out,allow_download=False);tag=expected_tag(item,original)
        stages=[n for n in rows if n.startswith(PREFIX) and n.endswith('.json.gz')]
        archive.extract_many([(n,rows[n]['sha256'],out/n,rows[n]['bytes']) for n in stages])
        for n in stages:
            value=read(out/n)
            assert value['result']==RESULT and value['configuration']==tag and value['complete'] is True
        save(out/'resume-inheritance-receipt.json',{'result':RESULT,'complete':True,'source_resume':source,
             'restored_complete_stages':[rows[n] for n in stages],
             'previous_final_not_required_as_current_inventory_snapshot':True,
             'range_transport':archive.receipt(),'old_node_or_gcd_arithmetic_recomputed':False})
    finally:archive.close()

def output_manifest(out):
    rows=[dict(spec(p),included_in_git=False) for p in sorted(out.iterdir()) if p.is_file()
          and p.name not in (MANIFEST,REFERENCE) and not p.name.endswith(('.tmp','.download'))]
    save(out/MANIFEST,{'result':RESULT,'files':rows,'temporary_active_checkpoint_retention_days':1,'reproducible_data_in_git_or_release':False})
    save(out/REFERENCE,{'result':RESULT,'manifest_file':MANIFEST,'manifest_sha256':sha(out/MANIFEST),
          'manifest_bytes':(out/MANIFEST).stat().st_size,'file_count':len(rows)})

def compute(item,out):
    out.mkdir(parents=True,exist_ok=True);process=None;code=1;error=None;outer=False
    try:
        restore(item,out);original,parent,receipt=prepare_inputs(item,out)
        save(out/'public-actions-expanded-job.json',item)
        save(out/'public-actions-input.json',{'result':RESULT,'source_repository':'Rogerhu12/math-research-public',
             'source_commit':os.environ['GITHUB_SHA'],'job':item,'request_sha256':sha(REQUEST),
             'driver_sha256':sha(__file__),'core_sha256':item['core_sha256'],
             'order2_proof_sha256':item['order2_proof_sha256'],'original_proof_sha256':ORIGINAL_PROOF,
             'io_framework_sha256':OLD_WRAPPER,'io_helper_sha256':RANGE_SHA,
             'workflow_sha256':sha(REPO/item['workflow']),'root_readme_sha256':sha(REPO/'README.md'),
             'topic_readme_sha256':sha(TOPIC/'README.md'),'source_inventory':receipt['source_inventory'],
             'prepared_at_utc':dt.datetime.now(dt.timezone.utc).isoformat()})
        command=[sys.executable,str(S/item['core']),'--config',str(out/'public-actions-expanded-job.json'),
             '--proof',str(topic_path(item['proof'])),'--original-proof',str(topic_path(item['original_proof'])),
             '--retained',str(original),'--determinantal-source',str(parent),'--output',str(out),
             '--budget-minutes',str(item['budget_minutes'])]
        with (out/'public-actions-run.log').open('w') as log:
            process=subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
            try:code=process.wait(timeout=item['budget_minutes']*60+900)
            except subprocess.TimeoutExpired:
                outer=True;os.killpg(process.pid,signal.SIGTERM)
                try:process.wait(timeout=20)
                except subprocess.TimeoutExpired:os.killpg(process.pid,signal.SIGKILL);process.wait()
                code=124
    except BaseException as caught:
        error=type(caught).__name__+': '+str(caught)
        if process is not None and process.poll() is None:
            os.killpg(process.pid,signal.SIGTERM)
            try:process.wait(timeout=20)
            except subprocess.TimeoutExpired:os.killpg(process.pid,signal.SIGKILL);process.wait()
        code=1
    finally:
        core_path=out/'core-receipt.json';core=read(core_path) if core_path.exists() else None
        complete=code==0 and core is not None and core.get('complete') is True and (out/FINAL).is_file()
        receipt={'result':RESULT,'complete':complete,'process_exit_code':code,'error':error,'outer_timeout':outer,
                 'core_receipt_sha256':sha(core_path) if core_path.exists() else None,
                 'source_commit':os.environ.get('GITHUB_SHA'),'workflow_run_id':os.environ.get('GITHUB_RUN_ID'),
                 'workflow_attempt':os.environ.get('GITHUB_RUN_ATTEMPT'),'execution_environment':'public-repository-github-actions',
                 'finished_at_utc':dt.datetime.now(dt.timezone.utc).isoformat()}
        save(out/'run-receipt.json',receipt);output_manifest(out)
        print('ORDER2_RUN_RECEIPT='+json.dumps(receipt,sort_keys=True),flush=True)
    return code

def verify(item,out):
    reference=read(out/REFERENCE)
    pseudo={'result':RESULT,'manifest_sha256':reference['manifest_sha256'],'manifest_bytes':reference['manifest_bytes'],
            'manifest_file_count':reference['file_count']}
    rows=manifest_files(pseudo,out)
    actual={p.name for p in out.iterdir() if p.is_file() and p.name not in (MANIFEST,REFERENCE) and not p.name.endswith(('.tmp','.download'))}
    assert actual==set(rows)
    for entry in rows.values():bound(out,entry)
    original,parent,receipt=prepare_inputs(item,out,allow_download=False);tag=expected_tag(item,original)
    initial=read(out/'public-actions-input.json')
    assert initial['job']==item and initial['result']==RESULT
    assert initial['driver_sha256']==item['wrapper_sha256'] and initial['core_sha256']==item['core_sha256']
    assert initial['root_readme_sha256']==item['readme_sha256']['root'] and initial['topic_readme_sha256']==item['readme_sha256']['topic']
    stages={}
    for name,entry in rows.items():
        if name.startswith(PREFIX) and name.endswith('.json.gz'):
            value=read(out/name)
            assert value['result']==RESULT and value['configuration']==tag and value['complete'] is True
            stages[name]=entry
    def stage(entry):
        entry=plain(entry);assert stages[entry['file']]==entry;return read(bound(out,entry))
    run=read(out/'run-receipt.json');assert run['result']==RESULT and run['source_commit']==initial['source_commit']
    core=read(out/'core-receipt.json') if 'core-receipt.json' in rows else None
    if core is None:assert run['complete'] is False and run['core_receipt_sha256'] is None
    else:
        assert core['result']==RESULT and core['source_sha256']==item['core_sha256'] and core['certification_mode']==MODE
        assert run['core_receipt_sha256']==rows['core-receipt.json']['sha256']
    if not run['complete']:
        assert run['process_exit_code']!=0
        print('ORDER2_PARTIAL_IO_REVIEW='+json.dumps({'complete_stages':len(stages),'manifest_files':len(rows),
              'core_receipt_present':core is not None,'all_output_bytes_verified':True,'mathematical_completion_claimed':False}),flush=True)
        return 1
    assert run['process_exit_code']==0 and run['error'] is None and core is not None and core['complete'] is True
    final=read(out/FINAL);assert final['result']==RESULT and final['complete'] is True and final['configuration']==tag
    assert core['certificate_sha256']==rows[FINAL]['sha256'] and final['certification_mode']==MODE
    assert final['actual_derivative_order']==core['actual_derivative_order']==2
    assert final['completed_scope']=='one_new_order2_determinant_and_exact_colength_bound'
    inventory=stage(final['stage_manifest']);listed={r['file']:plain(r) for r in inventory['files']}
    complete_names={n for n in stages if not n.startswith(PREFIX+'stage-manifest-') and not n.endswith('-current.json.gz')}
    assert set(listed)==complete_names and all(listed[n]==stages[n] for n in complete_names)
    source=stage(final['source_completed_column_interface']);assert source['original_column_count']==816
    assert source['derivative_order']==2 and source['same_original_field_branch_free_column_and_C_preserved'] is True
    assert source['original_infinity_minor_already_uses_only_layers0and1'] is True
    inv=read(original/SOURCE_INVENTORY);oldfiles={r['file']:plain(r) for r in inv['selected_files']}
    assert source['source_original_tau_layer_indexes']==[oldfiles[OLD.layer_name(k)] for k in range(3)]
    assert source['source_column_inventory_sha256']==fingerprint([oldfiles[OLD.column_name(k,c)] for k in range(3) for c in range(N)])
    assert final['sigma_infinity_certificate']==oldfiles[INFINITY] and final['sigma_infinity_source_group']=='original_R827'
    infinity=read(original/INFINITY)
    assert infinity['actual_selected_pivot_columns']==list(range(252))+[272]+list(range(345,364))
    assert infinity['actual_full_minor_determinant_mod_prime']==695832206
    d1=stage(final['new_determinant_polynomial'])
    assert d1['prime']==PRIME and d1['projection_number']==0 and d1['integer_parameter']==1
    assert d1['proven_determinant_degree_bound']==2428
    values=d1['determinant_coefficients_mod_prime']
    assert len(values)<=2429 and all(type(v) is int and 0<=v<PRIME for v in values)
    assert not values or values[-1]!=0
    assert d1['actual_determinant_degree']==len(values)-1
    for k in ('all_degree_bound_plus_one_nodes_exactly_verified','exact_interpolant_is_the_entire_determinant_by_proven_degree_bound','no_adjugate_coefficients_computed'):assert d1[k] is True
    matrix=stage(d1['source_projection_matrix'])
    assert matrix['projection_number']==0 and matrix['integer_parameter']==1
    assert matrix['source_layer_scalar_coefficients']==[1,1,1]
    assert matrix['proven_determinant_degree_bound']==2428
    assert matrix['source_homogeneous_column_weights']==[9+e for e in EPS]
    assert matrix['original_normal_weight_sum']==398 and matrix['source_C_determinant_degree']==20
    assert matrix['polynomial_coefficient_count']==len(matrix['coefficient_blocks'])==12
    for degree,entry in enumerate(matrix['coefficient_blocks']):
        block=stage(entry);assert block['coefficient_exponent']==degree
        assert block['prime']==PRIME and block['integer_parameter']==1 and block['projection_number']==0
        assert block['source_completed_columns']==final['source_completed_column_interface']
        assert block['source_original_column_inventory_sha256']==source['source_column_inventory_sha256']
        assert block['old_source_columns_recomputed'] is False and block['only_new_constant_projection_linear_combination_performed'] is True
        a=block['coefficient_matrix_mod_prime'];assert len(a)==N and all(len(r)==N for r in a)
        assert all(type(v) is int and 0<=v<PRIME for r in a for v in r)
    nodes=stage(d1['source_complete_nodes'])
    assert nodes['node_count']==len(nodes['node_records'])==2429
    assert nodes['points_are_exactly_consecutive_zero_through_bound'] is True
    assert nodes['source_projection_matrix']==d1['source_projection_matrix']
    for point,entry in enumerate(nodes['node_records']):
        node=stage(entry)
        assert node['prime']==PRIME and node['point']==point and node['integer_parameter']==1 and node['projection_number']==0
        assert node['source_projection_matrix']==d1['source_projection_matrix']
        assert node['proven_determinant_degree_bound']==2428 and node['matrix_rows']==node['matrix_columns']==N
        assert type(node['determinant_mod_prime']) is int and 0<=node['determinant_mod_prime']<PRIME
        assert node['actual_exact_finite_field_determinant_computed'] is True
    oldref=dict(item['completed_determinantal_source']['old_determinant'],source_group='completed_R835')
    assert final['old_determinant_source']==oldref
    length=stage(final['colength_certificate'])
    assert length['source_determinant_polynomials']==[oldref,final['new_determinant_polynomial']]
    assert length['complete_polynomial_Bezout_multiplyback_verified'] is True
    gcd=length['monic_gcd_coefficients_mod_prime'];degree=len(gcd)-1
    assert gcd and gcd[-1]==1 and 395<=degree<=1320
    assert len(length['Bezout_coefficients_mod_prime'])==2
    for p in [gcd]+length['Bezout_coefficients_mod_prime']:
        assert isinstance(p,list) and all(type(v) is int and 0<=v<PRIME for v in p)
        assert not p or p[-1]!=0
    assert degree==length['actual_monic_gcd_degree']==final['actual_monic_gcd_degree']==core['actual_monic_gcd_degree']
    success=degree==395
    assert length['complete_original_I2_certified'] is success
    assert final['original_characteristic_zero_J2_equals_I2'] is core['original_characteristic_zero_J2_equals_I2'] is success
    assert final['actual_P0_multiplicity_in_D']==length['actual_P0_multiplicity_in_D']==(0 if success else None)
    assert final['actual_original_I2_colength']==(415 if success else None)
    assert final['special_global_cokernel_length_upper_bound']==length['special_global_cokernel_length_upper_bound']==20+degree
    assert length['proper_finite_DVR_module_length_comparison_applied'] is success
    assert length['generic_original_I2_colength_lower_bound']==415
    for k in ('original_infinity_minor_already_uses_only_layers0and1','whole_sigma_infinity_fiber_surjective','exact_implicit_source_defined_by_original_unit_chart'):assert final[k] is True
    for k in ('actual_short_RR_coordinates_computed','actual_D_eta_or_height_computed','old_columns_derivatives_C_divisions_Hermite_d0_or_infinity_arithmetic_recomputed'):assert final[k] is False
    print('ORDER2_COMPLETE_IO_REVIEW='+json.dumps({'result':RESULT,'actual_new_node_count':2429,
          'actual_new_determinant_degree':d1['actual_determinant_degree'],'old_d0_degree':1320,
          'actual_gcd_degree':degree,'original_J2_equals_I2':success,'epsilon':0 if success else None,
          'manifest_files':len(rows),'complete_stages':len(stages),'certificate':rows[FINAL],
          'stage_manifest':final['stage_manifest'],'source_bundle':rows[SOURCE_BUNDLE],
          'parent_bundle':rows[PARENT_BUNDLE],'all_output_and_selected_source_bytes_verified':True,
          'seconds':final['seconds']},sort_keys=True),flush=True)
    return 0

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True);parser.add_argument('--verify',action='store_true')
    args=parser.parse_args();item=read(REQUEST);guard(item)
    return verify(item,args.output) if args.verify else compute(item,args.output)

if __name__=='__main__':raise SystemExit(main())
