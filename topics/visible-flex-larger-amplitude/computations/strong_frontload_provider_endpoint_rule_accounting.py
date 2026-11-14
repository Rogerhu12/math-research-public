#!/usr/bin/env python3
"""Separate actual provider quadrature-rule and endpoint arithmetic errors.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The stored angle-boost height uses one whole-segment Gauss64 rule, while its
radius uses the original ramp/plateau/ramp split.  This fresh consumer retains
the former r1 diagnostic and explicitly pays the difference between the two
height rules.  It certifies actual stored endpoints relative to a specified
analytic piecewise meridian, not a uniform floating-point implementation or
any accepted new surface.  No physical ODE, field, or Newton solve is run.
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import time
from flint import arb, ctx

HERE = Path(__file__).resolve().parent
PINS = {
    'strong_newg_binary_background_C2_comparison.py': '483b784c9c7aabde360aa04a06eea063b7dee8b1dadd0f0ae81f8be0d7f14e08',
    'strong_newg_gauss64_piecewise_C2_bridge.py': 'a830cdd1da8c4dc187b0ca4e27c0c67d4834c92b8539677f6ef32fbb93e60ea6',
    'alternative-neck-provider.py': '84ed048425c8b0f4deeec8af37828e318150cde5d59995da77f64d923591b9c2',
    'alternative-neck-flatturn.py': 'c0578ed401a2433c72ec99702c9c32a8412c66264a7fb81a8b8c74ba054fbbdd',
    'strong_angle_boost.py': 'ce2117cffe2e55d310eb0be219e7d22e750d97cd22704e75c3dd74a085c020be',
}
TABLE_SHA = '0a6bb86d0b492ba47ff5d34a4ef63419686aef316cacdec62ed1781f48da621d'
R1_SHA = '07672eff22ff35f7145a1e9dd34f7ec32d554122e79793f6bd17964b76cef2ab'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def rational(value):
    return F(value['numerator']) / F(value['denominator'])


def binary(value):
    return F.from_float(float(value))


def aq(value):
    value = F(value)
    return arb(value.numerator) / value.denominator


def dyadic(value):
    return F(int(value[0])) * F(2) ** int(value[1])


def bound(value, side):
    mantissa, exponent = getattr(arb(value), side)().man_exp()
    return [str(mantissa), int(exponent)]


def upper(value):
    return bound(value, 'upper')


def box(value):
    return [bound(value, 'lower'), upper(value)]


def bernstein(controls, u):
    row = list(controls)
    for count in range(len(row)-1, 0, -1):
        row = [(1-u)*row[j] + u*row[j+1] for j in range(count)]
    return row[0]


def module(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE/filename)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('background', 'background-resource', 'first-piece', 'table',
                 'previous-diagnostic', 'previous-resource', 'out'):
        parser.add_argument('--'+name, type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    ctx.prec = 256
    ctx.threads = 1
    if args.out.exists():
        raise FileExistsError(args.out)
    bg = read(args.background)
    owned = read(args.background_resource)
    first = read(args.first_piece)
    table = read(args.table)
    previous = read(args.previous_diagnostic)
    previous_owned = read(args.previous_resource)
    gates = {}

    def check(name, condition):
        if not condition:
            raise ArithmeticError(name)
        gates[name] = True

    check('completed_matching_unsolved_warm_background',
          bg['all_gates'] and bg['input_kind'] == 'completed-unsolved-warm'
          and not bg['accepted_new_solution'] and len(bg['profiles']) == 1
          and owned['exitcode'] == 0 and owned['wait4_observed']
          and owned['termination_signal'] is None)
    profile = bg['profiles'][0]
    check('same_complete_first_piece',
          first['all_gates'] and first['actual_profile'] == profile['frozen_profile']
          and first['input_kind'] == 'completed-unsolved-warm'
          and sha(args.first_piece) in bg['input_identities'].values())
    check('previous_owned_diagnostic_retained',
          sha(args.previous_diagnostic) == R1_SHA and previous['all_gates']
          and previous_owned['exitcode'] == 0 and previous_owned['wait4_observed']
          and previous_owned['termination_signal'] is None
          and previous['warm_screen_sha256'] == profile['completed_warm_screen_sha256'])
    for filename, digest in PINS.items():
        check('frozen_source_'+filename, sha(HERE/filename) == digest)
    check('complete_certified_actual_table',
          sha(args.table) == TABLE_SHA and table['all_gates']
          and len(table['root_weight_rows']) == 64)
    check('actual_angle_boost_profile', profile['frozen_profile']['boost_law'] == 'angle')
    provider_source = (HERE/'alternative-neck-provider.py').read_text()
    angle_source = (HERE/'strong_angle_boost.py').read_text()
    check('original_provider_whole_rule_branch',
          "if seg['kind']in('hermite','boost'):" in provider_source
          and "np.dot(np.sqrt(1-velocity(seg,base.gu)**2),base.gw)" in provider_source)
    check('original_angle_hook_preserves_boost_kind',
          "turn.update(kind='boost'" in angle_source
          and "np.sin(provider.fl.phase(seg,u))" in angle_source)
    base = module('endpoint_rules_base', 'strong_newg_binary_background_C2_comparison.py')
    helper = module('endpoint_rules_gauss', 'strong_newg_gauss64_piecewise_C2_bridge.py')
    node_q = [rational(row['actual_binary_gu']) for row in table['root_weight_rows']]
    nodes = list(map(aq, node_q))
    weights = [aq(rational(row['actual_normalized_binary_weight'])) for row in table['root_weight_rows']]
    Ew = dyadic(table['certified_error_bounds']['normalized_total_weight_error'])
    Eu = dyadic(table['certified_error_bounds']['maximum_normalized_node_error'])
    remainder = helper.remainder_jet(F(2), F(1 << 20))
    rows = []
    split_by_component = {}
    provider_by_component = {}
    actual_by_component = {}
    analytic_fee = F(0)
    split_nodes = 0
    additional_whole_nodes = 0
    whole_boost_count = 0

    for index, record in enumerate(profile['comparison_definition']['actual_binary_segments']):
        seg = record['original_binary_segment']
        length = binary(seg['length'])
        component = record['component']
        if component not in split_by_component:
            split_by_component[component] = arb(0)
            provider_by_component[component] = arb(0)
        a0 = binary(seg['a0'])
        if seg['kind'] == 'hermite':
            check('only_actual_frontload_polynomial',
                  index == 0 and seg['strong_initial_speed_frontload_degree'] == 22)
            speed = [aq(binary(x)) for x in seg['strong_initial_speed_frontload_velocity_controls']]
            radius = list(map(binary, seg['strong_initial_speed_frontload_radius_controls']))
            dr = aq(radius[-1]-a0)
            split_dh = arb(0)
            for i, (u, weight) in enumerate(zip(nodes, weights)):
                velocity = bernstein(speed, u)
                radicand = 1-velocity*velocity
                check('first_Gauss_sqrt_domain_'+str(i), radicand.lower() > 0)
                split_dh += weight*radicand.sqrt()
                split_nodes += 1
            split_dh *= aq(length)
            fee = rational(first['physical_first_piece_partial_height_C0_C1_C2'][0])
            provider_dh = split_dh
            rule = 'whole64-sqrt-stored-Bernstein-velocity'
        else:
            dr = arb(0)
            split_dh = arb(0)
            fee = F(0)
            pieces = base.phase_pieces(seg)
            for piece_index, (lo, hi, phi) in enumerate(pieces):
                span = hi-lo
                normalized = base.affine_poly(phi, lo, span)
                centered = base.affine_poly(normalized, F(1, 2), F(1))
                cap = sum((abs(c)*2**j for j, c in enumerate(centered)), F(0))
                check('phase_entire_disk_'+str(index)+'_'+str(piece_index),
                      aq(cap).exp() < 1 << 20)
                derivatives = []
                for order in range(1, 4):
                    polynomial = normalized
                    for unused in range(order):
                        polynomial = base.derivative(polynomial)
                    derivatives.append(sum(map(abs, polynomial), F(0)))
                d1, d2, d3 = derivatives
                M = [F(1), d1, d1*d1+d2, d1**3+3*d1*d2+d3]
                unused_table, unused_exact, total = helper.primitive_errors(Ew, Eu, M, remainder)
                fee += length*span*total[0]
                for u, weight in zip(nodes, weights):
                    theta = base.polyeval(phi, aq(lo)+aq(span)*u)
                    dr += aq(length*span)*weight*theta.sin()
                    split_dh += aq(length*span)*weight*theta.cos()
                    split_nodes += 1
            provider_dh = split_dh
            rule = 'split64-exact-binary-phase-cosine'
            if seg['kind'] == 'boost':
                check('unique_angle_boost_whole_height_rule',
                      seg.get('strong_angle_boost') is True and index == 1 and len(pieces) == 3)
                provider_dh = arb(0)
                for i, (uq, weight) in enumerate(zip(node_q, weights)):
                    matching = [(lo, hi, phi) for lo, hi, phi in pieces if lo <= uq <= hi]
                    check('boost_whole_node_unique_piece_'+str(i), len(matching) == 1)
                    theta = base.polyeval(matching[0][2], aq(uq))
                    sine = theta.sin()
                    radicand = 1-sine*sine
                    check('boost_whole_node_positive_sqrt_'+str(i),
                          radicand.lower() > 0 and theta.cos().lower() > 0)
                    provider_dh += weight*radicand.sqrt()
                    additional_whole_nodes += 1
                provider_dh *= aq(length)
                rule = 'whole64-sqrt-one-minus-sine-phase-squared'
                whole_boost_count += 1
        analytic_fee += fee
        dr_error = aq(binary(seg['dr']))-dr
        evaluation_error = aq(binary(seg['dh']))-provider_dh
        rule_difference = provider_dh-split_dh
        split_by_component[component] += split_dh
        provider_by_component[component] += provider_dh
        actual_by_component[component] = float(seg['h1'])
        exact_accumulation_residual = binary(seg['h1'])-binary(seg['h0'])-binary(seg['dh'])
        rows.append(dict(
            segment=index, component=component, local_segment=record['local_segment'], kind=seg['kind'],
            exact_provider_height_rule=rule,
            actual_stored_dr=seg['dr'], actual_stored_dh=seg['dh'],
            actual_local_h0=seg['h0'], actual_local_h1=seg['h1'],
            exact_radius_increment_box=box(dr),
            exact_provider_height_increment_box=box(provider_dh),
            exact_split_height_increment_box=box(split_dh),
            actual_stored_dr_minus_exact_radius_box=box(dr_error),
            actual_stored_dh_minus_exact_provider_rule_box=box(evaluation_error),
            exact_provider_minus_split_height_rule_box=box(rule_difference),
            actual_stored_dh_endpoint_evaluation_difference_upper=upper(abs(evaluation_error)),
            exact_provider_to_split_rule_difference_upper=upper(abs(rule_difference)),
            exact_height_accumulation_rounding_residual=dict(
                numerator=str(exact_accumulation_residual.numerator),
                denominator=str(exact_accumulation_residual.denominator)),
            actual_component_height_minus_exact_provider_sum_box=box(
                aq(binary(seg['h1']))-provider_by_component[component]),
            exact_split_Gauss_and_binary_table_to_analytic_height_fee=upper(aq(fee))))

    check('all_twelve_original_segments',
          len(rows) == profile['segments'] == 12 and set(split_by_component) == {'prefix', 'bridge'})
    check('exactly_one_actual_whole_angle_boost_rule', whole_boost_count == 1)
    check('complete_original_and_extra_node_coverage', split_nodes == 1536 and additional_whole_nodes == 64)
    actual_combined = actual_by_component['prefix']+actual_by_component['bridge']
    provider_combined = provider_by_component['prefix']+provider_by_component['bridge']
    split_combined = split_by_component['prefix']+split_by_component['bridge']
    evaluation_error = aq(binary(actual_combined))-provider_combined
    rule_difference = provider_combined-split_combined
    complete_error = aq(binary(actual_combined))-split_combined
    direct_fee = abs(complete_error)+aq(analytic_fee)
    decomposed_fee = abs(evaluation_error)+abs(rule_difference)+aq(analytic_fee)
    old_split_box = previous['exact_mathematical_binary_Gauss_combined_height_box']
    check('same_r1_mathematical_split_sum',
          split_combined.overlaps(aq(dyadic(old_split_box[0])))
          or (dyadic(old_split_box[0]) <= dyadic(upper(split_combined))
              and dyadic(old_split_box[1]) >= dyadic(bound(split_combined, 'lower'))))
    check('same_r1_actual_combined_height',
          binary(actual_combined) == binary(previous['actual_binary_combined_provider_height']))
    input_paths = (args.background, args.background_resource, args.first_piece, args.table,
                   args.previous_diagnostic, args.previous_resource)
    output = dict(
        schema='actual-frontload-complete-provider-endpoint-rule-accounting-v2',
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)', source_sha256=sha(__file__),
        input_sha256={str(path): sha(path) for path in input_paths}, frozen_helper_sha256=PINS,
        input_kind='completed-unsolved-warm', warm_screen_sha256=profile['completed_warm_screen_sha256'],
        profile=profile['frozen_profile'], rows=rows, gate_count=len(gates), gates=gates, all_gates=True,
        original_split_quadrature_nodes=split_nodes, additional_whole_boost_quadrature_nodes=additional_whole_nodes,
        actual_binary_component_endpoint_heights=actual_by_component,
        actual_binary_combined_provider_height=actual_combined,
        exact_mathematical_provider_rule_combined_height_box=box(provider_combined),
        exact_mathematical_split_rule_combined_height_box=box(split_combined),
        actual_combined_minus_exact_provider_rule_box=box(evaluation_error),
        exact_provider_minus_split_rule_combined_height_box=box(rule_difference),
        actual_combined_minus_exact_split_rule_box=box(complete_error),
        actual_endpoint_evaluation_and_height_accumulation_fee=upper(abs(evaluation_error)),
        exact_quadrature_rule_discrepancy_fee=upper(abs(rule_difference)),
        complete_split_Gauss_and_binary_table_to_analytic_fee=upper(aq(analytic_fee)),
        decomposed_total_actual_endpoint_to_analytic_fee=upper(decomposed_fee),
        direct_total_actual_endpoint_to_analytic_fee=upper(direct_fee),
        analytic_reference='Constructor-length integrals of the stored first velocity square-root and subsequent exact binary phase cosines, with one zero global height anchor.',
        correction_to_previous_r1='r1 compared actual provider height against the split mathematical rule. Its 1.66e-9 difference is a valid endpoint discrepancy but is not exclusively arithmetic error: it includes the retained original whole-rule angle boost.',
        all_actual_endpoint_rule_evaluation_and_height_accumulation_differences_included=True,
        phase_parameter_initialization_relative_to_ideal_physical_parameters_paid=False,
        uniform_libm_or_floating_function_derivative_error_claimed=False,
        repaired_radius_induced_height_or_complete_surface_mean_or_closed_D_certified=False,
        ideal_length_root_global_alignment_or_new_solution_claimed=False,
        new_ODE_Node_Newton_or_geometry_samples=0,
        elapsed_seconds=time.monotonic()-started,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    args.out.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(dict(out=str(args.out), sha256=sha(args.out), gates=len(gates),
                         actual_height=actual_combined,
                         evaluation_fee=float(abs(evaluation_error).upper()),
                         rule_discrepancy=float(abs(rule_difference).upper()),
                         split_analytic_fee=float(aq(analytic_fee).upper()),
                         decomposed_total_fee=float(decomposed_fee.upper()))), flush=True)


if __name__ == '__main__':
    main()
