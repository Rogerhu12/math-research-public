#!/usr/bin/env python3
"""Uniform binary64 value/jet bridge for the actual stored first-piece law.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
All estimates are exact rational inequalities for the frozen de Casteljau
algorithm. The standard basic binary64-operation model includes a generous
absolute underflow/flush fee. These are pointwise value and supplied-jet
bounds, not derivatives of a floating-point function. The actual warm is
not an accepted new solution. No transcendental error model is imported.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import resource
import sys
import time

HERE = Path(__file__).resolve().parent
PINS = {
    'strong_monotone_initial_speed.py': '12d6340d4e9dce27ee93d390971d0258cc1e2299dedf99fe21365a70494549e7',
    'strong_monotone_initial_speed_anchor.py': '583af82cdd6bb672325844587d8aac67e47365ccb5152ac2eae543837adc0ffc',
    'alternative-neck-provider.py': '84ed048425c8b0f4deeec8af37828e318150cde5d59995da77f64d923591b9c2',
}
FIRST_SHA = '21dde900416fa727e2523722114b0cf19ed56e114ff411b15920dabf93286147'
BACKGROUND_SHA = '01aa989aecc9959f10ce556052b90475d5e60c884b814c10811aef63fbadb5ac'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def q(value):
    return F(value['numerator']) / F(value['denominator'])


def pack(value):
    value = F(value)
    return dict(numerator=str(value.numerator), denominator=str(value.denominator))


def binary(value):
    return F.from_float(float(value))


def dyadic(value):
    return F(int(value[0])) * F(2) ** int(value[1])


def up(value, bits=160):
    value = F(value)
    scaled = value * (1 << bits)
    integer = -(-scaled.numerator // scaled.denominator)
    return F(integer, 1 << bits)


def differentiate(controls):
    degree = len(controls)-1
    return [degree*(controls[j+1]-controls[j]) for j in range(degree)]


def elevate(controls, degree):
    row = list(controls)
    while len(row)-1 < degree:
        n = len(row)-1
        row = [row[0]] + [F(j, n+1)*row[j-1] + (1-F(j, n+1))*row[j]
                         for j in range(1, n+1)] + [row[-1]]
    return row


def difference_cap(left, right):
    degree = max(len(left), len(right))-1
    return max(abs(a-b) for a, b in zip(elevate(left, degree), elevate(right, degree)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('first-piece', 'first-piece-resource', 'background', 'background-resource', 'out'):
        parser.add_argument('--'+name, type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    if args.out.exists():
        raise FileExistsError(args.out)
    first = read(args.first_piece)
    bg = read(args.background)
    resources = [read(args.first_piece_resource), read(args.background_resource)]
    gates = {}

    def check(name, condition):
        if not condition:
            raise ArithmeticError(name)
        gates[name] = True

    check('actual_owned_first_piece',
          sha(args.first_piece) == FIRST_SHA and first['all_gates']
          and first['input_kind'] == 'completed-unsolved-warm')
    check('actual_owned_complete_background',
          sha(args.background) == BACKGROUND_SHA and bg['all_gates']
          and bg['input_kind'] == 'completed-unsolved-warm'
          and not bg['accepted_new_solution'])
    for j, owned in enumerate(resources):
        check('owned_exit_zero_'+str(j), owned['exitcode'] == 0 and owned['wait4_observed']
              and owned['termination_signal'] is None)
    for name, digest in PINS.items():
        check('pinned_source_'+name, sha(HERE/name) == digest)
    source = (HERE/'strong_monotone_initial_speed.py').read_text()
    provider = (HERE/'alternative-neck-provider.py').read_text()
    check('same_literal_de_Casteljau_expression',
          'values[:count] = (1-u)*values[:count] + u*values[1:count+1]' in source
          and 'np.result_type(u.dtype, np.float64)' in source)
    check('same_literal_clipped_coordinate',
          "np.clip((ss[mask]-seg['s0'])/seg['length'],0.,1.)" in provider)
    check('runtime_float_binary64', sys.float_info.radix == 2 and sys.float_info.mant_dig == 53
          and binary(sys.float_info.min) == F(2)**-1022)
    profile = bg['profiles'][0]
    check('same_actual_profile', first['actual_profile'] == profile['frozen_profile'])
    first_segment = profile['comparison_definition']['actual_binary_segments'][0]['original_binary_segment']
    data = first['exact_provider_first_piece_data']
    check('actual_first_branch_starts_at_zero',
          binary(first_segment['s0']) == 0
          and binary(first_segment['s1']) == binary(first_segment['length']) == q(first['exact_binary_length']))
    for name in ('radius', 'velocity', 'acceleration'):
        key = 'strong_initial_speed_frontload_'+name+'_controls'
        check('same_stored_'+name+'_controls', first_segment[key] == data[key])

    eps = F(2)**-52
    # A basic-operation absolute fee for operands bounded by 4 (division
    # denominator >=1/2). It also covers a subnormal input or result being
    # flushed: two input losses plus output loss are below 16*2^-1022 here.
    eta = F(16) * F(2)**-1022
    length = q(first['exact_binary_length'])
    check('physical_length_for_safe_normalization', F(1, 2) < length < 1)
    check('rounding_constants_small', 0 < eta < eps < F(1, 100))
    argument_error = eps+4*eta
    controls = {name: list(map(binary, data['strong_initial_speed_frontload_'+name+'_controls']))
                for name in ('radius', 'velocity', 'acceleration')}
    check('complete_original_control_degrees',
          [len(controls[n])-1 for n in ('radius', 'velocity', 'acceleration')] == [23, 22, 21])
    radius_first = [x/length for x in differentiate(controls['radius'])]
    radius_second = [x/length for x in differentiate(radius_first)]
    exact_targets = [controls['radius'], radius_first, radius_second]
    original_order = ('radius', 'velocity', 'acceleration')
    rows = []
    tuple_errors = []
    for index, name in enumerate(original_order):
        row = controls[name]
        degree = len(row)-1
        hull = max(map(abs, row))
        check(name+'_nonnegative_hull_below_two', min(row) >= 0 and hull < 2)
        error = F(0)
        steps = []
        for level in range(1, degree+1):
            exact_next = ((1+eps)**3*error + ((1+eps)**3-1)*hull
                          + 16*eta*(hull+error+1))
            rounded = up(exact_next)
            check(name+'_level_'+str(level)+'_outward_and_no_overflow',
                  rounded >= exact_next >= 0 and hull+rounded < 2)
            steps.append(pack(rounded))
            error = rounded
        derivative_hull = max(map(abs, differentiate(row)))
        coordinate_fee = derivative_hull*argument_error
        supplied_jet_mismatch = difference_cap(row, exact_targets[index])
        tuple_error = up(error+coordinate_fee+supplied_jet_mismatch)
        tuple_errors.append(tuple_error)
        rows.append(dict(name=name, degree=degree, control_hull=pack(hull),
                         all_levels_outward_error=steps,
                         complete_binary64_evaluation_error=pack(error),
                         exact_normalized_polynomial_derivative_hull=pack(derivative_hull),
                         normalized_argument_displacement_fee=pack(coordinate_fee),
                         supplied_jet_to_stored_radius_derivative_mismatch=pack(supplied_jet_mismatch),
                         actual_supplied_jet_to_exact_stored_radius_jet=pack(tuple_error)))
    repair = list(map(dyadic, profile['piece_rows'][0]['quintic_repair_uniform_C0_C1_C2_upper']))
    repaired_tuple_errors = [up(e+r) for e, r in zip(tuple_errors, repair)]
    check('same_first_piece_C2_comparison_interval',
          q(profile['piece_rows'][0]['physical_interval'][0]) == 0
          and q(profile['piece_rows'][0]['physical_interval'][1]) == length)
    check('three_finite_complete_uniform_bounds',
          all(0 <= x < F(1, 10**10) for x in repaired_tuple_errors))
    inputs = (args.first_piece, args.first_piece_resource, args.background, args.background_resource)
    output = dict(
        schema='actual-frontload-binary64-first-piece-supplied-jet-bridge-v1',
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)', source_sha256=sha(__file__),
        input_sha256={str(path): sha(path) for path in inputs}, frozen_source_sha256=PINS,
        input_kind='completed-unsolved-warm', actual_profile=first['actual_profile'],
        warm_screen_sha256=profile['completed_warm_screen_sha256'],
        exact_binary_length=pack(length),
        arithmetic_model=dict(
            format='binary64 basic +,-,*,/; actual input arrays binary64',
            permitted_rounding='any standard IEEE rounding direction; no overflow',
            relative_operation_error=pack(eps), absolute_operation_error=pack(eta),
            subnormal_input_or_result_flush_included=True,
            single_operation_bound='abs(fl(z)-z)<=eps*abs(z)+eta on the explicitly bounded operands',
            layer_bound='Enew <= (1+eps)^3 E + ((1+eps)^3-1) A + 16 eta (A+E+1)',
            transcendental_function_accuracy_assumed=False),
        physical_coordinate_argument_error=pack(argument_error),
        coordinate_domain='binary64 physical s in [0,L]; exact u=s/L; actual clipped first-piece normalization',
        rows=rows,
        actual_supplied_jet_to_exact_stored_radius_jet=list(map(pack, tuple_errors)),
        explicit_first_piece_quintic_repair_C0_C1_C2=list(map(pack, repair)),
        actual_supplied_jet_to_explicit_C2_comparison_radius_jet=list(map(pack, repaired_tuple_errors)),
        comparison_definition_sha256=profile['comparison_definition_sha256'],
        all_binary64_arguments_covered_by_analytic_error_recurrence=True,
        sample_based_error_maximum_used=False,
        rounded_function_differentiability_claimed=False,
        certificate_applies_to_piece_jet_before_neighbor_mask_overwrite=True,
        global_Pieces_profile_tolerance_overlap_bands_paid=False,
        angular_chart_s_to_material_t_evaluation_paid=False,
        partial_height_sqrt_dot_fullmean_or_Cartesian_surface_certified=False,
        new_accepted_solution_or_closed_D_or_reach_claimed=False,
        gates=gates, gate_count=len(gates), all_gates=True,
        new_ODE_Node_Newton_or_geometry_samples=0,
        elapsed_seconds=time.monotonic()-started,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    args.out.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(dict(out=str(args.out), sha256=sha(args.out), gates=len(gates),
                         supplied_to_stored=[float(x) for x in tuple_errors],
                         supplied_to_repaired=[float(x) for x in repaired_tuple_errors])), flush=True)


if __name__ == '__main__':
    main()
