#!/usr/bin/env python3
"""Prepare the original4318 constant unit and only selected missing-third RHS.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
No large Gaussian or rational solve. All data remain temporary.
The complete F31 source kernel with free identity selects the unit rows.
"""
import argparse,gzip,hashlib,io,itertools,json,math,os,pathlib,resource,signal,struct,sys,time,traceback
sys.dont_write_bytecode=True
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
for k in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):os.environ[k]="1"
class BudgetExpired(Exception):pass
STOP=False
def stop(signum,frame):
 global STOP
 STOP=True
def need(v,s):
 if not v:raise ValueError(s)
def identity(p):
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
  b=json.dumps(v,sort_keys=True,separators=(",",":")).encode()
  need(len(b)<100000,"small permanent metadata only");q.write_bytes(b)
 os.replace(q,p);return {"file":p.name,**identity(p),"temporaryOnly":True}
def vsha(v):
 h=hashlib.sha256()
 for x in v:h.update((str(x)+"\n").encode())
 return h.hexdigest()
def pivots(R,rank):
 pp=[]
 for i in range(int(rank)):
  j=next((j for j in range(R.ncols()) if R[i,j]),None)
  need(j is not None and R[i,j]==1,"normalized field profile");pp.append(j)
 need(pp==sorted(set(pp)),"strict pivot order");return pp
def rowdict(row,n):
 pairs=[(int(j),int(v)) for j,v in row]
 need(len(pairs)==len({j for j,v in pairs}) and all(0<=j<n and v for j,v in pairs),"original sparse row canonical")
 return dict(pairs)
PINS={
 "old_unit":(9008513,"c53406d65cfd66f2f3b6f1c946bd7495e44c7041538c4f3c85518eb7be7d5dfe"),
 "m4":(911218,"a359450582e0081fbabd6ff79e6e0e7083d7cd5bfdcef1d801438d00a3d5c814"),
 "m5":(564745,"97054ecb078055a85af7ca4dbb2490b1f868ebcb40290fa4197efa67126a26b1"),
 "four":(106872,"7d8ef24fae893516a54667234d6e50eac52e006671e66c35de7c004f4f15db40"),
 "high_profile":(9606,"254a5173f108fec33890160d3424a8235e1ca2ef169fe7a801d7b6be268821d3"),
 "prepared_rhs":(4617848,"22d41ddbd72836d013f0855cf094f243ae5bc63a07f9006b9603031383794598"),
 "kernel36":(222788,"c008e57b7a7e80312f8ba292bb24241d53bb59d4c57b2a8d07ec1017b9de0744"),
 "selected_receipt":(75700,"5cd9543de68bdb562bbe21189d5b0712248e6943c5572fe38ff27ec4fc1f5f68"),
 "selected":(21285,"20373c07422701e37b9226fe1fe72cb8ee1e7848df505ebbacd92cf818093c2a"),
 "profile":(21066,"044b28d717749d23a2959a02c0f8ed7570bfa19bcdff04207056f2a66d2e413d"),
 "coefficients":(20580,"7ab537a3c8f9a3d13b924a23f37f8d4ce4fa7621e3608920404ed0051b2fd5c1")}
OLD="c40049455e9f310607586b55cc271ca00636dc954f0de63693d0da886a6d067e"
N4="672a21c0de59ec537f5d19333524f92ceb71ad3621eec643b9c11cf3f3fce2d3"
N5="eff732ce44d956078f54b08550801cecf96aed1f1ce9d517cd3bfd0c45698b2b"
FOUR="cd315e7a0b2999f9522fd96cd0c2d720de37938e75ae5133a97ad4ed3162bf3b"
PREP="3ac423ccd312ea0fa7084f70b9a2fb788a26822a62e9918998f17d6762fc371a"
FIELD="c11dd73f0b8f469a8c1abee84de0b8ff7a38906a992376a16129a44fcad8607b"
FREE=[1271,1204,1205,1256,1206,1223,1257,1156,1207,1224,2393,3328,4093,2326,3261,4501,4026,4281,4502,4587,2327,2378,3262,3313,4027,4078,4248,4282,4503,1716,1733,1750,1767,1784,1801,1818]
def paths_for(a):
 return {
 "old_unit":a.second_out/"prepared"/"second-left-m0-unit-input.json.gz",
 "m4":a.normal_four_out/"paid-high"/"complete-original-normal-four-block.json.gz",
 "m5":a.normal_five_out/"prepared"/"complete-original-normal-five-block.json.gz",
 "four":a.high_profile_out/"four-genuine-third-head-quotient-representatives.json.gz",
 "high_profile":a.high_profile_out/"complete-original-H45-field-profile.json.gz",
 "prepared_rhs":a.prepared_out/"complete-third21-original-right-hand-sides.json.gz",
 "kernel36":a.kernel36,"selected_receipt":a.selected_receipt,
 "selected":a.rebuild_root/"rebuilt-inputs"/"same-selected-original-source-indices.json",
 "profile":a.rebuild_root/"rebuilt-inputs"/"same-selected-original-output-indices.json",
 "coefficients":a.rebuild_root/"rebuilt-first"/"same-original-natural-constant-and-first-coefficients.json.gz",
 "gauge":a.second_out/"prepared"/"same-support-field-unit-gauge.json.gz",
 "field_cokernel":a.rebuild_root/"rebuilt-first"/"complete-selected-cokernel36-field31.json.gz"}
def prepare(a):
 from flint import nmod_mat
 start=time.monotonic();deadline=start+a.seconds-min(3,a.seconds/10)
 out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 rec={"format":"isp-missing-third-constant-unit-preparation-v1","status":"running","phase":"inputs",
  "parameters":{},"events":[],"outputs":[],"largeDataUploadedOrCommitted":False,
  "newRationalRightHandSidesSolved":0,"newOriginalThirdCoChainsConstructed":False,
  "old786PivotsRecomputed":False,"old130UnitSolutionsRecomputed":False,"newLargeGaussianPerformed":False,
  "constantUnitPrime31Proved":False,"fullTwelveQuotientColumnsSelected":False}
 cp=out/"missing-third-constant-unit-preparation-receipt.json";code=1
 def ck():
  rec["mathematicalElapsedSeconds"]=time.monotonic()-start;save(cp,rec)
 def check():
  if STOP or time.monotonic()>=deadline:raise BudgetExpired("complete constant preparation boundary")
 def add(p):
  q={"file":p.name,**identity(p),"temporaryOnly":True}
  rec["outputs"]=[x for x in rec["outputs"] if x["file"]!=p.name]+[q];ck()
 try:
  ps=paths_for(a)
  ids={k:identity(v) for k,v in ps.items()}
  for k,(n,h) in PINS.items():need(ids[k]=={"bytes":n,"sha256":h},"same pinned original input "+k)
  unit=read(ps["old_unit"]);gauge=read(ps["gauge"]);field=read(ps["field_cokernel"])
  need(unit["binding"]==gauge["binding"]==OLD and unit["newGaugeIdentity"]==ids["gauge"] and
   gauge["fieldCokernelIdentity"]==ids["field_cokernel"] and field["binding"]==FIELD,
   "complete chained original31-unit correction gauge identities")
  material={"programIdentity":identity(__file__),"inputIdentities":ids,
   "constantUnitSize":4318,"sourceCokernelDimension":36,"completePaidQuotientRankOverQ":12,
   "missingHeadCoordinates":[15,18,19,20],"naturalChart":"u=1/s","onlyAlgorithmicField":31}
  binding=hashlib.sha256(json.dumps(material,sort_keys=True,separators=(",",":")).encode()).hexdigest()
  rec["parameters"].update(material);rec["parameters"].update(binding=binding,secondsLimit=a.seconds,memoryMiB=a.memory_mib)
  invp=out/"invocation.json"
  if invp.exists():need(read(invp)["binding"]==binding,"same portable preparation binding")
  save(invp,{**material,"binding":binding,"paths":{k:str(v.resolve()) for k,v in ps.items()}})
  old=read(cp) if cp.exists() else None
  if old and old.get("binding")==binding and old.get("status")=="completed":
   for z in old["outputs"]:need(identity(out/z["file"])=={"bytes":z["bytes"],"sha256":z["sha256"]},"actual complete prepared output")
   old["reusedCompletePreparation"]=True;save(cp,old);print(json.dumps(old),flush=True);return 0
  rec["binding"]=binding;ck()
  J=list(map(int,unit["originalSourceRows"]));sel=read(ps["selected"]);pr=read(ps["profile"]);paid=read(ps["selected_receipt"])
  need(J==list(map(int,sel["selectedRows"]))==sorted(set(J)) and len(J)==4354,"same4354 original source rows")
  I=list(map(int,pr["originalOutputI"]));need(len(I)==len(set(I))==4354 and I==sorted(I),"same4354 original outputs")
  free=list(map(int,sel["freeRows"]))
  need(free==FREE==list(map(int,paid["selectedConstantKernelFreeOriginalRows"])) and
   paid["selectedFullConstantRankModulo31"]==4318,"paid original constant rank and free rows")
  fp=[J.index(r) for r in free];fset=set(fp);unitrows=[i for i in range(4354) if i not in fset]
  need(len(unitrows)==4318,"the true complement of36 original source free rows")
  m4=read(ps["m4"]);m5=read(ps["m5"]);co=read(ps["coefficients"])
  need(m4["binding"]==N4 and m5["binding"]==N5 and co["binding"]==FIELD and
   m4["originalSourceRows"]==m5["originalSourceRows"]==J,"same original M4/M5/F0 labels")
  E0=list(map(int,unit["secondCorrectionOutputCoordinates"]))
  E4=list(map(int,m4["normalFourOutputCoordinates"]));E5=list(map(int,m5["normalFiveOutputCoordinates"]))
  E=E0+E4+E5;need(len(E0)==1546 and len(E4)==1485 and len(E5)==1287 and len(set(E))==4318 and set(E)<=set(I),
   "complete4318 distinct original correction columns")
  rows=[]
  for r0,r4,r5 in zip(unit["originalCorrectionRows"],m4["originalNormalFourRows"],m5["originalNormalFiveRows"]):
   d=rowdict(r0,1546);d.update({1546+j:v for j,v in rowdict(r4,1485).items()})
   d.update({3031+j:v for j,v in rowdict(r5,1287).items()});rows.append(d)
  need(len(rows)==4354,"whole original correction matrix rows")
  F0=[list(map(int,r)) for r in co["constant"]]
  need(len(F0)==17 and all(len(r)==77 for r in F0) and co["all1309ConstantIdentitiesVerified"],
   "all actual original17 constant coefficients")
  whole=[q for d in range(5,0,-1) for q in itertools.combinations_with_replacement(range(11),d)]
  wi={q:i for i,q in enumerate(whole)};ei={q:i for i,q in enumerate(E)}
  mon=[(i,) for i in range(11)]+[(i,j) for i in range(11) for j in range(i,11)]
  mu=[q for d in range(4) for q in itertools.combinations_with_replacement(range(11),d)]
  proj=[i for i,q in enumerate(whole) if 1<=sum(j<=8 for j in q)<=2]
  pure=[i for i,q in enumerate(whole) if i in set(I) and all(j>=9 for j in q)]
  need(len(whole)==4367 and len(mu)==364 and len(proj)==585 and len(pure)==10,"same complete moment dictionaries")
  need(all(sum(j<=8 for j in whole[i])==4 for i in E4) and
   all(sum(j<=8 for j in whole[i])==5 for i in E5),"all original normal4/5 coordinates")
  need(field["rank"]==556 and field["allOriginalSourceProductsVerified"],"paid complete field low left kernel")
  L=nmod_mat(field["fullProjectedLeftKernel"],31)*nmod_mat(field["excludedRowKernel"],31)
  need((L.nrows(),L.ncols())==(585,26),"complete actual26 nonpure constant heads")
  lr={proj[i]:[int(L[i,j]) for j in range(26)] for i in range(585)}
  lr={i:v for i,v in lr.items() if any(v)}
  need(set(lr)<=set(I),"all actual field heads zero off I")
  G=list(map(int,gauge["newZeroGaugeOutputCoordinates"]))
  need(set(I)-set(E)==set(pure+G) and len(G)==26 and len(set(pure+G))==36,"same complete constant-kernel gauge complement")
  gd=int(nmod_mat([lr.get(i,[0]*26) for i in G],31).det())%31
  need(gd!=0 and gd==int(gauge["fieldGaugeDeterminantModulo31"])%31 and
   unit["actualUnscaledM0RankModulo31"]==1546,"actual paid26 gauge unit and M0 field full rank")
  del L
  kb=ps["kernel36"].read_bytes()
  need(kb[:8]==b"R150BC31" and struct.unpack_from("<III",kb,8)==(31,6188,36) and len(kb)==20+6188*36,
   "complete original field source kernel")
  K=[list(kb[20+36*i:20+36*(i+1)]) for i in range(6188)]
  need(all(v<31 for row in K for v in row) and all(not any(K[i]) for i in range(6188) if i+1 not in set(J)),
   "canonical actual kernel and exact selected support")
  need(all(K[free[j]-1]==[int(j==k) for k in range(36)] for j in range(36)),"full36 original free identity")
  kj=[K[r-1] for r in J];del K,kb
  rec["phase"]="same-original-constant-unit-proof";ck();check()
  km=[[0]*36 for _ in range(4318)];products=0
  for i,raw in enumerate(J):
   e=(raw-1)%17;mul=mu[(raw-1)//17];actual={};headprod=[0]*26
   for q,v in zip(mon,F0[e]):
    if not v:continue
    ix=wi[tuple(sorted(mul+q))]
    if ix in ei:actual[ei[ix]]=actual.get(ei[ix],0)+v
    if ix in lr:
     for j,a0 in enumerate(lr[ix]):headprod[j]=(headprod[j]+(v%31)*a0)%31
    need(ix not in pure,"actual pure endpoint rows vanish")
   actual={j:v for j,v in actual.items() if v}
   need(actual==rows[i],"whole original constant correction row "+str(raw))
   need(not any(headprod),"all actual26 constant left-head products at raw "+str(raw))
   for j,v in rows[i].items():
    aa=v%31
    for c,x in enumerate(kj[i]):km[j][c]=(km[j][c]+aa*x)%31
   products+=26
   if i%128==127:check()
  need(not any(any(r) for r in km),"all155448 original Mstar^T K36 field products")
  need(products==113204,"all4354x26 field left products")
  rec.update(constantUnitPrime31Proved=True,allOriginalCorrectionRowsMatched=True,
   allOriginalSourceKernelFreeCoordinatesVerified=True,all155448ConstantKernelPairingsZero=True,
   all113204ConstantLeftProductsZero=True,unitSelectionUsesOnlyPaidFieldKernel=True)
  rec["parameters"].update(constantUnitOriginalSourceRowsSHA256=vsha([J[i] for i in unitrows]),
   constantUnitRowCount=4318,actualConstantGaugeDeterminantModulo31=gd,
   constantUnitJustification="K_F=I, K^T*M=0, rank(M)=4318 imply M[J\\F,:] invertible overF31 and Q",
   unitDeterminantNumericallyRecomputed=False)
  # Only the small36x36 quotient profile is new Gaussian work.
  HF=[[int(v) for v in r] for r in unit["originalRightHandSideRows"]]
  need(len(HF)==4354 and all(len(r)==36 for r in HF),"all original HF/T rows")
  hcols=[[HF[i][j] for i in range(4354)] for j in range(36)];contents=[]
  for col in hcols:
   g=0
   for v in col:g=math.gcd(g,abs(v))
   contents.append(g or 1)
  prim=[[v//contents[j] for v in c] for j,c in enumerate(hcols)]
  rec["phase"]="actual-twelve-incoming-column-profile";ck();check()
  KP=nmod_mat(36,4354,[kj[i][j] for j in range(36) for i in range(4354)],31)
  HP=nmod_mat(4354,36,[prim[j][i]%31 for i in range(4354) for j in range(36)],31)
  pair=KP*HP;RR,rank=pair.rref();rank=int(rank);pp=pivots(RR,rank)
  need(rank<=12,"finite incoming quotient rank cannot exceed paid Qrank12")
  qprofile={"binding":binding,"originalSourceKernelIdentity":ids["kernel36"],"originalForcingIdentity":ids["old_unit"],
   "pairing36Rows":[[int(pair[i,j]) for j in range(36)] for i in range(36)],
   "originalColumnContents":[str(v) for v in contents],"rankModulo31":rank,"pivotOriginalHFandTColumns":pp,
   "completeRankOverQAlreadyProved":12,"scaledColumnsDefineSameQImage":True}
  p=out/"original-HF-T-twelve-column-field-profile.json.gz";save(p,qprofile);add(p)
  rec["parameters"].update(actualIncomingPrimitiveFieldRank=rank,selectedOriginalHFandTColumns=pp)
  del KP,HP,pair,RR,km,lr
  four=read(ps["four"]);hp=read(ps["high_profile"]);rhs=read(ps["prepared_rhs"])
  need(four["binding"]==hp["binding"]==FOUR and hp["rankModulo31"]==1736 and
   four["fourQuotientRepresentativeCoordinates"]==[15,18,19,20] and four["actualOriginalResidualRank"]==4,
   "same actual four missing quotient representatives")
  need(rhs["binding"]==PREP and rhs["originalSourceRows"]==J and rhs["all21HeadCombinationsThirdCompatible"],
   "actual complete third-compatible21 RHS")
  targets=list(map(int,four["fourQuotientRepresentativeCoordinates"]))
  Q=[[int(v) for v in rhs["primitiveIntegerRightHandSideColumns"][j]] for j in targets]
  need(all(len(c)==4354 for c in Q),"all4354 original target RHS coordinates")
  hi=list(map(int,unit["oldZeroRowPositions"]))
  need(all(not Q[j][i] for j in range(4) for i in hi),"four original target RHS high rows allzero")
  # Save the entire original constant matrix even if the convenient12-column
  # field basis is deficient. Never invent additional exact quotient columns.
  model={"binding":binding,"inputIdentities":ids,"originalSourceRows":J,"originalOutputI":I,
   "correctionOutputCoordinates":E,"oldCorrectionColumnCount":1546,"normalFourColumnCount":1485,"normalFiveColumnCount":1287,
   "sourceUnitRowPositions":unitrows,"sourceFreeRowPositions":fp,"sourceFreeOriginalRows":free,
   "originalSparseRows":[[[j,str(v)] for j,v in sorted(r.items())] for r in rows],
   "actualOriginalConstantUnitPrime31Proved":True,"allOriginalRowsAndKernelProductsVerified":True,
   "missingHeadCoordinates":targets,"originalTargetRightHandSideColumns":[[str(v) for v in c] for c in Q],
   "originalHFandTColumnContents":[str(v) for v in contents],"selectedOriginalHFandTColumns":pp,
   "actualIncomingFieldRank":rank,"completeIncomingQrank":12,
   "primitiveSelectedIncomingColumns":[[str(v) for v in prim[j]] for j in pp],
   "headScalingRule":"q_j=(R3 Z_j)/g_j; same Z_j/g_j on all lower primitive old22 cochains",
   "noHighHomogeneousDirectionsDiscarded":"Mstar spans all B0^T; selected12 span all paid quotient only when rank12 is verified"}
  mp=out/"complete-original-constant-unit-model.json.gz";save(mp,model);add(mp)
  if rank!=12:
   rec.update(status="completed-prefix",phase="quotient-profile",outcome="constant-unit-proved-quotient-field-profile-incomplete",
    fullTwelveQuotientColumnsSelected=False);code=75
  else:
   gr=[];hc=[0]*4318;un=[]
   for pos in unitrows:
    row=rows[pos];g=0
    for v in row.values():g=math.gcd(g,abs(v))
    need(g>0 and g%31,"every original unit row content prime to31")
    gr.append(g);rr={j:v//g for j,v in row.items()}
    for j,v in rr.items():hc[j]=math.gcd(hc[j],abs(v))
    un.append(rr)
   need(all(v>0 and v%31 for v in hc),"all actual unit column contents positive and prime to31")
   sparse=[[[j,str(v//hc[j])] for j,v in sorted(row.items())] for row in un]
   need(all(v%hc[j]==0 for row in un for j,v in row.items()),"all original coefficient row/column divisions exact")
   W=[prim[j] for j in pp]+Q
   meta={"binding":binding,"modelIdentity":identity(mp),"quotientProfileIdentity":identity(p),
    "unitSize":4318,"targets":16,"originalSourceUnitRows":[J[i] for i in unitrows],
    "sourceUnitRowPositions":unitrows,"originalCorrectionOutputCoordinates":E,
    "positiveRowContents":[str(v) for v in gr],"positiveColumnContents":[str(v) for v in hc],
    "scaledSparseUnitRows":sparse,"wholeOriginalRightHandSideColumns":[[str(v) for v in c] for c in W],
    "rightHandSideSignForNative":-1,
    "selectedOriginalHFandTColumns":pp,"selectedIncomingColumnContents":[str(contents[j]) for j in pp],
    "targetHeadCoordinates":targets,"targetColumnContents":["1"]*4,
    "equation":"Mstar*x=-W on4318 original unit rows; x=diag(h)^(-1)Z; diag(g)Aprime Z=-W",
    "allOriginalUnitCoefficientDivisionsVerified":True,"allWholeOriginalRowsRetained":True}
   up=out/"constant-unit-sixteen-right-hand-sides.json.gz";save(up,meta);add(up)
   rec.update(status="completed",phase="complete",outcome="complete-constant-unit-and-sixteen-rhs-prepared",
    fullTwelveQuotientColumnsSelected=True,constantUnitSize=4318,actualRightHandSides=16,
    allFourOriginalTargetsRetained=True)
   rec["parameters"].update(nativeUnitInputIdentity=identity(up),originalConstantModelIdentity=identity(mp),
    actualSparseUnitNonzeros=sum(len(r) for r in sparse),
    maximumOriginalCoefficientBits=max(abs(v).bit_length() for row in rows for v in row.values()),
    maximumScaledUnitCoefficientBits=max(abs(int(v)).bit_length() for row in sparse for j,v in row),
    maximumOriginalRightHandSideBits=[max(abs(v).bit_length() for v in c) for c in W])
   code=0
 except BudgetExpired as e:rec.update(status="checkpointed-time-budget",error=str(e));code=75
 except Exception as e:
  rec.update(status="failed",error=str(e),exceptionType=type(e).__name__);code=1
  (out/"exception.log").write_text(traceback.format_exc(),encoding="utf-8")
 finally:ck()
 print(json.dumps(rec),flush=True);return code
def main(argv):
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ("second-out","normal-four-out","normal-five-out","high-profile-out","prepared-out","rebuild-root","kernel36","selected-receipt","out"):
  ap.add_argument("--"+k,type=pathlib.Path,required=True)
 ap.add_argument("--seconds",type=float,default=60);ap.add_argument("--memory-mib",type=int,default=2048)
 a=ap.parse_args(argv);need(math.isfinite(a.seconds) and 0<a.seconds<=180 and 0<a.memory_mib<=4096,"bounded preparation")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
 return prepare(a)
if __name__=="__main__":sys.exit(main(sys.argv[1:]))
