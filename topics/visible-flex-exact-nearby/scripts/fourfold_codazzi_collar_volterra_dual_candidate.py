"""One complete W2C collar Volterra/dual candidate in public own Actions.

All old completed objects are verified and read as whole original records.
The only new targets are five complete graphs, fifty scalar records, and
two conditional finite-inverse records when the strict comparison is true.
Full signed centre combination, actual high graph, all means, all193 low
observations, seven ports, both right-hand sides and independent affine
sources retain the complete mathematical contracts bound by the manifest.
No old producer is imported, no original norm is reevaluated, and no array
or separate native artifact is published.
"""
from __future__ import annotations
import argparse, copy, hashlib, importlib.util, json, math, os, platform
import re, sys, time, traceback
from fractions import Fraction
from pathlib import Path

TOPIC="topics/visible-flex-exact-nearby/"
SOURCE_PATH=TOPIC+"scripts/fourfold_codazzi_collar_volterra_dual_candidate.py"
READONLY_PATH=TOPIC+"scripts/fourfold_codazzi_collar_volterra_dual_readonly.py"
CORE_PATH=TOPIC+"scripts/fourfold_codazzi_collar_volterra_dual_readonly_core.py"
KIND="complete_collar_Volterra_dual_candidate_v1"
PREFLIGHT_KIND="complete_collar_Volterra_dual_preflight_v1"
MAX_SCIENTIFIC_BYTES=99000
MAX_RECORD_TEXT_BYTES=128
DIAGNOSTIC_MESSAGE_BYTES=1000
DIAGNOSTIC_TRACEBACK_BYTES=2048
PARAMETERS=json.loads(r'''{"actual_delta_degree":96,"actual_tail_inverse_bound":3,"bits":320,"collar_piece":2549,"complete_family_residual_last_index":416,"complete_new_scalar_targets":50,"conditional_inverse_targets":2,"cutoff_width":"1/16","decimal_record_digits":75,"first_high_index":97,"fixed_completed_provider":"WVC_43891414339_1","head_dimension":193,"high_trial_last_index":224,"new_array_artifacts":false,"old_collar_eta_reused":true,"old_targets_recomputed":0,"original_complete_same_operator_records":29,"parent_band_subcells":8,"parent_cells":153,"physical_high_minimum":388,"real_direction_radius":"1/100000000","reference_centre_degree":32,"reference_high_last_index":160,"refined_cells":24480,"repaired_centre_residual_last_index":288,"same_actual_spaces_and_projections":true,"true_root_is_not_an_enclosure_endpoint":true,"uniform_refinement":160}''')
RETAINED_SCOPE=json.loads(r'''{"actual_S_P_Q_A_B_C_R_and_high_space_unchanged":true,"actual_head_dimension":193,"actual_tail_inverse_bound_from_published_analytic_m160":3,"all_completed_old_bounds_maxima_and_m1_m2_false_gates_read_only":true,"all_four_finite_Schur_blocks_and_both_rhs_retained":true,"all_independent_mean_affine_head_cokernel_and_external_rows_retained":true,"all_original_4650_rows_3594_interfaces_and_4801_intersections_admitted":true,"all_original_two_order_native_rows_read_only":true,"all_seven_primal_dual_ports_retained":true,"complete_actual_family_degree":96,"exact_reference_definition_materialization_only":true,"finite_false_sufficient_gate_does_not_prove_singularity":true,"finite_gate_is_complete_E0_plus_3_D_T_upper_less_than_one":true,"full_family_error_is_whole_output_norm_not_Q224_projection":true,"full_family_residual_last_j":416,"new_head_lift_analytic_upper":"6/5","no_automatic_scientific_retry":true,"no_dense_finite_matrix_or_new_array_artifact":true,"no_derivative_of_continuous_centre_BHL_needed":true,"only_actual_full96_correction_in_family_error_legs":true,"ordinary_radial_L2_measure":true,"original_WPS60_success_false_gate_and_six_modal_prefixes_retained":true,"other_physical_readouts_require_their_full_actual_conversion":true,"outer_chart_dimension":96,"physical_96_root_even_normalization_is_boundary_identity_if_inverse_proved":true,"physical_density_means_Theta_nu_and_actual_96_columns_not_deleted":true,"physical_frequency":4,"physical_mean_reference_zero_actual_mean_fully_retained":true,"prescribed_root_even_dimension":96,"raw_identity_transmissions_and_independent_affine_jumps_retained":true,"reference_only_degree":32,"repaired_centre_is_operator_replacement_not_a_new_physical_background":true,"repaired_centre_residual_last_j":288,"root_complement_dimension":97,"same_complete_repaired_degree32_centre_inside_Green_source":true,"same_selected_positive_genuine_family":true,"whole_actual_radial_head_not_finitely_truncated":true,"trial_last_j":224,"reference_high_last_j":160,"fixed_original_WVC_reference_and_all29_whole_same_operator_copies":true,"original_WVC56_success_false_gate_and_five_modal_prefixes_retained":true,"actual_eta_is_the_same_full_family_function_in_A_and_Ac":true,"whole_true_root_collar_is_not_a_zero_coefficient_packet":true,"all65_signed_repair_offsets_and13_signed_intrinsic_fields_retained":true,"full193_family_direction_fees_and_independent_even_mean_retained":true,"full_true_J_adjoint_integrates_to_R":true,"all_primal_and_dual_cutoff_derivatives_retained":true,"chi_prime_cancellation_applies_only_to_whole_joint_centre_kernel":true,"signed_low_remainder_and_feedback_combined_after_the_same_Gf_before_abs":true,"all193_Gf_atoms_and_true_complete_adjoint_retained":true,"trial_and_dual_compact_core_are_in_the_true_homogeneous_high_graph":true,"original_high_state_error_is_not_copied_for_the_new_trial":true,"full_actual_family_error_output416_and_true_dual_H1_cost_paid":true,"continuous_Gf_has_no_finite_rho2_denominator":true,"finite_Qf_keeps_its_original_full_paired_rho2_and_endpoint_fees":true,"whole_original_intrinsic_parameter_family_claimed":false,"closed_C2_fixed_metric_family_not_concluded_here":true}''')
ORDERED_GRAPH_NAMES=json.loads(r'''["complete_primal_trial_and_actual_residual","complete_dual_actual_residual","complete_family_and_dual_feedback","complete_signed_centre","complete_same_actual_finite_comparison"]''')
GRAPH_RECORD_NAMES=json.loads(r'''{"complete_primal_trial_and_actual_residual":["complete_raw_trial_row_ratio_upper","complete_raw_trial_column_ratio_upper","complete_raw_trial_norm_upper","complete_centre_collar_source_row_ratio_upper","complete_centre_collar_source_column_ratio_upper","complete_centre_collar_source_norm_upper","complete_centre_body_source_row_ratio_upper","complete_centre_body_source_column_ratio_upper","complete_centre_body_source_norm_upper","complete_family_collar_source_row_ratio_upper","complete_family_collar_source_column_ratio_upper","complete_family_collar_source_norm_upper","complete_family_body_source_row_ratio_upper","complete_family_body_source_column_ratio_upper","complete_family_body_source_norm_upper","complete_primal_collar_source_upper","complete_primal_body_source_upper","complete_high_state_error_upper"],"complete_dual_actual_residual":["complete_centre_collar_dual_row_ratio_upper","complete_centre_collar_dual_column_ratio_upper","complete_centre_collar_dual_norm_upper","complete_centre_body_dual_row_ratio_upper","complete_centre_body_dual_column_ratio_upper","complete_centre_body_dual_norm_upper","complete_family_collar_dual_row_ratio_upper","complete_family_collar_dual_column_ratio_upper","complete_family_collar_dual_norm_upper","complete_family_body_dual_row_ratio_upper","complete_family_body_dual_column_ratio_upper","complete_family_body_dual_norm_upper","complete_dual_collar_residual_upper","complete_dual_body_residual_upper","complete_dual_residual_upper"],"complete_family_and_dual_feedback":["complete_low_family_feedback_row_ratio_upper","complete_low_family_feedback_column_ratio_upper","complete_low_family_feedback_norm_upper","complete_cross_family_feedback_row_ratio_upper","complete_cross_family_feedback_column_ratio_upper","complete_cross_family_feedback_norm_upper","complete_trial_family_feedback_row_ratio_upper","complete_trial_family_feedback_column_ratio_upper","complete_trial_family_feedback_norm_upper","complete_dual_feedback_error_upper","complete_head_paired_error_upper"],"complete_signed_centre":["complete_joint_signed_centre_row_ratio_upper","complete_joint_signed_centre_column_ratio_upper","complete_joint_signed_centre_norm_upper"],"complete_same_actual_finite_comparison":["complete_actual_E0_upper","complete_actual_D_upper","complete_actual_finite_defect_upper"]}''')
CONDITIONAL_RECORD_NAMES=json.loads(r'''["complete_actual_finite_gap_lower","complete_actual_finite_inverse_upper"]''')
ADMISSION_GATE_LABELS=json.loads(r'''["all_current_UTF8_files_and_three_fixed_contracts_verified","all_new_and_original_definition_sources_AST_only_verified","all_nineteen_historical_receipts_and_original_native_bytes_verified","complete_original_summary_and_native_projection_identical","both_complete_4650_row_covers_and_3594_interfaces_verified","same_real_family_and_all_original_successes_verified","all_nine_original_literals_and_completed_WHVA_retained","all_five_original_cubic_parts_and_full_shape_verified","original_repair_whole_document_and_all_65_suprema_verified","actual_raw_identity_transmissions_and_full_affine_ports_retained","all_sixty_old_WPS_records_full_false_scope_and_six_prefix_records_verified","complete_WVC_43_scientific_and_44_execution_fields_and_false_gate_verified","all_twenty_nine_same_operator_original_records_verified","original_nineteen_restoration_object_unchanged_and_two_native_extension_verified","all_signed_germ_fields_and_complex_record5_shapes_verified","complete_root_budget_193_upper_records_and_four_full_angular_arrays_verified","exact_signed_65_offsets_and_piece2549_full_complex_domain_verified","same_actual_full_family_eta_and_independent_mean_rows_retained"]''')
GATE_LABELS=json.loads(r'''["all_current_UTF8_files_and_three_fixed_contracts_verified","all_new_and_original_definition_sources_AST_only_verified","all_nineteen_historical_receipts_and_original_native_bytes_verified","complete_original_summary_and_native_projection_identical","both_complete_4650_row_covers_and_3594_interfaces_verified","same_real_family_and_all_original_successes_verified","all_nine_original_literals_and_completed_WHVA_retained","all_five_original_cubic_parts_and_full_shape_verified","original_repair_whole_document_and_all_65_suprema_verified","actual_raw_identity_transmissions_and_full_affine_ports_retained","all_sixty_old_WPS_records_full_false_scope_and_six_prefix_records_verified","complete_WVC_43_scientific_and_44_execution_fields_and_false_gate_verified","all_twenty_nine_same_operator_original_records_verified","original_nineteen_restoration_object_unchanged_and_two_native_extension_verified","all_signed_germ_fields_and_complex_record5_shapes_verified","complete_root_budget_193_upper_records_and_four_full_angular_arrays_verified","exact_signed_65_offsets_and_piece2549_full_complex_domain_verified","same_actual_full_family_eta_and_independent_mean_rows_retained","fixed_directed_runtime_and_one_new_entry","all_twenty_nine_same_operator_records_typed_and_original_optical_eta_retained","entire_fixed_WVC_reference_definition_and_diagonal_chains_materialized","complete_true_collar_body_and_all_kernel_domains_admitted","complete_primal_trial_and_actual_residual_saved","complete_dual_actual_residual_saved","complete_family_and_dual_feedback_saved","complete_signed_centre_saved","complete_same_actual_finite_comparison_saved","all_current_inputs_and_manifest_reverified_after_new_work","complete_whole_candidate_shape_and_old_zero_recomputation"]''')
SCI_FIELDS=json.loads(r'''["actual_checkout_commit","actual_mathematical_wall_seconds","actual_progress","actual_returncode","automatic_retry_authorized","collar_native_identities","collar_original_contexts","complete","complete_current_file_receipts","complete_new_graphs","complete_restoration_receipts","complete_support_contract","completed_targets","conditional_finite_inverse","copied_complete_candidate_metadata","copied_complete_repair_definition","copied_original_scope","copied_same_operator_records","current_target","failure","finite_gate","gates","kernel_progress","kind","manifest_sha256","original_admission","original_closure_admission","original_optical_records","parameters","preparation_prefix","prior_completed_candidate","problem_id","proved","reference_identity","retained_completed_five_maxima","retained_original_false_candidates","retained_scope","run_attempt","run_id","runtime","saved_record_counts","scientific_modules","stage","workflow_event_commit"]''')

def require(ok,message):
    if not ok:
        raise ValueError(message)

def bounded_diagnostic(text,limit):
    value=text.encode("utf-8","replace")[:limit].decode("utf-8","ignore")
    while len(json.dumps(value,ensure_ascii=False).encode("utf-8"))>limit:
        value=value[:-1]
    return value

def import_new_source(root,spec,module_name):
    path=(root/spec["path"]).resolve()
    require(path.is_relative_to(root) and path.is_file(),"new module containment")
    raw=path.read_bytes()
    require(len(raw)==spec["bytes"] and hashlib.sha256(raw).hexdigest()==spec["sha256"]
            and hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
                ==spec["git_blob_sha"],"new module whole-file binding")
    loader=importlib.util.spec_from_file_location(module_name,path)
    require(loader is not None and loader.loader is not None,"new module loader")
    module=importlib.util.module_from_spec(loader)
    loader.loader.exec_module(module)
    return module

def record_text(record):
    require(isinstance(record,dict) and set(record)=={"ball"}
            and isinstance(record["ball"],str) and record["ball"].isascii()
            and 0<len(record["ball"])<=MAX_RECORD_TEXT_BYTES
            and not re.search(r"nan|inf",record["ball"],re.I),
            "one whole finite new scalar record")
    return record["ball"]


def whole_identity(value,canonical,digest):
    raw=canonical(value)
    return {"bytes":len(raw),"sha256":digest(raw)}

def lossless_context_table(contexts,canonical,digest):
    """Factor repeated source identities; reconstruct every original field."""
    require(isinstance(contexts,list),"complete original ordered context list")
    original_keys={"source_role","source_path","source_bytes","source_sha256",
        "source_git_blob_sha","json_path","complete_original_object_bytes",
        "complete_original_object_sha256","whole_original_object_retained_by_immutable_identity"}
    sources={};rows=[]
    row_keys=("source_role","json_path","complete_original_object_bytes",
              "complete_original_object_sha256","whole_original_object_retained_by_immutable_identity")
    for value in contexts:
        require(isinstance(value,dict) and set(value)==original_keys,
                "entire original nine-field context retained")
        spec={"role":value["source_role"],"path":value["source_path"],
              "bytes":value["source_bytes"],"sha256":value["source_sha256"],
              "git_blob_sha":value["source_git_blob_sha"]}
        require(spec["role"] not in sources or sources[spec["role"]]==spec,
                "one whole source identity per role")
        sources[spec["role"]]=spec
        rows.append({key:copy.deepcopy(value[key]) for key in row_keys})
    restored=[]
    for row in rows:
        spec=sources[row["source_role"]]
        restored.append({"source_role":spec["role"],"source_path":spec["path"],
            "source_bytes":spec["bytes"],"source_sha256":spec["sha256"],
            "source_git_blob_sha":spec["git_blob_sha"],**copy.deepcopy(row)})
    require(canonical(restored)==canonical(contexts),
            "lossless reconstruction of every original complete context")
    return {"kind":"lossless_complete_context_table_v1",
        "sources":list(sources.values()),"contexts":rows,
        "complete_original_context_list_identity":whole_identity(contexts,canonical,digest),
        "reconstruction":"For each context row join source_role to its entire sources entry; restore the five original source_* field names."}

def compact_old_archive(archive,records,canonical,digest):
    """Retain every original qualification and reference one shared whole29."""
    value=copy.deepcopy(archive)
    require(value["complete_twenty_nine_copied_record_objects"]==records,
            "identical complete29 before sharing the same scientific object")
    value["complete_twenty_nine_copied_record_objects"]={
        "kind":"whole_same_document_object_reference_v1",
        "json_path":["copied_same_operator_records"],
        "complete_original_object_identity":whole_identity(records,canonical,digest),
        "complete_shared_object_equality_verified":True}
    value["complete_W2CI_required_contexts"]=lossless_context_table(
        value["complete_W2CI_required_contexts"],canonical,digest)
    # All other archive fields, including complete parameters/scopes/false gates,
    # remain the exact original values. No scientific bound is compressed.
    return value

def restoration_reference(receipt,manifest,run,attempt,canonical,digest):
    """The one full21 receipt is published whole in this outcome's execution."""
    require(receipt["kind"]=="complete_W2C_readonly_restoration_v1"
            and receipt["historical_input_count"]==21
            and len(receipt["original_WVC_restoration"]["historical_inputs"])==19,
            "complete admitted restoration before same-outcome sharing")
    return {"kind":"whole_same_outcome_execution_object_reference_v1",
        "path":manifest["operation"]["output_base"]+"/run-"+run+"-"+attempt+"/execution.json",
        "json_path":["historical_restoration"],
        "complete_original_object_identity":whole_identity(receipt,canonical,digest),
        "historical_input_count":21,
        "original_WVC_restoration_identity":whole_identity(
            receipt["original_WVC_restoration"],canonical,digest),
        "whole_original_object_must_be_published_in_same_outcome":True}

class NumericalAPI:
    """Directed finite scalars and exact whole-matrix Arb multiplication."""
    def __init__(self,flint):
        self.arb=flint.arb
        self.arb_mat=flint.arb_mat
        self.zero=self.arb(0);self.one=self.arb(1)
    def upper(self,value):
        require(value.is_finite() and value.lower()>=0,"finite nonnegative bound")
        return value.upper()
    def lower(self,value):
        require(value.is_finite(),"finite signed directed lower")
        return value.lower()
    def magnitude(self,value):
        require(value.is_finite(),"finite signed coefficient")
        return abs(value).upper()
    def sqrt(self,value):
        require(value.is_finite() and value.lower()>=0,"nonnegative square root")
        return value.sqrt()
    def exp(self,value):
        require(value.is_finite(),"finite exponential argument")
        return value.exp()
    def rational(self,numerator,denominator=1):
        require(type(numerator) is int and type(denominator) is int and denominator>0,
                "exact rational with positive denominator")
        return self.arb(numerator)/self.arb(denominator)
    def interval(self,lo,hi):
        lo=lo if hasattr(lo,"is_finite") else self.arb(lo)
        hi=hi if hasattr(hi,"is_finite") else self.arb(hi)
        require(lo.is_finite() and hi.is_finite() and lo.lower()<=hi.upper(),
                "whole finite directed interval")
        return lo.lower().union(hi.upper())
    def hull(self,values):
        require(values and all(x.is_finite() for x in values),"whole nonempty finite hull")
        result=values[0]
        for value in values[1:]:
            result=result.union(value)
        return result
    def old_interval(self,record):
        # Original record3/record5 endpoint semantics. Decimal diagnostics are
        # never used as numerical values. Strings remain the original source.
        if isinstance(record,dict) and "lower" in record and "upper" in record:
            require(isinstance(record["lower"],str) and isinstance(record["upper"],str),
                    "original whole endpoint strings")
            return self.interval(self.arb(record["lower"]).lower(),
                                 self.arb(record["upper"]).upper())
        value=self.arb(record["ball"] if isinstance(record,dict) else record)
        require(value.is_finite(),"whole original finite ball")
        return value
    def matrix_product(self,left,right):
        require(left and right and len(left[0])==len(right),"whole ordered matrix product")
        result=self.arb_mat(left)*self.arb_mat(right)
        rows,cols=len(left),len(right[0])
        return [[result[i,j] for j in range(cols)] for i in range(rows)]

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ("repo","manifest","manifest-sha","out","native","native-receipts",
                 "candidate-index","centre-repair","root-germ","root-budget"):
        parser.add_argument("--"+name,required=True)
    parser.add_argument("--bits",type=int,required=True)
    parser.add_argument("--preflight-only",action="store_true")
    args=parser.parse_args()
    require(args.bits==320,"fixed320-bit directed arithmetic")
    require(os.environ.get("GITHUB_ACTIONS")=="true"
            and os.environ.get("GITHUB_REPOSITORY")=="Rogerhu12/math-research-public",
            "public own Actions only")
    require("flint" not in sys.modules,"readonly boundary precedes numerical imports")
    root=Path(args.repo).resolve()
    manifest_raw=Path(args.manifest).read_bytes()
    require(0<len(manifest_raw)<100000
            and hashlib.sha256(manifest_raw).hexdigest()==args.manifest_sha,
            "complete frozen manifest CLI identity")
    initial=json.loads(manifest_raw)
    specs={item["role"]:item for item in initial["files"]}
    require(specs["science"]["path"]==SOURCE_PATH
            and specs["readonly_admission"]["path"]==READONLY_PATH
            and specs["readonly_core"]["path"]==CORE_PATH
            and Path(__file__).resolve()==(root/SOURCE_PATH).resolve(),
            "actual three new entry/readonly paths")
    raw_self=Path(__file__).read_bytes()
    require(len(raw_self)==specs["science"]["bytes"]
            and hashlib.sha256(raw_self).hexdigest()==specs["science"]["sha256"]
            and hashlib.sha1(b"blob "+str(len(raw_self)).encode()+b"\0"+raw_self).hexdigest()
                ==specs["science"]["git_blob_sha"],"entire new scientific entry identity")
    core=import_new_source(root,specs["readonly_core"],"_w2c_new_readonly_core")
    readonly=import_new_source(root,specs["readonly_admission"],"_w2c_new_readonly")
    canonical,data,digest=core.canonical,core.data,core.digest
    admitted=readonly.admit(root,args.manifest,args.manifest_sha,args.native,
        args.native_receipts,args.candidate_index,args.centre_repair,
        args.root_germ,args.root_budget,core)
    manifest=admitted["manifest"]
    require(canonical(manifest["parameters"])==canonical(PARAMETERS)
            and manifest["retained_scope"]==RETAINED_SCOPE,
            "complete owner parameters and physical scope")
    require([item["name"] for item in admitted["admission"]["checks"]]==ADMISSION_GATE_LABELS
            and all(item["passed"] is True for item in admitted["admission"]["checks"]),
            "whole original and new readonly admission order")
    require(manifest["operation"]["ordered_targets"]==ORDERED_GRAPH_NAMES
            and manifest["operation"]["complete_gate_names"]==GATE_LABELS
            and manifest["operation"]["scientific_field_names"]==SCI_FIELDS,
            "complete frozen outcome schema")
    run=os.environ.get("GITHUB_RUN_ID","");attempt=os.environ.get("GITHUB_RUN_ATTEMPT","")
    event=os.environ.get("GITHUB_SHA","");checkout=os.environ.get("ACTUAL_CHECKOUT_COMMIT","")
    require(re.fullmatch(r"\d{1,20}",run) and re.fullmatch(r"\d{1,10}",attempt)
            and re.fullmatch(r"[0-9a-f]{40}",event)
            and re.fullmatch(r"[0-9a-f]{40}",checkout),"actual public run identity")
    if args.preflight_only:
        result={"kind":PREFLIGHT_KIND,"complete":True,"preflight_only":True,
            "problem_id":readonly.PROBLEM_ID,"manifest_sha256":args.manifest_sha,
            "admission":admitted["admission"],
            "same_complete_WVC_reference":admitted["paired_inputs"]["reference_chain"],
            "same_complete_selected_diagonal_chain":
                admitted["completed_tracefree_inputs"]["selected_diagonal_chain"],
            "same_operator_record_count":29,
            "all_original_successes_false_gates_and_mean_scopes_retained":True,
            "complete_native_original_shapes":admitted["collar_native_shape_summary"],
            "old_scientific_calls":0,"new_scalar_targets_evaluated":0,
            "flint_imported":False}
        require("flint" not in sys.modules,"complete preflight has no numerical library")
        print(canonical(result).decode("utf-8"),end="",flush=True)
        return 0
    output=Path(args.out)
    require(not output.exists(),"one never-overwritten scientific output")
    output.parent.mkdir(parents=True,exist_ok=True)
    paired=admitted["paired_inputs"]
    completed=admitted["completed_tracefree_inputs"]
    document={
        "kind":KIND,"problem_id":readonly.PROBLEM_ID,"complete":False,"proved":False,
        "stage":"complete_readonly_inputs_saved","failure":None,"actual_returncode":None,
        "run_id":run,"run_attempt":attempt,"workflow_event_commit":event,
        "actual_checkout_commit":checkout,"manifest_sha256":args.manifest_sha,
        "scientific_modules":copy.deepcopy(admitted["scientific_modules"]),
        "complete_current_file_receipts":copy.deepcopy(admitted["current_receipts"]),
        "original_admission":copy.deepcopy(admitted["admission"]),
        "original_closure_admission":copy.deepcopy(admitted["original_closure_admission"]),
        "complete_restoration_receipts":restoration_reference(
            admitted["complete_restoration_receipts"],manifest,run,attempt,canonical,digest),
        "parameters":copy.deepcopy(PARAMETERS),"retained_scope":copy.deepcopy(RETAINED_SCOPE),
        "copied_same_operator_records":copy.deepcopy(admitted["same_operator_records"]),
        "copied_original_scope":copy.deepcopy(paired["scope"]),
        "copied_complete_candidate_metadata":copy.deepcopy(admitted["candidate_metadata"]),
        "copied_complete_repair_definition":copy.deepcopy(admitted["repair_definition"]),
        "retained_completed_five_maxima":copy.deepcopy(paired["completed_five_maxima"]),
        "retained_original_false_candidates":copy.deepcopy(paired["old_false_candidates"]),
        "prior_completed_candidate":compact_old_archive(
            completed["archive"],admitted["same_operator_records"],canonical,digest),
        "original_optical_records":copy.deepcopy(admitted["original_optical_records"]),
        "collar_native_identities":copy.deepcopy(admitted["collar_native_identities"]),
        "collar_original_contexts":lossless_context_table(
            admitted["collar_original_contexts"],canonical,digest),
        "reference_identity":None,"complete_support_contract":None,
        "preparation_prefix":{"stage":"not_started","detail":None,
                             "private_packets_are_not_independent_array_targets":True},
        "kernel_progress":{"count":0,"chain_sha256":None,"latest":None},
        "complete_new_graphs":{},"current_target":None,"completed_targets":[],
        "saved_record_counts":{name:0 for name in ORDERED_GRAPH_NAMES},
        "finite_gate":None,"conditional_finite_inverse":None,"gates":[],
        "actual_progress":{
            "current_files_admitted":len(admitted["current_receipts"]),
            "historical_files_admitted":len(admitted["complete_restored_input_map"]),
            "new_source_AST_count":admitted["admission"]["new_source_AST_count"],
            "old_source_AST_count":admitted["admission"]["old_source_AST_count"],
            "old_WVC_records_verified":56,"old_WVC_modal_prefix_records_verified":5,
            "old_WPS_records_verified":60,"old_WPS_modal_prefix_records_verified":6,
            "same_operator_records_copied":29,"original_optical_records_copied":2,
            "reference_definitions_materialized":0,"completed_new_centre_parents":0,
            "original_closed_rows_covered":0,"original_body_intersections":0,
            "comparison_cells":0,"new_graphs_completed":0,"new_scalar_records_saved":0,
            "new_strict_finite_comparisons":0,"conditional_finite_inverses":0,
            "old_targets_recomputed":0,"old_producer_imports_or_calls":0,
            "old_reference_bound_targets_reevaluated":0,"physical_state_columns_computed":0,
            "dense_full_finite_matrices_allocated":0,"new_arrays_published":0,
            "new_artifacts":0,"new_Releases":0},
        "runtime":{},"actual_mathematical_wall_seconds":0.0,
        "automatic_retry_authorized":False}
    require(sorted(document)==SCI_FIELDS,"whole output field schema before numerical work")
    math_start=None
    api=None
    prepared=False

    def publish(check_size=True):
        if math_start is not None:
            elapsed=time.perf_counter()-math_start
            require(math.isfinite(elapsed) and elapsed>=0,"finite elapsed wall time")
            document["actual_mathematical_wall_seconds"]=elapsed
        raw=canonical(document)
        temporary=output.with_name(output.name+".tmp")
        with temporary.open("wb") as stream:
            stream.write(raw);stream.flush();os.fsync(stream.fileno())
        os.replace(temporary,output)
        sys.stdout.write(raw.decode("utf-8"));sys.stdout.flush()
        restored=data(output.read_bytes())
        require(canonical(restored)==raw,"complete atomic output readback")
        if check_size:
            require(len(raw)<=MAX_SCIENTIFIC_BYTES,"complete scientific publication byte cap")
        return restored

    def gate(name,passed=True):
        n=len(document["gates"])
        require(n<len(GATE_LABELS) and name==GATE_LABELS[n],"complete gate order")
        document["gates"].append({"name":name,"passed":bool(passed)})
        publish()
        require(passed,name)

    def progress(stage,detail):
        require(isinstance(stage,str) and 0<len(stage)<=160
                and isinstance(detail,dict),"whole current private-work metadata")
        raw=canonical({"stage":stage,"detail":detail})
        require(len(raw)<=2000,"complete compact work metadata without coefficient arrays")
        previous=document["kernel_progress"]
        previous["count"]+=1
        previous["chain_sha256"]=digest(canonical({
            "previous":previous["chain_sha256"],"current":data(raw)}))
        previous["latest"]=data(raw)
        if not prepared:
            document["preparation_prefix"]={
                "stage":stage,"detail":copy.deepcopy(detail),
                "private_packets_are_not_independent_array_targets":True}
        if stage=="same_exact_reference_definition":
            document["actual_progress"]["reference_definitions_materialized"]=detail["parents_verified"]
        elif stage=="complete_new_centre_parent":
            document["actual_progress"]["completed_new_centre_parents"]=detail["parents_complete"]
            document["actual_progress"]["original_closed_rows_covered"]=detail["closed_rows_covered"]
            document["actual_progress"]["original_body_intersections"]=detail["closed_intersections"]
        elif stage=="complete_signed_kernel_inputs":
            document["actual_progress"]["comparison_cells"]=detail["comparison_cells"]
        document["stage"]="working:"+stage
        publish()

    def read_saved(record,endpoint="upper"):
        value=api.arb(record_text(record))
        require(value.is_finite(),"complete saved new scalar finite")
        if endpoint=="lower":
            require(value.lower()>0,"saved strictly positive directed gap")
            return value.lower()
        return api.upper(value)

    class Owner:
        def start_graph(self,name,declared_names):
            n=len(document["completed_targets"])
            require(n<len(ORDERED_GRAPH_NAMES) and name==ORDERED_GRAPH_NAMES[n]
                    and document["current_target"] is None
                    and name not in document["complete_new_graphs"],"one ordered whole new graph")
            allowed=GRAPH_RECORD_NAMES[name]+(CONDITIONAL_RECORD_NAMES
                if name==ORDERED_GRAPH_NAMES[-1] else [])
            require(declared_names==allowed,"whole declared scalar order")
            document["complete_new_graphs"][name]={"complete":False,"new_records":{}}
            document["current_target"]=name;document["stage"]="started:"+name
            publish()
            def emit(key,value,endpoint="upper"):
                graph=document["complete_new_graphs"][name]
                count=document["saved_record_counts"][name]
                require(document["current_target"]==name and count<len(allowed)
                        and key==allowed[count] and key not in graph["new_records"],
                        "new scalar saved exactly once in declared order")
                require(endpoint in ("upper","lower")
                        and ((endpoint=="lower")==(key=="complete_actual_finite_gap_lower")),
                        "only strict positive finite gap is a lower record")
                if endpoint=="lower":
                    require(value.is_finite() and value.lower()>0,"positive new gap")
                    value=value.lower()
                else:
                    value=api.upper(value)
                record={"ball":value.str(PARAMETERS["decimal_record_digits"])}
                graph["new_records"][key]=record
                document["saved_record_counts"][name]+=1
                document["actual_progress"]["new_scalar_records_saved"]+=1
                document["stage"]="record_saved:"+name
                restored=publish()
                return read_saved(restored["complete_new_graphs"][name]["new_records"][key],endpoint)
            return emit

        def finish_graph(self,name,passed=False):
            require(document["current_target"]==name,"same current whole graph")
            graph=document["complete_new_graphs"][name]
            expected=GRAPH_RECORD_NAMES[name]+(CONDITIONAL_RECORD_NAMES
                if name==ORDERED_GRAPH_NAMES[-1] and passed else [])
            require(list(graph["new_records"])==expected
                    and document["saved_record_counts"][name]==len(expected),
                    "all and only whole new graph records retained")
            for record in graph["new_records"].values():
                record_text(record)
            if name==ORDERED_GRAPH_NAMES[-1]:
                records=graph["new_records"]
                defect=read_saved(records["complete_actual_finite_defect_upper"])
                require(bool(defect<api.one)==bool(passed),"same strict saved finite comparison")
                document["finite_gate"]={
                    "comparison":"saved complete E0 upper + 3 D upper original_T upper < 1",
                    "complete_defect_record":copy.deepcopy(records["complete_actual_finite_defect_upper"]),
                    "complete_original_T_record":copy.deepcopy(
                        document["copied_same_operator_records"]["complete_actual_T_upper"]),
                    "passed":bool(passed),"false_sufficient_gate_does_not_prove_singularity":True,
                    "actual_tail_inverse_upper":3,
                    "actual_tail_gate_is_the_published_analytic_m160":True}
                document["actual_progress"]["new_strict_finite_comparisons"]=1
                if passed:
                    document["conditional_finite_inverse"]={
                        "operator":"actual finite Schur matrix in the unchanged WVC Hilbert coordinates",
                        "complete_gap_lower":copy.deepcopy(records["complete_actual_finite_gap_lower"]),
                        "complete_inverse_upper":copy.deepcopy(records["complete_actual_finite_inverse_upper"]),
                        "all_four_Schur_blocks_and_both_rhs_retained":True,
                        "genuine_root_even96_normalization_is_boundary_identity":True,
                        "physical_state_columns_not_numerically_materialized":True,
                        "other_readouts_require_their_true_complete_conversion":True}
                    document["actual_progress"]["conditional_finite_inverses"]=1
            graph["complete"]=True
            document["completed_targets"].append(name)
            document["current_target"]=None
            document["actual_progress"]["new_graphs_completed"]+=1
            document["stage"]="complete_graph_saved:"+name
            gate(name+"_saved")

    publish()
    try:
        for item in admitted["admission"]["checks"]:
            gate(item["name"],item["passed"])
        import flint
        require(platform.python_version()=="3.12.14" and flint.__version__=="0.9.0",
                "fixed public directed runtime")
        flint.ctx.prec=320
        api=NumericalAPI(flint)
        document["runtime"]={"Python":"3.12.14","python_flint":"0.9.0","bits":320,
            "old_module_imports":0,"numpy_imported":False,
            "whole_matrix_product":"python_flint.arb_mat"}
        gate("fixed_directed_runtime_and_one_new_entry")
        old={}
        for name,record in document["copied_same_operator_records"].items():
            if name in ("G_c","L_c_raw"):
                exact=Fraction(record)
                value=api.rational(exact.numerator,exact.denominator)
            else:
                value=api.old_interval(record)
            old[name]=api.upper(value)
        require(len(old)==29 and document["copied_same_operator_records"]==
                completed["copied_records"]
                and len(document["original_optical_records"])==2
                and PARAMETERS["actual_tail_inverse_bound"]==3,
                "all29 complete old values and same full-family optical eta")
        gate("all_twenty_nine_same_operator_records_typed_and_original_optical_eta_retained")
        collar=import_new_source(root,specs["collar_math"],"_w2c_new_collar_math")
        km=import_new_source(root,specs["kernel_math"],"_w2c_new_kernel_math")
        assembly=import_new_source(root,specs["assembly_math"],"_w2c_new_assembly_math")
        reference=import_new_source(root,specs["reference_math"],"_w2c_new_reference_math")
        require(assembly.GRAPH_NAMES==ORDERED_GRAPH_NAMES
                and all(assembly.record_names(name)==GRAPH_RECORD_NAMES[name]
                        for name in ORDERED_GRAPH_NAMES)
                and assembly.record_names(ORDERED_GRAPH_NAMES[-1],True)==
                    GRAPH_RECORD_NAMES[ORDERED_GRAPH_NAMES[-1]]+CONDITIONAL_RECORD_NAMES,
                "complete fixed five graphs and50 plus conditional2")
        math_start=time.perf_counter()
        context=assembly.prepare_complete_kernel_context(api,km,reference,collar,admitted,
            completed["complete_original_candidate"],old,core.signed_display_centre,progress)
        document["reference_identity"]=copy.deepcopy(context.reference_identity)
        require(context.reference_identity["original_reference_chain"]==
                    completed["complete_original_candidate"]["reference_chain"]
                and context.reference_identity["selected_diagonal_chain"]==
                    completed["selected_diagonal_chain"],
                "same whole original WVC definition and diagonal")
        gate("entire_fixed_WVC_reference_definition_and_diagonal_chains_materialized")
        document["complete_support_contract"]={
            "all_actual_qualifications":copy.deepcopy(context.qualifications),
            "ordinary_dr_pairing":True,"body_angular_coordinates":"true normalized real parity",
            "head_dimension":193,"reference_high_last_j":160,"trial_last_j":224,
            "repaired_centre_residual_last_j":288,"complete_family_residual_last_j":416,
            "all193_finite_Gf_observation_atoms":193,"actual_tail_inverse_last_j":None,
            "actual_high_inverse_is_not_finitely_truncated":True,
            "parent_definitions":context.parent_definition_count,
            "closed_original_rows":context.original_body_row_count,
            "closed_intersections":context.original_intersection_count,
            "comparison_cells":len(context.domain.cells),
            "fixed_original_reference_fine_cells":24480,
            "both_true_cutoff_derivatives_retained_in_primal_and_dual_residuals":True,
            "true_collar_primitive_adjoint_upper_limit":"R",
            "full_mean_and_all_seven_independent_ports_remain":True}
        require(context.parent_definition_count==153
                and context.original_body_row_count==4650
                and context.original_intersection_count==4801
                and len(context.domain.cells)<=155
                and all(value is True for value in context.qualifications.values())
                and document["actual_progress"]["reference_definitions_materialized"]==153
                and document["actual_progress"]["completed_new_centre_parents"]==153,
                "whole true-root collar and all body domains")
        prepared=True
        document["preparation_prefix"]={"stage":"complete",
            "detail":{"parent_definitions":153,"complete_centre_parents":153,
                "closed_original_rows":4650,"closed_intersections":4801,
                "comparison_cells":len(context.domain.cells)},
            "private_packets_are_not_independent_array_targets":True}
        gate("complete_true_collar_body_and_all_kernel_domains_admitted")
        signed=assembly.complete_joint_operator_graph(api,km,context)
        operators=assembly.complete_weighted_graph_operators(api,km,context,signed,
            context.family_fees,old)
        norms=assembly.CompleteGraphNorms(api,km,context)
        answer=assembly.evaluate_five_complete_graphs(api,norms,operators,old,Owner())
        passed=bool(answer["passed"])
        for spec in admitted["current_receipts"]:
            core.read_spec(root,spec)
        require(digest(Path(args.manifest).read_bytes())==args.manifest_sha,
                "complete unchanged manifest after new work")
        gate("all_current_inputs_and_manifest_reverified_after_new_work")
        expected_count=50+(2 if passed else 0)
        require(sorted(document)==SCI_FIELDS
                and document["completed_targets"]==ORDERED_GRAPH_NAMES
                and document["current_target"] is None
                and all(graph["complete"] is True
                        for graph in document["complete_new_graphs"].values())
                and document["actual_progress"]["new_scalar_records_saved"]==expected_count
                and sum(document["saved_record_counts"].values())==expected_count
                and document["actual_progress"]["new_graphs_completed"]==5
                and document["actual_progress"]["new_strict_finite_comparisons"]==1
                and document["finite_gate"]["passed"]==passed
                and (document["conditional_finite_inverse"] is not None)==passed
                and document["copied_same_operator_records"]==admitted["same_operator_records"]
                and document["original_optical_records"]==admitted["original_optical_records"]
                and all(document["actual_progress"][name]==0 for name in (
                    "old_targets_recomputed","old_producer_imports_or_calls",
                    "old_reference_bound_targets_reevaluated","physical_state_columns_computed",
                    "dense_full_finite_matrices_allocated","new_arrays_published",
                    "new_artifacts","new_Releases")),
                "all complete targets, false scopes, old-zero accounting and publication bounds")
        gate("complete_whole_candidate_shape_and_old_zero_recomputation")
        document["complete"]=True;document["proved"]=True
        document["stage"]="complete";document["actual_returncode"]=0
        publish()
        return 0
    except BaseException as error:
        trace=traceback.format_exc()
        sys.stderr.write(trace);sys.stderr.flush()
        document["complete"]=False;document["proved"]=False
        document["stage"]="failed_complete_prefix_preserved";document["actual_returncode"]=1
        document["failure"]={
            "type":bounded_diagnostic(type(error).__name__,128),
            "message":bounded_diagnostic(str(error),DIAGNOSTIC_MESSAGE_BYTES),
            "traceback":bounded_diagnostic(trace,DIAGNOSTIC_TRACEBACK_BYTES),
            "complete_traceback_printed_to_stderr":True,
            "all_completed_scalar_records_and_whole_graphs_retained":True,
            "current_unfinished_graph_preserves_its_entire_saved_record_prefix":True,
            "private_unfinished_packets_are_not_complete_scalar_targets":True,
            "automatic_retry_authorized":False}
        publish(check_size=False)
        return 1

if __name__=="__main__":
    raise SystemExit(main())
