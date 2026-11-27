#!/usr/bin/env python3
"""Exact q=13 calibration for the three ORIGINAL j=0 six-sigma sources.

No generated coefficient file, target-prime scan, central value, or assumed
calibration result is consumed.  The Hurwitz ODE and a separate Laurent
recurrence agree through order 30.  A failed v_13=3 gate is reported verbatim.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the named public Actions repository.")

from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
from math import comb, factorial
import json
from pathlib import Path


@dataclass(frozen=True)
class K:
    a: F = F(0)
    d: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, "a", F(self.a))
        object.__setattr__(self, "d", F(self.d))

    @staticmethod
    def coerce(x):
        return x if isinstance(x, K) else K(x)

    def __add__(self, other):
        y = K.coerce(other)
        return K(self.a + y.a, self.d + y.d)

    __radd__ = __add__

    def __neg__(self):
        return K(-self.a, -self.d)

    def __sub__(self, other):
        return self + (-K.coerce(other))

    def __rsub__(self, other):
        return K.coerce(other) - self

    def __mul__(self, other):
        y = K.coerce(other)
        return K(self.a*y.a - 3*self.d*y.d, self.a*y.d + self.d*y.a)

    __rmul__ = __mul__

    def inv(self):
        n = self.a*self.a + 3*self.d*self.d
        if not n:
            raise ZeroDivisionError("zero in Q(delta)")
        return K(self.a/n, -self.d/n)

    def __truediv__(self, other):
        return self * K.coerce(other).inv()

    def __pow__(self, n):
        if n < 0:
            return self.inv() ** (-n)
        out, x = K(1), self
        while n:
            if n & 1:
                out = out*x
            x = x*x
            n >>= 1
        return out

    def conjugate(self):
        return K(self.a, -self.d)

    def pair(self):
        return [[self.a.numerator, self.a.denominator],
                [self.d.numerator, self.d.denominator]]


def hproduct(a, b, n):
    """Hurwitz coefficient n of a*b, where arrays store derivatives at 0."""
    return sum((comb(n, j)*a[j]*b[n-j] for j in range(n+1)), 0)


def sigma_hurwitz(b, nmax):
    """Integral system u'=v, v'=3b*u^5, L'=-2b*u^4, theta'=L*theta."""
    u, v, ell, theta = ([0]*(nmax+1) for _ in range(4))
    u2, u3, u4, u5 = ([0]*(nmax+1) for _ in range(4))
    v[0], theta[0] = 1, 1
    for n in range(nmax):
        u2[n] = hproduct(u, u, n)
        u3[n] = hproduct(u2, u, n)
        u4[n] = hproduct(u2, u2, n)
        u5[n] = hproduct(u4, u, n)
        u[n+1] = v[n]
        v[n+1] = 3*b*u5[n]
        ell[n+1] = -2*b*u4[n]
        theta[n+1] = hproduct(ell, theta, n)
    sig = [hproduct(u, theta, n) for n in range(nmax+1)]
    assert all(isinstance(z, int) for z in sig)
    assert sig[0] == 0 and sig[1] == 1 and sig[7] == 24*b
    assert all(sig[n] == 0 for n in range(nmax+1) if n % 6 != 1)
    return sig


def source_hurwitz(sig, axes, nmax):
    out = [K(1)] + [K(0)]*nmax
    for a in axes:
        one = [sig[n]*(a**n) for n in range(nmax+1)]
        out = [hproduct(out, one, n) for n in range(nmax+1)]
    return [z/(-84) for z in out]


def laurent_exponential_check(axes, leading, b, nmax=30):
    """Independent x''=6x^2 and (log(sigma/z))''=z^-2-x."""
    order = (nmax-6)//6
    w = [F(1), F(-1, 7)]
    for r in range(2, order+1):
        w.append(sum((w[j]*w[r-j] for j in range(1, r)), F(0))
                 / ((r-1)*(6*r+1)))
    logf = [F(0)] + [-w[r]/(6*r*(6*r-1)) for r in range(1, order+1)]
    g = [K(0)] + [
        logf[r]*(b**r)*sum((a**(6*r) for a in axes), K(0))
        for r in range(1, order+1)
    ]
    ex = [K(1)]
    for r in range(1, order+1):
        ex.append(sum((j*g[j]*ex[r-j] for j in range(1, r+1)), K(0))/r)
    out = [K(0)]*(nmax+1)
    for r, c in enumerate(ex):
        n = 6+6*r
        out[n] = factorial(n)*leading*c
    return out


def det3(rows):
    a, b, c = rows
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0]))


def valuation_integer(n, q):
    if n == 0:
        return None
    n, v = abs(n), 0
    while n % q == 0:
        n //= q
        v += 1
    return v


def valuation_fraction(x, q):
    if not x:
        return None
    return valuation_integer(x.numerator, q)-valuation_integer(x.denominator, q)


def rational_mod(x, modulus):
    return (x.numerator % modulus)*pow(x.denominator, -1, modulus) % modulus


def digest(value):
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return sha256(payload.encode("ascii")).hexdigest()


def build_report():
    b, q, nmax = 17, 13, 30
    delta = K(0, 1)
    omega = (delta-1)/2
    gamma = (5+delta)/2
    pi13 = (7+delta)/2
    sources = [
        ("S34_raw", [gamma, gamma.conjugate(), delta, 2*delta, K(1), K(2)], K(1)),
        ("T72_raw_6delta", [gamma, gamma.conjugate(), delta, 2*delta, 3*delta, K(4)], 6*delta),
        ("A126_raw_39delta", [K(7), pi13, pi13.conjugate(), 3*delta, 2*delta, 2*delta], 39*delta),
    ]
    assert delta*delta == K(-3) and omega*omega+omega+1 == K(0)
    sig = sigma_hurwitz(b, nmax)
    source_records, rows = [], []
    selected = [6, 18, 30]
    normalized_c12_b1 = [F(-988, 105), F(-2938, 35), F(15836, 35)]
    for pos, (name, axes, leading) in enumerate(sources):
        product = K(1)
        for a in axes:
            product *= a
        assert product/(-84) == leading
        actual = source_hurwitz(sig, axes, nmax)
        other = laurent_exponential_check(axes, leading, b, nmax)
        assert actual == other
        assert actual[6] == factorial(6)*leading
        assert actual[12]/(factorial(12)*leading*b) == K(normalized_c12_b1[pos])
        assert all(actual[n] == K(0) for n in range(6))
        assert all(actual[n] == K(0) for n in range(nmax+1) if n % 6)
        # Raw integral lattice: do NOT divide the A source by 39*delta.
        assert all((84*z).a.denominator == 1 and (84*z).d.denominator == 1
                   for z in actual)
        rows.append([actual[n] for n in selected])
        source_records.append({
            "name": name,
            "axes_Qdelta": [a.pair() for a in axes],
            "raw_z6_coefficient_Qdelta": leading.pair(),
            "raw_z12_over_z6_and_b": str(normalized_c12_b1[pos]),
            "hurwitz_at_6_18_30_Qdelta": [actual[n].pair() for n in selected],
            "full_hurwitz_0_through_30_sha256": digest([x.pair() for x in actual]),
            "two_complete_recursions_agree": True,
            "whole_source_order": 6,
            "84_times_whole_hurwitz_is_integral_in_Zdelta": True,
        })
    determinant = det3(rows)
    assert determinant.d == 0
    vdet = valuation_fraction(determinant.a, q)
    gate = vdet == 3
    reduced_mod = None
    if determinant.a and vdet >= 3:
        reduced_mod = rational_mod(determinant.a/F(q**3), q**2)
    report = {
        "schema": "original_three_jzero_sources_quadratic_thirteen_hurwitz_v1",
        "verification_status": "PASS",
        "calibration_gate_v13_equals_3": gate,
        "auxiliary_prime": q,
        "model_b": b,
        "highest_hurwitz_index": nmax,
        "row_order": [x[0] for x in sources],
        "column_indices": selected,
        "source_lattice": "raw -1/84 product of all six sigma(a*z), b=17",
        "delta_square": -3,
        "sigma_hurwitz_0_through_30_sha256": digest(sig),
        "sources": source_records,
        "matrix_Qdelta": [[z.pair() for z in row] for row in rows],
        "determinant_Q": [determinant.a.numerator, determinant.a.denominator],
        "determinant_v13": vdet,
        "determinant_div_13cubed_mod_13squared": reduced_mod,
        "scope": {
            "no_target_prime_scan": True,
            "no_generated_input": True,
            "no_central_value_assumed_or_computed": True,
            "no_period_set_to_one": True,
            "no_normalized_A_lattice_substitution": True,
            "all_index_claim_requires_the_paper_divided_difference_proof": True,
        },
    }
    report["calibration_payload_sha256"] = digest(report)
    return report


def main():
    report = build_report()
    report["consumer_source_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    print(json.dumps(report, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
