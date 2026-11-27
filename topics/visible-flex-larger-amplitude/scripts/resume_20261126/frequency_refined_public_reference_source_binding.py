#!/usr/bin/env python3
"""Pure complete source/model/report binding for the full analytic-frame and local-J3 family.

Only immutable source text and already returned JSON metadata are consumed.
There is no NumPy/Torch import, numeric matrix construction, F/J/root call,
quadrature, or inference of root/geometry success.
"""
import ast
import copy
import hashlib
import importlib.util
import sys
import json
import math
from pathlib import Path

SCHEMA = 'complete-public09-frequency-refined-analytic-frame-source-model-binding-v1'
OPERATOR_SCHEMA = 'complete-frequency-refined-public-reference-analytic-frame-normal-plane-SO3-v1'
ROOT_SNAPSHOT_SCHEMA = 'actual-frequency-refined-public-reference-analytic-frame-snapshot-v1'
LEGACY_OPERATOR_SCHEMA = 'complete-R711-reference-centred-C1-reuse-SO3-fixed-normal-plane-six-control-layer-v1'
LEGACY_OPERATOR_SHA256 = 'a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd'
LEGACY_CALIBRATION_SHA256 = '3e478bbeacbe236947070f9422ab6c75852f460f41536c68ebb3995ff0a2a991'
LEGACY_C1_SHA256 = 'ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9'
BASE_SOURCE_SHA256 = '41c865d9a505f4b7ac3b0b9c2b89a027235e78968b1f62cf7840bc119179efb2'
SOURCE_BINDINGS = {'analytic_J3': ('frequency_refined_public_reference_stage_jacobian.py', '2655c90ce07233cb3eb55ed64fa5702442ae0daaf5cafed53571afe35f5fbfa2'), 'analytic_frame': ('frequency_refined_public_reference_normal_frame.py', '787825f17de647598099fe7b4cbfc3d82b6ad90eac9943de6b67f653f092520a'), 'frame_C1': ('frequency_refined_public_reference_frame_c1.py', 'f272aaa95e63867d18015d9e92fa321f36785459377433a4433382794ae9c15a'), 'stage_matrices': ('frequency_refined_public_reference_stage_matrices.py', 'd7a6ebc317637667a18b8fb58ac8717aba8cbada981a349027bcaa60b448e4b7'), 'adjacent_matrices': ('frequency_refined_public_reference_adjacent_matrices.py', '610805744bdb5f4826d0c3a63bb769c9744639734db232ec31b3dbeaa0f89569'), 'reference_calibration': ('frequency_refined_public_reference_calibration.py', 'b72572b13f94bf5482ced96c06aa940b5097ace270c159ec1837495519d9387a'), 'endpoint': ('so3_frequency_refined_public_reference_normal_lift.py', '014fd521d315db223590d45b9b4d4da4e09975036044e533f601dcab636731d9')}
POLICY_KEYS = {'analytic_J3': 'analytic_stage_jacobian', 'frame_C1': 'normal_frame_C1_reuse', 'stage_matrices': 'detached_stage_matrix_reuse', 'adjacent_matrices': 'adjacent_normal_frame_matrices', 'analytic_frame': 'analytic_normal_frame'}
POLICY_CONSTANTS = {'analytic_J3': {'BASE_SOURCE_SHA256', 'COUNTER_KEYS', 'ENDPOINT_SCHEMA', 'METHOD_AST', 'OBSERVED_COUNTER_KEYS', 'PARENT_NORMAL_SOURCE_SHA256', 'SCHEMA'}, 'frame_C1': {'ANALYTIC_STAGE_SOURCE_SHA256', 'METHOD_AST', 'ORIGINAL_CENTERED_SOURCE', 'SCHEMA'}, 'stage_matrices': {'ANALYTIC_STAGE_SOURCE_SHA256', 'BASE_SOURCE_SHA256', 'FRAME_C1_SOURCE_SHA256', 'ORIGINAL_C1_OPERATOR_SOURCE_SHA256', 'PHASES', 'SCHEMA'}, 'adjacent_matrices': {'ANALYTIC_STAGE_SOURCE_SHA256', 'BASE_SOURCE_SHA256', 'FRAME_C1_SOURCE_SHA256', 'PARENT_OPERATOR_SOURCE_SHA256', 'SCHEMA', 'STAGE_MATRIX_SOURCE_SHA256'}, 'analytic_frame': {'BASE_SOURCE_SHA256', 'COUNTER_KEYS', 'ENDPOINT_SCHEMA', 'METHOD_AST', 'OBSERVED_COUNTER_KEYS', 'ORIGINAL_FRAME_AST_SHA256', 'PARENT_NORMAL_SOURCE_SHA256', 'SCHEMA'}}

ACTUAL_RUN09_BINDING_SHA256 = '2f8de167fb0b66a9328bb7e45c2a31b0fe985678a0af7143fc1c9e965d18ec3d'
ACTUAL_RUN09_BINDING_BYTES = 430906
ACTUAL_RUN09_TARGET_IDENTITY = '7c766fb2d5008761c35d1ee848c76ef66f75510bee860efa037e70ed4f0f1f5a'
ACTUAL_RUN09_MODEL_IDENTITY = 'd4494b14955535635b8b72b1ed3278fa8f60186d4ef7df5687ca3de5566c2f75'
ACTUAL_RUN09_PUBLIC_INPUT_SOURCE = '306b5f86e0d287ea0c6cf9abb0f326f0eec869640b52daa59cf76db1492e382a'
ACTUAL_RUN09_PRODUCER_SOURCE = '9e3d0590c6d37eb07da094128df9e3b82fc03a7e9cf784cea1831b4ab0d39a18'
ACTUAL_RUN09_CHART_IDENTITY = '90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),
        allow_nan=False).encode()).hexdigest()


def _pure(path,expected,constants,functions):
    path=Path(path).resolve()
    raw=path.read_bytes()
    if len(raw)>=100000 or hashlib.sha256(raw).hexdigest()!=expected:
        raise ValueError('Bind the whole independently declared small source: '+path.name)
    tree=ast.parse(raw)
    body=[];seen_names=set();seen_functions=set()
    for node in tree.body:
        if (isinstance(node,ast.Assign) and len(node.targets)==1
                and isinstance(node.targets[0],ast.Name) and node.targets[0].id in constants):
            ast.literal_eval(node.value)
            body.append(node);seen_names.add(node.targets[0].id)
        if isinstance(node,ast.FunctionDef) and node.name in functions:
            body.append(node);seen_functions.add(node.name)
    if seen_names!=set(constants) or seen_functions!=set(functions):
        raise ValueError('The full source-bound pure interface changed: '+path.name)
    namespace=dict(Path=Path,hashlib=hashlib,json=json,math=math,__file__=str(path))
    exec(compile(ast.Module(body=body,type_ignores=[]),'<complete bound pure analytic J3>','exec'),namespace)
    if sha(path)!=expected:
        raise ValueError('Source bytes changed during pure extraction')
    return namespace


def _policies(directory):
    directory=Path(directory).resolve()
    result={}
    for role,key in POLICY_KEYS.items():
        name,digest=SOURCE_BINDINGS[role]
        functions={'sha','definition'}
        if role in ('analytic_J3','analytic_frame'):
            functions|={'canonical','_copy','_digest','_counts','validate_metadata'}
        namespace=_pure(directory/name,digest,POLICY_CONSTANTS[role],functions)
        result[key]=namespace['definition']()
        if role in ('analytic_J3','analytic_frame'):
            result['actual_validator' if role=='analytic_J3' else 'frame_actual_validator']=namespace['validate_metadata']
    return result


def validate_current_model(model, *, roles, source_directory):
    directory=Path(source_directory).resolve()
    for role,(name,expected) in SOURCE_BINDINGS.items():
        if roles.get(role)!=expected or sha(directory/name)!=expected:
            raise ValueError('The actual full analytic-J3 source role differs: '+role)
    if (not isinstance(model,dict) or model.get('schema')!=OPERATOR_SCHEMA
            or model.get('source_sha256')!=roles['endpoint']
            or model.get('base_source_sha256')!=BASE_SOURCE_SHA256
            or model.get('base_complete_model',{}).get('source_sha256')!=BASE_SOURCE_SHA256
            or canonical(model['base_complete_model'])!=model.get('base_model_identity_sha256')):
        raise ValueError('Keep the complete actual current normal and fixed base')
    _layout(directory).validate_base_model(model['base_complete_model'],expected_base_source_sha256=BASE_SOURCE_SHA256)
    policies=_policies(directory)
    for role,key in POLICY_KEYS.items():
        if model.get(key)!=policies[key]:
            raise ValueError('The complete actual current working policy changed: '+key)
    centering=model.get('reference_centering_definition',{})
    if (centering.get('source_sha256')!=roles['reference_calibration']
            or centering.get('endpoint_source_sha256')!=roles['endpoint']
            or model.get('common_partition_for_all_angles_and_free_points') is not True
            or model.get('per_angle_adaptive_normal_partition') is not False
            or model.get('normal_stage_count',0)<1
            or model.get('implicit_control_dimension')!=6
            or model.get('normal_increment_dimension')!=3
            or model.get('complete_first_angular_implicit_dimension')!=6*model['normal_stage_count']
            or model.get('complete_second_angular_implicit_dimension')!=9*model['normal_stage_count']):
        raise ValueError('The current calibration, complete six controls or finite chain changed')
    return policies


def _bound_module(path, expected):
    path=Path(path).resolve()
    if sha(path)!=expected:raise ValueError('Keep the entire bound source '+path.name)
    name='_public09_frequency_binding_'+expected
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module
    spec.loader.exec_module(module)
    if sha(path)!=expected:raise ValueError('The bound source changed during reading')
    return module

def _layout(source_directory):
    return _bound_module(Path(source_directory)/'so3_frequency_refinement_layout.py',
        'ce188ae4bdf1ccecfbf9549897284e8dc44f4722e04e974c7a0cd045c78a3a27')

def _validate_original_parent_model(old,directory):
    if (old.get('source_sha256')!='3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc'
            or old.get('schema')!='complete-R711-reference-centred-analytic-frame-and-J3-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1'):
        raise ValueError('Use the complete actual public09 M160 analytic-frame model')
    original=_bound_module(Path(directory)/'run09_public_reference_analytic_frame_binding.py',
        '15f6393acb1f069e3c5dee62708f9350b3e329b877b19fc8a69868365a45a592')
    roles={role:record[1] for role,record in original.SOURCE_BINDINGS.items()}
    original.validate_current_model(old,roles=roles,source_directory=directory)
    return tuple(original.POLICY_KEYS.values())

def validate_frozen_point_relation(value,model,*,source_directory):
    layout_module=_layout(source_directory)
    layout=layout_module.validate_base_model(model['base_complete_model'],
        expected_base_source_sha256=BASE_SOURCE_SHA256)
    if not isinstance(value,dict) or set(value)!={'original_full_point_sha256',
            'current_full_point_sha256','coordinate_inclusion'}:
        raise ValueError('Retain the actual full frozen-reference coordinate inclusion')
    included=layout_module.validate_inclusion(value['coordinate_inclusion'],layout)
    if (included['original_full_point_sha256']!=value['original_full_point_sha256']
            or included['current_full_point_sha256']!=value['current_full_point_sha256']
            or model['frozen_moment_Q_definition']['initial_full_point_sha256']!=value['current_full_point_sha256']
            or model['reference_centering_definition']['original_reference_point_sha256']!=value['current_full_point_sha256']):
        raise ValueError('The new Q and calibration must bind the actual included frozen point')
    return copy.deepcopy(value)

def compatible_legacy_model(old,new,current_pins,*,source_directory,frozen_point_relation):
    roles={role:value[1] for role,value in current_pins.items()}
    validate_current_model(new,roles=roles,source_directory=source_directory)
    old_policy_keys=_validate_original_parent_model(old,source_directory)
    relation=validate_frozen_point_relation(frozen_point_relation,new,source_directory=source_directory)
    oldpoint,newpoint=relation['original_full_point_sha256'],relation['current_full_point_sha256']
    before,after=copy.deepcopy(old),copy.deepcopy(new)
    oldbase,newbase=old['base_complete_model'],new['base_complete_model']
    normalized=copy.deepcopy(newbase)
    for key in ('reference_M','current_M','frequency_layout_definition',
            'frequency_layout_identity_sha256','frequency_layout_source_sha256',
            'all_original_outer_free_variables_retained_and_new_modes_added',
            'frozen_reference_layout_unchanged','current_norm_layout_changed'):
        normalized.pop(key)
    normalized.update(schema=oldbase['schema'],source_sha256=oldbase['source_sha256'],M=160,
        all_original_outer_free_variables_and_norm_layout_unchanged=True)
    if normalized!=oldbase:
        raise ValueError('Keep the entire fixed scalar/reference/chart/seed/radial mesh and physical working definition')
    oldq,newq=old['frozen_moment_Q_definition'],new['frozen_moment_Q_definition']
    if (oldq.get('schema')!='supported-smooth-triangle-reference-literal-two-bubble-endpoint-Q-v1'
            or newq.get('schema')!='frequency-refined-supported-smooth-triangle-reference-literal-two-bubble-endpoint-Q-v1'
            or oldq.get('initial_full_point_sha256')!=oldpoint
            or newq.get('initial_full_point_sha256')!=newpoint
            or canonical(oldq)!=old['frozen_moment_Q_definition_identity_sha256']
            or canonical(newq)!=new['frozen_moment_Q_definition_identity_sha256']):
        raise ValueError('Bind both complete literal-Q definitions to their own exact full frozen points')
    qcopy=copy.deepcopy(newq)
    qcopy.update(schema=oldq['schema'],base_model_identity_sha256=canonical(oldbase),
        initial_full_point_sha256=oldpoint)
    if qcopy!=oldq:
        raise ValueError('Every original Q word, support and entire seed/target definition must be retained')
    oldcal,newcal=old['reference_centering_definition'],new['reference_centering_definition']
    if (oldcal.get('original_reference_point_sha256')!=oldpoint
            or newcal.get('original_reference_point_sha256')!=newpoint
            or newcal.get('frozen_reference_M')!=160 or newcal.get('current_M')!=320
            or newcal.get('current_layout_reference_point_is_old_layout_byte_identical') is not False
            or newcal.get('frozen_seed_and_original_reference_core_H_unchanged') is not True):
        raise ValueError('Distinguish exact fixed seed identity from distinct current coordinate bytes')
    calcopy=copy.deepcopy(newcal)
    for key in ('reference_point_coordinate_layout','frozen_reference_M','current_M',
            'current_layout_reference_point_is_old_layout_byte_identical',
            'frozen_seed_and_original_reference_core_H_unchanged'):
        calcopy.pop(key)
    calcopy.update(source_sha256=oldcal['source_sha256'],
        endpoint_source_sha256=oldcal['endpoint_source_sha256'],
        original_reference_point_sha256=oldpoint,base_model_identity_sha256=canonical(oldbase))
    if calcopy!=oldcal:
        raise ValueError('The complete frozen quadrature/centering definition changed beyond declared coordinates and sources')
    for key in old_policy_keys:before.pop(key)
    for key in POLICY_KEYS.values():after.pop(key)
    after.update(base_complete_model=copy.deepcopy(oldbase),
        base_model_identity_sha256=canonical(oldbase),base_source_sha256=old['base_source_sha256'],
        base_schema=old['base_schema'],M=160,frozen_moment_Q_definition=copy.deepcopy(oldq),
        frozen_moment_Q_definition_identity_sha256=canonical(oldq),
        literal_Q_input_schema=old['literal_Q_input_schema'],
        new_reference_input_binding_source_sha256=old['new_reference_input_binding_source_sha256'],
        reference_centering_definition=copy.deepcopy(oldcal),
        schema=old['schema'],source_sha256=old['source_sha256'])
    if before!=after:
        raise ValueError('An undeclared fixed target, original variable, gamma, partition, observation or implicit-selection parameter changed')
    return dict(complete_unchanged_definition_sha256=canonical(before),
        exact_old_complete_model_identity_sha256=canonical(old),
        exact_new_complete_model_identity_sha256=canonical(new),
        original_base_model_identity_sha256=canonical(oldbase),
        current_base_model_identity_sha256=canonical(newbase),
        reference_M=160,current_M=320,full_N=2048,J=923,
        frequency_layout_identity_sha256=newbase['frequency_layout_identity_sha256'],
        frozen_original_point_relation=relation,
        full_fixed_reference_chart_profile_seed_mesh_Q_gamma_partition_and_observer_equal=True,
        only_declared_current_frequency_layout_and_complete_source_policies_changed=True,
        computed_float_field_equality_claimed=False,
        exact_selected_field_inclusion_requires_compatible_implicit_branch=True,
        original_geometry_or_metric_certificate_inherited=False)

def frequency_refinement_binding(report,*,roles,source_directory):
    module=_layout(source_directory)
    model=report['representation'];base=model['base_complete_model']
    layout=module.validate_base_model(base,expected_base_source_sha256=BASE_SOURCE_SHA256)
    if (roles.get('frequency_layout')!=sha(module.__file__)
            or report.get('frequency_layout_definition')!=layout
            or report.get('frequency_layout_identity_sha256')!=canonical(layout)
            or report.get('frequency_layout_source',{}).get('sha256')!=sha(module.__file__)
            or report.get('reference_M')!=160 or report.get('current_M')!=320
            or report.get('M')!=320 or report.get('N')!=2048 or report.get('J')!=923
            or report.get('original_variables')!=layout['current_free_size']
            or report.get('radial_observation_refinement_performed') is not False
            or report.get('angular_observation_refinement_performed') is not False
            or report.get('saved_parent_Phi_used_as_current_baseline') is not False):
        raise ValueError('Declare the entire M-only inclusion and unchanged N/radial observation rules')
    norm=report['coordinate_norm']
    if canonical({k:v for k,v in norm.items() if k!='norm_identity_sha256'})!=norm.get('norm_identity_sha256'):
        raise ValueError('The complete current norm identity must be independently read')
    transfer=report['material_envelope_transfer']
    relation=validate_frozen_point_relation(transfer['frozen_original_point_relation'],
        model,source_directory=source_directory)
    record=report.get('frequency_refinement')
    if (not isinstance(record,dict)
            or record.get('frequency_layout_identity_sha256')!=canonical(layout)
            or record.get('current_full_point_sha256')!=report.get('initial_full_variable_point_sha256')
            or record.get('frozen_original_point_relation')!=relation
            or record.get('source_sha256')!=report.get('material_envelope_transfer_source',{}).get('sha256')):
        raise ValueError('The actual fine first point and fixed seed inclusion must remain separate')
    mode=record.get('mode')
    if mode in ('fresh-original-reference-zero-inclusion','terminal-history-original-reference-zero-inclusion'):
        if (record['current_full_point_sha256']!=relation['current_full_point_sha256']
                or report.get('restart') is not None
                or report.get('explicit_prior_final_variable_seed_requested') is not False
                or report.get('prior_envelope_final_variable_seed') is not None):
            raise ValueError('A fresh/reference point must not impersonate a returned parent final')
        expected=('explicit-independent-branch' if mode=='fresh-original-reference-zero-inclusion'
            else 'strict-current-target-terminal-transfer')
        if transfer.get('current_invocation_memory_mode')!=expected:
            raise ValueError('Keep explicit fresh and actual terminal-history modes distinct')
    elif mode=='actual-complete-parent-zero-inclusion':
        seed=report.get('prior_envelope_final_variable_seed')
        if (not isinstance(seed,dict) or record.get('coordinate_inclusion')!=seed.get('coordinate_inclusion')
                or record.get('parent_report')!=seed.get('parent_report')
                or report.get('explicit_prior_final_variable_seed_requested') is not True):
            raise ValueError('Bind the real complete prior final and all its uncapped history')
        included=module.validate_inclusion(record['coordinate_inclusion'],layout)
        if included['current_full_point_sha256']!=record['current_full_point_sha256']:
            raise ValueError('The full zero inclusion must equal the actual first M320 point')
    elif mode=='same-source-complete-restart':
        if (report.get('restart') is None or record.get('restart_report')!=transfer.get('actual_same_source_restart_report')
                or report.get('explicit_prior_final_variable_seed_requested') is not False):
            raise ValueError('A same-source restart requires its actual complete source-bound report')
    else:raise ValueError('Use one explicitly declared M320 input mode')
    for key in ('all_original_free_variables_retained','all_new_mode_initialization_explicit',
            'fixed_reference_seed_unchanged','new_initial_field_roots_geometry_and_norm_require_read'):
        if record.get(key) is not True:raise ValueError('Keep every complete inclusion responsibility: '+key)
    if record.get('old_values_roots_norm_or_certificates_inherited') is not False:
        raise ValueError('No old computed field or certificate may be inherited')
    return dict(schema='actual-public09-M320-complete-refinement-binding-v1',
        source_sha256=sha(__file__),layout=layout,layout_identity_sha256=canonical(layout),
        reference_M=160,current_M=320,full_N=2048,J=923,mode=mode,
        actual_initial_full_point_sha256=record['current_full_point_sha256'],
        frozen_original_point_relation=relation,
        all_original_free_variables_retained=True,
        exact_selected_field_inclusion_requires_compatible_implicit_branch=True,
        old_field_values_or_certificates_inherited=False)

def read_actual(report,*,roles,source_directory):
    """Validate every actual new snapshot and full metadata at its OWN point."""
    model=report['representation']
    policies=validate_current_model(model,roles=roles,source_directory=source_directory)
    expected=policies['analytic_stage_jacobian']
    if (report.get('analytic_stage_jacobian_definition')!=expected
            or report.get('analytic_stage_jacobian_source',{}).get('sha256')!=roles['analytic_J3']
            or report.get('analytic_stage_J3_full_original_residual_and_chain_retained') is not True
            or report.get('analytic_stage_J3_speedup_or_rounding_certified') is not False):
        raise ValueError('Bind the complete declared analytic partial without inherited success or speed')
    frame_expected=policies['analytic_normal_frame']
    if (report.get('analytic_normal_frame_definition')!=frame_expected
            or report.get('analytic_normal_frame_source',{}).get('sha256')!=roles['analytic_frame']
            or report.get('analytic_normal_frame_full_six_columns_and_active_graph_retained') is not True
            or report.get('analytic_normal_frame_speedup_or_rounding_certified') is not False):
        raise ValueError('Bind the complete six-control derivative without borrowing a cost or certificate')
    frame_validator=policies['frame_actual_validator']
    validator=policies['actual_validator']
    count=0
    metadata_count=0
    def visit(value):
        nonlocal count,metadata_count
        if isinstance(value,dict):
            if value.get('schema')==ROOT_SNAPSHOT_SCHEMA:
                if (value.get('operator_schema')!=OPERATOR_SCHEMA
                        or value.get('operator_source_sha256')!=roles['endpoint']
                        or value.get('model_identity_sha256')!=canonical(model)):
                    raise ValueError('An analytic matrix snapshot belongs to another actual field')
                validator(value.get('analytic_stage_jacobian'),model=model,source_by_role=roles,
                    current_full_point_sha256=value.get('current_full_point_sha256'))
                frame_validator(value.get('analytic_normal_frame'),model=model,source_by_role=roles,
                    current_full_point_sha256=value.get('current_full_point_sha256'))
                count+=1
            elif value.get('schema')==OPERATOR_SCHEMA and 'model' in value:
                if value['model']!=model or value.get('model_identity_sha256')!=canonical(model):
                    raise ValueError('A full matrix metadata record belongs to another actual field')
                validator(value.get('analytic_stage_jacobian'),model=model,source_by_role=roles,
                    current_full_point_sha256=value.get('current_full_point_sha256'))
                frame_validator(value.get('analytic_normal_frame'),model=model,source_by_role=roles,
                    current_full_point_sha256=value.get('current_full_point_sha256'))
                metadata_count+=1
            for child in value.values():
                visit(child)
        elif isinstance(value,list):
            for child in value:
                visit(child)
    visit(report)
    latest=report.get('latest_operator_metadata')
    actual=None
    frame_actual=None
    if latest:
        if latest.get('schema')!=OPERATOR_SCHEMA or latest.get('model')!=model:
            raise ValueError('Do not substitute another latest operator record')
        actual=validator(latest.get('analytic_stage_jacobian'),model=model,source_by_role=roles,
            current_full_point_sha256=latest.get('current_full_point_sha256'))
        frame_actual=frame_validator(latest.get('analytic_normal_frame'),model=model,source_by_role=roles,
            current_full_point_sha256=latest.get('current_full_point_sha256'))
    elif report.get('complete') is True:
        raise ValueError('A complete budget must retain its own actual local-matrix counters')
    return dict(schema=SCHEMA,source_sha256=sha(__file__),
        actual_analytic_source_sha256=roles['analytic_J3'],
        actual_operator_source_sha256=roles['endpoint'],
        actual_model_identity_sha256=canonical(model),
        definition=expected,definition_identity_sha256=canonical(expected),
        actual_bound_snapshot_count=count,actual_bound_full_metadata_count=metadata_count,
        latest_actual_diagnostics=actual,
        frequency_refinement=frequency_refinement_binding(report,roles=roles,source_directory=source_directory),
        analytic_normal_frame=dict(source_sha256=roles['analytic_frame'],
            actual_operator_source_sha256=roles['endpoint'],
            actual_model_identity_sha256=canonical(model),definition=frame_expected,
            definition_identity_sha256=canonical(frame_expected),
            actual_bound_snapshot_count=count,actual_bound_full_metadata_count=metadata_count,
            latest_actual_diagnostics=frame_actual,snapshot_values_backfilled_from_latest=False,
            full_six_columns_and_all_upstream_J_retained=True,
            current_scientific_values_recomputed=False),
        snapshot_values_backfilled_from_latest=False,
        original_full_stage_residual_domain_Armijo_and_all_upstream_J_retained=True,
        local_J3_is_not_an_endpoint_root_or_geometry_certificate=True,
        every_matrix_request_is_a_complete_three_by_three_batch=True,
        source_or_binding_failures_silently_fallback=False,
        current_scientific_values_recomputed=False)



def bind_actual_run09_input(path, *, current_files=None):
    """Read only the genuinely returned whole input binding and all six inputs.

    The old/current carrier reconstruction is never rerun here. The complete
    source-bound memory separately rechecks its public snapshots, full chart,
    original P0 and actual carrier arrays before the first physical field.
    """
    path=Path(path).resolve()
    raw=path.read_bytes()
    record=dict(path=str(path),sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw))
    if (record['sha256']!=ACTUAL_RUN09_BINDING_SHA256
            or record['bytes']!=ACTUAL_RUN09_BINDING_BYTES):
        raise ValueError('Use the whole actually returned run09 input binding, not a relabelled current file')
    payload=json.loads(raw)
    target=payload.get('fixed_target_definition',{})
    evidence=target.get('complete_public_input_evidence',{})
    if (payload.get('schema')!='material-envelope-actual-public-run09-fixed-target-binding-v1'
            or payload.get('producer',{}).get('source_sha256')!=ACTUAL_RUN09_PRODUCER_SOURCE
            or payload.get('fixed_target_definition_identity_sha256')!=ACTUAL_RUN09_TARGET_IDENTITY
            or canonical(target)!=ACTUAL_RUN09_TARGET_IDENTITY
            or target.get('schema')!='independently-frozen-actual-public-run09-scalar-and-material-chart-v1'
            or target.get('definition_source_sha256')!=ACTUAL_RUN09_PRODUCER_SOURCE
            or target.get('public_input_binding_source_sha256')!=ACTUAL_RUN09_PUBLIC_INPUT_SOURCE
            or target.get('current_reference_model_identity_sha256')!=ACTUAL_RUN09_MODEL_IDENTITY
            or canonical(target.get('complete_current_reference_model'))!=ACTUAL_RUN09_MODEL_IDENTITY
            or target.get('fixed_chart_core_array_record',{}).get('sha256')!=ACTUAL_RUN09_CHART_IDENTITY
            or target.get('same_original_fixed_chart') is not True
            or target.get('same_mathematical_g_claimed') is not False
            or evidence.get('actual_run_id')!='45943410994'
            or evidence.get('actual_run_attempt')!='1'
            or evidence.get('actual_reference_step_id')!='independent-axisymmetric-R690-reference-prepare-v2-first-20261127-09'
            or canonical(evidence)!=target.get('complete_public_input_evidence_identity_sha256')):
        raise ValueError('The complete returned run09 target/evidence/source identity changed')
    files=evidence.get('current_files')
    expected={'current_warm_bundle','current_node_report','current_scalar_input',
        'current_carrier','current_preparation_report','current_reference_bundle'}
    if not isinstance(files,dict) or set(files)!=expected:
        raise ValueError('Every one of the six actual run09 input records is required')
    supplied={} if current_files is None else current_files
    if not isinstance(supplied,dict) or not set(supplied)<=expected:
        raise ValueError('Only explicit original complete input roles can be matched')
    for role,declared in files.items():
        source=Path(declared['path']).resolve()
        data=source.read_bytes()
        actual=dict(path=str(source),sha256=hashlib.sha256(data).hexdigest(),bytes=len(data))
        if actual!=declared or (role in supplied and Path(supplied[role]).resolve()!=source):
            raise ValueError('The current entry input is not its whole actual run09 file: '+role)
    if path.read_bytes()!=raw:
        raise ValueError('The immutable actual input binding changed while being consumed')
    return dict(schema='actual-run09-returned-input-entry-binding-v1',
        source_sha256=sha(__file__),actual_binding_file=record,
        actual_input_producer_source_sha256=ACTUAL_RUN09_PRODUCER_SOURCE,
        actual_public_input_binding_source_sha256=ACTUAL_RUN09_PUBLIC_INPUT_SOURCE,
        actual_run_id='45943410994',actual_run_attempt='1',
        actual_reference_step_id=evidence['actual_reference_step_id'],
        actual_reference_model_identity_sha256=ACTUAL_RUN09_MODEL_IDENTITY,
        actual_fixed_target_definition_identity_sha256=ACTUAL_RUN09_TARGET_IDENTITY,
        actual_fixed_chart_core_sha256=ACTUAL_RUN09_CHART_IDENTITY,
        complete_current_input_files=copy.deepcopy(files),
        all_six_current_whole_files_reread=True,
        complete_memory_public_snapshot_and_array_validation_still_required=True,
        same_original_fixed_chart=True,same_mathematical_g_claimed=False,
        not_claimed_metric_relation_is_not_a_claim_of_mathematical_inequality=True,
        physical_values_roots_or_certificates_inherited=False)

def independent_chart_binding(report, envelope_binding):
    checked=envelope_binding['actual_metadata'].get('independent_fixed_target_validation')
    target=report.get('independent_fixed_target_definition')
    identity=report.get('independent_fixed_target_definition_identity_sha256')
    if checked is None:
        raise ValueError('This run09 entry always requires its complete actual public input binding')
    path=report['material_envelope']['historical_address_binding']['actual_path_binding']
    actual=bind_actual_run09_input(path['binding_file']['path'])
    if (actual!=report.get('actual_public_reference_input_binding')
            or actual['actual_binding_file']!=path['binding_file']
            or identity!=ACTUAL_RUN09_TARGET_IDENTITY):
        raise ValueError('Read the same complete run09 binding before the first field and in the actual report')
    base=report['representation']['base_complete_model']
    reference=base['complete_axisymmetric_reference_model']
    if (not isinstance(target,dict) or target!=path.get('fixed_target_definition')
            or identity!=canonical(target) or identity!=path.get('fixed_target_definition_identity_sha256')
            or identity!=checked.get('fixed_target_definition_identity_sha256')
            or checked!=report.get('independent_fixed_target_validation')
            or target.get('complete_current_reference_model')!=reference
            or target.get('current_reference_model_identity_sha256')!=canonical(reference)
            or checked.get('actual_current_model_identity_sha256')!=canonical(reference)
            or target.get('complete_current_reference_bundle_sha256')!=report['bundle_sha256']
            or target.get('complete_current_reference_bundle_sha256')!=base['initial_reference_bundle_sha256']
            or target.get('fixed_chart_core_array_record',{}).get('sha256')!=reference['fixed_chart_core_sha256']
            or base['fixed_chart_core_sha256']!=reference['fixed_chart_core_sha256']
            or checked.get('current_fixed_chart_core_sha256')!=reference['fixed_chart_core_sha256']
            or target.get('same_original_fixed_chart') is not True
            or target.get('same_mathematical_g_claimed') is not False):
        raise ValueError('The verified full target, all chart words and actual report reference must be identical')
    return dict(definition_identity_sha256=identity,
        actual_reference_model_identity_sha256=canonical(reference),
        actual_reference_bundle_sha256=report['bundle_sha256'],
        actual_fixed_chart_core_sha256=reference['fixed_chart_core_sha256'],
        complete_target_and_actual_report_reference_equal=True,
        actual_full_chart_words_verified=True,same_original_fixed_chart=True,
        actual_returned_public_input_binding=actual,
        same_mathematical_g_claimed=False,old_values_or_certificates_inherited=False)
