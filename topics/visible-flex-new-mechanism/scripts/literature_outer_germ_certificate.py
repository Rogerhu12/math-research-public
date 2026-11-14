#!/usr/bin/env python3
"""Exact finite algebra for the analytic fourth-order endpoint germ.

No geometry, optimization, or numerical ODE is evaluated.  The accompanying
note supplies the analytic existence proof; this file checks its universal
Euler polynomial and its nonresonant recurrence denominators.
"""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path

from literature_internal_phase_certificate import (
    add, multiply, scale, coefficient,
)


def certificate():
    # D_j(theta)=(theta+4)...(theta+5-j), q=t^4 v.
    operators = [[F(1)]]
    for j in range(1, 5):
        operators.append(multiply(operators[-1], [F(5-j), F(1)]))
    d1, d2, d3, d4 = operators[1:]
    # After dividing the inward-coordinate Q by t^3, the leading expression
    # is c0/7*(30 D1(v)D4(v)-14 D2(v)D4(v)-14 D3(v)^2
    #             +32 D2(v)D3(v)).  Normalize c0=A=1 for this algebra.
    constant = (30*d1[0]*d4[0]-14*d2[0]*d4[0]
                -14*d3[0]*d3[0]+32*d2[0]*d3[0])/7
    assert constant == 0
    linearized = scale(add(
        scale(add(scale(d4, d1[0]), scale(d1, d4[0])), 30),
        scale(add(scale(d4, d2[0]), scale(d2, d4[0])), -14),
        scale(d3, -28*d3[0]),
        scale(add(scale(d3, d2[0]), scale(d2, d3[0])), 32),
    ), F(1, 7))
    indicial = multiply(multiply([F(0), F(1)], [F(8), F(1)]),
                        multiply([F(4), F(1)], [F(4), F(1)]))
    expected = scale(indicial, F(-48, 7))
    assert linearized == expected
    assert indicial == list(map(F, [0, 128, 80, 16, 1]))
    highest_coefficient = (30*d1[0]-14*d2[0])/7
    assert highest_coefficient == F(-48, 7)
    denominators = []
    for n in range(1, 17):
        actual = sum(coefficient(linearized, j)*n**j
                     for j in range(len(linearized)))
        wanted = F(-48, 7)*n*(n+4)**2*(n+8)
        assert actual == wanted and actual != 0
        denominators.append(dict(degree=n, exact=str(actual)))
    return dict(
        schema="literature-analytic-outer-germ-exact-certificate-v1",
        arithmetic="fractions.Fraction",
        normalized_amplitude="1", normalized_inward_C_derivative="1",
        euler_operators_low_to_high=[list(map(str, p)) for p in operators],
        leading_constant=str(constant),
        highest_euler_derivative_coefficient=str(highest_coefficient),
        linearized_polynomial_low_to_high=list(map(str, linearized)),
        monic_indicial_polynomial_low_to_high=list(map(str, indicial)),
        characteristic_roots=["0", "-4", "-4", "-8"],
        positive_integer_recurrence_denominators=denominators,
        sign_convention="t increases inward; c0=dC/dt at the endpoint",
        no_geometry_or_numerical_research_evaluated=True,
        global_profile_constructed=False, geometric_base_realized=False,
        finite_flex_proved=False,
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    body = json.dumps(certificate(), indent=2)+"\n"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(body)
    print(body)


if __name__ == "__main__":
    main()
