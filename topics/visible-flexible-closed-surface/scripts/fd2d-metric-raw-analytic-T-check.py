#!/usr/bin/env python3
"""Check the new analytic raw T column at interior and near-boundary points.

The saved raw field is held fixed. The near-boundary T point is an explicitly
synthetic derivative probe, not a new solved field or admissible surface.
Centered and second-order inward differences are independent finite diagnostics;
they are not the production column and are not rigorous error certificates.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse
import json
from pathlib import Path
import time
import numpy as np
from fd2d_gc_archive_arrays import identity,load_npz
from fd2d_gc_raw_lifted_dae import RawLiftedDAE as BaseRawLiftedDAE
from fd2d_gc_raw_analytic_T import AnalyticTRawLiftedDAE

HERE=Path(__file__).resolve().parent
TOP=HERE.parent


def error(difference,analytic):
    delta=np.asarray(difference)-np.asarray(analytic)
    return dict(absolute_max=float(np.max(np.abs(delta),initial=0.)),
        relative_l2=float(np.linalg.norm(delta)/max(1.,np.linalg.norm(analytic))))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--field',type=Path,required=True)
    p.add_argument('--candidate',type=Path,default=TOP/'notes/2026-11-12-fd2d-flat-cut-prefix-v1-coast-compatible-candidate.json')
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--mesh-step',type=float,default=.04)
    args=p.parse_args()
    if args.out.exists():raise FileExistsError('Use a new report')
    started=time.monotonic()
    saved=load_npz(args.field)
    K=(saved['corrections'].shape[1]-2)//3
    choices={}
    for key in ('profile_kind','tail_kind','base_kind'):
        if key not in saved:raise ValueError('This check requires the saved explicit '+key)
        choices[key]=str(saved[key])
    if str(saved['candidate_sha256'])!=identity(args.candidate)['sha256']:
        raise ValueError('Saved field binds another physical candidate')
    common=dict(modes=K,max_step=args.mesh_step,gap=.9,**choices)
    problem=AnalyticTRawLiftedDAE(args.candidate,**common)
    base=BaseRawLiftedDAE(args.candidate,**common)
    if not np.array_equal(saved['mesh'],problem.x):
        raise ValueError('Wrong actual radial mesh')
    original=np.r_[saved['corrections'].ravel(),saved['parameters']]
    F,J,data=problem.evaluate(original,jacobian=True)
    FB,JB,base_data=base.evaluate(original,jacobian=True)
    difference=(J[:,:-1]-JB[:,:-1]).tocoo()
    equal=dict(F_max=float(np.max(np.abs(F-FB))),fields_max=float(np.max(np.abs(data['fields']-base_data['fields']))),
        non_T_Jacobian_max=float(np.max(np.abs(difference.data),initial=0.)))
    bound=float(problem.profile.model.Tmax)
    cases=[('actual_interior',float(original[-1]),'centered',(8e-6,4e-6,2e-6,1e-6)),
           ('synthetic_near_upper',bound-2.25e-13,'inward_backward',(2e-5,1e-5,5e-6,2.5e-6))]
    rows=[]
    for name,T,method,steps in cases:
        vector=original.copy();vector[-1]=T
        _,_,values=problem.evaluate(vector,jacobian=True)
        analytic=values['analytic_T']
        def at(point):
            if not 0<point<bound:
                raise ValueError('Finite probe would leave the actual physical interval')
            z=vector.copy();z[-1]=point
            problem.profile.set_parameter(point)
            residual,data0=problem.evaluate(z,jacobian=False)
            ops=problem.operators(point)
            return dict(raw_F_T=residual,op_T=ops['op'],
                forcing_T=data0['lift']['forcing'],field_T=data0['fields'])
        baseline=at(T)
        samples=[]
        for h in steps:
            if method=='centered':
                left,right=T-h,T+h
                lm,rp=at(left),at(right)
                finite={key:(rp[key]-lm[key])/(right-left) for key in baseline}
                points=[left,right]
            else:
                one,two=T-h,T-2*h
                f1,f2=at(one),at(two)
                d1,d2=one-T,two-T
                w1=-d2/(d1*(d1-d2));w2=-d1/(d2*(d2-d1))
                finite={key:w1*(f1[key]-baseline[key])+w2*(f2[key]-baseline[key])
                        for key in baseline}
                points=[T,one,two]
            samples.append(dict(step=h,actual_probe_T=points,
                all_points_strictly_inside=bool(all(0<t<bound for t in points)),
                errors={key:error(finite[key],analytic[key]) for key in baseline}))
        rows.append(dict(name=name,T=T,Tmax=bound,upper_gap=bound-T,method=method,
            production_definition=analytic['definition'],
            derivative_norms={key:float(np.linalg.norm(analytic[key])) for key in baseline},
            samples=samples,synthetic_point_not_new_candidate=name.startswith('synthetic')))
    checks=dict(original_residual_unchanged=equal['F_max']==0.,
        original_fields_unchanged=equal['fields_max']==0.,
        all_non_T_columns_unchanged=equal['non_T_Jacobian_max']==0.,
        all_probe_points_inside=all(s['all_points_strictly_inside'] for row in rows for s in row['samples']),
        actual_interior_column=rows[0]['samples'][-1]['errors']['raw_F_T']['relative_l2']<2e-6,
        near_upper_column=rows[1]['samples'][-1]['errors']['raw_F_T']['relative_l2']<2e-5)
    report=dict(schema='fd2d-analytic-raw-T-column-check-v1',
        field=identity(args.field),candidate=identity(args.candidate),
        sources=[identity(__file__),identity(HERE/'fd2d_gc_raw_analytic_T.py'),
                 identity(HERE/'fd2d_gc_raw_lifted_dae.py'),identity(HERE/'fd2d_gc_raw_native_field.py'),
                 identity(HERE/'fd2d_gc_design_profile_positive.py')],
        modes=K,choices=choices,unchanged_columns=equal,cases=rows,checks=checks,
        implementation_checks_passed=all(checks.values()),elapsed_seconds=time.monotonic()-started,
        production_uses_finite_difference=False,continuous_certificate=False)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(report=str(args.out),checks=checks,unchanged=equal,
        final_errors={row['name']:row['samples'][-1]['errors'] for row in rows},
        elapsed_seconds=report['elapsed_seconds'])),flush=True)
    return 0 if all(checks.values()) else 1


if __name__=='__main__':raise SystemExit(main())

