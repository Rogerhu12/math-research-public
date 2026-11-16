#!/usr/bin/env python3
"""Restore the exact original H25 mod31^3 source from two historical git parts.
AI-assisted: GPT-6 Astra Pro / literature_audit, 2026-11-16.
No elimination, source recomputation, artifact upload, or tracked checkout writes.
"""
import argparse,gzip,hashlib,json,os,struct,subprocess,time
from pathlib import Path
REF="8c6304e273e64b0544d3dd58bc0e48a672a87c36"
SMALL=[{"key":"product","name":"original-product.json","historicalPath":"topics/invariant-subspace-problem/notes/r150-projector-free-original17-mod29791-789f/continuation-results/continued__projector-free-original__projector-free-original-original-product.json","bytes":815,"sha256":"25203923b41f758f7e7ada1c0d13e9d23adde710bbe5d3594f64a8780309582e","gitBlob":"a4372d142544176516e6b575c30764b5468e93df"},{"key":"recipe","name":"original.recipe","historicalPath":"topics/invariant-subspace-problem/notes/r150-projector-free-original17-mod29791-789f/continuation-results/continued__inputs__projector-free-nine-original.recipe","bytes":1468,"sha256":"ffe0677a0d2cd14b1cae55fb8e8eb4b5074454e6a99b0def430b4b1fff3ae52a","gitBlob":"3786af73d8cd5afca3f17dd3d47606c56b7ddc62"},{"key":"continuation","name":"continuation-receipt.json","historicalPath":"topics/invariant-subspace-problem/notes/r150-projector-free-original17-mod29791-789f/continuation-results/projector-free-three-stage-continuation-receipt.json","bytes":11009,"sha256":"55e7c11e136df8bacfb78db6ed50a575faa1c7f91a7c721d89322ef599935dde","gitBlob":"040063c8bfd16cf491406ec47440170de76e6057"},{"key":"preservation","name":"root-preservation-manifest.json","historicalPath":"topics/invariant-subspace-problem/notes/r150-projector-free-original17-mod29791-789f/root-preservation-manifest.json","bytes":27436,"sha256":"5d87cc8a4fa623a122cafe3ee8053f47c068680fc1c72e3920a123b1d3097c7f","gitBlob":"ce0563fa14c4a5951eed14a012987e31890986fe"},{"key":"model","name":"original-integer-h25-mod29791.txt","historicalPath":"topics/invariant-subspace-problem/notes/r150-h25-second-residual-789f/original-integer-h25-mod29791.txt","bytes":22824,"sha256":"2785c53d015d05db4550e1978c05db7d42009cfa8942e915541599a76d3701cc","gitBlob":"c240b309164a0dacc01bcd8bbdb73d347cb1e3f1"}]
PARTS=[{"name":"h25-source.gz.part001","historicalPath":"topics/invariant-subspace-problem/notes/r150-projector-free-original17-mod29791-789f/continuation-results/certificates/continued__projector-free-original__projector-free-original-primitive-source-mod29791.bin.gz.part001","bytes":4500000,"gitBlob":"c754b6cf49c2b3414dad643f8252a3c3900513ec","sha256":"36143404afbc54107dc193c2b83233eb98089539fca760c4fdac6d71fba94778"},{"name":"h25-source.gz.part002","historicalPath":"topics/invariant-subspace-problem/notes/r150-projector-free-original17-mod29791-789f/continuation-results/certificates/continued__projector-free-original__projector-free-original-primitive-source-mod29791.bin.gz.part002","bytes":274246,"gitBlob":"93b54d889ea401a63437088e4c309c2f135c7aa0","sha256":"c0c460c87ac4b06d04533981bb09b2804e861a8e503bafb3b0de8cb5a98df569"}]
SOURCE={"name":"original-h25-source-mod29791.bin","bytes":4989406,"sha256":"593643d82b259995194b0d89c9f46c8f042cd8d0c66bdfff0a00227689810cdd"}
FORMAT="r150-original-h25-minimal-recovery-v1"
def require(ok,message):
 if not ok:raise ValueError(message)
def identity(path):
 h=hashlib.sha256()
 with path.open("rb") as f:
  for b in iter(lambda:f.read(1048576),b""):h.update(b)
 return {"bytes":path.stat().st_size,"sha256":h.hexdigest()}
def exact(path,pin):
 return path.is_file() and identity(path)=={k:pin[k] for k in ("bytes","sha256")}
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--repo",type=Path,required=True);ap.add_argument("--out",type=Path,required=True)
 ap.add_argument("--seconds",type=float,default=180);a=ap.parse_args()
 require(0<a.seconds<=600,"bounded historical recovery clock")
 a.out.mkdir(parents=True,exist_ok=True);start=time.monotonic();end=start+a.seconds
 rec={"format":FORMAT,"status":"running","historicalCommit":REF,"files":{},"largeDataUploadedOrCommitted":False}
 receipt=a.out/"original-h25-minimal-recovery-receipt.json"
 def save():
  rec["elapsedSeconds"]=time.monotonic()-start
  tmp=receipt.with_name(receipt.name+".tmp");tmp.write_text(json.dumps(rec,sort_keys=True,separators=(",",":"))+"\n")
  os.replace(tmp,receipt)
 def run(args,stdout=None):
  remaining=end-time.monotonic()
  if remaining<=0:raise TimeoutError("historical recovery budget")
  return subprocess.run(args,cwd=a.repo,stdin=subprocess.DEVNULL,stdout=subprocess.PIPE if stdout is None else stdout,
                        stderr=subprocess.PIPE,timeout=remaining,check=False)
 try:
  q=run(["git","cat-file","-e",REF+"^{commit}"])
  if q.returncode:
   q=run(["git","fetch","--no-tags","--depth=1","--filter=blob:none","origin",REF])
   require(q.returncode==0,"exact historical commit fetch failed")
  require(run(["git","cat-file","-e",REF+"^{commit}"]).returncode==0,"pinned historical commit exists")
  def restore(pin,target):
   if exact(target,pin):return {"reused":True,**identity(target)}
   require(not target.exists(),"existing recovery file differs from its exact pin")
   q=run(["git","rev-parse",REF+":"+pin["historicalPath"]])
   require(q.returncode==0 and q.stdout.decode().strip()==pin["gitBlob"],"exact historical git object identity")
   tmp=target.with_name(target.name+".tmp");target.parent.mkdir(parents=True,exist_ok=True)
   with tmp.open("wb") as out:q=run(["git","show",REF+":"+pin["historicalPath"]],out)
   require(q.returncode==0 and exact(tmp,pin),"all historical file bytes and SHA256")
   os.replace(tmp,target);return {"reused":False,**identity(target)}
  for pin in SMALL:
   rec["files"][pin["key"]]=restore(pin,a.out/pin["name"]);save()
  target=a.out/SOURCE["name"]
  if not exact(target,SOURCE):
   require(not target.exists(),"existing original H25 source differs from its exact pin")
   paths=[]
   for pin in PARTS:
    p=a.out/"compressed-parts"/pin["name"];rec["files"][pin["name"]]=restore(pin,p);paths.append(p);save()
   joined=a.out/"compressed-parts"/"h25-source.bin.gz"
   with joined.open("wb") as out:
    for p in paths:
     with p.open("rb") as f:
      for b in iter(lambda:f.read(1048576),b""):out.write(b)
   require(joined.stat().st_size==sum(p["bytes"] for p in PARTS),"exact joined compressed size")
   tmp=target.with_name(target.name+".tmp");total=0
   with gzip.open(joined,"rb") as f,tmp.open("wb") as out:
    while True:
     b=f.read(1048576)
     if not b:break
     total+=len(b);require(total<=SOURCE["bytes"],"bounded exact original source decompression");out.write(b)
   require(exact(tmp,SOURCE),"complete original H25 raw source bytes and SHA256")
   os.replace(tmp,target)
  with target.open("rb") as f:head=f.read(46)
  require(len(head)==46 and head[:8]==b"R150PS31" and struct.unpack_from("<5I",head,8)==(31,29791,6188,9,87)
          and struct.unpack_from("<9H",head,28)==tuple(range(2,11)),"actual complete H25 source schema and labels")
  product=json.loads((a.out/"original-product.json").read_text())
  continuation=json.loads((a.out/"continuation-receipt.json").read_text())
  require(continuation["status"]=="completed" and continuation["originalSeventeenConclusion"]==product,
          "same paid complete original product identity")
  require(product["fullOriginalSeventeenEquationIdentityMod29791"] and product["failedCoefficientCount"]==0
          and product["modulus"]==29791 and product["divisor"]==29791,"paid original p3 product gates")
  rec["files"]["decodedSource"]=identity(target);rec["status"]="completed";rec["allHistoricalBytesAndSHA256Verified"]=True
  rec["originalSourceHeaderVerified"]=True;save();print(json.dumps(rec,sort_keys=True),flush=True);return 0
 except BaseException as e:
  rec["status"]="budget-checkpoint" if isinstance(e,(TimeoutError,subprocess.TimeoutExpired)) else "failed"
  rec["errorType"]=type(e).__name__;rec["error"]=str(e);save();print(json.dumps(rec,sort_keys=True),flush=True)
  return 75 if rec["status"]=="budget-checkpoint" else 1
if __name__=="__main__":raise SystemExit(main())
