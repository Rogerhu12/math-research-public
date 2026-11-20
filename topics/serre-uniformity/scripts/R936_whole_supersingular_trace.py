#!/usr/bin/env python3
"""Evaluate the whole R932 supersingular sum by the explicit H6 trace.

The mathematical contract is results/R936-explicit-polynomial-trace-of-the-whole-supersingular-pairing.md.
No third-party packages are needed. Run new arithmetic only in this repository's
public GitHub Actions. JSON outputs are recomputable and must not be committed.

Field elements are [a, b] for a + b*s, with s^2 = -3. Every polynomial coefficient
list is in increasing degree. The output retains the original zeta^2 phase,
both original labels, every supersingular branch, and its multiplicity.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import pathlib
import time


class Arithmetic:
    def __init__(self, p: int):
        self.p = p
        self.zero = (0, 0)
        self.one = (1, 0)
        self.s = (0, 1)

    def scalar(self, a: int):
        return (a % self.p, 0)

    def add(self, a, b):
        return ((a[0] + b[0]) % self.p, (a[1] + b[1]) % self.p)

    def neg(self, a):
        return ((-a[0]) % self.p, (-a[1]) % self.p)

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        return (
            (a[0] * b[0] - 3 * a[1] * b[1]) % self.p,
            (a[0] * b[1] + a[1] * b[0]) % self.p,
        )

    def inv(self, a):
        norm = (a[0] * a[0] + 3 * a[1] * a[1]) % self.p
        if not norm:
            raise ZeroDivisionError("zero element of F_(p^2)")
        inv_norm = pow(norm, -1, self.p)
        return (a[0] * inv_norm % self.p, -a[1] * inv_norm % self.p)

    def div(self, a, b):
        return self.mul(a, self.inv(b))

    def power(self, a, n):
        if n < 0:
            return self.power(self.inv(a), -n)
        out = self.one
        while n:
            if n & 1:
                out = self.mul(out, a)
            a = self.mul(a, a)
            n >>= 1
        return out

    def trim(self, a):
        a = list(a)
        while a and a[-1] == self.zero:
            a.pop()
        return a

    def padd(self, a, b):
        out = [self.zero] * max(len(a), len(b))
        for i in range(len(out)):
            out[i] = self.add(
                a[i] if i < len(a) else self.zero,
                b[i] if i < len(b) else self.zero,
            )
        return self.trim(out)

    def pneg(self, a):
        return [self.neg(x) for x in a]

    def psub(self, a, b):
        return self.padd(a, self.pneg(b))

    def pscale(self, a, c):
        return self.trim([self.mul(c, x) for x in a])

    def pmul(self, a, b, cutoff=None):
        if not a or not b:
            return []
        length = len(a) + len(b) - 1
        if cutoff is not None:
            length = min(length, cutoff)
        out = [self.zero] * length
        for i, x in enumerate(a):
            if x == self.zero or i >= length:
                continue
            for j, y in enumerate(b[: length - i]):
                if y != self.zero:
                    out[i + j] = self.add(out[i + j], self.mul(x, y))
        return self.trim(out)

    def ppower(self, a, n, cutoff=None):
        out = [self.one]
        while n:
            if n & 1:
                out = self.pmul(out, a, cutoff)
            a = self.pmul(a, a, cutoff)
            n >>= 1
        return out

    def pdivmod(self, a, b):
        a, b = self.trim(a), self.trim(b)
        if not b:
            raise ZeroDivisionError("zero polynomial divisor")
        if len(a) < len(b):
            return [], a
        quotient = [self.zero] * (len(a) - len(b) + 1)
        inv_leading = self.inv(b[-1])
        while a and len(a) >= len(b):
            shift = len(a) - len(b)
            coeff = self.mul(a[-1], inv_leading)
            quotient[shift] = coeff
            for j, y in enumerate(b):
                a[shift + j] = self.sub(a[shift + j], self.mul(coeff, y))
            a = self.trim(a)
        return self.trim(quotient), a

    def pmod(self, a, modulus):
        return self.pdivmod(a, modulus)[1]

    def pmulmod(self, a, b, modulus):
        return self.pmod(self.pmul(a, b), modulus)

    def ppowmod(self, a, n, modulus):
        out = [self.one]
        a = self.pmod(a, modulus)
        while n:
            if n & 1:
                out = self.pmulmod(out, a, modulus)
            a = self.pmulmod(a, a, modulus)
            n >>= 1
        return out

    def pinvmod(self, a, modulus):
        r0, r1 = list(modulus), self.pmod(a, modulus)
        t0, t1 = [], [self.one]
        while r1:
            quotient, remainder = self.pdivmod(r0, r1)
            r0, r1 = r1, remainder
            t0, t1 = t1, self.psub(t0, self.pmul(quotient, t1))
        if len(r0) != 1:
            raise ZeroDivisionError("polynomial is not a unit in the full algebra")
        inverse = self.pmod(self.pscale(t0, self.inv(r0[0])), modulus)
        if self.pmulmod(a, inverse, modulus) != [self.one]:
            raise ArithmeticError("polynomial inverse failed its complete identity")
        return inverse

    def derivative(self, a):
        return self.trim([self.mul(self.scalar(i), a[i]) for i in range(1, len(a))])

    def peval(self, a, x):
        out = self.zero
        for coeff in reversed(a):
            out = self.add(self.mul(out, x), coeff)
        return out

    def compose(self, a, x):
        out = []
        for coeff in reversed(a):
            out = self.padd(self.pmul(out, x), [coeff])
        return out

    def coeff(self, a, i):
        return a[i] if 0 <= i < len(a) else self.zero


def is_prime(n):
    if n < 2:
        return False
    return all(n % d for d in range(2, math.isqrt(n) + 1))


def eta_product(ar, step, exponent, shift, cutoff):
    """q^shift product_(n>=1) (1-q^(step*n))^exponent, below cutoff."""
    out = [ar.one]
    for n in range(1, (cutoff - 1 - shift) // step + 1):
        degree = step * n
        factor = [ar.zero] * (min(exponent, (cutoff - 1) // degree) * degree + 1)
        for j in range(min(exponent, (cutoff - 1) // degree) + 1):
            factor[j * degree] = ar.scalar((-1) ** j * math.comb(exponent, j))
        out = ar.pmul(out, factor, cutoff - shift)
    return ar.trim(([ar.zero] * shift + out)[:cutoff])


def oldform(ar, form, weight, cutoff):
    half = ar.scalar(pow(2, -1, ar.p))
    zeta_squared = ar.neg(ar.mul(half, ar.add(ar.one, ar.s)))
    multiple = ar.mul(ar.scalar(pow(2, weight, ar.p)), zeta_squared)
    out = list(form) + [ar.zero] * (cutoff - len(form))
    for n in range(1, (cutoff - 1) // 4 + 1):
        out[4 * n] = ar.sub(out[4 * n], ar.mul(multiple, ar.coeff(form, n)))
    return ar.trim(out)


def cm_theta(ar, weight, cutoff):
    """ET24, summing the six equivalent generators of every original ideal."""
    half = ar.scalar(pow(2, -1, ar.p))
    zeta = ar.mul(half, ar.sub(ar.s, ar.one))
    out = [ar.zero] * cutoff
    bound = math.isqrt(2 * (cutoff - 1)) + 1
    generator_counts = [0] * cutoff
    for a in range(-bound, bound + 1):
        for b in range(-bound, bound + 1):
            norm = a * a - a * b + b * b
            if not 1 <= norm < cutoff or norm % 3 == 0:
                continue
            residue = (a + b) % 3
            if residue not in (1, 2):
                raise ArithmeticError("invalid original conductor-three sign")
            sign = 1 if residue == 1 else -1
            alpha = ar.add(ar.scalar(a), ar.mul(ar.scalar(b), zeta))
            term = ar.mul(ar.scalar(sign), ar.power(alpha, weight - 1))
            out[norm] = ar.add(out[norm], term)
            generator_counts[norm] += 1
    inv6 = ar.scalar(pow(6, -1, ar.p))
    out = [ar.mul(inv6, x) for x in out]
    if out[1] != ar.one or any(x[1] for x in out):
        raise ArithmeticError("original theta normalization/rationality failed")
    if any(c % 6 for c in generator_counts):
        raise ArithmeticError("incomplete unit-generator orbit")
    return ar.trim(out)


def companion_polynomial(ar, weight, j_degree):
    max_q_degree = 1 + 3 * j_degree
    cutoff = max_q_degree + 1
    theta = cm_theta(ar, weight, cutoff)
    target = oldform(ar, theta, weight, cutoff)
    f4 = eta_product(ar, 3, 8, 1, cutoff)
    v4 = oldform(ar, f4, 4, cutoff)
    eta12 = eta_product(ar, 6, 12, 3, cutoff)
    e6 = [ar.zero] * cutoff
    e6[0] = ar.one
    for n in range(1, max_q_degree // 6 + 1):
        sigma5 = sum(d**5 for d in range(1, n + 1) if n % d == 0)
        e6[6 * n] = ar.scalar(-504 * sigma5)
    e6 = ar.trim(e6)

    residual = list(target)
    coefficients = []
    for j in range(j_degree + 1):
        basis = ar.pmul(
            ar.pmul(v4, ar.ppower(e6, j_degree - j, cutoff), cutoff),
            ar.ppower(eta12, j, cutoff),
            cutoff,
        )
        leading_degree = 1 + 3 * j
        if ar.coeff(basis, leading_degree) != ar.one:
            raise ArithmeticError("nonunit diagonal in the full original basis")
        if any(ar.coeff(basis, n) != ar.zero for n in range(leading_degree)):
            raise ArithmeticError("incorrect triangular cusp order")
        coeff = ar.coeff(residual, leading_degree)
        coefficients.append(coeff)
        residual = ar.psub(residual, ar.pscale(basis, coeff))
    if residual:
        raise ArithmeticError("original companion does not match its whole basis window")
    polynomial = list(reversed(coefficients))
    if len(polynomial) != j_degree + 1 or polynomial[-1] != ar.one:
        raise ArithmeticError("companion polynomial is not monic of the stated degree")
    return polynomial, {
        "maximum_original_Q_degree": max_q_degree,
        "basis_coefficients_cj": coefficients,
        "original_companion_Q_coefficients": target,
        "complete_truncated_identity": True,
    }


def hasse_polynomial(ar, n):
    m = 3 * n + 2
    fact = [1]
    for j in range(1, m + 1):
        fact.append(fact[-1] * j % ar.p)
    d = [ar.one, ar.scalar(-4)]
    linear = [ar.scalar(pow(2, -1, ar.p)), ar.scalar(-4)]
    out = []
    for a in range(n // 2 + 1):
        denominator = fact[2 * n + 1 - a] * fact[3 * a + 1] * fact[n - 2 * a]
        scalar = fact[m] * pow(denominator % ar.p, -1, ar.p)
        scalar = scalar * pow(3, 3 * a + 1, ar.p) % ar.p
        term = ar.pmul(ar.ppower(d, a), ar.ppower(linear, n - 2 * a))
        term = [ar.zero] * a + ar.pscale(term, ar.scalar(scalar))
        out = ar.padd(out, term)
    if len(out) != n + 1 or out[0] == ar.zero:
        raise ArithmeticError("unexpected Hasse degree or zero at t=0")
    if ar.peval(out, ar.scalar(pow(4, -1, ar.p))) == ar.zero:
        raise ArithmeticError("unexpected Hasse root at an elliptic branch")
    return out


def algebra_trace(ar, value, modulus):
    d = len(modulus) - 1
    euler = ar.pmod(ar.pmul(value, ar.derivative(modulus)), modulus)
    trace_euler = ar.coeff(euler, d - 1)
    diagonal_sum = ar.zero
    columns = []
    for j in range(d):
        column = ar.pmod([ar.zero] * j + list(value), modulus)
        diagonal_sum = ar.add(diagonal_sum, ar.coeff(column, j))
        columns.append(column + [ar.zero] * (d - len(column)))
    if trace_euler != diagonal_sum:
        raise ArithmeticError("Euler coefficient and full multiplication trace differ")
    return trace_euler, columns


def calculate_prime(p):
    if p < 41 or p % 6 != 5 or not is_prime(p):
        raise ValueError("the paper contract requires a prime p >= 41, p == 5 mod 6")
    ar = Arithmetic(p)
    n = (p - 5) // 6
    r = 2 if p % 12 == 11 else 8
    k_minus = p + 1 - r
    j_degree = (k_minus - 4) // 6
    if ar.power(ar.s, p) != ar.neg(ar.s):
        raise ArithmeticError("incorrect inert coefficient field")

    companion, q_receipt = companion_polynomial(ar, k_minus, j_degree)
    hasse = hasse_polynomial(ar, n)
    modulus_raw = [ar.zero] + hasse
    modulus = ar.pscale(modulus_raw, ar.inv(modulus_raw[-1]))
    # This inverse is the complete squarefreeness witness of the full algebra.
    derivative_inverse = ar.pinvmod(ar.derivative(modulus), modulus)
    d = [ar.one, ar.scalar(-4)]
    t_hprime = [ar.zero] + ar.derivative(hasse)
    b = ar.pneg(ar.pmul(d, ar.padd(hasse, ar.pscale(t_hprime, ar.scalar(3)))))
    b = ar.pmod(b, modulus)
    b_inverse = ar.pinvmod(b, modulus)

    argument = [ar.mul(ar.scalar(24), ar.s), ar.mul(ar.scalar(-192), ar.s)]
    c = ar.compose(companion, argument)
    c_scale = ar.mul(
        ar.mul(ar.scalar(12), ar.s),
        ar.power(ar.mul(ar.scalar(6), ar.s), j_degree),
    )
    c = ar.pmod(ar.pscale(c, c_scale), modulus)
    quotient = ar.pmulmod(
        ar.ppowmod(d, 2 * n + 2, modulus),
        ar.ppowmod(c, p + 1, modulus),
        modulus,
    )
    quotient = ar.pmulmod(
        quotient, ar.ppowmod(b_inverse, k_minus, modulus), modulus
    )
    e0 = ar.pscale(hasse, ar.inv(hasse[0]))
    if ar.pmulmod(e0, e0, modulus) != e0:
        raise ArithmeticError("t=0 idempotent failed its exact identity")
    weight = ar.psub([ar.scalar(3)], ar.pscale(e0, ar.scalar(2)))
    weighted = ar.pmulmod(weight, quotient, modulus)
    trace, trace_columns = algebra_trace(ar, weighted, modulus)

    c_r = -pow(6, r - 1, p) * math.factorial(r - 1) % p
    s_to_p = ar.mul(ar.scalar(12 * c_r * c_r), trace)
    s_value = ar.power(s_to_p, p)
    if ar.power(s_value, p) != s_to_p:
        raise ArithmeticError("wrong pth-root recovery in the original residue field")

    point_zero = ar.peval(quotient, ar.zero)
    root_part = ar.div(ar.sub(trace, point_zero), ar.scalar(3))
    return {
        "prime": p,
        "original_allowed_prime_class": p % 9 in (2, 5),
        "prime_mod_9": p % 9,
        "prime_mod_12": p % 12,
        "h": (p + 3) // 2 if r == 2 else (p + 9) // 2,
        "r": r,
        "k_minus": k_minus,
        "N": n,
        "J": j_degree,
        "field": {"basis": ["1", "s"], "relation": "s^2=-3", "s_frobenius": "-s"},
        "phase": "zeta=(-1+s)/2; original oldform phase zeta^2",
        "trace_algebra_dimension": n + 1,
        "H_N": hasse,
        "P_J": companion,
        "monic_tH_N": modulus,
        "modulus_derivative_inverse": derivative_inverse,
        "b_remainder": b,
        "b_inverse": b_inverse,
        "C_remainder": c,
        "R_remainder": quotient,
        "e0_remainder": e0,
        "weighted_R_remainder": weighted,
        "full_multiplication_matrix_columns": trace_columns,
        "trace_weighted_R": trace,
        "u_zero_contribution_before_fine_degree": point_zero,
        "H_N_roots_trace_before_factor_three": root_part,
        "elliptic_D_zero_contribution": [0, 0],
        "fine_tame_cover_degree": 12,
        "fine_supersingular_point_count": 6 * (p - 1),
        "fine_sum_S_to_p": s_to_p,
        "fine_sum_S": s_value,
        "fine_sum_is_nonzero": s_to_p != ar.zero,
        "unknown_original_lambda_scale_retained": True,
        "Q_prime_source_comparison_proved": False,
        "Legendre_factor_removed": False,
        "q_receipt": q_receipt,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primes", nargs="+", type=int, default=[41, 47, 59, 71, 83, 107])
    parser.add_argument("--output", type=pathlib.Path, required=True)
    args = parser.parse_args()
    rows = []
    for p in args.primes:
        started = time.perf_counter()
        row = calculate_prime(p)
        rows.append(row)
        print(
            json.dumps(
                {
                    "prime": p,
                    "original_allowed": row["original_allowed_prime_class"],
                    "r": row["r"],
                    "dimension": row["trace_algebra_dimension"],
                    "trace": row["trace_weighted_R"],
                    "fine_sum_S_to_p": row["fine_sum_S_to_p"],
                    "nonzero": row["fine_sum_is_nonzero"],
                    "elapsed_seconds": time.perf_counter() - started,
                },
                separators=(",", ":"),
            ),
            flush=True,
        )
    result = {
        "contract": "R936, ET1-ET31",
        "status": "exact_finite_computation_only",
        "requested_primes": args.primes,
        "rows": rows,
        "local_mathematical_execution_authorized": False,
        "execution_location_required": "Rogerhu12/math-research-public GitHub Actions",
        "all_prime_nonvanishing_proved": False,
        "serre_uniformity_proved": False,
    }
    payload = (json.dumps(result, sort_keys=True, indent=2) + "\n").encode()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(payload)
    print(
        json.dumps(
            {"output_bytes": len(payload), "sha256": hashlib.sha256(payload).hexdigest()},
            separators=(",", ":"),
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
