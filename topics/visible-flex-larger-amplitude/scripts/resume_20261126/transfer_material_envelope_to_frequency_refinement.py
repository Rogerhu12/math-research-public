#!/usr/bin/env python3
"""Complete source-bound M160 to M320 inclusion and historical memory.

The original reference, chart, exact target, radial mesh, supported seed,
literal Q, gamma and common normal partition are fixed. Both real M160
producer/reader families are independently retained. Every actual old free
word is included in its correct core/odd-sine/odd-cosine/even-sine slot;
new modes are zero. Original physical/root/norm/geometry values are never
promoted to values of the new field. Complete explicit roles, protected
points, all typed rows and unresolved parallel obligations remain binding.
This source never constructs or evaluates the original scientific field.
"""
import ast
import copy
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import struct
import sys
from types import SimpleNamespace


SCHEMA = 'complete-source-bound-M160-to-M320-frequency-and-material-memory-transfer-v1'
MEMORY_SOURCE_SHA256 = 'c79c7f7ec1febf0ab6dca30d28a91b1566745972342c7336a3a9a106f56b3152'
CURRENT_MEMORY_SOURCE_SHA256 = '5f22ad999b33a657d5e59721f3d6459b3411faabb180a475cd3fd989b662fba0'
HISTORY_SOURCE_SHA256 = '4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60'
ORIGINAL_DRIVER_SHA256 = 'cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5'
ORIGINAL_READER_SHA256 = '104e014062f29969c0c94884bf810b6f9b23999ad8cc902238f981a9b0ad35f7'
ORIGINAL_OPERATOR_SHA256 = 'a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd'
ORIGINAL_CALIBRATION_SHA256 = '3e478bbeacbe236947070f9422ab6c75852f460f41536c68ebb3995ff0a2a991'
ORIGINAL_REPORT_SCHEMA = 'complete-R711-reference-centred-C1-material-envelope-fixed-normal-plane-SO3-QP-v1'
ORIGINAL_OPERATOR_SCHEMA = 'complete-R711-reference-centred-C1-reuse-SO3-fixed-normal-plane-six-control-layer-v1'
ORIGINAL_READER_RELATIVE = 'scripts/resume_20261126/read_reference_centred_c1_material_envelope_so3_report.py'
ADDRESS_ROLES = ('curvature_points','radius_points','protected_curvature_points')
TYPE_KEYS = ('family','location','partner','branch','sign')

LAYOUT_SOURCE_SHA256 = 'ce188ae4bdf1ccecfbf9549897284e8dc44f4722e04e974c7a0cd045c78a3a27'
COARSE_BASE_SOURCE_SHA256 = '6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865'
COARSE_BASE_SCHEMA = 'complete-supported-smooth-triangle-reference-so3-meridian-with-core-lift-v1'
COARSE_BINDER_SOURCE_SHA256 = '307ebae301db059f30ff1cc5fda024b09e9c2730c9f6bffbd82f0821d2a727a7'
COARSE_INPUT_SCHEMA = 'supported-smooth-triangle-reference-literal-zero-endpoint-Q-input-v1'
COARSE_DEFINITION_SCHEMA = 'supported-smooth-triangle-reference-literal-two-bubble-endpoint-Q-v1'
ADJACENT_DRIVER_SHA256 = '91c86a4fed296cda92a9ac522dace21fb7e0ab603c288226b5cc8e7c3b8f44b6'
FAMILIES = {
    ORIGINAL_DRIVER_SHA256: dict(schema=ORIGINAL_REPORT_SCHEMA,
        operator_schema=ORIGINAL_OPERATOR_SCHEMA,operator_sha256=ORIGINAL_OPERATOR_SHA256,
        calibration_sha256=ORIGINAL_CALIBRATION_SHA256,reader_sha256=ORIGINAL_READER_SHA256,
        reader_relative=ORIGINAL_READER_RELATIVE),
    ADJACENT_DRIVER_SHA256: dict(
        schema='complete-R711-reference-centred-adjacent-frame-material-envelope-fixed-normal-plane-SO3-QP-v1',
        operator_schema='complete-R711-reference-centred-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1',
        operator_sha256='d5da5e3db88a03cc0afdc00e3a6bc74e425aa3f1b730ea7f66ac278f93d8e6eb',
        calibration_sha256='ccb3340e500a032943aaed084376136fd67ad81b222e1afbcc5e79d468f21ef8',
        reader_sha256='c0cc0011498154a171e401d9874d34f060242180d341d6d2ea2b85eb963455dd',
        reader_relative='scripts/resume_20261126/read_reference_centred_adjacent_frame_material_envelope_so3_report.py')}
SOURCE_REPLACEMENTS = {
    '41c865d9a505f4b7ac3b0b9c2b89a027235e78968b1f62cf7840bc119179efb2':COARSE_BASE_SOURCE_SHA256,
    'bde3fd4cab72c6296472928cd9760ad88063462ac5872c2c88addd75958d2971':COARSE_BINDER_SOURCE_SHA256,
    'aaca0b63c132bf7cb3dd37385c8dff2329614e9852c2293cd93fd46f9364ae67':'ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9',
    'd65f20fdd4d162482f041f8d85ddd0e3bc03238685e28dcaebbabb73b2b3d488':'375059dc973633a1639ceddd3105fc34fe8b37eec4c9e61a55ce3959a0b9fc59',
    'd6c0c90784a6335874afc183ac65cc6de868c3c8d8b0bf821f8cbb25789c2b34':'955dafdc865e34695489f4e8832ecb8a6d48e056f801ba119fd92e9097ad69b3'}

def _family(payload):
    family=FAMILIES.get(payload.get('source_sha256'))
    if family is None or payload.get('schema')!=family['schema']:
        raise ValueError('Only the two explicit complete M160 producer/reader families are supported')
    return family

def _replace_sources(value):
    if isinstance(value,dict):
        return {key:_replace_sources(item) for key,item in value.items()}
    if isinstance(value,list):
        return [_replace_sources(item) for item in value]
    if isinstance(value,str):
        return SOURCE_REPLACEMENTS.get(value,value)
    return value

def _layout(q,pins):
    module=getattr(q.base,'frequency_layout_module',None)
    if module is None:
        # The current base stores the source-bound module in its constructor globals.
        path=Path(q.base.__class__.__init__.__code__.co_filename).parent/'so3_frequency_refinement_layout.py'
        if sha(path)!=LAYOUT_SOURCE_SHA256:
            raise ValueError('Bind the complete independent frequency-layout module')
        name='_actual_frequency_layout_'+LAYOUT_SOURCE_SHA256
        spec=importlib.util.spec_from_file_location(name,path)
        module=importlib.util.module_from_spec(spec);sys.modules[name]=module;spec.loader.exec_module(module)
    for function in (module.definition,module.validate_base_model,module.embed_outer_words,module.validate_inclusion):
        if sha(function.__code__.co_filename)!=LAYOUT_SOURCE_SHA256:
            raise ValueError('Keep each complete current layout and byte inclusion body')
    if pins.get('frequency_layout',(None,None))[1]!=LAYOUT_SOURCE_SHA256:
        raise ValueError('The actual full caller must pin the independent layout source')
    module.validate_base_model(q.base.model,expected_base_source_sha256=pins['meridian'][1])
    return module

def _frozen_initial_points(q,pins):
    import numpy as np
    module=_layout(q,pins)
    array_sha=q.base.__class__.__init__.__globals__['array_sha']
    if sha(array_sha.__code__.co_filename)!=pins['meridian'][1]:
        raise ValueError('Bind the current complete point identity source')
    old=np.r_[q.parent_core[q.K:],np.zeros(len(q.radial_free)*482),float.fromhex(q.parent_jet.model['initial_height_hex'])]
    current=q.base.initial()
    included,record=module.embed_outer_words(old,q.base.frequency_layout_definition)
    if (included.dtype!=current.dtype or included.shape!=current.shape
            or included.tobytes()!=current.tobytes()
            or array_sha(current)!=q.reference_point_sha256):
        raise ValueError('The new frozen reference point must be the exact zero inclusion of the old core/H/zero-omega point')
    return dict(original_full_point_sha256=array_sha(old),
        current_full_point_sha256=array_sha(current),coordinate_inclusion=record)

def select_memory_source(args):
    path=args.restart_report if args.restart_report is not None else args.frequency_parent_report
    payload=json.loads(Path(path).read_text())
    if args.restart_report is None:_family(payload)
    result=payload.get('material_envelope',{}).get('source_sha256')
    if result not in (MEMORY_SOURCE_SHA256,CURRENT_MEMORY_SOURCE_SHA256):
        raise ValueError('The actual complete predecessor declares an unsupported memory producer')
    return result

def _input_identity(payload,args,q):
    records=dict(bundle_sha256=args.reference_bundle,observation_carrier_sha256=args.carrier,
        exact_tail_node_report_sha256=args.node_report,exact_tail_scalar_input_sha256=args.scalar_input)
    if any(payload.get(key)!=sha(path) for key,path in records.items()):
        raise ValueError('The original reference, carrier, symbolic nodes and scalar input must be the same whole files')
    if payload.get('independent_preparation_report',{}).get('sha256')!=sha(args.preparation_report):
        raise ValueError('Keep the complete actual original preparation report')
    if (payload.get('N')!=q.full_N or payload.get('J')!=q.J
            or payload.get('fixed_scalar_metric',{}).get('identity_sha256')!=q.context.scalar_identity
            or float(payload.get('material_envelope_active_band',math.nan)).hex()!=float(args.active_band).hex()
            or payload.get('radial_weights',{}).get('legacy_fraction')!=args.legacy_fraction
            or any(payload.get('spectral_parameters',{}).get(key)!=value for key,value in
                dict(p=args.spectral_p,epsilon=args.spectral_epsilon,scale=args.spectral_scale).items())
            or float(payload.get('numerical_reach_safety_factor',math.nan)).hex()!=float(args.reach_safety_factor).hex()):
        raise ValueError('Keep the same full observation measure, spectral loss and strict geometric safety policy')
    budgets=payload.get('amplitude_design_constraints',{}).get('budgets',{})
    for key,wanted in dict(marked_diameter_budget=args.marked_diameter_budget,
            witness_lower_budget=args.witness_lower_budget,height_floor=args.amplitude_height_floor,
            cap_radius=float(q.R)).items():
        if budgets.get(key)!=wanted:
            raise ValueError('Retain the same complete physical amplitude budget: '+key)
    geometric=payload.get('final_geometry')
    if isinstance(geometric,dict) and geometric.get('source_binding',{}).get('reach_ratio')!=args.reach_ratio:
        raise ValueError('Retain the same actual reach ratio')
    norm=payload.get('coordinate_norm',{})
    if (norm.get('norm_kind')!=args.norm_kind or norm.get('radial_length')!=args.radial_norm_length
            or norm.get('angular_transition')!=args.angular_transition
            or canonical({key:value for key,value in norm.items() if key!='norm_identity_sha256'})
            !=norm.get('norm_identity_sha256')):
        raise ValueError('Bind the actual full previous norm, without inheriting it as the new norm')
    return {key:sha(path) for key,path in records.items()}

def _parent(args,path,q,pins,memory):
    record,raw=_record_bytes(path);payload=json.loads(raw);family=_family(payload)
    topic=Path(args.repo).resolve()/'topics/visible-flex-larger-amplitude'
    pure=_old_reader(topic,payload).read_report(args.repo,path,verify_final_bundle=False)
    if pure.get('report_sha256')!=record['sha256']:
        raise ValueError('The original complete reader and captured report are different snapshots')
    _same_bytes(record);_input_identity(payload,args,q)
    if (payload.get('M')!=160 or payload.get('original_variables')
            !=q.base.frequency_layout_definition['original_free_size']):
        raise ValueError('The parent is the actual complete M160 free space')
    terminal=_terminal(payload)
    relation=_frozen_initial_points(q,pins)
    binding=_compatible_models(payload['representation'],q.model,pins,frozen_point_relation=relation)
    actual=payload.get('material_envelope')
    memory.validate_report_metadata(actual,model_identity=payload['model_identity_sha256'],
        carrier_sha256=sha(args.carrier))
    if actual.get('definition')!=memory.definition(args.envelope_near_active_rows):
        raise ValueError('Retain the actual complete old/new material envelope policy')
    return dict(record=record,payload=payload,terminal=terminal,model_binding=binding,
        original_complete_reader_sha256=family['reader_sha256'])



def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Actual complete history transfer requires public repository Actions')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),
        allow_nan=False).encode()).hexdigest()


def definition():
    return dict(schema=SCHEMA,source_sha256=sha(__file__),
        frequency_layout_source_sha256=LAYOUT_SOURCE_SHA256,
        complete_original_history_walker_sha256=HISTORY_SOURCE_SHA256,
        supported_complete_M160_families=copy.deepcopy(FAMILIES),
        supported_actual_memory_sources=[MEMORY_SOURCE_SHA256,CURRENT_MEMORY_SOURCE_SHA256],
        reference_M=160,current_M=320,J=923,full_N=2048,
        fresh_entry_requires_actual_complete_parent_final=True,
        current_source_same_model_complete_restart_also_supported=True,
        actual_parent_reader_checks_all_current_input_bytes=True,
        complete_fixed_reference_seed_chart_scalar_mesh_and_partition_retained=True,
        all_original_free_words_included_with_new_modes_zero=True,
        old_coordinate_point_bytes_equal_to_new_point_claimed=False,
        old_norm_identity_or_damping_implicitly_inherited=False,
        original_same_model_restore_guard_unchanged=True,
        all_actual_prior_typed_rows_transferred_without_eviction_or_count_cap=True,
        complete_known_explicit_roles_and_protected_addresses_serialized=True,
        prior_pending_parallel_obligations_preserved_as_provenance=True,
        unknown_protection_or_priority_reconstructed=False,
        old_field_values_root_states_jacobians_or_acceptance_inherited=False,
        numerical_coarse_fine_field_equality_claimed=False,
        exact_selected_field_inclusion_requires_compatible_implicit_branch=True,
        all_addresses_and_types_require_actual_new_field_reread=True,
        fixed_reference_seed_is_not_reselected_from_old_final=True)


def _record_bytes(path):
    path = Path(path).resolve()
    raw = path.read_bytes()
    record = dict(path=str(path),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
    return record,raw


def _same_bytes(record):
    path = Path(record['path'])
    if path.stat().st_size != record['bytes'] or sha(path) != record['sha256']:
        raise ValueError('An actual history input changed during its complete consumption')


def _literal_assignments(raw):
    result = {}
    for node in ast.parse(raw).body:
        if isinstance(node,ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0],ast.Name):
            if node.targets[0].id in ('SCHEMA','SOURCE_PINS'):
                result[node.targets[0].id] = ast.literal_eval(node.value)
    if set(result) != {'SCHEMA','SOURCE_PINS'}:
        raise ValueError('Bind the complete actual caller source and role table')
    return result


def _point(value):
    if (not isinstance(value,(tuple,list)) or len(value) != 3
            or isinstance(value[0],bool) or int(value[0]) != value[0]
            or not 0 <= int(value[0]) < 922
            or any(isinstance(v,bool) or not isinstance(v,(float,int))
                or not math.isfinite(v) for v in value[1:])
            or not 0 <= float(value[1]) <= 1
            or not 0 <= float(value[2]) <= math.pi/2):
        raise ValueError('Keep the complete literal same-mesh material point')
    return int(value[0]),float(value[1]).hex(),float(value[2]).hex()


def _address_fingerprints(arrays):
    if not isinstance(arrays,dict) or set(arrays) != set(ADDRESS_ROLES):
        raise ValueError('Serialize all three complete explicit role arrays')
    result,sets = {},{}
    for role in ADDRESS_ROLES:
        if not isinstance(arrays[role],list):
            raise ValueError('The whole explicit address array must remain a list')
        words = [_point(row) for row in arrays[role]]
        if len(words) != len(set(words)):
            raise ValueError('The complete explicit union must not carry duplicate words')
        sets[role] = set(words)
        result[role] = dict(count=len(words),exact_binary_word_set_sha256=canonical(sorted(words)))
    if not sets['protected_curvature_points'] <= sets['curvature_points']:
        raise ValueError('Every protected known address must remain in complete curvature memory')
    return result


def _from_witnesses(witnesses,radii):
    arrays = dict(curvature_points=[[int(v['cell']),float(v['u']),float(v['phi'])] for v in witnesses],
        radius_points=[[int(v['cell']),float(v['u']),float(v['phi'])] for v in radii],
        protected_curvature_points=[[int(v['cell']),float(v['u']),float(v['phi'])]
            for v in witnesses if v.get('protected',False)])
    for role in ADDRESS_ROLES:
        arrays[role].sort(key=_point)
    _address_fingerprints(arrays)
    return arrays


def _type(row):
    if not isinstance(row,dict) or not all(key in row for key in TYPE_KEYS):
        raise ValueError('Keep every original family/location/partner/branch/sign component')
    return {key:copy.deepcopy(row[key]) for key in TYPE_KEYS}


def _typed_key(row):
    return canonical(_type(row))


def _terminal(value):
    if value.get('complete') is True:
        return 'complete-original-budget-report'
    if (value.get('complete') is False
            and value.get('stop_reason') == 'actual_initial_zero_closure_field_read_failed'
            and isinstance(value.get('actual_initial_read_error'),str)
            and value.get('initial_failed_candidate_is_not_an_accepted_field') is True
            and not value.get('metric_directions') and not value.get('restoration_directions')):
        return 'explicit-original-initial-field-failure-report'
    raise ValueError('Do not consume a future, still-running or unclosed partial envelope report as terminal history')


def _old_reader(topic,payload):
    family=_family(payload);path=topic/family['reader_relative']
    expected=family['reader_sha256']
    if sha(path)!=expected:
        raise ValueError('Use the complete original reader for this exact M160 producer')
    name='_complete_original_frequency_parent_reader_'+expected
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module;spec.loader.exec_module(module)
    if sha(module.read_report.__code__.co_filename)!=expected:
        raise ValueError('The complete original report reader body changed')
    return module


def _compatible_models(old,new,current_pins,*,frozen_point_relation):
    family=next((value for value in FAMILIES.values()
        if value['operator_sha256']==old.get('source_sha256')),None)
    if (family is None or old.get('schema')!=family['operator_schema']
            or new.get('schema')!='complete-R711-reference-centred-adjacent-frame-frequency-refined-SO3-fixed-normal-plane-six-control-layer-v1'
            or new.get('source_sha256')!=current_pins['endpoint'][1]
            or new.get('base_source_sha256')!=current_pins['meridian'][1]
            or new.get('new_reference_input_binding_source_sha256')!=current_pins['new_moment_input'][1]):
        raise ValueError('Bind the explicitly declared complete coarse and fine physical producers')
    oldbase=old['base_complete_model'];newbase=new['base_complete_model']
    if (oldbase.get('schema')!=COARSE_BASE_SCHEMA
            or oldbase.get('source_sha256')!=COARSE_BASE_SOURCE_SHA256
            or canonical(oldbase)!=old.get('base_model_identity_sha256')
            or canonical(newbase)!=new.get('base_model_identity_sha256')
            or newbase.get('reference_M')!=160 or newbase.get('current_M')!=320
            or newbase.get('frequency_layout_source_sha256')!=LAYOUT_SOURCE_SHA256):
        raise ValueError('Keep the fixed old reference separate from the new current angular space')
    normalized=copy.deepcopy(newbase)
    for key in ('reference_M','current_M','frequency_layout_definition',
            'frequency_layout_identity_sha256','frequency_layout_source_sha256',
            'all_original_outer_free_variables_retained_and_new_modes_added',
            'frozen_reference_layout_unchanged','current_norm_layout_changed'):
        normalized.pop(key)
    normalized.update(schema=COARSE_BASE_SCHEMA,source_sha256=COARSE_BASE_SOURCE_SHA256,M=160,
        all_original_outer_free_variables_and_norm_layout_unchanged=True)
    if normalized!=oldbase:
        raise ValueError('The full frozen scalar/reference/seed/chart/radial mesh or physical working rules changed')
    oldpoint=frozen_point_relation['original_full_point_sha256']
    newpoint=frozen_point_relation['current_full_point_sha256']
    before,after=copy.deepcopy(old),copy.deepcopy(new)
    oldq,newq=before['frozen_moment_Q_definition'],after['frozen_moment_Q_definition']
    if (oldq.get('schema')!=COARSE_DEFINITION_SCHEMA
            or newq.get('schema')!='frequency-refined-supported-smooth-triangle-reference-literal-two-bubble-endpoint-Q-v1'
            or oldq.get('initial_full_point_sha256')!=oldpoint
            or newq.get('initial_full_point_sha256')!=newpoint
            or canonical(oldq)!=before['frozen_moment_Q_definition_identity_sha256']
            or canonical(newq)!=after['frozen_moment_Q_definition_identity_sha256']):
        raise ValueError('Bind each full literal-Q definition to its own actual complete initial coordinate point')
    qcopy=copy.deepcopy(newq)
    qcopy.update(schema=COARSE_DEFINITION_SCHEMA,base_model_identity_sha256=canonical(oldbase),
        initial_full_point_sha256=oldpoint)
    if qcopy!=oldq:
        raise ValueError('The eighteen literal Q words, supports or full fixed seed/target definition changed')
    oldcal=before['reference_centering_definition'];newcal=after['reference_centering_definition']
    if (oldcal.get('source_sha256')!=family['calibration_sha256']
            or oldcal.get('endpoint_source_sha256')!=family['operator_sha256']
            or oldcal.get('original_reference_point_sha256')!=oldpoint
            or newcal.get('source_sha256')!=current_pins['reference_calibration'][1]
            or newcal.get('endpoint_source_sha256')!=current_pins['endpoint'][1]
            or newcal.get('original_reference_point_sha256')!=newpoint
            or newcal.get('frozen_reference_M')!=160 or newcal.get('current_M')!=320
            or newcal.get('current_layout_reference_point_is_old_layout_byte_identical') is not False
            or newcal.get('frozen_seed_and_original_reference_core_H_unchanged') is not True):
        raise ValueError('Keep the exact fixed reference and honest distinct coordinate-point identities')
    calcopy=copy.deepcopy(newcal)
    for key in ('reference_point_coordinate_layout','frozen_reference_M','current_M',
            'current_layout_reference_point_is_old_layout_byte_identical',
            'frozen_seed_and_original_reference_core_H_unchanged'):
        calcopy.pop(key)
    calcopy.update(source_sha256=family['calibration_sha256'],
        endpoint_source_sha256=family['operator_sha256'],
        original_reference_point_sha256=oldpoint,base_model_identity_sha256=canonical(oldbase))
    if calcopy!=oldcal:
        raise ValueError('The complete reference quadrature/centering definition changed beyond its explicit layout and sources')
    after['base_complete_model']=copy.deepcopy(oldbase)
    after['base_model_identity_sha256']=canonical(oldbase)
    after['base_source_sha256']=COARSE_BASE_SOURCE_SHA256
    after['base_schema']=COARSE_BASE_SCHEMA
    after['M']=160
    after['frozen_moment_Q_definition']=copy.deepcopy(oldq)
    after['frozen_moment_Q_definition_identity_sha256']=canonical(oldq)
    after['literal_Q_input_schema']=COARSE_INPUT_SCHEMA
    after['new_reference_input_binding_source_sha256']=COARSE_BINDER_SOURCE_SHA256
    after['reference_centering_definition']=copy.deepcopy(oldcal)
    for key,role in (('normal_frame_C1_reuse','frame_C1'),
            ('detached_stage_matrix_reuse','stage_matrices'),
            ('adjacent_normal_frame_matrices','adjacent_matrices')):
        policy=after.get(key)
        if not isinstance(policy,dict) or policy.get('source_sha256')!=current_pins[role][1]:
            raise ValueError('Bind each entire fine working policy to its complete real source')
        normalized_policy=_replace_sources(policy)
        if key in before:
            if normalized_policy!=before[key]:
                raise ValueError('The complete unchanged working policy changed beyond the explicit source rebinding')
            after[key]=copy.deepcopy(before[key])
        elif key=='detached_stage_matrix_reuse':
            if (normalized_policy.get('original_stage_equations_domain_solves_and_trace_retained') is not True
                    or normalized_policy.get('original_active_residual_and_full_upstream_parameter_chain_retained') is not True):
                raise ValueError('The additional complete detached producer must retain every original stage/J edge')
            after.pop(key)
        elif key=='adjacent_normal_frame_matrices':
            if (normalized_policy.get('all_original_stage_equations_roots_Newton_J3_and_angular_solves_retained') is not True
                    or normalized_policy.get('original_active_residual_and_all_upstream_parameter_edges_retained') is not True
                    or normalized_policy.get('block_products_have_independent_working_rounding_definition') is not True):
                raise ValueError('The complete adjacent-frame producer must declare its own rounding without changing stages')
            after.pop(key)
        else:
            raise ValueError('Every supported parent already has the full fixed C1 policy')
    after['schema']=before['schema'];after['source_sha256']=before['source_sha256']
    if before!=after:
        raise ValueError('An undeclared exact target, original variable, gamma, common partition or implicit-selection parameter changed')
    return dict(complete_unchanged_definition_sha256=canonical(before),
        exact_old_complete_model_identity_sha256=canonical(old),
        exact_new_complete_model_identity_sha256=canonical(new),
        original_base_model_identity_sha256=canonical(oldbase),
        current_base_model_identity_sha256=canonical(newbase),
        reference_M=160,current_M=320,frequency_layout_identity_sha256=newbase['frequency_layout_identity_sha256'],
        frozen_original_point_relation=copy.deepcopy(frozen_point_relation),
        full_fixed_reference_chart_scalar_mesh_seed_Q_gamma_partition_equal=True,
        only_declared_current_frequency_layout_and_source_working_policy_fields_changed=True,
        computed_float_field_equality_claimed=False,
        exact_selected_field_inclusion_requires_compatible_implicit_branch=True,
        original_geometry_or_metric_certificate_inherited=False)


def _restore_annotations(envelope,rows):
    for old in rows:
        key = _typed_key(old)
        current = envelope._separation.get(key)
        if current is None or _type(current) != _type(old):
            raise ValueError('The unchanged same-model restore lost a complete typed address')
        if current['first_discovered_current_full_point_sha256'] != old['first_discovered_current_full_point_sha256']:
            raise ValueError('Retain the actual original first-discovery point')
        # This restores only the same-source record's provenance fields.  It
        # does not substitute a different-model envelope into old restore().
        envelope._separation[key] = copy.deepcopy(old)


def load_memory(args, preparation, q, history, *, memory, current_driver_source,
                restart=None, source_report_path=None):
    require_actions()
    actual_memory_sha=sha(memory.__file__)
    if (actual_memory_sha not in (MEMORY_SOURCE_SHA256,CURRENT_MEMORY_SOURCE_SHA256)
            or sha(history.Locations.walk.__code__.co_filename) != HISTORY_SOURCE_SHA256):
        raise ValueError('Keep both complete original history consumers unchanged')
    for function in (memory.load_memory,memory.validate_report_metadata,
            memory.MaterialEnvelope._separate,memory.MaterialEnvelope.restore,memory.MaterialEnvelope.metadata):
        if sha(function.__code__.co_filename) != actual_memory_sha:
            raise ValueError('The actual full memory method differs from its bound source')
    topic = Path(args.repo).resolve()/'topics/visible-flex-larger-amplitude'
    caller_record,caller_bytes = _record_bytes(current_driver_source)
    caller = _literal_assignments(caller_bytes)
    pins = caller['SOURCE_PINS']
    if (pins.get('envelope_transfer',(None,None))[1] != sha(__file__)
            or pins.get('envelope_memory',(None,None))[1] != MEMORY_SOURCE_SHA256
            or pins.get('independent_envelope_memory',(None,None))[1] != CURRENT_MEMORY_SOURCE_SHA256
            or pins.get('history',(None,None))[1] != HISTORY_SOURCE_SHA256
            or pins.get('endpoint',(None,None))[1] != q.model.get('source_sha256')
            or pins.get('reference_calibration',(None,None))[1]
                != q.model.get('reference_centering_definition',{}).get('source_sha256')
            or canonical(q.model) != q.identity):
        raise ValueError('Bind the complete actual caller, model, original memory and this independent transfer')
    for relative,expected in pins.values():
        if sha(topic/relative) != expected:
            raise ValueError('The full actual current runtime source closure changed')
    current_carrier_sha = sha(args.carrier)
    expected_policy = memory.definition(args.envelope_near_active_rows)
    paths=[Path(path).resolve() for path in getattr(args,'material_envelope_parent_report',[])]
    primary=getattr(args,'frequency_parent_report',None)
    if primary is not None:
        primary=Path(primary).resolve()
        if primary not in paths:paths.insert(0,primary)
    if len(paths)!=len(set(paths)):
        raise ValueError('Each complete actual predecessor must occur once')
    if getattr(args,'independent_envelope_branch',False) or getattr(args,'pending_parallel_envelope_run',[]):
        raise ValueError('Frequency inclusion is an actual complete-parent transfer, not a fresh independent reset')
    if (restart is None and primary is None) or (restart is not None and primary is not None):
        raise ValueError('Choose one complete coarse final or the complete same-source fine restart')
    expected_memory=select_memory_source(args)
    if actual_memory_sha!=expected_memory:
        raise ValueError('Use the actual predecessor memory producer; do not relabel its entire policy')
    parents=[_parent(args,path,q,pins,memory) for path in paths]
    restart_record = None
    prior_transfer = None
    if restart is not None:
        if source_report_path is None:
            raise ValueError('The complete actual same-source restart report path is required')
        restart_record,restart_raw = _record_bytes(source_report_path)
        if json.loads(restart_raw) != restart:
            raise ValueError('Keep the already source-validated restart snapshot')
        if (restart.get('schema') != caller['SCHEMA']
                or restart.get('source_sha256') != caller_record['sha256']
                or restart.get('complete') is not True
                or restart.get('model_identity_sha256') != q.identity
                or restart.get('representation') != q.model
                or restart.get('observation_carrier_sha256') != current_carrier_sha):
            raise ValueError('Only the actual complete same-source/model restart is restored directly')
        _input_identity(restart,args,q)
        prior_transfer = restart.get('material_envelope_transfer')
        validate_metadata(prior_transfer,model=q.model,envelope=restart['material_envelope'],
            caller_source_sha256=caller_record['sha256'],carrier_sha256=current_carrier_sha)
    manifest = [Path(path).resolve() for path in args.manifest]
    for path in paths:
        if path not in manifest:
            manifest.append(path)
    original_args = SimpleNamespace(**vars(args))
    original_args.manifest = manifest
    witnesses,radii,history_record,envelope = memory.load_memory(original_args,preparation,q,history,
        restart=restart,source_report_path=source_report_path)
    if envelope.definition != expected_policy:
        raise ValueError('The actually constructed complete envelope uses a different working policy')
    if restart is not None:
        _restore_annotations(envelope,restart['material_envelope']['actual_separation_memory']['rows'])
    arrays = _from_witnesses(witnesses,radii)
    current_sets = {role:{_point(row) for row in arrays[role]} for role in ADDRESS_ROLES}
    parent_records = [] if prior_transfer is None else copy.deepcopy(prior_transfer['actual_parent_reports'])
    imported = []
    for parent in parents:
        payload,record = parent['payload'],parent['record']
        old = payload['material_envelope']
        if (old['implicit_grid'] != envelope.metadata()['implicit_grid']
                or old['historical_address_binding']['origin_carrier']['record']['sha256']
                    != envelope.metadata()['historical_address_binding']['origin_carrier']['record']['sha256']):
            raise ValueError('Keep the entire actual old/current material grid and angle-word union')
        locations = history.Locations(q.J,q.P,q.full_N)
        locations.walk(payload,path=('complete_source_bound_envelope_parent',))
        locations.resolve_grid(args.carrier)
        old_arrays = locations.arrays()
        fingerprints = _address_fingerprints(old_arrays)
        for role in ADDRESS_ROLES:
            if not {_point(row) for row in old_arrays[role]} <= current_sets[role]:
                raise ValueError('The original complete walker lost a prior explicit role/protection address')
        rows = old['actual_separation_memory']['rows']
        source_record = dict(report=copy.deepcopy(record),
            actual_driver_sha256=payload['source_sha256'],
            actual_model_identity_sha256=payload['model_identity_sha256'],
            original_complete_reader_sha256=parent['original_complete_reader_sha256'],
            actual_terminal_report_kind=parent['terminal'],
            model_binding=parent['model_binding'],
            actual_complete_walker_role_fingerprints=fingerprints,
            actual_typed_memory_count=len(rows),actual_typed_memory_sha256=canonical(rows),
            actual_typed_core_order_sha256=canonical([_type(row) for row in rows]),
            all_typed_rows_transferred_without_eviction_or_count_cap=True,
            previous_numeric_values_or_certificates_inherited=False)
        parent_records.append(source_record)
        for ordinal,row in enumerate(rows):
            typed = _type(row)
            key = canonical(typed)
            origin = dict(source_report_sha256=record['sha256'],source_row_ordinal=ordinal,
                source_model_identity_sha256=payload['model_identity_sha256'],
                source_driver_sha256=payload['source_sha256'],
                first_discovered_source_full_point_sha256=row['first_discovered_current_full_point_sha256'],
                typed_core_sha256=key,actual_new_field_value_inherited=False)
            was_new = key not in envelope._separation
            envelope._separate(row['family'],row['location'],partner=row['partner'],
                branch=row['branch'],sign=row['sign'],token=row['first_discovered_current_full_point_sha256'])
            current = envelope._separation[key]
            origins = current.setdefault('source_bound_address_transfer_origins',[])
            if origin not in origins:
                origins.append(origin)
            if was_new:
                current['origin'] = 'source-bound prior typed address transfer; no current field value inherited'
            imported.append(dict(parent_report_sha256=record['sha256'],source_row_ordinal=ordinal,
                typed_core_sha256=key,retained_initial_ordinal=list(envelope._separation).index(key)))
        _same_bytes(record)
    branch_origin=None
    obligations=[] if prior_transfer is None else copy.deepcopy(prior_transfer['inherited_parallel_obligations'])
    for parent in parents:
        prior=parent['payload'].get('material_envelope_transfer',{})
        entry=dict(parent_report_sha256=parent['record']['sha256'],
            parent_transfer_identity_sha256=canonical(prior),
            independent_branch_origin=copy.deepcopy(prior.get('independent_branch_origin')),
            inherited_parallel_obligations=copy.deepcopy(prior.get('inherited_parallel_obligations',[])),
            unread_parallel_reports_or_typed_priority_claimed_restored=False,
            later_actual_report_merge_obligation_retained=True)
        if entry not in obligations:obligations.append(entry)
    initial_rows = envelope.separation_rows()
    record = dict(schema=SCHEMA,source_sha256=sha(__file__),definition=definition(),
        actual_current_driver_sha256=caller_record['sha256'],
        actual_current_model_identity_sha256=q.identity,
        actual_current_base_model_identity_sha256=q.base.identity,
        actual_current_carrier_sha256=current_carrier_sha,
        actual_memory_source_sha256=actual_memory_sha,
        actual_current_fixed_scalar_identity_sha256=q.context.scalar_identity,
        envelope_policy_identity_sha256=canonical(envelope.definition),
        actual_parent_reports=parent_records,
        independent_branch_origin=None,inherited_parallel_obligations=obligations,
        current_invocation_memory_mode=('same-source-restart' if restart is not None else 'frequency-refinement'),
        current_invocation_parent_report_count=len(parents),
        actual_same_source_restart_report=restart_record,
        prior_transfer_identity_sha256=None if prior_transfer is None else canonical(prior_transfer),
        complete_initial_explicit_address_union=arrays,
        complete_initial_explicit_role_fingerprints=_address_fingerprints(arrays),
        initial_imported_typed_rows=initial_rows,
        initial_imported_typed_count=len(initial_rows),initial_imported_typed_sha256=canonical(initial_rows),
        current_invocation_typed_source_order_mapping=imported,
        all_original_report_addresses_consumed_by_original_walker=True,
        all_transferred_known_protection_retained=True,
        all_transferred_types_require_actual_new_field_read=True,
        previous_feasibility_or_function_values_inherited=False,
        actual_new_field_already_screened_by_transfer=False,
        original_same_model_restore_guard_changed=False,
        continuous_same_field_geometry_or_metric_certificate=False)
    for parent in parents:
        _same_bytes(parent['record'])
    if restart_record is not None:
        _same_bytes(restart_record)
    _same_bytes(caller_record)
    validated = validate_metadata(record,model=q.model,envelope=envelope.metadata(),
        caller_source_sha256=caller_record['sha256'],carrier_sha256=current_carrier_sha)
    history_record['source_bound_prior_envelope_transfer'] = dict(
        source_sha256=sha(__file__),definition_identity_sha256=canonical(definition()),
        actual_parent_report_records=[copy.deepcopy(parent['record']) for parent in parents],
        initial_imported_typed_count=validated['initial_imported_typed_count'],
        complete_initial_explicit_role_fingerprints=validated['complete_initial_explicit_role_fingerprints'],
        old_values_or_certificates_inherited=False)
    return witnesses,radii,history_record,envelope,record


def _digest(value):
    if (not isinstance(value,str) or len(value) != 64
            or any(character not in '0123456789abcdef' for character in value)):
        raise ValueError('Keep an actual complete source/model/point digest')
    return value


def seed_from_complete_prior_final(args,q,*,current_driver_source,transfer_record):
    """Read the actual complete coarse final and include EVERY free word."""
    require_actions()
    checkpoint=getattr(args,'frequency_parent_checkpoint',None)
    report_path=getattr(args,'frequency_parent_report',None)
    if checkpoint is None and report_path is None:return None,None
    if checkpoint is None or report_path is None or args.restart_checkpoint is not None:
        raise ValueError('A fine first point has one complete coarse report/checkpoint pair')
    caller_record,caller_bytes=_record_bytes(current_driver_source)
    pins=_literal_assignments(caller_bytes)['SOURCE_PINS']
    if (pins.get('envelope_transfer',(None,None))[1]!=sha(__file__)
            or transfer_record.get('actual_current_driver_sha256')!=caller_record['sha256']
            or transfer_record.get('actual_current_model_identity_sha256')!=q.identity
            or canonical(q.model)!=q.identity):
        raise ValueError('Keep the complete actual source, current model and historical transfer')
    source_record,raw=_record_bytes(report_path)
    parents=[item for item in transfer_record['actual_parent_reports'] if item['report']==source_record]
    if len(parents)!=1:
        raise ValueError('The complete coarse final must be the explicitly transferred actual predecessor')
    payload=json.loads(raw);family=_family(payload)
    topic=Path(args.repo).resolve()/'topics/visible-flex-larger-amplitude'
    pure=_old_reader(topic,payload).read_report(args.repo,report_path,verify_final_bundle=True)
    _same_bytes(source_record);_input_identity(payload,args,q)
    if (pure.get('report_sha256')!=source_record['sha256'] or payload.get('complete') is not True
            or payload.get('final_statistics') is None
            or payload.get('final_geometry',{}).get('complete') is not True):
        raise ValueError('Only a returned complete original field supplies free-variable words')
    model_binding=_compatible_models(payload['representation'],q.model,pins,
        frozen_point_relation=_frozen_initial_points(q,pins))
    if model_binding!=parents[0]['model_binding']:
        raise ValueError('The seed and history must be the same complete source-bound parent')
    bundle_record,bundle_bytes=_record_bytes(checkpoint)
    if (bundle_record['sha256']!=payload.get('final_bundle_sha256')
            or pure.get('actual_final_bundle_sha256')!=bundle_record['sha256']):
        raise ValueError('Read the exact actual complete reported coarse checkpoint bytes')
    import io
    import numpy as np
    module=_layout(q,pins)
    array_sha=q.base.__class__.__init__.__globals__['array_sha']
    before_model=canonical(q.model);frozen_initial=array_sha(q.base.initial())
    if frozen_initial!=q.reference_point_sha256:
        raise ValueError('The original complete reference remains frozen before any coarse final inclusion')
    names={'schema','omega_jets','core','Hcap','mesh','fixed_parent_core',
        'zero_closure_model_json','zero_closure_model_identity_sha256',
        'base_so3_model_identity_sha256','fixed_scalar_metric_identity_sha256',
        'endpoint_root_policy_json','working_integration_order','working_full_angles'}
    oldmodel=payload['representation']
    with np.load(io.BytesIO(bundle_bytes),allow_pickle=False) as saved:
        if set(saved.files)!=names or len(saved.files)!=len(names):
            raise ValueError('Read all thirteen original checkpoint members without hidden state or aliases')
        if (str(saved['schema'].item())!=family['operator_schema']
                or str(saved['zero_closure_model_identity_sha256'].item())!=payload['model_identity_sha256']
                or json.loads(str(saved['zero_closure_model_json'].item()))!=oldmodel
                or str(saved['base_so3_model_identity_sha256'].item())!=oldmodel['base_model_identity_sha256']
                or str(saved['fixed_scalar_metric_identity_sha256'].item())!=q.context.scalar_identity
                or json.loads(str(saved['endpoint_root_policy_json'].item()))!=q.policy.metadata()
                or saved['working_integration_order'].shape!=()
                or saved['working_full_angles'].shape!=()
                or int(saved['working_integration_order'].item())!=q.integration_order
                or int(saved['working_full_angles'].item())!=q.full_N):
            raise ValueError('Keep the actual old complete model, exact target and unchanged complete working quadrature')
        arrays={name:np.array(saved[name],copy=True) for name in
            ('omega_jets','core','Hcap','mesh','fixed_parent_core')}
    expected_shapes=dict(omega_jets=(923,3,482),core=(160,),Hcap=(),mesh=(923,),fixed_parent_core=(160,))
    for name,value in arrays.items():
        if value.dtype!=np.dtype(float) or value.shape!=expected_shapes[name] or not np.isfinite(value).all():
            raise ValueError('Every actual old saved array must be finite binary64 with its ORIGINAL complete layout: '+name)
    same=lambda a,b:a.dtype==b.dtype and a.shape==b.shape and np.ascontiguousarray(a).tobytes()==np.ascontiguousarray(b).tobytes()
    if (not same(arrays['mesh'],q.mesh) or not same(arrays['fixed_parent_core'],q.parent_core)
            or not same(arrays['core'][:q.K],q.parent_core[:q.K])):
        raise ValueError('The actual complete fixed chart/core slots and radial mesh must agree')
    flat=arrays['omega_jets'].reshape(3*q.J,482)
    zero_slots=[0,3*(q.J-1),3*(q.J-1)+1]
    if np.any(flat[zero_slots]!=0):
        raise ValueError('The original complete checkpoint must retain all structural endpoint zeros')
    old=np.r_[arrays['core'][q.K:],flat[q.radial_free].ravel(),float(arrays['Hcap'])]
    if old.shape!=(q.base.frequency_layout_definition['original_free_size'],):
        raise ValueError('Reassemble every actual coarse free core, radial rotation and height word')
    point=array_sha(old)
    if (payload.get('latest_operator_metadata',{}).get('current_full_point_sha256')!=point
            or payload['final_geometry'].get('current_full_point_sha256')!=point):
        raise ValueError('The returned complete original variable words are not the actual final-read point')
    result,inclusion=module.embed_outer_words(old,q.base.frequency_layout_definition)
    core,omega,height=q.unpack(result)
    if (not same(core[:160],arrays['core']) or np.any(core[160:]!=0)
            or not same(omega[:,:,:161],arrays['omega_jets'][:,:,:161])
            or not same(omega[:,:,321:482],arrays['omega_jets'][:,:,161:322])
            or not same(omega[:,:,642:802],arrays['omega_jets'][:,:,322:482])
            or not same(np.array(height),arrays['Hcap'])):
        raise ValueError('Reconstruct all three correctly offset odd-sine/odd-cosine/even-sine blocks and the complete core/H')
    used=np.zeros(962,dtype=bool);used[:161]=True;used[321:482]=True;used[642:802]=True
    if np.any(omega[:,:,~used]!=0):
        raise ValueError('Every added rotation mode must be explicitly zero, never a copied old block alias')
    if (canonical(q.model)!=before_model or array_sha(q.base.initial())!=frozen_initial
            or q.reference_point_sha256!=frozen_initial):
        raise ValueError('Including an old final must not change the fixed reference, Q or exact model')
    for record in (source_record,bundle_record,caller_record):_same_bytes(record)
    record=dict(schema='actual-complete-M160-final-to-M320-zero-inclusion-v1',
        mode='actual-complete-parent-zero-inclusion',source_sha256=sha(__file__),
        actual_current_driver_sha256=caller_record['sha256'],
        actual_current_model_identity_sha256=q.identity,
        parent_report=source_record,parent_checkpoint=bundle_record,
        parent_driver_source_sha256=payload['source_sha256'],
        parent_model_identity_sha256=payload['model_identity_sha256'],
        parent_norm_identity_sha256=payload['coordinate_norm']['norm_identity_sha256'],
        original_complete_reader_sha256=family['reader_sha256'],
        complete_model_binding=model_binding,coordinate_inclusion=inclusion,
        current_full_point_sha256=array_sha(result),
        frozen_original_reference_point_sha256=frozen_initial,
        reference_M=160,current_M=320,
        complete_saved_array_sha256={name:array_sha(value) for name,value in arrays.items()},
        actual_current_free_layout=dict(J=q.J,n=q.n,K=q.K,core_size=q.core_size,
            rotation_size=q.rotation_size,free_size=q.free_size,radial_free_sha256=array_sha(q.radial_free)),
        source_complete_field_read=True,
        source_final_true_sampled_geometry_feasible=payload['final_true_sampled_geometry_feasible'],
        source_actual_accepted_direction_count=sum(int(item.get('accepted') is True)
            for item in payload.get('metric_directions',[])+payload.get('restoration_directions',[])),
        all_original_variable_words_retained_and_new_modes_zero=True,
        fixed_reference_seed_and_original_core_height_unchanged=True,
        old_norm_identity_damping_roots_physical_values_or_certificates_inherited=False,
        exact_selected_field_inclusion_requires_compatible_implicit_branch=True,
        new_initial_metric_geometry_roots_and_norm_must_be_read=True,
        current_field_already_read_by_variable_copy=False)
    return result,record


def validate_seed_metadata(value,*,report,model,transfer):
    """Pure complete inclusion evidence; this does not evaluate a new field."""
    requested=report.get('explicit_prior_final_variable_seed_requested')
    if type(requested) is not bool:
        raise ValueError('Declare whether a complete actual coarse final supplies the fine first point')
    _digest(report.get('initial_full_variable_point_sha256'))
    if value is None:
        if requested or report.get('restart') is None:
            raise ValueError('A first fine point cannot omit its actual complete coarse-variable inclusion')
        return None
    if (not requested or not isinstance(value,dict)
            or value.get('schema')!='actual-complete-M160-final-to-M320-zero-inclusion-v1'
            or value.get('mode')!='actual-complete-parent-zero-inclusion'
            or value.get('source_sha256')!=sha(__file__)
            or value.get('actual_current_driver_sha256')!=report['source_sha256']
            or value.get('actual_current_model_identity_sha256')!=canonical(model)
            or value.get('current_full_point_sha256')!=report['initial_full_variable_point_sha256']
            or value.get('frozen_original_reference_point_sha256')!=report['actual_reference_initial_full_point_sha256']
            or value.get('reference_M')!=160 or value.get('current_M')!=320
            or report.get('restart') is not None or report.get('direct_base_seed') is not None):
        raise ValueError('The actual coarse final inclusion must belong to this complete independently read M320 point')
    family=FAMILIES.get(value.get('parent_driver_source_sha256'))
    if family is None or value.get('original_complete_reader_sha256')!=family['reader_sha256']:
        raise ValueError('Bind the exact original complete source/reader family')
    for key in ('source_complete_field_read','all_original_variable_words_retained_and_new_modes_zero',
            'fixed_reference_seed_and_original_core_height_unchanged',
            'exact_selected_field_inclusion_requires_compatible_implicit_branch',
            'new_initial_metric_geometry_roots_and_norm_must_be_read'):
        if value.get(key) is not True:raise ValueError('A complete inclusion responsibility is missing: '+key)
    for key in ('old_norm_identity_damping_roots_physical_values_or_certificates_inherited',
            'current_field_already_read_by_variable_copy'):
        if value.get(key) is not False:raise ValueError('Do not inherit an old field value or certificate: '+key)
    parents=[item for item in transfer['actual_parent_reports'] if item['report']==value.get('parent_report')]
    if (len(parents)!=1 or parents[0]['actual_terminal_report_kind']!='complete-original-budget-report'
            or parents[0]['actual_driver_sha256']!=value['parent_driver_source_sha256']
            or parents[0]['actual_model_identity_sha256']!=value.get('parent_model_identity_sha256')
            or parents[0]['model_binding']!=value.get('complete_model_binding')):
        raise ValueError('The complete free point and uncapped memory must have the same actual parent')
    _digest(value.get('parent_norm_identity_sha256'))
    checkpoint=value.get('parent_checkpoint',{})
    if not isinstance(checkpoint.get('path'),str) or type(checkpoint.get('bytes')) is not int or checkpoint['bytes']<1:
        raise ValueError('Keep the actual complete old checkpoint file record')
    _digest(checkpoint.get('sha256'))
    inclusion=value.get('coordinate_inclusion',{})
    if (inclusion.get('layout_source_sha256')!=LAYOUT_SOURCE_SHA256
            or inclusion.get('layout_identity_sha256')!=model['base_complete_model']['frequency_layout_identity_sha256']
            or inclusion.get('current_full_point_sha256')!=value['current_full_point_sha256']):
        raise ValueError('Bind the independent full zero-inclusion record to the current layout and first point')
    arrays=value.get('complete_saved_array_sha256')
    if not isinstance(arrays,dict) or set(arrays)!={'omega_jets','core','Hcap','mesh','fixed_parent_core'}:
        raise ValueError('Keep every actual complete old saved array identity')
    for digest in arrays.values():_digest(digest)
    layout=value.get('actual_current_free_layout',{})
    if (set(layout)!={'J','n','K','core_size','rotation_size','free_size','radial_free_sha256'}
            or layout['J']!=923 or layout['n']!=962 or layout['K']!=3 or layout['core_size']!=317
            or layout['free_size']!=report['original_variables']
            or layout['core_size']+layout['rotation_size']+1!=layout['free_size']):
        raise ValueError('Keep the complete current M320 layout without treating M160 as its size')
    _digest(layout['radial_free_sha256'])
    count=value.get('source_actual_accepted_direction_count')
    if type(count) is not int or count<0 or type(value.get('source_final_true_sampled_geometry_feasible')) is not bool:
        raise ValueError('A returned final and an accepted direction remain distinct actual facts')
    initial=report.get('initial')
    snapshot=initial.get('endpoint_roots') if isinstance(initial,dict) else report.get('initial_endpoint_roots')
    if isinstance(snapshot,dict) and snapshot.get('current_full_point_sha256') not in (None,value['current_full_point_sha256']):
        raise ValueError('The actual initial root record belongs to another full variable point')
    return copy.deepcopy(value)


def validate_metadata(value, *, model, envelope, caller_source_sha256, carrier_sha256):
    """Pure stdlib reader for complete imported addresses, types and provenance."""
    expected = definition()
    actual_memory_sha=value.get('actual_memory_source_sha256') if isinstance(value,dict) else None
    if (not isinstance(value,dict) or value.get('schema') != SCHEMA
            or value.get('source_sha256') != sha(__file__) or value.get('definition') != expected
            or value.get('actual_current_driver_sha256') != caller_source_sha256
            or value.get('actual_current_model_identity_sha256') != canonical(model)
            or value.get('actual_current_base_model_identity_sha256') != model['base_model_identity_sha256']
            or value.get('actual_current_fixed_scalar_identity_sha256') != model['fixed_scalar_metric_identity_sha256']
            or value.get('actual_current_carrier_sha256') != carrier_sha256
            or value.get('envelope_policy_identity_sha256') != envelope['definition_identity_sha256']
            or envelope.get('actual_model_identity_sha256') != canonical(model)
            or actual_memory_sha not in (MEMORY_SOURCE_SHA256,CURRENT_MEMORY_SOURCE_SHA256)
            or envelope.get('source_sha256') != actual_memory_sha):
        raise ValueError('Read the complete actual transfer from its own new model, source and policy')
    arrays = value.get('complete_initial_explicit_address_union')
    fingerprints = _address_fingerprints(arrays)
    if fingerprints != value.get('complete_initial_explicit_role_fingerprints'):
        raise ValueError('Keep the complete actual initial known-role/protection union')
    for key in ('all_original_report_addresses_consumed_by_original_walker',
            'all_transferred_known_protection_retained','all_transferred_types_require_actual_new_field_read'):
        if value.get(key) is not True:
            raise ValueError('A declared transferred responsibility was omitted: '+key)
    for key in ('previous_feasibility_or_function_values_inherited','actual_new_field_already_screened_by_transfer',
            'original_same_model_restore_guard_changed','continuous_same_field_geometry_or_metric_certificate'):
        if value.get(key) is not False:
            raise ValueError('An address transfer is not a physical value, root or certificate: '+key)
    parents = value.get('actual_parent_reports')
    if not isinstance(parents,list):
        raise ValueError('Preserve every actual predecessor evidence list')
    branch=value.get('independent_branch_origin')
    mode=value.get('current_invocation_memory_mode')
    if branch is not None or mode not in ('same-source-restart','frequency-refinement') or not parents:
        raise ValueError('Frequency inclusion retains actual complete parent evidence, never an independent reference reset')
    known_reports = {}
    for parent in parents:
        report = parent.get('report',{})
        digest = _digest(report.get('sha256'))
        family=FAMILIES.get(parent.get('actual_driver_sha256'))
        if (family is None or not isinstance(report.get('path'),str) or type(report.get('bytes')) is not int or report['bytes'] < 1
                or parent.get('original_complete_reader_sha256') != family['reader_sha256']
                or parent.get('actual_terminal_report_kind') not in (
                    'complete-original-budget-report','explicit-original-initial-field-failure-report')
                or parent.get('all_typed_rows_transferred_without_eviction_or_count_cap') is not True
                or parent.get('previous_numeric_values_or_certificates_inherited') is not False):
            raise ValueError('Keep each actual whole parent and its independently checked terminal scope')
        _digest(parent.get('actual_model_identity_sha256'))
        _digest(parent.get('actual_typed_memory_sha256'))
        _digest(parent.get('actual_typed_core_order_sha256'))
        binding = parent.get('model_binding',{})
        if (binding.get('exact_old_complete_model_identity_sha256') != parent['actual_model_identity_sha256']
                or binding.get('exact_new_complete_model_identity_sha256') != canonical(model)
                or binding.get('full_fixed_reference_chart_scalar_mesh_seed_Q_gamma_partition_equal') is not True
                or binding.get('only_declared_current_frequency_layout_and_source_working_policy_fields_changed') is not True
                or binding.get('reference_M')!=160 or binding.get('current_M')!=320
                or binding.get('frequency_layout_identity_sha256')!=model['base_complete_model']['frequency_layout_identity_sha256']
                or binding.get('exact_selected_field_inclusion_requires_compatible_implicit_branch') is not True
                or binding.get('original_geometry_or_metric_certificate_inherited') is not False
                or binding.get('computed_float_field_equality_claimed') is not False):
            raise ValueError('Do not loosen the explicitly paid old/new complete-model relationship')
        _digest(binding.get('complete_unchanged_definition_sha256'))
        if type(parent.get('actual_typed_memory_count')) is not int or parent['actual_typed_memory_count'] < 0:
            raise ValueError('Keep actual nonnegative parent typed-memory counts')
        known_reports[digest] = parent
    count = value.get('current_invocation_parent_report_count')
    if type(count) is not int or not 0 <= count <= len(parents):
        raise ValueError('Keep actual current-parent and inherited-parent scopes distinct')
    restart = value.get('actual_same_source_restart_report')
    if restart is None:
        if value.get('prior_transfer_identity_sha256') is not None:
            raise ValueError('A fresh branch cannot invent a same-source restart')
        if mode!='frequency-refinement' or count==0:
            raise ValueError('A first refined field needs a nonempty complete actual coarse-parent transfer')
    else:
        if mode!='same-source-restart':
            raise ValueError('An actual same-source restore must retain its declared mode')
        _digest(restart.get('sha256'))
        _digest(value.get('prior_transfer_identity_sha256'))
        if not isinstance(restart.get('path'),str) or type(restart.get('bytes')) is not int or restart['bytes'] < 1:
            raise ValueError('Keep the complete actual same-source restart file record')
    rows = value.get('initial_imported_typed_rows')
    final_rows = envelope['actual_separation_memory']['rows']
    if (not isinstance(rows,list) or value.get('initial_imported_typed_count') != len(rows)
            or value.get('initial_imported_typed_sha256') != canonical(rows)
            or final_rows[:len(rows)] != rows or len(final_rows) < len(rows)):
        raise ValueError('The entire initial typed memory must remain an unchanged uncapped prefix')
    core_keys = [_typed_key(row) for row in rows]
    if len(core_keys) != len(set(core_keys)):
        raise ValueError('The complete typed union must retain one append-only entry per actual typed constraint')
    for row in rows:
        _digest(row.get('first_discovered_current_full_point_sha256'))
        for origin in row.get('source_bound_address_transfer_origins',[]):
            source = known_reports.get(origin.get('source_report_sha256'))
            if (source is None or origin.get('source_driver_sha256') != source['actual_driver_sha256']
                    or origin.get('source_model_identity_sha256') != source['actual_model_identity_sha256']
                    or type(origin.get('source_row_ordinal')) is not int
                    or not 0 <= origin['source_row_ordinal'] < source['actual_typed_memory_count']
                    or origin.get('typed_core_sha256') != _typed_key(row)
                    or origin.get('actual_new_field_value_inherited') is not False):
                raise ValueError('Keep the old discovery provenance distinct from an actual new-model scan')
            _digest(origin.get('first_discovered_source_full_point_sha256'))
    mapping = value.get('current_invocation_typed_source_order_mapping')
    if not isinstance(mapping,list):
        raise ValueError('Keep every actual imported source-row ordinal and its retained union position')
    for item in mapping:
        source = known_reports.get(item.get('parent_report_sha256'))
        ordinal = item.get('source_row_ordinal')
        target = item.get('retained_initial_ordinal')
        if (source is None or type(ordinal) is not int or not 0 <= ordinal < source['actual_typed_memory_count']
                or type(target) is not int or not 0 <= target < len(rows)
                or item.get('typed_core_sha256') != core_keys[target]):
            raise ValueError('An imported typed row was lost, reordered or given a false target address')
    if count:
        current_parents = parents[-count:]
        expected_pairs = [(item['report']['sha256'],i) for item in current_parents
            for i in range(item['actual_typed_memory_count'])]
        if [(item['parent_report_sha256'],item['source_row_ordinal']) for item in mapping] != expected_pairs:
            raise ValueError('Transfer every source typed row in its complete actual order')
    elif mapping:
        raise ValueError('A restore-only call cannot invent newly imported parent rows')
    obligations=value.get('inherited_parallel_obligations')
    if not isinstance(obligations,list):
        raise ValueError('Retain actual unresolved prior parallel obligations without inventing their reports')
    for item in obligations:
        if (not isinstance(item,dict) or item.get('parent_report_sha256') not in known_reports
                or item.get('unread_parallel_reports_or_typed_priority_claimed_restored') is not False
                or item.get('later_actual_report_merge_obligation_retained') is not True
                or not isinstance(item.get('inherited_parallel_obligations'),list)):
            raise ValueError('An unread prior obligation was removed or promoted to a known historical value')
        _digest(item.get('parent_transfer_identity_sha256'))
    return dict(schema=SCHEMA,source_sha256=sha(__file__),definition=expected,
        actual_current_model_identity_sha256=canonical(model),
        actual_memory_source_sha256=actual_memory_sha,
        actual_parent_report_count=len(parents),current_invocation_parent_report_count=count,
        same_source_restart_used=restart is not None,
        current_invocation_memory_mode=mode,independent_branch_origin=None,
        inherited_parallel_obligations=copy.deepcopy(obligations),
        pending_parallel_report_values_or_priority_inherited=False,
        complete_initial_explicit_role_fingerprints=fingerprints,
        initial_imported_typed_count=len(rows),initial_imported_typed_sha256=canonical(rows),
        current_envelope_typed_count=len(final_rows),all_imported_types_retained_as_prefix=True,
        original_full_walker_and_same_model_restore_unchanged=True,
        old_values_or_feasibility_inherited=False,new_field_already_screened=False,
        continuous_certificate=False)
