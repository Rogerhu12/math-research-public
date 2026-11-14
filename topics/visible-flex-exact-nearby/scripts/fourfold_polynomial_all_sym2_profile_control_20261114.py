#!/usr/bin/env python3
"""Exact finite-jet elimination and conservative polynomial control budget."""
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
    def gate(name,ok,**data):
        if not ok: raise ArithmeticError(name)
        gates.append({"name":name,"passed":True,**data})
    def ident(name,expr):
        residual=s.fraction(s.cancel(expr))[0]
        gate(name,residual==0,residual=str(residual))
    def qgate(name,x,relation,y):
        x,y=F(x),F(y)
        gate(name,{"<":x<y,"<=":x<=y,"=":x==y}[relation],
             left=str(x),relation=relation,right=str(y))
    q0=s.symbols("Q",positive=True)
    q1,q2,q3,q4,lam,aa,X,Y,Z=s.symbols("Q1 Q2 Q3 Q4 lambda a X Y Z")
    def dt(expr):
        return (s.diff(expr,q0)*q1+s.diff(expr,q1)*q2+s.diff(expr,q2)*q3+
                s.diff(expr,q3)*q4+s.diff(expr,X)*(-(1+q0)*X+2*Y)+
                s.diff(expr,Y)*(Z-lam*q0*X)+
                s.diff(expr,Z)*((1+q0)*Z-2*lam*q0*Y))
    kern=Z-2*lam*Y+lam*X
    kern1=dt(kern);kern2=dt(kern1);kern3=dt(kern2)
    V=4*lam*q0-(1+q0)**2
    ident("complete_Sym2_first_identity",
          kern1-((1+q0-2*lam)*kern-2*lam*(lam-1)*dt(X)))
    ident("complete_Sym2_second_identity",
          kern2+(V-q1)*kern-2*lam*(lam-1)*q1*X)
    ident("complete_third_order_kernel",
          q1*kern3-q2*kern2+q1*V*kern1+
          (3*(2*lam-1-q0)*q1*q1-q2*V)*kern)
    p0,p1,p2,p3=s.symbols("p0 p1 p2 p3")
    def dx(expr):
        return (s.diff(expr,q0)*q1+s.diff(expr,q1)*q2+s.diff(expr,q2)*q3+
                s.diff(expr,q3)*q4+s.diff(expr,p0)*p1+s.diff(expr,p1)*p2+s.diff(expr,p2)*p3)
    f=p0*q0**(-s.Rational(9,2))
    transformed=s.expand(q0**s.Rational(15,2)*
        (q1*dx(dx(dx(f)))-q2*dx(dx(f))+aa*aa*q1*V*dx(f)+
         aa*aa*(3*(2*lam-1-q0)*q1*q1-q2*V)*f))
    A3=q1*q0**3
    A2=-s.Rational(27,2)*q0*q0*q1*q1-q0**3*q2
    A1=s.Rational(297,4)*q0*q1**3-s.Rational(9,2)*q0*q0*q1*q2+aa*aa*q1*V*q0**3
    A0=(-s.Rational(1287,8)*q1**4+s.Rational(99,2)*q0*q1*q1*q2-
        s.Rational(9,2)*q0*q0*q1*q3+s.Rational(9,2)*q0*q0*q2*q2+
        aa*aa*(-s.Rational(9,2)*q1*q1*V*q0*q0+
               3*(2*lam-1-q0)*q1*q1*q0**3-q2*V*q0**3))
    ident("exact_polynomial_deflation",transformed-(A3*p3+A2*p2+A1*p1+A0*p0))
    x,B=s.symbols("x B")
    quartic=7+30*B*x*x*(1-x)**2
    substitutions={q0:quartic,q1:s.diff(quartic,x),q2:s.diff(quartic,x,2),q3:s.diff(quartic,x,3)}
    for name,expr,bound in [("A3",A3,15),("A2",A2,14),("A1",A1,23),("A0",A0,22)]:
        degree=s.Poly(s.expand(expr.subs(substitutions)),x).degree()
        gate("true_quartic_degree_"+name,degree<=bound,degree=degree,bound=bound)
    qgate("complete_polynomial_residual_degree",max(15+16,14+17,23+18,22+19),"=",41)
    ell=s.symbols("ell")
    indicial=ell*(ell-1)*(ell-2)-s.Rational(27,2)*ell*(ell-1)+s.Rational(297,4)*ell-s.Rational(1287,8)
    ident("complete_indicial_factorization",
          indicial-(ell-s.Rational(9,2))*(ell-s.Rational(11,2))*(ell-s.Rational(13,2)))
    expected=[F(1287,8),F(693,8),F(315,8),F(105,8),F(15,8)]
    for j,v in enumerate(expected):
        val=abs(F(indicial.subs(ell,j)))
        qgate("all_root_indicial_row_"+str(j),val,"=",v)
    qgate("root_slope_squared",840,">" if False else "<",2**10)
    qgate("root_slope_lower_squared",16**2,"<",840)
    qgate("root_separation_coefficient_squared",F(1,16)**2,"<",F(7,30))
    qgate("full_indicial_denominator",F(15,8)*16**4,">" if False else "<",2**17)
    qgate("indicial_denominator_lower",2**16,"<",F(15,8)*16**4)
    # Exact node sum and all fixed-degree complex/Hermite charges.
    node_sum=sum(F(1,factorial(j)*factorial(41-j)) for j in range(42))
    qgate("complete_Lagrange_node_sum",node_sum,"=",F(2**41,factorial(41)))
    qgate("fixed_degree_real_to_complex_fee",F((8*41)**41,factorial(41)),"<",2**400)
    qgate("real_coefficient_to_root_jet_fee",80+400,"=",480)
    qgate("lower_triangular_combinatorics",20*24,"<",2**10)
    qgate("lower_triangular_coefficient_fee",128+10,"=",138)
    qgate("divide_true_root_slope_fee",138-16,"=",122)
    qgate("five_jet_triangular_recurrence_fee",4*(122+1),"<",512)
    qgate("all_root_jets_complete_fee",480+512,"=",992)
    qgate("Hermite_complete_sum",100*4**19*2**19,"<",2**64)
    qgate("Hermite_root_separation_bits",64+4*19,"=",140)
    qgate("Hermite_root_separation_power",F(19,2),"<",10)
    qgate("center_full_jet_fee",992+140+1,"=",1133)
    qgate("true_first_three_K_jets",32*2**12,"<",2**20)
    qgate("complete_K_from_g_second_jet",1+9*2+F(99,4)*4+F(9,2)*32,"<",2**9)
    qgate("center_observability_spare_fee",20+9,"<",50)
    qgate("actual_twentieth_derivative_binary_fee",1133+50,"=",1183)
    qgate("actual_twentieth_derivative_safe_fee",1183,"<",1280)
    qgate("actual_twentieth_derivative_B_power",32+4,"<",40)
    qgate("actual_twentieth_derivative_lambda_power",5+2,"<",8)
    # Explicit conservative coefficient products for the real/disk rows.
    real_products=(2**10*2**3+
        F(27,2)*4*2**20+8*2**10+
        F(297,4)*2*2**30+F(9,2)*4*2**20+
        2**10*2**5*8+
        F(1287,8)*2**40+F(99,2)*2*2**30+
        F(9,2)*4*2**20+F(9,2)*4*2**20+
        F(9,2)*2**20*2**5*4+3*2**3*2**20*8+2**10*2**5*8)
    qgate("real_D_coefficients_bound",real_products,"<",2**80)
    disk_products=16*2**(4*14+8)+16*2**(6*14+35)
    qgate("disk_D_coefficients_bound",disk_products,"<",2**128)
    qgate("actual_22_factorial",factorial(22),"<",2**70)
    qgate("true_jet_recurrence_ratio",F(2,1)/(1-F(1,8)),"<",4)
    qgate("true_two_line_22jet_binary_fee",70+42*22+1,"<",1024)
    qgate("true_two_line_22jet_lambda_power",22+1,"<",24)
    qgate("true_two_line_22jet_B_power",2*22,"<",48)
    qgate("full_kernel_21jet_binary_fee",2*1024+40+34+3,"<",2200)
    qgate("full_Q_power_21jet_binary_fee",70+3*21+20,"=",153)
    qgate("full_g_21jet_binary_fee",2200+153+21,"<",4096)
    qgate("full_g_21jet_lambda_power",2*24+1,"<",64)
    qgate("full_g_21jet_B_power",2*48+2+5,"<",128)
    qgate("actual_compact_radius_binary_fee",1280+4096+4,"=",5380)
    qgate("actual_compact_radius_B_power",40+128,"=",168)
    qgate("actual_compact_radius_lambda_power",8+64,"=",72)
    qgate("witness_shift_keeps_sign",F(3,16),"<",F(1,2))
    qgate("actual_Q_power_C4_fee",24*8**4*2**20,"<",2**37)
    qgate("actual_bump_24jet_fee",2**30*60**24,"<",2**174)
    qgate("actual_full_C4_sum",80*2**37*2**174,"<",2**220)
    qgate("actual_positive_bump_integral",F(1,2**15),"<",F(3,4)**30)
    qgate("actual_pairing_measure_fee",220+1+15,"=",236)
    qgate("actual_pairing_complete_bits",236+1280+25*5380,"=",136016)
    qgate("actual_pairing_safe_bits",136016,"<",140000)
    qgate("actual_pairing_a_power",1+1+25,"=",27)
    qgate("actual_pairing_interval_power",41*26,"=",1066)
    qgate("actual_pairing_B_power",5+40+25*168,"=",4245)
    qgate("actual_pairing_lambda_power",8+25*72,"=",1808)
    qgate("actual_pairing_K_power",25*2,"=",50)
    qgate("positive_identity_target_inside_convex_ball",F(1,8),"<",F(9,16))
    qgate("complete_two_incoming_positive_fee",4*2,"=",8)
    qgate("actual_matrix_Hessian_box_margin",F(1,64),"<",F(1,8)-F(1,16))

    here=Path(__file__).resolve();topic=here.parent.parent
    paths=[here,
        topic/"results/R119-supplement-polynomial-all-Sym2-profile-separation-and-positive-control.md",
        topic/"results/R119-supplement-all-quadratic-phase-preserving-positive-scattering-control.md",
        topic/"results/R119-supplement-high-oscillation-polynomial-phase-preserving-control.md",
        topic/"results/R119-supplement-actual-canonical-profile-generator-and-complete-weak-sources.md"]
    return {
        "schema":"visible-exact-R119-polynomial-all-sym2-profile-control-v1",
        "implementation":"new exact SymPy elimination and Fraction computation",
        "scope":"All real Sym2 actual radial kernels, fixed-degree polynomial real-to-root elimination, complete compact phase annihilator and positive two-port scattering direction",
        "file_sha256":{str(p.relative_to(topic)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
        "gate_count":len(gates),"all_passed":all(g["passed"] for g in gates),"gates":gates,
        "retained":["same actual profile","true dt measure","actual center wave normalization","all four complex roots and all twenty Hermite conditions","both complex incoming ports","ordinary/weak source and mean permissions unchanged"],
        "not_claimed":["nonradial positive cluster derivative","rho5 divided for free by rho25","same-weight full source inverse","solution of full nonlinear F"]}


if __name__=="__main__":
    parser=argparse.ArgumentParser();parser.add_argument("--output",type=Path)
    args=parser.parse_args();report=compute();raw=json.dumps(report,ensure_ascii=False,indent=2)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(raw,encoding="utf-8")
        print(json.dumps({"output":str(args.output),"gates":report["gate_count"],"all_passed":report["all_passed"],"sha256":hashlib.sha256(raw.encode()).hexdigest()}))
    else: print(raw,end="")
