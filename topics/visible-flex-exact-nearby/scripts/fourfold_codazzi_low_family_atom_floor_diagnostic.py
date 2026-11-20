#!/usr/bin/env python3
"""Independent mean-atom lower floor for the fixed R139 comparison recipe.

This public Actions entry computes three independent LOWER-floor records.
None of the fifty parent scalar targets or the old low-family three is evaluated.  The
unchanged seven-module W2C admission and fifty-target parent parameters are
input context, not a claim that the five parent graphs have been computed.
No original producer or old completed bound is evaluated.
"""
import argparse
import copy
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import platform
import re
import sys
import time
import traceback

REPOSITORY = "Rogerhu12/math-research-public"
DIAGNOSTIC_ROLE = "low_family_atom_floor_diagnostic"
SOURCE_PATH = "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_low_family_atom_floor_diagnostic.py"
PROOF_ROLE = "low_family_atom_floor_proof"
PROOF_PATH = "topics/visible-flex-exact-nearby/results/R139-supplement-mean-atom-lower-budget-for-fixed-comparison.md"
KIND = "W2C_low_family_mean_atom_floor_diagnostic_v1"
PREFLIGHT_KIND = "W2C_low_family_mean_atom_floor_readonly_preflight_v1"
TARGET = "complete_low_family_mean_atom_necessary_floor"
RECORD_NAMES = [
    "complete_low_family_atom_row_floor",
    "complete_low_family_atom_column_floor",
    "complete_low_family_atom_squared_norm_floor",
]
ADDITIONAL_GATE_LABELS = [
    "fixed_directed_runtime_and_one_low_family_entry",
    "all_twenty_nine_same_operator_records_typed_and_original_optical_eta_retained",
    "fixed_old_comparison_constants_meet_R139_hypotheses",
    "entire_fixed_WVC_reference_definition_and_diagonal_chains_materialized",
    "complete_true_collar_body_and_all_kernel_domains_admitted",
    "complete_low_family_atom_floor_three_records_saved",
    "necessary_budget_diagnostic_resolved_without_parent_gate_or_inverse",
    "all_current_inputs_and_manifest_reverified_after_new_work",
    "complete_diagnostic_shape_and_old_zero_recomputation",
]
DIAGNOSTIC_SCOPE = {
    "new_operator_targets": 1,
    "new_scalar_targets": 3,
    "parent_scalar_targets_computed": 0,
    "original_low_family_three_records_computed": 0,
    "all_new_records_are_lower_floors_for_the_fixed_comparison_recipe": True,
    "no_whole_box_signed_profiles_or_Green_kernel_evaluated": True,
    "product_threshold_is_exact_rational": "1/16384",
    "parent_scalar_targets": 50,
    "parent_parameters_and_seven_module_input_contract_retained": True,
    "complete_parent_graphs_computed": 0,
    "parent_graph1_primal_computed": False,
    "parent_graph2_dual_computed": False,
    "parent_graph3_complete_family_computed": False,
    "parent_graph4_joint_signed_centre_computed": False,
    "parent_graph5_finite_comparison_computed": False,
    "full_low193_with_independent_physical_mean": True,
    "all193_observations_in_one_complete_Hilbert_block": True,
    "same_full_family_AL_fee_and_actual_S_inverse": True,
    "all_seven_ports_and_both_rhs_retained_as_parent_context": True,
    "complete_signed_DAG_or_centre_residual_comparisons_constructed": False,
    "L_is_the_fixed_upper_bound_recipe_not_an_actual_norm_lower_bound": True,
    "threshold_is_exact_rational": "1/128",
    "only_fixed_comparison_recipe_can_be_excluded": True,
    "failure_to_reject_is_not_a_passed_finite_gate": True,
    "actual_operator_singularity_not_concluded": True,
    "finite_inverse_not_concluded": True,
    "old_completed_targets_recomputed": 0,
    "new_arrays_or_artifacts_published": 0,
}
SCI_FIELDS = [
    "actual_checkout_commit", "actual_mathematical_wall_seconds", "actual_progress",
    "actual_returncode", "automatic_retry_authorized", "collar_native_identities",
    "collar_original_contexts", "complete", "complete_current_file_receipts",
    "complete_restoration_receipts", "complete_support_contract", "completed_targets",
    "conditional_finite_inverse", "copied_complete_candidate_metadata",
    "copied_complete_repair_definition", "copied_original_scope",
    "copied_same_operator_records", "current_target", "diagnostic_scope",
    "diagnostic_source", "failure", "finite_gate", "gates", "kernel_progress",
    "kind", "manifest_sha256", "necessary_budget", "new_records",
    "original_admission", "original_closure_admission", "original_optical_records",
    "parameters", "parent_candidate_complete", "preparation_prefix",
    "prior_completed_candidate", "problem_id", "reference_identity",
    "retained_completed_five_maxima", "retained_original_false_candidates",
    "retained_scope", "run_attempt", "run_id", "runtime", "saved_record_count",
    "scientific_modules", "stage", "workflow_event_commit",
]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load_pinned_helper(root, spec):
    """Load only the already reviewed new owner's side-effect-free helpers."""
    path = (root / spec["path"]).resolve()
    require(path.is_relative_to(root) and path.is_file(), "helper path containment")
    raw = path.read_bytes()
    require(len(raw) == spec["bytes"]
            and hashlib.sha256(raw).hexdigest() == spec["sha256"]
            and hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
                == spec["git_blob_sha"], "complete pinned new-owner helper source")
    loader = importlib.util.spec_from_file_location("_w2c_budget_owner_helpers", path)
    require(loader is not None and loader.loader is not None, "helper loader")
    module = importlib.util.module_from_spec(loader)
    loader.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("repo", "manifest", "manifest-sha", "out", "native", "native-receipts",
                 "candidate-index", "centre-repair", "root-germ", "root-budget"):
        parser.add_argument("--" + name, required=True)
    parser.add_argument("--bits", type=int, required=True)
    parser.add_argument("--preflight-only", action="store_true")
    args = parser.parse_args()
    require(args.bits == 320, "fixed 320-bit directed arithmetic")
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
            "own public repository Actions only")
    require("flint" not in sys.modules, "complete readonly admission precedes flint")
    root = Path(args.repo).resolve()
    manifest_raw = Path(args.manifest).read_bytes()
    require(0 < len(manifest_raw) < 100000
            and hashlib.sha256(manifest_raw).hexdigest() == args.manifest_sha,
            "whole frozen diagnostic manifest")
    initial = json.loads(manifest_raw)
    specs = {item["role"]: item for item in initial["files"]}
    require(specs[DIAGNOSTIC_ROLE]["path"] == SOURCE_PATH
            and specs[PROOF_ROLE]["path"] == PROOF_PATH
            and Path(__file__).resolve() == (root / SOURCE_PATH).resolve(),
            "actual diagnostic source and R139 proof paths")
    helper = load_pinned_helper(root, specs["science"])
    core = helper.import_new_source(root, specs["readonly_core"], "_w2c_budget_readonly_core")
    readonly = helper.import_new_source(root, specs["readonly_admission"], "_w2c_budget_readonly")
    canonical, data, digest = core.canonical, core.data, core.digest
    admitted = readonly.admit(root, args.manifest, args.manifest_sha, args.native,
        args.native_receipts, args.candidate_index, args.centre_repair,
        args.root_germ, args.root_budget, core)
    manifest = admitted["manifest"]
    op = manifest["operation"]
    gates = helper.ADMISSION_GATE_LABELS + ADDITIONAL_GATE_LABELS
    require(canonical(manifest["parameters"]) == canonical(helper.PARAMETERS)
            and manifest["retained_scope"] == helper.RETAINED_SCOPE
            and op["retained_scope"] == helper.RETAINED_SCOPE,
            "unchanged parent fifty-target parameters and complete physical context")
    require(op["scientific_entry_role"] == DIAGNOSTIC_ROLE
            and op["scientific_kind"] == KIND
            and op["ordered_targets"] == [TARGET]
            and op["complete_target_counts"] == [1]
            and op["complete_gate_names"] == gates
            and op["scientific_field_names"] == sorted(SCI_FIELDS)
            and op.get("readonly_diagnostic_only", False) is False
            and manifest["diagnostic_contract"] == DIAGNOSTIC_SCOPE,
            "one independent three-scalar diagnostic contract")
    require([item["name"] for item in admitted["admission"]["checks"]]
                == helper.ADMISSION_GATE_LABELS
            and all(item["passed"] is True for item in admitted["admission"]["checks"]),
            "whole original and collar readonly admission")
    require(core.read_spec(root, specs[DIAGNOSTIC_ROLE]) == Path(__file__).read_text(),
            "actual diagnostic is the complete admitted source")
    run = os.environ.get("GITHUB_RUN_ID", "")
    attempt = os.environ.get("GITHUB_RUN_ATTEMPT", "")
    event = os.environ.get("GITHUB_SHA", "")
    checkout = os.environ.get("ACTUAL_CHECKOUT_COMMIT", "")
    require(re.fullmatch(r"\d{1,20}", run) and re.fullmatch(r"\d{1,10}", attempt)
            and re.fullmatch(r"[0-9a-f]{40}", event)
            and re.fullmatch(r"[0-9a-f]{40}", checkout), "actual public run identity")
    if args.preflight_only:
        require("flint" not in sys.modules, "preflight remains pure readonly")
        result = {"kind": PREFLIGHT_KIND, "complete": True, "preflight_only": True,
            "problem_id": readonly.PROBLEM_ID, "manifest_sha256": args.manifest_sha,
            "admission": admitted["admission"], "diagnostic_scope": DIAGNOSTIC_SCOPE,
            "diagnostic_source": specs[DIAGNOSTIC_ROLE],
            "same_complete_WVC_reference": admitted["paired_inputs"]["reference_chain"],
            "same_complete_selected_diagonal_chain":
                admitted["completed_tracefree_inputs"]["selected_diagonal_chain"],
            "same_operator_record_count": 29, "old_scientific_calls": 0,
            "new_scalar_targets_evaluated": 0, "flint_imported": False}
        print(canonical(result).decode("utf-8"), end="", flush=True)
        return 0

    output = Path(args.out)
    require(not output.exists(), "one never-overwritten diagnostic output")
    output.parent.mkdir(parents=True, exist_ok=True)
    paired = admitted["paired_inputs"]
    completed = admitted["completed_tracefree_inputs"]
    document = {
        "kind": KIND, "problem_id": readonly.PROBLEM_ID, "complete": False,
        "parent_candidate_complete": False, "stage": "complete_readonly_inputs_saved",
        "failure": None, "actual_returncode": None, "run_id": run, "run_attempt": attempt,
        "workflow_event_commit": event, "actual_checkout_commit": checkout,
        "manifest_sha256": args.manifest_sha,
        "scientific_modules": copy.deepcopy(admitted["scientific_modules"]),
        "diagnostic_source": copy.deepcopy(specs[DIAGNOSTIC_ROLE]),
        "diagnostic_scope": copy.deepcopy(DIAGNOSTIC_SCOPE),
        "complete_current_file_receipts": copy.deepcopy(admitted["current_receipts"]),
        "original_admission": copy.deepcopy(admitted["admission"]),
        "original_closure_admission": copy.deepcopy(admitted["original_closure_admission"]),
        "complete_restoration_receipts": helper.restoration_reference(
            admitted["complete_restoration_receipts"], manifest, run, attempt, canonical, digest),
        "parameters": copy.deepcopy(helper.PARAMETERS),
        "retained_scope": copy.deepcopy(helper.RETAINED_SCOPE),
        "copied_same_operator_records": copy.deepcopy(admitted["same_operator_records"]),
        "copied_original_scope": copy.deepcopy(paired["scope"]),
        "copied_complete_candidate_metadata": copy.deepcopy(admitted["candidate_metadata"]),
        "copied_complete_repair_definition": copy.deepcopy(admitted["repair_definition"]),
        "retained_completed_five_maxima": copy.deepcopy(paired["completed_five_maxima"]),
        "retained_original_false_candidates": copy.deepcopy(paired["old_false_candidates"]),
        "prior_completed_candidate": helper.compact_old_archive(
            completed["archive"], admitted["same_operator_records"], canonical, digest),
        "original_optical_records": copy.deepcopy(admitted["original_optical_records"]),
        "collar_native_identities": copy.deepcopy(admitted["collar_native_identities"]),
        "collar_original_contexts": helper.lossless_context_table(
            admitted["collar_original_contexts"], canonical, digest),
        "reference_identity": None, "complete_support_contract": None,
        "preparation_prefix": {"stage": "not_started", "detail": None,
            "private_packets_are_not_independent_array_targets": True},
        "kernel_progress": {"count": 0, "chain_sha256": None, "latest": None},
        "current_target": None, "completed_targets": [], "new_records": {},
        "saved_record_count": 0, "necessary_budget": None, "finite_gate": None,
        "conditional_finite_inverse": None, "gates": [],
        "actual_progress": {
            "current_files_admitted": len(admitted["current_receipts"]),
            "historical_files_admitted": len(admitted["complete_restored_input_map"]),
            "old_WVC_records_verified": 56, "old_WVC_modal_prefix_records_verified": 5,
            "old_WPS_records_verified": 60, "old_WPS_modal_prefix_records_verified": 6,
            "same_operator_records_copied": 29, "original_optical_records_copied": 2,
            "reference_definitions_materialized": 0, "completed_new_centre_parents": 0,
            "original_closed_rows_covered": 0, "original_body_intersections": 0,
            "comparison_cells": 0, "new_diagnostic_targets_completed": 0,
            "new_scalar_records_saved": 0, "parent_declared_scalar_targets": 50,
            "complete_parent_graphs_computed": 0, "new_strict_finite_comparisons": 0,
            "parent_scalar_targets_computed": 0, "original_low_family_three_records_computed": 0,
            "conditional_finite_inverses": 0, "old_targets_recomputed": 0,
            "old_producer_imports_or_calls": 0, "old_reference_bound_targets_reevaluated": 0,
            "physical_state_columns_computed": 0, "dense_full_finite_matrices_allocated": 0,
            "new_arrays_published": 0, "new_artifacts": 0, "new_Releases": 0},
        "runtime": {}, "actual_mathematical_wall_seconds": 0.0,
        "automatic_retry_authorized": False,
    }
    require(sorted(document) == sorted(SCI_FIELDS), "complete diagnostic output fields")
    math_start = None
    api = None
    prepared = False

    def publish(check_size=True):
        if math_start is not None:
            elapsed = time.perf_counter() - math_start
            require(math.isfinite(elapsed) and elapsed >= 0, "finite elapsed wall time")
            document["actual_mathematical_wall_seconds"] = elapsed
        raw = canonical(document)
        temporary = output.with_name(output.name + ".tmp")
        with temporary.open("wb") as stream:
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, output)
        sys.stdout.write(raw.decode("utf-8"))
        sys.stdout.flush()
        restored = data(output.read_bytes())
        require(canonical(restored) == raw, "whole atomic diagnostic output readback")
        if check_size:
            require(len(raw) <= op["maximum_scientific_bytes"], "complete output byte budget")
        return restored

    def gate(name, passed=True):
        n = len(document["gates"])
        require(n < len(gates) and name == gates[n], "diagnostic gate order")
        document["gates"].append({"name": name, "passed": bool(passed)})
        publish()
        require(passed, name)

    def progress(stage, detail):
        require(isinstance(stage, str) and 0 < len(stage) <= 160
                and isinstance(detail, dict), "compact private preparation metadata")
        raw = canonical({"stage": stage, "detail": detail})
        require(len(raw) <= 2000, "no coefficient arrays in preparation output")
        previous = document["kernel_progress"]
        previous["count"] += 1
        previous["chain_sha256"] = digest(canonical({
            "previous": previous["chain_sha256"], "current": data(raw)}))
        previous["latest"] = data(raw)
        if not prepared:
            document["preparation_prefix"] = {"stage": stage, "detail": copy.deepcopy(detail),
                "private_packets_are_not_independent_array_targets": True}
        actual = document["actual_progress"]
        if stage == "same_exact_reference_definition":
            actual["reference_definitions_materialized"] = detail["parents_verified"]
        elif stage == "complete_new_centre_parent":
            actual["completed_new_centre_parents"] = detail["parents_complete"]
            actual["original_closed_rows_covered"] = detail["closed_rows_covered"]
            actual["original_body_intersections"] = detail["closed_intersections"]
        elif stage == "complete_signed_kernel_inputs":
            actual["comparison_cells"] = detail["comparison_cells"]
        document["stage"] = "working:" + stage
        publish()

    def emit(name, value):
        count = document["saved_record_count"]
        require(document["current_target"] == TARGET and count < len(RECORD_NAMES)
                and name == RECORD_NAMES[count] and name not in document["new_records"],
                "one saved complete scalar in its original order")
        value = api.lower(value)
        require(value >= 0, "proved nonnegative directed lower certificate")
        record = {"ball": value.str(helper.PARAMETERS["decimal_record_digits"])}
        helper.record_text(record)
        document["new_records"][name] = record
        document["saved_record_count"] += 1
        document["actual_progress"]["new_scalar_records_saved"] += 1
        document["stage"] = "record_saved:" + name
        restored = publish()
        return api.lower(api.arb(helper.record_text(restored["new_records"][name])))

    publish()
    try:
        for item in admitted["admission"]["checks"]:
            gate(item["name"], item["passed"])
        import flint
        require(platform.python_version() == "3.12.14" and flint.__version__ == "0.9.0",
                "fixed public directed runtime")
        flint.ctx.prec = 320
        api = helper.NumericalAPI(flint)
        document["runtime"] = {"Python": "3.12.14", "python_flint": "0.9.0", "bits": 320,
            "old_module_imports": 0, "numpy_imported": False,
            "new_owner_helper_module_imported_without_calling_main": True}
        gate("fixed_directed_runtime_and_one_low_family_entry")
        old = {}
        for name, record in document["copied_same_operator_records"].items():
            if name in ("G_c", "L_c_raw"):
                exact = Fraction(record)
                value = api.rational(exact.numerator, exact.denominator)
            else:
                value = api.old_interval(record)
            old[name] = api.upper(value)
        require(len(old) == 29 and document["copied_same_operator_records"]
                    == completed["copied_records"]
                and len(document["original_optical_records"]) == 2,
                "complete old29 and both optical records retained without recomputation")
        gate("all_twenty_nine_same_operator_records_typed_and_original_optical_eta_retained")
        floor_hypotheses = [
            ("complete_reference_rho_defect_upper", 7, 100),
            ("complete_outer_paired_error_upper", 2, 3),
            ("complete_outer_endpoint_correction_upper", 1, 8),
            ("complete_actual_T_upper", 15, 4),
        ]
        require(all(bool(old[name].lower() > api.rational(n, d).upper())
                    for name, n, d in floor_hypotheses),
                "frozen upper-budget constants satisfy the strict R139 rational hypotheses")
        gate("fixed_old_comparison_constants_meet_R139_hypotheses")
        collar = helper.import_new_source(root, specs["collar_math"], "_w2c_budget_collar")
        km = helper.import_new_source(root, specs["kernel_math"], "_w2c_budget_kernel")
        assembly = helper.import_new_source(root, specs["assembly_math"], "_w2c_budget_assembly")
        reference = helper.import_new_source(root, specs["reference_math"], "_w2c_budget_reference")
        math_start = time.perf_counter()
        context = assembly.prepare_complete_kernel_context(api, km, reference, collar, admitted,
            completed["complete_original_candidate"], old, core.signed_display_centre, progress)
        document["reference_identity"] = copy.deepcopy(context.reference_identity)
        require(context.reference_identity["original_reference_chain"]
                    == completed["complete_original_candidate"]["reference_chain"]
                and context.reference_identity["selected_diagonal_chain"]
                    == completed["selected_diagonal_chain"], "identical whole WVC reference")
        gate("entire_fixed_WVC_reference_definition_and_diagonal_chains_materialized")
        require(context.parent_definition_count == 153
                and context.original_body_row_count == 4650
                and context.original_intersection_count == 4801
                and len(context.domain.cells) <= 155
                and all(value is True for value in context.qualifications.values())
                and document["actual_progress"]["reference_definitions_materialized"] == 153
                and document["actual_progress"]["completed_new_centre_parents"] == 153,
                "entire true-root collar, original cover and all comparison domains")
        document["complete_support_contract"] = {
            "all_actual_qualifications": copy.deepcopy(context.qualifications),
            "ordinary_dr_pairing": True, "head_dimension": 193,
            "all193_finite_Gf_observation_atoms": 193, "independent_mean_retained": True,
            "parent_definitions": 153, "closed_original_rows": 4650,
            "closed_intersections": 4801, "comparison_cells": len(context.domain.cells),
            "fixed_original_reference_fine_cells": 24480,
            "same_physical_AL_family_error_and_S_inverse": True,
            "parent_high_windows_and_ports_are_context_not_new_computed_targets": True,
        }
        prepared = True
        document["preparation_prefix"] = {"stage": "complete", "detail": {
            "parent_definitions": 153, "complete_centre_parents": 153,
            "closed_original_rows": 4650, "closed_intersections": 4801,
            "comparison_cells": len(context.domain.cells)},
            "private_packets_are_not_independent_array_targets": True}
        gate("complete_true_collar_body_and_all_kernel_domains_admitted")

        # The complete original atom callback is max(1, all modal bounds).
        # Its mean entry alone gives R>=sum(h*a), C>=max(a), L^2>=R*C.
        # No profile.at, modal Green kernel, or original parent target is called.
        document["current_target"] = TARGET
        document["stage"] = "started:" + TARGET
        publish()
        coefficients = [api.upper(a*s) for a, s in zip(
            context.family_fees["AL"], context.S_inverse_norms)]
        lengths = [api.upper(context.domain.full_length(k))
                   for k in range(len(context.domain.cells))]
        require(len(coefficients) == len(lengths) == 155
                and all(x >= 0 for x in coefficients) and all(h > 0 for h in lengths),
                "complete positive same-recipe coefficient and true-length numbers")
        row_floor = emit(RECORD_NAMES[0], sum(
            (h*a for h, a in zip(lengths, coefficients)), api.zero))
        column_floor = emit(RECORD_NAMES[1], max(coefficients))
        require(row_floor >= 0 and column_floor >= 0,
                "saved lower certificate readback remains nonnegative")
        emit(RECORD_NAMES[2], row_floor*column_floor)
        require(list(document["new_records"]) == RECORD_NAMES
                and document["saved_record_count"] == 3,
                "three independent complete mean-atom lower records retained")
        gate("complete_low_family_atom_floor_three_records_saved")
        saved_product = api.arb(helper.record_text(document["new_records"][RECORD_NAMES[-1]]))
        rejected = bool(saved_product.lower() >= api.rational(1, 16384).upper())
        document["necessary_budget"] = {
            "kind": "fixed_W2C_mean_atom_lower_recipe_budget_v1",
            "proof": copy.deepcopy(specs[PROOF_ROLE]),
            "fixed_parent_formula": "F(h)=e+(1+e)*sqrt((6h/5)^2+b^2)+sqrt((6oH/5)^2+ob^2)+3*T*((1+e)*h+oH)",
            "nonnegative_remainder_relation": "h=K+epsilon >= L >= 0",
            "verified_old_upper_budget_hypotheses": [
                {"record_name": name, "strict_lower_fraction": str(n) + "/" + str(d),
                 "passed": True} for name, n, d in floor_hypotheses],
            "derived_necessary_floor": "F(h)>=109/120+(963/80)*h",
            "atom_recipe_identity": "b_k>=1; R>=S=sum(h_k*a_k); C>=M=max(a_k); L^2>=S*M",
            "saved_record_semantics": "all three are saved-and-reread directed LOWER certificates",
            "squared_L_lower_record": RECORD_NAMES[-1],
            "product_threshold": "1/16384", "original_L_threshold": "1/128",
            "comparison_uses_saved_record_lower_endpoint": True,
            "saved_product_lower_at_least_threshold": rejected,
            "fixed_recipe_rejection_proved": rejected,
            "floor_at_L_threshold": "30793/30720", "floor_excess_over_one": "73/30720",
            "outcome": "fixed_comparison_recipe_excluded_by_mean_atom" if rejected else "necessary_atom_rejection_not_proved",
            "false_rejection_flag_is_not_a_passed_parent_gate": True,
            "actual_operator_norm_lower_bound_proved": False,
            "actual_operator_singularity_proved": False,
            "parent_finite_gate_computed": False, "finite_inverse_proved": False,
            "parent_scalar_records_computed": 0,
            "original_low_family_three_records_computed": 0,
        }
        gate("necessary_budget_diagnostic_resolved_without_parent_gate_or_inverse")
        for spec in admitted["current_receipts"]:
            core.read_spec(root, spec)
        require(digest(Path(args.manifest).read_bytes()) == args.manifest_sha,
                "unchanged manifest after diagnostic")
        gate("all_current_inputs_and_manifest_reverified_after_new_work")
        document["completed_targets"] = [TARGET]
        document["current_target"] = None
        document["actual_progress"]["new_diagnostic_targets_completed"] = 1
        require(sorted(document) == sorted(SCI_FIELDS)
                and document["saved_record_count"] == 3
                and document["actual_progress"]["new_scalar_records_saved"] == 3
                and document["parent_candidate_complete"] is False
                and document["finite_gate"] is None and document["conditional_finite_inverse"] is None
                and document["copied_same_operator_records"] == admitted["same_operator_records"]
                and document["original_optical_records"] == admitted["original_optical_records"]
                and all(document["actual_progress"][name] == 0 for name in (
                    "complete_parent_graphs_computed", "new_strict_finite_comparisons",
                    "conditional_finite_inverses", "old_targets_recomputed",
                    "old_producer_imports_or_calls", "old_reference_bound_targets_reevaluated",
                    "physical_state_columns_computed", "dense_full_finite_matrices_allocated",
                    "new_arrays_published", "new_artifacts", "new_Releases")),
                "three independent lower certificates; no parent scalar, graph or inverse claim")
        gate("complete_diagnostic_shape_and_old_zero_recomputation")
        document["complete"] = True
        document["stage"] = "complete_three_independent_atom_lower_certificates"
        document["actual_returncode"] = 0
        publish()
        return 0
    except BaseException as error:
        trace = traceback.format_exc()
        sys.stderr.write(trace)
        sys.stderr.flush()
        document["complete"] = False
        document["stage"] = "failed_diagnostic_prefix_preserved"
        document["actual_returncode"] = 1
        document["failure"] = {
            "type": helper.bounded_diagnostic(type(error).__name__, 128),
            "message": helper.bounded_diagnostic(str(error), 2048),
            "traceback": helper.bounded_diagnostic(trace, 6000),
            "complete_traceback_printed_to_stderr": True,
            "entire_saved_scalar_prefix_retained": True,
            "automatic_retry_authorized": False,
        }
        publish(check_size=False)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
