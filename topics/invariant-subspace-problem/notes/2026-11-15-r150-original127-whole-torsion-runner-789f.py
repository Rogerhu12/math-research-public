#!/usr/bin/env python3
"""Complete original F127 torsion and full affine characteristic polynomial.
Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-15.
The finite state includes all bounded free directions; all leakage is observed
to actual stabilization. The old field31 dimensions are never input.
"""
from __future__ import annotations
import argparse,hashlib,json,os,resource,signal,struct,subprocess,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
PINS={
 "2026-11-15-r150-original-f127-bitplane-789f.hpp":"03272796bb20c883291d27c9a0b796197f8295ccd9b16552c13894657dc8afd3",
 "2026-11-15-r150-original127-whole-torsion-state-789f.cpp":"d92bcb7395f4d81c89b6a5d291951a6d7bf920862ea68c6bb6b3fe454e485528"}
GB_NATIVE_SHA="696c3c07461de74f9a2d3d92dbe835e1b5aa057d7dd1392c0baf8d7ffe57e508"
FORMAT="r150-original127-whole-torsion-pipeline-v1"
def check(ok,msg):
 if not ok:raise ValueError(msg)
def canonical(x):return json.dumps(x,sort_keys=True,separators=(",",":")).encode("ascii")
def sha(p):
 h=hashlib.sha256()
 with Path(p).open("rb") as f:
  for b in iter(lambda:f.read(1048576),b""):h.update(b)
 return h.hexdigest()
def record(p):return {"file":p.name,"bytes":p.stat().st_size,"sha256":sha(p),"temporaryOnly":True}
def atomic(p,obj):
 t=p.with_name(p.name+".tmp");t.write_bytes(canonical(obj)+b"\n");os.replace(t,p)
def verify_file(root,d):
 p=root/d["file"];check(p.is_file() and p.stat().st_size==d["bytes"] and sha(p)==d["sha256"],"exact retained file "+str(p));return p
def active_state(root,binding,parent):
 b=(root/"torsion-active.bin").read_bytes()
 check(len(b)==92 and b[:8]==b"R15TA127" and b[8:72].decode()==binding and b[-8:]==b"ENDTA127","whole torsion active selector")
 generation,slot=struct.unpack_from("<QI",b,72);check(slot==generation%2,"active whole generation")
 path=root/("torsion-checkpoint-"+str(slot)+".bin")
 with path.open("rb") as f:h=f.read(272);f.seek(-8,2);end=f.read(8)
 check(len(h)==272 and h[:8]==b"R15TC127" and h[8:72].decode()==binding and h[72:136].decode()==parent and end==b"ENDTC127","whole native checkpoint identity")
 check(struct.unpack_from("<Q",h,136)[0]==generation,"whole native generation")
 geom=struct.unpack_from("<9I",h,144)
 prime,q,D,rank,B,total,n,nf,nt=geom
 check((prime,q,D,nt)==(127,1034,45,9) and rank+nf==q and n==total+B*nf,"complete dynamic finite window")
 counters=struct.unpack_from("<11I",h,180);values=struct.unpack_from("<6Q",h,224)
 phase,cols,targets,layer,obsrow,before,mulrow,obs,stable_plus1,verified,vt=counters
 return {"generation":generation,"activeSlot":slot,"phase":phase,"basisRank":rank,
  "maximumBasisDegree":B,"sumBasisDegrees":total,"stateDimension":n,"freeModuleRank":nf,
  "stateColumnsComplete":cols,"originalTargetsNormalized":targets,"currentObservationPower":layer,
  "currentObservationRow":obsrow,"rankBeforeCurrentLayer":before,"nextObservationRowsComplete":mulrow,
  "observationRank":obs,"stableAtPower":stable_plus1-1,"verifiedKernelColumns":verified,
  "verifiedTargets":vt,"committedSourceTraceBytes":values[0],"normalOperations":values[1],
  "linearReductions":values[2],"kernelOriginalLeakageProducts":values[3],
  "kernelInvarianceProducts":values[4],"kernelObservedProducts":values[5],"activeStateFile":path.name}
def inspect_whole_state(path,binding,parent,with_action=False):
 with path.open("rb") as f:
  h=f.read(184)
  check(len(h)==184 and h[:8]==b"R15TS127" and h[8:72].decode()==binding and h[72:136].decode()==parent,"entire original torsion certificate identity")
  prime,q,D,rank,B,total,n,nf,t,nt,obs,stable=struct.unpack_from("<12I",h,136)
  check((prime,q,D,nt)==(127,1034,45,9) and rank+nf==q and n==total+B*nf and t+obs==n and stable<=n,"entire original dynamic torsion geometry")
  body=184+3*n+2*nf
  flags_at=body+n*n+nf*n+nt*n
  f.seek(flags_at);bounded=list(f.read(nt));members=list(f.read(nt))
  check(len(bounded)==nt and len(members)==nt and all(x in (0,1) for x in bounded+members),"entire original target flags")
  action_at=flags_at+2*nt+t*n
  expected=action_at+t*t+nt*t+obs*(4+n)+obs*8+8
  check(path.stat().st_size==expected,"all state, free leakage, kernel, action, observation and target coordinates retained")
  f.seek(-8,2);check(f.read(8)==b"ENDTS127","whole state EOF")
  result={"prime":prime,"components":q,"basisRank":rank,"maximumBasisDegree":B,
    "sumBasisDegrees":total,"stateDimension":n,"freeModuleRank":nf,"torsionDimension":t,
    "observationRank":obs,"stableAtPower":stable,"targetCount":nt,
    "originalTargetBoundedFlags":bounded,"originalTargetInTorsionFlags":members,
    "actionOffset":action_at,"allFreePolynomialDirectionsRetained":True}
  if with_action:
   check(t<=2048,"whole torsion verified but characteristic expansion exceeds this worker's bounded allocation")
   f.seek(action_at);data=f.read(t*t)
   check(len(data)==t*t and all(v<127 for v in data),"complete canonical original torsion action")
   result["action"]=data
  return result
def characteristic_worker(argv):
 ap=argparse.ArgumentParser()
 for k in ("state","state-sha256","binding","parent-binding","out"):ap.add_argument("--"+k,required=True)
 a=ap.parse_args(argv);start=time.monotonic();p=Path(a.state)
 check(sha(p)==a.state_sha256,"actual whole state before characteristic computation")
 z=inspect_whole_state(p,a.binding,a.parent_binding,True)
 import flint
 from flint import nmod_mat,nmod_poly
 t=z["torsionDimension"]
 if t:pol=nmod_mat(t,t,list(z["action"]),127).charpoly()
 else:pol=nmod_poly([1],127)
 coefficients=[int(c) for c in pol.coeffs()]
 check(pol.degree()==t and coefficients[-1]==1,"complete characteristic degree and monic normalization")
 unit,factors=pol.factor();product=nmod_poly([int(unit)],127);out_factors=[]
 for f,e in factors:
  c=[int(v) for v in f.coeffs()];product*=f**int(e)
  out_factors.append({"coefficients":c,"degree":int(f.degree()),"multiplicity":int(e)})
 check(product==pol,"full finite-field characteristic factor product")
 data={"format":"r150-original127-whole-torsion-characteristic-v1","status":"completed",
   "binding":a.binding,"parentGBBinding":a.parent_binding,"wholeStateSHA256":a.state_sha256,
   "workerSHA256":sha(__file__),"pythonFlintVersion":getattr(flint,"__version__","unknown"),
   "torsionDimension":t,"characteristicDegree":t,"coefficients":coefficients,
   "factorizationUnit":int(unit),"factors":out_factors,"completeFactorProductVerified":True,
   "characteristicPolynomialOfEntireTorsionAction":True,"elapsedSeconds":time.monotonic()-start}
 atomic(Path(a.out),data)
 print(json.dumps({"status":"completed","wholeTorsionDegree":t,"factorCount":len(factors)}),flush=True)
 return 0
def main():
 ap=argparse.ArgumentParser()
 for k in ("gb-out","sources-root","out"):ap.add_argument("--"+k,type=Path,required=True)
 ap.add_argument("--seconds",type=float,default=60)
 ap.add_argument("--memory-mib",type=int,default=2048)
 ap.add_argument("--compile-seconds",type=float,default=30)
 ap.add_argument("--characteristic-seconds",type=float,default=30)
 a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=True)
 check(1<=a.seconds<=1800 and 1024<=a.memory_mib<=8192 and 1<=a.compile_seconds<=120 and 1<=a.characteristic_seconds<=300,"bounded whole-torsion configuration")
 start=time.monotonic();rp=a.out/"original127-whole-torsion-pipeline-receipt.json"
 previous=json.loads(rp.read_text()) if rp.exists() else None
 r={"format":FORMAT,"status":"running","parameters":{"prime":127,"author":"Astra-ISP-789f / normal_annihilator",
   "aiAssisted":"GPT-6 Astra Pro","completeOriginalSourceCount":6188,"allLargeArraysTemporaryOnly":True,
   "infinityGoodReductionProved":False,"characteristicZeroDegreeBoundInferred":False,
   "oldField31ProfileUsed":False},"events":[]}
 nrp=a.out/"torsion-native-receipt.json";charp=a.out/"whole-torsion-characteristic.json"
 files=[a.out/n for n in ("torsion-active.bin","torsion-checkpoint-0.bin","torsion-checkpoint-1.bin","torsion-normal-operations.bin","torsion-whole-state.bin")]
 files += [a.out/("torsion-target-"+str(j)+".bin") for j in range(2,11)]
 files += [charp]
 def save():r["elapsedSeconds"]=time.monotonic()-start;atomic(rp,r)
 def limits():
  resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2);resource.setrlimit(resource.RLIMIT_CORE,(0,0))
 try:
  for name,digest in PINS.items():check(sha(a.sources_root/name)==digest,"frozen whole-torsion source "+name)
  pp=a.gb_out/"original127-graded-module-pipeline-receipt.json";parent=json.loads(pp.read_text());p=parent.get("parameters",{})
  check(parent.get("format")=="r150-original127-complete-graded-module-pipeline-v1" and parent.get("status")=="completed","complete original127 GB parent")
  check(p["identity"]["sources"]["2026-11-15-r150-original127-graded-module-gb-789f.cpp"]==GB_NATIVE_SHA,"frozen complete GB native")
  check(p["identity"]["originalSourceCount"]==6188 and p["identity"]["remainingSourceCount"]+3333==6188,"all original sources retained in basis")
  audit=p["completeBasisAudit"];meta=p["basisMetadata"]
  check(audit["allBasisSourceNodesPresent"] and audit["allNineOriginalTargetRowsRetained"] and meta["allOriginalSourceDAGRetained"] and meta["noParameterPolynomialInverted"],"complete original module and target scope")
  pf={d["file"]:d for d in p["temporaryFiles"]}
  needed=("gb-basis.bin","gb-operations.bin","gb-basis-metadata.json")
  for name in needed:verify_file(a.gb_out,pf[name])
  identity={"prime":127,"sources":PINS,"wrapperSHA256":sha(__file__),"parentGBBinding":parent["binding"],
    "originalBasisFiles":{n:pf[n] for n in needed},"algorithm":"whole-standard-window-and-complete-free-observability"}
  binding=hashlib.sha256(canonical(identity)).hexdigest();r["binding"]=binding
  r["parameters"].update({"identity":identity,"parentActualReceipt":record(pp),
    "seconds":a.seconds,"memoryMiB":a.memory_mib,"characteristicSeconds":a.characteristic_seconds})
  if previous:
   check(previous.get("binding")==binding,"same whole-torsion mathematical continuation")
   for d in previous.get("parameters",{}).get("temporaryFiles",[]):verify_file(a.out,d)
   if previous.get("status")=="completed":
    r["status"]="completed";r["outcome"]="reused-complete-original127-whole-torsion"
    r["parameters"].update({k:v for k,v in previous["parameters"].items() if k not in ("seconds","memoryMiB","characteristicSeconds")})
    r["parameters"]["completedMathematicsRecomputed"]=False
    save();print(json.dumps({"status":"completed","reusedComplete":True}),flush=True);return 0
  elif any(p.exists() for p in files):raise ValueError("unbound existing whole-torsion data")
  native_complete=False
  if nrp.exists():
   nr=json.loads(nrp.read_text())
   if nr.get("binding")==binding and nr.get("status")=="completed":
    state=active_state(a.out,binding,parent["binding"])
    check(state["phase"]==5 and state["verifiedKernelColumns"]==state["stateDimension"]-state["observationRank"] and state["verifiedTargets"]==9,"native completed exact state")
    native_complete=True
  if not native_complete:
   binary=a.out/"original127-whole-torsion";build=a.out/"compile.json"
   compiler=subprocess.run(["g++","--version"],capture_output=True,text=True,timeout=10,check=True).stdout.splitlines()[0]
   bk=hashlib.sha256(canonical({"sources":PINS,"compiler":compiler,"flags":["-std=c++17","-O3","-DNDEBUG"]})).hexdigest()
   old=json.loads(build.read_text()) if build.exists() else {}
   if not(binary.exists() and old.get("key")==bk and old.get("binary")==record(binary)):
    ct=time.monotonic()
    cp=subprocess.run(["g++","-std=c++17","-O3","-DNDEBUG",str(a.sources_root/"2026-11-15-r150-original127-whole-torsion-state-789f.cpp"),"-o",str(binary)],capture_output=True,text=True,timeout=a.compile_seconds)
    r["parameters"]["compileSeconds"]=time.monotonic()-ct
    check(cp.returncode==0,"whole-torsion compilation: "+cp.stderr[-3000:])
    atomic(build,{"key":bk,"compiler":compiler,"binary":record(binary)});r["parameters"]["compileReused"]=False
   else:r["parameters"]["compileReused"]=True
   r["parameters"]["compiler"]=compiler;r["parameters"]["binary"]=record(binary);save()
   log=a.out/"native.log";ct=time.monotonic();hard=False
   with log.open("ab") as f:
    process=subprocess.Popen([str(binary),str(a.gb_out/"gb-basis.bin"),str(a.out/"torsion"),parent["binding"],binding,str(a.seconds)],stdout=f,stderr=subprocess.STDOUT,preexec_fn=limits,start_new_session=True)
    try:code=process.wait(timeout=a.seconds+15)
    except subprocess.TimeoutExpired:
     hard=True;os.killpg(process.pid,signal.SIGTERM)
     try:process.wait(timeout=5)
     except subprocess.TimeoutExpired:os.killpg(process.pid,signal.SIGKILL);process.wait()
     code=75
   r["parameters"].update({"nativeWallSeconds":time.monotonic()-ct,"nativeExitCode":code,"nativeHardBudgetStop":hard})
   check(nrp.exists(),"no retained complete torsion checkpoint")
   nr=json.loads(nrp.read_text())
  else:
   code=0;r["parameters"]["completedNativeReused"]=True
  check(nr.get("format")=="r150-original127-whole-torsion-native-v1" and nr["binding"]==binding and nr["parentGBBinding"]==parent["binding"],"native whole-torsion source binding")
  state=active_state(a.out,binding,parent["binding"])
  r["parameters"]["nativeStatistics"]=nr;r["parameters"]["committedState"]=state
  for k in ("generation","phase","basisRank","maximumBasisDegree","sumBasisDegrees","stateDimension","freeModuleRank","stateColumnsComplete","originalTargetsNormalized","observationRank","stableAtPower","verifiedKernelColumns","verifiedTargets","normalOperations","linearReductions","committedSourceTraceBytes"):
   check(nr[k]==state[k],"whole native checkpoint consistency "+k)
  check((a.out/"torsion-normal-operations.bin").stat().st_size>=state["committedSourceTraceBytes"],"complete original normal-form operation trace")
  if code==75:
   r["status"]="budget-checkpoint";r["outcome"]="whole-state-observation-or-verification-prefix-retained";rc=75
  elif code==0:
   check(nr["status"]=="completed" and nr["phase"]==5 and nr["completeStateAndFreeLeakageVerified"] and nr["actualObservationStableRowReductionVerified"] and nr["allKernelAndActionProductsVerified"],"entire torsion and all free leakage actually verified")
   actual=inspect_whole_state(a.out/"torsion-whole-state.bin",binding,parent["binding"])
   for k in ("basisRank","maximumBasisDegree","sumBasisDegrees","stateDimension","freeModuleRank","torsionDimension","observationRank","stableAtPower","originalTargetBoundedFlags","originalTargetInTorsionFlags"):
    check(actual[k]==nr[k],"whole certificate/native identity "+k)
   check(actual["basisRank"]==meta["basisRank"] and actual["sumBasisDegrees"]==meta["sumBasisDegrees"],"actual complete original basis profile")
   r["parameters"]["completeStateAudit"]=actual
   r["parameters"]["wholeAffineTorsionDegree"]=actual["torsionDimension"]
   r["parameters"]["fullOriginalGenericRank"]=3333+actual["basisRank"]
   r["parameters"]["wholeAffineDegreeVerified"]=True
   whole=record(a.out/"torsion-whole-state.bin")
   char=None
   if charp.exists():
    char=json.loads(charp.read_text())
    check(char["binding"]==binding and char["wholeStateSHA256"]==whole["sha256"] and char["workerSHA256"]==sha(__file__),"same cached whole-action characteristic")
   else:
    ct=time.monotonic();clog=a.out/"characteristic.log"
    with clog.open("ab") as f:
     try:
      cp=subprocess.run([sys.executable,str(Path(__file__).resolve()),"--characteristic-worker","--state",str(a.out/"torsion-whole-state.bin"),"--state-sha256",whole["sha256"],"--binding",binding,"--parent-binding",parent["binding"],"--out",str(charp)],stdout=f,stderr=subprocess.STDOUT,preexec_fn=limits,timeout=a.characteristic_seconds)
     except subprocess.TimeoutExpired:
      cp=None
    r["parameters"]["characteristicWallSeconds"]=time.monotonic()-ct
    if cp is None:
     r["status"]="budget-checkpoint";r["outcome"]="whole-torsion-verified-characteristic-pending";rc=75;save();return rc
    check(cp.returncode==0,"whole characteristic worker: "+clog.read_bytes()[-3000:].decode(errors="replace"))
    char=json.loads(charp.read_text())
   check(char["status"]=="completed" and char["torsionDimension"]==actual["torsionDimension"] and char["characteristicDegree"]==actual["torsionDimension"] and char["completeFactorProductVerified"] and char["characteristicPolynomialOfEntireTorsionAction"],"entire original affine characteristic polynomial")
   r["parameters"]["completeCharacteristic"]=char
   r["status"]="completed";r["outcome"]="complete-original127-whole-affine-torsion";rc=0
  else:raise RuntimeError("whole torsion native failed: "+(a.out/"native.log").read_bytes()[-3000:].decode(errors="replace"))
 except BaseException as e:
  r["status"]="failed";r["errorType"]=type(e).__name__;r["error"]=str(e);rc=1
 finally:
  r["parameters"]["temporaryFiles"]=[record(p) for p in files if p.exists()]
  if nrp.exists():r["parameters"]["nativeReceipt"]=record(nrp)
  save()
 print(json.dumps({"status":r["status"],"outcome":r.get("outcome"),"elapsedSeconds":r["elapsedSeconds"],"error":r.get("error")}),flush=True)
 return rc
if __name__=="__main__":
 if len(sys.argv)>1 and sys.argv[1]=="--characteristic-worker":sys.exit(characteristic_worker(sys.argv[2:]))
 sys.exit(main())
