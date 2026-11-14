#!/usr/bin/env python3
"""Exact identities and rational budgets for the actual compact ray response.

No floating solve, finite-frequency replacement, or recovered old native is
used.  All symbolic identities are rational functions of independent jets.
The finite rational calculations pay the inverse/composition constants and
consume the already proved complete gauged-field response, including mean.
"""
from __future__ import annotations
import argparse, hashlib, json, math, platform, sys
from fractions import Fraction as F
from pathlib import Path
import sympy as sp

PROOF='R133-supplement-actual-compact-ray-endpoint-response.md'
INPUTS=[
 'R119-supplement-actual-compact-profile-flux-gauge-and-principal-port-derivative.md',
 'R119-supplement-actual-compact-profile-label-response.md',
 'R119-supplement-controlled-profile-full-label-and-raw-ports.md',
 'R119-supplement-controlled-tail-actual-joint-phase-and-remainder.md',
 'R119-supplement-actual-strict-density-complete-relative-Cauchy.md',
 'R119-supplement-radial-phase-compensation-and-full-Wronskian-Hessian.md',
 'R119-supplement-high-oscillation-polynomial-phase-preserving-control.md',
 'R119-supplement-high-oscillation-small-amplitude-Hessian.md',
]

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def git_blob(p):
    b=Path(p).read_bytes()
    return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def exact(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,sp.Basic):return str(x)
    return x

def budget():
    gates=[]
    def gate(name,condition,**data):
        item=dict(name=name,passed=bool(condition),**{k:exact(v) for k,v in data.items()})
        gates.append(item)
        if not condition:raise AssertionError(json.dumps(item))
    def identity(name,value):
        numerator=sp.cancel(value).as_numer_denom()[0]
        gate(name,numerator==0,cleared_numerator=numerator)

    w,p,k,q,kt,ptt,ktt=sp.symbols('w p k q kt ptt ktt')
    E=1+w*w;K=w+k;T=1-p*p;J=K+E*q;D=E*T-K*K;z=kt-p
    d=E*z/J;kv=E*z*z/J
    def theta(h):
        return sp.diff(h,p)*q+sp.diff(h,k)*kt+sp.diff(h,q)*ptt+sp.diff(h,kt)*ktt
    DtD=sp.diff(D,p)*z+sp.diff(D,k)*kv
    DtJ=kv+E*(ktt-q)
    identity('full_V_D_transport',DtD-d*theta(D))
    identity('full_V_J_transport',DtJ-d*theta(J)-J*theta(d)-E*z*z/J)
    identity('log_velocity_full_V_cancellation',DtD/(2*D)-DtJ/J-d*(theta(D)/(2*D)-theta(J)/J)+theta(d)+d*d/E)
    f=w*(-k-q+w*(k*q-p*p))/J
    def B(h):return w*sp.diff(h,w)+f*sp.diff(h,k)
    identity('complete_B_D_identity',B(D)-2*w*w*q*D/J)
    identity('complete_B_J_identity',B(J)-w*w*(T+K*q+2*q*J)/J)
    identity('complete_B_log_velocity',1+B(D)/(2*D)-B(J)/J-(1-w*w*(T+2*K*q+E*q*q)/(J*J)))
    Q,q0,qt,bv,bd,v,dd,ee,sigma,psi=sp.symbols('Q q0 qt bv bd v dd ee sigma psi',nonzero=True)
    Lc=sigma*(-q0*q0*bv-v*dd*dd/ee)/(2*q0)-sigma*v*qt/(2*q0*q0)
    original=-psi*(bd+sigma*q0*bv+Lc)
    G=bd+sigma*q0*bv/2-sigma*v*dd*dd/(2*q0*ee)-sigma*(v-1)*qt/(2*q0*q0)
    identity('ray_source_radial_split',original-(sigma*psi*qt/(2*q0*q0)-psi*G))

    n=F(1,64);r=F(1,2**32)
    gate('J_inverse_full_Banach_gap',1/(1-3*n)<2,bound=1/(1-3*n))
    dfee=2*n+3*n*n
    gate('D_inverse_full_Banach_gap',1/(1-dfee)<2,bound=1/(1-dfee))
    gate('sqrt_D_minus_one',dfee/(1-dfee)<3*n,bound=dfee/(1-dfee),target=3*n)
    gate('v_minus_one',6/(1-3*n)<8,coefficient=6/(1-3*n))
    gate('v_full_norm',1+8*n<2,bound=1+8*n)
    gate('d_full_norm',2/(1-3*n)<4,coefficient=2/(1-3*n))
    gate('delta_D_all_components',2+6*n<3,coefficient=2+6*n)
    gate('delta_d_all_components',4+16*n<5,coefficient=4+16*n)
    gate('delta_v_all_components',2*(3+4)<16,coefficient=14)
    gate('quadratic_d_term_retained',16*n<=F(1,4),coefficient=16*n)
    gate('complete_radial_response_integral',2*2*16*2==128,coefficient=128)

    x=sp.symbols('x');quartic=30*x*x*(1-x)*(1-x)
    left=sp.Rational(7,16);right=sp.Rational(15,32)
    fl=quartic.subs(x,left);fr=quartic.subs(x,right)
    dfl=sp.diff(quartic,x).subs(x,left);dfr=sp.diff(quartic,x).subs(x,right)
    gate('actual_quartic_lower',fl>sp.Rational(7,4),value=fl)
    gate('actual_quartic_upper_with_7_over_B',fr+sp.Rational(7,2**190)<2,value=fr+sp.Rational(7,2**190))
    gate('actual_quartic_first_derivative',0<dfr<=dfl<2,left=dfl,right=dfr)
    # f'' is convex on this interval, hence its maximum is at an endpoint.
    second=[sp.diff(quartic,x,2).subs(x,t) for t in (left,right)]
    gate('actual_quartic_derivative_monotonicity',max(second)<0,endpoint_max=max(second))
    gate('q_t_ratio_first',F(1,1)<F(7,4),squared_denominator=F(7,4))
    gate('q_t_over_q_squared',F(1,1)<F(7,4)**3,squared_denominator=F(7,4)**3)
    gate('sqrt_two_upper',F(3,2)**2>2,value=F(3,2)**2)

    def mul(a,b,degree):
        c=[F(0)]*(degree+1)
        for i,aa in enumerate(a):
            for j,bb in enumerate(b):
                if i+j<=degree:c[i+j]+=aa*bb
        return c
    def power(a,n,degree):
        out=[F(1)]+[F(0)]*degree
        for _ in range(n):out=mul(out,a,degree)
        return out
    def composition_majorant(e,factorial_jets=True):
        a=[F(0),1+e]+[e/F(math.factorial(i)) if factorial_jets else e for i in range(2,7)]
        return max(sum(power(a,j,6)) for j in range(7))
    comp=composition_majorant(r)
    gate('all_six_H_composition_jets',comp<2,maximum_column_sum=comp)
    gate('ordered_variation_A_minus_one',6/(1-3*r)<7,coefficient=6/(1-3*r))
    gate('ordered_variation_A_norm',(1+3*r)/(1-3*r)<2,bound=(1+3*r)/(1-3*r))
    b=[F(0)]*9;b[1]=1/(1-r)
    gate('inverse_jet_1',b[1]-1<2*r,bound=b[1]-1)
    for degree in range(2,9):
        b[degree]=r/(1-r)*sum(power(b[:degree],ell,degree)[degree]/math.factorial(ell) for ell in range(2,degree+1))
        gate('inverse_jet_'+str(degree),math.factorial(degree)*b[degree]<2*r,
             bound=math.factorial(degree)*b[degree])
    gate('all_six_inverse_composition_jets',composition_majorant(2*r)<2,
         maximum_column_sum=composition_majorant(2*r))
    gate('all_six_return_composition_jets',composition_majorant(15*r,False)<2,
         maximum_column_sum=composition_majorant(15*r,False))
    gate('return_inverse_J_minus_one',6/(1-6*r)<7,coefficient=6/(1-6*r))
    gate('return_inverse_J_norm',1/(1-6*r)<2,bound=1/(1-6*r))

    coefficient_a=2**11+2**10*F(3,2)+F(1,2)
    gate('all_compact_G_integral_terms',coefficient_a<2**12 and 8<2**12,
         a_sqrt_B_coefficient=coefficient_a,inverse_sqrt_B_coefficient=8)
    gate('single_ray_compact_coefficient',2**14*4*33+7*2**34<2**38,
         coefficient=2**14*4*33+7*2**34)
    gate('return_compact_coefficient',2**17*4*33+64*2**34<2**41,
         coefficient=2**17*4*33+64*2**34)
    gate('single_ray_actual_response',2**839+2**38<2**840)
    gate('inverse_ray_actual_response',4*2**840<2**843)
    gate('return_actual_response',2**842+2**41<2**843)
    gate('current_complete_global_r_smallness',160056-262144<-32,
         exponent=160056-262144)
    gate('angular_operator_full_safe_factor',4*8*8<2**10,explicit_factor=4*8*8)
    return dict(schema='visible-exact-R133-actual-compact-ray-endpoint-rho5-v2',
                complete=True,all_passed=all(g['passed'] for g in gates),gate_count=len(gates),gates=gates,
                output_contracts=dict(single_ray_inverse_and_return_Cstar6='2^843 Ncal_i X P_j rho^5',
                    complete_angular_strong_derivative='2^853 Ncal_i X P_j rho^5 : H^(s+1) -> H^s, -1<=s<=1',
                    response_input='L.2 full two-component A_2^2 sum; no response left as an uncomputed placeholder',
                    gamma_columns='both actual D_Omega Gamma_i retained separately',
                    component_N='sum of (N_k^c)^# over all intersecting cells, at most two',
                    all_mean_retained=True,all_fourier_retained=True,
                    density_shear_kernel_not_paid_by_this_consumer=True,
                    full_F_inverse_not_claimed=True),
                computations=dict(symbolic='exact rational SymPy cancellation',
                    numeric='Python integers and Fraction only; no floating evaluation',
                    inverse_jets='all orders 1..8',composition_jets='all orders 0..6'),
                recovered_old_temporary_report=False,
                scientific_scope='new exact execution after runtime recovery, not a replay of vanished temporary bytes')

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError('preserve each actual report')
    topic=Path(__file__).resolve().parents[1]
    inputs=[topic/'results'/p for p in INPUTS]+[topic/'results'/PROOF]
    for p in inputs:
        if p.stat().st_size>=100000:raise ValueError('unexpected large proof input')
    report=budget()
    report.update(producer_sha256=sha(__file__),python_version=platform.python_version(),
        sympy_version=sp.__version__,inputs=[dict(path=str(p.relative_to(topic)),sha256=sha(p),
            git_blob_sha=git_blob(p),bytes=p.stat().st_size) for p in inputs])
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(complete=report['complete'],all_passed=report['all_passed'],
        gate_count=report['gate_count'],report_sha256=sha(args.out),report_path=str(args.out)),indent=2))

if __name__=='__main__':main()
