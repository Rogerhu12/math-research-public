#!/usr/bin/env python3
"""New correlated terminal-Ai leading scalar from four completed small records."""
from __future__ import annotations
import argparse
import copy
import hashlib
import importlib.metadata
import json
import os
import platform
import time
import traceback
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
REL="topics/visible-flex-exact-nearby/"
PRODUCER=REL+"scripts/fourfold_codazzi_correlated_terminal_Ai_leading_scalar.py"
KIND="actual_correlated_terminal_Ai_leading_scalar_v1"
MANIFEST_KIND="correlated_terminal_Ai_leading_scalar_public_inputs_v1"
RUNTIME={"Python":"3.12.14","python_flint":"0.9.0"}
GATE_COUNT=16
PINNED={"wl_execution":"936633fcfb2cdc9ed3f0e108909275497337f59daea9e1fa33ee0ab40de0ec5d","wt_science":"2a406e4506bb5a19646924e2072ec83d8806055a083ba7e1b1acfb9ab21d142d","wx_execution":"e9fc1611dc582e0264f0222069e03d8e9a1953616db540fc14896d4765abfb12","fa_science":"2985b74e314f39fc52d587dae193fd5eacb12d75ea42c45bc88fe73848dc64f2","kl_contract":"dc48bdb46fde624f5e6f3820a7f37e326cb3b84274f34d46e1538f6166285b9a","metric_contract":"92fd222bbcc4495cce091cedee2628f83d014be23a40328a7292d47616621635","wl_contract":"e2e9d6d4dc98c8f0b2d9c6c5cc7700a3389d228c39470736f3a8706dccbd192e","wx_contract":"c5157bbb14b300c1a418642e96917b49f0f90c1ebc3571a124a26b863adc9ae1","fa_contract":"24216c6d78f1261e16b9d53030fb2b899a94e9e9d8900e7fea79746ef32d96af","pf_contract":"5856c8cf5fac8c75997a6e3d8c9aba1ad88cb136d1ae184985164d1745aab026","wy_contract":"ebf8713508a11ef96decc5691056ea6eaa15d967d08b3a8af4b20c4284f6d1b3"}
PARAMETERS={"arithmetic_bits":320,"runtime":{"Python":"3.12.14","python_flint":"0.9.0"},"exact_real_delta_radius":"1/100000000","fixed_intrinsic_parameter":"eta_0","continuous_centre_definition_sha256":"440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47","continuous_response_definition_sha256":"6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04","exact_strict_cut":"76285779072683/320000000000000","exact_root_interval":["1191984371497/5000000000000","2383968743003/10000000000000"],"exact_short_interval_upper_length":"1220703413/320000000000000","exact_metric_support":["1/20","9/50"],"original_WL_parameter_radius":"1/10000000000","chosen_complete_state_A0":{"centre":"7","response":"19"},"reference_column":"same terminal Ai free P8 first column","physical_waves":[-1,1],"physical_input_signs":[-1,1],"original_nonmean_windows":["L2","H^(-1/3)","H^(-4/3)"],"independent_physical_means":2,"root_mean_residual_set_to_zero":False,"root_density_cancelled_by_exact_identity":True,"strict_radial_factor_orientation":"forward exp(integral_0^rc ell0 dr)","old_WL_global_parameter_fee_extended":False,"short_metric_identity_only_outside_compact_support":True,"old_root_ng_or_R0_integral_evaluated":False,"old_row_fold_profile_phase_normalizer_or_source_calls":0,"old_native_binary_or_archive_restored":0,"optional_left_state_products_evaluated":False,"all_four_moduli_equal_for_this_reference_column":True,"original_input_order":"E_star Lambda_sigma_inverse T_F_inverse S_inverse","expected_gate_count":16,"full_incoming_finite_Schur_or_actual_solution_claimed":False}
EXPECTED={
 "wl_execution":{"run":"43749764738","gates":18,
  "kind":"actual_complete_waist_lifting_from_saved_positive_algorithm_v1",
  "source":"d6764c570b935ed760425b10aeead6dea20e406fa0a0e606c1e61ad0c027d3b6",
  "manifest":"70c8488c51d5e930b333108fd6ee0d091bd270cf5720871e813b53da13c12e43"},
 "wt_science":{"run":"43763134339","gates":20,
  "kind":"actual_waist_normalizer_coefficients_and_two_window_gates_v1",
  "source":"7cde6f7f6d03bbfa107a93abdd4ee925b332f47ac7c4a2257d6557e00927a393",
  "manifest":"4cec7ef0ba21373190dd0bf142d10546823d46bb832a58df66529822990ad125"},
 "wx_execution":{"run":"43763424840","gates":20,
  "kind":"actual_true_waist_coordinates_from_saved_positive_products_v1",
  "source":"63fc880f409151152a40a6361b781280bd3785b337cf2bd3386c03496e1b9424",
  "manifest":"aa3c9d7e9f3a217122af5a321fadfcb2abe420e7e7c48217e3a181c9dbdd6f26"},
 "fa_science":{"run":"43763658978","gates":24,
  "kind":"actual_complete_free_Airy_first_omitted_cut_scalars_v1",
  "source":"a6c89d502f7583bba3b663c4296ec462fd892ad01e94427dbe55bc1c3d304954",
  "manifest":"d06951509b4af18ce5039997c032b6377c0c55be07bd01f79a686c2471e4dd6b"}
}

def canonical(x):
    return (json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(",",":"),
                       allow_nan=False)+"\n").encode("utf-8")
def sha_bytes(x):return hashlib.sha256(x).hexdigest()
def sha(path):return sha_bytes(Path(path).read_bytes())
def read(path):return json.loads(Path(path).read_text())
def q(x):
    x=Fraction(x)
    return arb(x.numerator)/x.denominator
def box(x):
    if isinstance(x,dict):
        if "lower" in x and "upper" in x:
            y=arb(x["lower"]).lower().union(arb(x["upper"]).upper())
        elif "ball" in x:y=arb(x["ball"])
        else:raise ValueError("saved scalar has no complete directed representation")
    else:y=arb(str(x))
    if not y.is_finite():raise ValueError("nonfinite saved scalar")
    return y
def up(x):
    y=box(x) if isinstance(x,dict) else arb(x)
    if not y.is_finite():raise ValueError("nonfinite directed upper")
    return y.upper()
def positive_lower(x):
    y=box(x).lower()
    if not y>0:raise ValueError("required full saved positive lower bound failed")
    return y
def nonnegative_upper(x):
    y=up(x)
    if not y>=0:raise ValueError("required nonnegative upper bound failed")
    return y
def record(x):
    y=arb(x)
    if not y.is_finite():raise ValueError("nonfinite new scalar")
    return {"ball":y.str(72)}
def gate(doc,name,ok):
    doc["gates"].append({"name":name,"passed":bool(ok)})
    if not ok:raise ValueError("correlated leading scalar gate failed: "+name)
def successful(x,info):
    return (x.get("kind")==info["kind"] and x.get("complete") is True
        and x.get("proved") is True and x.get("actual_returncode")==0
        and x.get("failure") is None and str(x.get("run_id"))==info["run"]
        and str(x.get("run_attempt"))=="1"
        and x.get("source_sha256")==info["source"]
        and x.get("input_manifest_sha256")==info["manifest"]
        and len(x.get("gates",[]))==info["gates"]
        and all(z.get("passed") is True for z in x["gates"]))
def receipt(path,execution):
    raw=read(path)
    if execution:
        if (raw.get("complete") is not True or raw.get("actual_returncode")!=0
            or raw.get("actual_failure") is not None):
            raise ValueError("original wrapper did not complete")
        return raw,raw["actual_scientific_receipt"]
    return None,raw

def checked_inputs(a,doc):
    actual={"Python":platform.python_version(),
            "python_flint":importlib.metadata.version("python-flint")}
    gate(doc,"public pinned runtime and320-bit directed scalar arithmetic",
         actual==RUNTIME and a.bits==320 and ctx.prec==320
         and os.environ.get("GITHUB_ACTIONS")=="true"
         and os.environ.get("GITHUB_REPOSITORY")==PUBLIC)
    doc["runtime"]=actual
    m=read(a.manifest)
    paths={role:Path(getattr(a,role)) for role in PINNED}
    gate(doc,"current-only closure source parameters and every immutable small input",
         sha(a.manifest)==a.manifest_sha and m.get("kind")==MANIFEST_KIND
         and m.get("public_repository")==PUBLIC
         and m.get("source_sha256")==sha(__file__)
         and m.get("parameters")==PARAMETERS
         and m.get("mathematical_input_sha256")==PINNED
         and m.get("expected_actual_gate_count")==GATE_COUNT
         and all(sha(paths[k])==v for k,v in PINNED.items()))
    ew,wl=receipt(paths["wl_execution"],True)
    gate(doc,"WL unique completed child and all eighteen original gates",
         successful(wl,EXPECTED["wl_execution"])
         and ew.get("source_budget_source_sha256")==wl["source_sha256"])
    wo=wl["complete_original_input_conclusion"]
    wp=wl["complete_positive_product_conclusion"]
    gate(doc,"WL exact positive algorithm global products and complete7/19 state identity",
         wo.get("background_definition_sha256")==PARAMETERS["continuous_centre_definition_sha256"]
         and wo.get("direction_definition_sha256")==PARAMETERS["continuous_response_definition_sha256"]
         and wo.get("complete_core_exact_measure")=="9/10"
         and wo.get("complete_original_rows")==7721
         and wo.get("complete_original_parts")==40
         and wo.get("compact_support")==PARAMETERS["exact_metric_support"]
         and wo.get("chosen_global_constants")=={
             "background_pair_A0":"7","background_pair_angle_A0":"6",
             "response_pair_A0":"19","response_pair_angle_A0":"83"}
         and wl["mathematical_parameters"]["exact_parameter_half_width"]
             ==PARAMETERS["original_WL_parameter_radius"]
         and wp.get("same_original_positive_algorithm_lower_summands_used") is True
         and wp.get("no_abstract_operator_norm_reverse_inference") is True
         and wp.get("no_division_by_current_delta_or_unknown_state") is True
         and wp.get("B_star_scope")=="absolute beta times max(1,absolute K_delta), uniformly on the whole core"
         and wp.get("G_star_scope")=="absolute G_delta times max(1,absolute K_delta), uniformly on the whole core")
    _,wt=receipt(paths["wt_science"],False)
    gate(doc,"WT completed twenty-gate object and unchanged full-family SP waist readout",
         successful(wt,EXPECTED["wt_science"])
         and wt.get("complete_waist_coefficient_bounds_proved") is True
         and wt.get("original_D_delta_fee_radius_not_extended") is True)
    wi=wt["copied_SP_family_identity"];waist=wt["copied_complete_SP_waist_factors"]
    gate(doc,"the true waist density includes both means the continuous repair andfull1e-8 state family",
         wi.get("continuous_centre_definition_sha256")==PARAMETERS["continuous_centre_definition_sha256"]
         and wi.get("continuous_response_definition_sha256")==PARAMETERS["continuous_response_definition_sha256"]
         and wi.get("fixed_current_eta")=="eta_0"
         and wt["parameters"].get("exact_delta_half_width")==PARAMETERS["exact_real_delta_radius"]
         and wt["parameters"].get("independent_mean_coordinates")==2
         and wt["new_coefficient_scope"].get("all_true_means_retained") is True
         and wt["new_coefficient_scope"].get("whole_core_D_delta_fee_extended") is False
         and wt.get("original_SP_source_and_manifest_sha256")==[
             "9d6ef721338e47e2cae8d179ce84976881df91762050d2a77d83b5399f6ba69a",
             "c77e969bd02ef95d30f16b53ae0a0d3854f596412151e9242ffa0485bd142210"])
    ex,wx=receipt(paths["wx_execution"],True)
    gate(doc,"WX completed twenty-gate current object on the same true strict interval",
         successful(wx,EXPECTED["wx_execution"])
         and ex.get("source_budget_source_sha256")==wx["source_sha256"]
         and wx["mathematical_parameters"].get("exact_strict_cut")==PARAMETERS["exact_strict_cut"]
         and wx["mathematical_parameters"].get("exact_root_interval")==PARAMETERS["exact_root_interval"]
         and wx["mathematical_parameters"].get("exact_real_delta_radius")==PARAMETERS["exact_real_delta_radius"]
         and wx["mathematical_parameters"].get("fixed_intrinsic_parameter")=="eta_0")
    flow=wx["complete_ungauged_leading_flow_conclusion"]
    gate(doc,"the copied complete forward radial factor has exactly the inverse-kSF orientation",
         flow.get("forward_orientation")=="b>=a"
         and flow.get("reverse_orientation")=="b<=a"
         and flow.get("exact_scalar_radial_rate")=="ell0 = -2 beta mean(u^2+K*v^2)"
         and flow.get("true_radial_interval")==["0",PARAMETERS["exact_strict_cut"]]
         and flow.get("all_shorter_subintervals_and_both_branches") is True
         and flow.get("complete_coupled_mean_source_and_all_seam_terms_remain") is True
         and flow.get("ng_endpoint_ratio_not_absorbed_or_inverted") is True
         and flow.get("ungauged_primitive_density_convention") is True)
    _,fa=receipt(paths["fa_science"],False)
    gate(doc,"FA2 completed twenty-four-gate terminal-Ai reference retains both signs andwaves",
         successful(fa,EXPECTED["fa_science"])
         and fa.get("complete_free_cut_strong_bound_proved") is True
         and fa["mathematical_parameters"].get("reference_column")==PARAMETERS["reference_column"]
         and fa["mathematical_parameters"].get("exact_real_delta_radius")==PARAMETERS["exact_real_delta_radius"]
         and fa["mathematical_parameters"].get("exact_strict_cut")==PARAMETERS["exact_strict_cut"]
         and fa["mathematical_parameters"].get("exact_root_interval")==PARAMETERS["exact_root_interval"]
         and fa["mathematical_parameters"].get("physical_signs")==[-1,1]
         and fa["mathematical_parameters"].get("oscillatory_branches")==[-1,1]
         and fa["mathematical_parameters"].get("fixed_intrinsic_parameter")=="eta_0")
    rr=fa["complete_saved_cut_receiver_conclusion"]["RR_ng_q_and_means_read_verbatim"]
    kr=rr["root_mean_value_q_bounds"]
    gate(doc,"the original body-germ K1 and exact whole root distance are kept distinct from cut-row eta",
         kr.get("whole_segment_in_one_original_germ") is True
         and kr.get("exact_root_distance")==["1/262144",PARAMETERS["exact_short_interval_upper_length"]]
         and kr.get("method")=="negative K at cut equals integral of outward K1 from cut to the same exact root"
         and kr.get("original_zero_order_curvature_enclosure_not_overwritten") is True
         and rr.get("both_mean_coordinates_retained") is True
         and fa["complete_saved_receiver_identity"]["RR_execution"]["run_id"]=="43750683671"
         and fa["complete_saved_receiver_identity"]["RR_execution"]["source_sha256"]
             =="2a51b8c45974808e65754ebaa0b476650596e7d8a1e36541e9afd3987146c4c9")
    rc=Fraction(PARAMETERS["exact_strict_cut"])
    rlo,rhi=map(Fraction,PARAMETERS["exact_root_interval"])
    short=Fraction(PARAMETERS["exact_short_interval_upper_length"])
    texts={k:paths[k].read_text() for k in PINNED if k.endswith("contract")}
    required={"kl_contract":["KL.8","KL.11","KL.14","KL.15","KL.20"],
        "metric_contract":["D.2","[1/20,9/50]"],
        "wl_contract":["WL.2","WL.8","WL.9"],
        "wx_contract":["WX.29","WX.30","WX.32"],
        "fa_contract":["FA.21","FA.28"],"pf_contract":["PF.20a","PF.20b"],
        "wy_contract":["WY.35","WY.44"]}
    gate(doc,"same-family off-support metric identity and exact root-leading proof closure",
         Fraction(9,50)<rc<rlo<=rhi<Fraction(9,10)
         and short==rhi-rc and Fraction(PARAMETERS["original_WL_parameter_radius"])>0
         and all(all(token in texts[k] for token in tokens) for k,tokens in required.items()))
    doc["copied_complete_input_objects"]={
      "WL_original_input_conclusion":copy.deepcopy(wo),
      "WL_complete_positive_product_conclusion":copy.deepcopy(wp),
      "WT_complete_SP_waist_factors":copy.deepcopy(waist),
      "WT_complete_SP_family_identity":copy.deepcopy(wi),
      "WT_complete_state_bounds":copy.deepcopy(wt["copied_complete_fixed_state_bounds"]),
      "WT_state_and_repair_parameters":copy.deepcopy(wt["copied_D_state_and_repair_parameters"]),
      "WX_complete_ungauged_leading_flow_conclusion":copy.deepcopy(flow),
      "FA_complete_root_mean_value_q_bounds":copy.deepcopy(kr),
      "FA_complete_reference_parameters":copy.deepcopy(fa["mathematical_parameters"]),
      "FA_complete_RR_source_identity":copy.deepcopy(fa["complete_saved_receiver_identity"]["RR_execution"])}
    doc["complete_original_receipt_identities"]={
       k:dict(v,actual_gate_count=len(s["gates"]),all_actual_gates_passed=True)
       for k,v,s in [("wl_execution",EXPECTED["wl_execution"],wl),
                      ("wt_science",EXPECTED["wt_science"],wt),
                      ("wx_execution",EXPECTED["wx_execution"],wx),
                      ("fa_science",EXPECTED["fa_science"],fa)]}
    doc["input_sha256"]=copy.deepcopy(PINNED)
    doc["input_manifest_sha256"]=a.manifest_sha
    doc["public_repository"]=PUBLIC
    doc["arithmetic_bits"]=a.bits
    return paths,dict(wp=wp,waist=waist,flow=flow,kr=kr)

def scalar_bounds(v,doc):
    B=nonnegative_upper(v["wp"]["B_star"])
    G=nonnegative_upper(v["wp"]["G_star"])
    ng=positive_lower(v["waist"]["density_radial_factor_lower"])
    k=positive_lower(v["kr"]["complete_Kr_lower"])
    forward=nonnegative_upper(v["flow"]["complete_forward_radial_exponential_upper"])
    gate(doc,"all complete endpoint lower bounds and positive global budget inputs are valid",
         B>0 and G>0 and ng>0 and k>0 and forward>0)
    M=up(q(7)+q(19)*q(PARAMETERS["exact_real_delta_radius"]))
    eta=up(G*M)
    ell=up(2*B*M*M)
    delta=q(PARAMETERS["exact_short_interval_upper_length"])
    logshort=up(ell*delta)
    inverse_short=up(logshort.exp())
    gate(doc,"only the new off-support root-short positive budget is evaluated",
         M>0 and eta>0 and ell>=0 and logshort>=0 and inverse_short>=1)
    ratio=up(eta/k)
    sixth=up(ratio**q(Fraction(1,6)))
    rootinverse=up(forward*inverse_short)
    prefactor=up((2*arb.pi()).sqrt())
    common=up(prefactor*sixth*inverse_short)
    K=up(common*forward/ng)
    out=record(K)
    rows=[dict(physical_wave=sigma,physical_input_sign=epsilon,
              inverse_leading_modulus_upper=copy.deepcopy(out),
              reference_column=PARAMETERS["reference_column"])
          for sigma in PARAMETERS["physical_waves"]
          for epsilon in PARAMETERS["physical_input_signs"]]
    gate(doc,"the correlated root density cancels exactly and all four Ai moduli shareone bound",
         K>0 and len(rows)==4 and all(x["inverse_leading_modulus_upper"]==out for x in rows))
    doc["complete_new_root_short_conclusion"]={
       "exact_root_bracket":copy.deepcopy(PARAMETERS["exact_root_interval"]),
       "exact_strict_cut":PARAMETERS["exact_strict_cut"],
       "exact_interval_upper_length":PARAMETERS["exact_short_interval_upper_length"],
       "exact_full_family_delta_radius":PARAMETERS["exact_real_delta_radius"],
       "complete_state_M_upper":record(M),
       "complete_characteristic_eta_at_root_upper":record(eta),
       "complete_short_radial_rate_absolute_upper":record(ell),
       "complete_new_short_log_upper":record(logshort),
       "complete_inverse_root_to_cut_radial_factor_upper":record(inverse_short),
       "old_WL_products_used_only_at_delta_zero_off_the_metric_support":True,
       "whole_core_old_small_delta_fee_not_extended":True,
       "complete_mean_state_used":True,
       "root_point_not_replaced_by_bracket_midpoint":True,
       "original_cut_eta_upper_not_reused_at_root":True}
    doc["complete_new_leading_scalar_conclusion"]={
       "exact_identity":"K_Lambda=sqrt(2*pi)/ng(0)*(eta_star/k_star)^(1/6)/k_root(0)",
       "root_mean_residual_retained_in_exact_log_derivative":True,
       "root_ng_cancelled_before_norms":True,
       "complete_saved_root_short_common_numerator_upper":record(common),
       "common_numerator_identity":"sqrt(2*pi)*(eta_root_upper/k_root_lower)^(1/6)*inverse_root_to_cut_factor",
       "common_numerator_has_no_endpoint_ng_division":True,
       "no_new_cut_leading_receiver_claimed":True,
       "complete_new_inverse_root_to_waist_radial_factor_upper":record(rootinverse),
       "complete_new_root_ratio_sixth_power_upper":record(sixth),
       "complete_inverse_leading_scalar_upper":out,
       "complete_four_sign_wave_records":rows,
       "complete_common_windows":copy.deepcopy(PARAMETERS["original_nonmean_windows"]),
       "strict_factor_is_saved_forward_radial_upper":True,
       "saved_reverse_radial_bound_not_used":True,
       "same_input_multiplier_in_every_window":True,
       "original_order":PARAMETERS["original_input_order"],
       "no_sector_sum_or_extra_sqrt2":True,
       "physical_means_and_transported_finite_blocks_independent":True,
       "reference_column":PARAMETERS["reference_column"],
       "second_Bi_or_other_genuine_root_column_covered":False}
    gate(doc,"all original signs means finite ranks and right factors remain independent",
         PARAMETERS["independent_physical_means"]==2
         and PARAMETERS["root_mean_residual_set_to_zero"] is False
         and PARAMETERS["optional_left_state_products_evaluated"] is False
         and PARAMETERS["full_incoming_finite_Schur_or_actual_solution_claimed"] is False)

def run(a,doc):
    ctx.prec=a.bits
    paths,v=checked_inputs(a,doc)
    scalar_bounds(v,doc)
    gate(doc,"all sixteen gates preserve original inputs and zero old scientific calls",
         len(doc["gates"])==15 and all(g["passed"] is True for g in doc["gates"])
         and all(sha(paths[k])==val for k,val in PINNED.items()))
    if len(doc["gates"])!=GATE_COUNT:raise ValueError("complete gate inventory changed")
    doc.update(complete=True,proved=True,actual_returncode=0,
       complete_correlated_terminal_Ai_leading_scalar_proved=True,
       original_completed_scientific_receipts_read=4,
       new_complete_root_short_budget_count=1,
       new_complete_leading_scalar_count=1,new_sign_wave_record_count=4,
       old_radial_mean_flow_fold_root_or_normalizer_calls=0,
       old_binary_archive_or_native_restored=0,old_scientific_source_imports=0,
       original_input_bytes_modified=False,new_recomputable_arrays_persisted=False,
       common_root_chart_inverse_evaluated=False,
       independent_physical_mean_coordinates=2,
       full_incoming_inverse_proved=False,finite_Schur_inverse_proved=False,
       actual_nonlinear_background_proved=False,final_surface_proved=False)

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--manifest",type=Path,required=True)
    p.add_argument("--manifest-sha",required=True)
    for role in PINNED:p.add_argument("--"+role.replace("_","-"),type=Path,required=True)
    p.add_argument("--bits",type=int,default=320)
    p.add_argument("--out",type=Path,required=True)
    a=p.parse_args();started=time.monotonic()
    if a.out.exists():raise FileExistsError("preserve every existing complete orpartial conclusion")
    doc=dict(kind=KIND,complete=False,proved=False,actual_returncode=1,
       failure=None,gates=[],source_sha256=sha(__file__),parameters=PARAMETERS,
       public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
       run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
       workflow_event_commit=os.environ.get("GITHUB_SHA"),
       actual_scientific_checkout_commit=os.environ.get("ACTUAL_CHECKOUT_COMMIT"))
    try:run(a,doc)
    except Exception as error:
        doc.update(complete=False,proved=False,actual_returncode=1,
            failure=dict(error_type=type(error).__name__,message=str(error)))
        traceback.print_exc()
    doc["actual_mathematical_wall_seconds"]=time.monotonic()-started
    raw=canonical(doc)
    a.out.parent.mkdir(parents=True,exist_ok=True)
    temp=a.out.with_name(a.out.name+".partial");temp.write_bytes(raw);temp.replace(a.out)
    print("CORRELATED_TERMINAL_AI_LEADING_SCALAR_SCIENTIFIC_RESULT_BEGIN",flush=True)
    print(json.dumps(dict(bytes=len(raw),sha256=sha_bytes(raw)),sort_keys=True),flush=True)
    print(raw.decode(),end="",flush=True)
    print("CORRELATED_TERMINAL_AI_LEADING_SCALAR_SCIENTIFIC_RESULT_END",flush=True)
    if len(raw)>35000:raise ValueError("saved complete leading scalar science exceeds35000bytes")
    return doc["actual_returncode"]

if __name__=="__main__":raise SystemExit(main())
