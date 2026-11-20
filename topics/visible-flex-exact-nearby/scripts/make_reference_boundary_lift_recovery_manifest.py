#!/usr/bin/env python3
"""Metadata only: recover the zero-mathematics D launch's declared threads.

The original79 inputs, old generator, scientific definitions, owner,
parameters, target contract and shared worker remain byte-for-byte fixed.
"""
from __future__ import annotations
import argparse
import ast
import copy
import hashlib
import json
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
ORIGINAL = TOPIC+"/notes/2026-11-20-reference-boundary-lifts-inputs.json"
ORIGINAL_BYTES = 70121
ORIGINAL_SHA = "9c4f0afe00aa1a5c1b3adb0f57df15d0773c67b8b163894eb06071b7e08f95f8"
ORIGINAL_WORKFLOW_SHA = "54b590f13ae2ec0dcb8034f6b35d770677a07589cdb36b41a07f2a6f834e5999"
MANIFEST = TOPIC+"/notes/2026-11-20-reference-boundary-lifts-thread-recovery-inputs.json"
GENERATOR = TOPIC+"/scripts/make_reference_boundary_lift_recovery_manifest.py"
WORKFLOW = ".github/workflows/fourfold-codazzi-reference-boundary-lifts-public.yml"
FAILURE_ACTUAL = TOPIC+"/notes/reference_boundary_lifts_ci/run-44742799448-1/actual-scientific-conclusion.json"
FAILURE_EXECUTION = TOPIC+"/notes/reference_boundary_lifts_ci/run-44742799448-1/execution.json"
FAILURE_ACTUAL_SHA = "eaeb74c5eb82ceb5dbd054f3ae00eb372d43f8eacc53fafa3405f5d156965af1"
FAILURE_EXECUTION_SHA = "7491a9f2372fa47c038590c58cf05fe70475f0678f855ca6cdd01863f9e37368"
THREAD_ENV = {"OPENBLAS_NUM_THREADS": "1", "OMP_NUM_THREADS": "1", "MKL_NUM_THREADS": "1"}
NEW_MARKER = TOPIC+"/notes/reference_boundary_lifts_ci/reference_boundary_lifts_thread_recovery_v2-consumed.json"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def identity(role, path, raw):
    require(0 < len(raw) < 100000, "whole small current input: "+path)
    raw.decode("utf-8")
    if path.endswith(".py"):
        ast.parse(raw, filename=path)
    return {"role": role, "path": path, "bytes": len(raw), "sha256": sha(raw),
            "git_blob_sha": hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()}


def encoded(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False)+"\n").encode()


def workflow_literal(raw):
    """Read only the unchanged old generator's complete literal template."""
    found = []
    for node in ast.walk(ast.parse(raw)):
        if (isinstance(node, ast.Assign) and len(node.targets) == 1
                and isinstance(node.targets[0], ast.Name) and node.targets[0].id == "workflow"):
            value = node.value
            while isinstance(value, ast.Call) and isinstance(value.func, ast.Attribute):
                require(value.func.attr == "replace", "only original literal workflow substitution")
                value = value.func.value
            literal = ast.literal_eval(value)
            require(isinstance(literal, str), "complete original workflow is one literal")
            found.append(literal)
    require(len(found) == 1, "one whole original workflow template")
    return found[0]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    root, out = args.repo.resolve(), args.out.resolve()
    raw_original = (root/ORIGINAL).read_bytes()
    require(len(raw_original) == ORIGINAL_BYTES and sha(raw_original) == ORIGINAL_SHA,
            "exact whole original70121-byte boundary manifest")
    original = json.loads(raw_original)
    require(original["kind"] == "complete_collar_Volterra_dual_current_inputs_v1"
            and original["problem_id"] == "W2C_complete_collar_Volterra_dual_candidate_v1"
            and len(original["files"]) == original["expected_current_input_count"] == 79,
            "unchanged original boundary operation and79 current input identities")
    by_role = {item["role"]: item for item in original["files"]}
    require(len(by_role) == 79, "all original roles unique")
    for item in original["files"]:
        require(identity(item["role"], item["path"], (root/item["path"]).read_bytes()) == item,
                "every original input remains byte-for-byte fixed: "+item["role"])
    require(original["worker"] == by_role["worker"]
            and by_role["worker"]["sha256"] == "98ef3773eab06178df086c5dcf551103c7cd3e00a5eca1c73cbfee089af84b1c"
            and by_role["reference_boundary_lift_owner"]["sha256"] == "4f585a3bd252fd827329e1bd84647be3926a9c258b5e4e0d884be5be2d860d95"
            and by_role["reference_boundary_lift_math"]["sha256"] == "ffb9185a9c2d97df7a04b7bbb2016c3365378be2be14589d53574cd3ae32a588"
            and by_role["reference_boundary_metadata_generator"]["sha256"] == "dc0dd610f22af1549eea74e2690546b4948192048feab364d6478fe0877be6e2",
            "all science, shared worker and old generator explicitly unchanged")
    operation = original["operation"]
    require(operation["scientific_entry_role"] == "reference_boundary_lift_owner"
            and len(operation["complete_gate_names"]) == 25
            and len(operation["scientific_field_names"]) == 39
            and operation["complete_target_counts"] == [2]
            and operation["return_parameters"]["complete_record_count"] == 10
            and operation["fixed_runtime"]["BLAS_threads"] == 1,
            "same25 gates39 fields two targets ten records and declared single thread")
    actual_raw, execution_raw = (root/FAILURE_ACTUAL).read_bytes(), (root/FAILURE_EXECUTION).read_bytes()
    require(len(actual_raw) == 51083 and sha(actual_raw) == FAILURE_ACTUAL_SHA
            and len(execution_raw) == 58697 and sha(execution_raw) == FAILURE_EXECUTION_SHA,
            "complete actual first failure and execution bytes")
    actual, execution = json.loads(actual_raw), json.loads(execution_raw)
    require(actual["kind"] == operation["scientific_kind"]
            and actual["run_id"] == execution["run_id"] == "44742799448"
            and actual["run_attempt"] == execution["run_attempt"] == "1"
            and actual["manifest_sha256"] == execution["manifest_sha256"] == ORIGINAL_SHA
            and actual["complete"] is False and actual["proved"] is False
            and actual["actual_returncode"] == execution["actual_child_returncode"] == 1
            and actual["failure"]["type"] == "ValueError"
            and actual["failure"]["message"] == "declared thread settings"
            and actual["current_target"] is None and actual["completed_targets"] == []
            and actual["saved_record_count"] == 0 and actual["new_records"] == {}
            and actual["actual_mathematical_wall_seconds"] == 0
            and actual["runtime"] == {}
            and actual["preparation_prefix"] == {"detail": None, "stage": "not_started"},
            "the actual first child failed solely at its declared thread gate before mathematics")
    require(len(actual["gates"]) == 19
            and [item["name"] for item in actual["gates"]] == operation["complete_gate_names"][:19]
            and all(item["passed"] is True for item in actual["gates"])
            and actual["parameters"] == original["parameters"]
            and actual["return_parameters"] == operation["return_parameters"]
            and actual["scientific_modules"] == operation["scientific_module_binding"],
            "all19 complete admission gates passed for the identical original science contract")
    zero_counters = ("reference_definitions_materialized", "reference_low_modes_prepared",
        "new_boundary_gram_panels_complete", "new_complete_targets", "new_boundary_records_saved",
        "actual_centre_or_family_packets_evaluated", "Gf_actions_evaluated", "GH_actions_evaluated",
        "low_inverse_actions_evaluated", "old_completed_targets_recomputed",
        "old_five_source_rate_targets_evaluated", "old_producer_entrypoints_called", "old_small_K50_graphs_called")
    require(all(actual["actual_progress"][key] == 0 for key in zero_counters)
            and execution["kind"] == "small_frozen_public_scientific_execution_v1"
            and execution["repository"] == "Rogerhu12/math-research-public"
            and execution["scientific_children"] == 1 and execution["scientific_complete"] is False
            and execution["completed_target_names"] == []
            and execution["readonly_preflight"]["returncode"] == 0
            and execution["failure"]["message"] == "unique scientific child failed",
            "zero scientific definitions, profiles, Grams, targets and records in the full actual prefix")
    review = json.loads((root/original["reviewed_rules"]["path"]).read_bytes())
    for path, digest in review["readme_sha256"].items():
        require(sha((root/path).read_bytes()) == digest, "current README rules still match the retained review")
    added = [
        identity("reference_boundary_thread_recovery_generator", GENERATOR, Path(__file__).read_bytes()),
        identity("reference_boundary_thread_failure_scientific", FAILURE_ACTUAL, actual_raw),
        identity("reference_boundary_thread_failure_execution", FAILURE_EXECUTION, execution_raw),
    ]
    manifest = copy.deepcopy(original)
    manifest["files"].extend(added)
    manifest["expected_current_input_count"] = 82
    manifest["operation"]["consumed_marker"] = NEW_MARKER
    manifest["thread_environment_recovery"] = {
        "kind": "same_scientific_operation_after_zero_math_thread_environment_failure_v1",
        "original_whole_manifest": identity("original_reference_boundary_manifest_readonly", ORIGINAL, raw_original),
        "whole_prior_failure_scientific": added[1], "whole_prior_failure_execution": added[2],
        "prior_run_id": "44742799448", "prior_run_attempt": "1",
        "prior_complete_admission_gates": 19, "prior_completed_scientific_targets": 0,
        "prior_saved_scientific_records": 0, "prior_mathematical_wall_seconds": 0,
        "prior_reference_profile_and_Gram_counters_all_zero": True,
        "required_thread_environment": THREAD_ENV,
        "all_original79_input_identities_unchanged": True,
        "original_owner_math_parameters25_gates39_fields_and_shared_worker_unchanged": True,
        "only_remaining_original_two_targets_are_scheduled": True,
        "no_completed_target_recomputation": True, "automatic_retry_authorized": False,
        "new_marker_preserves_original_consumed_marker": True,
        "scientific_execution_by_metadata_generator": False,
    }
    require(manifest["files"][:79] == original["files"]
            and len(manifest["files"]) == len({x["role"] for x in manifest["files"]}) == 82
            and len({x["path"] for x in manifest["files"]}) == 82,
            "exact old79 plus only generator and two whole failure files")
    for key in original:
        if key not in ("files", "expected_current_input_count", "operation"):
            require(manifest[key] == original[key], "every original non-operations contract unchanged: "+key)
    new_op = copy.deepcopy(manifest["operation"])
    new_op["consumed_marker"] = operation["consumed_marker"]
    require(new_op == operation, "only the consumed-marker location changes in original operation")
    raw = encoded(manifest)
    require(len(raw) < 100000, "one whole small recovery manifest")
    template = workflow_literal((root/by_role["reference_boundary_metadata_generator"]["path"]).read_bytes())
    old_workflow = template.replace("MANIFEST_PATH", ORIGINAL).replace("MANIFEST_SHA", ORIGINAL_SHA)
    require(sha(old_workflow.encode()) == ORIGINAL_WORKFLOW_SHA,
            "old fixed generator reconstructs exactly the original whole workflow")
    workflow = template.replace("MANIFEST_PATH", MANIFEST).replace("MANIFEST_SHA", sha(raw))
    require(workflow.count("group: reference-boundary-lifts-first-v1") == 1
            and workflow.count("          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}\n") == 1,
            "one concurrency group and one worker environment insertion")
    workflow = workflow.replace("group: reference-boundary-lifts-first-v1",
                                "group: reference-boundary-lifts-thread-recovery-v2")
    workflow = workflow.replace("          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}\n",
        "          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}\n"
        "          OPENBLAS_NUM_THREADS: '1'\n"
        "          OMP_NUM_THREADS: '1'\n"
        "          MKL_NUM_THREADS: '1'\n")
    out.mkdir(parents=True, exist_ok=True)
    (out/Path(MANIFEST).name).write_bytes(raw)
    (out/Path(WORKFLOW).name).write_text(workflow)
    print(json.dumps({"manifest_bytes": len(raw), "manifest_sha256": sha(raw),
        "workflow_bytes": len(workflow.encode()), "workflow_sha256": sha(workflow.encode()),
        "current_inputs": 82, "unchanged_original_inputs": 79,
        "historical_inputs": len(manifest["historical_inputs"]),
        "new_remaining_targets": 2, "old_completed_targets_recomputed": 0,
        "worker_sha256": by_role["worker"]["sha256"],
        "recovery_generator_sha256": added[0]["sha256"], "scientific_execution": False}, sort_keys=True))


if __name__ == "__main__":
    main()
