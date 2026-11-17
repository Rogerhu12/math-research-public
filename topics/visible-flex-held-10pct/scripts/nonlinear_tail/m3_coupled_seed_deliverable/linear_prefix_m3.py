#!/usr/bin/env python3
"""Run the original m3 Cartesian BVP with an optional explicit ShortBridge.

The solver, residuals, core parameters and domain guard are unchanged. The
port remains a finite linear DN; successful output is an OPEN prefix only.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
import argparse,hashlib,importlib.util,json,sys,time,traceback

def module(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def main():
 p=argparse.ArgumentParser(add_help=False);p.add_argument('--source-topic',type=Path,required=True);p.add_argument('--short-bridge',type=Path)
 a,rest=p.parse_known_args();record=dict(scope=__doc__,command=[sys.executable,*sys.argv],wrapper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
 runfile=None
 if '--out-prefix'in rest:
  out=Path(rest[rest.index('--out-prefix')+1]);runfile=out.with_name(out.name+'-run.json');runfile.write_text(json.dumps(record,indent=2)+'\n')
 src=a.source_topic.resolve();ad=module('m3_prefix_adaptive',src/'scripts/950f-prefix-adaptive-chart-bvp-v2.py');patch=module('m3_prefix_flat',src/'scripts/db6f-prefix-flat-profile.py');patch.install(ad)
 if a.short_bridge:
  short=module('m3_prefix_short',a.short_bridge.resolve());original=ad.old.install_source
  def install(root):original(root);short.install()
  ad.old.install_source=install
 sys.argv=[sys.argv[0],'--source-root',str(src/'repro/source-root')]+rest
 t=time.time()
 try:
  ad.main();record['completed']=True
 except Exception as exc:
  traceback.print_exc()
  if '--out-prefix'in rest:
   out=Path(rest[rest.index('--out-prefix')+1]);out.with_name(out.name+'-failure.json').write_text(json.dumps(dict(scope=__doc__,error=repr(exc),seconds=time.time()-t,command=sys.argv),indent=2)+'\n')
  record.update(completed=False,error=repr(exc))
  raise
 finally:
  record['seconds']=time.time()-t
  if runfile:runfile.write_text(json.dumps(record,indent=2)+'\n')
if __name__=='__main__':main()
