#!/usr/bin/env python3
"""Standard-library source/carrier runner for original global polar DAGs."""
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

S=Path(__file__).resolve().parent
REPO=S.parents[2]
TOPIC=REPO/'topics/serre-uniformity'
REQUEST=TOPIC/'notes/R839-global-polar-DAG-public-request.json'
RESULT='R839-original-global-addition-polar-ideal-DAGs'
FINAL='p41-original-global-addition-polar-ideal-DAG-certificate.json'
PREFIX='R839-global-polar-'
MANIFEST='full-outputs-manifest.json'
REFERENCE='full-outputs-manifest-reference.json'
MATH_INVENTORY=PREFIX+'stage-manifest.json.gz'
INVENTORY=PREFIX+'original-source-inventory.json'
BUNDLE=PREFIX+'retained-original-inputs.tar.gz'
INPUT_RECEIPT=PREFIX+'retained-inputs-receipt.json'
HELPER='R824_public_original_global_polar_generators.py'
HELPER_SHA='c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c'
LABELS=['R787','R781','R786','R806','R809','R840','R845','R791']
BASE_KEYS=['result','run_id','source_commit','core_sha256','manifest_sha256','configuration_sha256']
META=[MANIFEST,'run-receipt.json','core-receipt.json','public-actions-input.json']
EPS=[0]+[1]*144+[2]*127
SCOPE={
    'p':41,'original_map_index':4,'original_map_degree':'1206',
    'canonical_free_column':1186,'original_unit_chart_shape':[2420,2420],
    'original_relation_condition_shape':[129,20,14],
    'normal_basis_rank':272,'normal_basis_degrees':EPS,
    'original_power5_dimension':1234,'S5_short_shape':[1380,1234],
    'original_Galois_order_over_K':7,'original_addition_exponents':[1,2,3,4,5],
    'global_base_pole_generator_count':8,'projective_minor_functions_per_map':3,
    'derivative_mode':'one_original_global_dz_y_and_Galois_conjugates',
    'derivative_backend':'source_bound_characteristic_polynomial_and_on_demand_cyclic_solve',
    'ideal_convention':'I_E=O(-E) embedded in the original function field',
    'old_numeric_arithmetic_recomputed':False,
    'no_modular_vector_used_as_characteristic_zero_coefficients':True,
    'no_CM_response_used_as_global_function':True,
    'no_arbitrary_cube_root_or_unknown_elliptic_division':True,
    'true_Galois_norm_preserves_all_original_field_constants':True,
    'output_representation':'finite_exact_source_bound_expression_DAG',
    'budget_and_absolute_directories_excluded_from_mathematical_identity':True,
}
TRUE_FLAGS=['global_y_exact_unit_expression_defined',
    'five_original_addition_pole_ideals_as_fractional_DAGs_certified',
    'original_eta_Picard_input_DAGs_defined','original_comparison_function_DAGs_defined']
FALSE_FLAGS=['expanded_global_function_coordinates_computed',
    'normal_polynomial_ideal_lattices_materialized','Jacobian_standard_representatives_computed',
    'original_rigidification_and_height_computed','original_eta_classes_proved_zero']
H64=re.compile(r'[0-9a-f]{64}')
IO=None


def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda:stream.read(4*1024*1024),b''):h.update(block)
    return h.hexdigest()


def read(path):
    path=Path(path)
    with (gzip.open if path.suffix=='.gz' else open)(path,'rt',encoding='utf-8') as stream:
        return json.load(stream)


def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_name(path.name+'.tmp')
    temporary.write_text(json.dumps(value,sort_keys=True,separators=(',',':'))+'\n',encoding='utf-8')
    temporary.replace(path)


def fingerprint(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def safe_name(name):
    assert isinstance(name,str) and Path(name).name==name and name not in ('.','..') and '\\' not in name
    return name


def plain(row):
    value={key:row[key] for key in ('file','bytes','sha256')};safe_name(value['file'])
    assert isinstance(value['bytes'],int) and value['bytes']>=0 and H64.fullmatch(value['sha256'])
    return value


def file_spec(path):
    path=Path(path)
    return {'file':path.name,'bytes':path.stat().st_size,'sha256':sha(path)}


def bound(folder,row):
    row=plain(row);path=Path(folder)/row['file'];assert file_spec(path)==row
    return path


def identity(item):
    return {key:item[key] for key in BASE_KEYS}


def same_origin(a,b):
    assert all(str(a[k])==str(b[k]) for k in BASE_KEYS[:-1])


def topic_path(name):
    path=PurePosixPath(name);assert not path.is_absolute() and '..' not in path.parts
    answer=(TOPIC/str(path)).resolve();assert answer.is_relative_to(TOPIC.resolve())
    return answer


def load_helper(item,helper_dir=None):
    global IO
    path=(S if helper_dir is None else Path(helper_dir))/HELPER
    assert item['io_helper_sha256']==HELPER_SHA and sha(path)==HELPER_SHA
    spec=importlib.util.spec_from_file_location('global_polar_stdlib_Range_IO',path)
    IO=importlib.util.module_from_spec(spec);spec.loader.exec_module(IO)


def guard(item,path):
    assert os.environ.get('GITHUB_ACTIONS')=='true'
    assert os.environ.get('GITHUB_REPOSITORY')=='Rogerhu12/math-research-public'
    assert path.resolve()==REQUEST.resolve()
    assert item['result']==RESULT and item['p']==41 and item['producer_inputs_pending'] is False
    assert item['core']=='R839_original_global_polar_DAG.py'
    assert item['wrapper']=='R839_global_polar_DAG_public.py'
    assert sha(S/item['core'])==item['core_sha256'] and sha(__file__)==item['wrapper_sha256']
    assert 0<item['budget_minutes']<=300
    for key in ('proof','method'):assert sha(topic_path(item[key]))==item[key+'_sha256']
    assert sha(REPO/'README.md')==item['readme_sha256']['root']
    assert sha(TOPIC/'README.md')==item['readme_sha256']['topic']
    assert set(item['sources'])==set(LABELS)
    for label,source in item['sources'].items():
        for key in ('core_sha256','manifest_sha256','configuration_sha256','selected_files_sha256'):
            assert H64.fullmatch(source[key])
        assert source['selected_file_count']>=4
        if label=='R781':
            assert source['transport']=='from_verified_R787_original_carrier'
            assert source['selected_file_count']==134
        else:
            assert source['artifact_id']>0 and source['archive_bytes']>0 and H64.fullmatch(source['archive_sha256'])
    load_helper(item)


def starting_names(label,source):
    names=set(META if label!='R781' else (MANIFEST,'run-receipt.json'))
    if source.get('certificate_name'):names.add(safe_name(source['certificate_name']))
    if source.get('configuration_stage'):names.add(safe_name(source['configuration_stage']))
    fixed={
        'R787':['R787-prime-1000000753-'+x+'.json.gz' for x in ('chart','rational-blocks','selection')]+
               ['R787-real-power5-row-'+str(i).zfill(4)+'.json.gz' for i in range(1234)],
        'R781':['R781-original-real-field-input.json.gz']+
               ['R781-inverse-free-Laurent-'+str(i).zfill(3)+'.json.gz' for i in range(130)],
        'R786':['R786-exact-power5-basis-index.json.gz'],
        'R806':['R806-original-input-and-coordinate-chart.json.gz',
                'R806-accepted-primitive-candidate.json.gz','R806-candidate-0000000000-definition.json.gz'],
        'R809':['R809-S5-basis-index.json.gz'],'R840':[],'R845':[],
        'R791':['R791-original-Hom-Galois-matrices.json.gz','R791-original-real-descent-and-eta-basis-inputs.json.gz'],
    }
    names.update(fixed[label]);return names


def extend_names(label,source,folder,names):
    names=set(names);folder=Path(folder);certname=source.get('certificate_name')
    cert=read(folder/certname) if certname and (folder/certname).exists() else None
    def add(entry):
        names.add(plain(entry)['file'])
    if label=='R806' and cert:
        for key in ('polynomial_multiplier','coordinate_chart','accepted_candidate','stage_manifest'):add(cert[key])
        for entry in cert['exact_coordinate_groups']:add(entry)
        path=folder/cert['polynomial_multiplier']['file']
        if path.exists():add(read(path)['actual_cyclic_witness'])
    if label=='R809' and cert:
        for key in ('S5_basis_index','minor_stage','stage_manifest'):add(cert[key])
        for j in range(6):
            entry=cert['normal_vectors']['C'+str(j)];add(entry);path=folder/entry['file']
            if path.exists():
                for group in read(path)['coordinate_groups']:add(group)
        path=folder/cert['S5_basis_index']['file']
        if path.exists():
            for row in read(path)['basis_rows']:add(row['source'])
    if label=='R840' and cert:
        for key in ('implicit_expression','source_audit','stage_manifest'):add(cert[key])
    if label=='R845' and cert:
        for key in ('pole_ideal_DAG','source_audit','stage_manifest'):add(cert[key])
    return names


def source_names(label,source,folder):
    names=starting_names(label,source)
    for _ in range(6):
        larger=extend_names(label,source,folder,names)
        if larger==names:return sorted(names)
        names=larger
    raise AssertionError('Original source closure did not stabilize')


def review_source(label,source,folder):
    folder=Path(folder)
    assert file_spec(folder/MANIFEST)=={'file':MANIFEST,'bytes':source['manifest_bytes'],'sha256':source['manifest_sha256']}
    manifest=read(folder/MANIFEST);assert manifest['result']==source['result']
    entries={row['file']:plain(row) for row in manifest['files']}
    assert len(entries)==len(manifest['files'])==source['manifest_file_count']
    entries[MANIFEST]=file_spec(folder/MANIFEST)
    selected={name:entries[name] for name in source_names(label,source,folder)}
    assert len(selected)==source['selected_file_count']
    assert fingerprint([selected[name] for name in sorted(selected)])==source['selected_files_sha256']
    for row in selected.values():bound(folder,row)
    run=read(folder/'run-receipt.json')
    assert run['result']==source['result'] and str(run['workflow_run_id'])==str(source['run_id'])
    assert run['source_commit']==source['source_commit']
    assert run['process_exit_code'] in source['accepted_process_exit_codes']
    certname=source.get('certificate_name');cert=read(folder/certname) if certname else None
    tag=cert['configuration'] if cert else read(folder/source['configuration_stage'])['configuration']
    assert tag['result']==source['result'] and tag['source_sha256']==source['core_sha256']
    assert fingerprint(tag)==source['configuration_sha256']
    if label!='R781':
        core=read(folder/'core-receipt.json');initial=read(folder/'public-actions-input.json')
        assert core['result']==initial['result']==source['result']
        assert initial['source_commit']==source['source_commit']
        assert initial['source_repository']=='Rogerhu12/math-research-public'
        assert core['source_sha256']==source['core_sha256']
        if label!='R791':assert initial['core_sha256']==source['core_sha256']
        assert initial['job']['core_sha256']==source['core_sha256']
        assert initial['wrapper_sha256' if label=='R840' else 'driver_sha256']==source['wrapper_sha256']
        if label!='R791':assert run['core_receipt_sha256']==selected['core-receipt.json']['sha256']
        if source['expected_conclusion']=='success':
            assert run['process_exit_code']==0 and run['complete'] is True and core['complete'] is True
            if 'certificate_sha256' in core:assert core['certificate_sha256']==selected[certname]['sha256']
        else:
            assert label=='R787' and source['expected_conclusion']=='failure'
            assert run['complete'] is False and core['complete'] is False and run['process_exit_code']!=0
    else:
        assert run['process_exit_code']==0 and run['complete'] is True
        assert source['transport']=='from_verified_R787_original_carrier'
    if cert:
        assert cert['complete'] is True and cert['result']==source['result']
    for name in selected:
        if name.endswith('.json.gz'):
            stage=read(folder/name)
            assert stage['complete'] is True and stage['configuration']==tag
            if 'result' in stage:assert stage['result']==source['result']
    return {**identity(source),'certificate_name':certname,
        'configuration_stage':source.get('configuration_stage'),
        'selected_file_count':len(selected),'selected_files_sha256':source['selected_files_sha256'],'files':selected}


def review_all(item,retained):
    retained=Path(retained)
    reviewed={label:review_source(label,item['sources'][label],retained/label) for label in LABELS}
    r787=read(retained/'R787/R787-prime-1000000753-chart.json.gz')['configuration']
    for child in ('R781','R786'):same_origin(r787['retained_artifacts'][child],reviewed[child])
    assert sum(x['selected_file_count'] for x in reviewed.values())==item['selected_original_file_count']
    assert fingerprint(reviewed)==item['expanded_sources_sha256']
    return reviewed


def fetch_direct(label,source,retained):
    folder=Path(retained)/label;folder.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(source,Path(retained).parent/('download-global-source-'+label),whole=False)
    try:
        archive.extract_bound(MANIFEST,source['manifest_sha256'],folder/MANIFEST,source['manifest_bytes'])
        manifest=read(folder/MANIFEST);assert manifest['result']==source['result']
        entries={row['file']:plain(row) for row in manifest['files']}
        assert len(entries)==len(manifest['files'])==source['manifest_file_count']
        assert set(archive.by_name)==set(entries)|{MANIFEST,REFERENCE}
        for name,row in entries.items():
            assert len(archive.by_name[name])==1 and archive.by_name[name][0].file_size==row['bytes']
        names=starting_names(label,source)
        for _ in range(6):
            need=[]
            for name in sorted(names):
                if name==MANIFEST:continue
                row=entries[name];path=folder/name
                if path.exists():bound(folder,row)
                else:need.append((name,row['sha256'],path,row['bytes']))
            archive.extract_many(need)
            larger=extend_names(label,source,folder,names)
            if larger==names:break
            names=larger
        else:raise AssertionError('Source selection did not close')
        review_source(label,source,folder)
        return archive.receipt()
    finally:archive.close()


def fetch_R781_from_original_carrier(item,retained):
    retained=Path(retained);source=item['sources']['R787'];child=item['sources']['R781']
    tag=read(retained/'R787/R787-prime-1000000753-chart.json.gz')['configuration']
    same_origin(tag['retained_artifacts']['R781'],child)
    original=read(retained/'R787'/MANIFEST)
    inventory={x['file']:plain(x) for x in original['files']}
    bundle=plain(child['source_carrier']);assert inventory[bundle['file']]==bundle
    temporary_dir=retained.parent/'original-carrier-R787';temporary_dir.mkdir(parents=True,exist_ok=True)
    target=temporary_dir/bundle['file']
    archive=IO.Archive(source,temporary_dir/'transport',whole=False)
    try:
        archive.extract_bound(bundle['file'],bundle['sha256'],target,bundle['bytes'])
        transport=archive.receipt()
    finally:archive.close()
    observed={'R781':{},'R786':{}}
    manifest_bytes={};folder=retained/'R781';folder.mkdir(parents=True,exist_ok=True)
    with tarfile.open(target,'r|gz') as tar:
        for member in tar:
            if member.isdir():continue
            path=PurePosixPath(member.name)
            assert member.isfile() and not path.is_absolute() and '..' not in path.parts and len(path.parts)==2
            group,name=path.parts;safe_name(name)
            assert group in observed and name not in observed[group]
            destination=folder/name if group=='R781' else None
            temp=destination.with_name(name+'.download') if destination else None
            stream=tar.extractfile(member);digest=hashlib.sha256();count=0;chunks=[]
            sink=temp.open('wb') if temp else None
            try:
                for block in iter(lambda:stream.read(4*1024*1024),b''):
                    digest.update(block);count+=len(block)
                    if sink:sink.write(block)
                    if name==MANIFEST:chunks.append(block)
            finally:
                if sink:sink.close()
            assert count==member.size
            row={'file':name,'bytes':count,'sha256':digest.hexdigest()};observed[group][name]=row
            if name==MANIFEST:manifest_bytes[group]=b''.join(chunks)
            if temp:
                if destination.exists():bound(folder,row);temp.unlink()
                else:temp.replace(destination)
    assert [len(observed[x]) for x in ('R781','R786')]==[134,1238]
    for group,rows in observed.items():
        assert hashlib.sha256(manifest_bytes[group]).hexdigest()==tag['retained_artifacts'][group]['manifest_sha256']
        manifest=json.loads(manifest_bytes[group]);entries={x['file']:plain(x) for x in manifest['files']}
        for name,row in rows.items():
            if name!=MANIFEST:assert entries[name]==row
    review_source('R781',child,folder)
    return {'original_carrier':bundle,'original_parent_source':identity(source),
        'all_original_1372_members_verified':True,'all_original_member_count':1372,
        'selected_child_member_count':134,'range_transport':transport}


def fetch_sources(item,retained):
    transport={};retained=Path(retained);retained.mkdir(parents=True,exist_ok=True)
    for label in LABELS:
        if label=='R781':transport[label]=fetch_R781_from_original_carrier(item,retained)
        else:transport[label]=fetch_direct(label,item['sources'][label],retained)
    return review_all(item,retained),transport


def pack_sources(retained,sources,target):
    retained,target=Path(retained),Path(target);temporary=target.with_name(target.name+'.tmp')
    with temporary.open('wb') as raw:
        with gzip.GzipFile(fileobj=raw,mode='wb',mtime=0,filename='') as compressed:
            with tarfile.open(fileobj=compressed,mode='w|') as tar:
                for label in LABELS:
                    for name,row in sorted(sources[label]['files'].items()):
                        path=bound(retained/label,row);info=tar.gettarinfo(str(path),arcname=label+'/'+name)
                        info.uid=info.gid=info.mtime=0;info.uname=info.gname=''
                        with path.open('rb') as stream:tar.addfile(info,stream)
    temporary.replace(target)


def unpack_sources(bundle,retained,sources):
    retained=Path(retained);wanted={(label,name):row for label in LABELS for name,row in sources[label]['files'].items()}
    seen=set()
    with tarfile.open(bundle,'r|gz') as tar:
        for member in tar:
            if member.isdir():continue
            path=PurePosixPath(member.name)
            assert member.isfile() and not path.is_absolute() and '..' not in path.parts and len(path.parts)==2
            key=tuple(path.parts);assert key in wanted and key not in seen;seen.add(key)
            row=wanted[key];assert member.size==row['bytes']
            target=retained/key[0]/key[1];target.parent.mkdir(parents=True,exist_ok=True)
            temporary=target.with_name(target.name+'.download');h=hashlib.sha256();count=0
            with tar.extractfile(member) as stream,temporary.open('wb') as sink:
                for block in iter(lambda:stream.read(4*1024*1024),b''):
                    sink.write(block);h.update(block);count+=len(block)
            assert count==row['bytes'] and h.hexdigest()==row['sha256']
            if target.exists():bound(target.parent,row);temporary.unlink()
            else:temporary.replace(target)
    assert seen==set(wanted);return len(seen)


def expected_tag(item,reviewed):
    return {'result':RESULT,'source_sha256':item['core_sha256'],
        'proof_sha256':item['proof_sha256'],'method_sha256':item['method_sha256'],
        'source_identities':{label:dict(identity(source),selected_files_sha256=source['selected_files_sha256'],
            selected_file_count=source['selected_file_count']) for label,source in reviewed.items()},
        'arithmetic':'symbolic exact original expression composition; no old numerical arithmetic executed',**SCOPE}


def prepare_sources(item,out,allow_download=True):
    out=Path(out);retained=out.parent/'retained-global-polar-DAG';retained.mkdir(parents=True,exist_ok=True)
    if all((out/name).exists() for name in (INPUT_RECEIPT,INVENTORY,BUNDLE)):
        receipt,inventory=read(out/INPUT_RECEIPT),read(out/INVENTORY)
        assert receipt['result']==inventory['result']==RESULT
        assert receipt['complete'] is True and inventory['complete'] is True
        assert receipt['source_requests']==item['sources']
        assert receipt['expanded_sources_sha256']==item['expanded_sources_sha256']
        bound(out,receipt['source_inventory']);bound(out,receipt['source_bundle'])
        count=unpack_sources(out/BUNDLE,retained,inventory['sources'])
        reviewed=review_all(item,retained);assert reviewed==inventory['sources']
        assert count==receipt['minimal_bundle_member_count']==item['selected_original_file_count']
        return retained,receipt,reviewed
    assert allow_download,'Continuation lost its original source carrier.'
    reviewed,transport=fetch_sources(item,retained)
    save(out/INVENTORY,{'result':RESULT,'complete':True,'sources':reviewed,
        'all_members_are_unchanged_original_producer_bytes':True})
    pack_sources(retained,reviewed,out/BUNDLE)
    receipt={'result':RESULT,'complete':True,'source_requests':item['sources'],
        'expanded_sources_sha256':item['expanded_sources_sha256'],
        'source_inventory':file_spec(out/INVENTORY),'source_bundle':file_spec(out/BUNDLE),
        'minimal_bundle_member_count':item['selected_original_file_count'],'range_transport':transport,
        'old_numerical_arithmetic_recomputed':False}
    save(out/INPUT_RECEIPT,receipt)
    print('GLOBAL_POLAR_SOURCE_IO='+json.dumps({'source_inventory':receipt['source_inventory'],
        'source_bundle':receipt['source_bundle'],'selected_original_files':item['selected_original_file_count'],
        'new_mathematics_executed':False},sort_keys=True),flush=True)
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


def restore(item,out):
    resume=item.get('resume')
    if resume is None:return
    assert resume['result']==RESULT and resume['core_sha256']==item['core_sha256']
    out=Path(out);meta=out.parent/'resume-global-polar-metadata';meta.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(resume,out.parent/'download-global-polar-resume',whole=False)
    try:
        archive.extract_bound(MANIFEST,resume['manifest_sha256'],meta/MANIFEST,resume['manifest_bytes'])
        manifest=read(meta/MANIFEST);assert manifest['result']==RESULT
        entries={row['file']:plain(row) for row in manifest['files']}
        assert len(entries)==len(manifest['files'])==resume['manifest_file_count']
        names=['run-receipt.json','public-actions-input.json',INPUT_RECEIPT,INVENTORY,BUNDLE]
        if 'core-receipt.json' in entries:names.append('core-receipt.json')
        for name in names:
            row=entries[name];destination=out/name if name in (INPUT_RECEIPT,INVENTORY,BUNDLE) else meta/name
            archive.extract_bound(name,row['sha256'],destination,row['bytes'])
        run=read(meta/'run-receipt.json');initial=read(meta/'public-actions-input.json')
        assert run['result']==initial['result']==RESULT
        assert run['source_commit']==initial['source_commit']==resume['source_commit']
        assert str(run['workflow_run_id'])==str(resume['run_id'])
        assert initial['core_sha256']==item['core_sha256'] and stable_job(initial['job'])==stable_job(item)
        assert run['process_exit_code'] in resume['accepted_process_exit_codes']
        core=None
        if (meta/'core-receipt.json').exists():
            core=read(meta/'core-receipt.json');assert core['source_sha256']==item['core_sha256']
            assert run['core_receipt_sha256']==entries['core-receipt.json']['sha256']
        else:assert run.get('core_receipt_sha256') is None and run['complete'] is False
        _,_,reviewed=prepare_sources(item,out,allow_download=False);tag=expected_tag(item,reviewed)
        math_names=sorted(name for name in entries if name.startswith(PREFIX) and name.endswith('.json.gz'))
        archive.extract_many([(name,entries[name]['sha256'],out/name,entries[name]['bytes']) for name in math_names])
        for name in math_names:
            value=read(out/name);assert value['complete'] is True and value['configuration']==tag
            assert value['result']==RESULT
        restored_final=False
        if FINAL in entries:
            row=entries[FINAL];archive.extract_bound(FINAL,row['sha256'],meta/FINAL,row['bytes'])
            final=read(meta/FINAL);assert final['result']==RESULT and final['configuration']==tag
            if final['complete'] is True:
                assert run['complete'] is True and run['process_exit_code']==0 and core and core['complete'] is True
                assert core['certificate_sha256']==row['sha256']
                assert all(final[key] is True for key in TRUE_FLAGS)
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
            'io_helper_sha256':HELPER_SHA,'workflow_sha256':sha(REPO/item['workflow']),
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
        print(json.dumps({'wrapper_error':error},sort_keys=True),flush=True)
    finally:
        core=read(out/'core-receipt.json') if (out/'core-receipt.json').exists() else None
        final=read(out/FINAL) if (out/FINAL).exists() else None
        complete=bool(exitcode==0 and not error and core and core['complete'] and final and final['complete'])
        run={'result':RESULT,'p':41,'source_commit':os.environ.get('GITHUB_SHA'),
            'workflow_run_id':os.environ.get('GITHUB_RUN_ID'),'workflow_attempt':os.environ.get('GITHUB_RUN_ATTEMPT'),
            'process_exit_code':exitcode,'complete':complete,'error':error,'outer_timeout':outer_timeout,
            'core_receipt_sha256':sha(out/'core-receipt.json') if core else None,
            'finished_at_utc':dt.datetime.now(dt.timezone.utc).isoformat(),
            'old_mathematical_computations_repeated':False,'original_rigidification_and_height_computed':False}
        save(out/'run-receipt.json',run);output_manifest(out)
    return 0 if complete else exitcode or 1


def check_source_ref(row,reviewed):
    assert row['producer'] in reviewed
    assert reviewed[row['producer']]['files'][row['file']]==plain(row)


def verify(out):
    out=Path(out);initial=read(out/'public-actions-input.json');item=initial['job']
    assert initial['result']==RESULT and initial['source_repository']=='Rogerhu12/math-research-public'
    assert initial['core_sha256']==item['core_sha256'] and initial['driver_sha256']==item['wrapper_sha256']
    load_helper(item)
    _,receipt,reviewed=prepare_sources(item,out,allow_download=False);tag=expected_tag(item,reviewed)
    run=read(out/'run-receipt.json');core=read(out/'core-receipt.json') if (out/'core-receipt.json').exists() else None
    assert run['result']==RESULT and run['source_commit']==initial['source_commit']
    if core:
        assert core['result']==RESULT and core['source_sha256']==item['core_sha256']
        assert run['core_receipt_sha256']==sha(out/'core-receipt.json')
        if core['configuration'] is not None:assert core['configuration']==tag
    else:assert run['core_receipt_sha256'] is None and run['complete'] is False
    all_math={}
    for path in sorted(out.glob(PREFIX+'*.json.gz')):
        value=read(path);assert value['configuration']==tag and value['result']==RESULT and value['complete'] is True
        all_math[path.name]=file_spec(path)
    if not (out/FINAL).exists():
        assert run['complete'] is False
        print('GLOBAL_POLAR_VERIFY='+json.dumps({'complete':False,'completed_math_files':len(all_math)}),flush=True)
        return False
    final=read(out/FINAL);assert final['result']==RESULT and final['configuration']==tag
    for key in FALSE_FLAGS:assert final[key] is False
    if final['complete'] is not True:
        assert run['complete'] is False
        print('GLOBAL_POLAR_VERIFY='+json.dumps({'complete':False,'completed_math_files':len(all_math)}),flush=True)
        return False
    assert run['complete'] is True and run['process_exit_code']==0 and run['error'] is None
    assert core and core['complete'] is True and core['process_exit_code']==0
    assert core['certificate_sha256']==sha(out/FINAL)
    assert all(final[key] is True for key in TRUE_FLAGS)
    inventory=read(bound(out,final['stage_manifest']))
    assert inventory['configuration']==tag and inventory['complete'] is True
    assert {x['file']:plain(x) for x in inventory['files']}=={k:v for k,v in all_math.items() if k!=MATH_INVENTORY}
    source_audit=read(bound(out,final['source_audit']));graph=read(bound(out,final['exact_expression_DAG']))
    assert graph['source_audit']==final['source_audit']
    for key in TRUE_FLAGS:assert graph[key] is True
    for key in FALSE_FLAGS:assert graph[key] is False
    assert source_audit['all_1234_original_real_rows_present'] is True
    assert source_audit['all130_original_Laurent_stages_present'] is True
    assert source_audit['global_W_complete_coordinate_group_count']==34
    assert source_audit['six_C_complete_coordinate_group_count']==12
    seen=set();nodes={}
    for i,node in enumerate(graph['graph_nodes']):
        assert node['ordinal']==i and all(x in seen for x in node['inputs'])
        body={key:node[key] for key in ('operation','domain','inputs','data')}
        assert node['id']=='n'+fingerprint(body) and node['id'] not in seen
        seen.add(node['id']);nodes[node['id']]=node
        for key in ('denominator_nonzero_proof','all_generators_not_simultaneously_zero_proof'):
            if key in node['data']:assert node['data'][key] in graph['nonzero_proof_obligations']
        if 'Galois_definition_node' in node['data']:assert node['data']['Galois_definition_node'] in seen
    assert final['actual_graph_node_count']==graph['actual_graph_node_count']==len(seen)
    assert set(graph['five_original_polar_and_eta_outputs'])==set(map(str,range(1,6)))
    def refs(value):
        if isinstance(value,dict):
            if all(key in value for key in ('producer','file','bytes','sha256')) and value['producer'] in reviewed:
                check_source_ref(value,reviewed)
            for v in value.values():refs(v)
        elif isinstance(value,list):
            for v in value:refs(v)
    refs(graph);refs(source_audit)
    for j in map(str,range(1,6)):
        output=graph['five_original_polar_and_eta_outputs'][j]
        assert output['eta_Picard_class']['sign']==-1
        assert set(output['global_pole_ideals'])=={'tau','sigma'}
        assert all(node in seen for node in output['global_pole_ideals'].values())
        comparison=graph['original_principal_comparisons'][j]
        assert comparison['fractional_ideal_identity']=='I_ZjR=R_j*I_Zj^3'
        assert comparison['uses_true_Galois_norm'] is True and comparison['same_target_product_used'] is False
    print('GLOBAL_POLAR_VERIFY='+json.dumps({'complete':True,'actual_graph_node_count':len(seen),
        'actual_nonzero_proof_obligation_count':len(graph['nonzero_proof_obligations']),
        'five_original_polar_DAGs':5,'both_original_affine_charts':True,
        'original_eta_classes_proved_zero':False,'original_rigidification_and_height_computed':False,
        'source_member_count':receipt['minimal_bundle_member_count']},sort_keys=True),flush=True)
    return True


def main():
    parser=argparse.ArgumentParser();parser.add_argument('mode',choices=['compute','verify'])
    parser.add_argument('--request',default=str(REQUEST));parser.add_argument('--out',required=True)
    args=parser.parse_args();out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    if args.mode=='verify':
        try:verify(out)
        finally:output_manifest(out)
        return
    request=Path(args.request);item=read(request);guard(item,request)
    code=compute(item,out,request);raise SystemExit(code)


if __name__=='__main__':main()
