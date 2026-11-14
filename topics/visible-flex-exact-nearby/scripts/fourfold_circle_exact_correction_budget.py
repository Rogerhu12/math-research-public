#!/usr/bin/env python3
"""Preserve small actual-Newton Fourier corrections by exact rational addition.

The old H is its stored dyadic polynomial. Each computed binary64 correction
is added as an exact Fraction before rounding once to the new denominator.
No sample FFT is used to redefine H. A sampled inverse only chooses q; the
R48 exact integer convolution proves the resulting inverse-derivative budget.
This does not certify the actual Newton equation or the ray-map residual.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

import numpy as np

from fourfold_circle_conjugacy_budget import (
    integer_fourier, convolution, norm_upper, dyadic_upper,
)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def nearest_dyadic_integer(value, bits):
    # Python Fraction.__round__ uses exact nearest integer, ties to even.
    return round(value*(1 << bits))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--newton-report",type=Path,required=True)
    parser.add_argument("--base-polynomials",type=Path,required=True)
    parser.add_argument("--polynomials",type=Path,required=True)
    parser.add_argument("--out",type=Path,required=True)
    parser.add_argument("--bits",type=int,default=120)
    parser.add_argument("--inverse-degree",type=int,default=512)
    parser.add_argument("--width-denominators",type=int,nargs="+",default=[512,256,128,64,32])
    args=parser.parse_args()
    prediction=json.loads(args.newton_report.read_text())
    old=json.loads(args.base_polynomials.read_text())
    if prediction["source_H_sha256"]!=digest(args.base_polynomials):
        raise ValueError("Newton report uses another exact initial H")
    labels=prediction["basis_labels"]
    corrections=prediction["coefficient_correction"]
    if len(labels)!=len(corrections):raise ValueError("incomplete finite correction")
    degree=max(int(k) for k,kind in labels)
    if degree<int(old["H_degree"]):raise ValueError("correction truncates the initial H")
    positive=[[Fraction(0),Fraction(0)] for _ in range(degree+1)]
    old_scale=1 << int(old["denominator_power_of_two"])
    for k,(real,imag) in enumerate(old["h_nonnegative_integer_coefficients"]):
        positive[k]=[Fraction(int(real),old_scale),Fraction(int(imag),old_scale)]
    if positive[0][1]:raise ValueError("H is not real")
    for (k,kind),value in zip(labels,corrections):
        delta=Fraction.from_float(float(value))/2
        if kind=="cos":positive[int(k)][0]+=delta
        elif kind=="sin":positive[int(k)][1]-=delta
        else:raise ValueError("unknown real Fourier basis label")
    pos=[tuple(nearest_dyadic_integer(v,args.bits) for v in pair) for pair in positive]
    scale=1 << args.bits
    errors=[[Fraction(a,scale)-r,Fraction(b,scale)-i]
            for (a,b),(r,i) in zip(pos,positive)]
    coefficient_rounding=[sum((1 if k==0 else 2)*(k**order if order else 1)*
        (abs(re)+abs(im)) for k,(re,im) in enumerate(errors)) for order in range(3)]
    h=[(a,-b) for a,b in pos[:0:-1]]+pos
    d=[(-k*b,k*a) for k,(a,b) in zip(range(-degree,degree+1),h)]
    d[degree]=(scale,0)
    count=max(8192,8*(args.inverse_degree+degree+1))
    x=np.arange(count)*2*np.pi/count;k=np.arange(-degree,degree+1)
    dc=np.array([complex(a,b)/scale for a,b in d])
    derivative=np.real(np.exp(1j*np.outer(x,k))@dc)
    if np.min(derivative)<=0:raise ValueError("sampled inverse selection failed")
    qpositive=np.fft.fft(1/derivative)[:args.inverse_degree+1]/count
    q=integer_fourier(qpositive,args.bits)
    product=convolution(d,q);residual=[(-a,-b) for a,b in product]
    center=(len(residual)-1)//2
    residual[center]=(residual[center][0]+(1 << (2*args.bits)),residual[center][1])
    d_at_zero=sum(a for a,b in d)
    definitions=dict(kind="exact_dyadic_trigonometric_polynomials_H_and_q",
        coefficient_convention="h(x)=sum h_k exp(i k x); H=x+h; negative coefficients conjugate",
        denominator_power_of_two=args.bits,H_degree=degree,q_degree=args.inverse_degree,
        h_nonnegative_integer_coefficients=[[str(a),str(b)] for a,b in pos],
        q_nonnegative_integer_coefficients=[[str(a),str(b)] for a,b in q[args.inverse_degree:]],
        source_base_polynomials_sha256=digest(args.base_polynomials),
        source_newton_report_sha256=digest(args.newton_report),
        construction="exact old dyadic H plus exact binary64 finite correction; one exact ties-to-even dyadic rounding; unchanged old constant, no precomposition",
        source_metadata={key:prediction[key] for key in
            ("target","rotation_number","angular_scale","base_parameter_delta",
             "proposed_parameter_delta","exact_delta_fraction","actual_nodes_sha256")})
    args.polynomials.write_text(json.dumps(definitions,indent=2)+"\n")
    bounds=[];cache={}
    for denominator in args.width_denominators:
        width=Fraction(1,denominator)
        hn=norm_upper(h,args.bits,width,cache);dn=norm_upper(d,args.bits,width,cache)
        qn=norm_upper(q,args.bits,width,cache);rn=norm_upper(residual,2*args.bits,width,cache)
        entry=dict(width_numerator=1,width_denominator=denominator,
            h_Wiener_upper=dyadic_upper(hn),Hprime_Wiener_upper=dyadic_upper(dn),
            q_Wiener_upper=dyadic_upper(qn),product_residual_Wiener_upper=dyadic_upper(rn),
            exact_rational_Neumann_test_passed=bool(rn<1),Hprime_at_zero_positive=bool(d_at_zero>0))
        if rn<1:
            entry["inverse_Hprime_Wiener_upper"]=dyadic_upper(qn/(1-rn))
            entry["strictly_positive_on_whole_real_circle_proved"]=bool(d_at_zero>0)
        bounds.append(entry);print(json.dumps(entry),flush=True)
    report=dict(kind="exact_integer_correction_and_rational_H_inverse_budget",
        run_source_sha256=digest(Path(__file__)),
        source_newton_report_sha256=digest(args.newton_report),
        source_base_polynomials_sha256=digest(args.base_polynomials),
        polynomials_file=args.polynomials.name,polynomials_sha256=digest(args.polynomials),
        polynomial_degree=degree,inverse_test_degree=args.inverse_degree,
        Hprime_at_zero_numerator=str(d_at_zero),Hprime_at_zero_denominator_power_of_two=args.bits,
        correction_rounding_C0_C1_C2_upper=[dyadic_upper(v,args.bits) for v in coefficient_rounding],
        exact_old_constant_preserved=bool(errors[0][0]==0),
        exp_majorant_order=80,bounds=bounds,
        proof_method="exact Fraction addition; exact ties-to-even dyadic rounding; R48 integer convolution, rational exp majorant and Wiener Neumann series",
        limitations=["computed finite Newton corrections are interpreted exactly, not proved to solve the true map equation",
            "a new exact H requires fresh actual ray validation and continuous E bounds",
            "q selection is floating, but its certificate is the exact finite convolution",
            "no root, geometric parameter, complete map or PDE error is paid by this report"])
    args.out.write_text(json.dumps(report,indent=2)+"\n")


if __name__=="__main__":main()
