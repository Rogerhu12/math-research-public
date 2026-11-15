#!/usr/bin/env python3
"""Restore two already-published original dictionary inputs to temporary storage.
Author: Astra-ISP-789f / root. AI-assisted: GPT-6 Astra Pro.
No new matrix computation, repository mutation, or large persistent output.
"""
import argparse,hashlib,json,os,pathlib,resource,subprocess,time
REF="8c6304e273e64b0544d3dd58bc0e48a672a87c36"
ITEMS=[
 ("native-normal-form-input.txt","topics/invariant-subspace-problem/notes/r150-module-actions-789f/43588728414-1/char31/native-normal-form-input.txt",128145,"291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6"),
 ("infinity-first-jet-receipt.json","topics/invariant-subspace-problem/notes/2026-11-14-r150-infinity-first-jet-receipt-789f.json",72072,"d904b1afcd6feb6d07e310e758869aa345342f7d013773aa0c433203291c438e")
]
def sha(b):return hashlib.sha256(b).hexdigest()
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument("--repo",type=pathlib.Path,required=True);p.add_argument("--out-dir",type=pathlib.Path,required=True);p.add_argument("--out",type=pathlib.Path,required=True);a=p.parse_args()
 resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,)*2)
 start=time.monotonic();rec={"format":"r150-paid-original-minor-dictionary-recovery-v2","status":"running","parameters":{"historicalCommit":REF,"temporaryOnly":True,"repositoryMutation":False,"newMatrixComputation":False,"largeDataUploadedOrCommitted":False}}
 rc=1
 try:
  a.out_dir.mkdir(parents=True,exist_ok=True);verified=[];fetched=False
  for name,path,n,s in ITEMS:
   dest=a.out_dir/name
   raw=dest.read_bytes() if dest.exists() else b""
   reused=len(raw)==n and sha(raw)==s
   if not reused:
    if not fetched:
     q=subprocess.run(["git","fetch","--no-tags","--depth=1","--filter=blob:none","origin",REF],cwd=a.repo,capture_output=True,timeout=60)
     if q.returncode:raise RuntimeError("pinned historical fetch failed, code "+str(q.returncode))
     fetched=True
    q=subprocess.run(["git","show",REF+":"+path],cwd=a.repo,capture_output=True,timeout=45)
    if q.returncode:raise RuntimeError("pinned historical text read failed, code "+str(q.returncode))
    raw=q.stdout
   if len(raw)!=n or sha(raw)!=s:raise RuntimeError("complete historical byte identity failed: "+name)
   raw.decode("utf-8")
   if not reused:
    tmp=dest.with_name(dest.name+".partial");tmp.write_bytes(raw);os.replace(tmp,dest)
   verified.append({"historicalPath":path,"file":name,"bytes":n,"sha256":s,"alreadyVerifiedTemporaryCopy":reused})
  rec.update(status="completed",allCompleteHistoricalInputsVerified=True);rec["parameters"].update({"inputs":verified,"actualHistoricalFetchPerformed":fetched});rc=0
 except Exception as e:rec.update(status="failed",error=str(e),exceptionType=type(e).__name__)
 finally:
  rec["elapsedSeconds"]=time.monotonic()-start;a.out.parent.mkdir(parents=True,exist_ok=True)
  raw=json.dumps(rec,sort_keys=True,indent=2).encode()+b"\n";tmp=a.out.with_name(a.out.name+".partial");tmp.write_bytes(raw);os.replace(tmp,a.out)
 print(json.dumps({"status":rec["status"],"receiptSHA256":sha(a.out.read_bytes())}),flush=True)
 return rc
if __name__=="__main__":raise SystemExit(main())
