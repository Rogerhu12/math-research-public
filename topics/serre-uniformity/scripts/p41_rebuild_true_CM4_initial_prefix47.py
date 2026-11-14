#!/usr/bin/env python3
"""Restore and independently replay the R552 true-CM4 initial prefixes.

The optional --continue-chain resumes both disks sequentially through the
unchanged retained-principal engine. R552 itself claims only the saved initial
geometry and actual one-bit prefixes, not those optional future computations.
"""
import argparse,gzip,hashlib,json,os,subprocess,sys,tarfile,time
from pathlib import Path
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for n in ['script-dir','work-dir']:ap.add_argument('--'+n,type=Path,required=True)
 ap.add_argument('--continue-chain',action='store_true');args=ap.parse_args();S=args.script_dir.resolve();D=S/'data';W=args.work_dir.resolve();W.mkdir(parents=True,exist_ok=True)
 with tarfile.open(D/'p41_true_CM4_initial_prefix47.tar.gz','r:gz') as tf:
  members=tf.getmembers();assert len(members)==6
  for m in members:
   pp=Path(m.name);assert m.isfile() and not pp.is_absolute() and '..' not in pp.parts and pp.parts[0]=='CM4-initial-prefix'
   p=W/pp;b=tf.extractfile(m).read();p.parent.mkdir(parents=True,exist_ok=True)
   if p.exists():assert p.read_bytes()==b
   else:p.write_bytes(b)
 root=W/'CM4-initial-prefix';manifest=json.loads((root/'prefix_manifest47.json').read_text());assert manifest['disk_ids']==['SS_j36_06','SS_j36_02'] and manifest['actual_bits_each']==1
 for row in manifest['members']:
  p=W/row['archive_member'];assert sha(p)==row['sha256'] and p.stat().st_size==row['bytes']
 based=D/'p41_true_CM4_two_based_points47.json.gz';assert sha(based)==manifest['original_based_points_sha256']
 env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
 def run(label,argv):
  log=W/(label+'.log')
  with log.open('w') as stream:
   child=subprocess.Popen([sys.executable,'-u']+list(map(str,argv)),env=env,stdout=stream,stderr=subprocess.STDOUT)
   while child.poll() is None:
    print('HEARTBEAT R552',label,time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),flush=True)
    try:child.wait(timeout=25)
    except subprocess.TimeoutExpired:pass
   if child.returncode:raise RuntimeError((label,child.returncode,str(log)))
  print('PASS R552',label,flush=True)
 run('independent_initial_geometry_and_prefix',[S/'verify_true_CM4_initial_geometry47.py','--script-dir',S,'--geometry',D/'p41_true_CM4_initial_geometry47.json.gz','--based-points',based,'--prefix-work',root/'work','--transports',root/'transports','--output',W/'p41_true_CM4_initial_geometry_independent_audit47.json'])
 if args.continue_chain:
  active=W/'continued-chains'
  for row in manifest['members']:
   relative=Path(row['archive_member']).relative_to('CM4-initial-prefix');src=root/relative;dst=active/relative;dst.parent.mkdir(parents=True,exist_ok=True)
   if dst.exists() and relative.parts[0]=='work':
    x=json.loads(gzip.decompress(dst.read_bytes()));initial=json.loads(gzip.decompress(src.read_bytes()))
    assert x['input_sha256']==initial['input_sha256']==sha(based) and x['input_point_sha256']==initial['input_point_sha256']
    assert x['target_multiplier']==initial['target_multiplier'] and 1<=x['bits_done']<=304
   elif dst.exists():assert dst.read_bytes()==src.read_bytes()
   else:dst.write_bytes(src.read_bytes())
  run('optional_sequential_actual_two_full_chains',[S/'p41_SS_Abel_with_transports47.py','--script-dir',S,'--SS-atlas',D/'p41_rational_SS_residue_atlas47_complete.json.gz','--common-based-points',D/'p41_all19_based_points47.json.gz','--based-points',based,'--workdir',active/'work','--transport-dir',active/'transports','--disk','SS_j36_06','--disk','SS_j36_02','--max-bits','304','--tiny',D/'p41_all129_tiny_Abel47_complete.json.gz'])
if __name__=='__main__':main()
