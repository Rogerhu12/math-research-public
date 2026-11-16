#!/usr/bin/env python3
"""Observe one frozen exact-low20 child; retain real heartbeats and termination.

Author: Astra-ISP-789f / normal_annihilator, with /root.
AI-assisted: GPT-6 Astra Pro.  Date: 2026-11-16.
No mathematical file is changed.  Only this child's own process group may be
terminated, and only after the explicitly requested outer wall-time deadline.
Heartbeat RSS is sampled; final child ru_maxrss is reported separately.
"""
import argparse,datetime,hashlib,json,os,resource,signal,subprocess,sys,time
from pathlib import Path

FORMAT="r150-exact-low20-observed-execution-v1"

def utc(): return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="microseconds")
def canon(x): return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")
def identity(p):
    p=Path(p);h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1048576),b""):h.update(b)
    return {"path":p.name,"bytes":p.stat().st_size,"sha256":h.hexdigest()}
def atomic(p,x):
    p=Path(p);q=p.with_name(p.name+".tmp");q.write_bytes(canon(x));os.replace(q,p)
def status(pid):
    result={"procStatusAvailable":False}
    try:
        for line in Path("/proc/%d/status"%pid).read_text().splitlines():
            k,_,v=line.partition(":")
            if k in ("VmRSS","VmHWM","VmSize","VmPeak"):
                z=v.split();result[k+"KiB"]=int(z[0])
            elif k=="State":result["state"]=v.strip()
        result["procStatusAvailable"]=True
    except (OSError,ValueError):pass
    try:
        for line in Path("/proc/meminfo").read_text().splitlines():
            k,_,v=line.partition(":")
            if k in ("MemAvailable","MemFree","SwapTotal","SwapFree"):
                result[k+"KiB"]=int(v.split()[0])
    except (OSError,ValueError):pass
    return result

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--outer-seconds",type=float,required=True)
    ap.add_argument("--heartbeat-seconds",type=float,default=10)
    ap.add_argument("--stdout",type=Path,required=True)
    ap.add_argument("--heartbeats",type=Path,required=True)
    ap.add_argument("--identity",type=Path,required=True)
    ap.add_argument("command",nargs=argparse.REMAINDER)
    a=ap.parse_args();cmd=a.command[1:] if a.command[:1]==["--"] else a.command
    if not cmd or not 0<a.outer_seconds<=1200 or not 1<=a.heartbeat_seconds<=10:
        raise ValueError("bounded real child command and observation interval required")
    paths=[a.stdout,a.heartbeats,a.identity]
    if len({str(p.resolve()) for p in paths})!=3 or any(p.exists() for p in paths):
        raise ValueError("all three observation paths must be distinct and new")
    for p in paths:p.parent.mkdir(parents=True,exist_ok=True)
    source=Path(cmd[1]) if len(cmd)>1 else None
    rec={"format":FORMAT,"observer":identity(Path(__file__)),"command":cmd,"cwd":str(Path.cwd()),
         "outerSeconds":a.outer_seconds,"heartbeatSeconds":a.heartbeat_seconds,"startedAtUTC":utc(),
         "source":identity(source) if source is not None and source.is_file() else None,
         "status":"running","terminationRequestedByObserver":False}
    atomic(a.identity,rec)
    start=time.monotonic();deadline=start+a.outer_seconds;next_beat=start;terminate_at=None;beats=0;sample_peak=0
    with a.stdout.open("xb",buffering=0) as log, a.heartbeats.open("xb",buffering=0) as heart:
        try:process=subprocess.Popen(cmd,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
        except BaseException as e:
            rec.update({"status":"launch-failed","finishedAtUTC":utc(),"elapsedSeconds":time.monotonic()-start,
                        "error":{"type":type(e).__name__,"message":str(e)}})
            atomic(a.identity,rec);print(json.dumps(rec,separators=(",",":")),flush=True);return 1
        rec["childPid"]=process.pid;atomic(a.identity,rec)
        while True:
            now=time.monotonic();rc=process.poll()
            if now>=next_beat or rc is not None:
                observation={"utc":utc(),"elapsedSeconds":now-start,"childPid":process.pid,
                             "returnCode":rc,"stdoutBytes":a.stdout.stat().st_size,**status(process.pid)}
                sample_peak=max(sample_peak,observation.get("VmRSSKiB",0));beats+=1
                heart.write(canon(observation)+b"\n");os.fsync(heart.fileno())
                print(json.dumps(observation,separators=(",",":")),flush=True)
                next_beat=now+a.heartbeat_seconds
            if rc is not None:break
            if now>=deadline and terminate_at is None:
                rec["terminationRequestedByObserver"]=True;rec["terminationRequestedAtUTC"]=utc()
                rec["terminationReason"]="explicit outer wall-time deadline"
                atomic(a.identity,rec)
                try:os.killpg(process.pid,signal.SIGTERM)
                except ProcessLookupError:pass
                terminate_at=now
            elif terminate_at is not None and now>=terminate_at+3:
                try:os.killpg(process.pid,signal.SIGKILL)
                except ProcessLookupError:pass
            time.sleep(min(0.5,max(0.01,next_beat-time.monotonic())))
        rc=process.wait()
    end=time.monotonic()
    rec.update({"status":"completed" if rc==0 else "child-nonzero","finishedAtUTC":utc(),
       "elapsedSeconds":end-start,"childReturnCode":rc,"shellEquivalentExitCode":rc if rc>=0 else 128-rc,
       "heartbeats":identity(a.heartbeats),"heartbeatCount":beats,"stdout":identity(a.stdout),
       "sampledPeakVmRSSKiB":sample_peak,"waitedChildRuMaxrssKiB":resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
       "unobservedTerminationCauseInferred":False})
    atomic(a.identity,rec);print(json.dumps(rec,separators=(",",":")),flush=True)
    return rc if rc>=0 else 128-rc

if __name__=="__main__":raise SystemExit(main())
