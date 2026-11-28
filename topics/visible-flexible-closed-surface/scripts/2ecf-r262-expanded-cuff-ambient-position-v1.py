#!/usr/bin/env python3
"""A complete new ambient image of the actual R262 field, with an enlarged cuff.

The exact definition uses the original analytic background, not an interpolant.
Numerical output is a finite observation of this new field and its new target g.
The old isometry and reach bounds are not transferred to it.
"""
import argparse, hashlib, importlib.util, json, os, time
from pathlib import Path
from fractions import Fraction as Q
for k in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):
    os.environ[k]='1'
import numpy as np

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,n):
    s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def dot(x,y): return np.sum(x*y,axis=-1)
def smooth(x): return x**3*(10+x*(-15+6*x))
def smooth1(x): return 30*x*x*(1-x)**2
def smooth2(x): return 60*x*(1-x)*(1-2*x)
def primitive(x): return x**4*(2.5+x*(-3+x))

class Ambient:
    def __init__(self,src,cuff,flat):
        self.src=src;self.bg=src.chart.background
        self.a=float(src.chart.cuff);self.b=float(src.chart.c)
        self.A=float(Q(cuff));self.c=float(Q(flat));self.ell=1/40
        self.lam=self.A/self.a
        self.v=(self.b-self.A-self.ell*(self.lam+1)/2)/(self.b-self.a-self.ell)
        assert 0<self.v<1<self.lam and self.A<self.c<self.b
        self.Z=float(src.pos.src.cut_height)
        self.oldH=self.Z+float(self.bg.point(self.bg.cuff)[2])
        self.L=self.b-self.c
        # W is cubic Hermite: W(c)=W'(c)=0; W(b)=1/2; W'(b)=-7/(2b).
        self.wb=float(self.bg.point(self.bg.cut)[0]);self.wrb=float(self.bg.point(self.bg.cut)[1])
        self.c2=3*self.wb-self.L*self.wrb
        self.c3=self.L*self.wrb-2*self.wb
        self.H=self.Z+self.L*(self.c2/3+self.c3/4)
        self.background_calls=0
    def radial(self,r):
        r=np.asarray(r,float);f=r.copy();fp=np.ones_like(r);fpp=np.zeros_like(r)
        inner=r<=self.a;f[inner]=self.lam*r[inner];fp[inner]=self.lam
        lo=(r>self.a)&(r<self.a+self.ell);x=(r[lo]-self.a)/self.ell
        f[lo]=self.A+self.ell*(self.lam*x+(self.v-self.lam)*primitive(x))
        fp[lo]=self.lam+(self.v-self.lam)*smooth(x)
        fpp[lo]=(self.v-self.lam)/self.ell*smooth1(x)
        left=self.A+self.ell*(self.lam+self.v)/2
        mid=(r>=self.a+self.ell)&(r<=self.b-self.ell)
        f[mid]=left+self.v*(r[mid]-self.a-self.ell);fp[mid]=self.v
        outer=(r>self.b-self.ell)&(r<self.b);x=(r[outer]-self.b+self.ell)/self.ell
        start=left+self.v*(self.b-self.a-2*self.ell)
        f[outer]=start+self.ell*(self.v*x+(1-self.v)*primitive(x))
        fp[outer]=self.v+(1-self.v)*smooth(x)
        fpp[outer]=(1-self.v)/self.ell*smooth1(x)
        return f,fp,fpp
    def new_profile(self,R):
        R=np.asarray(R,float);x=np.clip((R-self.c)/self.L,0,1)
        w=self.c2*x*x+self.c3*x**3
        wr=(2*self.c2*x+3*self.c3*x*x)/self.L
        h=self.Z+self.L*(self.c2*(1-x**3)/3+self.c3*(1-x**4)/4)
        return h,w,wr
    def displacement(self,r):
        r=np.asarray(r,float);R,Rp,Rpp=self.radial(r);h,w,wr=self.new_profile(R)
        oldh=np.full(r.shape,self.oldH);oldw=np.zeros(r.shape);oldwr=np.zeros(r.shape)
        mask=(r>self.a)&(r<self.b)
        for i in np.flatnonzero(mask.ravel()):
            rr=r.flat[i];b=self.bg.point(np.longdouble(rr));self.background_calls+=1
            oldw.flat[i]=b[0];oldwr.flat[i]=b[1];oldh.flat[i]=self.Z+float(b[2])
        d=h-oldh;d1=-w*Rp+oldw;d2=-wr*Rp*Rp-w*Rpp+oldwr
        outer=r>=self.b;d[outer]=0;d1[outer]=0;d2[outer]=0
        inner=r<=self.a;d[inner]=self.H-self.oldH;d1[inner]=0;d2[inner]=0
        return R,Rp,Rpp,d,d1,d2
    def transform(self,J):
        J=np.asarray(J,float);P,S,U,SS,SU,UU=np.moveaxis(J,1,0)
        r=np.linalg.norm(P[...,:2],axis=-1);assert np.min(r)>0
        R,Rp,Rpp,d,d1,d2=self.displacement(r)
        rS=dot(P[...,:2],S[...,:2])/r;rU=dot(P[...,:2],U[...,:2])/r
        rij=[]
        for V,W,A,ri,rj in ((S,S,SS,rS,rS),(S,U,SU,rS,rU),(U,U,UU,rU,rU)):
            rij.append((dot(V[...,:2],W[...,:2])+dot(P[...,:2],A[...,:2])-ri*rj)/r)
        g=R/r;g1=Rp/r-R/r**2;g2=Rpp/r-2*Rp/r**2+2*R/r**3
        z=P[...,2];x=np.clip(abs(z)/1.5,0,1);sg=np.sign(z)
        chi=sg*smooth(x);chi1=smooth1(x)/1.5;chi2=sg*smooth2(x)/1.5**2
        out=np.empty_like(J);out[:,0,:,:2]=g[...,None]*P[...,:2]
        out[:,0,:,2]=z+chi*d
        for k,V,ri in ((1,S,rS),(2,U,rU)):
            out[:,k,:,:2]=g[...,None]*V[...,:2]+(g1*ri)[...,None]*P[...,:2]
            out[:,k,:,2]=(1+chi1*d)*V[...,2]+chi*d1*ri
        for k,V,W,A,ri,rj,rr in ((3,S,S,SS,rS,rS,rij[0]),(4,S,U,SU,rS,rU,rij[1]),(5,U,U,UU,rU,rU,rij[2])):
            out[:,k,:,:2]=(g[...,None]*A[...,:2]+g1[...,None]*(rr[...,None]*P[...,:2]+ri[...,None]*W[...,:2]+rj[...,None]*V[...,:2])+(g2*ri*rj)[...,None]*P[...,:2])
            out[:,k,:,2]=((1+chi1*d)*A[...,2]+chi2*d*V[...,2]*W[...,2]+chi1*d1*(V[...,2]*rj+W[...,2]*ri)+chi*d2*ri*rj+chi*d1*rr)
        stats={'maximumAbsVerticalDisplacement':float(abs(d).max()),'minimumAmbientVerticalDerivative':float((1+chi1*d).min()),'minimumOriginalSpatialRadius':float(r.min())}
        return out,stats
    def target(self,z,bb):
        targetE=np.ones(len(z));targetb=np.asarray(bb,float).copy()
        tail=z>self.src.S/self.src.T+1e-14
        for i in np.flatnonzero(tail):
            r=self.b+self.src.S-self.src.T*z[i]
            r=min(self.b,max(self.a,r));R,Rp,_=self.radial(np.array([r]));_,w,_=self.new_profile(R)
            wo=float(self.bg.point(np.longdouble(r))[0])
            targetE[i]=Rp[0]**2*(1+w[0]**2)/(1+wo*wo)
            targetb[i]*=R[0]/r
        return targetE,targetb

def observe(J,E0,b):
    P,S,U,SS,SU,UU=np.moveaxis(np.asarray(J,float),1,0)
    E,F,G=dot(S,S),dot(S,U),dot(U,U);aa=E/E0[:,None];cc=G/b**2;ff=F/(np.sqrt(E0[:,None])*b)
    err=abs(aa+cc-2)/2+np.hypot((aa-cc)/2,ff)
    normal=np.cross(S,U);area=np.linalg.norm(normal,axis=-1);normal/=area[...,None]
    l,m,n=dot(normal,SS),dot(normal,SU),dot(normal,UU)
    tr=(E*n-2*F*m+G*l)/area**2;det=(l*n-m*m)/area**2
    K=abs(tr)/2+np.sqrt(np.maximum(0,tr*tr/4-det))
    ix=np.unravel_index(err.argmax(),err.shape);ik=np.unravel_index(K.argmax(),K.shape)
    return dict(metricMaximum=float(err.max()),metricIndex=list(map(int,ix)),curvatureMaximum=float(K.max()),curvatureIndex=list(map(int,ik)),minimumOutwardSupport=float((-dot(P,normal)).min()),ballRadiusMaximum=float(np.linalg.norm(P,axis=-1).max()),heightMaximum=float(P[...,2].max()),minimumArea=float(area.min()))

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for k in ('scripts','data','grid','field','query-report','query-cache','output'):ap.add_argument('--'+k,type=Path,required=True)
    ap.add_argument('--cuff',default='8/25');ap.add_argument('--flat',default='21/50')
    ap.add_argument('--prefix-rows',type=int,default=40);ap.add_argument('--tail-rows',type=int,default=32);ap.add_argument('--angles',type=int,default=96)
    a=ap.parse_args();assert not a.output.exists();start=time.monotonic()
    module=load(a.scripts/'2ecf-r262-minkowski-physical-continuation.py','r280_r262_source')
    src=module.Source(a);amb=Ambient(src,a.cuff,a.flat);reports=[]
    for shift in (False,True):
        old=src.old(a.prefix_rows,a.tail_rows,a.angles if not shift else a.angles+17,shift)
        z,t,_,_,J,bb=old
        print(json.dumps({'stage':'original-ready','shift':shift,'rows':len(z),'angles':len(t),'elapsed':time.monotonic()-start}),flush=True)
        new,stats=amb.transform(J);E0,b=amb.target(z,bb)
        reports.append(dict(shift=shift,rows=len(z),angles=len(t),original=observe(J,np.ones(len(z)),np.asarray(bb,float)),new=observe(new,E0,b),ambient=stats))
        print(json.dumps(reports[-1]),flush=True)
    report=dict(schema='R262-complete-ambient-enlarged-cuff-and-new-target-finite-observation-v1',scriptSHA256=sha(__file__),originalFieldSHA256=sha(a.field),sourceSHA256=sha(a.scripts/'2ecf-r262-minkowski-physical-continuation.py'),cuff=a.cuff,flat=a.flat,originalCuffExact=str(Q(str(src.chart.cuff))),originalCutExact=str(Q(str(src.chart.c))),expansion=amb.lam,minimumRadialDerivative=amb.v,newCuffHeight=amb.H,oldCuffHeight=amb.oldH,newProfileCoefficients=[amb.c2,amb.c3],observations=reports,backgroundPointQueries=amb.background_calls,newTargetMetric=True,inheritedOldMetricOrReach=False,numericalOnly=True,seconds=time.monotonic()-start)
    a.output.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'output':str(a.output),'SHA256':sha(a.output),'seconds':report['seconds']}),flush=True)
if __name__=='__main__':main()
