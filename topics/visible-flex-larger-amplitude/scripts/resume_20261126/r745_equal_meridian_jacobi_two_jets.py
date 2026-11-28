#!/usr/bin/env python3
"""R745 equal-meridian tilted oval, full closed reference with stationary cubic markers.

Run on the project's public Actions. Chart convention, derivative order and
outward head arclength are those of R744. The tilt is solved from the actual
smoothed rolls, rather than from the limiting-circle comparison.
"""
from functools import lru_cache
import importlib.util
import numpy as np
from scipy.optimize import brentq
import r744_extruded_closed_two_jets as parent

H=.15
CX=.595
MARKS=((-0.10,.12,.077),(.10,.12,.086),(0.,-.13,.093))
HEIGHT=.002
# An independent module namespace keeps all original R744 functions and
# geometry constants intact for other callers in the same process.
spec=importlib.util.spec_from_file_location("r745_common_head_geometry",parent.__file__)
head=importlib.util.module_from_spec(spec)
spec.loader.exec_module(head)
J,unary=head.J,head.unary

@lru_cache(maxsize=64)
def constants(tilt,order=32):
    c,s=np.cos(tilt),np.sin(tilt)
    normal=np.array([-s,c]);center=np.array([CX,0.])
    rr=head.PLANAR_TURN;ep=head.PLANAR_BLEND
    al,ar=np.pi/2+tilt,np.pi-tilt
    left=rr*al+ep;right=rr*ar+ep
    _,_,_,lc,ls=head.turn(np.asarray(left),al,rr,ep,order)
    _,_,_,rc,rs=head.turn(np.asarray(right),ar,rr,ep,order)
    u,v=head.disk.bent_curve(np.asarray(1.),order);disk_right=np.array([u,H+v])
    pleft=np.array([-1.-lc,H-ls]);pright=disk_right+[rs,rc]
    hleft=float((pleft-center)@normal);hright=float((pright-center)@normal)
    wall_l=pleft-hleft*normal;wall_r=pright-hright*normal
    m0=hleft+left;m1=m0+2.;rtop=m1+right;half=rtop+hright
    return (hleft,m0,m1,rtop,half,float(wall_l[0]),float(wall_r[0]),float(u),float(H+v),
            normal,center,wall_l,wall_r,float(hright),float(left),float(right))

@lru_cache(maxsize=None)
def chosen(order=32):
    head.disk._public()
    def fun(v):
        z=constants(float(v),order)
        return z[13]+z[15]-z[0]-z[14]
    return float(brentq(fun,.47,.5,xtol=5e-15,rtol=1e-15))

def profile_constants(order):
    return constants(chosen(order),order)[:9]

def profile_coordinates(s,order=32):
    angle=chosen(order)
    lh,m0,m1,rtop,half,lx,rx,ux,uz,n,c,wl,wr,rh,ll,rl=constants(angle,order)
    raw=np.asarray(s,dtype=float);sh=raw.shape
    a=np.mod(raw.ravel(),2*half);lo=a>half;v=np.where(lo,2*half-a,a)
    pos=np.empty((len(v),2));t=np.empty_like(pos);k=np.zeros(len(v));kp=np.zeros_like(k)
    ii=v<=lh;pos[ii]=wl+v[ii,None]*n;t[ii]=n
    ii=(v>lh)&(v<=m0)
    al,kk,kkp,p,q=head.turn(m0-v[ii],np.pi/2+angle,head.PLANAR_TURN,head.PLANAR_BLEND,order)
    pos[ii]=np.stack([-1-p,H-q],axis=-1);t[ii]=np.stack([np.cos(al),np.sin(al)],axis=-1)
    k[ii]=kk;kp[ii]=-kkp
    ii=(v>m0)&(v<=m1);x=v[ii]-m0-1
    u,w=head.disk.bent_curve(x,order);be=head.disk.beta(x);kb=head.disk.curvature(x)
    z=(x-head.disk.HOLD)/head.disk.BEND
    d=np.clip(np.minimum(z,1-z)/head.disk.EDGE,0,1)
    bk=np.pi*30*d*d*(1-d)**2/(2*head.disk.BEND**2*(1-head.disk.EDGE)*head.disk.EDGE)
    bk*=np.where(z<.5,1.,-1.)
    pos[ii]=np.stack([u,H+w],axis=-1);t[ii]=np.stack([np.cos(be),np.sin(be)],axis=-1)
    k[ii]=-kb;kp[ii]=-bk
    ii=(v>m1)&(v<=rtop)
    al,kk,kkp,p,q=head.turn(v[ii]-m1,np.pi-angle,head.PLANAR_TURN,head.PLANAR_BLEND,order)
    pos[ii]=np.stack([ux+q,uz+p],axis=-1);t[ii]=np.stack([np.sin(al),np.cos(al)],axis=-1)
    k[ii]=kk;kp[ii]=kkp
    ii=v>rtop;pos[ii]=wr+(half-v[ii,None])*n;t[ii]=-n
    pos[lo]-=2*((pos[lo]-c)@n)[:,None]*n
    t[lo]=-(t[lo]-2*(t[lo]@n)[:,None]*n);kp[lo]*=-1
    normal=np.stack([-t[:,1],t[:,0]],axis=-1)
    return pos.reshape(sh+(2,)),t.reshape(sh+(2,)),normal.reshape(sh+(2,)),k.reshape(sh),kp.reshape(sh)

def step_second(t):
    """Twice integrated clamped S7(t/.02), including the exact linear tail of its first integral."""
    d=.02;u=np.clip(t.v/d,0.,1.)
    coeff=(35.,-84.,70.,-20.)
    q1=sum(c*u**(k+1)/(k+1) for k,c in enumerate(coeff,4))*d
    q2=sum(c*u**(k+2)/((k+1)*(k+2)) for k,c in enumerate(coeff,4))*d*d
    tail=np.maximum(t.v-d,0.)
    q2+=tail*d/2+tail**2/2;q1+=tail
    return unary(t,q2,q1,head.disk.s7(u))

def focus_amplitude(t):
    w=.02;u=unary(t,np.clip(t.v,0.,.30),((t.v>0.)&(t.v<.30)).astype(float),0.)
    a=u-.02;b=u-.26;scale=25/6
    source=scale*(head.cap_s7(a/w)-head.cap_s7(b/w))
    jacobi=1+u-scale*(step_second(a)-step_second(b))
    return (-head.PLANAR_TURN*source)/jacobi

def jacobi_height(u,y,amp,order):
    _,m0,m1,_,half,*_=profile_constants(order)
    pos=np.mod(u.v,2*half);lo=pos>half;sg=np.where(lo,-1.,1.)
    ss=J(np.where(lo,2*half-pos,pos),*(sg*v for v in u.parts()[1:]))
    t1,t2=m0-ss,ss-m1
    A=focus_amplitude(t1)+focus_amplitude(t2)
    yy=y*y;cut=1-yy;v=np.maximum(cut.v,0.)
    p=unary(cut,v**4,4*v**3,12*v**2)
    den=1+(1024.**2)*yy
    return amp*A*yy*p/(2*den*den)

def active(chart,u,v,phase,order,markers,gap_amplitude):
    if gap_amplitude not in (0,1):raise ValueError("expected original or full Jacobi-corrected physical profile")
    y=v if chart=="cylinder" else (1+v)*(1 if chart=="end+" else -1)
    su,yy,x,r2,lower=head.apply_phase_chart(u,y,phase,order)
    X,Y,Z=head.s_and_y(su,yy,order,gap_amplitude)
    cp,sp=np.cos(phase),np.sin(phase)
    X,Y=X*cp-Y*sp,X*sp+Y*cp
    if markers:
        for cx,cy,r in MARKS:
            dx=x-cx;dy=y-cy;b=1-(dx*dx+dy*dy)/(r*r)
            pos=np.where(lower,0.,np.maximum(b.v,0.))
            Z+=unary(b,HEIGHT*pos**3,3*HEIGHT*pos**2,6*HEIGHT*pos)
    return X,Y,Z

head.profile_constants=profile_constants
head.profile_coordinates=profile_coordinates
head.active_chart=active
head.gap_height=jacobi_height

def chart_jet(chart,u,v,phase=0.,order=32,markers=True,jacobi=True):
    return head.chart_jet(chart,u,v,phase=phase,order=order,markers=markers,gap_amplitude=int(jacobi))

def normal_jet(s,y,order=32):
    s,y=np.broadcast_arrays(np.asarray(s,float),np.asarray(y,float))
    f=jacobi_height(J(s,s=1.),J(y,a=1.),1.,order)
    return np.stack([np.asarray(v)+np.zeros(s.shape) for v in f.parts()],axis=-1)

def deformed_cylinder_jet(s,y,normal_data,order=32):
    """A real free correction in addition to the prescribed Jacobi field."""
    data=normal_jet(s,y,order)+np.asarray(normal_data)
    return head.deformed_cylinder_jet(s,y,data,order)

def cap_cartesian(x,z,side=1,phase=0.):
    return head.cap_cartesian(x,z,side,phase)

def disk_jet(rho,theta,phase=0.,side=1,order=32,markers=True):
    rho,theta,phase,side=np.broadcast_arrays(np.asarray(rho,float),np.asarray(theta,float),
                                             np.asarray(phase,float),np.asarray(side))
    sh=rho.shape;r=J(rho.ravel(),s=1.);a=J(theta.ravel(),a=1.);ph=phase.ravel()
    if np.any((r.v<0)|(r.v>1+2e-14)) or np.any((side!=1)&(side!=-1)):
        raise ValueError("disk material outside domain")
    _,m0,_,_,half,*_=profile_constants(order)
    ca,sa=head.trig(a)
    x,y=r*ca,r*sa
    upper=(side.ravel()==1)
    sg=np.where(upper,1.,-1.)
    u=J(np.where(upper,m0+1.,2*half-m0-1.))+x*sg
    # active() applies the same material rotation as the complete cylinder.
    return head.gather(active("cylinder",u,y,ph,order,markers,1.),len(r.v)).reshape(sh+(6,3))
