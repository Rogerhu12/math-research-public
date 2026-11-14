#!/usr/bin/env python3
"""Complete ramified-j F3 from one already audited F2 chain, in unit parameter z.

All long-chain inputs are read-only. Each actual short stage is checkpointed.
"""
import argparse,gzip,hashlib,json,os,re,subprocess,sys
from pathlib import Path

def read(p):
 raw=Path(p).read_bytes();return json.loads(gzip.decompress(raw) if str(p).endswith('.gz') else raw)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ['script-dir','source-dir','f2-dir','recovery-dir','based-points','canonical','derivative','ramified-j-certificate','ramified-j-audit','work-dir']:
  ap.add_argument('--'+k,type=Path,required=True)
 ap.add_argument('--disk-id',required=True);ap.add_argument('--result-id',required=True)
 args=ap.parse_args();S=args.script_dir.resolve();A=args.source_dir.resolve();D=S/'data';F=args.f2_dir.resolve();W=args.work_dir.resolve();d=args.disk_id
 assert re.fullmatch(r'SS_j(?:0|36)_[0-9]+',d)
 W.mkdir(parents=True,exist_ok=True)
 based=args.based_points.resolve(strict=True);canonical=args.canonical.resolve(strict=True)
 second=F/(d+'_actual_second_kind_integrals47.json.gz');flat=F/(d+'_principal_expression47.json.gz')
 mult=F/'chain'/(d+'_multiply47.json.gz');abel=F/'chain'/(d+'_Abel47.json.gz')
 trans=F/'SS-principal-transports'/d
 f2norm=F/(d+'_actual_F2_first_variable_norm47.json.gz')
 f2poly=F/(d+'_actual_canonical_F2_polynomial47.json.gz');f2audit=F/(d+'-principal-F2-independent-audit.json')
 for p in [second,flat,mult,abel,f2norm,f2poly,f2audit,trans/'transport_manifest47.json']:assert p.is_file(),p
 fp,fa=read(f2poly),read(f2audit);assert fp['disk_id']==fa['disk_id']==d
 assert fp['complete_actual_local_sigma_F2_polynomial_on_disk'] and fp['residual_QC_roots']
 assert set(v for k,v in fa['input_sha256'].items() if Path(k).name==f2poly.name)=={sha(f2poly)}
 support=W/(d+'_actual_T3_support47.json.gz');tnorm=W/(d+'_actual_T3_principal_norm47.json.gz')
 norm=W/(d+'_actual_F3_first_variable_norm47.json.gz');center=W/(d+'_actual_canonical_F3_height47.json.gz')
 poly=W/(d+'_actual_canonical_F3_polynomial47.json.gz');audit=W/(d+'-principal-F3-independent-audit.json')
 env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
 stages=[]
 def run(label,source,argv,out):
  cmd=[sys.executable,'-u',str(source)]+[str(v) for v in argv];log=W/(label+'.log')
  reused=out.is_file()
  if reused:
   old=read(out);assert old['source_sha256']==sha(source),(label,'source changed')
   for k,v in old.get('input_sha256',{}).items():
    p=Path(k);candidates=[p,D/p.name,F/p.name,F/'chain'/p.name,W/p.name,based if p.name==based.name else D/'__missing__']
    present=[p for p in candidates if p.is_file()]
    if present:assert any(sha(p)==v for p in present),(label,'changed input',k)
  else:
   with log.open('w') as h:subprocess.run(cmd,stdout=h,stderr=subprocess.STDOUT,env=env,check=True)
  assert out.is_file()
  stages.append({'stage':label,'source':str(source),'source_sha256':sha(source),'command':cmd,
                 'output':str(out),'sha256':sha(out),'bytes':out.stat().st_size,'log':str(log),
                 'reused_actual_output':reused,'actually_executed_in_this_invocation':not reused})
  p=W/'F3_checkpoint47.json';tmp=p.with_suffix('.new')
  tmp.write_text(json.dumps({'result':args.result_id,'disk_id':d,'completed_stages':stages,'source_sha256':sha(__file__)},indent=2)+'\n');tmp.replace(p)
  print('PASS',args.result_id,label,sha(out),flush=True)
 common=['--script-dir',S,'--principal-expression',flat,'--transport-directory',trans,'--based-points',based,'--second-kind-certificate',second,'--multiplication',mult]
 run('actual_T3_support',A/'p41_selected_ramified_SS_T3_support47.py',
     ['--script-dir',S,'--disk-id',d,'--result-id',args.result_id,'--work-dir',W/'support','--output',support],support)
 run('actual_T3_norm',S/'p41_ordinary_t3_split_norm47.py',common+['--support',support,'--cache-dir',W/'T3-jets','--output',tnorm],tnorm)
 nsrc=A/'p41_SS_F3_fixed_norm_ramified_unit_parameter47.py'
 csrc=A/'p41_selected_SS_F3_connection_ramified_unit_parameter47.py'
 psrc=A/'p41_selected_SS_F3_polynomial_ramified_unit_parameter47.py'
 run('actual_full_F3_norm',nsrc,common+['--fixed-support',D/'p41_T3_fixed_divisor47.json.gz','--same-phi-F2-norm',f2norm,'--t3-norm',tnorm,'--canonical',canonical,'--derivative',args.derivative,'--cache-dir',W/'fixed-jets','--output',norm],norm)
 run('actual_F3_center',csrc,['--script-dir',S,'--recovery-dir',args.recovery_dir,'--disk-id',d,'--result-id',args.result_id,'--second-kind',second,'--principal',flat,'--t3-support',support,'--full-norm',norm,'--fixed-support',D/'p41_T3_fixed_divisor47.json.gz','--cm11-second',D/'ORD_j38_second_kind_complete47.json.gz','--canonical',canonical,'--derivative',args.derivative,'--work-dir',W/'center','--output',center],center)
 run('actual_F3_polynomial',psrc,['--script-dir',S,'--center',center,'--disk-id',d,'--result-id',args.result_id,'--abel',abel,'--multiply',mult,'--tiny',D/'p41_all129_second_kind_tiny47_complete.json.gz','--f2-polynomial',f2poly,'--f2-audit',f2audit,'--t3-support',support,'--derivative',args.derivative,'--ramified-j-certificate',args.ramified_j_certificate,'--work-dir',W/'poly','--output',poly],poly)
 run('independent_F3_audit',A/'verify_selected_SS_F3_ramified_unit_parameter47.py',
     ['--script-dir',S,'--source-dir',S,'--center-source',csrc,'--norm-source',nsrc,'--poly-source',psrc,'--derivative',args.derivative,'--ramified-j-certificate',args.ramified_j_certificate,'--ramified-j-audit',args.ramified_j_audit,'--disk-id',d,'--result-id',args.result_id,'--center',center,'--polynomial',poly,'--full-norm',norm,'--t3-support',support,'--t3-norm',tnorm,'--principal',flat,'--second-kind',second,'--transport-directory',trans,'--f2-norm',f2norm,'--f2-polynomial',f2poly,'--f2-audit',f2audit,'--output',audit],audit)
 output={'result':args.result_id,'disk_id':d,'all_six_F3_stages_complete':True,
  'entire_disk_excluded':read(poly)['entire_disk_excluded_by_F2_and_F3_for_all_four_bad_components'],
  'remaining_pairs':read(poly)['remaining_F2_F3_candidate_and_component_pairs'],
  'completed_stages':stages,'polynomial_sha256':sha(poly),'audit_sha256':sha(audit),
  'long_chain_repeated':False,'source_sha256':sha(__file__)}
 dest=W/(args.result_id+'_'+d+'_F3_completion47.json');dest.write_text(json.dumps(output,indent=2)+'\n')
 print('ACTUAL_F3_COMPLETE',args.result_id,d,'remaining',output['remaining_pairs'],flush=True)
if __name__=='__main__':main()
