#!/usr/bin/env python3
"""Build R138 axis metadata only; never import or execute numerical modules."""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
from pathlib import Path
import subprocess

TOPIC = "topics/visible-flex-exact-nearby"
REPO = "Rogerhu12/math-research-public"
PREFIX = "2026-11-20-R138-root-axis-support"
SOURCE_NAME = "fourfold_codazzi_root_axis_support.py"
WORKER_NAME = "fourfold_codazzi_root_axis_support_public_worker.py"
GENERATOR_NAME = "make_root_axis_support_manifest.py"
POSITIVE_COMMIT = "46f127c7153f5393dcd2a00f42d4c1d3662c294d"
POSITIVE_SHA = "ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d"
GERM_SHA = "397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864"
CANDIDATE_SHA = "ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"


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
    small.append(spec("axis_contract", contract_relative, source_path(contract, contract_relative)))
    current = [
        ("reviewed_rules", "notes/2026-11-20-reviewed-public-CI-rules.json"),
        ("positive_parts_index", "notes/2026-11-14-R133-current-positive-complete-ac1-binary-parts.json"),
        ("candidate_index", "data/phase_transport_resume127_20261114/candidate/moving-m32-alpha0765-fullR-v2-tol2e9-candidate.json"),
        ("physical_support_proof", "results/R138-supplement-actual-positive-support-for-repaired-physical-frame.md"),
        ("fixed_interior_point_proof", "results/R138-supplement-exact-residual-transport-and-fixed-interior-point.md"),
        ("root_axis_and_angular_proof", "results/R138-supplement-complete-root-angular-form-and-two-scalar-geometry.md"),
        ("whole_positive_curvature_bound", "results/R133-supplement-whole-positive-reference-floor-and-cached-producer.md"),
    ]
    small.extend(spec(role, TOPIC + "/" + relative) for role, relative in current)
    by_role = {item["role"]: item for item in small}
    review = json.loads((root / by_role["reviewed_rules"]["path"]).read_bytes())
    for path, expected in review["readme_sha256"].items():
        if sha((root / path).read_bytes()) != expected:
            raise ValueError("README differs from the explicit current rule review: " + path)
    index = json.loads((root / by_role["positive_parts_index"]["path"]).read_bytes())
    if index["original_sha256"] != POSITIVE_SHA or index["original_bytes"] != 6223338:
        raise ValueError("wrong complete positive native index")
    if by_role["candidate_index"]["sha256"] != CANDIDATE_SHA:
        raise ValueError("wrong original complete candidate")
    originals = []
    for number, part in enumerate(index["parts"]):
        relative = TOPIC + "/notes/" + part["file"]
        originals.append(dict(role="original_positive_part_" + str(number), path=relative,
                              commit=POSITIVE_COMMIT,
                              git_blob_sha=git("rev-parse", POSITIVE_COMMIT + ":" + relative),
                              bytes=part["compressed_bytes"], sha256=part["compressed_sha256"]))
    # This previous metadata is only a source of already checked history paths;
    # the new child does not import, run, or rebuild any W2C numerical context.
    old = json.loads((root / TOPIC / "notes/2026-11-20-centre-mean-floor-inputs.json").read_bytes())
    for number in range(5):
        item = next(x for x in old["historical_inputs"]
                    if x["role"] == "original_candidate_part_" + str(number).zfill(3))
        copied = {key: item[key] for key in ("path", "commit", "git_blob_sha", "bytes", "sha256")}
        copied["role"] = "original_candidate_part_" + str(number)
        originals.append(copied)
    item = next(x for x in old["historical_inputs"] if x["role"] == "original_signed_intrinsic_root_germ")
    if item["sha256"] != GERM_SHA:
        raise ValueError("wrong accepted root germ")
    copied = {key: item[key] for key in ("path", "commit", "git_blob_sha", "bytes", "sha256")}
    copied["role"] = "original_root_germ"
    originals.append(copied)
    if len(originals) != 10:
        raise ValueError("incomplete exact ten-object restoration")
    allowed = sorted([
        "identity", "complete", "failure", "completed_original_rows", "axis_projection_count",
        "current_axis_piece", "nominal_q", "nominal_s", "axis_error", "old_target_or_primitive_calls",
        "old_geometry_ODE_calls", "scope", "current_left", "seconds", "proved",
        "true_root_support_coordinates", "complete_axis_error", "root_collar_fee",
        "original_root_collar_K_bound", "exact_repair_fee", "same_global_fixed_support_lower",
        "root_axis_q_negative", "root_axis_s_positive",
    ])
    manifest = dict(
        kind="R138_same_physical_anchor_root_axis_inputs_v1", repository=REPO,
        problem_id="R138_same_physical_root_axis_two_scalars_v1",
        scientific_kind="R138_same_physical_anchor_true_root_axis_support_v1",
        files=small, expected_current_input_count=len(small), historical_inputs=originals,
        accepted_natives=dict(positive=POSITIVE_SHA, germ=GERM_SHA, candidate=CANDIDATE_SHA),
        runtime=dict(python="3.12.14", packages={"python-flint": "0.9.0", "numpy": "2.3.5"}),
        parameters=dict(arithmetic_bits=320, physical_axis="phi=theta=0",
                        fixed_interior_point="(0,0,1/2)", exact_repair_C0="1/250000000000000000",
                        exact_eta="-7789843107295549/4611686018427387904",
                        exact_nu="-2572625729470897/72057594037927936",
                        true_root_interval=["1191984371497/5000000000000", "2383968743003/10000000000000"],
                        original_body_cut="1192029371497/5000000000000", outer_endpoint="25/8",
                        original_rows=4650, original_candidate_shape=[4, 6144, 65],
                        scientific_checkpoint_rows=64, same_complete_physical_outer_anchor=True),
        allowed_scientific_fields=allowed,
        scope=dict(new_target="two support coordinates of the repaired physical frame at its true root",
                   old_producer_calls=0, old_completed_targets_recomputed=0, W2C_context_constructed=False,
                   candidate_definition_restoration_only=True, full_original_positive_rows_retained=True,
                   exact_original_root_germ_used_without_new_intrinsic_evaluation=True,
                   full_root_interval_and_paid_repair_retained=True,
                   full_root_angular_denominator_proved=False, full_root_energy_positive=False,
                   full_inverse_proved=False, final_topic_complete=False, new_array_output=False),
        operation=dict(child_timeout_seconds=5400, readme_pull_interval_seconds=1800,
                       topic_maximum_bytes=200000000, reserve_bytes=120000,
                       maximum_total_publication_bytes=100000, maximum_execution_bytes=85000,
                       maximum_scientific_bytes=16000,
                       output_base=TOPIC + "/notes/root_axis_support_ci",
                       consumed_marker=TOPIC + "/notes/root_axis_support_ci/R138_axis_two_scalars_v1-consumed.json",
                       automatic_scientific_retry=False,
                       publication="complete small scalar conclusion or unfinished prefix, run metadata and hashes only",
                       no_artifacts=True, no_Releases=True, no_new_arrays=True),
    )
    raw = (json.dumps(manifest, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()
    if len(raw) >= 100000:
        raise ValueError("manifest must remain one complete small text")
    filename = PREFIX + "-inputs.json"
    (out / filename).write_bytes(raw)
    workflow = """name: R138 same-anchor root-axis support

on:
  push:
    branches: [main]
    paths:
      - .github/workflows/fourfold-codazzi-root-axis-support-public.yml

permissions:
  contents: write

concurrency:
  group: r138-root-axis-two-scalars-v1
  cancel-in-progress: false

jobs:
  two-scalar-root-axis:
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
            topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_root_axis_support_public_worker.py
            topics/visible-flex-exact-nearby/notes/MANIFEST_NAME
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install the fixed directed runtime
        run: python -m pip install --disable-pip-version-check python-flint==0.9.0 numpy==2.3.5
      - name: Restore original bytes and enclose two new root-axis coordinates
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_root_axis_support_public_worker.py --repo "$GITHUB_WORKSPACE" --manifest topics/visible-flex-exact-nearby/notes/MANIFEST_NAME --manifest-sha MANIFEST_SHA
""".replace("MANIFEST_NAME", filename).replace("MANIFEST_SHA", sha(raw))
    (out / "fourfold-codazzi-root-axis-support-public.yml").write_text(workflow)
    print(json.dumps(dict(manifest_bytes=len(raw), manifest_sha256=sha(raw),
                          current_inputs=len(small), historical_inputs=len(originals),
                          scientific_source_sha256=by_role["science"]["sha256"],
                          worker_sha256=by_role["worker"]["sha256"],
                          numerical_execution=False), sort_keys=True))


if __name__ == "__main__":
    main()
