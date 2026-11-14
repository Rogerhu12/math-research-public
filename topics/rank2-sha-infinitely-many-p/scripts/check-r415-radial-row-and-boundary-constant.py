#!/usr/bin/env python3
"""Exact rational certificate for R415, without a prime search."""
from fractions import Fraction as F
from math import comb
import json

N = 13
X = [F(1), F(-1,7)]
for n in range(2,N+1):
    X.append(sum(X[i]*X[n-i] for i in range(1,n))/((6*n+1)*(n-1)))
    assert (-1)**n*X[n] > 0

trace = [2,-286]
for n in range(2,N+1):
    trace.append(-286*trace[-1]-117649*trace[-2])
log_power = [F(0)]
for n in range(1,N+1):
    fn = -X[n]/(6*n*(6*n-1))
    mn = (-27)**n+(-1728)**n+(-19683)**n+4096**n+trace[n]
    assert (-1)**n*mn > 0
    assert fn*mn < 0
    log_power.append(F(-77,6)*fn*mn)


def exp_series(L):
    C = [F(1)]
    for n in range(1,len(L)):
        C.append(sum(F(i)*L[i]*C[n-i] for i in range(1,n+1))/n)
    return C


C13 = exp_series(log_power)[13]
assert C13 == F(
    15589695079897392452264643266319015779194056268822379768788948458915829290376583989633812775432093506892382,
    124529319870798155459262408573660930111728788953986119654278586212158203125)
assert C13 > 0

# Exact fixed h-series for the two specified boundary vectors.
h = [F(comb(2*n,n),4**n*(6*n+1)) for n in range(N+1)]
hinv = [F(1)]
for n in range(1,N+1):
    hinv.append(-sum(h[i]*hinv[n-i] for i in range(1,n+1)))

poch_ratio = F(1)
Ltheta = [F(0)]
for n in range(1,N+1):
    poch_ratio *= F(6*n-4,6*n-1)
    Ltheta.append(F(17,3*n)*poch_ratio)
theta17 = exp_series(Ltheta)
G = [theta17[0]]+[theta17[n]+8*theta17[n-1] for n in range(1,N+1)]
C_Rt6 = sum(F(6+i)*G[i]*hinv[N-i] for i in range(N+1))


def mod(q,p):
    return q.numerator*pow(q.denominator,-1,p) % p


assert mod(hinv[13],101) == 77
assert 2*pow(17,-1,101)*mod(hinv[13],101) % 101 == 15
assert mod(C_Rt6,113) == 32
assert -89*pow(2*19,-1,113)*mod(C_Rt6,113) % 113 == 44

print(json.dumps({
    "status":"passed", "C13_numerator":str(C13.numerator),
    "C13_denominator":str(C13.denominator),
    "fixed_boundary_checks":[
        {"p":101,"source":"t^4","h_inverse_coefficient":77,"beta1":15},
        {"p":113,"source":"R*t^6","G_h_coefficient":32,"beta1":44}
    ]},indent=2))
