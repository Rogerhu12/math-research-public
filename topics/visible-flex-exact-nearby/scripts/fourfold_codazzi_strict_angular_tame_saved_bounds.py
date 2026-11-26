#!/usr/bin/env python3
"""NT: exact completed-scalar combinations for strict angular tame flow."""

from fractions import Fraction as F
import json
from fourfold_codazzi_compact_root_Cauchy_saved_bounds import (
    read, endpoints, SP_PATH, SP_SHA,
)
from fourfold_codazzi_compact_tame_Hessian_saved_bounds import decimal_upper


def main():
    execution=read(SP_PATH,SP_SHA)
    actual=execution["actual_scientific_receipt"]
    assert execution["complete"] and execution["actual_returncode"]==0
    assert actual["complete"] and actual["proved"] and actual["failure"] is None
    sp=actual["complete_strict_propagation_conclusion"]
    checks={}

    def lt(name,x,y):
        checks[name]=x<F(y)
        if not checks[name]:
            raise AssertionError(name)

    rho=F("1e-6")
    eR=F("5e-7")+F("1.03")*rho
    eL=F("1.31e-6")+F("1.03")*rho
    R,L=F("1.912")+eR,F("3.704")+eL
    deltaD=4*(2*F("1.912")*eR+eR*eR)
    oldD=endpoints(sp["complete_selected_scalar_maxima"]["complete_D"])[1]
    lt("complete nearby pointwise drift derivative",oldD+deltaD,F(".423"))
    lt("true whole derivative rate length",F(".423")*F(".234"),F(1,10))
    X0=F("1.03")*(F("6.407")+rho)
    X1=F("1.03")*(F("5.438")+rho)
    X2=F("1.03")*(128*F("5.438")+rho)
    lt("complete low weighted A0",X0,F("6.6"))
    lt("complete low weighted first angular derivative",X1,F("5.602"))
    lt("complete low weighted second angular derivative",X2,717)
    C1=12*R*L+(R*X2+L*L)+7*X2
    lt("entire first commutator remainder",C1,6500)
    # NR already proves these actual finite combinations from the same
    # saved positive matrices. Only their directed scalar conclusions
    # are consumed here; no chronological product is rerun.
    lt("complete reverse nonradial weak bound",F("2.163851")/(1-F(".000113")),F("2.166"))
    lt("complete forward nonradial weak bound",F("2.515703")/(1-F(".000131")),F("2.517"))
    qfactor=F("1.03")/F(".5338")
    limits={}
    for direction,U0,U1,k,Ctop,Clow in (
        ("reverse",F(176),F(174),F("2.166"),F(340),F(1120000)),
        ("forward",F(6),F("5.869"),F("2.517"),F(12),F(44500)),
    ):
        top=qfactor*U1
        lower=qfactor*(U0+6500*F(".234")*k*U0)
        lt(direction+" raw H1 high-data coefficient",top,Ctop)
        lt(direction+" raw H1 lower-data coefficient",lower,Clow)
        limits[direction]=dict(
            high_data_upper=decimal_upper(top,6),
            lower_data_upper=decimal_upper(lower,6),
            displayed_high=str(Ctop),displayed_lower=str(Clow))
    print(json.dumps({
        "all_passed":all(checks.values()),
        "exact_rational_comparisons":len(checks),
        "full_tail_low_A3_radius":"1e-6",
        "complete_first_commutator_coefficient_upper":decimal_upper(C1,6),
        "complete_first_angular_increment":limits,
        "high_background_factor_is_linear":True,
        "all_high_background_norms_required_small":False,
        "full_mean_and_original_jumps_retained":True,
        "root_or_positive_high_inverse_increment_claimed":False,
        "native_rows_or_old_products_evaluated":0,
    },indent=2,sort_keys=True))


if __name__=="__main__":
    main()
