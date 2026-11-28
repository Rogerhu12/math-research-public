#!/usr/bin/env python3
"""Real two-ended small-gap continuation from an exact mixed-Gaussian-curvature round surface."""
import argparse
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
for q in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[q]='1'
import numpy as np
from scipy.interpolate import BSpline
from scipy.special import ellipe,ellipeinc
from scipy.linalg import solve
from numpy.polynomial.legendre import leggauss

L=.4;Z=.51;cut=.8
O=((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))
HP=np.array([[1,0,0,-10,15,-6],[0,1,0,-6,8,-3],[0,0,.5,-1.5,1.5,-.5],[0,0,0,10,-15,6],[0,0,0,-4,7,-3],[0,0,0,.5,-1,.5]])


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,name):
    s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def bump(x,d):
    on=(x>=0)&(x<=1);t=np.clip(x,0,1)
    v=64*t**3*(1-t)**3 if d==0 else 192*t*t*(1-t)**2*(1-2*t)
    return np.where(on,v,0.)
def phase(t,d=0):
    return (np.pi/2*(t**3*(10+t*(-15+6*t)))-.035*bump(4*t,0)+.035*bump(4*(1-t),0) if d==0 else
            np.pi/2*30*t*t*(1-t)**2-.14*bump(4*t,1)-.14*bump(4*(1-t),1))
GX,GW=leggauss(32);GX=(GX+1)/2;GW/=2
def integrate(t,func):
    t=np.asarray(t);res=np.zeros_like(t,dtype=float)
    for l,r in ((0,.25),(.25,.75),(.75,1)):
        a=np.minimum(r,np.maximum(l,t));res+=(a-l)*np.sum(func(phase(l+(a-l)[...,None]*GX))*GW,axis=-1)
    return res
I0=float(integrate(1.,np.sin));R0=cut+L*I0;central=Z-L*I0
def round_curve(t):
    ph=phase(t);rate=phase(t,1)/L
    return (R0-L*integrate(t,np.sin),central+L*integrate(t,np.cos),-np.sin(ph),np.cos(ph),-rate*np.cos(ph),-rate*np.sin(ph))
def hermite(t):
    v=[]
    for j in range(3):
        ds=np.arange(j,6);pow=np.stack([t**(d-j)*(math.factorial(d)//math.factorial(d-j)) for d in ds],axis=1)
        v.append((pow@HP[:,ds].T)*L**(np.arange(6)%3-j))
    return v
def ellipse(gap,u):
    a,b=R0+gap/2,R0-gap/2;m=1-(b/a)**2;radius=2*a*ellipe(m)/np.pi
    th=u.copy()
    for it in range(7):
        v=ellipeinc(th+np.pi/2,m)-ellipe(m);spd=np.hypot(a*np.sin(th),b*np.cos(th));th-=(a*v-radius*u)/spd
    c,s=np.cos(th),np.sin(th);spd=np.hypot(a*s,b*c);tp=radius/spd;tpp=-radius*radius*(a*a-b*b)*s*c/spd**4
    zero=0*u
    return radius,np.stack([np.stack(q,axis=-1) for q in ((a*c,b*s,zero),(-a*s*tp,b*c*tp,zero),(-a*c*tp**2-a*s*tpp,-b*s*tp**2+b*c*tpp,zero))])


class Turn:
    def __init__(self,a,gap,t,u):
        self.t=t;self.u=u;self.gap=gap;self.nu=len(u);self.n=len(t)
        self.m=a.modes;self.kw=a.curvature_weight;self.kt=a.curvature_guide
        self.channels=[(d,k) for d in range(3) for k in (range(1,2*self.m+1,2) if d<2 else range(0,2*self.m,2))]
        self.nc=len(self.channels)
        knots=np.r_[np.zeros(6),np.arange(1,a.spans)/a.spans,np.ones(6)]
        basis=BSpline(knots,np.eye(len(knots)-6)[:,3:-3],5,extrapolate=False)
        self.B=[basis(t,j)/L**j for j in range(3)];self.nr=self.B[0].shape[1]
        self.H=np.zeros((3,len(u),self.nc,3))
        for k,(d,m) in enumerate(self.channels):
            c,s=np.cos(m*u),np.sin(m*u)
            for j,w in enumerate(((c,-m*s,-m*m*c) if d!=1 else (s,m*c,-m*m*s))):self.H[j,:,k,d]=w
        self.hw=hermite(t);E,ell=ellipse(gap,u);self.ell=E
        c,s=np.cos(u),np.sin(u);v0=np.stack([np.stack(k,axis=-1) for k in ((c,s,0*u),(-s,c,0*u),(-c,-s,0*u))]);vert=np.zeros_like(v0);vert[0,:,2]=1.
        r,z,rs,zs,rss,zss=round_curve(t)
        self.r0=r+(E-R0)*self.hw[0][:,0];self.r0s=rs+(E-R0)*self.hw[1][:,0];self.r0ss=rss+(E-R0)*self.hw[2][:,0]
        self.base=np.stack([r1[:,None,None]*v0[j]+z1[:,None,None]*vert[j]+self.hw[i][:,0,None,None]*(ell[j]-R0*v0[j]) for (i,j),(r1,z1) in zip(O,((r,z),(rs,zs),(r,z),(rss,zss),(rs,zs),(r,z)))],axis=1)
        self.warm=a.warm
        zero=self.warm.developed_tail_port(0.,Z,u,cut)
        self.zero=np.array([[zero[key+'u'*j] for j in range(3)] for key in ('P','V','A')])
        self.root=a.helper
    def right(self,amp):
        pr=self.warm.developed_tail_port(amp,Z,self.u,cut)
        right=np.array([[pr[key+'u'*j] for j in range(3)] for key in ('P','V','A')])-self.zero
        return np.stack([np.einsum('nl,lud->nud',self.hw[i][:,3:],right[:,j]) for i,j in O],axis=1)
    def field(self,x,y,amp):
        x=x.reshape(self.nr,self.nc);raw=self.base+self.right(amp)
        return raw+np.stack([np.einsum('nc,ucd->nud',self.B[i]@x,self.H[j],optimize=True) for i,j in O],axis=1),self.r0*np.exp(self.B[0]@y)
    def values(self,x,y,amp):
        j,r=self.field(x,y,amp);E,K,A=self.root.metrics(j,r)
        ag=self.B[0]@y;ags=self.B[1]@y;agss=self.B[2]@y
        Kg=-(self.r0ss/self.r0+2*self.r0s/self.r0*ags+agss+ags**2)
        ij=np.unravel_index(np.argmax(E),E.shape);ik=np.unravel_index(np.argmax(K),K.shape);neg=np.argmin(Kg)
        soft=.30*np.logaddexp(0.,(K-self.kt)/.30)
        return dict(merit=float(np.mean(E**4)**.25+self.kw*np.sqrt(np.mean(soft**2))+.013*max(0.,K.max()-9.55)),metric=float(E[ij]),curvature=float(K[ik]),area=float(A.min()),rms=float(np.sqrt(np.mean(E*E))),
              fourthMean=float(np.mean(E**4)),metricAt=[float(self.t[ij[0]]),float(self.u[ij[1]])],
              curvatureAt=[float(self.t[ik[0]]),float(self.u[ik[1]])],gMinGaussian=float(Kg[neg]),gMinGaussianAt=float(self.t[neg]),amp=float(amp))
    def iterate(self,x,y,amp,joint,damping,power):
        J,r=self.field(x,y,amp);P,V,U,A,B,C=J.swapaxes(0,1);d=lambda v,w:np.sum(v*w,axis=-1)
        E=d(V,V);F=d(V,U);G=d(U,U);rr=r[:,None];err=abs(E+G/rr**2-2)/2+np.hypot((E-G/rr**2)/2,F/rr)
        w=np.sqrt(0.015+(err/np.maximum(err.max(),1e-14))**power)
        width=self.nc+(1 if joint else 0);N=self.nr*width+(1 if joint else 0);H=np.zeros((N,N));g=np.zeros(N)
        if joint:
            delta=1e-5
            plus=self.right(amp+delta);minus=self.right(amp-delta);da=((plus-minus)/(2*delta)).swapaxes(0,1)
            ca=np.stack([2*d(V,da[1]),np.sqrt(2)*(d(U,da[1])+d(V,da[2]))/rr,2*d(U,da[2])/rr**2],axis=2)
        # Both eigenvalues of the ACTUAL induced second form in an orthonormal tangent basis.
        normal=np.cross(V,U);area=np.linalg.norm(normal,axis=-1);normal/=area[...,None]
        e=np.sqrt(E);t1=1/e;t2=-F/(e*area);t3=e/area
        II0=d(normal,A);II1=d(normal,B);II2=d(normal,C)
        curv=np.empty((*E.shape,2,2));curv[...,0,0]=t1*t1*II0
        curv[...,0,1]=curv[...,1,0]=t1*(t2*II0+t3*II1)
        curv[...,1,1]=t2*t2*II0+2*t2*t3*II1+t3*t3*II2
        eig,dirs=np.linalg.eigh(curv);rad=t1[...,None]*dirs[...,0,:]+t2[...,None]*dirs[...,1,:]
        ang=t3[...,None]*dirs[...,1,:]
        dualS=(G[...,None]*V-F[...,None]*U)/area[...,None]**2
        dualU=(E[...,None]*U-F[...,None]*V)/area[...,None]**2
        for n in range(len(self.t)):
            ix=np.nonzero((np.abs(self.B[0][n])+np.abs(self.B[1][n]))>0)[0]
            if len(ix)==0:continue
            v,u=V[n],U[n];rs=r[n];bv=self.B[0][n,ix];bs=self.B[1][n,ix];row=np.empty((self.nu,3,len(ix),width))
            inner=lambda p,j:np.einsum('ud,ucd->uc',p,self.H[j])
            row[:,0,:,:self.nc]=2*inner(v,0)[:,None,:]*bs[None,:,None]
            row[:,1,:,:self.nc]=np.sqrt(2)*(inner(u,0)[:,None,:]*bs[None,:,None]+inner(v,1)[:,None,:]*bv[None,:,None])/rs
            row[:,2,:,:self.nc]=2*inner(u,1)[:,None,:]*bv[None,:,None]/rs**2
            if joint:
                row[:,0,:,-1]=0;row[:,1,:,-1]=-np.sqrt(2)*(F[n]/rs)[:,None]*bv;row[:,2,:,-1]=-2*(G[n]/rs**2)[:,None]*bv
            row=row.reshape(self.nu,3,-1);ids=(ix[:,None]*width+np.arange(width)).ravel()
            if joint:row=np.concatenate([row,ca[n,:,:,None]],axis=-1);ids=np.r_[ids,N-1]
            jac=(row*w[n,:,None,None]).reshape(self.nu*3,-1);rhs=np.stack([E[n]-1,np.sqrt(2)*F[n]/rs,G[n]/rs**2-1],axis=1)*w[n,:,None]
            H[np.ix_(ids,ids)]+=jac.T@jac;g[ids]+=jac.T@rhs.ravel()
            br=self.B[2][n,ix]
            for eigen in (0,1):
                k=eig[n,:,eigen];ts=rad[n,:,eigen];tu=ang[n,:,eigen]
                b1=(abs(k)-self.kt)/.30
                sel=b1>-11
                if not np.any(sel):continue
                # Differentiate N dot X_tt - k times the true Gram, holding only the
                # normalized generalized eigen-direction fixed at this physical point.
                NN=normal[n];acc=ts[:,None]**2*A[n]+2*(ts*tu)[:,None]*B[n]+tu[:,None]**2*C[n]
                T=ts[:,None]*v+tu[:,None]*u
                ds=-d(dualS[n],acc)[:,None]*NN-2*(k*ts)[:,None]*T
                du=-d(dualU[n],acc)[:,None]*NN-2*(k*tu)[:,None]*T
                block=np.zeros((self.nu,len(ix),width))
                h0=inner(NN,0);h1=inner(NN,1);h2=inner(NN,2)
                block[:,:,:self.nc]=(br[None,:,None]*(ts[:,None]**2*h0)[:,None,:]+
                  bs[None,:,None]*(2*(ts*tu)[:,None]*h1+inner(ds,0))[:,None,:]+
                  bv[None,:,None]*(tu[:,None]**2*h2+inner(du,1))[:,None,:])
                row=block.reshape(self.nu,-1)
                if joint:
                    ap=ts[:,None]**2*da[3,n]+2*(ts*tu)[:,None]*da[4,n]+tu[:,None]**2*da[5,n]
                    cols=d(NN,ap)+d(ds,da[1,n])+d(du,da[2,n]);row=np.c_[row,cols]
                mul=self.kw*np.sign(k[sel])/(1+np.exp(-b1[sel]))
                cj=row[sel]*mul[:,None];cv=self.kw*.30*np.logaddexp(0.,b1[sel])
                H[np.ix_(ids,ids)]+=cj.T@cj;g[ids]+=cj.T@cv
        scale=np.maximum(np.sqrt(np.diag(H)),1e-9);mat=H/scale[:,None]/scale[None,:]+damping*np.eye(N)
        step=solve(mat,-g/scale,assume_a='pos')/scale
        if joint:
            vec=step[:-1].reshape(self.nr,width);return vec[:,:-1].ravel(),vec[:,-1],step[-1]
        return step,np.zeros(self.nr),0.


def main():
    ap=argparse.ArgumentParser()
    for k in ('scripts','output'):ap.add_argument('--'+k,type=Path,required=True)
    ap.add_argument('--curvature-guide',type=float,default=8.65);ap.add_argument('--curvature-weight',type=float,default=.018);ap.add_argument('--gap',type=float,required=True);ap.add_argument('--parent',type=Path)
    ap.add_argument('--spans',type=int,default=18);ap.add_argument('--modes',type=int,default=6);ap.add_argument('--joint-steps',type=int,default=7);ap.add_argument('--fixed-steps',type=int,default=3)
    a=ap.parse_args();a.warm=load(a.scripts/'6a65-geometry-cauchy-unit-t-warm.py','round_original_R205')
    a.helper=load(a.scripts/'2ecf-strong-port-hermite-fourier-background-physical-W.py','round_measures')
    grid=lambda n,m,shift:(np.r_[0,(np.arange(n-1)+shift)/(n-1),1] if shift else np.linspace(0,1,n),2*np.pi*(np.arange(m)+shift)/m)
    t,u=grid(145,96,0.);train=Turn(a,a.gap,t,u)
    amp=.8*a.gap;x=np.zeros(train.nr*train.nc);y=np.zeros(train.nr)
    if a.parent:
        parent=json.loads(a.parent.read_bytes());ratio=a.gap/parent['gap']
        if parent['spans']!=a.spans or parent['modes']!=a.modes:raise ValueError('Parent space differs')
        x=ratio*np.array(parent['xyz']);y=ratio*np.array(parent['logRadius']);amp=ratio*parent['amp']
    initial=train.values(x,y,amp);history=[];peaks=[]
    print('start',a.gap,initial,flush=True)
    for phase_name,count in [('joint',a.joint_steps),('fixed',a.fixed_steps)]:
        damp=.00035
        for it in range(count):
            before=train.values(x,y,amp);success=False;power=min(3.0,1.2+it*.4)
            for attempt in range(3):
                dx,dy,di=train.iterate(x,y,amp,phase_name=='joint',damp,power)
                for al in [1.,.5,.25,.125,.0625,.03125]:
                    aa=amp+al*di
                    if not 0<=aa<=1.2:continue
                    nxt=train.values(x+al*dx,y+al*dy,aa)
                    good=(nxt['merit']<before['merit']*(1-1e-7) and nxt['curvature']<max(10.15,before['curvature']+.001)
                        and nxt['metric']<max(1.05*before['metric'],before['metric']+.001))
                    if good:
                        x+=al*dx;y+=al*dy;amp=aa;success=True
                        history.append(dict(stage=phase_name,it=it,scale=al,damping=damp,after=nxt))
                        print('actual',phase_name,it,al,nxt['metric'],nxt['curvature'],amp,flush=True)
                        damp=max(1e-9,damp*.5);break
                if success:break
                damp*=10
            if not success:break
        peaks.append(train.values(x,y,amp))
    obs=Turn(a,a.gap,*grid(257,192,0));ind=Turn(a,a.gap,*grid(234,256,.5))
    report=dict(schema='mixed-Gaussian-round-to-accurate-two-ended-full-small-gap-physical-continuation-v1',entrySHA256=sha(__file__),gap=a.gap,
        parentSHA256=sha(a.parent) if a.parent else None,actualCurvatureGuide=a.curvature_guide,actualCurvatureWeight=a.curvature_weight,spans=a.spans,modes=a.modes,amp=amp,xyz=x.tolist(),logRadius=y.tolist(),
        centralEllipseSemiaxes=[R0+a.gap/2,R0-a.gap/2],centralAngleArcRadius=train.ell,roundCentralRadius=R0,centralLength=central,cutHeight=Z,
        exactReferenceTurnLength='2/5',initial=initial,history=history,postJointTraining=peaks[0],finalTraining=peaks[-1],
        observer=obs.values(x,y,amp),independent=ind.values(x,y,amp),centralAndDevelopedTailMetricDefectExactlyZero=True,
        exactReferenceMixedGaussianCurvature=True,completeNonzeroGapExactIsometry=False)
    with a.output.open('x') as f:json.dump(report,f,indent=2);f.write('\n')
    print('final independent',report['independent'],flush=True)


if __name__=='__main__':main()
