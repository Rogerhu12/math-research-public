#!/usr/bin/env python3
"""Immutable records of ALREADY COMPUTED complete normal-chain cache words.

This independent recorder never evaluates a field, endpoint equation, root,
Jacobian, normal frame, or integral. Runtime copying is restricted to this
repository's public Actions. Pure metadata/file validation uses stdlib only.
Its packets are working numerical inputs, not root, derivative, branch,
quadrature, continuous-geometry, or same-field certificates.
"""
import ast
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path
import struct
import time
import uuid
import zipfile

SCHEMA = 'immutable-current-analytic-full-frame-normal-root-packets-v1'
PACKET_SCHEMA = 'actual-complete-normal-angle-cache-packet-v1'
POINT_SCHEMA = 'actual-normal-packet-current-free-point-v1'
SNAPSHOT_SCHEMA = 'actual-normal-packet-cache-snapshot-v1'
NORMALS = {
    '33c269f3cd04c9435ccb5144984124c8a0b6ae348f95c8bd71ac92a334c51cf4': dict(schema='complete-fixed-fejer-detached-meridian-values-normal-layer-v1',
        base='552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3',
        adjacent='bd65734da69f3e5bc560ec81df03f8555593257560455b56adfa353e025c4564',calibration='aa40b224da667b5e01b207a431f771e2bf11177fabaebb075ca6218bbb130de3',
        analytic='223afb992e0e9904c30ab20387a92569dc2979dbfde84f75f04e3402b9c5e811',analytic_frame='d3cf01067c0c3cd348560a74d1845b02f859bbd0a41f2938ec544034d2a63bcd',
        closure_values='2889fef0d09a32c3f609f9a4e100efb1b136070dad77c8104204b552a867c4e0'),
    '42b205ee34af4233002cec3d782acd78ed72a38f6013c1b931b3892f55d73e10': dict(schema='complete-fixed-fejer-reference-centred-immutable-point-closure-values-analytic-frame-J3-normal-layer-v1',
        base='552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3',
        adjacent='d04cf80d40a16410a2338f3b4b0c3bbdd0084cfc2ad5270bee21d33ded9449b5',calibration='fe36240c08ad32c4d4d665a387c70aaf02c0392419a51eef01e072081945e95c',
        analytic='7645268ee3538a43a4a04b73a5aee4fc5483b56962affeb0ba7e7f879d5d4a72',analytic_frame='75db2f20039b66a2784a922bf062e792328c0153fb0458c16acef92e0ab7e38c',
        closure_values='01ca74a9f00ac17ef4452173b758d785c0e06869efa98980426f822d4beeb595'),
    '1aa64d7731333f8ae008f86b717421abbbbfdb7f4c3edb1173f93754364bd778': dict(schema='complete-fixed-fejer-reference-centred-immutable-point-closure-values-analytic-frame-J3-normal-layer-v1',
        base='552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3',
        adjacent='257e5e44d38dffb82925a410c42e51f084cf7821a398b9928e543088a3f234c0',calibration='fe36240c08ad32c4d4d665a387c70aaf02c0392419a51eef01e072081945e95c',
        analytic='7645268ee3538a43a4a04b73a5aee4fc5483b56962affeb0ba7e7f879d5d4a72',analytic_frame='75db2f20039b66a2784a922bf062e792328c0153fb0458c16acef92e0ab7e38c',
        closure_values='01ca74a9f00ac17ef4452173b758d785c0e06869efa98980426f822d4beeb595'),
    '9bd394592f95668956c6718387b02d22d47c445b3f981f9101ae0e2c482594d6': dict(schema='complete-R711-reference-centred-immutable-point-closure-values-analytic-frame-J3-normal-layer-v1',
        base='6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865',
        adjacent='ab944e9c9af4b84a65d201a6cc997669a8f274077fc7e1f69ee35b268380bb59',calibration='794275121ee8d2f79972c5302012a10ba1fd8aa58fa5f67f05399825244fd238',
        analytic='21a929c14abfe5e66ca56c232d31b77d8f8e3a5e969d796c4601d1a1e1374024',analytic_frame='4e9b027b365752878069fa29671f8f549fa4cd9be478487b12ceeb64a908f8fa',
        closure_values='2543ee5db3ff15108fbdb4e340dad84301b94eecb773f757da4126ab86778cfb'),
    '6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4': dict(schema='complete-R711-reference-centred-detached-closure-values-analytic-frame-J3-normal-layer-v1',
        base='6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865',
        adjacent='6efb1b4de61635bb4121b2cc05daf4b817ecfb772f302568e2a570b7fa16b650',calibration='b59776d52653f036590b619124579a20400d3bb7a4de8117d3221ca32bec144f',
        analytic='9646c1cb1e239f4625dfaa0f13e0d0776dfd9684401789a089326e177c02a5aa',analytic_frame='8239fc8f3588afd4f93ba10368c599a85652d3b350a088b1397731c196258598',
        closure_values='e1af4fc8cfecbd30ab5cf9f7ded31d6a7a8d11385a8558cc76cbb8a8b1851e9e'),
    '3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc': dict(schema='complete-R711-reference-centred-analytic-frame-and-J3-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1',
        base='6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865',
        adjacent='3788b809c986668042e1c02f927afb85bf45434c4ff69607f9aaa2e2bf142695',calibration='fe422dbf2eac68bbc4f54e8fe290ba0e5d1b7a080f12f1d148cffe834957dba0',
        analytic='894efd3b277b8a8c1fbd4abcd68b573fb09ee10a706a90ded7b2e1894fe3b866',analytic_frame='4ed6dfb93bb15b864d79c227b852421bc69b888a32923b98a21fe816da5be3d8'),
    '04f1d2724e1d93f138d03c558262f53e1dd5433791c081c7f93c37eeab84e21e': dict(
        schema='complete-R711-reference-centred-analytic-J3-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1',
        base='6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865',
        adjacent='8a63cc1817fd0853c2b7ee69b64e3083de22106c239b62acc602ad9b69698787',
        calibration='4c3fb7a6d19a9c214e2dc69428456b62bc406c8329bc60083e1f5f8be3ff3d6d',
        analytic='64b39a8be75ee976dbf4b49768e4ebaf37a372f77dba397a439a054cc4e7465d'),
    'd5da5e3db88a03cc0afdc00e3a6bc74e425aa3f1b730ea7f66ac278f93d8e6eb': dict(
        schema='complete-R711-reference-centred-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1',
        base='6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865',
        adjacent='955dafdc865e34695489f4e8832ecb8a6d48e056f801ba119fd92e9097ad69b3',
        calibration='ccb3340e500a032943aaed084376136fd67ad81b222e1afbcc5e79d468f21ef8'),
    '8349fc52c9b2d399b2511d2af5f2cf23b8be284f7fa0ae12f28fc5bd7d1d3404': dict(
        schema='complete-R711-reference-centred-adjacent-frame-frequency-refined-SO3-fixed-normal-plane-six-control-layer-v1',
        base='41c865d9a505f4b7ac3b0b9c2b89a027235e78968b1f62cf7840bc119179efb2',
        adjacent='d6c0c90784a6335874afc183ac65cc6de868c3c8d8b0bf821f8cbb25789c2b34',
        calibration='688e111664eaca9f57803388f18f220c22d8bc6c4b9472589df2e06f3c8d9e47'),
    '9764c0c8df3558732d03cc03e793847f63e92c0690c440a3602fddf647cdc375': dict(
        schema='complete-R711-reference-centred-adjacent-frame-frequency-refined-SO3-fixed-normal-plane-six-control-layer-v1',
        base='e1f82aa5e397c9c6ac803796c198b761587bd4bc2ef3b797c24f2530b2e37f03',
        adjacent='e80936a0f49f0a8502e1dd4190635a7b70a1892d6c9d19b74fd286cfdd67d0da',
        calibration='5f9e772c4e6b017e617d9327c12efc6a434443833de25c1465515e7e9506d75a'),
}
ARRAY_SHAPES = dict(Z=(3,6),zero=(3,3),eta=(3,3),frame=(3,3,6),
                    controls=(3,6),J=(3,3))
METHODS = ('metadata','_select_point','_get_roots','_run_chain',
           '_implicit_jet_value','fields_torch')
RUNTIME_COUNTS = ('capture_calls_started','capture_calls_completed',
    'capture_calls_failed','point_files_created','point_files_reused',
    'angle_packets_created','angle_packets_reused','cache_angles_seen',
    'actual_J3_stage_blocks_copied','actual_J6_stage_blocks_copied',
    'actual_J9_stage_blocks_copied','snapshot_files_created',
    'scientific_field_calls','scientific_root_calls','scientific_J_calls')

def require_actions():
    if (os.environ.get('GITHUB_ACTIONS')!='true'
            or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise RuntimeError('Actual numerical-word recording requires public repository Actions')

def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as handle:
        for block in iter(lambda:handle.read(1024*1024),b''):h.update(block)
    return h.hexdigest()

def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),
        allow_nan=False).encode()).hexdigest()

def copy_json(value):
    return json.loads(json.dumps(value,allow_nan=False))

def digest(value):
    return isinstance(value,str) and len(value)==64 and all(c in '0123456789abcdef' for c in value)

def literal_angle(value):
    if (not isinstance(value,str) or not math.isfinite(float.fromhex(value))
            or float.fromhex(value).hex()!=value):
        raise ValueError('Keep the actual finite canonical binary64 angle word')
    return value

def file_record(path):
    path=Path(path).resolve()
    return dict(path=str(path),sha256=sha(path),bytes=path.stat().st_size)

def validate_file_record(value, *, reread=False):
    if (not isinstance(value,dict) or set(value)!=set(('path','sha256','bytes'))
            or not isinstance(value['path'],str) or not Path(value['path']).is_absolute()
            or not digest(value['sha256']) or type(value['bytes']) is not int or value['bytes']<=0):
        raise ValueError('Keep a complete actual immutable file record')
    if reread and file_record(value['path'])!=value:
        raise ValueError('An actual immutable packet file changed')
    return value

def read_json_record(value):
    validate_file_record(value)
    raw=Path(value['path']).read_bytes()
    if len(raw)!=value['bytes'] or hashlib.sha256(raw).hexdigest()!=value['sha256']:
        raise ValueError('The exact JSON snapshot changed')
    return json.loads(raw)

def definition():
    return dict(schema=SCHEMA,source_sha256=sha(__file__),
        supported_complete_operator_sources=copy_json(NORMALS),
        recorded_values='existing complete current-point cache only; every cached angle and every declared normal stage',
        copied_arrays=['complete current x','Z','zero','eta','frame','controls','J3','existing J6 or J9'],
        all_existing_cache_angles_recorded=True,
        supplied_required_angle_order_retained=True,
        cache_insertion_order_is_not_full_historical_batch_order=True,
        complete_original_stage_records_and_frame_provenance_retained=True,
        first_order_uncomputed_second_order_slots_are_not_actual_second_jets=True,
        absent_angular_matrices_are_recorded_as_absent=True,
        per_item_matrix_producer_choice_not_in_cache_is_not_inferred=True,
        no_field_root_J_frame_or_integral_evaluation=True,
        no_cache_upgrade_or_replacement=True,
        packet_point_need_not_be_accepted_outer_point=True,
        exact_file_bytes_and_source_bound_working_branch_identity=True,
        continuous_branch_identity_or_uniqueness_certified=False,
        derivative_root_or_quadrature_errors_paid=False,
        all_attempted_past_points_or_batches_recovered=False,
        instantaneous_current_cache_coverage_is_separate_from_all_domain_coverage=True,
        raw_numeric_arrays_remain_on_runner=True,
        actual_report_and_QP_return_hooks_bound=True,
        outer_point_and_current_cache_point_recorded_separately=True)

def _array_descriptor(name,shape,array_sha256,dtype='float64'):
    return dict(name=name,shape=list(shape),dtype=dtype,array_sha256=array_sha256)

def _validate_array_descriptors(value):
    if not isinstance(value,list) or not value:raise ValueError('Keep actual full array descriptors')
    names=[]
    for item in value:
        if (not isinstance(item,dict) or set(item)!=set(('name','shape','dtype','array_sha256'))
                or not isinstance(item['name'],str) or not item['name']
                or '/' in item['name'] or '\\' in item['name']
                or item['dtype'] not in ('float64','int64') or not digest(item['array_sha256'])
                or not isinstance(item['shape'],list)
                or any(type(n) is not int or n<=0 for n in item['shape'])):
            raise ValueError('An actual complete float64 array descriptor differs')
        names.append(item['name'])
    if len(set(names))!=len(names):raise ValueError('Packet array names must be unique')
    return {item['name']:item for item in value}

def _npy_words(stream,expected):
    if stream.read(6)!=b'\x93NUMPY':raise ValueError('Require a real NPY array member')
    version=tuple(stream.read(2))
    if version==(1,0):raw=stream.read(2);fmt='<H'
    elif version in ((2,0),(3,0)):raw=stream.read(4);fmt='<I'
    else:raise ValueError('Unsupported complete NPY member version')
    if len(raw)!=struct.calcsize(fmt):raise ValueError('Truncated NPY header size')
    size=struct.unpack(fmt,raw)[0]
    if not 0<size<=1024*1024:raise ValueError('Malformed NPY header')
    header=stream.read(size)
    if len(header)!=size:raise ValueError('Truncated NPY header')
    value=ast.literal_eval(header.decode('utf-8' if version==(3,0) else 'latin1').strip())
    shape=tuple(expected['shape'])
    if (set(value)!=set(('descr','fortran_order','shape')) or value['descr']!={'float64':'<f8','int64':'<i8'}[expected['dtype']]
            or value['fortran_order'] is not False or value['shape']!=shape):
        raise ValueError('Use the recorded complete C-order little-endian float64 words')
    h=hashlib.sha256(expected['dtype'].encode());h.update(json.dumps(list(shape)).encode())
    remaining=8*math.prod(shape)
    while remaining:
        block=stream.read(min(remaining,1024*1024))
        if not block:raise ValueError('Truncated actual array payload')
        h.update(block);remaining-=len(block)
    if stream.read(1) or h.hexdigest()!=expected['array_sha256']:
        raise ValueError('The immutable actual array words differ')
    return expected['array_sha256']

def validate_arrays_file(record,descriptors):
    """Hash/read recorded words only; no field or floating numerical algebra."""
    validate_file_record(record,reread=True);expected=_validate_array_descriptors(descriptors)
    with zipfile.ZipFile(record['path'],'r') as archive:
        names=archive.namelist()
        if len(names)!=len(expected) or set(names)!={k+'.npy' for k in expected}:
            raise ValueError('Keep every actual packet member, without extras or missing arrays')
        for name,item in expected.items():
            with archive.open(name+'.npy') as stream:_npy_words(stream,item)
    validate_file_record(record,reread=True)
    return dict(complete=True,array_count=len(expected),
        exact_recorded_words_rechecked=True,scientific_evaluations=0)

def _validate_partition(value,carriers):
    if (not isinstance(value,list) or len(value)<2
            or any(not isinstance(v,str) or str(Fraction(v))!=v for v in value)):
        raise ValueError('Keep the complete canonical exact common partition')
    nodes=[Fraction(v) for v in value]
    if (nodes[0]!=0 or nodes[-1]!=1 or any(a>=b for a,b in zip(nodes,nodes[1:]))
            or carriers!=[float(v).hex() for v in nodes]):
        raise ValueError('The exact partition or its declared working words differ')
    return len(nodes)-1

def _model_binding(value,model,operator_source,caller_sha):
    if (not digest(caller_sha) or canonical(model)!=value.get('model_identity_sha256')
            or operator_source not in NORMALS or model.get('source_sha256')!=operator_source
            or model.get('schema')!=NORMALS[operator_source]['schema']
            or value.get('operator_source_sha256')!=operator_source
            or value.get('caller_source_sha256')!=caller_sha
            or value.get('recorder_source_sha256')!=sha(__file__)
            or value.get('fixed_scalar_metric_identity_sha256')
                !=model['base_complete_model']['fixed_scalar_metric_identity_sha256']):
        raise ValueError('Bind the complete actual model, fixed metric and two real sources')

def validate_packet(value, *, model, operator_source_sha256, caller_source_sha256,
                    point_sha256, angle_hex, reread_arrays=False):
    if (not isinstance(value,dict) or value.get('schema')!=PACKET_SCHEMA
            or value.get('packet_identity_sha256')!=canonical(value.get('definition'))):
        raise ValueError('The complete immutable angle-packet identity differs')
    d=value['definition'];_model_binding(d,model,operator_source_sha256,caller_source_sha256)
    count=_validate_partition(d.get('exact_normal_step_nodes'),d.get('normal_step_carriers_hex'))
    if (d.get('exact_normal_step_nodes')!=model.get('exact_normal_step_nodes')
            or d.get('normal_step_carriers_hex')!=model.get('actual_normal_step_carriers_binary64_hex')
            or count!=model.get('normal_stage_count')):
        raise ValueError('The packet partition must be the complete actual model partition')
    order=d.get('actual_cached_angular_order')
    if (d.get('current_full_point_sha256')!=point_sha256 or not digest(point_sha256)
            or d.get('literal_angle_hex')!=literal_angle(angle_hex)
            or type(order) is not int or order not in (1,2)
            or d.get('normal_stage_count')!=count
            or len(d.get('stages',[]))!=count
            or d.get('all_original_declared_stages_present') is not True
            or d.get('actual_computed_angular_orders')!=list(range(order+1))
            or d.get('uncomputed_stored_angular_orders')!=list(range(order+1,3))
            or d.get('continuous_branch_certified') is not False
            or d.get('field_acceptance_inferred') is not False
            or d.get('per_item_angular_matrix_algorithm_choice')!='not_retained_in_original_cache'):
        raise ValueError('Keep exact own-point/order scope without inventing computed jets or branches')
    arrays=_validate_array_descriptors(d.get('arrays'));names={'Z','zero'}
    for name in names:
        if arrays.get(name,{}).get('shape')!=list(ARRAY_SHAPES[name]):
            raise ValueError('Keep all original root and zero-target jets')
    zero=hashlib.sha256(b'float64');zero.update(json.dumps([3,6]).encode());zero.update(bytes(3*6*8))
    previous=zero.hexdigest()
    protected_stages=[]
    for i,stage in enumerate(d['stages']):
        prefix='stage_'+str(i+1).zfill(3)+'_'
        if (stage.get('normal_stage_index')!=i+1
                or stage.get('exact_auxiliary_node')!=d['exact_normal_step_nodes'][i+1]
                or stage.get('actual_auxiliary_node_hex')!=d['normal_step_carriers_hex'][i+1]
                or not isinstance(stage.get('original_stage_record'),dict)):
            raise ValueError('Keep the original complete stage record at its exact fixed auxiliary node')
        for key in ('eta','frame','controls','J'):
            name=prefix+key;names.add(name)
            if arrays.get(name,{}).get('shape')!=list(ARRAY_SHAPES[key]):
                raise ValueError('A complete stage array is missing')
        prov=stage.get('frame_provenance')
        if (not isinstance(prov,dict)
                or prov.get('provenance_identity_sha256')!=canonical({
                    k:v for k,v in prov.items() if k!='provenance_identity_sha256'})
                or prov.get('current_full_point_sha256')!=point_sha256
                or prov.get('model_identity_sha256')!=canonical(model)
                or prov.get('operator_source_sha256')!=operator_source_sha256
                or prov.get('source_sha256')!=NORMALS[operator_source_sha256]['adjacent']
                or prov.get('literal_angle_hex')!=angle_hex
                or prov.get('normal_stage_index')!=i+1
                or prov.get('actual_root_angular_order')!=order
                or prov.get('actual_frame_all_three_jets_sha256')!=arrays[prefix+'frame']['array_sha256']
                or len(prov.get('jet_sources',[]))!=order+1):
            raise ValueError('The actual full frame/input provenance differs')
        if previous is not None and prov.get('current_previous_all_three_jets_sha256')!=previous:
            raise ValueError('The stage frame must retain all preceding selected-control words')
        protected_stages.append(dict(values={key:arrays[prefix+key]['array_sha256']
            for key in ('eta','frame','controls','J')},record=stage['original_stage_record'],frame_provenance=prov))
        previous=arrays[prefix+'controls']['array_sha256']
        matrix_order=stage.get('actual_cached_implicit_matrix_angular_order')
        if type(matrix_order) is not int or not 0<=matrix_order<=order:
            raise ValueError('Keep the actual independently recorded matrix order')
        matrix_name=stage.get('angular_matrix_array')
        if matrix_order==0:
            if matrix_name is not None:raise ValueError('An uncomputed angular matrix must stay absent')
        else:
            name=prefix+'jacobian';names.add(name)
            if matrix_name!=name or arrays.get(name,{}).get('shape')!=[3*(matrix_order+1)]*2:
                raise ValueError('Keep the actual complete J6/J9; do not fill a missing matrix')
    if (set(arrays)!=names or arrays['Z']['array_sha256']!=previous
            or any(a['dtype']!='float64' for a in arrays.values())):
        raise ValueError('The full last-stage control and root packet differ')
    record=d.get('original_root_record',{})
    protected=canonical([dict(literal_angle_hex=angle_hex,actual_root_order=order,
        Z=arrays['Z']['array_sha256'],zero=arrays['zero']['array_sha256'],record=record,stages=protected_stages)])
    if protected!=d.get('original_protected_root_fields_sha256'):
        raise ValueError('Keep the complete original selected-root protection identity')
    if (record.get('all_normal_stages_returned') is not True
            or record.get('normal_stage_count')!=count
            or record.get('exact_normal_step_nodes')!=d['exact_normal_step_nodes']
            or record.get('final_original_physical_endpoint_equation_checked') is not True
            or d.get('computed_physical_angular_endpoint_residual_norms')
                !=record.get('physical_angular_endpoint_residual_norms',[])[:order+1]):
        raise ValueError('Retain the real final original endpoint read and computed residual orders')
    validate_file_record(value.get('arrays_file'),reread=reread_arrays)
    if reread_arrays:validate_arrays_file(value['arrays_file'],d['arrays'])
    return dict(packet_identity_sha256=value['packet_identity_sha256'],
        current_full_point_sha256=point_sha256,literal_angle_hex=angle_hex,
        actual_cached_angular_order=order,normal_stage_count=count,
        actual_J6_stage_blocks=sum(s['actual_cached_implicit_matrix_angular_order']==1 for s in d['stages']),
        actual_J9_stage_blocks=sum(s['actual_cached_implicit_matrix_angular_order']==2 for s in d['stages']),
        all_stages_recorded=True,continuous_branch_certified=False,scientific_evaluations=0)

def validate_snapshot(value, *, model, operator_source_sha256,
                      caller_source_sha256, reread_packets=False, reread_arrays=False):
    if (not isinstance(value,dict) or value.get('schema')!=SNAPSHOT_SCHEMA
            or value.get('snapshot_identity_sha256')!=canonical(value.get('definition'))):
        raise ValueError('The immutable snapshot identity differs')
    d=value['definition'];_model_binding(d,model,operator_source_sha256,caller_source_sha256)
    if (type(d.get('capture_ordinal')) is not int or d['capture_ordinal']<1
            or not isinstance(d.get('snapshot_label'),str) or not d['snapshot_label']):
        raise ValueError('Keep the actual capture ordinal and hook label')
    point=d.get('current_full_point_sha256')
    if point is not None and not digest(point):raise ValueError('Retain actual current point or honest None')
    required=d.get('required_literal_angle_hex')
    cache=d.get('cache_literal_angle_hex')
    if (not isinstance(required,list) or not isinstance(cache,list)
            or len(set(required))!=len(required) or len(set(cache))!=len(cache)):
        raise ValueError('Keep exact unique angle lists in their supplied/cache order')
    for angle in required+cache:literal_angle(angle)
    if d.get('cached_angle_count')!=len(cache) or len(d.get('angle_packets',[]))!=len(cache):
        raise ValueError('Each actually cached angle needs its complete packet')
    if point is None:
        if cache or d.get('current_point_file') is not None:
            raise ValueError('A not-yet-selected point must have no numerical packet')
    else:
        p=d.get('current_point_file')
        if (not isinstance(p,dict) or p.get('schema')!=POINT_SCHEMA
                or p.get('current_full_point_sha256')!=point
                or p.get('model_identity_sha256')!=canonical(model)
                or p.get('array',{}).get('array_sha256')!=point
                or p['array'].get('dtype')!='float64'
                or p['array'].get('name')!='x'):
            raise ValueError('Keep the entire selected free point, not just its digest')
        validate_file_record(p['arrays_file'],reread=reread_packets)
        if reread_arrays:validate_arrays_file(p['arrays_file'],[p['array']])
    roots2=[];matrices2=[]
    for angle,item in zip(cache,d['angle_packets']):
        if (item.get('literal_angle_hex')!=angle or not digest(item.get('packet_identity_sha256'))
                or item.get('actual_cached_angular_order') not in (1,2)
                or type(item.get('actual_cached_angular_order')) is not int
                or type(item.get('all_stages_have_second_order_implicit_matrix')) is not bool):
            raise ValueError('Keep actual per-angle root/matrix order in original cache insertion order')
        validate_file_record(item['packet_file'],reread=reread_packets)
        if reread_packets:
            packet=read_json_record(item['packet_file'])
            out=validate_packet(packet,model=model,operator_source_sha256=operator_source_sha256,
                caller_source_sha256=caller_source_sha256,point_sha256=point,angle_hex=angle,
                reread_arrays=reread_arrays)
            if (out['packet_identity_sha256']!=item['packet_identity_sha256']
                    or out['actual_cached_angular_order']!=item['actual_cached_angular_order']
                    or (out['actual_J9_stage_blocks']==out['normal_stage_count'])
                        !=item['all_stages_have_second_order_implicit_matrix']):
                raise ValueError('The immutable angle packet differs from the snapshot')
        if item['actual_cached_angular_order']==2:roots2.append(angle)
        if item['all_stages_have_second_order_implicit_matrix']:matrices2.append(angle)
    missing=[a for a in required if a not in set(cache)]
    if (d.get('missing_required_literal_angle_hex')!=missing
            or d.get('all_required_angle_roots_recorded')!=(point is not None and not missing)
            or d.get('all_required_second_angular_roots_recorded')!=(point is not None and set(required)<=set(roots2))
            or d.get('all_required_second_angular_implicit_matrices_recorded')
                !=(point is not None and set(required)<=set(matrices2))
            or d.get('current_point_and_cache_unchanged_during_capture') is not True
            or d.get('scientific_counts_before')!=d.get('scientific_counts_after')
            or d.get('actual_scientific_evaluations_by_recorder')!=0
            or d.get('continuous_branch_or_field_certified') is not False
            or d.get('accepted_outer_point_inferred_from_cache') is not False):
        raise ValueError('Keep actual coverage separate from hypothetical fields or matrices')
    validate_file_record(d['operator_metadata_snapshot'],reread=reread_packets)
    if reread_packets:
        meta=read_json_record(d['operator_metadata_snapshot'])
        if (meta.get('source_sha256')!=operator_source_sha256
                or meta.get('model_identity_sha256')!=canonical(model)
                or meta.get('model')!=model
                or meta.get('current_full_point_sha256')!=point
                or meta.get('current_cached_angle_roots')!=len(cache)):
            raise ValueError('Keep the exact existing metadata snapshot at the same point')
    calibration=d.get('actual_reference_calibration_files')
    if not isinstance(calibration,list):raise ValueError('Keep all existing calibration cache records')
    for item in calibration:
        old=item.get('original_complete_record',{})
        source={key:old.get(key) for key in ('path','sha256','bytes')}
        validate_file_record(source)
        validate_file_record(item.get('immutable_copy'),reread=reread_packets)
        if (item['immutable_copy']['sha256']!=source['sha256']
                or item['immutable_copy']['bytes']!=source['bytes']
                or item.get('unchanged_whole_file_bytes') is not True
                or item.get('reference_defect_or_core_cap_recomputed') is not False):
            raise ValueError('Do not replace an original reference defect cache by a reconstruction')
    if reread_packets and [c['original_complete_record'] for c in calibration]!=meta.get(
            'reference_centering',{}).get('actual_reference_records'):
        raise ValueError('Preserve every actually recorded reference calibration batch')
    return dict(snapshot_identity_sha256=value['snapshot_identity_sha256'],
        capture_ordinal=d['capture_ordinal'],snapshot_label=d['snapshot_label'],
        current_full_point_sha256=point,cached_angle_count=len(cache),
        required_angle_count=len(required),missing_required_angle_count=len(missing),
        all_required_angle_roots_recorded=d['all_required_angle_roots_recorded'],
        all_required_second_angular_roots_recorded=d['all_required_second_angular_roots_recorded'],
        all_required_second_angular_implicit_matrices_recorded=d['all_required_second_angular_implicit_matrices_recorded'],
        continuous_branch_or_field_certified=False,scientific_evaluations=0)

def validate_metadata(value, *, model, operator_source_sha256, caller_source_sha256,
                      source_sha256_by_role, reread_packets=False, reread_arrays=False):
    """Pure source-bound reader interface; does not import NumPy or Torch."""
    if (not isinstance(value,dict) or value.get('schema')!=SCHEMA
            or value.get('definition')!=definition()
            or value.get('definition_identity_sha256')!=canonical(definition())
            or value.get('source_sha256')!=sha(__file__)
            or value.get('model_identity_sha256')!=canonical(model)
            or value.get('operator_source_sha256')!=operator_source_sha256
            or value.get('caller_source_sha256')!=caller_source_sha256
            or value.get('source_sha256_by_role')!=source_sha256_by_role
            or source_sha256_by_role.get('root_packets')!=sha(__file__)):
        raise ValueError('Use the complete independently bound recorder, caller and source closure')
    counts=value.get('actual_recorder_counts')
    if (not isinstance(counts,dict) or set(counts)!=set(RUNTIME_COUNTS)
            or any(type(v) is not int or v<0 for v in counts.values())
            or counts['capture_calls_started']!=counts['capture_calls_completed']+counts['capture_calls_failed']
            or any(counts[k]!=0 for k in ('scientific_field_calls','scientific_root_calls','scientific_J_calls'))):
        raise ValueError('Keep actual recorder operations separate from zero scientific calls')
    snapshots=value.get('snapshots')
    if (not isinstance(snapshots,list) or len(snapshots)!=counts['capture_calls_completed']
            or counts['snapshot_files_created']!=counts['capture_calls_completed']):
        raise ValueError('Keep every successful immutable capture and every actual failed capture')
    actual=[]
    for item in snapshots:
        if (not isinstance(item,dict) or not digest(item.get('snapshot_identity_sha256'))
                or not isinstance(item.get('summary'),dict)):
            raise ValueError('Keep the full ordered capture index')
        validate_file_record(item['snapshot_file'],reread=reread_packets)
        if reread_packets:
            snapshot=read_json_record(item['snapshot_file'])
            summary=validate_snapshot(snapshot,model=model,operator_source_sha256=operator_source_sha256,
                caller_source_sha256=caller_source_sha256,reread_packets=True,reread_arrays=reread_arrays)
            if summary!=item['summary'] or summary['snapshot_identity_sha256']!=item['snapshot_identity_sha256']:
                raise ValueError('The entire actual capture summary changed')
        actual.append(item['summary'])
    last=value.get('latest_complete_capture')
    if last!=(actual[-1] if actual else None):
        raise ValueError('Do not replace a missing latest complete capture by a synthetic result')
    carrier=value.get('fixed_working_carrier')
    if not isinstance(carrier,dict) or carrier.get('model_identity_sha256')!=canonical(model):
        raise ValueError('Keep the full actual integration carriers')
    validate_file_record(carrier['arrays_file'],reread=reread_packets)
    _validate_array_descriptors(carrier['arrays'])
    if reread_arrays:validate_arrays_file(carrier['arrays_file'],carrier['arrays'])
    seconds=value.get('capture_seconds')
    if isinstance(seconds,bool) or not isinstance(seconds,(int,float)) or not math.isfinite(seconds) or seconds<0:
        raise ValueError('Keep actual finite recording time')
    for key,expected in (
            ('no_scientific_evaluations',True),('old_scientific_methods_changed',False),
            ('actual_query_integration_words_recorded',True),
            ('all_past_root_attempts_recovered',False),('field_acceptance_claimed',False),
            ('continuous_branch_certified',False),('root_or_quadrature_or_derivative_errors_paid',False),
            ('full_current_meridian_arrays_recorded',False)):
        if value.get(key) is not expected:raise ValueError('Preserve the precise record-only scope: '+key)
    return dict(schema=SCHEMA,source_sha256=sha(__file__),
        definition_identity_sha256=value['definition_identity_sha256'],
        model_identity_sha256=canonical(model),operator_source_sha256=operator_source_sha256,
        caller_source_sha256=caller_source_sha256,actual_recorder_counts=copy_json(counts),
        capture_seconds=seconds,latest_complete_capture=copy_json(last),
        latest_capture_failure=copy_json(value.get('latest_capture_failure')),
        immutable_snapshot_count=len(snapshots),no_scientific_evaluations=True,
        root_or_quadrature_or_derivative_errors_paid=False,continuous_branch_certified=False)

ENTRY_CAPTURE_SCHEMA = 'actual-normal-root-packet-entry-capture-v1'

def validate_entry_capture(value, *, metadata, expected_label=None, expected_outer_point=None):
    if (not isinstance(value,dict) or value.get('schema')!=ENTRY_CAPTURE_SCHEMA
            or not digest(value.get('outer_full_point_sha256'))
            or value.get('current_cache_full_point_sha256') is not None
                and not digest(value['current_cache_full_point_sha256'])
            or type(value.get('capture_ordinal')) is not int or value['capture_ordinal']<1
            or value.get('capture_ordinal')>metadata['actual_recorder_counts']['capture_calls_started']
            or type(value.get('capture_completed')) is not bool
            or not isinstance(value.get('label'),str) or not value['label']
            or value.get('actual_scientific_evaluations_by_recorder')!=0
            or value.get('cache_point_is_not_assumed_accepted_outer_point') is not True
            or value.get('current_cache_equals_outer_point')!=
                (value['current_cache_full_point_sha256']==value['outer_full_point_sha256'])):
        raise ValueError('Bind the actual capture and outer point without inventing cache acceptance')
    if expected_label is not None and value['label']!=expected_label:
        raise ValueError('Keep the exact actual entry hook label')
    if expected_outer_point is not None and value['outer_full_point_sha256']!=expected_outer_point:
        raise ValueError('The entry capture is not associated with its actual full outer point')
    matching=[item for item in metadata['snapshots']
              if item['summary']['capture_ordinal']==value['capture_ordinal']]
    snapshot=value.get('snapshot')
    failure=value.get('capture_failure')
    if value['capture_completed']:
        if len(matching)!=1 or snapshot!=matching[0] or failure is not None:
            raise ValueError('A completed entry hook must select its own immutable capture')
        actual=snapshot['summary']
        if (actual['snapshot_label']!=value['label']
                or actual['current_full_point_sha256']!=value['current_cache_full_point_sha256']):
            raise ValueError('Do not associate another point or past completed capture with this hook')
    else:
        actual=None
        if (matching or snapshot is not None or not isinstance(failure,dict)
                or failure.get('capture_ordinal')!=value['capture_ordinal']
                or failure.get('actual_current_full_point_sha256')!=value['current_cache_full_point_sha256']
                or not isinstance(failure.get('type'),str) or not failure['type']
                or not isinstance(failure.get('message'),str)
                or failure.get('incomplete_capture_not_counted_as_complete') is not True
                or failure.get('science_was_not_restarted_or_recomputed') is not True):
            raise ValueError('A failed capture must remain an explicit incomplete record')
    return dict(capture_ordinal=value['capture_ordinal'],label=value['label'],
        capture_completed=value['capture_completed'],
        outer_full_point_sha256=value['outer_full_point_sha256'],
        current_cache_full_point_sha256=value['current_cache_full_point_sha256'],
        current_cache_equals_outer_point=value['current_cache_equals_outer_point'],
        actual_complete_snapshot=copy_json(actual),capture_failure=copy_json(failure),
        actual_scientific_evaluations_by_recorder=0,
        root_or_quadrature_or_derivative_errors_paid=False)

def validate_entry_report(report, *, reread_packets=True, reread_arrays=True):
    """Pure whole-entry reader: fixed sources, every QP hook, and the last report hook."""
    model=report['representation'];roles=report['source_sha256_by_role']
    if (roles.get('root_packets')!=sha(__file__)
            or report.get('normal_root_packet_source',{}).get('sha256')!=sha(__file__)
            or report.get('normal_root_packet_definition')!=definition()
            or report.get('normal_root_packet_record_only') is not True):
        raise ValueError('Keep the complete independently bound record-only entry source')
    metadata=report['normal_root_packets']
    answer=validate_metadata(metadata,model=model,operator_source_sha256=roles['endpoint'],
        caller_source_sha256=report['source_sha256'],source_sha256_by_role=roles,
        reread_packets=reread_packets,reread_arrays=reread_arrays)
    latest=report.get('normal_root_packet_latest_entry_capture')
    counts=metadata['actual_recorder_counts']
    if latest is None:
        if counts['capture_calls_started'] or report.get('complete') is True:
            raise ValueError('Only a genuinely not-yet-captured initial report has no entry capture')
        latest_answer=None
    else:
        if latest['capture_ordinal']!=counts['capture_calls_started']:
            raise ValueError('Retain the last actual report-save capture, including an I/O failure')
        expected=None
        if report.get('complete') is True:
            expected=(report.get('final_geometry') or {}).get('current_full_point_sha256')
            if not digest(expected):raise ValueError('Bind a complete report to its actual final field point')
        elif report.get('actual_initial_read_error') is not None:
            expected=report.get('initial_full_variable_point_sha256')
            if not digest(expected):raise ValueError('Bind the actual failed initial field point')
        latest_answer=validate_entry_capture(latest,metadata=metadata,
            expected_label='actual-report-save',expected_outer_point=expected)
        actual_metadata=report.get('latest_operator_metadata')
        if not isinstance(actual_metadata,dict) or actual_metadata.get('current_full_point_sha256')!=latest[
                'current_cache_full_point_sha256']:
            raise ValueError('The report and last captured operator metadata must share the actual cache point')
    qp_returns=[]
    for phase in ('metric','restoration'):
        for item in report.get(phase+'_directions',[]):
            expected=(item.get('starting_geometry') or {}).get('current_full_point_sha256')
            if not digest(expected):raise ValueError('Every completed QP has its actual same-parent geometry')
            value=validate_entry_capture(item.get('normal_root_packet_at_QP_return'),metadata=metadata,
                expected_label=phase+'-QP-return-'+str(item['serial']),expected_outer_point=expected)
            value.update(phase=phase,index=item['index'],serial=item['serial'])
            qp_returns.append(value)
    ordinals=[v['capture_ordinal'] for v in qp_returns]
    if len(set(ordinals))!=len(ordinals):
        raise ValueError('Keep distinct actual captures at every separately completed QP')
    answer.update(latest_entry_capture=latest_answer,actual_QP_return_captures=qp_returns,
        complete_original_QP_logic_unchanged=True,complete_original_true_screening_unchanged=True,
        extra_field_or_root_or_J_calls=0,
        immutable_words_are_not_outward_error_bounds=True)
    return answer

def _atomic_bytes(path,raw):
    path=Path(path)
    if path.exists():
        if path.read_bytes()!=raw:raise ValueError('Never overwrite an existing different immutable record')
        return file_record(path),False
    tmp=path.with_name('.'+path.name+'.'+uuid.uuid4().hex+'.tmp')
    try:
        with tmp.open('xb') as handle:
            handle.write(raw);handle.flush();os.fsync(handle.fileno())
        try:os.link(tmp,path)
        except FileExistsError:
            if path.read_bytes()!=raw:raise ValueError('A concurrent immutable record differs')
    finally:
        if tmp.exists():tmp.unlink()
    return file_record(path),True

def _json_bytes(value):
    return (json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False)+'\n').encode()

def _load_pins(path):
    tree=ast.parse(Path(path).read_bytes())
    values=[ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign)
        and len(n.targets)==1 and isinstance(n.targets[0],ast.Name) and n.targets[0].id=='SOURCE_PINS']
    if len(values)!=1 or not isinstance(values[0],dict):raise ValueError('Bind one complete actual caller source table')
    return values[0]

def _scientific_counts(q):
    value=dict(field=q.counts,endpoint=q.endpoint_counts,normal=q.normal_counts,
        frame=q.frame_c1.counts,stage=q.stage_matrices.counts,adjacent=q.adjacent_frames.counts)
    spec=NORMALS[q.model['source_sha256']]
    if 'analytic' in spec:value['analytic_stage_jacobian']=q.analytic_stage_jacobian.counts
    if 'analytic_frame' in spec:value['analytic_normal_frame']=q.analytic_normal_frame.counts
    if 'closure_values' in spec:value['detached_closure_values']=q.detached_closure_values.counts
    return copy_json(value)

def _angles(q,witnesses,radius_witnesses):
    answer=[];seen=set()
    for value in q.phi:
        key=literal_angle(float(value).hex())
        if key not in seen:seen.add(key);answer.append(key)
    for group in (witnesses,radius_witnesses):
        # The complete actual memory/driver return dictionaries. Read named
        # physical coordinates only; never rewrite role/protected metadata,
        # re-normalize an angle, or change the caller's point deduplication.
        locations=[]
        for value in group:
            if not isinstance(value,dict) or not {'cell','u','phi'}<=set(value):
                raise ValueError('Keep the actual literal-location dictionary interface')
            cell,u,phi=value['cell'],float(value['u']),float(value['phi'])
            if (type(cell) is not int or not 0<=cell<q.J-1 or not math.isfinite(u)
                    or not 0<=u<=1 or not math.isfinite(phi)):
                raise ValueError('Keep every supplied finite complete literal physical location')
            locations.append((cell,u,phi))
        for cell,u,phi in sorted(locations,key=lambda p:(p[0],p[1].hex(),p[2].hex())):
            key=literal_angle(phi.hex())
            if key not in seen:seen.add(key);answer.append(key)
    return answer

class NormalRootPacketRecorder:
    """Source-bound snapshots of existing cache words; no callbacks to science."""
    def __init__(self,q,*,repo,outdir,caller_source,source_paths):
        require_actions()
        import numpy as np
        self.np=np;self.q=q;self.repo=Path(repo).resolve();self.outdir=Path(outdir).resolve()
        if self.outdir==self.repo or self.repo in self.outdir.parents:
            raise ValueError('Raw root packets must remain outside the repository')
        self.caller=Path(caller_source).resolve();self.caller_sha=sha(self.caller)
        pins=_load_pins(self.caller)
        if set(pins)!=set(source_paths):raise ValueError('Retain every original actual source role')
        self.paths={key:Path(value).resolve() for key,value in source_paths.items()}
        for role,(relative,expected) in pins.items():
            if (not isinstance(relative,str) or not digest(expected)
                    or sha(self.paths[role])!=expected):
                raise ValueError('An entire actual source role differs: '+role)
            if self.outdir==self.paths[role] or self.outdir in self.paths[role].parents:
                raise ValueError('Raw output must not contain a source input')
        if ('root_packets' not in self.paths
                or self.paths['root_packets']!=Path(__file__).resolve()
                or pins['root_packets'][1]!=sha(__file__)):
            raise ValueError('The full caller must explicitly pin this complete recorder source')
        self.roles={key:sha(path) for key,path in self.paths.items()}
        self.operator=q.model.get('source_sha256')
        if self.operator not in NORMALS:raise ValueError('Use one explicitly supported complete normal operator')
        self.model_object=q.model;self.model=copy_json(q.model);self.identity=q.identity
        self.spec=NORMALS[self.operator]
        if (canonical(q.model)!=q.identity or q.model.get('schema')!=self.spec['schema']
                or q.model.get('base_source_sha256')!=self.spec['base']
                or q.model.get('base_complete_model')!=q.base.model
                or canonical(q.base.model)!=q.base.identity):
            raise ValueError('The complete normal/base/selected field identity differs')
        self.methods={}
        for name in METHODS:
            fn=getattr(q,name).__func__
            if sha(fn.__code__.co_filename)!=self.operator:
                raise ValueError('Actual normal method code differs: '+name)
            self.methods[name]=fn
        if (sha(q.adjacent_frames._root_protection.__func__.__code__.co_filename)!=self.spec['adjacent']
                or sha(q.reference_calibration.metadata.__func__.__code__.co_filename)!=self.spec['calibration']):
            raise ValueError('Bind actual full provenance and calibration implementations')
        self.analytic_functions={}
        if 'analytic' in self.spec:
            actual=q.analytic_stage_jacobian
            if (self.roles.get('analytic_J3')!=self.spec['analytic']
                    or actual.definition!=q.model.get('analytic_stage_jacobian')
                    or actual.definition.get('source_sha256')!=self.spec['analytic']):
                raise ValueError('Bind the complete actual analytic local-J3 source and model definition')
            for name in ('matrix','metadata'):
                function=getattr(actual,name).__func__
                if sha(function.__code__.co_filename)!=self.spec['analytic']:
                    raise ValueError('The actual local-J3 counter/metadata source differs')
                self.analytic_functions[name]=function
        self.analytic_frame_functions={}
        if 'analytic_frame' in self.spec:
            actual=q.analytic_normal_frame
            if (self.roles.get('analytic_frame')!=self.spec['analytic_frame']
                    or actual.definition!=q.model.get('analytic_normal_frame')
                    or actual.definition.get('source_sha256')!=self.spec['analytic_frame']):
                raise ValueError('Bind the complete actual analytic six-control frame source and model')
            for name in ('frame','metadata'):
                function=getattr(actual,name).__func__
                if sha(function.__code__.co_filename)!=self.spec['analytic_frame']:
                    raise ValueError('The actual full-frame producer/metadata source differs')
                self.analytic_frame_functions[name]=function
        self.closure_functions={}
        if 'closure_values' in self.spec:
            actual=q.detached_closure_values
            if (self.roles.get('closure_values')!=self.spec['closure_values']
                    or actual.definition!=q.model.get('detached_closure_value_reuse')
                    or actual.definition.get('source_sha256')!=self.spec['closure_values']):
                raise ValueError('Bind complete same-chain closure provenance without evaluating it')
            for name in ('value','metadata'):
                function=getattr(actual,name).__func__
                if sha(function.__code__.co_filename)!=self.spec['closure_values']:
                    raise ValueError('The complete closure counter/metadata source differs')
                self.closure_functions[name]=function
        self.partition=[str(v) for v in q.normal_step_nodes]
        self.carriers=[float(v).hex() for v in q.normal_step_carriers]
        self.stage_count=_validate_partition(self.partition,self.carriers)
        if self.stage_count!=q.normal_stage_count or q.model['exact_normal_step_nodes']!=self.partition:
            raise ValueError('Preserve every declared common normal stage')
        if self.outdir.exists() and any(self.outdir.iterdir()):
            raise ValueError('Use a fresh recorder directory; immutable past inputs are not silently restored')
        self.outdir.mkdir(parents=True,exist_ok=True)
        for name in ('points','angles','snapshots','operator-metadata','reference-calibration'):
            (self.outdir/name).mkdir()
        self.counts={key:0 for key in RUNTIME_COUNTS}
        self.capture_seconds=0.;self.snapshots=[];self.last_failure=None
        self.point_cache={};self.angle_cache={};self.reference_files={}
        self._check_model()
        self.fixed_carrier=self._save_carrier()

    def _check_model(self):
        q=self.q
        if (q.model is not self.model_object or q.model!=self.model
                or canonical(q.model)!=self.identity or q.identity!=self.identity
                or [str(v) for v in q.normal_step_nodes]!=self.partition
                or [float(v).hex() for v in q.normal_step_carriers]!=self.carriers
                or any(getattr(q,n).__func__ is not f for n,f in self.methods.items())):
            raise ValueError('Do not record a changed source/model/partition under an old identity')

        if self.analytic_functions and any(getattr(q.analytic_stage_jacobian,n).__func__ is not f
                for n,f in self.analytic_functions.items()):
            raise ValueError('Do not replace the bound actual analytic-J3 implementation during capture')
        if self.analytic_frame_functions and any(getattr(q.analytic_normal_frame,n).__func__ is not f
                for n,f in self.analytic_frame_functions.items()):
            raise ValueError('Do not replace the complete analytic-frame producer during capture')
        if self.closure_functions and any(getattr(q.detached_closure_values,n).__func__ is not f
                for n,f in self.closure_functions.items()):
            raise ValueError('Do not replace the complete closure value source during capture')

    def _array(self,value,shape=None,dtype='float64'):
        np=self.np
        if hasattr(value,'detach'):value=value.detach().cpu().numpy()
        value=np.asarray(value)
        if value.dtype!=np.dtype(dtype) or (shape is not None and value.shape!=tuple(shape)):
            raise ValueError('Keep the actual complete array dtype/shape; no conversion or padding')
        if not np.isfinite(value).all():raise ValueError('A successful cache packet must contain finite words')
        array=np.array(value,copy=True,order='C');array.setflags(write=False)
        return array

    def _array_sha(self,array):
        h=hashlib.sha256(str(array.dtype).encode())
        h.update(json.dumps(list(array.shape)).encode());h.update(array.tobytes(order='C'))
        return h.hexdigest()

    def _descriptors(self,arrays):
        return [_array_descriptor(name,array.shape,self._array_sha(array),str(array.dtype))
                for name,array in arrays.items()]

    def _npz(self,path,arrays):
        path=Path(path);descriptors=self._descriptors(arrays)
        if path.exists():
            record=file_record(path);validate_arrays_file(record,descriptors)
            return record,False
        tmp=path.with_name('.'+path.name+'.'+uuid.uuid4().hex+'.tmp')
        try:
            with tmp.open('xb') as handle:
                self.np.savez(handle,**arrays);handle.flush();os.fsync(handle.fileno())
            try:os.link(tmp,path)
            except FileExistsError:
                validate_arrays_file(file_record(path),descriptors)
        finally:
            if tmp.exists():tmp.unlink()
        return file_record(path),True

    def _carrier_arrays(self):
        q=self.q;query=q.integration_query
        if set(query)!=set(('cells','local','s','widths','cells_torch','weights','h','hp','hpp')):
            raise ValueError('The complete original integration query interface changed')
        arrays=dict(mesh=self._array(q.mesh),gauss_u=self._array(q.gauss_u),
            gauss_w=self._array(q.gauss_w),grid_phi=self._array(q.phi))
        for name in ('cells','local','s','widths','weights','h','hp','hpp'):
            arrays['integration_'+name]=self._array(query[name],dtype='int64' if name=='cells' else 'float64')
        if (not self.np.array_equal(query['cells_torch'].detach().cpu().numpy(),arrays['integration_cells'])
                or len(arrays['integration_cells'])!=(q.J-1)*q.integration_order):
            raise ValueError('Keep all original actual integration nodes and their integer addresses')
        return arrays

    def _save_carrier(self):
        q=self.q;arrays=self._carrier_arrays()
        descriptors=self._descriptors(arrays);identity=canonical(descriptors)
        record,_=self._npz(self.outdir/('working-carriers-'+identity+'.npz'),arrays)
        return dict(model_identity_sha256=self.identity,arrays_file=record,arrays=descriptors,
            exact_normal_step_nodes=self.partition,normal_step_carriers_hex=self.carriers,
            original_S_carrier_hex=float(q.S).hex(),integration_order=int(q.integration_order),
            all_actual_integral_nodes_recorded=True,
            fixed_scalar_metric_identity_sha256=q.base.model['fixed_scalar_metric_identity_sha256'],
            original_node_words_recomputed=False,accurate_affine_nodes_are_not_these_float_carriers=True)

    def _binding(self,point):
        return dict(model_identity_sha256=self.identity,operator_source_sha256=self.operator,
            caller_source_sha256=self.caller_sha,recorder_source_sha256=sha(__file__),
            current_full_point_sha256=point,
            fixed_scalar_metric_identity_sha256=self.q.base.model['fixed_scalar_metric_identity_sha256'])

    def _point(self):
        q=self.q
        if q._current_x is None:
            if q._current_point_sha256 is not None or q._root_cache:
                raise ValueError('An unselected point cannot own cached roots')
            return None,None
        x=self._array(q._current_x,(q.free_size,))
        point=self._array_sha(x)
        if point!=q._current_point_sha256:raise ValueError('The complete cache-owning point words differ')
        if point in self.point_cache:
            result=self.point_cache[point]
            validate_arrays_file(result['arrays_file'],[result['array']])
            self.counts['point_files_reused']+=1
        else:
            record,created=self._npz(self.outdir/'points'/(point+'.npz'),dict(x=x))
            result=dict(schema=POINT_SCHEMA,model_identity_sha256=self.identity,
                current_full_point_sha256=point,array=self._descriptors(dict(x=x))[0],arrays_file=record)
            self.point_cache[point]=result
            self.counts['point_files_created' if created else 'point_files_reused']+=1
        return point,copy_json(result)

    def _angle(self,angle,item,point):
        q=self.q;order=item.get('order')
        if type(order) is not int or order not in (1,2):raise ValueError('Keep the actual completed cache order')
        # This original source-bound routine hashes/validates stored words only.
        # It does not invoke a root, derivative, field, or frame evaluation.
        protected=q.adjacent_frames._root_protection([item],[angle],order)
        arrays=dict(Z=self._array(item['Z'],ARRAY_SHAPES['Z']),
                    zero=self._array(item['zero'],ARRAY_SHAPES['zero']))
        stages=[]
        for i,stage in enumerate(item['stages']):
            prefix='stage_'+str(i+1).zfill(3)+'_'
            for name in ('eta','frame','controls','J'):
                arrays[prefix+name]=self._array(stage[name],ARRAY_SHAPES[name])
            matrix_order=stage['jacobian_order'];matrix_name=None
            if type(matrix_order) is not int or not 0<=matrix_order<=order:
                raise ValueError('An existing angular matrix has inconsistent actual order')
            if matrix_order==0:
                if stage['jacobian'] is not None:raise ValueError('Do not invent the order of an existing matrix')
            else:
                matrix_name=prefix+'jacobian'
                arrays[matrix_name]=self._array(stage['jacobian'],(3*(matrix_order+1),)*2)
            stages.append(dict(normal_stage_index=i+1,exact_auxiliary_node=self.partition[i+1],
                actual_auxiliary_node_hex=self.carriers[i+1],
                original_stage_record=copy_json(stage['record']),
                frame_provenance=copy_json(stage['frame_provenance']),
                actual_cached_implicit_matrix_angular_order=matrix_order,
                angular_matrix_array=matrix_name,
                per_item_angular_matrix_algorithm_choice='not_retained_in_original_cache'))
        root_record=copy_json(item['record'])
        d=dict(**self._binding(point),literal_angle_hex=angle,
            actual_cached_angular_order=order,normal_stage_count=self.stage_count,
            exact_normal_step_nodes=self.partition,normal_step_carriers_hex=self.carriers,
            arrays=self._descriptors(arrays),stages=stages,original_root_record=root_record,
            original_protected_root_fields_sha256=protected,
            actual_computed_angular_orders=list(range(order+1)),
            uncomputed_stored_angular_orders=list(range(order+1,3)),
            computed_physical_angular_endpoint_residual_norms=
                root_record['physical_angular_endpoint_residual_norms'][:order+1],
            all_original_declared_stages_present=True,
            per_item_angular_matrix_algorithm_choice='not_retained_in_original_cache',
            matrix_possible_complete_producers=['adjacent_total_frames','complete_original_AD_fallback'],
            numerical_matrix_words_are_recorded_without_reconstruction=True,
            root_requested_order_history_recovered=False,
            continuous_branch_certified=False,field_acceptance_inferred=False)
        identity=canonical(d);path=self.outdir/'angles'/(identity+'.json')
        if path.exists():
            packet=read_json_record(file_record(path))
            if packet.get('definition')!=d:raise ValueError('An immutable angle identity collided')
            validate_packet(packet,model=self.model,operator_source_sha256=self.operator,
                caller_source_sha256=self.caller_sha,point_sha256=point,angle_hex=angle,
                reread_arrays=True)
            self.counts['angle_packets_reused']+=1
        else:
            raw_record,_=self._npz(self.outdir/'angles'/(identity+'.npz'),arrays)
            packet=dict(schema=PACKET_SCHEMA,packet_identity_sha256=identity,
                definition=d,arrays_file=raw_record)
            validate_packet(packet,model=self.model,operator_source_sha256=self.operator,
                caller_source_sha256=self.caller_sha,point_sha256=point,angle_hex=angle)
            _atomic_bytes(path,_json_bytes(packet))
            self.counts['angle_packets_created']+=1
        self.counts['cache_angles_seen']+=1
        self.counts['actual_J3_stage_blocks_copied']+=self.stage_count
        self.counts['actual_J6_stage_blocks_copied']+=sum(
            s['actual_cached_implicit_matrix_angular_order']==1 for s in stages)
        self.counts['actual_J9_stage_blocks_copied']+=sum(
            s['actual_cached_implicit_matrix_angular_order']==2 for s in stages)
        result=dict(literal_angle_hex=angle,packet_identity_sha256=identity,
            packet_file=file_record(path),actual_cached_angular_order=order,
            all_stages_have_second_order_implicit_matrix=all(
                s['actual_cached_implicit_matrix_angular_order']==2 for s in stages))
        self.angle_cache[identity]=result
        return copy_json(result)

    def _cache_token(self):
        q=self.q
        if q._current_x is None:
            return canonical(dict(point=None,cache=[]))
        point=self._array_sha(self._array(q._current_x,(q.free_size,)))
        if point!=q._current_point_sha256:raise ValueError('Current cache point changed')
        records=[]
        for key,item in q._root_cache.items():
            literal_angle(key)
            protected=q.adjacent_frames._root_protection([item],[key],item['order'])
            matrices=[]
            for stage in item['stages']:
                order=stage['jacobian_order']
                if order==0:
                    if stage['jacobian'] is not None:raise ValueError('Unknown matrix order')
                    matrices.append(None)
                elif type(order) is int and order in (1,2):
                    a=self._array(stage['jacobian'],(3*(order+1),)*2)
                    matrices.append(dict(order=order,array_sha256=self._array_sha(a)))
                else:raise ValueError('Invalid actual matrix cache order')
            records.append(dict(angle=key,protected=protected,matrices=matrices))
        return canonical(dict(point=point,cache=records,
            last_root_failure=q._last_root_failure,last_normal_batch=q._last_normal_batch))

    def _calibration_files(self,metadata):
        value=metadata['reference_centering']
        if (value.get('source_sha256')!=self.spec['calibration']
                or value.get('model_identity_sha256')!=self.identity):
            raise ValueError('Keep actual same-field reference calibration records')
        answer=[]
        for original in value.get('actual_reference_records',[]):
            original=copy_json(original)
            source={key:original[key] for key in ('path','sha256','bytes')}
            validate_file_record(source,reread=True)
            key=source['sha256']
            target=self.outdir/'reference-calibration'/(key+'.npz')
            if key in self.reference_files:
                copied=self.reference_files[key]
                validate_file_record(copied,reread=True)
            else:
                raw=Path(source['path']).read_bytes()
                if len(raw)!=source['bytes'] or hashlib.sha256(raw).hexdigest()!=key:
                    raise ValueError('The actual reference cache changed while being copied')
                copied,_=_atomic_bytes(target,raw)
                self.reference_files[key]=copied
            if copied['sha256']!=key or copied['bytes']!=source['bytes']:
                raise ValueError('Copy exact actual calibration bytes without reconstruction')
            answer.append(dict(original_complete_record=original,immutable_copy=copied,
                unchanged_whole_file_bytes=True,reference_defect_or_core_cap_recomputed=False))
        return answer

    def capture(self,operator_metadata,*,witnesses=(),radius_witnesses=(),label='actual-save-report'):
        require_actions();started=time.monotonic()
        self.counts['capture_calls_started']+=1
        completed=False;before=None
        try:
            self._check_model();q=self.q
            if self._descriptors(self._carrier_arrays())!=self.fixed_carrier['arrays']:
                raise ValueError('The complete actual integration carrier words changed')
            if not isinstance(label,str) or not label:raise ValueError('Supply an honest actual snapshot label')
            metadata=copy_json(operator_metadata)
            if (metadata.get('source_sha256')!=self.operator
                    or metadata.get('model_identity_sha256')!=self.identity
                    or metadata.get('model')!=self.model
                    or metadata.get('current_full_point_sha256')!=q._current_point_sha256
                    or metadata.get('current_cached_angle_roots')!=len(q._root_cache)
                    or metadata.get('normal_stage_count')!=self.stage_count
                    or metadata.get('exact_normal_step_nodes')!=self.partition):
                raise ValueError('Pass the actual already-read whole operator metadata at its current cache point')
            before=_scientific_counts(q)
            if (metadata.get('actual_field_counts')!=before['field']
                    or metadata.get('endpoint_counts')!=before['endpoint']
                    or metadata.get('actual_normal_counts')!=before['normal']):
                raise ValueError('The supplied full metadata is not the same actual counter snapshot')
            if ('analytic' in self.spec and metadata.get('analytic_stage_jacobian',{}).get(
                    'actual_counts')!=before['analytic_stage_jacobian']):
                raise ValueError('Use the same actual analytic-J3 count snapshot as the whole operator metadata')
            if ('analytic_frame' in self.spec and metadata.get('analytic_normal_frame',{}).get(
                    'actual_counts')!=before['analytic_normal_frame']):
                raise ValueError('Actual full-frame metadata must retain its own unchanged counters')
            start_token=self._cache_token()
            point,point_record=self._point()
            required=_angles(q,witnesses,radius_witnesses)
            keys=list(q._root_cache)
            packets=[self._angle(key,q._root_cache[key],point) for key in keys]
            calibration=self._calibration_files(metadata)
            meta_identity=canonical(metadata)
            meta_record,_=_atomic_bytes(self.outdir/'operator-metadata'/(meta_identity+'.json'),
                                       _json_bytes(metadata))
            after=_scientific_counts(q)
            end_token=self._cache_token();self._check_model()
            if before!=after or end_token!=start_token:
                raise ValueError('Record-only capture changed scientific counters or current complete cache words')
            missing=[key for key in required if key not in set(keys)]
            roots2={p['literal_angle_hex'] for p in packets if p['actual_cached_angular_order']==2}
            matrices2={p['literal_angle_hex'] for p in packets if p['all_stages_have_second_order_implicit_matrix']}
            d=dict(**self._binding(point),capture_ordinal=self.counts['capture_calls_started'],
                snapshot_label=label,current_point_file=point_record,
                required_literal_angle_hex=required,cache_literal_angle_hex=keys,
                required_angle_origin='actual quarter-angle array followed by both current supplied literal permanent sets',
                cache_order_scope='current Python cache insertion order, not all historical batch or request order',
                cached_angle_count=len(keys),angle_packets=packets,
                missing_required_literal_angle_hex=missing,
                all_required_angle_roots_recorded=point is not None and not missing,
                all_required_second_angular_roots_recorded=point is not None and set(required)<=roots2,
                all_required_second_angular_implicit_matrices_recorded=point is not None and set(required)<=matrices2,
                operator_metadata_snapshot=meta_record,actual_reference_calibration_files=calibration,
                last_failed_or_partial_batch_is_in_operator_metadata=True,
                failed_partial_stages_are_not_complete_angle_packets=True,
                original_last_matrix_producer_record_is_not_reassigned_to_older_cache_items=True,
                cache_before_sha256=start_token,cache_after_sha256=end_token,
                current_point_and_cache_unchanged_during_capture=True,
                scientific_counts_before=before,scientific_counts_after=after,
                actual_scientific_evaluations_by_recorder=0,
                continuous_branch_or_field_certified=False,accepted_outer_point_inferred_from_cache=False,
                all_past_candidate_or_root_attempts_recovered=False)
            identity=canonical(d)
            snapshot=dict(schema=SNAPSHOT_SCHEMA,snapshot_identity_sha256=identity,definition=d)
            summary=validate_snapshot(snapshot,model=self.model,operator_source_sha256=self.operator,
                caller_source_sha256=self.caller_sha)
            record,created=_atomic_bytes(self.outdir/'snapshots'/(identity+'.json'),_json_bytes(snapshot))
            if not created:raise ValueError('A fresh capture ordinal unexpectedly reused an immutable snapshot')
            self.snapshots.append(dict(snapshot_identity_sha256=identity,
                snapshot_file=record,summary=summary))
            self.counts['snapshot_files_created']+=1
            self.counts['capture_calls_completed']+=1
            self.last_failure=None;completed=True
        except (MemoryError,OSError) as error:
            self.last_failure=dict(type=type(error).__name__,message=str(error),
                capture_ordinal=self.counts['capture_calls_started'],
                actual_current_full_point_sha256=self.q._current_point_sha256,
                incomplete_capture_not_counted_as_complete=True,
                science_was_not_restarted_or_recomputed=True)
        finally:
            if not completed:self.counts['capture_calls_failed']+=1
            self.capture_seconds+=time.monotonic()-started
            if before is not None and before!=_scientific_counts(self.q):
                raise AssertionError('The recorder must never alter scientific counters')
        return self.metadata()


    def capture_entry(self,operator_metadata,*,outer_full_point_sha256,witnesses=(),
                      radius_witnesses=(),label):
        if not digest(outer_full_point_sha256):
            raise ValueError('Supply the actual complete outer point digest without selecting a new cache point')
        state=self.capture(operator_metadata,witnesses=witnesses,
            radius_witnesses=radius_witnesses,label=label)
        ordinal=state['actual_recorder_counts']['capture_calls_started']
        failure=state['latest_capture_failure']
        completed=failure is None
        snapshot=copy_json(state['snapshots'][-1]) if completed else None
        point=self.q._current_point_sha256
        value=dict(schema=ENTRY_CAPTURE_SCHEMA,label=label,capture_ordinal=ordinal,
            capture_completed=completed,snapshot=snapshot,capture_failure=copy_json(failure),
            outer_full_point_sha256=outer_full_point_sha256,
            current_cache_full_point_sha256=point,
            current_cache_equals_outer_point=point==outer_full_point_sha256,
            cache_point_is_not_assumed_accepted_outer_point=True,
            actual_scientific_evaluations_by_recorder=0)
        validate_entry_capture(value,metadata=state)
        return value

    def metadata(self):
        value=dict(schema=SCHEMA,source_sha256=sha(__file__),definition=definition(),
            definition_identity_sha256=canonical(definition()),
            model_identity_sha256=self.identity,operator_source_sha256=self.operator,
            caller_source_sha256=self.caller_sha,source_sha256_by_role=copy_json(self.roles),
            fixed_working_carrier=copy_json(self.fixed_carrier),
            actual_recorder_counts=dict(self.counts),capture_seconds=self.capture_seconds,
            snapshots=copy_json(self.snapshots),
            latest_complete_capture=copy_json(self.snapshots[-1]['summary']) if self.snapshots else None,
            latest_capture_failure=copy_json(self.last_failure),
            no_scientific_evaluations=True,old_scientific_methods_changed=False,
            actual_query_integration_words_recorded=True,
            all_past_root_attempts_recovered=False,field_acceptance_claimed=False,
            continuous_branch_certified=False,root_or_quadrature_or_derivative_errors_paid=False,
            full_current_meridian_arrays_recorded=False,
            scope='Immutable existing numerical normal-root/cache inputs only; not a numerical reevaluation, a certified branch, or a paid continuous sixjet')
        validate_metadata(value,model=self.model,operator_source_sha256=self.operator,
            caller_source_sha256=self.caller_sha,source_sha256_by_role=self.roles)
        return value
