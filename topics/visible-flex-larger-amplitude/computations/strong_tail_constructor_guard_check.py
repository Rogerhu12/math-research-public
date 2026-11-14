#!/usr/bin/env python3
"""Reproduce the seven constructor-cleanup checks with two tiny owned children.

The first execution used these same test bodies in an inline Python command.
This reusable entry adds only a fresh output argument and its own source hash.
It starts no mathematical Node worker, physical Flow, Jacobian, or BVP.
"""
import argparse
import contextlib
import hashlib
import io
import json
from pathlib import Path
import resource
import subprocess
import sys
import time
import strong_tail_constructor_guard as guard


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    if args.out.exists():raise FileExistsError('Use a fresh verification output')
    started=time.monotonic();checks={};records=[]
    helper_sha=guard.HELPER_SHA256
    check_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    class Good:
        def __init__(self,*a,**kw):self.received=(a,kw);self.sources={'unchanged':'literal'}
        def close(self):raise AssertionError('Successful construction must not close')
    value=guard.protect_tail_class(Good)('config','root',None,node_heap=128)
    checks['success_argument_and_source_objects_preserved']=(value.received==
        (('config','root',None),{'node_heap':128}) and value.sources=={'unchanged':'literal'})
    class OwnedFailure:
        latest=None
        def __init__(self,*a,**kw):
            type(self).latest=self
            self.error=OSError(28,'synthetic metadata write failure')
            self.proc=subprocess.Popen([sys.executable,'-u','-c',
                'import sys\nfor line in sys.stdin:\n if line.strip()=="stop": break\n'],
                stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True)
            self.pid=self.proc.pid;self.close_calls=0
            raise self.error
        def close(self):
            self.close_calls+=1
            if self.proc.poll() is None:
                self.proc.stdin.write('stop\n');self.proc.stdin.flush();self.proc.wait(timeout=15)
    Guard=guard.protect_tail_class(OwnedFailure);error=None;stream=io.StringIO()
    with contextlib.redirect_stderr(stream):
        try:Guard('config','root',None)
        except OSError as caught:error=caught
    obj=Guard.latest;records.extend(json.loads(x) for x in stream.getvalue().splitlines())
    checks['same_original_exception_object_rethrown']=error is obj.error
    checks['only_original_owned_close_called_once']=obj.close_calls==1
    checks['real_owned_child_reaped_with_observed_zero']=(obj.proc.poll()==0
        and records[-1]['observed_final_child_returncode']==0 and records[-1]['owned_child_pid']==obj.pid)
    class BeforeChild:
        def __init__(self,*a,**kw):raise ValueError('synthetic failure before any child')
        def close(self):raise AssertionError('No child exists')
    stream=io.StringIO()
    with contextlib.redirect_stderr(stream):
        try:guard.protect_tail_class(BeforeChild)('config','root',None)
        except ValueError:pass
    row=json.loads(stream.getvalue());records.append(row)
    checks['no_child_failure_does_not_invent_cleanup']=row['child_was_not_created']
    old=guard.atomic_same
    guard.atomic_same=lambda *a,**kw:(_ for _ in ()).throw(OSError(28,'synthetic secondary recording failure'))
    Guard=guard.protect_tail_class(OwnedFailure);stream=io.StringIO();error=None
    try:
        with contextlib.redirect_stderr(stream):
            try:Guard('config','root','notes/unused-probe-no-file-created')
            except OSError as caught:error=caught
        obj=Guard.latest;rows=[json.loads(x) for x in stream.getvalue().splitlines()];records+=rows
        checks['secondary_recording_failure_keeps_original_exception']=error is obj.error
        checks['secondary_recording_failure_still_reaps_only_owned_child']=(obj.proc.poll()==0
            and obj.close_calls==1 and rows[-1]['event']=='constructor_failure_record_unavailable')
    finally:guard.atomic_same=old
    result=dict(scope=__doc__,passed=all(checks.values()),checks=checks,
        source_sha256=helper_sha,check_source_sha256=check_sha,
        observed_records=records,seconds=time.monotonic()-started,
        self_peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        child_peak_rss_kib=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,physical_workers=0)
    args.out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
    if not result['passed']:raise SystemExit(1)


if __name__=='__main__':main()
