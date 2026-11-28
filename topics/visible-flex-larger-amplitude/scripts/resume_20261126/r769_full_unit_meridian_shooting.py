#!/usr/bin/env python3
"""Complete R769 unit-speed meridians, with a moving interface and two genuine capped ends."""
from functools import lru_cache
from hashlib import sha256
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import least_squares
import r769_closed_turn_redistribution_and_complete_rolls as geom
from r742_tilted_disk_two_jets import J,unary,cap_s7,gather,trig
base,old,m=geom.base,geom.old,geom.m
E,L,B=geom.E,geom.L,geom.B
T=E+L
RETREATS=(.30,.42)
CUTS=(0.,E/4,E/2,3*E/4,E,E+m.END_E,E+L/2,T-m.END_E,T)

def old_angle(u):
    reg=u>E
    p,dp=geom.angle(np.minimum(u,E),False)
    r,dr=geom.angle(np.maximum(0.,u-E),True)
    return np.where(reg,r,p),np.where(reg,dr,dp)

def weight(u):
    x=u/T
    return 16*(x*(1-x))**2,32*x*(1-x)*(1-2*x)/T

def factor(h):
    """tanh(sqrt(h))/sqrt(h), with first two derivatives continuous at zero."""
    x=np.asarray(h);safe=np.maximum(x,.001);t=np.sqrt(safe);f=np.tanh(t)/t;c=1/np.cosh(t)**2
    d=(c-f)/(2*safe);dd=(-c*f-3*d)/(2*safe)
    co=(1.,-1/3,2/15,-17/315,62/2835,-1382/155925,21844/6081075)
    sm=x<.001;z=np.where(sm,x,0.)
    return (np.where(sm,np.polynomial.polynomial.polyval(z,co),f),
        np.where(sm,np.polynomial.polynomial.polyval(z,[i*a for i,a in enumerate(co) if i]),d),
        np.where(sm,np.polynomial.polynomial.polyval(z,[i*(i-1)*a for i,a in enumerate(co) if i>=2]),dd))

def tangent_plain(xi,u):
    al,_=old_angle(u);w=weight(u)[0]/2;h=(xi@xi)*w*w
    p=(w*factor(h)[0])[:,None]*xi
    a=p+np.column_stack((np.zeros_like(u),np.cos(al),np.sin(al)))
    den=np.einsum("ij,ij->i",a,a)
    return p+((1-np.einsum("ij,ij->i",p,p))/den)[:,None]*a

@lru_cache(maxsize=16)
def quad(order):
    x,w=m.old.disk.rule(order)
    return (np.concatenate([l+(h-l)*x for l,h in zip(CUTS[:-1],CUTS[1:])]),
            np.concatenate([(h-l)*w for l,h in zip(CUTS[:-1],CUTS[1:])]))

def target(s,ph,order,retreat):
    q=geom.curve(s,ph,order)[0];q0,t,n,_,_=old.data(s,0.,order,True)
    sh=geom.right_motion(order,ph);pb,db=m.terminal(order)
    dy=base.axial(order)+pb-retreat*(ph/.90)
    guess=q0+sh-db*n-q;z=np.linalg.norm(guess,axis=1)
    radius=np.sqrt((T-.005)**2-dy**2);low=.9*radius;gap=radius-low
    ex=np.maximum(0.,z-low);cap=low+ex/(1+(ex/gap)**4)**.25
    multiplier=np.ones_like(z);mask=z>low;multiplier[mask]=cap[mask]/z[mask]
    planar=guess*multiplier[:,None]
    three=np.column_stack((np.einsum("ij,ij->i",t,planar),np.full(len(q),dy),
                           -np.einsum("ij,ij->i",n,planar)))
    return three,np.column_stack((np.hypot(z,dy)-T,np.linalg.norm(three,axis=1)-T,
                                   np.linalg.norm(planar-guess,axis=1)))

@lru_cache(maxsize=112)
def controls(order,ph,retreat):
    n={16:96,24:192,32:384}[order]
    period=2*old.material(order,True)[-1];s0=geom.stations(order)[0]
    s=np.unique(np.r_[np.arange(n)*period/n,s0,period-s0]);s=s[(s>=0)&(s<period-1e-13)]
    s=s[np.r_[True,np.diff(s)>2e-12]]
    D,prices=target(s,ph,order,retreat)
    u,w=quad(order);coef=[];neval=[];residual=[];previous=np.zeros(3)
    for d in D:
        def residual_at(p):
            return w@tangent_plain(p,u)-d
        if not ph:
            p=np.zeros(3);calls=0
        else:
            opt=least_squares(residual_at,previous,bounds=(-18.,18.),max_nfev=72,
                              ftol=1e-13,xtol=1e-13,gtol=1e-13)
            p=opt.x;calls=opt.nfev
            if np.linalg.norm(opt.fun)>3e-9:
                for seed in (np.zeros(3),np.clip(3*d/T,-4.,4.)):
                    alt=least_squares(residual_at,seed,bounds=(-18.,18.),max_nfev=144,
                                      ftol=1e-14,xtol=1e-14,gtol=1e-14)
                    calls+=alt.nfev
                    if np.linalg.norm(alt.fun)<np.linalg.norm(residual_at(p)):
                        p=alt.x
        coef.append(p);neval.append(calls);residual.append(np.linalg.norm(residual_at(p)));previous=p
    vals=np.asarray(coef);ss=np.r_[s,period]
    spl=CubicSpline(ss,np.vstack((vals,vals[0])),axis=0,bc_type="periodic")
    # Independent whole-circle midpoint prices of the actual interpolated roots.
    mid=(ss[:-1]+ss[1:])/2;DM,pm=target(mid,ph,order,retreat)
    err=np.array([np.linalg.norm(w@tangent_plain(p,u)-d) for p,d in zip(spl(mid),DM)])
    def extrem(z):
        i=int(np.argmax(z));return [float(z[i]),float(s[i])]
    b=np.asarray(vals,dtype="<f8").tobytes()
    record={"distinct_periodic_controls":len(s),"node_angular_max":[extrem(prices[:,j]) for j in range(3)],
            "edge_root_max":extrem(np.asarray(residual)),"evaluations":int(sum(neval)),
            "max_abs_control":float(np.max(np.abs(vals))),"coeff_bytes_sha256":[len(b),sha256(b).hexdigest()],
            "independent_midpoint_max":[float(err.max()),float(mid[np.argmax(err)])],
            "midpoint_angular_max":pm.max(axis=0).tolist(),"axial_retreat":retreat*ph/.90}
    return spl,period,record

def flow(xi,u):
    av,ad=old_angle(u.v);one=J(np.ones_like(u.v));w,dw=weight(u.v)
    # In this routine u has at most one nonzero entry among its first derivatives.
    # Only F_vv needs a first derivative of tangents in the transverse direction.
    v=unary(u,w,dw,0.)/2;al=unary(u,av,ad,0.);c,s=trig(al)
    h=v*v*sum((x*x for x in xi),J(0.))
    y,dy,ddy=factor(h.v);scale=v*unary(h,y,dy,ddy)
    p=[scale*x for x in xi];a=[p[0],p[1]+c,p[2]+s]
    den=sum((b*b for b in a),J(0.));num=one-sum((b*b for b in p),J(0.))
    return [b+(num/den)*c for b,c in zip(p,a)]

def integrals(s,v,ph,order,retreat):
    spl,period,_=controls(order,ph,retreat);u=np.mod(s.v,period)
    co,dc,ddc=spl(u),spl(u,1),spl(u,2)
    x,w=m.old.disk.rule(order);tot=np.zeros((3,3,len(u)))
    X=[J(co[:,j,None],s=dc[:,j,None],ss=ddc[:,j,None]) for j in range(3)]
    for low,high in zip(CUTS[:-1],CUTS[1:]):
        delta=np.clip(v.v-low,0.,high-low)
        if np.any(delta):
            vs=J(low+delta[:,None]*x)
            for j,component in enumerate(flow(X,vs)):
                for k,value in enumerate((component.v,component.s,component.ss)):
                    tot[j,k]+=delta*(value@w)
    local=[J(co[:,j],s=dc[:,j],ss=ddc[:,j]) for j in range(3)]
    # v=constant when building the cap rim.
    ut=flow(local,J(v.v,a=np.ones_like(u)))
    out=[]
    for j,t in enumerate(ut):
        val,ds,dss=tot[j]
        out.append(J(val,ds,t.v*v.a,dss,t.s*v.a,t.a*v.a*v.a+t.v*v.aa))
    return out

def block(chart,a,b,ph,order,retreat):
    if not ph:
        return base.chart_jet(chart,a,b,0.,order,.14,False)
    if chart=="cylinder":
        return geom.block(chart,a,b,ph,order,1.)
    side=1 if chart.endswith("+") else -1
    rawcap=chart.startswith("cap")
    if chart.startswith("cap-cartesian"):
        raw=base.chart_jet(chart,a,b,0.,order,.14,False)
        sh=geom.right_motion(order,ph)
        raw[:,0,0]+=sh[0];raw[:,0,2]+=sh[1];raw[:,0,1]-=side*retreat*(ph/.90)
        return raw
    s=J(a,s=1.);v=J(b,a=1.)
    q,_,_=geom.section(s,ph,order)
    qo,no=old.profile(s,0.,order,True)
    # The true initial oriented tangent T=(N_z,-N_x).
    tt=(no[1],-no[0]);w=J(np.full(len(a),T)) if rawcap else (v+E if chart.startswith("round") else v)
    along,axial,inward=integrals(s,w,ph,order,retreat)
    f=[q[i]+along*tt[i]-inward*no[i] for i in range(2)]
    if not rawcap:
        return gather((f[0],side*(B+axial),f[1]),len(a))
    raw=base.chart_jet(chart,a,b,0.,order,.14,False);pb,db=m.terminal(order)
    sh=geom.right_motion(order,ph);ret=retreat*(ph/.90)
    raw[:,0,0]+=sh[0];raw[:,0,2]+=sh[1];raw[:,0,1]-=side*ret
    cv=v if chart.startswith("cap-normal") else 1-v
    _,rho=old.collar_clock(cv);fade=cap_s7((rho-.83)/.15)
    dx=[fade*(f[i]-qo[i]-sh[i]+db*no[i]) for i in range(2)]
    dy=side*fade*(axial-base.axial(order)-pb+ret)
    return gather(tuple(J(*raw[:,:,i].T)+z for i,z in enumerate((dx[0],dy,dx[1]))),len(a))

def chart_jet(chart,u,v,ph,order,retreat,rotate=False):
    if retreat not in RETREATS:raise ValueError("R769 registered rigid-cap retreat")
    aa,bb=np.broadcast_arrays(np.asarray(u,float),np.asarray(v,float));sh=aa.shape
    a,b=aa.ravel(),bb.ravel()
    z=np.concatenate([block(chart,a[i:i+192],b[i:i+192],float(ph),order,retreat) for i in range(0,len(a),192)])
    if rotate:
        axis=np.asarray(m.axis(order));p=z[:,:,[0,2]].copy();p[:,0]-=axis
        p=geom.parent.rot(p,ph);p[:,0]+=axis;z[:,:,0]=p[:,:,0];z[:,:,2]=p[:,:,1]
    return z.reshape(sh+(6,3))
