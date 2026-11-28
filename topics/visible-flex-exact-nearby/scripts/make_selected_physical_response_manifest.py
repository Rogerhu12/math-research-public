"""Create the first new joint response entry from genuinely complete GG, WSS and FHC receipts."""
import argparse
import ast
from hashlib import sha1,sha256
import importlib.util
import json
from pathlib import Path

TOPIC="topics/visible-flex-exact-nearby"
KIND="R149_actual_selected_physical_response_inputs_v1"
SCRIPTS={
    "science":"fourfold_codazzi_selected_physical_response_owner.py",
    "worker":"fourfold_codazzi_selected_physical_response_public_worker.py",
    "generator":"make_selected_physical_response_manifest.py",
    "grr":"fourfold_codazzi_grassmann_response_graph_restore.py",
    "gbc":"fourfold_codazzi_grassmann_all_boundary_columns.py",
    "srr":"fourfold_codazzi_whole_signed_response_source_restore.py",
    "gsr":"fourfold_codazzi_grassmann_signed_response.py",
    "sar":"fourfold_codazzi_selected_affine_response.py",
    "gtp":"fourfold_codazzi_grassmann_physical_consumer_math.py",
    "npg":"fourfold_codazzi_nearby_physical_received_response.py",
    "fhc":"fourfold_codazzi_positive_selected_far_height_loop.py",
    "independent":"fourfold_codazzi_selected_independent_port_rows.py",
}
ANCHOR_ROLES={"gh5_actual":"completed_actual_GH_source_fees_actual","gh5_execution":"completed_actual_GH_source_fees_execution",
    "gh4_actual":"completed_actual_GH_head_response_actual","gh4_execution":"completed_actual_GH_head_response_execution",
    "L_actual":"completed_original_low_family_actual","L_execution":"completed_original_low_family_execution",
    "base0":"completed_actual_base0_high_summary","base0_process":"completed_actual_base0_high_process",
    "negative":"negative_one_summary","negative_process":"negative_one_process","high_admit":"actual_GH_source_fees_math"}
NOTES={
    "gg_manifest":"2026-11-28-true-low193-grassmann-inputs.json",
    "wss_manifest":"2026-11-28-whole-selected-signed-sources-inputs.json",
    "wss_actual":"whole_selected_signed_sources_ci/run-46136409179-1/whole-selected-signed-source.json",
    "wss_execution":"whole_selected_signed_sources_ci/run-46136409179-1/execution.json",
    "D_actual":"reference_boundary_lifts_ci/run-44745017016-1/actual-scientific-conclusion.json",
    "D_execution":"reference_boundary_lifts_ci/run-44745017016-1/execution.json",
    "D_manifest":"2026-11-20-reference-boundary-lifts-thread-recovery-inputs.json",
    "weighted_actual":"actual_GH_weighted_response_ci/run-44746534556-1/actual-scientific-conclusion.json",
    "weighted_execution":"actual_GH_weighted_response_ci/run-44746534556-1/execution.json",
    "weighted_manifest":"2026-11-20-actual-GH-weighted-response-inputs.json",
    "SPN":"2026-11-28-SPN-complete-saved-consequence.json","OHR":"2026-11-28-OHR-complete-saved-consequence.json",
    "WHN":"2026-11-28-WHN-complete-saved-consequence.json","FHC":"2026-11-28-FHC-complete-saved-consequence.json",
    "NPG_fees":"2026-11-28-NPG-root-new-exact-fees.json",
    "OA":"selected_physical_outer_values_ci/run-44769445246-1/selected-physical-outer-values.json",
    "outer":"full_delta_positive_ci/run-43615531666-1-full-real-delta-positive/evidence/full-delta-complete-regular-Hs-outer-summary.json",
    "WOB":"outer_rows_and_rough_positive_observations_ci/run-43844596176-1/actual-scientific-conclusion.json",
    "operational_review":"2026-11-28-read-public-model-ultra-rules.json",
}
PROOFS={"GBC":"all-signed-hybrid-boundary-columns-and-terminal-physical-preconditioner",
        "GRR":"whole-signed-response-graph-carrier-recovery",
        "SAR":"signed-selected-affine-columns-and-true-high-return-at-the-cut",
        "NPG":"nonlinear-neighbourhood-physical-inverse-and-received-columns",
        "FHC":"selected-far-height-feedback-through-the-true-physical-cut",
        "GSA":"public-signed-physical-response-and-independent-port-columns"}


def require(ok,message):
    if not ok:
        raise ValueError(message)


def load(p,name):
    spec=importlib.util.spec_from_file_location(name,p)
    obj=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ("repo","gg-result-dir","manifest-out","workflow-out"):
        ap.add_argument("--"+name,type=Path,required=True)
    ap.add_argument("--fhc-receipt",type=Path)
    ap.add_argument("--reviewed-rules",type=Path)
    a=ap.parse_args()
    root=a.repo.resolve()
    def rel(p):
        result=(root/p).resolve().relative_to(root).as_posix()
        require(result.startswith(TOPIC+"/"),"whole actual topic file")
        return result
    def spec(role,p):
        name=rel(p)
        raw=(root/name).read_bytes()
        require(0<len(raw)<100000,"small whole text input "+name)
        raw.decode()
        if name.endswith(".py"):
            ast.parse(raw)
        return dict(role=role,path=name,bytes=len(raw),sha256=sha256(raw).hexdigest(),
                    git_blob_sha=sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest(),encoding="utf-8")
    paths={k:TOPIC+"/scripts/"+n for k,n in SCRIPTS.items()}
    paths.update({k:TOPIC+"/notes/"+n for k,n in NOTES.items()})
    if a.fhc_receipt:
        paths["FHC"]=rel(a.fhc_receipt)
    if a.reviewed_rules:
        paths["operational_review"]=rel(a.reviewed_rules)
    paths.update({k+"_proof":TOPIC+"/results/R149-supplement-"+v+".md" for k,v in PROOFS.items()})
    paths.update(gg_actual=rel(a.gg_result_dir/"actual-scientific-conclusion.json"),
                 gg_execution=rel(a.gg_result_dir/"execution.json"))
    absent=[v for v in (paths["gg_actual"],paths["gg_execution"],paths["FHC"]) if not (root/v).is_file()]
    if absent:
        print(json.dumps(dict(ready=False,missing_whole_files=absent,manifest_created=False,old_science=0)))
        return
    def data(k):
        return json.loads((root/paths[k]).read_bytes())
    if not (data("gg_actual")["complete"] and data("gg_actual")["proved"] and data("gg_execution")["scientific_complete"]):
        print(json.dumps(dict(ready=False,actual_GG_complete=data("gg_actual")["complete"],
             actual_GG_targets=data("gg_actual")["completed_targets"],manifest_created=False,old_science=0)))
        return
    anchor={x["role"]:x for x in data("D_manifest")["files"]}
    for k,role in ANCHOR_ROLES.items():
        paths[k]=anchor[role]["path"]
    files={k:spec(k,p) for k,p in paths.items()}
    for k,role in ANCHOR_ROLES.items():
        require(all(files[k][p]==anchor[role][p] for p in ("path","bytes","sha256","git_blob_sha")),
                "entire actual GTP factor "+k)
    gg,wss=data("gg_manifest"),data("wss_manifest")
    all_current={}
    for row in list(files.values())+gg["files"]+wss["files"]:
        path=row["path"]
        item=spec(row["role"],path)
        require(all(item[k]==row[k] for k in ("path","bytes","sha256","git_blob_sha")),
                "immutable actual original at "+path)
        require(path not in all_current or all_current[path]["sha256"]==row["sha256"],"one same whole input per path")
        all_current[path]=item
    owner=load(root/paths["science"],"_selected_response_metadata_only")
    draft=dict(kind=KIND,repository="Rogerhu12/math-research-public",problem_id="actual_selected_physical_response_"+
               files["gg_actual"]["sha256"][:16],files=list(files.values()),whole_distinct_current_files=len(all_current),
               original_GG_history=21,original_WSS_TC_current=184,original_WSS_TC_history=32,
               reviewed_rules=files["operational_review"],target_order=owner.TARGETS,parameters=owner.PARAMETERS,
               runtime=owner.RUNTIME)
    draft["operation"]=dict(output_base=TOPIC+"/notes/selected_physical_response_ci",
         consumed_marker=TOPIC+"/notes/selected_physical_response_ci/"+draft["problem_id"]+"-consumed.json",
         reserve_bytes=120000,topic_maximum_bytes=200000000,maximum_total_publication_bytes=198000,
         child_timeout_seconds=20100,automatic_scientific_retry=False)
    owner.metadata(root,draft)
    raw=(json.dumps(draft,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
    require(len(raw)<100000,"one whole compact manifest with transitive manifests")
    mp,wp=(root/a.manifest_out).resolve(),(root/a.workflow_out).resolve()
    mrel=rel(mp)
    wrel=wp.relative_to(root).as_posix()
    require(mrel.startswith(TOPIC+"/notes/") and wrel.startswith(".github/workflows/")
            and not mp.exists() and not wp.exists(),"one new first entry")
    # The original public raw-only bootstrap reads its parent and grandparent before materialization.
    source=(root/".github/workflows/fourfold-codazzi-whole-selected-signed-sources-public.yml").read_text()
    start=source.index("          sparse-checkout: |\n")+len("          sparse-checkout: |\n")
    original_sparse=[]
    for line in source[start:].splitlines():
        if not line.startswith("            /"):
            break
        original_sparse.append(line.strip().lstrip("/"))
    require("README.md" in original_sparse and len(original_sparse)>20,"complete original raw bootstrap checkout")
    sparse=sorted(set(original_sparse)|set(all_current)|{mrel,"README.md",TOPIC+"/README.md"})
    workflow="""name: Full selected physical response and ordinary negative readout
on:
  push:
    branches: [main]
    paths: [__WORKFLOW__]
permissions:
  contents: write
  actions: read
concurrency:
  group: __PROBLEM__
  cancel-in-progress: false
jobs:
  receive:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-latest
    timeout-minutes: 350
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
          filter: blob:none
          persist-credentials: false
          sparse-checkout-cone-mode: false
          sparse-checkout: |
__SPARSE__
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Prepare the original WSS image and native restoration packages
        run: |
          docker build --tag r149-original-wss:job - <<'DOCKERFILE'
          FROM python@sha256:4d1caded1f729ae443eb803f26ffde7b61e696aeaef62f099abb6dd6b14257c7
          RUN apt-get update -qq && apt-get install -y --no-install-recommends git ca-certificates
          RUN python -m pip install --disable-pip-version-check --only-binary=:all: numpy==2.3.5 python-flint==0.9.0 scipy==1.17.0 sympy==1.14.0 mpmath==1.3.0
          DOCKERFILE
      - name: Install the fixed directed arithmetic and chart proposal runtime
        run: >-
          python -m pip install --only-binary=:all: python-flint==0.9.0 numpy==2.3.5
      - name: Restore the two actual source objects and solve the full physical positive system
        env:
          GITHUB_TOKEN: __TOKEN__
          OPENBLAS_NUM_THREADS: '1'
          OMP_NUM_THREADS: '1'
          MKL_NUM_THREADS: '1'
          PYTHONUNBUFFERED: '1'
        run: python __WORKER__ --repo "$GITHUB_WORKSPACE" --manifest __MANIFEST__ --manifest-sha __SHA__
"""
    for k,v in dict(WORKFLOW=wrel,PROBLEM=draft["problem_id"],SPARSE="\n".join("            /"+p for p in sparse),
        TOKEN="\x24{{ secrets.GITHUB_TOKEN }}",WORKER=paths["worker"],MANIFEST=mrel,SHA=sha256(raw).hexdigest()).items():
        workflow=workflow.replace("__"+k+"__",v)
    mp.parent.mkdir(parents=True,exist_ok=True)
    wp.parent.mkdir(parents=True,exist_ok=True)
    mp.write_bytes(raw)
    wp.write_text(workflow)
    print(json.dumps(dict(ready=True,whole_current=len(all_current),manifest_bytes=len(raw),
        manifest_sha256=sha256(raw).hexdigest(),actual_GG=files["gg_actual"]["sha256"],
        actual_WSS=files["wss_actual"]["sha256"],workflow_sha256=sha256(workflow.encode()).hexdigest(),old_science=0)))


if __name__=="__main__":
    main()
