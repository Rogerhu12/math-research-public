#!/usr/bin/env python3
"""Two-end finite Frenet BVP with a fixed scalar profile and free core tail.

Only the chosen first K R225 core coefficients are retained. All K+1..M
support coefficients are unknowns. This defines a NEW core and metric and
is not a fixed-g refinement of the original R225 field. The terminal
condition is an axisymmetric WKB design, not an exact stable manifold.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import gzip
import hashlib
import importlib.util
import json
import time
from fractions import Fraction
from pathlib import Path
import numpy as np
from scipy.integrate import solve_bvp
import scipy.integrate._bvp as bvp_backend
from scipy.interpolate import interp1d

P = Path(__file__).resolve().parent


def module(name,file):
    spec = importlib.util.spec_from_file_location(name,P/file)
    ans = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ans)
    return ans


native = module('free_core_native','geometry_20261114_r225_high_core_bvp.py')
fixed = module('free_core_fixed','geometry_20261114_r225_fixed_profile.py')


class BatchedFFTFlow(native.BatchedFlow):
    """Same uniform-angle projection, with real/imaginary FFTs separated."""
    def synth_real(self,y):
        q=self.q; M=q.M; rows=y.shape[1]
        spec=np.zeros((rows,3,q.N//2+1),complex)
        spec[:,0,q.freq.astype(int)]=(q.N/2)*y[:M+1].T
        spec[:,0,0]*=2
        spec[:,1,q.freq[1:].astype(int)]=-1j*(q.N/2)*y[M+1:2*M+1].T
        spec[:,2,q.freq.astype(int)]=(q.N/2)*y[2*M+1:].T
        spec[:,2,0]*=2
        multiplier=1j*np.arange(q.N//2+1)
        values=np.fft.irfft(spec,n=q.N,axis=-1).transpose(0,2,1)
        first=np.fft.irfft(spec*multiplier,n=q.N,axis=-1).transpose(0,2,1)
        second=np.fft.irfft(spec*multiplier*multiplier,n=q.N,axis=-1).transpose(0,2,1)
        d=np.stack((first[...,0]-values[...,1],first[...,1]+values[...,0],first[...,2]),axis=-1)
        dd=np.stack((second[...,0]-2*first[...,1]-values[...,0],
                     second[...,1]+2*first[...,0]-values[...,1],second[...,2]),axis=-1)
        return d,dd

    def project_real(self,value):
        q=self.q; c=np.fft.rfft(value.transpose(0,2,1),n=q.N,axis=-1)
        rr=(2/q.N)*c[:,0,q.freq.astype(int)].real
        rr[:,0]*=.5
        tt=-(2/q.N)*c[:,1,q.freq[1:].astype(int)].imag
        zz=(2/q.N)*c[:,2,q.freq.astype(int)].real
        zz[:,0]*=.5
        return np.concatenate((rr,tt,zz),axis=1).T

    def __call__(self,x,y):
        self.calls+=1
        if np.iscomplexobj(y):
            dr,ddr=self.synth_real(y.real); di,ddi=self.synth_real(y.imag)
            d,dd=dr+1j*di,ddr+1j*ddi
        else:
            d,dd=self.synth_real(y)
        lam2=np.sum(d*d,axis=-1)
        tangent=d/np.sqrt(lam2)[...,None]
        normal_raw=dd-np.sum(dd*tangent,axis=-1)[...,None]*tangent
        nn=np.sqrt(np.sum(normal_raw*normal_raw,axis=-1))
        normal=normal_raw/nn[...,None]
        binormal=np.cross(tangent,normal)
        key=np.asarray(x,dtype=float).tobytes()
        if key not in self.profiles:
            self.profiles[key]=np.asarray([self.q.profile(float(s)) for s in x])
        prof=self.profiles[key]
        alpha=-prof[:,1,None]/(prof[:,0,None]*(nn/lam2))
        with np.errstate(invalid='ignore'):
            velocity=alpha[...,None]*normal+np.sqrt(1-alpha*alpha)[...,None]*binormal
        if np.iscomplexobj(velocity):
            return self.project_real(velocity.real)+1j*self.project_real(velocity.imag)
        return self.project_real(velocity)


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--profile',type=Path,required=True)
    p.add_argument('--seed',type=Path,required=True)
    p.add_argument('--turn-seed',type=Path)
    p.add_argument('--M',type=int,default=48)
    p.add_argument('--N',type=int,default=512)
    p.add_argument('--fixed-modes',type=int,default=3)
    p.add_argument('--end',type=float)
    p.add_argument('--base-step',type=float,default=.025)
    p.add_argument('--tol',type=float,default=1e-5)
    p.add_argument('--max-nodes',type=int,default=256)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    source_hash=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    profile_data=fixed.read(args.profile)
    scalar=fixed.FixedProfile(profile_data['geometry'])
    if scalar.exact_coefficient_sha256!=profile_data['exact_coefficient_sha256']:
        raise ValueError('Exact scalar profile identity differs')
    end=scalar.end if args.end is None else args.end
    seed=fixed.read(args.seed)
    oldM=seed['numerical_parameters']['M']
    if not 1<=args.fixed_modes<=32<=args.M<=oldM:
        raise ValueError('Require 1 <= fixed-modes <= 32 <= M <= seed M')
    ident=seed['metric_identity']; law=ident['law']
    c=np.array([float(Fraction(v)) for v in ident['coefficients_rational']])
    q=native.outward.FullCoreProbe(c,args.M,args.N,law['velocity'],law['length'],law['k0'])
    q.profile=scalar.profile
    fixed.fft.enable_fft(q)
    ss=list(seed['state_locations']); yy=list(seed['coefficient_states'])
    if args.turn_seed:
        turn=fixed.read(args.turn_seed)
        if turn['M']!=oldM:
            raise ValueError('Turn seed M differs')
        for s,y in zip(turn['state_locations'],turn['augmented_states']):
            if s>ss[-1]+1e-13:
                ss.append(s);yy.append(y[2:])
    if ss[-1]<end-1e-13:
        raise ValueError('Need actual initial-guess states through the requested end')
    ss=np.asarray(ss)
    yy=np.array([native.resize(y,oldM,args.M) for y in yy])
    interpolation=interp1d(ss,yy,axis=0,kind='linear')
    prefix=np.linspace(0,scalar.join,int(np.ceil(scalar.join/args.base_step))+1)
    mesh=np.unique(np.r_[prefix,scalar.x[scalar.x<=end],end])
    initial=interpolation(mesh)
    flow=BatchedFFTFlow(q)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    flow.checkpoint=args.out.with_name(args.out.name.removesuffix('.json.gz')+'-newton-checkpoint.json.gz')
    preflight_additions=[]
    for unused in range(10):
        f0=flow(mesh,initial.T)
        if not np.all(np.isfinite(f0)):
            raise FloatingPointError('Truncated initial-guess node has invalid point domain: '+str(mesh[np.any(~np.isfinite(f0),axis=0)].tolist()))
        h=np.diff(mesh); mids=(mesh[:-1]+mesh[1:])/2
        ymid=(initial[:-1]+initial[1:])/2-(h[:,None]/8)*(f0[:,1:]-f0[:,:-1]).T
        bad=np.any(~np.isfinite(flow(mids,ymid.T)),axis=0)
        if not np.any(bad):
            break
        added=mids[bad]
        preflight_additions.extend(added.tolist())
        if len(mesh)+len(added)>args.max_nodes:
            raise FloatingPointError('Initial midpoint domain needs more nodes')
        mesh=np.unique(np.r_[mesh,added]);initial=interpolation(mesh)
    else:
        raise FloatingPointError('Initial midpoint domain still invalid')
    cross_points=np.array([0,len(mesh)//2,len(mesh)-1])
    xx,ys=mesh[cross_points],initial[cross_points].T
    dense=native.BatchedFlow(q)
    real_difference=float(np.max(abs(flow(xx,ys)-dense(xx,ys))))
    perturb=np.zeros_like(ys);perturb[args.M//2]=1
    jac_difference=float(np.max(abs((flow(xx,ys+1j*1e-25*perturb)-dense(xx,ys+1j*1e-25*perturb)).imag/1e-25)))
    if real_difference>1e-12 or jac_difference>1e-10:
        raise ArithmeticError(f'FFT batch comparison differs: {real_difference}, {jac_difference}')
    M,K=args.M,args.fixed_modes; high=np.arange(K+1,M+1); frequency=q.freq[1:]
    a,v,app=q.profile(end)
    if app>=0:
        raise ValueError('WKB end must have negative scalar acceleration')
    beta=np.sqrt(1-v*v); A=-app/beta; B=(app+((2*high)**2-v*v)/a)/beta
    lam=(v/a+np.sqrt((v/a)**2+4*A*B))/2
    lz=B/lam; le=np.ones_like(lz); norm=np.hypot(lz,le);lz/=norm;le/=norm
    br=lz*v-le*beta;bz=lz*beta+le*v

    def bc(ya,yb):
        rho=ya[0]+((1-frequency**2)*ya[1:M+1])@q.C[1:]
        if float(rho.min())<=0:
            return np.full(q.n,np.nan)
        return np.r_[ya[0]-1,ya[1:K+1]-c[:K],
                     ya[M+1:2*M+1]+frequency*ya[1:M+1],ya[2*M+1:],
                     br*yb[high]+bz*yb[2*M+1+high]]

    def bc_jac(ya,yb):
        left=np.zeros((q.n,q.n));right=np.zeros_like(left)
        left[:K+1,:K+1]=np.eye(K+1)
        j=np.arange(M);left[K+1+j,1+j]=frequency;left[K+1+j,M+1+j]=1
        j=np.arange(M+1);left[K+1+M+j,2*M+1+j]=1
        j=np.arange(len(high));right[K+2*M+2+j,high]=br;right[K+2*M+2+j,2*M+1+high]=bz
        return left,right

    begin=time.time()
    print(json.dumps(dict(event='start',M=M,N=args.N,fixed_modes=K,nodes=len(mesh),end=end,
                          initial_boundary=float(np.max(abs(bc(initial[0],initial[-1])))),
                          fft_rhs_difference=real_difference,fft_directional_jacobian_difference=jac_difference)),flush=True)
    bvp_backend.solve_newton=native.domain_safe_newton
    sol=solve_bvp(flow,bc,mesh,initial.T,fun_jac=flow.jac,bc_jac=bc_jac,
                  tol=args.tol,bc_tol=1e-11,max_nodes=args.max_nodes,verbose=2)
    actual=sol.y[1:M+1,0]
    original=np.r_[c,np.zeros(M-len(c))]
    delta=actual-original
    q.coefficients=actual;q.rho0=1+((1-frequency**2)*actual)@q.C[1:]
    q.hmajor=1+float(actual.sum());q.hminor=1+float(np.sum((-1.)**np.arange(1,M+1)*actual))
    q.gap=q.hmajor-q.hminor;q.witness=np.array([0.,q.hmajor,0.])
    rows=[]
    for s,y in zip(sol.x,sol.y.T):
        try:rows.append(q.stats(float(s),y))
        except Exception as error:rows.append(dict(s=float(s),error=repr(error)))
    good=[r for r in rows if 'metric_sample'in r]
    result=dict(scope=__doc__,success=bool(sol.success),status=int(sol.status),message=sol.message,
                M=M,N=args.N,fixed_modes=K,end=end,seconds=time.time()-begin,
                source_sha256=source_hash,profile_sha256=hashlib.sha256(args.profile.read_bytes()).hexdigest(),
                fixed_scalar_profile=profile_data,
                original_metric_identity=ident,parameters={k:str(v)if isinstance(v,Path)else v for k,v in vars(args).items()},
                flow_calls=flow.calls,jacobian_calls=flow.jacobians,preflight_added_nodes=preflight_additions,
                fft_rhs_difference=real_difference,fft_directional_jacobian_difference=jac_difference,
                mesh=sol.x.tolist(),states=sol.y.T.tolist(),rhs=flow(sol.x,sol.y).T.tolist(),
                collocation_rms_max=float(np.max(sol.rms_residuals)),
                boundary_residual_max=float(np.max(abs(bc(sol.y[:,0],sol.y[:,-1])))),
                terminal=dict(kind='axisymmetric-wkb-design',modes=high.tolist(),r_weights=br.tolist(),z_weights=bz.tolist()),
                core=dict(coefficients=actual.tolist(),delta_from_R225=delta.tolist(),axis_support_gap=q.gap,
                          rho_sample_min=float(q.rho0.min()),rho_sample_max=float(q.rho0.max()),
                          support_C1_triangle_bound=float(np.sum((1+frequency)*abs(delta))),
                          rho_triangle_bound=float(np.sum((frequency**2-1)*abs(delta)))),
                rows=rows,summary=dict(valid_sample_rows=len(good),
                                       metric_sample=max((r['metric_sample']for r in good),default=None),
                                       kappa_sample=max((r['surface_kappa_sample']for r in good),default=None),
                                       reflected_prefix_D_sample=2*max((r['ball_radius_max']for r in good),default=0),
                                       smallest_point_domain=min((r['margin']for r in good),default=None),
                                       minimum_witness_distance=min((r['core_witness_sample_distance']for r in good),default=None)))
    encoded=(json.dumps(result,indent=2)+'\n').encode();args.out.write_bytes(gzip.compress(encoded,mtime=0))
    print(json.dumps({k:result[k]for k in ('success','status','message','seconds','collocation_rms_max','boundary_residual_max','core','summary')}),flush=True)


if __name__=='__main__':
    main()
