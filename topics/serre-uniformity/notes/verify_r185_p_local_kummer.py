#!/usr/bin/env python3
"""Exact p-local Kummer coordinates for the SAME principal unit as R171.

Uses only Python's standard library, and the R171/R161 arithmetic module.
The p-local computations have finite algebraic tail bounds proved in R185.
The one q-local computation selects the sign of the global four-torsion mark;
it does not repeat the R171 1848-point enumeration or search for new primes.
"""
import argparse
import importlib.util
import json
import sys
from math import lcm
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
MODEL = HERE / 'r171_principal_norm_selflocal_certificate.json'
TARGET = HERE / 'r185_p_local_kummer_certificate.json'
spec = importlib.util.spec_from_file_location(
    'r171', HERE / 'verify_r171_principal_norm_selflocal.py')
r171 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r171)


def common_denominator(coefficients):
    denominator = lcm(*(d for _, d in coefficients))
    return [n*(denominator//d) for n, d in coefficients], denominator


def exact_modular_identity(data, extra):
    """Verify t^3=16 h^2(h^2+4) in Q[y]/P by integer arithmetic."""
    P = list(reversed(data['P']))
    T, dt = common_denominator(data['weber_map'])
    H, dh = common_denominator(extra['h_coefficients_ascending'])
    mul = lambda a, b: r171.multiply_poly(a, b, P)
    h2 = mul(H, H)
    h2plus = h2[:]
    h2plus[0] += 4*dh*dh
    lhs = [16*dt**3*c for c in mul(h2, h2plus)]
    rhs = [dh**4*c for c in mul(mul(T, T), T)]
    assert lhs == rhs
    assert all(d % 43 for _, d in extra['h_coefficients_ascending'])
    n, d = extra['h_coefficients_ascending'][0]
    assert n*pow(d, -1, 43) % 43 == 2
    assert pow(8, 21, 43) == 42


def marked_scalar_norm(data, extra):
    """One existing prime, all 42 scalars; fix z=-i*h by an exact equality."""
    q = data['q']
    field = r171.CertifiedField(q)  # q is proved prime in R171.
    curve = r171.r161.Curve(field)
    P = tuple(tuple(c) for c in data['expected']['P'])
    P2 = (field.i, (1, q-1))
    assert curve.on_curve(P) and curve.mul(43, P) is None
    y0 = (-pow(data['b'], -1, q) % q, 0)
    assert r171.polyval(field, data['P'], y0) == field.zero
    h = r171.polyval(field, [n*pow(d, -1, q) % q
        for n, d in reversed(extra['h_coefficients_ascending'])], y0)
    value = field.one
    for a in range(1, 43):
        Q = curve.add(P2, curve.mul(a, P))
        value = field.mul(value, field.div(
            field.power((64, 0), 10), curve.division_values(Q)(11)))
    matches = []
    for sign in (1, -1):
        z = field.scale(sign, field.mul(field.i, h))
        U = field.div(field.scale(2, field.power(field.sub(z, (2, 0)), 4)),
            field.mul(z, field.power(field.add(z, (2, 0)), 2)))
        rhs = field.div(field.power(U, 5), field.power((2, 0), 15))
        matches.append(value == rhs)
    assert matches == [False, True]


class Series:
    """Truncated series over (Z/43^3)[i], i^2=-1."""
    def __init__(self):
        self.p, self.mod, self.N = 43, 43**3, 90
        self.zero = [(0, 0)]*self.N
        self.one = [(1, 0)] + self.zero[1:]

    def ga(self, a, b):
        return ((a[0]+b[0]) % self.mod, (a[1]+b[1]) % self.mod)

    def gm(self, a, b):
        return ((a[0]*b[0]-a[1]*b[1]) % self.mod,
                (a[0]*b[1]+a[1]*b[0]) % self.mod)

    def gi(self, a):
        r = pow((a[0]*a[0]+a[1]*a[1]) % self.mod, -1, self.mod)
        return (a[0]*r % self.mod, -a[1]*r % self.mod)

    def add(self, a, b):
        return [self.ga(x, y) for x, y in zip(a, b)]

    def scale(self, a, c):
        if isinstance(c, int):
            c = (c, 0)
        return [self.gm(x, c) for x in a]

    def sub(self, a, b):
        return self.add(a, self.scale(b, -1))

    def shift(self, a, n):
        return [(0, 0)]*n + a[:self.N-n]

    def mul(self, a, b):
        c = self.zero[:]
        ia = [(i, x) for i, x in enumerate(a) if x != (0, 0)]
        ib = [(i, x) for i, x in enumerate(b) if x != (0, 0)]
        for i, x in ia:
            for j, y in ib:
                if i+j < self.N:
                    c[i+j] = self.ga(c[i+j], self.gm(x, y))
        return c

    def power(self, a, n):
        c = self.one[:]
        while n:
            if n & 1:
                c = self.mul(c, a)
            a = self.mul(a, a)
            n >>= 1
        return c

    def inv(self, a):
        c = self.zero[:]
        c[0] = self.gi(a[0])
        for n in range(1, self.N):
            s = (0, 0)
            for j in range(1, n+1):
                s = self.ga(s, self.gm(a[j], c[n-j]))
            z = self.gm(c[0], s)
            c[n] = (-z[0] % self.mod, -z[1] % self.mod)
        return c

    def evaluate(self, coefficients, y):
        z = self.zero[:]
        for n, d in reversed(coefficients):
            z = self.mul(z, y)
            z[0] = self.ga(z[0], (n*pow(d, -1, self.mod) % self.mod, 0))
        return z

    def plog(self, unit):
        v = self.sub(self.scale(unit, self.gi(unit[0])), self.one)
        assert v[0] == (0, 0)
        ans, power = self.zero[:], self.one[:]
        for n in range(1, self.N):
            power = self.mul(power, v)
            coefficient = (pow(n//self.p, -1, self.mod) if n % self.p == 0
                else self.p*pow(n, -1, self.mod))
            ans = self.add(ans, self.scale(power,
                -coefficient if n % 2 == 0 else coefficient))
        return ans


def canonical_parameter(ring, data):
    p, mod = ring.p, ring.mod
    P = list(reversed(data['P']))
    assert P[-1] == 1 and len(P) == 45
    assert all(c % p == 0 for c in P[:-1]) and P[0] % (p*p) != 0
    C = -P[0]//p
    assert C % p
    coefficients = [((P[i]//p)*pow(C, -1, mod)) % mod for i in range(44)]

    def equation(u):
        powers = [ring.one]
        for _ in range(44):
            powers.append(ring.mul(powers[-1], u))
        F = ring.sub(powers[44], ring.one)
        D = ring.scale(powers[43], 44)
        for i in range(1, 44):
            if coefficients[i]:
                F = ring.add(F, ring.scale(ring.shift(powers[i], i), coefficients[i]))
                D = ring.add(D, ring.scale(ring.shift(powers[i-1], i), i*coefficients[i]))
        return F, D

    u = ring.one[:]
    for _ in range(8):
        F, D = equation(u)
        u = ring.sub(u, ring.mul(F, ring.inv(D)))
    assert equation(u)[0] == ring.zero
    return C, ring.shift(u, 1)


def log_coordinates(ring, ell, C):
    p = ring.p
    assert all(c % p == 0 for c in ell[1])
    A = tuple((ell[1][j]//p+C*ell[45][j]+C*C*p*ell[89][j]) % (p*p)
        for j in (0, 1))
    pB = tuple((ell[43][j]+C*p*ell[87][j]) % (p*p) for j in (0, 1))
    return A, pB


def compute(data, extra):
    exact_modular_identity(data, extra)
    marked_scalar_norm(data, extra)
    ring = Series()
    p, mod, N = ring.p, ring.mod, ring.N
    C, y = canonical_parameter(ring, data)
    ell = ring.plog(ring.add(ring.one, ring.scale(y, data['b'])))
    A, pB = log_coordinates(ring, ell, C)
    assert A[1] == pB[1] == 0 and (A[0]-pB[0]) % p == 0
    alpha_coordinates = [pB[0] % p, ((A[0]-pB[0])//p*pow(C, -1, p)) % p]
    alpha = dict(p=p, modulus=mod, C=C, C_mod_p=C % p,
        b_mod_p=data['b'] % p, precision_degree=N-1, root_equation_pass=True,
        p_log_coefficients={str(i): ell[i][0] for i in (1, 43, 45, 87, 89)},
        A_mod_p2=A[0], pB_mod_p2=pB[0], artin_hasse_coordinates=alpha_coordinates,
        basis=['E_43(pi)', 'E_43(pi^45)'],
        relation='pi^44=C*43; pi/y=1+O(y^2)',
        scope='W-isotypic local Kummer class of alpha; not Omega_2 or t_q/43^2')

    h = ring.evaluate(extra['h_coefficients_ascending'], y)
    assert h[0][0] % p == 2 and h[0][1] == 0
    z, two = ring.scale(h, (0, -1)), ring.scale(ring.one, 2)
    U = ring.scale(ring.mul(ring.power(ring.sub(z, two), 4),
        ring.inv(ring.mul(z, ring.power(ring.add(z, two), 2)))), 2)
    unit = ring.scale(ring.power(U, 5), pow(2, -15, mod))
    ell = ring.plog(unit)
    A, pB = log_coordinates(ring, ell, C)
    assert A[0] == pB[0] == 0 and (A[1]+pB[1]) % p == 0
    robert_coordinates = [-pB[1] % p, ((A[1]+pB[1])//p*pow(C, -1, p)) % p]
    robert = dict(p=p, precision_degree=N-1, h_constant_mod_p3=h[0][0],
        robert_constant_mod_p3=list(unit[0]),
        coefficients_p_log={str(i): list(ell[i]) for i in (1, 43, 45, 87, 89)},
        A_over_i_mod_p2=A[1], pB_over_i_mod_p2=pB[1],
        complex_AH_coordinates=robert_coordinates,
        R161_dRob_in_R171_orbit_AH_basis=robert_coordinates,
        scope='actual p-local raw Robert Kummer class; no flat-line identification and no Omega2 value')
    determinant = (alpha_coordinates[0]*robert_coordinates[1]
        - alpha_coordinates[1]*robert_coordinates[0]) % p
    beta = alpha_coordinates[0]*pow(robert_coordinates[0], -1, p) % p
    normalized = [(a-beta*b) % p for a, b in zip(alpha_coordinates, robert_coordinates)]
    return dict(alpha=alpha, robert=robert, determinant=determinant,
        flat_normalization_beta=beta, normalized_dq_coordinates=normalized)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    data, extra = json.loads(MODEL.read_text()), json.loads(TARGET.read_text())
    result = compute(data, extra)
    if args.check:
        assert result == extra['expected']
        print('PASS: exact global marked norm; canonical 43-adic parameter; AH coordinates (20,29), (24,20); beta=8; normalized=(0,41)')
    else:
        print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
