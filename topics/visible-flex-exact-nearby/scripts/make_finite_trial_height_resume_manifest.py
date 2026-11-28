"""Metadata-only H96 suffix entry. Never computes a radial cell or a scientific target."""
import argparse
import ast
import copy
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
S = TOPIC+"/scripts/"
SOURCE = S+"fourfold_codazzi_finite_trial_height_resume_owner.py"
MATH = S+"fourfold_codazzi_finite_trial_height_resume_math.py"
WORKER = S+"fourfold_codazzi_finite_trial_height_resume_public_worker.py"
GENERATOR = S+"make_finite_trial_height_resume_manifest.py"
OLD_GENERATOR = S+"make_finite_trial_height_manifest.py"
ORIGINAL_SHA = "26cfe21a6bb26be29611660e2ace51f90b06eaf33072a809cbc8802de4adb221"
MANIFEST = TOPIC+"/notes/2026-11-28-finite-trial-height-after-728-inputs.json"
WORKFLOW = ".github/workflows/visible-exact-finite-trial-height-after-728.yml"


def require(ok,message):
    if not ok:
        raise ValueError(message)


def load(root,path):
    spec=importlib.util.spec_from_file_location("_"+Path(path).stem,root/path)
    obj=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


def build(root):
    require(not any(x in sys.modules for x in ("numpy","flint","scipy")), "no local scientific inputs or execution")
    sys.dont_write_bytecode=True
    owner,math,worker=(load(root,p) for p in (SOURCE,MATH,WORKER))
    require(owner.sha((root/OLD_GENERATOR).read_bytes())==ORIGINAL_SHA,"whole original H96 generator")
    oldgen=load(root,OLD_GENERATOR)
    old=json.loads((root/owner.ORIGINAL_MANIFEST).read_bytes())
    new=copy.deepcopy(old)
    aliases={"science","worker","generator","reviewed_rules"}
    for item in new["files"]:
        role=item["role"]
        raw=(root/item["path"]).read_bytes()
        require(len(raw)==item["bytes"] and owner.sha(raw)==item["sha256"],
                "original whole H96 input retained: "+role)
        if role in aliases:
            item["role"]="H96_original_"+role
            new["roles"][item["role"]]=item["path"]
    def add(role,path):
        require(all(x["path"]!=path and x["role"]!=role for x in new["files"]),"unique successor role and path")
        raw=(root/path).read_bytes()
        require(0<len(raw)<100000,"whole small continuation input")
        if path.endswith(".py"):
            ast.parse(raw)
        new["files"].append({"role":role,"path":path,"bytes":len(raw),"sha256":owner.sha(raw),
            "git_blob_sha":hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()})
        new["roles"][role]=path
    for role,(path,_) in owner.PARENT_FILES.items():
        add(role,path)
    for role,path in [("science",SOURCE),("worker",WORKER),("generator",GENERATOR),("resume_math",MATH),
                      ("reviewed_rules",owner.REVIEW[0])]:
        add(role,path)
    new["files"].sort(key=lambda x:x["role"])
    raws={item["path"]:(root/item["path"]).read_bytes() for item in new["files"]}
    original,parent=owner.check_parent(raws)
    rules=json.loads(raws[owner.REVIEW[0]])
    require(all(owner.sha((root/path).read_bytes())==s for path,s in rules["readme_sha256"].items()),
            "both reviewed READMEs remain current")
    for path,tree in ((SOURCE,owner.build_main(raws[new["roles"]["H96_original_science"]])),
                      (MATH,math.build_compute(raws[new["roles"]["height_math"]])),
                      (WORKER,worker.build_adapter(root))):
        compile(tree,path,"exec")
    require(old==original and parent["height_integral_prefix"]["complete_relative_cells"]==math.START
            and owner.sha(raws[MATH])==owner.MATH_SHA and owner.sha(raws[SOURCE])==worker.OWNER_SHA,
            "whole candidate execution chain and exact signed prefix")
    op=new["operation"]
    op["output_base"]=owner.NOTES+"finite_trial_height_after_728_ci"
    op["consumed_marker"]=op["output_base"]+"/consumed-target.json"
    new.update(kind=owner.MANIFEST_KIND,scientific_kind=owner.KIND,stage=owner.STAGE,
        problem_id=owner.PROBLEM,resume=owner.RECEIPT,expected_current_input_count=len(new["files"]),
        allowed_scientific_fields=sorted(old["allowed_scientific_fields"]+["resume"]))
    raw=owner.canonical(new)
    require(len(raw)<100000 and len(new["historical_inputs"])==51 and new["target_order"]==old["target_order"]
            and new["parameters"]==old["parameters"], "same complete arithmetic, old closure and seven targets")
    sparse=sorted({"README.md",TOPIC+"/README.md",MANIFEST,*oldgen.BOOTSTRAP,*(x["path"] for x in new["files"])})
    workflow=oldgen.WORKFLOW_TEMPLATE
    replacements={oldgen.WORKFLOW:WORKFLOW,oldgen.WORKER:WORKER,oldgen.MANIFEST:MANIFEST,
        "name: R149 original96 complete height and reduced phase rows":"name: R149 original96 complete height after 728 paid cells",
        "group: visible-flex-exact-original96-complete-height-20261128":"group: visible-flex-exact-H96-after-46123190757-1",
        "first-complete-original96-height-rows:":"joint-original96-height-rows-after-728:",
        "  contents: write":"  contents: write\n  actions: read",
        "@CONTAINER@":oldgen.CONTAINER,"@MANIFEST_SHA@":owner.sha(raw),
        "@SPARSE_PATHS@":"\n".join("            /"+path for path in sparse)}
    for pattern,replacement in replacements.items():
        require(workflow.count(pattern)==1,"one exact original workflow site: "+pattern)
        workflow=workflow.replace(pattern,replacement,1)
    return raw,workflow.encode()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,required=True)
    parser.add_argument("--manifest-output",type=Path)
    parser.add_argument("--workflow-output",type=Path)
    args=parser.parse_args()
    raw,workflow=build(args.repo.resolve())
    for path,data in [(args.manifest_output,raw),(args.workflow_output,workflow)]:
        if path:
            path.write_bytes(data)
    print(json.dumps({"manifest_bytes":len(raw),"manifest_sha256":hashlib.sha256(raw).hexdigest(),
        "workflow_bytes":len(workflow),"workflow_sha256":hashlib.sha256(workflow).hexdigest(),
        "paid_cells":728,"first_new_cell":728,"exclusive_stop":2847,"all_columns":96,
        "old_and_new_scientific_targets_evaluated_locally":0}))


if __name__=="__main__":
    main()
