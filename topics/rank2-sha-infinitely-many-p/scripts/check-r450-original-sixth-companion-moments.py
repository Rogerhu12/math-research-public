#!/usr/bin/env python3
"""Exact characteristic-zero certificate for R450.

Reconstructs all seven sixth-moment columns of the actual retained-sigma
source Phi_0.  No point sampling, target-prime search, or imported matrix is
used.  The finite covariant Taylor identity is valid as a whole function of
the first elliptic variable.  Run with --output to save the exact JSON.
"""

import argparse
import json
from pathlib import Path

import sympy as sp


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    x, ell_y, v, u = sp.symbols("x ell_y v u")

    def reduce_elliptic(poly):
        return sp.rem(
            sp.Poly(sp.expand(poly), ell_y),
            sp.Poly(ell_y**2 - x**3 - 1, ell_y),
        ).as_expr().expand()

    def deriv(poly):
        return reduce_elliptic(
            2 * ell_y * sp.diff(poly, x) + 3 * x**2 * sp.diff(poly, ell_y)
        )

    p_s = x**2 * (
        x**12 - sp.Rational(53, 7) * x**9
        - sp.Rational(12, 7) * x**6 - sp.Rational(80, 7) * x**3
        - sp.Rational(128, 7)
    )
    p_c = x * (x**3 + 1) * (x**3 - 8) * (
        x**9 - 30 * x**6 - 144 * x**3 - 32
    )
    zeta_derivs = {
        2: -x, 3: -2 * ell_y, 4: -6 * x**2,
        5: -24 * x * ell_y, 6: -24 * (5 * x**3 + 2),
    }
    # The omitted k=1 term is identically zero: 34*9 - 280 - 26 = 0.
    exponent = {
        k: sp.expand(zeta_derivs[k] * (
            34 * (9 * u)**k + (-v - 280 * u)**k - (-v + 26 * u)**k
        ) / sp.factorial(k))
        for k in range(2, 7)
    }
    e = exponent
    exp_coeff = {
        0: sp.Integer(1), 1: sp.Integer(0), 2: e[2], 3: e[3],
        4: e[4] + e[2]**2 / 2,
        5: e[5] + e[2] * e[3],
        6: e[6] + e[2] * e[4] + e[3]**2 / 2 + e[2]**3 / 6,
    }
    d_s = [p_s]
    for _ in range(6):
        d_s.append(deriv(d_s[-1]))
    sixth = sum(
        exp_coeff[6-k] * (9*u)**k * d_s[k] / sp.factorial(k)
        for k in range(7)
    )
    sixth -= sp.Rational(156, 5) * (v - 17*u)**6 * p_s
    sixth -= (v - 17*u)**4 * (
        exp_coeff[2] * p_c + (9*u)**2 * deriv(deriv(p_c)) / 2
    )
    sixth = reduce_elliptic(-sp.Rational(2, 3) * sixth)
    assert not sixth.has(ell_y)
    sixth_poly = sp.Poly(sixth, v, u)

    columns = []
    for j in range(7):
        column_poly = sp.expand(
            sixth_poly.coeff_monomial(v**(6-j) * u**j)
            * sp.factorial(6-j) * sp.factorial(j)
        )
        assert all(m[0] % 3 == 2 for m, _ in sp.Poly(column_poly, x).terms())
        assert sp.degree(column_poly, x) <= 17
        columns.append([column_poly.coeff(x, 2 + 3*a) for a in range(6)])
    matrix = sp.Matrix(columns).T
    positive_u = matrix[:, 1:]
    det = sp.factor(positive_u.det())
    assert det != 0

    s_column = sp.Matrix([
        -sp.Rational(128, 7), -sp.Rational(80, 7),
        -sp.Rational(12, 7), -sp.Rational(53, 7), 1, 0,
    ])
    refs = {
        "S": s_column,
        "H3": sp.Matrix([-2048, 12032, 8128, 400, -208, 1]),
        "H5": sp.Matrix([1024, -6784, -14912, -272, 272, 1]),
    }
    assert matrix[:, 0] == 14976 * s_column
    assert matrix[5, 6] == -44755200 * sp.factorial(6)

    z, h, t = sp.symbols("z h t")

    def fifth_moment(poly):
        poly = sp.Poly(sp.expand(poly), z, h)
        return sp.factor(sum(
            poly.coeff_monomial(z**(5-j) * h**j)
            * (-sp.Rational(2, 3)) * sp.factorial(5-j) * sp.factorial(j)
            for j in range(4)
        ))

    extraction = {}
    inverse = positive_u.inv()
    for name, target in refs.items():
        coefficients = inverse * target
        assert positive_u * coefficients == target
        denominator = sp.ilcm(*[c.q for c in coefficients])
        numerators = [int(c * denominator) for c in coefficients]
        test = sum(coefficients[j-1] * v**(6-j) * u**j for j in range(1, 7))
        assert sp.expand(test).subs(u, 0) == 0
        slope_value = sp.factor(test.subs(u, 280*v) / v**6)

        # Exact same-depth test: X=-c+tH, U=-280c+t(9Z-17H).
        # Degree six permits c=1 when extracting the two c^1 moments.
        moved = sp.Poly(sp.expand(test.subs({
            v: -1 + t*h, u: -280 + t*(9*z-17*h),
        }, simultaneous=True)), t)
        beta = fifth_moment(moved.coeff_monomial(t**5))
        alpha = sp.factor(sum(
            fifth_moment(moved.coeff_monomial(t**(5-k))
                         * (-1)**(k-1) * z**k / sp.Integer(k))
            for k in range(1, 6)
        ))
        assert beta == target[5]
        extraction[name] = {
            "denominator": int(denominator), "numerators": numerators,
            "coefficients": [str(c) for c in coefficients],
            "slope_U_equals_280X": str(slope_value),
            "local_fifth_alpha": str(alpha), "local_fifth_beta": str(beta),
            "denominator_factors": {str(q): int(e) for q, e in sp.factorint(denominator).items()},
            "slope_numerator_factors": {str(q): int(e) for q, e in sp.factorint(abs(slope_value.p)).items()},
            "alpha_numerator_factors": {str(q): int(e) for q, e in sp.factorint(abs(alpha.p)).items()},
        }

    extra_den_primes = [4357, 501843101759]
    s_slope_primes = [181, 42131, 92863, 7643]
    s_alpha_primes = [1093, 1431421, 43898162053]
    checked_primes = extra_den_primes + s_slope_primes + s_alpha_primes
    assert all(sp.isprime(q) and q % 64 != 7 for q in checked_primes)
    assert sp.factorint(abs(det.p)) == {
        2: 59, 3: 53, 5: 3, 17: 4, 4357: 1, 501843101759: 1,
    }
    assert det.q == 7**5
    assert extraction["S"]["local_fifth_beta"] == "0"
    assert extraction["S"]["local_fifth_alpha"] == "-480763982085139011763/107052528108059628480"

    result = {
        "normalization": {
            "b": 1, "columns": "X^(6-j) U^j, j=0..6, with both moment factorials",
            "rows": "sigma^34 x^(2+3a), a=0..5",
            "general_b_row_factor": "b^(5-a)",
            "tests": "substitute X/Omega,U/Omega; divide S test by b only",
        },
        "matrix": [[str(matrix[a,j]) for j in range(7)] for a in range(6)],
        "integer_matrix_7M": [[int(7*matrix[a,j]) for j in range(7)] for a in range(6)],
        "positive_u_determinant": str(det),
        "positive_u_det_factor_sign": int(sp.sign(det)),
        "positive_u_det_numerator_factors": {str(q): int(e) for q, e in sp.factorint(abs(det.p)).items()},
        "positive_u_det_denominator_factors": {"7": 5},
        "rank_all": matrix.rank(), "rank_positive_u": positive_u.rank(),
        "extractions": extraction,
        "additional_prime_residues_mod64": {str(q): q % 64 for q in checked_primes},
    }
    encoded = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(encoded, encoding="utf-8")
        print(json.dumps({"status": "exact identities verified", "output": str(args.output),
                          "rank_positive_u": 6, "S_slope": extraction["S"]["slope_U_equals_280X"],
                          "S_local_fifth_alpha": extraction["S"]["local_fifth_alpha"]}))
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
