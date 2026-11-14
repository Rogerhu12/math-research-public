#!/usr/bin/env python3
"""Compute only missing true-CM4 F3 stages from the completed public R656 F2."""
import argparse
import datetime as dt
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

REQUEST=TOPIC/'notes/public-p41-true-CM4-F3-request.json'
D=S/'data'


def prepare(item,base):
    assert os.environ.get('GITHUB_ACTIONS')=='true'
    assert os.environ.get('GITHUB_REPOSITORY')=='Rogerhu12/math-research-public'
    prior=base/'prior';f2=base/'work/f2';out=base/'output'
    for p in [prior,f2,out]:p.mkdir(parents=True,exist_ok=True)
    completed=sorted((TOPIC/'computations'/item['result']).glob('*/run-receipt.json'))
    for path in reversed(completed):
        receipt=read(path)
        if receipt.get('complete'):
            assert receipt['disk_id']==item['disk_id']
            for direction in ['f2','f3']:
                for row in receipt[direction.upper()+'_files']:
                    assert sha(path.parent/direction/row['file'])==row['sha256']
            save(base/'reuse-complete.json',{'already_complete_receipt':str(path),'sha256':sha(path)})
            print('REUSE completed original F3',path,flush=True)
            return
    subprocess.run(['gh','run','download',str(item['prior_run']),'--repo','Rogerhu12/math-research-public',
        '--name',item['artifact'],'--dir',str(prior)],check=True)
    receipt=read(prior/'run-receipt.json');initial=read(prior/'public-actions-input.json');disk=item['disk_id']
    assert sha(prior/'run-receipt.json')==item['prior_receipt_sha256']
    assert receipt['result']==item['prior_result'] and receipt['disk_id']==disk
    assert receipt['complete'] and receipt['exit_code']==0 and receipt['F3_required']
    assert receipt['source_commit']==initial['source_commit']==item['prior_source']
    assert not receipt['F3_files']
    for row in receipt['F2_files']:
        path=prior/'f2'/row['file']
        assert sha(path)==row['sha256'] and path.stat().st_size==row['bytes'],row['file']
    shutil.copytree(prior/'f2',f2,dirs_exist_ok=True)
    archive=f2/('p41_'+disk+'_principal_transports47.tar.gz')
    with tarfile.open(archive,'r:gz') as tf:
        members=tf.getmembers();assert len(members)==459
        for member in members:
            path=Path(member.name)
            assert member.isfile() and not path.is_absolute() and '..' not in path.parts
            assert path.parts==('SS-principal-transports','run_manifest47.json') or (len(path.parts)==3 and path.parts[:2]==('SS-principal-transports',disk))
            target=f2/path;target.parent.mkdir(parents=True,exist_ok=True)
            data=tf.extractfile(member).read()
            if target.exists():assert target.read_bytes()==data
            else:target.write_bytes(data)
    state=read(f2/'chain'/(disk+'_multiply47.json.gz'))
    assert state['bits_done']==state['target_bits']==304
    assert state['input_sha256']==sha(f2/'p41_true_CM4_two_based_points47.json.gz')
    p2=f2/(disk+'_actual_canonical_F2_polynomial47.json.gz')
    a2=f2/(disk+'-principal-F2-independent-audit.json')
    assert read(p2)['residual_QC_roots']==[31,40]
    assert read(a2)['source_sha256']==sha(S/'verify_true_CM4_F2_principal47.py')
    for name in ['p41_rational_SS_second_kind_integrals47_complete.json.gz','p41_SS_second_kind_rhs47.json.gz']:
        target=f2/'recovery-inputs'/name;target.parent.mkdir(parents=True,exist_ok=True)
        target.symlink_to((D/name).resolve(strict=True))
    (f2/'recovery-inputs/SS-second-kind-rhs').symlink_to((D/'SS_second_kind_rhs47').resolve(strict=True),target_is_directory=True)
    rc=D/'p41_true_CM4_regular_height_derivative47.json.gz';ra=D/'p41_true_CM4_regular_height_derivative47_independent.json'
    assert read(rc)['both_true_rational_CM4_disks_complete'] and read(ra)['certificate_sha256']==sha(rc)
    source=subprocess.check_output(['git','rev-parse','HEAD'],cwd=REPO,text=True).strip()
    save(out/'public-actions-input.json',{'result':item['result'],'disk_id':disk,'request_item':item,
        'source_commit':source,'request_sha256':sha(REQUEST),'prior_receipt_sha256':sha(prior/'run-receipt.json'),
        'prior_input_sha256':sha(prior/'public-actions-input.json'),'prior_F2_polynomial_sha256':sha(p2),
        'prior_F2_audit_sha256':sha(a2),'original_chain_bits_restored':304,
        'joint_Laurent_certificate_sha256':sha(rc),'joint_Laurent_audit_sha256':sha(ra),
        'root_readme_sha256':sha(REPO/'README.md'),'topic_readme_sha256':sha(TOPIC/'README.md'),
        'original_chain_terminal_principal_or_F2_repeated':False,
        'T3_four_kernel_multiplicities_retained':True,'mathematical_completion_claimed':False})


def run(item,base,budget):
    if (base/'reuse-complete.json').exists():return 0
    f2=base/'work/f2';f3=base/'work/f3';out=base/'output';disk=item['disk_id'];started=time.monotonic()
    rc=D/'p41_true_CM4_regular_height_derivative47.json.gz';ra=D/'p41_true_CM4_regular_height_derivative47_independent.json'
    command=[sys.executable,'-u',str(S/'p41_compute_true_CM4_F3_from_complete_F2_47.py'),
        '--script-dir',str(S),'--source-dir',str(S),'--f2-dir',str(f2),
        '--recovery-dir',str(f2/'recovery-inputs'),'--based-points',str(f2/'p41_true_CM4_two_based_points47.json.gz'),
        '--canonical',str(D/'p41_canonical_SS_robust47_raw.json.gz'),'--derivative',str(rc),
        '--ramified-j-certificate',str(rc),'--ramified-j-audit',str(ra),'--work-dir',str(f3),
        '--disk-id',disk,'--result-id',item['result']]
    error=None;code=1
    try:
        with (out/'actual_CM4_F3.log').open('w') as log:
            proc=subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
            try:code=proc.wait(timeout=budget*60)
            except subprocess.TimeoutExpired:
                os.killpg(proc.pid,signal.SIGTERM)
                try:proc.wait(timeout=10)
                except subprocess.TimeoutExpired:os.killpg(proc.pid,signal.SIGKILL);proc.wait()
                raise TimeoutError('CM4 F3 budget reached; completed stages preserved.')
        if code:raise subprocess.CalledProcessError(code,command)
    except Exception as exc:
        error=type(exc).__name__+': '+str(exc);code=1
    finally:
        rows2=preserve(f2,out/'f2',disk);rows3=preserve(f3,out/'f3',disk)
        receipt={'result':item['result'],'disk_id':disk,'complete':code==0,'exit_code':code,'error':error,
            'command':command,'F2_files':rows2,'F3_files':rows3,
            'source_commit':read(out/'public-actions-input.json')['source_commit'],
            'prior_result':item['prior_result'],'prior_run':item['prior_run'],
            'original_chain_repeated':False,'original_F2_repeated':False,
            'execution_environment':'public-repository-github-actions','workflow_run_id':os.environ.get('GITHUB_RUN_ID'),
            'finished_at_utc':dt.datetime.now(dt.timezone.utc).isoformat(),'elapsed_seconds':round(time.monotonic()-started,3)}
        poly=f3/(disk+'_actual_canonical_F3_polynomial47.json.gz')
        if poly.exists():
            value=read(poly);receipt['F3_remaining_pairs']=value['remaining_F2_F3_candidate_and_component_pairs']
            receipt['F2_F3_entire_disk_excluded']=value['entire_disk_excluded_by_F2_and_F3_for_all_four_bad_components']
        save(out/'run-receipt.json',receipt)
    print({'result':item['result'],'complete_F3':code==0,'error':error},flush=True)
    return code


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('mode',choices=['prepare','run','publish','verify'])
    ap.add_argument('--result',required=True);ap.add_argument('--budget-minutes',type=int,default=311);args=ap.parse_args()
    item=next(v for v in read(REQUEST)['jobs'] if v['result']==args.result)
    assert item['result']=='R709' and item['disk_id']=='SS_j36_06'
    base=Path(os.environ['RUNNER_TEMP'])/'serre-p41-true-CM4-F3'/args.result
    if args.mode=='prepare':prepare(item,base);return 0
    if args.mode=='run':return run(item,base,args.budget_minutes)
    if (base/'reuse-complete.json').exists():return 0
    if args.mode=='publish':return publish(item,base/'output',artifact_prefix='serre-p41-true-CM4-F3',omit_derived_based_points=False)
    return 0 if read(base/'output/run-receipt.json')['complete'] else 1


if __name__=='__main__':sys.exit(main())
