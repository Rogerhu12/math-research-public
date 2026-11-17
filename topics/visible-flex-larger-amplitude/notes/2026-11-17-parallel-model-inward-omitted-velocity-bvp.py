#!/usr/bin/env python3
"""A new finite inward BVP: suppress the first M-K omitted V_z cosines.

Retains all 3M+2 Frenet ODEs and the 2M+K+2 original core conditions.
The right conditions are nonlinear coefficients of UNPROJECTED velocity,
j=M+1,...,2M-K, not a principal projector or an infinite tail DN map.
Only duration zero is implemented: the accepted parent is a warm start for
this different boundary problem on the same stored inward scalar metric.
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np
from scipy.integrate import solve_bvp

SCRIPTS=Path(__file__).resolve().parents[1]/'scripts'
sys.path.insert(0,str(SCRIPTS))
import parallel_20261117_continue as frozen
from parallel_20261117_frenet_symbol import Frenet
from parallel_20261117_inward_profile import InwardProfile


class OmittedVelocityBoundary:
    def __init__(self,q,k,fixed=3):
        self.q=q;self.k=float(k);self.fixed=int(fixed)
        self.modes=np.arange(q.M+1,2*q.M-fixed+1)
        self.frequency=2*self.modes
        if self.frequency[-1]>=q.N//2:
            raise ValueError('Omitted frequencies must stay strictly below Nyquist')
        self.plus=(self.frequency[:,None]-q.freq[None,:])%q.N
        self.minus=(self.frequency[:,None]+q.freq[None,:])%q.N

    def coefficient(self,value):
        # Extend the real FFT cosine functional complex-linearly. Applying
        # real(...) to a complex-step spectrum would destroy its derivative.
        real=(2/self.q.N)*np.fft.rfft(np.real(value)).real[self.frequency]
        if np.iscomplexobj(value):
            imag=(2/self.q.N)*np.fft.rfft(np.imag(value)).real[self.frequency]
            return real+1j*imag
        return real

    def value(self,state):
        return self.coefficient(self.q.local(state,self.k)['V'][:,2])

    def jacobian(self,state):
        """Exact derivative of the same finite FFT functional by convolution."""
        q=self.q;local=q.local(state,self.k);zero=np.zeros((q.N,3))
        dd=np.empty((q.N,3));de=np.empty_like(dd)
        for component in range(3):
            unit=zero.copy();unit[:,component]=1
            dd[:,component]=q.variation(local,unit,zero)[:,2]
            de[:,component]=q.variation(local,zero,unit)[:,2]
        dh=np.fft.fft(dd,axis=0)/q.N;eh=np.fft.fft(de,axis=0)/q.N
        plus=(np.einsum('omk,mkc->omc',dh[self.plus],q.Dp)
              +np.einsum('omk,mkc->omc',eh[self.plus],q.D2p))
        minus=(np.einsum('omk,mkc->omc',dh[self.minus],q.Dm)
               +np.einsum('omk,mkc->omc',eh[self.minus],q.D2m))
        cosine=(plus+minus)/2;sine=(-1j*plus+1j*minus)/2
        return np.hstack((2*cosine[:,:,0].real,
                          2*sine[:,1:,1].real,
                          2*cosine[:,:,2].real))

    def probe(self,state):
        begin=time.perf_counter();raw=self.value(state);jac=self.jacobian(state)
        singular=np.linalg.svd(jac,compute_uv=False)
        norm=np.linalg.norm(jac,axis=1)
        normalized=np.linalg.svd(jac/norm[:,None],compute_uv=False)
        rng=np.random.default_rng(20261117);checks=[]
        for index in range(5):
            direction=rng.normal(size=self.q.n);direction/=np.linalg.norm(direction)
            step=1e-28
            exact=np.imag(self.value(state.astype(complex)+1j*step*direction))/step
            analytic=jac@direction;error=float(np.max(abs(analytic-exact)))
            checks.append(dict(index=index,step=step,max_abs_error=error,
                max_abs_derivative=float(np.max(abs(exact))),
                relative_inf_error=error/max(float(np.max(abs(exact))),1e-300)))
        threshold=max(jac.shape)*np.finfo(float).eps*singular[0]
        return dict(rows=len(self.modes),columns=self.q.n,
                    raw_coefficient_max=float(np.max(abs(raw))),
                    raw_coefficients=raw.tolist(),
                    singular_max=float(singular[0]),singular_min=float(singular[-1]),
                    numerical_rank=int(np.sum(singular>threshold)),
                    rank_threshold=float(threshold),
                    condition=float(singular[0]/singular[-1]),
                    row_norm_min=float(norm.min()),row_norm_max=float(norm.max()),
                    row_normalized_condition=float(normalized[0]/normalized[-1]),
                    directional_checks=checks,seconds=time.perf_counter()-begin)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main(args):
    raw=args.input.read_bytes();data=json.loads(gzip.decompress(raw))
    if not data.get('success'):raise ValueError('Accepted inward parent required')
    prior=data.get('inward_scalar_profile')
    if not prior:raise ValueError('Missing inward scalar profile')
    profile_source=SCRIPTS/'parallel_20261117_inward_profile.py'
    if data.get('inward_profile_sha256')!=sha(profile_source):
        raise ValueError('Stored inward profile source does not match')
    if args.fixed_modes!=3:
        raise ValueError('This experiment fixes precisely the first three core modes')
    q=Frenet(data['M'],args.angles or data['N'])
    inherited=data['fixed_scalar_profile'];origin=data['analytic_extension_origin']
    profile=InwardProfile(inherited['geometry'],origin,prior['cut'],
        prior['curvature'],prior['ramp_in'],prior['ramp_out'],prior['quadrature'])
    endpoint=float(data['mesh'][-1]);a,ap,_=profile(endpoint)
    right=OmittedVelocityBoundary(q,ap/a,args.fixed_modes)
    x=np.asarray(data['mesh']);y=np.asarray(data['states']).T.copy()
    initial_probe=right.probe(y[:,-1])
    if initial_probe['numerical_rank']!=q.M-args.fixed_modes:
        raise ValueError('Omitted boundary Jacobian does not have full row rank')
    if max(v['relative_inf_error'] for v in initial_probe['directional_checks'])>1e-9:
        raise ValueError('Omitted boundary Jacobian failed directional checks')
    nc=2*q.M+args.fixed_modes+2
    left=np.zeros((q.n,q.n));left[0,0]=1
    for j in range(args.fixed_modes):left[1+j,1+j]=1
    row=1+args.fixed_modes
    for j in range(q.M):
        left[row+j,1+j]=q.freq[j+1];left[row+j,q.M+1+j]=1
    row+=q.M;left[row:row+q.M+1,2*q.M+1:]=np.eye(q.M+1)
    target=np.zeros(q.n);target[0]=1
    target[1:1+args.fixed_modes]=np.asarray(data['core']['coefficients'])[:args.fixed_modes]
    def bc(ya,yb):
        result=left@ya-target
        try:result[nc:]=right.value(yb)
        except FloatingPointError:result[nc:]=np.nan
        return result
    def bc_jac(ya,yb):
        rb=np.zeros_like(left);rb[nc:]=right.jacobian(yb)
        return left,rb
    definition=dict(type='nonlinear_omitted_unprojected_velocity_z_cosines',
        M=q.M,N=q.N,fixed_modes=args.fixed_modes,first_mode=int(right.modes[0]),
        last_mode=int(right.modes[-1]),angular_frequencies=right.frequency.tolist(),
        raw_target=0.,normalization='none; literal raw cosine coefficients',
        endpoint=endpoint,all_ode_components=q.n,left_rows=nc,right_rows=q.M-args.fixed_modes,
        infinite_DN_claim=False,duration=0.)
    manifest={p.name:sha(p) for p in [Path(__file__),profile_source,
        SCRIPTS/'parallel_20261117_frenet_symbol.py',
        SCRIPTS/'parallel_20261117_continue.py',
        SCRIPTS/'parallel_20261117_profile.py']}
    metadata=dict(scope=__doc__,input_sha256=hashlib.sha256(raw).hexdigest(),
        source_sha256=sha(__file__),sources=manifest,terminal_boundary=definition,
        inward_scalar_profile=prior,inward_profile_sha256=sha(profile_source),
        initial_probe=initial_probe,tolerance=args.tol,bc_tolerance=args.bc_tol,
        max_nodes=args.max_nodes)
    args.out.with_suffix('.definition.json').write_text(json.dumps(metadata,indent=2)+'\n')
    print(json.dumps(dict(event='new_omitted_velocity_boundary_probe',**initial_probe)),flush=True)
    if args.probe_only:
        args.out.write_text(json.dumps(metadata,indent=2)+'\n')
        return
    counts=dict(fun=0,jac=0)
    def fun(s,states):
        counts['fun']+=1;out=np.empty_like(states)
        for j,t in enumerate(s):
            aa,av,_=profile(float(t))
            try:out[:,j]=q.rhs(states[:,j],av/aa)
            except FloatingPointError:out[:,j]=np.nan
        return out
    def jac(s,states):
        counts['jac']+=1;begin=time.perf_counter()
        out=np.empty((q.n,q.n,len(s)))
        for j,t in enumerate(s):
            aa,av,_=profile(float(t));out[:,:,j]=q.jacobian(states[:,j],av/aa)
        print(json.dumps(dict(event='complete_analytic_jacobian',count=counts['jac'],
            nodes=len(s),seconds=time.perf_counter()-begin)),flush=True)
        return out
    import scipy.integrate._bvp as backend
    if args.linear_solver=='separated-qr':
        path=Path(__file__).resolve().parents[1]/'computations/geometry_20261114_separated_qr_bvp.py'
        spec=importlib.util.spec_from_file_location('omitted_existing_qr',path)
        qr=importlib.util.module_from_spec(spec);spec.loader.exec_module(qr)
        qr.enable(args.out.with_suffix('.qr-work'),nc,chunk_size=32,
                  checkpoint=str(args.out)+'.checkpoint.gz',M=q.M,N=q.N)
        backend.splu=qr.factor
        metadata['sources'][path.name]=sha(path)
    backend.solve_newton=frozen.feasible_newton
    begin=time.perf_counter()
    print(json.dumps(dict(event='new_finite_bvp_start',M=q.M,N=q.N,nodes=len(x),
        endpoint=endpoint,all_ode_components=q.n,left_rows=nc,right_rows=q.M-args.fixed_modes,
        initial_raw_boundary=float(np.max(abs(bc(y[:,0],y[:,-1])))))),flush=True)
    sol=solve_bvp(fun,bc,x,y,fun_jac=jac,bc_jac=bc_jac,tol=args.tol,
                  bc_tol=args.bc_tol,max_nodes=args.max_nodes,verbose=2)
    core=sol.y[1:q.M+1,0]
    rho=1+np.cos(q.angle[:,None]*q.freq[None,1:])@((1-q.freq[1:]**2)*core)
    raw_right=right.value(sol.y[:,-1]);all_bc=bc(sol.y[:,0],sol.y[:,-1])
    report=dict(**metadata,success=bool(sol.success),status=int(sol.status),
        message=sol.message,M=q.M,N=q.N,start=endpoint,end=endpoint,duration=0.,
        seconds=time.perf_counter()-begin,counts=counts,
        collocation_rms_max=float(np.max(sol.rms_residuals)),
        boundary_residual_max=float(np.max(abs(all_bc))),
        right_raw_coefficients=raw_right.tolist(),right_raw_coefficient_max=float(np.max(abs(raw_right))),
        terminal_projector='none: a new nonlinear finite omitted-velocity condition',
        symbol_source_sha256=sha(SCRIPTS/'parallel_20261117_frenet_symbol.py'),
        profile_source_sha256=sha(SCRIPTS/'parallel_20261117_profile.py'),
        fixed_scalar_profile=inherited,analytic_extension_origin=origin,
        metric_reader_requirement='Use inward_scalar_profile with the frozen prefix_inward_readout.py',
        fixed_modes=args.fixed_modes,core_fixed_targets=target[1:1+args.fixed_modes].tolist(),
        mesh=sol.x.tolist(),states=sol.y.T.tolist(),rhs=fun(sol.x,sol.y).T.tolist(),
        core=dict(coefficients=core.tolist(),rho_min=float(rho.min()),
                  axis_support_gap=float(2*np.sum(core[::2]))))
    args.out.write_bytes(gzip.compress((json.dumps(report)+'\n').encode(),mtime=0))
    print(json.dumps({key:report[key] for key in ['success','status','message','seconds',
        'collocation_rms_max','boundary_residual_max','right_raw_coefficient_max','core']}),flush=True)
    print(json.dumps(dict(event='new_finite_bvp_saved',output_sha256=sha(args.out))),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--angles',type=int);p.add_argument('--fixed-modes',type=int,default=3)
    p.add_argument('--tol',type=float,default=1e-8);p.add_argument('--bc-tol',type=float,default=1e-11)
    p.add_argument('--max-nodes',type=int,default=1800);p.add_argument('--probe-only',action='store_true')
    p.add_argument('--linear-solver',choices=['separated-qr','direct-csc'],default='separated-qr')
    main(p.parse_args())
