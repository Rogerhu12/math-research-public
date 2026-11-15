#!/usr/bin/env python3
"""Checkpointed sparse Dixon on the paid2751 unit, then exact original seven recovery.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
No original normal form, old finite rank, or paid1567 pivot is recomputed.
"""
import argparse,fractions,gzip,hashlib,json,math,os,pathlib,resource,shlex,signal,struct,subprocess,sys,time,traceback
sys.dont_write_bytecode=True
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
S_ID={"bytes":80674893,"sha256":"54288bdab2af917695df1a9e2e681cafffaee435ef0fcc86d766f058324d94ba"}
S_BIND="044ea5d75d28042c53c2db1896ec186173b6b320e598cc35208d761f48dbdad0"
C_ID={"bytes":109635,"sha256":"1b8ce16d22d6435ae3c61ec00a4b7cd2a583bc17c1b93231e0011b3a3d3fab2e"}
G_ID={"bytes":118120,"sha256":"9ff2019837a8d86d8c1d912821802971150bb9c8fde844dae182624d43586ec4"}
G_BIND="6bf64a842cf35cb7ee587a9e6c86c4f9fade57ae88c206caef62bf9f4c83f6c5"
CPP_SHA="0bad7fcf2973d9a8d1f76250ca40f93bcdaaab8abeaea884ab4deba5d02824e7"
OLD_SHA="c9d064c4a64c8f0c9ef78b93db68c9d30883c42eb0a85e931e87a7bf862b98c6"
OLD_BIND="74bf887ac9ce134b551b8957061bc713cded79bd6a88e7a35fe8faa3101bb58c"
CORE_ID={"bytes":1497227,"sha256":"5cd0c5430089a3d4431ef6d058ec36a55d084d70e311cf13790fd60a5457efcc"}
PROFILE_ID={"bytes":62084,"sha256":"43cd638dfe13978f375490db9afdca5f318e137a384820b69bbc74b0ce48a7df"}
class BudgetExpired(Exception):pass
def need(v,s):
 if not v:raise ValueError(s)
def sha(p):
 h=hashlib.sha256();n=0
 with pathlib.Path(p).open("rb") as f:
  while True:
   z=f.read(1048576)
   if not z:break
   n+=len(z);h.update(z)
 return {"bytes":n,"sha256":h.hexdigest()}
def read(p):
 p=pathlib.Path(p)
 with (gzip.open(p,"rt",encoding="utf-8") if p.suffix==".gz" else p.open()) as f:return json.load(f)
def save(p,x):
 p=pathlib.Path(p);q=p.with_name(p.name+".tmp")
 with (gzip.open(q,"wt",encoding="utf-8",compresslevel=1) if p.suffix==".gz" else q.open("w")) as f:json.dump(x,f,separators=(",",":"))
 os.replace(q,p);return {"file":p.name,**sha(p),"temporaryOnly":True}
def ident(rec):return {k:rec[k] for k in ("bytes","sha256")}
class BinWriter:
 def __init__(self,p):self.p=pathlib.Path(p);self.t=self.p.with_name(self.p.name+".tmp");self.f=self.t.open("wb");self.h=hashlib.sha256();self.n=0
 def raw(self,b):self.f.write(b);self.h.update(b);self.n+=len(b)
 def u(self,v):self.raw(struct.pack("<I",v))
 def z(self,v):
  v=int(v);b=abs(v).to_bytes((abs(v).bit_length()+7)//8,"big");self.raw(struct.pack("<i",-len(b) if v<0 else len(b)));self.raw(b)
 def close(self):
  self.f.flush();os.fsync(self.f.fileno());self.f.close();os.replace(self.t,self.p);return {"file":self.p.name,"bytes":self.n,"sha256":self.h.hexdigest(),"temporaryOnly":True}
class BinReader:
 def __init__(self,p):self.f=pathlib.Path(p).open("rb")
 def raw(self,n):
  b=self.f.read(n);need(len(b)==n,"complete native solution record");return b
 def u(self):return struct.unpack("<I",self.raw(4))[0]
 def z(self):
  n=struct.unpack("<i",self.raw(4))[0];need(abs(n)<100000000,"bounded native integer record");v=int.from_bytes(self.raw(abs(n)),"big");return -v if n<0 else v
 def close(self):need(self.f.read(1)==b"","complete solution EOF");self.f.close()
def child(cmd,log,seconds,grace):
 start=time.monotonic()
 with pathlib.Path(log).open("a") as f:
  p=subprocess.Popen(cmd,stdout=f,stderr=subprocess.STDOUT,start_new_session=True)
  try:p.wait(timeout=max(.01,seconds));timed=False
  except subprocess.TimeoutExpired:
   timed=True;os.killpg(p.pid,signal.SIGTERM)
   try:p.wait(timeout=grace)
   except subprocess.TimeoutExpired:os.killpg(p.pid,signal.SIGKILL);p.wait()
 return {"exitCode":p.returncode,"elapsedSeconds":time.monotonic()-start,"outerDeadlineReached":timed}
def main(argv):
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ["native-source","state","columns","scales","old-solver","old-dir","helper","point-model","native-model","prepared-model","prime-dir","out"]:ap.add_argument("--"+k,required=True,type=pathlib.Path)
 ap.add_argument("--seconds",type=float,default=600);ap.add_argument("--memory-mib",type=int,default=2048)
 ap.add_argument("--compile-seconds",type=float,default=30);ap.add_argument("--maximum-digits",type=int,default=100000)
 ap.add_argument("--compiler",default="g++");ap.add_argument("--cxxflags",default="");ap.add_argument("--ldflags",default="-lflint -lgmp")
 a=ap.parse_args(argv)
 need(math.isfinite(a.seconds) and 0<a.seconds<=7200 and 0<a.memory_mib<=4096,"explicit bounded native shared budget")
 need(0<a.compile_seconds<=120 and 0<a.maximum_digits<=100000,"bounded compilation and iteration count")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 out=a.out.resolve();out.mkdir(parents=True,exist_ok=True);nativeout=out/"native";nativeout.mkdir(exist_ok=True)
 rec={"format":"isp-seven-original-checkpointed-sparse-dixon-pipeline-v1","status":"running",
  "oldNormalFormsRecomputed":False,"old1567PivotsRecomputed":False,"largeDataUploadedOrCommitted":False,
  "unitSolutionExactVerified":False,"fullOriginal4367VerificationComplete":False,
  "parameters":{"secondsLimit":a.seconds,"memoryMiBPerProcess":a.memory_mib,"compileSecondsLimit":a.compile_seconds},
  "events":[]}
 start=None;deadline=None;temps=[];code=1;binding=None
 def check():
  if deadline is not None and time.monotonic()>=deadline:raise BudgetExpired("actual shared mathematical deadline")
 def temp(p):
  p=pathlib.Path(p);x={"file":str(p.relative_to(out)) if p.is_relative_to(out) else p.name,**sha(p),"temporaryOnly":True}
  for k,r in enumerate(temps):
   if r["file"]==x["file"]:temps[k]=x;break
  else:temps.append(x)
  return x
 def checkpoint():
  rec["parameters"]["temporaryFiles"]=temps
  if start is not None:rec["mathematicalElapsedSeconds"]=time.monotonic()-start
  save(out/"seven-sparse-dixon-original-pipeline-receipt.json",rec)
 try:
  need(sha(a.native_source)["sha256"]==CPP_SHA,"frozen native source")
  need(sha(a.old_solver)["sha256"]==OLD_SHA,"unchanged original4367 consumer source")
  # Compilation is separate from the explicitly shared mathematical clock.
  exe=out/"sparse-dixon-native";cm=out/"native-compile-receipt.json"
  compile_material={"sourceSHA256":CPP_SHA,"compiler":a.compiler,"cxxflags":a.cxxflags,"ldflags":a.ldflags}
  if cm.exists() and exe.exists():
   old=read(cm);need(old["material"]==compile_material and old["executable"]==sha(exe) and old["status"]=="completed","actual compiled executable cache")
   rec["events"].append({"reusedNativeCompilation":True,"executable":old["executable"]})
  else:
   cmd=[a.compiler,"-std=c++17","-O2",*shlex.split(a.cxxflags),str(a.native_source),"-o",str(exe),*shlex.split(a.ldflags)]
   cr=child(cmd,out/"native-compile.log",a.compile_seconds,1)
   rec["parameters"]["lastCompilation"]={**cr,"command":cmd}
   if cr["exitCode"]!=0:
    rec["parameters"]["lastCompilation"]["logTail"]=(out/"native-compile.log").read_text(errors="replace")[-8000:]
   need(cr["exitCode"]==0 and exe.exists(),"native compilation succeeded within actual budget")
   save(cm,{"status":"completed","material":compile_material,"command":cmd,"executable":sha(exe),**cr})
   rec["events"].append({"newNativeCompilation":True,**cr})
  temp(cm)
  start=time.monotonic();deadline=start+a.seconds-min(5,a.seconds/20)
  need(sha(a.state)==S_ID and sha(a.columns)==C_ID and sha(a.scales)==G_ID,"same completed2751 state and actual two-sided scales")
  need(sha(a.old_dir/"seven-original-integer-core.json.gz")==CORE_ID and sha(a.old_dir/"seven-original-unit-row-profile.json")==PROFILE_ID,"same original full core and4318 unit profile")
  st=read(a.state);cs=read(a.columns);gs=read(a.scales);profile=read(a.old_dir/"seven-original-unit-row-profile.json")
  need(st["binding"]==S_BIND and st["originalBinding"]==OLD_BIND and gs["binding"]==G_BIND and gs["sourceBinding"]==S_BIND,"actual source and scale bindings")
  need(profile["binding"]==OLD_BIND and profile["coreIdentity"]==CORE_ID,"old true source profile")
  need(len(st["reverseSubstitutionDAG"])==1567 and len(st["rows"])==2751,"all inherited complete pivots and remaining rows")
  active=list(map(int,st["remainingSourceColumnPositions"]));need(active==sorted(set(active)) and len(active)==2751,"exact2751 source positions")
  h={int(j):int(v) for j,v in gs["columnPositionsAndPositiveContents"]}
  need(h=={int(j):int(v) for j,v in cs["columnPositionsAndPositiveContents"]} and set(h)==set(active),"same paid h scales")
  g={int(i):int(v) for i,v in gs["originalOutputRowsAndPositiveContents"]}
  need(len(g)==2751 and all(v>0 for v in h.values()) and all(v>0 for v in g.values()),"complete positive row and column scales")
  need(gs["all424921CoefficientDivisionsExact"] and cs["all424921EntriesExactlyDivisible"],"all original scaled entries paid")
  material={"runnerSHA256":sha(__file__)["sha256"],"nativeSHA256":CPP_SHA,"state":S_ID,"columns":C_ID,"scales":G_ID,
     "oldSolverSHA256":OLD_SHA,"oldCore":CORE_ID,"oldProfile":PROFILE_ID,"oldBinding":OLD_BIND,
     "equation":"diag(g)*Aprime*Z=E-p^k*N; z=diag(h)*x; full1567 reverse DAG"}
  binding=hashlib.sha256(json.dumps(material,sort_keys=True,separators=(",",":")).encode()).hexdigest()
  rec["parameters"].update({"binding":binding,"inputIdentity":material,"allActualRowScalesOne":all(v==1 for v in g.values()),
    "actualUnitSize":2751,"actualRHSCount":7,"actualSparseNonzeros":424921,
    "internalPrimeIsOnlyExactSolverUnitSelection":True})
  bp=out/"actual-scaled-sparse-seven.bin";bm=out/"actual-scaled-sparse-seven-input.json"
  if bp.exists() and bm.exists():
   pm=read(bm);need(pm["binding"]==binding and sha(bp)==ident(pm["input"]),"complete actual native input cache")
   rec["events"].append({"reusedCompleteNativeInput":True})
  else:
   loc={j:k for k,j in enumerate(active)};w=BinWriter(bp)
   w.raw(b"R15QDX7\0");w.u(1);w.u(2751);w.u(7);w.u(424921);w.raw(binding.encode())
   for j in active:w.u(j);w.z(h[j])
   nnz=0;seen=set()
   for k,row in enumerate(st["rows"]):
    i=int(row["originalOutputRow"]);need(i in g and i not in seen,"unique actual row scale");seen.add(i)
    w.u(i);w.z(g[i]);ee=list(map(int,row["rightHandSideSeven"]));need(len(ee)==7,"all original seven RHS")
    for v in ee:w.z(v)
    terms=sorted((loc[int(j)],int(v),int(j)) for j,v in row["coefficients"]);w.u(len(terms))
    need(len({j for j,v,orig in terms})==len(terms),"unique source positions")
    for j,v,orig in terms:
     d=g[i]*h[orig];need(v%d==0 and v!=0,"exact whole original entry division by g*h");w.u(j);w.z(v//d)
    nnz+=len(terms)
    if k%32==0:check()
   need(nnz==424921 and len(seen)==2751,"all original sparse entries serialized")
   ix=w.close();pm={"binding":binding,"input":ix,"all424921OriginalCoefficientDivisionsVerified":True}
   save(bm,pm)
  temp(bm);rec["parameters"]["nativeInputIdentity"]=ident(pm["input"])
  # The large paid coefficients can be released. The exact back-substitution DAG remains.
  del st["rows"];st.pop("initialRowContentDivisors",None);del cs,gs
  checkpoint();check()
  nrp=nativeout/"sparse-dixon-native-receipt.json";solution=nativeout/"active-unit-rational-solution.bin"
  nr=read(nrp) if nrp.exists() else None
  already=(nr is not None and nr.get("status")=="completed" and nr.get("binding")==binding and nr.get("unitSolutionExactVerified") and solution.exists())
  if already:
   need(sha(solution)=={"bytes":nr["parameters"]["solutionBytes"],"sha256":nr["parameters"]["solutionSHA256"]},"actual completed native solution bytes")
   rec["events"].append({"reusedCompletedNativeRationalSolution":True})
  else:
   rem=deadline-time.monotonic();need(rem>0,"positive native remaining budget")
   cr=child([str(exe),str(bp),str(nativeout),binding,str(rem),str(a.maximum_digits)],out/"native-exact-dixon.log",rem,8)
   rec["events"].append({"nativeRun":cr})
   nr=read(nrp) if nrp.exists() else {}
   rec["parameters"]["nativeStatistics"]=nr
   need(nr.get("binding")==binding,"native receipt bound to actual input")
   need(nr.get("parameters",{}).get("inputSHA256")==pm["input"]["sha256"],"native reader agrees actual whole input SHA")
   rec["parameters"]["nativeStatistics"]=nr
   temp(nrp);checkpoint()
   if cr["exitCode"]!=0 or nr.get("status")!="completed":
    if cr["outerDeadlineReached"] or cr["exitCode"]==75 or nr.get("status")=="budget-exhausted":raise BudgetExpired("native incomplete; actual inverse and last complete digit retained")
    raise ValueError("actual native stage failed; no rational solve claim")
  need(nr.get("unitSolutionExactVerified") and nr.get("phase")=="unit-seven-rational-solution-complete","true entire current integer unit equation")
  rec["unitSolutionExactVerified"]=True;rec["parameters"]["nativeStatistics"]=nr
  need(sha(solution)=={"bytes":nr["parameters"]["solutionBytes"],"sha256":nr["parameters"]["solutionSHA256"]},"native solution complete bytes")
  temp(nrp);temp(solution);checkpoint();check()
  from flint import fmpq
  revmeta=out/"reverse-substitution-active.json";revslot=-1;completed=0
  if revmeta.exists():
   meta=read(revmeta);need(meta["binding"]==binding and meta["nativeSolution"]==sha(solution),"same reverse-DAG solution binding")
   rp=out/meta["file"];need(sha(rp)==ident(meta),"actual full reverse-DAG checkpoint bytes")
   rd=read(rp);need(rd["binding"]==binding,"same full reverse-DAG state")
   x={int(j):[fmpq(int(n),int(d)) for n,d in v] for j,v in rd["sourceValues"]}
   completed=int(rd["completedReversePivots"]);revslot=int(meta["slot"])
   need(len(x)==2751+completed and 0<=completed<=1567,"complete inverse-DAG pivot cursor")
   rec["events"].append({"reusedCompletedReversePivots":completed})
  else:
   r=BinReader(solution);need(r.raw(8)==b"Q7SOLV1\0" and r.raw(64).decode()==binding,"complete source solution header")
   n,m,p,digits=(r.u() for _ in range(4));need((n,m)==(2751,7),"all2751 by7 solution entries")
   D=[r.z() for _ in range(7)];need(all(v>0 for v in D),"positive actual seven denominators")
   x={}
   for j in active:x[j]=[fmpq(r.z(),D[t]*h[j]) for t in range(7)]
   r.close()
  def save_reverse():
   nonlocal revslot
   slot=0 if revslot<0 else 1-revslot;p=out/("reverse-substitution-%d.json.gz"%slot)
   xx={"binding":binding,"completedReversePivots":completed,"sourceValues":[[j,[[str(v.p),str(v.q)] for v in x[j]]] for j in sorted(x)]}
   rr=save(p,xx);save(revmeta,{"binding":binding,"nativeSolution":sha(solution),"slot":slot,**rr});revslot=slot
  if revslot<0:save_reverse()
  dag=st["reverseSubstitutionDAG"]
  try:
   for k in range(completed,1567):
    check();z=dag[1567-1-k];j=int(z["sourceColumnPosition"]);need(j not in x,"new inverse-DAG source coordinate")
    aa=int(z["pivotCoefficient"]);need(aa!=0,"true nonzero rational pivot")
    v=[fmpq(int(y)) for y in z["rightHandSideSeven"]]
    for c,b in z["otherTerms"]:
     c=int(c);b=int(b);need(c in x,"all successor coordinates already restored")
     for t in range(7):v[t]-=b*x[c][t]
    v=[y/aa for y in v]
    # Equation is reconstructed exactly from this original integer pivot row.
    need(all(aa*v[t]==fmpq(int(z["rightHandSideSeven"][t]))-sum((int(b)*x[int(c)][t] for c,b in z["otherTerms"]),fmpq(0)) for t in range(7)),"all seven actual reverse-pivot identities")
    x[j]=v;completed=k+1
    if completed%64==0:save_reverse()
  except BudgetExpired:
   save_reverse();rec["parameters"]["completedReversePivots"]=completed;raise
  save_reverse();temp(revmeta);rec["parameters"]["completedReversePivots"]=completed
  pp=list(map(int,profile["pivotColumnPositions"]));need(set(x)==set(pp) and len(x)==4318,"all original4318 source coordinates restored")
  oldsolution=a.old_dir/"seven-original-unit-block-solution.json.gz"
  sols={"format":"isp-seven-exact-original-unit-solution-v1","binding":OLD_BIND,"rows":4318,"columns":7,
    "unitProfileIdentity":PROFILE_ID,"solutionPairsByRows":[[[str(v.p),str(v.q)] for v in x[j]] for j in pp],
    "equation":"B*X=E; original source graph uses -X","fullOriginalProductsVerified":False}
  if oldsolution.exists():need(read(oldsolution)==sols,"existing old4318 solution exact agreement")
  else:save(oldsolution,sols)
  rec["parameters"]["restoredOriginalUnitSolution"]=temp(oldsolution)
  # Large local rational states may now be discarded from this process; all are retained on disk.
  del x,st,sols;checkpoint();check()
  cmd=[sys.executable,"-B",str(a.old_solver),"--helper",str(a.helper),"--point-model",str(a.point_model),
     "--native-model",str(a.native_model),"--prepared-model",str(a.prepared_model),"--prime-dir",str(a.prime_dir),
     "--out",str(a.old_dir),"--seconds",str(min(1200,deadline-time.monotonic())),"--memory-mib",str(a.memory_mib),"--resume"]
  rem=deadline-time.monotonic();cr=child(cmd,out/"original4367-consumer.log",rem,2)
  rec["events"].append({"originalFrozenConsumer":cr})
  oldrec=read(a.old_dir/"seven-exact-rational-original-receipt.json")
  safe=dict(oldrec);safe["events"]=[e if isinstance(e,dict) else {"event":str(e)} for e in oldrec.get("events",[])]
  save(out/"original4367-consumer-sanitized-receipt.json",safe);temp(out/"original4367-consumer-sanitized-receipt.json")
  rec["parameters"]["originalFullConsumerStatistics"]=safe
  if cr["exitCode"]!=0 or oldrec.get("status")!="completed":
   if cr["outerDeadlineReached"] or cr["exitCode"]==75 or oldrec.get("status")=="budget-exhausted":raise BudgetExpired("original continuation incomplete; all solved source coordinates retained")
   raise ValueError("original4367 consumer failed; not a full original certificate")
  need(oldrec.get("completeRationalComplementKernelCertified") and oldrec.get("all4367ExactKernelProductsZero") and oldrec.get("all1834OutsideSourceCoordinatesZero") and oldrec.get("allFirst29FreeCoordinatesZero"),"entire original source classification certified")
  for k in ["newTrueComplementKernelDimension","combinedPaid29AndNewKernelDimension","completeTailSevenFreeImageRankOverQ","completeSelectedOriginalC0RankOverQ","completeSelectedOriginalB0RankOverQ","completeSelectedB0RankLowerBound","completeSelectedB0RankUpperBound","completeOriginalGraphResidualRankOverQ","completeOriginalOutputIResidualRankOverQ"]:
   rec[k]=oldrec[k]
  rec.update(status="completed",fullOriginal4367VerificationComplete=True,
     outcome="complete-original-seven-complement-classification")
  code=0
 except BudgetExpired as e:rec.update(status="budget-exhausted",error=str(e));code=75
 except Exception as e:
  rec.update(status="failed",error=str(e),exceptionType=type(e).__name__);(out/"exception.log").write_text(traceback.format_exc());code=1
 finally:
  # Small permanent metadata only; every large checkpoint remains temporary in this same job.
  if binding is not None:
   for name in ["checkpoint-active.txt","inverse-meta.txt"]:
    p=nativeout/name
    if p.exists():temp(p)
   if (out/"reverse-substitution-active.json").exists():temp(out/"reverse-substitution-active.json")
  checkpoint()
 need((out/"seven-sparse-dixon-original-pipeline-receipt.json").stat().st_size<100000,"small persistent conclusion receipt")
 print(json.dumps(rec),flush=True);return code
if __name__=="__main__":sys.exit(main(sys.argv[1:]))
