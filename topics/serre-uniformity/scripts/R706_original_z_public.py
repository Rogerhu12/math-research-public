#!/usr/bin/env python3
"""Public single-prime original-z verification; preserve complete receipts."""
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
from R698_verify_original_z import run
from p41_public_actions_recovery import publish, read, sha, REPO, TOPIC


def save(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    data=(json.dumps(value,indent=2)+'\n').encode()
    if path.suffix=='.gz':data=gzip.compress(data,mtime=0)
    tmp=path.with_name(path.name+'.tmp');tmp.write_bytes(data);tmp.replace(path)


def stop(signum,frame):raise InterruptedError('Received signal '+str(signum))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode',choices=['compute','publish','verify'])
    args=parser.parse_args()
    request_path=TOPIC/'notes/R706-original-z-request.json';request=read(request_path)
    p=request['prime'];assert p==137147
    result='R706-original-z-'+str(p)
    out=Path(os.environ['RUNNER_TEMP'])/'serre-cartier'/result
    out.mkdir(parents=True,exist_ok=True)
    if args.mode=='publish':return publish({'result':result},out,artifact_prefix='serre-cartier')
    if args.mode=='verify':return 0 if read(out/'summary.json')['complete'] else 1
    source=subprocess.check_output(['git','rev-parse','HEAD'],cwd=REPO,text=True).strip()
    arithmetic=Path(__file__).with_name('R698_verify_original_z.py')
    hashes={'arithmetic_source_sha256':sha(arithmetic),'wrapper_source_sha256':sha(Path(__file__)),
            'publisher_source_sha256':sha(Path(__file__).with_name('p41_public_actions_recovery.py')),
            'parameters_sha256':sha(request_path),'root_readme_sha256':sha(REPO/'README.md'),
            'topic_readme_sha256':sha(TOPIC/'README.md')}
    save(out/'public-actions-input.json',{'source_commit':source,'result':result,
         'repository':'Rogerhu12/math-research-public','request':request,**hashes})
    for path in [arithmetic,Path(__file__),request_path]:
        (out/(path.name+'.gz')).write_bytes(gzip.compress(path.read_bytes(),mtime=0))
    summary={'complete':False,'prime':p,'source_commit':source,'result':result,
             'computed_now':False,'reused_from':None,**hashes}
    save(out/'summary.json',summary)
    signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
    try:
        value=None
        # A published complete calculation is an input, never repeated here.
        previous=TOPIC/'computations'/result
        for summary_path in sorted(previous.glob('*/summary.json')):
            old=read(summary_path)
            if not old.get('complete') or old.get('prime')!=p:continue
            assert old['arithmetic_source_sha256']==hashes['arithmetic_source_sha256'],(
                'Existing complete original-z run uses different source; root review required, not automatic recomputation.')
            cert=summary_path.parent/old['certificate']
            assert sha(cert)==old['certificate_sha256']
            value=read(cert);shutil.copyfile(cert,out/'original-z-137147.json.gz')
            summary['reused_from']=str(summary_path.relative_to(REPO))
            summary['reused_source_commit']=old['source_commit']
            break
        if value is None:
            value=run(p,full=True)
            value.update({'source_commit':source,**hashes})
            save(out/'original-z-137147.json.gz',value)
            summary['computed_now']=True
        # Preserve the full computed data even if agreement were to fail.
        for key,expected in request['expected'].items():
            assert value[key]==expected,(key,value[key],expected)
        cert=out/'original-z-137147.json.gz'
        summary.update({'complete':True,'agrees_with_original_window':True,
            'certificate':cert.name,'certificate_sha256':sha(cert),
            'values':{key:value[key] for key in request['expected']},
            'M2_itself_proved_zero':False})
    except BaseException as exc:
        summary['error']=type(exc).__name__+': '+str(exc)
        (out/'failure.txt').write_text(traceback.format_exc())
    summary['finished_at_utc']=dt.datetime.now(dt.timezone.utc).isoformat()
    save(out/'summary.json',summary);print(json.dumps(summary),flush=True)
    return 0 if summary['complete'] else 1


if __name__=='__main__':sys.exit(main())
