#!/usr/bin/env python3
"""Rebuild the actual SS_j10_11 F2 disk using integral finite-flat T2 pole constraints.

The default reuses its immutable 304-bit chain and repeats terminal transport,
principal flattening, genuine Hecke support, all Norms, center and polynomial.
--rebuild-chain executes the scalar chain again and retains all457 sections.
This entry point preserves every mathematical guard in the underlying engines.
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
import tarfile


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
 b=Path(p).read_bytes();return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)
def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--script-dir',type=Path,required=True);ap.add_argument('--work-dir',type=Path,required=True)
 ap.add_argument('--disk-id',default='SS_j10_11');ap.add_argument('--result-id',default='R372')
 ap.add_argument('--canonical',type=Path,required=True);ap.add_argument('--canonical-certificate',type=Path,required=True)
 ap.add_argument('--based-points',type=Path);ap.add_argument('--rebuild-chain',action='store_true')
 args=ap.parse_args();S=args.script_dir.resolve();D=S/'data';W=args.work_dir.resolve();d=args.disk_id
 assert d=='SS_j10_11' and args.result_id=='R372';W.mkdir(parents=True,exist_ok=True)
 env=dict(os.environ,OPENBLAS_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
 def link(source,target):
  source=source.resolve(strict=True);target.parent.mkdir(parents=True,exist_ok=True)
  if target.exists() or target.is_symlink():assert target.resolve(strict=True)==source
  else:target.symlink_to(source,target_is_directory=source.is_dir())
 def copy(source,target):
  content=source.read_bytes();target.parent.mkdir(parents=True,exist_ok=True)
  if target.exists():assert target.read_bytes()==content
  else:target.write_bytes(content)
 recovery=W/'recovery-inputs'
 for n in ['p41_rational_SS_second_kind_integrals47_complete.json.gz','p41_SS_second_kind_rhs47.json.gz']:link(D/n,recovery/n)
 link(D/'SS_second_kind_rhs47',recovery/'SS-second-kind-rhs')
 based=(args.based_points or D/(args.result_id+'_'+d+'_based_points47.json.gz')).resolve(strict=True)
 based_local=W/based.name;copy(based,based_local)
 chain=W/'chain';transport=W/'SS-principal-transports';chain.mkdir(exist_ok=True)
 completed=[]
 def run(label,name,argv,output):
  src=S/name;command=[sys.executable,'-u',str(src)]+list(map(str,argv));log=W/(label+'.log')
  with log.open('w') as stream:subprocess.run(command,env=env,stdout=stream,stderr=subprocess.STDOUT,check=True)
  assert output.exists();completed.append({'stage':label,'command':command,'source_sha256':sha(src),'output':str(output),'sha256':sha(output),'log':str(log)})
  p=W/'rebuild_checkpoint47.json';tmp=p.with_suffix('.new');tmp.write_text(json.dumps({'disk_id':d,'result':args.result_id,'completed_stages':completed},indent=2)+'\n');tmp.replace(p)
  print('PASS',label,sha(output),flush=True)
 mult=chain/(d+'_multiply47.json.gz');abel=chain/(d+'_Abel47.json.gz')
 if args.rebuild_chain:
  run('actual_chain','p41_SS_Abel_with_transports47.py',['--script-dir',S,'--SS-atlas',D/'p41_rational_SS_residue_atlas47_complete.json.gz','--common-based-points',D/'p41_all19_based_points47.json.gz','--based-points',based_local,'--disk',d,'--workdir',chain,'--transport-dir',transport,'--tiny',D/'p41_all129_tiny_Abel47_complete.json.gz'],abel)
 else:
  copy(D/mult.name,mult);copy(D/abel.name,abel)
  with tarfile.open(D/('p41_'+d+'_principal_transports47.tar.gz'),'r:gz') as tar:
   members=tar.getmembers();assert len(members)==459
   for item in members:
    p=Path(item.name);assert item.isfile() and not p.is_absolute() and '..' not in p.parts
    assert p.parts[0]=='SS-principal-transports'
    assert p.parts==('SS-principal-transports','run_manifest47.json') or (len(p.parts)==3 and p.parts[1]==d)
    destination=W/p;content=tar.extractfile(item).read();destination.parent.mkdir(parents=True,exist_ok=True)
    if destination.exists():assert destination.read_bytes()==content
    else:destination.write_bytes(content)
 second=W/(d+'_actual_second_kind_integrals47.json.gz');principal=W/(d+'_principal_expression47.json.gz');support=W/(d+'_actual_T2_support47.json.gz');t2norm=W/(d+'_actual_T2_principal_norm47.json.gz');fullnorm=W/(d+'_actual_F2_first_variable_norm47.json.gz');center=W/(d+'_actual_canonical_F2_height47.json.gz');poly=W/(d+'_actual_canonical_F2_polynomial47.json.gz')
 common=['--script-dir',S,'--based-points',based_local,'--second-kind-certificate',second,'--multiplication',mult,'--transport-directory',transport/d,'--principal-expression',principal]
 run('actual_terminal_and_nu','p41_SS_second_kind_from_principal47.py',['--script-dir',S,'--based-points',based_local,'--second-kind',D/'p41_second_kind_connection47.json.gz','--Abel',abel,'--multiplication',mult,'--transport-directory',transport/d,'--build-dir',W/'native-terminal','--output',second],second)
 run('actual_integer_principal','p41_principal_chain_flatten47.py',['--transport-directory',transport/d,'--second-kind-certificate',second,'--bases',D/'p41_hecke3_abel_bases_checkpoint.json.gz','--output',principal],principal)
 run('actual_T2_support','p41_CM48_disk_T2_support47.py',['--script-dir',S,'--disk-id',d,'--work-dir',W/'support','--output',support],support)
 polecert=W/(d+'_actual_confluent_T2_pole_constraints47.json.gz')
 run('finite_flat_pole_probe','p41_CM48_confluent_T2_pole_constraints47.py',['--script-dir',S,'--support',support,'--work-dir',W/'pole-probe','--output',polecert],polecert)
 run('actual_T2_norm','p41_ordinary_t2_etale_norm47.py',common+['--support',support,'--cache-dir',W/'T2-jets','--output',t2norm],t2norm)
 canonical=args.canonical.resolve(strict=True)
 run('actual_full_F2_norm','p41_SS_F2_full_canonical_norm47.py',common+['--canonical-algebra',canonical,'--canonical-unit-certificate',args.canonical_certificate.resolve(strict=True),'--ss-support',support,'--t2-norm',t2norm,'--cache-dir',W/'fixed-jets','--output',fullnorm],fullnorm)
 run('actual_finite_flat_F2_center','p41_selected_SS_F2_connection_finite_flat47.py',['--script-dir',S,'--recovery-dir',recovery,'--disk-id',d,'--result-id',args.result_id,'--second-kind',second,'--principal',principal,'--t2-support',support,'--full-norm',fullnorm,'--canonical',canonical,'--work-dir',W/'center','--output',center],center)
 run('actual_F2_polynomial','p41_selected_SS_F2_local_polynomial_all_unit_fractions47.py',['--script-dir',S,'--center',center,'--disk-id',d,'--result-id',args.result_id,'--abel',abel,'--multiply',mult,'--tiny',D/'p41_all129_second_kind_tiny47_complete.json.gz','--work-dir',W/'poly','--output',poly],poly)
 audit=W/(d+'-principal-F2-independent-audit.json')
 run('independent_audit','verify_selected_SS_F2_finite_flat47.py',['--script-dir',S,'--qc-dir',W,'--source-dir',S,'--center-source',S/'p41_selected_SS_F2_connection_finite_flat47.py','--poly-source',S/'p41_selected_SS_F2_local_polynomial_all_unit_fractions47.py','--polynomial',poly,'--chain-dir',chain,'--transport-dir',transport/d,'--based-points',based_local,'--disk-id',d,'--result-id',args.result_id,'--output',audit],audit)

if __name__=='__main__':main()
