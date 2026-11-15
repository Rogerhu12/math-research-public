#!/usr/bin/env python3
"""Public, temporary-only original-row consumption with small actual receipts."""
from __future__ import annotations
import argparse
import ast
import base64
from datetime import datetime,timezone
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import time
import traceback
import urllib.request

PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
SCI=TOPIC/"scripts/fourfold_codazzi_cached_weighted_cap_Q.py"
WORKER=TOPIC/"scripts/fourfold_codazzi_cached_weighted_cap_Q_CI.py"
FOLDER=TOPIC/"notes/cached_weighted_cap_Q_ci"
KIND="actual_public_cached_weighted_cap_Q_process_v1"
SCIENTIFIC_KIND="actual_cached_weighted_cap_Q_joint_gate_v1"
SCI_SHA="1be4b1115380c722a09c504e2fea99f6e32d3e0b12c8e92f44b1aa50ee27de16"
HISTORY="7c130fb94528de8f003a43e7049fb42768a64eec"
RULES_SHA="f2661bd5cf5cb006c1f78c64126b3ac065e6bc26a50790545ac443efb5e372bd"
README={
 "README.md":"c6db597c32b022d46d861463e32ad7160545e088610916339bd47e1acae74970",
 "topics/visible-flex-exact-nearby/README.md":"81249053c4c14a7a14289b58184e1b81601146d412fa117973f7a1d05bf95220"}

def now():return datetime.now(timezone.utc).isoformat()
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def hbytes(x):return hashlib.sha256(x).hexdigest()
def read(p):return json.loads(Path(p).read_bytes())
def small(p,v):
    raw=(json.dumps(v,indent=2,allow_nan=False)+"\n").encode()
    if len(raw)>60000:raise ValueError("genuine small metadata exceeds60000 UTF8 bytes")
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    q=p.with_name(p.name+".tmp");q.write_bytes(raw);q.replace(p)
def relative(p):
    q=Path(p)
    if q.is_absolute() or ".." in q.parts:raise ValueError("unsafe repository path")
    return q
def git_env():
    env=os.environ.copy()
    token=env.get("GITHUB_TOKEN")
    if not token:raise ValueError("the authorized ephemeral workflow token is required")
    count=int(env.get("GIT_CONFIG_COUNT","0"))
    env["GIT_CONFIG_COUNT"]=str(count+1)
    env["GIT_CONFIG_KEY_"+str(count)]="http.https://github.com/.extraheader"
    encoded=base64.b64encode(("x-access-token:"+token).encode()).decode()
    env["GIT_CONFIG_VALUE_"+str(count)]="AUTHORIZATION: basic "+encoded
    env["GIT_TERMINAL_PROMPT"]="0"
    return env
def run(command,repo,**kw):
    if command[0]=="git":kw["env"]=git_env()
    return subprocess.run(command,cwd=repo,check=True,**kw)
def git_bytes(repo,*args):return run(["git",*args],repo,stdout=subprocess.PIPE).stdout

class Worker:
    def __init__(self,a):
        self.a=a;self.repo=a.repo.resolve();self.work=a.work.resolve()
        self.work.mkdir(parents=True,exist_ok=True)
        self.science=self.work/"immutable-science";self.science.mkdir(exist_ok=True)
        self.rid=os.environ.get("GITHUB_RUN_ID","");self.attempt=os.environ.get("GITHUB_RUN_ATTEMPT","")
        if not self.rid.isdigit() or not self.attempt.isdigit():
            raise ValueError("the public Actions run and attempt are required")
        self.dest=self.repo/FOLDER/f"run-{self.rid}-{self.attempt}-cached-weighted-cap-Q"
        self.tempout=self.work/"new-temporary-weighted-cap-Q-output.json"
        self.tempsummary=self.work/"actual-weighted-cap-Q-summary.json"
        self.started=time.monotonic();self.stop=False;self.child=None;self.last_checkpoint=time.monotonic()
        self.state={"kind":KIND,"complete":False,"repository":PUBLIC,
            "run_id":self.rid,"run_attempt":self.attempt,"started_utc":now(),
            "workflow_commit":os.environ.get("GITHUB_SHA"),"worker_source_sha256":digest(__file__),
            "actual_source_sha256":SCI_SHA,"input_manifest_sha256":a.manifest_sha,
            "children":[],"readme_checks":[],"published_checkpoints":[],
            "old_target_and_full_coefficient_convolutions_recomputed":0,
            "old_L1_integrals_recomputed":0,"old_reference_Riccati_recomputed":0,
            "original_recomputable_inputs_only_in_temporary_storage":True,
            "new_recomputable_data_persisted":False,"new_Actions_artifacts":False,
            "new_Release_uploads":False,"complete_nonlinear_endpoint_invariance_proved":False,
            "complete_nonlinear_cap_solution_proved":False,"full_infinite_BVP_inverse_proved":False,
            "historical_restore_commit":HISTORY,"reviewed_rules_sha256":RULES_SHA}

    def sync(self):
        before=git_bytes(self.repo,"rev-parse","HEAD").decode().strip()
        old={p:git_bytes(self.repo,"show",before+":"+p) for p in README}
        # The workflow checks out public main. All local commits belong to this worker.
        branch=git_bytes(self.repo,"branch","--show-current").decode().strip()
        if branch!="main":raise ValueError("the publication checkout is not public main")
        p=subprocess.run(["git","pull","--rebase","origin","main"],cwd=self.repo,
                         stdout=subprocess.PIPE,stderr=subprocess.STDOUT,env=git_env())
        if p.returncode:
            self.state["failed_actual_pull"]={"utc":now(),"returncode":p.returncode,
                "output":p.stdout.decode(errors="replace")[-10000:]}
            raise RuntimeError("actual public git pull failed")
        after=git_bytes(self.repo,"rev-parse","HEAD").decode().strip()
        new={p:git_bytes(self.repo,"show",after+":"+p) for p in README}
        diff=git_bytes(self.repo,"diff",before,after,"--",*README).decode()
        self.state["readme_checks"].append({"time":now(),"before":before,"after":after,
            "changed":any(old[p]!=new[p] for p in README),"actual_diff":diff,
            "actual_sha256":{p:hbytes(x) for p,x in new.items()},
            "separately_read_rules_commit":"137c5a877fb387a82cbde01f084d1fa67ee717aa"})
        self.state["last_read_commit"]=after
        if any(hbytes(new[p])!=expected for p,expected in README.items()):
            raise RuntimeError("new unread repository rules need their actual diff read")
        self.last_checkpoint=time.monotonic()

    def topic_metadata_size(self):
        """Only tree metadata; no blob-size lookup that can lazily fetch file bodies."""
        commit=git_bytes(self.repo,"rev-parse","HEAD").decode().strip()
        tree=git_bytes(self.repo,"rev-parse",commit+":"+str(TOPIC)).decode().strip()
        self.state["topic_size_metadata"]={"commit":commit,"topic_tree":tree,"utc":now(),
            "metadata_only":True,"blob_contents_read":False,"limit_bytes":200000000}
        base="https://api.github.com/repos/"+PUBLIC+"/git/trees/"
        token=os.environ.get("GITHUB_TOKEN")
        def get_tree(sha,recursive=False):
            if len(sha)!=40 or any(c not in "0123456789abcdef" for c in sha):
                raise ValueError("a tree identity is not a full public Git SHA")
            request=urllib.request.Request(base+sha+("?recursive=1" if recursive else ""),
                headers={"Authorization":"Bearer "+token,"Accept":"application/vnd.github+json",
                         "X-GitHub-Api-Version":"2022-11-28","User-Agent":"visible-exact-metadata-size"})
            with urllib.request.urlopen(request,timeout=90) as response:
                data=json.load(response)
            if data.get("sha")!=sha:raise ValueError("tree metadata returned a different object")
            return data
        data=get_tree(tree,True);entries=[]
        if data.get("truncated"):
            pending=[("",tree)]
            while pending:
                prefix,ident=pending.pop()
                current=get_tree(ident)
                if current.get("truncated"):raise ValueError("nonrecursive topic tree metadata is truncated")
                for row in current["tree"]:
                    rel=prefix+row["path"]
                    if row["type"]=="tree":pending.append((rel+"/",row["sha"]))
                    else:entries.append(dict(row,path=rel))
        else:
            entries=[r for r in data["tree"] if r["type"]!="tree"]
        by_path={}
        for row in entries:
            path=str(TOPIC)+"/"+row["path"]
            relative(path)
            if (path in by_path or row["type"]!="blob" or not isinstance(row.get("size"),int)
                or row["size"]<0):
                raise ValueError("topic tree contains a duplicate, unsupported object or missing exact size")
            by_path[path]={"sha":row["sha"],"bytes":row["size"],"mode":row["mode"]}
        # This command reads only tree identities. In a partial clone, -l may
        # fetch missing blobs to discover sizes, so sizes above come from the API.
        raw=git_bytes(self.repo,"ls-tree","-r","-z",commit,"--",str(TOPIC))
        local={}
        for record in raw.split(b"\0"):
            if not record:continue
            head,path=record.split(b"\t",1)
            mode,kind,ident=head.decode().split()
            if kind!="blob":raise ValueError("topic metadata has a non-blob leaf")
            local[path.decode()]={"sha":ident,"mode":mode}
        if (set(local)!=set(by_path)
            or any(local[p]!={k:by_path[p][k] for k in ("sha","mode")} for p in local)):
            raise ValueError("Git and GitHub topic tree path/SHA metadata differ")
        total=sum(r["bytes"] for r in by_path.values())
        receipt=self.state["topic_size_metadata"]
        receipt.update(file_count=len(by_path),total_bytes=total,remaining_bytes=200000000-total,
            exact_tree_entries_sha256=hbytes(json.dumps(by_path,sort_keys=True,separators=(",",":")).encode()),
            git_path_sha_set_verified=True,within_limit=total<=200000000)
        if total>200000000:
            raise ValueError("current topic exceeds the200000000-byte main limit; no mathematics started")

    def hydrate(self):
        mp=self.repo/relative(self.a.manifest);rp=self.repo/relative(self.a.rules)
        if digest(mp)!=self.a.manifest_sha or digest(rp)!=RULES_SHA:
            raise ValueError("the exact source manifest or reviewed rules changed")
        m=read(mp);rules=read(rp)
        if (m["kind"]!="cached_weighted_cap_Q_public_inputs_v1"
            or m["historical_restore_commit"]!=HISTORY or m["readme_sha256"]!=README
            or rules["readme_sha256"]!=README or m["source_sha256"]!=SCI_SHA
            or m["files"].get(str(WORKER))!=digest(__file__)):
            raise ValueError("the new consumer identity or rules do not match")
        self.manifest=m;receipts=[]
        present=subprocess.run(["git","cat-file","-e",HISTORY+"^{commit}"],cwd=self.repo,
            stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode==0
        if not present:
            run(["git","fetch","--filter=blob:none","--no-tags","--depth=1","origin",HISTORY],self.repo)
        allowed=set(m["historical_input_paths"])
        for text,expected in sorted(m["files"].items()):
            rel=relative(text);source=self.repo/rel;target=self.science/rel
            target.parent.mkdir(parents=True,exist_ok=True)
            if source.is_file() and digest(source)==expected:
                shutil.copyfile(source,target);origin="exact_current_file"
            else:
                if text not in allowed:raise ValueError("a new immutable source is not present: "+text)
                raw=git_bytes(self.repo,"show",HISTORY+":"+text)
                if hbytes(raw)!=expected:raise ValueError("historical original file SHA mismatch: "+text)
                target.write_bytes(raw);origin="exact_public_history"
            if digest(target)!=expected:raise ValueError("frozen input differs: "+text)
            receipts.append({"path":text,"sha256":expected,"bytes":target.stat().st_size,"source":origin})
        for path in (self.science/SCI,self.science/WORKER):
            ast.parse(path.read_text(),filename=str(path))
        if digest(self.science/SCI)!=SCI_SHA:raise ValueError("the frozen science source changed")
        versions={name:importlib.metadata.version(name) for name in ("python-flint","numpy")}
        if versions!={"python-flint":"0.9.0","numpy":"2.3.5"} or sys.version.split()[0]!="3.12.14":
            raise ValueError("the exact directed-arithmetic runtime changed")
        self.state.update(package_versions=versions,python_version=sys.version,
            historical_hydration={"files":len(receipts),
                "historical_files":sum(x["source"]=="exact_public_history" for x in receipts),
                "full_temporary_receipt_sha256":hbytes(json.dumps(receipts,sort_keys=True).encode()),
                "restored_into_checkout":False,"old_mathematics_executed":False},
            actual_original_input_receipts=receipts,
            all_pinned_inputs_verified=True,
            actual_parameters=m["parameters"])
        small(self.work/"original-hydration-receipt.json",{"files":receipts})
        shutil.copyfile(mp,self.science/relative(self.a.manifest))
        self.state["immutable_scientific_copy"]=str(self.science)

    def summary_valid(self,s):
        return (s.get("kind")==SCIENTIFIC_KIND and s.get("source_sha256")==SCI_SHA
            and s.get("parameters")==self.manifest["parameters"] and s.get("complete") is True
            and s.get("failure") is None and bool(s.get("gates"))
            and all(g.get("passed") is True for g in s["gates"])
            and s.get("original_complete_positive_rows")==4650
            and s.get("original_reference_rows")==949
            and s.get("original_reference_closed_intersections")==1346
            and s.get("candidate_original_shards_read")==1
            and s.get("candidate_scalar_component_newly_enclosed")==32
            and s.get("new_scalar_mean_Bernstein_domains")==s.get("complete_common_cap_cells")
            and s.get("complete_common_cap_cells",0)>0
            and s.get("old_target_and_full_coefficient_convolutions_recomputed")==0
            and s.get("old_L1_integrals_recomputed")==0 and s.get("old_reference_Riccati_recomputed")==0
            and s.get("scope",{}).get("complete_nonlinear_endpoint_invariance_proved") is False)

    def previous(self):
        root=self.repo/FOLDER
        if not root.exists():return None
        found=[]
        for pp in sorted(root.glob("*/process.json")):
            if pp.parent==self.dest:continue
            p=read(pp)
            if (p.get("kind")!=KIND or p.get("repository")!=PUBLIC
                or p.get("actual_source_sha256")!=SCI_SHA
                or p.get("input_manifest_sha256")!=self.a.manifest_sha):continue
            if any(c.get("actual_returncode") not in (None,0) for c in p.get("children",[])):
                raise RuntimeError("the same mathematical source already failed; preserve it until a correction")
            sp=pp.parent/"actual-weighted-cap-Q-summary.json"
            if not sp.is_file():continue
            s=read(sp)
            child0=any(c.get("label")=="cached_weighted_cap_Q_joint_gate"
                       and c.get("actual_returncode")==0 for c in p.get("children",[]))
            reused=p.get("complete_original_conclusion_reused_without_new_child") and p.get("original_success_process_sha256")
            if self.summary_valid(s) and (child0 or reused):
                expected=p.get("actual_scientific_summary_sha256")
                if expected and digest(sp)!=expected:raise ValueError("old actual conclusion bytes changed")
                found.append((pp,sp))
        return found[0] if found else None

    def capture(self):
        if self.tempsummary.exists():
            s=read(self.tempsummary)
            if s.get("source_sha256")!=SCI_SHA or s.get("parameters")!=self.manifest["parameters"]:
                raise ValueError("actual new summary has a different mathematical identity")
            self.state["actual_scientific_summary_sha256"]=digest(self.tempsummary)
            self.state["actual_scientific_summary_bytes"]=self.tempsummary.stat().st_size
            self.state["actual_output_sha256"]=s.get("temporary_full_output_sha256")
            self.state["actual_output_bytes"]=s.get("temporary_full_output_bytes")
            self.state["actual_scientific_gates"]=s.get("gates")
            self.state["actual_scientific_complete"]=s.get("complete")
            self.state["actual_scientific_failure"]=s.get("failure")
        self.state["snapshot_utc"]=now()
        self.state["wall_seconds"]=time.monotonic()-self.started

    def publish(self,final=False):
        self.capture()
        attempt=0
        while True:
            attempt+=1
            self.sync()
            self.dest.mkdir(parents=True,exist_ok=True)
            if self.tempsummary.exists():
                raw=self.tempsummary.read_bytes()
                if len(raw)>60000:raise ValueError("no artificially split full output may be published")
                (self.dest/"actual-weighted-cap-Q-summary.json").write_bytes(raw)
            self.state["publication_is_final_attempt"]=bool(final)
            small(self.dest/"process.json",self.state)
            paths=[str((self.dest/"process.json").relative_to(self.repo))]
            if (self.dest/"actual-weighted-cap-Q-summary.json").exists():
                paths.append(str((self.dest/"actual-weighted-cap-Q-summary.json").relative_to(self.repo)))
            run(["git","add","--",*paths],self.repo)
            changed=subprocess.run(["git","diff","--cached","--quiet"],cwd=self.repo).returncode
            if changed:
                run(["git","commit","-m",f"Record cached weighted cap Q run {self.rid} actual small conclusion"],self.repo)
            result=subprocess.run(["git","push","origin","HEAD:main"],cwd=self.repo,
                                  stdout=subprocess.PIPE,stderr=subprocess.STDOUT,env=git_env())
            if result.returncode==0:
                commit=git_bytes(self.repo,"rev-parse","HEAD").decode().strip()
                self.state["published_checkpoints"].append({"utc":now(),"commit":commit,"final":final})
                return
            # Pull and read both README differences before every non-FF retry.
            self.state["last_push_retry"]={"attempt":attempt,"utc":now(),
                "output":result.stdout.decode(errors="replace")[-3000:]}

    def compute(self):
        cmd=[sys.executable,"-u",str(self.science/SCI),"--root",str(self.science),
             "--out",str(self.tempout),"--summary",str(self.tempsummary)]
        log=self.work/"actual-science.log"
        entry={"label":"cached_weighted_cap_Q_joint_gate",
               "command":cmd,"started_utc":now(),"actual_returncode":None}
        self.state["children"].append(entry)
        started=time.monotonic();deadline=started+60*self.a.compute_minutes
        with log.open("wb") as out:
            self.child=subprocess.Popen(cmd,cwd=self.science/TOPIC,stdout=out,stderr=subprocess.STDOUT)
            while self.child.poll() is None:
                if self.stop or time.monotonic()>deadline:
                    self.child.terminate()
                    try:self.child.wait(timeout=30)
                    except subprocess.TimeoutExpired:self.child.kill();self.child.wait()
                    entry["termination_reason"]="actual_interrupt_or_explicit_math_deadline"
                    break
                if time.monotonic()-self.last_checkpoint>=600:self.publish()
                time.sleep(1)
            entry.update(actual_returncode=self.child.returncode,finished_utc=now(),
                actual_wall_seconds=time.monotonic()-started,
                temporary_log_bytes=log.stat().st_size,temporary_log_sha256=digest(log))
        self.child=None
        self.capture()
        if entry["actual_returncode"]!=0:
            entry["actual_log_tail"]=log.read_text(errors="replace")[-12000:]
            raise RuntimeError("actual public weighted cap Q mathematics returned a nonzero code")
        if not self.tempsummary.exists() or not self.summary_valid(read(self.tempsummary)):
            raise ValueError("the complete true scientific conclusion did not pass its exact scope")
        self.state["complete"]=True

    def run(self):
        run(["git","config","user.name","github-actions[bot]"],self.repo)
        run(["git","config","user.email","41898282+github-actions[bot]@users.noreply.github.com"],self.repo)
        status=0
        try:
            self.sync();self.topic_metadata_size();self.hydrate();old=self.previous()
            if old:
                pp,sp=old;shutil.copyfile(sp,self.tempsummary)
                self.state.update(complete=True,complete_original_conclusion_reused_without_new_child=True,
                    original_success_process_sha256=digest(pp),
                    original_success_summary_sha256=digest(sp),original_success_run=read(pp)["run_id"])
            else:
                self.publish()
                self.compute()
        except Exception as e:
            status=1
            self.state["failure"]={"type":type(e).__name__,"message":str(e),"traceback":traceback.format_exc()}
        try:self.publish(final=True)
        except Exception as e:
            status=1
            self.state["publication_failure"]={"type":type(e).__name__,"message":str(e)}
        self.capture()
        small(self.work/"final-small-process.json",self.state)
        print(json.dumps(self.state,indent=2,allow_nan=False),flush=True)
        if self.tempsummary.exists():print(self.tempsummary.read_text(),flush=True)
        return status

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo",type=Path,required=True);p.add_argument("--work",type=Path,required=True)
    p.add_argument("--manifest",required=True);p.add_argument("--manifest-sha",required=True)
    p.add_argument("--rules",required=True);p.add_argument("--compute-minutes",type=int,default=20)
    a=p.parse_args()
    if os.environ.get("GITHUB_REPOSITORY")!=PUBLIC or not 1<=a.compute_minutes<=60:
        raise ValueError("only the authorized public repository and bounded new consumer are permitted")
    w=Worker(a)
    for sig in (signal.SIGINT,signal.SIGTERM):signal.signal(sig,lambda *_:setattr(w,"stop",True))
    raise SystemExit(w.run())

if __name__=="__main__":main()
