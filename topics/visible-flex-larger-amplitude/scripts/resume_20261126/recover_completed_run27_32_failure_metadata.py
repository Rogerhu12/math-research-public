#!/usr/bin/env python3
"""Read six existing completed public job logs on a runner; publish only complete failure metadata.
No mathematical computation, field replay, artifact upload, or raw-log publication.
"""
import hashlib,json,os,re,subprocess,sys,time,urllib.error,urllib.parse,urllib.request
from pathlib import Path
REPOSITORY="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-larger-amplitude"
SOURCES=[(46136563673,140953069476),(46105138690,140856083740),(46108296054,140865899880),(46112781312,140879807850),(46122200592,140908938124),(46125006601,140917553486)]
RULES={"README.md":"539f1ea02feb8a63c5aa734ed560ab6ecbf3ff7f570212e46788413bb072f444",
 TOPIC+"/README.md":"3c1c03b358792b6c9937b95fcfea05b80a572a4da2cce615c4c9832fe929057d"}
ROOT=Path(os.environ["GITHUB_WORKSPACE"]).resolve()
TOKEN=os.environ["GITHUB_TOKEN"]
def sha(data):return hashlib.sha256(data).hexdigest()
def git(*args,check=True):
 p=subprocess.run(["git",*args],cwd=ROOT,capture_output=True,text=True)
 if check and p.returncode:raise RuntimeError("git command failed: "+" ".join(args)+"\n"+p.stdout+p.stderr)
 return p
def sync():
 old=git("rev-parse","HEAD").stdout.strip()
 git("pull","--rebase","origin","main")
 new=git("rev-parse","HEAD").stdout.strip()
 for name,digest in RULES.items():
  data=(ROOT/name).read_bytes()
  if sha(data)!=digest:
   print(git("diff",old,new,"--",name).stdout,flush=True)
   raise RuntimeError("README changed; root must read the exact diff before this diagnostic continues")
 return new
class NoRedirect(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,req,fp,code,msg,headers,newurl):return None
opener=urllib.request.build_opener(NoRedirect)
def api(path,redirect=False):
 if not any(path.startswith("/repos/"+REPOSITORY+"/"+kind) for kind in ("actions/","git/trees/")):raise ValueError("Own public Actions or tree metadata only")
 request=urllib.request.Request("https://api.github.com"+path,
  headers={"Authorization":"Bearer "+TOKEN,"Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28","User-Agent":"math-research-public-original-failure-reader"})
 try:return opener.open(request,timeout=60)
 except urllib.error.HTTPError as e:
  if not redirect or e.code not in (301,302,303,307,308):raise
  location=e.headers.get("Location","")
  parsed=urllib.parse.urlparse(location)
  if parsed.scheme!="https" or not parsed.hostname or parsed.username or parsed.password:
   raise RuntimeError("Invalid official log redirect")
  # The signed official destination receives no GitHub Authorization header.
  return urllib.request.urlopen(urllib.request.Request(location,headers={"User-Agent":"math-research-public-original-failure-reader"}),timeout=60)
def json_api(path):
 with api(path) as r:return json.load(r)
def topic_bytes(note,body):
 tree_sha=git("rev-parse","refs/remotes/origin/main:"+TOPIC).stdout.strip()
 tree=json_api("/repos/"+REPOSITORY+"/git/trees/"+tree_sha+"?recursive=1")
 if tree.get("truncated"):
  entries=[]
  pending=[("",tree_sha)]
  while pending:
   prefix,current=pending.pop()
   part=json_api("/repos/"+REPOSITORY+"/git/trees/"+current)
   if part.get("truncated"):raise RuntimeError("Incomplete public topic tree metadata")
   for entry in part["tree"]:
    if entry["type"]=="tree":pending.append((prefix+entry["path"]+"/",entry["sha"]))
    elif entry["type"]=="blob":entries.append(dict(entry,path=prefix+entry["path"]))
 else:entries=[x for x in tree["tree"] if x["type"]=="blob"]
 if any(not isinstance(x.get("size"),int) for x in entries):raise RuntimeError("Missing whole blob size metadata")
 relative=note[len(TOPIC)+1:]
 previous=sum(x["size"] for x in entries if x["path"]==relative)
 return sum(x["size"] for x in entries)-previous+len(body.encode())
if os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY:raise RuntimeError("Public own repository only")

def recover(SOURCE_RUN,SOURCE_JOB):
 rules_commit=sync()
 run=json_api("/repos/"+REPOSITORY+"/actions/runs/"+str(SOURCE_RUN))
 job=json_api("/repos/"+REPOSITORY+"/actions/jobs/"+str(SOURCE_JOB))
 if job["run_id"]!=SOURCE_RUN or run["run_attempt"]!=1 or job["run_attempt"]!=1:
  raise RuntimeError("Original run/job attempt changed")
 scratch=Path(os.environ["RUNNER_TEMP"])/("original-job-log-"+str(SOURCE_JOB)+".txt")
 with api("/repos/"+REPOSITORY+"/actions/jobs/"+str(SOURCE_JOB)+"/logs",redirect=True) as r:
  with scratch.open("wb") as f:
   while True:
    chunk=r.read(65536)
    if not chunk:break
    f.write(chunk)
 raw=scratch.read_bytes()
 text=raw.decode("utf-8",errors="replace")
 lines=text.splitlines(keepends=True)
 starts=[i for i,line in enumerate(lines) if "Traceback (most recent call last):" in line]
 traces=[]
 for i in starts:
  end=i+1
  while end<len(lines):
   clean=re.sub(r"^\d{4}-\d\d-\d\dT\S+\s+","",lines[end])
   end+=1
   if re.match(r"^[A-Za-z_][A-Za-z_0-9.]*(Error|Exception|Exit|Interrupt)(?::|$)",clean.strip()):
    break
  trace="".join(lines[i:end])
  item={"start_line_one_based":i+1,"end_line_one_based":end,"bytes":len(trace.encode()),
        "sha256":sha(trace.encode()),"complete_observed_trace_segment":True}
  if len(trace.encode())<=24000:item["full_text"]=trace
  else:item["full_text"]=None;item["reason"]="Complete trace remains in the original log; no truncated trace is labelled complete."
  traces.append(item)
 summary_messages=[]
 for number,line in enumerate(lines,1):
  if '"raw_runner_only"' in line:
   clean=re.sub(r"^\d{4}-\d\d-\d\dT\S+\s+","",line).strip()
   try:parsed=json.loads(clean)
   except (ValueError,TypeError):continue
   if isinstance(parsed,dict) and "raw_runner_only" in parsed:
    summary_messages.append({"line_one_based":number,"complete_original_summary":parsed})
 error_lines=[{"line_one_based":i+1,"full_text":line}
  for i,line in enumerate(lines)
  if re.search(r"##\[error\]|RuntimeError:|Traceback \(most recent call last\):",line)]
 selected={"run":{k:run.get(k) for k in ("id","run_attempt","head_sha","status","conclusion","created_at","run_started_at","updated_at","html_url")},
  "job":{k:job.get(k) for k in ("id","run_id","run_attempt","head_sha","status","conclusion","started_at","completed_at","html_url","steps")}}
 out={"schema":"completed-public-job-failure-metadata-v1",
  "scope":"Existing official job log only; no scientific rerun or inference of unreturned mathematical results.",
  "observed_utc":time.strftime("%Y-%m-%d %H:%M:%S UTC",time.gmtime()),
  "repository":REPOSITORY,"original_official":selected,
  "original_log":{"bytes":len(raw),"sha256":sha(raw),"line_count":len(lines),
     "complete_log_only_on_runner":True,"raw_log_committed_or_uploaded":False,
     "decode_replacement_used":raw.decode("utf-8",errors="replace").encode("utf-8")!=raw},
  "complete_trace_segments":traces,"original_error_lines":error_lines,
  "complete_R734_calculation_summary_messages":summary_messages,
  "original_mathematical_results_not_reconstructed":True,
  "original_producer":{"path":TOPIC+"/scripts/resume_20261126/recover_public_run29_failure_metadata.py","git_blob_sha":"dea2cb7f003720de5b52a87cda869a54ef813e5d","fixed_commit":"d9112d40bd141ed3e29e531beaaa022e2ba51a29"},
  "actual_log_recovery_run":os.environ["GITHUB_RUN_ID"],
  "actual_log_recovery_attempt":os.environ["GITHUB_RUN_ATTEMPT"],
  "actual_log_recovery_head":os.environ["GITHUB_SHA"],
  "rules_read_commit":rules_commit,"rules_sha256":RULES,
  "capacity_scope":"Complete current origin/main topic tree blob.size metadata plus this whole new note; no sparse-checkout undercount or lazy git-ls-tree -l blob reads.",
  "source_sha256":sha(Path(__file__).read_bytes()),
  "scientific_computation_executed":False,"fixture_or_new_gate_added":False}
 body=json.dumps(out,ensure_ascii=False,indent=2)+"\n"
 if len(body.encode())>=90000:raise RuntimeError("Complete failure metadata too large; retain original log without publishing a partial result")
 sync()
 NOTE=TOPIC+"/notes/2026-11-28-run"+str(SOURCE_RUN)+"-job-failure-metadata.json"
 dest=ROOT/NOTE
 if dest.exists() and dest.read_text()!=body:raise RuntimeError("Do not overwrite another actual log recovery record")
 dest.write_text(body)
 if topic_bytes(NOTE,body)>200000000:raise RuntimeError("Topic capacity must be freed before publishing complete failure metadata")
 git("config","user.name","math-research Actions")
 git("config","user.email","41898282+github-actions[bot]@users.noreply.github.com")
 git("add",NOTE)
 git("commit","-m","Record actual completed job "+str(SOURCE_JOB)+" failure from full official log")
 helper='!f() { if test "$1" = get; then printf "%s\\n" "username=x-access-token" "password=$GITHUB_TOKEN"; fi; }; f'
 while True:
  result=git("-c","credential.helper=","-c","credential.helper="+helper,"push","origin","main",check=False)
  if result.returncode==0:break
  if not any(x in result.stderr for x in ("fetch first","non-fast-forward","cannot lock ref")):
   raise RuntimeError("Ordinary diagnostic push failed without concurrent movement")
  sync()
  if topic_bytes(NOTE,body)>200000000:raise RuntimeError("Fresh topic capacity exceeded before ordinary retry")
 print(json.dumps({"published_note":NOTE,"bytes":len(body.encode()),"sha256":sha(body.encode()),
  "commit":git("rev-parse","HEAD").stdout.strip(),"original_log_bytes":len(raw),
  "original_log_sha256":sha(raw),"trace_count":len(traces),"error_line_count":len(error_lines)}),flush=True)
 

for source_run,source_job in SOURCES:
 recover(source_run,source_job)
