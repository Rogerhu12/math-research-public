#!/usr/bin/env python3
"""Fejer-smoothed bounded-curvature cores with rational interval certificates.

Each finite N is an exact analytic planar curve, not a closed flexible surface.
True coefficients are defined by r,R,N,pi,sin; floats are initial guesses only.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import json
from pathlib import Path

Q = 10 ** 45


def rounded(lo: F, hi: F) -> tuple[F, F]:
    assert lo <= hi
    return F((lo.numerator*Q)//lo.denominator, Q), F(-((-hi.numerator*Q)//hi.denominator), Q)


def add(x, y):
    return rounded(x[0]+y[0], x[1]+y[1])


def scale(x, c: F):
    return rounded(c*x[0], c*x[1]) if c >= 0 else rounded(c*x[1], c*x[0])


def mul(x, y):
    p = [a*b for a in x for b in y]
    return rounded(min(p), max(p))


def reciprocal(x):
    assert x[0] > 0
    return rounded(1/x[1], 1/x[0])


def pi_interval():
    def arctan_reciprocal(q):
        x = F(1, q)
        s = sum((-1)**k*x**(2*k+1)/(2*k+1) for k in range(40))
        next_term = x**81/81
        return s, s+next_term
    a, b = arctan_reciprocal(5), arctan_reciprocal(239)
    # 40 terms end with a negative term; the next term is positive.
    return add(scale(a,F(16)), scale(b,F(-4)))


def sin_pi(q: F, pi):
    q = q % 2
    sign = F(1)
    if q > 1:
        q -= 1
        sign = -sign
    if q > F(1,2):
        q = 1-q
    if q == 0:
        return F(0),F(0)
    x = scale(pi,q)
    x2 = mul(x,x)
    term = x
    total = (F(0),F(0))
    for k in range(32):
        total = add(total,scale(term,F((-1)**k)))
        term = scale(mul(term,x2),F(1,(2*k+2)*(2*k+3)))
    # Alternating-series error is <= the next positive term, with either sign.
    total = rounded(total[0]-term[1],total[1]+term[1])
    return scale(total,sign)


def describe(x):
    return {"lower_exact":str(x[0]),"upper_exact":str(x[1]),
            "lower_approx":float(x[0]),"upper_approx":float(x[1])}


def generate(r: F, R: F, n: int, diameter: F):
    if not (0 < r < 1 < R and n >= 1 and diameter > 0):
        raise ValueError("Need 0 < r < 1 < R, N >= 1 and diameter > 0")
    pi = pi_interval()
    inv_pi = reciprocal(pi)
    q = (R-1)/(2*(R-r))
    cs=[]
    for j in range(1,n+1):
        coeff = scale(mul(sin_pi(2*j*q,pi), inv_pi),
                      -2*(R-r)*F(n+1-j,n+1)/j/(1-4*j*j))
        cs.append(coeff)
    A=(F(1),F(1));B=A;gap=(F(0),F(0));radius_upper=F(1)
    for j,c in enumerate(cs,1):
        A=add(A,c);B=add(B,scale(c,F((-1)**j)))
        if j%2:gap=add(gap,scale(c,F(2)))
        radius_upper+=max(abs(c[0]),abs(c[1]))
    opt_gap=scale(add(add(sin_pi(q,pi),sin_pi(F(1,2)-q,pi)),(F(-1),F(-1))),R-r)
    return {
        "scope":"Proved exact analytic core; full closed isometric transition unsolved.",
        "r_exact":str(r),"R_exact":str(R),"N":n,
        "phi0_over_pi_exact":str(q),"pi_interval":describe(pi),
        "coefficient_definition":"-2*(R-r)/pi*sin(2*j*phi0)/j*(1-j/(N+1))/(1-4*j*j)",
        "coefficients_intervals":[describe(c)for c in cs],
        "coefficients_float_initial_guess":[float((c[0]+c[1])/2)for c in cs],
        "rho_min_lower_exact":str(r),"rho_max_upper_exact":str(R),
        "A_axis":describe(A),"B_axis":describe(B),"axis_phase_gap":describe(gap),
        "core_radius_upper_exact":str(radius_upper),"core_radius_upper_approx":float(radius_upper),
        "optimal_axis_gap_supremum":describe(opt_gap),
        "assumed_whole_D_upper_exact":str(diameter),
        "conditional_gap_ratio":describe(scale(gap,1/diameter)),
        "conditional_gap_gate":gap[0]>=diameter/5,
        "core_curvature_gate":r>=3*diameter/100,
        "unpaid":"Whole diameter, whole witness exclusion, nonlinear closed transition, full reach, fixed-g convergence, delta_E.",
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--r",type=F,default=F(3,20))
    parser.add_argument("--R",type=F,default=F(3))
    parser.add_argument("--N",type=int,default=16)
    parser.add_argument("--diameter",type=F,default=F(19,5))
    parser.add_argument("--out",type=Path)
    args=parser.parse_args()
    result=generate(args.r,args.R,args.N,args.diameter)
    encoded=json.dumps(result,indent=2)+'\n'
    if args.out:
        args.out.parent.mkdir(parents=True,exist_ok=True)
        args.out.write_text(encoded)
    else:print(encoded)


if __name__=='__main__':main()
