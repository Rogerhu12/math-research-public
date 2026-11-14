#!/usr/bin/env python3
"""Exact C1 Fourier-tail bound for the round background of a support chart.

This studies a frozen reference only; it creates no curve or nonlinear solve.
All polynomial arithmetic and the Taylor remainder are rational.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import time

HERE=Path(__file__).resolve().parent


def identity(p):
    p=Path(p).resolve();raw=p.read_bytes()
    return dict(path=str(p),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reference',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--order',type=int,default=16)
    args=parser.parse_args()
    if args.out.exists():raise FileExistsError(args.out)
    start=time.monotonic();ref=json.loads(args.reference.read_text())
    M,m,L=ref['M'],ref['m'],args.order
    cs=list(map(Q,ref['reference_coefficients_exact']))
    spec=importlib.util.spec_from_file_location('reference_round_laurent',HERE/'78718-geometry-inlet-angular-bound-v1.py')
    poly=importlib.util.module_from_spec(spec);spec.loader.exec_module(poly)
    phase={}
    for j,c in enumerate(cs,1):
        a=Q(1-(m*j)**2,m*j)*c
        if a:phase[j]=a/2;phase[-j]=-a/2
    A=poly.norm(phase);B=sum((abs(j*v) for j,v in phase.items()),Q(0))
    assert A<Q(L+1)
    power={0:Q(1)};value=dict(power)
    for n in range(1,L+1):
        power=poly.scale(poly.mul(power,phase),Q(1,n))
        value=poly.add(value,power)
    tail=sum((abs((1+m*j)*v) for j,v in value.items() if abs(j)>M),Q(0))
    e0=A**(L+1)/(math.factorial(L+1)*(1-A/Q(L+2)))
    e1=B*A**L/(math.factorial(L)*(1-A/Q(L+1)))
    N=max(2048,128*M);period=N//math.gcd(N,m)
    assert period-M>L*M
    alias=(1+m*M)*e0
    derivative=tail+e0+m*e1+alias
    rho=Q(ref['reference_rho_triangle_lower']['exact'])
    metric=2*derivative/rho+(derivative/rho)**2
    scale=10**30
    count=(metric.numerator*scale+metric.denominator-1)//metric.denominator
    output=dict(scope=__doc__,reference=identity(args.reference),script=identity(__file__),
                M=M,m=m,N=N,exponential_order=L,phase_l1_exact=str(A),phase_derivative_l1_exact=str(B),
                polynomial_derivative_tail_display=float(tail),
                C1_remainder_display=float(e0+m*e1),alias_derivative_bound_display=float(alias),
                full_derivative_tail_upper_display=float(derivative),
                inlet_G_upper_display=float(metric),safe_G_upper_exact=str(Q(count,scale)),
                below_2e_minus9=metric<Q(1,500000000),
                scope_binary_trig_and_rounding_excluded=True,BVP_calls=0,tail_calls=0,
                seconds=time.monotonic()-start)
    args.out.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(dict(out=str(args.out.resolve()),bytes=args.out.stat().st_size,
                         derivative_tail_upper=float(derivative),metric_upper=float(metric),
                         below_2e_minus9=output['below_2e_minus9'],seconds=output['seconds'])))


if __name__=='__main__':main()
