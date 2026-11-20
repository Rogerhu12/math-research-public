"""Public one-shot owner of two actual selected physical outer residual values.

Only one old84KB raw endpoint container is restored. Complete small repaired,
family, exact-direction and selected-member receipts are read unchanged.
No old producer, physical Fourier moment, outer solve or endpoint target is run.
"""
from __future__ import annotations

import argparse
import ast
import copy
from fractions import Fraction
import gzip
import hashlib
import importlib.metadata
import importlib.util
import json
import os
from pathlib import Path
import platform
import sys
import time
import traceback

REPOSITORY = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
KIND = "complete_selected_member_physical_outer_residual_values_v1"
MANIFEST_KIND = "complete_selected_physical_outer_residual_value_inputs_v1"
PROBLEM_ID = "R141_selected_physical_outer_Robin_mean_values_d10_v1"
MATH_NAME = "fourfold_codazzi_selected_physical_outer_values_math.py"
RUNTIME = {"Python": "3.12.14", "python_flint": "0.9.0"}
PARAMETERS = {
    "arithmetic_bits": 320,
    "true_physical_outer_endpoint": "25/8",
    "exact_direction_radius": "1/10000000000",
    "old_complete_direction_radius": "1/100000000",
    "old_homotopy_C_difference_scale": "1/100",
    "selected_member_run": "43588332723/1",
    "selected_member_loss": "1/250",
    "selected_parameter_absolute_upper": "0.00000000009368259853002",
    "selected_parameter_not_replaced_by_a_numeric_point": True,
    "exact_amplitude": "6890507429876859/9007199254740992",
    "exact_eta0": "-7789843107295549/4611686018427387904",
    "exact_nu0": "-2572625729470897/72057594037927936",
    "raw_candidate": "ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413",
    "centre_definition": "440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47",
    "direction_definition": "6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04",
    "whole_raw_physical_rows": 128,
    "full_moving_direction_dimension": 193,
    "independent_direction_mean_retained": True,
    "old_complete_interval_record_count": 19,
    "new_principal_scalar_count": 2,
    "common_mean_floor": "29/5",
    "raw_analytic_strip": "1/8",
    "physical_Z_ball_radius": "1/1000000000000",
    "same_background_height_radius": "1/1152921504606846976",
    "height_radius_is_not_a_height_rhs_value": True,
    "Robin_output_norm": "normalized physical-circle H^-5/6",
    "mean_output_norm": "absolute physical scalar",
    "frequency": "4j",
    "physical_angle_is_the_original_theta": True,
    "old_successful_targets_recomputed": 0,
    "scientific_wall_cap_seconds": 120,
    "single_threads": True,
}
TARGETS = (
    "complete_selected_physical_Robin_Hminus5over6_upper",
    "complete_selected_independent_physical_mean_residual_upper",
)
GATES = (
    "pinned_manifest_contract",
    "all_current_input_bytes_and_AST_exact",
    "one_historical_raw_boundary_native_exact",
    "old_raw_reference_all13_gates_and_full128_physical_rows",
    "old_repaired_outer_execution_and_complete25_gate_summary",
    "old_family_outer_execution_and_complete25_gate_summary",
    "old_full193_direction_endpoint_execution_and_all14_gates",
    "old_selected_NIF_execution_and_all16_gates",
    "old_same_member_WOBSA_execution_and_all18_gates",
    "same_raw_repair_direction_fixed_eta_and_same_background_height",
    "declared_single_threads_and_pinned_public_runtime",
    "nineteen_complete_old_records_and_exact_mean_directed_read",
    "moving_increment_and_true_full_mean_complete",
    "same_physical_inverse_angle_and_positive_gaps_complete",
    "old_whole_C_change_scaling_and_same_theta_B_difference_complete",
    "both_new_values_saved_readback_contain_their_original_upper",
    "physical_norms_reciprocal_mean_and_all_unpaid_scope_retained",
    "all_inputs_unchanged_and_complete_two_target_schema",
)
REQUIRED_ROLES = (
    "science", "math_core", "outer_values_proof", "raw_values_proof",
    "raw_restore_note", "raw_source", "repaired_summary", "repaired_process",
    "family_summary", "family_process", "endpoint_process", "nif_actual",
    "nif_execution", "wobsa_actual", "wobsa_execution", "family_outer_source",
    "actual_source_pair_proof", "nif_proof",
)
RETAINED_SCOPE = {
    "same_selected_member_by_uniform_delta10_restriction_only": True,
    "selected_delta_is_not_zero_or_the_radius_point": True,
    "selected_KAM_H_is_not_the_exterior_height": True,
    "same_raw_repaired_centre_unscaled_direction_and_fixed_eta0": True,
    "nu_invariance_uses_the_entire_original_exterior_metric_and_unique_graph": True,
    "same_fixed_background_fB_in_both_values": True,
    "height_background_radius_is_not_a_Newton_height_rhs": True,
    "independent_moving_mean_and_true_physical_reciprocal_mean_retained": True,
    "whole_physical_circle_and_infinite_Fourier_tail_retained": True,
    "old_actual_values_plus_same_operator_DN_difference_not_derivative_relabelling": True,
    "full_nonmean_physical_DN_domain_not_only_high_compression": True,
    "only_old_uniform_homotopy_direction_fee_scaled_by_one_over100": True,
    "fixed_centre_repair_not_scaled_by_parameter_radius": True,
    "raw_physical_amplitude_not_applied_again": True,
    "physical_source_norms_do_not_include_unknown_endpoint_Theta_weight": True,
    "both_positive_and_negative_outer_graph_qualifications_retained": True,
    "complete_WOB_high_and_low_affine_source_paths_both_required": True,
    "height_actual_rhs_far_label_and_global_gauge_still_unpaid": True,
    "nu_response_boundary_discrepancy_of_known_Z_still_separate": True,
    "negative_germ_interface_root_and_seven_port_inputs_still_separate": True,
    "original_finite_rho_and_full_inverse_still_separate": True,
    "future224_future32_and_both_WPN_rhs_not_created": True,
    "no_old_producer_imports_or_old_scientific_targets": True,
    "no_new_arrays_artifacts_or_Releases": True,
}
NATIVE = {
    "role": "original_raw_boundary_native",
    "path": "topics/visible-flex-exact-nearby/notes/2026-11-14-R133-moving0765-actual-R-boundary-restored-native.json.gz",
    "commit": "46f127c7153f5393dcd2a00f42d4c1d3662c294d",
    "bytes": 84003,
    "sha256": "bb2767633225f19f27c6c2646ac47c1142352a3a03882c916868e079f0fb055a",
    "git_blob_sha": "aded3d60581649518060190c49e7d0524365ada5",
}
SCIENTIFIC_FIELDS = (
    "actual_mathematical_wall_seconds", "actual_progress", "actual_returncode",
    "actual_scientific_checkout_commit", "all_saved_records_readback_verified",
    "automatic_scientific_retry", "complete", "complete_metadata",
    "complete_new_scalar_records", "complete_physical_value_conclusion",
    "copied_old_scalar_records", "current_input_receipts", "failure",
    "gates", "input_manifest_sha256", "kind", "metadata_admission_complete",
    "new_arrays_published", "new_artifacts", "new_Releases",
    "old_numerical_producers_called", "old_scientific_source_imports",
    "old_successful_targets_recomputed", "parameters", "problem_id", "proved",
    "repository", "restoration_receipts", "retained_scope", "runtime",
    "run_attempt", "run_id", "saved_record_count", "source_sha256",
    "target_order", "whole_old_evidence",
)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False)+"\n").encode("utf-8")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def git_blob(raw):
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def parse(raw):
    return json.loads(raw, parse_constant=lambda value: (_ for _ in ()).throw(
        ValueError("nonfinite JSON token: "+value)))


def atomic(path, raw):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".tmp")
    with temporary.open("wb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)
    require(path.read_bytes() == raw, "complete atomic result did not read back")


def complete(document, count):
    return (document.get("complete") is True and document.get("failure") is None
            and len(document.get("gates", [])) == count
            and all(g.get("passed") is True for g in document["gates"]))


def load_new_math(path):
    spec = importlib.util.spec_from_file_location("_new_selected_physical_values_math", path)
    require(spec is not None and spec.loader is not None, "new math loader is absent")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class DirectedAPI:
    def __init__(self, arb):
        self.arb = arb

    def rational(self, value):
        value = Fraction(value)
        return self.arb(value.numerator)/value.denominator

    def old_interval(self, record):
        if isinstance(record, dict):
            require(isinstance(record.get("lower"), str)
                    and isinstance(record.get("upper"), str),
                    "old complete scalar lacks its saved endpoint balls")
            result = self.arb(record["lower"]).lower().union(
                self.arb(record["upper"]).upper())
        else:
            require(isinstance(record, str), "old scalar is not complete saved text")
            result = self.arb(record)
        require(result.is_finite(), "nonfinite saved interval")
        return result

    def upper(self, value):
        require(value.is_finite(), "nonfinite new directed expression")
        return value.upper()

    def lower(self, value):
        require(value.is_finite(), "nonfinite new directed expression")
        return value.lower()

    def record(self, value):
        require(value.is_finite(), "nonfinite new scalar record")
        return {"ball": value.str(80)}


def execute(args):
    root, output = Path(args.repo).resolve(), Path(args.out)
    start, math_start, api = time.monotonic(), None, None
    require(not output.exists(), "new one-shot output already exists")
    document = {
        "kind": KIND, "repository": REPOSITORY, "problem_id": PROBLEM_ID,
        "input_manifest_sha256": args.manifest_sha,
        "source_sha256": sha(Path(__file__).read_bytes()),
        "run_id": os.environ.get("GITHUB_RUN_ID"),
        "run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT"),
        "actual_scientific_checkout_commit": os.environ.get("CURRENT_SCIENCE_COMMIT"),
        "parameters": copy.deepcopy(PARAMETERS),
        "retained_scope": copy.deepcopy(RETAINED_SCOPE),
        "runtime": None, "gates": [], "current_input_receipts": [],
        "restoration_receipts": None, "whole_old_evidence": {},
        "metadata_admission_complete": False, "complete_metadata": None,
        "copied_old_scalar_records": {},
        "target_order": list(TARGETS), "complete_new_scalar_records": {},
        "complete_physical_value_conclusion": None,
        "actual_progress": {
            "stage": "not_started", "completed_targets": 0,
            "current_target": None, "last_complete_budget_stage": None,
            "unfinished_complete_budget_records": {},
        },
        "saved_record_count": 0, "all_saved_records_readback_verified": False,
        "old_numerical_producers_called": 0, "old_scientific_source_imports": 0,
        "old_successful_targets_recomputed": 0, "new_arrays_published": 0,
        "new_artifacts": 0, "new_Releases": 0, "automatic_scientific_retry": False,
        "actual_mathematical_wall_seconds": 0, "actual_returncode": None,
        "complete": False, "proved": False, "failure": None,
    }

    def save():
        require(sorted(document) == sorted(SCIENTIFIC_FIELDS),
                "scientific result outer fields changed")
        if math_start is not None:
            document["actual_mathematical_wall_seconds"] = time.monotonic()-math_start
        data = canonical(document)
        require(len(data) <= 60000, "complete small result exceeds its fixed cap")
        atomic(output, data)

    def gate(name, ok=True):
        require(name == GATES[len(document["gates"])], "new gates reordered")
        document["gates"].append({"name": name, "passed": bool(ok)})
        save()
        require(ok, "new physical-value gate failed: "+name)

    def wall_guard():
        require(time.monotonic()-start < PARAMETERS["scientific_wall_cap_seconds"],
                "fixed new wall cap; complete original prefix retained")

    def execution(actual, receipt, role, run_id, count):
        result = receipt.get("scientific_conclusion", {})
        return (complete(actual, count) and actual.get("proved") is True
                and actual.get("actual_returncode") == 0
                and str(receipt.get("run_id")) == run_id
                and str(receipt.get("run_attempt")) == "1"
                and receipt.get("complete") is True
                and receipt.get("actual_returncode") == 0
                and result.get("complete") is True
                and result.get("actual_returncode") == 0
                and result.get("actual_gate_count") == count
                and result.get("actual_passed_gate_count") == count
                and result.get("bytes") == by_role[role]["bytes"]
                and result.get("sha256") == by_role[role]["sha256"])

    def summary_in_process(summary, receipt, role, run_id, key, native):
        entries = [item for item in receipt.get("native_files", [])
                   if item.get("bytes") == by_role[role]["bytes"]
                   and item.get("sha256") == by_role[role]["sha256"]]
        children = receipt.get("children", [])
        return (complete(summary, 25) and receipt.get("complete") is True
                and str(receipt.get("run_id")) == run_id
                and str(receipt.get("run_attempt")) == "1"
                and receipt.get(key+"_complete") is True
                and receipt.get(key+"_native_sha256") == native
                and summary.get("native_sha256") == native
                and receipt.get("all_pinned_inputs_verified") is True
                and len(entries) == 1 and len(children) == 2
                and all(child.get("actual_returncode") == 0 for child in children))

    try:
        save()
        require(os.environ.get("GITHUB_ACTIONS") == "true"
                and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
                "new directed arithmetic belongs to authorized public Actions only")
        manifest_bytes = Path(args.manifest).read_bytes()
        manifest = parse(manifest_bytes)
        gate(GATES[0], sha(manifest_bytes) == args.manifest_sha
             and manifest.get("kind") == MANIFEST_KIND
             and manifest.get("repository") == REPOSITORY
             and manifest.get("problem_id") == PROBLEM_ID
             and manifest.get("parameters") == PARAMETERS
             and manifest.get("runtime") == RUNTIME
             and manifest.get("scope") == RETAINED_SCOPE
             and manifest.get("scientific_kind") == KIND
             and tuple(manifest["target_order"]) == TARGETS
             and tuple(manifest["gate_order"]) == GATES
             and sorted(manifest["allowed_scientific_fields"]) == sorted(SCIENTIFIC_FIELDS))
        by_role, contents = {}, {}
        for item in manifest["files"]:
            role, relative = item["role"], item["path"]
            require(role not in by_role and relative.startswith(TOPIC+"/")
                    and all(part not in ("", ".", "..") for part in relative.split("/")),
                    "duplicate or unsafe current input role")
            path = (root/relative).resolve()
            require(path.is_relative_to(root), "current input left the snapshot")
            data = path.read_bytes()
            require(len(data) == item["bytes"] and sha(data) == item["sha256"]
                    and git_blob(data) == item["git_blob_sha"],
                    "current byte identity differs: "+role)
            data.decode("utf-8")
            if relative.endswith(".py"):
                ast.parse(data, filename=relative)
            by_role[role], contents[role] = item, data
            document["current_input_receipts"].append(copy.deepcopy(item))
        gate(GATES[1], len(by_role) == manifest["expected_current_input_count"]
             and set(REQUIRED_ROLES).issubset(by_role)
             and by_role["science"]["sha256"] == document["source_sha256"]
             and Path(by_role["math_core"]["path"]).name == MATH_NAME)
        historical = manifest["historical_inputs"]
        restored = parse(Path(args.restoration_receipts).read_bytes())
        require(historical == [NATIVE] and restored["original_inputs"] == [NATIVE],
                "only the exact single historical raw endpoint container is allowed")
        raw_bytes = Path(args.raw_boundary).read_bytes()
        gate(GATES[2], len(raw_bytes) == NATIVE["bytes"]
             and sha(raw_bytes) == NATIVE["sha256"]
             and git_blob(raw_bytes) == NATIVE["git_blob_sha"]
             and raw_bytes[:2] == b"\x1f\x8b")
        raw = parse(gzip.decompress(raw_bytes))
        document["restoration_receipts"] = copy.deepcopy(restored)
        gate(GATES[3], raw.get("complete") is True and raw.get("failure") is None
             and len(raw.get("gates", {})) == 13
             and all(value is True for value in raw["gates"].values())
             and len(raw.get("rows", [])) == 128
             and raw.get("source_sha256") == by_role["raw_source"]["sha256"])
        old = {role: parse(contents[role]) for role in (
            "repaired_summary", "repaired_process", "family_summary", "family_process",
            "endpoint_process", "nif_actual", "nif_execution", "wobsa_actual", "wobsa_execution")}
        repaired, family = old["repaired_summary"], old["family_summary"]
        gate(GATES[4], summary_in_process(repaired, old["repaired_process"],
             "repaired_summary", "43601149891", "actual_repaired_outer",
             "75e7c0e1447306a97971ee05dcb68b8d357cb4fffa5c1a37335a6fc29a473424"))
        gate(GATES[5], summary_in_process(family, old["family_process"],
             "family_summary", "43615531666", "actual_full_delta_outer",
             "5ab1d1b85cb71556b051fd53f5579cb30260ebdda6a844df9a4b377508e057fc")
             and family.get("source_sha256") == by_role["family_outer_source"]["sha256"])
        endpoint = old["endpoint_process"]
        gate(GATES[6], endpoint.get("complete") is True and endpoint.get("failure") is None
             and endpoint.get("actual_returncode") == 0
             and endpoint.get("mathematical_complete") is True
             and endpoint.get("mathematical_failure") is None
             and len(endpoint.get("mathematical_gates", [])) == 14
             and all(g.get("passed") is True for g in endpoint["mathematical_gates"]))
        gate(GATES[7], execution(old["nif_actual"], old["nif_execution"],
                                "nif_actual", "43795909913", 16))
        w, we = old["wobsa_actual"], old["wobsa_execution"]
        wf = we.get("scientific_files", [])
        gate(GATES[8], complete(w, 18) and w.get("actual_returncode") == 0
             and str(we.get("run_id")) == "43844596176"
             and str(we.get("run_attempt")) == "1"
             and we.get("actual_child_returncode") == 0
             and we.get("scientific_complete") is True
             and we.get("original_scientific_complete_flag") is True
             and we.get("failure") is None
             and we.get("original_scientific_failure") is None
             and we.get("scientific_children") == 1 and len(wf) == 1
             and wf[0]["bytes"] == by_role["wobsa_actual"]["bytes"]
             and wf[0]["sha256"] == by_role["wobsa_actual"]["sha256"])
        math = load_new_math(root/by_role["math_core"]["path"])
        require(math.KIND == KIND and math.TARGETS == TARGETS,
                "new mathematical contract differs")
        admitted = math.admit_metadata(raw, repaired, family, endpoint,
                                       old["nif_actual"], old["wobsa_actual"])
        document["metadata_admission_complete"] = True
        document["complete_metadata"] = copy.deepcopy(admitted["metadata"])
        document["copied_old_scalar_records"] = {
            "complete_nineteen_intervals": copy.deepcopy(admitted["records"]),
            "exact_direction_mean": admitted["exact_direction_mean"],
            "same_far_height_background_radius": copy.deepcopy(admitted["raw_far_height_radius"]),
        }
        document["whole_old_evidence"] = {
            "raw_native": {"identity": copy.deepcopy(NATIVE),
                           "complete": raw["complete"], "whole_gates": raw["gates"]},
            **{role: {"identity": copy.deepcopy(by_role[role]),
                      "complete": old[role].get("complete"),
                      "whole_gates": copy.deepcopy(old[role].get(
                          "mathematical_gates" if role == "endpoint_process" else "gates"))}
               for role in ("repaired_summary", "family_summary", "endpoint_process",
                            "nif_actual", "wobsa_actual")},
        }
        gate(GATES[9])
        runtime = {"Python": platform.python_version(),
                   "python_flint": importlib.metadata.version("python-flint")}
        document["runtime"] = runtime
        gate(GATES[10], runtime == RUNTIME
             and all(os.environ.get(key) == "1" for key in
                     ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS")))
        from flint import arb, ctx
        ctx.prec = 320
        api = DirectedAPI(arb)
        math_start = time.monotonic()
        for record in admitted["records"].values():
            require(api.upper(api.old_interval(record)) >= 0,
                    "old complete interval has no nonnegative upper")
        require(api.rational(admitted["exact_direction_mean"]).is_finite(),
                "exact independent direction mean is not finite")
        gate(GATES[11], len(admitted["records"]) == 19)

        def progress(stage, values):
            expected = {
                "complete_moving_increment": GATES[12],
                "complete_same_physical_angle": GATES[13],
                "complete_fixed_theta_state_difference": GATES[14],
            }
            require(stage in expected, "unexpected new budget stage")
            wall_guard()
            document["actual_progress"]["stage"] = stage
            document["actual_progress"]["last_complete_budget_stage"] = stage
            document["actual_progress"]["unfinished_complete_budget_records"][stage] = {
                key: api.record(value) for key, value in values.items()}
            gate(expected[stage])

        saved_uppers = {}

        def emit(name, value):
            wall_guard()
            index = len(document["complete_new_scalar_records"])
            require(index < len(TARGETS) and name == TARGETS[index],
                    "new complete targets reordered or duplicated")
            original_upper = api.upper(value)
            require(original_upper >= 0, "new value upper is negative")
            document["actual_progress"]["current_target"] = name
            document["complete_new_scalar_records"][name] = api.record(original_upper)
            document["saved_record_count"] = index+1
            document["actual_progress"]["completed_targets"] = index+1
            save()
            reread = parse(output.read_bytes())
            stored = arb(reread["complete_new_scalar_records"][name]["ball"])
            require(stored.is_finite() and stored.contains(original_upper),
                    "saved interval fails explicit original-upper containment")
            saved_upper = api.upper(stored)
            require(saved_upper >= original_upper, "saved directed upper narrowed")
            saved_uppers[name] = saved_upper
            return saved_upper

        conclusion = math.complete_bounds(api, admitted, emit, progress)
        gate(GATES[15], len(saved_uppers) == 2
             and document["saved_record_count"] == 2
             and tuple(document["complete_new_scalar_records"]) == TARGETS)
        false_fields = (
            "height_actual_rhs_value_proved", "far_regular_label_or_height_gauge_equation_proved",
            "actual_nu_response_boundary_discrepancy_of_Z_proved",
            "negative_germ_interface_and_root_inputs_proved", "both_complete_WPN_rhs_proved",
            "complete_infinite_inverse_proved", "nonlinear_solution_proved",
        )
        gate(GATES[16], conclusion.get("complete") is True
             and conclusion.get("completed_target_count") == 2
             and conclusion.get("same_fixed_physical_theta_and_complete_Fourier_tail") is True
             and conclusion.get("independent_physical_mean_is_reciprocal_moving_mean") is True
             and all(conclusion.get(key) is False for key in false_fields))
        for role, item in by_role.items():
            data = (root/item["path"]).read_bytes()
            require(len(data) == item["bytes"] and sha(data) == item["sha256"]
                    and data == contents[role], "an admitted current input changed")
        require(Path(args.raw_boundary).read_bytes() == raw_bytes
                and Path(args.manifest).read_bytes() == manifest_bytes,
                "the original native or fixed manifest changed")
        document["complete_physical_value_conclusion"] = conclusion
        document["all_saved_records_readback_verified"] = True
        gate(GATES[17], document["old_successful_targets_recomputed"] == 0
             and document["old_numerical_producers_called"] == 0
             and document["old_scientific_source_imports"] == 0
             and len(document["gates"]) == 17)
        document["complete"] = True
        document["proved"] = True
        document["actual_returncode"] = 0
        document["actual_progress"]["stage"] = "complete_two_physical_values"
        document["actual_progress"]["current_target"] = None
        save()
        print(json.dumps({"complete": True, "gates": 18, "saved_values": 2,
                          "output": str(output), "height_rhs_proved": False}), flush=True)
        return 0
    except Exception as exc:
        document["complete"] = False
        document["proved"] = False
        document["actual_returncode"] = 1
        document["failure"] = {"type": type(exc).__name__, "message": str(exc),
                               "traceback": traceback.format_exc()[-12000:]}
        save()
        print(json.dumps({"complete": False, "failure": document["failure"],
                          "completed_targets": document["saved_record_count"]}), flush=True)
        return 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--manifest-sha", required=True)
    parser.add_argument("--raw-boundary", required=True)
    parser.add_argument("--restoration-receipts", required=True)
    parser.add_argument("--out", required=True)
    return execute(parser.parse_args())


if __name__ == "__main__":
    sys.exit(main())
