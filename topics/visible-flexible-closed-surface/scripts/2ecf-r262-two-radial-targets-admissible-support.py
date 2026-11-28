#!/usr/bin/env python3
"""Physical bulk positions and two smooth radial metric factors on the R262 noncircular continuum, keeping the complete center fixed."""
import argparse,hashlib,importlib.util,json,os
from pathlib import Path
for k in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[k]='1'
import numpy as np
from scipy.linalg import solve
from scipy.interpolate import BSpline
HERE=Path(__file__).resolve().parent
def module(p,n):
    s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
free=module(HERE/'2ecf-r262-free-support-full-shape.py','r262_2radial_fit');base=free.base
class Grid:
    def __init__(self,src,old,a,q):
        ff=free.Fit(src,old,a);ff.change(q);self.g=g=ff.core;self.rb=a.radius_spans-1
        knot=np.r_[np.zeros(6),np.arange(1,a.radius_spans)/a.radius_spans,np.ones(6)]
        self.B=BSpline(knot,np.eye(len(knot)-6)[:,3:-3],5)(g.z);self.rb=self.B.shape[1]
    def vals(self,x,alpha,beta):
        g=self.g;J=g.field(x);u,v=J[:,1],J[:,2];a=np.exp(self.B@alpha)[:,None];b=np.exp(self.B@beta)[:,None]*g.bb
        E=base.dot(u,u)/a**2-1;F=base.dot(u,v)/(a*b);G=base.dot(v,v)/b**2-1
        er=abs(E+G)/2+np.hypot((E-G)/2,F);i=np.unravel_index(np.argmax(er),er.shape)
        r=g.metrics(x);r.update(metric=float(er[i]),rms=float(np.mean(er**2)**.5),point=[float(g.z[i[0]]),float(g.t[i[1]])],
                               maxAbsLogRadialSpeed=float(abs(self.B@alpha).max()),maxAbsLogAngularRadius=float(abs(self.B@beta).max()))
        r['areaRatioMin']=float((np.linalg.norm(np.cross(u,v),axis=-1)/(a*b)).min());return r
    def step(self,x,alpha,beta,reg,power,joint):
        g=self.g;J=g.field(x);v,u=J[:,1],J[:,2];aa=np.exp(self.B@alpha)[:,None];bb=np.exp(self.B@beta)[:,None]*g.bb
        E,F,G=base.dot(v,v)/aa**2-1,base.dot(v,u)/(aa*bb),base.dot(u,u)/bb**2-1
        M=abs(E+G)/2+np.hypot((E-G)/2,F);w=(.025+(M/M.max())**power)**.5;nx=x.size;nt=self.rb
        N=nx+2*nt if joint else nx;H=np.zeros((N,N));rhs=np.zeros(N)
        for i in range(len(g.z)):
            ix=np.nonzero(abs(g.B[0][i])+abs(g.B[1][i])>1e-15)[0];b=g.B[0][i,ix];s=g.B[1][i,ix]
            aa1=aa[i,0];bb1=bb[i,:,None,None];inner=lambda d,j:np.einsum('uc,uac->ua',d,g.ang[j])
            row=np.stack([2*s[None,:,None]*inner(v[i],0)[:,None,:]/aa1**2,
                np.sqrt(2)/(aa1*bb1)*(s[None,:,None]*inner(u[i],0)[:,None,:]+b[None,:,None]*inner(v[i],1)[:,None,:]),
                2*b[None,:,None]*inner(u[i],1)[:,None,:]/bb1**2],axis=1).reshape(len(g.t),3,-1)
            ids=(ix[:,None]*g.na+np.arange(g.na)).ravel()
            if joint:
                kr=np.nonzero(abs(self.B[i])>1e-15)[0];block=self.B[i,kr];zeros=np.zeros_like(F[i]);a=np.stack([-2*(1+E[i]),-np.sqrt(2)*F[i],zeros],axis=1);b=np.stack([zeros,-np.sqrt(2)*F[i],-2*(1+G[i])],axis=1)
                row=np.concatenate([row,a[:,:,None]*block,b[:,:,None]*block],axis=-1);ids=np.r_[ids,nx+kr,nx+nt+kr]
            if not len(ids):continue
            j=(row*w[i,:,None,None]).reshape(3*len(g.t),-1);r=(w[i,:,None]*np.stack([E[i],np.sqrt(2)*F[i],G[i]],axis=-1)).ravel()
            H[np.ix_(ids,ids)]+=j.T@j;rhs[ids]+=j.T@r
        scale=np.maximum(np.sqrt(np.diag(H)),1e-13);step=solve(H/scale[:,None]/scale[None,:]+reg*np.eye(N),-rhs/scale,assume_a='pos')/scale
        return step[:nx].reshape(x.shape),step[nx:nx+nt] if joint else np.zeros(nt),step[nx+nt:] if joint else np.zeros(nt)
def main():
    p=argparse.ArgumentParser()
    for k in ('scripts','data','grid','query-report','query-cache','field','output','parent'):p.add_argument('--'+k,required=True,type=Path)
    p.add_argument('--spans',type=int,default=24);p.add_argument('--modes',type=int,default=15);p.add_argument('--radius-spans',type=int,default=12);p.add_argument('--steps',type=int,default=8);p.add_argument('--fixed-steps',type=int,default=3)
    p.add_argument('--radial-bias',type=float,default=0.);p.add_argument('--eta',type=float);p.add_argument('--support-scale',type=float);a=p.parse_args();par=json.loads(a.parent.read_bytes());a.eta=a.eta if a.eta is not None else par['eta'];ratio=a.eta/par['eta']
    support_scale=ratio if a.support_scale is None else a.support_scale
    q=support_scale*np.array(par['support']);a.support_max=len(q)+2
    two=bool(par.get('widthConstraintSourceSHA256') or par.get('twoConstraints'))
    if two:free.directions=module(HERE/'2ecf-r262-fixed-width-free-support.py','r262_two_W_support').directions
    x=ratio*free.refine(np.array(par['xyz']),par['spans'],par['modes'],a.spans,a.modes)
    src=base.Source(a);make=lambda n,m,k,shift:Grid(src,src.old(n,m,k,shift),a,q)
    g=make(145,65,167,False);alpha=ratio*np.array(par.get('logSpeed',[0.]*g.rb));beta=ratio*np.array(par.get('logRadius',[0.]*g.rb))
    if a.radial_bias:alpha+=a.radial_bias*np.sin(np.linspace(-np.pi,np.pi,len(alpha)))**3
    obs=[g.vals(x,alpha,beta)];hist=[];print('start',obs[-1],flush=True)
    for joint,count in [(True,a.steps),(False,a.fixed_steps)]:
        for it in range(count):
            old=obs[-1];ok=False
            for reg in [.0000003,.00002,.001,.06]:
                dx,da,db=g.step(x,alpha,beta,reg,min(4,1+it*.45),joint)
                for st in (1,.5,.25,.125,.0625,.03125):
                    rr=g.vals(x+st*dx,alpha+st*da,beta+st*db)
                    if rr['metric']<old['metric']*(1-1e-6) and rr['curvature']<max(10.,old['curvature']+.01):
                        x+=st*dx;alpha+=st*da;beta+=st*db;obs.append(rr);hist.append(dict(joint=joint,reg=reg,step=st));ok=True;print('acc',joint,it,rr,flush=True);break
                if ok:break
            if not ok:break
    out=[]
    for c in [(201,82,241,False),(188,79,257,True)]:
        gg=make(*c);out.append(dict(radial=len(gg.g.z),angular=len(gg.g.t),actual=gg.vals(x,alpha,beta)));print('obs',out[-1],flush=True)
    rep=dict(schema='r262-variable-radial-speed-and-radius-full-polar-metric-v1',entrySHA256=base.sha(__file__),sourceFieldSHA256=base.sha(a.field),parentSHA256=base.sha(a.parent),eta=a.eta,spans=a.spans,modes=a.modes,radiusSpans=a.radius_spans,radialBias=a.radial_bias,supportScale=support_scale,twoConstraints=two,support=q.tolist(),xyz=x.tolist(),logSpeed=alpha.tolist(),logRadius=beta.tolist(),training=obs,history=hist,observers=out)
    with a.output.open('x') as f:json.dump(rep,f,indent=2);f.write('\n')
if __name__=='__main__':main()
