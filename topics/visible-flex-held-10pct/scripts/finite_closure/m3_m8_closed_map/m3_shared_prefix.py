#!/usr/bin/env python3
"""Explicit shared-jet m3 prefix with analytic core and full Cartesian cut lifts.

Both lifts are exact Hermite constructions from full angular functions. Their
small floating audit residuals are evaluations of identities, never the reason
for C2 regularity. The physical metric and original frozen angular chart stay
fixed. No nonlinear solver is run here.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from types import SimpleNamespace
import importlib.util,json,math
import numpy as np
from scipy.interpolate import PPoly
from scipy.special import jv,jvp
from numpy.polynomial import Polynomial
from shared_jet import SharedJetQuintic,build_mean

H=np.array([[1,0,0,-10,15,-6],[0,1,0,-6,8,-3],
            [0,0,.5,-1.5,1.5,-.5]],float)

def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def load_prefix(source_topic,short_bridge,checkpoint,port_path,angular=512):
    source=Path(source_topic)
    ad=module('closed_m3_adaptive',source/'scripts/950f-prefix-adaptive-chart-bvp-v2.py')
    module('closed_m3_flat',source/'scripts/db6f-prefix-flat-profile.py').install(ad)
    ad.old.install_source(source/'repro/source-root')
    module('closed_m3_short',short_bridge).install()
    from curve_stable_prefix_bvp import load_checkpoint
    r=load_checkpoint(checkpoint)
    if not r['solver_success'] or r['config']['base_mode']!=3:
        raise ValueError('Accepted m3 prefix required')
    port=json.loads(Path(port_path).read_text())
    port['cut']['_prefix_bridge']=r['frozen_profile']['prefix_bridge']
    if port['parameters']!=r['physical_tail_parameters']or port['cut']!=r['physical_tail_cut']:
        raise ValueError('Different physical g/port')
    _,BVP=ad.build_classes(r['chart'])
    obj=BVP(r['frozen_profile'],port,r['gauge_amplitude'],r['config']['modes'],angular,True,r['warp_reference_q'])
    par=np.asarray(r['parameters']);par[0]=math.log(r['actual_primary_amplitude']/obj.q)
    obj.initial(par);flow=obj.flow(par[0])
    raw=PPoly.construct_fast(np.asarray(r['pp_coefficients']),np.asarray(r['mesh']),extrapolate=False,axis=1)
    rep=SharedJetQuintic.from_ppoly(raw)
    sol=SimpleNamespace(x=rep.x,y=rep(rep.x),p=par,sol=rep)
    sol.mean_spline=build_mean(flow,sol,angular,8)
    return r,obj,flow,sol,raw

def circle(theta,order=0):
    theta=np.asarray(theta);z=np.exp(1j*theta)*(1j**order)
    return np.stack([z.real,z.imag,np.zeros_like(z.real)],axis=-1)

class M3SharedPrefix:
    def __init__(self,obj,flow,sol,center_width=.04):
        self.obj,self.flow,self.sol=obj,flow,sol
        self.q,self.M,self.n=obj.q,obj.M,3
        self.modes=3*np.arange(1,self.M+1)
        self.core=obj._core;self.center_width=float(center_width)
        self.E0=float(flow.warp_e*flow.spline(0.))
        self.Epp=float(flow.warp_e*flow.spline(0.,2)/flow.end**2)
        if abs(float(flow.spline(0.,1)))>1e-14:raise ValueError('Expected zero inlet warp derivative')
        if not 0<self.center_width<flow.end:raise ValueError('Bad center width')
        self.end_lift=None;self._center_cache={}

    def coefficient_value(self,c,psi,order=0):
        psi=np.atleast_1d(np.asarray(psi,float));m=self.modes;M=self.M
        co=np.cos(psi[:,None]*m);si=np.sin(psi[:,None]*m)
        r=c[0]+co@c[1:M+1];t=si@c[M+1:2*M+1];z=co@c[2*M+1:]
        if order:
            rp=-si@(m*c[1:M+1]);tp=co@(m*c[M+1:2*M+1]);zp=-si@(m*c[2*M+1:])
        if order==1:r,t,z=rp-t,r+tp,zp
        elif order==2:
            rpp=-co@(m*m*c[1:M+1]);tpp=-si@(m*m*c[M+1:2*M+1]);zpp=-co@(m*m*c[2*M+1:])
            r,t,z=rpp-r-2*tp,tpp-t+2*rp,zpp
        return np.stack([r*np.cos(psi)-t*np.sin(psi),r*np.sin(psi)+t*np.cos(psi),z],axis=-1)

    def center_delta(self,psi):
        psi=np.atleast_1d(np.asarray(psi,float));n=3
        theta=psi-self.E0*np.sin(n*psi)/n
        rho=1-self.E0*np.cos(n*psi);rhop=n*self.E0*np.sin(n*psi)
        b=-self.Epp*np.sin(n*psi)/n;bp=-self.Epp*np.cos(n*psi);bpp=n*self.Epp*np.sin(n*psi)
        cg=self.core.evaluate(theta);ng=self.core.normal_geometry(cg['phi']);phi=cg['phi'];rc=ng['rho']
        rhop_core=-np.sin(phi[:,None]*self.core.frequencies)@(self.core.frequencies*(1-self.core.frequencies**2)*self.core.coefficients)
        gt=cg['Ft'];gtt=cg['Ftt']
        gttt=-ng['et']/rc[:,None]**2+ng['er']*rhop_core[:,None]/rc[:,None]**3
        er=circle(theta);et=circle(theta,1)
        Y,D,Q=self.sol.sol.jets[:,:,0];mu=self.sol.mean_spline.jets[:,0,0]
        result=[]
        for j in range(3):
            if j==0:
                d0=cg['F']-er-self.q*self.coefficient_value(Y,psi);d0[:,2]-=mu[0]
                d1=-self.q*self.coefficient_value(D,psi);d1[:,2]+=1-mu[1]
                d2=b[:,None]*(gt-et)-self.q*self.coefficient_value(Q,psi);d2[:,2]-=mu[2]
            elif j==1:
                d0=rho[:,None]*(gt-et)-self.q*self.coefficient_value(Y,psi,1)
                d1=-self.q*self.coefficient_value(D,psi,1)
                d2=bp[:,None]*(gt-et)+(b*rho)[:,None]*(gtt+er)-self.q*self.coefficient_value(Q,psi,1)
            else:
                d0=rho[:,None]**2*(gtt+er)+rhop[:,None]*(gt-et)-self.q*self.coefficient_value(Y,psi,2)
                d1=-self.q*self.coefficient_value(D,psi,2)
                d2=bpp[:,None]*(gt-et)+(2*bp*rho+b*rhop)[:,None]*(gtt+er)+(b*rho*rho)[:,None]*(gttt+et)-self.q*self.coefficient_value(Q,psi,2)
            result.append(np.stack([d0,d1,d2]))
        return result

    def center_weights(self,s,order):
        s=np.atleast_1d(np.asarray(s,float));t=np.clip(s/self.center_width,0,1)
        out=np.zeros((len(s),3));inside=s<=self.center_width
        for j in range(3):out[inside,j]=Polynomial(H[j]).deriv(order)(t[inside])*self.center_width**(j-order)
        return out

    def angular(self,s,psi):
        s,psi=np.broadcast_arrays(np.asarray(s,float),np.asarray(psi,float));x=s/self.flow.end
        t=np.clip((x-.75)/.25,0,1);fac=1/(.25*self.flow.end)
        cut=1-t**3*(10-15*t+6*t*t);cp=-30*t*t*(1-t)**2*fac;cpp=-60*t*(1-t)*(1-2*t)*fac*fac
        f=self.flow.spline;h=f(x);hp=f(x,1)/self.flow.end;hpp=f(x,2)/self.flow.end**2
        e=self.flow.warp_e*h*cut;ep=self.flow.warp_e*(hp*cut+h*cp);epp=self.flow.warp_e*(hpp*cut+2*hp*cp+h*cpp)
        sn=np.sin(3*psi);co=np.cos(3*psi)
        return psi-e*sn/3,1-e*co,3*e*sn,-ep*sn/3,-epp*sn/3,-ep*co

    def inverse_angle(self,s,theta):
        s,theta=np.broadcast_arrays(np.asarray(s,float),np.asarray(theta,float));psi=theta.copy()
        for _ in range(30):
            value,rho,*_=self.angular(s,psi);change=(value-theta)/rho;psi-=change
            if np.max(abs(change))<2e-15:break
        if np.max(abs(self.angular(s,psi)[0]-theta))>2e-13:raise ValueError('Material angle inversion failed')
        return psi

    def raw_grid(self,s,N):
        s=np.atleast_1d(np.asarray(s,float));B,B1,B2=self.flow.basis(N)
        Y,Yp,Ypp=[self.sol.sol(s,j)for j in range(3)];g=self.flow.geo(s,N)
        X=g['pos']+self.q*self.flow.values(Y,B);X[:,:,2]+=self.sol.mean_spline(s)[0,:,None]
        Xs=g['s1']+self.q*self.flow.values(Yp,B);Xs[:,:,2]+=self.sol.mean_spline(s,1)[0,:,None]
        Xss=g['s2']+self.q*self.flow.values(Ypp,B);Xss[:,:,2]+=self.sol.mean_spline(s,2)[0,:,None]
        Xp=g['p1']+self.q*self.flow.values(Y,B1)
        Xpp=g['p2']+self.q*self.flow.values(Y,B2);Xsp=g['sp']+self.q*self.flow.values(Yp,B1)
        return [X,Xs,Xss,Xp,Xpp,Xsp],g

    def grid(self,s,N):
        s=np.atleast_1d(np.asarray(s,float));jets,g=self.raw_grid(s,N)
        if np.any(s<=self.center_width):
            if N not in self._center_cache:self._center_cache[N]=self.center_delta(2*np.pi*np.arange(N)/N)
            d=self._center_cache[N];w=[self.center_weights(s,j)for j in range(3)]
            for x,(i,j)in zip(jets,[(0,0),(1,0),(2,0),(0,1),(0,2),(1,1)]):x+=np.einsum('sj,juk->suk',w[i],d[j])
        if self.end_lift is not None:
            add=self.end_lift.correction(s,2*np.pi*np.arange(N)/N)
            for x,y in zip(jets,add):x+=y
        return (*jets,g)

    def raw_endpoint_angular_jets(self,psi):
        # The frozen angular warp vanishes with two radial derivatives here.
        a,ap,app=[float(v[0])for v in self.flow.profile([self.flow.end])]
        Y,D,Q=self.sol.sol.jets[:,:,-1];mu=self.sol.mean_spline.jets[:,0,-1]
        out=[]
        for j in range(3):
            er=circle(psi,j)
            jets=np.stack([a*er+self.q*self.coefficient_value(Y,psi,j),
                           ap*er+self.q*self.coefficient_value(D,psi,j),
                           app*er+self.q*self.coefficient_value(Q,psi,j)])
            if j==0:jets[:,:,2]+=mu[:,None]
            out.append(jets)
        return out

    def point(self,s,psi):
        s=float(s);psi=float(psi);theta,rho,rhop,ts,tss,rhos=self.angular(s,psi)
        a,ap,app=[float(v[0])for v in self.flow.profile([s])]
        er=circle(theta);et=circle(theta,1);Y,D,Q=[self.sol.sol(s,j)for j in range(3)]
        X=a*er+self.q*self.coefficient_value(Y,[psi])[0];X[2]+=self.sol.mean_spline(s)[0]
        Xs=ap*er+a*ts*et+self.q*self.coefficient_value(D,[psi])[0];Xs[2]+=self.sol.mean_spline(s,1)[0]
        Xss=(app-a*ts*ts)*er+(2*ap*ts+a*tss)*et+self.q*self.coefficient_value(Q,[psi])[0];Xss[2]+=self.sol.mean_spline(s,2)[0]
        Xp=a*rho*et+self.q*self.coefficient_value(Y,[psi],1)[0]
        Xpp=a*(rhop*et-rho*rho*er)+self.q*self.coefficient_value(Y,[psi],2)[0]
        Xsp=-a*rho*ts*er+(ap*rho+a*rhos)*et+self.q*self.coefficient_value(D,[psi],1)[0]
        jets=[X,Xs,Xss,Xp,Xpp,Xsp]
        if s<=self.center_width:
            d=self.center_delta([psi]);w=[self.center_weights([s],j)for j in range(3)]
            for x,(i,j)in zip(jets,[(0,0),(1,0),(2,0),(0,1),(0,2),(1,1)]):x+=np.einsum('sj,juk->suk',w[i],d[j])[0,0]
        if self.end_lift is not None:
            for x,y in zip(jets,self.end_lift.correction([s],[psi])):x+=y[0,0]
        return tuple(jets)

class CartesianCutLift:
    """Match an entire two-jet from one target provider on a fixed end strip."""
    def __init__(self,prefix,target,width=.04):
        self.prefix,self.target,self.width=prefix,target,float(width)
        self.end=prefix.flow.end;self.cache={}
        if self.width<=0 or self.width+prefix.center_width>=self.end:raise ValueError('Overlapping or empty lifts')

    def delta(self,psi):
        old=self.prefix.raw_endpoint_angular_jets(psi);new=self.target.angular_jets(psi)
        return [n-o for n,o in zip(new,old)]

    def weights(self,s,order):
        s=np.atleast_1d(np.asarray(s,float));t=np.clip((self.end-s)/self.width,0,1)
        out=np.zeros((len(s),3));inside=s>=self.end-self.width
        # A right-end j-jet is a left-end t-jet multiplied by (-width)^j.
        for j in range(3):out[inside,j]=Polynomial(H[j]).deriv(order)(t[inside])*(-1)**(j+order)*self.width**(j-order)
        return out

    def correction(self,s,psi):
        d=self.delta(psi);w=[self.weights(s,j)for j in range(3)]
        return [np.einsum('sj,juk->suk',w[i],d[j])for i,j in [(0,0),(1,0),(2,0),(0,1),(0,2),(1,1)]]

class M3CartesianPrefix(M3SharedPrefix):
    """Finite Cartesian Fourier coefficients, each with a shared radial two-jet.

This also interpolates the background a*exp(i theta). Thus C2 regularity of
this finite map depends only on Hermite algebra, not on a numerical primitive
being exactly differentiated by separately evaluated source-profile jets.
"""
    def __init__(self,old,side_modes=32):
        super().__init__(old.obj,old.flow,old.sol,old.center_width)
        if side_modes<self.M:raise ValueError('Must contain every original mode')
        self.pm=1+3*np.arange(-side_modes,side_modes+1)
        self.hm=3*np.arange(self.M+1);self.P=len(self.pm);self.C=self.P+len(self.hm)
        s=old.sol.x.copy();extra=np.unique(np.r_[old.flow.breaks,old.flow.spline.x*old.flow.end,
                                               .75*old.flow.end,old.center_width])
        self.inserted_knots=0;self.near_existing_breaks=[]
        for x in extra:
            if x<0 or x>old.flow.end:continue
            distance=float(np.min(abs(s-x)))
            if distance<1e-10:
                if distance:self.near_existing_breaks.append([float(x),distance])
                continue
            s=np.sort(np.r_[s,x]);self.inserted_knots+=1
        x=s/old.flow.end;t=np.clip(4*x-3,0,1);fac=4/old.flow.end
        cut=1-t**3*(10+t*(-15+6*t));cp=-30*t*t*(1-t)**2*fac;cpp=-60*t*(1-t)*(1-2*t)*fac**2
        h=old.flow.spline(x);hp=old.flow.spline(x,1)/old.flow.end;hpp=old.flow.spline(x,2)/old.flow.end**2
        ee=[old.flow.warp_e*h*cut,old.flow.warp_e*(hp*cut+h*cp),old.flow.warp_e*(hpp*cut+2*hp*cp+h*cpp)]
        aa=old.flow.profile(s);b,bp,bpp=[-z/3 for z in ee]
        data=np.zeros((3,self.C,len(s)))
        for j,m in enumerate(self.pm):
            k=(int(m)-1)//3;J,J1,J2=jv(k,b),jvp(k,b,1),jvp(k,b,2)
            data[:,j]=np.stack([aa[0]*J,aa[1]*J+aa[0]*J1*bp,
                aa[2]*J+2*aa[1]*J1*bp+aa[0]*(J2*bp*bp+J1*bpp)])
        index={int(m):j for j,m in enumerate(self.pm)}
        Y=np.stack([old.sol.sol(s,j)for j in range(3)])*self.q
        data[:,index[1]]+=Y[:,0]
        for j,m in enumerate(self.modes):
            R,T=Y[:,1+j],Y[:,self.M+1+j]
            data[:,index[int(m)+1]]+=(R+T)/2
            data[:,index[1-int(m)]]+=(R-T)/2
            data[:,self.P+1+j]=Y[:,2*self.M+1+j]
        data[:,self.P]=np.stack([old.sol.mean_spline(s,j)[0]for j in range(3)])
        self.rep=SharedJetQuintic(s,data)

    def tensor_values(self,C,psi,order=0):
        psi=np.atleast_1d(np.asarray(psi,float));ep=np.exp(1j*psi[:,None]*self.pm)
        xy=np.einsum('ks,uk->su',C[:self.P],ep*(1j*self.pm)**order,optimize=True)
        phase=psi[:,None]*self.hm
        trig=np.cos(phase)if order==0 else(-np.sin(phase)if order==1 else-np.cos(phase))
        zh=trig*self.hm**order
        z=np.einsum('ks,uk->su',C[self.P:],zh,optimize=True)
        return np.stack([xy.real,xy.imag,z],axis=-1)

    def center_delta(self,psi):
        psi=np.atleast_1d(np.asarray(psi,float));theta=psi-self.E0*np.sin(3*psi)/3
        rho=1-self.E0*np.cos(3*psi);rhop=3*self.E0*np.sin(3*psi)
        b=-self.Epp*np.sin(3*psi)/3;bp=-self.Epp*np.cos(3*psi);bpp=3*self.Epp*np.sin(3*psi)
        cg=self.core.evaluate(theta);ng=self.core.normal_geometry(cg['phi'])
        f=self.core.frequencies;co=self.core.coefficients
        rhop_core=-np.sin(cg['phi'][:,None]*f)@(f*(1-f*f)*co)
        gt,gtt=cg['Ft'],cg['Ftt']
        gttt=-ng['et']/ng['rho'][:,None]**2+ng['er']*rhop_core[:,None]/ng['rho'][:,None]**3
        C=self.rep.jets[:,:,0];out=[]
        for j in range(3):
            before=self.tensor_values(C.T,psi,j);target=np.zeros_like(before)
            if j==0:target[0]=cg['F'];target[1,:,2]=1;target[2]=b[:,None]*gt
            elif j==1:target[0]=rho[:,None]*gt;target[2]=bp[:,None]*gt+(b*rho)[:,None]*gtt
            else:
                target[0]=rho[:,None]**2*gtt+rhop[:,None]*gt
                target[2]=bpp[:,None]*gt+(2*bp*rho+b*rhop)[:,None]*gtt+(b*rho*rho)[:,None]*gttt
            out.append(target-before)
        return out

    def raw_endpoint_angular_jets(self,psi):
        C=self.rep.jets[:,:,-1]
        return [self.tensor_values(C.T,psi,j)for j in range(3)]

    def evaluate(self,s,psi):
        s=np.atleast_1d(np.asarray(s,float));psi=np.atleast_1d(np.asarray(psi,float))
        C=[self.rep(s,j)for j in range(3)];pairs=[(0,0),(1,0),(2,0),(0,1),(0,2),(1,1)]
        jets=[self.tensor_values(C[i],psi,j)for i,j in pairs]
        if np.any(s<=self.center_width):
            d=self.center_delta(psi);w=[self.center_weights(s,j)for j in range(3)]
            for X,(i,j)in zip(jets,pairs):X+=np.einsum('sj,juk->suk',w[i],d[j])
        if self.end_lift is not None:
            for X,d in zip(jets,self.end_lift.correction(s,psi)):X+=d
        return jets

    def grid(self,s,N):
        psi=2*np.pi*np.arange(N)/N
        return (*self.evaluate(s,psi),self.flow.geo(np.atleast_1d(s),N))

    def point(self,s,psi):
        return tuple(x[0,0]for x in self.evaluate([s],[psi]))

class TailCutTarget:
    """One exact endpoint function, shared by both sides of the seam.

The perturbation's numerical outer anchor c can differ by one ulp from the
physical radius Rcut. A C2 near-cut reparametrization is used for V only;
the background and reference metric retain R itself. Its r-map has derivatives
1 and 0 at the endpoint, so the formulas below are exactly its endpoint jets.
"""
    def __init__(self,prefix,capped_tail):
        self.prefix,self.tail=prefix,capped_tail
        self.R=float(capped_tail.meta['parameters']['rCut'])
        self.w=float(capped_tail.meta['parameters']['wCut'])
        self.wr=-7*self.w/self.R
        self.ap=-1/math.sqrt(1+self.w*self.w)
        self.app=-self.w*self.wr/(1+self.w*self.w)**2
        self.zcut=float(prefix.sol.mean_spline(prefix.flow.end)[0])
        # Exact model: the same coefficient sum defines this constant and V.
        self.c=capped_tail.c
        f=capped_tail.finite
        self.A=(f.value_nodes[-1],f.first[-1],f.second[-1])
        self.mean=float(self.A[0][capped_tail.finite.P])

    def fourier(self,coeff,psi,order):
        psi=np.atleast_1d(np.asarray(psi,float));f=self.tail.finite
        xy=np.exp(1j*psi[:,None]*f.planar_modes)@((1j*f.planar_modes)**order*coeff[:f.P])
        mh=f.height_modes
        phase=psi[:,None]*mh
        trig=np.cos(phase)if order==0 else(-np.sin(phase)if order==1 else-np.cos(phase))
        z=(trig*mh**order)@coeff[f.P:]
        return np.asarray(np.stack([xy.real,xy.imag,z],axis=-1),float)

    def angular_jets(self,psi):
        psi=np.atleast_1d(np.asarray(psi,float));out=[];flip=np.array([1,1,-1.])
        for j in range(3):
            er=circle(psi,j)
            X=self.R*er+self.fourier(self.A[0],psi,j)*flip
            Xr=er+self.fourier(self.A[1],psi,j)*flip
            Xrr=self.fourier(self.A[2],psi,j)*flip
            if j==0:
                X[:,2]+=self.zcut+self.mean;Xr[:,2]-=self.w;Xrr[:,2]-=self.wr
            out.append(np.stack([X,self.ap*Xr,self.ap*self.ap*Xrr+self.app*Xr]))
        return out

    def perturbation_radius(self,R,width=.02):
        R=np.asarray(R,dtype=np.longdouble);c0=np.longdouble(self.R);delta=self.c-c0
        t=np.clip((R-(c0-width))/width,0,1)
        S=t**3*(10+t*(-15+6*t));Sp=30*t*t*(1-t)**2/width
        Spp=60*t*(1-t)*(1-2*t)/width**2
        r=R+delta*S
        r=np.where(R==c0,self.c,r)
        return r,1+delta*Sp,delta*Spp
