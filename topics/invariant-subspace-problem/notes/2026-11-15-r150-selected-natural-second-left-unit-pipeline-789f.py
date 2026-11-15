#!/usr/bin/env python3
"""Bounded same-I,J natural second left jets, using the actual paid first-jet family.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
Only the existing1546 correction coordinates are tried in this entry.
All large exact arrays remain temporary. No old first RREF or large NF is repeated.
"""
import argparse,gzip,hashlib,io,itertools,json,math,os,pathlib,resource,signal,subprocess,sys,time,traceback
sys.dont_write_bytecode=True
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
os.environ["OPENBLAS_NUM_THREADS"]="1"
os.environ["OMP_NUM_THREADS"]="1"
FIRST_BINDING="717dd4bfc621d633c40c01ffd0e35345828ffc98b9edf25b10989153ece49d91"
UNIT_WORKER=(16244,"a706713bb49b292c7256aa67b5cb1d75b81003175ef0b87e094e4f0efc03a8a9")
PINS={
 "prepared":(3244457,"2fabe7d680cc65e6098c4a9940d7f8e7c5eb21c0ffd57e5a168b0b348f53ba8a"),
 "heads":(633788,"3107ab8547071205466ff5b5aa2ef5f0e3ea81a976258a25184c9a0d7e709fe2"),
 "first_rref":(1515677,"3eae6c4d2b9d2c01187ea436665499555b3a8b9843bdd7ed2925b4551e0148d2"),
 "first_jets":(1701626,"2aabfc92860f66942e7a8eb3d9254ab911e7b8b2f255d40bfaa1235ed4d482fe"),
 "first_worker":(1051,"013af2e79ba1e2db0ca310dfa0593803ad84d7a9e50251f56e908b45e15874fe"),
 "coefficients":(20580,"7ab537a3c8f9a3d13b924a23f37f8d4ce4fa7621e3608920404ed0051b2fd5c1"),
 "selected":(21285,"20373c07422701e37b9226fe1fe72cb8ee1e7848df505ebbacd92cf818093c2a"),
 "profile":(21066,"044b28d717749d23a2959a02c0f8ed7570bfa19bcdff04207056f2a66d2e413d"),
 "primitive":(65159,"44350c49f9f60c61427b7278bf7f3d24b6cb2e6583848a113b03bb109516d4fe")}
PRIMITIVE_RAW_SHA="fa2e5d80e9fbd47e1e237ae60c548900a15922a0543e02be77fc972dc52944b3"
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
    with io.TextIOWrapper(gz,encoding="utf-8",newline="\n") as f:json.dump(v,f,separators=(",",":"),sort_keys=True)
 else:
  b=json.dumps(v,separators=(",",":"),sort_keys=True).encode()
  need(len(b)<100000,"only small uncompressed receipts/metadata")
  q.write_bytes(b)
 os.replace(q,p);return {"file":p.name,**identity(p),"temporaryOnly":True}
def pivots(R,rank):
 ans=[]
 for i in range(int(rank)):
  j=next((j for j in range(R.ncols()) if R[i,j]),None)
  need(j is not None and R[i,j]==1,"complete normalized RREF pivot");ans.append(j)
 need(ans==sorted(set(ans)),"strict RREF pivot order");return ans
def primitive_q(values):
 den=1
 for v in values:den=math.lcm(den,int(v.q))
 z=[int(v.p)*(den//int(v.q)) for v in values];g=0
 for v in z:g=math.gcd(g,abs(v))
 need(g>0,"nonzero exact kernel column")
 sign=-1 if next(v for v in z if v)<0 else 1
 return [sign*(v//g) for v in z]
def input_paths(a):
 old=a.first_out/"left-envelope"
 return {"prepared":old/"same-original-natural-left-envelope-integer-input.json.gz",
  "heads":old/"complete-same-I-characteristic-zero-left-heads.json.gz",
  "first_rref":old/"complete-left-envelope-rref.json.gz",
  "first_jets":old/"complete-original-left-first-jets.json.gz",
  "first_worker":old/"left-envelope-worker-receipt.json",
  "coefficients":a.rebuild_root/"rebuilt-first"/"same-original-natural-constant-and-first-coefficients.json.gz",
  "selected":a.rebuild_root/"rebuilt-inputs"/"same-selected-original-source-indices.json",
  "profile":a.rebuild_root/"rebuilt-inputs"/"same-selected-original-output-indices.json",
  "primitive":a.primitive_equations}
def load_inv(p):
 inv=read(p)
 for k,v in inv["paths"].items():need(identity(v)==inv["inputIdentities"][k],"all same paid input bytes: "+k)
 need(identity(__file__)["sha256"]==inv["programIdentity"]["sha256"],"same new second-entry program")
 return inv
def completed_cache(path,binding):
 if not path.exists():return None
 v=read(path);need(v["binding"]==binding,"same actual stage binding")
 if v.get("status")!="completed":return None
 for r in v.get("outputs",[]):need(identity(path.parent/r["file"])=={"bytes":r["bytes"],"sha256":r["sha256"]},"actual complete stage output "+r["file"])
 return v
def prepare_worker(invpath,out):
 from flint import fmpq_mat,nmod_mat
 inv=load_inv(invpath);bind=inv["binding"];out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True)
 cp=out/"prepare-second-left-receipt.json";cached=completed_cache(cp,bind)
 if cached:print(json.dumps({"status":"completed","reused":True,"outcome":cached["outcome"]}),flush=True);return 0
 start=time.monotonic();rec={"status":"running","phase":"paid-first-family","binding":bind,"outputs":[],"parameters":{}}
 def checkpoint():
  rec["elapsedSeconds"]=time.monotonic()-start;save(cp,rec)
 checkpoint();paths=inv["paths"]
 old=read(paths["prepared"]);heads=read(paths["heads"]);rr=read(paths["first_rref"]);jj=read(paths["first_jets"]);wr=read(paths["first_worker"])
 need(wr["status"]=="completed" and wr["selectedFirstConnectionRankExactly3"] and
  wr["all4354OriginalFirstLeftJetProductsZero"] and wr["allHeadProjectionFreeCoordinatesIndependent"],"actual complete exact first proof")
 need(old["binding"]==heads["binding"]==rr["binding"]==jj["binding"]==wr["binding"]==FIRST_BINDING,"all paid first semantic bindings")
 need(rr["rank"]==1549 and rr["columns"]==1582 and old["correctionVariables"]==1546 and old["headVariables"]==36,"same first complete dimensions")
 need(jj["completeRREFIdentity"]==inv["inputIdentities"]["first_rref"] and wr["completeJetCandidates"]==inv["inputIdentities"]["first_jets"],"actual full RREF and first candidates")
 pp=list(map(int,rr["pivotColumns"]));F=[j-1546 for j in pp if j>=1546];free=list(map(int,jj["freeHeadCoordinates"]))
 need(pp[:1546]==list(range(1546)) and len(F)==3 and len(free)==33 and sorted(F+free)==list(range(36)),"complete head complement and first-kernel free coordinates")
 cols=[[int(v) for v in c] for c in jj["primitiveIntegerVariableColumns"]]
 need(len(cols)==33 and all(len(c)==1582 for c in cols),"all33 exact first variable columns")
 X=[[cols[c][i] for c in range(33)] for i in range(1546)]
 C=[[cols[c][1546+i] for c in range(33)] for i in range(36)]
 need(all(C[f][c]!=0 and all(C[f][k]==0 for k in range(33) if k!=c) for c,f in enumerate(free)),"full33 independent original first heads")
 E=list(map(int,heads["correctionOutputCoordinates"]));need(len(E)==len(set(E))==1546,"same correction output coordinates")
 J=sorted(map(int,read(paths["selected"])["selectedRows"]));I=set(map(int,read(paths["profile"])["originalOutputI"]))
 need(len(J)==len(set(J))==len(I)==4354 and set(E)<=I,"same original selected I,J")
 active=list(map(int,old["activeOriginalSourceRows"]));omitted=list(map(int,old["omittedOriginalSourceRows"]))
 need(len(active)==2618 and len(omitted)==1736 and sorted(active+omitted)==J and
  old["allOmittedOriginalRowsExactlyZero"] and old["all4354OriginalConstantLeftProductsZero"],"all original first-envelope rows")
 firstrows={raw:{int(j):int(v) for j,v in row} for raw,row in zip(active,old["originalIntegerRows"])}
 raw=gzip.decompress(pathlib.Path(paths["primitive"]).read_bytes())
 need(hashlib.sha256(raw).hexdigest()==PRIMITIVE_RAW_SHA,"full raw primitive integer polynomial model")
 equations=json.loads(raw)["equations"];co=read(paths["coefficients"]);Fs=[[],[],[]]
 need(len(equations)==17 and all(len(r)==77 for r in equations),"complete original17 by77 parameter coefficients")
 for e,row in enumerate(equations):
  r=[[],[],[]]
  for j,pol in enumerate(row):
   v=list(map(int,pol));need(v,"nonempty original coefficient polynomial")
   if e>=11 and j<11:
    need(not any(v),"original Gamma linear coefficients exactly zero")
    for k in range(3):r[k].append(0)
    continue
   d=10 if e<11 and j<11 else 0 if e<11 else 5
   need(not any(v[d+1:]),"same natural-u degree and no coefficient beyond it")
   for k in range(3):r[k].append(v[d-k] if d>=k and d-k<len(v) else 0)
  for k in range(3):Fs[k].append(r[k])
 need(Fs[0]==[list(map(int,r)) for r in co["constant"]] and Fs[1]==[list(map(int,r)) for r in co["naturalFirst"]],"all1309 paid natural constant and first coefficients exactly match")
 mon=[(i,) for i in range(11)]+[(i,j) for i in range(11) for j in range(i,11)]
 mult=[q for d in range(4) for q in itertools.combinations_with_replacement(range(11),d)]
 whole=[q for d in range(5,0,-1) for q in itertools.combinations_with_replacement(range(11),d)];wi={q:i for i,q in enumerate(whole)}
 hrows={int(i):{int(j):int(v) for j,v in r} for i,r in heads["primitiveIntegerRows"]}
 need(set(hrows)<=I and heads["all4354ConstantProductsZero"] and heads["completeSameIHeadBasisIndependent"],"paid whole original constant left basis")
 l0={i:[sum(v*C[j][c] for j,v in row.items()) for c in range(33)] for i,row in hrows.items()}
 l1={i:X[k] for k,i in enumerate(E)}
 forcing=out/"complete-original-second-left-forcing.json.gz"
 if forcing.exists():
  data=read(forcing);need(data["binding"]==bind and data["inputIdentities"]==inv["inputIdentities"],"same whole original second forcing")
  rec["parameters"]["reusedCompleteOriginalSecondForcing"]=True
 else:
  rows0=[];rhs=[];counts=[0,0]
  for rawid in J:
   row=firstrows.get(rawid,{})
   rows0.append([[j,str(v)] for j,v in sorted(row.items()) if j<1546])
   v=[row.get(1546+f,0) for f in F]+[0]*33
   e=(rawid-1)%17;mu=mult[(rawid-1)//17]
   for k,q in enumerate(mon):
    a1=Fs[1][e][k];a2=Fs[2][e][k]
    if not a1 and not a2:continue
    ix=wi[tuple(sorted(mu+q))]
    if a1 and ix in l1:
     x=l1[ix]
     for c in range(33):v[3+c]+=a1*x[c]
     counts[0]+=33
    if a2 and ix in l0:
     x=l0[ix]
     for c in range(33):v[3+c]+=a2*x[c]
     counts[1]+=33
   rhs.append([str(x) for x in v])
  data={"format":"isp-selected-second-left-forcing-v1","binding":bind,"inputIdentities":inv["inputIdentities"],
   "correctionVariables":1546,"rhsColumns":36,"originalSourceRows":J,"originalCorrectionRows":rows0,
   "originalRightHandSideRows":rhs,"headComplementCoordinates":F,"firstKernelFreeHeadCoordinates":free,
   "oldZeroRowPositions":[J.index(rawid) for rawid in omitted],"oldFirstCoreBinding":FIRST_BINDING,
   "correctionNormalDegreeAtMost":3,"all4354OriginalSecondForcingRowsConstructed":True,
   "allOriginalNaturalF2CoefficientsTakenFromPinnedPrimitive":True,"oldFirstKernelFreedomDimension":33,
   "lastCorrectionKernelFreedomDimension":36,"secondFamilyFormula":"lambda0=Lambda*C*c; lambda1=E*X*c+Lambda*F*t+Lambda*C*y; lambda2=E*x2prime+E*X*y+Lambda*e",
   "firstAndSecondMatrixTimesHeadProducts":counts}
  save(forcing,data)
 rec["outputs"]=[{"file":forcing.name,**identity(forcing)}];rec["phase"]="old-zero-row-restriction";checkpoint()
 hp=out/"complete-old-zero-row-second-head-restriction.json.gz"
 if hp.exists():
  high=read(hp);need(high["binding"]==bind and high["forcingIdentity"]==identity(forcing),"same actual old-zero-row restriction")
 else:
  highrows=[[int(v) for v in data["originalRightHandSideRows"][i][3:]] for i in data["oldZeroRowPositions"]]
  H=fmpq_mat(len(highrows),33,[v for r in highrows for v in r]);R,rank=H.rref();rank=int(rank);ph=pivots(R,rank)
  high={"binding":bind,"forcingIdentity":identity(forcing),"rows":len(highrows),"columns":33,"rankOverQ":rank,
   "pivotColumns":ph,"nonzeroRREFRows":[[[j,str(R[i,j])] for j in range(33) if R[i,j]] for i in range(rank)],
   "sameSupportHeadDimensionUpperBound":33-rank,"onlyNecessaryRestrictionForCorrectionNormalDegreeAtMost3":True}
  save(hp,high);del H,R
 rec["outputs"].append({"file":hp.name,**identity(hp)});rec["oldZeroRowRestrictionRankOverQ"]=high["rankOverQ"]
 rec["sameSupportHeadDimensionUpperBoundFromOldZeroRows"]=high["sameSupportHeadDimensionUpperBound"]
 if high["rankOverQ"]>9:
  rec.update(status="completed",phase="complete",outcome="same-support-obstruction-before-unit-solve",
   unitSolveNeededForCurrentSupport=False,sourceSupportExpansionNeeded=True,
   fullSelectedSecondConnectionComputed=False,nextCorrectionNormalDegree=4);checkpoint();print(json.dumps(rec),flush=True);return 0
 rec["phase"]="actual-primitive-M0-unit-profile";checkpoint()
 up=out/"second-left-m0-unit-input.json.gz"
 if up.exists():
  unit=read(up);need(unit["binding"]==bind and unit["forcingIdentity"]==identity(forcing),"same complete true M0 unit input")
  rank=unit["actualPrimitiveM0RankModulo31"];det=unit["unitDeterminantModulo31"]
 else:
  rows=[[(int(j),int(v)) for j,v in row] for row in data["originalCorrectionRows"]];d=1546
  nonzero=[i for i,row in enumerate(rows) if row];m=len(nonzero);local={i:k for k,i in enumerate(nonzero)}
  gs=[];flat=[0]*(d*m)
  for i,row in enumerate(rows):
   g=0
   for j,v in row:g=math.gcd(g,abs(v))
   g=g or 1;gs.append(g)
   for j,v in row:need(v%g==0,"exact coefficient-only row content");flat[j*m+local[i]]=(v//g)%31
  MM=nmod_mat(d,m,flat,31);del flat
  RR,rank=MM.rref();rank=int(rank);pr=[nonzero[k] for k in pivots(RR,rank)];del MM,RR
  if rank!=1546:
   rec.update(status="completed",phase="complete",outcome="mod31-unit-profile-incomplete",
    actualPrimitiveM0RankModulo31=rank,exactM0RankOverQAlreadyPaid=1546,
    fullSelectedSecondConnectionComputed=False,unitSolveNeededForCurrentSupport=False)
   checkpoint();print(json.dumps(rec),flush=True);return 0
  chosen=[{j:v//gs[i] for j,v in rows[i]} for i in pr]
  U31=nmod_mat(d,d,[row.get(j,0)%31 for row in chosen for j in range(d)],31)
  del chosen
  det=int(U31.det())%31;del U31
  need(det!=0,"actual scaled original M0 unit determinant modulo31")
  unit={**data,"format":"isp-selected-second-left-unit-input-v1","forcingIdentity":identity(forcing),
   "rowCoefficientContents":[str(g) for g in gs],"selectedUnitRowIndices":pr,"unitPrime":31,
   "unitDeterminantModulo31":det,"actualPrimitiveM0RankModulo31":rank,
   "rightHandSidesMustBeRowDividedBySameContent":True}
  save(up,unit)
 rec["outputs"].append({"file":up.name,**identity(up)})
 rec.update(status="completed",phase="complete",outcome="ready-for-actual-unit-solve",unitSolveNeededForCurrentSupport=True,
  actualPrimitiveM0RankModulo31=rank,actualUnitDeterminantModulo31=det,fullSelectedSecondConnectionComputed=False,
  oldFirstKernelFreedomRetained=True,allOriginalNaturalSecondForcingConstructed=True)
 checkpoint();print(json.dumps(rec),flush=True);return 0
def finish_worker(invpath,out,preparedir,unitdir):
 from flint import fmpq,fmpq_mat
 inv=load_inv(invpath);bind=inv["binding"];out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True)
 prep=pathlib.Path(preparedir);unitdir=pathlib.Path(unitdir);cp=out/"second-left-full-products-receipt.json"
 cached=completed_cache(cp,bind)
 if cached:print(json.dumps({"status":"completed","reused":True,"outcome":cached["outcome"]}),flush=True);return 0
 start=time.monotonic();rec={"status":"running","phase":"complete-unit-solution","binding":bind,"outputs":[],"parameters":{}}
 def checkpoint():
  rec["elapsedSeconds"]=time.monotonic()-start;save(cp,rec)
 checkpoint()
 up=prep/"second-left-m0-unit-input.json.gz";unit=read(up)
 sp=unitdir/"complete-m0-unit-solution.json.gz";sol=read(sp);ur=read(unitdir/"m0-unit-solve-receipt.json")
 need(unit["binding"]==sol["binding"]==ur["binding"]==bind and sol["inputIdentity"]==identity(up),"same complete actual original unit solve")
 sid=identity(sp);uid=identity(up)
 need(ur["status"]=="completed" and ur["all1546OriginalUnitRowsVerified"] and ur["originalUnitProductCoordinates"]==1546*36 and
  ur["candidateIdentity"]==sid,"all original unscaled unit products paid")
 D=list(map(int,sol["denominators"]));N=[[int(x) for x in c] for c in sol["numeratorColumns"]]
 need(len(D)==len(N)==36 and all(d>0 for d in D) and all(len(c)==1546 for c in N),"all36 complete rational unit solutions")
 rows=[[(int(j),int(v)) for j,v in row] for row in unit["originalCorrectionRows"]]
 rhs=[[int(v) for v in row] for row in unit["originalRightHandSideRows"]];J=unit["originalSourceRows"];selected=set(unit["selectedUnitRowIndices"])
 need(len(rows)==len(rhs)==len(J)==4354,"all original source rows in residual")
 residual=[];rid=[]
 rec["phase"]="whole-original-residual-columns";checkpoint()
 for c in range(36):
  p=out/("original-residual-column-%02d.json.gz"%c)
  if p.exists():
   rc=read(p);need(rc["binding"]==bind and rc["unitSolutionIdentity"]==sid and rc["column"]==c and
    rc["unitInputIdentity"]==uid,"same full residual column checkpoint")
   v=list(map(int,rc["values"]));need(len(v)==4354 and rc["all1546UnitResidualEntriesZero"],"complete residual column")
  else:
   v=[D[c]*rhs[i][c]+sum(a*N[c][j] for j,a in row) for i,row in enumerate(rows)]
   need(all(v[i]==0 for i in selected),"all actual original selected unit-row residuals zero")
   rc={"binding":bind,"unitSolutionIdentity":sid,"unitInputIdentity":uid,"column":c,
    "denominator":str(D[c]),"values":[str(x) for x in v],"all1546UnitResidualEntriesZero":True,
    "all4354OriginalResidualEntriesComputed":True};save(p,rc)
  residual.append(v);rid.append({"file":p.name,**identity(p)})
  rec["completedOriginalResidualColumns"]=c+1;rec["outputs"]=rid[:];checkpoint()
 sr=out/"complete-small-second-residual-rref.json.gz"
 if sr.exists():
  rr=read(sr);need(rr["binding"]==bind and rr["residualColumnIdentities"]==rid,"same complete small residual RREF")
  rank=int(rr["rank"]);pp=list(map(int,rr["pivotColumns"]));rrows=[{int(j):fmpq(v) for j,v in row} for row in rr["nonzeroRREFRows"]]
 else:
  inds=[i for i in range(4354) if any(residual[c][i] for c in range(36))]
  S=fmpq_mat(len(inds),36,[residual[c][i] for i in inds for c in range(36)])
  R,rank=S.rref();rank=int(rank);pp=pivots(R,rank)
  rr={"binding":bind,"residualColumnIdentities":rid,"rank":rank,"pivotColumns":pp,"nonzeroOriginalRowIndices":inds,
   "nonzeroRREFRows":[[[j,str(R[i,j])] for j in range(36) if R[i,j]] for i in range(rank)]}
  save(sr,rr);rrows=[{j:R[i,j] for j in range(36) if R[i,j]} for i in range(rank)];del S,R
 need(pp[:3]==[0,1,2],"actual complete first-head complement residual rank3")
 free=[j for j in range(36) if j not in set(pp)];dim=len(free)
 need(dim==36-rank and 0<=dim<=24 and all(f>=3 for f in free),"paid second F31 lower9 and complete same-support head count")
 rec.update(phase="true-original-second-jets",smallResidualRank=rank,secondHeadImageDimension=dim,
  firstHeadComplementResidualRank=3,all4354ResidualRowsRetained=True,completeSmallResidualRREF=identity(sr));rec["outputs"]=rid+[{"file":sr.name,**identity(sr)}];checkpoint()
 candidates=[];verified=[]
 for c,f in enumerate(free):
  p=out/("complete-original-second-left-jet-%02d.json.gz"%c);vp=out/("verified-second-left-jet-%02d.json"%c)
  if p.exists():
   cand=read(p);need(cand["binding"]==bind and cand["smallResidualRREFIdentity"]==identity(sr) and
    cand["unitSolutionIdentity"]==sid and cand["freeResidualCoordinate"]==f,"same complete second candidate")
   gamma=list(map(int,cand["primitiveResidualKernel"]));x2=list(map(int,cand["secondCorrectionVariables"]))
   t=list(map(int,cand["threeFirstHeadComplementCoefficients"]));h=list(map(int,cand["firstHeadKernelCoefficients"]))
  else:
   vals=[fmpq(0) for _ in range(36)];vals[f]=fmpq(1)
   for row,piv in zip(rrows,pp):vals[piv]=-row.get(f,fmpq(0))
   gamma=primitive_q(vals)
   x2=[sum(N[k][i]*gamma[k] for k in range(36)) for i in range(1546)]
   t=[D[k]*gamma[k] for k in range(3)];h=[D[3+k]*gamma[3+k] for k in range(33)]
   cand={"binding":bind,"smallResidualRREFIdentity":identity(sr),"unitSolutionIdentity":sid,
    "freeResidualCoordinate":f,"primitiveResidualKernel":[str(v) for v in gamma],
    "secondCorrectionVariables":[str(v) for v in x2],"threeFirstHeadComplementCoefficients":[str(v) for v in t],
    "firstHeadKernelCoefficients":[str(v) for v in h],"headComplementCoordinates":unit["headComplementCoordinates"],
    "oldFirstHeadAndCorrectionSourceIdentities":{k:inv["inputIdentities"][k] for k in ["heads","first_jets"]},
    "candidateOnlyUntilMatchingVerifiedReceipt":True};save(p,cand)
  need(len(gamma)==36 and len(x2)==1546 and len(t)==3 and len(h)==33 and h[f-3]!=0 and
   all(gamma[g]==0 for g in free if g!=f),"independent full33 c projection, not only residual nullity")
  cid=identity(p)
  if vp.exists():
   vr=read(vp);need(vr["binding"]==bind and vr["candidateIdentity"]==cid and vr["all4354OriginalSecondProductsZero"],"same verified whole original second candidate")
  else:
   z=t+h
   for i,row in enumerate(rows):
    value=sum(a*x2[j] for j,a in row)+sum(rhs[i][k]*z[k] for k in range(36))
    need(value==0,"original second left product raw source %s, candidate %s"%(J[i],c))
   vr={"binding":bind,"candidateIdentity":cid,"all4354OriginalSecondProductsZero":True,"originalProductCoordinates":4354,
    "independentHeadFreeCoordinate":f-3,"independentHeadFreeValue":str(h[f-3])};save(vp,vr)
  rec["maximumCandidateVariableIntegerBits"]=max(rec.get("maximumCandidateVariableIntegerBits",0),max((abs(v).bit_length() for v in x2+t+h),default=0))
  candidates.append({"file":p.name,**cid});verified.append({"file":vp.name,**identity(vp)})
  rec["completedOriginalSecondHeadCandidates"]=c+1;rec["outputs"]=rid+[{"file":sr.name,**identity(sr)}]+candidates+verified;checkpoint()
 rec.update(status="completed",phase="complete",outcome="same-selected-second-rank-nine-proved" if dim==24 else "restricted-second-left-support-only",
  selectedSecondConnectionRankOverQLowerBound=9,selectedSecondConnectionRankOverQUpperBound=33-dim,
  selectedSecondConnectionRankExactly9=dim==24,allConstructedOriginalSecondJetsVerified=bool(dim),
  all4354OriginalSecondLeftProductsZero=bool(dim),allHeadProjectionFreeCoordinatesIndependent=True,
  fullOriginalSecondJetProductCoordinates=4354*dim,completeFixedSupportSecondEnvelopeComputed=True,
  completeSelectedSecondHeadSpaceProved=dim==24,higherCorrectionSupportExcludedAsPremise=False,
  oldFirstKernelFreedomRetained=True,oldFirstKernelFreedomDimension=33,lastCorrectionKernelFreedomDimension=36,
  sourceSupportExpansionNeeded=dim<24,correctionNormalDegreeAtMost=3,
  firstFamilyContinuationFormula="lambda0=Lambda*C*c; lambda1=E*X*c+Lambda*F*t+Lambda*C*y; lambda2=E*x2prime+E*X*y+Lambda*e",
  leadingUnitProved=False,largeDataUploadedOrCommitted=False)
 checkpoint();print(json.dumps({k:v for k,v in rec.items() if k!="outputs"}),flush=True);return 0
def main(argv):
 ap=argparse.ArgumentParser(description=__doc__)
 for key in ["first-out","rebuild-root","primitive-equations","unit-worker","out"]:ap.add_argument("--"+key,type=pathlib.Path,required=True)
 ap.add_argument("--seconds",type=float,default=300);ap.add_argument("--memory-mib",type=int,default=2048)
 a=ap.parse_args(argv);need(math.isfinite(a.seconds) and 0<a.seconds<=600 and 0<a.memory_mib<=4096,"bounded explicit new second entry")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 start=time.monotonic();deadline=start+a.seconds;reserve=min(5,a.seconds/20);out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 rec={"format":"isp-selected-natural-second-left-unit-pipeline-v1","status":"running","phase":"pinned-actual-first-inputs",
  "oldFirstRREFRecomputed":False,"old585RREFRecomputed":False,"oldLargeNormalFormsRecomputed":False,"newDixonSourceDigitsComputed":0,
  "newOriginalRankPrimeComputed":False,"leadingUnitProved":False,"largeDataUploadedOrCommitted":False,"parameters":{},"events":[]}
 code=1
 def remaining():
  t=deadline-time.monotonic()-reserve
  if t<=0:raise BudgetExpired("shared300-second exact second-left clock; actual completed stages retained")
  return t
 def checkpoint():
  rec["mathematicalElapsedSeconds"]=time.monotonic()-start;save(out/"selected-natural-second-left-unit-pipeline-receipt.json",rec)
 def run(name,cmd,receipt_path):
  rec["phase"]=name;checkpoint();t0=time.monotonic()
  with (out/(name+".log")).open("a",encoding="utf-8") as log:
   p=subprocess.Popen(cmd,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
   available=remaining();grace=min(20.0,max(.5,available/8)) if name=="unit-solve" else .25
   try:p.wait(timeout=max(.1,available-grace))
   except subprocess.TimeoutExpired:
    os.killpg(p.pid,signal.SIGTERM)
    try:p.wait(timeout=grace)
    except subprocess.TimeoutExpired:os.killpg(p.pid,signal.SIGKILL);p.wait()
    rec["events"].append({"phase":name,"deadlineStoppedWorker":True,"exitCode":p.returncode,"elapsedSeconds":time.monotonic()-t0})
    raise BudgetExpired("same "+name+" incomplete; no unreturned native result claimed")
  rec["events"].append({"phase":name,"exitCode":p.returncode,"elapsedSeconds":time.monotonic()-t0})
  if p.returncode==75:raise BudgetExpired("same "+name+" safely checkpointed")
  need(p.returncode==0 and receipt_path.exists(),"actual "+name+" failed: "+(out/(name+".log")).read_text(encoding="utf-8",errors="replace")[-1800:])
  r=read(receipt_path);need(r["status"]=="completed","actual "+name+" completion")
  return r
 try:
  paths=input_paths(a);ids={}
  for k,p in paths.items():
   ids[k]=identity(p);need(ids[k]=={"bytes":PINS[k][0],"sha256":PINS[k][1]},"actual paid first input "+k)
  wid=identity(a.unit_worker);need(wid=={"bytes":UNIT_WORKER[0],"sha256":UNIT_WORKER[1]},"frozen exact unit-solve worker")
  material={"programIdentity":identity(__file__),"unitWorkerIdentity":wid,"inputIdentities":ids,
   "sameCorrectionVariables":1546,"rhsColumns":36,"rowProfilePrime":31,"firstCoreBinding":FIRST_BINDING}
  bind=hashlib.sha256(json.dumps(material,sort_keys=True,separators=(",",":")).encode()).hexdigest()
  inv={**material,"binding":bind,"paths":{k:str(p.resolve()) for k,p in paths.items()}}
  ip=out/"invocation.json";save(ip,inv)
  rec["parameters"].update(binding=bind,inputIdentities=ids,programIdentity=material["programIdentity"],unitWorkerIdentity=wid,
   secondsLimit=a.seconds,memoryMiBPerProcess=a.memory_mib,sourceSupport="same original I; lambda2 normal<=3; all4354 J rows",
   oldFirstKernelFreedomDimension=33,lastCorrectionKernelFreedomDimension=36)
  checkpoint()
  prep=out/"prepared";prp=prep/"prepare-second-left-receipt.json"
  pr=completed_cache(prp,bind)
  if pr:rec["events"].append({"reusedCompletePreparation":True})
  else:pr=run("prepare",[sys.executable,"-B",str(pathlib.Path(__file__).resolve()),"--prepare-worker",str(ip),str(prep)],prp)
  rec["parameters"]["preparation"]={k:v for k,v in pr.items() if k not in ["outputs","parameters"]}
  rec["parameters"]["preparationOutputs"]=pr.get("outputs",[])
  if pr["outcome"]!="ready-for-actual-unit-solve":
   rec.update(status="completed",phase="complete",outcome=pr["outcome"],fullSelectedSecondConnectionComputed=False,
    sourceSupportExpansionNeeded=pr.get("sourceSupportExpansionNeeded",False),selectedSecondConnectionRankExactly9=False)
   code=0
  else:
   unitdir=out/"unit-solve";urp=unitdir/"m0-unit-solve-receipt.json";up=prep/"second-left-m0-unit-input.json.gz"
   ur=read(urp) if urp.exists() else None
   if ur and ur.get("status")=="completed":
    need(ur["binding"]==bind and ur["inputIdentity"]==identity(up) and ur["all1546OriginalUnitRowsVerified"] and
     ur["candidateIdentity"]==identity(unitdir/"complete-m0-unit-solution.json.gz"),"same actual completed whole unit solve")
    rec["events"].append({"reusedCompleteExactUnitSolution":True})
   else:
    ur=run("unit-solve",[sys.executable,"-B",str(a.unit_worker.resolve()),"--input",str(up),"--out",str(unitdir)],urp)
   rec["parameters"]["unitSolve"]={k:v for k,v in ur.items() if k not in ["parameters"]}
   finish=out/"full-products";frp=finish/"second-left-full-products-receipt.json"
   fr=completed_cache(frp,bind)
   if fr:rec["events"].append({"reusedCompleteWholeOriginalSecondProducts":True})
   else:fr=run("full-products",[sys.executable,"-B",str(pathlib.Path(__file__).resolve()),"--finish-worker",str(ip),str(finish),str(prep),str(unitdir)],frp)
   rec["parameters"]["actualFullProductReceipt"]=identity(frp)
   rec["parameters"]["fullProductTemporaryOutputs"]=fr.get("outputs",[])
   for k,v in fr.items():
    if k not in ["outputs","parameters","binding","phase","elapsedSeconds"]:rec[k]=v
   rec["phase"]="complete";code=0
 except BudgetExpired as e:rec.update(status="checkpointed-time-budget",outcome="checkpointed-time-budget",error=str(e));code=75
 except Exception as e:
  rec.update(status="failed-or-incomplete",outcome="failed-or-incomplete",error=str(e),exceptionType=type(e).__name__)
  (out/"exception.log").write_text(traceback.format_exc(),encoding="utf-8");code=1
 finally:
  rec["parameters"]["temporaryCheckpointDirectories"]={"preparation":"prepared","completeUnitSolution":"unit-solve","fullOriginalResidualsAndJets":"full-products"}
  for folder,name in [("prepared","prepare-second-left-receipt.json"),("unit-solve","m0-unit-solve-receipt.json"),("full-products","second-left-full-products-receipt.json")]:
   p=out/folder/name
   if p.exists():
    r=read(p);rec["parameters"][folder+"LastActualStatus"]={k:v for k,v in r.items() if k not in ["outputs","parameters","paths"]}
  checkpoint()
 print(json.dumps(rec),flush=True);return code
if __name__=="__main__":
 if len(sys.argv)>1 and sys.argv[1]=="--prepare-worker":sys.exit(prepare_worker(sys.argv[2],sys.argv[3]))
 if len(sys.argv)>1 and sys.argv[1]=="--finish-worker":sys.exit(finish_worker(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5]))
 sys.exit(main(sys.argv[1:]))
