"""Planar threefold core with an independently defined exact circular arc.

The defining rho, compact support bases and integral definition are retained;
a finite Fourier projection is never identified with the exact core curve.
Floating evaluations of the defining integrals use Gauss quadrature. Numerical
positivity/rank outputs are diagnostics, not interval certificates.
"""
from __future__ import annotations
import math
import numpy as np
from numpy.polynomial import Polynomial


class PlateauSupportCore:
    def __init__(self, q=.025, corrections=(), base_mode=3, *, halfwidth=.20,
                 transition=.10, homotopy=1., center=0., arc_nodes=4096):
        if base_mode != 3: raise ValueError('This prototype uses exactly threefold symmetry')
        self.base_mode=3; self.T=2*np.pi/3; self.q=float(q); self.support_amplitude=self.q
        self.corrections=tuple(float(c) for c in corrections); self.c=np.asarray(self.corrections)
        self.a=float(halfwidth); self.transition=float(transition); self.lam=float(homotopy)
        self.center=float(center)%self.T
        if min(abs(self.center),abs(self.center-self.T/2))>1e-12:
            raise ValueError('Reflection-preserving center must be 0 or pi/3')
        if not 0<self.a<self.a+self.transition<self.T/2 or not 0<=self.lam<=1 or q<=0:
            raise ValueError('Invalid plateau geometry')
        self.sign=-1 if abs(self.center)<1e-12 else 1
        self.mean_chi=(2*self.a+self.transition)/self.T
        self.target_min=min(self.sign*8.,-self.sign*8*self.mean_chi/(1-self.mean_chi))
        self.target_max=max(self.sign*8.,-self.sign*8*self.mean_chi/(1-self.mean_chi))
        self.rho_lower=1+self.q*((1-self.lam)*(-8)+self.lam*self.target_min)-sum(abs(self.c))
        self.rho_upper=1+self.q*((1-self.lam)*8+self.lam*self.target_max)+sum(abs(self.c))
        self.rho_triangle_lower=self.rho_lower
        # Each local basis is b_j=f_j', where f_j is a compactly supported odd
        # bump about the complementary arc midpoint. Thus integral b_j=0
        # exactly and its rho perturbation is f_j'+f_j'''.
        B=Polynomial([0]*6+[1])*Polynomial([1,-1])**6*4096
        self.polys=[B.deriv(k) for k in range(6)]
        def pmax(p):
            roots=p.deriv().roots(); xs=[0.,1.]+[float(r.real) for r in roots if abs(r.imag)<1e-8 and 0<r.real<1]
            return max(abs(p(np.array(xs))))*(1+1e-9)
        self.Pmax=np.array([pmax(p) for p in self.polys]); self.L=self.T-2*self.a
        self.omega=2*np.pi*np.arange(1,len(self.c)+1)
        w=self.omega;P=self.Pmax;L=self.L
        self.norms=(P[1]+w*P[0])/L+(P[3]+3*w*P[2]+3*w*w*P[1]+w**3*P[0])/L**3
        Dnorm=((P[2]+2*w*P[1]+w*w*P[0])/L**2+(P[4]+4*w*P[3]+6*w*w*P[2]+4*w**3*P[1]+w**4*P[0])/L**4)/self.norms
        self.rho_derivative_bound=self.q*((1-self.lam)*24+self.lam*15/(self.transition*(1-self.mean_chi)))+float(np.sum(abs(self.c)*Dnorm))
        count=512
        while True:
            grid=self.T*np.arange(count)/count;ff=self._basis(grid);rr=1+self.q*self.unit_rho(grid)+self.c@(ff[1]+ff[3]);slack=self.T/(2*count)*self.rho_derivative_bound
            self.rho_lower=max(self.rho_triangle_lower,float(rr.min()-slack));self.rho_upper=min(self.rho_upper,float(rr.max()+slack));self.positivity_grid_per_sector=count
            if self.rho_lower>1e-5:break
            if rr.min()<=1e-5 or count>=32768:raise FloatingPointError('Core rho positivity failed: '+str((float(rr.min()),self.rho_lower,count)))
            count*=2
        self.gx,self.gw=np.polynomial.legendre.leggauss(32)
        marks=[0.,self.T,self.center]
        for v in (-self.a-self.transition,-self.a,self.a,self.a+self.transition):marks.append((self.center+v)%self.T)
        self.breaks=np.unique(np.array(marks)); self.cum=np.zeros((len(self.breaks),3))
        for i,(lo,hi) in enumerate(zip(self.breaks[:-1],self.breaks[1:])):
            self.cum[i+1]=self.cum[i]+self._quad(lo,np.array([hi]))[0]
        self.period_integral_roundoff=float(self.cum[-1,0]); self.cum[-1,0]=0.
        R=np.array([[math.cos(self.T),-math.sin(self.T)],[math.sin(self.T),math.cos(self.T)]])
        self.unit_origin=np.linalg.solve(R-np.eye(2),self.cum[-1,1:])
        self.f0,self.f20=self._basis(np.array([0.]))[0][:,0],self._basis(np.array([0.]))[2][:,0]
        phi=2*np.pi*np.arange(arc_nodes)/arc_nodes;g=self.normal_geometry(phi);rho=g['rho']
        self.rho_min_sample=float(rho.min());self.rho_max_sample=float(rho.max())
        self.minimum_sampled_curvature=1/self.rho_max_sample;self.maximum_sampled_curvature=1/self.rho_min_sample
        self.curvature_upper_bound=1/self.rho_lower;self.curvature_lower_bound=1/self.rho_upper
        self.radius_max_sample=float(np.linalg.norm(g['F'],axis=1).max());self.radius_min_sample=float(np.linalg.norm(g['F'],axis=1).min())
        self.radius_upper_bound=self.radius_max_sample+2*np.pi/arc_nodes*self.rho_upper
        self.radius_lower_bound=max(0,self.radius_min_sample-2*np.pi/arc_nodes*self.rho_upper)
        self.constant_width_exact=False;self.width_defect_bound=math.nan
        width=g['h']+self.normal_geometry(phi+np.pi)['h'];self.width_min_sample=float(width.min());self.width_max_sample=float(width.max())
        self.support_monotone=False;self.coefficients=np.r_[q,self.c];self.frequencies=3*np.arange(1,len(self.c)+2)
        self._last_theta=None;self._last_evaluation=None

    def chi(self,phi):
        d=np.abs((np.asarray(phi)-self.center+self.T/2)%self.T-self.T/2)
        t=np.clip((d-self.a)/self.transition,0,1)
        return 1-t**3*(10+t*(-15+6*t))

    def unit_rho(self,phi):
        target=self.sign*8*(self.chi(phi)-self.mean_chi)/(1-self.mean_chi)
        return (1-self.lam)*(-8*np.cos(3*np.asarray(phi)))+self.lam*target

    def _quad(self,lo,hi):
        hi=np.asarray(hi);x=(hi[...,None]+lo)/2+(hi[...,None]-lo)/2*self.gx
        u=self.unit_rho(x);v=np.stack((u,-u*np.sin(x),u*np.cos(x)),axis=-1)
        return (hi-lo)[...,None]/2*np.einsum('...ij,i->...j',v,self.gw)

    def unit_geometry(self,phi):
        phi=np.asarray(phi,float);flat=phi.ravel();sector=np.floor(flat/self.T);local=flat-sector*self.T
        index=np.clip(np.searchsorted(self.breaks,local,side='right')-1,0,len(self.breaks)-2)
        integral=np.empty((len(flat),3))
        for j in range(len(self.breaks)-1):
            mask=index==j
            if np.any(mask):integral[mask]=self.cum[j]+self._quad(self.breaks[j],local[mask])
        xy=self.unit_origin+integral[:,1:];a=sector*self.T;co=np.cos(a);si=np.sin(a)
        rotated=np.c_[co*xy[:,0]-si*xy[:,1],si*xy[:,0]+co*xy[:,1],np.zeros(len(flat))]
        return integral[:,0].reshape(phi.shape),rotated.reshape(phi.shape+(3,))

    def _basis(self,phi):
        phi=np.asarray(phi,float);flat=phi.ravel();z=(flat-self.center-self.a)%self.T;inside=z<self.L;t=np.clip(z/self.L,0,1)
        if len(self.c)==0:return tuple(np.empty((0,len(flat))) for _ in range(4))
        w=self.omega[:,None];ang=w*t[None,:];sn=np.sin(ang);co=np.cos(ang);P=[p(t)[None,:] for p in self.polys]
        f=P[0]*sn
        f1=(P[1]*sn+w*P[0]*co)/self.L
        f2=(P[2]*sn+2*w*P[1]*co-w*w*P[0]*sn)/self.L**2
        f3=(P[3]*sn+3*w*P[2]*co-3*w*w*P[1]*sn-w**3*P[0]*co)/self.L**3
        return tuple(np.where(inside[None,:],x/self.norms[:,None],0.) for x in (f,f1,f2,f3))

    def rho_material_jets(self,theta):
        g=self.evaluate(theta);phi=g['phi'];rho=1/g['kappa']
        d=(phi-self.center+self.T/2)%self.T-self.T/2
        t=np.clip((abs(d)-self.a)/self.transition,0.,1.)
        chip=-30*t*t*(1-t)**2*np.sign(d)/self.transition
        chipp=-60*t*(1-t)*(1-2*t)/self.transition**2
        rp=self.q*((1-self.lam)*24*np.sin(3*phi)+self.lam*self.sign*8*chip/(1-self.mean_chi))
        rpp=self.q*((1-self.lam)*72*np.cos(3*phi)+self.lam*self.sign*8*chipp/(1-self.mean_chi))
        z=(phi-self.center-self.a)%self.T;inside=z<self.L;t=np.clip(z/self.L,0.,1.)
        if len(self.c):
            w=self.omega[:,None];v=w*t[None,:]
            def fj(j):
                ans=sum(math.comb(j,l)*self.polys[j-l](t)[None,:]*w**l*np.sin(v+l*np.pi/2) for l in range(j+1))/self.L**j
                return np.where(inside[None,:],ans/self.norms[:,None],0.)
            rp+=self.c@(fj(2)+fj(4));rpp+=self.c@(fj(3)+fj(5))
        ru=rp/rho;ruu=(rpp*rho-rp*rp)/rho**3
        return dict(**g,rho=rho,rho_u=ru,rho_uu=ruu,rho_phi=rp,rho_phiphi=rpp,normal=np.c_[np.cos(phi),np.sin(phi),np.zeros_like(phi)])

    def normal_geometry(self,phi):
        phi=np.asarray(phi,float);U,V=self.unit_geometry(phi);f,f1,f2,f3=self._basis(phi)
        n=np.stack((np.cos(phi),np.sin(phi),np.zeros_like(phi)),axis=-1);t=np.stack((-np.sin(phi),np.cos(phi),np.zeros_like(phi)),axis=-1)
        b=(self.c@f1).reshape(phi.shape);bp=(self.c@f2).reshape(phi.shape)
        F=n+self.q*V+b[...,None]*n+bp[...,None]*t
        rho=1+self.q*self.unit_rho(phi)+(self.c@(f1+f3)).reshape(phi.shape)
        return dict(F=F,h=np.sum(F*n,axis=-1),hp=np.sum(F*t,axis=-1),rho=rho,er=n,et=t,U=U,V=V)

    def arc(self,phi):
        phi=np.asarray(phi,float);U,_=self.unit_geometry(phi);f,_,f2,_=self._basis(phi)
        return phi+self.q*U+(self.c@(f+f2-self.f0[:,None]-self.f20[:,None])).reshape(phi.shape)

    def evaluate(self,theta):
        theta=np.asarray(theta,float)
        if self._last_theta is not None and np.array_equal(theta,self._last_theta):return self._last_evaluation
        phi=theta.copy();lo=np.floor(theta/self.T)*self.T;hi=lo+self.T
        for it in range(80):
            g=self.normal_geometry(phi);r=self.arc(phi)-theta;done=abs(r)<2e-13
            if np.all(done):break
            lo=np.where((r<0)&~done,phi,lo);hi=np.where((r>0)&~done,phi,hi);v=phi-r/g['rho'];bad=(v<=lo)|(v>=hi)|~np.isfinite(v);phi=np.where(done,phi,np.where(bad,(lo+hi)/2,v))
        r=self.arc(phi)-theta
        if np.max(abs(r))>5e-12:raise FloatingPointError('Arc inverse residual '+str(np.max(abs(r))))
        g=self.normal_geometry(phi)
        ans=dict(F=g['F'],Ft=g['et'],Ftt=-g['er']/g['rho'][...,None],phi=phi,kappa=1/g['rho'],arc_residual=r,arc_iterations=it+1)
        self._last_theta=theta.copy();self._last_evaluation=ans;return ans

    def parameter_derivatives(self,theta):
        g=self.evaluate(theta);phi=g['phi'];U,V=self.unit_geometry(phi);f,f1,_,_=self._basis(phi)
        n=np.stack((np.cos(phi),np.sin(phi),np.zeros_like(phi)),axis=-1);t=np.stack((-np.sin(phi),np.cos(phi),np.zeros_like(phi)),axis=-1)
        first=V-U[...,None]*t
        rest=f1[:,:,None]*n[None,:,:]+(self.f0[:,None]+self.f20[:,None]-f)[:,:,None]*t[None,:,:]
        return np.concatenate((first[None,:,:],rest),axis=0)

    def summary(self):
        R=1+self.sign*8*self.q
        phi=np.array([self.center-self.a,self.center+self.a]);u=self.arc(phi)
        return dict(core_kind='exact_defined_plateau_integral',base_mode=3,q_parameter=self.q,
            corrections=list(self.corrections),halfwidth=self.a,transition=self.transition,homotopy=self.lam,
            center=self.center,exact_circle_only_at_homotopy_one=self.lam==1.,plateau_radius_at_one=R,
            plateau_normal_width=2*self.a,plateau_material_endpoints=u.tolist(),plateau_material_length=float(u[1]-u[0]),
            exact_perimeter=2*np.pi,rho_lower_conservative=self.rho_lower,rho_triangle_lower=self.rho_triangle_lower,positivity_grid_per_sector=self.positivity_grid_per_sector,rho_derivative_bound=self.rho_derivative_bound,rho_min_sample=self.rho_min_sample,
            rho_max_sample=self.rho_max_sample,curvature_max_sample=self.maximum_sampled_curvature,
            radius_max_sample=self.radius_max_sample,quadrature_period_roundoff=self.period_integral_roundoff,
            scope='Exact integral definition and independent evaluation; no Fourier truncation is called an exact circular arc.')
