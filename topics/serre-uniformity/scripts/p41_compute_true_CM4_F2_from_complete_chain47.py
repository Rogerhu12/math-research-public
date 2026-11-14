#!/usr/bin/env python3
"""Compute only missing CM4 F2 stages from the complete original R655 chain."""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for key in ['script-dir','work-dir']:
        ap.add_argument('--'+key,type=Path,required=True)
    ap.add_argument('--disk-id',choices=['SS_j36_06','SS_j36_02'],required=True)
    ap.add_argument('--result-id',required=True)
    args=ap.parse_args();S=args.script_dir.resolve();D=S/'data';W=args.work_dir.resolve();d=args.disk_id
    based=W/'p41_true_CM4_two_based_points47.json.gz';chain=W/'chain';transport=W/'SS-principal-transports'/d
    mult=chain/(d+'_multiply47.json.gz');abel=chain/(d+'_Abel47.json.gz')
    second=W/(d+'_actual_second_kind_integrals47.json.gz');principal=W/(d+'_principal_expression47.json.gz')
    frozen=read(W/'restored-original-inputs.json')
    for row in frozen['files']:
        assert sha(W/row['file'])==row['sha256'],row['file']
    state=read(mult);assert state['bits_done']==state['target_bits']==304
    assert state['input_sha256']==sha(based)
    assert read(transport/'transport_manifest47.json')['completed_Abel_sha256']==sha(abel)
    def link(source,target):
        source=source.resolve(strict=True);target.parent.mkdir(parents=True,exist_ok=True)
        if target.exists() or target.is_symlink():assert target.resolve(strict=True)==source
        else:target.symlink_to(source,target_is_directory=source.is_dir())
    recovery=W/'recovery-inputs'
    for name in ['p41_rational_SS_second_kind_integrals47_complete.json.gz','p41_SS_second_kind_rhs47.json.gz']:
        link(D/name,recovery/name)
    link(D/'SS_second_kind_rhs47',recovery/'SS-second-kind-rhs')
    checkpoint=W/'rebuild_checkpoint47.json';old=read(checkpoint) if checkpoint.exists() else None
    if old:assert old['disk_id']==d and old['result']==args.result_id
    saved={row['stage']:row for row in old['completed_stages']} if old else {};completed=[]
    def execute(label,name,arguments,output):
        source=S/name;command=[sys.executable,'-u',str(source)]+list(map(str,arguments))
        previous=saved.get(label);log=W/(label+'.log')
        if previous:
            assert previous['source_sha256']==sha(source) and previous['sha256']==sha(output)
        else:
            with log.open('w') as f:
                subprocess.run(command,stdout=f,stderr=subprocess.STDOUT,check=True,
                    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1'))
        completed.append({'stage':label,'command':command,'source_sha256':sha(source),
            'output':str(output),'sha256':sha(output),'reused_complete_stage':bool(previous)})
        tmp=checkpoint.with_suffix('.new');tmp.write_text(json.dumps({'result':args.result_id,
            'disk_id':d,'original_chain_repeated':False,'completed_stages':completed},indent=2)+'\n');tmp.replace(checkpoint)
        print('PASS',label,sha(output),flush=True)
    support=W/(d+'_actual_T2_support47.json.gz');t2norm=W/(d+'_actual_T2_principal_norm47.json.gz')
    fullnorm=W/(d+'_actual_F2_first_variable_norm47.json.gz');center=W/(d+'_actual_canonical_F2_height47.json.gz')
    poly=W/(d+'_actual_canonical_F2_polynomial47.json.gz');audit=W/(d+'-principal-F2-independent-audit.json')
    rc=D/'p41_true_CM4_regular_height_derivative47.json.gz';ra=D/'p41_true_CM4_regular_height_derivative47_independent.json'
    canonical=D/'p41_canonical_SS_robust47_raw.json.gz';cc=D/'p41_canonical_SS_robust47_certificate.json.gz'
    common=['--script-dir',S,'--based-points',based,'--second-kind-certificate',second,'--multiplication',mult,
        '--transport-directory',transport,'--principal-expression',principal]
    execute('actual_T2_support','p41_true_CM4_T2_support47.py',['--script-dir',S,'--disk-id',d,
        '--result-id',args.result_id,'--work-dir',W/'support','--output',support],support)
    execute('actual_T2_norm','p41_ordinary_t2_etale_norm47.py',common+['--support',support,
        '--cache-dir',W/'T2-jets','--output',t2norm],t2norm)
    execute('actual_full_F2_norm','p41_true_CM4_F2_full_canonical_norm47.py',common+['--derivative',rc,
        '--canonical-algebra',canonical,'--canonical-unit-certificate',cc,'--ss-support',support,
        '--t2-norm',t2norm,'--cache-dir',W/'fixed-jets','--output',fullnorm],fullnorm)
    execute('actual_F2_center','p41_true_CM4_F2_connection47.py',['--script-dir',S,'--recovery-dir',recovery,
        '--disk-id',d,'--result-id',args.result_id,'--second-kind',second,'--principal',principal,
        '--t2-support',support,'--full-norm',fullnorm,'--derivative',rc,'--canonical',canonical,
        '--work-dir',W/'center','--output',center],center)
    execute('actual_F2_polynomial','p41_true_CM4_F2_polynomial47.py',['--script-dir',S,
        '--ramified-j-certificate',rc,'--derivative',rc,'--center',center,'--disk-id',d,
        '--result-id',args.result_id,'--abel',abel,'--multiply',mult,
        '--tiny',D/'p41_all129_second_kind_tiny47_complete.json.gz','--work-dir',W/'poly','--output',poly],poly)
    execute('independent_audit','verify_true_CM4_F2_principal47.py',['--script-dir',S,
        '--ramified-j-certificate',rc,'--ramified-j-audit',ra,'--source-dir',S,
        '--poly-source',S/'p41_true_CM4_F2_polynomial47.py','--polynomial',poly,'--derivative',rc,
        '--norm-source',S/'p41_true_CM4_F2_full_canonical_norm47.py',
        '--center-source',S/'p41_true_CM4_F2_connection47.py','--qc-dir',W,'--chain-dir',chain,
        '--transport-dir',transport,'--based-points',based,'--disk-id',d,'--result-id',args.result_id,'--output',audit],audit)


if __name__=='__main__':
    main()
