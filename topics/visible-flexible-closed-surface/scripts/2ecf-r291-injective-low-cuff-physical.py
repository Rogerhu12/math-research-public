#!/usr/bin/env python3
"""Convex, strictly height-ordered complete low-cuff core; independent genuine physical deformations through the complete R289 shape maps."""
import argparse,importlib.util,json,os
from pathlib import Path
for k in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[k]='1'
import numpy as np
from scipy.linalg import solve
from math import comb
p=Path(__file__).with_name('2ecf-r289-true-cuff-closed-image-maps.py');sp=importlib.util.spec_from_file_location('true_r291_maps',p);F=importlib.util.module_from_spec(sp);sp.loader.exec_module(F);m=F.m;dot=F.dot

def mul(a,b):return np.array([a[0]*b[0],a[1]*b[0]+a[0]*b[1],a[2]*b[0]+2*a[1]*b[1]+a[0]*b[2]])
def unary(a,f,df,dd):return np.array([f,df*a[1],df*a[2]+dd*a[1]**2])
def exp(a):return unary(a,*([np.exp(a[0])]*3))
def inv(a):y=1/a[0];return unary(a,y,-y*y,2*y**3)
def tanh(a):y=np.tanh(a[0]);d=1-y*y;return unary(a,y,d,-2*y*d)
def con(x):return np.array([x,np.zeros_like(x),np.zeros_like(x)])
def powr(a,n):
    b=con(np.ones_like(a[0]));
    for _ in range(n):b=mul(b,a)
    return b

def prod(a,b):
    p,v,u,ss,su,uu=a;q,w,t,aa,bb,cc=b
    return np.stack([p*q,v*q+p*w,u*q+p*t,ss*q+2*v*w+p*aa,su*q+v*t+u*w+p*bb,uu*q+2*u*t+p*cc])
def recip(a):
    p,v,u,ss,su,uu=a;x=1/p;return np.stack([x,-x*x*v,-x*x*u,2*x**3*v*v-x*x*ss,2*x**3*v*u-x*x*su,2*x**3*u*u-x*x*uu])

def bern(t,co):
    one=con(np.ones_like(t[0]));return sum(comb(len(co)-1,k)*z*mul(powr(t,k),powr(one-t,len(co)-1-k)) for k,z in enumerate(co))
class Model:
    def __init__(self,src,eps=.34):
        self.src=src;self.eps=eps;self.R=src.R;self.Z=src.original(np.array([0]))[0,2];self.modes=2*np.arange(1,33);b=np.array([2*(-1)**j*comb(64,32-j)/comb(64,32)/(1-4*j*j) for j in range(1,33)]);self.unit=b/b[::2].sum();self.A=self.R+eps*self.unit.sum();F.install(self.A)
    def curves(self,rows,u,c):
        src=self.src;n=len(rows);t=np.array([rows[:,0]/src.T,np.full(n,1/src.T),np.zeros(n)]);one=con(np.ones(n));r=rows[:,(1,3,5)].T;z=rows[:,(2,4,6)].T;f=rows[:,(7,9,11)].T;lift=64*mul(powr(t,3),powr(one-t,3));clock=mul(t,inv(t+mul(exp(bern(t,c[:4])),one-t)));q=one-mul(powr(clock,3),10*one-15*clock+6*powr(clock,2));inner=mul(one-q,r)
        shape0=mul(mul(r,q),con(self.eps/self.R*np.ones(n)));base2=.2*tanh(mul(f,inv(r))*(self.eps/.2)+mul(lift,bern(t,c[4:7])));base4=.015*tanh(mul(lift,bern(t,c[7:10])));coef=shape0[:,:,None]*self.unit[None,None,:];coef[:,:,0]+=mul(inner,base2);coef[:,:,1]+=mul(inner,base4)
        raw=np.tile(u,(n,1));a2=.11*mul(lift,bern(t,np.tanh(c[10:13])));a4=.035*mul(lift,bern(t,np.tanh(c[13:16])));k2=2*u;k4=4*u;eff=raw+a2[0,:,None]*np.sin(k2)+a4[0,:,None]*np.sin(k4);vs=a2[1,:,None]*np.sin(k2)+a4[1,:,None]*np.sin(k4);vu=1+2*a2[0,:,None]*np.cos(k2)+4*a4[0,:,None]*np.cos(k4);vss=a2[2,:,None]*np.sin(k2)+a4[2,:,None]*np.sin(k4);vsu=2*a2[1,:,None]*np.cos(k2)+4*a4[1,:,None]*np.cos(k4);vuu=-4*a2[0,:,None]*np.sin(k2)-16*a4[0,:,None]*np.sin(k4)
        # Strict positive curvature makes this scalar normal angle unique on each material ring.
        ph=eff.copy();km=self.modes;sigma=(1-km*km);dcoef=coef*sigma[None,None,:];r0,rs,rss=r[:,:,None]
        for _ in range(14):
            arg=ph[:,:,None]*km;co=np.cos(arg);si=np.sin(arg);res=r0*(ph-eff)+np.einsum('nuk,nk->nu',si,dcoef[0]/km);rho=r0+np.einsum('nuk,nk->nu',co,dcoef[0]);delta=np.clip(res/rho,-.6,.6);ph-=delta
            if abs(delta).max()<1e-13:break
        bad=np.abs(r0*(ph-eff)+np.einsum('nuk,nk->nu',np.sin(ph[:,:,None]*km),dcoef[0]/km))>8e-13
        if np.any(bad):
            ir,iu=np.where(bad);v0=eff[ir,iu];rr=r[0,ir];ac=dcoef[0,ir]/km;lo=v0-2*np.pi;hi=v0+2*np.pi
            for _ in range(47):
                mid=(lo+hi)/2;val=rr*(mid-v0)+(np.sin(mid[:,None]*km)*ac).sum(axis=1);lo=np.where(val<=0,mid,lo);hi=np.where(val>0,mid,hi)
            ph[ir,iu]=(lo+hi)/2
        arg=ph[:,:,None]*km;co=np.cos(arg);si=np.sin(arg);pair=lambda a,b:np.einsum('nuk,nk->nu',a,b)
        rho=r0+pair(co,dcoef[0]);rho_s=rs+pair(co,dcoef[1]);rho_phi=-pair(si,dcoef[0]*km);h=r0+pair(co,coef[0]);hs=rs+pair(co,coef[1]);hss=rss+pair(co,coef[2]);hp=-pair(si,coef[0]*km);hps=-pair(si,coef[1]*km);hpss=-pair(si,coef[2]*km)
        ps=(rs*(eff-ph)+r0*vs-pair(si,dcoef[1]/km))/rho;pu=r0*vu/rho;pss=(rss*(eff-ph)+2*rs*vs+r0*vss-pair(si,dcoef[2]/km)-2*rho_s*ps-rho_phi*ps**2)/rho
        en=np.stack([np.cos(ph),np.sin(ph)],axis=-1);et=np.stack([-np.sin(ph),np.cos(ph)],axis=-1);vec=lambda a,b:a[...,None]*en+b[...,None]*et
        xy=np.stack([vec(h,hp),vec(hs,hps+rho*ps),vec(0*pu,r0*vu),vec(hss-rho*ps**2,hpss+2*rho_s*ps+rho_phi*ps**2+rho*pss),vec(-r0*vu*ps,rs*vu+r0*vsu),vec(-r0*vu*pu,r0*vuu)])
        x,y=xy[...,0],xy[...,1];xx=prod(x,x);yy=prod(y,y);cos2=prod(xx-yy,recip(xx+yy));cos4=2*prod(cos2,cos2);cos4[0]-=1
        hgt=z/self.Z;wave=64*mul(powr(hgt,3),powr(one-hgt,3));wav2=mul(wave,2*hgt-one);rad=lambda a:np.stack([a[i,:,None]*np.ones(raw.shape) if j==0 else np.zeros_like(raw) for i,j in m.O]);zz=rad(z)+self.Z*(.14*np.tanh(c[16])*prod(rad(wave),cos2)+.08*np.tanh(c[17])*prod(rad(wav2),cos4));J=np.concatenate([xy,zz[...,None]],axis=-1).transpose(1,0,2,3);return J
    def field(self,rows,u,c):return F.k.ball(F.k.slab(self.curves(rows,u,c))[0])

def metrics(J,rows,u):
    q=type('q',(),{})();q.old=J;q.bb=rows[:,1,None]+np.zeros((1,len(u)));q.t=u;q.z=rows[:,0];ret=m.base.Grid.metrics(q,None,True);P=J[:,0];ret.update(maxAbsY=float(abs(P[...,1]).max()),maxNorm=float(np.linalg.norm(P,axis=-1).max()),heightRange=[float(P[...,2].min()),float(P[...,2].max())]);return ret

def observe(g,c):
    all=[]
    for count,angles,shift in [(275,120,False),(267,149,True)]:
        rr,u=g.src.grid(count,angles,shift);results=[]
        for i in range(0,len(rr),36):
            rows=rr[i:i+36];J=g.field(rows,u,c);results.append(metrics(J,rows,u))
        top=max(results,key=lambda z:z['metric']).copy();top.update(curvature=max(z['curvature'] for z in results),maxAbsY=max(z['maxAbsY'] for z in results),maxNorm=max(z['maxNorm'] for z in results),areaRatioMin=min(z['areaRatioMin'] for z in results),heightRange=[min(z['heightRange'][0] for z in results),max(z['heightRange'][1] for z in results)]);top['minimumUpperHeight']=top['heightRange'][0];top['maximumRadius']=max(z['maximumRadius'] for z in results);top.pop('rms');all.append(dict(radial=len(rr),angular=angles,actual=top));print('observe',all[-1],flush=True)
    return all

def native_observer(g,c):
    ids=np.flatnonzero(g.src.tail['r']<=g.src.rb[0]+1e-14)
    raw=g.src.original(ids)
    rows=np.unique(raw,axis=0)
    u=(np.arange(120)+.5)*2*np.pi/120
    stats=[]
    for i in range(0,len(rows),48):
        r=rows[i:i+48]
        stats.append(metrics(g.field(r,u,c),r,u))
    return dict(nativeRows=len(raw),distinctTwoJetRows=len(rows),angles=120,metric=max(z['metric'] for z in stats),curvature=max(z['curvature'] for z in stats),areaRatioMin=min(z['areaRatioMin'] for z in stats))

def main():
    p=argparse.ArgumentParser()
    for n in ('meridian','buffer','tail-table','out'):p.add_argument('--'+n,type=Path,required=True)
    p.add_argument('--native',action='store_true');p.add_argument('--index',type=int,default=1);p.add_argument('--steps',type=int,default=5);p.add_argument('--parent',type=Path);p.add_argument('--clock',type=float,default=1.);p.add_argument('--kweight',type=float,default=.025);a=p.parse_args();src=m.Source(a);g=Model(src);c=np.r_[np.full(4,a.clock),np.zeros(14)] if not a.parent else np.array(json.loads(a.parent.read_bytes())['controls']);raw,u=src.grid(83,39,True);idx=np.r_[np.linspace(0,len(raw)-1,90,dtype=int),np.argmin(abs(raw[:,0]-.25))];rr=raw[np.unique(idx)];u=np.linspace(0,np.pi/2,35)
    def vals(x,full=False):
        J=g.field(rr,u,x);M=metrics(J,rr,u);V,U=J[:,1],J[:,2];r=rr[:,1,None];E,H,G=dot(V,V)-1,np.sqrt(2)*dot(V,U)/r,dot(U,U)/r**2-1;K,_=F.v.curve(J);kp=np.maximum(abs(K)-9.6,0)*np.sign(K);peak=abs(E+G)/2+np.hypot((E-G)/2,H/np.sqrt(2));res=np.stack([E,H,G,a.kweight*kp],axis=-1);return M,res,peak
    hist=[];steps=[]
    for it in range(a.steps+1):
        old,r,peak=vals(c);hist.append(old);print('run',it,old,flush=True)
        if it==a.steps:break
        weight=(.05+(peak/max(1.e-9,peak.max()))**2)**.5;W=np.broadcast_to(weight[...,None],r.shape).ravel();cols=[]
        for j in range(len(c)):
            v=c.copy();v[j]+=.00007;cols.append(((vals(v)[1]-r)/.00007).ravel()*W)
        A=np.array(cols).T;q=r.ravel()*W;h=A.T@A;ss=np.maximum(np.diag(h)**.5,.01);best=None;merit=lambda z:z['metric']+a.kweight*max(0,z['curvature']-9.6)
        for reg in (.0003,.015,.2):
            dx=solve(h/ss[:,None]/ss[None,:]+reg*np.eye(len(c)),-(A.T@q)/ss,assume_a='pos')/ss;dx*=min(1,1.5/(abs(dx).max()+1e-15))
            for st in [1,.5,.25,.125,.0625]:
                z=vals(c+st*dx)[0]
                if merit(z)<merit(old)*(1-1e-5) and (best is None or merit(z)<best[0]):best=(merit(z),st,reg,dx)
        if best is None:break
        _,st,reg,dx=best;c+=st*dx;steps.append(dict(scale=st,reg=reg))
    obs=observe(g,c);d=dict(schema='R291-embedded-complete-low-cuff-candidate-true-positive-height-convex-ring-v1',entrySHA256=m.base.sha(__file__),meridianSHA256=m.base.sha(a.meridian),bufferSHA256=m.base.sha(a.buffer),tableSHA256=m.base.sha(a.tail_table),parentSHA256=m.base.sha(a.parent) if a.parent else None,index=a.index,epsilon=g.eps,centralRadius=src.R,major=g.A,cuffHeight=g.Z,materialT=src.T,controls=c.tolist(),history=hist,steps=steps,observers=obs,kweight=a.kweight)
    if a.native:d['nativeObserver']=native_observer(g,c);print('native',d['nativeObserver'],flush=True)
    with a.out.open('x') as f:json.dump(d,f,indent=2);f.write('\n')
if __name__=='__main__':main()
