#!/usr/bin/env python3
"""R774 two complete nonintersecting material folds through a genuine flat R764 panel."""
import numpy as np
from r742_tilted_disk_two_jets import J,unary,gather
import r769_closed_turn_redistribution_and_complete_rolls as core

m=core.m;old=core.old;E,L,B=core.E,core.L,core.B
T=E+L;WIDTH=.35;P=.18;W1=.146;W2=.354;RAM=.0005
MAT_CENTER=-.30

def smooth(t):
    x=np.clip(t,0.,1.);return x**3*(10-15*x+6*x*x)

def rotate_matrix(axis,b):
    a=np.asarray(axis,float);ax,ay,az=a
    cross=np.array([[0.,-az,ay],[az,0.,-ax],[-ay,ax,0.]])
    return np.eye(3)*np.cos(b)+(1-np.cos(b))*np.outer(a,a)+np.sin(b)*cross

def pose(lam):
    l=lam/2;p=P
    b1=2*np.arctan2(np.sin(l),np.sin(p+l))
    q=-np.arctan2(1-np.cos(lam),np.tan(p)+np.sin(lam))
    cb=np.sin(p)/np.sqrt(2*(np.sin(p+l)**2+np.sin(l)**2))
    b2=-2*np.arccos(np.clip(cb,-1.,1.))
    c1=.004+WIDTH*np.tan(p)/2+W1/(2*np.cos(p))
    c2=c1+WIDTH*(np.tan(p)-np.tan(q))/2+W1/(2*np.cos(p))+W2/(2*np.cos(q))+.004
    return b1,q,b2,c1,c2

def clock(turn,width):
    return lambda v:m.old.disk.softened_angle(v,width,RAM,turn/(width-RAM))

def bend(s,v,axis,turn,width,ctr,order):
    cp,sp=np.cos(axis),np.sin(axis);p=-sp*s+cp*(v-ctr)+width/2
    z=p.v;w=np.clip(z,0.,width);alpha=clock(turn,width)
    a=alpha(w);edge=np.clip(np.minimum(w,width-w)/RAM,0.,1.)
    k=m.old.disk.s5(edge)*turn/(width-RAM)
    C,S=m.old.disk.integrals(w,(0.,RAM,width-RAM,width),alpha,order)
    tail=np.maximum(0.,z-width)
    U=unary(p,C-z.clip(0.,width)+tail*(np.cos(turn)-1),np.cos(a)-1,-k*np.sin(a))
    V=unary(p,S+tail*np.sin(turn),np.sin(a),k*np.cos(a))
    return [-sp*U,cp*U,V]

def apply(mat,j):
    return [sum((mat[i,n]*j[n] for n in range(3)),J(0.)) for i in range(3)]

def unrotated(a,b,time,upper,side,order):
    # Material coordinate a increases left-to-right on either corresponding panel.
    s=J(a,s=1.);v=J(b,a=1.);out=[s,v,J(np.zeros_like(a))]
    theta=.90*smooth((time-1/3)/(2/3))
    if time<=1/6:
        amp=1-smooth(time*6)
        pre=np.minimum(b,E)
        fun=lambda z:amp*core.angle(z,False)[0]
        p,d=m.old.disk.integrals(pre,(0.,E/4,E/2,3*E/4,E),fun,order)
        d=np.where(pre==E,0.,d)
        end=b>E
        rd=np.clip(b-E,0.,L);pr,dr=m.end(J(rd),order)
        angle=np.where(end,core.angle(rd,True)[0],fun(pre))
        ad=np.where(end,core.angle(rd,True)[1],amp*core.angle(pre,False)[1])
        out[1]=unary(v,p+pr.v,np.cos(angle),-np.sin(angle)*ad)
        out[2]=unary(v,-d-dr.v,-np.sin(angle),-np.cos(angle)*ad)
    else:
        lam=core.state(order,float(theta))[2] if theta else 0.
        b1,q,b2,c1,c2=pose(lam)
        t=smooth((time-1/6)*6);w2=(1-t)*L+t*W2;c2=(1-t)*(E+L/2)+t*c2
        f1=bend(s,v,P,b1,W1,c1,order);f2=bend(s,v,q,b2,w2,c2,order)
        r1=rotate_matrix([np.cos(P),np.sin(P),0.],b1)
        second=apply(r1,f2);out=[j+h+g for j,h,g in zip(out,f1,second)]
    label=float(m.flat_material_s(np.asarray([MAT_CENTER]),order=order)[0])
    if not upper:label=2*old.material(order,True)[-1]-label
    point,tan,n,_,_,*_=core.curve(np.asarray([label]),theta,order)
    # Lower labels increase right-to-left under the global traversal; the local a is physical material x.
    t=tan[0]*(1 if upper else -1);n=n[0]
    x=point[0,0]+out[0]*t[0]+out[2]*n[0]
    z=point[0,1]+out[0]*t[1]+out[2]*n[1]
    return gather((x,side*(B+out[1]),z),len(a)),theta

def local_jet(a,u,time=0.,upper=True,side=1,order=32,rotate=True):
    m.old.disk._public();aa,bb=np.broadcast_arrays(np.asarray(a,float),np.asarray(u,float));sh=aa.shape
    if not 0<=time<=1 or side not in (-1,1) or np.any(abs(aa)>WIDTH/2+2e-14) or np.any((bb<0)|(bb>T+2e-14)):
        raise ValueError("outside the complete R774 material rectangle")
    j,theta=unrotated(aa.ravel(),bb.ravel(),float(time),upper,side,order)
    if rotate:
        axis=np.asarray(m.axis(order));p=j[:,:,[0,2]].copy();p[:,0]-=axis
        p=core.parent.rot(p,theta);p[:,0]+=axis;j[:,:,0]=p[:,:,0];j[:,:,2]=p[:,:,1]
    return j.reshape(sh+(6,3))
