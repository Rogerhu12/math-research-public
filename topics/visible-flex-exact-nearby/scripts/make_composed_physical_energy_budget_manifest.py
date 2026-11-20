#!/usr/bin/env python3
"""Build the R138 composed physical energy input metadata; never run numerical code."""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
from pathlib import Path
import subprocess

TOPIC = "topics/visible-flex-exact-nearby"
REPO = "Rogerhu12/math-research-public"
PREFIX = "2026-11-20-R138-composed-physical-energy-budget"
SOURCE_NAME = "fourfold_codazzi_composed_physical_energy_budget.py"
WORKER_NAME = "fourfold_codazzi_composed_physical_energy_budget_public_worker.py"
GENERATOR_NAME = "make_composed_physical_energy_budget_manifest.py"
HISTORY = "46f127c7153f5393dcd2a00f42d4c1d3662c294d"
POSITIVE_SHA = "ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d"
ANGULAR_SHA = "7a3dd2c1d48b611f5d9a6bd8c2d7ebeeeb4c2f6a7c2bcc4f61f4d012be4e2f90"
GERM_SHA = "397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864"
CANDIDATE_SHA = "ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
SOURCE_SHA = "3fca5cd0b9da843bc8c56128c31f9c307456769952dc0f64b7c3f59f66a1aff1"
PROOF_SHA = "f8a7eb3d190eaf387415c6fa1aaf03249dd6a0bc670f2abfe5d39b696fb58b34"
PRIOR_BUDGET_SHA = "1259c3687cea0af523dd52055e88d5ee9a7b77094c218101835b6c38dfbbc7ec"
PRIOR_EXECUTION_SHA = "999555eafb3c443266f1a8fed98056c9d4f448c0131ef5ffff93941b35040c92"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def blob(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", type=Path, required=True)
    ap.add_argument("--source-dir", type=Path, default=Path(__file__).resolve().parent)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    root, source_dir, out = args.repo.resolve(), args.source_dir.resolve(), args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)

    def git(*parts):
        return subprocess.check_output(["git", *parts], cwd=root, text=True).strip()

    def spec(role, relative, preferred=None):
        source = Path(preferred) if preferred is not None else root / relative
        raw = source.read_bytes()
        if not 0 < len(raw) < 100000:
            raise ValueError("not a complete small current text: " + str(source))
        raw.decode("utf-8")
        if relative.endswith(".py"):
            ast.parse(raw, filename=relative)
        return dict(role=role, path=relative, bytes=len(raw), sha256=sha(raw), git_blob_sha=blob(raw))

    def source_path(name, relative):
        candidate = source_dir / name
        return candidate if candidate.exists() else root / relative

    small = []
    for role, name in (("worker", WORKER_NAME), ("science", SOURCE_NAME),
                       ("metadata_generator", GENERATOR_NAME)):
        relative = TOPIC + "/scripts/" + name
        selected = Path(__file__) if role == "metadata_generator" else source_path(name, relative)
        small.append(spec(role, relative, selected))
    contract = PREFIX + "-contract.md"
    contract_relative = TOPIC + "/notes/" + contract
    small.append(spec("composed_physical_budget_contract", contract_relative, source_path(contract, contract_relative)))
    current = [
        ("reviewed_rules", "notes/2026-11-20-reviewed-public-CI-rules.json"),
        ("composed_physical_feedback_proof", "results/R138-supplement-composed-physical-Hessian-and-smoothing-budget.md"),
        ("completed_X_budget", "notes/physical_energy_budget_ci/run-44737045152-1/physical-energy-conclusion.json"),
        ("completed_X_execution", "notes/physical_energy_budget_ci/run-44737045152-1/execution.json"),
        ("positive_parts_index", "notes/2026-11-14-R133-current-positive-complete-ac1-binary-parts.json"),
        ("angular_parts_index", "notes/2026-11-14-R133-final-complete-angular-defect-parts.json"),
        ("physical_multiplier_budget_proof", "results/R138-supplement-complete-physical-residual-multiplier-budget.md"),
        ("Volterra_Grushin_energy_proof", "results/R138-supplement-Volterra-Grushin-energy-and-root-defect-trace.md"),
        ("exact_residual_transport_proof", "results/R138-supplement-exact-residual-transport-and-fixed-interior-point.md"),
        ("same_repaired_physical_object_proof", "results/R138-supplement-actual-positive-support-for-repaired-physical-frame.md"),
        ("physical_Jacobi_bridge_proof", "results/R138-residual-sensitive-Codazzi-frame-and-geometric-Jacobi-bridge.md"),
        ("original_complete_angular_proof", "results/R133-supplement-complete-angular-model-geometry-from-moving-residual.md"),
        ("exact_continuous_repair_proof", "results/R133-supplement-exact-continuous-repair-of-final-centre.md"),
        ("whole_positive_curvature_proof", "results/R133-supplement-whole-positive-reference-floor-and-cached-producer.md"),
        ("complete_outer_energy_proof", "results/R138-supplement-actual-outer-rotation-energy-and-mean-defect.md"),
    ]
    small.extend(spec(role, TOPIC + "/" + relative) for role, relative in current)
    by_role = {item["role"]: item for item in small}
    review = json.loads((root / by_role["reviewed_rules"]["path"]).read_bytes())
    for path, expected in review["readme_sha256"].items():
        if sha((root / path).read_bytes()) != expected:
            raise ValueError("README differs from the explicit current rule review: " + path)
    if by_role["science"]["sha256"] != SOURCE_SHA or by_role["composed_physical_feedback_proof"]["sha256"] != PROOF_SHA:
        raise ValueError("the fully reviewed new source or complete Y proof changed")

    if (by_role["completed_X_budget"]["sha256"] != PRIOR_BUDGET_SHA
            or by_role["completed_X_execution"]["sha256"] != PRIOR_EXECUTION_SHA):
        raise ValueError("the complete successful X outcome changed")

    originals = []
    for role, expected_sha, expected_rows, expected_bytes in (
            ("positive", POSITIVE_SHA, 4650, 6223338),
            ("angular", ANGULAR_SHA, 7722, 6871825)):
        index = json.loads((root / by_role[role + "_parts_index"]["path"]).read_bytes())
        if (index["original_sha256"] != expected_sha or index["original_bytes"] != expected_bytes
                or not index["native_complete"] or index["native_failure"] is not None
                or index["complete_native_rows"] != expected_rows or len(index["parts"]) != 4):
            raise ValueError("wrong complete existing " + role + " native index")
        for number, part in enumerate(index["parts"]):
            relative = TOPIC + "/notes/" + part["file"]
            originals.append(dict(role="original_" + role + "_part_" + str(number), path=relative,
                                  commit=HISTORY, git_blob_sha=git("rev-parse", HISTORY + ":" + relative),
                                  bytes=part["compressed_bytes"], sha256=part["compressed_sha256"]))
    # Only immutable history metadata is reused, without any old numerical
    # module, W2C context, candidate array, or previously completed target.
    old = json.loads((root / TOPIC / "notes/2026-11-20-centre-mean-floor-inputs.json").read_bytes())
    item = next(x for x in old["historical_inputs"] if x["role"] == "original_signed_intrinsic_root_germ")
    if item["sha256"] != GERM_SHA:
        raise ValueError("wrong accepted root germ")
    copied = {key: item[key] for key in ("path", "commit", "git_blob_sha", "bytes", "sha256")}
    copied["role"] = "original_root_germ"
    originals.append(copied)
    if len(originals) != 9 or len({x["path"] for x in originals}) != 9:
        raise ValueError("incomplete exact nine-object restoration")

    allowed = sorted([
        "identity", "complete", "proved", "failure", "completed_closed_cells",
        "prior_complete_budget", "reused_prior_scalar_paths",
        "old_scientific_target_calls", "old_primitive_calls", "old_geometry_ODE_calls",
        "old_frame_propagation_steps", "old_energy_constant_targets_recomputed",
        "published_Fourier_or_frame_arrays", "scope",
        "new_scalar_suprema", "new_scalar_integrals", "current_exact_left",
        "current_wall_seconds", "complete_derived_energy_bounds", "body_only_sufficient_comparison",
        "stage", "wall_seconds",
    ])
    manifest = dict(
        kind="R138_same_Qrepair_complete_composed_physical_energy_inputs_v1", repository=REPO,
        problem_id="R138_same_Qrepair_composed_physical_energy_budget_v1",
        scientific_kind="R138_same_Qrepair_composed_physical_energy_budget_v1",
        files=small, expected_current_input_count=len(small), historical_inputs=originals,
        accepted_natives=dict(positive=POSITIVE_SHA, angular=ANGULAR_SHA,
                              germ=GERM_SHA, candidate=CANDIDATE_SHA),
        runtime=dict(python="3.12.14", packages={"python-flint": "0.9.0"}),
        parameters=dict(arithmetic_bits=320, physical_period="2*pi", fixed_point="(0,0,1/2)",
                        exact_repair_A0="1/250000000000000000",
                        exact_eta="-7789843107295549/4611686018427387904",
                        exact_nu="-2572625729470897/72057594037927936",
                        true_root_interval=["1191984371497/5000000000000", "2383968743003/10000000000000"],
                        conservative_integration_interval=["1191984371497/5000000000000", "25/8"],
                        original_body_cut="1192029371497/5000000000000",
                        original_positive_rows=4650, original_angular_rows=7722,
                        original_positive_interfaces=3594, original_angular_interfaces=6143,
                        scientific_checkpoint_closed_cells=32,
                        actual_Qrepair_not_WVC_hybrid=True, complete_decimal_bound_readback=True,
                        prior_X_budget_sha256=PRIOR_BUDGET_SHA,
                        prior_X_execution_sha256=PRIOR_EXECUTION_SHA,
                        exact_common_partition_sha256="b86e1b057e14b61d09364dc8dc0969a2650c727104abcdf8d39e67cc9dcd14a6"),
        allowed_scientific_fields=allowed,
        scope=dict(new_target="one complete composed physical feedback budget; all completed X propagation and bounds are read only",
                   mathematical_target_count=1, complete_ordinary_dr_and_true_root_collar=True,
                   full_real_angular_circle=True, all_means_retained=True,
                   old_producer_calls=0, old_completed_targets_recomputed=0,
                   W2C_context_constructed=False, original_array_restoration_only=True,
                   candidate_coefficients_recomputed=False, original_residual_recomputed=False,
                   completed_X_actual_and_execution_read=True,
                   completed_X_propagation_recomputed=False,
                   completed_X_scalar_targets_recomputed=False,
                   mean_denominator_called_or_read=False, axis_coordinates_called_or_read=False,
                   root_boundary_form_constant_paid=False, full_inverse_proved=False,
                   both_original_rhs_solved=False, final_topic_complete=False, new_array_output=False),
        operation=dict(child_timeout_seconds=5400, readme_pull_interval_seconds=1800,
                       topic_maximum_bytes=200000000, reserve_bytes=120000,
                       maximum_total_publication_bytes=100000, maximum_execution_bytes=60000,
                       maximum_scientific_bytes=30000,
                       output_base=TOPIC + "/notes/composed_physical_energy_budget_ci",
                       consumed_marker=TOPIC + "/notes/composed_physical_energy_budget_ci/R138_composed_physical_energy_budget_v1-consumed.json",
                       automatic_scientific_retry=False,
                       first_run_resume=False,
                       publication="complete scalar conclusion or unfinished accumulator prefix, run metadata and hashes only",
                       no_artifacts=True, no_Releases=True, no_new_arrays=True),
    )
    raw = (json.dumps(manifest, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()
    if len(raw) >= 100000:
        raise ValueError("manifest must remain one complete small text")
    filename = PREFIX + "-inputs.json"
    (out / filename).write_bytes(raw)
    workflow = """name: R138 complete composed physical energy budget

on:
  push:
    branches: [main]
    paths:
      - .github/workflows/fourfold-codazzi-composed-physical-energy-budget-public.yml

permissions:
  contents: write

concurrency:
  group: r138-complete-composed-physical-energy-budget-v1
  cancel-in-progress: false

jobs:
  complete-composed-physical-energy:
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
            topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_composed_physical_energy_budget_public_worker.py
            topics/visible-flex-exact-nearby/notes/MANIFEST_NAME
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install the fixed directed runtime
        run: python -m pip install --disable-pip-version-check python-flint==0.9.0
      - name: Restore original bytes and enclose the complete composed physical energy budget
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_composed_physical_energy_budget_public_worker.py --repo "$GITHUB_WORKSPACE" --manifest topics/visible-flex-exact-nearby/notes/MANIFEST_NAME --manifest-sha MANIFEST_SHA
""".replace("MANIFEST_NAME", filename).replace("MANIFEST_SHA", sha(raw))
    (out / "fourfold-codazzi-composed-physical-energy-budget-public.yml").write_text(workflow)
    print(json.dumps(dict(manifest_bytes=len(raw), manifest_sha256=sha(raw),
                          current_inputs=len(small), historical_inputs=len(originals),
                          scientific_source_sha256=by_role["science"]["sha256"],
                          worker_sha256=by_role["worker"]["sha256"],
                          numerical_execution=False), sort_keys=True))


if __name__ == "__main__":
    main()
