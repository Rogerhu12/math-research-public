#!/usr/bin/env python3
"""True forward endpoint from the complete chronological coordinate integral.

The finite reference endpoint is x/4+U(x).  Every Laurent coefficient of
P2=x+4U+(1+4U')w+2U''w^2 is kept.  Coordinate-flow error, coefficient selection,
and the full cubic composition remainder are separate directed charges.
Without --flow-index this produces only finite endpoint derivative bounds.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
from pathlib import Path
import time
from flint import arb, acb, acb_poly, ctx

from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_half_return_predictor import endpoint, laurent
from fourfold_retarget_reference_segment_package import load_package
from fourfold_phase_unified_scalar_time_circle import exact_time
from fourfold_phase_field_time_turn_collar import PiTime
from fourfold_saved_circle_field_multidomain_budget import read, upper
from fourfold_forward_density_pipeline_Q1024_v3 import (
    save, decode_ball, encode_ball,
)


def norm(row, width, derivative=0):
    return sum(((1 if k == 0 else 2)*k**derivative*abs(z)*(k*width).exp()
                for k, z in enumerate(row)), arb(0)).upper()


def add(*terms):
    K = max(len(row) for scale, row in terms)-1
    output = [acb(0) for k in range(K+1)]
    for scale, row in terms:
        for k, z in enumerate(row):
            output[k] += scale*z
    if not output[0].imag.contains(0):
        raise ValueError('real Fourier sum lost its real mean')
    output[0] = acb(output[0].real)
    return output


def derivative(row, order=1):
    return [acb(0, k)**order*z for k, z in enumerate(row)]


def product(left, right):
    K = len(left)+len(right)-2
    full = acb_poly(laurent(left))*acb_poly(laurent(right))
    if not full[K].imag.contains(0):
        raise ValueError('complete Laurent product lost its real mean')
    return [acb(full[K].real)]+[full[K+k] for k in range(1, K+1)]


def midpoint(row):
    chosen = [acb(z.real.mid(), z.imag.mid()) for z in row]
    if not row[0].imag.contains(0):
        raise ValueError('the enclosed first/second integral mean is not real')
    chosen[0] = acb(chosen[0].real)
    return chosen


def load_full_flow(path, descriptor_sha):
    index = read(path)
    if (not index.get('complete') or not index.get('whole_forward_leg')
        or index.get('completed_segments') != 550
        or not index.get('all_listed_time_and_finite_reference_seams_exact')
        or index['descriptor_sha256'] != descriptor_sha):
        raise ValueError('a completed same-reference whole forward flow is required')
    controllers = sorted(Path(__file__).parent.glob('fourfold_forward_density_cover*.py'))
    if index['source_sha256'] not in {sha(path) for path in controllers}:
        raise ValueError('the completed controller source identity differs')
    S, sigma = map(Fraction, (index['label_strip'], index['inner_strip']))
    if not 0 < sigma < S:
        raise ValueError('invalid saved nested strips')
    last = PiTime(Fraction(0), Fraction(-1, 2))
    A, E, J = arb(0), arb(0), arb(0)
    expected_segment, expected_left = 0, Fraction(0)
    for row in index['leaves']:
        report_path = Path(row['path'])
        if sha(report_path) != row['sha256']:
            raise ValueError('a completed true-density leaf changed')
        report = read(report_path)
        identity = report['identity']['reference']
        left, right = map(Fraction, row['normalized_subspan'])
        if (not report.get('complete') or not report.get('complete_continuous_true_density_proved')
            or Fraction(report['label_strip']) != S or Fraction(report['inner_strip']) != sigma
            or identity['retarget_descriptor_sha256'] != descriptor_sha
            or identity['leg'] != 'forward' or identity['segment'] != expected_segment
            or int(row['segment']) != expected_segment or left != expected_left
            or list(map(Fraction, identity['normalized_subspan'])) != [left, right]
            or not left < right <= 1):
            raise ValueError('whole-forward leaf identity or exact partition differs')
        start, stop = map(exact_time, report['identity']['exact_time_endpoints'])
        if start != last:
            raise ValueError('the saved forward density has an exact-time gap')
        last = stop
        if right == 1:
            expected_segment += 1
            expected_left = Fraction(0)
        else:
            expected_left = right
        bounds = report['R72_inputs']
        A = (A+upper(bounds['common_integrated_majorant_A'])).upper()
        E = (E+upper(bounds['integrated_approximation_error_E'])).upper()
        J = (J+upper(bounds['omitted_local_second_integral_bound_on_inner_strip'])).upper()
    if (expected_segment != 550 or expected_left != 0
        or last != PiTime(Fraction(0), Fraction(1, 2))):
        raise ValueError('the complete exact forward interval is not covered')
    gap = exact_arb(S-sigma)
    if not A <= gap/2:
        raise ValueError('complete R72 smallness fails')
    B = (E*(1+A/gap)+A**3/(2*(gap-A)**2)+J).upper()
    accumulator_path = Path(index['accumulator_path'])
    if sha(accumulator_path) != index['accumulator_sha256']:
        raise ValueError('saved ordered accumulator changed')
    accumulator = read(accumulator_path)
    if (accumulator['identity']['descriptor_sha256'] != descriptor_sha
        or accumulator['identity']['leaves'] != index['leaves']
        or not accumulator.get('every_cross_frequency_retained')):
        raise ValueError('accumulator belongs to a different ordered sequence')
    C1 = [decode_ball(z) for z in accumulator['first']]
    C2 = [decode_ball(z) for z in accumulator['second_cross']]
    W = add((1, C1), (1, C2))
    return index, W, A, E, J, B, S, sigma


def inverse_constants(path, H_sha, width):
    report = read(path)
    candidates = [row for row in report['finite_inverse_budgets']
        if row.get('local_inverse_finite_budget_proved')
        and row['polynomials_sha256'] == H_sha
        and Fraction(row['strip_width']) >= width]
    if not report.get('complete') or not candidates:
        raise ValueError('the same finite H has no wide-enough proved inverse budget')
    row = candidates[0]
    for name in ('inverse_Hprime_bound', 'contraction_bound'):
        if 'upper_exact' not in row[name]:
            raise ValueError('finite inverse needs directed exact upper endpoints')
    R = exact_arb(Fraction(row['inverse_Hprime_bound']['upper_exact']))
    kappa = exact_arb(Fraction(row['contraction_bound']['upper_exact']))
    radius = exact_arb(Fraction(row['displacement_radius']))
    if not 0 < R or not 0 <= kappa <= arb(1)/2 or not radius > 0:
        raise ValueError('invalid previously proved local inverse constants')
    return R, kappa, radius, row


def main():
    p = argparse.ArgumentParser(description=__doc__)
    b = Path('data/phase_ring_continuation')
    p.add_argument('--package', type=Path, default=b/'step5_forward549_exact_reference_package.npz.gz')
    p.add_argument('--flow-index', type=Path)
    p.add_argument('--inverse-budget', type=Path, default=Path('notes/2026-11-12-D5-exact-affine-step5-local-inverse-budget.json'))
    p.add_argument('--derivative-strip', default='1/256')
    p.add_argument('--widths', default='1/512,5/2048')
    p.add_argument('--full-map-outer-strip', default='9/4096')
    p.add_argument('--full-map-inner-strip', default='1/512')
    p.add_argument('--bits', type=int, default=320)
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    ctx.prec = args.bits
    start = time.monotonic()
    package = load_package(args.package)
    identity = package['metadata']['identity']
    descriptor_sha = package['documents']['descriptor']['sha256']
    U = endpoint(package)
    Hdoc = package['documents']['target_H']['document']
    if Hdoc.get('source_metadata', {}).get('target') != 'D5':
        raise ValueError('this proof fixes the accurate D5 half rotation')
    H_sha = package['documents']['target_H']['sha256']
    denominator = 2**int(Hdoc['denominator_power_of_two'])
    h = [acb(arb(int(a))/denominator, arb(int(b))/denominator)
         for a, b in Hdoc['h_nonnegative_integer_coefficients']]
    d = arb.pi()*(15121+arb(5).sqrt())/27422
    width = Fraction(args.derivative_strip)
    report = dict(kind='complete_finite_forward_endpoint_and_true_flow_transfer',
        complete_finite_endpoint=True, complete_true_forward_endpoint=False,
        source_sha256=sha(__file__), package_path=str(args.package), package_sha256=sha(args.package),
        identity=identity, descriptor_sha256=descriptor_sha,
        H_sha256=H_sha, target_half_angle=ball_record(d), bits=args.bits,
        finite_endpoint_degree=len(U)-1,
        finite_endpoint_derivative_strip=str(width),
        finite_U_derivative_bounds={str(j): ball_record(norm(U, exact_arb(width), j)) for j in range(4)},
        dependency_sha256={name: sha(Path(__file__).with_name(name)) for name in (
            'fourfold_half_return_predictor.py', 'fourfold_retarget_reference_segment_package.py',
            'fourfold_forward_density_pipeline_Q1024_v3.py')})
    if args.flow_index is None:
        report.update(scope='Only the exact finite endpoint and its complete Fourier derivatives; no actual ODE correction.',
                      wall_seconds=time.monotonic()-start)
        save(args.out, report)
        print({'finite_endpoint_complete': True, 'true_forward_flow_supplied': False,
               'derivatives': report['finite_U_derivative_bounds']}, flush=True)
        return
    index, W, A, E, J, B, S, sigma = load_full_flow(args.flow_index, descriptor_sha)
    widths = list(map(Fraction, args.widths.split(',')))
    if not widths or any(not 0 <= s < sigma for s in widths):
        raise ValueError('all endpoint Wiener widths must be strictly below the proved flow strip')
    w = midpoint(W)
    sigma_ball = exact_arb(sigma)
    choice = norm([z-v for z, v in zip(W, w)], sigma_ball)
    D = norm(w, sigma_ball)
    derivative_radius = (sigma_ball+max(A, D)).upper()
    endpoint_lipschitz = (1+4*norm(U, derivative_radius, 1)).upper()
    cubic = (arb(2)/3*norm(U, (sigma_ball+D).upper(), 3)*D**3).upper()
    endpoint_error = (endpoint_lipschitz*(B+choice)+cubic).upper()
    w2 = product(w, w)
    Pperiodic = add((4, U), (1, w), (4, product(derivative(U), w)),
                    (2, product(derivative(U, 2), w2)))
    shifted_h = [z*(acb(0, k)*d).exp() for k, z in enumerate(h)]
    residual = add((1, Pperiodic), (-1, shifted_h), (-1, [acb(d)]))
    rows = []
    R, kappa, radius, inverse = inverse_constants(args.inverse_budget, H_sha, max(widths))
    for s in widths:
        gap = exact_arb(sigma-s)
        hardy = (1+4/((2*gap).exp()-1)).sqrt().upper()
        finite_error = norm(residual, exact_arb(s))
        true_error = (finite_error+hardy*endpoint_error).upper()
        accepted = bool(R*true_error <= radius/2)
        row = dict(strip=str(s), finite_P2_error_A_norm=ball_record(finite_error),
            Hardy_factor=ball_record(hardy), true_half_endpoint_error_A_norm=ball_record(true_error),
            R63_local_inverse_smallness_passed=accepted)
        if accepted:
            row['preconjugated_half_defect_A_norm'] = ball_record((R*true_error/(1-kappa/2)).upper())
        rows.append(row)
    outer, inner = map(Fraction, (args.full_map_outer_strip, args.full_map_inner_strip))
    if not 0 <= inner < outer < max(widths):
        raise ValueError('invalid nested full-map strips')
    wide = next(row for row in rows if Fraction(row['strip']) == max(widths))
    squared = dict(outer_strip=str(outer), inner_strip=str(inner), proved=False,
        exact_relation='C=H^-1 o A; H^-1 o R o H=C o C, where A=P o H and R=P o P')
    if wide['R63_local_inverse_smallness_passed']:
        Uhalf = upper(wide['preconjugated_half_defect_A_norm'])
        if Uhalf <= exact_arb(max(widths)-outer):
            full_error = (2*Uhalf).upper()
            second = (2*full_error/exact_arb(outer-inner)**2).upper()
            squared.update(proved=True, true_full_preconjugacy_error_A_outer=ball_record(full_error),
                           true_full_spatial_second_derivative_A_inner=ball_record(second))
    finite_path = args.out.with_name(args.out.name.removesuffix('.json.gz').removesuffix('.json')+'_P2.json.gz')
    save(finite_path, dict(kind='complete_enclosed_finite_quadratic_endpoint_residual',
        identity=identity, H_sha256=H_sha, formula='4U+w+4Uprime*w+2Usecond*w^2-d-h(x+d)',
        coefficients=[encode_ball(z) for z in residual], all_product_frequencies_retained=True,
        source_flow_index_sha256=sha(args.flow_index)))
    report.update(complete_true_forward_endpoint=True, flow_index_path=str(args.flow_index),
        flow_index_sha256=sha(args.flow_index), flow_outer_strip=str(S), flow_inner_strip=str(sigma),
        total_A=ball_record(A), total_E=ball_record(E), total_omitted_local_J=ball_record(J),
        R72_coordinate_error=ball_record(B), full_coefficient_midpoint_choice_fee=ball_record(choice),
        selected_w_A_sigma=ball_record(D), endpoint_lipschitz=ball_record(endpoint_lipschitz),
        endpoint_derivative_radius=ball_record(derivative_radius),
        complete_cubic_endpoint_remainder=ball_record(cubic),
        true_endpoint_vs_finite_P2_sup_error=ball_record(endpoint_error), Wiener_bounds=rows,
        finite_residual_path=str(finite_path), finite_residual_sha256=sha(finite_path),
        finite_residual_degree=len(residual)-1, full_return_square=squared,
        inverse_budget_path=str(args.inverse_budget), inverse_budget_sha256=sha(args.inverse_budget),
        reused_proved_finite_inverse=inverse, wall_seconds=time.monotonic()-start,
        limitations=['Fixed actual parameter only; actual first/second parameter sources and twist are separate.',
                    'No R31 KAM acceptance or complete PDE inverse is inferred.'])
    save(args.out, report)
    print({'true_forward_endpoint_complete': True, 'Wiener_bounds': rows,
           'full_return_square': squared, 'report_sha256': sha(args.out)}, flush=True)


if __name__ == '__main__':
    main()
