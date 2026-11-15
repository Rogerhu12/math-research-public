#!/usr/bin/env python3
"""Same original selected J: exact pure-tangent projection and first-lift envelope.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
No large rank or new original rational solve is performed.
"""
import argparse,gzip,hashlib,importlib.util,itertools,json,os,pathlib,resource,signal,sys,time,traceback
sys.dont_write_bytecode=True
GEN_SHA="2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186"
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
def main(argv):
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ["generator","point-model","selected-model","unit-profile","out"]:ap.add_argument("--"+k,type=pathlib.Path,required=True)
 ap.add_argument("--seconds",type=float,default=10);ap.add_argument("--memory-mib",type=int,default=512)
 a=ap.parse_args(argv);need(0<a.seconds<=60 and 0<a.memory_mib<=2048,"explicit small-probe budget")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 start=time.monotonic();out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 rec={"format":"isp-same-original-selected-J-pure-projection-envelope-v1","status":"running",
  "newOriginalLargeRankComputed":False,"newOriginalRationalSourcesComputed":False,
  "old1567PivotsRecomputed":False,"largeDataUploadedOrCommitted":False,"events":[],"parameters":{}}
 temps=[];code=1
 def alarm(sig,frame):raise BudgetExpired("actual10-second projection budget")
 signal.signal(signal.SIGALRM,alarm);signal.setitimer(signal.ITIMER_REAL,a.seconds)
 try:
  need(sha(a.generator)["sha256"]==GEN_SHA and sha(a.point_model)["sha256"]==POINT_SHA,"same physical generator and primitive point")
  need(sha(a.selected_model)==MODEL_ID and sha(a.unit_profile)==PROFILE_ID,"same original4354 sources and outputs")
  point=read(a.point_model);model=read(a.selected_model);profile=read(a.unit_profile)
  J=set(map(int,model["selectedRows"]));I=set(map(int,profile["originalOutputI"]))
  need(len(J)==4354 and len(I)==4354 and all(1<=x<=6188 for x in J),"same original I,J sizes")
  material={"codeSHA256":sha(__file__)["sha256"],"generatorSHA256":GEN_SHA,"pointSHA256":POINT_SHA,
    "selectedModel":MODEL_ID,"unitProfile":PROFILE_ID}
  binding=hashlib.sha256(json.dumps(material,sort_keys=True,separators=(",",":")).encode()).hexdigest()
  sp=importlib.util.spec_from_file_location("actual_physical",a.generator);G=importlib.util.module_from_spec(sp);sp.loader.exec_module(G)
  from flint import fmpq,fmpq_mat
  primitive=[list(map(int,r)) for r in point["primitivePointCoefficients"]]
  need(point["characteristicZeroSameOriginal17Verified"] and len(primitive)==17 and all(len(r)==77 for r in primitive),"all17 primitive rows")
  K=fmpq_mat([[G.ORIGINAL_K[5-i][5-j] for j in range(6)] for i in range(6)])
  evaluate,_=G.original_jet_evaluator(K);zero=[fmpq(0)]*11
  need(all(x==0 for x in evaluate(zero,zero)[0]),"no physical constant terms")
  mons=[(i,) for i in range(11)]+[(i,j) for i in range(11) for j in range(i,11)]
  mi={m:i for i,m in enumerate(mons)};phys=[[fmpq(0)]*77 for _ in range(17)];at=[]
  for i in range(11):
   v=G.sequence(i);p=evaluate(v,zero)[0];n=evaluate([-x for x in v],zero)[0];at.append(p)
   for e in range(17):phys[e][i]=(p[e]-n[e])/2;phys[e][mi[(i,i)]]=(p[e]+n[e])/2
  for i in range(11):
   for j in range(i+1,11):
    v=G.sequence(i);v[j]+=1;p=evaluate(v,zero)[0]
    for e in range(17):phys[e][mi[(i,j)]]=p[e]-at[i][e]-at[j][e]
  perm=[10-e if e<11 else 27-e for e in range(17)];invperm={v:k for k,v in enumerate(perm)};scales=[]
  for e,orig in enumerate(perm):
   row=[fmpq(primitive[orig][mi[tuple(sorted(10-i for i in m))]]) for m in mons]
   k=next((k for k,v in enumerate(phys[e]) if v),None);need(k is not None,"nonzero whole physical polynomial")
   c=row[k]/phys[e][k];need(c!=0 and all(row[t]==c*phys[e][t] for t in range(77)),"whole77 coefficient scaling for equation%d"%e);scales.append(c)
  P0,P1,outmons,srcrows,_=G.make_projection_jets("infinity")
  Q,fullrank,_,_=G.nullspace(P0);need(fullrank==128 and Q.ncols()==7,"paid full physical projection")
  srcindex={v:i for i,v in enumerate(srcrows)}
  multipliers=[q for d in range(4) for q in itertools.combinations_with_replacement(range(11),d)]
  chosen=[]
  for k,q in enumerate(multipliers):
   if any(j not in (9,10) for j in q):continue
   aa=q.count(10);bb=q.count(9)
   for orig in range(17):
    raw=17*k+orig+1
    if raw in J:chosen.append((raw,invperm[orig],aa,bb,srcindex[(invperm[orig],aa,bb)]))
  nPure=len(chosen);nNonpure=4354-nPure
  # Retain actual primitive equation scales in BOTH zero/first jets.
  PJ=fmpq_mat(nPure,135,[scales[e]*P0[row,c] for raw,e,aa,bb,row in chosen for c in range(135)])
  P1J=fmpq_mat(nPure,135,[scales[e]*P1[row,c] for raw,e,aa,bb,row in chosen for c in range(135)])
  U,rJT,_,_=G.nullspace(PJ.transpose());rJ=int(rJT)
  need(rJ<=128,"selected projection sits in the full projection")
  C=U.transpose()*P1J*Q
  cRank=int(C.rank())
  need(G.matrix_zero(PJ.transpose()*U),"complete selected pure-source relation kernel")
  output=[q for d in range(5,0,-1) for q in itertools.combinations_with_replacement(range(11),d)]
  need(len(output)==4367,"same original output monomial order")
  counts={0:0,1:0,2:0}
  excluded=[]
  for i,q in enumerate(output):
   z=sum(j<=8 for j in q);cat=min(z,2)
   if i in I:counts[cat]+=1
   else:excluded.append({"originalOutputIndex":i,"monomial":list(q),"transverseDegree":z})
  rankUpper=min(4325,4212+rJ) # actual paid29 true kernels, plus this fresh projection upper bound.
  need(rankUpper>=4318,"compatible with actual original mod31 lower bound")
  exact=(rankUpper==4318);kLower=4354-rankUpper
  sLower=max(29,kLower-cRank)
  mt={"binding":binding,"selectedPureRows":[list(v) for v in chosen],"primitiveOverPhysicalScales":[str(v) for v in scales],
    "P0J":[[str(PJ[i,j]) for j in range(135)] for i in range(nPure)],
    "P1J":[[str(P1J[i,j]) for j in range(135)] for i in range(nPure)],
    "completeSelectedPureRelationColumns":[[str(U[i,j]) for i in range(nPure)] for j in range(U.ncols())],
    "completeFullProjectionQColumns":[[str(Q[i,j]) for i in range(135)] for j in range(7)],
    "upperEnvelopeConnection":[[str(C[i,j]) for j in range(7)] for i in range(C.nrows())]}
  temps.append(save(out/"selected-pure-projection-and-envelope-matrices.json.gz",mt))
  rec.update({"status":"completed","selectedPureSourceCount":nPure,"selectedNonpureSourceCount":nNonpure,
    "selectedPureProjectionRankOverQ":rJ,"selectedPureRelationDimension":nPure-rJ,
    "selectedOriginalConstantRankLowerBound":4318,"selectedOriginalConstantRankUpperBound":rankUpper,
    "selectedOriginalConstantRankExactly4318":exact,"selectedFullConstantKernelDimensionLowerBound":kLower,
    "selectedFirstConnectionUpperEnvelopeRank":cRank,"envelopeIsNotClaimedFullConnectionLowerBound":True,
    "selectedFirstLiftConstantDimensionLowerBound":sLower,
    "sameMinorInfinityOrderLowerBound":sLower+14,
    "replacementInfinityOrderLowerBound":sLower+13,"cofactorInfinityOrderLowerBound":sLower+12,
    "conditionalSourceCostUnderK67":8734-sLower,
    "all17Whole77CoefficientScalingsVerified":True,"allSelectedPureRelationIdentitiesVerified":True,
    "nonpureSourceIndependenceInferredFromCount":False,
    "nonpureImageEqualsWholeHProved":False})
  rec["parameters"].update({"binding":binding,"inputIdentity":material,
    "sameSelectedJExactly4354":True,"sameSelectedIExactly4354":True,
    "selectedPureSourceRows":[v[0] for v in chosen],"selectedPurePhysicalRowIndices":[v[4] for v in chosen],
    "originalOutputITransverseCount":{"pure":counts[0],"oneTransverse":counts[1],"atLeastTwoTransverse":counts[2]},
    "excludedOriginal13Outputs":excluded,"equationPermutationPhysicalToOriginal":perm,
    "primitiveOverPhysicalScales":[str(v) for v in scales],
    "matrixSHA256":{"P0":G.matrix_hash(P0),"P1":G.matrix_hash(P1),"Q":G.matrix_hash(Q),
      "P0J":G.matrix_hash(PJ),"P1J":G.matrix_hash(P1J),"selectedPureKernel":G.matrix_hash(U),"upperEnvelope":G.matrix_hash(C)}})
  code=0
 except BudgetExpired as e:rec.update(status="budget-exhausted",error=str(e));code=75
 except Exception as e:
  rec.update(status="failed",error=str(e),exceptionType=type(e).__name__);(out/"exception.log").write_text(traceback.format_exc());code=1
 finally:
  signal.setitimer(signal.ITIMER_REAL,0);rec["parameters"]["temporaryFiles"]=temps
  rec["mathematicalElapsedSeconds"]=time.monotonic()-start
  save(out/"selected-pure-projection-rank-and-envelope-receipt.json",rec)
 need((out/"selected-pure-projection-rank-and-envelope-receipt.json").stat().st_size<100000,"small result text")
 print(json.dumps(rec),flush=True);return code
if __name__=="__main__":sys.exit(main(sys.argv[1:]))
