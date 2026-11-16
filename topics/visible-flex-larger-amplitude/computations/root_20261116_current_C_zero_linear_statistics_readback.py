#!/usr/bin/env python3
"""R496 necessary original zero-eliding linear metadata, no scientific imports.

Call only from the existing readback after the original owner is observed quiet.
The stream is read in full; the last complete observation is returned. The
first record retains its identity and address without duplicating counters. A
missing stream is absent, not a zero counter or proof that native work ran.
All original counters and last_observation members keep their JSON values.
Author: OpenAI / ChatGPT amplitude agent (AI), 2026-11-16.
"""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path

SCHEMA='R496-current-C-zero-linear-necessary-statistics-v1'
RUNTIME_SCHEMA='R494-current-C-noJ-captured-product-zero-eliding-linear-v1-actual-statistics'
CALLER='geometry_20261116_current_C_noj_zero_eliding_variational_engine.mjs'
CALLER_SHA='eafb41179f08105ac2cbc2708a3db84e1a3ae14eeec67027a94d3d7db70ea3c4'
HELPER='geometry_20261116_finite_trace_zero_coefficient_linear.mjs'
HELPER_SHA='eb487b2dff111d0af543a722c0882d28f7408eeb61e4e25559cef147d2e16e02'
ANCESTOR_NOJ='f9b292c4c3f80d1d7b3030ea0350416746795377833661af8d3095e349a73ad9'
PRODUCT='205b28dbde3b43392ef8ad0a915e9f4265264f4663b5bc2a0ea34421516cfd25'

def require(ok,message):
    if not ok:raise ValueError(message)

def receipt(path):
    digest=hashlib.sha256();n=0
    with path.open('rb') as stream:
        for block in iter(lambda:stream.read(1<<20),b''):
            digest.update(block);n+=len(block)
    return dict(file=str(path),bytes=n,sha256=digest.hexdigest())

def unique(pairs):
    result={}
    for k,v in pairs:
        require(k not in result,'Duplicate metadata JSON member: '+k);result[k]=v
    return result

def read_actual_native_statistics(client_directory,expected_worker):
    require(os.environ.get('GITHUB_ACTIONS')=='true' and
        os.environ.get('GITHUB_REPOSITORY')=='Rogerhu12/math-research-public',
        'Read current native metadata only in the named public Actions')
    directory=Path(client_directory).resolve()
    root=Path(os.environ['RUNNER_TEMP']).resolve()
    require(directory!=root and root in directory.parents,'Actual owned native directory required')
    path=directory/'native'/'actual-zero-eliding-linear-statistics.jsonl'
    answer=dict(schema=SCHEMA,actual_path=str(path),exists=path.is_file(),
        expected_worker_source=expected_worker,
        original_noJ_ancestor_sha256=ANCESTOR_NOJ,unchanged_product_sha256=PRODUCT,
        all_present_original_stream_bytes_read=False,
        observations_are_last_persisted_metadata_not_a_whole_session_or_complete_J_claim=True,
        current_in_flight_call_after_last_observation_not_inferred=True,
        scientific_acceptance_or_speed_inferred=False)
    if not path.is_file():return answer
    require(not path.is_symlink() and path.resolve().parent==directory/'native',
        'Do not read a redirected metadata stream')
    before=receipt(path);first=None;last=None;count=0;locations={};calls=set()
    with path.open('rb') as stream:
        for index,raw in enumerate(stream):
            require(raw.endswith(b'\n'),'A partial final native metadata line is not silently dropped')
            value=json.loads(raw,object_pairs_hook=unique,
                parse_constant=lambda x:(_ for _ in ()).throw(ValueError(x)))
            worker=value.get('worker_source')
            require(isinstance(worker,dict) and all(worker.get(k)==expected_worker[k]
                for k in ('file','bytes','sha256')),'The actual observation worker source differs')
            statistics=value.get('statistics')
            require(isinstance(statistics,dict) and statistics.get('schema')==RUNTIME_SCHEMA,
                'The actual R494 statistics family differs')
            source=statistics.get('actual_variational_source',{})
            require(source.get('file')==CALLER and source.get('sha256')==CALLER_SHA and
                source.get('unchanged_R474_linear_helper',{}).get('file')==HELPER and
                source.get('unchanged_R474_linear_helper',{}).get('sha256')==HELPER_SHA and
                source.get('original_loaded_noJ_source',{}).get('sha256')==ANCESTOR_NOJ and
                source.get('original_product_source',{}).get('sha256')==PRODUCT,
                'Actual caller, helper, ancestor and original product are separate bound sources')
            require(isinstance(statistics.get('complete_linear_statistics'),dict),
                'Keep the complete original statistics object')
            selected=dict(original_line_index=index,original_record=value)
            if first is None:
                first=dict(original_line_index=index,original_record_bytes=len(raw),
                    original_record_sha256=hashlib.sha256(raw).hexdigest(),
                    location=value.get('location'),actual_call=value.get('actual_call'),
                    scope='identity and actual address only; no separate first counter table returned')
            last=selected;count+=1
            key=value.get('location');require(isinstance(key,str),'Actual observation location required')
            locations[key]=locations.get(key,0)+1
            call=value.get('actual_call')
            require(call is None or (type(call) is int and call>=0),'Actual original call address required')
            if call is not None:calls.add(call)
    after=receipt(path)
    require(before==after,'The native metadata stream changed while being read')
    answer.update(original_complete_stream=before,all_present_original_stream_bytes_read=True,
        original_record_count=count,original_location_counts=locations,
        number_of_distinct_present_call_addresses=len(calls),
        first_complete_observation_identity=first,last_complete_observation=last,
        every_original_last_statistics_field_preserved=True,
        no_counter_sum_reset_or_scientific_recomputation=True)
    return answer
