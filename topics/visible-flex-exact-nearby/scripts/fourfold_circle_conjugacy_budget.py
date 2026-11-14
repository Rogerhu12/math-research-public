#!/usr/bin/env python3
"""Exact rational Wiener budgets for a defined finite Fourier conjugacy.

Rounded coefficients DEFINE H and q. Integer convolution and rational upper
bounds prove ||1-q H'||_s<1 when reported successful. FFT and sampling only
choose these polynomials; no reliability of those choices is assumed by the
subsequent rational identity. This proves no conjugacy equation for a ray map.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
from math import isqrt
import json
from pathlib import Path

import numpy as np


def upper_sqrt_integer(value):
    floor=isqrt(value)
    return floor if floor*floor==value else floor+1


def exp_upper(x, order=80):
    """Rational Taylor sum plus its geometric majorant, for x>=0."""
    if x<0 or x>=order+2:
        raise ValueError("invalid exponential majorant range")
    term=Fraction(1);total=term
    for j in range(1,order+1):
        term*=x/j
        total+=term
    next_term=term*x/(order+1)
    return total+next_term/(1-x/(order+2))


def integer_fourier(positive,bits):
    """Conjugate-symmetric complex integer coefficients, -m through m."""
    scale=1<<bits
    pos=[(int(round(float(z.real)*scale)),int(round(float(z.imag)*scale)))
         for z in positive]
    pos[0]=(pos[0][0],0)
    return [(a,-b) for a,b in pos[:0:-1]]+pos


def convolution(first,second):
    out=[[0,0] for _ in range(len(first)+len(second)-1)]
    for i,(ar,ai) in enumerate(first):
        for j,(br,bi) in enumerate(second):
            out[i+j][0]+=ar*br-ai*bi
            out[i+j][1]+=ar*bi+ai*br
    return [tuple(value) for value in out]


def norm_upper(coeff,bits,width,exp_cache):
    degree=(len(coeff)-1)//2
    denominator=1<<bits
    out=Fraction(0)
    for k,(real,imag) in zip(range(-degree,degree+1),coeff):
        magnitude=Fraction(upper_sqrt_integer(real*real+imag*imag),denominator)
        argument=width*abs(k)
        if argument not in exp_cache:
            exp_cache[argument]=exp_upper(argument)
        out+=magnitude*exp_cache[argument]
    return out


def dyadic_upper(value,bits=60):
    scale=1<<bits
    integer=(value.numerator*scale+value.denominator-1)//value.denominator
    return dict(numerator=str(integer),denominator_power_of_two=bits,
                floating_upper_display=float(np.nextafter(integer/scale,np.inf)))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--conjugacy",type=Path,required=True)
    parser.add_argument("--polynomials",type=Path,required=True)
    parser.add_argument("--out",type=Path,required=True)
    parser.add_argument("--bits",type=int,default=80)
    parser.add_argument("--inverse-degree",type=int,default=512)
    parser.add_argument("--width-denominators",type=int,nargs="+",default=[4096,2048,1024,512])
    args=parser.parse_args()
    with np.load(args.conjugacy,allow_pickle=False) as saved:
        values=saved["h_values"]
        metadata=json.loads(str(saved["metadata"]))
    degree=(len(values)-1)//2
    positive=np.fft.fft(values)[:degree+1]/len(values)
    positive[0]=0.
    h=integer_fourier(positive,args.bits)
    d=[(-k*b,k*a) for k,(a,b) in zip(range(-degree,degree+1),h)]
    d[degree]=(1<<args.bits,0)
    # This sampled inverse merely selects q; the exact convolution below pays it.
    count=max(8192,8*(args.inverse_degree+degree+1))
    x=np.arange(count)*2*np.pi/count
    k=np.arange(-degree,degree+1)
    dc=np.array([complex(a,b)/(1<<args.bits) for a,b in d])
    derivative=np.real(np.exp(1j*np.outer(x,k))@dc)
    qpositive=np.fft.fft(1/derivative)[:args.inverse_degree+1]/count
    q=integer_fourier(qpositive,args.bits)
    product=convolution(d,q)
    residual=[(-a,-b) for a,b in product]
    center=(len(residual)-1)//2
    residual[center]=(residual[center][0]+(1<<(2*args.bits)),residual[center][1])
    d_at_zero=sum(a for a,_ in d)
    assert sum(b for _,b in d)==0
    definitions=dict(
        kind="exact_dyadic_trigonometric_polynomials_H_and_q",
        coefficient_convention="h(x)=sum h_k exp(i k x); H=x+h; negative coefficients conjugate",
        denominator_power_of_two=args.bits,H_degree=degree,q_degree=args.inverse_degree,
        h_nonnegative_integer_coefficients=[[str(a),str(b)] for a,b in h[degree:]],
        q_nonnegative_integer_coefficients=[[str(a),str(b)] for a,b in q[args.inverse_degree:]],
        source_conjugacy_sha256=hashlib.sha256(args.conjugacy.read_bytes()).hexdigest(),
        source_metadata=metadata)
    args.polynomials.write_text(json.dumps(definitions,indent=2)+"\n")
    bounds=[];exp_cache={}
    for denominator in args.width_denominators:
        width=Fraction(1,denominator)
        hnorm=norm_upper(h,args.bits,width,exp_cache)
        dnorm=norm_upper(d,args.bits,width,exp_cache)
        qnorm=norm_upper(q,args.bits,width,exp_cache)
        rnorm=norm_upper(residual,2*args.bits,width,exp_cache)
        entry=dict(width_numerator=1,width_denominator=denominator,
                   h_Wiener_upper=dyadic_upper(hnorm),
                   Hprime_Wiener_upper=dyadic_upper(dnorm),
                   q_Wiener_upper=dyadic_upper(qnorm),
                   product_residual_Wiener_upper=dyadic_upper(rnorm),
                   exact_rational_Neumann_test_passed=bool(rnorm<1),
                   Hprime_at_zero_positive=bool(d_at_zero>0))
        if rnorm<1:
            entry["inverse_Hprime_Wiener_upper"]=dyadic_upper(qnorm/(1-rnorm))
            entry["strictly_positive_on_whole_real_circle_proved"]=bool(d_at_zero>0)
        bounds.append(entry)
        print(json.dumps(entry),flush=True)
    report=dict(kind="exact_rational_finite_polynomial_Wiener_budget",
                polynomials_file=args.polynomials.name,
                polynomials_sha256=hashlib.sha256(args.polynomials.read_bytes()).hexdigest(),
                source_conjugacy_sha256=definitions["source_conjugacy_sha256"],
                Hprime_at_zero_numerator=str(d_at_zero),
                Hprime_at_zero_denominator_power_of_two=args.bits,
                polynomial_degree=degree,inverse_test_degree=args.inverse_degree,
                exp_majorant_order=80,bounds=bounds,
                proof_method="exact integer convolution; ceil integer square roots; rational Taylor exponential majorant; Wiener Neumann series",
                limitations=["H is the explicitly defined dyadic polynomial, not an inferred exact conjugacy",
                             "no bound on actual map E0, parameter twist, P/Q/T/B supplied here",
                             "no actual map reflection, interpolation, ODE, or PDE scattering error paid"])
    args.out.write_text(json.dumps(report,indent=2)+"\n")


if __name__=="__main__":
    main()
