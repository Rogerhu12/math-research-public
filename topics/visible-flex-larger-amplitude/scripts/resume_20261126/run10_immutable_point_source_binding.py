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

SCHEMA = "complete-run10-immutable-point-closure-value-source-model-and-report-binding-v1"
OPERATOR_SCHEMA = "complete-R711-reference-centred-immutable-point-closure-values-analytic-frame-J3-normal-layer-v1"
ROOT_SNAPSHOT_SCHEMA = "actual-reference-centred-immutable-point-closure-value-current-point-snapshot-v1"
LEGACY_OPERATOR_SCHEMA = 'complete-R711-reference-centred-C1-reuse-SO3-fixed-normal-plane-six-control-layer-v1'
LEGACY_OPERATOR_SHA256 = 'a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd'
LEGACY_CALIBRATION_SHA256 = '3e478bbeacbe236947070f9422ab6c75852f460f41536c68ebb3995ff0a2a991'
LEGACY_C1_SHA256 = 'ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9'
BASE_SOURCE_SHA256 = '6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865'
SOURCE_BINDINGS = {"analytic_J3": ["analytic_local_stage_jacobian_immutable_point.py", "21a929c14abfe5e66ca56c232d31b77d8f8e3a5e969d796c4601d1a1e1374024"], "frame_C1": ["normal_frame_c1_immutable_point.py", "53b5bc456cb3f62c6a25d329de54920253d9193168ef3fb761198ff61fa0822d"], "stage_matrices": ["detached_stage_matrices_immutable_point.py", "a41872f7563683b28d34cb9da35d7fc3bd0879fb5a8d1d183230a518f6b8f052"], "adjacent_matrices": ["adjacent_normal_matrices_immutable_point.py", "ab944e9c9af4b84a65d201a6cc997669a8f274077fc7e1f69ee35b268380bb59"], "reference_calibration": ["reference_centred_immutable_point_calibration.py", "794275121ee8d2f79972c5302012a10ba1fd8aa58fa5f67f05399825244fd238"], "endpoint": ["so3_reference_centred_immutable_point_normal_lift_operator.py", "9bd394592f95668956c6718387b02d22d47c445b3f981f9101ae0e2c482594d6"], "analytic_frame": ["analytic_normal_frame_jets_immutable_point.py", "4e9b027b365752878069fa29671f8f549fa4cd9be478487b12ceeb64a908f8fa"], "closure_values": ["immutable_point_detached_closure_values.py", "2543ee5db3ff15108fbdb4e340dad84301b94eecb773f757da4126ab86778cfb"]}
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


IMMUTABLE_POINT_PARENT_DRIVER = ('fullclosed_run10_detached_closure_so3_qp.py',
    'c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1')
IMMUTABLE_POINT_PARENT_BINDING = ('run10_detached_closure_value_binding.py',
    'dc3b40645eb47f924392a703eb65e3fda982f43804b1861f89da1c038e9140a1')
IMMUTABLE_POINT_PARENT_NORMAL = '6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4'


def _compatible_immutable_point_parent(old,new,current_pins,*,source_directory):
    """The complete actual run10 parent; all physical/input fields stay exact."""
    directory=Path(source_directory).resolve()
    topic=directory.parents[1]
    driver_path=directory/IMMUTABLE_POINT_PARENT_DRIVER[0]
    binding_path=directory/IMMUTABLE_POINT_PARENT_BINDING[0]
    if (current_pins.get('immutable_point_parent_driver',(None,None))[1]!=IMMUTABLE_POINT_PARENT_DRIVER[1]
            or current_pins.get('immutable_point_parent_binding',(None,None))[1]!=IMMUTABLE_POINT_PARENT_BINDING[1]
            or sha(driver_path)!=IMMUTABLE_POINT_PARENT_DRIVER[1]
            or sha(binding_path)!=IMMUTABLE_POINT_PARENT_BINDING[1]):
        raise ValueError('Bind the entire actual original run10 driver and pure model reader')
    records=[n for n in ast.parse(driver_path.read_bytes()).body
        if isinstance(n,ast.Assign) and len(n.targets)==1
        and isinstance(n.targets[0],ast.Name) and n.targets[0].id=='SOURCE_PINS']
    if len(records)!=1:
        raise ValueError('The complete actual parent has one literal full source role table')
    old_pins=ast.literal_eval(records[0].value)
    if not isinstance(old_pins,dict) or len(old_pins)!=75:
        raise ValueError('Retain all 75 complete source roles of the original run10 parent')
    for role,pair in old_pins.items():
        if (not isinstance(pair,(list,tuple)) or len(pair)!=2
                or tuple(pair) not in {tuple(v) for v in current_pins.values()}
                or sha(topic/pair[0])!=pair[1]):
            raise ValueError('A full source of the actual parent is absent or changed: '+role)
    module_name='_complete_immutable_point_parent_binding_'+IMMUTABLE_POINT_PARENT_BINDING[1]
    if module_name not in sys.modules:
        spec=importlib.util.spec_from_file_location(module_name,binding_path)
        module=importlib.util.module_from_spec(spec)
        sys.modules[module_name]=module
        spec.loader.exec_module(module)
    module=sys.modules[module_name]
    if sha(module.validate_current_model.__code__.co_filename)!=IMMUTABLE_POINT_PARENT_BINDING[1]:
        raise ValueError('Use the original complete run10 model validator')
    old_policies=module.validate_current_model(old,
        roles={role:pair[1] for role,pair in old_pins.items()},source_directory=directory)
    before,after=copy.deepcopy(old),copy.deepcopy(new)
    for role,key in POLICY_KEYS.items():
        if old.get(key)!=old_policies.get(key):
            raise ValueError('The actual complete parent working policy differs: '+key)
        before.pop(key);after.pop(key)
    for value in (before,after):
        value.pop('schema');value.pop('source_sha256')
        for key in ('source_sha256','endpoint_source_sha256'):
            value['reference_centering_definition'].pop(key)
    if before!=after:
        raise ValueError('A physical target/reference/seed/Q/space/partition changed during point-storage transfer')
    if sha(driver_path)!=IMMUTABLE_POINT_PARENT_DRIVER[1] or sha(binding_path)!=IMMUTABLE_POINT_PARENT_BINDING[1]:
        raise ValueError('The actual parent sources changed during complete model validation')
    return dict(complete_unchanged_definition_sha256=canonical(before),
        exact_old_complete_model_identity_sha256=canonical(old),
        exact_new_complete_model_identity_sha256=canonical(new),
        full_base_reference_chart_profile_and_partition_equal=True,
        only_explicit_source_schema_and_frame_matrix_working_policy_fields_changed=True,
        complete_detached_closure_value_policy_change_explicit=True,
        same_exact_equations_variables_target_and_partition_retained=True,
        complete_original_run10_source_roles=75,
        immutable_point_owner_replaces_only_per_key_complete_point_word_copy=True,
        all_original_stage_final_and_endpoint_rereads_retained=True,
        computed_float_field_equality_claimed=False)


def compatible_legacy_model(old,new,current_pins,*,source_directory):
    """Four explicit actual parent sources, each consumed by its entire original reader."""
    roles={role:record[1] for role,record in current_pins.items()}
    validate_current_model(new,roles=roles,source_directory=source_directory)
    if old.get('source_sha256')==IMMUTABLE_POINT_PARENT_NORMAL:
        return _compatible_immutable_point_parent(old,new,current_pins,source_directory=source_directory)
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
    elif original=='04f1d2724e1d93f138d03c558262f53e1dd5433791c081c7f93c37eeab84e21e':
        old_schema,old_calibration='complete-R711-reference-centred-analytic-J3-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1','4c3fb7a6d19a9c214e2dc69428456b62bc406c8329bc60083e1f5f8be3ff3d6d'
        old_keys=['normal_frame_C1_reuse','detached_stage_matrix_reuse',
            'adjacent_normal_frame_matrices','analytic_stage_jacobian']
    elif original=='3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc':
        old_schema='complete-R711-reference-centred-analytic-frame-and-J3-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1'
        old_calibration='fe422dbf2eac68bbc4f54e8fe290ba0e5d1b7a080f12f1d148cffe834957dba0'
        old_keys=['normal_frame_C1_reuse','detached_stage_matrix_reuse',
            'adjacent_normal_frame_matrices','analytic_stage_jacobian','analytic_normal_frame']
    else:
        raise ValueError('Use one of the four complete explicitly declared parent families')
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
    if original=='04f1d2724e1d93f138d03c558262f53e1dd5433791c081c7f93c37eeab84e21e':
        original_policies={'normal_frame_C1_reuse': ('analytic_j3_normal_frame_c1_reuse.py','8e6c3f255a6acbd27aa1291c1a8b0555eeaaeb869a58fde6a49b3fc5d16361f8',{'ANALYTIC_STAGE_SOURCE_SHA256', 'METHOD_AST', 'ORIGINAL_CENTERED_SOURCE', 'SCHEMA'},'frame_parent_C1'),
            'detached_stage_matrix_reuse': ('analytic_j3_detached_normal_stage_matrix_reuse.py','5db725b423db4e97229a697ff6ce712b9183236070000e8ed66ed45cbe1767c1',{'ANALYTIC_STAGE_SOURCE_SHA256', 'BASE_SOURCE_SHA256', 'FRAME_C1_SOURCE_SHA256', 'ORIGINAL_C1_OPERATOR_SOURCE_SHA256', 'PHASES', 'SCHEMA'},'frame_parent_stage_matrices'),
            'adjacent_normal_frame_matrices': ('analytic_j3_adjacent_normal_frame_matrices.py','8a63cc1817fd0853c2b7ee69b64e3083de22106c239b62acc602ad9b69698787',{'ANALYTIC_STAGE_SOURCE_SHA256', 'BASE_SOURCE_SHA256', 'FRAME_C1_SOURCE_SHA256', 'PARENT_OPERATOR_SOURCE_SHA256', 'SCHEMA', 'STAGE_MATRIX_SOURCE_SHA256'},'frame_parent_adjacent_matrices'),
            'analytic_stage_jacobian': ('analytic_normal_stage_jacobian.py','64b39a8be75ee976dbf4b49768e4ebaf37a372f77dba397a439a054cc4e7465d',{'BASE_SOURCE_SHA256', 'COUNTER_KEYS', 'ENDPOINT_SCHEMA', 'METHOD_AST', 'OBSERVED_COUNTER_KEYS', 'PARENT_NORMAL_SOURCE_SHA256', 'SCHEMA'},'frame_parent_J3')}
    if original=='3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc':
        original_policies={
            'normal_frame_C1_reuse':("analytic_frame_c1_reuse.py","f1c74928089b60fb8f5350084ace0805fa956f4b06ac0de3f6a11357dd1aa2fb",
                {"ANALYTIC_STAGE_SOURCE_SHA256", "METHOD_AST", "ORIGINAL_CENTERED_SOURCE", "SCHEMA"},'closure_parent_frame_C1'),
            'detached_stage_matrix_reuse':("analytic_frame_detached_normal_stage_matrix_reuse.py","fa06705ebe19153edf455151a19c4217e42b8ab81ae3ffa4c1815701ec135255",
                {"ANALYTIC_STAGE_SOURCE_SHA256", "BASE_SOURCE_SHA256", "FRAME_C1_SOURCE_SHA256", "ORIGINAL_C1_OPERATOR_SOURCE_SHA256", "PHASES", "SCHEMA"},'closure_parent_stage_matrices'),
            'adjacent_normal_frame_matrices':("analytic_frame_adjacent_normal_matrices.py","3788b809c986668042e1c02f927afb85bf45434c4ff69607f9aaa2e2bf142695",
                {"ANALYTIC_STAGE_SOURCE_SHA256", "BASE_SOURCE_SHA256", "FRAME_C1_SOURCE_SHA256", "PARENT_OPERATOR_SOURCE_SHA256", "SCHEMA", "STAGE_MATRIX_SOURCE_SHA256"},'closure_parent_adjacent_matrices'),
            'analytic_stage_jacobian':("analytic_frame_local_stage_jacobian.py","894efd3b277b8a8c1fbd4abcd68b573fb09ee10a706a90ded7b2e1894fe3b866",
                {"BASE_SOURCE_SHA256", "COUNTER_KEYS", "ENDPOINT_SCHEMA", "METHOD_AST", "OBSERVED_COUNTER_KEYS", "PARENT_NORMAL_SOURCE_SHA256", "SCHEMA"},'closure_parent_analytic_J3'),
            'analytic_normal_frame':("analytic_normal_frame_jets.py","4ed6dfb93bb15b864d79c227b852421bc69b888a32923b98a21fe816da5be3d8",
                {"BASE_SOURCE_SHA256", "COUNTER_KEYS", "ENDPOINT_SCHEMA", "METHOD_AST", "OBSERVED_COUNTER_KEYS", "ORIGINAL_FRAME_AST_SHA256", "PARENT_NORMAL_SOURCE_SHA256", "SCHEMA"},'closure_parent_analytic_frame')}
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
        only_explicit_source_schema_and_frame_matrix_working_policy_fields_changed=True,
        complete_detached_closure_value_policy_change_explicit=True,
        same_exact_equations_variables_target_and_partition_retained=True,
        computed_float_field_equality_claimed=False)

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
