#!/usr/bin/env python3
"""Only the21 new exact M0 unit RHS after the actual high-zero gate.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
The complete4354 products and lower-page compensation belong to the next
consumer. Reuse paid36/130 sources; do not rebuild or solve those RHS.
"""
import argparse,gzip,hashlib,json,math,os,pathlib,resource,signal,subprocess,sys,time,traceback
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
 b=json.dumps(v,sort_keys=True,separators=(",",":")).encode();need(len(b)<100000,"small summary only")
 q.write_bytes(b);os.replace(q,p)
PREP_PROGRAM={"bytes":14109,"sha256":"a6bb496eeff96c9a7ca69583f372190e2974e89335b677ea29b5e89c74a2df48"}
WORKER={"bytes":16412,"sha256":"c9e1eee6142d29daf661682e177702825e90aef7222611baa2adadaffe0dc731"}
OLD_UNIT={"bytes":9008513,"sha256":"c53406d65cfd66f2f3b6f1c946bd7495e44c7041538c4f3c85518eb7be7d5dfe"}
def main():
 a=argparse.ArgumentParser(description=__doc__)
 for k in ["prepared-out","regauged-out","unit-worker","out"]:a.add_argument("--"+k,required=True,type=pathlib.Path)
 a.add_argument("--seconds",type=float,default=300);a.add_argument("--memory-mib",type=int,default=4096)
 q=a.parse_args();need(math.isfinite(q.seconds) and 0<q.seconds<=600,"finite shared unit budget at most600")
 need(0<q.memory_mib<=8192,"at most8192MiB per process")
 resource.setrlimit(resource.RLIMIT_AS,(q.memory_mib*1024**2,)*2)
 start=time.monotonic();deadline=start+q.seconds;out=q.out.resolve();out.mkdir(parents=True,exist_ok=True)
 cp=out/"third21-unit-pipeline-receipt.json"
 rec={"status":"running","phase":"paid-preparation","events":[],"parameters":{},
 "old36ExactUnitSolutionsRecomputed":False,"old130ExactUnitSolutionsRecomputed":False,
 "full4354OriginalThirdProductsVerified":False,"explicitNewLambda3SourcesConstructed":False,
 "newRightHandSides":21,"largeDataUploadedOrCommitted":False}
 code=1
 def ck():
  rec["mathematicalElapsedSeconds"]=time.monotonic()-start;save(cp,rec)
 try:
  rp=q.prepared_out/"third21-original-forcing-support-and-unit-preparation-receipt.json"
  ip=q.prepared_out/"third21-left-m0-unit-input.json.gz"
  fp=q.prepared_out/"complete-third21-original-right-hand-sides.json.gz"
  oldp=q.regauged_out/"prepared"/"second-left-m0-unit-input.json.gz"
  pr=read(rp);inv=read(q.prepared_out/"invocation.json")
  need(pr["status"]=="completed" and pr["outcome"]=="all21-high-rows-zero-old-unit-input-prepared" and
   pr["all21ForcingsVanishOnOld1736ZeroRows"] and pr["newUnitRightHandSidesPrepared"]==21 and
   pr["parameters"]["programIdentity"]==inv["programIdentity"]==PREP_PROGRAM,
   "actual completed high-zero gate under exact frozen preparation")
  need(pr["parameters"]["binding"]==inv["binding"] and
   inv["inputIdentities"]["unit"]==OLD_UNIT and ident(oldp)==OLD_UNIT,
   "same complete paid old M0")
  outputs={z["file"]:z for z in pr["outputs"]}
  for p in [ip,fp]:
   z=outputs[p.name];need(ident(p)=={"bytes":z["bytes"],"sha256":z["sha256"]},"actual prepared "+p.name)
  need(ident(q.unit_worker)==WORKER,"exact paid rational RHS unit worker")
  u=read(ip);old=read(oldp);f=read(fp)
  need(u["binding"]==f["binding"]==inv["binding"] and u["rhsColumns"]==21 and
   u["previousUnitInputIdentity"]==OLD_UNIT and u["forcingIdentity"]==ident(fp),
   "all21 actual prepared RHS")
  for k in ["originalSourceRows","originalCorrectionRows","rowCoefficientContents","selectedUnitRowIndices",
   "unitPrime","unitDeterminantModulo31","secondCorrectionOutputCoordinates"]:
   need(u[k]==old[k],"unchanged original unit field "+k)
  cols=[[int(x) for x in c] for c in f["primitiveIntegerRightHandSideColumns"]]
  need(len(cols)==21 and all(len(c)==4354 for c in cols),"complete21 by4354 original RHS")
  need(all([int(x) for x in u["originalRightHandSideRows"][i]]==[cols[j][i] for j in range(21)]
   for i in range(4354)),"exact original RHS including every unused row")
  mat={"programIdentity":ident(__file__),"workerIdentity":WORKER,"unitInputIdentity":ident(ip),
   "preparedReceiptIdentity":ident(rp),"preparedProgramIdentity":PREP_PROGRAM,"oldUnitIdentity":OLD_UNIT}
  bind=hashlib.sha256(json.dumps(mat,sort_keys=True,separators=(",",":")).encode()).hexdigest()
  rec["parameters"].update(mat);rec["parameters"].update(binding=bind,sourceBinding=u["binding"],
   secondsLimit=q.seconds,memoryMiBPerProcess=q.memory_mib,
   rowScalingFormula="U_i=M0_i/g_i, R_i=-rhs_i/g_i in Q; no divisibility of rhs by g_i required",
   all4354PreparedRightHandSideRowsReverified=True)
  ck()
  urp=out/"m0-unit-solve-receipt.json";sp=out/"complete-m0-unit-solution.json.gz"
  ur=read(urp) if urp.exists() else None
  if ur and ur.get("status")=="completed":
   need(ur["binding"]==u["binding"] and ur["inputIdentity"]==ident(ip) and
    ur["workerSHA256"]==WORKER["sha256"] and ur["candidateIdentity"]==ident(sp) and
    ur["all1546OriginalUnitRowsVerified"] and ur["verifiedColumnCount"]==21 and
    ur["originalUnitProductCoordinates"]==1546*21,"same complete actual unit21 source cache")
   rec["events"].append({"stage":"unit21","completeCandidateAndProductsReused":True})
  else:
   rec["phase"]="actual-new21-unit-solve";ck();remaining=deadline-time.monotonic()
   if remaining<=5:raise BudgetExpired("no shared unit time remains")
   grace=min(20,max(1,remaining/10));t=time.monotonic()
   with (out/"unit21.log").open("a",encoding="utf-8") as log:
    proc=subprocess.Popen([sys.executable,"-B",str(q.unit_worker.resolve()),"--input",str(ip.resolve()),"--out",str(out)],
     stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
    try:proc.wait(timeout=max(.1,remaining-grace))
    except subprocess.TimeoutExpired:
     os.killpg(proc.pid,signal.SIGTERM)
     try:proc.wait(timeout=grace)
     except subprocess.TimeoutExpired:os.killpg(proc.pid,signal.SIGKILL);proc.wait()
     rec["events"].append({"stage":"unit21","elapsedSeconds":time.monotonic()-t,"exitCode":proc.returncode,
      "sharedDeadlineReached":True})
     raise BudgetExpired("exact returned candidate and actual completed columns retained")
   rec["events"].append({"stage":"unit21","elapsedSeconds":time.monotonic()-t,"exitCode":proc.returncode})
   if proc.returncode==75:raise BudgetExpired("unit worker stopped at actual safe checkpoint")
   need(proc.returncode==0 and urp.exists(),"actual unit worker failed; inspect unit21.log")
   ur=read(urp)
  need(ur["status"]=="completed" and ur["binding"]==u["binding"] and ur["inputIdentity"]==ident(ip) and
   ur["workerSHA256"]==WORKER["sha256"] and ur["candidateIdentity"]==ident(sp) and
   ur["all1546OriginalUnitRowsVerified"] and ur["verifiedColumnCount"]==21 and
   ur["originalUnitProductCoordinates"]==32466,"all21 exact solutions and original undivided unit products")
  rec.update(status="completed",phase="complete",outcome="all21-exact-unit-solutions-original-products-complete",
   all21CompleteUnitSolutionsSaved=True,all32466OriginalUnitProductsZero=True,
   full4354OriginalThirdProductsStillRequired=True)
  rec["parameters"].update(completeUnitSolution=ident(sp),completeUnitReceipt=ident(urp),
   completeSolutionSavedBeforeProductVerification=ur["completeSolutionSavedBeforeProductVerification"],
   actualWorkerParameters=ur.get("parameters",{}));code=0
 except BudgetExpired as e:
  rec.update(status="completed-prefix",error=str(e));code=75
 except Exception as e:
  rec.update(status="failed",error=str(e),exceptionType=type(e).__name__)
  (out/"exception.log").write_text(traceback.format_exc(),encoding="utf-8");code=1
 finally:
  urp=out/"m0-unit-solve-receipt.json"
  if urp.exists():
   ur=read(urp);rec["parameters"]["lastActualUnitCheckpoint"]={k:v for k,v in ur.items() if k not in ["parameters","paths"]}
  ck()
 print(json.dumps(rec),flush=True);return code
if __name__=="__main__":sys.exit(main())
