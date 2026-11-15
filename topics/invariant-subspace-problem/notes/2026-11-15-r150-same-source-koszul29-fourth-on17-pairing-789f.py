#!/usr/bin/env python3
"""Same-source29 natural fourth forcing on exactly17 verified third cochains.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
Known incoming image13, full incoming15, complete third-head domain21.
Only new natural coefficient B4,17 original R4 columns and29 by75 pairing.
"""
import argparse,gzip,hashlib,io,itertools,json,math,os,pathlib,resource,signal,subprocess,sys,time,traceback
sys.dont_write_bytecode=True
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
os.environ["OPENBLAS_NUM_THREADS"]="1"
os.environ["OMP_NUM_THREADS"]="1"
class BudgetExpired(Exception):pass
def need(v,s):
 if not v:raise ValueError(s)
def identity(p):
 h=hashlib.sha256();n=0
 with pathlib.Path(p).open("rb") as f:
  while True:
   b=f.read(1048576)
   if not b:break
   n+=len(b);h.update(b)
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
  b=json.dumps(v,sort_keys=True,separators=(",",":")).encode()
  need(len(b)<100000,"small permanent metadata only");q.write_bytes(b)
 os.replace(q,p);return {"file":p.name,**identity(p),"temporaryOnly":True}
def vecsha(v):
 h=hashlib.sha256()
 for x in v:h.update((str(x)+"\n").encode())
 return h.hexdigest()
def pivots(R,rank):
 ans=[]
 for i in range(int(rank)):
  j=next((j for j in range(R.ncols()) if R[i,j]),None)
  need(j is not None and R[i,j]==1,"normalized rational RREF");ans.append(j)
 need(ans==sorted(set(ans)),"ordered actual pivot columns");return ans
def primitive_q(v):
 den=1
 for x in v:den=math.lcm(den,int(x.q))
 z=[int(x.p)*(den//int(x.q)) for x in v];g=0
 for x in z:g=math.gcd(g,abs(x))
 need(g>0,"nonzero rational vector")
 sg=-1 if next(x for x in z if x)<0 else 1
 return [sg*(x//g) for x in z]
def sparse_rows(x):
 return {int(i):[(int(j),int(v)) for j,v in row] for i,row in x}
def checked_inv(p):
 inv=read(p)
 need(identity(__file__)==inv["programIdentity"],"same third-pairing program on continuation")
 for k,v in inv["paths"].items():need(identity(v)==inv["inputIdentities"][k],"actual pinned input: "+k)
 return inv
def add_output(rec,p):
 z={"file":p.name,**identity(p),"temporaryOnly":True}
 rec["outputs"]=[a for a in rec["outputs"] if a["file"]!=p.name]+[z]
 return z
PINS={
 "old_unit":(9008513,"c53406d65cfd66f2f3b6f1c946bd7495e44c7041538c4f3c85518eb7be7d5dfe"),
 "consumer_products":(10890,"8a147b79e6f7a502aacc58fc07605c6754addf5d550295e838929955f5d1055f"),
 "through3":(40272,"795a0ae79597cdd55ace1ccc215aedc639e19100e1e2e1942fd30f99b373951a"),
 "primitive":(65159,"44350c49f9f60c61427b7278bf7f3d24b6cb2e6583848a113b03bb109516d4fe"),
 "old_pair":(112488,"b1b4c81c2e827fa92a375dfdc94d183604741badba3962de9e998add821946b1"),
 "old_pair_receipt":(15304,"11b0f10e9c0750b73644c425f91b48a249e5829a8dc7960e68e7713ef545f289"),
 "third_pair":(152226,"912a777573f261446f87fda25b71fe889963f31cb5a7f34dc192b42045a1af47"),
 "third_pair_receipt":(2365,"f25f2b7c8f3c2cba1999bf4bf9f96721038f29f78960834dbd2b6fb990de0415")}
PRIMITIVE_RAW_SHA="fa2e5d80e9fbd47e1e237ae60c548900a15922a0543e02be77fc972dc52944b3"
CONSUMER_BINDING="68b83b621a2219162ca36499757ab327cac7431f669e2fcc83e1de232affef50"
SECOND_BINDING="c40049455e9f310607586b55cc271ca00636dc954f0de63693d0da886a6d067e"
PAIR_BINDING="ea772f01fa0ab8a761287893c15a94f83ebc6326703b40b82a5846e02b020e39"
THIRD_BINDING="7aa59b81b9364f4e3a214b9f809af030000a524fbe7cf94b3bdf4606e9867a1f"
SOURCE_BINDING="2d9b068281400ec635fc2c912edf29e59d2bec1e3686bf6c3f6abd6ac01890f2"
def done_stage(p,bind):
 if not pathlib.Path(p).exists():return None
 r=read(p);need(r["binding"]==bind,"same actual fourth stage binding")
 if r["status"]!="completed":return None
 for z in r["outputs"]:
  need(identity(pathlib.Path(p).parent/z["file"])=={"bytes":z["bytes"],"sha256":z["sha256"]},"complete fourth stage bytes")
 return r
def forcing_worker(invpath,out):
 inv=checked_inv(invpath);p=inv["paths"];bind=inv["binding"];out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True)
 rp=out/"original-fourth-forcing-on17-receipt.json"
 if done_stage(rp,bind):print(json.dumps({"status":"completed","completeActualCacheReused":True}),flush=True);return 0
 st=time.monotonic();rec={"status":"running","phase":"original-natural-B4","binding":bind,"outputs":[],"parameters":{}}
 def ck():
  rec["elapsedSeconds"]=time.monotonic()-st;save(rp,rec)
 ck()
 paid=read(p["consumer_products"]);unit=read(p["old_unit"]);co=read(p["through3"])
 need(paid["binding"]==CONSUMER_BINDING and unit["binding"]==SECOND_BINDING and paid["status"]=="completed" and
 paid["actualExplicitThirdHeadDimension"]==17 and paid["completeGlobalThirdHeadDimension"]==21 and
 paid["allOriginalFourLayerProductsZero"] and paid["allActualHeadCoordinatesIndependent"] and
 paid["originalFourLayerProductCoordinates"]==296072 and not paid["all21CompleteThirdHeadsExplicit"],
 "actual17 complete original cochains and full21 existence, not a full21 explicit domain")
 need(co["binding"]==THIRD_BINDING and co["allNaturalDegreeRulesVerified"] and
 not co["coMovingSourceDerivativeTermDiscarded"],"same original natural previous coefficients")
 raw=gzip.decompress(pathlib.Path(p["primitive"]).read_bytes())
 need(hashlib.sha256(raw).hexdigest()==PRIMITIVE_RAW_SHA,"complete primitive original integer model")
 eqs=json.loads(raw)["equations"];need(len(eqs)==17 and all(len(v)==77 for v in eqs),"complete17 by77 coefficient model")
 Fs=[[] for _ in range(5)]
 for e,row in enumerate(eqs):
  rr=[[] for _ in range(5)]
  for j,pol in enumerate(row):
   v=list(map(int,pol));need(v,"nonempty original coefficient polynomial")
   if e>=11 and j<11:
    need(not any(v),"all Gamma linear coefficients exactly zero")
    for k in range(5):rr[k].append(0)
   else:
    d=10 if e<11 and j<11 else 0 if e<11 else 5
    need(not any(v[d+1:]),"same natural weighted primitive degree")
    for k in range(5):rr[k].append(v[d-k] if d>=k and d-k<len(v) else 0)
  for k in range(5):Fs[k].append(rr[k])
 for k,key in enumerate(["constant","naturalFirst","naturalSecond","naturalThird"]):
  need(Fs[k]==[list(map(int,v)) for v in co[key]],"every paid natural coefficient through3, "+key)
 J=list(map(int,unit["originalSourceRows"]));need(len(J)==len(set(J))==4354 and J==sorted(J),"same original selected J")
 mon=[(i,) for i in range(11)]+[(i,j) for i in range(11) for j in range(i,11)]
 mult=[q for d in range(4) for q in itertools.combinations_with_replacement(range(11),d)]
 whole=[q for d in range(5,0,-1) for q in itertools.combinations_with_replacement(range(11),d)]
 oi={v:i for i,v in enumerate(whole)};need(len(whole)==4367 and len(mult)*17==6188,"same complete original dictionaries")
 rows=[]
 for rawid in J:
  e=(rawid-1)%17;mu=mult[(rawid-1)//17];r=[]
  for j,m in enumerate(mon):
   c=[Fs[k][e][j] for k in range(1,5)]
   if any(c):r.append((oi[tuple(sorted(mu+m))],*c))
  rows.append(r)
 cf=out/"same-original-natural-through-fourth-coefficients.json.gz"
 save(cf,{"binding":bind,"originalPrimitiveIdentity":inv["inputIdentities"]["primitive"],
  "paidThrough3Identity":inv["inputIdentities"]["through3"],"constant":Fs[0],"naturalFirst":Fs[1],
  "naturalSecond":Fs[2],"naturalThird":Fs[3],"naturalFourth":Fs[4],
  "all5236PaidNaturalCoefficientIdentitiesVerified":True,"allNaturalDegreeRulesVerified":True,
  "coMovingSourceDerivativeTermDiscarded":False})
 add_output(rec,cf)
 table={z["file"]:z for z in paid["outputs"]};products=pathlib.Path(p["consumer_products"]).parent
 audits=[];forces=[]
 for j in range(17):
  ca=products/("complete-original-third-left-jet-%02d.json.gz"%j)
  ve=products/("verified-original-third-left-jet-%02d.json"%j)
  for fp in [ca,ve]:
   z=table[fp.name];need(identity(fp)=={"bytes":z["bytes"],"sha256":z["sha256"]},"actual paid candidate or verification bytes")
  cid=identity(ca);vid=identity(ve);candidate=read(ca);verified=read(ve)
  need(candidate["binding"]==verified["binding"]==CONSUMER_BINDING and
   candidate["column"]==verified["column"]==j and verified["candidateIdentity"]==cid and
   verified["all17416OriginalProductsZero"] and verified["fullOriginalCoChainProductCoordinates"]==17416 and
   verified["originalSourceRows"]==4354 and verified["completeCoChainLayers"]==4,
   "exact original four-layer products inherited only after matching actual bytes")
  layers=[list(map(int,v)) for v in candidate["primitiveOriginalLambdaLayers"]]
  hc=list(map(int,candidate["primitiveIntegerParameters"]["oldSecondFirstHeadCoefficients"]))
  need(len(layers)==4 and all(len(v)==4367 for v in layers) and len(hc)==33 and any(layers[0]),"all original integer source layers")
  fp=out/("original-fourth-forcing-%02d.json.gz"%j)
  if fp.exists():
   q=read(fp);need(q["binding"]==bind and q["candidateIdentity"]==cid and q["verifiedCandidateIdentity"]==vid and
    q["column"]==j and q["originalSourceRows"]==J,"same complete original fourth forcing")
   values=list(map(int,q["originalFourthForcingIntegerColumn"]))
  else:
   values=[]
   for row in rows:
    val=0
    for ix,f1,f2,f3,f4 in row:
     val+=f1*layers[3][ix]+f2*layers[2][ix]+f3*layers[1][ix]+f4*layers[0][ix]
    values.append(val)
   save(fp,{"format":"isp-original-fourth-forcing-paid17-third-head-v1","binding":bind,"column":j,
    "candidateIdentity":cid,"verifiedCandidateIdentity":vid,"originalSourceRows":J,
    "originalFourthForcingIntegerColumn":[str(v) for v in values],
    "oldFirst33HeadCoefficients":[str(v) for v in hc],
    "paidOriginalFourLayerProductsInheritedByExactHashes":True,"paidOriginalProductCoordinates":17416,
    "originalFourthForcingFormula":"B1^T*lambda3+B2^T*lambda2+B3^T*lambda1+B4^T*lambda0",
    "wholePrimitiveCoChainRetainedWithoutNewColumnScaling":True,
    "originalLambdaLayerSHA256":[vecsha(v) for v in layers],
    "originalFourthForcingSHA256":vecsha(values)})
  need(len(values)==4354,"all original4354 fourth forcing entries")
  z={"file":fp.name,**identity(fp)};forces.append(z);add_output(rec,fp)
  audits.append({"column":j,"candidateIdentity":cid,"verifiedCandidateIdentity":vid,
   "forcingIdentity":identity(fp),"maximumFourthForcingBits":max(abs(v).bit_length() for v in values),
   "originalFourthForcingSHA256":vecsha(values)})
  rec["completedOriginalFourthColumns"]=j+1;rec["parameters"]["verifiedInputCoChains"]=audits;ck()
 rec.update(status="completed",phase="complete",actualFourthForcingColumns=17,
  actualOriginalSourceRows=4354,originalFourthForcingCoordinates=4354*17,
  all17PaidFourLayerProductsInheritedByExactHashes=True,paidOriginalProductCoordinates=296072,
  completeGlobalThirdHeadDimension=21,missingExplicitThirdHeads=4,
  all5236PaidNaturalCoefficientIdentitiesVerified=True,originalFourLayerProductsRecomputed=False)
 rec["parameters"].update(forcingColumns=forces,completeNaturalCoefficientIdentity=identity(cf),
  originalNaturalSparseFourthTermsPerBundle=sum(len(v) for v in rows),
  previousFourLayerProductsReceiptIdentity=inv["inputIdentities"]["consumer_products"])
 ck();print(json.dumps({"status":"completed","fourthForcingColumns":17,"originalRows":4354}),flush=True);return 0
def pairing_worker(invpath,forcingdir,out):
 from flint import fmpz_mat,fmpq_mat,fmpq
 inv=checked_inv(invpath);p=inv["paths"];bind=inv["binding"];out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True)
 rp=out/"same-source29-fourth-on17-worker-receipt.json"
 if done_stage(rp,bind):print(json.dumps({"status":"completed","completeActualCacheReused":True}),flush=True);return 0
 st=time.monotonic();rec={"status":"running","phase":"same29-and-known-incoming13","binding":bind,"outputs":[],"parameters":{}}
 def ck():
  rec["elapsedSeconds"]=time.monotonic()-st;save(rp,rec)
 ck()
 op=read(p["old_pair"]);opr=read(p["old_pair_receipt"]);tp=read(p["third_pair"]);tpr=read(p["third_pair_receipt"])
 unit=read(p["old_unit"]);J=list(map(int,unit["originalSourceRows"]))
 need(op["binding"]==opr["binding"]==PAIR_BINDING and opr["status"]=="completed" and
  opr["pairingRankOverQ"]==5 and opr["firstThreeHFPairingRankOverQ"]==1 and
  opr["completeFree36ImageRankOverQ"]==29 and opr["all29FullOriginal4367ProductsZero"] and
  opr["all1309ConstantCoefficientsExactlyMatched"] and
  opr["parameters"]["sourceBinding"]==SOURCE_BINDING,"same exact29 source basis and actual old pairing")
 need(op["oldUnitIdentity"]==inv["inputIdentities"]["old_unit"] and op["originalSourceRows"]==J,"same source coordinates and unscaled rows")
 need(tp["binding"]==tpr["binding"]==THIRD_BINDING and tpr["status"]=="completed" and
  tpr["completeCombined29By58PairingRank"]==6 and tpr["fullSelectedThirdRankExactly3"] and
  tpr["restricted22ThirdConnectionRankOverQ"]==1 and tpr["fullThirdHeadSpaceDimension"]==21 and
  tp["oldPairIdentity"]==inv["inputIdentities"]["old_pair"],"same paid third rank and complete21 head existence")
 oldrows=[list(map(int,v)) for v in tp["integerRows"]]
 need(len(oldrows)==29 and all(len(v)==58 for v in oldrows) and
  [v[:36] for v in oldrows]==[list(map(int,v)) for v in op["integerRows"]],"unchanged old58 column block and source order")
 audits=opr["parameters"]["verifiedSourceColumns"];need(len(audits)==29 and op["sourceAudits"]==audits,"same29 exact source audit order")
 sources=[];sd=pathlib.Path(inv["supportDirectory"])
 for j,a in enumerate(audits):
  z=a["certificate"];fp=sd/z["file"]
  need(identity(fp)=={"bytes":z["bytes"],"sha256":z["sha256"]},"actual source29 certificate bytes")
  q=read(fp);v=list(map(int,q["original6188IntegerCoefficients"]))
  need(q["binding"]==SOURCE_BINDING and q["column"]==j and len(v)==6188 and
   q["all1834OutsideSourceCoefficientsZero"] and q["all4367ExactIntegerProductsZero"] and
   vecsha(v)==a["sourceSHA256"],"same whole original source and full product identity")
  sources.append([v[i-1] for i in J])
 fd=pathlib.Path(forcingdir);fr=read(fd/"original-fourth-forcing-on17-receipt.json")
 need(fr["binding"]==bind and fr["status"]=="completed" and fr["actualFourthForcingColumns"]==17 and
  fr["all17PaidFourLayerProductsInheritedByExactHashes"],"complete actual17 forcing before pairing")
 forces=[];heads33=[]
 for j,z in enumerate(fr["parameters"]["forcingColumns"]):
  fp=fd/z["file"];need(identity(fp)=={"bytes":z["bytes"],"sha256":z["sha256"]},"complete actual R4 bytes")
  q=read(fp);v=list(map(int,q["originalFourthForcingIntegerColumn"]));h=list(map(int,q["oldFirst33HeadCoefficients"]))
  need(q["binding"]==bind and q["column"]==j and q["originalSourceRows"]==J and len(v)==4354 and
   len(h)==33 and q["paidOriginalFourLayerProductsInheritedByExactHashes"],"complete actual forcing coordinates")
  forces.append(v);heads33.append(h)
 need(len(forces)==17,"exact17 actual third sources")
 need(int(fmpq_mat(33,17,[heads33[j][i] for i in range(33) for j in range(17)]).rank())==17,
  "actual17 original heads remain independent")
 mp=out/"actual-same-source29-by75-fourth-on17-pairing.json.gz"
 if mp.exists():
  q=read(mp);need(q["binding"]==bind and q["paidThirdPairIdentity"]==inv["inputIdentities"]["third_pair"] and
   q["forcingReceiptIdentity"]==identity(fd/"original-fourth-forcing-on17-receipt.json"),"same complete saved fourth pairing")
  rows=[list(map(int,v)) for v in q["integerRows"]]
 else:
  K=fmpz_mat(29,4354,[v for c in sources for v in c])
  F=fmpz_mat(4354,17,[forces[j][i] for i in range(4354) for j in range(17)])
  Z=K*F;rows=[oldrows[i]+[int(Z[i,j]) for j in range(17)] for i in range(29)]
  save(mp,{"format":"isp-same-source29-fourth-on17-pairing-v1","binding":bind,"rows":29,"columns":75,
   "paidThirdPairIdentity":inv["inputIdentities"]["third_pair"],
   "forcingReceiptIdentity":identity(fd/"original-fourth-forcing-on17-receipt.json"),
   "integerRows":[[str(v) for v in c] for c in rows],
   "columnOrder":"oldHF3,oldT33,paidR3_on22,newR4_on17",
   "sameOriginalSourceBasisRetained":True,"originalRowsNotDividedByUnitContents":True})
  del K,F,Z
 add_output(rec,mp);rec["phase"]="exact17-domain-rank-in-known23-dimensional-quotient";ck()
 need(len(rows)==29 and all(len(v)==75 for v in rows) and [v[:58] for v in rows]==oldrows,"unchanged old58 pair block")
 rd=[]
 for row in rows:
  g=0
  for v in row:g=math.gcd(g,abs(v))
  rd.append(g or 1)
 A=[[v//rd[i] for v in row] for i,row in enumerate(rows)]
 cd=[]
 for j in range(75):
  g=0
  for i in range(29):g=math.gcd(g,abs(A[i][j]))
  cd.append(g or 1)
 N=[[A[i][j]//cd[j] for j in range(75)] for i in range(29)]
 M=fmpq_mat(N);RR,rk=M.rref();rk=int(rk);pv=pivots(RR,rk)
 oldrank=int(fmpq_mat([v[:58] for v in N]).rank())
 need(oldrank==6,"actual unchanged known incoming pairing rank6")
 r=rk-6;need(0<=r<=17,"actual fourth raw rank on17 heads")
 null=[]
 for j in range(75):
  if j in pv:continue
  v=[fmpq(0) for _ in range(75)];v[j]=fmpq(1)
  for i,k in enumerate(pv):v[k]=-RR[i,j]
  null.append(primitive_q([v[k]/cd[k] for k in range(75)]))
 Z=fmpq_mat(75,len(null),[null[j][i] for i in range(75) for j in range(len(null))])
 need(all(not v for v in (fmpq_mat(rows)*Z).entries()),"all original75-coordinate paired kernel products")
 P=fmpq_mat(17,len(null),[null[j][58+i] for i in range(17) for j in range(len(null))])
 PR,hr=P.transpose().rref();hr=int(hr);need(hr==17-r,"complete projection to actual17 domain")
 hpcols=[primitive_q([PR[i,j] for j in range(17)]) for i in range(hr)]
 hp=out/"complete-fourth-pairing-kernel-and17-head-projection.json.gz"
 save(hp,{"binding":bind,"pairingIdentity":identity(mp),"completeCombinedPairingRank":rk,
  "restricted17FourthRankModuloKnownIncoming13":r,
  "primitiveOriginal75KernelColumns":[[str(v) for v in c] for c in null],
  "complete17HeadProjectionColumns":[[str(v) for v in c] for c in hpcols],
  "headProjectionRank":hr,"headCoordinatesReferToActualPrimitiveFourLayerSources":True,
  "rowGCDs":[str(v) for v in rd],"columnGCDs":[str(v) for v in cd],
  "nonzeroNormalizedRREFRows":[[str(RR[i,j]) for j in range(75)] for i in range(rk)],
  "allOriginal75PairingKernelProductsZero":True,
  "fourthHeadExistenceFromKnownQuotientOnly":True,"explicitLambda4SourcesConstructed":False})
 add_output(rec,hp)
 lo=max(3,r-2);hi=r+4;need(0<=lo<=hi<=21,"full21 domain and two missing incoming directions")
 order=114+hr;cof=110+max(hr-1,0)
 rec.update(status="completed",phase="complete",outcome="restricted17-fourth-image-and-full-rank-interval",
  knownIncomingPairingRank=6,completeCombined29By75PairingRank=rk,
  restricted17FourthRankModuloKnownIncoming13=r,completeRestricted17RawFourthImageComputed=True,
  completeGlobalThirdHeadDimension=21,actualExplicitThirdHeadDimension=17,missingExplicitThirdHeads=4,
  knownFourthIncomingImageDimension=13,completeFourthIncomingImageDimension=15,missingIncomingImageDirections=2,
  fullSelectedFourthRankOverQLowerBound=lo,fullSelectedFourthRankOverQUpperBound=hi,
  fullSelectedFourthRankExactlyKnown=lo==hi,provedFourthHeadDimensionLowerBound=hr,
  allOriginal75PairingKernelProductsZero=True,all17ActualHeadsIndependent=True,
  selectedMinorInfinityOrderOverQLowerBound=order,selectedCofactorInfinityOrderOverQLowerBound=cof,
  selectedOriginalSourceReplacementOrderOverQLowerBound=cof,
  explicitLambda4SourcesConstructed=False,completeFourthIncomingImageComputed=False,
  all21CompleteThirdHeadsExplicit=False,newM0RightHandSidesSolved=0,leadingUnitProved=False)
 rec["parameters"].update(knownQuotientIsomorphism="E/W13 -> K29*/pi(W13), dimensions23; ker pi subset W12 subset W13",
  currentTrueDomainDimension=17,completeDomainDimension=21,domainCodimension=4,incomingCodimension=2,
  intervalFormula="[max(3,r-2),r+4]",rankZeroOnRestrictedDomainIsAllowed=True,
  nextFpLowerBoundReason="same Q/F31 ranks4318 and connection ranks3,9,3 already proved; fourth F31 rank3",
  selectedQThresholdCountsLowerBounds=[36,33,24,21,hr],pairedPivotColumns=pv,
  paidThirdPairIdentity=inv["inputIdentities"]["third_pair"],actualFourthPairIdentity=identity(mp),
  actualHeadProjectionIdentity=identity(hp),conditionalCostRecalculationDeferredToCurrentPublishedFactor=True)
 ck();print(json.dumps({"status":"completed","outcome":rec["outcome"],"restrictedRawRank":r,
  "fullFourthRankInterval":[lo,hi],"provedFourthHeads":hr}),flush=True);return 0
def main(argv):
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ["consumer-out","second-out","pairing-out","third-out","primitive-equations","out"]:
  ap.add_argument("--"+k,required=True,type=pathlib.Path)
 ap.add_argument("--seconds",type=float,default=120);ap.add_argument("--memory-mib",type=int,default=2048)
 a=ap.parse_args(argv);need(math.isfinite(a.seconds) and 0<a.seconds<=300,"finite shared fourth budget at most300")
 need(0<a.memory_mib<=4096,"memory at most4096MiB per process")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 st=time.monotonic();deadline=st+a.seconds-min(5,a.seconds/10);out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 rec={"format":"isp-same-source29-fourth-on17-pipeline-v1","status":"running","phase":"inputs",
  "events":[],"parameters":{},"largeDataUploadedOrCommitted":False,"newM0RightHandSidesSolved":0,
  "normalFiveEliminationContinued":False,"oldQSourceKernelsRebuilt":False,
  "explicitLambda4SourcesConstructed":False,"completeFourthIncomingImageComputed":False,
  "all21CompleteThirdHeadsExplicit":False,"leadingUnitProved":False}
 code=1
 def ck():
  rec["mathematicalElapsedSeconds"]=time.monotonic()-st;save(out/"same-source-koszul29-fourth-on17-pairing-receipt.json",rec)
 def run_stage(name,cmd,rp):
  rem=deadline-time.monotonic()
  if rem<=0:raise BudgetExpired("shared original fourth deadline")
  t=time.monotonic()
  with (out/(name+".log")).open("a",encoding="utf-8") as log:
   pr=subprocess.Popen(cmd,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
   try:pr.wait(timeout=rem)
   except subprocess.TimeoutExpired:
    os.killpg(pr.pid,signal.SIGTERM)
    try:pr.wait(timeout=2)
    except subprocess.TimeoutExpired:os.killpg(pr.pid,signal.SIGKILL);pr.wait()
    rec["events"].append({"stage":name,"exitCode":pr.returncode,"elapsedSeconds":time.monotonic()-t,"sharedDeadlineReached":True})
    raise BudgetExpired("actual completed fourth arrays retained: "+name)
  rec["events"].append({"stage":name,"exitCode":pr.returncode,"elapsedSeconds":time.monotonic()-t})
  q=read(rp) if rp.exists() else {}
  rec["parameters"][name+"ActualStatus"]=q.get("status");ck()
  need(pr.returncode==0 and q.get("status")=="completed","actual complete stage required: "+name)
  return q
 try:
  paths={"old_unit":a.second_out/"prepared"/"second-left-m0-unit-input.json.gz",
   "consumer_products":a.consumer_out/"original-products"/"third21-complete-original-four-layer-products-receipt.json",
   "through3":a.third_out/"original-forcing"/"same-original-natural-through-third-coefficients.json.gz",
   "primitive":a.primitive_equations,
   "old_pair":a.pairing_out/"pairing"/"actual-koszul29-by36-original-forcing-pairing.json.gz",
   "old_pair_receipt":a.pairing_out/"pairing"/"same-source-koszul29-pairing-worker-receipt.json",
   "third_pair":a.third_out/"pairing"/"actual-same-source29-by58-third-pairing.json.gz",
   "third_pair_receipt":a.third_out/"pairing"/"same-source29-third-quotient-worker-receipt.json"}
  ids={k:identity(v) for k,v in paths.items()}
  for k,(n,s) in PINS.items():need(ids[k]=={"bytes":n,"sha256":s},"actual fixed fourth input "+k)
  material={"programIdentity":identity(__file__),"inputIdentities":ids,"actualThirdHeads":17,
   "completeThirdHeadDimension":21,"knownIncomingDimension":13,"fullIncomingDimension":15,
   "naturalChart":"same original infinity u=1/s"}
  bind=hashlib.sha256(json.dumps(material,sort_keys=True,separators=(",",":")).encode()).hexdigest()
  ip=out/"invocation.json"
  if ip.exists():need(read(ip)["binding"]==bind,"same exact fourth semantic binding")
  save(ip,{**material,"binding":bind,"paths":{k:str(v.resolve()) for k,v in paths.items()},
   "supportDirectory":str((a.pairing_out/"reconstructed-source29").resolve())})
  rec["parameters"].update(material);rec["parameters"].update(binding=bind,secondsLimit=a.seconds,memoryMiBPerProcess=a.memory_mib)
  ck();fd=out/"original-forcing";pd=out/"pairing"
  for name,mode,folder,rname in [
   ("original-fourth-forcing","--forcing-worker",fd,"original-fourth-forcing-on17-receipt.json"),
   ("same-source29-fourth-on17","--pairing-worker",pd,"same-source29-fourth-on17-worker-receipt.json")]:
   rec["phase"]=name;ck();rp=folder/rname;q=done_stage(rp,bind)
   if q:rec["events"].append({"stage":name,"completeActualCacheReused":True})
   else:
    cmd=[sys.executable,"-B",str(pathlib.Path(__file__).resolve()),mode,str(ip)]
    if mode=="--pairing-worker":cmd.append(str(fd))
    cmd.append(str(folder));q=run_stage(name,cmd,rp)
   rec["parameters"][name+"ReceiptIdentity"]=identity(rp)
   rec["parameters"][name+"ActualTemporaryOutputs"]=q["outputs"]
   if mode=="--forcing-worker":
    for k in ["actualFourthForcingColumns","originalFourthForcingCoordinates","all17PaidFourLayerProductsInheritedByExactHashes",
     "paidOriginalProductCoordinates","all5236PaidNaturalCoefficientIdentitiesVerified","originalFourLayerProductsRecomputed"]:
     rec[k]=q[k]
   else:
    for k,v in q.items():
     if k not in ["parameters","outputs","binding","elapsedSeconds","status","phase"]:rec[k]=v
    rec["parameters"]["actualFourthConclusion"]=q["parameters"]
  rec.update(status="completed",phase="complete");code=0
 except (BudgetExpired,subprocess.TimeoutExpired) as e:
  rec.update(status="completed-prefix",error=str(e));code=75
 except Exception as e:
  rec.update(status="failed",error=str(e),exceptionType=type(e).__name__)
  (out/"exception.log").write_text(traceback.format_exc(),encoding="utf-8");code=1
 finally:ck()
 print(json.dumps(rec),flush=True);return code
if __name__=="__main__":
 if len(sys.argv)>1 and sys.argv[1]=="--forcing-worker":
  sys.exit(forcing_worker(pathlib.Path(sys.argv[2]),pathlib.Path(sys.argv[3])))
 if len(sys.argv)>1 and sys.argv[1]=="--pairing-worker":
  sys.exit(pairing_worker(pathlib.Path(sys.argv[2]),pathlib.Path(sys.argv[3]),pathlib.Path(sys.argv[4])))
 sys.exit(main(sys.argv[1:]))
