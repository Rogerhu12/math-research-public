#!/usr/bin/env python3
"""Public complete regular-transport first-local-vector reduction; persist only small conclusions."""
from __future__ import annotations
import argparse,ast,base64,hashlib,json,os,shutil,signal,subprocess,sys,time
from datetime import datetime,timezone
from pathlib import Path
PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
PIPELINE=TOPIC/"scripts/fourfold_codazzi_regular_transport_first_local_vector.py"
REPORTS=TOPIC/"notes/regular_transport_first_local_vector_ci"
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def utc():return datetime.now(timezone.utc).isoformat()
def save(p,v):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    t=p.with_name(p.name+".partial")
    t.write_text(json.dumps(v,indent=2,ensure_ascii=False,allow_nan=False)+"\n");t.replace(p)
def checked(p,size,digest):
    p=Path(p)
    if not p.is_file() or p.stat().st_size!=size or sha(p)!=digest:
        raise ValueError("a complete pinned input differs: "+str(p))
def read(p):return json.loads(Path(p).read_text())
def relpath(p):
    p=Path(p)
    if p.is_absolute() or ".." in p.parts or not str(p).startswith(str(TOPIC)+"/"):
        raise ValueError("an input left the authorized topic")
    return p
def rec(p,base):
    p=Path(p);return dict(file=str(p.relative_to(base)),bytes=p.stat().st_size,sha256=sha(p))
def ball(v):
    if isinstance(v,dict):
        if isinstance(v.get("ball"),str):return v["ball"]
        if "upper" in v:return str(v["upper"])
        return json.dumps(v,ensure_ascii=False,separators=(",",":"))
    return str(v)
def cell(v):return str(v).replace("|","\\|").replace("\n"," ")

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--mode",choices=("hydrate","run"),required=True)
    p.add_argument("--manifest",type=Path,required=True)
    p.add_argument("--manifest-sha",required=True)
    p.add_argument("--pipeline-sha",required=True)
    p.add_argument("--rules",type=Path,required=True)
    p.add_argument("--rules-sha",required=True)
    p.add_argument("--work",type=Path);p.add_argument("--out-dir",type=Path)
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("only the public repository Actions may consume the scientific inputs")
    root=Path(os.environ["GITHUB_WORKSPACE"]).resolve()
    a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    if sha(a.manifest)!=a.manifest_sha or sha(a.rules)!=a.rules_sha:raise ValueError("separate execution pins changed")
    m=read(a.manifest);rules=read(a.rules)
    if m["public_repository"]!=PUBLIC or rules["repository"]!=PUBLIC:raise ValueError("wrong public repository")
    for k in ("reproducible_data_persisted_in_repository","reproducible_data_persisted_in_Releases","new_reproducible_Actions_output_uploads"):
        if rules["large_data_policy"].get(k) is not False:raise ValueError("latest no-data rule15 is required")
    rm=a.manifest.relative_to(root);rr=a.rules.relative_to(root);rw=Path(__file__).resolve().relative_to(root)
    gb=["git","-c","safe.directory="+str(root)]
    if a.mode=="hydrate":
        paths={str(PIPELINE),str(rw),str(rm),str(rr),str(REPORTS)+"/"}|set(rules["readme_sha256"])
        # Every post-history input is explicitly present before freezing science.
        paths.update(e["path"] for e in m["files"] if e["path"].endswith((".py",".md")))
        paths.update(m["input_paths"][k] for k in m["current_text_input_roles"])
        subprocess.run(gb+["sparse-checkout","set","--no-cone","--stdin"],cwd=root,
            input="\n".join("/"+v for v in sorted(paths))+"\n",text=True,check=True)
        print("Hydrated the reviewed regular-transport reduction script and current contracts; no numerical data checkout.",flush=True);return
    if a.work is None or a.out_dir is None:raise ValueError("temporary work paths are required")
    work=a.work.resolve();out=a.out_dir.resolve()
    if work.exists() or out.exists():raise FileExistsError("preserve an existing actual execution")
    if any(v.is_relative_to(root) for v in (work,out)):raise ValueError("reproducible data must stay outside Git")
    work.mkdir(parents=True);out.mkdir(parents=True);ws=sha(__file__)
    state=dict(kind="actual_public_regular_transport_first_local_vector_execution",repository=PUBLIC,
        run_id=os.environ["GITHUB_RUN_ID"],run_attempt=os.environ["GITHUB_RUN_ATTEMPT"],
        workflow_commit=os.environ["GITHUB_SHA"],worker_source_sha256=ws,
        source_budget_source_sha256=a.pipeline_sha,input_manifest_sha256=a.manifest_sha,
        reviewed_rules_sha256=a.rules_sha,explicitly_read_rules_commit=rules["read_commit"],
        started_utc=utc(),complete=False,actual_returncode=None,readme_checks=[],
        actual_source_budget_processes=0,old_numerical_enclosures_recomputed=0,
        reproducible_data_published_to_repository=False,reproducible_data_uploaded_to_Releases=False,
        new_reproducible_data_artifact_uploaded=False,full_high_inverse_claimed=False,final_topic_complete=False)
    env=os.environ.copy();token=env.pop("GITHUB_TOKEN")
    env.update(GIT_TERMINAL_PROMPT="0",GIT_CONFIG_COUNT="1",
        GIT_CONFIG_KEY_0="http.https://github.com/.extraheader",
        GIT_CONFIG_VALUE_0="AUTHORIZATION: basic "+base64.b64encode(("x-access-token:"+token).encode()).decode())
    def git(*args,check=True,stdout=None):
        r=subprocess.run(gb+list(args),cwd=root,env=env,text=stdout is None,
            stdout=subprocess.PIPE if stdout is None else stdout,stderr=subprocess.PIPE,timeout=900)
        if check and r.returncode:
            e=r.stderr if isinstance(r.stderr,str) else r.stderr.decode("utf-8","replace")
            raise RuntimeError("public Git "+str(args[0])+" failed: "+e[:1200])
        return r
    def sync():
        before=git("rev-parse","HEAD").stdout.strip();git("pull","--rebase","origin","main")
        after=git("rev-parse","origin/main").stdout.strip()
        diff=git("diff",before,after,"--",*rules["readme_sha256"]).stdout
        state["readme_checks"].append(dict(time=utc(),before=before,after=after,actual_diff=diff,
            explicitly_reviewed_commit=rules["read_commit"]))
        # Metadata only: no certificate or array body is read for capacity.
        objects=git("ls-tree","-r","-l","HEAD","--",str(TOPIC)).stdout.splitlines()
        sizes=[int(line.split("\t",1)[0].split()[3]) for line in objects
            if line.split("\t",1)[0].split()[1]=="blob"]
        state["current_topic_blob_bytes"]=sum(sizes)
        state["current_topic_blob_count"]=len(sizes)
        state["current_topic_metadata_commit"]=git("rev-parse","HEAD").stdout.strip()
        state["current_topic_below_200000000_bytes"]=sum(sizes)<200000000
        save(out/"worker-process.json",state)
        if not state["current_topic_below_200000000_bytes"]:
            raise ValueError("actual topic Git blobs reach the200000000-byte hard limit")
        for path,digest in rules["readme_sha256"].items():
            if sha(root/path)!=digest:
                print(diff,flush=True);raise RuntimeError("read and apply the newly changed README diff")
        if sha(a.rules)!=a.rules_sha or sha(a.manifest)!=a.manifest_sha or sha(root/PIPELINE)!=a.pipeline_sha:
            raise ValueError("the separately pinned execution contract changed during pull")
        if sha(root/rw)!=ws:raise ValueError("the running wrapper changed during pull")
    git("config","user.name","github-actions[bot]")
    git("config","user.email","41898282+github-actions[bot]@users.noreply.github.com");sync()
    for old in sorted((root/REPORTS).glob("*/execution.json")):
        v=read(old)
        if v.get("complete") is True and v.get("input_manifest_sha256")==a.manifest_sha and v.get("source_budget_source_sha256")==a.pipeline_sha:
            print(json.dumps(dict(reused_existing_complete_conclusion=str(old.relative_to(root)),
                original_run_id=v["run_id"],new_source_budget_processes=0,new_numerical_enclosures=0)),flush=True);return
    hist=m["historical_input_commit"]
    if len(hist)!=40 or any(c not in "0123456789abcdef" for c in hist):raise ValueError("the input commit is not immutable")
    git("fetch","--filter=blob:none","--no-tags","origin",hist)
    state["historical_input_commit"]=hist;state["input_receipts"]=[]
    if m.get("legacy_artifact_inputs",[]):raise ValueError("this small input closure needs no legacy artifact")
    last_sync=time.monotonic()
    actual_inputs=[]
    must_be_current={str(PIPELINE)}|{m["input_paths"][k] for k in m["current_text_input_roles"]}
    for e in m["files"]:
        rel=relpath(e["path"]);dst=work/rel;dst.parent.mkdir(parents=True,exist_ok=True)
        if str(rel) in must_be_current:
            checked(root/rel,e["bytes"],e["sha256"]);shutil.copyfile(root/rel,dst)
            origin=dict(kind="exact_current_text_input")
        elif ((root/rel).is_file() and (root/rel).stat().st_size==e["bytes"]
            and sha(root/rel)==e["sha256"]):
            shutil.copyfile(root/rel,dst)
            origin=dict(kind="exact_current_identical_legacy_input")
        else:
            with dst.open("wb") as stream:git("show",hist+":"+str(rel),stdout=stream)
            origin=dict(kind="exact_public_historical_blob",commit=hist)
        checked(dst,e["bytes"],e["sha256"])
        actual_inputs.append(dict(path=str(rel),bytes=e["bytes"],sha256=e["sha256"],origin=origin))
        if time.monotonic()-last_sync>3000:
            sync();last_sync=time.monotonic()
    # Preserve the exact complete input digest without copying reproducible numerical data.
    state.pop("input_receipts",None)
    state["actual_verified_input_count"]=len(actual_inputs)
    state["actual_verified_input_receipts_sha256"]=hashlib.sha256(
        json.dumps(actual_inputs,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
    origins={}
    for entry in actual_inputs:
        key=entry["origin"]["kind"];origins[key]=origins.get(key,0)+1
    state["actual_input_origins"]=origins
    critical=must_be_current|{str(rm),str(rr)}
    state["actual_current_contract_receipts"]=[
        entry for entry in actual_inputs if entry["path"] in critical]
    tm=work/rm;tm.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(a.manifest,tm)
    checked(tm,a.manifest.stat().st_size,a.manifest_sha)
    tr=work/rr;tr.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(a.rules,tr)
    checked(tr,a.rules.stat().st_size,a.rules_sha)
    state["actual_current_contract_receipts"].extend([
        dict(path=str(rm),bytes=tm.stat().st_size,sha256=a.manifest_sha,
            origin=dict(kind="exact_current_separately_pinned_manifest")),
        dict(path=str(rr),bytes=tr.stat().st_size,sha256=a.rules_sha,
            origin=dict(kind="exact_current_separately_pinned_rules"))])
    checked(work/PIPELINE,next(e["bytes"] for e in m["files"] if e["path"]==str(PIPELINE)),a.pipeline_sha)
    parsed=[]
    for entry in m["files"]:
        if entry["path"].endswith(".py"):
            path=work/relpath(entry["path"])
            ast.parse(path.read_text(),filename=str(path))
            parsed.append(dict(path=entry["path"],sha256=entry["sha256"]))
    state["complete_immutable_Python_AST_closure_passed"]=True
    state["complete_immutable_Python_AST_file_count"]=len(parsed)
    state["complete_immutable_Python_AST_inventory_sha256"]=hashlib.sha256(
        json.dumps(parsed,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
    cmd=[sys.executable,"-u",str(work/PIPELINE),"--repo",str(work),"--manifest",str(tm),
        "--manifest-sha",a.manifest_sha,"--out-dir",str(out/"consumers")]
    state["command"]=cmd;state["actual_scientific_checkout_commit"]=git("rev-parse","HEAD").stdout.strip()
    state["actual_source_budget_processes"]=1;save(out/"worker-process.json",state)
    ce=os.environ.copy();ce.pop("GITHUB_TOKEN",None);ce["VISIBLE_PHASE_SCIENCE_COMMIT"]=state["actual_scientific_checkout_commit"]
    started=time.monotonic()
    with (out/"source-budget.stdout.log").open("wb") as log:
        child=subprocess.Popen(cmd,cwd=work,env=ce,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
        try:child.wait(timeout=900)
        except subprocess.TimeoutExpired:
            state["timeout_seconds"]=900;os.killpg(child.pid,signal.SIGTERM)
            try:child.wait(timeout=10)
            except subprocess.TimeoutExpired:os.killpg(child.pid,signal.SIGKILL);child.wait()
        state["actual_returncode"]=child.returncode
    state["source_budget_child_wall_seconds"]=time.monotonic()-started
    c=out/"consumers";proc=read(c/"process.json") if (c/"process.json").is_file() else None
    state["complete"]=bool(child.returncode==0 and proc and proc.get("complete") is True
        and proc.get("proved") is True and proc.get("actual_returncode")==0
        and proc.get("failure") is None and len(proc.get("gates",[]))==13
        and all(g["passed"] for g in proc["gates"])
        and proc.get("source_sha256")==a.pipeline_sha and proc.get("input_manifest_sha256")==a.manifest_sha
        and proc.get("old_numerical_enclosures_recomputed")==0
        and proc.get("old_forcing_transport_Taylor_RF_or_profile_recomputed")==0
        and proc.get("old_operator_words_or_positive_calibration_recomputed")==0
        and proc.get("old_source_rows_or_radial_integrals_recomputed")==0
        and proc.get("original_natural_stage_bytes_modified")==0
        and proc.get("original_complete_fold_stages_read")==1
        and proc.get("original_successful_small_receipts_read")==4
        and proc.get("original_positive_linear_coefficients_read")==18
        and proc.get("original_complete_source_terms_read")==31
        and proc.get("new_complete_subproduct_budgets")==1
        and proc.get("new_complete_regular_local_vector_budgets")==1
        and proc.get("new_fixed_positive_operator_comparisons")==1
        and proc.get("new_complete_uniform_factors")==1
        and proc.get("new_complete_scalar_recombinations")==3
        and proc.get("full_physical_negative_volume_source_paid") is True
        and proc.get("full_high_inverse_claimed") is False)
    state["new_complete_regular_transport_local_reduction_proved"]=state["complete"]
    state["actual_failure"]=(dict(type="MissingScientificProcessReport",
        message="the actual child did not produce its small process.json") if proc is None else proc.get("failure"))
    if proc and proc.get("formatting_failure") is not None:
        state["formatting_failure"]=proc["formatting_failure"]
        state["actual_scientific_returncode"]=proc.get("actual_scientific_returncode")
    selected_outputs=[c/"conclusion.md",c/"process.json",
        c/"temporary-regular-transport-first-local-vector.json.gz",out/"source-budget.stdout.log"]
    state["output_hashes"]=[rec(path,out) for path in selected_outputs if path.is_file()]
    if proc is not None:
        state["actual_scientific_receipt"]={k:proc.get(k) for k in (
            "complete","proved","actual_returncode","failure","gates",
            "actual_mathematical_wall_seconds","source_sha256","input_manifest_sha256","runtime","arithmetic_bits",
            "public_repository","run_id","run_attempt","workflow_event_commit","actual_scientific_checkout_commit",
            "original_natural_stage_bytes_modified","original_complete_fold_stages_read",
            "original_successful_small_receipts_read","original_positive_linear_coefficients_read",
            "original_complete_source_terms_read","new_complete_subproduct_budgets",
            "new_complete_regular_local_vector_budgets","new_fixed_positive_operator_comparisons",
            "new_complete_uniform_factors","new_complete_scalar_recombinations",
            "old_numerical_enclosures_recomputed","old_forcing_transport_Taylor_RF_or_profile_recomputed",
            "old_operator_words_or_positive_calibration_recomputed","old_source_rows_or_radial_integrals_recomputed",
            "full_physical_negative_volume_source_paid","full_high_inverse_claimed",
            "mathematical_parameters","complete_domain_conclusion","complete_raw_local_vector_conclusion",
            "complete_comparison_conclusion","complete_source_conclusion","scope",
            "temporary_native_sha256","temporary_native_bytes","temporary_native_is_not_published",
            "reproducible_outputs_published_to_repository",
            "reproducible_outputs_uploaded_to_Releases","new_reproducible_data_artifact_uploaded")}
    save(out/"worker-process.json",state)
    # One bounded15-minute scientific child, followed by an actual README-checked pull.
    sync();report=root/REPORTS/("run-"+state["run_id"]+"-"+state["run_attempt"]);report.mkdir(parents=True,exist_ok=True)
    def conclusion():
        actual=c/"conclusion.md"
        if actual.is_file():
            return actual.read_text()
        return "\n".join(["# Regular-transport first-local-vector reduction: actual incomplete run","",
            "- Public repository: "+PUBLIC,
            "- Actual run: "+state["run_id"]+"/"+state["run_attempt"],
            "- Script: "+str(PIPELINE),"- Script SHA256: "+a.pipeline_sha,
            "- Manifest: "+str(rm),"- Manifest SHA256: "+a.manifest_sha,
            "- Original input commit: "+hist,
            "- Actual child return code: "+str(state["actual_returncode"]),
            "- Actual failure: "+json.dumps(state["actual_failure"],ensure_ascii=False),
            "- Old numerical enclosures recomputed: 0.",
            "No new complete regular-transport improvement is asserted. No new data, Release, or artifact is persisted.",""])
    def snapshot():
        text=conclusion()
        names=[str((report/name).relative_to(root)) for name in ("actual-result.md","execution.json")]
        current=git("ls-tree","-r","-l","HEAD","--",str(TOPIC)).stdout.splitlines()
        total=sum(int(line.split("\t",1)[0].split()[3]) for line in current
            if line.split("\t",1)[0].split()[1]=="blob")
        previous=git("ls-tree","-r","-l","HEAD","--",*names).stdout.splitlines()
        oldbytes=sum(int(line.split("\t",1)[0].split()[3]) for line in previous
            if line.split("\t",1)[0].split()[1]=="blob")
        state["publication_base_topic_blob_bytes"]=total
        state["publication_capacity_metadata_commit"]=git("rev-parse","HEAD").stdout.strip()
        state["projected_topic_blob_bytes"]=0
        while True:
            raw=(json.dumps(state,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
            projected=total-oldbytes+len(text.encode())+len(raw)
            if projected==state["projected_topic_blob_bytes"]:break
            state["projected_topic_blob_bytes"]=projected
        if projected>=200000000:raise ValueError("the two small conclusions exceed the actual topic capacity")
        if len(text.encode())>60000 or len(raw)>60000:raise ValueError("small conclusion or provenance exceeds its size limit")
        (report/"actual-result.md").write_text(text);(report/"execution.json").write_bytes(raw)
        # Never copy any native, stage, numerical array or original case into Git.
    snapshot();owned=str(report.relative_to(root));git("add","--sparse","--",owned)
    git("commit","-m","visible-exact: record complete regular-transport first-local-vector reduction")
    while True:
        r=git("push","origin","HEAD:refs/heads/main",check=False)
        if r.returncode==0:break
        if not any(v in r.stderr for v in ("non-fast-forward","fetch first","cannot lock ref","remote rejected")):
            raise RuntimeError("conclusion push failed outside concurrent-main rebase")
        sync();snapshot();git("add","--sparse","--",owned);git("commit","--amend","--no-edit")
    print(json.dumps(dict(complete=state["complete"],actual_returncode=state["actual_returncode"],
        report=owned,old_numerical_enclosures_recomputed=0,new_source_budget_processes=1,
        reproducible_output_files_persisted=0,output_hash_count=len(state["output_hashes"]),
        original_inputs_unchanged=True),ensure_ascii=False),flush=True)
    if not state["complete"]:raise SystemExit(1)
if __name__=="__main__":main()
