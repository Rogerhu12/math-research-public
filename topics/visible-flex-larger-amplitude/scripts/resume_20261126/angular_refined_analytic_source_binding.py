#!/usr/bin/env python3
"""Pure complete source/model/report binding for the analytic local-J3 family.

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

SCHEMA = 'complete-angular-refined-analytic-J3-source-model-and-report-binding-v1'
OPERATOR_SCHEMA = 'complete-angular-refined-reference-centred-analytic-J3-fixed-normal-plane-SO3-v1'
ROOT_SNAPSHOT_SCHEMA = 'actual-angular-refined-analytic-J3-normal-current-point-snapshot-v1'
LEGACY_OPERATOR_SCHEMA = 'complete-R711-reference-centred-C1-reuse-SO3-fixed-normal-plane-six-control-layer-v1'
LEGACY_OPERATOR_SHA256 = 'a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd'
LEGACY_CALIBRATION_SHA256 = '3e478bbeacbe236947070f9422ab6c75852f460f41536c68ebb3995ff0a2a991'
LEGACY_C1_SHA256 = 'ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9'
BASE_SOURCE_SHA256 = '1ba446d9283891cfbb8d3af319a27804b4889f4b7f5f2891dea0b101aa042529'
SOURCE_BINDINGS = {'analytic_J3': ('angular_refined_analytic_normal_stage_jacobian.py', 'f497452ff23188bca80556773f7493418e3f60b94108af5e5c92956c82e544b7'), 'frame_C1': ('angular_refined_analytic_frame_c1.py', 'aeda86f6c10054f79758174d978356fc046881b5f3aba9aea91c4b2b50617f35'), 'stage_matrices': ('angular_refined_analytic_stage_matrices.py', '0ac33e262d4bb95f84f548b630c955e481430d2cf4b899ec7829bafea845ab3d'), 'adjacent_matrices': ('angular_refined_analytic_adjacent_matrices.py', '032c69fad6425c7b70d75d288884fff293eaa76b2e1fdfb822b87f2d2b9febfd'), 'reference_calibration': ('angular_refined_analytic_calibration.py', '186798d2d31924941f7917c32afb856d584ca13dfea8602798e5206e0489af93'), 'endpoint': ('so3_angular_refined_analytic_normal_lift.py', '361df1bcd7034616d3c0830a20444896dd3992a0d1295ec01ab690f94a61262b')}
POLICY_KEYS = {
    'analytic_J3':'analytic_stage_jacobian',
    'frame_C1':'normal_frame_C1_reuse',
    'stage_matrices':'detached_stage_matrix_reuse',
    'adjacent_matrices':'adjacent_normal_frame_matrices'}
POLICY_CONSTANTS = {
    'analytic_J3':{'SCHEMA','ENDPOINT_SCHEMA','BASE_SOURCE_SHA256',
        'PARENT_NORMAL_SOURCE_SHA256','METHOD_AST','COUNTER_KEYS','OBSERVED_COUNTER_KEYS'},
    'frame_C1':{'SCHEMA','ORIGINAL_CENTERED_SOURCE','METHOD_AST','ANALYTIC_STAGE_SOURCE_SHA256'},
    'stage_matrices':{'SCHEMA','FRAME_C1_SOURCE_SHA256','ORIGINAL_C1_OPERATOR_SOURCE_SHA256',
        'BASE_SOURCE_SHA256','PHASES','ANALYTIC_STAGE_SOURCE_SHA256'},
    'adjacent_matrices':{'SCHEMA','FRAME_C1_SOURCE_SHA256','STAGE_MATRIX_SOURCE_SHA256',
        'PARENT_OPERATOR_SOURCE_SHA256','BASE_SOURCE_SHA256','ANALYTIC_STAGE_SOURCE_SHA256'}}


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
        if role=='analytic_J3':
            functions|={'canonical','_copy','_digest','_counts','validate_metadata'}
        namespace=_pure(directory/name,digest,POLICY_CONSTANTS[role],functions)
        result[key]=namespace['definition']()
        if role=='analytic_J3':
            result['actual_validator']=namespace['validate_metadata']
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
    _observer(directory).validate_base_model(model['base_complete_model'])
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
    if sha(path)!=expected:
        raise ValueError('Keep the entire actual pure source '+path.name)
    name='_angular_analytic_binding_'+expected
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    if sha(path)!=expected:
        raise ValueError('The pure source changed while loading')
    return module

def _observer(source_directory):
    return _bound_module(Path(source_directory)/'angular_observation_refinement.py',
        '8506eb861bb8650ddfd0c5db5c268e8bb0a71b38e48ebb551767b45d2d339ab3')

def _validate_original_parent_model(model, source_directory):
    """Validate an entire original N2048 family before normalizing identities."""
    original_source='f34fcafc06b50594b7a651a90e38553ea8ae3da5b6ac8b6ca4ea691d2ab9f14f'
    original=_bound_module(Path(source_directory)/'analytic_j3_source_and_report_binding.py',original_source)
    analytic='04f1d2724e1d93f138d03c558262f53e1dd5433791c081c7f93c37eeab84e21e'
    adjacent='d5da5e3db88a03cc0afdc00e3a6bc74e425aa3f1b730ea7f66ac278f93d8e6eb'
    if model.get('source_sha256')==analytic:
        roles={name:value[1] for name,value in original.SOURCE_BINDINGS.items()}
        original.validate_current_model(model,roles=roles,source_directory=source_directory)
        keys=tuple(original.POLICY_KEYS.values())
    elif model.get('source_sha256')==adjacent:
        if (model.get('schema')!='complete-R711-reference-centred-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1'
                or model.get('reference_centering_definition',{}).get('source_sha256')
                    !='ccb3340e500a032943aaed084376136fd67ad81b222e1afbcc5e79d468f21ef8'
                or model['reference_centering_definition'].get('endpoint_source_sha256')!=adjacent):
            raise ValueError('Keep the entire actual N2048 adjacent parent calibration')
        policies={
            'normal_frame_C1_reuse':('normal_frame_c1_reuse.py',
                'ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9',
                {'SCHEMA','ORIGINAL_CENTERED_SOURCE','METHOD_AST'}),
            'detached_stage_matrix_reuse':('detached_normal_stage_matrix_reuse.py',
                '375059dc973633a1639ceddd3105fc34fe8b37eec4c9e61a55ce3959a0b9fc59',
                {'SCHEMA','FRAME_C1_SOURCE_SHA256','ORIGINAL_C1_OPERATOR_SOURCE_SHA256','BASE_SOURCE_SHA256','PHASES'}),
            'adjacent_normal_frame_matrices':('adjacent_normal_frame_matrices.py',
                '955dafdc865e34695489f4e8832ecb8a6d48e056f801ba119fd92e9097ad69b3',
                {'SCHEMA','FRAME_C1_SOURCE_SHA256','STAGE_MATRIX_SOURCE_SHA256','PARENT_OPERATOR_SOURCE_SHA256','BASE_SOURCE_SHA256'})}
        for key,(name,digest,constants) in policies.items():
            namespace=original._pure(Path(source_directory)/name,digest,constants,{'sha','definition'})
            if model.get(key)!=namespace['definition']():
                raise ValueError('The entire actual N2048 parent policy changed: '+key)
        keys=tuple(policies)
    else:
        raise ValueError('This N-only relation requires its complete N2048 analytic or adjacent parent')
    base=model.get('base_complete_model',{})
    if (model.get('base_source_sha256')!='6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865'
            or base.get('source_sha256')!=model['base_source_sha256']
            or base.get('schema')!='complete-supported-smooth-triangle-reference-so3-meridian-with-core-lift-v1'
            or canonical(base)!=model.get('base_model_identity_sha256')
            or model.get('base_schema')!=base['schema']
            or model.get('new_reference_input_binding_source_sha256')
                !='307ebae301db059f30ff1cc5fda024b09e9c2730c9f6bffbd82f0821d2a727a7'
            or model.get('literal_Q_input_schema')!='supported-smooth-triangle-reference-literal-zero-endpoint-Q-input-v1'):
        raise ValueError('Keep the actual complete original supported base and Q input')
    return keys

def compatible_legacy_model(old,new,current_pins,*,source_directory):
    """Normalize only the declared observer/source identities; compare all else."""
    roles={role:value[1] for role,value in current_pins.items()}
    validate_current_model(new,roles=roles,source_directory=source_directory)
    old_policy_keys=_validate_original_parent_model(old,source_directory)
    observer=_observer(source_directory)
    observation=observer.validate_base_model(new['base_complete_model'])
    if (roles.get('angular_observation')!=sha(observer.__file__)
            or new.get('new_reference_input_binding_source_sha256')
                !='a4a53ff3ff92bb4fdbf8db2da048c717437d945423932e2b3d69cfc1cc06035d'
            or new.get('literal_Q_input_schema')!='angular-refined-supported-smooth-triangle-literal-Q-input-v1'):
        raise ValueError('Bind the exact complete current observer and dependent Q identity source')
    before,after=copy.deepcopy(old),copy.deepcopy(new)
    old_base,new_base=before['base_complete_model'],after['base_complete_model']
    for key in ('angular_observation_refinement','reference_full_N','current_full_N'):
        new_base.pop(key)
    for base in (old_base,new_base):
        base.pop('schema');base.pop('source_sha256')
    if old_base!=new_base:
        raise ValueError('The fixed full scalar/reference/chart/seed/radial mesh or free layout changed')
    base_identity=canonical(old_base)
    for key in old_policy_keys:
        before.pop(key)
    for key in POLICY_KEYS.values():
        after.pop(key)
    for original,value in ((old,before),(new,after)):
        own_base=original['base_model_identity_sha256']
        value['base_model_identity_sha256']=base_identity
        value['base_complete_model']=copy.deepcopy(old_base)
        for key in ('schema','source_sha256','base_source_sha256','base_schema',
                'literal_Q_input_schema','new_reference_input_binding_source_sha256'):
            value.pop(key)
        calibration=value['reference_centering_definition']
        if calibration.get('base_model_identity_sha256')!=own_base:
            raise ValueError('Each complete calibration must bind its own full base')
        calibration['base_model_identity_sha256']=base_identity
        calibration.pop('source_sha256');calibration.pop('endpoint_source_sha256')
        Q=value['frozen_moment_Q_definition']
        expected_schema=('supported-smooth-triangle-reference-literal-two-bubble-endpoint-Q-v1'
            if original is old else 'angular-refined-supported-smooth-triangle-literal-two-bubble-Q-v1')
        if (Q.get('base_model_identity_sha256')!=own_base or Q.get('schema')!=expected_schema
                or canonical(Q)!=original['frozen_moment_Q_definition_identity_sha256']):
            raise ValueError('Each actual complete Q definition must bind its own base/source schema')
        Q['base_model_identity_sha256']=base_identity
        Q.pop('schema')
        value['frozen_moment_Q_definition_identity_sha256']=canonical(Q)
    if before!=after:
        raise ValueError('Only observer/source/dependent identities may change; keep every target/seed/Q/gamma/tau/free parameter')
    return dict(complete_unchanged_definition_sha256=canonical(before),
        exact_old_complete_model_identity_sha256=canonical(old),
        exact_new_complete_model_identity_sha256=canonical(new),
        full_fixed_reference_chart_profile_seed_mesh_Q_gamma_partition_and_free_layout_equal=True,
        only_explicit_observation_source_schema_and_matrix_working_policy_fields_changed=True,
        reference_full_N=2048,old_current_full_N=2048,new_current_full_N=4096,
        original_angle_words_at_all_even_indices=True,
        angular_observation_definition_identity_sha256=observation['definition_identity_sha256'],
        computed_float_field_equality_claimed=False,old_finite_objective_inherited=False)

def angular_observation_binding(report,*,roles,source_directory):
    observer=_observer(source_directory)
    model=report['representation']
    if roles.get('angular_observation')!=sha(observer.__file__):
        raise ValueError('Bind the actual entire observer source')
    checked=observer.validate_report(report.get('angular_observation_refinement'),model)
    if (report.get('N')!=4096 or report.get('reference_full_N')!=2048
            or report.get('current_full_N')!=4096 or report.get('reference_quarter_angle_count')!=513
            or report.get('current_quarter_angle_count')!=1025
            or report.get('radial_observation_refinement_performed') is not False
            or report.get('full_fixed_reference_target_unchanged') is not True
            or report.get('saved_parent_Phi_used_as_current_baseline') is not False):
        raise ValueError('State the actual N-only scope and new finite-objective responsibility')
    attribution=[]
    def visit(value):
        if isinstance(value,dict):
            if value.get('schema')=='same-current-buffer-dyadic-observation-attribution-v1':
                attribution.append(observer.validate_attribution(value))
            for child in value.values():visit(child)
        elif isinstance(value,list):
            for child in value:visit(child)
    visit(report.get('initial'))
    visit(report.get('final_statistics'))
    visit(report.get('metric_directions',[]))
    visit(report.get('restoration_directions',[]))
    return dict(**checked,actual_same_buffer_attribution_count=len(attribution),
        actual_same_buffer_attributions=attribution,
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
                count+=1
            elif value.get('schema')==OPERATOR_SCHEMA and 'model' in value:
                if value['model']!=model or value.get('model_identity_sha256')!=canonical(model):
                    raise ValueError('A full matrix metadata record belongs to another actual field')
                validator(value.get('analytic_stage_jacobian'),model=model,source_by_role=roles,
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
    if latest:
        if latest.get('schema')!=OPERATOR_SCHEMA or latest.get('model')!=model:
            raise ValueError('Do not substitute another latest operator record')
        actual=validator(latest.get('analytic_stage_jacobian'),model=model,source_by_role=roles,
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
        angular_observation=angular_observation_binding(report,roles=roles,source_directory=source_directory),
        snapshot_values_backfilled_from_latest=False,
        original_full_stage_residual_domain_Armijo_and_all_upstream_J_retained=True,
        local_J3_is_not_an_endpoint_root_or_geometry_certificate=True,
        every_matrix_request_is_a_complete_three_by_three_batch=True,
        source_or_binding_failures_silently_fallback=False,
        current_scientific_values_recomputed=False)


def independent_chart_binding(report, envelope_binding):
    checked=envelope_binding['actual_metadata'].get('independent_fixed_target_validation')
    target=report.get('independent_fixed_target_definition')
    identity=report.get('independent_fixed_target_definition_identity_sha256')
    if checked is None:
        if target is not None or identity is not None or report.get('independent_fixed_target_validation') is not None:
            raise ValueError('The original strict transfer cannot claim an unbound independent chart')
        return None
    path=report['material_envelope']['historical_address_binding']['actual_path_binding']
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
            or target.get('same_original_fixed_chart') is not False
            or target.get('same_mathematical_g_claimed') is not False):
        raise ValueError('The verified full target, all chart words and actual report reference must be identical')
    return dict(definition_identity_sha256=identity,
        actual_reference_model_identity_sha256=canonical(reference),
        actual_reference_bundle_sha256=report['bundle_sha256'],
        actual_fixed_chart_core_sha256=reference['fixed_chart_core_sha256'],
        complete_target_and_actual_report_reference_equal=True,
        actual_full_chart_words_verified=True,same_original_fixed_chart=False,
        same_mathematical_g_claimed=False,old_values_or_certificates_inherited=False)
