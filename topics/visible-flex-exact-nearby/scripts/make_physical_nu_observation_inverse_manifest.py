"""Metadata-only concrete PO entry after actual NP/NH/JC/RW success.

No local scientific arithmetic, trial, pairing, row or norm is evaluated.
"""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util, json, subprocess, sys
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
OWNER = TOPIC+"/scripts/fourfold_codazzi_physical_nu_observation_inverse_owner.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_physical_nu_observation_inverse_public_worker.py"
GENERATOR = TOPIC+"/scripts/make_physical_nu_observation_inverse_manifest.py"
MANIFEST = TOPIC+"/notes/2026-11-27-physical-nu-observation-inverse-inputs.json"
WORKFLOW = ".github/workflows/visible-exact-physical-nu-observation-inverse.yml"
DEFAULT_NH_BASE = TOPIC+"/notes/strict_nu_high_forcing_ci/run-45897599620-1"

WORKFLOW_TEMPLATE = '''name: R147 complete physical nu observation inverse
on:
  push:
    branches: [main]
    paths:
      - '.github/workflows/visible-exact-physical-nu-observation-inverse.yml'
  workflow_dispatch:
permissions:
  contents: write
concurrency:
  group: visible-flex-exact-physical-nu-observation-inverse-20261127
  cancel-in-progress: false
jobs:
  complete-new96-observation-inverse:
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
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_support_localized_nu_public_worker.py
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_strict_nu_particular_public_worker.py
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_strict_nu_high_forcing_public_worker.py
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_physical_nu_observation_inverse_public_worker.py
            /topics/visible-flex-exact-nearby/notes/2026-11-27-physical-nu-observation-inverse-inputs.json
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install fixed directed runtime
        run: python -m pip install --disable-pip-version-check python-flint==0.9.0
      - name: Invert the new complete observation map and receive the physical column
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: >-
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_physical_nu_observation_inverse_public_worker.py
          --repo "$GITHUB_WORKSPACE"
          --manifest topics/visible-flex-exact-nearby/notes/2026-11-27-physical-nu-observation-inverse-inputs.json
          --manifest-sha @MANIFEST_SHA@
'''


def require(ok,message):
    if not ok:
        raise ValueError(message)


def load(root,relative,name):
    raw = (root/relative).read_bytes()
    require(0 < len(raw) < 100000,"whole small metadata source")
    ast.parse(raw.decode(),filename=relative)
    spec = importlib.util.spec_from_file_location(name,root/relative)
    module = importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


def build(root,nh_actual,nh_execution,nh_manifest):
    require(not any(name in sys.modules for name in ("flint","numpy","scipy")),"metadata-only start")
    sys.dont_write_bytecode = True
    owner = load(root,OWNER,"_PO_metadata_owner")
    worker = load(root,WORKER,"_PO_metadata_worker")
    math = load(root,owner.MATH,"_PO_pure_definitions")
    require(owner.SOURCE == OWNER and owner.WORKER == WORKER and owner.GENERATOR == GENERATOR
            and list(math.OUTPUT_ORDER) == owner.TARGETS,"the complete new public entry")
    compile(worker.build_adapter(root),WORKER,"exec")
    declared = owner.gather(root,nh_actual,nh_execution,nh_manifest)
    files,historical,roles = (declared[key] for key in ("files","historical_inputs","roles"))
    raws = {item["path"]:(root/item["path"]).read_bytes() for item in files}
    paths = {item["path"]:root/item["path"] for item in files}
    for item in historical:
        raw = subprocess.run(["git","show",item["commit"]+":"+item["path"]],
            cwd=root,capture_output=True,check=True).stdout
        require(len(raw) == item["bytes"] and owner.sha(raw) == item["sha256"],"whole saved original native")
        raws[item["path"]] = raw
    prior = owner.admit(declared,raws,paths)
    require(prior["NP"]["complete"] is prior["NH"]["complete"] is prior["JC"]["complete"]
            is prior["RW_actual"]["complete"] is True,"all genuine whole predecessors completed")
    review = owner.parse(raws[roles["reviewed_rules"]])
    require(review["repository"] == owner.REPO
        and review["new_unread_rules_must_still_be_reported_and_applied"] is True
        and set(review["readme_sha256"]) == {"README.md",TOPIC+"/README.md"},"both complete reviewed rule files")
    for relative,digest in review["readme_sha256"].items():
        require(owner.sha((root/relative).read_bytes()) == digest,"already read README unchanged: "+relative)
    require(review["large_data_policy"]["maximum_topic_bytes"] == 200000000
        and review["large_data_policy"]["original_completed_mathematics_must_not_be_recomputed"] is True
        and not any(name in sys.modules for name in ("flint","numpy","scipy")),"no local scientific evaluation")
    manifest = {
        "repository":owner.REPO,"kind":owner.MANIFEST_KIND,"scientific_kind":owner.KIND,"stage":owner.STAGE,
        "problem_id":"R147_complete_physical_nu_observation_inverse_20261127",
        "parameters":owner.PARAMETERS,"runtime":owner.RUNTIME,"target_order":owner.TARGETS,
        "complete_record_counts":[12],"allowed_scientific_fields":owner.SCI_FIELDS,
        "files":files,"expected_current_input_count":len(files),"historical_inputs":historical,"roles":roles,
        "operation":{"topic_maximum_bytes":200000000,"reserve_bytes":120000,
            "readme_pull_interval_seconds":1800,"automatic_scientific_retry":False,
            "consumed_marker":TOPIC+"/notes/physical_nu_observation_inverse_ci/consumed-target.json",
            "output_base":TOPIC+"/notes/physical_nu_observation_inverse_ci",
            "maximum_scientific_bytes":30000,"maximum_execution_bytes":50000,
            "maximum_total_publication_bytes":85000,"child_timeout_seconds":1920},
        "scope":{"same_original_selected_Q_delta_and_true_H":True,
            "only_NP_exact_even96_physical_primitive_reconstructed":True,
            "all_original_RW_carriers_restored_only_as_necessary_inputs":True,
            "all194_true_and192_raw_signed_observations_distinct":True,
            "mean_translation_removed_without_assuming_H_at_zero_is_mean":True,
            "original_same_sign_B_and_same_high_projection_retained":True,
            "whole_infinite_error_and_both_physical_means_retained":True,
            "old_trials_norms_or_pairings_recomputed":False,"unobserved_directions_recovered":False,
            "complete_high_inverse_or_true_Schur_proved":False,"topic_completion_proved":False},
    }
    raw = owner.canonical(manifest);require(len(raw) < 100000,"one whole small immutable manifest")
    return raw,WORKFLOW_TEMPLATE.replace("@MANIFEST_SHA@",owner.sha(raw)).encode()


def main():
    parser = argparse.ArgumentParser(description=__doc__);parser.add_argument("--repo",default=".",type=Path)
    parser.add_argument("--nh-actual",default=DEFAULT_NH_BASE+"/actual-strict-nu-high-forcing.json")
    parser.add_argument("--nh-execution",default=DEFAULT_NH_BASE+"/execution.json")
    parser.add_argument("--nh-manifest",default=TOPIC+"/notes/2026-11-27-strict-nu-high-forcing-inputs.json")
    args = parser.parse_args();root = args.repo.resolve();sys.dont_write_bytecode = True
    missing = [path for path in (args.nh_actual,args.nh_execution) if not (root/path).is_file()]
    if missing:
        print(json.dumps({"ready":False,"missing_complete_NH_files":missing,"manifest_or_workflow_emitted":False,
                          "scientific_targets_evaluated_locally":0},sort_keys=True));return
    actual,execution = (json.loads((root/path).read_bytes()) for path in (args.nh_actual,args.nh_execution))
    if actual.get("complete") is not True or execution.get("complete") is not True:
        print(json.dumps({"ready":False,"whole_NH_actual_complete":actual.get("complete"),
            "whole_NH_execution_complete":execution.get("complete"),"manifest_or_workflow_emitted":False,
            "scientific_targets_evaluated_locally":0},sort_keys=True));return
    raw,workflow = build(root,args.nh_actual,args.nh_execution,args.nh_manifest)
    for name,content in ((MANIFEST,raw),(WORKFLOW,workflow)):
        path = root/name;path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(content)
    print(json.dumps({"ready":True,"manifest":MANIFEST,"manifest_bytes":len(raw),
        "manifest_sha256":hashlib.sha256(raw).hexdigest(),"workflow":WORKFLOW,
        "scientific_targets_evaluated_locally":0},sort_keys=True))


if __name__ == "__main__":
    main()

