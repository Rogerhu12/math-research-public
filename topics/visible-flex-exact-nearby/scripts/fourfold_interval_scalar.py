#!/usr/bin/env python3
"""Small outward binary64 interval kernel, including a rational exp enclosure.

Elementary binary64 +,-,*,/ are assumed correctly rounded (IEEE 754).
Exponential bounds use exact Fraction Taylor sums, a proved geometric
remainder, and outward repeated squaring. No library transcendental value
is used as an endpoint. These routines are for modest finite arguments.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
import math
import sys


def floor_float(value):
    answer = float(value)
    while Fraction.from_float(answer) > value:
        answer = math.nextafter(answer, -math.inf)
    return answer


def ceiling_float(value):
    answer = float(value)
    while Fraction.from_float(answer) < value:
        answer = math.nextafter(answer, math.inf)
    return answer


@dataclass(frozen=True)
class Interval:
    lo: float
    hi: float

    def __post_init__(self):
        if math.isnan(self.lo) or math.isnan(self.hi) or self.lo > self.hi:
            raise ValueError('invalid interval')

    @classmethod
    def point(cls, value):
        x = float(value)
        return cls(x, x)

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Interval) else Interval.point(value)

    def __add__(self, other):
        other = self.coerce(other)
        return Interval(math.nextafter(self.lo+other.lo, -math.inf),
                        math.nextafter(self.hi+other.hi, math.inf))

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self+-self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other)+-self

    def __mul__(self, other):
        other = self.coerce(other)
        products = (self.lo*other.lo, self.lo*other.hi,
                    self.hi*other.lo, self.hi*other.hi)
        return Interval(math.nextafter(min(products), -math.inf),
                        math.nextafter(max(products), math.inf))

    __rmul__ = __mul__

    def reciprocal(self):
        if self.lo <= 0 <= self.hi:
            raise ZeroDivisionError('interval contains zero')
        return Interval(math.nextafter(1/self.hi, -math.inf),
                        math.nextafter(1/self.lo, math.inf))

    def __truediv__(self, other):
        return self*self.coerce(other).reciprocal()

    def __rtruediv__(self, other):
        return self.coerce(other)*self.reciprocal()

    def __pow__(self, power):
        if not isinstance(power, int):
            raise ValueError('only integer powers are supported')
        if power < 0:
            return self.reciprocal()**(-power)
        result, factor = Interval.point(1), self
        while power:
            if power & 1:
                result *= factor
            power //= 2
            if power:
                factor *= factor
        return result


@lru_cache(maxsize=32768)
def exp_point(value):
    """Enclose exp of one exact binary64 argument, without calling exp.

    For 0<=y<=1/8, S_N=sum_{j=0}^N y^j/j! is a lower bound, and
    S_N + (y^(N+1)/(N+1)!)/(1-y/(N+2)) is an upper bound. Use N=24.
    Rational sums/conversion comparisons are exact; squaring is outward.
    """
    x = float(value)
    if sys.float_info.radix != 2 or sys.float_info.mant_dig != 53:
        raise RuntimeError('this kernel requires IEEE binary64 Python floats')
    if not math.isfinite(x) or abs(x) > 700:
        raise ValueError('exp kernel expects a finite argument of absolute value <=700')
    if x == 0:
        return Interval.point(1)
    if x < 0:
        return exp_point(-x).reciprocal()
    y = Fraction.from_float(x)
    squarings = 0
    while y > Fraction(1, 8):
        y /= 2
        squarings += 1
    term = total = Fraction(1)
    for index in range(1, 25):
        term *= y/index
        total += term
    next_term = term*y/25
    remainder = next_term/(1-y/26)
    answer = Interval(floor_float(total), ceiling_float(total+remainder))
    for _ in range(squarings):
        answer *= answer
    return answer


def interval_exp(value):
    value = Interval.coerce(value)
    return Interval(exp_point(value.lo).lo, exp_point(value.hi).hi)
