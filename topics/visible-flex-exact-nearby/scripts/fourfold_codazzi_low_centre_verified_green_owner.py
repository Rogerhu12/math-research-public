"""Public first directed R141 low193 Green/source/observation certificate.

The original W2C readonly admission and21 native restorations are retained.
The successful44721851908/1 floating endpoint diagnostic is read whole and
never rerun.  Its complete raw model is reidentified while constructing the
exact dyadic comparison generators needed by this new directed target.
The same model is exactly refined along every completed substep cut, with
directed short-span checks.  New reference-chart proposals do not replay
the successful AL forward/backward QR or its endpoint/matching SVDs.

The first two targets establish the exact comparison Green and the complete
true-coefficient residual.  If its strict sufficient gate is false, the
planned complete branch ends with those two bounds and no inverse claim.
Otherwise all four declared source roles,193 output atoms, and every whole
radial box are certified.  Full CFB, the original finite rho bridge, actual
family differences, seven input ports and both original RHS remain unpaid.
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
import resource
import struct
import sys
import time
import traceback
from fractions import Fraction
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby/"
SOURCE_PATH = TOPIC + "scripts/fourfold_codazzi_low_centre_verified_green_owner.py"
KIND = "complete_R141_low193_directed_Green_certificate_v1"
PREFLIGHT_KIND = "complete_R141_low193_directed_Green_preflight_v1"
ENTRY_ROLE = "low_centre_verified_green_owner"
MATH_ROLE = "low_centre_verified_green_math"
LOCAL_ROLE = "low_centre_verified_green_local_math"
REFINED_ROLE = "low_centre_refined_green_math"
PRIOR_ACTUAL_ROLE = "completed_low193_balanced_endpoint_actual"
PRIOR_EXECUTION_ROLE = "completed_low193_balanced_endpoint_execution"
CENTRE_ACTUAL_ROLE = "completed_centre_mean_floor_actual"
CENTRE_EXECUTION_ROLE = "completed_centre_mean_floor_execution"
TARGETS = [
    "complete_exact_low193_comparison_Green",
    "complete_true_hybrid_low_coefficient_defect",
    "complete_ordinary_raw_low_source_and193_atoms",
    "complete_transformed_low_source_and193_atoms",
    "complete_low_second_kind_inverse_and193_atoms",
    "complete_high0_return_source_without_CFB",
    "complete_actual_whole_interval_low_transversality",
]
SOURCE_ROLES = ["ordinary_raw_low_source", "transformed_low_source",
                "low_second_kind_correction", "centre_high0_return_source"]
RUNTIME = {"Python": "3.12.14", "python_flint": "0.9.0",
           "admission_and_model_definition_bits": 320,
           "directed_certificate_bits": 768, "BLAS_threads": 1}
CERTIFICATE_PARAMETERS = {
    "state_dimension": 193, "left_carrier": 97, "right_carrier": 96,
    "whole_output_atom_count": 193, "outer_impedance": "13/80",
    "original_parent_count": 153, "comparison_panel_count": 155,
    "original_body_rows": 4650, "original_closed_intersections": 4801,
    "prior_complete_substeps": 1424, "maximum_refined_cells": 1536,
    "integration_boxes_per_refined_cell": 4, "local_shared_scalar_Taylor_order": 16,
    "directed_balanced_span_per_refined_cell": 4,
    "maximum_private_packed_payload_bytes": 8589934592,
    "maximum_decoded_matrix_entries": 200000,
    "maximum_scientific_process_resident_bytes": 15032385536,
    "cuts_rule": "all exact v3 equal-fraction cuts retained; at most one directed-guarded doubling per parent",
    "comparison_rule": "exact dyadic product of original binary64 h_mid and AL_mid",
    "comparison_physical_generator": "H_i divided by TRUE h_i",
    "coefficient_object": "same WVC hybrid centre: full-family eta and repaired lower coefficients",
    "refined_comparison_generator": "exact same H_i/n_i, raw identity transmissions at every inserted cut",
    "chart_rule": "determinant-one dyadic trial charts from same reference p,H at all true inserted nodes",
    "boundary_columns": "original exact root columns and exact rational13/80 Robin columns",
    "local_factor_method": "shared scalar whole-box Taylor enclosure with exact parent template reuse",
    "actual_coefficient_balls_narrowed_by_new_cuts": False,
    "compact_matrix_storage": "binary64 midpoint/radius with an Arb outward-containment guard for every entry",
    "source_packet_order": "complete defect first; after strict gap, four source roles together per cell",
    "complete_source_roles": ["true_coefficient_defect", "ordinary_raw_low_source",
        "transformed_low_source", "low_second_kind_correction", "centre_high0_return_source"],
    "maximum_certificate_wall_seconds": 16800,
    "completed_prior_run_id": "44721851908", "completed_prior_run_attempt": "1",
    "completed_centre_mean_floor_run_id": "44727185157",
    "completed_centre_mean_floor_run_attempt": "1",
    "completed_centre_mean_floor_or_original_L_targets_recomputed": False,
    "prior_model_chain": "33fdf6eeba4d5904c961b2bedea43c5207d80fb66920017168f41f9106cc4d79",
    "original_float_endpoint_QR_or_SVD_evaluated": False,
    "ordinary_source_is_L2_without_radial_derivative": True,
    "all193_observations_and_both_same_panel_triangles_retained": True,
    "complete_two_target_branch_if_strict_low_gate_false": True,
    "source_atom_point_branch_requires_strict_low_gate": True,
    "full_CFB_evaluated": False, "original_finite_rho_bridge_evaluated": False,
    "old_W2C_graphs_evaluated": 0, "automatic_retries": 0,
    "scalar_decimal_enclosure_digits": 48,
}
GATE_SUFFIX = [
    "fixed_directed_runtime_verified",
    "same29_original_records_typed_without_recomputing_bounds",
    "whole_same_WVC_context_and_successful_prior_model_identified",
    "complete_declared_directed_certificate_branch_saved",
    "all_current_inputs_reverified_after_new_work",
    "complete_low_only_scope_and_all_unpaid_obligations_retained",
]
SCI_FIELDS = [
    "actual_checkout_commit", "actual_mathematical_wall_seconds", "actual_progress",
    "actual_returncode", "automatic_retry_authorized", "certificate", "certificate_parameters",
    "complete", "complete_current_file_receipts", "complete_restoration_receipts",
    "completed_prior_centre_mean_floor", "completed_prior_diagnostic", "completed_targets", "copied_same_operator_records",
    "current_target", "failure", "gates", "kind", "manifest_sha256", "original_admission",
    "parameters", "preparation_prefix", "prior_complete_WVC_provider", "problem_id",
    "proved", "reference_identity", "retained_scope", "run_attempt", "run_id", "runtime",
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


def prior_success(actual, execution):
    require(actual["run_id"] == execution["run_id"] == "44721851908"
            and actual["run_attempt"] == execution["run_attempt"] == "1"
            and actual["complete"] is True and actual["proved"] is False
            and actual["actual_returncode"] == execution["actual_child_returncode"] == 0
            and execution["scientific_started"] is True
            and execution["scientific_children"] == 1
            and execution["scientific_complete"] is True,
            "whole successful original floating outcome and execution")
    diagnostic = actual["diagnostic"]
    expected = {"coefficient_panels": 155, "forward_panels": 155, "backward_panels": 155,
                "forward_substeps": 1424, "backward_substeps": 1424,
                "matched_boundaries": 156, "forward_interface_QR": 310, "backward_interface_QR": 310}
    require(diagnostic["status"] == "complete_floating_comparison_diagnostic_only"
            and diagnostic["progress"] == expected
            and diagnostic["comparison_matrix_sha256_chain"] == CERTIFICATE_PARAMETERS["prior_model_chain"]
            and all(value is False for value in diagnostic["certification"].values()),
            "complete prior low193 diagnostic retained without certification upgrade")
    plan = diagnostic["complete_plan"]
    require(plan["complete"] is True and plan["budget_passed"] is True
            and plan["planned_substeps_per_direction"] == 1424
            and plan["largest_panel_substeps"] == 80
            and len(plan["rows"]) == 155
            and all(type(row[6]) is int and 1 <= row[6] <= 80
                    and row[0] == i for i, row in enumerate(plan["rows"]))
            and sum(row[6] for row in plan["rows"]) == 1424,
            "complete old plan defines the exact new integration boxes")
    return diagnostic


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
            "one public own-Actions certificate only")
    require(args.bits == 320 and not any(name in sys.modules for name in ("flint", "numpy", "scipy")),
            "complete readonly admission before numerical imports")
    root = Path(args.repo).resolve()
    manifest_raw = Path(args.manifest).read_bytes()
    require(0 < len(manifest_raw) < 100000
            and hashlib.sha256(manifest_raw).hexdigest() == args.manifest_sha,
            "whole frozen manifest identity")
    initial = json.loads(manifest_raw)
    specs = {item["role"]: item for item in initial["files"]}
    require(specs[ENTRY_ROLE]["path"] == SOURCE_PATH
            and Path(__file__).resolve() == (root / SOURCE_PATH).resolve(), "actual new owner path")
    raw_self = Path(__file__).read_bytes()
    require(len(raw_self) == specs[ENTRY_ROLE]["bytes"]
            and hashlib.sha256(raw_self).hexdigest() == specs[ENTRY_ROLE]["sha256"], "whole new owner bytes")
    core = import_pinned(root, specs["readonly_core"], "_R141_readonly_core")
    readonly = import_pinned(root, specs["readonly_admission"], "_R141_readonly")
    admitted = readonly.admit(root, args.manifest, args.manifest_sha, args.native,
        args.native_receipts, args.candidate_index, args.centre_repair,
        args.root_germ, args.root_budget, core)
    manifest = admitted["manifest"]
    operation = manifest["operation"]
    canonical, digest = core.canonical, core.digest
    prior_actual = json.loads(core.read_spec(root, specs[PRIOR_ACTUAL_ROLE]))
    prior_execution = json.loads(core.read_spec(root, specs[PRIOR_EXECUTION_ROLE]))
    prior = prior_success(prior_actual, prior_execution)
    centre_actual = json.loads(core.read_spec(root, specs[CENTRE_ACTUAL_ROLE]))
    centre_execution = json.loads(core.read_spec(root, specs[CENTRE_EXECUTION_ROLE]))
    require(centre_actual["kind"] == "W2C_complete_joint_centre_mean_floor_diagnostic_v1"
            and centre_actual["run_id"] == centre_execution["run_id"] == "44727185157"
            and centre_actual["run_attempt"] == centre_execution["run_attempt"] == "1"
            and centre_actual["complete"] is True and centre_execution["scientific_complete"] is True
            and centre_actual["actual_returncode"] == centre_execution["actual_child_returncode"] == 0
            and centre_actual["completed_targets"] == ["complete_joint_centre_mean_atom_necessary_floor"]
            and centre_actual["necessary_budget"]["fixed_recipe_rejection_proved"] is True
            and centre_actual["necessary_budget"]["complete_signed_centre_norm_squared_lower_bound_proved"] is True
            and centre_actual["necessary_budget"]["actual_operator_singularity_proved"] is False
            and centre_actual["actual_progress"]["centre_mean_panels_completed"] == 155
            and centre_actual["actual_progress"]["old_targets_recomputed"] == 0
            and centre_actual["actual_progress"]["original_low_family_three_records_computed"] == 0,
            "whole completed centre-floor result retained read only without any replay")
    admission_names = [item["name"] for item in admitted["admission"]["checks"]]
    require(len(admission_names) == 18
            and all(item["passed"] is True for item in admitted["admission"]["checks"]),
            "all complete original and collar admission checks")
    gates = admission_names + GATE_SUFFIX
    require(operation["scientific_entry_role"] == ENTRY_ROLE
            and operation["scientific_kind"] == KIND
            and operation["ordered_targets"] == TARGETS
            and operation["complete_target_counts"] == [2, 7]
            and operation["scientific_field_names"] == SCI_FIELDS
            and operation["complete_gate_names"] == gates
            and operation["certificate_parameters"] == CERTIFICATE_PARAMETERS
            and operation["fixed_runtime"] == RUNTIME,
            "whole distinct directed certificate contract")
    bound_sources = list(manifest["scientific_modules"]) + [
        specs[ENTRY_ROLE], specs[MATH_ROLE], specs[LOCAL_ROLE], specs[REFINED_ROLE]]
    require(operation["scientific_module_binding"] == bound_sources,
            "original seven definitions plus all four complete new sources")
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
            "admission": admitted["admission"], "new_targets": TARGETS,
            "same_complete_WVC_reference": admitted["paired_inputs"]["reference_chain"],
            "same_complete_selected_diagonal_chain": admitted["completed_tracefree_inputs"]["selected_diagonal_chain"],
            "certificate_parameters": CERTIFICATE_PARAMETERS,
            "complete_prior_successful_outcome_and_execution_admitted": True,
            "complete_prior_centre_mean_exclusion_and_execution_admitted": True,
            "prior_diagnostic_will_not_be_recomputed": True,
            "new_scientific_targets_evaluated": 0, "old_scientific_calls": 0,
            "numerical_libraries_imported": False}
        print(canonical(value).decode("utf-8"), end="", flush=True)
        return 0

    helper = import_pinned(root, specs["science"], "_R141_W2C_definition_helpers")
    output = Path(args.out)
    require(not output.exists(), "one new never-overwritten scientific outcome")
    output.parent.mkdir(parents=True, exist_ok=True)
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
        "certificate_parameters": copy.deepcopy(CERTIFICATE_PARAMETERS),
        "retained_scope": copy.deepcopy(operation["retained_scope"]),
        "copied_same_operator_records": copy.deepcopy(admitted["same_operator_records"]),
        "prior_complete_WVC_provider": {"kind": "whole_existing_public_object_reference_v1",
            "file": copy.deepcopy(specs["WVC_actual"]), "json_path": [],
            "all_original_fields_successes_false_gates_scopes_and_prefixes_admitted": True},
        "completed_prior_diagnostic": {"kind": "two_whole_existing_public_object_references_v1",
            "scientific": {"file": copy.deepcopy(specs[PRIOR_ACTUAL_ROLE]), "json_path": []},
            "execution": {"file": copy.deepcopy(specs[PRIOR_EXECUTION_ROLE]), "json_path": []},
            "all_prior_float_successes_retained_without_recomputation_or_upgrade": True},
        "completed_prior_centre_mean_floor": {"kind": "two_whole_existing_public_object_references_v1",
            "scientific": {"file": copy.deepcopy(specs[CENTRE_ACTUAL_ROLE]), "json_path": []},
            "execution": {"file": copy.deepcopy(specs[CENTRE_EXECUTION_ROLE]), "json_path": []},
            "whole_fixed_recipe_exclusion_retained_without_recomputing_any_bound": True,
            "actual_operator_singularity_not_inferred": True},
        "preparation_prefix": {"stage": "not_started", "detail": None},
        "reference_identity": None, "runtime": {}, "current_target": None,
        "completed_targets": [], "gates": [],
        "actual_progress": {"original_inputs_admitted": True,
            "reference_definitions_materialized": 0, "complete_centre_parents": 0,
            "original_closed_rows_covered": 0, "original_intersections": 0,
            "exact_comparison_panels_defined": 0, "whole_model_transfers_completed": 0,
            "complete_refined_cells": 0, "refined_left_carriers_completed": 0,
            "refined_right_carriers_completed": 0, "complete_reference_chart_nodes": 0,
            "current_source_role": None, "current_source_panels_completed": 0,
            "all_four_source_packet_cells_completed": 0,
            "whole_point_boxes_completed": 0, "new_targets_completed": 0,
            "old_completed_targets_recomputed": 0, "old_W2C_graphs_called": 0,
            "existing_W2C_owner_main_called": False,
            "existing_W2C_owner_used_for_definition_helpers_only": True,
            "prior_endpoint_QR_or_SVD_called": False,
            "old_completed_producer_entrypoints_called": 0, "new_arrays_published": 0},
        "certificate": {"model": None, "defect": None, "sources": {},
            "whole_interval_transversality": None, "strict_low_coefficient_gate_passed": None,
            "actual_low_hybrid_inverse_proved": False, "actual_complete_CFB_centre_proved": False,
            "actual_positive_family_inverse_proved": False, "original_finite_rho_bridge_proved": False,
            "original_seven_input_ports_proved": False, "either_original_RHS_proved": False,
            "topic_completion_proved": False, "declared_early_end": None},
        "automatic_retry_authorized": False, "actual_mathematical_wall_seconds": 0.0,
    }
    require(sorted(document) == SCI_FIELDS, "complete distinct output schema")
    math_start = None
    prepared = False
    packed_store = None

    def budget():
        require(sys.platform.startswith("linux"), "declared Linux public runner memory units")
        resident = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)*1024
        document["actual_progress"]["maximum_process_resident_bytes_observed"] = resident
        require(resident <= CERTIFICATE_PARAMETERS["maximum_scientific_process_resident_bytes"],
                "fixed complete scientific process resident-memory cap; prefix retained")
        if math_start is not None:
            require(time.perf_counter()-math_start <= CERTIFICATE_PARAMETERS["maximum_certificate_wall_seconds"],
                    "fixed complete certificate wall cap; prefix retained")

    def publish():
        if math_start is not None:
            elapsed = time.perf_counter()-math_start
            require(math.isfinite(elapsed) and elapsed >= 0, "finite mathematical elapsed time")
            document["actual_mathematical_wall_seconds"] = elapsed
        if packed_store is not None:
            document["certificate"]["private_directed_storage"] = packed_store.metadata()
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
            "completed_targets": document["completed_targets"], "whole_output_bytes": len(raw),
            "whole_output_sha256": digest(raw)}, sort_keys=True), flush=True)

    def gate(name):
        require(len(document["gates"]) < len(gates)
                and gates[len(document["gates"])] == name, "whole declared gate order")
        document["gates"].append({"name": name, "passed": True})
        publish()

    def start_target(name):
        budget()
        require(TARGETS[len(document["completed_targets"])] == name,
                "next exact new directed target")
        document["current_target"] = name
        document["stage"] = "starting:" + name
        publish()

    def finish_target():
        budget()
        require(document["current_target"] == TARGETS[len(document["completed_targets"])],
                "whole target completion order")
        document["completed_targets"].append(document["current_target"])
        document["current_target"] = None
        document["actual_progress"]["new_targets_completed"] = len(document["completed_targets"])
        document["stage"] = "complete_new_target"
        publish()

    def progress(stage, detail):
        budget()
        require(isinstance(stage, str) and isinstance(detail, dict)
                and len(canonical({"stage": stage, "detail": detail})) <= 2500,
                "bounded progress metadata without arrays")
        if not prepared:
            document["preparation_prefix"] = {"stage": stage, "detail": copy.deepcopy(detail)}
        if stage == "same_exact_reference_definition":
            document["actual_progress"]["reference_definitions_materialized"] = detail["parents_verified"]
        elif stage == "complete_new_centre_parent":
            document["actual_progress"]["complete_centre_parents"] = detail["parents_complete"]
            document["actual_progress"]["original_closed_rows_covered"] = detail["closed_rows_covered"]
            document["actual_progress"]["original_intersections"] = detail["closed_intersections"]
        elif stage == "verified_comparison_transfer":
            document["actual_progress"]["whole_model_transfers_completed"] = detail["panels_complete"]
        elif stage == "refined_reference_chart_proposals":
            document["actual_progress"]["complete_reference_chart_nodes"] = detail["nodes_complete"]
        elif stage == "refined_complete_left_carrier_parent":
            document["actual_progress"]["refined_left_carriers_completed"] = detail["cells_complete"]
        elif stage == "refined_complete_right_carrier_parent":
            document["actual_progress"]["refined_right_carriers_completed"] = detail["cells_complete"]
        document["stage"] = "working:" + stage
        publish()

    def scalar(value):
        require(value.is_finite(), "finite complete directed scalar")
        midpoint, radius, exponent = value.mid_rad_10exp(CERTIFICATE_PARAMETERS["scalar_decimal_enclosure_digits"])
        require(int(radius) >= 0, "nonnegative enclosing decimal radius")
        return {"kind": "complete_decimal_ball_v1", "midpoint_integer": str(int(midpoint)),
                "radius_integer": str(int(radius)), "decimal_exponent": str(int(exponent)),
                "semantics": "the exact directed scalar lies in (midpoint +/- radius)*10^exponent"}

    def saved_scalar_ball(record):
        require(record["kind"] == "complete_decimal_ball_v1", "one complete saved scalar enclosure")
        exponent = int(record["decimal_exponent"])
        scale = api.rational(10**exponent) if exponent >= 0 else api.rational(1, 10**(-exponent))
        midpoint = api.rational(int(record["midpoint_integer"]))*scale
        radius = api.rational(int(record["radius_integer"]))*scale
        return api.interval(midpoint-radius, midpoint+radius)

    def norm_summary(value):
        keys = ("body_HS2_upper", "root97_HS2_upper", "outer96_HS2_upper",
                "body_norm_upper", "atoms193_norm_upper", "complete_norm_upper")
        return {"source_role": value["source_role"], "complete_original_panels": 155,
                "complete_refined_cells": value["complete_refined_cells"],
                "complete_output_atoms": 193, **{key: scalar(value[key]) for key in keys}}

    def actual_summary(value):
        return {key: (scalar(item) if hasattr(item, "is_finite") else item)
                for key, item in value.items()}

    publish()
    try:
        for name in admission_names:
            gate(name)
        import flint
        require(platform.python_version() == RUNTIME["Python"]
                and flint.__version__ == RUNTIME["python_flint"], "fixed published directed runtime")
        require(not any(name in sys.modules for name in ("numpy", "scipy")),
                "no replay of a floating propagation dependency")
        require(all(os.environ.get(name) == "1" for name in
                    ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")),
                "declared single-thread external math environment")
        flint.ctx.prec = RUNTIME["admission_and_model_definition_bits"]
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
        collar = import_pinned(root, specs["collar_math"], "_R141_collar_math")
        km = import_pinned(root, specs["kernel_math"], "_R141_kernel_math")
        assembly = import_pinned(root, specs["assembly_math"], "_R141_assembly_math")
        reference = import_pinned(root, specs["reference_math"], "_R141_reference_math")
        green = import_pinned(root, specs[MATH_ROLE], "_R141_Green_math")
        local = import_pinned(root, specs[LOCAL_ROLE], "_R141_local_math")
        refined = import_pinned(root, specs[REFINED_ROLE], "_R141_refined_math")
        math_start = time.perf_counter()
        context = assembly.prepare_complete_kernel_context(api, km, reference, collar, admitted,
            completed["complete_original_candidate"], old, core.signed_display_centre, progress)
        require(context.reference_identity["original_reference_chain"] ==
                    completed["complete_original_candidate"]["reference_chain"]
                and context.reference_identity["selected_diagonal_chain"] == completed["selected_diagonal_chain"]
                and len(context.domain.cells) == 155 and context.parent_definition_count == 153
                and context.original_body_row_count == 4650 and context.original_intersection_count == 4801,
                "same complete original WVC reference and all coefficient coverage")
        document["reference_identity"] = copy.deepcopy(context.reference_identity)
        prepared = True
        generators = []
        chain = hashlib.sha256(b"fixed_WVC_low193_midpoint_comparison_v1").hexdigest()
        rows_plan = prior["complete_plan"]["rows"]
        for panel in range(155):
            budget()
            whole = context.centre_matrix(green.HEAD, green.HEAD, context.domain.whole_cell_box(panel))
            require(whole.shape == (193, 193), "entire raw low193 model definition")
            h_float = float(context.domain.full_length(panel).mid())
            require(math.isfinite(h_float) and h_float > 0
                    and rows_plan[panel][1] == context.parent_indices[panel]
                    and h_float.hex() == rows_plan[panel][2].hex(), "same whole prior raw model length")
            hn, hd = h_float.as_integer_ratio()
            h_mid = api.rational(hn, hd)
            values, payload = [], bytearray()
            for row in whole.values:
                mids = [float(value.mid()) for value in row]
                require(all(math.isfinite(value) for value in mids), "finite whole prior raw model row")
                payload.extend(struct.pack("<193d", *mids))
                dyadic_row = []
                for value in mids:
                    numerator, denominator = value.as_integer_ratio()
                    exact = h_mid*api.rational(numerator, denominator)
                    require(exact.lower() == exact.upper(), "exact dyadic normalized generator entry")
                    dyadic_row.append(exact)
                values.append(dyadic_row)
            chain = hashlib.sha256(bytes.fromhex(chain)+panel.to_bytes(4, "big")
                                   +h_float.hex().encode("ascii")+payload).hexdigest()
            generators.append(km.Matrix(193, 193, values))
            document["actual_progress"]["exact_comparison_panels_defined"] = panel+1
            progress("R141_complete_exact_model_panel", {"panels_complete": panel+1,
                "panels": 155, "prior_endpoint_target_recomputed": False})
        require(chain == prior["comparison_matrix_sha256_chain"], "same complete successful prior raw model chain")
        gate(GATE_SUFFIX[2])
        flint.ctx.prec = RUNTIME["directed_certificate_bits"]
        start_target(TARGETS[0])
        plan = refined.refined_plan(api, km, green, context, generators, rows_plan)
        cell_count = plan["complete_refined_cells"]
        require(plan["original_completed_substeps"] == 1424
                and cell_count <= CERTIFICATE_PARAMETERS["maximum_refined_cells"]
                and refined.INTEGRATION_SUBBOXES == CERTIFICATE_PARAMETERS["integration_boxes_per_refined_cell"]
                and refined.LOCAL_TAYLOR_ORDER == CERTIFICATE_PARAMETERS["local_shared_scalar_Taylor_order"]
                and refined.MAX_PACKED_BYTES == CERTIFICATE_PARAMETERS["maximum_private_packed_payload_bytes"]
                and refined.MAX_DECODED_ENTRIES == CERTIFICATE_PARAMETERS["maximum_decoded_matrix_entries"],
                "complete exact refinement and declared memory/local-factor plan")
        document["actual_progress"]["complete_refined_cells"] = cell_count
        document["certificate"]["refinement"] = {
            "original_panels": 155, "prior_complete_substeps": 1424,
            "complete_refined_cells": cell_count,
            "complete_integration_boxes": cell_count*refined.INTEGRATION_SUBBOXES,
            "counts": list(plan["counts"]),
            "doubled_original_panels": list(plan["doubled_original_panels"]),
            "maximum_directed_balanced_span_upper": scalar(green.maximum_upper(api, plan["spans"])),
            "same_exact_raw_midpoint_model": True, "all_prior_cuts_retained": True,
            "true_parent_tau_map_and_lengths_retained": True,
            "actual_coefficient_balls_narrowed_by_cuts": False}
        refined_context = refined.RefinedContext(context, plan["counts"])
        charts = refined.prepare_chart_specs(api, context, refined_context, progress)
        packed_store = refined.PackedMatrices(api, km)
        model = refined.build_refined_model(api, km, green, context, generators,
                                            plan, charts, packed_store, progress)
        del charts, refined_context
        backend = refined.make_factor_provider(api, km, green, local, model)
        cuts = [backend.cuts(panel) for panel in range(cell_count)]
        require(sum(len(v)-1 for v in cuts) == cell_count*refined.INTEGRATION_SUBBOXES,
                "all whole refined integration boxes")
        document["certificate"]["model"] = {
            "comparison_BVP_verified": model["comparison_BVP_verified"],
            "true_coefficient_inverse_claimed_by_this_target": False,
            "complete_raw_model_chain": chain, "original_panels": 155,
            "refined_cells": cell_count, "boundary_charts": cell_count+1,
            "left_carrier": 97, "right_carrier": 96, "whole_atoms": 193,
            "same_true_panel_lengths_retained": True,
            "prior_endpoint_QR_and_SVD_recomputed": False,
            "refined_storage_contract": refined.contract_metadata(),
            "local_factor_backend_contract": {
                "kind": "R141_signed_shared_scalar_Taylor_and_entrywise_positive_tail_v1",
                "complete_source_role_requested_on_every_true_box": True,
                "full_same_panel_two_triangles_retained": True}}
        finish_target()

        def make_packets(role):
            document["actual_progress"]["current_source_role"] = role
            document["actual_progress"]["current_source_panels_completed"] = 0
            packets = refined.PackedPackets(packed_store, model, role)
            for panel in range(cell_count):
                budget()
                packets.append(local.panel_gram_packet(backend, panel, cuts[panel], role))
                document["actual_progress"]["current_source_panels_completed"] = panel+1
                if panel % 8 == 7 or panel+1 == cell_count:
                    progress("R141_complete_source_refined_cell", {"source_role": role,
                        "cells_complete": panel+1, "cells": cell_count})
            return packets

        start_target(TARGETS[1])
        defect_packets = make_packets("true_coefficient_defect")
        defect = refined.complete_gram_norm_packed(api, km, green, model, defect_packets,
                                                   ("norm", "defect"), progress)
        document["certificate"]["defect"] = norm_summary(defect)
        # The sufficient gate is tested on the upper endpoint of the whole
        # published decimal ball, not on a hidden more favorable number.
        epsilon = saved_scalar_ball(document["certificate"]["defect"]["body_norm_upper"]).upper()
        require(bool(epsilon >= defect["body_norm_upper"]), "saved complete body upper retains original enclosure")
        defect["body_norm_upper"] = epsilon
        passed = bool(epsilon < api.one)
        document["certificate"]["defect"]["strict_gate_uses_saved_decimal_upper"] = True
        document["certificate"]["strict_low_coefficient_gate_passed"] = passed
        finish_target()
        if not passed:
            document["certificate"]["declared_early_end"] = {
                "reason": "complete directed sufficient defect upper is not strictly below1",
                "actual_singularity_inferred": False,
                "completed_complete_bounds_retained": True,
                "ordinary_source_atom_and_point_certificate_not_claimed": True}
        else:
            document["certificate"]["actual_low_hybrid_inverse_proved"] = True
            start_target(TARGETS[2])
            source_packets = {role: refined.PackedPackets(packed_store, model, role)
                              for role in SOURCE_ROLES}
            for panel in range(cell_count):
                budget()
                for role in SOURCE_ROLES:
                    document["actual_progress"]["current_source_role"] = role
                    source_packets[role].append(local.panel_gram_packet(backend,
                        panel, cuts[panel], role))
                document["actual_progress"]["all_four_source_packet_cells_completed"] = panel+1
                if panel % 8 == 7 or panel+1 == cell_count:
                    progress("R141_all_four_source_packets_refined_cell", {
                        "cells_complete": panel+1, "cells": cell_count,
                        "complete_source_roles": len(SOURCE_ROLES)})
            for position, role in enumerate(SOURCE_ROLES):
                if position:
                    start_target(TARGETS[position+2])
                packets = source_packets.pop(role)
                norm = refined.complete_gram_norm_packed(api, km, green, model, packets,
                                                         ("norm", role), progress)
                result = green.actual_low_source_bound(api, defect, norm)
                require(result["actual_low_BVP_proved"] is True,
                        "strict same-model actual low source lift")
                document["certificate"]["sources"][role] = {
                    "comparison": norm_summary(norm), "actual": actual_summary(result)}
                packed_store.release(norm["private_storage_prefix"])
                packets.release()
                del packets, norm
                finish_target()
            start_target(TARGETS[6])
            covariance = refined.source_covariances_packed(api, km, green, model,
                                                            defect_packets, progress)
            max_weighted = max_raw = api.zero
            min_angle = None
            witness = None
            for panel in range(cell_count):
                for left, right in zip(cuts[panel][:-1], cuts[panel][1:]):
                    budget()
                    box = (panel, left, right)
                    result = local.whole_box_projection_bound(backend, panel, box,
                        defect_packets, covariance, defect, epsilon)
                    weighted = result["actual_weighted_oblique_projection_upper"]
                    raw = result["actual_raw_oblique_projection_upper"]
                    angle = result["actual_raw_orthonormal_matching_singular_lower"]
                    max_weighted = green.maximum_upper(api, [max_weighted, weighted])
                    max_raw = green.maximum_upper(api, [max_raw, raw])
                    if min_angle is None or bool(angle < min_angle):
                        min_angle = angle
                        witness = {"panel": panel, "left": str(left), "right": str(right)}
                    document["actual_progress"]["whole_point_boxes_completed"] += 1
                if panel % 8 == 7 or panel+1 == cell_count:
                    progress("R141_complete_point_refined_cell", {"cells_complete": panel+1,
                        "cells": cell_count,
                        "whole_boxes_complete": document["actual_progress"]["whole_point_boxes_completed"]})
            require(document["actual_progress"]["whole_point_boxes_completed"] == cell_count*refined.INTEGRATION_SUBBOXES
                    and min_angle is not None and api.lower(min_angle) > 0,
                    "all whole point boxes and strictly positive true matching lower")
            document["certificate"]["whole_interval_transversality"] = {
                "every_real_radius_covered": True,
                "complete_box_count": cell_count*refined.INTEGRATION_SUBBOXES,
                "actual_weighted_projection_upper": scalar(max_weighted),
                "actual_raw_projection_upper": scalar(max_raw),
                "actual_raw_orthonormal_matching_singular_lower": scalar(min_angle),
                "minimum_enclosure_witness_box": witness,
                "raw_nodes_only_diagnostic_used_as_certificate": False,
                "full_CFB_included": False}
            finish_target()
            document["proved"] = True
        document["certificate"]["local_factor_actual_statistics"] = copy.deepcopy(backend.private_statistics)
        backend.release()
        gate(GATE_SUFFIX[3])
        require(Path(args.manifest).read_bytes() == manifest_raw, "frozen manifest unchanged")
        for spec in manifest["files"]:
            core.read_spec(root, spec)
        gate(GATE_SUFFIX[4])
        require(len(document["completed_targets"]) == (7 if passed else 2)
                and document["certificate"]["actual_complete_CFB_centre_proved"] is False
                and document["certificate"]["actual_positive_family_inverse_proved"] is False
                and document["certificate"]["original_finite_rho_bridge_proved"] is False
                and document["certificate"]["original_seven_input_ports_proved"] is False
                and document["certificate"]["either_original_RHS_proved"] is False,
                "whole declared branch and complete unpaid obligations")
        document["actual_returncode"] = 0
        document["complete"] = True
        document["stage"] = "complete_low193_directed_certificate" if passed else "complete_directed_low_gate_not_passed"
        gate(GATE_SUFFIX[5])
        require(sorted(document) == SCI_FIELDS, "complete distinct result schema")
        return 0
    except BaseException as error:
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
