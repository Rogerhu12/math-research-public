#!/usr/bin/env python3
"""Metadata only: original three unfinished L records after positive products.

No scientific import or old target evaluation.  Prior manifests and all
success/failure records are read-only; only current assembly bytes change.
"""
from __future__ import annotations

import argparse
import ast
import copy
import hashlib
import json
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
BASE = f"{TOPIC}/notes/2026-11-20-low-family-budget-v3-inputs.json"
BASE_SHA = "09b8c0d042c73c57e95b178919a09deb624074afdb3d44499b8650ac8bf85007"
FINAL = f"{TOPIC}/notes/2026-11-20-low-family-budget-v4-inputs.json"
ASSEMBLY = f"{TOPIC}/scripts/fourfold_codazzi_collar_dual_feedback_math.py"
ASSEMBLY_SHA = "af84dcfdad6d959f6113d83ee201401014e3ba53e4995d2e0a084fdec320e92d"
PROOF = f"{TOPIC}/results/R139-supplement-directed-upper-products-for-complete-Green-comparison.md"
FAILED = f"{TOPIC}/notes/low_family_budget_ci/run-44723722475-1"
WORKFLOW = ".github/workflows/fourfold-codazzi-low-family-budget-public.yml"
MARKER = f"{TOPIC}/notes/low_family_budget_ci/W2C_low_family_budget_v4_remaining3-consumed.json"


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def pin(repo, path, role, expected=None):
    data = (repo/path).read_bytes()
    data.decode("utf-8")
    digest = hashlib.sha256(data).hexdigest()
    require(len(data) < 100000 and (expected is None or digest == expected),
            f"complete fixed current text: {path}")
    return {"path": path, "role": role, "bytes": len(data), "sha256": digest,
            "git_blob_sha": hashlib.sha1(f"blob {len(data)}\0".encode()+data).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    repo, out = args.repo.resolve(), args.out.resolve()
    require(repo != out and repo not in out.parents, "independent metadata scratch output")
    old_manifest = pin(repo, BASE, "prior_zero_scalar_v3_manifest", BASE_SHA)
    base = json.loads((repo/BASE).read_text())
    require(len(base["files"]) == base["expected_current_input_count"] == 69,
            "entire original v3 inventory")
    current = copy.deepcopy(base)
    assembly = pin(repo, ASSEMBLY, "assembly_math", ASSEMBLY_SHA)
    old_assembly = next(s for s in base["scientific_modules"] if s["role"] == "assembly_math")
    for spec in base["files"]:
        if spec["role"] != "assembly_math":
            require(pin(repo, spec["path"], spec["role"]) == spec,
                    f"every other original current input unchanged: {spec['role']}")
    require(pin(repo, base["worker"]["path"], "worker") == base["worker"],
            "original shared worker unchanged")
    for group in (current["files"], current["scientific_modules"]):
        indices = [i for i, s in enumerate(group) if s["role"] == "assembly_math"]
        require(len(indices) == 1, "one complete assembly role")
        group[indices[0]] = copy.deepcopy(assembly)
    extra = [
        pin(repo, PROOF, "reference_positive_product_inclusion_proof"),
        pin(repo, f"{FAILED}/actual-scientific-conclusion.json", "third_zero_scalar_failure",
            "3bb5b0912b7d0fa418ced7074e7b0e19a4ba07a458d9c37e55ed06dda52bc09a"),
        pin(repo, f"{FAILED}/execution.json", "third_zero_scalar_execution",
            "53e9c468ced57040c3e58bd514aab6f328155f9dcf584ca94597ac87c5bb6840"),
    ]
    failed = json.loads((repo/extra[1]["path"]).read_text())
    execution = json.loads((repo/extra[2]["path"]).read_text())
    require(failed["run_id"] == execution["run_id"] == "44723722475"
            and failed["run_attempt"] == execution["run_attempt"] == "1",
            "actual third failed attempt")
    require(failed["complete"] is False and failed["actual_returncode"] == 1
            and failed["saved_record_count"] == 0 and failed["new_records"] == {}
            and failed["completed_targets"] == []
            and failed["current_target"] == "complete_low_family_feedback_necessary_budget"
            and execution["scientific_complete"] is False
            and execution["actual_child_returncode"] == 1
            and execution["current_input_receipts"] == base["files"],
            "whole third failure has no completed original scalar")
    require(failed["failure"]["message"] == "nonnegative square root",
            "actual positive-product representation failure")
    old_marker = pin(repo, base["operation"]["consumed_marker"], "retained_v3_consumed_marker")
    require(not (repo/MARKER).exists(), "new v4 marker not consumed")
    current["files"].extend(extra)
    current["expected_current_input_count"] = 72
    current["operation"]["consumed_marker"] = MARKER
    current["positive_product_continuation"] = {
        "kind": "complete_nonnegative_upper_products_remaining_three_v1",
        "previous_manifest": old_manifest,
        "previous_run_id": "44723722475", "previous_attempt": "1",
        "previous_status": "failure", "complete_prior_receipts": extra[1:],
        "inclusion_proof": extra[0], "old_assembly": old_assembly,
        "new_assembly": assembly, "old_consumed_marker": old_marker,
        "new_consumed_marker": MARKER,
        "completed_original_low_family_records": 0,
        "remaining_original_low_family_records": 3,
        "original_diagnostic_owner_and_three_target_names_unchanged": True,
        "signed_centre_kernel_and_context_unchanged": True,
        "complete_positive_formulas_and_all193_atoms_retained": True,
        "all_old_reference_continuation_objects_retained_verbatim": True,
        "completed_mean_atom_and_endpoint_targets_recomputed": 0,
        "private_context_can_be_rematerialized_for_unfinished_targets": True,
        "automatic_retry_of_old_run": False,
    }
    require(len({s["role"] for s in current["files"]}) == 72
            and len({s["path"] for s in current["files"]}) == 72,
            "complete distinct72 inventory")
    operation = copy.deepcopy(current["operation"])
    operation["consumed_marker"] = base["operation"]["consumed_marker"]
    require(operation == base["operation"], "only new consumed marker changes operation")
    for key in base:
        if key not in {"files", "expected_current_input_count", "operation", "scientific_modules"}:
            require(current[key] == base[key], f"retain entire original contract: {key}")
    for spec in current["scientific_modules"]:
        ast.parse((repo/spec["path"]).read_text(), filename=spec["path"])
    data = (json.dumps(current, ensure_ascii=False, sort_keys=True, indent=2)+"\n").encode()
    require(len(data) < 100000, "complete new manifest below100KB")
    digest = hashlib.sha256(data).hexdigest()
    workflow = (repo/WORKFLOW).read_text()
    require(workflow.count(BASE) == 2 and workflow.count(BASE_SHA) == 1
            and workflow.count("r139-w2c-low-family-budget-v3") == 1,
            "exact existing original-budget workflow")
    workflow = workflow.replace(BASE, FINAL).replace(BASE_SHA, digest).replace(
        "r139-w2c-low-family-budget-v3", "r139-w2c-low-family-budget-v4")
    out.mkdir(parents=True, exist_ok=True)
    (out/Path(FINAL).name).write_bytes(data)
    (out/Path(WORKFLOW).name).write_text(workflow)
    print(json.dumps({"manifest_bytes": len(data), "manifest_sha256": digest,
        "current_input_count": 72, "assembly_sha256": ASSEMBLY_SHA,
        "original_L_records_remaining": 3, "scientific_modules_imported": 0}, indent=2))


if __name__ == "__main__":
    main()
