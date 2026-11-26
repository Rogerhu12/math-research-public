#!/usr/bin/env python3
"""Write the new signed metric-mean input metadata and public workflow; no science."""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path
import subprocess

TOPIC = "topics/visible-flex-exact-nearby"
PREFIX = "2026-11-27-R144-signed-metric-mean-moments"
SCIENCE = "fourfold_codazzi_signed_metric_mean_moments.py"
WORKER = "fourfold_codazzi_signed_metric_mean_moments_public_worker.py"
GENERATOR = "make_signed_metric_mean_moments_manifest.py"
WORKFLOW_NAME = "fourfold-codazzi-signed-metric-mean-moments-public.yml"
WORKFLOW = r"""name: R144 signed true metric mean moments

on:
  push:
    branches: [main]
    paths:
      - .github/workflows/fourfold-codazzi-signed-metric-mean-moments-public.yml

permissions:
  contents: write

concurrency:
  group: r144-signed-metric-mean-moments-v1
  cancel-in-progress: false

jobs:
  signed-metric-mean-moments:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-latest
    timeout-minutes: 40
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 1
          filter: blob:none
          persist-credentials: false
          sparse-checkout-cone-mode: false
          sparse-checkout: |
            README.md
            topics/visible-flex-exact-nearby/README.md
            topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_signed_metric_mean_moments_public_worker.py
            topics/visible-flex-exact-nearby/notes/2026-11-27-R144-signed-metric-mean-moments-inputs.json
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install directed arithmetic
        run: python -m pip install --disable-pip-version-check python-flint==0.9.0
      - name: Evaluate new signed compact metric moments
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          OPENBLAS_NUM_THREADS: "1"
          OMP_NUM_THREADS: "1"
          MKL_NUM_THREADS: "1"
        run: |
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_signed_metric_mean_moments_public_worker.py --repo "$GITHUB_WORKSPACE" --manifest topics/visible-flex-exact-nearby/notes/2026-11-27-R144-signed-metric-mean-moments-inputs.json --manifest-sha __SHA__
"""


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--read-commit", default="origin/main")
    args = parser.parse_args()
    root = args.repo.resolve()
    head = subprocess.check_output(["git", "rev-parse", args.read_commit], cwd=root, text=True).strip()
    for path in ("README.md", TOPIC + "/README.md"):
        reviewed = subprocess.check_output(["git", "show", head + ":" + path], cwd=root)
        if reviewed != (root / path).read_bytes():
            raise ValueError("read rules differ from the declared public commit: " + path)
    current = [
        ("science", "scripts/" + SCIENCE),
        ("worker", "scripts/" + WORKER),
        ("generator", "scripts/" + GENERATOR),
        ("proof", "results/R144-supplement-signed-metric-mean-moments-and-compact-parameter-lift.md"),
        ("sharp_root_proof", "results/R144-supplement-sharp-compact-root-from-completed-forward-mean.md"),
        ("cp", "notes/compact_mean_c0_receivers_ci/run-45787608966-1/compact-mean-c0-receivers.json"),
        ("cp_execution", "notes/compact_mean_c0_receivers_ci/run-45787608966-1/execution.json"),
        ("mean_parts_index", "notes/2026-11-14-R133-final-complete-scalar-mean-native-binary-parts.json"),
    ]
    files = []
    for role, suffix in current:
        path = TOPIC + "/" + suffix
        raw = (root / path).read_bytes()
        if not 0 < len(raw) < 100000:
            raise ValueError("current complete small input size: " + path)
        raw.decode()
        if path.endswith(".py"):
            ast.parse(raw, filename=path)
        files.append(dict(role=role, path=path, bytes=len(raw), sha256=digest(raw)))
    manifest = dict(
        kind="R144_signed_metric_mean_moments_inputs_v1",
        repository="Rogerhu12/math-research-public",
        scientific_kind="R144_signed_true_metric_terminal_mean_moments_v1",
        files=files, read_commit=head,
        readmes={path: digest((root / path).read_bytes())
                 for path in ("README.md", TOPIC + "/README.md")},
        historical_mean_commit="46f127c7153f5393dcd2a00f42d4c1d3662c294d",
        mean_native_sha256="e233ece0f264eb73f93dfe5b43c5d45b4d5d6db06da2418b9c20fb545a01889b",
        parameters=dict(exact_alpha="6890507429876859/9007199254740992",
                        exact_nu="-2572625729470897/72057594037927936",
                        exact_eta="-7789843107295549/4611686018427387904",
                        compact_interval=["1/20", "9/50"], derivative_sign_split="23/200",
                        original_rows=7721, original_joins=6143, compact_rows=1156,
                        raw_modes=32, arithmetic_bits=320,
                        xi_interval=["-0.0000000000008", "-0.0000000000007"],
                        a0_interval=["1.06873282", "1.068732841"],
                        saved_H_range="1 <= H(r) <= complete CP H(9/50).upper",
                        reused_complete_targets=["abar", "bbar", "H_at_compact_right"]),
        new_integrals=["I_U", "E0", "E1", "E2", "A3"],
        new_signed_moments=["M0", "M1", "M2"],
        new_conclusions=["kappa_nu", "density_control_metric_derivative"],
        mathematical_target="signed genuine metric derivative at the same exact-mean compact centre",
        scope=dict(old_H_ODE_calls=0, old_mean_retraction_calls=0,
                   old_ordinary_nu_source_norm_calls=0, old_producers_called=0,
                   new_arrays_artifacts_or_Releases=False,
                   nonzero_is_not_full_Schur=True,
                   interval_containing_zero_is_not_proof_of_zero=True,
                   same_original_compact_jumps_retained=True),
    )
    raw = (json.dumps(manifest, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False) + "\n").encode()
    path = root / TOPIC / "notes" / (PREFIX + "-inputs.json")
    path.write_bytes(raw)
    workflow = root / ".github" / "workflows" / WORKFLOW_NAME
    workflow.parent.mkdir(parents=True, exist_ok=True)
    workflow.write_text(WORKFLOW.replace("__SHA__", digest(raw)))
    print(json.dumps(dict(manifest_bytes=len(raw), manifest_sha256=digest(raw),
                          current_inputs=len(files), science_not_executed=True),
                     sort_keys=True))


if __name__ == "__main__":
    main()
