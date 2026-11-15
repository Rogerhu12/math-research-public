#!/usr/bin/env python3
"""Temporary ISP research session. Persist only source, parameters, run and hashes.
Astra-ISP-789f; AI-assisted, GPT-6 Astra Pro.
Existing pre-rule temporary assets are consumed once and deleted. No large
result, checkpoint, binary or archive is uploaded or committed.
"""
import base64,hashlib,importlib.metadata,json,os,pathlib,re,shutil,subprocess,sys,tarfile,time
REPO="Rogerhu12/math-research-public"
ROOT="topics/invariant-subspace-problem/"
REQUEST=ROOT+"notes/2026-11-15-r150-infinity-remote-session-request-789f.json"
INPUTS=ROOT+"notes/2026-11-15-r150-selected-infinity-resume486-input-locations-789f.json"
RULES=["README.md",ROOT+"README.md"]
CWD=pathlib.Path.cwd()
WORK=pathlib.Path(os.environ["RUNNER_TEMP"])/("isp-infinity-session-"+os.environ["GITHUB_RUN_ID"])
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
 if actual!=expected:
  print("ISP_SESSION_RULE_DIFF_BEGIN\n"+diff+"\nISP_SESSION_RULE_DIFF_END",flush=True)
  raise RuntimeError("Root must read and apply the actual README changes before this session proceeds")
 return origin
def record_handoff():
 path=CWD/(ROOT+"HANDOFF.md");body=path.read_text()
 line="- **最近成功实际 pull 与已读规则提交：** "+last_read+"（"+time.strftime("%Y-%m-%d %H:%M:%S UTC",time.gmtime())+"，临时研究session run"+RUN+"实际pull --rebase，两README无差异；详见notes/r150-infinity-remote-session-789f/）。"
 body,n=re.subn(r"^- \*\*最近成功实际 pull 与已读规则提交：\*\*.*$",lambda m:line,body,count=1,flags=re.M)
 if n!=1:raise RuntimeError("HANDOFF rule-read marker missing")
 if len(body.encode())>10000:raise RuntimeError("HANDOFF size bound")
 path.write_text(body)
def publish(rel,summary,message,deletions=None):
 origin=pull()
 deletions=deletions or {}
 for path,blob in deletions.items():
  current=git("rev-parse",origin+":"+path,check=False)
  if current.returncode or current.stdout.strip()!=blob:
   raise RuntimeError("a data path changed after the inventory; preserve it for root review: "+path)
 summary["pulls"]=pulls.copy();summary["lastRulesReadCommit"]=last_read
 target=CWD/rel;jwrite(target,summary)
 if target.stat().st_size>=100000:raise RuntimeError("only small execution summaries may be published")
 # Any deletion here is already bound to the current exact Git tree.
 if deletions:git("rm","--cached","--sparse","--ignore-unmatch","--",*deletions)
 record_handoff();git("add","--sparse","--",rel,ROOT+"HANDOFF.md")
 git("commit","-m",message)
 while True:
  p=git("push","origin","HEAD:refs/heads/main",check=False)
  if p.returncode==0:
   commit=git("rev-parse","HEAD").stdout.strip()
   print("ISP_SESSION_PUBLICATION "+json.dumps({"runId":RUN,"commit":commit,"summary":rel,"lastRulesReadCommit":last_read}),flush=True)
   return commit
  msg=(p.stdout+p.stderr).lower()
  if not any(s in msg for s in ("non-fast-forward","fetch first","[rejected]","failed to update ref","cannot lock ref")):
   raise RuntimeError("push failed for a reason other than non-fast-forward: "+clean(msg[-1000:]))
  pull()
  summary["pulls"]=pulls.copy();summary["lastRulesReadCommit"]=last_read;jwrite(target,summary)
  record_handoff();git("add","--sparse","--",rel,ROOT+"HANDOFF.md")
  git("commit","--amend","--no-edit")
def topic_tree(ref):
 root=api("repos/"+REPO+"/git/trees/"+ref)["tree"]
 topics=next(x["sha"] for x in root if x["path"]=="topics")
 subtree=api("repos/"+REPO+"/git/trees/"+topics)["tree"]
 topic=next(x["sha"] for x in subtree if x["path"]=="invariant-subspace-problem")
 data=api("repos/"+REPO+"/git/trees/"+topic+"?recursive=1")
 if data.get("truncated"):raise RuntimeError("topic inventory truncated")
 return {x["path"]:x for x in data["tree"] if x["type"]=="blob"}
def data_path(x):
 path=x["path"]
 return path.startswith("notes/") and bool(re.search(r"\.part\d+$|\.gz$|\.bin(?:[-.].*)?$|\.np[yz]$|\.zip$|\.tar$|\.dat$|\.csv$|\.tsv$",path,re.I))
def bootstrap():
 pull()
 loc=json.loads((CWD/INPUTS).read_text())
 asset=next(x for x in request["temporaryAssetsToRemove"] if x["id"]==749870028)
 release_dir=WORK/"one-time-input";release_dir.mkdir()
 call(["gh","release","download","data-invariant-subspace-problem","--repo",REPO,
       "--pattern",asset["name"],"--dir",str(release_dir)],timeout=600)
 archive=release_dir/asset["name"]
 if archive.stat().st_size!=asset["bytes"] or sha(archive)!=asset["sha256"]:raise RuntimeError("temporary p486 archive mismatch")
 extracted=WORK/"p486-restore";extracted.mkdir()
 with tarfile.open(archive,"r:") as tf:
  for member in tf:
   name=pathlib.PurePosixPath(member.name)
   if name.is_absolute() or ".." in name.parts or not (member.isfile() or member.isdir()):
    raise RuntimeError("unsafe archive member")
   target=extracted.joinpath(*name.parts)
   if member.isdir():target.mkdir(parents=True,exist_ok=True);continue
   target.parent.mkdir(parents=True,exist_ok=True)
   with tf.extractfile(member) as src,target.open("wb") as dst:shutil.copyfileobj(src,dst,1048576)
 archive.unlink()
 contexts={"work":str(WORK),"repo":str(CWD),"scripts":str(WORK/"scripts")}
 for item in loc["currentInputs"]:
  candidates=[x for x in extracted.rglob(pathlib.Path(item["file"]).name)
              if x.is_file() and x.stat().st_size==item["bytes"] and sha(x)==item["sha256"]]
  if len(candidates)!=1:raise RuntimeError("unique verified current input missing: "+item["key"])
  contexts[item["key"].replace("-","_")]=str(candidates[0])
 contexts["p486"]=str(pathlib.Path(contexts["paid_exact_kernels"]).parent)
 historical=loc["historicalInputs"][0]["historicalCommit"]
 git("fetch","--no-tags","--depth=1","--filter=blob:none","origin",historical)
 for item in loc["historicalInputs"]:
  raw=git_bytes(item["historicalCommit"],item["historicalPath"])
  if len(raw)!=item["bytes"] or hashlib.sha256(raw).hexdigest()!=item["sha256"]:raise RuntimeError("historical input mismatch "+item["key"])
  target=WORK/"inputs"/item["scope"]/item["file"];target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(raw)
  contexts[item["scope"]+"_dir"]=str(WORK/"inputs"/item["scope"])
  contexts[item["key"].replace("-","_")]=str(target)
 contexts["certificates"]=contexts["paid_exact_kernels"]
 contexts["selected_model"]=contexts["point"];contexts["native_model"]=contexts["model"]
 # Current mathematical inputs are now in this job's temporary workspace.
 # Follow the latest rule immediately; do not keep the old persistent assets.
 removed=[]
 for a in request["temporaryAssetsToRemove"]:
  actual=api("repos/"+REPO+"/releases/assets/"+str(a["id"]),check=False)
  if actual is None:removed.append({"id":a["id"],"alreadyAbsent":True});continue
  if actual["name"]!=a["name"] or actual["size"]!=a["bytes"] or actual.get("digest")!="sha256:"+a["sha256"]:
   raise RuntimeError("asset identity changed; refuse unrelated deletion")
  api("repos/"+REPO+"/releases/assets/"+str(a["id"]),"DELETE")
  removed.append({"id":a["id"],"name":a["name"],"bytes":a["bytes"],"sha256":a["sha256"],"deleted":True})
 # Remove only unchanged regenerable old data not already removed by coordination.
 origin=pull();current=topic_tree(origin);old=topic_tree("b6dd686c404c15cc7744c5c26f32862055ea3c67")
 deletes={ROOT+path:x["sha"] for path,x in current.items() if data_path(x) and path in old and old[path]["sha"]==x["sha"]}
 before=sum(x.get("size",0) for x in current.values())
 after=before-sum(current[x[len(ROOT):]].get("size",0) for x in deletes)
 summary={"format":"isp-current-rule15-temporary-input-and-cleanup-v1","runId":RUN,"sourceCommit":os.environ["GITHUB_SHA"],
          "rulesReadAtCommit":last_read,"temporaryP486ArchiveSHA256":asset["sha256"],
          "allCurrentInputsVerified":True,"allHistoricalInputsVerified":True,
          "temporaryAssetDeletions":removed,"oldMainDeletionCount":len(deletes),
          "oldMainDeletionPathBlobSHA256":hashlib.sha256(json.dumps([(x,current[x[len(ROOT):]]["sha"]) for x in deletes],separators=(",",":")).encode()).hexdigest(),
          "topicBytesBeforeThisCleanup":before,"topicBytesAfterDataDeletionBeforeSmallSummary":after,"topicWithin200000000":after<=200000000,
          "largeDataUploadedOrCommitted":False,"workingDataTemporaryOnly":True}
 if after>200000000:raise RuntimeError("topic still exceeds 200 MB after known data cleanup")
 publish(ROOT+"notes/r150-infinity-remote-session-789f/"+RUN+"-bootstrap.json",summary,"ISP: apply current reproducible-data rule and retain only temporary research inputs",deletes)
 jwrite(WORK/"context.json",contexts)
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
  proc=subprocess.run(args,cwd=WORK,env=ENV,stdout=output,stderr=subprocess.STDOUT,timeout=task["timeoutSeconds"])
 receipt_path=pathlib.Path(expand(task["receiptPath"]))
 if not receipt_path.is_file():raise RuntimeError("task has no actual receipt: "+clean(logpath.read_text(errors="replace")[-2000:]))
 raw=receipt_path.read_bytes();actual=json.loads(raw)
 summary={"format":"isp-temporary-research-step-source-parameters-run-sha256-v1","runId":RUN,
          "stepId":task["id"],"executionSourceCommit":source,"script":task["script"],
          "scriptSHA256":task["scriptSHA256"],"argvTemplate":task["argv"],
          "timeoutSeconds":task["timeoutSeconds"],"exitCode":proc.returncode,
          "wallSeconds":time.monotonic()-started,"fullTemporaryReceiptBytes":len(raw),
          "fullTemporaryReceiptSHA256":hashlib.sha256(raw).hexdigest(),
          "result":sanitise(actual),"largeDataUploadedOrCommitted":False,
          "python":sys.version,"pythonFlint":importlib.metadata.version("python-flint")}
 print("ISP_REMOTE_STEP "+json.dumps(summary,ensure_ascii=False),flush=True)
 publish(ROOT+"notes/r150-infinity-remote-session-789f/"+RUN+"-"+task["id"]+".json",summary,"ISP: record actual temporary "+task["id"]+" result and output hashes")
 return summary
def main():
 global request,expected
 git("config","user.name","github-actions[bot]")
 git("config","user.email","41898282+github-actions[bot]@users.noreply.github.com")
 git("fetch","--no-tags","--depth=1","--filter=blob:none","origin",last_read)
 contexts=bootstrap();done={};last_work=time.monotonic();start=last_work
 print("ISP_REMOTE_READY "+json.dumps({"runId":RUN,"temporaryContext":contexts,"persistentLargeData":False}),flush=True)
 while time.monotonic()-start<340*60:
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
