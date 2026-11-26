#!/usr/bin/env python3
"""Pure-text construction of the complete new gamma/KKT entry.

Only stdlib source/AST/bytes are read. No scientific module is imported.
The complete outer QP and physical-screen loop is retained from the pinned
continuation entry; all changed setup and root-report interfaces are explicit.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path
import pprint


PARENTS = {
    'driver': ('fullclosed_zero_moment_continuation_so3_qp.py', '9649ed99b614c468258646145948d7c06feb356c72806c73727728ea498ed88e'),
    'launcher': ('launch_zero_moment_continuation_so3_actions.py', 'e57eb3d7f85a0abb44fb75ea56e918a9cd254025a718936bc163b82131f774d9'),
    'reader': ('read_zero_moment_continuation_so3_report.py', 'a0c927aa9d7608a16ad7c051861903ebb533be3602325c2aada60ed6b1ccae61')}
REPORT_SCHEMA = 'complete-independent-fixed-deep-added-gamma-nine-KKT-SO3-QP-v1'
OPERATOR_SCHEMA = 'complete-direct-R690-SO3-added-gamma-six-control-KKT-zero-layer-v1'
SNAPSHOT_SCHEMA = 'actual-added-gamma-nine-KKT-current-point-snapshot-v1'
NAMES = {
    'driver': 'fullclosed_zero_gamma_kkt_so3_qp.py',
    'launcher': 'launch_zero_gamma_kkt_so3_actions.py',
    'reader': 'read_zero_gamma_kkt_so3_report.py'}
ROOT_KEYS = (
    'current_full_point_sha256', 'endpoint_root_policy',
    'current_cached_angle_roots', 'current_all_grid_angle_roots_available',
    'current_maximum_endpoint_residual', 'current_maximum_dimensionless_control_norm',
    'current_maximum_multiplier_norm', 'current_maximum_KKT_residual',
    'current_maximum_stationarity_residual', 'current_maximum_physical_z_norm',
    'current_maximum_gamma_axis_norm', 'current_minimum_KKT_sample_singular_value',
    'current_maximum_first_angular_root_residual',
    'current_maximum_second_angular_root_residual',
    'endpoint_counts', 'actual_KKT_counts', 'last_root_failure',
    'endpoint_continuation_policy', 'endpoint_continuation_counts',
    'endpoint_continuation_last_summary',
    'numerical_Newton_iterations_differentiated',
    'complete_uniform_IFT_conditions_verified',
    'complete_continuous_root_branch_certified', 'endpoint_root_error_enclosed',
    'selected_KKT_stationary_branch', 'SOSC_verified', 'global_minimum_verified')


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def function(source, name):
    matches = [n for n in ast.parse(source).body if isinstance(n, (ast.FunctionDef, ast.ClassDef)) and n.name == name]
    if len(matches) != 1:
        raise ValueError(('one whole source function required', name))
    node = matches[0]
    return '\n'.join(source.splitlines()[node.lineno-1:node.end_lineno])+'\n'


def replace_function(source, name, value):
    old = function(source, name)
    if source.count(old) != 1:
        raise ValueError(('whole function identity changed', name))
    return source.replace(old, value.rstrip()+'\n', 1)


def replace_once(source, old, new):
    if source.count(old) != 1:
        raise ValueError(('exact source edit mismatch', old[:120], source.count(old)))
    return source.replace(old, new, 1)


def assignment(source, name, value):
    nodes = [n for n in ast.parse(source).body if isinstance(n, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == name for t in n.targets)]
    if len(nodes) != 1:
        raise ValueError(('one exact literal assignment required', name))
    node = nodes[0]
    lines = source.splitlines(True)
    return ''.join(lines[:node.lineno-1])+name+' = '+pprint.pformat(value, width=100, sort_dicts=False)+'\n'+''.join(lines[node.end_lineno:])


def declaration(source, name):
    nodes = [n for n in ast.parse(source).body if isinstance(n, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == name for t in n.targets)]
    if len(nodes) != 1:
        raise ValueError(('literal declaration missing', name))
    return ast.literal_eval(nodes[0].value)


def parse_source(parent):
    value = function(parent, 'parse_args')
    value = replace_once(value,
        "    p.add_argument('--endpoint-root-branch-radius', type=float, default=.5)",
        "    p.add_argument('--endpoint-kkt-tolerance', type=float, default=2.e-12)\n"
        "    p.add_argument('--endpoint-control-radius', type=float, default=2.)\n"
        "    p.add_argument('--endpoint-multiplier-radius', type=float, default=64.)\n"
        "    p.add_argument('--gamma-left', default='1/16')\n"
        "    p.add_argument('--gamma-middle', default='1/8')\n"
        "    p.add_argument('--gamma-right', default='3/16')")
    value = replace_once(value, "    p.add_argument('--moment-definition-sha256')",
        "    p.add_argument('--moment-definition-sha256')\n"
        "    p.add_argument('--moment-input-binding', choices=('same-reference', 'new-reference'), default='same-reference')")
    value = replace_once(value, '    a = p.parse_args()\n',
        "    a = p.parse_args()\n"
        "    if a.moment_input_binding == 'new-reference' and a.moment_trace_report is not None:\n"
        "        raise ValueError('The explicit new-reference mode adopts the published literal parameter input; it does not relabel an old trace as current')\n")
    value = replace_once(value, "    if (a.endpoint_root_iterations < 1 or a.endpoint_root_backtracks < 1",
        "    gamma = [Fraction(getattr(a, 'gamma_'+position)) for position in ('left','middle','right')]\n"
        "    if (not 0 < gamma[0] < gamma[1] < gamma[2] < 1\n"
        "            or not any(Fraction(getattr(a,'endpoint_bubble_'+str(i)+'_left')) < gamma[0]\n"
        "                < gamma[2] < Fraction(getattr(a,'endpoint_bubble_'+str(i)+'_right')) for i in (1,2))):\n"
        "        raise ValueError('The complete independent gamma support must lie strictly inside an original bubble support')\n"
        "    if (a.endpoint_root_iterations < 1 or a.endpoint_root_backtracks < 1")
    value = replace_once(value, 'a.endpoint_root_tolerance, a.endpoint_root_branch_radius',
        'a.endpoint_root_tolerance, a.endpoint_kkt_tolerance,\n'
        '                a.endpoint_control_radius, a.endpoint_multiplier_radius')
    return value


DRIVER_READOUT = '''def endpoint_readout(q):
    """A complete explicit current-point snapshot; no replacement from another point."""
    value = q.metadata()
    result = {name: value[name] for name in ROOT_SNAPSHOT_KEYS}
    result.update(schema=ROOT_SNAPSHOT_SCHEMA,
        operator_schema=value['schema'], operator_source_sha256=value['source_sha256'],
        model_identity_sha256=value['model_identity_sha256'],
        snapshot_scope='actual current point and its own continuation/root cache at this call; absent numerical values remain null')
    return result
'''


MOMENT_SETUP = '''    if args.moment_input_binding == 'new-reference':
        origin = moment_binding.from_parameter_file(args.moment_input,
            input_sha256=args.moment_input_sha256,
            expected_definition_identity_sha256=args.moment_definition_sha256)
        frozen_moment_input = new_moment_binding.bind_new_input(origin,
            base_model=base.model, initial_reference_bundle_sha256=sha(args.reference_bundle),
            fixed_scalar_metric_identity_sha256=fixed_profile,
            initial_full_point_sha256=meridian.array_sha(base.initial()), bubble_nodes=bubble_nodes)
        moment_definition_identity = new_moment_binding.bind_to_base(frozen_moment_input,
            base_model=base.model, initial_reference_bundle_sha256=sha(args.reference_bundle),
            fixed_scalar_metric_identity_sha256=fixed_profile,
            initial_full_point_sha256=meridian.array_sha(base.initial()), bubble_nodes=bubble_nodes)
        moment_input_record = dict(mode='explicit NEW reference adopts complete published literal Q parameters',
            actual_parameter_file=file_record(args.moment_input),
            input_binding_source=file_record(paths['new_moment_input']),
            no_moment_or_inverse_recomputed=True, old_reference_or_initial_point_binding_inherited=False,
            same_mathematical_g_claimed=False, current_moment_inverse_property_claimed=False)
    else:
        if args.moment_trace_report is not None:
            frozen_moment_input = moment_binding.from_trace(args.repo, args.moment_trace_report,
                trace_report_sha256=args.moment_trace_report_sha256,
                failed_report=args.moment_failed_report,
                expected_definition_identity_sha256=args.moment_definition_sha256)
            moment_input_record = dict(mode='strict SAME reference actual trace word extraction',
                actual_trace_report=file_record(args.moment_trace_report),
                actual_failed_report=file_record(args.moment_failed_report),
                no_moment_or_inverse_recomputed=True)
        else:
            frozen_moment_input = moment_binding.from_parameter_file(args.moment_input,
                input_sha256=args.moment_input_sha256,
                expected_definition_identity_sha256=args.moment_definition_sha256)
            moment_input_record = dict(mode='strict SAME reference published complete parameter definition',
                actual_parameter_file=file_record(args.moment_input),
                no_moment_or_inverse_recomputed=True)
        moment_definition_identity = moment_binding.bind_to_base(frozen_moment_input,
            base_model=base.model, initial_reference_bundle_sha256=sha(args.reference_bundle),
            fixed_scalar_metric_identity_sha256=fixed_profile, bubble_nodes=bubble_nodes)
'''


def make_driver(parent, pins):
    source = assignment(parent, 'SCHEMA', REPORT_SCHEMA)
    source = replace_once(source,
        'Independent frozen literal moment-Q zero-closure SO(3) optimization of one fixed deep g.',
        'Independent added-gamma six-control KKT SO(3) optimization of one actual fixed deep g.')
    source = replace_once(source,
        'An actual implicit endpoint root replaces the closure lift. The complete\nfirst-parameter implicit 6x6/9x9 system is inside every Gram and geometric\nderivative; numerical Newton iterations have no derivative graph.',
        'A new independent radial gamma and all six controls enter nine KKT equations.\nThe complete first-parameter implicit 18x18/27x27 control-and-multiplier\nsystem is inside every Gram and geometric derivative; numerical Newton\nand auxiliary continuation iterations have no derivative graph.')
    source = assignment(source, 'SOURCE_PINS', pins)
    source = replace_once(source, '\n\ndef sha(path):',
        '\n\nROOT_SNAPSHOT_SCHEMA = '+repr(SNAPSHOT_SCHEMA)+'\nROOT_SNAPSHOT_KEYS = '
        +pprint.pformat(ROOT_KEYS, width=100)+'\n\ndef sha(path):')
    source = replace_function(source, 'parse_args', parse_source(parent))
    source = replace_function(source, 'endpoint_readout', DRIVER_READOUT)
    source = replace_once(source,
        "    moment_binding = load('_so3_complete_frozen_moment_input', paths['frozen_moment_input'])",
        "    moment_binding = load('_so3_complete_frozen_moment_input', paths['frozen_moment_input'])\n"
        "    new_moment_binding = load('_so3_explicit_new_reference_literal_Q', paths['new_moment_input'])")
    source = replace_once(source, 'root_policy = endpoint.EndpointPolicy(tolerance=args.endpoint_root_tolerance,',
        'root_policy = endpoint.EndpointPolicy(endpoint_tolerance=args.endpoint_root_tolerance,\n'
        '        kkt_tolerance=args.endpoint_kkt_tolerance,')
    source = replace_once(source, 'armijo=args.endpoint_root_armijo, branch_radius=args.endpoint_root_branch_radius)',
        'armijo=args.endpoint_root_armijo, control_radius=args.endpoint_control_radius,\n'
        '        multiplier_radius=args.endpoint_multiplier_radius)')
    start = source.index('    if args.moment_trace_report is not None:', source.index('def main():'))
    end = source.index('    q = endpoint.ZeroClosureOperator(', start)
    source = source[:start]+MOMENT_SETUP+source[end:]
    source = replace_once(source, '        continuation_policy=continuation_policy)\n',
        '        continuation_policy=continuation_policy,\n'
        '        gamma_nodes=(args.gamma_left,args.gamma_middle,args.gamma_right),\n'
        "        new_input_binder=(new_moment_binding if args.moment_input_binding == 'new-reference' else None))\n")
    source = replace_once(source, '        endpoint_continuation_final_equation_is_original_C=True,',
        '        endpoint_continuation_final_equation_is_original_KKT=True,\n'
        '        final_original_physical_closure_is_separately_checked=True,\n'
        '        moment_input_binding_mode=args.moment_input_binding,\n'
        '        implicit_control_dimension=6, KKT_dimension=9, complete_second_angular_implicit_dimension=27,\n'
        "        implicit_control_cost='(|z/S|^2+|v|^2)/2',\n"
        '        selected_KKT_stationary_branch=True, SOSC_verified=False, global_minimum_verified=False,')
    source = replace_once(source, "            exact_relative_bubble_nodes=q.model['exact_relative_bubble_nodes'],",
        "            exact_relative_bubble_nodes=q.model['exact_relative_bubble_nodes'],\n"
        "            exact_relative_gamma_nodes=q.model['exact_relative_gamma_nodes'],\n"
        '            implicit_control_dimension=6, KKT_dimension=9, complete_second_angular_implicit_dimension=27,')
    source = replace_once(source, "        frozen_moment_Q_input_record=moment_input_record,",
        "        frozen_moment_Q_input_record=moment_input_record,\n"
        "        actual_reference_initial_full_point_sha256=meridian.array_sha(base.initial()),")
    return source


def make_launcher(parent, driver, driver_sha):
    source = assignment(parent, 'DRIVER_SHA', driver_sha)
    source = source.replace('complete independent zero-closure SO3 QP',
        'complete added-gamma nine-KKT SO3 QP')
    parser = function(driver, 'parse_args')
    parser = replace_once(parser, '    a = p.parse_args()\n',
        "    p.add_argument('--install-torch', action='store_true')\n"
        "    p.add_argument('--print-command', action='store_true')\n"
        '    a = p.parse_args()\n')
    source = replace_function(source, 'parse_args', parser)
    source = source.replace(PARENTS['driver'][0], NAMES['driver'])
    source = source.replace('public-actions-complete-frozen-Q-endpoint-continuation-SO3-command-v1',
        'public-actions-complete-added-gamma-nine-KKT-SO3-command-v1')
    source = replace_once(source, '        endpoint_root_implicit_derivative_separate_from_iterations=True,',
        '        endpoint_root_implicit_derivative_separate_from_iterations=True,\n'
        '        implicit_control_dimension=6, KKT_dimension=9, complete_second_angular_implicit_dimension=27,\n'
        '        full_multiplier_and_constraint_Hessian_chain_retained=True,')
    return source


READER_ROOTS = '''def endpoint_roots(value):
    """Read this point's explicit snapshot, or an already bound full metadata record."""
    if value is None:
        return None
    if value.get('schema') not in (ROOT_SNAPSHOT_SCHEMA, OPERATOR_SCHEMA):
        raise ValueError('No old short endpoint snapshot is relabelled as a complete new KKT snapshot')
    missing = [key for key in ROOT_SNAPSHOT_KEYS if key not in value]
    if missing:
        raise ValueError('The actual NEW KKT snapshot lacks its declared fields: '+repr(missing))
    for key in ('numerical_Newton_iterations_differentiated',
                'complete_uniform_IFT_conditions_verified',
                'complete_continuous_root_branch_certified', 'endpoint_root_error_enclosed',
                'SOSC_verified', 'global_minimum_verified'):
        if value[key] is not False:
            raise ValueError('The numerical KKT record cannot certify '+key)
    if value['selected_KKT_stationary_branch'] is not True:
        raise ValueError('Keep the declared stationary-branch scope')
    result = {key:value[key] for key in ROOT_SNAPSHOT_KEYS}
    result.update(actual_snapshot_schema=value['schema'],
        all_grid_roots_available_is_a_numerical_cache_statement_only=True,
        missing_point_values_replaced_from_latest_metadata=False,
        KKT_stationarity_is_local_or_global_minimum_proof=False)
    return result
'''


READER_SNAPSHOT_BINDING = '''def bind_snapshots(value, model, roles):
    """Bind every stored short readout to this exact operator/model, without filling gaps."""
    count = 0
    if isinstance(value, dict):
        if value.get('schema') == ROOT_SNAPSHOT_SCHEMA:
            if (value.get('operator_schema') != OPERATOR_SCHEMA
                    or value.get('operator_source_sha256') != roles['endpoint']
                    or value.get('model_identity_sha256') != canonical(model)):
                raise ValueError('A stored KKT snapshot belongs to another actual operator/model')
            endpoint_roots(value)
            count += 1
        for key,child in value.items():
            if key in ('endpoint_roots','initial_endpoint_roots') and child is not None:
                if not isinstance(child,dict) or child.get('schema') != ROOT_SNAPSHOT_SCHEMA:
                    raise ValueError('Every actual point-read snapshot must use its complete NEW declared contract')
            count += bind_snapshots(child,model,roles)
    elif isinstance(value,list):
        count += sum(bind_snapshots(child,model,roles) for child in value)
    return count


def bind_literal_input(topic, report, model, roles, profile):
    """Pure complete source and definition validation for two DISJOINT input modes."""
    value = report['frozen_moment_Q_input']
    mode = report['moment_input_binding_mode']
    if mode == 'same-reference':
        role,filename = 'frozen_moment_input','frozen_zero_moment_input.py'
        if (value.get('schema') != 'frozen-zero-endpoint-moment-Q-input-v1'
                or model.get('new_reference_input_binding_source_sha256') is not None):
            raise ValueError('The original strict same-reference input keeps its original schema and validator')
    elif mode == 'new-reference':
        role,filename = 'new_moment_input','new_reference_literal_zero_moment_input.py'
        if (value.get('schema') != 'new-reference-literal-zero-endpoint-Q-input-v1'
                or model.get('new_reference_input_binding_source_sha256') != roles[role]
                or report['frozen_moment_Q_input_record'].get('same_mathematical_g_claimed') is not False
                or report['frozen_moment_Q_input_record'].get('current_moment_inverse_property_claimed') is not False):
            raise ValueError('The new actual reference adopts literal parameters without an old-field or inverse claim')
    else:
        raise ValueError('Declare one explicit complete literal-input binding mode')
    path = topic/'scripts/resume_20261126'/filename
    if sha(path) != roles[role]:
        raise ValueError('The complete selected pure input binder differs')
    spec = importlib.util.spec_from_file_location('_pure_gamma_Q_'+roles[role],path)
    binder = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = binder
    spec.loader.exec_module(binder)
    kwargs = dict(base_model=model['base_complete_model'],
        initial_reference_bundle_sha256=report['bundle_sha256'],
        fixed_scalar_metric_identity_sha256=profile,
        bubble_nodes=model['exact_relative_bubble_nodes'])
    if mode == 'new-reference':
        kwargs['initial_full_point_sha256'] = report['actual_reference_initial_full_point_sha256']
    identity = binder.bind_to_base(value,**kwargs)
    if (model.get('literal_Q_input_schema') != value['schema']
            or model.get('historical_reference_same_mathematical_g_claimed') is not False):
        raise ValueError('Keep the actual new control-input mode and its historical-identity boundary')
    return value, identity
'''


def make_reader(parent, driver, driver_sha, pins):
    source = assignment(parent,'DRIVER_SHA',driver_sha)
    source = assignment(source,'REPORT_SCHEMA',REPORT_SCHEMA)
    source = replace_once(source,'\n\ndef sha(path):',
        '\n\nOPERATOR_SCHEMA = '+repr(OPERATOR_SCHEMA)+'\nROOT_SNAPSHOT_SCHEMA = '+repr(SNAPSHOT_SCHEMA)
        +'\nROOT_SNAPSHOT_KEYS = '+pprint.pformat(ROOT_KEYS,width=100)+'\n\ndef sha(path):')
    source = replace_function(source,'endpoint_roots',READER_ROOTS)
    source = replace_once(source,'\ndef endpoint_metadata(', '\n'+READER_SNAPSHOT_BINDING+'\ndef endpoint_metadata(')
    metadata = function(source,'endpoint_metadata')
    metadata = metadata.replace('final_implicit_J_uses_original_endpoint_equation',
                                'final_implicit_J_uses_original_KKT_equation')
    metadata = metadata.replace('all_attempted_fields_maximum_successful_correction_norm',
                                'all_attempted_fields_maximum_successful_dimensionless_control_norm')
    metadata = metadata.replace('all_attempted_fields_minimum_sample_endpoint_singular_value',
                                'all_attempted_fields_minimum_sample_KKT_singular_value')
    metadata = replace_once(metadata,
        "        'all_attempted_fields_maximum_core_inverse_residual',",
        "        'all_attempted_fields_maximum_successful_KKT_residual',\n"
        "        'all_attempted_fields_maximum_successful_multiplier_norm',\n"
        "        'all_attempted_fields_maximum_core_inverse_residual',")
    metadata = replace_once(metadata,'    current = endpoint_roots(value)',
        "    if (value.get('implicit_control_dimension') != 6 or value.get('KKT_dimension') != 9\n"
        "            or value.get('complete_second_angular_implicit_dimension') != 27\n"
        "            or value.get('implicit_control_cost') != '(|z/S|^2+|v|^2)/2'\n"
        "            or value.get('exact_relative_gamma_nodes') != model['exact_relative_gamma_nodes']\n"
        "            or value.get('maximum_required_mixed_exponential_derivative_order') != 4\n"
        "            or value.get('literal_Q_input_schema') != model['literal_Q_input_schema']\n"
        "            or value.get('new_reference_input_binding_source_sha256') != model['new_reference_input_binding_source_sha256']):\n"
        "        raise ValueError('Retain all six controls, nine KKT equations and twenty-seven implicit angle jets')\n"
        '    current = endpoint_roots(value)')
    metadata = replace_once(metadata, "        continuation_counts_scope=value['continuation_counts_scope'],",
        "        continuation_counts_scope=value['continuation_counts_scope'],\n"
        "        actual_KKT_counts=value['actual_KKT_counts'], actual_KKT_counter_scope=value['actual_KKT_counter_scope'],\n"
        '        implicit_control_dimension=6, KKT_dimension=9, complete_second_angular_implicit_dimension=27,\n'
        '        full_multiplier_and_constraint_Hessian_chain_retained=True,\n'
        '        maximum_required_mixed_exponential_derivative_order=4,\n'
        '        selected_KKT_stationary_branch=True, SOSC_verified=False, global_minimum_verified=False,')
    source = replace_function(source,'endpoint_metadata',metadata)
    source = source.replace(PARENTS['driver'][0],NAMES['driver'])
    start = source.index("    binder_path = topic/'scripts/resume_20261126/frozen_zero_moment_input.py'",source.index('def read_report('))
    end = source.index('    if (model.get(\'schema\')',start)
    source = source[:start]+"    frozen_input, moment_identity = bind_literal_input(topic,report,model,roles,profile)\n"+source[end:]
    source = source.replace("'complete-direct-R690-frozen-Q-residual-continuation-zero-endpoint-layer-v1'",repr(OPERATOR_SCHEMA))
    source = source.replace('original_implicit_root_algorithm_source_sha256','historical_original_three_root_algorithm_source_sha256')
    source = replace_once(source,
        "            or float(working['endpoint_root_policy']['branch_radius']).hex() != model['root_branch_radius_hex']",
        "            or working['exact_relative_gamma_nodes'] != model['exact_relative_gamma_nodes']\n"
        "            or working['endpoint_root_policy'] != model['root_KKT_policy']\n"
        "            or float(working['endpoint_root_policy']['control_radius']).hex() != model['root_control_radius_hex']\n"
        "            or float(working['endpoint_root_policy']['multiplier_radius']).hex() != model['root_multiplier_radius_hex']")
    source = source.replace('endpoint_continuation_final_equation_is_original_C',
                            'endpoint_continuation_final_equation_is_original_KKT')
    source = replace_once(source, "    seed = report.get('direct_base_seed')",
        "    for container in (model,report,working):\n"
        "        if (container.get('implicit_control_dimension') != 6 or container.get('KKT_dimension') != 9\n"
        "                or container.get('complete_second_angular_implicit_dimension') != 27):\n"
        "            raise ValueError('Every actual field/working/report contract retains the complete KKT dimensions')\n"
        "    for container in (model,report):\n"
        "        if (container.get('implicit_control_cost') != '(|z/S|^2+|v|^2)/2'\n"
        "                or container.get('selected_KKT_stationary_branch') is not True\n"
        "                or container.get('SOSC_verified') is not False\n"
        "                or container.get('global_minimum_verified') is not False):\n"
        "            raise ValueError('A numerical KKT stationary point is not a certified minimum')\n"
        "    if report.get('final_original_physical_closure_is_separately_checked') is not True:\n"
        "        raise ValueError('Normalized KKT residual tolerance cannot replace the original physical closure tolerance')\n"
        "    snapshot_count = bind_snapshots(report,model,roles)\n"
        "    seed = report.get('direct_base_seed')")
    source = source.replace('actual-complete-frozen-Q-endpoint-continuation-SO3-scalar-readout-v1',
                            'actual-complete-added-gamma-nine-KKT-SO3-scalar-readout-v1')
    source = replace_once(source, "        actual_base_source_sha256=roles['meridian'],",
        "        actual_base_source_sha256=roles['meridian'],\n"
        "        moment_input_binding_mode=report['moment_input_binding_mode'],\n"
        "        actual_reference_initial_full_point_sha256=report['actual_reference_initial_full_point_sha256'],\n"
        '        actual_bound_current_point_snapshot_count=snapshot_count,\n'
        '        snapshot_values_backfilled_from_other_points=False,\n'
        '        implicit_control_dimension=6, KKT_dimension=9, complete_second_angular_implicit_dimension=27,\n'
        "        exact_relative_gamma_nodes=model['exact_relative_gamma_nodes'],\n"
        "        implicit_control_cost='(|z/S|^2+|v|^2)/2',\n"
        '        selected_KKT_stationary_branch=True, SOSC_verified=False, global_minimum_verified=False,')
    return source


def normalized(source):
    source = '\n'.join(line.rstrip() for line in source.splitlines())+'\n'
    tree = ast.parse(source)
    compile(tree, '<complete pure source construction>', 'exec')
    for node in ast.walk(tree):
        if isinstance(node, ast.Dict):
            keys = [k.value for k in node.keys if isinstance(k,ast.Constant)
                and isinstance(k.value,(str,int,float))]
            if len(keys) != len(set(keys)):
                raise ValueError(('duplicate literal key',node.lineno))
    return source


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', type=Path, required=True)
    p.add_argument('--operator-source', type=Path, required=True)
    p.add_argument('--geometry-source', type=Path, required=True)
    p.add_argument('--new-input-binder-source', type=Path, required=True)
    p.add_argument('--outdir', type=Path, required=True)
    args = p.parse_args()
    directory = args.repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261126'
    parents = {role:(directory/name).read_text() for role,(name,expected) in PARENTS.items()}
    for role,(name,expected) in PARENTS.items():
        if digest(parents[role]) != expected:
            raise ValueError('The complete pinned parent source changed: '+name)
    dependencies = {'endpoint':args.operator_source, 'geometry':args.geometry_source,
                    'new_moment_input':args.new_input_binder_source}
    pins = declaration(parents['driver'],'SOURCE_PINS')
    for role,path in dependencies.items():
        body = path.read_text()
        if '__UNLOCKED' in body:
            raise ValueError('A required complete source is not yet locked: '+str(path))
        ast.parse(body)
        pins[role] = ('scripts/resume_20261126/'+path.name, digest(body))
    driver = normalized(make_driver(parents['driver'],pins))
    launcher = normalized(make_launcher(parents['launcher'],driver,digest(driver)))
    # The reader builder is a separate pure-text section below. It must
    # explicitly handle the NEW complete snapshot and both input contracts.
    reader = normalized(make_reader(parents['reader'],driver,digest(driver),pins))
    args.outdir.mkdir(parents=True,exist_ok=True)
    records = {}
    for role,body in [('driver',driver),('launcher',launcher),('reader',reader)]:
        path = args.outdir/NAMES[role]
        path.write_text(body)
        records[role] = dict(path=str(path),sha256=digest(body),bytes=len(body.encode()))
    # Prove the whole original optimization loop is retained as text.
    marker = '    def save_report():\n'
    if driver[driver.index(marker):] != parents['driver'][parents['driver'].index(marker):]:
        raise ValueError('The complete outer optimization and real-screen loop changed')
    records['derivation'] = dict(parent_sha256={role:value[1] for role,value in PARENTS.items()},
        complete_optimization_loop_byte_identical=True, scientific_computation_performed=False)
    (args.outdir/'entry-source-derivation.json').write_text(json.dumps(records,indent=2)+'\n')
    print(json.dumps(records,sort_keys=True))


if __name__ == '__main__':
    main()
