#!/usr/bin/env python3
"""Freeze the first low193 endpoint diagnostic's public metadata and workflow.

Metadata only: source literals are read through AST, and input bytes are
hashed.  No scientific module is imported, no old outcome is recomputed,
and no git operation or shared-repository mutation is performed here.
The caller supplies the two output paths and copies reviewed files to git.
"""
import argparse
import ast
import copy
import hashlib
import json
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
BASE_MANIFEST = TOPIC + "/notes/2026-11-20-W2C-native-readonly-inputs.json"
MANIFEST_PATH = TOPIC + "/notes/2026-11-20-low193-endpoint-diagnostic-inputs.json"
WORKFLOW_PATH = ".github/workflows/fourfold-codazzi-low193-endpoint-diagnostic-public.yml"
WORKER_PATH = TOPIC + "/scripts/fourfold_codazzi_collar_volterra_dual_public_worker.py"
OWNER_PATH = TOPIC + "/scripts/fourfold_codazzi_low_centre_endpoint_owner.py"
MATH_PATH = TOPIC + "/scripts/fourfold_codazzi_low_centre_endpoint_diagnostic.py"
PROOF_PATH = TOPIC + "/results/R137-continuous-signed-centre-and-exact-endpoint-system.md"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def identity(role, path, raw):
    require(0 < len(raw) < 100000, "one complete small input: " + path)
    raw.decode("utf-8")
    return {"role": role, "path": path, "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest(),
            "git_blob_sha": hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()}


def literal_assignments(raw, requested):
    """Evaluate only literal data and string concatenation in source AST."""
    tree = ast.parse(raw.decode("utf-8"))
    known = {}

    def literal(node):
        if isinstance(node, ast.Name) and node.id in known:
            return known[node.id]
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
            left, right = literal(node.left), literal(node.right)
            require(isinstance(left, str) and isinstance(right, str), "literal string concatenation")
            return left + right
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                and isinstance(node.func.value, ast.Name) and node.func.value.id == "json"
                and node.func.attr == "loads" and len(node.args) == 1 and not node.keywords):
            return json.loads(ast.literal_eval(node.args[0]))
        return ast.literal_eval(node)

    for node in tree.body:
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        target = node.targets[0]
        if not isinstance(target, ast.Name):
            continue
        try:
            known[target.id] = literal(node.value)
        except (ValueError, TypeError, SyntaxError):
            if target.id in requested:
                raise
    require(set(requested) <= set(known), "all requested complete source literals")
    return {name: known[name] for name in requested}


def encode(value):
    return (json.dumps(value, ensure_ascii=False, allow_nan=False,
                       sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--base-manifest", default=BASE_MANIFEST)
    parser.add_argument("--owner-source")
    parser.add_argument("--manifest-out", required=True)
    parser.add_argument("--workflow-out", required=True)
    args = parser.parse_args()
    root = Path(args.repo).resolve()
    base_path = Path(args.base_manifest)
    if not base_path.is_absolute():
        base_path = root / base_path
    require(base_path.resolve().is_relative_to(root), "base metadata in repository")
    base_raw = base_path.read_bytes()
    manifest = json.loads(base_raw)
    require(manifest["repository"] == "Rogerhu12/math-research-public"
            and manifest["kind"] == "complete_collar_Volterra_dual_current_inputs_v1"
            and manifest["problem_id"] == "W2C_complete_collar_Volterra_dual_candidate_v1",
            "same whole W2C admission and mathematical input contract")
    original_files = copy.deepcopy(manifest["files"])
    by_role = {item["role"]: item for item in original_files}
    owner_raw = (Path(args.owner_source) if args.owner_source else root / OWNER_PATH).read_bytes()
    constants = literal_assignments(owner_raw, {
        "SOURCE_PATH", "KIND", "ENTRY_ROLE", "MATH_ROLE", "TARGET", "RUNTIME",
        "DIAGNOSTIC_PARAMETERS", "GATE_SUFFIX", "SCI_FIELDS"})
    require(constants["SOURCE_PATH"] == OWNER_PATH
            and constants["DIAGNOSTIC_PARAMETERS"]["endpoint_matrix_dimension"] == 97
            and constants["SCI_FIELDS"] == sorted(constants["SCI_FIELDS"]),
            "whole distinct low193/97 owner metadata")
    helper = literal_assignments((root / by_role["science"]["path"]).read_bytes(),
                                 {"ADMISSION_GATE_LABELS", "PARAMETERS", "RETAINED_SCOPE"})
    require(manifest["parameters"] == helper["PARAMETERS"]
            and manifest["retained_scope"] == helper["RETAINED_SCOPE"]
            and manifest["parameters"]["complete_new_scalar_targets"] == 50,
            "entire old parameter and physical-scope objects remain unchanged")
    replacements = {}
    for role in ("assembly_math", "worker", "rules"):
        spec = by_role[role]
        replacements[role] = identity(role, spec["path"], (root / spec["path"]).read_bytes())
    for spec in original_files:
        now = identity(spec["role"], spec["path"], (root / spec["path"]).read_bytes())
        if spec["role"] not in replacements:
            require(now == spec, "whole immutable original/current input: " + spec["role"])

    def replace(value):
        if isinstance(value, dict):
            if set(value) == {"role", "path", "bytes", "sha256", "git_blob_sha"}:
                role = value["role"]
                if role in replacements:
                    require(value == by_role[role], "consistent original source pin")
                    return copy.deepcopy(replacements[role])
            return {key: replace(item) for key, item in value.items()}
        if isinstance(value, list):
            return [replace(item) for item in value]
        return value

    manifest = replace(manifest)
    entry = identity(constants["ENTRY_ROLE"], OWNER_PATH, owner_raw)
    math_source = identity(constants["MATH_ROLE"], MATH_PATH, (root / MATH_PATH).read_bytes())
    proof = identity("proof_R137_continuous_endpoint", PROOF_PATH, (root / PROOF_PATH).read_bytes())
    ast.parse((root / MATH_PATH).read_text(), filename=MATH_PATH)
    manifest["files"].extend((entry, math_source, proof))
    manifest["expected_current_input_count"] = len(manifest["files"])
    require(len({item["role"] for item in manifest["files"]}) == len(manifest["files"])
            and len({item["path"] for item in manifest["files"]}) == len(manifest["files"]),
            "unique whole source roles and paths")
    require([item["role"] for item in manifest["scientific_modules"]] == [
        "science", "readonly_admission", "readonly_core", "collar_math", "kernel_math",
        "assembly_math", "reference_math"], "original complete seven-module admission contract")
    manifest.pop("readonly_diagnostic_contract", None)
    manifest.pop("active_workflow_scope_audit", None)
    manifest["diagnostic_contract"] = {
        "proof": proof, "target": constants["TARGET"],
        "same_current_WVC_candidate_and_all_original_admission_retained": True,
        "full_high_feedback_and_all_actual_remainders_unpaid": True,
        "all193_original_observation_atoms_and_both_RHS_remain_obligations": True,
        "complete_finite_Qf_rho_bridge_unpaid": True,
        "midpoint_comparison_is_not_an_actual_centre_certificate": True,
        "original_609_endpoint_equivalence_not_numerically_evaluated_here": True,
        "new_rule12_administrative_approval_gate_added": False,
    }
    manifest["fixed_runtime_primary_sources"] = {
        "checked_UTC_date": "2026-11-20",
        "numpy_2_3_5_python_support": "https://numpy.org/doc/stable/release/2.3.5-notes.html",
        "scipy_1_16_3_release": "https://docs.scipy.org/doc/scipy/release/1.16.3-notes.html",
        "scipy_python_numpy_compatibility": "https://docs.scipy.org/doc/scipy/dev/toolchain.html",
        "numpy_cp312_linux_wheel": "https://pypi.org/project/numpy/2.3.5/",
        "scipy_cp312_linux_wheel": "https://pypi.org/project/scipy/1.16.3/",
        "claim": "Both fixed releases exist, support the declared Python/NumPy combination, and publish CPython3.12 Linux x86_64 wheels.",
    }
    scope = copy.deepcopy(manifest["retained_scope"])
    scope.update({
        "new_low193_midpoint_comparison_only": True,
        "full_physical_mean_in_low193_and_terminal_row": True,
        "low193_true_centre_inverse_not_proved": True,
        "full_high_feedback_and_family_remainder_unpaid": True,
        "whole193_atoms_and_both_original_RHS_not_certified_by_matching_angles": True,
        "finite_radial_projection_and_rho_normalizer_not_bypassed": True,
        "full609_endpoint_system_not_evaluated": True,
        "old_completed_scientific_targets_recomputed": False,
    })
    op = manifest["operation"]
    op.update({
        "scientific_entry_role": constants["ENTRY_ROLE"],
        "scientific_kind": constants["KIND"],
        "scientific_module_binding": manifest["scientific_modules"] + [entry, math_source],
        "ordered_targets": [constants["TARGET"]], "complete_target_counts": [1],
        "complete_gate_names": helper["ADMISSION_GATE_LABELS"] + constants["GATE_SUFFIX"],
        "scientific_field_names": constants["SCI_FIELDS"],
        "diagnostic_parameters": constants["DIAGNOSTIC_PARAMETERS"],
        "fixed_runtime": constants["RUNTIME"], "retained_scope": scope,
        "readonly_diagnostic_only": False,
        "consumed_marker": TOPIC + "/notes/low193_endpoint_diagnostic_ci/WVC_low193_endpoint_midpoint_v1-consumed.json",
        "output_base": TOPIC + "/notes/low193_endpoint_diagnostic_ci",
        "scientific_filename": "actual-scientific-conclusion.json",
        "child_timeout_seconds": 5400,
    })
    op.pop("concurrent_workflow_scope_bindings", None)
    op.pop("concurrent_pending_run_reservations", None)
    manifest["publication_budget_model"] = {
        "full_scientific_cap": op["maximum_scientific_bytes"],
        "full_execution_cap": op["maximum_execution_bytes"],
        "full_report_cap": op["maximum_report_bytes"], "full_marker_cap": 4000,
        "complete_total_publication_bound": op["maximum_total_publication_bytes"],
        "preflight_and_immediate_child_reserve": op["reserve_bytes"],
        "actual_postpublication_reserve_required": False,
        "one_full_floating_diagnostic_in_scientific_output": True,
        "private_diagnostic_prefix_cap": constants["DIAGNOSTIC_PARAMETERS"]["maximum_private_diagnostic_bytes"],
        "coefficient_and_frame_arrays_published": False,
        "complete_actual_UTF8_output_bytes_checked_before_publication": True,
    }
    raw = encode(manifest)
    require(len(raw) < 100000, "one complete small UTF8 manifest")
    digest = hashlib.sha256(raw).hexdigest()
    workflow = """name: R137 full low193 endpoint midpoint diagnostic

on:
  push:
    branches: [main]
    paths:
      - .github/workflows/fourfold-codazzi-low193-endpoint-diagnostic-public.yml

permissions:
  contents: write

concurrency:
  group: r137-wvc-low193-endpoint-midpoint-v1
  cancel-in-progress: false

jobs:
  complete-low193-endpoint-diagnostic:
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
      - name: Install fixed published Arb and floating runtimes
        run: python -m pip install --disable-pip-version-check --only-binary=:all: python-flint==0.9.0 numpy==2.3.5 scipy==1.16.3
      - name: Admit original inputs and compute one complete low193 diagnostic
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          OPENBLAS_NUM_THREADS: '1'
          OMP_NUM_THREADS: '1'
          MKL_NUM_THREADS: '1'
        run: |
          python WORKER_PATH --repo "$GITHUB_WORKSPACE" --manifest MANIFEST_PATH --manifest-sha MANIFEST_SHA
""".replace("WORKER_PATH", WORKER_PATH).replace("MANIFEST_PATH", MANIFEST_PATH).replace("MANIFEST_SHA", digest)
    for path, content in ((Path(args.manifest_out), raw),
                          (Path(args.workflow_out), workflow.encode("utf-8"))):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
    print(json.dumps({"manifest_path": MANIFEST_PATH, "manifest_bytes": len(raw),
        "manifest_sha256": digest, "workflow_path": WORKFLOW_PATH,
        "input_count": len(manifest["files"]), "admission_modules": 7,
        "complete_source_binding_modules": len(op["scientific_module_binding"]),
        "new_targets": 1, "parent_parameter_scalar_targets_retained": 50,
        "new_owner": entry, "new_diagnostic_math": math_source,
        "current_worker": replacements["worker"],
        "local_scientific_targets_evaluated": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
