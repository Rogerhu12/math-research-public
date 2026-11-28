"""Real arclength two-moment profiles for the R750 annulus. Science runs on public Actions."""
import numpy as np
from scipy.optimize import brentq

import r750_rigid_annulus as material

weak=material.weak
START=material.early.EARLY
TOTAL=material.space.TOTAL
LENGTH=TOTAL-START
STRAIGHT=material.early.FORCED_END-START
VERTICAL=.0001
A=1.2
K=10.
KNOTS=np.array([0.,.0005,.0015,.5,.9985,.9995,1.])


def rules(cuts,order):
    q,w=weak.physical.quadrature(order)
    lo=np.unique(np.asarray(cuts,float))
    half=np.diff(lo)/2
    return (lo[:-1,None]+half[:,None]*(1+q)).ravel(),(half[:,None]*w).ravel()


def step(t):
    val=weak.physical.sym_step(t)
    der=(weak.physical.mollifier_cdf((t-.001)/.0005)-weak.physical.mollifier_cdf((t-.999)/.0005))/.998
    return val,der


def original(build,z):
    z=np.asarray(z,float)
    theta=np.zeros(z.shape);slope=theta.copy()
    live=(z>=0.)&(z<=material.early.LENGTH)
    if np.any(live):theta[live],slope[live],_=build.profile.s.angle_jet(z[live])
    cap=z>material.early.LENGTH
    if np.any(cap):
        t=(z[cap]-material.early.LENGTH)/weak.physical.L
        v,d=step(t)
        theta[cap]=np.pi/2*v;slope[cap]=np.pi/(2*weak.physical.L)*d
    return theta,slope


def high_parameters(build,b,order):
    amp=np.array([-A,A+b,np.pi/2-b])
    widths=np.abs(amp)/K
    v,w=rules(KNOTS,order)
    theta=np.array([0.,-A,b])[:,None]+amp[:,None]*step(v)[0]
    ic=widths@(np.cos(theta)@w);isn=widths@(np.sin(theta)@w)
    free=LENGTH-STRAIGHT-VERTICAL-widths.sum()
    dwell_plus=(build.profile.ub-VERTICAL-isn+free*np.sin(A))/(np.sin(A)+np.sin(b))
    dwell_minus=free-dwell_plus
    if not (.059<dwell_minus<.124 and dwell_plus>.098):
        raise ArithmeticError('R760 true sine moment lost a positive material dwell')
    starts=np.array([STRAIGHT,STRAIGHT+widths[0]+dwell_minus,
                     STRAIGHT+widths[0]+dwell_minus+widths[1]+dwell_plus])
    offsets=STRAIGHT+ic+dwell_minus*np.cos(A)+dwell_plus*np.cos(b)
    return dict(b=float(b),starts=starts,widths=widths,dwell_minus=float(dwell_minus),
                dwell_plus=float(dwell_plus),x=float(offsets),
                u=float(VERTICAL+isn-dwell_minus*np.sin(A)+dwell_plus*np.sin(b)))


def high_angles(z,profile):
    z=np.asarray(z,float);angle=np.zeros_like(z);slope=np.zeros_like(z)
    for a,h,amp in zip(profile['starts'],profile['widths'],
                       (-A,A+profile['b'],np.pi/2-profile['b']),strict=True):
        t=(z-a)/h;inside=(t>0)&(t<1)
        angle[t>=1]+=amp
        if np.any(inside):
            v,d=step(t[inside]);angle[inside]+=amp*v;slope[inside]+=amp*d/h
    return angle,slope


def cuts(build,profile):
    native=np.r_[0.,LENGTH,
        *(a+h*KNOTS for a,h in ((0.,material.early.LEG),(material.early.LEG,2*material.early.LEG),
                         (3*material.early.LEG,material.early.LEG),(material.early.LENGTH,weak.physical.L)))]
    return np.unique(np.clip(np.r_[native,*(a+h*KNOTS for a,h in zip(
                     profile['starts'],profile['widths'],strict=True))],0.,LENGTH))


def solve_profile(build):
    target=build.profile.endx-(weak.physical.W+START)-.42
    if not .234<target<.244:raise ArithmeticError('wrong R743 full radial progress')
    def at(order):
        b=brentq(lambda b:high_parameters(build,b,order)['x']-target,1.9,2.1,xtol=2.e-14)
        return high_parameters(build,b,order)
    hi=at(48);lo=at(32)
    z,w=rules(cuts(build,hi),64);theta,_=high_angles(z,hi)
    val=np.array([w@np.cos(theta),w@np.sin(theta)])
    desired=np.array([target,build.profile.ub])
    if np.max(abs(val-desired))>3.e-11 or abs(hi['b']-lo['b'])>3.e-10:
        raise ArithmeticError('R760 two independent orders and complete material moments disagree')
    hi.update(target=desired,full_moments=val,lower_order_b=lo['b'],ell_breaks=START+cuts(build,hi))
    return hi


def phase_parameters(build,phase,profile,small=False):
    rcuts=cuts(build,profile)
    if small and phase>.08:raise ValueError('short-amplitude branch outside its proved range')
    def solve(order):
        z,w=rules(rcuts,order);o,op=original(build,z);high,hp=high_angles(z,profile)
        if small:
            delta=np.where(z<=material.early.LENGTH,o,0.)
            upper=7.8
        else:delta=high-o;upper=1.
        def loss_and_derivative(mu):
            angle=o+mu*delta
            # cos(o)-cos(angle) without order-one subtraction at tiny phases.
            return np.array([w@(2*np.sin(.5*(angle+o))*np.sin(.5*mu*delta)),
                             w@(np.sin(angle)*delta)])
        target=.42*np.sqrt(phase)
        if not phase:root=0.
        elif phase==1. and not small:root=1.
        else:root=brentq(lambda mu:loss_and_derivative(mu)[0]-target,0.,upper,xtol=2.e-14)
        loss,der=loss_and_derivative(root)
        return root,np.array([loss-target,der,w@np.sin(o+root*delta)])
    hi,v=solve(48);lo,u=solve(32)
    if abs(v[0])>4.e-11 or max(abs(hi-lo),max(abs(v-u)))>4.e-10 or v[1]<=0:
        raise ArithmeticError('R760 actual radial parameter or independent moment quadrature failed')
    return dict(phase=phase,small=bool(small),parameter=float(hi),lower_order=float(lo),
                horizontal_defect=float(v[0]),derivative=float(v[1]),vertical_moment=float(v[2]))


def mixture(build,z,profile,state):
    o,op=original(build,z);mu=state['parameter']
    if state['small']:
        enabled=np.asarray(z)<=material.early.LENGTH
        return o*(1+mu*enabled),op*(1+mu*enabled),o,op
    a,ap=high_angles(z,profile)
    return o+mu*(a-o),op+mu*(ap-op),o,op
