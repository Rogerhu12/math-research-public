#!/usr/bin/env python3
"""Exact energy identities and actual-label budgets for the full packet map."""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import factorial
from pathlib import Path
import sympy as s


def compute():
    gates=[]
    def gate(name, ok, **data):
        if not ok:
            raise ArithmeticError(name)
        gates.append({"name":name,"passed":True,**data})
    def ident(name, expr):
        residual=s.fraction(s.cancel(expr))[0]
        gate(name,residual==0,residual=str(residual))
    def qgate(name,x,relation,y):
        x,y=F(x),F(y)
        gate(name,{"<":x<y,"<=":x<=y,"=":x==y}[relation],left=str(x),relation=relation,right=str(y))
    def expgate(name,left,right):
        gate(name,left<right,left_binary_exponent=left,right_binary_exponent=right)

    th=s.symbols("theta")
    aa,cc,dd,hh,pp=[s.Function(n)(th) for n in ("a","c","d","h","pi")]
    at,ct,Q,Qt,b,bt=s.symbols("a_t c_t Q Q_t b b_t")
    der=lambda x:s.diff(x,th)
    ht=dd*der(hh)+aa*pp
    pit=der(dd*pp)+Q*der(cc*der(hh))
    energy_t=(ct*Q+cc*Qt)*der(hh)**2+2*cc*Q*der(hh)*der(ht)+at*pp**2+2*aa*pp*pit
    claimed=(ct*Q+cc*Qt+der(dd)*cc*Q-dd*Q*der(cc))*der(hh)**2+(at+der(dd)*aa-dd*der(aa))*pp**2
    flux=cc*Q*dd*der(hh)**2+aa*dd*pp**2+2*aa*cc*Q*pp*der(hh)
    ident("complete_wave_energy_with_true_cross_terms",s.expand(energy_t-claimed-der(flux)))
    mass_t=bt*hh**2+2*b*hh*ht
    mass_claimed=(bt-b*der(dd))*hh**2+2*b*aa*hh*pp
    ident("complete_height_mean_mass_energy",mass_t-mass_claimed-der(b*dd*hh**2))

    w,p,k,q,kt,ptt,ktt=s.symbols("w p k q kt ptt ktt")
    E=1+w*w; T=1-p*p; K=w+k; J=K+E*q; D=E*T-K*K; z=kt-p
    f=w*(-k-q+w*(k*q-p*p))/J
    d=E*z/J
    def theta(expr):
        return sum(s.diff(expr,x)*y for x,y in ((p,q),(k,kt),(q,ptt),(kt,ktt)))
    def control(expr):
        return w*s.diff(expr,w)+f*s.diff(expr,k)+theta(f)*s.diff(expr,kt)
    def U(expr):
        return sum(s.diff(expr,x)*y for x,y in ((p,z),(k,E*z*z/J),(q,ktt-q)))
    BJ,BD=control(J),control(D)
    fk=s.diff(f,k)
    loga_t=1+s.Rational(3,2)*(U(D)-Q*BD)/D-(U(J)-Q*BJ)/J
    loga_theta=s.Rational(3,2)*theta(D)/D-theta(J)/J
    ident("exact_complete_flux_energy_log_derivative",loga_t-d*loga_theta+theta(d)-(1-d*d/E-Q*fk))
    logc_t=-1-(U(J)-Q*BJ)/J-(U(D)-Q*BD)/(2*D)-2*Q
    logc_theta=-theta(J)/J-theta(D)/(2*D)
    Bc=2-BJ/J-BD/(2*D)
    ident("exact_complete_gradient_energy_log_derivative",logc_t-d*logc_theta+theta(d)-(-Q*Bc-1-d*d/E))
    for ell in (1,2,3):
        Fl=sum(s.binomial(ell,r)*(s.diff(dd,th,r)*s.diff(hh,th,ell+1-r)+s.diff(aa,th,r)*s.diff(pp,th,ell-r)) for r in range(1,ell+1))
        Gl=sum(s.binomial(ell,r)*der(s.diff(dd,th,r)*s.diff(pp,th,ell-r)+Q*s.diff(cc,th,r)*s.diff(hh,th,ell+1-r)) for r in range(1,ell+1))
        ident("full_height_commutator_order_"+str(ell),s.diff(ht,th,ell)-dd*s.diff(hh,th,ell+1)-aa*s.diff(pp,th,ell)-Fl)
        ident("full_flux_commutator_order_"+str(ell),s.diff(pit,th,ell)-der(dd*s.diff(pp,th,ell))-Q*der(cc*s.diff(hh,th,ell+1))-Gl)

    tiny=F(1,2**512); n=F(1,2**4096)
    qgate("packet_inside_unused_interval",F(8,32),"<",F(1,2))
    qgate("scaled_length_inverse",tiny/80,"<",tiny)
    qgate("complete_four_jet_factorial_sum",sum(factorial(j) for j in range(5)),"=",34)
    qgate("true_energy_growth_all_modes",3+8*tiny+2*tiny/80+2**40*n,"<",4)
    qgate("energy_log_growth_full_packet",4*16,"=",64)
    # e < 11/4 follows from its ordinary positive rational Taylor remainder.
    esum=sum(F(1,factorial(j)) for j in range(10))
    erem=F(1,factorial(10))*F(11,10)
    qgate("exp_unit_rational_upper",esum+erem,"<",F(11,4))
    qgate("exp32_sqrt8_binary_margin",F(11,4)**64*8,"<",2**98)
    qgate("full_packet_Cauchy_margin",49,"<",56)
    qgate("complete_Duhamel_packet_fee",56+40+56+4,"<",160)
    qgate("band_input_H1_fee_squared",1+4,"=",5)
    qgate("band_input_H3_fee_squared",1+4+16+64,"<",128)
    qgate("kernel_actual_coefficient_fee",2**20*5*2**112,"<",2**135)
    qgate("kernel_full_solution_difference_fee",4*(2*2**56)*2**160*5,"<",2**222)
    qgate("kernel_sum_and_true_measure_fee",2*(2**135+2**222),"<",2**232)
    qgate("profile_wave_scale_exact_exponent",232-72,"=",160)
    qgate("complete_response_packet_fee",16+112+4,"<",136)
    qgate("center_true_shear_small",F(9,2)*tiny**2,"<",F(1,2))
    qgate("center_true_wave_comparison",2+F(9,2)*tiny**2,"<",4*F(3,2))
    qgate("actual_rank_one_radial_binary_fee",-2039-2+4*72,"=",-1753)
    qgate("radial_comparison_spare_bits",-1800,"<",-1753)
    expgate("actual_complete_input_n",160019-262144,-4096)
    qgate("P_deep_exponent",F(7,4)+F(14,256),"=",F(231,128))
    qgate("P_real_first_layer",-42+F(231,128)*8197,"<",14800)
    qgate("P_next_layer_multiplier",F(231,128),"<",2)
    qgate("actual_deep_product_exponent",F(31867,256)-F(231,128),"=",F(31405,256))
    qgate("actual_deep_product_decreases",0,"<",F(31405,256))
    qgate("complete_global_normalization_factor_kept",160017+14800+2,"<",175000)
    qgate("direct_relative_binary_fee",160+1800+160019,"=",161979)
    expgate("actual_direct_error_less_eighth",161979-262144,-3)
    qgate("response_profile_scale_binary_fee",136+832+1800-72,"=",2696)
    qgate("true_high_frequency_response_gain",2696-1024,"=",1672)
    expgate("actual_response_error_less_eighth",1672+175000-262144,-3)
    qgate("both_errors_leave_half",F(1,8)+F(1,8),"<",F(1,2))

    here=Path(__file__).resolve(); topic=here.parent.parent
    paths=[here,
        topic/"results/R119-supplement-actual-wave-packet-Cauchy-and-rank-one-profile-control.md",
        topic/"results/R119-supplement-actual-canonical-profile-generator-and-complete-weak-sources.md",
        topic/"results/R119-supplement-actual-compact-profile-label-response.md",
        topic/"results/R119-supplement-high-oscillation-polynomial-phase-preserving-control.md",
        topic/"results/R119-supplement-controlled-tail-actual-joint-phase-and-remainder.md"]
    return {
        "schema":"visible-exact-R119-actual-wave-packet-profile-control-v1",
        "implementation":"new exact rational-jet and Fraction computation in restored terminal",
        "scope":"Complete actual packet Cauchy, frequency-band input with all-frequency output, real single-mode rank-one profile form including actual label response on the packet",
        "file_sha256":{str(p.relative_to(topic)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
        "gate_count":len(gates),"all_passed":all(g["passed"] for g in gates),"gates":gates,
        "retained":["two physical means","all output Fourier modes","true total-flux weak source","same current Gamma","real fixed-label background response","actual normalization factors"],
        "not_claimed":["full Sym2 polynomial positive control","nonradial multifrequency-cluster inverse","response outside packet is zero","joint Gamma derivative is zero","full nonlinear F solved"]}


if __name__=="__main__":
    parser=argparse.ArgumentParser();parser.add_argument("--output",type=Path)
    args=parser.parse_args();report=compute();raw=json.dumps(report,ensure_ascii=False,indent=2)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(raw,encoding="utf-8")
        print(json.dumps({"output":str(args.output),"gates":report["gate_count"],"all_passed":report["all_passed"],"sha256":hashlib.sha256(raw.encode()).hexdigest()}))
    else: print(raw,end="")
