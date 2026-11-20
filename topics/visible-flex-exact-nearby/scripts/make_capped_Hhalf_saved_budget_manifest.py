#!/usr/bin/env python3
"""Metadata only: pin five new Hhalf body combinations of whole completed X/Y."""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
PREFIX = "2026-11-20-capped-Hhalf-saved-budget"
SCIENCE = "fourfold_codazzi_capped_Hhalf_saved_budget.py"
WORKER = "fourfold_codazzi_capped_Hhalf_saved_budget_public_worker.py"
GENERATOR = "make_capped_Hhalf_saved_budget_manifest.py"
PROOFS = {
    "capped_Hhalf_Grushin_and_root_allowance_proof":
        "R138-supplement-capped-curvature-Hhalf-Grushin-and-root-budget.md",
    "sharper_outer_lift_and_capped_curvature_proof":
        "R138-supplement-sharper-outer-lift-and-capped-curvature-energy.md",
    "completed_Y_composed_feedback_proof":
        "R138-supplement-composed-physical-Hessian-and-smoothing-budget.md",
    "completed_X_physical_budget_proof":
        "R138-supplement-complete-physical-residual-multiplier-budget.md",
    "original_Grushin_and_root_trace_proof":
        "R138-supplement-Volterra-Grushin-energy-and-root-defect-trace.md",
    "exact_residual_transport_proof":
        "R138-supplement-exact-residual-transport-and-fixed-interior-point.md",
    "complete_outer_energy_and_mean_proof":
        "R138-supplement-actual-outer-rotation-energy-and-mean-defect.md",
    "whole_positive_curvature_proof":
        "R133-supplement-whole-positive-reference-floor-and-cached-producer.md",
}


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

    science_path = choose(SCIENCE, TOPIC + "/scripts/" + SCIENCE)
    tree = ast.parse(science_path.read_bytes())
    definitions = {node.targets[0].id: node.value for node in tree.body
                   if isinstance(node, ast.Assign) and len(node.targets) == 1
                   and isinstance(node.targets[0], ast.Name)}
    parameters = ast.literal_eval(definitions["PARAMETERS"])
    target_order = ast.literal_eval(definitions["RECORD_NAMES"])
    conditional_target = ast.literal_eval(definitions["OPTIONAL_RECORD_NAME"])
    inputs = ast.literal_eval(definitions["INPUTS"])
    old_specs = ast.literal_eval(definitions["OLD"])
    kind = ast.literal_eval(definitions["KIND"])
    fields_node = definitions["SCI_FIELDS"]
    if not (isinstance(fields_node, ast.Call) and isinstance(fields_node.func, ast.Name)
            and fields_node.func.id == "sorted" and len(fields_node.args) == 1):
        raise ValueError("literal declared scientific field list")
    fields = sorted(ast.literal_eval(fields_node.args[0]))
    if len(target_order) != 5 or conditional_target in target_order or len(inputs) != 4:
        raise ValueError("five new body targets, one conditional root lower, four whole old files")

    files = []
    for role, name in (("worker", WORKER), ("science", SCIENCE), ("metadata_generator", GENERATOR)):
        relative = TOPIC + "/scripts/" + name
        selected = Path(__file__) if role == "metadata_generator" else choose(name, relative)
        files.append(spec(role, relative, selected))
    contract = PREFIX + "-contract.md"
    relative = TOPIC + "/notes/" + contract
    files.append(spec("new_capped_Hhalf_scalar_contract", relative, choose(contract, relative)))
    files.append(spec("reviewed_rules", TOPIC + "/notes/2026-11-20-reviewed-public-CI-rules.json"))
    for role, expected in inputs.items():
        item = spec(role, TOPIC + "/" + expected["path"])
        if item["sha256"] != expected["sha256"] or item["bytes"] != expected["bytes"]:
            raise ValueError("the entire accepted completed X/Y file: " + role)
        files.append(item)
    for role, name in PROOFS.items():
        relative = TOPIC + "/results/" + name
        files.append(spec(role, relative, choose(name, relative)))
    if len({item["role"] for item in files}) != len(files) or len({item["path"] for item in files}) != len(files):
        raise ValueError("all complete input roles and paths must be unique")
    by_role = {item["role"]: item for item in files}
    for label in ("X", "Y"):
        old = json.loads((root / by_role["completed_" + label + "_budget"]["path"]).read_bytes())
        execution = json.loads((root / by_role["completed_" + label + "_execution"]["path"]).read_bytes())
        prior = old_specs[label]
        if (old["complete"] is not True or old["proved"] is not True or old["failure"] is not None
                or old["completed_closed_cells"] != 4651 or old["stage"] != prior["stage"]
                or old["identity"]["source_sha256"] != prior["source_sha256"]
                or execution["complete"] is not True or execution["failure"] is not None
                or execution["original_scientific_complete"] is not True
                or execution["actual_child_returncode"] != 0 or execution["run_id"] != prior["run_id"]
                or execution["run_attempt"] != "1" or execution["manifest_sha256"] != prior["manifest_sha256"]):
            raise ValueError("whole successful original X/Y metadata")
    review = json.loads((root / by_role["reviewed_rules"]["path"]).read_bytes())
    for relative, expected in review["readme_sha256"].items():
        if sha((root / relative).read_bytes()) != expected:
            raise ValueError("README differs from the current explicit review: " + relative)
    manifest = {
        "kind": "R138_capped_Hhalf_saved_body_budget_inputs_v1", "repository": REPO,
        "problem_id": "R138_capped_Hhalf_saved_body_budget_first_v1", "scientific_kind": kind,
        "files": files, "expected_current_input_count": len(files), "historical_inputs": [],
        "runtime": {"python": "3.12.14", "packages": {"python-flint": "0.9.0"}},
        "fixed_runtime_qualification": {"same_as_completed_source_runs": ["44737045152/1", "44740320925/1"],
            "new_dependency": False, "primary_documentation": "https://python-flint.readthedocs.io/en/stable/arb.html"},
        "parameters": parameters, "target_order": target_order, "conditional_target": conditional_target,
        "allowed_scientific_fields": fields,
        "scope": {"mandatory_new_mathematical_targets": 5, "conditional_new_lower_target": 1,
            "whole_original_XY_actual_and_execution_retained": True,
            "whole_original_XY_false_gates_retained": True, "all_means_retained": True,
            "old_root_Htwo_thirds_path_and_rE_rB_unchanged": True,
            "old_completed_target_calls": 0, "old_scientific_source_imports": 0,
            "new_numerical_ODE_or_integral_calls": 0, "native_or_array_restoration": False,
            "actual_root_form_constant_paid": False, "full_positive_inverse_proved": False,
            "either_original_RHS_proved": False, "final_topic_proved": False},
        "operation": {"child_timeout_seconds": 900, "readme_pull_interval_seconds": 1800,
            "topic_maximum_bytes": 200000000, "reserve_bytes": 120000,
            "maximum_total_publication_bytes": 100000, "maximum_execution_bytes": 60000,
            "maximum_scientific_bytes": 30000,
            "output_base": TOPIC + "/notes/capped_Hhalf_saved_budget_ci",
            "consumed_marker": TOPIC + "/notes/capped_Hhalf_saved_budget_ci/capped_Hhalf_saved_budget_first_v1-consumed.json",
            "automatic_scientific_retry": False, "first_run_resume": False,
            "publication": "five whole body bounds and optional root lower, or incomplete prefix, with complete hashes",
            "no_artifacts": True, "no_Releases": True, "no_new_arrays": True}}
    raw = (json.dumps(manifest, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode()
    if len(raw) >= 100000:
        raise ValueError("complete small manifest")
    filename = PREFIX + "-inputs.json"
    (out / filename).write_bytes(raw)
    workflow = """name: Capped Hhalf saved body budget

on:
  push:
    branches: [main]
    paths:
      - .github/workflows/fourfold-codazzi-capped-Hhalf-saved-budget-public.yml

permissions:
  contents: write

concurrency:
  group: capped-Hhalf-saved-body-budget-v1
  cancel-in-progress: false

jobs:
  complete-new-body-bounds:
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
      - name: Consume whole completed X and Y scalar budgets
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          python topics/visible-flex-exact-nearby/scripts/WORKER_NAME --repo "$GITHUB_WORKSPACE" --manifest topics/visible-flex-exact-nearby/notes/MANIFEST_NAME --manifest-sha MANIFEST_SHA
""".replace("WORKER_NAME", WORKER).replace("MANIFEST_NAME", filename).replace("MANIFEST_SHA", sha(raw))
    (out / "fourfold-codazzi-capped-Hhalf-saved-budget-public.yml").write_text(workflow)
    print(json.dumps({"manifest_bytes": len(raw), "manifest_sha256": sha(raw),
        "current_inputs": len(files), "historical_inputs": 0, "mandatory_new_targets": len(target_order),
        "conditional_new_target": conditional_target,
        "science_sha256": by_role["science"]["sha256"], "worker_sha256": by_role["worker"]["sha256"],
        "numerical_execution": False}, sort_keys=True))


if __name__ == "__main__":
    main()
