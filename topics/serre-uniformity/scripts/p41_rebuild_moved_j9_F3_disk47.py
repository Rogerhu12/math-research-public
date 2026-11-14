#!/usr/bin/env python3
"""Rebuild a moved j9 F3 height from the published complete 459-function archive.

All six genuine F3 stages execute in a fresh work directory; the long group
chain and its two initial moves are restored unchanged from the F2 result.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tarfile

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for n in ['script-dir','work-dir','canonical','derivative']:ap.add_argument('--'+n,type=Path,required=True)
 ap.add_argument('--based-points',type=Path)
 ap.add_argument('--f2-polynomial',type=Path);ap.add_argument('--f2-audit',type=Path)
 ap.add_argument('--disk-id',default='SS_j9_02');ap.add_argument('--result-id',default='R387')
 args=ap.parse_args();S=args.script_dir.resolve();D=S/'data';W=args.work_dir.resolve();d=args.disk_id
 assert re.fullmatch(r'SS_j9_[0-9]{2}',d);W.mkdir(parents=True,exist_ok=True);R=W/'recovery-inputs'
 def link(src,dst):
  src=src.resolve(strict=True);dst.parent.mkdir(parents=True,exist_ok=True)
  if dst.exists() or dst.is_symlink():assert dst.resolve(strict=True)==src
  else:dst.symlink_to(src,target_is_directory=src.is_dir())
 for n in ['p41_rational_SS_second_kind_integrals47_complete.json.gz','p41_SS_second_kind_rhs47.json.gz']:link(D/n,R/n)
 link(D/'SS_second_kind_rhs47',R/'SS-second-kind-rhs')
 with tarfile.open(D/('p41_'+d+'_principal_transports47.tar.gz'),'r:gz') as tf:
  members=tf.getmembers();assert len(members)==461
  for member in members:
   p=Path(member.name);assert member.isfile() and not p.is_absolute() and '..' not in p.parts
   assert p.parts==('SS-principal-transports','run_manifest47.json') or (len(p.parts)==3 and p.parts[:2]==('SS-principal-transports',d))
   dst=W/p;b=tf.extractfile(member).read();dst.parent.mkdir(parents=True,exist_ok=True)
   if dst.exists():assert dst.read_bytes()==b
   else:dst.write_bytes(b)
 T=W/'SS-principal-transports'/d;manifest=json.loads((T/'transport_manifest47.json').read_text())
 assert manifest['retained_function_count']==459 and manifest['nonformal_principal_function_count']==457
 for row in manifest['functions']:
  p=T/row['filename'];assert sha(p)==row['sha256'] and p.stat().st_size==row['bytes']
 based=(args.based_points or D/'p41_j9_first_four_moved_based_points47.json.gz').resolve(strict=True)
 f2poly=(args.f2_polynomial or D/(d+'_actual_canonical_F2_polynomial47.json.gz')).resolve(strict=True)
 f2audit=(args.f2_audit or D/(d+'-principal-F2-independent-audit.json')).resolve(strict=True)
 argv=['--script-dir',S,'--source-dir',S,'--recovery-dir',R,'--f2-dir',D,'--chain-dir',D,'--transport-directory',T,'--based-points',based,'--canonical',args.canonical.resolve(strict=True),'--derivative',args.derivative.resolve(strict=True),'--work-dir',W/'stages','--output-dir',W/'outputs','--disk-id',d,'--result-id',args.result_id,'--f2-polynomial',f2poly,'--f2-audit',f2audit,'--poly-source',S/'p41_selected_SS_F3_local_polynomial_all_unit_fractions_derivative47.py','--audit-source',S/'verify_moved_SS_F3_all_unit_fractions_derivative47.py']
 subprocess.run([sys.executable,'-u',str(S/'p41_run_moved_j9_F3_derivative47.py')]+list(map(str,argv)),check=True)
if __name__=='__main__':main()
