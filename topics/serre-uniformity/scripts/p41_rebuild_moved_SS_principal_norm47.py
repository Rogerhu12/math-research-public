#!/usr/bin/env python3
"""Portable R399 reconstruction on the unchanged820-point evaluation model.

Default: independently audit all four frozen real initial moves, restore the
first complete459-function chain, and recompute terminal transport, exact SLP,
all three actual V2 Norms and the independent integer Norm audit.
--rebuild-chain repeats the304-bit chain. --rebuild-moving also rebuilds the
four moves and requires --rebuild-chain, so no old chain is bound to new inputs.
"""
import argparse,gzip,hashlib,json,os,subprocess,sys,tarfile,time
from pathlib import Path

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
 p=Path(p);b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for n in ['script-dir','work-dir','canonical','canonical-unit-certificate','derivative']:ap.add_argument('--'+n,type=Path,required=True)
 ap.add_argument('--source-dir',type=Path);ap.add_argument('--disk-id',default='SS_j9_01')
 ap.add_argument('--based-points',type=Path);ap.add_argument('--t2-support',type=Path)
 ap.add_argument('--rebuild-moving',action='store_true');ap.add_argument('--rebuild-chain',action='store_true')
 ap.add_argument('--rebuild-support',action='store_true')
 args=ap.parse_args();S=args.script_dir.resolve();D=S/'data';A=(args.source_dir or S).resolve();W=args.work_dir.resolve();d=args.disk_id
 assert d in ['SS_j9_01','SS_j9_02','SS_j9_03','SS_j9_04']
 assert not args.rebuild_moving or args.rebuild_chain,'A freshly regenerated moving-data hash requires its own chain.'
 W.mkdir(parents=True,exist_ok=True);env=dict(os.environ,OPENBLAS_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1');done=[]
 def copy(src,dst):
  src=src.resolve(strict=True);dst.parent.mkdir(parents=True,exist_ok=True);b=src.read_bytes()
  if dst.exists():assert dst.read_bytes()==b
  else:dst.write_bytes(b)
 def source(name):
  p=A/name
  if not p.is_file():p=S/name
  assert p.is_file(),str(p)
  return p
 def run(label,name,argv,output):
  src=source(name);command=[sys.executable,'-u',str(src)]+list(map(str,argv));log=W/(label+'.log')
  with log.open('w') as stream:
   proc=subprocess.Popen(command,env=env,stdout=stream,stderr=subprocess.STDOUT)
   while proc.poll() is None:
    print('HEARTBEAT',label,time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),flush=True)
    try:proc.wait(timeout=30)
    except subprocess.TimeoutExpired:pass
   if proc.returncode:raise RuntimeError((label,proc.returncode,str(log)))
  assert output.is_file();done.append({'stage':label,'command':command,'source_sha256':sha(src),'output':str(output),'sha256':sha(output),'log':str(log)})
  p=W/'R399_rebuild_checkpoint47.json';tmp=p.with_suffix('.new');tmp.write_text(json.dumps({'result':'R399','disk_id':d,'completed_stages':done},indent=2)+'\n');tmp.replace(p)
  print('PASS',label,sha(output),flush=True)
 based=W/'p41_j9_first_four_moved_based_points47.json.gz'
 if args.rebuild_moving:
  argv=['--script-dir',S,'--SS-atlas',D/'p41_rational_SS_residue_atlas47_complete.json.gz','--common-based-points',D/'p41_all19_based_points47.json.gz','--based-points',based,'--workdir',W/'moving-work']
  for disk in ['SS_j9_01','SS_j9_02','SS_j9_03','SS_j9_04']:argv+=['--disk',disk]
  run('four_actual_initial_moves','p41_SS_evaluation_collision_moving_points47.py',argv,based)
 else:copy(args.based_points or D/based.name,based)
 movingaudit=W/'p41_j9_moving_two_flip_independent_audit47.json'
 run('independent_four_moving_flips','verify_SS_initial_moving_flips47.py',['--script-dir',S,'--based-points',based,'--common-based-points',D/'p41_all19_based_points47.json.gz','--SS-atlas',D/'p41_rational_SS_residue_atlas47_complete.json.gz','--output',movingaudit],movingaudit)
 chain=W/'chain';chain.mkdir(exist_ok=True);transport=W/'SS-principal-transports';T=transport/d
 mult=chain/(d+'_multiply47.json.gz');abel=chain/(d+'_Abel47.json.gz')
 if args.rebuild_chain:
  run('actual_moved_chain','p41_moved_SS_Abel_with_transports47.py',['--script-dir',S,'--SS-atlas',D/'p41_rational_SS_residue_atlas47_complete.json.gz','--common-based-points',D/'p41_all19_based_points47.json.gz','--based-points',based,'--disk',d,'--workdir',chain,'--transport-dir',transport,'--tiny',D/'p41_all129_tiny_Abel47_complete.json.gz','--max-bits',304],abel)
 else:
  copy(D/mult.name,mult);copy(D/abel.name,abel)
  assert read(mult)['input_sha256']==sha(based)
  archive=D/('p41_'+d+'_principal_transports47.tar.gz')
  with tarfile.open(archive,'r:gz') as tf:
   members=tf.getmembers();assert len(members)==461
   for item in members:
    p=Path(item.name);assert item.isfile() and not p.is_absolute() and '..' not in p.parts
    assert p.parts==('SS-principal-transports','run_manifest47.json') or (len(p.parts)==3 and p.parts[:2]==('SS-principal-transports',d))
    dst=W/p;b=tf.extractfile(item).read();dst.parent.mkdir(parents=True,exist_ok=True)
    if dst.exists():assert dst.read_bytes()==b
    else:dst.write_bytes(b)
  man=read(T/'transport_manifest47.json');assert len(man['functions'])==459
  for f in man['functions']:
   p=T/f['filename'];assert sha(p)==f['sha256'] and p.stat().st_size==f['bytes']
  assert man['completed_Abel_sha256']==sha(abel) and man['multiplication_sha256']==sha(mult)
 support=W/(d+'_actual_T2_support47.json.gz')
 if args.rebuild_support:
  run('actual_three_T2_branches','p41_selected_nonelliptic_SS_T2_support47.py',['--script-dir',S,'--disk-id',d,'--result-id','R399','--work-dir',W/'T2-support','--output',support],support)
 else:copy(args.t2_support or D/support.name,support)
 second=W/(d+'_actual_second_kind_integrals47.json.gz');flat=W/(d+'_principal_expression47.json.gz');t2=W/(d+'_actual_T2_principal_norm47.json.gz');full=W/(d+'_actual_F2_first_variable_norm47.json.gz')
 common=['--script-dir',S,'--based-points',based,'--second-kind-certificate',second,'--multiplication',mult,'--transport-directory',T,'--principal-expression',flat]
 run('actual_terminal_and_nu','p41_moved_SS_second_kind_from_principal47.py',['--script-dir',S,'--based-points',based,'--second-kind',D/'p41_second_kind_connection47.json.gz','--Abel',abel,'--multiplication',mult,'--transport-directory',T,'--build-dir',W/'terminal-native','--output',second],second)
 run('integer_principal_SLP','p41_moved_principal_chain_flatten47.py',['--transport-directory',T,'--second-kind-certificate',second,'--bases',D/'p41_hecke3_abel_bases_checkpoint.json.gz','--output',flat],flat)
 run('actual_three_branch_Norm','p41_moved_SS_T2_norm47.py',common+['--support',support,'--cache-dir',W/'T2-jets','--output',t2],t2)
 run('actual_full_F2_Norm','p41_moved_SS_F2_full_canonical_norm_clearing_frame47.py',common+['--canonical-algebra',args.canonical.resolve(strict=True),'--canonical-unit-certificate',args.canonical_unit_certificate.resolve(strict=True),'--derivative',args.derivative.resolve(strict=True),'--ss-support',support,'--t2-norm',t2,'--cache-dir',W/'fixed-jets','--output',full],full)
 audit=W/(d+'-moved-principal-Norm-independent-audit.json')
 run('independent_principal_and_Norm','verify_moved_SS_principal_norm47.py',['--script-dir',S,'--source-dir',A,'--qc-dir',W,'--chain-dir',chain,'--transport-dir',T,'--based-points',based,'--moving-audit',movingaudit,'--t2-support',support,'--derivative',args.derivative.resolve(strict=True),'--disk-id',d,'--output',audit],audit)
 print('COMPLETE R399 actual moved principal/Norm',d,sha(audit),flush=True)
if __name__=='__main__':main()
