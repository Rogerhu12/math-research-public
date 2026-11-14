#!/usr/bin/env python3
"""Owned execution wrapper for the new node-only tail readout.
It does not run any old recovery stage, git command, or numerical solver itself.
Only a real os.wait4 result may create the final resource record.
"""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import signal
import sys
import time

def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def atomic_new(file, obj):
    raw=(json.dumps(obj, indent=2, sort_keys=True)+"\n").encode()
    fd=os.open(file, os.O_WRONLY|os.O_CREAT|os.O_EXCL, 0o644)
    try:
        with os.fdopen(fd,"wb") as f:
            f.write(raw);f.flush();os.fsync(f.fileno())
    except BaseException:
        raise

def replace(file, obj):
    temp=Path(str(file)+".tmp-"+str(os.getpid()))
    raw=(json.dumps(obj, indent=2, sort_keys=True)+"\n").encode()
    with temp.open("wb") as f:
        f.write(raw);f.flush();os.fsync(f.fileno())
    os.replace(temp,file)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--prefix",type=Path,required=True)
    p.add_argument("--timeout-seconds",type=float,required=True)
    p.add_argument("--rss-limit-kib",type=int,required=True)
    p.add_argument("command",nargs=argparse.REMAINDER)
    a=p.parse_args()
    cmd=a.command[1:] if a.command[:1]==["--"] else a.command
    if not cmd or a.timeout_seconds<=0 or a.rss_limit_kib<=0:
        p.error("positive resource limits and a command are required")
    prefix=a.prefix.resolve()
    prefix.parent.mkdir(parents=True,exist_ok=True)
    log=Path(str(prefix)+".log")
    resource=Path(str(prefix)+"-resource.json")
    heartbeat=Path(str(prefix)+"-heartbeat.json")
    intent=Path(str(prefix)+"-intent.json")
    for x in [log,resource,heartbeat,intent]:
        if x.exists():raise FileExistsError(x)
    begin=time.monotonic()
    common=dict(schema="new-A-tail-readout-owned-v1",command=cmd,started_utc=utc(),
                wrapper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                timeout_seconds=a.timeout_seconds,rss_limit_kib=a.rss_limit_kib,
                numerical_scope="New finite Cartesian node readout; no old recovery stage.")
    atomic_new(intent,dict(common,wait4_observed=False,exitcode=None))
    fd=os.open(log,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o644)
    pid=os.fork()
    if pid==0:
        try:
            os.setsid()
            os.dup2(fd,1);os.dup2(fd,2);os.close(fd)
            os.execvpe(cmd[0],cmd,os.environ)
        except BaseException as exc:
            print("owned child exec failed: "+repr(exc),file=sys.stderr,flush=True)
            os._exit(127)
    os.close(fd)
    received=[]
    def stop(signum,frame):
        received.append(dict(signal=signum,utc=utc()))
        try:os.kill(pid,signal.SIGTERM)
        except ProcessLookupError:pass
    for sig in [signal.SIGTERM,signal.SIGINT,signal.SIGHUP]:
        signal.signal(sig,stop)
    reason=None;sent_at=None;hwm=0;lastbeat=-100
    while True:
        got,status,usage=os.wait4(pid,os.WNOHANG)
        if got:break
        now=time.monotonic()
        try:
            lines=Path("/proc/"+str(pid)+"/status").read_text().splitlines()
            for line in lines:
                if line.startswith("VmHWM:"):
                    hwm=max(hwm,int(line.split()[1]))
        except (FileNotFoundError,ProcessLookupError):
            pass
        if reason is None:
            if hwm>a.rss_limit_kib:reason="declared_rss_limit"
            elif now-begin>a.timeout_seconds:reason="declared_timeout"
            elif received:reason="received_supervisor_signal"
            if reason is not None:
                sent_at=now
                try:os.kill(pid,signal.SIGTERM)
                except ProcessLookupError:pass
        elif sent_at is not None and now-sent_at>10:
            try:os.kill(pid,signal.SIGKILL)
            except ProcessLookupError:pass
        if now-lastbeat>=5:
            replace(heartbeat,dict(common,pid=pid,utc=utc(),wall_seconds=now-begin,
                observed_hwm_kib=hwm,wait4_observed=False,exitcode=None,
                limit_reason=reason,received_supervisor_signals=received))
            lastbeat=now
        time.sleep(.2)
    exitcode=os.waitstatus_to_exitcode(status)
    row=dict(common,finished_utc=utc(),wall_seconds=time.monotonic()-begin,
             wait4_observed=True,wait_status=status,exitcode=exitcode,
             termination_signal=-exitcode if exitcode<0 else None,
             peak_rss_kib=usage.ru_maxrss,user_seconds=usage.ru_utime,
             system_seconds=usage.ru_stime,supervisor_limit_reason=reason,
             received_supervisor_signals=received,
             source_preparation_is_not_numerical_success=True)
    atomic_new(resource,row)
    print(json.dumps(dict(resource=str(resource),exitcode=exitcode,
                         wait4_observed=True,peak_rss_kib=usage.ru_maxrss)),flush=True)
    return 0 if exitcode==0 else 1

if __name__=="__main__":
    raise SystemExit(main())
