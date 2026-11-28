"""Metadata-only CFC entry; all SC/DCP/H96/PWA96 actual parents must finish.

Without every whole successful predecessor, only readiness is returned.
The generator never supplies zero stand-ins or starts any numerical target.
"""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util, json, sys, textwrap
from pathlib import Path
from types import SimpleNamespace

TOPIC="topics/visible-flex-exact-nearby"
OWNER=TOPIC+"/scripts/fourfold_codazzi_complete_finite_columns_owner.py"
WORKER=TOPIC+"/scripts/fourfold_codazzi_complete_finite_columns_public_worker.py"
GENERATOR=TOPIC+"/scripts/make_complete_finite_columns_manifest.py"
PROOF=TOPIC+"/results/R149-supplement-complete-normalized-TC-columns-and-finite-physical-interface.md"
MANIFEST=TOPIC+"/notes/2026-11-28-complete-finite-columns-inputs.json"
WORKFLOW=".github/workflows/visible-exact-complete-finite-columns.yml"
PARENTS={
    "SC":(TOPIC+"/notes/2026-11-27-actual-signed-finite-inputs.json","actual-signed-finite-state.json"),
    "DCP":(TOPIC+"/notes/2026-11-28-particular-density-Theta-inputs.json","actual-particular-density-Theta.json"),
    "H96":(TOPIC+"/notes/2026-11-28-finite-trial-height-complete-inputs.json","actual-finite-trial-height.json"),
    "PWA96":(TOPIC+"/notes/2026-11-28-PWA-height-phase-saved-inputs.json","actual-pwa-height-phase.json")}
TEMPLATE='''name: R149 original TC96 complete target columns and physical rows
on:
  push:
    branches: [main]
    paths:
      - '.github/workflows/visible-exact-complete-finite-columns.yml'
permissions:
  contents: write
concurrency:
  group: visible-flex-exact-CFC-original96-full-columns-20261128
  cancel-in-progress: false
jobs:
  first-complete-original96-full-target-columns:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-24.04
    container: python@sha256:4d1caded1f729ae443eb803f26ffde7b61e696aeaef62f099abb6dd6b14257c7
    timeout-minutes: 350
    env:
      OPENBLAS_CORETYPE: Haswell
      OPENBLAS_NUM_THREADS: '1'
      OMP_NUM_THREADS: '1'
      MKL_NUM_THREADS: '1'
      BLIS_NUM_THREADS: '1'
      VECLIB_MAXIMUM_THREADS: '1'
      NUMEXPR_NUM_THREADS: '1'
    steps:
      - name: Install Git in the original immutable runtime
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
      - name: Trust the explicitly mounted checkout
        run: git config --global --add safe.directory "$GITHUB_WORKSPACE"
      - name: Install the original complete directed arithmetic
        run: python -m pip install --disable-pip-version-check numpy==2.3.5 python-flint==0.9.0 scipy==1.17.0 sympy==1.14.0 mpmath==1.3.0
      - name: Whole original carriers and one complete all96 target group
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: >-
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_complete_finite_columns_public_worker.py
          --repo "$GITHUB_WORKSPACE"
          --manifest topics/visible-flex-exact-nearby/notes/2026-11-28-complete-finite-columns-inputs.json
          --manifest-sha @SHA@
'''


def require(ok,message):
    if not ok:raise ValueError(message)


def sha(raw):return hashlib.sha256(raw).hexdigest()


def encode(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()


def load(root,path,name):
    raw=(root/path).read_bytes();ast.parse(raw)
    spec=importlib.util.spec_from_file_location(name,root/path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


def descriptor(root,role,path):
    require(path.startswith(TOPIC+"/") and all(v not in ("", ".", "..") for v in path.split("/")),"one complete safe topic input")
    raw=(root/path).read_bytes();raw.decode()
    require(0<len(raw)<100000,"one whole small metadata input")
    return {"role":role,"path":path,"bytes":len(raw),"sha256":sha(raw),
        "git_blob_sha":hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()}


def check_source(root,spec):
    here=descriptor(root,spec["role"],spec["path"])
    require(all(here[k]==spec[k] for k in ("path","bytes","sha256","git_blob_sha")),
        "the entire original actual metadata source")
    return load(root,spec["path"],"_CFC_parent_definition_"+spec["sha256"][:12])


def public_group(root,tag,manifest_path,directory):
    pm=json.loads((root/manifest_path).read_bytes())
    by_role={x["role"]:x for x in pm["files"]}
    owner=check_source(root,by_role["science"])
    names={"manifest":manifest_path,"execution":directory+"/execution.json"}
    if tag=="SC":
        names.update(state=directory+"/"+owner.FILES["state"],columns=directory+"/"+owner.FILES["columns"],
            physical=directory+"/"+owner.FILES["physical_primitive96"],
            incoming=directory+"/"+owner.FILES["declared_incoming_cosine96"])
    else:names["actual"]=directory+"/"+PARENTS[tag][1]
    specs={key:descriptor(root,tag+"_"+key,path) for key,path in names.items()}
    docs={key:json.loads((root/spec["path"]).read_bytes()) for key,spec in specs.items()}
    execution=docs["execution"];actual=docs["state" if tag=="SC" else "actual"]
    require(actual["complete"] is execution["complete"] is True
        and actual["actual_returncode"]==execution["actual_child_returncode"]==0
        and actual["failure"] is execution["failure"] is None
        and execution["manifest_sha256"]==specs["manifest"]["sha256"]
        and actual["completed_targets"]==pm["target_order"]
        and execution["old_completed_targets_recomputed"]==0,
        "every target actually completed in the same original public job: "+tag)
    if tag=="SC":
        require(actual["parameters"]==owner.PARAMETERS==pm["parameters"]
            and actual["manifest_sha256"]==specs["manifest"]["sha256"]
            and actual["old_completed_targets_recomputed"]==0
            and len(actual["completed_targets"])==3,"all three original SC targets")
        for key,name in (("columns","columns"),("physical","physical_primitive96"),("incoming","declared_incoming_cosine96")):
            owner.validate_result(docs[key],name,specs["manifest"]["sha256"],actual["whole_input_identity"])
    else:
        worker=check_source(root,by_role["worker"])
        env={"require":require,"parse":json.loads,"manifest":pm,"by_role":by_role,"op":pm["operation"],
            "args":SimpleNamespace(manifest_sha=specs["manifest"]["sha256"]),
            "run":execution["run_id"],"attempt":execution["run_attempt"],
            "snapshots":{role:root/spec["path"] for role,spec in by_role.items()}}
        exec(compile(textwrap.dedent(worker.VALIDATOR),"<CFC entire original public validator>","exec"),env)
        require(env["validate_output"]((root/specs["actual"]["path"]).read_bytes())==actual
            and actual["proved"] is True and actual["saved_record_count"]==len(pm["target_order"]),
            "whole original output identity and all rows: "+tag)
    for key,spec in specs.items():
        if key not in ("manifest","execution"):
            require([x for x in execution["scientific_files"] if x["path"]==spec["path"]]==[
                {k:spec[k] for k in ("path","bytes","sha256")}],"whole successful execution file: "+tag+"/"+key)
    return specs,docs,owner


def build(root,directories,manifests=None):
    require(not any(name in sys.modules for name in ("numpy","flint","scipy")),"metadata-only CFC entry")
    sys.dont_write_bytecode=True
    owner=load(root,OWNER,"_CFC_metadata_owner");pure=load(root,owner.MATH,"_CFC_pure_definitions")
    carriers=load(root,owner.CARRIERS,"_CFC_carrier_definitions");worker=load(root,WORKER,"_CFC_worker_definitions")
    worker.original_input_prefix(root)
    original=carriers.load(root/carriers.SC_RESTORE,"_CFC_frozen_SC_restore_metadata")
    unused,receipt=carriers.original_waist_prefix(original,(root/carriers.SC_RESTORE).read_bytes())
    require(receipt["old_norm_or_signed_matrix_targets_called"]==0 and len(pure.TARGETS)==10,
            "new actual owner and both exact whole-source adapters compile")
    for path in (OWNER,owner.MATH,owner.CARRIERS,WORKER,GENERATOR):
        compile(ast.parse((root/path).read_bytes()),path,"exec")
    require((root/PROOF).is_file(),"the full new mathematical contract")
    missing=[name for name in PARENTS if not directories.get(name)]
    readiness={"kind":"CFC_complete_actual_parent_readiness_v1","ready":False,
        "complete_source_and_whole_prefix_AST_compiled":True,"old_scientific_target_calls":0,
        "complete_required_parent_groups":["SC3_with_full_root96","DCP18","H96_7","PWA96_7"],
        "missing_parent_locations":missing,"new_complete_targets":10}
    if missing:return readiness,None,None
    manifests=manifests or {}
    parents,documents,definitions={},{},{}
    for tag,(default,unused) in PARENTS.items():
        path=manifests.get(tag) or default
        if not (root/path).is_file():
            readiness["missing_parent_manifests"]=[path];return readiness,None,None
        specs,docs,definition=public_group(root,tag,path,directories[tag])
        parents[tag],documents[tag],definitions[tag]=specs,docs,definition
    sc,hi,pwa=documents["SC"],documents["H96"]["actual"],documents["PWA96"]["actual"]
    require(pwa["complete_original_TC_arrays"]==hi["necessary_original_trial_receipts"]["complete_original_arrays"]
        and pwa["selected_member_identity"]==hi["selected_member_identity"],"same full original columns in H96/PWA")
    pmanifest=documents["PWA96"]["manifest"]
    praw={item["path"]:(root/item["path"]).read_bytes() for item in pmanifest["files"]}
    definitions["PWA96"].admit(pmanifest,praw)
    files={}
    def add(role,path,expected=None):
        spec=descriptor(root,role,path)
        if expected:require(all(spec[k]==expected[k] for k in ("path","bytes","sha256","git_blob_sha")),"entire shared original descriptor")
        if path in files:require(all(files[path][k]==spec[k] for k in ("bytes","sha256","git_blob_sha")),"one entire shared file")
        else:files[path]=spec
    for role,path in (("science",OWNER),("math",owner.MATH),("carriers",owner.CARRIERS),
        ("worker",WORKER),("generator",GENERATOR),("proof",PROOF),("SC_worker",worker.SC_WORKER),
        ("reviewed_rules",TOPIC+"/notes/2026-11-20-reviewed-public-CI-rules.json")):
        add(role,path)
    for tag,specs in parents.items():
        for key,spec in specs.items():add(tag+"_"+key,spec["path"],spec)
    review=json.loads((root/(TOPIC+"/notes/2026-11-20-reviewed-public-CI-rules.json")).read_bytes())
    require(set(review["readme_sha256"])=={"README.md",TOPIC+"/README.md"}
        and review["new_unread_rules_must_still_be_reported_and_applied"] is True,"both reviewed README rules")
    for path,digest in review["readme_sha256"].items():require(sha((root/path).read_bytes())==digest,"current reviewed rules: "+path)
    identity=sha(encode({tag:parents[tag]["execution"]["sha256"] for tag in PARENTS}))
    manifest={"repository":owner.REPO,"kind":owner.MANIFEST_KIND,"scientific_kind":owner.KIND,
        "problem_id":"CFC_original_TC96_full_columns_"+identity[:20],"parameters":owner.PARAMETERS,
        "runtime":owner.RUNTIME,"target_order":pure.TARGETS,"allowed_scientific_fields":owner.SCI_FIELDS,
        "files":sorted(files.values(),key=lambda item:item["role"]),"parents":parents,
        "input_tree_recipe":{"original_SC_current_TC_native_and_direction_closure":"unchanged_original_SC_prefix",
            "DCP_H96_PWA_current_files":"entire_each_parent_actual_scientific_checkout",
            "historical_native_files":"entire_each_original_pinned_commit",
            "all_shared_whole_bytes_must_agree":True,"all_metadata_admission_before_numerical_import":True},
        "operation":{"topic_maximum_bytes":200000000,"reserve_bytes":120000,
            "maximum_total_publication_bytes":210000,"maximum_execution_bytes":99000,
            "readme_pull_interval_seconds":1800,"automatic_scientific_retry":False,
            "child_timeout_seconds":18600,"consumed_marker":TOPIC+"/notes/complete_finite_columns_ci/consumed-"+identity[:20]+".json",
            "output_base":TOPIC+"/notes/complete_finite_columns_ci"},
        "scope":{"all_original96_columns_one_complete_target_group":True,
            "all_original_physical_low_mean_and_high_feedback_retained":True,
            "complete_whole_target_tail_error_not_zero":True,"original_Theta_all96_rows_and_complete_source_order":True,
            "full_same_rho_PWA_and_independent_world_receivers_retained":True,
            "complete_PH_inverse_PKQ_PU_Pg_Pf_carriers_independent":True,
            "full_physical_square_or_Schur_inverse_proved":False,"topic_completion_proved":False}}
    raw=encode(manifest);require(len(raw)<100000,"one entire small concrete CFC manifest")
    sparse=sorted({"README.md",TOPIC+"/README.md",MANIFEST,*files})
    yaml=TEMPLATE.replace("@SHA@",sha(raw)).replace("@SPARSE@","\n".join("            /"+path for path in sparse)).encode()
    require(not any(name in sys.modules for name in ("numpy","flint","scipy")),"zero local numerical targets")
    readiness.update(ready=True,manifest_sha256=sha(raw),manifest_bytes=len(raw),missing_parent_locations=[],
        complete_parent_execution_identity=identity)
    return readiness,raw,yaml


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument("--repo",type=Path,default=Path("."))
    for key in PARENTS:
        parser.add_argument("--"+key.lower()+"-directory");parser.add_argument("--"+key.lower()+"-manifest")
    parser.add_argument("--check-only",action="store_true");args=parser.parse_args();root=args.repo.resolve()
    dirs={key:getattr(args,key.lower()+"_directory") for key in PARENTS}
    manifests={key:getattr(args,key.lower()+"_manifest") for key in PARENTS}
    readiness,raw,yaml=build(root,dirs,manifests)
    if readiness["ready"]:
        for path,body in ((MANIFEST,raw),(WORKFLOW,yaml)):
            if args.check_only:require((root/path).read_bytes()==body,"same whole CFC actual entry")
            else:(root/path).parent.mkdir(parents=True,exist_ok=True);(root/path).write_bytes(body)
    print(encode(readiness).decode(),end="")


if __name__=="__main__":main()
