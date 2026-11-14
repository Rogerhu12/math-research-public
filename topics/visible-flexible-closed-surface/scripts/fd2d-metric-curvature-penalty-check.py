"""Check the optional finite merit on an explicitly supplied saved raw field.

This recovered checker has not yet run. Pass --arrays for a real mesh/corrections/
parameters NPZ. It never certifies or solves that input, and never changes raw F.
"""
from __future__ import annotations
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse
import hashlib
import json
from pathlib import Path
import time
import numpy as np
from fd2d_gc_raw_lifted_dae import RawLiftedDAE
from fd2d_gc_curvature_penalty import curvature_penalty,penalty_values_on_labels,_active

HERE=Path(__file__).resolve().parent


def identity(path):
    p=Path(path);b=p.read_bytes()
    return dict(path=str(p.resolve()),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())


def maximum(x):
    return float(np.max(np.abs(x),initial=0.))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--arrays',type=Path,required=True)
    parser.add_argument('--candidate',type=Path,default=HERE.parent/'notes/2026-11-12-fd2d-flat-cut-prefix-v1-coast-compatible-candidate.json')
    parser.add_argument('--mesh-step',type=float,default=.04)
    args=parser.parse_args()
    if args.out.exists():
        raise FileExistsError('Use a new report')
    started=time.monotonic()
    with np.load(args.arrays,allow_pickle=False) as z:
        nodes=z['mesh'].copy();values=z['corrections'].copy();parameters=z['parameters'].copy()
    K=(values.shape[1]-2)//3
    source_ids=[identity(__file__),identity(HERE/'fd2d_gc_curvature_penalty.py'),
                identity(HERE/'fd2d_gc_raw_lifted_dae.py')]
    problem=RawLiftedDAE(args.candidate,modes=K,max_step=args.mesh_step,gap=.9,
                         profile_kind='positive_clock',tail_kind='positive_bernstein')
    if not np.array_equal(nodes,problem.x):
        raise ValueError('Supplied raw field uses another radial grid; pass its true mesh-step/chart')
    vector=np.r_[values.ravel(),parameters]
    raw,data=problem.evaluate(vector)
    cap=125/17;weight=.2
    result=curvature_penalty(problem,vector,cap=cap,weight=weight,data=data)
    raw_after,data_after=problem.evaluate(vector)
    rng=np.random.default_rng(129131)
    offset=problem.q*problem.N
    directions={}
    d=np.zeros_like(vector);d[:offset]=rng.standard_normal(offset)
    directions['three_independent_node_fields']=d/np.linalg.norm(d)
    d=np.zeros_like(vector);d[offset+problem.K:-1]=rng.standard_normal(problem.K+1)
    directions['tail_parameters']=d/np.linalg.norm(d)
    d=np.zeros_like(vector);d[-1]=1.
    directions['physical_T']=d
    d=np.zeros_like(vector);d[offset:offset+problem.K]=rng.standard_normal(problem.K)
    directions['central_c_before_boundary_composition']=d/np.linalg.norm(d)
    rows=[]
    for name,d in directions.items():
        exact=result['jacobian']@d
        for h in (1e-5,3e-6,1e-6):
            plus_vector=vector+h*d;minus_vector=vector-h*d
            if not 0<minus_vector[-1]<plus_vector[-1]<problem.profile.model.Tmax and name=='physical_T':
                rows.append(dict(direction=name,step=h,skipped='Centered difference would leave the actual physical T domain'))
                continue
            _,plus=problem.evaluate(plus_vector)
            _,minus=problem.evaluate(minus_vector)
            pv=penalty_values_on_labels(plus['fields'],result['labels'],result['branch'],cap=cap,weight=weight)
            mv=penalty_values_on_labels(minus['fields'],result['labels'],result['branch'],cap=cap,weight=weight)
            finite=(pv-mv)/(2*h);error=finite-exact
            rows.append(dict(direction=name,step=h,absolute_maximum=maximum(error),
                relative_l2=float(np.linalg.norm(error)/max(1.,np.linalg.norm(exact))),
                fixed_active_rows=len(exact),
                original_active_hinges_remained_positive=bool(np.all(pv>0)&np.all(mv>0))))
    synthetic=np.array([[[10.,0.,10.],[0.,0.,0.],[-10.,0.,-10.]]])
    residual,gradient,labels,branch,repeated,_,_=_active(synthetic,cap,weight)
    subgradient_slack=[]
    for sign in (1.,-1.):
        for _ in range(32):
            v=rng.standard_normal(3)*.01
            n,m,l=sign*10+v[0],v[1],sign*10+v[2]
            ev=np.linalg.eigvalsh(np.array([[n,m],[m,l]]))
            f=float(ev[-1]) if sign>0 else float(-ev[0])
            linear=sign*.5*(v[0]+v[2])
            subgradient_slack.append(f-10-linear)
    disabled=curvature_penalty(problem,vector,cap=cap,weight=0.,data=data)
    report=dict(schema='fd2d-finite-curvature-merit-check-recovered-v1',
        sources_at_start=source_ids,candidate=identity(args.candidate),arrays=identity(args.arrays),
        K=K,cap=cap,weight=weight,penalty=result['info'],
        sparse_matrix_shape=list(result['jacobian'].shape),directional_checks=rows,
        original_raw_F_absolute_change=maximum(raw_after-raw),
        original_fields_absolute_change=maximum(data_after['fields']-data['fields']),
        repeated_eigenvalue_check=dict(fields_nml=synthetic.tolist(),
            residual=residual.tolist(),gradients_nml=gradient.tolist(),
            labels=labels.tolist(),branch=branch.tolist(),repeated=repeated.tolist(),
            minimum_tested_subgradient_slack=float(min(subgradient_slack)),
            exact_zero_matrix_has_no_row=bool(not np.any(labels[:,1]==1))),
        zero_weight=dict(row_count=len(disabled['residual']),matrix_shape=list(disabled['jacobian'].shape)),
        scope='Derivative/merit implementation check only; the input field is not solved or geometrically certified by this check.',
        seconds=time.monotonic()-started)
    ordinary=[q for q in rows if q.get('step')==1e-6 and 'relative_l2' in q and q['original_active_hinges_remained_positive']]
    report['implementation_checks_passed']=bool(
        maximum(raw_after-raw)==0. and maximum(data_after['fields']-data['fields'])==0.
        and ordinary and max(q['relative_l2'] for q in ordinary)<2e-6
        and np.all(repeated) and len(residual)==2
        and report['repeated_eigenvalue_check']['exact_zero_matrix_has_no_row']
        and min(subgradient_slack)>-1e-13 and len(disabled['residual'])==0)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(report),flush=True)
    return 0 if report['implementation_checks_passed'] else 1


if __name__=='__main__':
    raise SystemExit(main())
