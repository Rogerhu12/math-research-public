#!/usr/bin/env python3
"""Compile and test the three frozen weight10 C++ files, without any200 parent.
Author: Astra-ISP-789f / literature_audit, with /root.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.
Only code, parameters and execution/output identities may be published.
"""
from __future__ import annotations
import argparse,hashlib,json,os,resource,shutil,signal,subprocess,sys,time
from pathlib import Path
FORMAT="r150-original-weight10-full-macaulay127-controls-v1"
NATIVE_FORMAT="r150-original-weight10-full-macaulay127-native-v1"
CHECKER_FORMAT="r150-original-weight10-full-ordinary-verifier127-v1"
PINS={
 "native_source":"0a53cd6179904977404db186dbc88bf1a04339c2bf4569b90a9007744f0a50df",
 "checker_source":"bf10b7ba832123c6208e8e7b4cf2a6e63ba1cfbd2f17cbf6d26e4f4c8a53f295",
 "bitplane_header":"03272796bb20c883291d27c9a0b796197f8295ccd9b16552c13894657dc8afd3"}
HEADER_NAME="2026-11-15-r150-original-f127-bitplane-789f.hpp"
FLAGS=["-O3","-std=c++17","-DNDEBUG","-Wall","-Wextra"]
def need(v,s):
 if not v:raise ValueError(s)
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")
def sha(b):return hashlib.sha256(b).hexdigest()
def identity(p):
 p=Path(p);h=hashlib.sha256()
 with p.open("rb") as f:
  for q in iter(lambda:f.read(1048576),b""):h.update(q)
 return {"path":p.name,"bytes":p.stat().st_size,"sha256":h.hexdigest()}
def exact(p,d):
 z=identity(p);need(z["bytes"]==d["bytes"] and z["sha256"]==d["sha256"],"whole controls file "+Path(p).name);return z
def atomic(p,b):
 p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);tmp=p.with_name(p.name+".tmp")
 with tmp.open("wb") as f:f.write(b);f.flush();os.fsync(f.fileno())
 os.replace(tmp,p)
def save_json(p,x):atomic(p,canon(x));return identity(p)
def execute(a):
 begun=time.monotonic();deadline=begun+a.seconds;a.out.mkdir(parents=True,exist_ok=True)
 own=identity(Path(__file__));mp=a.out/"full-weight10-controls-manifest.json";rp=a.out/"full-weight10-controls-receipt.json"
 state=None;code=1;new_units=0;child=None
 rec={"format":FORMAT,"source":own,"status":"running","parameters":{"seconds":a.seconds,"memoryMiB":a.memory_mib,
      "original200ParentRead":False,"fullOriginalMatrixGenerated":False,"stages":[]}}
 def flush():
  if state is not None:save_json(mp,state)
 def run(label,argv,limit):
  nonlocal child
  need(deadline-time.monotonic()>10,"actual remaining controls budget")
  state["generation"]+=1;flush()
  log=a.out/("%04d-%s.log"%(state["generation"],label));start=time.monotonic()
  with log.open("wb") as f:
   child=subprocess.Popen(list(map(str,argv)),stdout=f,stderr=subprocess.STDOUT,start_new_session=True)
   try:rc=child.wait(timeout=max(1,min(limit,deadline-time.monotonic()-5)))
   except subprocess.TimeoutExpired:
    os.killpg(child.pid,signal.SIGTERM)
    try:child.wait(timeout=3)
    except subprocess.TimeoutExpired:os.killpg(child.pid,signal.SIGKILL);child.wait()
    raise TimeoutError("actual "+label+" controls exceeded its bound")
  child=None
  item={"name":label,"arguments":list(map(str,argv)),"exitCode":rc,"elapsedSeconds":time.monotonic()-start,"log":identity(log)}
  rec["parameters"]["stages"].append(item)
  need(rc==0,"actual completed controls process "+label);return log,item
 try:
  need(tuple(sys.version_info[:3])==(3,12,14),"pinned Python3.12.14 controls runtime")
  for k,h in PINS.items():need(identity(getattr(a,k))["sha256"]==h,"exact controls source "+k)
  sem={"format":FORMAT,"source":own,"prime":127,"sourceSHA256":PINS,"compilerFlags":FLAGS,
       "original200ParentRead":False,"fullOriginalMatrixGenerated":False}
  binding=sha(canon(sem));rec["binding"]=binding
  state={"format":FORMAT+"-manifest","binding":binding,"semantic":sem,"generation":0}
  if mp.exists():
   state=json.loads(mp.read_bytes())
   need(state["format"]==FORMAT+"-manifest" and state["binding"]==binding and state["semantic"]==sem,"same exact controls continuation")
  flush();build=a.out/"build";build.mkdir(exist_ok=True)
  if "compiled" not in state:
   compiler=shutil.which(a.cxx) if not Path(a.cxx).is_file() else str(a.cxx)
   need(compiler is not None,"actual C++17 compiler")
   vp=subprocess.run([compiler,"--version"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=10)
   need(vp.returncode==0,"actual compiler version")
   for src,name in ((a.native_source,"native.cpp"),(a.checker_source,"checker.cpp"),(a.bitplane_header,HEADER_NAME)):
    atomic(build/name,src.read_bytes())
   for label in ("native","checker"):
    run("compile-"+label,[compiler,*FLAGS,build/(label+".cpp"),"-I",build,"-o",a.out/(label+".bin")],90)
   state["compiled"]={"native":identity(a.out/"native.bin"),"checker":identity(a.out/"checker.bin"),
        "compiler":{"path":str(compiler),"versionFirstLine":vp.stdout.decode(errors="replace").splitlines()[0],"versionSHA256":sha(vp.stdout)},"flags":FLAGS}
   new_units+=1;flush()
  for label in ("native","checker"):exact(a.out/state["compiled"][label]["path"],state["compiled"][label])
  if "controls" not in state:
   td=a.out/("native-tiny-%04d"%(state["generation"]+1))
   log,item=run("native-controls",[a.out/"native.bin","--selftest",td],45);q=json.loads(log.read_bytes().splitlines()[-1])
   need(q["format"]==NATIVE_FORMAT+"-selftest" and q["allComplete"] and q["checkpointRoundtrip"] and
        q["oldExhaustiveChecks"]==244990 and q["signedScalarChecks"]==2048256 and q["tinyOriginalProducts"]==43,
        "every actual native arithmetic/DAG/checkpoint/source/left control")
   log2,item2=run("ordinary-controls",[a.out/"checker.bin","--selftest"],30);qq=json.loads(log2.read_bytes().splitlines()[-1])
   need(qq["format"]==CHECKER_FORMAT+"-selftest" and qq["allComplete"] and qq["ordinaryChecks"]==93412,
        "every independent ordinary/dictionary control")
   state["controls"]={"native":q,"nativeLog":identity(log),"ordinary":qq,"ordinaryLog":identity(log2)}
   new_units+=1;flush()
  for key in ("nativeLog","ordinaryLog"):exact(a.out/state["controls"][key]["path"],state["controls"][key])
  rec["status"]="completed"
  rec["parameters"].update(compiled=state["compiled"],controls=state["controls"],
       allFrozenCppCompiled=True,allNewNativeAndIndependentControlsVerified=True)
  code=0;return code
 except BaseException as e:
  rec["status"]="memory-error" if isinstance(e,MemoryError) else "failed"
  rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};code=1;return code
 finally:
  if child is not None and child.poll() is None:
   os.killpg(child.pid,signal.SIGTERM)
   try:child.wait(timeout=3)
   except subprocess.TimeoutExpired:os.killpg(child.pid,signal.SIGKILL);child.wait()
  flush();rec["elapsedSeconds"]=time.monotonic()-begun
  rec["parameters"].update(newCompleteUnitsThisRun=new_units,continuationEligible=False,
       parentPeakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,childPeakRssKiB=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss)
  if state is not None:rec["parameters"]["manifest"]=identity(mp)
  save_json(rp,rec);print(canon(rec).decode(),flush=True)
def main():
 ap=argparse.ArgumentParser()
 for k in tuple(PINS)+("out",):ap.add_argument("--"+k.replace("_","-"),type=Path,required=True)
 ap.add_argument("--seconds",type=float,default=120);ap.add_argument("--memory-mib",type=int,default=1024)
 ap.add_argument("--cxx",default="g++")
 a=ap.parse_args();need(30<=a.seconds<=300 and 256<=a.memory_mib<=2048,"bounded independent controls")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2);return execute(a)
if __name__=="__main__":raise SystemExit(main())
