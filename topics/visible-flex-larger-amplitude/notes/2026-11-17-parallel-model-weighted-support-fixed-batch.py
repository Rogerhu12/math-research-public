#!/usr/bin/env python3
"""Bookkeeping only: five frozen representatives plus 814 fixed support pieces.

The unchanged reader f115 performs every scientific operation. This wrapper
creates the exact 819-piece plan without a Transform, then consumes a complete
five-piece representative report. A run calls each other planned piece once,
with the same Q8192, four radial subdivisions, beta=1/4 and R648 lambda bounds.
It never retries, adjusts grids, recomputes normalization, or certifies reach.
"""
import argparse
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import resource
import time
import traceback

READER_SHA='f1158760756728ed1cbbdb419ed88a8d47bea2f5fba070bf4c1d7de43d3cfe6b'
REPRESENTATIVES=[(0,'all'),(390,'all'),(498,'all'),(817,'before'),(817,'after')]
ORDER=[(i,'all')for i in range(817)]+[(817,'before'),(817,'after')]

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def encode(value):return json.dumps(value,indent=2,allow_nan=False)+'\n'

def save(path,value):
    temporary=path.with_name(path.name+'.tmp')
    with temporary.open('w')as stream:
        stream.write(encode(value));stream.flush();os.fsync(stream.fileno())
    os.replace(temporary,path)

def load_reader(args):
    if sha(args.reader)!=READER_SHA:raise ValueError('Changed frozen support reader')
    spec=importlib.util.spec_from_file_location('fixed_weighted_support_reader',args.reader)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module.Reader(args.input,args.interval_source,args.gram_index,args.component_source)

def planned(args,reader,source_sha):
    entries=[]
    for key in ORDER:
        row=reader.scaling[key]
        entries.append(dict(**row,action='reuse_representative'if key in REPRESENTATIVES else'execute_once'))
    if len(entries)!=819 or sum(e['action']=='execute_once'for e in entries)!=814:
        raise ValueError('Changed fixed operation counts')
    edge=Fraction(0)
    for e in entries:
        if Fraction(e['left_exact'])!=edge:raise ValueError('Plan has a radial gap or overlap')
        edge=Fraction(e['right_exact'])
    if edge!=1:raise ValueError('Plan does not cover the closed pulse interval')
    return dict(schema='fixed-weighted-support-plan-v1',wrapper_source_sha256=source_sha,
        reader_source_path=str(args.reader.resolve()),reader_source_sha256=READER_SHA,
        bindings=reader.bindings,field=reader.metadata(),
        representative_order=[dict(cell=i,part=p)for i,p in REPRESENTATIVES],
        planned=819,representative_reuses=5,new_geometry_calls=814,new_lambda_evaluations=0,
        exact_radial_cover=['0','1'],entries=entries,
        scientific_gate='Every declared piece has nonzero N and strict positive weighted support',
        failure_policy='Record each failed enclosure or exception; no repeat, refinement, or replacement',
        success_scope='Same open pulse image, with its phase rotations and exact reflected half',
        closed_surface=False,reach_certified=False)

def validate_representatives(path,reader):
    digest=sha(path);report=json.loads(path.read_bytes())
    metadata=reader.metadata()
    for key,value in metadata.items():
        if report.get(key)!=value:raise ValueError('Representative metadata mismatch: '+key)
    if report.get('requested_count')!=5 or report.get('mode')!='declared_pieces_executed_once':
        raise ValueError('Wrong representative scope')
    if report.get('scientific_readout_executed')is not True or report.get('all_requested_positive')is not True:
        raise ValueError('Representatives did not all certify positive support')
    records=report.get('records',[])
    if [(r.get('cell'),r.get('part'))for r in records]!=REPRESENTATIVES:
        raise ValueError('Representative order or number changed')
    for record in records:
        key=(record['cell'],record['part']);row=reader.scaling[key]
        for k,v in metadata.items():
            if record.get(k)!=v:raise ValueError('Representative record binding mismatch: '+k)
        if record.get('scaling_certificate')!=row:
            raise ValueError('Representative normalization certificate changed')
        if any(record.get(k)!=row[k]for k in ('left_exact','right_exact')):
            raise ValueError('Representative exact piece changed')
        required=('normal_nonzero_certified','positive_weighted_support_certified',
                  'all_radius_and_angle_covered','strict_under_stated_IEEE_arithmetic',
                  'original_width_used_for_derivatives')
        if any(record.get(k)is not True for k in required)or record.get('status')!='certified':
            raise ValueError('Uncertified representative record')
        if not math.isfinite(record['support_lower'])or record['support_lower']<=0:
            raise ValueError('Invalid representative support bound')
    return digest,{(r['cell'],r['part']):r for r in records}

def execute(args,reader,plan,source_sha,plan_sha):
    if args.representatives is None or args.outdir is None:
        raise ValueError('Execution requires representatives and a new output directory')
    rep_sha,reps=validate_representatives(args.representatives,reader)
    if args.outdir.exists():raise ValueError('Output directory exists; do not repeat completed calls')
    reader.assert_bindings(all_reports=True)
    args.outdir.mkdir(parents=True)
    save(args.outdir/'plan.json',plan)
    begin=time.perf_counter();entries=[];calls=0;exceptions=0;fatal=None
    journal=(args.outdir/'journal.jsonl').open('x')

    def event(value):
        value=dict(utc_time=time.time(),**value)
        journal.write(json.dumps(value,allow_nan=False)+'\n');journal.flush();os.fsync(journal.fileno())
        print(json.dumps(value,allow_nan=False),flush=True)

    def frozen():
        if sha(Path(__file__))!=source_sha or sha(args.plan)!=plan_sha:
            raise ValueError('Frozen wrapper or plan changed during batch')
        if sha(args.representatives)!=rep_sha:raise ValueError('Representative report changed')
        reader.assert_bindings()

    def state():
        good=[e for e in entries if e['status']=='certified']
        bad=[e for e in entries if e['status']!='certified']
        minimum=min(good,key=lambda e:e['support_lower'])if good else None
        complete=len(entries)==819 and not bad and fatal is None
        return dict(schema='fixed-weighted-support-batch-v1',source_sha256=source_sha,
            plan_sha256=plan_sha,reader_source_sha256=READER_SHA,
            input_sha256=reader.metadata()['input_sha256'],
            representatives_path=str(args.representatives.resolve()),representatives_sha256=rep_sha,
            planned=819,completed=len(entries),remaining=819-len(entries),
            counts=dict(representative_reuses=sum(e['action']=='representative_report_reused'for e in entries),
                        new_geometry_calls=calls,new_lambda_evaluations=0,new_exceptions=exceptions),
            failures=len(bad),minimum=minimum,complete_scope_certified=complete,fatal=fatal,
            closed_surface=False,reach_certified=False,seconds=time.perf_counter()-begin,
            maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

    def record_entry(record,path,action):
        entry=dict(cell=record['cell'],part=record['part'],status=record['status'],action=action,
                   report_path=str(path.resolve()),report_sha256=sha(path),
                   support_lower=record.get('support_lower'))
        entries.append(entry);save(args.outdir/'progress.json',state())
        event(dict(event='piece_completed',**entry,completed=len(entries)))

    try:
        for key in REPRESENTATIVES:
            record=reps[key];path=args.outdir/f'cell-{key[0]:04d}-{key[1]}.json'
            save(path,record);record_entry(record,path,'representative_report_reused')
        for key in ORDER:
            if key in reps:continue
            frozen();row=reader.scaling[key]
            if sha(row['report_path'])!=row['report_sha256']:
                raise ValueError('Current R648 scaling report changed')
            calls+=1;address=dict(cell=key[0],part=key[1],stage='continuous_weighted_support')
            save(args.outdir/'active-call.json',dict(event='call_started',utc_time=time.time(),**address))
            event(dict(event='call_started',**address))
            try:
                record=reader.certify(*key)
            except Exception as error:
                exceptions+=1
                record=dict(cell=key[0],part=key[1],status='exception',support_lower=None,
                            error_type=type(error).__name__,message=str(error),traceback=traceback.format_exc(),
                            source_sha256=source_sha,reader_source_sha256=READER_SHA,
                            scaling_certificate=row)
            path=args.outdir/f'cell-{key[0]:04d}-{key[1]}.json'
            save(path,record);record_entry(record,path,'fixed_piece_executed_once')
            frozen()
            if sha(row['report_path'])!=row['report_sha256']:
                raise ValueError('Consumed R648 scaling report changed during call')
        reader.assert_bindings(all_reports=True);frozen()
    except Exception as error:
        fatal=dict(error_type=type(error).__name__,message=str(error),traceback=traceback.format_exc())
        event(dict(event='fatal',fatal=fatal))
    finally:
        result=dict(**state(),entries=entries)
        save(args.outdir/'result.json',result);save(args.outdir/'progress.json',state())
        event(dict(event='batch_finished',completed=len(entries),failures=result['failures'],fatal=fatal,
                   report=str(args.outdir/'result.json'),report_sha256=sha(args.outdir/'result.json')))
        journal.close()
    return 0 if result['complete_scope_certified']else 2

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('reader','input','interval-source','gram-index','component-source','plan'):
        parser.add_argument('--'+name,type=Path,required=True)
    parser.add_argument('--representatives',type=Path);parser.add_argument('--outdir',type=Path)
    parser.add_argument('--execute',action='store_true');args=parser.parse_args()
    source_sha=sha(Path(__file__));reader=load_reader(args);plan=planned(args,reader,source_sha)
    reader.assert_bindings(all_reports=True)
    if not args.execute:
        if args.plan.exists():raise ValueError('Plan exists; consume its frozen bytes')
        save(args.plan,plan)
        print(json.dumps(dict(mode='metadata_only_no_new_geometry',plan=str(args.plan),
                              plan_sha256=sha(args.plan),source_sha256=source_sha,planned=819,
                              representative_reuses=5,new_geometry_calls=814)),flush=True)
        return 0
    if not args.plan.exists()or json.loads(args.plan.read_bytes())!=plan:
        raise ValueError('Execution plan differs from the frozen metadata plan')
    return execute(args,reader,plan,source_sha,sha(args.plan))

if __name__=='__main__':raise SystemExit(main())
