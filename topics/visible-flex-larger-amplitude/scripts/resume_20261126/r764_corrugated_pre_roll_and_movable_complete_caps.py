#!/usr/bin/env python3
"""R764 complete embedded R760-section family with two corrugated pre-rolls and both real cap images."""
from functools import lru_cache
import numpy as np
import r760_cartesian_curved_crown_and_lower_rate_walls as old
from r742_tilted_disk_two_jets import J,unary,trig,cap_s7,gather

m=old.m
HALF=.88
E=.44
EPS=.0025
ENDS=(.13,.14)
L=m.END_L
PERIOD=old.material
JOIN=old.JOIN

def smooth5(t):
    a=np.clip(t.v,0.,1.)
    return unary(t,a**3*(10+a*(-15+6*a)),30*a*a*(1-a)**2,60*a*(1-a)*(1-2*a))

def initial_turn(v,order):
    """Unnormalized two-jet of the exact original pre-roll integrals p,d."""
    a=np.asarray(v.v);angle=lambda z:EPS*np.sin(2*np.pi*z/E)*np.sin(np.pi*z/E)**2
    av=angle(a);w=np.pi*a/E
    ap=EPS*np.pi/E*(2*np.cos(2*w)*np.sin(w)**2+np.sin(2*w)**2)
    p,d=m.old.disk.integrals(a,(0.,E/2,E),angle,order)
    # Antisymmetry gives the exact endpoint normal displacement.
    d=np.where(a==E,0.,d)
    return unary(v,p,np.cos(av),-ap*np.sin(av)),unary(v,d,np.sin(av),ap*np.cos(av))

@lru_cache(maxsize=6)
def axial(order):
    return float(initial_turn(J(np.asarray([E])),order)[0].v[0])

def signed(chart):
    return 1 if chart.endswith("+") else -1

def chart_jet(chart,u,v,phase=0.,order=32,retreat=.14,rotate=True):
    m.old.disk._public()
    if retreat not in ENDS:
        raise ValueError("R764 registered terminal retreat")
    a,b=np.broadcast_arrays(np.asarray(u,float),np.asarray(v,float));shape=a.shape
    a,b=a.ravel(),b.ravel();ph=float(phase)
    if not 0<=ph<=.90000000000001:
        raise ValueError("phase outside R764 family")
    eta=retreat*ph/.90;side=signed(chart);name=chart[:-1]
    if chart=="cylinder":
        if np.any(np.abs(b)>HALF+2e-13):
            raise ValueError("central interval")
        out=old.chart_jet(chart,a,b,ph,order,rotate=False)
    elif name=="preband":
        if np.any((b<0)|(b>E+2e-13)):
            raise ValueError("pre-roll interval")
        s,vv=J(a,s=1.),J(b,a=1.)
        pp,dd=initial_turn(vv,order);h=smooth5(vv/E)
        cx=m.section_center(order)
        def planar(theta):
            q,n=old.profile(s,theta,order,True)
            return old.polar(s,q[0]-cx-dd*n[0],q[1]-dd*n[1],order)[:2]
        ra,pa=planar(ph);rb,pb=planar(0.)
        r=(1-h)*ra+h*rb;co,si=trig((1-h)*pa+h*pb)
        out=gather((cx+r*co,side*(HALF+pp-eta*h),r*si),len(a))
    else:
        nm=("end"+chart[-1]) if name=="round" else chart
        if name not in ("round","cap","cap-normal","cap-cartesian"):
            raise ValueError("unknown R764 chart")
        out=old.chart_jet(nm,a,b,0.,order,rotate=False)
        out[:,0,1]+=side*(HALF-1+axial(order)-eta)
    if rotate:
        ox,oz=m.axis(order);c,h=np.cos(ph),np.sin(ph)
        x=out[:,:,0].copy();z=out[:,:,2].copy();x[:,0]-=ox;z[:,0]-=oz
        out[:,:,0]=c*x-h*z;out[:,:,2]=h*x+c*z;out[:,0,0]+=ox;out[:,0,2]+=oz
    return out.reshape(shape+(6,3))

def gate(kind,s,y,order):
    if kind!="cylinder":
        return J(np.ones_like(s.v))
    alpha=(s-m.grip_s(0.,order))/m.old.PLANAR_TURN
    angular=cap_s7((alpha-.10)/.08)*cap_s7((1.05-alpha)/.09)
    yy=cap_s7((.78**2-y*y)/(.78**2-.70**2))
    return 1-angular*yy

def legacy_prices(order):
    """Actual metric address and symmetric path addressed by the old R760 boundary evidence."""
    lh,m0,m1,rtop,xl,xr,ux,uz,start,stop,core,half=m.constants(order)
    s=m.LEFT_LENGTH/2+stop-.05;w=.0065;ch="cap-normal+"
    base=old.chart_jet(ch,s,w,0.,order,rotate=False);end=old.chart_jet(ch,s,w,.9,order,rotate=False)
    q0=old.data(np.array([s]),0.,order,True);q1=old.data(np.array([s]),.9,order,True)
    beta=.49;k=np.pi/(2*.26*.875);xe=.30+.26*.125
    beta_e=float(m.old.disk.beta(np.asarray(xe)))
    material_x=xe+(beta-beta_e)/k
    sm=float(m.flat_material_s(np.asarray([material_x]),order=order)[0])
    p0=old.data(np.array([sm]),0.,order,True);p1=old.data(np.array([sm]),.9,order,True)
    db=m.terminal(order)[1]
    projected_z=p0[0][0,1]-db*p0[2][0,1]
    path=2*L+2*projected_z*np.sqrt(1+.00075**2)
    chord=2*p1[0][0,1]
    return {"angular_address":[s,w],"k":[float(q0[3][0]),float(q1[3][0])],
        "gss":[float(base[1]@base[1]),float(end[1]@end[1])],
        "symmetric_path":[sm,material_x,float(path),float(chord),float(chord-path)]}
