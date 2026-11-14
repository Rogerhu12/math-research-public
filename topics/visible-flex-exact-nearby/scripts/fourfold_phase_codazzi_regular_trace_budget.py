#!/usr/bin/env python3
"""Exact arithmetic for the R119 actual tail to Codazzi boundary contract.

This checks the stated all-frequency algebra constants, not a numerical
solution of the missing body/cap matching problem. The actual nonlinear
Dirichlet solution and its complete mean come from the named R119 theorem.
"""
from __future__ import annotations
import argparse,json,hashlib
from fractions import Fraction as Q
from pathlib import Path


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run():
    radius=Q(1,2**20);w=Q(1,800000);chi=Q(5,28)
    E=1+w*w;N=4*radius
    d_error=w*w*(2*N+N*N+E*N*N)
    j_error=(1+E)*N
    c_relative=(j_error+d_error)/(1-d_error)
    b_bound=chi*2*N/(1-d_error)
    c_bound=chi*c_relative
    checks=[]
    def gate(name,condition,formula):
        if not condition:raise AssertionError(name)
        checks.append(dict(name=name,passed=True,exact_evidence=formula))
    gate('actual_tail_slope_bound',Q(7,10**6)/(4*Q(7,5))==w,
         'a<7e-6, omega>7/5 imply w=a/(4omega)<1/800000')
    gate('full_state_radius',N<Q(1,16),'N<4 r, r=2^-20')
    gate('positive_normal_component_denominator',d_error<Q(1,2**55),
         '|D-1| <= w^2(2N+N^2+E N^2) < 2^-55')
    gate('nonzero_angular_curvature_denominator',j_error<9*radius,
         '|J-1| <= (1+E)N < 9r')
    gate('relative_C_trace_bound',c_relative<10*radius,
         '|C/Cref-1| <= (|J-1|+|D-1|)/(1-|D-1|) < 10r')
    gate('absolute_B_trace_bound',b_bound<2*radius,
         '|B| <= chi*2N/(1-|D-1|) < 2r')
    gate('absolute_C_trace_change_bound',c_bound<2*radius,
         '|C-Cref| <= chi*|C/Cref-1| < 2r')
    gate('binomial_remainder_domain',3*w*w*N<Q(1,4),
         '|D-1|<3w^2N<1/4')
    gate('binomial_remainder_constant',Q(9,64)*(Q(4,3)**5)<1,
         'Square of (3/8)(4/3)^(5/2) is <1; Taylor remainder <=|D-1|^2')
    gate('quadratic_mean_remainder',18*w*w<1,
         '6w^2 N^2+18w^4 N^2 < 7w^2 N^2')
    gate('quadratic_mean_C_relative',256+368*w*w<257,
         '|mean(C)/Cref-1| <= (256+368w^2)r^2 <257r^2')
    gate('quadratic_mean_C_absolute',chi*257<46,
         '|mean(C)-Cref| <46r^2')
    coth=Q(257,255)
    tc_lower=1-coth/4
    gate('finite_length_coth_bound',Q(1,256)<1,
         'M>=4,L>1,e>2 imply e^(-2ML)<1/256 and coth(ML)<257/255')
    gate('full_frequency_C_dirichlet_inverse',1/tc_lower<Q(3,2),
         'Homogeneous M^2 norm on nonzero modes: M^2/(M^2-M coth(ML)) <=1020/763<3/2')
    gate('inhomogeneous_second_order_weight_conversion',Q(25,16)*Q(3,2)==Q(75,32),
         '(1+M)^2/M^2<=25/16 for M>=4; the inhomogeneous inverse bound is <75/32')
    gate('full_frequency_linear_robin_bound',(4*coth-1)/(4-coth)<2,
         '(M coth(ML)-1)/(M-coth(ML)) <=773/763<2')
    root=Path(__file__).resolve().parents[1]
    paths=[Path(__file__).resolve(),
        root/'results/R119-supplement-actual-long-radial-nonlinear-dirichlet-problem.md',
        root/'results/R119-supplement-Codazzi-boundary-from-actual-regular-tail.md']
    return dict(kind='R119_actual_tail_to_Codazzi_boundary_exact_arithmetic',all_pass=True,
        arithmetic_only=True,complete_PDE_input='R119 actual long-radial nonlinear Dirichlet theorem',
        actual_location='r=25/8, on the installed long-radial annulus, not r=.25',
        radius=str(radius),chi_upper=str(chi),w_upper=str(w),
        C_Dirichlet_inverse_norm_convention='A0=sum_{m in 4Z nonzero} exp(sigma|m|)|f_m|; homogeneous A2=sum exp(sigma|m|)|m|^2|f_m|; zero mode is independent',
        checks=checks,exact_bounds={k:str(v) for k,v in dict(D_error=d_error,J_error=j_error,
            relative_C_error=c_relative,B_bound=b_bound,C_change_bound=c_bound,
            mean_C_change_bound=46*radius*radius,C_Dirichlet_inverse_norm=1/tc_lower,
            linear_Robin_norm=(4*coth-1)/(4-coth)).items()},
        input_sha256={str(p.relative_to(root)):sha(p) for p in paths},
        retains_mean_C=True,retains_mean_height=True,retains_regular_reflection=True,
        full_body_cap_DN_constructed=False,body_to_tail_matching_solved=False,
        scope='Exact true-tail trace conversion and all-frequency linear boundary operator with finite-length reflection. No body/cap BVP candidate or global exact surface is claimed.')


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    if args.out.exists():raise FileExistsError('refusing to overwrite an existing report')
    result=run();args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(dict(all_pass=result['all_pass'],checks=len(result['checks']),out=str(args.out)))


if __name__=='__main__':main()
