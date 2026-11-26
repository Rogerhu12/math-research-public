#!/usr/bin/env python3
"""Pure full-body derivation of fixed literal moment-Q zero SO3 entries."""
import argparse
import ast
import hashlib
from pathlib import Path
import pprint

OLD_DRIVER = 'b4d71ade8082d99dfef6eefc0e26aed83eeda507aa2e9656864bf2c596977d4b'
OLD_LAUNCHER = '27414140270a0fb1a9533a21a0bd28a46988c55aecd9952c38e7c05512b64166'
OLD_READER = 'b25e5a5f370e69fe8164d835a608b1845db926d2488939dc9bafaa3bba0a6857'
OPERATOR = '44ac53f1fcecceae55ed3b3230e1925292ce76ced85dc75f08e15ff0b70f5e4e'
GEOMETRY = 'e4a3271d829a1fc52080b0ac1bdb719f5a13065f23223e64288c77ea6bbc514c'
BINDER = '4dc3e1a8ba8f128e1d05176f4d0f4b18c62d278fed603cc46f7ed686f6e4e611'
SCHEMA = 'complete-independent-axisymmetric-fixed-deep-frozen-moment-Q-zero-SO3-QP-v1'

ARGUMENTS = """    moment_choice = p.add_mutually_exclusive_group(required=True)
    moment_choice.add_argument('--moment-trace-report', type=Path)
    moment_choice.add_argument('--moment-input', type=Path)
    p.add_argument('--moment-trace-report-sha256')
    p.add_argument('--moment-failed-report', type=Path)
    p.add_argument('--moment-input-sha256')
    p.add_argument('--moment-definition-sha256')
"""
VALIDATION = """    if a.moment_trace_report is not None:
        if a.moment_failed_report is None or a.moment_trace_report_sha256 is None or a.moment_input_sha256 is not None:
            raise ValueError('The actual-trace route needs its complete recorded failure and trace SHA; no small-file SHA is mixed in')
    elif (a.moment_input_sha256 is None or a.moment_definition_sha256 is None
            or a.moment_trace_report_sha256 is not None or a.moment_failed_report is not None):
        raise ValueError('The small fixed-parameter route needs its file SHA and the SAME complete definition identity')
    for digest in (a.moment_trace_report_sha256, a.moment_input_sha256, a.moment_definition_sha256):
        if digest is not None and (len(digest) != 64 or any(c not in '0123456789abcdef' for c in digest)):
            raise ValueError('Use complete explicit SHA256 input identities')
"""
LOAD_INPUT = """    if args.moment_trace_report is not None:
        frozen_moment_input = moment_binding.from_trace(args.repo, args.moment_trace_report,
            trace_report_sha256=args.moment_trace_report_sha256,
            failed_report=args.moment_failed_report,
            expected_definition_identity_sha256=args.moment_definition_sha256)
        moment_input_record = dict(mode='one-time exact actual trace word extraction',
            actual_trace_report=file_record(args.moment_trace_report),
            actual_failed_report=file_record(args.moment_failed_report),
            no_moment_or_inverse_recomputed=True)
    else:
        frozen_moment_input = moment_binding.from_parameter_file(args.moment_input,
            input_sha256=args.moment_input_sha256,
            expected_definition_identity_sha256=args.moment_definition_sha256)
        moment_input_record = dict(mode='same complete published eighteen-parameter definition',
            actual_parameter_file=file_record(args.moment_input),
            no_moment_or_inverse_recomputed=True)
    moment_definition_identity = moment_binding.bind_to_base(frozen_moment_input,
        base_model=base.model, initial_reference_bundle_sha256=sha(args.reference_bundle),
        fixed_scalar_metric_identity_sha256=fixed_profile, bubble_nodes=bubble_nodes)
"""


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def read(path, expected):
    text = Path(path).read_text()
    if digest(text) != expected:
        raise ValueError('Bind the original entire source '+str(path))
    return text


def once(text, old, new):
    if text.count(old) != 1:
        raise ValueError('A complete literal replacement is not unique: '+old[:100])
    return text.replace(old, new, 1)


def set_assignment(text, name, value):
    nodes = [n for n in ast.parse(text).body if isinstance(n,ast.Assign)
        and any(isinstance(t,ast.Name) and t.id==name for t in n.targets)]
    if len(nodes) != 1:
        raise ValueError('One complete literal assignment required')
    node = nodes[0]
    lines = text.splitlines(keepends=True)
    return ''.join(lines[:node.lineno-1])+name+' = '+pprint.pformat(value,sort_dicts=False,width=110)+'\n'+''.join(lines[node.end_lineno:])


def validate(text, name):
    tree = ast.parse(text,filename=name)
    compile(tree,name,'exec')
    for node in ast.walk(tree):
        if isinstance(node,ast.Dict):
            keys = [k.value for k in node.keys if isinstance(k,ast.Constant) and isinstance(k.value,(str,int,float))]
            if len(keys) != len(set(keys)):
                raise ValueError('Duplicate literal key '+name)
    return tree


def common_parse_changes(text):
    text = once(text,"    p.add_argument('--seed-so3-report', type=Path)\n",
        "    p.add_argument('--seed-so3-report', type=Path)\n"+ARGUMENTS)
    text = once(text,"    a = p.parse_args()\n","    a = p.parse_args()\n"+VALIDATION)
    text = once(text,"                 'seed_so3_checkpoint', 'seed_so3_report'):",
        "                 'seed_so3_checkpoint', 'seed_so3_report', 'moment_trace_report',\n                 'moment_failed_report', 'moment_input'):")
    return text


def derive(args):
    original = read(args.original_driver,OLD_DRIVER)
    driver = original
    driver = once(driver,'"""Independent zero-closure SO(3) optimization of one fixed deep g.',
        '"""Independent frozen literal moment-Q zero-closure SO(3) optimization of one fixed deep g.')
    driver = set_assignment(driver,'SCHEMA',SCHEMA)
    pins = [ast.literal_eval(n.value) for n in ast.parse(driver).body if isinstance(n,ast.Assign)
        and any(isinstance(t,ast.Name) and t.id=='SOURCE_PINS' for t in n.targets)][0]
    pins['endpoint'] = ('scripts/resume_20261126/so3_zero_closure_moment_operator.py',OPERATOR)
    pins['geometry'] = ('scripts/resume_20261126/so3_zero_closure_moment_geometry.py',GEOMETRY)
    pins['frozen_moment_input'] = ('scripts/resume_20261126/frozen_zero_moment_input.py',BINDER)
    pins['moment_trace_source'] = ('scripts/resume_20261126/trace_zero_initial_endpoint_failure.py','73193414b094c05c9d8ce1dd033aab6a18446a88a5d7c4a6f352fcbcd966fb54')
    pins['moment_initial_binding'] = ('scripts/resume_20261126/diagnose_zero_initial_chord.py','65787b3e51f80505f5619c35fb05f8ad064e88de111578ff53e8bdad442092c0')
    pins['moment_original_endpoint'] = ('scripts/resume_20261126/so3_zero_closure_endpoint_operator.py','5b4c3921a0f56a9ac3acc12c03e788b3b648b15817b2e89e155a18feb2b24c46')
    pins['moment_original_driver'] = ('scripts/resume_20261126/fullclosed_zero_closure_so3_qp.py',OLD_DRIVER)
    driver = set_assignment(driver,'SOURCE_PINS',pins)
    driver = common_parse_changes(driver)
    driver = once(driver,"    endpoint = load('_so3_independent_zero_closure_endpoint', paths['endpoint'])\n",
        "    endpoint = load('_so3_independent_frozen_moment_zero_endpoint', paths['endpoint'])\n    moment_binding = load('_so3_complete_frozen_moment_input', paths['frozen_moment_input'])\n")
    driver = once(driver,"    q = endpoint.ZeroClosureOperator(base, expected_base_source_sha256=SOURCE_PINS['meridian'][1],\n",
        LOAD_INPUT+"    q = endpoint.ZeroClosureOperator(base, expected_base_source_sha256=SOURCE_PINS['meridian'][1],\n")
    driver = once(driver,"        bubble_nodes=bubble_nodes, endpoint_policy=root_policy)\n",
        "        bubble_nodes=bubble_nodes, frozen_moment_input=frozen_moment_input, endpoint_policy=root_policy)\n")
    driver = once(driver,"        representation=q.model, coordinate_norm=coordinates.record,\n",
        "        representation=q.model, coordinate_norm=coordinates.record,\n        frozen_moment_Q_input=frozen_moment_input,\n        frozen_moment_Q_definition_identity_sha256=moment_definition_identity,\n        frozen_moment_Q_input_record=moment_input_record,\n        moment_Q_recomputed_from_current_free_point=False,\n        old_zero_field_or_root_certificate_inherited=False,\n        changed_control_map_has_independent_model_identity=True,\n")
    driver = once(driver,"            endpoint_root_policy=root_policy.metadata(), exact_relative_bubble_nodes=q.model['exact_relative_bubble_nodes'],\n",
        "            endpoint_root_policy=root_policy.metadata(), exact_relative_bubble_nodes=q.model['exact_relative_bubble_nodes'],\n            fixed_moment_Q_definition_identity_sha256=moment_definition_identity,\n            old_endpoint_coordinate_ball_certificate_inherited=False,\n")
    marker = '    def save_report():\n'
    if driver[driver.index(marker):] != original[original.index(marker):]:
        raise ValueError('The entire actual original scientific main loop changed')
    a = {n.name:n for n in ast.parse(original).body if isinstance(n,(ast.FunctionDef,ast.ClassDef))}
    b = {n.name:n for n in validate(driver,'fullclosed_zero_moment_so3_qp.py').body if isinstance(n,(ast.FunctionDef,ast.ClassDef))}
    if a.keys()!=b.keys():
        raise ValueError('An original complete interface was removed')
    for name in a:
        if name not in ('main','parse_args') and ast.dump(a[name])!=ast.dump(b[name]):
            raise ValueError('An unchanged complete physical/Phase-I interface differs '+name)
    launcher = read(args.original_launcher,OLD_LAUNCHER)
    launcher = common_parse_changes(launcher)
    launcher = set_assignment(launcher,'DRIVER_SHA',digest(driver))
    launcher = once(launcher,"source/'fullclosed_zero_closure_so3_qp.py'","source/'fullclosed_zero_moment_so3_qp.py'")
    launcher = once(launcher,"        inputs.extend([args.seed_so3_checkpoint, args.seed_so3_report])\n",
        "        inputs.extend([args.seed_so3_checkpoint, args.seed_so3_report])\n    if args.moment_trace_report is not None:\n        inputs.extend([args.moment_trace_report, args.moment_failed_report])\n    else:\n        inputs.append(args.moment_input)\n")
    launcher = once(launcher,'public-actions-complete-independent-zero-closure-SO3-command-v1',
        'public-actions-complete-independent-frozen-moment-Q-zero-SO3-command-v1')
    validate(launcher,'launch_zero_moment_so3_actions.py')
    reader = read(args.original_reader,OLD_READER)
    reader = set_assignment(reader,'DRIVER_SHA',digest(driver))
    reader = set_assignment(reader,'REPORT_SCHEMA',SCHEMA)
    reader = once(reader,"import hashlib\n","import hashlib\nimport importlib.util\nimport sys\n")
    reader = once(reader,"scripts/resume_20261126/fullclosed_zero_closure_so3_qp.py",
        "scripts/resume_20261126/fullclosed_zero_moment_so3_qp.py")
    reader = once(reader,"    base = value['base_complete_metadata']\n",
        "    if (value.get('frozen_moment_Q_definition') != model['frozen_moment_Q_definition']\n            or value.get('frozen_moment_Q_definition_identity_sha256') != model['frozen_moment_Q_definition_identity_sha256']\n            or value.get('Q_input_recomputed_at_current_point') is not False\n            or value.get('actual_working_moment_inverse_is_not_a_continuous_certificate') is not True):\n        raise ValueError('The actual endpoint metadata changed its complete frozen literal control input')\n    base = value['base_complete_metadata']\n")
    reader = once(reader,"    working = report['working_evaluation']\n",
        """    binder_path = topic/'scripts/resume_20261126/frozen_zero_moment_input.py'
    if sha(binder_path) != roles['frozen_moment_input']:
        raise ValueError('The whole pure fixed input binder changed')
    spec = importlib.util.spec_from_file_location('_pure_actual_fixed_moment_input',binder_path)
    binder = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = binder
    spec.loader.exec_module(binder)
    frozen_input = report['frozen_moment_Q_input']
    moment_identity = binder.bind_to_base(frozen_input, base_model=base_model,
        initial_reference_bundle_sha256=report['bundle_sha256'],
        fixed_scalar_metric_identity_sha256=profile,
        bubble_nodes=model['exact_relative_bubble_nodes'])
    if (model.get('schema') != 'complete-direct-R690-SO3-frozen-moment-Q-zero-endpoint-layer-v1'
            or model.get('frozen_moment_Q_definition') != frozen_input['definition']
            or model.get('frozen_moment_Q_definition_identity_sha256') != moment_identity
            or report.get('frozen_moment_Q_definition_identity_sha256') != moment_identity
            or model.get('moment_Q_recomputed_from_current_field') is not False
            or model.get('moment_Q_is_an_exact_integral_inverse_claimed') is not False
            or report.get('moment_Q_recomputed_from_current_free_point') is not False
            or report.get('old_zero_field_or_root_certificate_inherited') is not False
            or model.get('original_implicit_root_algorithm_source_sha256') != roles['moment_original_endpoint']):
        raise ValueError('Do not replace, recompute or relabel the fixed moment-Q mathematical control input')
    working = report['working_evaluation']
    if (working.get('fixed_moment_Q_definition_identity_sha256') != moment_identity
            or working.get('old_endpoint_coordinate_ball_certificate_inherited') is not False):
        raise ValueError('The new coordinate ball has its own declared scope and no inherited old certificate')
""")
    reader = once(reader,"schema='actual-complete-independent-zero-closure-SO3-scalar-readout-v1'",
        "schema='actual-complete-independent-frozen-moment-Q-zero-SO3-scalar-readout-v1'")
    reader = once(reader,"        direct_base_seed=seed,\n",
        "        direct_base_seed=seed,\n        frozen_moment_Q_definition=frozen_input['definition'],\n        frozen_moment_Q_definition_identity_sha256=moment_identity,\n        frozen_moment_Q_input_provenance=frozen_input['provenance'],\n        frozen_moment_Q_input_record=report['frozen_moment_Q_input_record'],\n        moment_Q_recomputed_from_current_free_point=False,\n        old_zero_field_or_root_certificate_inherited=False,\n        old_endpoint_coordinate_ball_certificate_inherited=False,\n")
    reader = once(reader,"        actual_metric_directions=metrics, actual_restoration_directions=restoration,\n",
        "        actual_metric_directions=metrics, actual_restoration_directions=restoration,\n        actual_metric_direction_count=len(metrics), actual_restoration_direction_count=len(restoration),\n        actual_accepted_metric_direction_count=sum(bool(v['accepted']) for v in metrics),\n        actual_accepted_restoration_direction_count=sum(bool(v['accepted']) for v in restoration),\n")
    reader = once(reader,"        initial=initial, final=final,\n",
        "        initial=initial, final=final,\n        initial_Phi=None if initial is None else initial['Phi'],\n        final_Phi=None if final is None else final['Phi'],\n        initial_max_relative_gram=None if initial is None else initial['max_relative_gram'],\n        final_max_relative_gram=None if final is None else final['max_relative_gram'],\n        initial_maximum_physical_g=(report.get('initial_geometry') or {}).get('maximum_physical_g'),\n        final_maximum_physical_g=(report.get('final_geometry') or {}).get('maximum_physical_g'),\n        final_finite_geometry_passed=None if final_geometry is None else final_geometry['true_finite_geometry_feasible'],\n")
    validate(reader,'read_zero_moment_so3_report.py')
    outputs = {'fullclosed_zero_moment_so3_qp.py':driver,
        'launch_zero_moment_so3_actions.py':launcher,
        'read_zero_moment_so3_report.py':reader}
    args.outdir.mkdir(parents=True,exist_ok=True)
    for name,text in outputs.items():
        (args.outdir/name).write_text(text)
        print(name,len(text.encode()),digest(text))
    print('Original scientific loop byte-identical from save_report to EOF; pure source only; no numerical source imported.')


if __name__=='__main__':
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('original-driver','original-launcher','original-reader','outdir'):
        p.add_argument('--'+name,type=Path,required=True)
    derive(p.parse_args())
