#!/usr/bin/env python3
"""Exact arithmetic certificate for the unique cubic-field cover in R126.

Uses only the Python standard library.  This certifies the algebraic
identities and the dyadic obstruction, not an elliptic rank or point list.
"""
import sys
sys.dont_write_bytecode = True
import argparse
import hashlib
import json
from fractions import Fraction as F
from itertools import product
from pathlib import Path


def determinant(M):
    M = [list(row) for row in M]
    n = len(M)
    ans = F(1)
    for j in range(n):
        k = next((i for i in range(j, n) if M[i][j]), None)
        if k is None:
            return F(0)
        if k != j:
            M[j], M[k] = M[k], M[j]
            ans = -ans
        pivot = M[j][j]
        ans *= pivot
        for i in range(j+1, n):
            t = M[i][j]/pivot
            for k in range(j+1, n):
                M[i][k] -= t*M[j][k]
    return ans


class L:
    """Q[r], r^3=3r+4, represented in the integral power basis."""
    def __init__(self, a=0, b=0, c=0):
        self.v = tuple(map(F, (a, b, c)))

    @staticmethod
    def coerce(a):
        return a if isinstance(a, L) else L(a)

    def __bool__(self):
        return any(self.v)

    def __eq__(self, other):
        return self.v == L.coerce(other).v

    def __add__(self, other):
        other = L.coerce(other)
        return L(*(a+b for a, b in zip(self.v, other.v)))

    __radd__ = __add__

    def __neg__(self):
        return L(*(-a for a in self.v))

    def __sub__(self, other):
        return self + -L.coerce(other)

    def __rsub__(self, other):
        return L.coerce(other) + -self

    def __mul__(self, other):
        other = L.coerce(other)
        a = [F(0)]*5
        for i, x in enumerate(self.v):
            for j, y in enumerate(other.v):
                a[i+j] += x*y
        a[2] += 3*a[4]
        a[1] += 4*a[4] + 3*a[3]
        a[0] += 4*a[3]
        return L(*a[:3])

    __rmul__ = __mul__

    def matrix(self):
        cols = [(self*L(*e)).v for e in [(1,0,0),(0,1,0),(0,0,1)]]
        return [list(row) for row in zip(*cols)]

    def norm(self):
        return determinant(self.matrix())

    def inverse(self):
        M = [row+[F(i == 0)] for i,row in enumerate(self.matrix())]
        for j in range(3):
            k = next(i for i in range(j,3) if M[i][j])
            M[j],M[k] = M[k],M[j]
            pivot = M[j][j]
            M[j] = [x/pivot for x in M[j]]
            for i in range(3):
                if i != j:
                    t = M[i][j]
                    M[i] = [x-t*y for x,y in zip(M[i],M[j])]
        result = L(*(row[3] for row in M))
        assert self*result == 1
        return result

    def __truediv__(self, other):
        return self*L.coerce(other).inverse()

    def __pow__(self, n):
        if n < 0:
            return self.inverse()**(-n)
        result, a = L(1), self
        while n:
            if n & 1:
                result *= a
            a *= a
            n //= 2
        return result

    def encoded(self):
        return [int(x) if x.denominator == 1 else str(x) for x in self.v]


def polymul(a,b):
    out = [L() for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j] += x*y
    return out


def value(a,x):
    ans = L()
    for c in reversed(a):
        ans = ans*x+c
    return ans


def resultant(a,b):
    # Rows are descending coefficient vectors of the shifted polynomials.
    n,m = len(a)-1,len(b)-1
    M = []
    for i in range(m):
        M.append([L()]*i+list(reversed(a))+[L()]*(m-i-1))
    for i in range(n):
        M.append([L()]*i+list(reversed(b))+[L()]*(n-i-1))
    return determinant(M)


def certificate():
    r = L(0,1)
    epsilon = r*r+r-7
    A = [r*r+r-1, -2*r*r-3*r-2, r*r+3*r+3]
    B = [-r*r+5*r-3, 6*r*r-17*r+6, -9*r*r+18*r+3,
         2*r*r-r-6, 3*r*r-5*r-3]
    S = [19,-72,84,-10,-36,12,7]
    assert polymul(A,B) == list(map(L,S))
    # The norm polynomial has degree <=6.  Seven exact values certify it.
    norm_values = []
    for x in range(7):
        n = value(A,x).norm()
        s = sum(c*x**i for i,c in enumerate(S))
        assert n == s
        norm_values.append([x,int(n)])
    R = resultant(A,B)
    assert R == L(19521,23652,10773)
    assert R.norm() == 2**8*3**14
    assert int(R.v[0]) % 2 == 1
    assert epsilon.norm() == 1
    assert (r+1).norm() == (r-2).norm() == 2
    theta = -r*r+r+3
    assert theta.norm() == 3
    assert (r-2)*(r+1)**2 == 2
    assert (r+1)*theta == r-1
    # There is no root of the cubic modulo5, so5 is inert.
    assert all((x**3-3*x-4) % 5 for x in range(5))
    # Every square in O_L/2 has zero r coefficient.
    squares = sorted({tuple(int(t) % 2 for t in (L(*a)**2).v)
                      for a in product(range(2),repeat=3)})
    assert all(t[1] == 0 for t in squares)
    assert (1,1,1) not in squares  # epsilon modulo2
    primitive_cases = []
    for u,v in [(1,0),(0,1),(1,1)]:
        a = A[2]*u*u+A[1]*u*v+A[0]*v*v
        residue = tuple(int(t) % 2 for t in a.v)
        assert residue[1] == 1 and residue not in squares
        primitive_cases.append([u,v,list(residue)])
    points = []
    for x,y,a,b in [(1,2,r*r+2*r+2,r*r+2*r+1),
                    (-1,12,4*r*r+9*r+8,r*r+4*r+1)]:
        assert value(A,x) == epsilon*a*a
        assert value(B,x) == epsilon*b*b
        assert epsilon*a*b == y
        points.append(dict(x=x,y=y,a=a.encoded(),b=b.encoded()))
    return dict(
        field_polynomial_ascending=[-4,-3,0,1],
        field_discriminant=-324,
        integral_basis=['1','r','r^2'],
        unit=epsilon.encoded(),
        quadratic_ascending=[a.encoded() for a in A],
        quartic_ascending=[a.encoded() for a in B],
        product_sextic_ascending=S,
        norm_quadratic_degree_bound=6,
        norm_identity_seven_values=norm_values,
        resultant=R.encoded(),resultant_norm=int(R.norm()),
        prime_generators=dict(norm2=[(r+1).encoded(),(r-2).encoded()],
                              norm3=theta.encoded()),
        squares_mod2=[list(a) for a in squares],
        primitive_dyadic_cases=primitive_cases,
        known_lifted_points=points,
        limitation='No elliptic rank bound or exhaustive rational point claim')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    data = certificate()
    raw = (json.dumps(data,indent=2,sort_keys=True)+'\n').encode()
    path = Path(__file__).with_name('r126_cubic_elliptic_cover_certificate.json')
    if args.write:
        path.write_bytes(raw)
    if args.check:
        assert path.read_bytes() == raw
    print('R126 exact identities and unique dyadic squareclass PASS')
    print('certificate SHA256',hashlib.sha256(raw).hexdigest())


if __name__ == '__main__':
    main()
