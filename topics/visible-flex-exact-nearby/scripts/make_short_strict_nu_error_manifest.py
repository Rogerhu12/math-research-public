"""Metadata-only SB entry; all scientific work remains in public Actions."""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util, json, sys
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
OWNER = TOPIC+"/scripts/fourfold_codazzi_short_strict_nu_error_owner.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_short_strict_nu_error_public_worker.py"
GENERATOR = TOPIC+"/scripts/make_short_strict_nu_error_manifest.py"
MANIFEST = TOPIC+"/notes/2026-11-27-short-strict-nu-error-inputs.json"
WORKFLOW = ".github/workflows/visible-exact-short-strict-nu-error.yml"
WORKFLOW_TEMPLATE = '''name: R147 short strict nu full error receiver
on:
  push:
    branches: [main]
    paths:
      - '.github/workflows/visible-exact-short-strict-nu-error.yml'
  workflow_dispatch:
permissions:
  contents: write
concurrency:
  group: visible-flex-exact-short-strict-nu-error-20261127
  cancel-in-progress: false
jobs:
  complete-new-short-radial-cost:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-latest
    timeout-minutes: 45
    env:
      OMP_NUM_THREADS: '1'
      OPENBLAS_NUM_THREADS: '1'
      MKL_NUM_THREADS: '1'
      NUMEXPR_NUM_THREADS: '1'
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
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_negative_nu_waist_public_worker.py
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_short_strict_nu_error_public_worker.py
            /topics/visible-flex-exact-nearby/notes/2026-11-27-short-strict-nu-error-inputs.json
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install the same directed scalar runtime
        run: python -m pip install --disable-pip-version-check python-flint==0.9.0
      - name: Receive the full parameter error through the genuine short interval
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: >-
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_short_strict_nu_error_public_worker.py
          --repo "$GITHUB_WORKSPACE"
          --manifest topics/visible-flex-exact-nearby/notes/2026-11-27-short-strict-nu-error-inputs.json
          --manifest-sha @MANIFEST_SHA@
'''


def require(ok,message):
    if not ok:raise ValueError(message)


def load(root,path,name):
    raw = (root/path).read_bytes();require(0 < len(raw) < 100000,"whole small source")
    ast.parse(raw.decode(),filename=path)
    spec = importlib.util.spec_from_file_location(name,root/path)
    module = importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


def build(root):
    require(not any(name in sys.modules for name in ("flint","numpy","scipy")),"metadata-only entry")
    sys.dont_write_bytecode = True
    owner = load(root,OWNER,"_SB_metadata_owner");worker = load(root,WORKER,"_SB_metadata_worker")
    math = load(root,owner.MATH,"_SB_pure_new_formula")
    require(owner.SOURCE == OWNER and owner.WORKER == WORKER and owner.GENERATOR == GENERATOR
        and list(math.OUTPUT_ORDER) == owner.TARGETS,"complete new concrete scalar entry")
    compile(worker.build_adapter(root),WORKER,"exec")
    declared = owner.gather(root);files,history,roles = (declared[key] for key in ("files","historical_inputs","roles"))
    raws = {item["path"]:(root/item["path"]).read_bytes() for item in files}
    paths = {item["path"]:root/item["path"] for item in files}
    admitted = owner.admit(declared,raws,paths)
    require(admitted["NP"]["complete"] is admitted["SP"]["complete"] is True,
        "genuine complete same-family predecessors")
    review = owner.parse(raws[roles["reviewed_rules"]])
    require(review["repository"] == owner.REPO and review["new_unread_rules_must_still_be_reported_and_applied"] is True
        and set(review["readme_sha256"]) == {"README.md",TOPIC+"/README.md"},"both explicitly reviewed README files")
    for relative,digest in review["readme_sha256"].items():
        require(owner.sha((root/relative).read_bytes()) == digest,"already reviewed README unchanged: "+relative)
    require(review["large_data_policy"]["maximum_topic_bytes"] == 200000000
        and review["large_data_policy"]["original_completed_mathematics_must_not_be_recomputed"] is True
        and not any(name in sys.modules for name in ("flint","numpy","scipy")),"no local scientific evaluation")
    manifest = {"repository":owner.REPO,"kind":owner.MANIFEST_KIND,"scientific_kind":owner.KIND,"stage":owner.STAGE,
        "problem_id":"R147_complete_short_strict_nu_error_20261127","parameters":owner.PARAMETERS,
        "runtime":owner.RUNTIME,"target_order":owner.TARGETS,"complete_record_counts":[11],
        "allowed_scientific_fields":owner.SCI_FIELDS,"files":files,"expected_current_input_count":len(files),
        "historical_inputs":history,"roles":roles,
        "operation":{"topic_maximum_bytes":200000000,"reserve_bytes":120000,"readme_pull_interval_seconds":1800,
            "automatic_scientific_retry":False,"consumed_marker":TOPIC+"/notes/short_strict_nu_error_ci/consumed-target.json",
            "output_base":TOPIC+"/notes/short_strict_nu_error_ci","maximum_scientific_bytes":18000,
            "maximum_execution_bytes":30000,"maximum_total_publication_bytes":55000,"child_timeout_seconds":1920},
        "scope":{"same_original_selected_Q_delta":True,"all40_original_body_parts_required":True,
            "all7721_full_original_rows_admitted":True,"new_radial_target_only_on_exact_0_to_9_over_50":True,
            "original_complete_SP_nonradial_matrix_and_both_means_retained":True,
            "every_strict_source_insertion_time_retained":True,"whole_NP_error_source_integrals_read_only":True,
            "uniform_interior_primitive_plus_mean_error_proved_only_by_actual_new_outputs":True,
            "uniform_and_radial_raw_L2_error_proved_only_by_actual_new_outputs":True,
            "degree160_factor_applies_only_to_original_centre_residual":True,
            "full_selected_differences_remain_in_original_L2_units":True,
            "old_intrinsic_trial_residual_pairing_or_matrix_targets_recomputed":False,
            "new_phase_height_signed_column_or_full_Schur_proved":False}}
    raw = owner.canonical(manifest);require(len(raw) < 100000,"whole small immutable input manifest")
    return raw,WORKFLOW_TEMPLATE.replace("@MANIFEST_SHA@",owner.sha(raw)).encode()


def main():
    parser = argparse.ArgumentParser(description=__doc__);parser.add_argument("--repo",default=".",type=Path)
    args = parser.parse_args();root = args.repo.resolve();sys.dont_write_bytecode = True
    raw,workflow = build(root)
    for relative,content in ((MANIFEST,raw),(WORKFLOW,workflow)):
        path = root/relative;path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(content)
    print(json.dumps({"ready":True,"manifest":MANIFEST,"manifest_bytes":len(raw),
        "manifest_sha256":hashlib.sha256(raw).hexdigest(),"workflow":WORKFLOW,
        "scientific_targets_evaluated_locally":0},sort_keys=True))


if __name__ == "__main__":
    main()
