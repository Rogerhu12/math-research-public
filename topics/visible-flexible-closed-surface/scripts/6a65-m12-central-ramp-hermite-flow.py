#!/usr/bin/env python3
"""Fixed original M12 g: central negative-K ramp and actual C2 Hermite map.

Reuse the R116 n,m equations and its hybrid pointwise-frame representation.
The initial exact curve is the original rational M12 central cross-section,
normalized by its exact arclength integral to the SAME fixed f(0)=1. Numerical
quadrature evaluates that one fixed input. The original polynomial ramp and
physical coordinates are retained. No positive-K stability is assumed.

Accepted ODE/dense-output values are merely inputs to a separate exact-form
finite Fourier/shared-two-jet Hermite map. Its sampled Gram metric is then
computed from its OWN position derivatives at interior Gauss points. Neither
frame orthogonality nor an ODE RHS is substituted for that map's derivatives.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np
from scipy import fft
from scipy.integrate import solve_ivp

HERE=Path(__file__).resolve().parent


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path);out=importlib.util.module_from_spec(spec)
    sys.modules[name]=out;spec.loader.exec_module(out);return out


ad=module('m12_ramp_adapter',HERE/'6a65-m12-r137-fixed-metric-adapter.py')
hybrid=module('m12_ramp_hybrid',HERE/'fd2d-gc-ellipse-hybrid-flow.py')
LD=np.longdouble;CLD=np.clongdouble


class OriginalRamp:
    def __init__(self,meta):
        self.cfg=meta['frozen_profile'];cfg=self.cfg
        if cfg['direction']!='outward' or cfg['ramp_law']!='flat' or cfg['cycles']!=1:
            raise ValueError('Expected original outward flat one-cycle profile')
        self.delta,self.vq,self.eps,self.etaq=[Q(float(cfg[k])) for k in ('delta','vu','ramp','ramp_eta')]
        self.Tu=self.delta/(self.vq*(1-self.eps));self.R=self.Tu*self.eps
        self.breaks=[Q(0),self.R*self.etaq,self.R*(1-self.etaq),self.R]
        self.v,self.eta,self.length=[ad.base.ld(q) for q in (self.vq,self.etaq,self.R)]

    def profile(self,s):
        s=np.asarray(s,dtype=LD);t=np.clip(s/self.length,0,1)
        z=np.minimum(t,1-t);x=z/self.eta;first=z<self.eta
        smallF=np.where(first,self.eta/(1-self.eta)*(x**3-x**4/2),(z-self.eta/2)/(1-self.eta))
        smallP=np.where(first,self.eta**2/(1-self.eta)*(x**4/4-x**5/10),
                        (z*z/2-self.eta*z/2+3*self.eta*self.eta/20)/(1-self.eta))
        F=np.where(t<=LD('.5'),smallF,1-smallF)
        P=np.where(t<=LD('.5'),smallP,LD('.5')-(1-t)+smallP)
        d=np.where(first,(3*x*x-2*x**3)/(1-self.eta),1/(1-self.eta))
        a=1+self.v*self.length*P;ap=self.v*F;app=self.v/self.length*d
        coast=s>=self.length
        return np.where(coast,1+self.v*self.length/2+self.v*(s-self.length),a),np.where(coast,self.v,ap),np.where(coast,0,app)


class M12Hybrid(hybrid.Hybrid):
    def __init__(self,candidate,raw,modes,oversample,max_calls=500000):
        if (modes+1)%3:raise ValueError('modes+1 must be divisible by 3')
        self.candidate,self.M,self.work=candidate,modes,2*oversample*(modes+1)
        self.max_calls,self.calls=max_calls,0
        self.a0=LD(1);self.raw=raw;self.curve=ad.FixedRadiusCurve(raw,1.)
        self.theta=np.arange(self.work,dtype=LD)*(2*ad.base.PI/self.work)
        self.wave=np.fft.fftfreq(self.work,1/self.work).astype(LD)
        self.X0=np.asarray(self.curve.derivative(self.theta),dtype=LD)
        gp=np.asarray(self.curve.derivative(self.theta,1),dtype=LD)
        gpp=np.asarray(self.curve.derivative(self.theta,2),dtype=LD)
        self.ell0=np.sqrt(np.sum(gp*gp,axis=1))
        self.T0=gp/self.ell0[:,None]
        self.n0=np.linalg.norm(np.cross(gp,gpp),axis=1)/self.ell0**3
        self.A=float(np.max(self.X0[:,0]));self.B=float(np.max(self.X0[:,1]))
        ks=list(range(0,modes+1,3))+list(range(3,modes+1,3))
        fs=[0]*len(range(0,modes+1,3))+[1]*len(range(3,modes+1,3))
        self.shape_indices=(np.asarray(ks),np.asarray(fs));self.shape_size=len(ks)
        self.active_wave=np.r_[np.asarray(ks),np.zeros(12*self.work)]
        self.cache_s,self.cache_y,self.cache_frame=None,None,None

    def initial(self):
        values=np.zeros((self.work,14),dtype=LD)
        values[:,0]=self.n0;values[:,2:5]=self.X0;values[:,7]=1
        values[:,8:11]=self.T0
        values[:,11:14]=np.cross(values[:,5:8],self.T0)
        return self.encode(values)

    def rhs(self,s,state):
        self.calls+=1
        if self.calls>self.max_calls:raise RuntimeError('Explicit RHS budget reached')
        values=self.decode(state);n,m=values[:,:2].T
        if np.min(n)<=0:raise ArithmeticError('Positive-n chart failed in actual stage')
        a,ap,app=[np.asarray(x)[0] for x in self.candidate.profile([s])]
        cc=ap/a;K=-app/a;b=a/self.a0*self.ell0;l=(m*m+K)/n
        derivative=self.derivative(np.column_stack((l,m)))
        e1,e2,N=(values[:,j:j+3] for j in (5,8,11));v=np.empty_like(values)
        v[:,0]=derivative[:,1]/b+cc*(l-n);v[:,1]=derivative[:,0]/b-2*cc*m
        v[:,2:5]=e1;v[:,5:8]=l[:,None]*N;v[:,8:11]=m[:,None]*N
        v[:,11:14]=-l[:,None]*e1-m[:,None]*e2
        return self.encode(v)


def position_jets(flow,s,state):
    values=flow.decode(state);n,m=values[:,:2].T
    a,ap,app=[np.asarray(x)[0] for x in flow.candidate.profile([s])]
    l=(m*m-app/a)/n
    return np.stack((values[:,2:5],values[:,5:8],l[:,None]*values[:,11:14]))


def symmetric_fourier(jets):
    """Exact-form C3/reflection Fourier definition after one binary64 cast."""
    N=jets.shape[-2];q=jets[...,0]+1j*jets[...,1]
    qhat=fft.fft(q,axis=-1,norm='forward');zhat=fft.fft(jets[...,2],axis=-1,norm='forward')
    wave=np.fft.fftfreq(N,1/N).astype(int)
    qhat=np.where(wave%3==1,qhat.real,0);zhat=np.where(wave%3==0,zhat.real,0)
    qhat[...,N//2]=0;zhat[...,N//2]=0
    neg=(-np.arange(N))%N
    out=np.stack(((qhat+qhat[...,neg])/2,(qhat-qhat[...,neg])/(2j),zhat),axis=-1)
    return np.asarray(out[...,:N//2+1,:],dtype=np.complex128)


def evaluate_coeff(c,N,order=0):
    k=np.arange(c.shape[-2],dtype=LD)
    raw=np.asarray(c,dtype=CLD)*(1j*k[:,None])**order
    return fft.irfft(raw,n=N,axis=-2,norm='forward')


def actual_hermite_observe(mesh,coeff,raw,candidate,N,gauss):
    theta=np.arange(N,dtype=LD)*2*ad.base.PI/N
    gp=np.asarray(raw.derivative(theta,1),dtype=LD)
    # Fixed chart u = integral |gamma'| / a_gamma, evaluated numerically.
    density=np.sqrt(np.sum(gp*gp,axis=1))/LD(raw.a)
    gx,gw=np.polynomial.legendre.leggauss(gauss)
    peak=LD(0);curv=LD(0);peak_at=None;energy=LD(0);cells=[]
    c=np.asarray(coeff,dtype=CLD)
    for j in range(len(mesh)-1):
        a,b=ad.base.ld(mesh[j]),ad.base.ld(mesh[j+1]);h=b-a
        c0,c1,c2=c[j,0],h*c[j,1],h*h*c[j,2]/2
        r0=c[j+1,0]-c0-c1-c2;r1=h*(c[j+1,1]-c[j,1])-2*c2;r2=h*h*(c[j+1,2]-c[j,2])
        p=np.stack((c0,c1,c2,10*r0-4*r1+r2/2,-15*r0+7*r1-r2,6*r0-3*r1+r2/2))
        local=LD(0)
        for x,w in zip(gx,gw):
            t=(LD(x)+1)/2;s=a+h*t
            value=p[-1].copy();derivative=5*p[-1];second=20*p[-1]
            for k in range(4,-1,-1):value=value*t+p[k]
            for k in range(4,0,-1):derivative=derivative*t+k*p[k]
            for k in range(4,1,-1):second=second*t+k*(k-1)*p[k]
            Xs=evaluate_coeff(derivative/h,N);Xss=evaluate_coeff(second/(h*h),N)
            Xth=evaluate_coeff(value,N,1);Xthth=evaluate_coeff(value,N,2);Xsth=evaluate_coeff(derivative/h,N,1)
            f=candidate.profile([s])[0][0];bb=f*density
            E=np.sum(Xs*Xs,axis=-1);F=np.sum(Xs*Xth,axis=-1);G=np.sum(Xth*Xth,axis=-1)
            ee,ff,gg=E-1,F/bb,G/(bb*bb)-1
            op=np.abs(ee+gg)/2+np.sqrt(((ee-gg)/2)**2+ff*ff)
            q=np.max(op);local=max(local,q)
            if q>peak:peak=q;peak_at={'s':float(s),'theta':float(theta[np.argmax(op)]),'cell':j}
            normal=np.cross(Xs,Xth);normal/=np.sqrt(np.sum(normal*normal,axis=-1))[:,None]
            L,M,Nc=(np.sum(normal*z,axis=-1) for z in (Xss,Xsth,Xthth));det=E*G-F*F
            tr=(G*L-2*F*M+E*Nc)/det;kg=(L*Nc-M*M)/det
            curv=max(curv,np.max(np.abs(tr)/2+np.sqrt(np.maximum(0,tr*tr/4-kg))))
            energy+=h*LD(w)/2*np.mean((ee*ee+2*ff*ff+gg*gg)*bb)
        cells.append(float(local))
    return {'sampled_metric_peak':float(peak),'sampled_curvature_peak':float(curv),'peak_at':peak_at,
            'sampled_weighted_energy':float(energy),'gauss_per_cell':gauss,'angular_nodes':N,
            'radial_cells':len(mesh)-1,'own_Hermite_position_derivatives_used':True,
            'continuous_certificate':False,'cell_peaks':cells}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--data',type=Path,required=True);ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--modes',type=int,default=95);ap.add_argument('--oversample',type=int,default=2)
    ap.add_argument('--step',type=float,default=.002);ap.add_argument('--rtol',type=float,default=2e-13)
    ap.add_argument('--atol',type=float,default=2e-15);ap.add_argument('--gauss',type=int,default=6)
    ap.add_argument('--observation-multiple',type=int,default=2)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError('Fresh output required')
    start=time.monotonic();meta=HERE.parent/'notes'/ad.base.META_NAME
    if ad.sha(args.data)!=ad.base.DATA_SHA:raise ValueError('M12 source identity mismatch')
    candidate=OriginalRamp(json.loads(meta.read_text()));_,central_c=ad.exact_section(args.data,Q(0))
    if any(x for x in central_c[49:]):raise ArithmeticError('Expected exactly planar source central curve')
    raw=ad.NativeCurve(central_c,512,32);flow=M12Hybrid(candidate,raw,args.modes,args.oversample)
    state=flow.initial();mesh=[];nodal=[];rows=[];failure=None
    for j,(left,right) in enumerate(zip(candidate.breaks[:-1],candidate.breaks[1:])):
        count=max(1,int(np.ceil(float(right-left)/args.step)))
        exact_nodes=[left+(right-left)*Q(k,count) for k in range(count+1)]
        target=np.asarray([float(x) for x in exact_nodes])
        try:
            atol=args.atol/(1+flow.active_wave)**2
            sol=solve_ivp(flow.rhs,(float(left),float(right)),state,method='DOP853',rtol=args.rtol,
                          atol=atol,max_step=args.step,t_eval=target)
            if not sol.success:raise RuntimeError(sol.message)
        except Exception as exc:
            failure={'piece':j,'type':type(exc).__name__,'message':str(exc)};break
        for k,(s,y) in enumerate(zip(sol.t,sol.y.T)):
            if mesh and k==0:continue
            mesh.append(exact_nodes[k]);nodal.append(position_jets(flow,s,y))
        state=sol.y[:,-1].copy();diag=flow.diagnostics(float(right),state)
        rows.append({'piece':j,'end':float(right),'ode_diagnostic':diag,'rhs_calls':flow.calls})
        print(json.dumps({'piece':j,'end':float(right),'RHS_metric_diagnostic':diag['metric'],'calls':flow.calls}),flush=True)
    out={'schema':'6a65-M12-fixed-g-central-ramp-own-Hermite-metric-v1','script_sha256':ad.sha(__file__),
         'data_sha256':ad.base.DATA_SHA,'geometry_sha256':ad.sha(meta),
         'dependencies':{name:ad.sha(HERE/name) for name in ('6a65-m12-r137-fixed-metric-adapter.py','fd2d-gc-ellipse-flow.py','fd2d-gc-ellipse-hybrid-flow.py')},
         'original_physical_metric_unchanged':True,'raw_central_curve_definition':'Exact rational Hermite source at native zero, normalized by exact arc integral to f(0)=1',
         'numerical_arc_radius':raw.a,'normalization_numerical':1/raw.a,
         'central_arc_quadrature':{'panels':512,'gauss':32,'remainder_certified_in_this_run':False},
         'ramp_end_exact':str(candidate.R),'ramp_piece_breaks_exact':[str(x) for x in candidate.breaks],
         'modes':args.modes,'geometry_grid':flow.work,'step':args.step,'rtol':args.rtol,'atol':args.atol,
         'rows':rows,'failure':failure,'rhs_calls':flow.calls,'closed_surface_constructed':False}
    if failure is None:
        coeff=symmetric_fourier(np.asarray(nodal,dtype=LD))
        # Exact central reflection two-jet in the actual finite map.
        coeff[0,1:]=0;coeff[0,1,0,2]=1
        fieldpath=Path(str(args.out)+'.field.npz')
        np.savez_compressed(fieldpath,coefficients=coeff,mesh_numerator=np.asarray([str(x.numerator) for x in mesh]),
                            mesh_denominator=np.asarray([str(x.denominator) for x in mesh]),
                            state=state,central_c_numerator=np.asarray([str(x.numerator) for x in central_c]),
                            central_c_denominator=np.asarray([str(x.denominator) for x in central_c]))
        observed=actual_hermite_observe(mesh,coeff,raw,candidate,flow.work*args.observation_multiple,args.gauss)
        out['own_Hermite_observer']=observed
        out['field_sha256']=ad.sha(fieldpath);out['field_file']=str(fieldpath)
        out['actual_map_definition']='Binary64 complex Cartesian Fourier nodal 0..2 jets with exact C3/reflection coefficient masks, exact rational physical mesh, exact quintic Hermite in sigma. At sigma=0 first jet exactly ez and second jet exactly zero.'
        out['new_numerical_solution_not_claimed_exact']=True
    out['seconds']=time.monotonic()-start
    args.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    display={k:v for k,v in out.items() if k not in ('rows','own_Hermite_observer')}
    if 'own_Hermite_observer' in out:display['own_Hermite_observer']={k:v for k,v in out['own_Hermite_observer'].items() if k!='cell_peaks'}
    print(json.dumps(display,indent=2,allow_nan=False))


if __name__=='__main__':main()
