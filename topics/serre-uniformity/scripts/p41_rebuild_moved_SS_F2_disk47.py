#!/usr/bin/env python3
"""Rebuild one moved-representative j9 F2 center/disk from its immutable full chain.

The R399 Norm and exact integer expression are independently replayed first;
then the frozen explicit-frame center and dynamic polynomial are executed.
Use p41_rebuild_moved_SS_principal_norm47.py to rerun the expensive chain/Norm.
"""
import argparse,gzip,hashlib,json,os,subprocess,sys,tarfile,time
from pathlib import Path

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
 p=Path(p);b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for n in ['script-dir','work-dir','canonical','derivative']:ap.add_argument('--'+n,type=Path,required=True)
 ap.add_argument('--disk-id',default='SS_j9_01');ap.add_argument('--result-id',default='R382');args=ap.parse_args()
 S=args.script_dir.resolve();D=S/'data';W=args.work_dir.resolve();d=args.disk_id;res=args.result_id
 assert {f'SS_j9_{i:02d}':'R'+str(381+i) for i in range(1,5)}[d]==res
 W.mkdir(parents=True,exist_ok=True);env=dict(os.environ,OPENBLAS_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1');done=[]
 def copy(src,dst):
  src=src.resolve(strict=True);dst.parent.mkdir(parents=True,exist_ok=True);b=src.read_bytes()
  if dst.exists():assert dst.read_bytes()==b
  else:dst.write_bytes(b)
 def link(src,dst):
  src=src.resolve(strict=True);dst.parent.mkdir(parents=True,exist_ok=True)
  if dst.exists() or dst.is_symlink():assert dst.resolve(strict=True)==src
  else:dst.symlink_to(src,target_is_directory=src.is_dir())
 recovery=W/'recovery-inputs'
 for name in ['p41_rational_SS_second_kind_integrals47_complete.json.gz','p41_SS_second_kind_rhs47.json.gz']:link(D/name,recovery/name)
 link(D/'SS_second_kind_rhs47',recovery/'SS-second-kind-rhs')
 chain=W/'chain';chain.mkdir(exist_ok=True);T=W/'SS-principal-transports'/d
 for n in [d+'_multiply47.json.gz',d+'_Abel47.json.gz']:copy(D/n,chain/n)
 names=['p41_j9_first_four_moved_based_points47.json.gz','p41_j9_moving_two_flip_independent_audit47.json',d+'_actual_second_kind_integrals47.json.gz',d+'_principal_expression47.json.gz',d+'_actual_T2_support47.json.gz',d+'_actual_T2_principal_norm47.json.gz',d+'_actual_F2_first_variable_norm47.json.gz']
 for name in names:copy(D/name,W/name)
 with tarfile.open(D/('p41_'+d+'_principal_transports47.tar.gz'),'r:gz') as tf:
  members=tf.getmembers();assert len(members)==461
  for member in members:
   p=Path(member.name);assert member.isfile() and not p.is_absolute() and '..' not in p.parts
   assert p.parts==('SS-principal-transports','run_manifest47.json') or (len(p.parts)==3 and p.parts[:2]==('SS-principal-transports',d))
   dst=W/p;b=tf.extractfile(member).read();dst.parent.mkdir(parents=True,exist_ok=True)
   if dst.exists():assert dst.read_bytes()==b
   else:dst.write_bytes(b)
 man=read(T/'transport_manifest47.json');assert len(man['functions'])==459
 for f in man['functions']:
  p=T/f['filename'];assert sha(p)==f['sha256'] and p.stat().st_size==f['bytes']
 def run(label,name,argv,output):
  source=S/name;command=[sys.executable,'-u',str(source)]+list(map(str,argv));log=W/(label+'.log')
  with log.open('w') as stream:
   p=subprocess.Popen(command,env=env,stdout=stream,stderr=subprocess.STDOUT)
   while p.poll() is None:
    print('HEARTBEAT',res,d,label,time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),flush=True)
    try:p.wait(timeout=25)
    except subprocess.TimeoutExpired:pass
   if p.returncode:raise RuntimeError((label,p.returncode,str(log)))
  done.append({'stage':label,'command':command,'source_sha256':sha(source),'output':str(output),'sha256':sha(output),'log':str(log)})
  path=W/'F2_rebuild_checkpoint47.json';tmp=path.with_suffix('.new');tmp.write_text(json.dumps({'result':res,'disk_id':d,'completed_stages':done},indent=2)+'\n');tmp.replace(path)
  print('PASS',label,sha(output),flush=True)
 based=W/names[0];moving=W/names[1];second=W/names[2];principal=W/names[3];support=W/names[4];full=W/names[6];deriv=args.derivative.resolve(strict=True);canonical=args.canonical.resolve(strict=True)
 common=['--script-dir',S,'--source-dir',S,'--qc-dir',W,'--chain-dir',chain,'--transport-dir',T,'--based-points',based,'--moving-audit',moving,'--t2-support',support,'--derivative',deriv,'--disk-id',d]
 na=W/(d+'-moved-principal-Norm-independent-audit.json')
 run('independent_actual_moved_Norm','verify_moved_SS_principal_norm47.py',common+['--output',na],na)
 center=W/(d+'_actual_canonical_F2_height47.json.gz');poly=W/(d+'_actual_canonical_F2_polynomial47.json.gz');audit=W/(d+'-principal-F2-independent-audit.json')
 cs=S/'p41_selected_SS_F2_connection_clearing_frame47.py';ps=S/'p41_selected_SS_F2_polynomial_clearing_frame47.py'
 run('actual_F2_center',cs.name,['--script-dir',S,'--recovery-dir',recovery,'--disk-id',d,'--result-id',res,'--second-kind',second,'--principal',principal,'--t2-support',support,'--full-norm',full,'--canonical',canonical,'--derivative',deriv,'--work-dir',W/'center','--output',center],center)
 run('actual_F2_disk',ps.name,['--script-dir',S,'--center',center,'--disk-id',d,'--result-id',res,'--abel',chain/(d+'_Abel47.json.gz'),'--multiply',chain/(d+'_multiply47.json.gz'),'--tiny',D/'p41_all129_second_kind_tiny47_complete.json.gz','--derivative',deriv,'--work-dir',W/'poly','--output',poly],poly)
 run('independent_complete_F2','verify_moved_SS_F2_clearing_frame47.py',common+['--result-id',res,'--norm-source',S/'p41_moved_SS_F2_full_canonical_norm_clearing_frame47.py','--center-source',cs,'--poly-source',ps,'--polynomial',poly,'--output',audit],audit)
if __name__=='__main__':main()
