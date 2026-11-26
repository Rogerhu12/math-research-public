"""Metadata-only PA entry from one whole completed NP scientific outcome.

All original NP descriptors are retained.  Only the four small original
definitions required by readonly admission are materialized locally; the
47 complete native carrier inputs are restored and checked by Actions.
"""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util, json, subprocess, sys
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
OWNER = TOPIC+"/scripts/fourfold_codazzi_strict_nu_amplitude_border_owner.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_strict_nu_amplitude_border_public_worker.py"
GENERATOR = TOPIC+"/scripts/make_strict_nu_amplitude_border_manifest.py"
MANIFEST = TOPIC+"/notes/2026-11-27-strict-nu-amplitude-border-inputs.json"
WORKFLOW = ".github/workflows/visible-exact-strict-nu-amplitude-border.yml"
DEFAULT_NP_BASE = TOPIC+"/notes/strict_nu_particular_ci/run-45893562391-1"

WORKFLOW_TEMPLATE = '''name: R147 true strict nu amplitude border
on:
  push:
    branches: [main]
    paths:
      - '.github/workflows/visible-exact-strict-nu-amplitude-border.yml'
  workflow_dispatch:
permissions:
  contents: write
concurrency:
  group: visible-flex-exact-strict-nu-amplitude-border-20261127
  cancel-in-progress: false
jobs:
  complete-new-amplitude-border:
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
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_strict_nu_amplitude_border_public_worker.py
            /topics/visible-flex-exact-nearby/notes/2026-11-27-strict-nu-amplitude-border-inputs.json
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install the same original directed and carrier runtime
        run: python -m pip install --disable-pip-version-check numpy==2.3.5 python-flint==0.9.0
      - name: Receive the actual strict parameter in the true physical amplitude row
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: >-
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_strict_nu_amplitude_border_public_worker.py
          --repo "$GITHUB_WORKSPACE"
          --manifest topics/visible-flex-exact-nearby/notes/2026-11-27-strict-nu-amplitude-border-inputs.json
          --manifest-sha @MANIFEST_SHA@
'''


def require(ok,message):
    if not ok:
        raise ValueError(message)


def load(root,relative,name):
    raw = (root/relative).read_bytes();require(0 < len(raw) < 100000,"whole small source")
    ast.parse(raw.decode(),filename=relative)
    spec = importlib.util.spec_from_file_location(name,root/relative)
    module = importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


def build(root,np_actual,np_execution,np_manifest):
    require(not any(name in sys.modules for name in ("flint","numpy","scipy")),"metadata-only start")
    sys.dont_write_bytecode = True
    owner = load(root,OWNER,"_PA_metadata_owner");worker = load(root,WORKER,"_PA_metadata_worker")
    math = load(root,owner.MATH,"_PA_pure_definitions")
    load(root,owner.RESTORE,"_PA_pure_carrier_restore_definitions")
    require(owner.SOURCE == OWNER and owner.WORKER == WORKER and owner.GENERATOR == GENERATOR
        and list(math.OUTPUT_ORDER) == owner.TARGETS and math.SIGNED_INDICES == owner.SIGNED_INDICES,
        "complete new concrete amplitude entry")
    compile(worker.build_adapter(root),WORKER,"exec")
    declared = owner.gather(root,np_actual,np_execution,np_manifest)
    files,historical,roles = (declared[key] for key in ("files","historical_inputs","roles"))
    raws = {item["path"]:(root/item["path"]).read_bytes() for item in files}
    paths = {item["path"]:root/item["path"] for item in files}
    small = [item for item in historical if item["role"].startswith("NP_RW_")]
    require(len(small) == 4,"all four whole native definitions needed for metadata admission")
    for item in small:
        raw = subprocess.run(["git","show",item["commit"]+":"+item["path"]],
            cwd=root,capture_output=True,check=True).stdout
        require(len(raw) == item["bytes"] and owner.sha(raw) == item["sha256"],"whole saved original small native")
        raws[item["path"]] = raw
    admitted = owner.admit(declared,raws,paths)
    require(admitted["NP"]["complete"] is True,"the genuine whole NP already completed")
    # The whole NP manifest and actual success already identify ALL51
    # historical descriptors.  No local PDE carrier reconstruction occurs.
    original_history = admitted["NP_manifest"]["historical_inputs"]
    require(historical == [dict(item,role="NP_"+item["role"]) for item in original_history],
            "every original historical descriptor preserved verbatim apart from role namespace")
    review = owner.parse(raws[roles["reviewed_rules"]])
    require(review["repository"] == owner.REPO
        and review["new_unread_rules_must_still_be_reported_and_applied"] is True
        and set(review["readme_sha256"]) == {"README.md",TOPIC+"/README.md"},"both whole reviewed README files")
    for relative,digest in review["readme_sha256"].items():
        require(owner.sha((root/relative).read_bytes()) == digest,"already reviewed README unchanged: "+relative)
    require(review["large_data_policy"]["maximum_topic_bytes"] == 200000000
        and review["large_data_policy"]["original_completed_mathematics_must_not_be_recomputed"] is True
        and not any(name in sys.modules for name in ("flint","numpy","scipy")),"no local scientific evaluation")
    manifest = {
        "repository":owner.REPO,"kind":owner.MANIFEST_KIND,"scientific_kind":owner.KIND,"stage":owner.STAGE,
        "problem_id":"R147_complete_strict_nu_amplitude_border_20261127","parameters":owner.PARAMETERS,
        "runtime":owner.RUNTIME,"target_order":owner.TARGETS,"complete_record_counts":[8],
        "allowed_scientific_fields":owner.SCI_FIELDS,"files":files,"expected_current_input_count":len(files),
        "historical_inputs":historical,"roles":roles,
        "operation":{"topic_maximum_bytes":200000000,"reserve_bytes":120000,
            "readme_pull_interval_seconds":1800,"automatic_scientific_retry":False,
            "consumed_marker":TOPIC+"/notes/strict_nu_amplitude_border_ci/consumed-target.json",
            "output_base":TOPIC+"/notes/strict_nu_amplitude_border_ci",
            "maximum_scientific_bytes":22000,"maximum_execution_bytes":58000,
            "maximum_total_publication_bytes":85000,"child_timeout_seconds":1920},
        "scope":{"same_original_selected_Q_delta":True,"whole_original_NP_private_carriers_only_restored":True,
            "same_four_full_original_trial_array_hashes_required":True,"whole_old97_physical_amplitude_directions":True,
            "complete_selected_row_change_paid_in_primitive_plus_mean_dual":True,
            "full_infinite_NP_error_and_both_density_means_retained":True,
            "physical_and_exact_alpha_normalized_signed_balls_separate":True,
            "old_residual_or_pairing_targets_recomputed":False,"new_trial_chosen":False,
            "old_amplitude_Bessel_or_row_targets_recomputed":False,"nonlocal_phase_column_proved":False,
            "true_Schur_or_topic_completion_proved":False},
    }
    raw = owner.canonical(manifest);require(len(raw) < 100000,"whole small immutable manifest")
    return raw,WORKFLOW_TEMPLATE.replace("@MANIFEST_SHA@",owner.sha(raw)).encode()


def main():
    parser = argparse.ArgumentParser(description=__doc__);parser.add_argument("--repo",default=".",type=Path)
    parser.add_argument("--np-actual",default=DEFAULT_NP_BASE+"/actual-strict-nu-particular.json")
    parser.add_argument("--np-execution",default=DEFAULT_NP_BASE+"/execution.json")
    parser.add_argument("--np-manifest",default=TOPIC+"/notes/2026-11-27-strict-nu-particular-inputs.json")
    args = parser.parse_args();root = args.repo.resolve();sys.dont_write_bytecode = True
    missing = [path for path in (args.np_actual,args.np_execution) if not (root/path).is_file()]
    if missing:
        print(json.dumps({"ready":False,"missing_whole_NP_files":missing,"manifest_or_workflow_emitted":False,
                          "scientific_targets_evaluated_locally":0},sort_keys=True));return
    actual,execution = (json.loads((root/path).read_bytes()) for path in (args.np_actual,args.np_execution))
    if actual.get("complete") is not True or execution.get("complete") is not True:
        print(json.dumps({"ready":False,"whole_NP_actual_complete":actual.get("complete"),
            "whole_NP_execution_complete":execution.get("complete"),"manifest_or_workflow_emitted":False,
            "scientific_targets_evaluated_locally":0},sort_keys=True));return
    raw,workflow = build(root,args.np_actual,args.np_execution,args.np_manifest)
    for name,content in ((MANIFEST,raw),(WORKFLOW,workflow)):
        path = root/name;path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(content)
    print(json.dumps({"ready":True,"manifest":MANIFEST,"manifest_bytes":len(raw),
        "manifest_sha256":hashlib.sha256(raw).hexdigest(),"workflow":WORKFLOW,
        "scientific_targets_evaluated_locally":0},sort_keys=True))


if __name__ == "__main__":
    main()

