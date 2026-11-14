#!/usr/bin/env python3
"""Actual finite-tail DN along a fixed specified boundary-height vector.

The scalar path is used only to initialize the final requested DN problem.
This does not assert the prefix and tail already have matching derivatives.
"""
import argparse,gzip,hashlib,importlib.util,json,time
from pathlib import Path
import numpy as np
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--config',type=Path,required=True);p.add_argument('--source-root',type=Path,required=True)
p.add_argument('--height-file',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
p.add_argument('--scales',type=float,nargs='+',default=[.236135294,.3,.4,.5,.6,.7,.8,.9,1.])
p.add_argument('--jacobian',action='store_true');p.add_argument('--node-heap',type=int,default=1536)
a=p.parse_args()
if a.out.exists():raise FileExistsError(a.out)
module_file=Path(__file__).with_name('950f-tail-client-v3.py')
spec=importlib.util.spec_from_file_location('weighted_stage_tail_client',module_file);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
body=json.loads(a.height_file.read_text());H=np.array(body['cut']['tail_input_height'] if isinstance(body,dict) and 'cut' in body else body,float)
result=dict(scope=__doc__,config=json.loads(a.config.read_text()),height_file=str(a.height_file),height_sha256=hashlib.sha256(a.height_file.read_bytes()).hexdigest(),target_height=H.tolist(),rows=[])
start=time.time();port=None
def save():
 result['seconds']=time.time()-start;a.out.write_text(json.dumps(result,indent=2)+'\n')
try:
 port=module.WeightedTailPort(a.config,a.source_root,a.out.with_name(a.out.stem+'-state'),node_heap=a.node_heap)
 result['ready']=port.ready;save();print(json.dumps(dict(event='ready',seconds=time.time()-start,modes=port.M)),flush=True)
 if H.shape!=(port.M,):raise ValueError('Input boundary vector and worker mode count differ')
 for scale in a.scales:
  before=time.time();row=dict(scale=scale,fundamental=float(scale*H[0]))
  try:
   r=port.solve(scale*H,jacobian=a.jacobian,audit=True)
   row.update(success=True,residual=r['residual'],audit=r['audit'],jets=r['jets'],last_iterations=r['history'][-3:])
  except Exception as e:row.update(success=False,error=repr(e))
  row['seconds']=time.time()-before;row['record_call']=port.calls;result['rows'].append(row);save();print(json.dumps(row),flush=True)
  if not row['success']:break
except Exception as e:
 result['error']=repr(e);save();print(result['error'],flush=True)
finally:
 if port:port.close()
