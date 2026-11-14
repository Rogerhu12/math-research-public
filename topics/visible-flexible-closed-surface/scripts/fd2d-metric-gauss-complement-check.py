#!/usr/bin/env python3
"""Finite JVP check of root's omitted-Gauss helper using the analytic T provider.

This does not solve or certify the supplied raw field. All original F values,
independent fields and analytic parameter choices remain unchanged. The test
records finite projection roundoff, including the nominally annihilated K_T.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse
import json
from pathlib import Path
import time
import numpy as np
from fd2d_gc_archive_arrays import identity,load_npz
from fd2d_gc_raw_analytic_T import AnalyticTRawLiftedDAE
from fd2d_gc_gauss_complement import gauss_complement

HERE=Path(__file__).resolve().parent
TOP=HERE.parent


def maximum(value):
    return float(np.max(np.abs(value),initial=0.))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--field',type=Path,required=True)
    p.add_argument('--candidate',type=Path,default=TOP/'notes/2026-11-12-fd2d-flat-cut-prefix-v1-coast-compatible-candidate.json')
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--weight',type=float,default=.3)
    p.add_argument('--mesh-step',type=float,default=.04)
    args=p.parse_args()
    if args.out.exists():raise FileExistsError('Use a new report')
    started=time.monotonic()
    source_paths=[Path(__file__),HERE/'fd2d_gc_gauss_complement.py',
        HERE/'fd2d_gc_raw_analytic_T.py',HERE/'fd2d_gc_raw_lifted_dae.py']
    source_ids=[identity(path) for path in source_paths]
    saved=load_npz(args.field)
    choices={key:str(saved[key]) for key in ('profile_kind','tail_kind','base_kind')}
    if str(saved['candidate_sha256'])!=identity(args.candidate)['sha256']:
        raise ValueError('Supplied field binds a different actual candidate')
    K=(saved['corrections'].shape[1]-2)//3
    problem=AnalyticTRawLiftedDAE(args.candidate,modes=K,max_step=args.mesh_step,gap=.9,**choices)
    if not np.array_equal(saved['mesh'],problem.x):
        raise ValueError('The recorded defining radial grid differs')
    vector=np.r_[saved['corrections'].ravel(),saved['parameters']]
    F,J,data=problem.evaluate(vector,jacobian=True)
    fields_before=data['fields'].copy()
    extra=gauss_complement(problem,vector,weight=args.weight,data=data)
    F_after,data_after=problem.evaluate(vector,jacobian=False)
    offset=problem.N*problem.q
    rng=np.random.default_rng(131133)
    directions={}
    d=np.zeros_like(vector);d[:offset]=rng.standard_normal(offset)
    directions['all_independent_state_fields']=d/np.linalg.norm(d)
    d=np.zeros_like(vector);d[offset+K:-1]=rng.standard_normal(K+1)
    directions['exact_tail_controls']=d/np.linalg.norm(d)
    d=np.zeros_like(vector);d[-1]=1.
    directions['physical_T']=d
    rows=[]
    for name,d in directions.items():
        exact=extra['jacobian']@d
        for h in (8e-6,4e-6,2e-6,1e-6):
            plus,minus=vector+h*d,vector-h*d
            if not 0<plus[-1]<problem.profile.model.Tmax or not 0<minus[-1]<problem.profile.model.Tmax:
                raise ValueError('Centered test point would leave the actual physical T interval')
            _,pd=problem.evaluate(plus,jacobian=False)
            _,md=problem.evaluate(minus,jacobian=False)
            pp=gauss_complement(problem,plus,weight=args.weight,data=pd,jacobian=False)['residual']
            mm=gauss_complement(problem,minus,weight=args.weight,data=md,jacobian=False)['residual']
            finite=(pp-mm)/(2*h);delta=finite-exact
            rows.append(dict(direction=name,step=h,analytic_direction_norm=float(np.linalg.norm(exact)),
                absolute_maximum=maximum(delta),relative_l2=float(np.linalg.norm(delta)/max(1.,np.linalg.norm(exact)))))
    def high(value):return value-problem.E@(problem.PE@value)
    omitted=high(data['full_gauss'][:,:-1])
    low_roundoff=maximum(problem.PE@omitted)
    n,m,l=data['fields'][:,:,0],data['fields'][:,:,1],data['fields'][:,:,2]
    T=data['fields_T']
    noK=l*T[:,:,0]+n*T[:,:,2]-2*m*T[:,:,1]
    withK=noK-data['K_T'][None,:]
    KT_projection_roundoff=maximum(high(noK[:,:-1])-high(withK[:,:-1]))
    source_after=[identity(path) for path in source_paths]
    unchanged_sources=all(a['sha256']==b['sha256'] for a,b in zip(source_ids,source_after))
    final=[q for q in rows if q['step']==1e-6]
    checks=dict(raw_F_unchanged=maximum(F_after-F)==0.,
        fields_unchanged=maximum(data_after['fields']-fields_before)==0.,
        source_bytes_unchanged=unchanged_sources,
        low_projection_roundoff_only=low_roundoff<1e-10,
        all_three_nonzero_directions=all(q['analytic_direction_norm']>1e-8 for q in final),
        all_three_JVP=all(q['relative_l2']<3e-6 for q in final))
    report=dict(schema='fd2d-finite-gauss-complement-JVP-check-v1',
        field=identity(args.field),candidate=identity(args.candidate),sources=source_ids,
        modes=K,choices=choices,weight=args.weight,helper=extra['info'],
        sparse_shape=list(extra['jacobian'].shape),sparse_nnz=int(extra['jacobian'].nnz),
        original_F_maximum_change=maximum(F_after-F),
        original_fields_maximum_change=maximum(data_after['fields']-fields_before),
        retained_projection_of_omitted_roundoff_max=low_roundoff,
        omitting_angular_constant_KT_changes_floating_projection_by=KT_projection_roundoff,
        directional_checks=rows,checks=checks,implementation_checks_passed=all(checks.values()),
        elapsed_seconds=time.monotonic()-started,continuous_certificate=False,
        scope='Finite implementation JVPs on the same recorded angular grid; no missing continuous angular modes are certified')
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(report=str(args.out),checks=checks,final_directions=final,
        low_projection_roundoff=low_roundoff,KT_projection_roundoff=KT_projection_roundoff,
        elapsed_seconds=report['elapsed_seconds'])),flush=True)
    return 0 if all(checks.values()) else 1


if __name__=='__main__':raise SystemExit(main())

