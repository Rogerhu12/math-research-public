#!/usr/bin/env python3
"""Literal b*delta and y_i*b*delta in completed original weight7/8 row states.

Author: Astra-ISP-789f / literature_audit, with /root. AI-assisted GPT-6 Astra Pro.
No parent matrix is re-eliminated or mutated. Only full original products can
yield a field delta source; nonzero remainders concern the specified spaces.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,itertools,json,os,resource,signal,struct,subprocess,sys,time
from pathlib import Path
sys.set_int_max_str_digits(0)
FORMAT="r150-original-rank-four-bounded-rhs127-v1"
P=127;WEIGHTS=[0]+[2]*5+[4]*4
MODEL_SHA="4a7c1d93e65079912c66ad3370ba7cf59c3c5ef7d385c7cf69ba3cde76dac8e4"
COMPRESS_SHA="b1d3dbedd597a8019bab2dca6ff59bfa915aaa457a8ac0c14833266f449a1ee9"
RANK_SHA="c5c36af57f8d75d2aac7d42b4048be2c8f382fdbe9ed4a0ebefdf85f0c93bd9f"
HEADER_SHA="03272796bb20c883291d27c9a0b796197f8295ccd9b16552c13894657dc8afd3"
NATIVE_SHA="9707a53c28f7c3082fec631675aea3974b2f637cdd5c5333bfeee46dac5d05a1"
CHART_SHA="ee9bdabfdd325150b622e77a91d20eb814c642c8cb66bbf4734106466af630e3"
MODEL_BINDING="7c59f3f6e05c836aa97eef0ad358eaae8f8174c8225b1842ed5c4f313000f3d4"
MODEL_MANIFEST={"bytes":30466,"sha256":"9120695ac2e42f8300fdea4aa814183bc033d83062810a8854998a25199795e2"}
COMPRESS_BINDING="baaa8ec3f9459c0d2f88ebb452c941ce241f2727d5becab1ca78511a55a589ca"
COMPRESS_MATH={"bytes":620742,"sha256":"a1d73ea1ce5809c87bdc34724c1eb4407d6a5c0ae78fbf16aa3650563aa089dd"}
PARENTS={
 7:{"format":"r150-original-mean-first-source-frontier127-v1","stem":"original-mean-frontier","sourceSHA256":"810904a2c797b08493ed377c069abd75018e0a0df8035cb700baad80616bea1e","binding":"9502b11bf94390e8833cdc236a1ad85746d9823f9f4fe1e62de60f1932434bfd","nativeBinding":"b144b9f481c845fb095968d2d89d071522fba0d4260dfed941ca57881ac49345","rows":7754,"columns":312,"first":282,"rank":312,
 "dictionary":{"bytes":245111,"sha256":"3463ec53d58d0d49d5f3298b3364d411e2a1a98beca49f63561df5aaf73c45da"},"input":{"bytes":2419340,"sha256":"23430d41a72391d2f7cd36efc2e7517cdd05187601ec654fec51d62c9224294d"},"checkpoint":{"bytes":2212820,"sha256":"c5553497e614338fc5a811ad5bce78571d1d835e32f269435f756e822e2e35df"},"result":{"bytes":2612,"sha256":"3996c60c05f2fadb339c7d4f9d411c0e75fb82ed103d875077fa93f207d7d020"}},
 8:{"format":"r150-original-complete-weight8-source-frontier127-v1","stem":"complete-weight8-frontier","sourceSHA256":"bf5fa8e6ea1a70ed9441cf28918c9bd46946661afd932c7888f713dc2eadc936","binding":"1fdb39f00f53e51f33cbecef6c25c503c43e85575ad79abbd189ade9fdc7d069","nativeBinding":"721ca4b226e01fe685efc7753fbf24aa335e82f7863b82118024b829c18b5d6d","rows":17674,"columns":1386,"first":1286,"rank":1312,
 "dictionary":{"bytes":586948,"sha256":"4164b25bfaa7504c12cb40d20fa3f9d22887d71b75bae943121808a4fc686ab0"},"input":{"bytes":24496256,"sha256":"b9c8085459685cdf728e9ba8cbc005daccfc80a0d8047ddccddb008e4002249a"},"checkpoint":{"bytes":22008128,"sha256":"e561e3652a0dd2583c8c6b2206c34f5e1c8b0ab4d77275a35b25f16db5ae581e"},"result":{"bytes":113472,"sha256":"c866eab92a0aa9a5c451b96135647a6391b9f6dc242b5ae9fa03aa9da54eb36d"}}
}
class Budget(Exception):pass
def need(v,s):
 if not v:raise ValueError(s)
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")
def sha(b):return hashlib.sha256(b).hexdigest()
def identity(p):
 p=Path(p);h=hashlib.sha256()
 with p.open("rb") as f:
  for b in iter(lambda:f.read(1048576),b""):h.update(b)
 return {"path":p.name,"bytes":p.stat().st_size,"sha256":h.hexdigest()}
def exact(p,d):
 z=identity(p);need(z["bytes"]==d["bytes"] and z["sha256"]==d["sha256"],"complete exact file "+p.name);return z
def atomic(p,b):
 p.parent.mkdir(parents=True,exist_ok=True);q=p.with_name(p.name+".tmp");q.write_bytes(b);os.replace(q,p)
def save_json(p,x):atomic(p,canon(x));return identity(p)
def module(p,h,name):
 need(identity(p)["sha256"]==h,"literal helper source "+p.name);s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def phase_read(folder,d,fmt,binding):
 p=folder/d["path"];exact(p,d);need(d["bytes"]<=16*1024*1024 and d["logicalBytes"]<=128*1024*1024,"bounded original polynomial phase")
 b=gzip.decompress(p.read_bytes());need(len(b)==d["logicalBytes"] and sha(b)==d["logicalSha256"],"whole original logical phase")
 z=json.loads(b);need(z["format"]==fmt+"-phase" and z["binding"]==binding,"same actual source phase binding");return z["data"]

def main():
 ap=argparse.ArgumentParser()
 for n in ("model-source","model-out","compression-source","compression-out","weight7-source","weight7-out","weight8-source","weight8-out","chart-source","rank-source","header","native-source","out"):ap.add_argument("--"+n,type=Path,required=True)
 ap.add_argument("--seconds",type=float,default=180);ap.add_argument("--memory-mib",type=int,default=2048);a=ap.parse_args()
 need(0<a.seconds<=600 and 768<=a.memory_mib<=4096,"bounded original RHS and source verification")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2);started=time.monotonic();deadline=started+a.seconds;a.out.mkdir(parents=True,exist_ok=True)
 own=identity(Path(__file__));semantic={"format":FORMAT,"source":own,"prime":127,"coefficientRoot":100,"chartIndex":14,"literalMeanRows":[2,3,4,5],
  "targets":{"7":["b*delta*e0"],"8":["y%d*b*delta*e0"%i for i in range(6)]},"completeParentStates":PARENTS,
  "modelSourceSHA256":MODEL_SHA,"compressionSourceSHA256":COMPRESS_SHA,"chartSourceSHA256":CHART_SHA,"rankSourceSHA256":RANK_SHA,"headerSHA256":HEADER_SHA,"readOnlyNativeSHA256":NATIVE_SHA,
  "positiveGate":"literal full scalar products; all ten module coordinates; original18; original17; exact Bell gluing","characteristicZeroClaimed":False}
 binding=sha(canon(semantic));mp=a.out/"rank-four-bounded-rhs-manifest.json";rp=a.out/"rank-four-bounded-rhs-receipt.json"
 state={"format":FORMAT+"-manifest","binding":binding,"semantic":semantic,"phases":{},"native":{}}
 if mp.exists():
  state=json.loads(mp.read_bytes());need(state["format"]==FORMAT+"-manifest" and state["binding"]==binding and state["semantic"]==semantic,"same actual RHS continuation")
 rec={"format":FORMAT,"binding":binding,"source":own,"status":"running","parameters":{"seconds":a.seconds,"memoryMiB":a.memory_mib,"characteristicZeroConclusion":False,"fullIdealNonmembershipClaimed":False,"newParentEliminationPerformed":False}}
 child=None;code=1
 def remaining():return deadline-time.monotonic()
 def tick():
  if remaining()<8:raise Budget("bounded original RHS/source phase")
 def alarm(*args):raise Budget("actual RHS source budget")
 def flush():save_json(mp,state)
 def event(name,**kw):
  rec["parameters"]["lastWholePhase"]=name;print(canon({"phase":name,"elapsedSeconds":time.monotonic()-started,**kw}).decode(),flush=True)
 def phase(name,data):
  b=canon({"format":FORMAT+"-phase","binding":binding,"data":data});p=a.out/(name+".json.gz");atomic(p,gzip.compress(b,compresslevel=1,mtime=0))
  d={**identity(p),"logicalBytes":len(b),"logicalSha256":sha(b)};state["phases"][name]=d;flush();return d
 def read_phase(name):return phase_read(a.out,state["phases"][name],FORMAT,binding)
 signal.signal(signal.SIGALRM,alarm);signal.setitimer(signal.ITIMER_REAL,a.seconds)
 try:
  m=module(a.model_source,MODEL_SHA,"rhs_original_model");c=module(a.compression_source,COMPRESS_SHA,"rhs_original_compression");ch=module(a.chart_source,CHART_SHA,"rhs_original_chart")
  for p,h in ((a.rank_source,RANK_SHA),(a.header,HEADER_SHA),(a.native_source,NATIVE_SHA)):need(identity(p)["sha256"]==h,"exact immutable native dependency")
  exact(a.model_out/"original-parameter-module-manifest.json",MODEL_MANIFEST)
  pm=json.loads((a.model_out/"original-parameter-module-manifest.json").read_bytes());pr=json.loads((a.model_out/"original-parameter-module-receipt.json").read_bytes())
  need(pm["binding"]==pr["binding"]==MODEL_BINDING and pr["status"]=="completed" and pr["source"]["sha256"]==MODEL_SHA and pr["parameters"]["all116OriginalSeedsVerified"],"complete original model parent")
  cm=json.loads((a.compression_out/"complete-parameter-seed-compression-manifest.json").read_bytes());cr=json.loads((a.compression_out/"complete-parameter-seed-compression-receipt.json").read_bytes());exact(a.compression_out/"complete-parameter-seed-compression-manifest.json",cr["parameters"]["manifest"])
  need(cm["binding"]==cr["binding"]==COMPRESS_BINDING and cr["status"]=="completed" and cr["source"]["sha256"]==COMPRESS_SHA,"complete source compression parent")
  cp=c.load_gz(a.compression_out/cm["phases"]["complete-original-compressed-parameter-seeds"]["path"],cm["phases"]["complete-original-compressed-parameter-seeds"],COMPRESS_BINDING)
  b=canon({k:cp[k] for k in ("parentBinding","prime","coefficientRoot","allOriginal116SeedExpansionColumns","retainedOriginalSeedIndices")})
  need(len(b)==COMPRESS_MATH["bytes"] and sha(b)==COMPRESS_MATH["sha256"],"same complete original compression mathematics")
  kept={}
  for w,n in ((6,20),(8,14)):
   q=cm["phases"]["complete-weight%d-seed-compression"%w];z=c.load_gz(a.compression_out/q["path"],q,COMPRESS_BINDING);kept[w]=z["keptOriginalTargetSeedIndices"]
   need(len(kept[w])==len(set(kept[w]))==n,"complete literal retained source labels")
  bd=pm["phases"]["complete-original-ten-parameter-action127"];base=m.load_gz(a.model_out/bd["path"],bd,MODEL_BINDING)
  od=pm["phases"]["complete-original-global-chart127"];oldchart=m.load_gz(a.model_out/od["path"],od,MODEL_BINDING)
  A=m.unpackvec(base["allOriginal18Generators"]);old=m.unpackvec(oldchart["originalComposedGradients"]);J=[m.unpackvec(r) for r in base["sourceCoordinateChange"]]
  need(len(A)==18 and len(old)==17 and len(J)==17 and all(len(r)==17 for r in J),"all original gradient coordinates")
  need(all(m.dot(row,old)==A[i] for i,row in enumerate(J)),"all17 original gradient transports")
  Y=list(m.CTX.gens()[:6]);W=list(m.CTX.gens()[6:12]);bell=sum((Y[i]*W[i] for i in range(6)),m.ZERO)
  need(A[17]==bell-1==m.unpack(oldchart["originalBellMinusOne"]),"literal original Bell polynomial")
  source_cache={}
  def original_seed(sid):
   z=m.load_gz(a.model_out/pm["seeds"][sid]["path"],pm["seeds"][sid],MODEL_BINDING)
   need(z["seedIndex"]==sid and z["fullOriginal18ProductVerified"] and z["allTenParameterCoordinatesRetained"],"literal complete paid source")
   v=m.unpackvec(z["vector"]);s=m.unpackvec(z["original18Source"])
   need(len(v)==10 and len(s)==18 and s[17]==0 and m.dot(m.MON,v)==m.dot(A,s),"complete pure-gradient original seed product")
   return v,s
  means=[]
  for sid in range(100,106):
   tick();v,s=original_seed(sid);means.append(v);source_cache["paid-%03d"%sid]=(v,s)
  T=base["allFourOriginalMeanMatrices"]
  need(len(T)==4 and all(len(q)==6 and all(len(r)==6 for r in q) for q in T),"all four original mean matrices")
  for k in range(4):
   for i in range(6):need(means[i][6+k]==sum((int(T[k][i][j])*Y[j] for j in range(6)),m.ZERO),"all24 original mean quadratic coordinates")
  piv=[[means[j][6+i] for j in (2,3,4,5)] for i in range(4)];delta=ch.det(piv,m);adj=ch.adj(piv,m);diag=[[delta if i==j else m.ZERO for j in range(4)] for i in range(4)]
  need(ch.same(ch.mm(piv,adj,m),diag) and ch.same(ch.mm(adj,piv,m),diag),"both literal original adjugate products")
  need(sha(canon(m.pack(delta)))=="eff3070880440dd84f3b8d6bcfac5fc71461537d55b9f3d2c323a4287cdde0f6" and delta!=0,"same actual delta14")
  parents={};inputs={"modelManifest":identity(a.model_out/"original-parameter-module-manifest.json"),"modelReceipt":identity(a.model_out/"original-parameter-module-receipt.json"),"compressionManifest":identity(a.compression_out/"complete-parameter-seed-compression-manifest.json"),"compressionReceipt":identity(a.compression_out/"complete-parameter-seed-compression-receipt.json"),"modelPhase":bd,"oldChartPhase":od}
  for degree in (7,8):
   tick();spec=PARENTS[degree];folder=getattr(a,"weight%d_out"%degree);src=getattr(a,"weight%d_source"%degree)
   need(identity(src)["sha256"]==spec["sourceSHA256"],"exact completed parent source")
   pm0=json.loads((folder/(spec["stem"]+"-manifest.json")).read_bytes());pr0=json.loads((folder/(spec["stem"]+"-receipt.json")).read_bytes())
   exact(folder/(spec["stem"]+"-manifest.json"),pr0["parameters"]["manifest"])
   need(pm0["format"]==spec["format"]+"-manifest" and pm0["binding"]==pr0["binding"]==spec["binding"] and sha(canon(pm0["semantic"]))==spec["binding"],"same complete parent semantic binding")
   need(pr0["status"]=="completed" and pr0["source"]["sha256"]==spec["sourceSHA256"] and pr0["parameters"]["actualRank"]==spec["rank"],"actual full parent status and rank")
   gates=("all30Original18ProductsVerified","all30Original18RelationProductsVerified") if degree==7 else ("all100Original18ProductsVerified","all100Original18RelationProductsVerified")
   need(all(pr0["parameters"][k] for k in gates),"all parent original source products")
   ns=pm0["native"];nd=folder/("complete-weight%d"%degree)
   need(ns["binding"]==spec["nativeBinding"] and ns["lastExitCode"]==0,"complete original native identity")
   for key in ("dictionary","input","checkpoint","result"):
    need(ns[key]["bytes"]==spec[key]["bytes"] and ns[key]["sha256"]==spec[key]["sha256"],"paid complete native descriptor "+key);exact(nd/ns[key]["path"],spec[key])
   exact(nd/ns["receipt"]["path"],ns["receipt"]);nr=json.loads((nd/ns["receipt"]["path"]).read_bytes())
   need(nr["status"]=="completed" and nr["binding"]==ns["binding"] and nr["completeWholeRows"]==spec["columns"] and nr["rank"]==spec["rank"] and nr["independentTinyProducts"]==25 and nr["exhaustiveBitplaneChecks"]>0,"actual complete native result")
   rr=c.parse_result(nd/ns["result"]["path"],ns["binding"],spec["rows"],spec["columns"],spec["first"])
   need(rr["next"]==spec["columns"] and rr["rank"]==spec["rank"],"all original source rows complete")
   dic=json.loads((nd/ns["dictionary"]["path"]).read_bytes());need(sha(canon(dic))==spec["dictionary"]["sha256"],"entire canonical original dictionary")
   rows=[(axis,e) for axis,w in enumerate(WEIGHTS) for e in c.weighted_monomials(m,degree-w)]
   need(dic["outputs"]==[[axis,list(e)] for axis,e in rows],"every original homogeneous output coordinate")
   if degree==7:labels=[("paid-%03d"%sid,e) for sid in range(100,106) for e in c.weighted_monomials(m,2)]+[("paid-%03d"%sid,e) for sid in kept[6] for e in c.weighted_monomials(m,1)]
   else:labels=[("paid-%03d"%sid,e) for sid in range(100,106) for e in c.weighted_monomials(m,3)]+[("paid-%03d"%sid,e) for sid in kept[6] for e in c.weighted_monomials(m,2)]+[("paid-%03d"%sid,(0,)*12) for sid in kept[8]]
   labels.extend(("frontier-i%d-mean%d"%(i,j),e) for i in range(5) for j in range(6) for e in ([(0,)*12] if degree==7 else c.weighted_monomials(m,1)))
   if degree==8:labels.extend(("weight8-i%d-comm%03d"%(i,sid),(0,)*12) for i in range(5) for sid in kept[6])
   need(len(rows)==spec["rows"] and len(labels)==spec["columns"] and dic["inputs"]==[[key,list(e)] for key,e in labels] and dic["firstNewOriginalTarget"]==spec["first"],"complete original input labels, no changed order")
   parents[degree]={"manifest":pm0,"folder":folder,"directory":nd,"native":ns,"rows":rows,"labels":labels}
   inputs[str(degree)]={"source":identity(src),"manifest":identity(folder/(spec["stem"]+"-manifest.json")),"receipt":identity(folder/(spec["stem"]+"-receipt.json")),"native":ns}
  if "inputs" in state:need(state["inputs"]==inputs,"same actual read-only parent files")
  else:state["inputs"]=inputs;flush()
  rec["parameters"].update(all17OriginalGradientTransportsVerified=True,all24OriginalMeanCoordinatesVerified=True,bothOriginalAdjugateProductsVerified=True,allCompletedParentStatesVerified=True,originalInputs=inputs)
  event("all-complete-original-parents",weight7Rank=312,weight8Rank=1312)
  build=a.out/"build";build.mkdir(exist_ok=True)
  for src in (a.native_source,a.rank_source,a.header):atomic(build/src.name,src.read_bytes())
  exe=build/"read-only-complete-original-rhs127"
  if "nativeBinary" in state:exact(exe,state["nativeBinary"])
  else:
   tick();q=subprocess.run(["g++","-std=c++17","-O3",str(build/a.native_source.name),"-o",str(exe)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=min(60,remaining()-8));atomic(build/"compile.log",q.stdout)
   need(q.returncode==0,"read-only native compilation: "+q.stdout[-1200:].decode(errors="replace"));state["nativeBinary"]=identity(exe);state["compileLog"]=identity(build/"compile.log");flush()
  targets={7:[bell*delta],8:[Y[i]*bell*delta for i in range(6)]};results={}
  for degree in (7,8):
   tick();par=parents[degree];spec=PARENTS[degree];nd=a.out/("weight%d-rhs"%degree);nd.mkdir(exist_ok=True);lookup={r:i for i,r in enumerate(par["rows"])}
   tb=[]
   for target in targets[degree]:
    row=bytearray(spec["rows"])
    for e,v in target.to_dict().items():
     need(not any(e[12:]),"literal target has all twelve parameter variables only");j=lookup.get((0,tuple(e[:12])))
     need(j is not None and not row[j] and 0<int(v)<127,"entire original target in its exact output dictionary");row[j]=int(v)
    tb.append(bytes(row))
   header=b"R15RHI01"+struct.pack("<6I",1,spec["rows"],spec["columns"],len(tb),127,spec["rank"])+spec["nativeBinding"].encode()+binding.encode()
   rhs=nd/"literal-original-rhs-input.bin";rawin=header+b"".join(tb);need(len(header)==160,"independent RHS protocol header")
   nstate=state["native"].setdefault(str(degree),{})
   if "input" in nstate:exact(rhs,nstate["input"]);need(rhs.read_bytes()==rawin,"same exact original target bytes")
   else:atomic(rhs,rawin);nstate["input"]=identity(rhs);flush()
   out=nd/"complete-original-rhs-result.bin";nrp=nd/"complete-original-rhs-native-receipt.json"
   if "result" in nstate:exact(out,nstate["result"]);exact(nrp,nstate["receipt"])
   else:
    tick();need(remaining()>20,"native RHS reserve");seconds=min(180,remaining()-12);signal.setitimer(signal.ITIMER_REAL,0)
    try:q=subprocess.run([str(exe),str(par["directory"]/par["native"]["input"]["path"]),str(par["directory"]/par["native"]["checkpoint"]["path"]),str(rhs),str(nd),str(seconds)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=seconds+8)
    finally:
     if remaining()>0:signal.setitimer(signal.ITIMER_REAL,remaining())
    atomic(nd/"native.log",q.stdout)
    if q.returncode==75:raise Budget("read-only native did not finish; no partial original row state used")
    need(q.returncode==0,"actual read-only RHS native: "+q.stdout[-1200:].decode(errors="replace"));nstate.update(result=identity(out),receipt=identity(nrp),log=identity(nd/"native.log"));flush()
   nr=json.loads(nrp.read_bytes());need(nr["binding"]==binding and nr["parentBinding"]==spec["nativeBinding"] and nr["status"]=="completed" and nr["actualParentRank"]==spec["rank"] and nr["allOriginalScalarProducts"]==spec["rows"]*len(tb) and nr["independentTinyProducts"]==25 and nr["exhaustiveBitplaneChecks"]>0 and not nr["parentMutated"] and not nr["newGaussianEliminationPerformed"],"all actual original source/RHS products")
   rb=out.read_bytes();need(rb[:8]==b"R15RHO01" and struct.unpack_from("<6I",rb,8)==(1,spec["rows"],spec["columns"],len(tb),127,spec["rank"]),"whole independent RHS result protocol")
   need(rb[32:96].decode()==spec["nativeBinding"] and rb[96:160].decode()==binding,"same parent and child result bindings")
   pos=160;res=[];co=[];nn=[]
   for k in range(len(tb)):
    nz=struct.unpack_from("<I",rb,pos)[0];pos+=4;r=rb[pos:pos+spec["rows"]];pos+=spec["rows"];q=list(rb[pos:pos+spec["columns"]]);pos+=spec["columns"]
    need(len(r)==spec["rows"] and len(q)==spec["columns"] and max(r)<127 and max(q)<127 and sum(v!=0 for v in r)==nz,"complete canonical residual and all original source coefficients")
    need(all(r[j]==0 for j in c.parse_result(par["directory"]/par["native"]["result"]["path"],spec["nativeBinding"],spec["rows"],spec["columns"],spec["first"])["pivotOutputRows"]),"all actual original pivot residuals zero")
    res.append(list(r));co.append(q);nn.append(nz)
   need(pos==len(rb) and nn==nr["residualNonzeroCounts"],"complete RHS output exact EOF and counts")
   for key in ("input","checkpoint","result","dictionary"):exact(par["directory"]/par["native"][key]["path"],spec[key])
   results[degree]={"coefficients":co,"residuals":res,"nonzeroCounts":nn,"native":nr}
   phase("complete-weight%d-original-rhs"%degree,{"targets":m.packvec(targets[degree]),"allOriginalInputCoefficients":co,"allResidualOutputCoordinates":res,"nonzeroCounts":nn,"fullOriginalScalarProductsVerified":True,"parentUnchangedVerified":True,"native":nstate})
   event("complete-weight%d-original-rhs"%degree,rightHandSides=len(tb),zeroRemainders=sum(n==0 for n in nn),originalProducts=nr["allOriginalScalarProducts"])
  def get_source(key):
   tick()
   if key in source_cache:return source_cache[key]
   if key.startswith("paid-"):v,s=original_seed(int(key[5:]))
   else:
    degree=7 if key.startswith("frontier-") else 8;par=parents[degree];spec=PARENTS[degree]
    need(key in par["manifest"]["phases"],"literal original frontier label")
    z=phase_read(par["folder"],par["manifest"]["phases"][key],spec["format"],spec["binding"])
    need(z["fullOriginal18ProductVerified"],"paid whole frontier source gate");v=m.unpackvec(z["vector"]);s=m.unpackvec(z["original18Source"])
    need(len(v)==10 and len(s)==18 and s[17]==0 and m.dot(m.MON,v)==m.dot(A,s),"complete pure-gradient original frontier product")
   return v,s
  positive=[]
  for degree in (7,8):
   for k,nz in enumerate(results[degree]["nonzeroCounts"]):
    if nz:continue
    tick();name="complete-weight%d-target%d-original-source"%(degree,k)
    if name in state["phases"]:
     z=read_phase(name);need(z["degree"]==degree and z["targetIndex"]==k and z["allTenCoordinatesVerified"] and z["allOriginal18ProductVerified"] and z["allOriginal17ProductVerified"],"same full positive original source");sig=m.unpackvec(z["original18Source"])
    else:
     grouped={}
     for q,(key,e) in zip(results[degree]["coefficients"][k],parents[degree]["labels"]):
      if q:grouped[key]=grouped.get(key,m.ZERO)+q*c.mon(m,e)
     total=[m.ZERO for _ in range(10)];sig=[m.ZERO for _ in range(18)]
     for key,pol in sorted(grouped.items()):
      tick();v,s=get_source(key)
      for j in range(10):total[j]+=pol*v[j]
      for j in range(18):sig[j]+=pol*s[j]
     need(total==[targets[degree][k]]+[m.ZERO]*9,"all ten literal original target coordinates")
     need(sig[17]==0 and m.dot(A,sig)==targets[degree][k],"complete original18 target product, no Bell source introduced")
     osig=[sum((sig[j]*J[j][i] for j in range(17)),m.ZERO) for i in range(17)]
     need(m.dot(old,osig)==targets[degree][k],"all original17 physical gradient target products")
     phase(name,{"degree":degree,"targetIndex":k,"allOriginalInputCoefficients":results[degree]["coefficients"][k],"original18Source":m.packvec(sig),"original17Source":m.packvec(osig),"allTenCoordinatesVerified":True,"allOriginal18ProductVerified":True,"allOriginal17ProductVerified":True})
    need(len(sig)==18 and sig[17]==0 and m.dot(A,sig)==targets[degree][k],"complete restored original target source")
    positive.append((degree,k,sig));event(name)
  sources={(d,k):s for d,k,s in positive};ways=[]
  if (7,0) in sources:
   sig=list(sources[(7,0)]);sig[17]-=delta;ways.append(("weight7-b-delta",sig))
  if all((8,i) in sources for i in range(6)):
   sig=[sum((W[i]*sources[(8,i)][j] for i in range(6)),m.ZERO) for j in range(18)];sig[17]-=(bell+1)*delta;ways.append(("weight8-six-y-b-delta",sig))
  certificates=[]
  for label,sig in ways:
   tick();need(m.dot(A,sig)==delta,"literal complete Bell gluing gives delta")
   osig=[sum((sig[j]*J[j][i] for j in range(17)),m.ZERO) for i in range(17)]
   need(m.dot(old,osig)+A[17]*sig[17]==delta,"complete original17 plus Bell product gives delta")
   d=phase("complete-original-delta-source-"+label,{"prime":127,"coefficientRoot":100,"chartIndex":14,"delta":m.pack(delta),"sourceRoute":label,"original18Source":m.packvec(sig),"original17Source":m.packvec(osig),"allOriginal18ProductVerified":True,"allOriginal17PlusBellProductVerified":True,"characteristicZeroLiftVerified":False});certificates.append({"route":label,"phase":d})
  rec["status"]="completed-positive" if ways else "completed-diagnostic"
  rec["parameters"].update(outcome="literal-original-delta14-field-source" if ways else "specified-complete-source-spaces-only",weight7ResidualNonzeroCounts=results[7]["nonzeroCounts"],weight8ResidualNonzeroCounts=results[8]["nonzeroCounts"],all113798OriginalScalarProductsVerified=True,allParentFilesUnchangedVerified=True,positiveIndividualTargetCount=len(positive),deltaSourceCertificates=certificates,allCompletedNativeResults=state["native"]);code=0;return code
 except Budget as e:rec["status"]="budget-checkpoint";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};code=75;return code
 except BaseException as e:rec["status"]="failed";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};code=1;return code
 finally:
  signal.setitimer(signal.ITIMER_REAL,0);flush();rec["elapsedSeconds"]=time.monotonic()-started;rec["parameters"]["peakRssKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss;rec["parameters"]["childPeakRssKiB"]=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss;rec["parameters"]["manifest"]=identity(mp);save_json(rp,rec);print(canon(rec).decode(),flush=True)
if __name__=="__main__":raise SystemExit(main())
