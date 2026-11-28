"""PWA96 consumes the genuine completed H96 successor with its complete original ancestry."""
import argparse
import ast
import hashlib
import json
import sys
from pathlib import Path
from types import ModuleType

TOPIC = "topics/visible-flex-exact-nearby"
S = TOPIC+"/scripts/"
SOURCE = S+"fourfold_codazzi_pwa_height_phase_after_728.py"
ORIGINAL = S+"fourfold_codazzi_pwa_height_phase_saved_owner.py"
ORIGINAL_SHA = "5664d6ebc220cab75f14fdf4cb3faf60429a51f78a32029c5577fa7395a8e911"
GEN = S+"make_pwa_height_phase_saved_manifest.py"
GEN_SHA = "d38341f27b2884f4a1e87e05ee15d770a46e73aeace0dd4bf72978f106614229"
RESUME = S+"fourfold_codazzi_finite_trial_height_resume_owner.py"
RESUME_SHA = "538e9198a2b04fcb75389aefe95422ab6df909be3efbfe4a412f54aeab288981"
WORKER_SHA = "735b03dae67f035ca52464e5f4605c5b235479a1bbfedccfa095ff9164193b03"
H_MANIFEST_SHA = "e730fd1e12b72356c88aa7718f8baa4e5e5c083e66a60a6612d71028d281ef69"
MANIFEST = TOPIC+"/notes/2026-11-28-PWA-height-phase-after-728-inputs.json"
WORKFLOW = ".github/workflows/visible-exact-PWA-height-phase-after-728.yml"


def require(ok,message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def load(path,digest,name):
    raw=Path(path).read_bytes()
    require(sha(raw)==digest,"whole bound source: "+name)
    module=ModuleType(name)
    module.__file__=str(path)
    exec(compile(raw,str(path),"exec"),vars(module))
    return module


def configure(old_path,h_path):
    h=load(h_path,RESUME_SHA,"_complete_H96_actual_contract")
    owner=load(old_path,ORIGINAL_SHA,"_original_PWA96_science")
    # Every original public validator (including all seven H96 result validators)
    # is still called, with the new true manifest, source, run, commit and execution.
    owner.PREDECESSORS["H96"]={**owner.PREDECESSORS["H96"],"manifest":h.MANIFEST,
                               "execution_kind":h.EXECUTION_KIND}
    owner.SOURCE=owner.GENERATOR=SOURCE
    owner.__file__=__file__
    old_gather,old_admit=owner.gather,owner.admit
    def gather(root,height_actual,height_execution):
        table=old_gather(root,height_actual,height_execution)
        roles,files=table["roles"],table["files"]
        def add(role,path):
            raw=(root/path).read_bytes()
            require(0<len(raw)<100000 and all(x["role"]!=role and x["path"]!=path for x in files),
                    "one additional whole PWA predecessor object")
            files.append({"role":role,"path":path,"bytes":len(raw),"sha256":sha(raw),
                "git_blob_sha":hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()})
            roles[role]=path
        for role,(path,_) in h.PARENT_FILES.items():
            add(role,path)
        # H96_source already contains the complete successor owner.
        for role,path in [("PWA_original_owner",ORIGINAL),("PWA_original_generator",GEN),
                ("H96_resume_worker",S+"fourfold_codazzi_finite_trial_height_resume_public_worker.py"),
                ("H96_parent_rules",TOPIC+"/notes/2026-11-20-reviewed-public-CI-rules.json"),
                ("H96_resume_consumed",h.NOTES+"finite_trial_height_after_728_ci/consumed-target.json")]:
            add(role,path)
        files.sort(key=lambda x:x["role"])
        return table
    def admit(manifest,raws):
        roles=manifest["roles"]
        require(sha(raws[roles["H96_manifest"]])==H_MANIFEST_SHA
                and sha(raws[roles["H96_source"]])==RESUME_SHA
                and sha(raws[roles["H96_resume_worker"]])==WORKER_SHA,"complete H96 successor source chain")
        old,parent=h.check_parent(raws)
        admitted=old_admit(manifest,raws)
        a=admitted["H96"]
        e=json.loads(raws[roles["H96_execution"]])
        m=json.loads(raws[roles["H96_manifest"]])
        marker=json.loads(raws[roles["H96_resume_consumed"]])
        dest=m["operation"]["output_base"]+"/run-"+a["identity"]["run_id"]+"-1"
        require(a["identity"]["kind"]==m["scientific_kind"]==h.KIND
                and a["identity"]["scalar_stage"]==m["stage"]==h.STAGE
                and e["problem_id"]==marker["problem_id"]==h.PROBLEM
                and e["kind"]==h.EXECUTION_KIND and a["identity"]["run_id"]!=h.PARENT_RUN
                and a["identity"]["run_id"]==e["run_id"]==marker["run_id"]
                and marker["run_attempt"]=="1" and marker["manifest_sha256"]==H_MANIFEST_SHA
                and marker["output_directory"]==dest and roles["H96_actual"]==dest+"/actual-finite-trial-height.json"
                and roles["H96_execution"]==dest+"/execution.json"
                and a["resume"]==m["resume"]==h.RECEIPT
                and all(a[key]==parent[key] for key in h.CARRIERS)
                and a["result"]["complete_new_target_order"]==a["completed_targets"]==old["target_order"]
                and len(e["terminal_original_parent_checks"])>=2 and e["terminal_original_parent_after"]
                and a["height_integral_prefix"]["complete_relative_cells"]==2847,
                "all 7 original targets on exactly the completed resume and the real carried 96-column lineage")
        for receipt in [*e["terminal_original_parent_checks"],e["terminal_original_parent_after"]]:
            require(str(receipt["run"]["id"])==h.PARENT_RUN and receipt["job"]["id"]==140911924186
                    and all(obj["status"]=="completed" and obj["conclusion"]=="failure"
                            and obj["head_sha"]==h.PARENT_EVENT for obj in receipt.values()),
                    "the original failure consistently pinned before and after the genuine successful suffix")
        return admitted
    owner.gather,owner.admit=gather,admit
    return owner


def companion(role, original):
    directory = Path(__file__).resolve().parent
    snapshot = directory / (role+".py")
    return snapshot if snapshot.is_file() else directory / Path(original).name


def admit(manifest, raws):
    owner = configure(companion("PWA_original_owner", ORIGINAL), companion("H96_source", RESUME))
    return owner.admit(manifest, raws)


def validate_output(raw, manifest, manifest_sha, source_sha, run, attempt):
    owner = load(companion("PWA_original_owner", ORIGINAL), ORIGINAL_SHA, "_PWA96_full_saved_output_definition")
    return owner.validate_output(raw, manifest, manifest_sha, source_sha, run, attempt)


def prepare(root,height_actual=None,height_execution=None):
    sys.dont_write_bytecode=True
    owner=configure(root/ORIGINAL,root/RESUME)
    gen=load(root/GEN,GEN_SHA,"_original_PWA96_generator")
    old_load=gen.load
    gen.OWNER=SOURCE
    gen.load=lambda repo,path,name: owner if path==SOURCE else old_load(repo,path,name)
    gen.TEMPLATE=gen.TEMPLATE.replace(gen.MANIFEST,MANIFEST).replace(gen.WORKFLOW,WORKFLOW)
    gen.MANIFEST,gen.WORKFLOW=MANIFEST,WORKFLOW
    return gen.build(root,height_actual,height_execution)


def main():
    sys.dont_write_bytecode=True
    parser=argparse.ArgumentParser(add_help=False)
    parser.add_argument("--prepare",action="store_true")
    parser.add_argument("--repo",type=Path)
    parser.add_argument("--height-actual")
    parser.add_argument("--height-execution")
    parser.add_argument("--manifest-output",type=Path)
    parser.add_argument("--workflow-output",type=Path)
    parser.add_argument("--input-map",type=Path)
    args,_=parser.parse_known_args()
    if args.prepare:
        receipt,raw,yaml=prepare(args.repo.resolve(),args.height_actual,args.height_execution)
        if receipt["ready"]:
            for path,payload in [(args.manifest_output,raw),(args.workflow_output,yaml)]:
                if path:
                    path.write_bytes(payload)
        print(json.dumps(receipt))
        return 0
    mapping=json.loads(args.input_map.read_bytes())
    return configure(mapping["PWA_original_owner"],mapping["H96_source"]).main()


if __name__=="__main__":
    raise SystemExit(main())
