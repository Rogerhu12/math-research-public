#!/usr/bin/env python3
"""Same complete M12 H2 LM with an exact-value angular source cache.

Version 4 retains only one angular group of original source packets at a time
and passively records the actual finite per-span Gram peaks for h refinement.
Version 3 additionally caches original binary64 source/target packets in a
private temporary disk directory, returns fresh arrays and deletes that cache
after the actual field is saved. Version 2 compares exact numeric angle values and signed-zero bits, ignoring
long-double storage padding. Only the fixed long-double sin/cos/frequency arrays in TailQueries.apply are
cached. Product association and summation order remain the original ones.
The first actual call at every (material-angle array, derivative order) is
compared with the original evaluator. The original source, query cache,
metric, residual rows and linear algebra are unchanged.

Pass --transfer-receipt for the tested C2 enriched-basis adapter, or omit it
for an actual field on the original simple knot vector.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,io,json,shutil,sys,tempfile,time
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
CORE_SHA='17da2cffaff34ec0d7eeb2470079f8a4b3320bd1a83dc876226925485571f39a'
C2_SHA='3fef5e3cfaa5a26ca9bf76647021db15adda61c74bdc28f3e6a9324aac55e42b'
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

def cache_fixed_packets(cls,root,binding,records):
 original=cls
 class PacketCachedWhole(original):
  def __init__(self,*args,**kwargs):
   super().__init__(*args,**kwargs)
   self._packet_directory=root/('instance-'+str(len(records)))
   self._packet_directory.mkdir();self._packet_known={};self._packet_active_N=None
   self._packet_record={'source_and_chart_binding':binding,'actual_source_identity':self.src.source_identity,
     'cache_is_private_to_this_fixed_WholePosition_instance':True,'misses':0,'hits':0,'disk_bytes':0,'live_disk_bytes':0,'peak_live_disk_bytes':0,'evicted_blocks_when_angle_count_changed':0,
     'all_original_packet_and_target_values_checked_after_disk_write':True,
     'every_return_is_a_fresh_array':True,'every_loaded_file_sha256_checked':True,'entries':[]}
   self._packet_initial_identity=json.dumps(self.src.source_identity,sort_keys=True)
   records.append(self._packet_record)
  def __call__(self,z,N):
   if json.dumps(self.src.source_identity,sort_keys=True)!=self._packet_initial_identity:raise ArithmeticError('The cached fixed source identity changed')
   if self._packet_active_N is not None and self._packet_active_N!=int(N):
    for oldkey in self._packet_known:(self._packet_directory/(oldkey+'.npz')).unlink()
    self._packet_record['evicted_blocks_when_angle_count_changed']+=len(self._packet_known)
    self._packet_known.clear();self._packet_record['live_disk_bytes']=0
   self._packet_active_N=int(N)
   zz=np.asarray(z);header=json.dumps({'N':int(N),'shape':zz.shape,'dtype':zz.dtype.str},sort_keys=True).encode()
   key=hashlib.sha256(header+b'\0'+zz.tobytes()).hexdigest();path=self._packet_directory/(key+'.npz')
   if key not in self._packet_known:
    p,b=super().__call__(z,N)
    if p.dtype!=np.float64 or b.dtype!=np.float64:raise ValueError('The original production source packet must be binary64')
    np.savez(path,packet=p,target=b);digest=sha(path);self._packet_known[key]=digest
    raw=path.read_bytes()
    with np.load(io.BytesIO(raw),allow_pickle=False) as f:rp=f['packet'];rb=f['target']
    if rp.dtype!=p.dtype or rb.dtype!=b.dtype or rp.tobytes()!=p.tobytes() or rb.tobytes()!=b.tobytes():raise ArithmeticError('Disk caching changed original source packet bytes')
    self._packet_record['misses']+=1;self._packet_record['disk_bytes']+=len(raw);self._packet_record['live_disk_bytes']+=len(raw)
    self._packet_record['peak_live_disk_bytes']=max(self._packet_record['peak_live_disk_bytes'],self._packet_record['live_disk_bytes'])
    self._packet_record['entries'].append({'radial_block_and_angles_sha256':key,'packet_file_sha256':digest,'radial_points':len(zz),'angular_nodes':int(N),'bytes':len(raw)})
   else:
    raw=path.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=self._packet_known[key]:raise ArithmeticError('A cached original source packet changed')
    with np.load(io.BytesIO(raw),allow_pickle=False) as f:rp=f['packet'];rb=f['target']
    self._packet_record['hits']+=1
   return rp,rb
 return PacketCachedWhole

def attach_radial_peak_probe(stream,grid,observations):
 """Passively record finite per-span Gram peaks without any source reevaluation."""
 original_observe=stream.observe;original_gram=stream.bvp.gram;active=[None]
 mesh=np.asarray(grid['unit_mesh'],dtype=float)
 def gram(xs,xt,bb):
  residual=original_gram(xs,xt,bb)
  current=active[0]
  if current is not None:
   e,f,g=residual[...,0],residual[...,1]/np.sqrt(2),residual[...,2]
   metric=np.abs(e+g)/2+np.sqrt(((e-g)/2)**2+f*f)
   current['values'].append(np.max(metric,axis=1));current['angles'].append(np.argmax(metric,axis=1))
  return residual
 def observe(basis,nodes,weights,background,coeff,N,block=24):
  if active[0] is not None:raise RuntimeError('Nested physical observers are not supported by this passive diagnostic')
  current={'values':[],'angles':[]};active[0]=current
  try:result=original_observe(basis,nodes,weights,background,coeff,N,block)
  finally:active[0]=None
  values=np.concatenate(current['values']);angles=np.concatenate(current['angles']);nodes=np.asarray(nodes)
  if len(values)!=len(nodes) or float(values.max())!=result['metric_peak']:raise ArithmeticError('The passive radial diagnostic disagrees with the original complete observer')
  ids=np.clip(np.searchsorted(mesh,nodes,side='right')-1,0,len(mesh)-2);rows=[]
  for element in np.unique(ids):
   indices=np.flatnonzero(ids==element);i=int(indices[np.argmax(values[indices])]);z=nodes[i];q=np.longdouble(z)*background.chart.total
   rows.append({'basis_element':int(element),'observed_nodes_in_element':len(indices),'metric_peak':float(values[i]),
    'radial_index':i,'unit_coordinate':float(z),'material_q':float(q),'source_region':'prefix' if q<=background.chart.S else 'tail_or_deep_collar',
    'tail_radius_numerical':str(background.chart.radius(z)[0]) if q>background.chart.S else None,
    'angle_index':int(angles[i]),'basis_theta':float(2*np.pi*angles[i]/N),
    'unit_span':[float(mesh[element]),float(mesh[element+1])]})
  rows.sort(key=lambda row:row['metric_peak'],reverse=True)
  observations.append({'coefficient_bytes_sha256':hashlib.sha256(np.asarray(coeff).tobytes()).hexdigest(),'angular_nodes':int(N),'radial_nodes':len(nodes),
    'radial_point_bytes_sha256':hashlib.sha256(nodes.tobytes()).hexdigest(),'physical_spans_observed':len(rows),
    'finite_per_span_samples_not_continuous_maxima':True,'original_full_observer_unchanged':True,
    'Fourier_axis':'uniform correction-basis theta; original source evaluated at actual u(theta)',
    'metric_peak':result['metric_peak'],'top_physical_spans':rows[:24],
    'top_prefix_physical_spans':[r for r in rows if r['source_region']=='prefix'][:24],
    'top_tail_physical_spans':[r for r in rows if r['source_region']!='prefix'][:24]})
  return result
 stream.bvp.gram=gram;stream.observe=observe

def main():
 ap=argparse.ArgumentParser(description=__doc__,add_help=False)
 ap.add_argument('--h2-core',type=Path,default=HERE/'2ecf-m12-h2-disk-normal-lm.py')
 ap.add_argument('--c2-adapter',type=Path,default=HERE/'2ecf-m12-h2-c2-disk-normal-lm.py')
 a,rest=ap.parse_known_args();p=argparse.ArgumentParser(add_help=False)
 for k in ('out','grid','data','query-report','query-cache'):p.add_argument('--'+k,type=Path,required=True)
 args,unused=p.parse_known_args(rest)
 if sha(a.h2_core)!=CORE_SHA:raise ValueError('Tested H2 core changed')
 receipts=[];packet_records=[];radial_observations=[]
 actual_grid=json.loads(args.grid.read_text())
 packet_root=Path(tempfile.mkdtemp(prefix='fixed-source-packets-',dir=args.out.parent))
 packet_binding={k:sha(getattr(args,k.replace('-','_'))) for k in ('grid','data','query-report','query-cache')}
 packet_binding['original_g_parameter_and_time_range_unchanged']=True
 def patch(lm):
  original_load=lm.load
  def actual_load(name,path):
   m=original_load(name,path)
   if name=='m12_original_warm_core':
    cache_tail_apply(m.TailQueries,receipts)
    m.WholePosition=cache_fixed_packets(m.WholePosition,packet_root,packet_binding,packet_records)
    child_load=m.load
    def observed_load(child_name,child_path):
     child=child_load(child_name,child_path)
     if child_name=='m12_h2_original_joint':attach_radial_peak_probe(child.stream,actual_grid,radial_observations)
     return child
    m.load=observed_load
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
 result['schema']=result['schema'].removesuffix('-v1')+'-packet-cached-v4'
 cache_rows=[row for record in packet_records for row in record['entries']]
 row_stream=hashlib.sha256(('\n'.join(json.dumps(row,sort_keys=True) for row in cache_rows)+'\n').encode()).hexdigest()
 for record in packet_records:record.pop('entries')
 shutil.rmtree(packet_root)
 result['fixed_source_packet_cache']={'schema':'2ecf-M12-original-packet-exact-byte-single-angle-group-disk-cache-v2','instances':packet_records,
   'all_packet_and_target_bytes_preserved':True,'temporary_cache_removed_after_actual_field_saved':True,'actual_block_receipt_stream_sha256':row_stream,'distinct_blocks':len(set(row['radial_block_and_angles_sha256'] for row in cache_rows)),'actual_packet_builds':len(cache_rows),'source_not_refitted_or_changed':True}
 with np.load(str(args.out)+'.field.npz',allow_pickle=False) as saved_field:actual_coeff_sha=hashlib.sha256(saved_field['coefficients'].tobytes()).hexdigest()
 if len(radial_observations)<2 or radial_observations[-1]['coefficient_bytes_sha256']!=actual_coeff_sha:raise ArithmeticError('The final passive radial diagnostic does not identify the actual saved field')
 result['independent_radial_peak_diagnostics']={'before':radial_observations[-2],'after':radial_observations[-1],'all_current_physical_spans_sampled':radial_observations[-1]['physical_spans_observed']==len(actual_grid['unit_mesh'])-1}
 args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
 print(json.dumps({'actual_cached_H2_result':str(args.out),'result_sha256':sha(args.out),'field_sha256':result['field_sha256'],
     'accepted_steps_this_refinement':result['accepted_steps_this_refinement'],'actual_source_cache':result['angular_source_cache'],'fixed_source_packet_cache':result['fixed_source_packet_cache']}),flush=True)
if __name__=='__main__':main()
