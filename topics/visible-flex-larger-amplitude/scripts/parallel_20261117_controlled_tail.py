#!/usr/bin/env python3
"""Complete finite tail BVP with M explicit scalar-metric design parameters.

The shallow P and nonconstant K traces are both imposed.  A shallow literal
mean row and M zero-height deep rows give 3M+1 boundary conditions for 2M+1
states and M scalar parameters.  Every logw correction has zero 0/1/2 jets
at its support endpoints.  This is new metric design, not fixed-g refinement
or an infinite-tail DN certificate.  A successful metric is frozen explicitly.
"""
import argparse
import copy
import gzip
import hashlib
import json
from pathlib import Path
import time

import numpy as np
from numpy.polynomial import Polynomial, Legendre
from scipy.integrate import solve_bvp
from scipy.interpolate import PPoly

from parallel_20261117_dynamic_tail import Background, DynamicMean
from parallel_20261117_continue import feasible_newton


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


class Controls:
    def __init__(self,definitions):
        self.definitions=definitions

    @classmethod
    def from_background(cls,bg,count,support_mode="cell"):
        cells=min(4,max(1,(count+1)//2));definitions=[]
        u=Polynomial([0.,1.])
        for j in range(count):
            cell=j%cells;degree=j//cells
            radial=[row['r'] for row in bg.rows if row['cell']==cell and (support_mode=='cell' or row['segment']==4)]
            lo=bg.data['bridge']['r1'] if cell==0 and support_mode=='cell' else min(radial)
            hi=max(radial)
            leg=Legendre.basis(degree).convert(kind=Polynomial)(2*u-1)
            poly=64*u**3*(1-u)**3*leg
            roots=poly.deriv().roots()
            points=[0.,1.]+[float(z.real) for z in roots if abs(z.imag)<1e-10 and 0<z.real<1]
            normalizer=1/max(abs(poly(np.array(points))))
            definitions.append(dict(cell=cell,support_mode=support_mode,degree=degree,lo=lo,hi=hi,
                                    normalizer=float(normalizer),polynomial=(normalizer*poly).coef.tolist()))
        return cls(definitions)

    def values(self,r,nu=0):
        r=np.atleast_1d(r);out=np.zeros((len(self.definitions),len(r)))
        for j,d in enumerate(self.definitions):
            mask=(r>d['lo'])&(r<d['hi']);u=(r[mask]-d['lo'])/(d['hi']-d['lo'])
            L=Legendre.basis(d['degree']);v=2*u-1
            f0=u**3*(1-u)**3;f1=3*u*u*(1-u)**2*(1-2*u)
            f2=6*u*(1-u)*(1-5*u+5*u*u)
            if nu==0:value=f0*L(v)
            elif nu==1:value=f1*L(v)+2*f0*L.deriv()(v)
            elif nu==2:value=f2*L(v)+4*f1*L.deriv()(v)+4*f0*L.deriv(2)(v)
            else:
                out[j,mask]=Polynomial(d['polynomial']).deriv(nu)(u)/(d['hi']-d['lo'])**nu
                continue
            out[j,mask]=64*d['normalizer']*value/(d['hi']-d['lo'])**nu
        return out


class AugmentedSpline:
    """Canonical factored C2 bumps, with a numerical PPoly evaluation cache."""
    def __init__(self,base,controls,parameters):
        self.base,self.controls,self.parameters=base,controls,np.array(parameters)
        self.x=base.x
        degree=max(3,max(len(d['polynomial'])-1 for d in controls.definitions))
        coefficients=np.zeros((degree+1,len(self.x)-1))
        coefficients[-4:]=base.c
        for i,left in enumerate(self.x[:-1]):
            mid=(left+self.x[i+1])/2
            for p,d in zip(self.parameters,controls.definitions):
                if d['lo']<mid<d['hi']:
                    local=Polynomial(d['polynomial'])(Polynomial([(left-d['lo'])/(d['hi']-d['lo']),1/(d['hi']-d['lo'])]))
                    coefficients[-len(local.coef):,i]+=p*local.coef[::-1]
        self.c=coefficients
        self.cache=PPoly(coefficients,self.x)

    def __call__(self,r,nu=0):
        scalar=np.ndim(r)==0;rr=np.atleast_1d(r)
        value=self.base(rr,nu)+self.parameters@self.controls.values(rr,nu)
        return value[0] if scalar else value


class FrozenControlBackground(Background):
    """Read the exact declared Hermite-plus-factored-polynomial metric."""
    def __init__(self,path,coordinate='source-index',depth=None):
        raw=path.read_bytes();definition=json.loads(raw)
        if definition.get('schema')!='parallel-frozen-logw-controls-v1':
            super().__init__(path,coordinate,depth);return
        if depth is not None:raise ValueError('Controlled background is already an explicitly fixed finite interval')
        class BytesPath:
            def read_bytes(self):return definition['base_background_raw'].encode()
        super().__init__(BytesPath(),coordinate)
        if self.sha256!=definition['base_background_sha256']:raise ValueError('Frozen base identity differs')
        self.spline=AugmentedSpline(self.spline,Controls(definition['controls']),definition['parameters'])
        self.logw=self.spline(self.r);self.derivative=self.spline(self.r,1)
        self.rows=copy.deepcopy(self.rows)
        for row,v,dv in zip(self.rows,self.logw,self.derivative):row.update(logw=float(v),dlogwdr=float(dv))
        self.data=copy.deepcopy(self.data);self.data['rows']=self.rows
        self.data['controlled_metric_definition']=definition
        self.raw=raw;self.sha256=digest(raw)


def main(a):
    started=time.perf_counter();source_sha=digest(Path(__file__).read_bytes())
    bg=Background(a.background,a.coordinate);trace_raw=a.trace.read_bytes();trace=json.loads(trace_raw)
    if bg.data.get('shallow_at')!='left':raise ValueError('Need an outward, left-shallow metric')
    q=DynamicMean(a.modes,a.angles);q.require_positive_height_slope=not a.allow_height_turn
    controls=Controls.from_background(bg,q.M,a.support_mode);targetp=a.scale*np.array(trace['P_sin_coefficients'][:q.M])
    targetk=a.scale*np.array(trace['K_cos_coefficients'][:q.M]);parameter=np.zeros(q.M)
    initial_sha=None
    if a.input:
        initial_raw=a.input.read_bytes();old=json.loads(gzip.decompress(initial_raw));initial_sha=digest(initial_raw)
        same_base=old['background_sha256']==bg.sha256 or old.get('base_background_sha256')==bg.sha256
        if not old['success'] or not same_base or old['coordinate']!=a.coordinate:raise ValueError('Seed must be accepted on this base or its explicitly controlled metric')
        x=np.array(old['mesh']);source=np.array(old['states']).T;keep=min(q.M,old['M']);y=np.zeros((q.n,len(x)))
        y[:keep]=source[:keep];y[q.M:q.M+keep]=source[old['M']:old['M']+keep];y[-1]=source[-1];y*=a.scale/old['scale']
        if old.get('base_background_sha256')==bg.sha256:
            if old['controls']!=controls.definitions:raise ValueError('Changed control basis requires a separately declared initialization')
            parameter=np.array(old['parameters'])
    else:
        x=bg.x;y=np.zeros((q.n,len(x)));y[:q.M]=targetp[:,None];y[q.M:2*q.M]=targetk[:,None]
    if a.parameters:parameter=np.array(json.loads(a.parameters))
    if len(parameter)!=q.M:raise ValueError('Need M scalar controls')
    dependencies={name:digest(Path(__file__).with_name(name).read_bytes()) for name in ['parallel_20261117_dynamic_tail.py','parallel_20261117_continue.py']}
    counts=dict(fun=0,jac=0)
    def metric(x,p):
        r,rx=bg.radial(x);B=controls.values(r);Br=controls.values(r,1)
        logw=bg.spline(r)+p@B;lr=bg.spline(r,1)+p@Br;w=np.exp(logw)
        return (rx/r,lr*rx,w*w),B,Br*rx,w,lr
    def fun(x,y,p):
        counts['fun']+=1;out=np.empty_like(y)
        if np.max(abs(p.real))>a.parameter_bound:return np.full_like(y,np.nan)
        for i in range(0,len(x),a.batch):
            sl=slice(i,i+a.batch);fields,B,Bx,w,lr=metric(x[sl],p)
            curvature=abs(w.real*lr.real)/(1+w.real*w.real)**1.5
            if np.any(curvature>a.reference_curvature_limit):out[:,sl]=np.nan;continue
            try:out[:,sl]=q.evaluate(y[:,sl],*fields)
            except FloatingPointError:out[:,sl]=np.nan
        return out
    def jac(x,y,p):
        counts['jac']+=1;A=np.empty((q.n,q.n,len(x)));B=np.empty((q.n,q.M,len(x)));h=1e-25
        for i in range(0,len(x),a.batch):
            sl=slice(i,i+a.batch);(s,ell,z),phi,phix,w,lr=metric(x[sl],p)
            A[:,:,sl]=q.jacobian(y[:,sl],s,ell,z)
            Fell=q.evaluate(y[:,sl],s,ell+1j*h,z).imag/h
            Fz=q.evaluate(y[:,sl],s,ell,z+1j*h).imag/h
            B[:,:,sl]=Fell[:,None,:]*phix[None,:,:]+Fz[:,None,:]*(2*z*phi)[None,:,:]
        return A,B
    left=bg.x[0]
    def bc(ya,yb,p):
        _,d=q.evaluate(ya[:,None],*bg(np.array([left])),True)
        return np.r_[(ya[:q.M]-targetp)/a.scale,(ya[q.M:2*q.M]-targetk)/a.scale,d['mean'][0],yb[:q.M]/a.scale]
    def bcjac(ya,yb,p):
        A=np.zeros((3*q.M+1,q.n));B=np.zeros_like(A);P=np.zeros((3*q.M+1,q.M));ii=np.arange(q.M)
        A[ii,ii]=1/a.scale;A[q.M+ii,q.M+ii]=1/a.scale;B[2*q.M+1+ii,ii]=1/a.scale;h=1e-25
        for j in range(q.n):
            v=ya.astype(complex);v[j]+=1j*h;A[2*q.M,j]=bc(v,yb,p)[2*q.M].imag/h
        return A,B,P
    import scipy.integrate._bvp as backend
    backend.solve_newton=feasible_newton
    print(json.dumps(dict(event='controlled_start',M=q.M,N=q.N,scale=a.scale,nodes=len(x),parameters=parameter.tolist(),parameter_bound=a.parameter_bound,reference_curvature_limit=a.reference_curvature_limit)),flush=True)
    sol=solve_bvp(fun,bc,x,y,p=parameter,fun_jac=jac,bc_jac=bcjac,tol=a.tol,bc_tol=1e-10,max_nodes=a.max_nodes,verbose=2)
    definition=dict(schema='parallel-frozen-logw-controls-v1',scope='New fixed metric: canonical original Hermite logw plus factored zero-2-jet polynomial bumps; expanded PPoly arrays are numerical evaluation caches only.',base_background_sha256=bg.sha256,base_background_raw=bg.raw.decode(),controls=controls.definitions,parameters=sol.p.tolist(),source_sha256=source_sha)
    metric_raw=(json.dumps(definition,separators=(',',':'))+'\n').encode();a.metric_out.write_bytes(metric_raw)
    newbg=FrozenControlBackground(a.metric_out,a.coordinate)
    audit=dict(max_mean=0.,min_D=float('inf'),min_S=float('inf'),min_L=float('inf'),min_y=float('inf'),min_N=float('inf'),max_P=0.,max_K=0.,max_reference_curvature=0.,max_full_P_radial_residual=0.,max_full_K_radial_residual=0.,sampled_branch_failure=False)
    for i in range(0,len(sol.x)-1,32):
        le=sol.x[i:min(i+32,len(sol.x)-1)];ri=sol.x[i+1:min(i+32,len(sol.x)-1)+1]
        xx=np.ravel(le[:,None]+(ri-le)[:,None]*np.linspace(0,1,5));yy=sol.sol(xx);yp=sol.sol(xx,1);r,rx=newbg.radial(xx);w=np.exp(newbg.spline(r));wr=w*newbg.spline(r,1)
        audit['max_reference_curvature']=max(audit['max_reference_curvature'],float(np.max(abs(wr)/(1+w*w)**1.5)))
        try:rhs,d=q.evaluate(yy,*newbg(xx),True)
        except FloatingPointError:audit['sampled_branch_failure']=True;continue
        audit['max_mean']=max(audit['max_mean'],float(np.max(abs(d['mean']))))
        for key in ('D','S','L','y','N'):audit['min_'+key]=min(audit['min_'+key],float(np.min(d[key])))
        for key in ('P','K'):audit['max_'+key]=max(audit['max_'+key],float(np.max(abs(d[key]))))
        rawp=q.S@rhs[:q.M]-d['pde_p_residual']
        audit['max_full_P_radial_residual']=max(audit['max_full_P_radial_residual'],float(np.max(abs((q.S@yp[:q.M]-rawp)/rx))))
        audit['max_full_K_radial_residual']=max(audit['max_full_K_radial_residual'],float(np.max(abs((q.C@yp[q.M:2*q.M]+yp[-1]-d['raw_k'])/rx))))
    report=dict(scope=__doc__,success=bool(sol.success),status=int(sol.status),message=sol.message,M=q.M,N=q.N,scale=a.scale,coordinate=a.coordinate,angular_chart='material theta',background_sha256=newbg.sha256,base_background_sha256=bg.sha256,background_file=str(a.metric_out),trace_sha256=digest(trace_raw),source_sha256=source_sha,dependency_sha256_at_start=dependencies,initial_input_sha256=initial_sha,parameters=sol.p.tolist(),controls=controls.definitions,parameter_bound=a.parameter_bound,reference_curvature_limit=a.reference_curvature_limit,deep_boundary_kind='finite zero nonmean height Dirichlet',allow_height_turn=a.allow_height_turn,height_mean_anchor=trace['height_mean'],seconds=time.perf_counter()-started,counts=counts,nodes=len(sol.x),collocation_rms_max=float(np.max(sol.rms_residuals)),boundary_residual_max=float(np.max(abs(bc(sol.y[:,0],sol.y[:,-1],sol.p)))),mesh=sol.x.tolist(),radial_mesh=newbg.radial(sol.x)[0].tolist(),states=sol.y.T.tolist(),rhs=fun(sol.x,sol.y,sol.p).T.tolist(),audit=audit)
    a.out.write_bytes(gzip.compress((json.dumps(report)+'\n').encode(),mtime=0))
    print(json.dumps({k:v for k,v in report.items() if k not in ('scope','mesh','radial_mesh','states','rhs','controls')}),flush=True)
    print(json.dumps(dict(output_sha256=digest(a.out.read_bytes()),metric_sha256=newbg.sha256)),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('background','trace','out','metric-out'):p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--input',type=Path);p.add_argument('--parameters');p.add_argument('--modes',type=int,default=2);p.add_argument('--angles',type=int,default=128)
    p.add_argument('--scale',type=float,default=1e-5);p.add_argument('--tol',type=float,default=1e-6);p.add_argument('--max-nodes',type=int,default=12000);p.add_argument('--batch',type=int,default=64)
    p.add_argument('--support-mode',choices=['cell','valley'],default='cell');p.add_argument('--parameter-bound',type=float,default=5.);p.add_argument('--reference-curvature-limit',type=float,default=7.)
    p.add_argument('--allow-height-turn',action='store_true');p.add_argument('--coordinate',choices=['source-index','physical-r'],default='source-index')
    main(p.parse_args())
