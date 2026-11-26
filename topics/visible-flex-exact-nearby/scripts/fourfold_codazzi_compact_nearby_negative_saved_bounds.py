#!/usr/bin/env python3
"""NR: complete nearby strict/root constants from saved small conclusions.

Only rational combinations of already completed whole bounds are formed.
No native coefficient row, reference flow, growth integral or target runs.
"""

from fractions import Fraction as F
import json
from fourfold_codazzi_compact_root_Cauchy_saved_bounds import (
    read, endpoints, ROOT_PATH, ROOT_SHA, SP_PATH, SP_SHA,
)
from fourfold_codazzi_compact_positive_high_saved_bounds import strict_sqrt_upper
from fourfold_codazzi_compact_tame_Hessian_saved_bounds import decimal_upper


def up(record):
    return endpoints(record)[1]


def low(record):
    return endpoints(record)[0]


def frob(matrix):
    return strict_sqrt_upper(sum(x*x for row in matrix for x in row), 12)


def scale4(matrix):
    return [[matrix[0][0],4*matrix[0][1]],
            [matrix[1][0]/4,matrix[1][1]]]


def main():
    root=read(ROOT_PATH,ROOT_SHA)
    execution=read(SP_PATH,SP_SHA)
    assert root["complete"] and root["failure"] is None
    assert root["same_full_real_family_root_Cauchy_estimate_proved"]
    assert execution["complete"] and execution["actual_returncode"]==0
    actual=execution["actual_scientific_receipt"]
    assert actual["complete"] and actual["proved"] and actual["failure"] is None
    sp=actual["complete_strict_propagation_conclusion"]
    readout=actual["complete_endpoint_readout_conclusion"]
    assert sp["all_shorter_ordered_products_and_source_insertions_included"]
    assert sp["complete_mean_coordinates"]==2
    checks={}

    def lt(name,x,y):
        checks[name]=x<F(y)
        if not checks[name]:
            raise AssertionError(name)

    rho=F("1e-6")
    cut=F(sp["exact_interval"][1])
    lt("true strict length",cut,F(".234"))
    lt("same strict lower q",F(".5338"),low(sp["new_entire_q_lower"]))
    lt("same strict upper q",up(sp["new_entire_q_upper"]),F("1.03"))
    R,L,b,g=map(F,("1.912","3.704","2","7"))
    eR,eL=F("5e-7")+F("1.03")*rho,F("1.31e-6")+F("1.03")*rho
    ss=2*R*eR+eR*eR
    pp=R*eL+L*eR+eR*eL
    tt=2*L*eL+eL*eL
    dD,drate=4*ss,8*ss
    da,db,dny,dnz,dng=12*pp,8*pp,4*pp+tt,pp,7*eL
    E=[[drate+dD+(da+dny)/4,dD/2+db/16+(dnz+dng)/4],
       [da+dny,drate+dnz]]
    Ew,Es=frob(E),frob(scale4(E))
    lt("complete weak comparison increment",Ew,F(".000224"))
    lt("complete strong comparison increment",Es,F(".000167"))
    strict={}
    for direction in ("reverse","forward"):
        p=[[up(v) for v in row] for row in sp[direction+"_nonradial_product"]]
        u=[[up(v) for v in row] for row in sp[direction+"_complete_matrix"]]
        kw,ks=frob(p),frob(scale4(p))
        tw,ts=kw*Ew*F(".234"),ks*Es*F(".234")
        lt(direction+" weak feedback",tw,F(".001"))
        lt(direction+" strong feedback",ts,F(".001"))
        uw=up(sp[direction+"_complete_operator_upper"])/(1-tw)
        us=frob(scale4(u))/(1-ts)
        strict[direction]=dict(kw=kw,ks=ks,tw=tw,ts=ts,weak=uw,strong=us)

    # The new actual waist mean is not reset to the exact-centre value.
    waist=readout["waist_complete_radial_factors"]
    a0=low(waist["physical_radius_lower"])
    n0lo=1/(1+rho/a0)**2
    n0hi=1/(1-rho/a0)**2
    lt("nearby actual waist density lower",F(".999998"),n0lo)
    lt("nearby actual waist density upper",n0hi,F("1.000002"))
    lt("nearby waist factor fits saved positive budget",n0hi,
       low(waist["density_radial_factor_upper"]))
    lt("waist square root lower",F(".9616")**2,low(waist["q_lower"]))
    lt("waist square root upper",up(waist["q_upper"]),F(".962")**2)
    source=up(readout["complete_strict_Hminus1_source_injection_upper"])
    c1=up(readout["strict_L1_Hminus1_source_to_waist_density_gain"])/(1-strict["reverse"]["tw"])
    c2=up(readout["strict_L2_Hminus1_source_to_waist_density_gain"])/(1-strict["reverse"]["tw"])

    # Original compact root increments are complete inputs of RTC. The
    # unknown tail alone is estimated by full-lag kernels, never by 768.
    Kq,qmax,W,CI=map(F,("1.049","1.025","1.432","1.031"))
    U,V,U1,V1=map(F,(".629","6.407","5.438","5.438"))
    qa43=F("34.141")
    lt("full regular root speed",
       F("1.253802")+7*(F("2e-7")+F("3.861e-18")+rho),F("1.3"))
    dqweighted=b*Kq*(2*qa43*rho+rho*rho)
    dqplain=b*Kq*(2*F("6.407")*rho+rho*rho)
    drift_diag=dqplain/2+F(4,3)*dqweighted+4*dqweighted
    l0=2*b*((U+V)*rho+rho*rho)
    l1=2*b*((U1+V+U+V1)*rho+2*rho*rho)
    aa,daa=U1+V1,2*rho
    bb,dbb=W*(U+U1)+Kq*(V+V1),2*(W+Kq)*rho
    pm=8*b*CI*(aa*dbb+bb*daa+daa*dbb)
    nm=4*g*(Kq+1)*rho
    root_tail_m=drift_diag+4*(qmax+W)*(l0+l1)+pm+nm
    cc,dcc=W*U+Kq*V,(W+Kq)*rho
    dd,ddd=F(".41")*(U1+128*U1)+V1/4,(F(".82")+F(1,4))*rho
    p0=8*b*(cc*ddd+dd*dcc+dcc*ddd)
    n0=4*g*(2*Kq+1)*rho
    root_tail_0=drift_diag+4*(qmax+W)*l0+p0+n0
    lt("full-tail negative root growth increment",root_tail_m,F(".0035"))
    lt("full-tail strong root growth increment",root_tail_0,F(".0135"))
    delta_m=F(".003253")+root_tail_m
    delta_0=F(".006290")+root_tail_0
    lt("total nearby negative root growth",delta_m,F(".0068"))
    lt("total nearby strong root growth",delta_0,F(".0200"))
    delta_m,delta_0=F(".0068"),F(".0200")
    left,right=map(F,root["exact_root_interval"])
    width=right-left
    assert width==F("9e-13")
    cases={c["exact_radius"]:c for c in root["cases"]}
    tables={}
    for radius,case in cases.items():
        assert case["passed"]
        length=F(radius)+width
        den0,denm=1-delta_0*length,1-delta_m*length
        lt(radius+" strong denominator",F(0),den0)
        lt(radius+" weak denominator",F(0),denm)
        bounds=case["bounds"]
        tables[radius]=dict(
            strong=up(bounds["H0"]["full_root_to_state"])/den0,
            weak=up(bounds["Hminus1"]["full_root_to_state"])/denm,
            primitive=up(bounds["primitive_after_Hminus1"]["full_root_bracket_to_L2"])/denm,
        )

    # Actual fixed cut and every original containing one-sided row.
    cutrad=readout["cut_complete_radial_factors"]
    em=F("2.001e-7")+rho
    mlo=F("1.117244")
    nglo=F(".958234592")/(1+em/mlo)**2
    nghi=F(".962284474")/(1-em/mlo)**2
    lt("actual nearby cut density lower",F(".958232"),nglo)
    lt("actual nearby cut density upper",nghi,F(".962287"))
    lt("cut T gap",1,F("1.224")**2*low(cutrad["q_lower"]))
    lt("actual nearby cut density T",nghi*F("1.224"),F("1.178"))
    denm=1-delta_m*(F("1/200")+width)
    den0=1-delta_0*(F("1/200")+width)
    selected=cases["1/200"]["bounds"]
    cutroot=F("1.178")*up(selected["primitive_after_Hminus1"]["full_root_bracket_to_L2"])/denm
    cutsource=F("1.178")*up(selected["primitive_after_Hminus1"]["ordinary_L2_radial_source_to_L2"])/denm
    weak_root_waist=up(readout["root_or_affine_jump_to_waist_density_gain"])/((1-strict["reverse"]["tw"])*denm)
    weak_source_waist=up(readout["ordinary_root_window_source_to_waist_density_gain"])/((1-strict["reverse"]["tw"])*denm)
    weak_forward=F("1.178")*strict["forward"]["weak"]*F(".962")/n0lo
    weak_forward_source=F("1.178")*strict["forward"]["weak"]*source
    raw_strict_reverse=strict["reverse"]["strong"]*F("1.03")/F(".5338")
    raw_strict_forward=strict["forward"]["strong"]*F("1.03")/F(".5338")
    raw_weak_reverse=CI*strict["reverse"]["weak"]*F("1.03")/F(".5338")
    raw_weak_forward=CI*strict["forward"]["weak"]*F("1.03")/F(".5338")
    for name,val,limit in (
        ("complete strong reverse common window",raw_strict_reverse,347),
        ("complete weak reverse common window",raw_weak_reverse,347),
        ("complete strong forward common window",raw_strict_forward,12),
        ("complete weak forward common window",raw_weak_forward,12)):
        lt(name,val,limit)
    out0=n0hi/F(".9616")
    strong_root_waist=out0*strict["reverse"]["strong"]*tables["1/200"]["strong"]
    root_sqrt=strict_sqrt_upper(F("1/200"),12)
    strict_sqrt=strict_sqrt_upper(cut,12)
    strong_source_waist=strong_root_waist*root_sqrt
    strong_strict_c1=out0*strict["reverse"]["strong"]*F("1.03")
    strong_strict_c2=strong_strict_c1*strict_sqrt

    def dec(obj):
        if isinstance(obj,F):
            return decimal_upper(obj,6)
        if isinstance(obj,dict):
            return {k:dec(v) for k,v in obj.items()}
        if isinstance(obj,list):
            return [dec(v) for v in obj]
        return obj

    print(json.dumps(dec({
        "all_passed":all(checks.values()),
        "exact_rational_comparisons":len(checks),
        "full_tail_unweighted_A3_radius":"1e-6",
        "strict_comparison_increment_weak":Ew,
        "strict_comparison_increment_strong":Es,
        "strict_complete":strict,
        "full_original_root_radii":tables,
        "nearby_cut_density_bounds":[".958232",".962287"],
        "nearby_waist_density_bounds":[".999998","1.000002"],
        "weak_complete_waist_gains":{
            "root_or_root_jump":weak_root_waist,
            "root_ordinary_L2":weak_source_waist,
            "strict_L1_or_jump":c1,
            "strict_L2":c2,
        },
        "strong_complete_waist_L2_density_gains":{
            "root_or_root_jump":strong_root_waist,
            "root_ordinary_L2":strong_source_waist,
            "strict_L1_or_jump":strong_strict_c1,
            "strict_L2":strong_strict_c2,
        },
        "strict_raw_L2_to_L2_uniform":{"reverse":raw_strict_reverse,"forward":raw_strict_forward},
        "strict_raw_Hminus1_to_Hminus1_uniform":{"reverse":raw_weak_reverse,"forward":raw_weak_forward},
        "strict_same_flow_all_Hs_minus1_to_zero":{"reverse":347,"forward":12},
        "true_cut_weak_gains":{
            "root_or_root_jump":cutroot,"root_ordinary_L2":cutsource,
            "forward_from_waist_density":weak_forward,
            "forward_L1_source_or_jump":weak_forward_source,
        },
        "root_tail_growth":{"strong":root_tail_0,"weak":root_tail_m},
        "all_means_and_affine_jumps_retained":True,
        "old_H1_flow_used_for_L2":False,
        "old_finite_lag_assumed_for_unknown_tail":False,
        "normalizer_radial_jets_or_full_return_proved":False,
        "native_rows_integrals_or_scientific_targets_evaluated":0,
    }),indent=2,sort_keys=True))


if __name__=="__main__":
    main()
