#!/usr/bin/env python3
"""Build R138 full-circle mean metadata only; never execute numerical modules."""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
REPO = "Rogerhu12/math-research-public"
PREFIX = "2026-11-20-R138-root-mean-angular"
SOURCE_NAME = "fourfold_codazzi_root_mean_angular.py"
WORKER_NAME = "fourfold_codazzi_root_mean_angular_public_worker.py"
GENERATOR_NAME = "make_root_mean_angular_manifest.py"
GERM_SHA = "397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864"
CANDIDATE_SHA = "ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
DEFINITION_SHA = "d152f31cef53c1d58099cf3d1f994d2dad9d31d6a75cb42a7d9e54a35c17ae79"
FRAME_TRANSFER_SHA = "36150e78e3fade8bd8f0af293177deed6150d507601a84b7a426999cf5390df9"


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
    small.append(spec("mean_contract", contract_relative, source_path(contract, contract_relative)))
    current = [
        ("reviewed_rules", "notes/2026-11-20-reviewed-public-CI-rules.json"),
        ("candidate_index", "data/phase_transport_resume127_20261114/candidate/moving-m32-alpha0765-fullR-v2-tol2e9-candidate.json"),
        ("definition_helper", "scripts/fourfold_codazzi_root_axis_support.py"),
        ("actual_root_frame_transfer_proof", "results/R138-supplement-actual-root-angular-comparison-and-mean-readout.md"),
        ("complete_root_angular_proof", "results/R138-supplement-complete-root-angular-form-and-two-scalar-geometry.md"),
        ("same_repaired_physical_object_proof", "results/R138-supplement-actual-positive-support-for-repaired-physical-frame.md"),
        ("exact_continuous_repair_proof", "results/R133-supplement-exact-continuous-repair-of-final-centre.md"),
    ]
    small.extend(spec(role, TOPIC + "/" + relative) for role, relative in current)
    by_role = {item["role"]: item for item in small}
    review = json.loads((root / by_role["reviewed_rules"]["path"]).read_bytes())
    for path, expected in review["readme_sha256"].items():
        if sha((root / path).read_bytes()) != expected:
            raise ValueError("README differs from the explicit current rule review: " + path)
    for role, expected in (("candidate_index", CANDIDATE_SHA),
                           ("definition_helper", DEFINITION_SHA),
                           ("actual_root_frame_transfer_proof", FRAME_TRANSFER_SHA)):
        if by_role[role]["sha256"] != expected:
            raise ValueError("the exact unchanged mean-definition input differs: " + role)

    # Existing metadata supplies only immutable historical paths and hashes.
    # No W2C context, previous axis target, producer, or old scalar is executed.
    old = json.loads((root / TOPIC / "notes/2026-11-20-centre-mean-floor-inputs.json").read_bytes())
    originals = []
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
    if len(originals) != 6 or len({x["path"] for x in originals}) != 6:
        raise ValueError("incomplete exact six-object restoration")

    allowed = sorted([
        "identity", "complete", "proved", "failure", "completed_cells", "current_target",
        "original_scientific_calls", "old_axis_target_calls", "old_geometry_target_calls",
        "arrays_published", "scope", "completed_integral_prefix",
        "coefficient_integral_prefix_upper", "accumulated_frame_error_upper", "seconds",
        "ideal_mean_denominator", "complete_mean_direction_coefficient_upper",
        "actual_frame_transfer_fee", "actual_mean_denominator",
        "maximum_complete_cell_connection_error_upper", "complete_frame_error_upper",
        "strict_sign_uses_complete_saved_decimal_ball",
    ])
    manifest = dict(
        kind="R138_same_Qrepair_root_mean_full_circle_inputs_v1", repository=REPO,
        problem_id="R138_same_Qrepair_true_root_full_circle_mean_v1",
        scientific_kind="R138_same_Qrepair_true_root_full_circle_mean_denominator_v1",
        files=small, expected_current_input_count=len(small), historical_inputs=originals,
        accepted_natives=dict(germ=GERM_SHA, candidate=CANDIDATE_SHA),
        runtime=dict(python="3.12.14", packages={"python-flint": "0.9.0", "numpy": "2.3.5"}),
        parameters=dict(arithmetic_bits=320, complete_angular_interval="[0,2*pi]",
                        angular_cells=8192, physical_frequency_factor=4,
                        actual_periodic_frame_fee="11/10000000",
                        exact_repair_C0="1/250000000000000000",
                        exact_eta="-7789843107295549/4611686018427387904",
                        exact_nu="-2572625729470897/72057594037927936",
                        true_root_interval=["1191984371497/5000000000000", "2383968743003/10000000000000"],
                        original_candidate_shape=[4, 6144, 65],
                        scientific_checkpoint_cells=128,
                        frame_at_zero="X=e_z,Y=e_y,n=e_x; one proper ambient rotation",
                        projection_vector="ell=X(root,0)=local e_z",
                        whole_cell_Rodrigues=True, complete_decimal_sign_readback=True),
        allowed_scientific_fields=allowed,
        scope=dict(new_target="one complete actual periodic-frame root mean denominator enclosure",
                   mathematical_target_count=1, original_mean_and_all_32_modes_retained=True,
                   old_producer_calls=0, old_completed_targets_recomputed=0, W2C_context_constructed=False,
                   candidate_definition_restoration_only=True,
                   existing_axis_source_role="input loader and private definition only; no axis run or q/s read",
                   exact_original_root_germ_used_without_new_intrinsic_evaluation=True,
                   full_root_interval_and_paid_repair_retained=True,
                   full_root_energy_positive=False, full_inverse_proved=False,
                   both_original_rhs_solved=False, final_topic_complete=False, new_array_output=False),
        operation=dict(child_timeout_seconds=5400, readme_pull_interval_seconds=1800,
                       topic_maximum_bytes=200000000, reserve_bytes=120000,
                       maximum_total_publication_bytes=100000, maximum_execution_bytes=85000,
                       maximum_scientific_bytes=16000,
                       output_base=TOPIC + "/notes/root_mean_angular_ci",
                       consumed_marker=TOPIC + "/notes/root_mean_angular_ci/R138_root_mean_full_circle_v1-consumed.json",
                       automatic_scientific_retry=False,
                       publication="complete scalar enclosure or unfinished integral prefix, run metadata and hashes only",
                       no_artifacts=True, no_Releases=True, no_new_arrays=True),
    )
    raw = (json.dumps(manifest, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()
    if len(raw) >= 100000:
        raise ValueError("manifest must remain one complete small text")
    filename = PREFIX + "-inputs.json"
    (out / filename).write_bytes(raw)
    workflow = """name: R138 complete root mean denominator

on:
  push:
    branches: [main]
    paths:
      - .github/workflows/fourfold-codazzi-root-mean-angular-public.yml

permissions:
  contents: write

concurrency:
  group: r138-root-mean-full-circle-v1
  cancel-in-progress: false

jobs:
  complete-root-mean:
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
            topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_root_mean_angular_public_worker.py
            topics/visible-flex-exact-nearby/notes/MANIFEST_NAME
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install the fixed directed runtime
        run: python -m pip install --disable-pip-version-check python-flint==0.9.0 numpy==2.3.5
      - name: Restore original bytes and enclose the full-circle root mean
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_root_mean_angular_public_worker.py --repo "$GITHUB_WORKSPACE" --manifest topics/visible-flex-exact-nearby/notes/MANIFEST_NAME --manifest-sha MANIFEST_SHA
""".replace("MANIFEST_NAME", filename).replace("MANIFEST_SHA", sha(raw))
    (out / "fourfold-codazzi-root-mean-angular-public.yml").write_text(workflow)
    print(json.dumps(dict(manifest_bytes=len(raw), manifest_sha256=sha(raw),
                          current_inputs=len(small), historical_inputs=len(originals),
                          scientific_source_sha256=by_role["science"]["sha256"],
                          worker_sha256=by_role["worker"]["sha256"],
                          numerical_execution=False), sort_keys=True))


if __name__ == "__main__":
    main()
