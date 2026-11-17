#!/usr/bin/env python3
"""Reuse every complete 97a707 support piece; call only its missing fixed slots.

The mathematical reader f115 and the original 819-piece plan are unchanged.
This recovery includes the five original representatives among the reused
reports, never calls a completed piece again, and does not recompute lambda.
"""
import argparse,hashlib,importlib.util,json,math,os,resource,time,traceback
from pathlib import Path

BATCH_SHA='97a707839c3ef45fb47ae9a9d844e0f8f293cb65b4cdd481f84bc48079740f0f'
PLAN_SHA='a2acf3719692e360f8e5a4d0dce1777882494a05286700ae82c5ff7a5561899b'
REP_SHA='48d5d0523e0fb3d0d850ccc543cdc25d74feab387c002354fbf85a99f0b03e52'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def inspect(a,B,reader,self_sha):
    if sha(a.plan)!=PLAN_SHA or json.loads(a.plan.read_bytes())!=B.planned(a,reader,BATCH_SHA):
        raise ValueError('Original fixed 819-piece plan changed')
    if sha(a.representatives)!=REP_SHA:raise ValueError('Original five representatives changed')
    _,representatives=B.validate_representatives(a.representatives,reader)
    if (a.prior/'result.json').exists():raise ValueError('Prior batch already has a terminal')
    progress=json.loads((a.prior/'progress.json').read_bytes())
    if progress['source_sha256']!=BATCH_SHA or progress['plan_sha256']!=PLAN_SHA:
        raise ValueError('Different interrupted support batch')
    metadata=reader.metadata();records=[];pending=False;first=True
    for key in B.ORDER:
        row=reader.scaling[key];p=a.prior/f'cell-{key[0]:04d}-{key[1]}.json'
        identity=dict(path=str(p),sha256=sha(p)if p.exists()else None)
        record=None
        if p.exists():
            try:record=json.loads(p.read_bytes())
            except (ValueError,UnicodeDecodeError):identity['incomplete_json']=True
        if record is None:
            if key in representatives:raise ValueError('An already-paid representative is missing')
            pending=True;records.append(dict(cell=key[0],part=key[1],action='execute_once',old=identity,
                reason='interrupted_or_unresolved_call'if first else'not_reached'));first=False;continue
        if not isinstance(record,dict)or (record.get('cell'),record.get('part'))!=key:
            raise ValueError('Complete support report has a wrong address')
        if pending and key not in representatives:
            raise ValueError('A later complete nonrepresentative follows a missing earlier slot')
        if key in representatives and record!=representatives[key]:
            raise ValueError('Original representative values changed')
        if record.get('status')=='exception':
            if record.get('source_sha256')!=BATCH_SHA or record.get('scaling_certificate')!=row:
                raise ValueError('Unbound completed exception')
        else:
            if any(record.get(k)!=v for k,v in metadata.items()):
                raise ValueError('Different fixed reader/candidate/parameters')
            if record.get('scaling_certificate')!=row or any(record.get(k)!=row[k]for k in ('left_exact','right_exact')):
                raise ValueError('Different exact piece or paid normalization evidence')
            if any(record.get(k)is not True for k in ('all_radius_and_angle_covered','strict_under_stated_IEEE_arithmetic','original_width_used_for_derivatives')):
                raise ValueError('Incomplete scientific coverage report')
            if record.get('status')=='certified':
                if record.get('normal_nonzero_certified')is not True or record.get('positive_weighted_support_certified')is not True:
                    raise ValueError('Contradictory positive status')
                if not math.isfinite(record['support_lower'])or record['support_lower']<=0:
                    raise ValueError('Invalid positive support bound')
            elif record.get('status')!='enclosure_did_not_certify_positive_support':
                raise ValueError('Unknown completed report status')
        records.append(dict(cell=key[0],part=key[1],action='reuse',old=identity,
                            status=record['status'],support_lower=record.get('support_lower'),
                            original_representative=key in representatives))
    complete=sum(r['action']=='reuse'for r in records)
    if complete<progress['completed']:raise ValueError('A previously completed report disappeared')
    return dict(schema='fixed-weighted-support-recovery-manifest-v1',source_sha256=self_sha,
        first_batch_source_sha256=BATCH_SHA,reader_source_sha256=B.READER_SHA,
        original_plan_sha256=PLAN_SHA,original_representatives_sha256=REP_SHA,
        input_sha256=metadata['input_sha256'],records=records,
        prior_progress_sha256=sha(a.prior/'progress.json'),prior_reported_completed=progress['completed'],
        prior_active_call=json.loads((a.prior/'active-call.json').read_bytes()),
        counts=dict(planned=819,reused_complete=complete,original_representative_reuses=5,
                    remaining_geometry_calls=819-complete,new_lambda_evaluations=0),
        mathematical_parameters_changed=False,completed_slots_recomputed=False,
        interruption_cause='tool session unknown, reports stopped, no matching OS worker; no terminal')

def execute(a,B,reader,manifest,self_sha):
    if a.outdir.exists():raise ValueError('Recovery output directory must be new')
    a.outdir.mkdir(parents=True);manifest_sha=sha(a.manifest)
    B.save(a.outdir/'manifest.json',manifest)
    begin=time.perf_counter();entries=[];calls=0;exceptions=0;fatal=None
    journal=(a.outdir/'journal.jsonl').open('x')
    def event(value):
        value=dict(utc_time=time.time(),**value)
        journal.write(json.dumps(value,allow_nan=False)+'\n');journal.flush();os.fsync(journal.fileno())
        print(json.dumps(value,allow_nan=False),flush=True)
    def guard():
        if sha(__file__)!=self_sha or sha(a.batch_source)!=BATCH_SHA or sha(a.manifest)!=manifest_sha:
            raise ValueError('Frozen bookkeeping source or manifest changed')
        if sha(a.plan)!=PLAN_SHA or sha(a.representatives)!=REP_SHA:
            raise ValueError('Frozen scientific plan or five representatives changed')
        if sha(a.prior/'progress.json')!=manifest['prior_progress_sha256']:
            raise ValueError('Earlier worker changed durable recovery evidence')
        reader.assert_bindings()
    def state(final=False):
        good=[e for e in entries if e['status']=='certified'];bad=[e for e in entries if e['status']!='certified']
        return dict(schema='fixed-weighted-support-recovery-result-v1'if final else'fixed-weighted-support-recovery-progress-v1',
            source_sha256=self_sha,manifest_sha256=manifest_sha,first_batch_source_sha256=BATCH_SHA,
            reader_source_sha256=B.READER_SHA,original_plan_sha256=PLAN_SHA,
            input_sha256=reader.metadata()['input_sha256'],planned=819,completed=len(entries),remaining=819-len(entries),
            counts=dict(reused_complete=sum(e['action']=='prior_report_reused'for e in entries),
                        original_representative_reuses=5,new_geometry_calls=calls,new_exceptions=exceptions,new_lambda_evaluations=0),
            failures=len(bad),minimum=min(good,key=lambda e:e['support_lower'])if good else None,
            fatal=fatal,complete_scope_certified=bool(final and len(entries)==819 and not bad and fatal is None),
            closed_surface=False,reach_certified=False,seconds=time.perf_counter()-begin,
            maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    try:
        for rec in manifest['records']:
            if rec['action']!='reuse':continue
            p=Path(rec['old']['path'])
            if sha(p)!=rec['old']['sha256']:raise ValueError('A complete reused report changed')
            entries.append(dict(cell=rec['cell'],part=rec['part'],status=rec['status'],action='prior_report_reused',
                report_path=str(p),report_sha256=rec['old']['sha256'],support_lower=rec['support_lower']))
        B.save(a.outdir/'progress.json',state())
        for rec in manifest['records']:
            if rec['action']=='reuse':continue
            guard();key=(rec['cell'],rec['part']);calls+=1
            event_value=dict(event='call_started',cell=key[0],part=key[1],reason=rec['reason'])
            B.save(a.outdir/'active-call.json',dict(utc_time=time.time(),**event_value));event(event_value)
            try:record=reader.certify(*key)
            except Exception as error:
                exceptions+=1;record=dict(cell=key[0],part=key[1],status='exception',support_lower=None,
                    source_sha256=self_sha,reader_source_sha256=B.READER_SHA,scaling_certificate=reader.scaling[key],
                    error_type=type(error).__name__,message=str(error),traceback=traceback.format_exc())
            p=a.outdir/f'cell-{key[0]:04d}-{key[1]}.json';B.save(p,record)
            entry=dict(cell=key[0],part=key[1],status=record['status'],action='missing_slot_executed_once',
                       report_path=str(p),report_sha256=sha(p),support_lower=record.get('support_lower'))
            entries.append(entry);B.save(a.outdir/'progress.json',state());event(dict(event='call_finished',**entry))
            guard()
        reader.assert_bindings(all_reports=True);guard()
    except Exception as error:
        fatal=dict(error_type=type(error).__name__,message=str(error),traceback=traceback.format_exc());event(dict(event='fatal',fatal=fatal))
    finally:
        entries.sort(key=lambda e:(e['cell'],0 if e['part']in ('all','before')else 1))
        result=dict(**state(final=True),entries=entries);B.save(a.outdir/'result.json',result)
        B.save(a.outdir/'progress.json',state());event(dict(event='batch_finished',completed=len(entries),failures=result['failures'],
            result_sha256=sha(a.outdir/'result.json'),fatal=fatal));journal.close()
    return 0 if result['complete_scope_certified']else 2

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for n in ('batch-source','reader','input','interval-source','gram-index','component-source','plan','representatives','prior','manifest','outdir'):
        p.add_argument('--'+n,type=Path,required=True)
    p.add_argument('--execute',action='store_true');a=p.parse_args()
    if sha(a.batch_source)!=BATCH_SHA:raise ValueError('Changed original batch source')
    spec=importlib.util.spec_from_file_location('original_97a707_support_batch',a.batch_source)
    B=importlib.util.module_from_spec(spec);spec.loader.exec_module(B)
    reader=B.load_reader(a);self_sha=sha(__file__);manifest=inspect(a,B,reader,self_sha)
    reader.assert_bindings(all_reports=True)
    if not a.execute:
        if a.manifest.exists():raise ValueError('Frozen recovery manifest exists')
        B.save(a.manifest,manifest)
        print(json.dumps(dict(mode='prepare_only_no_geometry',source_sha256=self_sha,
                              manifest_sha256=sha(a.manifest),counts=manifest['counts'])),flush=True);return 0
    if not a.manifest.exists()or json.loads(a.manifest.read_bytes())!=manifest:
        raise ValueError('Recovery manifest changed')
    return execute(a,B,reader,manifest,self_sha)

if __name__=='__main__':raise SystemExit(main())
