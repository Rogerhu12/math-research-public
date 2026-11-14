#!/usr/bin/env python3
"""Continue the two actual R552 one-bit prefixes on the public runner.

The preserved based file and ordered pair remain unchanged. Only missing chain,
terminal second-kind, and principal-expression computations are executed. The
already published initial geometry and audit are consumed without replaying them.
This task does not claim F2/F3 heights or disk exclusions.
"""
import argparse
import datetime
import gzip
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import tarfile
import tempfile
import time


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def read(p):
    b=p.read_bytes()
    return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)


def pack_disk(transports,disk,target):
    paths=[transports/'run_manifest47.json']+sorted((transports/disk).glob('*.json*'))
    paths=[p for p in paths if p.is_file()]
    if not paths:
        return None
    with target.open('wb') as raw:
        with gzip.GzipFile(fileobj=raw,mode='wb',mtime=0,filename='') as gz:
            with tarfile.open(fileobj=gz,mode='w') as tf:
                for p in paths:
                    arc=Path('SS-principal-transports')/p.relative_to(transports)
                    info=tf.gettarinfo(str(p),arcname=str(arc))
                    info.uid=info.gid=0; info.uname=info.gname=''; info.mtime=0
                    with p.open('rb') as stream:
                        tf.addfile(info,stream)
    return {'disk_id':disk,'members':len(paths),'bytes':target.stat().st_size,'sha256':digest(target)}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',required=True,type=Path)
    ap.add_argument('--result-id',default='R655',choices=['R655'])
    ap.add_argument('--budget-minutes',default=320,type=int)
    args=ap.parse_args()
    assert 1<=args.budget_minutes<=330
    S=Path(__file__).resolve().parent; D=S/'data'
    out=args.output.resolve(); out.mkdir(parents=True,exist_ok=True)
    assert not (out/'run-receipt.json').exists()
    source_commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=S.parents[2],text=True).strip()
    W=Path(tempfile.mkdtemp(prefix='R655-true-CM4-',dir=os.environ.get('RUNNER_TEMP')))
    archive=D/'p41_true_CM4_initial_prefix47.tar.gz'
    with tarfile.open(archive,'r:gz') as tf:
        members=tf.getmembers(); assert len(members)==6
        for item in members:
            p=Path(item.name)
            assert item.isfile() and not p.is_absolute() and '..' not in p.parts
            assert p.parts[0]=='CM4-initial-prefix'
            target=W/p; target.parent.mkdir(parents=True,exist_ok=True)
            target.write_bytes(tf.extractfile(item).read())
    root=W/'CM4-initial-prefix'; manifest=read(root/'prefix_manifest47.json')
    disks=['SS_j36_06','SS_j36_02']
    assert manifest['disk_ids']==disks and manifest['actual_bits_each']==1
    for row in manifest['members']:
        p=W/row['archive_member']
        assert digest(p)==row['sha256'] and p.stat().st_size==row['bytes']
    based=D/'p41_true_CM4_two_based_points47.json.gz'
    assert digest(based)==manifest['original_based_points_sha256']
    work=root/'work'; transports=root/'transports'
    for disk in disks:
        state=read(work/(disk+'_multiply47.json.gz'))
        assert state['bits_done']==1 and state['input_sha256']==digest(based)
        assert not (D/(disk+'_Abel47.json.gz')).exists(), 'A completed chain is already published.'
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
    start=time.monotonic(); deadline=start+60*args.budget_minutes
    stages=[]; status=1; error=None

    def run(label,script,argv,outputs):
        command=[sys.executable,'-u',str(S/script)]+list(map(str,argv))
        remaining=deadline-time.monotonic()
        if remaining<=0:
            raise TimeoutError('Internal budget exhausted before '+label)
        print('START',args.result_id,label,flush=True)
        log=W/(label+'.log')
        with log.open('w') as stream:
            p=subprocess.Popen(command,env=env,start_new_session=True,stdout=stream,stderr=subprocess.STDOUT)
            try:
                code=p.wait(timeout=remaining)
            except subprocess.TimeoutExpired:
                os.killpg(p.pid,signal.SIGTERM)
                try:p.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    os.killpg(p.pid,signal.SIGKILL); p.wait()
                raise TimeoutError('Internal budget exhausted during '+label)
        entry={'stage':label,'command':command,'source_sha256':digest(S/script),'exit_code':code,'log':log.name}
        stages.append(entry)
        if code:
            raise subprocess.CalledProcessError(code,command)
        entry['outputs']=[]
        for output in outputs:
            assert output.exists()
            entry['outputs'].append({'file':str(output.relative_to(W)),'sha256':digest(output),'bytes':output.stat().st_size})
        (W/'checkpoint.json').write_text(json.dumps({'result':args.result_id,'stages':stages},indent=2)+'\n')
        print('COMPLETE',args.result_id,label,flush=True)

    try:
        run('continue_both_original_chains','p41_SS_Abel_with_transports47.py',[
            '--script-dir',S,'--SS-atlas',D/'p41_rational_SS_residue_atlas47_complete.json.gz',
            '--common-based-points',D/'p41_all19_based_points47.json.gz','--based-points',based,
            '--workdir',work,'--transport-dir',transports,'--disk',disks[0],'--disk',disks[1],
            '--max-bits','304','--tiny',D/'p41_all129_tiny_Abel47_complete.json.gz'],
            [work/(d+'_Abel47.json.gz') for d in disks])
        for disk in disks:
            mult=work/(disk+'_multiply47.json.gz'); abel=work/(disk+'_Abel47.json.gz')
            second=W/(disk+'_actual_second_kind_integrals47.json.gz')
            principal=W/(disk+'_principal_expression47.json.gz')
            run(disk+'_actual_terminal_and_nu','p41_SS_second_kind_from_principal47.py',[
                '--script-dir',S,'--based-points',based,'--second-kind',D/'p41_second_kind_connection47.json.gz',
                '--Abel',abel,'--multiplication',mult,'--transport-directory',transports/disk,
                '--build-dir',W/('native-terminal-'+disk),'--output',second],[second])
            run(disk+'_actual_integer_principal','p41_principal_chain_flatten47.py',[
                '--transport-directory',transports/disk,'--second-kind-certificate',second,
                '--bases',D/'p41_hecke3_abel_bases_checkpoint.json.gz','--output',principal],[principal])
        status=0
    except Exception as exc:
        error=type(exc).__name__+': '+str(exc)
        print('INCOMPLETE',args.result_id,error,flush=True)
    finally:
        shutil.copyfile(based,out/based.name)
        shutil.copyfile(root/'prefix_manifest47.json',out/'original-prefix-manifest.json')
        (out/'chain').mkdir(exist_ok=True)
        for p in work.glob('*.json.gz'):
            shutil.copyfile(p,out/'chain'/p.name)
        for pattern in ['*.json','*.json.gz','*.log']:
            for p in W.glob(pattern):
                q=out/p.name
                if p.suffix!='.gz' and p.stat().st_size>1_000_000:
                    q=q.with_name(q.name+'.gz')
                    with p.open('rb') as src,q.open('wb') as raw:
                        with gzip.GzipFile(fileobj=raw,mode='wb',mtime=0,filename='') as dst:
                            shutil.copyfileobj(src,dst)
                else:shutil.copyfile(p,q)
        archives=[pack_disk(transports,d,out/('p41_'+d+'_principal_transports47.tar.gz')) for d in disks]
        states={d:{k:read(work/(d+'_multiply47.json.gz')).get(k) for k in ['bits_done','target_bits','point_sha256','zero_test_mod47']} for d in disks}
        packages={}
        for name in ['numpy','scipy','sympy','python-flint','mpmath']:
            try:packages[name]=importlib.metadata.version(name)
            except importlib.metadata.PackageNotFoundError:pass
        receipt={'result':args.result_id,'exit_code':status,'complete':status==0,'error':error,
            'disk_ids':disks,'initial_bits_each':1,'initial_geometry_repeated':False,
            'source_commit':source_commit,'runner_workflow_commit':os.environ.get('GITHUB_SHA'),
            'driver_sha256':digest(Path(__file__)),'input_archive_sha256':digest(archive),
            'elapsed_seconds':round(time.monotonic()-start,3),'stages':stages,'chain_states':states,
            'principal_archives':archives,'python':sys.version,'packages':packages,
            'finished_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'F2_F3_height_computed':False,'disk_exclusion_claimed':False,
            'files':[{'file':str(p.relative_to(out)),'bytes':p.stat().st_size,'sha256':digest(p)} for p in sorted(out.rglob('*')) if p.is_file()]}
        receipt['files_over_repository_cap']=[f['file'] for f in receipt['files'] if f['bytes']>=5_000_000]
        (out/'run-receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
        print('SAVED',args.result_id,'complete',receipt['complete'],flush=True)
    return status


if __name__=='__main__':
    sys.exit(main())
