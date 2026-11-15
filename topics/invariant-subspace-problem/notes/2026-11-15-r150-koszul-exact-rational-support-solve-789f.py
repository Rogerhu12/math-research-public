#!/usr/bin/env python3
"""Exact characteristic-zero support solve for the original infinity Koszul family.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
Preserves original6188 source identities and verifies all4367 integer products.
"""
import argparse, fractions, gzip, hashlib, importlib.util, json, math, os, pathlib, resource, signal, subprocess, sys, time, traceback
sys.dont_write_bytecode=True
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
H_SHA="9332d9d394b1a17444c9ccc20b3971cf74b7e932cffc8d9189e4e2f64fe0c428"
P_SHA="97d31570a0bd99d33066fc6ea47984203b2964521ceeb50920f0a49dd3bb8074"
PAID=[0,1,2,4,10,11,12,13,14,16,20,22,24,3,5,6,7,21,23,25,8,9,15]
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
 with (gzip.open(p,"rt",encoding="utf-8") if p.suffix==".gz" else p.open("r",encoding="utf-8")) as f:return json.load(f)
def save(p,x):
 p=pathlib.Path(p);q=p.with_name(p.name+".tmp")
 with (gzip.open(q,"wt",encoding="utf-8",compresslevel=1) if p.suffix==".gz" else q.open("w",encoding="utf-8")) as f:json.dump(x,f,separators=(",",":"))
 os.replace(q,p);return {"file":p.name,**sha(p),"temporaryOnly":True}
def rows_of(x):return [{int(j):int(v) for j,v in row} for row in x]
def canonical(v):
 g=0
 for x in v:g=math.gcd(g,abs(x))
 if not g:return v
 sign=-1 if next(x for x in v if x)<0 else 1
 return [sign*(x//g) for x in v]
def vecsha(v):
 h=hashlib.sha256()
 for x in v:h.update((str(x)+"\n").encode())
 return h.hexdigest()
def pivots(R,rank,n):
 ans=[];j=0
 for i in range(rank):
  while j<n and R[i,j]==0:j+=1
  need(j<n,"pivot count");ans.append(j);j+=1
 return ans
def fmpq_pair(x):return [str(int(x.p)),str(int(x.q))]
def worker(argv):
 ap=argparse.ArgumentParser()
 ap.add_argument("--core",required=True,type=pathlib.Path);ap.add_argument("--profile",required=True,type=pathlib.Path)
 ap.add_argument("--out",required=True,type=pathlib.Path)
 a=ap.parse_args(argv);start=time.monotonic()
 from flint import fmpq_mat
 core=read(a.core);pr=read(a.profile);rows=rows_of(core["coreRows"])
 need(sha(a.core)==pr["coreFileIdentity"],"core bytes before exact solve")
 pp=pr["pivotVariables"];ff=pr["freeVariables"];ii=pr["unitRowPositions"];rank=len(pp)
 if rank:
  B=fmpq_mat(rank,rank,[rows[i].get(j,0) for i in ii for j in pp])
  E=fmpq_mat(rank,len(ff),[rows[i].get(j,0) for i in ii for j in ff])
  X=B.solve(E,algorithm="dixon") if ff else fmpq_mat(rank,0)
  pairs=[[fmpq_pair(X[i,j]) for j in range(len(ff))] for i in range(rank)]
 else:pairs=[]
 sol={"format":"isp-exact-koszul-unit-block-solution-v1","binding":pr["binding"],
      "profileIdentity":sha(a.profile),"rows":rank,"columns":len(ff),
      "pivotVariables":pp,"freeVariables":ff,"solutionPairsByRows":pairs,
      "equation":"B*X=E; the graph has pivot part -X",
      "selectedBlockProductVerified":False}
 # Save the exact solver output before any complete residual/product work.
 rec=save(a.out/"exact-unit-block-solution.json.gz",sol)
 receipt={"status":"completed","binding":pr["binding"],"solution":rec,
          "elapsedSeconds":time.monotonic()-start,
          "completeOriginalResidualChecksPending":True,"exactSolver":"fmpq_mat.solve(algorithm=dixon)"}
 save(a.out/"exact-unit-block-solve-receipt.json",receipt);print(json.dumps(receipt),flush=True);return 0
def main(argv):
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ["helper","point-model","prepared-dir","out"]:ap.add_argument("--"+k,required=True,type=pathlib.Path)
 ap.add_argument("--seconds",type=float,default=300);ap.add_argument("--memory-mib",type=int,default=2048)
 ap.add_argument("--resume",action="store_true")
 a=ap.parse_args(argv)
 need(math.isfinite(a.seconds) and 0<a.seconds<=600,"shared bounded budget <=600s")
 need(0<a.memory_mib<=2048,"memory <=2048MiB per process")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 start=time.monotonic();deadline=start+a.seconds-min(5,a.seconds/10)
 out=a.out.resolve();need(a.resume or not out.exists() or not any(out.iterdir()),"fresh output or explicit resume")
 out.mkdir(parents=True,exist_ok=True)
 receipt={"format":"isp-exact-rational-selected-koszul-support-v1","status":"running",
  "secondsLimit":a.seconds,"memoryMiBPerProcess":a.memory_mib,
  "oldNormalFormsRecomputed":False,"newOriginalDixonDigitsComputed":0,
  "largeFilesTemporaryOnly":True,"largeDataUploadedOrCommitted":False,
  "allOriginal4367IntegerProductsZero":False,"parameters":{},"events":[]}
 temps=[];verified=[];code=1
 def check():
  if time.monotonic()>=deadline:raise BudgetExpired("actual shared deadline")
 def remember(p):
  rr={"file":p.name,**sha(p),"temporaryOnly":True}
  if not any(z["file"]==rr["file"] for z in temps):temps.append(rr)
  return rr
 def checkpoint():
  receipt["parameters"]["temporaryFiles"]=temps
  receipt["parameters"]["verifiedColumns"]=verified
  receipt["mathematicalElapsedSeconds"]=time.monotonic()-start
  save(out/"koszul-exact-rational-support-receipt.json",receipt)
 try:
  need(sha(a.helper)["sha256"]==H_SHA and sha(a.point_model)["sha256"]==P_SHA,"paid helper/point bytes")
  sp=importlib.util.spec_from_file_location("paid_helper",a.helper);H=importlib.util.module_from_spec(sp);sp.loader.exec_module(H)
  from flint import fmpq_mat,nmod_mat
  prep=read(a.prepared_dir/"koszul-exact-sparse-preparation-receipt.json")
  need(prep["status"]=="completed" and prep["exactQKernelBijectionRecorded"] is True,"completed exact sparse preparation")
  pm=a.prepared_dir/"exact-original-koszul-outside-model.json.gz"
  pc=a.prepared_dir/"exact-koszul-sparse-core-and-dag.json.gz"
  pfiles={x["file"]:x for x in prep["parameters"]["temporaryFiles"]}
  for p in [pm,pc]:
   got=sha(p);expected=pfiles[p.name];need(got["bytes"]==expected["bytes"] and got["sha256"]==expected["sha256"],"prepared actual bytes")
  model=read(pm);core=read(pc)
  need(model["binding"]==core["binding"]==prep["parameters"]["binding"],"preparation binding")
  material={"codeSHA256":sha(__file__)["sha256"],"core":sha(pc),"original":sha(pm),"helper":H_SHA,"point":P_SHA}
  binding=hashlib.sha256(json.dumps(material,sort_keys=True,separators=(",",":")).encode()).hexdigest()
  receipt["parameters"].update({"binding":binding,"inputIdentity":material,"preparedBinding":model["binding"],
      "declaredPaid23Slots":PAID,"exactSolveDoesNotTreatMod31CoefficientsAsRational":True})
  rows=rows_of(core["coreRows"]);av=list(map(int,core["activeVariables"]));m=len(rows);n=len(av)
  phi=rows_of(model["phiRows"]);outside=list(map(int,model["outsideRows"]));free=list(map(int,model["freeRows"]))
  need(len(phi)==6188 and len(outside)==1834 and len(free)==36,"full original dictionaries")
  profile_path=out/"exact-unit-block-profile.json"
  if profile_path.exists():
   pr=read(profile_path);need(pr["binding"]==binding and pr["coreFileIdentity"]==sha(pc),"saved profile binding")
   receipt["events"].append("reused complete exact-unit-block profile")
  else:
   check()
   M=nmod_mat(m,n,[row.get(j,0)%31 for row in rows for j in av],31)
   R,rank=M.rref();rank=int(rank);ppos=pivots(R,rank,n)
   pp=[av[j] for j in ppos];ps=set(pp);ff=[j for j in av if j not in ps]
   if rank:
    TT=nmod_mat(rank,m,[row.get(j,0)%31 for j in pp for row in rows],31)
    RT,rt=TT.rref();need(int(rt)==rank,"same full rank for column transpose")
    ii=pivots(RT,rank,m)
    # The selected original integer unit block has nonzero determinant mod31.
    BB=nmod_mat(rank,rank,[rows[i].get(j,0)%31 for i in ii for j in pp],31)
    need(int(BB.rref()[1])==rank,"complete selected unit block rank")
   else:ii=[]
   pr={"format":"isp-exact-koszul-unit-block-profile-v1","binding":binding,"coreFileIdentity":sha(pc),
       "coreRows":m,"coreVariables":n,"unitRankModulo31":rank,"unitRowPositions":ii,
       "pivotVariables":pp,"freeVariables":ff,"unitBlockNonzeroModulo31Verified":True}
   save(profile_path,pr);del M,R
  remember(profile_path);rank=len(pr["pivotVariables"]);ff=pr["freeVariables"];pp=pr["pivotVariables"];f=len(ff)
  receipt.update({"coreRows":m,"coreVariables":n,"unitRankModulo31":rank,"candidateGraphColumns":f})
  checkpoint();check()
  # A complete solver output is retained even if later source verification times out.
  solution_path=out/"exact-unit-block-solution.json.gz";srp=out/"exact-unit-block-solve-receipt.json"
  if solution_path.exists():
   sol=read(solution_path);need(sol["binding"]==binding and sol["profileIdentity"]==sha(profile_path),"saved exact solve binding")
   receipt["events"].append("reused exact rational unit-block solution")
  else:
   log=out/"exact-unit-block-solve.log";remaining=max(.01,deadline-time.monotonic())
   cmd=[sys.executable,"-B",str(pathlib.Path(__file__).resolve()),"--solve-worker","--core",str(pc),"--profile",str(profile_path),"--out",str(out)]
   ws=time.monotonic()
   with log.open("w") as logf:
    proc=subprocess.Popen(cmd,stdout=logf,stderr=subprocess.STDOUT,start_new_session=True)
    try:proc.wait(timeout=remaining)
    except subprocess.TimeoutExpired:
     os.killpg(proc.pid,signal.SIGKILL);proc.wait()
     receipt["events"].append({"exactSolveStoppedAtDeadline":True,"exitCode":proc.returncode,"elapsedSeconds":time.monotonic()-ws})
     raise BudgetExpired("exact rational solve at shared deadline; input core/profile retained")
   need(proc.returncode==0 and solution_path.exists(),"exact unit-block solver completion")
   sol=read(solution_path);need(sol["binding"]==binding,"new solve binding")
  remember(solution_path)
  if srp.exists():remember(srp)
  need((sol["rows"],sol["columns"])==(rank,f),"all unit solution dimensions")
  kernel_path=out/"exact-koszul-source-coefficient-basis.json.gz"
  if kernel_path.exists():
   kb=read(kernel_path);need(kb["binding"]==binding,"exact kernel basis binding")
   basis=[[int(x) for x in v] for v in kb["primitiveIntegerColumns"]]
   need(all(len(v)==1632 for v in basis),"complete1632 saved source coefficients")
   receipt["events"].append("reused complete exact source-coefficient kernel")
  else:
   # Reverse each sparse two-variable equation once as a one-variable rational map.
   roots={j:j for j in av};ratios={j:fractions.Fraction(1) for j in av}
   for d in reversed(core["eliminationDAG"]):
    p=int(d["pivot"]);t=d["target"]
    if t is None:roots[p]=None;ratios[p]=fractions.Fraction(0)
    else:
     t=int(t);need(t in roots,"topological inverse DAG")
     roots[p]=roots[t];ratios[p]=(-fractions.Fraction(int(d["b"]),int(d["a"])))*ratios[t]
   need(len(roots)==1632,"all1632 DAG source variables")
   dagden=1
   for x in ratios.values():dagden=math.lcm(dagden,x.denominator)
   factors={j:int(x.numerator)*(dagden//x.denominator) for j,x in ratios.items()}
   graph=[]
   for col in range(f):
    check();den=1
    for i in range(rank):den=math.lcm(den,int(sol["solutionPairsByRows"][i][col][1]))
    x={j:0 for j in av};x[ff[col]]=den
    for i,j in enumerate(pp):
     u,v=map(int,sol["solutionPairsByRows"][i][col]);x[j]=-u*(den//v)
    v=[0 if roots[j] is None else x[roots[j]]*factors[j] for j in range(1632)]
    graph.append(canonical(v))
   # Check every original outside row, before accepting any mod31 free direction.
   residual=[[0]*f for _ in outside]
   for oi,raw in enumerate(outside):
    row=phi[raw-1]
    for j,v in row.items():
     for c in range(f):residual[oi][c]+=v*graph[c][j]
    if oi%64==0:check()
   # Check the chosen core equations separately, with the active graph before DAG.
   # The original residual alone will certify final kernels; solver correctness is
   # also paid here by B*(-X)+E at its actual rational graph.
   for c in range(f):
    den=1
    for i in range(rank):den=math.lcm(den,int(sol["solutionPairsByRows"][i][c][1]))
    x={j:0 for j in av};x[ff[c]]=den
    for i,j in enumerate(pp):
     u,v=map(int,sol["solutionPairsByRows"][i][c]);x[j]=-u*(den//v)
    for i in pr["unitRowPositions"]:
     need(sum(v*x[j] for j,v in rows[i].items())==0,"original integer selected unit-block product")
    check()
   residual_path=out/"complete-original-outside-graph-residual.json.gz"
   rr=save(residual_path,{"binding":binding,"rows":1834,"columns":f,"integerRows":[[str(x) for x in row] for row in residual]})
   temps.append(rr)
   if f:
    RR,rrank=fmpq_mat(1834,f,[x for row in residual for x in row]).rref();rrank=int(rrank)
    piv=pivots(RR,rrank,f);free_c=[j for j in range(f) if j not in set(piv)]
    basis=[]
    for c in free_c:
     coeff=[fractions.Fraction(0) for _ in range(f)];coeff[c]=1
     for i,p in enumerate(piv):coeff[p]=-fractions.Fraction(int(RR[i,c].p),int(RR[i,c].q))
     den=1
     for x in coeff:den=math.lcm(den,x.denominator if isinstance(x,fractions.Fraction) else 1)
     cc=[int(x*den) for x in coeff]
     basis.append(canonical([sum(cc[c]*graph[c][j] for c in range(f) if cc[c]) for j in range(1632)]))
   else:rrank=0;basis=[]
   need(len(basis)==f-rrank and len(basis)<=29,"exact dimension and paid finite-field upper bound")
   kb={"format":"isp-complete-exact-koszul-coefficient-kernel-v1","binding":binding,
       "primitiveIntegerColumns":[[str(x) for x in v] for v in basis],
       "unitRank":rank,"graphResidualRankOverQ":rrank,"dimensionOverQ":len(basis),
       "exactOriginalOutsideRankOverQ":len(core["eliminationDAG"])+rank+rrank,
       "selectedUnitBlockIntegerProductsVerified":True,
       "completeAll1834GraphResidualUsed":True}
   save(kernel_path,kb)
  remember(kernel_path);checkpoint();check()
  point=read(a.point_model);terms=H.original_row_terms(point)
  dim=len(basis);free_image=[];all_cert=[]
  for k,coeff in enumerate(basis):
   check();cp=out/("exact-selected-koszul-kernel-%03d.json.gz"%k)
   ksha=vecsha(coeff)
   if cp.exists():
    cert=read(cp);need(cert["binding"]==binding and cert["koszulCoefficientSHA256"]==ksha and
      cert["all1834OutsideSourceCoefficientsZero"] and cert["all4367ExactIntegerProductsZero"],"saved full source certificate")
    nums=[int(x) for x in cert["original6188IntegerCoefficients"]]
    need(len(nums)==6188,"saved all6188")
    receipt["events"].append({"reusedVerifiedKernel":k})
   else:
    nums=[]
    for raw,row in enumerate(phi):
     nums.append(sum(v*coeff[j] for j,v in row.items()))
     if raw%128==0:check()
    need(all(nums[i-1]==0 for i in outside),"all1834 original outside source entries")
    product=H.exact_product(nums,terms,check)
    need(len(product)==4367 and all(x==0 for x in product),"all4367 original INTEGER products")
    cert={"format":"isp-exact-original-koszul-selected-source-certificate-v1","binding":binding,"column":k,
      "koszulCoefficientSHA256":ksha,"all1632KoszulCoefficients":[str(x) for x in coeff],
      "original6188IntegerCoefficients":[str(x) for x in nums],
      "all1834OutsideSourceCoefficientsZero":True,"all4367ExactIntegerProductsZero":True,
      "fullOriginalProductSHA256":vecsha(product),"free36IntegerCoefficients":[str(nums[i-1]) for i in free]}
    save(cp,cert)
   fr=[nums[i-1] for i in free];free_image.append(fr)
   file_rec=remember(cp);verified.append({"column":k,"sourceSHA256":vecsha(nums),"certificate":file_rec,
      "maximumSourceIntegerBits":max((abs(x).bit_length() for x in nums),default=0),
      "nonzeroOriginalSourceRows":sum(x!=0 for x in nums),"all4367ExactIntegerProductsZero":True})
   checkpoint()
  rankfree=int(fmpq_mat(36,dim,[free_image[c][r] for r in range(36) for c in range(dim)]).rank()) if dim else 0
  union=int(fmpq_mat(36,dim+23,[x for r in range(36) for x in
      ([free_image[c][r] for c in range(dim)]+[int(r==j) for j in PAID])]).rank())
  need(rankfree==dim and 23<=union<=36,"complete free coordinate independence")
  free_path=out/"exact-selected-koszul-free36-image.json.gz"
  remember_rec=save(free_path,{"binding":binding,"rows":36,"columns":dim,
      "integerColumns":[[str(x) for x in v] for v in free_image],"rankOverQ":rankfree,
      "unionWithPaid23RankOverQ":union})
  temps.append(remember_rec)
  receipt.update({"status":"completed","selectedStandardKoszulDimensionOverQ":dim,
   "outsideSupportRankOverQ":1632-dim,"complete36FreeImageRankOverQ":rankfree,
   "unionWithPaid23FreeAxesRankOverQ":union,"newTrueIndependentDirectionsBeyondPaid23":union-23,
   "selectedOriginalMatrixRankLowerBound":4318,"selectedOriginalMatrixRankUpperBound":4354-union,
   "all1834OutsideSourceCoefficientsZero":True,"allOriginal4367IntegerProductsZero":True,
   "completeKernelDimensionCertifiedOverQ":True,"paid23FreeAxesContainedInNewExactImage":union==dim})
  code=0
 except BudgetExpired as e:receipt.update(status="budget-exhausted",error=str(e));code=75
 except Exception as e:
  receipt.update(status="failed",error=str(e),exceptionType=type(e).__name__)
  (out/"exception.log").write_text(traceback.format_exc());code=1
 finally:
  checkpoint()
  need((out/"koszul-exact-rational-support-receipt.json").stat().st_size<100000,"small long-term receipt cap")
 print(json.dumps(receipt),flush=True);return code
if __name__=="__main__":
 if len(sys.argv)>1 and sys.argv[1]=="--solve-worker":sys.exit(worker(sys.argv[2:]))
 sys.exit(main(sys.argv[1:]))
