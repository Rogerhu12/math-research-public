#!/usr/bin/env python3
"""Restore the recorded numerical reference before the unchanged actual response.

The accepted fixed physical profile and raw state remain unchanged. The
original raw reader is still authoritative for every physical, layout,
tolerance, context, chunk and parameter identity. This wrapper only restores
the old numerical knots that an ordinary newly constructed Fixed object would
otherwise replace by final-profile normalized knots. No worker is permitted by
the original response entry; all full-field, half-step and backward gates stay.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
SELF_SHA=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
EXPECTED={
    'strong_initial_laws_disk_control_response.py':'42db431d26f8cc87b56f3e8baf38b7afba38816f701d185efd1955028afe9750',
    'root_raw_collocation.py':'e2378a1c7ee11bd9a4f90b0a46d05d550f9e97a0883dda327a5edc09593eda3f',
}
FIELDS='delta,boost_length,boost_speed,initial_speed_pulse,initial_speed_frontload,vd,vu,descending_turn_curvature'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    path=Path(path);data=path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix=='.gz' else data)


def argument(argv,name):
    if argv.count(name)!=1:
        raise ValueError('Require exactly one explicit '+name)
    return argv[argv.index(name)+1]


def main():
    parser=argparse.ArgumentParser(add_help=False,description=__doc__)
    parser.add_argument('--samechart-source-record',type=Path)
    own,remaining=parser.parse_known_args()
    for name,expected in EXPECTED.items():
        if sha(HERE/name)!=expected:
            raise ValueError('Frozen actual response interface changed: '+name)
    import strong_initial_laws_disk_control_response as entry
    if own.samechart_source_record:
        unused,transform=entry.transformed_source()
        record=dict(scope=__doc__,prepared=True,actual_response_executed=False,
            restoration_executed=False,entry_sha256=SELF_SHA,original_sources=EXPECTED,
            original_response_source_transforms=transform,
            original_raw_identity_check_is_preserved=True,
            original_source_files_and_all_MJS_unchanged=True)
        with own.samechart_source_record.open('x') as stream:
            json.dump(record,stream,indent=2);stream.write('\n')
        print(json.dumps(dict(prepared=True,actual_response_executed=False,
            file=str(own.samechart_source_record))),flush=True)
        return
    input_path=Path(argument(remaining,'--response-raw'))
    checkpoint=Path(argument(remaining,'--response-checkpoint'))
    prefix=Path(argument(remaining,'--response-out-prefix'))
    original=read(input_path);saved=read(checkpoint)
    ident=original['identity'];knots=ident['numerical_reference_knots']
    if (not ident['fixed'] or not saved['config'].get('fixed_metric') or
            saved['raw_collocation_checkpoint']['sha256']!=sha(input_path) or
            knots!=saved['numerical_meridian_chart']['reference_t'] or
            not saved.get('solver_success') or saved.get('audit_pending',True)):
        raise ValueError('The accepted same-chart fixed raw identity is required')
    if '--response-fields' not in remaining:
        remaining+=['--response-fields',FIELDS]
    metadata_only='--metadata-only' in remaining
    record=dict(scope=__doc__,entry_sha256=SELF_SHA,original_sources=EXPECTED,
        input_raw=dict(file=str(input_path),sha256=sha(input_path)),
        input_checkpoint=dict(file=str(checkpoint),sha256=sha(checkpoint)),
        numerical_reference_knots=knots,original_raw_reader_kept=True,
        metadata_only=metadata_only,read_calls=0,restored_objects=0,observations=[],
        physical_profile_or_raw_arrays_modified=False,worker_started=False)
    record_path=prefix.with_name(prefix.name+'-samechart-adapter.json')
    if record_path.exists():
        raise FileExistsError('Fresh same-chart response output prefix required')
    prefix.parent.mkdir(parents=True,exist_ok=True)
    record_path.write_text(json.dumps(record,indent=2)+'\n')
    import numpy as np
    import root_raw_collocation as raw
    numerical=np.asarray(knots,dtype=np.float64)
    if (numerical.ndim!=1 or len(numerical)<2 or numerical[0]!=0 or numerical[-1]!=1 or
            not np.isfinite(numerical).all() or np.any(np.diff(numerical)<=0)):
        raise ValueError('Recorded positive numerical reference is malformed')
    original_read,old_argv=raw.read,sys.argv
    seen=set()
    def samechart_read(path,obj,args):
        if Path(path).resolve()!=input_path.resolve():
            return original_read(path,obj,args)
        record['read_calls']+=1
        if (not obj.fixed or obj.M!=ident['modes'] or obj.nt!=ident['angular'] or
                obj.tail is not None or obj.cfg!=ident['profile'] or obj.q!=ident['gauge']):
            raise ValueError('Expected the unchanged real Fixed/Actual object before any worker')
        first=id(obj) not in seen
        before=getattr(obj,'_neck_knots',None)
        was_equal=before is not None and np.asarray(before,dtype=np.float64).tobytes()==numerical.tobytes()
        if first:
            obj._neck_knots=numerical.copy()
            obj.chart_breaks=obj._neck_knots.copy()
            obj._flow=obj._flow_key=obj._core_key=obj._initial=None
            seen.add(id(obj));record['restored_objects']+=1
        elif not was_equal:
            raise ValueError('The saved numerical reference changed after its first restoration')
        # This is the original byte/chunk/profile/context/layout identity gate,
        # not a permissive replacement of it.
        solution,accepted_record=original_read(path,obj,args)
        if raw.canonical(raw.identity(obj,args))!=raw.canonical(ident):
            raise ValueError('The original full live raw identity did not match')
        record['observations'].append(dict(call=record['read_calls'],first_for_object=first,
            constructor_reference_was_already_equal=was_equal,
            original_full_raw_reader_passed=True,
            same_recorded_numerical_reference_after_read=True))
        return solution,accepted_record
    raw.read=samechart_read;sys.argv=[old_argv[0],*remaining]
    error=None
    try:
        entry.main()
        if not metadata_only and (record['read_calls']!=2 or record['restored_objects']!=1):
            raise RuntimeError('Expected original initial restoration and inspection reads on one object')
        if metadata_only and record['read_calls']!=0:
            raise RuntimeError('Metadata-only inspection unexpectedly constructed a numerical state')
        output=prefix.with_suffix('.json')
        data=read(output)
        if not metadata_only and (not data.get('finished') or data.get('tail_worker_started')):
            raise RuntimeError('The unchanged full no-worker response did not complete')
        record['completed']=True
        data['samechart_response_adapter']=dict(record)
        data.setdefault('source_sha256',{})[str(Path(__file__))]=SELF_SHA
        temporary=output.with_name(output.name+'.samechart.tmp')
        temporary.write_text(json.dumps(data,indent=2)+'\n');temporary.replace(output)
    except BaseException as exc:
        error=repr(exc);record['completed']=False
        raise
    finally:
        raw.read=original_read;sys.argv=old_argv
        record['error']=error
        temporary=record_path.with_name(record_path.name+'.tmp')
        temporary.write_text(json.dumps(record,indent=2)+'\n');temporary.replace(record_path)


if __name__=='__main__':
    main()
