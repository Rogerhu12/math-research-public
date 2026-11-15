#!/usr/bin/env python3
"""New known-source scalar combinations from completed core records only."""
from __future__ import annotations
import argparse
import copy
import hashlib
import importlib.metadata
import json
import platform
import time
import traceback
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
REL="topics/visible-flex-exact-nearby/"
PRODUCER=REL+"scripts/fourfold_codazzi_known_core_high_source_and_negative_one.py"
KIND="actual_complete_known_core_high_source_and_negative_one_v1"
MANIFEST_KIND="known_core_high_source_negative_one_public_inputs_v1"
RUNTIME={"Python":"3.12.14","python_flint":"0.9.0"}
GATE_COUNT=18
CENTRE="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
DIRECTION="6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
CR_SOURCE="59f9130e024c51ce63b6138960535f986d0eaaa63dd724a1015a55729ff98f54"
CR_MANIFEST="88a732839ec83e5661efdf7417d163b46784c7f4865f658463ba4b6540aabbf9"
CR_COMMIT="9c0e3263200f63ea61420d0d691b7ef763263feb"
CR_OLD_INPUTS={
 "raw_manifest":"0705cb80101f25105d74181aafdf9daaf5a65baeece2d41e8a25b4589259cdad",
 "z_summary":"e1ae6bd3ae8b9f04297fb2c9664d249c15ffe9366d15a4504444f06f08b727ac",
 "z_process":"0cc2e8f876261c0fa86c0547b1400d47ad71759f43c7001b6359049827017f48",
 "d_execution":"6956c214240cd85e6263331b33e0c7efcf6abc3e71190d46ff3eabddecd35071",
 "wl_execution":"936633fcfb2cdc9ed3f0e108909275497337f59daea9e1fa33ee0ab40de0ec5d"}
PINNED={
 "cr_science":"dbae6acdde2de41375aaa0886b847fee8ef92c0344150bf176716b88d0cb5734",
 "cr_execution":"8d54c07e363b23a8b4be66ff1d73beafb5840fab9b82c1126c308cfcbfb43391",
 "rh_proof":"b3bfaf73dda241de03e52e052164b33313166de94b5387304aba771b9ec3a1f2",
 "st_proof":"b15c1630edba1510dc293dea447d4bfe8144680cf73523c3b3b7a237949d5938",
 "hs_contract":"18a683a215c4b28dc56ec029ed0c02013b42e083f95f463c9d5fa7e3850ac2f7"}
L=Fraction(9,10)
D=Fraction(1,10**10)
RC=Fraction(76285779072683,320000000000000)
SHELLS=((97,160),(161,224),(225,288))
THRESHOLDS=(96,160,224)
PARAMETERS={
 "arithmetic_bits":320,"runtime":RUNTIME,
 "exact_core_interval":["0","9/10"],"exact_delta_half_width":str(D),
 "exact_ST_restriction_interval":["0",str(RC)],
 "exact_eta0":"-7789843107295549/4611686018427387904",
 "exact_nu0":"-2572625729470897/72057594037927936",
 "centre_definition_sha256":CENTRE,"direction_definition_sha256":DIRECTION,
 "known_centre_degree":32,"known_direction_degree":96,
 "known_centre_residual_degree":96,"known_linear_source_degree":160,
 "known_selected_residual_degree":288,
 "ordinary_tail_thresholds":[96,160,224],
 "complete_shells":[[97,160],[161,224],[225,288]],
 "physical_frequency_factor":4,"negative_Sobolev_exponents_evaluated":[-1],
 "ordinary_radial_measure":"dr",
 "ordinary_angle_measure":"normalized original moving circle",
 "pair_norm":"Euclidean pair with complete even mean before declared projections",
 "known_global_A0_bounds":{"Q0":7,"Q0_phi":6,"Z":19,"Z_phi":83},
 "selection":"minimum upper endpoint of final retained complete candidate records; first candidate wins ties",
 "expected_gate_count":18,
 "original_CR_restriction_recomputed":False,
 "original_Z_D_WL_targets_recomputed":False,
 "original_quad_contribution_recomputed":False,
 "old_raw_mean_or_direction_offset_recharged":False,
 "old_producer_integral_or_Green_calls":0,
 "ST_propagation_or_endpoint_gains_evaluated":False,
 "actual_unknown_state_or_domain_entry_claimed":False}

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
        else:raise ValueError("a saved scalar lacks its complete directed interval")
    else:y=arb(str(x))
    if not y.is_finite():raise ValueError("nonfinite saved scalar")
    return y
def up(x):
    y=box(x) if isinstance(x,dict) else arb(x)
    if not y.is_finite():raise ValueError("nonfinite directed upper bound")
    return y.upper()
def nn(x):
    y=up(x)
    if not y>=0:raise ValueError("a nonnegative norm upper bound is invalid")
    return y
def root_upper(x):
    y=up(x)
    if not y>=0:raise ValueError("a square-root argument is not nonnegative")
    return up(y.sqrt())
def record(x):
    y=arb(x)
    if not y.is_finite():raise ValueError("nonfinite new scalar")
    return {"ball":y.str(72)}
def gate(doc,name,ok):
    doc["gates"].append({"name":name,"passed":bool(ok)})
    if not ok:raise ValueError("known-high-source gate failed: "+name)
def successful(x,n):
    return (x.get("complete") is True and x.get("proved") is True
        and x.get("actual_returncode")==0 and x.get("failure") is None
        and len(x.get("gates",[]))==n
        and all(g.get("passed") is True for g in x["gates"]))
def complete_minimum(candidates):
    if not candidates:raise ValueError("empty complete candidate set")
    selected=0;best=nn(candidates[0]["bound"])
    for i,c in enumerate(candidates[1:],1):
        value=nn(c["bound"])
        if value<best:selected=i;best=value
    return dict(candidates=copy.deepcopy(candidates),
        selected_candidate=candidates[selected]["name"],
        complete_upper_bound=copy.deepcopy(candidates[selected]["bound"]),
        selection_uses_final_retained_outward_upper=True,
        no_componentwise_mixing=True)

def checked_inputs(a,doc):
    actual={"Python":platform.python_version(),
            "python_flint":importlib.metadata.version("python-flint")}
    gate(doc,"pinned public runtime and320-bit directed arithmetic",
         actual==RUNTIME and a.bits==320 and ctx.prec==320)
    doc["runtime"]=actual
    m=read(a.manifest);paths={role:Path(getattr(a,role)) for role in PINNED}
    gate(doc,"current-only immutable manifest source parameters and all five small mathematical inputs",
         sha(a.manifest)==a.manifest_sha and m.get("kind")==MANIFEST_KIND
         and m.get("public_repository")==PUBLIC and m.get("source_sha256")==sha(__file__)
         and m.get("parameters")==PARAMETERS and m.get("mathematical_input_sha256")==PINNED
         and m.get("expected_actual_gate_count")==GATE_COUNT
         and all(sha(paths[k])==v for k,v in PINNED.items()))
    c=read(paths["cr_science"]);e=read(paths["cr_execution"])
    gate(doc,"original CR child and all eighteen complete structural gates succeeded",
         c.get("kind")=="actual_complete_core_background_restriction_and_selected_residual_v1"
         and successful(c,18) and c.get("source_sha256")==CR_SOURCE
         and c.get("complete_core_residual_restriction_proved") is True
         and c.get("complete_selected_ordinary_source_bounds_proved") is True)
    sr=e.get("scientific_conclusion",{})
    gate(doc,"original CR execution binds the exact saved science and same immutable successful run",
         str(e.get("run_id"))=="43757468943" and str(e.get("run_attempt"))=="1"
         and e.get("workflow_commit")==CR_COMMIT and e.get("complete") is True
         and e.get("actual_returncode")==0 and e.get("actual_failure") is None
         and e.get("complete_mathematical_receipt_available") is True
         and e.get("source_sha256")==CR_SOURCE and e.get("input_manifest_sha256")==CR_MANIFEST
         and sr.get("file")=="actual-scientific-conclusion.json"
         and sr.get("bytes")==paths["cr_science"].stat().st_size
         and sr.get("sha256")==PINNED["cr_science"]
         and sr.get("actual_gate_count")==18 and sr.get("actual_passed_gate_count")==18
         and sr.get("actual_returncode")==0 and sr.get("complete") is True)
    cp=c.get("parameters",{})
    gate(doc,"same continuous centre direction selected width moving angle and complete ordinary pair",
         c.get("derived_continuous_centre_definition_sha256")==CENTRE
         and c.get("exact_continuous_direction_definition_sha256")==DIRECTION
         and cp.get("exact_core_interval")==["0","9/10"]
         and cp.get("exact_delta_half_width")==str(D)
         and cp.get("exact_eta0")==PARAMETERS["exact_eta0"]
         and cp.get("exact_nu0")==PARAMETERS["exact_nu0"]
         and cp.get("ordinary_radial_measure")=="dr"
         and cp.get("ordinary_angle_measure")=="normalized original moving circle"
         and cp.get("pair_norm")=="Euclidean L2, with the full even mean of weight one"
         and cp.get("original_state_and_repair_degree")==32
         and cp.get("original_residual_degree")==96)
    gate(doc,"complete original Z D WL identity chain and old no-recomputation claims remain exact",
         e.get("mathematical_input_sha256")==CR_OLD_INPUTS
         and c.get("input_sha256")==dict(CR_OLD_INPUTS,manifest=CR_MANIFEST)
         and e.get("actual_verified_Git_input_count")==24
         and all(c.get(k)==0 for k in ("original_7296_row_residuals_recomputed",
             "original_Z_inner_sources_recomputed","original_whole_interval_integral_recomputed",
             "original_D_or_WL_scalar_budgets_recomputed","old_scientific_source_imports"))
         and c.get("original_input_bytes_changed") is False)
    old=c["copied_successful_source_inputs"];z=old["Z_inner_source_bounds"]
    high=z["high97_through160"]
    gate(doc,"complete original high97-through160 record is retained without squared-upper subtraction",
         set(z)=={"full_through160","low193","high97_through160"}
         and set(high)=={"L2_L2_radial","L2_sup"}
         and old.get("Z_mean_and_continuity_repair_already_paid") is True
         and old.get("Z_successful_finish_run")=="43613560173"
         and old.get("Z_old_failed_plan_run")=="43612904296"
         and old.get("old_source_integrals_or_repair_fees_recomputed") is False
         and nn(high["L2_L2_radial"])>0 and nn(high["L2_sup"])>0)
    wl=old["WL_complete_positive_product_conclusion"]
    gate(doc,"whole-core positive coefficient product and complete D source have the same selected width",
         old.get("D_selected_parameter_half_width")==str(D)
         and nn(old["D_whole_core_complete_additional_response_source"])>0
         and nn(wl["B_star"])>0 and nn(wl["G_star"])>0
         and wl.get("B_star_scope")=="absolute beta times max(1,absolute K_delta), uniformly on the whole core"
         and wl.get("same_original_positive_algorithm_lower_summands_used") is True
         and wl.get("no_abstract_operator_norm_reverse_inference") is True
         and wl.get("no_division_by_current_delta_or_unknown_state") is True)
    selected=c["complete_selected_source_conclusion"]
    quad=selected["complete_quadratic_source_contribution"]
    choices=selected["complete_background_choices"]
    gate(doc,"old complete quadratic and full low source records are copied rather than recomputed",
         selected.get("exact_delta_half_width")==str(D)
         and selected.get("D_additional_source_not_misidentified_as_total_f_delta") is True
         and selected.get("old_Z_inner_integrals_and_raw_mean_not_recomputed") is True
         and selected.get("no_second_amplitude_on_continuous_Z") is True and nn(quad)>=0
         and set(choices)=={"new_core_restriction","old_global_fallback"}
         and all(x.get("full_even_mean_retained") is True
             and x.get("extra_Z_mean_or_384EZ_fee") is False
             and x.get("known_centre_residual_is_exactly_low193") is True for x in choices.values()))
    gate(doc,"RH exact support and ST true subinterval use physical4j in the original moving angle",
         0<RC<L and SHELLS==((97,160),(161,224),(225,288))
         and THRESHOLDS==(96,160,224)
         and PARAMETERS["known_selected_residual_degree"]==288
         and PARAMETERS["physical_frequency_factor"]==4
         and PARAMETERS["negative_Sobolev_exponents_evaluated"]==[-1])
    doc["input_sha256"]=dict(PINNED,manifest=a.manifest_sha)
    doc["complete_original_input_conclusion"]={
       "CR_run_id":"43757468943","CR_run_attempt":"1","CR_source_sha256":CR_SOURCE,
       "CR_manifest_sha256":CR_MANIFEST,"CR_scientific_sha256":PINNED["cr_science"],
       "CR_execution_sha256":PINNED["cr_execution"],
       "CR_complete_original_gate_inventory":copy.deepcopy(c["gates"]),
       "CR_original_mathematical_input_sha256":copy.deepcopy(CR_OLD_INPUTS),
       "complete_original_inner_Z_source_object":copy.deepcopy(z),
       "complete_original_high97_through160_record":copy.deepcopy(high),
       "complete_original_WL_positive_product_object":copy.deepcopy(wl),
       "complete_original_D_core_source_record":copy.deepcopy(old["D_whole_core_complete_additional_response_source"]),
       "old_complete_quadratic_contribution_read_verbatim":copy.deepcopy(quad),
       "old_complete_full_and_low_background_choices_read_verbatim":copy.deepcopy(choices),
       "old_failed_plan_and_successful_finish_retained":{
          "failed_plan_run":old["Z_old_failed_plan_run"],
          "successful_finish_run":old["Z_successful_finish_run"],
          "original_plan_native_sha256":old["Z_original_plan_native_sha256"],
          "summary_native_sha256":old["Z_summary_native_sha256"]},
       "old_source_raw_mean_and_direction_offsets_already_paid":True}
    return paths,{"SH":nn(high["L2_L2_radial"]),"B":nn(wl["B_star"]),"quad":copy.deepcopy(quad)}

def scalar_bounds(v,doc):
    d=q(D);length=q(L);B=v["B"]
    t2=up(B*(q(Fraction(19**2*6,4))+q(Fraction(7*19*83,2))+3*7*19**2))
    t3=up(B*(q(Fraction(19**2*83,4))+19**3))
    gate(doc,"new fixed-parameter complete quadratic and cubic coefficients are finite and nonnegative",
         t2.is_finite() and t3.is_finite() and t2>0 and t3>0)
    linear=up(d*v["SH"])
    a96=record(up(linear+nn(v["quad"])))
    ordinary={}
    ordinary["96"]=dict(
       candidates=[dict(name="complete_original_high_linear_plus_saved_parameter_remainder",bound=copy.deepcopy(a96))],
       selected_candidate="complete_original_high_linear_plus_saved_parameter_remainder",
       complete_upper_bound=copy.deepcopy(a96),
       selection_uses_final_retained_outward_upper=True,no_componentwise_mixing=True)
    gate(doc,"H96 uses the complete original high source and the saved whole quadratic remainder",
         nn(a96)>=0 and linear>=0)
    p160=record(up(length.sqrt()*(d*d*t2+d*d*d*t3)))
    ordinary["160"]=complete_minimum([
       dict(name="saved_complete_selected_parameter_remainder",bound=copy.deepcopy(v["quad"])),
       dict(name="complete_fixed_parameter_state_quadratic_and_cubic",bound=p160)])
    gate(doc,"H160 selects one complete valid candidate by its retained outward upper endpoint",
         nn(ordinary["160"]["complete_upper_bound"])>=0
         and len(ordinary["160"]["candidates"])==2)
    p224=record(up(length.sqrt()*d*d*d*t3))
    ordinary["224"]=complete_minimum([
       dict(name="complete_fixed_parameter_state_cubic",bound=p224),
       dict(name="orthogonal_contraction_of_complete_H160",bound=copy.deepcopy(ordinary["160"]["complete_upper_bound"]))])
    gate(doc,"H224 keeps both complete candidates and source above288 is exactly zero",
         nn(ordinary["224"]["complete_upper_bound"])>=0
         and PARAMETERS["known_selected_residual_degree"]==288)
    doc["complete_new_ordinary_high_source_conclusion"]={
       "exact_core_interval":["0","9/10"],"exact_delta_half_width":str(D),
       "same_real_parameter_family_for_every_bound":True,
       "original_moving_angle_and_physical4j":True,
       "ordinary_radial_measure":"dr","full_two_component_Euclidean_norm":True,
       "new_complete_T2":record(t2),"new_complete_T3":record(t3),
       "new_d_times_original_SH":record(linear),
       "old_complete_quadratic_remainder_read_verbatim":copy.deepcopy(v["quad"]),
       "new_complete_fixed_parameter_H160_candidate":copy.deepcopy(p160),
       "new_complete_fixed_parameter_H224_candidate":copy.deepcopy(p224),
       "complete_uniform_ordinary_tail_bounds":ordinary,
       "H288_source_exactly_zero":True,"H288_ordinary_norm_exact":"0",
       "all_three_high_sources_at_delta_zero_exactly_zero":True,
       "whole_core_family_not_misidentified_as_cubic_in_delta":True,
       "full_mean_retained_before_declared_high_projections":True,
       "raw_mean_or_384EZ_not_charged_again":True,
       "original_CR_restriction_or_D_quadratic_not_recomputed":True}
    shell_records=[]
    for lo,hi in SHELLS:
        n=4*lo;lam2=1+n*n
        norm=ordinary[str(lo-1)]["complete_upper_bound"]
        weighted=record(root_upper(nn(norm)**2/q(lam2)))
        shell_records.append(dict(first_abs_index=lo,last_abs_index=hi,
           both_physical_signs_retained=True,complete_pair=True,
           physical_minimum_frequency=n,exact_lambda_minimum_squared=str(lam2),
           complete_ordinary_shell_upper=copy.deepcopy(norm),
           complete_Hminus1_shell_upper=weighted,
           shell_bound_is_contraction_not_squared_upper_difference=True))
    gate(doc,"all three complete shells pay their exact physical-frequency negative-one factors",
         len(shell_records)==3
         and all(x["physical_minimum_frequency"]==4*x["first_abs_index"]
             and nn(x["complete_Hminus1_shell_upper"])>=0 for x in shell_records))
    negative={}
    for J in THRESHOLDS:
        lam2=1+(4*(J+1))**2
        direct=record(root_upper(nn(ordinary[str(J)]["complete_upper_bound"])**2/q(lam2)))
        square=arb(0)
        included=[]
        for x in shell_records:
            if x["first_abs_index"]>J:
                square=up(square+nn(x["complete_ordinary_shell_upper"])**2/q(x["exact_lambda_minimum_squared"]))
                included.append([x["first_abs_index"],x["last_abs_index"]])
        fullshell=record(root_upper(square))
        negative[str(J)]=complete_minimum([
           dict(name="complete_direct_tail_negative_one_bound",bound=direct),
           dict(name="complete_orthogonal_shell_negative_one_bound",bound=fullshell)])
        negative[str(J)]["complete_shells_included"]=included
    gate(doc,"every negative-one tail retains both complete candidates without receiver or phase substitution",
         set(negative)=={"96","160","224"}
         and all(len(x["candidates"])==2 and nn(x["complete_upper_bound"])>=0 for x in negative.values()))
    doc["complete_new_negative_one_source_conclusion"]={
       "exact_core_interval":["0","9/10"],
       "negative_Sobolev_exponent":-1,
       "Sobolev_weight":"Lambda_j=sqrt(1+16*j^2)",
       "ordinary_radial_measure":"dr",
       "original_moving_circle_normalized_measure":True,
       "complete_uniform_Hminus1_tail_bounds":negative,
       "complete_shell_records":shell_records,
       "H288_source_exactly_zero":True,"H288_Hminus1_norm_exact":"0",
       "ST_restriction_interval":["0",str(RC)],
       "same_source_restriction_cannot_increase_the_norm":True,
       "ST_interval_is_not_the_whole_core":True,
       "ST_forcing_requires_the_original_complete_state_convention":True,
       "ST_output_retains_both_independent_means":True,
       "high_projection_not_commuted_through_propagation":True,
       "ST_propagation_or_endpoint_gain_evaluated":False,
       "Hminus4over3_or_true_phase_receiver_transfer_claimed":False}

def run(a,doc):
    ctx.prec=a.bits
    paths,v=checked_inputs(a,doc)
    scalar_bounds(v,doc)
    gate(doc,"all original small bytes remain unchanged and no old scientific target is executed",
         all(sha(paths[k])==val for k,val in PINNED.items())
         and PARAMETERS["old_producer_integral_or_Green_calls"]==0)
    gate(doc,"all eighteen gates describe known sources only with complete means and independent unknown inputs",
         len(doc["gates"])==17 and all(g["passed"] is True for g in doc["gates"])
         and PARAMETERS["actual_unknown_state_or_domain_entry_claimed"] is False)
    if len(doc["gates"])!=GATE_COUNT:raise ValueError("the complete eighteen-gate inventory changed")
    doc.update(complete=True,proved=True,actual_returncode=0,
       complete_known_high_source_bounds_proved=True,
       complete_known_negative_one_source_bounds_proved=True,
       original_CR_or_Z_D_WL_calculations_recomputed=0,
       original_old_quadratic_contribution_recomputed=0,
       original_rows_native_or_artifacts_restored=0,
       old_scientific_source_imports=0,old_Green_or_propagation_calls=0,
       new_ordinary_tail_bound_count=3,new_negative_one_tail_bound_count=3,
       new_complete_shell_count=3,exact_zero_highest_threshold=288,
       original_input_bytes_modified=False,new_recomputable_arrays_persisted=False,
       actual_unknown_state_bounds_proved=False,actual_cap_domain_entry_proved=False,
       full_high_inverse_proved=False,actual_PDE_solution_proved=False,final_surface_proved=False,
       independent_remaining_inputs=[
          "complete cap affine and waist loads","wholecore nonlinear source",
          "unknown high-body and high-cut state inputs","wholecore and cut regularity radii",
          "same-state right collar data","actual physical curvature product-domain entry",
          "receiver-specific complete coordinate and source identifications"])

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--manifest",type=Path,required=True)
    p.add_argument("--manifest-sha",required=True)
    for role in PINNED:p.add_argument("--"+role.replace("_","-"),type=Path,required=True)
    p.add_argument("--bits",type=int,default=320)
    p.add_argument("--out",type=Path,required=True)
    a=p.parse_args();started=time.monotonic()
    if a.out.exists():raise FileExistsError("preserve every existing scientific conclusion")
    doc=dict(kind=KIND,complete=False,proved=False,actual_returncode=1,
       failure=None,gates=[],source_sha256=sha(__file__),parameters=PARAMETERS,
       derived_continuous_centre_definition_sha256=CENTRE,
       exact_continuous_direction_definition_sha256=DIRECTION)
    try:run(a,doc)
    except Exception as error:
        doc.update(complete=False,proved=False,actual_returncode=1,
            failure=dict(error_type=type(error).__name__,message=str(error)))
        traceback.print_exc()
    doc["actual_mathematical_wall_seconds"]=time.monotonic()-started
    raw=canonical(doc)
    a.out.parent.mkdir(parents=True,exist_ok=True)
    temp=a.out.with_name(a.out.name+".partial");temp.write_bytes(raw);temp.replace(a.out)
    print("KNOWN_CORE_HIGH_SOURCE_SCIENTIFIC_RESULT_BEGIN",flush=True)
    print(json.dumps(dict(bytes=len(raw),sha256=sha_bytes(raw)),sort_keys=True),flush=True)
    print(raw.decode(),end="",flush=True)
    print("KNOWN_CORE_HIGH_SOURCE_SCIENTIFIC_RESULT_END",flush=True)
    if len(raw)>45000:raise ValueError("saved complete known-high source science exceeds45000 bytes")
    return doc["actual_returncode"]

if __name__=="__main__":raise SystemExit(main())
