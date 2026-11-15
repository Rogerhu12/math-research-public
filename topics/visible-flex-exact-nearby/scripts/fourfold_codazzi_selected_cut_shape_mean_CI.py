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
import urllib.error,urllib.request

PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
SCI=TOPIC/"scripts/fourfold_codazzi_selected_cut_shape_mean.py"
WORKER=TOPIC/"scripts/fourfold_codazzi_selected_cut_shape_mean_CI.py"
FOLDER=TOPIC/"notes/selected_cut_shape_mean_ci"
KIND="actual_public_selected_cut_shape_mean_process_v1"
SCIENTIFIC_KIND="actual_complete_selected_cut_shape_mean_scalar_conclusion_v1"
SCI_SHA="745fc480b101dbd7ca035c11826d2d0208c4d2db3568e0bbb4214fa401ddbb19"
HISTORY="7c130fb94528de8f003a43e7049fb42768a64eec"
RULES_SHA="65503a41254348a301fd71657ea61e5c32aa2d0bf7c980967b9ae35022a6b1d1"
README={
 "README.md":"6979d793d8335488df16d92c5617c6e5f25503187d5c27f22041eb8a027dbec9",
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

def topic_tree_metadata(git,topic,repository):
    """Read the exact published origin/main tree; never request an unpublished local HEAD or a blob body."""
    head=git("rev-parse","origin/main").stdout.strip()
    def oid(value):
        return isinstance(value,str) and len(value)==40 and all(c in "0123456789abcdef" for c in value)
    if not oid(head):raise ValueError("the capacity audit requires an exact Git commit")
    root_tree=git("rev-parse",head+"^{tree}").stdout.strip()
    local_topic_tree=git("rev-parse",head+":"+str(topic)).stdout.strip()
    if not oid(root_tree) or not oid(local_topic_tree):
        raise ValueError("the capacity audit requires complete local commit and tree identities")
    token=os.environ.get("GITHUB_TOKEN")
    if not token:raise RuntimeError("the public metadata request requires its Actions token")
    responses=[]
    class NoMetadataRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self,request,fp,code,message,headers,newurl):
            raise RuntimeError("the capacity metadata endpoint attempted a redirect")
    opener=urllib.request.build_opener(NoMetadataRedirect())
    def request_tree(tree,recursive=False):
        url="https://api.github.com/repos/"+repository+"/git/trees/"+tree
        if recursive:url+="?recursive=1"
        request=urllib.request.Request(url,headers={
            "Accept":"application/vnd.github+json",
            "X-GitHub-Api-Version":"2022-11-28",
            "Authorization":"Bearer "+token})
        try:
            with opener.open(request,timeout=45) as response:
                if response.geturl()!=url:
                    raise RuntimeError("the capacity metadata request was redirected")
                data=response.read(16000001)
        except urllib.error.HTTPError as error:
            raise RuntimeError("the Git tree metadata request returned HTTP "+str(error.code)) from None
        except urllib.error.URLError:
            raise RuntimeError("the Git tree metadata request failed at transport") from None
        if len(data)>16000000:raise ValueError("the Git tree metadata response exceeded its bounded size")
        doc=json.loads(data)
        if doc.get("sha")!=tree or doc.get("truncated") is not False or not isinstance(doc.get("tree"),list):
            raise ValueError("a Git tree metadata identity or complete-response gate failed")
        responses.append(dict(tree=tree,recursive=recursive,bytes=len(data),
            sha256=hashlib.sha256(data).hexdigest(),truncated=False))
        return doc["tree"]
    # Freeze the public origin/main commit before resolving its topic components.
    # Compare with Git's independent commit:topic identity; API URLs contain only exact object IDs.
    tree=root_tree
    for component in topic.parts:
        entries=request_tree(tree)
        matches=[entry for entry in entries if entry.get("path")==component]
        if len(matches)!=1 or matches[0].get("type")!="tree" or matches[0].get("mode")!="040000":
            raise ValueError("the authorized topic is not an exact tree at this commit")
        tree=matches[0].get("sha")
        if not oid(tree):raise ValueError("the topic path contains an invalid Git tree identity")
    if tree!=local_topic_tree:
        raise ValueError("the API and local published-commit topic tree identities differ")
    entries=request_tree(tree,recursive=True)
    seen=set();blobs={};inventory=[];trees=0;gitlinks=0
    for entry in entries:
        path=entry.get("path")
        if (not isinstance(path,str) or not path or path.startswith("/")
            or any(part in ("",".","..") for part in path.split("/")) or path in seen):
            raise ValueError("the complete topic tree contains an invalid or duplicate path")
        seen.add(path)
        kind=entry.get("type");mode=entry.get("mode");digest=entry.get("sha")
        if not oid(digest):raise ValueError("a topic object has an invalid Git identity")
        if kind=="blob":
            size=entry.get("size")
            if type(size) is not int or size<0 or mode not in ("100644","100755","120000"):
                raise ValueError("a topic blob has no exact nonnegative metadata size or valid mode")
            full=str(topic)+"/"+path
            blobs[full]=dict(bytes=size,git_blob=digest,mode=mode)
            inventory.append(dict(path=full,bytes=size,git_blob=digest,mode=mode))
        elif kind=="tree":
            if mode!="040000":raise ValueError("a nested topic tree has the wrong mode")
            trees+=1
        elif kind=="commit":
            if mode!="160000":raise ValueError("a topic Git link has the wrong mode")
            gitlinks+=1
        else:raise ValueError("the complete topic tree has an unsupported entry type")
    inventory.sort(key=lambda entry:entry["path"])
    receipt=dict(method="published_origin_main_Git_Trees_API_metadata_only",commit=head,
        root_tree=root_tree,topic=str(topic),topic_tree=tree,
        truncated=False,all_blob_sizes_checked=True,blob_count=len(blobs),
        blob_bytes=sum(entry["bytes"] for entry in blobs.values()),
        nested_tree_count=trees,gitlink_count=gitlinks,
        complete_blob_metadata_inventory_sha256=hashlib.sha256(
            json.dumps(inventory,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest(),
        metadata_responses=responses,blob_bodies_requested=False)
    return receipt,blobs


class Worker:
    def __init__(self,a):
        self.a=a;self.repo=a.repo.resolve();self.work=a.work.resolve()
        self.work.mkdir(parents=True,exist_ok=True)
        self.science=self.work/"immutable-science";self.science.mkdir(exist_ok=True)
        self.rid=os.environ.get("GITHUB_RUN_ID","");self.attempt=os.environ.get("GITHUB_RUN_ATTEMPT","")
        if not self.rid.isdigit() or not self.attempt.isdigit():
            raise ValueError("the public Actions run and attempt are required")
        self.dest=self.repo/FOLDER/f"run-{self.rid}-{self.attempt}-selected-cut-shape-mean"
        self.tempout=self.work/"new-temporary-cut-shape-signed-audit.json"
        self.tempsummary=self.work/"actual-cut-shape-mean-conclusion.json"
        self.started=time.monotonic();self.stop=False;self.child=None;self.last_checkpoint=time.monotonic()
        self.state={"kind":KIND,"complete":False,"repository":PUBLIC,
            "run_id":self.rid,"run_attempt":self.attempt,"started_utc":now(),
            "workflow_commit":os.environ.get("GITHUB_SHA"),"worker_source_sha256":digest(__file__),
            "actual_source_sha256":SCI_SHA,"input_manifest_sha256":a.manifest_sha,
            "children":[],"readme_checks":[],"published_checkpoints":[],
            "original_targets_residual_enclosures_reference_ODE_and_primitive_recomputed":0,
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
            "separately_read_rules_commit":"2f72b274f8647dbf6ce236ff2185cbe22153f8e1"})
        self.state["last_read_commit"]=after
        if not hasattr(self,"scientific_commit"):self.scientific_commit=after
        if any(hbytes(new[p])!=expected for p,expected in README.items()):
            raise RuntimeError("new unread repository rules need their actual diff read")
        self.last_checkpoint=time.monotonic()

    def hydrate(self):
        mp=self.repo/relative(self.a.manifest);rp=self.repo/relative(self.a.rules)
        if digest(mp)!=self.a.manifest_sha or digest(rp)!=RULES_SHA:
            raise ValueError("the exact source manifest or reviewed rules changed")
        m=read(mp);rules=read(rp)
        if (m["kind"]!="selected_cut_shape_mean_public_inputs_v1"
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
                if text in allowed:
                    commit=HISTORY;origin="exact_public_history"
                elif text in m["current_only_paths"]:
                    commit=self.scientific_commit;origin="exact_immutable_current_commit"
                else:raise ValueError("an input is neither current science nor original history: "+text)
                raw=git_bytes(self.repo,"show",commit+":"+text)
                if hbytes(raw)!=expected:raise ValueError("exact input file SHA mismatch: "+text)
                target.write_bytes(raw)
            if digest(target)!=expected:raise ValueError("frozen input differs: "+text)
            receipts.append({"path":text,"sha256":expected,"bytes":target.stat().st_size,"source":origin})
        for path in (self.science/SCI,self.science/WORKER):
            ast.parse(path.read_text(),filename=str(path))
        if digest(self.science/SCI)!=SCI_SHA:raise ValueError("the frozen science source changed")
        versions={"python-flint":importlib.metadata.version("python-flint")}
        if versions!={"python-flint":"0.9.0"} or sys.version.split()[0]!="3.12.14":
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
            and s.get("actual_new_scalar_coefficient_consumption_complete") is True
            and s.get("all_193_raw_amplitudes_used_before_absolute_values") is True
            and s.get("known_base32_shape_subtracted_before_norm") is True
            and s.get("old_target_trial_angle_repair_matrix_Green_recomputations")==0
            and s.get("no_core_existence_unknown_correction_or_low_selfmap_claim") is True
            and s.get("input_sha256",{}).get("manifest")==self.a.manifest_sha)

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
            sp=pp.parent/"actual-cut-shape-mean-conclusion.json"
            if not sp.is_file():continue
            s=read(sp)
            child0=any(c.get("label")=="selected_cut_shape_mean"
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
            self.state["actual_output_sha256"]=s.get("temporary_complete_signed_audit",{}).get("sha256")
            self.state["actual_output_bytes"]=s.get("temporary_complete_signed_audit",{}).get("bytes")
            self.state["actual_remaining_low_gamma_budget_proved"]=s.get("conditional_low_gamma_entry",{}).get("positive_remaining_low_gamma_budget_proved")
            self.state["core_existence_or_low_gamma_selfmap_claimed"]=False
            self.state["actual_scientific_gates"]=s.get("gates")
            self.state["actual_scientific_complete"]=s.get("complete")
            self.state["actual_scientific_failure"]=s.get("failure")
        self.state["snapshot_utc"]=now()
        self.state["wall_seconds"]=time.monotonic()-self.started

    def emit_scientific_receipt(self):
        """Emit the complete small actual conclusion before any terminal Git publication."""
        if not self.tempsummary.exists():return
        s=read(self.tempsummary)
        if s.get("source_sha256")!=SCI_SHA or s.get("parameters")!=self.manifest["parameters"]:
            raise ValueError("the stdout scientific receipt has the wrong mathematical identity")
        children=self.state.get("children",[])
        outcome=children[-1].get("actual_returncode") if children else None
        if self.state.get("complete_original_conclusion_reused_without_new_child"):
            outcome=0
        payload=dict(kind="complete_small_selected_cut_shape_mean_stdout_receipt_v1",
            repository=PUBLIC,run_id=self.rid,run_attempt=self.attempt,
            source_sha256=SCI_SHA,worker_source_sha256=digest(__file__),
            input_manifest_sha256=self.a.manifest_sha,
            actual_returncode=outcome,
            scientific_conclusion_bytes=self.tempsummary.stat().st_size,
            scientific_conclusion_sha256=digest(self.tempsummary),
            complete_original_conclusion_reused_without_new_child=bool(
                self.state.get("complete_original_conclusion_reused_without_new_child")),
            original_success_process_sha256=self.state.get("original_success_process_sha256"),
            original_success_summary_sha256=self.state.get("original_success_summary_sha256"),
            actual_scientific_receipt=s)
        raw=(json.dumps(payload,ensure_ascii=False,sort_keys=True,
                        separators=(",",":"),allow_nan=False)+"\n").encode()
        if len(raw)>59000:
            raise ValueError("the complete scientific stdout receipt exceeds 59000 UTF8 bytes")
        self.state["prepublication_scientific_stdout_receipt"]=dict(
            bytes=len(raw),sha256=hbytes(raw),complete_conclusion_included=True,
            emitted_before_terminal_publication=True)
        print("COMPLETE_SCIENTIFIC_RECEIPT "+json.dumps(
            self.state["prepublication_scientific_stdout_receipt"],sort_keys=True),flush=True)
        print(raw.decode(),end="",flush=True)

    def publish(self,final=False):
        self.capture()
        self.emit_scientific_receipt()
        attempt=0
        while True:
            attempt+=1
            self.sync()
            self.dest.mkdir(parents=True,exist_ok=True)
            def metagit(*args):
                return run(["git",*args],self.repo,stdout=subprocess.PIPE,text=True)
            capacity,blobs=topic_tree_metadata(metagit,TOPIC,PUBLIC)
            self.state["published_topic_capacity_metadata"]=capacity
            if capacity["blob_bytes"]>=200000000:
                raise ValueError("the current topic exceeds the actual 200 MB limit")
            if self.tempsummary.exists():
                raw=self.tempsummary.read_bytes()
                if len(raw)>60000:raise ValueError("no artificially split full output may be published")
                (self.dest/"actual-cut-shape-mean-conclusion.json").write_bytes(raw)
            self.state["publication_is_final_attempt"]=bool(final)
            small(self.dest/"process.json",self.state)
            paths=[str((self.dest/"process.json").relative_to(self.repo))]
            if (self.dest/"actual-cut-shape-mean-conclusion.json").exists():
                paths.append(str((self.dest/"actual-cut-shape-mean-conclusion.json").relative_to(self.repo)))
            addition=sum((self.repo/p).stat().st_size-blobs.get(p,{}).get("bytes",0) for p in paths)
            if capacity["blob_bytes"]+addition+4096>200000000:
                raise ValueError("publishing this small actual conclusion would exceed the topic limit")
            if not self.state["children"] and not self.tempsummary.exists():
                if capacity["blob_bytes"]+addition+4096+120000>200000000:
                    raise ValueError("the initial publication cannot reserve 120000 bytes for complete small conclusions")
                self.state["pre_math_small_conclusion_capacity_reserve_bytes"]=120000
                self.state["pre_math_topic_bytes_with_reserve_upper"]=capacity["blob_bytes"]+addition+4096+120000
            self.state["projected_topic_bytes_upper"]=capacity["blob_bytes"]+addition+4096
            small(self.dest/"process.json",self.state)
            run(["git","add","--",*paths],self.repo)
            changed=subprocess.run(["git","diff","--cached","--quiet"],cwd=self.repo).returncode
            if changed:
                run(["git","commit","-m",f"Record actual cut shape/mean scalars run {self.rid} actual small conclusion"],self.repo)
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
        ip=self.manifest["input_paths"]
        cmd=[sys.executable,"-u",str(self.science/SCI),
             "--manifest",str(self.science/relative(self.a.manifest)),
             "--manifest-sha",self.a.manifest_sha,
             "--boundary",str(self.science/relative(ip["boundary"])),
             "--boundary-process",str(self.science/relative(ip["boundary_process"])),
             "--base-cut",str(self.science/relative(ip["base_cut"])),
             "--temporary-audit",str(self.tempout),"--out",str(self.tempsummary)]

        log=self.work/"actual-science.log"
        entry={"label":"selected_cut_shape_mean",
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
            raise RuntimeError("actual public cut shape/mean scalar mathematics returned a nonzero code")
        if not self.tempsummary.exists() or not self.summary_valid(read(self.tempsummary)):
            raise ValueError("the complete true scientific conclusion did not pass its exact scope")
        self.state["complete"]=True

    def run(self):
        run(["git","config","user.name","github-actions[bot]"],self.repo)
        run(["git","config","user.email","41898282+github-actions[bot]@users.noreply.github.com"],self.repo)
        status=0
        try:
            self.sync();self.hydrate();old=self.previous()
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
