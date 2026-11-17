#!/usr/bin/env python3
"""Assemble existing source modules and new n4 design drivers in scratch."""
import argparse,hashlib,json,shutil
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--dest',type=Path,required=True);a=p.parse_args()
root=Path(__file__).resolve().parent;a.dest.mkdir(parents=True,exist_ok=True)
for name,ref in json.loads((root/'source_dependencies.json').read_text()).items():
 source=root/ref['package']/name
 if hashlib.sha256(source.read_bytes()).hexdigest()!=ref['sha256']:raise RuntimeError('Dependency hash mismatch: '+name)
 shutil.copy2(source,a.dest/name)
for source in root.glob('*.py'):
 if source.name!='prepare_scripts.py':shutil.copy2(source,a.dest/source.name)
for name in ('root03-profile.json','vu035-profile.json'):shutil.copy2(root/name,a.dest/name)
print('Prepared n4 scripts in',a.dest)
