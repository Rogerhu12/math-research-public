#!/usr/bin/env python3
"""Exact whole-source coefficient certificate for R455.

The source -2/3 sigma(y-33t)(S/sigma)(y+t) is globally in
S34 x S1122.  Its first-axis invariant subspace has dimension six;
the six Taylor coordinates used below are an exact triangular basis,
not a sampled approximation to an unspecified function.
"""

import argparse
from fractions import Fraction as F
import json
import math
from pathlib import Path

import sympy as sp


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    length = 12

    def multiply(a, b):
        out = [F(0)] * length
        for i, ai in enumerate(a[:length]):
            for j, bj in enumerate(b[:length-i]):
                out[i+j] += ai * bj
        return out

    def power(a, exponent):
        out = [F(1)] + [F(0)] * (length-1)
        for _ in range(exponent):
            out = multiply(out, a)
        return out

    # x(z)=z^-2 B(z^6), sigma(z)=z A(z^6), b=1.
    b_series = [F(0)] * length
    b_series[0], b_series[1] = F(1), F(-1, 7)
    for n in range(2, length):
        b_series[n] = sum(b_series[i] * b_series[n-i] for i in range(1, n)) / (
            (6*n+1) * (n-1)
        )
    log_a = [F(0)] + [
        -b_series[n] / (6*n*(6*n-1)) for n in range(1, length)
    ]
    a_series = [F(0)] * length
    a_series[0] = F(1)
    for n in range(1, length):
        a_series[n] = sum(k*log_a[k]*a_series[n-k] for k in range(1, n+1)) / n

    p_s = [F(-128, 7), F(-80, 7), F(-12, 7), F(-53, 7), F(1)]
    a33, a34 = power(a_series, 33), power(a_series, 34)
    b_powers = {j: power(b_series, j) for j in [2, 5, 8, 11, 14, 17]}

    # (S/sigma)(z)=z^5 H(z^6).
    h_series = [F(0)] * length
    for a in range(5):
        column = multiply(a33, b_powers[2+3*a])
        for n in range(4-a, length):
            h_series[n] += p_s[a] * column[n-4+a]
    assert h_series[0] == 1

    basis_coeffs = {a: multiply(a34, b_powers[2+3*a]) for a in range(6)}
    jet_basis = sp.Matrix([
        [F(0) if ell-5+a < 0 else basis_coeffs[a][ell-5+a] for a in range(6)]
        for ell in range(6)
    ])
    assert jet_basis.det() == -1
    inverse_jets = jet_basis.inv()

    def moment_jets(k):
        out = []
        for ell in range(6):
            total = 6*(k+ell)
            coefficient = F(0)
            for i in range(length):
                r = 1+6*i
                s = total-r
                if s < 5 or (s-5) % 6:
                    continue
                j = (s-5)//6
                if j >= length:
                    continue
                binomial = sum(
                    math.comb(r, a) * math.comb(s, 6*k-a) * (-33)**a
                    for a in range(max(0, 6*k-s), min(r, 6*k)+1)
                )
                coefficient += a_series[i] * h_series[j] * binomial
            out.append(-F(2, 3) * math.factorial(6*k) * coefficient)
        return sp.Matrix(out)

    matrix = sp.Matrix.hstack(*[inverse_jets * moment_jets(k) for k in range(7)])
    target = sp.Matrix(p_s + [F(0)])
    assert matrix[:, 0] == -sp.Rational(2, 3) * target
    expected_tc6 = sp.Matrix([
        -85896216576, -sp.Rational(402567874560, 7),
        sp.Rational(295133363712, 7), sp.Rational(166501438848, 7),
        -12258012096, 15840,
    ])
    assert matrix[:, 1] == expected_tc6
    positive = matrix[:, 1:]
    determinant = positive.det()
    assert determinant.q == 1 and int(determinant) % 101 == 61
    coefficients = positive.inv() * target
    assert positive * coefficients == target

    # Complete fifth-order logarithm and test collision.  The fifth
    # moment of the true Z marginal -2/3(S/sigma) is -80 Omega^5.
    nonlog_coefficients, log_coefficients = [], []
    residue = sp.Rational(0)
    for k in range(1, 7):
        m = 6*k
        collision = sum(
            F((-1)**(a-1), a) * math.comb(m, 5-a) * (-33)**(m-5+a)
            for a in range(1, 6)
        )
        alpha_k = sp.factor(-80 * coefficients[k-1] * collision)
        beta_k = sp.factor(-80 * coefficients[k-1]
                          * math.comb(m, 5) * (-33)**(m-5))
        sigma_moment = F(math.factorial(m-5)) * a_series[k-1]
        residue += alpha_k * sigma_moment
        nonlog_coefficients.append(alpha_k)
        log_coefficients.append(beta_k)
    residue = sp.factor(residue)
    expected_residue = -sp.Rational(
        135188347596868709906380397884740707393526598671052246381035814315,
        13559034699200566332243539122188477010090222459025420929220870144,
    )
    assert residue == expected_residue and residue != 0

    common_denominator = sp.ilcm(*[c.q for c in coefficients], residue.q)
    bad_integer = 17 * common_denominator * abs(residue.p)

    def mod101(q):
        q = sp.Rational(q)
        return (int(q.p) * pow(int(q.q), -1, 101)) % 101

    result = {
        "normalization": {
            "source": "-2/3 sigma(y-33t)(S/sigma)(y+t)",
            "rows": "sigma^34 x^(2+3a), a=0..5",
            "columns": "(Tc/Omega)^(6k), k=0..6, all factorials included",
            "b_scaling": "column k, row a is b^(k+4-a) times the b=1 entry",
            "test": "sum_{k=1}^6 c_k b^(-k)(Tc/Omega)^(6k)",
        },
        "sigma_A_coefficients": [str(q) for q in a_series],
        "x_B_coefficients": [str(q) for q in b_series],
        "S_over_sigma_H_coefficients": [str(q) for q in h_series],
        "jet_basis": [[str(q) for q in jet_basis.row(i)] for i in range(6)],
        "moment_matrix": [[str(q) for q in matrix.row(i)] for i in range(6)],
        "positive_matrix_mod101": [[mod101(q) for q in positive.row(i)] for i in range(6)],
        "positive_determinant": str(determinant),
        "positive_determinant_mod101": 61,
        "test_coefficients": [str(c) for c in coefficients],
        "test_numerators": [int(c.p) for c in coefficients],
        "test_denominators": [int(c.q) for c in coefficients],
        "nonlog_fifth_coefficients": [str(q) for q in nonlog_coefficients],
        "log_fifth_coefficients": [str(q) for q in log_coefficients],
        "fifth_residue_alpha": str(residue),
        "common_denominator": str(common_denominator),
        "fixed_bad_integer": str(bad_integer),
        "fixed_bad_set": "prime divisors of fixed_bad_integer; no factorization assumption",
    }
    encoded = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(encoded, encoding="utf-8")
        print(json.dumps({"status": "exact whole-source and fifth-jet identities verified",
                          "output": str(args.output), "det_mod101": 61,
                          "fifth_residue_alpha": str(residue)}))
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
