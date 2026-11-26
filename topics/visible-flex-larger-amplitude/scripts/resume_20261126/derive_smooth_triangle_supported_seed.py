#!/usr/bin/env python3
"""Pure source construction of the independent R711 complete seed entry.

Only stdlib text/AST/hash operations occur here.  This does not import or run
any numerical operator, quadrature, root, field, Jacobian, or factorization.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path
import re


SOURCES = (
    ('supported_unit_seed_mean_jets.py',
     'bd9c0761e101679b10ff52d50f27a3dfb964687130c59878d756389b304ee771'),
    ('supported_unit_meridian_reference.py',
     '30ea80ec0673f3bdff3e59b97dfb5f7166a296aeb4b989fbca18b2feb5e9544c'),
    ('so3_supported_unit_meridian_operator.py',
     'e1bb7303540b1e807176ca5e71dcb2798b3f1e4e34909cd207cea300a9d4ebc0'),
    ('supported_unit_literal_zero_moment_input.py',
     '9fecbe018442be23d0c36d139ebb6ba3574b550aed76ef89cdcadd279770b0d6'),
    ('so3_supported_unit_normal_lift_operator.py',
     '5297192216356970140585eb9e56c521d9f35453211fb5a76086b713350eaa67'),
    ('so3_supported_unit_normal_lift_geometry.py',
     'd84b540d21622d4d609efa5ea85fef432a2dcebb51bea0f3c7c24376294918f4'),
    ('fullclosed_supported_unit_normal_lift_so3_qp.py',
     'e482428ee68aefa23da5b3b5c0a6b3363f047b0457f67a9193044ef151caec35'),
    ('launch_supported_unit_normal_lift_so3_actions.py',
     'fa468e7bbe58daa8aba0b6403b81468c7e8ed399028c19b1a2c71d47be87919b'),
    ('read_supported_unit_normal_lift_so3_report.py',
     'd788f4f07559b9375247874abbd57ec7d493a1cb4f543b8ab9f31f8dab3d128b'),
)


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def replace(text, old, new, count=None):
    found = text.count(old)
    if found == 0 or (count is not None and found != count):
        raise ValueError(('unexpected source replacement count', old, found, count))
    return text.replace(old, new)


def replace_function(text, name, new):
    lines = text.splitlines(keepends=True)
    matches = [node for node in ast.walk(ast.parse(text))
               if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
               and node.name == name]
    if len(matches) != 1:
        raise ValueError(('ambiguous function', name, len(matches)))
    node = matches[0]
    return ''.join(lines[:node.lineno-1])+new.rstrip()+'\n'+''.join(lines[node.end_lineno:])


PROFILE_VALUE = '''def smooth_triangle_value_and_derivative(t, profile_delta):
    """R711 full twelve-piece h and its normalized-coordinate derivative.

    All points use the same actual binary64 expression in the moment rule and
    reference provider.  Exact-domain/carrier/trigonometric errors are not
    silently zero; this routine returns working values only.
    """
    t = np.asarray(t, dtype=np.float64)
    delta = float(profile_delta)
    if (not np.isfinite(t).all() or np.any(t < 0.0) or np.any(t > 1.0)
            or not math.isfinite(delta) or not 0.0 < delta < 0.125):
        raise ValueError('Use the complete [0,1] query and a positive delta below 1/8')
    a = 0.25
    c = a-delta
    x = np.empty_like(t)
    sign = np.empty_like(t)
    orientation = np.empty_like(t)
    quarters = (t < a, (t >= a) & (t < 2*a),
                (t >= 2*a) & (t < 3*a), t >= 3*a)
    x[quarters[0]], sign[quarters[0]], orientation[quarters[0]] = t[quarters[0]], 1., 1.
    x[quarters[1]], sign[quarters[1]], orientation[quarters[1]] = 2*a-t[quarters[1]], 1., -1.
    x[quarters[2]], sign[quarters[2]], orientation[quarters[2]] = t[quarters[2]]-2*a, -1., 1.
    x[quarters[3]], sign[quarters[3]], orientation[quarters[3]] = 4*a-t[quarters[3]], -1., -1.
    first = x < delta
    middle = (x >= delta) & (x < a-delta)
    last = x >= a-delta
    H, g = np.empty_like(t), np.empty_like(t)

    def I5(u):
        return u*u*u*u*(2.5+u*(-3.+u))

    def S5(u):
        return u*u*u*(10.+u*(-15.+6.*u))

    u = x[first]/delta
    H[first], g[first] = delta*I5(u)/c, S5(u)
    H[middle], g[middle] = (x[middle]-delta/2.)/c, 1.
    u = (a-x[last])/delta
    H[last], g[last] = 1.-delta*I5(u)/c, S5(u)
    return sign*H, sign*orientation*g/c
'''

PROFILE_RULE = '''def _twelve_piece_profile(profile_delta, order):
    """All twelve R711 polynomial pieces; positive unnormalised Gauss weights."""
    try:
        exact = (profile_delta if isinstance(profile_delta, Fraction)
                 else Fraction.from_float(float(profile_delta))
                 if isinstance(profile_delta, (float, np.floating))
                 else Fraction(profile_delta))
    except (ValueError, TypeError, OverflowError, ZeroDivisionError) as error:
        _fail('input', 'Invalid exact profile delta: '+str(error))
    if not Fraction(0) < exact < Fraction(1, 8):
        _fail('input', 'Use one declared common exact profile delta in (0,1/8)')
    delta = float(exact)
    if not math.isfinite(delta) or not 0. < delta < .125:
        _fail('input', 'Exact profile delta has no usable positive working carrier')
    x, w = np.polynomial.legendre.leggauss(order)
    local, base_weights = (x+1.)/2., w/2.
    a = Fraction(1, 4)
    exact_edges = [Fraction(0)]
    for quarter in range(4):
        left, right = quarter*a, (quarter+1)*a
        exact_edges.extend((left+exact, right-exact, right))
    edges = np.asarray([float(v) for v in exact_edges], dtype=np.float64)
    widths = np.diff(edges)
    if not np.all(np.isfinite(widths) & (widths > 0.)):
        _fail('profile_quadrature', 'Some actual twelve-piece profile width is not positive',
              carriers={'edges': edges, 'widths': widths})
    nodes = np.concatenate([edges[j]+widths[j]*local for j in range(12)])
    weights = np.concatenate([widths[j]*base_weights for j in range(12)])
    profile, profile_derivative = smooth_triangle_value_and_derivative(nodes, exact)
    if (not np.isfinite(nodes).all() or not np.isfinite(profile).all()
            or not np.isfinite(profile_derivative).all()
            or not np.all(np.isfinite(weights) & (weights > 0.))):
        _fail('profile_quadrature', 'Actual complete profile rule is invalid',
              carriers={'nodes': nodes, 'weights': weights, 'profile': profile})
    record = dict(
        exact_profile_delta=str(exact), working_profile_delta_hex=delta.hex(),
        exact_piece_edges=[str(v) for v in exact_edges],
        working_piece_edges_hex=[float(v).hex() for v in edges],
        quadrature_order_per_piece=order, complete_piece_count=12,
        actual_node_count=len(nodes), actual_weight_sum=float(np.sum(weights)),
        actual_weight_sum_hex=float(np.sum(weights)).hex(),
        weights_not_renormalized=True, profile_values_not_clipped=True,
        complete_rule_not_reduced_to_one_quarter=True,
        nodes=_array_identity(nodes), weights=_array_identity(weights),
        profile=_array_identity(profile),
        profile_derivative=_array_identity(profile_derivative),
        mathematical_amplitude_interval='(0,pi)',
        mathematical_moment_at_pi_is_zero=True,
        working_moment_at_pi_evaluated_not_forced=True,
        exact_integral_error_enclosed=False)
    return nodes, weights, profile, record
'''

PROVIDER_PROFILE = '''def _profile(t, profile_delta, kernel):
    """Use the same full R711 evaluator as the bound complete mean rule."""
    return kernel.smooth_triangle_value_and_derivative(t, profile_delta)
'''


def top_function_ast(text):
    tree = ast.parse(text)
    answer = {}

    def visit(nodes, scope=()):
        for node in nodes:
            if isinstance(node, ast.ClassDef):
                visit(node.body, scope+(node.name,))
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                key = '.'.join(scope+(node.name,))
                if key in answer:
                    raise ValueError(('duplicate qualified function', key))
                answer[key] = ast.dump(node, include_attributes=False)
                visit(node.body, scope+(node.name,))
    visit(tree.body)
    return answer


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--outdir', type=Path, required=True)
    args = parser.parse_args()
    source_root = args.repo.resolve()/'topics/visible-flex-larger-amplitude/scripts/resume_20261126'
    here = args.outdir.resolve()
    if here == args.repo.resolve() or args.repo.resolve() in here.parents:
        raise ValueError('Pure derived output must remain outside the repository')
    here.mkdir(parents=True, exist_ok=True)
    sources = tuple((source_root/name, expected) for name, expected in SOURCES)
    old_text = {}
    name_map = {}
    for path, expected in sources:
        text = path.read_text()
        if digest(text) != expected:
            raise ValueError(('complete base source changed', str(path)))
        old_text[path.name] = text
        name_map[path.name] = path.name.replace('supported_unit_', 'supported_smooth_triangle_')
    pins = {}
    records = []
    outputs = {}
    for path, old_sha in sources:
        text = old_text[path.name]
        # Whole independent source and field identities; generic metadata keys
        # remain supported_unit_seed because the object is still a unit seed.
        for old_name, new_name in name_map.items():
            text = text.replace(old_name, new_name)
        text = text.replace('supported-unit', 'supported-smooth-triangle')
        text = text.replace('profile_epsilon', 'profile_delta')
        text = text.replace('profile-epsilon', 'profile-delta')
        text = text.replace('all_five_profile_pieces_used', 'all_twelve_profile_pieces_used')
        for old_pin, new_pin in pins.items():
            text = text.replace(old_pin, new_pin)

        if path.name == 'supported_unit_seed_mean_jets.py':
            text = re.sub(r'\bepsilon\b', 'profile_delta', text)
            text = text.replace('a_epsilon(lambda)', 'a_delta(lambda)')
            text = replace_function(text, '_five_piece_profile', PROFILE_VALUE+'\n\n'+PROFILE_RULE)
            text = replace(text, '_five_piece_profile(profile_delta, order)',
                           '_twelve_piece_profile(profile_delta, order)', 1)
            text = replace(text, 'half_pi = math.pi/2.0', 'full_pi = math.pi', 1)
            text = text.replace('half_pi', 'full_pi')
            text = replace(text, 'original open bracket', 'new complete (0,pi) working bracket', 1)
            text = text.replace('a_at_full_pi', 'a_at_pi')
            text = replace(text,
                '        central_transverse_mean_is_zero_by_exact_odd_profile_definition=True,',
                '        complete_R711_positive_radius_amplitude_interval=True,\n'
                '        previous_five_piece_or_monotone_height_certificate_inherited=False,\n'
                '        central_transverse_mean_is_zero_by_exact_odd_profile_definition=True,', 1)

        elif path.name == 'supported_unit_meridian_reference.py':
            text = re.sub(r'\bepsilon\b', 'profile_delta', text)
            text = replace(text, 'profile_delta: str = "1/10"', 'profile_delta: str = "1/128"', 1)
            text = text.replace('five-piece', 'twelve-piece smooth-triangle')
            text = text.replace('all five exact profile pieces', 'all twelve exact profile pieces')
            text = text.replace('"profile profile_delta"', '"smooth-triangle profile delta"')
            text = text.replace('a_epsilon(lambda)', 'a_delta(lambda)')
            text = text.replace('h_epsilon with two constant platforms',
                                'h_delta with four reflected smooth ramps and no constant nonzero phase platform')
            text = text.replace('The exact definition is R708/R709:',
                                'The exact definition is R708/R709 with the independent R711 central profile:')
            text = replace_function(text, '_profile', PROVIDER_PROFILE)
            text = replace(text, '_profile(np.array([t]), self.profile_delta)',
                           '_profile(np.array([t]), self.profile_delta, self.kernel)', 1)
            text = replace(text,
                'or sha(mean_kernel_module.solve_mean_jets.__code__.co_filename) != MEAN_KERNEL_SHA):',
                'or sha(mean_kernel_module.solve_mean_jets.__code__.co_filename) != MEAN_KERNEL_SHA\n'
                '                or sha(mean_kernel_module.smooth_triangle_value_and_derivative.__code__.co_filename) != MEAN_KERNEL_SHA):', 1)
            text = replace(text, '            exact_profile_delta=str(profile_delta),',
                '            exact_profile_delta=str(profile_delta),\n'
                '            mathematical_amplitude_interval="(0,pi)",\n'
                '            mathematical_profile_piece_count=12,\n'
                '            old_five_piece_working_cache_or_geometry_inherited=False,', 1)
            text = replace(text,
                '            central_profile="the full C2 twelve-piece smooth-triangle odd h_delta with four reflected smooth ramps and no constant nonzero phase platform",',
                '            central_profile="R711 full C3 twelve-piece odd smooth-triangle h_delta; quarter primitive of S5-flat-S5 velocity",', 1)

        elif path.name == 'so3_supported_unit_normal_lift_operator.py':
            text = replace(text,
                'supported_unit_implementation_derived_from_normal_source_sha256=DERIVED_FROM_COMPLETE_NORMAL_SOURCE_SHA256,',
                'supported_unit_implementation_derived_from_normal_source_sha256=DERIVED_FROM_COMPLETE_NORMAL_SOURCE_SHA256,\n'
                '            previous_supported_seed_normal_source_sha256="'+old_sha+'",\n'
                '            normal_frame_create_graph_matches_outer_grad_enabled=True,\n'
                '            active_full_parameter_J_and_transpose_graph_retained=True,', 1)
            start = text.index('    def _normal_frame_jets(')
            end = text.index('\n    def ', start+5)
            segment = text[start:end]
            if 'enabled = torch.is_grad_enabled()' not in segment:
                raise ValueError('The source does not have the already reviewed enabled value')
            segment = replace(segment, 'create_graph=True, retain_graph=True, allow_unused=False',
                              'create_graph=enabled, retain_graph=True, allow_unused=False', 1)
            text = text[:start]+segment+text[end:]
            text = replace(text, '            normal_count_scope=',
                '            normal_frame_create_graph_matches_outer_grad_enabled=True,\n'
                '            active_full_parameter_J_and_transpose_graph_retained=True,\n'
                '            normal_count_scope=', 1)
            text = replace(text, 'retained-graph frame reverse products',
                           'frame reverse products with create_graph matching outer grad mode', 1)

        elif path.name in ('fullclosed_supported_unit_normal_lift_so3_qp.py',
                           'launch_supported_unit_normal_lift_so3_actions.py'):
            text = replace(text, "p.add_argument('--seed-profile-delta', default='1/10')",
                           "p.add_argument('--seed-profile-delta', default='1/128')", 1)
            text = replace(text, 'boundary, epsilon =', 'boundary, profile_delta =', 1)
            text = replace(text, 'str(epsilon)', 'str(profile_delta)', 1)
            text = replace(text, '0 < epsilon <', '0 < profile_delta <', 1)

        elif path.name == 'supported_unit_literal_zero_moment_input.py':
            text = text.replace('fixed seed profile epsilon', 'fixed seed smooth-triangle profile delta')
            text = replace(text,
                "    _positive_exact_fraction(seed.get('exact_profile_delta'), 'fixed seed smooth-triangle profile delta')",
                "    profile_delta = _positive_exact_fraction(seed.get('exact_profile_delta'), 'fixed seed smooth-triangle profile delta')\n"
                "    if (profile_delta >= Fraction(1, 8)\n"
                "            or seed.get('mathematical_profile_piece_count') != 12\n"
                "            or seed.get('mathematical_amplitude_interval') != '(0,pi)'\n"
                "            or seed.get('old_five_piece_working_cache_or_geometry_inherited') is not False):\n"
                "        raise ValueError('Bind the full independent R711 profile and its declared amplitude interval')", 1)

        elif path.name == 'read_supported_unit_normal_lift_so3_report.py':
            text = replace(text,
                "                or metadata.get('schema') != 'complete-supported-smooth-triangle-seed-working-newton-mean-and-angular-jets-v1'",
                "                or metadata.get('schema') != 'complete-supported-smooth-triangle-seed-working-newton-mean-and-angular-jets-v1'", 1)

        # No root/field is executed here.  Both parse and compiler consume text.
        parsed = ast.parse(text, filename=name_map[path.name])
        compile(parsed, name_map[path.name], 'exec')
        if any(line.rstrip() != line for line in text.splitlines()):
            raise ValueError(('trailing whitespace', path.name))
        output = here/name_map[path.name]
        output.write_text(text)
        new_sha = digest(text)
        pins[old_sha] = new_sha
        outputs[path.name] = text
        old_functions, new_functions = top_function_ast(old_text[path.name]), top_function_ast(text)
        common = sorted(set(old_functions) & set(new_functions))
        records.append(dict(
            source_path=str(output), bytes=len(text.encode()), sha256=new_sha,
            exact_parent_path=str(path), exact_parent_sha256=old_sha,
            same_function_AST=[key for key in common if old_functions[key] == new_functions[key]],
            changed_function_AST=[key for key in common if old_functions[key] != new_functions[key]],
            new_function_AST=sorted(set(new_functions)-set(old_functions)),
            removed_function_AST=sorted(set(old_functions)-set(new_functions))))
    driver_old = old_text['fullclosed_supported_unit_normal_lift_so3_qp.py']
    driver_new = outputs['fullclosed_supported_unit_normal_lift_so3_qp.py']
    marker = '    def save_report():'
    if driver_old[driver_old.index(marker):] != driver_new[driver_new.index(marker):]:
        raise ValueError('The complete actual solver loop changed')
    geo_old = old_text['so3_supported_unit_normal_lift_geometry.py']
    geo_new = outputs['so3_supported_unit_normal_lift_geometry.py']
    marker = '    def _set_x('
    if geo_old[geo_old.index(marker):] != geo_new[geo_new.index(marker):]:
        raise ValueError('The complete original geometry/row/scan body changed')
    review = dict(
        schema='pure-source-R711-supported-seed-complete-derivation-v1',
        scientific_execution=False, imported_scientific_modules=False,
        complete_parent_source_hashes_checked=True,
        complete_original_solver_suffix_byte_equal=True,
        complete_original_geometry_suffix_byte_equal=True,
        source_records=records)
    (here/'source-derivation-review.json').write_text(json.dumps(review, indent=2)+'\n')
    print(json.dumps(review, indent=2))


if __name__ == '__main__':
    main()
