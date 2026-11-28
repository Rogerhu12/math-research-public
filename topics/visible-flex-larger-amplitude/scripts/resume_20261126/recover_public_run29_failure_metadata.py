#!/usr/bin/env python3
"""Read one existing public job log on a runner; publish only complete failure metadata.
No mathematical computation, field replay, artifact upload, or raw-log publication.
"""
import hashlib,json,os,re,subprocess,sys,time,urllib.error,urllib.parse,urllib.request
from pathlib import Path
REPOSITORY="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-larger-amplitude"
SOURCE_RUN=46110194444
SOURCE_JOB=140871777584
RULES={"README.md":"581402c2148ee8c4ee2af741198ab54a56d71de2b5a7b0d0edf65359121cb102",
 TOPIC+"/README.md":"3c1c03b358792b6c9937b95fcfea05b80a572a4da2cce615c4c9832fe929057d"}
NOTE=TOPIC+"/notes/2026-11-28-run29-original-job-failure-metadata.json"
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
 if not path.startswith("/repos/"+REPOSITORY+"/actions/"):raise ValueError("Public own Actions only")
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
def topic_bytes():
 return sum(x.stat().st_size for x in (ROOT/TOPIC).rglob("*") if x.is_file())
if os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY:raise RuntimeError("Public own repository only")
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
error_lines=[{"line_one_based":i+1,"full_text":line}
 for i,line in enumerate(lines)
 if re.search(r"##\[error\]|RuntimeError:|Traceback \(most recent call last\):",line)]
selected={"run":{k:run.get(k) for k in ("id","run_attempt","head_sha","status","conclusion","created_at","run_started_at","updated_at","html_url")},
 "job":{k:job.get(k) for k in ("id","run_id","run_attempt","head_sha","status","conclusion","started_at","completed_at","html_url","steps")}}
out={"schema":"original-public-run29-job-failure-metadata-v1",
 "scope":"Existing official job log only; no scientific rerun or inference of unreturned mathematical results.",
 "observed_utc":time.strftime("%Y-%m-%d %H:%M:%S UTC",time.gmtime()),
 "repository":REPOSITORY,"original_official":selected,
 "original_log":{"bytes":len(raw),"sha256":sha(raw),"line_count":len(lines),
    "complete_log_only_on_runner":True,"raw_log_committed_or_uploaded":False,
    "decode_replacement_used":raw.decode("utf-8",errors="replace").encode("utf-8")!=raw},
 "complete_trace_segments":traces,"original_error_lines":error_lines,
 "original_mathematical_report_or_second_input_not_reconstructed":True,
 "actual_log_recovery_run":os.environ["GITHUB_RUN_ID"],
 "actual_log_recovery_attempt":os.environ["GITHUB_RUN_ATTEMPT"],
 "actual_log_recovery_head":os.environ["GITHUB_SHA"],
 "rules_read_commit":rules_commit,"rules_sha256":RULES,
 "source_sha256":sha(Path(__file__).read_bytes()),
 "scientific_computation_executed":False,"fixture_or_new_gate_added":False}
body=json.dumps(out,ensure_ascii=False,indent=2)+"\n"
if len(body.encode())>=90000:raise RuntimeError("Complete failure metadata too large; retain original log without publishing a partial result")
sync()
dest=ROOT/NOTE
if dest.exists() and dest.read_text()!=body:raise RuntimeError("Do not overwrite another actual log recovery record")
dest.write_text(body)
if topic_bytes()>200000000:raise RuntimeError("Topic capacity must be freed before publishing complete failure metadata")
git("config","user.name","math-research Actions")
git("config","user.email","41898282+github-actions[bot]@users.noreply.github.com")
git("add",NOTE)
git("commit","-m","Record original run29 job failure from complete runner-side official log")
helper='!f() { if test "$1" = get; then printf "%s\\n" "username=x-access-token" "password=$GITHUB_TOKEN"; fi; }; f'
while True:
 result=git("-c","credential.helper=","-c","credential.helper="+helper,"push","origin","main",check=False)
 if result.returncode==0:break
 if not any(x in result.stderr for x in ("fetch first","non-fast-forward","cannot lock ref")):
  raise RuntimeError("Ordinary diagnostic push failed without concurrent movement")
 sync()
 if topic_bytes()>200000000:raise RuntimeError("Fresh topic capacity exceeded before ordinary retry")
print(json.dumps({"published_note":NOTE,"bytes":len(body.encode()),"sha256":sha(body.encode()),
 "commit":git("rev-parse","HEAD").stdout.strip(),"original_log_bytes":len(raw),
 "original_log_sha256":sha(raw),"trace_count":len(traces),"error_line_count":len(error_lines)}),flush=True)
