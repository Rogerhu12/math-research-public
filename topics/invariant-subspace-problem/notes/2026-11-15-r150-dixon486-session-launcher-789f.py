#!/usr/bin/env python3
"""Place pinned headers in temporary scopes, then run the actual p486 continuation.
Only a small source/parameter/run/hash summary leaves this temporary job.
"""
import ast,hashlib,json,pathlib,shutil,subprocess,sys,time,traceback
src=pathlib.Path(__file__).resolve().parent
args=sys.argv[1:]
def arg(name):
 return pathlib.Path(args[args.index(name)+1])
out=arg("--out")
target=out.parent/"dixon-after486-session-small-summary.json"
result={"status":"setup-running","largeDataPersistenceAllowed":False}
try:
 runner=src/"2026-11-15-r150-selected-infinity-dixon-resume486-runner-789f.py"
 ast.parse(runner.read_text())
 bit=src/"2026-11-14-r150-f31-bitplane-789f.hpp"
 data=bit.read_bytes()
 if hashlib.sha256(data).hexdigest()!="73d113f207c718b230162c786dfc8d367c5113193ed5fe590166af414c6fe8ec":
  raise ValueError("bitplane source identity")
 destination=arg("--repo-notes")/bit.name
 destination.write_bytes(data)
 if not pathlib.Path("/usr/include/gmpxx.h").is_file():
  for command in (["sudo","apt-get","update","-qq"],["sudo","apt-get","install","-y","-qq","libgmp-dev"]):
   p=subprocess.run(command,capture_output=True,text=True,timeout=120)
   if p.returncode:raise RuntimeError("GMP dependency setup: "+p.stderr[-1500:])
 began=time.monotonic()
 p=subprocess.run([sys.executable,"-B",str(runner),*args],check=False)
 raw=(out/"selected-infinity-dixon-after486-small-summary.json").read_bytes()
 original=json.loads(raw)
 result={k:v for k,v in original.items() if isinstance(v,(str,int,float,bool)) or v is None}
 result["parameters"]={k:original[k] for k in ("compile","inputs","sources","fullTemporaryReceipt","checkpoints","nativeStageSummaries","exactKernelSummary","rationalAttemptStatusCounts") if k in original}
 for k in ("characteristicZeroSelectedRankBounds","characteristicZeroSelectedColumnsFull4367RankBounds"):
  if k in original:result[k]=original[k]
 result.update(nativeRunnerExitCode=p.returncode,runnerWallSeconds=time.monotonic()-began,
               originalSmallSummaryBytes=len(raw),originalSmallSummarySHA256=hashlib.sha256(raw).hexdigest(),
               launcherSHA256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest())
 if p.returncode not in (0,75):
  for name in ("compile.log","exception.log"):
   path=out/name
   if path.exists():result[name.replace(".","_")+"_tail"]=path.read_text(errors="replace")[-3000:]
except Exception as e:
 result.update(status="setup-or-run-failed",errorType=type(e).__name__,error=str(e),traceback=traceback.format_exc()[-2000:])
target.parent.mkdir(parents=True,exist_ok=True)
data=(json.dumps(result,ensure_ascii=False,indent=2)+"\n").encode()
if len(data)>=99000:raise RuntimeError("small execution summary exceeds bound")
target.write_bytes(data)
print(json.dumps({"status":result.get("status"),"completedExponent":result.get("completedExponent"),
 "exactFull4367RationalKernelCount":result.get("exactFull4367RationalKernelCount"),
 "summarySHA256":hashlib.sha256(data).hexdigest(),"largeDataUploaded":False}),flush=True)
