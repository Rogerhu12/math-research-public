"""Own-Actions v3 continuation of the unfinished low193/97 endpoint target.

The complete old W2C reader and its21 exact native restorations are reused.
The existing candidate owner is imported only for reusable definitions after
admission; its main and all five old target graphs are never called.  The
scientific result is explicitly floating comparison data, with proved=False.
The complete original44719196304/1 outcome and execution are pinned inputs.
They show138 coefficient-definition panels but zero propagation, endpoint
or matching targets.  The new balanced full plan is complete before any
propagation, and all matching frames are returned to the original raw space.
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
SOURCE_PATH = TOPIC + "scripts/fourfold_codazzi_low_centre_balanced_endpoint_owner.py"
KIND = "complete_WVC_low193_balanced_endpoint_continuation_v3"
PREFLIGHT_KIND = "complete_WVC_low193_balanced_endpoint_preflight_v3"
ENTRY_ROLE = "low_centre_balanced_endpoint_owner"
MATH_ROLE = "low_centre_balanced_endpoint_diagnostic"
TARGET = "remaining_low193_balanced_plan_endpoint_and_all_boundary_frames"
PRIOR_ACTUAL_ROLE = "previous_low193_endpoint_actual"
PRIOR_EXECUTION_ROLE = "previous_low193_endpoint_execution"
RUNTIME = {"Python": "3.12.14", "python_flint": "0.9.0", "numpy": "2.3.5",
           "scipy": "1.16.3", "bits": 320, "BLAS_threads": 1}
DIAGNOSTIC_PARAMETERS = {
    "state_dimension": 193, "left_frame_dimension": 97, "right_frame_dimension": 96,
    "endpoint_matrix_dimension": 97, "outer_impedance": "13/80",
    "maximum_panels": 155, "maximum_step_infinity_norm": 4.0,
    "maximum_substeps_per_panel": 8192, "maximum_substeps_per_direction": 8192,
    "maximum_diagnostic_wall_seconds": 1800, "maximum_private_diagnostic_bytes": 35000,
    "coefficient_rule": "entrywise float64 midpoint of whole-panel signed AL enclosures",
    "length_rule": "float64 midpoint of true panel length enclosures",
    "high_feedback_evaluated": False, "actual_centre_coefficients_identified_with_midpoints": False,
    "old_W2C_graphs_evaluated": 0, "automatic_retries": 0,
    "prior_run_id": "44719196304", "prior_run_attempt": "1",
    "prior_coefficient_definition_prefix": 138, "prior_endpoint_targets_completed": 0,
    "complete_all_panel_plan_before_propagation": True,
    "similarity_balance": "positive dyadic diag(1_96,q_mid,q_mid I_96) from same WVC reference",
    "every_panel_interface_and_all_matching_frames_in_raw_coordinates": True,
}
GATE_SUFFIX = [
    "fixed_Arb_and_floating_runtime_verified",
    "same29_original_records_typed_without_recomputing_bounds",
    "whole_same_WVC_context_materialized",
    "complete_low193_balanced_continuation_saved",
    "all_current_inputs_reverified_after_new_work",
    "complete_floating_diagnostic_without_inverse_claim",
]
SCI_FIELDS = [
    "actual_checkout_commit", "actual_mathematical_wall_seconds", "actual_progress",
    "actual_returncode", "automatic_retry_authorized", "complete",
    "complete_current_file_receipts", "complete_restoration_receipts", "completed_targets",
    "copied_same_operator_records", "current_target", "diagnostic", "diagnostic_parameters",
    "failure", "gates", "kind", "manifest_sha256", "original_admission", "parameters",
    "preparation_prefix", "prior_complete_WVC_provider", "prior_endpoint_attempt", "problem_id", "proved",
    "reference_identity", "retained_scope", "run_attempt", "run_id", "runtime",
    "scientific_modules", "stage", "workflow_event_commit",
]


def require(ok, message):
    if not ok:
        raise ValueError(message)


def import_pinned(root, spec, name):
    path = (root / spec["path"]).resolve()
    require(path.is_relative_to(root) and path.is_file(), "whole source containment")
    raw = path.read_bytes()
    require(len(raw) == spec["bytes"] and hashlib.sha256(raw).hexdigest() == spec["sha256"]
            and hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
            == spec["git_blob_sha"], "complete bound source: " + spec["role"])
    loader = importlib.util.spec_from_file_location(name, path)
    require(loader is not None and loader.loader is not None, "whole source loader")
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
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public",
            "one public own-Actions diagnostic only")
    require(args.bits == 320 and "flint" not in sys.modules
            and "numpy" not in sys.modules and "scipy" not in sys.modules,
            "complete readonly admission before numerical imports")
    root = Path(args.repo).resolve()
    manifest_raw = Path(args.manifest).read_bytes()
    require(0 < len(manifest_raw) < 100000
            and hashlib.sha256(manifest_raw).hexdigest() == args.manifest_sha,
            "whole frozen manifest identity")
    initial = json.loads(manifest_raw)
    specs = {item["role"]: item for item in initial["files"]}
    require(specs[ENTRY_ROLE]["path"] == SOURCE_PATH
            and Path(__file__).resolve() == (root / SOURCE_PATH).resolve(),
            "actual new diagnostic owner path")
    raw_self = Path(__file__).read_bytes()
    require(len(raw_self) == specs[ENTRY_ROLE]["bytes"]
            and hashlib.sha256(raw_self).hexdigest() == specs[ENTRY_ROLE]["sha256"],
            "whole new owner bytes")
    core = import_pinned(root, specs["readonly_core"], "_low193_readonly_core")
    readonly = import_pinned(root, specs["readonly_admission"], "_low193_readonly")
    admitted = readonly.admit(root, args.manifest, args.manifest_sha, args.native,
        args.native_receipts, args.candidate_index, args.centre_repair,
        args.root_germ, args.root_budget, core)
    manifest = admitted["manifest"]
    operation = manifest["operation"]
    canonical, digest = core.canonical, core.digest
    # These two original outcomes contain explicitly floating diagnostics.
    # Their bytes are verified before parsing; JSON float round-trip keeps
    # the declared binary64 values and does not turn them into Arb bounds.
    prior_actual = json.loads(core.read_spec(root, specs[PRIOR_ACTUAL_ROLE]))
    prior_execution = json.loads(core.read_spec(root, specs[PRIOR_EXECUTION_ROLE]))
    require(prior_actual["run_id"] == prior_execution["run_id"] == "44719196304"
            and prior_actual["run_attempt"] == prior_execution["run_attempt"] == "1"
            and prior_actual["complete"] is False and prior_actual["proved"] is False
            and prior_execution["scientific_started"] is True
            and prior_execution["scientific_children"] == 1
            and prior_execution["actual_child_returncode"] == 1
            and prior_execution["scientific_complete"] is False
            and prior_execution["completed_target_names"] == []
            and prior_actual["diagnostic"]["progress"]["coefficient_panels"] == 138
            and all(prior_actual["diagnostic"]["progress"][name] == 0 for name in
                    ("forward_panels", "backward_panels", "forward_substeps", "backward_substeps", "matched_boundaries")),
            "whole original failed outcome permits only its unfinished endpoint target")
    admission_names = [item["name"] for item in admitted["admission"]["checks"]]
    require(len(admission_names) == 18
            and all(item["passed"] is True for item in admitted["admission"]["checks"]),
            "all complete original and collar admission checks")
    gates = admission_names + GATE_SUFFIX
    require(operation["scientific_entry_role"] == ENTRY_ROLE
            and operation["scientific_kind"] == KIND
            and operation["ordered_targets"] == [TARGET]
            and operation["complete_target_counts"] == [1]
            and operation["scientific_field_names"] == SCI_FIELDS
            and operation["complete_gate_names"] == gates
            and operation["diagnostic_parameters"] == DIAGNOSTIC_PARAMETERS
            and operation["fixed_runtime"] == RUNTIME,
            "whole distinct new diagnostic contract")
    bound_sources = list(manifest["scientific_modules"]) + [specs[ENTRY_ROLE], specs[MATH_ROLE]]
    require(operation["scientific_module_binding"] == bound_sources,
            "original seven definitions plus both complete new sources")
    run = os.environ.get("GITHUB_RUN_ID", "")
    attempt = os.environ.get("GITHUB_RUN_ATTEMPT", "")
    event = os.environ.get("GITHUB_SHA", "")
    checkout = os.environ.get("ACTUAL_CHECKOUT_COMMIT", "")
    require(re.fullmatch(r"\d{1,20}", run) and re.fullmatch(r"\d{1,10}", attempt)
            and re.fullmatch(r"[0-9a-f]{40}", event)
            and re.fullmatch(r"[0-9a-f]{40}", checkout), "actual public run identity")
    if args.preflight_only:
        require(not any(name in sys.modules for name in ("flint", "numpy", "scipy")),
                "readonly preflight contains no numerical execution")
        value = {"kind": PREFLIGHT_KIND, "complete": True, "preflight_only": True,
            "problem_id": readonly.PROBLEM_ID, "manifest_sha256": args.manifest_sha,
            "admission": admitted["admission"], "new_target": TARGET,
            "same_complete_WVC_reference": admitted["paired_inputs"]["reference_chain"],
            "same_complete_selected_diagonal_chain":
                admitted["completed_tracefree_inputs"]["selected_diagonal_chain"],
            "diagnostic_parameters": DIAGNOSTIC_PARAMETERS,
            "complete_prior_failed_outcome_and_execution_admitted": True,
            "prior_endpoint_or_matching_targets_completed": 0,
            "new_scientific_targets_evaluated": 0, "old_scientific_calls": 0,
            "numerical_libraries_imported": False}
        print(canonical(value).decode("utf-8"), end="", flush=True)
        return 0

    helper = import_pinned(root, specs["science"], "_low193_W2C_definition_helpers")
    output = Path(args.out)
    require(not output.exists(), "one new never-overwritten scientific outcome")
    output.parent.mkdir(parents=True, exist_ok=True)
    private_diagnostic = output.with_name("low193-private-diagnostic-prefix.json")
    require(not private_diagnostic.exists(), "one new private diagnostic prefix")
    completed = admitted["completed_tracefree_inputs"]
    document = {
        "kind": KIND, "problem_id": readonly.PROBLEM_ID, "complete": False, "proved": False,
        "stage": "complete_readonly_inputs_saved", "failure": None, "actual_returncode": None,
        "run_id": run, "run_attempt": attempt, "workflow_event_commit": event,
        "actual_checkout_commit": checkout, "manifest_sha256": args.manifest_sha,
        "scientific_modules": copy.deepcopy(bound_sources),
        "complete_current_file_receipts": copy.deepcopy(admitted["current_receipts"]),
        "original_admission": copy.deepcopy(admitted["admission"]),
        "complete_restoration_receipts": helper.restoration_reference(
            admitted["complete_restoration_receipts"], manifest, run, attempt, canonical, digest),
        "parameters": copy.deepcopy(manifest["parameters"]),
        "diagnostic_parameters": copy.deepcopy(DIAGNOSTIC_PARAMETERS),
        "retained_scope": copy.deepcopy(operation["retained_scope"]),
        "copied_same_operator_records": copy.deepcopy(admitted["same_operator_records"]),
        "prior_complete_WVC_provider": {
            "kind": "whole_existing_public_object_reference_v1",
            "file": copy.deepcopy(specs["WVC_actual"]), "json_path": [],
            "all_original_fields_successes_false_gates_scopes_and_prefixes_admitted": True},
        "prior_endpoint_attempt": {
            "kind": "two_whole_existing_public_object_references_v1",
            "scientific": {"file": copy.deepcopy(specs[PRIOR_ACTUAL_ROLE]), "json_path": []},
            "execution": {"file": copy.deepcopy(specs[PRIOR_EXECUTION_ROLE]), "json_path": []},
            "original_complete_outcome_and_execution_retained": True,
            "completed_coefficient_definition_prefix": 138,
            "completed_endpoint_or_matching_targets": 0,
            "new_continuation_does_not_repeat_a_successful_endpoint_or_matching_target": True},
        "preparation_prefix": {"stage": "not_started", "detail": None},
        "reference_identity": None, "diagnostic": None, "runtime": {},
        "current_target": None, "completed_targets": [], "gates": [],
        "actual_progress": {"original_inputs_admitted": True,
            "reference_definitions_materialized": 0, "complete_centre_parents": 0,
            "original_closed_rows_covered": 0, "original_intersections": 0,
            "new_targets_completed": 0, "old_completed_targets_recomputed": 0,
            "old_W2C_graphs_called": 0, "existing_W2C_owner_main_called": False,
            "existing_W2C_owner_used_for_definition_helpers_only": True,
            "old_completed_producer_entrypoints_called": 0, "new_arrays_published": 0},
        "automatic_retry_authorized": False, "actual_mathematical_wall_seconds": 0.0,
    }
    require(sorted(document) == SCI_FIELDS, "complete distinct output schema")
    math_start = None
    prepared = False

    def publish():
        if math_start is not None:
            elapsed = time.perf_counter() - math_start
            require(math.isfinite(elapsed) and elapsed >= 0, "finite mathematical elapsed time")
            document["actual_mathematical_wall_seconds"] = elapsed
        raw = canonical(document)
        require(0 < len(raw) <= operation["maximum_scientific_bytes"] < 100000,
                "whole one-file scientific publication cap")
        temporary = output.with_name(output.name + ".tmp")
        with temporary.open("wb") as stream:
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())
        temporary.replace(output)
        print(json.dumps({"stage": document["stage"], "current_target": document["current_target"],
                          "completed_targets": document["completed_targets"],
                          "whole_output_bytes": len(raw), "whole_output_sha256": digest(raw)},
                         sort_keys=True), flush=True)

    def gate(name):
        require(len(document["gates"]) < len(gates)
                and gates[len(document["gates"])] == name, "whole declared gate order")
        document["gates"].append({"name": name, "passed": True})
        publish()

    def copy_private_diagnostic():
        if private_diagnostic.is_file():
            raw = private_diagnostic.read_bytes()
            require(0 < len(raw) <= DIAGNOSTIC_PARAMETERS["maximum_private_diagnostic_bytes"],
                    "complete bounded private diagnostic record")
            # The diagnostic owner returned binary64 numbers.  A Decimal
            # parser would break exact JSON round-trip equality with them.
            document["diagnostic"] = json.loads(raw)

    def progress(stage, detail):
        require(isinstance(stage, str) and isinstance(detail, dict)
                and len(canonical({"stage": stage, "detail": detail})) <= 2500,
                "bounded progress metadata, no arrays")
        if not prepared:
            document["preparation_prefix"] = {"stage": stage, "detail": copy.deepcopy(detail)}
        if stage == "same_exact_reference_definition":
            document["actual_progress"]["reference_definitions_materialized"] = detail["parents_verified"]
        elif stage == "complete_new_centre_parent":
            document["actual_progress"]["complete_centre_parents"] = detail["parents_complete"]
            document["actual_progress"]["original_closed_rows_covered"] = detail["closed_rows_covered"]
            document["actual_progress"]["original_intersections"] = detail["closed_intersections"]
        elif stage == "low_centre_endpoint_diagnostic":
            copy_private_diagnostic()
        document["stage"] = "working:" + stage
        publish()

    publish()
    try:
        for name in admission_names:
            gate(name)
        import flint
        import numpy
        import scipy
        require(platform.python_version() == RUNTIME["Python"]
                and flint.__version__ == RUNTIME["python_flint"]
                and numpy.__version__ == RUNTIME["numpy"] and scipy.__version__ == RUNTIME["scipy"],
                "fixed published Arb/NumPy/SciPy runtime")
        require(all(os.environ.get(name) == "1" for name in
                    ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")),
                "declared single-thread BLAS runtime")
        flint.ctx.prec = 320
        api = helper.NumericalAPI(flint)
        document["runtime"] = copy.deepcopy(RUNTIME)
        gate(GATE_SUFFIX[0])
        old = {}
        for name, record in admitted["same_operator_records"].items():
            if name in ("G_c", "L_c_raw"):
                exact = Fraction(record)
                value = api.rational(exact.numerator, exact.denominator)
            else:
                value = api.old_interval(record)
            old[name] = api.upper(value)
        require(len(old) == 29 and admitted["same_operator_records"] == completed["copied_records"],
                "whole29 original saved records, no old target calls")
        gate(GATE_SUFFIX[1])
        collar = import_pinned(root, specs["collar_math"], "_low193_collar_math")
        km = import_pinned(root, specs["kernel_math"], "_low193_kernel_math")
        assembly = import_pinned(root, specs["assembly_math"], "_low193_assembly_math")
        reference = import_pinned(root, specs["reference_math"], "_low193_reference_math")
        diagnostic = import_pinned(root, specs[MATH_ROLE], "_low193_endpoint_diagnostic")
        require(diagnostic.STATE_DIMENSION == DIAGNOSTIC_PARAMETERS["state_dimension"]
                and diagnostic.LEFT_FRAME_DIMENSION == DIAGNOSTIC_PARAMETERS["left_frame_dimension"]
                and diagnostic.RIGHT_FRAME_DIMENSION == DIAGNOSTIC_PARAMETERS["right_frame_dimension"]
                and diagnostic.MAX_PANELS == DIAGNOSTIC_PARAMETERS["maximum_panels"]
                and diagnostic.MAX_STEP_INFINITY_NORM == DIAGNOSTIC_PARAMETERS["maximum_step_infinity_norm"]
                and diagnostic.MAX_SUBSTEPS_PER_PANEL == DIAGNOSTIC_PARAMETERS["maximum_substeps_per_panel"]
                and diagnostic.MAX_SUBSTEPS_PER_DIRECTION == DIAGNOSTIC_PARAMETERS["maximum_substeps_per_direction"]
                and diagnostic.MAX_WALL_SECONDS == DIAGNOSTIC_PARAMETERS["maximum_diagnostic_wall_seconds"]
                and diagnostic.MAX_OUTPUT_BYTES == DIAGNOSTIC_PARAMETERS["maximum_private_diagnostic_bytes"],
                "complete fixed diagnostic dimensions and budgets")
        math_start = time.perf_counter()
        context = assembly.prepare_complete_kernel_context(api, km, reference, collar, admitted,
            completed["complete_original_candidate"], old, core.signed_display_centre, progress)
        require(context.reference_identity["original_reference_chain"] ==
                    completed["complete_original_candidate"]["reference_chain"]
                and context.reference_identity["selected_diagonal_chain"] ==
                    completed["selected_diagonal_chain"], "same complete original WVC reference")
        document["reference_identity"] = copy.deepcopy(context.reference_identity)
        prepared = True
        gate(GATE_SUFFIX[2])
        document["current_target"] = TARGET
        document["stage"] = "starting:" + TARGET
        publish()
        result = diagnostic.run_from_context(api, km, context, private_diagnostic, progress,
            prior_attempt={"source_identity": copy.deepcopy(specs[PRIOR_ACTUAL_ROLE]),
                           "whole_original_outcome": prior_actual})
        require(result["status"] == "complete_floating_comparison_diagnostic_only"
                and all(value is False for value in result["certification"].values())
                and result["progress"]["matched_boundaries"] == len(context.domain.cells) + 1
                and result["complete_plan"]["complete"] is True
                and result["complete_plan"]["budget_passed"] is True
                and result["continuation"]["original_raw_definition_prefix_reidentified"] is True,
                "complete new floating target with all proof flags false")
        copy_private_diagnostic()
        require(document["diagnostic"] == result, "whole exact diagnostic readback")
        document["completed_targets"] = [TARGET]
        document["current_target"] = None
        document["actual_progress"]["new_targets_completed"] = 1
        gate(GATE_SUFFIX[3])
        require(Path(args.manifest).read_bytes() == manifest_raw, "frozen manifest unchanged")
        for spec in manifest["files"]:
            core.read_spec(root, spec)
        gate(GATE_SUFFIX[4])
        document["actual_returncode"] = 0
        document["complete"] = True
        document["stage"] = "complete_floating_diagnostic_only"
        gate(GATE_SUFFIX[5])
        require(sorted(document) == SCI_FIELDS and document["proved"] is False,
                "complete distinct result, never an inverse certificate")
        return 0
    except BaseException as error:
        copy_private_diagnostic()
        document["complete"] = False
        document["actual_returncode"] = 1
        document["stage"] = "failed_with_complete_prefix"
        full_traceback = traceback.format_exc()
        print(full_traceback, flush=True)
        document["failure"] = {"type": type(error).__name__, "message": str(error)[:1500],
            "traceback": full_traceback[-2500:], "full_traceback_in_public_job_log": True}
        publish()
        return 1


if __name__ == "__main__":
    sys.exit(main())
