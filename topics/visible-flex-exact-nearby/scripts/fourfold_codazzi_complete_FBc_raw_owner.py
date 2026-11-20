"""One new complete receiver-free WJK F Bc raw-L2 comparison, public only.

This target does not call Gf, a low inverse, endpoint/atom norms, the old
small-K50 graphs, or any completed source-bound producer.  It preserves
the original readonly W2C admission and materializes the same full signed
centre/reference definitions.  The complete positive comparison is for
Pi0(P Bc-Q* Rc), with every collar and transition term already retained.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import importlib.util
import json
import math
import os
import platform
import re
import sys
import time
import traceback
from fractions import Fraction
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby/"
SOURCE_PATH = TOPIC+"scripts/fourfold_codazzi_complete_FBc_raw_owner.py"
ENTRY_ROLE = "complete_FBc_raw_owner"
MATH_ROLE = "complete_FBc_raw_math"
KIND = "complete_receiver_free_WJK_FBc_raw_L2_comparison_v1"
PREFLIGHT_KIND = "complete_receiver_free_WJK_FBc_readonly_preflight_v1"
TARGETS = ["complete_projected_WJK_FBc_raw_L2_operator"]
RECORD_NAMES = ["complete_projected_WJK_FBc_raw_row_ratio_upper",
                "complete_projected_WJK_FBc_raw_column_ratio_upper",
                "complete_projected_WJK_FBc_raw_norm_upper"]
L_ACTUAL_ROLE = "completed_original_low_family_actual"
L_EXECUTION_ROLE = "completed_original_low_family_execution"
CENTRE_ACTUAL_ROLE = "completed_centre_mean_floor_actual"
CENTRE_EXECUTION_ROLE = "completed_centre_mean_floor_execution"
RUNTIME = {"Python": "3.12.14", "python_flint": "0.9.0", "bits": 320,
           "BLAS_threads": 1}
RETURN_PARAMETERS = {"original_parent_count": 153, "comparison_panel_count": 155,
    "original_body_rows": 4650, "original_closed_intersections": 4801,
    "input_dimension": 193, "exact_active_input_dimension": 128,
    "complete_returned_high_dimension": 128, "returned_modes": "97..160",
    "trial_intermediate_modes": "97..224", "complete_primal_residual_modes": "97..288",
    "actual_high_unknown_truncated": False,
    "same_actual_eta_and_original_S_inverse": True,
    "complete_F_definition": "Pi0(P+Qstar-Qstar Lc P) Bc",
    "comparison_definition": "Pi0 P Bc plus whole Qstar Pi1 Rc positive triangle",
    "full_Rc_retained_before_exact_return_projection": True,
    "true_Jstar_upper_endpoint": "25/8",
    "original_chi_and_psi_width": "1/16",
    "complete_record_count": 3, "complete_target_count": 1,
    "Gf_or_low_inverse_evaluated": False, "atoms_or_endpoint_targets_evaluated": False,
    "signed_F_cancellation_not_present_in_this_positive_bound": True,
    "original_small_K50_recipe_reentered": False,
    "completed_L_or_centre_or_endpoint_targets_recomputed": False,
    "maximum_scientific_wall_seconds": 2400, "automatic_retries": 0,
    "source_operator_is_finite_WJK_trial_not_actual_GH": True}
GATE_SUFFIX = ["whole_completed_L_and_centre_exclusion_retained_readonly",
    "fixed_public_directed_runtime_verified",
    "same29_original_records_typed_without_recomputing_bounds",
    "whole_same_WVC_context_and_reference_identified",
    "complete_receiver_free_FBc_three_records_saved",
    "all_current_input_files_reverified_after_new_work",
    "complete_fixed_trial_scope_and_all_unpaid_obligations_retained"]
SCI_FIELDS = ["actual_checkout_commit", "actual_mathematical_wall_seconds", "actual_progress",
    "actual_returncode", "automatic_retry_authorized", "complete", "complete_current_file_receipts",
    "complete_restoration_receipts", "complete_support_contract", "completed_original_L", "completed_original_centre_mean_floor",
    "completed_targets", "copied_same_operator_records", "current_target", "failure", "gates",
    "kind", "manifest_sha256", "new_records", "original_admission", "parameters", "preparation_prefix",
    "prior_complete_WVC_provider", "problem_id", "proved", "reference_identity", "retained_scope",
    "return_parameters", "run_attempt", "run_id", "runtime", "saved_record_count", "scientific_modules",
    "stage", "trial_comparison", "workflow_event_commit"]


def require(ok, message):
    if not ok:
        raise ValueError(message)


def import_pinned(root, spec, name):
    path = root/spec["path"]
    raw = path.read_bytes()
    require(0 < len(raw) < 100000 and len(raw) == spec["bytes"]
            and hashlib.sha256(raw).hexdigest() == spec["sha256"], "whole pinned definition: "+spec["role"])
    definition = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(definition)
    definition.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("repo", "manifest", "manifest-sha", "out", "native", "native-receipts",
                 "candidate-index", "centre-repair", "root-germ", "root-budget"):
        parser.add_argument("--"+name, required=True)
    parser.add_argument("--bits", type=int, required=True)
    parser.add_argument("--preflight-only", action="store_true")
    args = parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"
            and args.bits == 320, "one public own-Actions target in its fixed runtime")
    require(not any(name in sys.modules for name in ("flint", "numpy", "scipy")),
            "full readonly admission before numerical imports")
    root = Path(args.repo).resolve()
    manifest_raw = Path(args.manifest).read_bytes()
    require(0 < len(manifest_raw) < 100000
            and hashlib.sha256(manifest_raw).hexdigest() == args.manifest_sha,
            "whole frozen manifest identity")
    initial = json.loads(manifest_raw)
    specs = {s["role"]: s for s in initial["files"]}
    require(specs[ENTRY_ROLE]["path"] == SOURCE_PATH
            and Path(__file__).resolve() == (root/SOURCE_PATH).resolve(), "actual frozen new owner path")
    raw_self = Path(__file__).read_bytes()
    require(len(raw_self) == specs[ENTRY_ROLE]["bytes"]
            and hashlib.sha256(raw_self).hexdigest() == specs[ENTRY_ROLE]["sha256"], "complete new owner bytes")
    core = import_pinned(root, specs["readonly_core"], "_FBc_readonly_core")
    readonly = import_pinned(root, specs["readonly_admission"], "_FBc_readonly")
    admitted = readonly.admit(root, args.manifest, args.manifest_sha, args.native,
        args.native_receipts, args.candidate_index, args.centre_repair,
        args.root_germ, args.root_budget, core)
    manifest, canonical, digest = admitted["manifest"], core.canonical, core.digest
    operation = manifest["operation"]
    base_names = [g["name"] for g in admitted["admission"]["checks"]]
    require(len(base_names) == 18 and all(g["passed"] is True for g in admitted["admission"]["checks"]),
            "all complete original readonly admission checks")
    gates = base_names+GATE_SUFFIX
    bindings = list(manifest["scientific_modules"])+[specs[ENTRY_ROLE], specs[MATH_ROLE]]
    require(operation["scientific_entry_role"] == ENTRY_ROLE
            and operation["scientific_kind"] == KIND
            and operation["scientific_module_binding"] == bindings
            and operation["ordered_targets"] == TARGETS
            and operation["complete_target_counts"] == [1]
            and operation["scientific_field_names"] == SCI_FIELDS
            and operation["complete_gate_names"] == gates
            and operation["return_parameters"] == RETURN_PARAMETERS
            and operation["fixed_runtime"] == RUNTIME,
            "complete distinct receiver-free target contract")
    L = json.loads(core.read_spec(root, specs[L_ACTUAL_ROLE]))
    Le = json.loads(core.read_spec(root, specs[L_EXECUTION_ROLE]))
    C = json.loads(core.read_spec(root, specs[CENTRE_ACTUAL_ROLE]))
    Ce = json.loads(core.read_spec(root, specs[CENTRE_EXECUTION_ROLE]))
    require(L["run_id"] == Le["run_id"] == "44724797559"
            and L["run_attempt"] == Le["run_attempt"] == "1"
            and L["complete"] is True and Le["scientific_complete"] is True
            and L["actual_returncode"] == Le["actual_child_returncode"] == 0
            and L["saved_record_count"] == 3
            and L["actual_progress"]["old_targets_recomputed"] == 0,
            "whole three completed low-family records and execution retained read only")
    require(C["run_id"] == Ce["run_id"] == "44727185157"
            and C["run_attempt"] == Ce["run_attempt"] == "1"
            and C["complete"] is True and Ce["scientific_complete"] is True
            and C["actual_returncode"] == Ce["actual_child_returncode"] == 0
            and C["saved_record_count"] == 1
            and C["necessary_budget"]["fixed_recipe_rejection_proved"] is True
            and C["necessary_budget"]["actual_operator_singularity_proved"] is False,
            "whole completed centre mean exclusion retained, not recomputed")
    run, attempt = os.environ.get("GITHUB_RUN_ID", ""), os.environ.get("GITHUB_RUN_ATTEMPT", "")
    event, checkout = os.environ.get("GITHUB_SHA", ""), os.environ.get("ACTUAL_CHECKOUT_COMMIT", "")
    require(re.fullmatch(r"\d{1,20}", run) and re.fullmatch(r"\d{1,10}", attempt)
            and re.fullmatch(r"[0-9a-f]{40}", event) and re.fullmatch(r"[0-9a-f]{40}", checkout),
            "actual public execution identity")
    if args.preflight_only:
        require(not any(name in sys.modules for name in ("flint", "numpy", "scipy")), "no numerical preflight imports")
        value = {"kind": PREFLIGHT_KIND, "complete": True, "preflight_only": True,
            "problem_id": readonly.PROBLEM_ID, "manifest_sha256": args.manifest_sha,
            "admission": admitted["admission"], "new_targets": TARGETS,
            "return_parameters": RETURN_PARAMETERS,
            "whole_completed_L_and_centre_records_retained": True,
            "numerical_libraries_imported": False, "new_scientific_targets_evaluated": 0,
            "old_scientific_targets_evaluated": 0}
        print(canonical(value).decode(), end="", flush=True)
        return 0
    helper = import_pinned(root, specs["science"], "_FBc_original_definition_helpers")
    completed = admitted["completed_tracefree_inputs"]
    output = Path(args.out)
    require(not output.exists(), "one distinct never-overwritten scientific outcome")
    output.parent.mkdir(parents=True, exist_ok=True)
    def reference(a, e):
        return {"kind": "two_whole_existing_public_object_references_v1",
            "scientific": {"file": copy.deepcopy(specs[a]), "json_path": []},
            "execution": {"file": copy.deepcopy(specs[e]), "json_path": []},
            "all_prior_bounds_and_scopes_retained_without_recomputation": True}
    document = {"kind": KIND, "problem_id": readonly.PROBLEM_ID,
        "complete": False, "proved": False, "actual_returncode": None,
        "run_id": run, "run_attempt": attempt, "workflow_event_commit": event,
        "actual_checkout_commit": checkout, "manifest_sha256": args.manifest_sha,
        "scientific_modules": copy.deepcopy(bindings),
        "complete_current_file_receipts": copy.deepcopy(admitted["current_receipts"]),
        "original_admission": copy.deepcopy(admitted["admission"]),
        "complete_restoration_receipts": helper.restoration_reference(
            admitted["complete_restoration_receipts"], manifest, run, attempt, canonical, digest),
        "parameters": copy.deepcopy(manifest["parameters"]),
        "return_parameters": copy.deepcopy(RETURN_PARAMETERS),
        "retained_scope": copy.deepcopy(operation["retained_scope"]),
        "copied_same_operator_records": copy.deepcopy(admitted["same_operator_records"]),
        "prior_complete_WVC_provider": {"kind": "whole_existing_public_object_reference_v1",
            "file": copy.deepcopy(specs["WVC_actual"]), "json_path": [],
            "all_original_successes_false_gates_and_scopes_retained": True},
        "completed_original_L": reference(L_ACTUAL_ROLE, L_EXECUTION_ROLE),
        "completed_original_centre_mean_floor": reference(CENTRE_ACTUAL_ROLE, CENTRE_EXECUTION_ROLE),
        "runtime": {}, "reference_identity": None, "complete_support_contract": None,
        "stage": "complete_readonly_inputs_saved",
        "preparation_prefix": {"stage": "not_started", "detail": None},
        "current_target": None, "completed_targets": [], "gates": [],
        "new_records": {}, "saved_record_count": 0, "failure": None,
        "actual_mathematical_wall_seconds": 0.0, "automatic_retry_authorized": False,
        "actual_progress": {"original_inputs_admitted": True,
            "reference_definitions_materialized": 0, "complete_centre_parents": 0,
            "original_closed_rows_covered": 0, "original_intersections": 0,
            "new_raw_FBc_records_saved": 0, "new_complete_targets": 0,
            "old_completed_targets_recomputed": 0, "old_small_K50_graphs_called": 0,
            "Gf_actions_evaluated": 0, "low_inverse_actions_evaluated": 0,
            "endpoint_or_atom_targets_evaluated": 0, "old_producer_entrypoints_called": 0,
            "new_arrays_published": 0, "new_artifacts": 0, "new_Releases": 0},
        "trial_comparison": {"complete_FBc_raw_norm_proved": False,
            "actual_GH_used_as_finite_F": False, "all_signed_terms_in_underlying_F_retained": True,
            "positive_triangle_pays_without_subtracting_positive_bounds": True,
            "complete_low_CFB_inverse_proved": False, "actual_low_high_inverse_proved": False,
            "actual_physical_outer_rows_proved": False, "original_finite_rho_bridge_proved": False,
            "original_seven_input_ports_proved": False, "either_original_RHS_proved": False,
            "topic_completion_proved": False}}
    require(sorted(document) == SCI_FIELDS, "whole distinct result schema")
    math_start = None
    def budget():
        if math_start is not None:
            require(time.perf_counter()-math_start <= RETURN_PARAMETERS["maximum_scientific_wall_seconds"],
                    "fixed complete source-comparison wall cap; prefix retained")
    def publish():
        if math_start is not None:
            elapsed = time.perf_counter()-math_start
            require(math.isfinite(elapsed) and elapsed >= 0, "finite mathematical elapsed time")
            document["actual_mathematical_wall_seconds"] = elapsed
        raw = canonical(document)
        require(0 < len(raw) <= operation["maximum_scientific_bytes"] < 100000,
                "whole small scientific output budget")
        temporary = output.with_name(output.name+".tmp")
        with temporary.open("wb") as stream:
            stream.write(raw); stream.flush(); os.fsync(stream.fileno())
        temporary.replace(output)
        print(json.dumps({"stage": document["stage"], "current_target": document["current_target"],
            "saved_record_count": document["saved_record_count"], "bytes": len(raw),
            "sha256": digest(raw)}, sort_keys=True), flush=True)
    def gate(name):
        require(len(document["gates"]) < len(gates) and gates[len(document["gates"])] == name,
                "complete declared gate order")
        document["gates"].append({"name": name, "passed": True}); publish()
    def progress(stage, detail):
        budget()
        require(isinstance(stage, str) and isinstance(detail, dict)
                and len(canonical({"stage": stage, "detail": detail})) < 2500, "bounded complete progress metadata")
        document["preparation_prefix"] = {"stage": stage, "detail": copy.deepcopy(detail)}
        if stage == "same_exact_reference_definition":
            document["actual_progress"]["reference_definitions_materialized"] = detail["parents_verified"]
        elif stage == "complete_new_centre_parent":
            document["actual_progress"]["complete_centre_parents"] = detail["parents_complete"]
            document["actual_progress"]["original_closed_rows_covered"] = detail["closed_rows_covered"]
            document["actual_progress"]["original_intersections"] = detail["closed_intersections"]
        document["stage"] = "working:"+stage; publish()
    def emit(name, value):
        budget()
        require(document["saved_record_count"] < 3
                and RECORD_NAMES[document["saved_record_count"]] == name,
                "complete new raw F source record order")
        original_upper = api.upper(value)
        record = {"ball": original_upper.str(helper.PARAMETERS["decimal_record_digits"])}
        helper.record_text(record)
        document["new_records"][name] = record
        document["saved_record_count"] += 1
        document["actual_progress"]["new_raw_FBc_records_saved"] = document["saved_record_count"]
        document["stage"] = "complete_new_record_saved"; publish()
        reread = json.loads(output.read_bytes())["new_records"][name]
        require(reread == record, "whole directed new record saved and reread")
        saved = api.old_interval(reread)
        require(saved.is_finite() and saved.contains(original_upper),
                "saved whole decimal interval contains the original directed upper")
        return api.upper(saved)
    publish()
    try:
        for name in base_names: gate(name)
        gate(GATE_SUFFIX[0])
        import flint
        require(platform.python_version() == RUNTIME["Python"] and flint.__version__ == RUNTIME["python_flint"]
                and not any(name in sys.modules for name in ("numpy", "scipy")), "fixed direct runtime without floating probes")
        require(all(os.environ.get(name) == "1" for name in
                    ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")), "declared thread settings")
        flint.ctx.prec = 320
        api = helper.NumericalAPI(flint)
        document["runtime"] = copy.deepcopy(RUNTIME); gate(GATE_SUFFIX[1])
        old = {}
        for name, record in admitted["same_operator_records"].items():
            if name in ("G_c", "L_c_raw"):
                exact = Fraction(record); value = api.rational(exact.numerator, exact.denominator)
            else: value = api.old_interval(record)
            old[name] = api.upper(value)
        require(len(old) == 29 and admitted["same_operator_records"] == completed["copied_records"],
                "whole29 original saved records without old target calls")
        gate(GATE_SUFFIX[2])
        collar = import_pinned(root, specs["collar_math"], "_FBc_collar")
        km = import_pinned(root, specs["kernel_math"], "_FBc_kernel")
        assembly = import_pinned(root, specs["assembly_math"], "_FBc_assembly")
        reference_math = import_pinned(root, specs["reference_math"], "_FBc_reference")
        closure = import_pinned(root, specs[MATH_ROLE], "_FBc_closure")
        math_start = time.perf_counter()
        context = assembly.prepare_complete_kernel_context(api, km, reference_math, collar, admitted,
            completed["complete_original_candidate"], old, core.signed_display_centre, progress)
        require(context.reference_identity["original_reference_chain"] == completed["complete_original_candidate"]["reference_chain"]
                and context.reference_identity["selected_diagonal_chain"] == completed["selected_diagonal_chain"]
                and len(context.domain.cells) == 155 and context.parent_definition_count == 153
                and context.original_body_row_count == 4650 and context.original_intersection_count == 4801
                and all(value is True for value in context.qualifications.values()),
                "same complete original WVC reference and all coefficient coverage")
        document["reference_identity"] = copy.deepcopy(context.reference_identity)
        document["complete_support_contract"] = {
            "all_original_qualifications": copy.deepcopy(context.qualifications),
            "original_parent_count": 153, "complete_comparison_panels": 155,
            "original_closed_rows": 4650, "original_intersections": 4801,
            "input_head_dimension": 193, "active_head_dimension": 128,
            "independent_original_even_mean_retained": True,
            "exact_centre_mean_to_high_zero_not_a_family_claim": True,
            "returned_high_dimension": 128, "returned_high_last_index": 160,
            "complete_trial_last_index": 224, "complete_primal_residual_last_index": 288,
            "actual_unknown_high_not_truncated": True, "true_Jstar_to_R": True,
            "all_atom_receivers_are_external_to_this_source_only_target": True}
        gate(GATE_SUFFIX[3])
        document["current_target"] = TARGETS[0]
        document["stage"] = "starting_complete_receiver_free_FBc"; publish()
        operators = closure.build_receiver_free_WJK_comparisons(api, km, context, assembly,
                                                                include_actual_remainders=False)
        require(set(operators) == {"whole_FBc_to_K0_raw"}, "only this one complete new comparison target")
        comparison = operators["whole_FBc_to_K0_raw"]
        require(comparison.atom_count == 0 and comparison.domain is context.domain,
                "raw high output without low/atom receivers")
        km.complete_positive_comparison_norm(comparison, emit, "complete_projected_WJK_FBc_raw")
        require(list(document["new_records"]) == RECORD_NAMES and document["saved_record_count"] == 3,
                "all three whole new comparison records")
        document["completed_targets"] = list(TARGETS); document["current_target"] = None
        document["actual_progress"]["new_complete_targets"] = 1
        document["trial_comparison"]["complete_FBc_raw_norm_proved"] = True
        document["trial_comparison"]["complete_norm_record_name"] = RECORD_NAMES[-1]
        gate(GATE_SUFFIX[4])
        require(Path(args.manifest).read_bytes() == manifest_raw, "frozen manifest unchanged")
        for spec in manifest["files"]: core.read_spec(root, spec)
        gate(GATE_SUFFIX[5])
        require(document["actual_progress"]["Gf_actions_evaluated"] == 0
                and document["actual_progress"]["old_completed_targets_recomputed"] == 0
                and document["trial_comparison"]["actual_low_high_inverse_proved"] is False
                and document["trial_comparison"]["either_original_RHS_proved"] is False,
                "complete independent target and all original remaining obligations")
        document["actual_returncode"] = 0; document["complete"] = True; document["proved"] = True
        document["stage"] = "complete_receiver_free_FBc_raw_comparison"
        gate(GATE_SUFFIX[6])
        require(sorted(document) == SCI_FIELDS, "entire final result schema")
        return 0
    except BaseException as error:
        document["complete"] = False; document["actual_returncode"] = 1
        document["stage"] = "failed_with_complete_prefix"
        trace = traceback.format_exc(); print(trace, flush=True)
        document["failure"] = {"type": type(error).__name__, "message": str(error)[:1500],
            "traceback": trace[-2500:], "full_traceback_in_public_job_log": True}
        publish(); return 1


if __name__ == "__main__":
    sys.exit(main())
