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
import textwrap
from pathlib import Path

SCHEMA = "complete-run10-N4096-detached-closure-source-model-binding-v1"
OPERATOR_SCHEMA = "complete-run10-angular-refined-detached-closure-values-normal-plane-SO3-v1"
ROOT_SNAPSHOT_SCHEMA = "actual-run10-angular-refined-closure-current-point-snapshot-v1"
LEGACY_OPERATOR_SCHEMA = 'complete-R711-reference-centred-C1-reuse-SO3-fixed-normal-plane-six-control-layer-v1'
LEGACY_OPERATOR_SHA256 = 'a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd'
LEGACY_CALIBRATION_SHA256 = '3e478bbeacbe236947070f9422ab6c75852f460f41536c68ebb3995ff0a2a991'
LEGACY_C1_SHA256 = 'ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9'
BASE_SOURCE_SHA256 = "1ba446d9283891cfbb8d3af319a27804b4889f4b7f5f2891dea0b101aa042529"
SOURCE_BINDINGS = {"closure_values":["run10_angular_refined_closure_values.py","c3ce1e6bdca28ab9b0e8977112e1bdd903d9684c3bd68ae18c3ec41b98c8c538"],"analytic_J3":["run10_angular_refined_stage_jacobian.py","cd8a39091f595be0df159310712008a8d764024169b0ead9a14c3abcf8013dde"],"analytic_frame":["run10_angular_refined_normal_frame.py","ab62ad2878bb26eb55e5365cec0bb9ae53db10bf494189a291da582251e3a642"],"frame_C1":["run10_angular_refined_frame_c1.py","12a62f4f90fe6bf5d2d0b3e8a9658e08219fdfbe37f046c7ecfef641f0ee874b"],"stage_matrices":["run10_angular_refined_stage_matrices.py","db4c677a3389c8768319b7d98c229c7781f7a5235d2a75ba93b04c37734fdd93"],"adjacent_matrices":["run10_angular_refined_adjacent_matrices.py","bcc71ec7e59fa8f0e57305937c26afb3a08a008a7c85b053548033a515232b51"],"reference_calibration":["run10_angular_refined_calibration.py","c0d140b33ec730f994662cc529022e3658a73e70325ee72c94f9d97bf53970a9"],"endpoint":["so3_run10_angular_refined_closure_normal_lift.py","e8a3d757046a408fa8d3322b7523d26944c4b8db8bc4a2f5acb4ca0f88ef6e16"]}
POLICY_KEYS = {"analytic_J3": "analytic_stage_jacobian", "frame_C1": "normal_frame_C1_reuse", "stage_matrices": "detached_stage_matrix_reuse", "adjacent_matrices": "adjacent_normal_frame_matrices", "analytic_frame": "analytic_normal_frame", "closure_values": "detached_closure_value_reuse"}
POLICY_CONSTANTS = {"analytic_J3": {"BASE_SOURCE_SHA256", "COUNTER_KEYS", "ENDPOINT_SCHEMA", "METHOD_AST", "OBSERVED_COUNTER_KEYS", "PARENT_NORMAL_SOURCE_SHA256", "SCHEMA", "METHOD_SOURCE_OVERRIDES", "CLOSURE_VALUE_SOURCE_SHA256"}, "frame_C1": {"ANALYTIC_STAGE_SOURCE_SHA256", "METHOD_AST", "ORIGINAL_CENTERED_SOURCE", "SCHEMA", "METHOD_SOURCE_OVERRIDES", "CLOSURE_VALUE_SOURCE_SHA256"}, "stage_matrices": {"ANALYTIC_STAGE_SOURCE_SHA256", "BASE_SOURCE_SHA256", "FRAME_C1_SOURCE_SHA256", "ORIGINAL_C1_OPERATOR_SOURCE_SHA256", "PHASES", "SCHEMA"}, "adjacent_matrices": {"ANALYTIC_STAGE_SOURCE_SHA256", "BASE_SOURCE_SHA256", "FRAME_C1_SOURCE_SHA256", "PARENT_OPERATOR_SOURCE_SHA256", "SCHEMA", "STAGE_MATRIX_SOURCE_SHA256"}, "analytic_frame": {"BASE_SOURCE_SHA256", "COUNTER_KEYS", "ENDPOINT_SCHEMA", "METHOD_AST", "OBSERVED_COUNTER_KEYS", "ORIGINAL_FRAME_AST_SHA256", "PARENT_NORMAL_SOURCE_SHA256", "SCHEMA", "METHOD_SOURCE_OVERRIDES", "CLOSURE_VALUE_SOURCE_SHA256"}, "closure_values": {"COUNTER_KEYS", "SCHEMA", "DEFINITION_SCHEMA", "ENDPOINT_SCHEMA", "NORMAL_PARENT_SHA256", "BASE_SOURCE_SHA256", "TORCH_VERSION"}}

ACTUAL_RUN10_BINDING_SHA256 = "4ace8184408aa0c7cac7970ba6fc96565c68786a518cd9d280a1a97ef82b50cf"
ACTUAL_RUN10_BINDING_BYTES = 430908
ACTUAL_RUN10_TARGET_IDENTITY = "e7110482f9bd2eb723e96c99f5bbaa8a85aa11a81519c5204a296fb1bad9a049"
ACTUAL_RUN10_MODEL_IDENTITY = "081bdf939b7bdc6d5dfb54bce955fdfbcda90a8cef3668388a8874272e594af5"
ACTUAL_RUN10_PUBLIC_INPUT_SOURCE = "9f69b860d4bf2e25e707d08c7c85ca01c17ebf468398ea007ad7448df9951209"
ACTUAL_RUN10_PRODUCER_SOURCE = "fcd20177bed258bc463f5ca6431c29c18c3b381b75146e1da7bbc8bc4e7a475a"
ACTUAL_RUN10_CHART_IDENTITY = '90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e'


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
    return _bound_module(Path(source_directory)/'angular_observation_refinement.py',
        '8506eb861bb8650ddfd0c5db5c268e8bb0a71b38e48ebb551767b45d2d339ab3')


def _validate_original_parent_model(old,directory):
    """Bind the actual whole N2048 run10 frame family before normalization."""
    if (old.get('source_sha256')!='6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4'
            or old.get('schema')!='complete-R711-reference-centred-detached-closure-values-analytic-frame-J3-normal-layer-v1'):
        raise ValueError('The N-parent must be the complete actual run10 analytic-frame model')
    original=_bound_module(Path(directory)/'run10_detached_closure_value_binding.py',
        'dc3b40645eb47f924392a703eb65e3fda982f43804b1861f89da1c038e9140a1')
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

def bind_actual_run10_input(path, *, current_files=None):
    """Read only the genuinely returned whole input binding and all six inputs.

    The old/current carrier reconstruction is never rerun here. The complete
    source-bound memory separately rechecks its public snapshots, full chart,
    original P0 and actual carrier arrays before the first physical field.
    """
    path=Path(path).resolve()
    raw=path.read_bytes()
    record=dict(path=str(path),sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw))
    if (record['sha256']!=ACTUAL_RUN10_BINDING_SHA256
            or record['bytes']!=ACTUAL_RUN10_BINDING_BYTES):
        raise ValueError('Use the whole actually returned run10 input binding, not a relabelled current file')
    payload=json.loads(raw)
    target=payload.get('fixed_target_definition',{})
    evidence=target.get('complete_public_input_evidence',{})
    if (payload.get('schema')!='material-envelope-actual-public-run10-fixed-target-binding-v1'
            or payload.get('producer',{}).get('source_sha256')!=ACTUAL_RUN10_PRODUCER_SOURCE
            or payload.get('fixed_target_definition_identity_sha256')!=ACTUAL_RUN10_TARGET_IDENTITY
            or canonical(target)!=ACTUAL_RUN10_TARGET_IDENTITY
            or target.get('schema')!='independently-frozen-actual-public-run10-scalar-and-material-chart-v1'
            or target.get('definition_source_sha256')!=ACTUAL_RUN10_PRODUCER_SOURCE
            or target.get('public_input_binding_source_sha256')!=ACTUAL_RUN10_PUBLIC_INPUT_SOURCE
            or target.get('current_reference_model_identity_sha256')!=ACTUAL_RUN10_MODEL_IDENTITY
            or canonical(target.get('complete_current_reference_model'))!=ACTUAL_RUN10_MODEL_IDENTITY
            or target.get('fixed_chart_core_array_record',{}).get('sha256')!=ACTUAL_RUN10_CHART_IDENTITY
            or target.get('same_original_fixed_chart') is not True
            or target.get('same_mathematical_g_claimed') is not False
            or evidence.get('actual_run_id')!='45972294636'
            or evidence.get('actual_run_attempt')!='1'
            or evidence.get('actual_reference_step_id')!='independent-axisymmetric-R690-reference-prepare-v2-first-20261127-10'
            or canonical(evidence)!=target.get('complete_public_input_evidence_identity_sha256')):
        raise ValueError('The complete returned run10 target/evidence/source identity changed')
    files=evidence.get('current_files')
    expected={'current_warm_bundle','current_node_report','current_scalar_input',
        'current_carrier','current_preparation_report','current_reference_bundle'}
    if not isinstance(files,dict) or set(files)!=expected:
        raise ValueError('Every one of the six actual run10 input records is required')
    supplied={} if current_files is None else current_files
    if not isinstance(supplied,dict) or not set(supplied)<=expected:
        raise ValueError('Only explicit original complete input roles can be matched')
    for role,declared in files.items():
        source=Path(declared['path']).resolve()
        data=source.read_bytes()
        actual=dict(path=str(source),sha256=hashlib.sha256(data).hexdigest(),bytes=len(data))
        if actual!=declared or (role in supplied and Path(supplied[role]).resolve()!=source):
            raise ValueError('The current entry input is not its whole actual run10 file: '+role)
    if path.read_bytes()!=raw:
        raise ValueError('The immutable actual input binding changed while being consumed')
    return dict(schema='actual-run10-returned-input-entry-binding-v1',
        source_sha256=sha(__file__),actual_binding_file=record,
        actual_input_producer_source_sha256=ACTUAL_RUN10_PRODUCER_SOURCE,
        actual_public_input_binding_source_sha256=ACTUAL_RUN10_PUBLIC_INPUT_SOURCE,
        actual_run_id='45972294636',actual_run_attempt='1',
        actual_reference_step_id=evidence['actual_reference_step_id'],
        actual_reference_model_identity_sha256=ACTUAL_RUN10_MODEL_IDENTITY,
        actual_fixed_target_definition_identity_sha256=ACTUAL_RUN10_TARGET_IDENTITY,
        actual_fixed_chart_core_sha256=ACTUAL_RUN10_CHART_IDENTITY,
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
        raise ValueError('This run10 entry always requires its complete actual public input binding')
    path=report['material_envelope']['historical_address_binding']['actual_path_binding']
    actual=bind_actual_run10_input(path['binding_file']['path'])
    if (actual!=report.get('actual_public_reference_input_binding')
            or actual['actual_binding_file']!=path['binding_file']
            or identity!=ACTUAL_RUN10_TARGET_IDENTITY):
        raise ValueError('Read the same complete run10 binding before the first field and in the actual report')
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
