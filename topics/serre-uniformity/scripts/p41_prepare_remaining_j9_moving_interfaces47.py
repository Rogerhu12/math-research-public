#!/usr/bin/env python3
"""R470: execute sixteen actual two-flip moves, independent audits and initial SLP interfaces.

Four compressed blocks keep every real matrix certificate below5MB. No304-bit
chain, Norm, local height or disk exclusion is claimed by this preparation.
"""
import argparse,gzip,hashlib,io,json,os,subprocess,sys,tarfile,time
from pathlib import Path
IDS=[f'SS_j9_{i:02d}' for i in [5,6,7,8,9,10,12,13,14,15,16,17,18,20,21,22]]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
 p=Path(p);b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for n in ['script-dir','work-dir','output-dir']:ap.add_argument('--'+n,type=Path,required=True)
 ap.add_argument('--source-dir',type=Path);args=ap.parse_args();S=args.script_dir.resolve();D=S/'data';A=(args.source_dir or S).resolve();W=args.work_dir.resolve();O=args.output_dir.resolve();W.mkdir(parents=True,exist_ok=True);O.mkdir(parents=True,exist_ok=True)
 env=dict(os.environ,OPENBLAS_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1');blocks=[];runs=[]
 def run(label,name,argv,output,canreuse=True):
  src=A/name;command=[sys.executable,'-u',str(src)]+list(map(str,argv));log=W/(label+'.log');reused=output.exists() and canreuse
  if reused:
   x=read(output);assert x['source_sha256']==sha(src)
  else:
   with log.open('w') as stream:
    child=subprocess.Popen(command,env=env,stdout=stream,stderr=subprocess.STDOUT)
    while child.poll() is None:
     print('HEARTBEAT R470',label,time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),flush=True)
     try:child.wait(timeout=25)
     except subprocess.TimeoutExpired:pass
    if child.returncode:raise RuntimeError((label,child.returncode,str(log)))
  assert output.is_file();runs.append({'label':label,'reused':reused,'command':command,'source_sha256':sha(src),'output_sha256':sha(output),'output':str(output),'log':str(log)})
  print('PASS R470',label,sha(output),flush=True)
 def checkpoint():
  x={'result':'R470','complete_all_sixteen_actual_initial_moves':len(blocks)==4,'assigned_disk_ids':IDS,'completed_disk_ids':[d for b in blocks for d in b['disk_ids']],'blocks':blocks,'actual_stages':runs,'source_sha256':sha(__file__)}
  p=O/'p41_j9_remaining16_moving_input_bundle47.json';tmp=p.with_suffix('.new');tmp.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');tmp.replace(p)
 for blockid in range(4):
  ds=IDS[4*blockid:4*blockid+4];tag=f'block{blockid+1:02d}';bp=O/f'p41_j9_remaining16_moved_based_points_{tag}47.json.gz';audit=O/f'p41_j9_remaining16_moving_independent_audit_{tag}47.json'
  argv=['--script-dir',S,'--SS-atlas',D/'p41_rational_SS_residue_atlas47_complete.json.gz','--common-based-points',D/'p41_all19_based_points47.json.gz','--based-points',bp,'--workdir',W/tag/'native-moving']
  for d in ds:argv+=['--disk',d]
  run(tag+'_actual_two_flips','p41_j9_additional_evaluation_moving_points47.py',argv,bp)
  x=read(bp);assert x['result']=='R470' and x['complete_selected_SS_actual_based_points'] and x['selected_disks']==x['completed_disks']==ds and bp.stat().st_size<5_000_000
  for k in ['p41_rational_SS_residue_atlas47_complete.json.gz','p41_all19_based_points47.json.gz']:assert x['input_sha256'][k]==sha(D/k)
  run(tag+'_independent_integer_flips','verify_j9_additional_initial_moving_flips47.py',['--script-dir',S,'--based-points',bp,'--common-based-points',D/'p41_all19_based_points47.json.gz','--SS-atlas',D/'p41_rational_SS_residue_atlas47_complete.json.gz','--output',audit],audit)
  au=read(audit);assert au['all_selected_initial_moving_transports_independently_replayed'] and au['selected_disk_ids']==ds and au['selected_disk_count']==4 and sha(bp) in au['input_sha256'].values()
  T=W/tag/'initial-principal-transports';argv=['--script-dir',S,'--SS-atlas',D/'p41_rational_SS_residue_atlas47_complete.json.gz','--common-based-points',D/'p41_all19_based_points47.json.gz','--based-points',bp,'--workdir',W/tag/'prepare-only','--transport-dir',T,'--prepare-only']
  for d in ds:argv+=['--disk',d]
  run(tag+'_actual_initial_SLP','p41_j9_extended_Abel_with_transports47.py',argv,T/'run_manifest47.json',False)
  initial=[]
  for rec in x['records']:
   d=rec['disk_id'];ff=rec['initial_moving_transport']['first_flip'];found=sorted((T/d).glob('function_*.json.gz'));assert len(found)==2
   byphase={read(p)['phase']:(p,read(p)) for p in found};f=byphase['initial_moving_first'][1];h=byphase['initial_moving_second'][1]
   assert f['numerator_coefficients']==ff['f_V2_coefficients'] and h['numerator_coefficients']==rec['initial_moving_transport']['second_flip_h_V2_coefficients']
   assert f['initial_moving_geometry_based_points_sha256']==h['initial_moving_geometry_based_points_sha256']==sha(bp)
   assert f['output_node']==h['input_nodes'][0] and h['output_node']['point_sha256']==rec['point_sha256']
   assert f['sole_nonunit_source_rows_0based']==[rec['original_source_is_exact_evaluation_row_0based']] and not f['unit_on_all820_source_points'] and h['unit_on_all820_source_points']
   initial += [{'disk_id':d,'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in found]
  blocks.append({'block_id':tag,'disk_ids':ds,'based_points':{'basename':bp.name,'path':str(bp),'sha256':sha(bp),'bytes':bp.stat().st_size},'independent_audit':{'basename':audit.name,'path':str(audit),'sha256':sha(audit),'bytes':audit.stat().st_size},'initial_run_manifest':{'path':str(T/'run_manifest47.json'),'sha256':sha(T/'run_manifest47.json')},'initial_actual_functions':initial});checkpoint()
 assert [d for b in blocks for d in b['disk_ids']]==IDS
 records=[];inputs={}
 for b in blocks:
  bp=Path(b['based_points']['path']);au=Path(b['independent_audit']['path']);inputs[str(bp)]=sha(bp);inputs[str(au)]=sha(au);records+=read(au)['records']
 out={'result':'R470','all_sixteen_initial_moving_transports_independently_replayed':True,'records':records,'input_sha256':inputs,'source_sha256':sha(__file__),'independent_integer_audit_source_sha256':sha(A/'verify_j9_additional_initial_moving_flips47.py'),'scope':'Aggregate of four actually executed independent integer geometry audits, all16 real pairs of flips and32 actual initial V2 SLP records. No304-bit chain, Norm or local QC value claimed.'}
 apath=O/'p41_j9_remaining16_moving_two_flip_independent_audit47.json';apath.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
 archive=O/'p41_j9_remaining16_initial_transport_records47.tar.gz';payloads=[]
 for b in blocks:
  root=W/b['block_id']/'initial-principal-transports';ps=[root/'run_manifest47.json']+[Path(x['path']) for x in b['initial_actual_functions']]
  for p in ps:payloads.append((p,'R470-'+b['block_id']+'/'+str(p.relative_to(root))))
 assert len(payloads)==36
 with archive.open('wb') as raw:
  with gzip.GzipFile(filename='',mode='wb',fileobj=raw,mtime=0) as gz:
   with tarfile.open(fileobj=gz,mode='w|') as tf:
    for p,name in payloads:
     b=p.read_bytes();info=tarfile.TarInfo(name);info.size=len(b);info.mode=0o644;info.uid=info.gid=info.mtime=0;info.uname=info.gname='';tf.addfile(info,io.BytesIO(b))
 with tarfile.open(archive,'r:gz') as tf:
  ms=tf.getmembers();assert len(ms)==36
  for (p,name),m in zip(payloads,ms):assert m.name==name and tf.extractfile(m).read()==p.read_bytes()
 final=read(O/'p41_j9_remaining16_moving_input_bundle47.json');final['complete_actual_initial_SLP_interface']=True;final['aggregate_independent_audit']={'basename':apath.name,'sha256':sha(apath),'bytes':apath.stat().st_size};final['initial_transport_archive']={'basename':archive.name,'sha256':sha(archive),'bytes':archive.stat().st_size,'file_count':36,'actual_V2_function_count':32};(O/'p41_j9_remaining16_moving_input_bundle47.json').write_text(json.dumps(final,ensure_ascii=False,indent=2)+'\n')
 print('COMPLETE R470 all16 real moving interfaces',sha(O/'p41_j9_remaining16_moving_input_bundle47.json'),flush=True)
if __name__=='__main__':main()
