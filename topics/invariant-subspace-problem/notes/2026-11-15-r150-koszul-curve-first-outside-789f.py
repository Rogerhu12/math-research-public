#!/usr/bin/env python3
"""First outside-source jets of the paid29 exact original Koszul curves.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
Only fixed constant combinations of paid curves; no new1603 solve or maximality claim.
"""
import argparse,gzip,hashlib,itertools,json,math,os,pathlib,resource,signal,subprocess,sys,time,traceback
sys.dont_write_bytecode=True
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
for _n in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS","NUMEXPR_NUM_THREADS"):os.environ[_n]="1"
PIN={
 "source_model":(814572,"0aa2d6d5c368b9885e279cd5b8e2cc7a59ba574ca161c0535193c30defe52d3d"),
 "basis":(1670175,"b2421f22d40ed376302982f049fa63a35f811ab9899604abc58c964e3a4a2808"),
 "free_image":(29488,"24f4cbd8ca7c39d5c6280159b71cf8fc85fd9811a1dc9bc6f8bdeb50a977f249"),
 "support_receipt":(18271,"1615d967b7e004803e82b8a057d106d0de7617788a5e573ed65d04f48f1aa47f"),
 "coefficients":(20582,"bfa40dd550fad408f4253484d31ceec39c4524f2f25c9fbade15911f39a776d3"),
 "first_receipt":(15594,"ef7b8a3f935eb376353a235c95d257b8f0785c7459d7c45b348b6e238390fb62")}
Q_BIND="10890e55000e9e0554b2488f333b899dbf224421e5bf091adc24d396348cc6a4"
F_BIND="479d3295113d0e1ea0bc5e2b404a0426e5f584229a16dcfdb18aa2d6ef5dac31"
class BudgetExpired(Exception):pass
def need(x,s):
 if not x:raise ValueError(s)
def identity(p):
 h=hashlib.sha256();n=0
 with pathlib.Path(p).open("rb") as f:
  while True:
   b=f.read(1048576)
   if not b:break
   n+=len(b);h.update(b)
 return {"bytes":n,"sha256":h.hexdigest()}
def checked(p,pin):
 need(identity(p)=={"bytes":pin[0],"sha256":pin[1]},"actual input byte identity "+str(p))
 with (gzip.open(p,"rt",encoding="utf-8") if str(p).endswith(".gz") else pathlib.Path(p).open("r",encoding="utf-8")) as f:return json.load(f)
def read(p):
 with (gzip.open(p,"rt",encoding="utf-8") if str(p).endswith(".gz") else pathlib.Path(p).open("r",encoding="utf-8")) as f:return json.load(f)
def save(p,x):
 p=pathlib.Path(p);q=p.with_name(p.name+".partial")
 if p.suffix==".gz":
  with gzip.open(q,"wt",encoding="utf-8",compresslevel=1) as f:json.dump(x,f,separators=(",",":"))
 else:q.write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 os.replace(q,p);return {"file":p.name,**identity(p),"temporaryOnly":True}
def vecsha(v):
 h=hashlib.sha256()
 for a in v:h.update((str(a)+"\n").encode())
 return h.hexdigest()
def primitive(v):
 g=0
 for a in v:g=math.gcd(g,abs(a))
 if not g:return v
 sign=-1 if next(a for a in v if a)<0 else 1
 return [sign*(a//g) for a in v]
def worker(argv):
 ap=argparse.ArgumentParser()
 ap.add_argument("--input",required=True,type=pathlib.Path);ap.add_argument("--out",required=True,type=pathlib.Path)
 a=ap.parse_args(argv);start=time.monotonic()
 from flint import fmpq_mat
 data=read(a.input);rows=[[int(x) for x in row] for row in data["integerRows"]]
 need(len(rows)==1834 and all(len(r)==29 for r in rows),"complete original outside1834 by29")
 kernel_path=a.out/"first-outside-complete-kernel29.json.gz"
 if kernel_path.exists():
  result=read(kernel_path)
  need(result["binding"]==data["binding"] and result["matrixIdentity"]==identity(a.input),"saved exact small solver binding")
  r=int(result["rankOverQ"]);free=list(map(int,result["freeColumns"]))
  cols=[[int(x) for x in v] for v in result["primitiveIntegerKernelColumns"]]
  need(len(cols)==29-r and all(len(v)==29 for v in cols),"saved complete exact small solver shape")
 else:
  active=[];contents=[];indices=[]
  for i,row in enumerate(rows):
   if not any(row):continue
   p=primitive(row);g=next(row[j]//p[j] for j in range(29) if p[j])
   need(all(x==g*y for x,y in zip(row,p)),"exact nonzero row content transport")
   active.append(p);contents.append(str(g));indices.append(i)
  M=fmpq_mat(len(active),29,[x for row in active for x in row])
  R,r=M.rref();r=int(r)
  piv=[];j=0
  for i in range(r):
   while j<29 and R[i,j]==0:j+=1
   need(j<29,"exact small rank profile");piv.append(j);j+=1
  free=[j for j in range(29) if j not in set(piv)];cols=[]
  for k in free:
   den=1
   for i in range(r):den=math.lcm(den,int(R[i,k].q))
   v=[0]*29;v[k]=den
   for i,p in enumerate(piv):v[p]=-int(R[i,k].p)*(den//int(R[i,k].q))
   cols.append(primitive(v))
  # Save the exact solver output before the complete original matrix product.
  result={"format":"isp-paid29-unadjusted-first-outside-kernel-v1","binding":data["binding"],
   "matrixIdentity":identity(a.input),"rankOverQ":r,"kernelDimension":len(cols),
   "pivotColumns":piv,"freeColumns":free,"primitiveIntegerKernelColumns":[list(map(str,v)) for v in cols],
   "nonzeroOriginalRowIndices":indices,"originalRowContents":contents,
   "allOriginalProductsVerified":False,"elapsedSeconds":time.monotonic()-start}
  kernel_path=a.out/"first-outside-complete-kernel29.json.gz";save(kernel_path,result)
 
 for row in rows:
  for v in cols:need(sum(x*y for x,y in zip(row,v))==0,"complete original1834 outside derivative kernel product")
 need(len(cols)==29-r and all(cols[i][free[j]]==0 for i in range(len(cols)) for j in range(len(cols)) if i!=j),
   "complete small source kernel independent free block")
 need(all(cols[i][free[i]]!=0 for i in range(len(cols))),"nonzero complete small free diagonal")
 result["allOriginalProductsVerified"]=True;result["elapsedSeconds"]=time.monotonic()-start;rr=save(kernel_path,result)
 receipt={"status":"completed","binding":data["binding"],"outsideFirstRankOverQ":r,"secondOrderOutsideDimension":29-r,
   "all1834ExactOutsideKernelProductsZero":True,"allKernelFreeCoordinatesIndependent":True,
   "kernelFile":rr,"elapsedSeconds":time.monotonic()-start}
 save(a.out/"first-outside-small-kernel-receipt.json",receipt);print(json.dumps(receipt),flush=True);return 0
def main(argv):
 ap=argparse.ArgumentParser()
 for n in ("support-dir","source-model","first-dir","out"):ap.add_argument("--"+n,type=pathlib.Path,required=True)
 ap.add_argument("--seconds",type=float,default=30);ap.add_argument("--memory-mib",type=int,default=512)
 a=ap.parse_args(argv);need(0<a.seconds<=180 and 0<a.memory_mib<=2048,"explicit finite first outside budget")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 start=time.monotonic();deadline=start+a.seconds-min(2.0,a.seconds/10)
 out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 receipt={"format":"isp-paid29-original-koszul-first-outside-source-v1","status":"running","phase":"inputs",
  "old1603RationalEliminationRepeated":False,"oldOriginalConstantRankEliminationRepeated":False,
  "newDixonDigitsComputed":0,"largeDataUploadedOrCommitted":False,
  "maximumSecondOrderSourceSpaceComputed":False,"parameters":{},"events":[]}
 rp=out/"koszul-curve-first-outside-receipt.json";temps=[];binding=None;code=1
 def check():
  if time.monotonic()>=deadline:raise BudgetExpired("shared exact first outside clock")
 def keep(p):
  r={"file":p.name,**identity(p),"temporaryOnly":True}
  temps[:]=[z for z in temps if z["file"]!=r["file"]];temps.append(r);return r
 def checkpoint():
  receipt["mathematicalElapsedSeconds"]=time.monotonic()-start
  receipt["parameters"]["temporaryFiles"]=temps;save(rp,receipt)
 def beat(p):
  receipt["phase"]=p;checkpoint();print(json.dumps({"phase":p,"elapsedSeconds":time.monotonic()-start}),flush=True);check()
 try:
  paths={
   "source_model":a.source_model,
   "basis":a.support_dir/"exact-koszul-source-coefficient-basis.json.gz",
   "free_image":a.support_dir/"exact-selected-koszul-free36-image.json.gz",
   "support_receipt":a.support_dir/"koszul-exact-rational-support-receipt.json",
   "coefficients":a.first_dir/"same-original-natural-constant-and-first-coefficients.json.gz",
   "first_receipt":a.first_dir/"selected-natural-first-connection-f31-receipt.json"}
  d={k:checked(p,PIN[k]) for k,p in paths.items()}
  material={"sourceSHA256":identity(__file__)["sha256"],"inputs":{k:identity(p) for k,p in paths.items()},
   "fixedFamily":"i<j lex; factor1,m0,...,m10; F_j e_i-F_i e_j",
   "naturalParameter":"u=1/s; original u10 L and u5 Gamma","noCurveCoefficientCorrection":True}
  binding=hashlib.sha256(json.dumps(material,sort_keys=True,separators=(",",":")).encode()).hexdigest()
  receipt["parameters"].update({"binding":binding,"inputIdentity":material,"secondsLimit":a.seconds,"memoryMiB":a.memory_mib,
    "scope":"fixed constant combinations of the paid29 exact polynomial Koszul curves"})
  sr=d["support_receipt"];first=d["first_receipt"];coeff=d["coefficients"];kb=d["basis"];fi=d["free_image"];model=d["source_model"]
  need(sr["status"]=="completed" and sr["parameters"]["binding"]==Q_BIND and sr["selectedStandardKoszulDimensionOverQ"]==29
    and sr["allOriginal4367IntegerProductsZero"] and sr["completeKernelDimensionCertifiedOverQ"],"complete paid29 source identity")
  need(kb["binding"]==fi["binding"]==Q_BIND and fi["rankOverQ"]==29,"same29 complete coefficient and free image")
  need(first["status"]=="completed" and first["parameters"]["binding"]==coeff["binding"]==F_BIND
    and first["allOriginalParameterCoefficientsModulo31Verified"] and first["all1309ExactPrimitiveConstantCoefficientsVerified"],
    "same paid whole natural primitive coefficients")
  X=[[int(v) for v in row] for row in kb["primitiveIntegerColumns"]]
  need(len(X)==29 and all(len(v)==1632 for v in X),"all paid1632 coefficients per29 columns")
  F0=[[int(v) for v in row] for row in coeff["constant"]];F1=[[int(v) for v in row] for row in coeff["naturalFirst"]]
  need(len(F0)==len(F1)==17 and all(len(v)==77 for v in F0+F1),"all original17 by77 natural coefficients")
  outside=list(map(int,model["outsideRows"]));free=list(map(int,model["freeRows"]));J=set(map(int,model["selectedRows"]))
  need(len(outside)==1834 and set(outside)==set(range(1,6189))-J and len(J)==4354 and len(set(free))==36,"same complete original source split")
  mx=out/"all1834-first-outside-source-matrix.json.gz";prep=out/"first-outside-original-products-receipt.json"
  if mx.exists() and prep.exists():
   pr=read(prep);need(pr["binding"]==binding and pr["matrixIdentity"]==identity(mx),"same actual complete outside matrix")
   need(pr["all29PaidConstantSourcesMatched"] and pr["all4367ExactFirstSyzygyProductsZero"],"complete original preparation cache")
   receipt["events"].append({"reusedCompleteOriginalFirstSourceProducts":True});keep(mx);keep(prep)
  else:
   beat("whole-original-koszul-source-jets")
   var=[8**i for i in range(11)]
   multipliers=[sum(var[i] for i in q) for degree in range(4) for q in itertools.combinations_with_replacement(range(11),degree)]
   mi={v:i for i,v in enumerate(multipliers)}
   terms=var+[var[i]+var[j] for i in range(11) for j in range(i,11)]
   original_keys=[sum(var[i] for i in q) for degree in range(5,0,-1) for q in itertools.combinations_with_replacement(range(11),degree)]
   oi={v:i for i,v in enumerate(original_keys)}
   phi0=[{} for _ in range(6188)];phi1=[{} for _ in range(6188)];col=0
   for i in range(17):
    for j in range(i+1,17):
     for factor in [0]+var:
      for e,pol,sign in ((i,j,1),(j,i,-1)):
       for k,key in enumerate(terms):
        row=17*mi[key+factor]+e
        for phi,F in ((phi0,F0),(phi1,F1)):
         v=F[pol][k]
         if v:phi[row][col]=phi[row].get(col,0)+sign*v
      col+=1
    check()
   need(col==1632,"same complete standard source family")
   phi0=[{j:v for j,v in row.items() if v} for row in phi0]
   phi1=[{j:v for j,v in row.items() if v} for row in phi1]
   old=[{int(j):int(v) for j,v in row} for row in model["phiRows"]]
   need(phi0==old,"every paid original constant Koszul coefficient identity")
   del old
   V0=[[0]*29 for _ in range(6188)];V1=[[0]*29 for _ in range(6188)]
   for r in range(6188):
    for phi,V in ((phi0,V0),(phi1,V1)):
     for j,v in phi[r].items():
      for k in range(29):
       if X[k][j]:V[r][k]+=v*X[k][j]
    if r%256==0:check()
   oldhash={int(z["column"]):z["sourceSHA256"] for z in sr["parameters"]["verifiedColumns"]}
   need(len(oldhash)==29,"all29 paid source column identities")
   hashes0=[];hashes1=[]
   for k in range(29):
    h0=vecsha(V0[r][k] for r in range(6188));need(h0==oldhash[k],"complete paid6188 source column "+str(k))
    hashes0.append(h0);hashes1.append(vecsha(V1[r][k] for r in range(6188)))
   need(all(not any(V0[r-1]) for r in outside),"all original1834 constant outside sources vanish")
   fcols=[[int(x) for x in row] for row in fi["integerColumns"]]
   need(len(fcols)==29 and all(len(v)==36 for v in fcols),"paid complete36 free image")
   need(all(V0[free[j]-1][k]==fcols[k][j] for j in range(36) for k in range(29)),"every paid original free source coefficient")
   beat("complete-original-first-syzygy-products")
   products=[[0]*29 for _ in range(4367)]
   for r in range(6188):
    e=r%17;mul=multipliers[r//17]
    a0=[(k,v) for k,v in enumerate(V0[r]) if v];a1=[(k,v) for k,v in enumerate(V1[r]) if v]
    if a0 or a1:
     for j,key in enumerate(terms):
      z0,z1=F0[e][j],F1[e][j]
      if z0 or z1:
       row=products[oi[mul+key]]
       if z0:
        for k,v in a1:row[k]+=z0*v
       if z1:
        for k,v in a0:row[k]+=z1*v
    if r%128==0:check()
   need(not any(any(row) for row in products),"all4367 exact A0 Phi1 X + A1 Phi0 X products")
   mdata={"format":"isp-original-first-outside-koszul-29-v1","binding":binding,
     "originalOutsideSourceRows":outside,"rows":1834,"columns":29,
     "integerRows":[[str(x) for x in V1[r-1]] for r in outside]}
   save(mx,mdata);keep(mx)
   pr={"status":"completed","binding":binding,"matrixIdentity":identity(mx),
    "all29PaidConstantSourcesMatched":True,"all6188ConstantFamilyCoefficientsMatched":True,
    "all1834ConstantOutsideSourcesZero":True,"all36FreeCoordinatesMatchPaidIndependentImage":True,
    "all4367ExactFirstSyzygyProductsZero":True,"constantSourceSHA256ByColumn":hashes0,
    "naturalFirstSourceSHA256ByColumn":hashes1,
    "nonzeroOutsideFirstRows":sum(any(V1[r-1]) for r in outside),
    "nonzeroOutsideFirstEntries":sum(v!=0 for r in outside for v in V1[r-1]),
    "maximumOutsideFirstIntegerBits":max((abs(v).bit_length() for r in outside for v in V1[r-1]),default=0)}
   save(prep,pr);keep(prep)
   del phi0,phi1,V0,V1,products,mdata,X
  receipt["parameters"]["originalSourcePreparation"]=pr
  beat("exact-small29-column-kernel")
  kr=out/"first-outside-small-kernel-receipt.json";kp=out/"first-outside-complete-kernel29.json.gz"
  if kr.exists() and kp.exists():
   krec=read(kr);need(krec["binding"]==binding and krec["status"]=="completed","same complete small kernel")
   need(krec["kernelFile"]["bytes"]==identity(kp)["bytes"] and krec["kernelFile"]["sha256"]==identity(kp)["sha256"],"same complete small kernel bytes")
   receipt["events"].append({"reusedCompleteOutsideFirstKernel":True})
  else:
   log=out/"exact-small29-kernel.log";remaining=max(.01,deadline-time.monotonic())
   with log.open("wb") as f:
    p=subprocess.Popen([sys.executable,"-B",str(pathlib.Path(__file__).resolve()),"--small-kernel-worker",
      "--input",str(mx),"--out",str(out)],stdout=f,stderr=subprocess.STDOUT,start_new_session=True)
    try:ret=p.wait(timeout=remaining)
    except subprocess.TimeoutExpired:
     os.killpg(p.pid,signal.SIGKILL);p.wait();receipt["events"].append({"smallKernelStoppedAtDeadline":True,"exitCode":p.returncode})
     raise BudgetExpired("exact small29 kernel stopped; complete original M retained")
   need(ret==0 and kr.exists() and kp.exists(),"complete exact small29 kernel; see saved worker log")
   krec=read(kr)
  keep(kp);keep(kr);need(krec["all1834ExactOutsideKernelProductsZero"] and krec["allKernelFreeCoordinatesIndependent"],"all exact small original products")
  rank=int(krec["outsideFirstRankOverQ"]);t2=int(krec["secondOrderOutsideDimension"])
  need(0<=rank<=29 and t2==29-rank,"actual fixed29 outside flag dimensions")
  receipt.update({"status":"completed","phase":"complete","outsideFirstRankOverQ":rank,
   "fixedPaidCurveFirstOrderDimension":29,"fixedConstantCombinationSecondOrderDimension":t2,
   "all29PaidConstantSourcesMatched":True,"all4367ExactFirstSyzygyProductsZero":True,
   "all1834ExactOutsideKernelProductsZero":True,"completeKernelOfThisFixedOutsideMatrixComputed":True,
   "allSecondOrderConstantHeadsIndependent":True})
  # These are source factors only; full-matrix Smith lower bounds are separately paid.
  g=29+t2;loss=1 if t2==0 else 2
  receipt["parameters"].update({"outsideFirstRankOverQ":rank,"fixedSecondOrderDimension":t2,
   "sourceDeterminantFactorOrder":g,"sourceNextMinorFactorOrder":g-loss,
   "maximumSourceWeight":loss,"fullSmithOrderNotInsertedByThisRun":True,
   "remainingAllowance":"u-dependent corrections by other Koszul columns have not been optimized",
   "completeOriginalCurveIdentity":"A^h(u) Phi(u) X=0 exactly; Phi0 X paid, Phi1 X freshly verified",
   "kernelFile":krec["kernelFile"],"newFirstSourceCurveIdentities":pr})
  code=0
 except BudgetExpired as e:receipt.update(status="budget-exhausted",error=str(e));code=75
 except Exception as e:
  receipt.update(status="failed",error=str(e),exceptionType=type(e).__name__);(out/"exception.log").write_text(traceback.format_exc());code=1
 finally:
  checkpoint()
 need(rp.stat().st_size<100000,"small permanent original curve receipt")
 print(json.dumps(receipt,ensure_ascii=False),flush=True);return code
if __name__=="__main__":
 if len(sys.argv)>1 and sys.argv[1]=="--small-kernel-worker":sys.exit(worker(sys.argv[2:]))
 sys.exit(main(sys.argv[1:]))
