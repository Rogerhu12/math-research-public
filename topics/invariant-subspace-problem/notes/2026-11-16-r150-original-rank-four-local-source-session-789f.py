#!/usr/bin/env python3
"""Independent original rank-four local-source session: source, parameters, run and hashes only.
Astra-ISP-789f; AI-assisted, GPT-6 Astra Pro.
Read explicitly pinned historical inputs. Never use or create Release assets.
Publish only execution manifests, excluding all computational result data; full
pull provenance remains in the job log and a cumulative logical SHA256.
"""
import base64,hashlib,importlib.metadata,json,os,pathlib,re,shutil,signal,subprocess,sys,tarfile,time
REPO="Rogerhu12/math-research-public"
ROOT="topics/invariant-subspace-problem/"
REQUEST=ROOT+"notes/2026-11-16-r150-original-rank-four-local-source-session-request-789f.json"
RULES=["README.md",ROOT+"README.md"]
CWD=pathlib.Path.cwd()
WORK=pathlib.Path(os.environ["RUNNER_TEMP"])/("isp-original-rank-four-local-source-session-"+os.environ["GITHUB_RUN_ID"])
WORK.mkdir(parents=True,exist_ok=True)
TOKEN=os.environ["GH_TOKEN"]
ENV=dict(os.environ)
ENV.update(GIT_CONFIG_COUNT="1",GIT_CONFIG_KEY_0="http.https://github.com/.extraheader",
           GIT_CONFIG_VALUE_0="AUTHORIZATION: basic "+base64.b64encode(("x-access-token:"+TOKEN).encode()).decode(),
           GIT_TERMINAL_PROMPT="0",GIT_EDITOR="true")
RUN=os.environ["GITHUB_RUN_ID"]
SESSION_STARTED=time.monotonic()
JOB_STARTED_WALL=float(os.environ.get("R150_RANK_FOUR_LOCAL_JOB_STARTED_UTC",str(time.time())))
SESSION_DEADLINE=SESSION_STARTED+min(80*60,max(0,88*60-(time.time()-JOB_STARTED_WALL)))
last_pull_monotonic=0.0
def sha(p):
 h=hashlib.sha256()
 with pathlib.Path(p).open("rb") as f:
  for b in iter(lambda:f.read(1048576),b""):h.update(b)
 return h.hexdigest()
def clean(s):
 return str(s).replace(TOKEN,"***").replace(ENV["GIT_CONFIG_VALUE_0"],"***")
def call(args,check=True,timeout=120):
 p=subprocess.run(args,cwd=CWD,env=ENV,capture_output=True,text=True,timeout=timeout)
 if check and p.returncode:raise RuntimeError(clean(" ".join(args[:4])+" : "+p.stderr[-2000:]))
 return p
def git(*args,check=True):
 return call(["git",*args],check=check,timeout=300 if args and args[0] in ("fetch","push","pull") else 120)
def api(path,method="GET",check=True):
 p=call(["gh","api","--method",method,path],check=check)
 if p.returncode and "(HTTP 404)" not in p.stderr and "HTTP 404" not in p.stderr:
  raise RuntimeError(clean("GitHub metadata request failed: "+p.stderr[-1000:]))
 return json.loads(p.stdout) if p.returncode==0 and p.stdout.strip() else None
def jwrite(p,x):
 p=pathlib.Path(p);p.parent.mkdir(parents=True,exist_ok=True)
 p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n")
def git_bytes(ref,path):
 p=subprocess.run(["git","show",ref+":"+path],cwd=CWD,env=ENV,capture_output=True,timeout=300)
 if p.returncode:raise RuntimeError(clean(p.stderr.decode(errors="replace")[-2000:]))
 return p.stdout
request=json.loads((CWD/REQUEST).read_text())
expected=request["rulesGitBlobs"]
last_read=request["rulesReadAtCommit"]
pulls=[]
def pull():
 global last_read,last_pull_monotonic
 before=last_read
 p=git("pull","--rebase","origin","main",check=False)
 origin=git("rev-parse","origin/main").stdout.strip()
 if p.returncode:
  conflicts=git("diff","--name-only","--diff-filter=U").stdout.splitlines()
  if conflicts==[ROOT+"HANDOFF.md"]:
   # This worker edits HANDOFF only to record the rule-read commit.
   (CWD/(ROOT+"HANDOFF.md")).write_bytes(git_bytes(origin,ROOT+"HANDOFF.md"))
   git("add","--sparse","--",ROOT+"HANDOFF.md")
   git("rebase","--continue")
  else:raise RuntimeError("pull/rebase failed: "+clean(p.stderr[-1500:]))
 actual={path:git("rev-parse",origin+":"+path).stdout.strip() for path in RULES}
 diff=git("diff",before,origin,"--",*RULES).stdout
 item={"utc":time.strftime("%Y-%m-%d %H:%M:%S UTC",time.gmtime()),"beforeReadCommit":before,
       "originMainAfterPull":origin,"rulesGitBlobs":actual,"rulesDiffer":actual!=expected}
 pulls.append(item);last_read=origin
 print("ISP_ACTUAL_RULE_PULL "+json.dumps(item,ensure_ascii=False),flush=True)
 if actual!=expected:
  print("ISP_SESSION_RULE_DIFF_BEGIN\n"+diff+"\nISP_SESSION_RULE_DIFF_END",flush=True)
  raise RuntimeError("Root must read and apply the actual README changes before this session proceeds")
 last_pull_monotonic=time.monotonic()
 return origin
def record_handoff():
 path=CWD/(ROOT+"HANDOFF.md");body=path.read_text()
 line="- **最近成功实际 pull 与已读规则提交：** "+last_read+"（"+time.strftime("%Y-%m-%d %H:%M:%S UTC",time.gmtime())+"，临时研究session run"+RUN+"实际pull --rebase，两README无差异；详见notes/r150-original-rank-four-local-source-execution-789f/）。"
 body,n=re.subn(r"^- \*\*最近成功实际 pull 与已读规则提交：\*\*.*$",lambda m:line,body,count=1,flags=re.M)
 if n!=1:raise RuntimeError("HANDOFF rule-read marker missing")
 if len(body.encode())>10000:raise RuntimeError("HANDOFF size bound")
 path.write_text(body)
def logical_identity(value):
 raw=json.dumps(value,ensure_ascii=False,separators=(",",":"),sort_keys=True).encode()
 return {"logicalJsonBytes":len(raw),"logicalJsonSHA256":hashlib.sha256(raw).hexdigest(),
         "itemCount":len(value) if isinstance(value,(list,dict)) else None}
def compact_summary(summary):
 # Serialization copies only: no mathematical object or temporary receipt changes.
 out=json.loads(json.dumps(summary))
 out["pulls"]=pulls[-2:]
 out["actualPullCount"]=len(pulls)
 out["allActualPullLogRecords"]=logical_identity(pulls)
 out["lastRulesReadCommit"]=last_read
 result=out.get("result",{})
 params=result.get("parameters",{})
 omitted=[]
 for key in ("completeOldToNewCokernelChange36","sameSelectedSchurFirstCoefficient"):
  if key in params:
   omitted.append({"field":"parameters."+key,**logical_identity(params.pop(key)),
                   "reason":"verified array already represented by the full temporary receipt SHA"})
 def encoded():
  return (json.dumps(out,ensure_ascii=False,indent=2)+"\n").encode()
 # Long regenerable parameter arrays remain only temporary; preserve exact identity.
 for target,prefix in ((params,"parameters."),(result,"result.")):
  for key in sorted(list(target),key=lambda k:len(json.dumps(target[k])),reverse=True):
   if len(encoded())<94000:break
   if key in ("parameters","events") or not isinstance(target[key],(list,dict)):continue
   if len(json.dumps(target[key]))<2048:continue
   omitted.append({"field":prefix+key,**logical_identity(target.pop(key)),
                   "reason":"bounded source-parameter-run-hash summary"})
 if omitted:
  result["serializedArrayIdentities"]=omitted
 out["summaryExcludesRecomputableArraysOnly"]=bool(omitted)
 raw=encoded()
 if len(raw)>=100000:raise RuntimeError("small summary remains over100KB before any checkout write")
 return out,raw
def publish(rel,summary,message):
 # Root rule15: computational outputs stay in temporary storage and job log.
 # The committed record retains only script/parameters/run/output identities.
 summary={k:v for k,v in summary.items() if k not in ("result",)}
 summary["computationalOutputPersisted"]=False
 pull()
 compact,raw=compact_summary(summary)
 target=CWD/rel;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(raw)
 record_handoff();git("add","--sparse","--",rel,ROOT+"HANDOFF.md")
 git("commit","-m",message)
 while True:
  p=git("push","origin","HEAD:refs/heads/main",check=False)
  if p.returncode==0:
   commit=git("rev-parse","HEAD").stdout.strip()
   print("ISP_SESSION_PUBLICATION "+json.dumps({"runId":RUN,"commit":commit,"summary":rel,"summaryBytes":len(raw),"lastRulesReadCommit":last_read}),flush=True)
   return commit
  msg=(p.stdout+p.stderr).lower()
  if not any(s in msg for s in ("non-fast-forward","fetch first","[rejected]","failed to update ref","cannot lock ref")):
   raise RuntimeError("push failed for a reason other than non-fast-forward: "+clean(msg[-1500:]))
  pull()
  # A rebase can remove directories excluded by sparse checkout.
  # Recreate the exact authorized receipt parent before every retry write.
  compact,raw=compact_summary(summary);target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(raw)
  record_handoff();git("add","--sparse","--",rel,ROOT+"HANDOFF.md")
  git("commit","--amend","--no-edit")
def bootstrap():
 if sha(__file__)!=request["sessionScriptSHA256"]:raise RuntimeError("Pinned independent session script identity")
 pull()
 contexts={"work":str(WORK),"repo":str(CWD),"scripts":str(WORK/"scripts")}
 fetched=set();verified=[]
 for item in request.get("historicalInputs",[]):
  ref=item["historicalCommit"];path=item["historicalPath"]
  if not re.fullmatch(r"[0-9a-f]{40}",ref) or not path.startswith(ROOT+"notes/"):
   raise RuntimeError("historical input must be pinned inside the authorized topic")
  if ref not in fetched:
   git("fetch","--no-tags","--depth=1","--filter=blob:none","origin",ref);fetched.add(ref)
  raw=git_bytes(ref,path)
  if len(raw)!=item["bytes"] or hashlib.sha256(raw).hexdigest()!=item["sha256"]:
   raise RuntimeError("historical input identity mismatch: "+item["key"])
  rel=pathlib.PurePosixPath(item["scope"])/item["file"]
  if rel.is_absolute() or ".." in rel.parts:raise RuntimeError("unsafe historical destination")
  target=WORK/"inputs"/rel;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(raw)
  contexts[item["scope"]+"_dir"]=str(WORK/"inputs"/item["scope"])
  contexts[item["key"].replace("-","_")]=str(target)
  verified.append({k:item[k] for k in ("key","bytes","sha256","historicalCommit","historicalPath")})
 if "point" in contexts:contexts["selected_model"]=contexts["point"]
 if "model" in contexts:contexts["native_model"]=contexts["model"]
 jwrite(WORK/"context.json",contexts)
 summary={"format":"isp-minimal-historical-recovery-bootstrap-v1","runId":RUN,
          "sourceCommit":git("rev-parse","HEAD").stdout.strip(),"sessionScriptSHA256":sha(__file__),
          "historicalInputsVerified":verified,"historicalInputCount":len(verified),
          "releaseAssetsUsedOrCreated":False,"largeDataUploadedOrCommitted":False,
          "workingDataTemporaryOnly":True}
 publish(ROOT+"notes/r150-original-rank-four-local-source-execution-789f/"+RUN+"-bootstrap.json",summary,
         "ISP: start the original parameter-module source job with temporary data only")
 return contexts
def sanitise(receipt):
 scalar={k:v for k,v in receipt.items() if isinstance(v,(str,int,float,bool)) or v is None}
 for k in ("inputs","parameters","characteristicZeroSelectedRankBounds","characteristicZeroSelectedColumnsFull4367RankBounds"):
  if k in receipt:scalar[k]=receipt[k]
 scalar["events"]=[{k:v for k,v in e.items() if isinstance(v,(str,int,float,bool)) or v is None} for e in receipt.get("events",[])]
 return scalar
def step(task,contexts):
 pull();source=git("rev-parse","HEAD").stdout.strip()
 scripts=pathlib.Path(contexts["scripts"]);scripts.mkdir(parents=True,exist_ok=True)
 for entry in task.get("sources",[])+[{"path":task["script"],"sha256":task["scriptSHA256"]}]:
  if not entry["path"].startswith(ROOT+"notes/"):raise RuntimeError("script outside authorized topic")
  raw=git_bytes(source,entry["path"])
  if len(raw)>100000 or hashlib.sha256(raw).hexdigest()!=entry["sha256"]:raise RuntimeError("pinned source mismatch")
  if entry["path"].endswith(".py"):
   compile(raw,entry["path"],"exec")  # Actual syntax gate before any mathematical program is started.
  (scripts/pathlib.Path(entry["path"]).name).write_bytes(raw)
 def expand(value):
  for key,v in contexts.items():value=value.replace("{"+key+"}",v)
  if "{" in value or "}" in value:raise RuntimeError("unknown workspace placeholder")
  return value
 args=[sys.executable,str(scripts/pathlib.Path(task["script"]).name)]+[expand(a) for a in task["argv"]]
 started=time.monotonic();logpath=WORK/(task["id"]+".log")
 if started+task["timeoutSeconds"]+120>SESSION_DEADLINE:
  raise RuntimeError("Insufficient bounded session time for the complete requested attempt; no new mathematical program started")
 with logpath.open("wb") as output:
  proc=subprocess.Popen(args,cwd=WORK,env=ENV,stdout=output,stderr=subprocess.STDOUT,start_new_session=True)
  def terminate_group():
   if proc.poll() is not None:return
   try:os.killpg(proc.pid,signal.SIGTERM)
   except ProcessLookupError:pass
   try:proc.wait(timeout=10)
   except subprocess.TimeoutExpired:
    try:os.killpg(proc.pid,signal.SIGKILL)
    except ProcessLookupError:pass
    proc.wait()
  try:
   while True:
    if proc.poll() is not None:
     exit_code=proc.returncode;break
    if time.monotonic()-started>=task["timeoutSeconds"]:
     terminate_group();exit_code=124;break
    # Long arithmetic uses immutable temporary scripts. Pull/read both READMEs
    # during it as well, before the 30-minute rule interval can expire.
    if time.monotonic()-last_pull_monotonic>=28*60:pull()
    try:proc.wait(timeout=min(20,max(.1,task["timeoutSeconds"]-(time.monotonic()-started))))
    except subprocess.TimeoutExpired:pass
  except BaseException:
   terminate_group();raise

 receipt_path=pathlib.Path(expand(task["receiptPath"]))
 if receipt_path.is_file():
  raw=receipt_path.read_bytes();actual=json.loads(raw)
 else:
  actual={"status":"failed-no-mathematical-receipt","receiptAbsent":True,
          "errorLogTail":clean(logpath.read_text(errors="replace")[-2000:])}
  raw=None
 summary={"format":"isp-temporary-research-step-source-parameters-run-sha256-v1","runId":RUN,
          "stepId":task["id"],"executionSourceCommit":source,"script":task["script"],
          "scriptSHA256":task["scriptSHA256"],"argvTemplate":task["argv"],
          "timeoutSeconds":task["timeoutSeconds"],"exitCode":exit_code,
          "wallSeconds":time.monotonic()-started,"fullTemporaryReceiptBytes":len(raw) if raw is not None else None,
          "fullTemporaryReceiptSHA256":hashlib.sha256(raw).hexdigest() if raw is not None else None,
          "result":sanitise(actual),"largeDataUploadedOrCommitted":False,
          "python":sys.version,"pythonFlint":importlib.metadata.version("python-flint")}
 print("ISP_REMOTE_STEP "+json.dumps(compact_summary(summary)[0],ensure_ascii=False),flush=True)
 publish(ROOT+"notes/r150-original-rank-four-local-source-execution-789f/"+RUN+"-"+task["id"]+".json",summary,"ISP: record actual temporary "+task["id"]+" result and output hashes")
 return summary
def main():
 global request,expected
 git("config","user.name","github-actions[bot]")
 git("config","user.email","41898282+github-actions[bot]@users.noreply.github.com")
 git("fetch","--no-tags","--depth=1","--filter=blob:none","origin",last_read)
 if importlib.metadata.version("python-flint")!="0.9.0":raise RuntimeError("Pinned arithmetic runtime version")
 contexts=bootstrap();done={};last_work=time.monotonic();start=last_work
 print("ISP_REMOTE_READY "+json.dumps({"runId":RUN,"temporaryContext":contexts,"persistentLargeData":False}),flush=True)
 last_periodic_rule_check=time.monotonic()
 while time.monotonic()<SESSION_DEADLINE:
  if time.monotonic()-last_pull_monotonic>=28*60:
   publish(ROOT+"notes/r150-original-rank-four-local-source-execution-789f/"+RUN+"-periodic-rules-"+str(len(pulls))+".json",
           {"format":"isp-periodic-actual-readme-pull-v1","runId":RUN,"largeDataUploadedOrCommitted":False},
           "ISP: record periodic actual pull and both README identities")
   last_periodic_rule_check=time.monotonic()
  if git("status","--porcelain").stdout.strip():raise RuntimeError("unexpected dirty research checkout")
  data=api("repos/"+REPO+"/contents/"+REQUEST+"?ref=main")
  candidate=json.loads(base64.b64decode(data["content"]))
  if candidate["rulesGitBlobs"]!=expected:
   request=candidate;expected=candidate["rulesGitBlobs"];pull()
  request=candidate
  for task in request.get("steps",[]):
   dependencies=task.get("requires",[])
   if task["id"] not in done and all(k in done and done[k]["exitCode"]==0 for k in dependencies):
    schedule=task.get("budgetResumeSeconds")
    attempts=len(schedule) if schedule is not None else int(task.get("budgetResumeAttempts",1))
    if not 1<=attempts<=4:raise RuntimeError("bounded same-binding resume count")
    if schedule is not None:
     if not all(isinstance(x,int) and 1<=x<=1800 for x in schedule):raise RuntimeError("bounded attempt budgets")
     if any(schedule[i]>=schedule[i+1] for i in range(len(schedule)-1)):raise RuntimeError("resume budgets must strictly increase")
     if task["argv"].count("--seconds")!=1:raise RuntimeError("one exact source budget argument")
     budget_at=task["argv"].index("--seconds")+1
     if int(task["argv"][budget_at])!=schedule[0]:raise RuntimeError("first attempt matches the frozen requested budget")
     padding=int(task.get("budgetOuterPaddingSeconds",60))
     if not 30<=padding<=120:raise RuntimeError("bounded outer timeout padding")
    def progress_signature():
     guard=task.get("budgetResumeWholeProgress")
     if guard is None:return None
     path=guard["manifestPath"]
     for key,value in contexts.items():path=path.replace("{"+key+"}",value)
     p=pathlib.Path(path)
     if "{" in path or "}" in path or not p.is_relative_to(WORK):raise RuntimeError("unsafe whole-prefix resume path")
     if not p.is_file():return None
     data=json.loads(p.read_bytes())
     if data.get("format")!=guard["format"] or data.get("binding")!=guard["binding"]:
      raise RuntimeError("same-binding whole candidate resume gate")
     # The materialized input and a running GB are not mathematical progress.
     if "candidate" not in data:return None
     signature={"candidate":data["candidate"]["data"],
                "sourceCandidate":data.get("sourceCandidate",{}).get("data"),
                "targetReduction":data.get("targetReduction",{}).get("zero"),
                "sourceTexts":data.get("sourceTexts",[]),
                "parsedSources":data.get("parsedSources",[]),
                "phases":data.get("phases",{})}
     return logical_identity(signature)["logicalJsonSHA256"]
    for attempt in range(attempts):
     before_progress=progress_signature()
     current=dict(task);current["argv"]=list(task["argv"])
     if attempt:current["id"]=task["id"]+"-resume"+str(attempt+1)
     if schedule is not None:
      current["argv"][budget_at]=str(schedule[attempt])
      current["timeoutSeconds"]=schedule[attempt]+padding
     done[task["id"]]=step(current,contexts);last_work=time.monotonic()
     # Only a genuine source budget75 continues. No syntax, input, memory or
     # mathematical verification failure is silently retried with more time.
     if done[task["id"]]["exitCode"]!=75:break
     if task.get("budgetResumeWholeProgress") is not None:
      after_progress=progress_signature()
      if after_progress is None or after_progress==before_progress:
       print("ISP_WHOLE_PREFIX_RESUME_STOP "+json.dumps({"stepId":task["id"],"attempt":attempt+1,
           "reason":"no newly complete candidate or verification prefix","previousSignature":before_progress,
           "actualSignature":after_progress}),flush=True)
       break
  if request.get("closeSessionWhenStepsComplete",False):break
  if time.monotonic()-last_work>request.get("maximumIdleSeconds",1200):break
  time.sleep(20)
 print("ISP_REMOTE_SESSION_DONE "+json.dumps({"runId":RUN,"steps":list(done),"largeDataSaved":False}),flush=True)
 missing=[t["id"] for t in request.get("steps",[]) if t["id"] not in done]
 failed=[k for k,v in done.items() if v["exitCode"]!=0]
 if missing or failed:raise RuntimeError("Requested finite job did not complete: missing="+str(missing)+" failed="+str(failed))
if __name__=="__main__":
 try:main()
 except Exception as e:
  print("ISP_REMOTE_SESSION_ERROR "+json.dumps({"type":type(e).__name__,"error":clean(e)}),flush=True)
  raise

