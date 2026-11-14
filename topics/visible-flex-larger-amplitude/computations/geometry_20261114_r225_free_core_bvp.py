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
import bisect
import gzip
import hashlib
import importlib.util
import json
import time
import resource
import gc
from concurrent.futures import ThreadPoolExecutor
from fractions import Fraction
from pathlib import Path
import numpy as np
from scipy.integrate import solve_bvp
import scipy.integrate._bvp as bvp_backend
from scipy.interpolate import interp1d,CubicHermiteSpline

P = Path(__file__).resolve().parent


def module(name,file):
    spec = importlib.util.spec_from_file_location(name,P/file)
    ans = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ans)
    return ans


native = module('free_core_native','geometry_20261114_r225_high_core_bvp.py')
fixed = module('free_core_fixed','geometry_20261114_r225_fixed_profile.py')
block_csc = module('free_core_block_csc','geometry_20261114_block_csc_bvp.py')
original_index_builder = bvp_backend.compute_jac_indices
original_splu=native.splu


def memory_status():
    result=dict(maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    for line in Path('/proc/self/status').read_text().splitlines():
        if line.startswith(('VmRSS:','VmHWM:')):
            key,value=line.split(':',1);result[key]=value.strip()
    return result


def traced_splu(matrix):
    begin=time.time()
    print(json.dumps(dict(event='factor_start',dimension=matrix.shape[0],**memory_status())),flush=True)
    factor=original_splu(matrix)
    print(json.dumps(dict(event='factor_end',seconds=time.time()-begin,**memory_status())),flush=True)
    return factor


def released_newton(n, m, h, col_fun, bc, jac, y, p, B, bvp_tol, bc_tol):
    """Original 16-backtrack Newton, releasing obsolete matrix storage.

    The equations, acceptance test, iteration counts and return contract are
    identical to native.domain_safe_newton. SuperLU owns its factors, so the
    input CSC matrix can be released immediately after factorization. A
    factor is released before, rather than after, constructing its successor.
    """
    tol_r=(2/3)*h*.05*bvp_tol
    col_res,ymid,f,fmid=col_fun(y,p)
    bc_res=bc(y[:,0],y[:,-1],p)
    residual=np.r_[col_res.ravel(order='F'),bc_res]
    njev=0;recompute=True;singular=False;lu=None;J=None
    for iteration in range(20):
        if not np.all(np.isfinite(residual)):
            print(json.dumps(dict(event='newton_invalid_current',iteration=iteration)),flush=True)
            return y,p,True
        if recompute:
            lu=None;J=None;gc.collect()
            print(json.dumps(dict(event='obsolete_factor_released',iteration=iteration,**memory_status())),flush=True)
            J=jac(y,p,ymid,f,fmid,bc_res)
            njev+=1
            try:
                lu=traced_splu(J)
            except RuntimeError:
                singular=True
                break
            J=None
            step=lu.solve(residual)
            cost=float(step@step)
        ys=step[:m*n].reshape((n,m),order='F');ps=step[m*n:]
        alpha=1.;accepted=False
        for trial in range(17):
            yn=y-alpha*ys;pn=p-alpha*ps
            if B is not None:
                yn[:,0]=B@yn[:,0]
            crn,ymn,fn,fmn=col_fun(yn,pn)
            bcn=bc(yn[:,0],yn[:,-1],pn)
            rn=np.r_[crn.ravel(order='F'),bcn]
            if np.all(np.isfinite(rn)):
                sn=lu.solve(rn);cn=float(sn@sn)
                if cn<(1-.4*alpha)*cost or (cn==0 and cost==0):
                    accepted=True
                    break
            alpha*=.5
        if not accepted:
            print(json.dumps(dict(event='newton_backtracking_failed',iteration=iteration,
                                  max_bc=float(np.max(abs(bc_res))),
                                  max_collocation=float(np.max(abs(col_res))))),flush=True)
            break
        y,p=yn,pn
        col_res,ymid,f,fmid,bc_res,residual=crn,ymn,fn,fmn,bcn,rn
        print(json.dumps(dict(event='newton',iteration=iteration,alpha=alpha,
                              max_bc=float(np.max(abs(bc_res))),
                              max_collocation=float(np.max(abs(col_res))))),flush=True)
        if np.all(abs(col_res)<tol_r*(1+abs(fmid))) and np.all(abs(bc_res)<bc_tol):
            break
        if njev>=8:
            break
        if alpha==1:
            step,cost,recompute=sn,cn,False
        else:
            recompute=True
    return y,p,singular


def finite_second_derivative(q,s,y):
    """Derivative of this projected finite ODE, including explicit profile s."""
    frame=q.frame(s,y)
    yp=q.project(frame['V']);h=1e-25
    state=q.project(q.frame(s,y.astype(complex)+1j*h*yp,strict=False)['V']).imag/h
    dalpha=-frame['app']/(frame['a']*frame['kap'])+frame['ap']**2/(frame['a']**2*frame['kap'])
    dbeta=-frame['al']*dalpha/frame['be']
    explicit=q.project(dalpha[:,None]*frame['N']+dbeta[:,None]*frame['B'])
    return yp,state+explicit


def compact_index_builder(n,m,k):
    """Exact same sparse indices; avoid redundant 64-to-32-bit COO copies."""
    rows,columns=original_index_builder(n,m,k)
    if n*m+k<2**31 and len(rows)<2**31:
        return rows.astype(np.int32),columns.astype(np.int32)
    return rows,columns


def merge_mesh(primary, extra):
    """Retain exact profile joins while coalescing roundoff duplicate nodes."""
    result=sorted(set(float(v) for v in primary))
    for value in extra:
        value=float(value);i=bisect.bisect_left(result,value)
        nearby=result[max(0,i-1):min(len(result),i+1)]
        if any(abs(value-other)<=8*np.spacing(max(1.,abs(value),abs(other))) for other in nearby):
            continue
        result.insert(i,value)
    return np.asarray(result)


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

    def jac(self,x,y):
        workers=getattr(self,'jac_workers',1)
        if workers==1:
            result=super().jac(x,y)
            print(json.dumps(dict(event='jacobian_memory',nodes=y.shape[1],**memory_status())),flush=True)
            return result
        self.jacobians+=1
        baseline=self(x,y)
        if self.checkpoint is not None and x[0]==0:
            snapshot=dict(scope='Unconverged Newton iterate; no solver success is implied.',
                          M=self.q.M,N=self.q.N,mesh=x.tolist(),states=y.T.tolist(),
                          rhs=baseline.T.tolist(),jacobian_call=self.jacobians)
            self.checkpoint.write_bytes(gzip.compress((json.dumps(snapshot)+'\n').encode(),mtime=0))
        n,m=y.shape;ans=np.empty((n,n,m));h=1e-25
        def column(j):
            yc=y.astype(complex);yc[j]+=1j*h
            ans[:,j]=self(x,yc).imag/h
        with ThreadPoolExecutor(max_workers=workers) as pool:
            list(pool.map(column,range(n)))
        print(json.dumps(dict(event='jacobian',count=self.jacobians,nodes=m,
                              workers=workers,seconds=time.time()-self.started,**memory_status())),flush=True)
        return ans


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--profile',type=Path,required=True)
    p.add_argument('--seed',type=Path,required=True)
    p.add_argument('--turn-seed',type=Path)
    p.add_argument('--warm',type=Path)
    p.add_argument('--M',type=int,default=48)
    p.add_argument('--N',type=int,default=512)
    p.add_argument('--fixed-modes',type=int,default=3)
    p.add_argument('--end',type=float)
    p.add_argument('--base-step',type=float,default=.025)
    p.add_argument('--extension-step',type=float,default=.001)
    p.add_argument('--seed-interpolation',choices=['linear','hermite'],default='linear')
    p.add_argument('--seed-predictor',choices=['homothetic','taylor2'],default='homothetic')
    p.add_argument('--terminal-reference',choices=['zero','seed'],default='zero')
    p.add_argument('--jac-workers',type=int,default=1)
    p.add_argument('--tol',type=float,default=1e-5)
    p.add_argument('--max-nodes',type=int,default=256)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--prepare-only',action='store_true',help='Save the actual starting mesh/field and diagnostics without evaluating any full Jacobian.')
    args=p.parse_args()
    source_hash=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    profile_hash=hashlib.sha256(args.profile.read_bytes()).hexdigest()
    seed_hash=hashlib.sha256(args.seed.read_bytes()).hexdigest()
    warm_hash=hashlib.sha256(args.warm.read_bytes()).hexdigest() if args.warm else None
    assembly_hash=hashlib.sha256((P/'geometry_20261114_block_csc_bvp.py').read_bytes()).hexdigest()
    profile_data=fixed.read(args.profile)
    scalar=fixed.FixedProfile(profile_data['geometry'])
    if scalar.exact_coefficient_sha256!=profile_data['exact_coefficient_sha256']:
        raise ValueError('Exact scalar profile identity differs')
    end=scalar.end if args.end is None else args.end
    if not 0<end<=scalar.end:
        raise ValueError('End must lie inside the fixed scalar profile')
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
    ss=np.asarray(ss)
    yy=np.array([native.resize(y,oldM,args.M) for y in yy])
    if args.seed_interpolation=='hermite':
        seed_rhs=np.array([q.fun(float(s),y) for s,y in zip(ss,yy)])
        interpolation=CubicHermiteSpline(ss,yy,seed_rhs,axis=0)
    else:
        interpolation=interp1d(ss,yy,axis=0,kind='linear')
    terminal_yp,terminal_ypp=finite_second_derivative(q,float(ss[-1]),yy[-1])
    def seed_at(points):
        points=np.asarray(points)
        guess=interpolation(np.minimum(points,ss[-1]))
        anchor=yy[-1].copy(); mean_index=2*args.M+1
        mean=anchor[mean_index];anchor[mean_index]=0
        olda=q.profile(float(ss[-1]))[0]
        for i in np.flatnonzero(points>ss[-1]):
            if args.seed_predictor=='taylor2':
                ds=float(points[i]-ss[-1])
                guess[i]=yy[-1]+ds*terminal_yp+.5*ds**2*terminal_ypp
                continue
            aa,vv,_=q.profile(float(points[i]))
            guess[i]=(aa/olda)*anchor
            guess[i,mean_index]=mean+(points[i]-ss[-1])*np.sqrt(1-vv*vv)
        return guess
    prefix=np.linspace(0,scalar.join,int(np.ceil(scalar.join/args.base_step))+1)
    extension=np.linspace(ss[-1],end,int(np.ceil((end-ss[-1])/args.extension_step))+1) if end>ss[-1] else []
    mesh=merge_mesh(np.r_[scalar.x[scalar.x<=end],end],np.r_[prefix,extension])
    warm=None
    if args.warm:
        warm=fixed.read(args.warm)
        if warm['M']!=args.M or warm['N']!=args.N:
            raise ValueError('Warm checkpoint frequency or angular grid differs')
        warm_mesh=np.array(warm['mesh'])
        warm_curve=CubicHermiteSpline(warm_mesh,np.array(warm['states']),np.array(warm['rhs']),axis=0)
        mesh=merge_mesh(warm_mesh[warm_mesh<=end],mesh)
    def initial_at(points):
        answer=seed_at(points)
        if warm is not None:
            mask=(points>=warm_mesh[0])&(points<=warm_mesh[-1])
            answer[mask]=warm_curve(points[mask])
        return answer
    initial=initial_at(mesh)
    flow=BatchedFFTFlow(q)
    flow.jac_workers=args.jac_workers
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
        mesh=np.unique(np.r_[mesh,added]);initial=initial_at(mesh)
    else:
        raise FloatingPointError('Initial midpoint domain still invalid')
    cross_points=np.array([0,len(mesh)//2,len(mesh)-1])
    xx,ys=mesh[cross_points],initial[cross_points].T
    dense=native.BatchedFlow(q)
    real_difference=float(np.max(abs(flow(xx,ys)-dense(xx,ys))))
    perturb=np.zeros_like(ys);perturb[args.M//2]=1
    dense_direction=dense(xx,ys+1j*1e-25*perturb).imag/1e-25
    fft_direction=flow(xx,ys+1j*1e-25*perturb).imag/1e-25
    jac_difference=float(np.max(abs(fft_direction-dense_direction)))
    jac_relative=jac_difference/max(1.,float(np.max(abs(dense_direction))))
    if real_difference>1e-11 or jac_relative>1e-11:
        raise ArithmeticError(f'FFT batch comparison differs: {real_difference}, {jac_difference}')
    M,K=args.M,args.fixed_modes; high=np.arange(K+1,M+1); frequency=q.freq[1:]
    a,v,app=q.profile(end)
    if app>=0:
        raise ValueError('WKB end must have negative scalar acceleration')
    beta=np.sqrt(1-v*v); A=-app/beta; B=(app+((2*high)**2-v*v)/a)/beta
    lam=(v/a+np.sqrt((v/a)**2+4*A*B))/2
    lz=B/lam; le=np.ones_like(lz); norm=np.hypot(lz,le);lz/=norm;le/=norm
    br=lz*v-le*beta;bz=lz*beta+le*v
    reference=seed_at(np.array([end]))[0]
    terminal_value=br*reference[high]+bz*reference[2*M+1+high] if args.terminal_reference=='seed' else np.zeros(len(high))

    def bc(ya,yb):
        rho=ya[0]+((1-frequency**2)*ya[1:M+1])@q.C[1:]
        if float(rho.min())<=0:
            return np.full(q.n,np.nan)
        return np.r_[ya[0]-1,ya[1:K+1]-c[:K],
                     ya[M+1:2*M+1]+frequency*ya[1:M+1],ya[2*M+1:],
                     br*yb[high]+bz*yb[2*M+1+high]-terminal_value]

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
    if args.prepare_only:
        fp=flow(mesh,initial.T)
        h=np.diff(mesh);ymid=(initial[:-1]+initial[1:])/2-(h[:,None]/8)*(fp[:,1:]-fp[:,:-1]).T
        fmid=flow((mesh[:-1]+mesh[1:])/2,ymid.T)
        residual=initial[1:]-initial[:-1]-(h[:,None]/6)*(fp[:,:-1]+fp[:,1:]+4*fmid).T
        rows=[q.stats(float(s),y) for s,y in zip(mesh,initial)]
        report=dict(scope='Prepared initial guess, not a solved BVP or a new isometric surface.',
                    M=M,N=args.N,mesh=mesh.tolist(),states=initial.tolist(),rhs=fp.T.tolist(),
                    parameters={k:str(v)if isinstance(v,Path)else v for k,v in vars(args).items()},
                    source_sha256=source_hash,assembly_source_sha256=assembly_hash,
                    seed_sha256=seed_hash,profile_sha256=profile_hash,
                    seed_reached_s=seed['reached_s'],end=end,
                    preflight_added_nodes=preflight_additions,
                    initial_boundary_max=float(np.max(abs(bc(initial[0],initial[-1])))),
                    initial_collocation_max=float(np.max(abs(residual))),
                    metric_sample=max(r['metric_sample']for r in rows),
                    kappa_sample=max(r['surface_kappa_sample']for r in rows),
                    point_domain_min=min(r['margin']for r in rows),
                    terminal=rows[-1],rows=rows,**memory_status())
        args.out.write_bytes(gzip.compress((json.dumps(report)+'\n').encode(),mtime=0))
        print(json.dumps({k:report[k]for k in ('scope','end','initial_boundary_max','initial_collocation_max','metric_sample','kappa_sample','point_domain_min','maximum_RSS_kib')}),flush=True)
        return
    bvp_backend.solve_newton=released_newton
    bvp_backend.compute_jac_indices=compact_index_builder
    native.splu=traced_splu
    block_csc.enable()
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
                sparse_index_policy='Direct sorted block CSC, bitwise equivalent to native Jacobian; exact int32 indices when all dimensions and entries fit, otherwise int64.',
                seed_status=seed['status'],seed_reached_s=seed['reached_s'],
                seed_sha256=seed_hash,warm_sha256=warm_hash,
                source_sha256=source_hash,assembly_source_sha256=assembly_hash,profile_sha256=profile_hash,
                fixed_scalar_profile=profile_data,
                original_metric_identity=ident,parameters={k:str(v)if isinstance(v,Path)else v for k,v in vars(args).items()},
                flow_calls=flow.calls,jacobian_calls=flow.jacobians,preflight_added_nodes=preflight_additions,
                fft_rhs_difference=real_difference,fft_directional_jacobian_difference=jac_difference,
                fft_directional_jacobian_relative_difference=jac_relative,
                solved_metric_definition=dict(core_coefficients_binary64_exact_rational=[str(Fraction(float(v)))for v in actual],
                                               scalar_initial_law=profile_data['geometry']['initial_law'],
                                               scalar_profile_knots=profile_data['geometry']['knots'],
                                               material_coordinate='Normal angle phi, d(arc length)=rho0(phi)dphi, constant support term exactly 1.'),
                mesh=sol.x.tolist(),states=sol.y.T.tolist(),rhs=flow(sol.x,sol.y).T.tolist(),
                collocation_rms_max=float(np.max(sol.rms_residuals)) if np.all(np.isfinite(sol.rms_residuals)) else None,
                boundary_residual_max=float(np.max(abs(bc(sol.y[:,0],sol.y[:,-1])))),
                terminal=dict(kind='axisymmetric-wkb-design',reference=args.terminal_reference,
                              values=terminal_value.tolist(),modes=high.tolist(),r_weights=br.tolist(),z_weights=bz.tolist()),
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
