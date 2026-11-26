#!/usr/bin/env python3
"""Lift one actual M12 correction into a nested radial/angular space.

Only exact Boehm knot insertion and zero Fourier embedding are used before
binary64 storage. Every storage change is bounded in all six native jets
and in the original physical/material coordinates. This is a warm initial
field, not a solved finer field and not an exact-isometry assertion.
"""
from __future__ import annotations
import argparse,collections,hashlib,importlib.util,json,math,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

BOEHM_SHA='f69035fe51642d30f2a1a5079c3e67f36c8cb05257df89be650cb5b015327db9'
R226_SHA='81003432a6823b3c86859be226c9a099012ed7fa21e46165ac12091d86727e80'
DEFINITION_KEYS=('data_sha256','common_meta_sha256','bridge_sha256','joint_source_sha256',
 'background_source_sha256','background_tolerance','physical_prefix_length_numerical',
 'material_chart_length_numerical','true_cuff_exact')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def fq(x):return Q.from_float(float(x))
def load(name,p):
    s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def bound_value(v):
    if isinstance(v,str):return Q(v)
    if isinstance(v,dict) and 'upper_exact' in v:return Q(v['upper_exact'])
    raise ValueError('An exact rational bound is required; a display float is insufficient')
def show(q):return {'upper_exact':str(q),'display':float(q)}
def check_knots(t,mesh):
    if len(t)<12 or t[:6]!=[Q(0)]*6 or t[-6:]!=[Q(1)]*6 or sorted(t)!=t:
        raise ValueError('Expected the complete clamped quintic material chart')
    counts=collections.Counter(t)
    if any(v>3 for k,v in counts.items() if 0<k<1):raise ValueError('The correction must remain at least C2')
    if sorted(counts)!=list(map(fq,mesh)):raise ValueError('Saved spline and physical grid disagree')
def derivative_controls(t,c,p):
    out=[]
    for i,(a,b) in enumerate(zip(c,c[1:])):
        den=t[i+p+1]-t[i+1]
        if den<=0:raise ArithmeticError('Degenerate active derivative support')
        out.append([p*(y-x)/den for x,y in zip(a,b)])
    return t[1:-1],out,p-1

def transfer(old_free,old_t,old_pm,old_zm,new_t,new_pm,new_zm,boehm):
    old_t=list(old_t);new_t=list(new_t)
    counts_old,counts_new=collections.Counter(old_t),collections.Counter(new_t)
    if any(counts_new[u]<count for u,count in counts_old.items()):raise ValueError('New knot multiset does not contain the old space')
    modes_old=[('planar',int(m)) for m in old_pm]+[('height',int(m)) for m in old_zm]
    modes_new=[('planar',int(m)) for m in new_pm]+[('height',int(m)) for m in new_zm]
    lookup={m:i for i,m in enumerate(modes_new)}
    if len(lookup)!=len(modes_new) or any(m not in lookup for m in modes_old):raise ValueError('Angular spaces are not nested')
    zero=[Q(0)]*len(modes_old);controls=[zero.copy() for _ in range(3)]+old_free+[zero.copy() for _ in range(3)]
    if len(controls)!=len(old_t)-6:raise ValueError('Incomplete old free coefficient matrix')
    inserted=0
    for u,count in sorted(counts_new.items()):
        for unused in range(count-counts_old[u]):
            old_t,controls=boehm.insert_knot(old_t,controls,5,u);inserted+=1
    if old_t!=new_t:raise ArithmeticError('Exact insertion produced the wrong knot multiset')
    exact=[]
    for row in controls:
        out=[Q(0)]*len(modes_new)
        for m,v in zip(modes_old,row):out[lookup[m]]=v
        exact.append(out)
    stored=np.asarray([[float(v) for v in row] for row in exact],dtype=np.float64)
    if any(v for row in exact[:3]+exact[-3:] for v in row):
        raise ArithmeticError('Exact knot insertion did not preserve both complete endpoint two-jets')
    error=[[fq(v)-q for v,q in zip(row,precise)] for row,precise in zip(stored,exact)]
    if any(v for row in error[:3]+error[-3:] for v in row):raise ArithmeticError('The exact zero endpoint controls changed')
    native={};t=new_t;p=5;current=error;modes=[m for family,m in modes_new]
    for radial in range(3):
        for angular in range(3-radial):
            native[radial,angular]=max((sum((abs(v)*abs(m)**angular for v,m in zip(row,modes)),Q(0)) for row in current),default=Q(0))
        if radial<2:t,current,p=derivative_controls(t,current,p)
    return stored[3:-3],native,inserted

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for key in ('scripts','old-field','old-grid','old-result','old-correction-bounds','new-grid','out'):
        ap.add_argument('--'+key,type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();field=Path(str(args.out)+'.field.npz')
    if args.out.exists() or field.exists():raise FileExistsError('Fresh nested-transfer output required')
    old=json.loads(args.old_grid.read_text());new=json.loads(args.new_grid.read_text())
    result=json.loads(args.old_result.read_text());bounds=json.loads(args.old_correction_bounds.read_text())
    for key in DEFINITION_KEYS:
        if old[key]!=new[key]:raise ValueError('Fixed original definition changed: '+key)
    for key,path in [('field_sha256',args.old_field),('grid_sha256',args.old_grid)]:
        if result[key]!=sha(path) or bounds[key]!=sha(path):raise ValueError('Actual old state identity mismatch: '+key)
    for key in ('data_sha256','common_meta_sha256','bridge_sha256'):
        if bounds.get(key)!=old.get(key):raise ValueError('Old R226 source binding changed: '+key)
    if bounds['script_sha256']!=R226_SHA or bounds['reference_only'] or not bounds['continuous_all_knots_and_all_angles']:
        raise ValueError('The actual old R226 field receipt is required')
    if not all(bounds['exact_zero_endpoint_jets']):raise ValueError('Old complete boundary traces were not fixed')
    for key in ('original_exact_metric_unchanged','all_internal_interfaces_free','true_flat_cuff_included','full_half_including_finite_tail_and_deep_collar'):
        if result.get(key) is not True:raise ValueError('Old solve did not cover the required original half: '+key)
    helper_path=args.scripts/'6a65-m12-local-bernstein-angular-metric-budget.py'
    if sha(helper_path)!=BOEHM_SHA:raise ValueError('Exact Boehm implementation identity changed')
    helper=load('nested_M12_exact_Boehm',helper_path)
    with np.load(args.old_field,allow_pickle=False) as a:
        coeff=a['coefficients'].copy();t=list(map(fq,a['unit_knots']))
        pm=a['planar_modes'].copy();zm=a['vertical_modes'].copy()
    if coeff.dtype!=np.float64 or not np.all(np.isfinite(coeff)):raise ValueError('Finite actual binary64 old coefficients required')
    if not np.array_equal(pm,3*np.arange(-old['order'],old['order']+1)+1) or not np.array_equal(zm,3*np.arange(old['order']+1)):
        raise ValueError('The complete original real D3 angular basis is required')
    check_knots(t,old['unit_mesh'])
    if coeff.shape!=(len(t)-12,len(pm)+len(zm)):raise ValueError('Old field is missing coefficients')
    nt=list(map(fq,new.get('unit_knots',[0.]*6+new['unit_mesh'][1:-1]+[1.]*6)))
    check_knots(nt,new['unit_mesh'])
    npm=3*np.arange(-new['order'],new['order']+1)+1;nzm=3*np.arange(new['order']+1)
    lifted,native,inserted=transfer([[fq(v) for v in row] for row in coeff],t,pm,zm,nt,npm,nzm,helper)
    notes=args.scripts.parent/'notes'
    meta_path=notes/'2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json'
    bridge_path=notes/'2026-11-09-db6f-root-exact-bridge-m12.json'
    if sha(meta_path)!=old['common_meta_sha256'] or sha(bridge_path)!=old['bridge_sha256']:
        raise ValueError('The physical-coordinate error budget uses different fixed original metadata')
    meta=json.loads(meta_path.read_text());bridge=json.loads(bridge_path.read_text())
    cfg=meta['frozen_profile'];delta,vu,vd,eps=[fq(cfg[k]) for k in ('delta','vu','vd','ramp')]
    manifest_path=notes/'2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json'
    if sha(manifest_path)!=result['background']['manifest_sha256']:
        raise ValueError('The original tail domain changed')
    manifest=json.loads(manifest_path.read_text());cut=fq(manifest['parameters']['rCut']);cuff=fq(manifest['parameters']['rCuff'])
    if cuff!=Q(old['true_cuff_exact']):raise ValueError('The exact true cuff identity changed')
    T=delta/((1-eps)*vu)+delta/((1-eps)*vd)+Q(bridge['exact_L']['lo'])+cut-cuff
    H=Q(171,250);Hq=Q(60)
    h=cut-cuff
    if h<=Q(11,25) or Q(3)/h*Q(3,2)+Q(711,500)**2*24>=Hq:
        raise ValueError('The inherited R223 physical chart constants do not cover this source')
    ahi=Q(bounds['central_arc_and_partial_primitive_proof']['mean_arc_radius_upper_exact'])
    Jmin=Q(bounds['central_speed_lower_exact']);U1=ahi/Jmin
    U2=bound_value(bounds['central_source_constants']['U2'])
    E=native
    physical={(0,0):E[0,0],(1,0):E[1,0]/(T*H),(0,1):U1*E[0,1],
      (2,0):E[2,0]/(T*T*H*H)+Hq*E[1,0]/(T*H**3),
      (1,1):U1*E[1,1]/(T*H),(0,2):U1*U1*E[0,2]+U2*E[0,1]}
    p=physical[1,0]+physical[0,1]/cuff
    hessian=physical[2,0]+2*physical[1,1]/cuff+physical[0,2]/cuff**2
    np.savez_compressed(field,coefficients=lifted,unit_knots=np.asarray(list(map(float,nt))),planar_modes=npm,vertical_modes=nzm)
    record={'schema':'6a65-M12-exact-nested-space-warm-transfer-v1','script_sha256':sha(__file__),
      'exact_Boehm_source_sha256':BOEHM_SHA,'old_field_sha256':sha(args.old_field),'old_grid_sha256':sha(args.old_grid),
      'old_result_sha256':sha(args.old_result),'old_R226_receipt_sha256':sha(args.old_correction_bounds),
      'new_grid_sha256':sha(args.new_grid),'transferred_field_sha256':sha(field),
      'unchanged_original_definition_keys':list(DEFINITION_KEYS),'same_original_g':True,
      'old_field_shape':list(coeff.shape),'new_field_shape':list(lifted.shape),
      'inserted_knots_counting_multiplicity':inserted,'old_angular_order':old['order'],'new_angular_order':new['order'],
      'exact_space_inclusion_before_binary_storage':True,'D3_and_ambient_reflection_retained':True,
      'complete_central_and_true_cuff_zero_two_jets_retained':True,
      'binary_storage_native_six_jet_error':{str(k):show(v) for k,v in native.items()},
      'binary_storage_physical_s_material_u_six_jet_error':{str(k):show(v) for k,v in physical.items()},
      'binary_storage_target_differential_Frobenius_upper':show(p),
      'binary_storage_target_scaled_coordinate_Hessian_upper':show(hessian),
      'new_nonlinear_solve_executed':False,'exact_isometry_proved':False,
      'raw_retention':'Temporary only; no raw Git/artifact/release.',
      'seconds':time.monotonic()-started}
    args.out.write_text(json.dumps(record,indent=2,allow_nan=False)+'\n');print(json.dumps(record,indent=2))
if __name__=='__main__':main()
