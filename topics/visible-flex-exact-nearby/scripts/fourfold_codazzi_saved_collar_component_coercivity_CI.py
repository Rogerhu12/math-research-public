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
SCI=TOPIC/"scripts/fourfold_codazzi_saved_collar_component_coercivity.py"
WORKER=TOPIC/"scripts/fourfold_codazzi_saved_collar_component_coercivity_CI.py"
FOLDER=TOPIC/"notes/saved_positive_collar_components_ci"
KIND="actual_public_saved_positive_collar_components_process_v1"
SCIENTIFIC_KIND="actual_saved_positive_collar_components_and_high_coercivity_v1"
SCI_SHA="02fc50c45ed2610b94619d9db60ee2f74dc3a1643ce2f398c8eb25505926f7ea"
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
        self.dest=self.repo/FOLDER/f"run-{self.rid}-{self.attempt}-saved-positive-collar-components"
        self.tempsummary=self.work/"actual-saved-positive-collar-components.json"
        self.started=time.monotonic();self.stop=False;self.child=None;self.last_checkpoint=time.monotonic()
        self.state={"kind":KIND,"complete":False,"repository":PUBLIC,
            "run_id":self.rid,"run_attempt":self.attempt,"started_utc":now(),
            "workflow_commit":os.environ.get("GITHUB_SHA"),"worker_source_sha256":digest(__file__),
            "actual_source_sha256":SCI_SHA,"input_manifest_sha256":a.manifest_sha,
            "children":[],"readme_checks":[],"published_checkpoints":[],
            "original_targets_residual_enclosures_reference_ODE_and_primitive_recomputed":0,
            "original_recomputable_inputs_only_in_temporary_storage":True,
            "new_recomputable_data_persisted":False,"new_Actions_artifacts":False,
            "new_Release_uploads":False,"new_cap_existence_claimed":False,
            "new_endpoint_invariance_claimed":False,"full_infinite_BVP_inverse_proved":False,
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
        if (m["kind"]!="saved_positive_collar_components_public_inputs_v1"
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
        cases=s.get("new_collar_cases",{})
        candidates=[c for row in cases.values() for c in row.get("candidate_energy",{}).values()]
        return (s.get("kind")==SCIENTIFIC_KIND and s.get("source_sha256")==SCI_SHA
            and s.get("parameters")==self.manifest["parameters"] and s.get("complete") is True
            and s.get("failure") is None and len(s.get("gates",[]))==16
            and all(g.get("passed") is True for g in s["gates"])
            and s.get("actual_returncode")==0 and s.get("new_rho_cases_evaluated")==6
            and len(cases)==6 and s.get("new_coercivity_candidates_evaluated")==12
            and len(candidates)==12 and s.get("source_integrals_recomputed") is False
            and s.get("old_target_Fourier_trial_convolution_residual_repair_mean_flow_Green_calls")==0
            and s.get("actual_core_solution_or_full_matching_proved") is False
            and s.get("actual_low_inner_curvature_entry_proved") is False
            and s.get("actual_unknown_body_or_cut_norm_supplied") is False
            and s.get("input_manifest_sha256")==self.a.manifest_sha
            and all((c.get("complete_energy_and_trace_bounds") is not None)
                    == bool(c.get("complete_coercivity_applies")) for c in candidates)
            and all(not c.get("complete_coercivity_applies") or
                    (c.get("actual_mean_gap_positive") and c.get("tau_below_one") and c.get("t_below_one"))
                    for c in candidates))

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
            sp=pp.parent/"actual-saved-positive-collar-components.json"
            if not sp.is_file():continue
            s=read(sp)
            child0=any(c.get("label")=="saved_positive_collar_components"
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
            self.state["actual_rho_case_count"]=s.get("new_rho_cases_evaluated")
            self.state["actual_coercivity_candidate_count"]=s.get("new_coercivity_candidates_evaluated")
            self.state["actual_coercivity_candidate_pass_count"]=s.get("new_coercivity_candidates_passed")
            self.state["two_energy_tests_per_candidate"]=["tau_below_one","t_below_one"]
            self.state["core_existence_or_low_gamma_selfmap_claimed"]=False
            self.state["narrow_MA_domain_extended"]=False
            self.state["actual_scientific_gates"]=s.get("gates")
            self.state["actual_scientific_complete"]=s.get("complete")
            self.state["actual_scientific_failure"]=s.get("failure")
        self.state["snapshot_utc"]=now()
        self.state["wall_seconds"]=time.monotonic()-self.started

    def actual_report(self,s):
        lines=["# Actual saved positive-collar components and high-frequency coercivity","",
            "This is the complete small conclusion of a new public scalar restriction. "
            "The original4650 complete closed rows are restored byte for byte. "
            "No original target, coefficient, Fourier, trial, convolution, residual, repair, "
            "mean flow, source integral, Riccati equation or Green propagation is recomputed.","",
            "Run: "+self.rid+"/"+self.attempt+".",
            "Scientific source SHA256: "+SCI_SHA+".",
            "Scientific conclusion SHA256: "+digest(self.tempsummary)+".",
            "Complete: "+str(s.get("complete"))+".",
            "Failure: "+json.dumps(s.get("failure"),ensure_ascii=False)+".",
            "Structural gates passed: "+str(sum(x.get("passed") is True for x in s.get("gates",[])))+
                "/"+str(len(s.get("gates",[])))+".","",
            "## Complete identity and coverage gates",""]
        for x in s.get("gates",[]):
            lines.append("- "+str(x.get("passed"))+": "+x.get("name",""))
        lines+=["","## Exact ordinary collar and complete saved components","",
            "The output collar is exactly [17/20,19/20], with true cut9/10 and radial measure dr. "
            "The old moving components already contain physical alpha and the full even mean. "
            "The saved nonmean component and signed full S mean are used directly.",
            "Original counts: "+json.dumps(s.get("original_counts"),sort_keys=True)+".",""]
        for key,value in s.get("complete_original_component_restrictions",{}).items():
            lines.append("- "+key+": "+json.dumps(value,ensure_ascii=False))
        lines+=["","## All12 coercivity candidates","",
            "There are six distinct wide C0 radii and two high projections for each radius. "
            "The actual negative mean is a prerequisite. Tau and t are separate energy tests; "
            "they are not counted as structural input gates. A failed candidate retains all "
            "its inputs and failure reason, and supplies no positive inverse or trace bound.","",
            "| Wide rho | J | Actual mean prerequisite | Tau | t | Complete coercivity | Half-trace source gain |",
            "|---|---|---|---|---|---|---|"]
        def val(x):
            if isinstance(x,dict):return str(x.get("ball"))
            return str(x)
        for rho,row in s.get("new_collar_cases",{}).items():
            for label,c in row.get("candidate_energy",{}).items():
                b=c.get("complete_energy_and_trace_bounds") or {}
                fields=[rho,label,c.get("actual_mean_gap_positive"),c.get("tau"),c.get("t"),
                        c.get("complete_coercivity_applies"),b.get("half_trace_source_gain")]
                lines.append("| "+" | ".join(val(x) for x in fields)+" |")
        lines+=["","## Complete source and mean obligations","",
            "The true high equation keeps every selected-reference low column, its shell column, "
            "the radial cutoff source20 Zhigh, and the full ordinary residual projection. "
            "The old NR/WC F96 value is not reintegrated. F288 is zero only for the same actual "
            "residual-zero state and its complete canonical degree288 residual.",
            "Actual log-speed uses the full negative moving mean and the signed Smean enclosure. "
            "For a nonzero-residual iterate the additional residual-mean term remains unpaid here.",
            "Known A0 primitive1/4 and unknown C0 sawtooth pi/8 costs are distinct. "
            "Centre repair, selected canonical direction, and the full low mean are all retained. "
            "No response mean-completion flow is substituted for the canonical direction.",
            "The physical radial multiplier P is paid once in the final moving trace. "
            "The independent narrow MA same-state high bound is not extended by these wide tables.",
            "Unknown actual cut, shell, high body or receiver norms supplied: false.",
            "Actual low inner-curvature entry or selfmap proved: false.",
            "Actual core existence or full matching proved: false.",""]
        return "\n".join(lines)

    def emit_scientific_receipt(self):
        if not self.tempsummary.exists():return
        s=read(self.tempsummary)
        if s.get("source_sha256")!=SCI_SHA or s.get("parameters")!=self.manifest["parameters"]:
            raise ValueError("the stdout scientific receipt has the wrong mathematical identity")
        children=self.state.get("children",[])
        outcome=children[-1].get("actual_returncode") if children else None
        if self.state.get("complete_original_conclusion_reused_without_new_child"):outcome=0
        payload=dict(kind="complete_small_saved_positive_collar_components_stdout_v1",
            repository=PUBLIC,run_id=self.rid,run_attempt=self.attempt,
            source_sha256=SCI_SHA,worker_source_sha256=digest(__file__),
            input_manifest_sha256=self.a.manifest_sha,actual_returncode=outcome,
            scientific_conclusion_bytes=self.tempsummary.stat().st_size,
            scientific_conclusion_sha256=digest(self.tempsummary),
            complete_original_conclusion_reused_without_new_child=bool(
                self.state.get("complete_original_conclusion_reused_without_new_child")),
            original_success_process_sha256=self.state.get("original_success_process_sha256"),
            original_success_summary_sha256=self.state.get("original_success_summary_sha256"),
            actual_scientific_receipt=s,complete_actual_report=self.actual_report(s))
        raw=(json.dumps(payload,ensure_ascii=False,sort_keys=True,
                        separators=(",",":"),allow_nan=False)+"\n").encode()
        status=dict(kind="saved_positive_collar_prepublication_status_v1",actual_returncode=outcome,
            complete=s.get("complete"),failure=s.get("failure"),
            gates_passed=sum(x.get("passed") is True for x in s.get("gates",[])),
            gates_total=len(s.get("gates",[])),
            scientific_bytes=self.tempsummary.stat().st_size,scientific_sha256=digest(self.tempsummary),
            payload_bytes=len(raw),payload_sha256=hbytes(raw))
        statusraw=json.dumps(status,sort_keys=True,separators=(",",":"),allow_nan=False)
        if len(statusraw.encode())>1000:raise ValueError("prepublication status exceeds 1000 bytes")
        print("PREPUBLICATION_STATUS "+statusraw,flush=True)
        if len(raw)>59000:raise ValueError("the complete scientific stdout receipt exceeds 59000 UTF8 bytes")
        self.state["prepublication_scientific_stdout_receipt"]=dict(
            bytes=len(raw),sha256=hbytes(raw),complete_conclusion_included=True,complete_report_included=True,
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
                (self.dest/"actual-saved-positive-collar-components.json").write_bytes(raw)
                report=self.actual_report(read(self.tempsummary)).encode()
                if len(report)>60000:raise ValueError("the complete small report exceeds 60000 bytes")
                (self.dest/"actual-result.md").write_bytes(report)

            self.state["publication_is_final_attempt"]=bool(final)
            small(self.dest/"process.json",self.state)
            paths=[str((self.dest/"process.json").relative_to(self.repo))]
            if (self.dest/"actual-saved-positive-collar-components.json").exists():
                paths.append(str((self.dest/"actual-saved-positive-collar-components.json").relative_to(self.repo)))
                paths.append(str((self.dest/"actual-result.md").relative_to(self.repo)))
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
                run(["git","commit","-m",f"Record actual saved positive collar component run {self.rid} actual small conclusion"],self.repo)
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
             "--root",str(self.science),
             "--manifest",str(self.science/relative(self.a.manifest)),
             "--bits","320","--out",str(self.tempsummary)]
        log=self.work/"actual-science.log"
        entry={"label":"saved_positive_collar_components",
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
            raise RuntimeError("actual public saved collar scalar mathematics returned a nonzero code")
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
