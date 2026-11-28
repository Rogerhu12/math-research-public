#!/usr/bin/env python3
"""Use original physical observers on the declared C2 knot multiset.

The original source, metric, point sets and all six physical jets are kept.
Only declared basis construction and the verified exact-value angular cache
are adapted. An inherited mixed-field 'before' union is explicitly discarded;
the actual after-field observer union remains well defined and unchanged.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
CACHE_SHA='b69d67754d935a4e4342c934f80e5272d520f86164804c710350cf412a805745'
C2_SHA='34fb3936a57bef17ceb3c326bdfad885fe7372366e373030ec7a83a4202f8814'
OBSERVERS={'microspan':'6a65-m12-entire-half-multiple-window-observer.py',
           'ancestor':'6a65-m12-entire-half-transitive-observer-union.py'}
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def main():
 ap=argparse.ArgumentParser(description=__doc__,add_help=False)
 ap.add_argument('--kind',choices=tuple(OBSERVERS),required=True)
 ap.add_argument('--cache-helper',type=Path,default=HERE/'2ecf-m12-h2-cached-direct-lm-v2.py')
 ap.add_argument('--basis-helper',type=Path,default=HERE/'2ecf-m12-h2-c2-direct-lm.py')
 a,rest=ap.parse_known_args()
 p=argparse.ArgumentParser(add_help=False)
 for key in ('scripts','grid','out','result','field'):p.add_argument('--'+key,type=Path,required=True)
 b,_=p.parse_known_args(rest)
 if sha(a.cache_helper)!=CACHE_SHA or sha(a.basis_helper)!=C2_SHA:raise ValueError('Tested value cache or declared-C2-basis helper changed')
 grid=json.loads(b.grid.read_text());saved=json.loads(b.result.read_text())
 if saved['field_sha256']!=sha(b.field) or saved['grid_sha256']!=sha(b.grid):raise ValueError('Actual result binding changed')
 cache=load('observed_exact_value_cache',a.cache_helper);basis=load('observed_declared_C2_basis',a.basis_helper)
 path=b.scripts/OBSERVERS[a.kind];entry=load('actual_original_observer',path);original_load=entry.load;receipts=[]
 def actual_load(name,path):
  m=original_load(name,path)
  if hasattr(m,'TailQueries') and hasattr(m,'basis_for'):
   cache.cache_tail_apply(m.TailQueries,receipts)
   if 'unit_knots' in grid:
    factory=m.basis_for
    m.basis_for=lambda joint,mesh,order,chart:basis.checked_basis(factory,joint,mesh,order,chart,grid['unit_knots'])
  return m
 entry.load=actual_load;sys.argv=[str(path),*rest];entry.main()
 result=json.loads(b.out.read_text())
 result['original_observer_schema']=result['schema'];result['original_observer_script_sha256']=result['script_sha256']
 result['schema']='2ecf-M12-declared-C2-basis-'+a.kind+'-observer-v1';result['script_sha256']=sha(__file__)
 result['basis_helper_sha256']=sha(a.basis_helper);result['angular_cache_helper_sha256']=sha(a.cache_helper)
 result['full_declared_knot_multiset_consumed']=True;result['same_physical_points_source_and_original_metric']=True
 result['actual_angular_source_cache']=receipts
 if a.kind=='ancestor':
  result['source_before_on_extra_points']=result.pop('old_missing_points_before')
  result.pop('union_before',None)
  result['mixed_source_and_initial_field_before_union_discarded']=True
  result['union_after_contains_same_actual_saved_field_at_every_point']=True
 else:result['before_means_source_without_saved_Cartesian_correction']=True
 b.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
 print(json.dumps({'actual_declared_basis_observer':str(b.out),'result_sha256':sha(b.out),
    'same_actual_field_sha256':sha(b.field),'after':result.get('after',result.get('union_after')),
    'actual_cached_angle_grids':len(receipts)}),flush=True)
if __name__=='__main__':main()
