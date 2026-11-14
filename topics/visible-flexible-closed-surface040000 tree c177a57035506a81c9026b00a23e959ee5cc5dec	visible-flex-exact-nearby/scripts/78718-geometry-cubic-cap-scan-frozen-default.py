#!/usr/bin/env python3
"""Exploratory small ODE/BVP calculation of the first cubic cap obstruction.

No rigorous interval certificate or exact nonlinear isometric family is claimed.
Only compact scalar summaries are written; dense solver arrays are not serialized.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp, solve_bvp, quad
from scipy.optimize import brentq
from scipy.special import expit


def step(x):
    x = np.asarray(x, dtype=float)
    val = np.zeros_like(x)
    d1 = np.zeros_like(x)
    d2 = np.zeros_like(x)
    val[x >= 1] = 1.0
    mask = (x > 0) & (x < 1)
    w = x[mask]
    f = -1/w+1/(1-w)
    fp = 1/w**2+1/(1-w)**2
    fpp = -2/w**3+2/(1-w)**3
    h = expit(f)
    val[mask] = h
    d1[mask] = h*(1-h)*fp
    d2[mask] = h*(1-h)*((1-2*h)*fp**2+fpp)
    return val, d1, d2


def bump(x):
    x = np.asarray(x, dtype=float)
    val = np.zeros_like(x)
    d1 = np.zeros_like(x)
    d2 = np.zeros_like(x)
    mask = (x > 0) & (x < 1)
    w = x[mask]
    h = np.exp(4-1/w-1/(1-w))
    fp = 1/w**2-1/(1-w)**2
    fpp = -2/w**3-2/(1-w)**3
    val[mask] = h
    d1[mask] = h*fp
    d2[mask] = h*(fp**2+fpp)
    return val, d1, d2


class Profile:
    def __init__(self, join, amplitude, width=.2):
        self.join = float(join)
        self.amplitude = float(amplitude)
        self.width = float(width)
        self.sigma = np.sqrt(1+2*self.join**2)
        self.center = 2*self.join
        self.end = self.join+self.width
        self.knots = sorted(set([0., .25, .5, .8, 1.2,
                                 self.join-self.width, self.end]))

    def __call__(self, z):
        original_shape = np.shape(z)
        z = np.atleast_1d(np.asarray(z, dtype=float))
        ah = np.sqrt(1+z*z)
        ah1, ah2 = z/ah, 1/ah**3
        h,h1,h2 = step((z-.25)/.25)
        h1,h2 = h1/.25,h2/.25**2
        a = 1+h*(ah-1)
        a1 = h1*(ah-1)+h*ah1
        a2 = h2*(ah-1)+2*h1*ah1+h*ah2
        mask = z >= self.join-self.width
        if np.any(mask):
            w=z[mask]
            sphere=np.sqrt(self.sigma**2-(w-self.center)**2)
            sphere1=-(w-self.center)/sphere
            sphere2=-self.sigma**2/sphere**3
            h,h1,h2=step((w-self.join+self.width)/(2*self.width))
            h1,h2=h1/(2*self.width),h2/(2*self.width)**2
            delta=sphere-ah[mask]
            delta1=sphere1-ah1[mask]
            delta2=sphere2-ah2[mask]
            a[mask]=ah[mask]+h*delta
            a1[mask]=ah1[mask]+h1*delta+h*delta1
            a2[mask]=ah2[mask]+h2*delta+2*h1*delta1+h*delta2
        h,h1,h2=bump((z-.8)/.4)
        a=a+self.amplitude*h
        a1=a1+self.amplitude*h1/.4
        a2=a2+self.amplitude*h2/.4**2
        return tuple(v.reshape(original_shape) for v in (a,a1,a2))


def first_order(profile, n, rtol):
    def rhs(z, state):
        a,az,azz=(float(k) for k in profile(np.array(z)))
        v,p,mean=state
        h0=(p*p/a**3-azz*v*v)/2
        return [n*p/a**2, -n*a*azz*v, az*h0]
    sol=solve_ivp(rhs,[0,profile.end],[1.,0.,0.],method="DOP853",
                  rtol=rtol,atol=rtol*.01,dense_output=True,max_step=.025)
    if not sol.success:
        raise RuntimeError(sol.message)
    v,p,_=sol.y[:,-1]
    residual=(p+profile.sigma*v)/np.hypot(p,profile.sigma*v)
    return float(residual),sol


def cubic(profile,n,rtol):
    residual,first=first_order(profile,n,rtol)
    N=2*n
    def rhs(z,state):
        a,az,azz=profile(z)
        v,p,_=first.sol(z)
        h2=-(p*p/a**3+azz*v*v)/2
        zz,yy=state
        return np.vstack((N*yy/a**2+az*h2,
                          -N*a*azz*zz-N*a*(1+az*az)*h2))
    def jac(z,state):
        a,az,azz=profile(z)
        out=np.zeros((2,2,len(z)))
        out[0,1]=N/a**2
        out[1,0]=-N*a*azz
        return out
    def bc(left,right):
        return np.array([left[1],right[1]+profile.sigma*right[0]])
    def bcjac(left,right):
        return np.array([[0,1],[0,0]]),np.array([[0,0],[profile.sigma,1]])
    mesh=np.unique(np.r_[np.linspace(0,profile.end,301),profile.knots])
    second=solve_bvp(rhs,bc,mesh,np.zeros((2,len(mesh))),tol=max(rtol*100,1e-7),
                     max_nodes=15000,fun_jac=jac,bc_jac=bcjac)
    if not second.success:
        raise RuntimeError("second order BVP: "+second.message)

    def bridge(z):
        a,az,azz=(float(k) for k in profile(np.array(z)))
        v,p,mean=(float(k) for k in first.sol(z))
        zz,yy=(float(k) for k in second.sol(z))
        h0=(p*p/a**3-azz*v*v)/2
        h2=-(p*p/a**3+azz*v*v)/2
        h3=p*yy/a**3-azz*v*(2*mean+zz)-(1+az*az)*v*(h0+h2/2)
        kernel=n*az*p+n*n*a*(1+az*az)*v
        return kernel*h3
    qbridge=0.; err=0.
    for left,right in zip(profile.knots[:-1],profile.knots[1:]):
        v,e=quad(bridge,left,right,epsabs=rtol*20,epsrel=rtol*20,limit=300)
        qbridge+=v;err+=e

    sigma=profile.sigma
    end=profile.end
    ts=np.sqrt((sigma-end+profile.center)/(sigma+end-profile.center))
    v,p,mean=first.y[:,-1]
    d=v/ts**n
    d2=second.sol(end)[0]/ts**(2*n)
    analytic_mean=d*d*(ts**(2*n-2)/(2*n-2)-ts**(2*n+2)/(2*n+2))/4
    # Exact antiderivative of the polynomial spherical-core integrand.
    poly=np.polynomial.polynomial.polymul([1.,1.],[n+1.,n-1.])
    selfpoly=np.polynomial.polynomial.polymul(
        poly,[(2.-n)/(n-1.),-2.,-(n+2.)/(n+1.)])
    qself=n*sigma*d**4/16*sum(c*ts**(4*n-4+2*k)/(4*n-4+2*k)
                             for k,c in enumerate(selfpoly))
    qcross=n*sigma*d*d*d2/2*sum(c*ts**(4*n-2+2*k)/(4*n-2+2*k)
                               for k,c in enumerate(poly))
    # Homogeneous doubled-mode mismatch: a nonzero value is only numerical evidence.
    doubled,_=first_order(profile,N,rtol)
    return dict(n=n,join=profile.join,bump=profile.amplitude,width=profile.width,
                rtol=rtol,resonance_residual=residual,
                doubled_resonance_residual=doubled,
                second_bvp_nodes=int(len(second.x)),
                second_bvp_max_rms=float(np.max(second.rms_residuals)),
                boundary_second_curvature=float(second.sol(0)[0]),
                mean_core_discrepancy=float(mean-analytic_mean),
                cubic_bridge=float(qbridge),cubic_core_self=float(qself),
                cubic_core_cross=float(qcross),
                cubic_total=float(qbridge+qself+qcross),
                quadrature_error_estimate=float(err),
                evidence="floating-point exploratory ODE/BVP; not certified")


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--n",type=int,default=3)
    ap.add_argument("--join-min",type=float,default=1.5)
    ap.add_argument("--join-max",type=float,default=6.)
    ap.add_argument("--scan",type=int,default=31)
    ap.add_argument("--bump",type=float,default=0.)
    ap.add_argument("--rtol",type=float,default=1e-10)
    ap.add_argument("--output",type=Path,required=True)
    args=ap.parse_args()
    grid=np.linspace(args.join_min,args.join_max,args.scan)
    vals=[first_order(Profile(j,args.bump),args.n,args.rtol)[0] for j in grid]
    roots=[]
    for j0,j1,f0,f1 in zip(grid[:-1],grid[1:],vals[:-1],vals[1:]):
        if f0*f1 < 0:
            fun=lambda j:first_order(Profile(j,args.bump),args.n,args.rtol)[0]
            root=brentq(fun,j0,j1,xtol=1e-11,rtol=1e-13)
            try:
                roots.append(cubic(Profile(root,args.bump),args.n,args.rtol))
            except RuntimeError as exc:
                roots.append(dict(n=args.n,join=root,bump=args.bump,error=str(exc),
                                  evidence="failed exploratory run; no certificate"))
    doc=dict(status="exploratory only",count=len(roots),results=roots)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(doc,indent=2)+"\n")
    print(json.dumps(dict(count=len(roots),n=args.n,bump=args.bump,
          summaries=[dict(join=r["join"],cubic_total=r.get("cubic_total"),
                     resonance_residual=r.get("resonance_residual"),
                     mean_core_discrepancy=r.get("mean_core_discrepancy"),error=r.get("error"))
                     for r in roots]),indent=2))


if __name__=="__main__":
    main()
