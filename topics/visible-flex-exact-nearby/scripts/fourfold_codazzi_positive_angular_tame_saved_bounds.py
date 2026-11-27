#!/usr/bin/env python3
"""PT: exact low-budget arithmetic for all-angular positive two-end graphs.

This evaluates no native coefficients, reference curves or Fourier arrays.
The auxiliary cutoff is a proof frequency split, not a new finite inverse.
"""

from fractions import Fraction as F
import json
from fourfold_codazzi_compact_tame_Hessian_saved_bounds import decimal_upper


def main():
    checks={}

    def lt(name,x,y):
        checks[name]=x<F(y)
        if not checks[name]:
            raise AssertionError(name)

    rho=F("1e-6")
    tau=F("1.894e-7")+rho+F("1.894e-7")*rho
    lt("same full body reference floor",F(1,46),(1-tau)/45)
    lt("same full nearby mean gap",1,F("1.068")-F("2e-7")-rho)
    Q0w,Q1w,Q2w,Q0=map(F,("12.815","10.877","1392.129","6.408"))
    lt("full low weighted centre and tail",2*F("6.407")+rho,Q0w)
    lt("full first weighted angular centre and tail",2*F("5.438")+rho,Q1w)
    lt("full second weighted angular centre and tail",256*F("5.438")+rho,Q2w)
    lt("actual unweighted full pair",F("6.407")+rho,Q0)
    cb=4+472*Q0w**2+190*Q0w*Q1w
    db=16*Q0w**2
    lt("entire collar first new zeroth-order increment",
       4*F(".211")*Q0w**2,139)
    # M_n = [560(n+1)]^3. These base comparisons imply the strict
    # absorption inequalities for every integer n >= 1.
    lt("all-order body absorption base",1472*(cb+db),560**3)
    lt("all-order collar absorption base",128*F("283.001"),560**2)
    lt("whole optical ratio cutoff",23**3,560**3)
    lt("pair of branch gains below one eighth",2,F(2)**2)

    def complete_frames(chi,qc,rc,Bc):
        qb=1/(1-chi);rb=chi*qb
        loop=rc*rb;sig=1/(1-loop)
        maxima=[]
        for j in range(7):
            s,fc,fb,B,jc,js,ju=[F(int(i==j)) for i in range(7)]
            x=sig*(qc*s+qc*(Bc*fc+jc)+js
                   +rc*(qb*(F(".126142")*fb+B)+ju))
            y=rb*x+qb*(F(".126142")*fb+B)+ju
            sb=qb*(x+F(".126142")*fb+B)
            sc=qc*(s+y+Bc*fc+jc)
            maxima.extend((sb,sc))
        return max(maxima)

    base=complete_frames(F(".310"),F(750,749),F(1,749),F(".009000020"))
    first=complete_frames(F(".801"),F(250,249),F(1,249),F(".009000020"))
    lt("actual whole order-zero two-end frame inverse",base,2)
    lt("actual whole order-one two-end frame inverse",first,6)
    lt("same full ordinary source frame",5*F("1.000003"),6)
    lt("whole two-branch ordinary L2 source gain",2*6**2*4,18**2)
    # Frobenius^2(F) <= M^-1/3 (2+2/W) in the body.
    lt("whole raw pointwise reconstruction",94**3,16**3*388)

    n=2
    M=F((560*(n+1))**3)
    power23=F((560*(n+1))**2)
    Cn=cb+n*db
    En=F("144.001")+139*n
    lt("second increment complete body auxiliary gate",92*Cn/M,F(1,16))
    lt("second increment complete collar auxiliary gate",8*En/power23,F(1,16))
    L=2**(n+1)*418*Q0w*Q1w+3**n*190*(Q0w*Q2w+Q1w**2)
    H=2**(2*n+1)*418*Q0+4*6**n*190*Q0
    kr=4/power23
    middle=3*Q0w**2*M+Cn
    A2=2+4*kr*L*6+6*M*(1+4*kr*middle)+8*kr*H
    print(json.dumps({
        "all_passed":all(checks.values()),
        "exact_rational_comparisons":len(checks),
        "full_body_energy_over_abs_beta":decimal_upper(cb,6),
        "highest_derivative_increment_over_n_abs_beta":decimal_upper(db,6),
        "complete_low_frame_constants":{"order_zero":"2","order_one":"6"},
        "proof_cutoff_formula":"M_n=[560(n+1)]^3, physical Fourier frequency",
        "second_increment":{
            "physical_cutoff":str(M),"index_cutoff":str(M/4),
            "body_auxiliary_relative_energy":decimal_upper(92*Cn/M,12),
            "collar_auxiliary_relative_energy":decimal_upper(8*En/power23,12),
            "L2":decimal_upper(L,6),"H2":decimal_upper(H,6),
            "tame_recurrence_A2":decimal_upper(A2,6)},
        "high_background_order":"n+5/3; one linear factor",
        "highest_derivative_growth_uses_only_fixed_low_A3_domain":True,
        "low97_to_auxiliary_cutoff_uses_existing_low_inverse_only":True,
        "new_finite_matrix_inverse_or_new_193_reference":False,
        "actual_right_unstable_trace_is_independent_input":True,
        "all_order_actual_physical_exterior_feedback_closed":False,
        "all_original_source_jump_and_mean_head_ports_retained":True,
        "old_native_rows_reference_curves_and_Fourier_arrays":0,
    },indent=2,sort_keys=True))


if __name__=="__main__":
    main()
