#!/usr/bin/env python3
"""Restore two pinned historical source dictionaries into this temporary job.
Astra-ISP-789f / root; AI-assisted, GPT-6 Astra Pro.
Only exact legacy inputs are read. No arrays or Release assets are published.
"""
import argparse,hashlib,json,os,pathlib,subprocess,sys,time
p=argparse.ArgumentParser(description=__doc__)
p.add_argument("--repo",type=pathlib.Path,required=True)
p.add_argument("--out-dir",type=pathlib.Path,required=True)
p.add_argument("--receipt",type=pathlib.Path,required=True)
a=p.parse_args();start=time.monotonic()
commit="8c6304e273e64b0544d3dd58bc0e48a672a87c36"
prefix="topics/invariant-subspace-problem/"
items=[
("native-normal-form-input.txt",prefix+"notes/r150-module-actions-789f/43588728414-1/char31/native-normal-form-input.txt",128145,"291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6"),
("infinity-first-jet-receipt.json",prefix+"notes/2026-11-14-r150-infinity-first-jet-receipt-789f.json",72072,"d904b1afcd6feb6d07e310e758869aa345342f7d013773aa0c433203291c438e")]
r={"format":"isp-two-pinned-source-dictionaries-temporary-restore-v1",
   "historicalCommit":commit,"largeDataUploadedOrCommitted":False,
   "temporaryOnly":True,"inputs":[]}
def git(args,seconds=60):
 return subprocess.run(["git","-C",str(a.repo)]+args,stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE,timeout=seconds)
try:
 a.out_dir.mkdir(parents=True,exist_ok=True)
 for name,path,size,wanted in items:
  target=a.out_dir/name;reused=target.is_file()
  if reused:raw=target.read_bytes()
  else:
   q=git(["show",commit+":"+path])
   if q.returncode:
    f=git(["fetch","--no-tags","--depth=1","--filter=blob:none","origin",commit],120)
    if f.returncode:raise RuntimeError("pinned historical fetch exited "+str(f.returncode))
    q=git(["show",commit+":"+path])
   if q.returncode:raise RuntimeError("pinned historical git show exited "+str(q.returncode))
   raw=q.stdout
  if len(raw)!=size or hashlib.sha256(raw).hexdigest()!=wanted:
   raise RuntimeError("complete historical input identity mismatch: "+name)
  decoded=raw.decode("utf-8")
  if name.endswith(".json"):json.loads(decoded)
  if not reused:
   tmp=target.with_name(target.name+".partial");tmp.write_bytes(raw);os.replace(tmp,target)
  r["inputs"].append({"temporaryName":name,"historicalPath":path,"verifiedBytes":size,
                      "verifiedSHA256":wanted,"reusedExistingVerifiedTemporaryInput":reused})
 r.update(status="completed",allInputBytesVerified=True);rc=0
except Exception as e:
 r.update(status="failed",error=str(e),exceptionType=type(e).__name__);rc=1
finally:
 r["elapsedSeconds"]=time.monotonic()-start
 a.receipt.parent.mkdir(parents=True,exist_ok=True)
 tmp=a.receipt.with_name(a.receipt.name+".partial")
 tmp.write_text(json.dumps(r,sort_keys=True)+"\n");os.replace(tmp,a.receipt)
print(json.dumps(r,sort_keys=True),flush=True)
sys.exit(rc)
