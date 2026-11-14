#!/usr/bin/env python3
"""Exact canonical-neighbor traces of the actual inert primitive.

The input is the fixed integer theta flow, not a table of L-values.  For
d=p+1, the target field is Q_p[varpi]/(varpi^d-p).  We solve K(varpi X)=0
by integral Newton iteration and take the exact field trace d*[varpi^0].
The companion note proves that degree 2*d*max(N+1,4) suffices modulo p^N.

Examples printed by default:
  actual Tr(I/L), the unchanged-central-jet perturbation M -> M+t^(p+3),
  and the separate Tr(I/L^3) unit calibration.
"""
import argparse
import importlib.util
from fractions import Fraction
from math import factorial
from pathlib import Path

from flint import ctx, fmpq, fmpq_series


def fraction(x):
    if isinstance(x, Fraction):
        return x
    return Fraction(int(x.numerator), int(x.denominator))


def valuation(x, p):
    x = fraction(x)
    if not x:
        return 10**9
    a, b, v = x.numerator, x.denominator, 0
    while a % p == 0:
        a //= p
        v += 1
    while b % p == 0:
        b //= p
        v -= 1
    return v


def unit_part(x, p, modulus):
    x = fraction(x)
    v = valuation(x, p)
    x = x / p**v if v >= 0 else x * p**(-v)
    return x.numerator * pow(x.denominator, -1, modulus) % modulus, v


class TameRing:
    """O/(p^N), O=Z_p[varpi], varpi^(p+1)=p; exact finite arithmetic."""

    def __init__(self, p, precision):
        self.p = p
        self.precision = precision
        self.degree = p + 1
        self.modulus = p**precision

    def constant(self, c=0):
        result = [0] * self.degree
        result[0] = c % self.modulus
        return result

    def add(self, a, b):
        return [(x + y) % self.modulus for x, y in zip(a, b)]

    def subtract(self, a, b):
        return [(x - y) % self.modulus for x, y in zip(a, b)]

    def multiply(self, a, b):
        result = [0] * self.degree
        for i, x in enumerate(a):
            if not x:
                continue
            for j, y in enumerate(b):
                if not y:
                    continue
                k = i + j
                result[k % self.degree] += x * y * (
                    self.p if k >= self.degree else 1
                )
        return [x % self.modulus for x in result]

    def inverse(self, a):
        assert a[0] % self.p
        x = self.constant(pow(a[0], -1, self.modulus))
        for _ in range((self.precision * self.degree).bit_length() + 1):
            x = self.multiply(
                x, self.subtract(self.constant(2), self.multiply(a, x))
            )
        assert self.multiply(a, x) == self.constant(1)
        return x

    def scaled_coefficient(self, c, exponent):
        """The integral element c*varpi^exponent, allowing rational c."""
        if not c:
            return self.constant()
        unit, v = unit_part(c, self.p, self.modulus)
        exponent += self.degree * v
        assert exponent >= 0, (c, exponent, v)
        result = self.constant()
        result[exponent % self.degree] = (
            unit * pow(self.p, exponent // self.degree, self.modulus)
        ) % self.modulus
        return result

    def evaluate(self, coefficients, x):
        result = self.constant()
        for n in range(len(coefficients) - 1, -1, -1):
            result = self.add(
                self.multiply(result, x),
                self.scaled_coefficient(coefficients[n], n),
            )
        return result

    def derivative_evaluate(self, coefficients, x):
        result = self.constant()
        for n in range(len(coefficients) - 1, 0, -1):
            result = self.add(
                self.multiply(result, x),
                self.scaled_coefficient(n * coefficients[n], n),
            )
        return result

    def trace(self, x):
        return self.degree * x[0] % self.modulus


def fixed_series(degree):
    ctx.cap = degree + 1
    path = Path(__file__).with_name("check-theta-hurwitz-integers.py")
    spec = importlib.util.spec_from_file_location("actual_theta_flow", path)
    flow = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(flow)
    h = flow.coefficients(degree, 1)

    c = [fmpq(0)] * (degree + 1)
    for m in range(4, degree + 1, 4):
        c[m] = fmpq(h[m] ** 2, 24 * factorial(m) * 17 ** (m - 4))
    k = [fmpq(0)] * (degree + 1)
    ell = k.copy()
    k[0], ell[1] = 1, 1
    for n in range(degree - 1):
        factor = fmpq((2 * n + 1) ** 2, (n + 1) * (n + 2))
        k[n + 2] = k[n] * factor
        ell[n + 2] = ell[n] * factor
    t = fmpq_series([0, 1])
    K, L = fmpq_series(k), fmpq_series(ell)
    J = fmpq_series(ell[1:] + [0])
    u = L / K
    composed = fmpq_series([0])
    for m in range(degree, -1, -1):
        composed = composed * u + c[m]
    M = composed / K
    assert M[4] == 1 and M[6] == fmpq(7, 2)
    return t, K, J, M, c


def root_in_tame_ring(p, precision, K, cutoff):
    ring = TameRing(p, precision)
    coefficients = [K[n] for n in range(cutoff)]
    kappa = fraction(p * K[p + 1])
    kappa_mod = kappa.numerator * pow(kappa.denominator, -1, p) % p
    norm_value = -pow(kappa_mod, -1, p) % p
    # R68: kappa=beta/alpha and alpha*beta=-1, so norm_value=beta^(-2).
    start = next(a for a in range(1, p) if a * a % p == norm_value)
    x = ring.constant(start)
    for _ in range((precision * (p + 1)).bit_length() + 1):
        value = ring.evaluate(coefficients, x)
        derivative = ring.derivative_evaluate(coefficients, x)
        x = ring.subtract(x, ring.multiply(value, ring.inverse(derivative)))
    assert ring.evaluate(coefficients, x) == ring.constant()
    return ring, x, kappa_mod


def primitive_ratio(t, K, J, M, power, cutoff):
    W = M * K / ((1 - 4 * t * t) * J * J)
    # I'=W/t^2.  I/L^power = sum W[n+power+1]/(n+power)*t^n/J^power.
    numerator = fmpq_series(
        [W[n + power + 1] / (n + power) for n in range(cutoff)]
    )
    F = numerator / J**power
    return [F[n] for n in range(cutoff)]


def check(p, precision):
    assert p >= 7 and p % 4 == 3
    d = p + 1
    cutoff = 2 * d * max(precision + 1, 4)
    t, K, J, M, c = fixed_series(cutoff + 6)
    assert all(valuation(M[n], p) >= 0 for n in range(cutoff + 1))
    ring, root, kappa = root_in_tame_ring(p, precision, K, cutoff)

    gamma = fraction(c[d] / p)
    assert valuation(gamma, p) >= 0
    gamma_mod = gamma.numerator * pow(gamma.denominator, -1, p) % p
    values = {}
    for label, modular_input, power in (
        ("actual_I_over_L", M, 1),
        ("perturbation_I_over_L", t ** (p + 3), 1),
        ("actual_I_over_L_cubed", M, 3),
    ):
        coefficients = primitive_ratio(t, K, J, modular_input, power, cutoff)
        # The proved Gauss bound ensures integrality of each scaled coefficient.
        element = ring.evaluate(coefficients, root)
        values[label] = ring.trace(element)

    assert values["actual_I_over_L"] % p == 0
    assert values["perturbation_I_over_L"] % p == 0
    assert values["actual_I_over_L_cubed"] % p == pow(12, -1, p)
    if precision >= 3 and p in (7, 11):
        expected = {
            7: (84, 168, 325),
            11: (429, 1012, None),
        }[p]
        for label, answer in zip(values, expected):
            if answer is not None:
                assert values[label] % (p**3) == answer
    # M=t^(p+3) has order >p+1, so its C_(p+1), and hence its Gamma, is exactly zero.
    print(
        {
            "p": p,
            "precision": precision,
            "input_degree": cutoff + 6,
            "kappa_mod_p": kappa,
            "actual_gamma_mod_p": gamma_mod,
            "traces_mod_pN": values,
            "actual_trace_div_p_mod_p": values["actual_I_over_L"] // p % p,
            "zero_gamma_perturbation_trace_div_p_mod_p": values[
                "perturbation_I_over_L"
            ] // p % p,
        }
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primes", default="7,11")
    parser.add_argument("--precision", type=int, default=3)
    args = parser.parse_args()
    if args.precision < 2:
        parser.error("precision must be at least 2")
    for p in map(int, args.primes.split(",")):
        check(p, args.precision)
    print("Actual traces, zero-central-jet perturbations, and cubic-weight units passed.")


if __name__ == "__main__":
    main()
