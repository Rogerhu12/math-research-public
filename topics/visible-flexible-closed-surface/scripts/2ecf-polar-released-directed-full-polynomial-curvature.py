#!/usr/bin/env python3
"""All-angle directed principal-curvature positivity on exact physical Cartesian polynomial pieces."""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time
for h in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[h]='1'
import numpy as np
def module(p,n):
    sp=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sp);sys.modules[n]=m;sp.loader.exec_module(m);return m
here=Path(__file__).parent
shape=module(here/'2ecf-polar-released-exact-full-shape-enclosure.py','directed_curvature_phases')
def left_right(P):
    stages=[P]
    while len(stages[-1][0])>1:
        a,b=stages[-1]
        stages.append((np.nextafter((a[:-1]+a[1:])*.5,-np.inf),np.nextafter((b[:-1]+b[1:])*.5,np.inf)))
    return ((np.stack([r[0][0] for r in stages]),np.stack([r[1][0] for r in stages])),(np.stack([r[0][-1] for r in stages[::-1]]),np.stack([r[1][-1] for r in stages[::-1]])))
def pieces(a,K,hf):
    I=K.I;raw=np.load(a.field);r=raw['coeff'];kn=list(map(Q,raw['knots']));b,T=kn[0],kn[-1]
    state=json.load(a.state.open());sol=json.load(a.spatial.open())
    assert state['fieldSHA256']==shape.digest(a.field)==sol['sourceFieldSHA256'] and sol['sourceStateSHA256']==shape.digest(a.state)
    rf=Q(4,5)+Q(state['oldS'])-T;M=r.shape[2]-1
    x=sol['spans'];mm=sol['modes'];sk=[b]*6+[b+(T-b)*Q(i/x) for i in range(1,x)]+[T]*6
    aco=np.array(sol['coefficients']).reshape(3,x-1,mm+1).transpose(1,0,2).reshape(x-1,-1)
    ex=module(a.scripts/'2ecf-polar-c2-correction-bernstein-budget.py','true_curvature_exact_boehm');ins=module(a.scripts/'6a65-m12-local-bernstein-angular-metric-budget.py','true_curvature_insert')
    extr=ex.extract(sk,[[Q(v) for v in row] for row in aco],ins.insert_knot)
    W={}
    for l,r1,ww in extr:
        lo=np.zeros((6,M+1,3,2));hi=lo.copy()
        for j,ctr in enumerate(ww):
            for d in range(3):
                for ma in range(mm+1):
                    k=2*ma+int(d<2);im=int(d==1);v=ctr[d*(mm+1)+ma]*(-1 if im else 1)
                    lo[j,k,d,im]=np.nextafter(float(v),-np.inf);hi[j,k,d,im]=np.nextafter(float(v),np.inf)
        W[l,r1]=I(lo,hi)
    delta=Q(sol['raisedCuffDelta']);assert sol['transition']==[0.,1.]
    # The entire quintic raising profile has its exact Bernstein control (0,0,0,delta,delta,delta).
    la=np.zeros((6,M+1,3,2));la[3:,0,2,0]=float(delta);lift=I(la)
    for cell in range(a.start_cell,a.end_cell):
        l,r1=kn[cell:cell+2];h=I(r1-l);rr=np.stack([r[cell:cell+2].real,r[cell:cell+2].imag],axis=-1);vl=rr.copy();vu=rr.copy()
        if cell==len(kn)-2:
            vl[-1]=0;vu[-1]=0
            for d1,m,d,im,v in ((0,1,0,0,rf),(0,1,1,1,-rf),(0,0,2,0,Q(83,200)),(1,1,0,0,Q(-1)),(1,1,1,1,Q(1))):
                vl[-1,d1,m,d,im]=np.nextafter(float(v),-np.inf);vu[-1,d1,m,d,im]=np.nextafter(float(v),np.inf)
        V=I(vl,vu);P,Ps,Pss=V[0];R,Rs,Rss=V[1]
        ctrl=hf.parts(I,[P,P+h*Ps/5,P+2*h*Ps/5+h.square()*Pss/20,R-2*h*Rs/5+h.square()*Rss/20,R-h*Rs/5,R])
        br=sorted({l,r1,*[w for w in sk if l<w<r1]})
        for aa,bb in zip(br,br[1:]):
            kr=next(w for w in W if w[0]<=aa<bb<=w[1]);P=hf.section(I,ctrl,l,r1,aa,bb)+hf.section(I,W[kr],*kr,aa,bb)+hf.section(I,lift,b,T,aa,bb)
            Ps=5*(P[1:]-P[:-1])/I(bb-aa);Pss=4*(Ps[1:]-Ps[:-1])/I(bb-aa)
            yield cell,aa,bb,(P,Ps,Pss)
def padval(v,r):
    return (np.nextafter(v-r,-np.inf),np.nextafter(v+r,np.inf))
def centred(v):
    lo,hi=v;c=np.asarray(.5*(lo+hi),dtype=float);r=np.maximum(abs(lo-c),abs(hi-c))
    return c,np.asarray(np.nextafter(r,np.longdouble(np.inf)),dtype=float)*(1+1e-14)+1e-15
class Phase:
    def __init__(self,n,M):
        ph,e=shape.trig(n,M);self.phase=ph/shape.V;self.err=float(e)+1e-12;self.n=n
        self.wave=np.arange(M,dtype=float)[None,:,None]
    def vals(self,ctrl,p):
        re,er=centred((ctrl.lo[:,:,:,0],ctrl.hi[:,:,:,0]));im,ei=centred((ctrl.lo[:,:,:,1],ctrl.hi[:,:,:,1]))
        d,M,xyz=re.shape;values=[];radii=[]
        for o in range(p,p+3):
            m=self.wave**o
            x,y=[(re,im),(-im,re),(-re,-im),(im,-re)][o%4];mag=((abs(x)+abs(y)+er+ei)*m).sum(1)*(1+1e-12)+1e-14
            if o==p+2:
                second=mag;break
            mat=np.concatenate([x*m,y*m],axis=1).transpose(0,2,1).reshape(d*xyz,2*M)
            y1=(mat@self.phase).reshape(d,xyz,-1).transpose(0,2,1)
            rr=((er+ei)*m).sum(1)*(1+1e-12)+self.err*(mag+1)
            values.append(y1);radii.append(rr[:,None,:])
        radius=radii[0]+(abs(values[1])+radii[1])/self.n+second[:,None,:]/(2*self.n**2)
        return padval(values[0],radius*(1+1e-12)+1e-13)
def addition(a,b):return (np.nextafter(a[0]+b[0],-np.inf),np.nextafter(a[1]+b[1],np.inf))
def minus(a,b):return (np.nextafter(a[0]-b[1],-np.inf),np.nextafter(a[1]-b[0],np.inf))
def times(a,b):
    p=a[0]*b[0];q=a[0]*b[1];r=a[1]*b[0];s=a[1]*b[1]
    return (np.nextafter(np.minimum(np.minimum(p,q),np.minimum(r,s)),-np.inf),np.nextafter(np.maximum(np.maximum(p,q),np.maximum(r,s)),np.inf))
def square(a):
    l=np.maximum(0,np.maximum(a[0],-a[1]));r=np.maximum(abs(a[0]),abs(a[1]));return (np.maximum(0,np.nextafter(l*l,-np.inf)),np.nextafter(r*r,np.inf))
def dot(a,b):
    t=times(a,b);return (np.nextafter(np.sum(t[0],axis=-1)-2e-14*(1+np.sum(abs(t[0]),axis=-1)),-np.inf),np.nextafter(np.sum(t[1],axis=-1)+2e-14*(1+np.sum(abs(t[1]),axis=-1)),np.inf))
def cross(a,b):
    return minus(times((np.roll(a[0],-1,axis=-1),np.roll(a[1],-1,axis=-1)),(np.roll(b[0],1,axis=-1),np.roll(b[1],1,axis=-1))),times((np.roll(a[0],1,axis=-1),np.roll(a[1],1,axis=-1)),(np.roll(b[0],-1,axis=-1),np.roll(b[1],-1,axis=-1))))
def scale(a,k):return times(a,(k,k))
def check(pack,K):
    A,B,C,D,E=[(np.min(p[0],axis=0),np.max(p[1],axis=0)) for p in pack]
    N=cross(A,B);lo,hi=square(N);ww=(np.maximum(1e-200,np.sqrt(np.maximum(1e-297,np.sum(lo,axis=1)))*(1-3e-14)),np.sqrt(np.sum(hi,axis=1))*(1+3e-14))
    En=scale(dot(A,A),K);Fn=scale(dot(A,B),K);Gn=scale(dot(B,B),K)
    U=[times(dot(N,T),(1/ww[1]*(1-1e-14),1/ww[0]*(1+1e-14))) for T in (C,D,E)]
    good=ww[0]>.05;mr=np.full(len(good),np.inf)
    for op in [addition,minus]:
        aa=op(En,U[0]);bb=op(Fn,U[1]);cc=op(Gn,U[2])
        det=minus(times(aa,cc),square(bb))[0]
        good &= (aa[0]>0)&(cc[0]>0)&(det>0);mr=np.minimum(mr,det)
    return good,mr
def run(a):
    start=time.monotonic();K=module(a.scripts/'prefix-hull-kernel/m12-correlated-gram-interval-kernel.py','curvature_x87')
    hf=module(a.scripts/'2ecf-strong-hf-interior-continuous-projection.py','exact_curvature_hf')
    M=np.load(a.field)['coeff'].shape[2];ph=Phase(a.quarter_angles,M);kk=float(a.threshold);assert Q(kk)<=a.threshold or a.threshold>=Q(np.nextafter(kk,-np.inf))
    kk=np.nextafter(kk,-np.inf);assert Q(kk)<=a.threshold
    out=[];maxrad=a.radial_depth
    for i,l,r,(P,Ps,Pss) in pieces(a,K,hf):
        packs=[ph.vals(Ps,0),ph.vals(P,1),ph.vals(Pss,0),ph.vals(Ps,1),ph.vals(P,2)]
        residual=0;leaves=0;badangles=set();mindet=np.inf
        def walk(arr,indices,d):
            nonlocal residual,leaves,mindet
            good,det=check(arr,kk);leaves+=int(np.sum(good))
            if np.any(good):mindet=min(mindet,float(np.min(det[good])))
            if np.all(good):return
            ids=indices[~good]
            if d>=maxrad:
                residual+=len(ids);badangles.update(map(int,ids));return
            children=[left_right((p[0][:,~good,:],p[1][:,~good,:])) for p in arr]
            for c in range(2):walk([child[c] for child in children],ids,d+1)
        walk(packs,np.arange(4*ph.n),0)
        out.append(dict(sourceCell=i,left=str(l),right=str(r),resolvedBoxes=leaves,failedTerminalBoxes=residual,remainingFullAngleSectorIndices=sorted(badangles),minimumProvedDeterminant=mindet))
        print(i,len(badangles),residual,leaves,flush=True)
    report=dict(entrySHA256=shape.digest(__file__),stateSHA256=shape.digest(a.state),fieldSHA256=shape.digest(a.field),spatialSHA256=shape.digest(a.spatial),sourceCells=[a.start_cell,a.end_cell],threshold=str(a.threshold),quarterAngleSectors=a.quarter_angles,radialDepth=maxrad,firstNonpolynomialCellIncluded=False,totalUnresolved=sum(c['failedTerminalBoxes'] for c in out),remainingPieces=sum(bool(c['failedTerminalBoxes']) for c in out),pieces=out,seconds=time.monotonic()-start)
    with a.output.open('x') as f:json.dump(report,f,indent=2);f.write('\n')
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for n in ('scripts','state','field','spatial','output'):p.add_argument('--'+n,type=Path,required=True)
    p.add_argument('--start-cell',type=int,default=1);p.add_argument('--end-cell',type=int,default=128);p.add_argument('--threshold',type=Q,default=Q(1041,100));p.add_argument('--quarter-angles',type=int,default=1024);p.add_argument('--radial-depth',type=int,default=6)
    a=p.parse_args();assert 1<=a.start_cell<a.end_cell<=128;run(a)
