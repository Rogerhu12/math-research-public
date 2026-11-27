#!/usr/bin/env python3
"""Capture the ACTUAL complete current-PCG pure-reader result or exception.

First capture the original completed followup's retained combined child log.
The original b527 pair inherits stdout/stderr and does not create per-child
log files. Then, distinctly, call unchanged 0d659 with both original flags
after the controller's recorded cleanup. A new exception is never promoted
to the cause of the old failure. Only JSON/source/whole-file bytes are read. No
field, J, transpose, root, optimization, restoration or numerical fixture is
executed. The scientific child's real success is kept separate from a failed
pure read. Full traceback/readout remain on the runner; public fields bounded.
"""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time
import traceback

SCHEMA='actual-current-PCG-original-log-and-post-cleanup-reader-v2'
READER_SHA='0d659ab94bff7fe12337cc8f1eb18263ae1623f8fb8bcbb40108e7e03ad3856f'
DRIVER_SHA='a0e27f36692d565d333b1ef5a207afa425ec0fc9a120164a0df3a3057f3dc743'
PAIR_SHA='b527b42440ebb792830c288cb28567b1c7c1cd7eba921dfc16e18ca3d76a0b24'
REPORT_SCHEMA='complete-normalized-parent-cached-current-eight-column-PCG-SOC-v1'
PAIR_SCHEMA='actual-complete-current-PCG-from-interior-inherited-damping-pair-v1'
FOLLOWUPS_SHA='3cb1e706ab43dac6e952ce00b41e83055112d2ee65edb37682d1f05e94f2ee3f'
ACTUAL_STEP_ID='complete-current-PCG-from-actual40-after41-independent-pair-20261127-run06'
ACTUAL_SOURCE_COMMIT='a6d1b337b3622b8aa65790a96401f0be836a5662'
TOPIC='topics/visible-flex-larger-amplitude'

def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda:stream.read(1024*1024),b''):h.update(block)
    return h.hexdigest()

def record(path):
    path=Path(path).resolve()
    return dict(path=str(path),bytes=path.stat().st_size,sha256=sha(path))

def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),
        allow_nan=False).encode()).hexdigest()

def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(value,indent=2,allow_nan=False)+'\n').encode()
    with path.open('xb') as stream:stream.write(raw)

def load_json(path,expected):
    raw=Path(path).read_bytes()
    if hashlib.sha256(raw).hexdigest()!=expected:
        raise ValueError('Bind the exact actually returned complete input: '+str(path))
    return json.loads(raw)


def original_log_evidence(a, pair):
    """Read only the real completed journal record and its retained log tail.

    Journal is mutable: preserve this captured snapshot identity, not a claim
    that a later journal stays byte-equal. The selected original log itself
    must remain unchanged before/after the bounded read.
    """
    result=dict(available=False,status='unavailable',journal_path=str(a.followup_journal),
        journal_snapshot_sha256=None,journal_snapshot_bytes=None,
        original_record_canonical_sha256=None,original_log_path=None,
        original_log_sha256=None,original_log_bytes=None,
        original_log_tail=None,original_log_tail_bytes=None,
        original_log_tail_truncated=None,pure_start_marker_in_retained_tail=False,
        pure_finish_marker_in_retained_tail=False,pure_event_interval_complete=False,
        selected_original_tail_scope='unavailable',
        separate_pure_stdout_or_stderr_files_declared=False,
        declared_pure_output_keys=sorted(pair['children'][1]),
        pair_stdout_stderr_scope='b527 inherits both streams; 3cb1 combines them in the original followup log',
        cleanup_recorded=False,cleanup_deleted_count=None,cleanup_recorded_deleted_bytes=None,
        cleanup_deleted_records_canonical_sha256=None,
        original_exception_diagnosed_automatically=False,error=None)
    try:
        data=a.followup_journal.read_bytes()
        result.update(journal_snapshot_sha256=hashlib.sha256(data).hexdigest(),
            journal_snapshot_bytes=len(data))
        journal=json.loads(data)
        if journal.get('module_sha256')!=FOLLOWUPS_SHA:
            raise ValueError('Use the actual complete followup module journal')
        rows=[v for v in journal.get('records',[]) if v.get('step_id')==a.actual_step_id]
        if len(rows)!=1:
            raise ValueError('Require the unique actually returned original pair record')
        value=rows[0]
        if (a.actual_step_id!=ACTUAL_STEP_ID or value.get('module_sha256')!=FOLLOWUPS_SHA
                or value.get('source_sha256')!=PAIR_SHA
                or value.get('source_commit')!=ACTUAL_SOURCE_COMMIT
                or value.get('state')!='failed' or value.get('returncode')!=1):
            raise ValueError('The selected log must belong to the exact returned original pair')
        outputs={str(Path(v['path']).resolve()):v for v in value.get('outputs',[])}
        for path,digest in ((a.report,a.report_sha256),(a.pair_status,a.pair_status_sha256),
                (a.checkpoint,a.checkpoint_sha256)):
            if outputs.get(str(path),{}).get('sha256')!=digest:
                raise ValueError('The original log record belongs to different returned bytes')
        result['original_record_canonical_sha256']=canonical(value)
        cleanup=value.get('cleanup_generated',{})
        deleted=cleanup.get('deleted')
        if isinstance(deleted,list):
            encoded=json.dumps(deleted,ensure_ascii=False,sort_keys=True,
                separators=(',',':'),allow_nan=False).encode()
            result.update(cleanup_recorded=True,cleanup_deleted_count=len(deleted),
                cleanup_recorded_deleted_bytes=sum(v.get('bytes',0) for v in deleted),
                cleanup_deleted_records_canonical_sha256=hashlib.sha256(encoded).hexdigest())
        path=Path(value['log']).resolve()
        log_directory=(a.followup_journal.parent/'followup-logs').resolve()
        if path.parent!=log_directory or path.suffix!='.log' or path.is_symlink():
            raise ValueError('Only the literal original same-run followup log is readable')
        before=record(path);result.update(original_log_path=str(path),
            original_log_sha256=before['sha256'],original_log_bytes=before['bytes'])
        with path.open('rb') as stream:
            stream.seek(max(0,before['bytes']-64000))
            tail=stream.read(64000)
        text=tail.decode('utf-8',errors='replace')
        lines=text.splitlines(keepends=True);start=None;finish=None
        for i,line in enumerate(lines):
            try:event=json.loads(line)
            except (ValueError,TypeError):continue
            if not isinstance(event,dict) or event.get('role')!='pure_reader':continue
            if event.get('event')=='bound_pair_child_start':start=i
            if event.get('event')=='bound_pair_child_return':finish=i
        interval_complete=start is not None and finish is not None and start<=finish
        selected=''.join(lines[start:finish+1]) if interval_complete else text
        selected_scope=('actual pure child start-through-return closed log interval'
            if interval_complete else
            'bounded original combined log tail; complete pure event interval unavailable; no causal attribution')
        bounded=selected[-7000:]
        if record(path)!=before:
            raise ValueError('The original returned log changed while its tail was read')
        result.update(available=True,status='original-retained-followup-log',
            original_log_tail=bounded,original_log_tail_bytes=len(bounded.encode()),
            original_log_tail_truncated=before['bytes']>len(bounded.encode()),
            pure_start_marker_in_retained_tail=start is not None,
            pure_finish_marker_in_retained_tail=finish is not None,
            pure_event_interval_complete=interval_complete,
            selected_original_tail_scope=selected_scope)
    except (OSError,KeyError,TypeError,ValueError) as error:
        result.update(status='original-log-unavailable-or-binding-failed',
            error=type(error).__name__+': '+str(error)[:1500])
    return result

def parse_args():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--report',type=Path,required=True)
    p.add_argument('--report-sha256',required=True)
    p.add_argument('--checkpoint',type=Path,required=True)
    p.add_argument('--checkpoint-sha256',required=True)
    p.add_argument('--pair-status',type=Path,required=True)
    p.add_argument('--pair-status-sha256',required=True)
    p.add_argument('--followup-journal',type=Path,required=True)
    p.add_argument('--actual-step-id',required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    for name in ('repo','report','checkpoint','pair_status','followup_journal','output'):
        setattr(a,name,getattr(a,name).resolve())
    if a.output==a.repo or a.repo in a.output.parents:
        raise ValueError('Keep actual diagnostic raw outside the repository')
    return a

def main():
    if (os.environ.get('GITHUB_ACTIONS')!='true'
            or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise SystemExit('Actual report diagnostics run only in public repository Actions')
    a=parse_args();started=time.monotonic()
    reader_path=a.repo/TOPIC/'scripts/resume_20261126/read_so3_cached_current_pcg_soc_report.py'
    driver_path=a.repo/TOPIC/'scripts/resume_20261126/fullclosed_so3_cached_current_pcg_soc.py'
    followups_path=a.repo/TOPIC/'scripts/resume_20261126/public_actions_followups_compact_metadata.py'
    if sha(followups_path)!=FOLLOWUPS_SHA:
        raise ValueError('Bind the actual stdout/stderr capture and cleanup source')
    if sha(reader_path)!=READER_SHA or sha(driver_path)!=DRIVER_SHA:
        raise ValueError('Use both exact whole previously executed sources')
    if sha(a.checkpoint)!=a.checkpoint_sha256:
        raise ValueError('The actual complete scientific final checkpoint changed')
    raw=load_json(a.report,a.report_sha256)
    pair=load_json(a.pair_status,a.pair_status_sha256)
    if (raw.get('schema')!=REPORT_SCHEMA or raw.get('source_sha256')!=DRIVER_SHA
            or raw.get('complete') is not True
            or raw.get('final_bundle_sha256')!=a.checkpoint_sha256
            or canonical(raw.get('representation'))!=raw.get('model_identity_sha256')):
        raise ValueError('Read the actual complete scientific source/model/final, not an invented failed field')
    children=pair.get('children',[])
    if (pair.get('schema')!=PAIR_SCHEMA or pair.get('source_sha256')!=PAIR_SHA
            or pair.get('complete') is not True or pair.get('both_children_returned') is not True
            or len(children)!=2
            or [c.get('role') for c in children]!=['scientific_launcher','pure_reader']
            or children[0].get('state')!='returned' or children[0].get('returncode')!=0
            or children[1].get('state')!='returned' or children[1].get('returncode')!=1
            or pair.get('scientific_success') is not True or pair.get('pure_success') is not False
            or pair.get('scientific_report',{}).get('sha256')!=a.report_sha256):
        raise ValueError('Keep the real scientific-success / pure-reader-failure distinction')
    inputs=dict(report=record(a.report),checkpoint=record(a.checkpoint),pair_status=record(a.pair_status))
    trace_path=a.output.with_name(a.output.stem+'-actual-traceback.txt')
    result_path=a.output.with_name(a.output.stem+'-actual-reader-result.json')
    for path in (a.output,trace_path,result_path):
        if path.exists() or path in (a.report,a.checkpoint,a.pair_status,a.followup_journal,reader_path,driver_path):
            raise ValueError('Use three fresh disjoint diagnostic output paths')
    original=original_log_evidence(a,pair)
    result=dict(schema=SCHEMA,source_sha256=sha(__file__),complete=False,
        actual_input_records=inputs,reader_source=record(reader_path),driver_source=record(driver_path),
        original_log_evidence=original,actual_followup_source=record(followups_path),
        reader_recheck_time_scope='after original pair return and recorded controller cleanup',
        recheck_exception_is_automatically_original_failure_cause=False,
        original_exception_or_original_log_replaced_by_recheck=False,
        actual_scientific_report_source_sha256=raw['source_sha256'],
        actual_model_identity_sha256=raw['model_identity_sha256'],
        actual_final_bundle_sha256=raw['final_bundle_sha256'],
        actual_pair_scientific_returncode=0,actual_pair_pure_returncode=1,
        actual_scientific_report_complete=True,underlying_reader_returned=False,
        reader_repeated_scientific_solve=False,F_calls=0,J_calls=0,Jtranspose_calls=0,root_calls=0,
        original_verify_final_bundle=True,original_verify_cache_files=True,
        exception_type=None,exception_message=None,traceback_tail=None,
        traceback_tail_truncated=False,traceback_file=None,reader_result_file=None,
        traceback_sha256=None,traceback_bytes=None,reader_result_sha256=None,reader_result_bytes=None,
        continuous_or_refinement_certificate_claimed=False)
    spec=importlib.util.spec_from_file_location('_exact_actual_PCGr_'+READER_SHA,reader_path)
    module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module
    try:
        spec.loader.exec_module(module)
        if sha(module.read_report.__code__.co_filename)!=READER_SHA:
            raise ValueError('The actual complete pure read entry changed')
        value=module.read_report(a.repo,a.report,verify_final_bundle=True,verify_cache_files=True)
        save(result_path,value)
        bound=record(result_path)
        result.update(underlying_reader_returned=True,reader_result_file=bound,
            reader_result_sha256=bound['sha256'],reader_result_bytes=bound['bytes'])
    except Exception as error:
        exact=traceback.format_exc()
        trace_path.parent.mkdir(parents=True,exist_ok=True)
        with trace_path.open('x',encoding='utf-8') as stream:stream.write(exact)
        message=str(error)
        result.update(exception_type=type(error).__name__,
            exception_message=message[:1500],exception_message_truncated=len(message)>1500,
            traceback_tail=exact[-7000:],traceback_tail_truncated=len(exact)>7000,
            traceback_file=record(trace_path),traceback_sha256=sha(trace_path),
            traceback_bytes=trace_path.stat().st_size,reader_failure_is_not_scientific_failure=True)
    for role,path in (('report',a.report),('checkpoint',a.checkpoint),('pair_status',a.pair_status)):
        if record(path)!=inputs[role]:raise ValueError('A complete actual input changed during pure diagnostics')
    if sha(reader_path)!=READER_SHA or sha(driver_path)!=DRIVER_SHA:
        raise ValueError('A complete original source changed during pure diagnostics')
    result.update(complete=True,seconds=time.monotonic()-started,
        original_report_checkpoint_and_pair_bytes_unchanged=True)
    save(a.output,result)
    print(json.dumps(result,separators=(',',':'),allow_nan=False),flush=True)
    return 0

if __name__=='__main__':
    raise SystemExit(main())
