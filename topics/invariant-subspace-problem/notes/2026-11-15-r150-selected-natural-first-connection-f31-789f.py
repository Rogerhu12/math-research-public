#!/usr/bin/env python3
"""Same selected natural-u first connection, from original integer coefficients.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
Only small coker construction and original products; no old large NF or Dixon.
All reproducible arrays remain temporary; only this source and small receipt persist.
"""
import argparse,gzip,hashlib,itertools,json,os,pathlib,re,resource,signal,struct,subprocess,sys,time,traceback
sys.dont_write_bytecode=True
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
os.environ["OPENBLAS_NUM_THREADS"]="1"
os.environ["OMP_NUM_THREADS"]="1"
PIN={
 "point_model":(87459,"97d31570a0bd99d33066fc6ea47984203b2964521ceeb50920f0a49dd3bb8074"),
 "selected_model":(814572,"0aa2d6d5c368b9885e279cd5b8e2cc7a59ba574ca161c0535193c30defe52d3d"),
 "unit_profile":(62084,"43cd638dfe13978f375490db9afdca5f318e137a384820b69bbc74b0ce48a7df"),
 "kernel36":(222788,"c008e57b7a7e80312f8ba292bb24241d53bb59d4c57b2a8d07ec1017b9de0744"),
 "projected_input":(170401,"eb7e216cceb96ff436b506c2c677f7740269ee9b63ae0b0457c83037c7d4f220"),
 "native_model":(128145,"291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6"),
 "pure_matrices":(88134,"1569efd597d0b6b3e746d6f4180371fd8c25f629a09c0da78d39a8a02850aa42"),
}
PRIMITIVE=(65159,"44350c49f9f60c61427b7278bf7f3d24b6cb2e6583848a113b03bb109516d4fe")
PRIMITIVE_RAW_SHA="fa2e5d80e9fbd47e1e237ae60c548900a15922a0543e02be77fc972dc52944b3"
HIST_REF="8c6304e273e64b0544d3dd58bc0e48a672a87c36"
HIST_PATH="topics/invariant-subspace-problem/notes/r150-first-padic-residual-789f/original-primitive-integer-equations.json.gz"
class BudgetExpired(Exception):pass
def need(x,msg):
 if not x:raise ValueError(msg)
def digest(b):return {"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest()}
def file_identity(p):
 h=hashlib.sha256();n=0
 with pathlib.Path(p).open("rb") as f:
  while True:
   b=f.read(1048576)
   if not b:break
   n+=len(b);h.update(b)
 return {"bytes":n,"sha256":h.hexdigest()}
def checked(p,pin):
 b=pathlib.Path(p).read_bytes()
 need(digest(b)=={"bytes":pin[0],"sha256":pin[1]},"pinned input: "+str(p))
 return b
def parse_json_bytes(p,b):return json.loads(gzip.decompress(b) if str(p).endswith(".gz") else b)
def save_json(p,x):
 p=pathlib.Path(p);tmp=p.with_name(p.name+".tmp")
 with (gzip.open(tmp,"wt",encoding="utf-8",compresslevel=1) if p.suffix==".gz" else tmp.open("w",encoding="utf-8")) as f:json.dump(x,f,separators=(",",":"),ensure_ascii=False)
 os.replace(tmp,p)
 return {"file":p.name,**file_identity(p),"temporaryOnly":True}
def save_field(p,A):
 import numpy as np
 B=np.asarray(A,dtype=np.int64)
 need(B.ndim==2 and bool(np.all((B>=0)&(B<31))),"complete canonical field matrix")
 raw=b"R150BC31"+struct.pack("<III",31,*B.shape)+B.astype(np.uint8).tobytes(order="C")
 p=pathlib.Path(p);tmp=p.with_name(p.name+".tmp")
 tmp.write_bytes(raw);os.replace(tmp,p)
 return {"file":p.name,**digest(raw),"rows":B.shape[0],"cols":B.shape[1],"temporaryOnly":True}
def iszero(M):return all(not M[i,j] for i in range(M.nrows()) for j in range(M.ncols()))
def rows_of(M):return [[int(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())]
def nullspace31(M):
 from flint import nmod_mat
 R,rank=M.rref();rank=int(rank);piv=[]
 for i in range(rank):
  j=next((j for j in range(M.ncols()) if R[i,j]),None)
  need(j is not None and int(R[i,j])==1,"complete finite RREF pivot")
  piv.append(j)
 need(piv==sorted(set(piv)),"strict finite pivot order")
 free=[j for j in range(M.ncols()) if j not in set(piv)]
 L=nmod_mat(M.ncols(),len(free),[0]*(M.ncols()*len(free)),31)
 for col,f in enumerate(free):
  L[f,col]=1
  for i,p in enumerate(piv):L[p,col]=-R[i,f]
 need(iszero(M*L),"complete original small matrix times nullspace")
 for col,f in enumerate(free):
  need(all(int(L[f,j])==(1 if col==j else 0) for j in range(len(free))),"complete finite free identity")
 return L,rank,piv,free
def main(argv):
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ["point-model","selected-model","unit-profile","kernel36","projected-input","native-model","out"]:
  ap.add_argument("--"+k,type=pathlib.Path,required=True)
 ap.add_argument("--pure-matrices",type=pathlib.Path)
 ap.add_argument("--primitive-equations",type=pathlib.Path)
 ap.add_argument("--repo",type=pathlib.Path)
 ap.add_argument("--historical-ref",default=HIST_REF)
 ap.add_argument("--historical-path",default=HIST_PATH)
 ap.add_argument("--seconds",type=float,default=30)
 ap.add_argument("--memory-mib",type=int,default=512)
 a=ap.parse_args(argv)
 need(0<a.seconds<=120 and 0<a.memory_mib<=2048,"bounded next selected first connection")
 resource.setrlimit(resource.RLIMIT_AS,(int(a.memory_mib*1024**2),)*2)
 out=a.out.resolve();out.mkdir(parents=True,exist_ok=True);start=time.monotonic()
 rec={"format":"isp-same-selected-natural-u-first-connection-f31-v1","status":"running","phase":"inputs",
  "oldLargeNormalFormsRecomputed":False,"newDixonDigitsComputed":0,"newOtherPrimeComputed":False,
  "characteristicZeroSelectedFirstConnectionComputed":False,"leadingUnitProved":False,
  "largeDataUploadedOrCommitted":False,"parameters":{},"events":[]}
 temps=[];exitcode=1
 def remaining():
  r=a.seconds-(time.monotonic()-start)
  if r<=0:raise BudgetExpired("shared selected natural-u deadline")
  return r
 def checkpoint():
  rec["mathematicalElapsedSeconds"]=time.monotonic()-start
  rec["parameters"]["temporaryFiles"]=temps
  save_json(out/"selected-natural-first-connection-f31-receipt.json",rec)
 def beat(phase):
  rec["phase"]=phase;checkpoint();print(json.dumps({"phase":phase,"elapsedSeconds":time.monotonic()-start}),flush=True);remaining()
 def alarm(sig,frame):raise BudgetExpired("actual shared selected first-connection clock")
 signal.signal(signal.SIGALRM,alarm);signal.setitimer(signal.ITIMER_REAL,a.seconds)
 try:
  raw={};ids={}
  for key in ["point_model","selected_model","unit_profile","kernel36","projected_input","native_model"]:
   raw[key]=checked(getattr(a,key),PIN[key]);ids[key]=digest(raw[key])
  if a.pure_matrices:
   raw["pure_matrices"]=checked(a.pure_matrices,PIN["pure_matrices"]);ids["pure_matrices"]=digest(raw["pure_matrices"])
  primitive_temp=out/"original-primitive-integer-equations.json.gz"
  if a.primitive_equations:
   pb=checked(a.primitive_equations,PRIMITIVE)
  elif primitive_temp.exists():
   pb=checked(primitive_temp,PRIMITIVE);rec["events"].append({"reusedHistoricalPrimitiveBytes":True})
  else:
   need(a.repo is not None,"provide original primitive file or read-only historical repository")
   need(re.fullmatch("[0-9a-f]{40}",a.historical_ref) and a.historical_path==HIST_PATH,"known exact historical source location")
   rr=subprocess.run(["git","-C",str(a.repo),"show",a.historical_ref+":"+a.historical_path],
      stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=min(10.0,remaining()),check=False)
   need(rr.returncode==0,"read-only historical git show failed: "+rr.stderr.decode("utf-8","replace")[-1000:])
   pb=rr.stdout;need(digest(pb)=={"bytes":PRIMITIVE[0],"sha256":PRIMITIVE[1]},"complete historical primitive bytes and SHA")
  if not primitive_temp.exists():primitive_temp.write_bytes(pb)
  ids["primitive_equations"]=digest(pb)
  pr=gzip.decompress(pb);need(hashlib.sha256(pr).hexdigest()==PRIMITIVE_RAW_SHA,"complete decompressed primitive model SHA")
  primitive=json.loads(pr);eq=primitive["equations"]
  need(len(eq)==17 and all(len(r)==77 for r in eq),"all original17 coefficient polynomials")
  point=json.loads(raw["point_model"]);model=parse_json_bytes(a.selected_model,raw["selected_model"])
  profile=json.loads(raw["unit_profile"]);data=parse_json_bytes(a.projected_input,raw["projected_input"])
  J=set(map(int,model["selectedRows"]));I=set(map(int,profile["originalOutputI"]));free_raw=list(map(int,model["freeRows"]))
  need(len(J)==4354 and len(I)==4354 and len(set(free_raw))==36 and set(free_raw)<=J,"same original I,J and36 free sources")
  need(point["characteristicZeroSameOriginal17Verified"],"paid original primitive point")
  F0=[];F1=[]
  for e,row in enumerate(eq):
   r0=[];r1=[]
   for j,pol in enumerate(row):
    v=list(map(int,pol));need(bool(v),"nonempty original polynomial coefficient")
    if e>=11 and j<11:
     need(not any(v),"Gamma has no linear coefficient");r0.append(0);r1.append(0);continue
    d=10 if e<11 and j<11 else 0 if e<11 else 5
    need(not any(v[d+1:]),"same natural infinity degree")
    r0.append(v[d] if d<len(v) else 0);r1.append(v[d-1] if d>0 and d-1<len(v) else 0)
   F0.append(r0);F1.append(r1)
  need(F0==[list(map(int,r)) for r in point["primitivePointCoefficients"]],"all1309 original constant coefficients exactly match old point")
  tok=iter(raw["native_model"].decode().split())
  need(next(tok)=="R150_NATIVE_NF_V1","frozen original native input")
  def take(n):return [next(tok) for _ in range(n)]
  native_checks=0
  for e in range(11):
   Q=list(map(int,take(66)))
   for k,v in enumerate(Q):
    need(v%31==int(eq[e][11+k][0])%31,"complete original N quadratic coefficient")
    native_checks+=1
   for j in range(11):
    v=list(map(int,take(11)));pol=list(map(int,eq[e][j]))
    need(all(v[k]%31==(pol[k] if k<len(pol) else 0)%31 for k in range(11)),"all original N parameter coefficients")
    native_checks+=11
  need(int(next(tok))==3333,"frozen original prebasis dictionary count");take(3333*4)
  for g in range(6):
   for k in range(66):
    v=list(map(int,take(6)));pol=list(map(int,eq[11+g][11+k]))
    need(all(v[j]%31==(pol[j] if j<len(pol) else 0)%31 for j in range(6)),"all original Gamma parameter coefficients")
    native_checks+=6
  ns,nt=map(int,take(2));need((ns,nt)==(2195,9),"frozen original source identities")
  take(ns*3);need(list(map(int,take(nt)))==list(range(2,11)),"frozen original nine target labels")
  need(next(tok,None) is None and native_checks==4433,"complete original native input and4433 exact parameter checks")
  from flint import nmod_mat,fmpq,fmpq_mat
  import numpy as np
  kb=raw["kernel36"];need(kb[:8]==b"R150BC31" and struct.unpack_from("<III",kb,8)==(31,6188,36),"complete original field kernel header")
  K=np.frombuffer(kb,dtype=np.uint8,offset=20).reshape(6188,36).astype(np.int64)
  need(bool(np.all(K<31)),"canonical original field kernel")
  outside=[r-1 for r in range(1,6189) if r not in J]
  need(not bool(np.any(K[outside,:])),"all original kernel source support is sameJ")
  need(bool(np.array_equal(K[[r-1 for r in free_raw],:],np.eye(36,dtype=np.int64))),"all36 original free coordinates identity")
  whole=[q for d in range(5,0,-1) for q in itertools.combinations_with_replacement(range(11),d)]
  multipliers=[q for d in range(4) for q in itertools.combinations_with_replacement(range(11),d)]
  mon=[(i,) for i in range(11)]+[(i,j) for i in range(11) for j in range(i,11)]
  need(len(whole)==4367 and len(multipliers)*17==6188,"complete original monomial dictionaries")
  wi={q:i for i,q in enumerate(whole)}
  projected=[i for i,q in enumerate(whole) if 1<=sum(j<=8 for j in q)<=2]
  need(projected==list(map(int,data["originalOutputIndices"])) and len(projected)==585,"same actual585 projected outputs")
  need([list(whole[i]) for i in projected]==data["originalOutputMonomials"],"all585 monomial labels")
  oi={whole[i]:j for j,i in enumerate(projected)}
  participating=[r for r in sorted(J) if sum(j<=8 for j in multipliers[(r-1)//17])<=1]
  need(participating==list(map(int,data["originalSourceRows"])) and len(participating)==954,"same complete954 source projection")
  sparse=[{int(i):int(v) for i,v in row} for row in data["originalSparseColumns"]]
  need(len(sparse)==954,"all actual source columns")
  for q,row in zip(participating,sparse):
   e=(q-1)%17;mul=multipliers[(q-1)//17];actual={}
   for j,v in enumerate(F0[e]):
    mm=tuple(sorted(mul+mon[j]))
    if v and mm in oi:actual[oi[mm]]=actual.get(oi[mm],0)+v
   need({i:v for i,v in actual.items() if v}==row,"same original integer projection source "+str(q))
  pureI=[i for i,q in enumerate(whole) if i in I and all(j>=9 for j in q)]
  excluded=[j for j,i in enumerate(projected) if i not in I]
  need(len(pureI)==10 and [whole[projected[j]] for j in excluded]==[(6,),(7,),(8,)],"same10 pure and3 excluded one-transverse outputs")
  material={"codeSHA256":file_identity(__file__)["sha256"],"inputs":ids,"field":31,"chart":"u=1/s; actual u10 L(1/u), u5 Gamma(1/u)","kernelSourceCount":6188,"originalOutputCount":4367}
  binding=hashlib.sha256(json.dumps(material,sort_keys=True,separators=(",",":")).encode()).hexdigest()
  rec["parameters"].update({"binding":binding,"inputIdentity":material,"historicalRef":a.historical_ref,
    "historicalPath":a.historical_path,"secondsLimit":a.seconds,"memoryMiB":a.memory_mib,
    "allPrimitiveConstantCoefficientChecks":1309,"allOriginalParameterCoefficientChecksModulo31":native_checks,
    "selectedFreeOriginalRows":free_raw,"pureSelectedOutputIndices":pureI,
    "excludedProjectedOutputs":[{"within585":j,"originalOutputIndex":projected[j],"monomial":list(whole[projected[j]])} for j in excluded]})
  coeffp=out/"same-original-natural-constant-and-first-coefficients.json.gz"
  temps.append(save_json(coeffp,{"binding":binding,"constant":F0,"naturalFirst":F1,"all1309ConstantIdentitiesVerified":True,"all4433ParameterFieldIdentitiesVerified":True}))
  beat("complete-small-cokernel")
  T=nmod_mat(954,585,[row.get(j,0)%31 for row in sparse for j in range(585)],31)
  cp=out/"complete-selected-cokernel36-field31.json.gz"
  if cp.exists():
   c= parse_json_bytes(cp,cp.read_bytes());need(c["binding"]==binding,"same completed small-cokernel binding")
   L=nmod_mat(c["fullProjectedLeftKernel"],31);Z=nmod_mat(c["excludedRowKernel"],31);LS=L*Z
   need((L.nrows(),L.ncols(),Z.nrows(),Z.ncols())==(585,29,29,26),"complete cached small dimensions")
   need(iszero(T*L) and int(L.rank())==29 and int(Z.rank())==26,"all original cached field kernel products and ranks")
   need(all(not LS[i,j] for i in excluded for j in range(26)),"all deleted rows exactlyzero")
   rec["events"].append({"reusedCompleteSmallCokernel":True})
  else:
   L,rank,piv,free=nullspace31(T);need(rank==556 and L.ncols()==29,"paid complete field rank556")
   LE=nmod_mat([[int(L[i,j]) for j in range(29)] for i in excluded],31)
   Z,erank,ep,ef=nullspace31(LE);need(erank==3 and Z.ncols()==26,"complete deleted-row rank3")
   LS=L*Z;need(all(not LS[i,j] for i in excluded for j in range(26)),"extend selected duals byzero on excluded rows")
   save_json(cp,{"binding":binding,"rank":rank,"fullProjectedLeftKernel":rows_of(L),"excludedRowKernel":rows_of(Z),
    "fullProjectedFreeCoordinates":free,"excludedRowKernelFreeCoordinates":ef,"allOriginalSourceProductsVerified":True})
  need(iszero(T*LS) and int(LS.rank())==26,"complete selected582 low-output coker")
  temps.append({"file":cp.name,**file_identity(cp),"temporaryOnly":True})
  if a.pure_matrices:
   pm=parse_json_bytes(a.pure_matrices,raw["pure_matrices"]);Qcols=pm["completeFullProjectionQColumns"]
   need(len(Qcols)==7 and all(len(c)==135 for c in Qcols),"old fullP0 complete rightkernel")
   # Exact generator order begins z2,z3,z4, i.e. original m8,m7,m6.
   QE=fmpq_mat([[fmpq(Qcols[j][i]) for j in range(7)] for i in range(3)])
   er=int(QE.rank());rec["parameters"]["fullA0RestrictedOutputI"]={
     "deletedOriginalVariablesInPhysicalRowOrder":[8,7,6],"deletedRowsOfQ":[[str(QE[i,j]) for j in range(7)] for i in range(3)],
     "deletedQRowRankOverQ":er,"rankFullA0RestrictedToI":4337+er,
     "derivation":"4212 higher outputs plus (128-3+rank Q_deleted)"}
  beat("whole-original-natural-products")
  prodp=out/"whole-natural-first-product-field31.json.gz"
  if prodp.exists():
   c=parse_json_bytes(prodp,prodp.read_bytes());need(c["binding"]==binding and c["all4367ConstantProductsZero"] is True,"same completed original product")
   R1=np.asarray(c["naturalFirstProductRows"],dtype=np.int64)
   need(R1.shape==(4367,36) and bool(np.all((R1>=0)&(R1<31))),"complete canonical restored original first product")
   rec["events"].append({"reusedCompleteOriginalNaturalFirstProduct":True})
  else:
   R0=np.zeros((4367,36),dtype=np.int64);R1=np.zeros((4367,36),dtype=np.int64)
   # Each coordinate receives at most6188*77*30*30 <2^31, so no int64 overflow.
   need(6188*77*30*30<2**31,"explicit exact accumulator bound")
   for ix,raw_id in enumerate(sorted(J)):
    v=K[raw_id-1,:]
    if not np.any(v):continue
    e=(raw_id-1)%17;mul=multipliers[(raw_id-1)//17]
    for j,m in enumerate(mon):
     z0=F0[e][j]%31;z1=F1[e][j]%31
     if z0 or z1:
      r=wi[tuple(sorted(mul+m))]
      if z0:R0[r,:]+=z0*v
      if z1:R1[r,:]+=z1*v
    if ix%500==499:remaining()
   R0%=31;R1%=31
   need(not bool(np.any(R0)),"all4367 by36 constant original kernel products")
   save_json(prodp,{"binding":binding,"all4367ConstantProductsZero":True,"all36SelectedSourceHeadsRetained":True,"naturalFirstProductRows":R1.tolist()})
  temps.append({"file":prodp.name,**file_identity(prodp),"temporaryOnly":True})
  beat("complete-same-selected-first-connection")
  LR=nmod_mat(R1[projected,:].tolist(),31)
  low=LS.transpose()*LR
  connection=nmod_mat(R1[pureI,:].tolist()+rows_of(low),31)
  need((connection.nrows(),connection.ncols())==(36,36),"complete sameI firstconnection")
  heads,brank,bp,bf=nullspace31(connection)
  # Full-output selected coker49 is also retained; this is NOT the fullA0 coker27.
  pureFull=[i for i,q in enumerate(whole) if all(j>=9 for j in q)]
  fullconnection=nmod_mat(R1[pureFull,:].tolist()+rows_of(L.transpose()*LR),31)
  need((fullconnection.nrows(),fullconnection.ncols())==(49,36),"complete full-output selected49 coker")
  fullrank=int(fullconnection.rank())
  HM=np.asarray(rows_of(heads),dtype=np.int64)
  original_heads=(K@HM)%31
  first_head_products=(R1@HM)%31
  need(iszero(connection*heads),"complete next33-or-other first-kernel source relations")
  temps.append(save_field(out/"same-selected-natural-first-connection31.bin",rows_of(connection)))
  temps.append(save_field(out/"full-output-selected-first-connection49-field31.bin",rows_of(fullconnection)))
  temps.append(save_field(out/"selected-natural-first-kernel-heads31.bin",original_heads))
  temps.append(save_field(out/"selected-natural-first-kernel-original-first-products31.bin",first_head_products))
  rec.update({"status":"completed","phase":"complete",
    "selectedNaturalFirstConnectionRankModulo31":brank,
    "selectedNaturalFirstConnectionRankOverQLowerBound":brank,
    "completeSameSelectedCokernelDimension":36,"fullOutputSelectedCokernelDimension":49,
    "fullOutputSelectedFirstConnectionRankModulo31":fullrank,
    "completeNextFirstKernelDimension":36-brank,
    "all4367ConstantKernelProductsZero":True,
    "allOriginalNaturalFirstProductsRetained":True,
    "all36OriginalKernelDirectionsRetained":True,
    "sameOriginalSelectedSourceSupportVerified":True,
    "allOriginalSmallCokernelProductsVerified":True,
    "allOriginalParameterCoefficientsModulo31Verified":True,
    "all1309ExactPrimitiveConstantCoefficientsVerified":True,
    "coMovingSourceDerivativeTermDiscarded":False,
    "nextFirstKernelHeadsHaveCompleteOriginalSourceCoordinates":True,
    "nextFirstKernelSourceCorrectionsComputed":False,
    "selectedMinorInfinityOrderModulo31LowerBound":72-brank,
    "completeSelectedInfinitySmithLengthComputed":False})
  rec["parameters"].update({"field":31,"sourceCount":6188,"selectedSourceCount":4354,
    "originalOutputCount":4367,"sameSelectedOutputCount":4354,"selectedConnectionMatrix36":rows_of(connection),
    "selectedFirstKernelCoefficientMatrix36":rows_of(heads),"selectedFirstKernelFreeCoordinates":bf,
    "sameSelectedNaturalFirstKernelScope":"constant heads only; true sameI B0 source correction still required before next u page",
    "firstConnectionOverQIsOnlyLowerBound":True,
    "physicalComplete27QuotientNotSubstitutedForSelected36":True,
    "historicalPrimitiveDataIsTemporaryOnly":True})
  exitcode=0
 except (BudgetExpired,subprocess.TimeoutExpired) as e:
  rec.update(status="budget-exhausted",error=str(e));exitcode=75
 except Exception as e:
  rec.update(status="failed",error=str(e),exceptionType=type(e).__name__)
  (out/"exception.log").write_text(traceback.format_exc());exitcode=1
 finally:
  signal.setitimer(signal.ITIMER_REAL,0);checkpoint()
 need((out/"selected-natural-first-connection-f31-receipt.json").stat().st_size<100000,"small permanent receipt")
 print(json.dumps(rec,ensure_ascii=False),flush=True);return exitcode
if __name__=="__main__":sys.exit(main(sys.argv[1:]))
