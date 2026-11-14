#!/usr/bin/env python3
"""Sparse, real-trigonometric evaluation of the unchanged exact R21 core.

The formulas are those of construct_general_reflected_core.py. This avoids
recomputing zero Fourier terms and uses only first jets for arc quadrature.
Author: GPT-6 Astra Pro / direct_geometry, AI-assisted 2026-11-08.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[name]='1'
import math
import numpy as np
from construct_general_reflected_core import ReflectedCore


def jets(phi,R,radial,height,order=4):
    phi=np.asarray(phi);shape=phi.shape;rho=np.zeros((order+1,)+shape);z=np.zeros_like(rho);rho[0]=R
    for coefficients,frequencies,target in [(radial,4*(np.arange(len(radial))+1),rho),(height,4*np.arange(len(height))+2,z)]:
        for coefficient,n in zip(coefficients,frequencies):
            if coefficient==0:continue
            phase=n*phi;co=coefficient*np.cos(phase);si=coefficient*np.sin(phase)
            target[0]+=co
            if order>=1:target[1]-=n*si
            if order>=2:target[2]-=n*n*co
            if order>=3:target[3]+=n**3*si
            if order>=4:target[4]+=n**4*co
    er=np.exp(1j*phi);out=[]
    for d in range(order+1):
        xy=er*sum(math.comb(d,k)*(1j**(d-k))*rho[k] for k in range(d+1))
        out.append(np.stack((xy.real,xy.imag,z[d]),axis=-1))
    return out


def geometry(phi,R,radial,height):
    F,d1,d2,d3,d4=jets(phi,R,radial,height)
    speed=np.linalg.norm(d1,axis=-1);cr=np.cross(d1,d2);cn=np.linalg.norm(cr,axis=-1)
    T=d1/speed[...,None];B=cr/cn[...,None];N=np.cross(B,T);kap=cn/speed**3
    triple=np.sum(cr*d3,axis=-1);triple_prime=np.sum(d1*np.cross(d2,d4),axis=-1)
    speed_log_prime=np.sum(d1*d2,axis=-1)/speed**2;cross_log_prime=np.sum(cr*np.cross(d1,d3),axis=-1)/cn**2
    w=triple*speed**3/cn**3;wt=(triple_prime+3*triple*(speed_log_prime-cross_log_prime))*speed**2/cn**3
    return dict(gamma=F,d1=d1,d2=d2,speed=speed,T=T,N=N,B=B,kappa=kap,w=w,wt=wt,D=B+w[...,None]*T)


class SparseReflectedCore(ReflectedCore):
    def __init__(self,R=1.,radial=(0.,0.),height=(.1,0.,0.),arc_nodes=4096):
        self.R=float(R);self.radial=tuple(radial);self.height=tuple(height)
        phi=2*np.pi*np.arange(arc_nodes)/arc_nodes;d1=jets(phi,R,radial,height,1)[1]
        speed=np.linalg.norm(d1,axis=-1);coef=np.fft.rfft(speed)/arc_nodes;self.a0=float(coef[0].real)
        active=np.flatnonzero(abs(coef[1:-1])>2e-16);K=int(active[-1]+1) if len(active) else 0
        self.k=np.arange(1,K+1);self.arccoef=coef[1:K+1]/(1j*self.k)
        self.arc_integral_omitted_l1=float(2*np.sum(abs(coef[K+1:-1])/np.arange(K+1,len(coef)-1)))
        self.speed_omitted_l1=float(2*np.sum(abs(coef[K+1:-1]))+abs(coef[-1]))
    def evaluate(self,x,theta):
        x,theta=np.broadcast_arrays(np.asarray(x,dtype=float),np.asarray(theta,dtype=float));y=self.a0*theta;phi=theta.copy()
        lo=np.floor(theta/(2*np.pi))*2*np.pi;hi=lo+2*np.pi
        for it in range(70):
            g=geometry(phi,self.R,self.radial,self.height);res=self.arc(phi)+x*g['w']-y;den=1+x*g['wt'];done=abs(res)<4e-15*max(1,self.a0)
            if np.all(done):break
            lo=np.where((res<0)&~done,phi,lo);hi=np.where((res>0)&~done,phi,hi)
            step=phi-res/(g['speed']*den);step=np.where((step<lo)|(step>hi)|~np.isfinite(step),(lo+hi)/2,step);phi=np.where(done,phi,step)
        g=geometry(phi,self.R,self.radial,self.height);den=1+x*g['wt'];scale=g['kappa']/den
        return dict(F=g['gamma']+x[...,None]*g['D'],Fx=g['B'],Ft=self.a0*g['T'],Fxx=(scale*g['w']**2)[...,None]*g['N'],
                    Fxt=(-self.a0*scale*g['w'])[...,None]*g['N'],Ftt=(self.a0*self.a0*scale)[...,None]*g['N'],N=g['N'],den=den,phi=phi,a0=self.a0,
                    residual=self.arc(phi)+x*g['w']-y)


def normalized_parameters(model,p):
    h=model.h0+p[0];maxmode=int(model.m[-1]);rad=np.zeros(maxmode//4);hei=np.zeros((maxmode+2)//4);hei[(model.base_mode-2)//4]=model.q
    for j,m in enumerate(model.m[1:],1):
        value=p[j]*model.pscale[j]
        if m%4==0:rad[m//4-1]=value
        else:hei[(m-2)//4]=value
    phi=2*np.pi*np.arange(model.S.arc_nodes)/model.S.arc_nodes;R=max(.2,math.sqrt(max(.04,1-(model.base_mode*model.q)**2/2)))
    erp=np.c_[-np.sin(phi),np.cos(phi),np.zeros(len(phi))]
    for it in range(20):
        d1=jets(phi,R,rad,hei,1)[1];speed=np.linalg.norm(d1,axis=-1);a0=float(np.mean(speed))
        if abs(a0-1)<3e-15:break
        derivative=float(np.mean(np.sum(d1*erp,axis=1)/speed));R-=(a0-1)/derivative
        if R<=.05:raise FloatingPointError('Core perimeter normalization left positive radius range')
    return dict(R=float(R),radial=rad.tolist(),height=hei.tolist(),halfwidth=float(h))


def control():
    import gzip,json,time
    from pathlib import Path
    from construct_general_reflected_core import curve_geometry
    p=Path('topics/large-amplitude-twist-flex/notes/f6curve_outward_base6_m12_q0075_c2.json.gz');data=json.load(gzip.open(p,'rt'));par=data['core'];theta=2*np.pi*np.arange(2048)/2048
    rad=np.r_[par['radial'],np.zeros(54)];hei=np.r_[par['height'],np.zeros(55)];rad[-1]=3e-11;hei[-2]=1e-11
    tic=time.monotonic();old=curve_geometry(theta,par['R'],rad,hei);oldtime=time.monotonic()-tic
    tic=time.monotonic();new=geometry(theta,par['R'],rad,hei);newtime=time.monotonic()-tic
    errors={k:float(np.max(abs(np.asarray(old[k])-np.asarray(new[k])))) for k in old}
    original=ReflectedCore(par['R'],rad,hei,9216).evaluate(par['halfwidth'],theta)
    sparse=SparseReflectedCore(par['R'],rad,hei,9216).evaluate(par['halfwidth'],theta)
    spatial={k:float(np.max(abs(np.asarray(original[k])-np.asarray(sparse[k])))) for k in original}
    from types import SimpleNamespace
    from f6curve_outward_bvp import OutwardPrefix
    cfg=data['config'];S=OutwardPrefix(48,cfg['amplitude'],cfg['delta'],cfg['v_up'],cfg['v_down'],cfg['ramp'],cfg['cycles'],32,cfg['base_mode'],compute_stable=False);S.h0=data['h0']
    model=SimpleNamespace(S=S,m=S.even,pscale=S.pscale,q=S.q,base_mode=S.base_mode,h0=S.h0)
    parameters=np.zeros(48);parameters[:len(data['parameters'])]=data['parameters'];parameters[24]=.01
    pn=S.parameters(parameters);pf=normalized_parameters(model,parameters)
    normalization={k:float(np.max(abs(np.asarray(pn[k])-np.asarray(pf[k])))) for k in pn}
    out=dict(scope='Independent dense original vs sparse trigonometric evaluation of the same exact R21 core, including high-mode perturbations',curve_errors=errors,core_errors=spatial,perimeter_normalization_errors=normalization,old_curve_seconds=oldtime,new_curve_seconds=newtime)
    Path('topics/large-amplitude-twist-flex/notes/f6direct_sparse_core_control.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

if __name__=='__main__':control()
