#!/usr/bin/env python3
"""Actual Cartesian correction of the complete enlarged-cuff input at fixed new g."""
import argparse,hashlib,importlib.util,json,os,time
from pathlib import Path
for k in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[k]='1'
import numpy as np
from scipy.interpolate import BSpline
from scipy.linalg import solve
def load(p,n):
    s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dot(a,b):return np.sum(a*b,axis=-1)
O=((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))

class Grid:
    def __init__(self,src,amb,old,spans,modes,start):
        z,t,H,Hq,J,bb=old;self.z=z;self.t=t;self.base,self.ambient=amb.transform(J)
        self.E0,self.bb=amb.target(z,bb);self.old=np.asarray(J,float)
        self.start=start;self.stop=1.
        k=np.r_[np.repeat(start,6),np.linspace(start,1,spans+1)[1:-1],np.ones(6)]
        b=BSpline(k,np.eye(len(k)-6)[:,3:-3],5,extrapolate=False)
        B=[np.nan_to_num(b(z,j),nan=0) for j in range(3)]
        self.B=[B[0],B[1]/(src.T*H[:,None]),B[2]/(src.T*H[:,None])**2-B[1]*Hq[:,None]/(src.T*H[:,None]**3)]
        self.nb=B[0].shape[1];channels=[(d,m) for d in range(3) for m in range(1 if d==1 else 0,modes+1)]
        self.na=len(channels);self.ang=np.zeros((3,len(t),self.na,3))
        for a,(d,m) in enumerate(channels):
            for j in range(3):
                self.ang[j,:,a,d]=m**j*np.cos(m*t+j*np.pi/2-(np.pi/2 if d==1 else 0))
    def field(self,x):
        return self.base+np.stack([np.einsum('na,uad->nud',self.B[i]@x,self.ang[j],optimize=True) for i,j in O],axis=1)
    def metric(self,x):
        J=self.field(x);P,S,U,SS,SU,UU=J.swapaxes(0,1);E=dot(S,S);F=dot(S,U);G=dot(U,U)
        e=E/self.E0[:,None]-1;f=F/(self.E0[:,None]**.5*self.bb);g=G/self.bb**2-1
        M=abs(e+g)/2+np.hypot((e-g)/2,f);N=np.cross(S,U);ar=np.linalg.norm(N,axis=-1);N/=ar[...,None]
        l,m,n=dot(N,SS),dot(N,SU),dot(N,UU);tr=(E*n-2*F*m+G*l)/ar**2
        K=abs(tr)/2+np.sqrt(np.maximum(0,tr*tr/4-(l*n-m*m)/ar**2))
        ind=np.unravel_index(M.argmax(),M.shape)
        return dict(metric=float(M.max()),rms=float(np.mean(M*M)**.5),cost=float(np.mean(e*e+2*f*f+g*g)),curvature=float(K.max()),minimumAreaRatio=float((ar/(np.sqrt(self.E0[:,None])*self.bb)).min()),minimumOutwardSupport=float((-dot(P,N)).min()),ballRadius=float(np.linalg.norm(P,axis=-1).max()),point=[float(self.z[ind[0]]),float(self.t[ind[1]])])
    def step(self,x,reg,power):
        J=self.field(x);v,u=J[:,1],J[:,2];rr=self.bb;nvar=x.size;lhs=np.zeros((nvar,nvar));rhs=np.zeros(nvar)
        E=dot(v,v)/self.E0[:,None]-1;F=dot(v,u)/(self.E0[:,None]**.5*rr);G=dot(u,u)/rr**2-1
        M=abs(E+G)/2+np.hypot((E-G)/2,F);w=(.03+(M/(M.max()+1e-30))**power)**.5
        for i in range(len(self.z)):
            ids=np.nonzero(abs(self.B[0][i])+abs(self.B[1][i])>1e-15)[0]
            if not len(ids):continue
            b=self.B[0][i,ids];s=self.B[1][i,ids];ee=self.E0[i]
            inner=lambda d,j:np.einsum('uc,uac->ua',d,self.ang[j])
            row=np.stack([2*s[None,:,None]*inner(v[i],0)[:,None,:]/ee,np.sqrt(2)/(ee**.5*rr[i,:,None,None])*(s[None,:,None]*inner(u[i],0)[:,None,:]+b[None,:,None]*inner(v[i],1)[:,None,:]),2*b[None,:,None]*inner(u[i],1)[:,None,:]/rr[i,:,None,None]**2],axis=1)
            jac=(row*w[i,:,None,None,None]).reshape(3*len(self.t),-1);f=(w[i,:,None]*np.stack([E[i],np.sqrt(2)*F[i],G[i]],axis=-1)).ravel()
            ix=(ids[:,None]*self.na+np.arange(self.na)).ravel();lhs[np.ix_(ix,ix)]+=jac.T@jac;rhs[ix]+=jac.T@f
        sc=np.maximum(np.sqrt(np.diag(lhs)),1e-12);A=lhs/sc[:,None]/sc[None,:]+reg*np.eye(nvar)
        return (solve(A,-rhs/sc,assume_a='pos')/sc).reshape(x.shape)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for k in ('scripts','data','grid','field','query-report','query-cache','ambient-source','output'):ap.add_argument('--'+k,type=Path,required=True)
    ap.add_argument('--spans',type=int,default=24);ap.add_argument('--modes',type=int,default=13);ap.add_argument('--steps',type=int,default=8)
    ap.add_argument('--parent',type=Path);a=ap.parse_args();assert not a.output.exists();start=time.monotonic()
    ar=load(a.ambient_source,'r280_ambient_solver');mo=load(a.scripts/'2ecf-r262-minkowski-physical-continuation.py','r280_original_solver')
    src=mo.Source(a);amb=ar.Ambient(src,'8/25','21/50');begin=(src.S-.20)/src.T
    def make(n,nt,N,shift):return Grid(src,amb,src.old(n,nt,N,shift),a.spans,a.modes,begin)
    g=make(80,160,160,False);x=np.zeros((g.nb,g.na))
    if a.parent:
        p=json.loads(a.parent.read_text());assert (a.spans,a.modes)==(p['spans'],p['modes']);x=np.asarray(p['xyz'])
    hist=[g.metric(x)];accept=[];print(json.dumps({'initial':hist[0],'variables':x.size,'start':begin}),flush=True)
    for i in range(a.steps):
        old=hist[-1];okay=False
        for reg in (3e-6,1e-4,.003,.05):
            dx=g.step(x,reg,min(4,i+1))
            for scale in (1,.5,.25,.125,.0625):
                trial=g.metric(x+scale*dx)
                if trial['metric']<old['metric']*(1-1e-4) and trial['curvature']<max(9.5,old['curvature']+.01):
                    x+=scale*dx;hist.append(trial);accept.append(dict(damping=reg,step=scale));okay=True;print(json.dumps({'accept':len(accept),'observation':trial}),flush=True);break
            if okay:break
        if not okay:break
    reports=[]
    for n,nt,N,shift in ((121,193,192,False),(108,181,233,True)):
        obs=make(n,nt,N,shift);row=dict(rows=len(obs.z),angles=len(obs.t),shift=shift,initial=obs.metric(np.zeros_like(x)),final=obs.metric(x));reports.append(row);print(json.dumps({'observer':row}),flush=True)
    packet=dict(schema='R262-enlarged-cuff-complete-C2-fixed-new-target-Cartesian-actual-correction-v1',scriptSHA256=sha(__file__),ambientSHA256=sha(a.ambient_source),originalFieldSHA256=sha(a.field),spans=a.spans,modes=a.modes,start=begin,xyz=x.tolist(),training=hist,accepted=accept,independent=reports,newFixedG=True,oldMetricOrReachInherited=False,originalCentralAndTrueNewCuffFixed=True,continuousNewMetricBound=False,newFieldEmbeddingInherited=False,seconds=time.monotonic()-start)
    a.output.write_text(json.dumps(packet,indent=2)+'\n');print(json.dumps({'output':str(a.output),'sha256':sha(a.output),'seconds':packet['seconds']}),flush=True)
if __name__=='__main__':main()
