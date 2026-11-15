#!/usr/bin/env python3
"""Bounded complete original F127 graded-module basis, with native two-slot recovery.
Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-15.
Every complementary original source, including zero NF rows, remains in the DAG.
No F31 numerical basis and no expected torsion dimension are used.
"""
from __future__ import annotations
import argparse,hashlib,json,os,resource,signal,struct,subprocess,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
PINS={
 "2026-11-15-r150-original-f127-bitplane-789f.hpp":"03272796bb20c883291d27c9a0b796197f8295ccd9b16552c13894657dc8afd3",
 "2026-11-15-r150-original127-graded-module-gb-789f.cpp":"696c3c07461de74f9a2d3d92dbe835e1b5aa057d7dd1392c0baf8d7ffe57e508"}
NF_NATIVE_SHA="46ef43c439aadb77a7458c97a0bce120846e6aa57d79bc9aed78d211242f81f8"
NF_MODEL_SHA="a0eec7261177a8806e6761e3bee98d6740e5cbf1d225a9da107c27c47a82d349"
FORMAT="r150-original127-complete-graded-module-pipeline-v1"
def check(ok,msg):
 if not ok:raise ValueError(msg)
def canonical(x):return json.dumps(x,sort_keys=True,separators=(",",":")).encode("ascii")
def sha(path):
 h=hashlib.sha256()
 with path.open("rb") as f:
  for b in iter(lambda:f.read(1048576),b""):h.update(b)
 return h.hexdigest()
def record(p):return {"file":p.name,"bytes":p.stat().st_size,"sha256":sha(p),"temporaryOnly":True}
def atomic(p,obj):
 t=p.with_name(p.name+".tmp");t.write_bytes(canonical(obj)+b"\n");os.replace(t,p)
def verify_descriptor(root,d):
 p=root/d["file"]
 check(p.is_file() and p.stat().st_size==d["bytes"] and sha(p)==d["sha256"],"exact retained file "+str(p))
 return p
def active_state(root,binding,parent):
 selector=root/"gb-active.bin";b=selector.read_bytes()
 check(len(b)==92 and b[:8]==b"R15GA127" and b[8:72].decode()==binding and b[-8:]==b"ENDGA127","complete active-slot selector")
 generation,slot=struct.unpack_from("<QI",b,72);check(slot==generation%2,"active checkpoint generation")
 p=root/("gb-state-"+str(slot)+".bin")
 with p.open("rb") as f:
  h=f.read(210);f.seek(-8,2);end=f.read(8)
 check(len(h)==210 and h[:8]==b"R15GC127" and h[8:72].decode()==binding and h[72:136].decode()==parent and end==b"ENDGC127","whole native state identity")
 values=struct.unpack_from("<QIIIIIIBBIIQQQQ",h,136)
 gen,prime,q,D,processed,rank,max_input_plus1,in_row,finalized,raw,node,reductions,swaps,input_offset,dag_bytes=values
 check(gen==generation and (prime,q,D)==(127,1034,45) and in_row in (0,1) and finalized in (0,1),"whole native state geometry")
 return {"generation":generation,"activeSlot":slot,"processedSources":processed,"basisRank":rank,
         "maximumInputDegree":max_input_plus1-1,"currentSourceActive":bool(in_row),
         "finalized":bool(finalized),"currentOriginalRawSource":raw,"currentSourceNode":node,
         "reductions":reductions,"swaps":swaps,"committedInputOffset":input_offset,
         "committedDAGBytes":dag_bytes,"activeStateFile":p.name}
def inspect_basis(path,binding,ns):
 with path.open("rb") as f:
  def read(n):
   b=f.read(n);check(len(b)==n,"complete final basis record");return b
  check(read(8)==b"R15GB127" and read(64).decode()==binding,"complete final basis identity")
  prime,q,D,rank,nt=struct.unpack("<IIIII",read(20))
  check((prime,q,D,nt)==(127,1034,45,9) and 0<=rank<=q,"dynamic final basis dimensions")
  nw=(D+1)*((q+31)//32);record_bytes=7*nw*4;previous=0;degrees=[];nodes=[]
  for j in range(rank):
   c,d,node,scale=struct.unpack("<HBIB",read(8))
   check(previous<c<=q and d<=D and node>0 and 0<scale<127,"all final basis source records")
   previous=c;degrees.append(d);nodes.append(node);read(record_bytes)
  for j in range(nt):read(record_bytes)
  check(read(8)==b"ENDGB127" and f.read(1)==b"","complete basis and all target EOF")
 return {"basisRank":rank,"maximumBasisDegree":max(degrees,default=-1),
         "sumBasisDegrees":sum(degrees),"freeModuleRank":q-rank,"components":q,
         "originalTargetCount":nt,"processedOriginalSources":ns,
         "allBasisSourceNodesPresent":True,"allNineOriginalTargetRowsRetained":True}
def main():
 ap=argparse.ArgumentParser()
 for k in ("normal-forms-out","sources-root","out"):ap.add_argument("--"+k,type=Path,required=True)
 ap.add_argument("--seconds",type=float,default=900)
 ap.add_argument("--memory-mib",type=int,default=2048)
 ap.add_argument("--compile-seconds",type=float,default=30)
 a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=True)
 check(1<=a.seconds<=7200 and 1024<=a.memory_mib<=8192 and 1<=a.compile_seconds<=120,"bounded native GB configuration")
 started=time.monotonic();rp=a.out/"original127-graded-module-pipeline-receipt.json"
 previous=json.loads(rp.read_text()) if rp.exists() else None
 r={"format":FORMAT,"status":"running","parameters":{"prime":127,
    "author":"Astra-ISP-789f / normal_annihilator","aiAssisted":"GPT-6 Astra Pro",
    "allLargeArraysTemporaryOnly":True,"affineTorsionDegreeComputed":False,
    "infinityGoodReductionProved":False,"oldField31NumericBasisReused":False},"events":[]}
 nrp=a.out/"gb-native-receipt.json"
 files=[a.out/n for n in ("gb-active.bin","gb-state-0.bin","gb-state-1.bin","gb-operations.bin","gb-basis.bin","gb-basis-metadata.json")]
 def save():r["elapsedSeconds"]=time.monotonic()-started;atomic(rp,r)
 def limits():
  resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2);resource.setrlimit(resource.RLIMIT_CORE,(0,0))
 try:
  for name,digest in PINS.items():check(sha(a.sources_root/name)==digest,"frozen original127 GB source "+name)
  parent_path=a.normal_forms_out/"original127-normal-form-pipeline-receipt.json"
  parent=json.loads(parent_path.read_text());p=parent.get("parameters",{})
  check(parent.get("format")=="r150-original127-normal-form-pipeline-v2" and parent.get("status")=="completed","complete all6188-source NF parent")
  identity0=p["identity"]
  check(identity0["sources"]["2026-11-15-r150-original127-normal-form-789f.cpp"]==NF_NATIVE_SHA and identity0["modelSource"]==NF_MODEL_SHA,"original NF source identity")
  ns=int(identity0["remainingSourceCount"]);check(ns>0 and ns+3333==6188,"entire original source complement")
  audit=p["completeNormalFormAudit"]
  check(audit.get("allOriginalSourceRecordsVerified") is True and audit.get("noSourceDroppedBeforeOrAfterNormalForms") is True and audit["remainingSourceCount"]==ns,"complete normal-form source audit")
  native0=p["nativeStatistics"]
  check(native0.get("all6188NativeOriginalSourceIdentitiesVerified") is True and native0.get("allOriginalRowsCompleted") is True and native0["completedSources"]==ns and native0["completedTargets"]==9,"native original source completion")
  parent_files={d["file"]:d for d in p["temporaryFiles"]}
  needed=("nf-normal-forms.bin","nf-forward.bin","nf-backward.bin","nf-reduction.bin","nf-component-dictionary.bin")
  for name in needed:verify_descriptor(a.normal_forms_out,parent_files[name])
  nf_input=a.normal_forms_out/"nf-normal-forms.bin"
  identity={"prime":127,"sources":PINS,"wrapperSHA256":sha(Path(__file__)),
    "normalFormBinding":parent["binding"],"normalFormFiles":{n:parent_files[n] for n in needed},
    "originalSourceCount":6188,"remainingSourceCount":ns,"algorithm":"complete-univariate-streaming-GB-two-slot-active-source"}
  binding=hashlib.sha256(canonical(identity)).hexdigest();r["binding"]=binding
  r["parameters"].update({"identity":identity,"parentActualReceipt":record(parent_path),
     "seconds":a.seconds,"memoryMiB":a.memory_mib,"maximumAll1034PivotCacheBytes":1034*46*33*7*4*9})
  if previous:
   check(previous.get("binding")==binding,"same immutable original127 GB continuation")
   for d in previous.get("parameters",{}).get("temporaryFiles",[]):verify_descriptor(a.out,d)
   if previous.get("status")=="completed":
    r["status"]="completed";r["outcome"]="reused-complete-original127-module-basis"
    r["parameters"].update({k:v for k,v in previous["parameters"].items() if k not in ("seconds","memoryMiB")})
    r["parameters"]["completedMathematicsRecomputed"]=False
    save();print(json.dumps({"status":"completed","reusedComplete":True}),flush=True);return 0
  elif any(p.exists() for p in files):raise ValueError("unbound existing original127 GB output")
  binary=a.out/"original127-graded-module-gb";build_receipt=a.out/"compile.json"
  version=subprocess.run(["g++","--version"],capture_output=True,text=True,timeout=10,check=True).stdout.splitlines()[0]
  build_key=hashlib.sha256(canonical({"sources":PINS,"compiler":version,"flags":["-std=c++17","-O3","-DNDEBUG"]})).hexdigest()
  old_build=json.loads(build_receipt.read_text()) if build_receipt.exists() else {}
  if not(binary.exists() and old_build.get("key")==build_key and old_build.get("binary")==record(binary)):
   ct=time.monotonic()
   cp=subprocess.run(["g++","-std=c++17","-O3","-DNDEBUG",str(a.sources_root/"2026-11-15-r150-original127-graded-module-gb-789f.cpp"),"-o",str(binary)],capture_output=True,text=True,timeout=a.compile_seconds)
   r["parameters"]["compileSeconds"]=time.monotonic()-ct
   check(cp.returncode==0,"GB compilation: "+cp.stderr[-3000:])
   atomic(build_receipt,{"key":build_key,"compiler":version,"binary":record(binary)})
   r["parameters"]["compileReused"]=False
  else:r["parameters"]["compileReused"]=True
  r["parameters"]["compiler"]=version;r["parameters"]["binary"]=record(binary);save()
  log=a.out/"native.log";native_start=time.monotonic();hard_stop=False
  with log.open("ab") as f:
   process=subprocess.Popen([str(binary),str(nf_input),str(a.out/"gb"),parent["binding"],binding,str(a.seconds)],
     stdout=f,stderr=subprocess.STDOUT,preexec_fn=limits,start_new_session=True)
   try:code=process.wait(timeout=a.seconds+15)
   except subprocess.TimeoutExpired:
    hard_stop=True;os.killpg(process.pid,signal.SIGTERM)
    try:process.wait(timeout=5)
    except subprocess.TimeoutExpired:os.killpg(process.pid,signal.SIGKILL);process.wait()
    code=75
  r["parameters"].update({"nativeWallSeconds":time.monotonic()-native_start,"nativeExitCode":code,"nativeHardBudgetStop":hard_stop})
  check(nrp.exists(),"no complete GB checkpoint receipt")
  nr=json.loads(nrp.read_text())
  check(nr.get("format")=="r150-original127-graded-gb-native-v2" and nr.get("binding")==binding and nr.get("parentNFBinding")==parent["binding"],"native GB source binding")
  state=active_state(a.out,binding,parent["binding"])
  r["parameters"]["nativeStatistics"]=nr;r["parameters"]["committedState"]=state
  check(state["processedSources"]<=ns and (not state["currentSourceActive"] or state["processedSources"]<ns),"complete active-source counters")
  check((a.out/"gb-operations.bin").stat().st_size>=state["committedDAGBytes"] and nf_input.stat().st_size>=state["committedInputOffset"],"retained original input and source DAG prefixes")
  for k in ("generation","processedSources","basisRank","currentSourceActive","finalized","reductions","swaps","committedInputOffset","committedDAGBytes"):
   check(nr[k]==state[k],"whole checkpoint agrees with native receipt: "+k)
  if code==0:
   check(nr["status"]=="completed" and nr["allOriginalComplementSourcesCompleted"] is True and state["finalized"] and state["processedSources"]==ns,"all original source rows complete")
   actual=inspect_basis(a.out/"gb-basis.bin",binding,ns)
   meta=json.loads((a.out/"gb-basis-metadata.json").read_text())
   check(meta["binding"]==binding and meta["allOriginalSourceDAGRetained"] is True and meta["noParameterPolynomialInverted"] is True,"complete original module source scope")
   for k in ("basisRank","maximumBasisDegree","sumBasisDegrees","freeModuleRank","components","originalTargetCount","processedOriginalSources"):
    check(meta[k]==actual[k],"complete dynamic basis metadata "+k)
   r["parameters"]["completeBasisAudit"]=actual;r["parameters"]["basisMetadata"]=meta
   r["status"]="completed";r["outcome"]="complete-original127-graded-module-basis";rc=0
  elif code==75:
   r["status"]="budget-checkpoint";r["outcome"]="complete-active-original-source-state-retained";rc=75
  else:raise RuntimeError("native GB failed: "+log.read_bytes()[-3000:].decode(errors="replace"))
 except BaseException as e:
  r["status"]="failed";r["errorType"]=type(e).__name__;r["error"]=str(e);rc=1
 finally:
  r["parameters"]["temporaryFiles"]=[record(p) for p in files if p.exists()]
  if nrp.exists():r["parameters"]["nativeReceipt"]=record(nrp)
  save()
 print(json.dumps({"status":r["status"],"outcome":r.get("outcome"),"elapsedSeconds":r["elapsedSeconds"],"error":r.get("error")}),flush=True)
 return rc
if __name__=="__main__":sys.exit(main())
