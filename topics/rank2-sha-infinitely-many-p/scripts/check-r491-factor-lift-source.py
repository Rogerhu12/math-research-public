#!/usr/bin/env python3
"""Fixed exact factor-lift certificate for R491; no theta-contact claim."""
from fractions import Fraction
from math import comb
import json

p = 101
D = 12
def trim(a):
    a = list(a)
    while a and not a[-1]:
        a.pop()
    return a
def mul(a, b):
    c = [0] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return trim(c)
def power(a, n):
    c = [1]
    for _ in range(n):
        c = mul(c, a)
    return c
def divide(a, b, modulus=None):
    if modulus:
        r = trim([x % modulus for x in a])
        b = trim([x % modulus for x in b])
        q = [0] * max(0, len(r)-len(b)+1)
        while r and len(r) >= len(b):
            shift = len(r)-len(b)
            c = r[-1] * pow(b[-1], -1, modulus) % modulus
            q[shift] = c
            for j, y in enumerate(b):
                r[shift+j] = (r[shift+j]-c*y) % modulus
            r = trim(r)
    else:
        r = trim([Fraction(x) for x in a])
        b = trim([Fraction(x) for x in b])
        q = [Fraction(0)] * max(0, len(r)-len(b)+1)
        while r and len(r) >= len(b):
            shift = len(r)-len(b)
            c = r[-1] / b[-1]
            q[shift] = c
            for j, y in enumerate(b):
                r[shift+j] -= c*y
            r = trim(r)
    return trim(q), r
def order(a, factor, modulus=None):
    count = 0
    while a:
        q, r = divide(a, factor, modulus)
        if r:
            return count
        a = q
        count += 1
    raise AssertionError("the coefficient must be nonzero")
def abc(n):
    return (n+1)//4, (n+1)//3, n//2
def ceildiv(a, b):
    return -((-a)//b)
def e(n):
    m=n+1
    return 3*ceildiv(3*m,4)+2*ceildiv(m,2)+ceildiv(2*m,3)-2

t = [0, 1]
h7 = [7, 4, 16]
tm1 = [-1, 1]
d = [1, 8]
good_f1 = [-x for x in power([1, -1], 8)]
naive_f1 = [x % p for x in good_f1]
assert sum(good_f1) == 0
assert sum(naive_f1) == 505
assert order(good_f1, tm1) == 8
assert order(naive_f1, tm1) == 0
assert order(naive_f1, tm1, p) == 8

# d^6 P = t^3 h7^3 (t-1)^3 d^2 Y^9 (1+f1 Y)^3.
base = mul(mul(power(t,3),power(h7,3)),mul(power(tm1,3),power(d,2)))
def source_coeffs(f1):
    return {9+i: [comb(3,i)*x for x in mul(base,power(f1,i))]
            for i in range(4)}
good = source_coeffs(good_f1)
naive = source_coeffs(naive_f1)
assert all([x%p for x in good[n]] == [x%p for x in naive[n]] for n in good)

def membership(coefficients, modulus=None):
    details = []
    cD = abc(D)[2]
    for n, coefficient in coefficients.items():
        an,bn,cn = abc(n)
        divisor = mul(mul(power(t,an),power(h7,an)),
                      mul(power(tm1,bn),power(d,cD-cn)))
        quotient, remainder = divide(coefficient,divisor,modulus)
        ok = not remainder and len(quotient)-1 <= e(n)
        details.append({"charge":n,"membership":ok,
                        "quotient_degree":len(quotient)-1 if not remainder else None,
                        "original_degree_cap":e(n)})
    return details
good_membership = membership(good)
naive_membership = membership(naive)
naive_reduction_membership = membership(naive,p)
assert all(x["membership"] for x in good_membership)
assert all(x["membership"] for x in naive_reduction_membership)
assert [x["charge"] for x in naive_membership if not x["membership"]] == [11,12]
assert [x["quotient_degree"] for x in good_membership] == [3,12,16,25]

def gauss(coefficients, modulus=None):
    result = {}
    for name, factor, base_weight, y_weight in [
            ("zero",t,4,-1),("h7",h7,4,-1),
            ("one",tm1,3,-1),("d_root",d,2,1)]:
        result[name] = min(base_weight*order(c,factor,modulus)+y_weight*n
                           for n,c in coefficients.items())
    result["infinity"] = min(-2*(len(trim([x%modulus for x in c] if modulus else c))-1)+9*n
                             for n,c in coefficients.items())
    return result
good_gauss = gauss(good)
assert good_gauss == gauss(good,p)
assert good_gauss == {"zero":0,"h7":0,"one":0,"d_root":13,"infinity":32}
assert gauss(naive)["one"] == -3
assert gauss(naive,p)["one"] == 0
# h7 is irreducible for this inert sample, so its valuation covers both roots.
assert pow((-3)%p,(p-1)//2,p) == p-1

print(json.dumps({
    "result":"passed","prime":p,"D":D,
    "factor":"F=1-Y(1-t)^8",
    "is_claimed_original_theta_contact":False,
    "same_source_degree_caps":good_membership,
    "naive_lift_fails_at_charges":[11,12],
    "naive_lift_at_t1":sum(naive_f1),
    "restored_factor_order_at_t1":8,
    "exact_good_Gauss_values":good_gauss,
    "required_Gauss_lower_bounds":{
        "zero":-2,"h7":-2,"one":-1,"d_root":12,"infinity":-20},
    "original_J_forcing_removed":False,
    "original_carry_removed":False,
},indent=2))

