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

SCHEMA = "complete-fixed-fejer-angular-refined-source-model-report-binding-v1"
OPERATOR_SCHEMA = "complete-fixed-fejer-angular-refined-immutable-point-closure-values-normal-layer-v1"
ROOT_SNAPSHOT_SCHEMA = "actual-fixed-fejer-angular-refined-current-point-snapshot-v1"
LEGACY_OPERATOR_SCHEMA = 'complete-R711-reference-centred-C1-reuse-SO3-fixed-normal-plane-six-control-layer-v1'
LEGACY_OPERATOR_SHA256 = 'a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd'
LEGACY_CALIBRATION_SHA256 = '3e478bbeacbe236947070f9422ab6c75852f460f41536c68ebb3995ff0a2a991'
LEGACY_C1_SHA256 = 'ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9'
BASE_SOURCE_SHA256 = '3f4d5c0ec5b03eba9e93660e1341c32f1bd4872e0d1250d489894dd4ba6ed915'
SOURCE_BINDINGS = {"analytic_J3":["fixed_fejer_angular_refined_stage_jacobian.py","272b129c52a3d3ee66a5320da41c5fce16f66c213722d3d9a4d9b708ac116552"],"frame_C1":["fixed_fejer_angular_refined_frame_c1.py","bbeda3ed59bf5f4af5577e43422af6e8058bd48b41767154c36ee0b8a1c58241"],"stage_matrices":["fixed_fejer_angular_refined_stage_matrices.py","3ae2c7fc2392881dff88f2fc5ba69b7b31ef3eb2102203076cef170e3df7014f"],"adjacent_matrices":["fixed_fejer_angular_refined_adjacent_matrices.py","6c8be90344961fc6fef3d8b73a10c49975b5cc6127de2aa47b05452f0f2142b1"],"reference_calibration":["fixed_fejer_angular_refined_calibration.py","9eadf599825400b85712591fc27758fb8a5ae21dc9b004cad3691cca45c93f64"],"endpoint":["fixed_fejer_angular_refined_normal_lift.py","2db038574bb13e226b61826949cc66d917f0186fe5b9156a50eb7180da3d4bda"],"analytic_frame":["fixed_fejer_angular_refined_normal_frame.py","6cff4f7d99a0b991b3f2737e374b5ec2aa0ca347a9d1cc12b374bd474741af18"],"closure_values":["fixed_fejer_angular_refined_closure_values.py","dc1072bfb384a91950f0ab0df5d04a58c5f6c3d9062e72aa4f6e879d79dc5e49"]}
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
    return _bound_module(Path(source_directory)/'fixed_fejer_angular_observation_refinement.py',
        '52b13e57f058001a5f1640809ae09995c793aadb2ab8eaa54e9c5ab9619d2b21')


def _validate_original_parent_model(old,directory):
    """Bind the actual whole N2048 fixed Fejer immutable-point family before normalization."""
    if (old.get('source_sha256')!='1aa64d7731333f8ae008f86b717421abbbbfdb7f4c3edb1173f93754364bd778'
            or old.get('schema')!='complete-fixed-fejer-reference-centred-immutable-point-closure-values-analytic-frame-J3-normal-layer-v1'):
        raise ValueError('The N-parent must be the complete actual Fejer immutable-point model')
    original=_bound_module(Path(directory)/'fixed_fejer_complete_source_binding.py',
        '3b3f2322eb1d1f6304e71e4d972a8e45ba2b5dd6605501d293212de46b5c5c88')
    roles={role:record[1] for role,record in original.SOURCE_BINDINGS.items()}
    original.validate_current_model(old,roles=roles,source_directory=directory)
    return tuple(original.POLICY_KEYS.values())


def compatible_legacy_model(old,new,current_pins,*,source_directory):
    """Normalize only the declared observer/source identities; compare all else."""
    roles={role:value[1] for role,value in current_pins.items()}
    validate_current_model(new,roles=roles,source_directory=source_directory)
    old_policy_keys=_validate_original_parent_model(old,source_directory)
    observer=_observer(source_directory)
    observation=observer.validate_base_model(new['base_complete_model'])
    if (roles.get('angular_observation')!=sha(observer.__file__)
            or new.get('new_reference_input_binding_source_sha256')
                !='242c31ee2981b9fe64eb0bd25fe5efc76382841e01b31d912b91f57ea0473a03'
            or new.get('literal_Q_input_schema')!='fixed-fejer-angular-refined-literal-Q-input-v1'):
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
        expected_schema=('fixed-fejer-supported-reference-literal-two-bubble-endpoint-Q-v1'
            if original is old else 'fixed-fejer-angular-refined-literal-two-bubble-Q-v1')
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
        only_explicit_observation_source_schema_and_frame_matrix_working_policy_fields_changed=True,
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
        angular_observation=angular_observation_binding(report,roles=roles,source_directory=source_directory),
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
