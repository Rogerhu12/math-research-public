#!/usr/bin/env python3
"""Complete physical R=25/8 ports of an exact finite moving-angle candidate.

The radial endpoint is evaluated over exact dyadic rationals.  The nonlinear
physical Fourier moments are integrated in Arb, with complete analytic alias
and infinite physical-mode tails.  The true regular q errors and both nonlinear
periodic-long ports remain separate from the candidate's nominal boundary rows.
This does not certify a body BVP solution or solve the far regular label equation.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import json
from pathlib import Path
import time

from flint import acb, arb, ctx
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record, save, sha


COORDINATES = ('moving phi: u=alpha*U; v=1/Cref_nu+alpha*V; '
               'theta_phi=v/mean_phi(v); B=u/v; C=1/v')


def read_json(path):
    path = Path(path)
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw)


def upper(x):
    return arb(x).upper()


def complex_record(x):
    return dict(real=record(x.real), imaginary=record(x.imag))


def norm_tail(J, sigma, output_width, psi_bound, u_bound, inverse_mean):
    """Both signs, all physical indices j>J, with weight exp(4j*tau)."""
    decay = sigma-psi_bound-output_width
    if not decay > 0:
        raise ValueError('nonpositive physical analytic strip')
    x = (-4*decay).exp()
    geometric = x**(J+1)/(1-x)
    first_moment = x**(J+1)*((J+1)-J*x)/(1-x)**2
    return (upper(8*inverse_mean*psi_bound*first_moment),
            upper(2*inverse_mean*u_bound*geometric))


def local_long_budget(radius, far_radius, ports):
    """One stated ball, using the already proved complete long-end theorem."""
    rZ = exact_arb(radius)
    rB = exact_arb(far_radius)
    rf = upper(10*(rZ+rB))
    F = upper(rf+rB)
    H = upper(6*F)
    b = ports['bounds']
    epsilon = box_from_record(b['complete_true_q_to_periodic_long_linear_difference'])
    reflection = box_from_record(b['far_Dirichlet_reflection'])
    image = upper(9*rZ+reflection*rB+9*arb(2)**12*F*F)
    contraction = upper(9*4*arb(2)**12*F)
    if not (2*F < arb(2)**-25 and H < arb(2)**-20
            and image < rf and contraction < 1):
        raise ValueError('the stated local periodic-long ball did not close')
    derivative = upper(9/(1-contraction))
    return dict(physical_C_radius=rZ, independent_far_Dirichlet_radius=rB,
                inner_Dirichlet_radius=rf, total_boundary_radius=F,
                long_Y_upper=H, C_inverse_image=image,
                C_inverse_image_margin=(rf-image).lower(),
                C_inverse_contraction=contraction,
                C_inverse_derivative=derivative,
                true_nonmean_d_upper=upper(epsilon*rZ+reflection*rB+arb(2)**14*F*F),
                true_C_mean_upper=upper(arb(2)**11*F*F),
                true_B_mean=arb(0),
                true_nonmean_d_derivative=upper(epsilon+4*arb(2)**14*F*derivative),
                true_C_mean_derivative=upper(4*arb(2)**11*F*derivative))


def run(args, doc):
    candidate_index = read_json(args.candidate)
    saved = load_candidate(args.candidate)
    meta = json.loads(str(saved['metadata']))
    M = int(meta['modes'])
    if (meta['coordinates'] != COORDINATES
            or meta['physical_frequency_factor'] != 4
            or meta['exact_cap_cut'] != '25/8'
            or saved['piece_coefficients'].shape[2] != 2*M+1):
        raise ValueError('the complete moving candidate coordinates do not match')
    alpha_fraction = Fraction(meta['exact_float_amplitude'])
    nu_fraction = Fraction(meta['exact_float_nu'])
    if (Fraction.from_float(meta['amplitude']) != alpha_fraction
            or Fraction.from_float(meta['nu']) != nu_fraction):
        raise ValueError('the candidate dyadic amplitude or metric parameter changed')
    if meta['object_sha256'] != sha(args.object):
        raise ValueError('the actual intrinsic object changed')
    if Fraction.from_float(float(saved['radial_nodes'][-1])) != Fraction(25, 8):
        raise ValueError('the complete PPoly does not end at the actual regular cut')
    if not (args.moments >= M and args.nodes > args.moments
            and 0 < args.strip <= Fraction(1, 8)
            and 0 <= args.output_width < args.strip
            and 0 < args.local_C_radius <= Fraction(1, 10**9)):
        raise ValueError('invalid complete moment or long-graph domain')

    ports = read_json(args.ports)
    qvector = read_json(args.q_vector)
    if (ports['kind'] != 'actual_R25over8_regular_vector_and_complete_nonlinear_long_ports'
            or not ports['complete'] or not ports['whole_affine_parameter_interval']
            or not ports['complete_primitive_tail']
            or not ports['all_Fourier_modes_and_mean_retained']
            or ports['physical_cut'] != '25/8'
            or ports['object_sha256'] != sha(args.object)
            or ports['source_sha256'] != sha(Path(__file__).with_name(
                'fourfold_codazzi_actual_regular_endpoint_ports.py'))):
        raise ValueError('the actual all-mode regular endpoint theorem is required')
    for path, expected in ports['inputs'].items():
        if sha(path) != expected:
            raise ValueError('changed true regular endpoint dependency: '+path)
    if (meta['q_vector_sha256'] != sha(args.q_vector)
            or qvector['modes'] < args.moments
            or qvector['right_boundary'] != '25/8'
            or len(ports['modes']) < args.moments):
        raise ValueError('the candidate and actual q proposal vector differ')
    for j in range(M):
        if Fraction(meta['exact_float_q_values'][j]) != Fraction.from_float(qvector['q_values'][j]):
            raise ValueError('a retained complete physical q proposal changed')

    # Exact PPoly evaluation.  Every input double is an exact dyadic number;
    # in particular no sampled floating endpoint is silently substituted.
    left = Fraction.from_float(float(saved['radial_nodes'][-2]))
    h = Fraction(25, 8)-left
    coeff = saved['piece_coefficients'][:, -1, :]
    endpoint = []
    for column in range(2*M+1):
        value = Fraction(0)
        for order in range(4):
            value = value*h+Fraction.from_float(float(coeff[order, column]))
        endpoint.append(value)
    U = [exact_arb(x) for x in endpoint[:M]]
    V = [exact_arb(x) for x in endpoint[M:]]
    alpha = exact_arb(alpha_fraction)
    sigma = exact_arb(args.strip)
    output_width = exact_arb(args.output_width)
    reference = box_from_record(ports['bounds']['actual_C_reference'])
    s = 1/reference
    mean = s+alpha*V[0]
    if not (reference < 0 and mean < 0):
        raise ValueError('the actual reference or moving mean is not negative')
    mean_gap = (-mean).lower()
    inv_mean = upper(1/mean_gap)
    u_strip = arb(0)
    v_strip = arb(0)
    primitive_strip = arb(0)
    u_real = arb(0)
    v_real = arb(0)
    for j in range(1, M+1):
        weight = (4*j*sigma).exp()
        u_real += abs(alpha*U[j-1])
        v_real += abs(alpha*V[j])
        u_strip += abs(alpha*U[j-1])*weight
        v_strip += abs(alpha*V[j])*weight
        primitive_strip += abs(alpha*V[j])*weight/(4*j)
    u_strip, v_strip, u_real, v_real = map(upper, (u_strip, v_strip, u_real, v_real))
    psi_strip = upper(primitive_strip*inv_mean)
    if not (v_strip < mean_gap and sigma-psi_strip-output_width > 0):
        raise ValueError('the full strip inverse/physical tail gates are unresolved')
    angle_jacobian_lower = (1-v_real*inv_mean).lower()
    if not angle_jacobian_lower > 0:
        raise ValueError('the real physical angle does not have positive degree-one derivative')

    N, J = args.nodes, args.moments
    q = []
    q_error = []
    for j in range(1, J+1):
        r = ports['modes'][j-1]
        if r['physical_frequency'] != 4*j:
            raise ValueError('the complete native q vector has the wrong frequencies')
        proposal = Fraction.from_float(qvector['q_values'][j-1])
        if proposal != Fraction.from_float(r['nominal_dyadic_q']):
            raise ValueError('a native proposal and the floating vector differ')
        q.append(exact_arb(proposal))
        q_error.append(box_from_record(r['whole_parameter_nominal_q_error']))

    sum_C = [acb(0) for _ in range(J)]
    sum_B = [acb(0) for _ in range(J)]
    sum_d = [acb(0) for _ in range(J)]
    imaginary_unit = acb(0, 1)
    for n in range(N):
        phi = arb.pi()*n/(2*N)
        u, primitive = arb(0), arb(0)
        for j in range(1, M+1):
            sine = (4*j*phi).sin()
            u += alpha*U[j-1]*sine
            primitive += alpha*V[j]*sine/(4*j)
        psi = primitive/mean
        base = acb(0, -4*phi).exp()
        shifted = acb(0, -4*psi).exp()
        base_power, shift_power = acb(1), acb(1)
        for j in range(J):
            base_power *= base
            shift_power *= shifted
            # The exactly zero nonconstant Fourier integral is subtracted
            # before enclosure.  Its N-node mean is also zero, since j+1<N.
            C_integrand = base_power*(shift_power-1)
            B_integrand = base_power*u*shift_power
            sum_C[j] += C_integrand
            sum_B[j] += B_integrand
            sum_d[j] += imaginary_unit*B_integrand+q[j]*C_integrand
        if args.progress and (n+1) % 128 == 0:
            print(dict(nodes_done=n+1, nodes=N, resolved_physical_modes=J), flush=True)

    alias_base = upper(2*(-4*N*sigma).exp()/(1-(-4*N*sigma).exp()))
    rows = []
    resolved_C, resolved_B, resolved_d, true_q_fee = [arb(0) for _ in range(4)]
    omitted_resolved_C, omitted_resolved_B, omitted_resolved_d = [arb(0) for _ in range(3)]
    alias_C_total, alias_B_total, alias_d_total = [arb(0) for _ in range(3)]
    for j in range(1, J+1):
        frequency = 4*j
        C_quad = sum_C[j-1]/(N*mean)
        B_quad = sum_B[j-1]/(N*mean)
        d_quad = sum_d[j-1]/(N*mean)
        growth = (frequency*(sigma+psi_strip)).exp()
        C_alias = upper(alias_base*frequency*psi_strip*growth*inv_mean)
        B_alias = upper(alias_base*u_strip*growth*inv_mean)
        d_alias = upper(B_alias+abs(q[j-1])*C_alias)
        C_abs = upper(abs(C_quad)+C_alias)
        B_abs = upper(abs(B_quad)+B_alias)
        d_abs = upper(abs(d_quad)+d_alias)
        weight = (frequency*output_width).exp()
        qc_fee = upper(q_error[j-1]*C_abs)
        resolved_C += 2*weight*C_abs
        resolved_B += 2*weight*B_abs
        resolved_d += 2*weight*d_abs
        true_q_fee += 2*weight*qc_fee
        alias_C_total += 2*weight*C_alias
        alias_B_total += 2*weight*B_alias
        alias_d_total += 2*weight*d_alias
        if j > M:
            omitted_resolved_C += 2*weight*C_abs
            omitted_resolved_B += 2*weight*B_abs
            omitted_resolved_d += 2*weight*(d_abs+qc_fee)
        rows.append(dict(index=j, physical_frequency=frequency,
                         retained_in_finite_BVP=j<=M,
                         exact_nominal_q=str(Fraction.from_float(qvector['q_values'][j-1])),
                         directed_C_quadrature=complex_record(C_quad),
                         directed_B_quadrature=complex_record(B_quad),
                         directed_nominal_robin_quadrature=complex_record(d_quad),
                         C_complete_alias=record(C_alias), B_complete_alias=record(B_alias),
                         nominal_robin_complete_alias=record(d_alias),
                         C_coefficient_abs_upper=record(C_abs),
                         B_coefficient_abs_upper=record(B_abs),
                         nominal_robin_coefficient_abs_upper=record(d_abs),
                         true_q_proposal_error=record(q_error[j-1]),
                         true_q_coefficient_fee=record(qc_fee)))
    C_tail, B_tail = norm_tail(J, sigma, output_width, psi_strip, u_strip, inv_mean)
    Q_upper = box_from_record(ports['bounds']['all_nonmean_true_q_abs_upper'])
    robin_tail = upper(B_tail+Q_upper*C_tail)
    C_full = upper(resolved_C+C_tail)
    B_full = upper(resolved_B+B_tail)
    true_robin = upper(resolved_d+true_q_fee+robin_tail)
    mean_delta = -reference*alpha*V[0]/mean
    mean_delta_upper = upper(abs(mean_delta))

    original_radius = box_from_record(ports['bounds']['physical_C_nonmean_radius'])
    if not C_full < original_radius:
        raise ValueError('the actual complete physical C data are outside the original long ball')
    if not C_full < exact_arb(args.local_C_radius):
        raise ValueError('the actual complete physical C data are outside the stated smaller ball')
    far_radius = Fraction(1, 2**60)
    original_far = box_from_record(ports['bounds']['independent_far_Dirichlet_radius'])
    if not original_far.contains(exact_arb(far_radius)):
        raise ValueError('the independent far Dirichlet input budget changed')
    local = local_long_budget(args.local_C_radius, far_radius, ports)
    old_d = box_from_record(ports['bounds']['exact_regular_q_nonlinear_nonmean_d_upper'])
    old_mean = box_from_record(ports['bounds']['true_C_mean_output_upper'])
    bounds = dict(actual_reference_C=reference, actual_moving_mean=mean,
                  actual_mean_absolute_lower=mean_gap,
                  exact_C_mean_minus_reference=mean_delta,
                  exact_B_mean=arb(0), actual_mean_C_error_abs_upper=mean_delta_upper,
                  u_real_A0_upper=u_real, v_nonmean_real_A0_upper=v_real,
                  u_full_finite_strip_A0_upper=u_strip,
                  v_nonmean_full_finite_strip_A0_upper=v_strip,
                  psi_full_finite_strip_A0_upper=psi_strip,
                  real_angle_derivative_lower=angle_jacobian_lower,
                  real_v_negative_gap=(mean_gap-v_real).lower(),
                  complex_v_nonzero_gap=(mean_gap-v_strip).lower(),
                  physical_analytic_decay=(sigma-psi_strip).lower(),
                  resolved_physical_C_nonmean=upper(resolved_C),
                  resolved_physical_B_nonmean=upper(resolved_B),
                  resolved_nominal_Robin=upper(resolved_d),
                  complete_true_q_proposal_fee=upper(true_q_fee),
                  complete_unresolved_C_tail=C_tail,
                  complete_unresolved_B_tail=B_tail,
                  complete_unresolved_true_Robin_tail=robin_tail,
                  resolved_unretained_C=upper(omitted_resolved_C),
                  resolved_unretained_B=upper(omitted_resolved_B),
                  resolved_unretained_true_Robin=upper(omitted_resolved_d),
                  all_j_above_finite_BVP_C=upper(omitted_resolved_C+C_tail),
                  all_j_above_finite_BVP_B=upper(omitted_resolved_B+B_tail),
                  all_j_above_finite_BVP_true_Robin=upper(omitted_resolved_d+robin_tail),
                  complete_C_alias_fee=upper(alias_C_total),
                  complete_B_alias_fee=upper(alias_B_total),
                  complete_nominal_Robin_alias_fee=upper(alias_d_total),
                  full_physical_C_nonmean_A0=C_full,
                  full_physical_B_nonmean_A0=B_full,
                  full_true_linear_Robin_A0=true_robin,
                  original_long_input_ball_margin=(original_radius-C_full).lower(),
                  smaller_long_input_ball_margin=(exact_arb(args.local_C_radius)-C_full).lower(),
                  original_ball_complete_nonlinear_Robin_residual=upper(true_robin+old_d),
                  original_ball_complete_mean_C_residual=upper(mean_delta_upper+old_mean),
                  smaller_ball_complete_nonlinear_Robin_residual=upper(true_robin+local['true_nonmean_d_upper']),
                  smaller_ball_complete_mean_C_residual=upper(mean_delta_upper+local['true_C_mean_upper']))
    paths = [args.candidate, args.object, args.ports, args.q_vector,
             Path('results/R133-supplement-moving-chart-complete-physical-boundary-moments.md'),
             Path('results/R133-supplement-actual-regular-R25over8-vector-and-long-ports.md')]
    doc.update(complete=True, certified_complete_physical_endpoint=True,
               candidate_sha256=sha(args.candidate), inputs={str(p):sha(p) for p in paths},
               candidate_shards=candidate_index['parts'],
               candidate_metadata=meta, object_sha256=sha(args.object),
               endpoint='25/8', last_piece_left=str(left), last_piece_width=str(h),
               last_piece_index=len(saved['radial_nodes'])-2,
               exact_normalized_endpoint_coefficients=[str(x) for x in endpoint],
               exact_amplitude=str(alpha_fraction), exact_nu=str(nu_fraction),
               exact_center_parameter=ports['exact_center_parameter'],
               parameter_half_width=ports['parameter_half_width'],
               whole_affine_parameter_interval=True, whole_real_angular_circle=True,
               complete_original_intrinsic_tail=True,
               finite_moving_modes=M, resolved_physical_positive_modes=J,
               physical_frequency_factor=4, directed_quadrature_nodes=N,
               quadrature_arithmetic_bits=ctx.prec,
               strip=str(args.strip), physical_output_width=str(args.output_width),
               actual_physical_norm='sum over both signs exp(|k|*tau)*|Fourier coefficient|, k in 4Z; mean separate',
               full_nonlinear_physical_angle_used=True,
               no_finite_quadrature_exactness_assumed=True,
               all_physical_Fourier_modes_and_mean_retained=True,
               local_long_ball_radius_chosen_before_run=str(args.local_C_radius),
               local_long_ball={k:record(v) for k,v in local.items()},
               bounds={k:record(v) for k,v in bounds.items()}, rows=rows,
               gates=dict(exact_dyadic_endpoint=True, whole_parameter_intrinsic_endpoint=True,
                          true_degree_one_physical_angle=True, complete_analytic_alias=True,
                          all_unretained_physical_modes=True,
                          original_C_input_ball=True, stated_smaller_C_input_ball=True,
                          true_q_proposal_error_paid=True, complete_nonlinear_nonmean_port_paid=True,
                          true_C_mean_port_paid=True, true_B_mean_exactly_zero=True,
                          independent_far_Dirichlet_preserved=True,
                          independent_mean_height_preserved=True),
               whole_body_PDE_certified=False, whole_body_inverse_certified=False,
               full_far_regular_label_equation_solved=False,
               far_equation='k_B(a)+C_L*f_B(a)-S_L*f_star-E_D(f_B(a),f_star)=0',
               interpretation='A complete endpoint residual and an actual periodic-long input, not a zero boundary residual or a global surface.',
               dependencies={name:sha(Path(__file__).with_name(name)) for name in (
                   'fourfold_codazzi_candidate_shards.py',
                   'fourfold_codazzi_rotational_cap_jacobi.py',
                   'fourfold_phase_metric_defect.py',
                   'fourfold_phase_beta_bulk_interval.py')})
    print({k:float(bounds[k].upper()) for k in (
        'full_physical_C_nonmean_A0', 'full_physical_B_nonmean_A0',
        'full_true_linear_Robin_A0', 'all_j_above_finite_BVP_true_Robin',
        'smaller_ball_complete_nonlinear_Robin_residual',
        'smaller_ball_complete_mean_C_residual')}, flush=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate', type=Path, required=True)
    ap.add_argument('--object', type=Path, default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--ports', type=Path, default=Path('notes/2026-11-13-R133-regular-r25over8-q256-long-ports-native.json.gz'))
    ap.add_argument('--q-vector', type=Path, default=Path('notes/2026-11-13-R133-regular-r25over8-q256-floating.json'))
    ap.add_argument('--moments', type=int, default=128)
    ap.add_argument('--nodes', type=int, default=512)
    ap.add_argument('--strip', type=Fraction, default=Fraction(1, 8))
    ap.add_argument('--output-width', type=Fraction, default=Fraction(0))
    ap.add_argument('--local-C-radius', type=Fraction, default=Fraction(1, 10**12))
    ap.add_argument('--native', type=Path, required=True)
    ap.add_argument('--progress', action='store_true')
    args = ap.parse_args()
    if args.native.exists():
        raise FileExistsError('preserve every actual endpoint attempt')
    ctx.prec = 320
    ctx.cap = 6
    started = time.monotonic()
    doc = dict(kind='actual_full_moving_candidate_complete_physical_R_boundary',
               complete=False, source_sha256=sha(__file__), failure=None)
    try:
        run(args, doc)
    except Exception as exc:
        doc['failure'] = dict(type=type(exc).__name__, message=str(exc))
        raise
    finally:
        doc['wall_seconds'] = time.monotonic()-started
        save(args.native, doc)
    print(dict(complete=doc['complete'], native=str(args.native),
               wall_seconds=doc['wall_seconds']), flush=True)


if __name__ == '__main__':
    main()
