"""Freeze the complete new RCS sources and the original whole TCXV raw entry.

Metadata only.  No numerical library, old science, proposed trial, scalar
target or new mathematical computation is imported or executed.
"""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util, json
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
MANIFEST_PATH = TOPIC+"/notes/2026-11-28-signed-strict-raw-inputs.json"
WORKFLOW_PATH = ".github/workflows/fourfold-codazzi-signed-strict-raw-public.yml"
FILES = {
    "science":TOPIC+"/scripts/fourfold_codazzi_signed_strict_raw_owner.py",
    "signed_math":TOPIC+"/scripts/fourfold_codazzi_signed_complete_Airy_symbol_math.py",
    "raw_math":TOPIC+"/scripts/fourfold_codazzi_signed_strict_raw_carrier.py",
    "worker":TOPIC+"/scripts/fourfold_codazzi_signed_strict_raw_public_worker.py",
    "generator":TOPIC+"/scripts/make_signed_strict_raw_manifest.py",
    "proof":TOPIC+"/results/R149-supplement-signed-strict-coefficients-and-complete-genuine-response-input.md",
    "JWS_proof":TOPIC+"/results/R133-supplement-joint-Wiener-contraction-and-small-complete-angular-inverse.md",
    "laurent_math":TOPIC+"/scripts/fourfold_codazzi_signed_density_transport_arithmetic.py",
    "parent_manifest":TOPIC+"/notes/2026-11-28-true-root-trial-complete2677-inputs.json",
    "parent_owner":TOPIC+"/scripts/fourfold_codazzi_true_root_parallel_vector_trial_owner.py",
    "parent_worker":TOPIC+"/scripts/fourfold_codazzi_true_root_parallel_vector_public_worker.py",
    "parent_parallel_worker":TOPIC+"/scripts/fourfold_codazzi_true_root_parallel_trial_public_worker.py",
    "parent_base_worker":TOPIC+"/scripts/fourfold_codazzi_true_root_trial_public_worker.py",
}


def require(ok,message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),
                       ensure_ascii=False,allow_nan=False)+"\n").encode()


def load_metadata(path):
    spec = importlib.util.spec_from_file_location("_RCS_new_owner_metadata",path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--workflow-output",type=Path,required=True)
    args = parser.parse_args()
    root = args.repo.resolve()
    specs = []
    for role,path in FILES.items():
        body = (root/path).read_bytes()
        require(0 < len(body) < 100000,"each entire complete new current input fits")
        body.decode("utf-8")
        if path.endswith(".py"):
            ast.parse(body,filename=path)
        specs.append({"role":role,"path":path,"bytes":len(body),"sha256":sha(body),
            "git_blob_sha":hashlib.sha1(b"blob "+str(len(body)).encode()+b"\0"+body).hexdigest(),
            "encoding":"utf-8"})
    by_role = {spec["role"]:spec for spec in specs}
    owner = load_metadata(root/FILES["science"])
    require(by_role["parent_manifest"]["sha256"] == owner.PARENT_MANIFEST_SHA
            and by_role["parent_owner"]["sha256"] == owner.PARENT_OWNER_SHA
            and by_role["JWS_proof"]["sha256"] == owner.JWS_PROOF_SHA
            and by_role["laurent_math"]["sha256"] == owner.LAURENT_SHA,
            "whole original entry and same-inverse predecessor pinned without science")
    old = json.loads((root/FILES["parent_manifest"]).read_bytes())
    # The whole old input list is already in this exact admitted manifest.
    # Its descriptor closure is retained by identity, not copied incompletely.
    whole_closure = old["files"]+old["historical_inputs"]
    manifest = {
        "kind":owner.MANIFEST_KIND,"scientific_kind":owner.KIND,"repository":owner.REPOSITORY,
        "problem_id":"complete_signed_strict_raw_and_same_angular_J_20261128_v1",
        "stage":"complete_signed_strict_raw","parameters":owner.PARAMETERS,"runtime":owner.RUNTIME,
        "target_order":[owner.TARGET],"allowed_scientific_fields":sorted(owner.FIELDS),
        "files":specs,"complete_current_input_count":len(specs),
        "whole_original_raw_closure":{
            "manifest_path":FILES["parent_manifest"],"manifest_bytes":by_role["parent_manifest"]["bytes"],
            "manifest_sha256":owner.PARENT_MANIFEST_SHA,"current_input_count":len(old["files"]),
            "historical_input_count":len(old["historical_inputs"]),
            "complete_descriptors_bytes":len(canonical(whole_closure)),
            "complete_descriptors_sha256":sha(canonical(whole_closure)),
            "all40_whole_original_native_parts_required":True,
            "old_worker_prefix_stops_before_target_reservation_and_science":True},
        "operation":{"topic_maximum_bytes":200000000,"reserve_bytes":120000,
            "readme_pull_interval_seconds":1800,"automatic_scientific_retry":False,
            "maximum_total_publication_bytes":170000,"child_timeout_seconds":20100,
            "consumed_marker":TOPIC+"/notes/signed_strict_raw_ci/consumed-2026-11-28-v1.json",
            "output_base":TOPIC+"/notes/signed_strict_raw_ci"},
        "scope":{"new_signed_coefficient_and_same_J_window_target_only":True,
            "all_physical_means_and_original_frequencies_retained":True,
            "same_selected_intrinsic_and_complete_direction":True,"old_successful_targets_recomputed":0,
            "whole_global_genuine_B_gap_proved":False,"uniform_high_response_proved":False,
            "full_physical_Schur_proved":False,"topic_completion_proved":False},
    }
    raw = canonical(manifest)
    require(len(raw) < 100000,"whole complete RCS manifest below the file cap")
    require(not args.output.exists() and not args.workflow_output.exists(),
            "never overwrite a frozen first-entry manifest or workflow")
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_bytes(raw)
    digest = sha(raw)
    workflow = '''name: R149 complete signed strict coefficient and J input
on:
  push:
    branches: [main]
    paths:
      - 'WORKFLOW_PATH'
  workflow_dispatch:
permissions:
  contents: write
  actions: read
concurrency:
  group: visible-flex-exact-signed-strict-raw-20261128
  cancel-in-progress: false
jobs:
  complete-new-signed-strict-input:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-24.04
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
      - name: Install Git in the fixed original Python container
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
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_true_root_trial_public_worker.py
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_true_root_parallel_trial_public_worker.py
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_true_root_parallel_vector_public_worker.py
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_signed_strict_raw_public_worker.py
            /topics/visible-flex-exact-nearby/notes/2026-11-28-true-root-trial-complete2677-inputs.json
            /MANIFEST_PATH
      - name: Trust only the actual checkout
        run: git config --global --add safe.directory "$GITHUB_WORKSPACE"
      - name: Install the fixed original native and new directed runtime
        run: python -m pip install --disable-pip-version-check numpy==2.3.5 python-flint==0.9.0 scipy==1.17.0 sympy==1.14.0 mpmath==1.3.0
      - name: Admit whole original inputs and compute the new signed strict packet once
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: >-
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_signed_strict_raw_public_worker.py
          --repo "$GITHUB_WORKSPACE"
          --manifest MANIFEST_PATH
          --manifest-sha MANIFEST_SHA
'''.replace("WORKFLOW_PATH",WORKFLOW_PATH).replace("MANIFEST_PATH",MANIFEST_PATH).replace("MANIFEST_SHA",digest)
    args.workflow_output.parent.mkdir(parents=True,exist_ok=True)
    args.workflow_output.write_text(workflow)
    print(canonical({"manifest":str(args.output),"bytes":len(raw),"sha256":digest,
        "complete_current_files":len(specs),"whole_parent_current_files":len(old["files"]),
        "whole_parent_history_files":len(old["historical_inputs"]),
        "workflow_bytes":len(workflow.encode()),"workflow_sha256":sha(workflow.encode()),
        "workflow_destination":WORKFLOW_PATH,"new_or_old_scientific_calls":0}).decode(),end="")


if __name__ == "__main__":
    main()
