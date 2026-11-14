#!/usr/bin/env python3
"""Finite half-return prediction from one exact forward endpoint package.

This computes 4*Y_ref,end(x)-H5(x+d) for the two possible half-angle lifts.
It includes the complete symbolic Q_end*a product and all finite Fourier
modes. It excludes the true delta5 ODE defect and is not a half-conjugacy
certificate. The quadratic irrational D5 target is evaluated with Arb.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path
import time
from flint import arb, acb, acb_poly, ctx

from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_retarget_reference_segment_package import load_package
from fourfold_phase_actual_field_fourier_package import write_json


def laurent(positive):
    return [z.conjugate() for z in positive[:0:-1]] + positive


def endpoint(package):
    identity = package['metadata']['identity']
    documents = package['documents']
    arrays = package['arrays']
    base = documents['old_forward_reference']['document']
    if (identity['leg'] != 'forward'
            or identity['segment'] != base['segment_count'] - 1
            or identity['branch_sign'] != -1):
        raise ValueError('the last complete forward segment is required')
    last = package['metadata']['exact_time_rows'][-1]
    if (last['kind'] != 'rational_multiple_of_pi'
            or Fraction(int(last['numerator']), int(last['denominator'])) != Fraction(1, 2)):
        raise ValueError('the exact final endpoint must be +pi/2')
    U = [acb(arb(float(r)), arb(float(i)))
         for r, i in zip(arrays['base_real'][-1, 0], arrays['base_imag'][-1, 0])]
    Q = [acb(arb(float(r)), arb(float(i)))
         for r, i in zip(arrays['Q_real'][-1], arrays['Q_imag'][-1])]
    if (arrays['Q_real'][-1].tobytes() != arrays['forward_end_Q_real'].tobytes()
            or arrays['Q_imag'][-1].tobytes() != arrays['forward_end_Q_imag'].tobytes()):
        raise ValueError('last Q control differs from the full forward-end Q')
    initial = documents['initial_correction']['document']
    denominator = 2 ** int(initial['denominator_power_of_two'])
    a = [acb(arb(int(r)) / denominator, arb(int(i)) / denominator)
         for r, i in initial['nonnegative_integer_coefficients']]
    KQ, KA = len(Q)-1, len(a)-1
    product = acb_poly(laurent(Q)) * acb_poly(laurent(a))
    K = max(len(U)-1, KQ+KA)
    full = [acb(0) for _ in range(2*K+1)]
    for j in range(2*(KQ+KA)+1):
        full[j + K - KQ - KA] += product[j]
    for j, z in enumerate(laurent(U)):
        full[j + K - len(U) + 1] += z
    if not full[K].imag.contains(0):
        raise ValueError('exact endpoint lost reality')
    return [acb(full[K].real)] + full[K+1:]


def norm(positive, width, derivative=0):
    s = exact_arb(width)
    return sum(((1 if k == 0 else 2) * k**derivative * abs(z) * (k*s).exp()
                for k, z in enumerate(positive)), arb(0)).upper()


def grid_summary(positive, nodes):
    K = len(positive)-1
    folded = [acb(0) for _ in range(nodes)]
    for k in range(-K, K+1):
        folded[k % nodes] += positive[-k].conjugate() if k < 0 else positive[k]
    values = [nodes*z for z in acb.dft(folded, inverse=True)]
    if not all(z.imag.contains(0) for z in values):
        raise ValueError('real-label residual lost exact reality')
    maximum = max(abs(z.real).upper() for z in values)
    minimum = min(z.real.lower() for z in values)
    high = max(z.real.upper() for z in values)
    return dict(nodes=nodes, sampled_absolute_max_upper=ball_record(maximum),
                sampled_real_range=[ball_record(minimum), ball_record(high)],
                x_zero_value=ball_record(values[0].real),
                scope='Finite reference values only; the continuous A_s bounds are reported separately.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--package', type=Path,
        default=Path('data/phase_ring_continuation/step5_forward549_exact_reference_package.npz.gz'))
    parser.add_argument('--widths', default='0,1/512,1/256,1/128')
    parser.add_argument('--nodes', type=int, default=4096)
    parser.add_argument('--bits', type=int, default=256)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if args.nodes < 1 or args.bits < 192:
        raise ValueError('positive grid and at least 192 bits required')
    ctx.prec = args.bits
    started, cpu = time.monotonic(), time.process_time()
    package = load_package(args.package)
    H = package['documents']['target_H']['document']
    if H.get('source_metadata', {}).get('target') != 'D5':
        raise ValueError('this entry fixes the exact quadratic D5 rotation')
    divisor = 2 ** int(H['denominator_power_of_two'])
    h = [acb(arb(int(r))/divisor, arb(int(i))/divisor)
         for r, i in H['h_nonnegative_integer_coefficients']]
    Uend = endpoint(package)
    K = max(len(Uend), len(h))-1
    Uend += [acb(0)]*(K+1-len(Uend))
    h += [acb(0)]*(K+1-len(h))
    rho = (15121+arb(5).sqrt())/27422
    half_angle = arb.pi()*rho
    widths = list(map(Fraction, args.widths.split(',')))
    if any(s < 0 for s in widths):
        raise ValueError('nonnegative label widths required')
    cases = []
    for integer in [0, 1]:
        shift = half_angle + integer*arb.pi()
        residual = [4*Uend[k]-h[k]*(acb(0,k)*shift).exp() for k in range(K+1)]
        residual[0] -= shift
        if not residual[0].imag.contains(0):
            raise ValueError('mean residual lost reality')
        residual[0] = acb(residual[0].real)
        cases.append(dict(half_lift_integer=integer, shift=ball_record(shift),
            mean_residual=ball_record(residual[0].real),
            finite_prediction_error_A_norms={str(s): ball_record(norm(residual, s)) for s in widths},
            finite_prediction_derivative_A_norms={str(s): ball_record(norm(residual, s, 1)) for s in widths},
            sample=grid_summary(residual,args.nodes)))
    correct = cases[0]
    report = dict(kind='exact_finite_forward_endpoint_half_return_prediction',
        complete=True, source_sha256=sha(__file__), package_sha256=sha(args.package),
        identity=package['metadata']['identity'], bits=args.bits, Fourier_degree=K,
        dependency_sha256={name:sha(Path(__file__).parent/name) for name in [
            'fourfold_retarget_reference_segment_package.py','fourfold_phase_beta_bulk_interval.py']},
        target_rho_exact='(15121+sqrt(5))/27422', target_rho=ball_record(rho),
        full_rotation_angle=ball_record(2*half_angle),
        exact_lift_mean_advance_of_finite_reference=ball_record((4*Uend[0]).real),
        formula='4*Y_ref,end(x)-H5(x+d)=4*(U4f,end+Qf,end*a)(x)-d-h5(x+d)',
        all_symbolic_modes_retained=True, initial_reference_contract='Y_ref,start=H5/4 from the exact retarget definition',
        half_angle_candidates=cases,
        selected_half_lift_prediction_integer=0,
        prediction_selects_first_half_lift=bool(norm([4*Uend[k]-h[k]*(acb(0,k)*half_angle).exp()
                    -(half_angle if k==0 else 0) for k in range(K+1)], Fraction(0)) < arb.pi()/4),
        limitations=[
            'This is a rigorous finite-function bound, not a true half-return error.',
            'No true delta5 field defect or reference-coordinate correction is included.',
            'The finite Q retarget is not declared to be the actual variational Jacobian.',
            'A small full-return residual alone is not used to infer a half-return residual.',
            'Selecting the actual ODE lift ultimately requires its true forward-flow error bound.'
        ],wall_seconds=time.monotonic()-started,cpu_seconds=time.process_time()-cpu)
    write_json(args.out, report)
    print(json.dumps(dict(complete=True,degree=K,mean_advance=report['exact_lift_mean_advance_of_finite_reference'],
        half_angle=correct['shift'],finite_A_norms=correct['finite_prediction_error_A_norms'],
        alternate_mean=cases[1]['mean_residual'],report_sha256=sha(args.out)),ensure_ascii=False))


if __name__ == '__main__':
    main()

