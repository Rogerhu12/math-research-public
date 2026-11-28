"""Prepare the conditional first MSS entry only after an actual terminal GDC failed inverse."""
import argparse
import ast
from hashlib import sha256
import importlib.util
import json
from pathlib import Path

from make_true_low193_direct_flow_manifest import TOPIC,WORKER_PATH,encode,identity,literals

BASE=TOPIC+"/notes/2026-11-28-signed-grassmann-defect-inputs.json"
BASE_ID=(77720,"7b1a72bf49a24db39804cae5f2cde5612db2c302566d89b6034f2648f36303b0")
MSS=TOPIC+"/scripts/fourfold_codazzi_multiple_shooting_"
OWNER=MSS+"owner.py"
MANIFEST=TOPIC+"/notes/2026-11-28-full-physical-multiple-shooting-inputs.json"
WORKFLOW=".github/workflows/fourfold-codazzi-full-physical-multiple-shooting-public.yml"
ORIGINAL=TOPIC+"/notes/signed_grassmann_defect_ci/run-46144819361-1/"
ADDITIONS={"physical_multiple_shooting_owner":OWNER,"MSS_envelopes":MSS+"envelopes.py","MSS_model":MSS+"physical_math.py",
    "MSS_restore":MSS+"after_chronological.py","MSS_validator":MSS+"validate.py","MSS_signed":MSS+"signed_response.py",
    "MSS_generator":TOPIC+"/scripts/make_physical_multiple_shooting_manifest.py",
    "MSS_proof":TOPIC+"/results/R149-supplement-full-physical-multiple-shooting-with-dyadic-signed-propagators.md"}


def require(ok,msg):
    if not ok:
        raise ValueError(msg)


def no_entry(reason):
    print(json.dumps(dict(ready=False,reason=reason,actual_mathematical_targets_evaluated=0,
                          manifest_or_workflow_written=False)))


def load(root,spec):
    p=root/spec["path"]
    require(identity(spec["role"],spec["path"],p.read_bytes())==spec,"whole qualified module")
    info=importlib.util.spec_from_file_location("_MSS_"+spec["role"],p)
    mod=importlib.util.module_from_spec(info)
    info.loader.exec_module(mod)
    return mod


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",required=True)
    parser.add_argument("--workflow-output",help="review location for the pending first public workflow")
    args=parser.parse_args()
    root=Path(args.repo).resolve()
    base=(root/BASE).read_bytes()
    require((len(base),sha256(base).hexdigest())==BASE_ID,"actual complete parent GDC input manifest")
    m=json.loads(base)
    files=m["files"]
    require(len(files)==109 and len(m["historical_inputs"])==21,"all original 109 current and 21 native inputs")
    for s in files:
        require(s==identity(s["role"],s["path"],(root/s["path"]).read_bytes()),"whole current source "+s["path"])
    added=[]
    for k,p in ADDITIONS.items():
        b=(root/p).read_bytes()
        if p.endswith(".py"): ast.parse(b,filename=p)
        added.append(identity(k,p,b))
    old={s["role"]:s for s in files}
    if not all((root/(ORIGINAL+p)).is_file() for p in ("actual-scientific-conclusion.json","execution.json")):
        return no_entry("the fixed actual terminal GDC whole result and execution have not both been published")
    triples=[identity(k,p,(root/p).read_bytes()) for k,p in (
        ("MSS_failed_GDC_actual",ORIGINAL+"actual-scientific-conclusion.json"),
        ("MSS_failed_GDC_execution",ORIGINAL+"execution.json"),("MSS_failed_GDC_manifest",BASE))]
    a,e=(json.loads((root/s["path"]).read_bytes()) for s in triples[:2])
    if not (e.get("finished_utc") and e.get("scientific_finished_utc")):
        return no_entry("the physical GDC scientific child has not reached an actual terminal outcome")
    if e.get("scientific_complete") or a.get("certificate",{}).get("actual_low_hybrid_inverse_proved"):
        return no_entry("the original actual low193 BVP is already solved, retain its paid result")
    files.extend(added+triples)
    specs={s["role"]:s for s in files}
    require(len(files)==len(specs)==len({s["path"] for s in files}),"independent whole input paths and roles")
    pure=load(root,specs["MSS_restore"])
    pure.admit(*[(root/s["path"]).read_bytes() for s in triples],triples,
        load(root,old["GDC_validator"]),load(root,old["grassmann_validator"]),load(root,old["GDC_failed_restore"]))
    decl=literals((root/OWNER).read_bytes(),
        ("KIND","ENTRY_ROLE","EXPLICIT","SCI_FIELDS","RUNTIME","GATE_SUFFIX","CERTIFICATE_PARAMETERS","TARGETS"))
    m["expected_current_input_count"]=len(files)
    op=m["operation"]
    op.update(scientific_entry_role=decl["ENTRY_ROLE"],scientific_kind=decl["KIND"],
        scientific_module_binding=m["scientific_modules"]+[specs[k] for k in decl["EXPLICIT"]],
        ordered_targets=decl["TARGETS"],complete_target_counts=[3],scientific_field_names=decl["SCI_FIELDS"],
        fixed_runtime=decl["RUNTIME"],complete_gate_names=op["complete_gate_names"][:18]+decl["GATE_SUFFIX"],
        certificate_parameters=decl["CERTIFICATE_PARAMETERS"],output_base=TOPIC+"/notes/full_physical_MSS_ci",
        consumed_marker=TOPIC+"/notes/full_physical_MSS_ci/R149_MSS_v1-consumed.json")
    op["retained_scope"].update(independent_full_physical_MSS_after_actual_failed_GDC=True,
        required_old_GDC_whole_packets_only=True,entire_193_times_1425_model_and_both_original_endpoints=True)
    m["directed_certificate_contract"]=dict(proof=specs["MSS_proof"],original_terminal_GDC=triples,
        method="global dyadic two-sided block maximal norm, directed angular induced-2 blocks",
        targets=decl["TARGETS"],producer_called_by_generator=False)
    raw=encode(m)
    require(len(raw)<100000,"whole first-run manifest budget")
    paths=sorted({"README.md",TOPIC+"/README.md",MANIFEST,m["reviewed_rules"]["path"],*[s["path"] for s in files]})
    digest=sha256(raw).hexdigest()
    w="""name: R149 full physical low193 multiple shooting
on:
  push:
    branches: [main]
    paths: [WORKFLOW_PATH]
permissions:
  contents: write
concurrency:
  group: r149-full-physical-MSS
  cancel-in-progress: false
jobs:
  certify:
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
SPARSE
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install original directed runtime
        run: >-
          python -m pip install --only-binary=:all: python-flint==0.9.0 numpy==2.3.5
      - name: Check all physical shooting rows, the full inverse, and all four sources
        env:
          GITHUB_TOKEN: TOKEN_EXPR
          OMP_NUM_THREADS: '1'
          OPENBLAS_NUM_THREADS: '1'
          MKL_NUM_THREADS: '1'
          PYTHONUNBUFFERED: '1'
          PYTHONDONTWRITEBYTECODE: '1'
        run: python WORKER --repo "$GITHUB_WORKSPACE" --manifest MANIFEST_PATH --manifest-sha MANIFEST_SHA
"""
    w=w.replace("TOKEN_EXPR",chr(36)+"{{ secrets.GITHUB_TOKEN }}").replace("WORKFLOW_PATH",WORKFLOW).replace(
        "SPARSE","\n".join("            /"+p for p in paths)).replace("WORKER",WORKER_PATH).replace(
        "MANIFEST_PATH",MANIFEST).replace("MANIFEST_SHA",digest)
    for p,b in ((root/MANIFEST,raw),(Path(args.workflow_output) if args.workflow_output else root/WORKFLOW,w.encode())):
        require(not p.exists() or p.read_bytes()==b,"immutable first-run target "+str(p))
        p.parent.mkdir(parents=True,exist_ok=True)
        p.write_bytes(b)
    print(json.dumps(dict(ready=True,bytes=len(raw),sha256=digest,current=len(files),historical=len(m["historical_inputs"]),
        actual_mathematical_targets_evaluated=0,source_scope=decl["TARGETS"])))


if __name__=="__main__":
    main()
