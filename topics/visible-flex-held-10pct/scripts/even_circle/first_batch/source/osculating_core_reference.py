"""Untruncated osculating-circle core reference for finite Frenet BVPs.
On every exact circular arc it equals the explicit local rotational patch.
Mean vertical position is removed before the existing mean-height recovery.
All integral evaluations are Gauss diagnostics, not certified quadrature.
"""
import math
import numpy as np


def install_osculating_reference(Flow,BaseBVP,window=(.5,.9),quadrature=16):
    old_geo=Flow.geo;gx,gw=np.polynomial.legendre.leggauss(quadrature)
    def geo(self,s,N):
        g=old_geo(self,s,N);core=getattr(self,'reference_core',None)
        if core is None:return g
        if self.warp_e!=0:raise ValueError('Osculating reference currently requires the physical angle chart')
        if N not in self.reference_cache:
            theta=2*np.pi*np.arange(N)/N;self.reference_cache[N]=core.rho_material_jets(theta)
        c=self.reference_cache[N];s=np.atleast_1d(s);A,V,K=self.profile(s)
        lo,hi=window;span=(hi-lo)*self.prefix_end;x=np.clip((s-lo*self.prefix_end)/span,0.,1.);chi=1-x**3*(10-15*x+6*x*x);chip=-30*x*x*(1-x)**2/span;chipp=-60*x*(1-x)*(1-2*x)/span**2
        active=np.flatnonzero(chi>0)
        if len(active)==0:return g
        sa=s[active];a=A[active,None];v=V[active,None];acc=K[active,None];rho=c['rho'][None,:];ru=c['rho_u'][None,:];ruu=c['rho_uu'][None,:];normal=c['normal'][None,:,:];tan=c['Ft'][None,:,:]
        bsq=1-v*v*rho*rho
        if np.min(bsq)<=0:raise FloatingPointError('Osculating reference root domain failure')
        b=np.sqrt(bsq);Z=np.zeros((len(sa),N,3))
        for low,high in zip(self.breaks[:-1],self.breaks[1:]):
            upper=np.minimum(sa,high);width=np.maximum(0,upper-low);indices=np.flatnonzero(width>0)
            if len(indices)==0:continue
            t=(low+upper[indices,None])/2+width[indices,None]*gx[None,:]/2
            vel=self.profile(t.ravel())[1].reshape(t.shape)[:,:,None];rr=c['rho'][None,None,:];r1=c['rho_u'][None,None,:];r2=c['rho_uu'][None,None,:];bb2=1-vel*vel*rr*rr
            if np.min(bb2)<=0:raise FloatingPointError('Osculating integral root domain failure')
            bb=np.sqrt(bb2);bu=-vel*vel*rr*r1/bb;buu=-vel*vel*(r1*r1+rr*r2)/bb-vel**4*rr*rr*r1*r1/bb**3
            for j,field in enumerate((bb,bu,buu)):Z[indices,:,j]+=width[indices,None]/2*np.einsum('tqu,q->tu',field,gw)
        local={}
        local['pos']=c['F'][None,:,:]+(a-1)[:,:,None]*rho[:,:,None]*normal
        local['pos'][:,:,2]=Z[:,:,0]-np.mean(Z[:,:,0],axis=1)[:,None]
        local['p1']=a[:,:,None]*tan+(a-1)[:,:,None]*ru[:,:,None]*normal;local['p1'][:,:,2]=Z[:,:,1]
        local['p2']=((a-1)*ruu-a/rho)[:,:,None]*normal+((a-1)*ru/rho)[:,:,None]*tan;local['p2'][:,:,2]=Z[:,:,2]
        local['s1']=v[:,:,None]*rho[:,:,None]*normal;local['s1'][:,:,2]=b-np.mean(b,axis=1)[:,None]
        b_s=-v*acc*rho*rho/b;local['s2']=acc[:,:,None]*rho[:,:,None]*normal;local['s2'][:,:,2]=b_s-np.mean(b_s,axis=1)[:,None]
        local['sp']=v[:,:,None]*(ru[:,:,None]*normal+tan);local['sp'][:,:,2]=-v*v*rho*ru/b
        local['spp']=v[:,:,None]*((ruu-1/rho)[:,:,None]*normal+(ru/rho)[:,:,None]*tan);local['spp'][:,:,2]=-v*v*(ru*ru+rho*ruu)/b-v**4*rho*rho*ru*ru/b**3
        h=chi[active,None,None];hp=chip[active,None,None];hpp=chipp[active,None,None]
        difference={k:local[k]-g[k][active] for k in local}
        for k in ('pos','p1','p2'):g[k][active]+=h*difference[k]
        g['s1'][active]+=h*difference['s1']+hp*difference['pos']
        g['s2'][active]+=h*difference['s2']+2*hp*difference['s1']+hpp*difference['pos']
        g['sp'][active]+=h*difference['sp']+hp*difference['p1']
        g['spp'][active]+=h*difference['spp']+hp*difference['p2']
        return g
    Flow.geo=geo
    class RefBVP(BaseBVP):
        def initial(self,p):
            super().initial(p)
            self._projected_core_initial=self._initial.copy();self._raw_projection=dict(self._inlet_metrics)
            self._initial=np.zeros(self.n);self._initial_jac=np.zeros((self.n,self.M))
            self._inlet_metrics=dict(position=0.,first=0.,second=0.,metric_l1=0.,scope='Exact core and circle-local osculating reference, evaluated by independent integral formulas.')
            f=super().flow(p[0])
            if getattr(f,'reference_key',None)!=self._core_key:
                f.reference_core=self._core;f.reference_cache={};f.reference_key=self._core_key
            return self._initial
        def fun(self,t,y,p):
            self.initial(p)
            return super().fun(t,y,p)
        def fun_jac(self,t,y,p):
            self.initial(p);f=self.flow(p[0]);s,ds=self.chart(t,p[0]);J,_=f.fun_jac(s,y,p);PJ=np.empty((self.n,len(p),len(t)))
            for j in range(len(p)):
                step=2e-6*max(.1,self.cfg['delta']+p[0]) if j==0 else 2e-5*max(1.,abs(p[j]))
                plus=p.copy();minus=p.copy();plus[j]+=step;minus[j]-=step
                PJ[:,j,:]=(self.fun(t,y,plus)-self.fun(t,y,minus))/(2*step)
            self.initial(p);return ds[None,None,:]*J,PJ
        def terminal(self,y,p):
            self.initial(p);return super().terminal(y,p)
        def seed(self,nodes):
            from fixed_metric_mode3_bvp import merge_profile_mesh
            f=self.flow(0);line=f.backward_line();t=merge_profile_mesh(np.linspace(0,1,nodes),self.chart_breaks);s,_=self.chart(t,0);fg=np.empty((2,len(s)))
            for j,(low,high,sol,scale)in enumerate(line.segments):
                mask=(s>=low)&((s<high)if j+1<len(line.segments)else(s<=high))
                if np.any(mask):fg[:,mask]=sol(s[mask])*math.exp(scale-line.logscale)/line.core[0]
            N=max(512,32*self.M);theta=2*np.pi*np.arange(N)/N;er=np.c_[np.cos(theta),np.sin(theta),np.zeros(N)];et=np.c_[-np.sin(theta),np.cos(theta),np.zeros(N)]
            first=np.cos(3*theta)[:,None]*er-np.sin(3*theta)[:,None]*et/3;shape=fg[0,:,None,None]*first[None,:,:];shape[:,:,2]+=fg[1,:,None]*np.cos(3*theta)[None,:]
            p=np.zeros(self.M);self.initial(p);B,_,_=f.basis(N);old=old_geo(f,s,N);ref=f.geo(s,N);y=f.project(shape-(ref['pos']-old['pos'])/self.q,B)
            y+=(-y[:,0])[:,None]*np.maximum(0,1-s/(f.Tu/2))[None,:]**3
            return t,y,p
    return RefBVP
