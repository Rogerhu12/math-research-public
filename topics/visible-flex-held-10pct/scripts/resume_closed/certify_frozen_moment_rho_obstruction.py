#!/usr/bin/env python3
"""R34: frozen old low moments force a negative rho at full circle homotopy.

The exact R32 mean-one base is used for every q in [.04,.0851].  R33 supplies
the same supported Riesz dual and its proved L2 norm.  A complete rational
Bernstein enclosure of its degree-24 cosine polynomial supplies a positive-
density dual obstruction.  No assertion concerns re-solved free low moments.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import sys
import time

import certify_protected_arc_curvature_dual as dual
from certify_protected_arc_curvature_dual import (
    point, add, sub, mul, scale, divide, neg, pi_interval, sincos, show)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def chebyshev(count):
    rows = [[1], [0, 1]]
    for degree in range(2, count+1):
        values = [0]*(degree+1)
        for k, value in enumerate(rows[-1]):
            values[k+1] += 2*value
        for k, value in enumerate(rows[-2]):
            values[k] -= value
        rows.append(values)
    return rows


def bernstein(coefficients, left, right):
    """Outward power-to-Bernstein conversion on one exact rational interval."""
    degree = len(coefficients)-1
    lp, hp = [point(1)], [point(1)]
    for _ in range(degree):
        lp.append(scale(lp[-1], left))
        hp.append(scale(hp[-1], right-left))
    powers = []
    for k in range(degree+1):
        value = point(0)
        for j in range(k, degree+1):
            value = add(value, scale(mul(coefficients[j], lp[j-k]), math.comb(j, k)))
        powers.append(mul(value, hp[k]))
    values = []
    for k in range(degree+1):
        value = point(0)
        for j in range(k+1):
            value = add(value, scale(powers[j], F(math.comb(k, j), math.comb(degree, j))))
        values.append(value)
    return min(v[0] for v in values), max(v[1] for v in values)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--r33-execution', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--cells', type=int, default=32)
    args = parser.parse_args()
    started = time.monotonic()
    prior = json.loads(args.r33_execution.read_text())
    record = prior['certificate']
    assert prior['result'] == 'R33' and prior['execution']['observed_exit_code'] == 0
    assert prior['source']['sha256'] == sha(dual.__file__)
    assert record['n'] == 3 and record['maximum_low_mode'] == 8
    assert F(record['protected_halfwidth']) == F(21, 100)
    z = tuple(F(x) for x in record['rational_dual'])
    moments = tuple(F(x) for x in record['exact_physical_binary64_moments'])
    linear = sum((x*y for x, y in zip(z, moments)), F(0))
    assert z == dual.DUAL and linear == F(record['exact_dual_linear_functional'])
    norm_square = tuple(F(x) for x in record['dual_quadratic'])
    assert norm_square[0] > 0 and norm_square[1] < 13**2 and linear > 144
    L = scale(pi_interval(), F(1, 3))
    d = sub(L, point(F(21, 100)))
    sine, cosine = sincos(d)
    determinant = add(d, mul(sine, cosine))
    beta_sum = point(0)
    for j, value in enumerate(z):
        k, factor = 3*j, (1 if j == 0 else 2)
        si, co = sincos(scale(d, k)) if k else (point(0), point(1))
        p = scale(co, F(factor, (1-k*k)**2))
        pp = scale(si, F(-factor*k, (1-k*k)**2))
        beta = divide(neg(add(mul(sine, p), mul(cosine, pp))), determinant)
        beta_sum = add(beta_sum, scale(beta, value))
    gamma = scale(beta_sum, 2)
    # w(t) = 2 sum(z_j beta_j) cos(t)
    #        + sum z_j s_j cos(3jt)/(1-9j^2).
    # Hence w is a literal degree-24 polynomial in x=cos(t).
    polynomials = chebyshev(24)
    exact = [F(0)]*25
    for j, value in enumerate(z):
        amplitude = value*F(1 if j == 0 else 2, 1-9*j*j)
        for k, coefficient in enumerate(polynomials[3*j]):
            exact[k] += amplitude*coefficient
    coefficients = [point(value) for value in exact]
    coefficients[1] = add(coefficients[1], gamma)
    left = cosine[0]
    assert left > 0 and args.cells > 0
    rows = []
    for i in range(args.cells):
        lo = left+(1-left)*F(i, args.cells)
        hi = left+(1-left)*F(i+1, args.cells)
        rows.append(bernstein(coefficients, lo, hi))
    full = min(F(0), min(r[0] for r in rows)), max(F(0), max(r[1] for r in rows))
    assert full[1] < 100
    # True R32 beta=-I/(L-mass).  Taylor cos(y)>=1-y^2/2 and 0<=chi<=1
    # give I<=36*(a+b)^2*mass, enough for the deliberately coarse -1<beta<0.
    mass, transition_end = F(1, 4), F(29, 100)
    integral_upper = 36*transition_end**2*mass
    assert integral_upper/(L[0]-mass) < 1
    qinterval = F(1, 25), F(851, 10000)
    rho0 = 1-9*qinterval[1], 1+8*qinterval[1]
    assert 0 < rho0[0] <= rho0[1] < 2
    # The proof uses ||rho0||_2<2 and ||w||_2<13.  A nonnegative density
    # with mean one would also satisfy <rho,w><100, contradicting >118.
    required_lower = linear-26
    assert required_lower > 118 and required_lower > full[1]
    result = dict(
        scope=__doc__, command=sys.argv,
        source_sha256={Path(__file__).name: sha(__file__), Path(dual.__file__).name: sha(dual.__file__)},
        r33_execution_sha256=sha(args.r33_execution), input_checkpoint_sha256=record['checkpoint_sha256'],
        exact_frozen_moments=[str(x) for x in moments], rational_dual=[str(x) for x in z],
        q_interval=[str(x) for x in qinterval], exact_circle_homotopy='1',
        true_base='R32: 1+q*(8 chi+(1-chi)*(8 cos(3x)+beta)); beta is the exact mean correction',
        beta_coarse_absolute_upper=str(integral_upper/(L[0]-mass)),
        true_rho0_range=[str(x) for x in rho0], true_rho0_l2_strict_upper='2',
        exact_dual_linear_functional=str(linear), dual_l2_square_enclosure=show(norm_square),
        dual_l2_strict_upper='13', complement_half_length=show(d),
        cosine_domain=[str(left), '1'], power_degree=24, bernstein_cells=args.cells,
        full_period_dual_weight_enclosure=show(full), dual_weight_strict_upper='100',
        required_density_dual_integral_strict_lower=str(required_lower),
        required_density_dual_integral_lower_display=dual.decimal(required_lower),
        hypothetical_nonnegative_density_dual_integral_strict_upper='100',
        contradiction_strict_margin=str(required_lower-100),
        conclusion='Every C4 even/C3 support control with these frozen seven low moments and the protected open arc has rho<0 somewhere at lambda=1 for every q in the stated interval.',
        limitations='Only the frozen old seven moments; no exclusion of free re-solved controls, the raw path, full actual BVP existence, or the research target.',
        cell_enclosures=[show(v) for v in rows],
        arithmetic='R33 exact rational outward operations; Chebyshev identity and Bernstein convex hull, with full interval coverage',
        seconds=time.monotonic()-started)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({key: result[key] for key in (
        'full_period_dual_weight_enclosure', 'required_density_dual_integral_lower_display',
        'hypothetical_nonnegative_density_dual_integral_strict_upper', 'seconds')}), flush=True)


if __name__ == '__main__':
    main()
