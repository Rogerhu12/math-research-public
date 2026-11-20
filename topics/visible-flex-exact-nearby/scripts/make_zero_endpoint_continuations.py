#!/usr/bin/env python3
"""Metadata-only continuation of two failed, zero-result public diagnostics.

Reads complete saved failure records; imports no scientific or numeric code.
The old manifests, markers and failures remain immutable.  Only the proved
reference interval representation is changed in the mathematical module pins.
"""
import argparse
import copy
import hashlib
import json
import subprocess
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
PROOF = TOPIC + "/results/R139-supplement-certified-zero-endpoint-interval-continuation.md"
REFERENCE = TOPIC + "/scripts/fourfold_codazzi_W2C_signed_reference_math.py"
FAILURE_BASE = TOPIC + "/notes/low_family_budget_ci/run-44716804300-1/"
BASE_COMMIT = "3731c70d223185aaafa76815924609747d175cf9"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def identity(role, path, raw):
    raw.decode("utf-8")
    require(0 < len(raw) < 100000, "complete small UTF8 input: " + path)
    return {"role": role, "path": path, "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest(),
            "git_blob_sha": hashlib.sha1(b"blob " + str(len(raw)).encode()
                                        + b"\0" + raw).hexdigest()}


def encode(value):
    return (json.dumps(value, ensure_ascii=False, allow_nan=False,
                       sort_keys=True, separators=(",", ":")) + "\n").encode()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True)
    args = parser.parse_args()
    root = Path(args.repo).resolve()
    failure_path = FAILURE_BASE + "actual-scientific-conclusion.json"
    execution_path = FAILURE_BASE + "execution.json"
    failure = json.loads((root / failure_path).read_bytes())
    execution = json.loads((root / execution_path).read_bytes())
    require(failure["run_id"] == "44716804300" and not failure["complete"]
            and failure["saved_record_count"] == 0 and failure["new_records"] == {}
            and failure["completed_targets"] == []
            and failure["failure"]["message"] == "true nonnegative segment length"
            and not execution["scientific_complete"],
            "preserved actual failure contains no completed new scalar target")
    new_reference = identity("reference_math", REFERENCE, (root / REFERENCE).read_bytes())
    proof = identity("reference_zero_endpoint_inclusion_proof", PROOF,
                     (root / PROOF).read_bytes())
    jobs = [
        ("low-family-budget", "fourfold-codazzi-low-family-budget-public.yml",
         "W2C_low_family_budget_v2_remaining3-consumed.json"),
        ("low193-endpoint-diagnostic", "fourfold-codazzi-low193-endpoint-diagnostic-public.yml",
         "WVC_low193_endpoint_midpoint_v2-consumed.json"),
    ]
    summaries = []
    for stem, workflow_name, marker_name in jobs:
        old_path = TOPIC + "/notes/2026-11-20-" + stem + "-inputs.json"
        new_path = TOPIC + "/notes/2026-11-20-" + stem + "-v2-inputs.json"
        old_raw = (root / old_path).read_bytes()
        old = json.loads(old_raw)
        old_reference = next(x for x in old["files"] if x["role"] == "reference_math")
        for spec in old["files"]:
            if spec["role"] != "reference_math":
                require(identity(spec["role"], spec["path"],
                                 (root / spec["path"]).read_bytes()) == spec,
                        "unchanged complete current input: " + spec["role"])

        def replace(value):
            if isinstance(value, dict):
                if value == old_reference:
                    return copy.deepcopy(new_reference)
                return {key: replace(item) for key, item in value.items()}
            if isinstance(value, list):
                return [replace(item) for item in value]
            return value

        new = replace(old)
        new["files"].append(proof)
        continuation = {
            "kind": "proved_zero_endpoint_representation_continuation_v1",
            "old_manifest": identity("prior_failed_manifest", old_path, old_raw),
            "old_reference": old_reference, "new_reference": new_reference,
            "inclusion_proof": proof,
            "all_original_mathematical_definitions_and_parameters_retained": True,
            "completed_scientific_targets_recomputed": 0,
            "automatic_retry_of_old_run": False,
        }
        if stem == "low-family-budget":
            saved = [identity("prior_zero_scalar_failure", failure_path,
                              (root / failure_path).read_bytes()),
                     identity("prior_zero_scalar_execution", execution_path,
                              (root / execution_path).read_bytes())]
            new["files"].extend(saved)
            continuation.update({
                "previous_run_id": "44716804300", "previous_attempt": "1",
                "previous_status": "failure", "complete_prior_receipts": saved,
                "completed_new_records": 0, "remaining_new_records": 3,
                "original_private_reference_parents_prepared": 153,
                "original_private_comparison_panels_prepared": 155,
                "private_context_can_be_rematerialized_for_unfinished_targets": True,
                "old_failure_and_consumed_marker_retained": True,
            })
        else:
            continuation.update({
                "previous_run_id": "44717190551", "previous_attempt": "1",
                "previous_head_sha": BASE_COMMIT,
                "previous_status": "failure", "previous_jobs": 0,
                "previous_scientific_children": 0,
                "failure_cause": "YAML plain scalar contains colon followed by space",
                "job_list_checked_via_public_GitHub_API": True,
                "reference_repair_shared_before_first_scientific_child": True,
                "diagnostic_remains_unproved_midpoint_model_only": True,
            })
        new["reference_representation_continuation"] = continuation
        new["expected_current_input_count"] = len(new["files"])
        new["operation"]["consumed_marker"] = (
            new["operation"]["output_base"] + "/" + marker_name)
        require(new["parameters"] == old["parameters"]
                and new["retained_scope"] == old["retained_scope"]
                and new["diagnostic_contract"] == old["diagnostic_contract"],
                "unchanged full mathematical scope and diagnostic target")
        require(len({x["role"] for x in new["files"]}) == len(new["files"]),
                "unique complete input roles")
        raw = encode(new)
        require(len(raw) < 100000, "small complete continuation manifest")
        destination = root / new_path
        require(not destination.exists() or destination.read_bytes() == raw,
                "never overwrite different frozen continuation")
        destination.write_bytes(raw)
        workflow_path = ".github/workflows/" + workflow_name
        workflow = subprocess.check_output(
            ["git", "show", BASE_COMMIT + ":" + workflow_path], cwd=root).decode()
        workflow = workflow.replace(old_path, new_path).replace(
            hashlib.sha256(old_raw).hexdigest(), hashlib.sha256(raw).hexdigest())
        workflow = workflow.replace("-v1\n", "-v2\n")
        workflow = workflow.replace(
            "        run: python -m pip install --disable-pip-version-check --only-binary=:all: ",
            "        run: |\n          python -m pip install --disable-pip-version-check --only-binary=:all: ")
        (root / workflow_path).write_text(workflow)
        summaries.append({"manifest": new_path, "bytes": len(raw),
                          "sha256": hashlib.sha256(raw).hexdigest(),
                          "complete_current_inputs": len(new["files"]),
                          "workflow": workflow_path})
    print(json.dumps({"new_reference": new_reference, "continuations": summaries},
                     ensure_ascii=False))


if __name__ == "__main__":
    main()
