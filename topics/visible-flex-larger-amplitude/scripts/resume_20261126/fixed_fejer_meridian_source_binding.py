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

SCHEMA = "complete-fixed-fejer-meridian-values-source-model-and-report-binding-v1"
OPERATOR_SCHEMA = "complete-fixed-fejer-detached-meridian-values-normal-layer-v1"
ROOT_SNAPSHOT_SCHEMA = "actual-fixed-fejer-immutable-point-current-point-snapshot-v1"
LEGACY_OPERATOR_SCHEMA = 'complete-R711-reference-centred-C1-reuse-SO3-fixed-normal-plane-six-control-layer-v1'
LEGACY_OPERATOR_SHA256 = 'a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd'
LEGACY_CALIBRATION_SHA256 = '3e478bbeacbe236947070f9422ab6c75852f460f41536c68ebb3995ff0a2a991'
LEGACY_C1_SHA256 = 'ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9'
BASE_SOURCE_SHA256 = '552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3'
SOURCE_BINDINGS = {"analytic_J3":["fixed_fejer_meridian_analytic_stage_jacobian.py","223afb992e0e9904c30ab20387a92569dc2979dbfde84f75f04e3402b9c5e811"],"frame_C1":["fixed_fejer_meridian_normal_frame_c1.py","c97749c8fae14981a1f86e45845d152134a62039d88b7cfaccfb69fb0665e246"],"stage_matrices":["fixed_fejer_meridian_stage_matrices.py","f98bf270265f9d41c9c297dd23c2db7da9ea91a039663c1785966e9135795791"],"adjacent_matrices":["fixed_fejer_meridian_adjacent_matrices.py","bd65734da69f3e5bc560ec81df03f8555593257560455b56adfa353e025c4564"],"reference_calibration":["fixed_fejer_meridian_reference_calibration.py","aa40b224da667b5e01b207a431f771e2bf11177fabaebb075ca6218bbb130de3"],"endpoint":["fixed_fejer_detached_meridian_normal_lift.py","33c269f3cd04c9435ccb5144984124c8a0b6ae348f95c8bd71ac92a334c51cf4"],"analytic_frame":["fixed_fejer_meridian_analytic_normal_frame.py","d3cf01067c0c3cd348560a74d1845b02f859bbd0a41f2938ec544034d2a63bcd"],"closure_values":["fixed_fejer_meridian_closure_values.py","2889fef0d09a32c3f609f9a4e100efb1b136070dad77c8104204b552a867c4e0"],"detached_meridian_values":["fixed_fejer_detached_meridian_values.py","7aa760baa30a46484d90bc5e327849ab5229cca708e6ba4289b12da253a5facd"]}
POLICY_KEYS = {"analytic_J3":"analytic_stage_jacobian","frame_C1":"normal_frame_C1_reuse","stage_matrices":"detached_stage_matrix_reuse","adjacent_matrices":"adjacent_normal_frame_matrices","analytic_frame":"analytic_normal_frame","closure_values":"detached_closure_value_reuse","detached_meridian_values":"detached_meridian_value_reuse"}
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
        if role=='detached_meridian_values':
            path=directory/name
            if sha(path)!=digest:
                raise ValueError('Bind the whole actual detached meridian value helper')
            module_key='_complete_meridian_values_policy_'+digest
            module=sys.modules.get(module_key)
            if module is None:
                spec=importlib.util.spec_from_file_location(module_key,path)
                module=importlib.util.module_from_spec(spec);sys.modules[module_key]=module
                spec.loader.exec_module(module)
            for method in ('definition','validate_metadata'):
                if sha(getattr(module,method).__code__.co_filename)!=digest:
                    raise ValueError('Keep the original complete pure meridian policy methods')
            result[key]=module.definition()
            result['meridian_actual_validator']=module.validate_metadata
            if sha(path)!=digest:
                raise ValueError('The full meridian policy source changed during pure attribution')
            continue
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
        if role=='detached_meridian_values':
            if key in before:
                raise ValueError('Do not invent a meridian cache policy in the actual original parent')
            after.pop(key)
            continue
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


STAGE_POINT_PARENT_DRIVER = ('fullclosed_fixed_fejer_immutable_point_so3_qp.py',
    '477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd')
STAGE_POINT_PARENT_BINDING = ('fixed_fejer_complete_source_binding.py',
    '3b3f2322eb1d1f6304e71e4d972a8e45ba2b5dd6605501d293212de46b5c5c88')
STAGE_POINT_PARENT_NORMAL = '1aa64d7731333f8ae008f86b717421abbbbfdb7f4c3edb1173f93754364bd778'


def _validate_stage_point_parent_model(old,directory,current_pins):
    if (old.get('source_sha256')!=STAGE_POINT_PARENT_NORMAL
            or old.get('schema')!='complete-fixed-fejer-reference-centred-immutable-point-closure-values-analytic-frame-J3-normal-layer-v1'):
        raise ValueError('Use the complete actual 477499 Fejer M160 source-bound field')
    directory=Path(directory).resolve()
    topic=directory.parents[1]
    driver_path=directory/STAGE_POINT_PARENT_DRIVER[0]
    binding_path=directory/STAGE_POINT_PARENT_BINDING[0]
    if (current_pins.get('stage_point_parent_driver',(None,None))[1]!=STAGE_POINT_PARENT_DRIVER[1]
            or current_pins.get('stage_point_parent_binding',(None,None))[1]!=STAGE_POINT_PARENT_BINDING[1]
            or sha(driver_path)!=STAGE_POINT_PARENT_DRIVER[1]
            or sha(binding_path)!=STAGE_POINT_PARENT_BINDING[1]):
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
    module_name='_complete_stage_point_parent_binding_'+STAGE_POINT_PARENT_BINDING[1]
    if module_name not in sys.modules:
        spec=importlib.util.spec_from_file_location(module_name,binding_path)
        module=importlib.util.module_from_spec(spec)
        sys.modules[module_name]=module
        spec.loader.exec_module(module)
    module=sys.modules[module_name]
    if sha(module.validate_current_model.__code__.co_filename)!=STAGE_POINT_PARENT_BINDING[1]:
        raise ValueError('Use the original complete Fejer M160 model validator')
    old_policies=module.validate_current_model(old,
        roles={role:pair[1] for role,pair in old_pins.items()},source_directory=directory)
    if sha(driver_path)!=STAGE_POINT_PARENT_DRIVER[1] or sha(binding_path)!=STAGE_POINT_PARENT_BINDING[1]:
        raise ValueError('The entire actual parent source changed during validation')
    return tuple(module.POLICY_KEYS.values())




def _compatible_stage_point_parent(old,new,current_pins,*,source_directory):
    """Every actual policy is source-bound; complete physical definitions stay equal."""
    old_keys=_validate_stage_point_parent_model(old,source_directory,current_pins)
    roles={role:pair[1] for role,pair in current_pins.items()}
    validate_current_model(new,roles=roles,source_directory=source_directory)
    before,after=copy.deepcopy(old),copy.deepcopy(new)
    if (before.get('base_complete_model')!=after.get('base_complete_model')
            or before.get('base_model_identity_sha256')!=after.get('base_model_identity_sha256')):
        raise ValueError('The entire fixed base and its complete identity must stay unchanged')
    for key in old_keys:
        before.pop(key)
    for key in POLICY_KEYS.values():
        after.pop(key)
    for value,expected_source in ((before,STAGE_POINT_PARENT_NORMAL),(after,roles['endpoint'])):
        if (value.get('source_sha256')!=expected_source
                or value.get('reference_centering_definition',{}).get('endpoint_source_sha256')!=expected_source):
            raise ValueError('Keep each actual complete normal source in its own calibration definition')
        value.pop('schema');value.pop('source_sha256')
        value['reference_centering_definition'].pop('source_sha256')
        value['reference_centering_definition'].pop('endpoint_source_sha256')
    if before!=after:
        raise ValueError('The full target, reference, chart, seed, Q, free layout, partition and all non-policy fields must match')
    return dict(complete_unchanged_definition_sha256=canonical(before),
        exact_old_complete_model_identity_sha256=canonical(old),
        exact_new_complete_model_identity_sha256=canonical(new),
        full_base_reference_chart_profile_and_partition_equal=True,
        only_explicit_source_schema_and_working_policy_fields_changed=True,
        same_exact_equations_variables_target_and_partition_retained=True,
        complete_stage_point_guard_change_explicit=True,
        complete_detached_meridian_value_policy_change_explicit=True,
        all_old_and_current_working_policies_read_from_their_own_whole_sources=True,
        full_free_layout_exactly_unchanged=True,
        complete_original_110_source_roles_read=True,
        actual_computed_float_field_or_root_words_inherited=False,
        computed_float_field_equality_claimed=False)


def compatible_legacy_model(old,new,current_pins,*,source_directory):
    """Four explicit actual parent sources, each consumed by its entire original reader."""
    roles={role:record[1] for role,record in current_pins.items()}
    validate_current_model(new,roles=roles,source_directory=source_directory)
    if old.get('source_sha256')==STAGE_POINT_PARENT_NORMAL:
        return _compatible_stage_point_parent(old,new,current_pins,source_directory=source_directory)
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
    meridian_expected=policies['detached_meridian_value_reuse']
    if (report.get('detached_meridian_value_reuse_definition')!=meridian_expected
            or report.get('detached_meridian_value_source',{}).get('sha256')!=roles['detached_meridian_values']
            or report.get('meridian_value_original_implicit_and_query_formulas_retained') is not True
            or report.get('meridian_value_active_J_and_transpose_use_original') is not True
            or report.get('meridian_value_speedup_rounding_or_root_certificate') is not False):
        raise ValueError('A meridian value cache retains every original implicit, query and active derivative computation')
    meridian_validator=policies['meridian_actual_validator']
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
                validate_at_own_point(value)
                meridian_validator(value.get('detached_meridian_value_reuse'),
                    model=model,source_by_role=roles,
                    current_full_point_sha256=value.get('current_full_point_sha256'))
                metadata_count+=1
            for child in value.values():visit(child)
        elif isinstance(value,list):
            for child in value:visit(child)
    visit(report)
    latest=report.get('latest_operator_metadata')
    actuals={key:None for key,_ in validators}
    meridian_actual=None
    if latest:
        if latest.get('schema')!=OPERATOR_SCHEMA or latest.get('model')!=model:
            raise ValueError('Do not substitute another latest operator record')
        for key,validator in validators:
            actuals[key]=validator(latest.get(key),model=model,source_by_role=roles,
                current_full_point_sha256=latest.get('current_full_point_sha256'))
        meridian_actual=meridian_validator(latest.get('detached_meridian_value_reuse'),
            model=model,source_by_role=roles,
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
    meridian=dict(source_sha256=roles['detached_meridian_values'],
        actual_operator_source_sha256=roles['endpoint'],
        actual_model_identity_sha256=canonical(model),definition=meridian_expected,
        definition_identity_sha256=canonical(meridian_expected),
        actual_bound_full_metadata_count=metadata_count,
        actual_bound_root_snapshot_count=0,
        latest_actual_diagnostics=meridian_actual,
        snapshot_values_backfilled_from_latest=False,
        original_stage_and_final_equations_reread_by_original_formula=True,
        original_implicit_interface_called_for_every_field=True,
        original_query_jets_and_partial_integrals_retained=True,
        active_J_and_transpose_bypass_cache=True,
        mutable_progress_file_not_consumed_as_immutable_evidence=True,
        speedup_root_or_geometry_certificate_inferred=False,
        current_scientific_values_recomputed=False)
    return dict(schema=SCHEMA,source_sha256=sha(__file__),
        actual_analytic_source_sha256=roles['analytic_J3'],
        actual_operator_source_sha256=roles['endpoint'],
        actual_model_identity_sha256=canonical(model),
        definition=expected,definition_identity_sha256=canonical(expected),
        actual_bound_snapshot_count=count,actual_bound_full_metadata_count=metadata_count,
        latest_actual_diagnostics=actuals['analytic_stage_jacobian'],
        analytic_normal_frame=frame,detached_closure_value_reuse=closure,
        detached_meridian_value_reuse=meridian,
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
