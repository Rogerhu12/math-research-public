#!/usr/bin/env python3
"""Exact symbolic certificates for R943; public repository Actions only.

Standard-library Fraction arithmetic in Q[T,X,Y], using sparse dictionaries.
No prime window and no numerical nonvanishing assertion are included.
"""

import argparse
from fractions import Fraction
from hashlib import sha256
import json
import os
from pathlib import Path


F = Fraction
ARITY = 3


def constant(value):
    value = F(value)
    return {(0, 0, 0): value} if value else {}


def variable(index):
    exponents = [0] * ARITY
    exponents[index] = 1
    return {tuple(exponents): F(1)}


def add(*polynomials):
    result = {}
    for polynomial in polynomials:
        for monomial, coefficient in polynomial.items():
            result[monomial] = result.get(monomial, F(0)) + coefficient
    return {m: c for m, c in result.items() if c}


def scale(polynomial, scalar):
    scalar = F(scalar)
    return {m: scalar * c for m, c in polynomial.items() if scalar * c}


def multiply(left, right):
    result = {}
    for lm, lc in left.items():
        for rm, rc in right.items():
            monomial = tuple(lm[i] + rm[i] for i in range(ARITY))
            result[monomial] = result.get(monomial, F(0)) + lc * rc
    return {m: c for m, c in result.items() if c}


def power(polynomial, exponent):
    assert isinstance(exponent, int) and exponent >= 0
    result = constant(1)
    while exponent:
        if exponent & 1:
            result = multiply(result, polynomial)
        polynomial = multiply(polynomial, polynomial)
        exponent //= 2
    return result


def derivative(polynomial, index):
    result = {}
    for monomial, coefficient in polynomial.items():
        if monomial[index]:
            exponents = list(monomial)
            exponents[index] -= 1
            result[tuple(exponents)] = coefficient * monomial[index]
    return result


def canonical(polynomial):
    return [[list(m), [c.numerator, c.denominator]]
            for m, c in sorted(polynomial.items())]


def fingerprint(polynomial):
    encoded = json.dumps(canonical(polynomial), separators=(",", ":")).encode()
    return sha256(encoded).hexdigest()


def degree_summary(polynomial):
    if not polynomial:
        return {"total": None, "by_variable_T_X_Y": [None] * ARITY}
    return {"total": max(sum(m) for m in polynomial),
            "by_variable_T_X_Y": [max(m[i] for m in polynomial)
                                   for i in range(ARITY)]}


def certificate(name, left, right, denominator="1"):
    residual = add(left, scale(right, -1))
    return {
        "name": name,
        "cleared_denominator": denominator,
        "all_coefficients_zero": not residual,
        "left_term_count": len(left),
        "right_term_count": len(right),
        "left_degrees": degree_summary(left),
        "right_degrees": degree_summary(right),
        "left_canonical_sha256": fingerprint(left),
        "right_canonical_sha256": fingerprint(right),
        "residual_term_count": len(residual),
        "first_nonzero_residual_terms": canonical(residual)[:20],
    }


def qmul(left, right):
    """Q(s), s^2=-3, represented by (rational constant, rational s coefficient)."""
    a, b = left
    c, d = right
    return a*c - 3*b*d, a*d + b*c


def qscale(value, scalar):
    scalar = F(scalar)
    return value[0] * scalar, value[1] * scalar


def qpower(value, exponent):
    result = (F(1), F(0))
    while exponent:
        if exponent & 1:
            result = qmul(result, value)
        value = qmul(value, value)
        exponent //= 2
    return result


def verify_symbolically():
    one = constant(1)
    t, x, y = (variable(i) for i in range(ARITY))
    a = add(scale(t, 12), constant(-15))
    b = add(scale(power(t, 2), 4), scale(t, -28), constant(22))
    f = add(power(x, 3), multiply(a, x), b)
    ft, fx = derivative(f, 0), derivative(f, 1)
    c = add(t, one)
    one_minus_t2 = add(one, scale(power(t, 2), -1))
    checks = []

    # 943.19: the total-X-derivative certificate for the Legendre equation.
    s_polynomial = add(
        scale(power(x, 4), F(2, 9)),
        multiply(add(scale(t, F(4, 3)), constant(F(-14, 3))), power(x, 2)),
        multiply(add(scale(power(t, 2), F(-4, 9)), scale(t, F(-44, 9)),
                     constant(F(68, 9))), x),
        scale(power(c, 2), F(4, 3)),
    )
    ode_left = add(
        multiply(one_minus_t2,
                 add(scale(power(ft, 2), F(3, 4)), scale(f, -4))),
        multiply(t, multiply(f, ft)),
        scale(power(f, 2), F(-2, 9)),
    )
    ode_right = add(scale(multiply(f, derivative(s_polynomial, 1)), 2),
                    scale(multiply(s_polynomial, fx), -3))
    checks.append(certificate("943.19 Legendre total-derivative certificate",
                              scale(ode_left, 36), scale(ode_right, 36),
                              "rational coefficient denominators cleared by 36"))
    checks.append(certificate("family f_TT equals 8", derivative(ft, 0), constant(8)))

    # 943.22: multiply the rational differential identity by D=6(1-T^2).
    d_gm = scale(one_minus_t2, 6)
    u_numerator = add(scale(t, 2), constant(-1))
    r_numerator = add(scale(power(x, 2), -1), multiply(u_numerator, x),
                      scale(a, F(-2, 3)))
    gm_left = scale(multiply(d_gm, ft), F(-1, 2))
    gm_right = add(multiply(add(u_numerator, x), f),
                   scale(multiply(derivative(r_numerator, 1), f), 2),
                   scale(multiply(r_numerator, fx), -1))
    checks.append(certificate("943.22 Gauss-Manin exact differential",
                              scale(gm_left, 6), scale(gm_right, 6),
                              "6 times D, D=6(1-T^2)"))
    checks.append(certificate("GM coefficient of X",
                              add(scale(multiply(a, u_numerator), 2), scale(b, -3)),
                              scale(d_gm, -6), "D=6(1-T^2)"))
    checks.append(certificate("GM constant coefficient",
                              add(scale(multiply(b, u_numerator), 3),
                                  scale(power(a, 2), F(2, 3))),
                              scale(multiply(d_gm, derivative(b, 0)), F(-1, 2)),
                              "D=6(1-T^2)"))

    # The fixed family, its discriminant and the displayed order-three point.
    checks.append(certificate("943.15 discriminant factor",
                              add(scale(power(a, 3), 4), scale(power(b, 2), 27)),
                              scale(multiply(add(t, constant(-1)), power(c, 3)), 432)))
    translated_x = add(x, constant(3))
    translated_f = add(power(translated_x, 3), multiply(a, translated_x), b)
    translated_y = add(y, scale(x, 3), scale(c, 2))
    tate_left = add(power(translated_y, 2), scale(translated_f, -1))
    tate_right = add(power(y, 2), scale(multiply(x, y), 6),
                     scale(multiply(c, y), 4), scale(power(x, 3), -1))
    checks.append(certificate("943.16 Tate order-three model", tate_left, tate_right))

    # 943.31: r=N/Z^2, r'=W/Z^3, and clear the full denominator Z^6.
    z = add(x, constant(-3))
    r_numerator_isogeny = add(multiply(x, power(z, 2)),
                              scale(multiply(c, z), 24), scale(power(c, 2), 16))
    derivative_numerator = add(multiply(derivative(r_numerator_isogeny, 1), z),
                               scale(r_numerator_isogeny, -2))
    expected_derivative_numerator = add(power(z, 3),
                                        scale(multiply(c, z), -24),
                                        scale(power(c, 2), -32))
    checks.append(certificate("943.29 derivative r' numerator",
                              derivative_numerator, expected_derivative_numerator,
                              "(X-3)^3"))
    a_conjugate = add(scale(t, -12), constant(-15))
    b_conjugate = add(scale(power(t, 2), 4), scale(t, 28), constant(22))
    a_target = scale(a_conjugate, 9)
    b_target = scale(b_conjugate, -27)
    isogeny_left = multiply(f, power(derivative_numerator, 2))
    isogeny_right = add(power(r_numerator_isogeny, 3),
                        multiply(a_target, multiply(r_numerator_isogeny, power(z, 4))),
                        multiply(b_target, power(z, 6)))
    checks.append(certificate("943.31 normalized three-isogeny curve equation",
                              isogeny_left, isogeny_right, "(X-3)^6"))

    # The stated conjugate target and differential multiplier in Q(s).
    # U=alpha X', V=beta Y', alpha=-1/3=1/s^2, beta=s/9=1/s^3.
    s = (F(0), F(1))
    alpha = (F(-1, 3), F(0))
    beta = (F(0), F(1, 9))
    beta_squared = qmul(beta, beta)
    quadratic_checks = {
        "s_squared_equals_minus_3": qpower(s, 2) == (F(-3), F(0)),
        "s_fourth_equals_9": qpower(s, 4) == (F(9), F(0)),
        "s_sixth_equals_minus_27": qpower(s, 6) == (F(-27), F(0)),
        "alpha_times_s_squared_equals_1": qmul(alpha, qpower(s, 2)) == (F(1), F(0)),
        "beta_times_s_cubed_equals_1": qmul(beta, qpower(s, 3)) == (F(1), F(0)),
        "target_cubic_coefficient": beta_squared == qpower(alpha, 3),
        "target_linear_coefficient": qscale(beta_squared, 9) == alpha,
        "target_constant_coefficient": qscale(beta_squared, -27) == (F(1), F(0)),
        "943.32_differential_multiplier_s": qmul(beta, s) == alpha,
    }
    return {
        "schema": "original-p11-fixed-cartier-symbolic-v1",
        "arithmetic": "stdlib Fraction; sparse Q[T,X,Y]; Q(s) with s^2=-3",
        "symbolic_certificates": checks,
        "quadratic_field_scaling_checks": quadratic_checks,
        "all_symbolic_identities_verified":
            all(item["all_coefficients_zero"] for item in checks) and all(quadratic_checks.values()),
        "new_prime_window_run": False,
        "all_prime_nonvanishing_claimed": False,
        "source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path("/tmp/p11-fixed-cartier-symbolic.json"))
    args = parser.parse_args()
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise SystemExit("New arithmetic is permitted only in public repository Actions.")
    report = verify_symbolically()
    encoded = (json.dumps(report, sort_keys=True, indent=2) + "\n").encode()
    args.output.write_bytes(encoded)
    print(json.dumps(report, sort_keys=True), flush=True)
    print("OUTPUT_SHA256=" + sha256(encoded).hexdigest(), flush=True)
    if not report["all_symbolic_identities_verified"]:
        raise SystemExit("A displayed symbolic certificate failed; see the exact residual above.")


if __name__ == "__main__":
    main()
