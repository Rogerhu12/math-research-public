"""First actual variable-coefficient low193 finite-flow inverse certificate.

The original21 native objects,4650 whole body rows,65 repair coordinates,
actual family speed, fixed WVC reference, mean and boundary193 coordinates
are admitted unchanged.  Old SL/HS records and original1424 cuts are read
only.  No old comparison Green, HS, trace, QR or producer target is called.

Two new targets: all true local-flow finite pivots, then all four complete
true-inverse source maps.  A failed second target preserves a completed
first target.  All finite-pivot indices and directed inverse-norm powers
are saved; large reconstructible matrices remain private.
"""
from __future__ import annotations
import argparse
import copy
import gzip
import hashlib
import importlib.util
import json
import math
import os
import platform
import re
import resource
import sys
import time
import traceback
from fractions import Fraction
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby/"
SOURCE_PATH = TOPIC+"scripts/fourfold_codazzi_true_low193_direct_flow_owner.py"
KIND = "complete_R149_true_low193_direct_flow_and_source_maps_v1"
PREFLIGHT_KIND = "complete_R149_true_low193_direct_flow_preflight_v1"
ENTRY_ROLE = "true_low193_direct_flow_owner"
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
TARGETS = ["complete_actual_low193_local_flow_and_all_finite_pivots",
           "complete_actual_low193_four_sources_and193_atoms"]
RUNTIME = {"Python": "3.12.14", "python_flint": "0.9.0",
           "admission_and_model_definition_bits": 320,
           "directed_certificate_bits": 384, "BLAS_threads": 1}
CERTIFICATE_PARAMETERS = {
    "actual_operator": "original WVC hybrid ALc, complete actual family eta and repaired lower coefficients",
    "all193_original_coordinates_and_independent_mean": True,
    "all193_original_observations": True,
    "ordinary_dr_and_true_root_lengths": True,
    "original_parents": 155, "original_body_rows": 4650, "repair_coordinates": 65,
    "complete_refined_cells": 1424,
    "cuts_per_refined_cell": 4, "Peano_Baker_order": 24,
    "maximum_cuts_only_in_uncompleted_current_cell": 64,
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
    "all_actual_finite_pivots_and_true_inverse_saved",
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
    bound_sources = manifest["scientific_modules"]+[specs[role] for role in
        (ENTRY_ROLE, GREEN_ROLE, REFINED_ROLE, CHILD_ROLE, FLOW_ROLE)]
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
        "certificate": {"actual_low_hybrid_inverse_proved": False,
            "actual_full_positive_inverse_proved": False, "actual_complete_CFB_centre_proved": False,
            "original_finite_rho_bridge_proved": False, "original_seven_ports_proved": False,
            "either_original_nonlinear_RHS_proved": False, "topic_completion_proved": False,
            "refinement": {"counts": list(counts), "complete_refined_cells": sum(counts),
                "all_original_cuts_retained": True, "true_root_lengths_retained": True},
            "finite_pivots": {"left97": [], "right96": [], "node_transversality": [],
                "entry_semantics": "each integer e certifies complete inverse induced-2 norm <= 2^e",
                "left_index_order": "0 through1423", "right_index_order": "1423 through0",
                "node_index_order": "1424 through0", "completed": 0, "in_progress": None,
                "whole_ordered_record_chain_sha256": hashlib.sha256(b"true_low193_pivots_v1").hexdigest()},
            "true_model": None, "sources": {}, "private_storage": None}}
    require(sorted(document) == SCI_FIELDS, "one complete output schema")
    math_start, store, provider, last_pivot_matrix = None, None, None, None
    last_publish = 0.0

    def budget():
        require(sys.platform.startswith("linux"), "Linux resident units")
        resident = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)*1024
        document["actual_progress"]["maximum_process_resident_bytes_observed"] = resident
        require(resident <= CERTIFICATE_PARAMETERS["maximum_scientific_process_resident_bytes"],
            "actual process memory cap; complete prefix retained")
        if math_start is not None:
            require(time.perf_counter()-math_start <= CERTIFICATE_PARAMETERS["maximum_certificate_wall_seconds"],
                "actual process wall cap; complete prefix retained")

    def publish(verbose=True):
        nonlocal last_publish
        if math_start is not None:
            document["actual_mathematical_wall_seconds"] = time.perf_counter()-math_start
        if store is not None:
            document["certificate"]["private_storage"] = store.metadata()
        if provider is not None:
            document["certificate"]["whole_child_provider_statistics"] = copy.deepcopy(provider.statistics)
        raw = canonical(document)
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
        document["preparation_prefix"] = {"stage": stage, "detail": detail}
        document["stage"] = "working:"+stage
        if stage == "true_low193_local_transfer_and_left_graph":
            document["actual_progress"]["actual_left_cells_complete"] = detail["cells_complete"]
        elif stage == "true_low193_right_graph_and_transversality":
            document["actual_progress"]["actual_right_cells_complete"] = detail["cells_complete"]
        elif stage == "true_low193_complete_source_covariances":
            document["actual_progress"]["actual_source_cells_complete"] = detail["cells_complete"]
        elif stage == "true_low193_refine_only_uncompleted_current_cell":
            document["actual_progress"]["local_current_cell_refinements"].append(copy.deepcopy(detail))
            publish()
        budget()
        if time.perf_counter()-last_publish >= 30:
            publish()

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
        require(value is None or isinstance(value, (str, int, bool)), "small complete public type")
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

    def pivot_observer(status, phase, index, matrix, inverse):
        nonlocal last_pivot_matrix
        ledger = document["certificate"]["finite_pivots"]
        require(phase in ("left97", "right96", "node_transversality"), "one full actual finite pivot")
        expected = (len(ledger[phase]) if phase == "left97" else
                    (1424 if phase == "node_transversality" else 1423)-len(ledger[phase]))
        require(index == expected and matrix.rows == matrix.cols == (97 if phase == "left97" else 96),
            "each true finite pivot appears exactly once in declared order")
        if status == "start":
            budget()
            last_pivot_matrix = matrix
            ledger["in_progress"] = {"phase": phase, "index": index, "dimension": matrix.rows,
                "whole_matrix_2norm_upper": scalar(flow.two_upper(api, matrix)),
                "same_actual_full_matrix_not_a_principal_projection": True}
            publish(verbose=False)
            return
        require(status == "complete" and inverse is not None, "directed actual inverse returned")
        bound = flow.two_upper(api, inverse)
        exponent = inverse_power(bound)
        record = {"phase": phase, "index": index, "dimension": matrix.rows, "inverse_norm_power2": exponent}
        ledger[phase].append(exponent)
        ledger["whole_ordered_record_chain_sha256"] = hashlib.sha256(
            bytes.fromhex(ledger["whole_ordered_record_chain_sha256"])+canonical(record)).hexdigest()
        ledger["completed"] += 1
        ledger["in_progress"] = None
        print(json.dumps({"actual_pivot": record, "whole_inverse_2norm_upper": scalar(bound)}, sort_keys=True), flush=True)
        publish(verbose=False)

    def private_failure_checkpoint():
        """Keep the complete failed matrix/last Z in THIS job, never git/Release.

        The whole private prefix is hashed in its original packed order.
        Reconstructible arrays are not published, split or uploaded.
        """
        matrices = {}
        if last_pivot_matrix is not None:
            matrices["last_attempted_actual_pivot"] = last_pivot_matrix
        if store is not None:
            keys = [key for key in store.data if key[:2] == ("true_temporary", "Z")]
            if keys:
                key = max(keys, key=lambda value: value[2])
                matrices["last_retained_complete_Z_at_node_"+str(key[2])] = store.get(key)
        if not matrices:
            return
        checkpoint = {"kind": "private_complete_true_low193_failure_state_v1",
            "manifest_sha256": args.manifest_sha, "run_id": run, "run_attempt": attempt,
            "finite_pivots": copy.deepcopy(document["certificate"]["finite_pivots"]),
            "preparation_prefix": copy.deepcopy(document["preparation_prefix"]),
            "matrices": {name: {"rows": value.rows, "cols": value.cols,
                "whole_decimal_balls": [[scalar(entry) for entry in row] for row in value.values]}
                for name, value in matrices.items()}}
        raw = canonical(checkpoint)
        compressed = gzip.compress(raw, mtime=0)
        path = output.parent/"private-true-low193-failed-matrix-and-last-Z.json.gz"
        path.write_bytes(compressed)
        chain = hashlib.sha256(b"true_low193_complete_private_packed_state_v1")
        if store is not None:
            for key in sorted(store.data):
                rows, cols, payload = store.data[key]
                chain.update(canonical({"key": key, "rows": rows, "cols": cols,
                    "native_array_byte_order": sys.byteorder, "payload_bytes": len(payload)*payload.itemsize}))
                chain.update(payload.tobytes())
        document["certificate"]["private_failure_checkpoint"] = {
            "kind": checkpoint["kind"], "complete_matrices": {
                name: [value.rows, value.cols] for name, value in matrices.items()},
            "uncompressed_bytes": len(raw), "uncompressed_sha256": digest(raw),
            "compressed_bytes": len(compressed), "compressed_sha256": digest(compressed),
            "whole_retained_private_prefix_sha256": chain.hexdigest(),
            "all_saved_matrix_entries_are_complete_directed_decimal_balls": True,
            "complete_private_job_file": path.name,
            "arrays_published_to_git_Release_or_artifact": False,
            "complete_private_payload_durable_after_runner_exit": False}

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
        math_start = time.perf_counter()
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
        store = refined.PackedMatrices(api, km,
            maximum_bytes=CERTIFICATE_PARAMETERS["maximum_private_packed_payload_bytes"],
            maximum_decoded_entries=CERTIFICATE_PARAMETERS["maximum_decoded_matrix_entries"])
        gate(GATE_SUFFIX[2])
        start_target(TARGETS[0])
        model = flow.certify_true_model(api, km, green, refined, refined_context, provider,
            charts, balances, store, cuts_per_cell=CERTIFICATE_PARAMETERS["cuts_per_refined_cell"],
            order=CERTIFICATE_PARAMETERS["Peano_Baker_order"], source_roles=SOURCE_ROLES,
            progress=progress, pivot_observer=pivot_observer,
            maximum_cuts_per_cell=CERTIFICATE_PARAMETERS["maximum_cuts_only_in_uncompleted_current_cell"])
        ledger = document["certificate"]["finite_pivots"]
        require(model["true_hybrid_BVP_verified"] is True and ledger["completed"] == 4273
            and len(ledger["left97"]) == len(ledger["right96"]) == 1424
            and len(ledger["node_transversality"]) == 1425 and ledger["in_progress"] is None,
            "all actual true-flow finite pivots, including every node, complete")
        document["certificate"]["true_model"] = {"kind": model["kind"],
            "complete_refined_cells": 1424,
            "complete_true_subboxes": sum(v["subboxes"] for v in model["local_statistics"]),
            "accepted_local_cuts_per_cell": [v["subboxes"] for v in model["local_statistics"]],
            "complete_actual_pivots": 4273, "true_hybrid_BVP_verified": True,
            "all193_original_mean_and_boundary_coordinates_retained": True,
            "ordinary_dr_and_true_root_lengths_retained": True,
            "maximum_local_Peano_tail_upper": scalar(flow._maximum(api,
                [v["largest_local_tail_upper"] for v in model["local_statistics"]])),
            "maximum_complete_balanced_cell_span_upper": scalar(flow._maximum(api,
                [v["beta_sum_upper"] for v in model["local_statistics"]]))}
        document["certificate"]["actual_low_hybrid_inverse_proved"] = True
        document["proved"] = True
        finish_target()
        gate(GATE_SUFFIX[3])
        start_target(TARGETS[1])
        maps = flow.complete_true_source_maps(api, km, green, model, progress)
        require(set(maps["sources"]) == set(SOURCE_ROLES), "all four actual source maps")
        document["certificate"]["sources"] = public(maps["sources"])
        finish_target()
        gate(GATE_SUFFIX[4])
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
        gate(GATE_SUFFIX[5])
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
        try:
            private_failure_checkpoint()
        except Exception as checkpoint_error:
            document["certificate"]["private_checkpoint_failure"] = {
                "type": type(checkpoint_error).__name__, "message": str(checkpoint_error)[:1000],
                "original_mathematical_failure_unchanged": True}
        publish()
        return 1


if __name__ == "__main__":
    sys.exit(main())
