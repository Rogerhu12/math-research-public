#!/usr/bin/env python3
"""Exact finite algebra for the D=0 sign-changing phase-opening seed.

This certificate does not integrate an ODE or optimize a geometric base.
The real analytic germ and the nonlinear complex branch are proved in the
accompanying note.  All formal coefficients below are exact Fractions.
"""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path

from literature_internal_phase_certificate import (
    add, scale, multiply, derivative, coefficient,
)


C = [F(0), F(1), F(1)]
W = [F(-55, 32)]
A1 = [F(-8, 3)]
A2 = [F(87, 32), F(2)]
BASE_JETS = [F(1), F(128, 261), F(-8192, 43065), F(524288, 5038605)]


def L(q):
    return add(multiply(A1, q), scale(multiply(A2, derivative(q)), 2),
               scale(multiply(C, derivative(q, 2)), -2))


def Q(q):
    ll, q3 = L(q), derivative(q, 3)
    return add(multiply(ll, derivative(q, 4)),
               scale(multiply(derivative(ll), q3), 2),
               scale(multiply(C, multiply(q3, q3)), 2))


def shift_polynomial(p, shift):
    answer = [F(0)]
    power = [F(1)]
    for value in p:
        answer = add(answer, scale(power, value))
        power = multiply(power, [F(shift), F(1)])
    return answer


def certificate(order=12):
    assert order >= 4
    p0, p1, p2, r0, r1, s0, s1, t0, t1 = (
        F(-8, 3), F(0), F(0), F(0), F(87, 32),
        F(-55, 32), F(2, 3), F(-1, 3), F(0))
    D = p0/2+s1-2*t0
    assert D == 0
    B0, B1, B2 = [r0, r1, -p0/4], [s0, s1, -p1/4], [t0, t1, -p2/4]
    reconstructed_C = add(B0, multiply([F(0), F(1)], B1),
                          multiply([F(0), F(0), F(1)], B2))
    reconstructed_W = add(B1, scale(multiply([F(0), F(1)], B2), 2))
    assert reconstructed_C == C and reconstructed_W == W
    assert add(derivative(C), scale(W, -1)) == A2
    determinant = r0*(s1*(-p2/4)-t1*(-p1/4)) \
        -s0*(r1*(-p2/4)-t1*(-p0/4)) \
        +t0*(r1*(-p1/4)-s1*(-p0/4))
    assert determinant == F(4, 27)

    _, a, b, c = BASE_JETS
    assert -F(8, 3)+F(87, 16)*a == 0
    assert F(4, 3)*a+F(55, 16)*b == 0
    assert F(4, 3)*b+F(39, 16)*c == 0
    ell = -c/2
    q = [F(1), a, b/2, c/6]
    denominators = []
    for n in range(4, order+1):
        residual = coefficient(Q(q+[F(0)]), n-2)
        slope = coefficient(Q(q+[F(1)]), n-2)-residual
        expected = ell*n*(n-1)*(n-F(9, 2))*(n+F(7, 2))
        assert slope == expected and slope != 0
        q.append(-residual/slope)
        denominators.append(dict(degree=n, slope=str(slope)))
    assert q[4] == F(4, 135)*c
    ll, qq = L(q), Q(q)
    assert coefficient(ll, 0) == coefficient(ll, 1) == 0
    assert coefficient(ll, 2) == ell
    assert all(coefficient(qq, j) == 0 for j in range(order-1))

    falling = [[F(1)]]
    for j in range(4):
        falling.append(multiply(falling[-1], [F(-j), F(1)]))
    indicial = add(falling[4], scale(falling[3], 4),
                   scale(falling[2], F(-55, 4)))
    expected = multiply(multiply([F(0), F(1)], [F(-1), F(1)]),
                        multiply([F(-9, 2), F(1)], [F(7, 2), F(1)]))
    assert indicial == expected
    base_euler = shift_polynomial(indicial, 4)
    phase_euler = shift_polynomial(indicial, F(9, 2))
    assert base_euler == list(map(F, [-45, F(231, 4), F(229, 4), 14, 1]))
    assert coefficient(phase_euler, 0) == 0
    return dict(
        schema="literature-D0-sign-changing-phase-exact-certificate-v1",
        arithmetic="fractions.Fraction",
        no_geometry_optimization_or_numerical_ode=True,
        coefficient_order=["p0", "p1", "p2", "r0", "r1", "s0", "s1", "t0", "t1"],
        coefficients=list(map(str, [p0, p1, p2, r0, r1, s0, s1, t0, t1])),
        D=str(D), B_determinant=str(determinant),
        fixed_base_jets=list(map(str, BASE_JETS)),
        L_second_coefficient=str(ell), fourth_base_derivative=str(24*q[4]),
        formal_base_coefficients=list(map(str, q)),
        recurrence_denominators=denominators,
        Q_zero_through_degree=order-2,
        transverse_indicial_polynomial=list(map(str, indicial)),
        base_euler_polynomial=list(map(str, base_euler)),
        phase_euler_polynomial=list(map(str, phase_euler)),
        analytic_base_euler_spectrum=["-4", "-3", "1/2", "-15/2"],
        transverse_indicial_roots=["0", "1", "9/2", "-7/2"],
        fixed_phase_amplitude_euler_spectrum=["0", "-9/2", "-7/2", "-8"],
        geometric_base_realized=False, global_profile_matched=False,
        finite_flex_proved=False,
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--order", type=int, default=12)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    body = json.dumps(certificate(args.order), indent=2)+"\n"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(body)
    print(body)


if __name__ == "__main__":
    main()
