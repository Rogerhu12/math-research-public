#!/usr/bin/env python3
"""Complete original parameter-seed compression, preserving the whole F127 module.
Author: Astra-ISP-789f / normal_annihilator, with /root.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.
All output monomials and original seed labels are retained. Each omitted seed
gets a full parameter combination and an original18 polynomial product.
This is only a finite-field module compression, not a characteristic-zero rank
claim, stable-closure certificate, or unit-ideal result.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,os,resource,signal,struct,subprocess,sys,time
from pathlib import Path
sys.set_int_max_str_digits(0)
FORMAT="r150-original-complete-parameter-seed-compression127-v1"
MODEL_SHA="4a7c1d93e65079912c66ad3370ba7cf59c3c5ef7d385c7cf69ba3cde76dac8e4"
NATIVE_SHA="c5c36af57f8d75d2aac7d42b4048be2c8f382fdbe9ed4a0ebefdf85f0c93bd9f"
HEADER_SHA="03272796bb20c883291d27c9a0b796197f8295ccd9b16552c13894657dc8afd3"
PARENT_BINDING="7c59f3f6e05c836aa97eef0ad358eaae8f8174c8225b1842ed5c4f313000f3d4"
PARENT_MANIFEST={"bytes":30466,"sha256":"9120695ac2e42f8300fdea4aa814183bc033d83062810a8854998a25199795e2"}
PARENT_RECEIPT={"bytes":30925,"sha256":"3615210e27511904dbadc086d8e00438442f33d2538b7f33fa57fa5de9fb18a3"}
P=127;MWEIGHT=[0]+[2]*5+[4]*4
def need(b,s):
 if not b:raise ValueError(s)
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")
def sha(b):return hashlib.sha256(b).hexdigest()
def identity(p):
 h=hashlib.sha256()
 with p.open("rb") as f:
  for z in iter(lambda:f.read(1048576),b""):h.update(z)
 return {"path":p.name,"bytes":p.stat().st_size,"sha256":h.hexdigest()}
def exact_file(p,d):
 x=identity(p);need(x["bytes"]==d["bytes"] and x["sha256"]==d["sha256"],"whole exact file "+p.name);return x
def atomic(p,b):
 p.parent.mkdir(parents=True,exist_ok=True);t=p.with_name(p.name+".tmp");t.write_bytes(b);os.replace(t,p)
def save_json(p,x):atomic(p,canon(x));return identity(p)
def save_gz(p,x,binding):
 b=canon({"format":FORMAT+"-phase","binding":binding,"data":x});z=gzip.compress(b,compresslevel=1,mtime=0);atomic(p,z)
 return {"path":p.name,"bytes":len(z),"sha256":sha(z),"logicalBytes":len(b),"logicalSha256":sha(b)}
def load_gz(p,d,binding):
 exact_file(p,d);b=gzip.decompress(p.read_bytes());need(len(b)==d["logicalBytes"] and sha(b)==d["logicalSha256"],"complete logical compression phase")
 x=json.loads(b);need(x["format"]==FORMAT+"-phase" and x["binding"]==binding,"same actual compression phase");return x["data"]
def weighted_monomials(m,d):
 out=[]
 for j in range(d//2+1):
  for a in m.mons(6,d-2*j):
   for b in m.mons(6,j):out.append(tuple(a)+tuple(b))
 return out
def output_dictionary(m,d):
 rows=[]
 for a,w in enumerate(MWEIGHT):
  for e in weighted_monomials(m,d-w):rows.append((a,e))
 need(len(rows)==(3188 if d==6 else 17674),"complete weighted original output dictionary")
 need(len(set(rows))==len(rows),"all original output rows unique");return rows
def mon(m,e):return m.CTX.from_dict({tuple(e)+(0,)*5:1})
def vectors_equal(a,b):return len(a)==len(b) and all(x==y for x,y in zip(a,b))
def parse_result(path,binding,no,ni,first):
 b=path.read_bytes();need(b[:8]==b"R15PCR01","exact complete-row output magic")
 v=struct.unpack_from("<7I",b,8);need(v[:4]==(1,no,ni,first),"same full original output and input dictionaries")
 nxt,rank,nd=v[4:];need(nxt<=ni and rank<=nxt and nd<=ni-first,"complete result bounds")
 need(b[36:100].decode("ascii")==binding,"same native semantic binding")
 reductions,units=struct.unpack_from("<2Q",b,100);pos=116
 piv=[];original=[]
 for _ in range(rank):
  p,s=struct.unpack_from("<2I",b,pos);pos+=8;need(p<no and s<nxt,"literal original pivot labels");piv.append(p);original.append(s)
 need(len(set(piv))==rank and len(set(original))==rank and units==rank,"unique whole original units")
 dep={}
 for _ in range(nd):
  k=struct.unpack_from("<I",b,pos)[0];pos+=4;q=list(b[pos:pos+ni]);pos+=ni
  need(k>=first and k<nxt and k not in dep and len(q)==ni and max(q)<P,"whole target source relation")
  need(q[k]==1 and not any(q[k+1:]),"unit target coefficient and preceding-source support");dep[k]=q
 need(pos==len(b),"no partial or extra complete native output")
 indep=set(original)
 for k in range(first,nxt):
  need((k in indep)!=(k in dep),"every completed target classified")
  if k in dep:
   need(all(not dep[k][j] or j==k or j in indep for j in range(ni)),"all dependent source recipes use actual retained input rows")
 return {"next":nxt,"rank":rank,"independentOriginalRows":original,"pivotOutputRows":piv,"relations":dep,"pivotCancellations":reductions}
def main():
 ap=argparse.ArgumentParser()
 for n in ("model-source","model-out","native-source","header","out"):ap.add_argument("--"+n,type=Path,required=True)
 ap.add_argument("--seconds",type=float,default=180);ap.add_argument("--memory-mib",type=int,default=768)
 ap.add_argument("--through",choices=("six","final"),default="final");a=ap.parse_args()
 need(0<a.seconds<=900 and 512<=a.memory_mib<=2048,"bounded complete original compression")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
 started=time.monotonic();deadline=started+a.seconds;a.out.mkdir(parents=True,exist_ok=True)
 own=identity(Path(__file__))
 semantic={"format":FORMAT,"source":own,"modelSourceSHA256":MODEL_SHA,"nativeSourceSHA256":NATIVE_SHA,"headerSHA256":HEADER_SHA,
  "parentBinding":PARENT_BINDING,"parentManifest":PARENT_MANIFEST,"paidParentReceiptReference":PARENT_RECEIPT,
  "prime":P,"coefficientRoot":100,"originalModuleWeights":MWEIGHT,"completeOutputDimensions":[3188,17674],
  "allOriginalMeanMultipliers":["weight1","weight3"],"allOriginalSelectedWeight6Multipliers":"weight2"}
 binding=sha(canon(semantic));mp=a.out/"complete-parameter-seed-compression-manifest.json"
 state={"format":FORMAT+"-manifest","binding":binding,"semantic":semantic,"phases":{},"native":{}}
 if mp.exists():
  state=json.loads(mp.read_bytes());need(state["format"]==FORMAT+"-manifest" and state["binding"]==binding and state["semantic"]==semantic,"same complete original compression continuation")
 rec={"format":FORMAT,"binding":binding,"source":own,"status":"running","parameters":{"seconds":a.seconds,"memoryMiB":a.memory_mib,"through":a.through,
  "onlyFiniteFieldModuleEqualityClaimed":True,"characteristicZeroCompressionClaimed":False,"stableClosureClaimed":False}}
 def flush():save_json(mp,state)
 def remaining():return max(0.0,deadline-time.monotonic())
 def budget(sig=None,frame=None):raise TimeoutError("whole original seed-compression budget")
 signal.signal(signal.SIGALRM,budget);signal.setitimer(signal.ITIMER_REAL,a.seconds);code=1
 def event(name,**kw):
  z={"phase":name,"elapsedSeconds":time.monotonic()-started,"peakRssKiB":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss};z.update(kw)
  rec["parameters"]["lastWholePhase"]=name;print(json.dumps(z,separators=(",",":")),flush=True)
 try:
  for p,w in ((a.model_source,MODEL_SHA),(a.native_source,NATIVE_SHA),(a.header,HEADER_SHA)):need(identity(p)["sha256"]==w,"exact executable source "+p.name)
  exact_file(a.model_out/"original-parameter-module-manifest.json",PARENT_MANIFEST)
  actualParentReceipt=identity(a.model_out/"original-parameter-module-receipt.json")
  parent=json.loads((a.model_out/"original-parameter-module-manifest.json").read_bytes())
  paid=json.loads((a.model_out/"original-parameter-module-receipt.json").read_bytes())
  need(parent["binding"]==PARENT_BINDING and paid["binding"]==PARENT_BINDING and paid["status"]=="completed" and
       paid["source"]["sha256"]==MODEL_SHA and paid["parameters"]["all116OriginalSeedsVerified"] and
       paid["parameters"]["manifest"]["sha256"]==PARENT_MANIFEST["sha256"] and
       paid["parameters"]["manifest"]["bytes"]==PARENT_MANIFEST["bytes"] and
       len(parent["seeds"])==116,"actual complete original116 parent")
  rec["parameters"]["actualParentReceipt"]=actualParentReceipt
  sp=importlib.util.spec_from_file_location("paid_original_ten_module",a.model_source);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
  base=m.load_gz(a.model_out/parent["phases"]["complete-original-ten-parameter-action127"]["path"],parent["phases"]["complete-original-ten-parameter-action127"],PARENT_BINDING)
  A=m.unpackvec(base["allOriginal18Generators"]);del base
  vectors=[];sources=[]
  for i,d in enumerate(parent["seeds"]):
   z=m.load_gz(a.model_out/d["path"],d,PARENT_BINDING)
   need(z["seedIndex"]==i and z["fullOriginal18ProductVerified"] and z["allTenParameterCoordinatesRetained"],"same entire original seed dictionary")
   v=m.unpackvec(z["vector"]);s=m.unpackvec(z["original18Source"])
   need(len(v)==10 and len(s)==18 and all(not any(e[12:]) for x in v for e in x.to_dict()),"all original parameter coordinates")
   vectors.append(v);sources.append(s)
  del z
  for i in range(0,100,10):need(all(x==0 for x in vectors[i]),"all ten original e0 commutator columns really zero")
  need(len(weighted_monomials(m,1))==6 and len(weighted_monomials(m,2))==27 and
       len(weighted_monomials(m,3))==92 and len(weighted_monomials(m,4))==273 and
       len(weighted_monomials(m,6))==1715,"whole original parameter monomial counts")
  event("all116-paid-original-seed-payloads")
  build=a.out/"build";build.mkdir(exist_ok=True)
  cpp=build/a.native_source.name;hdr=build/"2026-11-15-r150-original-f127-bitplane-789f.hpp";exe=build/"original-seed-compression-native"
  atomic(cpp,a.native_source.read_bytes());atomic(hdr,a.header.read_bytes())
  if "nativeBinary" in state:exact_file(exe,state["nativeBinary"])
  else:
   need(remaining()>10,"remaining actual compiler budget")
   q=subprocess.run(["g++","-std=c++17","-O3",str(cpp),"-o",str(exe)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=min(60,remaining()-5))
   atomic(build/"compile.log",q.stdout);need(q.returncode==0,"original native compilation: "+q.stdout[-1500:].decode(errors="replace"))
   state["nativeBinary"]=identity(exe);state["compileLog"]=identity(build/"compile.log");flush();event("native-compiled")
  def input_file(degree,labels,first,rows):
   name="weight%d"%degree;dir=a.out/name;dir.mkdir(exist_ok=True)
   dictionary={"degree":degree,"completeOutputs":[[j,list(e)] for j,e in rows],
               "completeOriginalInputs":[{"parentSeedIndex":s,"parameterMonomial":list(e)} for s,e in labels],"firstNewOriginalTarget":first}
   dh=sha(canon(dictionary));nb=sha(canon({"parentCompressionBinding":binding,"literalDictionarySHA256":dh,"degree":degree}))
   item=state["native"].setdefault(name,{"binding":nb,"dictionarySHA256":dh})
   need(item["binding"]==nb and item["dictionarySHA256"]==dh,"same complete original weighted dictionary")
   p=dir/"all-original-row-input.bin"
   if "input" in item:exact_file(p,item["input"]);return dir,nb,item,p
   lookup={r:i for i,r in enumerate(rows)};t=p.with_name(p.name+".tmp")
   with t.open("wb") as f:
    f.write(b"R15PCI01");f.write(struct.pack("<5I",1,len(rows),len(labels),first,P));f.write(nb.encode("ascii"))
    for seed,e in labels:
     row=bytearray(len(rows))
     for axis,poly in enumerate(vectors[seed]):
      for ee,c in poly.to_dict().items():
       need(not any(ee[12:]),"input still over all twelve parameters")
       new=tuple(int(ee[j])+e[j] for j in range(12));k=lookup.get((axis,new))
       need(k is not None and not row[k] and 0<int(c)<P,"every full original monomial belongs to the declared output dictionary")
       row[k]=int(c)
     f.write(row)
    f.flush()
   os.replace(t,p);item["input"]=identity(p);item["dictionary"]=save_json(dir/"complete-original-dictionaries.json",dictionary);flush()
   event(name+"-whole-input",outputRows=len(rows),originalColumns=len(labels));return dir,nb,item,p
  def native_result(degree,labels,first,rows):
   dir,nb,item,inp=input_file(degree,labels,first,rows)
   result=dir/"complete-row-result.bin";checkpoint=dir/"complete-row-state.bin";raw=dir/"parameter-seed-native-receipt.json"
   if "result" in item:
    exact_file(result,item["result"]);exact_file(checkpoint,item["checkpoint"]);exact_file(raw,item["receipt"])
    rr=parse_result(result,nb,len(rows),len(labels),first)
    if rr["next"]==len(labels):event("reused-weight%d-native-complete"%degree);return rr,item
   else:
    need(not checkpoint.exists() and not result.exists(),"unregistered native state is not silently adopted")
   left=remaining();need(left>18,"remaining complete native solve reserve")
   secs=min(900,left-15)
   signal.setitimer(signal.ITIMER_REAL,0)
   try:
    q=subprocess.run([str(exe),str(inp),str(dir),str(secs)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=secs+8)
   finally:
    if remaining()>0:signal.setitimer(signal.ITIMER_REAL,remaining())
   atomic(dir/"last-native.log",q.stdout)
   need(q.returncode in (0,75),"original native failure: "+q.stdout[-2000:].decode(errors="replace"))
   nr=json.loads(raw.read_bytes());need(nr["binding"]==nb and nr["status"]==("completed" if q.returncode==0 else "budget-checkpoint"),"actual native status and complete binding")
   need(nr["independentTinyProducts"]==25 and nr["exhaustiveBitplaneChecks"]>0,"actual independent original arithmetic tests")
   rr=parse_result(result,nb,len(rows),len(labels),first)
   need(rr["next"]==nr["completeWholeRows"] and rr["rank"]==nr["rank"],"whole native result agrees with receipt")
   item.update({"result":identity(result),"checkpoint":identity(checkpoint),"receipt":identity(raw),"log":identity(dir/"last-native.log"),"lastExitCode":q.returncode})
   flush();event("weight%d-native-whole-prefix"%degree,rank=rr["rank"],processed=rr["next"],total=len(labels))
   if q.returncode==75:raise TimeoutError("complete native rows saved; weighted phase not yet complete")
   return rr,item
  def phase(degree,kept6):
   name="complete-weight%d-seed-compression"%degree
   if name in state["phases"]:
    z=load_gz(a.out/state["phases"][name]["path"],state["phases"][name],binding)
    need(z["degree"]==degree and z["previousKeptWeight6"]==kept6 and z["allOriginalVectorRelationsVerified"] and z["allOriginal18SourceProductsVerified"],"same complete verified lower-source phase")
    event("reused-"+name);return z
   rows=output_dictionary(m,degree)
   lowdegree=1 if degree==6 else 3
   labels=[(seed,e) for seed in range(100,106) for e in weighted_monomials(m,lowdegree)]
   if degree==8:labels.extend((seed,e) for seed in kept6 for e in weighted_monomials(m,2))
   first=len(labels)
   targets=[10*pair+axis for pair in range(10) for axis in (range(1,6) if degree==6 else range(6,10))]
   labels.extend((seed,(0,)*12) for seed in targets)
   rr,item=native_result(degree,labels,first,rows)
   keep=[labels[k][0] for k in rr["independentOriginalRows"] if k>=first]
   need(keep==sorted(set(keep)),"complete selected original target order")
   available=set(range(100,106))|set(kept6)|set(keep)
   expressions=[];deleted=0
   for target in range(first,len(labels)):
    sid=labels[target][0]
    if target in rr["relations"]:
     coeff={}
     for k,c in enumerate(rr["relations"][target]):
      if not c or k==target:continue
      seed,e=labels[k];need(seed in available,"only real retained original generators")
      coeff[seed]=coeff.get(seed,m.ZERO)-int(c)*mon(m,e)
     coeff={i:x for i,x in coeff.items() if x!=0}
     v=[sum((c*vectors[i][j] for i,c in coeff.items()),m.ZERO) for j in range(10)]
     need(vectors_equal(v,vectors[sid]),"all complete weighted output coordinates for deleted original seed")
     source=[sum((c*sources[i][j] for i,c in coeff.items()),m.ZERO) for j in range(18)]
     need(m.dot(A,source)==m.dot(m.MON,vectors[sid]),"entire original18 polynomial product for each deleted seed")
     deleted+=1
    else:
     need(sid in keep,"every original target either kept or fully reconstructed");coeff={sid:m.ONE}
    expressions.append({"parentSeedIndex":sid,"coefficients":[[i,m.pack(c)] for i,c in sorted(coeff.items())]})
   z={"degree":degree,"previousKeptWeight6":kept6,"allOriginalOutputRows":len(rows),"allOriginalInputColumns":len(labels),
      "allPreviousLowerColumns":first,"actualRank":rr["rank"],"keptOriginalTargetSeedIndices":keep,
      "allOriginalTargetSeedIndices":targets,"allOriginalTargetExpressions":expressions,
      "deletedOriginalSeedCount":deleted,"allOriginalVectorRelationsVerified":True,
      "allOriginal18SourceProductsVerified":True,"native":item,"noCharacteristicZeroCompressionClaimed":True}
   d=save_gz(a.out/(name+".json.gz"),z,binding);state["phases"][name]=d;flush()
   event(name,kept=len(keep),deleted=deleted,rank=rr["rank"]);return z
  six=phase(6,[])
  rec["parameters"]["completeWeight6KeptCount"]=len(six["keptOriginalTargetSeedIndices"])
  if a.through=="final":
   eight=phase(8,six["keptOriginalTargetSeedIndices"])
   retained=list(range(100,106))+six["keptOriginalTargetSeedIndices"]+eight["keptOriginalTargetSeedIndices"]+list(range(106,116))
   need(len(retained)==len(set(retained)),"all compressed generators are literal distinct original seeds")
   reps={i:{i:m.ONE} for i in retained}
   for ph in (six,eight):
    for x in ph["allOriginalTargetExpressions"]:reps[x["parentSeedIndex"]]={i:m.unpack(v) for i,v in x["coefficients"]}
   for i in range(0,100,10):reps[i]={}
   need(set(reps)==set(range(116)),"all116 original seeds represented, no omissions")
   allcols=[]
   for sid in range(116):
    c=reps[sid];need(set(c)<=set(retained),"complete retained-original-seed support")
    v=[sum((z*vectors[k][j] for k,z in c.items()),m.ZERO) for j in range(10)]
    need(vectors_equal(v,vectors[sid]),"all1160 final parameter-module equality coordinates")
    allcols.append({"parentSeedIndex":sid,"retainedCoefficients":[[retained.index(k),m.pack(z)] for k,z in sorted(c.items())]})
   final={"parentBinding":PARENT_BINDING,"parentManifest":PARENT_MANIFEST,"prime":P,"coefficientRoot":100,
      "allOriginal116SeedExpansionColumns":allcols,"retainedOriginalSeedIndices":retained,
      "retainedOriginalSeedDescriptors":[parent["seeds"][i] for i in retained],
      "all1160FinalParameterCoordinatesVerified":True,"sameCompleteOriginalParameterSubmodule":True,
      "allDeletedOriginal18SourceProductsVerified":True,"retainedSourcesArePaidFullOriginal18Sources":True,
      "allTwelveParametersRetained":True,"noMomentParameterSpecialized":True,
      "stableClosureComputed":False,"characteristicZeroModuleEqualityClaimed":False,"unitIdealClaimed":False,
      "sourceExpansionRecipe":"sigma(original_seed_j) may be replaced by sum C_ij*sigma(retained_seed_i); the difference is an original syzygy.",
      "weight6":state["phases"]["complete-weight6-seed-compression"],"weight8":state["phases"]["complete-weight8-seed-compression"]}
   name="complete-original-compressed-parameter-seeds"
   if name not in state["phases"]:state["phases"][name]=save_gz(a.out/(name+".json.gz"),final,binding);flush()
   else:need(load_gz(a.out/state["phases"][name]["path"],state["phases"][name],binding)==final,"same final whole original module equality")
   rec["parameters"].update({"allOriginalSeedCount":116,"retainedOriginalSeedCount":len(retained),
    "weight6KeptOriginalCount":len(six["keptOriginalTargetSeedIndices"]),"weight8KeptOriginalCount":len(eight["keptOriginalTargetSeedIndices"]),
    "all1160ModuleCoordinatesVerified":True,"allDeletedOriginal18ProductsVerified":True,
    "sameCompleteOriginalFiniteFieldParameterSubmodule":True})
   event("complete-original-compression",retained=len(retained))
  rec["status"]="completed" if a.through=="final" else "completed-prefix";code=0
 except BaseException as e:
  rec["status"]="budget-checkpoint" if isinstance(e,(TimeoutError,subprocess.TimeoutExpired)) else "failed"
  rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)}
  code=75 if rec["status"]=="budget-checkpoint" else 1
 finally:
  signal.setitimer(signal.ITIMER_REAL,0);rec["elapsedSeconds"]=time.monotonic()-started
  rec["peakRssKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss;rec["childPeakRssKiB"]=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
  if mp.exists():rec["parameters"]["manifest"]=identity(mp)
  rec["parameters"]["completePhases"]=state["phases"];rec["parameters"]["nativeWholePhases"]=state["native"]
  save_json(a.out/"complete-parameter-seed-compression-receipt.json",rec)
  print(json.dumps(rec,sort_keys=True,separators=(",",":")),flush=True)
 return code
if __name__=="__main__":sys.exit(main())
