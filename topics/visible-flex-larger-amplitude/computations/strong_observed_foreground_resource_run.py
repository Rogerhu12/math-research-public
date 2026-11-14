#!/usr/bin/env python3
"""Add bounded read-only memory observations to the original owned supervisor.

No limits, process groups, numerical sources, child arguments, or wait4 gates
change. A cgroup counter is shared evidence and never assigns a cause to a
particular termination. Only this supervisor and its recorded child descendants
are read in this process namespace; no cross-execution PID is accepted.
"""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import sys
import strong_foreground_resource_run as original

SELF_SHA=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()

def observed(pid):
    value={'pid_in_own_namespace':pid}
    try:
        for line in Path(f'/proc/{pid}/status').read_text().splitlines():
            key,_,entry=line.partition(':')
            if key in ('Name','State','PPid','VmRSS','VmHWM','Threads'):
                value[key]=entry.strip()
    except OSError as exc:
        value['status_error']=type(exc).__name__
    return value

def descendants(pid,limit=8):
    pending=[pid];seen=set();values=[]
    while pending and len(seen)<limit:
        child=pending.pop(0)
        if child in seen:continue
        seen.add(child);values.append(observed(child))
        try:
            pending.extend(int(x) for x in Path(f'/proc/{child}/task/{child}/children').read_text().split())
        except OSError:
            pass
    return values

def cgroup():
    result={'scope':'Shared counters do not establish this job termination cause'}
    try:
        record=Path('/proc/self/cgroup').read_text()
        result['self_cgroup']=record
        roots=[Path('/sys/fs/cgroup')]
        for line in record.splitlines():
            parts=line.split(':',2)
            if len(parts)==3 and parts[0]=='0':roots.append(Path('/sys/fs/cgroup')/parts[2].lstrip('/'))
        result['files']={}
        for root in dict.fromkeys(roots):
            for name in ('memory.max','memory.current','memory.events','memory.events.local','memory.peak'):
                path=root/name
                try:result['files'][str(path)]=path.read_text()[:2048]
                except OSError as exc:result['files'][str(path)]={'unavailable':type(exc).__name__}
    except OSError as exc:
        result['error']=type(exc).__name__
    return result

def main():
    parser=argparse.ArgumentParser(add_help=False)
    parser.add_argument('--memory-observations',type=Path,required=True)
    args,remaining=parser.parse_known_args()
    path=args.memory_observations
    path.parent.mkdir(parents=True,exist_ok=True)
    if path.exists():raise FileExistsError('Fresh memory observation path required')
    def append(stage,pid=None):
        event=dict(stage=stage,utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
            observer_sha256=SELF_SHA,original_supervisor_sha256=original.SELF_SHA,
            supervisor=observed(os.getpid()),owned_tree=descendants(pid) if pid else [],
            cgroup=cgroup(),new_limits_applied=False)
        try:
            with path.open('a') as stream:
                stream.write(json.dumps(event,separators=(',',':'))+'\n');stream.flush()
        except OSError as exc:
            print(json.dumps({'event':'memory_observation_write_failed','error':repr(exc)}),flush=True)
    old_status=original.owned_status
    def status(pid):
        append('owned_child_running',pid)
        return old_status(pid)
    original.owned_status=status
    append('before_owned_spawn')
    oldargv=sys.argv
    try:
        sys.argv=[oldargv[0],*remaining]
        original.main()
    finally:
        append('after_original_supervisor_return')
        original.owned_status=old_status;sys.argv=oldargv

if __name__=='__main__':main()
