"""Metadata-only terminal admission and exact missing-cell fleet generation.

An active original run produces readiness=false and no assignments, new
manifest or workflow. Only its genuine whole terminal record can determine
the complement. A previous complete terminal fleet union may be carried
verbatim, including every successfully preserved prefix of failed jobs.
"""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util, json, sys
from pathlib import Path

TOPIC="topics/visible-flex-exact-nearby"
BASE=TOPIC+"/scripts/fourfold_codazzi_true_root_missing_cell_fleet"
GENERATOR=TOPIC+"/scripts/make_true_root_missing_cell_fleet_manifest.py"
PROOF=TOPIC+"/results/R149-supplement-terminal-missing-cell-fleet-and-complete-source-aggregation.md"
ENTRY=TOPIC+"/notes/2026-11-28-TCF-terminal-missing-cell-fleet-entry.md"
ORIGINAL_DIRECTORY=TOPIC+"/notes/true_root_trial_residual_ci/run-46117170011-1"
ORIGINAL_WORKERS=[TOPIC+"/scripts/fourfold_codazzi_true_root_trial_public_worker.py",
    TOPIC+"/scripts/fourfold_codazzi_true_root_parallel_trial_public_worker.py",
    TOPIC+"/scripts/fourfold_codazzi_true_root_parallel_vector_public_worker.py"]


def require(ok,message):
    if not ok:raise ValueError(message)


def sha(raw):return hashlib.sha256(raw).hexdigest()


def encode(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()


def load(root,path,name):
    source=(root/path).read_bytes();compile(ast.parse(source),path,"exec")
    spec=importlib.util.spec_from_file_location(name,root/path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


def workflow(manifest_path,manifest_sha,workflow_path,manifest):
    sparse=sorted({"README.md",TOPIC+"/README.md",manifest_path,
        *ORIGINAL_WORKERS,manifest["terminal_parent_objects"]["manifest"]["path"],
        *(item["path"] for item in manifest["files"])})
    checkout="\n".join("            /"+path for path in sparse)
    installation="""      - name: Install Git in the original immutable runtime
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
""".replace("@SPARSE@",checkout)
    runtime="""    runs-on: ubuntu-24.04
    container: python@sha256:4d1caded1f729ae443eb803f26ffde7b61e696aeaef62f099abb6dd6b14257c7
    env:
      OPENBLAS_CORETYPE: Haswell
      OPENBLAS_NUM_THREADS: '1'
      OMP_NUM_THREADS: '1'
      MKL_NUM_THREADS: '1'
      BLIS_NUM_THREADS: '1'
      VECLIB_MAXIMUM_THREADS: '1'
      NUMEXPR_NUM_THREADS: '1'
"""
    source="""name: R149 terminal-admitted original TC missing cells @SHORT@
on:
  push:
    branches: [main]
    paths:
      - '@WORKFLOW@'
  workflow_dispatch:
permissions:
  contents: write
  actions: read
concurrency:
  group: visible-flex-exact-TCF-@IDENTITY@
  cancel-in-progress: false
jobs:
  original-missing-cells:
    name: TCF original cells ${{ matrix.ordinal }}
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    strategy:
      fail-fast: false
      max-parallel: @PARALLEL@
      matrix:
        ordinal: @ORDINALS@
@RUNTIME@    timeout-minutes: 350
    steps:
@INSTALL@      - name: Install the unchanged complete native reconstruction and directed cell runtime
        run: python -m pip install --disable-pip-version-check numpy==2.3.5 python-flint==0.9.0 scipy==1.17.0 sympy==1.14.0 mpmath==1.3.0
      - name: One disjoint original-cell interval with every96 column and all source windows
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: >-
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_true_root_missing_cell_fleet_public_worker.py
          --repo "$GITHUB_WORKSPACE"
          --manifest @MANIFEST@
          --manifest-sha @SHA@
          --ordinal ${{ matrix.ordinal }}
  merge-whole-terminal-union:
    name: TCF complete terminal union
    needs: original-missing-cells
    if: always() && github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
@RUNTIME@    timeout-minutes: 35
    steps:
@INSTALL@      - name: Install only the final directed scalar arithmetic
        run: python -m pip install --disable-pip-version-check python-flint==0.9.0
      - name: Preserve every accepted original cell and finish only complete missing norms
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: >-
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_true_root_missing_cell_fleet_merge_public_worker.py
          --repo "$GITHUB_WORKSPACE"
          --manifest @MANIFEST@
          --manifest-sha @SHA@
"""
    replacements={"@SHORT@":manifest["fleet_identity_sha256"][:12],"@WORKFLOW@":workflow_path,
        "@IDENTITY@":manifest["parent_identity_sha256"],"@PARALLEL@":str(manifest["maximum_parallel_public_jobs"]),
        "@ORDINALS@":json.dumps(list(range(len(manifest["assignments"])))),"@RUNTIME@":runtime,
        "@INSTALL@":installation,"@MANIFEST@":manifest_path,"@SHA@":manifest_sha}
    for key,value in replacements.items():source=source.replace(key,value)
    require("@" not in source.replace("python@sha256:","").replace("actions/checkout@v4","")
        and len(source.encode())<100000,"the entire concrete workflow has no unresolved placeholders")
    return source.encode()


def build(root,*,maximum_cells=256,maximum_parallel=6,carry_directory=None,carry_manifest=None):
    root=Path(root);sys.dont_write_bytecode=True
    require(not any(name in sys.modules for name in ("numpy","flint","scipy")),"metadata-only TC continuation generator")
    helper=load(root,BASE+".py","_TCF_generator_metadata")
    owner=load(root,BASE+"_owner.py","_TCF_generator_owner")
    worker=load(root,BASE+"_public_worker.py","_TCF_generator_transport")
    merger=load(root,BASE+"_merge_public_worker.py","_TCF_generator_merge_transport")
    code,cell_receipt=helper.original_cell_factory(root);worker.original_input_prefix(root)
    require(type(maximum_parallel) is int and 1<=maximum_parallel<=20,"a declared public-job concurrency limit")
    require(type(maximum_cells) is int and 1<=maximum_cells<=512,"a bounded complete-cell scheduling interval")
    for path in (PROOF,ENTRY):require((root/path).is_file(),"the whole new proof and entry contract")
    status,original=helper.inspect_parent(root,ORIGINAL_DIRECTORY)
    readiness={"kind":"TCF_original_terminal_parent_readiness_v1",**status,
        "complete_new_source_AST_compiled":True,"whole_original_cell_adapter":cell_receipt,
        "whole_original_public_restoration_prefix_compiled":True,"scientific_calls":0,
        "numerical_modules_loaded":[],"new_workflow_launched":False}
    if not status["ready"]:return readiness,None,None,None,None
    require(bool(carry_directory)==bool(carry_manifest),"a previous union requires both its entire manifest and actual directory")
    carry=None
    if carry_directory:
        carry={key:helper.descriptor(root,path) for key,path in {
            "manifest":carry_manifest,"union":carry_directory+"/actual-accepted-union.json",
            "execution":carry_directory+"/execution.json"}.items()}
    parent=helper.apply_carry(root,original,carry)
    assignments=helper.partition_missing(parent,maximum_cells)
    require(assignments,"at least one genuinely missing original cell")
    files=[]
    for role,path in (("helper",BASE+".py"),("science",BASE+"_owner.py"),("worker",BASE+"_public_worker.py"),
        ("merge_worker",BASE+"_merge_public_worker.py"),("generator",GENERATOR),("proof",PROOF),("entry",ENTRY)):
        files.append({"role":role,**helper.descriptor(root,path)})
    case_path=TOPIC+"/scripts/fourfold_codazzi_tcf_whole_terminal_rule16.py"
    case=load(root,case_path,"_TCF_terminal_rule16_evidence")
    require(sha((root/case_path).read_bytes())=="f9d35b5558427d75ea18ac1585489971cfced93ca134311b563f637a9cbc0522","the entire exact hard-stop evidence reader")
    files.append({"role":"TC_hard_stop_reader",**helper.descriptor(root,case_path)})
    for role,spec in case.INPUTS.items():
        case.read(root,spec)
        files.append({"role":role,**helper.descriptor(root,spec[0])})
    for key,spec in original["specs"].items():files.append({"role":"original_terminal_"+key,**spec})
    require(len({item["path"] for item in files})==len(files),"one whole descriptor per current metadata object")
    identity=sha(encode({"parent":parent["parent_identity"],"assignments":assignments,
        "whole_new_sources":files,"parameters":owner.PARAMETERS,"runtime":owner.RUNTIME,
        "maximum_parallel_public_jobs":maximum_parallel}))
    base=TOPIC+"/notes/true_root_missing_cell_fleet_ci"
    operation={"topic_maximum_bytes":200000000,"reserve_bytes":120000,
        "maximum_total_publication_bytes":85000,"maximum_merge_publication_bytes":360000,
        "maximum_execution_bytes":20000,"maximum_fleet_publication_bytes":len(assignments)*85000+390000,
        "readme_pull_interval_seconds":1800,"automatic_scientific_retry":False,"child_timeout_seconds":17400,
        "parent_marker":base+"/exclusive-parent-"+parent["parent_identity"]+".json",
        "assignment_marker_base":base+"/consumed-"+identity,
        "merge_marker":base+"/consumed-merge-"+identity+".json","output_base":base}
    manifest={"repository":"Rogerhu12/math-research-public","kind":owner.MANIFEST_KIND,
        "problem_id":"original_TC_whole_missing_cells_"+identity[:20],"fleet_identity_sha256":identity,
        "parent_identity_sha256":parent["parent_identity"],"terminal_parent_directory":ORIGINAL_DIRECTORY,
        "terminal_parent_objects":original["specs"],"carry_union":carry,
        "parameters":owner.PARAMETERS,"runtime":owner.RUNTIME,"files":files,"operation":operation,
        "maximum_cells_per_public_job":maximum_cells,"maximum_parallel_public_jobs":maximum_parallel,
        "assignments":assignments,"accepted_cells_copied_without_evaluation":parent["accepted_cells"],
        "remaining_original_cells":7724-parent["accepted_cells"],"accepted_intervals":parent["accepted_intervals"],
        "whole_original_mathematical_targets":original["owner"].TARGETS,
        "already_complete_original_targets_copied_verbatim":original["owner"].TARGETS[:len(original["completed_natural_keys"])],
        "input_tree_recipe":{"original_manifest_sha256":helper.PARENT_MANIFEST_SHA,
            "all_original_current_files":len(original["documents"]["manifest"]["files"]),
            "all_original_historical_inputs":len(original["documents"]["manifest"]["historical_inputs"]),
            "whole_original_native_parts":40,"same_original_direction_native_recipe":True,
            "same_four_whole_trial_arrays_reconstructed_only_as_inputs":True,
            "no_old_matrix_norm_or_accepted_cell_target_called":True,
            "previous_union_graph":"whole immutable metadata edges, never duplicate science",
            "whole_public_capacity_accounting_includes_all_jobs_and_merge":True},
        "scope":{"original_full7724_domain_required_for_any_new_complete_source_norm":True,
            "each_assigned_cell_contains_all96_columns_and_original_windows":True,
            "one_arithmetic_process_per_public_runner":True,"same_cell_readonly_identity_Legendre_memo":True,
            "old_completed_original_norms_copied_verbatim":True,
            "partial_fleet_union_retained_for_strict_complement_continuation":True,
            "original_operator_trial_boundary_conditions_or_trial_jumps_changed":False,
            "true_PDE_columns_or_inverse_proved":False}}
    helper.resolve_parent(root,manifest)
    parent_short=parent["parent_identity"][:16]
    manifest_path=TOPIC+"/notes/2026-11-28-true-root-missing-cell-fleet-"+parent_short+"-inputs.json"
    workflow_path=".github/workflows/visible-exact-true-root-missing-cell-fleet-"+parent_short+".yml"
    raw=encode(manifest);require(0<len(raw)<100000,"one complete small metadata DAG manifest")
    # A positive unsigned 64-bit Actions id occupies at most 20 decimal bytes.
    longest_run=str(2**64-1)
    directory=base+"/run-"+longest_run+"-1/"
    markers=[worker.parent_marker(manifest,sha(raw)),
        merger.merge_marker(manifest,sha(raw),longest_run,directory+"aggregate")]
    markers.extend(worker.assignment_marker(manifest,sha(raw),i,longest_run,
        directory+"assignment-%03d"%i) for i in range(len(assignments)))
    marker_bytes=sum(len(worker.encode(item)) for item in markers)
    require(marker_bytes<=30000,"all complete common and consumed markers fit the reserved 30000 bytes")
    readiness["complete_marker_publication_byte_upper_bound"]=marker_bytes
    action=workflow(manifest_path,sha(raw),workflow_path,manifest)
    readiness.update(ready=True,parent_identity_sha256=parent["parent_identity"],
        accepted_complete_cells=parent["accepted_cells"],remaining_cells=7724-parent["accepted_cells"],
        complete_disjoint_assignments=len(assignments),maximum_parallel_public_jobs=maximum_parallel,
        manifest_path=manifest_path,manifest_bytes=len(raw),manifest_sha256=sha(raw),workflow_path=workflow_path,
        workflow_bytes=len(action),workflow_sha256=sha(action),previous_terminal_union_carried=carry is not None)
    require(not any(name in sys.modules for name in ("numpy","flint","scipy")),"no numerical producer imported or executed")
    return readiness,manifest_path,raw,workflow_path,action


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,default=Path(__file__).resolve().parents[3])
    parser.add_argument("--maximum-cells",type=int,default=256);parser.add_argument("--maximum-parallel",type=int,default=6)
    parser.add_argument("--carry-directory");parser.add_argument("--carry-manifest");parser.add_argument("--write",action="store_true")
    args=parser.parse_args()
    status,mpath,raw,wpath,action=build(args.repo.resolve(),maximum_cells=args.maximum_cells,
        maximum_parallel=args.maximum_parallel,carry_directory=args.carry_directory,carry_manifest=args.carry_manifest)
    if status["ready"] and args.write:
        worker=load(args.repo.resolve(),BASE+"_public_worker.py","_TCF_generator_terminal_check")
        status["terminal_original_run_API"]=worker.terminal_actions_parent(status["parent_run"].split("/")[0])
        if args.carry_directory:
            prior=json.loads((args.repo/args.carry_directory/"actual-accepted-union.json").read_bytes())
            status["terminal_previous_fleet_API"]=worker.terminal_actions_parent(prior["run_id"])
        for name,data in ((mpath,raw),(wpath,action)):
            path=args.repo/name;path.parent.mkdir(parents=True,exist_ok=True)
            require(not path.exists() or path.read_bytes()==data,"an earlier concrete fleet entry is immutable")
            path.write_bytes(data);require(path.read_bytes()==data,"whole generated entry readback")
        status["wrote_complete_manifest_and_workflow"]=True
    else:status["wrote_complete_manifest_and_workflow"]=False
    print(encode(status).decode(),end="")


if __name__=="__main__":main()
