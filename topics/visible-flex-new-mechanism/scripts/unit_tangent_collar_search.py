#!/usr/bin/env python3
"""Parallel eccentric collars using a unit angular tangent and its primitive.

The angular closure residual is retained explicitly. The metric is designed
unless --fixed-radius is set; finite residuals are never exact-isometry claims.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from eccentric_collar_search import Meridian, TrialSpace, fourier, smoothstep


def primitive(v):
    """Zero-mean Fourier primitive on the uniform angular grid, axis 1."""
    n = v.shape[1]
    k = np.fft.fftfreq(n, d=1/n)
    multipliers = np.zeros(n, complex)
    mask = k != 0
    multipliers[mask] = 1/(1j*k[mask])
    if n % 2 == 0:
        multipliers[n//2] = 0
    shape = (1,n)+tuple(1 for _ in range(v.ndim-2))
    return np.fft.ifft(np.fft.fft(v, axis=1)*multipliers.reshape(shape), axis=1).real


class UnitTangentSpace:
    def __init__(self, args):
        self.args = args
        self.meridian = Meridian(args.radius,args.length,args.collar,args.beta_wiggle,args.quadrature)
        self.radial = TrialSpace(self.meridian,args.controls,args.modes,args.offset,0.)
        self.j, self.k = args.controls-6, 2*args.modes+1
        self.nangle = self.j*self.k
        self.size = 2*self.nangle + 3*self.j + (0 if args.fixed_radius else self.j)

    def prepare(self,s,n):
        s=np.asarray(s)
        u=np.arange(n)*2*np.pi/n
        aa,zz,ap,zp,app,zpp=self.meridian.evaluate(s)
        h,hp,hpp=smoothstep((s-self.meridian.start)/(self.meridian.end-self.meridian.start))
        width=self.meridian.end-self.meridian.start
        c=np.column_stack((self.args.offset*h,np.zeros_like(s),zz))
        cp=np.column_stack((self.args.offset*hp/width,np.zeros_like(s),zp))
        cpp=np.column_stack((self.args.offset*hpp/width**2,np.zeros_like(s),zpp))
        return {"s":s,"u":u,"radial":self.radial.radial_basis(s),
                "fourier":fourier(u,self.args.modes),
                "a":aa,"ap":ap,"app":app,"c":c,"cp":cp,"cpp":cpp}

    def unpack(self,q):
        count=self.nangle
        d=q[:count].reshape(self.j,self.k)
        p=q[count:2*count].reshape(self.j,self.k)
        c=q[2*count:2*count+3*self.j].reshape(self.j,3)
        a=np.zeros(self.j) if self.args.fixed_radius else q[2*count+3*self.j:]
        return d,p,c,a

    def geometry(self,q,grid,second=False):
        d,p,cc,ar=self.unpack(np.asarray(q))
        r0,r1,r2=grid['radial']
        f0,f1,f2=grid['fourier']
        theta=grid['u'][None,:]+r0@d@f0.T
        phi=r0@p@f0.T
        ds,ps=r1@d@f0.T,r1@p@f0.T
        st,ct,sp,cp=np.sin(theta),np.cos(theta),np.sin(phi),np.cos(phi)
        zero=np.zeros_like(theta)
        t=np.stack((-st*cp,ct*cp,sp),axis=-1)
        td=np.stack((-ct*cp,-st*cp,zero),axis=-1)
        tp=np.stack((st*sp,-ct*sp,cp),axis=-1)
        tdd=np.stack((st*cp,-ct*cp,zero),axis=-1)
        tdp=np.stack((ct*sp,st*sp,zero),axis=-1)
        ts=td*ds[:,:,None]+tp*ps[:,:,None]
        gamma,gammas=primitive(t),primitive(ts)
        a,ap,app=(grid['a']+r0@ar,grid['ap']+r1@ar,grid['app']+r2@ar)
        c,cs=grid['c']+r0@cc,grid['cp']+r1@cc
        mean=t.mean(axis=1,keepdims=True)
        ss=t-mean
        x=c[:,None,:]+a[:,None,None]*gamma
        xs=cs[:,None,:]+ap[:,None,None]*gamma+a[:,None,None]*gammas
        xu=a[:,None,None]*ss
        out=dict(t=t,td=td,tp=tp,tdd=tdd,tdp=tdp,ts=ts,ds=ds,ps=ps,
                 gamma=gamma,gammas=gammas,a=a,ap=ap,mean=mean,ss=ss,x=x,xs=xs,xu=xu)
        if second:
            dss,pss=r2@d@f0.T,r2@p@f0.T
            tss=(td*dss[:,:,None]+tp*pss[:,:,None]+tdd*(ds*ds)[:,:,None]
                 +2*tdp*(ds*ps)[:,:,None]-t*(ps*ps)[:,:,None])
            tu=td*(1+r0@d@f1.T)[:,:,None]+tp*(r0@p@f1.T)[:,:,None]
            xss=(grid['cpp']+r2@cc)[:,None,:]+app[:,None,None]*gamma
            xss+=2*ap[:,None,None]*gammas+a[:,None,None]*primitive(tss)
            xsu=ap[:,None,None]*ss+a[:,None,None]*(ts-ts.mean(axis=1,keepdims=True))
            out.update(xss=xss,xsu=xsu,xuu=a[:,None,None]*tu)
        return out

    def residual(self,q,grid):
        z=self.geometry(q,grid)
        e=np.sum(z['xs']**2,axis=-1)-1
        f=np.sqrt(2)*np.sum(z['xs']*z['ss'],axis=-1)
        close=self.args.closure_weight*np.sqrt(len(grid['u']))*z['mean'][:,0,:]
        lo=self.args.radius_floor*grid['a']
        hi=self.args.radius_ceiling*grid['a']
        bounds=self.args.radius_weight*np.sqrt(len(grid['u']))*np.stack(
            (np.maximum(lo-z['a'],0),np.maximum(z['a']-hi,0)),axis=-1)
        return np.r_[np.stack((e,f),axis=-1).ravel(),close.ravel(),bounds.ravel()]

    def jacobian(self,q,grid):
        z=self.geometry(q,grid)
        r0,r1,_=grid['radial']
        f0=grid['fourier'][0]
        b=(r0[:,None,:,None]*f0[None,:,None,:]).reshape(len(r0),len(f0),-1)
        bs=(r1[:,None,:,None]*f0[None,:,None,:]).reshape(len(r0),len(f0),-1)
        d_t=np.concatenate((z['td'][:,:,None,:]*b[:,:,:,None],
                            z['tp'][:,:,None,:]*b[:,:,:,None]),axis=2)
        d_ds=z['tdd']*z['ds'][:,:,None]+z['tdp']*z['ps'][:,:,None]
        d_ps=z['tdp']*z['ds'][:,:,None]-z['t']*z['ps'][:,:,None]
        d_ts=np.concatenate((d_ds[:,:,None,:]*b[:,:,:,None]+z['td'][:,:,None,:]*bs[:,:,:,None],
                             d_ps[:,:,None,:]*b[:,:,:,None]+z['tp'][:,:,None,:]*bs[:,:,:,None]),axis=2)
        dxs=z['ap'][:,None,None,None]*primitive(d_t)+z['a'][:,None,None,None]*primitive(d_ts)
        dmean=d_t.mean(axis=1,keepdims=True)
        dss=d_t-dmean
        core=np.zeros((len(r0),len(f0),2,self.size))
        na=2*self.nangle
        core[:,:,0,:na]=2*np.einsum('ruc,rupc->rup',z['xs'],dxs)
        core[:,:,1,:na]=np.sqrt(2)*(np.einsum('ruc,rupc->rup',z['ss'],dxs)
                                   +np.einsum('ruc,rupc->rup',z['xs'],dss))
        center0=na
        for c in range(3):
            core[:,:,0,center0+c:center0+3*self.j:3]=2*z['xs'][:,:,c,None]*r1[:,None,:]
            core[:,:,1,center0+c:center0+3*self.j:3]=np.sqrt(2)*z['ss'][:,:,c,None]*r1[:,None,:]
        if not self.args.fixed_radius:
            drxs=r1[:,None,:,None]*z['gamma'][:,:,None,:]+r0[:,None,:,None]*z['gammas'][:,:,None,:]
            core[:,:,0,-self.j:]=2*np.einsum('ruc,rupc->rup',z['xs'],drxs)
            core[:,:,1,-self.j:]=np.sqrt(2)*np.einsum('ruc,rupc->rup',z['ss'],drxs)
        close=np.zeros((len(r0),3,self.size))
        close[:,:,:na]=self.args.closure_weight*np.sqrt(len(f0))*dmean[:,0].transpose(0,2,1)
        bound=np.zeros((len(r0),2,self.size))
        if not self.args.fixed_radius:
            scale=self.args.radius_weight*np.sqrt(len(f0))
            bound[:,0,-self.j:]=-scale*(z['a']<self.args.radius_floor*grid['a'])[:,None]*r0
            bound[:,1,-self.j:]=scale*(z['a']>self.args.radius_ceiling*grid['a'])[:,None]*r0
        return np.vstack((core.reshape(-1,self.size),close.reshape(-1,self.size),bound.reshape(-1,self.size)))

    def seed(self):
        s=self.radial.collocation(10)
        n=max(128,8*self.args.modes)
        grid=self.prepare(s,n)
        u=grid['u']
        phi=u.copy()
        for _ in range(30):
            rho=1+self.args.seed2*np.cos(2*phi)+self.args.seed3*np.cos(3*phi)
            step=(phi+self.args.seed2*np.sin(2*phi)/2+self.args.seed3*np.sin(3*phi)/3-u)/rho
            phi-=step
            if np.max(np.abs(step))<1e-14:
                break
        angle_coeff=np.linalg.lstsq(grid['fourier'][0],phi-u,rcond=None)[0]
        h=(s-self.meridian.start)/(self.meridian.end-self.meridian.start)
        envelope=64*h**3*(1-h)**3*(1+self.args.seed_asymmetry*(2*h-1))
        envelope_coeff=np.linalg.lstsq(grid['radial'][0],envelope,rcond=None)[0]
        q=np.zeros(self.size)
        q[:self.nangle]=np.outer(envelope_coeff,angle_coeff).ravel()
        return q

    def audit(self,q,radial,angles):
        s=np.linspace(0,self.meridian.length,radial)
        grid=self.prepare(s,angles)
        z=self.geometry(q,grid,True)
        e=np.sum(z['xs']**2,axis=-1)
        f=np.sum(z['xs']*z['ss'],axis=-1)
        g=np.sum(z['ss']**2,axis=-1)
        mat=np.empty((*e.shape,2,2))
        mat[:,:,0,0]=e-1
        mat[:,:,0,1]=mat[:,:,1,0]=f
        mat[:,:,1,1]=g-1
        xx=np.cross(z['xs'],z['xu'])
        det=np.sum(xx*xx,axis=-1)
        normal=xx/np.sqrt(np.maximum(det,1e-300))[:,:,None]
        hss=np.sum(normal*z['xss'],axis=-1)
        hsu=np.sum(normal*z['xsu'],axis=-1)
        huu=np.sum(normal*z['xuu'],axis=-1)
        gg=g*z['a'][:,None]**2
        ff=f*z['a'][:,None]
        hh=(gg*hss+e*huu-2*ff*hsu)/(2*np.maximum(det,1e-300))
        kk=(hss*huu-hsu*hsu)/np.maximum(det,1e-300)
        root=np.sqrt(np.maximum(hh*hh-kk,0))
        return {"radial_points":radial,"angular_points":angles,
                "metric_relative_operator_sample_max":float(np.max(np.abs(np.linalg.eigvalsh(mat)))),
                "angular_closure_sample_max":float(np.max(np.linalg.norm(z['mean'][:,0],axis=-1))),
                "radius_range":[float(np.min(z['a'])),float(np.max(z['a']))],
                "min_area_density_sample":float(np.min(np.sqrt(det))),
                "max_principal_curvature_sample":float(np.max(np.abs(hh)+root)),
                "coordinate_min":np.min(z['x'],axis=(0,1)).tolist(),
                "coordinate_max":np.max(z['x'],axis=(0,1)).tolist(),
                "closed_surface":False,"continuous_error_bound":False,"reach_proved":False}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--radius',type=float,default=.45)
    ap.add_argument('--length',type=float,default=2.)
    ap.add_argument('--collar',type=float,default=.06)
    ap.add_argument('--beta-wiggle',type=float,default=.9)
    ap.add_argument('--quadrature',type=int,default=96)
    ap.add_argument('--controls',type=int,default=12)
    ap.add_argument('--modes',type=int,default=5)
    ap.add_argument('--offset',type=float,default=.02)
    ap.add_argument('--radial-order',type=int,default=8)
    ap.add_argument('--angles',type=int,default=48)
    ap.add_argument('--seed2',type=float,default=.25)
    ap.add_argument('--seed3',type=float,default=.2)
    ap.add_argument('--seed-asymmetry',type=float,default=.4)
    ap.add_argument('--closure-weight',type=float,default=2.)
    ap.add_argument('--radius-floor',type=float,default=.7)
    ap.add_argument('--radius-ceiling',type=float,default=1.3)
    ap.add_argument('--radius-weight',type=float,default=10.)
    ap.add_argument('--fixed-radius',action='store_true')
    ap.add_argument('--max-nfev',type=int,default=120)
    ap.add_argument('--check-jacobian',action='store_true')
    ap.add_argument('--resume',type=Path)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    if abs(args.seed2)+abs(args.seed3)>=1:
        ap.error('Need |seed2|+|seed3|<1')
    begin=time.monotonic()
    space=UnitTangentSpace(args)
    grid=space.prepare(space.radial.collocation(args.radial_order),args.angles)
    q=space.seed()
    if args.resume:
        saved=json.loads(args.resume.read_text())
        q=np.asarray(saved['coefficients'])
        if len(q)!=space.size:
            raise ValueError('Resume dimensions differ; project explicitly')
    jac_error=None
    if args.check_jacobian:
        direction=np.random.default_rng(20261114).normal(size=space.size)
        direction/=np.linalg.norm(direction)
        step=1e-6
        fd=(space.residual(q+step*direction,grid)-space.residual(q-step*direction,grid))/(2*step)
        analytic=space.jacobian(q,grid)@direction
        jac_error=float(np.linalg.norm(fd-analytic)/max(1.,np.linalg.norm(analytic)))
        print(json.dumps({'jacobian_direction_relative_error':jac_error}),flush=True)
    evaluations=[0]
    def fun(v):
        res=space.residual(v,grid)
        evaluations[0]+=1
        if evaluations[0]%10==1:
            print(json.dumps({'evaluation':evaluations[0],'rms':float(np.sqrt(np.mean(res**2))),
                              'max':float(np.max(np.abs(res))),'seconds':time.monotonic()-begin}),flush=True)
        return res
    initial=space.audit(q,97,max(args.angles*2,96))
    result=least_squares(fun,q,jac=lambda v:space.jacobian(v,grid),method='lm',x_scale='jac',
                         ftol=1e-11,gtol=1e-11,xtol=1e-11,max_nfev=args.max_nfev)
    audits=[space.audit(result.x,n,max(128,2*args.angles)) for n in [129,257,513]]
    report={'schema':'unit-tangent-collar-search-v1','status':'finite_design_only',
            'definition':vars(args)|{'out':str(args.out),'resume':str(args.resume) if args.resume else None},
            'reference_meridian':space.meridian.identity(),
            'metric_is_designed':not args.fixed_radius,
            'fixed_metric_refinement_demonstrated':False,
            'open_parallel_collar_two_jets_exact_by_representation':True,
            'solver':{'success':bool(result.success),'message':result.message,'nfev':result.nfev,
                      'cost':float(result.cost),'optimality':float(result.optimality)},
            'jacobian_direction_relative_error':jac_error,
            'initial_audit':initial,'final_audits':audits,'coefficients':result.x.tolist(),
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'shared_source_sha256':hashlib.sha256(Path(__file__).with_name('eccentric_collar_search.py').read_bytes()).hexdigest(),
            'elapsed_seconds':time.monotonic()-begin,
            'claim':{'exact_isometry':False,'closed_family':False,'reach_certified':False,'task_complete':False}}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'out':str(args.out),'metric_sample_max':audits[-1]['metric_relative_operator_sample_max'],
                      'closure_sample_max':audits[-1]['angular_closure_sample_max'],
                      'curvature_sample_max':audits[-1]['max_principal_curvature_sample'],
                      'seconds':report['elapsed_seconds']}),flush=True)


if __name__=='__main__':
    main()
