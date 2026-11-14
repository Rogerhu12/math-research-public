#!/usr/bin/env python3
"""Install the finite-neck metric provider, then run the existing dual BVP.

All command-line options are those of root_dual_core_bvp.py. The input port
must carry finite_neck_terminal_v1 metadata and the profile must select
hermite_boost_neck. A solved output is still a finite linear-tail-DN prefix.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import gzip,hashlib,importlib.util,json,sys
from pathlib import Path
P=Path(__file__).resolve().parent

def module(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m

def main():
 neck=module('alternative_bvp_neck_provider',P/'alternative-neck-provider.py')
 dual=module('alternative_bvp_root_dual',P/'root_dual_core_bvp.py');original=dual.make_dual
 def make_dual(*args,**kwargs):
  neck.install();return original(*args,**kwargs)
 dual.make_dual=make_dual
 try:dual.main()
 finally:
  if '--out-prefix'in sys.argv:
   out=Path(sys.argv[sys.argv.index('--out-prefix')+1])
   names=['alternative-neck-bvp.py','alternative-neck-provider.py','alternative-neck-flatturn.py','alternative-neck-excursion.py','alternative-angle-plateau-connector.py','alternative-direct-tail-connector.py']
   provenance=dict(scope=__doc__,source_sha256={name:hashlib.sha256((P/name).read_bytes()).hexdigest()for name in names})
   for path in [out.with_suffix('.json.gz'),out.with_name(out.name+'-summary.json')]:
    if not path.exists():continue
    raw=gzip.decompress(path.read_bytes())if path.suffix=='.gz'else path.read_bytes();data=json.loads(raw);data['alternative_neck_adapter']=provenance;raw=(json.dumps(data,indent=2)+'\n').encode()
    if path.suffix=='.gz':raw=gzip.compress(raw,mtime=0)
    if len(raw)>=5000000:raise RuntimeError('BVP artifact would exceed the repository file-size limit')
    path.write_bytes(raw)
if __name__=='__main__':main()
