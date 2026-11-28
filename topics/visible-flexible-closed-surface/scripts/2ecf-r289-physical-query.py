#!/usr/bin/env python3
"""Numerical arbitrary-material and arbitrary native finite-layer querying of the true R289 field, including the full spatial-map two-jet chain."""
import argparse,bisect,importlib.util,json,os,sys
from pathlib import Path
for key in ('MKL_NUM_THREADS','OPENBLAS_NUM_THREADS','OMP_NUM_THREADS'):os.environ[key]='1'
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from math import comb

def module(path,name):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m);return m
HERE=Path(__file__).resolve().parent
class Field:
    def __init__(self,scripts,meridian,buffer,table,state,scale,primitive_tolerance='2e-18'):
        from types import SimpleNamespace
        self.scripts=Path(scripts).resolve();self.scale=float(scale);self.table=Path(table);self.mod=module(HERE/'2ecf-r289-true-cuff-closed-image-maps.py','r289_query_maps');f=self.mod;m=f.m;self.m=m;self.d=d=json.loads(Path(state).read_bytes());self.x=np.array(d['xyz']);self.src=q=m.Source(SimpleNamespace(meridian=Path(meridian),buffer=Path(buffer),tail_table=self.table,index=d['index']));self.T=q.T;self.S=q.S;self.sa=q.S+q.dso;self.eps=d['epsilon'];pw=d['stadiumPower'];mix=d['stadiumMix'];b=np.array([2*(-1)**j*comb(2*pw,pw-j)/comb(2*pw,pw)/(1-4*j*j) for j in range(1,pw+1)]);self.A=q.R+self.eps*((1-mix)+mix*b.sum()/b[::2].sum());f.install(self.A);m.support=lambda R,e,u:f.v.stadium_center(R,e,u,pw,mix);old=m.jet
        def scaled(rr,u,eps,linear=True):
            t=rr.copy();t[:,[7,9,11]]*=d['horizontalLinearScale'];t[:,[8,10,12]]*=d['verticalLinearScale'];return old(t,u,eps,linear)
        m.jet=scaled;self.cutZ=q.original(np.array([0]))[0,2];self.cuff=float(q.tail['r'][0]);self.tol=primitive_tolerance;self.bg=None
    def _prepare(self):
        if self.bg is not None:return
        S=self.scripts;mod=module(S/'6a65-m12-original-tail-background.py','r289_query_original_background');n=S.parent/'notes';bg=mod.OriginalTailBackground(n/'2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json',n/'2026-11-09-db6f-tail-finite-source-calibrations.json',np.longdouble(self.tol));self.bg=bg;self.cache={};self.ends=[];self.order=[];self.floor={};ds=dz=np.longdouble(0)
        labels=self.src.tail['labels'];lookup={}
        for i,(n,j,x) in enumerate(labels):lookup.setdefault((int(n),int(j)),[]).append(i)
        for row in bg.outer_order:
            key=(row.n,row.j);self.floor[key]=(ds,dz);ds+=row.total[2]+bg.alpha*row.total[3];dz+=row.total[4]+bg.alpha*row.total[5];self.ends.append(ds);self.order.append(key);self.cache[key]=np.array(lookup[key],int)
    def _raw(self,n,j,x):
        self._prepare();bg=self.bg;row=bg.profiles[9*n+j];part=row.partial(np.longdouble(x));sr,zr=self.floor[n,j];rad=row.r_left+part[0]+bg.alpha*part[1];sr+=(row.total[2]-part[2])+bg.alpha*(row.total[3]-part[3]);zr+=(row.total[4]-part[4])+bg.alpha*(row.total[5]-part[5]);A,B,w,wx=bg.source.evaluate(n,j,np.longdouble(x));return float(rad*self.scale),float(sr*self.scale),float(zr*self.scale),float(w),float(wx/(self.scale*(A+bg.alpha*B)))
    def native_row(self,n,j,x):
        if not (0<=n<160 and 0<=j<=8 and 0<=x<=1):raise ValueError('Numerical raw-label interface covers every native finite layer 0..159')
        r,s,z,w,wr=self._raw(n,j,x);src=self.src
        if r>src.rb[0]+2e-13:raise ValueError('Use prefix or buffer interface outside the protected scaled inner tail')
        ids=self.cache[n,j];xx=src.tail['labels'][ids,2];ii=np.clip(np.searchsorted(xx,x,side='right')-1,0,len(ids)-1);i=ids[ii];x0=xx[ii];r0=src.tail['r'][i];F0,H0=src.tail['linear'][:2,i];mu=np.longdouble(self.cuff)**7*np.longdouble(2)**(-np.longdouble(11)*n/4);root=np.sqrt(np.longdouble(12));q0=np.longdouble(H0)/np.longdouble(r0)**4;p0=-3*np.longdouble(r0)**3*np.longdouble(F0)/(root*mu);norm=max(abs(q0),abs(p0));F=H=0.
        if norm!=0:
            y=np.asarray([q0/norm,p0/norm,r0],float)
            if abs(x-x0)>5e-17:
                bg=self.bg
                def rhs(t,y):
                    A,B,w0,_=bg.source.evaluate(n,j,np.longdouble(t));dr=(A+bg.alpha*B)*self.scale;rr=np.longdouble(y[2]);return [float(root*mu*dr/(rr**8*w0))*y[1],-float(root*rr**6*w0*dr/mu)*y[0],float(dr)]
                sol=solve_ivp(rhs,(float(x0),float(x)),y,method='DOP853',rtol=5e-12,atol=5e-14,max_step=abs(x-x0)/3);assert sol.success;y=sol.y[:,-1]
            H=float(np.longdouble(y[0])*norm*np.longdouble(r)**4)*src.tailScale;F=float(-root*mu*np.longdouble(y[1])*norm/(3*np.longdouble(r)**3))*src.tailScale
        E=1+w*w;v=-1/np.sqrt(E);b=w/np.sqrt(E);vs=-w*wr/E**2;bs=-wr/E**2;J=-3*F/(w*r);Hr=4*H/r+J;Fs=-(3*v*F+4*b*H)/r;Hs=v*Hr;Fss=-(3*vs*F+4*v*Fs+4*bs*H+4*b*Hs)/r;Hss=-v*v*wr*J/w+vs*Hr
        return np.array([self.sa+s-src.sa,r,src.shift+src.dzo+z-src.za,v,b,vs,bs,F,H,Fs,Hs,Fss,Hss])
    def row(self,s):
        src=self.src;s=abs(float(s))
        if s<0 or s>self.T+2e-15:raise ValueError('Outside the complete material half-core')
        if s<=self.S:return src.prefix(np.array([s]))[0]
        if s<=self.sa:
            target=self.sa-s
            for j,(left,right) in enumerate(zip(src.rb[:-1],src.rb[1:])):
                fun=lambda r:src.bsol[j](r)[3]-target
                if fun(left)<=0<=fun(right):return src.buffer(np.array([brentq(fun,left,right,xtol=2e-15)]))[0]
            return src.buffer(np.array([src.rb[0] if target<1e-12 else src.rb[-1]]))[0]
        if s>=self.T:return np.array([self.T,self.cuff,self.cutZ,-1.,0.,0.,0.,0.,0.,0.,0.,0.,0.])
        self._prepare();target=np.longdouble(s-self.sa+src.sa)/self.scale;k=min(bisect.bisect_left(self.ends,target),len(self.ends)-1);n,j=self.order[k];row=self.bg.profiles[9*n+j];outside=self.floor[n,j][0];alpha=self.bg.alpha
        def fun(x):
            part=row.partial(np.longdouble(x));return float(outside+row.total[2]-part[2]+alpha*(row.total[3]-part[3])-target)
        if fun(0)<=0:x=0.
        elif fun(1)>=0:x=1.
        else:x=brentq(fun,0,1,xtol=2e-14)
        return self.native_row(n,j,x)
    def _jet(self,rows,u):return self.m.Fit(self.src,np.asarray(rows),np.remainder(np.asarray(u,dtype=float),2*np.pi),self.eps,self.d['spans'],self.d['modes']).field(self.x)
    def grid(self,s,u):
        ss=np.atleast_1d(s).astype(float);jets=self._jet([self.row(z) for z in ss],np.atleast_1d(u));neg=ss<0
        if np.any(neg):
            jets[neg,:,: ,2]*=-1
            for j in (1,4):jets[neg,j]*=-1
        return jets
    def native_grid(self,n,j,x,u):return self._jet([self.native_row(n,j,xx) for xx in np.atleast_1d(x)],np.atleast_1d(u))
    def observed_rows(self,radial,angular,shift=True):
        rows,u=self.src.grid(radial,angular,shift);return rows[:,0],u,self._jet(rows,u)

    def phase_grid(self,s,u,alpha):
        J=self.grid(s,np.asarray(u)-alpha);c,sn=np.cos(alpha),np.sin(alpha);old=J[...,:2].copy();J[...,0]=c*old[...,0]-sn*old[...,1];J[...,1]=sn*old[...,0]+c*old[...,1];return J
