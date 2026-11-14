"""Tight binary64 enclosures of exp/log via exact rational series.

The libm result is never used as an enclosure endpoint. Rational exp is
rounded outward to a 200-bit dyadic grid after each squaring; the final
conversion compares the exact rational endpoint against binary64.
"""
from fractions import Fraction as Q
from functools import lru_cache
import importlib.util
import math
from pathlib import Path
import numpy as np

backend = Path(__file__).with_name('db6f-audit-continuous-hermite.py')
spec = importlib.util.spec_from_file_location('db6f_tight_interval_backend', backend)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
I, qbounds = mod.I, mod.qbounds

BITS = 200
SCALE = 1 << BITS


def downq(x):
    return Q((x.numerator*SCALE)//x.denominator, SCALE)


def upq(x):
    return Q(-((-x.numerator*SCALE)//x.denominator), SCALE)


@lru_cache(maxsize=200000)
def exp_point(x):
    """Outward binary64 pair enclosing exp of the exact input float."""
    if not math.isfinite(x):
        raise ValueError('finite exponential argument required')
    if x == 0:
        return 1., 1.
    a = Q.from_float(x)
    k = max(0, math.ceil(math.log2(abs(x)*8))) if abs(x)*8 else 0
    while abs(a) > Q(1 << k, 8):
        k += 1
    y = a / (1 << k)
    term, value = Q(1), Q(1)
    for j in range(1, 19):
        term = term*y/j
        value += term
    rem = Q(8, 7)*Q(1, 8)**19/math.factorial(19)
    lo, hi = max(Q(0), downq(value-rem)), upq(value+rem)
    for _ in range(k):
        lo, hi = downq(lo*lo), upq(hi*hi)
    return float(qbounds(lo).lo), float(qbounds(hi).hi)


def exp(a):
    a = I.get(a)
    lo, hi = np.broadcast_arrays(a.lo, a.hi)
    left = np.fromiter((exp_point(float(x))[0] for x in lo.flat), dtype=float, count=lo.size).reshape(lo.shape)
    right = np.fromiter((exp_point(float(x))[1] for x in hi.flat), dtype=float, count=hi.size).reshape(hi.shape)
    return I(left, right)


def log_unit(m):
    m = Q(m)
    if not 1 <= m <= 2:
        raise ValueError('logarithm mantissa outside [1,2]')
    z = (m-1)/(m+1)
    z2, term, total = z*z, z, Q(0)
    for j in range(48):
        total += term/(2*j+1)
        term *= z2
    rem = 2*abs(z)**97/(97*(1-z*z))
    return 2*total-rem, 2*total+rem


LOG2Q = log_unit(Q(2))


@lru_cache(maxsize=4096)
def log_point(x):
    if not math.isfinite(x) or not x > 0:
        raise ValueError('positive finite logarithm input required')
    if x == 1:
        return 0., 0.
    mant, expo = math.frexp(x)
    lo, hi = log_unit(Q.from_float(2*mant))
    e = expo-1
    lo += e*LOG2Q[0 if e >= 0 else 1]
    hi += e*LOG2Q[1 if e >= 0 else 0]
    return float(qbounds(lo).lo), float(qbounds(hi).hi)


def log(a):
    a = I.get(a)
    if a.lo.shape or a.hi.shape:
        raise ValueError('This logarithm wrapper requires scalar input')
    return I(log_point(float(a.lo))[0], log_point(float(a.hi))[1])


LOG2 = I(float(qbounds(LOG2Q[0]).lo), float(qbounds(LOG2Q[1]).hi))


if __name__ == '__main__':
    import json
    rows = []
    for x in [.006, .02, .4, 1.426600691200502, 64.]:
        z = log(I(x)); rows.append({'function': 'log', 'argument': x, 'width': float(z.hi-z.lo)})
    for x in [-40., -5., .1]:
        z = exp(I(x)); rows.append({'function': 'exp', 'argument': x, 'width': float(z.hi-z.lo)})
    print(json.dumps({'scope': 'enclosure width diagnostics, not a new function-value assertion', 'rows': rows}))
