#!/usr/bin/env python3
"""Rebuild the beta8 physical port without storing any DN array in the repo.

The complete coupling source closure is restored, including the required
.cjs smooth-cell factory absent from the earlier 39-file stage1 subset.
First eight columns and the entire cut object come from the original finite
worker startup (512 integration steps). Additional columns use the unchanged
factory with 2048 steps and far=48. All generated data go to --dest.
"""
from pathlib import Path
import argparse,hashlib,json,shutil,subprocess,sys

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--dest',type=Path,required=True)
 p.add_argument('--source-manifest',type=Path);p.add_argument('--stage1-dir',type=Path,required=True);p.add_argument('--linear-script',type=Path,required=True);p.add_argument('--export-script',type=Path,required=True);a=p.parse_args()
 repo=a.repo.resolve();dest=a.dest.resolve();stage=a.stage1_dir.resolve()
 if dest==repo or repo in dest.parents:raise ValueError('Generated data must stay outside the repository')
 manifest=a.source_manifest or stage.parent/'coupling/coupling_recovery_manifest.json';d=json.loads(manifest.read_text());dest.mkdir(parents=True,exist_ok=True)
 for row in d['files']:
  out=dest/row['target'];out.parent.mkdir(parents=True,exist_ok=True)
  if out.exists():data=out.read_bytes()
  else:data=subprocess.check_output(['git','-C',str(repo),'show',row['revision']+':'+row['path']])
  if len(data)!=row['bytes']or hashlib.sha256(data).hexdigest()!=row['sha256']:raise ValueError('Source mismatch: '+row['path'])
  if not out.exists():out.write_bytes(data)
 source=dest/'bundle/topics/visible-flexible-closed-surface';run=dest/'beta8';run.mkdir(exist_ok=True)
 factory=run/'hybrid_outer_factory.mjs';config=run/'hybrid_raised_valley_m8_config.json'
 for name,target,expected in [('hybrid_outer_factory.mjs',factory,'a8fa355e984c2eff4de7e2ff7f654b04da1cbfa53f9591e7137f0c79b56b12ab')]:
  if sha(stage/name)!=expected:raise ValueError('Frozen beta8 input differs: '+name)
  shutil.copyfile(stage/name,target)
 frozen_config=stage/'hybrid_raised_valley_m8_config.json';frozen_config_sha256=sha(frozen_config)
 if frozen_config_sha256 not in ['c4dc0f9820dd6af8eee2ea458e05fa86061a176ba26760bb90cdaf541b1c0df3','47559eb35fa51ab6778a45f242b898c995401212f54f290c06744eadb3a968a5']:
  raise ValueError('Unexpected frozen beta8 configuration')
 cfg=json.loads(frozen_config.read_text());pad_to=int(cfg.pop('valleyControlsPadTo',160));controls=cfg['valleyControls']
 if pad_to!=160 or len(controls)>pad_to:raise ValueError('Unexpected valley control padding')
 cfg['valleyControls']=controls+[0]*(pad_to-len(controls));config.write_text(json.dumps(cfg,indent=2)+'\n')
 if sha(config)!='c4dc0f9820dd6af8eee2ea458e05fa86061a176ba26760bb90cdaf541b1c0df3':raise ValueError('Runtime physical metadata do not match the original expanded configuration')
 if sha(a.linear_script)!='4abd319c532b2aedba62b0b70f2b7dcebf6c480f129a78457094ae9402b4de08':raise ValueError('Unexpected canonical linear generator')
 if sha(a.export_script)!='fe326f293591f91653d2e18c82b69cad1b4ab55f01f66c4c38aeb3d1fe7d88f0':raise ValueError('Unexpected worker port exporter')
 worker=run/'tail_worker.mjs';port8=run/'port8.json';port32=run/'port32_s2048.json'
 commands=[
  [sys.executable,str(stage/'make_hybrid_worker.py'),str(source),str(worker)],
  [sys.executable,str(a.export_script.resolve()),'--source-topic',str(source),'--worker',str(worker),'--config',str(config),'--out',str(port8),'--constructor','hybrid_outer_cell_v1'],
  ['node',str(a.linear_script.resolve()),str(source),str(factory),str(config),str(port32),'2048','32',str(port8)]]
 for cmd in commands:subprocess.run(cmd,check=True)
 a8=json.loads(port8.read_text());a32=json.loads(port32.read_text())
 if a32['linearSlope'][:8]!=a8['linearSlope']or a32['cut']!=a8['cut']:raise ValueError('Literal original columns/cut were not retained')
 result=dict(scope=__doc__,commands=commands,source_manifest_sha256=sha(manifest),frozen_config_sha256=frozen_config_sha256,runtime_config_sha256=sha(config),config_normalization='Remove optional valleyControlsPadTo and append zeros to exactly 160 entries; this restores the original physical metadata without changing the function.',port8_sha256=sha(port8),port32_sha256=sha(port32),historical_port32_sha256='51fca6818d36707fc7f3b0e4aa2073c891fbe67c792295ad04e0917f5889674e',hash_note='Historical output hash identifies the consumed file. New report path/timing/source metadata can change its byte hash; literal columns and cut are checked separately.',retained=a32['retained'],cut_literal_normalization=a32['cut_literal_normalization'])
 (run/'reproduction.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items()if k not in ['commands','scope']}))
if __name__=='__main__':main()
