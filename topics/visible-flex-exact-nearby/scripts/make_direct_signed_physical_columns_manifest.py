"""Emit a single new public signed physical entry only after the complete actual ASQ23 and DCP parents."""
import argparse
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

TOPIC="topics/visible-flex-exact-nearby"
BASE=TOPIC+"/scripts/fourfold_codazzi_direct_signed_physical"
SCI=BASE+"_owner.py"
MANIFEST=TOPIC+"/notes/2026-11-28-three-direct-signed-physical-columns-inputs.json"
WORKFLOW=".github/workflows/fourfold-codazzi-three-signed-physical-columns-public.yml"
DCP=TOPIC+"/notes/particular_density_Theta_ci/run-46124617641-1/"
NEG=TOPIC+"/notes/negative_signed_waists_ci/run-46144609049-1/"


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ("repo","output","workflow-output"):
        parser.add_argument("--"+name,type=Path,required=True)
    a=parser.parse_args()
    root=a.repo.resolve()
    def module(name,path):
        desc=importlib.util.spec_from_file_location(name,root/path)
        obj=importlib.util.module_from_spec(desc)
        sys.modules[name]=obj
        desc.loader.exec_module(obj)
        return obj
    o=module("_ASQ25_new_owner_metadata",SCI)
    nm_path=TOPIC+"/notes/2026-11-28-negative-signed-waists-inputs.json"
    nm=json.loads((root/nm_path).read_bytes())
    previous={"ASQ23_"+s["role"]:s["path"] for s in nm["files"]}
    dirs={**previous,"current_reviewed_rules":previous["ASQ23_current_reviewed_rules"],"science":SCI,
        "physical":BASE+"_columns.py","direct":TOPIC+"/scripts/fourfold_codazzi_direct_signed_density_inverse.py",
        "worker":BASE+"_public_worker.py","generator":TOPIC+"/scripts/make_direct_signed_physical_columns_manifest.py",
        "proof":TOPIC+"/results/R149-supplement-direct-signed-physical-density-inverse-and-coordinate-residual.md",
        "cfc":TOPIC+"/scripts/fourfold_codazzi_complete_finite_columns_owner.py",
        "batch":TOPIC+"/scripts/fourfold_codazzi_complete_finite_columns_math.py",
        "carrier":TOPIC+"/scripts/fourfold_codazzi_complete_finite_columns_carriers.py",
        "recover":TOPIC+"/scripts/fourfold_codazzi_asq18_CFC_finite_reconstruction.py",
        "asq18":TOPIC+"/results/R149-supplement-actual-signed-Theta-trial-and-finite-inverse-by-primitive-residual.md",
        "asq20":TOPIC+"/results/R149-supplement-actual-low-coordinate-recovery-on-complete-physical-columns.md",
        "PA":TOPIC+"/notes/strict_nu_amplitude_border_ci/run-45906257068-1/actual-strict-nu-amplitude-border.json",
        "NP":TOPIC+"/notes/strict_nu_particular_ci/run-45893562391-1/actual-strict-nu-particular.json",
        "DCP_manifest":TOPIC+"/notes/2026-11-28-particular-density-Theta-inputs.json",
        "DCP_actual":DCP+"actual-particular-density-Theta.json","DCP_execution":DCP+"execution.json",
        "ASQ23_manifest":nm_path,"ASQ23_actual":NEG+"negative-signed-waists.json","ASQ23_execution":NEG+"execution.json",
        "ASQ23_consumed":TOPIC+"/notes/negative_signed_waists_ci/consumed-v1.json"}
    specs=[]
    for role,path in dirs.items():
        raw=(root/path).read_bytes()
        o.require(0<len(raw)<100000,"whole public input: "+role)
        if path.endswith(".py"):
            ast.parse(raw)
        specs.append({"role":role,"path":path,"bytes":len(raw),"sha256":o.sha(raw),"encoding":"utf-8",
                      "git_blob_sha":hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()})
    roles={s["role"]:s for s in specs}
    neg,ex=(json.loads((root/dirs["ASQ23_"+s]).read_bytes()) for s in ("actual","execution"))
    orig=module("_ASQ25_original_asq23_definition",dirs["ASQ23_science"])
    orig.validate(neg,nm)
    o.require(neg["complete"] and ex["complete"] and neg["proved"] and neg["actual_returncode"]==ex["actual_child_returncode"]==0
              and neg["completed_targets"]==ex["completed_natural_targets"]==orig.TARGETS and neg["new_complete_negative_trial_cells"]==3073
              and ex["run_id"]==neg["identity"]["run_id"]=="46144609049" and ex["scientific_children"]==1,
              "real whole successful ASQ23 terminal execution before any entry")
    o.require(all(roles["ASQ23_"+s["role"]]["sha256"]==s["sha256"] for s in nm["files"]) and
              roles["ASQ23_manifest"]["sha256"]==o.ASQ23_MANIFEST and roles["DCP_manifest"]["sha256"]==o.DCP_MANIFEST and
              roles["DCP_actual"]["sha256"]==o.DCP_SHA and roles["ASQ23_science"]["sha256"]==o.ASQ23_SOURCE and
              roles["direct"]["sha256"]==o.DIRECT_SHA and roles["proof"]["sha256"]==o.PROOF_SHA,"all immutable originals")
    review=json.loads((root/dirs["current_reviewed_rules"]).read_bytes())
    o.require(all(o.sha((root/path).read_bytes())==digest for path,digest in review["readme_sha256"].items()) and
              review["model"]=="gpt-6.2-astra" and review["reasoning_effort"]=="ultra","whole two currently reviewed README rules")
    parents={n:dict(run=run,**{k:roles[n+"_"+k]["sha256"] for k in ("manifest","actual","execution")})
             for n,run in (("DCP","46124617641/1"),("ASQ23","46144609049/1"))}
    m={"kind":o.MANIFEST_KIND,"scientific_kind":o.KIND,"repository":o.REPO,"problem_id":"direct_signed_theta_coordinate_columns_v1",
       "parameters":o.PARAMETERS,"runtime":o.RUNTIME,"target_order":o.TARGETS,"files":specs,"parents":parents,
       "allowed_scientific_fields":sorted(o.FIELDS),"whole_original_descriptors":nm["whole_original_descriptors"],
       "reviewed_rules":roles["current_reviewed_rules"],
       "operation":dict(nm["operation"],output_base=TOPIC+"/notes/direct_signed_physical_ci",
                        consumed_marker=TOPIC+"/notes/direct_signed_physical_ci/consumed-v1.json")}
    body=o.encode(m)
    o.require(len(body)<100000,"whole small manifest")
    template=module("_ASQ25_original_workflow_constructor",TOPIC+"/scripts/make_whole_selected_signed_source_manifest.py")
    template.FILES,template.MANIFEST,template.WORKFLOW=dirs,MANIFEST,WORKFLOW
    wf=template.source_workflow(o.sha(body)).replace("whole selected signed Newton and nu ordinary sources",
         "three signed physical Theta and recovered coordinates").replace("R149-whole-selected-signed-sources-v1",
         "R149-three-direct-signed-physical-cols-v1").replace("  signed-sources:","  signed-coordinates:").replace(
         "Admit all original inputs and compute both complete signed source targets","Receive the three actual signed physical columns")
    for path,raw in ((a.output,body),(a.workflow_output,wf.encode())):
        o.require(not path.exists(),"one first new metadata file")
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_bytes(raw)
        o.require(path.read_bytes()==raw,"whole new metadata readback")
    o.require(not any(k in sys.modules for k in ("numpy","flint","scipy")),"metadata only")
    print(o.encode({"new_scientific_calls":0,"manifest":o.sha(body),"workflow":o.sha(wf.encode())}).decode(),end="")


if __name__=="__main__":
    main()
