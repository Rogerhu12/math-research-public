"""The complete weighted high response of the low head in the true selected neighbourhood."""
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path


TOPIC=Path(__file__).resolve().parents[1]
FILES={
    "gh5":("notes/actual_GH_source_fees_ci/run-44736533396-1/actual-scientific-conclusion.json",49719,
        "e7766bc9e1a714456fa224b9dc69171ba119626bf62ffce2437d43dcd80924d6"),
    "gh5_run":("notes/actual_GH_source_fees_ci/run-44736533396-1/execution.json",54316,
        "2feec091d753aa856bbcbd6140f41c693972cf88b43d07232efea6c03f44629e"),
    "weighted":("notes/actual_GH_weighted_response_ci/run-44746534556-1/actual-scientific-conclusion.json",56554,
        "6e32b9ef4cafc6517670c9de76e3041ba35ee7454e70cf2ccc3aaef34916f36c"),
    "weighted_run":("notes/actual_GH_weighted_response_ci/run-44746534556-1/execution.json",57850,
        "d96bd1137d6e6f3f49ee5613402a9bd6b3763b096c3f4be9613437bddd1cbedc"),
    "WVC":("notes/continuous_centre_tracefree_residual_ci/run-43891414339-1/actual-scientific-conclusion.json",78627,
        "85fd5bc63c7cb558ef04ff9699f1f9be81dbd7e7b9638a2e0922818dc559cb88"),
    "outer":("notes/full_delta_positive_ci/run-43615531666-1-full-real-delta-positive/evidence/full-delta-complete-regular-Hs-outer-summary.json",
        23649,"769204e822787216c5aebd2cde30e73759fcf66d3bb1d6d1d76d2381bad6cae6"),
    "SPN":("results/R149-supplement-true-positive-seven-port-graph-around-the-selected-member.md",9590,
        "83c787877cca06ea22b575da1d50c24a67a054e056abdabe94d7a66232549092"),
    "NBE":("results/R149-supplement-nonlinear-background-negative-ordinary-response.md",7654,
        "35b2075696ece5529e649bc373d81af4c6551cd1d76dea0aad57e5558649a2d0"),
    "OHR":("results/R149-supplement-strong-physical-outer-residuals-and-complete-independent-right-hand-sides.md",7715,
        "37f9e72dbdad3dbf19a2d6465424657991d2eb0f06320309bd7ce4dd0d4af387"),
    "QN":("results/R144-supplement-actual-whole-positive-high-inverse-in-a-full-tail-neighbourhood.md",32805,
        "1fe88442bb35d0280a54dc416014f59773f1777a1b74998eb9513052b2f5a15e"),
    "PH":("results/R144-supplement-actual-positive-high-graph-for-compact-centres.md",24110,
        "634706af859ac5c793a82e50cc93bf2044bb47d92c89310f77bde2d08a802a67"),
    "weighted_formula":("scripts/fourfold_codazzi_actual_GH_radially_weighted_math.py",17375,
        "6bb32619998f8cdeb428a88faf021afab6fe92409a216bee9ebca439ac7cfa30"),
    "parser":("scripts/fourfold_codazzi_negative_ordinary_response_saved_bounds.py",10330,
        "88df151b7ecc9c22bff382cd96e647ba2ea1010baa6332b5dcc8a88baf9ea4b9"),
}


def require(ok,message):
    if not ok:
        raise ValueError(message)


def main():
    docs={}
    for k,(name,size,digest) in FILES.items():
        raw=(TOPIC/name).read_bytes()
        require(len(raw)==size and sha256(raw).hexdigest()==digest,"whole input "+k)
        if name.endswith(".json"):
            docs[k]=json.loads(raw)
    from fourfold_codazzi_negative_ordinary_response_saved_bounds import endpoints
    S,W,base,out=(docs[k] for k in ("gh5","weighted","WVC","outer"))
    for k,run in (("gh5","44736533396"),("weighted","44746534556")):
        x,y=docs[k],docs[k+"_run"]
        require(x["complete"] and x["proved"] and x["failure"] is None and x["actual_returncode"]==0
                and y["scientific_complete"] and y["actual_child_returncode"]==0
                and str(x["run_id"])==str(y["run_id"])==run and str(x["run_attempt"])==str(y["run_attempt"])=="1"
                and y["scientific_files"]==[dict(bytes=FILES[k][1],path="topics/visible-flex-exact-nearby/"+FILES[k][0],
                    sha256=FILES[k][2])] and x["saved_record_count"]==5, "original whole successful result "+k)
    w=W["weighted_response"]
    require(S["source_comparison"]["complete_five_source_rates_proved"]
            and w["complete_actual_head_to_high_weighted_response_proved"]
            and w["whole_actual_GH_family_in_original_resolvent"] and w["same_full_family_mean_source_column_retained"]
            and w["original_kernel_rows_consumed"]==4650 and w["exact_common_refinement_cells"]==4802
            and w["both_orthogonal_branches_and_disjoint_input_half_intervals_used"]
            and W["reference_identity"]==S["reference_identity"]==w["reference_identity"]
            and W["scientific_modules"][:7]==S["scientific_modules"][:7]
            and base["complete"] and base["proved"] and base["actual_returncode"]==0
            and base["parameters"]["reference_q_floor"]=="1/8"
            and W["reference_identity"]["complete_original_WVC_file"]["sha256"]==FILES["WVC"][2],
            "same whole original graph and every physical head weight")
    require(out["complete"] and out["full_Hone_sixth_Riccati_graph_proved"]
            and len(out["gates"])==25 and all(g["passed"] for g in out["gates"]),
            "actual original strong low and independent height exterior columns")
    checks={}
    def test(name,left,right):
        require(left<right,name)
        checks[name]=True
    rho=F("1e-7")
    W96=F("7.269")
    test("true_finite_head_Hthird",1+384**2,W96**6)
    A,D=33,28
    coefficient=8*(6*W96*((2*A+rho)*(1+F(384,4))+2*(A+F(D,4))+
                                  2*A*F(5,4)+2*rho*F(5,4))+14)
    test("all_frequencies_nearby_BHL_on_true_193_head",coefficient,2_300_000)
    up=lambda obj:endpoints(obj)[1]
    rates=S["new_records"]
    Cc=up(rates["complete_centre_BHL_Hthird_collar_upper"])+up(rates["complete_family_BHL_Hthird_collar_upper"])
    core=Cc+2_300_000*rho
    test("actual_perturbed_whole_collar_source",core,F("9.76"))
    tau,sigma=F("1e-7"),F("2e-7")
    lam=F("1.000001")
    test("new_both_direction_weighted_source_square_resolvents",1,lam**2*(1-tau)*(1-2*sigma))
    wr=W["new_records"]
    weighted=lam*up(wr["actual_GH_body_weighted_unperturbed_source_upper"])+F(".126142")*2_300_000*rho
    test("whole_perturbed_weighted_body_functional",weighted,F("8.161"))
    qc,rc,Bc,qb,rb=F(750,749),F(1,749),F(".009"),F(100,69),F(31,69)
    sig=1/(1-rc*rb)
    body=[]
    collar=[]
    for fc,fb in ((Bc*core,0),(0,weighted)):
        x=sig*(qc*fc+rc*qb*fb)
        y=rb*x+qb*fb
        collar.append(qc*(y+fc))  # with zero external data this equals root outgoing
        body.append(qb*(x+fb))
    for name,row in (("body",body),("collar_and_root",collar)):
        test("true_entire_weighted_"+name+"_head_row",sum(v*v for v in row),F("11.9")**2)
    test("true_raw_high_response_to_weighted_head",F("11.9")**2*(9*F("9e-6")+F("2.518")**2),30**2)
    test("true_high_outer_readout_from_head",F(5,388)*F("11.9"),F(".154"))
    test("strong_terminal_change_of_head_units",1+384**2,F("384.002")**2)
    fac=F("25.95")*F("9.00002")+F("2.86e-6")
    test("neighbourhood_full_negative_cost_of_weighted_low",fac*F("11.9"),2780)
    test("neighbourhood_full_negative_cost_of_charted_low_terminal",fac*F("1.453")*F(".001")*F("384.002"),131)
    test("neighbourhood_full_negative_cost_of_independent_height",fac*F("1.453")*F(".004"),F("1.36"))
    old_fac=F("25.95")*F("9.00002")+F("2.85e-6")
    old_frame=up(wr["actual_GH_weighted_root_outgoing_Z_from_complete_head_upper"])
    ext=out["bounds"]
    test("selected_full_negative_cost_of_weighted_low",old_fac*old_frame,2732)
    test("selected_full_negative_cost_of_charted_low_terminal",old_fac*F("1.439")*
         up(ext["complete_low_to_high_outer_source"])*F("384.002"),F("3.03"))
    test("selected_full_negative_cost_of_height",old_fac*F("1.439")*up(ext["independent_fB_outer_source"]),F(".0096"))
    test("continuous_neighbourhood_sufficient_ordinary_L2_gate",F("25.95")*F(".000020")+2780*F("1.2e-6")+
         131*F("4e-6")+F("1.774e-5")+5530*rho,F(".005"))
    print(json.dumps(dict(proved=True,checks=checks,whole_inputs={k:v[2] for k,v in FILES.items()},
        true_selected_nearby_head_rates=dict(root_collar_body_Z="11.9",raw_high="30",outer_even_Hminus5over6=".154"),
        selected_finite_response_costs=["2732","3.03",".0096"],nearby_finite_response_costs=["2780","131","1.36"],
        complete_external_rows_and_means_retained=True,actual_global_port_sizes_verified=False,
        full_negative_nonlinear_target_proved=False,old_scientific_target_calls=0),sort_keys=True))


if __name__=="__main__":
    main()
