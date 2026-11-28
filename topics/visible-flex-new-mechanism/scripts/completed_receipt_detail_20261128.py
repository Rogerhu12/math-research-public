#!/usr/bin/env python3
"""Read the verified receipt archive and the single naturally completed R714 log."""
import ast
from collections import Counter
from contextlib import ExitStack
import gzip
import hashlib
import io
import json
import math
import os
from pathlib import Path
import re
import struct
import tempfile
import time
import zipfile

HERE=Path(__file__).resolve().parent
PARENT=HERE/'completed_receipt_recovery_20261128.py'
if hashlib.sha256(PARENT.read_bytes()).hexdigest()!='c4c11a492e0aa6c066a98b09e99b6615ca9d903502890034ce98f832bfd321e8':
    raise RuntimeError('Pinned receipt parser differs')
from completed_receipt_recovery_20261128 import TARGETS, STAMP, enc, get, file_sha, sha, vector, verify

OUT=Path('completed-receipt-details')
ARCHIVE=(15268777040,46158534504,'1858f6a734922868935e9fffa853ec0c4a72b1ce',5268344,
         '4984be237dfef952f2e1406b67c42ddeb072344790fe1ecb490eb46bc1bc84c0')
R714=(46154358456,141007604570,'015a97501eeea47636826c4fe655a5dbf89d8c98')
BUDGET={'R631':9500,'R643':11200,'R707':8200,'R705':18700,'R714':14100,
        'R695':4800,'R702':4800,'R711':1000,'R703':1000}
HISTORY=('history','stage_records','outer_records','factor_receipts','reconstruction_attempts',
         'accepted_history','failed_attempts','attempt_receipts','remaining_unprocessed_candidates','peaks',
         'actual_working_field_orbit_rows','actual_complete_required_peak_orbits')


def desc(v):
    data=enc(v)
    out={'canonical_bytes':len(data),'canonical_sha256':sha(data)}
    if isinstance(v,(dict,list,str)):
        out['entries']=len(v)
    if isinstance(v,list):
        dims=[]
        level=[v]
        while level and all(isinstance(row,list) for row in level):
            n=len(level[0])
            if any(len(row)!=n for row in level):
                out['ragged_after_axes']=len(dims)
                break
            dims.append(n)
            level=[w for row in level for w in row]
        out['common_shape']=dims
    return out


def project(v,key=''):
    # Every dictionary key in the chosen original record survives. Long numeric
    # arrays and repetitive history retain their exact canonical object identities.
    if isinstance(v,dict):
        return {k:project(w,k) for k,w in v.items()}
    if isinstance(v,list):
        if len(v)>12 and (all(not isinstance(w,dict) for w in v)
                          or any(a in key.lower() for a in HISTORY)):
            return {'array_receipt':desc(v)}
        return [project(w,key) for w in v]
    if isinstance(v,str) and len(v)>2200:
        return {'text_receipt':desc(v)}
    if isinstance(v,float) and not math.isfinite(v):
        return {'original_nonfinite_scalar':repr(v)}
    return v


def pick(v,names):
    return {k:v[k] for k in names.split() if k in v}


def prior_key(k):
    k=k.lower()
    return any(p in k for p in ('prior','older','inherited','not_counted_as_new','preceding','old_cost','brought_forward'))


def last_records(v):
    if isinstance(v,list):
        return {'count':len(v),'identity':desc(v),'last':v[-1] if v else None}
    return v


def cost_fields(f):
    current={}
    inherited={}
    for k,v in f.items():
        if prior_key(k):
            inherited[k]=desc(v)
        elif any(x in k.lower() for x in ('cost','count','fees','seconds','clock','calls','rejections','new_work')):
            current[k]=v
    return {'original_current_fields':current,'ancestral_receipt_identities':inherited,
            'current_and_ancestor_counters_may_overlap':True}


def split_cost(cost):
    if not isinstance(cost,dict):
        return cost
    return {'original_current_fields':{k:v for k,v in cost.items() if not prior_key(k)},
            'ancestor_field_receipts':{k:desc(v) for k,v in cost.items() if prior_key(k)}}


def fit(v,budget,path=''):
    # Bounded stdout always points back to the *complete recursive projection*
    # in the corresponding artifact. Keep sibling fields present where possible.
    if len(enc(v))<=budget:
        return v
    ref={'whole_in_report':path or '/','bytes':len(enc(v))}
    if not isinstance(v,(list,dict)) or budget<160:
        return ref
    pairs=list(v.items()) if isinstance(v,dict) else list(enumerate(v))
    if not pairs:
        return v
    costs=[len(enc(w)) for _,w in pairs]
    overhead=sum(len(enc(str(k)))+2 for k,_ in pairs)+32
    cap=max(0,budget-overhead)
    lo,hi=0,max(costs)
    while lo<hi:
        m=(lo+hi+1)//2
        if sum(min(n,m) for n in costs)<=cap:
            lo=m
        else:
            hi=m-1
    out={k:fit(w,min(n,lo),path+'/'+str(k)) for (k,w),n in zip(pairs,costs)}
    obj=out if isinstance(v,dict) else list(out.values())
    if len(enc(obj))<=budget:
        return obj
    # Fill partial fields in producer-independent order of size. All missing
    # names and their exact values remain in the artifact path.
    out={'whole_in_report':path or '/'}
    for k,w in sorted(pairs,key=lambda x:len(enc(x[1]))):
        vv=fit(w,min(max(100,cap//max(1,len(pairs))),len(enc(w))),path+'/'+str(k))
        if len(enc({**out,str(k):vv}))<=budget:
            out[str(k)]=vv
    return out


def check_archive(tmp):
    aid,rid,head,size,want=ARCHIVE
    run=get(f'/actions/runs/{rid}')
    meta=get(f'/actions/artifacts/{aid}')
    if (run['status']!='completed' or run['conclusion']!='success' or run['run_attempt']!=1
            or run['id']!=rid or run['head_sha']!=head or meta['id']!=aid or meta['expired']
            or meta['name']!=f'visible-completed-receipts-{rid}-1' or meta['size_in_bytes']!=size
            or meta['workflow_run']['id']!=rid or meta['workflow_run']['head_sha']!=head
            or meta['digest']!='sha256:'+want):
        raise ValueError('Wrong original receiver run or artifact')
    p=tmp/'receipts.zip'
    get(f'/actions/artifacts/{aid}/zip',p)
    if p.stat().st_size!=size or file_sha(p)!=want:
        raise ValueError('Recovery artifact bytes differ')
    return p


def zipnames(z):
    names=z.namelist()
    if len(names)!=len(set(names)):
        raise ValueError('Duplicate artifact entry')
    return names


def journal(archive, label):
    rows={}
    with gzip.GzipFile(fileobj=io.BytesIO(archive.read(label+'/paid-events.jsonl.gz'))) as stream:
        for line in stream:
            name,sep,literal=line.rstrip(b'\r\n').partition(b' ')
            if sep and name in (b'R705_PAID_OBJECT',b'R705_R709_CONTINUOUS_PHYSICAL_STRIP',b'R705_NEW_ATLAS'):
                rows.setdefault(name.decode(),[]).append(json.loads(literal))
    return rows


def npz_headers(data,current_q_sha):
    arrays={}
    with zipfile.ZipFile(io.BytesIO(data)) as npz:
        for nm in zipnames(npz):
            if not nm.endswith('.npy'):
                raise ValueError('Unexpected member in numerical archive')
            with npz.open(nm) as part:
                if part.read(6)!=b'\x93NUMPY':
                    raise ValueError('Unexpected numerical header')
                ver=part.read(2)
                if ver not in (b'\x01\x00',b'\x02\x00',b'\x03\x00'):
                    raise ValueError('Unknown NPY version')
                n=int.from_bytes(part.read(2 if ver[0]==1 else 4),'little')
                if n>1<<20:
                    raise ValueError('Oversized array header')
                hd=ast.literal_eval(part.read(n).decode('utf-8' if ver[0]==3 else 'latin1'))
                measured=hashlib.sha256()
                total=0
                while block:=part.read(262144):
                    measured.update(block)
                    total+=len(block)
                rec=dict(shape=list(hd['shape']),dtype=hd['descr'],fortran_order=hd['fortran_order'],
                         stored_payload_bytes=total,stored_payload_sha256=measured.hexdigest())
                if nm=='q.npy':
                    rec['matches_terminal_packed_q']=hd['descr']=='<f8' and not hd['fortran_order'] and measured.hexdigest()==current_q_sha
                arrays[nm]=rec
    return arrays


def r705_detail(f,z):
    events=journal(z,'R705')
    pbytes=z.read('R705/original-paid-state.zip')
    if len(pbytes)!=494659 or sha(pbytes)!='d621875382f6a4fa6aff05b478f41644b4f846fdd19d8c03466da43216c1de90':
        raise ValueError('Original R705 solver state ZIP differs')
    latest={r['file']:r for r in events.get('R705_PAID_OBJECT',[])}
    op={}
    with zipfile.ZipFile(io.BytesIO(pbytes)) as original:
        for nm in zipnames(original):
            if nm.endswith('/'):
                continue
            b=original.read(nm)
            name=Path(nm).name
            if name.endswith('.npz'):
                receipt=latest[name]
                if (len(b),sha(b))!=(receipt['bytes'],receipt['sha256']):
                    raise ValueError('Wrong paid operator for '+name)
                op[name]={'original_file_sha256':sha(b),'arrays':npz_headers(b,f['packed_le_float64_sha256'])}
            elif name=='current.json':
                op[name]={'same_as_terminal':json.loads(b)==f,'bytes':len(b),'sha256':sha(b)}
    for name in latest:
        if name not in op:
            raise ValueError('Latest paid state absent from original ZIP: '+name)
    out={'actual_work_and_independent':{},'existing_operator_FILES':op,'counts_and_clock':pick(f,'status new_work elapsed next_damping damping_and_line_search'),
         'R709_paid_strip_rows':events.get('R705_R709_CONTINUOUS_PHYSICAL_STRIP',[]),'real_material_grids':events.get('R705_NEW_ATLAS',[])}
    for key,expected in (('coarse',[0,.3,.65,1]),('independent',[0,.15,.3,.475,.65,.825,1])):
        rows=f[key]['phases']
        if [a['phase'] for a in rows]!=expected:
            raise ValueError('Unexpected R705 '+key+' phase labels')
        out['actual_work_and_independent'][key]=f[key]
    return out


def details(label,f,z):
    if label=='R705':
        return r705_detail(f,z)
    if label=='R631':
        return dict(terminal=pick(f,'status failure actual_accepted_Newton_steps actual_next_damping elapsed_seconds'),
                    actual_complete_or_partial_final_readout=f.get('complete_or_partial_final_readout'),
                    pending_actual_trial_not_accepted=f.get('pending_actual_trial_not_accepted'),costs=cost_fields(f))
    if label=='R643':
        return dict(terminal=pick(f,'status failure elapsed_seconds actual_total_accepted_steps actual_new_accepted_steps actual_next_damping prior_quarter_trial_resolved'),
                    paid_partial_readout=f.get('partial_readout'),complete_final_readout=f.get('complete_final_readout'),
                    pending_trial_not_accepted=f.get('pending_trial_not_accepted'),
                    actual_hourly_rule_receipts=f.get('hourly_actual_public_rules_pull_receipts'),
                    actual_start_rule_source=pick(json.loads(z.read('R643/source.json')),'source_commit public_rules_read_commit private_rules_read_commit request_sha256'),
                    old_scope_science_restarted=False,rule_failure_evidence='Only the saved source and terminal fields. A textual diff not retained there cannot be inferred.',
                    last_failed_attempt=last_records(f.get('failed_attempts_and_partial_readouts')),
                    actual_same_object_tail_extension=f.get('same_object_R648_R650_true_tail_extension'),
                    costs=cost_fields(f))
    if label=='R707':
        held=f.get('actual_retained_state')
        return dict(retained=held,last_assessed_trial_separate=f.get('last_completed_full_scan_trial'),
                    constructed_and_pending_grids=pick(f,'actual_grid_p actual_retained_p actual_constraint_radial_nodes actual_constraint_theta_nodes actual_fine_radial_nodes actual_fine_theta_nodes proposed_constraint_radial_nodes proposed_constraint_theta_nodes pending_radial_nodes pending_angular_upgrade actual_backend_trust proposed_next_trust'),
                    stage=last_records(f.get('stage_records')),outer=last_records(f.get('outer_records')),
                    decision_and_disposition=pick(f,'reason termination phase stage outer original_ada2_pending_identity paid_fine_prefix_artifact original_ada2_missing_prefix_debt_not_erased_by_new_partition'),
                    other_terminal_fine_fields={k:v for k,v in f.items() if ('fine' in k or 'peak' in k) and k not in ('actual_fine_radial_nodes',)},
                    costs=cost_fields(f))
    if label in ('R695','R702'):
        return dict(terminal=pick(f,'status exception actual_last_complete_true_state_identity total_aligned_acceptances prior_aligned_acceptances fixed_original_acceptances_before_this_run last_trust last_damping'),
                    genuine_fine=f.get('fixed_actual_curve_refinement'),last_completed_observation=f.get('actual_last_complete_true_observation'),
                    current_solver=f.get('solver_counters'),inflight_trial=f.get('inflight_trial'),
                    exact_material_tree_cost=f.get('physical_material_tree_cost'),costs=cost_fields(f))
    return dict(actual_crossed=f.get('independent_crossed'),terminal=pick(f,'actual_q actual_space attempted_level actual_accepted accepted elapsed_seconds counts continuous_metric_certified continuous_t_verified README_completion_claim'))


def r714(tmp):
    rid,jid,head=R714
    verify('R714',rid,jid,head)
    folder=OUT/'R714'
    folder.mkdir()
    raw=tmp/'r714.log'
    get(f'/actions/jobs/{jid}/logs',raw)
    rawmeta={'run':rid,'job':jid,'head':head,'raw_log_bytes':raw.stat().st_size,'raw_log_sha256':file_sha(raw),'original_log_requests':1}
    (folder/'log-identity.json').write_bytes(enc(rawmeta))
    source=None
    final=None
    partials={}
    terminal_count=0
    with raw.open('rb') as stream:
        for line in stream:
            body=STAMP.sub(b'',line.rstrip(b'\n\r'),count=1)
            tag,sep,literal=body.partition(b' ')
            if not sep:
                continue
            if tag==b'INVERSE_ACTIONS_SOURCE':
                if source is not None:
                    raise ValueError('Duplicate R714 source')
                (folder/'source.json').write_bytes(literal)
                source=json.loads(literal)
            elif tag==b'WORKING_ROWS_FINAL':
                terminal_count+=1
                if terminal_count>1:
                    raise ValueError('Duplicate R714 science terminal')
                (folder/'final.json').write_bytes(literal)
                final=json.loads(literal)
            elif re.fullmatch(rb'[A-Z_0-9]*PARTIAL[A-Z_0-9]*',tag) and literal.startswith(b'{'):
                name=tag.decode()
                rec=partials.setdefault(name,{'occurrences':0})
                rec.update(occurrences=rec['occurrences']+1,last_literal_bytes=len(literal),last_literal_sha256=sha(literal))
                (folder/(name+'.last.json')).write_bytes(literal)
    raw.unlink()
    if not isinstance(final,dict) or not isinstance(source,dict):
        raise ValueError('R714 actual source or terminal missing')
    if source['source_commit']!=head or str(source['run_id'])!=str(rid) or str(source['run_attempt'])!='1':
        raise ValueError('Actual R714 source differs')
    if final['schema']!='r714-actual516-original4261-angular-queue-and-full-physical-continuation-v1':
        raise ValueError('Wrong R714 science schema')
    held=vector(final['actual_retained_q'])
    if held.get('packed_le_float64_sha256')!=final['actual_q_binary64_sha256']:
        raise ValueError('Actual retained R714 q identity differs')
    fpath=folder/'final.json'
    identity=dict(**rawmeta,request_sha256=source['request_sha256'],literal_FINAL_bytes=fpath.stat().st_size,literal_FINAL_sha256=file_sha(fpath))
    d=dict(retained={'q_identity':held,**pick(final,'actual_retained_qualification actual_retained_observed_peak_summary actual_retained_geometry_margin_state actual_backend_local_trust retained_qualification_fine_radial_nodes retained_qualification_fine_radial_nodes_binary64_sha256')},
           last_trial_not_implicitly_accepted=final.get('last_trial_not_implicitly_accepted'),
           raw_backend_trial_separate=final.get('last_raw_backend_trial_not_implicitly_accepted'),
           current=pick(final,'reason outer phase actual_required_fine_radial_nodes actual_required_fine_radial_nodes_binary64_sha256 actual_uniform_angles_and_FFT_nodes recorded_unapplied_physical_peak_orbits recorded_unapplied_working_rows proposed_next_local_trust post_backend_trust_decision_completed last_working_backtrack'),
           actual_saved_queue_resolution=final.get('source_r714_saved_queue_receipt'),cost=split_cost(final.get('cost')),
           remaining_partial_event_receipts=partials)
    return identity,d


def anchors(v):
    if not isinstance(v,dict):
        return v
    return {k:w for k,w in v.items() if not isinstance(w,(dict,list)) or isinstance(w,list) and len(w)<=4 and all(not isinstance(a,(list,dict)) for a in w)}


def stdout_detail(label,d):
    if label=='R705':
        rows=d['actual_work_and_independent']
        return dict(work=rows['coarse'],independent=rows['independent'],stored_operators=d['existing_operator_FILES'],
                    readout_cost=d['counts_and_clock'])
    if label=='R631':
        return pick(d,'actual_complete_or_partial_final_readout terminal pending_actual_trial_not_accepted')
    if label=='R643':
        return pick(d,'paid_partial_readout complete_final_readout terminal pending_trial_not_accepted actual_hourly_rule_receipts last_failed_attempt rule_failure_evidence')
    if label=='R707':
        return dict(retained=d['retained'],grids=d['constructed_and_pending_grids'],decision=d['decision_and_disposition'],
                    actual_cost=d['costs']['original_current_fields'],
                    last_trial_anchors=anchors(d['last_assessed_trial_separate']),last_outer=anchors((d['outer'] or {}).get('last')))
    if label=='R714':
        return dict(retained=d['retained'],queue=d['actual_saved_queue_resolution'],current=d['current'],
                    actual_last_trial=anchors(d['last_trial_not_implicitly_accepted']),actual_raw_backend=anchors(d['raw_backend_trial_separate']),
                    last_trial_fine=(d['last_trial_not_implicitly_accepted'] or {}).get('full_fine_scan'),
                    last_trial_peak=(d['last_trial_not_implicitly_accepted'] or {}).get('observed_peaks'),
                    cost=d['cost'],partials=d['remaining_partial_event_receipts'])
    if label in ('R695','R702'):
        return dict(terminal=d['terminal'],genuine_fine=d['genuine_fine'],all_solver_counters=d['current_solver'],
                    costs=d['costs']['original_current_fields'])
    return d


def mandatory(label,d):
    if label=='R705':
        cols=['phase','actual_sigma','max_two_sided_normal_chord_ratio','attaining_pair','physical_points',
              'max_relative_gram','max_abs_window_principal','min_window_sine_squared','max_cartesian_curl',
              'raw_period_components','max_raw_two_port_components']
        return {'columns':cols,**{k:[[p.get(c) for c in cols] for p in v['phases']]
                                   for k,v in d['actual_work_and_independent'].items()},
                'actual_operator_types':{k:{a:r.get('shape') for a,r in v.get('arrays',{}).items()}
                                         for k,v in d['existing_operator_FILES'].items()}}
    if label=='R631':
        rd=d['actual_complete_or_partial_final_readout']
        return {'fine':anchors((rd or {}).get('fine')),'readout_status':(rd or {}).get('status')}
    if label=='R643':
        p=d['paid_partial_readout']
        return {'stage':(p or {}).get('stage'),'fine':anchors((p or {}).get('fine')),
                'hourly_rules':d['actual_hourly_rule_receipts'],'actual_failure':d['terminal'].get('failure')}
    if label=='R707':
        r=d['retained'] or {}
        return {'retained_q_identity':r.get('q_identity'),'retained_scan':anchors(r.get('scan'))}
    if label=='R714':
        trial=d['last_trial_not_implicitly_accepted'] or {}
        raw=d['raw_backend_trial_separate'] or {}
        return {'retained_q':d['retained']['q_identity'],'trial_q':trial.get('q_binary64_sha256'),
                'separate_raw_q':raw.get('q_binary64_sha256'),'previous_4261_disposition':d['actual_saved_queue_resolution'],
                'unresolved_partial_artifact_fields':d['remaining_partial_event_receipts']}
    return {}


def main():
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY','').lower()!='rogerhu12/math-research-public':
        raise RuntimeError('Bound public recovery workflow required')
    start=time.monotonic()
    OUT.mkdir()
    rows={}
    faults=[]
    with tempfile.TemporaryDirectory() as td,ExitStack() as stack:
        tmp=Path(td)
        z=stack.enter_context(zipfile.ZipFile(check_archive(tmp)))
        zipnames(z)
        batch=json.loads(z.read('summary.json'))
        if batch.get('failures') or batch.get('new_scientific_evaluations')!=0:
            raise ValueError('Original receiver did not close all fixed identities')
        prior={r['label']:r for r in batch['records']}
        if set(prior)!={t[0] for t in TARGETS}:
            raise ValueError('Wrong fixed recovered set')
        for t in (*TARGETS,('R714',*R714,'WORKING_ROWS_FINAL')):
            label=t[0]
            before=time.monotonic()
            try:
                if label=='R714':
                    ident,d=r714(tmp)
                else:
                    s=prior[label]
                    if (s['run'],s['job'],s['head'],s['attempt'])!=(t[1],t[2],t[3],1):
                        raise ValueError('Wrong source identity in original receiver')
                    literal=z.read(label+'/final.json')
                    if (len(literal),sha(literal))!=(s['literal_FINAL_bytes'],s['literal_FINAL_sha256']):
                        raise ValueError('Archived literal does not match original receipt')
                    ident=pick(s,'literal_FINAL_bytes literal_FINAL_sha256 head job run raw_log_bytes raw_log_sha256')
                    f=json.loads(literal)
                    d=details(label,f,z)
                entire=project(d)
                path=OUT/(label+'-details.json')
                path.write_bytes(enc(entire))
                must=project(mandatory(label,d))
                main_budget=max(900,BUDGET[label]-len(enc(must)))
                view=fit(project(stdout_detail(label,d)),main_budget)
                rows[label]={'identity':ident,'artifact_report':path.name,'artifact_report_sha256':file_sha(path),
                             'mandatory_original_readouts':must,'report':view,'recovery_seconds':time.monotonic()-before}
            except Exception as e:
                faults.append(dict(label=label,error=type(e).__name__,message=str(e)[:350],recovery_seconds=time.monotonic()-before))
    data={'schema':'actual-completed-detail-and-R714-v1','receiver_artifact_sha256':ARCHIVE[-1],
          'new_scientific_evaluations':0,'original_eight_job_log_requests':0,'records':rows,'failures':faults,
          'recovery_elapsed_seconds':time.monotonic()-start}
    raw=enc(data)
    if len(raw)>79300:
        for label in ('R711','R703','R695','R702','R714','R707','R705'):
            if label in rows:
                rows[label]['report']=fit(rows[label]['report'],BUDGET[label]*4//5)
            raw=enc(data)
            if len(raw)<=79300:
                break
    if len(raw)>79300:
        raise ValueError('Detailed readout exceeds 79,300 bytes')
    (OUT/'summary.json').write_bytes(raw)
    print('COMPLETED_RECEIPT_DETAIL '+raw.decode(),flush=True)
    if faults:
        raise SystemExit(1)


if __name__=='__main__':
    main()
