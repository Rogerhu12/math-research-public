#!/usr/bin/env python3
"""Full physical solver releasing the central support shape at fixed measured support gain, with exact true-arclength shape derivatives."""
import argparse,json,importlib.util,os
from pathlib import Path
for k in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[k]='1'
import numpy as np
from scipy.linalg import solve
from scipy.interpolate import BSpline
HERE=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('minkowski_original_source',HERE/'2ecf-r262-minkowski-physical-continuation.py');base=importlib.util.module_from_spec(s);s.loader.exec_module(base)
def directions(t,ms):
    lam=(1-np.array([1,.5,-.5,-1,-.5,.5])[ms%6])/1.5
    x=t[:,None];m=ms[None,:];c=np.cos(x*m);ss=np.sin(x*m);c2=np.cos(2*x);s2=np.sin(2*x)
    h=c-c2*lam;hp=-m*ss+2*s2*lam;rad=(1-m*m)*c+3*c2*lam
    drad=-(1-m*m)*m*ss-6*s2*lam
    integ=ss/m-s2*lam/2;radint=(1-m*m)*ss/m+3*s2*lam/2
    return h,hp,rad,drad,integ,radint
class Port:
    def __init__(self,cc,eta,th,ms):
        self.cc=cc;self.eta=eta;self.th=th;self.u=cc.arc(th);self.ms=ms
        self.v=cc.native(th,0.);self.t0=np.linalg.norm(self.v[1],axis=1);self.t00=base.dot(self.v[1],self.v[2])/self.t0;self.last=th.copy()
    def evaluate(self,q,derivative=False):
        cc=self.cc;th=self.last.copy()
        def parts(th):
            p,v,a=cc.native(th,self.eta);spd=np.linalg.norm(v,axis=1);T=v/spd[:,None];N=np.c_[T[:,1],-T[:,0],0*spd]
            phi=np.arctan2(N[:,1],N[:,0]);phi+=2*np.pi*np.rint((th-phi)/(2*np.pi))
            w=base.xy_det(v,a)/spd**2
            return p,v,a,spd,T,N,w,directions(phi,self.ms)
        for i in range(15):
            p,v,a,spd,T,N,w,(h,hp,rad,drad,I,Ir)=parts(th);rr=spd/w+rad@q
            if rr.min()<=.02:raise ValueError('True central support curve lost a positive curvature radius at a sampled point')
            res=cc.native(th,self.eta,True)+Ir@q-self.u
            if abs(res).max()<3e-14:break
            th=np.clip(th-res/(rr*w),0,2*np.pi)
        if abs(res).max()>2e-12:raise ValueError('True material inverse did not settle')
        self.last=th
        # At fixed material u, new unit tangent is T, dT/du=-N/radius.
        pp=p+(h@q)[:,None]*N+(hp@q)[:,None]*T
        jets=np.array([pp,T*self.t0[:,None],T*self.t00[:,None]-N*(self.t0**2/rr)[:,None]])-np.asarray(self.v)
        if not derivative:return jets
        d0=h[:,:,None]*N[:,None,:]-I[:,:,None]*T[:,None,:]
        d1=((hp+I)*(self.t0/rr)[:,None])[:,:,None]*N[:,None,:]
        return jets,d0,d1
class Fit:
    def __init__(self,src,old,a):
        self.core=g=base.Grid(src,old,a.eta,a.spans,a.modes);self.ms=np.arange(3,a.support_max+1)
        self.port=Port(src.center,a.eta,g.t,self.ms);z,t,H,Hq,J,bb=old
        self.H=[v[:,0] for v in g.scales([base.polynomial(z,j)[:,None] for j in range(3)],H,Hq)]
    def change(self,q,der=False):
        v=self.port.evaluate(q,der)
        if der:jets,d0,d1=v
        else:jets=v
        self.core.base=self.core.old+np.stack([self.H[i][:,None,None]*jets[j] for i,j in base.O],axis=1)
        if der:return d0,d1
    def observe(self,x,q):
        self.change(q);return self.core.metrics(x)
    def step(self,x,q,reg,power):
        g=self.core;d0,d1=self.change(q,True);J=g.field(x);v,u=J[:,1],J[:,2];rr=g.bb;nx=x.size
        nvar=nx+len(q);lhs=np.zeros((nvar,nvar));rhs=np.zeros(nvar)
        E,F,G=base.dot(v,v)-1,base.dot(v,u)/rr,base.dot(u,u)/rr**2-1
        M=abs(E+G)/2+np.hypot((E-G)/2,F);w=(.02+(M/(M.max()+1e-30))**power)**.5
        ind=np.arange(nx,nvar)
        for i in range(len(g.z)):
            ids=np.nonzero(abs(g.B[0][i])+abs(g.B[1][i])>1e-15)[0]
            b=g.B[0][i,ids];s=g.B[1][i,ids];n=len(g.t);r=rr[i,:,None]
            inner=lambda d,j:np.einsum('uc,uac->ua',d,g.ang[j])
            row=np.stack([2*s[None,:,None]*inner(v[i],0)[:,None,:],np.sqrt(2)/r[:,:,None]*(s[None,:,None]*inner(u[i],0)[:,None,:]+b[None,:,None]*inner(v[i],1)[:,None,:]),2*b[None,:,None]*inner(u[i],1)[:,None,:]/r[:,:,None]**2],axis=1).reshape(n,3,-1)
            qv=self.H[1][i]*d0;qu=self.H[0][i]*d1
            innerq=lambda V,U:np.einsum('uc,ujc->uj',V,U)
            qm=np.stack([2*innerq(v[i],qv),np.sqrt(2)/r*(innerq(u[i],qv)+innerq(v[i],qu)),2*innerq(u[i],qu)/r**2],axis=1)
            row=np.concatenate([row,qm],axis=-1);jac=(row*w[i,:,None,None]).reshape(3*n,-1);f=(w[i,:,None]*np.stack([E[i],np.sqrt(2)*F[i],G[i]],axis=-1)).ravel()
            ix=np.r_[(ids[:,None]*g.na+np.arange(g.na)).ravel(),ind];lhs[np.ix_(ix,ix)]+=jac.T@jac;rhs[ix]+=jac.T@f
        sc=np.maximum(np.sqrt(np.diag(lhs)),1e-13);step=solve(lhs/sc[:,None]/sc[None,:]+reg*np.eye(nvar),-rhs/sc,assume_a='pos')/sc
        return step[:nx].reshape(x.shape),step[nx:]
def refine(x,oldN,oldM,nr,modes):
    if nr%oldN or modes<oldM:raise ValueError('Space must nest')
    a=np.zeros((len(x),3*modes+2));j0=0;j1=0
    for d in (0,1,2):
        n=oldM+(d!=1);a[:,j1:j1+n]=x[:,j0:j0+n];j0+=n;j1+=modes+(d!=1)
    knots=np.r_[np.zeros(6),np.arange(1,oldN)/oldN,np.ones(6)]
    f=BSpline(knots,np.pad(a,((3,3),(0,0))),5)
    for t in np.arange(1,nr)/nr:
        if t not in knots:f=f.insert_knot(t)
    return f.c[3:-3]
def main():
    p=argparse.ArgumentParser()
    for k in ('scripts','data','grid','query-report','query-cache','field','output','parent'):p.add_argument('--'+k,required=True,type=Path)
    p.add_argument('--eta',type=float,required=True);p.add_argument('--spans',type=int,default=12);p.add_argument('--modes',type=int,default=9);p.add_argument('--steps',type=int,default=6);p.add_argument('--support-max',type=int,default=10);a=p.parse_args()
    src=base.Source(a);par=json.loads(a.parent.read_bytes());ratio=a.eta/par['eta']
    make=lambda n,m,k,shift:Fit(src,src.old(n,m,k,shift),a)
    fit=make(108,49,152,False);x=ratio*refine(np.array(par['xyz']),par['spans'],par['modes'],a.spans,a.modes)
    q=np.zeros(a.support_max-2);orig=np.array(par.get('support',[]));q[:len(orig)]=ratio*orig
    obs=[fit.observe(x,q)];hist=[];print('start',obs[-1],flush=True)
    for i in range(a.steps):
        old=obs[-1];ok=False
        for reg in [.000001,.00005,.002]:
            dx,dq=fit.step(x,q,reg,min(4,1+i*.6))
            for sc in (1,.5,.25,.125,.0625):
                try:v=fit.observe(x+sc*dx,q+sc*dq)
                except ValueError:continue
                if v['metric']<old['metric']*(1-1e-5) and v['curvature']<max(10.15,old['curvature']+.01):
                    x+=sc*dx;q+=sc*dq;obs.append(v);hist.append(dict(scale=sc,reg=reg));ok=True;print('accepted',i,v,'sup',q,flush=True);break
            if ok:break
        if not ok:break
    res=[]
    for c in [(151,71,211,False),(128,59,257,True)]:
        o=make(*c);res.append(dict(radial=len(o.core.z),angular=len(o.core.t),actual=o.observe(x,q),original=o.core.metrics(x,True)));print('ind',res[-1],flush=True)
    rep=dict(schema='R262-full-integer-correction-free-true-support-at-fixed-held-direction-difference-v1',entrySHA256=base.sha(__file__),sourceBaseSHA=base.sha(Path(base.__file__)),sourceFieldSHA256=base.sha(a.field),parentSHA256=base.sha(a.parent),eta=a.eta,spans=a.spans,modes=a.modes,xyz=x.tolist(),support=q.tolist(),training=obs,history=hist,observers=res,originalMetricFrozen=True)
    with a.output.open('x') as f:json.dump(rep,f,indent=2);f.write('\n')
if __name__=='__main__':main()
