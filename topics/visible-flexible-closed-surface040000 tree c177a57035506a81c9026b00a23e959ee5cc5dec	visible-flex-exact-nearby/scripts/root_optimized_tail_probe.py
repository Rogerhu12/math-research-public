#!/usr/bin/env python3
"""Actual finite nonlinear DN continuation on one fixed cut-preserving metric.
This is a branch/domain diagnostic, not an exact round-tail closure proof.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
os.environ.setdefault('NODE_OPTIONS','--max-old-space-size=384')
import argparse,json,sys,time
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--source-root',required=True,type=Path);p.add_argument('--config',required=True,type=Path);p.add_argument('--out',required=True,type=Path)
p.add_argument('--amplitudes',nargs='+',type=float,default=[1e-8,3e-8,1e-7,3e-7,1e-6,3e-6,1e-5,3e-5,.0001,.00035]);a=p.parse_args()
sys.path.insert(0,str(a.source_root/'topics/large-amplitude-twist-flex/scripts'))
from root_optimized_tail_port import OptimizedTailPort
start=time.time();port=None;result=dict(scope=__doc__,config=json.loads(a.config.read_text()),rows=[])
try:
 port=OptimizedTailPort(a.config,a.source_root,a.out.with_name(a.out.stem+'_tail'))
 result['actual_ready']=port.ready
 for amp in a.amplitudes:
  row=dict(cut_fundamental=-amp);t=time.time()
  try:
   r=port.solve([-amp]+[0]*(port.M-1),jacobian=False,audit=True)
   row.update(success=True,residual=r['residual'],jets=r['jets'],audit=r['audit'])
  except Exception as e:row.update(success=False,error=repr(e))
  row['seconds']=time.time()-t;result['rows'].append(row);result['seconds']=time.time()-start
  a.out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(row),flush=True)
  if not row['success']:break
except Exception as e:
 result['error']=repr(e);a.out.write_text(json.dumps(result,indent=2)+'\n');print(result['error'],flush=True)
finally:
 if port:port.close()
