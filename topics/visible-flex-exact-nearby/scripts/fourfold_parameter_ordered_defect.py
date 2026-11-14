#!/usr/bin/env python3
"""R82 parameter budgets and signed finite chronological accumulation.

Inputs are true g0/gp/gpp approximations in one fixed reference coordinate.
Positive-frequency rows define negative modes by exact conjugacy. Frequencies
are those of the normalized label x: differentiation multiplies by i*k.
This module does not certify an input field, parameter box, or reference.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from flint import arb, acb, acb_poly, ctx

from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record


def _nonnegative(value, name):
    value = arb(value)
    if not value.is_finite() or not value >= 0:
        raise ValueError(name + ' must be finite and nonnegative')
    return value


def parameter_coordinate_budget(A, B1, B2, E0, E1, E2, radius,
                                integration_fees=(0, 0, 0)):
    """Directed R82 (82.8), (82.12)--(82.15), (82.20).

    radius is S-sigma. Every supplied majorant must cover its entire declared
    time/label/parameter domain; this algebra does not supply that premise.
    """
    A, B1, B2, E0, E1, E2 = [
        _nonnegative(v, n) for v, n in
        zip((A, B1, B2, E0, E1, E2), ('A', 'B1', 'B2', 'E0', 'E1', 'E2'))]
    R = arb(radius)
    if not R.is_finite() or not R > 0 or not 2*A < R:
        raise ValueError('R82 requires 0 <= 2*A < S-sigma')
    fees = [_nonnegative(v, 'integration fee') for v in integration_fees]
    if len(fees) != 3:
        raise ValueError('three integration fees required')
    d, e, denominator = R-A, arb(1).exp(), R**2*(1-2*A/R)
    tails = [A**3/(2*d**2), 4*e*A*A*B1/denominator,
             (4*e*A*A*B2 + 4*e*(2*e-1)*A*B1*B1)/denominator]
    source_errors = [E0*(1+A/R), E1+(A*E1+B1*E0)/R,
                     E2+(A*E2+2*B1*E1+B2*E0)/R]
    exponential = (A/d).exp()
    return dict(
        chronological_tails=[v.upper() for v in tails],
        source_transfer_errors=[v.upper() for v in source_errors],
        total_coordinate_errors=[(t+s+f).upper()
                                 for t, s, f in zip(tails, source_errors, fees)],
        true_first_parameter_modulus=(exponential*B1).upper(),
        true_second_parameter_modulus=(exponential*B2
                         +exponential*(2*exponential-1)*B1*B1/d).upper(),
        true_coordinate_displacement=A.upper(),
        finite_coordinate_displacement=(A+A*A/(2*R)+fees[0]).upper(),
        remaining_width=d.lower())


def endpoint_parameter_budget(coordinate_errors, Q0, Q1, Q2,
                              true_Z, true_W, finite_Z):
    """Physical Y -> normalized Gamma=4Y, exactly as R82 (82.22)."""
    b0, b1, b2 = [_nonnegative(v, 'coordinate error') for v in coordinate_errors]
    Q0, Q1, Q2, Z, W, Zh = [_nonnegative(v, 'endpoint bound') for v in
                            (Q0, Q1, Q2, true_Z, true_W, finite_Z)]
    return [(4*Q0*b0).upper(), (4*(Q1*b0*Z+Q0*b1)).upper(),
            (4*(Q2*b0*Z*Z+Q1*b1*(Z+Zh)+Q1*b0*W+Q0*b2)).upper()]


def _real_row(row):
    row = list(map(acb, row))
    if not row or any(not z.is_finite() for z in row):
        raise ValueError('nonempty finite positive-frequency row required')
    if not row[0].imag.contains(0):
        raise ValueError('zero Fourier mode violates the real-function contract')
    row[0] = acb(row[0].real)
    return row


def _source_rows(rows):
    rows = [_real_row(row) for row in rows]
    if not rows or any(len(row) != len(rows[0]) for row in rows):
        raise ValueError('rectangular time-by-positive-frequency source required')
    return rows


def row_norms(row, width):
    """Complete finite A_width norm and its x-derivative norm."""
    s = _nonnegative(width, 'label width')
    n, d = arb(0), arb(0)
    for k, value in enumerate(row):
        w = abs(value)*(1 if k == 0 else 2)*(k*s).exp()
        n += w
        d += k*w
    return n.upper(), d.upper()


def first_and_local_parameter_bounds(sources, width):
    """Keep all signed first integrals; bound the three entire local J_i.

    Uses the exact even/even endpoint term and the odd/even chronological
    brackets, not a product of global integral moduli. No local J is declared
    zero. The returned fees must be accumulated if its coefficients are omitted.
    """
    if len(sources) != 3:
        raise ValueError('g0, g1 and g2 required')
    sources = [_source_rows(source) for source in sources]
    m = max(map(len, sources))
    first, norms, derivatives = [], [], []
    for rows in sources:
        first.append([sum((2*rows[i][k]/(i+1) for i in range(0, len(rows), 2)), acb(0))
                      for k in range(len(rows[0]))])
        nd = [row_norms(row, width) for row in rows]
        norms.append([v[0] for v in nd]+[arb(0)]*(m-len(rows)))
        derivatives.append([v[1] for v in nd]+[arb(0)]*(m-len(rows)))
    endpoints = [row_norms(row, width) for row in first]

    def diagonal(i):
        value = endpoints[i][0]*endpoints[i][1]/2
        for even in range(0, m, 2):
            for odd in range(1, m, 2):
                w = arb(2)/((even+odd+2)*(even+1))
                value += w*(derivatives[i][odd]*norms[i][even]
                            +derivatives[i][even]*norms[i][odd])
        return value

    def symmetric(i, j):
        value = (endpoints[i][1]*endpoints[j][0]
                 +endpoints[j][1]*endpoints[i][0])/2
        for even in range(0, m, 2):
            for odd in range(1, m, 2):
                w = arb(2)/((even+odd+2)*(even+1))
                value += w*(derivatives[i][odd]*norms[j][even]
                            +derivatives[j][odd]*norms[i][even]
                            +derivatives[i][even]*norms[j][odd]
                            +derivatives[j][even]*norms[i][odd])
        return value

    fees = [diagonal(0), symmetric(0, 1), symmetric(0, 2)+2*diagonal(1)]
    return first, [v.upper() for v in fees]


def add_rows(*rows):
    n = max(map(len, rows))
    return _real_row([sum((row[k] for row in rows if k < len(row)), acb(0))
                      for k in range(n)])


def derivative_product(left, right):
    """Full finite positive-frequency coefficients of left_x * right."""
    left, right = _real_row(left), _real_row(right)
    k1, k2 = len(left)-1, len(right)-1
    a = [acb(0, k)*(left[-k].conjugate() if k < 0 else left[k])
         for k in range(-k1, k1+1)]
    b = [right[-k].conjugate() if k < 0 else right[k] for k in range(-k2, k2+1)]
    product = acb_poly(a)*acb_poly(b)
    offset = k1+k2
    return _real_row([product[offset+k] for k in range(offset+1)])


def advance_parameter_integrals(C, D, first, local_second=None):
    """R82 (82.17), using every old C_i before changing any accumulator.

    C,D,first contain three complete positive-frequency arrays. local_second
    may contain actual enclosed J0,J1,J2. If absent, all three local-J fees from
    first_and_local_parameter_bounds must be paid by the caller.
    """
    if any(len(v) != 3 for v in (C, D, first)):
        raise ValueError('three parameter orders required in every accumulator')
    C, D, first = [[_real_row(row) for row in data] for data in (C, D, first)]
    J = [[acb(0)] for _ in range(3)] if local_second is None else local_second
    if len(J) != 3:
        raise ValueError('three local chronological integrals required')
    newD = [add_rows(D[0], derivative_product(first[0], C[0]), J[0]),
            add_rows(D[1], derivative_product(first[1], C[0]),
                     derivative_product(first[0], C[1]), J[1]),
            add_rows(D[2], derivative_product(first[2], C[0]),
                     [2*z for z in derivative_product(first[1], C[1])],
                     derivative_product(first[0], C[2]), J[2])]
    return [add_rows(C[i], first[i]) for i in range(3)], newD


def exact_monomial_integral(power):
    return Fraction(0) if power % 2 else Fraction(2, power+1)


def chronological_weight(m, n):
    """Exact rational weight; handy for retaining full local mixed integrals."""
    if m < 0 or n < 0:
        raise ValueError('nonnegative polynomial exponents required')
    return (exact_monomial_integral(m+n+1)
            -(-1)**(n+1)*exact_monomial_integral(m))/(n+1)


def closed_flow_check():
    """Two noncommuting solvable flows: translation then sin(x) flow.

    tan(X/2)=exp(2*lambda*b)*tan((x+2*lambda*a)/2). Its first two
    lambda coefficients and both p derivatives are known independently.
    a=e*(1+2p+3p^2), b=e*(2-p+4p^2), p=0.
    """
    e = exact_arb(Fraction(1, 1024))
    a = [e, 2*e, 6*e]
    b = [2*e, -e, 8*e]
    constant = lambda v: [acb(v)]
    sine = lambda v: [acb(0), acb(0, -v/2)]
    zero = [[acb(0)] for _ in range(3)]
    C, D = advance_parameter_integrals(zero, zero, [constant(2*v) for v in a], zero)
    # J=2*b^2*sin(x)*cos(x)=b^2*sin(2x), with its exact p derivatives.
    jamp = [b[0]**2, 2*b[0]*b[1], 2*(b[1]**2+b[0]*b[2])]
    J = [[acb(0), acb(0), acb(0, -v/2)] for v in jamp]
    C, D = advance_parameter_integrals(C, D, [sine(2*v) for v in b], J)
    cross = [4*a[0]*b[0], 4*(a[1]*b[0]+a[0]*b[1]),
             4*(a[2]*b[0]+2*a[1]*b[1]+a[0]*b[2])]
    for i in range(3):
        expected_C = [acb(2*a[i]), acb(0, -b[i])]
        expected_D = [acb(0), acb(cross[i]/2), acb(0, -jamp[i]/2)]
        for row, expected in ((C[i], expected_C), (D[i], expected_D)):
            if len(row) != len(expected) or any(not z.contains(w) for z, w in zip(row, expected)):
                raise AssertionError('noncommuting exact-flow coefficient identity failed')
    first, fees = first_and_local_parameter_bounds([[sine(v)] for v in b], arb(0))
    for fee, row in zip(fees, J):
        if not fee >= row_norms(row, arb(0))[0]:
            raise AssertionError('full local mixed-integral fee failed')
    return dict(exact_noncommuting_flow_coefficients=True,
                first_and_second_parameter_orders=True,
                full_local_J_moduli_enclosed=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--closed-flow-check', action='store_true')
    parser.add_argument('--bits', type=int, default=192)
    args = parser.parse_args()
    ctx.prec = args.bits
    if not args.closed_flow_check:
        parser.error('import the budget/accumulator API, or use --closed-flow-check')
    print(json.dumps(closed_flow_check(), sort_keys=True))


if __name__ == '__main__':
    main()
