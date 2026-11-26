"""Metadata-only first IL launch, with complete old natural carrier restoration."""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util, json, subprocess, sys
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
OWNER = TOPIC+"/scripts/fourfold_codazzi_inverse_density_lift_owner.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_inverse_density_lift_public_worker.py"
GENERATOR = TOPIC+"/scripts/make_inverse_density_lift_manifest.py"
MANIFEST = TOPIC+"/notes/2026-11-27-inverse-density-lift-inputs.json"
WORKFLOW = ".github/workflows/fourfold-codazzi-inverse-density-lift-public.yml"
OLD = TOPIC+"/notes/2026-11-26-reflected-waist-rows-inputs.json"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def blob(raw):
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def encode(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False)+"\n").encode()


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build(root):
    root = Path(root).resolve()
    owner = load(root/OWNER, "_IL_metadata_owner")
    worker = load(root/WORKER, "_IL_metadata_worker")
    ast.parse(worker.patched_source())
    old = json.loads((root/OLD).read_bytes())
    files, contents = [], {}
    for spec in old["files"]:
        raw = (root/spec["path"]).read_bytes()
        owner.require(len(raw) == spec["bytes"] and sha(raw) == spec["sha256"]
                      and blob(raw) == spec["git_blob_sha"], "unchanged whole original RW input")
        role = owner.RENAMED_RW_ROLES.get(spec["role"], spec["role"])
        files.append(dict(spec, role=role))
        contents[role] = raw
    additions = {
        "science": OWNER, "worker": WORKER, "generator": GENERATOR,
        "proof": TOPIC+"/results/R149-supplement-complete-inverse-density-lift-derivative-bounds.md",
        "DC_proof": TOPIC+"/results/R149-supplement-same-sign-density-compression-and-finite-Theta-rows.md",
        "DC_math": TOPIC+"/scripts/fourfold_codazzi_density_compression_theta_math.py",
        "RW_manifest": OLD,
        "cover_source": TOPIC+"/scripts/fourfold_codazzi_phase_complete_transport_cover.py",
        "wiener_source": TOPIC+"/scripts/fourfold_codazzi_phase_Wiener_transport_lift.py",
        "cover_process": TOPIC+"/notes/phase_transport_complete_ci/run-43580721166-1/process.json",
    }
    for role, path in additions.items():
        raw = (root/path).read_bytes()
        owner.require(0 < len(raw) < 100000, "entire small current input")
        raw.decode()
        if path.endswith(".py"):
            ast.parse(raw.decode(), filename=path)
        files.append(dict(role=role, path=path, bytes=len(raw), sha256=sha(raw), git_blob_sha=blob(raw)))
        contents[role] = raw
    owner.require(len({s["path"] for s in files}) == len(files), "complete unique current paths")
    historical = old["historical_inputs"]+owner.EXTRA_HISTORICAL_INPUTS
    for spec in historical:
        raw = subprocess.check_output(["git", "show", spec["commit"]+":"+spec["path"]], cwd=root)
        contents[spec["role"]] = raw
    specs = {s["role"]: s for s in files+historical}
    owner.admit_complete_inputs(contents, specs)
    owner.require(not any(name in sys.modules for name in ("flint", "numpy", "scipy")),
                  "local generator performs only whole-input metadata admission")
    review = json.loads(contents["reviewed_rules"])
    for path, expected in review["readme_sha256"].items():
        owner.require(sha((root/path).read_bytes()) == expected, "reviewed README unchanged")
    return {
        "repository": owner.REPO, "kind": owner.MANIFEST_KIND,
        "problem_id": "R149_original_inverse_density_lift_20261127",
        "scientific_kind": owner.KIND, "stage": owner.STAGE,
        "parameters": owner.PARAMETERS, "runtime": old["runtime"],
        "files": sorted(files, key=lambda s: s["role"]),
        "historical_inputs": historical, "expected_current_input_count": len(files),
        "allowed_scientific_fields": owner.SCI_FIELDS,
        "complete_record_counts": [4], "target_order": owner.TARGETS,
        "scope": {
            "whole_original_two_leg_terminal_and_central_means_retained": True,
            "same_selected_true_inverse_map_and_full_root_fee": True,
            "only_four_first_time_scalar_targets": True,
            "old_transport_KAM_fit_DFT_or_norm_targets_recomputed": False,
            "whole_compression_rows_or_Theta_Schur_proved": False,
        },
        "operation": {
            "topic_maximum_bytes": 200000000, "reserve_bytes": 120000,
            "readme_pull_interval_seconds": 1800, "automatic_scientific_retry": False,
            "child_timeout_seconds": 240,
            "consumed_marker": TOPIC+"/notes/inverse_density_lift_ci/consumed-target.json",
            "output_base": TOPIC+"/notes/inverse_density_lift_ci",
            "maximum_scientific_bytes": 45000, "maximum_execution_bytes": 38000,
            "maximum_total_publication_bytes": 85000,
        },
    }


def workflow(digest):
    return '''name: R149 complete original inverse-density lift
on:
  push:
    branches: [main]
    paths:
      - '.github/workflows/fourfold-codazzi-inverse-density-lift-public.yml'
  workflow_dispatch:
permissions:
  contents: write
concurrency:
  group: visible-flex-exact-original-inverse-density-lift-20261127
  cancel-in-progress: false
jobs:
  complete-four-new-inverse-lift-scalars:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-latest
    timeout-minutes: 20
    steps:
      - uses: actions/checkout@v4
        with:
          ref: main
          fetch-depth: 0
          filter: blob:none
          persist-credentials: false
          sparse-checkout-cone-mode: false
          sparse-checkout: |
            /README.md
            /topics/visible-flex-exact-nearby/README.md
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_inverse_density_lift_public_worker.py
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_reflected_waist_rows_public_worker.py
            /topics/visible-flex-exact-nearby/notes/2026-11-27-inverse-density-lift-inputs.json
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install the fixed directed scalar runtime
        run: python -m pip install --disable-pip-version-check python-flint==0.9.0
      - name: Restore the complete original one-leg inputs and certify four new scalars
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: >-
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_inverse_density_lift_public_worker.py
          --repo "$GITHUB_WORKSPACE"
          --manifest topics/visible-flex-exact-nearby/notes/2026-11-27-inverse-density-lift-inputs.json
          --manifest-sha '''+digest+"\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", type=Path, required=True)
    args = ap.parse_args()
    root = args.repo.resolve()
    result = build(root)
    raw = encode(result)
    if not 0 < len(raw) < 100000:
        raise ValueError("whole manifest must remain below100KB")
    digest = sha(raw)
    (root/MANIFEST).write_bytes(raw)
    (root/WORKFLOW).parent.mkdir(parents=True, exist_ok=True)
    (root/WORKFLOW).write_text(workflow(digest))
    print(json.dumps({"manifest": MANIFEST, "bytes": len(raw), "sha256": digest,
                      "current_inputs": len(result["files"]),
                      "whole_original_native_inputs": len(result["historical_inputs"]),
                      "new_targets": len(result["target_order"]),
                      "numerical_imports_or_old_targets": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
