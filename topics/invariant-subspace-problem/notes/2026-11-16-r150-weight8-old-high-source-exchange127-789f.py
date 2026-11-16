#!/usr/bin/env python3
"""Read the paid74 exact relations; exchange only actual original high sources.

Author: Astra-ISP-789f / normal_annihilator, with /root.
AI-assisted GPT-6 Astra Pro. 2026-11-16.
No large matrix elimination. All exchanges must pass the full10/original18
polynomial identities. An exchange is not a generator-count or unit claim.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,os,resource,signal,sys,time
from pathlib import Path
sys.set_int_max_str_digits(0)
FORMAT="r150-paid-weight8-original-high-source-exchange127-v1"
P=127
MODEL_SHA="4a7c1d93e65079912c66ad3370ba7cf59c3c5ef7d385c7cf69ba3cde76dac8e4"
COMPRESS_SHA="b1d3dbedd597a8019bab2dca6ff59bfa915aaa457a8ac0c14833266f449a1ee9"
PARENT_SOURCE_SHA="bf5fa8e6ea1a70ed9441cf28918c9bd46946661afd932c7888f713dc2eadc936"
PARENT_BINDING="1fdb39f00f53e51f33cbecef6c25c503c43e85575ad79abbd189ade9fdc7d069"
PARENT_FORMAT="r150-original-complete-weight8-source-frontier127-v1"
MODEL_BINDING="7c59f3f6e05c836aa97eef0ad358eaae8f8174c8225b1842ed5c4f313000f3d4"
MEAN_BINDING="9502b11bf94390e8833cdc236a1ad85746d9823f9f4fe1e62de60f1932434bfd"
MODEL_MANIFEST={"bytes":30466,"sha256":"9120695ac2e42f8300fdea4aa814183bc033d83062810a8854998a25199795e2"}
PINS={"all-original-row-input.bin":{"bytes":24496256,"sha256":"b9c8085459685cdf728e9ba8cbc005daccfc80a0d8047ddccddb008e4002249a"},
 "complete-original-dictionaries.json":{"bytes":586948,"sha256":"4164b25bfaa7504c12cb40d20fa3f9d22887d71b75bae943121808a4fc686ab0"},
 "complete-row-result.bin":{"bytes":113472,"sha256":"c866eab92a0aa9a5c451b96135647a6391b9f6dc242b5ae9fa03aa9da54eb36d"}}
class Budget(Exception):pass
def need(b,s):
 if not b:raise ValueError(s)
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")
def sha(b):return hashlib.sha256(b).hexdigest()
def identity(p):
 h=hashlib.sha256()
 with p.open("rb") as f:
  for b in iter(lambda:f.read(1048576),b""):h.update(b)
 return {"path":p.name,"bytes":p.stat().st_size,"sha256":h.hexdigest()}
def exact(p,d):
 z=identity(p);need(z["bytes"]==d["bytes"] and z["sha256"]==d["sha256"],"whole exact file "+p.name);return z
def atomic(p,b):
 p.parent.mkdir(parents=True,exist_ok=True);q=p.with_name(p.name+".tmp");q.write_bytes(b);os.replace(q,p)
def load_module(p,digest,name):
 need(identity(p)["sha256"]==digest,"exact original helper "+p.name)
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def phase_read(p,d,binding,format0):
 exact(p,d);b=gzip.decompress(p.read_bytes());need(len(b)==d["logicalBytes"] and sha(b)==d["logicalSha256"],"whole original logical phase")
 x=json.loads(b);need(x["binding"]==binding and x["format"]==format0+"-phase","original phase semantic identity");return x["data"]
def main():
 ap=argparse.ArgumentParser()
 for n in ("model-source","model-out","compression-source","weight8-source","weight8-out","mean-frontier-out","out"):ap.add_argument("--"+n,type=Path,required=True)
 ap.add_argument("--through",choices=("inspect","final"),default="final");ap.add_argument("--seconds",type=float,default=120);ap.add_argument("--memory-mib",type=int,default=768);a=ap.parse_args()
 need(0<a.seconds<=300 and 512<=a.memory_mib<=1024,"bounded small original exchange")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2);started=time.monotonic();deadline=started+a.seconds;a.out.mkdir(parents=True,exist_ok=True)
 semantic={"format":FORMAT,"source":identity(Path(__file__)),"modelSourceSHA256":MODEL_SHA,"compressionSourceSHA256":COMPRESS_SHA,"parentSourceSHA256":PARENT_SOURCE_SHA,"parentBinding":PARENT_BINDING,"originalNativeFiles":PINS,"oldHighInputPositions":list(range(1092,1106)),"completeKernelCount":74,"prime":P,"coefficientRoot":100}
 binding=sha(canon(semantic));mp=a.out/"original-high-exchange-manifest.json";state={"format":FORMAT+"-manifest","binding":binding,"semantic":semantic,"phases":{}}
 if mp.exists():
  state=json.loads(mp.read_bytes());need(state["binding"]==binding and state["semantic"]==semantic,"same complete exchange continuation")
 rec={"format":FORMAT,"binding":binding,"source":semantic["source"],"status":"running","parameters":{"through":a.through,"seconds":a.seconds,"memoryMiB":a.memory_mib,"onlyFiniteFieldSourceExchange":True,"unitOrStableClosureClaim":False,"characteristicZeroClaim":False}}
 def flush():atomic(mp,canon(state))
 def phase(name,x):
  b=canon({"format":FORMAT+"-phase","binding":binding,"data":x});p=a.out/(name+".json.gz");atomic(p,gzip.compress(b,compresslevel=1,mtime=0));d={**identity(p),"logicalBytes":len(b),"logicalSha256":sha(b)};state["phases"][name]=d;flush();return d
 def tick():
  if time.monotonic()>deadline-5:raise Budget("complete small exchange phase budget")
 def alarm(sig=None,frame=None):raise Budget("actual exchange budget")
 def event(name,**kw):print(json.dumps({"phase":name,"elapsedSeconds":time.monotonic()-started,**kw},separators=(",",":")),flush=True)
 signal.signal(signal.SIGALRM,alarm);signal.setitimer(signal.ITIMER_REAL,a.seconds);code=1
 try:
  c=load_module(a.compression_source,COMPRESS_SHA,"high_exchange_parse");need(identity(a.weight8_source)["sha256"]==PARENT_SOURCE_SHA,"exact original weight8 producer")
  pm=json.loads((a.weight8_out/"complete-weight8-frontier-manifest.json").read_bytes());pr=json.loads((a.weight8_out/"complete-weight8-frontier-receipt.json").read_bytes())
  need(pm["binding"]==PARENT_BINDING and pr["binding"]==PARENT_BINDING and pm["format"]==PARENT_FORMAT+"-manifest" and pr["status"]=="completed" and pr["source"]["sha256"]==PARENT_SOURCE_SHA,"complete paid original weight8 parent")
  exact(a.weight8_out/"complete-weight8-frontier-manifest.json",pr["parameters"]["manifest"])
  need(all(pr["parameters"][k] for k in ("all100Original18ProductsVerified","all100CompleteParameterRelationsVerified","all100Original18RelationProductsVerified")),"all original parent source products paid")
  nd=a.weight8_out/"complete-weight8";files={n:exact(nd/n,d) for n,d in PINS.items()};dictionary=json.loads((nd/"complete-original-dictionaries.json").read_bytes());labels=dictionary["inputs"]
  need(len(labels)==1386 and len(dictionary["outputs"])==17674 and dictionary["firstNewOriginalTarget"]==1286,"same complete original dictionary")
  rr=c.parse_result(nd/"complete-row-result.bin",pm["native"]["binding"],17674,1386,1286)
  need(rr["next"]==1386 and rr["rank"]==1312 and len(rr["relations"])==74 and sum(k<1286 for k in rr["independentOriginalRows"])==1286,"paid complete74 kernel and independent1286 prefix")
  dpos=list(range(1092,1106));need(len({labels[k][0] for k in dpos})==14 and all(labels[k][0].startswith("paid-") and labels[k][1]==[0]*12 for k in dpos),"fourteen literal old high generators")
  depids=sorted(rr["relations"]);old=[rr["relations"][k] for k in depids];q=[r.copy() for r in old];trans=[[int(i==j) for j in range(74)] for i in range(74)];origin=list(range(74));piv=[];rank=0;unitchecks=0
  for col in dpos:
   tick();sel=next((j for j in range(rank,74) if q[j][col]),None)
   if sel is None:continue
   for a0 in (q,trans,origin):a0[rank],a0[sel]=a0[sel],a0[rank]
   inv=pow(q[rank][col],P-2,P);q[rank]=[(v*inv)%P for v in q[rank]];trans[rank]=[(v*inv)%P for v in trans[rank]];need(q[rank][col]==1,"actual normalized old-high pivot");unitchecks+=1
   for j in range(74):
    if j==rank or not q[j][col]:continue
    a0=q[j][col];q[j]=[(x-a0*y)%P for x,y in zip(q[j],q[rank])];trans[j]=[(x-a0*y)%P for x,y in zip(trans[j],trans[rank])];need(q[j][col]==0,"complete original small pivot cancellation")
   piv.append(col);rank+=1
  selected=[depids[origin[j]] for j in range(rank)];selected_set={origin[j] for j in range(rank)};products=0
  for j in range(rank):
   tick();active=[(k,v) for k,v in enumerate(trans[j]) if v];need(all(k in selected_set for k,v in active),"only selected actual dependent targets enter the exchange")
   for k in range(1386):
    need(sum(v*old[h][k] for h,v in active)%P==q[j][k],"all1386 coordinates of original kernel row combination");products+=1
   need(all(q[j][col]==int(j==l) for l,col in enumerate(piv)),"all pivot-old-high coordinates identity")
   need(all(not q[j][k] for k in depids if k not in selected),"no unselected dependent source in exchange")
  need(all(not any(q[j][col] for col in dpos) for j in range(rank,74)),"complete74 projected rows exhausted")
  inspection={"parentBinding":PARENT_BINDING,"allOriginalKernelTargetIndices":depids,"originalHighInputPositions":dpos,"projectedRank":rank,"pivotOldHighInputPositions":piv,"pivotOldHighKeys":[labels[k][0] for k in piv],"selectedReplacementTargetInputPositions":selected,"selectedReplacementKeys":[labels[k][0] for k in selected],"allSelectedOriginalKernelCombinations":trans[:rank],"completeExchangeRows":q[:rank],"allOriginalCombinationCoordinateProducts":products,"allProductsVerified":True,"completeRemainingHighCodimension":14-rank,"inputFiles":files}
  if "complete-small-projection" in state["phases"]:
   z=phase_read(a.out/state["phases"]["complete-small-projection"]["path"],state["phases"]["complete-small-projection"],binding,FORMAT);need(z==inspection,"same exact complete projected kernel")
  else:phase("complete-small-projection",inspection)
  rec["parameters"].update(projectedRank=rank,remainingHighCodimension=14-rank,allOriginalCombinationCoordinateProducts=products,allOriginalSmallProductsVerified=True,originalInputs=files);event("complete-small-projection",rank=rank,removedOriginalHigh=rank,addedOriginalTargets=rank)
  if a.through=="inspect":rec["status"]="completed-prefix";code=0;return code
  m=load_module(a.model_source,MODEL_SHA,"high_exchange_model");exact(a.model_out/"original-parameter-module-manifest.json",MODEL_MANIFEST);mm=json.loads((a.model_out/"original-parameter-module-manifest.json").read_bytes());need(mm["binding"]==MODEL_BINDING,"same original model")
  bd=mm["phases"]["complete-original-ten-parameter-action127"];base=m.load_gz(a.model_out/bd["path"],bd,MODEL_BINDING);A=m.unpackvec(base["allOriginal18Generators"]);cache={}
  mean_desc=pm["inputs"]["all30MeanPhaseDescriptors"]
  def fetch(key):
   if key in cache:return cache[key]
   tick()
   if key.startswith("paid-"):
    sid=int(key[5:]);d=mm["seeds"][sid];z=m.load_gz(a.model_out/d["path"],d,MODEL_BINDING);need(z["seedIndex"]==sid,"literal original paid source")
   elif key.startswith("frontier-"):
    d=mean_desc[key];z=phase_read(a.mean_frontier_out/d["path"],d,MEAN_BINDING,"r150-original-mean-first-source-frontier127-v1")
   else:
    need(key.startswith("weight8-"),"only literal original weight8 sources");d=pm["phases"][key];z=phase_read(a.weight8_out/d["path"],d,PARENT_BINDING,PARENT_FORMAT)
   v=m.unpackvec(z["vector"]);s=m.unpackvec(z["original18Source"]);need(len(v)==10 and len(s)==18 and m.dot(m.MON,v)==m.dot(A,s),"complete actual input source product");cache[key]=(v,s);return v,s
  out=[];before_terms=after_terms=0
  for j,col in enumerate(piv):
   tick();key=labels[col][0];v,s=fetch(key);coeff={}
   for k,a0 in enumerate(q[j]):
    if not a0 or k==col:continue
    kk,e=labels[k];need(kk not in [labels[h][0] for h in piv],"all removed high source keys absent from replacement")
    coeff[kk]=coeff.get(kk,m.ZERO)-int(a0)*c.mon(m,e)
   coeff={k:v0 for k,v0 in coeff.items() if v0!=0}
   for kk in coeff:fetch(kk)
   vv=[sum((co*cache[kk][0][axis] for kk,co in coeff.items()),m.ZERO) for axis in range(10)];need(vv==v,"all ten complete parameter source exchange coordinates")
   ss=[sum((co*cache[kk][1][axis] for kk,co in coeff.items()),m.ZERO) for axis in range(18)];need(m.dot(A,ss)==m.dot(m.MON,v),"all original18 source exchange products")
   z={"removedOriginalKey":key,"coefficients":[[kk,m.pack(co)] for kk,co in sorted(coeff.items())],"replacementOriginal18Source":m.packvec(ss),"allTenCoordinatesVerified":True,"allOriginal18ProductVerified":True}
   name="complete-exchange-%02d"%j
   if name in state["phases"]:need(phase_read(a.out/state["phases"][name]["path"],state["phases"][name],binding,FORMAT)==z,"same exact full source exchange")
   else:phase(name,z)
   out.append(name);before_terms+=sum(len(x.to_dict()) for x in v)
   rv,rs=fetch(labels[selected[j]][0]);after_terms+=sum(len(x.to_dict()) for x in rv)
   event(name,removed=key,added=labels[selected[j]][0])
  cert={"projectedRank":rank,"allOriginalKernelCombinationsVerified":True,"allExchangesVerified":True,"removedOriginalHighKeys":[labels[k][0] for k in piv],"addedOriginalImageKeys":[labels[k][0] for k in selected],"allExchangePhases":out,"oldGeneratorCount":106,"newGeneratorCount":106,"removedVectorTermTotal":before_terms,"addedVectorTermTotal":after_terms,"completeSameParameterModule":True,"notAUnitStableOrCharacteristicZeroClaim":True}
  d=phase("complete-original-high-source-exchange",cert);rec["status"]="completed";rec["parameters"].update(allTenCoordinateExchangesVerified=True,allOriginal18ExchangesVerified=True,sameGeneratorCount=106,removedVectorTermTotal=before_terms,addedVectorTermTotal=after_terms,certificate=d);code=0;return code
 except Budget as e:rec["status"]="budget-checkpoint";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};code=75;return code
 except BaseException as e:rec["status"]="failed";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};code=1;return code
 finally:
  signal.setitimer(signal.ITIMER_REAL,0);flush();rec["elapsedSeconds"]=time.monotonic()-started;rec["peakRssKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss;rec["parameters"]["manifest"]=identity(mp);rec["parameters"]["completePhases"]=state["phases"];atomic(a.out/"original-high-exchange-receipt.json",canon(rec));print(canon(rec).decode(),flush=True)
if __name__=="__main__":sys.exit(main())
