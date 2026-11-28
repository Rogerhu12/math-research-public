#!/usr/bin/env python3
"""Physical positions on the same fixed meridian, with analytical principal-curvature derivatives in the XYZ update."""
import argparse,importlib.util,json,os
from pathlib import Path
for name in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[name]='1'
import numpy as np
from scipy.linalg import solve
path=Path(__file__).with_name('2ecf-r262-m2-low-cap-physical-continuation.py');spec=importlib.util.spec_from_file_location('r262_physical',path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);dot=m.base.dot

def curve(J):
    p,v,u,a,b,c=J.swapaxes(0,1);N=np.cross(v,u);ar=np.linalg.norm(N,axis=-1);N/=ar[...,None];E=dot(v,v);F=dot(v,u);rE=np.sqrt(E);l,mm,n=dot(N,a),dot(N,b),dot(N,c)
    p11=l/E;p12=(E*mm-F*l)/(E*ar);p22=(F*F*l/E-2*F*mm+E*n)/ar**2
    phase=.5*np.arctan2(2*p12,p11-p22);t=(p11+p22)/2;gap=np.hypot((p11-p22)/2,p12);pos=t>=0;k=np.where(pos,t+gap,t-gap)
    cx=np.where(pos,np.cos(phase),-np.sin(phase));cy=np.where(pos,np.sin(phase),np.cos(phase));x=cx/rE-cy*F/(rE*ar);y=cy*rE/ar
    wx=x[...,None];wy=y[...,None];D=wx*v+wy*u;A=wx**2*a+2*wx*wy*b+wy**2*c-k[...,None]*N
    fac=2*k[...,None]*D;cv=np.cross(u,A)/ar[...,None]-wx*fac;cu=np.cross(A,v)/ar[...,None]-wy*fac
    return k,(cv,cu,wx**2*N,2*wx*wy*N,wy**2*N)
def step(g,x,mu,guide,reg,power):
    J=g.field(x);V,U=J[:,1],J[:,2];R=g.bb;E,F,G=dot(V,V)-1,dot(V,U)/R,dot(U,U)/R**2-1;er=abs(E+G)/2+np.hypot((E-G)/2,F);K,dK=curve(J);kp=np.maximum(abs(K)-guide,0);n=x.size;H=np.zeros((n,n));rhs=np.zeros(n);ks=max(.1,float(kp.max()));peak=er.max()
    for i in range(len(g.z)):
        ids=np.nonzero(abs(g.B[0][i])+abs(g.B[1][i])+abs(g.B[2][i])>1e-15)[0]
        if not len(ids):continue
        q=g.B[0][i,ids];s=g.B[1][i,ids];t=g.B[2][i,ids];rr=R[i,:,None,None];inner=lambda V,j:np.einsum('uc,uac->ua',V,g.ang[j]);ix=(ids[:,None]*g.na+np.arange(g.na)).ravel()
        jac=np.stack([2*s[None,:,None]*inner(V[i],0)[:,None,:],np.sqrt(2)/rr*(s[None,:,None]*inner(U[i],0)[:,None,:]+q[None,:,None]*inner(V[i],1)[:,None,:]),2*q[None,:,None]*inner(U[i],1)[:,None,:]/rr**2],axis=1);weight=np.sqrt(.03+(er[i]/peak)**power);j=(jac*weight[:,None,None,None]).reshape(-1,len(ix));r=(weight[:,None]*np.stack([E[i],np.sqrt(2)*F[i],G[i]],axis=-1)).ravel();hh=j.T@j;vv=j.T@r
        active=np.where(kp[i]>0)[0]
        if len(active):
            kk=sum(rad[None,:,None]*np.einsum('uc,uac->ua',v[i,active],g.ang[order,active])[:,None,:] for v,rad,order in zip(dK,(s,q,t,s,q),(0,1,0,1,2)));w=mu*np.sqrt(.1+(kp[i,active]/ks)**power);j=(w[:,None,None]*kk).reshape(len(active),-1);r=w*np.sign(K[i,active])*kp[i,active];hh+=j.T@j;vv+=j.T@r
        H[np.ix_(ix,ix)]+=hh;rhs[ix]+=vv
    scale=np.maximum(np.sqrt(np.diag(H)),1e-13);dx=solve(H/scale[:,None]/scale[None,:]+reg*np.eye(n),-rhs/scale,assume_a='pos')/scale;return dx.reshape(x.shape)
def screen(src,x,eps,sp,mo,guide):
    ids=np.where(src.tail['r']<=src.rb[0]+1e-14)[0];rows=src.original(ids);u=np.arange(48)*np.pi/48
    # Reflection parity gives [0,pi); include both coordinate axes explicitly.
    values=[]
    for ii in range(0,len(rows),96):
        gg=m.Fit(src,rows[ii:ii+96],u,eps,sp,mo);J=gg.field(x);K,_=curve(J);V,U=J[:,1],J[:,2];E,F,G=dot(V,V)-1,dot(V,U)/gg.bb,dot(U,U)/gg.bb**2-1
        M=abs(E+G)/2+np.hypot((E-G)/2,F);values.append(np.column_stack([abs(K).max(axis=1),M.max(axis=1)]))
    v=np.vstack(values);lv=src.tail['labels'][ids,:2].astype(int);selected=set();km=v[:,0].max();em=v[:,1].max()
    for j,bound in ((0,min(guide*.9,km*.85)),(1,em*.75)):
        hit=np.flatnonzero(v[:,j]>=bound);pairs=np.unique(lv[hit],axis=0)
        for n,k in pairs:
            jj=hit[(lv[hit,0]==n)&(lv[hit,1]==k)];order=jj[np.argsort(v[jj,j])[-4:]];selected.update(ids[order].tolist())
    ii=np.argmax(v[:,0]);return np.array(sorted(selected),dtype=int),dict(maxCurvature=float(km),maxMetric=float(em),active=len(selected),worstLabel=src.tail['labels'][ids[ii]].tolist(),worstPhysicalRadius=float(src.tail['r'][ids[ii]]))

def stadium_center(R,eps,u,p,mix):
    from math import comb
    from scipy.optimize import brentq
    j=np.arange(1,p+1);modes=2*j;c=np.array([2*(-1)**int(k)*comb(2*p,p-int(k))/comb(2*p,p) for k in j]);b=c/(1-modes**2);b=b/b[::2].sum();b[0]=mix*b[0]+1-mix;b[1:]*=mix;b*=eps;rho=b*(1-modes**2)
    lower=R-(1-mix)*3*eps-mix*eps/(c/(1-modes**2))[::2].sum()
    if lower<=0:raise ValueError('The exact convex radius sufficient bound is nonpositive')
    def raw(ph):
        a=ph[:,None]*modes;co=np.cos(a);si=np.sin(a);return R*ph+si@(rho/modes),R+co@rho,R+co@b,-si@(b*modes)
    ph=u.copy()
    for it in range(18):
        val,rr,_,_=raw(ph);step=np.clip((val-R*u)/rr,-.55,.55);ph-=step
    val,rr,h,dh=raw(ph)
    for i in np.flatnonzero(abs(val-R*u)>2e-13):ph[i]=brentq(lambda th:raw(np.array([th]))[0][0]-R*u[i],-2*np.pi,4*np.pi)
    val,rr,h,dh=raw(ph);assert np.max(abs(val-R*u))<3e-12
    N=np.stack([np.cos(ph),np.sin(ph),0*u],axis=-1);T=np.stack([-np.sin(ph),np.cos(ph),0*u],axis=-1)
    return np.stack([h[:,None]*N+dh[:,None]*T,R*T,-R**2/rr[:,None]*N])

def main():
    p=argparse.ArgumentParser()
    for k in ('meridian','buffer','tail-table','out'):p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--parent',type=Path);p.add_argument('--spans',type=int,default=32);p.add_argument('--modes',type=int,default=8);p.add_argument('--vertical-scale',type=float,default=1.);p.add_argument('--horizontal-scale',type=float,default=1.);p.add_argument('--index',type=int,default=0);p.add_argument('--epsilon',required=True,type=float);p.add_argument('--steps',type=int,default=14);p.add_argument('--guide',type=float,default=9.65);p.add_argument('--mu',type=float,default=.018);p.add_argument('--train-radial',type=int,default=222);p.add_argument('--train-angular',type=int,default=104);p.add_argument('--stadium-p',type=int,default=32);p.add_argument('--stadium-mix',type=float,required=True);a=p.parse_args();m.support=lambda R,eps,u:stadium_center(R,eps,u,a.stadium_p,a.stadium_mix);src=m.Source(a);sourceJet=m.jet
    def scaledJet(rows,u,eps,linear=True):
        v=rows.copy();v[:,[7,9,11]]*=a.horizontal_scale;v[:,[8,10,12]]*=a.vertical_scale;return sourceJet(v,u,eps,linear)
    m.jet=scaledJet
    if a.parent:
        d=json.loads(a.parent.read_bytes());sp,mo=d['spans'],d['modes'];x=np.array(d['xyz'])*(a.epsilon/d['epsilon'])**2
    else:
        sp,mo=a.spans,a.modes;x=np.zeros((sp-1,3*mo));d={}
    d.update(meridianSHA256=m.base.sha(a.meridian),bufferSHA256=m.base.sha(a.buffer),tableSHA256=m.base.sha(a.tail_table),index=a.index,centralRadius=src.R,cutS=src.S,materialT=src.T,cutHeight=src.shift,physicalCuffHeight=float(src.original(np.array([0]))[0,2]),cutHeightGain=src.cutGain,correctedCoasts=src.co.tolist(),fixedNewG=True,spans=sp,modes=mo,horizontalLinearScale=a.horizontal_scale,verticalLinearScale=a.vertical_scale)
    fit=lambda n,k,shift:m.Fit(src,*src.grid(n,k,shift),a.epsilon,sp,mo);rawRows,angles=src.grid(a.train_radial,a.train_angular,False);extra=set();screens=[]
    def active():
        idx,z=screen(src,x,a.epsilon,sp,mo,a.guide);extra.update(idx.tolist());screens.append(z);print('native active',z,flush=True);return m.Fit(src,np.vstack([rawRows,src.original(np.array(sorted(extra),dtype=int))]),angles,a.epsilon,sp,mo)
    g=active();hist=[g.metrics(x)];steps=[]
    def merit(z):return z['metric']+a.mu*max(0,z['curvature']-a.guide)
    print('initial',hist[0],flush=True)
    for i in range(a.steps):
        if i and i%5==0:g=active()
        old=g.metrics(x);ok=False
        for power,reg in [(2,1e-6),(4,2e-5),(1,.0008),(6,.001),(2,.05)]:
            dx=step(g,x,a.mu,a.guide,reg,power)
            for s in (1,.5,.25,.125,.0625,.03125,.015625):
                z=g.metrics(x+s*dx)
                if merit(z)<merit(old)*(1-5e-6):
                    x+=s*dx;hist.append(z);steps.append(dict(power=power,reg=reg,scale=s));print('accepted',i,z,flush=True);ok=True;break
            if ok:break
        if not ok:break
    obs=[]
    for aa in [(407,192,False),(397,225,True)]:
        gg=fit(*aa);v=gg.metrics(x);JJ=gg.field(x);K,_=curve(JJ);idx=np.unravel_index(np.argmax(abs(K)),K.shape);zs=float(gg.z[idx[0]]);obs.append(dict(radial=len(gg.z),angular=len(gg.t),actual=v,sampledMaxNorm=float(np.linalg.norm(JJ[:,0],axis=-1).max()),sampledMaxAbsX=float(abs(JJ[:,0,: ,0]).max()),sampledMaxAbsY=float(abs(JJ[:,0,:,1]).max()),sampledUpperHeightRange=[float(JJ[:,0,:,2].min()),float(JJ[:,0,:,2].max())],curvatureLocation=[zs,float(gg.t[idx[1]])]));print('observed',obs[-1],flush=True)
    inner=src.original(np.where(src.tail['r']<=src.rb[0]+1e-14)[0]);deep=[]
    for ii in range(0,len(inner),48):
        gg=m.Fit(src,inner[ii:ii+48],np.pi/120+np.arange(120)*2*np.pi/120,a.epsilon,sp,mo);deep.append(gg.metrics(x))
    result={k:v for k,v in d.items() if k not in ('xyz','history','steps','observers','deepObserver')};result.update(schema='same-fixed-physical-m2-meridian-and-exact-central-support-principal-response-v1',epsilon=a.epsilon,centralHalfWidthDifference=2*a.epsilon,pureSecondModeRadiusReference=src.R-3*a.epsilon,stadiumPower=a.stadium_p,stadiumMix=a.stadium_mix,entrySHA256=m.base.sha(__file__),nativeSelection=screens,previousCompleteFieldSHA256=m.base.sha(a.parent) if a.parent else None,guide=a.guide,mu=a.mu,xyz=x.tolist(),history=hist,steps=steps,observers=obs,deepObserver=dict(rawRadial=len(inner),angular=120,metric=max(z['metric'] for z in deep),curvature=max(z['curvature'] for z in deep)))
    result.pop('newExactSupportRadiusLower',None)
    with a.out.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
if __name__=='__main__':main()
