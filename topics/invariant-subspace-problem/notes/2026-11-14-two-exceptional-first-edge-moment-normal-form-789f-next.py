"""Exact common-source moment normal form for R273, relative birth two.

The default check compares with the complete physical-layer inverse.
No adjacent positivity is inferred from a finite parameter check.
"""

from functools import lru_cache
from math import factorial
from pathlib import Path
import argparse
import importlib.util
import sympy as sp


def choose_polynomial(x, k):
    return sp.Rational(1, factorial(k))*sp.prod(sp.sympify(x)-r for r in range(k))


@lru_cache(None)
def moment_data(q, pool, z, j):
    weights = [choose_polynomial(q, i)*choose_polynomial(pool, j-i)*z**i
               for i in range(j+1)]
    mm = [sp.factor(sum(i**r*weights[i] for i in range(j+1)))
          for r in range(5)]
    ee = mm[0]
    delta2 = sp.factor(ee*mm[2]-mm[1]**2)
    delta3 = sp.factor(sp.Matrix(3, 3, lambda r, c: mm[r+c]).det())
    mean = sp.cancel(mm[1]/ee)
    second = sp.cancel(mm[2]/ee)
    if j == 0:
        return ee, mean, second, sp.S.Zero, None, sp.S.Zero
    chi = sp.cancel((ee*mm[3]-mm[1]*mm[2])/delta2)
    bnorm = sp.cancel(ee/delta2)
    precision = sp.cancel(delta3/delta2)
    return ee, mean, second, chi, bnorm, precision


def normal_gram(q, pool, z, w1, w2, n):
    """n=0,1,2, q,pool>=3; normalized by the common C_q."""
    dd = [moment_data(q, pool, z, n+k) for k in range(3)]
    aa = 1/dd[0][0]+(w1+w2)/dd[1][0]+w1*w2/dd[2][0]
    difference = dd[0][3]-2*dd[1][3]+dd[2][3]
    increment = dd[2][3]-dd[1][3]
    ff = [x[2]-x[3]*x[1] for x in dd]
    mixed = ff[0]-2*ff[1]+ff[2]
    lam = sp.cancel(w1*w2/(w1*w2*dd[0][5]
                          +(w1+w2)*dd[1][5]+dd[2][5]))
    matrix = sp.zeros(5)
    matrix[0, 0] = aa
    for y, z0 in ((0, 0), (1, 0), (0, 1), (1, 1)):
        datum = dd[y+z0]
        if datum[4] is not None:
            row = sp.Matrix([[-datum[1], y, z0, 0, 1]])
            matrix += w1**y*w2**z0*datum[4]*(row.T*row)
    row = sp.Matrix([[-mixed, -increment, -increment, 1, -difference]])
    matrix += lam*(row.T*row)
    if n == 0:
        answer = matrix[:4, :4]  # the actual hard constraint x=0
    else:
        answer = matrix[:4, :4]-matrix[:4, 4]*matrix[4, :4]/matrix[4, 4]
    return answer.applyfunc(sp.cancel)


def check_identity():
    original = Path(__file__).with_name('2026-11-14-two-exceptional-schur-789f.py')
    spec = importlib.util.spec_from_file_location('r273_complete', original)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    q, pool, a, u, v = 3, 4, sp.Rational(2), sp.Rational(3), sp.Rational(5)
    source = sp.diag(1, -1, -1, 1)
    scale = factorial(q)**2*a**(2*q)
    for n in range(3):
        complete = module.full_gram(q, pool, 2, n, a, u, v)
        wanted = source.T*complete*source/scale
        actual = normal_gram(q, pool, a*a, u*u, v*v, n)
        assert (actual-wanted).applyfunc(sp.cancel) == sp.zeros(4)
        print(f'PASS exact common-source identity: q={q}, L={pool}, n={n}', flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    options = parser.parse_args()
    if options.check:
        check_identity()
