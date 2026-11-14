#!/usr/bin/env python3
"""Explicit bridge and fixed-parameter Codazzi initialization for its actual g.

The supplied trajectory must bind the supplied physical candidate. Only its
valid positive-n interval is read. Subsequent interpolation and the single
linear Codazzi projection are initialization choices, not a nonlinear solve.
The radial cut lifting retains all three exact fields and the cut mean.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse
import hashlib
import json
import platform
from pathlib import Path
import resource
import sys
import time
import numpy as np
import scipy
from fd2d_gc_raw_bridge_api_snapshot_01 import RawLiftedDAE,step5
from fd2d_flat_gc_codazzi_api_projector import FixedCodazziProjector
from fd2d_flat_prefix_initializer import ActualFlatPrefixInitializer
from fd2d_gc_archive_arrays import save_npz,identity


def diagnostics(model,vector):
    residual,data=model.evaluate(vector)
    result=model.diagnostics(vector,data)
    result.update(codazzi_maximum=float(np.max(abs(data['codazzi_cells']))),
        projected_gauss_maximum=float(np.max(abs(data['projected_gauss']))),
        exact_endpoint_correction_maximum=float(np.max(abs(model.unpack(vector)[0][[0,-1]]))))
    return result,data


def bridge(model,prefix,handoff,relaxation_end,tail_start):
    T=prefix.T
    p=np.r_[np.zeros(model.K),np.ones(model.K+1),T]
    jet=model.operators(T)['jet'];lift=model.lifting(T,p[model.K:-1])
    a,v,K,s=[np.asarray(jet[k],float) for k in ('a','a_s','K','s')]
    if not 0<=handoff<=prefix.interval[1] or not handoff<relaxation_end<s[-1]:
        raise ValueError('The handoff must be inside the actual closed IVP interval')
    if not handoff<=tail_start<s[-1]:
        raise ValueError('The exact tail lifting weight must start after handoff')
    nr=np.sqrt(np.maximum(0.,(1-v)*(1+v)))/a
    U=model.coords['u'];sn,cs=np.sin(U),np.cos(U)
    kk=model.tail(p[model.K:-1]).angle_jets(a[None,:]*sn)['kappa']
    nt,mt=kk*cs*cs,-kk*sn*cs
    tw=step5((s-tail_start)/(s[-1]-tail_start))[0]
    last=prefix.evaluate_material(np.full_like(U,handoff),U)
    aa,ap,_=prefix.candidate.profile(np.array([handoff]))
    nr0=float(np.sqrt((1-ap[0])*(1+ap[0]))/aa[0])
    logg=np.log(last['n']/nr0);shear=last['m']/nr0
    fade=1-step5((s-handoff)/(relaxation_end-handoff))[0]
    n=nr[None,:]*np.exp(fade[None,:]*logg)+tw[None,:]*nt
    m=nr[None,:]*fade[None,:]*shear+tw[None,:]*mt
    keep=s<=handoff
    actual=prefix.evaluate_material(s[None,keep],U[:,keep])
    n[:,keep],m[:,keep]=actual['n'],actual['m']
    # The final node is replaced by the full exact tail, without dividing n.
    l=np.divide(K[None,:]+m*m,n,out=np.zeros_like(n),where=abs(n)>1e-14)
    total=np.stack((n,m,l),axis=-1);total[:,-1]=lift['values'][:,-1]
    correction=total-lift['values']
    y=np.concatenate(((model.PE@correction[...,0]).T,
                      (model.PO@correction[...,1]).T,
                      (model.PE@correction[...,2]).T),axis=1)
    y[0]=0.;y[-1]=0.
    return np.r_[y.ravel(),p],dict(handoff=handoff,
        relaxation_end=relaxation_end,tail_start=tail_start,derivative_carry=0.,
        physical_T=T,tail_radius='actual a(s)',
        radial_coordinate='physical s from the actual positive design clock',
        maximum_abs_reference_x_minus_s=float(np.max(abs(model.x-s))),
        original_trajectory_interval=list(prefix.interval),
        true_prefix_retained_only_through=handoff,
        beyond_handoff='explicit logarithmic anisotropy relaxation and exact tail shape blending',
        exact_central_and_cut_retained=True)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--trajectory',type=Path,required=True)
    ap.add_argument('--expected-candidate-sha',required=True)
    ap.add_argument('--stem',type=Path,required=True)
    ap.add_argument('--modes',type=int,default=15)
    ap.add_argument('--mesh-step',type=float,default=.04)
    ap.add_argument('--handoff',type=float,required=True)
    ap.add_argument('--relaxation-end',type=float,required=True)
    ap.add_argument('--tail-start',type=float,required=True)
    args=ap.parse_args();started=time.monotonic()
    if identity(args.candidate)['sha256']!=args.expected_candidate_sha:
        raise ValueError('The physical candidate does not match the explicit requested SHA')
    if list(args.stem.parent.glob(args.stem.name+'*')):
        raise FileExistsError('Use a new stem for the actual computation')
    args.stem.parent.mkdir(parents=True,exist_ok=True)
    model=RawLiftedDAE(args.candidate,modes=args.modes,max_step=args.mesh_step,gap=.91,
        profile_kind='positive_clock',tail_kind='positive_bernstein')
    prefix=ActualFlatPrefixInitializer(args.trajectory,args.candidate,geometry=model.geometry)
    z,recipe=bridge(model,prefix,args.handoff,args.relaxation_end,args.tail_start)
    before,data=diagnostics(model,z)
    yy,pp=model.unpack(z)
    projector=FixedCodazziProjector(model,pp,l_weight=.5)
    delta,linear=projector.direction(z)
    outputs=[]
    for fraction,label in ((0.,'000'),(.25,'025'),(.75,'075')):
        vector=z.copy();vector[projector.free]+=fraction*delta
        dd,_=diagnostics(model,vector);y,p=model.unpack(vector)
        if not np.array_equal(p,pp) or not np.array_equal(y[[0,-1]],yy[[0,-1]]):
            raise ArithmeticError('The physical parameters or exact boundary corrections changed')
        file=save_npz(Path(str(args.stem)+'-amount'+label+'.npz'),
            mesh=model.x,x=model.x,corrections=y,parameters=p,modes=np.array(model.K),
            candidate_sha256=np.array(args.expected_candidate_sha),
            trajectory_sha256=np.array(identity(args.trajectory)['sha256']),
            profile_kind=np.array(model.profile_kind),tail_kind=np.array(model.tail_kind),
            base_kind=np.array(model.base_kind),blend=np.asarray(model.blend),
            physical_s=np.asarray(model.operators(p[-1])['jet']['s'],float),
            amount=np.array(fraction),initializer_only=np.array(True))
        row=dict(amount=fraction,output=file,diagnostics=dd);outputs.append(row)
        print(json.dumps(dict(event='actual_initializer_saved',**row)),flush=True)
    here=Path(__file__).resolve().parent
    imported=sorted({Path(m.__file__).resolve() for m in list(sys.modules.values())
        if getattr(m,'__file__',None) and Path(m.__file__).resolve().parent==here})
    report=dict(schema='fd2d-physical-g-bridge-recovery-v1',body_completed=True,
        source=identity(__file__),source_dependencies=[identity(p) for p in imported],
        inputs=dict(candidate=identity(args.candidate),trajectory=identity(args.trajectory)),
        recipe=recipe,finite_space=dict(modes=model.K,angular_work=model.work,
            radial_nodes=model.N,vector_size=model.size,blend=list(model.blend),
            component_order='n,m,l',mesh_step=args.mesh_step),
        bridge_diagnostics=before,linear_projection=linear,projector=projector.definition,
        outputs=outputs,seconds=time.monotonic()-started,
        versions=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__),
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        initializer_only=True,nonlinear_solution=False,continuous_certificate=False)
    rp=Path(str(args.stem)+'-report.json');rp.write_text(json.dumps(report,indent=2)+'\n')
    manifest=dict(scope='Closed explicit initializer and fixed-parameter linear projection only',
        files=[identity(rp)]+[q['output'] for q in outputs],source=identity(__file__))
    Path(str(args.stem)+'-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps(dict(event='body_completed',report=str(rp),seconds=report['seconds'],
        peak_rss_kib=report['peak_rss_kib'])),flush=True)


if __name__=='__main__':
    main()
