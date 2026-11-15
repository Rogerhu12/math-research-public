#!/usr/bin/env python3
"""Prepare the complete21 third-head RHS and test the paid old zero rows.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
No M0 solve, no high elimination, no new rank prime. Large data temporary only.
"""
import argparse,gzip,hashlib,io,json,math,os,pathlib,resource,sys,time,traceback
sys.dont_write_bytecode=True
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
os.environ["OPENBLAS_NUM_THREADS"]="1";os.environ["OMP_NUM_THREADS"]="1"
class BudgetExpired(Exception):pass
def need(v,m):
 if not v:raise ValueError(m)
def ident(p):
 h=hashlib.sha256();n=0
 with pathlib.Path(p).open("rb") as f:
  while True:
   b=f.read(1048576)
   if not b:break
   h.update(b);n+=len(b)
 return {"bytes":n,"sha256":h.hexdigest()}
def read(p):
 p=pathlib.Path(p)
 with (gzip.open(p,"rt",encoding="utf-8") if p.suffix==".gz" else p.open("r",encoding="utf-8")) as f:return json.load(f)
def save(p,v):
 p=pathlib.Path(p);p.parent.mkdir(parents=True,exist_ok=True);q=p.with_name(p.name+".tmp")
 if p.suffix==".gz":
  with q.open("wb") as raw:
   with gzip.GzipFile(fileobj=raw,mode="wb",mtime=0,compresslevel=1) as gz:
    with io.TextIOWrapper(gz,encoding="utf-8",newline="\n") as f:json.dump(v,f,sort_keys=True,separators=(",",":"))
 else:
  b=json.dumps(v,sort_keys=True,separators=(",",":")).encode();need(len(b)<100000,"small metadata only");q.write_bytes(b)
 os.replace(q,p);return {"file":p.name,**ident(p),"temporaryOnly":True}
def vhash(v):
 h=hashlib.sha256()
 for x in v:h.update((str(x)+"\n").encode())
 return h.hexdigest()
def primitive(v):
 d=1
 for x in v:d=math.lcm(d,int(x.q))
 z=[int(x.p)*(d//int(x.q)) for x in v];g=0
 for x in z:g=math.gcd(g,abs(x))
 need(g>0,"nonzero kernel vector")
 sg=-1 if next(x for x in z if x)<0 else 1
 return [sg*(x//g) for x in z]
PINS={
 "unit":(9008513,"c53406d65cfd66f2f3b6f1c946bd7495e44c7041538c4f3c85518eb7be7d5dfe"),
 "third":(11769,"954f135c5eab26021fab59aaafd8bd998a232dd2ec02ddcd3204866b93e52ab7"),
 "forcing_receipt":(22412,"59f44ff409f56e420db91f0640b8a6f605e6fbcbf88d7b493f21184741ce5245"),
 "projection":(45993,"c8e25e15ec3f07e887974adaeff2c573a6391335859bed896a3ca2a6b7af5ae6"),
 "pairing":(152226,"912a777573f261446f87fda25b71fe889963f31cb5a7f34dc192b42045a1af47")}
THIRD_BINDING="7aa59b81b9364f4e3a214b9f809af030000a524fbe7cf94b3bdf4606e9867a1f"
OLD_BINDING="c40049455e9f310607586b55cc271ca00636dc954f0de63693d0da886a6d067e"
def main():
 from flint import fmpq,fmpq_mat,fmpz_mat
 p=argparse.ArgumentParser(description=__doc__)
 for key in ["regauged-out","third-out","out"]:p.add_argument("--"+key,required=True,type=pathlib.Path)
 p.add_argument("--seconds",type=float,default=30);p.add_argument("--memory-mib",type=int,default=2048)
 a=p.parse_args();need(math.isfinite(a.seconds) and 0<a.seconds<=120,"finite shared budget at most120 seconds")
 need(0<a.memory_mib<=2048,"at most2048MiB per process")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 start=time.monotonic();deadline=start+a.seconds;out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 receipt=out/"third21-original-forcing-support-and-unit-preparation-receipt.json"
 r={"status":"running","phase":"actual-paid-inputs","events":[],"parameters":{},"outputs":[],
 "newM0RightHandSidesSolved":0,"newHighEliminationPerformed":False,"largeDataUploadedOrCommitted":False,
 "explicitNewLambda3SourcesConstructed":False,"completeThirdHeadDimension":21}
 def ck():
  r["mathematicalElapsedSeconds"]=time.monotonic()-start;save(receipt,r)
 def check():
  if time.monotonic()>=deadline:raise BudgetExpired("shared preparation clock; actual completed arrays retained")
 code=1
 try:
  paths={"unit":a.regauged_out/"prepared"/"second-left-m0-unit-input.json.gz",
   "third":a.third_out/"same-source-koszul29-third-pairing-receipt.json",
   "forcing_receipt":a.third_out/"original-forcing"/"original-third-forcing-on22-receipt.json",
   "projection":a.third_out/"pairing"/"complete-third-pairing-kernel-and22-head-projection.json.gz",
   "pairing":a.third_out/"pairing"/"actual-same-source29-by58-third-pairing.json.gz"}
  ids={}
  for k,z in paths.items():
   ids[k]=ident(z);need(ids[k]=={"bytes":PINS[k][0],"sha256":PINS[k][1]},"actual fixed input "+k)
  mat={"programIdentity":ident(__file__),"inputIdentities":ids,"headCount":21,"oldCorrectionColumns":1546,
   "originalSourceRows":4354,"oldZeroRows":1736}
  binding=hashlib.sha256(json.dumps(mat,sort_keys=True,separators=(",",":")).encode()).hexdigest()
  ip=out/"invocation.json"
  if ip.exists():need(read(ip)["binding"]==binding,"same actual preparation binding")
  save(ip,{**mat,"binding":binding,"paths":{k:str(z.resolve()) for k,z in paths.items()}})
  r["parameters"].update(mat);r["parameters"].update(binding=binding,secondsLimit=a.seconds,memoryMiBPerProcess=a.memory_mib)
  ck();check()
  u=read(paths["unit"]);tr=read(paths["third"]);fr=read(paths["forcing_receipt"])
  z=read(paths["projection"]);pa=read(paths["pairing"])
  need(u["binding"]==OLD_BINDING and tr["parameters"]["binding"]==THIRD_BINDING and
   tr["status"]=="completed" and tr["fullSelectedThirdRankExactly3"] and
   tr["all287364LowerOriginalProductsZero"] and tr["completePaired22HeadProjectionDimension"]==21,
   "actual complete third result and actual21 heads")
  need(z["binding"]==pa["binding"]==fr["binding"]==THIRD_BINDING and
   z["pairingIdentity"]==ids["pairing"] and z["headProjectionRank"]==21 and z["restrictedThirdRank"]==1 and
   fr["status"]=="completed" and fr["all287364LowerOriginalProductsZero"],
   "complete same binding cochain and projected head data")
  J=list(map(int,u["originalSourceRows"]));need(len(J)==len(set(J))==4354 and J==sorted(J),"same original J")
  M0=[[(int(j),int(v)) for j,v in row] for row in u["originalCorrectionRows"]]
  zero=list(map(int,u["oldZeroRowPositions"]))
  need(len(M0)==4354 and len(zero)==1736 and zero==[i for i,row in enumerate(M0) if not row],
   "all actual zero rows of complete old M0")
  need(all(not any(int(v) for v in u["originalRightHandSideRows"][i]) for i in zero),
   "all complete old HF/T forcing rows zero on old high rows")
  Z=[[int(v) for v in c] for c in z["complete22HeadProjectionColumns"]]
  need(len(Z)==21 and all(len(c)==22 for c in Z),"complete saved22 by21 head coordinates")
  zm=fmpz_mat(22,21,[Z[j][i] for i in range(22) for j in range(21)])
  need(int(fmpq_mat(zm).rank())==21,"actual full21 independent head coordinates")
  pair=[list(map(int,row)) for row in pa["integerRows"]]
  need(len(pair)==29 and all(len(row)==58 for row in pair),"complete actual third pairing")
  paidr=fmpz_mat(29,22,[pair[i][36+j] for i in range(29) for j in range(22)])*zm
  small=fmpq_mat(29,57,[pair[i][j] if j<36 else int(paidr[i,j-36]) for i in range(29) for j in range(57)])
  need(int(small.rank())==5,"all21 combinations lie in the complete third quotient kernel")
  r["phase"]="complete21-original-forcing";ck();check()
  columns=[];audits=[]
  for j,q in enumerate(fr["parameters"]["forcingColumns"]):
   fp=a.third_out/"original-forcing"/q["file"];need(ident(fp)=={"bytes":q["bytes"],"sha256":q["sha256"]},"paid forcing bytes")
   c=read(fp);v=list(map(int,c["originalThirdForcingIntegerColumn"]))
   need(c["binding"]==THIRD_BINDING and c["column"]==j and c["originalSourceRows"]==J and
    len(v)==4354 and c["allThreeLowerOriginalProductsZero"],"complete original forcing and lower products")
   columns.append(v);audits.append({"column":j,"inputIdentity":ident(fp),
    "oldPrimitiveCoChainCommonDivisor":c["primitiveCoChainCommonDivisor"]})
   check()
  need(len(columns)==22,"all22 actual forcing columns")
  fp=out/"complete-third21-original-right-hand-sides.json.gz"
  if fp.exists():
   rhs=read(fp);need(rhs["binding"]==binding and rhs["headProjectionIdentity"]==ids["projection"] and
    rhs["forcingInputAudit"]==audits,"same completed original21 RHS")
   Q=[[int(v) for v in c] for c in rhs["primitiveIntegerRightHandSideColumns"]]
   divisors=[int(v) for v in rhs["rightHandSideCommonDivisors"]]
  else:
   F=fmpz_mat(4354,22,[columns[j][i] for i in range(4354) for j in range(22)])
   U=F*zm;Q=[];divisors=[]
   for j in range(21):
    v=[int(U[i,j]) for i in range(4354)];g=0
    for x in v:g=math.gcd(g,abs(x))
    if not g:g=1
    Q.append([x//g for x in v]);divisors.append(g)
   rhs={"binding":binding,"originalSourceRows":J,"headProjectionIdentity":ids["projection"],
    "forcingReceiptIdentity":ids["forcing_receipt"],"forcingInputAudit":audits,
    "headCoordinatesInPrimitiveOld22":[[str(v) for v in c] for c in Z],
    "rightHandSideCommonDivisors":[str(v) for v in divisors],
    "primitiveIntegerRightHandSideColumns":[[str(v) for v in c] for c in Q],
    "preciseTargetFormula":"rhs_j=(R3*Z_j)/g_j; the complete lower cochain is (L0,L1,L2)*Z_j/g_j",
    "headScalingAppliedToAllLowerCoChainLayers":True,"all21HeadCombinationsThirdCompatible":True}
   save(fp,rhs);del F,U
  need(len(Q)==len(divisors)==21 and all(len(v)==4354 for v in Q) and all(d>0 for d in divisors),
   "all21 actual full original RHS columns")
  r["outputs"]=[{"file":fp.name,**ident(fp),"temporaryOnly":True}]
  r["parameters"]["rightHandSideIdentity"]=ident(fp)
  r["parameters"]["rightHandSideCommonDivisorBits"]=[v.bit_length() for v in divisors]
  r["parameters"]["maximumRightHandSideBits"]=[max(abs(v).bit_length() for v in c) for c in Q]
  r["parameters"]["originalRightHandSideSHA256ByColumn"]=[vhash(c) for c in Q]
  check();r["phase"]="actual-old1736-zero-row-gate";ck()
  nonzero=[j for j,c in enumerate(Q) if any(c[i] for i in zero)]
  high_nnz=sum(bool(c[i]) for c in Q for i in zero)
  hkernel=out/"complete-third21-high-forcing-kernel.json.gz"
  if not nonzero:
   rank=0;nullcols=[[int(i==j) for i in range(21)] for j in range(21)]
  else:
   H=fmpq_mat(1736,21,[Q[j][i] for i in zero for j in range(21)])
   HR,rank=H.rref();rank=int(rank)
   piv=[]
   for i in range(rank):
    j=next(j for j in range(21) if HR[i,j]);need(HR[i,j]==1,"actual high RREF pivot");piv.append(j)
   need(piv==sorted(set(piv)),"actual high pivot order")
   nullcols=[]
   for j in range(21):
    if j in piv:continue
    v=[fmpq(0) for _ in range(21)];v[j]=fmpq(1)
    for i,k in enumerate(piv):v[k]=-HR[i,j]
    nullcols.append(primitive(v))
   if nullcols:
    NN=fmpq_mat(21,len(nullcols),[nullcols[j][i] for i in range(21) for j in range(len(nullcols))])
    need(all(not v for v in (H*NN).entries()),"all actual high kernel products")
   del H,HR
  save(hkernel,{"binding":binding,"rightHandSideIdentity":ident(fp),"highOriginalRowPositions":zero,
   "highOriginalSourceRows":[J[i] for i in zero],"highRankOverQ":rank,
   "primitiveIntegerHighKernelColumns":[[str(v) for v in c] for c in nullcols],
   "allOriginalHighKernelProductsZero":True,"headCoordinatesReferToScaled21RightHandSides":True,
   "thisHighKernelIsNotAFullLambda3ExistenceTest":True})
  r["outputs"].append({"file":hkernel.name,**ident(hkernel),"temporaryOnly":True})
  r.update(all21OriginalRightHandSidesConstructed=True,all21CompleteHeadCoordinatesIndependent=True,
   all21ThirdCompatibleHeadCombinationsVerified=True,old1736RowsActuallyZeroForM0AndOldForcing=True,
   highForcingRankOverQ=rank,highForcingKernelDimension=21-rank,
   all21ForcingsVanishOnOld1736ZeroRows=not nonzero,newUnitRightHandSidesPrepared=0)
  r["parameters"].update(nonzeroHighForcingColumns=nonzero,highForcingNonzeroEntries=high_nnz,
   highKernelIdentity=ident(hkernel),zeroOriginalRows=1736,
   completeThirdHeadsGlobalExistenceStillTrue=True,oldM0UnitNotRecomputed=True)
  check()
  if not nonzero:
   up=out/"third21-left-m0-unit-input.json.gz"
   new={**u,"binding":binding,"format":"isp-selected-second-left-unit-input-v1","rhsColumns":21,
    "originalRightHandSideRows":[[str(Q[j][i]) for j in range(21)] for i in range(4354)],
    "forcingIdentity":ident(fp),"previousUnitInputIdentity":ids["unit"],
    "old36RightHandSidesRecomputed":False,"originalRightHandSideRowsUnchanged":False,
    "secondFamilyFormula":"third-step particular: M0_new*x+(R3*Z_j)/g_j=0 on original unit rows; complete4354 residual still required",
    "actualTargetRole":"21 complete third heads; fixed particular low cochain may still need HF/T compensation",
    "actualThirdHeadCoordinateCount":21,"all21ActualHighForcingRowsZero":True}
   need(new["originalCorrectionRows"]==u["originalCorrectionRows"] and
    new["selectedUnitRowIndices"]==u["selectedUnitRowIndices"] and
    new["rowCoefficientContents"]==u["rowCoefficientContents"],"unchanged complete paid exact unit matrix and scale")
   save(up,new);r["outputs"].append({"file":up.name,**ident(up),"temporaryOnly":True})
   r["newUnitRightHandSidesPrepared"]=21;r["parameters"]["preparedUnitInputIdentity"]=ident(up)
   outcome="all21-high-rows-zero-old-unit-input-prepared"
  else:outcome="actual-high-forcing-retained-new-correction-required"
  r.update(status="completed",phase="complete",outcome=outcome);code=0
 except BudgetExpired as e:
  r.update(status="completed-prefix",error=str(e));code=75
 except Exception as e:
  r.update(status="failed",error=str(e),exceptionType=type(e).__name__)
  (out/"exception.log").write_text(traceback.format_exc(),encoding="utf-8");code=1
 finally:ck()
 print(json.dumps(r),flush=True);return code
if __name__=="__main__":sys.exit(main())
