#!/usr/bin/env python3
"""Serialization-only continuation of the frozen same-I/J natural-u solver.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
Imports the exact paid runner. Its __file__, source hashes, mathematics, native
state and checkpoint binding are unchanged. Only one redundant JSON field is
omitted from a shallow serialization copy of the main result.
"""
import argparse,hashlib,importlib.util,json,pathlib,sys,time,traceback
sys.dont_write_bytecode=True
RUNNER_BYTES=21664
RUNNER_SHA="80f6815133250cf559f81afb557f138952f7268ce2d2b43e2c15bfb822775e67"
BINDING="1fdb07aa85a565c45d7adfe04721a29cdbe6911cc0cb50ca45044c51f88ccc01"
FIRST_RECEIPT=(98033,"93fe8e62a883cdecc51d1185f162648d1f439e355eb646f3999669c419a0e4df")
def ident(p):
 b=pathlib.Path(p).read_bytes();return {"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest()}
def need(x,s):
 if not x:raise ValueError(s)
def main(argv=None):
 ap=argparse.ArgumentParser()
 ap.add_argument("--runner",required=True,type=pathlib.Path)
 a,rest=ap.parse_known_args(argv)
 if rest and rest[0]=="--":rest=rest[1:]
 need(rest.count("--out")==1 and rest.count("--maximum-degree")==1,"explicit one output and degree")
 out=pathlib.Path(rest[rest.index("--out")+1]).resolve()
 goal=int(rest[rest.index("--maximum-degree")+1]);need(8<goal<=32,"strict continuation after paid8, finite degree")
 old=a.runner.resolve();need(ident(old)=={"bytes":RUNNER_BYTES,"sha256":RUNNER_SHA},"exact frozen mathematical runner SHA")
 ledger=out/"natural-ledger.txt";rp=out/"selected-natural-u-schur-pipeline-receipt.json"
 lb,ln=ledger.read_text().split();initial=int(ln)
 need(lb==BINDING and 8<=initial<=goal,"actual same original source checkpoint")
 initial_receipt=json.loads(rp.read_text())
 initial_parameters=initial_receipt.get("parameters",{})
 need(initial_parameters.get("binding",initial_parameters.get("serializationOnlyContinuation",{}).get("mathematicalBinding"))==BINDING,"same original pipeline binding")
 if initial==8:
  need(ident(rp)=={"bytes":FIRST_RECEIPT[0],"sha256":FIRST_RECEIPT[1]} or
       initial_receipt["parameters"].get("serializationOnlyContinuation",{}).get("frozenRunnerSHA256")==RUNNER_SHA,
       "paid8 receipt or same serialization continuation")
 meta={"wrapper":pathlib.Path(__file__).name,"wrapperIdentity":ident(__file__),
   "frozenRunnerSHA256":RUNNER_SHA,"mathematicalBinding":BINDING,
   "actualInitialCompleteDegree":initial,"requestedMaximumDegree":goal,
   "omittedRedundantSerializedField":"nativeStatistics.unitOriginalOutputIndices",
   "inMemoryNativeStatisticsUnchanged":True,"mathematicalRunnerSourceUnchanged":True}
 spec=importlib.util.spec_from_file_location("same_original_u_frozen",old)
 module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
 original_save=module.jsave;counts={"mainReceiptCopies":0,"omittedUnitIndexEntries":0}
 def compact_save(path,value):
  if pathlib.Path(path).name==rp.name and isinstance(value,dict):
   copied=dict(value)
   if isinstance(value.get("nativeStatistics"),dict):
    stats=dict(value["nativeStatistics"])
    unit=stats.pop("unitOriginalOutputIndices",None)
    if unit is not None:
     need(len(unit)==4318 and len(set(unit))==4318,"actual duplicate unit-output dictionary")
     counts["omittedUnitIndexEntries"]+=len(unit)
    copied["nativeStatistics"]=stats
   params=dict(value.get("parameters",{}));params["serializationOnlyContinuation"]=meta
   copied["parameters"]=params
   counts["mainReceiptCopies"]+=1
   original_save(path,copied)
  else:original_save(path,value)
 module.jsave=compact_save
 start=time.monotonic();code=1;error=None
 try:code=module.main(rest)
 except Exception as e:
  error=str(e);(out/"serialization-continuation-exception.log").write_text(traceback.format_exc());code=1
 finally:
  result=json.loads(rp.read_text()) if rp.exists() else {}
  if result.get("parameters",{}).get("binding"):
   need(result["parameters"]["binding"]==BINDING,"actual continuation must keep the old mathematical binding")
  wrapper_receipt={"format":"isp-serialization-only-original-u-continuation-v1",
    "status":result.get("status","failed"),"exitCode":code,"error":error,
    "wallSeconds":time.monotonic()-start,"parameters":{**meta,"serializationCounts":counts,
       "actualPipelineReceipt":ident(rp) if rp.exists() else None,
       "actualCompletedDegree":result.get("completedNaturalDegree",result.get("parameters",{}).get("actualLastCompleteNativeDegree")),
       "compileReused":result.get("compile",{}).get("reused",False)},
    "largeDataUploadedOrCommitted":False}
  original_save(out/"selected-natural-u-schur-serialization-continuation-receipt.json",wrapper_receipt)
  print(json.dumps(wrapper_receipt),flush=True)
 return code
if __name__=="__main__":sys.exit(main())
