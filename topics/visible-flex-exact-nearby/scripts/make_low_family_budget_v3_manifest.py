#!/usr/bin/env python3
"""Metadata-only continuation of the original three unfinished L records.

No scientific module is imported and no scientific quantity is recalculated.
The v2 manifest and both zero-record failure receipts remain unchanged.  The
completed mean-atom diagnostic is a read-only input, never the selected entry.
"""

from __future__ import annotations

import argparse
import ast
import copy
import hashlib
import json
from pathlib import Path


TOPIC = "topics/visible-flex-exact-nearby"
BASE = f"{TOPIC}/notes/2026-11-20-low-family-budget-v2-inputs.json"
BASE_SHA = "309dab6c3318322f45a98bc674b0c0e2ae2c2abd5f869cfb6d8e53f627b6bae9"
FINAL = f"{TOPIC}/notes/2026-11-20-low-family-budget-v3-inputs.json"
WORKFLOW = ".github/workflows/fourfold-codazzi-low-family-budget-public.yml"
REFERENCE = f"{TOPIC}/scripts/fourfold_codazzi_W2C_signed_reference_math.py"
REFERENCE_SHA = "e57e0953fd6d0d9cf0f79a85189bc611b474f3fc06c57ac88862ac9b0455a8d8"
PROOF = f"{TOPIC}/results/R139-supplement-positive-reference-pivot-and-endpoint-hull.md"
PROOF_SHA = "0c33b852df668b39af354c1d435850af4a26bd00c21a10ab54682b33ff5e9a1c"
FAILED = f"{TOPIC}/notes/low_family_budget_ci/run-44719196440-1"
ATOM = f"{TOPIC}/notes/low_family_atom_floor_ci/run-44721682192-1/actual-scientific-conclusion.json"
OLD_MARKERS = (
    f"{TOPIC}/notes/low_family_budget_ci/W2C_low_family_budget_v1-consumed.json",
    f"{TOPIC}/notes/low_family_budget_ci/W2C_low_family_budget_v2_remaining3-consumed.json",
    f"{TOPIC}/notes/low_family_atom_floor_ci/W2C_mean_atom_floor_v1-consumed.json",
)
NEW_MARKER = f"{TOPIC}/notes/low_family_budget_ci/W2C_low_family_budget_v3_remaining3-consumed.json"
TARGET = "complete_low_family_feedback_necessary_budget"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def pin(repo, path, role, expected_sha=None):
    data = (repo / path).read_bytes()
    data.decode("utf-8")
    require(len(data) < 100000, f"complete input below 100KB: {path}")
    digest = sha256(data)
    require(expected_sha is None or digest == expected_sha, f"fixed input bytes: {path}")
    header = f"blob {len(data)}\0".encode("ascii")
    return {
        "bytes": len(data),
        "git_blob_sha": hashlib.sha1(header + data).hexdigest(),
        "path": path,
        "role": role,
        "sha256": digest,
    }


def read_json(repo, path):
    return json.loads((repo / path).read_text(encoding="utf-8"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True,
                        help="independent metadata output directory")
    args = parser.parse_args()
    repo, out = args.repo.resolve(), args.out.resolve()
    require(out != repo and repo not in out.parents,
            "generate in independent scratch; root integrates explicitly")
    old_manifest = pin(repo, BASE, "prior_zero_scalar_v2_manifest", BASE_SHA)
    base = read_json(repo, BASE)
    manifest = copy.deepcopy(base)
    require(len(base["files"]) == base["expected_current_input_count"] == 65,
            "fixed complete v2 input inventory")
    old_reference = next(s for s in base["scientific_modules"]
                         if s["role"] == "reference_math")
    new_reference = pin(repo, REFERENCE, "reference_math", REFERENCE_SHA)
    for spec in base["files"]:
        if spec["role"] != "reference_math":
            require(pin(repo, spec["path"], spec["role"]) == spec,
                    f"retain every other original current input: {spec['role']}")
    require(pin(repo, base["worker"]["path"], "worker") == base["worker"],
            "retain original shared worker bytes")
    for group in (manifest["files"], manifest["scientific_modules"]):
        reference_indices = [i for i, s in enumerate(group) if s["role"] == "reference_math"]
        require(len(reference_indices) == 1, "one current complete reference module")
        group[reference_indices[0]] = copy.deepcopy(new_reference)
    # Only these current module references change.  Historical 1ec6/6aa0
    # reference pins in the earlier continuation remain historical verbatim.
    extra_specs = [
        pin(repo, PROOF, "reference_positive_pivot_inclusion_proof", PROOF_SHA),
        pin(repo, f"{FAILED}/actual-scientific-conclusion.json", "second_zero_scalar_failure",
            "e4cdba135faa1d19ee90263b1c05dfa4506275d6fa9f992e1456a8ddb4336b1d"),
        pin(repo, f"{FAILED}/execution.json", "second_zero_scalar_execution",
            "8c2d5884ac925fbd98ff49465e4dd651d87432ea775f4af6a8e4f5309baa78ae"),
        pin(repo, ATOM, "completed_mean_atom_floor_actual",
            "c51d21c18ebad81b7966590a38aa00b04b9602a9687f3dddb45bb15f495871da"),
    ]
    failed = read_json(repo, extra_specs[1]["path"])
    execution = read_json(repo, extra_specs[2]["path"])
    require(failed["run_id"] == execution["run_id"] == "44719196440"
            and failed["run_attempt"] == execution["run_attempt"] == "1",
            "complete second failed public attempt")
    require(failed["kind"] == base["operation"]["scientific_kind"]
            and failed["complete"] is False
            and failed["actual_returncode"] == 1
            and failed["saved_record_count"] == 0
            and failed["new_records"] == {}
            and failed["completed_targets"] == []
            and failed["current_target"] == TARGET
            and execution["scientific_complete"] is False
            and execution["actual_child_returncode"] == 1,
            "second failure saved no original scientific target or scalar")
    atom = read_json(repo, ATOM)
    require(atom["run_id"] == "44721682192" and atom["run_attempt"] == "1"
            and atom["kind"] == "W2C_low_family_mean_atom_floor_diagnostic_v1"
            and atom["complete"] is True and atom["actual_returncode"] == 0
            and atom["saved_record_count"] == 3
            and atom["completed_targets"] == ["complete_low_family_mean_atom_necessary_floor"]
            and set(atom["new_records"]) == {
                "complete_low_family_atom_column_floor",
                "complete_low_family_atom_row_floor",
                "complete_low_family_atom_squared_norm_floor"},
            "completed separate mean-atom diagnostic retained whole")
    require(atom["parent_candidate_complete"] is False
            and atom["finite_gate"] is None
            and atom["conditional_finite_inverse"] is None
            and atom["necessary_budget"]["fixed_recipe_rejection_proved"] is False
            and atom["necessary_budget"]["original_low_family_three_records_computed"] == 0
            and atom["necessary_budget"]["parent_scalar_records_computed"] == 0,
            "atom success is neither original L completion nor parent gate")
    retained_markers = [pin(repo, path, f"retained_consumed_marker_{i + 1}")
                        for i, path in enumerate(OLD_MARKERS)]
    require(not (repo / NEW_MARKER).exists(), "v3 continuation has not been consumed")
    manifest["files"].extend(extra_specs)
    manifest["expected_current_input_count"] = len(manifest["files"])
    require(len({s["role"] for s in manifest["files"]}) == 69
            and len({s["path"] for s in manifest["files"]}) == 69,
            "69 distinct complete current input paths and roles")
    manifest["operation"]["consumed_marker"] = NEW_MARKER
    manifest["positive_reference_pivot_continuation"] = {
        "kind": "proved_positive_reference_pivot_remaining_three_continuation_v1",
        "previous_run_id": "44719196440",
        "previous_attempt": "1",
        "previous_status": "failure",
        "previous_manifest": old_manifest,
        "old_reference": old_reference,
        "new_reference": new_reference,
        "inclusion_proof": extra_specs[0],
        "complete_prior_receipts": extra_specs[1:3],
        "completed_original_low_family_records": 0,
        "remaining_original_low_family_records": 3,
        "original_private_reference_parents_prepared": 153,
        "original_private_comparison_panels_prepared": 155,
        "private_context_can_be_rematerialized_for_unfinished_targets": True,
        "all_original_mathematical_definitions_and_parameters_retained": True,
        "original_diagnostic_owner_and_three_target_names_unchanged": True,
        "previous_zero_endpoint_continuation_retained_verbatim": True,
        "completed_scientific_targets_recomputed": 0,
        "automatic_retry_of_old_run": False,
        "retained_old_consumed_markers": retained_markers,
        "new_consumed_marker": NEW_MARKER,
    }
    manifest["completed_mean_atom_floor_readonly_input"] = {
        "complete_actual": extra_specs[3],
        "completed_independent_lower_records": 3,
        "original_low_family_records_computed": 0,
        "original_parent_50_records_computed": 0,
        "fixed_recipe_rejection_proved": False,
        "failed_atom_rejection_is_not_a_passed_finite_gate": True,
        "atom_entry_selected_or_called": False,
        "completed_atom_records_recomputed": 0,
        "retained_consumed_marker": OLD_MARKERS[2],
    }
    require(manifest["diagnostic_contract"] == base["diagnostic_contract"]
            and manifest["parameters"] == base["parameters"]
            and manifest["operation"]["scientific_entry_role"] == "low_family_budget_diagnostic"
            and manifest["operation"]["ordered_targets"] == [TARGET],
            "original complete diagnostic target and parent contract unchanged")
    restored_operation = copy.deepcopy(manifest["operation"])
    restored_operation["consumed_marker"] = base["operation"]["consumed_marker"]
    require(restored_operation == base["operation"], "only continuation marker changes operation")
    require(manifest["reference_representation_continuation"]
            == base["reference_representation_continuation"], "v1-to-v2 history unchanged")
    for spec in manifest["scientific_modules"]:
        ast.parse((repo / spec["path"]).read_text(encoding="utf-8"), filename=spec["path"])
    owner = next(s for s in manifest["files"] if s["role"] == "low_family_budget_diagnostic")
    ast.parse((repo / owner["path"]).read_text(encoding="utf-8"), filename=owner["path"])
    encoded = (json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
    require(len(encoded) < 100000, "complete new metadata below 100KB")
    digest = sha256(encoded)
    workflow = (repo / WORKFLOW).read_text(encoding="utf-8")
    require(workflow.count(BASE) == 2 and workflow.count(BASE_SHA) == 1
            and workflow.count("r139-w2c-low-family-budget-v2") == 1,
            "update only the existing budget workflow")
    workflow = (workflow.replace(BASE, FINAL).replace(BASE_SHA, digest)
                .replace("r139-w2c-low-family-budget-v2", "r139-w2c-low-family-budget-v3")
                .replace("name: R139 complete low-family necessary-budget diagnostic",
                         "name: R139 complete low-family remaining-three continuation")
                .replace("name: Compute one complete low-family budget diagnostic",
                         "name: Continue the three unfinished low-family records"))
    out.mkdir(parents=True, exist_ok=True)
    manifest_output = out / Path(FINAL).name
    workflow_output = out / Path(WORKFLOW).name
    manifest_output.write_bytes(encoded)
    workflow_output.write_text(workflow, encoding="utf-8")
    print(json.dumps({
        "manifest": str(manifest_output), "manifest_bytes": len(encoded),
        "manifest_sha256": digest, "workflow": str(workflow_output),
        "current_input_count": len(manifest["files"]),
        "reference_sha256": new_reference["sha256"],
        "owner_unchanged_sha256": owner["sha256"],
        "worker_unchanged_sha256": manifest["worker"]["sha256"],
        "original_L_records_completed": 0, "original_L_records_remaining": 3,
        "successful_atom_records_recomputed": 0,
        "scientific_modules_imported": 0,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
