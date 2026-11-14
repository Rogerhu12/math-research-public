#!/usr/bin/env python3
"""Run one explicitly recorded numerical job on the public rule-14 runner.

The plan is an argv array, not shell code. Only its five documented path
placeholders are expanded. Large scratch arrays stay outside the repository;
the requested OUT_DIR retains actual child outcomes and scientific outputs.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from string import Template
import subprocess
import sys
import tempfile
import time
import traceback
import root_20261114_ci_prepare as preparation


def now():
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--plan', type=Path)
    group.add_argument('--tail-radial', action='store_true')
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--steps', type=int, default=24)
    parser.add_argument('--angles', type=int, default=1024)
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[3]
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    work = Path(tempfile.mkdtemp(prefix='visible-larger-', dir=os.environ.get('RUNNER_TEMP')))
    status_file = out / 'driver-status.json'
    status = dict(scope=__doc__, started=now(), ended=None, phase='preparing',
                  work=str(work), out=str(out), child_returncode=None,
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    status_file.write_text(json.dumps(status, indent=2) + '\n')
    started = time.time()
    code = 1
    try:
        restored = preparation.prepare(repo, work, out / 'preparation.json',
                                       restore_a_raw=args.plan is not None)
        bindings = dict(PYTHON=sys.executable, RUNTIME_TOPIC=restored['runtime_topic'],
                        SOURCE_TOPIC=restored['source_topic'], OUT_DIR=str(out), WORK=str(work))
        if args.plan:
            content = args.plan.read_bytes()
            plan = json.loads(content)
            if not isinstance(plan['command'], list) or not all(isinstance(x, str) for x in plan['command']):
                raise TypeError('Plan command must be an argv array')
            command = [Template(x).substitute(bindings) for x in plan['command']]
            cwd = Template(plan['cwd']).substitute(bindings)
            status['plan'] = str(args.plan)
            status['plan_sha256'] = hashlib.sha256(content).hexdigest()
        else:
            command = [sys.executable, str(repo / 'topics/visible-flex-larger-amplitude/computations/exact_20261114_ci_radial_refinement.py'),
                       '--source-topic', restored['source_topic'], '--out', str(out),
                       '--steps', str(args.steps), '--angles', str(args.angles)]
            cwd = str(repo)
        status.update(phase='running', command=command, cwd=cwd)
        status_file.write_text(json.dumps(status, indent=2) + '\n')
        code = subprocess.run(command, cwd=cwd, check=False).returncode
        status.update(phase='finished', child_returncode=code)
    except BaseException as error:
        status.update(phase='failed', exception=repr(error), traceback=traceback.format_exc())
        print(status['traceback'], file=sys.stderr, flush=True)
    finally:
        status.update(ended=now(), seconds=time.time()-started)
        status_file.write_text(json.dumps(status, indent=2) + '\n')
        print(json.dumps(dict(event='driver-complete', phase=status['phase'],
                              child_returncode=status['child_returncode'], seconds=status['seconds'])), flush=True)
    return code


if __name__ == '__main__':
    raise SystemExit(main())
