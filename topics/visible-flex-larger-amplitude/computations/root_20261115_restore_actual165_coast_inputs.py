#!/usr/bin/env python3
"""Request180: recover original165 inputs from one immutable official log.
Transport, JSON and byte identities only. No mathematical module is imported.
The 1.48GB log is streamed, never retained; only three necessary original
members are written under this request-owned temporary directory.
"""
from __future__ import annotations
import argparse, hashlib, json, os, re, signal, sys, time, traceback
from pathlib import Path
import urllib.error, urllib.parse, urllib.request

REPOSITORY="Rogerhu12/math-research-public"
SCHEMA="request180-original165-complete-input-recovery-v1"
REQUEST_SCHEMA="request180-accurate-R323-coast-three-coefficient-repair-v1"
RUN=43736208020
JOB=132879253906
SOURCE_COMMIT="1f2ec637430e5c6b27b1a93720e106539281a156"
LOG_BYTES=1486048285
LOG_SHA="4ab8c6d688a27869353bb428288d467502c7aed6ad8cd96140a6cfaea508aea2"
MEMBERS={
 "complete-input-and-rebuilt-definition-binding":("original-input-binding.json",62398,"996593f3a615c3694596463c949990a4967cc5c5a1bf48b100fbc4e149e73e48"),
 "complete-target-result":("original-target-result.json",105512,"e5ec825f39c2f57aa6f04b46c56371b6876670a04ac7c5c9129bdcc80af2c619"),
 "complete-construction-summary":("original-construction-summary.json",27207,"6ff7fb33455be8dbc4eef1eb819a8f7b90329c8575c442dc810c83db13117fb8")
}
TIMESTAMP=re.compile(rb"^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d+)?Z ")
MAX_LINE=1048576

def require(ok,message):
 if not ok:raise ValueError(message)

def sha(raw):return hashlib.sha256(raw).hexdigest()

def canonical(value):
 return (json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=True,allow_nan=False)+"\n").encode("ascii")

def write(path,value):
 raw=canonical(value);path.write_bytes(raw)
 return dict(file=path.name,bytes=len(raw),sha256=sha(raw))

def bounded_emit(value):
 raw=canonical(value)
 require(len(raw)<=90000,"One small metadata result; no data-splitting fallback")
 print(raw.decode("ascii"),end="",flush=True)

class ResourceStop(RuntimeError):pass

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):
        return None


def api_json(path,token):
    url="https://api.github.com/repos/"+REPOSITORY+path
    headers={"Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28",
        "User-Agent":"request180-original165-input-recovery","Accept-Encoding":"identity"}
    if token:headers["Authorization"]="Bearer "+token
    request=urllib.request.Request(url,headers=headers)
    with urllib.request.build_opener(NoRedirect()).open(request,timeout=45) as response:
        raw=response.read(2097153)
        require(len(raw)<=2097152,"Bounded official metadata response")
        require(response.status==200,"Official metadata returned200")
        value=json.loads(raw)
    return value,dict(endpoint=path,bytes=len(raw),sha256=sha(raw))


def open_log(token):
    """Only the official API receives a token; the redirect request never does."""
    url="https://api.github.com/repos/"+REPOSITORY+"/actions/jobs/"+str(JOB)+"/logs"
    headers={"Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28",
        "User-Agent":"request180-original165-input-recovery","Accept-Encoding":"identity"}
    if token:headers["Authorization"]="Bearer "+token
    request=urllib.request.Request(url,headers=headers)
    opener=urllib.request.build_opener(NoRedirect())
    try:
        response=opener.open(request,timeout=60)
    except urllib.error.HTTPError as error:
        if error.code not in (301,302,303,307,308):raise
        location=error.headers.get("Location")
        require(isinstance(location,str),"Official job log redirect has a location")
        target=urllib.parse.urlparse(location)
        require(target.scheme=="https" and target.hostname and not target.username,
            "Only the HTTPS location returned by the official job log API is used")
        # Do not put the signed URL or original bearer token in any output.
        redirected=urllib.request.Request(location,headers={
            "User-Agent":"request180-original165-input-recovery","Accept-Encoding":"identity"})
        response=urllib.request.urlopen(redirected,timeout=60)
        return response,dict(official_job_logs_endpoint=url,official_redirect_status=error.code,
            bearer_token_not_forwarded_to_redirect=True,signed_URL_not_logged=True,
            downloaded_from_official_redirect=True)
    return response,dict(official_job_logs_endpoint=url,official_redirect_status=None,
        bearer_token_not_forwarded_to_redirect=True,signed_URL_not_logged=True,
        downloaded_from_official_redirect=False)



class Scan:
 def __init__(self,out,deadline,maximum_bytes):
  self.out=out;self.deadline=deadline;self.maximum_bytes=maximum_bytes
  self.h=hashlib.sha256();self.bytes=0;self.lines=0;self.bom_lines=0
  self.parts={};self.members={};self.duplicates={};self.construction=None
  self.complete=False
 def check(self):
  if time.monotonic()>=self.deadline:raise ResourceStop("original-log-wall-budget")
  if self.bytes>self.maximum_bytes:raise ResourceStop("original-log-byte-budget")
 def accept(self,label,raw,location):
  filename,size,digest=MEMBERS[label]
  require(len(raw)==size and sha(raw)==digest,"Original member bytes/SHA: "+label)
  require(raw.endswith(b"\n") and raw.isascii(),"Original canonical ASCII member including LF")
  value=json.loads(raw)
  if label in self.members:
   require((self.out/filename).read_bytes()==raw,"Repeated original member differs")
   self.duplicates[label]=self.duplicates.get(label,0)+1
   return
  (self.out/filename).write_bytes(raw)
  self.members[label]=dict(file=filename,bytes=size,sha256=digest,source_location=location)
 def line(self,raw):
  self.check();require(len(raw)<=MAX_LINE,"Bounded original physical line")
  offset=self.bytes;self.h.update(raw);self.bytes+=len(raw);self.lines+=1
  line=raw
  if line.startswith(b"\xef\xbb\xbf"):line=line[3:];self.bom_lines+=1
  line=TIMESTAMP.sub(b"",line,count=1)
  payload=line.rstrip(b"\r\n")
  location=dict(physical_line=self.lines,raw_byte_start=offset,raw_line_bytes=len(raw),raw_line_sha256=sha(raw))
  if payload==b"BEGIN_REQUEST147_CONTINUOUS_NINE_CONSTRUCTION_SUMMARY":
   require(self.construction is None,"Nonoverlapping original construction frame")
   self.construction=[];return
  if self.construction is not None:
   if payload==b"END_REQUEST147_CONTINUOUS_NINE_CONSTRUCTION_SUMMARY":
    frame=b"".join(self.construction);self.construction=None
    value=json.loads(frame)
    if "actual_recipe" in value:self.accept("complete-construction-summary",frame,location)
    return
   self.construction.append(payload+b"\n")
   require(sum(map(len,self.construction))<=90000,"Original bounded construction summary")
   return
  if b"request165_complete_metadata_" not in payload and b"request147_complete_metadata_" not in payload:return
  if not payload.lstrip().startswith(b"{"):return
  value=json.loads(payload);event=value.get("event")
  label=value.get("label")
  if label not in MEMBERS:return
  if event in ("request165_complete_metadata_begin","request147_complete_metadata_group"):
   require(label not in self.parts,"No overlapping original metadata groups")
   self.parts[label]=dict(begin=value,data=[],index=0,location=location)
  elif event in ("request165_complete_metadata_segment","request147_complete_metadata_segment"):
   state=self.parts.get(label);require(state is not None,"Original segment has begin")
   require(type(value["index"]) is int and value["index"]==state["index"]
      and value["segments"]==state["begin"]["segments"],"Complete original segment order")
   data=value["data"];require(isinstance(data,str) and data.isascii(),"Original ASCII data")
   state["data"].append(data);state["index"]+=1
   if state["index"]==state["begin"]["segments"]:
    joined="".join(state["data"]).encode("ascii");begin=state["begin"]
    require(len(joined)==begin["bytes"] and sha(joined)==begin["sha256"],"Original group identity")
    self.accept(label,joined,dict(begin=state["location"],end=location,segments=state["index"]))
    del self.parts[label]
 def finish(self):
  require(self.complete and not self.parts and self.construction is None,"Original stream and selected frames complete")
  require(self.bytes==LOG_BYTES and self.h.hexdigest()==LOG_SHA,"Whole immutable original165 log bytes/SHA")
  require(set(self.members)==set(MEMBERS),"All three original required members recovered")
 def record(self):
  return dict(complete=self.complete,bytes=self.bytes,sha256=self.h.hexdigest(),physical_lines=self.lines,
   line_prefix_BOM_count=self.bom_lines,normalization="Parsing view only: one physical-line-leading BOM, then one anchored GitHub timestamp; body unchanged",
   raw_log_saved=False,members=self.members,identical_duplicate_members=self.duplicates,
   incomplete_selected_groups=sorted(self.parts),construction_frame_incomplete=self.construction is not None)

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument("--request",type=Path,required=True);ap.add_argument("--out",type=Path,required=True)
 args=ap.parse_args()
 require(os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")==REPOSITORY,"Public Actions only")
 request=json.loads(args.request.read_bytes())
 require(request["schema"]==REQUEST_SCHEMA and request["request_number"]==180,"Independent explicit180 request")
 require(request["source_sha256"][Path(__file__).name]==sha(Path(__file__).read_bytes()),"Actual recovery source pin")
 policy=request["recovery_policy"]
 require(policy["original_run_id"]==RUN and policy["original_job_id"]==JOB and policy["original_source_commit"]==SOURCE_COMMIT,"Actual165 tuple")
 require(policy["maximum_original_log_bytes"]==LOG_BYTES and policy["maximum_scan_seconds"]==600,"Explicit recovery resources")
 root=Path(os.environ["RUNNER_TEMP"]).resolve();out=args.out.resolve()
 require(not args.out.exists() and not args.out.is_symlink() and out!=root and out.is_relative_to(root),"Fresh request-owned output")
 args.out.mkdir(parents=True)
 start=time.monotonic();scan=Scan(out,start+policy["maximum_scan_seconds"],policy["maximum_original_log_bytes"])
 result=dict(schema=SCHEMA,request_number=180,run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
  source_sha256=sha(Path(__file__).read_bytes()),original_run_id=RUN,original_job_id=JOB,original_source_commit=SOURCE_COMMIT,
  complete=False,resource_partial=False,error=None,no_scientific_calculation=True,raw_Git_Release_artifact_uploads=0)
 code=2;response=None
 def stop(signum,frame):raise ResourceStop("external-signal-"+str(signum))
 signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
 token=os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
 try:
  require(bool(token),"Official job token is inherited only through environment")
  run,runr=api_json("/actions/runs/"+str(RUN),token);job,jobr=api_json("/actions/jobs/"+str(JOB),token)
  require(run["id"]==RUN and run["head_sha"]==SOURCE_COMMIT and run["status"]=="completed","Official immutable actual165 run")
  require(job["id"]==JOB and job["run_id"]==RUN and job["status"]=="completed","Official original compute job")
  result["official_metadata"]=dict(run=runr,job=jobr,run_conclusion=run.get("conclusion"),job_conclusion=job.get("conclusion"))
  response,transport=open_log(token);result["transport"]=transport
  require(response.status==200 and response.headers.get("Content-Encoding") in (None,"","identity"),"Exact official unencoded log stream")
  advertised=response.headers.get("Content-Length")
  while True:
   scan.check();line=response.readline(MAX_LINE+1)
   if not line:break
   scan.line(line)
  scan.complete=True
  if advertised is not None:require(scan.bytes==int(advertised),"Whole advertised log byte count")
  scan.finish();result["complete"]=True;code=0
 except ResourceStop as exc:
  result["resource_partial"]=True;result["error"]=dict(type=type(exc).__name__,message=str(exc));code=3
 except BaseException as exc:
  message=str(exc)
  if token:message=message.replace(token,"[redacted]")
  # Avoid signed-URL disclosure from urllib exceptions.
  if isinstance(exc,(urllib.error.HTTPError,urllib.error.URLError)):
   result["error"]=dict(type=type(exc).__name__,HTTP_status=getattr(exc,"code",None),reason="Official transport failed; URL and authorization omitted")
  else:result["error"]=dict(type=type(exc).__name__,message=message,traceback=traceback.format_exc().replace(token or "\x00","[redacted]"))
  code=2
 finally:
  signal.signal(signal.SIGTERM,signal.SIG_IGN);signal.signal(signal.SIGINT,signal.SIG_IGN)
  if response is not None:response.close()
  result["original_stream"]=scan.record();result["elapsed_seconds"]=time.monotonic()-start;result["exit_code"]=code
  write(out/"recovery-result.json",result);bounded_emit(result)
 return code

if __name__=="__main__":raise SystemExit(main())
