#!/usr/bin/env python3
"""Portable natural subprocess receipt, including expected source failures."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import resource
import subprocess
import time

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--prefix',type=Path,required=True)
    parser.add_argument('--expected-returncode',type=int,default=0)
    parser.add_argument('command',nargs=argparse.REMAINDER)
    args=parser.parse_args()
    command=args.command[1:] if args.command[:1]==['--'] else args.command
    if not command:raise ValueError('An explicit actual command is required')
    log=Path(str(args.prefix)+'.log');receipt=Path(str(args.prefix)+'-exit.json')
    if log.exists() or receipt.exists():raise FileExistsError('Fresh receipt prefix required')
    start=time.monotonic()
    with log.open('x') as output:
        process=subprocess.Popen(command,stdout=output,stderr=subprocess.STDOUT)
        code=process.wait()
    result=dict(returncode=code,seconds=time.monotonic()-start,
        peakChildRSSKiB=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
        command=command,naturalExit=(code>=0),signalNumber=(-code if code<0 else None),
        expectedReturncode=args.expected_returncode)
    receipt.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result),flush=True)
    if code!=args.expected_returncode:raise SystemExit('Unexpected actual return code: '+str(code))

if __name__=='__main__':main()
