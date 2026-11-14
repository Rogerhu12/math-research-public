#!/usr/bin/env python3
"""Restore immutable published F2 inputs for F3, without rerunning any mathematics."""
import argparse,gzip,hashlib,json,re,tarfile
from pathlib import Path

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
 raw=Path(p).read_bytes();return json.loads(gzip.decompress(raw) if str(p).endswith('.gz') else raw)
def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--script-dir',type=Path,required=True)
 ap.add_argument('--work-dir',type=Path,required=True)
 ap.add_argument('--disk-id',required=True);ap.add_argument('--result-id',required=True)
 args=ap.parse_args();D=args.script_dir.resolve()/'data';W=args.work_dir.resolve();d=args.disk_id
 assert re.fullmatch(r'SS_j(?:0|36)_[0-9]+',d) and re.fullmatch(r'R[0-9]+',args.result_id)
 W.mkdir(parents=True,exist_ok=True);restored=[]
 def copy(source,dest):
  content=source.read_bytes();dest.parent.mkdir(parents=True,exist_ok=True)
  if dest.exists():assert dest.read_bytes()==content,dest
  else:dest.write_bytes(content)
  restored.append({'source':str(source),'path':str(dest),'bytes':len(content),'sha256':sha(dest)})
 based=D/(args.result_id+'_'+d+'_based_points47.json.gz');copy(based,W/based.name)
 for suffix in ['_Abel47.json.gz','_multiply47.json.gz']:copy(D/(d+suffix),W/'chain'/(d+suffix))
 for suffix in ['_actual_second_kind_integrals47.json.gz','_principal_expression47.json.gz',
                '_actual_T2_support47.json.gz','_actual_T2_principal_norm47.json.gz',
                '_actual_F2_first_variable_norm47.json.gz','_actual_canonical_F2_height47.json.gz',
                '_actual_canonical_F2_polynomial47.json.gz','-principal-F2-independent-audit.json']:
  copy(D/(d+suffix),W/(d+suffix))
 archive=D/('p41_'+d+'_principal_transports47.tar.gz')
 with tarfile.open(archive,'r:gz') as tar:
  members=tar.getmembers();assert len(members)==459
  for m in members:
   p=Path(m.name)
   assert m.isfile() and not p.is_absolute() and '..' not in p.parts
   assert p.parts==('SS-principal-transports','run_manifest47.json') or (len(p.parts)==3 and p.parts[:2]==('SS-principal-transports',d))
   content=tar.extractfile(m).read();dest=W/p;dest.parent.mkdir(parents=True,exist_ok=True)
   if dest.exists():assert dest.read_bytes()==content
   else:dest.write_bytes(content)
 manifest=read(W/'SS-principal-transports'/d/'transport_manifest47.json')
 assert manifest['disk_id']==d and len(manifest['functions'])==457
 for f in manifest['functions']:
  p=W/'SS-principal-transports'/d/f['filename']
  assert p.stat().st_size==f['bytes'] and sha(p)==f['sha256']
 assert manifest['completed_Abel_sha256']==sha(W/'chain'/(d+'_Abel47.json.gz'))
 assert manifest['multiplication_sha256']==sha(W/'chain'/(d+'_multiply47.json.gz'))
 assert read(W/'chain'/(d+'_multiply47.json.gz'))['input_sha256']==sha(W/based.name)
 def link(src,dest):
  src=src.resolve(strict=True);dest.parent.mkdir(parents=True,exist_ok=True)
  if dest.exists() or dest.is_symlink():assert dest.resolve(strict=True)==src
  else:dest.symlink_to(src,target_is_directory=src.is_dir())
 recovery=W/'recovery-inputs'
 for name in ['p41_rational_SS_second_kind_integrals47_complete.json.gz','p41_SS_second_kind_rhs47.json.gz']:link(D/name,recovery/name)
 link(D/'SS_second_kind_rhs47',recovery/'SS-second-kind-rhs')
 out={'disk_id':d,'source_F2_result':args.result_id,'archive_sha256':sha(archive),
      'archive_members':459,'all457_principal_function_hashes_verified':True,
      'restored_files':restored,'long_chain_or_mathematics_reexecuted':False,
      'source_sha256':sha(__file__)}
 p=W/'published_inputs_restore_manifest47.json';p.write_text(json.dumps(out,indent=2)+'\n')
 print('RESTORED',d,'all457 principal functions; no mathematics rerun',sha(p))
if __name__=='__main__':main()
