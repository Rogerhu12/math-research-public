#!/usr/bin/env python3
"""Replay the actual probe after one explicitly recorded workspace-path change."""
from pathlib import Path
import argparse,hashlib,json
p=argparse.ArgumentParser();p.add_argument('--workspace',type=Path,required=True);a=p.parse_args()
src=Path(__file__).with_name('probe_legacy_core.py');old=src.read_text()
anchor="b=Path('/workspace/scratch/f00f08c94d46');"
if old.count(anchor)!=1:raise ValueError('Expected one workspace anchor')
workspace=a.workspace.resolve();(workspace/'m2_circle_work').mkdir(exist_ok=True,parents=True)
new=old.replace(anchor,'b=Path('+repr(str(workspace))+');')
record=dict(scope='Only workspace path changed; numerical formulas and fixed parameters unchanged.',source_sha256=hashlib.sha256(old.encode()).hexdigest(),executed_text_sha256=hashlib.sha256(new.encode()).hexdigest(),replacements=1)
(workspace/'m2_circle_work/replay_transform.json').write_text(json.dumps(record,indent=2)+'\n')
exec(compile(new,str(src),'exec'),dict(__name__='__main__',__file__=str(src)))
