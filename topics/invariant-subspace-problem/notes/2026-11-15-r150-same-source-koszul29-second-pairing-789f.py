#!/usr/bin/env python3
"""Pair the actual same-J 29 Koszul source kernels with the paid second forcing.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
Only lost temporary 29-source data are reconstructed by the unchanged paid solver.
All large data remain temporary. No normal5 restart or new M0 solve is performed.
"""
import argparse,gzip,hashlib,importlib.util,io,itertools,json,math,os,pathlib,resource,signal,subprocess,sys,time,traceback
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
  need(len(b)<100000,"only small uncompressed metadata");q.write_bytes(b)
 os.replace(q,p);return {"file":p.name,**identity(p),"temporaryOnly":True}
def vecsha(v):
 h=hashlib.sha256()
 for x in v:h.update((str(x)+"\n").encode())
 return h.hexdigest()
def pivots(R,rank):
 ans=[]
 for i in range(int(rank)):
  j=next((j for j in range(R.ncols()) if R[i,j]),None)
  need(j is not None and R[i,j]==1,"complete normalized rational RREF")
  ans.append(j)
 need(ans==sorted(set(ans)),"increasing pivot columns")
 return ans
def qcolumn_primitive(v):
 den=1
 for x in v:den=math.lcm(den,int(x.q))
 z=[int(x.p)*(den//int(x.q)) for x in v];g=0
 for x in z:g=math.gcd(g,abs(x))
 need(g>0,"nonzero rational kernel column")
 sg=-1 if next(x for x in z if x)<0 else 1
 return [sg*(x//g) for x in z]
def import_file(name,p):
 sp=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
PINS={
 "helper":(22765,"9332d9d394b1a17444c9ccc20b3971cf74b7e932cffc8d9189e4e2f64fe0c428"),
 "preparation":(7833,"7fcaee1cf34ea2545f10050fbb899e6d2a682a61485e2351214250072d819170"),
 "support_solver":(17287,"0689aec8f35c098a3d1e831297b94102ec38596fe724ac63cdf4bbc9c012e7a2"),
 "point_model":(87459,"97d31570a0bd99d33066fc6ea47984203b2964521ceeb50920f0a49dd3bb8074"),
 "native_model":(128145,"291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6"),
 "old_unit":(9008513,"c53406d65cfd66f2f3b6f1c946bd7495e44c7041538c4f3c85518eb7be7d5dfe"),
 "coefficients":(20580,"7ab537a3c8f9a3d13b924a23f37f8d4ce4fa7621e3608920404ed0051b2fd5c1"),
 "old_full":(12690,"b186ecd4ef8a8ca910392a8900c838da1e9e166a0b4738b40748677fd7e14a70")}
SELECTED_SHA="5cd9543de68bdb562bbe21189d5b0712248e6943c5572fe38ff27ec4fc1f5f68"
PAID_SECOND="c40049455e9f310607586b55cc271ca00636dc954f0de63693d0da886a6d067e"
def pairing_worker(invpath,support,out):
 from flint import fmpz_mat,fmpq_mat
 inv=read(invpath);paths=inv["paths"];bind=inv["binding"];out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True)
 start=time.monotonic();cp=out/"same-source-koszul29-pairing-worker-receipt.json"
 rec={"status":"running","phase":"exact-source-scope","binding":bind,"parameters":{},"outputs":[]}
 def ck():
  rec["elapsedSeconds"]=time.monotonic()-start;save(cp,rec)
 def output(p):
  z={"file":p.name,**identity(p),"temporaryOnly":True}
  rec["outputs"]=[a for a in rec["outputs"] if a["file"]!=p.name]+[z]
  return z
 ck()
 for k,p in paths.items():need(identity(p)==inv["inputIdentities"][k],"same actual input before pairing: "+k)
 H=import_file("paid_same_source_helper",paths["helper"])
 point=read(paths["point_model"]);co=read(paths["coefficients"]);unit=read(paths["old_unit"]);paid=read(paths["old_full"])
 F0=[list(map(int,r)) for r in co["constant"]]
 need(co["all1309ConstantIdentitiesVerified"] and
 F0==[list(map(int,r)) for r in point["primitivePointCoefficients"]],"all1309 actual natural-infinity constant coefficients equal the paid point model")
 need(len(F0)==17 and all(len(r)==77 for r in F0) and point["characteristicZeroSameOriginal17Verified"],
 "complete original characteristic-zero17 by77")
 need(unit["binding"]==paid["binding"]==PAID_SECOND and paid["status"]=="completed" and
 paid["secondHeadImageDimension"]==22 and paid["smallResidualRank"]==14 and
 paid["all4354OriginalSecondLeftProductsZero"] and paid["firstHeadComplementResidualRank"]==3,
 "paid22 original second heads and complete first three-column complement")
 J=list(map(int,unit["originalSourceRows"]));selected=H.read_native_selected(pathlib.Path(paths["native_model"]),point)
 need(len(J)==len(set(J))==4354 and J==sorted(selected),"same complete original selected4354 source rows and order")
 need(unit["rhsColumns"]==36 and unit["originalRightHandSideRowsUnchanged"],"all paid36 unscaled forcing columns")
 rhs=[[int(x) for x in r] for r in unit["originalRightHandSideRows"]]
 need(len(rhs)==4354 and all(len(r)==36 for r in rhs),"all4354 by36 original forcing coefficients")
 # Never divide individual rows by the M0 unit-profile contents.
 support=pathlib.Path(support);sr=read(support/"koszul-exact-rational-support-receipt.json")
 need(sr["status"]=="completed" and sr["selectedStandardKoszulDimensionOverQ"]==29 and
 sr["all1834OutsideSourceCoefficientsZero"] and sr["allOriginal4367IntegerProductsZero"] and
 sr["completeKernelDimensionCertifiedOverQ"],"fully rebuilt29 actual source kernels")
 files={r["file"]:r for r in sr["parameters"]["temporaryFiles"]};sb=sr["parameters"]["binding"]
 modelpath=pathlib.Path(inv["preparedDirectory"])/"exact-original-koszul-outside-model.json.gz"
 model=read(modelpath)
 need(model["selectedRows"]==J,"rebuilt Koszul source model and current forcing use exactly the sameJ")
 outside=list(map(int,model["outsideRows"]));free=list(map(int,model["freeRows"]))
 need(outside==[r for r in range(1,6189) if r not in selected] and len(free)==36 and len(set(free))==36,
 "complete1834 source complement and36 original free coordinates")
 terms=H.original_row_terms(point);source_columns=[];free_columns=[];audits=[]
 for j in range(29):
  p=support/("exact-selected-koszul-kernel-%03d.json.gz"%j);z=files[p.name]
  need(identity(p)=={"bytes":z["bytes"],"sha256":z["sha256"]},"actual reconstructed certificate bytes")
  v=read(p);nums=list(map(int,v["original6188IntegerCoefficients"]))
  need(v["binding"]==sb and v["column"]==j and len(nums)==6188 and
  v["all1834OutsideSourceCoefficientsZero"] and v["all4367ExactIntegerProductsZero"],
  "complete actual source certificate")
  need(all(nums[r-1]==0 for r in outside),"every original outside-source coefficient is zero")
  product=H.exact_product(nums,terms,lambda:None)
  need(len(product)==4367 and not any(product),"fresh all4367 original integer products before pairing")
  need(vecsha(product)==v["fullOriginalProductSHA256"],"same full original product hash")
  source_columns.append([nums[r-1] for r in J]);free_columns.append([nums[r-1] for r in free])
  audits.append({"column":j,"certificate":z,"sourceSHA256":vecsha(nums),
   "fullOriginalProductSHA256":vecsha(product),"all1834OutsideSourceCoefficientsZero":True,
   "all4367FreshIntegerProductsZero":True})
  rec["parameters"]["verifiedSourceColumns"]=audits;ck()
 G=fmpz_mat(36,29,[free_columns[j][i] for i in range(36) for j in range(29)])
 grank=int(fmpq_mat(G).rank());need(grank==29,"all29 sources independent in the original36 free coordinates")
 rec.update(all1309ConstantCoefficientsExactlyMatched=True,sameSelectedSourceSupportVerified=True,
 all29FullOriginal4367ProductsZero=True,originalProductCoordinates=29*4367,
 completeFree36ImageRankOverQ=grank,originalForcingRowsUnscaled=True,
 sourceSpaceNotConfusedWithOutputCokernel=True)
 rec["phase"]="actual29-by36-pairing";ck()
 pp=out/"actual-koszul29-by36-original-forcing-pairing.json.gz"
 if pp.exists():
  p=read(pp);need(p["binding"]==bind and p["sourceAudits"]==audits and p["oldUnitIdentity"]==inv["inputIdentities"]["old_unit"],
  "same complete saved pairing")
  rows=[[int(x) for x in r] for r in p["integerRows"]]
  need(len(rows)==29 and all(len(r)==36 for r in rows),"complete saved pairing dimensions")
 else:
  KK=fmpz_mat(29,4354,[x for col in source_columns for x in col])
  FF=fmpz_mat(4354,36,[x for row in rhs for x in row])
  P=KK*FF
  rows=[[int(P[i,j]) for j in range(36)] for i in range(29)]
  save(pp,{"format":"isp-same-original-koszul29-second-forcing-pairing-v1","binding":bind,
   "sourceAudits":audits,"oldUnitIdentity":inv["inputIdentities"]["old_unit"],
   "rows":29,"columns":36,"columnOrder":"threeHF,thirty-threeT",
   "originalSourceRows":J,"integerRows":[[str(x) for x in row] for row in rows],
   "allSourcesVerifiedBeforePairing":True,"noOriginalRowRescalingApplied":True})
  del KK,FF,P
 output(pp);rec["phase"]="exact-small-rank-and-head-projection";ck()
 # Only invertible rational row/column scalings are used below.
 rd=[]
 for row in rows:
  g=0
  for x in row:g=math.gcd(g,abs(x))
  rd.append(g or 1)
 normalized=[[x//rd[i] for x in row] for i,row in enumerate(rows)]
 cd=[]
 for j in range(36):
  g=0
  for i in range(29):g=math.gcd(g,abs(normalized[i][j]))
  cd.append(g or 1)
 N=[[normalized[i][j]//cd[j] for j in range(36)] for i in range(29)]
 R,rho=fmpq_mat(N).rref();rho=int(rho);pv=pivots(R,rho)
 Hf=fmpq_mat([[row[j] for j in range(3)] for row in N]);h=int(Hf.rank())
 need(0<=h<=3 and h<=rho<=14,"paired first-complement and total ranks obey paid full-original bounds")
 lower=rho-h
 need(lower<=11,"pairing lower bound exceeds paid22 true heads: input/implementation mismatch")
 ff=[j for j in range(36) if j not in set(pv)];nullcolumns=[]
 from flint import fmpq
 for c in ff:
  w=[fmpq(0) for _ in range(36)];w[c]=fmpq(1)
  for i,piv in enumerate(pv):w[piv]=-R[i,c]
  # N = diag(1/rd) P diag(1/cd); original coordinates are w_j/cd_j.
  nullcolumns.append(qcolumn_primitive([w[j]/cd[j] for j in range(36)]))
 Pq=fmpq_mat(rows)
 Z=fmpq_mat(36,len(nullcolumns),[nullcolumns[j][i] for i in range(36) for j in range(len(nullcolumns))])
 need(all(not x for x in (Pq*Z).entries()),"complete original29 by36 pairing kernel products")
 C=fmpq_mat(33,len(nullcolumns),[nullcolumns[j][i+3] for i in range(33) for j in range(len(nullcolumns))])
 CR,cr=C.transpose().rref();cr=int(cr)
 need(cr==33-rho+h and cr>=22,"actual33-head projection dimension and paid22 lower inclusion")
 # Each nonzero row of rref(C^T) is a complete independent head column.
 head_columns=[qcolumn_primitive([CR[i,j] for j in range(33)]) for i in range(cr)]
 sp=out/"complete-koszul29-pairing-nullspace-and-head-projection.json.gz"
 save(sp,{"binding":bind,"pairingIdentity":identity(pp),"pairingRankOverQ":rho,
  "firstThreeHFPairingRankOverQ":h,"secondConnectionRankLowerBoundFromPairing":lower,
  "originalPairingNullspaceIntegerColumns":[[str(x) for x in v] for v in nullcolumns],
  "complete33HeadProjectionIntegerColumns":[[str(x) for x in v] for v in head_columns],
  "originalPairingKernelProductsVerified":True,"headProjectionDimension":cr,
  "rowScalingGCDs":[str(x) for x in rd],"columnScalingGCDs":[str(x) for x in cd],
  "normalizedPairingRREF":[[str(R[i,j]) for j in range(36)] for i in range(rho)],
  "normalizedPairingPivotColumns":pv,"pairedSystemOnlyNotAllOriginalSourceKernel":True})
 output(sp)
 lo=max(9,lower)
 outcome="complete-selected-second-rank-eleven" if lo==11 else (
 "selected-second-lower-bound-ten" if lo==10 else "paired-subspace-insufficient-to-close-second")
 rec.update(status="completed",phase="complete",outcome=outcome,pairingRankOverQ=rho,
 firstThreeHFPairingRankOverQ=h,secondConnectionRankLowerBoundFromPairing=lower,
 selectedSecondConnectionRankOverQLowerBound=lo,selectedSecondConnectionRankOverQUpperBound=11,
 selectedSecondConnectionRankExactly11=lo==11,completeSelectedSecondHeadSpaceProved=lo==11,
 completePaired33HeadProjectionDimension=cr,pairedConstraintKernelDimension=36-rho,
 completeOriginalPairingKernelProductsVerified=True,
 sourceKernelDimensionUsed=29,all36SourceKernelDirectionsUsed=False,
 newFullM0RightHandSidesSolved=0,normalFiveEliminationContinued=False,
 exactSourceReconstructionNotNewKernelDiscovery=True,leadingUnitProved=False)
 rec["parameters"].update(sourceBinding=sb,pairingIdentity=identity(pp),
 completeHeadProjectionIdentity=identity(sp),pairingPivotColumns=pv,
 firstThreeColumnMeaning="HF; all3 old first-head complement directions retained",
 remainingColumnMeaning="T; all33 first-lift heads retained",
 boundFormula="beta2 >= rank(K29^T[HF,T])-rank(K29^T HF)",
 paidUpperBoundSource="22 complete original second left jets",
 rankOverQNotDeducedFromMod31Pairing=True)
 ck();print(json.dumps({"status":"completed","outcome":outcome,"pairingRankOverQ":rho,
 "firstThreeHFPairingRankOverQ":h,"completePaired33HeadProjectionDimension":cr,
 "selectedSecondConnectionRankOverQLowerBound":lo,"selectedSecondConnectionRankOverQUpperBound":11}),flush=True)
 return 0
def main(argv):
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ["helper","preparation","support-solver","native-model","point-model","selected-receipt","regauged-out","rebuild-root","out"]:
  ap.add_argument("--"+k,required=True,type=pathlib.Path)
 ap.add_argument("--seconds",type=float,default=180);ap.add_argument("--memory-mib",type=int,default=2048)
 a=ap.parse_args(argv)
 need(math.isfinite(a.seconds) and 0<a.seconds<=600,"shared finite budget at most600 seconds")
 need(0<a.memory_mib<=2048,"at most2048MiB per process")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 start=time.monotonic();deadline=start+a.seconds-min(5,a.seconds/10)
 out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 rec={"format":"isp-same-original-koszul29-second-forcing-pairing-pipeline-v1","status":"running",
 "phase":"inputs","parameters":{},"events":[],"largeDataUploadedOrCommitted":False,
 "oldNormalFormsRecomputed":False,"normalFiveEliminationContinued":False,"newM0RightHandSidesSolved":0,
 "all29FullOriginal4367ProductsZero":False,"completeSelectedSecondHeadSpaceProved":False,
 "leadingUnitProved":False}
 code=1
 def checkpoint():
  rec["mathematicalElapsedSeconds"]=time.monotonic()-start
  save(out/"same-source-koszul29-second-pairing-receipt.json",rec)
 def check():
  if time.monotonic()>=deadline:raise BudgetExpired("actual shared mathematical deadline")
 def run(name,cmd,rp):
  check();log=out/(name+".log");st=time.monotonic();remain=max(.001,deadline-time.monotonic())
  with log.open("w") as f:
   pr=subprocess.Popen(cmd,stdout=f,stderr=subprocess.STDOUT,start_new_session=True)
   try:pr.wait(timeout=remain)
   except subprocess.TimeoutExpired:
    os.killpg(pr.pid,signal.SIGTERM)
    try:pr.wait(timeout=2)
    except subprocess.TimeoutExpired:os.killpg(pr.pid,signal.SIGKILL);pr.wait()
    rec["events"].append({"stage":name,"exitCode":pr.returncode,"elapsedSeconds":time.monotonic()-st,"sharedDeadlineReached":True})
    if rp.exists():rec["parameters"][name+"ActualStatus"]=read(rp).get("status")
    raise BudgetExpired(name+": shared deadline; all complete child stages retained")
  rec["events"].append({"stage":name,"exitCode":pr.returncode,"elapsedSeconds":time.monotonic()-st})
  if rp.exists():
   rr=read(rp);rec["parameters"][name+"ActualStatus"]=rr.get("status")
  else:rr={}
  checkpoint()
  if pr.returncode==75:raise BudgetExpired(name+": child actual bounded prefix retained")
  need(pr.returncode==0 and rr.get("status")=="completed",name+": completed actual receipt required; see temporary log")
  return rr
 try:
  paths={k:getattr(a,k) for k in ["helper","preparation","support_solver","native_model","point_model","selected_receipt"]}
  paths.update(old_unit=a.regauged_out/"prepared"/"second-left-m0-unit-input.json.gz",
   old_full=a.regauged_out/"full-products"/"full-second-left-products-receipt.json",
   coefficients=a.rebuild_root/"rebuilt-first"/"same-original-natural-constant-and-first-coefficients.json.gz")
  # The exact actual receipt name is pinned; locate it by its committed bytes if needed.
  if not paths["old_full"].exists():
   candidates=[p for p in (a.regauged_out/"full-products").glob("*.json") if p.stat().st_size==PINS["old_full"][0]]
   candidates=[p for p in candidates if identity(p)["sha256"]==PINS["old_full"][1]]
   need(len(candidates)==1,"unique actual paid full-product receipt by bytes/SHA")
   paths["old_full"]=candidates[0]
  ids={}
  for k,p in paths.items():
   ids[k]=identity(p)
   if k in PINS:need(ids[k]=={"bytes":PINS[k][0],"sha256":PINS[k][1]},"exact paid input: "+k)
   else:need(k=="selected_receipt" and ids[k]["sha256"]==SELECTED_SHA,"same selected source/free dictionary")
  material={"scriptIdentity":identity(__file__),"inputIdentities":ids,"chart":"same natural infinity u=1/s",
   "normalVariables":list(range(9)),"pureVariables":[9,10],"forcingOrder":"HF3,T33"}
  bind=hashlib.sha256(json.dumps(material,sort_keys=True,separators=(",",":")).encode()).hexdigest()
  prep=out/"reconstructed-source-model";support=out/"reconstructed-source29";pair=out/"pairing"
  inv={**material,"binding":bind,"paths":{k:str(p.resolve()) for k,p in paths.items()},
   "preparedDirectory":str(prep),"supportDirectory":str(support)}
  ip=out/"invocation.json"
  if ip.exists():need(read(ip)["binding"]==bind,"same actual sources and code on continuation")
  save(ip,inv)
  rec["parameters"].update(binding=bind,inputIdentities=ids,programIdentity=material["scriptIdentity"],
   secondsLimit=a.seconds,memoryMiBPerProcess=a.memory_mib,
   reconstructLostOld29TemporaryData=True,oldPaidKernelCount=29,
   phaseDirectories={"sourceModel":prep.name,"exactSource29":support.name,"pairing":pair.name})
  rec["phase"]="reconstruct-paid-source-model";checkpoint()
  prp=prep/"koszul-exact-sparse-preparation-receipt.json"
  if prp.exists() and read(prp).get("status")=="completed":
   rec["events"].append({"stage":"source-model","completeActualCacheReused":True})
  else:
   check();remaining=min(60,max(.01,deadline-time.monotonic()))
   run("source-model",[sys.executable,"-B",str(a.preparation),"--helper",str(a.helper),
    "--native-model",str(a.native_model),"--point-model",str(a.point_model),"--selected-receipt",str(a.selected_receipt),
    "--out",str(prep),"--seconds",str(remaining),"--memory-mib",str(a.memory_mib)],prp)
  rec["phase"]="reconstruct-paid29-exact-sources";checkpoint()
  srp=support/"koszul-exact-rational-support-receipt.json"
  if srp.exists() and read(srp).get("status")=="completed":
   rec["events"].append({"stage":"source29","completeActualCacheReused":True})
  else:
   check();remaining=max(.01,deadline-time.monotonic())
   run("source29",[sys.executable,"-B",str(a.support_solver),"--helper",str(a.helper),
    "--point-model",str(a.point_model),"--prepared-dir",str(prep),"--out",str(support),
    "--seconds",str(remaining),"--memory-mib",str(a.memory_mib),"--resume"],srp)
  rec["phase"]="pair-full-original-sources";checkpoint()
  rp=pair/"same-source-koszul29-pairing-worker-receipt.json"
  if rp.exists() and read(rp).get("status")=="completed":
   rr=read(rp);need(rr["binding"]==bind,"same completed pairing binding")
   for z in rr["outputs"]:need(identity(pair/z["file"])=={"bytes":z["bytes"],"sha256":z["sha256"]},"complete saved pairing output")
   rec["events"].append({"stage":"pairing","completeActualCacheReused":True})
  else:rr=run("pairing",[sys.executable,"-B",str(pathlib.Path(__file__).resolve()),"--pairing-worker",str(ip),str(support),str(pair)],rp)
  need(rr["binding"]==bind and rr["all29FullOriginal4367ProductsZero"],"full same-original products before final conclusion")
  fields=["outcome","pairingRankOverQ","firstThreeHFPairingRankOverQ","secondConnectionRankLowerBoundFromPairing",
   "selectedSecondConnectionRankOverQLowerBound","selectedSecondConnectionRankOverQUpperBound",
   "selectedSecondConnectionRankExactly11","completeSelectedSecondHeadSpaceProved",
   "completePaired33HeadProjectionDimension","pairedConstraintKernelDimension",
   "completeOriginalPairingKernelProductsVerified","all1309ConstantCoefficientsExactlyMatched",
   "sameSelectedSourceSupportVerified","all29FullOriginal4367ProductsZero","originalProductCoordinates",
   "completeFree36ImageRankOverQ","originalForcingRowsUnscaled","sourceSpaceNotConfusedWithOutputCokernel",
   "sourceKernelDimensionUsed","all36SourceKernelDirectionsUsed","newFullM0RightHandSidesSolved"]
  for k in fields:rec[k]=rr[k]
  rec.update(status="completed",phase="complete")
  rec["parameters"].update(pairingReceiptIdentity=identity(rp),pairingSummary=rr["parameters"],
   actualTemporaryOutputs=rr["outputs"])
  code=0
 except (BudgetExpired,subprocess.TimeoutExpired) as e:
  rec.update(status="completed-prefix",error=str(e),completeSelectedSecondHeadSpaceProved=False);code=75
 except Exception as e:
  rec.update(status="failed",error=str(e),exceptionType=type(e).__name__)
  (out/"exception.log").write_text(traceback.format_exc());code=1
 finally:checkpoint()
 print(json.dumps(rec),flush=True);return code
if __name__=="__main__":
 if len(sys.argv)>1 and sys.argv[1]=="--pairing-worker":
  sys.exit(pairing_worker(pathlib.Path(sys.argv[2]),pathlib.Path(sys.argv[3]),pathlib.Path(sys.argv[4])))
 sys.exit(main(sys.argv[1:]))
