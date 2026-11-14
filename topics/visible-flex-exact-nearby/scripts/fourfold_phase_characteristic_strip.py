#!/usr/bin/env python3
"""Directed complex-angle denominator gate for a frozen real R33 graph.

Uses an already certified continuous real N upper bound and the fact that
the first vertical Taylor term of a real analytic function is imaginary.
No complex FFT, sampled complex minimum, or area square-root branch is used.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

from fourfold_interval_scalar import interval_exp
from fourfold_phase_root_interval import Box
from fourfold_phase_core_interval import CoreTarget
from fourfold_phase_uniform_tail import (
    exact_iv, endpoint_up, exp_up, weighted_sum_up,
    add_up, mul_up, power_up, up, down,
)


def product(*values):
    answer = 1.
    for value in values:
        answer = mul_up(answer, value)
    return float(answer)


def total(*values):
    answer = 0.
    for value in values:
        answer = add_up(answer, value)
    return float(answer)


def hyperbolic_weights(width, modes):
    cosh, sinh = [], []
    for m in 4*np.arange(1, modes+1):
        v = exact_iv(width)*int(m)
        ep, em = interval_exp(v), interval_exp(-v)
        cosh.append(endpoint_up((ep+em)/2))
        sinh.append(endpoint_up((ep-em)/2))
    return np.array(cosh), np.array(sinh)


def strip_cell(beta, gamma, radius, real_x_norm, real_n_upper, width, weights):
    """All coefficients are real-radial interval jets of the exact object."""
    b, g = beta.abs_upper(), gamma.abs_upper()
    frequency = 4*np.arange(1, b.shape[-1]+1)
    cosh, sinh = weights

    def angular(radial, order):
        w = mul_up(power_up(frequency, order), cosh)
        return total(weighted_sum_up(b[radial], w),
                     weighted_sum_up(g[radial], w))

    imaginary_phase = total(width, weighted_sum_up(b[0], sinh),
                            weighted_sum_up(g[0], sinh))
    exponential = float(exp_up(imaginary_phase))
    p1, p2, p3 = total(1., angular(0, 1)), angular(0, 2), angular(0, 3)
    r0, r1 = angular(1, 0), angular(1, 1)
    t0 = exponential
    t1 = product(t0, p1)
    t2 = product(t0, total(p2, product(p1, p1)))
    t3 = product(t0, total(p3, product(3., p1, p2), product(p1, p1, p1)))
    tx = product(t0, r0)
    tx1 = product(t0, total(r1, product(r0, p1)))
    a, ap = float(radius[0].abs_upper()), float(radius[1].abs_upper())
    x_theta = total(product(ap, t0), product(a, tx))
    x_complex = total(real_x_norm, product(width, x_theta))
    # n=a^2(T cross X).Ttheta, X=Fx. Its second angular derivative:
    # a^3(T cross Tx_theta).Ttheta + 2a^3(T cross Tx).Ttheta2
    # + a^2(Ttheta cross X).Ttheta2 + a^2(T cross X).Ttheta3.
    n2 = product(a, a, total(product(a, t0, tx1, t1),
                            product(2., a, t0, tx, t2),
                            product(x_complex, t1, t2),
                            product(x_complex, t0, t3)))
    real_part_loss = product(.5, width, width, n2)
    real_part_upper = float(up(real_n_upper+real_part_loss))
    result = dict(real_Nraw_upper=float(real_n_upper),
                  real_Fx_norm_upper=float(real_x_norm),
                  radius_upper=a, imaginary_phase_upper=imaginary_phase,
                  T_norm_upper=t0, Ttheta_norm_upper=t1,
                  Ttheta2_norm_upper=t2, Ttheta3_norm_upper=t3,
                  Tx_norm_upper=tx, Tx_theta_norm_upper=tx1,
                  Fx_strip_norm_upper=x_complex,
                  Nraw_theta2_strip_norm_upper=n2,
                  Nraw_real_part_loss_upper=real_part_loss,
                  Nraw_real_part_upper=real_part_upper,
                  passed=bool(real_part_upper < 0))
    if not result['passed']:
        return result
    # For complex arguments all dot products are bilinear. Area squared is
    # G=(aT cross X).(aT cross X), not a Hermitian norm.
    denominator = float(down(-real_part_upper))
    m0 = product(a, a, t0, x_complex, tx)
    m1 = product(a, a, x_complex, total(product(t1, tx), product(t0, tx1)))
    g0 = product(a, a, t0, t0, x_complex, x_complex)
    g1 = product(2., a, a, t0, x_complex,
                 total(product(t1, x_complex), product(a, t0, tx)))
    n1 = product(a, a, total(product(a, t0, tx, t1),
                            product(t0, x_complex, t2)))
    # v_sigma = -Mraw/Nraw - sigma sqrt(-K0) G/Nraw. K0 is radial.
    inv = float(up(1./denominator))
    result.update(Nraw_modulus_lower=denominator, Mraw_strip_norm_upper=m0,
                  Mraw_theta_strip_norm_upper=m1,
                  G_strip_norm_upper=g0, G_theta_strip_norm_upper=g1,
                  Nraw_theta_strip_norm_upper=n1,
                  drift_norm_upper=product(m0, inv),
                  wave_factor_norm_upper=product(g0, inv),
                  drift_theta_norm_upper=total(product(m1, inv),
                                               product(m0, n1, inv, inv)),
                  wave_factor_theta_norm_upper=total(product(g1, inv),
                                                     product(g0, n1, inv, inv)))
    return result


def load_real_rows(report):
    if report.get('kind') == 'continuous_symmetric_infinite_R33_core_N_and_support_intervals':
        if not report['complete'] or report['pending'] or report['failed_cells']:
            raise ValueError('a complete continuous real certificate is required')
        sha = report['configuration']['inputs_sha256']
        rows = [(r['radial_interval'], r['raw_N_upper'], r['Fx_norm_upper'])
                for r in report['cells']]
        right = report['radial_core'][1]
    elif report.get('kind') == 'directed_continuous_core_N_gate_for_explicitly_symmetric_infinite_R33':
        if report['status'] != 'complete' or report['pending'] or report['failures']:
            raise ValueError('a complete continuous real certificate is required')
        sha = report['inputs_sha256']
        rows = [(r['interval'], -r['raw_minus_n_lower'],
                 total(r['Fx_horizontal_upper'], r['Fx_z_abs_upper']))
                for r in report['rows']]
        right = report['core'][1]
    else:
        raise ValueError('unsupported real certificate object; do not silently transfer a gate')
    if rows[0][0][0] != 0 or rows[-1][0][1] != right:
        raise ValueError('wrong endpoints')
    if any(a[0][1] != b[0][0] for a, b in zip(rows, rows[1:])):
        raise ValueError('radial coverage gap')
    return sha, right, rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inputs', type=Path, required=True)
    parser.add_argument('--real-certificate', type=Path, required=True)
    parser.add_argument('--width', type=float, default=1/1024)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if not 0 < args.width <= .02:
        raise ValueError('width must be positive and at most .02')
    real = json.loads(args.real_certificate.read_text())
    sha, right, real_rows = load_real_rows(real)
    if sha != hashlib.sha256(args.inputs.read_bytes()).hexdigest():
        raise ValueError('real N certificate belongs to a different exact object')
    with np.load(args.inputs, allow_pickle=False) as stored:
        frozen = {key:stored[key].copy() for key in stored.files}
    target = CoreTarget(frozen, 256, 256)
    weights = hyperbolic_weights(args.width, target.modes)
    rows = []
    for index, (interval, real_n, real_x) in enumerate(real_rows):
        beta, gamma, radius, slope = target.scalars(Box(*interval))
        row = strip_cell(beta, gamma, radius, real_x, real_n, args.width, weights)
        row['radial_interval'] = interval
        rows.append(row)
        if (index+1) % 50 == 0:
            print(json.dumps(dict(covered=index+1,total=len(real_rows),
                                  failed=sum(not r['passed'] for r in rows))),flush=True)
    report = dict(kind='continuous_complex_angle_Nraw_gate_for_explicitly_symmetric_infinite_R33',
        inputs_sha256=sha,
        real_certificate_sha256=hashlib.sha256(args.real_certificate.read_bytes()).hexdigest(),
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        dependency_sha256={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
            for name in ['fourfold_phase_core_interval.py','fourfold_phase_root_interval.py',
                         'fourfold_phase_uniform_tail.py','fourfold_interval_scalar.py']},
        radial_core=[-right,right], angular_strip_width=args.width,
        angular_coordinate='physical theta; the x=4theta circle strip is four times this width',
        cells=rows, cell_count=len(rows),
        all_passed=all(r['passed'] for r in rows),
        maximum_Nraw_real_part_upper=max(r['Nraw_real_part_upper'] for r in rows),
        limitations=['The exact same symmetrized input as the real certificate; no Gaussian or finite primitive replacement',
                     'Real radial variable only; not a complex radial domain or parameter tube',
                     'Does not certify a return map integration, conjugacy error, or full PDE inverse',
                     'Bilinear analytic G=C dot C is used; no complex norm or unselected square-root branch'])
    if report['all_passed']:
        for key in ['drift_norm_upper','wave_factor_norm_upper',
                    'drift_theta_norm_upper','wave_factor_theta_norm_upper']:
            report['maximum_'+key]=max(r[key] for r in rows)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='cells'},indent=2),flush=True)
    if not report['all_passed']:
        raise SystemExit('the proposed complex strip failed; preserve this diagnostic')


if __name__ == '__main__':
    main()
