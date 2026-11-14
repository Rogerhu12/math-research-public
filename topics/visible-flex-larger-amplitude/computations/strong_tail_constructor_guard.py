#!/usr/bin/env python3
"""Close only the owned tail process if client construction fails.

The original numerical client, worker, MJS sources, exact-stage identity, request
protocol and all acceptance gates are unchanged. This is explicit error-path
resource cleanup, including an observed final child status after metadata I/O
errors. It never accepts a partially constructed client or tail response.
"""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import resource
import sys
import time

HERE=Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


HELPER_SHA256=sha(__file__)


def atomic_same(path,data):
    path=Path(path)
    if path.exists():
        if path.read_bytes()!=data:
            raise FileExistsError('Different immutable guard provenance: '+str(path))
        return
    temporary=path.with_name(path.name+'.tmp-'+str(os.getpid()))
    with temporary.open('xb') as stream:
        stream.write(data);stream.flush();os.fsync(stream.fileno())
    try:
        try:
            os.link(temporary,path)
        except FileExistsError:
            if path.read_bytes()!=data:
                raise
    finally:
        temporary.unlink()


def protect_tail_class(Base):
    class GuardedTailPort(Base):
        def __init__(self,*args,**kwargs):
            started=time.monotonic()
            record_prefix=kwargs.get('record_prefix',args[2] if len(args)>2 else None)
            try:
                super().__init__(*args,**kwargs)
            except BaseException as error:
                proc=getattr(self,'proc',None)
                record=dict(event='owned_tail_constructor_failure_cleanup',
                    error=repr(error),constructor_returned_successfully=False,
                    new_tail_response=False,helper_sha256=HELPER_SHA256,
                    mathematical_worker_sources_and_protocol_unchanged=True)
                if proc is not None:
                    record['owned_child_pid']=getattr(proc,'pid',None)
                    try:
                        record['returncode_before_original_close']=proc.poll()
                        Base.close(self)
                    except BaseException as close_error:
                        record['original_close_error']=repr(close_error)
                    try:
                        # Original close is authoritative; wait only this known
                        # constructor-owned child so wait4 includes its resources.
                        record['returncode_after_original_close']=proc.poll()
                        if proc.poll() is None:
                            proc.wait(timeout=15)
                        record['observed_final_child_returncode']=proc.poll()
                    except BaseException as wait_error:
                        record['final_wait_error']=repr(wait_error)
                else:
                    record['child_was_not_created']=True
                record['seconds']=time.monotonic()-started
                record['waited_children_peak_rss_kib']=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
                try:
                    print(json.dumps(record),file=sys.stderr,flush=True)
                except BaseException:
                    pass
                if record_prefix is not None:
                    try:
                        p=Path(record_prefix)
                        path=p.with_name(p.name+'_constructor-failure.json')
                        atomic_same(path,(json.dumps(record,indent=2)+'\n').encode())
                    except BaseException as recording_error:
                        try:
                            print(json.dumps(dict(event='constructor_failure_record_unavailable',
                                error=repr(recording_error),original_error=repr(error))),
                                file=sys.stderr,flush=True)
                        except BaseException:
                            pass
                raise
    return GuardedTailPort


def main():
    if sys.argv.count('--out-prefix')!=1:
        raise ValueError('An explicit fresh output prefix is required')
    prefix=Path(sys.argv[sys.argv.index('--out-prefix')+1])
    prefix.parent.mkdir(parents=True,exist_ok=True)
    record=dict(scope=__doc__,helper_sha256=HELPER_SHA256,
        retained_seed_audit_entry_sha256=sha(HERE/'strong_cached_seed_tail_audit.py'),
        retained_stage_client_sha256=sha(HERE/'strong_exact_stage_tail_client.py'),
        source_MJS_bytes_unchanged=True,stage_cache_identity_unchanged=True,
        normal_constructor_and_numerical_execution_unchanged=True,
        added_action='On constructor failure call its original close, then wait for that same child and rethrow original error.')
    # If even provenance cannot be stored, fail before creating a Node process.
    atomic_same(prefix.with_name(prefix.name+'-constructor-guard.json'),
        (json.dumps(record,indent=2)+'\n').encode())
    import strong_exact_stage_tail_client as client
    import strong_cached_seed_tail_audit as runner
    original=client.WeightedTailPort
    client.WeightedTailPort=protect_tail_class(original)
    try:
        runner.main()
    finally:
        client.WeightedTailPort=original


if __name__=='__main__':
    main()
