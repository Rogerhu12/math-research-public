#!/usr/bin/env python3
"""Exact rational tail bounds for the q=q_ref, pure-j=1 inlet model.

No saved candidate is loaded or changed. Bounds apply to exact arithmetic
continuous Fourier or exact uniform-grid projection, not binary trig tables.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    if args.out.exists(): raise FileExistsError(args.out)
    q=Q.from_float(.1);w=8*q;b=w/6;rho=1-w
    assert 0<b<Q(1,7) and rho>Q(19,100)
    rows=[]
    for M in (8,12,14,15,22):
        N=max(2048,128*M);period=N//math.gcd(N,3);cutoff=period-M
        # |e_j| <= exp(b^2)b^j/j!; exp(b^2) <= 1/(1-b^2).
        derivative=6*b**(M+1)/(math.factorial(M)*(1-b*b)*(1-b/Q(M+1)))
        # Exact finite-grid aliases only use |j| >= period-M. Coarser b<1/7
        # avoids printing or storing thousands of digits from the FFT aliases.
        alias=Q(343,144)*(1+3*M)*Q(1,7)**cutoff
        assert alias<Q(1,10**100)
        total=derivative+Q(1,10**100)
        gamma=2*total/rho+(total/rho)**2
        scale=10**60
        count=(gamma.numerator*scale+gamma.denominator-1)//gamma.denominator
        rows.append(dict(M=M,N=N,local_alias_period=period,
                         first_possible_alias_index=cutoff,
                         derivative_tail_upper_exact=str(derivative),
                         derivative_tail_upper_display=float(derivative),
                         alias_strictly_below_1e_minus100=True,
                         metric_upper_display=float(gamma),
                         safe_metric_upper_exact=str(Q(count,scale)),
                         below_1e_minus24=gamma<Q(1,10**24),
                         below_original_2e_minus9=gamma<Q(1,500000000)))
    me=Path(__file__)
    report=dict(scope=__doc__,q_reference_exact=str(q),w_exact=str(w),b_exact=str(b),
                rho_min_exact=str(rho),rows=rows,
                script=dict(path=str(me.resolve()),sha256=hashlib.sha256(me.read_bytes()).hexdigest()),
                candidate_loaded=False,BVP_calls=0,tail_calls=0)
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(out=str(args.out.resolve()),bytes=args.out.stat().st_size,
                         M15_upper_display=rows[3]['metric_upper_display'],
                         M14_upper_display=rows[2]['metric_upper_display'],
                         M22_upper_display=rows[4]['metric_upper_display'],
                         all_alias_bounds_below_1e_minus100=True)))


if __name__=='__main__': main()
