#!/usr/bin/env python3
"""Pure complete source/model/report binding for the analytic local-J3 family.

Only immutable source text and already returned JSON metadata are consumed.
There is no NumPy/Torch import, numeric matrix construction, F/J/root call,
quadrature, or inference of root/geometry success.
"""
import ast
import copy
import hashlib
import json
import math
from pathlib import Path

SCHEMA = 'complete-analytic-J3-source-model-and-report-binding-v1'
OPERATOR_SCHEMA = 'complete-R711-reference-centred-analytic-J3-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1'
ROOT_SNAPSHOT_SCHEMA = 'actual-reference-centred-analytic-J3-normal-current-point-snapshot-v1'
LEGACY_OPERATOR_SCHEMA = 'complete-R711-reference-centred-C1-reuse-SO3-fixed-normal-plane-six-control-layer-v1'
LEGACY_OPERATOR_SHA256 = 'a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd'
LEGACY_CALIBRATION_SHA256 = '3e478bbeacbe236947070f9422ab6c75852f460f41536c68ebb3995ff0a2a991'
LEGACY_C1_SHA256 = 'ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9'
BASE_SOURCE_SHA256 = '6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865'
SOURCE_BINDINGS = {
    "analytic_J3": ("analytic_normal_stage_jacobian.py", "64b39a8be75ee976dbf4b49768e4ebaf37a372f77dba397a439a054cc4e7465d"),
    "frame_C1": ("analytic_j3_normal_frame_c1_reuse.py", "8e6c3f255a6acbd27aa1291c1a8b0555eeaaeb869a58fde6a49b3fc5d16361f8"),
    "stage_matrices": ("analytic_j3_detached_normal_stage_matrix_reuse.py", "5db725b423db4e97229a697ff6ce712b9183236070000e8ed66ed45cbe1767c1"),
    "adjacent_matrices": ("analytic_j3_adjacent_normal_frame_matrices.py", "8a63cc1817fd0853c2b7ee69b64e3083de22106c239b62acc602ad9b69698787"),
    "reference_calibration": ("reference_centred_analytic_j3_smooth_triangle_calibration.py", "4c3fb7a6d19a9c214e2dc69428456b62bc406c8329bc60083e1f5f8be3ff3d6d"),
    "endpoint": ("so3_reference_centred_analytic_j3_smooth_triangle_normal_lift_operator.py", "04f1d2724e1d93f138d03c558262f53e1dd5433791c081c7f93c37eeab84e21e"),
}
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


def compatible_legacy_model(old,new,current_pins,*,source_directory):
    """Strict cc0a/104e or 95559/f382 relation, after the whole original reader."""
    roles={role:record[1] for role,record in current_pins.items()}
    validate_current_model(new,roles=roles,source_directory=source_directory)
    adjacent_source='d5da5e3db88a03cc0afdc00e3a6bc74e425aa3f1b730ea7f66ac278f93d8e6eb'
    adjacent_schema='complete-R711-reference-centred-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1'
    adjacent_calibration='ccb3340e500a032943aaed084376136fd67ad81b222e1afbcc5e79d468f21ef8'
    stage_source='375059dc973633a1639ceddd3105fc34fe8b37eec4c9e61a55ce3959a0b9fc59'
    adjacent_helper='955dafdc865e34695489f4e8832ecb8a6d48e056f801ba119fd92e9097ad69b3'
    original=old.get('source_sha256')
    if original==LEGACY_OPERATOR_SHA256:
        old_schema,old_calibration=LEGACY_OPERATOR_SCHEMA,LEGACY_CALIBRATION_SHA256
        old_keys=['normal_frame_C1_reuse']
    elif original==adjacent_source:
        old_schema,old_calibration=adjacent_schema,adjacent_calibration
        old_keys=['normal_frame_C1_reuse','detached_stage_matrix_reuse','adjacent_normal_frame_matrices']
    else:
        raise ValueError('This explicit transfer supports only its two whole declared parent families')
    if (old.get('schema')!=old_schema
            or old.get('reference_centering_definition',{}).get('source_sha256')!=old_calibration
            or old.get('reference_centering_definition',{}).get('endpoint_source_sha256')!=original
            or roles.get('analytic_parent_frame_C1')!=LEGACY_C1_SHA256):
        raise ValueError('Bind the complete actual parent normal, calibration and original frame source')
    original_policies={
        'normal_frame_C1_reuse':('normal_frame_c1_reuse.py',LEGACY_C1_SHA256,
            {'SCHEMA','ORIGINAL_CENTERED_SOURCE','METHOD_AST'},'analytic_parent_frame_C1')}
    if original==adjacent_source:
        original_policies.update({
            'detached_stage_matrix_reuse':('detached_normal_stage_matrix_reuse.py',stage_source,
                {'SCHEMA','FRAME_C1_SOURCE_SHA256','ORIGINAL_C1_OPERATOR_SOURCE_SHA256',
                 'BASE_SOURCE_SHA256','PHASES'},'analytic_parent_stage_matrices'),
            'adjacent_normal_frame_matrices':('adjacent_normal_frame_matrices.py',adjacent_helper,
                {'SCHEMA','FRAME_C1_SOURCE_SHA256','STAGE_MATRIX_SOURCE_SHA256',
                 'PARENT_OPERATOR_SOURCE_SHA256','BASE_SOURCE_SHA256'},'analytic_parent_adjacent_matrices')})
    for key,(name,digest,constants,role) in original_policies.items():
        if roles.get(role)!=digest:
            raise ValueError('The whole original parent working policy is absent: '+role)
        namespace=_pure(Path(source_directory)/name,digest,constants,{'sha','definition'})
        if old.get(key)!=namespace['definition']():
            raise ValueError('Do not relabel the actual complete parent working policy: '+key)
    before,after=copy.deepcopy(old),copy.deepcopy(new)
    for key in old_keys:
        before.pop(key)
    for key in POLICY_KEYS.values():
        after.pop(key)
    for value in (before,after):
        for key in ('schema','source_sha256'):
            value.pop(key)
        for key in ('source_sha256','endpoint_source_sha256'):
            value['reference_centering_definition'].pop(key)
    if before!=after:
        raise ValueError('The complete actual base/target/chart/seed/free space/partition or other field definition changed')
    return dict(complete_unchanged_definition_sha256=canonical(before),
        exact_old_complete_model_identity_sha256=canonical(old),
        exact_new_complete_model_identity_sha256=canonical(new),
        full_base_reference_chart_profile_and_partition_equal=True,
        only_explicit_source_schema_and_matrix_working_policy_fields_changed=True,
        computed_float_field_equality_claimed=False)

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
        snapshot_values_backfilled_from_latest=False,
        original_full_stage_residual_domain_Armijo_and_all_upstream_J_retained=True,
        local_J3_is_not_an_endpoint_root_or_geometry_certificate=True,
        every_matrix_request_is_a_complete_three_by_three_batch=True,
        source_or_binding_failures_silently_fallback=False,
        current_scientific_values_recomputed=False)
