#!/usr/bin/env python3
"""Observe one original command with an owner-internal termination request.

Independent successor of observe_owned_original_command_v2. An explicit, matched
JSON request is read inside the live owner loop. It invokes the existing owned
session cleanup, records its actual return, and exits 4 normally. This provides
a verifiable engineering handoff without relying on tool-level TTY Control-C.

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
import actual_process_memory_limits as actual_limits


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--command-record', type=Path, required=True)
    parser.add_argument('--outdir', type=Path, required=True)
    parser.add_argument('--termination-request', type=Path)
    parser.add_argument('--control-nonce')
    args = parser.parse_args()
    if (args.termination_request is None) != (args.control_nonce is None):
        raise ValueError('The termination path and explicit nonce must be supplied together')
    if args.control_nonce is not None and not (8 <= len(args.control_nonce) <= 128):
        raise ValueError('The control nonce must have 8 to 128 characters')
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
    first_limits = {}
    observer_initial_limits = actual_limits.snapshot()
    sources = {str(path.resolve()):sha(path) for path in
        (Path(__file__), Path(__file__).with_name('owned_process_session.py'),
         Path(actual_limits.__file__))}

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

    def termination_request():
        path = args.termination_request
        if path is None or not path.exists():
            return None
        if path.stat().st_size > 4096:
            raise ValueError('The explicit termination request exceeds 4096 bytes')
        request = json.loads(path.read_text())
        if (request.get('scope') != 'held10-owned-original-command-control-v1'
                or request.get('outdir') != str(args.outdir.resolve())
                or request.get('nonce') != args.control_nonce
                or request.get('action') != 'terminate_owned_command'):
            raise ValueError('The termination request does not identify this exact owner')
        return request

    try:
        request = termination_request()
        if request is not None:
            event('actual_controlled_no_launch_request', request=request,
                  child_started=False, mathematical_failure_inferred=False)
            return 4
        with (args.outdir/'original.log').open('x') as output:
            child = subprocess.Popen(command, stdout=output, stderr=subprocess.STDOUT,
                start_new_session=True, env=dict(os.environ,
                    OPENBLAS_NUM_THREADS='2', OMP_NUM_THREADS='2', MKL_NUM_THREADS='2'))
            owner = OwnedProcessSession(child)
            event('actual_original_command_started', command=command,
                command_record=str(args.command_record.resolve()),
                command_record_sha256=sha(args.command_record),
                source_hashes=sources, actual_leader_identity=owner.leader,
                observer_initial_limits=observer_initial_limits,
                launcher_requested_threads=2, original_module_thread_settings_retained=True)
            while owner.poll_leader() is None:
                request = termination_request()
                if request is not None:
                    event('actual_controlled_termination_requested', request=request,
                          actual_leader_identity=owner.leader,
                          mathematical_failure_inferred=False)
                    cleanup = owner.cleanup()
                    observed_code = cleanup['returncode']
                    owner = None
                    usage = resource.getrusage(resource.RUSAGE_CHILDREN)
                    event('actual_original_command_joined', actual_returncode=observed_code,
                        owned_session_cleanup=cleanup, explicit_termination_request=request,
                        observer_exit_code=4, actual_owner_cleanup_return_observed=True,
                        observer_limits_after_join=actual_limits.snapshot(),
                        kernel_joined_children_maxRSS_KiB=usage.ru_maxrss,
                        kernel_joined_children_user_seconds=usage.ru_utime,
                        kernel_joined_children_system_seconds=usage.ru_stime,
                        maximum_sampled_single_process_RSS_bytes=maximum_sampled_RSS,
                        one_numerical_leader_launched=True, mathematical_failure_inferred=False)
                    return 4
                members = []
                for member in owner.members():
                    path = Path('/proc')/str(member['pid'])/'status'
                    try:
                        status = {line.split(':',1)[0]:line.split(':',1)[1].split()
                            for line in path.read_text().splitlines() if ':' in line}
                    except FileNotFoundError:
                        continue
                    identity_key = (member['pid'], member['start_ticks'])
                    limits = actual_limits.snapshot(member['pid'])
                    if identity_key not in first_limits:
                        first_limits[identity_key] = limits
                        event('actual_owned_member_initial_limits', identity=member, limits=limits)
                    row = dict(identity=member, actual_limits=limits,
                        limits_delta=actual_limits.difference(first_limits[identity_key], limits),
                        **{name+'_bytes':int(status.get(name,['0'])[0])*1024
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
            leader_limits_before_reap = actual_limits.snapshot(owner.leader['pid'])
            observer_limits_before_reap = actual_limits.snapshot()
            event('actual_limits_after_terminal_before_reap',
                leader_identity=owner.leader, leader_limits=leader_limits_before_reap,
                observer_limits=observer_limits_before_reap,
                observer_delta=actual_limits.difference(observer_initial_limits, observer_limits_before_reap))
            cleanup = owner.cleanup()
            owner = None
            usage = resource.getrusage(resource.RUSAGE_CHILDREN)
            event('actual_original_command_joined', actual_returncode=observed_code,
                owned_session_cleanup=cleanup,
                observer_limits_after_join=actual_limits.snapshot(),
                leader_limits_before_reap=leader_limits_before_reap,
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
