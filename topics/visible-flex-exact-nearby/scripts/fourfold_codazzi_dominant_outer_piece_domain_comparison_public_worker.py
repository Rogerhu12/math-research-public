#!/usr/bin/env python3
"""Public exact whole-piece domain comparison with only conclusions and provenance persisted."""
from __future__ import annotations
import argparse,base64,hashlib,json,os,shutil,signal,subprocess,sys,time
from datetime import datetime,timezone
from pathlib import Path
PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
PIPELINE=TOPIC/"scripts/fourfold_codazzi_dominant_outer_piece_domain_comparison.py"
REPORTS=TOPIC/"notes/dominant_outer_piece_domain_comparison_ci"
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
    p.add_argument("--work",type=Path);p.add_argument("--prepared",type=Path);p.add_argument("--out-dir",type=Path)
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
        subprocess.run(gb+["sparse-checkout","set","--no-cone","--stdin"],cwd=root,
            input="\n".join("/"+v for v in sorted(paths))+"\n",text=True,check=True)
        print("Hydrated scripts, parameters, reviewed READMEs and small earlier conclusions only.",flush=True);return
    if a.work is None or a.prepared is None or a.out_dir is None:raise ValueError("temporary work paths are required")
    work=a.work.resolve();out=a.out_dir.resolve();prepared=a.prepared.resolve()
    if work.exists() or out.exists():raise FileExistsError("preserve an existing actual execution")
    if any(v.is_relative_to(root) for v in (work,out,prepared)):raise ValueError("reproducible data must stay outside Git")
    work.mkdir(parents=True);out.mkdir(parents=True);ws=sha(__file__)
    state=dict(kind="actual_public_dominant_whole_piece_domain_comparison_execution",repository=PUBLIC,
        run_id=os.environ["GITHUB_RUN_ID"],run_attempt=os.environ["GITHUB_RUN_ATTEMPT"],
        workflow_commit=os.environ["GITHUB_SHA"],worker_source_sha256=ws,
        domain_comparison_source_sha256=a.pipeline_sha,input_manifest_sha256=a.manifest_sha,
        reviewed_rules_sha256=a.rules_sha,explicitly_read_rules_commit=rules["read_commit"],
        started_utc=utc(),complete=False,actual_returncode=None,readme_checks=[],
        actual_domain_comparison_processes=0,old_numerical_enclosures_recomputed=0,
        reproducible_data_published_to_repository=False,reproducible_data_uploaded_to_Releases=False,
        new_reproducible_data_artifact_uploaded=False,new_operator_norm_claimed=False,final_topic_complete=False)
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
        save(out/"worker-process.json",state)
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
        if v.get("complete") is True and v.get("input_manifest_sha256")==a.manifest_sha and v.get("domain_comparison_source_sha256")==a.pipeline_sha:
            print(json.dumps(dict(reused_existing_complete_conclusion=str(old.relative_to(root)),
                original_run_id=v["run_id"],new_domain_comparison_processes=0,new_numerical_enclosures=0)),flush=True);return
    hist=m["historical_input_commit"]
    if len(hist)!=40 or any(c not in "0123456789abcdef" for c in hist):raise ValueError("the input commit is not immutable")
    git("fetch","--filter=blob:none","--no-tags","origin",hist)
    state["historical_input_commit"]=hist;state["input_receipts"]=[]
    external={v["path"]:v for v in m.get("external_original_inputs",[])}
    for e in m["files"]:
        rel=relpath(e["path"]);dst=work/rel;dst.parent.mkdir(parents=True,exist_ok=True)
        if str(rel) in external:
            spec=external[str(rel)];src=prepared/spec["artifact_relative_path"]
            checked(src,e["bytes"],e["sha256"]);shutil.copyfile(src,dst)
            origin=dict(kind="original_complete_Actions_artifact",run_id=spec["artifact_run_id"],
                artifact_id=spec["artifact_id"],artifact_relative_path=spec["artifact_relative_path"])
        elif (root/rel).is_file():
            checked(root/rel,e["bytes"],e["sha256"]);shutil.copyfile(root/rel,dst)
            origin=dict(kind="exact_current_text_input")
        else:
            with dst.open("wb") as stream:git("show",hist+":"+str(rel),stdout=stream)
            origin=dict(kind="exact_public_historical_blob",commit=hist)
        checked(dst,e["bytes"],e["sha256"])
        state["input_receipts"].append(dict(path=str(rel),bytes=e["bytes"],sha256=e["sha256"],origin=origin))
    tm=work/rm;tm.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(a.manifest,tm)
    checked(work/PIPELINE,next(e["bytes"] for e in m["files"] if e["path"]==str(PIPELINE)),a.pipeline_sha)
    cmd=[sys.executable,"-u",str(work/PIPELINE),"--repo",str(work),"--manifest",str(tm),
        "--manifest-sha",a.manifest_sha,"--out-dir",str(out/"consumers")]
    state["command"]=cmd;state["actual_scientific_checkout_commit"]=git("rev-parse","HEAD").stdout.strip()
    state["actual_domain_comparison_processes"]=1;save(out/"worker-process.json",state)
    ce=os.environ.copy();ce.pop("GITHUB_TOKEN",None);ce["VISIBLE_PHASE_SCIENCE_COMMIT"]=state["actual_scientific_checkout_commit"]
    started=time.monotonic()
    with (out/"domain-comparison.stdout.log").open("wb") as log:
        child=subprocess.Popen(cmd,cwd=work,env=ce,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
        try:child.wait(timeout=3000)
        except subprocess.TimeoutExpired:
            state["timeout_seconds"]=3000;os.killpg(child.pid,signal.SIGTERM)
            try:child.wait(timeout=10)
            except subprocess.TimeoutExpired:os.killpg(child.pid,signal.SIGKILL);child.wait()
        state["actual_returncode"]=child.returncode
    state["domain_comparison_child_wall_seconds"]=time.monotonic()-started
    c=out/"consumers";proc=read(c/"process.json") if (c/"process.json").is_file() else None
    state["complete"]=bool(child.returncode==0 and proc and proc.get("complete") is True and proc.get("actual_returncode")==0)
    state["actual_failure"]=None if proc is None else proc.get("failure")
    state["output_hashes"]=[rec(p,out) for p in sorted(out.rglob("*")) if p.is_file() and not p.name.endswith(".partial") and p.name!="worker-process.json"]
    if proc is not None:
        state["actual_domain_comparison_receipt"]={k:proc.get(k) for k in
            ("new_exact_domain_comparison_processes","old_numerical_enclosures_recomputed",
             "old_mathematical_stages_recomputed","new_target_or_FFT_evaluations",
             "original_cubic_values_evaluated","new_operator_norms_or_radial_integrals_evaluated",
             "actual_domain_comparison_wall_seconds","historical_input_commit","gates",
             "domain_extension_permitted_by_this_comparison","required_next_source_contract")}
    save(out/"worker-process.json",state)
    # One bounded50-minute child, followed by an actual README-checked pull.
    sync();report=root/REPORTS/("run-"+state["run_id"]+"-"+state["run_attempt"]);report.mkdir(parents=True,exist_ok=True)
    def conclusion():
        actual=c/"conclusion.md"
        if actual.is_file():
            return actual.read_text()
        return "\n".join(["# Whole-piece domain comparison: actual incomplete run","",
            "- Public repository: "+PUBLIC,
            "- Actual run: "+state["run_id"]+"/"+state["run_attempt"],
            "- Script: "+str(PIPELINE),"- Script SHA256: "+a.pipeline_sha,
            "- Manifest: "+str(rm),"- Manifest SHA256: "+a.manifest_sha,
            "- Original input commit: "+hist,
            "- Actual child return code: "+str(state["actual_returncode"]),
            "- Actual failure: "+json.dumps(state["actual_failure"],ensure_ascii=False),
            "- Old numerical enclosures recomputed: 0.",
            "No domain or new source bound is asserted. No new data, Release, or artifact is persisted.",""])
    def snapshot():
        text=conclusion();raw=(json.dumps(state,indent=2,ensure_ascii=False,allow_nan=False)+"\n").encode()
        if len(text.encode())>=100000 or len(raw)>60000:raise ValueError("small conclusion or provenance exceeds its size limit")
        (report/"actual-result.md").write_text(text);(report/"execution.json").write_bytes(raw)
        # Never copy any native, stage, numerical array or original case into Git.
    snapshot();owned=str(report.relative_to(root));git("add","--sparse","--",owned)
    git("commit","-m","visible-exact: record exact whole-piece domain conclusions under no-data rule15")
    while True:
        r=git("push","origin","HEAD:refs/heads/main",check=False)
        if r.returncode==0:break
        if not any(v in r.stderr for v in ("non-fast-forward","fetch first","cannot lock ref","remote rejected")):
            raise RuntimeError("conclusion push failed outside concurrent-main rebase")
        sync();snapshot();git("add","--sparse","--",owned);git("commit","--amend","--no-edit")
    print(json.dumps(dict(complete=state["complete"],actual_returncode=state["actual_returncode"],
        report=owned,old_numerical_enclosures_recomputed=0,new_domain_comparison_processes=1,
        reproducible_output_files_persisted=0,output_hash_count=len(state["output_hashes"]),
        original_inputs_unchanged=True),ensure_ascii=False),flush=True)
    if not state["complete"]:raise SystemExit(1)
if __name__=="__main__":main()
