#!/usr/bin/env python3
"""Exact ordinary-coefficient plane-jet certificate, p=103 and degree=6.

The graph is Y(w)=4 integral_0^z A(t)dt/t / theta((4-i)z), w=z^4.
It is the fixed actual Euler-primitive graph, not its p-dependent central
projection.  Integer Hurwitz coefficients are converted to ordinary
coefficients before every lattice computation.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[1]
flow = runpy.run_path(str(ROOT / 'scripts/check-theta-hurwitz-integers.py'))
p, degree, stop = 103, 6, 27
zero, one = (F(0), F(0)), (F(1), F(0))

def add(x, y):
    return (x[0]+y[0], x[1]+y[1])

def neg(x):
    return (-x[0], -x[1])

def mul(x, y):
    return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])

def red(x):
    def scalar(a):
        if a.denominator % p == 0:
            raise ValueError('nonintegral coefficient')
        return a.numerator * pow(a.denominator, -1, p) % p
    return (scalar(x[0]), scalar(x[1]))

h = flow['coefficients'](4*stop, 1)
theta = flow['universal_sigma_theta'](4*stop)[1]
f, power = [], (1, 0)
for n in range(stop+1):
    f.append((F(theta[4*n]*power[0], factorial(4*n)), F(theta[4*n]*power[1], factorial(4*n))))
    power = mul(power, (161, -240))
y = [zero]
for n in range(1, stop+1):
    value = (F(h[4*n], n*factorial(4*n)), F(0))
    for j in range(1, n+1):
        value = add(value, neg(mul(f[j], y[n-j])))
    y.append(value)
yp = [red(a) for a in y[:stop]]
bad = red((p*y[stop][0], p*y[stop][1]))

Z, O = (0, 0), (1, 0)

def fa(a, b):
    return ((a[0]+b[0]) % p, (a[1]+b[1]) % p)

def fn(a):
    return (-a[0] % p, -a[1] % p)

def fm(a, b):
    return ((a[0]*b[0]-a[1]*b[1]) % p, (a[0]*b[1]+a[1]*b[0]) % p)

def fi(a):
    den = pow((a[0]*a[0]+a[1]*a[1]) % p, -1, p)
    return (a[0]*den % p, -a[1]*den % p)

powers = [[O]+[Z]*(stop-1)]
for j in range(1, degree+1):
    previous = powers[-1]
    cur = [Z]*stop
    for n in range(stop):
        for m in range(n+1):
            cur[n] = fa(cur[n], fm(previous[m], yp[n-m]))
    powers.append(cur)
cols = [(d-j, j) for d in range(degree+1) for j in range(d+1)]
matrix = [[powers[j][n-i] if n>=i else Z for i,j in cols] for n in range(stop)]

def rref(input_rows):
    a = [row[:] for row in input_rows]
    nr, nc = len(a), len(a[0])
    pivots, determinant = [], O
    for col in range(nc):
        row = len(pivots)
        found = next((k for k in range(row, nr) if a[k][col] != Z), None)
        if found is None:
            continue
        if found != row:
            a[found], a[row] = a[row], a[found]
            determinant = fn(determinant)
        v = a[row][col]
        determinant = fm(determinant, v)
        inv = fi(v)
        a[row] = [fm(inv, t) for t in a[row]]
        for k in range(nr):
            if k == row or a[k][col] == Z:
                continue
            scale = a[k][col]
            a[k] = [fa(t, fn(fm(scale, u))) for t,u in zip(a[k], a[row])]
        pivots.append(col)
        if len(pivots) == nr:
            break
    return a, pivots, determinant

rr, pivots, det = rref(matrix)
free = [j for j in range(len(cols)) if j not in pivots]
kernels=[]
for j in free:
    v=[Z]*len(cols)
    v[j]=O
    for i,c in enumerate(pivots):
        v[c]=fn(rr[i][j])
    kernels.append(v)
scaled_last = [bad if (i,j)==(0,1) else Z for i,j in cols]
_, final_pivots, final_det = rref(matrix+[scaled_last])
assert y[1] == one
assert y[2] == (F(-1513, 120), F(20))
assert bad == (29, 0)
assert pivots == list(range(27))
assert det == (1, 34)
assert free == [27]
assert kernels[0][cols.index((0,1))] == (45, 60)
assert fm(bad, kernels[0][cols.index((0,1))]) == (69, 92)
assert len(final_pivots) == 28
assert final_det == (31, 69)
print(json.dumps({
    'p': p, 'degree': degree, 'rows_before_bad': stop,
    'p_times_Y_bad': bad,
    'prefix_rank': len(pivots), 'prefix_pivot_columns': pivots,
    'prefix_pivot_minor': det, 'free_columns': free,
    'monomials': cols, 'kernel_vectors': kernels,
    'kernel_Y_coefficients': [v[cols.index((0,1))] for v in kernels],
    'scaled_last_kernel': [fm(bad, v[cols.index((0,1))]) for v in kernels],
    'full_scaled_rank': len(final_pivots), 'full_scaled_determinant': final_det,
    'ordinary_smith_exponents': [-1] + [0]*27,
}, separators=(',', ':')))
