#!/usr/bin/env python3
"""Metadata only: pin four new scalar combinations of completed GH evidence."""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
PREFIX = "2026-11-20-actual-GH-saved-response"
SCIENCE = "fourfold_codazzi_actual_GH_saved_response.py"
WORKER = "fourfold_codazzi_actual_GH_saved_response_public_worker.py"
GENERATOR = "make_actual_GH_saved_response_manifest.py"
OLD_MANIFEST = "notes/2026-11-20-actual-GH-source-fees-inputs.json"
OLD_MANIFEST_SHA = "69449ea01bbdfc202d6a6c763661a13f42efdcb08303fd356b1b32dc2f09887f"
OLD_ACTUAL = "notes/actual_GH_source_fees_ci/run-44736533396-1/actual-scientific-conclusion.json"
OLD_ACTUAL_SHA = "e7766bc9e1a714456fa224b9dc69171ba119626bf62ffce2437d43dcd80924d6"
OLD_EXECUTION = "notes/actual_GH_source_fees_ci/run-44736533396-1/execution.json"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def blob(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--source-dir", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    root, source, out = args.repo.resolve(), args.source_dir.resolve(), args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)

    def choose(name, relative):
        preferred = source / name
        return preferred if preferred.exists() else root / relative

    def spec(role, relative, selected=None):
        path = selected if selected is not None else root / relative
        raw = path.read_bytes()
        if not 0 < len(raw) < 100000:
            raise ValueError("one complete small input: " + str(path))
        raw.decode("utf-8")
        if relative.endswith(".py"):
            ast.parse(raw, filename=relative)
        return {"role": role, "path": relative, "bytes": len(raw),
                "sha256": sha(raw), "git_blob_sha": blob(raw)}

    files = []
    for role, name in (("worker", WORKER), ("science", SCIENCE), ("metadata_generator", GENERATOR)):
        relative = TOPIC + "/scripts/" + name
        selected = Path(__file__) if role == "metadata_generator" else choose(name, relative)
        files.append(spec(role, relative, selected))
    contract = PREFIX + "-contract.md"
    contract_relative = TOPIC + "/notes/" + contract
    files.append(spec("new_four_scalar_contract", contract_relative, choose(contract, contract_relative)))
    old_manifest_raw = (root / TOPIC / OLD_MANIFEST).read_bytes()
    if sha(old_manifest_raw) != OLD_MANIFEST_SHA:
        raise ValueError("the exact already successful five-source manifest")
    old_manifest = json.loads(old_manifest_raw)
    original = {item["role"]: item for item in old_manifest["files"]}
    review_item = old_manifest["reviewed_rules"]
    files.append(spec("reviewed_rules", review_item["path"]))
    for role, rel in (("completed_five_sources", OLD_ACTUAL),
                      ("completed_five_sources_execution", OLD_EXECUTION),
                      ("completed_five_sources_manifest", OLD_MANIFEST)):
        files.append(spec(role, TOPIC + "/" + rel))
    role_map = {"original_high_admission": "actual_GH_source_fees_math",
                "base0_summary": "completed_actual_base0_high_summary",
                "base0_process": "completed_actual_base0_high_process",
                "negative_summary": "negative_one_summary", "negative_process": "negative_one_process",
                "original_strong_source_proof": "proof_actual_base0_high_source_window",
                "original_rough_source_proof": "proof_actual_negative_one_high_source_window"}
    for role, old_role in role_map.items():
        prior = original[old_role]
        item = spec(role, prior["path"])
        if any(item[key] != prior[key] for key in ("bytes", "sha256", "git_blob_sha")):
            raise ValueError("changed whole completed original object: " + old_role)
        files.append(item)
    files.append(spec("actual_GH_source_window_contract", TOPIC +
        "/results/R141-supplement-actual-GH-source-window-and-return-contract.md"))
    if len({item["role"] for item in files}) != len(files) or len({item["path"] for item in files}) != len(files):
        raise ValueError("all input roles and paths must be unique")
    by_role = {item["role"]: item for item in files}
    if by_role["completed_five_sources"]["sha256"] != OLD_ACTUAL_SHA:
        raise ValueError("the exact completed original five directed records")
    old = json.loads((root / TOPIC / OLD_ACTUAL).read_bytes())
    execution = json.loads((root / TOPIC / OLD_EXECUTION).read_bytes())
    if (not old["complete"] or not old["proved"] or old["failure"] is not None
            or old["saved_record_count"] != 5 or old["actual_returncode"] != 0
            or not execution["scientific_complete"] or execution["actual_child_returncode"] != 0):
        raise ValueError("whole completed original scalar sources and execution")
    review = json.loads((root / by_role["reviewed_rules"]["path"]).read_bytes())
    for relative, expected in review["readme_sha256"].items():
        if sha((root / relative).read_bytes()) != expected:
            raise ValueError("README differs from the current explicit review: " + relative)
    tree = ast.parse(choose(SCIENCE, TOPIC + "/scripts/" + SCIENCE).read_bytes())
    definitions = {node.targets[0].id: node.value for node in tree.body
                   if isinstance(node, ast.Assign) and len(node.targets) == 1
                   and isinstance(node.targets[0], ast.Name)}
    parameters = ast.literal_eval(definitions["PARAMETERS"])
    target_order = ast.literal_eval(definitions["RECORD_NAMES"])
    fields_node = definitions["SCI_FIELDS"]
    if not (isinstance(fields_node, ast.Call) and isinstance(fields_node.func, ast.Name)
            and fields_node.func.id == "sorted" and len(fields_node.args) == 1):
        raise ValueError("literal declared scientific field list")
    fields = sorted(ast.literal_eval(fields_node.args[0]))
    kind = ast.literal_eval(definitions["KIND"])
    manifest = {
        "kind": "actual_GH_saved_head_response_inputs_v1", "repository": REPO,
        "problem_id": "actual_GH_saved_head_response_first_v1", "scientific_kind": kind,
        "files": files, "expected_current_input_count": len(files), "historical_inputs": [],
        "runtime": {"python": "3.12.14", "packages": {"python-flint": "0.9.0"}},
        "fixed_runtime_qualification": {"same_as_completed_source_run": "44736533396/1",
            "new_dependency": False, "primary_documentation": "https://python-flint.readthedocs.io/en/stable/arb.html"},
        "parameters": parameters, "target_order": target_order, "allowed_scientific_fields": fields,
        "scope": {"new_mathematical_targets": 4, "whole_original_five_source_records_retained": True,
            "all_original_high_response_rows_and_seven_ports_retained": True,
            "original_exterior_mean_and_affine_rows_retained": True,
            "old_completed_target_calls": 0, "coefficient_context_or_Green_action_calls": 0,
            "native_or_array_restoration": False, "actual_internal_inverse_proved": False,
            "actual_physical_outer_rows_proved": False, "original_finite_rho_bridge_proved": False,
            "either_original_RHS_proved": False, "final_topic_proved": False},
        "operation": {"child_timeout_seconds": 900, "readme_pull_interval_seconds": 1800,
            "topic_maximum_bytes": 200000000, "reserve_bytes": 120000,
            "maximum_total_publication_bytes": 100000, "maximum_execution_bytes": 60000,
            "maximum_scientific_bytes": 30000,
            "output_base": TOPIC + "/notes/actual_GH_saved_response_ci",
            "consumed_marker": TOPIC + "/notes/actual_GH_saved_response_ci/actual_GH_saved_response_first_v1-consumed.json",
            "automatic_scientific_retry": False, "first_run_resume": False,
            "publication": "whole four scalar conclusions or incomplete prefix with execution and complete hashes",
            "no_artifacts": True, "no_Releases": True, "no_new_arrays": True}}
    raw = (json.dumps(manifest, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode()
    if len(raw) >= 100000:
        raise ValueError("complete small manifest")
    filename = PREFIX + "-inputs.json"
    (out / filename).write_bytes(raw)
    workflow = """name: Actual GH saved head response

on:
  push:
    branches: [main]
    paths:
      - .github/workflows/fourfold-codazzi-actual-GH-saved-response-public.yml

permissions:
  contents: write

concurrency:
  group: actual-GH-saved-head-response-v1
  cancel-in-progress: false

jobs:
  complete-four-responses:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-latest
    timeout-minutes: 45
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
            topics/visible-flex-exact-nearby/scripts/WORKER_NAME
            topics/visible-flex-exact-nearby/notes/MANIFEST_NAME
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install the same completed directed runtime
        run: python -m pip install --disable-pip-version-check python-flint==0.9.0
      - name: Consume complete source and high-response scalars
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          python topics/visible-flex-exact-nearby/scripts/WORKER_NAME --repo "$GITHUB_WORKSPACE" --manifest topics/visible-flex-exact-nearby/notes/MANIFEST_NAME --manifest-sha MANIFEST_SHA
""".replace("WORKER_NAME", WORKER).replace("MANIFEST_NAME", filename).replace("MANIFEST_SHA", sha(raw))
    (out / "fourfold-codazzi-actual-GH-saved-response-public.yml").write_text(workflow)
    print(json.dumps({"manifest_bytes": len(raw), "manifest_sha256": sha(raw),
        "current_inputs": len(files), "historical_inputs": 0, "new_targets": len(target_order),
        "science_sha256": by_role["science"]["sha256"], "worker_sha256": by_role["worker"]["sha256"],
        "numerical_execution": False}, sort_keys=True))


if __name__ == "__main__":
    main()
