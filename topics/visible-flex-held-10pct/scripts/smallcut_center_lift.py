#!/usr/bin/env python3
"""Exact analytic-core C2 center lift of a shared-jet open prefix.

A width-fixed quintic Hermite lift corrects the Cartesian inlet position and
physical-radial two-jet. In the computational angle psi the required second
jet is theta_ss * gamma_theta, not zero. The actual endpoint analytic core is
used before any Fourier projection. All angular derivatives of the lift are
computed analytically. The metric g=ds^2+a(s)^2 dtheta^2 is unchanged.
Neither this center repair nor the finite linear outer port closes the tail.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse,hashlib,json,math,time
from pathlib import Path
import numpy as np
from numpy.polynomial import Polynomial
from scipy.optimize import minimize
from smallcut_c2_representative import load_model,build_mean

H=np.array([[1,0,0,-10,15,-6],[0,1,0,-6,8,-3],[0,0,.5,-1.5,1.5,-.5]],float)

class CenterLift:
    def __init__(self,obj,flow,sol,width=.04):
        self.obj=obj;self.flow=flow;self.sol=sol;self.width=float(width);self.q=obj.q;self.M=obj.M
        self.core=obj._core;self.modes=2*np.arange(1,self.M+1);self.cache={}
        self.E0=float(flow.warp_e*flow.spline(0.))
        self.Epp=float(flow.warp_e*flow.spline(0.,2)/flow.end**2)
        if abs(float(flow.spline(0.,1)))>1e-14:raise ValueError('This lift requires theta_s=0 at the inlet.')
        a,ap,app=flow.profile(np.array([0.]))
        if max(abs(float(a[0])-1),abs(float(ap[0])),abs(float(app[0])))>1e-14:
            raise ValueError('Expected the documented inlet a=1,a_s=a_ss=0.')
        if not 0<self.width<flow.end:raise ValueError('Invalid center lift width.')
    def value_at(self,c,psi,order=0):
        psi=np.atleast_1d(np.asarray(psi,float));m=self.modes
        co=np.cos(psi[:,None]*m);si=np.sin(psi[:,None]*m)
        r=c[0]+co@c[1:self.M+1];t=si@c[self.M+1:2*self.M+1];z=co@c[2*self.M+1:]
        if order>=1:
            rp=-si@(m*c[1:self.M+1]);tp=co@(m*c[self.M+1:2*self.M+1]);zp=-si@(m*c[2*self.M+1:])
        if order==1:r,t,z=rp-t,r+tp,zp
        elif order==2:
            rpp=-co@(m*m*c[1:self.M+1]);tpp=-si@(m*m*c[self.M+1:2*self.M+1]);zpp=-co@(m*m*c[2*self.M+1:])
            r,t,z=rpp-r-2*tp,tpp-t+2*rp,zpp
        return np.stack((r*np.cos(psi)-t*np.sin(psi),r*np.sin(psi)+t*np.cos(psi),z),axis=-1)
    def delta(self,psi):
        psi=np.atleast_1d(np.asarray(psi,float));theta=psi-self.E0*np.sin(2*psi)/2
        rho=1-self.E0*np.cos(2*psi);rhop=2*self.E0*np.sin(2*psi)
        b=-self.Epp*np.sin(2*psi)/2;bp=-self.Epp*np.cos(2*psi);bpp=2*self.Epp*np.sin(2*psi)
        cg=self.core.evaluate(theta);ng=self.core.normal_geometry(cg['phi']);phi=cg['phi'];rc=ng['rho']
        rhop_core=-np.sin(phi[:,None]*self.core.frequencies)@(self.core.frequencies*(1-self.core.frequencies**2)*self.core.coefficients)
        gt=cg['Ft'];gtt=cg['Ftt'];gttt=-ng['et']/rc[:,None]**2+ng['er']*rhop_core[:,None]/rc[:,None]**3
        er=np.stack((np.cos(theta),np.sin(theta),np.zeros_like(theta)),axis=-1)
        et=np.stack((-np.sin(theta),np.cos(theta),np.zeros_like(theta)),axis=-1)
        Y,D,Q=self.sol.sol.jets[:,:,0];mu=self.sol.mean_spline.jets[:,0,0]
        ds=[]
        for order in range(3):
            if order==0:
                d0=cg['F']-er-self.q*self.value_at(Y,psi,0);d0[:,2]-=mu[0]
                d1=-self.q*self.value_at(D,psi,0);d1[:,2]+=1-mu[1]
                d2=b[:,None]*(gt-et)-self.q*self.value_at(Q,psi,0);d2[:,2]-=mu[2]
            elif order==1:
                d0=rho[:,None]*(gt-et)-self.q*self.value_at(Y,psi,1)
                d1=-self.q*self.value_at(D,psi,1)
                d2=bp[:,None]*(gt-et)+(b*rho)[:,None]*(gtt+er)-self.q*self.value_at(Q,psi,1)
            else:
                d0=rho[:,None]**2*(gtt+er)+rhop[:,None]*(gt-et)-self.q*self.value_at(Y,psi,2)
                d1=-self.q*self.value_at(D,psi,2)
                d2=bpp[:,None]*(gt-et)+(2*bp*rho+b*rhop)[:,None]*(gtt+er)+(b*rho*rho)[:,None]*(gttt+et)-self.q*self.value_at(Q,psi,2)
            ds.append(np.stack((d0,d1,d2)))
        return ds
    def weights(self,s,derivative=0):
        s=np.atleast_1d(np.asarray(s,float));t=np.clip(s/self.width,0,1)
        out=np.zeros((len(s),3));inside=s<=self.width
        for j in range(3):
            out[inside,j]=Polynomial(H[j]).deriv(derivative)(t[inside])*self.width**(j-derivative)
        return out
    def correction(self,s,psi):
        ds=self.delta(psi);weights=[self.weights(s,k) for k in range(3)]
        pair=[(0,0),(1,0),(2,0),(0,1),(0,2),(1,1)]
        return [np.einsum('sj,juk->suk',weights[i],ds[j]) for i,j in pair]
    def grid(self,s,N):
        s=np.atleast_1d(np.asarray(s,float));B,B1,B2=self.flow.basis(N);Y,Yp,Ypp=[self.sol.sol(s,k) for k in range(3)]
        g=self.flow.geo(s,N)
        X=g['pos']+self.q*self.flow.values(Y,B);X[:,:,2]+=self.sol.mean_spline(s)[0,:,None]
        Xs=g['s1']+self.q*self.flow.values(Yp,B);Xs[:,:,2]+=self.sol.mean_spline(s,1)[0,:,None]
        Xss=g['s2']+self.q*self.flow.values(Ypp,B);Xss[:,:,2]+=self.sol.mean_spline(s,2)[0,:,None]
        Xp=g['p1']+self.q*self.flow.values(Y,B1);Xpp=g['p2']+self.q*self.flow.values(Y,B2);Xsp=g['sp']+self.q*self.flow.values(Yp,B1)
        if np.any(s<=self.width):
            if N not in self.cache:self.cache[N]=self.delta(2*np.pi*np.arange(N)/N)
            ds=self.cache[N];ww=[self.weights(s,k) for k in range(3)]
            for a,(i,j) in zip([X,Xs,Xss,Xp,Xpp,Xsp],[(0,0),(1,0),(2,0),(0,1),(0,2),(1,1)]):
                a+=np.einsum('sj,juk->suk',ww[i],ds[j])
        return X,Xs,Xss,Xp,Xpp,Xsp,g
    def angular(self,s,psi):
        x=s/self.flow.end;t=np.clip((x-.75)/.25,0,1);fac=1/(.25*self.flow.end)
        cut=1-t**3*(10-15*t+6*t*t);cp=-30*t*t*(1-t)**2*fac;cpp=-60*t*(1-t)*(1-2*t)*fac*fac
        f=self.flow.spline;h=f(x);hp=f(x,1)/self.flow.end;hpp=f(x,2)/self.flow.end**2
        e=self.flow.warp_e*h*cut;ep=self.flow.warp_e*(hp*cut+h*cp);epp=self.flow.warp_e*(hpp*cut+2*hp*cp+h*cpp)
        sn=np.sin(2*psi);co=np.cos(2*psi)
        return psi-e*sn/2,1-e*co,2*e*sn,-ep*sn/2,-epp*sn/2,-ep*co
    def point(self,s,psi):
        s=float(s);psi=float(psi%(2*np.pi));theta,rho,rhop,ts,tss,rhos=self.angular(s,psi)
        a,ap,app=[float(v[0]) for v in self.flow.profile(np.array([s]))]
        er=np.array([np.cos(theta),np.sin(theta),0.]);et=np.array([-np.sin(theta),np.cos(theta),0.])
        Y,Yp,Ypp=[self.sol.sol(s,k) for k in range(3)]
        X=a*er+self.q*self.value_at(Y,[psi])[0];X[2]+=self.sol.mean_spline(s)[0]
        Xs=ap*er+a*ts*et+self.q*self.value_at(Yp,[psi])[0];Xs[2]+=self.sol.mean_spline(s,1)[0]
        Xss=(app-a*ts*ts)*er+(2*ap*ts+a*tss)*et+self.q*self.value_at(Ypp,[psi])[0];Xss[2]+=self.sol.mean_spline(s,2)[0]
        Xp=a*rho*et+self.q*self.value_at(Y,[psi],1)[0]
        Xpp=a*(rhop*et-rho*rho*er)+self.q*self.value_at(Y,[psi],2)[0]
        Xsp=-a*rho*ts*er+(ap*rho+a*rhos)*et+self.q*self.value_at(Yp,[psi],1)[0]
        if s<=self.width:
            for arr,add in zip([X,Xs,Xss,Xp,Xpp,Xsp],self.correction([s],[psi])):arr+=add[0,0]
        return X,Xs,Xss,Xp,Xpp,Xsp


def coefficient_norms(c,M):
    m=2*np.arange(1,M+1);r=abs(c[0]);R=abs(c[1:M+1]);T=abs(c[M+1:2*M+1]);Z=abs(c[2*M+1:])
    return np.array([r+np.sum(R+T+Z),r+np.sum((m+1)*(R+T)+m*Z),r+np.sum((m+1)**2*(R+T)+m*m*Z)])

def mesh_cover_bounds(model,N,ss):
    flow=model.flow;sol=model.sol;q=model.q;M=model.M
    hn=np.diff(sol.x);c=np.asarray(sol.sol._normalized,float)
    cb=np.sum(abs(c),axis=0).T;cp=np.sum(abs(c[1:])*np.arange(1,6)[:,None,None],axis=0).T/hn[:,None]
    cm=np.asarray(sol.mean_spline._normalized,float)
    mean1=float(np.max(np.sum(abs(cm[1:])*np.arange(1,6)[:,None,None],axis=0)[0]/hn))
    eb=0.;esb=0.
    for k,(lo,hi) in enumerate(zip(flow.spline.x[:-1],flow.spline.x[1:])):
        hp=Polynomial(flow.spline.c[:,k][::-1]);u=Polynomial([4*(lo-.75),4.])
        cut=Polynomial([1.]) if hi<=.75+1e-15 else Polynomial([1.])-10*u**3+15*u**4-6*u**5
        e=flow.warp_e*hp*cut;d=hi-lo;ed=e.deriv()/flow.end
        eb=max(eb,float(np.sum(abs(e.coef)*d**np.arange(len(e.coef)))))
        esb=max(esb,float(np.sum(abs(ed.coef)*d**np.arange(len(ed.coef)))))
    amax=1+float(model.obj.cfg['delta']);m=2*np.arange(1,M+1)
    ub=amax*(1+eb)+q*float(np.max(cb[:,0]+np.sum((m+1)*(cb[:,1:M+1]+cb[:,M+1:2*M+1])+m*cb[:,2*M+1:],axis=1)))
    sb=1+amax*esb/2+q*float(np.max(np.sum(cp,axis=1)))+mean1
    # Uniform bounds for the analytic non-polynomial inlet correction from
    # a sampled value plus an explicit whole-circle derivative bound.
    psi=2*np.pi*np.arange(N)/N;delta=model.delta(psi)
    dmax=np.array([[np.linalg.norm(v,axis=1).max() for v in row] for row in delta])
    Y,D,Q=sol.sol.jets[:,:,0];normY=coefficient_norms(Y,M);normD=coefficient_norms(D,M);normQ=coefficient_norms(Q,M)
    rhomax=1+abs(model.E0);rhopmax=2*abs(model.E0);kmax=model.core.curvature_upper_bound
    d0prime_bound=2*rhomax+q*normY[1]
    d0second_bound=(kmax+1)*rhomax*rhomax+2*rhopmax+q*normY[2]
    d2prime_bound=2*abs(model.Epp)+abs(model.Epp)/2*(kmax+1)*rhomax+q*normQ[1]
    dsup=np.array([dmax[0,0]+np.pi/N*d0prime_bound,
         q*normD[0]+abs(1-sol.mean_spline.jets[1,0,0]),
         dmax[0,2]+np.pi/N*d2prime_bound])
    dusup=np.array([dmax[1,0]+np.pi/N*d0second_bound,q*normD[1],d2prime_bound])
    w=model.width
    s_lift=float(np.dot([15/(8*w),1,2*w/9],dsup))
    u_lift=float(np.dot([1,16*w/81,54*w*w/3125],dusup))
    sb+=s_lift;ub+=u_lift
    # Explicit finite map: no continuous Frenet-root assumption is used here.
    # A tiny numerical evaluation budget is displayed, not claimed as an
    # interval-arithmetic proof. All derivative bounds are triangle bounds.
    rounding_budget=1e-10
    pad=sb*np.max(np.diff(ss))/2+ub*np.pi/N+rounding_budget
    return dict(s_bound=sb,psi_bound=ub,mean_slope_bound=mean1,angular_e_bound=eb,angular_es_bound=esb,
        lift_sampled_delta_norms=dmax.tolist(),lift_delta_uniform_bounds=dsup.tolist(),lift_delta_psi_uniform_bounds=dusup.tolist(),
        lift_s_derivative_bound=s_lift,lift_psi_derivative_bound=u_lift,position_padding=pad,numerical_evaluation_budget=rounding_budget,
        scope='Analytic derivative/mesh-cover inequalities for the explicit finite C2 map. Floating bounds and sampling evaluations use the displayed numerical budget; no directed-rounding or continuous isometry certificate is asserted.')

def audit(model,N=1536,radial=2049):
    flow=model.flow;sol=model.sol
    ss=np.unique(np.r_[np.linspace(0,flow.end,radial),sol.x,(sol.x[:-1]+sol.x[1:])/2,flow.breaks,np.linspace(0,model.width,401)])
    psi=2*np.pi*np.arange(N)/N;ext={};lo=np.full(3,np.inf);hi=-lo;out=dict(metric_l1=0.,kappa_sample=0.,root_min=1.,area_element_min=np.inf)
    p0=model.core.evaluate(np.array([0.]))['F'][0]
    def upd(name,arr,first,maximum=False):
        ij=np.unravel_index((np.argmax if maximum else np.argmin)(arr),arr.shape);v=float(arr[ij])
        if name not in ext or (v>ext[name]['value'] if maximum else v<ext[name]['value']):ext[name]=dict(value=v,s=float(ss[first+ij[0]]),psi=float(psi[ij[1]]))
    for first in range(0,len(ss),24):
        s=ss[first:first+24];X,Xs,Xss,Xp,Xpp,Xsp,g=model.grid(s,N);a,ap,app=flow.profile(s);rho=g['rho'];v=g['v']
        Fs=Xs-v[:,:,None]*Xp;Ft=Xp/rho[:,:,None]
        Ftt=Xpp/rho[:,:,None]**2-Xp*g['rhop'][:,:,None]/rho[:,:,None]**3
        Fst=(Xsp-g['vp'][:,:,None]*Xp-v[:,:,None]*Xpp)/rho[:,:,None]
        Fss=Xss-2*v[:,:,None]*Xsp+v[:,:,None]**2*Xpp+(v*g['vp']-g['vs'])[:,:,None]*Xp
        E=np.sum(Fs*Fs,axis=2);F=np.sum(Fs*Ft,axis=2);G=np.sum(Ft*Ft,axis=2)
        errors=np.stack((E-1,F/a[:,None],G/a[:,None]**2-1),axis=2)
        out['metric_l1']=max(out['metric_l1'],float(np.max(np.sum(abs(np.fft.fft(errors,axis=1)/N),axis=1))))
        cross=np.cross(Xp,Xs);area=np.linalg.norm(cross,axis=2);nn=cross/area[:,:,None]
        L=np.sum(Fss*nn,axis=2);M=np.sum(Fst*nn,axis=2);NN=np.sum(Ftt*nn,axis=2);detI=E*G-F*F
        trace=(L*G-2*M*F+NN*E)/detI;detII=(L*NN-M*M)/detI
        kap=(abs(trace)+np.sqrt(np.maximum(0,trace*trace-4*detII)))/2
        out['kappa_sample']=max(out['kappa_sample'],float(kap.max()));out['area_element_min']=min(out['area_element_min'],float(area.min()))
        lam=np.linalg.norm(Xp,axis=2);T=Xp/lam[:,:,None];curveN=Xpp-np.sum(Xpp*T,axis=2)[:,:,None]*T;ck=np.linalg.norm(curveN,axis=2)/lam**2
        out['root_min']=min(out['root_min'],float(np.min(1-(ap[:,None]/(a[:,None]*ck))**2)))
        support=np.sum(X*nn,axis=2);R=np.linalg.norm(X,axis=2);xy=np.linalg.norm(X[:,:,:2],axis=2)
        theta_u=(X[:,:,0]*Xp[:,:,1]-X[:,:,1]*Xp[:,:,0])/xy**2
        theta_s=(X[:,:,0]*Xs[:,:,1]-X[:,:,1]*Xs[:,:,0])/xy**2
        zgraph=Xs[:,:,2]-Xp[:,:,2]*theta_s/theta_u
        rot=np.stack((-X[:,:,1],X[:,:,0],X[:,:,2]),axis=-1);dist=np.linalg.norm(rot-p0,axis=2)
        for name,arr in [('surface_support',support),('core_witness_distance',dist),('theta_psi_min',theta_u),('z_s_at_fixed_azimuth_min',zgraph),('radius_xy_min',xy)]:upd(name,arr,first)
        for name,arr in [('radius_3d_max',R),('height_max',X[:,:,2]),('radius_xy_max',xy)]:upd(name,arr,first,True)
        lo=np.minimum(lo,X.min(axis=(0,1)));hi=np.maximum(hi,X.max(axis=(0,1)))
        if first==0:
            cg=model.core.evaluate(g['theta'][0]);ez=np.zeros_like(Fs[0]);ez[:,2]=1
            out['center_physical_jet_max_errors']=dict(position=float(np.linalg.norm(X[0]-cg['F'],axis=1).max()),Fs=float(np.linalg.norm(Fs[0]-ez,axis=1).max()),Fss=float(np.linalg.norm(Fss[0],axis=1).max()),Ft=float(np.linalg.norm(Ft[0]-cg['Ft'],axis=1).max()),Fst=float(np.linalg.norm(Fst[0],axis=1).max()),Ftt=float(np.linalg.norm(Ftt[0]-cg['Ftt'],axis=1).max()))
    refinements={}
    for name in ['surface_support','radius_3d_max','core_witness_distance']:
        start=ext[name]
        def fun(t):
            X,Xs,_,Xu,_,_=model.point(t[0],t[1])
            if name=='surface_support':
                n=np.cross(Xu,Xs);return float(np.dot(X,n)/np.linalg.norm(n))
            if name=='radius_3d_max':return -float(np.dot(X,X))
            z=np.array([-X[1],X[0],X[2]])-p0;return float(np.dot(z,z))
        z=minimize(fun,[start['s'],start['psi']],method='Nelder-Mead',bounds=[(0.,flow.end),(start['psi']-.1,start['psi']+.1)],options=dict(xatol=1e-12,fatol=1e-14,maxiter=500))
        value=float(z.fun)
        if name=='radius_3d_max':value=math.sqrt(-value)
        elif name=='core_witness_distance':value=math.sqrt(value)
        refinements[name]=dict(value=value,s=float(z.x[0]),psi=float(z.x[1]%(2*np.pi)),success=bool(z.success),scope='Local refinement initialized at dense-grid extremum; not a global certificate.')
    cover=mesh_cover_bounds(model,N,ss);pad=cover['position_padding'];Dupper=2*(ext['radius_3d_max']['value']+pad);wlower=max(0.,ext['core_witness_distance']['value']-pad)
    out.update(radial_samples=len(ss),angular_samples=N,sampled_extrema=ext,local_refinements=refinements,bbox_upper=dict(min=lo.tolist(),max=hi.tolist()),bbox_both_reflections=dict(min=[float(lo[0]),float(lo[1]),-float(hi[2])],max=hi.tolist()),mesh_cover=cover,
        diameter=dict(sampled=2*ext['radius_3d_max']['value'],local_estimate=2*refinements['radius_3d_max']['value'],mesh_cover_upper_estimate=Dupper,reason='Half-turn XY symmetry and z reflection imply central symmetry, hence D=2 max norm for the reflected OPEN prefix. No tail included.'),
        witness=dict(point=p0.tolist(),sampled_distance=ext['core_witness_distance']['value'],local_estimate=refinements['core_witness_distance']['value'],mesh_cover_lower_estimate=wlower,mesh_cover_ratio=wlower/Dupper,closing_requirements=dict(tail_distance_from_witness_at_least=wlower,complete_diameter_at_most=10*wlower),scope='The z=0 witness has equal distance to the upper and reflected lower prefixes. Any future closing tail must separately remain outside its witness ball.'))
    return out

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--recovery',type=Path,required=True);p.add_argument('--checkpoint',type=Path,required=True);p.add_argument('--port',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--width',type=float,default=.04);p.add_argument('--angular',type=int,default=1536);p.add_argument('--radial',type=int,default=2049)
    a=p.parse_args();start=time.time();r,obj,flow,sol,old,ad=load_model(a.recovery,a.checkpoint,a.port,a.angular);sol.mean_spline=build_mean(flow,sol,a.angular,8);model=CenterLift(obj,flow,sol,a.width)
    result=audit(model,a.angular,a.radial)
    result.update(scope=__doc__,checkpoint_sha256=hashlib.sha256(a.checkpoint.read_bytes()).hexdigest(),script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),shared_jet_script_sha256=hashlib.sha256(Path(__file__).with_name('smallcut_c2_representative.py').read_bytes()).hexdigest(),actual_q=r['actual_primary_amplitude'],frozen_profile=r['frozen_profile'],lift_width=a.width,mean_angular=a.angular,mean_gauss_order=8,seconds=time.time()-start)
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(event='center_lift_audit',metric_l1=result['metric_l1'],kappa=result['kappa_sample'],center=result['center_physical_jet_max_errors'],support=result['sampled_extrema']['surface_support']['value'],D=result['diameter'],witness=result['witness'],seconds=result['seconds'])),flush=True)
if __name__=='__main__':main()
