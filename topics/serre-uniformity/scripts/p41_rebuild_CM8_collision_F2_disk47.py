#!/usr/bin/env python3
"""Rebuild the actual CM8-collision SS_j10_06 F2 disk and its joint Norm/Laurent cancellation.

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
 ap.add_argument('--disk-id',default='SS_j10_06');ap.add_argument('--result-id',default='R368')
 ap.add_argument('--canonical',type=Path,required=True);ap.add_argument('--canonical-certificate',type=Path,required=True)
 ap.add_argument('--based-points',type=Path);ap.add_argument('--rebuild-chain',action='store_true')
 args=ap.parse_args();S=args.script_dir.resolve();D=S/'data';W=args.work_dir.resolve();d=args.disk_id
 assert d=='SS_j10_06' and args.result_id=='R368';W.mkdir(parents=True,exist_ok=True)
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
 second=W/(d+'_actual_second_kind_integrals47.json.gz');principal=W/(d+'_principal_expression47.json.gz');support=W/(d+'_actual_T2_diagonal_support47.json.gz');t2norm=W/(d+'_actual_T2_principal_unit_parts47.json.gz');fullnorm=W/(d+'_actual_F2_joint_first_variable_norm47.json.gz');center=W/(d+'_actual_canonical_F2_height47.json.gz');poly=W/(d+'_actual_canonical_F2_polynomial47.json.gz')
 common=['--script-dir',S,'--based-points',based_local,'--second-kind-certificate',second,'--multiplication',mult,'--transport-directory',transport/d,'--principal-expression',principal]
 run('actual_terminal_and_nu','p41_SS_second_kind_from_principal47.py',['--script-dir',S,'--based-points',based_local,'--second-kind',D/'p41_second_kind_connection47.json.gz','--Abel',abel,'--multiplication',mult,'--transport-directory',transport/d,'--build-dir',W/'native-terminal','--output',second],second)
 run('actual_integer_principal','p41_principal_chain_flatten47.py',['--transport-directory',transport/d,'--second-kind-certificate',second,'--bases',D/'p41_hecke3_abel_bases_checkpoint.json.gz','--output',principal],principal)
 run('actual_T2_support','p41_selected_SS_T2_diagonal_support47.py',['--script-dir',S,'--disk-id',d,'--work-dir',W/'support','--output',support],support)
 run('actual_T2_norm','p41_CM8_T2_principal_unit_parts47.py',common+['--support',support,'--cache-dir',W/'T2-jets','--output',t2norm],t2norm)
 canonical=args.canonical.resolve(strict=True)
 horizontal=W/'p41_CM8_horizontal_j_unit47.json.gz'
 run('true_horizontal_j_unit','p41_CM8_horizontal_unit47.py',['--j',3449387,'--output',horizontal],horizontal)
 run('actual_full_F2_norm','p41_CM8_joint_F2_principal_norm47.py',common+['--canonical-algebra',canonical,'--canonical-unit-certificate',args.canonical_certificate.resolve(strict=True),'--horizontal-unit',horizontal,'--ss-support',support,'--t2-norm',t2norm,'--cache-dir',W/'fixed-jets','--output',fullnorm],fullnorm)
 run('actual_F2_center','p41_CM8_selected_SS_F2_connection47.py',['--script-dir',S,'--recovery-dir',recovery,'--disk-id',d,'--result-id',args.result_id,'--second-kind',second,'--principal',principal,'--t2-support',support,'--full-norm',fullnorm,'--canonical',canonical,'--work-dir',W/'center','--output',center],center)
 branches=W/(d+'_actual_CM8_T2_local_branches47.json.gz')
 reference=W/(d+'_actual_CM8_C_and_fixed_connections47.json.gz')
 difference=W/(d+'_actual_CM8_F2_height_difference47.json.gz')
 run('true_CM8_T2_jets','p41_CM8_T2_local_branches47.py',['--script-dir',S,'--support',support,'--disk-id',d,'--work-dir',W/'branches','--output',branches],branches)
 run('true_CM8_C_connection','p41_CM8_actual_C_and_fixed_connections47.py',['--script-dir',S,'--branches',branches,'--fixed-reference',D/'SS_j10_05_actual_F2_connections47.json.gz','--work-dir',W/'CM-connection','--output',reference],reference)
 run('joint_Laurent_differential','p41_CM8_F2_Laurent_height_difference47.py',['--script-dir',S,'--branches',branches,'--reference-connections',reference,'--work-dir',W/'CM-Laurent','--output',difference],difference)
 run('actual_F2_polynomial','p41_CM8_assemble_actual_F2_disk47.py',['--script-dir',S,'--center',center,'--difference',difference,'--branches',branches,'--abel',abel,'--multiply',mult,'--output',poly],poly)
 for name in ['p41_CM8_selected_SS_F2_connection47.py','p41_CM8_assemble_actual_F2_disk47.py','p41_CM8_F2_Laurent_height_difference47.py','p41_CM8_T2_principal_unit_parts47.py','p41_CM8_joint_F2_principal_norm47.py']:link(S/name,W/name)
 audit=W/(d+'-principal-F2-independent-audit.json')
 run('independent_audit','verify_CM8_actual_F2_disk47.py',['--script-dir',S,'--qc-dir',W,'--chain-dir',chain,'--transport-dir',transport/d,'--based-points',based_local,'--disk-id',d,'--output',audit],audit)

if __name__=='__main__':main()
