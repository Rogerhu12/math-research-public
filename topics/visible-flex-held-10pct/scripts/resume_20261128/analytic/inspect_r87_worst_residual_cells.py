#!/usr/bin/env python3
"""Inspect only the genuine worst cells already identified by an RMS report.

Retain the original complete state and parameters. Evaluate the two nodes,
midpoint and two off-midpoint RMS points of each recorded worst interval.
The extended-precision evaluation is a diagnostic of that same stored input,
not a changed live solver, new BVP, Jacobian or acceptance gate.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name] = '1'

import argparse
import hashlib
import inspect
import json
from pathlib import Path
import resource
import sys
import time

import numpy as np
import scipy.integrate._bvp as bvp

HERE = Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import check_unaccepted_design_delta_nodes_v2 as builder


def ref(path):
    path=Path(path).resolve()
    return dict(path=str(path),sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def fmax(values):
    return float(np.max(np.abs(values)))


def hermite(y,f,h,t):
    q=np.asarray(t,np.longdouble)[None,:]
    h=np.longdouble(h)
    left,right=y[:,0,None],y[:,1,None]
    fleft,fright=f[:,0,None],f[:,1,None]
    value=left+(right-left)*(3*q*q-2*q*q*q)+h*(q*(q-1)**2*fleft+q*q*(q-1)*fright)
    derivative=6*q*(q-1)*(left-right)/h+(3*q*q-4*q+1)*fleft+(3*q*q-2*q)*fright
    return value,derivative


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--residual-report',type=Path,required=True)
    parser.add_argument('--outdir',type=Path,required=True)
    args=parser.parse_args()
    original=json.loads(args.residual_report.read_text())
    if original['kind']!='actual_original_unaccepted_full_residual_observations':
        raise ValueError('Use the actual already returned complete RMS observation')
    source=args.residual_report.parent/'source-run-snapshot.json'
    if ref(source)['sha256']!=original['source_run_snapshot_sha256']:
        raise ValueError('The genuinely observed source snapshot changed')
    record=json.loads(source.read_text())
    for path,digest in original['original_definition_hashes'].items():
        if ref(path)['sha256']!=digest:
            raise ValueError('A complete original source/input changed: '+path)
    out=args.outdir.resolve()
    repo=HERE.parents[4]
    if out==repo or repo in out.parents:
        raise ValueError('Use a fresh scratch diagnostic output')
    out.mkdir(parents=True,exist_ok=False)
    obj,tables,branch=builder.build_original_model(record,repo)
    started=time.monotonic()
    results=[]
    for observed in original['observations']:
        path=Path(observed['checkpoint_path'])
        if ref(path)['sha256']!=observed['checkpoint']['sha256']:
            raise ValueError('The original complete checkpoint changed')
        with np.load(path,allow_pickle=False) as data:
            x,y,p=(data[k].copy() for k in ('x','y','p'))
        index=observed['maximum_RMS_interval_index']
        t=x[index:index+2]
        yy=y[:,index:index+2]
        if t.tolist()!=observed['maximum_RMS_interval']:
            raise ValueError('The actual worst interval no longer matches its saved report')
        h=np.diff(t)
        col,ym,f,fm=bvp.collocation_fun(obj.fun,yy,p,t,h)
        spline=bvp.create_spline(yy,f,t,h)
        middle=t[:1]+h/2
        distance=h/2*(3/7)**.5
        tt=np.r_[middle,middle+distance,middle-distance]
        sampled_y=np.column_stack((ym[:,0],spline(tt[1:])))
        sampled_f=np.column_stack((fm[:,0],obj.fun(tt[1:],sampled_y[:,1:],p)))
        sampled_d=spline(tt,1)
        residual=np.column_stack((1.5*col[:,0]/h[0],sampled_d[:,1:]-sampled_f[:,1:]))
        normalized=residual/(1+np.abs(sampled_f))
        components=np.sqrt(.5*(32/45*normalized[:,0]**2+49/90*(normalized[:,1]**2+normalized[:,2]**2)))
        rms=float(np.linalg.norm(components))
        scipyrms=float(bvp.estimate_rms_residuals(obj.fun,spline,t,h,p,(1.5*col/h).copy(),fm)[0])
        worst=int(np.argmax(components))
        # Same literal real inputs, original function, no model/Jacobian edit.
        fl=obj.fun(t,yy.astype(np.longdouble),p)
        fm_same=obj.fun(tt,sampled_y.astype(np.longdouble),p)
        q=(tt.astype(np.longdouble)-np.longdouble(t[0]))/np.longdouble(h[0])
        ylong,dlong=hermite(yy.astype(np.longdouble),fl,h[0],q)
        f_at_long=obj.fun(tt,ylong,p)
        rlong=dlong-f_at_long
        nlong=rlong/(1+np.abs(f_at_long))
        rmslong=float(np.sqrt(.5*np.sum(32/45*nlong[:,0]**2+49/90*(nlong[:,1]**2+nlong[:,2]**2))))
        obj.initial(p)
        flow=obj.flow(p[0])
        all_t=np.r_[t[0],tt,t[1]]
        s,ds=obj.chart(all_t,p[0])
        a,v,acc=flow.profile(s)
        physical_breaks=np.asarray(flow.breakpoints)
        surrounding=physical_breaks[(physical_breaks>=s[0]-2*(s[-1]-s[0]))&(physical_breaks<=s[-1]+2*(s[-1]-s[0]))]
        distances=np.abs(s[:,None]-physical_breaks[None,:])
        reference_s=np.mod(s,flow.period)/flow._multistage_ratio
        segments=flow._multistage_segments
        starts=np.asarray([row[0] for row in segments])
        ids=np.clip(np.searchsorted(starts,reference_s,side='right')-1,0,len(starts)-1)
        segment_coordinates=[float((z-segments[j][0])/segments[j][1]) for z,j in zip(reference_s,ids)]
        label=('radial' if worst<=obj.M else 'tangential' if worst<obj.iz else 'height')
        result=dict(checkpoint=ref(path),nodes=len(x),source_observed_interval=index,
            t=t.tolist(),h=float(h[0]),p=p.tolist(),gauge_q=obj.q,
            support_scales_are_not_RHS_divisors=True,
            recomputed_one_cell_RMS=rms,original_scipy_one_cell_RMS=scipyrms,
            previously_observed_global_maximum_RMS=observed['maximum_RMS'],
            worst_component=worst,worst_component_family=label,
            component_RMS=components.tolist(),normalized_residual_three_points=normalized.tolist(),
            raw_residual_three_points=residual.tolist(),RHS_three_points=sampled_f.tolist(),
            derivative_three_points=sampled_d.tolist(),
            endpoint_Y_maximum=fmax(yy),endpoint_RHS_maximum=fmax(f),
            maximum_collocation_residual=fmax(col),
            full_RHS_same_literal_Y_extended_precision_difference=fmax(fm_same-sampled_f.astype(np.longdouble)),
            endpoint_RHS_extended_precision_difference=fmax(fl-f.astype(np.longdouble)),
            same_Hermite_extended_Y_difference=fmax(ylong-sampled_y.astype(np.longdouble)),
            same_Hermite_extended_derivative_difference=fmax(dlong-sampled_d.astype(np.longdouble)),
            full_extended_Hermite_RHS_residual_RMS=rmslong,
            maximum_extended_residual_difference=fmax(rlong-residual.astype(np.longdouble)),
            original_physical_query_s=s.tolist(),original_chart_ds=ds.tolist(),
            original_profile_a=a.tolist(),original_profile_v=v.tolist(),original_profile_acc=acc.tolist(),
            nearby_physical_profile_breaks=surrounding.tolist(),
            closest_actual_profile_break_distance=distances.min(axis=1).tolist(),
            reference_segment_ids=ids.tolist(),reference_segment_coordinates=segment_coordinates,
            actual_source_segment_rows=[segments[int(i)] for i in np.unique(ids)],
            mathematical_bound_claimed=False,full_J_or_BVP_called=False)
        results.append(result)
        print(json.dumps({key:result[key] for key in ('nodes','t','worst_component','worst_component_family',
            'recomputed_one_cell_RMS','full_extended_Hermite_RHS_residual_RMS',
            'full_RHS_same_literal_Y_extended_precision_difference','maximum_extended_residual_difference',
            'nearby_physical_profile_breaks')}),flush=True)
    paths=[Path(__file__),Path(builder.__file__),Path(bvp.__file__)]
    paths.extend(Path(inspect.getsourcefile(getattr(type(obj),name))).resolve() for name in ('fun','initial','bc_jac'))
    report=dict(status='actual_worst_cells_profile_and_precision_inspected',source=ref(__file__),
        original_RMS_report=ref(args.residual_report),source_snapshot=ref(source),
        original_definition_hashes=original['original_definition_hashes'],
        source_hashes={str(p.resolve()):ref(p)['sha256'] for p in paths},
        original_model_branch=branch,observations=results,
        precision=dict(float64_bits=np.finfo(np.float64).nmant,longdouble_bits=np.finfo(np.longdouble).nmant),
        complete_RHS_mesh_recomputed=False,Jacobian_assembled=False,Newton_or_BVP_invoked=False,
        live_process_or_source_changed=False,acceptance_claimed=False,
        seconds=time.monotonic()-started,maximum_rss_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    dest=out/'report.json'
    dest.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(status=report['status'],report=ref(dest),seconds=report['seconds'],
        maximum_rss_KiB=report['maximum_rss_KiB'])),flush=True)


if __name__=='__main__':
    main()
