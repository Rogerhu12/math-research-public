#!/usr/bin/env python3
"""New adaptive NC/BD geometry from completed small coefficients only."""
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
KIND="actual_adaptive_collar_geometry_complete_direct_trace_rows_v1"
NC_KIND="actual_nested_collar_direct_first_angular_trace_rows_v1"
LC_KIND="actual_saved_positive_collar_components_and_high_coercivity_v1"
NC_BASE="notes/nested_collar_direct_trace_ci/run-43733916510-1-nested-collar-direct-trace/"
LC_BASE="notes/saved_positive_collar_components_ci/run-43731225532-1-saved-positive-collar-components/"
FILES={
 "NC_science":NC_BASE+"actual-nested-collar-direct-trace.json",
 "NC_process":NC_BASE+"process.json",
 "LC_science":LC_BASE+"actual-saved-positive-collar-components.json",
 "LC_process":LC_BASE+"process.json","LC_recovery":LC_BASE+"recovery.json",
 "NC":"results/R133-supplement-nested-collar-localization-and-direct-projected-first-angular-trace.md",
 "BD":"results/R133-supplement-complete-degree32-splitting-of-the-differentiated-collar-equation.md",
 "NG":"results/R133-supplement-adjustable-nested-collar-geometry-and-complete-direct-trace.md"}
EXPECTED={
 "NC_science":"83e06a289105254022cba13ae23ff102ce384c1ae9e2ade468e5cdc979654df6",
 "NC_process":"3157ed355d059c032662f130b40f5952f564c7337a7ef986e8429ae019bc4057",
 "LC_science":"44b4da07b50dcca9be7671b8cb59b227999e76871237c25a1bc0aec4bc02492c",
 "LC_process":"a15e9b16d6867d0f69a85d9549ad66953f70b444e7d9462ec45281aadf84cb58",
 "LC_recovery":"22d627a37aeb0b5a519df4d82aa4de111f82caca15127e2081010e94c3820a41",
 "NC":"558f47f743ccbfbb14c5305a56a699900e472b03183037951d0b26be33983df9",
 "BD":"bb792252f0a3400547293ba5d8e9f9f5c2aa842dcf749abfd3f993abd478935c",
 "NG":"cc3add84d3c7cad870345d6aef4f5101023d448d27df9025a72d9ecbe29bbbbc"}
NC_SOURCE_SHA="57ca8b5b9357a875180c7aec2caef7ab975a2e1b5d64b0ae6b88f510dd606204"
NC_MANIFEST_SHA="191aec33eee20cae472857dc10d5d7cc81f2023738310e56fe02feabb30f0e1d"
LC_SOURCE_SHA="02fc50c45ed2610b94619d9db60ee2f74dc3a1643ce2f398c8eb25505926f7ea"
LC_PRETTY_SHA="903a537a0454464e8c30ff57034b2811d1c43ad47a18979f5a7d8403c888b981"
RHO=("1/10000","1/1048576","1/16777216","1/268435456","1/4294967296","1/68719476736")
LABELS=(96,288)
HALF_WIDTHS=("1/100","1/200","1/400","1/1000")
COLUMN_ORDER=("ordinary_angle_source","ordinary_source","shell_body","low_body","high_body")
GEOMETRY_ORDER=("r","eta","sigma")
READOUT_ORDER=("known_source","conditional_high_C0","known_source_plus_conditional_high_C0")
PARAMETERS={
 "arithmetic_bits":320,"output_ball_significant_digits":24,
 "output_ball_minimum_significant_digits":16,"output_ball_maximum_characters":56,
 "exact_interval":["17/20","19/20"],"exact_cut":"9/10","outer_half_width":"1/20",
 "selected_delta_half_width":"1/10000000000","wide_rho_candidates":list(RHO),
 "high_projection_labels":list(LABELS),"physical_frequency_factor":4,
 "new_inner_half_widths":list(HALF_WIDTHS),"new_nested_counts":list(range(1,129)),
 "new_parameter_triples":6144,"new_complete_formula_rows":12288,
 "per_case_new_geometry_triples":512,"per_case_new_complete_formula_rows":1024,
 "useful_decay_count_order":list(HALF_WIDTHS),
 "exact_terminal_interval_formula":["9/10-a","9/10+a"],
 "exact_inner_cutoff_support_formula":["9/10-a/2","9/10+a/2"],
 "old_reference_half_width":"1/40","old_complete_reference_row_pairs":12,
 "old_reference_rows_recomputed":False,
 "five_column_order":list(COLUMN_ORDER),"selected_geometry_order":list(GEOMETRY_ORDER),
 "conditional_readout_order":list(READOUT_ORDER),
 "new_nested_spacing":"(1/20-a)/N","two_inner_cutoff_derivative_upper":"2/a",
 "selection":"minimize max of the two high-body upper endpoints in the retained outward publication balls; old reference first on an exact tie, then displayed a order and increasing N",
 "same_a_and_N_for_NC_and_BD":True,
 "entrywise_minimum_or_total_unknown_error_optimality":False,
 "old_rows_are_copied_complete_without_new_scalar_evaluation":True,
 "CS_CL_and_bp_are_read_directly_from_the_same_completed_LC":True,
 "no_ratio_of_old_upper_bounds_is_used_to_recover_CS_or_CL":True,
 "global_Pnorm_was_already_paid_once_in_copied_T":True,
 "ordinary_radial_measure":"dr","angular_measure":"normalized original moving circle",
 "same_real_continuous_two_sided_H1_true_solution_required":True,
 "full_low_means_and_all_five_columns_retained":True,
 "unknown_C0_whole_collar_is_a_hypothesis":True,
 "ordinary_source_and_angular_source_are_the_completed_NC_inputs":True,
 "nonzero_residual_iterate_requires_independent_source_and_mean_logspeed_fees":True,
 "narrow_MA_domain_neither_used_nor_extended":True,
 "all6144_new_rows_only_in_temporary_audit":True,
 "maximum_complete_scientific_conclusion_bytes":45000,
 "old_successful_math_native_grid_source_integrals_or_Green_recomputed":False}

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
    gate(doc,"immutable_source_parameters_directed_precision_and_output_format",
        args.bits==320 and manifest["parameters"]==PARAMETERS
        and manifest["source_sha256"]==sha(__file__))
    gate(doc,"all_current_small_inputs_match_the_exact_manifest_and_no_history_is_requested",
        all(sha(args.root/p)==v for p,v in manifest["files"].items())
        and all(sha(args.root/TOPIC/FILES[k])==v for k,v in EXPECTED.items())
        and manifest.get("historical_input_paths")==[])
    nc=read(args.root/TOPIC/FILES["NC_science"])
    process=read(args.root/TOPIC/FILES["NC_process"])
    lc=read(args.root/TOPIC/FILES["LC_science"])
    lc_process=read(args.root/TOPIC/FILES["LC_process"])
    lc_recovery=read(args.root/TOPIC/FILES["LC_recovery"])
    children=process.get("children",[])
    gate(doc,"the_NC_actual_child_16_structural_gates_and12_t1_gates_are_frozen_successes",
        nc.get("kind")==NC_KIND and nc.get("complete") is True
        and nc.get("failure") is None and nc.get("actual_returncode")==0
        and nc.get("source_sha256")==NC_SOURCE_SHA
        and nc.get("input_manifest_sha256")==NC_MANIFEST_SHA
        and len(nc.get("gates",[]))==16 and all(g["passed"] is True for g in nc["gates"])
        and nc.get("new_first_angular_cases_evaluated")==12
        and nc.get("new_first_angular_cases_passed")==12
        and nc.get("parameter_triples_examined")==768
        and nc.get("complete_formula_rows_evaluated")==1536)
    gate(doc,"the_complete_NC_process_matches_the_science_without_a_publication_failure",
        process.get("complete") is True and process.get("failure") is None
        and process.get("publication_failure") is None and len(children)==1
        and children[0].get("actual_returncode")==0
        and process.get("actual_source_sha256")==NC_SOURCE_SHA
        and process.get("input_manifest_sha256")==NC_MANIFEST_SHA
        and process.get("actual_scientific_summary_sha256")==EXPECTED["NC_science"]
        and process.get("actual_scientific_summary_bytes")==35707)
    pretty=encoded(lc,pretty=True)
    lc_children=lc_process.get("children",[])
    lc_marker=lc_recovery.get("original_PREPUBLICATION_STATUS",{})
    gate(doc,"the_same_completed_LC_compact_is_read_without_recomputing_its_coefficients",
        lc.get("kind")==LC_KIND and lc.get("complete") is True and lc.get("actual_returncode")==0
        and lc.get("source_sha256")==LC_SOURCE_SHA and lc.get("failure") is None
        and len(lc.get("gates",[]))==16 and all(g["passed"] is True for g in lc["gates"])
        and len(pretty)==74725 and sha_bytes(pretty)==LC_PRETTY_SHA
        and nc["input_identity"]["lc_science"]["sha256"]==EXPECTED["LC_science"]
        and lc_process.get("complete") is True and len(lc_children)==1
        and lc_children[0].get("actual_returncode")==0
        and lc_process.get("actual_scientific_summary_sha256")==LC_PRETTY_SHA
        and lc_process.get("actual_scientific_summary_bytes")==74725
        and lc_process.get("publication_failure",{}).get("message")==
            "the complete scientific stdout receipt exceeds 59000 UTF8 bytes"
        and lc_recovery.get("complete") is True
        and lc_recovery["lossless_compaction"]["compact_complete_science"]["sha256"]==EXPECTED["LC_science"]
        and lc_recovery["complete_final_process"]["sha256"]==EXPECTED["LC_process"]
        and lc_recovery["original_scientific_pretty"]["sha256"]==LC_PRETTY_SHA
        and lc_marker.get("actual_returncode")==0 and lc_marker.get("gates_passed")==16
        and lc_marker.get("scientific_bytes")==74725 and lc_marker.get("scientific_sha256")==LC_PRETTY_SHA)
    np=nc["parameters"];lp=lc["parameters"]
    gate(doc,"the_same_outer_collar_delta_radii_modes_and_true_source_domains_are_retained",
        np["exact_interval"]==PARAMETERS["exact_interval"] and np["exact_cut"]=="9/10"
        and np["selected_delta_half_width"]=="1/10000000000"
        and np["wide_rho_candidates"]==list(RHO) and np["high_projection_labels"]==list(LABELS)
        and np["physical_frequency_factor"]==4 and np["inner_cutoff_derivative_upper"]=="80"
        and np["last_nested_interval"]==["7/8","37/40"]
        and np["full_low_mean_retained"] is True
        and np["same_real_continuous_two_sided_H1_state_required"] is True
        and np["true_ordinary_residual_zero_required_for_copied_source_bounds"] is True
        and lp["rho_candidates"]==list(RHO) and lp["high_projection_labels"]==list(LABELS)
        and lp["exact_interval"]==PARAMETERS["exact_interval"]
        and lp["selected_delta_half_width"]=="1/10000000000")
    pairs=[nc["cases"][rho]["projections"][str(J)] for rho in RHO for J in LABELS]
    gate(doc,"all12_old_reference_pairs_are_complete_and_copyable_without_new_old_geometry_math",
        len(pairs)==12 and all(c["new_first_angular_gate_passed"] is True
            and c["failure"] is None and c["eta_selection_certified"] is True
            and c["selected_complete_rows"]["N"] in (13,39)
            and set(c["selected_complete_rows"]["methods"])=={"NC","BD"}
            and all(len(v["five_column_balls"])==5 and len(v["conditional_readout_balls"])==3
                for v in c["selected_complete_rows"]["methods"].values()) for c in pairs))
    src=nc["copied_source_bounds"]
    gate(doc,"the_complete_ordinary_sources_mean_repairs_and_true_high288_zero_are_copied",
        src["exact_interval"]==PARAMETERS["exact_interval"]
        and src["mean_repair_and_offset_unchanged"] is True
        and src["source_integrals_recomputed"] is False
        and src["F288_exactly_zero_for_true_solution"] is True
        and src["F288_angle_exactly_zero_for_true_solution"] is True
        and nc["scope"]["arbitrary_approximate_F_phi_or_mean_residual_supplied"] is False)
    gate(doc,"the_prior_results_supply_no_unknown_norm_or_unproved_domain_to_this_new_run",
        nc["actual_unknown_low_shell_body_or_cut_norm_supplied"] is False
        and nc["actual_low_curvature_entry_proved"] is False
        and nc["actual_core_existence_or_matching_proved"] is False
        and nc["old_source_integrals_or_successful_LC_math_recomputed"] is False
        and nc["original_targets_intrinsic_jets_Fourier_repair_mean_flow_Green_calls"]==0)
    doc["input_identity"]={k:{"path":FILES[k],"sha256":v} for k,v in EXPECTED.items()}
    doc["copied_source_bounds"]=src
    doc["preserved_original_LC_publication_failure"]=nc["LC_original_workflow_failure_preserved"]
    doc["preserved_original_LC_pretty_identity"]=nc["LC_original_pretty_identity"]
    return nc,lc,{96:(norm(src["F96"]),norm(src["F96_angle_complete_upper_used"])),
                  288:(arb(0),arb(0))}

def decode_array(names,values):
    if len(names)!=len(values) or len(set(names))!=len(names):
        raise ValueError("the completed coefficient array has a different declared schema")
    return {k:norm({"ball":v}) for k,v in zip(names,values)}

def completed_constants(nc,lc,rho,J):
    case=nc["cases"][rho];projection=case["projections"][str(J)]
    radius=decode_array(nc["parameters"]["radius_coefficient_order"],case["radius_coefficient_balls"])
    pc=decode_array(nc["parameters"]["projection_constant_order"],projection["projection_constant_balls"])
    old=lc["new_collar_cases"][rho]
    if old["candidate_energy"][str(J)]["complete_coercivity_applies"] is not True:
        raise ValueError("a copied LC energy domain failed")
    eb=old["candidate_energy"][str(J)]["complete_energy_and_trace_bounds"]
    ub=old["complete_upper_coefficients"]
    result={
        "T":pc["trace_T"],"k":pc["k"],
        "bp":norm(eb["cp_after_high_absorption"]),
        "CS":norm(ub["C_shell"+str(J)]),"CL":norm(ub["C_low"+str(J)]),
        "BNC":radius["B10_NC"],"BBD":radius["B10_BD"],
        "GL_NC":pc["GammaL_NC"],"DS_BD":pc["shell_derivative_BD"],
        "DL_BD":pc["low_derivative_BD"],"B0":radius["high_body_C0_hypothesis_bound"]}
    if any(not arb(x).is_finite() or x<0 for x in result.values()):
        raise ValueError("the complete positive budget coefficients are not finite nonnegative bounds")
    return result,projection

def candidate(base,a_text,N,sources):
    a=Fraction(a_text);h=(Fraction(1,20)-a)/N
    if not (0<a<Fraction(1,20) and N in range(1,129) and h>0):
        raise ValueError("the new inner and nested interval geometry is invalid")
    kappa=exact(2/a);r=upper(base["k"]/exact(h))
    power=arb(1);series=arb(0)
    for _ in range(N):
        series=upper(series+power);power=upper(power*r)
    eta=upper(power);sigma=upper(base["k"]*series)
    row={"a":a_text,"N":N,"exact_nested_h":str(h),"exact_cutoff_kappa":str(2/a),
        "exact_terminal_interval":[str(Fraction(9,10)-a),str(Fraction(9,10)+a)],
        "exact_inner_cutoff_support":[str(Fraction(9,10)-a/2),str(Fraction(9,10)+a/2)],
        "r":r,"eta":eta,"sigma":sigma,"r_below_one":bool(r<1),"methods":{}}
    f0,f1=sources
    for method in ("NC","BD"):
        GH=upper(base["B"+method]+kappa*kappa*base["bp"])
        theta=upper(kappa*base["bp"]+GH*sigma)
        if method=="NC":
            shell=upper(theta*base["CS"]);low=upper(base["GL_NC"]+theta*base["CL"])
        else:
            shell=upper(base["DS_BD"]+theta*base["CS"])
            low=upper(base["DL_BD"]+theta*base["CL"])
        coeff=[base["T"],upper(base["T"]*theta),upper(base["T"]*shell),
               upper(base["T"]*low),upper(base["T"]*GH*eta)]
        known=upper(coeff[0]*f1+coeff[1]*f0);high=upper(coeff[4]*base["B0"])
        row["methods"][method]={"coefficients":coeff,"GammaH":GH,"Theta":theta,
            "known_source_upper":known,"conditional_high_C0_upper":high,
            "known_source_plus_conditional_high_C0_upper":upper(known+high)}
    # Compare exactly the directed high balls that the small conclusion will retain.
    # Final formatting may widen an internal winner; it is part of the score.
    row["published_rows"]=complete_row_record(row)
    row["objective"]=max(norm({"ball":v["five_column_balls"][4]})
                         for v in row["published_rows"]["methods"].values())
    return row

def complete_row_record(row,digits=24,include_intermediates=False):
    out={"N":row["N"],"geometry_balls":[rec(row[k],digits)["ball"] for k in GEOMETRY_ORDER],
        "r_below_one":row["r_below_one"],"methods":{}}
    for method,v in row["methods"].items():
        out["methods"][method]={"five_column_balls":[rec(x,digits)["ball"] for x in v["coefficients"]],
            "conditional_readout_balls":[rec(v[k+"_upper"],digits)["ball"] for k in READOUT_ORDER]}
        if include_intermediates:
            out["methods"][method]["GammaH"]=rec(v["GammaH"],digits)
            out["methods"][method]["Theta"]=rec(v["Theta"],digits)
    return out

def audit_record(row):
    return {"a":row["a"],"exact_nested_h":row["exact_nested_h"],
        "exact_cutoff_kappa":row["exact_cutoff_kappa"],
        "exact_terminal_interval":row["exact_terminal_interval"],
        "exact_inner_cutoff_support":row["exact_inner_cutoff_support"],
        "objective":rec(row["objective"],60),
        "retained_high_column_balls":[row["published_rows"]["methods"][m]["five_column_balls"][4]
                                      for m in ("NC","BD")],
        "complete_rows":complete_row_record(row,60,include_intermediates=True)}

def run(args,doc):
    nc,lc,sources=checked_inputs(args,doc);audit=[];cases={};new_selected=0
    old_copy_checks=[];selection_checks=[];new_total=0
    for rho in RHO:
        case={"rho":rho,"projections":{}}
        for J in LABELS:
            base,projection=completed_constants(nc,lc,rho,J)
            oldrows=projection["selected_complete_rows"]
            old_objective=max(norm({"ball":v["five_column_balls"][4]})
                              for v in oldrows["methods"].values())
            selected=None;best_objective=old_objective
            all_new=[];decay=[]
            for a in HALF_WIDTHS:
                rows=[candidate(base,a,N,sources[J]) for N in range(1,129)]
                useful=[x["N"] for x in rows if x["r_below_one"]]
                if useful!=list(range(1,len(useful)+1)):
                    raise ValueError("the useful finite r_N gates are not in exact monotone order")
                decay.append(len(useful))
                for row in rows:
                    if row["objective"]<best_objective:
                        selected=row;best_objective=row["objective"]
                all_new.extend(rows)
            selected_is_old=selected is None
            certified=(best_objective<=old_objective
                       and all(best_objective<=x["objective"] for x in all_new))
            if not certified:raise ValueError("the common whole-pair objective selection was not certified")
            selection_checks.append(certified);new_total+=len(all_new)
            if selected_is_old:
                selection={"origin":"copied_old_reference","a":"1/40",
                    "objective_ball":rec(best_objective)["ball"],"complete_rows":oldrows}
            else:
                new_selected+=1
                selection={"origin":"new_geometry","a":selected["a"],
                    "objective_ball":rec(best_objective)["ball"],
                    "complete_rows":selected["published_rows"]}
            actual_copy=json.loads(json.dumps(oldrows,allow_nan=False))
            old_copy_checks.append(encoded(actual_copy)==encoded(oldrows))
            temp_rows=[audit_record(x) for x in all_new]
            temp_raw=encoded(temp_rows)
            case["projections"][str(J)]={
                "J":J,"copied_first_angular_gate":projection["new_first_angular_gate_t1"],
                "copied_first_angular_gate_passed":True,
                "old_reference":{"a":"1/40","objective_ball":rec(old_objective)["ball"],
                    "complete_rows":actual_copy},
                "useful_decay_counts":decay,"objective_selection_certified":True,
                "selected":selection,"temporary_new_audit_sha256":sha_bytes(temp_raw)}
            audit.append({"rho":rho,"J":J,"complete_constants":records(base,60),"new_rows":temp_rows})
        cases[rho]=case
    gate(doc,"all12_old_reference_pairs_are_copied_exactly_with_full_five_columns_and_readouts",
        len(old_copy_checks)==12 and all(old_copy_checks))
    gate(doc,"all6144_new_geometry_triples_and12288_complete_formulas_are_evaluated",
        new_total==6144 and len(audit)==12 and all(len(x["new_rows"])==512 for x in audit))
    gate(doc,"all_new_positive_nested_geometries_keep_both_inner_cutoffs_and_the_finite_polynomial",
        all(len(c["useful_decay_counts"])==4 for r in cases.values() for c in r["projections"].values()))
    gate(doc,"each_selected_geometry_keeps_both_complete_five_column_rows_at_the_same_a_N",
        all(set(c["selected"]["complete_rows"]["methods"])=={"NC","BD"}
            and all(len(v["five_column_balls"])==5 for v in c["selected"]["complete_rows"]["methods"].values())
            for r in cases.values() for c in r["projections"].values()))
    gate(doc,"the_high_column_maximum_selection_includes_the_complete_old_reference_and_exact_tie_rule",
        len(selection_checks)==12 and all(selection_checks))
    aid=save(Path(str(args.out)+".complete6144-audit.json"),{
        "kind":"temporary_complete_adaptive_collar_geometry_audit_v1",
        "source_sha256":sha(__file__),"parameters":PARAMETERS,"cases":audit})
    gate(doc,"the_complete_new_audit_is_temporary_only_with_its_exact_hash_and_count",
        aid["bytes"]>0 and len(aid["sha256"])==64)
    doc.update(cases=cases,old_complete_reference_row_pairs_copied=12,
        new_geometry_triples_examined=6144,new_complete_formula_rows_evaluated=12288,
        selected_pair_count=12,selected_new_geometry_count=new_selected,
        selected_old_reference_count=12-new_selected,
        temporary_complete_audit={**aid,"new_parameter_triples":6144,
            "new_complete_formula_rows":12288,"persisted":False},
        actual_unknown_low_shell_body_or_cut_norm_supplied=False,
        actual_low_curvature_entry_proved=False,actual_core_existence_or_matching_proved=False,
        old_successful_math_native_grid_source_integrals_or_Green_recomputed=False,
        new_recomputable_native_persisted=False,
        scope={"same_real_two_sided_H1_true_solution_required":True,
            "unknown_C0_domain_remains_a_hypothesis":True,
            "all_means_ordinary_sources_and_cutoff_columns_retained":True,
            "copied_T_already_contains_one_global_Pnorm_fee":True,
            "old_reference_complete_rows_unchanged":True,
            "max_high_column_is_the_only_selection_objective":True,
            "source_shell_low_columns_may_increase":True,
            "entrywise_minimum_or_total_unknown_error_optimality_claimed":False,
            "approximate_source_and_mean_logspeed_fees_supplied":False,
            "narrow_MA_domain_neither_used_nor_extended":True})
    gate(doc,"all_same_state_source_mean_unknown_domain_and_selection_limitations_remain_explicit",
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
    doc["seconds"]=time.monotonic()-start;saved=save(args.out,doc)
    print(json.dumps({"kind":"adaptive_collar_geometry_scientific_status",
        "actual_returncode":status,"complete":doc["complete"],
        "structural_gates_passed":sum(g["passed"] for g in doc["gates"]),
        "structural_gates_total":len(doc["gates"]),
        "new_triples":doc.get("new_geometry_triples_examined"),
        "selected_new_geometry_count":doc.get("selected_new_geometry_count"),**saved},
        separators=(",",":"),allow_nan=False),flush=True)
    return status

if __name__=="__main__":raise SystemExit(main())
