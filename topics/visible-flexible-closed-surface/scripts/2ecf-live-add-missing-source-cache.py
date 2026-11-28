#!/usr/bin/env python3
"""Add missing public research source files to a running job without replacing any existing definition."""
import argparse,hashlib,json,shutil
from pathlib import Path
def main():
 p=argparse.ArgumentParser()
 p.add_argument('--scripts',required=True,type=Path);p.add_argument('--out',required=True,type=Path)
 a=p.parse_args();src=Path.cwd()/'topics/visible-flexible-closed-surface/scripts'
 added=[]
 for q in sorted(src.rglob('*')):
  if q.is_symlink() or not q.is_file() or q.suffix not in ('.py','.mjs','.cjs','.js','.sh'):continue
  rel=q.relative_to(src);d=a.scripts/rel
  if d.exists():continue
  d.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(q,d)
  added.append(dict(path=str(rel),bytes=d.stat().st_size,sha256=hashlib.sha256(d.read_bytes()).hexdigest()))
 result=dict(schema='add-only-public-source-cache-v1',copiedCount=len(added),copiedBytes=sum(x['bytes'] for x in added),added=added,preservedExistingDefinitions=True,scope='Only missing source files are copied; no actual field, scientific state, existing implementation or stored physical definition is altered.')
 a.out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
if __name__=='__main__':main()
