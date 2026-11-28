#!/usr/bin/env python3
"""Full three-component Cartesian cap restoration against the original R764 tensor, with true roll continuation."""
import numpy as np
from scipy.optimize import least_squares
from scipy.sparse import csr_matrix,vstack
from scipy.sparse.linalg import LinearOperator
import solve_r764_corrugated_whole_sphere as oldfit
import r777_bent_complete_caps_and_true_terminal_collars as g
from r742_tilted_disk_two_jets import J,unary,cap_s7

# A partition of unity over physical coordinates; degree-three splines, full tip and outside overlaps.
LEVELS=((6,8,18,32),(10,14,28,44),(16,22,42,64))
SCALE=1e-5

def shaped(j):
    return [np.broadcast_to(w,j.v.shape)[:,None] for w in j.parts()[1:]]

def cardinal(x,n,lo,hi):
    a=(x-lo)*(n/(hi-lo))
    return oldfit.cardinal(J(a.v[:,None]-np.arange(-1,n+2)[None,:],*shaped(a)))

def lifted(j):
    return J(*(np.asarray(x)[:,None] for x in np.broadcast_arrays(*j.parts())))

def cap_basis(chart,a,b,order,nx,nz):
    count=len(a);p=(nx+3)*(nz+3)+4
    if chart=="cylinder" or chart.startswith("preband") or (chart.startswith("round") and np.max(b)<=g.L-.12):
        return np.zeros((count,6,p))
    ref=g.base.chart_jet(chart,a,b,0.,order,.14,False);x,y,z=g.rawparts(ref)
    side=1 if chart.endswith("+") else -1
    gate=cap_s7((J(b,a=1.)-g.L+.12)/.10) if chart.startswith("round") else J(np.ones(count))
    xx=cardinal(x,nx,-1.8,1.15);zz=cardinal(z,nz,-1.6,1.6)
    xx=J(*(t[:,:,None] for t in np.broadcast_arrays(*xx.parts())))
    zz=J(*(t[:,None,:] for t in np.broadcast_arrays(*zz.parts())))
    product=xx*zz
    add=J(*(t.reshape(count,-1) for t in np.broadcast_arrays(*product.parts())))*lifted(gate)
    result=np.zeros((count,6,p))
    for i,t in enumerate(add.parts()):result[:,i,:-4]=t*SCALE
    if chart.startswith("cap"):
        f=side*y-(g.B+g.base.axial(order)+g.m.terminal(order)[0])
        # The actual f and its two-jets vanish at the true cap rim, so zero is its correct roll continuation.
        for j,col in enumerate((f,f*x,f*z,f*x*z)):
            for i,t in enumerate(col.parts()):result[:,i,-4+j]=t
    return result

def weighted_jet(chart,a,b,ph,order,mode,shape,z):
    cur=g.chart_jet(chart,a,b,ph,order,mode,False)
    if z is None or (chart=="cylinder" or chart.startswith("preband")):return cur
    sh=cur.shape;cur=cur.reshape(-1,6,3)
    a,b=np.broadcast_arrays(np.asarray(a),np.asarray(b));a,b=a.ravel(),b.ravel()
    side=1 if chart.endswith("+") else -1
    for i in range(0,len(a),96):
        ix=slice(i,i+96)
        h=cap_basis(chart,a[ix],b[ix],order,*shape)
        corr=h@z;corr[:,:,1]*=side;cur[ix]+=corr
    return cur.reshape(sh)

class CapMetric:
    def __init__(self,fields,phase,order,mode,shape):
        A=[];D=[];J1=[];J2=[];self.blocks={}
        for name,ss,vv in fields:
            lo=len(A);amount=0
            for i in range(0,ss.size,96):
                s=ss.ravel()[i:i+96];v=vv.ravel()[i:i+96]
                old=g.base.chart_jet(name,s,v,0.,order,.14,False)
                now=g.chart_jet(name,s,v,phase,order,mode,False)
                if name.endswith("-"):now[:,:,1]*=-1
                r,t=old[:,1],old[:,2];nr=np.linalg.norm(r,axis=1);e=r/nr[:,None]
                shear=np.einsum("ij,ij->i",e,t);nv=np.linalg.norm(t-shear[:,None]*e,axis=1)
                H=cap_basis(name,s,v,order,*shape)
                A.append(now[:,1]/nr[:,None]);D.append((now[:,2]-shear[:,None]*A[-1])/nv[:,None])
                ha=H[:,1]/nr[:,None];hd=(H[:,2]-shear[:,None]*ha)/nv[:,None]
                J1.append(csr_matrix(ha));J2.append(csr_matrix(hd));amount+=len(s)
            self.blocks[name]=amount
        self.a=np.vstack(A);self.d=np.vstack(D);self.ha=vstack(J1,format="csr");self.hd=vstack(J2,format="csr")
        self.p=self.ha.shape[1];self.weight=np.hstack([np.full(n,1/np.sqrt(n)) for n in self.blocks.values()])
    def state(self,z):
        zz=z.reshape(self.p,3);a=self.a+self.ha@zz;d=self.d+self.hd@zz
        dot=lambda x,y:np.einsum("ij,ij->i",x,y)
        return a,d,np.column_stack((dot(a,a)-1,dot(a,d),dot(d,d)-1))
    def fun(self,z):
        a,d,R=self.state(z)
        return np.r_[(R*(1e6*self.weight[:,None])*np.array([1.,np.sqrt(2.),1.])).ravel(),1e-6*z]
    def jac(self,z):
        a,d,_=self.state(z);p=self.p;w=1e6*self.weight[:,None];rt=np.sqrt(2.)
        def mv(v):
            v=np.asarray(v).ravel();t=v.reshape(p,3);u=self.ha@t;v2=self.hd@t
            mul=lambda x,y:np.einsum("ij,ij->i",x,y)
            return np.r_[(w*np.column_stack((2*mul(a,u),rt*(mul(a,v2)+mul(d,u)),2*mul(d,v2)))).ravel(),1e-6*v]
        def rv(v):
            v=np.asarray(v).ravel();r=w*v[:-3*p].reshape(-1,3)
            u=2*r[:,0,None]*a+rt*r[:,1,None]*d;t=rt*r[:,1,None]*a+2*r[:,2,None]*d
            return (self.ha.T@u+self.hd.T@t).ravel()+1e-6*v[-3*p:]
        return LinearOperator((3*(len(a)+p),3*p),matvec=mv,rmatvec=rv,dtype=float)
    def report(self,z):
        R=self.state(z)[2];half=.5*(R[:,0]+R[:,2]);rad=np.hypot(.5*(R[:,0]-R[:,2]),R[:,1])
        op=np.maximum(abs(half-rad),abs(half+rad));out={};start=0
        for name,count in self.blocks.items():
            sl=slice(start,start+count);k=int(np.argmax(op[sl]))
            out[name]=[count,float(op[start+k]),k,*np.max(abs(R[sl]),axis=0).tolist()]
            start+=count
        return out

def get_fields(axes,level,ph,audit):
    out=[]
    for name,(s,v) in zip(oldfit.CHARTS,axes(level,ph,audit)):
        if name.startswith("cap"):
            out.append((name,s,v))
        elif name.startswith("round"):
            k=v[0]>=g.L-g.EDGE;out.append((name,s[:,k],v[:,k]))
    return out

def restore(axes,level,index,ph,mode,fit,seed):
    nx,nz,nfev,maxit=LEVELS[index]
    p=(nx+3)*(nz+3)+4
    z=np.zeros(3*p) if seed is None else seed.ravel().copy()
    Z=np.zeros_like(z)
    study=CapMetric(get_fields(axes,level,ph,False),ph,level[2],mode,(nx,nz));before=study.report(Z)
    if fit and ph:
        if np.linalg.norm(study.fun(z))>np.linalg.norm(study.fun(Z)):z=Z
        res=least_squares(study.fun,z,jac=study.jac,method="trf",tr_solver="lsmr",
             tr_options={"maxiter":maxit,"atol":1e-8,"btol":1e-8},max_nfev=nfev,
             ftol=1e-12,xtol=1e-12,gtol=1e-12,x_scale=1.)
        z=res.x;status=[int(res.status),int(res.nfev),float(res.cost),float(res.optimality)]
    else:status=None
    fitted=study.report(z);del study
    audit=CapMetric(get_fields(axes,level,ph,True),ph,level[2],mode,(nx,nz))
    return z.reshape(p,3),{"phase":ph,"zero_fit":before,"fitted":fitted,"independent":audit.report(z),
                           "independent_uncorrected":audit.report(Z),"status":status}
