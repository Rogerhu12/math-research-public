#!/usr/bin/env python3
"""Prepare a source-complete scratch replay for the first complementary prefix batch."""
from pathlib import Path
import argparse,json,hashlib,shutil,subprocess,sys
p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--dest',type=Path,required=True);a=p.parse_args();here=Path(__file__).resolve().parent;dest=a.dest.resolve()
subprocess.run([sys.executable,str(here.parent/'narrow_old_basis/prepare_narrow_runtime.py'),'--repo',str(a.repo.resolve()),'--dest',str(dest)],check=True)
source=dest/'recovery/bundle/topics/visible-flexible-closed-surface';snap=dest/'complementary_snapshot';snap.mkdir()
for name in ['uniform_complement_core.py','complementary_moment_basis.py','moment_interval_bounds.py']:shutil.copyfile(here.parent/'complementary_controls'/name,snap/name)
for name in ['complement_plateau_prefix.py','complement_plateau_prefix_cached.py','mode4_physical_config24.json']:shutil.copyfile(here/name,dest/name)
subprocess.run([sys.executable,str(dest/'export_original_worker_port.py'),'--source-topic',str(source),'--config',str(dest/'mode4_physical_config24.json'),'--out',str(dest/'mode4_port24.json')],check=True)
r=json.loads((here/'completed_runs.json').read_text());assert hashlib.sha256((dest/'mode4_port24.json').read_bytes()).hexdigest()==r['port24']['sha256']
commands=[]
for row in r['runs']:
    argv=[sys.executable,row['captured_driver']]
    for key,value in row['replay_arguments'].items():
        if value is None or value is False:continue
        argv.append('--'+key.replace('_','-'))
        if value is True:continue
        if key=='source_topic':argv.append(str(source))
        elif isinstance(value,list):argv.extend(map(str,value))
        else:argv.append(str(value))
    commands.append(dict(name=row['name'],working_directory=str(dest),argv=argv))
(dest/'complement_replay_commands.json').write_text(json.dumps(commands,indent=2)+'\n')
print(json.dumps(dict(bvp_runs_executed=0,replay_runs=len(commands),port24_sha256=r['port24']['sha256'])))
