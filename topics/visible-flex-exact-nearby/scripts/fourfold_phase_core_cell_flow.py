#!/usr/bin/env python3
"""Validated true single-cell finite core propagation by an exact reference.

The reference polynomial is defined by an exact rational recurrence from
chosen dyadic generator coefficients. The true analytic generator, angular
aliases, radial primitive tails, time-circle aliases and the complete
reference defect are all included. This certifies one stated common-span
cell only; it is not the full core DN or infinite Schur certificate.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import time
import traceback

import numpy as np
from flint import arb, acb, acb_mat, ctx

from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_affine import provenance
from fourfold_phase_beta_interval import ball_record as native_ball_record


def ball_record(value):
    value = arb(value)
    if not value.is_finite():
        raise ValueError('nonfinite value cannot be recorded as a proof bound')
    return native_ball_record(value)

from fourfold_phase_core_radial_taylor import frobenius
from fourfold_phase_core_waist_taylor import WaistCoreTarget
from fourfold_phase_core_parameter_taylor import ParameterCoreTarget, core_provenance


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def exact_matrix(values):
    return acb_mat([[acb(float(z.real), float(z.imag)) for z in row]
                    for row in np.asarray(values)])


def identity(d):
    value = acb_mat(d, d)
    for j in range(d):
        value[j, j] = 1
    return value


def real_midpoint(value):
    return np.array([[float(value[i, j].real.mid()) for j in range(value.ncols())]
                     for i in range(value.nrows())], dtype=float)


def conjugate(value):
    return acb_mat([[value[i, j].conjugate() for j in range(value.ncols())]
                    for i in range(value.nrows())])


def real_projection(value):
    for i in range(value.nrows()):
        for j in range(value.ncols()):
            if not value[i, j].imag.contains(0):
                raise ValueError('a mathematically real projected generator lost its real axis')
    return acb_mat([[acb(value[i, j].real) for j in range(value.ncols())]
                    for i in range(value.nrows())])


def local_flow(target, left, right, cutoff, strip, outer, sample, nodes, terms,
               degree, momentum_scale, report, save):
    left, right = Fraction(left), Fraction(right)
    if not left < right or not target.cell[0] <= left < right <= target.cell[1]:
        raise ValueError('flow interval must remain inside the selected true common span')
    if not 1 < sample < outer or nodes % 2 or not 0 < terms < nodes:
        raise ValueError('invalid holomorphic time-circle extraction parameters')
    if degree < terms or terms < 2:
        raise ValueError('the exact reference degree must contain the generator recurrence')
    center, half = (left+right)/2, (right-left)/2
    c, h = exact_arb(center), exact_arb(half)
    R, rho = exact_arb(outer), exact_arb(sample)
    width = h*R
    radial_box = acb(c+arb(0, width), arb(0, width))
    M = target.whole_generator_modulus(radial_box, cutoff, momentum_scale)
    report.update(
        stage='true_outer_domain_complete',
        exact_real_interval=[str(left), str(right)], exact_center=str(center),
        exact_halfwidth=str(half),
        whole_true_generator_modulus=ball_record(M),
        actual_outer_domain=target.last_generator_domain)
    save()
    d = 2*(2*cutoff+1)
    samples = [None]*nodes
    for j in range(nodes//2+1):
        if j == 0:
            u = acb(rho)
        elif j == nodes//2:
            u = acb(-rho)
        else:
            u = rho*acb(0, 2*arb.pi()*j/nodes).exp()
        value = target.projected_generator(acb(c)+h*u, cutoff, strip, momentum_scale)
        if j in (0, nodes//2):
            value = real_projection(value)
        samples[j] = value
        if 0 < j < nodes//2:
            samples[nodes-j] = conjugate(value)
        report.update(stage='true_time_circle_sampling',
                      completed_independent_time_nodes=j+1,
                      independent_time_nodes_required=nodes//2+1)
        save()

    dft = [acb_mat(d, d) for _ in range(terms)]
    for i in range(d):
        for j in range(d):
            transformed = acb.dft([value[i, j] for value in samples])
            for k in range(terms):
                dft[k][i, j] = transformed[k]/(nodes*rho**k)
    del samples
    polynomial = []
    exact_coefficients = []
    rows = []
    eps_finite = arb(0)
    ratio = (rho/R)**nodes
    for k, enclosure in enumerate(dft):
        binary = real_midpoint(enclosure)
        chosen = exact_matrix(binary)
        arithmetic = frobenius(enclosure-chosen)
        alias = (M*R**(-k)*ratio/(1-ratio)).upper()
        error = (arithmetic+alias).upper()
        rows.append(dict(time_power=k,
            complete_node_and_coefficient_choice_error=ball_record(arithmetic),
            complete_holomorphic_time_alias=ball_record(alias),
            total_coefficient_error=ball_record(error)))
        eps_finite += error
        polynomial.append(chosen)
        exact_coefficients.append(binary)
    del dft
    time_tail = (M*R**(-terms)/(1-1/R)).upper()
    eps = (eps_finite+time_tail).upper()
    report.update(stage='complete_generator_polynomial',
        exact_generator_polynomial_definition='The stored binary64 matrices are exact dyadic coefficients in u=(r-center)/halfwidth; no point-value interpolation claim is used.',
        physical_momentum_scale=str(momentum_scale),
        coefficient_errors=rows, complete_unretained_time_tail=ball_record(time_tail),
        complete_real_time_generator_error=ball_record(eps))
    save()

    # Exact mathematical definition of Z: each displayed operation is over
    # rational numbers because h and every polynomial coefficient are dyadic.
    # Arb carries an enclosure of that exact recurrence, without choosing
    # rounded Z coefficients or presuming numerical cancellations are exact.
    Z = [identity(d)]
    for k in range(degree):
        value = acb_mat(d, d)
        for j in range(min(k, terms-1)+1):
            value += polynomial[j]*Z[k-j]
        Z.append(h*value/(k+1))
    variation = sum((frobenius(Z[k]) for k in range(1, degree+1)), arb(0)).upper()
    if not variation < 1:
        raise ValueError('exact reference does not have a verified uniform inverse: delta='+variation.str(18))
    inverse_bound = (1/(1-variation)).upper()
    Z_bound = (1+variation).upper()
    residual = arb(0)
    residual_rows = []
    for k in range(degree, degree+terms):
        value = acb_mat(d, d)
        for j in range(max(0, k-degree), min(k, terms-1)+1):
            value += polynomial[j]*Z[k-j]
        bound = (h*frobenius(value)).upper()
        residual += bound
        residual_rows.append(dict(time_power=k, norm_upper=ball_record(bound)))
    residual = residual.upper()
    defect = (residual+h*eps*Z_bound).upper()
    reduced_action = (2*inverse_bound*defect).upper()
    flow_fee = (Z_bound*inverse_bound*(reduced_action.exp()-1)).upper()
    plus, minus = acb_mat(d, d), acb_mat(d, d)
    for k, value in enumerate(Z):
        plus += value
        minus += value if k % 2 == 0 else -value
    exact_reference_transfer = plus*minus.inv()
    center_matrix = real_midpoint(exact_reference_transfer)
    selection = frobenius(exact_reference_transfer-exact_matrix(center_matrix))
    total_error = (flow_fee+selection).upper()
    if not total_error.is_finite():
        raise ValueError('no finite true local transfer error has been established')
    report.update(
        stage='actual_local_transfer_complete',
        exact_reference_definition='Z0=I; Z[k+1]=h/(k+1)*sum_{j=0}^{min(k,m-1)} F[j] Z[k-j]. The actual exact reference has degree q, and the stored F[j] define it uniquely over the rationals.',
        reference_degree=degree,
        complete_reference_variation=ball_record(variation),
        complete_reference_inverse_norm=ball_record(inverse_bound),
        complete_finite_reference_residual=ball_record(residual),
        complete_finite_reference_residual_rows=residual_rows,
        complete_true_reference_defect=ball_record(defect),
        reduced_matrix_defect_action=ball_record(reduced_action),
        true_transfer_minus_exact_reference_error=ball_record(flow_fee),
        exact_reference_to_saved_dyadic_selection_error=ball_record(selection),
        true_scaled_local_transfer_operator_error=ball_record(total_error),
        transfer_direction='left to right in physical r, on all retained heights w and fluxes p/momentum_scale',
        real_matrix_structure='a,c,tau even in theta; b,sigma odd. The projected generator is real in this complex Fourier coefficient basis for real r, hence its radial Taylor coefficients are real and the lower time half-circle is the exact conjugate of the upper one.')
    return np.asarray(exact_coefficients), center_matrix


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--object', type=Path, default=Path(
        'data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    parser.add_argument('--common-span', type=int, default=90)
    parser.add_argument('--parameter-half-width', type=Fraction, default=Fraction(0))
    parser.add_argument('--left', type=Fraction)
    parser.add_argument('--right', type=Fraction)
    parser.add_argument('--modes', type=int, default=4)
    parser.add_argument('--primitive-nodes', type=int, default=512)
    parser.add_argument('--angles', type=int, default=1024)
    parser.add_argument('--bits', type=int, default=192)
    parser.add_argument('--native-order', type=int, default=32)
    parser.add_argument('--native-radius', type=Fraction, default=Fraction(1, 64))
    parser.add_argument('--outer-radius', type=Fraction, default=Fraction(3))
    parser.add_argument('--sample-radius', type=Fraction, default=Fraction(5, 4))
    parser.add_argument('--time-nodes', type=int, default=40)
    parser.add_argument('--time-terms', type=int, default=24)
    parser.add_argument('--flow-degree', type=int, default=32)
    parser.add_argument('--normalized-strip', type=Fraction, default=Fraction(1, 16))
    parser.add_argument('--momentum-scale', type=Fraction, default=Fraction(8))
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    ctx.prec, ctx.cap = args.bits, 4
    started, cpu = time.monotonic(), time.process_time()
    report = dict(kind='true_single_common_span_scaled_core_transfer', complete=False,
        source_sha256=sha(__file__), common_span_index=args.common_span,
        bits=args.bits, modes=args.modes,
        requested_exact_parameter_half_width=str(args.parameter_half_width),
        primitive_nodes=args.primitive_nodes, angular_nodes=args.angles,
        native_order=args.native_order, native_radius=str(args.native_radius),
        outer_radius=str(args.outer_radius), sample_radius=str(args.sample_radius),
        time_nodes=args.time_nodes, time_terms=args.time_terms, flow_degree=args.flow_degree,
        normalized_angular_strip=str(args.normalized_strip),
        momentum_scale=str(args.momentum_scale),
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_core_radial_taylor.py','fourfold_phase_core_waist_taylor.py',
            'fourfold_phase_core_parameter_taylor.py','fourfold_phase_beta_parameter_germ.py',
            'fourfold_native_series_fft.py',
            'fourfold_phase_beta_affine.py','fourfold_phase_beta_bulk_interval.py',
            'fourfold_phase_beta_bulk_box.py','fourfold_phase_beta_interval.py',
            'fourfold_phase_core_low_coefficients.py','fourfold_phase_actual_positive_cap.py')},
        scope='Actual finite projected generator and its transfer on precisely this one real interval. No complete half-core, core DN, omitted-channel solve, or full Schur inverse.')
    args.out.parent.mkdir(parents=True, exist_ok=True)
    def save():
        report.update(CPU_seconds=time.process_time()-cpu,
                      wall_seconds=time.monotonic()-started)
        args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    save()
    try:
        if args.parameter_half_width < 0:
            raise ValueError('negative parameter half-width')
        if args.parameter_half_width:
            target = ParameterCoreTarget(args.object, args.parameter_half_width,
                args.primitive_nodes, args.angles, arb('.003'), arb('.0025'), arb('.32'),
                native_order=args.native_order, native_radius=args.native_radius)
        else:
            target = WaistCoreTarget(args.object, args.primitive_nodes, args.angles,
                arb('.003'), arb('.0025'), arb('.32'),
                native_order=args.native_order, native_radius=args.native_radius)
        report.update({key:value for key, value in core_provenance(target, args.object).items()
                       if key not in ('source_sha256','dependency_sha256')})
        cuts = sorted({Fraction(0), Fraction(1, 4)}
            |{x for x in target.common_cells() if 0 < x < Fraction(1, 4)})
        if not 0 <= args.common_span < len(cuts)-1:
            raise ValueError('the common span index is absent')
        a, b = cuts[args.common_span:args.common_span+2]
        target.set_cell(a, b)
        left = a if args.left is None else args.left
        right = b if args.right is None else args.right
        report['exact_common_span'] = [str(a), str(b)]
        polynomial, transfer = local_flow(target, left, right, args.modes,
            exact_arb(args.normalized_strip), args.outer_radius, args.sample_radius,
            args.time_nodes, args.time_terms, args.flow_degree, args.momentum_scale,
            report, save)
        arrays = args.out.with_suffix('.npz')
        np.savez_compressed(arrays,
            exact_dyadic_generator_coefficients=polynomial,
            exact_dyadic_local_transfer_center=transfer)
        report.update(complete=True, arrays=dict(path=str(arrays), sha256=sha(arrays),
            bytes=arrays.stat().st_size))
    except Exception as exc:
        report.update(failure=repr(exc), traceback=traceback.format_exc())
    save()
    print(json.dumps({key:report.get(key) for key in (
        'complete','exact_common_span','true_scaled_local_transfer_operator_error',
        'failure','CPU_seconds','wall_seconds')}), flush=True)
    if not report['complete']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
