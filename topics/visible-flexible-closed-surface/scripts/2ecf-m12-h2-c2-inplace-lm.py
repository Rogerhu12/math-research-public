#!/usr/bin/env python3
"""Consume the actual Boehm-transferred C2 M12 field with the H2 direct LM.

This adapter only broadens the declared quintic knot multiset. The unique
physical mesh, every source query, quadrature and original g are unchanged.
It validates the real transfer's field/result identity, including reported
binary64 storage error, and does not call knot insertion exact after storage.
"""
from __future__ import annotations
import argparse,collections,hashlib,importlib.util,json,sys
from pathlib import Path
import numpy as np
from scipy.interpolate import BSpline

HERE=Path(__file__).resolve().parent
CORE_SHA='771daeed3f56303b87d79323c0d04fdb9627a32c72d1dfa43d739adf9cfb27a1'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
def load(name,p):
 spec=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def checked_basis(original_factory,joint,mesh,order,chart,declared):
 mesh=np.asarray(mesh,float);knots=np.asarray(declared,float)
 if not np.all(np.isfinite(knots)) or np.any(np.diff(knots)<0):raise ValueError('Finite nondecreasing full knot vector required')
 count=collections.Counter(knots)
 if count.get(0.,0)!=6 or count.get(1.,0)!=6 or any(n>3 for x,n in count.items() if 0<x<1):raise ValueError('Quintic clamped C2 knots required')
 if not np.array_equal(np.unique(knots),mesh):raise ValueError('The actual physical mesh differs from the full knot vector')
 b=original_factory(joint,mesh,order,chart)
 b.knots=knots;b.full_nb=len(knots)-6;b.nb=b.full_nb-6
 b.spline=BSpline(knots,np.eye(b.full_nb),5,axis=0)
 return b

def main():
 ap=argparse.ArgumentParser(description=__doc__,add_help=False)
 ap.add_argument('--transfer-receipt',type=Path,required=True)
 ap.add_argument('--h2-core',type=Path,default=HERE/'2ecf-m12-h2-inplace-direct-lm.py')
 a,rest=ap.parse_known_args()
 p=argparse.ArgumentParser(add_help=False)
 for name in ('grid','initial-field','initial-result','out','scripts'):p.add_argument('--'+name,type=Path,required=True)
 args,unused=p.parse_known_args(rest)
 if sha(a.h2_core)!=CORE_SHA:raise ValueError('The tested H2 core changed; use a separately identified new adapter')
 grid=read(args.grid);tr=read(a.transfer_receipt)
 if tr.get('schema')!='6a65-M12-exact-nested-space-warm-transfer-v1':raise ValueError('Actual existing exact nested transfer required')
 expected_source=args.scripts/'6a65-m12-exact-radial-angular-warm-transfer.py'
 if tr.get('script_sha256')!=sha(expected_source):raise ValueError('Nested transfer source changed')
 for k,path in [('old_result_sha256',args.initial_result),('new_grid_sha256',args.grid),('transferred_field_sha256',args.initial_field)]:
  if tr.get(k)!=sha(path):raise ValueError('Actual transferred input identity mismatch '+k)
 for k in ('same_original_g','exact_space_inclusion_before_binary_storage','D3_and_ambient_reflection_retained','complete_central_and_true_cuff_zero_two_jets_retained'):
  if tr.get(k) is not True:raise ValueError('Missing actual transfer condition '+k)
 for k in ('binary_storage_native_six_jet_error','binary_storage_physical_s_material_u_six_jet_error'):
  if len(tr.get(k,{}))!=6:raise ValueError('Full six-jet storage error report required')
 if 'unit_knots' not in grid:raise ValueError('This consumer requires the declared C2 enriched knot multiset')
 bind=Path(str(args.out)+'.initial-binding.json')
 if bind.exists() or args.out.exists():raise FileExistsError('Fresh actual C2-LM outputs required')
 binding={'schema':'2ecf-M12-actual-nested-transfer-input-binding-not-observation-v1','script_sha256':sha(__file__),
   'grid_sha256':sha(args.grid),'field_sha256':sha(args.initial_field),'actual_transfer_receipt_sha256':sha(a.transfer_receipt),
   'actual_old_result_sha256':sha(args.initial_result),'exact_inclusion_only_before_binary_storage':True,
   'binary_storage_target_differential_Frobenius_upper':tr['binary_storage_target_differential_Frobenius_upper'],
   'binary_storage_target_scaled_coordinate_Hessian_upper':tr['binary_storage_target_scaled_coordinate_Hessian_upper'],
   'new_nonlinear_solve_in_this_binding':False,'source':read(args.initial_result)['source'],'background':read(args.initial_result)['background']}
 bind.write_text(json.dumps(binding,indent=2,allow_nan=False)+'\n')
 core=load('frozen_M12_H2_core',a.h2_core);original_load=core.load
 def actual_load(name,path):
  m=original_load(name,path)
  if name=='m12_original_warm_core':
   factory=m.basis_for
   m.basis_for=lambda joint,mesh,order,chart:checked_basis(factory,joint,mesh,order,chart,grid['unit_knots'])
  return m
 core.load=actual_load
 rest=list(rest);i=rest.index('--initial-result');rest[i+1]=str(bind)
 sys.argv=[str(a.h2_core),*rest];core.main()
 result=read(args.out)
 result.update(schema='2ecf-original-M12-entire-half-C2-inplace-H2-increment-direct-LM-v1',
   frozen_H2_core_sha256=result['script_sha256'],script_sha256=sha(__file__),
   actual_transfer_receipt_sha256=sha(a.transfer_receipt),actual_original_parent_result_sha256=sha(args.initial_result),
   full_declared_knots_consumed=True,finite_space_at_least_C2=True,
   exact_source_radial_knot_coincidence_claimed=False,
   actual_new_radial_columns=len(grid['unit_knots'])-12,
   physical_mesh_source_queries_and_g_preserved=True)
 args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
 print(json.dumps({'actual_C2_H2_result':str(args.out),'result_sha256':sha(args.out),'field_sha256':result['field_sha256'],
    'accepted_steps_this_refinement':result['accepted_steps_this_refinement'],'independent_after':result['independent_observer_after']}),flush=True)
if __name__=='__main__':main()
