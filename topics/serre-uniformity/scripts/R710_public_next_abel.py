#!/usr/bin/env python3
"""Extract the next original Abel weight pair using the completed R706 input."""
import argparse
import datetime as dt
import gzip
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import traceback
from p41_public_actions_recovery import publish,read,sha,REPO,TOPIC

RESULT='R710-next-original-Abel-pair'
CERTIFICATE='R710-next-actual-Abel-pair-137147.json'


def save(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_name(path.name+'.tmp')
    temporary.write_text(json.dumps(value,indent=2)+'\n');temporary.replace(path)


def stop(signum,frame):raise InterruptedError('Received signal '+str(signum))


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('mode',choices=['compute','publish','verify']);args=ap.parse_args()
    request_path=TOPIC/'notes/R710-public-next-Abel-request.json';request=read(request_path)
    out=Path(os.environ['RUNNER_TEMP'])/'serre-cartier'/RESULT;out.mkdir(parents=True,exist_ok=True)
    if args.mode=='publish':return publish({'result':RESULT},out,artifact_prefix='serre-cartier')
    if args.mode=='verify':
        summary=read(out/'summary.json')
        return 0 if summary['complete'] and sha(out/CERTIFICATE)==summary['certificate_sha256'] else 1
    source=subprocess.check_output(['git','rev-parse','HEAD'],cwd=REPO,text=True).strip()
    arithmetic=Path(__file__).with_name('R710_extract_next_original_Abel_pair.py')
    publisher=Path(__file__).with_name('p41_public_actions_recovery.py')
    workflow=REPO/'.github/workflows/serre-next-original-Abel-pair.yml'
    original=TOPIC/'computations/R706-original-z-137147/43587480525-1/original-z-137147.json.gz'
    hashes={'arithmetic_source_sha256':sha(arithmetic),'wrapper_source_sha256':sha(__file__),
        'publisher_source_sha256':sha(publisher),'workflow_source_sha256':sha(workflow),
        'request_sha256':sha(request_path),'original_certificate_sha256':sha(original),
        'root_readme_sha256':sha(REPO/'README.md'),'topic_readme_sha256':sha(TOPIC/'README.md')}
    run_url='https://github.com/Rogerhu12/math-research-public/actions/runs/'+os.environ.get('GITHUB_RUN_ID','missing')
    save(out/'public-actions-input.json',{'result':RESULT,'source_commit':source,
        'source_repository':'Rogerhu12/math-research-public','run_url':run_url,'request':request,**hashes})
    for path in [arithmetic,Path(__file__),publisher,workflow,request_path,REPO/'README.md',TOPIC/'README.md']:
        name='root-README.md' if path==REPO/'README.md' else 'topic-README.md' if path==TOPIC/'README.md' else path.name
        (out/(name+'.gz')).write_bytes(gzip.compress(path.read_bytes(),mtime=0))
    shutil.copyfile(original,out/original.name)
    summary={'result':RESULT,'source_commit':source,'run_url':run_url,'complete':False,
        'computed_now':False,'reused_from':None,'differential_equation_or_window_repeated':False,**hashes}
    save(out/'summary.json',summary);signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
    try:
        assert os.environ.get('GITHUB_ACTIONS')=='true' and os.environ.get('GITHUB_REPOSITORY')=='Rogerhu12/math-research-public'
        assert request['result']==RESULT and request['prime']==137147
        for key,value in request['pinned_sha256'].items():assert hashes[key]==value,(key,hashes[key],value)
        certificate=out/CERTIFICATE
        for oldpath in sorted((TOPIC/'computations'/RESULT).glob('*/summary.json')):
            old=read(oldpath)
            if not old.get('complete'):continue
            assert all(old[key]==hashes[key] for key in ['arithmetic_source_sha256','original_certificate_sha256']), 'Do not rerun completed arithmetic with silently changed sources.'
            oldcert=oldpath.parent/old['certificate'];assert sha(oldcert)==old['certificate_sha256']
            shutil.copyfile(oldcert,certificate);summary['reused_from']=str(oldpath.relative_to(REPO));break
        if not certificate.exists():
            command=[sys.executable,'-u',str(arithmetic),'--certificate',str(original),'--output',str(certificate)]
            save(out/'command.json',{'argv':command,'timeout_seconds':600})
            with (out/'public-actions-run.log').open('w') as log:
                result=subprocess.run(command,cwd=REPO,stdout=log,stderr=subprocess.STDOUT,timeout=600)
            summary['process_exit_code']=result.returncode
            assert result.returncode==0,'Original-pair extraction failed; preserve input and failure.'
            summary['computed_now']=True
        value=read(certificate)
        assert value['input_gzip_sha256']==hashes['original_certificate_sha256']
        assert value['source_sha256']==hashes['arithmetic_source_sha256']
        assert value['original_arrays_and_full_energy_equation_checked']
        assert value['differential_equation_or_window_repeated'] is False
        for row in value['rows']:
            expected=request['expected_C_by_weight'][str(row['weight'])]
            assert row['C']==expected,(row['weight'],row['C'],expected)
        assert sha(certificate)==request['development_certificate_sha256']
        summary.update({'complete':True,'certificate':CERTIFICATE,'certificate_sha256':sha(certificate),
            'actual_rows':value['rows'],'implication_using_R705':value['implication_using_R705'],
            'public_result_matches_development_bytes':True})
    except BaseException as exc:
        summary['error']=type(exc).__name__+': '+str(exc);(out/'failure.txt').write_text(traceback.format_exc())
    summary['finished_at_utc']=dt.datetime.now(dt.timezone.utc).isoformat()
    save(out/'summary.json',summary);print(json.dumps(summary),flush=True)
    return 0 if summary['complete'] else 1


if __name__=='__main__':sys.exit(main())
