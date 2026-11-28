#!/usr/bin/env python3
"""New reconstruction of the short-phase H65 closed strip and same-target spatial updates.

The W coefficient tensor is a genuinely added position field. The saved R299
packet is used in all its native modes, with the mathematical inlet in cell 0.
"""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path

for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import numpy as np
from scipy.interpolate import BSpline
from scipy.linalg import solve


def module(path):
    spec=importlib.util.spec_from_file_location('r299_ramp_input',path)
    m=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def smooth(t):
    return t**3*(10-15*t+6*t*t)


def left_basis(t,h):
    b=[1-smooth(t),t-6*t**3+8*t**4-3*t**5,(t*t-3*t**3+3*t**4-t**5)/2]
    d=[-30*t*t*(1-t)**2,1-18*t*t+32*t**3-15*t**4,t-4.5*t*t+6*t**3-2.5*t**4]
    e=[-60*t*(1-t)*(1-2*t),-36*t+96*t*t-60*t**3,1-9*t+18*t*t-10*t**3]
    return np.array([[v*h**(j-i) for j,v in enumerate(row)] for i,row in enumerate((b,d,e))])


class PhysicalSource:
    def __init__(self,a,nd):
        self.a=a
        self.inlet=module(a.scripts/'2ecf-r299-short-phase-positive-curvature-arc-cauchy.py').Inlet()
        with np.load(a.field) as d:
            self.s=d['radialNodes'].copy()
            data=d['portPVA'].copy()
        self.u=np.arange(nd)*2*np.pi/nd
        self.gamma,self.T,self.N=self.inlet.geometry(self.u)
        self.k=self.inlet.k(self.u)
        self.gamma_u2=-self.k[:,None]*self.N
        self.ez=np.zeros_like(self.gamma)
        self.ez[:,2]=1
        self.gamma_j=(self.gamma,self.T,self.gamma_u2)
        self.central=self.gamma+a.c*self.ez
        self.end=a.c+self.s[-1]
        self.capstart=self.end+a.length
        w=np.arange(data.shape[2])
        self.G=[]
        for j in range(3):
            # Fold the actual full even/odd trigonometric polynomial on
            # any requested angular grid, including all high positive modes.
            cc=data*((1j*w)**j)[None,None,:,None]
            folded=np.zeros((len(self.s),3,nd,3),complex)
            folded[:,:,0]=cc[:,:,0].real
            for k in range(1,len(w)):
                folded[:,:,k%nd]+=cc[:,:,k]
                folded[:,:,(-k)%nd]+=cc[:,:,k].conj()
            v=np.fft.ifft(folded,axis=2,norm='forward').real
            if j==0:
                v[:,0,:,2]+=a.c-.2
                v[0]=0
                v[0,0]=self.central
                v[0,1]=self.ez
            else:
                v[0]=0
                v[0,0]=self.gamma_j[j]
            self.G.append(v)
        co,si=np.cos(self.u),np.sin(self.u)
        self.circle=np.stack((co,si,co*0),axis=1)
        self.circle_t=np.stack((-si,co,si*0),axis=1)

    def ramp(self,r):
        i=np.clip(np.searchsorted(self.s,r,side='right')-1,0,len(self.s)-2)
        h=self.s[i+1]-self.s[i]
        t=(r-self.s[i])/h
        b=left_basis(t,h)
        br=left_basis(1-t,h)
        J=np.empty((6,len(self.u),3))
        for j,entries in enumerate((((0,0),(1,1),(2,3)),((0,2),(1,4)),((0,5),))):
            for order,index in entries:
                c=br[order]*(-1.)**(order+np.arange(3))
                J[index]=np.einsum('i,iuc->uc',b[order],self.G[j][i])+np.einsum('i,iuc->uc',c,self.G[j][i+1])
        t=r/self.s[-1]
        f=1+.006*self.s[-1]*(21*t**6-60*t**7+67.5*t**8-35*t**9+7*t**10)
        return J,(1.,f)

    def closing(self,t):
        a=self.a
        d=a.length*t
        q=1-smooth(t)
        qp=-30*t*t*(1-t)**2/a.length
        qpp=-60*t*(1-t)*(1-2*t)/a.length**2
        cc=(a.cap_radius*self.circle,a.cap_radius*self.circle_t,-a.cap_radius*self.circle)
        J=np.empty((6,len(self.u),3))
        for j,entries in enumerate((((0,0),(1,1),(2,3)),((0,2),(1,4)),((0,5),))):
            left=self.gamma_j[j]
            right=cc[j]
            corr=self.G[j][-1].copy()
            corr[0]-=left+(self.end*self.ez if j==0 else 0)
            if j==0:
                corr[1]-=self.ez
            for order,index in entries:
                if order==0:
                    val=q*left+(1-q)*right+((self.end+d)*self.ez if j==0 else 0)
                elif order==1:
                    val=qp*(left-right)+(self.ez if j==0 else 0)
                else:
                    val=qpp*(left-right)
                if d<a.gate:
                    val+=np.einsum('i,iuc->uc',left_basis(d/a.gate,a.gate)[order],corr)
                J[index]=val
        f0=1+.006*self.s[-1]/2
        f=q*(f0+.006*d)+(1-q)*a.cap_radius
        fp=qp*(f0+.006*d-a.cap_radius)+.006*q
        return J,(1+smooth(t)*fp*fp,f)

    def middle(self,z,u,eta):
        X=self.inlet.geometry(u-eta)[0]
        X=rotation(X,eta)
        X[:,2]=z
        for i,(site,length,tilt) in enumerate(((.243,1.777,.127),(1.710,2.117,-1.117))):
            _,T,N=self.inlet.geometry(np.array([site]))
            direction=N[0]*np.cos(tilt)+T[0]*np.sin(tilt)
            k=(self.inlet.low,self.inlet.high)[i]
            du=(u-site+np.pi)%(2*np.pi)-np.pi
            bump=length*np.maximum(0,1-(z/.18)**2-(du/.19)**2)**3
            X+=bump[:,None]*rotation(direction,(1-k)*eta)
        return X

    def cap(self,p,u):
        # The geometric chart at the pole uses z as a function of x^2+y^2.
        r=self.a.cap_radius*np.cos(p)
        z=self.capstart+self.a.cap_height*np.sqrt(np.sin(p))
        return np.stack((r*np.cos(u),r*np.sin(u),z+0*u),axis=-1)


def rotation(P,t):
    Q=P.copy()
    Q[...,0]=np.cos(t)*P[...,0]-np.sin(t)*P[...,1]
    Q[...,1]=np.sin(t)*P[...,0]+np.cos(t)*P[...,1]
    return Q


def gram(J,e,f):
    v,u=J[:,1],J[:,2]
    E=(v*v).sum(-1)
    F=(v*u).sum(-1)
    G=(u*u).sum(-1)
    p=E/e-1
    q=F/(np.sqrt(e)*f)
    r=G/f**2-1
    err=np.abs(p+r)/2+np.hypot((p-r)/2,q)
    return np.stack((p,np.sqrt(2)*q,r)),err,(v,u,E,F,G)


def curvature(J,geom):
    v,u,E,F,G=geom
    N=np.cross(v,u)
    area2=(N*N).sum(-1)
    N/=np.sqrt(area2)[...,None]
    l,m,n=[(N*J[:,k]).sum(-1) for k in (3,4,5)]
    trace=(l*G+n*E-2*m*F)/area2
    K=(l*n-m*m)/area2
    return np.abs(trace)/2+np.sqrt(np.maximum(0,trace**2/4-K)),area2


class WorkGrid:
    def __init__(self,a,angles,radial,shift,training):
        self.a=a
        self.src=PhysicalSource(a,angles)
        self.u=self.src.u[:angles//4+1]
        self.t=np.unique(np.r_[np.linspace(0,1,radial+1),(np.arange(radial)+shift)/radial])
        rows=[self.src.closing(t) for t in self.t]
        self.base=np.array([J[:,:len(self.u)] for J,tt in rows])
        targets=np.array([tt for J,tt in rows])
        self.e=targets[:,0,None]
        self.f=targets[:,1,None]
        knots=np.r_[np.zeros(5),np.linspace(0,1,a.spans+1),np.ones(5)]
        n=len(knots)-6
        spline=BSpline(knots,np.eye(n)[:,3:-3],5)
        self.B=[spline.derivative(i)(self.t)/a.length**i for i in range(3)]
        self.A=[]
        self.jac=[]
        self.shape=(3,n-6,a.modes)
        self.nvar=int(np.prod(self.shape))
        for c in range(3):
            w=2*np.arange(a.modes)+(c!=2)
            phase=(c==1)*(-np.pi/2)
            basis=[w[None,:]**j*np.cos(self.u[:,None]*w[None,:]+j*np.pi/2+phase) for j in range(3)]
            self.A.append(basis)
            if training:
                self.jac.append([np.einsum('ri,uj->ruij',self.B[k],basis[d]).reshape(len(self.t)*len(self.u),-1) for k,d in ((1,0),(0,1))])

    def jets(self,x):
        J=self.base.copy()
        for c,X in enumerate(x.reshape(self.shape)):
            for j,(k,d) in enumerate(((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))):
                J[:,j,:,c]+=(self.B[k]@X)@self.A[c][d].T
        return J

    def evaluate(self,x):
        J=self.jets(x)
        res,err,geom=gram(J,self.e,self.f)
        k,area=curvature(J,geom)
        i,j=np.unravel_index(np.argmax(err),err.shape)
        return dict(relativeOperatorPeak=float(err.max()),absolutePrincipalCurvaturePeak=float(k.max()),rms=float(np.sqrt(np.mean(res**2))),minimumAreaSquared=float(area.min()),peakAtPhysicalRadialAndMaterialAngle=[float(self.src.end+self.a.length*self.t[i]),float(self.u[j])])

    def linear(self,x,power):
        res,err,(v,u,E,F,G)=gram(self.jets(x),self.e,self.f)
        ws=(np.maximum(.025,err/(err.max()+1e-30))**power).reshape(-1,1)/np.sqrt(err.size)
        cross=np.sqrt(2)/(np.sqrt(self.e)*self.f)
        M=np.empty((3,err.size,self.nvar))
        size=self.nvar//3
        for c,(ds,du) in enumerate(self.jac):
            ix=slice(c*size,(c+1)*size)
            V=v[:,:,c]
            U=u[:,:,c]
            M[0,:,ix]=(2*V/self.e).reshape(-1,1)*ds
            M[1,:,ix]=(cross*U).reshape(-1,1)*ds+(cross*V).reshape(-1,1)*du
            M[2,:,ix]=(2*U/self.f**2).reshape(-1,1)*du
        M*=ws[None,:,:]
        return M.reshape(-1,self.nvar),(res.reshape(3,-1)*ws[:,0]).ravel(),err


def ramp_observe(grid):
    rs=grid.src.s
    radial=np.unique(np.r_[rs,*[rs[:-1]+v*np.diff(rs) for v in (.112701665379,.5,.887298334621)]])
    peak=kmax=0.
    for r in radial:
        jet,(e,f)=grid.src.ramp(r)
        _,err,geom=gram(jet[None],e,f)
        k,_=curvature(jet[None],geom)
        peak=max(peak,float(err.max()))
        kmax=max(kmax,float(k.max()))
    return dict(radialRows=len(radial),angles=len(grid.src.u),relativeOperatorPeak=peak,absolutePrincipalCurvaturePeak=kmax)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(a):
    if not (a.gate>0 and a.length>=a.gate and a.cap_radius>0 and a.spans>=3 and a.angles%4==0 and a.independent%4==0):
        raise ValueError('invalid physical or angular data')
    P=WorkGrid(a,a.angles,a.radial,.37,True)
    Q=WorkGrid(a,a.independent,a.test_radial,.627,False)
    x=np.zeros(P.nvar)
    if a.seed:
        with np.load(a.seed) as z:
            x=z['coefficients'].copy()
        if x.shape!=(P.nvar,):
            raise ValueError('seed tensor shape mismatch')
    initial=x.copy()
    steps=[]
    for num in range(a.steps):
        M,res,err=P.linear(x,.4 if num<4 else 1 if num<12 else 1.8)
        H=M.T@M
        grad=M.T@res
        peak=err.max()
        exp=4 if num<5 else 8
        oldobj=np.mean(err**exp)**(1/exp)
        best=None
        for damping in (1e-7,1e-5,.0005,.01):
            diagonal=np.maximum(1e-7,H.diagonal())*damping+5e-11
            dx=solve(H+np.diag(diagonal),-grad,assume_a='pos')
            for scale in (1.,.5,.25,.125,.0625,.03125):
                candidate=x+scale*dx
                _,e1,_=gram(P.jets(candidate),P.e,P.f)
                obj=np.mean(e1**exp)**(1/exp)
                score=obj+.14*e1.max()
                if obj<oldobj and e1.max()<peak*(1.01 if num<4 else 1.0002) and (best is None or score<best[0]):
                    best=(score,candidate,scale,damping)
        if best is None:
            break
        x=best[1]
        steps.append(dict(step=num+1,scale=best[2],damping=best[3],actual=P.evaluate(x)))
        print(json.dumps(steps[-1]),flush=True)
    out=a.out
    out.parent.mkdir(parents=True,exist_ok=True)
    state=out.with_suffix('.npz')
    with state.open('xb') as f:
        np.savez_compressed(f,coefficients=x)
    report=dict(schema='R303-reconstructed-full-physical-closure-and-fixed-metric-XYZ-v2',
        entrySHA256=digest(Path(__file__)),r299InputSHA256=digest(a.field),stateSHA256=digest(state),
        parameters={k:v for k,v in vars(a).items() if not isinstance(v,Path)},
        variables=P.nvar,initialTraining=P.evaluate(initial),initialIndependent=Q.evaluate(initial),
        independentUnchangedWholeRamp=ramp_observe(Q),accepted=steps,finalTraining=P.evaluate(x),finalIndependent=Q.evaluate(x),
        unchangedComponents='Both physical caps and the two local moving rigid attachments have zero relative metric error at every phase. The nonzero field is zero to two jets at both ends of the closing strip. The shape ratios and reach of a corrected field require its own geometric bounds.')
    with out.open('x') as f:
        json.dump(report,f,indent=2)
        f.write('\n')
    print('FINAL',json.dumps(report['finalIndependent']),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--scripts',type=Path,required=True)
    p.add_argument('--field',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--seed',type=Path)
    for key,value in (('c',.65),('length',.38),('gate',.10),('cap-radius',.62),('cap-height',.30)):
        p.add_argument('--'+key,type=float,default=value)
    for key,value in (('steps',18),('angles',96),('radial',38),('independent',256),('test-radial',83),('spans',10),('modes',6)):
        p.add_argument('--'+key,type=int,default=value)
    run(p.parse_args())
