"""Exact strict consequences of the original entire same-window parameter source."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import re

INPUTS={
 "NW":("notes/negative_nu_waist_ci/run-45781137624-1/actual-negative-nu-waist.json","1a06d01060a63eac98aeaa330f130a8ee766ab5ac878634e637f9cea30e1cb70"),
 "NWproof":("results/R147-supplement-same-window-selected-nu-source-to-complete-waist.md","f122a8492662da32aafc7a64f7a5930782a298b9dda0d42b1b80caf7fe98fad5"),
 "NHT":("results/R149-supplement-selected-complete-high-Newton-and-nu-from-the-Z-tail.md","6b4202ede35ed025bb52cd5abcb5a60089353436866a6e32dfac54f0ee5140d9"),
 "NRO":("results/R149-supplement-ordinary-negative-response-from-the-strong-positive-root.md","fb1e034f04c79c4a893cdd1407b7a590959f5383dddb1ea786abb34366dfa91d"),
 "ASQ22":("results/R149-supplement-small-true-Theta-reception-of-the-negative-parameter-defect.md","6a3568c62ba7bfff45d2a5509f2721d7581c312602d47afc47f7ab3825f218ee"),
 "ASQ24":("results/R149-supplement-physical-Sobolev-rotation-selection-and-normalized-smooth-family.md","26669f292a88613d3a6de3330c337436571c4c8606590ec5418e11f4075d2c17")}


def upper(record):
    mat=re.fullmatch(r"\[([^ \]]+) \+/- ([^\]]+)\]",record["ball"])
    if not mat:
        raise ValueError("entire original Arb ball")
    return Q(mat[1])+Q(mat[2])


def main():
    d=Path(__file__).resolve().parent.parent
    evidence={}
    for key,(p,s) in INPUTS.items():
        raw=(d/p).read_bytes()
        if hashlib.sha256(raw).hexdigest()!=s:
            raise ValueError(key)
        evidence[key]={"sha256":s,"bytes":len(raw)}
        if key=="NW":
            w=json.loads(raw)
    assert w["actual_returncode"]==0 and w["complete"] is w["proved"] is True and w["failure"] is None
    assert w["identity"]["run_id"]=="45781137624" and len(w["completed_targets"])==w["saved_record_count"]==4
    x=Q(w["selected_member_identity"]["absolute_delta_upper"])
    d=Q(w["parameters"]["delta_budget_radius"])
    f0=upper(w["copied_prior_scalar_records"]["source_zero_same_fixed_negative_full"])
    F=upper(w["new_records"]["selected_negative_source_from_same_fixed_window_upper"])
    diff=upper(w["copied_prior_scalar_records"]["complete_selected_difference_at_radius_d"])
    a=x*(f0+(x/d)*diff/2)
    h=x*Q("1.254870e-9")
    R,c=Q(1,200),Q(2333968743003,10**13)
    U,C,W,A=map(Q,["8.22","6.531704","7.269","25.943"])
    b,p=Q("13.405"),Q("27.882")
    sa,sp=Q("1.835"),Q("3.797")
    checks={
        "same_real_interval":x<d==Q("1e-10"),
        "whole_base_source":f0<Q("3.125876e-7"),
        "whole_difference_row":diff<Q("1.061687e-6"),
        "whole_endpoint_source":F<Q("1.307204e-6"),
        "integrated_ordinary_source":a<Q("7.59e-17"),
        "integrated_strong_high_source":h<Q("1.176e-19"),
        "ordinary_body_row":(c*U)**2/2+A*A*R*W*W<b*b,
        "high_body_row":A*A*R<sa*sa,
        "ordinary_endpoint_row":U*U*(c+C*C*R*W*W)<p*p,
        "high_endpoint_row":U*U*C*C*R<sp*sp,
        "actual_negative_body":b*a+sa*h<Q("1.019e-15"),
        "actual_negative_endpoint":p*a+sp*h<Q("2.12e-15"),
        "true_phase_value_transfer":Q("5.38")*Q("1.019e-15")<Q("5.49e-15"),
        "true_full_Theta_transfer":Q(".456")*Q("2.12e-15")<Q("9.67e-16"),
        "true_recovered_Theta_transfer":Q(".457")*Q("2.12e-15")<Q("9.70e-16"),
        "independent_amplitude_mean_transfer":Q(".681")*Q("2.12e-15")<Q("1.45e-15")}
    if not all(checks.values()):
        raise ValueError([k for k,v in checks.items() if not v])
    print(json.dumps({"complete":True,"whole":evidence,"new_exact_rational_checks":checks,
        "old_source_or_flow_targets_called":0},sort_keys=True,separators=(",",":")))


if __name__=="__main__":
    main()
