"""Build the immutable first public fixed-affine negative Newton input manifest and workflow."""
import argparse
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

TOPIC="topics/visible-flex-exact-nearby"
PREFIX=TOPIC+"/scripts/fourfold_codazzi_fixed_negative_Newton"
SCI=PREFIX+"_owner.py"
MANIFEST=TOPIC+"/notes/2026-11-28-fixed-affine-negative-Newton-trajectory-inputs.json"
WORKFLOW=".github/workflows/fourfold-codazzi-fixed-affine-negative-Newton-trajectory-public.yml"
NEG=TOPIC+"/notes/2026-11-28-negative-signed-waists-inputs.json"
FM=TOPIC+"/notes/2026-11-26-R144-fixed-eta0-correlated-mean-inputs.json"


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ("repo","output","workflow-output"):
        p.add_argument("--"+k,type=Path,required=True)
    arg=p.parse_args()
    root=arg.repo.resolve()
    def module(path,label):
        s=importlib.util.spec_from_file_location(label,root/path)
        obj=importlib.util.module_from_spec(s)
        sys.modules[label]=obj
        s.loader.exec_module(obj)
        return obj
    o=module(SCI,"_ASQ27_first_operational_schema")
    nm,fm=[json.loads((root/z).read_bytes()) for z in (NEG,FM)]
    previous={"ASQ23_"+s["role"]:s["path"] for s in nm["files"]}
    fixed={"FM_"+s["role"]:s["path"] for s in fm["files"]
           if s["role"] in ("science","object","definition_arb","definition_bulk")}
    dirs={**previous,**fixed,"ASQ23_manifest":NEG,"FM_manifest":FM,"current_reviewed_rules":previous["ASQ23_current_reviewed_rules"],
        "science":SCI,"worker":PREFIX+"_public_worker.py","generator":TOPIC+"/scripts/make_fixed_negative_Newton_trajectory_manifest.py",
        "radial":PREFIX+"_radial.py","trial":PREFIX+"_trial.py",
        "proof":TOPIC+"/results/R149-supplement-fixed-affine-negative-Newton-trajectory-and-flat-quadrature.md",
        "ASQ26_proof":TOPIC+"/results/R149-supplement-correlated-base-to-selected-negative-Newton-response.md",
        "ASQ26_receipt":TOPIC+"/notes/2026-11-28-ASQ26-correlated-negative-original-consequence.json",
        "D_proof":TOPIC+"/results/R133-supplement-exact-selected-parameter-core-differences-and-finite193-transfer.md",
        "D_actual_proof":TOPIC+"/results/R133-supplement-actual-selected-parameter-core-scalar-fees-and-collar-jets.md",
        "D_execution":TOPIC+"/notes/selected_parameter_core_scalar_fees_ci/run-43713242980-1/execution.json"}
    specs=[]
    for role,path in dirs.items():
        b=(root/path).read_bytes()
        o.require(0<len(b)<100000,"entire small source or metadata file "+role)
        if path.endswith(".py"):
            ast.parse(b,filename=path)
        specs.append(dict(role=role,path=path,bytes=len(b),sha256=o.sha(b),encoding="utf-8",
                          git_blob_sha=hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()))
    roles={s["role"]:s for s in specs}
    o.require(all(roles[k]["sha256"]==v for k,v in o.FIXED.items()) and
        all(roles["ASQ23_"+s["role"]]["sha256"]==s["sha256"] for s in nm["files"]),"entire frozen historical family")
    review=json.loads((root/dirs["current_reviewed_rules"]).read_bytes())
    o.require(review["model"]=="gpt-6.2-astra" and review["reasoning_effort"]=="ultra" and
              all(o.sha((root/k).read_bytes())==z for k,z in review["readme_sha256"].items()),"complete current review of both README files")
    historical=[s for s in fm["historical_inputs"] if s["role"] in o.GEOMETRY]
    o.require(len(historical)==2,"the entire affine scientific object and direction")
    contract={ "kind":o.MANIFEST_KIND,"scientific_kind":o.KIND,"problem_id":"fixed_affine_negative_Newton_trajectory_v1",
        "repository":o.REPO,"runtime":o.RUNTIME,"parameters":o.PARAMETERS,"target_order":o.TARGETS,
        "allowed_scientific_fields":sorted(o.FIELDS),"files":specs,"whole_original_descriptors":nm["whole_original_descriptors"],
        "original_affine_historical_inputs":historical,"reviewed_rules":roles["current_reviewed_rules"],
        "operation":dict(nm["operation"],output_base=TOPIC+"/notes/fixed_negative_Newton_trajectory_ci",
                         consumed_marker=TOPIC+"/notes/fixed_negative_Newton_trajectory_ci/consumed-v1.json")}
    body=o.encode(contract)
    o.require(len(body)<100000,"whole new manifest")
    previous_worker=module(dirs["worker"],"_ASQ27_public_transport_schema")
    previous_worker.adapter((root/previous_worker.OLD).read_bytes())
    t=module(TOPIC+"/scripts/make_whole_selected_signed_source_manifest.py","_ASQ27_orig_workflow_constructor")
    t.FILES,t.MANIFEST,t.WORKFLOW=dirs,MANIFEST,WORKFLOW
    wf=t.source_workflow(o.sha(body))
    for x,y in (("whole selected signed Newton and nu ordinary sources","fixed affine negative Newton trajectory and true waist"),
                ("R149-whole-selected-signed-sources-v1","R149-fixed-affine-negative-Newton-trajectory-v1"),
                ("  signed-sources:","  fixed-trajectory:"),
                ("Admit all original inputs and compute both complete signed source targets","Admit the fixed affine geometry and measure the true negative Newton response")):
        o.require(wf.count(x)==1,"single exact first workflow substitution "+x)
        wf=wf.replace(x,y)
    for path,b in ((arg.output,body),(arg.workflow_output,wf.encode())):
        o.require(not path.exists(),"one first manifest/workflow target")
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_bytes(b)
        o.require(path.read_bytes()==b,"whole first source output")
    o.require(not any(k in sys.modules for k in ("flint","numpy","scipy")),"metadata-only preparation")
    print(o.encode({"files":len(specs),"additional_historical":2,"new_scientific_calls":0,"manifest_sha256":o.sha(body),
                    "workflow_sha256":o.sha(wf.encode())}).decode(),end="")


if __name__=="__main__":
    main()
