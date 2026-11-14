#!/usr/bin/env python3
"""Regenerate the useful 25%/75% initializer from committed inputs.

Reconstructed from complete execution history after the cloud executor
became unavailable. This NEW source must actually run before any output
is described as recovered. No old unavailable numerical entity is read
or claimed present. No nonlinear BVP or new IVP is solved here.

Default recipe is the actual earlier best explicit bridge:
preserve the true prefix to s=.5, relax log(n/nref) to zero by s=.9,
and add the exact tail shape with a quintic weight starting at s=.95.
Then take 25% and 75% of one fixed-parameter linear Codazzi projection.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import gzip
import hashlib
import io
import json
import platform
from pathlib import Path
import resource
import time
import numpy as np
import scipy
from fd2d_gc_raw_bridge_api_snapshot_01 import RawLiftedDAE,step5
from fd2d_flat_gc_codazzi_api_projector import FixedCodazziProjector
from fd2d_flat_prefix_initializer import ActualFlatPrefixInitializer


EXPECTED_CANDIDATE_SHA='a92b552f70bcc26c97f16261fbc78fac10c1daad6d72eafc8063dcb093cdd147'
EXPECTED_TRAJECTORY_SHA='db7614138c5f55b77e23f04849af02c75db36a277064b64f684a8da574c68c51'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_state(path, **arrays):
    buffer=io.BytesIO()
    np.savez_compressed(buffer,**arrays)
    payload=buffer.getvalue()
    final=Path(path)
    if len(payload)>1000000:
        payload=gzip.compress(payload,compresslevel=9,mtime=0)
        final=Path(str(final)+'.gz')
    if len(payload)>=5000000:
        raise ValueError('Artifact exceeds the repository single-item limit')
    final.write_bytes(payload)
    return dict(path=str(final),bytes=len(payload),sha256=sha(final))


def diagnostics(model,vector):
    unused,data=model.evaluate(vector)
    result=model.diagnostics(vector,data)
    result.update(
        codazzi_maximum=float(np.max(np.abs(data['codazzi_cells']))),
        projected_gauss_maximum=float(np.max(np.abs(data['projected_gauss']))),
        exact_endpoint_correction_maximum=float(np.max(np.abs(model.unpack(vector)[0][[0,-1]]))))
    return result,data


def explicit_bridge(model,prefix,*,handoff=.5,relaxation_end=.9,
                    tail_start=.95,derivative_carry=0.):
    """Same physical recipe as the historical earlier-handoff screen."""
    p=np.r_[np.zeros(model.K),np.ones(model.K+1),.02]
    jet=model.operators(.02)['jet']
    lift=model.lifting(.02,p[model.K:-1])
    a,v,K,s=[np.asarray(jet[k],float) for k in ('a','a_s','K','s')]
    if not 0<=handoff<=prefix.interval[1] or not handoff<relaxation_end<s[-1]:
        raise ValueError('Invalid actual-prefix or relaxation interval')
    if not handoff<=tail_start<s[-1]:
        raise ValueError('The tail weight must start after the retained prefix')
    nr=np.sqrt(np.maximum(0.,(1-v)*(1+v)))/a
    U=model.coords['u']
    sn,cs=np.sin(U),np.cos(U)
    kk=model.tail(p[model.K:-1]).angle_jets(a[None,:]*sn)['kappa']
    nt,mt=kk*cs*cs,-kk*sn*cs
    tw=step5((s-tail_start)/(s[-1]-tail_start))[0]
    last=prefix.evaluate_material(np.full_like(U,handoff),U)
    aa,ap,app=prefix.candidate.profile(np.array([handoff]))
    nr0=float(np.sqrt((1-ap[0])*(1+ap[0]))/aa[0])
    K0=float(-app[0]/aa[0]);c0=float(ap[0]/aa[0])
    nr0s=c0*(K0/nr0-nr0)
    logg=np.log(last['n']/nr0)
    loggs=last['n_s']/last['n']-nr0s/nr0
    shear=last['m']/nr0
    shears=last['m_s']/nr0-shear*nr0s/nr0
    length=relaxation_end-handoff
    q=np.clip((s-handoff)/length,0.,1.)
    fade=1-step5(q)[0]
    h=q-6*q**3+8*q**4-3*q**5
    h[(s<=handoff)|(s>=relaxation_end)]=0.
    n=nr[None,:]*np.exp(fade[None,:]*logg+
        derivative_carry*length*h[None,:]*loggs)+tw[None,:]*nt
    m=nr[None,:]*(fade[None,:]*shear+
        derivative_carry*length*h[None,:]*shears)+tw[None,:]*mt
    keep=s<=handoff
    actual=prefix.evaluate_material(s[None,keep],U[:,keep])
    n[:,keep],m[:,keep]=actual['n'],actual['m']
    l=np.divide(K[None,:]+m*m,n,out=np.zeros_like(n),where=np.abs(n)>1e-14)
    total=np.stack((n,m,l),axis=-1)
    total[:,-1]=lift['values'][:,-1]
    correction=total-lift['values']
    y=np.concatenate(((model.PE@correction[...,0]).T,
                      (model.PO@correction[...,1]).T,
                      (model.PE@correction[...,2]).T),axis=1)
    y[0]=0.;y[-1]=0.
    return np.r_[y.ravel(),p],dict(
        handoff=handoff,relaxation_end=relaxation_end,tail_start=tail_start,
        derivative_carry=derivative_carry,tail_radius='current a(s)',
        true_prefix_retained_only_through=handoff,physical_T=.02,
        source_scope='actual shared-node cubic initializer, then explicit algebraic trial',
        exact_central_and_cut_retained=True)


def run(args):
    started=time.time()
    if sha(args.source)!=EXPECTED_CANDIDATE_SHA:
        raise ValueError('Different physical candidate; no silent substitution')
    if sha(args.trajectory)!=EXPECTED_TRAJECTORY_SHA:
        raise ValueError('Different actual trajectory; no silent substitution')
    stem=Path(args.stem)
    stem.parent.mkdir(parents=True,exist_ok=True)
    report_path=Path(str(stem)+'-report.json')
    if report_path.exists():
        raise FileExistsError('Use another stem; existing closed evidence is not overwritten')
    model=RawLiftedDAE(args.source,modes=7,max_step=.04,gap=.91,
        profile_kind='positive_clock',tail_kind='positive_bernstein')
    prefix=ActualFlatPrefixInitializer(args.trajectory,args.source,geometry=model.geometry)
    bridge,recipe=explicit_bridge(model,prefix,handoff=args.handoff,
        relaxation_end=args.relaxation_end,tail_start=args.tail_start,
        derivative_carry=args.derivative_carry)
    before,unused=diagnostics(model,bridge)
    y,p=model.unpack(bridge)
    projector=FixedCodazziProjector(model,p,l_weight=.5)
    delta,linear=projector.direction(bridge)
    outputs=[]
    all_diagnostics=[]
    for amount in (.25,.75):
        vector=bridge.copy()
        vector[projector.free]+=amount*delta
        diag,data=diagnostics(model,vector)
        yy,pp=model.unpack(vector)
        if not np.array_equal(pp,p) or not np.array_equal(yy[[0,-1]],y[[0,-1]]):
            raise ArithmeticError('The fixed physical/end-point data changed')
        suffix='025' if amount==.25 else '075'
        artifact=write_state(str(stem)+'-amount'+suffix+'.npz',
            x=model.x,corrections=yy,parameters=pp,vector=vector,
            fields_n_m_l=data['fields'],material_u=model.coords['u'],
            physical_s=np.asarray(model.operators(pp[-1])['jet']['s'],float),
            candidate_sha256=np.array(EXPECTED_CANDIDATE_SHA),
            trajectory_sha256=np.array(EXPECTED_TRAJECTORY_SHA),
            modes=np.array(model.K),blend=np.array(model.blend),
            profile_kind=np.array(model.profile_kind),tail_kind=np.array(model.tail_kind),
            base_kind=np.array(model.base_kind),amount=np.array(amount),
            initializer_only=np.array(True),source_reconstruction=np.array('API recovery source 01'))
        artifact['amount']=amount
        artifact['diagnostics']=diag
        outputs.append(artifact)
        all_diagnostics.append(diag)
        print(json.dumps(dict(event='actual_initializer_saved',amount=amount,
            output=artifact)),flush=True)
    scripts=Path(__file__).resolve().parent
    dependency_names=['fd2d-flat-prefix-bridge-api-recovery.py',
        'fd2d_gc_raw_bridge_api_snapshot_01.py','fd2d_flat_gc_codazzi_api_projector.py',
        'fd2d_flat_prefix_initializer.py','fd2d_gc_design_profile_positive.py',
        'fd2d_gc_design_profile.py','fd2d_gc_blended.py','fd2d_gc_intrinsic.py',
        'fd2d_balanced_curvature_core.py','fd2d_positive_flat_developable_family.py',
        'fd2d_flat_developable_family.py']
    inputs=dict(candidate=dict(path=args.source,sha256=sha(args.source)),
                actual_prefix=dict(path=args.trajectory,sha256=sha(args.trajectory)))
    report=dict(kind='new_actual_recomputation_from_committed_inputs',
        body_completed=True,inputs=inputs,recipe=recipe,
        finite_space=dict(modes=model.K,angular_work=model.work,
            radial_nodes=model.N,vector_size=model.size,blend=list(model.blend),
            component_order='n,m,l',profile_kind=model.profile_kind,
            tail_kind=model.tail_kind,base_kind=model.base_kind),
        bridge_diagnostics=before,linear_projection=linear,
        projector=projector.definition,outputs=outputs,
        source_sha256={name:sha(scripts/name) for name in dependency_names},
        versions=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__),
        runtime_seconds=time.time()-started,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        historical_reference_only=dict(
            source='in-session observed exits, not reverified old binary artifacts',
            previous_25_percent=dict(residual=9.189797098490777,
                full_gauss=2.3382541228866325,formal_curvature=7.001638467996436),
            previous_75_percent=dict(residual=3.0632656994969247,
                full_gauss=6.869729892456082,formal_curvature=7.123311908510938)),
        nonlinear_solution=False,continuous_metric_or_geometry_certificate=False)
    report_path.write_text(json.dumps(report,indent=2)+'\n')
    manifest_path=Path(str(stem)+'-manifest.json')
    manifest=dict(scope='New recomputed initialization files only',
        files=[dict(path=str(report_path),bytes=report_path.stat().st_size,sha256=sha(report_path))]+
              [{key:row[key] for key in ('path','bytes','sha256')} for row in outputs],
        source_sha256=report['source_sha256'],report_body_completed=True)
    manifest_path.write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps(dict(event='body_completed',report=str(report_path),
        report_sha256=sha(report_path),manifest=str(manifest_path),
        runtime_seconds=report['runtime_seconds'],peak_rss_kib=report['peak_rss_kib'])),flush=True)
    return report


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--source',default='notes/2026-11-12-fd2d-flat-cut-prefix-v1-coast-compatible-candidate.json')
    parser.add_argument('--trajectory',default='notes/2026-11-12-fd2d-flat-prefix-balanced-ivp-01-trajectory.npz.gz')
    parser.add_argument('--stem',default='notes/2026-11-12-fd2d-api-bridge-recovery-01')
    parser.add_argument('--handoff',type=float,default=.5)
    parser.add_argument('--relaxation-end',type=float,default=.9)
    parser.add_argument('--tail-start',type=float,default=.95)
    parser.add_argument('--derivative-carry',type=float,choices=[0.,1.],default=0.)
    args=parser.parse_args()
    run(args)


if __name__=='__main__':
    main()
