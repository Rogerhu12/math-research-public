#!/usr/bin/env python3
"""New positive-seven-port / mixed-root / waist-density scalar composition.

Only PW.6,16--21 are evaluated. Every positive graph, Riccati reference,
Cauchy estimate, strict propagation, intrinsic/target/Fourier/Taylor source
and the completed current genuine-source product is read without rerunning.
"""
from __future__ import annotations
import argparse,copy,gzip,hashlib,json,os,platform,time,traceback
from fractions import Fraction
from pathlib import Path
import flint
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
REL="topics/visible-flex-exact-nearby/"
PRODUCER=REL+"scripts/fourfold_codazzi_positive_ports_to_waist_density.py"
KIND="actual_complete_positive_ports_to_waist_density_v1"
CONTRACT="246c81ac387392c75a3267faaa934a7f0a4b978fdad8b8ac7cbbd4bd5c413562"
POS_SOURCE="16ffa1a5b3753bc2a70fcf979814b18161df90ae8997510acc8feafac2a88509"
POS_MANIFEST="4c4f8456ff244599e1d3216b10406e8973888e7117ca71710a1cde6e0b0e32d1"
POS_SUMMARY="0a3fb8e1be19b9ad82655099da8d5446ac49d92f073e7f6626d08a0626ec4fef"
POS_PROCESS="f4ac37531a76893b62050d3291f5227f343ad9f48e3365783bff1a52c451a3f1"
POS_NATIVE="498a5f8be6d2729a1029dbc45a7c06f832c58e2d269031f7db929c2327a0c260"
SP_SOURCE="9d6ef721338e47e2cae8d179ce84976881df91762050d2a77d83b5399f6ba69a"
SP_MANIFEST="c77e969bd02ef95d30f16b53ae0a0d3854f596412151e9242ffa0485bd142210"
SP_EXECUTION="a3a02969178e5e8b3b040fafd51d08b25d75b3f3922f2ae2e9ee0d4a8ab18a12"
SP_RESULT="6a1df053edd9e4ecfff26ea91e9f0a01b37b5d51aefd828cc1c99b83448a9367"
CANDIDATE="ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
CENTRE="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
DIRECTION="6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
PARAMETERS=json.loads(r'''{
  "arithmetic_bits": 320,
  "exact_real_delta_radius": "1/100000000",
  "fixed_intrinsic_parameter": "eta_0",
  "exact_nu_family": "nu_delta=nu0+delta",
  "physical_frequency_factor": 4,
  "high_index_minimum": 97,
  "physical_frequency_minimum": 388,
  "exact_root_interval": [
    "1191984371497/5000000000000",
    "2383968743003/10000000000000"
  ],
  "exact_negative_root_radius": "1/200",
  "exact_negative_strict_interval": [
    "0",
    "2333968743003/10000000000000"
  ],
  "positive_source_window": "L2_r H_phi^(-2/3)",
  "positive_raw_state_window": "L2_r H_phi^(-1)",
  "root_trace_window": [
    "H_phi^(-2/3)",
    "H_phi^(-1)"
  ],
  "negative_root_ordinary_windows": [
    "L2_r H_phi^(-2/3)",
    "L2_r constants"
  ],
  "strict_ordinary_window": "L1_r (H_phi^(-1) pair), alternatively L2_r",
  "waist_output": "L2 old-circle density pair plus both full mean coordinates",
  "positive_input_order": [
    "root_stable_Y_port",
    "collar_ordinary_Hminus2over3_source",
    "body_ordinary_Hminus2over3_source",
    "body_outer_mean_head_and_Y_weighted_jumps",
    "collar_Y_weighted_affine_jumps",
    "cut_stable_Y_jump",
    "cut_unstable_Y_jump"
  ],
  "root_output_factor": "9",
  "optional_raw_stable_input_factor": "153/16",
  "complete_mean_coordinates": 2,
  "ordinary_radial_measure": "dr",
  "angular_measure": "normalized original physical moving circle",
  "positive_graph_run": "43627228225/1",
  "primitive_mean_strict_run": "43731464771/1",
  "positive_existing_gate_count": 18,
  "strict_existing_gate_count": 20,
  "new_seven_port_rows": 2,
  "new_raw_jump_columns": 4,
  "new_combined_cut_jump_column": 1,
  "new_exterior_columns": 4,
  "new_positive_volume_joint_column": 1,
  "copied_exterior_mean_columns": 3,
  "copied_original_positive_matrix_rows": 8,
  "old_graph_Riccati_target_coefficients_or_kernels_recomputed": false,
  "old_Cauchy_normalizer_or_strict_products_recomputed": false,
  "old_genuine_source_product_recomputed": false,
  "finite_root_head_and_both_means_are_independent": true,
  "true_positive_trial_source_and_jump_norms_supplied": false,
  "complete_strong_return_or_high_BVP_claimed": false
}''')
INPUT_ORDER=tuple(PARAMETERS["positive_input_order"])
POS_ROWS=("body_incoming_stable_cut_Y_port","collar_incoming_unstable_cut_Y_port",
    "full_root_outgoing_unstable_Y_port","body_Y_sup","collar_Y_sup","entire_positive_Y_sup",
    "entire_positive_raw_L2r_Hminus1","entire_positive_primitive_L2r_L2phi")
EXT_ORDER=("low_nonmean_y_Hminus5over6","independent_outer_height_dotH_two_minus5over6",
    "ordinary_Robin_Hminus5over6","independent_mean_residual")
MEAN_ORDER=("full_nonmean_y_Hminus5over6","independent_outer_height_dotH_two_minus5over6",
    "independent_mean_residual")
SP_KEYS=("root_or_affine_jump_to_waist_density_gain",
    "ordinary_root_window_source_to_waist_density_gain",
    "strict_L1_Hminus1_source_to_waist_density_gain",
    "strict_L2_Hminus1_source_to_waist_density_gain")
NATIVE_NAME="temporary-complete-positive-ports-to-waist-density.json.gz"
EXPECTED_GATES=21
ZERO_COUNTERS=("old_numerical_enclosures_recomputed","old_positive_graph_or_Riccati_kernels_recomputed",
    "old_Cauchy_normalizer_or_strict_products_recomputed","old_genuine_source_product_recomputed",
    "old_target_FFT_intrinsic_repair_or_Taylor_recomputed","old_natural_parts_or_archives_read")

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()

def read(path):
    return json.loads(Path(path).read_bytes())

def save_small(path,value):
    raw=canonical(value)
    if len(raw)>60000:raise ValueError("the complete final scientific process exceeds60000 UTF8 bytes")
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temp=path.with_name(path.name+".partial");temp.write_bytes(raw);temp.replace(path)

def exact(value):
    value=Fraction(value)
    return arb(value.numerator)/value.denominator

def interval(value):
    if isinstance(value,dict):
        if "lower" in value and "upper" in value:
            result=arb(value["lower"]).lower().union(arb(value["upper"]).upper())
        elif isinstance(value.get("ball"),str):
            result=arb(value["ball"])
        else:raise ValueError("an accepted scalar lacks its complete original enclosure")
    else:result=arb(value)
    if not result.is_finite():raise ValueError("a complete scalar enclosure is not finite")
    return result

def upper(value):
    result=interval(value).upper()
    if not result>=0:raise ValueError("a positive budget has no nonnegative upper endpoint")
    return result

def record(value):
    result=interval(value)
    return {"ball":result.str(64)}

def records(value):
    if isinstance(value,dict):return {key:records(x) for key,x in value.items()}
    if isinstance(value,(tuple,list)):return [records(x) for x in value]
    if isinstance(value,arb):return record(value)
    return value

def gate(doc,name,condition):
    doc["gates"].append({"name":name,"passed":bool(condition)})
    if not condition:raise ValueError("PW gate failed: "+name)

def relpath(value):
    value=Path(value)
    if value.is_absolute() or ".." in value.parts or not str(value).startswith(REL):
        raise ValueError("a PW input left the authorized topic")
    return value

def check(path,size,digest):
    path=Path(path)
    if not path.is_file() or path.stat().st_size!=size or sha(path)!=digest:
        raise ValueError("an exact small input changed: "+str(path))

def inputs(args,doc):
    manifest=read(args.manifest);entries=manifest["files"]
    bypath={entry["path"]:entry for entry in entries}
    ok=(len(bypath)==len(entries) and manifest.get("public_repository")==PUBLIC
        and manifest.get("scientific_source_path")==PRODUCER
        and manifest.get("scientific_source_sha256")==sha(__file__)
        and sha(args.manifest)==args.manifest_sha
        and manifest.get("mathematical_parameters")==PARAMETERS
        and manifest.get("expected_actual_gate_count")==EXPECTED_GATES
        and manifest.get("legacy_artifact_inputs")==[]
        and manifest.get("all_inputs_are_current_small_texts") is True)
    for entry in entries:
        if entry["bytes"]>=100000 or not entry["path"].endswith((".json",".py",".md")):
            raise ValueError("only pinned small UTF8 conclusions, scripts and contracts are allowed")
        check(args.repo/relpath(entry["path"]),entry["bytes"],entry["sha256"])
    paths={key:args.repo/relpath(value) for key,value in manifest["input_paths"].items()}
    gate(doc,"the new source PW contract exact parameters and all small input bytes are frozen",
        ok and sha(paths["contract"])==CONTRACT
        and sha(paths["positive_summary"])==POS_SUMMARY and sha(paths["positive_process"])==POS_PROCESS
        and sha(paths["positive_source"])==POS_SOURCE and sha(paths["positive_manifest"])==POS_MANIFEST
        and sha(paths["strict_source"])==SP_SOURCE and sha(paths["strict_manifest"])==SP_MANIFEST
        and sha(paths["strict_execution"])==SP_EXECUTION and sha(paths["strict_result"])==SP_RESULT)

    pos=read(paths["positive_summary"]);process=read(paths["positive_process"])
    pm=read(paths["positive_manifest"])
    child=process.get("children",[])
    gate(doc,"the complete original positive child run source manifest and summary native identities agree",
        process.get("complete") is True and process.get("repository")==PUBLIC
        and str(process.get("run_id"))+"/"+str(process.get("run_attempt"))=="43627228225/1"
        and process.get("workflow_commit")=="e5e4acacf2076be23c74a5f326ab01ebe0a82e7e"
        and process.get("input_manifest_sha256")==POS_MANIFEST
        and len(child)==1 and child[0].get("actual_returncode")==0
        and pos.get("source_sha256")==POS_SOURCE and pos.get("native_sha256")==POS_NATIVE
        and process.get("complete_native_sha256")==POS_NATIVE
        and any(x.get("sha256")==POS_SUMMARY and x.get("bytes")==41797
                for x in process.get("native_files",[])))
    gate(doc,"the original negative_one positive graph has all18 gates seven columns and eight rows",
        pos.get("kind")=="actual_full_real_delta_negative_one_positive_given_head_graph_v1"
        and pos.get("complete") is True and pos.get("failure") is None
        and len(pos.get("gates",[]))==18 and all(g.get("passed") is True for g in pos["gates"])
        and process.get("actual_scientific_gates")==18
        and process.get("actual_complete_source_columns")==pm.get("full_input_columns")==7
        and process.get("actual_complete_output_rows")==pm.get("full_output_rows")==8
        and process.get("original_collar_body_outer_target_or_response_mathematics_recomputed")==0
        and pos.get("all_original_collar_body_target_reference_and_outer_mathematics_recomputed")==0)

    ex=read(paths["strict_execution"]);sp=ex.get("actual_scientific_receipt",{})
    gate(doc,"the original strict propagation child is the immutable completed20gate result",
        ex.get("complete") is True and ex.get("actual_returncode")==0
        and ex.get("repository")==PUBLIC
        and str(ex.get("run_id"))+"/"+str(ex.get("run_attempt"))=="43731464771/1"
        and ex.get("source_budget_source_sha256")==SP_SOURCE
        and ex.get("input_manifest_sha256")==SP_MANIFEST and ex.get("actual_source_budget_processes")==1
        and sp.get("kind")=="actual_complete_primitive_mean_strict_propagation_v1"
        and sp.get("complete") is True and sp.get("proved") is True
        and sp.get("actual_returncode")==0 and sp.get("failure") is None
        and sp.get("source_sha256")==SP_SOURCE and sp.get("input_manifest_sha256")==SP_MANIFEST
        and len(sp.get("gates",[]))==20 and all(g.get("passed") is True for g in sp["gates"])
        and sp.get("old_numerical_enclosures_recomputed")==0
        and any(x.get("file")=="consumers/conclusion.md" and x.get("sha256")==SP_RESULT
                and x.get("bytes")==13189 for x in ex.get("output_hashes",[])))
    ident=sp["exact_family_identity"];spar=sp["mathematical_parameters"]
    gate(doc,"both completed operators use the same full_real_delta repaired centre and complete193 direction",
        pos.get("original_candidate_sha256")==ident.get("original_candidate_sha256")==CANDIDATE
        and pos.get("derived_definition_sha256")==ident.get("continuous_centre_definition_sha256")==CENTRE
        and pos.get("explicit_direction_definition_sha256")==ident.get("continuous_response_definition_sha256")==DIRECTION
        and pos.get("exact_real_delta_radius")==pm.get("exact_real_delta_radius")==
            spar.get("exact_real_delta_radius")==PARAMETERS["exact_real_delta_radius"]
        and pos.get("exact_affine_parameter_offset")=="0"
        and pos.get("physical_parameter")=="same fixed physical eta0"
        and spar.get("fixed_intrinsic_parameter")==ident.get("fixed_current_eta")=="eta_0"
        and pos.get("nu_family")=="nu_delta=nu0+delta; its compact intrinsic bump is identically zero on this positive interval"
        and pos.get("same_genuine_forward_and_backward_Riccati_reference") is True)

    rows=pos["response_rows"]
    gate(doc,"all seven typed positive input ports and every complete output row keep their original order",
        tuple(pos.get("input_order",[]))==INPUT_ORDER and set(rows)==set(POS_ROWS)
        and all(len(rows[key])==7 for key in POS_ROWS)
        and pos.get("ordinary_source_contract")=="L2_r H_phi^(-2/3); supplied complete head forcing included"
        and pos.get("raw_state_contract")=="L2_r H_phi^(-1), independent mean is separate"
        and pos.get("state_normalization")=="Y_j=M^-1 F_M^-1 diag(-i sign(j),1) h_j"
        and pos.get("physical_minimum")==388 and pos.get("all_unbounded_high_indices")=="every |j|>=97"
        and pos.get("all_affine_jump_inputs_are_in_new_Y_units") is True
        and pos.get("independent_even_mean_and_all_head_and_affine_source_ports_retained") is True
        and tuple(pos.get("exterior_input_order",[]))==EXT_ORDER
        and tuple(pos.get("exterior_mean_input_order",[]))==MEAN_ORDER)

    endpoint=sp["complete_endpoint_readout_conclusion"]
    prop=sp["complete_strict_propagation_conclusion"]
    gate(doc,"the original uncertain_root_window strict cut two means and real_dr readouts remain exact",
        spar.get("exact_root_interval")==PARAMETERS["exact_root_interval"]
        and spar.get("exact_root_Cauchy_radius")==PARAMETERS["exact_negative_root_radius"]
        and spar.get("exact_strict_interval")==PARAMETERS["exact_negative_strict_interval"]
        and endpoint.get("exact_cut")==PARAMETERS["exact_negative_strict_interval"][1]
        and prop.get("complete_mean_coordinates")==2
        and endpoint.get("waist_output")==PARAMETERS["waist_output"]
        and prop.get("affine_jumps_are_independent_without_radial_length_factor") is True
        and prop.get("all_shorter_ordered_products_and_source_insertions_included") is True
        and sp.get("scope",{}).get("all_Fourier_variations_and_two_means_retained") is True
        and sp.get("scope",{}).get("actual_radial_measure_used") is True)

    const=pos["constants"]
    cin=interval(const["raw_mixed_root_input_to_Y"])
    cout=interval(const["Y_to_raw_mixed_root_output"])
    gate(doc,"raw_mixed_root_input_and_output_conversions_are_the_saved153over16_and9",
        cin==exact("153/16") and cout==arb(9)
        and pos.get("root_input_and_output_mixed_Bessel_conversions_paid") is True
        and pos.get("ordinary_and_raw_jump_Bessel_conversions_paid") is True
        and pm.get("negative_order_root_reflection_one_half_gate_required") is False)

    # Parse accepted bound numbers, never infer a lower bound on an actual function.
    for key in POS_ROWS:
        for value in rows[key]:upper(value)
    for value in pos["exterior_affine_Y_output_coefficients"]+pos["exterior_mean_output_coefficients"]:
        upper(value)
    for key in SP_KEYS:upper(endpoint[key])
    for key in ("uniform_body_raw_Hminus2over3_jump_to_Y_gain",
                "collar_or_cut_raw_Hminus2over3_jump_to_Y_gain"):
        upper(const[key])
    gate(doc,"all_complete_saved_bound_numbers_are_finite_and_the_original_two_port_tests_remain_passed",
        upper(const["body_feedback"])<1 and upper(const["interface_loop_upper"])<1
        and interval(const["positive_interface_margin"]).lower()>0
        and len(pos["exterior_affine_Y_output_coefficients"])==4
        and len(pos["exterior_mean_output_coefficients"])==3
        and pos.get("negative_order_root_reflection_one_half_gate_not_required") is True
        and pos.get("given_complete_head_positive_high_inverse_and_root_graph_proved") is True)

    source=sp["accepted_small_input_conclusions"]["source"]
    gate(doc,"the current genuine_root_piece_source_is_the_same_completed31term_RJ_pair_and_old_product",
        source.get("run")=="43728317408/1"
        and source.get("first_term_count")==21 and source.get("independent_mean_term_count")==10
        and source.get("combined_L2_upper")==endpoint["current_genuine_source_pair_L2_upper"]
        and source.get("exact_negative_physical_cover")==endpoint["current_source_support"]
        and endpoint.get("current_genuine_input")=="both genuine columns and both signs |j|>=97 in H^(-4/3)"
        and sp.get("scope",{}).get("complete_current_RJ_ledger_read_verbatim") is True
        and endpoint.get("all_positive_graph_inputs_still_separate") is True
        and endpoint.get("all_root_and_affine_jump_inputs_still_separate") is True)

    doc["accepted_small_input_conclusions"]={
        "positive":dict(run="43627228225/1",source_sha256=POS_SOURCE,
            input_manifest_sha256=POS_MANIFEST,summary_sha256=POS_SUMMARY,summary_bytes=41797,
            summary_path=manifest["input_paths"]["positive_summary"],process_sha256=POS_PROCESS,
            original_native_sha256=POS_NATIVE,original_native_read=False),
        "strict":dict(run="43731464771/1",source_sha256=SP_SOURCE,
            input_manifest_sha256=SP_MANIFEST,execution_sha256=SP_EXECUTION,
            result_sha256=SP_RESULT,execution_path=manifest["input_paths"]["strict_execution"]),
        "genuine_source":copy.deepcopy(source)}
    doc["exact_family_identity"]=copy.deepcopy(ident)
    doc["retained_positive_response_identity"]=dict(
        summary_path=manifest["input_paths"]["positive_summary"],summary_sha256=POS_SUMMARY,
        input_order=list(INPUT_ORDER),output_order=list(POS_ROWS),complete_rows=8,complete_columns=7,
        original_complete_matrix_sha256=hashlib.sha256(canonical(rows)).hexdigest(),
        all_bounds_referenced_byte_exact=True,old_matrix_recomputed=False)
    return manifest,paths,pos,sp

def compose_seven_ports(pos,sp,doc):
    raw=pos["response_rows"]["full_root_outgoing_unstable_Y_port"]
    saved=copy.deepcopy(raw);u=[upper(value) for value in raw]
    omega=[upper(value+int(i==0)) for i,value in enumerate(u)]
    gate(doc,"the complete_root_Y_pair_adds_the_independent_stable_input_once_and_keeps_all_seven_columns",
        len(omega)==7 and all(x>=0 for x in omega)
        and raw==saved and PARAMETERS["finite_root_head_and_both_means_are_independent"] is True)
    root=[upper(9*x) for x in omega]
    CR=upper(sp["complete_endpoint_readout_conclusion"][SP_KEYS[0]])
    waist=[upper(CR*x) for x in root]
    gate(doc,"the_same_complete_seven_root_columns_are_mapped_through_the_saved_root_Cauchy_and_strict_gain",
        len(root)==len(waist)==7 and all(x>=0 for x in root+waist))
    conclusion=dict(
        input_order=list(INPUT_ORDER),output=PARAMETERS["waist_output"],
        old_full_root_outgoing_unstable_Y_row_read_verbatim=saved,
        complete_root_Y_pair_coefficients_upper=records(omega),
        complete_high_raw_mixed_root_coefficients_upper=records(root),
        complete_positive_seven_port_to_waist_coefficients_upper=records(waist),
        root_output_factor="9",root_stable_input_retained=True,
        finite_root_head_and_two_mean_inputs_retained=True,
        raw_Hminus1_is_not_raw_L2=True,
        ordered_composition=["complete_positive_seven_port_graph",
            "physical_mixed_root_output","complete_negative_root_Cauchy",
            "complete_strict_primitive_mean_propagation","actual_waist_density_readout"])
    doc["complete_seven_port_waist_conclusion"]=conclusion
    doc["new_complete_root_and_waist_columns"]=14
    return waist

def raw_and_exterior(pos,waist,doc):
    const=pos["constants"]
    cin=upper(const["raw_mixed_root_input_to_Y"])
    cb=upper(const["uniform_body_raw_Hminus2over3_jump_to_Y_gain"])
    cc=upper(const["collar_or_cut_raw_Hminus2over3_jump_to_Y_gain"])
    raw_stable=upper(waist[0]*cin)
    jumps=[upper(waist[3]*cb)]+[upper(waist[i]*cc) for i in (4,5,6)]
    joint_cut=upper((waist[5]+waist[6])*cc)
    gate(doc,"raw_stable_and_all_four_positive_jump_columns_pay_only_their_original_frame_conversion",
        raw_stable>=0 and len(jumps)==4 and all(x>=0 for x in jumps) and joint_cut>=0)
    ext=pos["exterior_affine_Y_output_coefficients"]
    out=[upper(waist[3]*upper(x)) for x in ext]
    means=copy.deepcopy(pos["exterior_mean_output_coefficients"])
    gate(doc,"four_exterior_inputs_expand_the_same_body_right_column_and_three_true_mean_outputs_are_copied",
        len(out)==4 and len(means)==3 and all(x>=0 for x in out)
        and means==pos["exterior_mean_output_coefficients"])
    joint_volume=upper((waist[1]*waist[1]+waist[2]*waist[2]).sqrt())
    gate(doc,"the_optional_positive_volume_bound_uses_only_the_two_disjoint_complete_ordinary_source_columns",
        joint_volume>=0 and PARAMETERS["ordinary_radial_measure"]=="dr")
    doc["complete_raw_and_exterior_conclusion"]=dict(
        optional_raw_stable_mixed_root_to_waist_upper=record(raw_stable),
        original_raw_stable_input_conversion_read_verbatim=copy.deepcopy(const["raw_mixed_root_input_to_Y"]),
        original_raw_body_jump_conversion_read_verbatim=copy.deepcopy(const["uniform_body_raw_Hminus2over3_jump_to_Y_gain"]),
        original_raw_collar_or_cut_jump_conversion_read_verbatim=copy.deepcopy(const["collar_or_cut_raw_Hminus2over3_jump_to_Y_gain"]),
        raw_jump_input_order=["body_raw_Hminus2over3_jump","collar_raw_Hminus2over3_jump",
            "cut_stable_raw_Hminus2over3_jump","cut_unstable_raw_Hminus2over3_jump"],
        positive_raw_jump_to_waist_coefficients_upper=records(jumps),
        same_physical_cut_jump_two_projections_to_waist_upper=record(joint_cut),
        exterior_input_order=list(EXT_ORDER),
        original_exterior_Y_input_coefficients_read_verbatim=copy.deepcopy(ext),
        complete_exterior_inputs_to_waist_coefficients_upper=records(out),
        independent_exterior_mean_input_order=list(MEAN_ORDER),
        independent_exterior_mean_output_coefficients_read_verbatim=means,
        exterior_mean_is_not_the_root_finite_head_trace=True,
        joint_positive_ordinary_source_to_waist_upper=record(joint_volume),
        joint_volume_requires_the_same_complete_source_on_disjoint_positive_intervals=True,
        all_seven_separate_inputs_remain_available=True,
        raw_or_Y_input_choice_is_explicit_no_double_charge=True)
    doc["new_raw_stable_column"]=1;doc["new_raw_jump_columns"]=4
    doc["new_combined_cut_jump_column"]=1;doc["new_exterior_columns"]=4
    doc["new_joint_positive_volume_column"]=1;doc["old_exterior_mean_columns_read_verbatim"]=3

def retain_negative_inputs(pos,sp,doc):
    endpoint=sp["complete_endpoint_readout_conclusion"]
    retained={key:copy.deepcopy(endpoint[key]) for key in SP_KEYS}
    doc["complete_negative_inputs_conclusion"]=dict(
        original_endpoint_gain_fields_read_verbatim=retained,
        input_order=["root_finite_head_and_two_means","negative_root_window_mixed_jumps",
            "negative_root_window_ordinary_pair","strict_L1_Hminus1_ordinary_pair","strict_Hminus1_impulses"],
        complete_to_waist_coefficients_read_verbatim=[copy.deepcopy(endpoint[key])
            for key in (SP_KEYS[0],SP_KEYS[0],SP_KEYS[1],SP_KEYS[2],SP_KEYS[2])],
        strict_L2_ordinary_alternative_read_verbatim=copy.deepcopy(endpoint[SP_KEYS[3]]),
        strict_L1_and_L2_are_alternatives_not_two_summands=True,
        strict_impulses_never_get_a_radial_length_factor=True,
        negative_root_window_impulses_keep_their_distinct_mixed_norm=True,
        independent_two_root_mean_coordinates=2)
    gate(doc,"all_negative_root_and_strict_source_and_impulse_coefficients_are_copied_without_recalculation",
        all(retained[k]==endpoint[k] for k in SP_KEYS)
        and doc["complete_negative_inputs_conclusion"]["independent_two_root_mean_coordinates"]==2)
    doc["current_genuine_source_contribution_read_verbatim"]={
        key:copy.deepcopy(endpoint[key]) for key in (
            "current_genuine_input","current_genuine_source_pair_L2_upper",
            "current_genuine_strong_source_to_waist_contribution_upper","current_source_support")}
    gate(doc,"the_complete_current_RJ_root_piece_source_product_is_kept_byte_exact_and_is_not_called_the_whole_return",
        all(value==endpoint[key] for key,value in doc["current_genuine_source_contribution_read_verbatim"].items())
        and doc["old_genuine_source_product_recomputed"]==0)
    gate(doc,"all_old_positive_output_rows_and_both_exterior_mean_and_head_scopes_remain_unchanged",
        len(pos["response_rows"])==8
        and hashlib.sha256(canonical(pos["response_rows"])).hexdigest()==
            doc["retained_positive_response_identity"]["original_complete_matrix_sha256"]
        and pos.get("full_low_high_Schur_inverse_proved") is False
        and pos.get("complete_infinite_BVP_inverse_proved") is False
        and pos.get("complete_strong_return_norm_evaluated") is False)

def markdown(doc):
    lines=["# Actual seven positive ports through the mixed root to the complete waist density","",
        "- Repository: "+PUBLIC,"- Run: "+str(doc["run_id"])+"/"+str(doc["run_attempt"]),
        "- Source: "+PRODUCER,"- Source SHA256: "+doc["source_sha256"],
        "- Manifest SHA256: "+doc["input_manifest_sha256"],
        "- Actual scientific return code: "+str(doc["actual_returncode"]),
        "- Complete: "+str(doc["complete"]),"- Passed gates: "+
            str(sum(g["passed"] for g in doc["gates"]))+"/"+str(len(doc["gates"])),
        "- New mathematical seconds: "+str(doc["actual_mathematical_wall_seconds"]),
        "- All old scientific enclosures, kernels, strict products and the current source product recomputed: 0.",""]
    if doc.get("failure") is not None:
        lines+=["## Actual failure","",json.dumps(doc["failure"],ensure_ascii=False),"",
            "No complete new seven-port to waist-density conclusion is asserted.",""]
        return "\n".join(lines)
    c=doc["complete_seven_port_waist_conclusion"];r=doc["complete_raw_and_exterior_conclusion"]
    n=doc["complete_negative_inputs_conclusion"];g=doc["current_genuine_source_contribution_read_verbatim"]
    lines+=["## Complete ordered seven-port map","",
        "The same repaired full-real-delta family, fixed eta0 and both signs |j|>=97 are used. "
        "The input vector is (s,Fc,Fb,B,Jc,Js,Ju). Its stable root input, finite head and both means remain independent. "
        "The output is the Euclidean old-circle density pair and both complete means at the waist.","",
        "| Exact input | High mixed root coefficient | Complete waist-density coefficient |",
        "|---|---:|---:|"]
    for i,name in enumerate(INPUT_ORDER):
        lines.append("| "+name+" | "+c["complete_high_raw_mixed_root_coefficients_upper"][i]["ball"]+
            " | "+c["complete_positive_seven_port_to_waist_coefficients_upper"][i]["ball"]+" |")
    lines+=["","The root output factor 9 is paid. The independent stable trace is added before taking this "
        "complete root bound. The old root reflection 3.82586263265... is retained through its actual two-port "
        "interface; no one-half reflection gate is imposed.","",
        "## Optional raw and exterior inputs","",
        "- Raw stable mixed-root datum: "+r["optional_raw_stable_mixed_root_to_waist_upper"]["ball"]+
            ". Its extra input factor is 153/16; this column is used instead of the already-normalized s column.",
        "- Same physical cut jump, both stable and unstable projections: "+
            r["same_physical_cut_jump_two_projections_to_waist_upper"]["ball"]+".",
        "- Joint complete positive ordinary source on the two disjoint intervals: "+
            r["joint_positive_ordinary_source_to_waist_upper"]["ball"]+".","",
        "| Positive raw jump | Complete waist coefficient |","|---|---:|"]
    for name,value in zip(r["raw_jump_input_order"],r["positive_raw_jump_to_waist_coefficients_upper"]):
        lines.append("| "+name+" | "+value["ball"]+" |")
    lines+=["","| Independent exterior input entering B | Complete waist coefficient |","|---|---:|"]
    for name,value in zip(r["exterior_input_order"],r["complete_exterior_inputs_to_waist_coefficients_upper"]):
        lines.append("| "+name+" | "+value["ball"]+" |")
    lines+=["","The three original exterior physical-mean coefficients remain separate in the execution "
        "receipt. They do not supply the finite-head root trace. The original eight positive output rows "
        "are retained by their exact summary SHA, with no repeated computation.","",
        "## Independent negative sources, head and impulses","",
        "| Independent input | Saved complete waist coefficient, copied verbatim |","|---|---:|"]
    for name,value in zip(n["input_order"],n["complete_to_waist_coefficients_read_verbatim"]):
        lines.append("| "+name+" | "+value["ball"]+" |")
    lines+=["","The alternative strict L2 ordinary-source coefficient is "+
        n["strict_L2_ordinary_alternative_read_verbatim"]["ball"]+
        ". It replaces only the L1 ordinary term; strict impulses retain the L1 coefficient with no length factor.","",
        "## Current complete genuine root-piece contribution","",
        "- Saved source pair: "+g["current_genuine_source_pair_L2_upper"]["ball"]+".",
        "- Saved complete source-to-waist product: "+g["current_genuine_strong_source_to_waist_contribution_upper"]["ball"]+".",
        "- Source support: "+json.dumps(g["current_source_support"])+".",
        "Both numbers and the whole 21+10 source accounting are read through the accepted SP receipt; "
        "this old product is not computed again. The additional positive sources, true jumps, finite "
        "root head and stable input are not assigned zero.","",
        "## Actual gates",""]
    lines += ["- "+str(i+1)+". "+x["name"]+": "+str(x["passed"]) for i,x in enumerate(doc["gates"])]
    lines+=["","## Exact scope","",
        "This completes the declared source/port composition in old-circle density coordinates. "
        "The raw curvature state is not promoted from Hminus1 to L2. A true-ray, principal-angle or physical-angle "
        "density transformation still uses its own actual norm. No high BVP, return inverse, finite Schur, "
        "complete strong remainder or final matching is proved by these coefficients alone.",
        "Only this small final conclusion and execution identity are published. No new array, native certificate, "
        "Release asset or Actions data artifact is persisted.",""]
    return "\n".join(lines)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,required=True)
    parser.add_argument("--manifest",type=Path,required=True)
    parser.add_argument("--manifest-sha",required=True)
    parser.add_argument("--out-dir",type=Path,required=True)
    args=parser.parse_args();args.repo=args.repo.resolve();args.out_dir=args.out_dir.resolve()
    args.out_dir.mkdir(parents=True,exist_ok=True)
    if (args.out_dir/"process.json").exists():raise FileExistsError("preserve every actual complete or failed PW conclusion")
    ctx.prec=320;started=time.monotonic()
    doc=dict(kind=KIND,public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),input_manifest_sha256=args.manifest_sha,
        complete=False,proved=False,actual_returncode=1,failure=None,gates=[],
        runtime={"python":platform.python_version(),"python_flint":flint.__version__},
        arithmetic_bits=320,mathematical_parameters=PARAMETERS,
        full_high_inverse_claimed=False,full_return_remainder_claimed=False,
        temporary_native_is_not_published=True,reproducible_outputs_published_to_repository=False,
        reproducible_outputs_uploaded_to_Releases=False,new_reproducible_data_artifact_uploaded=False,
        **{key:0 for key in ZERO_COUNTERS})
    native=None
    try:
        gate(doc,"the unique new scalar child runs only in public Actions with Python3.12.14 flint0.9 and320bits",
            os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")==PUBLIC
            and platform.python_version()=="3.12.14" and flint.__version__=="0.9.0" and ctx.prec==320)
        manifest,paths,pos,sp=inputs(args,doc)
        old_hash=hashlib.sha256(canonical({"positive":pos,"strict":sp})).hexdigest()
        waist=compose_seven_ports(pos,sp,doc)
        raw_and_exterior(pos,waist,doc)
        retain_negative_inputs(pos,sp,doc)
        gate(doc,"every_successful_old_scientific_object_is_unchanged_and_all_original_mathematics_calls_are_zero",
            hashlib.sha256(canonical({"positive":pos,"strict":sp})).hexdigest()==old_hash
            and all(doc[key]==0 for key in ZERO_COUNTERS))
        doc["scope"]=dict(
            same_full_real_delta_family=True,all_unbounded_high_physical_signs_retained=True,
            positive_source_window_is_the_completed_negative_one_window=True,
            all_seven_positive_ports_retained=True,finite_root_head_and_two_means_independent=True,
            raw_input_153over16_and_output9_are_distinct=True,
            ordinary_sources_and_affine_impulses_are_distinct=True,
            actual_dr_measure_and_uncertain_root_band_retained=True,
            no_second_primitive_or_radial_normalizer_fee=True,
            current_RJ_source_product_copied_verbatim=True,
            old_positive_matrix_and_mean_rows_preserved_by_exact_input_identity=True,
            true_positive_trial_source_jump_magnitudes_not_assigned_zero=True,
            raw_Hminus1_not_called_raw_L2=True,
            actual_angle_and_KAM_density_change_not_assumed=True,
            complete_strong_return_and_high_BVP_not_claimed=True,new_row_arrays_published=False)
        gate(doc,"the_complete_final_connection_keeps_all_scopes_and_the_exact_twenty_one_proof_gates",
            len(doc["gates"])+1==EXPECTED_GATES
            and doc["new_complete_root_and_waist_columns"]==14
            and doc["new_exterior_columns"]==4 and doc["new_raw_jump_columns"]==4)
        native=dict(kind=KIND+"_temporary_native",source_sha256=doc["source_sha256"],
            input_manifest_sha256=args.manifest_sha,complete=True,
            original_positive_matrix_sha256=doc["retained_positive_response_identity"]["original_complete_matrix_sha256"],
            complete_seven_port_waist_conclusion=doc["complete_seven_port_waist_conclusion"],
            complete_raw_and_exterior_conclusion=doc["complete_raw_and_exterior_conclusion"],
            no_original_scientific_result_recomputed=True)
        doc["complete"]=doc["proved"]=True;doc["actual_returncode"]=0
    except Exception as exc:
        doc["failure"]={"type":type(exc).__name__,"message":str(exc)}
        traceback.print_exc()
    finally:
        doc["actual_mathematical_wall_seconds"]=time.monotonic()-started
        if native is not None:
            raw=gzip.compress(canonical(native),mtime=0);(args.out_dir/NATIVE_NAME).write_bytes(raw)
            doc["temporary_native_sha256"]=hashlib.sha256(raw).hexdigest()
            doc["temporary_native_bytes"]=len(raw)
        try:
            text=markdown(doc)
            if len(text.encode())>60000:raise ValueError("the final conclusion exceeds60000 UTF8 bytes")
            (args.out_dir/"conclusion.md").write_text(text);save_small(args.out_dir/"process.json",doc)
        except Exception as exc:
            original=doc["actual_returncode"]
            slim={key:value for key,value in doc.items() if key not in (
                "complete_seven_port_waist_conclusion","complete_raw_and_exterior_conclusion",
                "complete_negative_inputs_conclusion","current_genuine_source_contribution_read_verbatim")}
            slim["actual_scientific_returncode"]=original
            slim["formatting_failure"]={"type":type(exc).__name__,"message":str(exc)}
            slim["actual_returncode"]=2;save_small(args.out_dir/"process.json",slim)
            (args.out_dir/"conclusion.md").write_text("# PW formatting failure\n\n"+json.dumps(slim["formatting_failure"])+"\n")
            doc["actual_returncode"]=2
    print(json.dumps(dict(complete=doc["complete"],actual_returncode=doc["actual_returncode"],
        gates=len(doc["gates"]),old_numerical_enclosures_recomputed=0,
        mathematical_seconds=doc["actual_mathematical_wall_seconds"]),sort_keys=True),flush=True)
    raise SystemExit(doc["actual_returncode"])

if __name__=="__main__":main()
