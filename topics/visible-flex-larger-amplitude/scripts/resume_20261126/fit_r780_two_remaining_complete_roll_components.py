#!/usr/bin/env python3
"""Fit the two remaining material components of both complete R780 rolls in periodic arclength coordinates."""
import numpy as np
from scipy.optimize import least_squares
from scipy.sparse.linalg import LinearOperator
import r780_complete_ring_arclength_and_physical_jets as ring

GEOM=ring.geom
LEVELS=((32,10,8,24),(56,16,12,36),(88,24,18,48))

class Fit:
    def __init__(self,level,phase,order,mode,side):
        ns,nu,_,_=LEVELS[level];self.shape=ring.SHAPES[level]
        P=ring.period(order);st=GEOM.c.stations(order)
        self.s=np.unique(np.r_[np.arange(ns)*P/ns,st,P-st])
        self.s=self.s[(self.s>=0)&(self.s<P-1e-12)]
        self.s=self.s[np.r_[True,np.diff(self.s)>1e-12]]
        self.ds=np.diff(np.r_[self.s,P])
        self.u=np.unique(np.r_[np.linspace(0,ring.ACTIVE,nu+1),ring.E/4,ring.E/2,3*ring.E/4,ring.E,
                                ring.E+.0005,ring.ACTIVE-.0005])
        a,u=np.meshgrid(self.s,self.u,indexing="xy")
        p,d=ring.radial(self.u,order);self.C=np.zeros((len(p.v),1,3));self.Cu=self.C.copy()
        self.C[:,:,0]=GEOM.m.section_center(order);self.C[:,:,1]=side*(ring.B+p.v[:,None])
        self.Cu[:,:,1]=side*p.a[:,None]
        self.ell0=(P-2*np.pi*d.v)[:,None];self.ell0u=(-2*np.pi*d.a)[:,None]
        K=ring.original_angle(self.s,order).v
        self.sigma0=(self.s[None,:]-d.v[:,None]*K)/self.ell0
        self.sigma0u=(-d.a[:,None]*K-self.sigma0*self.ell0u)/self.ell0
        fixed=ring.native(a,u,phase,order,mode,side,self.shape,None)
        basis=ring.basis(a,u,P,self.shape)
        self.H=[basis[...,k,:] for k in (0,1,2,4)]
        self.baseline=[fixed[...,k,:] for k in (0,1,2,4)]
        self.n=self.H[0].shape[-1];self.weights=np.sqrt((self.ds+np.roll(self.ds,1))/(2*P*len(self.u)))
        self.key=None;self.saved=None
    def cum(self,y):
        shape=(1,len(self.ds))+(1,)*(y.ndim-2)
        q=.5*self.ds.reshape(shape)*(y+np.roll(y,-1,axis=1))
        z=np.cumsum(q,axis=1)
        return np.concatenate((np.zeros_like(z[:,:1]),z[:,:-1]),axis=1),z[:,-1:]
    def state(self,x):
        key=x.tobytes()
        if self.key==key:return self.saved
        mat=x.reshape(self.n,3)
        q,g,b,h=[r+H@mat for r,H in zip(self.baseline,self.H)]
        V=np.linalg.norm(g,axis=2);safe=np.maximum(V,1e-14)
        t=g/safe[:,:,None];vu=np.einsum("rij,rij->ri",t,h)
        I,L=self.cum(V);Iu,Lu=self.cum(vu)
        sig=I/L;sigu=(Iu-sig*Lu)/L
        comp=[];slope=[]
        for a,ou,xs in zip(self.sigma0,self.sigma0u,sig):
            grid=np.r_[a,1.];vals=np.r_[ou,0.]
            ix=np.clip(np.searchsorted(grid,xs,side="right")-1,0,len(a)-1)
            sp=(vals[ix+1]-vals[ix])/(grid[ix+1]-grid[ix])
            comp.append(vals[ix]+sp*(xs-grid[ix]));slope.append(sp)
        P0=np.asarray(comp);S0=np.asarray(slope)
        r=self.ell0/L;ru=(self.ell0u-r*Lu)/L
        gauge=(P0-sigu)*self.ell0
        H=self.Cu+r[:,:,None]*(b-self.Cu)+ru[:,:,None]*(q-self.C)+t*gauge[:,:,None]
        R=np.stack((np.sqrt(2)*np.einsum("rij,rij->ri",t,H),np.einsum("rij,rij->ri",H,H)-1.),axis=-1)
        self.saved=(q,g,b,h,safe,t,L,Lu,sig,sigu,S0,r,ru,gauge,H,R)
        self.key=key
        return self.saved
    def fun(self,x):
        return np.r_[(self.state(x)[-1]*self.weights[None,:,None]).ravel(),.00025*x]
    def jac(self,x):
        q,g,b,h,V,t,L,Lu,sig,sigu,sp,r,ru,gauge,H,R=self.state(x)
        rows=2*R.shape[0]*R.shape[1];m=3*self.n;M=np.empty((rows,m))
        for lo in range(0,m,8):
            ids=np.arange(lo,min(lo+8,m));eye=np.eye(3)[ids%3].T
            dq,dg,db,dh=[np.take(H0,ids//3,axis=2)[:,:,None,:]*eye[None,None,:,:] for H0 in self.H]
            dv=np.einsum("rij,rijk->rik",t,dg)
            dt=(dg-t[:,:,:,None]*dv[:,:,None,:])/V[:,:,None,None]
            dvu=np.einsum("rijk,rij->rik",dt,h)+np.einsum("rij,rijk->rik",t,dh)
            di,dl=self.cum(dv);diu,dlu=self.cum(dvu)
            ds=(di-sig[:,:,None]*dl)/L[:,:,None]
            dsu=(diu-ds*Lu[:,:,None]-sig[:,:,None]*dlu-sigu[:,:,None]*dl)/L[:,:,None]
            dr=-r[:,:,None]*dl/L[:,:,None]
            dru=(-dr*Lu[:,:,None]-r[:,:,None]*dlu-ru[:,:,None]*dl)/L[:,:,None]
            dw=(sp[:,:,None]*ds-dsu)*self.ell0[:,:,None]
            D=(dr[:,:,None,:]*(b-self.Cu)[:,:,:,None]+r[:,:,None,None]*db+
               dru[:,:,None,:]*(q-self.C)[:,:,:,None]+ru[:,:,None,None]*dq+
               dt*gauge[:,:,None,None]+t[:,:,:,None]*dw[:,:,None,:])
            d1=np.einsum("rijk,rij->rik",dt,H)+np.einsum("rij,rijk->rik",t,D)
            d2=2*np.einsum("rij,rijk->rik",H,D)
            M[:,ids]=(np.stack((np.sqrt(2)*d1,d2),axis=2)*self.weights[None,:,None,None]).reshape(rows,len(ids))
        def mv(z):
            z=np.asarray(z).ravel();return np.r_[M@z,.00025*z]
        def rv(z):
            z=np.asarray(z).ravel();return M.T@z[:rows]+.00025*z[rows:]
        return LinearOperator((rows+m,m),matvec=mv,rmatvec=rv,dtype=float)
    def report(self,x):
        q,g,b,h,V,t,L,Lu,sig,sigu,sp,r,ru,w,H,R=self.state(x)
        val=np.stack((abs(R[...,0])/np.sqrt(2),abs(R[...,1])),axis=-1);worst=[]
        for j in range(2):
            i,k=np.unravel_index(np.argmax(val[...,j]),val[...,j].shape)
            worst.append([float(val[i,k,j]),float(self.s[k]),float(self.u[i])])
        return {"nodes":[len(self.s),len(self.u)],"max_abs_shear_radial":worst,
                "min_native_speed":float(np.linalg.norm(g,axis=2).min()),
                "minmax_ring_scale":[float(r.min()),float(r.max())]}

def fit(level,ph,order,mode,side,seed):
    study=Fit(level,ph,order,mode,side);zero=np.zeros(study.n*3)
    start=zero if seed is None else seed.ravel()
    if np.linalg.norm(study.fun(start))>np.linalg.norm(study.fun(zero)):start=zero
    before=study.report(start);nfev,it=LEVELS[level][2:]
    if ph:
        sol=least_squares(study.fun,start,jac=study.jac,method="trf",tr_solver="lsmr",
                          tr_options={"maxiter":it,"atol":2e-7,"btol":2e-7},max_nfev=nfev,
                          ftol=1e-10,xtol=1e-10,gtol=1e-10,x_scale=1.)
        z=sol.x;info=[int(sol.status),int(sol.nfev),float(sol.cost),float(sol.optimality)]
    else:z=zero;info=[0,0,float(np.linalg.norm(study.fun(z))**2/2),0.]
    return z.reshape(-1,3),{"seed":before,"fit":study.report(z),"status":info}
