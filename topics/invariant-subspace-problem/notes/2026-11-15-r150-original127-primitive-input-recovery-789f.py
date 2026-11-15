#!/usr/bin/env python3
"""Restore one pinned historical primitive input in the current temporary job.
Astra-ISP-789f / root; AI-assisted, GPT-6 Astra Pro.
No new arrays, Release assets, binary commits, or cross-job caches are created.
"""
import argparse,gzip,hashlib,json,os,pathlib,subprocess,sys,time
p=argparse.ArgumentParser(description=__doc__)
p.add_argument("--repo",type=pathlib.Path,required=True)
p.add_argument("--out",type=pathlib.Path,required=True)
p.add_argument("--receipt",type=pathlib.Path,required=True)
a=p.parse_args();start=time.monotonic()
commit="8c6304e273e64b0544d3dd58bc0e48a672a87c36"
path="topics/invariant-subspace-problem/notes/r150-first-padic-residual-789f/original-primitive-integer-equations.json.gz"
wanted="44350c49f9f60c61427b7278bf7f3d24b6cb2e6583848a113b03bb109516d4fe"
unpacked="fa2e5d80e9fbd47e1e237ae60c548900a15922a0543e02be77fc972dc52944b3"
r={"format":"isp-one-pinned-primitive-temporary-restore-v1","historicalCommit":commit,
 "historicalPath":path,"largeDataUploadedOrCommitted":False,"temporaryOnly":True}
def git(args,seconds=60):
 return subprocess.run(["git","-C",str(a.repo)]+args,stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE,timeout=seconds)
try:
 if a.out.is_file():
  raw=a.out.read_bytes();r["reusedExistingVerifiedTemporaryInput"]=True
 else:
  q=git(["show",commit+":"+path])
  if q.returncode:
   f=git(["fetch","--no-tags","--depth=1","--filter=blob:none","origin",commit],120)
   if f.returncode:raise RuntimeError("pinned historical fetch exited "+str(f.returncode))
   q=git(["show",commit+":"+path])
  if q.returncode:raise RuntimeError("pinned historical git show exited "+str(q.returncode))
  raw=q.stdout;r["reusedExistingVerifiedTemporaryInput"]=False
 if len(raw)!=65159 or hashlib.sha256(raw).hexdigest()!=wanted:
  raise RuntimeError("complete historical primitive compressed identity mismatch")
 decoded=gzip.decompress(raw)
 if hashlib.sha256(decoded).hexdigest()!=unpacked:
  raise RuntimeError("complete historical primitive uncompressed identity mismatch")
 json.loads(decoded)
 a.out.parent.mkdir(parents=True,exist_ok=True)
 if not a.out.exists():
  q=a.out.with_name(a.out.name+".partial");q.write_bytes(raw);os.replace(q,a.out)
 r.update(status="completed",verifiedBytes=len(raw),verifiedSHA256=wanted,
          verifiedUncompressedBytes=len(decoded),verifiedUncompressedSHA256=unpacked,
          allInputBytesVerified=True);rc=0
except Exception as e:
 r.update(status="failed",error=str(e),exceptionType=type(e).__name__);rc=1
finally:
 r["elapsedSeconds"]=time.monotonic()-start
 a.receipt.parent.mkdir(parents=True,exist_ok=True)
 q=a.receipt.with_name(a.receipt.name+".partial")
 q.write_text(json.dumps(r,sort_keys=True)+"\n");os.replace(q,a.receipt)
print(json.dumps(r,sort_keys=True),flush=True)
sys.exit(rc)
