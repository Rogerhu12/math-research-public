#!/usr/bin/env python3
"""Bind one actual complete fixed-deep parent before normalized-parent SO3 work.

No fixed profile digest from another run is substituted.  The complete
actual parent report, original e091 scalar definition, input bytes, and
rebuilt 4ae canonical context must agree.  This is a source/input binder,
not a field computation or a metric/geometry certificate.
"""
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

SCHEMA = 'actual-complete-fixed-deep-parent-for-normalized-SO3-binding-v1'
FACTORY_SHA = '4ae012fbc0ccd58ae093069e0229ee8b72db9ef8d7d153565ef4507dc67db2d1'
BASE_FACTORY_SHA = '2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216'
DEEP_SCALAR_SHA = 'e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2'
BASE_DRIVER_SHA = 'd3c35492a9cef5b4b005829f0ce502d8a377195541b64893f4ab063f0676ba95'
SOC_DRIVER_SHA = '329ebd1828e12d18fcf89137ee0370b7ebafbb61644bbf7bc97cb0b26b284f90'
PARENT_BINDER_SHA = 'd80f9af278b89796d64cebf708080499cd44e3a8cde089be1009b7c26e2105ec'
SCALAR_ROLES = {
    'scalar_source': ('scalar', 'tail_scalar', 'a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670'),
    'integer_source': ('integer', 'tail_integer', 'babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0'),
    'hold_source': ('hold', 'tail_hold', 'ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1'),
    'observed_source': ('observed', 'implementation', '26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d'),
}
OPERATORS = {
    'dense': 'e7aa70c3458f2b1bf823d19870da4e050d50125c31d161d94e2cc8c3cb384b6d',
    'batch': '02a5e83a799d929a9d1426b5eaff9f65484a660932b0bf51634298a1a2284b4a',
    'observed': '26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d',
}


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for chunk in iter(lambda: stream.read(1048576), b''):
            digest.update(chunk)
    return digest.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
        separators=(',', ':'), allow_nan=False).encode('utf-8')).hexdigest()


def record(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path), bytes=path.stat().st_size)


def load_binder(path):
    path = Path(path).resolve()
    if sha(path) != PARENT_BINDER_SHA:
        raise ValueError('Use the actual complete d80 fixed-parent/SOC binder')
    spec = importlib.util.spec_from_file_location('_actual_fixed_deep_source_binder', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def literal_assignment(path, name):
    matches = [node.value for node in ast.parse(Path(path).read_text()).body
        if isinstance(node, ast.Assign) and any(isinstance(target, ast.Name)
        and target.id == name for target in node.targets)]
    if len(matches) != 1:
        raise ValueError('Need one literal source declaration '+name)
    return ast.literal_eval(matches[0])


def bind_actual_parent(args, paths):
    """Bind a real d3 or complete 329e parent and all four complete input bytes."""
    report = json.loads(Path(args.parent_report).read_text())
    if report.get('complete') is not True:
        raise ValueError('Use an actually completed full fixed-deep parent')
    for role, expected in (
            ('deep_parent', BASE_DRIVER_SHA), ('deep_soc_parent', SOC_DRIVER_SHA),
            ('deep_parent_binder', PARENT_BINDER_SHA), ('factory', FACTORY_SHA),
            ('base_factory', BASE_FACTORY_SHA), ('deep_scalar', DEEP_SCALAR_SHA)):
        if sha(paths[role]) != expected:
            raise ValueError('The actual complete source role changed: '+role)
    binder = load_binder(paths['deep_parent_binder'])
    digest = report.get('source_sha256')
    if digest == BASE_DRIVER_SHA:
        if report.get('schema') != 'complete-fixed-deep-scalar-with-held-amplitude-budgets-v1':
            raise ValueError('The actual d3 parent must retain its original report schema')
        expected = literal_assignment(paths['deep_parent'], 'SCALAR_COARSE_EXPECTED_SOURCES')
        source_roles = report['source_sha256_by_role']
        for role, wanted in expected.items():
            if source_roles.get(role) != wanted:
                raise ValueError('The actual full d3 scientific role changed: '+role)
        for role, wanted in (
                ('amplitude_rows', 'd494f92a3d212c40c8b602588c8cfe74f01ff332f116992ffca6469b3978ad8e'),
                ('amplitude_screen', 'e6be35e97702e4185f29fb8f9b7c326fd62083cb4027880956aacdf8b0ba296f')):
            if source_roles.get(role) != wanted:
                raise ValueError('The actual complete amplitude role changed: '+role)
        selected = report.get('selected_scalar_objective_key')
        if selected == 'centered_phi_normalized':
            centered = literal_assignment(paths['deep_parent'], 'SCALAR_CENTERED_SOURCE_SHA')
            if source_roles.get('centered_loss') != centered:
                raise ValueError('The actual selected centered parent statistic changed')
        elif selected != 'phi_normalized':
            raise ValueError('Unknown actual parent scalar objective')
        old_binding = dict(actual_source_sha256=digest,
            actual_source=record(paths['deep_parent']),
            full_fixed_target=binder.verify_fixed_target(report))
    elif digest == SOC_DRIVER_SHA:
        old_binding = binder.bind_report(report, paths['deep_soc_parent'], args.repo)
    else:
        raise ValueError('Choose a genuine complete fixed-deep parent, not a moving target')
    # Reuse the complete published d80 initial/final target verification.
    # The new work below binds its result to actual files and constructor.
    verified = (old_binding['full_fixed_target'] if digest == BASE_DRIVER_SHA
        else old_binding['fixed_scalar_target'])
    fixed = dict(verified, exact_parent_model=report['exact_tail_context']['definition'],
        target_fixed_before_new_field_construction=True, target_from_current_SO3_field=False)
    model = fixed['exact_parent_model']
    if (fixed['exact_profile_definition'].get('source_sha256') != DEEP_SCALAR_SHA
            or model.get('operator_source_sha256s') != OPERATORS
            or model.get('source_sha256s') != {role: value[2] for role, value in SCALAR_ROLES.items()}):
        raise ValueError('The actual complete scalar and physical-operator definitions changed')
    files = {key: record(path) for key, path in dict(
        parent_bundle=args.parent_bundle, carrier=args.carrier,
        node_report=args.node_report, scalar_input=args.scalar_input).items()}
    for field, role in (
            ('final_bundle_sha256', 'parent_bundle'),
            ('observation_carrier_sha256', 'carrier'),
            ('exact_tail_node_report_sha256', 'node_report'),
            ('exact_tail_scalar_input_sha256', 'scalar_input')):
        if report.get(field) != files[role]['sha256']:
            raise ValueError('The actual parent report has different complete bytes: '+field)
    model = fixed['exact_parent_model']
    for role, field in (
            ('carrier', 'original_observation_carrier_sha256'),
            ('node_report', 'node_report_sha256'),
            ('scalar_input', 'scalar_input_sha256')):
        if files[role]['sha256'] != model.get(field):
            raise ValueError('Canonical parent input differs from its actual bytes: '+role)
    for role, (path_role, report_role, expected) in SCALAR_ROLES.items():
        if sha(paths[path_role]) != expected:
            raise ValueError('The new consumer must retain the actual scalar source '+role)
        if report['source_sha256_by_role'].get(report_role) != expected:
            raise ValueError('The parent scalar runtime source differs: '+report_role)
    expected_original = dict(scalar_input=files['scalar_input']['sha256'],
        scalar_source=SCALAR_ROLES['scalar_source'][2],
        integer_source=SCALAR_ROLES['integer_source'][2],
        hold_source=SCALAR_ROLES['hold_source'][2])
    if fixed['exact_profile_definition'].get('original_input') != expected_original:
        raise ValueError('The e091 definition is not bound to this exact original scalar and three sources')
    nodes = json.loads(Path(args.node_report).read_text())
    if (nodes.get('schema') != 'deep-valley-fixed-scalar-symbolic-nodes-v1'
            or nodes.get('input_sha256') != files['scalar_input']['sha256']
            or nodes.get('scalar_model_identity_sha256') != fixed['identity_sha256']
            or report.get('exact_tail_lambda') != 1.
            or report.get('exact_tail_eta_start_node') != args.eta_start_node
            or model.get('eta_start_node') != args.eta_start_node
            or int(report['N']) != args.angles):
        raise ValueError('Retain the actual exact profile/nodes/eta and the original complete angle grid')
    binding = dict(schema=SCHEMA, source_sha256=sha(__file__),
        original_parent_report=record(args.parent_report),
        actual_parent_source_binding=old_binding, complete_input_records=files,
        fixed_scalar_target=fixed, canonical_profile_from_actual_parent=True,
        profile_digest_copied_from_another_run=False,
        no_old_metric_or_geometry_certificate_inherited=True,
        rebuilt_context_independently_verified=False)
    binding['binding_identity_sha256'] = canonical(binding)
    return report, binding


def bind_rebuilt_context(context, report, binding):
    """Verify the actual physical constructor result, not only report labels."""
    if binding.get('schema') != SCHEMA or binding.get('source_sha256') != sha(__file__):
        raise ValueError('The same complete input binder must verify the rebuilt context')
    payload = {key: value for key, value in binding.items() if key != 'binding_identity_sha256'}
    if canonical(payload) != binding['binding_identity_sha256']:
        raise ValueError('The frozen actual parent binding changed after construction')
    fixed = binding['fixed_scalar_target']
    actual = context.definition()
    if (sha(context.definition.__code__.co_filename) != FACTORY_SHA
            or sha(context.create_pair.__code__.co_filename) != FACTORY_SHA
            or sha(context.deep.reference_at_affine.__code__.co_filename) != DEEP_SCALAR_SHA
            or context.deep.model_identity_sha256 != fixed['identity_sha256']
            or context.deep.definition != fixed['exact_profile_definition']
            or canonical(context.deep.definition) != fixed['identity_sha256']
            or actual != fixed['exact_parent_model']
            or actual != report['exact_tail_context_final']['definition']
            or canonical(actual) != fixed['actual_model_identity_sha256']):
        raise ValueError('Rebuilt actual whole context differs from the frozen parent scalar or canonical model')
    for role, current_role in (
            ('parent_bundle', 'bundle'), ('carrier', 'carrier'),
            ('node_report', 'node_report'), ('scalar_input', 'scalar_input')):
        expected = binding['complete_input_records'][role]['sha256']
        if context.input_records[current_role]['sha256'] != expected or sha(context.paths[current_role]) != expected:
            raise ValueError('An actual physical constructor input changed: '+current_role)
    for role, expected in OPERATORS.items():
        source = context._operator_sources.get(role)
        if source is None or source['sha256'] != expected or sha(source['path']) != expected:
            raise ValueError('The actual full physical operator dependency changed: '+role)
    if set(context._operator_sources) != set(OPERATORS):
        raise ValueError('No complete physical operator source may be omitted or added')
    if 'reference_tail_model_json' not in context.data:
        raise ValueError('The actual complete bundle must contain its canonical mathematical definition')
    if json.loads(str(context.data['reference_tail_model_json'].item())) != actual:
        raise ValueError('The actual parent bundle canonical model differs from the rebuilt whole context')
    return dict(schema='rebuilt-whole-fixed-deep-parent-context-binding-v1',
        source_sha256=sha(__file__), parent_binding_identity_sha256=binding['binding_identity_sha256'],
        fixed_scalar_metric_identity_sha256=fixed['identity_sha256'],
        canonical_model_identity_sha256=canonical(actual),
        exact_profile_definition_equal=True, complete_parent_definition_equal=True,
        all_four_actual_input_bytes_equal=True,
        actual_runtime_source_functions_bound=True,
        no_field_metric_or_geometry_value_inherited=True)


def verify_saved_binding(report, *, expected_binding_source_sha256):
    """Pure report attribution of the already verified fixed-parent binding."""
    binding = report['frozen_parent_binding']
    rebuilt = report['rebuilt_parent_context_binding']
    target = binding['fixed_scalar_target']
    profile = report['fixed_scalar_metric']
    identity = target['identity_sha256']
    model = target['exact_parent_model']
    payload = {key: value for key, value in binding.items() if key != 'binding_identity_sha256'}
    if (binding.get('schema') != SCHEMA
            or binding.get('source_sha256') != expected_binding_source_sha256
            or canonical(payload) != binding['binding_identity_sha256']
            or canonical(target['exact_profile_definition']) != identity
            or target['exact_profile_definition'].get('source_sha256') != DEEP_SCALAR_SHA
            or canonical(model) != target['actual_model_identity_sha256']
            or model.get('profile_identity_sha256') != identity
            or model.get('profile_definition') != target['exact_profile_definition']
            or model.get('source_sha256') != FACTORY_SHA
            or model.get('base_reference_factory_source_sha256') != BASE_FACTORY_SHA
            or model.get('deep_scalar_source_sha256') != DEEP_SCALAR_SHA
            or model.get('fixed_new_scalar_metric') is not True
            or model.get('target_is_a_moving_angular_mean') is not False
            or model.get('lambda_value') != 1.
            or profile.get('identity_sha256') != identity
            or profile.get('exact_profile_definition') != target['exact_profile_definition']
            or report['exact_tail_context']['definition'] != model
            or report['exact_tail_context']['model_identity_sha256'] != canonical(model)
            or report['representation']['frozen_parent_complete_model'] != model
            or report['representation']['frozen_parent_model_identity_sha256'] != canonical(model)
            or report['representation']['fixed_scalar_profile_definition'] != target['exact_profile_definition']
            or rebuilt.get('schema') != 'rebuilt-whole-fixed-deep-parent-context-binding-v1'
            or rebuilt.get('source_sha256') != expected_binding_source_sha256
            or rebuilt.get('parent_binding_identity_sha256') != binding['binding_identity_sha256']
            or rebuilt.get('fixed_scalar_metric_identity_sha256') != identity
            or rebuilt.get('canonical_model_identity_sha256') != canonical(model)):
        raise ValueError('Saved actual SO3 target/binding/context is not the same frozen canonical parent')
    for key in ('exact_profile_definition_equal', 'complete_parent_definition_equal',
                'all_four_actual_input_bytes_equal', 'actual_runtime_source_functions_bound',
                'no_field_metric_or_geometry_value_inherited'):
        if rebuilt.get(key) is not True:
            raise ValueError('The actual whole context verification is incomplete: '+key)
    files = binding['complete_input_records']
    for role, field in (
            ('parent_bundle', 'bundle_sha256'),
            ('carrier', 'observation_carrier_sha256'),
            ('node_report', 'exact_tail_node_report_sha256'),
            ('scalar_input', 'exact_tail_scalar_input_sha256')):
        if files[role]['sha256'] != report[field]:
            raise ValueError('Saved actual complete input binding changed: '+role)
    if (files['carrier']['sha256'] != model['original_observation_carrier_sha256']
            or files['node_report']['sha256'] != model['node_report_sha256']
            or files['scalar_input']['sha256'] != model['scalar_input_sha256']
            or files['parent_bundle']['sha256'] != report['representation']['frozen_parent_bundle_sha256']
            or report['original_parent_report']['sha256'] != binding['original_parent_report']['sha256']
            or binding.get('canonical_profile_from_actual_parent') is not True
            or binding.get('profile_digest_copied_from_another_run') is not False
            or target.get('target_fixed_before_new_field_construction') is not True
            or target.get('target_from_current_SO3_field') is not False):
        raise ValueError('The actual frozen input/source provenance was replaced by another run')
    return identity
