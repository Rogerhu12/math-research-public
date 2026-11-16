#!/usr/bin/env python3
"""R442 metadata-only complete-M sampler/native necessary selection API.

All original actual record traversal is retained. The only modal changes are
the explicit new source/schema, actual M and full declared mode sequence.
No scientific module or interval arithmetic is imported. This API is called
by the one bounded R442 owner reader after actual process quiescence.
Author: exact_refinement agent (AI), 2026-11-16.
"""
from __future__ import annotations
import argparse
from collections import Counter, deque
import gzip
import hashlib
import json
import math
import os
import re
from pathlib import Path
import sys

REPOSITORY="Rogerhu12/math-research-public"
SCHEMA="R442-current-C-complete-M-native-necessary-api-v1"
SAMPLER_SCHEMA="current-C-complete-M-pruefer-joint-physical-radial-samples-and-general-far-v1"
SAMPLER_SHA="9a85d7d17796ea567cdcfdac567ee531fcf5c225bfe9f57699bbb403aead41c1"
LIMIT=90000
SOURCE_PINS={
    "geometry_20261115_stored_continuous_E_cover_v3.py": "f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df",
    "geometry_20261115_stored_continuous_E_cover_v2.py": "004010b681aa35635e15b229a3e5b78602b3ec480a631a761e42f6c7d563b6ea",
    "geometry_20261115_stored_continuous_E_cover.py": "9aa0da45027afa37ca329eab73e5e93e788f2bbafb908b9e8c2960f537a427ed",
    "tail_frozen_geometry.mjs": "db6664fcd7be618d2b684c39c01c53d97833d11e14af206b12c71e4b058713e3",
    "strong_frozen_calibration_factory.mjs": "77e9d2fc0e277ef69c9a4300ceba2d3d6b03056fc6a4868fab049a1a1c290247",
    "closure_bounded_point_cache.mjs": "35289a4de44ec409bc211f82c7a1bee81a10c6bc1c5fb31e4ca9a8634cc09043",
    "exact_20261114_closed_background.mjs": "be358bf780c88ebd85cdf07d9e8d2cc3b37ca20a4d8ea3a1ba69e7c40c2c4e1b",
    "exact_20261114_public_resume.py": "11399783f01b145ee3f23d88213af368daee9c16dfb858b40dd7316870b300a5",
    "source-dependencies.json": "7de25376ab0ec10277840ccdca8ec6b46b41bee6add97acd9d38c06bbc8cd941",
    "root_20261114_current576_rules_runner.py": "3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde",
    "geometry_20261115_stored_C_v3_cut_twojet_readout.py": "1c39b242224824b361cbe5d28ea838b7e4824f5506a05302c662f045f735aeed",
    "geometry_20261115_stored_continuous_C_far_graph.py": "fe66789e7d94ab014662250e90642ab7fda3084b39c00b93836459220b33bb2a",
    "geometry_20261115_stored_C_finite_head_flux.py": "4531b5b35093fa9c0010f9fdbd6700dcf4b099c076b5a3d69d20ccafda8af87d",
    "geometry_20261115_stored_C_finite_head_projective.py": "5440e2e0457b360120c180a2531e3db899d8534cf6366183fd68d111ede18216",
    "geometry_20261115_stored_C_finite_head_riccati.py": "34606e3fea2093f78cc3cb88fa6e5f7bcc32112c8f9053484628ad1a16e11124",
    "geometry_20261115_stored_C_finite_head_pruefer.py": "250474d748842d9b5423be2123460308ab16419d4b5dac1d8c9967fc208c0122",
    "geometry_20261115_current_C_general_robin_native.mjs": "fae2cb0fface7eadcc955fe09a07e9b59a7df8cd692bccc6cdf826c691eb8349",
    "geometry_20261115_current_C_synchronous_linear_bridge.mjs": "67e3b23c9e5306764db3d6b8e0392eb8f59d4b63bfb671a0703fe33b2146c286",
    "exact_20261115_current_C_general_robin_chain.py": "946251656306a6cbe137513e12bac305c7758e5ec7306995a63314bd0f400bb5",
    "geometry_20261115_current_C_projective_native_launch.py": "ae54abbb383269cbd2fd111c08a103b7eb8a14b15db01d09c2fcc8227488bf9d",
    "root_20261115_current_C_projective_native_scalar_readout.py": "8a3ddc5d59244b245292bd5a0e3fb33768527017148cc4e697d2f2cf771989e7",
    "exact_20261114_tail_capacity_loader.mjs": "07d45b95a970d38489c17142b9202ceeca648a549f76cecaba7c7036261fa395",
    "geometry_20261114_noj_matched_variational_engine.mjs": "f9b292c4c3f80d1d7b3030ea0350416746795377833661af8d3095e349a73ad9",
    "exact_20261114_native_damped_chain_qr.py": "9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33",
    "geometry_20261115_current_C_pruefer_joint_radial_sampling.py": "32b0b7e2b02f54f5086b6c9485c1f63bce4702c3a690fed49bbc78d9d690d5f4",
    "geometry_20261115_current_C_pruefer_joint_native_worker.mjs": "d015a52c126b26a749ed1dfd60d613fdf09c54826a9465c7e38824d41bda6e4a",
    "geometry_20261115_current_C_pruefer_joint_tail_client.py": "02e1645248ef01ffff10a50c2198194fafd40709254816408e1b9944e1cd0ae1",
    "geometry_20261115_stored_C_finite_head_pruefer_positive.py": "c2f515aa276890da63871fe0e9e1440775950d4985465457e9d6025976d914c8",
    "geometry_20261115_pruefer_positive_endpoints.py": "91dd207bc20a87a36e2d4bc13e1b88a14333b67cf47ec048f85e8d46500822ff",
    "geometry_20261115_pruefer_joint_row_representative.py": "24c7681c75d5615bcfbfa7b14cdf0155a858bf09578f856433313408b6a16e97",
    "geometry_20261116_current_C_M_general_robin_native.mjs": "fb951f3688673a01b698bb7c606d6a854c061816e139bae55e51a176b4439f8c",
    "geometry_20261116_current_C_M_synchronous_linear_bridge.mjs": "8f189c095ec5bfbc3c323e2421cd98f931931334603ec902a94a75a60a3854de",
    "exact_20261116_current_C_M_general_robin_chain.py": "d4f6d4ffa7f54c38fb251ed72ef7d5bcdd8c5371c99506b0b8d98095506c3737",
    "geometry_20261116_current_C_M_pruefer_joint_radial_sampling.py": "9a85d7d17796ea567cdcfdac567ee531fcf5c225bfe9f57699bbb403aead41c1",
    "geometry_20261116_current_C_M_pruefer_joint_native_worker.mjs": "17a58fde59a4dbc126bce6c7f4584edf74a94690ec0aace831a31f10783c8509",
    "geometry_20261116_current_C_M_pruefer_joint_tail_client.py": "ab326e5b4814341b9cf6fbb054d56e8183e4560922c16878a4c57ca6620b135d",
    "geometry_20261116_stored_C_finite_M_head_pruefer_positive.py": "82a3f3e28e506320f474c64fd50d9ceadf3b39e9de9dc07f70c3df3c5c66bde6",
    "geometry_20261116_stored_continuous_C_M_far_graph.py": "5f16872e6e2e71914a73345b2f9b9142dbb0a7438e68805033a3277d3eb3d528",
    "geometry_20261116_continuous_ten_frozen_M_refinement.py": "395da6c8d43c0d31e59c58a2089fb4b116900a9b3192fa8d76456fc680adde12",
    "geometry_20261116_current_C_frozen_M_owned_launch.py": "47fc1aba734742c67d772eac7479a4f56165f711c5f646f4ff6e47c17c53829b"
}
RAW_KEYS={"states","augmented_states","rhs","augmented_rhs","mesh","public_u",
    "heightJetJacobian","jacobian","matrix","matrices","factors","factor_arrays",
    "complete_numeric_compilation","original_mesh_float64le","public_u_float64le",
    "actual_new_mesh_float64le","original_active_parameter_float64le",
    "original_shallow_rows","original_reference_field_arrays","complete_factors",
    "current_C_full112_implementation","current_C_complete_M_implementation","current_profile_binding","current_exact_profile_binding",
    "current_native_binding","current_native_geometry_binding","current_C_common_input_binding",
    "consumed_source_sha256","frozen_original_sources","actual_current_profile_binding",
    "exact_target_binding","accurate_family_binding","current_C_profile_binding",
    "r300_source_binding","implementation","original_metric_identity","complete_scalar_profile",
    "numeric_geometry_identity","original_C_input_binding","actual_original_input_binding"}
SEEN={}
ERRORS=[]
OMISSIONS=[]
DOCUMENTS=[]
LOGS=[]
FAR_MODE_COLUMNS=["m","complete","complete_required_far_propagation","unit_family_complete",
    "accepted","coarse","range_splits","norm_splits","Taylor_work_splits",
    "angle_lift_splits","row_norm_splits","candidates","unit_rows","norm_unproved",
    "required_leaves","completed_leaves","error","last_source_panel","last_piece","last_parameter",
    "original_row_sha256"]
NUMERIC_ROW_COLUMNS=["m","complete_numeric_row","source_panel","source_piece","inverse_leaf",
    "precision_bits","precision_attempts","old_Q_center_exact_zero","old_Pi_center_exact_zero",
    "old_Q_nonzero_center_rounded_zero","old_Pi_nonzero_center_rounded_zero","old_pair_both_zero",
    "Q_numeric_value","Q_f64le","Pi_numeric_value","Pi_f64le","actual_error"]
TRIAL_COLUMNS=["iteration","trial","step","alpha","baseNorm","trialNorm","accepted",
    "reason","guard","stage","row","error","original_row_sha256"]
NATIVE_COLUMNS=["directory","call","normalizedResidual","converged","current_native_completed",
    "last_withJ_norm","audit","predicted","actual_nonlinear_solve","minA","minD",
    "history_count","trial_count","last_iteration","state_sha256","J_length","J_sha256",
    "error","original_request_sha256","original_result_or_failure_sha256"]
LINEAR_COLUMNS=["directory","call","iteration","kind","eta","completed","failed",
    "rows","rhs_columns","complete_factorization","completed_factor_nodes",
    "pending_factor_nodes","minimum_triangular_diagonal_original","exact_direction_maximum",
    "all_original_numeric_maxima_by_rhs","error","result_sha256","snapshot_sha256"]
BVP_FIELDS=("schema","source_sha256","phase","success","new_coupled_finite_acceptance",
    "new_coupled_finite_acceptance_refers_to","full_Cartesian_closed_surface",
    "exact_R300_target_or_continuous_C_DN_certified","state_dimension","physical_state_dimension",
    "left_rows","right_rows","nodes","current_outer_iteration","initial_collocation_max",
    "preflight_added_nodes","outer_history","physical_RMS_max","physical_node_relative_residual",
    "original_full_DN_phase","original_full_DN_exit_status","original_boundary_FD_passed",
    "maximum_boundary_FD_relative_error","exception","traceback","native_close_exception",
    "native_owner_closed","native_owner_close_exception","actual_protocol_solve_entries",
    "complete_nine_scalar_parameters","sampled_geometry_scalar_parameters","M","N",
    "inner_success","status","message","collocation_rms_max","boundary_residual_max",
    "physical_test_final_cut_audit","actual_tail_boundary_max","audited_boundary_max",
    "same_metric_refinement","complete_closed_surface","elapsed_seconds","scalar_parameters",
    "physical_frozen_control_RMS_max","constant_core_state_drift","constant_parameter_state_drift",
    "height_seam","summary","core","native_live_calls","native_owner_close_attempted")
FD_FIELDS=("schema","physical_test_schema","maximum_relative_directional_error",
    "maximum_second_order_relative_directional_error","maximum_fourth_order_relative_directional_error",
    "verification_threshold","verification_estimator","second_order_truncation_contracts",
    "implementation_check_passed","actual_current_H_solved_before_this_FD",
    "FD_perturbed_states_use_explicit_affine_map","zero_anchor_J_not_relabelled_as_current_H_J",
    "original_three_perturbations_directions_steps_and_threshold_unchanged",
    "same_live_client_will_be_retained_if_FD_passes","full_BVP_solved",
    "full_Cartesian_closed_surface","prepared_sha256","native_anchor_response_sha256",
    "direct_boundary","separated_boundary")
SAMPLER_FIELDS=("schema","source_sha256","target_model_schema","repository","run_id","source_commit",
    "completed","native_geometry_ready","error","old_graphs_or_gains_used",
    "no_height_division_in_far_rows","exact_global_C_realization_of_numeric_representatives_certified",
    "nonlinear_solve_or_DN_computed","closed_field_or_BVP_accepted",
    "actual_original_scope_conditions","actual_far_radius_choice","actual_far_modes_attempted",
    "actual_far_modes_completed","actual_not_started_far_modes","actual_point_count",
    "actual_inverse_range_count","actual_coarse_valid_point_leaves","linear_phase_attempts",
    "sampling_phase_attempts","elapsed_seconds","complete_native_field_occurrences",
    "complete_unique_sample_points","numerical_sample_work_resolution_complete","grid_identity",
    "actual_far_coordinate_mu_word","complete_factorized_far_modes","complete_unit_far_row_modes",
    "linear_phase_resource_receipt","sampling_phase_resource_receipt","actual_R380_proof","actual_R357_proof",
    "original187_sampler_source_sha256","joint_nominal_row_source_sha256",
    "joint_nominal_representation_precision_cap_bits",
    "same_complete_uncertain_root_family_and_all_candidate_units_retained",
    "nominal_parameter_point_is_not_selected_exact_global_C")

def actions():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY:
        raise RuntimeError("Actual temporary output readback belongs to this public repository Actions")

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def canonical(value):
    return (json.dumps(value,ensure_ascii=True,sort_keys=True,separators=(",",":"),
        allow_nan=False)+"\n").encode("utf-8")

def require(value,message):
    if not value:
        raise ValueError(message)

def short(text,limit=1800):
    text=str(text)
    try:
        raw=text.encode("utf-8")
        original_UTF8=True
    except UnicodeEncodeError:
        try:
            raw=text.encode("utf-8",errors="surrogateescape")
        except UnicodeEncodeError:
            raw=text.encode("utf-8",errors="surrogatepass")
        original_UTF8=False
    if len(raw)<=limit and original_UTF8:
        return text
    return dict(original_or_surrogate_mapped_bytes=len(raw),mapped_bytes_sha256=sha(raw),
        prefix=raw[:limit].decode("utf-8",errors="replace"),
        prefix_limit_bytes=limit,complete_text_not_exported=True,
        invalid_or_split_UTF8_display_not_original_bytes=True)


def fail(scope,error,**more):
    ERRORS.append(dict(scope=scope,type=type(error).__name__,message=short(error,1200),**more))

def contained(root,relative):
    root=Path(root).resolve()
    relative=Path(relative)
    require(not relative.is_absolute(),"Contained original payload path required")
    path=root/relative
    require(path.resolve()!=root and root in path.resolve().parents,"Payload escaped actual owned root")
    cursor=path
    while cursor!=root:
        require(not cursor.is_symlink(),"Symlink is not a preserved original payload")
        cursor=cursor.parent
    return path

def identity(path):
    path=Path(path)
    require(not path.is_symlink(),"No symlink identity")
    before=path.stat()
    stamp=(before.st_ino,before.st_size,before.st_mtime_ns)
    cached=SEEN.get(str(path))
    if cached and cached[0]==stamp:
        return dict(cached[1])
    h=hashlib.sha256();count=0
    with path.open("rb") as stream:
        while block:=stream.read(1048576):
            h.update(block);count+=len(block)
    after=path.stat()
    require(stamp==(after.st_ino,after.st_size,after.st_mtime_ns),"File changed during whole-byte read")
    value=dict(file=path.name,bytes=count,sha256=h.hexdigest())
    SEEN[str(path)]=(stamp,value)
    return dict(value)

def descriptor(root,record):
    require(isinstance(record,dict),"Original descriptor object required")
    path=contained(root,record["file"])
    got=identity(path)
    require(got["bytes"]==record["bytes"] and got["sha256"]==record["sha256"],
        "Original descriptor bytes/SHA mismatch: "+record["file"])
    return dict(record)

def decode(raw):
    return json.loads(raw,parse_constant=lambda token:dict(original_nonstandard_JSON_constant=token))

def document(path,scope,required=False):
    path=Path(path)
    if not path.is_file():
        if required:
            fail(scope,FileNotFoundError("Required actual file absent: "+str(path)))
        return None,None
    try:
        record=identity(path);raw=path.read_bytes()
        require(len(raw)==record["bytes"] and sha(raw)==record["sha256"],"File changed before parsing")
        plain=gzip.decompress(raw) if raw[:2]==b"\x1f\x8b" else raw
        value=decode(plain)
        DOCUMENTS.append(dict(scope=scope,**record,parsed=True))
        return value,record
    except Exception as error:
        record=identity(path) if path.is_file() else None
        fail(scope,error,original_file=record,unparsed_complete_bytes_not_exported=True)
        return None,record

def raw_member(value,path):
    raw=canonical(value)
    record=dict(path=list(path),canonical_bytes=len(raw),canonical_sha256=sha(raw))
    if isinstance(value,list):
        record["members"]=len(value)
    OMISSIONS.append(record)
    return dict(original_member_identity=record,not_exported=True)

def small(value,path=()):
    if isinstance(value,dict):
        out={}
        for key,item in value.items():
            loc=path+(str(key),)
            out[key]=raw_member(item,loc) if key in RAW_KEYS else small(item,loc)
        return out
    if isinstance(value,list):
        if len(value)>16:
            return raw_member(value,path)
        return [small(v,path+(str(i),)) for i,v in enumerate(value)]
    if isinstance(value,str):
        return short(value,1800)
    if isinstance(value,float) and not math.isfinite(value):
        return dict(original_nonfinite_parsed_number=repr(value))
    return value

def select(value,keys):
    if not isinstance(value,dict):
        return None
    return {key:small(value[key],(key,)) for key in keys if key in value}

def endpoints(value):
    if value is None:
        return None
    require(isinstance(value,dict) and "lower" in value and "upper" in value,
        "An actual interval must retain its original two dyadic endpoints")
    return [value["lower"]["mantissa"],value["lower"]["binary_exponent"],
        value["upper"]["mantissa"],value["upper"]["binary_exponent"]]


def display(value):
    return value.get("display") if isinstance(value,dict) else value

def state_view(value):
    if not isinstance(value,dict):
        return None
    chart=value.get("chart_index");vector=value.get("normalized_vector") or []
    return dict(chart=chart,balance=value.get("flux_balance_power_of_two"),
        sign=value.get("amplitude_sign"),
        ratio=endpoints(vector[1-chart]) if chart in (0,1) and len(vector)==2 else None,
        logabs_original_display=display(value.get("log_absolute_amplitude")),
        factor_count=value.get("complete_amplitude_factor_count"),
        factor_chain_sha256=value.get("complete_amplitude_factor_chain_sha256"),
        original_complete_state_canonical_sha256=sha(canonical(value)),
        full_log_and_other_state_witness_not_exported=True)

def error_view(value):
    if value is None:
        return None
    return small(value)

def barrier_view(value):
    if not isinstance(value,dict):
        return None
    tube=value.get("complete_closed_auxiliary_tube") or []
    return dict(exact_A=value.get("exact_A"),exact_B=value.get("exact_B"),
        initial=value.get("exact_initial_ratio"),closed_time=value.get("exact_closed_time_interval"),
        norm_split=value.get("needs_norm_split"),
        denominator_positive=value.get("complete_closed_denominator_strictly_positive"),
        entire_denominator=endpoints(tube[0]) if tube else None,
        endpoint_ratio=endpoints(value.get("endpoint_ratio_enclosure")),
        column_Taylor_error_original=display(value.get("whole_tube_column_Taylor_error_bound")),
        original_complete_barrier_sha256=sha(canonical(value)))

def last_failure(value):
    if not isinstance(value,dict):
        return None
    candidate=value.get("candidate") or {}
    return dict(original_source_panel_row=value.get("original_source_panel_row"),
        closed_parameter_interval=value.get("closed_parameter_interval"),
        subdivision_depth=value.get("subdivision_depth"),
        incoming_state=state_view(value.get("incoming_factorized_state")),
        error=error_view(value.get("error")),
        needs_norm_split=candidate.get("needs_norm_split"),
        needs_barrier_split=candidate.get("needs_barrier_split"),
        lower=barrier_view(candidate.get("lower_exact_comparison_barrier")),
        upper=barrier_view(candidate.get("upper_exact_comparison_barrier")),
        far_row_norm_conditions=small(value.get("candidate_row_norm_conditions")),
        original_complete_failure_sha256=sha(canonical(value)),
        full_matrices_and_witnesses_not_exported=True)

def unpaid_view(row,index,line_sha):
    keep=("kind","physical_frequency","physical_far_word","remaining_modes","all_required_modes",
          "all_native_stages_unstarted","complete_pending_scope","last_paid",
          "complete_native_geometry_not_returned","attempted_modes_with_unpaid_unit_rows",
          "complete_native_field_occurrences_done","all_remaining_field_plan_preserved",
          "completed_far_modes","unstarted_far_modes","error","complete_family_candidate_count",
          "complete_unit_row_count","row_norm_unproved_count","entire_mode_spatial_scope_remains_partial",
          "original_QF_one_column_not_materialized","no_unread_point_or_row_claimed_complete")
    value={key:row[key] for key in keep if key in row}
    # A complete pending stack/suffix is essential, never count-capped.
    last=value.get("last_paid")
    if isinstance(last,dict):
        value["last_paid"]={key:item for key,item in last.items() if key!="complete_factorized_state"}
        value["last_paid"]["state"]=state_view(last.get("complete_factorized_state"))
    if "error" in value:
        value["error"]=error_view(value["error"])
    value.update(original_row_index=index,original_line_sha256=line_sha,
        current_state=state_view(row.get("complete_current_state")),
        last_unaccepted=last_failure(row.get("last_unaccepted_candidate")))
    transaction=row.get("uncommitted_transaction")
    if transaction is not None:
        value["uncommitted_transaction"]=select(transaction,("transaction_index",
            "original_source_panel_row","closed_parameter_interval","prepared_panel_row",
            "prepared_far_rows"))
        value["uncommitted_transaction_original_sha256"]=sha(canonical(transaction))
    return value

def line_stream(path,scope,callback=None,expected=None):
    path=Path(path)
    if not path.is_file():
        if expected is not None:
            fail(scope,FileNotFoundError("Declared original stream absent"))
        return None
    got=identity(path)
    if expected:
        require(got["bytes"]==expected["bytes"] and got["sha256"]==expected["sha256"],
            "Original stream identity mismatch: "+scope)
    count=parsed=0;decoded_hash=hashlib.sha256();decoded_bytes=0
    opener=gzip.open if path.name.endswith(".gz") else open
    with opener(path,"rb") as stream:
        for index,raw in enumerate(stream):
            count+=1;decoded_hash.update(raw);decoded_bytes+=len(raw)
            if not raw.endswith(b"\n"):
                fail(scope,ValueError("Unterminated original JSONL tail"),
                    original_row_index=index,tail_bytes=len(raw),tail_sha256=sha(raw),
                    original_tail_necessary_excerpt=short(raw.decode("utf-8",errors="surrogateescape"),1200),
                    complete_tail_not_exported=True)
            if callback is None:
                continue
            original=raw
            if raw.startswith(b"\xef\xbb\xbf"):
                raw=raw[3:]
            if not raw.strip():
                fail(scope,ValueError("Empty original JSONL row"),original_row_index=index)
                continue
            try:
                value=decode(raw);parsed+=1
                callback(value,index,sha(original))
            except Exception as error:
                fail(scope,error,original_row_index=index,original_line_bytes=len(original),
                    original_line_sha256=sha(original),
                    original_line_necessary_excerpt=short(original.decode("utf-8",errors="surrogateescape"),1200),
                    complete_bad_line_not_exported=True)
    if expected and isinstance(expected.get("rows"),int):
        require(count==expected["rows"],"Original declared row count mismatch: "+scope)
    return dict(**got,rows=count,parsed_rows=parsed,
        decoded_stream_bytes=decoded_bytes,decoded_stream_sha256=decoded_hash.hexdigest(),
        whole_original_bytes_hashed=True,
        parse_scope="all original rows parsed in Actions" if callback is not None else "byte identity and line count only")

def log_view(path,scope):
    path=Path(path)
    if not path.is_file():
        return None
    ident=identity(path);first=[];last=deque(maxlen=1);matches=0;lines=0
    pattern=re.compile(r"Traceback|(?:^|[\s])(?:[A-Za-z_][A-Za-z0-9_.]*(?:Error|Exception)|Error|Exception|SystemExit):|\b(?:EPIPE|ENOSPC|SIGTERM|SIGKILL|SIGINT)\b|^Killed|^Terminated|Unhandled rejection")
    with path.open("rb") as stream:
        for number,raw in enumerate(stream):
            lines+=1
            text=raw.decode("utf-8",errors="surrogateescape")
            if pattern.search(text):
                matches+=1
                item=dict(line=number,original_bytes=len(raw),original_sha256=sha(raw),excerpt=short(text,1200))
                if len(first)<2:
                    first.append(item)
                last.append(item)
    value=dict(scope=scope,original_file=ident,complete_lines=lines,
        original_error_matched_lines=matches,first_error_lines=first,
        last_error_lines=list(last),selection_rule="literal exception/traceback/signal/storage-error lines only",
        full_log_text_not_exported=True,absence_of_selected_error_not_scientific_success=True)
    LOGS.append(value)
    return value


def sampler_readback(directory,expected):
    directory=Path(directory);errors_before=len(ERRORS)
    doc,record=document(directory/"result.json","sampler-result")
    if doc is None:
        return dict(available=False,actual_result=record,no_missing_geometry_inferred=True)
    require(doc.get("schema")==SAMPLER_SCHEMA and doc.get("source_sha256")==SAMPLER_SHA,
        "Independent actual joint-nominal sampler identity required")
    require(doc.get("run_id")==os.environ["GITHUB_RUN_ID"] and
        doc.get("source_commit")==os.environ["GITHUB_SHA"],"Same actual run sampler required")
    if expected:
        require(record["sha256"]==expected,"Actual sampler result SHA differs")
    M=doc.get("field_modes")
    require(type(M) is int and M>=112,"Actual complete-M sampler dimension required")
    modes=list(range(2,2*M+1,2))
    require(doc.get("complete_requested_modes")==modes,"The complete declared physical mode sequence differs")
    result=select(doc,SAMPLER_FIELDS)
    result.update(field_modes=M,complete_requested_modes=modes)
    result["sampler_required_result_present_and_bound"]=True
    result["actual_result"]=record
    for key in ("actual_far_modes_attempted","actual_far_modes_completed",
            "actual_not_started_far_modes","complete_factorized_far_modes","complete_unit_far_row_modes"):
        if key in doc:
            result[key]=doc[key]
    result["full_input_binding_canonical_sha256"]=sha(canonical(doc.get("actual_original_input_binding")))
    modes=[];mode_unpaid=[];unpaid=[];coverage_unpaid=[];coverage_count=Counter();tube_count=Counter()
    streams={};numeric_rows=[];numeric_by_mode={};numeric_status_counts=Counter();numeric_failures=[]
    def numeric(row,index,line_sha):
        m=row.get("physical_frequency");seed=row.get("source_candidate") or {}
        attempts=row.get("precision_attempts") or [];last=attempts[-1] if attempts else {}
        old=row.get("original_independent_component_midpoints") or [{},{}]
        if len(old)!=2:raise ValueError("Actual original numeric midpoint pair was not complete")
        words=row.get("actual_numeric_row") or [{},{}]
        if len(words)!=2:raise ValueError("Actual joint numeric row pair was not complete")
        require(m not in numeric_by_mode,"Duplicate actual numeric row selection mode")
        numeric_by_mode[m]=row;numeric_status_counts[str(row.get("status"))]+=1
        numeric_rows.append([m,row.get("complete_numeric_row"),seed.get("original_source_panel_row"),
            seed.get("source_piece"),seed.get("possible_inverse_leaf_row"),last.get("precision_bits"),
            len(attempts),old[0].get("exact_center_zero"),old[1].get("exact_center_zero"),
            old[0].get("nonzero_exact_center_rounded_to_zero"),old[1].get("nonzero_exact_center_rounded_to_zero"),
            row.get("original_independent_binary64_pair_both_zero"),
            words[0].get("value"),words[0].get("f64le"),words[1].get("value"),words[1].get("f64le"),
            error_view(row.get("actual_error"))])
        if row.get("complete_numeric_row") is not True:
            numeric_failures.append(dict(physical_frequency=m,status=row.get("status"),
                actual_error=error_view(row.get("actual_error")),
                original_row_index=index,original_line_sha256=line_sha,
                actual_failed_physical_frequency=row.get("actual_failed_physical_frequency"),
                actual_remaining_numeric_mode_suffix=row.get("actual_remaining_numeric_mode_suffix"),
                source_candidate_address=select(seed,("original_source_panel_row","source_piece",
                    "possible_inverse_leaf_row","transaction_index","coefficient_row",
                    "closed_step_interval","closed_leaf_intersection")),
                exact_input_precision_bits=row.get("minimum_exact_input_precision_bits"),
                representation_precision_cap_bits=row.get("nominal_representation_precision_cap_bits"),
                complete_family_propagation_failure_not_inferred=True))
    def mode(row,index,line_sha):
        last=row.get("last_paid") or {}
        modes.append([row.get("physical_frequency"),row.get("complete"),
            row.get("complete_required_far_propagation"),row.get("complete_unit_row_family_enclosed"),
            row.get("accepted_panels"),row.get("valid_coarse_panels"),
            row.get("coefficient_range_splits"),row.get("norm_work_splits"),row.get("defect_work_splits"),
            row.get("uncertain_angle_lift_splits"),row.get("uncertain_far_row_norm_splits"),
            row.get("candidate_count"),row.get("complete_unit_row_count"),row.get("row_norm_unproved_count"),
            row.get("required_leaf_count"),row.get("completed_leaf_count"),error_view(row.get("error")),
            last.get("original_source_panel_row"),last.get("source_piece"),last.get("parameter"),line_sha])
        if row.get("error") is not None or not row.get("complete"):
            mode_unpaid.append(unpaid_view(dict(row,kind="original-mode-necessary-unpaid",
                complete_current_state=row.get("complete_current_factorized_state")),index,line_sha))
    def leaf(row,index,line_sha):
        coverage_count[str(row.get("physical_frequency"))]+=1
        if not row.get("complete_original_inverse_leaf_spatial_scope_paid") or row.get("unit_row_norm_unproved_count"):
            coverage_unpaid.append(dict(original_row_index=index,original_line_sha256=line_sha,
                original_row=row))
    def tube(row,index,line_sha):
        tube_count[str(row.get("physical_frequency"))]+=1
    callbacks={"far-all-mode-rows":mode,
        "complete-unpaid-scope":lambda row,i,h:unpaid.append(unpaid_view(row,i,h)),
        "far-inverse-leaf-coverage":leaf,"far-complete-tubes":tube,
        "numeric-far-row-selection":numeric}
    for name,d in doc.get("detailed_ledgers",{}).items():
        try:
            streams[name]=line_stream(contained(directory,d["file"]),"sampler/"+name,
                callbacks.get(name),d)
        except Exception as error:
            fail("sampler/"+name,error)
    result.update(mode_columns=FAR_MODE_COLUMNS,all_attempted_mode_rows=modes,
        complete_necessary_unpaid=unpaid or mode_unpaid,unpaid_inverse_leaves=coverage_unpaid,
        mode_unpaid_fallback_used=not bool(unpaid),
        all_original_mode_unpaid_rows_also_parsed_but_duplicate_state_not_exported=True,
        all_original_stream_identities=streams,
        all_inverse_leaf_counts_by_mode=dict(coverage_count),
        all_candidate_counts_by_mode_from_actual_stream=dict(tube_count),
        complete_candidate_and_leaf_records_parsed_in_Actions=(len(ERRORS)==errors_before),
        successful_candidate_tubes_matrices_logs_and_rows_not_exported=True,
        coefficient_prepared_commit_streams_byte_count_only_not_numeric_audit=True,
        numeric_row_columns=NUMERIC_ROW_COLUMNS,all_actual_numeric_row_selections=numeric_rows,
        numeric_row_status_counts=dict(numeric_status_counts),actual_numeric_row_failures=numeric_failures,
        numeric_row_modes_not_started=[m for m in modes if m not in numeric_by_mode],
        all_actual_numeric_row_records_parsed_in_Actions=(len(ERRORS)==errors_before),
        complete_family_and_numeric_word_error_ledgers_not_exported=True,
        no_original187_failed_mode_or_midpoint_reconstructed=True)
    rowdoc,rowid=document(directory/"actual-general-far-row-intervals-and-representatives.json","general-far-rows")
    if rowdoc is not None:
        require(rowdoc.get("schema")==SAMPLER_SCHEMA+"-all_M-general-far-rows",
            "Actual same-sampler general far row identity required")
        require(len(rowdoc.get("complete_rows",[]))==M,"Actual general far JSON must retain all M original rows")
        candidates=[];all_actual_words_match=True;all_error_fields_retained=True
        for row in rowdoc.get("complete_rows",[]):
            m=row.get("physical_frequency");selection=numeric_by_mode.get(m)
            require(selection is not None and selection.get("complete_numeric_row") is True,
                "Complete general row lacks its actual numerical selection record")
            a,b=row.get("complete_Q_coefficient") or {},row.get("complete_Pi_coefficient") or {}
            actual=[a.get("actual_word"),b.get("actual_word")]
            require(actual==selection.get("actual_numeric_row"),
                "Actual returned numeric words and their original selection record differ")
            candidates.append([m,row.get("candidate_count")])
            all_error_fields_retained=all_error_fields_retained and all(
                isinstance(v.get("difference_exact_quantity_minus_numeric_word"),dict)
                for v in (a,b))
        result.update(general_far_original_json=rowid,
            complete_general_row_count=len(rowdoc["complete_rows"]),
            all_general_row_words_match_original_selection_records=all_actual_words_match,
            all_general_row_family_to_word_error_fields_retained=all_error_fields_retained,
            general_row_candidate_counts=candidates,
            original_complete_general_rows_and_error_bounds_read_but_not_exported=True,
            original_row_error_fields_not_recomputed=True)
    if doc.get("geometry"):
        try:
            descriptor(directory,doc["geometry"])
            geometry,gid=document(contained(directory,doc["geometry"]["file"]),"native-geometry",True)
            require(geometry is not None,"Actual geometry JSON parse required")
            result["actual_geometry"]=gid
            result["geometry_scope"]=select(geometry,("schema","model_schema","modes","spacing","orientation",
                "stage_count","rawNode","cut_radius","finite_far_radius","steps_per_stage","field_count_per_stage",
                "coordinate_mu_rule","native_old_graphs_or_gains_used",
                "finite_far_rows_are_nondividing_approximations_with_bound_error",
                "exact_global_same_C_and_infinite_nonlinear_DN_not_certified"))
            result["complete_native_arrays"]={name:descriptor(directory,d)
                for name,d in geometry.get("arrays",{}).items()}
        except Exception as error:
            fail("native-geometry",error)
    return result

def native_call(directory):
    directory=Path(directory);errors_before=len(ERRORS)
    request,request_id=document(directory/"request.json","native-request")
    answer,answer_id=document(directory/"native-result.json","native-result")
    failure,failure_id=document(directory/"native-failure.json","native-failure")
    request_failure,request_failure_id=document(directory/"request-failure.json","native-request-failure")
    initial,initial_id=document(directory/"initial-guess.json","native-initial")
    doc=answer if answer is not None else failure
    doc=doc or {}
    history_count=0;trial_count=0;last_iteration=None;last_trials=[];last_baseline=None
    ids={}
    def trace(row,index,line_sha):
        nonlocal history_count,last_baseline
        history_count+=1
        last_baseline=select(row,("event","iteration","norm","normalizedResidual","minA","minD",
            "withJ","accepted","step","alpha","error","state_sha256"))
        d=row.get("complete_actual_states")
        if d:
            descriptor(directory,d)
    def trial(row,index,line_sha):
        nonlocal trial_count,last_iteration,last_trials
        trial_count+=1;iteration=row.get("iteration")
        if iteration!=last_iteration:
            last_iteration=iteration;last_trials=[]
        last_trials.append([row.get(key) if key not in ("error","guard","reason") else error_view(row.get(key))
            for key in TRIAL_COLUMNS[:-1]]+[line_sha])
    for name,callback in (("native-trace.jsonl",trace),("native-trials.jsonl",trial)):
        path=directory/name
        if path.is_file():
            ids[name]=line_stream(path,directory.name+"/"+name,callback)
    if not ids:
        # Explicit fallback only when no original standalone streams exist.
        for row in doc.get("history",[]):
            trace(row,history_count,sha(canonical(row)))
        for row in doc.get("trialRecords",[]):
            trial(row,trial_count,sha(canonical(row)))
    cp=doc.get("checkpoint") or {}
    for key in ("raw_states",):
        if cp.get(key):
            descriptor(directory,cp[key])
    if doc.get("actual_complete_states"):
        descriptor(directory,doc["actual_complete_states"])
    J=doc.get("heightJetJacobian")
    state_sha=doc.get("state_sha256")
    result_id=answer_id or failure_id
    row=[directory.name,doc.get("call",(request or {}).get("call")),doc.get("normalizedResidual"),
        doc.get("converged"),doc.get("current_native_completed"),doc.get("last_withJ_norm"),
        doc.get("audit"),doc.get("predicted"),doc.get("actual_nonlinear_solve"),doc.get("minA"),
        doc.get("minD"),history_count,trial_count,last_iteration,state_sha,
        len(J) if isinstance(J,list) else None,sha(canonical(J)) if J is not None else None,
        error_view(doc.get("error") or (request_failure or {}).get("error")),
        (request_id or {}).get("sha256"),(result_id or {}).get("sha256")]
    height=(request or {}).get("height")
    height_record=None
    if isinstance(height,list):
        height_record=dict(call=(request or {}).get("call"),height=height,
            height_negative_zero_columns=(request or {}).get("height_negative_zero_columns"),
            height_sha256=(request or {}).get("height_sha256"),
            original_request=request_id)
    detail=dict(directory=directory.name,original_stream_identities=ids,last_baseline=last_baseline,
        last_actual_iteration=last_iteration,last_actual_iteration_trials=last_trials,
        all_existing_original_trace_and_trial_rows_parsed_without_error=(len(ERRORS)==errors_before),
        earlier_iteration_trial_details_not_exported=True,
        original_request_scope=select(request,("call","jacobian","audit","height_sha256",
            "height_negative_zero_columns","request_sha256")),
        initial_guess_scope=select(initial,("schema","kind","source","source_call",
            "old_state_or_J_reused","tangent_predictor_used","error")),
        original_request_failure=select(request_failure,("schema","call","error","type")),
        actual_checkpoint_scope=select(cp,("schema","cutHeight_sha256","rawNode",
            "actual_current_native_call","accepted_native_state","accepted_full_BVP_or_closed_surface")),
        response_scope=select(doc,("schema","nonlinear_finite_response_computed","old_graphs_or_gains_used",
            "old_finite_tail_output_relabelled","complete_infinite_C_nonlinear_DN_certified",
            "heightJetJacobianRows","heightJetJacobianMethod","exact_saved_matrix_nonresonance_certified",
            "meanHeightToCut")),
        original_native_row_canonical_sha256=sha(canonical(doc)) if doc else None)
    return row,detail,height_record

def numeric_word(value):
    if not isinstance(value,dict):
        return value
    return [value.get("value"),value.get("f64le"),value.get("classification")]

def linear_child(directory):
    directory=Path(directory)
    launch,launch_id=document(directory/"launch.json","linear-launch")
    exit_doc,exit_id=document(directory/"child-exit.json","linear-exit")
    returned,returned_id=document(directory/"returned-correction.json","linear-returned")
    failure,failure_id=document(directory/"bridge-failure.json","linear-failure")
    snapshot,sid=document(directory/"snapshot"/"snapshot.json","linear-snapshot")
    result,rid=document(directory/"linear-result"/"result.json","linear-result")
    for name in ("linear.stdout.log","linear.stderr.log"):
        log_view(directory/name,directory.name+"/"+name)
    snapshot=snapshot or {};result=result or {}
    for name,d in snapshot.get("arrays",{}).items():
        descriptor(directory/"snapshot",d)
    md=result.get("output_array_manifest")
    if md:
        descriptor(directory/"linear-result",md)
        manifest,_=document(contained(directory/"linear-result",md["file"]),"linear-array-manifest",True)
        require(manifest is not None,"Original output array manifest parse required")
        for item in manifest.get("arrays",[]):
            descriptor(directory/"linear-result",item)
    exact=result.get("exact_original_readback") or {}
    if exact.get("ledger"):
        descriptor(directory/"linear-result",exact["ledger"])
    factor=result.get("factorization") or {};numeric=result.get("readback") or {}
    maximum=exact.get("maximum") or {}
    exact_selected=select(maximum,("global_row","kind","node","component",
        "absolute_original_sigma_residual_decimal","decimal_is_a_display_not_a_new_gate"))
    row=[directory.name,snapshot.get("call"),snapshot.get("iteration"),result.get("kind",snapshot.get("kind")),
        result.get("eta"),result.get("completed"),result.get("failed"),numeric.get("complete_rows"),
        numeric.get("columns"),result.get("complete_factorization_completed",factor.get("complete")),
        result.get("completed_factor_nodes"),result.get("pending_factor_nodes"),
        numeric_word(factor.get("minimum_absolute_triangular_diagonal")),exact_selected,
        [numeric_word(v) for v in numeric.get("maximum_by_rhs",[])],
        error_view(result.get("error") or (failure or {}).get("error")),
        (rid or {}).get("sha256"),(sid or {}).get("sha256")]
    return row,dict(directory=directory.name,
        actual_exit=select(exit_doc,("exit_code","signal","error","elapsed_seconds","returncode")),
        returned=select(returned,("kind","call","iteration","snapshot_sequence","delta","cut_sensitivity",
            "source_matrix_identity","complete_all_node_sensitivity")),
        bridge_failure=select(failure,("kind","call","iteration","error","message")),
        result_scope=select(result,("error_type","reason_scope","exact_saved_matrix_nonresonance_certified")),
        factor_scope=select(factor,("all_cut_stage_far_rows_retained","all_penalty_and_constant_rows_retained",
            "general_far_rows","old_graph_used","explicit_inverse_used","interior_Dirichlet_charts_required",
            "no_threshold_rank_truncation","triangular_failure","negative_zero_recovered")),
        actual_snapshot_scope=select(snapshot,("kind","call","iteration","snapshot_sequence","modes","depth",
            "shape_dimension","actual_norm","actual_minA","actual_minD","source_of_snapshot")),
        original_launch=launch_id,original_exit=exit_id,original_return=returned_id,
        original_failure=failure_id,
        complete_factor_metadata_canonical_sha256=sha(canonical(result.get("complete_factors"))),
        original_output_arrays_hashed_without_numeric_recomputation=True)

def bvp_documents(driver):
    driver=Path(driver);selected=[]
    for path in sorted(driver.rglob("*")) if driver.is_dir() else []:
        if path.is_symlink():
            fail("BVP-document",ValueError("Owned symlink not followed"),path=str(path))
            continue
        if not path.is_file() or (driver/"full-DN"/"true-tail") in path.parents:
            continue
        relative=str(path.relative_to(driver))
        if path.name.endswith(".log"):
            log_view(path,relative)
            continue
        if path.name.endswith(".jsonl"):
            # The complete original stream is parsed; only declared useful events
            # and terminal records are selected, never treated as every row exported.
            first=[];last=deque(maxlen=2);events=Counter()
            def onrow(row,index,h):
                event=str(row.get("event","original-row")) if isinstance(row,dict) else "original-value"
                events[event]+=1
                value=dict(index=index,line_sha256=h,value=small(row))
                if len(first)<1:
                    first.append(value)
                last.append(value)
            record=line_stream(path,"BVP/"+relative,onrow)
            selected.append(dict(file=relative,identity=record,events=dict(events),
                first_record=first,last_records=list(last),
                middle_records_not_exported=True))
            continue
        if not path.name.endswith((".json",".json.gz")):
            continue
        value,record=document(path,"BVP/"+relative)
        if value is None:
            continue
        if path.name=="response-check.json":
            shown=select(value,FD_FIELDS)
        elif path.name=="actual-first-height-input.json":
            shown=select(value,("schema","formula","actual_current_height_sha256",
                "old_zero_J_or_supplied_literal_height_or_cached_parent_used"))
            shown["actual_full_M_height"]=value.get("actual_current_full_height")
            shown["actual_full_M_height_float64le"]=value.get("actual_current_full_height_float64le")
        elif path.name=="original-five-cut-comparisons.json":
            shown=select(value,("schema","rows","no_profile_target_value_replaced",
                "exact_real_same_C_seam_or_evaluator_error_certified"))
        elif path.name=="physical-test-final-cut-audit.json":
            shown=small(value)
        elif path.name in ("adapter-status.json","driver-status.json","actual.json.gz") or path.name.endswith("-pending.json.gz"):
            shown=select(value,BVP_FIELDS)
        elif path.name.endswith(("-anchor-tail.json.gz","-actual-tail.json.gz","final-audit.json.gz")) or path.name=="initial-actual-H-tail.json.gz":
            shown=select(value,("schema","call","normalizedResidual","converged","audit","predicted",
                "heightJetJacobianRows","heightJetJacobianMethod","nonlinear_finite_response_computed",
                "current_native_completed","last_withJ_norm","meanHeightToCut","error"))
        else:
            # Parse all other original JSON, preserve identity and the small
            # original explicit status only; source/config/large metadata is raw.
            shown=select(value,("schema","phase","success","completed","failed","error",
                "message","kind","status","initial_collocation_max","preflight_added_nodes"))
        selected.append(dict(file=relative,identity=record,original_selected_values=shown,
            full_recomputable_member_tree_not_exported=True))
    return selected

def native_readback(client):
    client=Path(client);errors_before=len(ERRORS)
    if not client.is_dir():
        return dict(actual_live_client_directory_exists=False,no_request_inferred=True)
    result=dict(actual_live_client_directory_exists=True)
    for name in ("client-launch.json","client-ready.json","client-session-result.json"):
        value,record=document(client/name,"client/"+name)
        if value is not None:
            result[name]=dict(identity=record,original_selected=select(value,("schema","ready","modes","depth",
                "cut","linearSlope_not_computed_or_assumed","no_old_node_graphs_or_gains_used",
                "explicit_zero_cut_root_evaluated","zero_height_full_native_response_not_precomputed",
                "exact_C_and_infinite_nonlinear_DN_certified","actual_requests","cached_same_height_hits",
                "closed","error","failed","worker_exit","actual_call_count")))
    log_view(client/"native-stderr.log","native-worker-stderr")
    native=client/"native";calls=[];details=[];heights=[]
    for path in sorted(native.glob("call-*")) if native.is_dir() else []:
        if path.is_dir():
            try:
                row,detail,height=native_call(path)
                calls.append(row);details.append(detail)
                if height is not None:
                    heights.append(height)
            except Exception as error:
                fail("native-call/"+path.name,error)
    linear=[];linear_details=[]
    parent=native/"linear-children"
    for path in sorted(parent.glob("call-*")) if parent.is_dir() else []:
        if path.is_dir():
            try:
                row,detail=linear_child(path)
                linear.append(row);linear_details.append(detail)
            except Exception as error:
                fail("linear-child/"+path.name,error)
    stream_ids={}
    for path in (client/"client-events.jsonl",native/"native-requests.jsonl"):
        if path.is_file():
            stream_ids[path.name]=line_stream(path,"native/"+path.name,lambda row,i,h:None)
    for path in (native/"actual-original-engine-geometry-words.jsonl",client/"native-protocol-stdout.jsonl"):
        if path.is_file():
            stream_ids[path.name]=line_stream(path,"native/"+path.name)
    result.update(native_columns=NATIVE_COLUMNS,all_actual_native_calls=calls,
        trial_columns=TRIAL_COLUMNS,last_iteration_trials_and_scopes_for_each_actual_call=details,
        all_existing_original_native_trace_and_trial_rows_parsed_without_error=(len(ERRORS)==errors_before),
        earlier_iteration_trial_rows_not_returned=True,
        first_and_last_actual_native_request_height=(
            [] if not heights else [heights[0]] if len(heights)==1 else [heights[0],heights[-1]]),
        other_actual_request_heights_bound_by_original_request_identity_not_exported=True,
        linear_columns=LINEAR_COLUMNS,all_original_linear_child_rows=linear,
        original_linear_child_scopes=linear_details,other_original_streams=stream_ids,
        actual_returned_J_and_states_only_read_if_present_not_recomputed=True,
        successful_J_or_complete_native_return_not_inferred_from_reader_scope=True,
        no_selected_scalar_changes_an_original_scientific_gate=True)
    return result

def inventory(roots):
    count=0;total=0;index_hash=hashlib.sha256()
    for role,root in roots:
        root=Path(root)
        if not root.is_dir():
            continue
        for path in sorted(root.rglob("*")):
            if path.is_symlink():
                fail("inventory",ValueError("Owned symlink not followed"),role=role,path=str(path))
                continue
            if not path.is_file():
                continue
            record=identity(path)
            index_hash.update(canonical(dict(role=role,path=str(path.relative_to(root)),**record)))
            count+=1;total+=record["bytes"]
    return dict(files=count,bytes=total,complete_path_byte_identity_index_sha256=index_hash.hexdigest(),
        complete_regular_owned_files_hashed=True,original_numeric_arrays_not_independently_recomputed=True,
        index_members_not_exported=True)

def write(path,value):
    raw=canonical(value)
    with Path(path).open("xb") as stream:
        stream.write(raw);stream.flush();os.fsync(stream.fileno())
    return dict(file=Path(path).name,bytes=len(raw),sha256=sha(raw))

