#!/usr/bin/env python3
"""Lossless scalar-only readout for the independent persistent Decimal50 search.

All actual outer/normal trials, direct forward columns, original64 projection
FD/domain/circle records and partial/error fields are retained. This reader
performs only JSON/file-byte operations; it does not evaluate a model.
Each emitted JSON block and the primary obey90000 bytes. Oversize values
are structurally segmented, never shortened or relabelled scientific success.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import uuid

LIMIT=90000
PRODUCER_NAME='geometry_20261115_small_core_nine_control_decimal_recipe.py'
PRODUCER_SHA='66906f121c52f6dc57894efa368299990eea45f2f1d4fc5e6ce4af2fc5b9536e'
MODEL_NAME='geometry_20261115_nine_control_decimal_literal_model.py'
MODEL_SHA='2422be0c2e30d10c38b56ff7b68412c5397d37ed36451676bb16acbdc142ef75'
SEARCH_NAME='geometry_20261115_nine_control_decimal_curved_search.py'
SEARCH_SHA='433d5ddd2587efa581fb28ea151ddf3cec5b6a63eb5017340375d1f19b6d98d0'
STATUS_NAME='nine-control-decimal50-status.json'
STATUS_SCHEMA='R259-nine-control-persistent-decimal50-complete-three-curved-search-v1'
VIEW_SCHEMA='original-nine-control-decimal50-complete-scalar-view-v1'
PRIMARY_SCHEMA='original-nine-control-decimal50-segmented-complete-readback-v1'
SEGMENT_SCHEMA='original-nine-control-decimal50-complete-scalar-segment-v1'


def encode(value):
    return json.dumps(value,ensure_ascii=True,allow_nan=False,sort_keys=True,
                      separators=(',',':')).encode('utf-8')


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def file_record(path,root):
    h=hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda:stream.read(1<<20),b''):
            h.update(block)
    return dict(file=str(path.relative_to(root)),bytes=path.stat().st_size,sha256=h.hexdigest())


def prepare(args):
    result=dict(schema=VIEW_SCHEMA,run_id=os.environ.get('GITHUB_RUN_ID'),
        source_commit=os.environ.get('GITHUB_SHA'),compute_step_outcome=args.compute_outcome,
        reader_performs_only_original_JSON_and_byte_operations=True,
        new_scientific_computation=False,no_additional_scientific_gate=True,
        raw_repo_Release_or_artifact_retention=False)
    path=args.directory/STATUS_NAME
    if not path.is_file():
        result.update(original_status_present=False,scientific_completion_not_claimed=True,
                      outer_searches=[])
        return result
    raw=path.read_bytes()
    original=json.loads(raw)
    if original.get('schema')!=STATUS_SCHEMA:
        raise ValueError('Require the actual independent Decimal50 producer schema')
    searches=original.get('searches',[])
    if not isinstance(searches,list) or any(not isinstance(row,dict) for row in searches):
        raise ValueError('All actual outer directions must remain an ordered original list')
    # No scalar whitelist or truncation: every field in the status survives.
    result.update({key:value for key,value in original.items() if key not in ('schema','searches')})
    result.update(schema=VIEW_SCHEMA,producer_status_schema=original['schema'],
        original_status=file_record(path,args.directory),original_status_present=True,
        status_field_mapping={'schema':'producer_status_schema','searches':'outer_searches'},
        outer_searches=searches,compute_step_outcome=args.compute_outcome)
    sources=original.get('consumed_source_sha256',{})
    wanted={PRODUCER_NAME:PRODUCER_SHA,MODEL_NAME:MODEL_SHA,SEARCH_NAME:SEARCH_SHA}
    result['readout_source_identity']=dict(
        expected=wanted,recorded={name:sources.get(name) for name in wanted},
        matches={name:sources.get(name)==sha for name,sha in wanted.items()},
        producer_top_source_matches=original.get('source_sha256')==PRODUCER_SHA,
        comparison_is_identity_readback_not_a_scientific_gate=True)
    result['temporary_file_byte_identities']=[]
    for child in sorted(args.directory.rglob('*')):
        if child.is_symlink():
            raise ValueError('Do not follow scientific-output symlinks')
        if child.is_file():
            result['temporary_file_byte_identities'].append(file_record(child,args.directory))
    result['raw_scientific_array_payloads_exported']=False
    if args.rules_directory and args.rules_directory.is_dir():
        rule=args.rules_directory
        paths=sorted(rule.glob('sync-*-completed.json'))
        if (rule/'runner-result.json').is_file():
            paths.append(rule/'runner-result.json')
        result['actual_rule_sync']=[]
        for path in paths:
            result['actual_rule_sync'].append(dict(receipt=file_record(path,rule),
                original=json.loads(path.read_bytes())))
    return result

class SegmentEmitter:
    """Lossless structural JSON transport; never evaluates numerical values.

    Each original view is a JSON value. Small values travel whole. Larger
    objects/lists use declared containers and complete child values/ranges;
    long strings use exact Unicode-index slices. A group can be reconstructed
    and canonicalized to its recorded bytes/SHA. There is no trial row cap.
    """
    def __init__(self, result):
        self.result = result
        self.reader_sha = digest(Path(__file__).read_bytes())
        self.emitted_parts = 0
        self.emitted_groups = 0

    def group(self, group_id, value, scope):
        original = encode(value)
        records = []

        def framed(operation, path, extra):
            return dict(schema=SEGMENT_SCHEMA, group_id=group_id,
                part_index=len(records), operation=operation, path=path,
                run_id=os.environ.get('GITHUB_RUN_ID'),
                source_commit=os.environ.get('GITHUB_SHA'),
                reader_source_sha256=self.reader_sha,
                original_status=self.result.get('original_status'), **extra)

        def size(operation, path, extra):
            return len(encode(framed(operation, path, extra)))

        def append(operation, path, extra):
            record = framed(operation, path, extra)
            raw = encode(record)
            if len(raw) > LIMIT:
                raise ValueError('A complete structural scalar segment exceeds its original90000-byte log limit')
            records.append((record, raw))

        def visit(item, path):
            if size('value', path, dict(value=item)) <= LIMIT:
                append('value', path, dict(value=item))
                return
            if isinstance(item, dict):
                append('begin_object', path, dict(entry_count=len(item)))
                for key in sorted(item):
                    if not isinstance(key, str):
                        raise ValueError('Original JSON object keys must be strings')
                    visit(item[key], path+[key])
            elif isinstance(item, list):
                append('begin_list', path, dict(length=len(item)))
                start, chunk = 0, []
                for index, child in enumerate(item):
                    candidate = chunk+[child]
                    extra = dict(start=start, stop=index+1, items=candidate)
                    if size('list_items', path, extra) <= LIMIT:
                        chunk = candidate
                        continue
                    if chunk:
                        append('list_items', path, dict(start=start, stop=index, items=chunk))
                        chunk = []
                    if size('list_items', path, dict(start=index, stop=index+1, items=[child])) <= LIMIT:
                        start, chunk = index, [child]
                    else:
                        visit(child, path+[index])
                        start = index+1
                if chunk:
                    append('list_items', path, dict(start=start, stop=len(item), items=chunk))
            elif isinstance(item, str):
                append('begin_string', path, dict(codepoint_length=len(item),
                    utf8_bytes=len(item.encode('utf-8')), utf8_sha256=digest(item.encode('utf-8'))))
                start = 0
                while start < len(item):
                    lower, upper = 1, len(item)-start
                    found = 0
                    while lower <= upper:
                        length = (lower+upper)//2
                        extra = dict(start=start, stop=start+length, text=item[start:start+length])
                        if size('string_slice', path, extra) <= LIMIT:
                            found = length
                            lower = length+1
                        else:
                            upper = length-1
                    if found == 0:
                        raise ValueError('One original JSON path/character exceeds framing capacity')
                    append('string_slice', path, dict(start=start, stop=start+found,
                                                     text=item[start:start+found]))
                    start += found
            else:
                # There is no lossy numeric rounding or scalar replacement.
                raise ValueError('One literal scalar cannot fit its bounded transport frame')

        visit(value, [])
        descriptors = []
        for record, raw in records:
            index = record['part_index']
            label = 'VISIBLE_NINE_DECIMAL50_'+group_id.upper().replace('-', '_')+'_PART_'+str(index).zfill(5)
            print('BEGIN_'+label, flush=True)
            print(raw.decode('utf-8'), flush=True)
            print('END_'+label, flush=True)
            descriptor = dict(part_index=index, bytes=len(raw), sha256=digest(raw),
                begin='BEGIN_'+label, end='END_'+label,
                operation=record['operation'], path=record['path'])
            for key in ('start', 'stop', 'length', 'entry_count', 'codepoint_length'):
                if key in record:
                    descriptor[key] = record[key]
            descriptors.append(descriptor)
            print(encode(dict(event='visible-nine-decimal50-scalar-segment-sha256',
                group_id=group_id, part=descriptor,
                hash_scope='UTF-8 compact segment JSON excluding separator LF',
                run_id=os.environ.get('GITHUB_RUN_ID'), source_commit=os.environ.get('GITHUB_SHA'))).decode(), flush=True)
            self.emitted_parts += 1
        self.emitted_groups += 1
        index_raw = encode(descriptors)
        return dict(group_id=group_id, scope=scope, canonical_value_bytes=len(original),
            canonical_value_sha256=digest(original),
            segment_index=dict(canonical_json_bytes=len(index_raw),
                canonical_json_sha256=digest(index_raw),
                record_source='Ordered part objects of this group in visible-nine-decimal50-scalar-segment-sha256 stdout events'),
            part_count=len(descriptors), complete_original_value_retained=True,
            group_reconstruction='Apply all declared containers/values/list ranges/string slices at exact JSON paths; encode with the original sorted compact encoder')



def segmented(result,emitter):
    complete=encode(result)
    primary=dict(result)
    searches=primary.pop('outer_searches',[])
    metadata=dict(protocol_schema='nine-control-decimal50-lossless-scalar-group-index-v1',
        original_view=dict(schema=result['schema'],canonical_json_bytes=len(complete),
                           canonical_json_sha256=digest(complete)),
        original_status=result.get('original_status'),outer_direction_groups=[],
        original_outer_direction_count=len(searches),moved_primary_fields=[],
        all_outer_and_normal_trials_retained=True,
        all_nine_physical_parameters_remain_exact_recorded_strings=True,
        original64_projection_points_and_differences_not_collapsed=True,
        all_original54_and_new54_FD_records_retained=True,
        full112_linear_rows_and_original453_projection_checks_retained=True,
        all_failure_exception_and_unvisited_suffix_records_retained=True,
        no_scientific_values_recomputed=True,no_payload_fields_omitted=True,
        per_segment_and_primary_limit_bytes=LIMIT,reader_source_sha256=emitter.reader_sha,
        reconstruction='Copy primary except segmented_readout; restore original_view.schema; reinsert outer_searches and moved_primary_fields from their exact groups; canonical encode and compare complete view SHA')
    for i,row in enumerate(searches):
        metadata['outer_direction_groups'].append(emitter.group('outer-'+str(i).zfill(3),row,
            dict(kind='complete_original_outer_direction',original_outer_index=i,
                original_iteration=row.get('iteration'),original_outer_trial_count=len(row.get('trials',[])),
                complete_normal_records_in_every_trial=True)))
    primary['schema']=PRIMARY_SCHEMA if result['schema']==VIEW_SCHEMA else 'nine-control-decimal50-partial-readout-v1'
    primary['segmented_readout']=metadata
    fixed={'schema','segmented_readout','run_id','source_commit','original_status','compute_step_outcome'}
    order=['temporary_file_byte_identities','original_zero_added_quadratic_counterfactual_at_projection',
           'initial_original_binary64_projection','final_original_binary64_projection',
           'initial','final','original_complete_circle_check_at_binary64_projection',
           'complete_scalar_domain_at_binary64_projection']
    order += [key for key in sorted(primary) if key not in fixed and key not in order]
    for key in order:
        if len(encode(primary))<=LIMIT:
            break
        if key not in primary:
            continue
        value=primary.pop(key)
        group=emitter.group('primary-'+str(len(metadata['moved_primary_fields'])).zfill(3),value,
            dict(kind='complete_named_primary_field',original_field=key))
        metadata['moved_primary_fields'].append(dict(original_field=key,group=group))
    metadata['emitted_group_count']=emitter.emitted_groups
    metadata['emitted_segment_count']=emitter.emitted_parts
    raw=encode(primary)
    if len(raw)>LIMIT:
        raise ValueError('Complete lossless group index exceeds90000 bytes; do not report complete transport')
    return raw


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory',type=Path,required=True)
    parser.add_argument('--rules-directory',type=Path)
    parser.add_argument('--compute-outcome',required=True)
    parser.add_argument('--primary-output',type=Path,required=True)
    args=parser.parse_args()
    prepared=False
    try:
        result=prepare(args)
        prepared=True
    except Exception as error:
        result=dict(schema='nine-control-decimal50-reader-exception-v1',
            run_id=os.environ.get('GITHUB_RUN_ID'),source_commit=os.environ.get('GITHUB_SHA'),
            error=repr(error)[:4000],compute_step_outcome=args.compute_outcome,
            complete_scientific_readout_not_claimed=True,outer_searches=[])
    emitter=SegmentEmitter(result)
    completed=False
    try:
        raw=segmented(result,emitter)
        completed=prepared
    except Exception as error:
        identity=None
        try:
            value=encode(result);identity=dict(bytes=len(value),sha256=digest(value))
        except Exception:
            pass
        raw=encode(dict(schema='nine-control-decimal50-transport-exception-v1',
            run_id=os.environ.get('GITHUB_RUN_ID'),source_commit=os.environ.get('GITHUB_SHA'),
            error=repr(error)[:4000],original_status=result.get('original_status'),
            original_prepared_view_identity=identity,
            emitted_groups=emitter.emitted_groups,emitted_segments=emitter.emitted_parts,
            prior_segments_remain_in_original_compute_log=True,
            complete_scalar_transport_not_claimed=True,
            scientific_failure_not_inferred_from_transport_error=True))
    args.primary_output.parent.mkdir(parents=True,exist_ok=True)
    args.primary_output.write_bytes(raw)
    if os.environ.get('GITHUB_OUTPUT'):
        token='VISIBLE_DECIMAL50_PRIMARY_'+uuid.uuid4().hex
        with open(os.environ['GITHUB_OUTPUT'],'a',encoding='utf-8') as stream:
            stream.write('scalar_summary<<'+token+'\n'+raw.decode('utf-8')+'\n'+token+'\n')
            stream.write('scalar_summary_bytes='+str(len(raw))+'\n')
            stream.write('scalar_summary_sha256='+digest(raw)+'\n')
    print('BEGIN_VISIBLE149_PRIMARY',flush=True)
    print(raw.decode('utf-8'),flush=True)
    print('END_VISIBLE149_PRIMARY',flush=True)
    print(encode(dict(event='visible149-complete-scalar-readout',bytes=len(raw),sha256=digest(raw),
        prepared_view=prepared,scalar_transport_completed=completed,
        complete_original_status_available=result.get('original_status_present',False),
        emitted_groups=emitter.emitted_groups,emitted_segments=emitter.emitted_parts,
        hash_scope='UTF-8 compact JSON string excluding separator LF',
        native_or_fullDN_acceptance_claimed=False)).decode(),flush=True)
    return 0 if completed else 70


if __name__=='__main__':
    raise SystemExit(main())
