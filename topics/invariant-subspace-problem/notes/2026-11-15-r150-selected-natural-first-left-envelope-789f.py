#!/usr/bin/env python3
"""Same original I,J: bounded characteristic-zero natural first left-jet envelope.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
Reuses the paid rational585 cokernel. No4318 solve, no new prime or Dixon digit.
All regenerable matrices and exact jets remain temporary in the live job.
"""
import argparse,gzip,hashlib,itertools,json,math,os,pathlib,resource,signal,subprocess,sys,time,traceback
sys.dont_write_bytecode=True
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
os.environ["OPENBLAS_NUM_THREADS"]="1"
os.environ["OMP_NUM_THREADS"]="1"
PIN={
 "selected_model":(814572,"0aa2d6d5c368b9885e279cd5b8e2cc7a59ba574ca161c0535193c30defe52d3d"),
 "unit_profile":(62084,"43cd638dfe13978f375490db9afdca5f318e137a384820b69bbc74b0ce48a7df"),
 "coefficients":(20582,"bfa40dd550fad408f4253484d31ceec39c4524f2f25c9fbade15911f39a776d3"),
 "first_receipt":(15594,"ef7b8a3f935eb376353a235c95d257b8f0785c7459d7c45b348b6e238390fb62"),
 "projected_input":(170401,"eb7e216cceb96ff436b506c2c677f7740269ee9b63ae0b0457c83037c7d4f220"),
 "left_kernel":(709321,"8e0e7e4d5410f7a53205a195a9880c65d3f3add2b69556d598c80b7d543eb37f")}
FIRST_BINDING="479d3295113d0e1ea0bc5e2b404a0426e5f584229a16dcfdb18aa2d6ef5dac31"
PROJECTED_BINDING="aa2ea2c1f89f43414e44a487e95e5e9609d391337fbed05a01f77bb56d36970a"
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
def save(p,x):
 p=pathlib.Path(p);q=p.with_name(p.name+".tmp")
 with (gzip.open(q,"wt",encoding="utf-8",compresslevel=1) if p.suffix==".gz" else q.open("w",encoding="utf-8")) as f:json.dump(x,f,separators=(",",":"),ensure_ascii=False)
 os.replace(q,p);return {"file":p.name,**identity(p),"temporaryOnly":True}
def zero(M):return all(not M[i,j] for i in range(M.nrows()) for j in range(M.ncols()))
def pivots(R,r):
 ans=[];j=0
 for i in range(r):
  while j<R.ncols() and not R[i,j]:j+=1
  need(j<R.ncols() and R[i,j]==1,"complete exact RREF pivot")
  ans.append(j);j+=1
 return ans
def nullspace(M):
 from flint import fmpq_mat
 R,rank=M.rref();rank=int(rank);pp=pivots(R,rank);ss=set(pp)
 ff=[j for j in range(M.ncols()) if j not in ss];Z=fmpq_mat(M.ncols(),len(ff))
 for c,f in enumerate(ff):
  Z[f,c]=1
  for i,p in enumerate(pp):Z[p,c]=-R[i,f]
 need(zero(M*Z),"original small exact nullspace product")
 return Z,rank,pp,ff
def primitive(values):
 d=1
 for v in values:d=math.lcm(d,int(v.q))
 z=[int(v.p)*(d//int(v.q)) for v in values];g=0
 for v in z:g=math.gcd(g,abs(v))
 need(g>0,"nonzero primitive column")
 sign=-1 if next(v for v in z if v)<0 else 1
 return [sign*(v//g) for v in z]
def vector_hash(values):
 h=hashlib.sha256()
 for v in values:h.update((str(v)+"\n").encode())
 return h.hexdigest()
def worker(argv):
 ap=argparse.ArgumentParser()
 ap.add_argument("--prepared",type=pathlib.Path,required=True);ap.add_argument("--out",type=pathlib.Path,required=True)
 a=ap.parse_args(argv);start=time.monotonic()
 from flint import fmpq,fmpq_mat
 data=read(a.prepared);binding=data["binding"];dcor=int(data["correctionVariables"]);n=dcor+36
 rows=[[(int(j),int(v)) for j,v in row] for row in data["originalIntegerRows"]]
 m=len(rows);need(n==data["columns"] and m==len(data["activeOriginalSourceRows"]),"complete original envelope dimensions")
 rp=a.out/"complete-left-envelope-rref.json.gz";kp=a.out/"complete-original-left-first-jets.json.gz"
 rec={"status":"running","phase":"exact-rref","binding":binding,"preparedIdentity":identity(a.prepared),"events":[]}
 def checkpoint():
  rec["elapsedSeconds"]=time.monotonic()-start;save(a.out/"left-envelope-worker-receipt.json",rec)
 checkpoint()
 if rp.exists():
  rr=read(rp);need(rr["binding"]==binding and rr["preparedIdentity"]==identity(a.prepared),"same complete RREF checkpoint")
  rank=int(rr["rank"]);pp=list(map(int,rr["pivotColumns"]));rrrows=[{int(j):fmpq(v) for j,v in row} for row in rr["nonzeroRREFRows"]]
  rec["events"].append({"reusedCompleteExactRREF":True})
 else:
  flat=[0]*(m*n)
  for i,row in enumerate(rows):
   g=0
   for j,v in row:g=math.gcd(g,abs(v))
   g=g or 1
   for j,v in row:need(v%g==0,"exact integer row content");flat[i*n+j]=v//g
  M=fmpq_mat(m,n,flat);del flat
  R,rank=M.rref();rank=int(rank);pp=pivots(R,rank);del M
  rrrows=[{j:R[i,j] for j in range(n) if R[i,j]} for i in range(rank)]
  # Save the complete exact row reduction before source reconstruction/products.
  save(rp,{"format":"isp-same-IJ-natural-first-left-envelope-rref-v1","binding":binding,
   "preparedIdentity":identity(a.prepared),"rank":rank,"pivotColumns":pp,"columns":n,
   "nonzeroRREFRows":[[[j,str(v)] for j,v in row.items()] for row in rrrows]})
  del R
 need(len(pp)==rank and pp==sorted(set(pp)) and len(rrrows)==rank,"all RREF pivot rows retained")
 for i,p in enumerate(pp):
  need(rrrows[i].get(p,0)==1 and not any(j<p for j in rrrows[i]),"actual echelon order")
  need(all(not rrrows[k].get(p,0) for k in range(rank) if k!=i),"complete reduced pivot column")
 freec=[j for j in range(36) if dcor+j not in set(pp)];dim=len(freec)
 rank0=sum(p<dcor for p in pp);rankextra=rank-rank0
 need(dim==36-rankextra and 0<=dim<=33,"paid F31 lower3 and complete projected head nullity")
 rec.update(phase="whole-original-left-jet-products",rrefRank=rank,constantCorrectionRank=rank0,
   envelopeObstructionRank=rankextra,leftHeadImageDimension=dim,completeRREF=identity(rp));checkpoint()
 if kp.exists():
  jets=read(kp);need(jets["binding"]==binding and jets["completeRREFIdentity"]==identity(rp),"same exact left jet checkpoint")
  columns=[[int(v) for v in c] for c in jets["primitiveIntegerVariableColumns"]]
  need(jets["freeHeadCoordinates"]==freec and len(columns)==dim and all(len(c)==n for c in columns),"all original jet variable columns")
  rec["events"].append({"reusedCompleteExactJetCandidates":True})
 else:
  columns=[]
  for f in freec:
   values=[fmpq(0) for _ in range(n)];values[dcor+f]=fmpq(1)
   for row,p in zip(rrrows,pp):values[p]=-row.get(dcor+f,fmpq(0))
   columns.append(primitive(values))
  save(kp,{"format":"isp-same-IJ-natural-first-left-jets-v1","binding":binding,
   "completeRREFIdentity":identity(rp),"correctionVariables":dcor,"headVariables":36,
   "freeHeadCoordinates":freec,"primitiveIntegerVariableColumns":[[str(v) for v in c] for c in columns],
   "candidateOnlyUntilMatchingWorkerReceiptCompleted":True})
 # Original unscaled row products, not only the reduced or selected pivot rows.
 for i,row in enumerate(rows):
  for c,col in enumerate(columns):
   v=sum(z*col[j] for j,z in row)
   need(v==0,"original first-left-jet product raw source %d, jet %d"%(data["activeOriginalSourceRows"][i],c))
 for c,f in enumerate(freec):
  need(columns[c][dcor+f]!=0 and all(columns[k][dcor+f]==0 for k in range(dim) if k!=c),"independent full36 head coefficient columns")
 need(data["allOmittedOriginalRowsExactlyZero"] is True and
   len(data["activeOriginalSourceRows"])+len(data["omittedOriginalSourceRows"])==4354,"all original J columns retained or exactly zero")
 rec.update(status="completed",phase="complete",all4354OriginalFirstLeftJetProductsZero=True,
   allSelectedOutputSupportVerified=True,allHeadProjectionFreeCoordinatesIndependent=True,
   completeFixedSupportEnvelopeComputed=True,selectedFirstConnectionRankOverQLowerBound=3,
   selectedFirstConnectionRankOverQUpperBound=rankextra,selectedFirstConnectionRankExactly3=rankextra==3,
   completeJetCandidates=identity(kp),completeRREF=identity(rp),
   maximumJetIntegerBits=max((abs(v).bit_length() for c in columns for v in c),default=0),
   fullOriginalFirstJetProductCoordinates=4354*dim,
   higherTransverseLeftCorrectionsRuledOut=False)
 checkpoint();print(json.dumps(rec),flush=True);return 0
def main(argv):
 ap=argparse.ArgumentParser(description=__doc__)
 for key in ["selected-model","unit-profile","first-dir","projected-dir","out"]:ap.add_argument("--"+key,type=pathlib.Path,required=True)
 ap.add_argument("--seconds",type=float,default=60);ap.add_argument("--memory-mib",type=int,default=1024)
 a=ap.parse_args(argv);need(math.isfinite(a.seconds) and 0<a.seconds<=180 and 0<a.memory_mib<=2048,"bounded new rational left envelope")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 start=time.monotonic();deadline=start+a.seconds;reserve=min(5,a.seconds/10)
 out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 paths={"selected_model":a.selected_model,"unit_profile":a.unit_profile,
  "coefficients":a.first_dir/"same-original-natural-constant-and-first-coefficients.json.gz",
  "first_receipt":a.first_dir/"selected-natural-first-connection-f31-receipt.json",
  "projected_input":a.projected_dir/"same-original-second-transverse-integer-input.json.gz",
  "left_kernel":a.projected_dir/"second-transverse-complete-left-nullspace.json.gz"}
 rec={"format":"isp-same-IJ-natural-first-rational-left-envelope-v1","status":"running","phase":"inputs",
  "old585RREFRecomputed":False,"old4318EliminationRecomputed":False,"newPrimeComputed":False,
  "newDixonDigitsComputed":0,"fullSelectedFirstSchurMatrixOverQComputed":False,
  "largeDataUploadedOrCommitted":False,"leadingUnitProved":False,"parameters":{},"events":[]}
 temps=[];exitcode=1
 def remaining():
  t=deadline-time.monotonic()-reserve
  if t<=0:raise BudgetExpired("shared exact left-envelope deadline; completed temporary stages retained")
  return t
 def checkpoint():
  rec["mathematicalElapsedSeconds"]=time.monotonic()-start
  rec["parameters"]["temporaryFiles"]=temps;save(out/"selected-natural-first-left-envelope-receipt.json",rec)
 def remember(p):
  r={"file":p.name,**identity(p),"temporaryOnly":True}
  for i,v in enumerate(temps):
   if v["file"]==r["file"]:temps[i]=r;break
  else:temps.append(r)
  return r
 def beat(phase):rec["phase"]=phase;checkpoint();print(json.dumps({"phase":phase,"elapsedSeconds":time.monotonic()-start}),flush=True);remaining()
 try:
  ids={}
  for k,p in paths.items():
   ids[k]=identity(p);need(ids[k]=={"bytes":PIN[k][0],"sha256":PIN[k][1]},"actual paid input "+k)
  material={"codeSHA256":identity(__file__)["sha256"],"inputs":ids,"originalSelectedRows":4354,
   "headSupport":"normal<=2, sameI","correctionSupport":"normal1..3, sameI, constant-coker gauge removed"}
  binding=hashlib.sha256(json.dumps(material,sort_keys=True,separators=(",",":")).encode()).hexdigest()
  rec["parameters"].update(binding=binding,inputIdentity=material,secondsLimit=a.seconds,memoryMiBPerProcess=a.memory_mib)
  prep=out/"same-original-natural-left-envelope-integer-input.json.gz"
  headp=out/"complete-same-I-characteristic-zero-left-heads.json.gz"
  if prep.exists():
   data=read(prep);need(data["binding"]==binding and headp.exists() and data["leftHeadIdentity"]==identity(headp),"same complete original prepared envelope")
   rec["events"].append({"reusedCompleteOriginalIntegerEnvelope":True})
  else:
   beat("paid-cokernel-and-original-integer-envelope")
   from flint import fmpq,fmpq_mat
   model=read(paths["selected_model"]);profile=read(paths["unit_profile"])
   co=read(paths["coefficients"]);fr=read(paths["first_receipt"]);pi=read(paths["projected_input"]);lk=read(paths["left_kernel"])
   need(co["binding"]==FIRST_BINDING==fr["parameters"]["binding"] and fr["status"]=="completed","paid natural original source binding")
   need(fr["selectedNaturalFirstConnectionRankModulo31"]==3 and fr["all1309ExactPrimitiveConstantCoefficientsVerified"] and fr["allOriginalParameterCoefficientsModulo31Verified"],"paid same-original first rank lower bound")
   need(lk["binding"]==pi["binding"]==PROJECTED_BINDING and lk["inputIdentity"]==ids["projected_input"] and lk["rank"]==556,"paid full585 rational left-kernel identity")
   F0=[list(map(int,row)) for row in co["constant"]];F1=[list(map(int,row)) for row in co["naturalFirst"]]
   need(len(F0)==len(F1)==17 and all(len(row)==77 for row in F0+F1),"all original17 natural coefficient rows")
   J=sorted(map(int,model["selectedRows"]));I=set(map(int,profile["originalOutputI"]))
   need(len(J)==len(set(J))==len(I)==4354,"same original I,J")
   whole=[q for d in range(5,0,-1) for q in itertools.combinations_with_replacement(range(11),d)];wi={q:i for i,q in enumerate(whole)}
   mult=[q for d in range(4) for q in itertools.combinations_with_replacement(range(11),d)]
   mon=[(i,) for i in range(11)]+[(i,j) for i in range(11) for j in range(i,11)]
   nd=[sum(j<=8 for j in q) for q in whole]
   need(len(whole)==4367 and len(mult)*17==6188,"complete original monomial dictionaries")
   need(all(not F0[e][j] for e in range(17) for j,q in enumerate(mon) if all(k>=9 for k in q)),"natural original F0 vanishes on pure plane")
   projected=[i for i,d in enumerate(nd) if 1<=d<=2]
   need(projected==pi["originalOutputIndices"] and len(projected)==585,"same paid full585 output order")
   L=fmpq_mat(585,29,[fmpq(v) for row in lk["leftKernelRows"] for v in row]);free=lk["freeOutputIndicesWithin585"]
   need(len(free)==29 and all(L[f,k]==int(c==k) for c,f in enumerate(free) for k in range(29)),"paid independent29 constant left coordinates")
   excluded=[i for i,r in enumerate(projected) if r not in I]
   Z,r,_,_=nullspace(fmpq_mat([[L[i,j] for j in range(29)] for i in excluded]))
   need(len(excluded)==r==3 and Z.ncols()==26,"exact sameI deleted-row kernel")
   LS=L*Z;need(all(not LS[i,j] for i in excluded for j in range(26)),"all sameI missing output coefficients zero")
   R,rr=LS.transpose().rref();need(int(rr)==26,"all26 selected rational low heads independent");gauge_local=pivots(R,26);del R
   gauge=[projected[i] for i in gauge_local];need(all(i in I for i in gauge),"constant-coker gauge uses only I outputs")
   pure=[i for i,d in enumerate(nd) if d==0 and i in I];need(len(pure)==10,"all sameI ten pure heads")
   heads={i:{} for i in pure+projected}
   for j,i in enumerate(pure):heads[i][j]=1
   for j in range(26):
    v=primitive([LS[i,j] for i in range(585)])
    for i,z in enumerate(v):
     if z:heads[projected[i]][10+j]=z
   heads={i:v for i,v in heads.items() if v};need(all(i in I for i in heads),"complete original constant left support is sameI")
   Eall=[i for i,d in enumerate(nd) if i in I and 1<=d<=3]
   need(len(Eall)==1572,"exact selected correction support count1572")
   E=[i for i in Eall if i not in set(gauge)];need(len(E)==1546,"exact26 constant-coker gauge removal")
   ei={i:j for j,i in enumerate(E)};n=len(E)+36
   active=[];omitted=[];rows=[];checks=0;nnz=0
   # Every original selected source is checked, including omitted high-normal rows.
   for ix,raw in enumerate(J):
    e=(raw-1)%17;mu=mult[(raw-1)//17];crow={};rhead=[0]*36;constant=[0]*36
    for k,q in enumerate(mon):
     a0=F0[e][k];a1=F1[e][k]
     if not a0 and not a1:continue
     outrow=wi[tuple(sorted(mu+q))]
     if a0 and outrow in ei:crow[ei[outrow]]=crow.get(ei[outrow],0)+a0
     for j,v in heads.get(outrow,{}).items():
      if a0:constant[j]+=a0*v
      if a1:rhead[j]+=a1*v
    need(not any(constant),"whole original constant left products source "+str(raw));checks+=36
    for j,v in enumerate(rhead):
     if v:crow[len(E)+j]=v
    crow={j:v for j,v in crow.items() if v}
    if sum(j<=8 for j in mu)<=2:
     active.append(raw);rows.append([[j,str(v)] for j,v in sorted(crow.items())]);nnz+=len(crow)
    else:
     need(not crow,"all omitted original high-normal source rows exactly zero");omitted.append(raw)
    if ix%256==255:remaining()
   need(checks==4354*36 and len(active)<=3383 and len(active)+len(omitted)==4354,"complete original selected row coverage")
   save(headp,{"format":"isp-same-I-complete-rational-cokernel36-integer-heads-v1","binding":binding,
    "originalOutputCount":4367,"dimensionOverQ":36,"primitiveIntegerRows":[[i,[[j,str(v)] for j,v in sorted(row.items())]] for i,row in sorted(heads.items())],
    "correctionOutputCoordinates":E,"zeroGaugeOutputCoordinates":gauge,"all4354ConstantProductsZero":True,
    "completeOriginalConstantProductCoordinates":checks,"completeSameIHeadBasisIndependent":True})
   data={"format":"isp-same-IJ-natural-first-original-envelope-input-v1","binding":binding,"leftHeadIdentity":identity(headp),
    "correctionVariables":len(E),"columns":n,"headVariables":36,"activeOriginalSourceRows":active,
    "omittedOriginalSourceRows":omitted,"originalIntegerRows":rows,"allOmittedOriginalRowsExactlyZero":True,
    "all4354OriginalConstantLeftProductsZero":True,"completeSameIHeadDimension":36,"nonzeroIntegerEntries":nnz,
    "fullCorrectionSupportCount":1572,"constantCokernelGaugeRemoved":26,
    "naturalF1PureCoefficientsZero":all(not F1[e][j] for e in range(17) for j,q in enumerate(mon) if all(k>=9 for k in q))}
   save(prep,data)
  remember(prep);remember(headp)
  rec["parameters"].update(originalSourceCount=4354,activeOriginalSourceCount=len(data["activeOriginalSourceRows"]),
   omittedOriginalSourceCount=len(data["omittedOriginalSourceRows"]),correctionVariables=data["correctionVariables"],
   headVariables=36,preparedColumns=data["columns"],originalIntegerNonzeros=data["nonzeroIntegerEntries"],
   fullCorrectionSupportCount=1572,constantCokernelGaugeRemoved=26,naturalF1PureCoefficientsZero=data["naturalF1PureCoefficientsZero"])
  rec["all4354OriginalConstantLeftProductsZero"]=True
  beat("exact-small-left-envelope")
  wr=out/"left-envelope-worker-receipt.json"
  if wr.exists() and read(wr).get("status")=="completed":
   result=read(wr);need(result["binding"]==binding and result["preparedIdentity"]==identity(prep),"same completed exact worker")
   for name,key in [("complete-left-envelope-rref.json.gz","completeRREF"),("complete-original-left-first-jets.json.gz","completeJetCandidates")]:need(identity(out/name)==result[key],"all complete exact worker arrays retained")
   rec["events"].append({"reusedCompletedExactEnvelope":True})
  else:
   log=out/"exact-left-envelope.log";cmd=[sys.executable,"-B",str(pathlib.Path(__file__).resolve()),"--worker","--prepared",str(prep),"--out",str(out)]
   started=time.monotonic()
   with log.open("a",encoding="utf-8") as f:
    proc=subprocess.Popen(cmd,stdout=f,stderr=subprocess.STDOUT,start_new_session=True)
    try:proc.wait(timeout=remaining())
    except subprocess.TimeoutExpired:
     os.killpg(proc.pid,signal.SIGKILL);proc.wait()
     rec["events"].append({"nativeWorkerStoppedAtDeadline":True,"exitCode":proc.returncode,"workerElapsedSeconds":time.monotonic()-started})
     raise BudgetExpired("uncompleted exact worker; complete preparation/RREF/jet stages remain temporary")
   rec["events"].append({"exactWorkerExitCode":proc.returncode,"workerElapsedSeconds":time.monotonic()-started})
   need(proc.returncode==0 and wr.exists(),"exact envelope worker completion: "+log.read_text(encoding="utf-8")[-1600:])
   result=read(wr);need(result["status"]=="completed" and result["binding"]==binding,"actual exact worker completed binding")
  for key in ["leftHeadImageDimension","constantCorrectionRank","envelopeObstructionRank","all4354OriginalFirstLeftJetProductsZero",
    "allSelectedOutputSupportVerified","allHeadProjectionFreeCoordinatesIndependent","completeFixedSupportEnvelopeComputed",
    "selectedFirstConnectionRankOverQLowerBound","selectedFirstConnectionRankOverQUpperBound","selectedFirstConnectionRankExactly3",
    "fullOriginalFirstJetProductCoordinates","maximumJetIntegerBits","higherTransverseLeftCorrectionsRuledOut"]:rec[key]=result[key]
  rec.update(status="completed",phase="complete");exitcode=0
 except (BudgetExpired,subprocess.TimeoutExpired) as e:rec.update(status="budget-exhausted",error=str(e));exitcode=75
 except Exception as e:
  rec.update(status="failed",error=str(e),exceptionType=type(e).__name__);(out/"exception.log").write_text(traceback.format_exc());exitcode=1
 finally:
  for name in ["same-original-natural-left-envelope-integer-input.json.gz","complete-same-I-characteristic-zero-left-heads.json.gz","complete-left-envelope-rref.json.gz","complete-original-left-first-jets.json.gz","left-envelope-worker-receipt.json"]:
   p=out/name
   if p.exists():remember(p)
  if (out/"left-envelope-worker-receipt.json").exists():
   w=read(out/"left-envelope-worker-receipt.json");rec["parameters"]["lastWorkerStatus"]={k:v for k,v in w.items() if k not in ["events"]}
  checkpoint()
 need((out/"selected-natural-first-left-envelope-receipt.json").stat().st_size<100000,"small permanent receipt")
 print(json.dumps(rec),flush=True);return exitcode
if __name__=="__main__":
 if len(sys.argv)>1 and sys.argv[1]=="--worker":sys.exit(worker(sys.argv[2:]))
 sys.exit(main(sys.argv[1:]))
