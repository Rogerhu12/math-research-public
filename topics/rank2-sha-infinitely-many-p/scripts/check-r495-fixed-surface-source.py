#!/usr/bin/env python3
"""Exact fixed-surface and actual-source identities for R495.

No formal-theta contact is asserted or computed.  This script checks the
nineteen actual multiplicities and all original Gauss source inequalities for
one irreducible odd-b family; the general geometry is proved in the result.
"""
from fractions import Fraction
from math import gcd
import json

def ceildiv(a, d):
    return -((-a)//d)
def abc(n):
    return (n+1)//4, (n+1)//3, n//2
def source_e(n):
    m=n+1
    return 3*ceildiv(3*m,4)+2*ceildiv(m,2)+ceildiv(2*m,3)-2
def increments(values):
    return [values[j]-values[j-1] for j in range(1,len(values))]

p = 239
b = 13
D = 3*b
A,B,c = abc(b)
E = source_e(b)-4
cD = abc(D)[2]
u = 2*c
degree_high = 3*A+B+E
assert degree_high == 5*b-(b%2)
assert max(c,degree_high-4*b) == u
assert cD-3*c == 1
assert gcd(b,c) == 1
assert (9*D)//2+4 < p
assert E >= 0 and A >= 1

# F=d^c(Y-1)+(t h7)^A(t-1)^B(1+t)^E Y^b.
# All other displayed factors are units at each relevant fixed angular root.
v4 = [0]+[min(j*A,b-1) for j in range(1,5)]
v3 = [0]+[min(j*B,b-1) for j in range(1,4)]
v2 = [0]+[min(j*c,b) for j in range(1,3)]
mu4,mu3,mu2 = map(increments,(v4,v3,v2))
multiplicities = mu4*3+mu3+mu2*2
assert len(multiplicities) == 19 and min(multiplicities) >= 0
kappa = 4*b*b+2*b*u-sum(m*m for m in multiplicities)
chi = 2*u+6*b-sum(multiplicities)
delta3={0:Fraction(2,3),1:Fraction(0),2:Fraction(8,3)}[b%3]
formula = (Fraction(47,12)*b*b+Fraction(13,6)*b-Fraction(25,12)
           -9*int(b%4==3)-delta3)
assert kappa == formula == 688
assert chi == 2*b+4 == 30
genus = 1+(kappa-chi)//2
assert 2*genus-2 == kappa-chi
h0C = 1+(kappa+chi)//2
h0_3C = 1+(9*kappa+3*chi)//2
ndim = sum(source_e(n)+1 for n in range(D+1))
assert ndim == 3250
assert h0_3C <= ndim

# The numerator of the original source after clearing d^C_D is
# t(t-1)h7 * d^(C_D-3c) * F^3, of Y degree 3b.
F_gauss = {
    "zero": min(-1,4*A-b),
    "h7_root_1": min(-1,4*A-b),
    "h7_root_2": min(-1,4*A-b),
    "one": min(-1,3*B-b),
    "d_root": min(2*c,b),
    "infinity": min(-2*c,-2*degree_high+9*b),
}
multiplier = {
    "zero":4,"h7_root_1":4,"h7_root_2":4,
    "one":3,"d_root":2*(cD-3*c),
    "infinity":-8-2*(cD-3*c),
}
actual={key:multiplier[key]+3*F_gauss[key] for key in F_gauss}
required={
    "zero":-2,"h7_root_1":-2,"h7_root_2":-2,
    "one":-1,"d_root":2*cD,"infinity":-2*cD-8,
}
assert all(actual[key] >= required[key] for key in actual)
assert actual["d_root"] == required["d_root"]
assert actual["infinity"] == required["infinity"]
assert -2*b+sum(F_gauss.values()) == -chi

print(json.dumps({
    "result":"passed","prime":p,"b":b,"D":D,
    "is_claimed_original_theta_contact":False,
    "coefficient_degree_caps":{"A":A,"B":B,"c":c,"E":E,"u":u},
    "Newton_segment":{"endpoints":[[0,c],[b,0]],"coprime":gcd(b,c)==1},
    "nineteen_multiplicities":multiplicities,
    "C_squared":kappa,"minus_K_dot_C":chi,"arithmetic_genus":genus,
    "h0_C":h0C,"h0_3C":h0_3C,"original_source_dimension":ndim,
    "joint_length_bounds_at_r1":{"value":2*kappa+chi,"normal":kappa+chi},
    "actual_source_Gauss_values":actual,
    "required_source_Gauss_lower_bounds":required,
    "entire_J_lift_claimed":False,
    "original_carry_removed":False,
},indent=2))

