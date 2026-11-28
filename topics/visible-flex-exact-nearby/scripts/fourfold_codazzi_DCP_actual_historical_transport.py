"""Receive the original 269 current and 53 heterogeneous historical DCP blobs after the real no-child failure."""
import argparse
import ast
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import sys
from urllib.request import HTTPRedirectHandler, Request, build_opener

TOPIC="topics/visible-flex-exact-nearby"
S=TOPIC+"/scripts/"
SOURCE=S+"fourfold_codazzi_DCP_actual_historical_transport.py"
DCP="d85c0d55f82e50d9f061756a4d132db6780992654f3c01fbf5ae9a03657c44df"
CUR="80d0fb93965d0480762f0df54d38ffe62007ab9dcc134835d03bb5b57a45dbf2"
HIST="a483fe515d3b6fca608749911e6ef5eb8090f6ce6b1b193bed0ba42698863fd7"
BASE=TOPIC+"/notes/direct_signed_physical_ci/run-46150713718-1/"
OUTCOME={
    "transport_failed_execution":(BASE+"execution.json","5eba5710b93cbca94ae11c8da0913ba345ffaee4d5dd5253d14d7a121ee5d123"),
    "transport_failed_report":(BASE+"report.md","dbbbfa3dcad13333e790766b7262421a77059dab15233b015d275d6db06e6222")}
RUN=46150713718
JOB=140996546327
EVENT="e289e68549748f79d60900ca2cace49556271dfc"
CASES={
    "ASQ25":("14b776d33235fdd27246c051909fc8ee9b3d426c2fd9e3909f7c3499d19df697",
        "c20e585101ca29cf3c01d39dd3954bd01f6bf6d9d282107bcc20194ed720c3f0",
        ".github/workflows/fourfold-codazzi-three-signed-physical-columns-public.yml",
        TOPIC+"/notes/2026-11-28-three-direct-signed-physical-columns-inputs.json",53),
    "ASQ28":("abe9794975734c1a2040c39753662c95c1d01383636276bd7f77b9a2c0162e41",
        "df4d90081cd1e0fca4d52351dff596f27b665345d2b2e90d7d1991aa295d4cf6",
        ".github/workflows/fourfold-codazzi-natural-terminal-Ai-high-action.yml",
        TOPIC+"/notes/2026-11-28-natural-terminal-Ai-high-action-inputs.json",93)}
RECEIPT={"failed_run":RUN,"failed_attempt":1,"failed_job":JOB,"failed_event":EVENT,
    "accepted_scientific_cells":0,"scientific_children":0,"scientific_files":[],
    "DCP_current_order_sha256":CUR,"DCP_historical_order_sha256":HIST}


def require(ok,message):
    if not ok:
        raise ValueError(message)


def sha(b):
    return hashlib.sha256(b).hexdigest()


def canonical(v):
    return (json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()


def whole(path,digest):
    b=Path(path).read_bytes()
    require(sha(b)==digest,"whole bound "+str(path))
    return b


def load(path,digest):
    from types import ModuleType
    m=ModuleType("_whole_"+path.stem)
    m.__file__=str(path)
    exec(compile(whole(path,digest),str(path),"exec"),vars(m))
    return m


def zero_parent(root):
    for _,(path,digest) in OUTCOME.items():
        whole(root/path,digest)
    e=json.loads((root/OUTCOME["transport_failed_execution"][0]).read_bytes())
    require(e["run_id"]==str(RUN) and e["run_attempt"]=="1" and e["event_commit"]==EVENT
        and e["manifest_sha256"]==CASES["ASQ25"][0] and e["scientific_children"]==0
        and e["scientific_files"]==e["completed_natural_targets"]==[] and e["actual_child_returncode"] is None
        and not e["complete"] and e["whole_new_current_input_count"]==53 and
        "consumed_marker_publication" not in e and e["failure"]["type"]=="KeyError"
        and e["failure"]["message"]=="'restore_only'" and "in stage_dcp" in e["failure"]["traceback"],
        "real failed transport before reservation, zero attempted or saved scientific targets")


def checked_original(m):
    case=m["DCP_historical_transport"]["case"]
    wanted=CASES[case]
    require(m["DCP_historical_transport"]==dict(RECEIPT,case=case),"exact transport scope")
    files={s["role"]:s for s in m["files"]}
    require(len(files)==wanted[-1]+4==len(m["files"]) and files["worker"]["path"]==files["generator"]["path"]==SOURCE
            and files["worker"]["sha256"]==files["generator"]["sha256"]==sha(Path(__file__).read_bytes()),
            "actually executing public adapter")
    for role,(path,digest) in OUTCOME.items():
        require(files[role]["path"]==path and files[role]["sha256"]==digest,"whole prior execution identity")
    old={k:v for k,v in m.items() if k!="DCP_historical_transport"}
    old["files"]=[dict(files["transport_original_"+s["role"]],role=s["role"]) if s["role"] in ("worker","generator") else s
                  for s in m["files"] if not s["role"].startswith("transport_")]
    require(len(old["files"])==wanted[-1] and sha(canonical(old))==wanted[0],
        "reconstruct the complete original manifest, including every original mathematical and operational role")
    return case,files,old


def definitions(root,files):
    sp=files["DCP_manifest"]
    require(sp["sha256"]==DCP,"original 322 DCP objects")
    d=json.loads(whole(root/sp["path"],DCP))
    current,history=d["files"],d["historical_inputs"]
    require(len(current)==269 and len(history)==53 and sha(canonical(current))==CUR and sha(canonical(history))==HIST,
            "both exact entire ordered descriptor objects")
    modes=Counter()
    for i,v in enumerate(history):
        base={"role","bytes","commit","encoding","git_blob_sha","path","sha256"}
        extra=set(v)-base
        require(base<=set(v) and v["role"]=="history%03d"%i and len(v["git_blob_sha"])==40
                and len(v["commit"])==40 and len(v["sha256"])==64 and v["bytes"]>0 and
                v["path"].startswith(TOPIC+"/") and ".." not in Path(v["path"]).parts,"original whole Git descriptor")
        if extra=={"restore_only"}:
            require(v["restore_only"] is True and v["encoding"]=="gzip-json","explicit restore-only whole Git JSON")
        elif extra=={"indices"}:
            require(v["encoding"]=="gzip-json" and len(v["indices"])==2,"original indexed whole row publication")
        else:
            require(not extra and v["encoding"] in ("gzip-npz","gzip-json","utf-8-json"),"original unflagged whole native Git object")
        modes[v["encoding"],tuple(sorted(extra))]+=1
    require(modes=={("gzip-json",("indices",)):40,("gzip-json",("restore_only",)):6,
        ("gzip-npz",()):5,("gzip-json",()):1,("utf-8-json",()):1},"all five original descriptor shapes")
    return current,history


def stage_dcp(shared,inputs,files,head,state):
    current,history=definitions(inputs,files)
    for seq,small in ((current,True),(history,False)):
        for v in seq:
            revision=head if small else v["commit"]
            if not small:
                shared["fetch_commit"](revision)
            payload,blob=shared["checked_bytes"](v,revision,small)
            require(len(payload)==v["bytes"] and sha(payload)==v["sha256"] and blob==v["git_blob_sha"]
                    and hashlib.sha1(b"blob "+str(len(payload)).encode()+b"\0"+payload).hexdigest()==blob,
                    "complete actual Git bytes in the original encoding")
            path=inputs/v["path"]
            if path.exists():
                require(path.read_bytes()==payload,"two materializations of a shared original input must agree")
            else:
                shared["atomic"](path,payload)
    state["whole_DCP_original_closure"]={"manifest":DCP,"current":269,"historical":53,
        "complete_ordered_descriptors_sha256":sha(canonical(current+history))}


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self,*args):
        return None


def terminal():
    base="https://api.github.com/repos/Rogerhu12/math-research-public/actions/"
    opener=build_opener(NoRedirect())
    headers={"Accept":"application/vnd.github+json","User-Agent":"verified-DCP-parent"}
    if os.getenv("GITHUB_TOKEN"):
        headers["Authorization"]="Bearer "+os.environ["GITHUB_TOKEN"]
    def read(url):
        with opener.open(Request(base+url,headers=headers),timeout=30) as response:
            return json.load(response)
    r=read("runs/"+str(RUN)+"/attempts/1")
    j=read("jobs/"+str(JOB))
    require(r["id"]==j["run_id"]==RUN and j["id"]==JOB and j["name"]=="signed-coordinates"
            and r["repository"]["full_name"]=="Rogerhu12/math-research-public"
            and all(x["run_attempt"]==1 and x["status"]=="completed" and x["conclusion"]=="failure"
                    and x["head_sha"]==EVENT for x in (r,j)),"the actual failed original attempt and job")
    return {"run":RUN,"job":JOB,"run_attempt":1,"head_sha":EVENT,"status":"completed","conclusion":"failure"}


def adapter(root,case,files):
    p=files["transport_original_worker"]
    o=load(root/p["path"],p["sha256"])
    if case=="ASQ25":
        original=root/o.OLD
        tree=o.adapter(original.read_bytes())
        old=load(original,o.OLD_SHA)
    else:
        tree,o25,original=o.adapter(root)
        old=load(original,o25.OLD_SHA)
    fn,=tree.body
    current,=[n for n in fn.body if isinstance(n,ast.FunctionDef) and n.name=="current"]
    require(ast.unparse(current.body[-1])=="stage_dcp(shared, inputs, files, head, state)","only the original history staging callback")
    current.body.extend(ast.parse('zero_parent(inputs)\nstate.setdefault("terminal_failed_parent_checks",[]).append(terminal())').body)
    last,=[n for n in fn.body if isinstance(n,ast.Try) and any(isinstance(s,ast.Assign) and
            isinstance(s.targets[0],ast.Name) and s.targets[0].id=="complete_small" for s in n.finalbody)]
    ix,=[i for i,s in enumerate(last.finalbody) if isinstance(s,ast.Assign) and isinstance(s.targets[0],ast.Name)
         and s.targets[0].id=="complete_small"]
    last.finalbody[ix:ix]=ast.parse('''try:
    state["terminal_failed_parent_after"]=terminal()
except Exception as terminal_error:
    state["complete"]=False
    state["terminal_parent_error"]={"type":type(terminal_error).__name__,"message":str(terminal_error)}
    if state["failure"] is None:
        state["failure"]=dict(state["terminal_parent_error"],traceback=traceback.format_exc())''').body
    return ast.fix_missing_locations(tree),dict(vars(old),__file__=__file__,SOURCE=SOURCE,stage_dcp=stage_dcp,
                                               zero_parent=zero_parent,terminal=terminal)


def build(root,case,original_file,workflow_file):
    oldsha,wfsha,oldwf,oldman,n=CASES[case]
    base=json.loads(whole(original_file,oldsha))
    wf=whole(workflow_file,wfsha).decode()
    zero_parent(root)
    def spec(role,path):
        b=(root/path).read_bytes()
        require(0<len(b)<100000,"whole small operational source")
        return dict(role=role,path=path,bytes=len(b),sha256=sha(b),encoding="utf-8",
                    git_blob_sha=hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest())
    entries=[]
    extra=[]
    for s in base["files"]:
        require(s==spec(s["role"],s["path"]),"all complete original rows including their original SHA and Git blob")
        if s["role"] in ("worker","generator"):
            extra.append(dict(s,role="transport_original_"+s["role"]))
            entries.append(spec(s["role"],SOURCE))
        else:
            entries.append(s)
    extra += [spec(r,p) for r,(p,h) in OUTCOME.items()]
    m=dict(base,files=entries+extra,DCP_historical_transport=dict(RECEIPT,case=case))
    _,f,_=checked_original(m)
    definitions(root,f)
    tree,_=adapter(root,case,f)
    compile(tree,"<complete original transport and failed zero-child gate>","exec")
    rr=json.loads((root/m["reviewed_rules"]["path"]).read_bytes())
    require(rr["model"]=="gpt-6.2-astra" and rr["reasoning_effort"]=="ultra" and
            all(sha((root/k).read_bytes())==d for k,d in rr["readme_sha256"].items()),"both whole current reviewed rules")
    newman=oldman[:-5]+"-historical-transport.json"
    newwf=oldwf[:-4]+"-historical-transport.yml"
    body=canonical(m)
    sparse=sorted({s["path"] for s in m["files"]}|{"README.md",TOPIC+"/README.md",newman})
    start=wf.index("          sparse-checkout: |\n")+len("          sparse-checkout: |\n")
    end=wf.index("      - name: Trust the original mounted checkout\n",start)
    wf=wf[:start]+"".join("            /"+s+"\n" for s in sparse)+wf[end:]
    for a,b in [(oldwf,newwf),("--manifest "+oldman,"--manifest "+newman),
                ("--manifest-sha "+oldsha,"--manifest-sha "+sha(body)),
                ("python "+f["transport_original_worker"]["path"],"python "+SOURCE)]:
        require(wf.count(a)==1,"exact original workflow substitution: "+a)
        wf=wf.replace(a,b)
    require(not any(k in sys.modules for k in ("numpy","flint","scipy")),"metadata-only admission")
    return body,wf.encode(),newman,newwf


def main():
    parser=argparse.ArgumentParser(add_help=False)
    parser.add_argument("--repo",required=True,type=Path)
    parser.add_argument("--prepare",choices=sorted(CASES))
    for k in ("original","original-workflow","output","workflow-output","manifest"):
        parser.add_argument("--"+k,type=Path)
    parser.add_argument("--manifest-sha")
    a,_=parser.parse_known_args()
    root=a.repo.resolve()
    if a.prepare:
        b,w,m,y=build(root,a.prepare,a.original,a.original_workflow)
        for p,data in ((a.output,b),(a.workflow_output,w)):
            with p.open("xb") as stream:
                stream.write(data)
        print(json.dumps(dict(manifest=m,workflow=y,manifest_sha256=sha(b),workflow_sha256=sha(w),new_science=0)))
        return
    manifest=json.loads(whole(root/a.manifest,a.manifest_sha))
    case,files,_=checked_original(manifest)
    tree,scope=adapter(root,case,files)
    exec(compile(tree,"<actual historical transport "+case+">","exec"),scope)
    scope["main"]()


if __name__=="__main__":
    sys.dont_write_bytecode=True
    main()
