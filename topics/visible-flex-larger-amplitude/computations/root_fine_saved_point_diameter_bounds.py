#!/usr/bin/env python3
"""Bound diameters of actual saved finite warm point sets.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Every saved Cartesian chunk is hash-checked and consumed. Exact dyadic
distances of exhibited point pairs give lower bounds; a complete scan with
explicit binary64 roundoff inflation gives enclosing-ball upper bounds.
Both the actual prefix set P and the explicitly defined diagnostic set
P union R_z(P) are reported. Neither set is asserted to be a complete closed
surface; sampled curvatures and their products remain numerical diagnostics.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
import math
from pathlib import Path
import resource
import time
import numpy as np


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
def binary(v):return F.from_float(float(v))
def exact(q):
    q=F(q);return dict(numerator=str(q.numerator),denominator=str(q.denominator))
def sqrt_bounds(q,bits=90):
    q=F(q)
    if q<0:raise ValueError('Nonnegative exact squared distance required')
    n=math.isqrt((q.numerator<<(2*bits))//q.denominator)
    lo=F(n,1<<bits)
    hi=lo if lo*lo==q else F(n+1,1<<bits)
    if not lo*lo<=q<=hi*hi:raise ArithmeticError('Exact square-root sandwich failed')
    return lo,hi


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('screen','resource','prepared-core','out'):
        p.add_argument('--'+key,type=Path,required=True)
    a=p.parse_args();start=time.monotonic()
    if a.out.exists():raise FileExistsError('Fresh complete stored-point diameter bounds required')
    screen,owned,prepared=map(read,(a.screen,a.resource,a.prepared_core))
    if not (owned['exitcode']==0 and owned['wait4_observed'] and screen['finished']
            and screen['nonlinear_solution'] is False and screen['worker_start_attempts']==0
            and screen['finite_domain_passed']):
        raise ValueError('The complete original unsolved fine geometry run must have actually finished')
    geom=screen['geometry_fields'];capture=geom['actual_point_cloud'];path=Path(capture['file'])
    manifest=read(path);shape=tuple(manifest['shape'])
    if (sha(path)!=capture['sha256'] or capture['complete_original_mean']!=1552
            or shape!=(3764,768,3) or not manifest['complete']
            or capture['components']!=['x','y','z'] or not capture['actual_prefix_only']):
        raise ValueError('The same complete original fine point cloud is required')
    if np.asarray(screen['actual_core'],dtype=np.float64).tobytes()!=np.asarray(prepared['actual_complete_core'],dtype=np.float64).tobytes():
        raise ValueError('The full warm field did not consume the actually prepared 32-core')
    points=np.empty(shape,dtype=np.float64);coverage=0;chunks=[]
    for item in manifest['chunks']:
        part=path.parent/item['file']
        if sha(part)!=item['sha256'] or item['start']!=coverage or not 0<=item['start']<item['end']<=shape[0]:
            raise ValueError('A point chunk or its contiguous radial coverage differs')
        with gzip.open(part,'rb') as f:values=np.load(f,allow_pickle=False)
        if values.dtype!=np.float64 or values.shape!=(item['end']-item['start'],shape[1],3) or not np.isfinite(values).all():
            raise ValueError('An actual Cartesian block has a wrong or nonfinite shape')
        points[item['start']:item['end']]=values;coverage=item['end']
        chunks.append(dict(file=str(part),sha256=item['sha256'],bytes=part.stat().st_size))
        del values
    if coverage!=shape[0]:raise ValueError('The complete point set is not covered')
    P=points.reshape(-1,3);N=len(P);block=131072
    minimum=np.min(P,axis=0);maximum=np.max(P,axis=0)
    if np.max(abs(P))>=1024:raise ValueError('The explicit no-overflow roundoff bound needs the actual small coordinates')
    u=F(2)**-53;inflation=(1-u)**-5;absolute=F(2)**-1000
    scanned=0

    def farthest(center):
        nonlocal scanned
        center=np.asarray(center,dtype=np.float64);best=-1.;index=-1
        for first in range(0,N,block):
            delta=P[first:first+block]-center
            values=np.sum(delta*delta,axis=1)
            if not np.isfinite(values).all() or float(values.min())<0:
                raise ArithmeticError('Finite positive squared distances required')
            j=int(np.argmax(values));v=float(values[j])
            if v>best:best,index=v,first+j
        scanned+=N
        # Three subtractions, three products, two positive additions. Every
        # component's squared subtraction has two relative factors; the
        # maximum path has five factors (1-u). The absolute remainder is
        # deliberately far larger than all possible subnormal effects.
        return index,binary(best)*inflation+absolute

    origin_index,origin_q=farthest([0.,0.,0.]);origin_lower,origin_radius=sqrt_bounds(origin_q)
    origin_D=2*origin_radius
    n2=np.empty(N,dtype=np.float64)
    for first in range(0,N,block):
        vv=P[first:first+block];n2[first:first+block]=np.sum(vv*vv,axis=1)
    lo,hi=float(minimum[2]),float(maximum[2]);z=P[:,2]
    for unused in range(36):
        c=(lo+hi)/2
        j=int(np.argmax(n2-2*c*z+c*c))
        if c<float(z[j]):lo=c
        else:hi=c
    centers=[[0.,0.,0.],[0.,0.,float((minimum[2]+maximum[2])/2)],[0.,0.,float((lo+hi)/2)]]
    balls=[]
    for center in centers:
        j,bound=farthest(center);unused,radius=sqrt_bounds(bound)
        balls.append(dict(center=center,all_points_scanned=N,squared_radius_upper=exact(bound),
                          diameter_upper=exact(2*radius),diameter_upper_display=float(2*radius),
                          farthest_index=j))
    bbox_q=sum((binary(b)-binary(a0))**2 for a0,b in zip(minimum,maximum))
    unused,bbox=sqrt_bounds(bbox_q)
    prefix_upper=min([F(int(b['diameter_upper']['numerator']),int(b['diameter_upper']['denominator'])) for b in balls]+[bbox])
    seeds={origin_index}
    for axis in range(3):seeds.update((int(np.argmin(P[:,axis])),int(np.argmax(P[:,axis]))))
    best_q=F(0);best_pair=None
    for seed in sorted(seeds):
        j=seed
        for unused in range(3):
            k,unused_bound=farthest(P[j])
            q=sum((binary(a0)-binary(b))**2 for a0,b in zip(P[j],P[k]))
            if q>best_q:best_q,best_pair=q,(j,k)
            if k==j:break
            j=k
    prefix_lower,unused=sqrt_bounds(best_q)
    if prefix_lower>prefix_upper:raise ArithmeticError('The actual prefix diameter lower/upper crossed')
    i=origin_index;radial=i//shape[1];angular=i%shape[1]
    j=radial*shape[1]+(angular+shape[1]//2)%shape[1]
    reflected=P[j].copy();reflected[2]=-reflected[2]
    sym_q=sum((binary(a0)-binary(b))**2 for a0,b in zip(P[i],reflected))
    sym_lower,unused=sqrt_bounds(sym_q)
    if sym_lower>origin_D:raise ArithmeticError('The explicit reflected-set lower/upper crossed')
    defect=float(0.)
    for first in range(0,shape[0],32):
        vv=points[first:first+32];other=np.roll(vv,shape[1]//2,axis=1).copy();other[:,:,2]*=-1
        difference=vv+other
        defect=max(defect,float(np.max(np.sum(difference*difference,axis=2))))
    unused,defect_upper=sqrt_bounds(binary(defect)*inflation+absolute)
    float_S=2*math.sqrt(float(np.max(n2)))
    if abs(float_S-geom['twice_radius_max_sample'])>4e-13:
        raise ValueError('Original 2maxnorm and complete saved point set differ')

    core=list(map(binary,screen['actual_core']));freq=list(range(2,2*len(core)+1,2))
    gap=2*sum((value for index,value in enumerate(core) if index%2==0),F(0))
    rho=1+sum(((1-m*m)*value*((-1)**(m//2)) for m,value in zip(freq,core)),F(0))
    k0=binary(geom['physical_profile']['start_acceleration']);R7=k0*gap*rho
    kappa=float(geom['kappa_abs_max_sample']);tail=7.994254693544539
    out=dict(schema='complete-stored-fine-point-diameter-bounds-v1',scope=__doc__,
        source_sha256=sha(__file__),input_sha256={str(p):sha(p) for p in (a.screen,a.resource,a.prepared_core,path)},
        chunks=chunks,all_complete_points_consumed=True,point_shape=list(shape),prefix_point_count=N,
        complete_mean_angular=1552,original_kappa_abs_max_sample=kappa,
        original_twice_norm_max_sample=geom['twice_radius_max_sample'],
        prefix_set=dict(definition='P: exactly the stored finite prefix Cartesian points interpreted as binary rational coordinates.',
            diameter_lower=exact(prefix_lower),diameter_upper=exact(prefix_upper),
            diameter_display=[float(prefix_lower),float(prefix_upper)],
            exhibited_pair_indices=list(best_pair),exhibited_pair_points=[P[k].tolist() for k in best_pair],
            exhibited_exact_squared_distance=exact(best_q),enclosing_balls=balls,
            exact_axis_box_squared_diagonal=exact(bbox_q),axis_box_diameter_upper=exact(bbox)),
        explicitly_reflected_diagnostic_set=dict(definition='P union R_z(P), where R_z(x,y,z)=(x,y,-z). This is an explicitly defined finite diagnostic set, not a claim about an existing complete surface.',
            diameter_lower=exact(sym_lower),diameter_upper=exact(origin_D),
            diameter_display=[float(sym_lower),float(origin_D)],
            exhibited_prefix_point_index=i,exhibited_reflected_original_index=j,
            exhibited_pair=[P[i].tolist(),reflected.tolist()],exact_pair_squared_distance=exact(sym_q),
            original_half_period_pair_central_symmetry_defect_upper=exact(defect_upper),
            symmetry_defect_display=float(defect_upper)),
        roundoff_contract=dict(binary64_unit_roundoff=exact(u),norm_squared_inflation=exact(inflation),
            absolute_subnormal_allowance=exact(absolute),
            squared_distance_formula='sum(fl(fl(X-c)*fl(X-c))) over three real coordinates; <=5 relative factors per positive contribution; all coordinates and proposed centers small and finite.',
            exact_selected_pair_and_bbox_arithmetic=True,exact_square_root_dyadic_bits=90),
        complete_core_budget=dict(axis_gap=exact(gap),short_axis_radius=exact(rho),initial_acceleration=exact(k0),
            original_R7_witness_product=exact(R7),display=dict(axis_gap=float(gap),short_axis_radius=float(rho),R7=float(R7))),
        finite_numerical_design_products=dict(kappa_times_original_S=kappa*geom['twice_radius_max_sample'],
            current_tail_floor_times_S=max(kappa,tail)*geom['twice_radius_max_sample'],
            kappa_times_prefix_diameter_upper=kappa*float(prefix_upper),
            kappa_times_explicit_reflected_diameter_upper=kappa*float(origin_D)),
        squared_distance_float_scan_points_total=scanned,
        physical_continuum_roundoff_or_geometry_error_paid=False,
        full_closed_surface_D_reach_deltaE_or_deltaHold_certified=False,
        new_ODE_Node_Newton_calls=0,elapsed_seconds=time.monotonic()-start,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(event='complete_actual_finite_point_diameter_bounds_finished',
        prefix=out['prefix_set']['diameter_display'],reflected=out['explicitly_reflected_diagnostic_set']['diameter_display'],
        products=out['finite_numerical_design_products'],core=out['complete_core_budget']['display'],
        out=str(a.out),sha256=sha(a.out))),flush=True)


if __name__=='__main__':main()
