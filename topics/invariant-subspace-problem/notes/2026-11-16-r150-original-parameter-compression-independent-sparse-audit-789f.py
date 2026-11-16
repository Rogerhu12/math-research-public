#!/usr/bin/env python3
"""Independent sparse-dictionary audit of all 116 original parameter seed expansions.
Author: ChatGPT (AI), root. Date: 2026-11-16.
Imports no producer, FLINT, native code or polynomial helper.
All mathematical arrays and raw output remain temporary.
"""
import argparse,gzip,hashlib,json,resource,signal,time
from pathlib import Path
P=127
PARENT=(30466,"9120695ac2e42f8300fdea4aa814183bc033d83062810a8854998a25199795e2")
MANIFEST=(4401,"aeff1ffda616285363d0a709b436b77ab0a8e24b5accec91dc187bc55feb9490")
RECEIPT=(4214,"9c4c1d20b331ccf19cf9f732c901b0cd2de6b02895c76405ed603a711db547fe")
BINDING="baaa8ec3f9459c0d2f88ebb452c941ce241f2727d5becab1ca78511a55a589ca"
def require(ok,msg):
 if not ok:raise ValueError(msg)
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")
def sha(b):return hashlib.sha256(b).hexdigest()
def identity(p):
 b=Path(p).read_bytes();return {"bytes":len(b),"sha256":sha(b)}
def pin(path,e):
 b=path.read_bytes();require((len(b),sha(b))==e,"Full input "+str(path));return b
def descriptor(path,d):return pin(path,(d["bytes"],d["sha256"]))
def phase(directory,d,binding):
 b=gzip.decompress(descriptor(directory/d["path"],d))
 require((len(b),sha(b))==(d["logicalBytes"],d["logicalSha256"]),"Complete logical payload")
 z=json.loads(b);require(z["binding"]==binding,"Same complete payload binding")
 return z["data"]
def polynomial(v,maximum):
 out={};previous=None
 for e,c in v:
  require(len(e)==17 and all(type(i)is int and 0<=i<=maximum for i in e) and not any(e[12:]),"Complete parameter-only exponent")
  require(type(c)is int and 0<c<P,"Canonical full-field coefficient")
  t=tuple(e);require(previous is None or previous<t,"Canonical unique exponent order");previous=t
  key=sum(i<<(4*j) for j,i in enumerate(e[:12]));require(key not in out,"Injective base16 exponent code")
  out[key]=c
 return out
def main():
 ap=argparse.ArgumentParser()
 for name in ("parent","compression","out"):ap.add_argument("--"+name,type=Path,required=True)
 a=ap.parse_args();start=time.monotonic();resource.setrlimit(resource.RLIMIT_AS,(768<<20,768<<20))
 signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError("Root ninety-second sparse audit budget")))
 signal.setitimer(signal.ITIMER_REAL,90)
 result={"format":"r150-root-independent-all116-seed-compression-expansions-v1","status":"started","source":identity(__file__),"parameters":{"seconds":90,"memoryMiB":768,"prime":P,"coordinateCount":1160}}
 code=1
 try:
  pp=a.parent/"original-parameter-module-manifest.json";cp=a.compression/"complete-parameter-seed-compression-manifest.json";rp=a.compression/"complete-parameter-seed-compression-receipt.json"
  parent=json.loads(pin(pp,PARENT));m=json.loads(pin(cp,MANIFEST));r=json.loads(pin(rp,RECEIPT))
  require(m["binding"]==r["binding"]==BINDING and sha(canon(m["semantic"]))==BINDING,"Complete compression binding")
  require(parent["binding"]==m["semantic"]["parentBinding"] and len(parent["seeds"])==116,"Same original116 seed dictionary")
  require(r["status"]=="completed" and r["parameters"]["all1160ModuleCoordinatesVerified"],"Actual completed parent-to-compressed operation")
  checks=0
  for name,z in m["native"].items():
   for key in ("input","dictionary","checkpoint","result","receipt","log"):
    descriptor(a.compression/name/z[key]["path"],z[key]);checks+=1
   nr=json.loads((a.compression/name/z["receipt"]["path"]).read_bytes())
   require(nr["binding"]==z["binding"] and nr["status"]=="completed" and nr["completeWholeRows"]==nr["inputRows"],"Complete native input and bound result")
   require(nr["exhaustiveBitplaneChecks"]==244990 and nr["independentTinyProducts"]==25,"Actual full arithmetic and independent tiny gates")
  phases={k:phase(a.compression,d,BINDING) for k,d in m["phases"].items()}
  f=phases["complete-original-compressed-parameter-seeds"];ret=f["retainedOriginalSeedIndices"]
  require(len(ret)==50 and len(set(ret))==50 and set(ret)<=set(range(116)),"All retained are distinct literal original seeds")
  require(f["parentBinding"]==parent["binding"] and f["retainedOriginalSeedDescriptors"]==[parent["seeds"][i] for i in ret],"Every retained payload stays original")
  vectors=[];source_counts=[];vector_terms=0
  for i,d in enumerate(parent["seeds"]):
   z=phase(a.parent,d,parent["binding"]);require(z["seedIndex"]==i and z["fullOriginal18ProductVerified"],"Same paid original source identity")
   require(len(z["vector"])==10 and len(z["original18Source"])==18,"Whole original vector and source shapes")
   v=[polynomial(x,8) for x in z["vector"]];vectors.append(v)
   source_counts.append(sum(len(x) for x in z["original18Source"]));vector_terms+=sum(len(x) for x in v)
  require(len(f["allOriginal116SeedExpansionColumns"])==116,"Entire original expansion list")
  products=0
  for sid,x in enumerate(f["allOriginal116SeedExpansionColumns"]):
   require(x["parentSeedIndex"]==sid,"Complete expansion literal order")
   terms=[];seen=set()
   for idx,c in x["retainedCoefficients"]:
    require(type(idx)is int and 0<=idx<50 and idx not in seen,"Distinct retained source indices");seen.add(idx)
    terms.append((ret[idx],polynomial(c,3)))
   # Every retained exponent is <=8, every multiplier exponent <=3.
   # Their componentwise sum is <=11<16, so integer key addition has no carry.
   for axis in range(10):
    total={}
    for seed,c in terms:
     for e,a0 in c.items():
      for u,b0 in vectors[seed][axis].items():
       k=e+u;total[k]=(total.get(k,0)+a0*b0)%P;products+=1
    total={e:c for e,c in total.items() if c}
    require(total==vectors[sid][axis],"Every complete original module coordinate: "+str(sid)+"/"+str(axis))
  result.update(status="completed",parentManifest=identity(pp),compressionManifest=identity(cp),compressionReceipt=identity(rp),binding=BINDING,nativeFilesRehashed=checks,compressionPhasesRehashed=len(phases),allOriginalSeedPayloadsRehashed=116,all1160OriginalModuleCoordinatesIndependentlyVerified=True,scalarMonomialProducts=products,originalVectorTerms=vector_terms,retainedVectorTerms=sum(len(x) for i in ret for x in vectors[i]),originalSourceTerms=sum(source_counts),retainedSourceTerms=sum(source_counts[i] for i in ret),method="independent-canonical-sparse-dictionaries-and-no-carry-base16-monomial-encoding",sameFiniteFieldParameterSubmodule=True,original18SourcesTransportByPaidLinearCombination=True,newOriginal18MultiplicationRepeated=False,stableClosureClaimed=False,mathematicalArraysTemporaryOnly=True);code=0
 except Exception as ex:result.update(status="failed",error={"type":type(ex).__name__,"message":str(ex)})
 finally:
  signal.setitimer(signal.ITIMER_REAL,0);result["elapsedSeconds"]=time.monotonic()-start;result["peakRssKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss;result["exitCode"]=code
  a.out.write_bytes(canon(result));print(canon(result).decode())
 return code
if __name__=="__main__":raise SystemExit(main())
