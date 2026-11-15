#!/usr/bin/env python3
"""Same-source29 exact third-quotient pairing on the paid22 second heads.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
The paid codimension equality makes the29 tests complete after quotienting HF/T.
No new M0 solve, normal5 continuation, or old support-kernel reconstruction.
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
 "old_full":(12690,"b186ecd4ef8a8ca910392a8900c838da1e9e166a0b4738b40748677fd7e14a70"),
 "heads":(633788,"3107ab8547071205466ff5b5aa2ef5f0e3ea81a976258a25184c9a0d7e709fe2"),
 "first_jets":(1701626,"2aabfc92860f66942e7a8eb3d9254ab911e7b8b2f255d40bfaa1235ed4d482fe"),
 "coefficients":(20580,"7ab537a3c8f9a3d13b924a23f37f8d4ce4fa7621e3608920404ed0051b2fd5c1"),
 "primitive":(65159,"44350c49f9f60c61427b7278bf7f3d24b6cb2e6583848a113b03bb109516d4fe"),
 "old_pair":(112488,"b1b4c81c2e827fa92a375dfdc94d183604741badba3962de9e998add821946b1"),
 "old_pair_receipt":(15304,"11b0f10e9c0750b73644c425f91b48a249e5829a8dc7960e68e7713ef545f289")}
PRIMITIVE_RAW_SHA="fa2e5d80e9fbd47e1e237ae60c548900a15922a0543e02be77fc972dc52944b3"
SECOND_BINDING="c40049455e9f310607586b55cc271ca00636dc954f0de63693d0da886a6d067e"
PAIR_BINDING="ea772f01fa0ab8a761287893c15a94f83ebc6326703b40b82a5846e02b020e39"
# The actual source binding is read from the verified pair receipt; the literal
# below is used as an independent check and does not contain a filesystem path.
SOURCE_BINDING="2d9b068281400ec635fc2c912edf29e59d2bec1e3686bf6c3f6abd6ac01890f2"
def forcing_worker(invpath,out):
 inv=checked_inv(invpath);p=inv["paths"];bind=inv["binding"];out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True)
 start=time.monotonic();cp=out/"original-third-forcing-on22-receipt.json"
 rec={"status":"running","phase":"actual-original-cochains","binding":bind,"outputs":[],"parameters":{},"verifiedColumns":[]}
 def ck():
  rec["elapsedSeconds"]=time.monotonic()-start;save(cp,rec)
 ck()
 unit=read(p["old_unit"]);paid=read(p["old_full"]);heads=read(p["heads"]);jj=read(p["first_jets"]);co=read(p["coefficients"])
 need(unit["binding"]==paid["binding"]==SECOND_BINDING and paid["status"]=="completed" and
 paid["secondHeadImageDimension"]==22 and paid["all4354OriginalSecondLeftProductsZero"],
 "same actual22 complete second jets")
 need(unit["inputIdentities"]["heads"]==inv["inputIdentities"]["heads"] and
 unit["inputIdentities"]["first_jets"]==inv["inputIdentities"]["first_jets"],
 "same actual first source basis used by the paid second forcing")
 raw=gzip.decompress(pathlib.Path(p["primitive"]).read_bytes())
 need(hashlib.sha256(raw).hexdigest()==PRIMITIVE_RAW_SHA,"complete original primitive integer polynomial bytes")
 eqs=json.loads(raw)["equations"];Fs=[[],[],[],[]]
 need(len(eqs)==17 and all(len(r)==77 for r in eqs),"complete original17 by77 parameter entries")
 for e,row in enumerate(eqs):
  rr=[[],[],[],[]]
  for j,pol in enumerate(row):
   v=list(map(int,pol));need(v,"nonempty primitive coefficient polynomial")
   if e>=11 and j<11:
    need(not any(v),"all original Gamma linear terms zero")
    for k in range(4):rr[k].append(0)
   else:
    d=10 if e<11 and j<11 else 0 if e<11 else 5
    need(not any(v[d+1:]),"same natural-u coefficient degree")
    for k in range(4):rr[k].append(v[d-k] if d>=k and d-k<len(v) else 0)
  for k in range(4):Fs[k].append(rr[k])
 need(Fs[0]==[list(map(int,r)) for r in co["constant"]] and
 Fs[1]==[list(map(int,r)) for r in co["naturalFirst"]],"all1309 natural constant and first coefficient identities")
 J=list(map(int,unit["originalSourceRows"]));need(len(J)==len(set(J))==4354 and J==sorted(J),"same full selected source order")
 mon=[(i,) for i in range(11)]+[(i,j) for i in range(11) for j in range(i,11)]
 mult=[q for d in range(4) for q in itertools.combinations_with_replacement(range(11),d)]
 whole=[q for d in range(5,0,-1) for q in itertools.combinations_with_replacement(range(11),d)]
 wi={q:i for i,q in enumerate(whole)};need(len(whole)==4367 and len(mult)*17==6188,"complete unchanged moment dictionaries")
 Eold=list(map(int,unit["oldFirstCorrectionOutputCoordinates"]));Enew=list(map(int,unit["secondCorrectionOutputCoordinates"]))
 need(Eold==list(map(int,heads["correctionOutputCoordinates"])) and len(Eold)==len(Enew)==1546,"old and new embeddings retained")
 F=list(map(int,unit["headComplementCoordinates"]));need(len(F)==len(set(F))==3 and all(0<=i<36 for i in F),"all three first complement coordinates")
 cols=[list(map(int,v)) for v in jj["primitiveIntegerVariableColumns"]]
 need(len(cols)==33 and all(len(v)==1582 for v in cols),"all33 actual first source columns")
 X=[[(j,cols[j][i]) for j in range(33) if cols[j][i]] for i in range(1546)]
 C=[[(j,cols[j][1546+i]) for j in range(33) if cols[j][1546+i]] for i in range(36)]
 L=sparse_rows(heads["primitiveIntegerRows"])
 need(heads["all4354ConstantProductsZero"] and heads["completeSameIHeadBasisIndependent"],"complete sameI constant left basis")
 rows=[]
 for raw_id in J:
  e=(raw_id-1)%17;mu=mult[(raw_id-1)//17];rr=[]
  for j,m in enumerate(mon):
   cs=[Fs[k][e][j] for k in range(4)]
   if any(cs):rr.append((wi[tuple(sorted(mu+m))],*cs))
  rows.append(rr)
 original_terms=sum(len(r) for r in rows)
 coeffp=out/"same-original-natural-through-third-coefficients.json.gz"
 save(coeffp,{"binding":bind,"coefficientInputIdentity":inv["inputIdentities"]["primitive"],"constant":Fs[0],
 "naturalFirst":Fs[1],"naturalSecond":Fs[2],"naturalThird":Fs[3],
 "coMovingSourceDerivativeTermDiscarded":False,"allNaturalDegreeRulesVerified":True})
 add_output(rec,coeffp)
 files={z["file"]:z for z in paid["outputs"]}
 source_dir=pathlib.Path(inv["oldSecondProductsDirectory"])
 audit=[];forcing_paths=[]
 for k in range(22):
  oldp=source_dir/("complete-original-second-left-jet-%02d.json.gz"%k);oid=identity(oldp)
  z=files[oldp.name];need(oid=={"bytes":z["bytes"],"sha256":z["sha256"]},"actual paid second candidate bytes")
  old=read(oldp);need(old["binding"]==SECOND_BINDING,"same original second candidate binding")
  h=list(map(int,old["firstHeadKernelCoefficients"]));t=list(map(int,old["threeFirstHeadComplementCoefficients"]))
  x2=list(map(int,old["secondCorrectionVariables"]))
  need(len(h)==33 and len(t)==3 and len(x2)==1546,"complete actual second source parameters")
  fp=out/("original-third-forcing-%02d.json.gz"%k)
  vp=out/("verified-original-third-forcing-%02d.json"%k)
  if fp.exists() and vp.exists():
   vr=read(vp);need(vr["binding"]==bind and vr["oldCandidateIdentity"]==oid and
   vr["forcingIdentity"]==identity(fp) and vr["allThreeLowerOriginalProductsZero"],
   "same completed source column and actual lower products")
  else:
   ch=[sum(v*h[j] for j,v in row) for row in C]
   ft=[0]*36
   for j,f in enumerate(F):ft[f]=t[j]
   a0=[0]*4367;a1=[0]*4367;a2=[0]*4367
   for i,row in L.items():
    a0[i]=sum(v*ch[j] for j,v in row)
    a1[i]=sum(v*ft[j] for j,v in row)
   for i,row in enumerate(X):a1[Eold[i]]+=sum(v*h[j] for j,v in row)
   for i,v in enumerate(x2):a2[Enew[i]]+=v
   need(any(a0),"nonzero actual second head")
   common=0
   for layer in [a0,a1,a2]:
    for v in layer:
     if v:common=math.gcd(common,abs(v))
     if common==1:break
    if common==1:break
   need(common>0,"nonzero actual three-level source")
   if common>1:
    a0=[v//common for v in a0];a1=[v//common for v in a1];a2=[v//common for v in a2]
   result=[];checks=0
   for i,row in enumerate(rows):
    v0=v1=v2=v3=0
    for ix,f0,f1,f2,f3 in row:
     b0=a0[ix];b1=a1[ix];b2=a2[ix]
     if f0:v0+=f0*b0;v1+=f0*b1;v2+=f0*b2
     if f1:v1+=f1*b0;v2+=f1*b1;v3+=f1*b2
     if f2:v2+=f2*b0;v3+=f2*b1
     if f3:v3+=f3*b0
    need(v0==v1==v2==0,"actual lower cochain product at source "+str(J[i])+" candidate "+str(k))
    result.append(v3);checks+=3
   need(checks==4354*3,"all three complete original lower products")
   save(fp,{"format":"isp-original-third-forcing-paid-second-head-v1","binding":bind,"column":k,
    "oldCandidateIdentity":oid,"oldFirstSourceIdentities":{a:inv["inputIdentities"][a] for a in ["heads","first_jets"]},
    "primitiveCoChainCommonDivisor":str(common),"originalSourceRows":J,
    "originalThirdForcingIntegerColumn":[str(x) for x in result],
    "lowerLambda0SHA256":vecsha(a0),"lowerLambda1SHA256":vecsha(a1),"lowerLambda2SHA256":vecsha(a2),
    "allThreeLowerOriginalProductsZero":True,"lowerOriginalProductCoordinates":checks,
    "naturalThirdFormula":"B1^T*lambda2+B2^T*lambda1+B3^T*lambda0",
    "maximumPrimitiveCoChainBits":max(abs(v).bit_length() for layer in [a0,a1,a2] for v in layer)})
   vr={"binding":bind,"column":k,"oldCandidateIdentity":oid,"forcingIdentity":identity(fp),
    "allThreeLowerOriginalProductsZero":True,"lowerOriginalProductCoordinates":checks,
    "originalThirdForcingSHA256":vecsha(result),
    "maximumThirdForcingBits":max((abs(v).bit_length() for v in result),default=0)}
   save(vp,vr)
  add_output(rec,fp);add_output(rec,vp);forcing_paths.append({"file":fp.name,**identity(fp)})
  audit.append(vr);rec["verifiedColumns"]=audit;ck()
 rec.update(status="completed",phase="complete",all22OriginalSecondCoChainsReverified=True,
 all287364LowerOriginalProductsZero=True,lowerOriginalProductCoordinates=22*4354*3,
 actualThirdForcingColumns=22,actualOriginalSourceRows=4354,
 full24SecondHeadsExplicit=False,coMovingThirdDerivativeUsed=False)
 rec["parameters"].update(originalSparseTermsPerSourceBundle=original_terms,forcingColumns=forcing_paths,
 completeNaturalCoefficientIdentity=identity(coeffp),oldAndNewCorrectionEmbeddingsKeptDistinct=True,
 bothFirstAndSecondKernelFreedomAccountedForInQuotient=True)
 ck();print(json.dumps({"status":"completed","columns":22,"all287364LowerOriginalProductsZero":True}),flush=True);return 0
def pairing_worker(invpath,forcingdir,out):
 from flint import fmpz_mat,fmpq_mat,fmpq
 inv=checked_inv(invpath);paths=inv["paths"];bind=inv["binding"];out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True)
 start=time.monotonic();cp=out/"same-source29-third-quotient-worker-receipt.json"
 rec={"status":"running","phase":"paid-complete-quotient","binding":bind,"outputs":[],"parameters":{}}
 def ck():
  rec["elapsedSeconds"]=time.monotonic()-start;save(cp,rec)
 ck()
 pp=read(paths["old_pair"]);pr=read(paths["old_pair_receipt"]);unit=read(paths["old_unit"])
 need(pp["binding"]==pr["binding"]==PAIR_BINDING and pr["status"]=="completed" and
 pr["pairingRankOverQ"]==5 and pr["firstThreeHFPairingRankOverQ"]==1 and
 pr["completeFree36ImageRankOverQ"]==29 and pr["all29FullOriginal4367ProductsZero"] and
 pr["all1309ConstantCoefficientsExactlyMatched"],"same actual rho5,h1,independent29 source pairing")
 need(pr["parameters"]["sourceBinding"]==SOURCE_BINDING and pp["oldUnitIdentity"]==inv["inputIdentities"]["old_unit"],
 "same restored29 and actual HF/T forcing")
 J=list(map(int,unit["originalSourceRows"]));need(pp["originalSourceRows"]==J,"same complete original J coordinate order")
 oldrows=[list(map(int,r)) for r in pp["integerRows"]]
 need(len(oldrows)==29 and all(len(r)==36 for r in oldrows),"all actual previous29 by36 pairing")
 fd=pathlib.Path(forcingdir);fr=read(fd/"original-third-forcing-on22-receipt.json")
 need(fr["binding"]==bind and fr["status"]=="completed" and fr["all287364LowerOriginalProductsZero"],
 "all actual22 true second cochains before pairing")
 audits=pr["parameters"]["verifiedSourceColumns"];support=pathlib.Path(inv["supportDirectory"])
 need(len(audits)==29 and pp["sourceAudits"]==audits,"same exact original29 source order")
 sources=[]
 for j,a in enumerate(audits):
  z=a["certificate"];p=support/z["file"]
  need(identity(p)=={"bytes":z["bytes"],"sha256":z["sha256"]},"actual paid29 certificate")
  c=read(p);v=list(map(int,c["original6188IntegerCoefficients"]))
  need(len(v)==6188 and c["binding"]==SOURCE_BINDING and c["column"]==j and
  c["all1834OutsideSourceCoefficientsZero"] and c["all4367ExactIntegerProductsZero"] and
  vecsha(v)==a["sourceSHA256"],"same actual full-original source and verified products")
  sources.append([v[r-1] for r in J])
 forces=[]
 for j,z in enumerate(fr["parameters"]["forcingColumns"]):
  p=fd/z["file"];need(identity(p)=={"bytes":z["bytes"],"sha256":z["sha256"]},"complete actual new forcing column")
  f=read(p);v=list(map(int,f["originalThirdForcingIntegerColumn"]))
  need(f["binding"]==bind and f["column"]==j and f["originalSourceRows"]==J and len(v)==4354 and
  f["allThreeLowerOriginalProductsZero"],"actual true second source and full third forcing")
  forces.append(v)
 need(len(forces)==22,"exactly22 paid second heads")
 mp=out/"actual-same-source29-by58-third-pairing.json.gz"
 if mp.exists():
  v=read(mp);need(v["binding"]==bind and v["oldPairIdentity"]==inv["inputIdentities"]["old_pair"] and
  v["forcingReceiptIdentity"]==identity(fd/"original-third-forcing-on22-receipt.json"),"same complete saved third pairing")
  rows=[list(map(int,r)) for r in v["integerRows"]]
 else:
  K=fmpz_mat(29,4354,[x for v in sources for x in v])
  R3=fmpz_mat(4354,22,[forces[j][i] for i in range(4354) for j in range(22)])
  X=K*R3
  rows=[oldrows[i]+[int(X[i,j]) for j in range(22)] for i in range(29)]
  save(mp,{"format":"isp-same-source29-third-pairing-v1","binding":bind,"rows":29,"columns":58,
   "oldPairIdentity":inv["inputIdentities"]["old_pair"],"forcingReceiptIdentity":identity(fd/"original-third-forcing-on22-receipt.json"),
   "integerRows":[[str(x) for x in r] for r in rows],"columnOrder":"oldHF3,oldT33,newR3_on22",
   "sameOriginalSourceBasisRetained":True,"originalRowsNotDividedByUnitContents":True})
  del K,R3,X
 add_output(rec,mp);rec["phase"]="complete-third-quotient-rank";ck()
 need(len(rows)==29 and all(len(r)==58 for r in rows) and [r[:36] for r in rows]==oldrows,
 "unchanged exact old pairing block")
 rd=[]
 for r in rows:
  g=0
  for x in r:g=math.gcd(g,abs(x))
  rd.append(g or 1)
 A=[[x//rd[i] for x in r] for i,r in enumerate(rows)]
 cd=[]
 for j in range(58):
  g=0
  for i in range(29):g=math.gcd(g,abs(A[i][j]))
  cd.append(g or 1)
 N=[[A[i][j]//cd[j] for j in range(58)] for i in range(29)]
 M=fmpq_mat(N);R,rank=M.rref();rank=int(rank);pv=pivots(R,rank)
 oldrank=int(fmpq_mat([r[:36] for r in N]).rank())
 need(oldrank==5,"actual unchanged lower-page image rank")
 b=rank-5;need(0<=b<=22,"actual third image on22 heads")
 need(b+2>=3,"restricted rank0 conflicts with paid full third modular lower bound3")
 free=[j for j in range(58) if j not in set(pv)];nullcols=[]
 for f in free:
  w=[fmpq(0) for _ in range(58)];w[f]=fmpq(1)
  for i,j in enumerate(pv):w[j]=-R[i,f]
  nullcols.append(primitive_q([w[j]/cd[j] for j in range(58)]))
 Z=fmpq_mat(58,len(nullcols),[nullcols[j][i] for i in range(58) for j in range(len(nullcols))])
 need(all(not x for x in (fmpq_mat(rows)*Z).entries()),"all original58-coordinate paired kernel products")
 projected=fmpq_mat(22,len(nullcols),[nullcols[j][36+i] for i in range(22) for j in range(len(nullcols))])
 PR,hrank=projected.transpose().rref();hrank=int(hrank)
 need(hrank==22-b,"complete projection to the actual22 head coordinates")
 headcols=[primitive_q([PR[i,j] for j in range(22)]) for i in range(hrank)]
 hp=out/"complete-third-pairing-kernel-and22-head-projection.json.gz"
 save(hp,{"binding":bind,"pairingIdentity":identity(mp),"rank":rank,"restrictedThirdRank":b,
  "primitiveOriginal58KernelColumns":[[str(x) for x in v] for v in nullcols],
  "complete22HeadProjectionColumns":[[str(x) for x in v] for v in headcols],
  "headProjectionRank":hrank,"headCoordinatesReferToPrimitiveCoChains":True,
  "old22CoordinateRecovery":"multiply each coordinate by the reciprocal of its recorded primitiveCoChainCommonDivisor",
  "rowGCDs":[str(x) for x in rd],"columnGCDs":[str(x) for x in cd],
  "nonzeroNormalizedRREFRows":[[str(R[i,j]) for j in range(58)] for i in range(rank)],
  "pairedKernelProductsVerified":True,"positiveThirdHeadsExistByCompleteQuotientButLambda3NotExplicit":True})
 add_output(rec,hp)
 lo=max(3,b);hi=b+2
 need(lo<=hi<=24,"full24 second-head domain rank interval")
 exact=lo==hi
 d=93+hrank;cof=90+max(hrank-1,0);qlo=8426;qhi=8770-d-101
 costs={"nonbasis":qhi-1+45,"sourceTransfer":8770+55-cof-101-11,
        "target":8770+64-cof-101-10-qlo}
 outcome="complete-selected-third-rank-three" if exact else "restricted22-third-exact-image-and-full-rank-interval"
 rec.update(status="completed",phase="complete",outcome=outcome,
 oldLowerPagePairingRank=5,completeCombined29By58PairingRank=rank,
 restricted22ThirdConnectionRankOverQ=b,completeRestricted22ThirdImageComputed=True,
 allLowerPageKernelFreedomRetained=True,quotientRestrictionIsomorphismProved=True,
 completePaired22HeadProjectionDimension=hrank,fullSelectedThirdRankOverQLowerBound=lo,
 fullSelectedThirdRankOverQUpperBound=hi,fullSelectedThirdRankExactly3=exact,
 fullThirdHeadSpaceDimension=21 if exact else None,provedThirdHeadSpaceDimensionLowerBound=hrank,
 explicitNewLambda3SourcesConstructed=False,full24SecondHeadsExplicit=False,
 allOriginal58PairingKernelProductsVerified=True,newM0RightHandSidesSolved=0,
 selectedMinorInfinityOrderOverQLowerBound=d,selectedCofactorInfinityOrderOverQLowerBound=cof,
 selectedOriginalSourceReplacementOrderOverQLowerBound=cof,
 conditionalSourceCostUpperBound=max(costs.values()),conditionalTargetBranchCostUpperBound=costs["target"],
 originalTargetMembershipProved=False,leadingUnitProved=False)
 rec["parameters"].update(quotientIsomorphism="E/W -> K29*/pi(W); dim E36,dim K29=29,dim W12,dim pi(W)5,ker pi subset W",
  fullSecondConnectionRankOverQ=9,fullSecondHeadSpaceDimension=24,paidExplicitSecondHeads=22,
  pairingPivotColumns=pv,fullThirdLowerBoundReason="same Q/F31 constant and first two ranks4318,3,9; paid F31 third rank3",
  conditionalCostPolynomialDegree=101,conditionalQuotientDegreeInterval=[qlo,qhi],
  conditionalCostBranches=costs,oldPairIdentity=inv["inputIdentities"]["old_pair"],
  newPairIdentity=identity(mp),newProjectionIdentity=identity(hp))
 ck()
 print(json.dumps({"status":"completed","outcome":outcome,"restrictedThirdRank":b,
 "fullThirdRankInterval":[lo,hi],"provedThirdHeads":hrank}),flush=True);return 0
def main(argv):
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ["first-out","second-out","rebuild-root","pairing-out","primitive-equations","out"]:
  ap.add_argument("--"+k,required=True,type=pathlib.Path)
 ap.add_argument("--seconds",type=float,default=120);ap.add_argument("--memory-mib",type=int,default=2048)
 a=ap.parse_args(argv);need(math.isfinite(a.seconds) and 0<a.seconds<=300,"shared actual budget at most300 seconds")
 need(0<a.memory_mib<=2048,"at most2048MiB per process")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 start=time.monotonic();deadline=start+a.seconds-min(5,a.seconds/10);out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 rec={"format":"isp-same-source29-third-pairing-pipeline-v1","status":"running","phase":"inputs","events":[],"parameters":{},
 "largeDataUploadedOrCommitted":False,"newM0RightHandSidesSolved":0,"normalFiveEliminationContinued":False,
 "oldQSourceKernelsRebuilt":False,"completeRestricted22ThirdImageComputed":False,
 "explicitNewLambda3SourcesConstructed":False,"leadingUnitProved":False}
 code=1
 def checkpoint():
  rec["mathematicalElapsedSeconds"]=time.monotonic()-start;save(out/"same-source-koszul29-third-pairing-receipt.json",rec)
 def check():
  if time.monotonic()>=deadline:raise BudgetExpired("actual shared third-pairing deadline")
 def run(name,cmd,rp):
  check();st=time.monotonic();rem=max(.001,deadline-time.monotonic())
  with (out/(name+".log")).open("w") as log:
   pr=subprocess.Popen(cmd,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
   try:pr.wait(timeout=rem)
   except subprocess.TimeoutExpired:
    os.killpg(pr.pid,signal.SIGTERM)
    try:pr.wait(timeout=2)
    except subprocess.TimeoutExpired:os.killpg(pr.pid,signal.SIGKILL);pr.wait()
    rec["events"].append({"stage":name,"exitCode":pr.returncode,"elapsedSeconds":time.monotonic()-st,"sharedDeadlineReached":True})
    raise BudgetExpired(name+": actual checkpoint retained")
  rec["events"].append({"stage":name,"exitCode":pr.returncode,"elapsedSeconds":time.monotonic()-st})
  rr=read(rp) if rp.exists() else {}
  rec["parameters"][name+"ActualStatus"]=rr.get("status");checkpoint()
  need(pr.returncode==0 and rr.get("status")=="completed",name+": completed actual receipt required")
  return rr
 try:
  paths={"old_unit":a.second_out/"prepared"/"second-left-m0-unit-input.json.gz",
   "old_full":a.second_out/"full-products"/"second-left-full-products-receipt.json",
   "heads":a.first_out/"left-envelope"/"complete-same-I-characteristic-zero-left-heads.json.gz",
   "first_jets":a.first_out/"left-envelope"/"complete-original-left-first-jets.json.gz",
   "coefficients":a.rebuild_root/"rebuilt-first"/"same-original-natural-constant-and-first-coefficients.json.gz",
   "primitive":a.primitive_equations,
   "old_pair":a.pairing_out/"pairing"/"actual-koszul29-by36-original-forcing-pairing.json.gz",
   "old_pair_receipt":a.pairing_out/"pairing"/"same-source-koszul29-pairing-worker-receipt.json"}
  ids={}
  for k,p in paths.items():
   ids[k]=identity(p);need(ids[k]=={"bytes":PINS[k][0],"sha256":PINS[k][1]},"actual input bytes: "+k)
  material={"programIdentity":identity(__file__),"inputIdentities":ids,"paidSecondRank":9,
   "headColumns":22,"forcingColumns":22,"lowerPairingRank":5,"naturalChart":"same infinity u=1/s"}
  bind=hashlib.sha256(json.dumps(material,sort_keys=True,separators=(",",":")).encode()).hexdigest()
  inv={**material,"binding":bind,"paths":{k:str(p.resolve()) for k,p in paths.items()},
   "oldSecondProductsDirectory":str((a.second_out/"full-products").resolve()),
   "supportDirectory":str((a.pairing_out/"reconstructed-source29").resolve())}
  ip=out/"invocation.json"
  if ip.exists():need(read(ip)["binding"]==bind,"same third-pairing input and code binding")
  save(ip,inv);rec["parameters"].update(binding=bind,inputIdentities=ids,programIdentity=material["programIdentity"],
   secondsLimit=a.seconds,memoryMiBPerProcess=a.memory_mib,completeSourceQuotientDimension=24,
   currentExplicitSecondHeadCount=22,allLowerPageKernelFreedomRetained=True,
   sourceBasisOriginalConstantChecksInheritedOnlyAfterExactFileHashMatch=True)
  checkpoint();fdir=out/"original-forcing";pdir=out/"pairing"
  for phase,worker,folder,rname in [
   ("original-third-forcing","--forcing-worker",fdir,"original-third-forcing-on22-receipt.json"),
   ("same-source29-third-quotient","--pairing-worker",pdir,"same-source29-third-quotient-worker-receipt.json")]:
   rec["phase"]=phase;checkpoint();rp=folder/rname
   rr=read(rp) if rp.exists() else None
   if rr and rr.get("status")=="completed":
    need(rr["binding"]==bind,"same completed actual stage")
    for z in rr["outputs"]:need(identity(folder/z["file"])=={"bytes":z["bytes"],"sha256":z["sha256"]},"complete stage cache bytes")
    rec["events"].append({"stage":phase,"completeActualCacheReused":True})
   else:
    cmd=[sys.executable,"-B",str(pathlib.Path(__file__).resolve()),worker,str(ip)]
    if worker=="--pairing-worker":cmd.append(str(fdir))
    cmd.append(str(folder));rr=run(phase,cmd,rp)
   rec["parameters"][phase+"ReceiptIdentity"]=identity(rp)
   rec["parameters"][phase+"ActualTemporaryOutputs"]=rr["outputs"]
   if worker=="--forcing-worker":
    for k in ["all22OriginalSecondCoChainsReverified","all287364LowerOriginalProductsZero","lowerOriginalProductCoordinates",
     "actualThirdForcingColumns","actualOriginalSourceRows"]:rec[k]=rr[k]
   else:
    for k,v in rr.items():
     if k not in ["parameters","outputs","binding","elapsedSeconds","status","phase"]:rec[k]=v
    rec["parameters"]["actualThirdQuotientConclusion"]=rr["parameters"]
  rec.update(status="completed",phase="complete");code=0
 except (BudgetExpired,subprocess.TimeoutExpired) as e:
  rec.update(status="completed-prefix",error=str(e));code=75
 except Exception as e:
  rec.update(status="failed",error=str(e),exceptionType=type(e).__name__)
  (out/"exception.log").write_text(traceback.format_exc());code=1
 finally:checkpoint()
 print(json.dumps(rec),flush=True);return code
if __name__=="__main__":
 if len(sys.argv)>1 and sys.argv[1]=="--forcing-worker":
  sys.exit(forcing_worker(pathlib.Path(sys.argv[2]),pathlib.Path(sys.argv[3])))
 if len(sys.argv)>1 and sys.argv[1]=="--pairing-worker":
  sys.exit(pairing_worker(pathlib.Path(sys.argv[2]),pathlib.Path(sys.argv[3]),pathlib.Path(sys.argv[4])))
 sys.exit(main(sys.argv[1:]))
