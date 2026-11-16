#!/usr/bin/env python3
"""Read a completed job log; recover and verify its exact bounded raw receipt.

Author: Astra-ISP-789f / literature_audit, with /root.
AI-assisted GPT-6 Astra Pro. Mathematical arrays remain temporary.
"""
import argparse,hashlib,json,re
from pathlib import Path

def need(b,s):
 if not b:raise ValueError(s)
def sha(b):return hashlib.sha256(b).hexdigest()
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")
def identity(p):
 b=p.read_bytes();return {"path":p.name,"bytes":len(b),"sha256":sha(b)}

ap=argparse.ArgumentParser()
for k in ("job-log","source","local-prepare-manifest","out"):ap.add_argument("--"+k,type=Path,required=True)
a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=True)
lines=[re.sub(r"^\ufeff?\d{4}-\d\d-\d\dT[\d:.]+Z ","",z) for z in a.job_log.read_text().splitlines()]
steps=[json.loads(z[len("ISP_REMOTE_STEP "):]) for z in lines if z.startswith("ISP_REMOTE_STEP ")]
need(len(steps)==3 and all(z["runId"]=="43883188532" for z in steps),"all three literal completed-job steps")
need([z["stepId"] for z in steps]==["original-ten-parameter-model116-180","original-parameter-seed-compression50-180","original-rank-four-unexpanded-local-positive600"],"exact original step order")
need([z["exitCode"] for z in steps]==[0,0,75],"successful parents and actual source budget75")
z=steps[-1];raw=dict(z["result"]);raw.pop("events",None)
src=identity(a.source)
need(src=={"path":"2026-11-16-r150-original-rank-four-unexpanded-local-source127-v2-789f.py","bytes":35070,"sha256":"ee9bdabfdd325150b622e77a91d20eb814c642c8cb66bbf4734106466af630e3"},"literal frozen original source")
need(z["scriptSHA256"]==src["sha256"],"actual script identity")
raw["source"]=src
# The producer's argparse type is float. Restore its 600.0 spelling after
# the GitHub JSON transport has represented that number as integer 600.
raw["parameters"]["seconds"]=float(raw["parameters"]["seconds"])
b=canon(raw)
need(len(b)==z["fullTemporaryReceiptBytes"]==19983,"entire raw byte count")
need(sha(b)==z["fullTemporaryReceiptSHA256"]=="b77565d9425d3e4a74b8567ec29873a24724802f0d3d779c39cb02c3bb5a390f","entire raw byte SHA256")
need(raw["binding"]=="8e701750318d6bed82bd5e202266e025a60da1d23397f2c740badae301ad0bff" and raw["status"]=="budget-checkpoint","actual bounded result identity")
pm=json.loads(a.local_prepare_manifest.read_bytes())
need(pm["semantic"]["source"]==src and sha(canon(pm["semantic"]))==raw["binding"]==pm["binding"],"independent canonical semantic binding, same prepared mathematical input")
p=raw["parameters"]
for k in ("all17OriginalGradientTransportsVerified","all40OriginalBellRemovalCoordinatesVerified","all4Original18BellRemovalProductsVerified","all50Original18ProductsVerified","localizedInitialModuleEqualityVerified"):
 need(p[k] is True,"complete original gate "+k)
need(p["moduleShape"]==[10,46] and p["localizedShape"]==[10,56] and p["moduleTerms"]==315860,"exact literal sparse presentation")
need(p["chartIndex"]==14 and p["originalMeanRows"]==[2,3,4,5] and p["deltaTerms"]==124,"original chart dictionary")
need(len(p["allFifteenLiteralMinorStatistics"])==15 and all(q["nonzero"] for q in p["allFifteenLiteralMinorStatistics"]),"all fifteen literal minors")
need(p["deltaLogicalSHA256"]=="eff3070880440dd84f3b8d6bcfac5fc71461537d55b9f3d2c323a4287cdde0f6","same literal delta")
st=p["stages"]
need(len(st)==3 and [x["exitCode"] for x in st]==[0,0,75],"complete selftest and SSI, unfinished candidate")
need(st[0]["markers"]==["@@LOCAL-SOURCE-SELFTEST-COMPLETE"] and st[1]["markers"]==["@@ALL-560-LOCAL-SSI-PRODUCTS"],"actual engine preflight markers")
need(st[2]["markers"]==["@@LOCAL-SLIMGB-START"] and st[2]["status"]=="budget","no complete candidate or target readout")
need(p["error"]=={"message":"candidate engine has no complete saved basis; no partial GB is reusable","type":"Budget"},"precise producer budget reason")
need(not p["nonmembershipClaimed"] and not p["characteristicZeroConclusion"] and not p["completeCriticalQuotientClaimed"],"strict mathematical boundary")
stops=[json.loads(q[len("ISP_WHOLE_PREFIX_RESUME_STOP "):]) for q in lines if q.startswith("ISP_WHOLE_PREFIX_RESUME_STOP ")]
need(len(stops)==1 and stops[0]["attempt"]==1 and stops[0]["previousSignature"] is None and stops[0]["actualSignature"] is None,"whole-prefix guard prevented an empty repeat")
pulls=[json.loads(q[len("ISP_ACTUAL_RULE_PULL "):]) for q in lines if q.startswith("ISP_ACTUAL_RULE_PULL ")]
need(pulls and all(q["rulesDiffer"] is False for q in pulls),"all actual rule-read gates")
need(not z["largeDataUploadedOrCommitted"],"temporary mathematical data only")
rawpath=a.out/"reconstructed-original-rank-four600-receipt.json";rawpath.write_bytes(b)
out={"format":"r150-original-rank-four600-completed-log-audit-v1","runId":43883188532,"jobId":133354233895,
 "source":src,"jobLog":identity(a.job_log),"reconstructedRaw":identity(rawpath),"binding":raw["binding"],
 "allOriginalInputAndEnginePreflightGatesVerified":True,"rawByteSHA256ReconstructionVerified":True,"canonicalBindingVerified":True,
 "sourceExitCode":75,"sourceSeconds":raw["elapsedSeconds"],"candidateSeconds":st[2]["elapsedSeconds"],"wallSeconds":z["wallSeconds"],
 "parentPeakRssKiB":p["parentPeakRssKiB"],"childPeakRssKiB":p["childPeakRssKiB"],
 "newCompleteCandidate":False,"targetRemainderComputed":False,"sourceCertificateComputed":False,"emptyRepeatPrevented":True,
 "mathematicalNonmembershipClaimed":False,"characteristicZeroConclusion":False}
q=a.out/"rank-four600-log-audit-receipt.json";q.write_bytes(canon(out));print(canon(out).decode())
