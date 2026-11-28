#!/usr/bin/env python3
"""R787 genuine long left section and once-filled terminal disks with the original right-wall clocks."""
from functools import lru_cache
import numpy as np
import r780_exact_bent_caps_and_closed_spatially_shifted_center as origin
from r742_tilted_disk_two_jets import J,unary,cap_s7

old,m=origin.old,origin.m
A=1.48
RADIUS=.15
WALL_RAMP=.0005
HOLD=.60
Q=RADIUS*A+WALL_RAMP
RESIDUAL_NORMAL=.0004
RADIAL_RAMP=.0004
RIM_TURN=RESIDUAL_NORMAL+RADIAL_RAMP/2

def stroke(t):return m.old.disk.softened_angle(t,Q,WALL_RAMP,1/RADIUS)

def angle(t):
    t=np.asarray(t)
    b=stroke(t)-stroke(t-Q-HOLD)
    up=np.clip(np.minimum(t,Q-t)/WALL_RAMP,0.,1.)
    q=t-Q-HOLD;dn=np.clip(np.minimum(q,Q-q)/WALL_RAMP,0.,1.)
    bp=(m.old.disk.s5(up)-m.old.disk.s5(dn))/RADIUS
    kd=lambda t,v:30*v*v*(1-v)**2*np.where(t<Q/2,1.,-1.)/(RADIUS*WALL_RAMP)
    return b,bp,kd(t,up)-kd(q,dn)

CLOCK=(0.,WALL_RAMP,Q-WALL_RAMP,Q,Q+HOLD,Q+HOLD+WALL_RAMP,2*Q+HOLD-WALL_RAMP,2*Q+HOLD)

@lru_cache(maxsize=16)
def spec(order):
    v,x=m.old.disk.integrals(np.asarray(CLOCK[-1]),CLOCK,lambda t:angle(t)[0],order)
    slack=m.Z_LEFT-float(v);length=CLOCK[-1]+slack
    return length,slack/2,float(x)

def parts(s,order):
    q,n=old.profile(s,0.,order,True);P=2*old.material(order,True)[-1]
    lab=np.mod(s.v,P);low=lab>P/2;z=np.where(low,P-lab,lab)
    half=m.LEFT_LENGTH/2;mask=z<half
    if not np.any(mask):return q,n
    sign=np.where(low,-1.,1.)
    U=unary(s,z,sign,0.);ell,stop,_=spec(order)
    a=U+(ell-half)*cap_s7(U/half)
    top=ell-a;t=top-stop
    v,h=m.old.disk.integrals(np.clip(t.v,0,CLOCK[-1]),CLOCK,lambda w:angle(w)[0],order)
    beta,k,kp=angle(t.v);si,co=np.sin(beta),np.cos(beta)
    h=unary(t,h,si,k*co)
    vertical=np.minimum(top.v,stop)+v+np.maximum(0.,t.v-CLOCK[-1])
    zz=unary(top,m.Z_LEFT-vertical,-co,k*si)
    xl=m.constants(order)[4];xx=xl-h
    # With the original positive material orientation the upper tangent is (sin beta,cos beta).
    # Reflection reverses the clockwise section parameter on the lower half.
    n1=unary(t,-co,k*si,kp*si+k*k*co)
    n2=unary(t,si,k*co,kp*co-k*k*si)
    def select(new,original):
        return J(*(np.where(mask,b,c) for b,c in zip(new.parts(),original.parts())))
    return [select(xx,q[0]),select(sign*zz,q[1])],[select(n1,n[0]),select(sign*n2,n[1])]

def cap_projection(chart,a,b,order):
    if chart.startswith(("cap-cartesian","cap-island")):
        return origin.inputs(chart,a,b)
    s,v=origin.inputs(chart,a,b);w=v if chart.startswith("cap-normal") else 1-v
    th=np.clip((w.v-RESIDUAL_NORMAL)/RADIAL_RAMP,0.,1.)
    j=np.where(w.v<RESIDUAL_NORMAL,w.v,RESIDUAL_NORMAL+RADIAL_RAMP*(th-2.5*th**4+3*th**5-th**6))
    j=unary(w,j,1-m.old.disk.s5(th),-30*th*th*(1-th)**2/RADIAL_RAMP)
    rho=1-(w-j)/(1-RIM_TURN)
    q,n=parts(s,order);dt=m.terminal(order)[1]+origin.LIP;cx=m.section_center(order)
    return cx+rho*(q[0]-cx-(dt+j)*n[0]),rho*(q[1]-(dt+j)*n[1])

def central(chart,a,b,order):
    s,v=origin.inputs(chart,a,b);q,n=parts(s,order)
    # The original marked upper-right arc is in the unchanged section, including every radius.
    h=m.marks(s,v,order)
    return q[0]+h*n[0],v,q[1]+h*n[1]
