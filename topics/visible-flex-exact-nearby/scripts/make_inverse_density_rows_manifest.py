"""Metadata-only IR launch after the WHOLE actual IL result is available."""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util, json, subprocess, sys
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
OWNER = TOPIC+"/scripts/fourfold_codazzi_inverse_density_rows_owner.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_inverse_density_rows_public_worker.py"
GENERATOR = TOPIC+"/scripts/make_inverse_density_rows_manifest.py"
MANIFEST = TOPIC+"/notes/2026-11-27-inverse-density-rows-inputs.json"
WORKFLOW = ".github/workflows/fourfold-codazzi-inverse-density-rows-public.yml"
OLD = TOPIC+"/notes/2026-11-27-inverse-density-lift-inputs.json"


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


def build(root, inverse_lift_run):
    root = Path(root).resolve()
    owner = load(root/OWNER, "_IR_metadata_owner")
    worker = load(root/WORKER, "_IR_metadata_worker")
    ast.parse(worker.patched_source())
    old = json.loads((root/OLD).read_bytes())
    files, contents = [], {}
    for spec in old["files"]:
        raw = (root/spec["path"]).read_bytes()
        owner.require(len(raw) == spec["bytes"] and sha(raw) == spec["sha256"]
                      and blob(raw) == spec["git_blob_sha"], "unchanged complete IL input")
        role = owner.RENAMED_IL_ROLES.get(spec["role"], spec["role"])
        files.append(dict(spec, role=role))
        contents[role] = raw
    run = str(inverse_lift_run)
    owner.require(run.isdigit(), "an actual immutable successful IL run number")
    base = TOPIC+"/notes/inverse_density_lift_ci/run-"+run+"-1"
    additions = {
        "science": OWNER, "worker": WORKER, "generator": GENERATOR,
        "proof": TOPIC+"/results/R149-supplement-complete-inverse-density-row-residuals.md",
        "IR_math": TOPIC+"/scripts/fourfold_codazzi_inverse_density_rows_math.py",
        "DB_proof": TOPIC+"/results/R149-supplement-complete-Theta-row-regularity-and-negative-window-density-inverse.md",
        "DB_math": TOPIC+"/scripts/fourfold_codazzi_density_inverse_regularization_math.py",
        "IL_manifest": OLD,
        "IL_actual": base+"/actual-original-inverse-density-lift.json",
        "IL_execution": base+"/execution.json",
    }
    for role, path in additions.items():
        raw = (root/path).read_bytes()
        owner.require(0 < len(raw) < 100000, "entire small actual/current input")
        raw.decode()
        if path.endswith(".py"):
            ast.parse(raw.decode(), filename=path)
        files.append(dict(role=role, path=path, bytes=len(raw), sha256=sha(raw), git_blob_sha=blob(raw)))
        contents[role] = raw
    owner.require(len({s["path"] for s in files}) == len(files), "complete unique current paths")
    historical = old["historical_inputs"]
    for spec in historical:
        raw = subprocess.check_output(["git", "show", spec["commit"]+":"+spec["path"]], cwd=root)
        contents[spec["role"]] = raw
    specs = {s["role"]: s for s in files+historical}
    owner.admit_complete_inputs(contents, specs)
    owner.require(not any(name in sys.modules for name in ("flint", "numpy", "scipy")),
                  "local preflight executes no old or new scientific target")
    review = json.loads(contents["reviewed_rules"])
    for path, expected in review["readme_sha256"].items():
        owner.require(sha((root/path).read_bytes()) == expected, "reviewed README unchanged")
    return {
        "repository": owner.REPO, "kind": owner.MANIFEST_KIND,
        "problem_id": "R149_original_inverse_density_rows_20261127",
        "scientific_kind": owner.KIND, "stage": owner.STAGE,
        "parameters": owner.PARAMETERS,
        "runtime": {"python": "3.12.14", "packages": {"numpy": "2.3.5", "python-flint": "0.9.0"}},
        "files": sorted(files, key=lambda s: s["role"]),
        "historical_inputs": historical, "expected_current_input_count": len(files),
        "allowed_scientific_fields": owner.SCI_FIELDS,
        "complete_record_counts": [96, 3], "target_order": owner.TARGETS,
        "scope": {
            "whole_successful_IL_result_directly_consumed": True,
            "same_selected_true_inverse_map_and_original_phase_means": True,
            "both_full_Hdot_minus_half_and_L2_residuals": True,
            "all96_signed_heads_aliases_tails_and_models": True,
            "only_original_coordinate_rows_before_A": True,
            "IL_and_other_old_targets_recomputed": False,
            "whole_VQ_Theta_or_physical_Schur_proved": False,
        },
        "operation": {
            "topic_maximum_bytes": 200000000, "reserve_bytes": 120000,
            "readme_pull_interval_seconds": 1800, "automatic_scientific_retry": False,
            "child_timeout_seconds": 15000,
            "consumed_marker": TOPIC+"/notes/inverse_density_rows_ci/consumed-target.json",
            "output_base": TOPIC+"/notes/inverse_density_rows_ci",
            "maximum_scientific_bytes": 95000, "maximum_execution_bytes": 38000,
            "maximum_total_publication_bytes": 135000,
        },
    }


def workflow(digest):
    return '''name: R149 complete original inverse-density96 rows
on:
  push:
    branches: [main]
    paths:
      - '.github/workflows/fourfold-codazzi-inverse-density-rows-public.yml'
  workflow_dispatch:
permissions:
  contents: write
concurrency:
  group: visible-flex-exact-original-inverse-density96-rows-20261127
  cancel-in-progress: false
jobs:
  complete96-full-residual-rows:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-latest
    container: python@sha256:4d1caded1f729ae443eb803f26ffde7b61e696aeaef62f099abb6dd6b14257c7
    timeout-minutes: 360
    env:
      OPENBLAS_CORETYPE: Haswell
      OPENBLAS_NUM_THREADS: '1'
      OMP_NUM_THREADS: '1'
      MKL_NUM_THREADS: '1'
      BLIS_NUM_THREADS: '1'
      VECLIB_MAXIMUM_THREADS: '1'
      NUMEXPR_NUM_THREADS: '1'
    steps:
      - name: Install Git in the fixed original numerical container
        run: |
          apt-get update -qq
          apt-get install -y --no-install-recommends git ca-certificates
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
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_inverse_density_rows_public_worker.py
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_reflected_waist_rows_public_worker.py
            /topics/visible-flex-exact-nearby/notes/2026-11-27-inverse-density-rows-inputs.json
      - name: Trust only this explicitly mounted checkout
        run: git config --global --add safe.directory "$GITHUB_WORKSPACE"
      - name: Install the fixed finite-proposal and directed runtime
        run: python -m pip install --disable-pip-version-check numpy==2.3.5 python-flint==0.9.0
      - name: Admit whole IL and certify all96 complete inverse-density residual rows
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: >-
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_inverse_density_rows_public_worker.py
          --repo "$GITHUB_WORKSPACE"
          --manifest topics/visible-flex-exact-nearby/notes/2026-11-27-inverse-density-rows-inputs.json
          --manifest-sha '''+digest+"\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", type=Path, required=True)
    ap.add_argument("--inverse-lift-run", default="45896427415")
    args = ap.parse_args()
    root = args.repo.resolve()
    result = build(root, args.inverse_lift_run)
    raw = encode(result)
    if not 0 < len(raw) < 100000:
        raise ValueError("the complete manifest must remain below100KB")
    digest = sha(raw)
    (root/MANIFEST).write_bytes(raw)
    (root/WORKFLOW).parent.mkdir(parents=True, exist_ok=True)
    (root/WORKFLOW).write_text(workflow(digest))
    print(json.dumps({"manifest": MANIFEST, "bytes": len(raw), "sha256": digest,
                      "current_inputs": len(result["files"]),
                      "whole_original_native_inputs": len(result["historical_inputs"]),
                      "new_targets": len(result["target_order"]),
                      "actual_IL_run": str(args.inverse_lift_run)+"/1",
                      "numerical_imports_or_old_targets": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
