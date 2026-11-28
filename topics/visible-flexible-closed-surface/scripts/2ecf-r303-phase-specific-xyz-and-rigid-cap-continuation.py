#!/usr/bin/env python3
"""Phase-specific physical XYZ continuation from an exact initial full induced metric.

The closure at each nonzero phase is an independent spatial surface. Arbitrary
proper rigid motion of the entire upper cap has six free variables. The lower
half is reflected. The high arm remains the common fixed material region
after applying its inverse instantaneous rigid motion to the entire surface.
"""
import argparse,hashlib,importlib.util,json,os
from pathlib import Path
from types import SimpleNamespace
for k in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):
    os.environ[k]='1'
import numpy as np
from scipy.interpolate import BSpline
from scipy.linalg import solve
from scipy.spatial.transform import Rotation

def mod(p,name):
    s=importlib.util.spec_from_file_location(name,p)
    m=importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def initial_ramp_with_shift(cl,a,n,delta):
    src=cl.PhysicalSource(a,n)
    if delta==0:
        return src
    with np.load(a.field) as pack:
        c=pack['portPVA']
    u=src.u+delta
    X,T,N=src.inlet.geometry(u)
    w=np.arange(c.shape[2])
    for j in range(3):
        cc=c*((1j*w)**j*np.exp(1j*w*delta))[None,None,:,None]
        folded=np.zeros((len(src.s),3,n,3),complex)
        folded[:,:,0]=cc[:,:,0].real
        for k in range(1,len(w)):
            folded[:,:,k%n]+=cc[:,:,k]
            folded[:,:,(-k)%n]+=cc[:,:,k].conj()
        zz=np.fft.ifft(folded,axis=2,norm='forward').real
        if j==0:
            zz[:,0,:,2]+=a.c-.2
            zz[0]=0
            zz[0,0]=X+a.c*src.ez
            zz[0,1]=src.ez
        else:
            zz[0]=0
            zz[0,0]=T if j==1 else -src.inlet.k(u)[:,None]*N
        src.G[j]=zz
    return src

class CommonTarget:
    def __init__(self,initial):
        v,u=initial[:,1],initial[:,2]
        e=(v*v).sum(-1)
        f=(v*u).sum(-1)
        g=(u*u).sum(-1)
        self.aa=1/np.sqrt(e)
        self.r=f/e
        self.bb=1/np.sqrt(g-f*f/e)

    def measure(self,J):
        v,u=J[:,1],J[:,2]
        A=self.aa[...,None]*v
        B=self.bb[...,None]*(u-self.r[...,None]*v)
        E=(A*A).sum(-1)-1.
        F=(A*B).sum(-1)
        G=(B*B).sum(-1)-1.
        err=np.abs(E+G)/2+np.hypot((E-G)/2,F)
        return np.stack((E,np.sqrt(2)*F,G)),err,A,B

def actual_curvature(J):
    v,u=J[:,1],J[:,2]
    E=(v*v).sum(-1);F=(v*u).sum(-1);G=(u*u).sum(-1)
    N=np.cross(v,u);area=(N*N).sum(-1);N=N/np.sqrt(area)[...,None]
    l,m,n=[(N*J[:,i]).sum(-1) for i in (3,4,5)]
    tr=(l*G+n*E-2*m*F)/area
    K=(l*n-m*m)/area
    return np.abs(tr)/2+np.sqrt(np.maximum(0,tr*tr/4-K)),area

class PhaseGrid:
    def __init__(self,cl,a,delta,nd,nr,shift,linear):
        self.cl=cl;self.a=a;self.delta=delta
        inlet=mod(a.scripts/'2ecf-r299-short-phase-positive-curvature-arc-cauchy.py','phaseInlet').Inlet()
        self.u=np.arange(nd)*2*np.pi/nd
        self.t=np.unique(np.r_[np.linspace(0,1,nr+1),(np.arange(nr)+shift)/nr])
        with np.load(a.field) as pack:
            c=pack['portPVA'][-1].copy()
            self.end=a.c+float(pack['radialNodes'][-1])
        self.pivot=np.array([0.,0.,self.end+a.length])
        c[0,0,2]+=a.c-.2
        wave=np.arange(c.shape[1])
        ez=np.zeros((nd,3));ez[:,2]=1.
        def source(t,delta):
            h=1-cl.smooth(t)
            h1=-30*t*t*(1-t)**2/a.length
            h2=-60*t*(1-t)*(1-2*t)/a.length**2
            u=self.u+delta*h
            X,T,N=inlet.geometry(u)
            gamma=(X,T,-inlet.k(u)[:,None]*N)
            co,si=np.cos(u),np.sin(u)
            ec=np.column_stack((co,si,0*u))
            et=np.column_stack((-si,co,0*u))
            circle=(a.cap_radius*ec,a.cap_radius*et,-a.cap_radius*ec)
            d=a.length*t
            J=np.empty((6,nd,3))
            if d<a.gate:
                phase=np.exp(1j*u[:,None]*wave[None,:])
                # Re(C0)+2 Re(sum_{k>0} Ck exp(iku)).
                phase[:,0]*=.5
                corr=[]
                for j in range(3):
                    pos=2*np.einsum('uk,jkc,k->juc',phase,c,(1j*wave)**j,optimize=True).real
                    pos[0]-=gamma[j]+(self.end*ez if j==0 else 0.)
                    if j==0: pos[1]-=ez
                    corr.append(pos)
            for j,indices in enumerate((((0,0),(1,1),(2,3)),((0,2),(1,4)),((0,5),))):
                for k,idx in indices:
                    g=gamma[j];r=circle[j]
                    if k==0:
                        v=h*g+(1-h)*r+((self.end+d)*ez if j==0 else 0.)
                    elif k==1:
                        v=h1*(g-r)+(ez if j==0 else 0.)
                    else:
                        v=h2*(g-r)
                    if d<a.gate:
                        v+=np.einsum('j,juc->uc',cl.left_basis(d/a.gate,a.gate)[k],corr[j])
                    J[idx]=v
            ua,uaa=delta*h1,delta*h2
            # Pull back by v=w+delta*(1-S5(a/L)); identical angle at inside cap.
            J[3]+=2*ua*J[4]+ua*ua*J[5]+uaa*J[2]
            J[4]+=ua*J[5]
            J[1]+=ua*J[2]
            return J
        self.Y=np.array([source(t,delta) for t in self.t])
        ref=self.Y if delta==0 else np.array([source(t,0.) for t in self.t])
        self.target=CommonTarget(ref)
        t=self.t
        self.gate=[cl.smooth(t)[:,None,None],(30*t*t*(1-t)**2/a.length)[:,None,None],(60*t*(1-t)*(1-2*t)/a.length**2)[:,None,None]]
        knots=np.r_[np.zeros(5),np.linspace(0,1,a.spans+1),np.ones(5)]
        n=len(knots)-6
        spline=BSpline(knots,np.eye(n)[:,3:-3],5)
        self.B=[spline.derivative(j)(t)/a.length**j for j in range(3)]
        freq=np.arange(1,a.modes+1)
        self.A=[]
        for j in range(3):
            v=self.u[:,None]*freq[None,:]+j*np.pi/2
            self.A.append(np.column_stack((np.full(nd,1. if j==0 else 0.),np.cos(v)*freq**j,np.sin(v)*freq**j)))
        self.shape=(3,n-6,1+2*a.modes)
        self.nvar=int(np.prod(self.shape))
        if linear:
            self.bases=[np.einsum('ri,uj->ruij',self.B[k],self.A[d]).reshape(len(t)*nd,-1) for k,d in ((1,0),(0,1))]

    def jets(self,x,R,T):
        J=self.Y.copy()
        H,H1,H2=self.gate
        C=R-np.eye(3)
        d=(self.Y[:,0]-self.pivot)@C.T+T
        da=self.Y[:,1]@C.T
        du=self.Y[:,2]@C.T
        J[:,0]+=H*d
        J[:,1]+=H1*d+H*da
        J[:,2]+=H*du
        J[:,3]+=H2*d+2*H1*da+H*(self.Y[:,3]@C.T)
        J[:,4]+=H1*du+H*(self.Y[:,4]@C.T)
        J[:,5]+=H*(self.Y[:,5]@C.T)
        for c,X in enumerate(x.reshape(self.shape)):
            for j,(k,d) in enumerate(((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))):
                J[:,j,:,c]+=(self.B[k]@X)@self.A[d].T
        return J

    def report(self,x,R,T):
        J=self.jets(x,R,T)
        residual,e,_,_=self.target.measure(J)
        k,area=actual_curvature(J)
        i,j=np.unravel_index(np.argmax(e),e.shape)
        return dict(peak=float(e.max()),rms=float(np.sqrt(np.mean(residual**2))),curvature=float(k.max()),minAreaSquared=float(area.min()),point=[float(self.t[i]*self.a.length+self.end),float(self.u[j])])

    def linear(self,x,R,T,power):
        residual,e,A,B=self.target.measure(self.jets(x,R,T))
        H,H1,H2=self.gate
        mult=(np.maximum(.045,e/max(float(e.max()),1e-25))**power/np.sqrt(e.size)).reshape(-1,1)
        ds,du=self.bases
        aa=self.target.aa.reshape(-1,1)
        bb=self.target.bb.reshape(-1,1)
        rr=self.target.r.reshape(-1,1)
        BA=ds*aa;BB=(du-rr*ds)*bb
        M=np.empty((3,e.size,self.nvar+6))
        each=self.nvar//3
        for c in range(3):
            ix=slice(c*each,(c+1)*each)
            av=A[:,:,c].reshape(-1,1);bv=B[:,:,c].reshape(-1,1)
            M[0,:,ix]=2*av*BA
            M[1,:,ix]=np.sqrt(2)*(av*BB+bv*BA)
            M[2,:,ix]=2*bv*BB
        for i in range(6):
            v=np.eye(3)[i%3]
            if i<3:
                ds1=H1*np.cross(v,(self.Y[:,0]-self.pivot)@R.T)+H*np.cross(v,self.Y[:,1]@R.T)
                du1=H*np.cross(v,self.Y[:,2]@R.T)
            else:
                ds1=H1*v+np.zeros_like(A);du1=np.zeros_like(A)
            DA=ds1*self.target.aa[...,None]
            DB=(du1-self.target.r[...,None]*ds1)*self.target.bb[...,None]
            M[0,:,self.nvar+i]=(2*A*DA).sum(-1).ravel()
            M[1,:,self.nvar+i]=(np.sqrt(2)*(A*DB+B*DA)).sum(-1).ravel()
            M[2,:,self.nvar+i]=(2*B*DB).sum(-1).ravel()
        M*=mult[None,:,:]
        return M.reshape(-1,self.nvar+6),(residual.reshape(3,-1)*mult[:,0]).ravel(),e

def ramp_reference_error(cl,a,delta):
    P=initial_ramp_with_shift(cl,a,a.independent,0.)
    Q=initial_ramp_with_shift(cl,a,a.independent,delta)
    s=P.s;peak=0.
    for r in np.unique(np.r_[s,*[s[:-1]+f*np.diff(s) for f in (.112701665379,.5,.887298334621)]]):
        J=P.ramp(r)[0][None];j=Q.ramp(r)[0][None]
        peak=max(peak,float(CommonTarget(J).measure(j)[1].max()))
    return peak

def run(a):
    cl=mod(a.solver,'r303newsource')
    assert all(0<=d<=.5 for d in a.deltas)
    out=a.out
    out.parent.mkdir(parents=True,exist_ok=True)
    pack=dict(schema='R303-phase-separated-full-position-recovery-with-one-fixed-true-initial-metric-v1',
       entrySHA256=sha(Path(__file__)),sourceSHA256=sha(a.solver),fieldSHA256=sha(a.field),parameters={k:v for k,v in vars(a).items() if not isinstance(v,Path)},arcs='C2 thick ports; high arm fixed by a global rigid normalization',metric='Single pointwise actual complete initial first fundamental form at material phase eta=.5',results=[])
    xold=Rold=Told=previous=None
    for delta in a.deltas:
        P=PhaseGrid(cl,a,delta,a.angles,a.radial,.347,True)
        Q=PhaseGrid(cl,a,delta,a.independent,a.test_radial,.619,False)
        if xold is None:
            x=np.zeros(P.nvar);R=np.eye(3);T=np.zeros(3)
        else:
            ratio=delta/previous if previous else 1.
            x=xold*ratio
            R=Rotation.from_rotvec(ratio*Rotation.from_matrix(Rold).as_rotvec()).as_matrix()
            T=Told*ratio
        start=P.report(x,R,T)
        newzero=Q.report(np.zeros(P.nvar),np.eye(3),np.zeros(3))
        accepted=[]
        for step in range(a.steps):
            power=.35 if step<5 else .9 if step<12 else 1.5
            M,res,er=P.linear(x,R,T,power)
            cov=M.T@M
            grad=M.T@res
            basepeak=er.max()
            if basepeak<2e-13:break
            exp=4. if step<6 else 8.
            old=np.mean(er**exp)**(1/exp)
            best=None
            for damp in (1e-9,3e-7,3e-5,.002,.025):
                reg=np.maximum(1e-9,cov.diagonal())*damp+1e-14
                dx=solve(cov+np.diag(reg),-grad,assume_a='pos')
                for k in (1.,.5,.25,.125,.0625):
                    xx=x+k*dx[:P.nvar]
                    rr=Rotation.from_rotvec(k*dx[P.nvar:P.nvar+3]).as_matrix()@R
                    tt=T+k*dx[P.nvar+3:]
                    ee=P.target.measure(P.jets(xx,rr,tt))[1]
                    score=np.mean(ee**exp)**(1/exp)
                    if score<old and ee.max()<basepeak*1.002 and (best is None or score+.10*ee.max()<best[0]):
                        best=(score+.10*ee.max(),xx,rr,tt,k,damp)
            if best is None:break
            _,x,R,T,k,damp=best
            z=P.report(x,R,T)
            accepted.append(dict(step=step+1,scale=k,damping=damp,actual=z))
            print(delta,step+1,z,flush=True)
        referr=ramp_reference_error(cl,a,delta)
        target=Q.report(x,R,T)
        state=out.with_name(out.stem+'-phase'+str(len(pack['results'])+1)+'.npz')
        with state.open('xb') as f:np.savez_compressed(f,delta=delta,coefficients=x,rotation=R,translation=T)
        result=dict(delta=delta,eta=.5-delta,variables=P.nvar+6,zeroCorrectionIndependent=newzero,warmTraining=start,accepted=accepted,finalTraining=P.report(x,R,T),finalIndependent=target,independentFullRamp=referr,completeObservedPeak=max(referr,target['peak']),stateSHA256=sha(state))
        pack['results'].append(result)
        xold,Rold,Told,previous=x,R,T,delta
        print('PHASE',json.dumps({k:v for k,v in result.items() if k!='accepted'}),flush=True)
    with out.open('x') as f:
        json.dump(pack,f,indent=2)
        f.write('\n')

if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('scripts','solver','field','out'):
        p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--deltas',type=float,nargs='+',default=[1/1024,1/256,1/64])
    for k,v in (('c',.78),('length',.38),('gate',.10),('cap-radius',.62),('cap-height',.30)):
        p.add_argument('--'+k,type=float,default=v)
    for k,v in (('spans',8),('modes',6),('angles',64),('radial',25),('independent',192),('test-radial',63),('steps',18)):
        p.add_argument('--'+k,type=int,default=v)
    run(p.parse_args())
