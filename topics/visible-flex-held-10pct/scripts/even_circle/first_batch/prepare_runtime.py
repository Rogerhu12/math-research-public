#!/usr/bin/env python3
"""Recover sources, regenerate actual m4 port/charts, and write BVP replay commands.

No BVP is executed by this preparer. Generated arrays remain in the selected
scratch runtime. The frozen source files are copied without editing them.
"""
from pathlib import Path
import argparse,json,hashlib,subprocess,shutil,sys
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--repo',type=Path,required=True);p.add_argument('--dest',type=Path,required=True);a=p.parse_args();here=Path(__file__).resolve().parent;repo=a.repo.resolve();dest=a.dest.resolve()
if dest==repo or repo in dest.parents:raise ValueError('Runtime data must be outside the repository')
dest.mkdir(parents=True,exist_ok=False)
subprocess.run([sys.executable,str(here/'recovery/recover_m3_source.py'),'--repo',str(repo),'--dest',str(dest/'recovery'),'--manifest',str(here/'recovery/m3_source_recovery_manifest.json')],check=True)
source=dest/'recovery/bundle/topics/visible-flexible-closed-surface'
for p in (here/'source').glob('*.py'):shutil.copyfile(p,dest/p.name)
shutil.copyfile(here/'inputs/mode4_physical_config.json',dest/'mode4_physical_config.json')
subprocess.run([sys.executable,str(dest/'export_original_worker_port.py'),'--source-topic',str(source),'--config',str(dest/'mode4_physical_config.json'),'--out',str(dest/'mode4_port8.json')],check=True)
port_sha=hashlib.sha256((dest/'mode4_port8.json').read_bytes()).hexdigest();expected=json.loads((here/'completed_first_batch.json').read_text())['physical_tail']['startup_port_sha256']
if port_sha!=expected:raise RuntimeError('Regenerated actual m4 startup bytes differ from the recorded canonical port: '+port_sha)
subprocess.run([sys.executable,str(here/'regenerate_linear_cases.py'),'--source-topic',str(source),'--runtime',str(dest)],check=True)
shutil.copyfile(here/'inputs/v25-q005-lam1-frozen-profile.json',dest/'v25-q005-lam1-frozen-profile.json')
shutil.copyfile(here/'consumed_head/case1-profile.json',dest/'case1-profile.json')
records=json.loads((here/'completed_first_batch.json').read_text());commands=[]
for r in records['runs']:
 command=r['replay']['command'].copy();command[0]=sys.executable;command=[str(source)if x=='SOURCE_TOPIC'else x for x in command];commands.append(dict(name=r['name'],working_directory=str(dest),argv=command,provenance=r['replay']['kind']))
(dest/'bvp_replay_commands.json').write_text(json.dumps(commands,indent=2)+'\n')
print(json.dumps(dict(runtime=str(dest),source_topic=str(source),canonical_m4_port_sha256=port_sha,linear_cases=7,bvp_runs_executed=0,replay_commands=str(dest/'bvp_replay_commands.json'))))
