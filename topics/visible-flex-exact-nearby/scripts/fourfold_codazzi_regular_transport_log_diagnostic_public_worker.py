#!/usr/bin/env python3
"""Read two failed public job logs and publish only bounded failure metadata; never run science."""
from __future__ import annotations
import argparse,base64,hashlib,json,os,re,subprocess,urllib.error,urllib.parse,urllib.request
from datetime import datetime,timezone
from pathlib import Path
PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
REPORTS=TOPIC/"notes/regular_transport_log_diagnostic_ci"
JOBS=((43705772615,132786394695,"fb3a6f2bbfa8d5d72266e709bcccd0ebd1848b18"),
      (43707514815,132791691389,"c9c96f3431a0ec6a8213e2359186531fb851f822"))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def utc():return datetime.now(timezone.utc).isoformat()
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--rules",type=Path,required=True);p.add_argument("--rules-sha",required=True)
    p.add_argument("--source-sha",required=True);a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("this read-only log diagnostic is public Actions only")
    root=Path(os.environ["GITHUB_WORKSPACE"]).resolve();source=Path(__file__).resolve()
    rules_path=a.rules.resolve()
    if sha(source)!=a.source_sha or sha(rules_path)!=a.rules_sha:raise ValueError("diagnostic or rules pin changed")
    rules=json.loads(rules_path.read_text())
    if rules["repository"]!=PUBLIC:raise ValueError("wrong reviewed repository")
    for key in ("reproducible_data_persisted_in_repository","reproducible_data_persisted_in_Releases","new_reproducible_Actions_output_uploads"):
        if rules["large_data_policy"].get(key) is not False:raise ValueError("current no-data rule15 is required")
    token=os.environ["GITHUB_TOKEN"];env=os.environ.copy();env.pop("GITHUB_TOKEN",None)
    env.update(GIT_TERMINAL_PROMPT="0",GIT_CONFIG_COUNT="1",
        GIT_CONFIG_KEY_0="http.https://github.com/.extraheader",
        GIT_CONFIG_VALUE_0="AUTHORIZATION: basic "+base64.b64encode(("x-access-token:"+token).encode()).decode())
    state=dict(kind="two_actual_regular_transport_failure_logs",repository=PUBLIC,
        run_id=os.environ["GITHUB_RUN_ID"],run_attempt=os.environ["GITHUB_RUN_ATTEMPT"],
        workflow_commit=os.environ["GITHUB_SHA"],source_sha256=a.source_sha,rules_sha256=a.rules_sha,
        started_utc=utc(),readme_checks=[],jobs=[],new_scientific_subprocesses=0,
        old_numerical_enclosures_recomputed=0,new_numerical_enclosures=0,
        original_logs_or_numerical_data_persisted=False,Release_or_artifact_upload=False,
        current_exact_topic_size_asserted=False,maximum_combined_published_receipt_bytes=40000)
    def git(*args,check=True):
        r=subprocess.run(["git","-c","safe.directory="+str(root),*args],cwd=root,env=env,
            text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=900)
        if check and r.returncode:raise RuntimeError("public Git "+args[0]+" failed: "+r.stderr[:1000])
        return r
    def sync():
        before=git("rev-parse","HEAD").stdout.strip();git("pull","--rebase","origin","main")
        after=git("rev-parse","origin/main").stdout.strip()
        diff=git("diff",before,after,"--",*rules["readme_sha256"]).stdout
        state["readme_checks"].append(dict(time=utc(),before=before,after=after,actual_diff=diff))
        for path,digest in rules["readme_sha256"].items():
            if sha(root/path)!=digest:raise RuntimeError("a reviewed README changed; read its actual diff")
        if sha(source)!=a.source_sha or sha(rules_path)!=a.rules_sha:raise ValueError("a diagnostic execution pin changed")
    git("config","user.name","github-actions[bot]")
    git("config","user.email","41898282+github-actions[bot]@users.noreply.github.com")
    sync()
    class StopRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self,request,fp,code,message,headers,newurl):return None
    opener=urllib.request.build_opener(StopRedirect())
    def public_read(path,limit):
        url="https://api.github.com/repos/"+PUBLIC+path
        for unused in range(5):
            parts=urllib.parse.urlsplit(url);host=parts.hostname
            allowed=(host=="api.github.com" or (host is not None and
                (host.endswith(".blob.core.windows.net") or host.endswith(".githubusercontent.com"))))
            if parts.scheme!="https" or parts.username or parts.password or parts.port not in (None,443) or not allowed:
                raise ValueError("the public log endpoint redirected outside its allowed hosts")
            headers={"Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28"} if host=="api.github.com" else {"Accept":"text/plain"}
            if host=="api.github.com":headers["Authorization"]="Bearer "+token
            try:
                with opener.open(urllib.request.Request(url,headers=headers),timeout=45) as response:
                    data=response.read(limit+1)
                if len(data)>limit:raise ValueError("the complete public metadata/log exceeded its bounded read")
                return data,host
            except urllib.error.HTTPError as error:
                if error.code in (301,302,303,307,308):
                    location=error.headers.get("Location","")
                    if not location:raise RuntimeError("public log redirect had no Location") from None
                    url=urllib.parse.urljoin(url,location);continue
                raise RuntimeError("public metadata/log HTTP "+str(error.code)) from None
            except urllib.error.URLError:raise RuntimeError("public metadata/log transport failure") from None
        raise RuntimeError("public metadata/log exceeded its redirect bound")
    for run_id,job_id,commit in JOBS:
        record=dict(run_id=run_id,job_id=job_id,workflow_commit=commit,complete=False,
            original_scientific_subprocess_started="not inferred by this diagnostic")
        try:
            raw_job,host=public_read("/actions/jobs/"+str(job_id),1000000);job=json.loads(raw_job)
            if (job.get("id")!=job_id or job.get("run_id")!=run_id or job.get("head_sha")!=commit
                or job.get("status")!="completed" or job.get("conclusion")!="failure"):
                raise ValueError("the actual job/run/commit/failure identity differs")
            record["job_metadata_identity"]=dict(bytes=len(raw_job),sha256=hashlib.sha256(raw_job).hexdigest())
            record["actual_job"]={key:job.get(key) for key in
                ("id","run_id","head_sha","status","conclusion","started_at","completed_at")}
            record["failed_steps"]=[{key:step.get(key) for key in
                ("number","name","status","conclusion","started_at","completed_at")}
                for step in job["steps"] if step.get("conclusion")=="failure"]
            raw,host=public_read("/actions/jobs/"+str(job_id)+"/logs",10000000)
            record["complete_log_identity"]=dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),
                download_host=host,complete=True,body_persisted=False)
            text=raw.decode("utf-8")
            lines=[re.sub(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z ?", "", line)
                for line in text.splitlines()]
            starts=[i for i,line in enumerate(lines) if "Traceback (most recent call last):" in line]
            trace=[]
            if starts:
                for line in lines[starts[-1]:]:
                    if line.startswith("##[group]") or line.startswith("##[error]Process completed"):break
                    trace.append(line)
            else:
                trace=[line for line in lines if line.startswith("##[error]") or
                    any(word in line for word in ("TimeoutExpired","Traceback","ValueError:","RuntimeError:","SyntaxError:"))][-30:]
            trace="\n".join(trace)
            record["actual_stack_sha256"]=hashlib.sha256(trace.encode()).hexdigest()
            record["actual_stack_bytes"]=len(trace.encode())
            record["actual_stack_is_complete"]=len(trace.encode())<=9000
            if len(trace.encode())>9000:trace=trace.encode()[-9000:].decode("utf-8","replace")
            record["actual_stack_or_error_lines"]=trace
            record["stack_markers"]=dict(
                TimeoutExpired="subprocess.TimeoutExpired" in trace,
                first_sync='git("config","user.email","41898282+github-actions[bot]@users.noreply.github.com");sync()' in trace,
                original_ls_tree='objects=git("ls-tree","-r","-l","HEAD","--",str(TOPIC)).stdout.splitlines()' in trace,
                exact_ls_tree_arguments="'ls-tree', '-r', '-l', 'HEAD', '--', 'topics/visible-flex-exact-nearby'" in trace,
                nine_hundred_seconds="900 seconds" in trace,
                capacity_tree_metadata="topic_tree_metadata" in trace,
                scientific_Popen_frame="child=subprocess.Popen" in trace)
            record["complete"]=True;record["failure"]=None
        except Exception as error:
            record["failure"]=dict(type=type(error).__name__,message=str(error)[:1600])
        state["jobs"].append(record)
    state["complete"]=all(row["complete"] for row in state["jobs"])
    state["finished_utc"]=utc()
    # This exact bounded summary is printed even if the later small Git publication fails.
    filtered=json.dumps(state,ensure_ascii=False,separators=(",",":"),allow_nan=False)
    if len(filtered.encode())>40000:raise ValueError("the filtered stdout diagnostic exceeds40000bytes")
    print("BEGIN_BOUNDED_ACTUAL_FAILURE_DIAGNOSTIC",flush=True)
    print(filtered,flush=True)
    print("END_BOUNDED_ACTUAL_FAILURE_DIAGNOSTIC",flush=True)
    sync()
    report=root/REPORTS/("run-"+state["run_id"]+"-"+state["run_attempt"]);report.mkdir(parents=True,exist_ok=True)
    def snapshot():
        text=["# Actual regular-transport failure logs: read-only diagnosis","",
            "This public run executes no scientific process, imports no mathematical producer, and requests no Git Trees or blob-size audit.",
            "The two original failures remain failures. Their elapsed time alone proves no scientific status.","",
            "Only exact full-log identities and bounded real stacks are retained. Full logs remain temporary.",""]
        for row in state["jobs"]:
            text += ["## Original job "+str(row["job_id"]),"",
                "- Run: "+str(row["run_id"])+"/1.",
                "- Workflow commit: "+row["workflow_commit"],
                "- Complete log identity: "+json.dumps(row.get("complete_log_identity"),sort_keys=True),
                "- Diagnostic error: "+json.dumps(row.get("failure"),sort_keys=True),
                "- Complete original stack retained: "+str(row.get("actual_stack_is_complete")),"",
                "```text",row.get("actual_stack_or_error_lines","No original stack has yet been established."),"```",""]
        text += ["The source and scientific17-pin manifest are unchanged. These receipts do not assert the current exact topic size.",
            "Combined publication is bounded by40000bytes; this is not a current topic capacity audit.",""]
        text="\n".join(text);state["actual_combined_published_receipt_bytes"]=0
        while True:
            raw=(json.dumps(state,ensure_ascii=False,separators=(",",":"),allow_nan=False)+"\n").encode()
            total=len(text.encode())+len(raw)
            if total==state["actual_combined_published_receipt_bytes"]:break
            state["actual_combined_published_receipt_bytes"]=total
        if total>40000:raise ValueError("the two small diagnostic files exceed40000bytes together")
        (report/"actual-result.md").write_text(text);(report/"execution.json").write_bytes(raw)
    snapshot();owned=str(report.relative_to(root));git("add","--sparse","--",owned)
    git("commit","-m","visible-exact: record two actual infrastructure failure logs")
    while True:
        result=git("push","origin","HEAD:refs/heads/main",check=False)
        if result.returncode==0:break
        if not any(word in result.stderr for word in ("non-fast-forward","fetch first","cannot lock ref","remote rejected")):
            raise RuntimeError("small diagnostic push failed outside concurrent-main rebase")
        sync();snapshot();git("add","--sparse","--",owned);git("commit","--amend","--no-edit")
    print(json.dumps(dict(complete=state["complete"],report=owned,new_scientific_subprocesses=0,
        combined_published_receipt_bytes=state["actual_combined_published_receipt_bytes"])),flush=True)
    if not state["complete"]:raise SystemExit(1)
if __name__=="__main__":main()
