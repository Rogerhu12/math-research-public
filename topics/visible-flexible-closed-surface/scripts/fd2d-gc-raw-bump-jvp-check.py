#!/usr/bin/env python3
"""Actual raw-bump Jacobian checks and a zero-delta warm initializer."""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import json
from pathlib import Path
import platform
import time
import numpy as np
import scipy
from fd2d_gc_raw_bump_dae import RawBumpDAE
from fd2d_gc_raw_lifted_dae import RawLiftedDAE
from fd2d_gc_archive_arrays import load_npz,save_npz,identity


def maximum(q):
    return float(np.max(abs(np.asarray(q)),initial=0.))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--arrays',type=Path,required=True)
    ap.add_argument('--stem',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic()
    if list(args.stem.parent.glob(args.stem.name+'*')):
        raise FileExistsError('Use a new actual check stem')
    z=load_npz(args.arrays);mesh=z['mesh'];y=z['corrections'];p=z['parameters']
    K=(y.shape[1]-2)//3
    old=RawLiftedDAE(args.candidate,modes=K,max_step=.04,gap=.9,
        profile_kind='positive_clock',tail_kind='positive_bernstein')
    if not np.array_equal(mesh,old.x):
        raise ValueError('The actual warm input grid does not match its recorded model')
    vector_old=np.r_[y.ravel(),p]
    oldF,oldData=old.evaluate(vector_old)
    same=RawBumpDAE(args.candidate,modes=K,max_step=.04,gap=.9,include_support_knots=False)
    samev=same.warm_from_standard(mesh,y,p,candidate_sha256=z['candidate_sha256'])
    sameF,sameData=same.evaluate(samev)
    zero_comparison=dict(original_F_absolute_max=maximum(sameF-oldF),
        fields_absolute_max=maximum(sameData['fields']-oldData['fields']),
        full_gauss_absolute_max=maximum(sameData['full_gauss']-oldData['full_gauss']))
    del same,sameData,old,oldData
    model=RawBumpDAE(args.candidate,modes=K,max_step=.04,gap=.9,include_support_knots=True)
    warm=model.warm_from_standard(mesh,y,p,candidate_sha256=z['candidate_sha256'])
    wy,wp=model.unpack(warm)
    warm_file=save_npz(Path(str(args.stem)+'-warm.npz'),mesh=model.x,
        corrections=wy,parameters=wp,modes=np.array(K),
        base_kind=np.array(model.base_kind),profile_kind=np.array(model.profile_kind),
        tail_kind=np.array(model.tail_kind),profile_supports=model.profile.supports,
        profile_count=np.array(model.J),fixed_base_T=np.array(model.fixed_base_T),
        candidate_sha256=np.array(model.profile.source_identity['sha256']),
        initializer_only=np.array(True))
    warm_diag=model.diagnostics(warm)
    vector=warm.copy();offset=model.N*model.q
    tested_delta=.0003*np.array([1.,-.7,.5,-.9,.4,.6,-.2])
    vector[offset+model.profile_slice.start:]=tested_delta
    F,J,data=model.evaluate(vector,jacobian=True)
    rng=np.random.default_rng(131007)
    directions={}
    q=np.zeros(model.size);q[:offset]=rng.standard_normal(offset);directions['independent_node_fields']=q/np.linalg.norm(q)
    q=np.zeros(model.size);q[offset+model.tail_slice.start:offset+model.tail_slice.stop]=rng.standard_normal(K+1)
    directions['actual_tail_controls']=q/np.linalg.norm(q)
    q=np.zeros(model.size);q[offset+model.profile_slice.start:]=rng.standard_normal(model.J)
    directions['physical_radial_deltas']=q/np.linalg.norm(q)
    q=np.zeros(model.size);q[offset:offset+K]=rng.standard_normal(K)
    directions['central_before_boundary_composition']=q/np.linalg.norm(q)
    q=directions['central_before_boundary_composition'].copy();q[:model.e]=model.core_coefficients@q[offset:offset+K]
    directions['central_with_exact_boundary_composition']=q/np.linalg.norm(q)
    rows=[]
    for name,direction in directions.items():
        exact=J@direction
        field_exact=np.einsum('wncp,p->wnc',data['fields_parameters'],direction[offset:])
        dy=direction[:offset].reshape(model.N,model.q)
        field_exact+=np.stack((model.E@dy[:,:model.e].T,
            model.O@dy[:,model.e:model.d].T,model.E@dy[:,model.d:].T),axis=-1)
        for h in (1e-5,3e-6,1e-6):
            plus,pd=model.evaluate(vector+h*direction)
            minus,md=model.evaluate(vector-h*direction)
            finite=(plus-minus)/(2*h);error=finite-exact
            fe=(pd['fields']-md['fields'])/(2*h)-field_exact
            rows.append(dict(direction=name,step=h,raw_absolute_maximum=maximum(error),
                raw_relative_l2=float(np.linalg.norm(error)/max(1.,np.linalg.norm(exact))),
                fields_absolute_maximum=maximum(fe),
                fields_relative_l2=float(np.linalg.norm(fe)/max(1.,np.linalg.norm(field_exact)))))
    report=dict(schema='fd2d-raw-physical-bump-jvp-check-v1',source=identity(__file__),
        dependencies=[identity(Path(__file__).with_name(name)) for name in
            ('fd2d_gc_raw_bump_dae.py','fd2d_gc_radial_bump_profile.py','fd2d_gc_raw_lifted_dae.py')],
        candidate=identity(args.candidate),input_arrays=identity(args.arrays),
        layout=model.parameter_layout(),zero_delta_same_grid_comparison=zero_comparison,
        grid_subdivision=dict(old_nodes=len(mesh),new_nodes=model.N,
            method='P1 evaluation at the union of old mesh and support endpoints; no solve'),
        warm=warm_file,warm_diagnostics=warm_diag,actual_test_delta=tested_delta.tolist(),
        jacobian_shape=list(J.shape),jacobian_nonzeros=int(J.nnz),directional_checks=rows,
        fields_parameters_shape=list(data['fields_parameters'].shape),
        versions=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__),
        seconds=time.monotonic()-started,
        scope='Implementation JVP plus a zero-delta actual warm initializer; neither a nonlinear solve nor a same-g refinement result')
    selected=[r for r in rows if r['step']==1e-6]
    report['passed']=bool(max(zero_comparison.values())<2e-10
        and max(r['raw_relative_l2'] for r in selected)<2e-6
        and max(r['fields_relative_l2'] for r in selected)<2e-6)
    rp=Path(str(args.stem)+'-report.json');rp.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(report=str(rp),passed=report['passed'],warm=warm_file,
        zero_delta_comparison=zero_comparison,jacobian_shape=list(J.shape),seconds=report['seconds'],
        maximum_raw_direction_relative_l2=max(r['raw_relative_l2'] for r in selected))),flush=True)
    return 0 if report['passed'] else 1


if __name__=='__main__':
    raise SystemExit(main())
