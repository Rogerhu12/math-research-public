#!/usr/bin/env python3
"""Exact small resultants for the reduced inside-mean residual restrictions."""
import json
from fractions import Fraction as Q

def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a

def det(a):
    a = [[Q(x) for x in row] for row in a]
    n = len(a)
    ans = Q(1)
    for j in range(n):
        k = next((k for k in range(j, n) if a[k][j]), None)
        if k is None:
            return Q(0)
        if k != j:
            a[j], a[k] = a[k], a[j]
            ans = -ans
        c = a[j][j]
        ans *= c
        for k in range(j+1, n):
            if a[k][j]:
                r = a[k][j] / c
                for l in range(j, n):
                    a[k][l] -= r*a[j][l]
    return ans

def resultant(a, b):
    a, b = trim(a), trim(b)
    m, n = len(a)-1, len(b)-1
    ad, bd = list(reversed(a)), list(reversed(b))
    mat = []
    for j in range(n):
        mat.append([0]*j + ad + [0]*(n-1-j))
    for j in range(m):
        mat.append([0]*j + bd + [0]*(m-1-j))
    value = det(mat)
    assert value.denominator == 1
    return value.numerator

K = [
    [0,0,0,0,5,-1], [0,0,0,-32,5,-1],
    [0,0,54,-4,5,0], [0,-32,-4,-8,0,0],
    [5,5,5,0,0,0], [-1,-1,0,0,0,0],
]
def dot(a, b):
    return sum(a[i]*K[i][j]*b[j] for i in range(6) for j in range(6))

def deriv_vector(s, order):
    if s == "infinity":
        a = [0]*6
        c = 1
        for j in range(1, order+1):
            c *= j
        a[5-order] = c
        return a
    a = []
    for j in range(6):
        c = 1
        for k in range(order):
            c *= j-k
        a.append(c * s**(j-order) if j >= order else 0)
    return a

def polar(a):
    return [sum(a[i]*K[i][j] for i in range(6)) for j in range(6)]

jets = {}
for s, expected in [(0, [0,0,216]), (2,[0,-32,-168]),
                    (-6,[0,288,-936]), ("infinity",[0,0,-32])]:
    a,b = deriv_vector(s,1), deriv_vector(s,2)
    actual = [dot(a,a),dot(a,b),dot(b,b)]
    assert actual == expected
    jets[str(s)] = actual

# Pairing the only possible isotropic v''-c v' with the other support point:
# 8 v''-21 v' at 2, and 8 v''+13 v' at -6.
linear_conditions = {
    2: [-21, [-1040,3952,-4488,2192,-445,21]],
    -6: [13, [-88560,-124272,-50904,-8784,-635,-13]],
}
for s, (coef, expected) in linear_conditions.items():
    vec = [8*b+coef*a for a,b in
           zip(deriv_vector(s,1),deriv_vector(s,2))]
    assert polar(vec) == expected, (s,polar(vec),expected)

cases = [
    ([6,-17,3], [520,-1716,1386,-403,21], -50331648),
    ([66,65,5], [14760,18252,5442,557,13], -31557943296),
    ([-12,40,-23,3], [-8,22,-15,1], -124928),
    ([-396,-456,-95,-5], [168,166,33,1], -488208384),
]
values = []
for a,b,expected in cases:
    got = resultant(a,b)
    assert got == expected, (a,b,got,expected)
    values.append(got)

print(json.dumps({
    "status":"PASS",
    "jet_pairings_g_ab_bb":jets,
    "four_resultants":values,
    "original_K_pairing_conditions":True,
    "all_arithmetic":"integer and rational, no numerical approximation"
}, indent=2))

