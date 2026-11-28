"""Build the first signed negative-waist manifest and its single new public entry. Metadata only."""
import argparse
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

TOPIC="topics/visible-flex-exact-nearby"
BASE=TOPIC+"/scripts/fourfold_codazzi_negative_defect_signed_waist"
MANIFEST=TOPIC+"/notes/2026-11-28-negative-signed-waists-inputs.json"
WORKFLOW=".github/workflows/fourfold-codazzi-negative-signed-waists-public.yml"
WSS=TOPIC+"/notes/2026-11-28-whole-selected-signed-sources-inputs.json"
SCI=BASE+"_owner.py"
WSSDIR=TOPIC+"/notes/whole_selected_signed_sources_ci/run-46136409179-1/"
RNAME=TOPIC+"/results/R149-supplement-two-signed-negative-waist-responses-and-common-Gram-remainder.md"

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for arg in ("repo","output","workflow-output"):
        parser.add_argument("--"+arg,type=Path,required=True)
    args=parser.parse_args()
    root=args.repo.resolve()
    def module(path,name):
        spec=importlib.util.spec_from_file_location(name,root/path)
        mod=importlib.util.module_from_spec(spec)
        sys.modules[name]=mod
        spec.loader.exec_module(mod)
        return mod
    owner=module(SCI,"_ASQ23_new_owner_metadata")
    wm=json.loads((root/WSS).read_bytes())
    orig=module(TOPIC+"/scripts/make_whole_selected_signed_source_manifest.py","_ASQ23_original_WSS_generator")
    wfiles={"wss_"+v["role"]:v["path"] for v in wm["files"]}
    dirs={**wfiles,"wss_manifest":WSS,"wss_actual":WSSDIR+"whole-selected-signed-source.json",
         "wss_execution":WSSDIR+"execution.json","wss_admission":WSSDIR+"root-complete-admission.json",
         "current_reviewed_rules":wfiles["wss_current_reviewed_rules"],"proof":RNAME,"science":SCI,
         "math":BASE+"_math.py","worker":BASE+"_public_worker.py","generator":TOPIC+"/scripts/make_negative_defect_signed_waist_manifest.py",
         "nu_math":TOPIC+"/scripts/fourfold_codazzi_strict_nu_particular_math.py",
         "asq22":TOPIC+"/results/R149-supplement-small-true-Theta-reception-of-the-negative-parameter-defect.md"}
    specs=[]
    for role,path in dirs.items():
        raw=(root/path).read_bytes()
        owner.require(0<len(raw)<100000,"whole small source, proof or receipt")
        if path.endswith(".py"):
            ast.parse(raw,filename=path)
        specs.append(dict(role=role,path=path,bytes=len(raw),sha256=owner.sha(raw),
             git_blob_sha=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest(),encoding="utf-8"))
    roles={i["role"]:i for i in specs}
    owner.require(all(roles[k]["sha256"]==v for k,v in owner.FIXED.items()) and len(wm["files"])==19
         and all(roles["wss_"+s["role"]]["sha256"]==s["sha256"] for s in wm["files"]),"entire fixed WSS actual scientific closure")
    review=json.loads((root/dirs["current_reviewed_rules"]).read_bytes())
    owner.require(all(owner.sha((root/k).read_bytes())==v for k,v in review["readme_sha256"].items()) and review["model"]=="gpt-6.2-astra"
                  and review["reasoning_effort"]=="ultra","both actually read current complete rules")
    m={"kind":owner.MANIFEST_KIND,"scientific_kind":owner.KIND,"problem_id":"two_genuine_signed_negative_waists_v1",
       "repository":owner.REPOSITORY,"parameters":owner.PARAMETERS,"runtime":owner.RUNTIME,"target_order":owner.TARGETS,"files":specs,
       "allowed_scientific_fields":sorted(owner.FIELDS),"whole_original_descriptors":wm["whole_original_descriptors"],
       "reviewed_rules":roles["current_reviewed_rules"],"operation":dict(wm["operation"],
         output_base=TOPIC+"/notes/negative_signed_waists_ci",consumed_marker=TOPIC+"/notes/negative_signed_waists_ci/consumed-v1.json")}
    payload=owner.canonical(m)
    digest=owner.sha(payload)
    orig.FILES,orig.MANIFEST,orig.WORKFLOW=dirs,MANIFEST,WORKFLOW
    workflow=orig.source_workflow(digest)
    for x,y in (("R149 whole selected signed Newton and nu ordinary sources","R149 two signed negative Newton and parameter waists"),
                ("R149-whole-selected-signed-sources-v1","R149-two-negative-signed-waists-v1"),
                ("signed-sources:","signed-waists:"),("both complete signed source targets","both genuine signed negative waist responses")):
        owner.require(workflow.count(x)==1,"one public workflow identity "+x)
        workflow=workflow.replace(x,y)
    owner.require(not any(k in sys.modules for k in ("numpy","flint","scipy")) and len(payload)<100000,"metadata-only bounded original closure")
    for p,body in ((args.output,payload),(args.workflow_output,workflow.encode())):
        owner.require(not p.exists(),"first fresh metadata path")
        p.parent.mkdir(parents=True,exist_ok=True)
        p.write_bytes(body)
        owner.require(p.read_bytes()==body,"identical complete canonical output")
    print(owner.canonical({"manifest":digest,"workflow":owner.sha(workflow.encode()),"files":len(specs),"new_scientific_calls":0}).decode(),end="")

if __name__=="__main__":
    main()
