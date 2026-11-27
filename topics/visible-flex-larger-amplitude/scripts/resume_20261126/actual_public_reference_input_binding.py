#!/usr/bin/env python3
"""Strict whole-file public run09 input binding, without field or numerical solves.

Both genuine public returns are selected by their complete published SHA and
unique stage identity. The producer freezes their whole small text files in its
fresh runner output before later controller appends can change a public volume.
This pure standard-library module verifies those immutable copies, all six
current input files, the embedded complete reference model, every chart word,
and the original scalar/domain projection. No old mathematical target or
scientific certificate is inherited merely because some file words coincide.
"""
import ast
import copy
from fractions import Fraction as F
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import re
import struct
import zipfile

SCHEMA = 'complete-actual-public-run09-reference-input-binding-v1'
EVIDENCE_SCHEMA = 'actual-public-run09-warm-reference-whole-file-evidence-v1'
TARGET_SCHEMA = 'independently-frozen-actual-public-run09-scalar-and-material-chart-v1'
COMPATIBILITY_SCHEMA = 'actual-public-run09-fixed-target-and-historical-carrier-binding-v1'
RUN_ID = '45943410994'
RUN_ATTEMPT = '1'
REFERENCE_STEP = 'independent-axisymmetric-R690-reference-prepare-v2-first-20261127-09'
REFERENCE_SHA = '4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3'
REFERENCE_SCHEMA = 'R690-independent-axisymmetric-SO3-reference-input-v1'
PREPARATION_SCHEMA = 'R690-independent-axisymmetric-SO3-preparation-v1'
WARM_SOURCE_SHA = 'bee5ae587bd519189b0b27c249987d80d82ab66822cd4f1ea4746a769f7fb3c3'
WARM_RECIPE_SHA = '561308ca74186ac8eeb302dc786b633f2f643a1f98896d0685691d06eec556a4'
WARM_CONTROLLER_SHA = '067b3f2e14145a6f88b2d171c555f1174f0505b45a5aaf670c3ec2610f7c286d'
PARAMETERS_SHA = 'e640aec831df350fa69740650b723a7d2d55676ca64ffb5ddabbacb3ab7d6dfa'
ORIGIN_MESH_SHA = 'eff967897039ec740c9aca49620253f27fb46d93cd8c59f4ed4759781ef88262'
ORIGIN_CHART_SHA = '90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e'
ORIGIN_WARM_SHA = '3df37dd362a1c700eaa86eece3d0b9a17524068c2a78fe0bebb1e96f1d09518c'
ORIGIN_CARRIER_SHA = 'dc5ffc55ecc4478d265bbad6e8f2abcf672709d99365e14ead01478a4042e7d0'
ORIGIN_CARRIER_BYTES = 227202
ORIGIN_PUBLIC_SHA = '6eca69a388330b3e539aac4e2c793ce8256c724d52abf11adc8c8e85d49d08b3'
ORIGIN_ENVELOPE_SHA = 'c79c7f7ec1febf0ab6dca30d28a91b1566745972342c7336a3a9a106f56b3152'
TOPIC = 'topics/visible-flex-larger-amplitude'
METRIC_KEY = 'axisymmetric-R690-reference-v2-first/report.json'
SOURCE_PINS = {
    'warm_producer': WARM_SOURCE_SHA,
    'observed': '26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d',
    'scalar': 'a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670',
    'integer': 'babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0',
    'hold': 'ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1',
    'deep_scalar': 'e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2',
    'history': '4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60',
}
ACTUAL_PUBLIC_RECORD_SHA = "5e3732096b95ccc65f7fc70cc2b4e5ba4ffc67023c444ce4f93762c7d765a1be"
ACTUAL_REFERENCE_MODEL_SHA = "d4494b14955535635b8b72b1ed3278fa8f60186d4ef7df5687ca3de5566c2f75"
ACTUAL_FIXED_PROFILE_SHA = "5de7dcbb0fd1daacad7c20b276120dfc52b9d1f2eb67890300c9afc56242b3ed"
ACTUAL_CURRENT_FILES = {
    "current_warm_bundle": {
        "path": "/home/runner/work/_temp/visible-larger-research-45943410994-1/research/fullclosed_solver/data/fullclosed-hold-warm.npz",
        "sha256": "3df37dd362a1c700eaa86eece3d0b9a17524068c2a78fe0bebb1e96f1d09518c",
        "bytes": 8767118
    },
    "current_node_report": {
        "path": "/home/runner/work/_temp/visible-larger-research-45943410994-1/research/fullclosed_solver/data/fullclosed-hold-warm.json",
        "sha256": "918ccdf1a132ca4ba50e0fa97cbb53f7aeabac8f63dc24e7eada64a18fb80269",
        "bytes": 554141
    },
    "current_scalar_input": {
        "path": "/home/runner/work/_temp/visible-larger-research-45943410994-1/research/fullclosed_solver/data/pulse-a5-complete-base.json.gz",
        "sha256": "83e65252955298326934ee371ace2391ea9161b69a9289ce4a3c5bd74c67c986",
        "bytes": 14227850
    },
    "current_carrier": {
        "path": "/home/runner/work/_temp/visible-larger-research-45943410994-1/research/axisymmetric-R690-reference-v2-first/observations.npz",
        "sha256": "792a132357861684ae01b15b2276c0259583ef27c44387288f424e08d6b488bb",
        "bytes": 227205
    },
    "current_preparation_report": {
        "path": "/home/runner/work/_temp/visible-larger-research-45943410994-1/research/axisymmetric-R690-reference-v2-first/report.json",
        "sha256": "4cc93d406cc1882771d2ebabb34856e7ed195fb6cdb6b361e1b213e504193ad2",
        "bytes": 29802
    },
    "current_reference_bundle": {
        "path": "/home/runner/work/_temp/visible-larger-research-45943410994-1/research/axisymmetric-R690-reference-v2-first/reference.npz",
        "sha256": "2ab8593585286a6c4eab78d107f83a02d8332e7ae1747253534264506b3da7f2",
        "bytes": 866176
    }
}

CURRENT_KEYS = ('current_warm_bundle','current_node_report','current_scalar_input',
    'current_carrier','current_preparation_report','current_reference_bundle')
WARM_MEMBERS = ('mesh','qjets','a_stages','radius','Hcap','width','fixed_core_first3',
    'circle_projection','a_stage_absolute_error','stage_time_absolute_error')
REFERENCE_MEMBERS = ('schema','mesh','initial_core','initial_height','original_warm_height',
    'radius','width','fixed_core_first3','cached_scalar_cells','cached_scalar_local',
    'cached_scalar_values','cached_scalar_errors','reference_model_json',
    'reference_model_identity_sha256')
CONSUMED_WARM_PROJECTION = ('mesh','width','radius','qjets[0,0,1:161]','fixed_core_first3')


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),
        allow_nan=False).encode()).hexdigest()


def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda:stream.read(1<<20),b''):
            h.update(block)
    return h.hexdigest()


def file_record(path):
    p=Path(path).resolve()
    return dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size)


def digest(value,name):
    if not isinstance(value,str) or not re.fullmatch(r'[0-9a-f]{64}',value):
        raise ValueError('A complete actual SHA256 is required: '+name)
    return value


def valid_record(value,name,*,reread=False):
    if (not isinstance(value,dict) or set(value)!={'path','sha256','bytes'}
            or not isinstance(value['path'],str) or not Path(value['path']).is_absolute()
            or type(value['bytes']) is not int or value['bytes']<=0):
        raise ValueError('A complete actual file record is required: '+name)
    digest(value['sha256'],name)
    if reread and file_record(value['path'])!=value:
        raise ValueError('The bound whole file changed: '+name)
    return value


def read_bytes(value,name):
    valid_record(value,name)
    raw=Path(value['path']).read_bytes()
    if len(raw)!=value['bytes'] or hashlib.sha256(raw).hexdigest()!=value['sha256']:
        raise ValueError('The exact file snapshot changed: '+name)
    return raw


def read_json(value,name):
    return json.loads(read_bytes(value,name))


def record_union(values):
    """Every alias of a consumed path must name exactly the same whole bytes."""
    used={}
    for name,value in values.items():
        valid_record(value,name)
        path=str(Path(value['path']).resolve())
        if path in used and used[path]!=value:
            raise ValueError('One input path has conflicting whole-file records: '+path)
        used[path]=copy.deepcopy(value)
    return used


def array_sha(dtype,shape,raw):
    h=hashlib.sha256(dtype.encode())
    h.update(json.dumps(list(shape)).encode())
    h.update(raw)
    return h.hexdigest()


def chart_record(words):
    if not isinstance(words,list) or len(words)!=160:
        raise ValueError('Keep every one of the 160 fixed-chart words')
    values=[]
    for word in words:
        if not isinstance(word,str):
            raise ValueError('A literal finite binary64 chart word is required')
        value=float.fromhex(word)
        if not math.isfinite(value) or value.hex()!=word:
            raise ValueError('The complete chart word is not canonical binary64')
        values.append(value)
    raw=b''.join(struct.pack('<d',v) for v in values)
    return dict(dtype='float64',shape=[160],sha256=array_sha('float64',(160,),raw),
        binary64_byte_order='little',all_words=160)


def npy_member(archive,name):
    raw=archive.read(name+'.npy')
    if len(raw)<10 or raw[:6]!=b'\x93NUMPY':
        raise ValueError('Invalid complete NPY member: '+name)
    version=tuple(raw[6:8])
    if version==(1,0):
        length,start=struct.unpack('<H',raw[8:10])[0],10
    elif version in ((2,0),(3,0)):
        if len(raw)<12:
            raise ValueError('Truncated NPY member: '+name)
        length,start=struct.unpack('<I',raw[8:12])[0],12
    else:
        raise ValueError('Unsupported actual NPY version')
    end=start+length
    if end>len(raw):
        raise ValueError('Truncated NPY header: '+name)
    h=ast.literal_eval(raw[start:end].decode('utf-8' if version==(3,0) else 'latin1'))
    if (not isinstance(h,dict) or set(h)!={'descr','fortran_order','shape'}
            or h['fortran_order'] is not False or not isinstance(h['shape'],tuple)
            or any(type(v) is not int or v<0 for v in h['shape'])):
        raise ValueError('Use complete C-order primitive arrays: '+name)
    d=h['descr']; shape=h['shape']; payload=raw[end:]
    if d in ('<f8','<i8'):
        width=8
    elif isinstance(d,str) and d.startswith('<U') and d[2:].isdigit():
        width=4*int(d[2:])
    else:
        raise ValueError('Changed actual array dtype: '+name)
    if len(payload)!=width*math.prod(shape):
        raise ValueError('Incomplete actual array payload: '+name)
    return d,shape,payload


def member(archive,name,dtype,shape):
    d,s,raw=npy_member(archive,name)
    if d!=dtype or s!=tuple(shape):
        raise ValueError('Changed actual array shape or dtype: '+name)
    if dtype=='<f8' and any(not math.isfinite(v) for (v,) in struct.iter_unpack('<d',raw)):
        raise ValueError('Nonfinite actual input member: '+name)
    return raw


def string_member(archive,name):
    d,s,raw=npy_member(archive,name)
    if not d.startswith('<U') or s!=():
        raise ValueError('A complete scalar Unicode member is required: '+name)
    return raw.decode('utf-32le').rstrip('\x00')


def scalar_word(archive,name):
    return struct.unpack('<d',member(archive,name,'<f8',()))[0]


def _output_map(value):
    outputs=value.get('outputs')
    if not isinstance(outputs,list):
        raise ValueError('The actual complete output list is required')
    result={}
    for item in outputs:
        valid_record(item,'published output')
        key=Path(item['path']).name
        if key in result:
            raise ValueError('Ambiguous duplicate published output basename')
        result[key]=copy.deepcopy(item)
    record_union({str(i):v for i,v in enumerate(outputs)})
    return result


def _source_roles(value):
    rows=value.get('input_files')
    if not isinstance(rows,list):
        raise ValueError('The actual complete public source/input list is required')
    result={}
    for row in rows:
        if not isinstance(row,dict) or not isinstance(row.get('role'),str) or row['role'] in result:
            raise ValueError('Duplicated or missing actual public input role')
        digest(row.get('sha256'),'actual public source '+row['role'])
        if (not isinstance(row.get('path'),str) or not row['path']
                or not re.fullmatch(r'[0-9a-f]{40}',str(row.get('commit','')))):
            raise ValueError('Keep complete actual source paths and commits')
        result[row['role']]=copy.deepcopy(row)
    return result


def _command_argument(command,name):
    if not isinstance(command,list) or any(not isinstance(v,str) for v in command) or command.count(name)!=1:
        raise ValueError('Missing unique actual public argument: '+name)
    j=command.index(name)
    if j+1==len(command):
        raise ValueError('Missing actual public argument value: '+name)
    return command[j+1]


def _document(document,role):
    if (not isinstance(document,dict) or set(document)!={'published_record','snapshot_record',
            'repository_relative_path','requested_public_sha256','source_checkout_commit'}
            or not isinstance(document['repository_relative_path'],str)
            or not re.fullmatch(r'[0-9a-f]{40}',str(document['source_checkout_commit']))):
        raise ValueError('Keep the complete immutable public-document provenance')
    original=valid_record(document['published_record'],role+' original public record')
    snap=valid_record(document['snapshot_record'],role+' immutable public snapshot')
    if (not 0<original['bytes']<100000 or snap['sha256']!=original['sha256']
            or snap['bytes']!=original['bytes']
            or digest(document['requested_public_sha256'],role)!=original['sha256']
            or original['sha256']!=ACTUAL_PUBLIC_RECORD_SHA):
        raise ValueError('The complete public snapshot differs from the explicit requested bytes')
    relative=Path(document['repository_relative_path'])
    if (relative.is_absolute() or '..' in relative.parts
            or relative.parent.as_posix()!=TOPIC+'/notes'
            or not re.fullmatch(r'\d{4}-\d{2}-\d{2}-public-actions-'+RUN_ID+'-'+RUN_ATTEMPT+r'-part-\d{3}\.md',relative.name)
            or Path(original['path']).name!=relative.name):
        raise ValueError('Select an actual complete public run09 volume, not another run')
    text=read_bytes(snap,role+' immutable public snapshot').decode()
    if (not text.startswith('# 公开Actions '+RUN_ID+'/'+RUN_ATTEMPT+'：实际阶段 ')
            or '[运行](https://github.com/Rogerhu12/math-research-public/actions/runs/'+RUN_ID+')' not in text):
        raise ValueError('The public source text belongs to another actual run')
    blocks=[json.loads(v) for v in re.findall(r'```json\s*\n(.*?)\n```',text,flags=re.S)]
    if any(not isinstance(v,dict) for v in blocks):
        raise ValueError('Every actual stage record must be a complete object')
    return blocks


def freeze_public_document(path,expected,repo,outdir,label,source_commit):
    """Copy only a whole <100KB published text; the immutable copy stays on runner."""
    p=Path(path).resolve(); repo=Path(repo).resolve()
    try:
        relative=p.relative_to(repo)
    except ValueError as exc:
        raise ValueError('Public stage evidence must come from this source checkout') from exc
    before=file_record(p)
    if before['sha256']!=digest(expected,'requested '+label+' public SHA'):
        raise ValueError('The actual public volume differs from its explicit requested SHA')
    raw=read_bytes(before,label+' complete public text')
    if not 0<len(raw)<100000:
        raise ValueError('Use the complete bounded public volume')
    target=Path(outdir)/('actual-public-'+label+'-immutable.md')
    if target.exists() or target.resolve()==p:
        raise ValueError('Use a fresh separate immutable public-evidence snapshot')
    target.write_bytes(raw)
    item=dict(published_record=before,snapshot_record=file_record(target),
        repository_relative_path=relative.as_posix(),requested_public_sha256=expected,
        source_checkout_commit=source_commit)
    _document(item,label)
    if file_record(p)!=before:
        raise ValueError('The public volume changed while its actual bytes were captured')
    return item


def public_evidence(documents,files,reference_step_id):
    """Rebind genuine completed warm/reference records to all six actual files."""
    if reference_step_id!=REFERENCE_STEP or not isinstance(documents,dict) or set(documents)!={'warm','reference'}:
        raise ValueError('Use the explicit actual run09 complete warm and reference selection')
    if not isinstance(files,dict) or files!=ACTUAL_CURRENT_FILES:
        raise ValueError('All six current whole input records are mandatory')
    record_union(dict(files,**{k+' snapshot':v['snapshot_record'] for k,v in documents.items()}))
    for key,value in files.items():
        valid_record(value,key,reread=True)
    warm_matches=[v for v in _document(documents['warm'],'warm') if v.get('name')=='warm']
    ref_matches=[v for v in _document(documents['reference'],'reference')
        if v.get('name')=='followup:'+REFERENCE_STEP]
    if len(warm_matches)!=1 or len(ref_matches)!=1:
        raise ValueError('Select exactly one genuine warm and exactly one reference stage')
    warm,step=warm_matches[0],ref_matches[0]
    wm=warm.get('metrics',{}); metrics=step.get('metrics',{}).get(METRIC_KEY,{})
    warm_sources=_source_roles(warm); wo=_output_map(warm); outputs=_output_map(step)
    for value,source in ((warm,WARM_CONTROLLER_SHA),(step,REFERENCE_SHA)):
        if (value.get('state')!='completed' or value.get('returncode')!=0
                or value.get('source_sha256')!=source
                or not re.fullmatch(r'[0-9a-f]{40}',str(value.get('source_commit','')))):
            raise ValueError('Only complete genuine source-bound public returns are inputs')
    if (warm_sources.get('recipe',{}).get('sha256')!=WARM_RECIPE_SHA
            or warm_sources.get('hold_warm',{}).get('sha256')!=WARM_SOURCE_SHA
            or wm.get('old_optimization_directions_started')!=0
            or [wm.get(k) for k in ('M','J','cells')]!=[160,923,922]
            or step.get('step_id')!=REFERENCE_STEP
            or metrics.get('schema')!=PREPARATION_SCHEMA
            or metrics.get('source_sha256')!=REFERENCE_SHA or metrics.get('complete') is not True
            or metrics.get('source_commit')!=step['source_commit']
            or metrics.get('model')!=ACTUAL_REFERENCE_MODEL_SHA
            or metrics.get('fixed_profile')!=ACTUAL_FIXED_PROFILE_SHA
            or metrics.get('scalar_parameters')!=PARAMETERS_SHA
            or [metrics.get(k) for k in ('M','J','P','N')]!=[160,923,7377,2048]
            or metrics.get('scalar_complete_tail') is not True
            or not isinstance(metrics.get('scalar_tolerance_reached'),bool)):
        raise ValueError('The actual returns do not satisfy the complete unchanged source/input contract')
    for k in ('original_warm','node','scalar_input','carrier','reference','model','fixed_profile','locations','ordered_provenance'):
        digest(metrics.get(k),'actual reference metric '+k)
    root=Path(files['current_preparation_report']['path']).parent.parent
    if (root.name!='research' or root.parent.name!='visible-larger-research-'+RUN_ID+'-'+RUN_ATTEMPT):
        raise ValueError('Current files belong to another actual runner workspace')
    expected={
        'current_warm_bundle':(root/'fullclosed_solver/data/fullclosed-hold-warm.npz','original_warm','hold_bundle_sha256',wo),
        'current_node_report':(root/'fullclosed_solver/data/fullclosed-hold-warm.json','node','hold_report_sha256',wo),
        'current_scalar_input':(root/'fullclosed_solver/data/pulse-a5-complete-base.json.gz','scalar_input','scalar_input_sha256',wo),
        'current_carrier':(root/'axisymmetric-R690-reference-v2-first/observations.npz','carrier',None,outputs),
        'current_reference_bundle':(root/'axisymmetric-R690-reference-v2-first/reference.npz','reference',None,outputs),
        'current_preparation_report':(root/'axisymmetric-R690-reference-v2-first/report.json',None,None,outputs),
    }
    for key,(path,metric,wmetric,entries) in expected.items():
        item=files[key]
        if (Path(item['path']).resolve()!=path.resolve()
                or entries.get(path.name)!=item
                or (metric is not None and item['sha256']!=metrics[metric])
                or (wmetric is not None and item['sha256']!=wm.get(wmetric))):
            raise ValueError('One current whole input is not its actual public output: '+key)
    command=step.get('command')
    required_args={'--warm-bundle':files['current_warm_bundle']['path'],
        '--node-report':files['current_node_report']['path'],
        '--scalar-input':files['current_scalar_input']['path'],
        '--outdir':str(root/'axisymmetric-R690-reference-v2-first'),
        '--angles':'2048','--panels':'128','--seed-integration-order':'8',
        '--scalar-integral-tolerance':'1e-18','--scalar-tail-cutoff':'1/8',
        '--scalar-admission-seconds':'300'}
    for name,expected_word in required_args.items():
        if _command_argument(command,name)!=expected_word:
            raise ValueError('The complete actual reference parameter changed: '+name)
    prepared=read_json(files['current_preparation_report'],'current preparation')
    history={}
    for name,filename,metric in (
            ('locations','locations.json','locations'),
            ('supplied_location_provenance','supplied-location-provenance.json','ordered_provenance')):
        item=outputs.get(filename)
        valid_record(item,'actual '+name,reread=True)
        if (Path(item['path']).resolve()!=(root/'axisymmetric-R690-reference-v2-first'/filename).resolve()
                or item['sha256']!=metrics[metric]):
            raise ValueError('The complete actual supplied history differs from its public return')
        history[name]=item
    if (prepared.get('new_locations')!=history['locations']
            or prepared.get('complete_supplied_location_provenance')!=history['supplied_location_provenance']
            or prepared.get('execution',{}).get('run_id')!=RUN_ID
            or prepared.get('execution',{}).get('run_attempt')!=RUN_ATTEMPT):
        raise ValueError('The actual preparation/history belongs to another complete source run')
    result=dict(schema=EVIDENCE_SCHEMA,source_sha256=sha(__file__),actual_run_id=RUN_ID,
        actual_run_attempt=RUN_ATTEMPT,actual_reference_step_id=REFERENCE_STEP,
        complete_public_documents=copy.deepcopy(documents),current_files=copy.deepcopy(files),
        complete_supplied_history_files=copy.deepcopy(history),
        actual_warm_record_identity_sha256=canonical(warm),
        actual_reference_record_identity_sha256=canonical(step),
        actual_warm_source_commit=warm['source_commit'],actual_reference_source_commit=step['source_commit'],
        actual_warm_source_sha256=WARM_CONTROLLER_SHA,actual_reference_source_sha256=REFERENCE_SHA,
        actual_warm_recipe_sha256=WARM_RECIPE_SHA,actual_warm_producer_sha256=WARM_SOURCE_SHA,
        actual_reference_model_identity_sha256=metrics['model'],
        actual_fixed_scalar_profile_identity_sha256=metrics['fixed_profile'],
        actual_scalar_tolerance_reached=metrics['scalar_tolerance_reached'],
        actual_reference_command_identity_sha256=canonical(command),
        complete_original_reference_parameters=required_args,
        actual_warm_complete_source_list_identity_sha256=canonical(warm['input_files']),
        public_snapshots_preserve_exact_returned_bytes=True,
        later_mutable_public_volume_is_not_the_immutable_input=True,
        historical_whole_warm_requirement_applied_to_current=False,
        unreturned_values_inferred=False)
    record_union(dict(files,**history,**{k+' snapshot':v['snapshot_record'] for k,v in documents.items()}))
    for key,item in dict(files,**history).items():
        valid_record(item,key,reread=True)
    return result,step,metrics,outputs


def full_reference_projection(files,*,expected_model=None):
    """Read whole NPZ bytes and exact primitive words; no F, quadrature or root."""
    if set(files)!=set(CURRENT_KEYS):
        raise ValueError('Keep all six genuine input files')
    for key,item in files.items():
        valid_record(item,key,reread=True)
    preparation=read_json(files['current_preparation_report'],'actual preparation')
    node=read_json(files['current_node_report'],'actual symbolic-node input')
    model=preparation.get('reference_definition')
    if (not isinstance(model,dict) or preparation.get('schema')!=PREPARATION_SCHEMA
            or preparation.get('source_sha256')!=REFERENCE_SHA or preparation.get('complete') is not True
            or preparation.get('source_sha256_by_role')!=SOURCE_PINS
            or [preparation.get(k) for k in ('M','J','P','N')]!=[160,923,7377,2048]
            or preparation.get('reference_model_identity_sha256')!=canonical(model)
            or canonical(model)!=ACTUAL_REFERENCE_MODEL_SHA
            or model.get('schema')!=REFERENCE_SCHEMA or model.get('source_sha256')!=REFERENCE_SHA
            or [model.get(k) for k in ('M','J')]!=[160,923]
            or model.get('mesh_sha256')!=ORIGIN_MESH_SHA
            or model.get('original_scalar_parameters_identity_sha256')!=PARAMETERS_SHA
            or canonical(model.get('fixed_scalar_profile_definition'))!=model.get('fixed_scalar_metric_identity_sha256')
            or (expected_model is not None and model!=expected_model)):
        raise ValueError('The complete actual source/model/scalar definition differs')
    expected_solver={key:files[record_key] for key,record_key in (
        ('reference_bundle','current_reference_bundle'),('carrier','current_carrier'),
        ('node_report','current_node_report'),('scalar_input','current_scalar_input'))}
    if (preparation.get('input_for_solver')!=expected_solver
            or preparation.get('old_warm_bundle')!=files['current_warm_bundle']
            or preparation.get('old_warm_node_report')!=files['current_node_report']):
        raise ValueError('Do not assemble independent input hashes outside their actual preparation')
    for key,model_key in (('current_warm_bundle','original_warm_bundle_sha256'),
            ('current_node_report','symbolic_node_report_sha256'),('current_scalar_input','scalar_input_sha256'),
            ('current_carrier','observation_carrier_sha256')):
        if model.get(model_key)!=files[key]['sha256']:
            raise ValueError('The actual complete model names another input: '+key)
    if (node.get('schema')!='fullclosed-hold-real-pulse-warm-v1'
            or node.get('source_sha256')!=WARM_SOURCE_SHA
            or node.get('bundle_sha256')!=files['current_warm_bundle']['sha256']
            or node.get('input_sha256')!=files['current_scalar_input']['sha256']
            or node.get('exact_core_affine') is not True
            or node.get('M')!=160 or node.get('J')!=923
            or node.get('width_carrier')!=float(.05) or node.get('width_exact')!=str(F(.05))):
        raise ValueError('The entire actual node report differs from its true warm/scalar inputs')
    definitions=[[str(F(v['S_coefficient'])),str(F(v['constant']))] for v in node['true_scalar_nodes']]
    if len(definitions)!=923 or definitions[0]!=['0','0'] or definitions[-1]!=['1','0']:
        raise ValueError('Keep the entire exact 923-node affine domain')
    raw=read_bytes(files['current_scalar_input'],'actual scalar input')
    scalar=json.loads(gzip.decompress(raw) if raw[:2]==b'\x1f\x8b' else raw)
    parameters=dict(analytic_extension_origin=scalar['analytic_extension_origin'],
        geometry=scalar['fixed_scalar_profile']['geometry'])
    if canonical(parameters)!=PARAMETERS_SHA:
        raise ValueError('The complete exact scalar parameter projection changed')
    with zipfile.ZipFile(files['current_warm_bundle']['path']) as warm:
        if set(warm.namelist())!={v+'.npy' for v in WARM_MEMBERS}:
            raise ValueError('Keep every complete original warm array')
        mesh=member(warm,'mesh','<f8',(923,))
        qraw=member(warm,'qjets','<f8',(923,3,482))
        core=qraw[8:161*8]
        first=member(warm,'fixed_core_first3','<f8',(3,))
        width=member(warm,'width','<f8',())
        warm_height=member(warm,'Hcap','<f8',())
        member(warm,'radius','<f8',())
        if core[:24]!=first or struct.unpack('<d',width)[0].hex()!=float(.05).hex():
            raise ValueError('The complete actual first-three/width words changed')
    words=[v.hex() for (v,) in struct.iter_unpack('<d',core)]
    chart=chart_record(words)
    if (array_sha('float64',(923,),mesh)!=ORIGIN_MESH_SHA
            or chart['sha256']!=model.get('fixed_chart_core_sha256')
            or words[:3]!=model.get('fixed_core_first3')):
        raise ValueError('The full actual mesh/chart words differ from the actual reference model')
    with zipfile.ZipFile(files['current_reference_bundle']['path']) as ref:
        if set(ref.namelist())!={v+'.npy' for v in REFERENCE_MEMBERS}:
            raise ValueError('Keep every actual complete reference NPZ member')
        embedded=json.loads(string_member(ref,'reference_model_json'))
        if (embedded!=model or string_member(ref,'schema')!=REFERENCE_SCHEMA
                or string_member(ref,'reference_model_identity_sha256')!=canonical(model)
                or member(ref,'mesh','<f8',(923,))!=mesh
                or member(ref,'initial_core','<f8',(160,))!=core
                or member(ref,'fixed_core_first3','<f8',(3,))!=first
                or member(ref,'width','<f8',())!=width
                or member(ref,'original_warm_height','<f8',())!=warm_height):
            raise ValueError('The entire reference does not contain the actual fixed source projection')
        height=scalar_word(ref,'initial_height'); radius=scalar_word(ref,'radius')
        if (radius.hex()!=model.get('radius_carrier_hex')
                or height.hex()!=float(preparation['new_height']).hex()
                or struct.unpack('<d',warm_height)[0].hex()!=float(preparation['original_warm_height']).hex()):
            raise ValueError('The actual height/radius carrier words differ from their report')
        d,shape,cells=npy_member(ref,'cached_scalar_cells')
        if d!='<i8' or len(shape)!=1:
            raise ValueError('Keep the whole exact scalar-cache address array')
        local=member(ref,'cached_scalar_local','<f8',shape)
        member(ref,'cached_scalar_values','<f8',(shape[0],4))
        errors=member(ref,'cached_scalar_errors','<f8',(shape[0],4))
        if any(v<0 for (v,) in struct.iter_unpack('<d',errors)):
            raise ValueError('A true cached scalar carrier error is negative')
        addresses=set()
        for (cell,),(u,) in zip(struct.iter_unpack('<q',cells),struct.iter_unpack('<d',local)):
            if not 0<=cell<922 or not 0<=u<=1 or (cell,u.hex()) in addresses:
                raise ValueError('The complete scalar-cache material addresses are invalid or duplicated')
            addresses.add((cell,u.hex()))
    with zipfile.ZipFile(files['current_carrier']['path']) as carrier:
        if (member(carrier,'mesh','<f8',(923,))!=mesh
                or member(carrier,'fixed_core_first3','<f8',(3,))!=first
                or member(carrier,'width','<f8',())!=width
                or scalar_word(carrier,'radius').hex()!=radius.hex()
                or string_member(carrier,'fixed_scalar_metric_identity_sha256')!=model['fixed_scalar_metric_identity_sha256']):
            raise ValueError('The actual complete observation carrier and reference disagree')
        a=member(carrier,'a_observations','<f8',(7377,))
        if array_sha('float64',(7377,),a)!=model.get('a_observations_sha256') or any(v<=0 for (v,) in struct.iter_unpack('<d',a)):
            raise ValueError('Every actual positive scalar observation must retain its true words')
    for key,item in files.items():
        valid_record(item,key,reread=True)
    return dict(model=model,complete_scalar_parameters=parameters,
        exact_scalar_node_definitions=definitions,fixed_chart_core_binary64_hex=words,
        fixed_chart_core_array_record=chart,mesh_sha256=ORIGIN_MESH_SHA,
        initial_height_binary64_hex=height.hex(),radius_binary64_hex=radius.hex(),
        current_and_historical_fixed_chart_words_sha_equal=chart['sha256']==ORIGIN_CHART_SHA,
        whole_warm_reference_carrier_inputs_actually_read=True,
        scientific_field_or_root_evaluations=0)


def freeze_target(*,producer_sha256,evidence,projection):
    digest(producer_sha256,'complete producer')
    if (not isinstance(evidence,dict) or evidence.get('schema')!=EVIDENCE_SCHEMA
            or evidence.get('source_sha256')!=sha(__file__)
            or evidence.get('actual_run_id')!=RUN_ID or evidence.get('actual_run_attempt')!=RUN_ATTEMPT
            or evidence.get('actual_reference_step_id')!=REFERENCE_STEP):
        raise ValueError('Bind the full actual public evidence before freezing the target')
    checked,_,_,_=public_evidence(evidence['complete_public_documents'],evidence['current_files'],REFERENCE_STEP)
    if checked!=evidence:
        raise ValueError('The complete recorded public input evidence changed')
    actual=full_reference_projection(evidence['current_files'],expected_model=projection['model'])
    if actual!=projection:
        raise ValueError('The entire actual source projection changed before target freezing')
    model=actual['model']
    if (canonical(model)!=evidence['actual_reference_model_identity_sha256']
            or model['fixed_scalar_metric_identity_sha256']!=evidence['actual_fixed_scalar_profile_identity_sha256']):
        raise ValueError('Public model/profile and whole current files disagree')
    equal=actual['current_and_historical_fixed_chart_words_sha_equal']
    return dict(schema=TARGET_SCHEMA,definition_source_sha256=producer_sha256,
        public_input_binding_source_sha256=sha(__file__),
        complete_public_input_evidence=copy.deepcopy(evidence),
        complete_public_input_evidence_identity_sha256=canonical(evidence),
        complete_current_reference_model=copy.deepcopy(model),
        current_reference_model_identity_sha256=canonical(model),
        complete_current_reference_bundle_sha256=evidence['current_files']['current_reference_bundle']['sha256'],
        complete_scalar_parameters=copy.deepcopy(actual['complete_scalar_parameters']),
        complete_scalar_parameters_identity_sha256=PARAMETERS_SHA,
        complete_current_fixed_scalar_profile_definition=copy.deepcopy(model['fixed_scalar_profile_definition']),
        current_fixed_scalar_metric_identity_sha256=model['fixed_scalar_metric_identity_sha256'],
        fixed_chart_core_binary64_hex=list(actual['fixed_chart_core_binary64_hex']),
        fixed_chart_core_array_record=copy.deepcopy(actual['fixed_chart_core_array_record']),
        exact_scalar_node_definitions=copy.deepcopy(actual['exact_scalar_node_definitions']),
        exact_scalar_node_definitions_identity_sha256=canonical(actual['exact_scalar_node_definitions']),
        exact_node_recipe_source_sha256=WARM_SOURCE_SHA,complete_literal_mesh_array_sha256=ORIGIN_MESH_SHA,
        exact_literal_width_hex=float(.05).hex(),
        mathematical_target='ds^2+a_R690(s)^2*dTheta_actual_run09(phi0)^2',
        fixed_chart='all 160 literal actual reference coefficients are frozen in this definition',
        original_complete_scalar_source_sha256=REFERENCE_SHA,
        historical_original_chart_core_sha256=ORIGIN_CHART_SHA,
        current_and_historical_fixed_chart_words_sha_equal=equal,
        same_original_fixed_chart=equal,same_mathematical_g_claimed=False,
        historical_metric_relation='not claimed by this independent input; unequal metadata identities are not a mathematical inequality',
        independently_bound_target_identity=True,old_target_identity_inherited=False,
        exact_old_to_new_chart_conjugacy_claimed=False,target_fixed_before_any_field_or_direction=True,
        current_free_core_does_not_redefine_target=True,current_free_height_is_not_a_target_parameter=True,
        old_and_current_literal_material_addresses_all_retained=True,
        historical_angles_reinterpreted_as_new_fixed_chart_phi0=True,
        same_historical_physical_points_claimed=False,
        unknown_parallel_typed_priorities_reconstructed=False,
        unresolved_parallel_history_remains_an_explicit_obligation=True,
        original_branch_replaced_or_declared_finished=False,
        old_field_values_or_scientific_certificates_inherited=False)


def validate_target(value,*,producer_sha256,actual_model,reference_bundle,node):
    if not isinstance(value,dict):
        raise ValueError('Keep the entire independently frozen actual public target')
    evidence=value.get('complete_public_input_evidence')
    if (not isinstance(evidence,dict)
            or value.get('complete_public_input_evidence_identity_sha256')!=canonical(evidence)
            or evidence.get('current_files',{}).get('current_reference_bundle')!=reference_bundle):
        raise ValueError('The fixed target lacks its actual whole public reference binding')
    projection=full_reference_projection(evidence['current_files'],expected_model=actual_model)
    definitions=[[str(F(v['S_coefficient'])),str(F(v['constant']))] for v in node['true_scalar_nodes']]
    if definitions!=projection['exact_scalar_node_definitions']:
        raise ValueError('The supplied complete symbolic domain differs from this target')
    expected=freeze_target(producer_sha256=producer_sha256,evidence=evidence,projection=projection)
    if value!=expected:
        raise ValueError('The entire actual public fixed target changed')
    return dict(schema=TARGET_SCHEMA,definition_identity_sha256=canonical(value),
        public_input_binding_source_sha256=sha(__file__),
        actual_public_input_evidence_identity_sha256=canonical(evidence),
        actual_run_id=RUN_ID,actual_run_attempt=RUN_ATTEMPT,actual_reference_step_id=REFERENCE_STEP,
        current_reference_model_identity_sha256=canonical(actual_model),
        current_fixed_chart_core_sha256=projection['fixed_chart_core_array_record']['sha256'],
        historical_original_chart_core_sha256=ORIGIN_CHART_SHA,
        same_original_fixed_chart=projection['current_and_historical_fixed_chart_words_sha_equal'],
        same_mathematical_g_claimed=False,old_values_or_certificates_inherited=False)


def validate_compatibility(value,*,producer_sha256,actual_model,current_carrier,
        current_preparation_report,current_reference_bundle,current_node_report,current_scalar_input):
    """Every complete target/current file and original dc5 record is rebound."""
    if (not isinstance(value,dict) or value.get('schema')!=COMPATIBILITY_SCHEMA
            or value.get('producer_source_sha256')!=producer_sha256
            or value.get('public_input_binding_source_sha256')!=sha(__file__)
            or value.get('origin_envelope_source_sha256')!=ORIGIN_ENVELOPE_SHA
            or value.get('historical_warm_bundle_sha256')!=ORIGIN_WARM_SHA
            or value.get('complete_scalar_parameters_sha256')!=PARAMETERS_SHA
            or canonical(value.get('complete_scalar_parameters'))!=PARAMETERS_SHA
            or value.get('current_mesh_sha256')!=ORIGIN_MESH_SHA
            or value.get('historical_mesh_sha256')!=ORIGIN_MESH_SHA
            or value.get('historical_fixed_chart_core_sha256')!=ORIGIN_CHART_SHA
            or value.get('exact_node_recipe_source_sha256')!=WARM_SOURCE_SHA
            or value.get('consumed_warm_projection')!=list(CONSUMED_WARM_PROJECTION)
            or value.get('literal_width_hex')!=float(.05).hex()):
        raise ValueError('The actual public target/domain/source binding is incomplete')
    supplied=dict(current_carrier=current_carrier,current_preparation_report=current_preparation_report,
        current_reference_bundle=current_reference_bundle,current_node_report=current_node_report,
        current_scalar_input=current_scalar_input)
    files={k:valid_record(value.get(k),k,reread=True) for k in CURRENT_KEYS}
    if any(files[k]!=v for k,v in supplied.items()):
        raise ValueError('The consumer names another actual whole reference input')
    record_union(dict(files,**{k:value[k] for k in ('historical_carrier','historical_public_return',
        'current_public_return','current_warm_public_return','origin_envelope_source')}))
    for key in ('historical_carrier','historical_public_return','current_public_return',
            'current_warm_public_return','origin_envelope_source'):
        valid_record(value[key],key,reread=True)
    if (value['historical_carrier']['sha256']!=ORIGIN_CARRIER_SHA
            or value['historical_carrier']['bytes']!=ORIGIN_CARRIER_BYTES
            or value['historical_public_return']['sha256']!=ORIGIN_PUBLIC_SHA
            or value['origin_envelope_source']['sha256']!=ORIGIN_ENVELOPE_SHA):
        raise ValueError('The complete historical carrier/source evidence changed')
    target=value.get('fixed_target_definition')
    node=read_json(current_node_report,'current complete symbolic nodes')
    validation=validate_target(target,producer_sha256=producer_sha256,
        actual_model=actual_model,reference_bundle=current_reference_bundle,node=node)
    evidence=target['complete_public_input_evidence']
    if (evidence['current_files']!=files
            or value.get('actual_public_input_evidence')!=evidence
            or value.get('actual_public_input_evidence_identity_sha256')!=canonical(evidence)
            or value['current_public_return']!=evidence['complete_public_documents']['reference']['snapshot_record']
            or value['current_warm_public_return']!=evidence['complete_public_documents']['warm']['snapshot_record']
            or value.get('fixed_target_definition_identity_sha256')!=canonical(target)
            or value.get('actual_current_model_identity_sha256')!=canonical(actual_model)
            or value.get('actual_current_fixed_scalar_identity_sha256')!=actual_model['fixed_scalar_metric_identity_sha256']
            or value.get('current_fixed_chart_core_sha256')!=validation['current_fixed_chart_core_sha256']
            or value.get('fixed_core_first3_hex')!=target['fixed_chart_core_binary64_hex'][:3]
            or value.get('exact_symbolic_nodes_sha256')!=target['exact_scalar_node_definitions_identity_sha256']
            or value.get('same_original_fixed_chart')!=validation['same_original_fixed_chart']
            or value.get('current_and_historical_fixed_chart_words_sha_equal')!=validation['same_original_fixed_chart']):
        raise ValueError('The entire public input/target/current-file identity differs')
    for key in ('same_complete_scalar_formula_verified','complete_current_fixed_material_chart_verified',
            'same_complete_symbolic_domain_verified','full_original_carrier_sha_verified',
            'actual_current_warm_return_bound','all_original_carrier_members_reconstructed'):
        if value.get(key) is not True:
            raise ValueError('The complete input reconstruction obligation is unpaid: '+key)
    for key in ('same_mathematical_g_claimed','exact_old_to_new_chart_conjugacy_claimed',
            'historical_whole_warm_recreated','historical_whole_warm_or_height_equality_claimed',
            'old_metric_or_geometry_values_inherited','current_files_relabelled_as_historical'):
        if value.get(key) is not False:
            raise ValueError('No old target/field/geometry certificate may be relabelled: '+key)
    return dict(schema=COMPATIBILITY_SCHEMA,producer_source_sha256=producer_sha256,
        public_input_binding_source_sha256=sha(__file__),
        independent_fixed_target_binding_identity_sha256=canonical(value),
        actual_public_input_evidence_identity_sha256=canonical(evidence),
        actual_run_id=RUN_ID,actual_run_attempt=RUN_ATTEMPT,actual_reference_step_id=REFERENCE_STEP,
        actual_current_model_identity_sha256=canonical(actual_model),
        actual_current_warm_bundle_sha256=files['current_warm_bundle']['sha256'],
        historical_warm_bundle_sha256=ORIGIN_WARM_SHA,
        current_and_historical_whole_warm_equal=files['current_warm_bundle']['sha256']==ORIGIN_WARM_SHA,
        historical_whole_warm_or_height_equality_claimed=False,
        complete_scalar_parameters_sha256=PARAMETERS_SHA,current_mesh_sha256=ORIGIN_MESH_SHA,
        current_fixed_chart_core_sha256=validation['current_fixed_chart_core_sha256'],
        historical_original_chart_core_sha256=ORIGIN_CHART_SHA,
        fixed_target_definition_identity_sha256=canonical(target),
        independent_fixed_target=validation,same_original_fixed_chart=validation['same_original_fixed_chart'],
        same_mathematical_g_claimed=False,exact_symbolic_nodes_sha256=value['exact_symbolic_nodes_sha256'],
        historical_carrier_sha256=ORIGIN_CARRIER_SHA,historical_carrier_bytes=ORIGIN_CARRIER_BYTES,
        whole_old_carrier_and_full_current_input_bytes_rechecked=True,
        same_complete_scalar_formula=True,complete_current_fixed_chart_verified=True,
        all_historical_and_current_material_addresses_still_required=True,
        scientific_certificates_inherited=False)
