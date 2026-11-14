#!/usr/bin/env python3
"""Run one owned numerical command and record wait4 resource/exit status.

This is a small replacement for /usr/bin/time, absent in this environment.
Usage: strong_resource_run.py --out resource.json -- python ...
The child inherits ordinary stdin/stdout/stderr; no solver behavior changes.
"""
import argparse,json,os,time,sys,hashlib
from pathlib import Path

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('command',nargs=argparse.REMAINDER)
    args=parser.parse_args()
    command=args.command[1:] if args.command[:1]==['--'] else args.command
    if not command:parser.error('A command is required')
    source_hash=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    started=time.time();pid=os.fork()
    if pid==0:
        try:os.execvp(command[0],command)
        except OSError as error:
            print(repr(error),file=sys.stderr,flush=True);os._exit(127)
    _,status,usage=os.wait4(pid,0)
    code=os.waitstatus_to_exitcode(status)
    report=dict(scope=__doc__,command=command,wall_seconds=time.time()-started,
                exitcode=code,termination_signal=-code if code<0 else None,
                peak_rss_kib=usage.ru_maxrss,user_seconds=usage.ru_utime,
                system_seconds=usage.ru_stime,resource_wrapper_sha256=source_hash)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(event='child_exit',**report)),flush=True)
    raise SystemExit(code if code>=0 else 128-code)

if __name__=='__main__':main()
