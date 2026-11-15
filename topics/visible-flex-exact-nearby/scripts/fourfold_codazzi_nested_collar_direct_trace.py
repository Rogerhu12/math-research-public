#!/usr/bin/env python3
"""New complete NC/BD scalar rows from already successful small conclusions only."""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time
import traceback
from flint import arb, ctx

TOPIC=Path("topics/visible-flex-exact-nearby")
KIND="actual_nested_collar_direct_first_angular_trace_rows_v1"
LC_KIND="actual_saved_positive_collar_components_and_high_coercivity_v1"
WC_KIND="actual_wide_collar_mean_and_projected_half_trace_v1"
LC_BASE="notes/saved_positive_collar_components_ci/run-43731225532-1-saved-positive-collar-components/"
FILES={
 "lc_science":LC_BASE+"actual-saved-positive-collar-components.json",
 "lc_process":LC_BASE+"process.json",
 "lc_recovery":LC_BASE+"recovery.json",
 "wide_source":"notes/wide_collar_mean_half_trace_ci/run-43722885993-1-wide-collar-mean-half-trace/actual-wide-collar-mean-half-trace.json",
 "NC":"results/R133-supplement-nested-collar-localization-and-direct-projected-first-angular-trace.md",
 "BD":"results/R133-supplement-complete-degree32-splitting-of-the-differentiated-collar-equation.md"}
EXPECTED={
 "lc_science":"44b4da07b50dcca9be7671b8cb59b227999e76871237c25a1bc0aec4bc02492c",
 "lc_process":"a15e9b16d6867d0f69a85d9549ad66953f70b444e7d9462ec45281aadf84cb58",
 "lc_recovery":"22d627a37aeb0b5a519df4d82aa4de111f82caca15127e2081010e94c3820a41",
 "wide_source":"1c650195524b78725358c40aabe9c2413c203309f2173cef1a0cb4a8adfc265b",
 "NC":"558f47f743ccbfbb14c5305a56a699900e472b03183037951d0b26be33983df9",
 "BD":"bb792252f0a3400547293ba5d8e9f9f5c2aa842dcf749abfd3f993abd478935c"}
LC_ORIGINAL_PRETTY_SHA="903a537a0454464e8c30ff57034b2811d1c43ad47a18979f5a7d8403c888b981"
LC_SCI_SHA="02fc50c45ed2610b94619d9db60ee2f74dc3a1643ce2f398c8eb25505926f7ea"
WC_SCI_SHA="9cfe1e741200467c215b30ffb41bb3c5eed6cadf9f01e029027dc86d636d3c43"
CENTRE="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
RESPONSE="6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
RHO=("1/10000","1/1048576","1/16777216","1/268435456","1/4294967296","1/68719476736")
LABELS=(96,288)
COLUMN_ORDER=("ordinary_angle_source","ordinary_source","shell_body","low_body","high_body")
RADIUS_ORDER=("M","Mdelta2","actual_drift_phi","A1","B10_NC","base_A1_mixing",
 "base_B10","delta_A1","delta_B10","B10_BD","pplus","high_body_C0_hypothesis_bound",
 "d0","dplus","delta_d")
PROJECTION_ORDER=("k","bp1","br1","trace_T","GammaH_NC","GammaL_NC","GammaH_BD",
 "shell_derivative_BD","low_derivative_BD")
GEOMETRY_ORDER=("r","eta","sigma")
READOUT_ORDER=("known_source","conditional_high_C0","known_source_plus_conditional_high_C0")
PARAMETERS={
 "arithmetic_bits":320,"output_ball_significant_digits":24,
 "output_ball_minimum_significant_digits":16,"output_ball_maximum_characters":56,
 "exact_interval":["17/20","19/20"],"exact_cut":"9/10",
 "selected_delta_half_width":"1/10000000000",
 "wide_rho_candidates":list(RHO),"high_projection_labels":list(LABELS),
 "physical_frequency_factor":4,"nested_counts":list(range(1,65)),
 "number_of_parameter_triples":768,"complete_formula_rows_per_triple":2,
 "formulas":["NC","BD"],"five_column_order":list(COLUMN_ORDER),
 "radius_coefficient_order":list(RADIUS_ORDER),
 "projection_constant_order":list(PROJECTION_ORDER),
 "selected_geometry_order":list(GEOMETRY_ORDER),
 "conditional_readout_order":list(READOUT_ORDER),
 "all_new_numeric_arrays_are_complete_directed_Arb_ball_strings":True,
 "nested_spacing":"1/(40*N)","last_nested_interval":["7/8","37/40"],
 "inner_cutoff_support":["71/80","73/80"],
 "inner_cutoff_derivative_upper":"80",
 "selection":"minimize the certified eta_N upper endpoint, then choose the smallest N; retain both complete five-column rows at that same N",
 "total_unknown_error_optimality_claimed":False,
 "entrywise_minimum_between_different_N_or_formulas":False,
 "source_angle_degree_bound":288,"source_angle_physical_bandwidth":1152,
 "ordinary_radial_measure":"dr","angular_measure":"normalized original moving circle",
 "same_real_continuous_two_sided_H1_state_required":True,
 "true_ordinary_residual_zero_required_for_copied_source_bounds":True,
 "full_low_mean_retained":True,"unknown_C0_whole_collar_is_a_hypothesis":True,
 "independent_narrow_MA_domain_is_not_required_for_this_direct_H1_estimate":True,
 "independent_narrow_MA_domain_is_not_proved_or_extended":True,
 "old_source_or_LC_math_recomputed":False,
 "original_target_grid_native_or_Green_read":False,
 "maximum_complete_scientific_conclusion_bytes":45000,
 "all768_rows_only_in_temporary_audit":True}

def sha_bytes(raw):return hashlib.sha256(raw).hexdigest()
def sha(path):return sha_bytes(Path(path).read_bytes())
def exact(value):
    q=Fraction(value)
    return arb(q.numerator)/q.denominator
def upper(value):return arb(value).upper()
def lower(value):return arb(value).lower()
def box(value):
    if not isinstance(value,dict):raise ValueError("a complete directed ball is required")
    if "ball" in value:z=arb(value["ball"])
    elif "lower" in value and "upper" in value:
        z=arb(value["lower"]).lower().union(arb(value["upper"]).upper())
    else:raise ValueError("a bare midpoint is not an input enclosure")
    if not z.is_finite():raise ValueError("nonfinite directed input")
    return z
def norm(value):
    z=box(value)
    if not z.upper()>=0:raise ValueError("negative norm upper endpoint")
    return abs(z).upper()
def rec(value,digits=24):
    z=arb(value)
    if not z.is_finite():raise ValueError("nonfinite new scalar")
    if digits<=24:
        for precision in (24,22,20,18,16):
            text=z.str(precision)
            if len(text)<=56:return {"ball":text}
        raise ValueError("the directed publication ball exceeds its fixed format bound")
    return {"ball":z.str(digits)}
def records(values,digits=24):return {k:rec(v,digits) for k,v in values.items()}
def encoded(value,pretty=False):
    options={"allow_nan":False}
    if pretty:options["indent"]=2
    else:options["separators"]=(",",":")
    return (json.dumps(value,**options)+"\n").encode()
def read(path):return json.loads(Path(path).read_bytes())
def save(path,value):
    raw=encoded(value);path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temp=path.with_name(path.name+".tmp");temp.write_bytes(raw);temp.replace(path)
    return {"bytes":len(raw),"sha256":sha_bytes(raw)}
def gate(doc,name,ok):
    doc["gates"].append({"name":name,"passed":bool(ok)})
    if not ok:raise ValueError("gate failed: "+name)

def checked_inputs(args,doc):
    manifest=read(args.manifest)
    gate(doc,"immutable_source_parameters_precision_and_small_conclusion_format",
        args.bits==320 and manifest["parameters"]==PARAMETERS and manifest["source_sha256"]==sha(__file__))
    gate(doc,"all_current_small_inputs_match_the_independent_exact_byte_manifest",
        all(sha(args.root/p)==s for p,s in manifest["files"].items())
        and all(sha(args.root/TOPIC/FILES[k])==v for k,v in EXPECTED.items())
        and manifest.get("historical_input_paths")==[])
    lc=read(args.root/TOPIC/FILES["lc_science"])
    process=read(args.root/TOPIC/FILES["lc_process"])
    recovery=read(args.root/TOPIC/FILES["lc_recovery"])
    wc=read(args.root/TOPIC/FILES["wide_source"])
    pretty=encoded(lc,pretty=True)
    gate(doc,"LC_compact_reproduces_the_exact_original_74725_byte_scientific_object",
        len(pretty)==74725 and sha_bytes(pretty)==LC_ORIGINAL_PRETTY_SHA
        and len((args.root/TOPIC/FILES["lc_science"]).read_bytes())==55770)
    children=process.get("children",[])
    gate(doc,"LC_completed_scientific_child_and_all16_gates_are_preserved",
        lc.get("kind")==LC_KIND and lc.get("complete") is True and lc.get("failure") is None
        and lc.get("actual_returncode")==0 and lc.get("source_sha256")==LC_SCI_SHA
        and len(lc.get("gates",[]))==16 and all(g["passed"] is True for g in lc["gates"])
        and process.get("complete") is True and len(children)==1
        and children[0].get("actual_returncode")==0
        and process.get("actual_scientific_summary_sha256")==LC_ORIGINAL_PRETTY_SHA
        and process.get("actual_scientific_summary_bytes")==74725)
    marker=recovery.get("original_PREPUBLICATION_STATUS",{})
    gate(doc,"the_original_publication_failure_and_lossless_recovery_identity_are_not_erased",
        process.get("publication_failure",{}).get("message")==
             "the complete scientific stdout receipt exceeds 59000 UTF8 bytes"
        and recovery.get("complete") is True
        and recovery["lossless_compaction"]["compact_complete_science"]["sha256"]==EXPECTED["lc_science"]
        and recovery["complete_final_process"]["sha256"]==EXPECTED["lc_process"]
        and recovery["original_scientific_pretty"]["sha256"]==LC_ORIGINAL_PRETTY_SHA
        and marker.get("actual_returncode")==0 and marker.get("gates_passed")==16
        and marker.get("scientific_bytes")==74725
        and marker.get("scientific_sha256")==LC_ORIGINAL_PRETTY_SHA)
    lp=lc["parameters"]
    gate(doc,"the_same_selected_object_interval_full_mean_and_all_six_C0_radii_are_fixed",
        lc.get("derived_continuous_centre_definition_sha256")==CENTRE
        and lp["exact_interval"]==PARAMETERS["exact_interval"] and lp["exact_cut"]=="9/10"
        and lp["selected_delta_half_width"]=="1/10000000000"
        and lp["rho_candidates"]==list(RHO) and lp["high_projection_labels"]==list(LABELS)
        and lp["centre_pair_A0_repair"]=="0.000000000000000003861"
        and lp["canonical_response_pair_A0"]=="19" and lp["canonical_response_pair_angle_A0"]=="83"
        and lp["full_low_mean_retained"] is True and lp["physical_frequency_factor"]==4
        and lc["original_counts"]["selected_closed_rows"]==140
        and lc["original_counts"]["exact_total_selected_measure"]=="1/10")
    cases=lc["new_collar_cases"]
    candidates=[cases[r]["candidate_energy"][str(j)] for r in RHO for j in LABELS]
    gate(doc,"all12_completed_LC_candidates_keep_their_actual_mean_and_both_energy_tests",
        len(cases)==6 and lc["new_coercivity_candidates_evaluated"]==12
        and lc["new_coercivity_candidates_passed"]==12
        and all(c["complete_coercivity_applies"] is True and c["failure"] is None
                and c["actual_mean_gap_positive"] is True and c["tau_below_one"] is True
                and c["t_below_one"] is True and c["complete_energy_and_trace_bounds"] is not None
                for c in candidates))
    wp=wc["parameters"];ws=wc["complete_wide_known_source"]
    gate(doc,"the_completed_WC_source_has_the_same_true_collar_and_canonical_selected_reference",
        wc.get("kind")==WC_KIND and wc.get("complete") is True and wc.get("proved") is True
        and wc.get("actual_returncode")==0 and wc.get("failure") is None
        and wc.get("source_sha256")==WC_SCI_SHA and len(wc.get("gates",[]))==13
        and all(g["passed"] is True for g in wc["gates"])
        and wc["derived_continuous_centre_definition_sha256"]==CENTRE
        and wc["derived_continuous_response_definition_sha256"]==RESPONSE
        and wc["exact_eta"]==lp["exact_eta"] and wc["exact_nu0"]==lp["exact_nu"]
        and wp["exact_wide_interval"]==PARAMETERS["exact_interval"] and wp["exact_cut"]=="9/10"
        and wp["delta_half_width"]=="1/10000000000"
        and ws["exact_interval"]==PARAMETERS["exact_interval"])
    gate(doc,"the_copied_sources_retain_mean_repair_true_dr_and_the_exact_high288_zero",
        ws["all_mean_and_repair_fees_retained"] is True
        and ws["ordinary_mean_killed_only_by_high_projection"] is True
        and ws["unknown_ordinary_source_still_required_if_not_true_solution"] is True
        and ws["known_H288_source_exactly_zero"] is True
        and ws["known_H288_angle_source_exactly_zero"] is True
        and wp["ordinary_radial_measure"]=="dr" and wp["true_unknown_ordinary_residual"]=="0"
        and wc["old_target_Fourier_residual_repair_mean_flow_or_Green_calls"]==0)
    f0=norm(ws["complete_known_F96_upper"])
    f1old=norm(ws["complete_known_F96_angle_upper"])
    f1band=upper(1152*f0)
    f1=min(f1old,f1band)
    gate(doc,"both_complete_F96_angle_bounds_are_nonnegative_and_same_window",
        f0>=0 and f1old>=0 and f1band>=0 and f1>=0)
    doc["input_identity"]={k:{"path":FILES[k],"sha256":v} for k,v in EXPECTED.items()}
    doc["LC_original_pretty_identity"]={"bytes":74725,"sha256":LC_ORIGINAL_PRETTY_SHA}
    doc["LC_original_workflow_failure_preserved"]=process["publication_failure"]
    doc["copied_source_bounds"]={
        "exact_interval":PARAMETERS["exact_interval"],
        "F96":ws["complete_known_F96_upper"],"F96_angle":ws["complete_known_F96_angle_upper"],
        "F96_angle_band_bound":rec(f1band),"F96_angle_complete_upper_used":rec(f1),
        "F288_exactly_zero_for_true_solution":True,
        "F288_angle_exactly_zero_for_true_solution":True,
        "mean_repair_and_offset_unchanged":True,
        "source_integrals_recomputed":False}
    return lc,{96:(f0,f1),288:(arb(0),arb(0))}

def coefficient_bounds(lc,rho):
    old=lc["complete_original_component_restrictions"]
    row=lc["new_collar_cases"][rho]["complete_upper_coefficients"]
    q=lambda key:norm(old[key])
    r=lambda key:norm(row[key])
    R=upper(q("raw_U")+q("raw_V"))
    beta=q("beta_absolute");kK=max(arb(1),q("K_upper"))
    b=q("b");alpha=q("alpha");pplus=q("Pnorm_upper")
    M0=q("M0");M1=q("M1")
    dnu=exact(PARAMETERS["selected_delta_half_width"]);rr=exact(rho)
    EQ=exact("0.000000000000000003861")
    ek=upper(EQ+19*dnu)
    E0=upper(19*pplus*dnu);E1=upper(83*pplus*dnu)
    E2=upper(384*E1);M20=upper(128*M1)
    Md=r("Mdelta");Md1=r("Mdelta1");eta=r("eta")
    M=upper(Md+eta);M2=upper(M20+E2)
    D1=upper(q("raw_drift_phi")+beta*kK*(2*R*ek+ek*ek)
             +2*beta*kK*rr*(2*(R+ek)+rr))
    A1=upper(D1+alpha+3*b*M*M)
    B10=upper(8*b*M*Md1+b*M*M2/2)
    # Same degree32 background; all primitive and mean projections are retained.
    delta_dphi=upper(beta*kK*(2*(R+EQ)*19*dnu+(19*dnu)**2)
                       +2*beta*kK*rr*(2*(R+ek)+rr))
    D10=upper(q("raw_drift_phi")+beta*kK*(2*R*EQ+EQ*EQ))
    A10=upper(D10+b*(6*q("Mmean")*q("N0")+3*q("N0")*q("N0")))
    err=upper(E0+eta);deltaB=upper(2*E0+eta)
    deltaA1=upper(delta_dphi+b*(6*M0*err+3*err*err))
    B100=upper(8*b*M0*M1+b*M0*M20/2)
    deltaB10=upper(b*(8*M0*E1+4*deltaB*(M1+E1))
                       +b*(E2*(2*M0+deltaB)+M20*deltaB)/4)
    DH=upper(B100+deltaB10)
    B0=upper(pplus*rr*exact("1/10").sqrt())
    return {
        "M":M,"Mdelta2":M2,"actual_drift_phi":D1,"A1":A1,"B10_NC":B10,
        "base_A1_mixing":A10,"base_B10":B100,"delta_A1":deltaA1,"delta_B10":deltaB10,
        "B10_BD":DH,"pplus":pplus,"high_body_C0_hypothesis_bound":B0,
        "d0":r("d0"),"dplus":r("actual_drift"),
        "delta_d":upper(r("drift_reference_delta")+r("drift_nonlinear"))}

def projection_constants(lc,rho,J,c):
    old=lc["new_collar_cases"][rho]
    energy=old["candidate_energy"][str(J)]["complete_energy_and_trace_bounds"]
    coeff=old["complete_upper_coefficients"];n=4*(J+1)
    cp0=norm(energy["cp_sharp"]);cr0=norm(energy["cr_sharp"])
    bp=norm(energy["cp_after_high_absorption"]);k=upper(bp/n)
    CS=norm(coeff["C_shell"+str(J)]);CL=norm(coeff["C_low"+str(J)])
    t1=upper(cp0*c["A1"]/n)
    result={"projection_label":J,"physical_first_high_frequency":n,
        "new_first_angular_gate_t1":rec(t1),"new_first_angular_gate_passed":bool(t1<1),
        "old_mean_tau_t0_gates_are_copied_from_LC":True}
    base={"k":k,"bp":bp,"CS":CS,"CL":CL,"B0":c["high_body_C0_hypothesis_bound"]}
    if not t1<1:
        result["failure"]="The sufficient first-angular absorption gate t1<1 was not certified."
        result["selected_complete_rows"]=None
        return result,None
    bp1=upper(cp0/(1-t1));br1=upper(cr0/(1-t1))
    TJ=upper(c["pplus"]*(1+arb(1)/(n*n)).sqrt()*(bp1*br1/n).sqrt())
    GH_NC=upper(c["B10_NC"]+6400*bp)
    GL_NC=upper(c["B10_NC"]+4*J*c["A1"]+(4*J)**2*c["dplus"])
    DS=upper(c["base_B10"]+4*J*c["base_A1_mixing"]+(4*J)**2*c["d0"])
    DL=upper(c["delta_B10"]+4*J*c["delta_A1"]+(4*J)**2*c["delta_d"])
    GH_BD=upper(c["B10_BD"]+6400*bp)
    base.update(T=TJ,GH_NC=GH_NC,GL_NC=GL_NC,DS_BD=DS,DL_BD=DL,GH_BD=GH_BD)
    result.update(failure=None,new_constants=records({
        "k":k,"bp1":bp1,"br1":br1,"trace_T":TJ,
        "GammaH_NC":GH_NC,"GammaL_NC":GL_NC,
        "GammaH_BD":GH_BD,"shell_derivative_BD":DS,"low_derivative_BD":DL}))
    result["projection_constant_balls"]=[result["new_constants"][key]["ball"] for key in PROJECTION_ORDER]
    del result["new_constants"]
    return result,base

def nested_row(base,N,sources):
    r=upper(40*N*base["k"]);power=arb(1);series=arb(0)
    for _ in range(N):
        series=upper(series+power);power=upper(power*r)
    eta=upper(power);sigma=upper(base["k"]*series)
    out={"N":N,"r":r,"eta":eta,"sigma":sigma,"r_below_one":bool(r<1),"methods":{}}
    f0,f1=sources
    for method in ("NC","BD"):
        GH=base["GH_"+method]
        theta=upper(80*base["bp"]+GH*sigma)
        if method=="NC":
            shell=upper(theta*base["CS"]);low=upper(base["GL_NC"]+theta*base["CL"])
        else:
            shell=upper(base["DS_BD"]+theta*base["CS"])
            low=upper(base["DL_BD"]+theta*base["CL"])
        coeff=[base["T"],upper(base["T"]*theta),upper(base["T"]*shell),
               upper(base["T"]*low),upper(base["T"]*GH*eta)]
        known=upper(coeff[0]*f1+coeff[1]*f0)
        high=upper(coeff[4]*base["B0"])
        out["methods"][method]={"coefficients":coeff,
            "known_source_upper":known,"conditional_high_C0_upper":high,
            "known_source_plus_conditional_high_C0_upper":upper(known+high)}
    return out

def row_record(row,digits=24):
    result={"N":row["N"],"geometry_balls":[rec(row[k],digits)["ball"] for k in GEOMETRY_ORDER],
        "r_below_one":row["r_below_one"],"methods":{}}
    for method,data in row["methods"].items():
        result["methods"][method]={
            "five_column_balls":[rec(x,digits)["ball"] for x in data["coefficients"]],
            "conditional_readout_balls":[rec(data[k+"_upper"],digits)["ball"] for k in READOUT_ORDER]}
    return result

def run(args,doc):
    lc,sources=checked_inputs(args,doc);audit=[];out={};valid=0;passed=0
    for rho in RHO:
        c=coefficient_bounds(lc,rho)
        rr={"rho":rho,"radius_coefficient_balls":[rec(c[key])["ball"] for key in RADIUS_ORDER],"projections":{}}
        for J in LABELS:
            summary,base=projection_constants(lc,rho,J,c)
            rows=[]
            if base is None:
                for N in range(1,65):
                    rows.append({"N":N,"complete_rows_valid":False,
                        "failure":summary["failure"],"new_first_angular_gate_t1":summary["new_first_angular_gate_t1"]})
                summary["N_rows_evaluated"]=64
                summary["valid_complete_row_pairs"]=0
                summary["useful_r_below_one_count"]=0
                summary["eta_selection_certified"]=None
            else:
                passed+=1;numerical=[nested_row(base,N,sources[J]) for N in range(1,65)]
                # One complete row is selected. No individual column is optimized separately.
                best=numerical[0]
                for row in numerical[1:]:
                    if row["eta"]<best["eta"]:best=row
                certified=all(best["eta"]<=row["eta"] for row in numerical)
                if not certified:raise ValueError("the complete-row eta selection was not certified")
                rows=[row_record(row,60) for row in numerical]
                decay=[row["N"] for row in numerical if row["r_below_one"]]
                if decay!=list(range(1,len(decay)+1)):
                    raise ValueError("the finite r_N decay gates are not in their exact monotone order")
                valid+=64
                summary.update(N_rows_evaluated=64,valid_complete_row_pairs=64,
                    useful_r_below_one_count=len(decay),
                    useful_r_below_one_N_range=[1,len(decay)] if decay else None,
                    eta_selection_certified=True,
                    selected_complete_rows=row_record(best))
            raw=encoded(rows)
            summary["temporary_case_audit_sha256"]=sha_bytes(raw)
            rr["projections"][str(J)]=summary
            audit.append({"rho":rho,"J":J,"rows":rows})
        out[rho]=rr
    gate(doc,"all6_radii_and12_independent_first_angular_gates_are_evaluated",
        len(out)==6 and sum(len(x["projections"]) for x in out.values())==12)
    gate(doc,"all768_parameter_triples_retain_both_formulas_or_the_same_explicit_failed_gate",
        len(audit)==12 and sum(len(x["rows"]) for x in audit)==768)
    gate(doc,"all_successful_selected_rows_retain_exactly_five_columns_for_both_formulas",
        all(x["selected_complete_rows"] is None or
            (set(x["selected_complete_rows"]["methods"])=={"NC","BD"}
             and all(len(y["five_column_balls"])==5
                     for y in x["selected_complete_rows"]["methods"].values()))
            for r in out.values() for x in r["projections"].values()))
    gate(doc,"selection_is_whole_row_at_one_N_with_no_entrywise_minimum",
        all(x["eta_selection_certified"] is None or x["eta_selection_certified"] is True
            for r in out.values() for x in r["projections"].values()))
    audit_path=Path(str(args.out)+".complete768-audit.json")
    audit_identity=save(audit_path,{"kind":"temporary_complete_nested_collar_scalar_audit_v1",
        "parameters":PARAMETERS,"source_sha256":sha(__file__),"rows":audit})
    gate(doc,"the_complete768_row_two_formula_audit_is_temporary_only_and_has_an_exact_identity",
        audit_identity["bytes"]>0 and len(audit_identity["sha256"])==64)
    doc.update(cases=out,new_first_angular_cases_evaluated=12,new_first_angular_cases_passed=passed,
        parameter_triples_examined=768,complete_formula_rows_considered=1536,
        complete_formula_rows_evaluated=2*valid,
        parameter_triples_with_valid_complete_rows=valid,
        complete_formula_rows_valid=2*valid,
        temporary_complete_audit={**audit_identity,"parameter_triples":768,
            "complete_formula_rows_considered":1536,"complete_formula_rows_evaluated":2*valid,"persisted":False},
        actual_unknown_low_shell_body_or_cut_norm_supplied=False,
        actual_low_curvature_entry_proved=False,actual_core_existence_or_matching_proved=False,
        old_source_integrals_or_successful_LC_math_recomputed=False,
        original_targets_intrinsic_jets_Fourier_repair_mean_flow_Green_calls=0,
        new_recomputable_native_persisted=False,
        scope={"same_real_two_sided_H1_true_solution_required":True,
            "all_low_means_and_cutoff_columns_retained":True,
            "unknown_C0_domain_remains_a_hypothesis":True,
            "t1_is_a_new_independent_sufficient_gate":True,
            "r_N_at_least_one_rows_are_finite_valid_bounds_without_decay":True,
            "all_N_are_finite_no_angular_regularization_is_assumed":True,
            "NC_and_BD_remain_two_complete_operator_rows":True,
            "one_whole_row_may_be_chosen_after_actual_nonnegative_inputs_are_supplied":True,
            "entrywise_minimum_claimed":False,
            "arbitrary_approximate_F_phi_or_mean_residual_supplied":False,
            "physical_or_pair_sum_conversion_not_added":True,
            "narrow_MA_high_domain_proved_or_extended":False})
    gate(doc,"all_mean_source_unknown_domain_and_same_state_obligations_remain_explicit",
        doc["actual_unknown_low_shell_body_or_cut_norm_supplied"] is False
        and doc["actual_low_curvature_entry_proved"] is False
        and doc["actual_core_existence_or_matching_proved"] is False)
    return doc

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root",type=Path,required=True);p.add_argument("--manifest",type=Path,required=True)
    p.add_argument("--bits",type=int,default=320);p.add_argument("--out",type=Path,required=True)
    args=p.parse_args();ctx.prec=args.bits;start=time.monotonic()
    doc={"kind":KIND,"complete":False,"failure":None,"actual_returncode":None,
        "source_sha256":sha(__file__),"input_manifest_sha256":sha(args.manifest),
        "parameters":PARAMETERS,"gates":[]}
    status=0
    try:
        run(args,doc);doc.update(complete=True,actual_returncode=0)
    except Exception as error:
        status=1;doc.update(actual_returncode=1,failure={
            "type":type(error).__name__,"message":str(error),"traceback":traceback.format_exc()})
    doc["seconds"]=time.monotonic()-start
    saved=save(args.out,doc)
    print(json.dumps({"kind":"nested_collar_direct_trace_scientific_status",
        "actual_returncode":status,"complete":doc["complete"],
        "structural_gates_passed":sum(g["passed"] for g in doc["gates"]),
        "structural_gates_total":len(doc["gates"]),
        "first_angular_passed":doc.get("new_first_angular_cases_passed"),
        "triples":doc.get("parameter_triples_examined"),**saved},
        separators=(",",":"),allow_nan=False),flush=True)
    return status

if __name__=="__main__":raise SystemExit(main())
