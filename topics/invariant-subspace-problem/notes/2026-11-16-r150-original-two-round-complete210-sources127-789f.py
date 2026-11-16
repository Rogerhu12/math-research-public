#!/usr/bin/env python3
"""Produce the 104 remaining exact original columns of the complete 210 model.

Author: Astra-ISP-789f / normal_annihilator, with /root.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.
This reads the paid original 106 columns and the actual first-image phases.
Only four literal quadratic paths times six means and twenty low commutators
are new. Each full ten-vector and eighteen-source product is checked before
an atomic phase is registered. No weighted matrix or Groebner basis is built.
The two-round completeness theorem is separate from these arithmetic products.
No E lift, unit ideal, or Bell natural-power identity is claimed by this source.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,os,resource,signal,sys,time,zlib
from collections import OrderedDict
from pathlib import Path

sys.set_int_max_str_digits(0)
FORMAT="r150-original-two-round-complete210-sources127-v1"
MODEL_SHA="4a7c1d93e65079912c66ad3370ba7cf59c3c5ef7d385c7cf69ba3cde76dac8e4"
COMPRESS_SHA="b1d3dbedd597a8019bab2dca6ff59bfa915aaa457a8ac0c14833266f449a1ee9"
MEAN_SHA="810904a2c797b08493ed377c069abd75018e0a0df8035cb700baad80616bea1e"
WEIGHT8_SHA="bf5fa8e6ea1a70ed9441cf28918c9bd46946661afd932c7888f713dc2eadc936"
MODEL_BINDING="7c59f3f6e05c836aa97eef0ad358eaae8f8174c8225b1842ed5c4f313000f3d4"
MODEL_MANIFEST={"bytes":30466,"sha256":"9120695ac2e42f8300fdea4aa814183bc033d83062810a8854998a25199795e2"}
COMPRESS_BINDING="baaa8ec3f9459c0d2f88ebb452c941ce241f2727d5becab1ca78511a55a589ca"
COMPRESS_MATH={"bytes":620742,"sha256":"a1d73ea1ce5809c87bdc34724c1eb4407d6a5c0ae78fbf16aa3650563aa089dd"}
MEAN_BINDING="9502b11bf94390e8833cdc236a1ad85746d9823f9f4fe1e62de60f1932434bfd"
MEAN_MATH={"bytes":7561,"sha256":"84602b544bc3a7275ba3e0d4aa6cbcdfb87eb01c29f5ddca045a344e3144c2df"}
WEIGHT8_BINDING="1fdb39f00f53e51f33cbecef6c25c503c43e85575ad79abbd189ade9fdc7d069"
WEIGHT8_PHASES={"bytes":25501,"sha256":"3f2c8d3b78df200d460c88a81ed9400ce20c84fb3040587f4cb51ec8709ad1b4"}
WEIGHT8_MATH={"bytes":1838728,"sha256":"875b3bced3dec064a7312e8c09ffdc19a329bc9608a831a798edd6610df40cf3"}
WEIGHT8_MATH_KEYS=("parentBinding","meanFrontierBinding","compressionBinding","prime","coefficientRoot","completeOldColumns","allOutputRows","allInputColumns","allYMeanColumns","previousColumns","actualRank","oldRank","prefixRank","all100CommutatorImages","keptNewSourceKeys","all100Expressions","allOriginalSourceRelationsVerified","originalFiftyPlusAllThirtyPlusAllHundredEqualsSameWithRetained")
FORMATS={"model":"r150-original-ten-generator-complete-parameter-seeds127-v2",
 "compression":"r150-original-complete-parameter-seed-compression127-v1",
 "mean":"r150-original-mean-first-source-frontier127-v1",
 "weight8":"r150-original-complete-weight8-source-frontier127-v1"}
KEEP=((1,4),(2,3),(2,4),(3,4))
LOW_IDS=(1,2,3,4,5,11,12,13,14,15,21,22,23,24,25,31,32,33,34,35)
HIGH_IDS=(6,7,8,9,16,17,18,19,26,27,28,29,36,37)
WEIGHTS=(0,2,2,2,2,2,4,4,4,4)
P=127

class Budget(Exception):pass
def need(b,s):
 if not b:raise ValueError(s)
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")
def sha(b):return hashlib.sha256(b).hexdigest()
def identity(p):
 p=Path(p);h=hashlib.sha256()
 with p.open("rb") as f:
  for b in iter(lambda:f.read(1048576),b""):h.update(b)
 return {"path":p.name,"bytes":p.stat().st_size,"sha256":h.hexdigest()}
def exact(p,d):
 a=identity(p);need(a["bytes"]==d["bytes"] and a["sha256"]==d["sha256"],"whole exact file "+Path(p).name);return a
def atomic(p,b):
 p.parent.mkdir(parents=True,exist_ok=True);q=p.with_name(p.name+".tmp");q.write_bytes(b);os.replace(q,p)
def save_json(p,x):atomic(p,canon(x));return identity(p)
def check_math(x,d,name):
 b=canon(x);need(len(b)==d["bytes"] and sha(b)==d["sha256"],"complete fixed mathematics "+name)
def read_phase(root,d,binding,fmt):
 p=root/d["path"];exact(p,d);raw=gzip.decompress(p.read_bytes())
 need(len(raw)==d["logicalBytes"] and sha(raw)==d["logicalSha256"],"whole logical phase "+p.name)
 z=json.loads(raw);need(z["format"]==fmt+"-phase" and z["binding"]==binding,"exact phase format and binding "+p.name)
 return z["data"]
def import_model(p):
 need(identity(p)["sha256"]==MODEL_SHA,"exact original model helper")
 s=importlib.util.spec_from_file_location("original_complete210_model",p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def main():
 ap=argparse.ArgumentParser()
 for name in ("model-source","model-out","compression-source","compression-out","mean-frontier-source","mean-frontier-out","weight8-source","weight8-out","out"):
  ap.add_argument("--"+name,type=Path,required=True)
 ap.add_argument("--through",choices=("prepare","mean","final"),default="final")
 ap.add_argument("--seconds",type=float,default=300)
 ap.add_argument("--memory-mib",type=int,default=1024)
 a=ap.parse_args();need(0<a.seconds<=900 and 512<=a.memory_mib<=2048,"bounded complete210 producer parameters")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
 started=time.monotonic();deadline=started+a.seconds;a.out.mkdir(parents=True,exist_ok=True)
 own=identity(Path(__file__))
 semantic={"format":FORMAT,"source":own,"prime":P,"coefficientRoot":100,
  "modelSourceSHA256":MODEL_SHA,"modelBinding":MODEL_BINDING,"modelManifest":MODEL_MANIFEST,
  "compressionSourceSHA256":COMPRESS_SHA,"compressionBinding":COMPRESS_BINDING,"compressionMathematics":COMPRESS_MATH,
  "meanSourceSHA256":MEAN_SHA,"meanBinding":MEAN_BINDING,"all30MeanPhaseDescriptors":MEAN_MATH,
  "weight8SourceSHA256":WEIGHT8_SHA,"weight8Binding":WEIGHT8_BINDING,"all100Weight8PhaseDescriptors":WEIGHT8_PHASES,"weight8Mathematics":WEIGHT8_MATH,
  "literalQuadraticPaths":[list(x) for x in KEEP],"originalLowCommutatorSeedIndices":list(LOW_IDS),"originalHighCommutatorSeedIndices":list(HIGH_IDS),
  "parentColumns":106,"newMeanColumns":24,"newCommutatorColumns":80,"completeColumns":210,
  "sourceRecurrence":"sigma(Np*v)=up*sigma(v)-Sp*v","arithmeticScope":"complete original ten-vector and eighteen-source products"}
 binding=sha(canon(semantic));mp=a.out/"complete210-sources-manifest.json"
 state={"format":FORMAT+"-manifest","binding":binding,"semantic":semantic,"phases":{}}
 if mp.exists():
  state=json.loads(mp.read_bytes());need(state["format"]==FORMAT+"-manifest" and state["binding"]==binding and state["semantic"]==semantic,"same exact complete210 continuation")
 rec={"format":FORMAT,"binding":binding,"source":own,"status":"running","parameters":{"through":a.through,"seconds":a.seconds,"memoryMiB":a.memory_mib,
  "noNewWeightedMatrix":True,"noNewRankOrGroebnerComputation":True,"unitIdealClaimed":False,"characteristicZeroLiftClaimed":False,
  "completenessTheoremIsSeparateFromThisArithmeticRun":True}}
 counts={"newOriginal18ProductsThisRun":0,"reusedVerifiedNewColumns":0,"all106OriginalProductsThisRun":0,"parentFirstImagesIndependentlyReplayedThisRun":0}
 def remaining():return deadline-time.monotonic()
 def tick():
  if remaining()<8:raise Budget("whole original source phase budget")
 def alarm(sig=None,frame=None):raise Budget("actual complete210 source budget")
 def flush():save_json(mp,state)
 def event(name,**kw):
  rec["parameters"]["lastWholePhase"]=name
  print(json.dumps({"phase":name,"elapsedSeconds":time.monotonic()-started,"peakRssKiB":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,**kw},separators=(",",":")),flush=True)
 def phase(name,data):
  raw=canon({"format":FORMAT+"-phase","binding":binding,"data":data});p=a.out/(name+".json.gz")
  atomic(p,gzip.compress(raw,compresslevel=1,mtime=0));d={**identity(p),"logicalBytes":len(raw),"logicalSha256":sha(raw)}
  state["phases"][name]=d;flush();return d
 def get_phase(name):return read_phase(a.out,state["phases"][name],binding,FORMAT)
 signal.signal(signal.SIGALRM,alarm);signal.setitimer(signal.ITIMER_REAL,a.seconds);code=1
 try:
  need(tuple(sys.version_info[:3])==(3,12,14),"same pinned Python3.12.14 gzip runtime")
  import flint
  need(flint.__version__=="0.9.0","same python-flint0.9.0")
  rec["parameters"]["runtime"]={"python":sys.version.split()[0],"pythonFlint":flint.__version__,"zlib":zlib.ZLIB_VERSION,"gzipOSByte":gzip.compress(b"identity",mtime=0)[9]}
  m=import_model(a.model_source)
  for path,digest in ((a.compression_source,COMPRESS_SHA),(a.mean_frontier_source,MEAN_SHA),(a.weight8_source,WEIGHT8_SHA)):
   need(identity(path)["sha256"]==digest,"same complete parent source "+path.name)
  exact(a.model_out/"original-parameter-module-manifest.json",MODEL_MANIFEST)
  roots={"model":a.model_out,"compression":a.compression_out,"mean":a.mean_frontier_out,"weight8":a.weight8_out}
  names={"model":("original-parameter-module-manifest.json","original-parameter-module-receipt.json"),
   "compression":("complete-parameter-seed-compression-manifest.json","complete-parameter-seed-compression-receipt.json"),
   "mean":("original-mean-frontier-manifest.json","original-mean-frontier-receipt.json"),
   "weight8":("complete-weight8-frontier-manifest.json","complete-weight8-frontier-receipt.json")}
  bindings={"model":MODEL_BINDING,"compression":COMPRESS_BINDING,"mean":MEAN_BINDING,"weight8":WEIGHT8_BINDING}
  digests={"model":MODEL_SHA,"compression":COMPRESS_SHA,"mean":MEAN_SHA,"weight8":WEIGHT8_SHA}
  parents={};executions={}
  for tag,(mn,rn) in names.items():
   pm=json.loads((roots[tag]/mn).read_bytes());pr=json.loads((roots[tag]/rn).read_bytes())
   need(pm["format"]==FORMATS[tag]+"-manifest" and pm["binding"]==bindings[tag] and pr["binding"]==bindings[tag] and pr["source"]["sha256"]==digests[tag] and pr["status"]=="completed","same completed parent "+tag)
   exact(roots[tag]/mn,pr["parameters"]["manifest"])
   parents[tag]=pm;executions[tag]={"manifest":identity(roots[tag]/mn),"receipt":identity(roots[tag]/rn)}
  pm=parents["model"];cm=parents["compression"];fm=parents["mean"];wm=parents["weight8"]
  need(len(pm["seeds"])==116,"complete original116 seed dictionary")
  cp=read_phase(a.compression_out,cm["phases"]["complete-original-compressed-parameter-seeds"],COMPRESS_BINDING,FORMATS["compression"])
  pure={k:cp[k] for k in ("parentBinding","prime","coefficientRoot","allOriginal116SeedExpansionColumns","retainedOriginalSeedIndices")}
  check_math(pure,COMPRESS_MATH,"all116 original compression")
  retained=list(range(100,106))+list(LOW_IDS)+list(HIGH_IDS)+list(range(106,116))
  need(cp["retainedOriginalSeedIndices"]==retained and len(retained)==50,"same literal50 original seed order")
  md={"frontier-i%d-mean%d"%(i,j):fm["phases"]["frontier-i%d-mean%d"%(i,j)] for i in range(5) for j in range(6)}
  check_math(md,MEAN_MATH,"all30 original mean-image descriptors")
  wk=["weight8-i%d-comm%03d"%(i,sid) for i in range(5) for sid in LOW_IDS]
  wd={k:wm["phases"][k] for k in wk};check_math(wd,WEIGHT8_PHASES,"all100 original commutator-image descriptors")
  wcert=read_phase(a.weight8_out,wm["phases"]["complete-original-weight8-frontier"],WEIGHT8_BINDING,FORMATS["weight8"])
  check_math({k:wcert[k] for k in WEIGHT8_MATH_KEYS},WEIGHT8_MATH,"complete paid weight8 rank and original relations")
  kept=wcert["keptNewSourceKeys"]
  need(wcert["actualRank"]==1312 and wcert["oldRank"]==1106 and wcert["prefixRank"]==1286 and wcert["allOriginalSourceRelationsVerified"] and wcert["originalFiftyPlusAllThirtyPlusAllHundredEqualsSameWithRetained"] and len(kept)==len(set(kept))==26 and set(kept)<=set(wk),"same complete original26 selection")
  bd=pm["phases"]["complete-original-ten-parameter-action127"]
  base=m.load_gz(a.model_out/bd["path"],bd,MODEL_BINDING)
  A,N,S,H,Hs=m.decode_base(base);U=m.CTX.gens()[12:]
  need(len(A)==18 and len(N)==len(S)==5 and all(len(q)==10 and all(len(r)==10 for r in q) for q in N) and all(len(q)==18 and all(len(r)==10 for r in q) for q in S),"all original dimensions retained")
  need(base["tenOriginalMonomials"]==[list(e) for e in m.MEXP] and tuple(m.KEEP)==KEEP and base["allNineLiteralCyclicPathsRetained"] and base["allElevenOriginalGeneratorsInBorderSubmoduleVerified"] and base["all50OriginalBorderSourceProductsVerified"],"same complete original monomial and source interpretation")
  for i in range(5):
   need([N[i][r][0] for r in range(10)]==m.unit(10,1+i),"literal original linear path")
   need(all(S[i][17][r]==0 for r in range(10)),"all borders use the original17 gradients only")
  for j,(p,q) in enumerate(KEEP):need([N[p][r][1+q] for r in range(10)]==m.unit(10,6+j),"literal original four quadratic paths")
  del base,cp,pure,wcert

  def ref(tag,key,d):return {"parent":tag,"phaseKey":key,"binding":bindings[tag],"format":FORMATS[tag],"descriptor":d}
  seed_refs={sid:ref("model","seed-%03d"%sid,pm["seeds"][sid]) for sid in retained}
  parent_refs=[{"kind":"original-seed","seedIndex":sid,**seed_refs[sid]} for sid in retained]
  parent_refs.extend({"kind":"mean-first-image","operator":i,"seedIndex":100+j,**ref("mean",key,md[key])} for i in range(5) for j in range(6) for key in ["frontier-i%d-mean%d"%(i,j)])
  for key in kept:
   zz=key.split("-");op=int(zz[1][1:]);sid=int(zz[2][4:])
   parent_refs.append({"kind":"commutator-first-image","operator":op,"seedIndex":sid,**ref("weight8",key,wd[key])})
  need(len(parent_refs)==106,"complete old50 plus30 plus26 parent columns")
  jobs=[]
  for family,ids,weight in (("mean",list(range(100,106)),9),("commutator",list(LOW_IDS),10)):
   for p,q in KEEP:
    for sid in ids:
     key="second-%s-p%d-q%d-seed%03d"%(family,p,q,sid)
     first_key="frontier-i%d-mean%d"%(q,sid-100) if family=="mean" else "weight8-i%d-comm%03d"%(q,sid)
     tag="mean" if family=="mean" else "weight8"
     jobs.append({"phaseKey":key,"family":family,"orderedOperators":[p,q],"originalSeedIndex":sid,"weight":weight,"firstImage":ref(tag,first_key,md[first_key] if tag=="mean" else wd[first_key])})
  need(len(jobs)==len({z["phaseKey"] for z in jobs})==104 and sum(z["family"]=="mean" for z in jobs)==24,"complete104 literal new source dictionary")
  parent_math={"base":bd,"old106":parent_refs,"new104":jobs}
  if "parentMathematics" in state:need(state["parentMathematics"]==parent_math,"same whole original input references")
  else:state["parentMathematics"]=parent_math;flush()
  rec["parameters"]["actualParentExecutions"]=executions
  seed_cache={};first_cache=OrderedDict();first_verified=set()
  def homogeneous(v,w):
   return all(not any(e[12:]) and sum(e[:6])+2*sum(e[6:12])+WEIGHTS[k]==w for k,f in enumerate(v) for e in f.to_dict())
  def seed(sid):
   if sid in seed_cache:return seed_cache[sid]
   z=m.load_gz(a.model_out/pm["seeds"][sid]["path"],pm["seeds"][sid],MODEL_BINDING)
   need(z["seedIndex"]==sid and z["fullOriginal18ProductVerified"] and z["allTenParameterCoordinatesRetained"],"same complete original seed")
   v=m.unpackvec(z["vector"]);s=m.unpackvec(z["original18Source"])
   need(len(v)==10 and len(s)==18,"complete original seed dimensions")
   if sid<106:
    w=5 if sid>=100 else (6 if sid in LOW_IDS else 8)
    need(homogeneous(v,w) and s[17]==0,"original nonBell seed weight and source")
   else:need(v==m.scale(m.unit(10,sid-106),A[17]) and s==m.scale(m.unit(18,17),m.MON[sid-106]),"all10 original Bell columns")
   seed_cache[sid]=(v,s);return v,s
  def first(tag,key,op,sid):
   ck=(tag,key)
   if ck in first_cache:
    z=first_cache.pop(ck);first_cache[ck]=z;return z
   d=md[key] if tag=="mean" else wd[key]
   z=read_phase(roots[tag],d,bindings[tag],FORMATS[tag]);sk="meanSeedIndex" if tag=="mean" else "commutatorSeedIndex"
   need(z["operator"]==op and z[sk]==sid and z["fullOriginal18ProductVerified"],"same literal first-image source")
   v=m.unpackvec(z["vector"]);s=m.unpackvec(z["original18Source"])
   need(len(v)==10 and len(s)==18 and s[17]==0 and homogeneous(v,7 if tag=="mean" else 8),"complete first-image coordinates and nonBell source")
   if ck not in first_verified:
    bv,bs=seed(sid)
    need(v==m.mv(N[op],bv),"all ten original first-image coordinates independently replayed")
    need(s==[U[op]*bs[k]-m.dot(S[op][k],bv) for k in range(18)],"all eighteen exact first-image source coordinates independently replayed")
    need(m.dot(m.MON,v)==m.dot(A,s),"whole original first-image polynomial product")
    first_verified.add(ck);counts["parentFirstImagesIndependentlyReplayedThisRun"]+=1
   first_cache[ck]=(v,s)
   while len(first_cache)>6:first_cache.popitem(last=False)
   return v,s

  common_name="complete-original106-parent-validation"
  if common_name in state["phases"]:
   common=get_phase(common_name)
   need(common["parentColumns"]==parent_refs and common["all106Original18ProductsVerified"] and common["all50OriginalBorderProductsVerified"] and common["allNineLiteralPathsVerified"],"whole previous original106 validation")
   event("reused-whole-original106-validation")
  else:
   for i in range(5):
    for j in range(10):
     tick();need(m.dot(m.MON,[N[i][k][j] for k in range(10)])==U[i]*m.MON[j]-m.dot(A,[S[i][k][j] for k in range(18)]),"all50 complete original border products")
   metadata=[]
   for rr in parent_refs:
    tick()
    if rr["kind"]=="original-seed":v,s=seed(rr["seedIndex"])
    else:v,s=first(rr["parent"],rr["phaseKey"],rr["operator"],rr["seedIndex"])
    need(m.dot(m.MON,v)==m.dot(A,s),"all106 original parent polynomial products")
    counts["all106OriginalProductsThisRun"]+=1
    metadata.append({"vectorTerms":sum(len(f.to_dict()) for f in v),"sourceTerms":sum(len(f.to_dict()) for f in s)})
   common={"parentColumns":parent_refs,"all106Original18ProductsVerified":True,"all50OriginalBorderProductsVerified":True,"allNineLiteralPathsVerified":True,"parentColumnTermCounts":metadata}
   phase(common_name,common);event(common_name,originalParentColumns=106)
  rec["parameters"]["all106OriginalParentColumnsVerified"]=True
  if a.through=="prepare":
   rec["status"]="completed-prefix";rec["parameters"]["outcome"]="whole original106 parent and104 literal source dictionary verified; new104 not yet produced";code=0;return code

  limit=24 if a.through=="mean" else 104
  for job in jobs[:limit]:
   tick();name=job["phaseKey"]
   if name in state["phases"]:
    z=get_phase(name)
    need(z["literalSource"]==job and z["allTenImageCoordinatesVerified"] and z["fullOriginal18ProductVerified"] and z["originalBellSourceIsZero"] and z["allTwelveParametersRetained"],"same complete previously verified second image")
    counts["reusedVerifiedNewColumns"]+=1;event("reused-"+name);continue
   p,q=job["orderedOperators"];rr=job["firstImage"]
   v1,s1=first(rr["parent"],rr["phaseKey"],q,job["originalSeedIndex"])
   v2=m.mv(N[p],v1)
   s2=[U[p]*s1[k]-m.dot(S[p][k],v1) for k in range(18)]
   need(len(v2)==10 and len(s2)==18 and s2[17]==0,"all new ten/eighteen coordinates and no Bell source")
   need(homogeneous(v2,job["weight"]),"every original second-image monomial has the exact declared weight")
   need(m.dot(m.MON,v2)==m.dot(A,s2),"whole original eighteen-generator second-image product")
   vt=sum(len(f.to_dict()) for f in v2);st=sum(len(f.to_dict()) for f in s2)
   maxv,maxs=(37874,16442) if job["family"]=="mean" else (77276,46304)
   need(vt<=maxv and st<=maxs,"whole ordinary monomial count bound")
   data={"literalSource":job,"vector":m.packvec(v2),"original18Source":m.packvec(s2),
    "allTenImageCoordinatesVerified":True,"fullOriginal18ProductVerified":True,"originalBellSourceIsZero":True,"allTwelveParametersRetained":True,
    "vectorTerms":vt,"sourceTerms":st,"sourceMaximumUDegree":max((sum(e[12:]) for f in s2 for e in f.to_dict()),default=0)}
   phase(name,data);counts["newOriginal18ProductsThisRun"]+=1
   event(name,vectorTerms=vt,sourceTerms=st,sourceMaximumUDegree=data["sourceMaximumUDegree"])
   del v2,s2,data
  if a.through=="mean":
   rec["status"]="completed-prefix";rec["parameters"]["outcome"]="all24 original quadratic-path mean images; remaining80 not asserted";code=0;return code
  allrefs=[];vsum=ssum=maxud=0
  for job in jobs:
   tick();z=get_phase(job["phaseKey"])
   need(z["literalSource"]==job and z["allTenImageCoordinatesVerified"] and z["fullOriginal18ProductVerified"] and z["originalBellSourceIsZero"],"complete new104 final closure")
   allrefs.append({"literalSource":job,"descriptor":state["phases"][job["phaseKey"]],"vectorTerms":z["vectorTerms"],"sourceTerms":z["sourceTerms"],"sourceMaximumUDegree":z["sourceMaximumUDegree"]})
   vsum+=z["vectorTerms"];ssum+=z["sourceTerms"];maxud=max(maxud,z["sourceMaximumUDegree"])
  final={"prime":P,"coefficientRoot":100,"parentColumns":parent_refs,"newColumns":allrefs,"allColumnCount":210,
   "all106ParentSourcesVerified":True,"all104NewTenVectorsVerified":True,"all104NewOriginal18ProductsVerified":True,"all104NewBellSourceCoefficientsZero":True,
   "newVectorTermTotal":vsum,"newSourceTermTotal":ssum,"newSourceMaximumUDegree":maxud,
   "completeModelMeaning":"P1 plus the four literal quadratic paths on six means and twenty low commutators; two-round completeness is proved separately",
   "parameterOnlyVectors":True,"characteristicZeroLiftClaimed":False,"unitIdealClaimed":False,"newWeightedRankPerformed":False}
  fn="complete-original210-source-model"
  if fn in state["phases"]:need(get_phase(fn)==final,"same complete210 final source model")
  else:phase(fn,final)
  rec["parameters"].update(all104NewOriginal18ProductsVerified=True,all104TenVectorsVerified=True,all210OriginalSourcesVerified=True,
   newVectorTermTotal=vsum,newSourceTermTotal=ssum,newSourceMaximumUDegree=maxud,completeModel=state["phases"][fn])
  rec["status"]="completed";code=0;event(fn,columns=210,newColumns=104);return code
 except Budget as e:
  rec["status"]="budget-checkpoint";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};code=75;return code
 except BaseException as e:
  rec["status"]="memory-error" if isinstance(e,MemoryError) else "error"
  rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};code=1;return code
 finally:
  signal.setitimer(signal.ITIMER_REAL,0)
  flush();rec["elapsedSeconds"]=time.monotonic()-started;rec["peakRssKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
  rec["parameters"].update(counts)
  rec["parameters"]["completeNewMeanColumns"]=sum(k.startswith("second-mean-") for k in state["phases"])
  rec["parameters"]["completeNewCommutatorColumns"]=sum(k.startswith("second-commutator-") for k in state["phases"])
  rec["parameters"]["completePhases"]=state["phases"];rec["parameters"]["manifest"]=identity(mp)
  save_json(a.out/"complete210-sources-receipt.json",rec)
  print(json.dumps({"receipt":rec},sort_keys=True,separators=(",",":")),flush=True)
if __name__=="__main__":sys.exit(main())
