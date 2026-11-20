#!/usr/bin/env python3
"""Metadata-only inputs for one new complete centre-mean LOWER certificate.

Retain all72 current inputs of the completed original L v4 run, add the
new owner/proof and its whole completed actual as a read-only input.  No
scientific module is imported; no completed L, atom or endpoint target is
called.  Generate in independent scratch for root's explicit integration.
"""
import argparse
import ast
import copy
import hashlib
import json
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
BASE = TOPIC + "/notes/2026-11-20-low-family-budget-v4-inputs.json"
BASE_SHA = "382cbdc96a44d990113609d352388ecce3f42f04041620d1134eaec6d43e38be"
OWNER = TOPIC + "/scripts/fourfold_codazzi_centre_mean_floor_diagnostic.py"
PROOF = TOPIC + "/results/R139-supplement-complete-joint-centre-mean-atom-lower-bound.md"
PROOF_SHA = "b69206d087a7fb9867bfc71b6df552fa5c25418917360f7dfde5c3f13217738a"
COMPLETE_L = TOPIC + "/notes/low_family_budget_ci/run-44724797559-1/actual-scientific-conclusion.json"
COMPLETE_L_SHA = "81b3bdc14a213b5b6b3400f69df2e87492641ab8d07722ff775ba55e310ff0a9"
MANIFEST = TOPIC + "/notes/2026-11-20-centre-mean-floor-inputs.json"
WORKFLOW = ".github/workflows/fourfold-codazzi-centre-mean-floor-public.yml"
WORKER = TOPIC + "/scripts/fourfold_codazzi_collar_volterra_dual_public_worker.py"
MARKER = TOPIC + "/notes/centre_mean_floor_ci/W2C_centre_mean_floor_v1-consumed.json"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def identity(role, path, raw, expected_sha=None):
    raw.decode("utf-8")
    require(0 < len(raw) < 100000, "small complete UTF8 input: " + path)
    digest = hashlib.sha256(raw).hexdigest()
    require(expected_sha is None or digest == expected_sha, "fixed complete input: " + path)
    return {"role": role, "path": path, "bytes": len(raw), "sha256": digest,
            "git_blob_sha": hashlib.sha1(b"blob " + str(len(raw)).encode()
                                        + b"\0" + raw).hexdigest()}


def literals(raw, requested):
    values = {}
    for node in ast.parse(raw).body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            target = node.targets[0]
            if isinstance(target, ast.Name) and target.id in requested:
                value = node.value
                if (isinstance(value, ast.Call) and isinstance(value.func, ast.Attribute)
                        and isinstance(value.func.value, ast.Name)
                        and value.func.value.id == "json" and value.func.attr == "loads"
                        and len(value.args) == 1 and not value.keywords):
                    values[target.id] = json.loads(ast.literal_eval(value.args[0]))
                else:
                    values[target.id] = ast.literal_eval(value)
    require(set(values) == set(requested), "all requested literal source constants")
    return values


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--owner", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    root, out = args.repo.resolve(), args.out.resolve()
    require(out != root and root not in out.parents,
            "metadata generated in independent scratch")
    base_raw = (root / BASE).read_bytes()
    base_spec = identity("completed_original_L_manifest", BASE, base_raw, BASE_SHA)
    manifest = json.loads(base_raw)
    require(manifest["parameters"]["complete_new_scalar_targets"] == 50
            and manifest["expected_current_input_count"] == len(manifest["files"]) == 72,
            "unchanged complete72 input and fifty-target parent contract")
    original_files = copy.deepcopy(manifest["files"])
    by_role = {x["role"]: x for x in original_files}
    for spec in original_files:
        require(identity(spec["role"], spec["path"],
                         (root / spec["path"]).read_bytes()) == spec,
                "retain every original current input: " + spec["role"])
    require(identity("worker", WORKER, (root / WORKER).read_bytes()) == manifest["worker"],
            "same complete public worker")
    owner_path = args.owner.resolve() if args.owner else root / OWNER
    owner_raw = owner_path.read_bytes()
    constants = literals(owner_raw, {"DIAGNOSTIC_ROLE", "SOURCE_PATH", "PROOF_ROLE",
        "PROOF_PATH", "KIND", "TARGET", "RECORD_NAMES", "ADDITIONAL_GATE_LABELS",
        "DIAGNOSTIC_SCOPE", "SCI_FIELDS"})
    require(constants["SOURCE_PATH"] == OWNER and constants["PROOF_PATH"] == PROOF
            and len(constants["RECORD_NAMES"]) == 1
            and constants["DIAGNOSTIC_SCOPE"]["new_scalar_targets"] == 1,
            "one independent all155 centre-mean lower owner")
    helper = literals((root / by_role["science"]["path"]).read_bytes(),
                      {"ADMISSION_GATE_LABELS"})
    extras = [
        identity(constants["DIAGNOSTIC_ROLE"], OWNER, owner_raw),
        identity(constants["PROOF_ROLE"], PROOF, (root / PROOF).read_bytes(), PROOF_SHA),
        identity("completed_original_low_family_actual", COMPLETE_L,
                 (root / COMPLETE_L).read_bytes(), COMPLETE_L_SHA),
    ]
    complete_L = json.loads((root / COMPLETE_L).read_bytes())
    require(complete_L["kind"] == "W2C_low_family_necessary_budget_diagnostic_v1"
            and complete_L["complete"] is True and complete_L["actual_returncode"] == 0
            and complete_L["run_id"] == "44724797559" and complete_L["run_attempt"] == "1"
            and complete_L["saved_record_count"] == 3
            and len(complete_L["new_records"]) == 3
            and complete_L["completed_targets"] == ["complete_low_family_feedback_necessary_budget"]
            and complete_L["parent_candidate_complete"] is False
            and complete_L["finite_gate"] is None
            and complete_L["conditional_finite_inverse"] is None,
            "whole successful original L actual retained without recomputation")
    require(not (root / MARKER).exists(), "new independent centre-mean target not consumed")
    manifest["files"].extend(extras)
    require(len({x["path"] for x in manifest["files"]}) == 75
            and len({x["role"] for x in manifest["files"]}) == 75,
            "75 distinct complete input roles and paths")
    manifest["expected_current_input_count"] = 75
    manifest["diagnostic_contract"] = constants["DIAGNOSTIC_SCOPE"]
    manifest["independent_centre_mean_floor_contract"] = {
        "completed_original_L_manifest": base_spec,
        "completed_original_L_actual": extras[2],
        "original_L_scalar_records_frozen": 3,
        "remaining_parent_scalar_records_not_computed_here": 47,
        "new_independent_scalar_records": 1,
        "new_target_is_not_a_retry_of_any_failed_or_successful_old_target": True,
        "all_prior_markers_and_failures_and_successes_retained": True,
        "old_L_atom_and_endpoint_targets_called_or_recomputed": 0,
        "same_all72_admitted_inputs_and_original_context": True,
        "source_is_complete_signed_mean_entry_not_a_positive_fee": True,
        "root_mean_atom_is_unchanged_by_original_finite_receiver_Pf": True,
        "source_domain_is_ordinary_L2_not_a_finite_radial_input_space": True,
        "true_panel_length_lower_and_reference_q_upper_required": True,
        "all155_panels_before_one_saved_lower_record": True,
        "only_saved_record_lower_is_compared_to_exact_1_over_16384": True,
        "no_midpoint_values_or_upper_norms_used_as_lower_bounds": True,
        "proof": extras[1],
    }
    op = manifest["operation"]
    op.update({"scientific_entry_role": constants["DIAGNOSTIC_ROLE"],
        "scientific_kind": constants["KIND"], "ordered_targets": [constants["TARGET"]],
        "complete_target_counts": [1],
        "complete_gate_names": helper["ADMISSION_GATE_LABELS"] + constants["ADDITIONAL_GATE_LABELS"],
        "scientific_field_names": sorted(constants["SCI_FIELDS"]),
        "consumed_marker": MARKER,
        "output_base": TOPIC + "/notes/centre_mean_floor_ci",
        "child_timeout_seconds": 5400})
    manifest["publication_budget_model"]["parent_scalar_records_computed"] = 0
    raw = (json.dumps(manifest, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"), allow_nan=False) + "\n").encode()
    require(len(raw) < 100000, "small complete centre-mean input manifest")
    digest = hashlib.sha256(raw).hexdigest()
    workflow = """name: R139 complete centre-mean necessary floor

on:
  push:
    branches: [main]
    paths:
      - WORKFLOW_PATH

permissions:
  contents: write

concurrency:
  group: r139-w2c-centre-mean-floor-v1
  cancel-in-progress: false

jobs:
  complete-centre-mean-necessary-floor:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-latest
    timeout-minutes: 120
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
          filter: blob:none
          persist-credentials: false
          sparse-checkout-cone-mode: false
          sparse-checkout: |
            README.md
            topics/visible-flex-exact-nearby/README.md
            WORKER_PATH
            MANIFEST_PATH
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install fixed directed runtime
        run: python -m pip install --disable-pip-version-check python-flint==0.9.0
      - name: Compute one complete signed centre-mean lower certificate
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          python WORKER_PATH --repo "$GITHUB_WORKSPACE" --manifest MANIFEST_PATH --manifest-sha MANIFEST_SHA
""".replace("WORKFLOW_PATH", WORKFLOW).replace("WORKER_PATH", WORKER).replace(
        "MANIFEST_PATH", MANIFEST).replace("MANIFEST_SHA", digest)
    out.mkdir(parents=True, exist_ok=True)
    (out / Path(MANIFEST).name).write_bytes(raw)
    (out / Path(WORKFLOW).name).write_text(workflow)
    print(json.dumps({"manifest": str(out / Path(MANIFEST).name),
        "sha256": digest, "bytes": len(raw), "current_inputs": 75,
        "new_lower_records": 1, "parent_records_computed_here": 0,
        "original_L_success_records_frozen": 3,
        "owner_sha256": extras[0]["sha256"], "owner_bytes": extras[0]["bytes"],
        "proof_sha256": extras[1]["sha256"], "scientific_imports_or_calls": 0}, indent=2))


if __name__ == "__main__":
    main()
