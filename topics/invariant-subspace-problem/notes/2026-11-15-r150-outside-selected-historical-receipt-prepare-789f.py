#!/usr/bin/env python3
"""Recover one pinned historical small receipt in this job only.
Astra-ISP-789f / root; AI-assisted, GPT-6 Astra Pro.
"""
import argparse,hashlib,json,os,pathlib,subprocess,sys,time
ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument("--repo",type=pathlib.Path,required=True)
ap.add_argument("--out",type=pathlib.Path,required=True)
ap.add_argument("--receipt",type=pathlib.Path,required=True)
a=ap.parse_args();start=time.monotonic()
commit="8c6304e273e64b0544d3dd58bc0e48a672a87c36"
path="topics/invariant-subspace-problem/notes/r150-selected-infinity-minor-dag-789f/selected-infinity-minor-dag-receipt.json"
wanted="5cd9543de68bdb562bbe21189d5b0712248e6943c5572fe38ff27ec4fc1f5f68"
r={"format":"isp-one-pinned-historical-receipt-temporary-restore-v1","historicalCommit":commit,"historicalPath":path,
   "largeDataUploadedOrCommitted":False,"temporaryOnly":True}
try:
 if a.out.is_file():
  raw=a.out.read_bytes();r["reusedExistingVerifiedTemporaryInput"]=True
 else:
  p=subprocess.run(["git","-C",str(a.repo),"show",commit+":"+path],stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=45)
  if p.returncode:raise RuntimeError("pinned historical git show exited "+str(p.returncode))
  raw=p.stdout;r["reusedExistingVerifiedTemporaryInput"]=False
 if len(raw)!=75700 or hashlib.sha256(raw).hexdigest()!=wanted:raise RuntimeError("complete historical receipt identity mismatch")
 d=json.loads(raw)
 if d.get("status")!="completed" or not d.get("allPaidTraceEventsVerified") or not d.get("allOriginalSourceIdentitiesVerified"):
  raise RuntimeError("historical paid selected source checks absent")
 a.out.parent.mkdir(parents=True,exist_ok=True)
 if not a.out.exists():
  p=a.out.with_name(a.out.name+".partial");p.write_bytes(raw);os.replace(p,a.out)
 r.update(status="completed",verifiedBytes=len(raw),verifiedSHA256=wanted,allInputBytesVerified=True);rc=0
except Exception as e:r.update(status="failed",error=str(e),exceptionType=type(e).__name__);rc=1
finally:
 r["elapsedSeconds"]=time.monotonic()-start
 a.receipt.parent.mkdir(parents=True,exist_ok=True)
 p=a.receipt.with_name(a.receipt.name+".partial");p.write_text(json.dumps(r,sort_keys=True)+"\n");os.replace(p,a.receipt)
print(json.dumps(r,sort_keys=True),flush=True)
sys.exit(rc)
