#!/usr/bin/env python3
"""Execute one argv without a shell and record the actual child's return code."""
import argparse,datetime,json,subprocess,time,sys
from pathlib import Path
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--receipt',type=Path,required=True)
    ap.add_argument('command',nargs=argparse.REMAINDER);a=ap.parse_args()
    argv=a.command[1:] if a.command[:1]==['--'] else a.command
    if not argv:raise ValueError('A concrete command is required')
    if a.receipt.exists():raise FileExistsError(a.receipt)
    a.receipt.parent.mkdir(parents=True,exist_ok=True)
    start=time.monotonic();utc=datetime.datetime.now(datetime.timezone.utc).isoformat()
    result=subprocess.run(argv,shell=False)
    receipt=dict(schema='fd2d-observed-child-process-exit-v1',argv=argv,cwd=str(Path.cwd()),
        started_utc=utc,ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        seconds=time.monotonic()-start,actual_child_returncode=result.returncode,
        returncode_convention='Negative child returncode is an observed signal; wrapper returns 128+signal')
    a.receipt.write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(dict(event='actual_child_exit',receipt=str(a.receipt),returncode=result.returncode)),flush=True)
    return result.returncode if result.returncode>=0 else 128-result.returncode
if __name__=='__main__':raise SystemExit(main())
