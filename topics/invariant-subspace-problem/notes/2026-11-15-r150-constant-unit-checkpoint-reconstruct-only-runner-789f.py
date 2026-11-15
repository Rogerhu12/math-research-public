#!/usr/bin/env python3
"""One actual reconstruction at the last complete original unit checkpoint.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
No new Dixon digit or inverse. All large files remain temporary in this job.
"""
import argparse,hashlib,json,math,os,pathlib,resource,shutil,struct,subprocess,sys,time,traceback
sys.dont_write_bytecode=True
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
for n in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):os.environ[n]="1"
BINDING="2cd043a0fa006deb45f0811412adcd021fb1c0bee395215b812b3d8ad1c5a2af"
NATIVE_NAME="2026-11-15-r150-constant-unit-multiple-rhs-dixon-checkpoint-789f.cpp"
NATIVE_PIN=(19136,"d592f2086e81be2206adb67c7553de15ce36d49a9d1e62721a47a469d8afece2")
ADAPTER_PIN=(6460,"8d32e180db2113fe4bbaa4963cbc0e4a10635e80c32d09c2d93d94c1fbeabe09")
INPUT_PIN=(9919512,"02a794f50fcc91e018ec93c941d5974619219edc6bd1225df292907950e33f49")
def need(x,s):
 if not x:raise ValueError(s)
def identity(p):
 h=hashlib.sha256();n=0
 with pathlib.Path(p).open("rb") as f:
  while True:
   b=f.read(1048576)
   if not b:break
   h.update(b);n+=len(b)
 return {"bytes":n,"sha256":h.hexdigest()}
def read(p):return json.loads(pathlib.Path(p).read_text())
def canonical(x):return json.dumps(x,sort_keys=True,separators=(",",":")).encode()
def save(p,x):
 p=pathlib.Path(p);tmp=p.with_name(p.name+".tmp")
 tmp.write_text(json.dumps(x,separators=(",",":"))+"\n",encoding="utf-8");os.replace(tmp,p)
 return {"file":p.name,**identity(p),"temporaryOnly":True}
def manifest(p):
 z=pathlib.Path(p).read_text().split()
 need(len(z)==7 and z[0]=="R150CUMMETA1" and z[1]==BINDING,"whole original active meta protocol")
 m={"slot":int(z[2]),"digits":int(z[3]),"prime":int(z[4]),"bytes":int(z[5]),"sha256":z[6]}
 need(m["slot"] in (0,1) and m["digits"]>0 and len(m["sha256"])==64,"complete original cursor")
 return m
def child(cmd,log,seconds,memory,grace=10):
 def limit():resource.setrlimit(resource.RLIMIT_AS,(memory*1024**2,)*2)
 start=time.monotonic();timeout=False
 with pathlib.Path(log).open("wb") as f:
  p=subprocess.Popen(cmd,stdout=f,stderr=subprocess.STDOUT,preexec_fn=limit)
  try:code=p.wait(timeout=seconds)
  except subprocess.TimeoutExpired:
   timeout=True;p.terminate()
   try:code=p.wait(timeout=grace)
   except subprocess.TimeoutExpired:p.kill();code=p.wait()
 return {"exitCode":code,"wallSeconds":time.monotonic()-start,"outerDeadlineReached":timeout,"log":pathlib.Path(log).name}
def main(argv=None):
 ap=argparse.ArgumentParser(description=__doc__)
 for n in ("pipeline-out","native-source","adapter-source","out"):ap.add_argument("--"+n,type=pathlib.Path,required=True)
 ap.add_argument("--seconds",type=float,default=180)
 ap.add_argument("--memory-mib",type=int,default=4096)
 ap.add_argument("--compile-seconds",type=float,default=30)
 ap.add_argument("--adopt-verified",action="store_true")
 a=ap.parse_args(argv)
 need(math.isfinite(a.seconds) and 0<a.seconds<=1200 and 0<a.compile_seconds<=30,"bounded reconstruction/compile budgets")
 need(0<a.memory_mib<=8192,"bounded address space")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 original=a.pipeline_out.resolve()/"native";attempt=out/"native-attempt";attempt.mkdir(parents=True,exist_ok=True)
 need(original.resolve()!=attempt.resolve(),"separate original and attempt directories")
 start=time.monotonic();compile_seconds=0.0;rc=1
 rec={"format":"isp-original-unit-last-checkpoint-reconstruction-runner-v1","status":"running","phase":"inputs",
  "newDixonDigitsComputed":0,"newInverseComputed":False,"largeDataUploadedOrCommitted":False,
  "fullOriginal4354VerificationComplete":False,"parameters":{},"events":[]}
 rp=out/"constant-unit-last-checkpoint-reconstruction-receipt.json"
 def save_receipt():
  rec["mathematicalElapsedSeconds"]=time.monotonic()-start-compile_seconds
  rec["compileElapsedSeconds"]=compile_seconds;save(rp,rec)
 def remaining():return a.seconds-(time.monotonic()-start-compile_seconds)
 try:
  inputs={"native_source":identity(a.native_source),"adapter_source":identity(a.adapter_source)}
  need(inputs["native_source"]=={"bytes":NATIVE_PIN[0],"sha256":NATIVE_PIN[1]},"frozen native source bytes")
  need(inputs["adapter_source"]=={"bytes":ADAPTER_PIN[0],"sha256":ADAPTER_PIN[1]},"reconstruct-only adapter bytes")
  bp=a.pipeline_out/"native-input"/"actual-constant-unit-eighteen.bin"
  inputs["native_input"]=identity(bp)
  need(inputs["native_input"]=={"bytes":INPUT_PIN[0],"sha256":INPUT_PIN[1]},"same whole original eighteen input")
  active=original/"checkpoint-active.txt";before=manifest(active);active_id=identity(active)
  state=original/("checkpoint-"+str(before["slot"])+".bin")
  need(state.stat().st_size==before["bytes"],"active original checkpoint complete extent")
  prior_native=read(original/"constant-unit-dixon-native-receipt.json")
  need(prior_native["binding"]==BINDING and prior_native["parameters"]["inputSHA256"]==INPUT_PIN[1]
       and prior_native["completedDigits"]==before["digits"] and prior_native["internalPrime"]==before["prime"],
       "latest actual native receipt and complete active digit agree")
  need(not prior_native.get("unitSolutionExactVerified",False),"already solved unit must use frozen final consumer directly")
  prior_receipt_id=identity(original/"constant-unit-dixon-native-receipt.json")
  material={"runner":identity(__file__),"inputs":inputs,"mathematicalBinding":BINDING,
   "originalActiveManifest":active_id,"originalCheckpoint":before,
   "originalNativeReceipt":prior_receipt_id,"operation":"restore original X,N; one reconstruct; zero digits/inverse"}
  adapter_binding=hashlib.sha256(canonical(material)).hexdigest()
  rec["parameters"].update({"binding":adapter_binding,"mathematicalBinding":BINDING,
    "inputIdentity":material,"secondsLimit":a.seconds,"memoryMiB":a.memory_mib,
    "adoptionRequested":a.adopt_verified,"expectedOriginalDigits":before["digits"]})
  invocation=out/"invocation.json"
  if invocation.exists():need(read(invocation)["binding"]==adapter_binding,"same actual checkpoint reconstruction invocation")
  else:save(invocation,{"binding":adapter_binding,"inputIdentity":material})
  rec["phase"]="compile";save_receipt()
  build=out/"build";build.mkdir(exist_ok=True);exe=build/"reconstruct-only"
  source=build/"reconstruct-only.cpp";frozen=build/NATIVE_NAME
  for sourcepath,target in ((a.adapter_source,source),(a.native_source,frozen)):
   if target.exists():need(identity(target)==identity(sourcepath),"unchanged copied source")
   else:shutil.copyfile(sourcepath,target)
  cm=build/"compile-receipt.json";compile_material={"native":inputs["native_source"],"adapter":inputs["adapter_source"],
    "flags":["-std=c++17","-O2","-lflint","-lgmp"]}
  if cm.exists() and exe.exists():
   cc=read(cm);need(cc["inputIdentity"]==compile_material and cc["exitCode"]==0
       and identity(exe)==cc["executableIdentity"],"same actual completed compile")
   rec["events"].append({"reusedCompleteAdapterCompile":True})
  else:
   cr=child(["g++","-std=c++17","-O2",str(source),"-lflint","-lgmp","-o",str(exe)],
       out/"compile.log",a.compile_seconds,a.memory_mib,3)
   compile_seconds=cr["wallSeconds"]
   cc={**cr,"inputIdentity":compile_material}
   if cr["exitCode"]==0:cc["executableIdentity"]=identity(exe)
   save(cm,cc);rec["parameters"]["actualCompile"]=cc;save_receipt()
   if cr["exitCode"]!=0:
    rec["compileLogTail"]=(out/"compile.log").read_text(errors="replace")[-5000:]
    raise ValueError("actual adapter compilation failed")
  rec["phase"]="one-current-precision-reconstruction";save_receipt()
  nrpath=attempt/"constant-unit-reconstruct-only-native-receipt.json"
  done=read(nrpath) if nrpath.exists() else None
  if done and done.get("status")=="completed":
   need(done.get("binding")==BINDING and done["completedDigits"]==before["digits"]
        and done["parameters"]["originalCheckpointSHA256"]==before["sha256"],"same completed adapter attempt")
   rec["events"].append({"reusedCompletedSameCheckpointAttempt":True})
  else:
   rem=remaining()-5;need(rem>0,"positive remaining reconstruction time")
   cr=child([str(exe),str(bp),str(original),str(attempt),BINDING,str(rem),
      str(before["digits"]),before["sha256"],INPUT_PIN[1]],out/"reconstruct-only.log",
      rem,a.memory_mib,10)
   rec["parameters"]["actualNativeRun"]=cr
   done=read(nrpath) if nrpath.exists() else {}
  rec["parameters"]["nativeReconstruction"]=done
  # This is an actual post-check of the original bytes, before optional solution adoption.
  need(manifest(active)==before and identity(active)==active_id,"original active manifest unchanged")
  need(identity(state)=={"bytes":before["bytes"],"sha256":before["sha256"]},"original complete source/residual bytes unchanged")
  need(identity(original/"constant-unit-dixon-native-receipt.json")==prior_receipt_id,"original native receipt unchanged before explicit adoption")
  rec["originalActiveManifestUnchanged"]=True;rec["originalCompleteCheckpointUnchanged"]=True
  temps=[]
  for p in sorted(attempt.iterdir()):
   if p.is_file() and not p.name.endswith(".tmp"):
    temps.append({"file":"native-attempt/"+p.name,**identity(p),"temporaryOnly":True})
  rec["parameters"]["temporaryFiles"]=temps
  if not done:
   cr=rec["parameters"].get("actualNativeRun",{})
   need(cr.get("outerDeadlineReached") or cr.get("exitCode")==75,
        "native exited without a reconstruction receipt; inspect reconstruct-only.log")
   rec.update(status="budget-exhausted",outcome="checkpoint-reconstruction-unfinished");rc=75
  elif done.get("status")=="budget-exhausted":
   rec.update(status="budget-exhausted",outcome="checkpoint-reconstruction-unfinished");rc=75
  elif done.get("status")!="completed":
   raise ValueError("actual reconstruct-only native failed: "+str(done.get("error","no native result")))
  else:
   need(done["newDigitsComputed"]==0 and not done["newInverseComputed"] and done["originalActiveManifestUnchanged"],
      "exact reconstruction-only scope")
   if done["allOriginalUnitRowsVerified"]:
    need(done["outcome"]=="verified-original-unit-solution" and done["originalUnitProductCoordinates"]==4318*18,
         "all original unit products really completed")
    nr=read(attempt/"constant-unit-dixon-native-receipt.json")
    solution=attempt/"active-unit-rational-solution.bin";sid=identity(solution)
    need(nr["status"]=="completed" and nr["phase"]=="constant-unit-multiple-rhs-rational-solution-complete"
      and nr["binding"]==BINDING and nr["allOriginalUnitRowsVerified"] and nr["unitSolutionExactVerified"]
      and nr["parameters"]["inputSHA256"]==INPUT_PIN[1]
      and sid=={"bytes":nr["parameters"]["solutionBytes"],"sha256":nr["parameters"]["solutionSHA256"]},
      "complete actual original unit solution bytes")
    with solution.open("rb") as f:head=f.read(88)
    need(head[:8]==b"R15CUSL1" and head[8:72].decode()==BINDING
      and struct.unpack_from("<IIII",head,72)==(4318,18,before["prime"],before["digits"]),"unit solution exact protocol")
    rec.update(status="completed",outcome="verified-original-unit-solution",
      allOriginalUnitRowsVerified=True,originalUnitProductCoordinates=4318*18)
    rec["parameters"]["solutionIdentity"]=sid
    if a.adopt_verified:
     # Explicit, audited bridge for the unchanged frozen --through final consumer.
     target=original/"active-unit-rational-solution.bin"
     if target.exists():need(identity(target)==sid,"do not replace a different existing solution")
     else:
      tmp=target.with_name(target.name+".from-checkpoint.tmp");shutil.copyfile(solution,tmp)
      need(identity(tmp)==sid,"complete adoption copy");os.replace(tmp,target)
     adoption={"format":"isp-explicit-verified-unit-solution-adoption-v1","adapterBinding":adapter_binding,
       "mathematicalBinding":BINDING,"originalActiveManifest":active_id,"originalCheckpoint":before,
       "solutionIdentity":sid,"sourceNativeReceiptIdentity":identity(attempt/"constant-unit-dixon-native-receipt.json"),
       "sourceAdapterReceiptIdentity":identity(nrpath),"adapterSourceIdentity":inputs["adapter_source"],
       "frozenNativeSourceIdentity":inputs["native_source"],"newDigitsComputed":0,
       "allOriginalUnitRowsVerified":True,"fullOriginal4354VerificationComplete":False}
     save(original/"unit-solution-adoption-receipt.json",adoption)
     nr["parameters"]["explicitReconstructionOnlyAdoption"]=adoption
     nr["parameters"]["reconstructionCheckpointDirectory"]=str(attempt)
     save(original/"constant-unit-dixon-native-receipt.json",nr)
     rec["verifiedSolutionAdoptedForFrozenFinalConsumer"]=True
     need(manifest(active)==before and identity(active)==active_id,"adoption does not change digit cursor")
   else:
    need(done["outcome"]=="no-verified-unit-solution-at-this-checkpoint","precise finite unsuccessful attempt outcome")
    rec.update(status="completed",outcome=done["outcome"],allOriginalUnitRowsVerified=False)
   rc=0
 except Exception as e:
  rec.update(status="failed",error=str(e),exceptionType=type(e).__name__)
  (out/"exception.log").write_text(traceback.format_exc(),encoding="utf-8");rc=1
 finally:save_receipt()
 need(rp.stat().st_size<100000,"small reconstruction summary only")
 print(json.dumps(rec,separators=(",",":")),flush=True);return rc
if __name__=="__main__":sys.exit(main())
