#!/usr/bin/env python3
"""Complete original normal<=4 third lifts from only21 new M0 unit solutions.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
Reuse all paid36+130 columns. Solve a true144-row residual unit, retain all
4354 residuals, then reconstruct and verify the original four cochain levels.
"""
import argparse,gzip,hashlib,io,itertools,json,math,os,pathlib,resource,signal,subprocess,sys,time,traceback
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
def primitive(v):
 d=1
 for x in v:d=math.lcm(d,int(x.q))
 z=[int(x.p)*(d//int(x.q)) for x in v];g=0
 for x in z:g=math.gcd(g,abs(x))
 need(g>0,"nonzero rational vector")
 sg=-1 if next(x for x in z if x)<0 else 1
 return [sg*(x//g) for x in z]
def pivots(M,rank):
 p=[]
 for i in range(int(rank)):
  j=next(j for j in range(M.ncols()) if M[i,j]);need(M[i,j]==1,"RREF unit pivot");p.append(j)
 need(p==sorted(set(p)),"ordered RREF pivots");return p
def colgcd(v):
 g=0
 for x in v:g=math.gcd(g,abs(x))
 return g or 1
def invread(p):
 i=read(p);need(ident(__file__)==i["programIdentity"],"same exact consumer source")
 for k,v in i["paths"].items():need(ident(v)==i["inputIdentities"][k],"same actual consumer input "+k)
 return i
def newrec(out,name,binding,phase):
 out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True);rp=out/name;st=time.monotonic()
 r={"status":"running","phase":phase,"binding":binding,"outputs":[],"parameters":{}}
 def ck():
  r["elapsedSeconds"]=time.monotonic()-st;save(rp,r)
 ck();return r,ck
def keep(r,p):
 z={"file":p.name,**ident(p),"temporaryOnly":True}
 r["outputs"]=[x for x in r["outputs"] if x["file"]!=p.name]+[z]
def completed(p,bind):
 if not p.exists():return None
 r=read(p);need(r["binding"]==bind,"same stage binding")
 if r["status"]!="completed":return None
 for z in r["outputs"]:need(ident(p.parent/z["file"])=={"bytes":z["bytes"],"sha256":z["sha256"]},"actual complete stage outputs")
 return r
PINS={
 "old_unit":(9008513,"c53406d65cfd66f2f3b6f1c946bd7495e44c7041538c4f3c85518eb7be7d5dfe"),
 "old_solution":(18124389,"9c3b02d2674af645ffcfd5297cf5c9ac287fe314d0c40f49c8bb99be9396352d"),
 "old_full":(12690,"b186ecd4ef8a8ca910392a8900c838da1e9e166a0b4738b40748677fd7e14a70"),
 "normal4_full":(27679,"4158cc3b978edeafd9c993e7f1c054d9acc419eb9a5d3f34cf8e9f2cff965c22"),
 "normal4_rref":(25174,"7e060678aa752228f8515e105726ad5335aaf403bb8965b19f6be796b25d1956"),
 "normal4_solution":(75595833,"ccfdf7dbcc6b0d20ec5979a0c198df70f539f10669687ac9a0108f2706caae0d"),
 "normal4_kernel":(1447062,"67e2d9b2dbf7c2eea4e56d060503565633ff064eec4b220c2f8417c751f47e33"),
 "normal4_block":(911218,"a359450582e0081fbabd6ff79e6e0e7083d7cd5bfdcef1d801438d00a3d5c814"),
 "heads":(633788,"3107ab8547071205466ff5b5aa2ef5f0e3ea81a976258a25184c9a0d7e709fe2"),
 "first_jets":(1701626,"2aabfc92860f66942e7a8eb3d9254ab911e7b8b2f255d40bfaa1235ed4d482fe"),
 "through3":(40272,"795a0ae79597cdd55ace1ccc215aedc639e19100e1e2e1942fd30f99b373951a"),
 "prepared_unit":(5511912,"675fea9cbc0be933f7c1dc742552184fd62ccdc21acd17efa9b5ba91de05b623"),
 "prepared_rhs":(4617848,"22d41ddbd72836d013f0855cf094f243ae5bc63a07f9006b9603031383794598"),
 "unit21_receipt":(2131,"f65f843bef9856075220b87c1870edbee50cdf8f5bbbad09564db1c8fbb0303d"),
 "unit21_solution":(9850907,"92f802330ac3c61fa30dc31b03b43ca4dfd534e4539f5d1ffde2a344a2829366")}
PREP_BINDING="3ac423ccd312ea0fa7084f70b9a2fb788a26822a62e9918998f17d6762fc371a"
OLD_BINDING="c40049455e9f310607586b55cc271ca00636dc954f0de63693d0da886a6d067e"
N4_BINDING="672a21c0de59ec537f5d19333524f92ceb71ad3621eec643b9c11cf3f3fce2d3"
UNIT_WORKER_SHA="c9e1eee6142d29daf661682e177702825e90aef7222611baa2adadaffe0dc731"
def span_worker(invpath,out):
 from flint import fmpq,fmpq_mat,fmpz_mat,nmod_mat
 inv=invread(invpath);bind=inv["binding"];p=inv["paths"];out=pathlib.Path(out)
 rp=out/"third21-complete-original-residual-span-receipt.json"
 oldcomplete=completed(rp,bind)
 if oldcomplete:print(json.dumps({"status":"completed","reused":True}),flush=True);return 0
 r,ck=newrec(out,rp.name,bind,"whole-original21-residuals")
 old=read(p["old_unit"]);nu=read(p["prepared_unit"]);sol=read(p["unit21_solution"]);ur=read(p["unit21_receipt"])
 need(old["binding"]==OLD_BINDING and nu["binding"]==sol["binding"]==ur["binding"]==PREP_BINDING and
 sol["inputIdentity"]==inv["inputIdentities"]["prepared_unit"] and ur["candidateIdentity"]==inv["inputIdentities"]["unit21_solution"] and
 ur["status"]=="completed" and ur["all1546OriginalUnitRowsVerified"] and ur["verifiedColumnCount"]==21 and
 ur["originalUnitProductCoordinates"]==32466 and ur["workerSHA256"]==UNIT_WORKER_SHA,"complete actual new21 unit solutions")
 for k in ["originalSourceRows","originalCorrectionRows","rowCoefficientContents","selectedUnitRowIndices","secondCorrectionOutputCoordinates"]:
  need(nu[k]==old[k],"same full original M0 and embedding "+k)
 rows=[[(int(j),int(v)) for j,v in x] for x in old["originalCorrectionRows"]]
 Q=[[int(x) for x in row] for row in nu["originalRightHandSideRows"]]
 dn=list(map(int,sol["denominators"]));nn=[[int(x) for x in c] for c in sol["numeratorColumns"]]
 need(len(dn)==len(nn)==21 and all(d>0 for d in dn) and all(len(c)==1546 for c in nn),"complete actual rational21")
 target=[];targetids=[]
 for j in range(21):
  f=out/("complete-original-third21-unit-residual-%02d.json.gz"%j)
  if f.exists():
   x=read(f);need(x["binding"]==bind and x["unitSolutionIdentity"]==inv["inputIdentities"]["unit21_solution"] and
    x["column"]==j,"same actual completed residual")
   v=list(map(int,x["values"]))
  else:
   v=[dn[j]*Q[i][j]+sum(a*nn[j][k] for k,a in row) for i,row in enumerate(rows)]
   need(all(v[i]==0 for i in old["selectedUnitRowIndices"]),"all original unit residual entries zero")
   save(f,{"binding":bind,"column":j,"unitSolutionIdentity":inv["inputIdentities"]["unit21_solution"],
    "unitInputIdentity":inv["inputIdentities"]["prepared_unit"],"values":[str(x) for x in v],
    "all1546OriginalUnitResidualEntriesZero":True,"all4354OriginalRowsRetained":True})
  need(len(v)==4354 and all(v[i]==0 for i in old["selectedUnitRowIndices"]),"complete actual residual4354")
  target.append(v);targetids.append({"file":f.name,**ident(f)});keep(r,f)
  r["completedOriginalTargetResiduals"]=j+1;ck()
 del Q,nn
 of=read(p["old_full"]);nf=read(p["normal4_full"]);rr=read(p["normal4_rref"])
 need(of["binding"]==OLD_BINDING and of["status"]=="completed" and of["smallResidualRank"]==14,
  "paid complete old36 original residuals")
 need(nf["binding"]==rr["binding"]==N4_BINDING and nf["status"]=="completed" and
 nf["extendedSmallResidualRank"]==rr["rank"]==144 and nf["secondHeadImageDimension"]==22 and
 nf["all4354OriginalSecondLeftProductsZero"],"paid complete normal4 residual span144")
 piv=list(map(int,rr["pivotColumns"]));need(len(piv)==len(set(piv))==144 and piv==sorted(piv),"complete paid pivot columns")
 ot={z["file"]:z for z in of["outputs"]};nt={z["file"]:z for z in nf["outputs"]}
 residual=[];resids=[]
 for j in range(166):
  d=pathlib.Path(p["old_full"]).parent if j<36 else pathlib.Path(p["normal4_full"]).parent
  name=("original-residual-column-%02d.json.gz"%j) if j<36 else ("additional-original-residual-column-%02d.json.gz"%(j-36))
  table=ot if j<36 else nt;f=d/name;z=table[name]
  need(ident(f)=={"bytes":z["bytes"],"sha256":z["sha256"]},"paid original residual bytes")
  x=read(f);need(x["binding"]==(OLD_BINDING if j<36 else N4_BINDING) and
   x["column"]==(j if j<36 else j-36) and x["all1546UnitResidualEntriesZero"],"paid complete original residual scope")
  v=list(map(int,x["values"]));need(len(v)==4354,"all4354 original paid residual rows")
  residual.append(v);resids.append({"column":j,"file":name,**ident(f)})
 r["phase"]="true144-original-unit-profile";ck()
 scaleS=[colgcd(residual[j]) for j in piv]
 B=[[x//g for x in residual[j]] for j,g in zip(piv,scaleS)]
 scaleT=[colgcd(v) for v in target];T=[[x//g for x in v] for v,g in zip(target,scaleT)]
 rg=[]
 for i in range(4354):
  g=0
  for c in B:g=math.gcd(g,abs(c[i]))
  rg.append(g or 1)
 active=[i for i in range(4354) if any(c[i] for c in B)]
 pp=out/"complete-residual144-original-unit-profile.json.gz"
 if pp.exists():
  pro=read(pp);need(pro["binding"]==bind and pro["paidResidualIdentities"]==resids and
   pro["targetResidualIdentities"]==targetids and pro["basisColumnContents"]==[str(x) for x in scaleS] and
   pro["targetColumnContents"]==[str(x) for x in scaleT],"same actual residual unit profile")
  chosen=list(map(int,pro["originalUnitRowPositions"]))
 else:
  prof=[]
  for prime in [31,65521]:
   A=nmod_mat(144,len(active),[(c[i]//rg[i])%prime for c in B for i in active],prime)
   R,rk=A.rref();rk=int(rk);pr=pivots(R,rk);del A,R
   prof.append({"prime":prime,"rank":rk,"algorithmicUnitSelectionOnly":True})
   if rk==144:
    chosen=[active[k] for k in pr];U=nmod_mat(144,144,[(B[j][i]//rg[i])%prime for i in chosen for j in range(144)],prime)
    det=int(U.det())%prime;need(det!=0,"actual original residual unit determinant");del U
    break
  else:raise ValueError("no certified residual144 unit at the two fixed algorithmic primes")
  pro={"binding":bind,"paidResidualIdentities":resids,"targetResidualIdentities":targetids,
   "paidPivotColumns":piv,"basisColumnContents":[str(x) for x in scaleS],
   "targetColumnContents":[str(x) for x in scaleT],"originalUnitRowPositions":chosen,
   "originalUnitSourceRows":[old["originalSourceRows"][i] for i in chosen],
   "unitRowContents":[str(rg[i]) for i in chosen],"algorithmicPrime":prime,
   "unitDeterminantModuloPrime":det,"attemptedAlgorithmicProfiles":prof,
   "newOriginalMatrixRankConclusionFromPrime":False}
  save(pp,pro)
 keep(r,pp)
 r["parameters"].update(actualResidualUnitOrder=144,algorithmicUnitPrime=pro["algorithmicPrime"],
  algorithmicUnitDeterminant=pro["unitDeterminantModuloPrime"],
  maximumPrimitiveUnitCoefficientBits=max(abs(B[j][i]//rg[i]).bit_length() for i in chosen for j in range(144)),
  maximumTargetPrimitiveCoefficientBits=max(abs(T[j][i]).bit_length() for i in chosen for j in range(21)),
  paidResidualColumnContentsKept=True,targetColumnContentsKept=True,all4354RowsRetained=True)
 ck()
 sp=out/"complete-residual144-by21-rational-unit-solution.json.gz"
 if sp.exists():
  sx=read(sp);need(sx["binding"]==bind and sx["unitProfileIdentity"]==ident(pp),"same complete span unit solution")
  dx=list(map(int,sx["denominators"]));nx=[[int(x) for x in c] for c in sx["numeratorColumns"]]
 else:
  U=fmpq_mat(144,144,[fmpq(B[j][i],rg[i]) for i in chosen for j in range(144)])
  R=fmpq_mat(144,21,[fmpq(-T[j][i],rg[i]) for i in chosen for j in range(21)])
  r["phase"]="actual-residual144-by21-exact-solve";ck()
  X=U.solve(R,algorithm="dixon");dx=[];nx=[]
  for j in range(21):
   d=1
   for i in range(144):d=math.lcm(d,int(X[i,j].q))
   dx.append(d);nx.append([int(X[i,j].p)*(d//int(X[i,j].q)) for i in range(144)])
  save(sp,{"binding":bind,"unitProfileIdentity":ident(pp),"denominators":[str(x) for x in dx],
   "numeratorColumns":[[str(x) for x in c] for c in nx],
   "completeCandidateSavedBeforeAllOriginalProducts":True,"selectedRowsVerified":False})
  del U,R,X
 keep(r,sp);need(len(dx)==len(nx)==21 and all(d>0 for d in dx) and all(len(c)==144 for c in nx),"complete true144 by21 solution")
 r["phase"]="all-original-residual-span-products";ck()
 rp2=out/"complete-third21-residual-after-paid166-span.json.gz"
 if rp2.exists():
  v=read(rp2);need(v["binding"]==bind and v["unitSolutionIdentity"]==ident(sp),"same complete all-row span residual")
  rem=[[int(x) for x in c] for c in v["integerResidualColumns"]]
 else:
  BM=fmpz_mat(4354,144,[B[j][i] for i in range(4354) for j in range(144)])
  NM=fmpz_mat(144,21,[nx[j][i] for i in range(144) for j in range(21)]);P=BM*NM
  rem=[[int(P[i,j])+dx[j]*T[j][i] for i in range(4354)] for j in range(21)]
  need(all(rem[j][i]==0 for j in range(21) for i in chosen),"all3024 original residual unit products")
  save(rp2,{"binding":bind,"unitSolutionIdentity":ident(sp),
   "integerResidualColumns":[[str(x) for x in c] for c in rem],"all3024OriginalUnitProductsZero":True,
   "all4354OriginalRowsRetained":True})
  del BM,NM,P
 keep(r,rp2);del residual,B,target,T
 need(len(rem)==21 and all(len(c)==4354 for c in rem) and
  all(rem[j][i]==0 for j in range(21) for i in chosen),"complete checked actual residuals")
 gg=[colgcd(c) for c in rem];acts=[i for i in range(4354) if any(c[i] for c in rem)]
 if acts:
  H=fmpq_mat(len(acts),21,[rem[j][i]//gg[j] for i in acts for j in range(21)])
  HR,rank=H.rref();rank=int(rank);pv=pivots(HR,rank)
  ks=[]
  for j in range(21):
   if j in pv:continue
   w=[fmpq(0) for _ in range(21)];w[j]=fmpq(1)
   for i,k in enumerate(pv):w[k]=-HR[i,j]
   ks.append(primitive([w[k]/gg[k] for k in range(21)]))
  del H,HR
 else:rank=0;ks=[[int(i==j) for i in range(21)] for j in range(21)]
 need(len(ks)==21-rank,"complete actual restricted head combination count")
 for j,k in enumerate(ks):
  need(all(sum(rem[c][i]*k[c] for c in range(21))==0 for i in range(4354)),
   "all original residual combination products")
 kp=out/"complete-third21-normal-four-head-combinations.json.gz"
 save(kp,{"binding":bind,"unitProfileIdentity":ident(pp),"unitSolutionIdentity":ident(sp),
  "originalResidualIdentity":ident(rp2),"restrictedResidualRank":rank,
  "primitiveIntegerResidualKernelColumns":[[str(x) for x in c] for c in ks],
  "actualNormalFourThirdHeadDimension":len(ks),"allOriginalResidualKernelProductsZero":True,
  "targetCombinationRule":"beta_j=Dspan_j*k_j/targetColumnContent_j",
  "paidResidualCombinationRule":"gamma_p=sum_j Nspan[j,p]*k_j/basisColumnContent_p",
  "completeGlobalThirdHeadDimensionRemains21":True})
 keep(r,kp)
 r.update(status="completed",phase="complete",restrictedResidualRank=rank,
 actualNormalFourThirdHeadDimension=len(ks),all21OriginalResidualsConstructed=True,
 all4354OriginalResidualRowsRetained=True,allOriginalResidualKernelProductsZero=True,
 newM0RightHandSidesRecomputed=False,old36And130UnitSolutionsRecomputed=False)
 r["parameters"].update(residualUnitProfile=ident(pp),residualUnitSolution=ident(sp),headCombinations=ident(kp),
 actualOriginalSpanUnitRows=144,completePaidSpanRank=144,
 originalResidualCombinationProducts=4354*len(ks))
 ck();print(json.dumps({"status":"completed","actualNormalFourHeads":len(ks),"restrictedResidualRank":rank}),flush=True);return 0

def cochain_worker(invpath,out,spandir):
 from flint import fmpq,fmpq_mat
 inv=invread(invpath);bind=inv["binding"];p=inv["paths"];out=pathlib.Path(out);spandir=pathlib.Path(spandir)
 rp=out/"third21-complete-original-four-layer-products-receipt.json"
 done=completed(rp,bind)
 if done:print(json.dumps({"status":"completed","reused":True}),flush=True);return 0
 r,ck=newrec(out,rp.name,bind,"actual-four-layer-source-assembly")
 sr=read(spandir/"third21-complete-original-residual-span-receipt.json")
 need(sr["binding"]==bind and sr["status"]=="completed","complete all-original span reduction")
 profile=read(spandir/"complete-residual144-original-unit-profile.json.gz")
 span=read(spandir/"complete-residual144-by21-rational-unit-solution.json.gz")
 kc=read(spandir/"complete-third21-normal-four-head-combinations.json.gz")
 ks=[[int(v) for v in c] for c in kc["primitiveIntegerResidualKernelColumns"]];h=len(ks)
 need(kc["binding"]==profile["binding"]==span["binding"]==bind and h==sr["actualNormalFourThirdHeadDimension"],
  "same complete actual head combinations")
 prep=read(p["prepared_rhs"]);old=read(p["old_unit"]);un=read(p["unit21_solution"])
 oldsol=read(p["old_solution"]);newsol=read(p["normal4_solution"])
 block=read(p["normal4_block"]);k4=read(p["normal4_kernel"])
 heads=read(p["heads"]);first=read(p["first_jets"]);coeff=read(p["through3"])
 J=list(map(int,old["originalSourceRows"]));need(len(J)==4354,"same original J")
 need(block["binding"]==k4["binding"]==N4_BINDING and k4["blockIdentity"]==inv["inputIdentities"]["normal4_block"] and
 k4["completeRationalKernelProved"] and k4["all1736OriginalHighProductsZero"],"complete actual130 high sources")
 D0=list(map(int,oldsol["denominators"]));N0=[[int(v) for v in c] for c in oldsol["numeratorColumns"]]
 D4=list(map(int,newsol["denominators"]));N4=[[int(v) for v in c] for c in newsol["numeratorColumns"]]
 Dn=list(map(int,un["denominators"]));Nn=[[int(v) for v in c] for c in un["numeratorColumns"]]
 K4=[[int(v) for v in c] for c in k4["primitiveIntegerKernelColumns"]]
 need(oldsol["binding"]==OLD_BINDING and newsol["binding"]==N4_BINDING and un["binding"]==PREP_BINDING and
  len(D0)==len(N0)==36 and len(D4)==len(N4)==len(K4)==130 and len(Dn)==len(Nn)==21 and
  all(d>0 for d in D0+D4+Dn) and all(len(v)==1546 for v in N0+N4+Nn) and
  all(len(v)==1485 for v in K4),"complete paid and new source columns")
 Eold=list(map(int,old["oldFirstCorrectionOutputCoordinates"]));Enew=list(map(int,old["secondCorrectionOutputCoordinates"]))
 E4=list(map(int,block["normalFourOutputCoordinates"]));F=list(map(int,old["headComplementCoordinates"]))
 need(len(Eold)==len(Enew)==1546 and len(E4)==1485 and len(F)==3,"all true source embeddings")
 basis=[[int(v) for v in c] for c in first["primitiveIntegerVariableColumns"]]
 X=[[basis[j][i] for j in range(33)] for i in range(1546)]
 C=[[basis[j][1546+i] for j in range(33)] for i in range(36)]
 L={int(i):[(int(j),int(v)) for j,v in row] for i,row in heads["primitiveIntegerRows"]}
 oldfull=read(p["old_full"]);ot={q["file"]:q for q in oldfull["outputs"]}
 source=[]
 for j,a in enumerate(prep["forcingInputAudit"]):
  name="complete-original-second-left-jet-%02d.json.gz"%j;cp=pathlib.Path(p["old_full"]).parent/name;z=ot[name]
  need(ident(cp)=={"bytes":z["bytes"],"sha256":z["sha256"]},"same actual old second cochain source")
  ca=read(cp);need(ca["binding"]==OLD_BINDING,"same old second cochain")
  source.append((list(map(int,ca["firstHeadKernelCoefficients"])),
   list(map(int,ca["threeFirstHeadComplementCoefficients"])),list(map(int,ca["secondCorrectionVariables"])),
   int(a["oldPrimitiveCoChainCommonDivisor"])))
 Z=[[int(v) for v in c] for c in prep["headCoordinatesInPrimitiveOld22"]]
 G=list(map(int,prep["rightHandSideCommonDivisors"]))
 DX=list(map(int,span["denominators"]));NX=[[int(v) for v in c] for c in span["numeratorColumns"]]
 bs=list(map(int,profile["basisColumnContents"]));ts=list(map(int,profile["targetColumnContents"]))
 pp=list(map(int,profile["paidPivotColumns"]))
 need(len(source)==22 and len(Z)==len(G)==len(DX)==len(NX)==len(ts)==21 and len(bs)==len(pp)==144,"complete true combination maps")
 Fs=[[list(map(int,x)) for x in coeff[k]] for k in ["constant","naturalFirst","naturalSecond","naturalThird"]]
 mons=[(i,) for i in range(11)]+[(i,j) for i in range(11) for j in range(i,11)]
 mus=[q for d in range(4) for q in itertools.combinations_with_replacement(range(11),d)]
 whole=[q for d in range(5,0,-1) for q in itertools.combinations_with_replacement(range(11),d)]
 oi={q:i for i,q in enumerate(whole)};need(len(whole)==4367,"complete original output dictionary")
 rows=[]
 for raw in J:
  e=(raw-1)%17;mu=mus[(raw-1)//17];rr=[]
  for j,m in enumerate(mons):
   fs=[Fs[k][e][j] for k in range(4)]
   if any(fs):rr.append((oi[tuple(sorted(mu+m))],*fs))
  rows.append(rr)
 heads33=[];cand=[];ver=[]
 for col,kappa in enumerate(ks):
  cp=out/("complete-original-third-left-jet-%02d.json.gz"%col);vp=out/("verified-original-third-left-jet-%02d.json"%col)
  if cp.exists():
   ca=read(cp);need(ca["binding"]==bind and ca["headCombinationIdentity"]==ident(spandir/"complete-third21-normal-four-head-combinations.json.gz"),
    "same original third candidate")
   pars=ca["primitiveIntegerParameters"]
   c=list(map(int,pars["oldSecondFirstHeadCoefficients"]));layers=[[int(v) for v in x] for x in ca["primitiveOriginalLambdaLayers"]]
  else:
   beta=[fmpq(DX[j]*kappa[j],ts[j]) for j in range(21)]
   gam=[fmpq(0) for _ in range(166)]
   for q,b in enumerate(pp):gam[b]=fmpq(sum(NX[j][q]*kappa[j] for j in range(21)),bs[q])
   weights=[]
   for k in range(22):
    value=sum((beta[j]*fmpq(Dn[j]*Z[j][k],G[j]) for j in range(21)),fmpq(0))
    weights.append(value/source[k][3])
   c0=[sum((weights[k]*source[k][0][i] for k in range(22)),fmpq(0)) for i in range(33)]
   t0=[sum((weights[k]*source[k][1][i] for k in range(22)),fmpq(0)) for i in range(3)]
   x2=[sum((weights[k]*source[k][2][i] for k in range(22)),fmpq(0)) for i in range(1546)]
   a=[D0[j]*gam[j] for j in range(3)];y=[D0[j+3]*gam[j+3] for j in range(33)]
   x3=[]
   for i in range(1546):
    value=sum((beta[j]*Nn[j][i] for j in range(21)),fmpq(0))
    value+=sum((gam[j]*N0[j][i] for j in range(36)),fmpq(0))
    value+=sum((gam[36+j]*N4[j][i] for j in range(130)),fmpq(0));x3.append(value)
   eta=[sum((gam[36+j]*D4[j]*K4[j][i] for j in range(130)),fmpq(0)) for i in range(1485)]
   groups=[c0,t0,x2,a,y,x3,eta];flat=[v for g in groups for v in g]
   zi=primitive(flat);lens=[len(g) for g in groups];parsed=[];off=0
   for n in lens:parsed.append(zi[off:off+n]);off+=n
   c,t,x2i,ai,yi,x3i,etai=parsed
   ch=[sum(C[i][j]*c[j] for j in range(33)) for i in range(36)]
   yh=[sum(C[i][j]*yi[j] for j in range(33)) for i in range(36)]
   ft=[0]*36;fa=[0]*36
   for j,f in enumerate(F):ft[f]=t[j];fa[f]=ai[j]
   layers=[[0]*4367 for _ in range(4)]
   for i,row in L.items():
    layers[0][i]=sum(v*ch[j] for j,v in row)
    layers[1][i]=sum(v*(ft[j]+yh[j]) for j,v in row)
    layers[2][i]=sum(v*fa[j] for j,v in row)
   for i in range(1546):
    layers[1][Eold[i]]+=sum(X[i][j]*c[j] for j in range(33))
    layers[2][Enew[i]]+=x2i[i]
    layers[2][Eold[i]]+=sum(X[i][j]*yi[j] for j in range(33))
    layers[3][Enew[i]]+=x3i[i]
   for i in range(1485):layers[3][E4[i]]+=etai[i]
   need(any(layers[0]),"nonzero actual third head")
   ca={"binding":bind,"column":col,"headCombinationIdentity":ident(spandir/"complete-third21-normal-four-head-combinations.json.gz"),
    "preparedRightHandSideIdentity":inv["inputIdentities"]["prepared_rhs"],
    "newUnitSolutionIdentity":inv["inputIdentities"]["unit21_solution"],
    "old36UnitSolutionIdentity":inv["inputIdentities"]["old_solution"],
    "old130UnitSolutionIdentity":inv["inputIdentities"]["normal4_solution"],
    "primitiveIntegerParameters":{"oldSecondFirstHeadCoefficients":[str(v) for v in c],
     "oldSecondFirstComplementCoefficients":[str(v) for v in t],"oldSecondCorrectionVariables":[str(v) for v in x2i],
     "thirdFirstComplementCompensation":[str(v) for v in ai],"thirdFirstKernelCompensation":[str(v) for v in yi],
     "thirdOldSupportCorrection":[str(v) for v in x3i],"thirdNormalFourCorrection":[str(v) for v in etai]},
    "primitiveOriginalLambdaLayers":[[str(v) for v in x] for x in layers],
    "actualTargetCombinationBeforePrimitiveScaling":[str(v) for v in beta],
    "actualPaid166ResidualCombinationBeforePrimitiveScaling":[str(v) for v in gam],
    "fourthForcingNotComputedHere":True,"candidateOnlyUntilMatchingVerifiedReceipt":True}
   save(cp,ca)
  need(len(c)==33 and len(layers)==4 and all(len(x)==4367 for x in layers),"all original four cochain layers")
  cid=ident(cp)
  if vp.exists():
   vr=read(vp);need(vr["binding"]==bind and vr["candidateIdentity"]==cid and vr["all17416OriginalProductsZero"],
    "same complete actual third cochain verification")
  else:
   for i,row in enumerate(rows):
    val=[0]*4
    for ix,f0,f1,f2,f3 in row:
     l0,l1,l2,l3=[x[ix] for x in layers]
     val[0]+=f0*l0
     val[1]+=f0*l1+f1*l0
     val[2]+=f0*l2+f1*l1+f2*l0
     val[3]+=f0*l3+f1*l2+f2*l1+f3*l0
    need(not any(val),"original four cochain products at source "+str(J[i])+" column "+str(col))
   vr={"binding":bind,"candidateIdentity":cid,"column":col,
    "all17416OriginalProductsZero":True,"originalSourceRows":4354,"completeCoChainLayers":4,
    "fullOriginalCoChainProductCoordinates":17416};save(vp,vr)
  heads33.append(c);cand.append({"file":cp.name,**cid});ver.append({"file":vp.name,**ident(vp)})
  r["outputs"]=cand+ver;r["completedOriginalThirdCoChains"]=col+1
  r["maximumOriginalCoChainBits"]=max(r.get("maximumOriginalCoChainBits",0),max(abs(x).bit_length() for layer in layers for x in layer))
  ck()
 rank=int(fmpq_mat(33,h,[heads33[j][i] for i in range(33) for j in range(h)]).rank()) if h else 0
 need(rank==h,"all actual third heads independent in complete first-head coordinates")
 r.update(status="completed",phase="complete",
 outcome="complete-original-third-cochains-normal-four" if h==21 else "restricted-normal-four-third-cochains-only",
 actualExplicitThirdHeadDimension=h,completeGlobalThirdHeadDimension=21,
 all21CompleteThirdHeadsExplicit=h==21,allOriginalFourLayerProductsZero=True,
 originalFourLayerProductCoordinates=4354*4*h,allActualHeadCoordinatesIndependent=True,
 correctionNormalDegreeAtMost=4,newM0RightHandSidesSolved=21,old36And130UnitSolutionsRecomputed=False,
 completeFourthIncomingImageComputed=False,knownFourthIncomingImageDimension=13,
 completeFourthIncomingImageDimension=15,remainingFourthIncomingImageDimension=2,
 fourthForcingComputed=False,leadingUnitProved=False)
 r["parameters"].update(originalCandidateIdentities=cand,verifiedCandidateIdentities=ver,
 completeGlobalThirdHeadExistenceRetained=True,
 knownZeroHeadThirdFreedom="restricted paid family plus36 constant lambda3 directions and explicit33 LambdaC transport; full extra2 second-head family not constructed here")
 ck();print(json.dumps({"status":"completed","actualThirdHeads":h,"all21CompleteThirdHeadsExplicit":h==21}),flush=True);return 0

def main(argv):
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ["regauged-out","normal4-out","first-out","third-out","prepared-out","unit-out","out"]:
  ap.add_argument("--"+k,required=True,type=pathlib.Path)
 ap.add_argument("--seconds",type=float,default=300);ap.add_argument("--memory-mib",type=int,default=4096)
 a=ap.parse_args(argv);need(math.isfinite(a.seconds) and 0<a.seconds<=600,"finite shared consumer budget at most600")
 need(0<a.memory_mib<=8192,"at most8192MiB per process")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 st=time.monotonic();deadline=st+a.seconds;out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 rec={"format":"isp-third21-normal-four-original-consumer-v1","status":"running","phase":"inputs",
 "events":[],"parameters":{},"largeDataUploadedOrCommitted":False,"explicitNewLambda3SourcesConstructed":False}
 code=1
 def ck():
  rec["mathematicalElapsedSeconds"]=time.monotonic()-st;save(out/"third21-normal-four-original-consumer-receipt.json",rec)
 try:
  o=a.regauged_out;n=a.normal4_out;t=a.third_out
  paths={"old_unit":o/"prepared"/"second-left-m0-unit-input.json.gz",
   "old_solution":o/"unit-solve"/"complete-m0-unit-solution.json.gz",
   "old_full":o/"full-products"/"second-left-full-products-receipt.json",
   "normal4_full":n/"full-products"/"normal-four-full-products-receipt.json",
   "normal4_rref":n/"full-products"/"complete-normal-four-extended-small-residual-rref.json.gz",
   "normal4_solution":n/"additional-unit"/"complete-m0-unit-solution.json.gz",
   "normal4_kernel":n/"paid-high"/"complete-original-normal-four-high-kernel.json.gz",
   "normal4_block":n/"paid-high"/"complete-original-normal-four-block.json.gz",
   "heads":a.first_out/"left-envelope"/"complete-same-I-characteristic-zero-left-heads.json.gz",
   "first_jets":a.first_out/"left-envelope"/"complete-original-left-first-jets.json.gz",
   "through3":t/"original-forcing"/"same-original-natural-through-third-coefficients.json.gz",
   "prepared_unit":a.prepared_out/"third21-left-m0-unit-input.json.gz",
   "prepared_rhs":a.prepared_out/"complete-third21-original-right-hand-sides.json.gz",
   "unit21_receipt":a.unit_out/"m0-unit-solve-receipt.json",
   "unit21_solution":a.unit_out/"complete-m0-unit-solution.json.gz"}
  ids={k:ident(v) for k,v in paths.items()}
  for k,(sz,sha) in PINS.items():need(ids[k]=={"bytes":sz,"sha256":sha},"actual fixed consumer input "+k)
  ur=read(paths["unit21_receipt"])
  need(ur["status"]=="completed" and ur["binding"]==PREP_BINDING and
   ur["inputIdentity"]==ids["prepared_unit"] and ur["candidateIdentity"]==ids["unit21_solution"] and
   ur["workerSHA256"]==UNIT_WORKER_SHA and ur["all1546OriginalUnitRowsVerified"] and
   ur["originalUnitProductCoordinates"]==32466,"complete true unit21 input before consumer")
  material={"programIdentity":ident(__file__),"inputIdentities":ids,"actualTargetHeads":21,
   "completePaidResidualColumns":166,"completePaidResidualRank":144,"correctionNormalDegreeAtMost":4}
  bind=hashlib.sha256(json.dumps(material,sort_keys=True,separators=(",",":")).encode()).hexdigest()
  ip=out/"invocation.json"
  if ip.exists():need(read(ip)["binding"]==bind,"same consumer binding")
  save(ip,{**material,"binding":bind,"paths":{k:str(v.resolve()) for k,v in paths.items()}})
  rec["parameters"].update(material);rec["parameters"].update(binding=bind,secondsLimit=a.seconds,memoryMiBPerProcess=a.memory_mib);ck()
  span=out/"residual-span";prod=out/"original-products"
  for name,mode,folder,rname in [
   ("complete-original-residual-span","--span-worker",span,"third21-complete-original-residual-span-receipt.json"),
   ("complete-original-four-layer-products","--cochain-worker",prod,"third21-complete-original-four-layer-products-receipt.json")]:
   rec["phase"]=name;ck();rp=folder/rname;c=completed(rp,bind)
   if c:rec["events"].append({"stage":name,"completeActualStageReused":True})
   else:
    remaining=deadline-time.monotonic()
    if remaining<=5:raise BudgetExpired("shared original consumer deadline")
    cmd=[sys.executable,"-B",str(pathlib.Path(__file__).resolve()),mode,str(ip),str(folder)]
    if mode=="--cochain-worker":cmd.append(str(span))
    began=time.monotonic();grace=min(10,max(1,remaining/10))
    with (out/(name+".log")).open("a",encoding="utf-8") as log:
     pr=subprocess.Popen(cmd,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
     try:pr.wait(timeout=remaining-grace)
     except subprocess.TimeoutExpired:
      os.killpg(pr.pid,signal.SIGTERM)
      try:pr.wait(timeout=grace)
      except subprocess.TimeoutExpired:os.killpg(pr.pid,signal.SIGKILL);pr.wait()
      rec["events"].append({"stage":name,"elapsedSeconds":time.monotonic()-began,"exitCode":pr.returncode,"sharedDeadlineReached":True})
      raise BudgetExpired(name+" actual arrays retained")
    rec["events"].append({"stage":name,"elapsedSeconds":time.monotonic()-began,"exitCode":pr.returncode})
    need(pr.returncode==0 and rp.exists(),"actual "+name+" incomplete; inspect stage log")
    c=read(rp);need(c["status"]=="completed","actual completed stage receipt")
   rec["parameters"][name+"ReceiptIdentity"]=ident(rp)
   rec["parameters"][name+"TemporaryOutputs"]=c["outputs"]
   if mode=="--cochain-worker":
    for k,v in c.items():
     if k not in ["parameters","outputs","binding","elapsedSeconds","status","phase"]:rec[k]=v
  rec.update(status="completed",phase="complete",explicitNewLambda3SourcesConstructed=rec.get("actualExplicitThirdHeadDimension",0)>0);code=0
 except BudgetExpired as e:
  rec.update(status="completed-prefix",error=str(e));code=75
 except Exception as e:
  rec.update(status="failed",error=str(e),exceptionType=type(e).__name__)
  (out/"exception.log").write_text(traceback.format_exc(),encoding="utf-8");code=1
 finally:ck()
 print(json.dumps(rec),flush=True);return code
if __name__=="__main__":
 if len(sys.argv)>1 and sys.argv[1]=="--span-worker":sys.exit(span_worker(sys.argv[2],sys.argv[3]))
 if len(sys.argv)>1 and sys.argv[1]=="--cochain-worker":sys.exit(cochain_worker(sys.argv[2],sys.argv[3],sys.argv[4]))
 sys.exit(main(sys.argv[1:]))
