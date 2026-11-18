#!/usr/bin/env python3
"""Collect the completed exact native double baseline; never call its library."""
import argparse
import hashlib
import json
from pathlib import Path
import struct
from record_fixed_actual import load, sha, scalar_tree
from record_tail_initialization import numeric_identity


def ident(path):
    return dict(path=str(Path(path).resolve()),sha256=sha(path))


def checked(ref):
    if sha(ref['path'])!=ref['sha256']:raise ValueError('Frozen baseline file changed: '+ref['path'])
    return load(ref['path'])


def packed(values):
    return struct.pack('<'+'d'*len(values),*values)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('plan','summary','resource','log','out'):
        p.add_argument('--'+key,type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise ValueError('Do not overwrite completed baseline record')
    plan,summary,resource=load(a.plan),load(a.summary),load(a.resource)
    for ref in plan['files'].values():
        if sha(ref['path'])!=ref['sha256']:raise ValueError('A planned source/input changed')
    if resource['status']!='observed_terminal' or resource['child_returncode']!=0:
        raise ValueError('Real successful terminal required')
    if resource['command']!=plan['command'] or resource['command'][1:]!=summary['command']:
        raise ValueError('Observed command differs from frozen plan')
    if summary['mode']!='float-baseline' or summary['full40_column_Jacobian_computed'] or summary['full_tail_or_DN_invoked']:
        raise ValueError('Only original double baseline was authorized')
    for key in ('all_three_outputs42_bitwise_identical','all_original_operands_and_judgments_bitwise_identical'):
        if not summary[key]:raise ValueError('Exact baseline did not pass')
    if summary['verified_output_count']!=126 or summary['verified_event_count']!=116608:
        raise ValueError('Incomplete prescribed exact baseline')
    cs=checked(summary['capsule_summary']);reference=checked(summary['reference_identity']);raw=checked(summary['raw'])
    build=checked(summary['build_record'])
    if summary['sources']!=build['sources'] or summary['library']!=build['library']:
        raise ValueError('Executed native source/build identity mismatch')
    if summary['source']!=build['sources']['harness']:raise ValueError('Executed harness identity mismatch')
    source_map={}
    for key in ('source_sha256','additional_original_root_sources'):
        for path,digest in cs[key].items():
            if sha(path)!=digest:raise ValueError('Original reference source changed')
            source_map[path]=digest
    stages={};total=0
    for old,row,scalar in zip(reference['rows'],raw['rows'],summary['named_results'],strict=True):
        if not old['stage']==row['stage']==scalar['stage']:raise ValueError('Stage mismatch')
        if len(row['state'])!=42 or packed(old['state'])!=packed(row['state']):
            raise ValueError('All42 original output byte identity failed')
        if numeric_identity(old['events'])!=numeric_identity(row['events']):
            raise ValueError('Original full trace operand/judgment identity failed')
        if bytes.fromhex(row['native_state_hex'])!=packed(row['state']):
            raise ValueError('Native mode0 output encoding differs')
        if hashlib.sha256(packed(row['state'])).hexdigest()!=scalar['output42_sha256']:
            raise ValueError('Saved output identity differs')
        roots=[event for event in row['events']if event['event']=='root_return']
        diag=scalar['diagnostics']
        if (len(roots)!=diag['root_calls'] or sum(event['iteration']for event in roots)!=diag['root_updates'] or
            sum(event['roundoffFallback']for event in roots)!=diag['root_fallbacks']):
            raise ValueError('Returned root diagnostics differ')
        if len(row['events'])!=scalar['trace_events'] or len(row['events'])!=diag['trace_events']:
            raise ValueError('Trace count mismatch')
        total+=len(row['events']);stages[str(row['stage'])]=dict(**scalar,
            complete_original_state_and_both_means_verified=True,
            complete_original_event_identity_verified=True)
    if total!=116608:raise ValueError('Total trace identity incomplete')
    output=dict(scope='Completed exact native DOUBLE/V8 port validation only. No long-double arithmetic, literal-Jacobian, full batch or DN acceptance.',
        collector=ident(__file__),helpers={name:sha(Path(__file__).with_name(name))for name in
                                         ('record_fixed_actual.py','record_tail_initialization.py')},
        frozen_plan=ident(a.plan),summary=ident(a.summary),raw=summary['raw'],build_record=summary['build_record'],
        native_sources=summary['sources'],compiled_library=summary['library'],compiled_batch_cli=summary['batch_executable'],
        original_entry_files={key:summary[key]for key in ('original_evaluator','bridge','capsule_summary','old_float_baseline',
            'mp90_summary','coefficient_identity','reference_identity','mp90_raw')},
        original_source_sha256=source_map,observer=scalar_tree(resource),observer_identity=ident(a.resource),log=ident(a.log),
        runtime=summary['runtime'],named_results=stages,verified_outputs=126,verified_events=116608,
        all_original_outputs_and_events_bitwise_identical=True,
        timing_scope='Stage kernel_seconds includes exact V8 scalar and full trace callbacks. Whole observer time includes parsing/collection. Neither is a null-trace native long-double performance benchmark.',
        precision_scope='Runtime ABI/storage/FE/x87 were read, but only double arithmetic plus original V8 scalar functions was invoked. The long-double branch and native math functions remain untested here.',
        outstanding=dict(longdouble_state_only_fullJac_identity=True,longdouble_MP90_accuracy=True,
            independent_full40_variational_reference=True,native_runtime_math_library_identity=True,
            null_trace_native_performance=True,whole_2304_batch_and_original_DN=True),
        production_installed=False,new_actual_tail_accepted=False,
        data_policy='Only compact source/input/output identities and scalar original-byte evidence are published; complete states/events stay scratch-only.')
    encoded=json.dumps(output,ensure_ascii=False,indent=2)+'\n'
    if len(encoded.encode())>=100000:raise ValueError('Record exceeds100KB')
    a.out.write_text(encoded);print(json.dumps(dict(bytes=a.out.stat().st_size,sha256=sha(a.out))))


if __name__=='__main__':main()
