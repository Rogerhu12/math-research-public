"""Metadata-only PWA96 entry; a whole successful H96 result is indispensable."""
from __future__ import annotations
import argparse, ast, importlib.util, json, sys
from pathlib import Path

TOPIC="topics/visible-flex-exact-nearby"
OWNER=TOPIC+"/scripts/fourfold_codazzi_pwa_height_phase_saved_owner.py"
WORKER=TOPIC+"/scripts/fourfold_codazzi_pwa_height_phase_saved_public_worker.py"
MANIFEST=TOPIC+"/notes/2026-11-28-PWA-height-phase-saved-inputs.json"
WORKFLOW=".github/workflows/visible-exact-PWA-height-phase-saved.yml"
CONTAINER="python@sha256:4d1caded1f729ae443eb803f26ffde7b61e696aeaef62f099abb6dd6b14257c7"
TEMPLATE='''name: R149 complete PWA height and common-ratio phase rows
on:
  push:
    branches: [main]
    paths:
      - '.github/workflows/visible-exact-PWA-height-phase-saved.yml'
permissions:
  contents: write
concurrency:
  group: visible-flex-exact-PWA-height-phase-saved-20261128
  cancel-in-progress: false
jobs:
  first-PWA-height-and-phase-saved-combinations:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-24.04
    container: @CONTAINER@
    timeout-minutes: 30
    env:
      OPENBLAS_NUM_THREADS: '1'
      OMP_NUM_THREADS: '1'
      MKL_NUM_THREADS: '1'
      NUMEXPR_NUM_THREADS: '1'
    steps:
      - name: Install Git in the original immutable Python container
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
@SPARSE_PATHS@
      - name: Trust the explicitly mounted checkout
        run: git config --global --add safe.directory "$GITHUB_WORKSPACE"
      - name: Install the declared small scalar arithmetic
        run: python -m pip install --disable-pip-version-check python-flint==0.9.0
      - name: Consume complete H96 P96 APHI objects exactly once
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: >-
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_pwa_height_phase_saved_public_worker.py
          --repo "$GITHUB_WORKSPACE"
          --manifest topics/visible-flex-exact-nearby/notes/2026-11-28-PWA-height-phase-saved-inputs.json
          --manifest-sha @MANIFEST_SHA@
'''


def require(ok,message):
    if not ok:
        raise ValueError(message)


def load(root,path,name):
    raw=(root/path).read_bytes();ast.parse(raw.decode(),filename=path)
    spec=importlib.util.spec_from_file_location(name,root/path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


def build(root,height_actual=None,height_execution=None):
    require(not any(x in sys.modules for x in ("numpy","flint","scipy")),"metadata-only entry")
    sys.dont_write_bytecode=True
    owner=load(root,OWNER,"_PWA96_metadata_owner")
    math=load(root,owner.MATH,"_PWA96_pure_definitions")
    worker=load(root,WORKER,"_PWA96_metadata_worker")
    require(math.TARGETS==owner.TARGETS and math.COUNTS==owner.COUNTS
        and math.SIGNED==owner.SIGNED and math.CENTRED==owner.CENTRED,"all whole target definitions agree")
    tree=worker.build_adapter(root);compile(tree,WORKER,"exec")
    require((root/owner.PROOF).is_file(),"the complete mathematical consumer proof")
    if height_actual is None or height_execution is None:
        return {"ready":False,"reason":"whole_successful_H96_actual_and_execution_required",
            "complete_source_and_worker_AST_compiled":True,"local_scientific_targets":0},None,None
    declared=owner.gather(root,height_actual,height_execution)
    raws={x["path"]:(root/x["path"]).read_bytes() for x in declared["files"]}
    admitted=owner.admit(declared,raws)
    review=owner.parse(raws[declared["roles"]["reviewed_rules"]])
    require(set(review["readme_sha256"])=={"README.md",TOPIC+"/README.md"}
        and review["new_unread_rules_must_still_be_reported_and_applied"] is True,
        "both complete reviewed rule files")
    for path,digest in review["readme_sha256"].items():
        require(owner.sha((root/path).read_bytes())==digest,"reviewed README remains identical: "+path)
    manifest={"repository":owner.REPO,"kind":owner.MANIFEST_KIND,"scientific_kind":owner.KIND,
        "stage":owner.STAGE,"problem_id":"R149_complete_PWA_height_phase_saved_20261128",
        "parameters":owner.PARAMETERS,"runtime":owner.RUNTIME,"target_order":owner.TARGETS,
        "complete_record_counts":[7],"allowed_scientific_fields":owner.SCI_FIELDS,
        **declared,"expected_current_input_count":len(declared["files"]),
        "operation":{"topic_maximum_bytes":200000000,"reserve_bytes":120000,
            "readme_pull_interval_seconds":1800,"automatic_scientific_retry":False,
            "consumed_marker":TOPIC+"/notes/PWA_height_phase_saved_ci/consumed-target.json",
            "output_base":TOPIC+"/notes/PWA_height_phase_saved_ci",
            "maximum_scientific_bytes":99000,"maximum_execution_bytes":35000,
            "maximum_total_publication_bytes":138000,"child_timeout_seconds":600},
        "scope":{key:True for key in owner.TRUE_FLAGS}|{key:False for key in owner.FALSE_FLAGS}}
    raw=owner.encode(manifest);require(len(raw)<100000,"one whole small immutable manifest")
    sparse=sorted({"README.md",TOPIC+"/README.md",MANIFEST,*(x["path"] for x in declared["files"])})
    yaml=TEMPLATE.replace("@CONTAINER@",CONTAINER).replace("@MANIFEST_SHA@",owner.sha(raw))
    yaml=yaml.replace("@SPARSE_PATHS@","\n".join("            /"+x for x in sparse)).encode()
    require(not any(x in sys.modules for x in ("numpy","flint","scipy")),"no scientific target prepared locally")
    receipt={"ready":True,"whole_H96_run":admitted["H96"]["identity"]["run_id"],
        "complete_source_and_worker_AST_compiled":True,"whole_input_files":len(declared["files"]),
        "manifest_sha256":owner.sha(raw),"manifest_bytes":len(raw),"local_scientific_targets":0}
    return receipt,raw,yaml


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,default=Path("."))
    parser.add_argument("--height-actual");parser.add_argument("--height-execution")
    parser.add_argument("--check-only",action="store_true");args=parser.parse_args()
    root=args.repo.resolve();receipt,raw,yaml=build(root,args.height_actual,args.height_execution)
    if raw is not None:
        for path,content in ((MANIFEST,raw),(WORKFLOW,yaml)):
            if args.check_only:
                require((root/path).read_bytes()==content,"same whole prepared entry: "+path)
            else:
                (root/path).parent.mkdir(parents=True,exist_ok=True);(root/path).write_bytes(content)
    print(json.dumps(receipt,sort_keys=True))


if __name__=="__main__":
    main()
