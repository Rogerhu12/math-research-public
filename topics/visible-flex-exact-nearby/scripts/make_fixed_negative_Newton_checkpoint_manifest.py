"""Bind every original ASQ27 input and the whole genuine terminal failure into its distinct successor."""
import argparse
import ast
import hashlib
import json
from pathlib import Path
import sys

import fourfold_codazzi_fixed_negative_Newton_checkpoint as f
import fourfold_codazzi_fixed_negative_Newton_checkpoint_worker as worker


def build(root):
    base,d=f.parent(root)
    entries=[]
    def add(role,path):
        body=(root/path).read_bytes()
        f.require(0<len(body)<100000,"whole small role "+role)
        if path.endswith(".py"):
            ast.parse(body,filename=path)
        s=dict(role=role,path=path,bytes=len(body),sha256=f.sha(body),encoding="utf-8",
               git_blob_sha=hashlib.sha1(b"blob "+str(len(body)).encode()+b"\0"+body).hexdigest())
        entries.append(s)
        return s
    for old in base["files"]:
        role=old["role"]
        new=add("ASQ27_"+role if role in ("science","worker","generator") else role,old["path"])
        f.require(all(old[k]==new[k] for k in old if k!="role"),"all original 49 whole current files")
    for role,(path,digest) in f.FILES.items():
        if role not in ("ASQ27_science","ASQ27_generator","ASQ27_worker"):
            f.require(add(role,path)["sha256"]==digest,"fixed whole terminal object "+role)
    for role,path in (("science",f.SCIENCE),("worker",f.WORKER),("generator",f.GENERATOR)):
        add(role,path)
    roles={s["role"]:s for s in entries}
    f.require(len(entries)==len(roles)==56 and all(roles[k]["sha256"]==d for k,(p,d) in f.FILES.items()),
              "complete old ancestry plus three actual zero-cell objects and distinct first owner")
    review=json.loads((root/base["reviewed_rules"]["path"]).read_bytes())
    f.require(base["reviewed_rules"]==roles["current_reviewed_rules"] and review["model"]=="gpt-6.2-astra" and
              review["reasoning_effort"]=="ultra" and all(f.sha((root/k).read_bytes())==s for k,s in review["readme_sha256"].items()),
              "complete current two-README admission")
    m=dict(base,kind=f.MANIFEST_KIND,scientific_kind=f.KIND,files=entries,allowed_scientific_fields=sorted(f.FIELDS),
           problem_id="fixed_negative_Newton_atomic_checkpoint_v1",predecessor=dict(run=f.PARENT_RUN,attempt="1",
           job=f.PARENT_JOB,event=f.EVENT,accepted_cells=0,accepted_targets=0),
           operation=dict(base["operation"],output_base=f.NEW_BASE,consumed_marker=f.NEW_BASE+"/consumed-v1.json"))
    fixed_source=root/roles["ASQ23_science"]["path"]
    f.require(fixed_source.is_file() and len(m["original_affine_historical_inputs"])==2,"original 184/32 and affine two")
    raw=f._original.encode(m)
    f.require(len(raw)<100000,"whole immutable manifest")
    tree,_,_=worker.adapter(root)
    compile(tree,"<ASQ27R operational terminal gates>","exec")
    # Read the complete original workflow, changing the sparse list and precisely the new entry definitions.
    oldpath=".github/workflows/fourfold-codazzi-fixed-affine-negative-Newton-trajectory-public.yml"
    original=(root/oldpath).read_bytes()
    f.require(f.sha(original)=="3cc643dad7c8d91d45575cebbd8015118d0378d240a610eb83f60d461b3c7ba3","whole original public workflow")
    t=original.decode()
    sparse=sorted({s["path"] for s in entries}|{"README.md",f.TOPIC+"/README.md",f.MANIFEST})
    start=t.index("          sparse-checkout: |\n")+len("          sparse-checkout: |\n")
    end=t.index("      - name: Trust the original mounted checkout\n",start)
    t=t[:start]+"".join("            /"+s+"\n" for s in sparse)+t[end:]
    for a,b in ((oldpath,f.WORKFLOW),("name: R149 fixed affine negative Newton trajectory and true waist",
            "name: R149 negative Newton trajectory after actual zero-cell failure"),
            ("group: R149-fixed-affine-negative-Newton-trajectory-v1","group: R149-fixed-negative-Newton-atomic-checkpoint-v1"),
            ("  fixed-trajectory:","  fixed-trajectory-checkpoint:"),
            ("python "+f.FILES["ASQ27_worker"][0],"python "+f.WORKER),
            ("--manifest "+f.PARENT_MANIFEST,"--manifest "+f.MANIFEST),
            ("--manifest-sha "+f.FILES["ASQ27_manifest"][1],"--manifest-sha "+f.sha(raw))):
        t=f.replace_once(t,a,b)
    f.require(not any(k in sys.modules for k in ("flint","numpy","scipy")),"no scientific construction during preparation")
    return raw,t.encode()


if __name__=="__main__":
    arg=argparse.ArgumentParser(description=__doc__)
    for k in ("repo","output","workflow-output"):
        arg.add_argument("--"+k,required=True,type=Path)
    args=arg.parse_args()
    data,wf=build(args.repo.resolve())
    for path,b in ((args.output,data),(args.workflow_output,wf)):
        with path.open("xb") as stream:
            stream.write(b)
        f.require(path.read_bytes()==b,"whole distinct first entry")
    print(json.dumps(dict(whole_files=len(json.loads(data)["files"]),local_scientific_targets=0,
                          manifest_sha256=f.sha(data),workflow_sha256=f.sha(wf))))
