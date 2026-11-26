#!/usr/bin/env python3
"""Pure-source derivation of the complete gamma-KKT geometry adapter.

This script reads text, hashes source bytes, compares ASTs and writes the full
independent source.  It never imports or executes a scientific source or reads
any candidate array.  A draft pin deliberately cannot match a real operator.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path

PARENT_SHA256 = 'e4a3271d829a1fc52080b0ac1bdb719f5a13065f23223e64288c77ea6bbc514c'
OPERATOR_SCHEMA = 'complete-direct-R690-SO3-added-gamma-six-control-KKT-zero-layer-v1'
GEOMETRY_SCHEMA = 'complete-added-gamma-six-control-KKT-zero-SO3-world-geometry-and-original-192-amplitude-rows-v1'
OUTPUT_NAME = 'so3_zero_gamma_kkt_geometry.py'
DRAFT_PIN = '__UNLOCKED_GAMMA_KKT_OPERATOR_SOURCE__'


def digest(value):
    return hashlib.sha256(value).hexdigest()


def replace_once(source, old, new):
    if source.count(old) != 1:
        raise ValueError('A complete parent source anchor is not unique: '+old[:100])
    return source.replace(old, new, 1)


def definitions(source):
    result = {}
    def walk(body, prefix=''):
        for node in body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                name = prefix+node.name
                result[name] = ast.dump(node, include_attributes=False)
                if isinstance(node, ast.ClassDef):
                    walk(node.body, name+'.')
    walk(ast.parse(source).body)
    return result


def pin_from_source(path, expected):
    data = path.read_bytes()
    actual = digest(data)
    if actual != expected:
        raise ValueError('The separately locked complete KKT operator bytes differ')
    tree = ast.parse(data.decode())
    schemas = [ast.literal_eval(node.value) for node in tree.body
        if isinstance(node, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == 'SCHEMA' for t in node.targets)]
    if schemas != [OPERATOR_SCHEMA]:
        raise ValueError('The actual new operator declares a different schema')
    classes = [node for node in tree.body
               if isinstance(node, ast.ClassDef) and node.name == 'ZeroClosureOperator']
    if len(classes) != 1:
        raise ValueError('Need the actual complete independent ZeroClosureOperator class')
    methods = {node.name for node in classes[0].body if isinstance(node, ast.FunctionDef)}
    required = {'grid_fields', 'point_fields', 'point_vjp', 'prepare', 'domain',
                'fields_torch', '_constraints', '_implicit_jet_value'}
    if not required <= methods:
        raise ValueError('The complete new operator must own all physical and implicit entry methods')
    return actual


def derive(parent, operator_sha256):
    child = replace_once(parent,
        '"""Independent frozen-moment-Q zero geometry and complete selected rows.',
        '"""Independent added-gamma six-control KKT geometry and complete selected rows.')
    child = replace_once(child,
        'The physical field is the NEW closed unit-meridian representation, evaluated',
        'The physical field is the NEW six-control KKT closed unit-meridian representation, evaluated')
    child = replace_once(child,
        "SCHEMA = 'complete-frozen-moment-Q-zero-SO3-world-geometry-and-original-192-amplitude-rows-v1'",
        'SCHEMA = '+repr(GEOMETRY_SCHEMA))
    child = replace_once(child,
        "OPERATOR_SCHEMA = 'complete-direct-R690-SO3-frozen-moment-Q-zero-endpoint-layer-v1'",
        'OPERATOR_SCHEMA = '+repr(OPERATOR_SCHEMA))
    child = replace_once(child,
        "ENDPOINT_SOURCE_SHA256 = '44ac53f1fcecceae55ed3b3230e1925292ce76ced85dc75f08e15ff0b70f5e4e'",
        'ENDPOINT_SOURCE_SHA256 = '+repr(operator_sha256))
    child = replace_once(child,
        "DERIVED_FROM_COMPLETE_GEOMETRY_SHA256 = '7698fd89e1b739391e2139c6c88dacd0c3b3d8be614fd65e435508420326b385'",
        'DERIVED_FROM_COMPLETE_GEOMETRY_SHA256 = '+repr(PARENT_SHA256))
    child = replace_once(child,
        "            raise ValueError('Use the complete independent zero-closure field and its full implicit first derivatives')\n        frozen = model.get('frozen_moment_Q_definition')",
        """            raise ValueError('Use the complete independent gamma-KKT field and its full 9/18/27 implicit derivatives')
        if (model.get('implicit_control_dimension') != 6
                or model.get('KKT_dimension') != 9
                or model.get('complete_second_angular_implicit_dimension') != 27
                or model.get('implicit_control_cost') != '(|z/S|^2+|v|^2)/2'
                or model.get('selected_KKT_stationary_branch') is not True
                or model.get('SOSC_verified') is not False
                or model.get('global_minimum_verified') is not False):
            raise ValueError('Keep the complete six-control stationary KKT contract; no implicit variables may be dropped')
        gamma_nodes = tuple(Fraction(value) for value in problem.gamma_nodes)
        gamma_words = [str(value) for value in gamma_nodes]
        if (len(gamma_nodes) != 3 or not 0 < gamma_nodes[0] < gamma_nodes[1] < gamma_nodes[2] < 1
                or model.get('exact_relative_gamma_nodes') != gamma_words):
            raise ValueError('The actual fixed relative gamma input differs from the complete mathematical model')
        frozen = model.get('frozen_moment_Q_definition')""")
    child = replace_once(child,
        "                or frozen.get('schema') != 'literal-two-bubble-endpoint-Q-v1'",
        "                or frozen.get('schema') not in ('literal-two-bubble-endpoint-Q-v1', 'new-reference-literal-two-bubble-endpoint-Q-v1')")
    child = replace_once(child,
        "        self.operator_sha256 = model['source_sha256']",
        """        new_literal_input = frozen['schema'] == 'new-reference-literal-two-bubble-endpoint-Q-v1'
        literal_input_schema = model.get('literal_Q_input_schema')
        literal_binder_sha = model.get('new_reference_input_binding_source_sha256')
        if new_literal_input:
            if (literal_input_schema != 'new-reference-literal-zero-endpoint-Q-input-v1'
                    or not isinstance(literal_binder_sha, str) or len(literal_binder_sha) != 64
                    or any(ch not in '0123456789abcdef' for ch in literal_binder_sha)):
                raise ValueError('The new-reference literal input must declare its actual independently bound producer source')
            expected_keys = {'schema', 'Q0_binary64_hex', 'exact_relative_bubble_nodes',
                'fixed_scalar_metric_identity_sha256', 'fixed_scalar_profile_definition',
                'initial_reference_bundle_sha256', 'initial_reference_model_identity_sha256',
                'base_model_identity_sha256', 'initial_full_point_sha256', 'fixed_chart_core_sha256'}
            if (set(frozen) != expected_keys
                    or frozen['fixed_scalar_metric_identity_sha256'] != problem.context.scalar_identity
                    or frozen['fixed_scalar_profile_definition'] != problem.context.scalar_definition
                    or canonical(frozen['fixed_scalar_profile_definition']) != problem.context.scalar_identity
                    or frozen['base_model_identity_sha256'] != problem.base.identity
                    or frozen['initial_reference_bundle_sha256'] != base['initial_reference_bundle_sha256']
                    or frozen['initial_reference_bundle_sha256'] != problem.context.input_records['reference_bundle']['sha256']
                    or frozen['initial_reference_model_identity_sha256'] != base['initial_reference_model_identity_sha256']
                    or frozen['initial_reference_model_identity_sha256'] != problem.context.identity
                    or frozen['fixed_chart_core_sha256'] != base['fixed_chart_core_sha256']
                    or frozen['fixed_chart_core_sha256'] != array_sha(problem.parent_core)
                    or frozen['initial_full_point_sha256'] != array_sha(problem.base.initial())
                    or frozen['exact_relative_bubble_nodes'] != [[str(Fraction(v)) for v in row]
                                                                for row in problem.bubble_nodes]):
                raise ValueError('The new literal Q must bind this actual complete reference, profile, chart and original full initial point')
        elif (literal_input_schema != 'frozen-zero-endpoint-moment-Q-input-v1'
                or literal_binder_sha is not None):
            raise ValueError('The original actual-moment input must retain its own exact schema and binding path')
        self.operator_sha256 = model['source_sha256']""")
    child = replace_once(child,
        "            frozen_moment_Q_trace_report_sha256=frozen['trace_report_sha256'],\n            numerical_moment_inverse_not_a_continuous_root_certificate=True,",
        """            frozen_moment_Q_definition_schema=frozen['schema'],
            literal_Q_input_schema=literal_input_schema,
            new_reference_input_binding_source_sha256=literal_binder_sha,
            frozen_Q_binding_kind=('explicit-literal-parameters-for-new-reference' if new_literal_input
                                   else 'actual-historical-working-moment-input'),
            frozen_moment_Q_trace_report_sha256=(None if new_literal_input else frozen['trace_report_sha256']),
            current_reference_Q_is_newly_bound_literal_input=new_literal_input,
            new_reference_same_mathematical_g_claimed=(False if new_literal_input else None),
            current_working_moment_inverse_claimed=False,
            historical_trace_is_only_provenance_for_new_literal_input=new_literal_input,
            exact_relative_gamma_nodes=gamma_words,
            implicit_control_dimension=6, KKT_dimension=9,
            complete_second_angular_implicit_dimension=27,
            implicit_control_cost=model['implicit_control_cost'],
            internal_KKT_unknowns_are_not_added_to_outer_free_point=True,
            all_original_free_point_coordinates_retained=True,
            selected_KKT_stationary_branch=True,
            SOSC_verified=False, global_minimum_verified=False,
            KKT_source_includes_full_multiplier_constraint_Hessian=True,
            numerical_moment_inverse_not_a_continuous_root_certificate=True,""")
    child = replace_once(child,
        "            physical_pullback='actual new SO3 point_vjp in world coordinates',",
        "            physical_pullback='actual new gamma-KKT SO3 point_vjp in world coordinates, through all 27 implicit control/multiplier jet slots',")
    child = replace_once(child,
        "            quarter_completion='declared literal moment-Q sparse reflection/half-turn covariance and fixed-chart equivariant branch; actual roots start at zero, both witness signs are read, continuous root existence remains unpaid',",
        "            quarter_completion='declared polar-z/axial-v literal-Q/gamma reflection and half-turn covariance; the chosen consistent KKT branch and axis jets remain a continuous responsibility, both witness signs are actually read',")
    parent_tail = parent[parent.index('    def _set_x'):]
    child_tail = child[child.index('    def _set_x'):]
    if parent_tail != child_tail:
        raise ArithmeticError('No complete physical screen, row, amplitude or permanent-memory method may change')
    old, new = definitions(parent), definitions(child)
    if set(old) != set(new):
        raise ArithmeticError('No parent definition may be deleted or silently added')
    allowed = {'GeometryScreen', 'GeometryScreen.__init__'}
    changed = sorted(name for name in old if old[name] != new[name])
    if set(changed) != allowed:
        raise ArithmeticError('Only the complete GeometryScreen constructor may have a different body')
    tree = ast.parse(child)
    for node in ast.walk(tree):
        if isinstance(node, ast.Dict):
            keys = [key.value for key in node.keys if isinstance(key, ast.Constant)]
            if len(keys) != len(set(keys)):
                raise ArithmeticError('Duplicate literal dictionary key')
        if isinstance(node, ast.Call):
            names = [keyword.arg for keyword in node.keywords if keyword.arg is not None]
            if len(names) != len(set(names)):
                raise ArithmeticError('Duplicate named keyword')
    compile(child, OUTPUT_NAME, 'exec')
    if any(line.rstrip() != line for line in child.splitlines()):
        raise ArithmeticError('Unexpected trailing whitespace')
    return child, dict(
        all_physical_geometry_methods_from_set_x_through_eof_byte_identical=True,
        unchanged_physical_method_suffix_sha256=digest(parent_tail.encode()),
        all_top_level_helpers_and_budget_methods_AST_identical=True,
        actual_changed_AST_definitions=changed,
        scientific_execution_performed=False,
        input_arrays_read=False,
        source_AST_and_compile_verified=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--parent-source', type=Path, required=True)
    parser.add_argument('--outdir', type=Path, required=True)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--operator-source', type=Path)
    group.add_argument('--draft-unlocked', action='store_true')
    parser.add_argument('--operator-sha256')
    args = parser.parse_args()
    raw = args.parent_source.read_bytes()
    if digest(raw) != PARENT_SHA256:
        raise ValueError('Bind the complete unchanged e4a3 parent geometry source')
    if args.draft_unlocked:
        if args.operator_sha256 is not None:
            raise ValueError('A draft cannot declare a locked operator hash')
        operator_pin = DRAFT_PIN
    else:
        if args.operator_sha256 is None or len(args.operator_sha256) != 64:
            raise ValueError('Supply the independently locked actual complete operator SHA256')
        operator_pin = pin_from_source(args.operator_source, args.operator_sha256)
    child, verification = derive(raw.decode(), operator_pin)
    args.outdir.mkdir(parents=True, exist_ok=True)
    destination = args.outdir/OUTPUT_NAME
    destination.write_text(child)
    metadata = dict(
        schema='complete-gamma-KKT-geometry-pure-source-derivation-v1',
        derivation_source_sha256=digest(Path(__file__).read_bytes()),
        parent_complete_source_sha256=PARENT_SHA256,
        operator_source_sha256=operator_pin,
        operator_schema=OPERATOR_SCHEMA,
        output_schema=GEOMETRY_SCHEMA,
        output_name=OUTPUT_NAME,
        output_sha256=digest(destination.read_bytes()),
        output_bytes=destination.stat().st_size,
        draft_unlocked=bool(args.draft_unlocked),
        executable_locked_scientific_source=not bool(args.draft_unlocked),
        verification=verification)
    (args.outdir/'source-derivation.json').write_text(json.dumps(metadata,indent=2,sort_keys=True)+'\n')
    print(json.dumps(metadata, sort_keys=True))


if __name__ == '__main__':
    main()
