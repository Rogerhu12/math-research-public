#!/usr/bin/env python3
"""Direct analytic-Jacobian continuation from a genuine accepted prefix.

The original accepted prefix is a warm start, not a new result.  A constant
angular-curvature scalar extension is a NEW design metric.  The terminal
condition transports the principal matrix at the previous ACTUAL endpoint;
it does not claim a nonlinear tail Dirichlet-to-Neumann map or closedness.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import time
import numpy as np
from scipy.integrate import solve_bvp
from scipy.interpolate import CubicHermiteSpline
from parallel_20261117_frenet_symbol import Frenet


class Profile:
    def __init__(self, geometry, start, angular_curvature=None):
        self.geometry = geometry
        self.law = geometry['initial_law']
        self.knots = geometry['knots']
        self.x = np.array([k['s'] for k in self.knots])
        self.coeff = []
        jets = [tuple(Fraction(float(k[v])) for v in ('a','ap','app')) for k in self.knots]
        L, v, k = (Fraction(float(self.law[a])) for a in ('length','velocity','k0'))
        s = Fraction(float(self.x[0])); u=s/L; b=k*L; c=3*v-2*b; d=b-2*v
        jets[0] = (1+L*(b*u*u/2+c*u**3/3+d*u**4/4), b*u+c*u*u+d*u**3, (b+2*c*u+3*d*u*u)/L)
        for i in range(len(self.x)-1):
            h=Fraction(float(self.x[i+1]))-Fraction(float(self.x[i]))
            left,right=jets[i],jets[i+1]
            c0,c1,c2=left[0],h*left[1],h*h*left[2]/2
            aa=right[0]-c0-c1-c2;bb=h*right[1]-c1-2*c2;cc=h*h*right[2]-2*c2
            self.coeff.append(np.array([float(q) for q in (c0,c1,c2,10*aa-4*bb+cc/2,-15*aa+7*bb-cc,6*aa-3*bb+cc/2)]))
        self.start=start
        self.a0,self.v0,self.u0=self.old(start)
        self.angle0=np.arcsin(self.v0)
        self.K=-self.u0/np.sqrt(1-self.v0**2) if angular_curvature is None else angular_curvature
        if angular_curvature is not None and abs(self.u0+self.K*np.cos(self.angle0))>1e-10:
            raise ValueError('Requested extension must preserve the actual initial acceleration')

    def old(self,s):
        if s<=self.x[0]:
            L,v,k=(self.law[a] for a in ('length','velocity','k0'))
            if s>=L:
                return 1+L*v/2+k*L*L/12+v*(s-L),v,0.
            u=s/L;b=k*L;c=3*v-2*b;d=b-2*v
            return 1+L*(b*u*u/2+c*u**3/3+d*u**4/4),b*u+c*u*u+d*u**3,(b+2*c*u+3*d*u*u)/L
        i=min(len(self.x)-2,np.searchsorted(self.x,s,side='right')-1)
        h=self.x[i+1]-self.x[i];u=(s-self.x[i])/h;c=self.coeff[i]
        return (float(np.polynomial.polynomial.polyval(u,c)),
                float(np.polynomial.polynomial.polyval(u,np.arange(1,6)*c[1:])/h),
                float(np.polynomial.polynomial.polyval(u,np.arange(2,6)*np.arange(1,5)*c[2:])/(h*h)))

    def __call__(self,s):
        if s<=self.start:return self.old(s)
        angle=self.angle0-self.K*(s-self.start)
        return self.a0+(np.cos(angle)-np.cos(self.angle0))/self.K,np.sin(angle),-self.K*np.cos(angle)


def physical(q,y,profile,s):
    a,ap,app=profile(s);k=ap/a
    yp=q.rhs(y,k);J=q.jacobian(y,k)
    ypp=J@yp+q.jvp(y,k,np.zeros(q.n),dk=app/a-k*k)
    F,d,e=q.jet(y);V,dV,_=q.jet(yp);Acc,_,_=q.jet(ypp)
    nn=np.cross(V,d);area=np.linalg.norm(nn,axis=1);normal=nn/area[:,None]
    E=np.sum(V*V,axis=1);cross=np.sum(V*d,axis=1);G=np.sum(d*d,axis=1)
    II=np.sum(Acc*normal,axis=1);IIf=np.sum(dV*normal,axis=1);IIg=np.sum(e*normal,axis=1)
    det=II*IIg-IIf**2
    return dict(F=F,d=d,e=e,V=V,dV=dV,Acc=Acc,normal=normal,area=area,
                E=E,cross=cross,G=G,II=II,IIf=IIf,IIg=IIg,det=det,J=J,yp=yp,ypp=ypp,a=a,ap=ap,app=app)


def projector(q,y,profile,s,fixed):
    z=physical(q,y,profile,s)
    if np.min(z['det'])<=0 or np.min(abs(z['IIg']))<=0:
        raise ValueError('Actual endpoint has no strictly positive-Gauss principal projector')
    def normal_derivative(value):
        n=z['normal'];return (value-n*np.sum(n*value,axis=1)[:,None])/z['area'][:,None]
    ns=normal_derivative(np.cross(z['Acc'],z['d'])+np.cross(z['V'],z['dV']))
    nt=normal_derivative(np.cross(z['dV'],z['d'])+np.cross(z['V'],z['e']))
    rows=np.empty((q.M-fixed,q.n))
    for j in range(q.n):
        basis=np.zeros(q.n);basis[j]=1
        U,dU,_=q.jet(basis);Us,_,_=q.jet(z['J'][:,j])
        w=np.sum(U*z['normal'],axis=1)
        ws=np.sum(Us*z['normal']+U*ns,axis=1)
        wt=np.sum(dU*z['normal']+U*nt,axis=1)
        absD=np.fft.irfft(np.arange(q.N//2+1)*np.fft.rfft(w),n=q.N)
        value=ws-z['IIf']/z['IIg']*wt+np.sqrt(z['det'])/abs(z['IIg'])*absD
        rows[:,j]=(2/q.N)*np.fft.rfft(value).real[2*np.arange(fixed+1,q.M+1)]
    rows/=np.linalg.norm(rows,axis=1)[:,None]
    return rows,z


def main(args):
    raw=args.input.read_bytes();data=json.loads(gzip.decompress(raw))
    if not data.get('success'):raise ValueError('Input is not an accepted solution')
    q=Frenet(data['M'],data['N']);start=float(data['mesh'][-1]);end=start+args.duration
    profile=Profile(data['fixed_scalar_profile']['geometry'],start)
    y0=np.array(data['states'][-1]);L,z=projector(q,y0,profile,start,args.fixed_modes)
    reference=y0+args.duration*z['yp']+.5*args.duration**2*z['ypp']
    oldx=np.array(data['mesh']);oldy=np.array(data['states']).T;oldf=np.array(data['rhs']).T
    warm=CubicHermiteSpline(oldx,oldy,oldf,axis=1)
    x=np.r_[oldx,np.linspace(start,end,max(2,int(np.ceil(args.duration/args.step))+1))[1:]]
    y=np.empty((q.n,len(x)));inside=x<=start;y[:,inside]=warm(x[inside])
    t=x[~inside]-start;y[:,~inside]=y0[:,None]+z['yp'][:,None]*t+.5*z['ypp'][:,None]*t*t
    core=np.array(data['core']['coefficients']);K=args.fixed_modes
    nc=2*q.M+K+2
    BA=np.zeros((q.n,q.n));BB=np.zeros_like(BA)
    BA[0,0]=1
    for j in range(K):BA[1+j,1+j]=1
    row=1+K
    for j in range(q.M):BA[row+j,1+j]=q.freq[j+1];BA[row+j,q.M+1+j]=1
    row+=q.M
    BA[row:row+q.M+1,2*q.M+1:]=np.eye(q.M+1)
    BB[nc:]=L
    target=np.zeros(q.n);target[0]=1;target[1:1+K]=core[:K];target[nc:]=L@reference
    def bc(ya,yb):return BA@ya+BB@yb-target
    counts=dict(fun=0,jac=0)
    def fun(s,states):
        counts['fun']+=1;out=np.empty_like(states)
        for j,t in enumerate(s):
            a,ap,_=profile(float(t))
            try:out[:,j]=q.rhs(states[:,j],ap/a)
            except FloatingPointError:out[:,j]=np.nan
        return out
    def jac(s,states):
        counts['jac']+=1;begin=time.perf_counter();out=np.empty((q.n,q.n,len(s)))
        for j,t in enumerate(s):
            a,ap,_=profile(float(t));out[:,:,j]=q.jacobian(states[:,j],ap/a)
        print(json.dumps(dict(event='analytic_jacobian',count=counts['jac'],nodes=len(s),seconds=time.perf_counter()-begin)),flush=True)
        return out
    begin=time.perf_counter()
    print(json.dumps(dict(event='start',M=q.M,N=q.N,start=start,end=end,nodes=len(x),
                         projector='previous_actual_endpoint',principal_gauss_min=float(np.min(z['det']/(z['E']*z['G']-z['cross']**2))),
                         initial_boundary=float(np.max(abs(bc(y[:,0],y[:,-1])))))),flush=True)
    if args.linear_solver == 'separated-qr':
        # This existing backend changes only elimination/storage, keeping the
        # same complete collocation equations and separated endpoint rows.
        path=Path(__file__).resolve().parents[1]/'computations/geometry_20261114_separated_qr_bvp.py'
        spec=importlib.util.spec_from_file_location('parallel_existing_qr',path)
        qr=importlib.util.module_from_spec(spec);spec.loader.exec_module(qr)
        work=args.out.with_suffix('.qr-work')
        qr.enable(work,nc,chunk_size=32,checkpoint=str(args.out)+'.checkpoint.gz',M=q.M,N=q.N)
        import scipy.integrate._bvp as backend
        backend.splu=qr.factor
    sol=solve_bvp(fun,bc,x,y,fun_jac=jac,bc_jac=lambda ya,yb:(BA,BB),tol=args.tol,bc_tol=1e-11,max_nodes=args.max_nodes,verbose=2)
    core_new=sol.y[1:q.M+1,0]
    rho=1+np.cos(q.angle[:,None]*q.freq[None,1:])@((1-q.freq[1:]**2)*core_new)
    rows=[]
    for s in np.unique(np.r_[np.linspace(0,end,101),start,end]):
        yy=sol.sol(s);zz=physical(q,yy,profile,s)
        metric=max(np.max(abs(zz['E']-1)),np.max(abs(zz['cross'])/(zz['a']*rho)),np.max(abs(zz['G']/(zz['a']**2*rho**2)-1)))
        gram=zz['E']*zz['G']-zz['cross']**2
        trace=(zz['II']*zz['G']+zz['IIg']*zz['E']-2*zz['IIf']*zz['cross'])/gram
        gauss=zz['det']/gram
        curvature=np.max((abs(trace)+np.sqrt(np.maximum(0,trace*trace-4*gauss)))/2)
        rows.append(dict(s=float(s),metric=float(metric),curvature=float(curvature),gauss_min=float(gauss.min()),gauss_max=float(gauss.max()),
                         a=float(zz['a']),ap=float(zz['ap']),app=float(zz['app']),height_min=float(zz['F'][:,2].min()),height_max=float(zz['F'][:,2].max()),
                         radius_norm_max=float(np.linalg.norm(zz['F'],axis=1).max())))
    report=dict(scope=__doc__,success=bool(sol.success),status=int(sol.status),message=sol.message,M=q.M,N=q.N,
                start=start,end=end,seconds=time.perf_counter()-begin,counts=counts,
                input_sha256=hashlib.sha256(raw).hexdigest(),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                symbol_source_sha256=hashlib.sha256(Path(__file__).with_name('parallel_20261117_frenet_symbol.py').read_bytes()).hexdigest(),
                collocation_rms_max=float(np.max(sol.rms_residuals)),boundary_residual_max=float(np.max(abs(bc(sol.y[:,0],sol.y[:,-1])))),
                terminal_projector='previous actual endpoint principal normal matrix transported as constant coefficients',
                extension_scalar=dict(start=start,a0=profile.a0,v0=profile.v0,u0=profile.u0,angular_curvature=float(profile.K)),
                inherited_profile=data['fixed_scalar_profile'],mesh=sol.x.tolist(),states=sol.y.T.tolist(),rhs=fun(sol.x,sol.y).T.tolist(),
                core=dict(coefficients=core_new.tolist(),rho_min=float(rho.min()),axis_support_gap=float(2*np.sum(core_new[::2]))),rows=rows)
    args.out.write_bytes(gzip.compress((json.dumps(report)+'\n').encode(),mtime=0))
    summary={k:report[k] for k in ('success','status','message','start','end','seconds','counts','collocation_rms_max','boundary_residual_max','extension_scalar')}
    summary.update(max_sample_metric=max(r['metric'] for r in rows),max_sample_curvature=max(r['curvature'] for r in rows),
                   reflected_prefix_D_proxy=2*max(r['radius_norm_max'] for r in rows),core=report['core'],endpoint=rows[-1],output_sha256=hashlib.sha256(args.out.read_bytes()).hexdigest())
    print(json.dumps(summary),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True);p.add_argument('--duration',type=float,default=.006)
    p.add_argument('--step',type=float,default=.001);p.add_argument('--fixed-modes',type=int,default=3)
    p.add_argument('--tol',type=float,default=1e-6);p.add_argument('--max-nodes',type=int,default=800)
    p.add_argument('--linear-solver',choices=['separated-qr','direct-csc'],default='separated-qr')
    p.add_argument('--out',type=Path,required=True)
    main(p.parse_args())
