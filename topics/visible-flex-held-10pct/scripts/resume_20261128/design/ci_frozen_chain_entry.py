#!/usr/bin/env python3
"""Build static inputs and execute the full chain from one frozen source tree.

The worker supplies an immutable detached sparse checkout and an unused sibling
computation directory.  Both the static 70-source recovery and every subsequent
numerical child therefore read this same pinned source, never the live control
checkout.  No field is uploaded or imported from a previous runner.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'work', 'outdir'):
        parser.add_argument('--'+name, type=Path, required=True)
    args = parser.parse_args()
    repo, work, out = (p.resolve() for p in (args.repo, args.work, args.outdir))
    if repo == work or repo in work.parents or work not in out.parents:
        raise ValueError('A frozen source tree and a separate owned computation directory are required')
    if work.exists():
        raise FileExistsError('Fresh runner input generation must not overwrite or repeat an existing computation directory')
    scripts = repo/'topics/visible-flex-held-10pct/scripts'
    setup = scripts/'resume_20261126/tail_recovery_setup.py'
    driver = scripts/'resume_20261128/design/ci_fresh_design.py'
    env = {key:value for key,value in os.environ.items()
           if not any(word in key.upper() for word in ('TOKEN', 'SECRET', 'PASSWORD'))}
    env['GITHUB_WORKSPACE'] = str(repo)
    env.pop('PYTHONPATH', None)
    for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
        env[key] = '2'
    command = [sys.executable, '-u', str(setup), '--repo', str(repo), '--work', str(work)]
    began = time.monotonic()
    log = work.with_name(work.name+'-frozen-source-setup.log')
    with log.open('x') as stream:
        process = subprocess.run(command, cwd=repo, env=env, stdout=stream,
                                 stderr=subprocess.STDOUT)
    record = dict(status='original_static_setup_returned', returncode=process.returncode,
        seconds=time.monotonic()-began, source_repository=str(repo),
        source_hashes={str(p):sha(p) for p in (Path(__file__).resolve(), setup, driver)},
        setup_command=command, setup_log_sha256=sha(log),
        actual_setup_record_sha256=sha(work/'recovery-setup.json')
            if (work/'recovery-setup.json').is_file() else None,
        BVP_started=False, arrays_imported=False, complete_surface=False)
    if work.is_dir():
        (work/'fresh-entry-setup.json').write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps(record), flush=True)
    if process.returncode:
        return process.returncode
    return subprocess.run([sys.executable, '-u', str(driver), '--repo', str(repo),
        '--work', str(work), '--outdir', str(out)], cwd=repo, env=env).returncode


if __name__ == '__main__':
    sys.exit(main())
