#!/usr/bin/env python3
"""DT: exact low-ball arithmetic for the real all-angular exterior theorem.

All expressions are transformations of the completed QN long-module
budgets. No long solve, coefficient enclosure or old target is evaluated.
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

    epsilon,b=F(1,2**512),F(1,2**60)
    Rz,Rb=F("5e-10"),F("1e-11")

    def module(z,bh):
        rf=10*(z+bh)
        ff=rf+bh
        coupling=36*4096*ff
        jf=9/(1-coupling)
        jb=(epsilon+coupling)/(1-coupling)
        T=epsilon+4*16384*ff*jf
        U=epsilon+4*16384*ff*(1+jb)
        return dict(rf=rf,F=ff,kappa=coupling,T=T,C=(T-epsilon)/8,
                    U=U,V=(U-epsilon)/8)

    wide=module(Rz,Rb)
    lt("complete wider long boundary input",2*wide["F"],F(1,2**25))
    lt("complete wider long state",6*wide["F"],F(1,2**20))
    lt("complete wider curvature contraction",wide["kappa"],".001")
    lt("complete wider actual curvature self-map",
       9*Rz+epsilon*Rb+9*4096*wide["F"]**2,wide["rf"])
    Mz,Mb=F(".0035"),F(".00039")
    lt("whole wider Z operator and actual mean",wide["T"]+wide["C"],Mz)
    lt("whole wider height operator and actual mean",wide["U"]+wide["V"],Mb)
    small=module(F("4e-11"),b)
    for key,limit in (("T",".00024"),("C",".00003"),
                      ("U",".000027"),("V",".000003375")):
        lt("actual low "+key,small[key],limit)
    actual_t=F("4e-11")/Rz+b/Rb
    actual_g1=F("7e-11")/Rz+16*b/Rb
    lt("actual whole normalized parameter norm",actual_t,".081")
    lt("actual first background moment",actual_g1,".141")
    x=F(".243")
    lt("absolute full Taylor ratio",3*actual_t,x)
    lt("complete infinite Taylor denominator",x,1)
    qmin,lowT,lowU,inv=map(F,(".9999",".00024",".000027","1.001"))
    lt("actual nonmean curvature graph inverse",1/(qmin-lowT),inv)
    atz=6*Mz*F(".141")/(1-x)**2
    ath=6*Mb*F(".141")/(1-x)**2
    btz=6*Mz/(1-x)**2
    bth=6*Mb/(1-x)**2
    K1=(1+inv*atz)*inv+inv*(1+ath+btz*inv+bth)
    lt("first exact tame recurrence constant",K1,"2.1")

    # The explicit raw-to-physical high-background formula uses only the
    # already completed real endpoint chart bounds.
    endpoint=F("1e-9")
    P,Vs=F("1.480385e-11"),F("9.603792e-9")
    ml=F("5.84461145233")-endpoint
    e1=8*P+endpoint*(1+8*P)/ml
    jhi=1+e1
    m=7+endpoint
    t=1/F("5.84")
    wa=145*Vs+endpoint
    lt("real endpoint derivative-product denominator",t*wa,1)
    lt("fourfold real A0 from one physical derivative",F(22,7)**2/48,F(".46")**2)
    # n=1 illustrative coefficient in the general raw high-norm formula;
    # the sharper actual first moment above, not this coarse expression,
    # is used for every low-norm recurrence.
    raw1=F(".46")*jhi*3*2*m*m*t**4/Rz
    print(json.dumps({
        "all_passed":all(checks.values()),
        "exact_rational_comparisons":len(checks),
        "wider_zero_width_function_parameter_radii":{"Z":"5e-10","g":"1e-11"},
        "wider_complete_module":{k:decimal_upper(v,12) for k,v in wide.items()},
        "actual_normalized_low_background_upper":decimal_upper(actual_t,12),
        "actual_first_background_moment_upper":decimal_upper(actual_g1,12),
        "all_order_absolute_Taylor_ratio_upper":".243",
        "actual_physical_nonmean_L2_inverse_upper":"1.001",
        "first_tame_recurrence_constant":decimal_upper(K1,12),
        "raw_first_high_background_coefficient":decimal_upper(raw1,6),
        "higher_background":"Gamma_n = ||dtheta^n Z||A0/Rz + ||dtheta^n g||A0/Rb",
        "raw_high_background_order":"n+1, one linear factor; no positive analytic width",
        "highest_order_input_uses_actual_low_L2_operator":True,
        "all_physical_mean_and_independent_height_ports_retained":True,
        "full_raw_boundary_or_positive_all_order_inverse_claimed":False,
        "old_native_rows_long_solves_and_old_targets":0,
    },indent=2,sort_keys=True))


if __name__=="__main__":
    main()
