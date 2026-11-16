#!/usr/bin/env python3
"""Restore the one paid K4 family needed by the complete210 p7 continuation.
Author: ChatGPT (AI), literature_audit. Date: 2026-11-16.
Immutable git reads only. No old elimination, mathematical arrays in Git, or uploads.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,resource,signal,subprocess,time
from pathlib import Path
REF="8c6304e273e64b0544d3dd58bc0e48a672a87c36"
BASE="topics/invariant-subspace-problem/notes/r150-augmented-seven-second-actions-789f/43634830833-1/"
ORIGINAL="genuine-seven-k4-original/genuine-seven-k4-original-primitive-source-mod28629151.bin"
MANIFEST=(19200,"b0c1e461fc9a10c9002f4a6a74cae7394283cccf7ffe0989804143c512745f3d")
FILE=(7645286,"a5e16cfe2f6c6665c0806c488ea0ba3db11516e81be259c1f213126d9339566a")
PRODUCT=(1020,"22f1bc8d89f3a63b3ad4f40b18e598681d7ce08f5fe283f09b078c9fb5be762a")
COMPRESSED=(6399260,"6fd02846e0b889686df4cb1318bed6cb4727e53f5577a4e8fa06310a5ff48a45")
PARTS=[
 ("certificates/genuine-seven-k4-original__genuine-seven-k4-original-primitive-source-mod28629151.bin.gz.part001",4500000,
  "43d8a5481547c7c4140586aab1ef50d87e63517b234de8f7c69d17a59502f76e"),
 ("certificates/genuine-seven-k4-original__genuine-seven-k4-original-primitive-source-mod28629151.bin.gz.part002",1899260,
  "bb5df055bc7583a68edff4d3abe673dbe0a782e6e3552b74bd7afb60629f1919")]
class BudgetStop(Exception):pass
def check(ok,msg):
 if not ok:raise ValueError(msg)
def sha(data):return hashlib.sha256(data).hexdigest()
def verified(data,pin):return len(data)==pin[0] and sha(data)==pin[1]
def same(path,pin):return path.is_file() and path.stat().st_size==pin[0] and verified(path.read_bytes(),pin)
def clean(value):
 s=str(value)
 for key in ("GH_TOKEN","GITHUB_TOKEN","GIT_CONFIG_VALUE_0"):
  x=os.environ.get(key)
  if x:s=s.replace(x,"***")
 return s
def atomic(path,data):
 temp=path.with_name(path.name+".part");temp.write_bytes(data);os.replace(temp,path)
def main():
 p=argparse.ArgumentParser()
 p.add_argument("--repo",type=Path,required=True);p.add_argument("--out",type=Path,required=True)
 p.add_argument("--seconds",type=float,default=180);a=p.parse_args()
 check(0<a.seconds<=600,"bounded historical read time")
 resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
 a.out.mkdir(parents=True,exist_ok=True);start=time.monotonic();deadline=start+a.seconds-3
 rec={"format":"r150-root2-fourth-current-k4-input-recovery-v1","status":"started",
  "parameters":{"historicalRef":REF,"historicalOriginalFile":ORIGINAL,
   "executionRunID":os.environ.get("GITHUB_RUN_ID"),"mathematicsRecomputed":False,
   "oldLargeChainRestored":False,"allOutputsTemporaryOnly":True,"selectedBinaryCount":1}}
 def save():
  rec["elapsedSeconds"]=time.monotonic()-start
  atomic(a.out/"currentK4-recovery-receipt.json",(json.dumps(rec,sort_keys=True,separators=(",",":"))+"\n").encode())
 def command(argv):
  remaining=deadline-time.monotonic()
  if remaining<=0:raise BudgetStop("historical-file checkpoint")
  try:c=subprocess.run(argv,cwd=a.repo,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=min(120,remaining))
  except subprocess.TimeoutExpired as exc:raise BudgetStop("bounded immutable git read") from exc
  check(c.returncode==0,"historical read failed: "+clean(c.stderr.decode(errors="replace")[-1000:]))
  return c.stdout
 def stop(signum,frame):raise BudgetStop("recovery signal "+str(signum))
 signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
 try:
  target=a.out/"currentK4.bin";product=a.out/"currentK4-product.json"
  complete=same(target,FILE) and same(product,PRODUCT)
  if not complete:
   probe=subprocess.run(["git","cat-file","-e",REF+"^{commit}"],cwd=a.repo,
      stdout=subprocess.DEVNULL,stderr=subprocess.PIPE,timeout=max(.1,min(30,deadline-time.monotonic())))
   if probe.returncode:command(["git","fetch","--no-tags","--depth=1","--filter=blob:none","origin",REF])
   manifest=command(["git","show",REF+":"+BASE+"certificate-manifest.json"])
   check(verified(manifest,MANIFEST),"exact historical storage manifest")
   found=[x for x in json.loads(manifest)["files"] if x["originalFile"]==ORIGINAL]
   check(len(found)==1,"unique complete historical K4 source")
   item=found[0]
   check((item["uncompressedBytes"],item["uncompressedSHA256"])==FILE and
      (item["compressedBytes"],item["compressedSHA256"])==COMPRESSED and
      [(x["file"],x["bytes"],x["sha256"]) for x in item["parts"]]==PARTS,"all exact historical K4 storage pins")
   if not same(target,FILE):
    chunks=[]
    for path,size,digest in PARTS:
     data=command(["git","show",REF+":"+BASE+path])
     check(verified(data,(size,digest)),"exact K4 compressed part")
     chunks.append(data)
    packed=b"".join(chunks);check(verified(packed,COMPRESSED),"complete K4 compressed stream")
    raw=gzip.decompress(packed);check(verified(raw,FILE),"complete K4 original source identity")
    atomic(target,raw)
   if not same(product,PRODUCT):
    data=command(["git","show",REF+":"+BASE+"genuine-seven-k4-original__genuine-seven-k4-original-original-product.json"])
    check(verified(data,PRODUCT),"exact paid K4 original-product receipt");atomic(product,data)
  check(same(target,FILE) and same(product,PRODUCT),"all final K4 source and receipt bytes")
  receipt=json.loads(product.read_bytes())
  check(receipt["status"]=="completed" and receipt["prime"]==31 and receipt["modulus"]==28629151
    and receipt["divisor"]==923521 and receipt["originalRawRows"]==6188 and receipt["originalComponents"]==4367
    and receipt["originalEquations"]==17 and receipt["targetLabels"]==list(range(7001,7008))
    and receipt["targetMode"]==0 and receipt["allOriginalProductCoefficientsDivisible"] is True
    and receipt["failedCoefficientCount"]==0,"original all-seven K4 divisibility scope")
  rec["status"]="completed";rec["parameters"].update(
   binary={"file":target.name,"bytes":FILE[0],"sha256":FILE[1]},
   originalProductReceipt={"file":product.name,"bytes":PRODUCT[0],"sha256":PRODUCT[1]},
   reusedCompleteFiles=complete,allSevenOriginalK4SourcesVerified=True,
   allOriginal6188And4367ScopeVerified=True,fullP7ProductsStillRequired=True)
  code=0
 except (BudgetStop,subprocess.TimeoutExpired) as e:
  rec["status"]="budget-checkpoint";rec["errorType"]=type(e).__name__;rec["error"]=clean(e);code=75
 except Exception as e:
  rec["status"]="failed";rec["errorType"]=type(e).__name__;rec["error"]=clean(e);code=1
 finally:
  save();print(json.dumps(rec,sort_keys=True,separators=(",",":")),flush=True)
 return code
if __name__=="__main__":raise SystemExit(main())
