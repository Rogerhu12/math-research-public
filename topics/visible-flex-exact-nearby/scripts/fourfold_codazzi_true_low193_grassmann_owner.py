"""Certify the full original low193 problem with joint rational Householder charts."""
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
SOURCE_PATH = TOPIC+"scripts/fourfold_codazzi_true_low193_grassmann_owner.py"
KIND = "complete_R149_true_low193_joint_grassmann_and_source_maps_v1"
PREFLIGHT_KIND = "complete_R149_true_low193_grassmann_preflight_v1"
ENTRY_ROLE = "true_low193_grassmann_owner"
FLOW_ROLE = "true_low193_direct_flow_math"
CHILD_ROLE = "true_low193_whole_child_coefficients"
GREEN_ROLE = "low_centre_verified_green_math"
REFINED_ROLE = "low_centre_refined_green_math"
SL_ACTUAL_ROLE = "completed_signed_loop_actual_readonly"
SL_EXECUTION_ROLE = "completed_signed_loop_execution_readonly"
PRIOR_ACTUAL_ROLE = "completed_low193_balanced_endpoint_actual"
PRIOR_EXECUTION_ROLE = "completed_low193_balanced_endpoint_execution"
SOURCE_ROLES = ["ordinary_raw_low_source", "transformed_low_source",
                "low_second_kind_correction", "centre_high0_return_source"]
TARGETS = ["complete_true_low193_joint_Grassmann_inverse",
           "complete_true_low193_joint_four_whole_source_maps"]
EXPLICIT = ["true_low193_grassmann_owner","low_centre_verified_green_math",
            "low_centre_refined_green_math","true_low193_whole_child_coefficients",
            "true_low193_direct_flow_math","original81_restore","grassmann_math",
            "grassmann_carriers","grassmann_runner","grassmann_validator"]
RUNTIME = {"Python": "3.12.14", "python_flint": "0.9.0",
           "admission_and_model_definition_bits": 320,
           "directed_certificate_bits": 384, "BLAS_threads": 1, "numpy_proposal_only": "2.3.5"}
CERTIFICATE_PARAMETERS = {
    "actual_operator": "original WVC hybrid ALc, complete actual family eta and repaired lower coefficients",
    "all193_original_coordinates_and_independent_mean": True,
    "all193_original_observations": True,
    "ordinary_dr_and_true_root_lengths": True,
    "original_parents": 155, "original_body_rows": 4650, "repair_coordinates": 65,
    "complete_refined_cells": 1424,
    "initial_subboxes_per_new_cell": 4, "largest_new_cut_denominator": 64, "old_81_order": 24, "post81_order": 16,
    "unchanged_original_TF_checkpoint_failed_cuts": 64, "workers": 4,
    "successful_prefix_cells_recomputed_on_local_refinement": 0,
    "flow_method": "signed varying-coefficient Peano-Baker with complete factorial tail",
    "prefix_method": "all u in [0,1] in each Peano term, complete same tail",
    "local_matrix_exponential_used_as_variable_flow": False,
    "coefficient_provider": "genuine whole-child intersection before matrix hull",
    "intrinsic_or_independent_mean_ball_divided_by_subdivision": False,
    "physical_S_replaced_by_internal_balance": False,
    "left_pivot_dimension": 97, "right_pivot_dimension": 96,
    "node_pivot_dimension": 96, "whole_finite_pivot_count": 4273,
    "outer_impedance": "13/80",
    "source_maps": ["ordinary_raw_low_source", "transformed_low_source",
                    "low_second_kind_correction", "centre_high0_return_source"],
    "source_columns": [193, 193, 193, 128],
    "source_covariance_method": "five whole raw193 moments; signed finite97/96 recurrence",
    "same_cell_triangles": "each complete positive triangle bounded by its whole branch square",
    "actual_full_CFB_or_finite_high_Schur_computed": False,
    "original_seven_ports_or_nonlinear_RHS_computed": False,
    "old_comparison_HS_trace_QR_or_producer_targets_called": False,
    "prior_SL_run": "45917913526/1", "prior_SL_false_gate_retained": True,
    "prior_midpoint_model_chain_readonly": "33fdf6eeba4d5904c961b2bedea43c5207d80fb66920017168f41f9106cc4d79",
    "scalar_decimal_enclosure_digits": 48,
    "maximum_private_packed_payload_bytes": 8589934592,
    "maximum_decoded_matrix_entries": 200000,
    "maximum_scientific_process_resident_bytes": 15032385536,
    "maximum_certificate_wall_seconds": 19500,
    "automatic_retries": 0,
}
GATE_SUFFIX = ["fixed_new_directed_runtime_verified",
    "same29_saved_records_and_true_WVC_context_verified",
    "complete_original1424_cuts_and_trial_chart_definition_retained",
    "all_joint_graph_inclusions_and_true_inverse_saved",
    "complete_true_source_maps_saved",
    "all_current_inputs_reverified_and_full_unpaid_scope_retained"]
SCI_FIELDS = ["actual_checkout_commit", "actual_mathematical_wall_seconds", "actual_progress",
    "actual_returncode", "automatic_retry_authorized", "certificate", "certificate_parameters",
    "complete", "complete_current_file_receipts", "complete_restoration_receipts",
    "completed_targets", "copied_same_operator_records", "current_target", "failure", "gates",
    "input_ball_identities", "kind", "manifest_sha256", "original_admission", "parameters",
    "preparation_prefix", "prior_completed_signed_loop", "problem_id", "proved",
    "reference_identity", "retained_scope", "run_attempt", "run_id", "runtime",
    "scientific_modules", "stage", "workflow_event_commit"]


def require(ok, message):
    if not ok:
        raise ValueError(message)


def import_pinned(root, spec, name):
    path = (root/spec["path"]).resolve()
    require(path.is_relative_to(root) and path.is_file(), "whole source path")
    raw = path.read_bytes()
    require(len(raw) == spec["bytes"] and hashlib.sha256(raw).hexdigest() == spec["sha256"]
        and hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest() == spec["git_blob_sha"],
        "complete bound source: "+spec["role"])
    loader = importlib.util.spec_from_file_location(name, path)
    require(loader is not None and loader.loader is not None, "complete source loader")
    module = importlib.util.module_from_spec(loader)
    loader.loader.exec_module(module)
    return module


def read_prior_plan(prior, execution, signed, signed_execution):
    require(prior["run_id"] == execution["run_id"] == "44721851908"
        and prior["run_attempt"] == execution["run_attempt"] == "1"
        and prior["complete"] is True and prior["proved"] is False
        and execution["scientific_complete"] is True
        and prior["actual_returncode"] == execution["actual_child_returncode"] == 0,
        "original successful FLOAT plan retained without certification upgrade")
    diagnostic = prior["diagnostic"]
    require(diagnostic["comparison_matrix_sha256_chain"] ==
        CERTIFICATE_PARAMETERS["prior_midpoint_model_chain_readonly"]
        and all(value is False for value in diagnostic["certification"].values()),
        "same original whole finite proposal only")
    require(signed["kind"] == "complete_R149_low193_signed_loop_coercivity_v1"
        and signed["run_id"] == signed_execution["run_id"] == "45917913526"
        and signed["run_attempt"] == signed_execution["run_attempt"] == "1"
        and signed["complete"] is True and signed["proved"] is False
        and signed_execution["scientific_complete"] is True
        and signed["actual_returncode"] == signed_execution["actual_child_returncode"] == 0
        and signed["completed_targets"] == signed_execution["completed_target_names"]
            == ["complete_same_weighted_body_signed_trace_and_symmetric_part"]
        and signed_execution["completed_old_targets_recomputed"] == 0,
        "whole actual completed SL false branch and its execution")
    certificate = signed["certificate"]
    require(certificate["strict_low_coefficient_gate_passed"] is False
        and certificate["strict_symmetric_part_gate_passed"] is False
        and certificate["actual_low_hybrid_inverse_proved"] is False,
        "both previous false sufficient gates remain false")
    rows = diagnostic["complete_plan"]["rows"]
    counts = certificate["refinement"]["counts"]
    require(len(rows) == len(counts) == 155 and sum(counts) == 1424
        and all(row[0] == i and type(row[6]) is int and row[6] == counts[i] > 0
                for i, row in enumerate(rows)), "all original exact1424 cuts retained")
    return rows, counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("repo", "manifest", "manifest-sha", "out", "native", "native-receipts",
                 "candidate-index", "centre-repair", "root-germ", "root-budget"):
        parser.add_argument("--"+name, required=True)
    parser.add_argument("--bits", type=int, required=True)
    parser.add_argument("--preflight-only", action="store_true")
    args = parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public",
        "own public Actions only")
    require(args.bits == 320 and not any(x in sys.modules for x in ("flint", "numpy", "scipy")),
        "complete readonly admission before any numerical import")
    root = Path(args.repo).resolve()
    manifest_raw = Path(args.manifest).read_bytes()
    require(0 < len(manifest_raw) < 100000 and hashlib.sha256(manifest_raw).hexdigest() == args.manifest_sha,
        "whole fixed new manifest")
    initial = json.loads(manifest_raw)
    specs = {v["role"]: v for v in initial["files"]}
    require(specs[ENTRY_ROLE]["path"] == SOURCE_PATH
        and Path(__file__).resolve() == root/SOURCE_PATH,
        "actual new owner source path")
    core = import_pinned(root, specs["readonly_core"], "_TF_readonly_core")
    readonly = import_pinned(root, specs["readonly_admission"], "_TF_readonly")
    admitted = readonly.admit(root, args.manifest, args.manifest_sha, args.native,
        args.native_receipts, args.candidate_index, args.centre_repair, args.root_germ, args.root_budget, core)
    manifest, canonical, digest = admitted["manifest"], core.canonical, core.digest
    operation = manifest["operation"]
    prior = json.loads(core.read_spec(root, specs[PRIOR_ACTUAL_ROLE]))
    prior_execution = json.loads(core.read_spec(root, specs[PRIOR_EXECUTION_ROLE]))
    signed = json.loads(core.read_spec(root, specs[SL_ACTUAL_ROLE]))
    signed_execution = json.loads(core.read_spec(root, specs[SL_EXECUTION_ROLE]))
    rows_plan, counts = read_prior_plan(prior, prior_execution, signed, signed_execution)
    admission_names = [v["name"] for v in admitted["admission"]["checks"]]
    require(len(admission_names) == 18 and all(v["passed"] is True for v in admitted["admission"]["checks"]),
        "all original18 admission checks retained")
    gates = admission_names+GATE_SUFFIX
    restore = import_pinned(root, specs["original81_restore"], "_GG_original81_restore")
    original = restore.admit_complete_original(*(core.read_spec(root, specs[k]) for k in
        ("original_TF_failure_actual","original_TF_failure_execution","original_TF_manifest")))
    validator = import_pinned(root, specs["grassmann_validator"], "_GG_validator")
    bound_sources = manifest["scientific_modules"]+[specs[role] for role in EXPLICIT]
    require(operation["scientific_entry_role"] == ENTRY_ROLE and operation["scientific_kind"] == KIND
        and operation["ordered_targets"] == TARGETS and operation["complete_target_counts"] == [2]
        and operation["scientific_field_names"] == SCI_FIELDS
        and operation["complete_gate_names"] == gates
        and operation["certificate_parameters"] == CERTIFICATE_PARAMETERS
        and operation["fixed_runtime"] == RUNTIME
        and operation["scientific_module_binding"] == bound_sources,
        "complete new target contract, preserving original source closure")
    run, attempt, event, checkout = (os.environ.get(name, "") for name in
        ("GITHUB_RUN_ID", "GITHUB_RUN_ATTEMPT", "GITHUB_SHA", "ACTUAL_CHECKOUT_COMMIT"))
    require(re.fullmatch(r"\d{1,20}", run) and re.fullmatch(r"\d{1,10}", attempt)
        and re.fullmatch(r"[0-9a-f]{40}", event) and re.fullmatch(r"[0-9a-f]{40}", checkout),
        "actual public run and checkout identity")
    input_ids = {"complete_candidate_metadata_sha256": digest(canonical(admitted["candidate_metadata"])),
        "complete_repair_definition_sha256": digest(canonical(admitted["repair_definition"])),
        "complete_same29_operator_records_sha256": digest(canonical(admitted["same_operator_records"])),
        "whole_body_row_count": len(admitted["rows"]), "whole_repair_coordinates": len(admitted["repair_suprema"]),
        "same_true_root_and_actual_full_family_eta": True,
        "original_WVC_file": copy.deepcopy(specs["WVC_actual"])}
    require(input_ids["complete_repair_definition_sha256"] ==
        "440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47",
        "unchanged full Qrepair definition")
    if args.preflight_only:
        require(not any(x in sys.modules for x in ("flint", "numpy", "scipy")), "readonly only")
        print(canonical({"kind": PREFLIGHT_KIND, "complete": True, "preflight_only": True,
            "problem_id": readonly.PROBLEM_ID, "manifest_sha256": args.manifest_sha,
            "admission": admitted["admission"], "input_ball_identities": input_ids,
            "new_targets": TARGETS, "complete_refined_cells": sum(counts),
            "old_complete_SL_false_branch_retained": True,
            "old_HS_trace_QR_or_producer_calls": 0,
            "new_scientific_targets_evaluated": 0}).decode("utf-8"), end="", flush=True)
        return 0

    helper = import_pinned(root, specs["science"], "_TF_definition_helpers")
    output = Path(args.out)
    require(not output.exists(), "one new actual outcome")
    output.parent.mkdir(parents=True, exist_ok=True)
    document = {"kind": KIND, "problem_id": readonly.PROBLEM_ID, "complete": False, "proved": False,
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
        "input_ball_identities": input_ids,
        "prior_completed_signed_loop": {"scientific": copy.deepcopy(specs[SL_ACTUAL_ROLE]),
            "execution": copy.deepcopy(specs[SL_EXECUTION_ROLE]), "run": "45917913526/1",
            "strict_low_coefficient_gate_passed": False, "strict_symmetric_part_gate_passed": False,
            "old_HS_trace_and_all_old_completed_targets_recomputed": 0},
        "preparation_prefix": {"stage": "not_started", "detail": None},
        "reference_identity": None, "runtime": {}, "current_target": None,
        "completed_targets": [], "gates": [], "automatic_retry_authorized": False,
        "actual_mathematical_wall_seconds": 0.0,
        "actual_progress": {"new_targets_completed": 0, "old_completed_targets_recomputed": 0,
            "actual_left_cells_complete": 0, "actual_right_cells_complete": 0,
            "actual_source_cells_complete": 0, "new_arrays_published": 0,
            "local_current_cell_refinements": [],
            "old_comparison_Green_HS_trace_QR_or_producer_calls": 0},
        "certificate": {"complete_packet_prefix":{"restored":0,"post81":0,"maximum_index":-1,
            "receipt_chain_sha256":hashlib.sha256(b"GG-received-packets").hexdigest()},
            "actual_low_hybrid_inverse_proved": False,
            "actual_full_positive_inverse_proved": False, "actual_complete_CFB_centre_proved": False,
            "original_finite_rho_bridge_proved": False, "original_seven_ports_proved": False,
            "either_original_nonlinear_RHS_proved": False, "topic_completion_proved": False,
            "refinement": {"counts": list(counts), "complete_refined_cells": sum(counts),
                "all_original_cuts_retained": True, "true_root_lengths_retained": True},
            "joint_inclusions": {"left": [], "right": [], "nodes": [],
                "power_semantics": "graph pairs [a,b] certify gap>=2^a and radius<=2^b; node e certifies inverse<=2^e",
                "order": "left ascending0; right descending1423; nodes descending1424",
                "whole_ordered_record_chain_sha256": hashlib.sha256(b"R149-GG-v1").hexdigest()},
            "true_model": None, "sources": {}, "restored_original81": None}}
    require(sorted(document) == SCI_FIELDS, "one complete output schema")
    math_start, last_publish = None, 0.0

    def budget():
        if math_start is not None:
            require(time.monotonic()-math_start <= CERTIFICATE_PARAMETERS["maximum_certificate_wall_seconds"],
                    "whole scientific wall limit")

    def publish(verbose=True):
        nonlocal last_publish
        if math_start is not None:
            document["actual_mathematical_wall_seconds"] = time.monotonic()-math_start
        public_certificate = dict(document["certificate"])
        public_certificate["joint_inclusions"] = validator.pack_powers(public_certificate["joint_inclusions"])
        published = {**document,"certificate":public_certificate}
        if document["complete"]:
            validator.validate(published, operation, signed["reference_identity"])
        raw = canonical(published)
        require(0 < len(raw) <= operation["maximum_scientific_bytes"] < 100000,
            "one whole small actual result; no array publication")
        temporary = output.with_name(output.name+".tmp")
        with temporary.open("wb") as stream:
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())
        temporary.replace(output)
        last_publish = time.perf_counter()
        if verbose:
            print(json.dumps({"stage": document["stage"], "current_target": document["current_target"],
                "completed_targets": document["completed_targets"], "whole_output_bytes": len(raw),
                "whole_output_sha256": digest(raw)}, sort_keys=True), flush=True)

    def gate(name):
        require(gates[len(document["gates"])] == name, "complete gate order")
        document["gates"].append({"name": name, "passed": True})
        publish()

    def start_target(name):
        budget()
        require(TARGETS[len(document["completed_targets"])] == name, "next new target only")
        document["current_target"] = name
        document["stage"] = "starting:"+name
        publish()

    def finish_target():
        # A completed actual mathematical target is durably recorded before
        # any subsequent budget check or final housekeeping can fail.
        name = document["current_target"]
        require(name == TARGETS[len(document["completed_targets"])], "complete next target")
        document["completed_targets"].append(name)
        document["actual_progress"]["new_targets_completed"] = len(document["completed_targets"])
        document["current_target"] = None
        document["stage"] = "completed:"+name
        publish()

    def progress(stage, detail):
        document["stage"] = "working:"+stage
        detail = dict(detail)
        ledger = document["certificate"]["joint_inclusions"]
        if stage == "complete_private_packet":
            packet_status = document["certificate"]["complete_packet_prefix"]
            packet_status["restored" if detail["panel"] < 81 else "post81"] += 1
            packet_status["maximum_index"] = max(packet_status["maximum_index"], detail["panel"])
            packet_status["receipt_chain_sha256"] = digest(
                bytes.fromhex(packet_status["receipt_chain_sha256"])+canonical(detail))
        if stage == "whole_original81_matched":
            document["certificate"]["restored_original81"] = detail
            publish()
        if stage.startswith("new_joint_"):
            activity = document["actual_progress"]
            if "complete_record" in detail:
                record = detail["complete_record"]
                side = "left" if stage == "new_joint_left_graph" else "right"
                expected = len(ledger[side]) if side == "left" else 1423-len(ledger[side])
                require(detail["index"] == expected, "whole ordered graph cell")
                gap = record["complete_denominator_lower"]
                radius = record["complete_graph_radius_upper"]
                ledger[side].append([-inverse_power(api.one/gap), inverse_power(radius)
                                     if radius.upper() > 0 else 0])
                activity["actual_"+side+"_cells_complete"] = detail["complete_cells"]
            if "transversality_inverse_upper" in detail:
                require(detail["index"] == 1424-len(ledger["nodes"]), "whole ordered node")
                ledger["nodes"].append(inverse_power(detail["transversality_inverse_upper"]))
            if stage == "new_joint_four_complete_source_covariances":
                activity["actual_source_cells_complete"] = detail["complete_cells"]
            ledger["whole_ordered_record_chain_sha256"] = digest(
                bytes.fromhex(ledger["whole_ordered_record_chain_sha256"])+canonical([stage,public(detail)]))
        document["preparation_prefix"] = {"stage": stage,"detail": public(detail)}
        if stage.startswith("new_joint_") or stage == "complete_private_packet":
            publish(False)
        elif time.perf_counter()-last_publish >= 30:
            publish()
        if stage != "complete_private_packet":
            budget()

    def scalar(value):
        require(value.is_finite(), "whole finite scalar")
        mid, rad, exponent = value.mid_rad_10exp(CERTIFICATE_PARAMETERS["scalar_decimal_enclosure_digits"])
        return {"kind": "complete_decimal_ball_v1", "midpoint_integer": str(int(mid)),
            "radius_integer": str(int(rad)), "decimal_exponent": str(int(exponent)),
            "semantics": "the exact directed scalar lies in (midpoint +/- radius)*10^exponent"}

    def public(value):
        if hasattr(value, "mid_rad_10exp"):
            return scalar(value)
        if isinstance(value, dict):
            return {k: public(v) for k, v in value.items() if k != "private_model_token"}
        if isinstance(value, (tuple, list)):
            return [public(v) for v in value]
        require(value is None or isinstance(value, (str, int, float, bool)), "small complete public type")
        return value

    def inverse_power(value):
        require(value.is_finite() and api.lower(value) > 0, "positive complete inverse norm")
        estimate = float(value.log()/api.rational(2).log())
        require(math.isfinite(estimate), "finite binary exponent proposal")
        exponent = math.ceil(estimate)+1
        while not bool(api.rational(2)**exponent >= value):
            exponent += 1
        while bool(api.rational(2)**(exponent-1) >= value):
            exponent -= 1
        return exponent

    publish()
    try:
        for name in admission_names:
            gate(name)
        import flint
        require(platform.python_version() == RUNTIME["Python"] and flint.__version__ == RUNTIME["python_flint"],
            "fixed new directed runtime")
        require(not any(x in sys.modules for x in ("numpy", "scipy")) and
            all(os.environ.get(x) == "1" for x in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")),
            "no floating propagation dependency; fixed external math threads")
        flint.ctx.prec = RUNTIME["admission_and_model_definition_bits"]
        api = helper.NumericalAPI(flint)
        document["runtime"] = copy.deepcopy(RUNTIME)
        gate(GATE_SUFFIX[0])
        collar = import_pinned(root, specs["collar_math"], "_TF_collar_math")
        km = import_pinned(root, specs["kernel_math"], "_TF_kernel_math")
        assembly = import_pinned(root, specs["assembly_math"], "_TF_assembly_math")
        reference = import_pinned(root, specs["reference_math"], "_TF_reference_math")
        green = import_pinned(root, specs[GREEN_ROLE], "_TF_Green_math")
        refined = import_pinned(root, specs[REFINED_ROLE], "_TF_refined_math")
        child = import_pinned(root, specs[CHILD_ROLE], "_TF_child_math")
        flow = import_pinned(root, specs[FLOW_ROLE], "_TF_true_flow_math")
        old = {}
        for name, record in admitted["same_operator_records"].items():
            if name in ("G_c", "L_c_raw"):
                exact = Fraction(record)
                value = api.rational(exact.numerator, exact.denominator)
            else:
                value = api.old_interval(record)
            old[name] = api.upper(value)
        require(len(old) == 29, "all original same-operator saved records, no old bounds recomputed")
        completed = admitted["completed_tracefree_inputs"]
        math_start = time.monotonic()
        context = assembly.prepare_complete_kernel_context(api, km, reference, collar, admitted,
            completed["complete_original_candidate"], old, core.signed_display_centre, progress)
        require(context.reference_identity == signed["reference_identity"]
            and len(context.domain.cells) == 155 and context.parent_definition_count == 153
            and context.original_body_row_count == 4650 and context.original_intersection_count == 4801,
            "unchanged complete true WVC coefficient object and full interval coverage")
        document["reference_identity"] = copy.deepcopy(context.reference_identity)
        gate(GATE_SUFFIX[1])
        flint.ctx.prec = RUNTIME["directed_certificate_bits"]
        refined_context = refined.RefinedContext(context, counts)
        balances = [refined.exact_float(api, row[3]) for row in rows_plan]
        charts = refined.prepare_chart_specs(api, context, refined_context, progress)
        provider = child.WholeChildSignedCoefficientProvider(api, km, green, assembly, collar,
            admitted, context, refined_context, refined_context.domain.to_parent_box)
        import numpy as np
        require(np.__version__ == RUNTIME["numpy_proposal_only"],"pinned floating chart proposal")
        math_module, carriers, runner = (import_pinned(root, specs["grassmann_"+name], "_GG_"+name)
                                         for name in ("math","carriers","runner"))
        gate(GATE_SUFFIX[2])
        start_target(TARGETS[0])

        def inverse_done(model):
            flags = ("kind","complete_refined_cells","true_hybrid_BVP_verified",
                "exact_rational_householder_frames","all193_original_mean_and_boundary_coordinates_retained",
                "ordinary_dr_and_true_root_lengths_retained","physical_S_replaced_by_internal_balance")
            document["certificate"]["true_model"] = {key:model[key] for key in flags}
            document["certificate"]["true_model"]["accepted_subbox_counts"] = [
                v["subboxes"] for v in model["local_statistics"]]
            document["certificate"]["actual_low_hybrid_inverse_proved"] = True
            document["proved"] = True
            finish_target()
            gate(GATE_SUFFIX[3])
            start_target(TARGETS[1])

        def maps_done(maps):
            require(maps["complete"] is True and maps["source_roles_completed"] == SOURCE_ROLES,
                    "all four complete source maps")
            document["certificate"]["sources"] = public(maps["sources"])
            finish_target()
            gate(GATE_SUFFIX[4])

        def save_receipts(packets, matrices, resources):
            document["certificate"].update(packet_carriers=packets, joint_matrices=matrices,
                                           observed_resource_usage=resources)
            publish(False)

        runner.run_joint_targets(np=np, flint=flint, api=api, km=km, green=green, refined=refined,
            flow=flow, context=refined_context, provider=provider, charts=charts, balances=balances,
            original=original, restore=restore, math_module=math_module, carriers_module=carriers,
            private_directory=output.parent/"private-grassmann",native_directory=Path(args.native).parent,
            started=math_start, wall_seconds=CERTIFICATE_PARAMETERS["maximum_certificate_wall_seconds"],
            progress=progress,finish_inverse=inverse_done,finish_maps=maps_done,save_receipts=save_receipts)
        require(Path(args.manifest).read_bytes() == manifest_raw, "same whole fixed manifest")
        for spec in manifest["files"]:
            core.read_spec(root, spec)
        require(document["completed_targets"] == TARGETS
            and all(document["certificate"][key] is False for key in
                ("actual_full_positive_inverse_proved", "actual_complete_CFB_centre_proved",
                 "original_finite_rho_bridge_proved", "original_seven_ports_proved",
                 "either_original_nonlinear_RHS_proved", "topic_completion_proved")),
            "same complete low-only result, all whole-problem obligations retained")
        document["complete"] = True
        document["actual_returncode"] = 0
        document["stage"] = "complete_true_low193_inverse_and_four_source_maps"
        document["gates"].append({"name":GATE_SUFFIX[5],"passed":True})
        publish()
        return 0
    except BaseException as error:
        document["complete"] = False
        document["actual_returncode"] = 1
        document["stage"] = "failed_with_actual_finite_prefix_retained"
        full = traceback.format_exc()
        print(full, flush=True)
        document["failure"] = {"type": type(error).__name__, "message": str(error)[:1500],
            "traceback": full[-2500:], "full_traceback_in_public_job_log": True,
            "actual_operator_singularity_inferred": False,
            "previously_completed_new_target_retained": True}
        publish()
        return 1


if __name__ == "__main__":
    sys.exit(main())
