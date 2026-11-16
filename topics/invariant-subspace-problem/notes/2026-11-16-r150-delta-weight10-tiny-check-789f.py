#!/usr/bin/env python3
"""Reproducible tiny checks only; never reads or prepares the original200.

Author: Astra-ISP-789f / literature_audit, with /root.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.
The output is a temporary execution receipt, not a repository artifact.
"""
from pathlib import Path
import argparse,ast,hashlib,importlib.util,json,sys,tempfile,time

PINS={
 "2026-11-16-r150-shifted-module-weight10-verifier127-789f.py":(13935,"54b082184273e254495be8e1eb788e6569e8ca9cc4b83a1a5d4330304e9d4246"),
 "2026-11-16-r150-original-delta-weight10-homogeneous127-789f.py":(40012,"09d8f5a04cf39ebee0613af1c056000d129b17d5aca60ebdd784860c035e36f3")}
def need(ok,message):
 if not ok:raise ValueError(message)
def identity(p):
 b=p.read_bytes();return {"path":p.name,"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest()}
def load(root,name):
 p=root/name;d=identity(p);need((d["bytes"],d["sha256"])==PINS[name],"same frozen tiny-test source")
 ast.parse(p.read_bytes(),filename=name)
 spec=importlib.util.spec_from_file_location(name.replace("-","_"),p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
 return m,{**d,"astParsed":True}
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--directory",type=Path,required=True);ap.add_argument("--receipt",type=Path,required=True);a=ap.parse_args()
 start=time.monotonic();need(sys.version_info[:3]==(3,12,14),"same Python3.12.14 runtime")
 v,vi=load(a.directory,list(PINS)[0]);d,di=load(a.directory,list(PINS)[1])
 need(d.one(["@@TEST 1","@@TEST 10"],"@@TEST 1")=="@@TEST 1","exact numeric marker")
 need(d.one(["@@TEST 10"],"@@TEST 1",False) is None,"no numeric marker prefix collision")
 checks=v.selftest()
 with tempfile.TemporaryDirectory(prefix="r150-weight10-tiny-",dir=a.directory) as td:
  td=Path(td);binding="a"*64;e=[0]*12;e[0]=1;terms=[(v.position(0,tuple(e)),3)]
  desc=v.write_vector(td/"tiny.bin.gz",terms,1,binding)
  need(v.read_vector(td/"tiny.bin.gz",desc,binding)==tuple(terms),"whole tiny binary roundtrip")
  paths=[]
  for i in range(10):
   p=td/("c%d.txt"%i);p.write_text("y0^2" if i==0 else "zz^2" if i==1 else "0");paths.append(p)
  vv,ww=v.shifted_text_vector(paths);need(ww==2 and len(vv)==2,"literal correct shifted coordinates")
  paths[1].write_text("zz^3")
  try:v.shifted_text_vector(paths)
  except ValueError:checks["wrongRowShiftRejected"]=True
  else:raise ValueError("wrong row shift was accepted")
 checks.update(numericMarkerDisambiguation=True,wholeBinaryRoundtrip=True)
 result={"format":"r150-delta-weight10-frozen-tiny-validation-v1","status":"completed","source":identity(Path(__file__)),"elapsedSeconds":time.monotonic()-start,"sources":[vi,di],"checks":checks,
  "realOriginal200Prepared":False,"realOriginal200CandidateRun":False,"mathematicalConclusionAboutDelta":False}
 raw=json.dumps(result,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")
 a.receipt.parent.mkdir(parents=True,exist_ok=True);a.receipt.write_bytes(raw)
 print(json.dumps({"receipt":identity(a.receipt),"status":result["status"],"elapsedSeconds":result["elapsedSeconds"],"tinyGatesPassed":len(checks),"realOriginal200Run":False},sort_keys=True))
 return 0
if __name__=="__main__":raise SystemExit(main())
