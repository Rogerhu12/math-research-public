"""Scratch three-field Gauss--Codazzi boundary value optimizer.

Coordinates: g=ds^2+a(s)^2 du^2; u has period 2*pi. L,N use
cos(2*k*u), M uses sin(2*k*u). Initial ellipse curvature is retained
without truncation via a fixed boundary lift. The unknowns are radial
B-spline coefficients and meridian length. No division by N occurs.

This is a prototype; a small collocation residual alone does not prove
existence, closure, embedding, or reach.
"""
import argparse
import hashlib
import json
import time
import numpy as np
from scipy.interpolate import BSpline
from scipy.linalg import null_space
from scipy.integrate import cumulative_trapezoid, simpson
from scipy.optimize import least_squares
from gc_prefix_explore import initial


def smooth5(t):
    return t**3*(10+t*(-15+6*t))


def dsmooth5(t):
    return 30*t*t*(1-t)**2


def make_spline(nc, degree, x):
    internal=np.linspace(0.,1.,nc-degree+1)[1:-1]
    knots=np.r_[np.zeros(degree+1),internal,np.ones(degree+1)]
    sp=BSpline(knots,np.eye(nc),degree)
    mats=[sp(x,nu=j) for j in range(4)]
    return sp,mats


class Problem:
    def __init__(self,B=.9,A=1.,rc=.25,nc=12,K=2,nr=None,nu=None,
                 degree=5,curv=12.,curv_weight=.1,flare=0.,oscillation=0.,waves=2,length_max=3.5):
        self.B,self.A,self.rc,self.nc,self.K,self.degree=B,A,rc,nc,K,degree
        self.curv,self.curv_weight=curv,curv_weight
        self.length_max=length_max
        self.nr=nr or (2*nc+1)
        self.nu=nu or max(32,8*(K+1))
        # Chebyshev-Lobatto values include endpoint compatibility equations.
        self.x=(1-np.cos(np.linspace(0,np.pi,self.nr)))/2
        self.u=2*np.pi*np.arange(self.nu)/self.nu
        self.sp,self.Bmat=make_spline(nc,degree,self.x)
        ep=np.array([0.,1.])
        ev=self.sp(ep);ed=self.sp(ep,nu=1);edd=self.sp(ep,nu=2)
        et=self.sp(ep,nu=3)
        # a: value, first/second derivatives at both ends, third derivative
        # at the planar end. The latter follows if all b-components vanish
        # and the solution is differentiable there.
        self.BCa=np.stack([ev[0],ed[0],edd[0],ev[1],ed[1],edd[1],et[1]])
        self.Za=null_space(self.BCa)
        self.ZL=null_space(ev)
        self.ZMN=null_space(np.stack([ev[0],ed[0],ev[1],ed[1]]))
        self.nL,self.nMN,self.na=self.ZL.shape[1],self.ZMN.shape[1],self.Za.shape[1]
        self.a0,y0=initial(A,B,self.nu)
        self.Ninitial=y0[self.nu:2*self.nu]
        self.Xinitial=y0[2*self.nu:5*self.nu].reshape(3,self.nu)
        self.e1initial=y0[5*self.nu:8*self.nu].reshape(3,self.nu)
        self.e2initial=y0[8*self.nu:11*self.nu].reshape(3,self.nu)
        bc=np.array([self.a0,0.,0.,rc,0.,0.,0.])
        bcl=np.array([0.,0.,0.,0.,-1.,0.,0.])
        self.apart=np.linalg.lstsq(self.BCa,bc,rcond=None)[0]
        self.apartS=np.linalg.lstsq(self.BCa,bcl,rcond=None)[0]
        self.BL=self.Bmat[0]@self.ZL
        self.BMN=self.Bmat[0]@self.ZMN
        self.BMNx=self.Bmat[1]@self.ZMN
        self.BA=[b@self.Za for b in self.Bmat[:3]]
        ks=2*np.arange(K+1)
        self.C=np.cos(self.u[:,None]*ks[None,:])
        self.Cu=-np.sin(self.u[:,None]*ks[None,:])*ks[None,:]
        self.Si=np.sin(self.u[:,None]*ks[None,1:])
        self.Siu=np.cos(self.u[:,None]*ks[None,1:])*ks[None,1:]
        self.lift=1-smooth5(self.x)
        self.liftx=-dsmooth5(self.x)
        sizes=[self.nL*(K+1),self.nMN*K,self.nMN*(K+1),self.na,1]
        ends=np.cumsum([0]+sizes)
        self.sl=[slice(ends[i],ends[i+1]) for i in range(5)]
        self.nvar=int(ends[-1])
        self.ngrid=self.nr*self.nu
        def prod(b,c):
            return np.einsum('ri,uj->ruij',b,c).reshape(self.ngrid,-1)
        self.DL=np.zeros((self.ngrid,self.nvar));self.DLu=self.DL.copy()
        self.DM=self.DL.copy();self.DMu=self.DL.copy();self.DMx=self.DL.copy()
        self.DN=self.DL.copy();self.DNx=self.DL.copy()
        self.DL[:,self.sl[0]]=prod(self.BL,self.C)
        self.DLu[:,self.sl[0]]=prod(self.BL,self.Cu)
        self.DM[:,self.sl[1]]=prod(self.BMN,self.Si)
        self.DMu[:,self.sl[1]]=prod(self.BMN,self.Siu)
        self.DMx[:,self.sl[1]]=prod(self.BMNx,self.Si)
        self.DN[:,self.sl[2]]=prod(self.BMN,self.C)
        self.DNx[:,self.sl[2]]=prod(self.BMNx,self.C)
        self.Nbase=(self.lift[:,None]*self.Ninitial).ravel()
        self.Nbasex=(self.liftx[:,None]*self.Ninitial).ravel()
        self.DAs=[]
        self.aparts=[];self.apartsS=[]
        for j in range(3):
            da=np.zeros((self.ngrid,self.nvar))
            da[:,self.sl[3]]=np.repeat(self.BA[j],self.nu,axis=0)
            da[:,-1]=np.repeat(self.Bmat[j]@self.apartS,self.nu)
            self.DAs.append(da)
            self.aparts.append(np.repeat(self.Bmat[j]@self.apart,self.nu))
            self.apartsS.append(da[:,-1])
        # Scaling quadrature-like weights so angular sampling does not alter
        # the relative curvature penalty.
        self.wres=1/np.sqrt(self.ngrid)
        self.last=None
        self.initial_vector=self.make_initial(flare,oscillation,waves)

    def make_initial(self,flare,oscillation,waves):
        fine=np.linspace(0,1,4001)
        # Flare is a smooth, initial negative meridian-angle excursion.
        bump=256*fine**4*(1-fine)**4
        theta=np.pi/2*smooth5(fine)-flare*bump+oscillation*16*fine*fine*(1-fine)**2*np.sin(2*np.pi*waves*fine)
        integ=simpson(np.sin(theta),x=fine)
        length=(self.a0-self.rc)/integ
        a=self.a0-length*cumulative_trapezoid(np.sin(theta),fine,initial=0)
        thetax=np.gradient(theta,fine,edge_order=2)
        l=thetax/length
        n=a*np.cos(theta)
        vals=[np.interp(self.x,fine,z) for z in [a,l,n]]
        p=np.zeros(self.nvar);p[-1]=length
        pa=self.apart+length*self.apartS
        p[self.sl[3]]=np.linalg.lstsq(self.BA[0],vals[0]-self.Bmat[0]@pa,rcond=None)[0]
        lc=np.zeros((self.nL,self.K+1))
        lc[:,0]=np.linalg.lstsq(self.BL,vals[1],rcond=None)[0]
        p[self.sl[0]]=lc.ravel()
        # Mean correction plus fixed nonradial boundary lift.
        nc=np.zeros((self.nMN,self.K+1))
        nc[:,0]=np.linalg.lstsq(self.BMN,vals[2]-self.a0*self.lift,rcond=None)[0]
        p[self.sl[2]]=nc.ravel()
        return p

    def unpack(self,p):
        length=p[-1]
        L=self.DL@p;Lu=self.DLu@p
        M=self.DM@p;Mu=self.DMu@p;Mx=self.DMx@p
        N=self.Nbase+self.DN@p;Nx=self.Nbasex+self.DNx@p
        a=self.aparts[0]+self.DAs[0]@p
        ax=self.aparts[1]+self.DAs[1]@p
        axx=self.aparts[2]+self.DAs[2]@p
        ap=ax/length;app=axx/length**2
        Ms=Mx/length;Ns=Nx/length
        return length,L,Lu,M,Mu,N,Ms,Ns,a,ap,app

    def evaluate(self,p,need_jac=True):
        if self.last is not None and np.array_equal(p,self.last[0]):
            return self.last[1],self.last[2],self.last[3]
        length,L,Lu,M,Mu,N,Ms,Ns,a,ap,app=self.unpack(p)
        aa=np.maximum(a,.05)
        q=ap/aa
        G=L*N-M*M+a*app
        CM=Ms-Lu+q*M
        CN=Ns-Mu-q*N-a*ap*L
        Rg=G/aa**2;Rm=CM/aa;Rn=CN/aa**2
        l=L;m=M/aa;n=N/aa**2
        tsum=l+n;tdif=l-n
        er=1e-12
        rad=np.sqrt(tdif**2+4*m*m+er)
        abst=np.sqrt(tsum**2+er)
        kmax=(abst+rad)/2
        kpen=np.maximum(kmax-self.curv,0.)
        apos=np.maximum(.15-a,0.)
        residual=np.concatenate([Rg,Rm,Rn,self.curv_weight*kpen,10*apos])*self.wres
        da=self.DAs[0].copy()
        da[a<.05]=0 # derivative of safe denominator, not numerator
        dap=self.DAs[1]/length
        dap[:,-1]-=ap/length
        dapp=self.DAs[2]/length**2
        dapp[:,-1]-=2*app/length
        dMs=self.DMx/length;dMs[:,-1]-=Ms/length
        dNs=self.DNx/length;dNs[:,-1]-=Ns/length
        dq=dap/aa[:,None]-ap[:,None]*da/aa[:,None]**2
        dG=N[:,None]*self.DL+L[:,None]*self.DN-2*M[:,None]*self.DM \
            +app[:,None]*self.DAs[0]+a[:,None]*dapp
        dCM=dMs-self.DLu+q[:,None]*self.DM+M[:,None]*dq
        dCN=dNs-self.DMu-q[:,None]*self.DN-N[:,None]*dq \
            -(a*ap)[:,None]*self.DL-L[:,None]*(ap[:,None]*self.DAs[0]+a[:,None]*dap)
        dRg=dG/aa[:,None]**2-2*G[:,None]*da/aa[:,None]**3
        dRm=dCM/aa[:,None]-CM[:,None]*da/aa[:,None]**2
        dRn=dCN/aa[:,None]**2-2*CN[:,None]*da/aa[:,None]**3
        dl=self.DL
        dm=self.DM/aa[:,None]-M[:,None]*da/aa[:,None]**2
        dn=self.DN/aa[:,None]**2-2*N[:,None]*da/aa[:,None]**3
        dk=.5*((tsum/abst)[:,None]*(dl+dn)+(tdif/rad)[:,None]*(dl-dn)
               +(4*m/rad)[:,None]*dm)
        dk[kmax<=self.curv]=0
        dapos=-self.DAs[0].copy();dapos[a>=.15]=0
        jac=np.vstack([dRg,dRm,dRn,self.curv_weight*dk,10*dapos])*self.wres
        stats=dict(length=float(length),residual_max=float(max(abs(Rg).max(),abs(Rm).max(),abs(Rn).max())),
                   gauss_max=float(abs(Rg).max()),codazzi_M_max=float(abs(Rm).max()),codazzi_N_max=float(abs(Rn).max()),
                   pde_rms=float(np.sqrt(np.mean(np.r_[Rg,Rm,Rn]**2))),
                   a_min=float(a.min()),a_max=float(a.max()),ap_min=float(ap.min()),ap_max=float(ap.max()),
                   curvature_max=float(kmax.max()),N_min=float(N.min()),M_max=float(abs(M).max()),
                   L_min=float(L.min()),L_max=float(L.max()))
        self.last=(p.copy(),residual,jac,stats)
        return residual,jac,stats

    def solve(self,p=None,max_nfev=500,verbose=0):
        if p is None:p=self.initial_vector.copy()
        lb=np.full(self.nvar,-100.);ub=np.full(self.nvar,100.)
        lb[-1]=max(.1,self.a0-self.rc+.001);ub[-1]=self.length_max
        p=p.copy();p[-1]=np.clip(p[-1],lb[-1]+1e-8,ub[-1]-1e-8)
        start=time.time()
        ans=least_squares(lambda p:self.evaluate(p)[0],p,jac=lambda p:self.evaluate(p)[1],
                          bounds=(lb,ub),method='trf',x_scale='jac',ftol=1e-11,
                          xtol=1e-11,gtol=1e-11,max_nfev=max_nfev,verbose=verbose)
        stats=self.evaluate(ans.x)[2]
        stats.update(nfev=ans.nfev,njev=ans.njev,cost=float(ans.cost),optimality=float(ans.optimality),
                     message=ans.message,seconds=time.time()-start)
        return ans.x,stats

    def save(self,path,p,stats):
        obj=dict(params={k:getattr(self,k) for k in ['A','B','rc','nc','K','nr','nu','degree','curv','curv_weight','length_max']},
                 a0=self.a0,coefficients=p.tolist(),statistics=stats)
        with open(path,'w') as f:json.dump(obj,f,indent=2)

    def transfer(self,old,pold):
        """Interpolate a previous small-text checkpoint onto this basis."""
        x=np.linspace(0,1,max(401,20*self.nc))
        bo=old.sp(x);bn=self.sp(x)
        p=np.zeros(self.nvar);S=pold[-1];p[-1]=S
        for block,zo,zn,kold,knew in [(0,old.ZL,self.ZL,old.K+1,self.K+1),
                                      (1,old.ZMN,self.ZMN,old.K,self.K),
                                      (2,old.ZMN,self.ZMN,old.K+1,self.K+1)]:
            co=pold[old.sl[block]].reshape(zo.shape[1],kold)
            target=bo@zo@co
            cn=np.zeros((zn.shape[1],knew))
            common=min(kold,knew)
            if common:
                cn[:,:common]=np.linalg.lstsq(bn@zn,target[:,:common],rcond=None)[0]
            p[self.sl[block]]=cn.ravel()
        ao=bo@(old.apart+S*old.apartS+old.Za@pold[old.sl[3]])
        anpart=bn@(self.apart+S*self.apartS)
        p[self.sl[3]]=np.linalg.lstsq(bn@self.Za,ao-anpart,rcond=None)[0]
        return p


def main():
    ag=argparse.ArgumentParser()
    ag.add_argument('--B',type=float,default=.9)
    ag.add_argument('--nc',type=int,default=12)
    ag.add_argument('--K',type=int,default=2)
    ag.add_argument('--nr',type=int)
    ag.add_argument('--nu',type=int)
    ag.add_argument('--flare',type=float,default=.4)
    ag.add_argument('--oscillation',type=float,default=0.)
    ag.add_argument('--waves',type=int,default=2)
    ag.add_argument('--length-max',type=float,default=3.5)
    ag.add_argument('--curv',type=float,default=12.)
    ag.add_argument('--curv-weight',type=float,default=.1)
    ag.add_argument('--max-nfev',type=int,default=500)
    ag.add_argument('--verbose',type=int,default=0)
    ag.add_argument('--output',default='gc_bvp_result.json')
    ag.add_argument('--resume')
    args=vars(ag.parse_args())
    maxfev=args.pop('max_nfev');verb=args.pop('verbose');out=args.pop('output');resume=args.pop('resume')
    pr=Problem(**args)
    p=pr.initial_vector
    if resume:
        with open(resume) as f:d=json.load(f)
        old=Problem(**d['params'])
        p=pr.transfer(old,np.array(d['coefficients']))
    print(json.dumps(dict(stage='initial',variables=pr.nvar,**pr.evaluate(p)[2])),flush=True)
    p,stats=pr.solve(p,max_nfev=maxfev,verbose=verb)
    pr.save(out,p,stats)
    print(json.dumps(dict(stage='final',**stats)),flush=True)
    print('sha256',hashlib.sha256(open(out,'rb').read()).hexdigest(),flush=True)


if __name__=='__main__':main()
