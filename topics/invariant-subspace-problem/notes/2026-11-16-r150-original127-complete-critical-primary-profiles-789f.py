#!/usr/bin/env python3
"""Complete critical primary profiles inside the paid original F127 torsion.
Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.
Read only the paid whole299 action. Compute every critical primary, all its
cyclic exponents, and a complete original-coordinate invariant basis.
This prepares generalized detectors; it makes no coefficient-torsion or Q claim.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,os,resource,signal,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
FORMAT="r150-original127-complete-critical-primary-profiles-v1"
HELPER="2026-11-16-r150-original127-nine-target-cyclic-module-789f.py"
HELPER_PIN=(20947,"d520b190ac84f1990ed8ee84d405cc34c31d09e140ad26b8442c099872d26ed3")
P=127
stop_requested=False
class Budget(Exception):pass
def need(ok,msg):
 if not ok:raise ValueError(msg)
def canonical(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")
def sha(p):
 h=hashlib.sha256()
 with Path(p).open("rb") as f:
  for b in iter(lambda:f.read(1048576),b""):h.update(b)
 return h.hexdigest()
def digest(b):return hashlib.sha256(b).hexdigest()
def atomic(p,x):
 t=p.with_name(p.name+".tmp");t.write_bytes(canonical(x)+b"\n");os.replace(t,p)
def record(p):return {"file":p.name,"bytes":p.stat().st_size,"sha256":sha(p),"temporaryOnly":True}
def verify(p,pin,what):
 need(p.is_file() and p.stat().st_size==pin[0] and sha(p)==pin[1],"exact paid bytes: "+what)
def stop(signum,frame):
 global stop_requested
 stop_requested=True
def main():
 ap=argparse.ArgumentParser()
 for key in ("whole-out","hstar","sources-root","out"):ap.add_argument("--"+key,type=Path,required=True)
 ap.add_argument("--seconds",type=float,default=60);ap.add_argument("--memory-mib",type=int,default=512)
 a=ap.parse_args();need(1<=a.seconds<=600 and 256<=a.memory_mib<=2048,"bounded primary consumer")
 a.out.mkdir(parents=True,exist_ok=True);started=time.monotonic();deadline=started+a.seconds
 rp=a.out/"original127-critical-primary-receipt.json";mp=a.out/"critical-primary-manifest.json"
 r={"format":FORMAT,"status":"running","parameters":{"author":"Astra-ISP-789f / normal_annihilator",
  "aiAssisted":"GPT-6 Astra Pro","prime":P,"finiteFieldScopeOnly":True,
  "normalFormsRecomputed":False,"gradedBasisRecomputed":False,"wholeTorsionRecomputed":False,
  "coefficientBocksteinComputed":False,"characteristicZeroConclusionInferred":False,
  "allLargeArraysTemporaryOnly":True},"events":[]}
 manifest=None;rc=1
 def save():
  r["elapsedSeconds"]=time.monotonic()-started;atomic(rp,r)
 def beat():
  if stop_requested or time.monotonic()>=deadline:raise Budget("complete factor checkpoints retained; stop before next exact operation")
 def put_phase(name,data):
  raw=canonical({"format":FORMAT+"-temporary-phase","binding":r["binding"],"phase":name,"data":data})
  p=a.out/(name+".json.gz");t=p.with_name(p.name+".tmp")
  with t.open("wb") as f:
   with gzip.GzipFile(filename="",mode="wb",fileobj=f,mtime=0,compresslevel=1) as z:z.write(raw)
  os.replace(t,p);d=record(p);d["payloadSHA256"]=digest(raw)
  manifest["phases"][name]=d;atomic(mp,manifest)
  r["events"].append({"phase":name,"reused":False,"elapsedSeconds":time.monotonic()-started});save()
  return data
 def get_phase(name):
  d=manifest["phases"].get(name)
  if d is None:return None
  p=a.out/d["file"];verify(p,(d["bytes"],d["sha256"]),"complete primary phase")
  with gzip.open(p,"rb") as f:raw=f.read()
  need(digest(raw)==d["payloadSHA256"],"primary payload hash");x=json.loads(raw)
  need(x["format"]==FORMAT+"-temporary-phase" and x["binding"]==r["binding"] and x["phase"]==name,"same original primary binding")
  r["events"].append({"phase":name,"reused":True});return x["data"]
 try:
  resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
  resource.setrlimit(resource.RLIMIT_CORE,(0,0));signal.signal(signal.SIGTERM,stop)
  hp=a.sources_root/HELPER;verify(hp,HELPER_PIN,"paid matrix reader")
  spec=importlib.util.spec_from_file_location("paid_original127_target_reader",hp)
  helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
  for name,pin in helper.PAID.items():verify(a.whole_out/name,pin,"whole299 "+name)
  parent=json.loads((a.whole_out/"original127-whole-torsion-pipeline-receipt.json").read_text())
  pp=parent["parameters"];ns=pp["nativeStatistics"]
  need(parent["status"]=="completed" and parent["binding"]==helper.WHOLE_BINDING and pp["wholeAffineDegreeVerified"] and pp["wholeAffineTorsionDegree"]==299,"complete original whole299 parent")
  need(pp["completeOriginalSourceCount"]==6188 and ns["phase"]==5 and ns["allKernelAndActionProductsVerified"] and ns["actualObservationStableRowReductionVerified"] and ns["wholeTorsionNotOnlyTargets"],"all original sources and all free directions covered by paid whole state")
  helper.read_hstar(a.hstar);integer_params=json.loads(a.hstar.read_text())
  identity={"algorithm":"complete-h-primary-powers-canonical-kernels-and-original-action-v1",
   "wrapperSHA256":sha(__file__),"helperSHA256":HELPER_PIN[1],"prime":P,
   "wholeBinding":helper.WHOLE_BINDING,"wholeGBBinding":helper.GB_BINDING,
   "paidFiles":{k:{"bytes":v[0],"sha256":v[1]} for k,v in helper.PAID.items()},
   "originalHStarParameters":{"bytes":helper.HSTAR_PIN[0],"sha256":helper.HSTAR_PIN[1]},
   "criticalIntegerFactors":["FPlus","FMinus","E8"],"completePrimaryNotOnlyParameterEigenvectors":True}
  r["binding"]=digest(canonical(identity));r["parameters"].update({"identity":identity,"seconds":a.seconds,"memoryMiB":a.memory_mib})
  if mp.exists():
   manifest=json.loads(mp.read_text());need(manifest["format"]==FORMAT+"-manifest" and manifest["binding"]==r["binding"],"exact primary continuation")
  else:
   need(not any(a.out.glob("*.json.gz")),"no unbound primary phases")
   manifest={"format":FORMAT+"-manifest","binding":r["binding"],"phases":{}};atomic(mp,manifest)
  import flint
  from flint import nmod_mat,nmod_poly
  r["parameters"]["pythonFlintVersion"]=getattr(flint,"__version__","unknown")
  J,T,audit=helper.read_state(a.whole_out/"torsion-whole-state.bin",nmod_mat)
  r["parameters"]["originalStateAudit"]=audit
  ch=json.loads((a.whole_out/"whole-torsion-characteristic.json").read_text())
  need(ch["binding"]==helper.WHOLE_BINDING and ch["wholeStateSHA256"]==helper.PAID["torsion-whole-state.bin"][1] and ch["completeFactorProductVerified"] and ch["characteristicDegree"]==299,"paid complete characteristic and factors")
  full=nmod_poly(ch["coefficients"],P);product=nmod_poly([ch["factorizationUnit"]],P);multiplicity={}
  for entry in ch["factors"]:
   h=nmod_poly(entry["coefficients"],P);m=int(entry["multiplicity"])
   need(int(h.degree())==entry["degree"] and helper.poly_coeff(h)[-1]==1 and m>=1,"actual monic characteristic factor")
   product*=h**m;multiplicity[tuple(helper.poly_coeff(h))]=m
  need(product==full and full.degree()==299,"all whole characteristic factors multiply back")
  factors=[]
  for label in ("FPlus","FMinus","E8"):
   q=helper.monic(nmod_poly([int(v)%P for v in integer_params[label]],P),nmod_poly)
   unit,fac=q.factor();reconstructed=nmod_poly([int(unit)],P)
   for index,(h,e) in enumerate(fac):
    need(int(e)==1,"each original critical polynomial is squarefree at127")
    reconstructed*=h**int(e);key=tuple(helper.poly_coeff(h))
    need(key in multiplicity,"each critical irreducible factor belongs to the paid whole characteristic")
    factors.append({"label":label+"-"+str(index+1),"originalFactor":label,
     "coefficients":list(key),"degree":int(h.degree()),"characteristicMultiplicity":multiplicity[key]})
   need(reconstructed==q,"complete original critical factor product")
  need(len(factors)==5 and len({tuple(x["coefficients"]) for x in factors})==5,"five disjoint actual critical factors")
  n=J.nrows();I=nmod_mat(n,n,[1 if i==j else 0 for i in range(n) for j in range(n)],P)
  summaries=[];bases=[];total_products=0
  for item in factors:
   name="primary-"+item["label"];data=get_phase(name)
   h=nmod_poly(item["coefficients"],P);degree=item["degree"];multip=item["characteristicMultiplicity"];dim=degree*multip
   if data is None:
    beat();H=nmod_mat(n,n,P)
    for c in reversed(item["coefficients"]):
     beat();H=J*H
     if c:H+=helper.scaled(I,c,nmod_mat)
    power=I;nullities=[0];ranks=[n];increments=[];maxexp=None
    for e in range(1,multip+1):
     beat();power=H*power;rank=int(power.rank());nullity=n-rank
     need(0<=nullity<=dim and nullity>=nullities[-1] and nullity%degree==0,"complete primary power-kernel dimensions")
     delta=(nullity-nullities[-1])//degree
     need(delta>0 and (not increments or delta<=increments[-1]),"positive decreasing cyclic-block counts until primary saturation")
     ranks.append(rank);nullities.append(nullity);increments.append(delta)
     if nullity==dim:maxexp=e;break
    need(maxexp is not None,"all primary directions actually exit by full characteristic multiplicity")
    beat();R,rank=power.rref();rank=int(rank);piv=helper.pivots(R,rank)
    free=[j for j in range(n) if j not in set(piv)]
    need(len(free)==dim and rank==n-dim,"full canonical primary kernel dimension")
    flat=[0]*(n*dim)
    for j,f in enumerate(free):
     flat[f*dim+j]=1
     for i,p in enumerate(piv):flat[p*dim+j]=(-int(R[i,f]))%P
    U=nmod_mat(n,dim,flat,P)
    need(helper.choose_rows(U,free,nmod_mat)==nmod_mat(dim,dim,[1 if i==j else 0 for i in range(dim) for j in range(dim)],P),"original-coordinate primary free identity")
    beat();need(helper.zero(power*U),"all original299 primary-kernel products")
    JU=J*U;Jh=helper.choose_rows(JU,free,nmod_mat)
    need(U*Jh==JU,"all original299 primary-action products")
    actual_char=Jh.charpoly();actual_min=Jh.minpoly()
    need(actual_char==h**multip and actual_min==h**maxexp,"entire primary characteristic and exact maximal exponent")
    cyclic=[]
    for e,b in enumerate(increments,1):
     number=b-(increments[e] if e<len(increments) else 0)
     need(number>=0,"nonnegative exact cyclic-block count")
     cyclic.extend([e]*number)
    need(sum(cyclic)==multip and len(cyclic)==increments[0] and max(cyclic)==maxexp,"complete primary cyclic decomposition")
    summary={**item,"primaryDimension":dim,"powerRanksIncludingZero":ranks,
     "powerNullitiesIncludingZero":nullities,"cyclicBlockCountsAtLeastEachPower":increments,
     "completeCyclicExponents":cyclic,"cyclicBlockCount":len(cyclic),"maximumExponent":maxexp,
     "allPrimaryDirectionsRetained":True,"canonicalKernelFreeIdentityVerified":True,
     "allOriginalPrimaryKernelProductsVerified":True,"kernelProductCoordinates":n*dim,
     "allOriginalPrimaryActionProductsVerified":True,"actionProductCoordinates":n*dim,
     "entirePrimaryCharacteristicVerified":True,"exactMinimalPolynomialVerified":True,
     "requiredUnramifiedRingDimensionForOneMaximalJet":degree*maxexp}
    data=put_phase(name,{"summary":summary,"original299Basis":helper.mat_data(U),
     "primaryAction":helper.mat_data(Jh),"originalFreeCoordinateRows":free,
     "polynomialPowerSHA256":helper.mat_data(power)["entriesSHA256"]})
   summary=data["summary"]
   need(all(summary[k]==item[k] for k in item) and summary["allPrimaryDirectionsRetained"] and summary["allOriginalPrimaryKernelProductsVerified"] and summary["allOriginalPrimaryActionProductsVerified"],"cached complete primary scope")
   U=helper.from_data(data["original299Basis"],nmod_mat)
   bases.append(U);summaries.append(summary);total_products+=summary["kernelProductCoordinates"]+summary["actionProductCoordinates"]
   r["parameters"]["completePrimaryProfiles"]=summaries;save()
  beat();columns=sum(U.ncols() for U in bases)
  union=nmod_mat(n,columns,[int(U[i,j]) for i in range(n) for U in bases for j in range(U.ncols())],P)
  need(int(union.rank())==columns and columns==sum(x["degree"]*x["characteristicMultiplicity"] for x in factors),"complete disjoint critical primary sum in original299 coordinates")
  r["parameters"].update({"completePrimaryProfiles":summaries,"criticalPrimaryDimension":columns,
   "allFiveCriticalFactorsComplete":True,"allPrimaryBasesDirectSumVerified":True,
   "allOriginalKernelAndActionProductCoordinates":total_products,
   "generalizedDetectorMustCoverAllCyclicBlocks":True,"coefficientBocksteinComputed":False})
  r["status"]="completed";r["outcome"]="all-five-complete-original-critical-primary-profiles";rc=0
 except Budget as e:
  r["status"]="budget-checkpoint";r["outcome"]="complete-primary-factor-phases-retained"
  r["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};rc=75
 except BaseException as e:
  r["status"]="failed";r["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};rc=1
 finally:
  if manifest is not None:
   r["parameters"]["completedTemporaryPhases"]=manifest["phases"]
   if mp.exists():r["parameters"]["temporaryManifest"]=record(mp)
  save()
 print(json.dumps({"status":r["status"],"outcome":r.get("outcome"),"elapsedSeconds":r["elapsedSeconds"],
  "error":r["parameters"].get("error")}),flush=True)
 return rc
if __name__=="__main__":sys.exit(main())
