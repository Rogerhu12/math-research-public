#!/usr/bin/env python3
"""Read one naturally completed R710 log once. No scientific evaluations."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import tempfile
import time
import zipfile

HERE=Path(__file__).resolve().parent
PINS={
    'completed_receipt_recovery_20261128.py':'c4c11a492e0aa6c066a98b09e99b6615ca9d903502890034ce98f832bfd321e8',
    'completed_receipt_detail_20261128.py':'7f32ba4b50cfc92731980e55878bed2c7b252652850629d7729996b746296ecc',
}
for name,wanted in PINS.items():
    if hashlib.sha256((HERE/name).read_bytes()).hexdigest()!=wanted:
        raise RuntimeError('Pinned original receipt reader differs: '+name)
import completed_receipt_recovery_20261128 as original
from completed_receipt_detail_20261128 import project,fit,cost_fields,desc,last_records


def recover_tail(request,tmp):
    """Recover the actual completed R734 literal and complete paid journal, never its operator."""
    spec=request['paid_r734']
    rid,jid,head=spec['run'],spec['job'],spec['head']
    job,run=original.verify('R734',rid,jid,head)
    folder=original.OUT/'R734';folder.mkdir()
    path=Path(tmp)/'r734-completed.log'
    original.get(f'/actions/jobs/{jid}/logs',path)
    final=None;source=None
    for line in path.read_bytes().splitlines():
        body=original.STAMP.sub(b'',line,count=1)
        tag,_,literal=body.partition(b' ')
        if tag==b'R734_FINAL':
            if final is not None:raise ValueError('Multiple original R734 terminal records')
            if len(literal)!=spec['terminal_bytes'] or original.sha(literal)!=spec['terminal_sha256']:
                raise ValueError('Original R734 literal differs from the already read terminal')
            (folder/'final.json').write_bytes(literal);final=json.loads(literal)
        elif tag==b'INVERSE_ACTIONS_SOURCE':
            if source is not None:raise ValueError('Multiple original R734 source records')
            (folder/'source.json').write_bytes(literal);source=json.loads(literal)
    log_identity={'bytes':path.stat().st_size,'sha256':original.file_sha(path)}
    if not final or not source or source['source_commit']!=head or str(source['run_id'])!=str(rid):
        raise ValueError('Missing or mismatched original R734 source and terminal')
    aid=spec['artifact'];meta=original.get(f'/actions/artifacts/{aid}')
    if (meta['id']!=aid or meta['expired'] or meta['workflow_run']['id']!=rid or
        meta['workflow_run']['head_sha']!=head or meta['size_in_bytes']!=spec['artifact_bytes'] or
        meta['digest']!='sha256:'+spec['artifact_sha256']):
        raise ValueError('Original R734 artifact metadata differs')
    archive=folder/'original-paid.zip';original.get(f'/actions/artifacts/{aid}/zip',archive)
    if archive.stat().st_size!=spec['artifact_bytes'] or original.file_sha(archive)!=spec['artifact_sha256']:
        raise ValueError('Original R734 artifact bytes differ')
    with zipfile.ZipFile(archive) as z:
        names=z.namelist()
        if len(names)!=len(set(names)):raise ValueError('Duplicate paid archive member')
        match=[s for s in names if s=='tail.jsonl' or s.endswith('/tail.jsonl')]
        if len(match)!=1:raise ValueError('Original unique R734 journal not found')
        raw=z.read(match[0]);(folder/'tail.jsonl').write_bytes(raw)
    keys=set();seconds=0.
    for line in raw.splitlines():
        row=json.loads(line)
        if row['scientific_fingerprint']!=final['source_fingerprint'] or row['key'] in keys:
            raise ValueError('Paid R734 fingerprint or unique operation identity differs')
        keys.add(row['key']);seconds+=row['value']['seconds']
    if len(keys)!=final['paid_units']:raise ValueError('Original R734 operation count differs')
    ports={k:{'kind':v['kind'],'port':v.get('actual_cut_port'),
              'cone':v['asymptotic_cone'],'accepted_cell_lines':len(v['paid_outer_lines'])}
           for k,v in final['completed_modes'].items()}
    return {'run':rid,'job':jid,'head':head,'job_completed_at':job['completed_at'],
            'literal_FINAL_bytes':spec['terminal_bytes'],'literal_FINAL_sha256':spec['terminal_sha256'],
            'artifact':aid,'artifact_bytes':spec['artifact_bytes'],'artifact_sha256':spec['artifact_sha256'],
            'artifact_expires_at':meta['expires_at'],'original_log':log_identity,
            'journal_member':match[0],'journal_bytes':len(raw),'journal_sha256':original.sha(raw),
            'journal_unique_keys':len(keys),'scientific_fingerprint':final['source_fingerprint'],
            'original_elapsed_seconds':final['current_elapsed_seconds'],
            'original_paid_unit_seconds_sum':seconds,'original_paid_seconds_overlap_wall':True,
            'ports':ports,'new_scientific_evaluations':0}


def main():
    started=time.monotonic()
    ap=argparse.ArgumentParser()
    ap.add_argument('--request',required=True)
    args=ap.parse_args()
    if (os.environ.get('GITHUB_ACTIONS')!='true' or
        os.environ.get('GITHUB_REPOSITORY','').lower()!='rogerhu12/math-research-public'):
        raise RuntimeError('Public completed receipt receiver required')
    raw=Path(args.request).read_bytes()
    request=json.loads(raw)
    for name,wanted in request['source_sha256'].items():
        if hashlib.sha256(Path(name).read_bytes()).hexdigest()!=wanted:
            raise RuntimeError('Request source differs: '+name)
    target=('R710',46152424706,141001739618,'12071581a715b36833640670ed5780014f73bc44',
            'R710_PAID149_ORIGINAL_BRACKET_FACES_FINAL')
    if request['target']!=list(target):
        raise RuntimeError('Another old scientific scope was requested')
    original.OUT=Path('r710-completed-receipt')
    original.OUT.mkdir(exist_ok=False)
    counts={};old_get=original.get
    def measured_get(path,output=None):
        if path.endswith('/logs'):counts[path]=counts.get(path,0)+1
        return old_get(path,output)
    original.get=measured_get
    original.STATE['R710']='actual_last_complete_true_state.shape_parameters'
    original.PICK['R710']='actual_last_complete_true_state_identity actual_last_complete_true_observation fixed_actual_curve_refinement inflight_trial last_trust last_damping paid_source_pending_trial_consumption latest_exact_left_or_right_bracket_work'
    original.SIDE['R710']=('R710_','FRONTIER_ACTUAL_','INVERSE_ACTIONS_')
    error=None
    recovered=None
    tail=None
    try:
        with tempfile.TemporaryDirectory(prefix='r710-completed-log-') as folder:
            recovered=original.recover(target,folder)
        root=original.OUT/'R710'
        final=json.loads((root/'final.json').read_bytes())
        source=json.loads((root/'source.json').read_bytes())
        full=project(final)
        (root/'all-field-projection.json').write_bytes(original.enc(full))
        retained={k:final[k] for k in (
            'status','exception','actual_last_complete_true_state_identity',
            'actual_last_complete_true_observation','fixed_actual_curve_refinement',
            'last_trust','last_damping','inflight_trial','latest_restoration_including_partial',
            'inflight_restoration','latest_original_physical_cone_model',
            'paid_source_pending_trial_consumption','latest_exact_left_or_right_bracket_work',
            'paid_fixed_weight_acceptances_before_this_run','total_fixed_weight_acceptances_including_this_run',
            'solver_counters','latest_adaptive_polynomial_bounds_including_partial',
            'latest_polynomial_field_frontier_including_partial') if k in final}
        history={k:last_records(final[k]) for k in (
            'all_complete_factor_receipts_including_partial','exact_partial_and_complete_path_receipts',
            'all_new_height_bracket_suffix_receipts') if k in final}
        details={'retained':project(retained),'original_cost_fields':project(cost_fields(final)),
                 'actual_state':original.vector(final['actual_last_complete_true_state']['shape_parameters']),
                 'complete_state':desc(final['actual_last_complete_true_state']),
                 'history':project(history),'source':source,
                 'all_field_projection_sha256':original.file_sha(root/'all-field-projection.json')}
        (root/'details.json').write_bytes(original.enc(details))
        # Any producer artifact is an actual saved object, not a request to recompute.
        artifacts=original.get(f'/actions/runs/{target[1]}/artifacts?per_page=100')
        if artifacts['total_count']!=len(artifacts['artifacts']):
            raise ValueError('Unexpected original artifact pagination')
        saved=[]
        for a in artifacts['artifacts']:
            if a['expired'] or a['workflow_run']['id']!=target[1] or a['workflow_run']['head_sha']!=target[3]:
                raise ValueError('Original R710 artifact identity differs or expired')
            if not a.get('digest','').startswith('sha256:'):
                raise ValueError('Original artifact missing a byte digest')
            path=root/('original-paid-artifact-'+str(a['id'])+'.zip')
            original.get(f"/actions/artifacts/{a['id']}/zip",path)
            if path.stat().st_size!=a['size_in_bytes'] or original.file_sha(path)!=a['digest'][7:]:
                raise ValueError('Original paid artifact bytes differ')
            saved.append({k:a[k] for k in ('id','name','size_in_bytes','digest','expires_at')})
        recovered.update(detailed_original_readout=fit(details,46000),
                         details_sha256=original.file_sha(root/'details.json'),saved_original_artifacts=saved)
        with tempfile.TemporaryDirectory(prefix='r734-completed-receipt-') as folder:
            tail=recover_tail(request,folder)
    except Exception as exc:
        error={'type':type(exc).__name__,'message':str(exc)[:800]}
    summary={'schema':'r710-natural-terminal-receiver-v1','new_scientific_evaluations':0,
             'completed_original_log_requests':counts,'receiver_elapsed_seconds':time.monotonic()-started,
             'receiver_head':os.environ['GITHUB_SHA'],'receiver_run':os.environ['GITHUB_RUN_ID'],
             'request_sha256':hashlib.sha256(raw).hexdigest(),'record':recovered,'paid_R734':tail,'error':error}
    body=original.enc(summary)
    (original.OUT/'summary.json').write_bytes(body)
    print('R710_RECEIPT_SUMMARY '+body.decode(),flush=True)
    if error:raise SystemExit(1)


if __name__=='__main__':main()
