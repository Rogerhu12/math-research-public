#!/usr/bin/env python3
"""Independent small local-projection session: source, parameters, run and hashes only.
Astra-ISP-789f; AI-assisted, GPT-6 Astra Pro.
Read explicitly pinned historical inputs. Never use or create Release assets.
Publish only bounded summaries with the last two actual pull records; full
pull provenance remains in the job log and a cumulative logical SHA256.
"""
import base64,hashlib,importlib.metadata,json,os,pathlib,re,shutil,subprocess,sys,tarfile,time
REPO="Rogerhu12/math-research-public"
ROOT="topics/invariant-subspace-problem/"
REQUEST=ROOT+"notes/2026-11-15-r150-local-projection-small-session-request-789f.json"
RULES=["README.md",ROOT+"README.md"]
CWD=pathlib.Path.cwd()
WORK=pathlib.Path(os.environ["RUNNER_TEMP"])/("isp-local-projection-session-"+os.environ["GITHUB_RUN_ID"])
WORK.mkdir(parents=True,exist_ok=True)
TOKEN=os.environ["GH_TOKEN"]
ENV=dict(os.environ)
ENV.update(GIT_CONFIG_COUNT="1",GIT_CONFIG_KEY_0="http.https://github.com/.extraheader",
           GIT_CONFIG_VALUE_0="AUTHORIZATION: basic "+base64.b64encode(("x-access-token:"+TOKEN).encode()).decode(),
           GIT_TERMINAL_PROMPT="0",GIT_EDITOR="true")
RUN=os.environ["GITHUB_RUN_ID"]
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
 global last_read
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
 return origin
def record_handoff():
 path=CWD/(ROOT+"HANDOFF.md");body=path.read_text()
 line="- **最近成功实际 pull 与已读规则提交：** "+last_read+"（"+time.strftime("%Y-%m-%d %H:%M:%S UTC",time.gmtime())+"，临时研究session run"+RUN+"实际pull --rebase，两README无差异；详见notes/r150-local-projection-session-789f/）。"
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
  compact,raw=compact_summary(summary);target.write_bytes(raw)
  record_handoff();git("add","--sparse","--",rel,ROOT+"HANDOFF.md")
  git("commit","--amend","--no-edit")
def bootstrap():
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
 publish(ROOT+"notes/r150-local-projection-session-789f/"+RUN+"-bootstrap.json",summary,
         "ISP: restore pinned historical inputs only in a temporary recovery job")
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
  (scripts/pathlib.Path(entry["path"]).name).write_bytes(raw)
 def expand(value):
  for key,v in contexts.items():value=value.replace("{"+key+"}",v)
  if "{" in value or "}" in value:raise RuntimeError("unknown workspace placeholder")
  return value
 args=[sys.executable,str(scripts/pathlib.Path(task["script"]).name)]+[expand(a) for a in task["argv"]]
 started=time.monotonic();logpath=WORK/(task["id"]+".log")
 with logpath.open("wb") as output:
  try:
   proc=subprocess.run(args,cwd=WORK,env=ENV,stdout=output,stderr=subprocess.STDOUT,timeout=task["timeoutSeconds"])
   exit_code=proc.returncode
  except subprocess.TimeoutExpired:
   exit_code=124

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
 publish(ROOT+"notes/r150-local-projection-session-789f/"+RUN+"-"+task["id"]+".json",summary,"ISP: record actual temporary "+task["id"]+" result and output hashes")
 return summary
def main():
 global request,expected
 git("config","user.name","github-actions[bot]")
 git("config","user.email","41898282+github-actions[bot]@users.noreply.github.com")
 git("fetch","--no-tags","--depth=1","--filter=blob:none","origin",last_read)
 contexts=bootstrap();done={};last_work=time.monotonic();start=last_work
 print("ISP_REMOTE_READY "+json.dumps({"runId":RUN,"temporaryContext":contexts,"persistentLargeData":False}),flush=True)
 while time.monotonic()-start<45*60:
  if git("status","--porcelain").stdout.strip():raise RuntimeError("unexpected dirty research checkout")
  data=api("repos/"+REPO+"/contents/"+REQUEST+"?ref=main")
  candidate=json.loads(base64.b64decode(data["content"]))
  if candidate["rulesGitBlobs"]!=expected:
   request=candidate;expected=candidate["rulesGitBlobs"];pull()
  request=candidate
  for task in request.get("steps",[]):
   if task["id"] not in done:
    done[task["id"]]=step(task,contexts);last_work=time.monotonic()
  if request.get("closeSessionWhenStepsComplete",False):break
  if time.monotonic()-last_work>request.get("maximumIdleSeconds",1200):break
  time.sleep(20)
 print("ISP_REMOTE_SESSION_DONE "+json.dumps({"runId":RUN,"steps":list(done),"largeDataSaved":False}),flush=True)
if __name__=="__main__":
 try:main()
 except Exception as e:
  print("ISP_REMOTE_SESSION_ERROR "+json.dumps({"type":type(e).__name__,"error":clean(e)}),flush=True)
  raise

