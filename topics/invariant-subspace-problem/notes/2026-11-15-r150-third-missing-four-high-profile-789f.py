#!/usr/bin/env python3
"""Exact missing-four preparation: original H45 profile and paid29 high-support dependencies.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
Reuse the actual786-pivot high preparation; no pivot or source solve is repeated.
Keep four genuine quotient right sides and every uncomputed high homogeneous freedom.
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
 "high_pair":(1019818,"d2ae353a064704e8d721d1663a6e838f93195438d004d2662386a8d34dd56024"),
 "old_h5_profile":(5489,"c4e504e9ad006aa6b44572c888d26602662f9efde7a040dd43c0a9e446c878f1"),
 "source_receipt":(15304,"11b0f10e9c0750b73644c425f91b48a249e5829a8dc7960e68e7713ef545f289"),
 "head_kernel":(2138,"4a27a932d31814078ee0b70c0e55878aade1f1c37772f5c41025bf69b1d8a322"),
 "residual":(65222,"7835f183e25640397796706042038d94fe46725b59a1918349747addc3c56e05"),
 "span_profile":(66597,"9b4815f10fc1fef3194f2ec24c95be2c7868a08b72570390ba6c5effd8ae1417"),
 "span_solution":(98953,"d81da8a51c570556ad98eabea5bb131d3cf9b91825a19ad6c93f3992b36316af")}
HIGH_BINDING="eff732ce44d956078f54b08550801cecf96aed1f1ce9d517cd3bfd0c45698b2b"
SOURCE_BINDING="2d9b068281400ec635fc2c912edf29e59d2bec1e3686bf6c3f6abd6ac01890f2"
PAIR_BINDING="ea772f01fa0ab8a761287893c15a94f83ebc6326703b40b82a5846e02b020e39"
CONSUMER_BINDING="68b83b621a2219162ca36499757ab327cac7431f669e2fcc83e1de232affef50"
STOP=False
def sigstop(signum,frame):
 global STOP
 STOP=True
def main(argv):
 from flint import fmpq,fmpq_mat,nmod_mat
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ["normal5-out","pairing-out","second-out","consumer-out","out"]:
  ap.add_argument("--"+k,required=True,type=pathlib.Path)
 ap.add_argument("--seconds",type=float,default=60);ap.add_argument("--memory-mib",type=int,default=2048)
 a=ap.parse_args(argv);need(math.isfinite(a.seconds) and 0<a.seconds<=180,"finite shared profile budget at most180")
 need(0<a.memory_mib<=4096,"at most4096MiB per process")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 signal.signal(signal.SIGTERM,sigstop);signal.signal(signal.SIGINT,sigstop)
 start=time.monotonic();deadline=start+a.seconds-min(5,a.seconds/10);out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 rec={"format":"isp-third-missing-four-high-profile-v1","status":"running","phase":"actual-inputs",
  "events":[],"outputs":[],"parameters":{},"largeDataUploadedOrCommitted":False,
  "old786HighPivotsRecomputed":False,"old29SourcesRecomputed":False,"old21UnitSolutionsRecomputed":False,
  "newOriginalThirdCoChainsConstructed":False,"completeHighKernelConstructed":False,
  "newM0RightHandSidesSolved":0,"leadingUnitProved":False}
 code=1;bind=None
 def ck():
  rec["mathematicalElapsedSeconds"]=time.monotonic()-start;save(out/"third-missing-four-high-profile-receipt.json",rec)
 def check():
  if STOP or time.monotonic()>=deadline:raise BudgetExpired("actual profile checkpoint boundary")
 def add(p):add_output(rec,p);ck()
 def cached(p,inputs):
  if not p.exists():return None
  x=read(p);need(x["binding"]==bind,"same high-profile result binding")
  for k,v in inputs.items():need(x[k]==v,"same actual stage input "+k)
  return x
 try:
  paths={"old_unit":a.second_out/"prepared"/"second-left-m0-unit-input.json.gz",
   "high_pair":a.normal5_out/"prepared"/"complete-original-high-normal-five-and-four.json.gz",
   "old_h5_profile":a.normal5_out/"prepared"/"original-h5-field-unit-profile.json.gz",
   "source_receipt":a.pairing_out/"pairing"/"same-source-koszul29-pairing-worker-receipt.json",
   "head_kernel":a.consumer_out/"residual-span"/"complete-third21-normal-four-head-combinations.json.gz",
   "residual":a.consumer_out/"residual-span"/"complete-third21-residual-after-paid166-span.json.gz",
   "span_profile":a.consumer_out/"residual-span"/"complete-residual144-original-unit-profile.json.gz",
   "span_solution":a.consumer_out/"residual-span"/"complete-residual144-by21-rational-unit-solution.json.gz"}
  ids={k:identity(v) for k,v in paths.items()}
  for k,(n,s) in PINS.items():need(ids[k]=={"bytes":n,"sha256":s},"actual missing-four input "+k)
  material={"programIdentity":identity(__file__),"inputIdentities":ids,
   "highRows":1736,"normalFiveColumns":1287,"normalFourColumns":1485,
   "paidSourceCount":29,"remainingHeadQuotientDimension":4}
  bind=hashlib.sha256(json.dumps(material,sort_keys=True,separators=(",",":")).encode()).hexdigest()
  rec["parameters"].update(material);rec["parameters"].update(binding=bind,secondsLimit=a.seconds,memoryMiB=a.memory_mib)
  ip=out/"invocation.json"
  if ip.exists():need(read(ip)["binding"]==bind,"same portable profile input binding")
  save(ip,{**material,"binding":bind,"paths":{k:str(v.resolve()) for k,v in paths.items()}})
  ck()
  unit=read(paths["old_unit"]);pair=read(paths["high_pair"]);oldh=read(paths["old_h5_profile"])
  J=list(map(int,unit["originalSourceRows"]));hi=list(map(int,unit["oldZeroRowPositions"]));hs=set(hi)
  need(len(J)==4354 and len(hi)==len(hs)==1736 and J==sorted(set(J)),"same complete source and high orders")
  need(pair["binding"]==oldh["binding"]==HIGH_BINDING and pair["highOriginalRowPositions"]==hi and
   oldh["highPairIdentity"]==ids["high_pair"] and oldh["rankModulo31"]==1287 and
   oldh["fullQColumnRankProvedByMinor"] and pair["allOriginalHighForcingRowsZero"] and
   pair["allNormalFourColumnsRetained"],"actual original high pair with paid H5 injection")
  rows=[]
  for i,row in zip(hi,pair["rows"]):
   need(int(row["originalSourcePosition"])==i and int(row["originalSourceRow"])==J[i],"original high row labels")
   d={int(j):int(v) for j,v in row["coefficients"]};need(all(0<=j<2772 and v for j,v in d.items()),"complete H5/H4 sparse columns")
   rows.append(d)
  need(len(rows)==1736 and all(not unit["originalCorrectionRows"][i] for i in hi),"whole high zero M0 rows")
  low=[i for i in range(4354) if i not in hs]
  # First retain the actual four quotient representatives; no large solve.
  rec["phase"]="four-genuine-head-quotient-representatives";ck();check()
  qpath=out/"four-genuine-third-head-quotient-representatives.json.gz"
  qinfo=cached(qpath,{"headKernelIdentity":ids["head_kernel"],"residualIdentity":ids["residual"]})
  if qinfo is None:
   kc=read(paths["head_kernel"]);rs=read(paths["residual"]);prof=read(paths["span_profile"]);ss=read(paths["span_solution"])
   need(kc["binding"]==rs["binding"]==prof["binding"]==ss["binding"]==CONSUMER_BINDING and
    kc["restrictedResidualRank"]==4 and kc["actualNormalFourThirdHeadDimension"]==17 and
    kc["allOriginalResidualKernelProductsZero"],"actual completed17 plus quotient4")
   Kc=[list(map(int,v)) for v in kc["primitiveIntegerResidualKernelColumns"]]
   need(len(Kc)==17 and all(len(v)==21 for v in Kc),"complete original residual kernel coordinates")
   KR,kr=fmpq_mat(Kc).rref();kr=int(kr);need(kr==17,"actual17 independent kernel directions")
   kp=pivots(KR,17);free=[j for j in range(21) if j not in set(kp)];need(len(free)==4,"actual four-dimensional quotient")
   R=[list(map(int,v)) for v in rs["integerResidualColumns"]]
   need(len(R)==21 and all(len(v)==4354 for v in R),"whole saved21 original residuals")
   four=[R[j] for j in free]
   need(all(not v[i] for v in four for i in hi),"all four quotient residuals have zero original high rows")
   active=[i for i in range(4354) if any(v[i] for v in four)]
   scaled=[]
   for i in active:
    g=0
    for v in four:g=math.gcd(g,abs(v[i]))
    scaled.append([v[i]//g for v in four])
   need(int(fmpq_mat(scaled).rank())==4,"actual four chosen original residual representatives independent")
   D=list(map(int,ss["denominators"]));N=[list(map(int,v)) for v in ss["numeratorColumns"]]
   ts=list(map(int,prof["targetColumnContents"]));bs=list(map(int,prof["basisColumnContents"]));pv=list(map(int,prof["paidPivotColumns"]))
   maps=[]
   for j in free:
    gamma=[str(fmpq(0)) for _ in range(166)]
    for k,col in enumerate(pv):gamma[col]=str(fmpq(N[j][k],bs[k]))
    maps.append({"residualCoordinate":j,"targetBeta":str(fmpq(D[j],ts[j])),
     "paid166Gamma":gamma,"headParameterMeaning":"kappa=e_j before the complete original consumer scale transport"})
   qinfo={"binding":bind,"headKernelIdentity":ids["head_kernel"],"residualIdentity":ids["residual"],
    "spanProfileIdentity":ids["span_profile"],"spanSolutionIdentity":ids["span_solution"],
    "kernel17PivotCoordinates":kp,"fourQuotientRepresentativeCoordinates":free,
    "complete4354OriginalResidualColumns":[[str(v) for v in c] for c in four],
    "actualOriginalResidualRank":4,"all1736HighResidualEntriesZero":True,
    "actualConsumerBetaGammaMaps":maps,"nonhomogeneousRightSideCount":4,
    "allHighHomogeneousFreedomStillRequired":True,"old17CompletedCoChainsNeedNoRecomputation":True}
   save(qpath,qinfo)
  add(qpath);rec["parameters"]["fourQuotientRepresentativeCoordinates"]=qinfo["fourQuotientRepresentativeCoordinates"];check()
  # Profile the same untouched integer H45, not the enlarged low system.
  rec["phase"]="actual-original-H45-field-profile";ck()
  fp=out/"complete-original-H45-field-profile.json.gz"
  field=cached(fp,{"originalHighPairIdentity":ids["high_pair"]})
  if field is None:
   H=nmod_mat(1736,2772,[row.get(j,0)%31 for row in rows for j in range(2772)],31)
   R,r=H.rref();r=int(r);cols=pivots(R,r);del H,R;check()
   MT=nmod_mat(r,1736,[row.get(j,0)%31 for j in cols for row in rows],31)
   RT,rr=MT.rref();need(int(rr)==r,"same actual transposed field profile rank")
   rid=pivots(RT,r);del MT,RT;check()
   U=nmod_mat(r,r,[rows[i].get(j,0)%31 for i in rid for j in cols],31)
   det=int(U.det())%31;need(det!=0,"actual original H45 unit minor");del U
   field={"binding":bind,"originalHighPairIdentity":ids["high_pair"],
    "prime":31,"rows":1736,"columns":2772,"rankModulo31":r,
    "originalHighRowIndices":rid,"originalSourcePositions":[hi[i] for i in rid],
    "originalSourceRows":[J[hi[i]] for i in rid],"originalHighColumnIndices":cols,
    "unitDeterminantModulo31":det,"normalFiveColumnPrefix":1287,
    "all1485NormalFourColumnsRetained":True,"exactQRankNotAssertedFromFieldAlone":True}
   save(fp,field)
  add(fp);rec["actualH45RankModulo31"]=field["rankModulo31"];check()
  # Exact support, not a truncation of nonsupported source kernels.
  rec["phase"]="paid29-exact-high-support-intersection";ck()
  sr=read(paths["source_receipt"]);need(sr["binding"]==PAIR_BINDING and sr["status"]=="completed" and
   sr["completeFree36ImageRankOverQ"]==29 and sr["all29FullOriginal4367ProductsZero"] and
   sr["parameters"]["sourceBinding"]==SOURCE_BINDING,"same true29 original source family")
  audits=sr["parameters"]["verifiedSourceColumns"];need(len(audits)==29,"complete source audit order")
  support=a.pairing_out/"reconstructed-source29";K=[]
  for j,aud in enumerate(audits):
   z=aud["certificate"];p=support/z["file"];need(identity(p)=={"bytes":z["bytes"],"sha256":z["sha256"]},"actual full source29 bytes")
   c=read(p);v=list(map(int,c["original6188IntegerCoefficients"]))
   need(c["binding"]==SOURCE_BINDING and c["column"]==j and len(v)==6188 and
    c["all1834OutsideSourceCoefficientsZero"] and c["all4367ExactIntegerProductsZero"] and
    vecsha(v)==aud["sourceSHA256"],"true full source, selected support and paid products")
   K.append([v[i-1] for i in J])
  sp=out/"complete-paid29-original-high-support-relations.json.gz"
  exact=cached(sp,{"sourceReceiptIdentity":ids["source_receipt"],"originalHighPairIdentity":ids["high_pair"]})
  if exact is None:
   active=[i for i in low if any(v[i] for v in K)];mat=[]
   for i in active:
    g=0
    for v in K:g=math.gcd(g,abs(v[i]))
    mat.append([v[i]//g for v in K])
   if mat:
    RR,rlo=fmpq_mat(mat).rref();rlo=int(rlo);pv=pivots(RR,rlo)
    cs=[]
    for j in range(29):
     if j in pv:continue
     w=[fmpq(0) for _ in range(29)];w[j]=fmpq(1)
     for i,k in enumerate(pv):w[k]=-RR[i,j]
     cs.append(primitive_q(w))
   else:rlo=0;cs=[[int(i==j) for i in range(29)] for j in range(29)]
   d=len(cs);need(d==29-rlo,"complete high-supported combinations of paid29")
   left=[]
   for aindex,c in enumerate(cs):
    check()
    full=[sum(c[j]*K[j][i] for j in range(29)) for i in range(4354)]
    need(all(full[i]==0 for i in low),"exact source combination supported wholly in original high rows")
    w=[full[i] for i in hi];need(any(w),"injective actual29 high relation")
    prod=[0]*2772
    for i,v in enumerate(w):
     if v:
      for j,b in rows[i].items():prod[j]+=v*b
    need(not any(prod),"all original2772 H45 products of true high source relation")
    left.append(w)
   if d:need(int(fmpq_mat(left).rank())==d,"all exact high dependencies independent")
   exact={"binding":bind,"sourceReceiptIdentity":ids["source_receipt"],"originalHighPairIdentity":ids["high_pair"],
    "paidSourceCount":29,"rankOfPaid29OutsideHighOverQ":rlo,"exactHighSupportedSourceDimension":d,
    "primitive29SourceCombinationColumns":[[str(v) for v in c] for c in cs],
    "complete1736HighLeftRelationColumns":[[str(v) for v in c] for c in left],
    "all2618NonhighSourceCoefficientsZero":True,"all2772OriginalHighProductsZero":True,
    "allHighRelationsIndependentOverQ":True,"newOriginalMatrixKernelReconstructionPerformed":False,
    "completeHighKernelConstructed":False}
   save(sp,exact)
  add(sp)
  r=int(field["rankModulo31"]);d=int(exact["exactHighSupportedSourceDimension"]);upper=1736-d
  need(r<=upper,"actual field lower and true rational dependency upper agree")
  exactrank=r==upper
  rec.update(status="completed",phase="complete",outcome="complete-high-rank-and-four-quotient-preparation" if exactrank else
   "high-rank-interval-and-four-quotient-preparation",
   actualH45RankModulo31=r,actualH45RankOverQLowerBound=r,actualH45RankOverQUpperBound=upper,
   actualH45RankOverQExactlyKnown=exactrank,actualPaid29HighSupportDimension=d,
   fullHighKernelDimensionLowerBound=2772-upper,fullHighKernelDimensionUpperBound=2772-r,
   highKernelQuotientByPaid130DimensionLowerBound=2772-upper-130,
   highKernelQuotientByPaid130DimensionUpperBound=2772-r-130,
   actualFourQuotientRepresentativesIndependent=True,allFourOriginalHighForcingRowsZero=True,
   allActualHighSourceDependencyProductsZero=True,completeHighKernelConstructed=False,
   newOriginalThirdCoChainsConstructed=False,newM0RightHandSidesSolved=0)
  rec["parameters"].update(actualFieldProfileIdentity=identity(fp),actualHighSourceRelationIdentity=identity(sp),
   actualFourQuotientIdentity=identity(qpath),old786HighPivotsUnchanged=True,
   nextSourceEquation="high: H*z=0; low modulo paid166: R4*c+L*z=0; retain all homogeneous high kernel",
   notAssumedJointHighRank1736=True,notAssumed906NewDirections=True,
   originalHighHomogeneousColumns=2772,originalHighRows=1736,originalNonhighRows=2618)
  code=0
 except BudgetExpired as e:
  rec.update(status="completed-prefix",error=str(e));code=75
 except Exception as e:
  rec.update(status="failed",error=str(e),exceptionType=type(e).__name__)
  (out/"exception.log").write_text(traceback.format_exc(),encoding="utf-8");code=1
 finally:ck()
 print(json.dumps(rec),flush=True);return code
if __name__=="__main__":sys.exit(main(sys.argv[1:]))
