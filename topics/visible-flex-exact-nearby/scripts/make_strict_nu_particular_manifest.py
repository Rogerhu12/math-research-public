"""Metadata-only entry for the new full selected strict nu particular.

Reads complete old output objects and original native input metadata.  It
does not import numerical packages or evaluate a trial, source, residual,
norm or signed pairing.  Only the public child evaluates those new targets.
"""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util, json, subprocess, sys
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
OWNER = TOPIC+"/scripts/fourfold_codazzi_strict_nu_particular_owner.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_strict_nu_particular_public_worker.py"
GENERATOR = TOPIC+"/scripts/make_strict_nu_particular_manifest.py"
MANIFEST = TOPIC+"/notes/2026-11-27-strict-nu-particular-inputs.json"
WORKFLOW = ".github/workflows/visible-exact-strict-nu-particular.yml"

WORKFLOW_TEMPLATE = '''name: R147 full selected strict nu particular and signed waist column
on:
  push:
    branches: [main]
    paths:
      - '.github/workflows/visible-exact-strict-nu-particular.yml'
  workflow_dispatch:
permissions:
  contents: write
concurrency:
  group: visible-flex-exact-strict-nu-particular-20261127
  cancel-in-progress: false
jobs:
  complete-forced-trial-and-signed-column:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-latest
    timeout-minutes: 140
    env:
      OMP_NUM_THREADS: '1'
      OPENBLAS_NUM_THREADS: '1'
      MKL_NUM_THREADS: '1'
      NUMEXPR_NUM_THREADS: '1'
      BLIS_NUM_THREADS: '1'
      VECLIB_MAXIMUM_THREADS: '1'
      OPENBLAS_CORETYPE: Haswell
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
            /topics/visible-flex-exact-nearby/notes/2026-11-27-strict-nu-particular-inputs.json
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install the fixed directed and floating runtime
        run: python -m pip install --disable-pip-version-check numpy==2.3.5 python-flint==0.9.0
      - name: Certify the complete strict forced trial and all signed waist observations
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: >-
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_strict_nu_particular_public_worker.py
          --repo "$GITHUB_WORKSPACE"
          --manifest topics/visible-flex-exact-nearby/notes/2026-11-27-strict-nu-particular-inputs.json
          --manifest-sha @MANIFEST_SHA@
'''


def require(ok, message):
    if not ok:
        raise ValueError(message)


def module(root, relative, name):
    raw = (root/relative).read_bytes()
    require(0 < len(raw) < 100000, "whole small metadata source")
    ast.parse(raw.decode(),filename=relative)
    spec = importlib.util.spec_from_file_location(name,root/relative)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def build(root):
    require(Path(__file__).resolve() == (root/GENERATOR).resolve(), "this exact local generator")
    require(not any(x in sys.modules for x in ("flint","numpy","scipy")), "metadata-only start")
    sys.dont_write_bytecode = True
    owner = module(root,OWNER,"_NP_metadata_owner")
    worker = module(root,WORKER,"_NP_metadata_public_worker")
    require(owner.SOURCE == OWNER and owner.WORKER == WORKER and owner.GENERATOR == GENERATOR,
            "the same complete new scientific entry")
    compile(worker.build_adapter(root),WORKER,"exec")
    declared = owner.gather(root)
    files,historical,roles = (declared[key] for key in ("files","historical_inputs","roles"))
    raws = {x["path"]:(root/x["path"]).read_bytes() for x in files}
    paths = {x["path"]:root/x["path"] for x in files}
    for item in historical:
        if item["role"].startswith("RW_"):
            raw = subprocess.run(["git","show",item["commit"]+":"+item["path"]],
                cwd=root,capture_output=True,check=True).stdout
            require(len(raw) == item["bytes"] and owner.sha(raw) == item["sha256"],
                    "whole original saved RW scalar/definition object")
            raws[item["path"]] = raw
    prior = owner.admit_current(declared,raws,paths)
    require(len(historical) == 51 and len({x["role"] for x in files+historical}) == len(files)+51
            and len({x["path"] for x in files+historical}) == len(files)+51,
            "whole current closure and all51 distinct original native/definition objects")
    current_by_role = {x["role"]:x for x in files}
    require(current_by_role["SL_worker"]["path"] == worker.ADAPTER
            and current_by_role["SL_worker"]["sha256"] == worker.ADAPTER_SHA,
            "the unchanged complete old public adapter")
    review = owner.parse(raws[roles["reviewed_rules"]])
    require(review["repository"] == owner.REPO
            and review["new_unread_rules_must_still_be_reported_and_applied"] is True
            and set(review["readme_sha256"]) == {"README.md",TOPIC+"/README.md"},
            "explicit review of both READMEs")
    for relative,digest in review["readme_sha256"].items():
        raw = (root/relative).read_bytes()
        require(0 < len(raw) < 100000 and owner.sha(raw) == digest,
                "current README equals the already read rules: "+relative)
    require(review["large_data_policy"]["maximum_topic_bytes"] == 200000000
            and review["large_data_policy"]["original_completed_mathematics_must_not_be_recomputed"] is True
            and review["large_data_policy"]["keep_only_scripts_parameters_runs_output_hashes_and_conclusions"] is True,
            "the unchanged storage and completed-target requirements")
    require(prior["R147"]["reference_identity"] == prior["RW"]["family"]
            and not any(x in sys.modules for x in ("flint","numpy","scipy")),
            "whole original selected family admitted without scientific execution")
    manifest = {
        "repository":owner.REPO,"kind":owner.MANIFEST_KIND,"scientific_kind":owner.KIND,
        "stage":owner.STAGE,"problem_id":"R147_true_selected_strict_nu_particular_20261127",
        "parameters":owner.PARAMETERS,"target_order":owner.TARGETS,
        "complete_record_counts":[2],"allowed_scientific_fields":owner.SCI_FIELDS,
        "files":files,"expected_current_input_count":len(files),
        "historical_inputs":historical,"roles":roles,"runtime":owner.RUNTIME,
        "operation":{
            "topic_maximum_bytes":200000000,"reserve_bytes":120000,
            "readme_pull_interval_seconds":1800,"automatic_scientific_retry":False,
            "consumed_marker":TOPIC+"/notes/strict_nu_particular_ci/consumed-target.json",
            "output_base":TOPIC+"/notes/strict_nu_particular_ci",
            "maximum_scientific_bytes":75000,"maximum_execution_bytes":65000,
            "maximum_total_publication_bytes":145000,"child_timeout_seconds":7500},
        "scope":{
            "new_complete_targets":2,"new_whole_signed_output_balls":194,
            "same_evaluation_uninflated_signed_trial_pairings":192,
            "old_completed_scientific_target_calls":0,
            "same_original_implicit_selected_member":True,
            "full_centre_M32_base_native_parts":5,"full_original_common_row_parts":40,
            "direction_shards_or_old_QR_reconstructed":False,
            "full_Hminus1_source_receiver_and_both_means_retained":True,
            "selected_operator_difference_from_whole_old_D_balls":True,
            "selected_parameter_source_difference_from_whole_old_D_ball":True,
            "positive_chain_or_incoming_inverse_preconditions":False,
            "complete_incoming_inverse_or_true_Schur_claimed":False,
            "topic_completion_claimed":False},
    }
    raw = owner.canonical(manifest)
    require(len(raw) < 100000, "whole small frozen new-target manifest")
    workflow = WORKFLOW_TEMPLATE.replace("@MANIFEST_SHA@",owner.sha(raw)).encode()
    return raw,workflow


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",default=".",type=Path)
    parser.add_argument("--manifest-out",default=MANIFEST)
    parser.add_argument("--workflow-out",default=WORKFLOW)
    args = parser.parse_args()
    require(args.manifest_out == MANIFEST and args.workflow_out == WORKFLOW,
            "one concrete new target entry")
    root = args.repo.resolve()
    manifest,workflow = build(root)
    for relative,raw in ((MANIFEST,manifest),(WORKFLOW,workflow)):
        path = root/relative
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_bytes(raw)
    print(json.dumps({"manifest":MANIFEST,"manifest_bytes":len(manifest),
        "manifest_sha256":hashlib.sha256(manifest).hexdigest(),"workflow":WORKFLOW,
        "scientific_targets_evaluated_locally":0},sort_keys=True))


if __name__ == "__main__":
    main()
