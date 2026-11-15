#!/usr/bin/env python3
"""Solve only the seven remaining original Q directions after paid29 Koszul deletion.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
Uses the actual65521 column profile solely to select original integer units.
"""
import argparse,array,fractions,gzip,hashlib,importlib.util,itertools,json,math,os,pathlib,resource,signal,struct,subprocess,sys,time,traceback
sys.dont_write_bytecode=True
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
H_SHA="9332d9d394b1a17444c9ccc20b3971cf74b7e932cffc8d9189e4e2f64fe0c428"
P_SHA="97d31570a0bd99d33066fc6ea47984203b2964521ceeb50920f0a49dd3bb8074"
MODEL_SHA="0aa2d6d5c368b9885e279cd5b8e2cc7a59ba574ca161c0535193c30defe52d3d"
PROFILE_SHA="523d3835e92d9a8747759c6fa5949c5aec1b452e6f78fc76db5a7455e4c5f66b"
MATRIX_SHA="a9b89935d75f7c56fd8fe7becc142b7c84a7e1164b481170dc6d9790fe6d3fc3"
P=65521
class BudgetExpired(Exception):pass
def need(b,s):
 if not b:raise ValueError(s)
def sha(p):
 h=hashlib.sha256();n=0
 with pathlib.Path(p).open("rb") as f:
  while True:
   z=f.read(1048576)
   if not z:break
   n+=len(z);h.update(z)
 return {"bytes":n,"sha256":h.hexdigest()}
def read(p):
 p=pathlib.Path(p)
 with (gzip.open(p,"rt",encoding="utf-8") if p.suffix==".gz" else p.open()) as f:return json.load(f)
def save(p,x):
 p=pathlib.Path(p);q=p.with_name(p.name+".tmp")
 with (gzip.open(q,"wt",encoding="utf-8",compresslevel=1) if p.suffix==".gz" else q.open("w")) as f:json.dump(x,f,separators=(",",":"))
 os.replace(q,p);return {"file":p.name,**sha(p),"temporaryOnly":True}
def vecsha(v):
 h=hashlib.sha256()
 for x in v:h.update((str(x)+"\n").encode())
 return h.hexdigest()
def canonical(v):
 g=0
 for x in v:g=math.gcd(g,abs(x))
 if not g:return v
 sg=-1 if next(x for x in v if x)<0 else 1
 return [sg*(x//g) for x in v]
def pivots(R,r,n):
 ans=[];j=0
 for i in range(r):
  while j<n and R[i,j]==0:j+=1
  need(j<n,"RREF pivot count");ans.append(j);j+=1
 return ans
def exact_kernel_of_rows(rows,n):
 from flint import fmpq_mat
 R,r=fmpq_mat(len(rows),n,[x for row in rows for x in row]).rref();r=int(r)
 pp=pivots(R,r,n);ff=[j for j in range(n) if j not in set(pp)];basis=[]
 for c in ff:
  v=[fractions.Fraction(0) for _ in range(n)];v[c]=fractions.Fraction(1)
  for i,p in enumerate(pp):v[p]=-fractions.Fraction(int(R[i,c].p),int(R[i,c].q))
  d=1
  for x in v:d=math.lcm(d,x.denominator)
  basis.append(canonical([int(x*d) for x in v]))
 return r,basis
def worker(argv):
 ap=argparse.ArgumentParser()
 for k in ["core","profile","out"]:ap.add_argument("--"+k,required=True,type=pathlib.Path)
 a=ap.parse_args(argv);start=time.monotonic()
 from flint import fmpq_mat
 core=read(a.core);profile=read(a.profile);need(profile["coreIdentity"]==sha(a.core),"actual original integer core")
 rows=[{int(j):int(v) for j,v in row} for row in core["integerRows"]]
 pp=profile["pivotColumnPositions"];ff=profile["freeColumnPositions"];ii=profile["unitOriginalRowsZeroBased"];r=len(pp)
 need(r==4318 and len(ff)==7,"only actual4318x7 problem")
 B=fmpq_mat(r,r,[rows[i].get(j,0) for i in ii for j in pp])
 E=fmpq_mat(r,7,[rows[i].get(j,0) for i in ii for j in ff])
 X=B.solve(E,algorithm="dixon")
 pairs=[[[str(int(X[i,j].p)),str(int(X[i,j].q))] for j in range(7)] for i in range(r)]
 output={"format":"isp-seven-exact-original-unit-solution-v1","binding":profile["binding"],
   "rows":r,"columns":7,"unitProfileIdentity":sha(a.profile),
   "solutionPairsByRows":pairs,"equation":"B*X=E; original source graph uses -X",
   "fullOriginalProductsVerified":False}
 rec=save(a.out/"seven-original-unit-block-solution.json.gz",output)
 # Native solve is fully retained before any later complete product work.
 receipt={"status":"completed","binding":profile["binding"],"solution":rec,
   "exactSolver":"fmpq_mat.solve(algorithm=dixon)","elapsedSeconds":time.monotonic()-start,
   "fullOriginalVerificationPending":True}
 save(a.out/"seven-original-unit-solve-receipt.json",receipt);print(json.dumps(receipt),flush=True);return 0
def main(argv):
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ["helper","point-model","native-model","prepared-model","prime-dir","out"]:ap.add_argument("--"+k,required=True,type=pathlib.Path)
 ap.add_argument("--seconds",type=float,default=600);ap.add_argument("--memory-mib",type=int,default=4096)
 ap.add_argument("--resume",action="store_true")
 a=ap.parse_args(argv);need(math.isfinite(a.seconds) and 0<a.seconds<=1200,"bounded shared seconds <=1200")
 need(0<a.memory_mib<=4096,"<=4096MiB per process")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 start=time.monotonic();deadline=start+a.seconds-min(8,a.seconds/20)
 out=a.out.resolve();need(a.resume or not out.exists() or not any(out.iterdir()),"fresh output or explicit resume");out.mkdir(parents=True,exist_ok=True)
 receipt={"format":"isp-seven-original-directions-exact-rational-solve-v1","status":"running",
  "secondsLimit":a.seconds,"memoryMiBPerProcess":a.memory_mib,"newOriginalDixonDigitsComputed":0,
  "oldNormalFormsRecomputed":False,"old31RowOperationsUsedAsRational":False,
  "largeDataUploadedOrCommitted":False,"parameters":{},"events":[]}
 temps=[];verified=[];code=1
 def check():
  if time.monotonic()>=deadline:raise BudgetExpired("actual shared mathematical deadline")
 def remember(p):
  rec={"file":p.name,**sha(p),"temporaryOnly":True}
  if not any(x["file"]==rec["file"] for x in temps):temps.append(rec)
  return rec
 def checkpoint():
  receipt["parameters"]["temporaryFiles"]=temps;receipt["parameters"]["verifiedKernelColumns"]=verified
  receipt["mathematicalElapsedSeconds"]=time.monotonic()-start
  save(out/"seven-exact-rational-original-receipt.json",receipt)
 try:
  need(sha(a.helper)["sha256"]==H_SHA and sha(a.point_model)["sha256"]==P_SHA,"paid helper and original point")
  need(sha(a.prepared_model)=={"bytes":814572,"sha256":MODEL_SHA},"same original source dictionary")
  oldprofile=a.prime_dir/"selected-65521-column-profile.json";oldmatrix=a.prime_dir/"original-selected-columns-65521.bin"
  need(sha(oldprofile)=={"bytes":41202,"sha256":PROFILE_SHA},"actual65521 profile bytes")
  need(sha(oldmatrix)=={"bytes":37774570,"sha256":MATRIX_SHA},"actual complete65521 matrix bytes")
  sp=importlib.util.spec_from_file_location("paid_helper",a.helper);H=importlib.util.module_from_spec(sp);sp.loader.exec_module(H)
  need(sha(a.native_model)["sha256"]==H.NATIVE_SHA,"same original native dictionaries")
  point=read(a.point_model);model=read(a.prepared_model);prior=read(oldprofile)
  need(prior["prime"]==65521 and prior["rank"]==4318 and prior["all4367KernelProductsZero"],"paid complete finite rank")
  columns=list(map(int,prior["selectedOriginalSourceRows"]));free=list(map(int,model["freeRows"]))
  selected=set(map(int,model["selectedRows"]));removed=free[:29]
  need(columns==sorted(selected-set(removed)) and len(columns)==4325 and len(free)==36,"same29 deleted exact source columns")
  pp=list(map(int,prior["pivotColumnsZeroBased"]));ff=list(map(int,prior["freeColumnsZeroBased"]))
  need(len(pp)==4318 and len(ff)==7 and sorted(pp+ff)==list(range(4325)),"complete65521 source profile")
  # Reconstruct the original4354 output set I, not an arbitrary new row restriction.
  vv=[8**i for i in range(11)]
  output_keys=[sum(vv[j] for j in q) for d in range(5,0,-1) for q in itertools.combinations_with_replacement(range(11),d)]
  key_index={k:i for i,k in enumerate(output_keys)};need(len(key_index)==4367,"original4367 outputs")
  tokens=a.native_model.read_text().split();pos=1+11*(66+11*11)
  need(tokens[0]=="R150_NATIVE_NF_V1" and int(tokens[pos])==3333,"3333 paid leading output dictionary")
  pre_outputs=[key_index[int(tokens[pos+1+4*j+2])] for j in range(3333)]
  extras=list(map(int,point["selectedOutputIndicesZeroBased"]));extra_keys=list(map(int,point["selectedOutputMonomialKeys"]))
  need(all(key_index[k]==i for i,k in zip(extras,extra_keys)),"original1021 output index transport")
  original_I=sorted(set(pre_outputs)|set(extras));need(len(original_I)==4354,"same actual4354 output set")
  terms=H.original_row_terms(point)
  material={"codeSHA256":sha(__file__)["sha256"],"helperSHA256":H_SHA,"pointSHA256":P_SHA,"nativeSHA256":H.NATIVE_SHA,
     "sourceModelSHA256":MODEL_SHA,"finiteProfileSHA256":PROFILE_SHA,"finiteMatrixSHA256":MATRIX_SHA}
  binding=hashlib.sha256(json.dumps(material,sort_keys=True,separators=(",",":")).encode()).hexdigest()
  receipt["parameters"].update({"binding":binding,"inputIdentity":material,
       "removedOriginalSourceRows":removed,"originalOutputIHas4354Rows":True,
       "noRationalRankClaimFromSecondPrimeAlone":True})
  core_path=out/"seven-original-integer-core.json.gz"
  if core_path.exists():
   core=read(core_path);need(core["binding"]==binding,"saved integer core binding")
   rows=[{int(j):int(v) for j,v in row} for row in core["integerRows"]]
   receipt["events"].append("reused full original integer core")
  else:
   rows=[{} for _ in range(4367)]
   for j,raw in enumerate(columns):
    for i,c in terms[raw-1]:rows[i][j]=rows[i].get(j,0)+c
    if j%128==0:check()
   rows=[{j:v for j,v in row.items() if v} for row in rows]
   core={"format":"isp-seven-original-integer-core-v1","binding":binding,"sourceRows":columns,
      "originalOutputI":original_I,"integerRows":[[[j,str(v)] for j,v in sorted(row.items())] for row in rows]}
   save(core_path,core)
  remember(core_path);profile_path=out/"seven-original-unit-row-profile.json"
  from flint import nmod_mat,fmpq_mat
  if profile_path.exists():
   profile=read(profile_path);need(profile["binding"]==binding and profile["coreIdentity"]==sha(core_path),"saved original unit row profile")
   receipt["events"].append("reused true original unit row profile")
  else:
   check()
   # One new transpose selection; first attempt stays inside original I.
   T=nmod_mat(4318,len(original_I),[rows[i].get(j,0)%P for j in pp for i in original_I],P)
   R,rank=T.rref();rank=int(rank)
   candidate=original_I;inside=True
   if rank!=4318:
    del T,R
    candidate=list(range(4367));inside=False
    T=nmod_mat(4318,4367,[rows[i].get(j,0)%P for j in pp for i in candidate],P)
    R,rank=T.rref();rank=int(rank);need(rank==4318,"actual full65521 pivot columns remain independent")
   ppos=pivots(R,4318,len(candidate));unit=[candidate[j] for j in ppos]
   profile={"format":"isp-seven-original-unit-row-profile-v1","binding":binding,"coreIdentity":sha(core_path),
      "pivotColumnPositions":pp,"freeColumnPositions":ff,"unitOriginalRowsZeroBased":unit,
      "unitRowsSubsetOriginalI":inside,"originalOutputI":original_I,
      "unitBlockNonzeroModulo65521":True,"finiteTransposeRank":4318}
   save(profile_path,profile);del T,R
  remember(profile_path)
  receipt.update({"unitRowsSubsetOriginalI":profile["unitRowsSubsetOriginalI"],"actualUnitSize":4318,"exactRightHandSides":7})
  checkpoint();check()
  solpath=out/"seven-original-unit-block-solution.json.gz";solve_receipt=out/"seven-original-unit-solve-receipt.json"
  if solpath.exists():
   sol=read(solpath);need(sol["binding"]==binding and sol["unitProfileIdentity"]==sha(profile_path),"saved exact7 solution binding")
   receipt["events"].append("reused completed exact7 unit-block solution")
  else:
   log=out/"seven-original-unit-solve.log"
   cmd=[sys.executable,"-B",str(pathlib.Path(__file__).resolve()),"--solve-worker","--core",str(core_path),"--profile",str(profile_path),"--out",str(out)]
   ws=time.monotonic()
   with log.open("w") as logf:
    proc=subprocess.Popen(cmd,stdout=logf,stderr=subprocess.STDOUT,start_new_session=True)
    try:proc.wait(timeout=max(.01,deadline-time.monotonic()))
    except subprocess.TimeoutExpired:
     os.killpg(proc.pid,signal.SIGKILL);proc.wait()
     receipt["events"].append({"exactSolveStoppedAtDeadline":True,"exitCode":proc.returncode,"elapsedSeconds":time.monotonic()-ws})
     raise BudgetExpired("exact7 solve did not return; true original input/profile retained")
   need(proc.returncode==0 and solpath.exists(),"exact7 rational solver completion")
   sol=read(solpath);need(sol["binding"]==binding,"new exact7 solution binding")
  remember(solpath)
  if solve_receipt.exists():remember(solve_receipt)
  need((sol["rows"],sol["columns"])==(4318,7),"complete exact7 solution dimensions")
  graph_path=out/"seven-original-integer-graph.json.gz"
  if graph_path.exists():
   gd=read(graph_path);need(gd["binding"]==binding,"saved source graph binding");graph=[[int(v) for v in c] for c in gd["columns"]]
   receipt["events"].append("reused seven original rational graph columns")
  else:
   graph=[]
   for c in range(7):
    check();D=1
    for i in range(4318):D=math.lcm(D,int(sol["solutionPairsByRows"][i][c][1]))
    v=[0]*4325;v[ff[c]]=D
    for i,j in enumerate(pp):
     n,d=map(int,sol["solutionPairsByRows"][i][c]);v[j]=-n*(D//d)
    graph.append(canonical(v))
   save(graph_path,{"binding":binding,"rows":4325,"columns":[[str(x) for x in v] for v in graph],
       "profileIdentity":sha(profile_path),"verificationPending":True})
  remember(graph_path);checkpoint();check()
  residual_path=out/"seven-complete-original-graph-residual.json.gz"
  if residual_path.exists():
   rd=read(residual_path);need(rd["binding"]==binding,"saved complete residual binding")
   residual=[[int(x) for x in row] for row in rd["integerRows"]]
   receipt["events"].append("reused complete original4367 graph residual")
  else:
   residual=[[0]*7 for _ in range(4367)]
   for i,row in enumerate(rows):
    for j,v in row.items():
     for c in range(7):residual[i][c]+=v*graph[c][j]
    if i%32==0:check()
   need(all(all(x==0 for x in residual[i]) for i in profile["unitOriginalRowsZeroBased"]),"all4318 original unit-block integer products")
   save(residual_path,{"binding":binding,"rows":4367,"columns":7,"integerRows":[[str(x) for x in row] for row in residual],
        "all4318OriginalUnitProductsZero":True})
  remember(residual_path);need(len(residual)==4367 and all(len(row)==7 for row in residual),"all4367 residual rows")
  rankR,Tkernel=exact_kernel_of_rows(residual,7)
  if profile["unitRowsSubsetOriginalI"]:
   rankRI,_=exact_kernel_of_rows([residual[i] for i in original_I],7)
   rankB=4318+rankRI
  else:rankRI=None;rankB=None
  rankC=4318+rankR;d=7-rankR
  basis_path=out/"seven-exact-complement-source-basis.json.gz"
  if basis_path.exists():
   kb=read(basis_path);need(kb["binding"]==binding and kb["dimension"]==d,"saved complement source basis binding")
   basis=[[int(x) for x in v] for v in kb["original6188Columns"]]
   receipt["events"].append("reused complete exact original complement basis")
  else:
   basis=[]
   for c in Tkernel:
    small=canonical([sum(c[t]*graph[t][j] for t in range(7) if c[t]) for j in range(4325)])
    v=[0]*6188
    for j,raw in enumerate(columns):v[raw-1]=small[j]
    basis.append(v)
   save(basis_path,{"binding":binding,"dimension":d,"original6188Columns":[[str(x) for x in v] for v in basis],
       "completeOriginalResidualRankOverQ":rankR,"allSourceRowsRetained":True,"verificationPending":True})
  remember(basis_path);checkpoint();check()
  freecols=[]
  for k,nums in enumerate(basis):
   check();cp=out/("seven-complement-kernel-%02d.json.gz"%k);nsha=vecsha(nums)
   if cp.exists():
    cert=read(cp);need(cert["binding"]==binding and cert["numeratorSHA256"]==nsha and cert["all4367ExactIntegerProductsZero"],"saved complete original kernel")
    receipt["events"].append({"reusedVerifiedComplementKernel":k})
   else:
    need(len(nums)==6188 and all(nums[r-1]==0 for r in model["outsideRows"]),"same selected support")
    need(all(nums[r-1]==0 for r in removed),"all first29 free coordinates zero")
    product=H.exact_product(nums,terms,check);need(all(x==0 for x in product),"all4367 original integer products")
    cert={"format":"isp-seven-complement-original-kernel-v1","binding":binding,"column":k,
       "original6188IntegerCoefficients":[str(x) for x in nums],"numeratorSHA256":nsha,
       "fullZeroProductSHA256":vecsha(product),"all4367ExactIntegerProductsZero":True,
       "allFirst29FreeCoordinatesZero":True,"all1834OutsideCoordinatesZero":True,
       "free36IntegerCoordinates":[str(nums[r-1]) for r in free]}
    save(cp,cert)
   cr=remember(cp);fr=[nums[r-1] for r in free];freecols.append(fr)
   verified.append({"column":k,"certificate":cr,"sourceSHA256":nsha,
     "maximumSourceIntegerBits":max((abs(x).bit_length() for x in nums),default=0),"all4367ExactIntegerProductsZero":True})
   checkpoint()
  free_rank=int(fmpq_mat(7,d,[freecols[c][r] for r in range(29,36) for c in range(d)]).rank()) if d else 0
  need(free_rank==d and all(all(v[j]==0 for j in range(29)) for v in freecols),"whole tail7 independent complement")
  fr=save(out/"seven-complement-complete-free-image.json.gz",{"binding":binding,"rows":36,"columns":d,
       "integerColumns":[[str(x) for x in v] for v in freecols],"tailRankOverQ":free_rank})
  temps.append(fr)
  receipt.update({"status":"completed","completeOriginalGraphResidualRankOverQ":rankR,
    "completeOriginalOutputIResidualRankOverQ":rankRI,"newTrueComplementKernelDimension":d,
    "combinedPaid29AndNewKernelDimension":29+d,"completeTailSevenFreeImageRankOverQ":free_rank,
    "completeSelectedOriginalC0RankOverQ":rankC,"completeSelectedOriginalB0RankOverQ":rankB,
    "completeSelectedB0RankLowerBound":4318 if rankB is None else rankB,
    "completeSelectedB0RankUpperBound":rankC if rankB is None else rankB,
    "all4367ExactKernelProductsZero":True,"all1834OutsideSourceCoordinatesZero":True,
    "allFirst29FreeCoordinatesZero":True,"completeRationalComplementKernelCertified":True})
  code=0
 except BudgetExpired as e:receipt.update(status="budget-exhausted",error=str(e));code=75
 except Exception as e:
  receipt.update(status="failed",error=str(e),exceptionType=type(e).__name__);(out/"exception.log").write_text(traceback.format_exc());code=1
 finally:checkpoint()
 need((out/"seven-exact-rational-original-receipt.json").stat().st_size<100000,"small long-term receipt")
 print(json.dumps(receipt),flush=True);return code
if __name__=="__main__":
 if len(sys.argv)>1 and sys.argv[1]=="--solve-worker":sys.exit(worker(sys.argv[2:]))
 sys.exit(main(sys.argv[1:]))
