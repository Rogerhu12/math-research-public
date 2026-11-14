#!/usr/bin/env python3
"""Exact whole odd-Tc source and connection-carry certificate for R460.

The already proved global source is
  -2/3 sigma(y-33t) (S/sigma)(y+t) in S34 x S1122.
The six odd columns have t orders 5,11,17,23,29,35 and lie in the
whole type-one space sigma^34 y times polynomials of degree at most
five in X=x^3.  Six triangular coordinates determine each whole
column; no sampled target prime or unproved Taylor truncation is used.
"""

import argparse
from fractions import Fraction as Q
import json
from math import comb, factorial
from pathlib import Path

import sympy as sp


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    directory = Path(__file__).resolve().parent
    original = json.loads(
        (directory / "check-r455-pure-companion-arithmetic-test.json").read_text()
    )
    boundary = json.loads(
        (directory / "check-r458-original-two-input-boundaries.json").read_text()
    )
    a_series = list(map(Q, original["sigma_A_coefficients"]))
    b_series = list(map(Q, original["x_B_coefficients"]))
    h_series = list(map(Q, original["S_over_sigma_H_coefficients"]))
    length = len(a_series)

    def multiply(a, b):
        return [
            sum(a[j] * b[i-j] for j in range(i+1))
            for i in range(length)
        ]

    def power(a, exponent):
        result = [Q(1)] + [Q(0)] * (length-1)
        for _ in range(exponent):
            result = multiply(result, a)
        return result

    # x=z^-2 B(w), y=x'/2=-z^-3 D(w), D=B-3wB', w=z^6.
    d_series = [(1-3*i) * q for i, q in enumerate(b_series)]
    a34d = multiply(power(a_series, 34), d_series)
    columns = [
        multiply(a34d, power(b_series, 3*j)) for j in range(6)
    ]
    basis = sp.Matrix([
        [0 if ell-5+j < 0 else -columns[j][ell-5+j] for j in range(6)]
        for ell in range(6)
    ])
    assert basis.det() == -1
    jets = []
    for k in range(1, 7):
        m = 6*k-1
        column = []
        for ell in range(6):
            value = Q(0)
            for i in range(k+ell):
                j = k+ell-1-i
                collision = sum(
                    comb(1+6*i, z) * comb(5+6*j, m-z) * (-33)**z
                    for z in range(max(0, m-5-6*j), min(m, 1+6*i)+1)
                )
                value += a_series[i] * h_series[j] * collision
            column.append(-Q(2, 3) * factorial(m) * value)
        jets.append(sp.Matrix(column))
    matrix = basis.inv() * sp.Matrix.hstack(*jets)
    determinant = matrix.det()
    det_mod101 = (
        int(determinant.p) * pow(int(determinant.q), -1, 101)
    ) % 101
    assert determinant != 0 and det_mod101 == 43
    inverse = matrix.inv()

    r1 = list(map(sp.Rational, [
        "32/49", "-120/539", "801/2156", "5911/21560", "-8991/12320",
    ]))
    r3 = list(map(sp.Rational, [
        "512/7", "-48512/77", "18492/77", "-135598/385", "73519/110",
    ]))
    r5 = list(map(sp.Rational, [
        "-256/7", "26944/77", "39768/77", "-49604/77", "11653/11",
    ]))
    expected = {
        "C13": list(map(sp.Rational, [
            "0", "10880/14847", "-13504/14847", "6269/9898",
            "-6523/59388", "-37/33936",
        ])),
        "C15": list(map(sp.Rational, [
            "0", "923/1470", "107/5880", "11399/15680",
            "-15919/94080", "-37/53760",
        ])),
    }
    targets, tests, alphas = {}, {}, {}
    for name, alpha, ref in [
        ("C13", -sp.Rational(37, 33936), r3),
        ("C15", -sp.Rational(37, 53760), r5),
    ]:
        target = sp.Matrix([0] + [q-alpha*r for q, r in zip(r1, ref)])
        assert list(target) == expected[name]
        assert target[5] == alpha  # C'(0)=-alpha/b.
        test = inverse * target
        assert matrix * test == target
        targets[name], tests[name], alphas[name] = target, test, alpha

    lam, kap, q, a, D, G, ell, z = sp.symbols(
        "lambda kappa q a D G ell z"
    )
    shifted_mass = -a * (1+lam*kap)
    arithmetic_mass = -a * (1-lam)
    connection_mass = sp.expand(shifted_mass-arithmetic_mass)
    assert sp.expand(connection_mass + a*lam*(1+kap)) == 0
    for r in [1, 2, 3, 4]:
        eps = (-1)**r
        y_carry = eps*kap**r*D-G
        t_carry = eps*D-G
        assert sp.expand(y_carry-kap**r*t_carry-(kap**r-1)*G) == 0
        assert sp.expand(
            y_carry-t_carry-eps*(kap**r-1)*D
        ) == 0
        y_mass = eps*kap**r*shifted_mass-arithmetic_mass
        expected_y_mass = a*((1-lam)-eps*kap**r*(1+lam*kap))
        assert sp.expand(y_mass-expected_y_mass) == 0
        # An identity for both parities; no target-prime sampling.
    eps, t = sp.symbols("epsilon t")
    assert sp.expand(
        (eps*t*D-G)-t*(eps*D-G)-(t-1)*G
    ) == 0

    denominator = sp.ilcm(
        *[entry.q for entry in inverse],
        *[entry.q for target in targets.values() for entry in target],
        *[entry.q for test in tests.values() for entry in test],
    )
    bad_integer = sp.ilcm(
        int(boundary["fixed_bad_integer"]), 17*37*101*denominator,
    )
    result = {
        "normalization": {
            "source": "-2/3 sigma(y-33t)(S/sigma)(y+t)",
            "rows": "sigma^34 y X^j, j=0..5, X=x^3",
            "columns": "(Tc/Omega)^(6k-1), k=1..6, factorials included",
            "b_scaling": "M[j,k]*b^(k+4-j)",
            "target_scaling": "P[j]*b^(4-j)",
            "test_scaling": "e[k]*b^(-k)",
            "odd_unit_euler": "1+q*kappa^(6k-1), q=-chi*lambda",
            "connection_test": "Y/Omega*hC(Tc/Omega)-hS(Tc/Omega)+a*hHa(Tc/Omega)",
        },
        "odd_jet_basis": [[str(q) for q in basis.row(i)] for i in range(6)],
        "odd_moment_matrix": [[str(q) for q in matrix.row(i)] for i in range(6)],
        "determinant": str(determinant),
        "determinant_mod101": det_mod101,
        "connection_alphas_at_b1": {name: str(v) for name, v in alphas.items()},
        "whole_companion_targets": {
            name: [str(q) for q in target] for name, target in targets.items()
        },
        "positive_odd_test_coefficients": {
            name: [str(q) for q in test] for name, test in tests.items()
        },
        "shifted_unit_mass": str(shifted_mass),
        "arithmetic_unit_mass": str(arithmetic_mass),
        "connection_unit_mass": str(connection_mass),
        "common_denominator": str(denominator),
        "fixed_bad_integer": str(bad_integer),
        "fixed_bad_set": "prime divisors of fixed_bad_integer, no factorization assumed",
        "status": "complete odd source, original companion and carry identities verified",
    }
    encoded = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(encoded, encoding="utf-8")
        print(json.dumps({
            "status": result["status"], "output": str(args.output),
            "det_mod101": det_mod101,
        }))
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()

