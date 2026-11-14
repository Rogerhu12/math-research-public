#!/usr/bin/env python3
"""Run one explicit research child and durably record its actual exit."""
import datetime,json,os,subprocess,sys,time
from pathlib import Path
if len(sys.argv)<5 or sys.argv[2]!="--":
 raise SystemExit("receipt.json -- command arguments")
receipt=Path(sys.argv[1]);command=sys.argv[3:]
if receipt.exists():raise SystemExit("Fresh receipt required")
receipt.parent.mkdir(parents=True,exist_ok=True)
log=receipt.with_suffix(".stdout.log")
if log.exists():raise SystemExit("Fresh stdout log required")
start=datetime.datetime.now(datetime.timezone.utc).isoformat();tick=time.monotonic()
with log.open("w") as stream:
 child=subprocess.Popen(command,stdout=stream,stderr=subprocess.STDOUT)
 launch={"schema":"fd2d-owned-math-child-exit-v1","command":command,"pid":child.pid,"startUTC":start,"stdoutLog":str(log),"completed":False,"exitCode":None}
 receipt.write_text(json.dumps(launch,indent=2)+"\n")
 rc=child.wait()
launch.update(completed=True,exitCode=rc,elapsedSeconds=time.monotonic()-tick,endUTC=datetime.datetime.now(datetime.timezone.utc).isoformat(),classification="natural_zero" if rc==0 else ("unknown_signal_termination" if rc<0 else "actual_nonzero_child_exit"))
temp=receipt.with_suffix(".tmp");temp.write_text(json.dumps(launch,indent=2)+"\n");temp.replace(receipt)
print(json.dumps(launch),flush=True)
sys.exit(rc if rc>=0 else 128-rc)
