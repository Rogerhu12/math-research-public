#!/usr/bin/env python3
"""One exact actual-source certificate for R489, with no prime search.

The curve in this certificate is algebraic and is NOT asserted to have the
original theta contact.  The theorem for arbitrary branches is proved in R489.
"""
import json

p = 101
D = 6
b = 2
u = 1
ceildiv = lambda a, d: -((-a) // d)
def abc(n):
    return (n + 1) // 4, (n + 1) // 3, n // 2
def e(n):
    m = n + 1
    return 3 * ceildiv(3*m, 4) + 2 * ceildiv(m, 2) + ceildiv(2*m, 3) - 2
def f(n):
    an, bn, cn = abc(n)
    return 3*an + bn - cn + e(n)
A, B, _ = abc(D)
n0 = D - 2*b + 1
K = 5*n0 + 4 - n0 % 2 - 3*A - B
V = A + b*K + u + 4*b*b + 2*b - 1
N = A + b*K - (2*b-1)*u + 2*b - 1
assert (A, n0, K, V, N) == (1, 3, 13, 47, 27)
assert f(D) < p and V < p
length = V

def mul(x, y):
    z = [0] * length
    for i, a in enumerate(x[:length]):
        if a:
            for j, c in enumerate(y[:length-i]):
                if c:
                    z[i+j] = (z[i+j] + a*c) % p
    return z

def power(poly, exponent):
    result = [1] + [0]*(length-1)
    factor = poly + [0]*(length-len(poly))
    for _ in range(exponent):
        result = mul(result, factor)
    return result

def binom_series(exponent, scalar):
    exponent %= p
    out = [1]
    for j in range(1, length):
        out.append(out[-1] * (exponent-j+1) * scalar * pow(j, -1, p) % p)
    return out

def shifted(base, order):
    return [0]*min(order, length) + base[:max(0, length-order)]

def pair(base, order, charge):
    value = shifted(base, order)
    return value + [charge*x % p for x in value[:N]]

# F=Y^2-1-t; psi^n=(1+t)^(n/2).  Every high-block column is
# H_D * Y^n * t^j and is checked against its own original q_n degree cap.
columns = []
membership = []
cn0 = abc(n0)[2]
for i in range(2*b):
    n = n0+i
    an, bn, cn = abc(n)
    quotient_degree = 3*(A-an) + (B-bn) + cn-cn0
    polynomial_cap = K+4*i
    assert min(A-an, B-bn, cn-cn0) >= 0
    assert polynomial_cap + quotient_degree <= e(n)
    membership.append({
        "charge": n,
        "polynomial_cap": polynomial_cap,
        "H_over_q_degree": quotient_degree,
        "original_allowed_degree": e(n),
    })
    base = binom_series(n * pow(2, -1, p), 1)
    base = mul(base, power([7, 4, 16], A))
    base = mul(base, power([-1, 1], B))
    base = mul(base, binom_series(-cn0, 8))
    for j in range(polynomial_cap+1):
        columns.append(pair(base, A+j, n))

high_count = len(columns)
assert high_count == 80
for r in range(A):
    for n in (r+1, r+2):
        an, bn, cn = abc(n)
        assert 0 <= r-an <= e(n)
        base = binom_series(n * pow(2, -1, p), 1)
        base = mul(base, power([7, 4, 16], an))
        base = mul(base, power([-1, 1], bn))
        base = mul(base, binom_series(-cn, 8))
        columns.append(pair(base, r, n))

pivots = {}
for column in columns:
    vector = column[:]
    assert len(vector) == V+N
    for row, entry in enumerate(vector):
        if not entry:
            continue
        if row in pivots:
            scale = entry
            vector = [(x-scale*y) % p for x, y in zip(vector, pivots[row])]
        else:
            inverse = pow(entry, -1, p)
            pivots[row] = [x*inverse % p for x in vector]
            break
assert len(pivots) == V+N

print(json.dumps({
    "result": "passed",
    "prime": p,
    "D": D,
    "F": "Y^2-1-t",
    "branch": "psi(0)=1",
    "is_claimed_original_theta_branch": False,
    "n0": n0,
    "K": K,
    "actual_membership": membership,
    "value_length": V,
    "Euler_normal_length": N,
    "high_block_columns": high_count,
    "low_columns": len(columns)-high_count,
    "rank": len(pivots),
    "entire_J_lift_claimed": False,
    "original_carry_removed": False,
}, indent=2))

