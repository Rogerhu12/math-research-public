#!/usr/bin/env python3
"""Run/resume complete original F127 normal forms from the exact model.
Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-15.
Time and memory are excluded from the mathematical binding. A completed native
row is checkpointed before it can count. The original source trace is retained.
"""
from __future__ import annotations
import argparse,hashlib,json,os,resource,signal,struct,subprocess,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
PINS={
 "2026-11-15-r150-original-f127-bitplane-789f.hpp":"03272796bb20c883291d27c9a0b796197f8295ccd9b16552c13894657dc8afd3",
 "2026-11-15-r150-original127-normal-form-789f.cpp":"46ef43c439aadb77a7458c97a0bce120846e6aa57d79bc9aed78d211242f81f8"
}
MODEL_SOURCE_SHA="a0eec7261177a8806e6761e3bee98d6740e5cbf1d225a9da107c27c47a82d349"
FORMAT="r150-original127-normal-form-pipeline-v2"
def check(ok,msg):
 if not ok:raise ValueError(msg)
def canonical(x):return json.dumps(x,sort_keys=True,separators=(",",":")).encode("ascii")
def sha(path):
 h=hashlib.sha256()
 with path.open("rb") as f:
  for b in iter(lambda:f.read(1048576),b""):h.update(b)
 return h.hexdigest()
def record(path):return {"file":path.name,"bytes":path.stat().st_size,"sha256":sha(path),"temporaryOnly":True}
def atomic(path,obj):
 t=path.with_name(path.name+".tmp");t.write_bytes(canonical(obj)+b"\n");os.replace(t,path)
def inspect_complete_normal_forms(path,binding,dictionary):
 d=json.loads(dictionary.read_text())
 rows=d["originalRemainingSources"];restored=set(d["newlyRestoredOriginalSourceIDs"])
 check(d["originalSourceCount"]==6188 and len(rows)==d["remainingSourceCount"] and len(rows)+len(d["originalSelected3333"])==6188,
       "complete original source partition at consumer")
 zero=0;restored_zero=0;coefficient_count=0
 restored_nonzero=[]
 with path.open("rb") as f:
  def read(n):
   b=f.read(n);check(len(b)==n,"complete normal-form record");return b
  check(read(8)==b"R15NF127" and read(64).decode()==binding,"complete normal-form identity")
  ns,nt,q=struct.unpack("<III",read(12))
  check((ns,nt,q)==(len(rows),9,1034),"dynamic complete normal-form dimensions")
  for j in range(ns+nt):
   raw,target,count=struct.unpack("<IHI",read(10))
   check((raw,target)==((rows[j][2],0) if j<ns else (0,j-ns+2)),"every original source/target record")
   check(count<=q,"normal-form support bound")
   previous=0
   for k in range(count):
    c,length=struct.unpack("<HB",read(3))
    check(previous<c<=q and 1<=length<=46,"normal-form component/degree bounds");previous=c
    values=read(length);check(values[-1]!=0 and all(x<127 for x in values),"canonical original127 coefficient")
    coefficient_count+=length
   if j<ns:
    zero+=count==0
    if raw in restored:
     restored_zero+=count==0
     if count:restored_nonzero.append(raw)
  check(f.read(1)==b"","complete normal-form EOF")
 return {"allOriginalSourceRecordsVerified":True,"remainingSourceCount":ns,"targetCount":nt,
         "originalZeroNormalFormCount":zero,"newlyRestoredSourceCount":len(restored),
         "newlyRestoredZeroNormalFormCount":restored_zero,
         "newlyRestoredNonzeroNormalFormCount":len(restored_nonzero),
         "newlyRestoredNonzeroOriginalSourceIDs":restored_nonzero,
         "canonicalPolynomialCoefficientCount":coefficient_count,
         "noSourceDroppedBeforeOrAfterNormalForms":True}
def main():
 ap=argparse.ArgumentParser()
 for k in ("model-out","sources-root","out"):ap.add_argument("--"+k,type=Path,required=True)
 ap.add_argument("--seconds",type=float,default=180)
 ap.add_argument("--memory-mib",type=int,default=2048)
 ap.add_argument("--compile-seconds",type=float,default=30)
 a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=True)
 check(1<=a.seconds<=1800 and 1024<=a.memory_mib<=8192 and 1<=a.compile_seconds<=120,"bounded native configuration")
 started=time.monotonic()
 receipt_path=a.out/"original127-normal-form-pipeline-receipt.json"
 previous=json.loads(receipt_path.read_text()) if receipt_path.exists() else None
 r={"format":FORMAT,"status":"running","parameters":{"prime":127,
   "author":"Astra-ISP-789f / normal_annihilator","aiAssisted":"GPT-6 Astra Pro",
   "allLargeArraysTemporaryOnly":True,"oldField31NumericOperationsReused":False,
   "affineTorsionDegreeComputed":False,"infinityGoodReductionProved":False},"events":[]}
 prefix=a.out/"nf";native_receipt=a.out/"nf-native-receipt.json"
 paths=[a.out/("nf"+ending) for ending in (
   "-prebasis.bin","-forward.bin","-backward.bin","-component-dictionary.bin",
   "-progress.bin","-normal-forms.bin","-reduction.bin","-normal-forms.sing")]
 def limits():
  resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
  resource.setrlimit(resource.RLIMIT_CORE,(0,0))
 def save():
  r["elapsedSeconds"]=time.monotonic()-started;atomic(receipt_path,r)
 try:
  for name,digest in PINS.items():
   check(sha(a.sources_root/name)==digest,"pinned original127 source "+name)
  mr_path=a.model_out/"original127-model-receipt.json";mr=json.loads(mr_path.read_text())
  check(mr["format"]=="r150-original-fixed127-model-v2" and mr["status"]=="completed","paid exact127 model")
  mp=mr["parameters"]
  for k in ("all4433OriginalCoefficientChecks","all6188OriginalSourceLabelsVerified",
            "allOriginalSourcesPartitioned","allOriginalRowNormalizationConstantsAre127Units"):
   check(mp.get(k) is True,"original model gate "+k)
  check(mp["identity"]["sourceSHA256"]==MODEL_SOURCE_SHA,"fixed model-generator source")
  remaining=int(mp["remainingSourceCount"])
  check(mp["selectedSourceCount"]==3333 and remaining+3333==mp["originalSourceCount"]==6188,
        "complete original6188 source coverage")
  model=a.model_out/mp["originalModel"]["file"];dictionary=a.model_out/mp["originalDictionary"]["file"]
  for path,key in ((model,"originalModel"),(dictionary,"originalDictionary")):
   check(path.stat().st_size==mp[key]["bytes"] and sha(path)==mp[key]["sha256"],"exact127 model output "+key)
  identity={"prime":127,"sources":PINS,"modelSource":MODEL_SOURCE_SHA,
            "modelSHA256":mp["originalModel"]["sha256"],"dictionarySHA256":mp["originalDictionary"]["sha256"],
            "modelBinding":mr["binding"],"remainingSourceCount":remaining,"algorithm":"original3333 constant block then its complete6188-source complement and nine targets"}
  binding=hashlib.sha256(canonical(identity)).hexdigest();r["binding"]=binding
  r["parameters"].update({"identity":identity,"modelActualReceipt":record(mr_path),
    "seconds":a.seconds,"memoryMiB":a.memory_mib,
    "conservativePrebasisCachedRowsBytes":374602536,
    "normalFormCoordinates":1034,"completeOriginalSourceCount":6188})
  if previous:
   check(previous.get("binding")==binding,"same immutable normal-form continuation")
   for old in previous.get("parameters",{}).get("temporaryFiles",[]):
    p=a.out/old["file"]
    check(p.is_file() and p.stat().st_size==old["bytes"] and sha(p)==old["sha256"],"retained exact checkpoint "+p.name)
   if previous.get("status")=="completed":
    r["status"]="completed";r["outcome"]="reused-complete-original127-normal-forms"
    r["parameters"].update({k:v for k,v in previous["parameters"].items() if k not in ("seconds","memoryMiB")})
    r["parameters"]["completedMathematicsRecomputed"]=False
    save();print(json.dumps({"status":"completed","reusedComplete":True}),flush=True);return 0
  elif any(p.exists() for p in paths):
   raise ValueError("unbound existing normal-form output directory")
  binary=a.out/"original127-normal-form";build_receipt=a.out/"compile.json"
  version=subprocess.run(["g++","--version"],capture_output=True,text=True,timeout=10,check=True).stdout.splitlines()[0]
  build_key=hashlib.sha256(canonical({"sources":PINS,"compiler":version,"flags":["-std=c++17","-O3","-DNDEBUG"]})).hexdigest()
  old_build=json.loads(build_receipt.read_text()) if build_receipt.exists() else {}
  if not (binary.exists() and old_build.get("key")==build_key and old_build.get("binary")==record(binary)):
   command=["g++","-std=c++17","-O3","-DNDEBUG",str(a.sources_root/"2026-11-15-r150-original127-normal-form-789f.cpp"),"-o",str(binary)]
   ct=time.monotonic()
   cp=subprocess.run(command,capture_output=True,text=True,timeout=a.compile_seconds)
   r["parameters"]["compileSeconds"]=time.monotonic()-ct
   check(cp.returncode==0,"native compilation: "+cp.stderr[-3000:])
   atomic(build_receipt,{"key":build_key,"compiler":version,"flags":["-std=c++17","-O3","-DNDEBUG"],"binary":record(binary)})
   r["parameters"]["compileReused"]=False
  else:r["parameters"]["compileReused"]=True
  r["parameters"]["compiler"]=version;r["parameters"]["binary"]=record(binary);save()
  log=a.out/"native.log";native_started=time.monotonic();timed_out=False
  with log.open("ab") as f:
   process=subprocess.Popen([str(binary),str(model),str(prefix),binding,str(a.seconds)],
     stdout=f,stderr=subprocess.STDOUT,preexec_fn=limits,start_new_session=True)
   try: code=process.wait(timeout=a.seconds+15)
   except subprocess.TimeoutExpired:
    timed_out=True;os.killpg(process.pid,signal.SIGTERM)
    try:process.wait(timeout=5)
    except subprocess.TimeoutExpired:os.killpg(process.pid,signal.SIGKILL);process.wait()
    code=75
  r["parameters"]["nativeWallSeconds"]=time.monotonic()-native_started
  r["parameters"]["nativeExitCode"]=code;r["parameters"]["nativeHardBudgetStop"]=timed_out
  check(native_receipt.exists(),"native produced no complete prebasis/row checkpoint")
  nr=json.loads(native_receipt.read_text())
  check(nr.get("binding")==binding and nr.get("format")=="r150-original127-normal-forms-native-v2","native exact binding")
  r["parameters"]["nativeStatistics"]=nr
  st=(a.out/"nf-progress.bin").read_bytes()
  check(len(st)==120 and st[:8]==b"R15NS127" and st[8:72].decode()==binding and st[-8:]==b"ENDNS127",
        "complete committed-row checkpoint")
  ns,nt,nops,nf_size,op_size,text_size=struct.unpack_from("<IIQQQQ",st,72)
  check(ns==nr["completedSources"] and nt==nr["completedTargets"] and nops==nr["normalOperations"],
        "same committed native counters")
  for p,n in ((a.out/"nf-normal-forms.bin",nf_size),(a.out/"nf-reduction.bin",op_size),(a.out/"nf-normal-forms.sing",text_size)):
   check(p.stat().st_size>=n,"complete committed output prefix")
  r["parameters"]["wholeCommittedRows"]={"sources":ns,"targets":nt,"normalBytes":nf_size,"operationBytes":op_size,"textBytes":text_size}
  if code==0:
   check((ns,nt)==(remaining,9) and nr.get("status")=="completed" and nr.get("allOriginalRowsCompleted") is True,"complete all original normal forms")
   check(nr.get("prebasisRank")==3333 and nr.get("components")==1034 and nr.get("noOriginalSourceDropped") is True and nr.get("all6188NativeOriginalSourceIdentitiesVerified") is True,
         "original source module exactly represented")
   r["parameters"]["completeNormalFormAudit"]=inspect_complete_normal_forms(a.out/"nf-normal-forms.bin",binding,dictionary)
   r["status"]="completed";r["outcome"]="complete-original127-normal-forms";rc=0
  elif code==75:
   r["status"]="budget-checkpoint";r["outcome"]="original127-whole-row-prefix-retained";rc=75
  else:
   raise RuntimeError("native failed: "+log.read_bytes()[-3000:].decode(errors="replace"))
 except BaseException as e:
  r["status"]="failed";r["errorType"]=type(e).__name__;r["error"]=str(e);rc=1
 finally:
  r["parameters"]["temporaryFiles"]=[record(p) for p in paths if p.exists()]
  if native_receipt.exists():r["parameters"]["nativeReceipt"]=record(native_receipt)
  save()
 print(json.dumps({"status":r["status"],"outcome":r.get("outcome"),"elapsedSeconds":r["elapsedSeconds"],"error":r.get("error")}),flush=True)
 return rc
if __name__=="__main__":sys.exit(main())
