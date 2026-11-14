#!/usr/bin/env python3
"""Read every saved prefix point and bracket its quarter-phase finite Hausdorff distance.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
KD-tree neighbours select actual finite-set pairs. Their complete streamed
distance maxima give an upper bound irrespective of nearest-neighbour search
accuracy. Complete direct scans at the selected witnesses give a lower bound.
Only binary finite point sets are certified; no continuum, tail, cap, accepted
solution, all-phase maximum, deltaHold or Euclidean noncongruence is asserted.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import io
import json
import math
from pathlib import Path
import resource
import time
import numpy as np
import scipy
from scipy.spatial import cKDTree


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
def binary(x):return F.from_float(float(x))
def rat(x):
    x=F(x);return dict(numerator=str(x.numerator),denominator=str(x.denominator))
def unrat(x):return F(int(x['numerator']),int(x['denominator']))
def sqrt_interval(x,bits=100):
    x=F(x)
    if x<0:raise ValueError('Nonnegative squared distance required')
    n=math.isqrt((x.numerator<<(2*bits))//x.denominator)
    lo=F(n,1<<bits);hi=lo if lo*lo==x else F(n+1,1<<bits)
    if not lo*lo<=x<=hi*hi:raise ArithmeticError('Exact square-root sandwich failed')
    return lo,hi
def rotate(v,sign):
    z=np.empty_like(v);z[...,0]=-sign*v[...,1];z[...,1]=sign*v[...,0];z[...,2]=v[...,2]
    return z


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('screen','geometry-resource','prepared-core','point-root','diameter','r1','r7','out'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--radial-batch',type=int,default=32)
    p.add_argument('--rss-limit-mib',type=float,default=768.)
    a=p.parse_args();started=time.monotonic()
    if a.out.exists():raise FileExistsError('A fresh complete finite-set phase diagnostic is required')
    if not 1<=a.radial_batch<=128 or not 128<=a.rss_limit_mib<=768:
        raise ValueError('Use explicit bounded query batches and at most 768 MiB')
    def guard():
        value=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if value>a.rss_limit_mib*1024:raise MemoryError('Actual RSS exceeded the declared finite-point guard')
        return value
    screen,owned,prepared,diameter=map(read,(a.screen,a.geometry_resource,a.prepared_core,a.diameter))
    if not (owned['exitcode']==0 and owned['wait4_observed'] and screen['finished'] and
            screen['finite_domain_passed'] and not screen['nonlinear_solution'] and screen['worker_start_attempts']==0):
        raise ValueError('This input must be the actually completed, explicitly unsolved warm field')
    if np.asarray(screen['actual_core'],dtype=np.float64).tobytes()!=np.asarray(prepared['actual_complete_core'],dtype=np.float64).tobytes():
        raise ValueError('Actual warm complete core differs')
    geometry=screen['geometry_fields'];capture=geometry['actual_point_cloud']
    points_path=a.point_root/capture['file'];grid_path=a.point_root/geometry['grid_file']
    if sha(points_path)!=capture['sha256'] or sha(grid_path)!=geometry['grid_sha256']:
        raise ValueError('Actual complete Cartesian or coordinate identity changed')
    manifest,grid=read(points_path),read(grid_path);shape=tuple(manifest['shape']);t=np.asarray(grid['numerical_t'])
    if (manifest['schema']!='complete-geometry-chunks-v1' or not manifest['complete'] or
            manifest['dtype']!='float64' or shape!=(len(t),grid['angular'],3) or shape[1]%4 or
            not capture['actual_prefix_only'] or capture['complete_original_mean']!=1552):
        raise ValueError('The full fine Cartesian point-array contract changed')
    for path in (a.screen,a.geometry_resource,a.prepared_core,points_path):
        if diameter['input_sha256'].get(str(path))!=sha(path):
            raise ValueError('The finite diameter bounds belong to another exact point set: '+str(path))
    if not diameter['all_complete_points_consumed'] or diameter['point_shape']!=list(shape):
        raise ValueError('The existing diameter certificate is incomplete')
    count=shape[0]*shape[1]
    points=np.empty((count,3),dtype=np.float64);chunks=[];cursor=0
    for item in manifest['chunks']:
        path=points_path.parent/item['file'];data=path.read_bytes()
        if (hashlib.sha256(data).hexdigest()!=item['sha256'] or len(data)!=item['bytes'] or
                item['start']!=cursor or not cursor<item['end']<=shape[0]):
            raise ValueError('A full saved Cartesian chunk changed or coverage has a gap')
        value=np.load(io.BytesIO(gzip.decompress(data)),allow_pickle=False)
        if value.dtype!=np.float64 or value.shape!=(item['end']-cursor,shape[1],3) or not np.isfinite(value).all() or np.max(abs(value))>=1024:
            raise ValueError('Finite original Cartesian coordinates are required')
        points[cursor*shape[1]:item['end']*shape[1]]=value.reshape(-1,3)
        chunks.append(dict(file=str(path),sha256=item['sha256'],start=cursor,end=item['end'],bytes=len(data)))
        cursor=item['end'];del value,data;guard()
    if cursor!=shape[0]:raise ValueError('The saved point set is incomplete')
    points.flags.writeable=False
    tree=cKDTree(points,leafsize=32,compact_nodes=True,balanced_tree=True,copy_data=False)
    print(json.dumps(dict(event='full_phase_tree_ready',points=count,tree_nodes=tree.size,rss_kib=guard())),flush=True)
    states={(setname,sign):dict(max_selected_pair_squared=-1.,candidate=None,complete_base_sources_scanned=0)
            for setname in ('prefix','reflected_union') for sign in (1,-1)}
    blocks=[];batch=a.radial_batch*shape[1]
    for first in range(0,count,batch):
        last=min(first+batch,count);source=points[first:last];block={}
        for sign in (1,-1):
            # d(P,R^sign P)=d(R^-sign P,P), with an exact coordinate permutation.
            query=rotate(source,-sign)
            unused,indices=tree.query(query,k=1,eps=0.,p=2,workers=1)
            target=rotate(points[indices],sign)
            delta=source-target;q0=np.sum(delta*delta,axis=1)
            if not np.isfinite(q0).all() or np.any(q0<0):raise ArithmeticError('Nonnegative finite selected-pair distances required')
            union_q=q0.copy();union_indices=indices.copy();reflected=np.zeros(len(source),dtype=bool)
            query[:,2]*=-1
            unused,idx_ref=tree.query(query,k=1,eps=0.,p=2,workers=1)
            target_ref=rotate(points[idx_ref],sign);target_ref[:,2]*=-1
            delta=source-target_ref;q_ref=np.sum(delta*delta,axis=1)
            choose=q_ref<union_q
            union_q[choose]=q_ref[choose];union_indices[choose]=idx_ref[choose];reflected[choose]=True
            for name,qs,idx,refl in (('prefix',q0,indices,np.zeros(len(source),dtype=bool)),
                                     ('reflected_union',union_q,union_indices,reflected)):
                k=int(np.argmax(qs));value=float(qs[k]);state=states[(name,sign)]
                state['complete_base_sources_scanned']+=len(source)
                if value>state['max_selected_pair_squared']:
                    state['max_selected_pair_squared']=value
                    state['candidate']=dict(source_index=first+k,selected_target_index=int(idx[k]),target_reflected_in_z=bool(refl[k]))
                block[name+('_plus' if sign==1 else '_minus')]=math.sqrt(value)
            del query,indices,target,delta,q0,union_q,union_indices,reflected,idx_ref,target_ref,q_ref,choose
        blocks.append(dict(first=first,last=last,maximum_selected_pair_distance=block))
        if len(blocks)%8==0 or last==count:
            print(json.dumps(dict(event='full_phase_all_point_query_progress',sources=last,total=count,rss_kib=guard(),
                current={name+str(sign):math.sqrt(state['max_selected_pair_squared']) for (name,sign),state in states.items()})),flush=True)
    del tree
    unit=F(1,2**53);allowance=F(1,2**1000)
    def coordinate(index):
        radial,angular=divmod(int(index),shape[1])
        return dict(flat_index=int(index),radial_index=radial,angular_index=angular,
            numerical_t=float(t[radial]),eta=float(2*np.pi*angular/shape[1]),
            physical_s=0. if radial==0 else None,cartesian=points[index].tolist(),
            coordinate_scope='Exact saved numerical t/eta indices. Physical s/theta require the original current chart replay except s=0 at the core.')
    results={}
    for (name,sign),state in states.items():
        if state['complete_base_sources_scanned']!=count:raise ValueError('A complete source sweep was omitted')
        candidate=state['candidate'];W=points[candidate['source_index']]
        minimum=math.inf;best=None;scanned=0
        for first in range(0,count,batch):
            last=min(first+batch,count);values=rotate(points[first:last],sign)
            for reflection in ((False,True) if name=='reflected_union' else (False,)):
                if reflection:values[:,2]*=-1
                diff=values-W;squared=np.sum(diff*diff,axis=1);k=int(np.argmin(squared))
                if float(squared[k])<minimum:
                    minimum=float(squared[k]);best=dict(index=first+k,reflected_in_z=reflection,rotated_point=values[k].tolist())
                scanned+=len(values)
            del values,diff,squared
        if scanned!=count*(2 if name=='reflected_union' else 1):raise ValueError('The complete witness target scan was omitted')
        lower_q=max(F(0),(binary(minimum)-allowance)/(1+unit)**5)
        selected_exact=sum((binary(x)-binary(y))**2 for x,y in zip(W,best['rotated_point']))
        lower=sqrt_interval(lower_q)[0];witness_upper=sqrt_interval(selected_exact)[1]
        global_upper_q=(binary(state['max_selected_pair_squared'])+allowance)/(1-unit)**5
        global_upper=sqrt_interval(global_upper_q)[1]
        if lower>witness_upper or witness_upper>global_upper:
            raise ArithmeticError('The exact finite Hausdorff sandwich crossed')
        source_point=W if sign==1 else rotate(W,1)
        target_point=np.asarray(best['rotated_point']) if sign==1 else rotate(np.asarray(best['rotated_point']),1)
        key=name+('_to_rotated' if sign==1 else '_rotated_to_original')
        results[key]=dict(unrotated_query_sign=sign,complete_base_sources_scanned=count,
            additional_reflected_sources_paid_by_exact_commuting_reflection=(name=='reflected_union'),
            complete_witness_targets_scanned=scanned,
            global_selected_pair_maximum_float_squared=state['max_selected_pair_squared'],
            exact_global_selected_pair_squared_upper=rat(global_upper_q),
            finite_directed_Hausdorff_lower=rat(lower),finite_directed_Hausdorff_upper=rat(global_upper),
            finite_directed_distance_display=[float(lower),float(global_upper)],
            witness_base_point=coordinate(candidate['source_index']),nearest_base_point=coordinate(best['index']),
            actual_directed_source_point=source_point.tolist(),actual_directed_target_point=target_point.tolist(),
            nearest_target_reflected_in_z=best['reflected_in_z'],exact_witness_selected_pair_squared=rat(selected_exact),
            witness_nearest_distance_display=[float(lower),float(witness_upper)],
            all_selected_pairs_are_actual_set_members=True,no_exact_unique_nearest_point_claim=True)
        print(json.dumps(dict(event='full_phase_witness_direct_scan_finished',case=key,
            directed_distance=[float(lower),float(global_upper)],source_index=candidate['source_index'],target_index=best['index'],
            rss_kib=guard())),flush=True)
    aggregate={}
    for name,diamkey in (('prefix','prefix_set'),('reflected_union','explicitly_reflected_diagnostic_set')):
        rr=[results[name+s] for s in ('_to_rotated','_rotated_to_original')]
        lo=max(unrat(x['finite_directed_Hausdorff_lower']) for x in rr)
        hi=max(unrat(x['finite_directed_Hausdorff_upper']) for x in rr)
        d=diameter[diamkey];dl,du=unrat(d['diameter_lower']),unrat(d['diameter_upper'])
        aggregate[name]=dict(finite_Hausdorff_lower=rat(lo),finite_Hausdorff_upper=rat(hi),
            finite_Hausdorff_display=[float(lo),float(hi)],same_set_finite_diameter_display=[float(dl),float(du)],
            finite_Hausdorff_over_same_finite_D_display=[float(lo/du),float(hi/dl)],
            finite_Hausdorff_over_same_finite_D_bounds=[rat(lo/du),rat(hi/dl)])
    record=dict(schema='complete-saved-prefix-quarter-phase-finite-Hausdorff-v1',scope=__doc__,
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),
        input_sha256={str(path):sha(path) for path in (a.screen,a.geometry_resource,a.prepared_core,points_path,grid_path,a.diameter,a.r1,a.r7)},
        current_data_scope='A q126 unsolved M32 warm prefix point set based on accepted q122; not the subsequently accepted A solution.',
        full_stored_core=screen['actual_core'],warm_profile=screen['warm_profile'],
        all_complete_points_and_chunks_consumed=True,point_shape=list(shape),prefix_count=count,reflected_union_count=2*count,
        complete_original_mean_angular=1552,chunks=chunks,query_blocks=blocks,directed_cases=results,sets=aggregate,
        phase_convention=dict(ambient_quarter_turn=[[0,-1,0],[1,0,0],[0,0,1]],reflection=[[1,0,0],[0,1,0],[0,0,-1]],
            R1_family='F_alpha(s,theta)=R_alpha F_0(s,theta-alpha); the full angular image is rotated. This diagnostic chooses the saved image samples then rotates them exactly.',
            material_reparametrization_is_not_pointwise_displacement=True,
            arbitrary_radial_and_angular_nearest_neighbours_allowed=True,
            second_direction_computed_by_common_inverse_isometry=True,
            reflection_and_rotation_commute_exactly=True,
            no_fixed_cap_or_marker_points_in_either_saved_set=True,
            quarter_phase_is_not_claimed_global_maximum_over_all_phases=True),
        rigorous_finite_arithmetic_scope=dict(binary64_unit_roundoff=rat(unit),positive_squared_sum_relative_factors=5,
            absolute_subnormal_allowance=rat(allowance),all_coordinates_magnitude_less_than_1024=True,
            all_selected_pairs_complete_global_max_upper=True,
            KD_tree_nearest_accuracy_not_required_for_upper_bound=True,
            lower_bound_uses_complete_direct_target_scan_not_tree=True,
            selected_exact_binary_witness_pairs_and_square_root_sandwich=True,sqrt_bits=100),
        scipy_version=scipy.__version__,KD_tree_options=dict(leafsize=32,compact_nodes=True,balanced_tree=True,copy_data=False,eps=0.,workers=1),
        RSS_limit_MiB=a.rss_limit_mib,new_ODE_Node_Jacobian_or_geometry_field_calls=0,
        derived_point_blocks_not_copied=True,continuous_sampling_or_cap_error_paid=False,
        full_closed_surface_D_deltaHold_reach_or_deltaE_certified=False,
        rigid_motion_quotient_Hausdorff_of_these_two_finite_sets_is_zero=True,
        elapsed_seconds=time.monotonic()-started,peak_rss_kib=guard())
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(record,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(event='complete_full_prefix_phase_Hausdorff_finished',out=str(a.out),sha256=sha(a.out),
        sets=aggregate,seconds=record['elapsed_seconds'],peak_rss_kib=record['peak_rss_kib'])),flush=True)


if __name__=='__main__':main()
