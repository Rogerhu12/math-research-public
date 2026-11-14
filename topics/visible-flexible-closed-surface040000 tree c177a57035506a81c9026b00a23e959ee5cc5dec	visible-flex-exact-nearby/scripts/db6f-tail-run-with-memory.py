#!/usr/bin/env python3
"""Record exit status and Linux child-process resource use for a math run.

Standard output and standard error are inherited. The command arguments are
not copied into this resource record; the mathematical producer records its
own reproducibility settings. This wrapper makes no mathematical assertion.
"""
import argparse
import hashlib
import json
from pathlib import Path
import resource
import subprocess
import sys
import time

ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument('--out', type=Path, required=True)
ap.add_argument('command', nargs=argparse.REMAINDER)
args = ap.parse_args()
command = args.command[1:] if args.command[:1] == ['--'] else args.command
if not command:
    raise ValueError('missing command')
if args.out.exists():
    raise ValueError('refusing to overwrite a resource record')
start = time.monotonic()
completed = subprocess.run(command, check=False)
usage = resource.getrusage(resource.RUSAGE_CHILDREN)
report = {
    'status': 'process-resource-record',
    'returnCode': completed.returncode,
    'elapsedSeconds': time.monotonic()-start,
    'userSeconds': usage.ru_utime,
    'systemSeconds': usage.ru_stime,
    'maximumResidentBytes': usage.ru_maxrss*1024,
    'maximumResidentUnitSource': 'Linux ru_maxrss in KiB',
    'wrapperSHA256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
args.out.write_text(json.dumps(report, indent=2)+'\n')
sys.exit(completed.returncode if completed.returncode >= 0 else 128-completed.returncode)
