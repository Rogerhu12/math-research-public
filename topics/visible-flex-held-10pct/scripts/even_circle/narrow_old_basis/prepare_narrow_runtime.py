#!/usr/bin/env python3
"""Extend the first-batch runtime with the completed narrow-window replay."""
from pathlib import Path
import argparse,json,hashlib,subprocess,sys,shutil
p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--dest',type=Path,required=True);a=p.parse_args();here=Path(__file__).resolve().parent;dest=a.dest.resolve()
subprocess.run([sys.executable,str(here.parent/'first_batch/prepare_runtime.py'),'--repo',str(a.repo.resolve()),'--dest',str(dest)],check=True)
source=dest/'recovery/bundle/topics/visible-flexible-closed-surface'
for name in ['even_plateau_prefix_analytic.py','analytic_adaptive_core_jac.py']:shutil.copyfile(here/name,dest/name)
s=(here/'screen_compact_window.py').read_text();anchor="src=root/'m3_flat17_work/recovered/bundle/topics/visible-flexible-closed-surface'";assert s.count(anchor)==1
s=s.replace(anchor,"src=r/'recovery/bundle/topics/visible-flexible-closed-surface'",1)
(dest/'screen_compact_window.py').write_text(s)
subprocess.run([sys.executable,str(dest/'screen_compact_window.py')],check=True,cwd=dest)
expected=json.loads((here/'linear_screen_scalars.json').read_text())['rows'];actual=json.loads((dest/'compact_window_screen.json').read_text())['rows']
for e,v in zip(expected,actual):
    v['directory']=Path(v['directory']).name
    assert e==v, (e,v)
commands=[]
for r in json.loads((here/'completed_runs.json').read_text())['runs']:
    argv=[sys.executable,r['captured_driver']]
    for key,value in r['replay_arguments'].items():
        if value is None or value is False:continue
        argv.append('--'+key.replace('_','-'))
        if value is True:continue
        if key=='source_topic':argv.append(str(source))
        elif isinstance(value,list):argv.extend(map(str,value))
        else:argv.append(str(value))
    commands.append(dict(name=r['name'],working_directory=str(dest),argv=argv,scope='Reconstructed replay arguments; original shell argv not claimed.'))
(dest/'narrow_replay_commands.json').write_text(json.dumps(commands,indent=2)+'\n')
print(json.dumps(dict(linear_rows_identical=len(actual),bvp_runs_executed=0,screen_transformed_sha256=hashlib.sha256(s.encode()).hexdigest(),replay_commands=str(dest/'narrow_replay_commands.json'))))
