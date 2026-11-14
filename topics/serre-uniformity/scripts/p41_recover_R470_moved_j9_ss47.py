#!/usr/bin/env python3
"""Continue one R470 moved j9 disk using its original block and two functions.

The original geometry and the two actual initial moving flips are consumed from
their published archive. New scalar-chain, Norm and local-height outputs are
retained after every completed stage. This local driver never modifies Git.
"""
import argparse
import datetime as dt
import gzip
import hashlib
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import tarfile
import time


DISKS=[5,6,7,8,9,10,12,13,14,15,16,17,18,20,21,22]
ASSIGNED={f'SS_j9_{d:02d}':f'R{666+i}' for i,d in enumerate(DISKS)}


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    p=Path(p);raw=p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix=='.gz' else raw)


def atomic_json(path,value):
    path=Path(path);tmp=path.with_suffix(path.suffix+'.new')
    tmp.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n');tmp.replace(path)


def copy_exact(source,target):
    source=Path(source);target=Path(target);target.parent.mkdir(parents=True,exist_ok=True)
    if target.exists():
        assert sha(source)==sha(target),(source,target)
    else:
        shutil.copyfile(source,target)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ['script-dir','work-dir','output']:
        ap.add_argument('--'+name,type=Path,required=True)
    ap.add_argument('--adapter-dir',type=Path)
    ap.add_argument('--disk-id',required=True,choices=list(ASSIGNED))
    ap.add_argument('--result-id',required=True)
    ap.add_argument('--budget-minutes',type=int,default=320)
    args=ap.parse_args();disk=args.disk_id;result=args.result_id
    assert ASSIGNED[disk]==result
    assert 1<=args.budget_minutes<=330
    S=args.script_dir.resolve();D=S/'data';A=(args.adapter_dir or S).resolve()
    W=args.work_dir.resolve();O=args.output.resolve();W.mkdir(parents=True,exist_ok=True);O.mkdir(parents=True,exist_ok=True)
    assert W!=O
    sys.path.insert(0,str(S))
    from p41_ci_recover_ramified_ss47 import preserve
    old_receipt=O/'run-receipt.json'
    if old_receipt.exists() and read(old_receipt)['complete']:
        raise RuntimeError('This recovery is complete; consume its preserved result.')
    if (D/(disk+'_actual_canonical_F2_polynomial47.json.gz')).exists():
        raise RuntimeError('This disk already has a published F2 result; do not repeat it.')
    bundle_path=D/'p41_j9_remaining16_moving_input_bundle47.json'
    bundle=read(bundle_path)
    assert bundle['result']=='R470' and bundle['complete_all_sixteen_actual_initial_moves'] and bundle['complete_actual_initial_SLP_interface']
    block=next(b for b in bundle['blocks'] if disk in b['disk_ids'])
    based=W/block['based_points']['basename'];moving=W/block['independent_audit']['basename']
    for key,target in [('based_points',based),('independent_audit',moving)]:
        meta=block[key];source=D/meta['basename']
        assert source.stat().st_size==meta['bytes'] and sha(source)==meta['sha256']
        copy_exact(source,target)
    b=read(based);ma=read(moving)
    assert b['result']=='R470' and set(b['selected_disks'])==set(block['disk_ids'])
    assert ma['result']=='R470' and ma['selected_disk_count']==4 and ma['all_selected_initial_moving_transports_independently_replayed']
    assert set(ma['selected_disk_ids'])==set(block['disk_ids']) and sha(based) in ma['input_sha256'].values()
    archive=D/bundle['initial_transport_archive']['basename']
    assert sha(archive)==bundle['initial_transport_archive']['sha256']
    transports=W/'SS-principal-transports';T=transports/disk
    wanted={f'R470-{block["block_id"]}/run_manifest47.json':(transports/'run_manifest47.json',block['initial_run_manifest']['sha256'])}
    initial=[row for row in block['initial_actual_functions'] if row['disk_id']==disk]
    assert len(initial)==2
    for row in initial:
        name=Path(row['path']).name
        wanted[f'R470-{block["block_id"]}/{disk}/{name}']=(T/name,row['sha256'])
    with tarfile.open(archive,'r:gz') as tf:
        assert len(tf.getmembers())==36
        for member_name,(target,digest) in wanted.items():
            member=tf.getmember(member_name);assert member.isfile()
            raw=tf.extractfile(member).read();assert hashlib.sha256(raw).hexdigest()==digest
            target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists():assert target.read_bytes()==raw
            else:target.write_bytes(raw)
    recovery=W/'recovery-inputs';recovery.mkdir(exist_ok=True)
    for name in ['p41_rational_SS_second_kind_integrals47_complete.json.gz','p41_SS_second_kind_rhs47.json.gz']:
        p=recovery/name;source=(D/name).resolve(strict=True)
        if p.exists():assert p.resolve()==source
        else:p.symlink_to(source)
    p=recovery/'SS-second-kind-rhs';source=(D/'SS_second_kind_rhs47').resolve(strict=True)
    if p.exists():assert p.resolve()==source
    else:p.symlink_to(source,target_is_directory=True)
    chain=W/'chain';chain.mkdir(exist_ok=True)
    mult=chain/(disk+'_multiply47.json.gz');abel=chain/(disk+'_Abel47.json.gz')
    second=W/(disk+'_actual_second_kind_integrals47.json.gz');flat=W/(disk+'_principal_expression47.json.gz')
    support=W/(disk+'_actual_T2_support47.json.gz');t2=W/(disk+'_actual_T2_principal_norm47.json.gz')
    full=W/(disk+'_actual_F2_first_variable_norm47.json.gz');center=W/(disk+'_actual_canonical_F2_height47.json.gz')
    poly=W/(disk+'_actual_canonical_F2_polynomial47.json.gz');audit=W/(disk+'-principal-F2-independent-audit.json')
    canonical=D/'p41_canonical_SS_robust47_raw.json.gz';certificate=D/'p41_canonical_SS_robust47_certificate.json.gz'
    derivative=D/'p41_serre_clearing_126_disks47.json.gz'
    cp=W/'R470_recovery_checkpoint47.json'
    previous=read(cp) if cp.exists() else {'result':result,'disk_id':disk,'completed_stages':[]}
    assert previous['result']==result and previous['disk_id']==disk
    old_stages={row['stage']:row for row in previous['completed_stages']};completed=[]
    start=time.monotonic();deadline=start+args.budget_minutes*60
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
    env['PYTHONPATH']=str(S)+(os.pathsep+env['PYTHONPATH'] if env.get('PYTHONPATH') else '')
    source_commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=S.parents[2],text=True).strip()

    def run(label,source,argv,output,extra_products=()):
        source=Path(source);output=Path(output)
        command=[sys.executable,'-u',str(source)]+list(map(str,argv));log=W/(label+'.log')
        old=old_stages.get(label);reused=False
        if old:
            assert old['source_sha256']==sha(source) and old['output_sha256']==sha(output)
            for item in old.get('extra_products',[]):
                assert sha(W/item['file'])==item['sha256']
            reused=True
        elif output.exists() and label!='actual_moved_chain':
            existing=read(output)
            assert existing['source_sha256']==sha(source),('changed source',label)
            for key,digest in existing.get('input_sha256',{}).items():
                key=Path(key)
                choices=[key,D/key.name,W/key.name,chain/key.name,T/key.name]
                available=[p for p in choices if p.is_file()]
                if available:assert any(sha(p)==digest for p in available),('changed input',label,key)
            reused=True
        if not reused:
            remaining=deadline-time.monotonic()
            if remaining<=0:raise TimeoutError('Work budget reached before '+label)
            print('START',result,disk,label,flush=True)
            with log.open('a') as stream:
                proc=subprocess.Popen(command,env=env,stdout=stream,stderr=subprocess.STDOUT,start_new_session=True)
                try:code=proc.wait(timeout=remaining)
                except subprocess.TimeoutExpired:
                    os.killpg(proc.pid,signal.SIGTERM)
                    try:proc.wait(timeout=10)
                    except subprocess.TimeoutExpired:os.killpg(proc.pid,signal.SIGKILL);proc.wait()
                    raise TimeoutError('Work budget reached during '+label)
            if code:raise subprocess.CalledProcessError(code,command)
        assert output.is_file()
        row={'stage':label,'source':str(source),'source_sha256':sha(source),'command':command,
             'output':str(output),'output_sha256':sha(output),'bytes':output.stat().st_size,
             'reused_existing_complete_output':reused,'log':str(log),
             'extra_products':[{'file':str(Path(p).relative_to(W)),'sha256':sha(p)} for p in extra_products]}
        completed.append(row)
        atomic_json(cp,{'result':result,'disk_id':disk,'original_R470_block':block['block_id'],
                        'initial_geometry_repeated':False,'completed_stages':completed})
        preserve(W,O/'f2',disk)
        print('PASS',result,label,row['output_sha256'],flush=True)

    status=1;error=None;F3=W/'f3'
    try:
        run('actual_moved_chain',S/'p41_j9_extended_Abel_with_transports47.py',
            ['--script-dir',S,'--SS-atlas',D/'p41_rational_SS_residue_atlas47_complete.json.gz',
             '--common-based-points',D/'p41_all19_based_points47.json.gz','--based-points',based,
             '--disk',disk,'--workdir',chain,'--transport-dir',transports,
             '--tiny',D/'p41_all129_tiny_Abel47_complete.json.gz','--max-bits',304],abel,[mult,T/'transport_manifest47.json'])
        run('actual_terminal_and_nu',S/'p41_moved_SS_second_kind_from_principal47.py',
            ['--script-dir',S,'--based-points',based,'--second-kind',D/'p41_second_kind_connection47.json.gz',
             '--Abel',abel,'--multiplication',mult,'--transport-directory',T,'--build-dir',W/'terminal-native','--output',second],second)
        run('integer_principal_SLP',S/'p41_moved_principal_chain_flatten47.py',
            ['--transport-directory',T,'--second-kind-certificate',second,'--bases',D/'p41_hecke3_abel_bases_checkpoint.json.gz','--output',flat],flat)
        if (D/support.name).exists():
            copy_exact(D/support.name,support)
        run('actual_three_T2_branches',S/'p41_selected_nonelliptic_SS_T2_support47.py',
            ['--script-dir',S,'--disk-id',disk,'--result-id',result,'--work-dir',W/'T2-support','--output',support],support)
        common=['--script-dir',S,'--based-points',based,'--second-kind-certificate',second,
                '--multiplication',mult,'--transport-directory',T,'--principal-expression',flat]
        run('actual_three_branch_Norm',S/'p41_moved_SS_T2_norm47.py',
            common+['--support',support,'--cache-dir',W/'T2-jets','--output',t2],t2)
        run('actual_full_F2_Norm',S/'p41_moved_SS_F2_full_canonical_norm_clearing_frame47.py',
            common+['--canonical-algebra',canonical,'--canonical-unit-certificate',certificate,
                    '--derivative',derivative,'--ss-support',support,'--t2-norm',t2,'--cache-dir',W/'fixed-jets','--output',full],full)
        certificate_args=['--script-dir',S,'--source-dir',S,'--qc-dir',W,'--chain-dir',chain,'--transport-dir',T,
                          '--based-points',based,'--moving-audit',moving,'--t2-support',support,'--derivative',derivative,'--disk-id',disk]
        norm_audit=W/(disk+'-moved-principal-Norm-independent-audit.json')
        run('complete_moved_principal_certificate',A/'verify_R470_moved_SS_principal_norm47.py',
            certificate_args+['--output',norm_audit],norm_audit)
        cs=S/'p41_selected_SS_F2_connection_clearing_frame47.py';ps=S/'p41_selected_SS_F2_polynomial_clearing_frame47.py'
        run('actual_F2_center',cs,['--script-dir',S,'--recovery-dir',recovery,'--disk-id',disk,'--result-id',result,
            '--second-kind',second,'--principal',flat,'--t2-support',support,'--full-norm',full,
            '--canonical',canonical,'--derivative',derivative,'--work-dir',W/'center','--output',center],center)
        run('actual_F2_disk',ps,['--script-dir',S,'--center',center,'--disk-id',disk,'--result-id',result,
            '--abel',abel,'--multiply',mult,'--tiny',D/'p41_all129_second_kind_tiny47_complete.json.gz',
            '--derivative',derivative,'--work-dir',W/'poly','--output',poly],poly)
        run('complete_actual_F2_certificate',A/'verify_R470_moved_SS_F2_clearing_frame47.py',
            certificate_args+['--result-id',result,'--norm-source',S/'p41_moved_SS_F2_full_canonical_norm_clearing_frame47.py',
                              '--center-source',cs,'--poly-source',ps,'--polynomial',poly,'--output',audit],audit)
        if read(poly)['residual_QC_roots']:
            completion=F3/(result+'_'+disk+'_F3_completion47.json')
            run('actual_same_chain_F3',S/'p41_run_moved_j9_F3_derivative47.py',
                ['--script-dir',S,'--source-dir',S,'--recovery-dir',recovery,'--f2-dir',W,'--chain-dir',chain,
                 '--transport-directory',T,'--based-points',based,'--canonical',canonical,'--derivative',derivative,
                 '--work-dir',F3,'--output-dir',F3,'--disk-id',disk,'--result-id',result,
                 '--f2-polynomial',poly,'--f2-audit',audit,
                 '--poly-source',S/'p41_selected_SS_F3_local_polynomial_all_unit_fractions_derivative47.py',
                 '--audit-source',S/'verify_moved_SS_F3_all_unit_fractions_derivative47.py'],completion)
        status=0
    except Exception as exc:
        error=type(exc).__name__+': '+str(exc);print('INCOMPLETE',result,error,flush=True)
    finally:
        f2files=preserve(W,O/'f2',disk);f3files=preserve(F3,O/'f3',disk)
        receipt={'result':result,'disk_id':disk,'complete':status==0,'exit_code':status,'error':error,
                 'execution_environment':'local','work_directory':str(W),'driver_sha256':sha(__file__),
                 'source_commit':source_commit,'original_R470_block':block['block_id'],
                 'based_points_sha256':sha(based),'original_initial_archive_sha256':sha(archive),
                 'initial_geometry_or_moving_flips_repeated':False,'long_chain_repeated_for_F3':False,
                 'elapsed_seconds':round(time.monotonic()-start,3),'completed_stages':completed,
                 'finished_at_utc':dt.datetime.now(dt.timezone.utc).isoformat(),'F2_files':f2files,'F3_files':f3files}
        if poly.exists():
            value=read(poly);receipt['F2_residual_roots']=value['residual_QC_roots']
            receipt['F2_entire_disk_excluded']=value['entire_disk_excluded_for_all_four_bad_components']
        p=F3/(disk+'_actual_canonical_F3_polynomial47.json.gz')
        if p.exists():
            value=read(p);receipt['F3_remaining_pairs']=value['remaining_F2_F3_candidate_and_component_pairs']
            receipt['F2_F3_entire_disk_excluded']=value['entire_disk_excluded_by_F2_and_F3_for_all_four_bad_components']
        receipt['files_over_repository_cap']=[str(p.relative_to(O)) for p in O.rglob('*') if p.is_file() and p.stat().st_size>=5_000_000]
        atomic_json(old_receipt,receipt)
        print('SAVED',result,'complete',receipt['complete'],'stages',len(completed),flush=True)
    return status


if __name__=='__main__':
    sys.exit(main())
