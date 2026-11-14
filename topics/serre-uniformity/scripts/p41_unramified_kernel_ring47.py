#!/usr/bin/env python3
"""Small sparse unramified extensions for actual prime-to-47 isogeny kernels.

Polynomial multiplication uses carry-free integer packing.  Irreducibility
is certified by the full Rabin criterion; unit inversion first works in the
residue field and then uses Newton lifting.  No external algebra package.
"""
from math import isqrt
from p41_etale_torsion_lift47 import QuadraticRing


def prime_divisors(n):
    out = []
    for p in range(2, isqrt(n)+1):
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
    if n > 1:
        out.append(n)
    return out


def polynomial_gcd(a, b, p=47):
    a, b = list(a), list(b)
    while a and a[-1] % p == 0:
        a.pop()
    while b and b[-1] % p == 0:
        b.pop()
    while b:
        c = a[:]
        inv = pow(b[-1], -1, p)
        while len(c) >= len(b):
            k = len(c)-len(b)
            v = c[-1]*inv % p
            for j in range(len(b)):
                c[k+j] = (c[k+j]-v*b[j]) % p
            while c and c[-1] == 0:
                c.pop()
        a, b = b, c
    if not a:
        return []
    inv = pow(a[-1], -1, p)
    return [v*inv % p for v in a]


class SparseUnramifiedRing:
    def __init__(self, polynomial, precision=1):
        assert polynomial[-1] == 1
        self.polynomial = tuple(polynomial)
        self.degree = len(polynomial)-1
        self.precision = precision
        self.modulus = 47**precision
        self.zero = (0,)*self.degree
        self.one = (1,)+(0,)*(self.degree-1)
        self.generator = (0,1)+(0,)*(self.degree-2)
        self.lower = tuple((j,c % self.modulus) for j,c in enumerate(polynomial[:-1]) if c)
        self.pack_bits = (self.degree*(self.modulus-1)**2).bit_length()
        self.pack_mask = (1 << self.pack_bits)-1
        self._residue = self if precision == 1 else None

    def integer(self, n):
        return (n % self.modulus,)+(0,)*(self.degree-1)

    def add(self, a, b):
        q = self.modulus
        return tuple((x+y) % q for x,y in zip(a,b))

    def neg(self, a):
        return tuple(-x % self.modulus for x in a)

    def sub(self, a, b):
        q = self.modulus
        return tuple((x-y) % q for x,y in zip(a,b))

    def scale(self, a, n):
        return tuple(x*n % self.modulus for x in a)

    def mul(self, a, b):
        # Every unreduced convolution coefficient is strictly below 2^pack_bits.
        x = y = 0
        for c in reversed(a):
            x = (x << self.pack_bits) | c
        for c in reversed(b):
            y = (y << self.pack_bits) | c
        z = x*y
        c = []
        for _ in range(2*self.degree-1):
            c.append((z & self.pack_mask) % self.modulus)
            z >>= self.pack_bits
        assert z == 0
        for k in range(2*self.degree-2, self.degree-1, -1):
            v = c[k]
            if v:
                for j, coefficient in self.lower:
                    c[k-self.degree+j] = (c[k-self.degree+j]-v*coefficient) % self.modulus
        return tuple(c[:self.degree])

    power = QuadraticRing.power

    def is_unit(self, a):
        return any(v % 47 for v in a)

    def residue_ring(self):
        if self._residue is None:
            self._residue = SparseUnramifiedRing(self.polynomial, 1)
        return self._residue

    def inverse(self, a):
        assert self.is_unit(a), 'Only unit inversions are allowed'
        F = self.residue_ring()
        b = F.power(tuple(v % 47 for v in a), 47**self.degree-2)
        attained = 1
        while attained < self.precision:
            b = self.mul(b, self.sub(self.integer(2), self.mul(a,b)))
            attained *= 2
        assert self.mul(a,b) == self.one
        return b

    def polynomial_value(self, coefficients, x):
        out = self.zero
        for c in reversed(coefficients):
            out = self.add(self.mul(out,x), self.integer(c))
        return out

    def is_irreducible(self):
        assert self.precision == 1
        checks = {self.degree//p for p in prime_divisors(self.degree)}
        t = self.generator
        for k in range(1, self.degree+1):
            t = self.power(t, 47)
            if k in checks:
                if len(polynomial_gcd(self.sub(t,self.generator), self.polynomial)) != 1:
                    return False
        return t == self.generator


def sparse_irreducible(degree):
    assert degree >= 2
    if degree == 2:
        return [1,0,1]
    # A finite exhaustive sparse search, followed by no unsupported fallback.
    for k in [2,1]+list(range(3,degree)):
        for a in range(1,47):
            for b in range(1,47):
                f = [0]*(degree+1)
                f[0],f[k],f[-1] = b,a,1
                if SparseUnramifiedRing(f).is_irreducible():
                    return f
    raise ArithmeticError('No sparse irreducible polynomial found')


def nonsquare(F):
    assert F.precision == 1
    q = 47**F.degree
    for n in range(2,10000):
        # Enumerate field elements, not just prime-field constants (all are squares here).
        v = n
        a = []
        for _ in range(F.degree):
            a.append(v % 47)
            v //= 47
        a = tuple(a)
        if F.power(a,(q-1)//2) == F.neg(F.one):
            return a
    raise ArithmeticError('Deterministic nonsquare search exhausted')


def square_root(a, F, z):
    """Deterministic Tonelli--Shanks in the certified finite field."""
    assert F.precision == 1
    if a == F.zero:
        return F.zero
    q = 47**F.degree
    if F.power(a,(q-1)//2) != F.one:
        return None
    t,s = q-1,0
    while t % 2 == 0:
        t //= 2
        s += 1
    c = F.power(z,t)
    x = F.power(a,(t+1)//2)
    b = F.power(a,t)
    m = s
    while b != F.one:
        v,i = b,0
        while v != F.one and i < m:
            v = F.mul(v,v)
            i += 1
        assert 0 < i < m
        v = F.power(c,1 << (m-i-1))
        x = F.mul(x,v)
        c = F.mul(v,v)
        b = F.mul(b,c)
        m = i
    assert F.mul(x,x) == a
    return min(x,F.neg(x))


def square_root_minus_one(R, z):
    F = R.residue_ring()
    i = F.power(z,(47**R.degree-1)//4)
    i = min(i,F.neg(i))
    assert F.mul(i,i) == F.neg(F.one)
    attained = 1
    while attained < R.precision:
        i = R.sub(i,R.mul(R.add(R.mul(i,i),R.one),R.inverse(R.scale(i,2))))
        attained *= 2
    assert R.mul(i,i) == R.neg(R.one)
    return i


def embed_quadratic(a, i, R):
    return R.add(R.integer(a[0]),R.scale(i,a[1]))


def extract_quadratic(a, i, R):
    k = next(k for k in range(1,R.degree) if i[k] % 47)
    b = a[k]*pow(i[k],-1,R.modulus) % R.modulus
    c = (a[0]-b*i[0]) % R.modulus
    assert embed_quadratic((c,b),i,R) == a, 'Kernel coefficient has not descended to R2'
    return c,b
