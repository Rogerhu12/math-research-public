#!/usr/bin/env python3
"""Observe one explicitly recorded original command in its own owned session.

No equation or solver is wrapped. The child runs the exact command list in
the supplied record. PID/start-time/SID identity, live RSS samples and the
joined child's kernel rusage are recorded, including signal terminations.
The already checked owned-session helper cleans surviving descendants before
reaping the leader. No resource failure is classified as mathematical failure.
"""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import resource
import subprocess
import sys
import time

from owned_process_session import OwnedProcessSession


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--command-record', type=Path, required=True)
    parser.add_argument('--outdir', type=Path, required=True)
    args = parser.parse_args()
    record = json.loads(args.command_record.read_text())
    command = record['command']
    if not isinstance(command, list) or not command or not all(isinstance(x,str) for x in command):
        raise ValueError('Require one explicit original argv list')
    for filename, expected in record.get('source_hashes', {}).items():
        if sha(filename) != expected:
            raise ValueError('A bound execution source changed: '+filename)
    args.outdir.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    maximum_sampled_RSS, last_emit = 0, -100.
    owner = None
    sources = {str(path.resolve()):sha(path) for path in
        (Path(__file__), Path(__file__).with_name('owned_process_session.py'))}

    def event(kind, **fields):
        row = dict(event=kind, utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
            seconds=time.monotonic()-started, **fields)
        with (args.outdir/'events.jsonl').open('a') as stream:
            stream.write(json.dumps(row, allow_nan=False)+'\n')
        temporary = args.outdir/'latest.json.tmp'
        temporary.write_text(json.dumps(row, indent=2, allow_nan=False)+'\n')
        temporary.replace(args.outdir/'latest.json')
        if kind != 'live_original_process_sample':
            print(json.dumps(row, allow_nan=False), flush=True)

    try:
        with (args.outdir/'original.log').open('x') as output:
            child = subprocess.Popen(command, stdout=output, stderr=subprocess.STDOUT,
                start_new_session=True, env=dict(os.environ,
                    OPENBLAS_NUM_THREADS='2', OMP_NUM_THREADS='2', MKL_NUM_THREADS='2'))
            owner = OwnedProcessSession(child)
            event('actual_original_command_started', command=command,
                command_record=str(args.command_record.resolve()),
                command_record_sha256=sha(args.command_record),
                source_hashes=sources, actual_leader_identity=owner.leader,
                launcher_requested_threads=2, original_module_thread_settings_retained=True)
            while owner.poll_leader() is None:
                members = []
                for member in owner.members():
                    path = Path('/proc')/str(member['pid'])/'status'
                    try:
                        status = {line.split(':',1)[0]:line.split(':',1)[1].split()
                            for line in path.read_text().splitlines() if ':' in line}
                    except FileNotFoundError:
                        continue
                    row = dict(identity=member, **{name+'_bytes':int(status.get(name,['0'])[0])*1024
                        for name in ('VmRSS','RssAnon','RssFile','VmHWM')})
                    maximum_sampled_RSS = max(maximum_sampled_RSS, row['VmRSS_bytes'])
                    members.append(row)
                if time.monotonic()-started-last_emit >= 5.:
                    event('live_original_process_sample', members=members,
                        maximum_sampled_single_process_RSS_bytes=maximum_sampled_RSS,
                        sample_is_not_a_whole_process_peak=True)
                    last_emit = time.monotonic()-started
                time.sleep(.5)
            observed_code = owner.poll_leader()
            cleanup = owner.cleanup()
            owner = None
            usage = resource.getrusage(resource.RUSAGE_CHILDREN)
            event('actual_original_command_joined', actual_returncode=observed_code,
                owned_session_cleanup=cleanup,
                kernel_joined_children_maxRSS_KiB=usage.ru_maxrss,
                kernel_joined_children_user_seconds=usage.ru_utime,
                kernel_joined_children_system_seconds=usage.ru_stime,
                maximum_sampled_single_process_RSS_bytes=maximum_sampled_RSS,
                one_numerical_leader_launched=True, mathematical_failure_inferred=False)
            return observed_code
    finally:
        if owner is not None and not owner.reaped:
            event('observer_exception_or_interruption_cleanup', cleanup=owner.cleanup(),
                  mathematical_failure_inferred=False)


if __name__ == '__main__':
    sys.exit(main())
