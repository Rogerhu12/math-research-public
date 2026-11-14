#!/usr/bin/env python3
"""Floating minimum-strain tangential projection on the SAME fixed target.

The actual common-prefix and optional own-tail metric is sampled in material
angle. A piecewise-linear radial p,q field is fitted separately for each
Fourier mode of g=ds^2+a(s)^2du^2. It minimizes all three normalized linear
metric errors together, instead of forcing E/F exactly to zero. The fit has
p(0)=0 and p=q=0 on a selected terminal collar. This is a SCREEN: the fitted
field is not C2, finite radial/angular samples are not a uniform bound, and
no nonlinear pullback map is constructed or certified.
"""
from __future__ import annotations

import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'

import argparse
import importlib.util
import json
from pathlib import Path
import sys
import time

import numpy as np
from scipy import fft
from scipy.linalg import solveh_banded

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
spec=importlib.util.spec_from_file_location('fd2d_noncircle_projection_source',
    HERE/'fd2d-metric-noncircle-gauge-screen.py')
screen=importlib.util.module_from_spec(spec);sys.modules[spec.name]=screen;spec.loader.exec_module(screen)
LD=screen.LD


def fit_mode(n,h,a,ap,error,weights,fixed):
    """Banded Hermitian normal equations for one exact Fourier symbol."""
    count=len(h);dimension=2*(count+1);omega=3j*n
    C=np.zeros((count,3,4),dtype=complex)
    C[:,0,0]=-2/h;C[:,0,2]=2/h
    C[:,1,0]=C[:,1,2]=omega/(2*a)
    C[:,1,1]=-a/h;C[:,1,3]=a/h
    C[:,2,0]=C[:,2,2]=ap/a
    C[:,2,1]=C[:,2,3]=omega
    w=(h*a*weights)[:,None]*np.array([1.,2.,1.])[None,:]
    H=np.einsum('cri,crj,cr->cij',C.conj(),C,w,optimize=True)
    b=-np.einsum('cri,cr,cr->ci',C.conj(),error,w,optimize=True)
    ab=np.zeros((4,dimension),dtype=complex);rhs=np.zeros(dimension,dtype=complex)
    base=2*np.arange(count)
    for i in range(4):
        np.add.at(rhs,base+i,b[:,i])
        for j in range(i+1):np.add.at(ab[i-j],base+j,H[:,i,j])
    # Prescribed zero values: delete the corresponding rows/columns exactly.
    for offset in range(4):
        starts=np.arange(dimension-offset)
        forbidden=fixed[starts]|fixed[starts+offset]
        ab[offset,starts[forbidden]]=0
    ab[0,fixed]=1;rhs[fixed]=0
    solution=solveh_banded(ab,rhs,lower=True,overwrite_ab=True,overwrite_b=True,check_finite=False)
    p,q=solution[0::2],solution[1::2]
    residual=error.copy()
    residual[:,0]+=2*np.diff(p)/h
    residual[:,1]+=omega*(p[:-1]+p[1:])/(2*a)+a*np.diff(q)/h
    residual[:,2]+=(ap/a)*(p[:-1]+p[1:])+omega*(q[:-1]+q[1:])
    return p,q,residual


def sample(prefix,tail,nprefix,ntail):
    locations=np.linspace(0,float(prefix.geom.x[-1]),nprefix+1,dtype=LD)
    s=[LD(0)];a=[];ap=[];errors=[];tags=[]
    for j in range(nprefix):
        mid=(locations[j]+locations[j+1])/2;point=prefix.point(mid)
        s.append(locations[j+1]);a.append(point['a']);ap.append(point['ap']);errors.append(point['errors'])
        tags.append(dict(region='prefix',native=float(mid)))
    if tail is not None:
        r=np.linspace(float(tail.reader.r[-1]),float(tail.cuff),ntail+1,dtype=LD)
        def point_at(value):
            if value<tail.reader.r[0]:
                return tail.point(-1,(value-tail.cuff)/tail.length)
            i=min(max(int(np.searchsorted(tail.reader.r,value,side='right')-1),0),len(tail.reader.L)-1)
            t=(value-tail.reader.r[i])/tail.reader.L[i]
            t=min(LD(1),max(LD(0),t))
            return tail.point(i,t)
        for j in range(ntail):
            left,right=r[j],r[j+1];mid=(left+right)/2
            first,middle,last=point_at(left),point_at(mid),point_at(right)
            length=(left-right)*(first['zeta']+4*middle['zeta']+last['zeta'])/6
            s.append(s[-1]+length);a.append(middle['a']);ap.append(middle['ap']);errors.append(middle['errors'])
            tags.append(dict(region=middle['region'],r=float(mid),span=middle['span'],tau=middle['tau']))
    return np.asarray(s,dtype=float),np.asarray(a),np.asarray(ap),np.asarray(errors),tags


def maxima(p,q,h,error,count):
    pm=(p[:-1]+p[1:])/2;qm=(q[:-1]+q[1:])/2
    omega=3j*np.arange(p.shape[1])
    names=dict(p=pm,q=qm,p_u=pm*omega,q_u=qm*omega,p_s=np.diff(p,axis=0)/h[:,None],
               q_s=np.diff(q,axis=0)/h[:,None])
    result={k:float(np.max(abs(fft.irfft(v,n=count,axis=-1,norm='forward')))) for k,v in names.items()}
    values=fft.irfft(error,n=count,axis=-1,norm='forward')
    op=screen.r105.symmetric_norm(values[:,0],values[:,1],values[:,2])
    result.update(metric=float(np.max(op)),E=float(np.max(abs(values[:,0]))),
                  F=float(np.max(abs(values[:,1]))),G=float(np.max(abs(values[:,2]))))
    return result,op


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--geometry',type=Path,required=True);ap.add_argument('--target',type=Path,required=True)
    ap.add_argument('--tail',type=Path);ap.add_argument('--tail-packet',type=Path)
    ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--angular',type=int,default=512);ap.add_argument('--psi-angular',type=int,default=2048)
    ap.add_argument('--prefix-cells',type=int,default=2048);ap.add_argument('--tail-cells',type=int,default=1024)
    ap.add_argument('--modes',type=int,default=192);ap.add_argument('--iterations',type=int,default=1)
    ap.add_argument('--fixed-cuff-width',type=float,default=.002)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError('Use a new report')
    if (args.tail is None)!=(args.tail_packet is None):raise ValueError('Provide both own tail and packet')
    if not 0<=args.modes<args.angular//2:raise ValueError('Fit modes must exclude Nyquist')
    started=time.monotonic();prefix=screen.Prefix(args.geometry,args.target,args.angular,args.psi_angular)
    tail=screen.Tail(args.tail,args.tail_packet,args.angular) if args.tail else None
    if tail and prefix.meta.get('tail_manifest_sha256')!=screen.r105.sha(args.tail):
        raise ValueError('Not this common prefix own tail')
    s,a,ar,original,tags=sample(prefix,tail,args.prefix_cells,args.tail_cells)
    h=np.diff(s);count=len(h)
    if np.any(h<=0):raise ValueError('Nonpositive approximate radial cell')
    original_coeff=fft.rfft(original,axis=-1,norm='forward')
    original_norm=screen.r105.symmetric_norm(original[:,0],original[:,1],original[:,2])
    del original
    fixed=np.zeros(2*(count+1),dtype=bool);fixed[0]=True
    terminal=s>=s[-1]-args.fixed_cuff_width
    fixed[2*np.nonzero(terminal)[0]]=True;fixed[2*np.nonzero(terminal)[0]+1]=True
    weights=np.ones(count);history=[]
    print(json.dumps(dict(stage='samples_ready',cells=count,seconds=time.monotonic()-started,
        original_sampled_metric_max=float(np.max(original_norm)),fitted_modes=args.modes)),flush=True)
    for iteration in range(args.iterations):
        p=np.zeros((count+1,original_coeff.shape[-1]),dtype=complex);q=p.copy();residual=original_coeff.copy()
        for n in range(args.modes+1):
            p[:,n],q[:,n],residual[:,:,n]=fit_mode(n,h,a,ar,original_coeff[:,:,n],weights,fixed)
        observed,op=maxima(p,q,h,residual,args.angular)
        worst=np.unravel_index(int(np.argmax(op)),op.shape)
        entry=dict(iteration=iteration+1,**observed,worst_cell=int(worst[0]),worst_angle_index=int(worst[1]),
            worst_location=tags[worst[0]],seconds=time.monotonic()-started)
        history.append(entry);print(json.dumps(entry),flush=True)
        # Radial reweighting keeps the Fourier systems decoupled. It is only
        # an experimental uniform-norm heuristic, not a minimax certificate.
        radial=op.max(axis=1);floor=max(float(np.median(radial)),1e-13)
        update=np.maximum(1,radial/floor)
        weights*=np.sqrt(update);weights/=np.mean(weights);weights=np.clip(weights,1e-4,1e4)
    p0=fft.irfft(p[0],n=args.angular,norm='forward');q0s=fft.irfft((q[1]-q[0])/h[0],n=args.angular,norm='forward')
    report=dict(schema='fd2d-noncircle-tangential-minimum-strain-screen-v1',status='SCREEN_ONLY__PIECEWISE_LINEAR_FIELD',
        scope=__doc__,script=screen.identity(__file__),metric_sampler=screen.identity(HERE/'fd2d-metric-noncircle-gauge-screen.py'),
        geometry=screen.identity(args.geometry),target=screen.identity(args.target),
        angular_samples=args.angular,psi_samples=args.psi_angular,prefix_cells=args.prefix_cells,
        tail_cells=args.tail_cells if tail else 0,fitted_modes=args.modes,iterations=history,
        sampled_original_metric_max=float(np.max(original_norm)),remaining_untreated_angular_modes=True,
        fixed_terminal_width=args.fixed_cuff_width,fixed_terminal_nodes=int(np.sum(terminal)),
        initial_p_sampled_absmax=float(np.max(abs(p0))),initial_q_s_sampled_absmax=float(np.max(abs(q0s))),
        mirror_second_jet_verified=False,terminal_values_exact_in_fitted_algebra=True,
        terminal_shared_two_jets_verified=False,field_C2=False,nonlinear_pullback_checked=False,
        exact_target_bridge_transfer_applied=False,continuous_certificate=False,metric_bound_certified=False,
        complete_closed_surface=False,solver_type='Complex Hermitian banded linear least squares; no nonlinear BVP',
        nonlinear_solver_calls=0,ODE_shooting_calls=0,seconds=time.monotonic()-started)
    if tail:report.update(tail=screen.identity(args.tail),tail_packet=screen.identity(args.tail_packet))
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(out=str(args.out),final=history[-1],continuous_certificate=False)),flush=True)


if __name__=='__main__':main()
