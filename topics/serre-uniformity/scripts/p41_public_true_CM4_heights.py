#!/usr/bin/env python3
"""Restore completed R655 chains and compute original CM4 heights in public Actions."""
import argparse
import datetime as dt
import hashlib
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import tarfile
import time
from p41_public_actions_recovery import REPO,S,TOPIC,publish,read,save,sha
from p41_ci_recover_ramified_ss47 import preserve

REQUEST=TOPIC/'notes/public-p41-true-CM4-height-request.json'
D=S/'data'


def prepare(item,base):
    prior=base/'prior';work=base/'work/f2';out=base/'output'
    prior.mkdir(parents=True,exist_ok=True);work.mkdir(parents=True,exist_ok=True);out.mkdir(parents=True,exist_ok=True)
    subprocess.run(['gh','run','download',str(item['prior_run']),'--repo','Rogerhu12/math-research-public',
        '--name',item['artifact'],'--dir',str(prior)],check=True)
    receipt=read(prior/'run-receipt.json');initial=read(prior/'public-actions-input.json');disk=item['disk_id']
    assert receipt['result']=='R655' and receipt['complete'] and receipt['exit_code']==0
    assert not receipt['F2_F3_height_computed'] and not receipt['disk_exclusion_claimed']
    assert disk in receipt['disk_ids'] and receipt['source_commit']==initial['source_commit']==item['prior_source']
    log_binding=None
    for row in receipt['files']:
        path=prior/row['file'];raw=path.read_bytes()
        if row['file']=='public-actions-run.log':
            # R655 sealed its receipt before its final success print. Bind the
            # recorded prefix AND the exact observed trailer, not an arbitrary
            # changed file. Every mathematical input keeps its complete SHA.
            assert hashlib.sha256(raw[:row['bytes']]).hexdigest()==row['sha256']
            assert raw[row['bytes']:]==b'SAVED R655 complete True\n'
            log_binding={'file':row['file'],'sealed_prefix_bytes':row['bytes'],
                'sealed_prefix_sha256':row['sha256'],'actual_bytes':len(raw),
                'actual_sha256':sha(path),'exact_trailer':'SAVED R655 complete True\\n'}
        else:
            assert sha(path)==row['sha256'] and len(raw)==row['bytes'],row['file']
    selected=['p41_true_CM4_two_based_points47.json.gz','chain/'+disk+'_multiply47.json.gz',
        'chain/'+disk+'_Abel47.json.gz',disk+'_actual_second_kind_integrals47.json.gz',
        disk+'_principal_expression47.json.gz','p41_'+disk+'_principal_transports47.tar.gz']
    records=[]
    for name in selected:
        target=work/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(prior/name,target)
        records.append({'file':name,'sha256':sha(target),'bytes':target.stat().st_size})
    archive=work/selected[-1]
    assert sha(archive)==next(x['sha256'] for x in receipt['principal_archives'] if x['disk_id']==disk)
    with tarfile.open(archive,'r:gz') as tf:
        members=tf.getmembers();assert len(members)==459
        for member in members:
            path=Path(member.name)
            assert member.isfile() and not path.is_absolute() and '..' not in path.parts
            assert path.parts==('SS-principal-transports','run_manifest47.json') or (len(path.parts)==3 and path.parts[:2]==('SS-principal-transports',disk))
            target=work/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(tf.extractfile(member).read())
    state=read(work/'chain'/ (disk+'_multiply47.json.gz'));assert state['bits_done']==state['target_bits']==304
    rc=D/'p41_true_CM4_regular_height_derivative47.json.gz';ra=D/'p41_true_CM4_regular_height_derivative47_independent.json'
    assert read(rc)['both_true_rational_CM4_disks_complete'] and read(ra)['certificate_sha256']==sha(rc)
    save(work/'restored-original-inputs.json',{'prior_result':'R655','disk_id':disk,'files':records,
        'prior_receipt_sha256':sha(prior/'run-receipt.json'),'prior_source_commit':item['prior_source']})
    source=subprocess.check_output(['git','rev-parse','HEAD'],cwd=REPO,text=True).strip()
    save(out/'public-actions-input.json',{'result':item['result'],'disk_id':disk,'request_item':item,
        'source_commit':source,'request_sha256':sha(REQUEST),'prior_receipt_sha256':sha(prior/'run-receipt.json'),
        'prior_input_sha256':sha(prior/'public-actions-input.json'),'original_chain_bits_restored':304,
        'original_driver_log_prefix_and_exact_trailer':log_binding,
        'clearing_result':'R554','joint_Laurent_certificate_sha256':sha(rc),'joint_Laurent_audit_sha256':sha(ra),
        'root_readme_sha256':sha(REPO/'README.md'),'topic_readme_sha256':sha(TOPIC/'README.md'),
        'original_chain_or_terminal_or_principal_repeated':False,'actual_T2_degree':3,
        'T2_repeated_coarse_target_retained':True,'mathematical_completion_claimed':False})


def run(item,base,budget):
    work=base/'work/f2';out=base/'output';disk=item['disk_id'];started=time.monotonic()
    command=[sys.executable,'-u',str(S/'p41_compute_true_CM4_F2_from_complete_chain47.py'),
        '--script-dir',str(S),'--work-dir',str(work),'--disk-id',disk,'--result-id',item['result']]
    error=None;code=1
    try:
        with (out/'actual_CM4_F2.log').open('w') as f:
            proc=subprocess.Popen(command,stdout=f,stderr=subprocess.STDOUT,start_new_session=True)
            try:code=proc.wait(timeout=budget*60)
            except subprocess.TimeoutExpired:
                os.killpg(proc.pid,signal.SIGTERM)
                try:proc.wait(timeout=10)
                except subprocess.TimeoutExpired:os.killpg(proc.pid,signal.SIGKILL);proc.wait()
                raise TimeoutError('CM4 height budget reached; completed new stages preserved.')
        if code:raise subprocess.CalledProcessError(code,command)
    except Exception as exc:
        error=type(exc).__name__+': '+str(exc);code=1
    finally:
        files=preserve(work,out/'f2',disk)
        receipt={'result':item['result'],'disk_id':disk,'complete':code==0,'exit_code':code,'error':error,
            'F2_files':files,'F3_files':[],'source_commit':read(out/'public-actions-input.json')['source_commit'],
            'prior_result':'R655','prior_run':item['prior_run'],'original_chain_repeated':False,
            'execution_environment':'public-repository-github-actions','workflow_run_id':os.environ.get('GITHUB_RUN_ID'),
            'finished_at_utc':dt.datetime.now(dt.timezone.utc).isoformat(),'elapsed_seconds':round(time.monotonic()-started,3)}
        poly=work/(disk+'_actual_canonical_F2_polynomial47.json.gz');audit=work/(disk+'-principal-F2-independent-audit.json')
        if poly.exists():
            value=read(poly);receipt['F2_residual_roots']=value['residual_QC_roots']
            receipt['F2_entire_disk_excluded']=value['entire_disk_excluded_for_all_four_bad_components']
        if audit.exists():receipt['F2_entire_disk_excluded_after_exact_lifting']=read(audit).get('entire_disk_excluded_by_F2_after_exact_lifting',False)
        receipt['F3_required']=bool(receipt.get('F2_residual_roots')) and not receipt.get('F2_entire_disk_excluded_after_exact_lifting',False)
        receipt['complete_F2_F3_disk_classification']=code==0 and not receipt['F3_required']
        save(out/'run-receipt.json',receipt)
    print({'result':item['result'],'complete_F2':code==0,'error':error},flush=True)
    return code


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('mode',choices=['prepare','run','publish','verify'])
    ap.add_argument('--result',required=True);ap.add_argument('--budget-minutes',type=int,default=320);args=ap.parse_args()
    item=next(v for v in read(REQUEST)['jobs'] if v['result']==args.result)
    base=Path(os.environ['RUNNER_TEMP'])/'serre-p41-true-CM4'/args.result
    if args.mode=='prepare':prepare(item,base);return 0
    if args.mode=='run':return run(item,base,args.budget_minutes)
    if args.mode=='publish':return publish(item,base/'output',artifact_prefix='serre-p41-true-CM4',omit_derived_based_points=False)
    return 0 if read(base/'output/run-receipt.json')['complete'] else 1


if __name__=='__main__':
    sys.exit(main())
