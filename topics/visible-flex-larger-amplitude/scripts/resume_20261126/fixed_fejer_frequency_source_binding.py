#!/usr/bin/env python3
"""Pure complete source/model/report binding for the full analytic-frame and local-J3 family.

Only immutable source text and already returned JSON metadata are consumed.
There is no NumPy/Torch import, numeric matrix construction, F/J/root call,
quadrature, or inference of root/geometry success.
"""
import ast
import copy
import importlib.util
import sys
import hashlib
import json
import math
import textwrap
from pathlib import Path

SCHEMA = "complete-fixed-fejer-frequency-refined-source-model-binding-v1"
OPERATOR_SCHEMA = "complete-fixed-fejer-frequency-refined-immutable-point-normal-layer-v1"
ROOT_SNAPSHOT_SCHEMA = "actual-fixed-fejer-frequency-refined-current-point-snapshot-v1"
LEGACY_OPERATOR_SCHEMA = 'complete-R711-reference-centred-C1-reuse-SO3-fixed-normal-plane-six-control-layer-v1'
LEGACY_OPERATOR_SHA256 = 'a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd'
LEGACY_CALIBRATION_SHA256 = '3e478bbeacbe236947070f9422ab6c75852f460f41536c68ebb3995ff0a2a991'
LEGACY_C1_SHA256 = 'ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9'
BASE_SOURCE_SHA256 = "f7058f9c9d3f02292b738b360b116062b60bcf07907286acb42346eb431bdf9a"
SOURCE_BINDINGS = {"analytic_J3":["fixed_fejer_frequency_stage_jacobian.py","740d3b39fcbdbb766962d26d3ec960b8883810418af83f13bd7b55c11776dbc3"],"frame_C1":["fixed_fejer_frequency_frame_c1.py","9d001b492aa49058b545e05eb67c6eb2413fa512580393243955f8a706015fdd"],"stage_matrices":["fixed_fejer_frequency_stage_matrices.py","f30eac74cfb436cd40fa3413d4ca4c037ef1fe79ac05b442738de07eef522642"],"adjacent_matrices":["fixed_fejer_frequency_adjacent_matrices.py","59e9089bc991136ff9e1e2fd4a37663d7f91c03837eac9bd49c8d49c206ce015"],"reference_calibration":["fixed_fejer_frequency_calibration.py","90a8c8eae8d67d5d09fc09ad0593872e40037256779cb94e5eab5fbbff25b11e"],"endpoint":["fixed_fejer_frequency_normal_lift.py","60769d4999af17f6dc904400e414e3f34ec1000bd84529ad168dca67f6889b5f"],"analytic_frame":["fixed_fejer_frequency_normal_frame.py","e165dda2543dd4175fa1f7187dfd28cad84ac08ec95a24f27a5e6addcaa2fc34"],"closure_values":["fixed_fejer_frequency_closure_values.py","6949ca97c49d338761ef2bc5e748ed9a55e20682a6e6225a7fc2bc63ead2bc88"]}
POLICY_KEYS = {"analytic_J3": "analytic_stage_jacobian", "frame_C1": "normal_frame_C1_reuse", "stage_matrices": "detached_stage_matrix_reuse", "adjacent_matrices": "adjacent_normal_frame_matrices", "analytic_frame": "analytic_normal_frame", "closure_values": "detached_closure_value_reuse"}
POLICY_CONSTANTS = {"analytic_J3": {"BASE_SOURCE_SHA256", "COUNTER_KEYS", "ENDPOINT_SCHEMA", "METHOD_AST", "OBSERVED_COUNTER_KEYS", "PARENT_NORMAL_SOURCE_SHA256", "SCHEMA", "METHOD_SOURCE_OVERRIDES", "CLOSURE_VALUE_SOURCE_SHA256"}, "frame_C1": {"ANALYTIC_STAGE_SOURCE_SHA256", "METHOD_AST", "ORIGINAL_CENTERED_SOURCE", "SCHEMA", "METHOD_SOURCE_OVERRIDES", "CLOSURE_VALUE_SOURCE_SHA256"}, "stage_matrices": {"ANALYTIC_STAGE_SOURCE_SHA256", "BASE_SOURCE_SHA256", "FRAME_C1_SOURCE_SHA256", "ORIGINAL_C1_OPERATOR_SOURCE_SHA256", "PHASES", "SCHEMA"}, "adjacent_matrices": {"ANALYTIC_STAGE_SOURCE_SHA256", "BASE_SOURCE_SHA256", "FRAME_C1_SOURCE_SHA256", "PARENT_OPERATOR_SOURCE_SHA256", "SCHEMA", "STAGE_MATRIX_SOURCE_SHA256"}, "analytic_frame": {"BASE_SOURCE_SHA256", "COUNTER_KEYS", "ENDPOINT_SCHEMA", "METHOD_AST", "OBSERVED_COUNTER_KEYS", "ORIGINAL_FRAME_AST_SHA256", "PARENT_NORMAL_SOURCE_SHA256", "SCHEMA", "METHOD_SOURCE_OVERRIDES", "CLOSURE_VALUE_SOURCE_SHA256"}, "closure_values": {"COUNTER_KEYS", "SCHEMA", "DEFINITION_SCHEMA", "ENDPOINT_SCHEMA", "NORMAL_PARENT_SHA256", "BASE_SOURCE_SHA256", "TORCH_VERSION"}}

FIXED_INPUT_BINDING_SOURCE_SHA256 = "3da43e82722dfb4548ff4e8b454d47ec2626ece76084c7801c0be5b8c989670f"
FIXED_INPUT_BINDING_NAME = "fixed_fejer_reference_input_binding.py"
FIXED_REFERENCE_SOURCE_SHA256 = "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb"
FIXED_MAKER_SOURCE_SHA256 = "89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60"


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
    namespace=dict(Path=Path,hashlib=hashlib,json=json,math=math,ast=ast,textwrap=textwrap,__file__=str(path))
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
        if role in ('analytic_J3','analytic_frame','frame_C1'):
            functions|={'canonical','_ast_value','complete_method_ast'}
        if role in ('analytic_J3','analytic_frame','closure_values'):
            functions|={'canonical','_copy','_digest','_counts','validate_metadata'}
        namespace=_pure(directory/name,digest,POLICY_CONSTANTS[role],functions)
        result[key]=namespace['definition']()
        if role in ('analytic_J3','analytic_frame','closure_values'):
            validator_key={'analytic_J3':'actual_validator',
                'analytic_frame':'frame_actual_validator',
                'closure_values':'closure_actual_validator'}[role]
            result[validator_key]=namespace['validate_metadata']
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


IMMUTABLE_POINT_PARENT_DRIVER = ('fullclosed_fixed_fejer_immutable_point_so3_qp.py',
    '477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd')
IMMUTABLE_POINT_PARENT_BINDING = ('fixed_fejer_complete_source_binding.py',
    '3b3f2322eb1d1f6304e71e4d972a8e45ba2b5dd6605501d293212de46b5c5c88')
IMMUTABLE_POINT_PARENT_NORMAL = '1aa64d7731333f8ae008f86b717421abbbbfdb7f4c3edb1173f93754364bd778'


def _bound_module(path, expected):
    path=Path(path).resolve()
    if sha(path)!=expected:raise ValueError('Keep the entire bound source '+path.name)
    name='_actual_fixed_fejer_frequency_binding_'+expected
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module
    spec.loader.exec_module(module)
    if sha(path)!=expected:raise ValueError('The bound source changed during reading')
    return module


def _layout(source_directory):
    return _bound_module(Path(source_directory)/'fixed_fejer_frequency_layout.py',
        '67c5503e8df036aa1468a3df2f395f5a33c91c4309520fbb8862b39c2495a251')


def _validate_original_parent_model(old,directory,current_pins):
    if (old.get('source_sha256')!=IMMUTABLE_POINT_PARENT_NORMAL
            or old.get('schema')!='complete-fixed-fejer-reference-centred-immutable-point-closure-values-analytic-frame-J3-normal-layer-v1'):
        raise ValueError('Use the complete actual 477499 Fejer M160 source-bound field')
    directory=Path(directory).resolve()
    topic=directory.parents[1]
    driver_path=directory/IMMUTABLE_POINT_PARENT_DRIVER[0]
    binding_path=directory/IMMUTABLE_POINT_PARENT_BINDING[0]
    if (current_pins.get('frequency_parent_driver',(None,None))[1]!=IMMUTABLE_POINT_PARENT_DRIVER[1]
            or current_pins.get('frequency_parent_binding',(None,None))[1]!=IMMUTABLE_POINT_PARENT_BINDING[1]
            or sha(driver_path)!=IMMUTABLE_POINT_PARENT_DRIVER[1]
            or sha(binding_path)!=IMMUTABLE_POINT_PARENT_BINDING[1]):
        raise ValueError('Bind the entire actual original Fejer M160 driver and pure model reader')
    records=[n for n in ast.parse(driver_path.read_bytes()).body
        if isinstance(n,ast.Assign) and len(n.targets)==1
        and isinstance(n.targets[0],ast.Name) and n.targets[0].id=='SOURCE_PINS']
    if len(records)!=1:
        raise ValueError('The complete actual parent has one literal full source role table')
    old_pins=ast.literal_eval(records[0].value)
    if not isinstance(old_pins,dict) or len(old_pins)!=110:
        raise ValueError('Retain all 110 complete source roles of the actual Fejer M160 parent')
    for role,pair in old_pins.items():
        if (not isinstance(pair,(list,tuple)) or len(pair)!=2
                or tuple(pair) not in {tuple(v) for v in current_pins.values()}
                or sha(topic/pair[0])!=pair[1]):
            raise ValueError('A full source of the actual parent is absent or changed: '+role)
    module_name='_complete_frequency_parent_binding_'+IMMUTABLE_POINT_PARENT_BINDING[1]
    if module_name not in sys.modules:
        spec=importlib.util.spec_from_file_location(module_name,binding_path)
        module=importlib.util.module_from_spec(spec)
        sys.modules[module_name]=module
        spec.loader.exec_module(module)
    module=sys.modules[module_name]
    if sha(module.validate_current_model.__code__.co_filename)!=IMMUTABLE_POINT_PARENT_BINDING[1]:
        raise ValueError('Use the original complete Fejer M160 model validator')
    old_policies=module.validate_current_model(old,
        roles={role:pair[1] for role,pair in old_pins.items()},source_directory=directory)
    if sha(driver_path)!=IMMUTABLE_POINT_PARENT_DRIVER[1] or sha(binding_path)!=IMMUTABLE_POINT_PARENT_BINDING[1]:
        raise ValueError('The entire actual parent source changed during validation')
    return tuple(module.POLICY_KEYS.values())




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
    old_policy_keys=_validate_original_parent_model(old,source_directory,current_pins)
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
    if (oldq.get('schema')!='fixed-fejer-supported-reference-literal-two-bubble-endpoint-Q-v1'
            or newq.get('schema')!='fixed-fejer-frequency-refined-literal-two-bubble-endpoint-Q-v1'
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
    return dict(schema='actual-fixed-fejer-M320-complete-refinement-binding-v1',
        source_sha256=sha(__file__),layout=layout,layout_identity_sha256=canonical(layout),
        reference_M=160,current_M=320,full_N=2048,J=923,mode=mode,
        actual_initial_full_point_sha256=record['current_full_point_sha256'],
        frozen_original_point_relation=relation,
        all_original_free_variables_retained=True,
        exact_selected_field_inclusion_requires_compatible_implicit_branch=True,
        old_field_values_or_certificates_inherited=False)


def read_actual(report,*,roles,source_directory):
    """Validate every actual snapshot and full metadata at its OWN point."""
    model=report['representation']
    policies=validate_current_model(model,roles=roles,source_directory=source_directory)
    expected=policies['analytic_stage_jacobian']
    if (report.get('analytic_stage_jacobian_definition')!=expected
            or report.get('analytic_stage_jacobian_source',{}).get('sha256')!=roles['analytic_J3']
            or report.get('analytic_stage_J3_full_original_residual_and_chain_retained') is not True
            or report.get('analytic_stage_J3_speedup_or_rounding_certified') is not False):
        raise ValueError('Bind the complete analytic partial without inherited success or speed')
    frame_expected=policies['analytic_normal_frame']
    if (report.get('analytic_normal_frame_definition')!=frame_expected
            or report.get('analytic_normal_frame_source',{}).get('sha256')!=roles['analytic_frame']
            or report.get('analytic_normal_frame_full_six_columns_and_active_graph_retained') is not True
            or report.get('analytic_normal_frame_speedup_or_rounding_certified') is not False):
        raise ValueError('Bind the full six-control derivative and actual upstream graph')
    closure_expected=policies['detached_closure_value_reuse']
    if (report.get('detached_closure_value_reuse_definition')!=closure_expected
            or report.get('detached_closure_value_source',{}).get('sha256')!=roles['closure_values']
            or report.get('closure_value_all_final_original_equation_checks_retained') is not True
            or report.get('closure_value_active_J_and_transpose_use_original') is not True
            or report.get('closure_value_speedup_rounding_or_root_certificate') is not False):
        raise ValueError('A value cache cannot replace any stage, active derivative or original final check')
    validators=(('analytic_stage_jacobian',policies['actual_validator']),
        ('analytic_normal_frame',policies['frame_actual_validator']),
        ('detached_closure_value_reuse',policies['closure_actual_validator']))
    count=0
    metadata_count=0
    def validate_at_own_point(value):
        for key,validator in validators:
            validator(value.get(key),model=model,source_by_role=roles,
                current_full_point_sha256=value.get('current_full_point_sha256'))
    def visit(value):
        nonlocal count,metadata_count
        if isinstance(value,dict):
            if value.get('schema')==ROOT_SNAPSHOT_SCHEMA:
                if (value.get('operator_schema')!=OPERATOR_SCHEMA
                        or value.get('operator_source_sha256')!=roles['endpoint']
                        or value.get('model_identity_sha256')!=canonical(model)):
                    raise ValueError('A complete snapshot belongs to another actual field')
                validate_at_own_point(value);count+=1
            elif value.get('schema')==OPERATOR_SCHEMA and 'model' in value:
                if value['model']!=model or value.get('model_identity_sha256')!=canonical(model):
                    raise ValueError('A full metadata record belongs to another actual field')
                validate_at_own_point(value);metadata_count+=1
            for child in value.values():visit(child)
        elif isinstance(value,list):
            for child in value:visit(child)
    visit(report)
    latest=report.get('latest_operator_metadata')
    actuals={key:None for key,_ in validators}
    if latest:
        if latest.get('schema')!=OPERATOR_SCHEMA or latest.get('model')!=model:
            raise ValueError('Do not substitute another latest operator record')
        for key,validator in validators:
            actuals[key]=validator(latest.get(key),model=model,source_by_role=roles,
                current_full_point_sha256=latest.get('current_full_point_sha256'))
    elif report.get('complete') is True:
        raise ValueError('A complete budget must retain its actual full numerical-policy metadata')
    def summary(role,key,definition):
        return dict(source_sha256=roles[role],actual_operator_source_sha256=roles['endpoint'],
            actual_model_identity_sha256=canonical(model),definition=definition,
            definition_identity_sha256=canonical(definition),
            actual_bound_snapshot_count=count,actual_bound_full_metadata_count=metadata_count,
            latest_actual_diagnostics=actuals[key],snapshot_values_backfilled_from_latest=False,
            current_scientific_values_recomputed=False)
    frame=summary('analytic_frame','analytic_normal_frame',frame_expected)
    frame['full_six_columns_and_all_upstream_J_retained']=True
    closure=summary('closure_values','detached_closure_value_reuse',closure_expected)
    closure.update(all_stage_and_chain_final_equations_reread_by_original_formula=True,
        active_J_and_transpose_bypass_cache=True,
        mutable_progress_file_not_consumed_as_immutable_evidence=True,
        speedup_root_or_geometry_certificate_inferred=False)
    return dict(schema=SCHEMA,source_sha256=sha(__file__),
        actual_analytic_source_sha256=roles['analytic_J3'],
        actual_operator_source_sha256=roles['endpoint'],
        actual_model_identity_sha256=canonical(model),
        definition=expected,definition_identity_sha256=canonical(expected),
        actual_bound_snapshot_count=count,actual_bound_full_metadata_count=metadata_count,
        latest_actual_diagnostics=actuals['analytic_stage_jacobian'],
        analytic_normal_frame=frame,detached_closure_value_reuse=closure,
        frequency_refinement=frequency_refinement_binding(report,roles=roles,source_directory=source_directory),
        snapshot_values_backfilled_from_latest=False,
        original_full_stage_residual_domain_Armijo_and_all_upstream_J_retained=True,
        local_J3_is_not_an_endpoint_root_or_geometry_certificate=True,
        every_matrix_request_is_a_complete_three_by_three_batch=True,
        source_or_binding_failures_silently_fallback=False,current_scientific_values_recomputed=False)

def bind_fixed_fejer_input(path, *, current_files=None):
    """Consume the real complete recipe, reference, six files and two distinct identities."""
    directory=Path(__file__).resolve().parent
    source=directory/FIXED_INPUT_BINDING_NAME
    if sha(source)!=FIXED_INPUT_BINDING_SOURCE_SHA256:
        raise ValueError('The complete fixed-reference actual-file binder changed')
    key='_fixed_fejer_actual_reference_'+FIXED_INPUT_BINDING_SOURCE_SHA256
    module=sys.modules.get(key)
    if module is None:
        spec=importlib.util.spec_from_file_location(key,source)
        module=importlib.util.module_from_spec(spec);sys.modules[key]=module
        spec.loader.exec_module(module)
    for name in ('read_binding','validate_binding','current_projection'):
        if sha(getattr(module,name).__code__.co_filename)!=FIXED_INPUT_BINDING_SOURCE_SHA256:
            raise ValueError('The actual complete fixed-input binding method changed')
    payload,checked=module.read_binding(path,current_files=current_files)
    return dict(schema='actual-fixed-fejer-complete-input-entry-binding-v1',
        source_sha256=sha(__file__),actual_binding_file=checked['actual_binding_file'],
        actual_input_producer_source_sha256=FIXED_REFERENCE_SOURCE_SHA256,
        actual_pure_input_binding_source_sha256=FIXED_INPUT_BINDING_SOURCE_SHA256,
        actual_fixed_input_maker_source_sha256=FIXED_MAKER_SOURCE_SHA256,
        actual_run_id=checked['actual_run_id'],actual_run_attempt=checked['actual_run_attempt'],
        actual_reference_model_identity_sha256=checked['actual_current_model_identity_sha256'],
        actual_fixed_target_definition_identity_sha256=checked['fixed_target_definition_identity_sha256'],
        mathematical_target_identity_sha256=checked['mathematical_target_identity_sha256'],
        actual_fixed_chart_core_sha256=checked['current_fixed_chart_core_sha256'],
        complete_current_input_files=copy.deepcopy(checked['current_input_records']),
        complete_input_validation=checked,
        all_six_current_whole_files_reread=True,
        complete_memory_literal_and_array_validation_still_required=True,
        predeclared_new_target=True,same_original_fixed_chart=False,
        same_mathematical_g_claimed=False,
        physical_values_roots_or_certificates_inherited=False)

def independent_chart_binding(report, envelope_binding):
    checked=envelope_binding['actual_metadata'].get('independent_fixed_target_validation')
    target=report.get('independent_fixed_target_definition')
    identity=report.get('independent_fixed_target_definition_identity_sha256')
    if checked is None:
        raise ValueError('This fixed Fejer entry requires its complete actual input binding')
    path=report['material_envelope']['historical_address_binding']['actual_path_binding']
    actual=bind_fixed_fejer_input(path['binding_file']['path'])
    if (actual!=report.get('actual_fixed_reference_input_binding')
            or actual['actual_binding_file']!=path['binding_file']
            or actual['complete_input_validation']!=checked):
        raise ValueError('The whole binding before the first field and in the complete report must be identical')
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
            or target.get('declared_new_target') is not True
            or target.get('same_previous_mathematical_g_claimed') is not False
            or target.get('mathematical_target_identity_sha256')!=actual['mathematical_target_identity_sha256']
            or reference.get('mathematical_target_recipe')!=target.get('mathematical_target_recipe')):
        raise ValueError('The verified complete recipe, generated words and actual report representation must be identical')
    return dict(definition_identity_sha256=identity,
        mathematical_target_identity_sha256=actual['mathematical_target_identity_sha256'],
        actual_reference_model_identity_sha256=canonical(reference),
        actual_reference_bundle_sha256=report['bundle_sha256'],
        actual_fixed_chart_core_sha256=reference['fixed_chart_core_sha256'],
        complete_target_and_actual_report_reference_equal=True,
        actual_full_chart_words_verified=True,same_original_fixed_chart=False,
        actual_fixed_recipe_input_binding=actual,predeclared_new_target=True,
        same_mathematical_g_claimed=False,old_values_or_certificates_inherited=False)
