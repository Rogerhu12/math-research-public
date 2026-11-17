#!/usr/bin/env python3
"""Select the original m=3 nonlinear coupler and install its explicit ShortBridge.

Original TailMixin, true nonlinear DN, residuals, boundary Jacobian, means,
acceptance and seam audit are unchanged. This wrapper only installs the
already-used flat law and ShortBridge after the source runtime is loaded.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,hashlib,importlib.util,json,sys,time
from pathlib import Path
p=argparse.ArgumentParser(add_help=False);p.add_argument('--source-topic',type=Path,required=True);p.add_argument('--short-bridge',type=Path,required=True)
a,rest=p.parse_known_args();source=a.source_topic.resolve()
def module(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
coupler_path=source/'scripts/db6f-prefix-coupled.py';flat_path=source/'scripts/db6f-prefix-flat-profile.py'
c=module('original_m3_smallcut_coupler',coupler_path);flat=module('original_m3_flat_profile',flat_path);flat.install(c.adaptive)
short=module('original_m3_short_bridge',a.short_bridge.resolve());original_install=c.adaptive.old.install_source
def install(root):original_install(root);short.install()
c.adaptive.old.install_source=install
sys.argv=[sys.argv[0],'--source-root',str(source/'repro/source-root')]+rest
out=Path(rest[rest.index('--out-prefix')+1]);out.parent.mkdir(parents=True,exist_ok=True)
sha=lambda f:hashlib.sha256(Path(f).read_bytes()).hexdigest()
record=dict(scope=__doc__,command=sys.argv,source_hashes={str(x):sha(x)for x in [Path(__file__),coupler_path,flat_path,a.short_bridge]},source_topic=str(source))
file=out.with_name(out.name+'-wrapper-record.json');file.write_text(json.dumps(record,indent=2)+'\n');started=time.monotonic()
try:c.main();record['returned']=True
finally:record['seconds']=time.monotonic()-started;file.write_text(json.dumps(record,indent=2)+'\n')
