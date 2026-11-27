"""Metadata-only first complete physical mean-height kernel entry."""
from __future__ import annotations
import argparse,ast,hashlib,importlib.util,json,subprocess,sys
from pathlib import Path

TOPIC="topics/visible-flex-exact-nearby"
OWNER=TOPIC+"/scripts/fourfold_codazzi_world_mean_height_owner.py"
WORKER=TOPIC+"/scripts/fourfold_codazzi_world_mean_height_public_worker.py"
MANIFEST=TOPIC+"/notes/2026-11-27-world-mean-height-inputs.json"
WORKFLOW=".github/workflows/visible-exact-world-mean-height.yml"


def require(ok,message):
    if not ok:
        raise ValueError(message)


def load(root,path,name):
    raw=(root/path).read_bytes()
    require(0<len(raw)<100000,"small whole source")
    ast.parse(raw.decode(),filename=path)
    spec=importlib.util.spec_from_file_location(name,root/path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


def workflow(files,manifest_sha):
    bootstrap=[TOPIC+"/scripts/fourfold_codazzi_negative_nu_waist_public_worker.py",
        TOPIC+"/scripts/fourfold_codazzi_support_localized_nu_public_worker.py",
        TOPIC+"/scripts/fourfold_codazzi_strict_nu_particular_public_worker.py",
        TOPIC+"/scripts/fourfold_codazzi_strict_nu_phase_public_worker.py",
        TOPIC+"/scripts/fourfold_codazzi_relative_nu_carrier_public_worker.py"]
    paths=sorted({"README.md",TOPIC+"/README.md",MANIFEST,*bootstrap,*[s["path"] for s in files]})
    lines=["name: R147 complete physical mean-height parameter kernel","on:","  push:",
        "    branches: [main]","    paths:","      - '"+WORKFLOW+"'",
        "  workflow_dispatch:","permissions:","  contents: write","concurrency:",
        "  group: visible-exact-world-mean-height-20261127","  cancel-in-progress: false",
        "jobs:","  first-complete-physical-mean-height:",
        "    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1",
        "    runs-on: ubuntu-24.04","    timeout-minutes: 350","    env:",
        "      OMP_NUM_THREADS: '1'","      OPENBLAS_NUM_THREADS: '1'","      MKL_NUM_THREADS: '1'",
        "      NUMEXPR_NUM_THREADS: '1'","      BLIS_NUM_THREADS: '1'","      VECLIB_MAXIMUM_THREADS: '1'",
        "    steps:","      - uses: actions/checkout@v4","        with:","          ref: main",
        "          fetch-depth: 0","          filter: blob:none","          persist-credentials: false",
        "          sparse-checkout-cone-mode: false","          sparse-checkout: |"]
    lines+=["            /"+path for path in paths]
    lines+=["      - uses: actions/setup-python@v5","        with:","          python-version: '3.12.14'",
        "      - name: Install the same original directed carrier runtime",
        "        run: python -m pip install --disable-pip-version-check numpy==2.3.5 python-flint==0.9.0",
        "      - name: Restore fixed whole carriers and pair the full physical height kernel",
        "        env:","          GITHUB_TOKEN: "+"$"+"{{ secrets.GITHUB_TOKEN }}",
        "        run: >-","          python "+WORKER,'          --repo "$GITHUB_WORKSPACE"',
        "          --manifest "+MANIFEST,"          --manifest-sha "+manifest_sha]
    return ("\n".join(lines)+"\n").encode()


def build(root,rhi_actual,rhi_execution,rhi_manifest):
    require(not any(x in sys.modules for x in ("numpy","flint","scipy")),"metadata-only generation")
    sys.dont_write_bytecode=True
    owner=load(root,OWNER,"_WMR_metadata_owner")
    worker=load(root,WORKER,"_WMR_metadata_worker")
    math=load(root,owner.MATH,"_WMR_pure_kernel_definitions")
    load(root,owner.RESTORE,"_WMR_necessary_carrier_restore_definitions")
    require(owner.SOURCE==OWNER and owner.WORKER==WORKER
        and math.TARGETS==owner.TARGETS and math.GRID==8192
        and math.MAXIMUM_KERNEL_DEGREE==2144,"complete concrete new contraction")
    compile(worker.build_adapter(root),WORKER,"exec")
    declared=owner.gather(root,rhi_actual,rhi_execution,rhi_manifest)
    files,history,roles=(declared[key] for key in ("files","historical_inputs","roles"))
    raws={s["path"]:(root/s["path"]).read_bytes() for s in files}
    paths={s["path"]:root/s["path"] for s in files}
    small=[s for s in history if s["role"].startswith("RHI_NP_RW_")]
    require(len(small)==4,"four whole necessary original reflected input definitions")
    for item in small:
        raw=subprocess.run(["git","show",item["commit"]+":"+item["path"]],
            cwd=root,check=True,capture_output=True).stdout
        require(len(raw)==item["bytes"] and owner.sha(raw)==item["sha256"],
            "whole necessary original input")
        raws[item["path"]]=raw
    admitted=owner.admit(declared,raws,paths)
    require(admitted["RHI"]["complete"] is admitted["NP"]["complete"] is admitted["SB"]["complete"] is True
        and history==[dict(s,role="RHI_"+s["role"]) for s in admitted["RHI_manifest"]["historical_inputs"]],
        "the full actual completed predecessor and unchanged original closure")
    review=owner.parse(raws[roles["reviewed_rules"]])
    require(review["repository"]==owner.REPO
        and review["new_unread_rules_must_still_be_reported_and_applied"] is True
        and set(review["readme_sha256"])=={"README.md",TOPIC+"/README.md"},
        "both reviewed README contracts")
    for path,digest in review["readme_sha256"].items():
        require(owner.sha((root/path).read_bytes())==digest,"already reviewed README unchanged: "+path)
    require(review["large_data_policy"]["maximum_topic_bytes"]==200000000
        and review["large_data_policy"]["original_completed_mathematics_must_not_be_recomputed"] is True
        and not any(x in sys.modules for x in ("numpy","flint","scipy")),"no local scientific target")
    manifest={
        "repository":owner.REPO,"kind":owner.MANIFEST_KIND,"scientific_kind":owner.KIND,"stage":owner.STAGE,
        "problem_id":"R147_complete_physical_mean_height_nu_kernel_20261127",
        "parameters":owner.PARAMETERS,"runtime":owner.RUNTIME,"target_order":owner.TARGETS,
        "complete_record_counts":[3],"allowed_scientific_fields":owner.SCI_FIELDS,
        "files":files,"expected_current_input_count":len(files),"historical_inputs":history,"roles":roles,
        "operation":{"topic_maximum_bytes":200000000,"reserve_bytes":120000,
            "readme_pull_interval_seconds":1800,"automatic_scientific_retry":False,
            "consumed_marker":TOPIC+"/notes/world_mean_height_ci/consumed-target.json",
            "output_base":TOPIC+"/notes/world_mean_height_ci","maximum_scientific_bytes":32000,
            "maximum_execution_bytes":75000,"maximum_total_publication_bytes":120000,
            "child_timeout_seconds":18600},
        "scope":{"same_original_implicit_selected_Q_delta":True,
            "all_four_original_NP_arrays_and_whole_RHI_profile_retained":True,
            "only_necessary_sameSHA_carrier_restoration":True,
            "full_physical_dotJ_coordinate_and_true_mean_terms":True,
            "all2144_kernel_modes_and_unaliased8192_quadrature":True,
            "true_PDE_error_uses_complete_RHI_and_ASB_receivers":True,
            "original_world_orientation_and_fixed_height_retained":True,
            "original_reference_body_signed_value_and_complete_anchor_error_coefficient":True,
            "actual_Qb_Fb_and_rigid_ports_independent":True,
            "old_RHI_NP_or_geometry_targets_recomputed":False,
            "new_trial_or_new_background_chosen":False,
            "full_world_height_Schur_or_topic_completion_proved":False}}
    raw=owner.canonical(manifest)
    require(len(raw)<100000,"whole small immutable input manifest")
    return raw,workflow(files,owner.sha(raw))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",default=".",type=Path)
    parser.add_argument("--rhi-manifest",default=TOPIC+"/notes/2026-11-27-relative-nu-carriers-inputs.json")
    parser.add_argument("--rhi-actual",default=TOPIC+"/notes/relative_nu_carriers_ci/run-45933988440-1/actual-relative-nu-carriers.json")
    parser.add_argument("--rhi-execution",default=TOPIC+"/notes/relative_nu_carriers_ci/run-45933988440-1/execution.json")
    parser.add_argument("--check-only",action="store_true")
    args=parser.parse_args();root=args.repo.resolve();sys.dont_write_bytecode=True
    raw,yaml=build(root,args.rhi_actual,args.rhi_execution,args.rhi_manifest)
    for relative,content in ((MANIFEST,raw),(WORKFLOW,yaml)):
        path=root/relative
        if args.check_only:
            require(path.read_bytes()==content,"exact complete current entry: "+relative)
        else:
            path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(content)
    print(json.dumps({"ready":True,"manifest":MANIFEST,"manifest_bytes":len(raw),
        "manifest_sha256":hashlib.sha256(raw).hexdigest(),"workflow":WORKFLOW,
        "local_scientific_targets_evaluated":0},sort_keys=True))


if __name__=="__main__":
    main()
