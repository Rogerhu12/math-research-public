#!/usr/bin/env python3
"""Integral prime-to-47 torsion retraction, including three deformation jets.

The Jacobian multiplication and cubic invariant-vector-field flow below work
over any supplied ring.  The executable certificate independently compares
them with division-polynomial Hensel lifting for every nonzero 3-torsion point
on two curves.  It does not claim to have constructed all remaining kernels.
"""
import argparse
import hashlib
import json
from pathlib import Path


class QuadraticRing:
    """(Z/modulus)[i], i^2=-1; modulus is a power of 47."""
    zero = (0, 0)
    one = (1, 0)

    def __init__(self, modulus=47**4):
        self.modulus = modulus

    def integer(self, n):
        return (n % self.modulus, 0)

    def add(self, a, b):
        return ((a[0]+b[0]) % self.modulus, (a[1]+b[1]) % self.modulus)

    def neg(self, a):
        return (-a[0] % self.modulus, -a[1] % self.modulus)

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        return ((a[0]*b[0]-a[1]*b[1]) % self.modulus,
                (a[0]*b[1]+a[1]*b[0]) % self.modulus)

    def scale(self, a, n):
        return (a[0]*n % self.modulus, a[1]*n % self.modulus)

    def is_unit(self, a):
        return (a[0]*a[0]+a[1]*a[1]) % 47 != 0

    def inverse(self, a):
        assert self.is_unit(a), 'Only unit inversions are allowed'
        v = pow((a[0]*a[0]+a[1]*a[1]) % self.modulus, -1, self.modulus)
        return (a[0]*v % self.modulus, -a[1]*v % self.modulus)

    def power(self, a, n):
        out = self.one
        while n:
            if n & 1:
                out = self.mul(out, a)
            a = self.mul(a, a)
            n >>= 1
        return out

    def conjugate(self, a):
        return (a[0], -a[1] % self.modulus)


class CubicJets:
    """R[t]/t^4, with all four coefficients retained at full base precision."""
    def __init__(self, base):
        self.base = base
        self.zero = (base.zero,)*4
        self.one = (base.one,)+(base.zero,)*3

    def constant(self, a):
        return (a,)+(self.base.zero,)*3

    def integer(self, n):
        return self.constant(self.base.integer(n))

    def add(self, a, b):
        return tuple(self.base.add(x, y) for x, y in zip(a, b))

    def neg(self, a):
        return tuple(self.base.neg(x) for x in a)

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        out = [self.base.zero]*4
        for k in range(4):
            for j in range(k+1):
                out[k] = self.base.add(out[k], self.base.mul(a[j], b[k-j]))
        return tuple(out)

    def scale(self, a, n):
        return tuple(self.base.scale(x, n) for x in a)

    def is_unit(self, a):
        return self.base.is_unit(a[0])

    def inverse(self, a):
        assert self.is_unit(a), 'Only unit inversions are allowed'
        b = [self.base.inverse(a[0])]+[self.base.zero]*3
        for n in range(1, 4):
            total = self.base.zero
            for j in range(1, n+1):
                total = self.base.add(total, self.base.mul(a[j], b[n-j]))
            b[n] = self.base.neg(self.base.mul(b[0], total))
        return tuple(b)

    power = QuadraticRing.power


def curve_value(x, A, B, R):
    return R.add(R.add(R.power(x, 3), R.mul(A, x)), B)


def lift_ordinate(x, y, A, B, R):
    # Two Newton steps suffice for (47)^4 or (t)^4 from an exact residue point.
    for _ in range(2):
        error = R.sub(R.mul(y, y), curve_value(x, A, B, R))
        y = R.sub(y, R.mul(error, R.inverse(R.scale(y, 2))))
    assert R.mul(y, y) == curve_value(x, A, B, R)
    return y


def jacobian_double(P, A, R):
    X, Y, Z = P
    y2 = R.mul(Y, Y)
    S = R.scale(R.mul(X, y2), 4)
    M = R.add(R.scale(R.mul(X, X), 3), R.mul(A, R.power(Z, 4)))
    X3 = R.sub(R.mul(M, M), R.scale(S, 2))
    Y3 = R.sub(R.mul(M, R.sub(S, X3)), R.scale(R.mul(y2, y2), 8))
    Z3 = R.scale(R.mul(Y, Z), 2)
    assert R.is_unit(Y3) or R.is_unit(Z3)
    return X3, Y3, Z3


def jacobian_add(P, Q, R):
    X1, Y1, Z1 = P
    X2, Y2, Z2 = Q
    U1, U2 = R.mul(X1, R.power(Z2, 2)), R.mul(X2, R.power(Z1, 2))
    S1, S2 = R.mul(Y1, R.power(Z2, 3)), R.mul(Y2, R.power(Z1, 3))
    H, v = R.sub(U2, U1), R.sub(S2, S1)
    H2 = R.mul(H, H)
    H3 = R.mul(H2, H)
    X3 = R.sub(R.sub(R.mul(v, v), H3), R.scale(R.mul(U1, H2), 2))
    Y3 = R.sub(R.mul(v, R.sub(R.mul(U1, H2), X3)), R.mul(S1, H3))
    Z3 = R.mul(H, R.mul(Z1, Z2))
    assert R.is_unit(Y3) or R.is_unit(Z3), 'Nonprimitive Jacobian result'
    return X3, Y3, Z3


def jacobian_multiply_prime(P, ell, A, R):
    """Left-to-right chain, for a residue point of exact odd prime order ell.

    Each proper prefix is between 1 and ell-1.  Intermediate additions never
    add equal residue points; the final opposite-residue addition is valid
    without inverting its nonunit x-coordinate difference.
    """
    assert ell > 2 and ell % 2 and ell % 47
    base = (P[0], P[1], R.one)
    out = base
    for bit in bin(ell)[3:]:
        out = jacobian_double(out, A, R)
        if bit == '1':
            out = jacobian_add(out, base, R)
    return out


def retract_torsion(P, ell, A, B, R):
    """Retract to ell-torsion when the resulting formal parameter has t^4=0."""
    x, y = P
    assert R.mul(y, y) == curve_value(x, A, B, R)
    X, Y, Z = jacobian_multiply_prime(P, ell, A, R)
    t = R.neg(R.mul(R.mul(X, Z), R.inverse(Y)))
    assert R.power(t, 4) == R.zero
    u = R.neg(R.mul(t, R.inverse(R.integer(ell))))
    u2, u3 = R.power(u, 2), R.power(u, 3)
    x2, x3 = R.mul(x, x), R.power(x, 3)
    c = R.add(R.scale(x2, 3), A)
    xx = R.add(x, R.add(R.scale(R.mul(y, u), 2),
                       R.add(R.mul(c, u2), R.scale(R.mul(R.mul(x, y), u3), 4))))
    d = R.add(R.scale(x3, 10), R.add(R.scale(R.mul(A, x), 6), R.scale(B, 4)))
    yy = R.add(y, R.add(R.mul(c, u),
                       R.add(R.scale(R.mul(R.mul(x, y), u2), 6), R.mul(d, u3))))
    assert R.mul(yy, yy) == curve_value(xx, A, B, R)
    X1, Y1, Z1 = jacobian_multiply_prime((xx, yy), ell, A, R)
    assert Z1 == R.zero and R.is_unit(X1) and R.is_unit(Y1)
    return (xx, yy), t


def psi3(x, A, B, R):
    return R.sub(R.add(R.scale(R.power(x, 4), 3),
                       R.add(R.scale(R.mul(A, R.power(x, 2)), 6),
                             R.scale(R.mul(B, x), 12))), R.mul(A, A))


def psi3_prime(x, A, B, R):
    return R.scale(curve_value(x, A, B, R), 12)


def independent_division_lift(x, y, A, B, R):
    for _ in range(2):
        x = R.sub(x, R.mul(psi3(x, A, B, R), R.inverse(psi3_prime(x, A, B, R))))
    assert psi3(x, A, B, R) == R.zero
    return x, lift_ordinate(x, y, A, B, R)


def verify():
    F, R = QuadraticRing(47), QuadraticRing()
    J = CubicJets(R)
    sqrt = {}
    for a in range(47):
        for b in range(47):
            z = (a, b)
            sqrt.setdefault(F.mul(z, z), []).append(z)
    rows = []
    constant_checks = jet_checks = 0
    for name, av, bv, aj, bj in [
            ('CM4', -1, 0, [-1,2,3,1], [0,5,7,1]),
            ('actual_source_j9', 1, 32, [1,0,0,0], [32,1,0,0])]:
        A, B = R.integer(av), R.integer(bv)
        Af, Bf = F.integer(av), F.integer(bv)
        Aj, Bj = tuple(map(R.integer, aj)), tuple(map(R.integer, bj))
        points = []
        for a in range(47):
            for b in range(47):
                x = (a, b)
                if psi3(x, Af, Bf, F) == F.zero:
                    points += [(x, y) for y in sqrt[curve_value(x, Af, Bf, F)]]
        assert len(points) == 8
        curve_rows = []
        for x0, y0 in points:
            expected = independent_division_lift(x0, y0, A, B, R)
            corrections = []
            for c in range(6):
                x = R.add(x0, R.scale((c+3*c*c, 2*c+1), 47))
                y = R.add(y0, R.scale((c+2, c*c), 47))
                y = lift_ordinate(x, y, A, B, R)
                actual, t = retract_torsion((x, y), 3, A, B, R)
                assert actual == expected
                assert all(v % 47 == 0 for v in t)
                corrections.append(t)
                constant_checks += 1
            xj, yj = J.constant(expected[0]), J.constant(expected[1])
            target = independent_division_lift(xj, yj, Aj, Bj, J)
            for c in range(3):
                startx = (expected[0], R.integer(c), (c, c+1), R.integer(c*c+3))
                starty = lift_ordinate(startx, yj, Aj, Bj, J)
                actual, t = retract_torsion((startx, starty), 3, Aj, Bj, J)
                assert t[0] == R.zero and actual == target
                jet_checks += 1
            curve_rows.append({'residue': [x0,y0], 'torsion': expected,
                               'initial_formal_parameters': corrections, 'torsion_jets': target})
        # Both chosen deformation families are rational; verify coefficientwise Frobenius.
        by_residue = {(tuple(e['residue'][0]), tuple(e['residue'][1])): e for e in curve_rows}
        for e in curve_rows:
            f = by_residue[tuple(F.conjugate(v) for v in e['residue'])]
            assert tuple(R.conjugate(v) for v in e['torsion']) == f['torsion']
            assert tuple(tuple(R.conjugate(v) for v in point) for point in e['torsion_jets']) == f['torsion_jets']
        rows.append({'curve':name,'A_jets':aj,'B_jets':bj,'all_nonzero_3_torsion_points':curve_rows,
                     'Frobenius':True})
    assert constant_checks == 96 and jet_checks == 48
    return {'p':47,'precision':47**4,'deformation_order':3,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'constant_lifts_independently_matched':constant_checks,
            'jet_lifts_independently_matched':jet_checks,
            'unit_inversions_only':True,'all_3_torsion_checks':True,'rows':rows,
            'scope':'General integral retraction formula; actual full 3-torsion tests on two curves. No claim of all remaining Hecke kernels.'}


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    result = verify()
    raw = (json.dumps(result, indent=2)+'\n').encode()
    args.output.write_bytes(raw)
    print(json.dumps({'constant_checks':result['constant_lifts_independently_matched'],
                      'jet_checks':result['jet_lifts_independently_matched'],
                      'sha256':hashlib.sha256(raw).hexdigest()}))
