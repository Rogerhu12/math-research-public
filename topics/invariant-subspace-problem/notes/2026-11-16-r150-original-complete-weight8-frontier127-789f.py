#!/usr/bin/env python3
"""Complete weight-eight source frontier: G8, all y*NiY, and all Ni*C6.

Author: Astra-ISP-789f / normal_annihilator, with /root.
AI-assisted GPT-6 Astra Pro. 2026-11-16.
This is a bounded F127 source computation, never a stable-closure or unit test.
The complete 1106 old columns and all180 y*NiY columns precede all100 Ni*C6.
Every new source is ui*sigma(C6)-Si*C6. Only actual full parameter and original
18-generator products allow a new column to be omitted. Arrays stay temporary.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,os,resource,signal,struct,subprocess,sys,time
from pathlib import Path
sys.set_int_max_str_digits(0)
FORMAT="r150-original-complete-weight8-source-frontier127-v1"
MODEL_SHA="4a7c1d93e65079912c66ad3370ba7cf59c3c5ef7d385c7cf69ba3cde76dac8e4"
COMPRESS_SHA="b1d3dbedd597a8019bab2dca6ff59bfa915aaa457a8ac0c14833266f449a1ee9"
NATIVE_SHA="c5c36af57f8d75d2aac7d42b4048be2c8f382fdbe9ed4a0ebefdf85f0c93bd9f"
HEADER_SHA="03272796bb20c883291d27c9a0b796197f8295ccd9b16552c13894657dc8afd3"
MODEL_BINDING="7c59f3f6e05c836aa97eef0ad358eaae8f8174c8225b1842ed5c4f313000f3d4"
MODEL_MANIFEST={"bytes":30466,"sha256":"9120695ac2e42f8300fdea4aa814183bc033d83062810a8854998a25199795e2"}
COMPRESS_BINDING="baaa8ec3f9459c0d2f88ebb452c941ce241f2727d5becab1ca78511a55a589ca"
COMPRESS_MATH={"bytes":620742,"sha256":"a1d73ea1ce5809c87bdc34724c1eb4407d6a5c0ae78fbf16aa3650563aa089dd"}
MEAN_SOURCE_SHA="810904a2c797b08493ed377c069abd75018e0a0df8035cb700baad80616bea1e"
MEAN_BINDING="9502b11bf94390e8833cdc236a1ad85746d9823f9f4fe1e62de60f1932434bfd"
MEAN_FORMAT="r150-original-mean-first-source-frontier127-v1"
MEAN_MATH={"bytes":7561,"sha256":"84602b544bc3a7275ba3e0d4aa6cbcdfb87eb01c29f5ddca045a344e3144c2df"}
P=127;WEIGHTS=[0]+[2]*5+[4]*4
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
 z=identity(p);need(z["bytes"]==d["bytes"] and z["sha256"]==d["sha256"],"exact whole file "+p.name);return z
def atomic(p,b):
 p.parent.mkdir(parents=True,exist_ok=True);q=p.with_name(p.name+".tmp");q.write_bytes(b);os.replace(q,p)
def save_json(p,x):atomic(p,canon(x));return identity(p)
def load_module(p,digest,name):
 need(identity(p)["sha256"]==digest,"exact helper "+p.name)
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def main():
 ap=argparse.ArgumentParser()
 for n in ("model-source","model-out","compression-source","compression-out","mean-frontier-source","mean-frontier-out","native-source","header","out"):ap.add_argument("--"+n,type=Path,required=True)
 ap.add_argument("--through",choices=("prepare","final"),default="final")
 ap.add_argument("--seconds",type=float,default=180);ap.add_argument("--memory-mib",type=int,default=768);a=ap.parse_args()
 need(0<a.seconds<=900 and 512<=a.memory_mib<=2048,"bounded complete original weight8 frontier")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
 started=time.monotonic();deadline=started+a.seconds;a.out.mkdir(parents=True,exist_ok=True);own=identity(Path(__file__))
 semantic={"format":FORMAT,"source":own,"modelSourceSHA256":MODEL_SHA,"compressionSourceSHA256":COMPRESS_SHA,"nativeSourceSHA256":NATIVE_SHA,"headerSHA256":HEADER_SHA,
  "modelBinding":MODEL_BINDING,"modelManifest":MODEL_MANIFEST,"compressionBinding":COMPRESS_BINDING,"compressionMathematics":COMPRESS_MATH,
  "meanFrontierSourceSHA256":MEAN_SOURCE_SHA,"meanFrontierBinding":MEAN_BINDING,"all30MeanPhaseDescriptors":MEAN_MATH,
  "prime":P,"coefficientRoot":100,"completeOutputWeight":8,"completeOutputRows":17674,"completeOldColumns":1106,"allYMeanColumns":180,"previousColumns":1286,"newColumns":100,
  "commutatorImages":"all i in range(5), then each actual kept6 original seed in paid order","sourceFormula":"ui*sigma(C6)-Si*C6"}
 binding=sha(canon(semantic));mp=a.out/"complete-weight8-frontier-manifest.json"
 state={"format":FORMAT+"-manifest","binding":binding,"semantic":semantic,"phases":{},"native":{}}
 if mp.exists():
  state=json.loads(mp.read_bytes());need(state["format"]==FORMAT+"-manifest" and state["binding"]==binding and state["semantic"]==semantic,"same bound original frontier continuation")
 rec={"format":FORMAT,"binding":binding,"source":own,"status":"running","parameters":{"seconds":a.seconds,"memoryMiB":a.memory_mib,"through":a.through,
  "onlyFiniteFieldSourceRelations":True,"unitIdealClaimed":False,"stableClosureClaimed":False,"characteristicZeroClaimed":False}}
 def remaining():return deadline-time.monotonic()
 def tick():
  if remaining()<8:raise Budget("whole weight8-frontier phase budget")
 def alarm(sig=None,frame=None):raise Budget("actual weight8-frontier budget")
 def flush():save_json(mp,state)
 def event(name,**kw):
  rec["parameters"]["lastWholePhase"]=name;print(json.dumps({"phase":name,"elapsedSeconds":time.monotonic()-started,"peakRssKiB":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,**kw},separators=(",",":")),flush=True)
 def phase(name,data):
  b=canon({"format":FORMAT+"-phase","binding":binding,"data":data});p=a.out/(name+".json.gz");atomic(p,gzip.compress(b,compresslevel=1,mtime=0))
  d={**identity(p),"logicalBytes":len(b),"logicalSha256":sha(b)};state["phases"][name]=d;flush();return d
 def read_phase(name):
  d=state["phases"][name];p=a.out/d["path"];exact(p,d);b=gzip.decompress(p.read_bytes());need(len(b)==d["logicalBytes"] and sha(b)==d["logicalSha256"],"whole logical frontier phase")
  z=json.loads(b);need(z["format"]==FORMAT+"-phase" and z["binding"]==binding,"same original phase binding");return z["data"]
 signal.signal(signal.SIGALRM,alarm);signal.setitimer(signal.ITIMER_REAL,a.seconds);code=1
 try:
  m=load_module(a.model_source,MODEL_SHA,"frontier_original_model");c=load_module(a.compression_source,COMPRESS_SHA,"frontier_original_compression")
  exact(a.model_out/"original-parameter-module-manifest.json",MODEL_MANIFEST)
  pm=json.loads((a.model_out/"original-parameter-module-manifest.json").read_bytes());pr=json.loads((a.model_out/"original-parameter-module-receipt.json").read_bytes())
  need(pm["binding"]==MODEL_BINDING and pr["binding"]==MODEL_BINDING and pr["status"]=="completed" and pr["source"]["sha256"]==MODEL_SHA and pr["parameters"]["all116OriginalSeedsVerified"] and len(pm["seeds"])==116,"complete original116 parent")
  cm=json.loads((a.compression_out/"complete-parameter-seed-compression-manifest.json").read_bytes());cr=json.loads((a.compression_out/"complete-parameter-seed-compression-receipt.json").read_bytes())
  exact(a.compression_out/"complete-parameter-seed-compression-manifest.json",cr["parameters"]["manifest"])
  need(cm["binding"]==COMPRESS_BINDING and cr["binding"]==COMPRESS_BINDING and cr["source"]["sha256"]==COMPRESS_SHA and cr["status"]=="completed" and cr["parameters"]["all1160ModuleCoordinatesVerified"] and cr["parameters"]["allDeletedOriginal18ProductsVerified"],"source-preserving original compression")
  d=cm["phases"]["complete-original-compressed-parameter-seeds"];cp=c.load_gz(a.compression_out/d["path"],d,COMPRESS_BINDING)
  pure={k:cp[k] for k in ("parentBinding","prime","coefficientRoot","allOriginal116SeedExpansionColumns","retainedOriginalSeedIndices")};b=canon(pure)
  need(len(b)==COMPRESS_MATH["bytes"] and sha(b)==COMPRESS_MATH["sha256"],"complete original pure compression mathematics")
  six=c.load_gz(a.compression_out/cm["phases"]["complete-weight6-seed-compression"]["path"],cm["phases"]["complete-weight6-seed-compression"],COMPRESS_BINDING)
  kept6=six["keptOriginalTargetSeedIndices"];need(len(kept6)==20 and len(set(kept6))==20 and all(i in cp["retainedOriginalSeedIndices"] for i in kept6),"twenty actual original weight-six commutators")
  eight=c.load_gz(a.compression_out/cm["phases"]["complete-weight8-seed-compression"]["path"],cm["phases"]["complete-weight8-seed-compression"],COMPRESS_BINDING)
  kept8=eight["keptOriginalTargetSeedIndices"];need(len(kept8)==14 and len(set(kept8))==14 and all(i in cp["retainedOriginalSeedIndices"] for i in kept8),"fourteen actual original weight-eight commutators")
  need(not set(kept6).intersection(kept8),"disjoint original commutator source degrees")
  need(identity(a.mean_frontier_source)["sha256"]==MEAN_SOURCE_SHA,"exact completed mean frontier source")
  fm=json.loads((a.mean_frontier_out/"original-mean-frontier-manifest.json").read_bytes());fr=json.loads((a.mean_frontier_out/"original-mean-frontier-receipt.json").read_bytes())
  exact(a.mean_frontier_out/"original-mean-frontier-manifest.json",fr["parameters"]["manifest"])
  need(fm["format"]==MEAN_FORMAT+"-manifest" and fm["binding"]==MEAN_BINDING and fr["binding"]==MEAN_BINDING and fr["source"]["sha256"]==MEAN_SOURCE_SHA and fr["status"]=="completed" and fr["parameters"]["actualRank"]==312 and fr["parameters"]["all30Original18ProductsVerified"] and fr["parameters"]["all30Original18RelationProductsVerified"],"complete actual original30 parent")
  meankeys=["frontier-i%d-mean%d"%(i,j) for i in range(5) for j in range(6)]
  md={key:fm["phases"][key] for key in meankeys};mb=canon(md)
  need(len(mb)==MEAN_MATH["bytes"] and sha(mb)==MEAN_MATH["sha256"],"all thirty exact source phase descriptors without timing metadata")
  bd=pm["phases"]["complete-original-ten-parameter-action127"];base=m.load_gz(a.model_out/bd["path"],bd,MODEL_BINDING)
  A=m.unpackvec(base["allOriginal18Generators"]);N=[[m.unpackvec(row) for row in mat] for mat in base["allFiveOriginalParameterMatrices"]];S=[[m.unpackvec(row) for row in mat] for mat in base["allFiveOriginalBorderSourceMatrices"]]
  need(len(A)==18 and len(N)==len(S)==5 and all(len(q)==10 and all(len(r)==10 for r in q) for q in N) and all(len(q)==18 and all(len(r)==10 for r in q) for q in S),"complete original multiplication/source dimensions")
  U=m.CTX.gens()[12:]
  for i in range(5):
   for j in range(10):
    tick();need(sum((m.MON[k]*N[i][k][j] for k in range(10)),m.ZERO)==U[i]*m.MON[j]-sum((A[k]*S[i][k][j] for k in range(18)),m.ZERO),"all50 exact original multiplication-source identities")
  paid_ids=list(range(100,106))+kept6+kept8;vec={};src={}
  for sid in paid_ids:
   tick();z=m.load_gz(a.model_out/pm["seeds"][sid]["path"],pm["seeds"][sid],MODEL_BINDING)
   need(z["seedIndex"]==sid and z["fullOriginal18ProductVerified"] and z["allTenParameterCoordinatesRetained"],"literal paid original seed")
   v=m.unpackvec(z["vector"]);s=m.unpackvec(z["original18Source"]);need(len(v)==10 and len(s)==18 and m.dot(m.MON,v)==m.dot(A,s),"all complete paid original products")
   vec["paid-%03d"%sid]=v;src["paid-%03d"%sid]=s
  for i in range(5):
   for j in range(6):
    tick();key="frontier-i%d-mean%d"%(i,j);pd=md[key];path=a.mean_frontier_out/pd["path"];exact(path,pd);pb=gzip.decompress(path.read_bytes())
    need(len(pb)==pd["logicalBytes"] and sha(pb)==pd["logicalSha256"],"complete original30 logical phase bytes")
    pz=json.loads(pb);need(pz["format"]==MEAN_FORMAT+"-phase" and pz["binding"]==MEAN_BINDING,"same original30 phase binding")
    z=pz["data"];need(z["operator"]==i and z["meanSeedIndex"]==100+j and z["fullOriginal18ProductVerified"],"literal original mean image")
    v=m.unpackvec(z["vector"]);s=m.unpackvec(z["original18Source"])
    need(len(v)==10 and len(s)==18 and v==[m.dot(row,vec["paid-%03d"%(100+j)]) for row in N[i]],"all original NiY vectors independently reproduced")
    need(m.dot(m.MON,v)==m.dot(A,s),"all restored original30 full source products")
    need(all(not any(e[12:]) and sum(e[:6])+2*sum(e[6:12])+WEIGHTS[k]==7 for k,f in enumerate(v) for e in f.to_dict()),"all complete original mean vectors homogeneous weight7")
    vec[key]=v;src[key]=s
  inp={"modelManifest":identity(a.model_out/"original-parameter-module-manifest.json"),"modelReceipt":identity(a.model_out/"original-parameter-module-receipt.json"),"compressionManifest":identity(a.compression_out/"complete-parameter-seed-compression-manifest.json"),"compressionReceipt":identity(a.compression_out/"complete-parameter-seed-compression-receipt.json"),"compressionPhase":d,"base":bd,"all40PaidSeedDescriptors":[pm["seeds"][i] for i in paid_ids],"meanFrontierManifest":identity(a.mean_frontier_out/"original-mean-frontier-manifest.json"),"meanFrontierReceipt":identity(a.mean_frontier_out/"original-mean-frontier-receipt.json"),"all30MeanPhaseDescriptors":md}
  if "inputs" in state:need(state["inputs"]==inp,"same actual frontier parent files")
  else:state["inputs"]=inp;flush()
  event("all-original-parents-and-multiplication-identities",paidSources=40,paidMeanProducts=30,originalBorderProducts=50)
  newkeys=[]
  for i in range(5):
   for sid in kept6:
    tick();name="weight8-i%d-comm%03d"%(i,sid);newkeys.append(name);v=vec["paid-%03d"%sid];s=src["paid-%03d"%sid]
    image=[m.dot(row,v) for row in N[i]]
    if name in state["phases"]:
     z=read_phase(name);need(z["operator"]==i and z["commutatorSeedIndex"]==sid and z["fullOriginal18ProductVerified"],"same completed original weight8 image")
     source=m.unpackvec(z["original18Source"]);need(m.unpackvec(z["vector"])==image,"all actual Ni commutator coordinates")
    else:
     source=[U[i]*s[k]-m.dot(S[i][k],v) for k in range(18)]
     need(m.dot(m.MON,image)==m.dot(A,source),"new entire original18 frontier product")
     phase(name,{"operator":i,"commutatorSeedIndex":sid,"vector":m.packvec(image),"original18Source":m.packvec(source),"fullOriginal18ProductVerified":True})
    need(len(source)==18 and m.dot(m.MON,image)==m.dot(A,source),"complete restored original18 frontier product")
    need(all(not any(e[12:]) and sum(e[:6])+2*sum(e[6:12])+WEIGHTS[k]==8 for k,f in enumerate(image) for e in f.to_dict()),"all new parameter monomials have exact original weight8")
    vec[name]=image;src[name]=source;event(name,vectorTerms=sum(len(f.to_dict()) for f in image),sourceTerms=sum(len(f.to_dict()) for f in source))
  labels=[("paid-%03d"%sid,e) for sid in range(100,106) for e in c.weighted_monomials(m,3)]+[("paid-%03d"%sid,e) for sid in kept6 for e in c.weighted_monomials(m,2)]+[("paid-%03d"%sid,(0,)*12) for sid in kept8]
  need(len(labels)==1106,"all552 mean,540 lowcomm and14 highcomm original columns")
  labels.extend((key,e) for key in meankeys for e in c.weighted_monomials(m,1))
  first=len(labels);need(first==1286,"all1106 old and180 y*NiY original columns")
  labels.extend((key,(0,)*12) for key in newkeys)
  rows=[(axis,e) for axis,w in enumerate(WEIGHTS) for e in c.weighted_monomials(m,8-w)]
  need(len(rows)==len(set(rows))==17674 and len(labels)==1386,"complete weight8 dimensions")
  dictionary={"outputs":[[axis,list(e)] for axis,e in rows],"inputs":[[key,list(e)] for key,e in labels],"firstNewOriginalTarget":first}
  db=canon(dictionary);dh=sha(db);nb=sha(canon({"parentBinding":binding,"dictionarySHA256":dh}));nd=a.out/"complete-weight8";nd.mkdir(exist_ok=True)
  ns=state["native"]
  if ns:need(ns["binding"]==nb and ns["dictionarySHA256"]==dh,"same complete frontier native dictionary")
  else:ns.update(binding=nb,dictionarySHA256=dh);flush()
  p=nd/"all-original-row-input.bin"
  if "input" in ns:exact(p,ns["input"])
  else:
   lookup={r:i for i,r in enumerate(rows)};tmp=p.with_name(p.name+".tmp")
   with tmp.open("wb") as f:
    f.write(b"R15PCI01"+struct.pack("<5I",1,len(rows),len(labels),first,P)+nb.encode("ascii"))
    for key,e in labels:
     tick();row=bytearray(len(rows))
     for axis,poly in enumerate(vec[key]):
      for ee,co in poly.to_dict().items():
       need(not any(ee[12:]),"all parameter coordinates retained");r=lookup.get((axis,tuple(ee[k]+e[k] for k in range(12))))
       need(r is not None and not row[r] and 0<int(co)<P,"every original monomial in complete declared output");row[r]=int(co)
     f.write(row)
    f.flush()
   os.replace(tmp,p);ns["input"]=identity(p);ns["dictionary"]=save_json(nd/"complete-original-dictionaries.json",dictionary);flush()
  rec["parameters"].update(all100Original18ProductsVerified=True,all30ParentMeanOriginal18ProductsVerified=True,all40ParentOriginal18ProductsVerified=True,all50OriginalMultiplicationProductsVerified=True,outputRows=17674,inputColumns=1386,previousColumns=1286,completeOldColumns=1106,allYMeanColumns=180,originalInputs=inp)
  if a.through=="prepare":rec["status"]="completed-prefix";rec["parameters"]["outcome"]="all100-original-commutator-images-and-full-weight8-input";code=0;return code
  for path,digest in ((a.native_source,NATIVE_SHA),(a.header,HEADER_SHA)):need(identity(path)["sha256"]==digest,"exact paid native arithmetic source")
  build=a.out/"build";build.mkdir(exist_ok=True);cpp=build/a.native_source.name;hdr=build/a.header.name;exe=build/"original-weight8-frontier-native"
  atomic(cpp,a.native_source.read_bytes());atomic(hdr,a.header.read_bytes())
  if "nativeBinary" in state:exact(exe,state["nativeBinary"])
  else:
   tick();q=subprocess.run(["g++","-std=c++17","-O3",str(cpp),"-o",str(exe)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=min(60,remaining()-5));atomic(build/"compile.log",q.stdout)
   need(q.returncode==0,"original frontier native compile: "+q.stdout[-1200:].decode(errors="replace"));state["nativeBinary"]=identity(exe);state["compileLog"]=identity(build/"compile.log");flush()
  result=nd/"complete-row-result.bin";cpfile=nd/"complete-row-state.bin";raw=nd/"parameter-seed-native-receipt.json"
  if "result" in ns:
   for path,key in ((result,"result"),(cpfile,"checkpoint"),(raw,"receipt")):exact(path,ns[key])
   rr=c.parse_result(result,nb,len(rows),len(labels),first)
  else:
   need(not result.exists() and not cpfile.exists(),"unregistered native prefix not adopted");rr={"next":0}
  if rr["next"]<len(labels):
   tick();need(remaining()>20,"remaining native reserve");secs=min(900,remaining()-15);signal.setitimer(signal.ITIMER_REAL,0)
   try:q=subprocess.run([str(exe),str(p),str(nd),str(secs)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=secs+8)
   finally:
    if remaining()>0:signal.setitimer(signal.ITIMER_REAL,remaining())
   atomic(nd/"last-native.log",q.stdout);need(q.returncode in (0,75),"original frontier native: "+q.stdout[-1200:].decode(errors="replace"))
   nr=json.loads(raw.read_bytes());rr=c.parse_result(result,nb,len(rows),len(labels),first)
   need(nr["binding"]==nb and nr["status"]==("completed" if q.returncode==0 else "budget-checkpoint") and nr["completeWholeRows"]==rr["next"] and nr["rank"]==rr["rank"] and nr["independentTinyProducts"]==25 and nr["exhaustiveBitplaneChecks"]>0,"all actual native arithmetic and complete source gates")
   ns.update(result=identity(result),checkpoint=identity(cpfile),receipt=identity(raw),log=identity(nd/"last-native.log"),lastExitCode=q.returncode);flush()
   if q.returncode==75:raise Budget("complete original-row prefix saved")
  need(rr["next"]==1386,"all original source rows completed")
  oldrank=sum(k<1106 for k in rr["independentOriginalRows"]);prefixrank=sum(k<first for k in rr["independentOriginalRows"])
  need(oldrank==1106,"complete original G8 rank independently reproduced")
  kept=[labels[k][0] for k in rr["independentOriginalRows"] if k>=first];available=set("paid-%03d"%sid for sid in paid_ids)|set(meankeys)|set(kept);expressions=[];deleted=0
  for k in range(first,len(labels)):
   tick();key=labels[k][0];name="verified-expression-%02d"%(k-first)
   if name in state["phases"]:
    z=read_phase(name);need(z["frontierKey"]==key and z["allTenCoordinatesVerified"] and z["allOriginal18ProductVerified"],"same complete frontier expression");expressions.append(z);deleted+=int(z["deleted"]);continue
   if k in rr["relations"]:
    coeff={}
    for j,v in enumerate(rr["relations"][k]):
     if not v or j==k:continue
     kk,e=labels[j];need(kk in available,"only actual old or retained new sources");coeff[kk]=coeff.get(kk,m.ZERO)-int(v)*c.mon(m,e)
    coeff={key0:v for key0,v in coeff.items() if v!=0};deleted+=1
   else:need(key in kept,"every new source classified");coeff={key:m.ONE}
   vv=[sum((co*vec[kk][axis] for kk,co in coeff.items()),m.ZERO) for axis in range(10)]
   need(vv==vec[key],"all ten complete parameter coordinates of every frontier relation")
   ss=[sum((co*src[kk][j] for kk,co in coeff.items()),m.ZERO) for j in range(18)]
   need(m.dot(A,ss)==m.dot(m.MON,vec[key]),"all original18 polynomial products of every frontier expression")
   z={"frontierKey":key,"deleted":k in rr["relations"],"coefficients":[[kk,m.pack(co)] for kk,co in sorted(coeff.items())],"allTenCoordinatesVerified":True,"allOriginal18ProductVerified":True};phase(name,z);expressions.append(z)
  need(len(expressions)==100 and len(kept)+deleted==100 and rr["rank"]==prefixrank+len(kept),"all100 new original images classified")
  cert={"prime":P,"coefficientRoot":100,"parentBinding":MODEL_BINDING,"compressionBinding":COMPRESS_BINDING,"meanFrontierBinding":MEAN_BINDING,"all100CommutatorImages":newkeys,"keptNewSourceKeys":kept,
   "all100Expressions":expressions,"allOutputRows":17674,"allInputColumns":1386,"completeOldColumns":1106,"allYMeanColumns":180,"previousColumns":1286,"oldRank":oldrank,"prefixRank":prefixrank,"actualRank":rr["rank"],"allOriginalSourceRelationsVerified":True,
   "originalFiftyPlusAllThirtyPlusAllHundredEqualsSameWithRetained":True,"noStableClosureClaim":True,"noUnitOrCharacteristicZeroClaim":True,"native":ns}
  d=phase("complete-original-weight8-frontier",cert);rec["status"]="completed";rec["parameters"].update(outcome="complete-source-certified-weight8-frontier",oldRank=oldrank,prefixRank=prefixrank,actualRank=rr["rank"],keptNewCount=len(kept),deletedNewCount=deleted,all100CompleteParameterRelationsVerified=True,all100Original18RelationProductsVerified=True,certificate=d);code=0;return code
 except Budget as e:rec["status"]="budget-checkpoint";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};code=75;return code
 except BaseException as e:rec["status"]="failed";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};code=1;return code
 finally:
  signal.setitimer(signal.ITIMER_REAL,0);flush();rec["elapsedSeconds"]=time.monotonic()-started;rec["peakRssKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss;rec["childPeakRssKiB"]=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
  rec["parameters"]["manifest"]=identity(mp);rec["parameters"]["completePhases"]=state["phases"];rec["parameters"]["nativeWholePrefix"]=state["native"]
  save_json(a.out/"complete-weight8-frontier-receipt.json",rec);print(canon(rec).decode(),flush=True)
if __name__=="__main__":sys.exit(main())
