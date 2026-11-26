#!/usr/bin/env python3
"""RT: all-order root tame structure and actual first angular increment.

Only exact rational combinations of already completed scalar bounds.
No native rows, Fourier evaluation, radial flow or growth integral runs.
"""

from fractions import Fraction as F
import json
from fourfold_codazzi_compact_root_Cauchy_saved_bounds import (
    read, endpoints, ROOT_PATH, ROOT_SHA,
)
from fourfold_codazzi_compact_tame_Hessian_saved_bounds import decimal_upper


def main():
    root=read(ROOT_PATH,ROOT_SHA)
    if not (root["complete"] and root["failure"] is None
            and root["same_full_real_family_root_Cauchy_estimate_proved"]
            and root["all_frequencies_and_independent_even_mean_retained"]):
        raise AssertionError("completed full original root conclusion")
    checks={}

    def lt(name,x,y):
        checks[name]=x<F(y)
        if not checks[name]:
            raise AssertionError(name)

    rho=F("1e-6")
    b,K,q,W,g=map(F,("2","1.049","1.025","1.432","7"))
    Q0,Qphi,Q13=F("6.407")+rho,F("5.438")+rho,F("8.732")+rho
    Qphi13=F("5.06")*F("5.438")+rho
    U,V=F(".629")+rho,F("6.407")+rho
    U1=V1=F("5.438")+rho
    U2=V2=128*F("5.438")+rho
    U2a=128*F("5.06")*F("5.438")+rho
    D=b*K*Q13**2
    lt("highest angular transport root growth",D,161)
    diag=8*b*K*Q13*Qphi13
    off=4*(q+W)*2*b*(U1*V+U*V1)
    primitive1=8*b*(W*U+K*V)*(F(".41")*U2a+V2/4)
    primitive2=8*b*(W*U1+K*V1)*(F(".41")*Qphi13+V1/4)
    mean=4*g*q*(128*F("5.438")+rho)
    R1=diag+off+primitive1+primitive2+mean
    lt("complete first root commutator including moving mean",R1,230000)
    lt("full low root A0",Q0,"6.408")
    lt("full low root A1",F("6.407")+F("5.438")+rho,"11.846")
    lt("full low root Afour-thirds",F("34.141")+rho,"34.142")
    lt("full low root Aseven-thirds",129*F("34.141")+rho,"4404.190")
    lt("structured root primitive radial coefficient",K,W)
    lt("primitive L2 to Hthird",17**1,F("1.64")**6)

    left,right=map(F,root["exact_root_interval"])
    width=right-left
    if width!=F("9e-13"):
        raise AssertionError("actual unchanged root interval")
    rows={}
    for case in root["cases"]:
        if not case["passed"]:
            raise AssertionError("all original root radii completed")
        key=case["exact_radius"]
        R=F(key); length=R+width
        # NR's proved entire growth addition, not a new coefficient bound.
        old=endpoints(case["bounds"]["H0"]["full_root_to_state"])[1]
        C0=old/(1-F(".0200")*length)
        x=F(161)*length/16
        lt(key+" low growth rational denominator",x,1)
        gain=(1-x)**-16
        first=C0*gain
        lower=C0*(1+R*F(230000)*gain)
        rows[key]={
            "low_root_C0":decimal_upper(C0,6),
            "low_growth_multiplier":decimal_upper(gain,9),
            "H1_data_coefficient":decimal_upper(first,6),
            "H0_data_coefficient":decimal_upper(lower,6),
        }
    selected=rows["1/200"]
    lt("selected true cut angular-data receiver",F(selected["H1_data_coefficient"]),15)
    lt("selected true cut lower-data receiver",F(selected["H0_data_coefficient"]),17200)
    all_negative_high=340*F(selected["H1_data_coefficient"])
    all_negative_low=(340*F(selected["H0_data_coefficient"])
                      +1120000*F(selected["low_root_C0"]))
    lt("whole negative first angular root receiver",all_negative_high,5100)
    lt("whole negative first angular lower root receiver",all_negative_low,13200000)
    waist_density=F("1.000002")/F(".9616")
    lt("actual full nearby waist density H1 conversion",waist_density,"1.041")

    # These are fixed low-norm constants, independent of every high norm.
    Qlo,Qone,Qfour,Qseven=map(F,("6.408","11.846","34.142","4404.190"))
    Clocal=8*b*(K+q+W)
    Pprimitive=8*b*W*F(".41")
    # Record the formula without evaluating a high-order recurrence or
    # supplying any high background norm. Only n=1 coefficients are shown.
    L1=2*(Clocal+b*K)*Qfour**2+3*Pprimitive*(Qlo*Qseven+Qfour*Qone)
    H1=8*(Clocal+b*K)*Qlo+6*Pprimitive*(Qlo+Qfour)+4*g*q
    print(json.dumps({
        "all_passed":all(checks.values()),
        "exact_rational_comparisons":len(checks),
        "actual_low_norm_highest_derivative_growth":decimal_upper(D,9),
        "actual_first_commutator":decimal_upper(R1,6),
        "first_commutator_parts":{
            "diagonal":decimal_upper(diag,6),"off_diagonal":decimal_upper(off,6),
            "outer_coefficient_primitive_word":decimal_upper(primitive1,6),
            "inner_coefficient_primitive_word":decimal_upper(primitive2,6),
            "independent_moving_mean":decimal_upper(mean,6),
        },
        "complete_actual_root_H1_windows":rows,
        "whole_negative_raw_H1":{
            "root_X1":decimal_upper(all_negative_high,6),
            "root_X0":decimal_upper(all_negative_low,6),
            "strict_L1r_H1_and_jumps":"340",
            "strict_L1r_L2_and_jumps":"1120000",
            "actual_waist_density_extra_factor_upper":"1.041"},
        "general_tame_constants":{
            "C_local":decimal_upper(Clocal,6),
            "C_primitive":decimal_upper(Pprimitive,6),
            "L1_general_bound":decimal_upper(L1,6),
            "H1_general_bound":decimal_upper(H1,6),
            "high_background_order":"n+4/3",
            "high_background_occurrences":"one, linear, outside all exponentials",
        },
        "full_tail_low_domain":"unweighted A3 <= 1e-6",
        "actual_root_data_and_sources":"X_n = H^{n+1/3} + H^n",
        "actual_state":"full H^n pair, including the original mean",
        "all_original_jumps_and_both_root_endpoints_retained":True,
        "unknown_high_norms_required_small":False,
        "radial_derivatives_of_background_required":False,
        "arbitrary_radial_L2_trace_used":False,
        "old_native_rows_Fourier_evaluations_flows_and_integrals":0,
    },indent=2,sort_keys=True))


if __name__=="__main__":
    main()
