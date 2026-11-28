#!/usr/bin/env python3
"""R758 closed preloaded curved collars, a rigid common quadratic bowl and a free middle annulus."""
from functools import lru_cache
import numpy as np
import r756_return_elbows_preloaded_exact_rolls as pre
from r742_tilted_disk_two_jets import J,unary,trig,cap_s7,gather

m=pre.m
WIDTH=.007
ROUND=.001
JOIN=WIDTH+ROUND/2
BETA=.014
RHO_CORE=.82
EX=.494
EZ=.22
OFFSET=.49
BOWL=.040
FLAT_BREAK=.00030


def expj(z):
    val=np.exp(z.v)
    return unary(z,val,val,val)


def angle(x):
    t=np.clip(x/WIDTH,0.,1.)
    return BETA*m.old.disk.s5(t),BETA*30*t*t*(1-t)**2/WIDTH


def collar_clock(w):
    t=np.clip((w.v-WIDTH)/ROUND,0.,1.)
    val=np.where(w.v<WIDTH,w.v,WIDTH+ROUND*(t-2.5*t**4+3*t**5-t**6))
    j=unary(w,val,1-m.old.disk.s5(t),-30*t*t*(1-t)**2/ROUND)
    return j,1-(w-j)/(1-JOIN)


def meridian(j,psi,order):
    """True fixed arclength j along the new initially curved cap meridian."""
    d0,p0=m.old.disk.integrals(j.v,(0.,WIDTH,JOIN),lambda a:angle(a)[0],order)
    az,ap=angle(j.v);cb,sb=np.cos(az),np.sin(az)
    d=unary(j,d0,cb,-sb*ap)
    if not np.any(psi.v):
        return d,unary(j,p0,sb,cb*ap)
    cp,sp=np.cos(psi.v),np.sin(psi.v)
    val=np.zeros_like(j.v);vp=val.copy();vpp=val.copy()
    nodes,wt=m.old.disk.rule(order)
    for lo,hi in ((0.,WIDTH),(WIDTH,JOIN)):
        length=np.clip(j.v-lo,0.,hi-lo)
        z=angle(lo+length[...,None]*nodes)[0]
        c,h=np.cos(z),np.sin(z)
        f=np.hypot(h,c*sp[...,None]);den=np.maximum(f,1e-100)
        df=c*c*(sp*cp)[...,None]/den
        ddf=(c*c*(cp*cp-sp*sp)[...,None]-df*df)/den
        val+=length*(f@wt);vp+=length*(df@wt);vpp+=length*(ddf@wt)
    f=np.hypot(sb,cb*sp);den=np.maximum(f,1e-100)
    fj=sb*cb*cp*cp*ap/den
    fp=cb*cb*sp*cp/den
    return d,J(val,vp*psi.s+f*j.s,vp*psi.a+f*j.a,
        vpp*psi.s**2+2*fp*psi.s*j.s+fj*j.s**2+vp*psi.ss+f*j.ss,
        vpp*psi.s*psi.a+fp*(psi.s*j.a+psi.a*j.s)+fj*j.s*j.a+vp*psi.sa+f*j.sa,
        vpp*psi.a**2+2*fp*psi.a*j.a+fj*j.a**2+vp*psi.aa+f*j.aa)


def right_weight(u,order):
    cut,extent,half=pre.material(order,True)
    s=np.mod(u.v,2*half);low=s>half
    p=unary(u,np.where(low,2*half-s,s),np.where(low,-1.,1.),0.)
    return cap_s7((p-cut+.30)/.20)


def polar(u,gx,gz,order):
    sq=gx*gx+gz*gz;rv=np.sqrt(sq.v)
    radius=unary(sq,rv,.5/rv,-.25/rv**3)
    half=pre.material(order,True)[-1];pos=np.mod(u.v,2*half)
    a=np.where(pos<=half,1.,-1.)*np.arctan2(np.abs(gz.v),gx.v)-2*np.pi*np.floor(u.v/(2*half))
    au=(gx.v*gz.s-gz.v*gx.s)/sq.v
    av=(gx.v*gz.a-gz.v*gx.a)/sq.v
    auu=(gx.v*gz.ss-gz.v*gx.ss-au*sq.s)/sq.v
    avv=(gx.v*gz.aa-gz.v*gx.aa-av*sq.a)/sq.v
    auv=(gx.a*gz.s+gx.v*gz.sa-gz.a*gx.s-gz.v*gx.sa-au*sq.a)/sq.v
    return radius,J(a,au,av,auu,auv,avv),np.pi-np.pi*u/half


def ellipse_radius(co,si):
    aa=co*co/EX**2+si*si/EZ**2
    bb=2*OFFSET*co/EX**2
    cc=(OFFSET/EX)**2-1
    disc=bb*bb-4*cc*aa
    rt=np.sqrt(disc.v)
    sqrt=unary(disc,rt,.5/rt,-.25/rt**3)
    return (-bb+sqrt)/(2*aa)


@lru_cache(maxsize=512)
def crown_shift(theta,order,mix):
    pbase=m.terminal(order)[0]
    if theta==0.:
        return 0.
    ratio=pre.amplitude(0.,order,True)/pre.amplitude(theta,order,True)
    psi=J(np.asarray([np.arccos(np.clip(ratio,0.,1.))]))
    p=pre.height(J(np.asarray([m.END_L])),psi,order)
    return mix*(float(p.v[0])-pbase)


def cap(chart,a,b,theta,order,mix):
    side=1 if chart.endswith("+") else -1
    u,v=J(a,s=1.),J(b,a=1.)
    cx=m.section_center(order);pb,db=m.terminal(order)
    shift=crown_shift(theta,order,mix)
    if chart.startswith("cap-cartesian"):
        if np.any(((a-cx+OFFSET)/EX)**2+(b/EZ)**2>1+2e-13):
            raise ValueError("outside fixed R758 entire Cartesian ellipse")
        return u,side*(1+pb+shift+BOWL*((u-cx+OFFSET)*(u-cx+OFFSET)+v*v)),v
    w=v if chart.startswith("cap-normal") else 1-v
    if np.any((w.v<0)|(w.v>(WIDTH if chart.startswith("cap-normal") else 1.)+2e-14)):
        raise ValueError("R758 cap transverse coordinate")
    j,rho=collar_clock(w)
    psi=pre.angle_knob(u,theta,order,True,True);co,si=trig(psi)
    d,p=meridian(j,psi,order);q,n=pre.profile(u,theta,order,True)
    total=co*(db+d)
    gx=q[0]-cx-total*n[0];gz=q[1]-total*n[1]
    outer,phi,base=polar(u,gx,gz,order)
    physical=base+cap_s7((rho-.82)/.04)*(phi-base)
    ca,sa=trig(physical)
    inner=ellipse_radius(ca,sa)/RHO_CORE
    rr=rho*(inner+cap_s7((rho-.87)/.10)*(outer-inner))
    x,z=cx+rr*ca,rr*sa
    p_end=pre.height(J(np.full_like(a,m.END_L)),psi,order)
    start,_=pre.profile(u,0.,order,True)
    extra=(1-right_weight(u,order))*(FLAT_BREAK/WIDTH**2)*j*j*j*expj(.5*(start[0]+.3*start[1]))
    outer_y=p_end+p+extra
    bowl_y=pb+shift+BOWL*((x-cx+OFFSET)*(x-cx+OFFSET)+z*z)
    # Both entire geometry and all three material metric entries on the
    # common real-sized inner ellipse are independent of its phase translation.
    blend=cap_s7((rho-.82)/.16)
    return x,side*(1+bowl_y+blend*(outer_y-bowl_y)),z


def chart_jet(chart,u,v,phase=0.,order=32,markers=True,rotate=True,core_mix=.45,free_field=None):
    """Same material chart names as R756. True collar w<=.007; Cartesian core covers full ellipse.
    free_field(chart,u,v,phase,x,y,z) returns three J objects on this same material chart.
    """
    m.old.disk._public()
    a,b,ph=np.broadcast_arrays(np.asarray(u,float),np.asarray(v,float),np.asarray(phase,float))
    if np.any((ph<0)|(ph>m.ANGLE_MAX+2e-14)):
        raise ValueError("R758 phase")
    out=np.empty((ph.size,6,3))
    for theta in np.unique(ph):
        ix=ph.ravel()==theta
        aa,bb=a.ravel()[ix],b.ravel()[ix]
        if chart in ("cylinder","end+","end-"):
            x,y,z=pre.actual(chart,aa,bb,float(theta),order,markers,True,True)
        elif chart in ("cap+","cap-","cap-normal+","cap-normal-","cap-cartesian+","cap-cartesian-"):
            x,y,z=cap(chart,aa,bb,float(theta),order,float(core_mix))
        else:
            raise ValueError("unknown R758 chart "+str(chart))
        if free_field is not None:
            dx,dy,dz=free_field(chart,J(aa,s=1.),J(bb,a=1.),float(theta),x,y,z)
            x,y,z=x+dx,y+dy,z+dz
        if rotate:
            c,h=np.cos(theta),np.sin(theta);ox,oz=m.axis(order);xx,zz=x-ox,z-oz
            x,z=ox+c*xx-h*zz,oz+h*xx+c*zz
        out[ix]=gather((x,y,z),np.count_nonzero(ix))
    return out.reshape(ph.shape+(6,3))
