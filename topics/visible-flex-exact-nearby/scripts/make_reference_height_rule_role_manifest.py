"""Exact metadata continuation of the genuine zero-child WRC rule-role failure."""
from __future__ import annotations
import argparse,ast,hashlib,importlib.util,json,sys
from pathlib import Path

TOPIC="topics/visible-flex-exact-nearby"
PARENT_GENERATOR=TOPIC+"/scripts/make_complete_reference_world_height_manifest.py"
PARENT_GENERATOR_SHA="cb5a00a95866237fb60b6da1f9ea720b870a18c9a1c391e50a44d07d9d578838"
WORKER=TOPIC+"/scripts/fourfold_codazzi_complete_reference_height_rule_role_public_worker.py"
GENERATOR=TOPIC+"/scripts/make_reference_height_rule_role_manifest.py"
MANIFEST=TOPIC+"/notes/2026-11-27-reference-height-rule-role-inputs.json"
WORKFLOW=".github/workflows/visible-exact-reference-height-rule-role.yml"


def require(ok,message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),
        ensure_ascii=False,allow_nan=False)+"\n").encode()


def load(root,path,name,digest=None):
    raw=(root/path).read_bytes()
    require(0<len(raw)<100000,"whole small metadata source")
    if digest is not None:
        require(hashlib.sha256(raw).hexdigest()==digest,"unchanged complete parent generator")
    ast.parse(raw.decode(),filename=path)
    spec=importlib.util.spec_from_file_location(name,root/path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


def build(root):
    require(not any(name in sys.modules for name in ("numpy","flint","scipy")),
        "only metadata is generated")
    sys.dont_write_bytecode=True
    worker=load(root,WORKER,"_WRC_rule_role_metadata_worker")
    previous_raw=worker.read_whole(root,worker.PREVIOUS_MANIFEST,worker.PREVIOUS_MANIFEST_SHA)
    manifest=json.loads(previous_raw)
    files=[dict(item) for item in manifest["files"]]
    roles=dict(manifest["roles"])
    for item in files:
        if item["role"]=="RHI_reviewed_rules":
            item["role"]="reviewed_rules"
        elif item["role"] in ("worker","generator"):
            old_role=item["role"];item["role"]="previous_"+old_role
            roles[item["role"]]=item["path"]
    def add(role,path):
        raw=(root/path).read_bytes();raw.decode()
        require(0<len(raw)<100000,"whole complete new metadata input")
        if path.endswith(".py"):
            ast.parse(raw.decode(),filename=path)
        spec={"role":role,"path":path,"bytes":len(raw),
            "sha256":hashlib.sha256(raw).hexdigest(),
            "git_blob_sha":hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()}
        require(not any(item["path"]==path or item["role"]==role for item in files),
            "one complete current object per receipt")
        files.append(spec);roles[role]=path
    for role,path in [("worker",WORKER),("generator",GENERATOR),
        ("predecessor_manifest",worker.PREVIOUS_MANIFEST),("previous_failure",worker.FAILURE)]:
        add(role,path)
    manifest.update(files=sorted(files,key=lambda item:item["role"]),
        expected_current_input_count=len(files),roles=roles,
        explicit_zero_child_continuation={
            "kind":"WRC_zero_child_rule_role_continuation_v1",
            "previous_run_id":"45941738781","previous_run_attempt":"1",
            "previous_manifest_sha256":worker.PREVIOUS_MANIFEST_SHA,
            "failure_receipt_path":worker.FAILURE,"failure_receipt_sha256":worker.FAILURE_SHA,
            "previous_completed_targets":[],"mathematical_target_and_input_changes":0,
            "primary_rules_role_repaired":"reviewed_rules"})
    manifest["scope"].update({
        "genuine_prechild_rule_role_failure_explicitly_admitted":True,
        "same_whole_reviewed_rules_object_and_both_path_aliases_retained":True,
        "original_four_scientific_targets_and_owner_unchanged":True,
        "prior_native_scientific_result_invented":False})
    worker.admit_zero_predecessor(root,manifest)
    compile(worker.build_adapter(root),WORKER,"exec")
    raw=canonical(manifest)
    require(len(raw)<100000,"one whole concrete continuation manifest")
    parent=load(root,PARENT_GENERATOR,"_WRC_original_workflow_definition",PARENT_GENERATOR_SHA)
    parent.workflow.__globals__.update(MANIFEST=MANIFEST,WORKFLOW=WORKFLOW,WORKER=WORKER)
    yaml=parent.workflow(manifest["files"],hashlib.sha256(raw).hexdigest())
    require(not any(name in sys.modules for name in ("numpy","flint","scipy")),
        "no mathematical target runs in metadata generation")
    return raw,yaml


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",default=".",type=Path)
    parser.add_argument("--check-only",action="store_true")
    args=parser.parse_args();root=args.repo.resolve()
    raw,yaml=build(root)
    for relative,value in ((MANIFEST,raw),(WORKFLOW,yaml)):
        path=root/relative
        if args.check_only:
            require(path.read_bytes()==value,"exact complete continuation entry: "+relative)
        else:
            path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(value)
    print(json.dumps({"ready":True,"manifest":MANIFEST,"manifest_bytes":len(raw),
        "manifest_sha256":hashlib.sha256(raw).hexdigest(),"workflow":WORKFLOW,
        "previous_run":"45941738781/1","previous_scientific_children":0,
        "local_scientific_targets_evaluated":0},sort_keys=True))


if __name__=="__main__":
    main()
