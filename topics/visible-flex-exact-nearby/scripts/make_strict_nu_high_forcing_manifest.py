"""Metadata-only NH entry, emitted only after a whole genuine NP success.

The generator reads complete NP/JC results and original small definitions.
Missing or incomplete NP input produces readiness only, never a manifest,
workflow or actual scientific conclusion. No numerical library is imported.
"""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util, json, subprocess, sys
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
OWNER = TOPIC+"/scripts/fourfold_codazzi_strict_nu_high_forcing_owner.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_strict_nu_high_forcing_public_worker.py"
GENERATOR = TOPIC+"/scripts/make_strict_nu_high_forcing_manifest.py"
MANIFEST = TOPIC+"/notes/2026-11-27-strict-nu-high-forcing-inputs.json"
WORKFLOW = ".github/workflows/visible-exact-strict-nu-high-forcing.yml"
DEFAULT_NP_BASE = TOPIC+"/notes/strict_nu_particular_ci/run-45893562391-1"

WORKFLOW_TEMPLATE = '''name: R147 complete true strict nu high forcing
on:
  push:
    branches: [main]
    paths:
      - '.github/workflows/visible-exact-strict-nu-high-forcing.yml'
  workflow_dispatch:
permissions:
  contents: write
concurrency:
  group: visible-flex-exact-strict-nu-high-forcing-20261127
  cancel-in-progress: false
jobs:
  complete-twelve-new-scalar-bounds:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-latest
    timeout-minutes: 20
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
            /topics/visible-flex-exact-nearby/notes/2026-11-27-strict-nu-high-forcing-inputs.json
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install the fixed directed scalar runtime
        run: python -m pip install --disable-pip-version-check python-flint==0.9.0
      - name: Receive the complete actual parameter column in the true high target
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: >-
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_strict_nu_high_forcing_public_worker.py
          --repo "$GITHUB_WORKSPACE"
          --manifest topics/visible-flex-exact-nearby/notes/2026-11-27-strict-nu-high-forcing-inputs.json
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


def build(root,np_actual,np_execution,np_manifest):
    require(not any(x in sys.modules for x in ("numpy","flint","scipy")),"metadata-only start")
    sys.dont_write_bytecode = True
    owner = load(root,OWNER,"_NH_metadata_owner")
    worker = load(root,WORKER,"_NH_metadata_worker")
    math = load(root,owner.MATH,"_NH_pure_definitions")
    require(owner.SOURCE == OWNER and owner.WORKER == WORKER and owner.GENERATOR == GENERATOR
            and list(math.OUTPUT_ORDER) == owner.TARGETS,"whole concrete new scalar entry")
    compile(worker.build_adapter(root),WORKER,"exec")
    declared = owner.gather(root,np_actual,np_execution,np_manifest)
    files,historical,roles = (declared[key] for key in ("files","historical_inputs","roles"))
    raws = {x["path"]:(root/x["path"]).read_bytes() for x in files}
    paths = {x["path"]:root/x["path"] for x in files}
    for item in historical:
        raw = subprocess.run(["git","show",item["commit"]+":"+item["path"]],
            cwd=root,capture_output=True,check=True).stdout
        require(len(raw) == item["bytes"] and owner.sha(raw) == item["sha256"],"whole saved original native")
        raws[item["path"]] = raw
    prior = owner.admit(declared,raws,paths)
    require(prior["NP"]["complete"] is prior["JC"]["complete"] is True,
            "both genuine whole predecessors completed")
    review = owner.parse(raws[roles["reviewed_rules"]])
    require(review["repository"] == owner.REPO
            and review["new_unread_rules_must_still_be_reported_and_applied"] is True
            and set(review["readme_sha256"]) == {"README.md",TOPIC+"/README.md"},
            "both complete reviewed rule files")
    for relative,digest in review["readme_sha256"].items():
        require(owner.sha((root/relative).read_bytes()) == digest,"already read README unchanged: "+relative)
    require(review["large_data_policy"]["maximum_topic_bytes"] == 200000000
            and review["large_data_policy"]["original_completed_mathematics_must_not_be_recomputed"] is True
            and not any(x in sys.modules for x in ("numpy","flint","scipy")),
            "same no-replay rule and no local numerical computation")
    manifest = {
        "repository":owner.REPO,"kind":owner.MANIFEST_KIND,"scientific_kind":owner.KIND,"stage":owner.STAGE,
        "problem_id":"R147_complete_true_strict_nu_high_forcing_20261127",
        "parameters":owner.PARAMETERS,"runtime":owner.RUNTIME,"target_order":owner.TARGETS,
        "complete_record_counts":[12],"allowed_scientific_fields":owner.SCI_FIELDS,
        "files":files,"expected_current_input_count":len(files),"historical_inputs":historical,"roles":roles,
        "operation":{"topic_maximum_bytes":200000000,"reserve_bytes":120000,
            "readme_pull_interval_seconds":1800,"automatic_scientific_retry":False,
            "consumed_marker":TOPIC+"/notes/strict_nu_high_forcing_ci/consumed-target.json",
            "output_base":TOPIC+"/notes/strict_nu_high_forcing_ci",
            "maximum_scientific_bytes":26000,"maximum_execution_bytes":46000,
            "maximum_total_publication_bytes":76000,"child_timeout_seconds":240},
        "scope":{"same_true_selected_H_full_derivative_Wiener_sum":True,
            "JC_homotopy_lower_includes_true_H_endpoint":True,
            "whole_NP_true_and_raw_signed_observations_retained":True,
            "complete_paired_high97_source_without_sine_truncation":True,
            "both_physical_means_retained":True,"old_trials_norms_or_pairings_recomputed":False,
            "complete_high_inverse_or_true_Schur_proved":False,"topic_completion_proved":False},
    }
    raw = owner.canonical(manifest)
    require(len(raw) < 100000,"whole small actual-input manifest")
    return raw,WORKFLOW_TEMPLATE.replace("@MANIFEST_SHA@",owner.sha(raw)).encode()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",default=".",type=Path)
    parser.add_argument("--np-actual",default=DEFAULT_NP_BASE+"/actual-strict-nu-particular.json")
    parser.add_argument("--np-execution",default=DEFAULT_NP_BASE+"/execution.json")
    parser.add_argument("--np-manifest",default=TOPIC+"/notes/2026-11-27-strict-nu-particular-inputs.json")
    args = parser.parse_args();root = args.repo.resolve();sys.dont_write_bytecode = True
    missing = [name for name in (args.np_actual,args.np_execution) if not (root/name).is_file()]
    if missing:
        print(json.dumps({"ready":False,"missing_whole_actual_NP_files":missing,
            "manifest_or_workflow_emitted":False,"scientific_targets_evaluated_locally":0},sort_keys=True));return
    actual,execution = (json.loads((root/name).read_bytes()) for name in (args.np_actual,args.np_execution))
    if actual.get("complete") is not True or execution.get("complete") is not True:
        print(json.dumps({"ready":False,"whole_NP_actual_complete":actual.get("complete"),
            "whole_NP_execution_complete":execution.get("complete"),
            "manifest_or_workflow_emitted":False,"scientific_targets_evaluated_locally":0},sort_keys=True));return
    raw,workflow = build(root,args.np_actual,args.np_execution,args.np_manifest)
    for name,content in ((MANIFEST,raw),(WORKFLOW,workflow)):
        path = root/name;path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(content)
    print(json.dumps({"ready":True,"manifest":MANIFEST,"manifest_bytes":len(raw),
        "manifest_sha256":hashlib.sha256(raw).hexdigest(),"workflow":WORKFLOW,
        "scientific_targets_evaluated_locally":0},sort_keys=True))


if __name__ == "__main__":
    main()
