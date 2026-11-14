#!/usr/bin/env python3
"""Resume an interrupted ramified scalar chain from its actual saved prefix.

This entry is for a failure during the first F2 stage. If any complete F2 stage
beyond the chain is already present, it requires consuming that checkpoint
explicitly; it never silently repeats a completed Norm or height calculation.
"""
import argparse,datetime,gzip,hashlib,json,os,subprocess,sys,time
from pathlib import Path

def read(p):
    p=Path(p);b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ['script-dir','work-dir','output']:ap.add_argument('--'+name,type=Path,required=True)
    for name in ['result-id','disk-id']:ap.add_argument('--'+name,required=True)
    args=ap.parse_args();S=args.script_dir.resolve();D=S/'data';W=args.work_dir.resolve();O=args.output.resolve()
    disk=args.disk_id;result=args.result_id;f2=W/'f2';f3=W/'f3'
    sys.path.insert(0,str(S));from p41_ci_recover_ramified_ss47 import preserve
    based=W/(result+'_'+disk+'_based_points47.json.gz');assert based.is_file()
    mult=f2/'chain'/(disk+'_multiply47.json.gz');initial=read(mult)
    assert initial['disk_id']==disk and 0<initial['bits_done']<=initial['target_bits']==304
    initial_sha=sha(mult);initial_bits=initial['bits_done']
    poly=f2/(disk+'_actual_canonical_F2_polynomial47.json.gz')
    cp=f2/'rebuild_checkpoint47.json'
    if not poly.exists() and cp.exists():
        assert not read(cp)['completed_stages'], 'Consume completed F2 stages without rerunning them.'
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
    start=time.monotonic();stages=[];error=None;status=1
    def run(label,source,argv):
        command=[sys.executable,'-u',str(source)]+list(map(str,argv));print('START',result,label,flush=True)
        subprocess.run(command,env=env,check=True)
        stages.append({'stage':label,'command':command,'source_sha256':sha(source)})
    try:
        if not poly.exists():
            run('resume_actual_F2',S/'p41_rebuild_ramified_SS_F2_unit_parameter47.py',[
                '--script-dir',S,'--work-dir',f2,'--disk-id',disk,'--result-id',result,
                '--canonical',D/'p41_canonical_SS_robust47_raw.json.gz',
                '--canonical-certificate',D/'p41_canonical_SS_robust47_certificate.json.gz',
                '--derivative',D/'p41_serre_clearing_126_disks47.json.gz',
                '--ramified-j-certificate',D/'p41_ramified_j_regular_height_derivative47.json.gz',
                '--ramified-j-audit',D/'p41_ramified_j_regular_height_derivative47_independent.json',
                '--based-points',based,'--rebuild-chain'])
        if read(poly)['residual_QC_roots']:
            run('actual_same_chain_F3',S/'p41_rebuild_ramified_SS_F3_unit_parameter47.py',[
                '--script-dir',S,'--source-dir',S,'--f2-dir',f2,'--recovery-dir',f2/'recovery-inputs',
                '--based-points',f2/based.name,'--canonical',D/'p41_canonical_SS_robust47_raw.json.gz',
                '--derivative',D/'p41_serre_clearing_126_disks47.json.gz',
                '--ramified-j-certificate',D/'p41_ramified_j_regular_height_derivative47.json.gz',
                '--ramified-j-audit',D/'p41_ramified_j_regular_height_derivative47_independent.json',
                '--work-dir',f3,'--disk-id',disk,'--result-id',result])
        status=0
    except Exception as exc:
        error=type(exc).__name__+': '+str(exc);print('INCOMPLETE',result,error,flush=True)
    finally:
        files2=preserve(f2,O/'f2',disk);files3=preserve(f3,O/'f3',disk)
        receipt={'result':result,'disk_id':disk,'complete':status==0,'exit_code':status,'error':error,
                 'work_directory':str(W),'initial_saved_bits':initial_bits,'initial_multiply_sha256':initial_sha,
                 'saved_chain_prefix_repeated':False,'long_chain_repeated_for_F3':False,
                 'driver_sha256':sha(__file__),'elapsed_seconds':round(time.monotonic()-start,3),
                 'finished_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'stages':stages,
                 'F2_files':files2,'F3_files':files3,'execution_environment':'local'}
        if poly.exists():
            value=read(poly);receipt['F2_residual_roots']=value['residual_QC_roots']
            receipt['F2_entire_disk_excluded']=value['entire_disk_excluded_for_all_four_bad_components']
        p=f3/(disk+'_actual_canonical_F3_polynomial47.json.gz')
        if p.exists():
            value=read(p);receipt['F3_remaining_pairs']=value['remaining_F2_F3_candidate_and_component_pairs']
            receipt['F2_F3_entire_disk_excluded']=value['entire_disk_excluded_by_F2_and_F3_for_all_four_bad_components']
        (O/'run-receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
        print('SAVED',result,'complete',receipt['complete'],flush=True)
    return status

if __name__=='__main__':sys.exit(main())
