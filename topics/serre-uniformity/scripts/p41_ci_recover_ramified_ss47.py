#!/usr/bin/env python3
"""Recover one missing ramified SS disk on the README-rule-14 public runner.

Actual computation stays in RUNNER_TEMP. Only the complete mathematical outputs,
principal functions, stage checkpoints and logs are copied to OUT_DIR. The checked-out
source commit is read with Git; no Git mutation or credential read is performed here.
The public runner owns publication.
"""
import argparse
import datetime
import gzip
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import sys
import tarfile
import tempfile
import time


def read(path):
    raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def archive_functions(work, dest):
    directory=work/'SS-principal-transports'
    if not directory.exists():
        return None
    paths=sorted(p for p in directory.rglob('*') if p.is_file())
    if not paths:
        return None
    with dest.open('wb') as raw:
        with gzip.GzipFile(fileobj=raw,mode='wb',mtime=0,filename='') as gz:
            with tarfile.open(fileobj=gz,mode='w') as tar:
                for path in paths:
                    entry=tar.gettarinfo(str(path),arcname=str(path.relative_to(work)))
                    entry.uid=entry.gid=0;entry.uname=entry.gname='';entry.mtime=0
                    with path.open('rb') as src:
                        tar.addfile(entry,src)
    return {'members':len(paths),'sha256':digest(dest),'bytes':dest.stat().st_size}


def preserve(work,out,disk):
    out.mkdir(parents=True,exist_ok=True)
    if not work.exists():
        return []
    sources=[]
    for pattern in ['*.json.gz','*.json','*.log']:
        sources.extend(sorted(work.glob(pattern)))
    for path in sources:
        target=out/path.name
        if path.suffix!='.gz' and path.stat().st_size>1_000_000:
            target=target.with_name(target.name+'.gz')
            with path.open('rb') as src,target.open('wb') as raw:
                with gzip.GzipFile(fileobj=raw,mode='wb',mtime=0,filename='') as dst:
                    shutil.copyfileobj(src,dst)
        else:
            shutil.copyfile(path,target)
    chain=work/'chain'
    if chain.exists():
        (out/'chain').mkdir(exist_ok=True)
        for path in chain.glob('*.json.gz'):
            shutil.copyfile(path,out/'chain'/path.name)
    archive_functions(work,out/('p41_'+disk+'_principal_transports47.tar.gz'))
    return [{'file':str(p.relative_to(out)),'bytes':p.stat().st_size,'sha256':digest(p)}
            for p in sorted(out.rglob('*')) if p.is_file()]


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--disk-id',required=True)
    ap.add_argument('--result-id',required=True)
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--budget-minutes',type=int,default=320)
    args=ap.parse_args()
    if not re.fullmatch(r'SS_j(?:0|36)_\d{2}',args.disk_id):
        ap.error('A ramified disk ID is required.')
    if not re.fullmatch(r'R\d+',args.result_id):
        ap.error('A reserved research result ID is required.')
    if not 1<=args.budget_minutes<=330:
        ap.error('Internal budget must leave room before the runner deadline.')
    S=Path(__file__).resolve().parent;D=S/'data';disk=args.disk_id
    frame=read(D/'p41_ramified_j_regular_height_derivative47.json.gz')
    covered={d for chart in frame['charts'] for d in chart['disk_ids']}
    if disk not in covered:
        raise RuntimeError('This disk requires its separate elliptic-stabilizer interface.')
    source_commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=S.parents[2],text=True).strip()
    out=args.output.resolve();out.mkdir(parents=True,exist_ok=True)
    if (out/'run-receipt.json').exists():
        raise RuntimeError('This output already has a receipt; consume it instead of rerunning sealed work.')
    if (D/(disk+'_actual_canonical_F2_polynomial47.json.gz')).exists():
        raise RuntimeError('The requested disk already has a published F2 result; do not recompute it.')
    scratch=Path(tempfile.mkdtemp(prefix=args.result_id+'-'+disk+'-',dir=os.environ.get('RUNNER_TEMP')))
    f2=scratch/'f2';f3=scratch/'f3';based=scratch/(args.result_id+'_'+disk+'_based_points47.json.gz')
    start=time.monotonic();deadline=start+60*args.budget_minutes
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
    stages=[];error=None;status=1
    def run(label,command):
        remaining=deadline-time.monotonic()
        if remaining<=0:
            raise TimeoutError('Internal runner budget exhausted before '+label)
        print('START',args.result_id,label,flush=True)
        process=subprocess.Popen(command,env=env,start_new_session=True)
        try:
            code=process.wait(timeout=remaining)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid,signal.SIGTERM)
            try:
                process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid,signal.SIGKILL);process.wait()
            raise TimeoutError('Internal runner budget exhausted during '+label)
        stages.append({'stage':label,'command':command,'exit_code':code})
        if code:
            raise subprocess.CalledProcessError(code,command)
        print('COMPLETE',args.result_id,label,flush=True)
    try:
        run('based_points',[sys.executable,'-u',str(S/'p41_SS_Abel_multiply47.py'),
            '--script-dir',str(S),'--SS-atlas',str(D/'p41_rational_SS_residue_atlas47_complete.json.gz'),
            '--common-based-points',str(D/'p41_all19_based_points47.json.gz'),
            '--based-points',str(based),'--workdir',str(scratch/'preparation'),
            '--disk',disk,'--prepare-only'])
        run('actual_F2',[sys.executable,'-u',str(S/'p41_rebuild_ramified_SS_F2_unit_parameter47.py'),
            '--script-dir',str(S),'--work-dir',str(f2),'--disk-id',disk,'--result-id',args.result_id,
            '--canonical',str(D/'p41_canonical_SS_robust47_raw.json.gz'),
            '--canonical-certificate',str(D/'p41_canonical_SS_robust47_certificate.json.gz'),
            '--derivative',str(D/'p41_serre_clearing_126_disks47.json.gz'),
            '--ramified-j-certificate',str(D/'p41_ramified_j_regular_height_derivative47.json.gz'),
            '--ramified-j-audit',str(D/'p41_ramified_j_regular_height_derivative47_independent.json'),
            '--based-points',str(based),'--rebuild-chain'])
        poly=read(f2/(disk+'_actual_canonical_F2_polynomial47.json.gz'))
        if poly['residual_QC_roots']:
            run('actual_F3',[sys.executable,'-u',str(S/'p41_rebuild_ramified_SS_F3_unit_parameter47.py'),
                '--script-dir',str(S),'--source-dir',str(S),'--f2-dir',str(f2),
                '--recovery-dir',str(f2/'recovery-inputs'),'--based-points',str(f2/based.name),
                '--canonical',str(D/'p41_canonical_SS_robust47_raw.json.gz'),
                '--derivative',str(D/'p41_serre_clearing_126_disks47.json.gz'),
                '--ramified-j-certificate',str(D/'p41_ramified_j_regular_height_derivative47.json.gz'),
                '--ramified-j-audit',str(D/'p41_ramified_j_regular_height_derivative47_independent.json'),
                '--work-dir',str(f3),'--disk-id',disk,'--result-id',args.result_id])
        status=0
    except Exception as exc:
        error=type(exc).__name__+': '+str(exc)
        print('INCOMPLETE',args.result_id,error,flush=True)
    finally:
        files_f2=preserve(f2,out/'f2',disk);files_f3=preserve(f3,out/'f3',disk)
        if based.exists() and not (out/'f2'/based.name).exists():
            shutil.copyfile(based,out/'f2'/based.name)
        packages={}
        for name in ['numpy','scipy','sympy','python-flint','mpmath']:
            try:packages[name]=importlib.metadata.version(name)
            except importlib.metadata.PackageNotFoundError:pass
        receipt={'result':args.result_id,'disk_id':disk,'exit_code':status,'error':error,
                 'elapsed_seconds':round(time.monotonic()-start,3),'stages':stages,
                 'finished_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
                 'driver_sha256':digest(Path(__file__)),'python':sys.version,'packages':packages,
                 'source_commit':source_commit,'runner_workflow_commit':os.environ.get('GITHUB_SHA'),
                 'F2_files':files_f2,'F3_files':files_f3,
                 'long_chain_repeated_for_F3':False,'complete':status==0,
                 'scope':'Actual new recovery outputs; root records each full mathematical conclusion after return.'}
        if (f2/(disk+'_actual_canonical_F2_polynomial47.json.gz')).exists():
            value=read(f2/(disk+'_actual_canonical_F2_polynomial47.json.gz'))
            receipt['F2_residual_roots']=value['residual_QC_roots']
            receipt['F2_entire_disk_excluded']=value['entire_disk_excluded_for_all_four_bad_components']
        if (f3/(disk+'_actual_canonical_F3_polynomial47.json.gz')).exists():
            value=read(f3/(disk+'_actual_canonical_F3_polynomial47.json.gz'))
            receipt['F3_remaining_pairs']=value['remaining_F2_F3_candidate_and_component_pairs']
            receipt['F2_F3_entire_disk_excluded']=value['entire_disk_excluded_by_F2_and_F3_for_all_four_bad_components']
        oversized=[str(p.relative_to(out)) for p in out.rglob('*') if p.is_file() and p.stat().st_size>=5_000_000]
        receipt['files_over_repository_cap']=oversized
        (out/'run-receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
        print('SAVED',args.result_id,'complete',receipt['complete'],'files',len(files_f2)+len(files_f3),flush=True)
    return status


if __name__=='__main__':
    sys.exit(main())
