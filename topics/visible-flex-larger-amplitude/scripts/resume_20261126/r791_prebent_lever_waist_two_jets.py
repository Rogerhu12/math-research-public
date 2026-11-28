"""R791. A pre-bent round waist between a moving lever and a fixed broad head.

This module evaluates the analytical all-angle construction. Solver trial
fields with noncircular or spatial sections are separate physical inputs.
"""
from functools import lru_cache
import numpy as np
from r742_tilted_disk_two_jets import J,unary,trig,gather
from r740_rolled_disk_seed import rule
from r767_negative_track_profile import clock,smooth_curve,ROUND

R=.43
WAIST=.11
P=2*np.pi*R
HALF_WIDTH=1.4
SHIFT=.55
LEFT=-.85
RIGHT=1.95
BEND=1.4
FLARE=.55
HEAD=.105
SM=.001
L=HEAD*np.pi/2+SM
D_UPPER=3.22
MATERIAL_GRIP_WIDTH=.035


def step(x):
    z=np.clip(x.v,0.,1.)
    return unary(x,z**3*(10.+z*(-15.+6*z)),30*z*z*(1-z)**2,60*z*(1-z)*(1-2*z))


def participation(t):
    return .10+.55*np.sin(float(t))**2


@lru_cache(maxsize=256)
def spine_table(phi,order):
    k=BEND*np.array([0.,ROUND,1.-ROUND,1.]);nodes,weights=rule(order);width=np.diff(k)
    z=k[:-1,None]+width[:,None]*nodes
    psi=phi*(1-clock(z/BEND)[0])
    rows=np.stack((np.sin(psi)@weights,np.cos(psi)@weights),axis=1)
    return k,np.vstack((np.zeros(2),np.cumsum(width[:,None]*rows,axis=0)))


def spine(s,t,order):
    phi=participation(t);v=np.asarray(s.v);q,qp,qpp=clock(v/BEND)
    psi=unary(s,phi*(1-q),-phi*qp/BEND,-phi*qpp/BEND**2)
    k,tab=spine_table(phi,order);nodes,weights=rule(order)
    a=np.clip(v,0.,BEND);ii=np.clip(np.searchsorted(k,a,side="right")-1,0,len(k)-2)
    h=a-k[ii];z=k[ii,None]+h[:,None]*nodes
    angle=phi*(1-clock(z/BEND)[0])
    tail=tab[ii]+h[:,None]*np.stack((np.sin(angle)@weights,np.cos(angle)@weights),axis=1)-tab[-1]
    left=np.minimum(v,0.);right=np.maximum(v-BEND,0.)
    xx=tail[:,0]+left*np.sin(phi)
    yy=BEND+tail[:,1]+left*np.cos(phi)+right
    cp,sp=trig(psi);kp=-phi*qp/BEND
    cx=unary(s,xx,sp.v,cp.v*kp)
    cy=unary(s,yy,cp.v,-sp.v*kp)
    return cx,cy,cp,sp


def radius(s):
    return WAIST+(R-WAIST)*(step(-s/FLARE)+step((s-BEND)/FLARE))


@lru_cache(maxsize=32)
def end_limits(order=20):
    p,d=smooth_curve(J(np.array([L])),L,HEAD,SM,order)
    return float(p.v[0]),float(d.v[0])


def normal_to_disk_material(e,w,order=20):
    return e,1-w/(R-end_limits(order)[1])


def offset(e,d,order=20):
    c,z=trig(e/R);return [(R-d)*c,(R-d)*z]


def disk_world(x,z,order=20):return x,z


def profile_marks():return list(P*np.arange(24)/24)


def axial_marks():
    return np.unique(np.r_[LEFT,-FLARE,-FLARE/2,0.,ROUND*BEND,BEND/2,(1-ROUND)*BEND,
                           BEND,BEND+FLARE/2,RIGHT]-SHIFT).tolist()


def material_radius(x,order=20):return radius(J(np.asarray(x,float))).v


def intrinsic_data(s,theta):
    # Exact pointwise coefficients of the unsheared waist and flanks in (s,theta).
    u=J(np.asarray(s,float),s=1.);r=radius(u)
    kp=-.10*clock(np.asarray(s,float)/BEND)[1]/BEND
    return (1-r.v*kp*np.cos(theta))**2+r.s**2,np.zeros_like(r.v),r.v**2


def view(coords,s,t,order):
    cx,cy,cp,sp=spine(s,t,order)
    xi,tangent,z=coords
    return [cx+xi*cp+tangent*sp,cy-xi*sp+tangent*cp,z]


def chart_jet(chart,u,v,phase=0.,order=20):
    a,b=np.broadcast_arrays(np.asarray(u,float),np.asarray(v,float))
    e=J(a.ravel(),s=1.);w=J(b.ravel(),a=1.)
    c,z=trig(e/R);zero=J(np.zeros(len(e.v)))
    if chart=="cylinder":
        s=w+SHIFT;r=radius(s);coords=[r*c,zero,r*z]
    else:
        sg=1 if chart.endswith("+") else -1
        ring=RIGHT if sg>0 else LEFT
        if chart.startswith("end"):
            p,d=smooth_curve(w,L,HEAD,SM,order)
            s=ring+sg*p;coords=[(R-d)*c,zero,(R-d)*z]
        elif chart.startswith("cap"):
            pb,db=end_limits(order);s=J(np.full(len(e.v),ring+sg*pb))
            if "cartesian" in chart:coords=[e,zero,w]
            elif "normal" in chart:coords=[(R-db-w)*c,zero,(R-db-w)*z]
            else:coords=[w*(R-db)*c,zero,w*(R-db)*z]
        else:raise ValueError(chart)
    return gather(view(coords,s,phase,order),len(e.v)).reshape(a.shape+(6,3))
