#!/usr/bin/env python3
"""Strict origin/current bridge for exact run10 reference continuation.

This standard-library module validates newly reconstructed files.  Run10's
e711 target and 081 reference model remain their original frozen definitions;
new scalar/node paths and execution records are never relabelled as run10.
The whole 512f reference and 71f carrier are regenerated numerical packs.
No physical field, root, derivative or certificate is evaluated here.
"""
import copy
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import re
import struct
import sys
import zipfile

SCHEMA='complete-same-run10-frozen-reference-input-bridge-v1'
PREPARATION_SCHEMA='complete-reconstructed-run10-reference-preparation-v1'
TARGET_SHA='e7110482f9bd2eb723e96c99f5bbaa8a85aa11a81519c5204a296fb1bad9a049'
TARGET_FILE_SHA='b24080447828d8ffb49ae146dd5672d34bf6f5cec512054633b6f849c2bdabfb'
EVIDENCE_SHA='47a8fa781713388379a6de4c259f4ddf7f810e1b3d69c63f8630565031b761ef'
MODEL_SHA='081bdf939b7bdc6d5dfb54bce955fdfbcda90a8cef3668388a8874272e594af5'
PROFILE_SHA='c46f875f96a41a09ccad4bcfb75ed6efd33e239b28dbcdb538ce9d2daa47bc65'
PARAMETERS_SHA='e640aec831df350fa69740650b723a7d2d55676ca64ffb5ddabbacb3ab7d6dfa'
MESH_SHA='eff967897039ec740c9aca49620253f27fb46d93cd8c59f4ed4759781ef88262'
CHART_SHA='90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e'
NODES_SHA='ba5a3188e048f69b6602b4b784640c70932fbc1f53cfbf13b0857ba25e6b4b02'
REFERENCE_SHA='4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3'
REFERENCE_FILE_SHA='512f13149c54b0cce9ca7b1d27fd4139493a480efcc824fe2e083d192d3a222b'
CARRIER_SHA='71f0048e2c6c973625fd110c6980c24242d2cf67b7dd7da5dd9e889fde26a22d'
OLD_CARRIER_SHA='dc5ffc55ecc4478d265bbad6e8f2abcf672709d99365e14ead01478a4042e7d0'
OLD_BINDER_NAME='actual_public_run10_reference_input_binding.py'
OLD_BINDER_SHA='9f69b860d4bf2e25e707d08c7c85ca01c17ebf468398ea007ad7448df9951209'
OLD_PRODUCER_SHA='fcd20177bed258bc463f5ca6431c29c18c3b381b75146e1da7bbc8bc4e7a475a'
WARM_SHA='bee5ae587bd519189b0b27c249987d80d82ab66822cd4f1ea4746a769f7fb3c3'
ORIGIN_PARAMETERS_SHA='d7c6fd9d571542f9c17f3ddc4e7ace589025ca74b69246c45b0c2e4239b8c088'
SCALAR_WIDTH='20705780131163723599438290019541571913013106551525357578680931811765776678181/14411518807585587200000000000000000000000000000000000000000000000000000000000000000000000'
CURRENT_KEYS=('current_warm_bundle','current_node_report','current_scalar_input',
    'current_carrier','current_preparation_report','current_reference_bundle')

def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for b in iter(lambda:stream.read(1<<20),b''):h.update(b)
    return h.hexdigest()

def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),
        allow_nan=False).encode()).hexdigest()

def record(path):
    p=Path(path).resolve()
    return dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size)

def digest(value,name):
    if not isinstance(value,str) or re.fullmatch(r'[0-9a-f]{64}',value) is None:
        raise ValueError('Complete SHA256 required: '+name)
    return value

def bound(value,name):
    if (not isinstance(value,dict) or set(value)!={'path','sha256','bytes'}
            or not isinstance(value['path'],str) or not Path(value['path']).is_absolute()
            or type(value['bytes']) is not int or value['bytes']<=0):
        raise ValueError('Complete actual file record required: '+name)
    digest(value['sha256'],name)
    if record(value['path'])!=value:raise ValueError('Actual file changed: '+name)
    return value

def read_json(value,name):
    bound(value,name)
    raw=Path(value['path']).read_bytes()
    if len(raw)!=value['bytes'] or hashlib.sha256(raw).hexdigest()!=value['sha256']:
        raise ValueError('Changed captured JSON bytes: '+name)
    return json.loads(raw)

def original_word_reader():
    path=Path(__file__).with_name(OLD_BINDER_NAME)
    if sha(path)!=OLD_BINDER_SHA:raise ValueError('Keep the full original primitive NPY reader')
    key='_same_run10_original_word_reader_'+OLD_BINDER_SHA[:16]
    module=sys.modules.get(key)
    if module is None:
        spec=importlib.util.spec_from_file_location(key,path)
        if spec is None or spec.loader is None:raise ValueError('Complete original pure source is required')
        module=importlib.util.module_from_spec(spec);sys.modules[key]=module;spec.loader.exec_module(module)
    for name in ('npy_member','member','string_member','chart_record'):
        if sha(getattr(module,name).__code__.co_filename)!=OLD_BINDER_SHA:
            raise ValueError('Changed actual complete primitive reader '+name)
    return module

def validate_origin_target(target):
    if (not isinstance(target,dict) or canonical(target)!=TARGET_SHA
            or hashlib.sha256((json.dumps(target,sort_keys=True,separators=(',',':'),allow_nan=False)+'\n').encode()).hexdigest()!=TARGET_FILE_SHA
            or target.get('schema')!='independently-frozen-actual-public-run10-scalar-and-material-chart-v1'
            or target.get('definition_source_sha256')!=OLD_PRODUCER_SHA
            or target.get('public_input_binding_source_sha256')!=OLD_BINDER_SHA
            or canonical(target.get('complete_public_input_evidence'))!=EVIDENCE_SHA
            or target.get('complete_public_input_evidence_identity_sha256')!=EVIDENCE_SHA
            or target.get('current_reference_model_identity_sha256')!=MODEL_SHA
            or canonical(target.get('complete_current_reference_model'))!=MODEL_SHA
            or target.get('complete_current_reference_bundle_sha256')!=REFERENCE_FILE_SHA
            or canonical(target.get('complete_scalar_parameters'))!=PARAMETERS_SHA
            or target.get('complete_scalar_parameters_identity_sha256')!=PARAMETERS_SHA
            or target.get('current_fixed_scalar_metric_identity_sha256')!=PROFILE_SHA
            or canonical(target.get('complete_current_fixed_scalar_profile_definition'))!=PROFILE_SHA
            or target.get('complete_literal_mesh_array_sha256')!=MESH_SHA
            or canonical(target.get('exact_scalar_node_definitions'))!=NODES_SHA
            or target.get('exact_scalar_node_definitions_identity_sha256')!=NODES_SHA):
        raise ValueError('Keep the entire genuinely recorded frozen run10 target as origin')
    reader=original_word_reader()
    if (reader.chart_record(target.get('fixed_chart_core_binary64_hex'))!=target.get('fixed_chart_core_array_record')
            or target['fixed_chart_core_array_record']['sha256']!=CHART_SHA):
        raise ValueError('All 160 original fixed-chart words must be retained')
    evidence=target['complete_public_input_evidence']
    if (evidence.get('actual_run_id')!='45972294636' or evidence.get('actual_run_attempt')!='1'
            or target.get('same_mathematical_g_claimed') is not False):
        raise ValueError('Do not rewrite the original target claim about its earlier historical input')
    return target

def current_projection(files,target):
    """Read ALL actual raw inputs; only exact formula/projection equality is used."""
    if not isinstance(files,dict) or set(files)!=set(CURRENT_KEYS):
        raise ValueError('Retain all six complete current inputs')
    for key,item in files.items():bound(item,key)
    reader=original_word_reader();model=target['complete_current_reference_model']
    with zipfile.ZipFile(files['current_warm_bundle']['path']) as z:
        if set(z.namelist())!={k+'.npy' for k in reader.WARM_MEMBERS}:
            raise ValueError('Retain all ten actual warm members')
        mesh=reader.member(z,'mesh','<f8',(923,))
        qraw=reader.member(z,'qjets','<f8',(923,3,482))
        core=qraw[8:161*8]
        first=reader.member(z,'fixed_core_first3','<f8',(3,))
        width=reader.member(z,'width','<f8',())
        warm_height=reader.member(z,'Hcap','<f8',())
        reader.member(z,'radius','<f8',())
    words=[v.hex() for (v,) in struct.iter_unpack('<d',core)]
    if (reader.array_sha('float64',(923,),mesh)!=MESH_SHA
            or words!=target['fixed_chart_core_binary64_hex'] or first!=core[:24]
            or struct.unpack('<d',width)[0].hex()!=target['exact_literal_width_hex']):
        raise ValueError('The new actual warm has not reproduced the fixed complete reference projection')
    node=read_json(files['current_node_report'],'current exact nodes')
    if (node.get('schema')!='fullclosed-hold-real-pulse-warm-v1'
            or node.get('source_sha256')!=WARM_SHA
            or node.get('bundle_sha256')!=files['current_warm_bundle']['sha256']
            or node.get('input_sha256')!=files['current_scalar_input']['sha256']
            or node.get('M')!=160 or node.get('J')!=923 or node.get('exact_core_affine') is not True):
        raise ValueError('The complete new node file must bind its real new warm and scalar')
    nodes=[[str(F(v['S_coefficient'])),str(F(v['constant']))] for v in node['true_scalar_nodes']]
    if nodes!=target['exact_scalar_node_definitions'] or canonical(nodes)!=NODES_SHA:
        raise ValueError('The full exact affine-in-S symbolic domain changed')
    raw=Path(files['current_scalar_input']['path']).read_bytes()
    if hashlib.sha256(raw).hexdigest()!=files['current_scalar_input']['sha256']:
        raise ValueError('Changed actual scalar payload')
    scalar=json.loads(gzip.decompress(raw) if raw[:2]==b'\x1f\x8b' else raw)
    parameters=dict(analytic_extension_origin=scalar['analytic_extension_origin'],
        geometry=scalar['fixed_scalar_profile']['geometry'])
    if parameters!=target['complete_scalar_parameters'] or canonical(parameters)!=PARAMETERS_SHA:
        raise ValueError('All exact scalar defining parameters must match the frozen run10 target')
    ref=files['current_reference_bundle'];carrier=files['current_carrier']
    if (ref['sha256']!=REFERENCE_FILE_SHA or ref['bytes']!=866207
            or carrier['sha256']!=CARRIER_SHA or carrier['bytes']!=227202):
        raise ValueError('Require the complete original numerical reference/carrier words, not only the recipe')
    arrays={}
    with zipfile.ZipFile(ref['path']) as z:
        if set(z.namelist())!={k+'.npy' for k in reader.REFERENCE_MEMBERS}:
            raise ValueError('Every original reference NPZ member is required')
        for name in reader.REFERENCE_MEMBERS:
            dtype,shape,data=reader.npy_member(z,name)
            arrays[name]=dict(dtype=dtype,shape=list(shape),sha256=hashlib.sha256(data).hexdigest(),bytes=len(data))
        if (json.loads(reader.string_member(z,'reference_model_json'))!=model
                or reader.string_member(z,'reference_model_identity_sha256')!=MODEL_SHA
                or reader.string_member(z,'schema')!=model['schema']
                or reader.member(z,'mesh','<f8',(923,))!=mesh
                or reader.member(z,'initial_core','<f8',(160,))!=core
                or reader.member(z,'fixed_core_first3','<f8',(3,))!=first
                or reader.member(z,'width','<f8',())!=width
                or reader.member(z,'original_warm_height','<f8',())!=warm_height):
            raise ValueError('The whole reference and new actual warm projection disagree')
        dtype,shape,cells=reader.npy_member(z,'cached_scalar_cells')
        if dtype!='<i8' or len(shape)!=1:raise ValueError('Complete scalar addresses required')
        local=reader.member(z,'cached_scalar_local','<f8',shape)
        values=reader.member(z,'cached_scalar_values','<f8',(shape[0],4))
        errors=reader.member(z,'cached_scalar_errors','<f8',(shape[0],4))
        if any(v<0 for (v,) in struct.iter_unpack('<d',errors)):
            raise ValueError('A complete scalar error bound is negative')
        addresses=set()
        for (cell,),(u,) in zip(struct.iter_unpack('<q',cells),struct.iter_unpack('<d',local)):
            if not 0<=cell<922 or not 0<=u<=1 or (cell,u.hex()) in addresses:
                raise ValueError('Invalid or duplicated actual complete scalar address')
            addresses.add((cell,u.hex()))
    with zipfile.ZipFile(carrier['path']) as z:
        if (reader.member(z,'mesh','<f8',(923,))!=mesh
                or reader.member(z,'width','<f8',())!=width
                or reader.member(z,'fixed_core_first3','<f8',(3,))!=first
                or reader.string_member(z,'fixed_scalar_metric_identity_sha256')!=PROFILE_SHA):
            raise ValueError('Whole current carrier differs from the frozen scalar/grid definition')
        a=reader.member(z,'a_observations','<f8',(7377,))
        if reader.array_sha('float64',(7377,),a)!=model['a_observations_sha256']:
            raise ValueError('All 7377 fixed scalar observations must retain their original words')
    for key,item in files.items():bound(item,key)
    return dict(complete_reference_member_payloads=arrays,
        current_actual_input_records=copy.deepcopy(files),complete_scalar_parameters_identity_sha256=PARAMETERS_SHA,
        complete_chart_array_sha256=CHART_SHA,complete_mesh_array_sha256=MESH_SHA,
        complete_exact_affine_nodes_identity_sha256=NODES_SHA,
        actual_scalar_cache_rows=len(addresses),all_reference_words_equal_to_origin=True,
        scalar_payload_whole_SHA_may_differ_but_exact_formula_is_verified=True)

def validate_bridge(value,*,expected_producer_source_sha256,current_files=None):
    digest(expected_producer_source_sha256,'complete actual reconstruction source')
    if (not isinstance(value,dict) or value.get('schema')!=SCHEMA
            or value.get('source_sha256')!=sha(__file__)
            or value.get('producer',{}).get('source_sha256')!=expected_producer_source_sha256
            or not re.fullmatch(r'[0-9a-f]{40}',str(value['producer'].get('source_commit','')))
            or value.get('origin_fixed_target_definition_identity_sha256')!=TARGET_SHA
            or value.get('fixed_target_definition_identity_sha256')!=TARGET_SHA
            or value.get('origin_execution_evidence_is_not_current_execution') is not True
            or value.get('current_files_relabelled_as_origin') is not False
            or value.get('old_field_values_or_scientific_certificates_inherited') is not False):
        raise ValueError('Require the full explicit origin/current continuation bridge')
    target=validate_origin_target(value.get('fixed_target_definition'))
    if value.get('origin_fixed_target_definition')!=target:
        raise ValueError('Do not substitute another inherited target object')
    files=value.get('current_files')
    if current_files is not None:
        for key,item in current_files.items():
            if key not in CURRENT_KEYS:raise ValueError('Unknown actual continuation input role')
            path=item['path'] if isinstance(item,dict) else item
            if Path(path).resolve()!=Path(files[key]['path']).resolve():
                raise ValueError('The caller uses another actual input path '+key)
            if isinstance(item,dict) and item!=files[key]:
                raise ValueError('The caller input record differs from the actual bridge '+key)
    projection=current_projection(files,target)
    preparation=read_json(files['current_preparation_report'],'complete current reconstruction report')
    if (preparation.get('schema')!=PREPARATION_SCHEMA
            or preparation.get('source_sha256')!=expected_producer_source_sha256
            or preparation.get('complete') is not True
            or preparation.get('reference_definition')!=target['complete_current_reference_model']
            or preparation.get('reference_model_identity_sha256')!=MODEL_SHA
            or preparation.get('origin_fixed_target_definition_identity_sha256')!=TARGET_SHA
            or preparation.get('fixed_scalar_metric_identity_sha256')!=PROFILE_SHA
            or preparation.get('original_reference_source_sha256')!=REFERENCE_SHA
            or preparation.get('origin_reference_definition_is_frozen_provenance') is not True):
        raise ValueError('The new report must truthfully identify the new constructor and original reference definition')
    expected={role:files['current_'+role] for role in
        ('reference_bundle','carrier','node_report','scalar_input')}
    if (preparation.get('input_for_solver')!=expected
            or preparation.get('old_warm_bundle')!=files['current_warm_bundle']
            or preparation.get('old_warm_node_report')!=files['current_node_report']
            or [preparation.get(k) for k in ('M','J','P','N')]!=[160,923,7377,2048]):
        raise ValueError('The new complete preparation input closure differs')
    actual=preparation.get('true_scalar',{})
    if (actual.get('definition')!=target['complete_current_fixed_scalar_profile_definition']
            or actual.get('model_identity_sha256')!=PROFILE_SHA
            or actual.get('integral_leaves')!=2218
            or actual.get('requested_integral_accuracy_reached') is not False
            or actual.get('all_tail_domain_included') is not True
            or actual.get('unresolved_oscillations_dropped') is not False
            or actual.get('integral_enclosure_width_exact')!=SCALAR_WIDTH):
        raise ValueError('The complete recorded 2218-leaf scalar table/accuracy status is required')
    execution=preparation.get('execution',{})
    if (execution!=value.get('current_execution')
            or execution.get('repository')!='Rogerhu12/math-research-public'
            or not str(execution.get('run_id','')).isdigit()
            or not str(execution.get('run_attempt','')).isdigit()
            or execution.get('run_id')=='45972294636'):
        raise ValueError('Use a genuinely separate declared public execution, never a renamed origin')
    for name in ('new_locations','complete_supplied_location_provenance'):
        bound(preparation[name],name)
    old=bound(value.get('origin_carrier'),'complete historical address carrier')
    if old['sha256']!=OLD_CARRIER_SHA or old['bytes']!=227202:
        raise ValueError('The whole historical dc5 address carrier remains required')
    if value.get('current_carrier')!=files['current_carrier']:
        raise ValueError('The material consumer and reference use different actual carriers')
    obligations=value.get('unresolved_parallel_history_obligations')
    if (not isinstance(obligations,list) or not obligations
            or not any(v.get('run_id')=='45972294636' and v.get('complete_report_or_typed_history_inferred') is False
                and v.get('unknown_history_is_empty') is False for v in obligations)):
        raise ValueError('Unknown later run10 state/history cannot be silently discarded')
    if value.get('complete_reference_member_payloads')!=projection['complete_reference_member_payloads']:
        raise ValueError('Every numerical reference member must keep its actual payload identity')
    for key,item in files.items():bound(item,key)
    return dict(schema=SCHEMA,source_sha256=sha(__file__),
        producer_source_sha256=expected_producer_source_sha256,
        actual_run_id=str(execution['run_id']),actual_run_attempt=str(execution['run_attempt']),
        origin_actual_run_id='45972294636',origin_actual_run_attempt='1',
        fixed_target_definition_identity_sha256=TARGET_SHA,
        actual_current_model_identity_sha256=MODEL_SHA,current_fixed_chart_core_sha256=CHART_SHA,
        actual_current_reference_bundle_sha256=REFERENCE_FILE_SHA,
        actual_current_carrier_sha256=CARRIER_SHA,
        current_input_records=copy.deepcopy(files),
        complete_reference_member_payloads=projection['complete_reference_member_payloads'],
        whole_old_carrier_and_full_current_input_bytes_rechecked=True,
        same_complete_scalar_formula=True,complete_current_fixed_chart_verified=True,
        same_mathematical_g_as_origin_run10_verified=True,
        same_finite_reference_words_as_origin_run10_verified=True,
        same_original_fixed_chart=True,same_mathematical_g_claimed=True,
        original_target_claim_about_pre_run10_history_rewritten=False,
        all_historical_and_current_material_addresses_still_required=True,
        unresolved_parallel_history_obligations=copy.deepcopy(obligations),
        current_provenance_is_not_origin_provenance=True,scientific_certificates_inherited=False)

def read_bridge(path,*,expected_producer_source_sha256,current_files=None):
    p=Path(path).resolve();before=record(p);value=read_json(before,'complete current continuation bridge')
    answer=validate_bridge(value,expected_producer_source_sha256=expected_producer_source_sha256,
        current_files=current_files)
    if record(p)!=before:raise ValueError('Complete continuation bridge changed during validation')
    answer['actual_binding_file']=before
    return value,answer
