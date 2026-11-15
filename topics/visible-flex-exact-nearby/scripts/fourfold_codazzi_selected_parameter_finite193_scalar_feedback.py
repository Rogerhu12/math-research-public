#!/usr/bin/env python3
"""Directed scalar finite193 feedback from complete small public conclusions.

This consumer does not regenerate any row, matrix, Gram, target, Fourier
product, residual integral or phase operator. New numerical arithmetic is
intended only for the public Actions runner. A negative sufficient feedback
verdict is a completed scalar result, not a singularity claim.
"""
from __future__ import annotations
import argparse,hashlib,json,os,time,traceback
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx

REL="topics/visible-flex-exact-nearby/"
PRODUCER=REL+"scripts/fourfold_codazzi_selected_parameter_finite193_scalar_feedback.py"
KIND="actual_selected_parameter_finite193_scalar_feedback_from_complete_Green_v1"
GREEN_KIND="actual_ephemeral_parallel_finite193_Green_true97_Poisson_same97_cap_v4"
GREEN_SOURCE="ba931a8a1d9897d3ef8d341b7b441a72e991e4955983c9c5eb51716a9fe49b9c"
GREEN_WORKER="f67d62e223891143dc80645acfba21ca28e18d1fde4fbe04f933ba69905a4b0b"
GREEN_MANIFEST="42810dfa5a313ede72bcedb34c7cbf9ecd2f1f7fa65e9b23c7ab79d8b01f2952"
GREEN_RUN="43711315338"
GREEN_CHILD="actual_ephemeral_missing_future_past_true97_Poisson_and_same97_contraction"
CUT_KIND="actual_complete_selected_cut_shape_mean_scalar_conclusion_v1"
CUT_PROCESS_KIND="actual_public_selected_cut_shape_mean_process_v1"
CUT_SOURCE="745fc480b101dbd7ca035c11826d2d0208c4d2db3568e0bbb4214fa401ddbb19"
CUT_WORKER="c7c83418a890245f224a04e7dc41dadaa80eee7223c00c7a1f1c458eda3eecce"
CUT_MANIFEST="95541c2e2bd7cd7547d13319fdacdaf3a0d8ba1eb1ac675fd4d68480b6994b57"
CUT_RUN="43715426316"
CUT_SUMMARY_SHA="5d74a0f24afe7d490cd17f04f0c0ea5efb671fd277ced502269f4d94c748a413"
CUT_PROCESS_SHA="82b7c37637c9ebec074ae7647595200c2cd790cf19728ef0e4d93a8452e59812"
CUT_CHILD="selected_cut_shape_mean"
SHAPE_CAP_PROOF="06ec6f0a405e89b456342b1a2260c9fae18de192733fae1c35c913a037373892"
SCALAR_EXECUTION="6956c214240cd85e6263331b33e0c7efcf6abc3e71190d46ff3eabddecd35071"
SCALAR_SOURCE="827fcb237a79b48c095872b61c370ff2ceafc143a8dc6a1774021188ff3ea320"
SCALAR_MANIFEST="14271d7d61c70996092f105768ca29cc0dd355665be0becea4386441b38c907f"
CENTRE="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
DIRECTION="6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
B="whole_inner_body"
N="fixed_complete_negative_phase_window"
C="true_cut_trace"
WINDOWS=(B,N,C)
PHASE_RIGHT="2383968743003/10000000000000"
BOUNDARY_UNITS="original97 regular row Euclidean coordinates; no second rho input weight"
COUNTS=dict(future=5970,past=5970,product=5970,ports=5970,groups=187)
PARAMETERS=dict(
    arithmetic_bits=320,exact_core_interval=["0","9/10"],
    exact_negative_output_interval=["0",PHASE_RIGHT],
    delta_half_width="1/10000000000",response_pair_A0="19",response_pair_angle_A0="83",
    head_physical_frequency=384,new_cross_physical_frequency=1152,
    physical_cap_comparisons=[
        dict(name="fixed_original_physical_cap",kappa="0",actual_cap_domain_hypotheses_required=False),
        dict(name="actual_physical_cap_under_its_proved_domain",kappa="1/5",actual_cap_domain_hypotheses_required=True)],
    complete_ordinary_source_domain="whole core [0,9/10]; normalized circle; full pair and even mean",
    exact_original_right_row_units=BOUNDARY_UNITS,
    original_science_recomputed=0,negative_sufficient_gate_is_complete_diagnosis=True,
    complete_shape_mean_cut_bounds_required=True,
    coordinate_row_bounds_combined_only_as_complete_operator_bounds=True,
    exact_response_repair_not_charged_again=True,
    infinite_inverse_or_true_parameter_Schur_claimed=False)

def sha_bytes(data):return hashlib.sha256(data).hexdigest()
def sha(path):return sha_bytes(Path(path).read_bytes())
def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,
                       allow_nan=False)+"\n").encode("utf-8")
def read(path):
    data=Path(path).read_bytes()
    if len(data)>100000:raise ValueError("only pinned small UTF8 records are admitted")
    return json.loads(data)
def save(path,value):
    data=canonical(value)
    if len(data)>60000:raise ValueError("the complete scalar conclusion exceeds 60000 bytes")
    p=Path(path);p.parent.mkdir(parents=True,exist_ok=True)
    tmp=p.with_name(p.name+".partial");tmp.write_bytes(data);tmp.replace(p)
def q(value):
    z=Fraction(value);return arb(z.numerator)/z.denominator
def box(value):
    if isinstance(value,arb):z=value
    elif isinstance(value,(int,Fraction)):z=q(value)
    elif isinstance(value,str):z=arb(value)
    elif isinstance(value,dict) and "ball" in value:z=arb(value["ball"])
    elif isinstance(value,dict) and "lower" in value and "upper" in value:
        z=arb(value["lower"]).lower().union(arb(value["upper"]).upper())
    else:raise ValueError("a scalar lacks its full directed interval")
    if not z.is_finite():raise ValueError("nonfinite directed scalar")
    return z
def upper(value):return box(value).upper()
def lower(value):return box(value).lower()
def bound(value,label):
    z=box(value)
    if z.lower()<0:raise ValueError("negative purported nonnegative bound: "+label)
    return z.upper()
def rec(value):return dict(ball=box(value).str(64))
def encode(value):
    if isinstance(value,arb):return rec(value)
    if isinstance(value,dict):return {str(k):encode(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)):return [encode(v) for v in value]
    return value
def gate(doc,name,condition):
    doc["gates"].append(dict(name=name,passed=bool(condition)))
    if not condition:raise ValueError("finite feedback input/evaluation gate: "+name)
def completed_science(value):
    return (value.get("complete") is True and value.get("failure") is None
        and isinstance(value.get("gates"),list) and bool(value["gates"])
        and all(g.get("passed") is True for g in value["gates"]))

def inputs(a,doc):
    gate(doc,"the exact new manifest and directed precision are fixed",
        sha(a.manifest)==a.manifest_sha and a.bits==PARAMETERS["arithmetic_bits"])
    manifest=read(a.manifest)
    gate(doc,"the declared scalar parameters and source bytes are unchanged",
        manifest.get("parameters")==PARAMETERS
        and manifest.get("files",{}).get(PRODUCER)==sha(__file__))
    root=a.root.resolve();receipts=[]
    files=manifest.get("file_receipts",[])
    if not files or len(files)!=len(manifest["files"]):
        raise ValueError("incomplete pinned small-file inventory")
    seen=set()
    for row in files:
        name=row["path"]
        if name in seen or not name.startswith(REL) or ".." in Path(name).parts:
            raise ValueError("a pinned small path is repeated or leaves the topic")
        p=(root/name).resolve()
        if not p.is_relative_to(root) or not p.is_file():
            raise ValueError("a pinned small file is absent from the immutable tree")
        data=p.read_bytes()
        if (len(data)!=row["bytes"] or len(data)>100000
            or sha_bytes(data)!=row["sha256"] or manifest["files"].get(name)!=row["sha256"]):
            raise ValueError("a complete pinned small input changed")
        data.decode("utf-8");seen.add(name);receipts.append(row)
    gate(doc,"every exact small input is present without native arrays or old recomputation",
        seen==set(manifest["files"]))
    paths=manifest.get("input_paths",{})
    if set(paths)!={"green_process","green_summary","scalar_execution","cut_process","cut_summary"}:
        raise ValueError("the five exact completed small scientific records are required")
    if any(p not in seen for p in paths.values()):
        raise ValueError("an actual scientific record was not pinned")
    actual={k:root/v for k,v in paths.items()}
    if sha(actual["scalar_execution"])!=SCALAR_EXECUTION:
        raise ValueError("the completed selected-parameter scalar execution changed")
    execution=read(actual["scalar_execution"])
    scalar=execution.get("actual_scientific_receipt",{})
    gate(doc,"the selected-parameter scalar child actually completed all original identity and coverage gates",
        str(execution.get("run_id"))=="43713242980"
        and str(execution.get("run_attempt"))=="1"
        and execution.get("complete") is True and execution.get("actual_returncode")==0
        and execution.get("actual_failure") is None
        and execution.get("source_budget_source_sha256")==SCALAR_SOURCE
        and execution.get("input_manifest_sha256")==SCALAR_MANIFEST
        and completed_science(scalar) and scalar.get("actual_returncode")==0
        and scalar.get("source_sha256")==SCALAR_SOURCE
        and scalar.get("input_manifest_sha256")==SCALAR_MANIFEST
        and scalar.get("complete_selected_parameter_body_scalar_fees_proved") is True
        and len(scalar["gates"])==12 and scalar.get("complete_original_rows_verified")==7721
        and len(scalar.get("original_part_receipts",[]))==40
        and scalar.get("old_target_Fourier_cubic_mean_residual_integral_or_Green_calls")==0
        and scalar.get("derived_continuous_centre_definition_sha256")==CENTRE
        and scalar.get("derived_continuous_response_definition_sha256")==DIRECTION)
    fees=scalar.get("selected_parameter_operator_fees",{})
    whole=scalar["complete_scalar_fee_conclusions"]["whole_core"]
    gate(doc,"the completed fees are whole-core ordinary suprema, not negative-window or integrated coefficient substitutions",
        fees.get("exact_core_interval")==["0","9/10"]
        and fees.get("ordinary_input")=="L2_r L2_phi with complete independent mean"
        and fees.get("source_head_physical_frequency")==384
        and fees.get("source_high_to_low_physical_frequency")==1152
        and fees.get("no_post_composition_or_phase_support_claimed") is True
        and fees.get("e")==whole["maxima"]["e_LL"]
        and fees.get("e_LH")==whole["maxima"]["e_LH"]
        and whole.get("exact_interval")==["0","9/10"]
        and scalar["parameters"]["delta_half_width"]==PARAMETERS["delta_half_width"]
        and scalar["chosen_global_constants"]==dict(background_pair_A0="7",
            background_pair_angle_A0="6",response_pair_A0="19",response_pair_angle_A0="83"))
    if sha(actual["cut_process"])!=CUT_PROCESS_SHA or sha(actual["cut_summary"])!=CUT_SUMMARY_SHA:
        raise ValueError("the original complete cut process or conclusion bytes changed")
    cut_process=read(actual["cut_process"]);cut=read(actual["cut_summary"])
    cut_children=[v for v in cut_process.get("children",[]) if v.get("label")==CUT_CHILD]
    gate(doc,"the exact shape and mean cut child completed its own original gates before consumption",
        str(cut_process.get("run_id"))==CUT_RUN and str(cut_process.get("run_attempt"))=="1"
        and cut_process.get("kind")==CUT_PROCESS_KIND
        and cut_process.get("repository")=="Rogerhu12/math-research-public"
        and cut_process.get("worker_source_sha256")==CUT_WORKER
        and cut_process.get("actual_source_sha256")==CUT_SOURCE
        and cut_process.get("input_manifest_sha256")==CUT_MANIFEST
        and len(cut_children)==1 and cut_children[0].get("actual_returncode")==0
        and cut_process.get("actual_scientific_complete") is True
        and cut_process.get("actual_scientific_failure") is None
        and cut_process.get("actual_scientific_summary_sha256")==sha(actual["cut_summary"])
        and cut_process.get("actual_scientific_summary_bytes")==actual["cut_summary"].stat().st_size
        and cut_process.get("actual_scientific_gates")==cut.get("gates")
        and cut.get("kind")==CUT_KIND and cut.get("source_sha256")==CUT_SOURCE
        and cut.get("input_sha256",{}).get("manifest")==CUT_MANIFEST
        and completed_science(cut) and len(cut["gates"])==9)
    cut_scope=cut.get("original_input_scope",{});cut_parameters=cut.get("parameters",{})
    gate(doc,"the full cut shape retains its signed base, repaired mean and original unscaled units",
        cut_scope.get("same_true_cut")=="9/10" and cut_scope.get("raw_side")=="left"
        and cut_scope.get("derived_continuous_direction_definition_sha256")==DIRECTION
        and cut_scope.get("base_endpoint_continuity_from_exact_repair") is True
        and cut_scope.get("base_whole_eta_box_used_only_as_enclosure_of_fixed_eta0") is True
        and cut_scope.get("complete_response_mean_flow_correction_not_consumed") is True
        and cut.get("original_response_slots")==dict(odd_nonmean=96,even_mean=1,even_nonmean=96)
        and cut.get("all_193_raw_amplitudes_used_before_absolute_values") is True
        and cut.get("known_base32_shape_subtracted_before_norm") is True
        and cut.get("physical_response_alpha_factor_applied") is False
        and cut.get("exact_continuous_response_offset_paid_once") is True
        and cut.get("mean_corrected_qstar_not_substituted_for_Z") is True
        and cut.get("actual_new_scalar_coefficient_consumption_complete") is True
        and cut.get("old_target_trial_angle_repair_matrix_Green_recomputations")==0
        and cut.get("old_native_bytes_changed")==0
        and cut.get("no_core_existence_unknown_correction_or_low_selfmap_claim") is True
        and cut_parameters.get("exact_cut")=="9/10"
        and cut_parameters.get("delta_half_width")==PARAMETERS["delta_half_width"]
        and cut_parameters.get("response_repair_pair_A0")=="0.0000000000000002292"
        and cut_parameters.get("physical_response_amplitudes_not_scaled_by_alpha") is True
        and SHAPE_CAP_PROOF in manifest["files"].values())
    process=read(actual["green_process"]);green=read(actual["green_summary"])
    children=[v for v in process.get("children",[]) if v.get("label")==GREEN_CHILD]
    gate(doc,"the exact Green v4 child really finished successfully before any scalar consumption",
        str(process.get("run_id"))==GREEN_RUN and str(process.get("run_attempt"))=="1"
        and process.get("worker_source_sha256")==GREEN_WORKER
        and process.get("input_manifest_sha256")==GREEN_MANIFEST
        and process.get("actual_source_sha256")==GREEN_SOURCE
        and len(children)==1 and children[0].get("actual_returncode")==0
        and process.get("actual_scientific_complete") is True
        and process.get("actual_scientific_failure") is None
        and process.get("actual_output_sha256")==green.get("output_sha256")
        and green.get("kind")==GREEN_KIND and green.get("source_sha256")==GREEN_SOURCE
        and completed_science(green))
    gate(doc,"the complete Green result retains all true ports, mean rows and independent high inputs",
        green.get("exact_inner_interval")==["0","9/10"]
        and green.get("exact_negative_output_interval")==["0",PHASE_RIGHT]
        and green.get("exact_boundary_input_units")==BOUNDARY_UNITS
        and green.get("input_sha256")==process.get("actual_input_sha256")
        and green.get("complete_finite193_directional_two_boundary_bound_proved") is True
        and green.get("complete97_input_Poisson_Gram_bound_proved") is True
        and green.get("complete_true_right_Poisson_contraction_proved") is True
        and green.get("independent_full_high_body_and_high_cut_inputs_retained") is True
        and green.get("complete_infinite_BVP_inverse_proved") is False
        and green.get("true_parameter_Schur_proved") is False
        and green.get("old_future_rows_recomputed")==0
        and green.get("old_target_F_C_Gram_or_validator_calls")==0
        and green.get("new_recomputable_arrays_persisted") is False
        and green.get("actual_true97_normalization",{}).get("full_mean_preserved") is True)
    phases=green.get("actual_phase_output_hashes",{})
    complete_counts={k:v.get("complete_state_files") for k,v in phases.items()}
    parallel=green.get("actual_parallel_completion",{})
    gate(doc,"all four 5970 phase covers and all 187 groups have complete original receipt identities",
        complete_counts==COUNTS
        and all(v.get("arrays_bound_by_each_original_exact_receipt") is True
            and v.get("persisted_recomputable_output") is False
            and isinstance(v.get("ordered_exact_state_receipts_sha256"),str)
            and len(v["ordered_exact_state_receipts_sha256"])==64 for v in phases.values())
        and parallel.get("complete_local_groups")==187
        and parallel.get("original_future_rows_reused")==1886
        and parallel.get("new_future_rows")==4084
        and parallel.get("new_past_rows")==5970
        and parallel.get("new_unnormalized_Poisson_product_rows")==5970
        and green.get("exact_original_future_prefix",{}).get("complete_rows")==1886)
    doc["input_sha256"]={k:sha(v) for k,v in actual.items()}
    doc["input_manifest_sha256"]=sha(a.manifest)
    doc["complete_small_input_inventory_sha256"]=sha_bytes(canonical(receipts))
    doc["actual_original_Green_run"]=dict(run_id=GREEN_RUN,run_attempt="1",
        source_sha256=GREEN_SOURCE,worker_sha256=GREEN_WORKER,input_manifest_sha256=GREEN_MANIFEST,
        native_output_sha256=green["output_sha256"],native_output_bytes=green["output_bytes"],
        native_read_or_recomputed=False,actual_phase_output_hashes=phases,
        original1886_recomputed=0,complete_counts=complete_counts)
    doc["actual_original_scalar_run"]=dict(run_id="43713242980",run_attempt="1",
        execution_sha256=SCALAR_EXECUTION,source_sha256=SCALAR_SOURCE,
        manifest_sha256=SCALAR_MANIFEST,original_closed_rows_recomputed=0)
    doc["actual_original_cut_run"]=dict(run_id=CUT_RUN,run_attempt="1",
        source_sha256=CUT_SOURCE,worker_sha256=CUT_WORKER,manifest_sha256=CUT_MANIFEST,
        process_sha256=sha(actual["cut_process"]),summary_sha256=sha(actual["cut_summary"]),
        actual_gate_count=len(cut["gates"]),old_native_read_or_recomputed=False,
        known_shape_was_subtracted_before_norm=True,continuous_mean_retained=True)
    doc["derived_continuous_centre_definition_sha256"]=CENTRE
    doc["derived_continuous_response_definition_sha256"]=DIRECTION
    return green,scalar,cut

def columns(green,doc):
    generic=green["posterior_complete_true_Green_constants"]
    poisson=green["complete_true_right_Poisson_operator_upper"]
    body=green["complete_true_finite193_body_high_to_low_bounds"]
    cap=green["complete_same_input_directional_contractions"]
    gate(doc,"all three actual output windows have complete separately typed columns",
        all(set(d)==set(WINDOWS) for d in (generic,poisson,body,cap))
        and all(cap[w].get("signed_trace_before_final_upper") is True
            and cap[w].get("selected_complete_contraction") in cap[w].get("all_complete_contraction_choices",{})
            and cap[w]["complete_operator_upper"]==cap[w]["all_complete_contraction_choices"][
                cap[w]["selected_complete_contraction"]]["operator_upper"] for w in WINDOWS))
    result={}
    for w in WINDOWS:
        result[w]=dict(g=bound(generic[w]["body"],"generic ordinary source "+w),
            p=bound(poisson[w],"complete true97 Poisson "+w),
            a=bound(body[w],"complete old body-cross "+w),
            c=bound(cap[w]["complete_operator_upper"],"complete signed old high-cap "+w))
    doc["original_complete_columns"]=encode(result)
    doc["original_complete_cap_contraction_choices"]={
        w:dict(selected_complete_contraction=cap[w]["selected_complete_contraction"],
            selected_complete_operator_upper=cap[w]["complete_operator_upper"],
            signed_trace_before_final_upper=True) for w in WINDOWS}
    doc["ordinary_source_input_domain"]=PARAMETERS["complete_ordinary_source_domain"]
    doc["actual_cut_gain_is_not_a_body_L2_trace"]=True
    doc["specialized_cross_a_substituted_for_generic_g"]=False
    return result

def legacy_boundary_constants():
    d=q(PARAMETERS["delta_half_width"]);E0=19*d;E1=83*d
    j=q("1.015211829")+17*E0/24;m=q("5.8639401366")+E0
    C0=q(".318181201")+E0/8;C1=q(".020269146")+E0+E1/4
    rootj=j.sqrt();s=upper(m*rootj);c=upper(rootj*(C0*C0+C1*C0/4))
    scale=upper(max(arb(1),s)*c)
    coord=upper(q(2**15)*E0+q(2**12)*E1)
    return dict(E0=E0,E1=E1,j_upper=upper(j),m_upper=upper(m),
        C_upper=upper(C0),C1_upper=upper(C1),S_upper=s,HC_upper=c,
        complete_physical_cap_fee_multiplier=scale,coordinate_epsilon=coord)

def boundary_constants(cut,doc):
    legacy=legacy_boundary_constants()
    values=cut["complete_scalar_bounds"];d=q(PARAMETERS["delta_half_width"])
    raw={key:bound(values[key],"complete cut "+key) for key in (
        "xi_A0","xi_phi_A0","zeta_A0","zeta_phi_A0","zeta_mean_absolute",
        "complete_shape_A0","complete_shape_phi_A0")}
    # Each independent complete bound concerns the same physical quantity.
    # The old whole-core pair bounds are also valid bounds for each component.
    U0=upper(min(d*raw["xi_A0"],legacy["E0"]))
    U1=upper(min(d*raw["xi_phi_A0"],legacy["E1"]))
    V0=upper(min(d*raw["zeta_A0"],legacy["E0"]))
    V1=upper(min(d*raw["zeta_phi_A0"],legacy["E1"]))
    mean=upper(min(d*raw["zeta_mean_absolute"],legacy["E0"]))
    # The correlated shape has exact zero mean and physical frequencies 4j.
    shape=upper(min(d*raw["complete_shape_A0"],d*raw["complete_shape_phi_A0"]/4))
    gate(doc,"the whole selected state segment meets the proved shape and mean row neighbourhood",
        lower(U0)>=0 and lower(U1)>=0 and lower(V0)>=0 and lower(V1)>=0
        and lower(mean)>=0 and lower(shape)>=0
        and upper(U0+V0)<=q("1/1000000") and upper(U1+V1)<=q("1/1000000"))
    theta=shape/12;phi=8*theta/7
    LS=9*mean/8+2592*phi
    DC=mean/27+2*V0/9+2*V1/9+2*theta
    q0=8*(mean+V0)/189+mean/504+2*DC/21+theta/84
    q1=8*theta/63
    D0=U0/3+7*V0/9
    D1=U1/3+U0/9+32*V0/27+7*V1/9
    Lodd=D0+D1/3+3*theta
    coordinate=upper(Lodd+2*mean/27+8*LS/3+108*q0+65536*q1)
    j=q("1.015211829")+shape/3
    m=q("5.8639401366")+mean
    C0=q(".318181201")+V0/9+theta/32
    C1=q(".020269146")+DC
    rootj=j.sqrt();su=upper(m*rootj);cu=upper(rootj*(C0*C0+C1*C0/4))
    scale=upper(max(arb(1),su)*cu)
    shaped=dict(U0=U0,U1=U1,V0=V0,V1=V1,M=mean,S0=shape,
        T=upper(theta),P=upper(phi),L_S=upper(LS),D_C=upper(DC),
        q0=upper(q0),q1=upper(q1),D0_sharp=upper(D0),D1_sharp=upper(D1),
        L_odd=upper(Lodd),j_upper=upper(j),m_upper=upper(m),
        C_upper=upper(C0),C1_upper=upper(C1),S_upper=su,HC_upper=cu,
        coordinate_epsilon=coordinate,complete_physical_cap_fee_multiplier=scale)
    selected=dict(coordinate_epsilon=upper(min(legacy["coordinate_epsilon"],coordinate)),
        complete_physical_cap_fee_multiplier=upper(min(
            legacy["complete_physical_cap_fee_multiplier"],scale)))
    doc["complete_boundary_comparison_candidates"]=encode(dict(
        original_Cdelta_bound=legacy,complete_shape_mean_bound=shaped))
    doc["complete_cut_scalar_fields_before_delta"]=encode(raw)
    doc["shape_mean_bound_primary_sha256"]=SHAPE_CAP_PROOF
    doc["boundary_bound_selection_scope"]=dict(
        each_minimum_combines_complete_bounds_for_the_same_operator_or_scalar=True,
        matrix_entries_or_HY_Grams_combined_by_minimum=False,
        no_sqrt97_dimension_fee=True,independent_even_mean_retained=True,
        already_complete_response_repair_fee_not_repeated=True,
        response_alpha_factor_not_applied=True,
        arbitrary_high_cut_input_retained=True,
        unknown_actual_cap_domain_not_proved=True)
    return selected

def diagnostic_threshold(old,e,bd):
    a=upper(old[B]["g"]*e);gap1=1-a
    result=dict(body_feedback=rec(a),body_gap=rec(gap1),
        diagnostic_only=True,strict_direct_matrix_gates_remain_authoritative=True)
    if not lower(gap1)>0:
        result["available"]=False;result["reason"]="body diagonal not below one";return result
    denominator=old[C]["p"]*gap1+old[B]["p"]*old[C]["g"]*e
    result["denominator"]=rec(denominator)
    if denominator==0:
        result.update(available=True,degenerate_boundary_feedback_zero=True,
            boundary_epsilon_threshold=None,no_zero_division=True);return result
    if not lower(denominator)>0:
        result.update(available=False,reason="positive diagnostic denominator unresolved");return result
    epscrit=lower(lower(gap1)/upper(denominator))
    result.update(available=True,sufficient_epsilon_strict_upper_threshold_lower=rec(epscrit),
        degenerate_boundary_feedback_zero=False)
    margin=lower(epscrit-bd["coordinate_epsilon"])
    scale=bd["complete_physical_cap_fee_multiplier"]
    if margin>0 and lower(scale)>0:
        result["sufficient_kappa_strict_upper_threshold_lower"]=rec(lower(margin/scale))
    else:
        result["sufficient_positive_kappa_margin_proved"]=False
    return result

def transfer_load(load,old,e,epsilon,M,gap):
    # M entries are already chosen nonnegative upper bounds. A lower
    # determinant and upper numerators give the full positive inverse.
    A,Bm,Cm,D=M[0][0],M[0][1],M[1][0],M[1][1]
    xb=upper((upper(1-D)*load[B]+Bm*load[C])/gap)
    xc=upper((Cm*load[B]+upper(1-A)*load[C])/gap)
    xn=upper(load[N]+old[N]["g"]*e*xb+old[N]["p"]*epsilon*xc)
    return {B:xb,N:xn,C:xc}

def feedback_case(case,old,e,eLH,rnu,bd):
    epsilon=upper(bd["coordinate_epsilon"]+
        bd["complete_physical_cap_fee_multiplier"]*q(case["kappa"]))
    M=[[upper(old[B]["g"]*e),upper(old[B]["p"]*epsilon)],
       [upper(old[C]["g"]*e),upper(old[C]["p"]*epsilon)]]
    d1=1-M[0][0];d2=1-M[1][1]
    determinant=d1*d2-M[0][1]*M[1][0]
    checks=dict(body_diagonal_below_one=bool(lower(d1)>0),
        cut_diagonal_below_one=bool(lower(d2)>0),
        complete_two_by_two_determinant_positive=bool(lower(determinant)>0))
    passed=all(checks.values())
    result=dict(name=case["name"],physical_cap_kappa=case["kappa"],
        actual_cap_domain_hypotheses_required=case["actual_cap_domain_hypotheses_required"],
        actual_cap_domain_proved_by_this_consumer=False,
        epsilon_low=rec(epsilon),epsilon_high=rec(epsilon),
        nonnegative_feedback_matrix=encode(M),diagonal_gaps=encode([d1,d2]),
        determinant=rec(determinant),strict_sufficient_gates=checks,
        all_strict_sufficient_gates_passed=passed,
        finite193_inverse_under_stated_boundary_hypotheses_proved=passed,
        numerical_nonpass_does_not_prove_singularity=True)
    if not passed:
        result["transferred_columns"]=None
        result["additional_parameter_volume_response_bound"]=None
        return result
    detlower=lower(determinant)
    loads=dict(
        ordinary_whole_core_source={w:old[w]["g"] for w in WINDOWS},
        independent_original_right97_row={w:old[w]["p"] for w in WINDOWS},
        independent_high_whole_body_state={w:upper(old[w]["a"]+old[w]["g"]*eLH) for w in WINDOWS},
        independent_high_actual_cut_state={w:upper(old[w]["c"]+old[w]["p"]*epsilon) for w in WINDOWS})
    transferred={name:transfer_load(load,old,e,epsilon,M,detlower) for name,load in loads.items()}
    result["complete_old_loads"]=encode(loads)
    result["positive_determinant_lower_used"]=rec(detlower)
    result["transferred_columns"]=encode(transferred)
    result["additional_parameter_volume_response_bound"]=encode({
        w:upper(transferred["ordinary_whole_core_source"][w]*rnu) for w in WINDOWS})
    result["additional_parameter_volume_response_scope"]=(
        "only Delta F_nu + Delta A Z on the whole core; old s0, true boundary nu row, "
        "independent waist and particular-source traces remain unpaid")
    result["low_response_matrix_for_independent_high_body_and_cut"]=encode([
        [transferred["independent_high_whole_body_state"][B],transferred["independent_high_actual_cut_state"][B]],
        [transferred["independent_high_whole_body_state"][C],transferred["independent_high_actual_cut_state"][C]]])
    result["true_high_inverse_required_before_infinite_Schur"]=True
    return result

def run(a,doc):
    ctx.prec=a.bits
    green,scalar,cut=inputs(a,doc)
    old=columns(green,doc)
    original=scalar["selected_parameter_operator_fees"]
    e=bound(original["e"],"whole-core ordinary LL operator fee")
    eLH=bound(original["e_LH"],"whole-core ordinary high-to-low operator fee")
    rnu=bound(scalar["complete_scalar_fee_conclusions"]["whole_core"]["ordinary_L2_bounds"][
        "complete_additional_response_source"],"whole-core extra intrinsic-response source")
    bd=boundary_constants(cut,doc)
    gate(doc,"all complete perturbation scalars and source loads are finite and nonnegative",
        all(box(v).is_finite() and lower(v)>=0 for v in [e,eLH,rnu,*bd.values()]))
    doc["complete_scalar_inputs"]=encode(dict(e=e,e_LH=eLH,
        additional_nu_volume_source_whole_core=rnu))
    doc["exact_boundary_comparison_constants"]=encode(bd)
    doc["scalar_fee_source_fields"]=dict(
        e="selected_parameter_operator_fees.e",e_LH="selected_parameter_operator_fees.e_LH",
        additional_nu_volume_source="complete_scalar_fee_conclusions.whole_core.ordinary_L2_bounds.complete_additional_response_source",
        negative_source_scalar_not_substituted=True)
    doc["complete_boundary_margin_diagnostic"]=diagnostic_threshold(old,e,bd)
    doc["complete_case_conclusions"]=[feedback_case(c,old,e,eLH,rnu,bd)
        for c in PARAMETERS["physical_cap_comparisons"]]
    gate(doc,"both complete boundary cases retain their strict scalar verdict and original domain",
        len(doc["complete_case_conclusions"])==2
        and all(c["actual_cap_domain_proved_by_this_consumer"] is False
                for c in doc["complete_case_conclusions"]))
    gate(doc,"finite output, complete mean and remaining parameter and high-block obligations stay separate",
        green["complete_infinite_BVP_inverse_proved"] is False
        and scalar["nu_boundary_affine_and_true_cap_source_not_evaluated"] is True)
    doc.update(complete=True,proved_complete_scalar_feedback_diagnosis=True,
        any_finite_case_passed=any(c["all_strict_sufficient_gates_passed"]
            for c in doc["complete_case_conclusions"]),
        complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False,
        nonlinear_core_constructed=False,physical_inner_trace_domain_proved=False,
        new_original_row_matrix_Gram_target_Fourier_or_integral_calls=0,
        new_recomputable_arrays_persisted=False,all_input_means_and_full97_rows_retained=True,
        exact_ordinary_source_domain=PARAMETERS["complete_ordinary_source_domain"],
        actual_right_row_input_units=BOUNDARY_UNITS)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root",type=Path,required=True)
    p.add_argument("--manifest",type=Path,required=True)
    p.add_argument("--manifest-sha",required=True)
    p.add_argument("--out",type=Path,required=True)
    p.add_argument("--bits",type=int,default=320)
    a=p.parse_args()
    if a.out.exists():raise FileExistsError("preserve the complete existing scalar conclusion")
    start=time.monotonic()
    doc=dict(kind=KIND,source_sha256=sha(__file__),input_manifest_sha256=a.manifest_sha,
        complete=False,failure=None,gates=[],parameters=PARAMETERS,arithmetic_bits=a.bits,
        public_repository=os.environ.get("GITHUB_REPOSITORY"),
        run_id=os.environ.get("GITHUB_RUN_ID"),run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False,
        nonlinear_core_constructed=False,physical_inner_trace_domain_proved=False)
    code=0
    try:run(a,doc)
    except Exception as error:
        code=1;doc["failure"]=dict(type=type(error).__name__,message=str(error),
            traceback_frames=[dict(file=Path(f.filename).name,line=f.lineno,function=f.name)
                for f in traceback.extract_tb(error.__traceback__)[-12:]])
    doc["actual_returncode"]=code;doc["seconds"]=time.monotonic()-start
    save(a.out,doc)
    print(json.dumps(dict(complete=doc["complete"],actual_returncode=code,
        proved_complete_scalar_feedback_diagnosis=doc.get("proved_complete_scalar_feedback_diagnosis",False),
        any_finite_case_passed=doc.get("any_finite_case_passed",False),
        output_bytes=a.out.stat().st_size,output_sha256=sha(a.out),
        complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False)),flush=True)
    if code:raise SystemExit(code)

if __name__=="__main__":main()
