#!/usr/bin/env python3
"""Exact embedded flat annular core with nonplanar material circles.

This is a LOCAL block only: no rotational collars, caps, or global flex.
The proof and conservative analytic bounds are in the matching note.
Run:
  python scripts/construct_rectifying_wavy_core.py --out notes/construct_rectifying_wavy_core.json
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import numpy as np
from scipy.special import ellipe, ellipeinc


def geometry(phi, R=.5, A=.1, m=2):
    phi = np.asarray(phi)
    c, s = np.cos(phi), np.sin(phi)
    cm, sm = np.cos(m*phi), np.sin(m*phi)
    gamma = np.stack((R*c, R*s, A*cm), axis=-1)
    d1 = np.stack((-R*s, R*c, -m*A*sm), axis=-1)
    d2 = np.stack((-R*c, -R*s, -m*m*A*cm), axis=-1)
    d3 = np.stack((R*s, -R*c, m**3*A*sm), axis=-1)
    v = np.linalg.norm(d1, axis=-1)
    cr = np.cross(d1,d2)
    crnorm = np.linalg.norm(cr, axis=-1)
    T = d1/v[...,None]
    B = cr/crnorm[...,None]
    N = np.cross(B,T)
    kappa = crnorm/v**3
    tau = np.sum(cr*d3,axis=-1)/crnorm**2
    w = tau/kappa
    bv = R*R+m*m*A*A*sm*sm
    cv = R*R+m*m*A*A*(sm*sm+m*m*cm*cm)
    wc = A*m*(m*m-1)/R
    wt = (wc*m*cm*(bv/cv)**1.5*
          (1+3*m*m*A*A*sm*sm*(1/bv+(m*m-1)/cv)))/v
    t = R/m*ellipeinc(m*phi,-(m*A/R)**2)
    return dict(gamma=gamma,T=T,N=N,B=B,kappa=kappa,tau=tau,w=w,
                wt=wt,v=v,t=t)


def evaluate(x,theta,R=.5,A=.1,m=2):
    x,theta=np.broadcast_arrays(x,theta)
    a0=2*R*ellipe(-(m*A/R)**2)/np.pi
    y=a0*theta
    phi=theta.copy()
    for _ in range(30):
        g=geometry(phi,R,A,m)
        residual=g['t']+x*g['w']-y
        step=residual/(g['v']*(1+x*g['wt']))
        phi=phi-step
        if np.max(np.abs(step)) < 2e-15:
            break
    g=geometry(phi,R,A,m)
    den=1+x*g['wt']
    D=g['B']+g['w'][...,None]*g['T']
    F=g['gamma']+x[...,None]*D
    Fx=g['B']
    Ft=a0*g['T']
    z=g['kappa']/den
    Fxx=(z*g['w']**2)[...,None]*g['N']
    Fxt=(-a0*z*g['w'])[...,None]*g['N']
    Ftt=(a0*a0*z)[...,None]*g['N']
    return dict(F=F,Fx=Fx,Ft=Ft,Fxx=Fxx,Fxt=Fxt,Ftt=Ftt,
                a0=a0,phi=phi,den=den,kappa=z*(1+g['w']**2),
                residual=g['t']+x*g['w']-y,**{k:g[k] for k in ('w','wt','N')})


def normmax(x):
    return float(np.max(np.abs(x)))


def metric_summary(Fx,Ft,a0):
    return dict(E_error=normmax(np.sum(Fx*Fx,axis=-1)-1),
                F_relative=normmax(np.sum(Fx*Ft,axis=-1)/a0),
                G_relative=normmax(np.sum(Ft*Ft,axis=-1)/a0**2-1))


def finite_difference_audit(R,A,m,h):
    rows=[]
    for n in (32,64,128,256,512,1024):
        theta=np.arange(n)*2*np.pi/n
        x=np.array([-.6*h,0.,.6*h])[:,None]
        dt=2*np.pi/n
        dx=.2/n
        def F(xx,tt):
            return evaluate(xx,tt,R,A,m)['F']
        Fx=(-F(x+2*dx,theta)+8*F(x+dx,theta)-8*F(x-dx,theta)+F(x-2*dx,theta))/(12*dx)
        Ft=(-F(x,theta+2*dt)+8*F(x,theta+dt)-8*F(x,theta-dt)+F(x,theta-2*dt))/(12*dt)
        exact=evaluate(x,theta,R,A,m)
        rows.append(dict(Ntheta=n,Nradial_scale=n,
                         **metric_summary(Fx,Ft,exact['a0']),
                         Fx_error=normmax(Fx-exact['Fx']),Ft_error=normmax(Ft-exact['Ft'])))
    return rows


def run(R,A,m,h):
    if not (R>0 and A>0 and isinstance(m,int) and m>=2):
        raise ValueError('Use R,A>0 and integer m>=2')
    wc=A*m*(m*m-1)/R
    wtbound=(wc*m/R)*(1+3*m*m*A*A*(1/(R*R)+(m*m-1)/(R*R+m*m*A*A)))
    kapbound=np.sqrt(R*R+m**4*A*A)/(R*R)
    Dbound=np.sqrt(1+wc*wc)
    dmin=1-h*wtbound
    radialmargin=R-h*Dbound
    normalmargin=R*R/((R*R+m*m*A*A)*kapbound)-h*Dbound
    bounds=dict(w_bound=wc,w_t_bound=wtbound,central_kappa_bound=kapbound,
                D_length_bound=Dbound,implicit_denominator_lower=dmin,
                projected_radial_support_lower=radialmargin,
                negative_normal_dot_horizontal_lower=normalmargin,
                principal_curvature_upper=kapbound*(1+wc*wc)/dmin if dmin>0 else None,
                diameter_upper=2*(np.sqrt(R*R+A*A)+h*Dbound),
                embedding_sufficient=bool(dmin>0 and radialmargin>0 and normalmargin>0))
    x=np.linspace(-h,h,201)[:,None]
    theta=np.arange(4096)*2*np.pi/4096
    g=evaluate(x,theta,R,A,m)
    metric=metric_summary(g['Fx'],g['Ft'],g['a0'])
    z=g['F'][...,2]
    E=np.sum(g['Fx']**2,axis=-1)
    FF=np.sum(g['Fx']*g['Ft'],axis=-1)
    G=np.sum(g['Ft']**2,axis=-1)
    L=np.sum(g['Fxx']*g['N'],axis=-1)
    M=np.sum(g['Fxt']*g['N'],axis=-1)
    NN=np.sum(g['Ftt']*g['N'],axis=-1)
    gauss=(L*NN-M*M)/(E*G-FF*FF)
    center=evaluate(0.,theta,R,A,m)
    gamma0=geometry(theta,R,A,m)
    samp=dict(**metric,implicit_equation_error=normmax(g['residual']),
              Gaussian_curvature_error=normmax(gauss),
              max_principal_curvature=float(np.max(np.abs(g['kappa']))),
              implicit_denominator_min=float(np.min(g['den'])),
              central_height_PV=float(np.ptp(center['F'][:,2])),
              max_ring_height_PV=float(np.max(np.ptp(z,axis=1))),
              max_abs_w=float(np.max(np.abs(gamma0['w']))),
              max_abs_w_t=float(np.max(np.abs(gamma0['wt']))),
              closure_position_error=normmax(evaluate(np.linspace(-h,h,31),0.,R,A,m)['F']-
                                             evaluate(np.linspace(-h,h,31),2*np.pi,R,A,m)['F']))
    return dict(status='EXACT LOCAL CORE ONLY; no rotational collars or caps',
                parameters=dict(R=R,A=A,m=m,halfwidth=h,core_intrinsic_width=2*h,
                                prospective_total_width_scale=1.,a0=float(g['a0'])),
                rigorous_formula_bounds=bounds,sampled_identities=samp,
                same_geometry_fourth_order_finite_difference_audit=finite_difference_audit(R,A,m,h),
                outstanding=['Construct genuine C2 transition(s) to rotational open collars',
                             'Close with caps, certify all twist phases and total width/diameter',
                             'Independent audit of any proposed full annulus'])


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--R',type=float,default=.5)
    p.add_argument('--A',type=float,default=.1)
    p.add_argument('--m',type=int,default=2)
    p.add_argument('--halfwidth',type=float,default=.05)
    p.add_argument('--out',type=Path,default=Path('notes/construct_rectifying_wavy_core.json'))
    args=p.parse_args()
    result=run(args.R,args.A,args.m,args.halfwidth)
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':
    main()
