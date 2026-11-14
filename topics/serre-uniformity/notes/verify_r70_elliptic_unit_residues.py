#!/usr/bin/env python3
"""Exact local Robert-unit projections for A: y^2=x^3-x, p=43.

Only Python's standard library is used.  See R70 for the interpretation.
Elements of F_(q^2) are pairs (a,b), meaning a+b*i with i^2=-1.
Run without arguments for the recorded certificates; --search enumerates
eligible primes until the first zero projection.  Every calculation is exact.
"""

import argparse
import hashlib
import json
from math import isqrt


def prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n) + 1, 2))


class Fq2:
    def __init__(self, q):
        assert prime(q) and q % 4 == 3
        self.q = q
        self.zero, self.one, self.i = (0, 0), (1, 0), (0, 1)

    def add(self, a, b):
        q = self.q
        return ((a[0] + b[0]) % q, (a[1] + b[1]) % q)

    def neg(self, a):
        return ((-a[0]) % self.q, (-a[1]) % self.q)

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        q = self.q
        return ((a[0]*b[0] - a[1]*b[1]) % q,
                (a[0]*b[1] + a[1]*b[0]) % q)

    def scale(self, n, a):
        return (n*a[0] % self.q, n*a[1] % self.q)

    def inv(self, a):
        q = self.q
        norm = (a[0]*a[0] + a[1]*a[1]) % q
        assert norm
        t = pow(norm, -1, q)
        return (a[0]*t % q, -a[1]*t % q)

    def div(self, a, b):
        return self.mul(a, self.inv(b))

    def power(self, a, n):
        if n < 0:
            a, n = self.inv(a), -n
        r = self.one
        while n:
            if n & 1:
                r = self.mul(r, a)
            a = self.mul(a, a)
            n >>= 1
        return r


class Curve:
    def __init__(self, field):
        self.f = field

    def on_curve(self, p):
        if p is None:
            return True
        f = self.f
        x, y = p
        return f.mul(y, y) == f.sub(f.power(x, 3), x)

    def add(self, p, r):
        if p is None:
            return r
        if r is None:
            return p
        f = self.f
        x, y = p
        z, w = r
        if x == z:
            if f.add(y, w) == f.zero:
                return None
            assert y == w
            slope = f.div(f.sub(f.scale(3, f.mul(x, x)), f.one),
                          f.scale(2, y))
        else:
            slope = f.div(f.sub(w, y), f.sub(z, x))
        xx = f.sub(f.sub(f.mul(slope, slope), x), z)
        yy = f.sub(f.mul(slope, f.sub(x, xx)), y)
        return (xx, yy)

    def mul(self, n, p):
        if n < 0:
            p, n = (p[0], self.f.neg(p[1])), -n
        r = None
        while n:
            if n & 1:
                r = self.add(r, p)
            p = self.add(p, p)
            n >>= 1
        return r

    def cm_i(self, p):
        if p is None:
            return None
        return (self.f.neg(p[0]), self.f.mul(self.f.i, p[1]))

    def division_values(self, p):
        """Division-polynomial recurrence, evaluated at one affine point."""
        f = self.f
        x, y = p
        xx, xxxx, xxxxxx = f.power(x, 2), f.power(x, 4), f.power(x, 6)
        cache = {0: f.zero, 1: f.one, 2: f.scale(2, y)}
        cache[3] = f.sub(f.sub(f.scale(3, xxxx), f.scale(6, xx)), f.one)
        cache[4] = f.mul(f.scale(4, y),
                         f.add(f.sub(f.sub(xxxxxx, f.scale(5, xxxx)),
                                     f.scale(5, xx)), f.one))

        def psi(n):
            if n in cache:
                return cache[n]
            m = n // 2
            if n & 1:
                result = f.sub(f.mul(psi(m+2), f.power(psi(m), 3)),
                               f.mul(psi(m-1), f.power(psi(m+1), 3)))
            else:
                result = f.div(f.mul(psi(m),
                    f.sub(f.mul(psi(m+2), f.power(psi(m-1), 2)),
                          f.mul(psi(m-2), f.power(psi(m+1), 2)))), psi(2))
            cache[n] = result
            return result
        return psi


def torsion_point(curve, p):
    """Choose a deterministic nonzero p-point in A(F_q)."""
    q = curve.f.q
    for x in range(2, q):
        rhs = (x*x*x - x) % q
        if not rhs or pow(rhs, (q-1)//2, q) != 1:
            continue
        y = pow(rhs, (q+1)//4, q)
        y = min(y, q-y)
        seed = ((x, 0), (y, 0))
        assert curve.on_curve(seed)
        point = curve.mul((q+1)//p, seed)
        if point is not None:
            assert curve.on_curve(point) and curve.mul(p, point) is None
            return seed, point
    raise AssertionError("no p-torsion point found")


def certificate(q, p=43):
    assert p == 43 and prime(p) and q % (4*p) == 4*p-1 and prime(q)
    f = Fq2(q)
    curve = Curve(f)
    p2 = (f.i, (1, q-1))
    assert curve.on_curve(p2)
    # Exact annihilator (1+i)^3, rather than only integer order four.
    t1 = curve.add(p2, curve.cm_i(p2))
    t2 = curve.add(t1, curve.cm_i(t1))
    t3 = curve.add(t2, curve.cm_i(t2))
    assert t1 == ((1, 0), (0, 0)) and t2 == ((0, 0), (0, 0)) and t3 is None
    seed, pp = torsion_point(curve, p)
    ip = curve.cm_i(pp)
    aa, bb = [None], [None]
    for _ in range(1, p):
        aa.append(curve.add(aa[-1], pp))
        bb.append(curve.add(bb[-1], ip))
    translated = [curve.add(p2, t) for t in aa]

    exponent = (q*q-1)//p
    for z in range(1, q):
        zeta = f.power((z, 1), exponent)
        if zeta != f.one:
            break
    assert f.power(zeta, p) == f.one
    logs, current = {}, f.one
    for j in range(p):
        assert current not in logs
        logs[current] = j
        current = f.mul(current, zeta)
    assert current == f.one and len(logs) == p

    total = [0, 0]
    rows = bytearray()
    seen = set()
    samples = []
    for u in range(p):
        for v in range(p):
            if u == v == 0:
                continue
            point = curve.add(translated[u], bb[v])
            assert point is not None and curve.on_curve(point)
            assert point not in seen
            seen.add(point)
            psi = curve.division_values(point)
            value = psi(11)
            assert value != f.zero
            residue = f.power(value, exponent)
            assert residue in logs
            ell = logs[residue]
            norminv = pow((u*u+v*v) % p, -1, p)
            # (u+vi)^(-p)=(u+vi)/(u^2+v^2) in F_(p^2).
            total[0] = (total[0] + ell*u*norminv) % p
            total[1] = (total[1] + ell*v*norminv) % p
            rows.extend((u, v, ell))
            if (u, v) in ((0, 1), (1, 0), (1, 1)):
                # Independent point-addition check on division-polynomial values.
                mult = curve.mul(11, point)
                expected_x = f.sub(point[0], f.div(f.mul(psi(10), psi(12)),
                                                 f.power(value, 2)))
                assert mult is not None and mult[0] == expected_x
                samples.append({"a": [u, v], "point": point,
                                "psi11": value, "residue": residue, "log": ell})
    assert len(seen) == p*p-1
    # Frobenius q sends P2 to i*P2, fixes Pp, and inverts zeta.
    # Therefore this choice of bases forces S=i*conjugate(S).
    assert total[0] == total[1]
    scale = 8*pow(7, -1, p) % p
    return {"p": p, "q": q, "seed": seed, "p_point": pp,
            "zeta_seed": [z, 1], "zeta": zeta,
            "exponent": exponent, "points": len(seen),
            "S": total, "u1_projection": [scale*t % p for t in total],
            "zero": total == [0, 0],
            "log_table_sha256": hashlib.sha256(rows).hexdigest(),
            "samples": samples}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("q", nargs="*", type=int)
    parser.add_argument("--search", action="store_true")
    args = parser.parse_args()
    if args.search:
        k = 1
        while True:
            q = 172*k-1
            k += 1
            if not prime(q):
                continue
            cert = certificate(q)
            print(json.dumps(cert, sort_keys=True), flush=True)
            if cert["zero"]:
                break
    else:
        for q in args.q or [859, 1031, 49019]:
            print(json.dumps(certificate(q), sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
