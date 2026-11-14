#!/usr/bin/env python3
"""Exact rectifying cores with reflection-preserving central Fourier freedom.

The formulas define an exact flat immersion whenever 1+x*w_t>0. Numerical
arc integration is spectrally resolved and separately reported. The optional
optimizer improves an interface to a linear cycle; it constructs no tail.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import json
import time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from construct_reflected_stable_interface import triangle_transfer,WIDTH_CONVENTION


def curve_geometry(phi,R=1.,radial=(0.,0.),height=(.1,0.,0.)):
    phi=np.asarray(phi); shape=phi.shape
    jets=[]
    radial_terms=[(0,R)]+[(4*(j+1),c) for j,c in enumerate(radial)]
    height_terms=[(4*j+2,c) for j,c in enumerate(height)]
    for d in range(5):
        xy=np.zeros(shape,dtype=complex); z=np.zeros(shape)
        for n,c in radial_terms:
            xy+=.5*c*((1j*(n+1))**d*np.exp(1j*(n+1)*phi)+
                       (1j*(1-n))**d*np.exp(1j*(1-n)*phi))
        for n,c in height_terms:
            z+=c*np.real((1j*n)**d*np.exp(1j*n*phi))
        jets.append(np.stack((xy.real,xy.imag,z),axis=-1))
    F,d1,d2,d3,d4=jets
    speed=np.linalg.norm(d1,axis=-1);cr=np.cross(d1,d2);cn=np.linalg.norm(cr,axis=-1)
    T=d1/speed[...,None];B=cr/cn[...,None];N=np.cross(B,T)
    kap=cn/speed**3;triple=np.sum(cr*d3,axis=-1)
    triple_prime=np.sum(d1*np.cross(d2,d4),axis=-1)
    speed_log_prime=np.sum(d1*d2,axis=-1)/speed**2
    cross_log_prime=np.sum(cr*np.cross(d1,d3),axis=-1)/cn**2
    w=triple*speed**3/cn**3
    wt=(triple_prime+3*triple*(speed_log_prime-cross_log_prime))*speed**2/cn**3
    D=B+w[...,None]*T
    return dict(gamma=F,d1=d1,d2=d2,speed=speed,T=T,N=N,B=B,kappa=kap,w=w,wt=wt,D=D)


def grid_port(R,radial,height,h,n=512):
    phi=2*np.pi*np.arange(n)/n;g=curve_geometry(phi,R,radial,height)
    a0=float(np.mean(g['speed']));coef=np.fft.fft(g['speed'])/n
    k=np.fft.fftfreq(n,d=1/n);integ=np.zeros(n,dtype=complex)
    nz=k!=0;integ[nz]=coef[nz]/(1j*k[nz])
    periodic=np.fft.ifft(integ*n).real
    t=a0*phi+periodic-periodic[0]
    theta=(t+h*g['w'])/a0;den=1+h*g['wt'];weight=g['speed']*den/a0
    F=g['gamma']+h*g['D'];er=np.c_[np.cos(theta),np.sin(theta),np.zeros(n)]
    et=np.c_[-np.sin(theta),np.cos(theta),np.zeros(n)]
    f=np.sum(F*er,axis=1)-a0;z=F[:,2]
    fc=float(2*np.mean(f*np.cos(2*theta)*weight))
    zc=float(2*np.mean(z*np.cos(2*theta)*weight))
    return dict(g=g,a0=a0,theta=theta,weight=weight,F=F,den=den,
                radial_projection=f,height=z,er=er,et=et,
                leading_radial=fc,leading_height=zc,
                central_PV=float(np.ptp(g['gamma'][:,2])),
                arc_fourier_tail=float(2*np.sum(abs(coef[(abs(k)>=n//4)]))))


class ReflectedCore:
    """Reusable analytic-curve port, with spectral arclength quadrature."""
    def __init__(self,R=1.,radial=(0.,0.),height=(.1,0.,0.),arc_nodes=4096):
        self.R=float(R);self.radial=tuple(radial);self.height=tuple(height)
        phi=2*np.pi*np.arange(arc_nodes)/arc_nodes
        speed=curve_geometry(phi,R,radial,height)['speed'];coef=np.fft.rfft(speed)/arc_nodes
        self.a0=float(coef[0].real)
        active=np.flatnonzero(abs(coef[1:-1])>2e-16)
        K=int(active[-1]+1) if len(active) else 0
        self.k=np.arange(1,K+1);self.arccoef=coef[1:K+1]/(1j*self.k)
        # arc uses the anchored primitive exp(i*k*phi)-1. Its complex
        # coefficient bound needs4 rather than2, plus the omitted Nyquist
        # term. This is a resolved-grid truncation diagnostic, not an analytic
        # bound for every unrepresented Fourier frequency of the exact speed.
        self.arc_integral_omitted_l1=float(4*np.sum(abs(coef[K+1:-1])/np.arange(K+1,len(coef)-1))
                                           +2*abs(coef[-1])/(len(coef)-1))
        self.speed_omitted_l1=float(2*np.sum(abs(coef[K+1:-1]))+abs(coef[-1]))
    def arc(self,phi):
        phi=np.asarray(phi);flat=phi.ravel();out=self.a0*flat
        if len(self.k):
            for j in range(0,len(flat),2048):
                e=np.exp(1j*flat[j:j+2048,None]*self.k[None,:])-1
                out[j:j+2048]+=2*np.real(e@self.arccoef)
        return out.reshape(phi.shape)
    def evaluate(self,x,theta):
        x,theta=np.broadcast_arrays(np.asarray(x,dtype=float),np.asarray(theta,dtype=float))
        y=self.a0*theta;phi=theta.copy()
        lo=np.floor(theta/(2*np.pi))*2*np.pi;hi=lo+2*np.pi
        for it in range(70):
            g=curve_geometry(phi,self.R,self.radial,self.height)
            res=self.arc(phi)+x*g['w']-y;den=1+x*g['wt']
            done=abs(res)<4e-15*max(1,self.a0)
            if np.all(done):break
            lo=np.where((res<0)&~done,phi,lo);hi=np.where((res>0)&~done,phi,hi)
            step=phi-res/(g['speed']*den)
            step=np.where((step<lo)|(step>hi)|~np.isfinite(step),(lo+hi)/2,step)
            phi=np.where(done,phi,step)
        g=curve_geometry(phi,self.R,self.radial,self.height);den=1+x*g['wt']
        scale=g['kappa']/den
        return dict(F=g['gamma']+x[...,None]*g['D'],Fx=g['B'],Ft=self.a0*g['T'],
                    Fxx=(scale*g['w']**2)[...,None]*g['N'],
                    Fxt=(-self.a0*scale*g['w'])[...,None]*g['N'],
                    Ftt=(self.a0*self.a0*scale)[...,None]*g['N'],
                    N=g['N'],den=den,phi=phi,a0=self.a0,
                    residual=self.arc(phi)+x*g['w']-y)


class InterfaceSearch:
    def __init__(self,delta=.6,speed=.8,ratio=.05,n=512,min_den=.12,max_kW=90.,
                 rho=None,length_over_a0=None):
        self.delta=delta;self.speed=speed;self.ratio=ratio;self.n=n
        self.min_den=min_den;self.max_kW=max_kW
        self.transfer=triangle_transfer(delta,speed)
        if rho is not None:
            if rho>=0 or length_over_a0 is None or length_over_a0<=0:
                raise ValueError('External interface needs rho<0 and length_over_a0>0')
            self.transfer=dict(hyperbolic=True,stable_height_over_radial=rho,
                               linear_halfwidth=-1/(4*rho),cycle_length=length_over_a0)
        if not self.transfer['hyperbolic']:raise ValueError('Need a negative stable eigenvalue')
        self.rho=self.transfer['stable_height_over_radial'];self.cache_p=None;self.cache_data=None
    def geometry(self,p,n=None):
        if n is None and self.cache_p is not None and np.array_equal(p,self.cache_p):return self.cache_data
        A,h,r4,r8,z6,z10,kk=p
        d=grid_port(1.,(r4,r8),(A,z6,z10),h,self.n if n is None else n)
        g=d['g'];a0=d['a0'];L=self.transfer['cycle_length']*a0;W=2*(h+L)
        kport=g['kappa']/d['den'];denmin=1-h*abs(g['wt'])
        ksurf=g['kappa']*(1+g['w']**2)/denmin
        gammah=g['gamma'][:,:2];Dh=g['D'][:,:2];d1h=g['d1'][:,:2]
        cross=lambda u,v:u[:,0]*v[:,1]-u[:,1]*v[:,0]
        support=cross(gammah,d1h)-h*abs(cross(Dh,d1h))
        normal=-np.sum(g['N'][:,:2]*gammah,axis=1)-h*abs(np.sum(g['N'][:,:2]*Dh,axis=1))
        d.update(W=W,prefix_length=L,kport=kport,denmin=denmin,ksurf=ksurf,
                 projection_turn_margin=support,normal_horizontal_margin=normal)
        if n is None:self.cache_p=np.array(p);self.cache_data=d
        return d
    def eq(self,p,n=None):
        d=self.geometry(p,n)
        return np.array([(d['leading_height']-self.rho*d['leading_radial'])/p[0],
                         (d['central_PV']/d['W']-self.ratio)/self.ratio])
    def inequality(self,p,n=None):
        d=self.geometry(p,n)
        return np.r_[d['a0']*d['kport']-p[-1],d['denmin']-self.min_den,
                     (self.max_kW-d['W']*d['ksurf'])/self.max_kW,
                     d['projection_turn_margin']-.02,d['normal_horizontal_margin']-.02]
    def summarize(self,p,n=8192):
        d=self.geometry(p,n);g=d['g'];modes=[]
        for k in (2,4,6,8,10,12):
            modes.append(dict(mode=k,
                radial_cos=float(2*np.mean(d['radial_projection']*np.cos(k*d['theta'])*d['weight'])),
                height_cos=float(2*np.mean(d['height']*np.cos(k*d['theta'])*d['weight']))))
        return dict(R=1.,radial=[float(p[2]),float(p[3])],height=[float(p[0]),float(p[4]),float(p[5])],
            halfwidth=float(p[1]),a0=d['a0'],planned_total_width=d['W'],prefix_length=d['prefix_length'],
            planned_Lband=d['W'],prefix_radial_excursion=self.delta*d['a0'],width_convention=WIDTH_CONVENTION,
            central_PV=d['central_PV'],central_PV_over_budget=float(d['central_PV']/d['W']),
            stable_height_over_radial=self.rho,
            stable_line_relative_defect=float((d['leading_height']-self.rho*d['leading_radial'])/p[0]),
            sampled_port_a0_kappa_min=float(d['a0']*np.min(d['kport'])),
            instantaneous_target_slope_root_min=float(1-(self.speed/(d['a0']*np.min(d['kport'])))**2),
            sampled_denominator_min=float(np.min(d['denmin'])),
            sampled_core_kappaW_max=float(d['W']*np.max(d['ksurf'])),
            sampled_projection_turn_margin=float(np.min(d['projection_turn_margin'])),
            sampled_normal_horizontal_margin=float(np.min(d['normal_horizontal_margin'])),
            arc_speed_Fourier_tail=d['arc_fourier_tail'],leading_modes=modes)


def audit_port(params):
    core=ReflectedCore(params['R'],params['radial'],params['height'])
    h=params['halfwidth'];records=[]
    for n in (32,64,128,256,512,1024):
        theta=2*np.pi*np.arange(n)/n;dt=2*np.pi/n;dx=.2/n
        x=np.array([-.7*h,0.,.7*h])[:,None]
        F=lambda xx,tt:core.evaluate(xx,tt)['F']
        Fx=(-F(x+2*dx,theta)+8*F(x+dx,theta)-8*F(x-dx,theta)+F(x-2*dx,theta))/(12*dx)
        Ft=(-F(x,theta+2*dt)+8*F(x,theta+dt)-8*F(x,theta-dt)+F(x,theta-2*dt))/(12*dt)
        records.append(dict(Ntheta=n,E_error=float(np.max(abs(np.sum(Fx*Fx,axis=-1)-1))),
            F_relative=float(np.max(abs(np.sum(Fx*Ft,axis=-1)/core.a0))),
            G_relative=float(np.max(abs(np.sum(Ft*Ft,axis=-1)/core.a0**2-1)))))
    theta=2*np.pi*np.arange(1024)/1024
    e=core.evaluate(h,theta);left=core.evaluate(-h,theta)['F']
    right=core.evaluate(h,theta+np.pi/2)['F'].copy()
    right=right[:,[1,0,2]]*np.array([1.,-1.,-1.])
    return dict(a0=core.a0,arc_omitted_l1=core.arc_integral_omitted_l1,
                speed_omitted_l1=core.speed_omitted_l1,
                implicit_residual=float(np.max(abs(e['residual']))),
                reflection_error=float(np.max(abs(left-right))),
                formula_metric_max_error=float(max(np.max(abs(np.sum(e['Fx']**2,axis=-1)-1)),
                    np.max(abs(np.sum(e['Fx']*e['Ft'],axis=-1)/core.a0)),
                    np.max(abs(np.sum(e['Ft']**2,axis=-1)/core.a0**2-1)))),
                same_geometry_fourth_order_audit=records)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',required=True)
    ap.add_argument('--delta',type=float,default=.6);ap.add_argument('--speed',type=float,default=.8)
    ap.add_argument('--ratio',type=float,default=.05);ap.add_argument('--nodes',type=int,default=512)
    ap.add_argument('--rho',type=float);ap.add_argument('--prefix-length-over-a0',type=float)
    ap.add_argument('--iterations',type=int,default=200);ap.add_argument('--restart');args=ap.parse_args()
    s=InterfaceSearch(args.delta,args.speed,args.ratio,args.nodes,
                      rho=args.rho,length_over_a0=args.prefix_length_over_a0)
    if args.restart:
        old=json.loads(Path(args.restart).read_text());p=np.array(old['parameters'])
    else:
        h=s.transfer['linear_halfwidth'];A=args.ratio*(h+s.transfer['cycle_length'])
        p=np.array([A,h,0.,0.,0.,0.,.5])
        p[-1]=s.geometry(p)['a0']*np.min(s.geometry(p)['kport'])-.002
    initial=s.summarize(p);tic=time.time()
    bounds=[(.015,.5),(.03,1.4),(-.12,.12),(-.05,.05),(-.04,.04),(-.015,.015),(.05,1.8)]
    sol=minimize(lambda p:-p[-1],p,method='SLSQP',bounds=bounds,
       constraints=[dict(type='eq',fun=s.eq),dict(type='ineq',fun=s.inequality)],
       options=dict(maxiter=args.iterations,ftol=2e-11,disp=False))
    final=s.summarize(sol.x)
    out=dict(author='constructive_geometry; GPT-6 Astra Pro; AI-assisted',scope=__doc__,settings=vars(args),
         width_convention=WIDTH_CONVENTION,
         status='EXACT CORE INTERFACE OPTIMIZATION ONLY; no smooth prefix/collar/caps',
         optimizer=dict(success=bool(sol.success),message=sol.message,iterations=int(sol.nit),
                        seconds=time.time()-tic),parameters=sol.x.tolist(),initial=initial,final=final,
         training_constraint_audit=dict(eq=s.eq(sol.x).tolist(),minimum_inequality=float(np.min(s.inequality(sol.x)))),
         dense_constraint_audit=dict(eq=s.eq(sol.x,8192).tolist(),minimum_inequality=float(np.min(s.inequality(sol.x,8192)))),
         exact_core_port_audit=audit_port(final))
    Path(args.out).write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('initial','scope','parameters')},indent=2),flush=True)


if __name__=='__main__':main()
