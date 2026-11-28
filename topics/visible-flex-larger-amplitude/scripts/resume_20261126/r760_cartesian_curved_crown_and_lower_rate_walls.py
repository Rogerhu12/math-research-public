#!/usr/bin/env python3
"""R760 physically spaced curved caps, a level elliptical boundary, and a lower-curvature right wall."""
from functools import lru_cache
import numpy as np
import r754_coherent_mirror_bowed_walls_two_jets as m
from r742_tilted_disk_two_jets import J,unary,trig,cap_s7,gather
from r756_return_elbows_preloaded_exact_rolls import height as roll_height
from r758_curved_outer_collars_and_fixed_elliptical_crowns import collar_clock,expj

WIDTH=.007
ROUND=.001
JOIN=WIDTH+ROUND/2
RHO_CORE=.82
EX=.494
EZ=.22
OFFSET=.49
BOWL=.000025
CART_CUT=.014
H_RIM=.0000015
FLAT_BREAK=1e-9

PEAK=1.44
RETURN=.71
RATE=5.4
E=.0004
PRE_CUT=.92
PRE_HALF=.95
PRE_DWELL=.06


def material(order,biased=True):
    if not biased:
        raise ValueError('R760 uses only its new fixed preloaded section')
    *_,core,half=m.constants(order)
    cut=m.LEFT_LENGTH/2+core
    if biased:
        cut-=PRE_CUT-m.Z_RIGHT
    extent=PRE_HALF if biased else m.Z_RIGHT
    return cut,extent,cut+extent


@lru_cache(maxsize=2)
def clock_spec(biased):
    segments=[]
    t=PRE_HALF-2*(PEAK+RETURN)/RATE-4*E-PRE_DWELL-.001
    for ang,sign in ((PEAK,1.),(PEAK,-1.),(RETURN,-1.),(RETURN,1.)):
        span=ang/RATE+E
        segments.append((t,span,sign));t+=span
        if len(segments)==1 and biased:
            t+=PRE_DWELL
    extent=PRE_HALF if biased else m.Z_RIGHT
    cuts=sorted(set([0.,extent]+[z for t,h,_ in segments for z in (t,t+E,t+h-E,t+h)]))
    return segments,tuple(cuts)


def heading(a,biased):
    a=np.asarray(a)
    az=np.zeros_like(a,dtype=float);ap=az.copy();app=az.copy()
    for t,h,sign in clock_spec(biased)[0]:
        z=a-t
        az+=sign*m.old.disk.softened_angle(z,h,E,RATE)
        piece=np.clip(np.minimum(z,h-z)/E,0.,1.)
        ap+=sign*RATE*m.old.disk.s5(piece)
        app+=sign*RATE*30*piece**2*(1-piece)**2*np.where(z<h/2,1.,-1.)/E
    return az,ap,app


def integral(a,lam,order,biased):
    return m.old.disk.integrals(a,clock_spec(biased)[1],
                                lambda x:lam*heading(x,biased)[0],order)


@lru_cache(maxsize=1024)
def amplitude(theta,order,biased):
    if not biased and theta==0.:
        return 0.
    initial=PRE_CUT if biased else m.Z_RIGHT
    extent=PRE_HALF if biased else m.Z_RIGHT
    target=initial-m.old.PLANAR_TURN*theta
    lo,hi=0.,1.
    for _ in range(56):
        mid=(lo+hi)/2
        c,_=integral(np.asarray(extent),mid,order,biased)
        if c>target:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2


def data(s,theta,order,biased):
    cut,extent,half=material(order,biased)
    s=np.asarray(s);p=np.mod(s,2*half);low=p>half;u=np.where(low,2*half-p,p)
    right=u>=cut
    q=np.zeros(s.shape+(2,));t=np.zeros_like(q);k=np.zeros_like(s,dtype=float);kp=k.copy()
    if np.any(~right):
        q[~right],t[~right],_,k[~right],kp[~right]=m.profile_data(u[~right],theta,order,True)
    if np.any(right):
        a=u[right]-cut;lam=amplitude(float(theta),order,biased)
        zc=PRE_CUT if biased else m.Z_RIGHT
        azi,ap,app=heading(a,biased);angle=lam*azi
        ve,ho=integral(a,lam,order,biased)
        q[right,0]=m.constants(order)[5]+ho;q[right,1]=zc-m.old.PLANAR_TURN*theta-ve
        t[right,0]=np.sin(angle);t[right,1]=-np.cos(angle)
        k[right]=-lam*ap;kp[right]=-lam*app
    q[low,1]*=-1;t[low,0]*=-1;kp[low]*=-1
    n=np.stack((-t[...,1],t[...,0]),axis=-1)
    return q,t,n,k,kp


def profile(u,theta,order,biased):
    ss,ix=np.unique(u.v,return_inverse=True)
    q,t,n,k,kp=(x[ix] for x in data(ss,theta,order,biased))
    return ([unary(u,q[:,i],t[:,i],-k*n[:,i]) for i in range(2)],
            [unary(u,n[:,i],k*t[:,i],kp*t[:,i]-k*k*n[:,i]) for i in range(2)])


def right_weight(u,order):
    cut,extent,half=material(order,True)
    s=np.mod(u.v,2*half);low=s>half
    p=unary(u,np.where(low,2*half-s,s),np.where(low,-1.,1.),0.)
    return cap_s7((p-cut+.30)/.20)


def polar(u,gx,gz,order):
    sq=gx*gx+gz*gz;rv=np.sqrt(sq.v)
    radius=unary(sq,rv,.5/rv,-.25/rv**3)
    half=material(order,True)[-1];pos=np.mod(u.v,2*half)
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


def angle_knob(u,theta,order,biased,exact_roll):
    if not biased or not exact_roll or theta==0.:
        return J(np.zeros_like(u.v))
    ratio=amplitude(0.,order,True)/amplitude(float(theta),order,True)
    cut,extent,half=material(order,True)
    pos=np.mod(u.v,2*half);lo=pos>half
    upper=unary(u,np.where(lo,2*half-pos,pos),np.where(lo,-1.,1.),0.)
    return np.arccos(np.clip(ratio,0.,1.))*cap_s7((upper-cut+.30)/.20)


@lru_cache(maxsize=512)
def crown_shift(theta,order,mix):
    pbase=m.terminal(order)[0]
    if theta==0.:
        return 0.
    ratio=amplitude(0.,order,True)/amplitude(theta,order,True)
    psi=J(np.asarray([np.arccos(np.clip(ratio,0.,1.))]))
    p=roll_height(J(np.asarray([m.END_L])),psi,order)
    return mix*(float(p.v[0])-pbase)



def collar_speed(w):
    t=np.clip(w/WIDTH,0.,1.);a=t*(1-t)
    return H_RIM*140*a**3/WIDTH,H_RIM*420*a*a*(1-2*t)/WIDTH**2


def collar_height(j,psi,order):
    if not np.any(psi.v):
        return H_RIM*cap_s7(j/WIDTH)
    sn,cs=np.sin(psi.v),np.cos(psi.v)
    val=np.zeros_like(j.v);v1=val.copy();v2=val.copy()
    nodes,weights=m.old.disk.rule(order)
    for lo,hi in ((0.,WIDTH),(WIDTH,JOIN)):
        dz=np.clip(j.v-lo,0.,hi-lo)
        h,_=collar_speed(lo+dz[...,None]*nodes)
        f=np.hypot(h,sn[...,None]);den=np.maximum(f,1e-100)
        fp=(sn*cs)[...,None]/den
        fpp=((cs*cs-sn*sn)[...,None]-fp*fp)/den
        val+=dz*(f@weights);v1+=dz*(fp@weights);v2+=dz*(fpp@weights)
    h,hp=collar_speed(j.v);f=np.hypot(h,sn);den=np.maximum(f,1e-100)
    fj=h*hp/den;fp=sn*cs/den
    return J(val,v1*psi.s+f*j.s,v1*psi.a+f*j.a,
         v2*psi.s**2+2*fp*psi.s*j.s+fj*j.s**2+v1*psi.ss+f*j.ss,
         v2*psi.s*psi.a+fp*(psi.s*j.a+psi.a*j.s)+fj*j.s*j.a+v1*psi.sa+f*j.sa,
         v2*psi.a**2+2*fp*psi.a*j.a+fj*j.a**2+v1*psi.aa+f*j.aa)


def bowl_h(x,z,cx):
    u=(x-cx+OFFSET)/EX;v=z/EZ
    q=u*u+v*v-1
    return BOWL*q*(1-cap_s7(q/CART_CUT))


def bump(x):
    t=unary(x,np.clip(x.v,0.,1.),((x.v>0)&(x.v<1)).astype(float),0.)
    q=t*(1-t)
    return q*q*q


def cap(chart,a,b,theta,order,mix):
    side=1 if chart.endswith("+") else -1
    u,v=J(a,s=1.),J(b,a=1.)
    cx=m.section_center(order);pb,db=m.terminal(order)
    shift=crown_shift(theta,order,mix)
    if chart.startswith("cap-cartesian"):
        if np.any(((a-cx+OFFSET)/EX)**2+(b/EZ)**2>1+2e-13):
            raise ValueError("outside regular R760 inner ellipse")
        return u,side*(1+pb+H_RIM+shift+bowl_h(u,v,cx)),v
    w=v if chart.startswith("cap-normal") else 1-v
    if np.any((w.v<0)|(w.v>(WIDTH if chart.startswith("cap-normal") else 1.)+2e-14)):
        raise ValueError("R760 cap coordinate")
    j,rho=collar_clock(w)
    ps=angle_knob(u,theta,order,True,True);co,si=trig(ps)
    q,n=profile(u,theta,order,True);d=co*(db+j)
    gx=q[0]-cx-d*n[0];gz=q[1]-d*n[1]
    outer,phi,_=polar(u,gx,gz,order)
    start,n0=profile(u,0.,order,True)
    _,base,_=polar(u,start[0]-cx-(db+JOIN)*n0[0],start[1]-(db+JOIN)*n0[1],order)
    ph=base+cap_s7((rho-.82)/.04)*(phi-base)
    cs,sn=trig(ph);inner=ellipse_radius(cs,sn)/RHO_CORE
    rr=rho*(inner+cap_s7((rho-.87)/.10)*(outer-inner))
    x,z=cx+rr*cs,rr*sn
    true_inner=ellipse_radius(*trig(phi))/RHO_CORE
    # The denominator is bounded away from zero by the strict enclosing box;
    # where the angle map has not yet reached phi the numerator is nonpositive.
    price=(rr-.87*inner)/(outer-.87*true_inner)
    physical_blend=cap_s7(price/.80)
    rise=collar_height(j,ps,order)
    extra=(1-right_weight(u,order))*FLAT_BREAK*bump(j/WIDTH)*expj(.5*(start[0]+.3*start[1]))
    outside=roll_height(J(np.full_like(a,m.END_L)),ps,order)+rise+extra
    # Continue the actual incoming normal slope during the physical radial join.
    outside=outside-(si/co)*(n[0]*(x-cx-gx)+n[1]*(z-gz))
    h=pb+H_RIM+bowl_h(x,z,cx)+(1-physical_blend)*shift+physical_blend*(outside-pb-H_RIM)
    return x,side*(1+h),z


def chart_jet(chart,u,v,phase=0.,order=32,markers=True,rotate=True,core_mix=.45,free_field=None):
    """Original R760 nine-chart two-jets in the same coordinate convention as R758."""
    m.old.disk._public()
    a,b,ph=np.broadcast_arrays(np.asarray(u,float),np.asarray(v,float),np.asarray(phase,float))
    if np.any((ph<0)|(ph>m.ANGLE_MAX+2e-14)):
        raise ValueError("R760 phase")
    out=np.empty((ph.size,6,3))
    for theta in np.unique(ph):
        ix=ph.ravel()==theta
        aa,bb=a.ravel()[ix],b.ravel()[ix]
        uj,vj=J(aa,s=1.),J(bb,a=1.)
        if chart=="cylinder":
            if np.any(np.abs(bb)>1+2e-14):
                raise ValueError("cylinder ordinate")
            q,n=profile(uj,float(theta),order,True)
            f=m.marks(uj,vj,order) if markers else 0.
            x,y,z=q[0]+f*n[0],vj,q[1]+f*n[1]
        elif chart in ("end+","end-"):
            if np.any((bb<0)|(bb>m.END_L+2e-14)):
                raise ValueError("rolled arclength")
            ps=angle_knob(uj,float(theta),order,True,True);co,_=trig(ps)
            q,n=profile(uj,float(theta),order,True);d=m.end(vj,order)[1]*co
            x,z=q[0]-d*n[0],q[1]-d*n[1]
            y=(1 if chart.endswith("+") else -1)*(1+roll_height(vj,ps,order))
        elif chart in ("cap+","cap-","cap-normal+","cap-normal-","cap-cartesian+","cap-cartesian-"):
            x,y,z=cap(chart,aa,bb,float(theta),order,float(core_mix))
        else:
            raise ValueError("unknown R760 chart "+str(chart))
        if free_field is not None:
            dx,dy,dz=free_field(chart,uj,vj,float(theta),x,y,z);x,y,z=x+dx,y+dy,z+dz
        if rotate:
            c,h=np.cos(theta),np.sin(theta);ox,oz=m.axis(order);xx,zz=x-ox,z-oz
            x,z=ox+c*xx-h*zz,oz+h*xx+c*zz
        out[ix]=gather((x,y,z),np.count_nonzero(ix))
    return out.reshape(ph.shape+(6,3))
