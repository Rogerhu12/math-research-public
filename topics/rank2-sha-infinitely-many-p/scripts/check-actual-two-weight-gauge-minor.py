#!/usr/bin/env python3
"""R197: actual Hurwitz ODE versus a finite-field common-gauge algorithm."""

import importlib.util
import json
from math import comb, factorial, gcd
from pathlib import Path

from flint import ctx, fmpq, fmpq_series as Series


def load(name, filename):
    spec = importlib.util.spec_from_file_location(
        name, Path(__file__).with_name(filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


flow = load("integer_flow", "check-theta-hurwitz-integers.py")
inputs = load("fixed_inputs", "check-fixed-five-adic-central-minor.py")


def residue(value, p):
    value = fmpq(value)
    denominator = int(value.denominator)
    assert denominator % p
    return int(value.numerator) * pow(denominator, -1, p) % p


def valuation(value, p):
    value = fmpq(value)
    if value == 0:
        return None
    answer = 0
    numerator, denominator = abs(int(value.numerator)), int(value.denominator)
    while numerator % p == 0:
        numerator //= p
        answer += 1
    while denominator % p == 0:
        denominator //= p
        answer -= 1
    return answer


class Truncated:
    """Plain finite-field series: every inversion denominator is explicit."""

    def __init__(self, p, degree):
        self.p, self.length = p, degree + 1

    def mul(self, a, b):
        c = [0] * self.length
        for i, x in enumerate(a):
            for j, y in enumerate(b[:self.length-i]):
                c[i+j] = (c[i+j] + x*y) % self.p
        return c

    def power(self, a, n):
        assert n >= 0
        c = [1] + [0] * (self.length-1)
        while n:
            if n & 1:
                c = self.mul(c, a)
            a = self.mul(a, a)
            n //= 2
        return c

    def inverse(self, a):
        c = [pow(a[0], -1, self.p)] + [0] * (self.length-1)
        for n in range(1, self.length):
            c[n] = -c[0]*sum(a[j]*c[n-j] for j in range(1, n+1))
            c[n] %= self.p
        return c

    def compose(self, coefficients, argument):
        assert argument[0] == 0
        out = [0] * self.length
        for coefficient in reversed(coefficients):
            out = self.mul(out, argument)
            out[0] = (out[0] + coefficient) % self.p
        return out

    def exponential(self, a):
        assert a[0] == 0 and self.length <= self.p
        out = [1] + [0] * (self.length-1)
        for n in range(1, self.length):
            out[n] = (sum(j*a[j]*out[n-j] for j in range(1, n+1))
                      * pow(n, -1, self.p)) % self.p
        return out


def fixed_polynomials():
    ctx.cap = 17
    s = Series([0, 1], prec=17)
    p_s, q_s = inputs.polys(s)
    return ([p_s[j] for j in range(17)],
            [q_s[j] for j in range(17)])


POLYNOMIALS = fixed_polynomials()


def finite_field_rows(p):
    r = (p+1)//4
    degree = 2*r
    ring = Truncated(p, degree)
    ell = [(comb(2*n, n) * pow(4**n*(4*n+1), -1, p)) % p
           for n in range(degree)] + [0]
    inverse_fourth = ring.power(ring.inverse(ell), 4)
    # Lagrange reversion of w=s F(s)^4; n< p throughout.
    s_of_w = [0] * (degree+1)
    for n in range(1, degree+1):
        s_of_w[n] = (ring.power(inverse_fourth, n)[n-1]
                     * pow(n, -1, p)) % p
    w_of_s = [0] + ring.power(ell, 4)[:-1]
    assert ring.compose(w_of_s, s_of_w) == [0, 1] + [0]*(degree-1)
    u_over_z = ring.inverse(ring.compose(ell, s_of_w))
    numerator = ring.power(u_over_z, 2)
    gauge = [0]*(degree+1)
    for n in range(1, degree):
        if n != r:
            gauge[n] = (68*numerator[n-1]
                        * pow(4*n*(4*n-1), -1, p)) % p
    factor = ring.exponential(gauge)
    series = [
        ring.mul(factor, ring.compose([residue(c, p) for c in polynomial],
                                      s_of_w))
        for polynomial in POLYNOMIALS]
    return [[series[0][j*r], series[1][j*r]] for j in (1, 2)]


def actual_ode_check(p):
    assert p >= 7 and p % 4 == 3
    r = (p+1)//4
    degree, m = 2*r, 2*p+2
    sigma, theta = flow.universal_sigma_theta(m)
    ctx.cap = degree+1
    w = Series([0, 1], prec=degree+1)
    th = Series([fmpq(theta[4*j], factorial(4*j))
                 for j in range(degree+1)], prec=degree+1)
    su = Series([fmpq(sigma[4*j+1], factorial(4*j+1))
                 for j in range(degree)], prec=degree+1)
    s = w*(su/th)**4
    p_s, q_s = inputs.polys(s)
    actual = (th**68*p_s, th**68*q_s)
    k = th.log()
    kappa = p*k[r]
    expected_kappa = comb(2*r-2, r-1)*pow(4**(r-1), -1, p) % p
    assert residue(kappa, p) == expected_kappa != 0
    assert all(valuation(k[n], p) is None or valuation(k[n], p) >= 0
               for n in range(1, degree) if n != r)
    gauge = Series([0] + [68*k[n] if n != r else 0
                          for n in range(1, degree)],
                   prec=degree+1)
    corrected = (gauge.exp()*p_s, gauge.exp()*q_s)
    for f, g in zip(actual, corrected):
        assert f[r] == g[r]
        assert f[2*r] == g[2*r] + 68*k[r]*g[r]
    finite = finite_field_rows(p)
    assert finite == [[residue(corrected[j][i*r], p) for j in range(2)]
                      for i in (1, 2)]
    # The independent integer flow includes the original A2 scaling.
    product = flow.coefficients(m, 1)
    for weight in (p+1, 2*p+2):
        assert factorial(weight)*actual[0][weight//4] == (
            2**(weight-4)*product[weight])
    first = [factorial(p+1)*f[r] for f in actual]
    second = [factorial(2*p+2)*f[2*r] for f in actual]
    eta = 68*k[r]*fmpq(factorial(2*p+2), factorial(p+1))
    assert valuation(eta, p) == 0
    assert residue(eta, p) == (-272*expected_kappa) % p
    for j in range(2):
        assert second[j]-eta*first[j] == (
            factorial(2*p+2)*corrected[j][2*r])
        assert valuation(first[j]/p, p) >= 0
        assert valuation((second[j]-eta*first[j])/p**2, p) >= 0
    delta = first[0]*second[1]-first[1]*second[0]
    finite_det = (finite[0][0]*finite[1][1]
                  - finite[0][1]*finite[1][0]) % p
    assert residue(delta/p**3, p) == -4*finite_det % p
    return {
        "p": p,
        "kappa_mod_p": expected_kappa,
        "eta_mod_p": residue(eta, p),
        "actual_corrected_rows_mod_p": finite,
        "delta_over_p_cubed_mod_p": residue(delta/p**3, p),
        "integer_ode_and_finite_field_algorithm_agree": True,
        "a2_six_factor_scale_checked": True,
    }


def e34_finite_kernel():
    def epsilon(a, b):
        for j, (x, y) in enumerate(((1, 0), (0, 1), (-1, 0), (0, -1))):
            aa, bb = a-x, b-y
            if aa % 2 == 0 and bb % 2 == 0 and (aa+bb) % 4 == 0:
                return j
        raise AssertionError((a, b))

    def weight(a, b):
        a, b = a % 68, b % 68
        if a % 2 != 1 or b % 2 != 0 or (a*a+b*b) % 17 == 0:
            return 0
        return ((1 if a % 4 == 1 else -1)
                * (1 if pow(a*a+b*b, 8, 17) == 1 else -1))

    actual = set()
    predicted = set()
    for a in range(68):
        for b in range(68):
            norm = a*a+b*b
            if norm % 2 == 0 or norm % 17 == 0:
                continue
            chi8 = 1 if norm % 8 in (1, 7) else -1
            chi17 = 1 if pow(norm, 8, 17) == 1 else -1
            finite_character = (-epsilon(a, b)
                                + (0 if chi8*chi17 == 1 else 2)) % 4
            if finite_character == 0:
                actual.add((a, b))
            if weight(a, b) == 1:
                predicted.add((a, b))
    assert actual == predicted and len(actual) == 512
    minus = {((-a) % 68, (-b) % 68) for a, b in actual}
    assert not actual.intersection(minus)
    for u in range(68):
        if gcd(u, 68) == 1:
            sign = 1 if u % 4 == 1 else -1
            for a in range(68):
                for b in range(68):
                    assert weight(u*a, u*b) == sign*weight(a, b)
    # u=33 is 1 modulo 4 and -1 modulo 17.
    for a in range(68):
        for b in range(68):
            assert weight(33*a, b) == weight(a, b)
            assert weight(a+34, b) == -weight(a, b)
    assert {a for a, b in actual if b == 0} == {
        a for a in range(68) if a % 4 == 1 and a % 17 != 0}
    return {"e34_actual_kernel_size": 512,
            "primary_character_matches_explicit_weight": True,
            "all_scalar_covariances": True,
            "seventeen_reflection_symmetry": True}


def main():
    # These two primes were already checked in the earlier raw-moment work.
    # The purpose here is the new equality of independent algorithms.
    output = {
        "two_weight_calibration": [actual_ode_check(p) for p in (7, 19)],
        "actual_finite_labels": e34_finite_kernel(),
        "verified": True,
    }
    print(json.dumps(output, separators=(",", ":")))


if __name__ == "__main__":
    main()
