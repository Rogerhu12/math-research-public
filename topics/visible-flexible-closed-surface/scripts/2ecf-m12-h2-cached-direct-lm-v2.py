#!/usr/bin/env python3
"""Same complete M12 H2 LM with an exact-value angular source cache.

Version 2 compares exact numeric angle values and signed-zero bits, ignoring
long-double storage padding. Only the fixed long-double sin/cos/frequency arrays in TailQueries.apply are
cached. Product association and summation order remain the original ones.
The first actual call at every (material-angle array, derivative order) is
compared with the original evaluator. The original source, query cache,
metric, residual rows and linear algebra are unchanged.

Pass --transfer-receipt for the tested C2 enriched-basis adapter, or omit it
for an actual field on the original simple knot vector.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,sys,time
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
CORE_SHA='a7e5229793ceb4753b74f8063a8abc3b7d99280a16e69cab9a7e0c844b794117'
C2_SHA='34fb3936a57bef17ceb3c326bdfad885fe7372366e373030ec7a83a4202f8814'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(name,p):
 spec=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def cache_tail_apply(cls,receipts):
 original=cls.apply
 def apply(self,a,u,order):
  if order not in (0,1,2):raise ValueError('Only the original position two-jets are cached')
  if not hasattr(self,'_exact_value_trig_cache'):
   self._exact_value_trig_cache={};self._exact_value_trig_inputs=[]
  u=np.asarray(u,np.longdouble)
  if not np.all(np.isfinite(u)):raise ValueError('Finite material angles required')
  key=next((i for i,v in enumerate(self._exact_value_trig_inputs) if u.shape==v.shape and np.array_equal(u,v) and np.array_equal(np.signbit(u),np.signbit(v))),len(self._exact_value_trig_inputs))
  if key not in self._exact_value_trig_cache:
   self._exact_value_trig_inputs.append(u.copy())
   began=time.monotonic();m=np.asarray(self.pm,np.longdouble);h=np.asarray(self.hm,np.longdouble)
   angle=m[:,None]*u[None,:];E=np.cos(angle)+1j*np.sin(angle)
   angle_z=h[:,None]*u[None,:];Z=np.cos(angle_z)+1j*np.sin(angle_z)
   factors={d:(1j*m.astype(np.clongdouble))**d for d in (0,1,2)}
   height={d:np.real((1j*h.astype(np.clongdouble))[:,None]**d*Z) for d in (0,1,2)}
   rec={'angular_count':len(u),'planar_modes':len(m),'height_modes':len(h),'calls':0,'verified_orders':[],
        'maximum_float_value_difference':0.,'float64_output_bytes_equal_on_first_calls':True,
        'cache_build_seconds':time.monotonic()-began,'sum_order_unchanged':True,'source_coefficients_uncached_and_unchanged':True}
   self._exact_value_trig_cache[key]=(E,factors,height,rec);receipts.append(rec)
  E,factors,height,rec=self._exact_value_trig_cache[key];P=len(self.pm)
  c=np.sum(a[:P,None]*factors[order][:,None]*E,axis=0)
  vertical=np.sum(a[P:,None]*height[order],axis=0)
  result=np.stack((c.real,c.imag,-vertical),axis=-1)
  if order not in rec['verified_orders']:
   expected=original(self,a,u,order)
   if result.dtype!=expected.dtype or result.shape!=expected.shape or not np.array_equal(result,expected):
    raise ArithmeticError('Angular source caching changed an actual returned source value')
   if np.asarray(result,dtype=np.float64).tobytes()!=np.asarray(expected,dtype=np.float64).tobytes():
    raise ArithmeticError('Angular source caching changed a source value after production binary64 conversion')
   rec['verified_orders'].append(order)
  rec['calls']+=1
  return result
 cls.apply=apply

def main():
 ap=argparse.ArgumentParser(description=__doc__,add_help=False)
 ap.add_argument('--h2-core',type=Path,default=HERE/'2ecf-m12-h2-direct-lm.py')
 ap.add_argument('--c2-adapter',type=Path,default=HERE/'2ecf-m12-h2-c2-direct-lm.py')
 a,rest=ap.parse_known_args();p=argparse.ArgumentParser(add_help=False);p.add_argument('--out',type=Path,required=True);args,unused=p.parse_known_args(rest)
 if sha(a.h2_core)!=CORE_SHA:raise ValueError('Tested H2 core changed')
 receipts=[]
 def patch(lm):
  original_load=lm.load
  def actual_load(name,path):
   m=original_load(name,path)
   if name=='m12_original_warm_core':cache_tail_apply(m.TailQueries,receipts)
   return m
  lm.load=actual_load;return lm
 if '--transfer-receipt' in rest:
  if sha(a.c2_adapter)!=C2_SHA:raise ValueError('Tested C2 consumer changed')
  entry=load('frozen_C2_H2_entry',a.c2_adapter);original=entry.load
  def actual_load(name,path):
   m=original(name,path)
   return patch(m) if name=='frozen_M12_H2_core' else m
  entry.load=actual_load;sys.argv=[str(a.c2_adapter),'--h2-core',str(a.h2_core),*rest];entry.main()
 else:
  entry=patch(load('frozen_H2_entry',a.h2_core));sys.argv=[str(a.h2_core),*rest];entry.main()
 result=json.loads(args.out.read_text());result['uncached_entry_script_sha256']=result['script_sha256']
 result['script_sha256']=sha(__file__);result['angular_source_cache']={'schema':'2ecf-original-M12-longdouble-trig-exact-value-cache-v2',
    'exact_numeric_key_includes_signed_zero_excludes_padding':True,'only_fixed_trigonometric_arrays_cached':True,'original_multiplication_and_sum_order_preserved':True,
    'first_actual_call_at_every_grid_and_derivative_compared_with_original':True,
    'original_source_queries_and_metric_unchanged':True,'arrays':receipts}
 result['schema']=result['schema'].removesuffix('-v1')+'-cached-v2'
 args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
 print(json.dumps({'actual_cached_H2_result':str(args.out),'result_sha256':sha(args.out),'field_sha256':result['field_sha256'],
     'accepted_steps_this_refinement':result['accepted_steps_this_refinement'],'actual_source_cache':result['angular_source_cache']}),flush=True)
if __name__=='__main__':main()
