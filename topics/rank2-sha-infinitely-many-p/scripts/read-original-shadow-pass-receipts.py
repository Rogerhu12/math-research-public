#!/usr/bin/env python3
"""Host-only authentication of two real original public PASS receipts.

This process alone may use the repository read token.  Stdout is exactly one
JSON envelope for a pipe into the --network none Sage consumer.  Diagnostic
messages go to stderr.  No log, receipt, or recomputable data file is written.
"""
import os
if (os.environ.get("GITHUB_ACTIONS")!="true" or
        os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public"):
    raise SystemExit("Use only the original public research workflow host.")
import argparse
import hashlib
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
DIRECTORY=Path(__file__).resolve().parent
sys.path.insert(0,str(DIRECTORY))
from original_shadow_receipt_tools import (
    SCHEMA,canonical,digest,add_pinned_arguments,pinned_request,
    validate_original_receipt,validate_envelope)
REPOSITORY="Rogerhu12/math-research-public"

def progress(stage,**kw):
    print("RANK2_SHADOW_HOST "+canonical(dict(stage=stage,**kw)),file=sys.stderr,flush=True)

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):
        return None

def public_github_read(relative,logs=False):
    url="https://api.github.com/repos/"+REPOSITORY+"/"+relative
    headers={"Accept":"application/vnd.github+json",
             "X-GitHub-Api-Version":"2022-11-28",
             "User-Agent":"original-rank2-shadow-host-authenticator"}
    token=os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"]="Bearer "+token
    opener=urllib.request.build_opener(NoRedirect)
    try:
        response=opener.open(urllib.request.Request(url,headers=headers),timeout=60)
    except urllib.error.HTTPError as err:
        if not logs or err.code not in (301,302,303,307,308):
            raise
        location=err.headers.get("Location")
        if not location or urllib.parse.urlsplit(location).scheme!="https":
            raise RuntimeError("Missing secure GitHub job-log redirect.")
        # A fresh request deliberately omits the repository token.
        response=urllib.request.urlopen(
            urllib.request.Request(location,headers={"User-Agent":headers["User-Agent"]}),
            timeout=60)
    with response:
        payload=response.read(32*1024*1024+1)
    if len(payload)>32*1024*1024:
        raise RuntimeError("Unexpectedly large complete certificate log.")
    return payload

def extract_unique_tag(text,tag):
    out=[]
    for line in text.splitlines():
        start=line.find(tag+" ")
        if start>=0:
            out.append(line[start+len(tag)+1:].strip())
    if not out or any(x!=out[0] for x in out):
        raise RuntimeError("Missing or conflicting complete "+tag+" receipt.")
    return out[0]

def authenticate(kind,stem,request):
    job_id=request[stem+"_job"]
    run_id=request[stem+"_run"]
    job=json.loads(public_github_read("actions/jobs/"+str(job_id)))
    run=json.loads(public_github_read("actions/runs/"+str(run_id)))
    assert int(job["id"])==job_id and int(job["run_id"])==run_id
    assert int(run["id"])==run_id
    assert run["repository"]["full_name"]==REPOSITORY
    if (job.get("status")!="completed" or job.get("conclusion")!="success" or
        run.get("status")!="completed" or run.get("conclusion")!="success"):
        raise RuntimeError("The same original "+kind+" public workflow has not succeeded.")
    expected_head=request[stem+"_run_head"]
    assert job["head_sha"]==run["head_sha"]==expected_head
    raw=public_github_read("actions/jobs/"+str(job_id)+"/logs",logs=True)
    text=raw.decode("utf-8")
    tag="RANK2_FIRST_FACTOR" if kind=="F" else "RANK2_RATIONAL_MAP"
    serialized=extract_unique_tag(text,tag+"_RESULT")
    logged_hash=extract_unique_tag(text,tag+"_SHA256")
    result=json.loads(serialized)
    assert hashlib.sha256(serialized.encode()).hexdigest()==digest(result)
    assert logged_hash==digest(result)==request[stem+"_result_sha256"]
    weight=validate_original_receipt(kind,result,request)
    auth={
        "job_id":job_id,"run_id":run_id,"job_status":job["status"],
        "job_conclusion":job["conclusion"],"run_status":run["status"],
        "run_conclusion":run["conclusion"],"run_head_sha":run["head_sha"],
        "job_head_sha":job["head_sha"],"mathematical_source":result["source"],
        "result_sha256":digest(result),
        "complete_job_log_sha256":hashlib.sha256(raw).hexdigest(),
    }
    progress("same original PASS authenticated",kind=kind,weight=weight,**auth)
    return result,auth

def main():
    parser=argparse.ArgumentParser()
    add_pinned_arguments(parser)
    args=parser.parse_args()
    request=pinned_request(args)
    first,auth_first=authenticate("F","first",request)
    packet,auth_packet=authenticate("P","packet",request)
    host_hash=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    body={"schema":SCHEMA,"repository":REPOSITORY,"request":request,
          "host_script_sha256":host_hash,
          "authentication":{"F":auth_first,"P":auth_packet},
          "certificates":{"F":first,"P":packet}}
    envelope=dict(body,envelope_sha256=digest(body))
    validate_envelope(envelope,request,host_hash)
    print(canonical(envelope),flush=True)

if __name__=="__main__":
    main()
