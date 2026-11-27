#!/usr/bin/env python3
"""Pure complete binding for one predeclared fixed Fejer/R690 reference.

Only immutable files, literal array payloads and the complete declared recipe
are checked. No F/J/root, integral, matrix or field is evaluated. The complete
generic primitive NPY reader below is retained from the original published
9f69 source; no old run10 target or execution identity is accepted by this type.
"""
import ast
import copy
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import re
import struct
import sys
import zipfile

SCHEMA='complete-fixed-fejer-actual-reference-binding-v1'
TARGET_SCHEMA='complete-fixed-fejer-reference-definition-v1'
REFERENCE_SCHEMA='R690-fixed-fejer-axisymmetric-SO3-reference-input-v1'
PREPARATION_SCHEMA='R690-fixed-fejer-axisymmetric-SO3-preparation-v1'
REFERENCE_SOURCE_SHA='e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb'
REFERENCE_NAME='fixed_fejer_axisymmetric_reference.py'
MAKER_SOURCE_SHA='89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60'
MAKER_NAME='fixed_fejer_r690_reference_inputs.py'
SCALAR_PARAMETERS_SHA='e640aec831df350fa69740650b723a7d2d55676ca64ffb5ddabbacb3ab7d6dfa'
DEEP_SOURCE_SHA='e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2'
PRIMITIVE_WORD_READER_PARENT_SHA='9f69b860d4bf2e25e707d08c7c85ca01c17ebf468398ea007ad7448df9951209'
CURRENT_KEYS=('current_fixed_input_bundle','current_node_report','current_scalar_input',
    'current_carrier','current_preparation_report','current_reference_bundle')
REFERENCE_MEMBERS=('schema','mesh','initial_core','initial_height','radius','width',
    'fixed_core_first3','cached_scalar_cells','cached_scalar_local',
    'cached_scalar_values','cached_scalar_errors','reference_model_json',
    'reference_model_identity_sha256')

def sha(path):
    result=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda:stream.read(1048576),b''):result.update(block)
    return result.hexdigest()

def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),
        allow_nan=False).encode()).hexdigest()

def record(path):
    path=Path(path).resolve()
    return dict(path=str(path),sha256=sha(path),bytes=path.stat().st_size)

def bound(value,name):
    if (not isinstance(value,dict) or set(value)!={'path','sha256','bytes'}
            or not isinstance(value['path'],str) or type(value['bytes']) is not int
            or value['bytes']<0 or not re.fullmatch(r'[0-9a-f]{64}',str(value['sha256']))):
        raise ValueError('Keep a complete actual file record: '+name)
    if record(value['path'])!=value:raise ValueError('Changed complete actual file: '+name)
    return value

def read_json(value,name):
    bound(value,name)
    raw=Path(value['path']).read_bytes()
    if hashlib.sha256(raw).hexdigest()!=value['sha256'] or len(raw)!=value['bytes']:
        raise ValueError('Changed captured JSON bytes: '+name)
    return json.loads(raw)

def maker():
    path=Path(__file__).with_name(MAKER_NAME)
    if sha(path)!=MAKER_SOURCE_SHA:raise ValueError('The complete predeclared fixed-input source changed')
    key='_fixed_fejer_pure_input_recipe_'+MAKER_SOURCE_SHA
    module=sys.modules.get(key)
    if module is None:
        spec=importlib.util.spec_from_file_location(key,path)
        if spec is None or spec.loader is None:raise ValueError('Complete source required')
        module=importlib.util.module_from_spec(spec);sys.modules[key]=module;spec.loader.exec_module(module)
    for name in ('fixed_definition','chart_recipe','mathematical_target_recipe',
            'chart_coefficients','read_preparation','validate_preparation'):
        if sha(getattr(module,name).__code__.co_filename)!=MAKER_SOURCE_SHA:
            raise ValueError('The actual pure recipe function changed: '+name)
    return module

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


def array_sha(dtype,shape,raw):
    h=hashlib.sha256(dtype.encode())
    h.update(json.dumps(list(shape)).encode())
    h.update(raw)
    return h.hexdigest()


def validate_target_definition(target, *, recipe=None):
    source=maker() if recipe is None else recipe
    mathematical=source.mathematical_target_recipe()
    working=source.fixed_definition()
    if (not isinstance(target,dict) or target.get('schema')!=TARGET_SCHEMA
            or target.get('definition_source_sha256')!=REFERENCE_SOURCE_SHA
            or target.get('fixed_input_producer_source_sha256')!=MAKER_SOURCE_SHA
            or target.get('mathematical_target_recipe')!=mathematical
            or target.get('mathematical_target_identity_sha256')!=canonical(mathematical)
            or target.get('working_input_definition')!=working
            or target.get('working_input_definition_identity_sha256')!=canonical(working)
            or target.get('declared_new_target') is not True
            or target.get('same_previous_mathematical_g_claimed') is not False
            or target.get('previous_target_fields_roots_or_certificates_inherited') is not False
            or target.get('exact_chart_parameters_are_predeclared_RN_even_binary64_images') is not True):
        raise ValueError('The complete predeclared mathematical target and working input must remain distinct')
    model=target.get('complete_current_reference_model')
    if (not isinstance(model,dict) or model.get('schema')!=REFERENCE_SCHEMA
            or model.get('source_sha256')!=REFERENCE_SOURCE_SHA
            or canonical(model)!=target.get('current_reference_model_identity_sha256')
            or model.get('mathematical_target_recipe')!=mathematical
            or model.get('mathematical_target_identity_sha256')!=canonical(mathematical)
            or model.get('fixed_input_definition')!=working
            or model.get('fixed_input_definition_identity_sha256')!=canonical(working)
            or model.get('fixed_chart_recipe')!=source.chart_recipe()
            or model.get('predeclared_fixed_chart_from_rational_recipe') is not True
            or model.get('warm_or_BVP_core_consumed') is not False
            or model.get('same_previous_target_claimed') is not False
            or model.get('M')!=160 or model.get('J')!=923
            or model.get('working_scalar_integral_leaf_target')!=2218
            or model.get('seed_integration_order')!=8
            or model.get('all_original_free_core_coefficients_retained') is not True):
        raise ValueError('Keep the complete declared fixed reference and all current free variables')
    profile=model.get('fixed_scalar_profile_definition')
    if (not isinstance(profile,dict) or profile.get('schema')!='fullhold-deep-valley-flat-tail-input-v1'
            or profile.get('source_sha256')!=DEEP_SOURCE_SHA
            or canonical(profile)!=model.get('fixed_scalar_metric_identity_sha256')):
        raise ValueError('The complete R690 law and original scalar projection must remain explicit')
    return model

def current_projection(files,target, *, recipe=None):
    source=maker() if recipe is None else recipe
    model=validate_target_definition(target,recipe=source)
    if not isinstance(files,dict) or set(files)!=set(CURRENT_KEYS):
        raise ValueError('Retain all six actual fixed-reference input roles')
    for key,item in files.items():bound(item,key)
    with zipfile.ZipFile(files['current_fixed_input_bundle']['path']) as z:
        if set(z.namelist())!={k+'.npy' for k in
                ('mesh','initial_core','fixed_core_first3','radius','width','M','J')}:
            raise ValueError('Use the complete seven-member fixed input without old qjets')
        mesh=member(z,'mesh','<f8',(923,))
        core=member(z,'initial_core','<f8',(160,))
        first=member(z,'fixed_core_first3','<f8',(3,))
        width=member(z,'width','<f8',())
        member(z,'radius','<f8',())
        if (struct.unpack('<q',member(z,'M','<i8',()))[0]!=160
                or struct.unpack('<q',member(z,'J','<i8',()))[0]!=923):
            raise ValueError('The complete fixed reference layout changed')
    declared_words,_=source.chart_coefficients()
    expected=b''.join(struct.pack('<d',v) for v in declared_words)
    mesh_words=[v for (v,) in struct.iter_unpack('<d',mesh)]
    if (core!=expected or first!=core[:24] or width!=struct.pack('<d',.05)
            or mesh_words[0]!=0. or any(a>=b for a,b in zip(mesh_words,mesh_words[1:]))
            or array_sha('float64',(923,),mesh)!=model.get('mesh_sha256')
            or array_sha('float64',(160,),core)!=model.get('fixed_chart_core_sha256')
            or [v.hex() for (v,) in struct.iter_unpack('<d',first)]!=model.get('fixed_core_first3')):
        raise ValueError('Every actual Fejer coefficient and working mesh word must match its complete fixed definition')
    chart_record=dict(dtype='float64',shape=[160],sha256=array_sha('float64',(160,),core))
    if target.get('fixed_chart_core_array_record')!=chart_record:
        raise ValueError('Keep the actual full generated chart identity')
    node=read_json(files['current_node_report'],'complete deterministic nodes')
    if (node.get('schema')!=source.NODE_SCHEMA or node.get('source_sha256')!=MAKER_SOURCE_SHA
            or node.get('M')!=160 or node.get('J')!=923
            or node.get('exact_core_affine') is not True
            or node.get('chart_recipe')!=source.chart_recipe()
            or node.get('fixed_definition_identity_sha256')!=canonical(source.fixed_definition())
            or node.get('mathematical_target_identity_sha256')!=canonical(source.mathematical_target_recipe())):
        raise ValueError('Bind the complete declared exact domain and two input-definition levels')
    definitions=[[str(F(v['S_coefficient'])),str(F(v['constant']))] for v in node['true_scalar_nodes']]
    if len(definitions)!=923 or definitions[0]!=['0','0'] or definitions[-1]!=['1','0']:
        raise ValueError('Keep every complete exact affine-in-S node')
    scalar=read_json(files['current_scalar_input'],'complete fixed scalar')
    if set(scalar)!={'analytic_extension_origin','fixed_scalar_profile'}:
        raise ValueError('Use the complete stable scalar mathematical projection without mutable surface outputs')
    parameters=dict(analytic_extension_origin=scalar['analytic_extension_origin'],
        geometry=scalar['fixed_scalar_profile']['geometry'])
    if (set(scalar['fixed_scalar_profile'])!={'geometry'}
            or canonical(parameters)!=SCALAR_PARAMETERS_SHA
            or model.get('original_scalar_parameters_identity_sha256')!=SCALAR_PARAMETERS_SHA):
        raise ValueError('Every complete original scalar defining parameter must remain fixed')
    for key,role in (('fixed_input_bundle_sha256','current_fixed_input_bundle'),
                    ('scalar_input_sha256','current_scalar_input'),
                    ('symbolic_node_report_sha256','current_node_report'),
                    ('observation_carrier_sha256','current_carrier')):
        if model.get(key)!=files[role]['sha256']:
            raise ValueError('Reference model and actual fixed input disagree: '+key)
    profile=model['fixed_scalar_profile_definition']
    if profile.get('original_input',{}).get('scalar_input')!=files['current_scalar_input']['sha256']:
        raise ValueError('The complete accurate scalar law must bind its real stable parameter file')
    arrays={}
    with zipfile.ZipFile(files['current_reference_bundle']['path']) as z:
        if set(z.namelist())!={k+'.npy' for k in REFERENCE_MEMBERS}:
            raise ValueError('Every actual fixed reference member is required')
        for name in REFERENCE_MEMBERS:
            dtype,shape,data=npy_member(z,name)
            arrays[name]=dict(dtype=dtype,shape=list(shape),sha256=hashlib.sha256(data).hexdigest(),bytes=len(data))
        if (json.loads(string_member(z,'reference_model_json'))!=model
                or string_member(z,'reference_model_identity_sha256')!=canonical(model)
                or string_member(z,'schema')!=REFERENCE_SCHEMA
                or member(z,'mesh','<f8',(923,))!=mesh
                or member(z,'initial_core','<f8',(160,))!=core
                or member(z,'fixed_core_first3','<f8',(3,))!=first
                or member(z,'width','<f8',())!=width):
            raise ValueError('The whole complete reference disagrees with the declared input')
        height=member(z,'initial_height','<f8',())
        radius=member(z,'radius','<f8',())
        if struct.unpack('<d',radius)[0].hex()!=model.get('radius_carrier_hex'):
            raise ValueError('Use the actual complete R690 terminal radius')
        dtype,shape,cells=npy_member(z,'cached_scalar_cells')
        if dtype!='<i8' or len(shape)!=1:raise ValueError('Complete scalar address rows required')
        local=member(z,'cached_scalar_local','<f8',shape)
        member(z,'cached_scalar_values','<f8',(shape[0],4))
        errors=member(z,'cached_scalar_errors','<f8',(shape[0],4))
        if any(v<0 for (v,) in struct.iter_unpack('<d',errors)):
            raise ValueError('Negative complete scalar enclosure carrier')
        addresses=set()
        for (cell,),(u,) in zip(struct.iter_unpack('<q',cells),struct.iter_unpack('<d',local)):
            if not 0<=cell<922 or not 0<=u<=1 or (cell,u.hex()) in addresses:
                raise ValueError('Invalid or repeated complete cached scalar address')
            addresses.add((cell,u.hex()))
    with zipfile.ZipFile(files['current_carrier']['path']) as z:
        if (member(z,'mesh','<f8',(923,))!=mesh or member(z,'width','<f8',())!=width
                or member(z,'radius','<f8',())!=radius
                or member(z,'fixed_core_first3','<f8',(3,))!=first
                or string_member(z,'fixed_scalar_metric_identity_sha256')!=model['fixed_scalar_metric_identity_sha256']):
            raise ValueError('The current carrier and complete reference disagree')
        a=member(z,'a_observations','<f8',(7377,))
        if (array_sha('float64',(7377,),a)!=model['a_observations_sha256']
                or any(v<=0 for (v,) in struct.iter_unpack('<d',a))):
            raise ValueError('All 7377 positive scalar observations are required')
    if target['complete_current_reference_bundle_sha256']!=files['current_reference_bundle']['sha256']:
        raise ValueError('The full target and actual reference file differ')
    for key,item in files.items():bound(item,key)
    return dict(complete_reference_member_payloads=arrays,
        complete_generated_chart_array_sha256=chart_record['sha256'],
        complete_generated_mesh_array_sha256=array_sha('float64',(923,),mesh),
        complete_exact_affine_nodes_identity_sha256=canonical(definitions),
        complete_scalar_parameters_identity_sha256=SCALAR_PARAMETERS_SHA,
        actual_reference_height_hex=struct.unpack('<d',height)[0].hex(),
        actual_scalar_cache_rows=len(addresses),all_six_actual_files_rechecked=True)

def validate_binding(value, *, current_files=None):
    if sha(Path(__file__).with_name(REFERENCE_NAME))!=REFERENCE_SOURCE_SHA:
        raise ValueError('The full actual fixed-reference producer source differs')
    source=maker()
    if (not isinstance(value,dict) or value.get('schema')!=SCHEMA
            or value.get('producer',{}).get('source_sha256')!=REFERENCE_SOURCE_SHA
            or not re.fullmatch(r'[0-9a-f]{40}',str(value['producer'].get('source_commit','')))
            or value.get('all_current_six_files_are_actual') is not True
            or value.get('previous_fields_roots_certificates_or_unknown_typed_history_inherited') is not False):
        raise ValueError('Require the complete new-target reference binding and actual execution provenance')
    target=value.get('fixed_target_definition')
    model=validate_target_definition(target,recipe=source)
    if (value.get('fixed_target_definition_identity_sha256')!=canonical(target)
            or value.get('mathematical_target_identity_sha256')!=canonical(source.mathematical_target_recipe())):
        raise ValueError('The fixed mathematical target and complete reference identity changed')
    files=value.get('current_files')
    if current_files is not None:
        if not isinstance(current_files,dict) or not set(current_files)<=set(CURRENT_KEYS):
            raise ValueError('Only explicit complete fixed-input roles may be matched')
        for key,item in current_files.items():
            p=item['path'] if isinstance(item,dict) else item
            if Path(p).resolve()!=Path(files[key]['path']).resolve():
                raise ValueError('The caller uses another actual fixed input: '+key)
            if isinstance(item,dict) and item!=files[key]:
                raise ValueError('The supplied actual file record changed: '+key)
    projection=current_projection(files,target,recipe=source)
    preparation=read_json(files['current_preparation_report'],'actual complete fixed-reference preparation')
    if (preparation.get('schema')!=PREPARATION_SCHEMA
            or preparation.get('source_sha256')!=REFERENCE_SOURCE_SHA
            or preparation.get('complete') is not True
            or preparation.get('reference_definition')!=model
            or preparation.get('reference_model_identity_sha256')!=canonical(model)
            or preparation.get('fixed_target_definition')!=target
            or preparation.get('fixed_target_definition_identity_sha256')!=canonical(target)
            or preparation.get('mathematical_target_identity_sha256')!=value['mathematical_target_identity_sha256']
            or preparation.get('fixed_input_definition')!=source.fixed_definition()
            or preparation.get('fixed_input_definition_identity_sha256')!=canonical(source.fixed_definition())
            or preparation.get('fixed_input_bundle')!=files['current_fixed_input_bundle']
            or preparation.get('no_warm_BVP_or_optimized_old_chart_required') is not True
            or [preparation.get(k) for k in ('M','J','P','N')]!=[160,923,7377,2048]):
        raise ValueError('The complete actual preparation must belong to this exact declared target')
    expected={role:files['current_'+role] for role in
        ('reference_bundle','carrier','node_report','scalar_input')}
    if preparation.get('input_for_solver')!=expected:
        raise ValueError('The original complete reference input closure changed')
    table=preparation.get('true_scalar',{})
    if (table.get('definition')!=model['fixed_scalar_profile_definition']
            or table.get('model_identity_sha256')!=model['fixed_scalar_metric_identity_sha256']
            or table.get('integral_leaves')!=2218
            or table.get('all_tail_domain_included') is not True
            or table.get('unresolved_oscillations_dropped') is not False
            or type(table.get('requested_integral_accuracy_reached')) is not bool
            or preparation.get('deterministic_scalar_work')!=dict(leaf_target=2218,actual_leaves=2218,
                wall_clock_decides_leaf_count=False,all_original_integer_leaf_operations_retained=True)):
        raise ValueError('The full deterministic 2218-leaf scalar computation and its actual accuracy status are required')
    maker_report=read_json(value['fixed_input_preparation_report'],'actual fixed recipe producer report')
    if (preparation.get('fixed_input_preparation_report')!=value['fixed_input_preparation_report']
            or maker_report.get('schema')!=source.PREPARATION_SCHEMA
            or maker_report.get('source_sha256')!=MAKER_SOURCE_SHA or maker_report.get('complete') is not True
            or maker_report.get('definition')!=source.fixed_definition()
            or maker_report.get('definition_identity_sha256')!=canonical(source.fixed_definition())
            or maker_report.get('mathematical_target_recipe')!=source.mathematical_target_recipe()
            or maker_report.get('mathematical_target_identity_sha256')!=value['mathematical_target_identity_sha256']
            or maker_report.get('outputs')!={k:files[v] for k,v in
                (('fixed_input','current_fixed_input_bundle'),('node_report','current_node_report'),
                 ('scalar_input','current_scalar_input'))}):
        raise ValueError('Retain the actual complete fixed-input producer and all its output files')
    bound_maker,maker_checked=source.read_preparation(value['fixed_input_preparation_report']['path'],
        actual_outputs={k:files[v] for k,v in
            (('fixed_input','current_fixed_input_bundle'),('node_report','current_node_report'),
             ('scalar_input','current_scalar_input'))})
    if (bound_maker!=maker_report or maker_checked.get('actual_preparation_report')!=
            value['fixed_input_preparation_report'] or maker_checked.get('complete') is not True):
        raise ValueError('The complete original scalar/source and deterministic-node preparation changed')
    execution=preparation.get('execution',{})
    if (execution!=value['producer'].get('execution')
            or execution.get('repository')!='Rogerhu12/math-research-public'
            or not str(execution.get('run_id','')).isdigit()
            or not str(execution.get('run_attempt','')).isdigit()):
        raise ValueError('Use the actual public reference execution, not a fabricated future identity')
    for key in ('fixed_target_definition_file','new_locations','complete_supplied_location_provenance'):
        bound(value[key],key)
        if preparation.get(key)!=value[key]:raise ValueError('A complete preparation side file changed: '+key)
    if read_json(value['fixed_target_definition_file'],'whole fixed target')!=target:
        raise ValueError('The complete fixed-target file changed')
    for key,item in files.items():bound(item,key)
    return dict(schema=SCHEMA,source_sha256=sha(__file__),
        actual_run_id=str(execution['run_id']),actual_run_attempt=str(execution['run_attempt']),
        fixed_target_definition_identity_sha256=canonical(target),
        mathematical_target_identity_sha256=value['mathematical_target_identity_sha256'],
        actual_current_model_identity_sha256=canonical(model),
        current_fixed_chart_core_sha256=model['fixed_chart_core_sha256'],
        actual_current_reference_bundle_sha256=files['current_reference_bundle']['sha256'],
        current_input_records=copy.deepcopy(files),complete_projection=projection,
        complete_generated_fixed_chart_verified=True,complete_current_six_files_verified=True,
        predeclared_deterministic_mathematical_target=True,
        same_previous_mathematical_g_claimed=False,old_values_or_certificates_inherited=False,
        historical_literal_addresses_are_reinterpreted_not_same_physical_points=True,
        unknown_previous_target_history_reconstructed=False,
        independent_fixed_target=dict(definition_identity_sha256=canonical(target),
            mathematical_target_identity_sha256=value['mathematical_target_identity_sha256'],
            current_reference_model_identity_sha256=canonical(model),
            current_fixed_chart_core_sha256=model['fixed_chart_core_sha256'],
            same_previous_mathematical_g_claimed=False,old_values_or_certificates_inherited=False))

def read_binding(path, *, current_files=None):
    path=Path(path).resolve()
    raw=path.read_bytes()
    actual=dict(path=str(path),sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw))
    value=json.loads(raw)
    checked=validate_binding(value,current_files=current_files)
    if record(path)!=actual or path.read_bytes()!=raw:
        raise ValueError('The complete actual fixed-reference binding changed while being read')
    checked['actual_binding_file']=actual
    return value,checked
