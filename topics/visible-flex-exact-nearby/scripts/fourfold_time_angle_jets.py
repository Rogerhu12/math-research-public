#!/usr/bin/env python3
"""Directed rectangular Taylor jets in time u and initial-angle v.

The algebra is C[u,v]/(u**m,v**n), with Arb complex balls as enclosures.
Products use acb_poly with Kronecker stride 2*m-1, followed by explicit
rectangular truncation. The stride prevents a discarded high time power
from being mistaken for a low time power in the next angle coefficient.
No analytic remainder is asserted by this algebra module.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import math
import time

from flint import acb, acb_poly, acb_series, arb, ctx


def ball(value):
    if isinstance(value, acb):
        return value
    if isinstance(value, Fraction):
        return acb(arb(value.numerator)/value.denominator)
    if isinstance(value, complex):
        return acb(arb(value.real), arb(value.imag))
    return acb(value)


class TimeAngleJet:
    """Rows indexed by angle order; columns by time order, both normalized."""

    __slots__ = ('m', 'n', 'stride', 'p')
    __array_priority__ = 10000

    def __init__(self, rows, *, time_precision, angle_precision):
        self.m, self.n = int(time_precision), int(angle_precision)
        if self.m < 1 or self.n < 1:
            raise ValueError('positive rectangular precisions are required')
        self.stride = 2*self.m-1
        if len(rows) > self.n or any(len(row) > self.m for row in rows):
            raise ValueError('too many supplied Taylor coefficients')
        values = [acb(0)]*(self.stride*(self.n-1)+self.m)
        for j, row in enumerate(rows):
            for i, value in enumerate(row):
                values[j*self.stride+i] = ball(value)
        self.p = acb_poly(values)

    @classmethod
    def constant(cls, value, *, time_precision, angle_precision):
        return cls([[value]], time_precision=time_precision, angle_precision=angle_precision)

    @classmethod
    def from_time_series(cls, series, *, time_precision, angle_precision):
        if series.prec < time_precision:
            raise ValueError('unknown time coefficients cannot be filled with zero')
        return cls([[series[i] for i in range(time_precision)]],
                   time_precision=time_precision, angle_precision=angle_precision)

    @classmethod
    def variable(cls, axis, *, time_precision, angle_precision):
        if axis == 'time' and time_precision >= 2:
            rows = [[0, 1]]
        elif axis == 'angle' and angle_precision >= 2:
            rows = [[0], [1]]
        else:
            raise ValueError('variable absent at this precision')
        return cls(rows, time_precision=time_precision, angle_precision=angle_precision)

    def _new(self, polynomial, *, truncate=False):
        result = object.__new__(TimeAngleJet)
        result.m, result.n, result.stride = self.m, self.n, self.stride
        if truncate:
            values = [acb(0)]*(self.stride*(self.n-1)+self.m)
            for j in range(self.n):
                for i in range(self.m):
                    values[j*self.stride+i] = polynomial[j*self.stride+i]
            result.p = acb_poly(values)
        else:
            result.p = polynomial
        return result

    def coefficient(self, time_order, angle_order):
        if not 0 <= time_order < self.m or not 0 <= angle_order < self.n:
            raise IndexError('coefficient lies outside the known rectangle')
        return self.p[angle_order*self.stride+time_order]

    def rows(self):
        return [[self.coefficient(i, j) for i in range(self.m)] for j in range(self.n)]

    def _constant(self, value):
        return TimeAngleJet.constant(value, time_precision=self.m, angle_precision=self.n)

    def _coerce(self, other):
        if isinstance(other, TimeAngleJet):
            if (other.m, other.n) != (self.m, self.n):
                raise ValueError('mixed jet precisions')
            return other
        if isinstance(other, acb_series):
            return TimeAngleJet.from_time_series(other, time_precision=self.m, angle_precision=self.n)
        return self._constant(other)

    def __add__(self, other):
        return self._new(self.p+self._coerce(other).p)

    __radd__ = __add__

    def __neg__(self):
        return self._new(-self.p)

    def __sub__(self, other):
        return self._new(self.p-self._coerce(other).p)

    def __rsub__(self, other):
        return self._coerce(other)-self

    def __mul__(self, other):
        if not isinstance(other, (TimeAngleJet, acb_series)):
            return self._new(self.p*ball(other))
        other = self._coerce(other)
        if other.p.degree() < self.m or self.p.degree() < self.m:
            left, right = (self, other) if other.p.degree() < self.m else (other, self)
            old = ctx.cap
            ctx.cap = self.m
            try:
                factor = acb_series([right.coefficient(i,0) for i in range(self.m)], prec=self.m)
                rows=[]
                for j in range(self.n):
                    value=acb_series([left.coefficient(i,j) for i in range(self.m)],prec=self.m)*factor
                    rows.append([value[i] for i in range(self.m)])
                return TimeAngleJet(rows,time_precision=self.m,angle_precision=self.n)
            finally:
                ctx.cap=old
        return self._new(self.p*other.p, truncate=True)

    __rmul__ = __mul__

    def __truediv__(self, other):
        if not isinstance(other, (TimeAngleJet, acb_series)):
            return self._new(self.p*(1/ball(other)))
        return self*self._coerce(other).inverse()

    def __rtruediv__(self, other):
        return self._coerce(other)*self.inverse()

    def __pow__(self, exponent):
        if not isinstance(exponent, int):
            raise TypeError('only integer jet powers are implicit')
        if exponent < 0:
            return self.inverse()**(-exponent)
        result, factor = self._constant(1), self
        while exponent:
            if exponent & 1:
                result = result*factor
            exponent >>= 1
            if exponent:
                factor = factor*factor
        return result

    def _time_function(self, name):
        old = ctx.cap
        ctx.cap = self.m
        try:
            constant = acb_series([self.coefficient(i, 0) for i in range(self.m)], prec=self.m)
            if name == 'inverse':
                value = 1/constant
            else:
                value = getattr(constant, name)()
            if any(not value[i].is_finite() for i in range(self.m)):
                raise ValueError('time-constant analytic function is unresolved')
            return TimeAngleJet.from_time_series(value, time_precision=self.m, angle_precision=self.n)
        finally:
            ctx.cap = old

    def _positive_angle_part(self):
        # Exact projection onto positive angular degree. This avoids falsely
        # treating subtraction of a ball from itself as an exact cancellation.
        rows = [[0]*self.m]+[[self.coefficient(i, j) for i in range(self.m)]
                            for j in range(1, self.n)]
        return TimeAngleJet(rows, time_precision=self.m, angle_precision=self.n)

    def inverse(self):
        return self._angular_function('inverse')

    def exp(self):
        return self._angular_function('exp')

    def log(self):
        return self._angular_function('log')

    def sqrt(self):
        return self._angular_function('sqrt')

    def _angular_function(self, operation):
        """Formal angular recurrences over native truncated time series.

        This is much faster than repeated large packed products for elementary
        functions. It is the same rectangular quotient algebra: all angular
        convolutions explicitly stop at n, all native time products at m.
        """
        old = ctx.cap
        ctx.cap = self.m
        try:
            f = [acb_series([self.coefficient(i,j) for i in range(self.m)], prec=self.m)
                 for j in range(self.n)]
            zero = acb_series([], prec=self.m)
            if operation == 'inverse':
                g = [1/f[0]]
                for j in range(1, self.n):
                    g.append(-g[0]*sum((f[k]*g[j-k] for k in range(1,j+1)), zero))
            elif operation == 'exp':
                g = [f[0].exp()]
                for j in range(1, self.n):
                    g.append(sum((k*f[k]*g[j-k] for k in range(1,j+1)), zero)/j)
            elif operation == 'sqrt':
                g = [f[0].sqrt()]
                inverse_two = 1/(2*g[0])
                for j in range(1, self.n):
                    g.append((f[j]-sum((g[k]*g[j-k] for k in range(1,j)), zero))*inverse_two)
            elif operation == 'log':
                inverse = [1/f[0]]
                for j in range(1, self.n):
                    inverse.append(-inverse[0]*sum((f[k]*inverse[j-k] for k in range(1,j+1)), zero))
                g = [f[0].log()]
                for j in range(1, self.n):
                    g.append(sum((k*f[k]*inverse[j-k] for k in range(1,j+1)), zero)/j)
            else:
                raise ValueError('unknown formal function')
            if any(not g[j][i].is_finite() for i in range(self.m) for j in range(self.n)):
                raise ValueError('formal analytic function has an unresolved coefficient')
            return TimeAngleJet([[g[j][i] for i in range(self.m)] for j in range(self.n)],
                                time_precision=self.m, angle_precision=self.n)
        finally:
            ctx.cap = old

    def sin_cos(self):
        plus, minus = (acb(0, 1)*self).exp(), (-acb(0, 1)*self).exp()
        return (plus-minus)/acb(0, 2), (plus+minus)/2

    def sin(self):
        return self.sin_cos()[0]

    def cos(self):
        return self.sin_cos()[1]

    def bound(self, time_radius=1, angle_radius=1):
        tr, ar = ball(time_radius).real, ball(angle_radius).real
        if not tr >= 0 or not ar >= 0:
            raise ValueError('nonnegative radii are required')
        return sum((abs(self.coefficient(i, j))*tr**i*ar**j
                    for j in range(self.n) for i in range(self.m)), arb(0)).upper()

    def add_cauchy_error(self, error, time_radius, angle_radius, *, real=False):
        error, tr, ar = arb(error), arb(time_radius), arb(angle_radius)
        if not error >= 0 or not tr > 0 or not ar > 0:
            raise ValueError('invalid analytic error budget')
        rows = self.rows()
        for j in range(self.n):
            for i in range(self.m):
                fee = (error/(tr**i*ar**j)).upper()
                z = rows[j][i]
                rows[j][i] = acb(z.real+arb(0, fee), 0 if real else z.imag+arb(0, fee))
        return TimeAngleJet(rows, time_precision=self.m, angle_precision=self.n)


def self_check():
    """Exact independent coefficients, including a deliberate carry trap."""
    ctx.prec = 192
    m, n = 7, 8
    kw = dict(time_precision=m, angle_precision=n)
    u, v = TimeAngleJet.variable('time', **kw), TimeAngleJet.variable('angle', **kw)
    def contains_rational(value, expected):
        # Do not compare with a separately rounded Arb enclosure of 1/120,
        # etc.: one valid enclosure need not contain another valid enclosure.
        # The outward Arb endpoints are exact dyadics, compared as Fractions.
        ends=[]
        for endpoint in (value.real.lower(), value.real.upper()):
            mantissa, exponent = endpoint.man_exp()
            ends.append(Fraction(int(mantissa))*Fraction(2)**int(exponent))
        return ends[0] <= expected <= ends[1] and value.imag.contains(0)
    functions = [(1/(1-u-v), lambda i,j:Fraction(math.comb(i+j, i))),
                 ((u+v).exp(), lambda i,j:Fraction(1, math.factorial(i)*math.factorial(j)))]
    for value, expected in functions:
        for j in range(n):
            for i in range(m):
                if not contains_rational(value.coefficient(i, j), expected(i,j)):
                    raise AssertionError(('independent coefficient mismatch', i, j))
    for value in [(u**(m-1))*(u**(m-1)), (v**(n-1))*(v**(n-1))]:
        if any(value.coefficient(i,j) != 0 for i in range(m) for j in range(n)):
            raise AssertionError('high-degree carry entered the retained rectangle')
    root = (1+u+v).sqrt()
    log = (1+u+v).log()
    for j in range(n):
        for i in range(m):
            k = i+j
            choose = Fraction(1)
            for q in range(1, k+1):
                choose *= Fraction(3-2*q, 2*q)
            expected_root = choose*math.comb(k, i)
            expected_log = Fraction(0) if k == 0 else Fraction((-1)**(k+1)*math.comb(k, i), k)
            if not contains_rational(root.coefficient(i,j), expected_root) or not contains_rational(log.coefficient(i,j), expected_log):
                raise AssertionError(('root/log coefficient mismatch', i, j))
    sine, cosine = (u+v).sin_cos()
    for j in range(n):
        for i in range(m):
            k = i+j
            ss = Fraction((-1)**((k-1)//2), math.factorial(i)*math.factorial(j)) if k%2 else Fraction(0)
            cc = Fraction((-1)**(k//2), math.factorial(i)*math.factorial(j)) if k%2 == 0 else Fraction(0)
            if not contains_rational(sine.coefficient(i,j), ss) or not contains_rational(cosine.coefficient(i,j), cc):
                raise AssertionError(('trigonometric coefficient mismatch', i, j))
    print('All independent rational coefficient and carry-trap checks passed.', flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--self-check', action='store_true')
    args = parser.parse_args()
    if args.self_check:
        start = time.monotonic()
        self_check()
        print('seconds', time.monotonic()-start, flush=True)
