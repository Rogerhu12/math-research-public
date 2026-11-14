#!/usr/bin/env python3
"""Add only an explicit V8 young-space resource limit to the retained worker.

The exact original Node command, worker source, physical parameters, cache
identity, nonlinear solver and audit remain. The only launch change appends
--max-semi-space-size to the existing explicit old-heap NODE_OPTIONS value.
An outer constructor guard closes/reaps only that same owned process on error.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from strong_tail_constructor_guard import atomic_same,protect_tail_class,HELPER_SHA256 as CLEANUP_SHA

HERE=Path(__file__).resolve().parent
SELF_SHA=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
WORKER=HERE/'strong_exact_stage_tail_worker.mjs'
WORKER_SHA=hashlib.sha256(WORKER.read_bytes()).hexdigest()


def augment_spawn(command,kwargs,old_heap,semi_space):
    """Return the explicit resource-only environment change for this worker."""
    if (not isinstance(command,(list,tuple)) or not command or command[0]!='node'
            or str(WORKER) not in command):
        return kwargs,None
    if command.count(str(WORKER))!=1 or not isinstance(kwargs.get('env'),dict):
        raise ValueError('The owned exact-stage Node launch changed')
    old_options='--max-old-space-size='+str(old_heap)
    if kwargs['env'].get('NODE_OPTIONS')!=old_options:
        raise ValueError('The original explicit Node old-heap option differs')
    new_options=old_options+' --max-semi-space-size='+str(semi_space)
    changed=dict(kwargs);changed['env']={**kwargs['env'],'NODE_OPTIONS':new_options}
    record=dict(schema='explicit-Node-young-space-resource-only-v1',
        actual_command_unchanged=list(command),worker_sha256=WORKER_SHA,
        NODE_OPTIONS_before=old_options,NODE_OPTIONS_after=new_options,
        source_sha256=SELF_SHA,constructor_cleanup_sha256=CLEANUP_SHA,
        only_changed_environment_key='NODE_OPTIONS',
        mathematical_parameters_and_MJS_sources_unchanged=True,
        all_original_nonlinear_full_Jacobian_and_audit_gates_preserved=True,
        exact_stage_identity_and_original_cached_bytes_unchanged=True)
    return changed,record


def resource_port_class(Base,old_heap,semi_space):
    class ResourcePort(Base):
        def __init__(self,*args,**kwargs):
            record_prefix=kwargs.get('record_prefix',args[2] if len(args)>2 else None)
            requested=kwargs.get('node_heap',args[3] if len(args)>3 else None)
            if record_prefix is None or requested!=old_heap:
                raise ValueError('The complete explicit resource request is required')
            prefix=Path(record_prefix);seen=[];original=subprocess.Popen
            def owned_spawn(command,*rest,**spawn_kwargs):
                changed,record=augment_spawn(command,spawn_kwargs,old_heap,semi_space)
                if record is None:return original(command,*rest,**spawn_kwargs)
                if seen:raise ValueError('One client constructor may launch only one owned worker')
                # Save the intention before creating the child. A disk failure
                # at this point therefore cannot leave an unowned child.
                atomic_same(prefix.with_name(prefix.name+'_Node-resource-intent.json'),
                    (json.dumps(record,indent=2)+'\n').encode())
                proc=original(command,*rest,**changed)
                self.proc=proc
                seen.append({**record,'owned_child_pid':proc.pid})
                return proc
            subprocess.Popen=owned_spawn
            try:
                super().__init__(*args,**kwargs)
                if len(seen)!=1 or seen[0]['owned_child_pid']!=self.proc.pid:
                    raise ValueError('The exact resource option was not applied once to this worker')
                atomic_same(prefix.with_name(prefix.name+'_Node-resource-observed.json'),
                    (json.dumps(seen[0],indent=2)+'\n').encode())
            finally:
                subprocess.Popen=original
    return protect_tail_class(ResourcePort)


def main():
    parser=argparse.ArgumentParser(add_help=False,description=__doc__)
    parser.add_argument('--node-young-semi-space',type=int,choices=(1,2,4,8,16),required=True)
    options,remaining=parser.parse_known_args()
    if remaining.count('--node-heap')!=1 or remaining.count('--out-prefix')!=1:
        raise ValueError('Explicit old-heap and fresh output prefix are required')
    old_heap=int(remaining[remaining.index('--node-heap')+1])
    if old_heap<=0:raise ValueError('The old-heap resource setting must be positive')
    prefix=Path(remaining[remaining.index('--out-prefix')+1])
    prefix.parent.mkdir(parents=True,exist_ok=True)
    source=HERE/'strong_cached_seed_tail_audit.py'
    metadata=dict(scope=__doc__,source_sha256=SELF_SHA,
        cleanup_guard_sha256=CLEANUP_SHA,
        retained_seed_audit_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
        original_worker_sha256=WORKER_SHA,
        old_heap_MiB=old_heap,young_semi_space_MiB=options.node_young_semi_space,
        no_claim_about_prior_signal9_cause=True,
        mathematical_parameters_and_MJS_sources_unchanged=True)
    atomic_same(prefix.with_name(prefix.name+'-Node-resource-wrapper.json'),
        (json.dumps(metadata,indent=2)+'\n').encode())
    import strong_exact_stage_tail_client as client
    import strong_cached_seed_tail_audit as runner
    original_class,old_argv=client.WeightedTailPort,sys.argv
    client.WeightedTailPort=resource_port_class(original_class,old_heap,options.node_young_semi_space)
    sys.argv=[old_argv[0],*remaining]
    try:runner.main()
    finally:
        client.WeightedTailPort=original_class
        sys.argv=old_argv


if __name__=='__main__':main()
