#!/usr/bin/env python3
"""Own one explicit command and persist its actual wait4 result and heartbeats.

This supervisor may be launched in a separate session so losing a tool session
does not erase its ownership record. It never restarts a command or changes its
arguments, numerical options, environment, or acceptance criteria. Received
SIGINT/SIGTERM are forwarded to the single owned child process group. An absent
heartbeat or a missing PID in another namespace is never an exit observation.
"""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time

SELF_SHA = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def atomic(path,value):
    temporary = path.with_name(path.name+'.tmp-'+str(os.getpid()))
    payload = (json.dumps(value,indent=2,allow_nan=False)+'\n').encode()
    with temporary.open('wb') as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary,path)


def owned_status(pid):
    # This PID was just returned by this supervisor's own Popen. It is never
    # discovered by name or imported from another execution namespace.
    result = {'owned_child_pid_in_supervisor_namespace':pid}
    try:
        for line in Path(f'/proc/{pid}/status').read_text().splitlines():
            name,_,value = line.partition(':')
            if name in ('State','PPid','VmRSS','VmHWM','Threads'):
                result[name] = value.strip()
    except (FileNotFoundError,PermissionError,ProcessLookupError) as error:
        result['owned_proc_observation_error'] = type(error).__name__
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--heartbeat',type=Path,required=True)
    parser.add_argument('--ownership',type=Path,required=True)
    parser.add_argument('--task-prefix',required=True)
    parser.add_argument('--heartbeat-seconds',type=float,default=20.)
    parser.add_argument('command',nargs=argparse.REMAINDER)
    args = parser.parse_args()
    command = args.command[1:] if args.command[:1]==['--'] else args.command
    if not command or not 1<=args.heartbeat_seconds<=60:
        raise ValueError('Require one explicit command and a bounded heartbeat period')
    for path in (args.out,args.heartbeat,args.ownership):
        path.parent.mkdir(parents=True,exist_ok=True)
        if path.exists():
            raise FileExistsError('Use fresh supervisor files: '+str(path))
    started = time.monotonic()
    ownership = dict(scope=__doc__,created_utc=utc(),task_prefix=args.task_prefix,
        supervisor_pid=os.getpid(),supervisor_pid_namespace=os.readlink('/proc/self/ns/pid'),
        cwd=str(Path.cwd()),command=command,resource_wrapper_sha256=SELF_SHA,
        resource_file=str(args.out),heartbeat_file=str(args.heartbeat),
        owned_child_pid=None,status='before-spawn',
        resource_limits_modified=False,automatic_restarts=0)
    atomic(args.ownership,ownership)
    child = subprocess.Popen(command,start_new_session=True)
    ownership.update(owned_child_pid=child.pid,owned_child_process_group=child.pid,
        status='spawned',spawned_utc=utc())
    try:
        atomic(args.ownership,ownership)
    except BaseException:
        # Failure to publish ownership cannot leave an unrecorded live child.
        # This is only the group returned by this exact Popen invocation.
        try:
            os.killpg(child.pid,signal.SIGTERM)
        except ProcessLookupError:
            pass
        deadline = time.monotonic()+10.
        while True:
            pid,status,unused_usage = os.wait4(child.pid,os.WNOHANG)
            if pid:
                child.returncode = os.waitstatus_to_exitcode(status)
                break
            if time.monotonic() >= deadline:
                os.killpg(child.pid,signal.SIGKILL)
                unused_pid,status,unused_usage = os.wait4(child.pid,0)
                child.returncode = os.waitstatus_to_exitcode(status)
                break
            time.sleep(.1)
        raise
    received = []

    def forward(signum,unused_frame):
        event = dict(signal=signum,utc=utc(),target_owned_group=child.pid)
        received.append(event)
        try:
            os.killpg(child.pid,signum)
            event['forwarded'] = True
        except ProcessLookupError:
            event['forwarded'] = False
            event['reason'] = 'Owned child group no longer observable when signal arrived'

    original = {s:signal.signal(s,forward) for s in (signal.SIGINT,signal.SIGTERM)}
    next_heartbeat = 0.
    try:
        while True:
            pid,status,usage = os.wait4(child.pid,os.WNOHANG)
            if pid:
                break
            elapsed = time.monotonic()-started
            if elapsed >= next_heartbeat:
                record = dict(task_prefix=args.task_prefix,utc=utc(),elapsed_seconds=elapsed,
                    status='running-wait4-not-returned',resource_wrapper_sha256=SELF_SHA,
                    own_process=owned_status(child.pid),received_signals=list(received))
                try:
                    atomic(args.heartbeat,record)
                except OSError as error:
                    print(json.dumps(dict(event='durable_heartbeat_storage_error',
                        error=repr(error),actual_child_exit_unobserved=True)),flush=True)
                next_heartbeat = elapsed+args.heartbeat_seconds
            time.sleep(.5)
    finally:
        for signum,handler in original.items():
            signal.signal(signum,handler)
    code = os.waitstatus_to_exitcode(status)
    child.returncode = code
    result = dict(scope=__doc__,task_prefix=args.task_prefix,command=command,
        started_utc=ownership['spawned_utc'],finished_utc=utc(),
        wall_seconds=time.monotonic()-started,exitcode=code,
        termination_signal=(-code if code<0 else None),
        wait4_observed=True,wait_status=status,peak_rss_kib=usage.ru_maxrss,
        user_seconds=usage.ru_utime,system_seconds=usage.ru_stime,
        resource_wrapper_sha256=SELF_SHA,received_supervisor_signals=received,
        owned_child_pid=child.pid,supervisor_pid=os.getpid(),
        supervisor_pid_namespace=ownership['supervisor_pid_namespace'],
        automatic_restarts=0)
    atomic(args.out,result)
    atomic(args.heartbeat,dict(task_prefix=args.task_prefix,utc=utc(),
        status='completed-by-owned-wait4',resource_file=str(args.out),
        exitcode=code,termination_signal=result['termination_signal']))
    print(json.dumps(dict(event='durable_child_exit',**result)),flush=True)
    raise SystemExit(code if code>=0 else 128-code)


if __name__ == '__main__':
    main()
