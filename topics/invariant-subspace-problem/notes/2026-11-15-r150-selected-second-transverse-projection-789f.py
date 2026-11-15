#!/usr/bin/env python3
"""Exact same-J projection to at most two transverse factors.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
Keeps all17 primitive equations. No old large solve or factor31 lift.
"""
import argparse,gzip,hashlib,itertools,json,math,os,pathlib,resource,signal,sys,time,traceback
sys.dont_write_bytecode=True
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
POINT_SHA="97d31570a0bd99d33066fc6ea47984203b2964521ceeb50920f0a49dd3bb8074"
MODEL_ID={"bytes":814572,"sha256":"0aa2d6d5c368b9885e279cd5b8e2cc7a59ba574ca161c0535193c30defe52d3d"}
PROFILE_ID={"bytes":62084,"sha256":"43cd638dfe13978f375490db9afdca5f318e137a384820b69bbc74b0ce48a7df"}
class BudgetExpired(Exception):pass
def need(v,s):
 if not v:raise ValueError(s)
def sha(p):
 h=hashlib.sha256();n=0
 with pathlib.Path(p).open("rb") as f:
  while True:
   b=f.read(1048576)
   if not b:break
   n+=len(b);h.update(b)
 return {"bytes":n,"sha256":h.hexdigest()}
def read(p):
 p=pathlib.Path(p)
 with (gzip.open(p,"rt",encoding="utf-8") if p.suffix==".gz" else p.open()) as f:return json.load(f)
def save(p,x):
 p=pathlib.Path(p);q=p.with_name(p.name+".tmp")
 with (gzip.open(q,"wt",encoding="utf-8",compresslevel=1) if p.suffix==".gz" else q.open("w")) as f:json.dump(x,f,separators=(",",":"))
 os.replace(q,p);return {"file":p.name,**sha(p),"temporaryOnly":True}
def matrix_sha(M):
 h=hashlib.sha256();h.update(("%d,%d\n"%(M.nrows(),M.ncols())).encode())
 for i in range(M.nrows()):h.update(("\t".join(str(M[i,j]) for j in range(M.ncols()))+"\n").encode())
 return h.hexdigest()
def zeros(M):return all(not M[i,j] for i in range(M.nrows()) for j in range(M.ncols()))
def main(argv):
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ["point-model","selected-model","unit-profile","out"]:ap.add_argument("--"+k,type=pathlib.Path,required=True)
 ap.add_argument("--seconds",type=float,default=30);ap.add_argument("--memory-mib",type=int,default=512)
 a=ap.parse_args(argv);need(0<a.seconds<=120 and 0<a.memory_mib<=4096,"bounded exact second-transverse projection")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 start=time.monotonic();out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 rec={"format":"isp-selected-J-second-transverse-exact-projection-v1","status":"running","phase":"input",
  "oldLargeNormalFormsRecomputed":False,"newOriginalDixonDigitsComputed":0,
  "newOriginalRationalSourceSolvePerformed":False,"largeDataUploadedOrCommitted":False,"events":[],"parameters":{}}
 temps=[];code=1
 def checkpoint():
  rec["parameters"]["temporaryFiles"]=temps;rec["mathematicalElapsedSeconds"]=time.monotonic()-start
  save(out/"selected-second-transverse-projection-receipt.json",rec)
 def alarm(sig,frame):raise BudgetExpired("actual shared second-transverse deadline")
 signal.signal(signal.SIGALRM,alarm);signal.setitimer(signal.ITIMER_REAL,a.seconds)
 try:
  need(sha(a.point_model)["sha256"]==POINT_SHA and sha(a.selected_model)==MODEL_ID and sha(a.unit_profile)==PROFILE_ID,"same original primitive point and I,J")
  point=read(a.point_model);model=read(a.selected_model);profile=read(a.unit_profile)
  J=set(map(int,model["selectedRows"]));I=set(map(int,profile["originalOutputI"]))
  need(len(J)==4354 and len(I)==4354 and point["characteristicZeroSameOriginal17Verified"],"same original selected sets and physical equations")
  eq=[list(map(int,r)) for r in point["primitivePointCoefficients"]];need(len(eq)==17 and all(len(r)==77 for r in eq),"all17 by77 coefficients")
  mon=[(i,) for i in range(11)]+[(i,j) for i in range(11) for j in range(i,11)]
  for e in range(17):need(all(eq[e][k]==0 for k,m in enumerate(mon) if all(i>=9 for i in m)),"every original equation vanishes on tangent plane")
  whole=[q for d in range(5,0,-1) for q in itertools.combinations_with_replacement(range(11),d)]
  need(len(whole)==4367,"all original output monomials")
  idx={q:i for i,q in enumerate(whole)}
  selectedout=[q for q in whole if 1<=sum(i<=8 for i in q)<=2];oi={q:i for i,q in enumerate(selectedout)}
  need(len(selectedout)==585 and sum(sum(i<=8 for i in q)==1 for q in selectedout)==135,"135 plus450 exact transverse outputs")
  nhigher=sum(sum(i<=8 for i in q)>=3 for q in whole);need(nhigher==3762,"all remaining higher outputs")
  mult=[q for d in range(4) for q in itertools.combinations_with_replacement(range(11),d)]
  selectedsrc=[]
  for k,q in enumerate(mult):
   if sum(i<=8 for i in q)>1:continue
   for e in range(17):
    raw=17*k+e+1
    if raw in J:selectedsrc.append((raw,e,q))
  material={"codeSHA256":sha(__file__)["sha256"],"pointSHA256":POINT_SHA,"selectedModel":MODEL_ID,"unitProfile":PROFILE_ID}
  binding=hashlib.sha256(json.dumps(material,sort_keys=True,separators=(",",":")).encode()).hexdigest()
  rec["parameters"].update({"binding":binding,"inputIdentity":material,
     "selectedSourceCount":len(selectedsrc),"outputCount":585,"higherOutputDimension":3762,
     "secondsLimit":a.seconds,"memoryMiB":a.memory_mib})
  inputp=out/"same-original-second-transverse-integer-input.json.gz"
  if inputp.exists():
   data=read(inputp);need(data["binding"]==binding,"reused actual projected input binding")
   sourcecols=[{int(i):int(v) for i,v in c} for c in data["originalSparseColumns"]]
   rec["events"].append({"reusedCompletedProjectedInput":True})
  else:
   sourcecols=[]
   for raw,e,q in selectedsrc:
    c={}
    for k,m in enumerate(mon):
     v=eq[e][k]
     if not v:continue
     mm=tuple(sorted(q+m))
     if mm in oi:i=oi[mm];c[i]=c.get(i,0)+v
    sourcecols.append({i:v for i,v in c.items() if v})
   data={"binding":binding,"originalSourceRows":[v[0] for v in selectedsrc],
     "originalOutputIndices":[idx[q] for q in selectedout],"originalOutputMonomials":[list(q) for q in selectedout],
     "originalSparseColumns":[[[i,str(v)] for i,v in sorted(c.items())] for c in sourcecols],
     "allOtherSelectedSourceColumnsProjectToZeroByTransverseDegree":True}
   save(inputp,data)
  temps.append({"file":inputp.name,**sha(inputp),"temporaryOnly":True})
  need(len(sourcecols)==len(selectedsrc),"all original participating sources retained")
  from flint import fmpq,fmpq_mat
  content=[]
  for c in sourcecols:
   g=0
   for v in c.values():g=math.gcd(g,abs(v))
   content.append(g or 1)
  T=fmpq_mat(len(sourcecols),585,[c.get(i,0)//g for c,g in zip(sourcecols,content) for i in range(585)])
  need(all(v%g==0 for c,g in zip(sourcecols,content) for v in c.values()),"exact positive source-content normalization")
  rec.update(phase="complete-left-nullspace",
     projectedNonzeroEntries=sum(len(c) for c in sourcecols),
     projectedZeroSourceColumns=sum(not c for c in sourcecols))
  checkpoint()
  nullp=out/"second-transverse-complete-left-nullspace.json.gz"
  if nullp.exists():
   saved=read(nullp);need(saved["binding"]==binding and saved["inputIdentity"]==sha(inputp),"same completed rational projection nullspace")
   rank=int(saved["rank"]);free=list(map(int,saved["freeOutputIndicesWithin585"]))
   L=fmpq_mat(585,len(free),[fmpq(s) for row in saved["leftKernelRows"] for s in row])
   need(zeros(T*L),"all actual normalized source rows verified on restored nullspace")
   rec["events"].append({"reusedCompletedProjectionNullspace":True})
  else:
   R,rr=T.rref();rank=int(rr);piv=[]
   for i in range(rank):
    p=next((j for j in range(585) if R[i,j]),None);need(p is not None and R[i,p]==1,"actual exact RREF pivot");piv.append(p)
   need(piv==sorted(set(piv)),"strict complete pivot order")
   free=[j for j in range(585) if j not in set(piv)]
   L=fmpq_mat(585,len(free))
   for c,f in enumerate(free):
    L[f,c]=1
    for r,p in enumerate(piv):L[p,c]=-R[r,f]
   # Save the full candidate before the possibly longer whole product validation.
   save(nullp,{"binding":binding,"inputIdentity":sha(inputp),"rank":rank,
     "freeOutputIndicesWithin585":free,"leftKernelRows":[[str(L[i,j]) for j in range(L.ncols())] for i in range(585)],
     "allOriginalProjectedProductsVerified":False})
   del R
   need(zeros(T*L),"all original projected source rows times full rational left kernel")
  need(rank+len(free)==585 and len(set(free))==len(free),"complete rank/nullity and unique free coordinates")
  for c,f in enumerate(free):need(all(L[f,k]==(1 if k==c else 0) for k in range(len(free))),"all independent left-kernel free coordinates")
  temps.append({"file":nullp.name,**sha(nullp),"temporaryOnly":True})
  excluded=[i for i,q in enumerate(selectedout) if idx[q] not in I]
  need(len(excluded)==3,"exact excluded one-transverse linear outputs")
  eRank=int(fmpq_mat([[L[i,j] for j in range(L.ncols())] for i in excluded]).rank())
  rankI=rank-len(excluded)+eRank
  fullupper=min(4324,3762+rank);Iupper=min(fullupper,3762+rankI)
  need(fullupper>=4318 and Iupper>=4318,"compatible with actual mod31 full and square lower bounds")
  kLower=4354-fullupper
  # The separately paid same-J whole32x7 first-connection envelope is ZERO.
  sLower=kLower
  rec.update({"status":"completed","phase":"complete",
    "exactProjectedRankOverQ":rank,
    "completeIndependentLeftKernelDimension":len(free),
    "allOriginalProjectedSourceRowsVerified":True,
    "allLeftKernelFreeCoordinatesIdentity":True,
    "selectedProjectedOutputIRankOverQ":rankI,
    "selectedOriginalFullConstantRankLowerBound":4318,
    "selectedOriginalFullConstantRankUpperBound":fullupper,
    "selectedOriginalSquareConstantRankLowerBound":4318,
    "selectedOriginalSquareConstantRankUpperBound":Iupper,
    "selectedFullConstantRankExactly4318":fullupper==4318,
    "selectedSquareConstantRankExactly4318":Iupper==4318,
    "selectedFullConstantKernelDimensionLowerBound":kLower,
    "paidSelectedFullFirstConnectionEnvelopeZeroRetained":True,
    "selectedFirstLiftConstantDimensionLowerBound":sLower,
    "sameMinorInfinityOrderLowerBound":sLower+14,
    "replacementInfinityOrderLowerBound":sLower+13,
    "cofactorInfinityOrderLowerBound":sLower+12,
    "conditionalSourceCostUnderK67":8734-sLower,
    "conditionalSourceCostUnderPaidK70":8731-sLower,
    "newExplicitOriginalKernelColumnsConstructed":0})
  rec["parameters"].update({"sourceRows":data["originalSourceRows"],
    "excludedProjectedOutputs":[{"within585":i,"originalOutputIndex":idx[selectedout[i]],"monomial":list(selectedout[i])} for i in excluded],
    "excludedOutputRowsOfLeftKernelRank":eRank,
    "matrixSHA256":{"sourceContentNormalizedTranspose":matrix_sha(T),"completeLeftKernel":matrix_sha(L)},
    "allOriginalSourceContentDivisionsVerified":True,
    "paidFirstConnectionZeroReceipt":"notes/r150-infinity-remote-session-789f/43679903558-selected-pure-projection-rank.json"})
  code=0
 except BudgetExpired as e:rec.update(status="budget-exhausted",error=str(e));code=75
 except Exception as e:
  rec.update(status="failed",error=str(e),exceptionType=type(e).__name__);(out/"exception.log").write_text(traceback.format_exc());code=1
 finally:
  signal.setitimer(signal.ITIMER_REAL,0);checkpoint()
 need((out/"selected-second-transverse-projection-receipt.json").stat().st_size<100000,"small permanent receipt")
 print(json.dumps(rec),flush=True);return code
if __name__=="__main__":sys.exit(main(sys.argv[1:]))
