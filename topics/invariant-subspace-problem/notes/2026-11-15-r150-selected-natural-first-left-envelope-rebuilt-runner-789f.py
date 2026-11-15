#!/usr/bin/env python3
"""Use the new same-I,J temporary reconstruction for the exact Q first envelope.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
The old rational585 left kernel was lost with the old session, so its submitted
small engine is rerun once; all later exact stages keep genuine temporary cache.
"""
import argparse,contextlib,hashlib,importlib.util,json,math,os,pathlib,resource,signal,subprocess,sys,time,traceback
sys.dont_write_bytecode=True
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
for k in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):os.environ[k]="1"
POINT=(87459,"97d31570a0bd99d33066fc6ea47984203b2964521ceeb50920f0a49dd3bb8074")
PROJECTED_SHA="d94b1f0be704c5eb7aee756a98a5d7a2097e66a331709c4e300434f78dbd7e9d"
ENVELOPE=(20823,"4901fa8fcebbda69a9c6042cdf20f622083c8e75285b19051bba47f435dc2ac9")
REBUILD=(19311,"bb4a217827ff7a8ac8faf9c0f1b2c5255e302c3bcc66f644cd31a8f8f50312c6")
class BudgetExpired(Exception):pass
def need(v,s):
 if not v:raise ValueError(s)
def ident(p):
 h=hashlib.sha256();n=0
 with pathlib.Path(p).open("rb") as f:
  while True:
   b=f.read(1048576)
   if not b:break
   n+=len(b);h.update(b)
 return {"bytes":n,"sha256":h.hexdigest()}
def read(p):return json.loads(pathlib.Path(p).read_text(encoding="utf-8"))
def save(p,o):
 p=pathlib.Path(p);q=p.with_name(p.name+".tmp");q.write_text(json.dumps(o,separators=(",",":"),ensure_ascii=False)+"\n",encoding="utf-8");os.replace(q,p)
def imported(name,p):
 sp=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
def worker(argv):
 ap=argparse.ArgumentParser()
 for key in ["engine","point-model","selected-model","unit-profile","out"]:ap.add_argument("--"+key,type=pathlib.Path,required=True)
 ap.add_argument("--seconds",type=float,required=True);ap.add_argument("--memory-mib",type=int,required=True)
 a=ap.parse_args(argv);need(ident(a.engine)["sha256"]==PROJECTED_SHA,"unchanged original rational585 engine")
 M=imported("original_exact585_rebuild",a.engine)
 M.MODEL_ID=ident(a.selected_model);M.PROFILE_ID=ident(a.unit_profile)
 return M.main(["--point-model",str(a.point_model),"--selected-model",str(a.selected_model),"--unit-profile",str(a.unit_profile),
  "--out",str(a.out),"--seconds",str(a.seconds),"--memory-mib",str(a.memory_mib)])
def main(argv):
 ap=argparse.ArgumentParser(description=__doc__)
 for key in ["rebuild-root","point-model","projected-engine","envelope-engine","out"]:ap.add_argument("--"+key,type=pathlib.Path,required=True)
 ap.add_argument("--seconds",type=float,default=60);ap.add_argument("--memory-mib",type=int,default=1024)
 a=ap.parse_args(argv);need(math.isfinite(a.seconds) and 0<a.seconds<=180 and 0<a.memory_mib<=2048,"single bounded rebuilt exact first envelope")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 start=time.monotonic();out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 rec={"format":"isp-rebuilt-same-IJ-natural-first-left-envelope-pipeline-v1","status":"running","phase":"verified-reconstruction",
  "oldLargeEliminationRecomputed":False,"newDixonDigitsComputed":0,"newPrimeComputed":False,
  "lostRational585CacheReconstructionRequired":True,
  "largeDataUploadedOrCommitted":False,"leadingUnitProved":False,"parameters":{},"events":[]}
 code=1;core=None;corestart=None
 def left():
  t=a.seconds-(time.monotonic()-start)
  if t<=1:raise BudgetExpired("actual shared Q-envelope clock; all complete temporary stages retained")
  return t
 def checkpoint():
  rec["mathematicalElapsedSeconds"]=time.monotonic()-start;save(out/"selected-natural-first-left-envelope-rebuilt-pipeline-receipt.json",rec)
 try:
  need(ident(a.point_model)=={"bytes":POINT[0],"sha256":POINT[1]} and ident(a.projected_engine)["sha256"]==PROJECTED_SHA and
   ident(a.envelope_engine)=={"bytes":ENVELOPE[0],"sha256":ENVELOPE[1]},"all actual unchanged exact source/point identities")
  rrp=a.rebuild_root/"selected-natural-u-minimal-rebuild-receipt.json";rr=read(rrp);rp=rr["parameters"]
  need(rr["status"]=="completed" and rr["all51PaidPrefixFilesCoefficientIdentitiesVerified"] and rr["allSeventeenPaidSmallSchurCoefficientsVerified"],"completed same-original reconstruction and full paid16 prefix")
  need(rp["wrapperIdentity"]=={"bytes":REBUILD[0],"sha256":REBUILD[1]} and rr["originalMathematicalEngineBytesUnchanged"] and rr["newInputBindingExplicit"],"known verified reconstruction recipe")
  rootinputs=a.rebuild_root/"rebuilt-inputs";firstdir=a.rebuild_root/"rebuilt-first"
  selected=rootinputs/"same-selected-original-source-indices.json";profile=rootinputs/"same-selected-original-output-indices.json"
  for key,p in [("selected_model",selected),("unit_profile",profile)]:need(ident(p)==rp["rebuiltInputs"][key],"all original rebuilt I,J dictionary bytes")
  fc=read(a.rebuild_root/"rebuilt-first-stage-cache.json")
  for name,v in fc["outputs"].items():need(ident(firstdir/name)==v,"complete first-cache bytes "+name)
  fr=read(firstdir/"selected-natural-first-connection-f31-receipt.json")
  need(fr["status"]=="completed" and fc["newFirstBinding"]==fr["parameters"]["binding"]==rp["rebuiltFirstBinding"] and
   fr["selectedNaturalFirstConnectionRankModulo31"]==3,"same actual rebuilt original first cache")
  inputids={"reconstructionReceipt":ident(rrp),"selectedModel":ident(selected),"unitProfile":ident(profile),
   "pointModel":ident(a.point_model),"projectedEngine":ident(a.projected_engine),"envelopeEngine":ident(a.envelope_engine),"wrapper":ident(__file__)}
  bind=hashlib.sha256(json.dumps(inputids,sort_keys=True,separators=(",",":")).encode()).hexdigest()
  rec["parameters"].update(binding=bind,inputIdentities=inputids,secondsLimit=a.seconds,memoryMiB=a.memory_mib,
   reconstructionRootIsTemporary=True,originalIAndJVerifiedByAll51PrefixIdentities=True)
  proj=out/"rebuilt-rational585";cache=out/"rational585-completed-cache.json"
  expected={"point":ident(a.point_model),"selected":ident(selected),"profile":ident(profile),"engine":ident(a.projected_engine)}
  checkpoint();left()
  if cache.exists():
   cc=read(cache);need(cc["inputIdentities"]==expected,"same exact rational585 reconstruction cache")
   for name,v in cc["outputs"].items():need(ident(proj/name)==v,"all reconstructed585 completed arrays")
   rec["events"].append({"reusedCompleteRebuiltRational585":True})
  else:
   rec["phase"]="rebuild-lost-rational585-cokernel";checkpoint();remain=left();limit=min(30,remain-1)
   cmd=[sys.executable,"-B",str(pathlib.Path(__file__).resolve()),"--rebuild-worker","--engine",str(a.projected_engine),
    "--point-model",str(a.point_model),"--selected-model",str(selected),"--unit-profile",str(profile),
    "--out",str(proj),"--seconds",str(limit),"--memory-mib",str(a.memory_mib)]
   ws=time.monotonic()
   with (out/"rational585-rebuild.log").open("a",encoding="utf-8") as log:
    p=subprocess.Popen(cmd,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
    try:p.wait(timeout=limit+.25)
    except subprocess.TimeoutExpired:
     os.killpg(p.pid,signal.SIGKILL);p.wait()
     rec["events"].append({"rational585WorkerStoppedAtActualDeadline":True,"exitCode":p.returncode,"elapsedSeconds":time.monotonic()-ws})
     raise BudgetExpired("lost rational585 reconstruction did not finish; completed input/nullspace candidate retained")
   rec["events"].append({"rational585WorkerExitCode":p.returncode,"elapsedSeconds":time.monotonic()-ws})
   if p.returncode==75:raise BudgetExpired("rational585 completed stage clock; temporary originals retained")
   need(p.returncode==0,"actual rational585 reconstruction failure; see its receipt/log")
   pr=read(proj/"selected-second-transverse-projection-receipt.json")
   need(pr["status"]=="completed" and pr["exactProjectedRankOverQ"]==556 and pr["completeIndependentLeftKernelDimension"]==29 and
    pr["allOriginalProjectedSourceRowsVerified"] and pr["allLeftKernelFreeCoordinatesIdentity"],"all original exact585 reconstruction checks")
   cc={"inputIdentities":expected,"reconstructedProjectionBinding":pr["parameters"]["binding"],
    "outputs":{x["file"]:{"bytes":x["bytes"],"sha256":x["sha256"]} for x in pr["parameters"]["temporaryFiles"]}}
   cc["outputs"]["selected-second-transverse-projection-receipt.json"]=ident(proj/"selected-second-transverse-projection-receipt.json")
   save(cache,cc)
  pr=read(proj/"selected-second-transverse-projection-receipt.json")
  paths={"selected_model":selected,"unit_profile":profile,
   "coefficients":firstdir/"same-original-natural-constant-and-first-coefficients.json.gz",
   "first_receipt":firstdir/"selected-natural-first-connection-f31-receipt.json",
   "projected_input":proj/"same-original-second-transverse-integer-input.json.gz",
   "left_kernel":proj/"second-transverse-complete-left-nullspace.json.gz"}
  E=imported("frozen_small_Q_left_envelope",a.envelope_engine);E.PIN={k:(ident(p)["bytes"],ident(p)["sha256"]) for k,p in paths.items()}
  E.FIRST_BINDING=fr["parameters"]["binding"];E.PROJECTED_BINDING=pr["parameters"]["binding"]
  rec["phase"]="actual-natural-first-left-envelope";checkpoint();remain=left();corestart=time.monotonic()
  coredir=out/"left-envelope"
  with (out/"left-envelope-pipeline.log").open("a",encoding="utf-8") as log:
   with contextlib.redirect_stdout(log):ec=E.main(["--selected-model",str(selected),"--unit-profile",str(profile),
    "--first-dir",str(firstdir),"--projected-dir",str(proj),"--out",str(coredir),"--seconds",str(remain),"--memory-mib",str(a.memory_mib)])
  core=read(coredir/"selected-natural-first-left-envelope-receipt.json")
  rec["parameters"].update(actualEnvelopeReceipt=ident(coredir/"selected-natural-first-left-envelope-receipt.json"),
   actualEnvelopeBinding=core["parameters"]["binding"],actualEnvelopeStatistics={k:v for k,v in core.items() if k not in ["events","parameters"]},
   actualEnvelopeParameters=core["parameters"],actualRational585RebuildReceipt=ident(proj/"selected-second-transverse-projection-receipt.json"))
  if ec==75:raise BudgetExpired("exact new envelope incomplete; original sparse system/whole completed RREF or jets are retained")
  need(ec==0 and core["status"]=="completed" and core["all4354OriginalFirstLeftJetProductsZero"] and
   core["all4354OriginalConstantLeftProductsZero"] and core["allHeadProjectionFreeCoordinatesIndependent"],"actual full original exact left-jet checks")
  for k in ["leftHeadImageDimension","constantCorrectionRank","envelopeObstructionRank","all4354OriginalFirstLeftJetProductsZero",
   "all4354OriginalConstantLeftProductsZero","allSelectedOutputSupportVerified","allHeadProjectionFreeCoordinatesIndependent",
   "completeFixedSupportEnvelopeComputed","selectedFirstConnectionRankOverQLowerBound","selectedFirstConnectionRankOverQUpperBound",
   "selectedFirstConnectionRankExactly3","fullOriginalFirstJetProductCoordinates","higherTransverseLeftCorrectionsRuledOut"]:rec[k]=core[k]
  rec.update(status="completed",phase="complete",outcome="same-selected-first-rank-three-proved" if core["selectedFirstConnectionRankExactly3"] else "restricted-left-support-upper-bound-only")
  code=0
 except BudgetExpired as e:rec.update(status="checkpointed-time-budget",outcome="checkpointed-time-budget",error=str(e));code=75
 except Exception as e:
  rec.update(status="failed-or-incomplete",outcome="failed-or-incomplete",error=str(e),exceptionType=type(e).__name__);(out/"exception.log").write_text(traceback.format_exc());code=1
 finally:
  rec["parameters"]["temporaryCheckpointLocations"]={"rational585":"rebuilt-rational585","rational585Cache":"rational585-completed-cache.json","originalEnvelopeAndExactRREF":"left-envelope"}
  checkpoint()
 need((out/"selected-natural-first-left-envelope-rebuilt-pipeline-receipt.json").stat().st_size<100000,"small permanent exact envelope receipt")
 print(json.dumps(rec),flush=True);return code
if __name__=="__main__":
 if len(sys.argv)>1 and sys.argv[1]=="--rebuild-worker":sys.exit(worker(sys.argv[2:]))
 sys.exit(main(sys.argv[1:]))
