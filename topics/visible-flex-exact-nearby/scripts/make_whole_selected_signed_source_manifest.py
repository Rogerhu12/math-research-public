"""Freeze the complete WSS source closure and its single first public entry. Metadata only."""
import argparse
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import sys


TOPIC="topics/visible-flex-exact-nearby"
BASE=TOPIC+"/scripts/fourfold_codazzi_whole_selected_signed_source"
MANIFEST=TOPIC+"/notes/2026-11-28-whole-selected-signed-sources-inputs.json"
WORKFLOW=".github/workflows/fourfold-codazzi-whole-selected-signed-sources-public.yml"
FILES={
    "science":BASE+"_owner.py","carrier":BASE+"_carrier.py","worker":BASE+"_public_worker.py",
    "generator":TOPIC+"/scripts/make_whole_selected_signed_source_manifest.py",
    "proof":TOPIC+"/results/R149-supplement-whole-signed-selected-both-ordinary-sources.md",
    "positive_signed_source":TOPIC+"/scripts/fourfold_codazzi_selected_positive_signed_sources.py",
    "positive_signed_proof":TOPIC+"/results/R149-supplement-selected-signed-Newton-nu-and-whole-cell-Grassmann-response.md",
    "D_formula":TOPIC+"/results/R133-supplement-exact-selected-parameter-core-differences-and-finite193-transfer.md",
    "compact_polynomial":TOPIC+"/results/R144-supplement-signed-metric-mean-moments-and-compact-parameter-lift.md",
    "raw_input_helper":TOPIC+"/scripts/fourfold_codazzi_signed_strict_raw_owner.py",
    "raw_transport":TOPIC+"/scripts/fourfold_codazzi_signed_strict_raw_public_worker.py",
    "parent_manifest":TOPIC+"/notes/2026-11-28-true-root-trial-complete2677-inputs.json",
    "parent_owner":TOPIC+"/scripts/fourfold_codazzi_true_root_parallel_vector_trial_owner.py",
    "parent_worker":TOPIC+"/scripts/fourfold_codazzi_true_root_parallel_vector_public_worker.py",
    "parent_parallel_worker":TOPIC+"/scripts/fourfold_codazzi_true_root_parallel_trial_public_worker.py",
    "parent_base_worker":TOPIC+"/scripts/fourfold_codazzi_true_root_trial_public_worker.py",
    "resource_carriers":TOPIC+"/scripts/fourfold_codazzi_true_low193_grassmann_carriers.py",
    "resource_directory":TOPIC+"/scripts/fourfold_codazzi_true_low193_grassmann_runner.py",
    "current_reviewed_rules":TOPIC+"/notes/2026-11-28-read-public-model-ultra-rules.json",
}


def require(ok,message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,
                       allow_nan=False)+"\n").encode()


def source_workflow(digest):
    sparse=sorted(set(FILES.values())|{"README.md",TOPIC+"/README.md",MANIFEST})
    text="""name: R149 whole selected signed Newton and nu ordinary sources
on:
  push:
    branches: [main]
    paths: ['@WORKFLOW@']
permissions:
  contents: write
  actions: read
concurrency:
  group: R149-whole-selected-signed-sources-v1
  cancel-in-progress: false
jobs:
  signed-sources:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-24.04
    timeout-minutes: 360
    container: python@sha256:4d1caded1f729ae443eb803f26ffde7b61e696aeaef62f099abb6dd6b14257c7
    env:
      OPENBLAS_CORETYPE: Haswell
      OPENBLAS_NUM_THREADS: '1'
      OMP_NUM_THREADS: '1'
      MKL_NUM_THREADS: '1'
      BLIS_NUM_THREADS: '1'
      VECLIB_MAXIMUM_THREADS: '1'
      NUMEXPR_NUM_THREADS: '1'
    steps:
      - name: Install Git in the original container
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
@SPARSE@
      - name: Trust the original mounted checkout
        run: git config --global --add safe.directory "$GITHUB_WORKSPACE"
      - name: Install the original native restoration and signed source runtime
        run: >-
          python -m pip install --disable-pip-version-check --only-binary=:all:
          numpy==2.3.5 python-flint==0.9.0 scipy==1.17.0 sympy==1.14.0 mpmath==1.3.0
      - name: Admit all original inputs and compute both complete signed source targets
        env:
          GITHUB_TOKEN: __EXPRESSION__
        run: >-
          python @WORKER@
          --repo "$GITHUB_WORKSPACE" --manifest @MANIFEST@ --manifest-sha @SHA@
"""
    return (text.replace("@WORKFLOW@",WORKFLOW).replace("@SPARSE@","\n".join("            /"+s for s in sparse))
        .replace("__EXPRESSION__","$"+"{{ secrets.GITHUB_TOKEN }}").replace("@WORKER@",FILES["worker"])
        .replace("@MANIFEST@",MANIFEST).replace("@SHA@",digest))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    ap.add_argument("--workflow-output",type=Path,required=True)
    a=ap.parse_args()
    root=a.repo.resolve()
    specs=[]
    for role,name in FILES.items():
        raw=(root/name).read_bytes()
        require(0<len(raw)<100000,"entire small code/proof/metadata file")
        if name.endswith(".py"):
            ast.parse(raw,filename=name)
        spec={"role":role,"path":name,"bytes":len(raw),"sha256":sha(raw),
              "git_blob_sha":hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest(),"encoding":"utf-8"}
        specs.append(spec)
    roles={s["role"]:s for s in specs}
    spec=importlib.util.spec_from_file_location("_WSS_owner_metadata",root/FILES["science"])
    owner=importlib.util.module_from_spec(spec);spec.loader.exec_module(owner)
    require(not any(k in sys.modules for k in ("numpy","flint","scipy")) and
            roles["parent_manifest"]["sha256"]==owner.PARENT_MANIFEST_SHA and
            roles["parent_owner"]["sha256"]==owner.PARENT_OWNER_SHA and
            roles["positive_signed_source"]["sha256"]=="71932ab306f3b1755f3dc120c0a7a1d63998efbdc8cef8e12866c0b70c559462",
            "whole original true-root closure and already frozen positive signed formula")
    parent=json.loads((root/FILES["parent_manifest"]).read_bytes())
    inherited=parent["files"]+parent["historical_inputs"]
    require(len(parent["files"])==184 and len(parent["historical_inputs"])==32,"original 184/32 closure")
    review=json.loads((root/FILES["current_reviewed_rules"]).read_bytes())
    require(review["repository"]==owner.REPOSITORY and review["model"]=="gpt-6.2-astra"
       and review["reasoning_effort"]=="ultra" and review["large_data_policy"]["original_completed_mathematics_must_not_be_recomputed"]
       and all(sha((root/path).read_bytes())==digest for path,digest in review["readme_sha256"].items()),
       "complete actually read operational rules, separate from old scientific inputs")
    result={"kind":owner.MANIFEST_KIND,"scientific_kind":owner.KIND,"problem_id":"whole_selected_body_signed_577x2_v1",
        "repository":owner.REPOSITORY,"parameters":owner.PARAMETERS,"runtime":owner.RUNTIME,
        "allowed_scientific_fields":sorted(owner.FIELDS),"target_order":owner.TARGETS,"files":specs,
        "whole_original_descriptors":{"bytes":len(canonical(inherited)),"sha256":sha(canonical(inherited))},
        "reviewed_rules":roles["current_reviewed_rules"],"operation":{"topic_maximum_bytes":200000000,"reserve_bytes":120000,
            "maximum_total_publication_bytes":196000,"child_timeout_seconds":20100,"automatic_scientific_retry":False,
            "consumed_marker":TOPIC+"/notes/whole_selected_signed_sources_ci/consumed-v1.json",
            "output_base":TOPIC+"/notes/whole_selected_signed_sources_ci"}}
    raw=canonical(result)
    digest=sha(raw)
    require(not a.output.exists() and not a.workflow_output.exists(),"fresh whole WSS entry only")
    workflow=source_workflow(digest)
    require(len(raw)<100000 and len(workflow.encode())<100000,"whole WSS metadata and workflow")
    for path,body in ((a.output,raw),(a.workflow_output,workflow.encode())):
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_bytes(body)
        require(path.read_bytes()==body,"whole metadata write/read equality")
    print(canonical({"manifest_bytes":len(raw),"manifest_sha256":digest,"current_files":len(specs),
        "whole_original_current":184,"whole_original_historical":32,"math_calls":0}).decode(),end="")


if __name__=="__main__":
    main()
