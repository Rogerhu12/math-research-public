#!/usr/bin/env python3
"""Run one selected SS F3 calculation with explicit actual F2 polynomial and audit inputs.

No long group-chain execution is needed here. Every stage has an atomic
checkpoint, and resumed outputs must retain their source and input hashes.
"""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys


def read(p):
 b=Path(p).read_bytes();return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for n in ['script-dir','source-dir','recovery-dir','f2-dir','chain-dir','transport-directory','based-points','canonical','work-dir','output-dir']:ap.add_argument('--'+n,type=Path,required=True)
 ap.add_argument('--disk-id',required=True);ap.add_argument('--result-id',required=True)
 ap.add_argument('--poly-source',type=Path,required=True);ap.add_argument('--audit-source',type=Path,required=True)
 ap.add_argument('--f2-polynomial',type=Path,required=True);ap.add_argument('--f2-audit',type=Path,required=True)
 args=ap.parse_args();S=args.script_dir.resolve();A=args.source_dir.resolve();D=S/'data';F=args.f2_dir.resolve();C=args.chain_dir.resolve();W=args.work_dir.resolve();O=args.output_dir.resolve();R=args.recovery_dir.resolve();d=args.disk_id
 assert re.fullmatch(r'SS_j[0-9]+_[0-9]+',d);W.mkdir(parents=True,exist_ok=True);O.mkdir(parents=True,exist_ok=True)
 based=args.based_points.resolve(strict=True);trans=args.transport_directory.resolve(strict=True);canonical=args.canonical.resolve(strict=True)
 second=F/(d+'_actual_second_kind_integrals47.json.gz');principal=F/(d+'_principal_expression47.json.gz');mult=C/(d+'_multiply47.json.gz');abel=C/(d+'_Abel47.json.gz');f2norm=F/(d+'_actual_F2_first_variable_norm47.json.gz');f2poly=args.f2_polynomial.resolve(strict=True);f2audit=args.f2_audit.resolve(strict=True)
 p=read(f2poly);au=read(f2audit);assert p['disk_id']==au['disk_id']==d and p['complete_actual_local_sigma_F2_polynomial_on_disk']
 hashes=[v for k,v in au['input_sha256'].items() if Path(k).name==f2poly.name];assert hashes and set(hashes)=={sha(f2poly)}
 assert p['residual_QC_roots'], 'This disk was already excluded by its actual F2 function.'
 support=O/(d+'_actual_T3_support47.json.gz');t3norm=O/(d+'_actual_T3_principal_norm47.json.gz');fullnorm=O/(d+'_actual_F3_first_variable_norm47.json.gz');center=O/(d+'_actual_canonical_F3_height47.json.gz');poly=O/(d+'_actual_canonical_F3_polynomial47.json.gz');audit=O/(d+'-principal-F3-independent-audit.json')
 env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1');completed=[]
 def run(label,source,argv,output):
  command=[sys.executable,'-u',str(source)]+list(map(str,argv));log=W/(label+'.log')
  reused=output.exists()
  if reused:
   existing=read(output);assert existing['source_sha256']==sha(source),('changed source',label)
   for key,digest in existing.get('input_sha256',{}).items():
    pp=Path(key);candidates=[pp,D/pp.name,F/pp.name,C/pp.name,O/pp.name,based if pp.name==based.name else D/'__absent__']
    available=[x for x in candidates if x.is_file()]
    if available:assert any(sha(x)==digest for x in available),('changed input',label,key)
  else:
   with log.open('w') as stream:subprocess.run(command,env=env,stdout=stream,stderr=subprocess.STDOUT,check=True)
  assert output.exists();completed.append({'stage':label,'reused_existing_actual_certificate':reused,'executed_in_this_run':not reused,'source':str(source),'source_sha256':sha(source),'output':str(output),'sha256':sha(output),'bytes':output.stat().st_size,'command':command,'log':str(log)})
  checkpoint=W/'F3_checkpoint47.json';tmp=checkpoint.with_suffix('.new');tmp.write_text(json.dumps({'result':args.result_id,'disk_id':d,'completed_stages':completed,'source_sha256':sha(Path(__file__))},indent=2)+'\n');tmp.replace(checkpoint)
  print('PASS',args.result_id,d,label,sha(output),flush=True)
 common=['--script-dir',S,'--principal-expression',principal,'--transport-directory',trans,'--based-points',based,'--second-kind-certificate',second,'--multiplication',mult]
 run('actual_T3_support',A/'p41_selected_SS_T3_support47.py',['--script-dir',S,'--disk-id',d,'--work-dir',W/'support','--output',support],support)
 run('actual_T3_norm',S/'p41_ordinary_t3_split_norm47.py',common+['--support',support,'--cache-dir',W/'T3-jets','--output',t3norm],t3norm)
 run('actual_full_F3_norm',S/'p41_ordinary_F3_fixed_norm47.py',common+['--fixed-support',D/'p41_T3_fixed_divisor47.json.gz','--same-phi-F2-norm',f2norm,'--t3-norm',t3norm,'--canonical',canonical,'--cache-dir',W/'fixed-jets','--output',fullnorm],fullnorm)
 run('actual_F3_center',A/'p41_selected_SS_F3_connection47.py',['--script-dir',S,'--recovery-dir',R,'--disk-id',d,'--result-id',args.result_id,'--second-kind',second,'--principal',principal,'--t3-support',support,'--full-norm',fullnorm,'--fixed-support',D/'p41_T3_fixed_divisor47.json.gz','--cm11-second',D/'ORD_j38_second_kind_complete47.json.gz','--canonical',canonical,'--work-dir',W/'center','--output',center],center)
 run('actual_F3_polynomial',args.poly_source.resolve(),['--script-dir',S,'--center',center,'--disk-id',d,'--result-id',args.result_id,'--abel',abel,'--multiply',mult,'--tiny',D/'p41_all129_second_kind_tiny47_complete.json.gz','--f2-polynomial',f2poly,'--f2-audit',f2audit,'--work-dir',W/'poly','--output',poly],poly)
 run('independent_F3_audit',args.audit_source.resolve(),['--script-dir',S,'--source-dir',A,'--poly-source',args.poly_source.resolve(),'--disk-id',d,'--result-id',args.result_id,'--center',center,'--polynomial',poly,'--full-norm',fullnorm,'--t3-support',support,'--t3-norm',t3norm,'--principal',principal,'--second-kind',second,'--transport-directory',trans,'--f2-norm',f2norm,'--f2-polynomial',f2poly,'--f2-audit',f2audit,'--output',audit],audit)
 out={'result':args.result_id,'disk_id':d,'all_six_F3_stages_complete':True,'actual_F3_math_and_independent_audit_complete':True,'entire_disk_excluded':read(poly)['entire_disk_excluded_by_F2_and_F3_for_all_four_bad_components'],'remaining_pairs':read(poly)['remaining_F2_F3_candidate_and_component_pairs'],'polynomial_sha256':sha(poly),'audit_sha256':sha(audit),'completed_stages':completed,'source_sha256':sha(Path(__file__))}
 p=O/(args.result_id+'_'+d+'_F3_completion47.json');tmp=p.with_suffix('.new');tmp.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');tmp.replace(p)
 print('ACTUAL_F3_COMPLETE',args.result_id,d,'remaining',out['remaining_pairs'],flush=True)

if __name__=='__main__':main()
