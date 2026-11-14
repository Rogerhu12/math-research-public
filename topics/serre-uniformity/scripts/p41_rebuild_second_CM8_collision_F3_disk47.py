#!/usr/bin/env python3
"""Portable selected SS F3 rebuild with explicit collision F2 data and faithfully represented fixed fractions."""
import argparse
from pathlib import Path
import re
import subprocess
import sys
import tarfile


def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--script-dir',type=Path,required=True);ap.add_argument('--work-dir',type=Path,required=True)
 ap.add_argument('--canonical',type=Path,required=True)
 ap.add_argument('--f2-norm',type=Path,required=True)
 ap.add_argument('--f2-polynomial',type=Path,required=True);ap.add_argument('--f2-audit',type=Path,required=True)
 ap.add_argument('--disk-id',default='SS_j10_18');ap.add_argument('--result-id',default='R371');ap.add_argument('--F2-result-id',default='R370')
 args=ap.parse_args();S=args.script_dir.resolve();D=S/'data';W=args.work_dir.resolve();d=args.disk_id
 assert re.fullmatch(r'SS_j[0-9]+_[0-9]+',d);W.mkdir(parents=True,exist_ok=True);R=W/'recovery-inputs'
 def link(src,dst):
  src=src.resolve(strict=True);dst.parent.mkdir(parents=True,exist_ok=True)
  if dst.exists() or dst.is_symlink():assert dst.resolve(strict=True)==src
  else:dst.symlink_to(src,target_is_directory=src.is_dir())
 for n in ['p41_rational_SS_second_kind_integrals47_complete.json.gz','p41_SS_second_kind_rhs47.json.gz']:link(D/n,R/n)
 link(D/'SS_second_kind_rhs47',R/'SS-second-kind-rhs')
 with tarfile.open(D/('p41_'+d+'_principal_transports47.tar.gz'),'r:gz') as tf:
  members=tf.getmembers();assert len(members)==459
  for member in members:
   pp=Path(member.name);assert member.isfile() and not pp.is_absolute() and '..' not in pp.parts
   assert pp.parts[0]=='SS-principal-transports'
   assert pp.parts==('SS-principal-transports','run_manifest47.json') or (len(pp.parts)==3 and pp.parts[1]==d)
   out=W/pp;content=tf.extractfile(member).read();out.parent.mkdir(parents=True,exist_ok=True)
   if out.exists():assert out.read_bytes()==content
   else:out.write_bytes(content)
 argv=['--script-dir',S,'--source-dir',S,'--recovery-dir',R,'--f2-dir',D,'--chain-dir',D,'--transport-directory',W/'SS-principal-transports'/d,'--based-points',D/(args.F2_result_id+'_'+d+'_based_points47.json.gz'),'--canonical',args.canonical.resolve(strict=True),'--f2-norm',args.f2_norm.resolve(strict=True),'--work-dir',W/'stages','--output-dir',W/'outputs','--disk-id',d,'--result-id',args.result_id,'--f2-polynomial',args.f2_polynomial.resolve(strict=True),'--f2-audit',args.f2_audit.resolve(strict=True),'--poly-source',S/'p41_selected_SS_F3_local_polynomial_all_unit_fractions47.py','--audit-source',S/'verify_selected_SS_F3_all_unit_fractions47.py']
 subprocess.run([sys.executable,'-u',str(S/'p41_run_selected_SS_F3_explicit_F2_norm47.py')]+list(map(str,argv)),check=True)

if __name__=='__main__':main()
