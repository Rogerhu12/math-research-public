#!/usr/bin/env python3
"""Own one actual fixed-support child and clean its complete mapped scratch.

The numerical argv is passed unchanged to the independent actual-DN entry.
The explicit standalone mode uses the already checked OwnedProcessSession
until all same-session descendants have ended, including after leader death.
The explicit inherited mode stays inside the CI v3 owner's unchanged SID.
Only then does the reviewed cleanup touch that child's uniquely owned QR
backing directories. Accepted fields and original checkpoints are retained.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
DESIGN = HERE.parent/'design'
sys.path.insert(0,str(DESIGN))
from owned_process_session import OwnedProcessSession, process_identity
from mapped_factor_cleanup import cleanup_joined_child


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write(path,value):
    temporary = path.with_name(path.name+'.tmp')
    temporary.write_text(json.dumps(value,indent=2,allow_nan=False)+'\n')
    temporary.replace(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--process-record',type=Path,required=True)
    parser.add_argument('--console',type=Path,required=True)
    owner = parser.add_mutually_exclusive_group(required=True)
    owner.add_argument('--inherit-owned-session',action='store_true',
        help='Keep the existing CI v3 owned session; its outer owner reaps every surviving descendant')
    owner.add_argument('--own-child-session',action='store_true',
        help='Standalone local owner creates and fully reaps one new child session')
    parser.add_argument('solver_args',nargs=argparse.REMAINDER)
    args = parser.parse_args()
    values = args.solver_args[1:] if args.solver_args[:1] == ['--'] else args.solver_args
    def option(flag):
        if values.count(flag) != 1:
            raise ValueError('Require exactly one original actual solver option '+flag)
        return values[values.index(flag)+1]
    out,work = Path(option('--outdir')).resolve(),Path(option('--work')).resolve()
    if (work not in out.parents or out.exists() or args.process_record.exists() or args.console.exists()
            or work not in args.process_record.resolve().parents or work not in args.console.resolve().parents):
        raise ValueError('Use fresh child output and terminal records within the owned outside-repo work tree')
    entry = HERE/'qr_fixed_support_actual_step.py'
    command = [sys.executable,'-u',str(entry),*values]
    sources = [Path(__file__),entry,HERE/'qr_fixed_support_actual_model.py',
        HERE/'qr_fixed_support_actual_acceptance.py',HERE/'qr_fixed_support_actual_resources.py',
        DESIGN/'owned_process_session.py',DESIGN/'mapped_factor_cleanup.py']
    inherited = None
    if os.environ.get('GITHUB_ACTIONS') == 'true' and not args.inherit_owned_session:
        raise ValueError('Under CI v3 explicitly inherit its owned session; do not create an escaping nested session')
    if args.inherit_owned_session:
        inherited = process_identity(os.getsid(0))
        if (inherited is None or inherited['pid'] != inherited['sid']
                or inherited['pgid'] != inherited['sid'] or inherited['uid'] != os.getuid()):
            raise ValueError('An existing outer-owned session leader is required')
    record = dict(status='starting_one_original_support_actual_fixed_DN_child',argv=command,
        source_hashes={str(p.resolve()):sha(p) for p in sources},output=str(out),
        console=str(args.console.resolve()),actual_child_terminal_observed=False,
        inherited_outer_owned_session=inherited,
        ownership_mode='inherit-owned-session' if args.inherit_owned_session else 'own-child-session',
        external_owner_responsible_for_whole_session_reaping=args.inherit_owned_session,
        mathematical_acceptance_inferred_from_returncode=False,complete_surface=False)
    write(args.process_record,record)
    started = time.monotonic()
    with args.console.open('x') as console:
        child = subprocess.Popen(command,stdout=console,stderr=subprocess.STDOUT,
                                 start_new_session=not args.inherit_owned_session)
        record.update(actual_child_session_id=os.getsid(child.pid),
                      actual_child_process_group_id=os.getpgid(child.pid))
        if args.inherit_owned_session:
            # The outer CI v3 owns this unchanged SID and its unreaped leader.
            # In particular a -9 of this small launcher cannot leave the large
            # child in an untracked second session. Do not claim or perform
            # outer-session signal authority from inside this descendant.
            record.update(status='one_actual_fixed_DN_child_running',child_pid=child.pid,
                          child_inherits_outer_session_id=inherited['sid'])
            write(args.process_record,record)
            try:
                child.wait()
            except KeyboardInterrupt:
                child.send_signal(signal.SIGINT)
                record['manual_interrupt_forwarded_to_actual_child'] = True
                child.wait()
        else:
            owned = OwnedProcessSession(child)
            record.update(status='one_actual_fixed_DN_child_running',owned_leader=dict(owned.leader))
            write(args.process_record,record)
            try:
                while owned.poll_leader() is None:
                    time.sleep(15)
            except KeyboardInterrupt:
                record['manual_interrupt_forwarded_to_owned_session'] = True
                owned.signal_session(signal.SIGINT)
            finally:
                # Keep the leader unreaped until every owned descendant ends.
                record['owned_process_session_cleanup'] = owned.cleanup()
    code = child.returncode
    record.update(status='one_actual_fixed_DN_child_returned',actual_child_terminal_observed=True,
        returncode=code,seconds=time.monotonic()-started,
        maximum_child_rss_kib=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss)
    write(args.process_record,record)
    try:
        record['joined_child_mapped_storage_cleanup'] = cleanup_joined_child(
            out,code,child_return_observed=True,entry_sha256=sha(entry))
    except Exception as error:
        record['joined_child_mapped_storage_cleanup_error'] = repr(error)
        record['cleanup_failure_does_not_relabel_original_child_return'] = True
    run = out/'run.json'
    if run.exists():
        record['actual_run'] = dict(path=str(run),sha256=sha(run))
    write(args.process_record,record)
    print(json.dumps(record,allow_nan=False),flush=True)
    return code


if __name__ == '__main__':
    raise SystemExit(main())
