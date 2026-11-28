#!/usr/bin/env python3
"""R756 two fixed-length return elbows and a distinct positively preloaded exact-roll atlas.

Call chart_jet(...,biased=False) for the same-g0 returning-wall geometry.
biased=True selects the independent preloaded initial metric. With exact_roll=True
the full right wall rolls and both terminal collars have that fixed metric.
The rest of the two cap disks are explicit smooth physical continuations.
"""
from functools import lru_cache
import numpy as np
import r754_coherent_mirror_bowed_walls_two_jets as m
from r742_tilted_disk_two_jets import J,unary,trig,cap_s7,gather


PEAK=1.44
RETURN=.71
RATE=7.2
E=.0004
PRE_CUT=.63
PRE_HALF=.66
PRE_DWELL=.06


def material(order,biased):
    *_,core,half=m.constants(order)
    cut=m.LEFT_LENGTH/2+core
    if biased:
        cut-=PRE_CUT-m.Z_RIGHT
    extent=PRE_HALF if biased else m.Z_RIGHT
    return cut,extent,cut+extent


@lru_cache(maxsize=2)
def clock_spec(biased):
    segments=[]
    t=0.
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


def star_point(u,d,rho,theta,order,biased):
    q,n=profile(u,theta,order,biased)
    cx=m.section_center(order)
    gx,gz=q[0]-d*n[0]-cx,q[1]-d*n[1]
    norm=gx*gx+gz*gz
    r=np.sqrt(norm.v)
    radius=unary(norm,r,.5/r,-.25/r**3)
    rr=rho*(m.CORE+cap_s7((rho-.4)/.3)*(radius-m.CORE))
    _,_,half=material(order,biased)
    where=np.mod(u.v,2*half)
    a=np.where(where<=half,1.,-1.)*np.arctan2(np.abs(gz.v),gx.v)-2*np.pi*np.floor(u.v/(2*half))
    au=(gx.v*gz.s-gz.v*gx.s)/norm.v
    av=(gx.v*gz.a-gz.v*gx.a)/norm.v
    auu=(gx.v*gz.ss-gz.v*gx.ss-au*norm.s)/norm.v
    avv=(gx.v*gz.aa-gz.v*gx.aa-av*norm.a)/norm.v
    auv=(gx.a*gz.s+gx.v*gz.sa-gz.a*gx.s-gz.v*gx.sa-au*norm.a)/norm.v
    angle=J(a,au,av,auu,auv,avv)
    base=np.pi-np.pi*u/half
    co,si=trig(base+cap_s7((rho-.15)/.20)*(angle-base))
    return cx+rr*co,rr*si


def angle_knob(u,theta,order,biased,exact_roll):
    if not biased or not exact_roll or theta==0.:
        return J(np.zeros_like(u.v))
    ratio=amplitude(0.,order,True)/amplitude(float(theta),order,True)
    cut,extent,half=material(order,True)
    pos=np.mod(u.v,2*half);lo=pos>half
    upper=unary(u,np.where(lo,2*half-pos,pos),np.where(lo,-1.,1.),0.)
    return np.arccos(np.clip(ratio,0.,1.))*cap_s7((upper-cut+.30)/.20)


def height(v,psi,order):
    """Meridian height with the full s- and v-derivatives of its true quadrature."""
    if not np.any(psi.v):
        return m.end(v,order)[0]
    ca,sa=np.cos(psi.v),np.sin(psi.v)
    val=np.zeros_like(v.v);vp=val.copy();vpp=val.copy()
    nodes,weights=m.old.disk.rule(order)
    for lo,hi in zip((0.,m.END_E,m.END_L-m.END_E),(m.END_E,m.END_L-m.END_E,m.END_L)):
        length=np.clip(v.v-lo,0,hi-lo)
        az=m.old.disk.softened_angle(lo+length[...,None]*nodes,m.END_L,m.END_E,1/m.END_R)
        c,h=np.cos(az),np.sin(az)
        f=np.hypot(c,h*sa[...,None])
        den=np.maximum(f,1e-100)
        df=h*h*(sa*ca)[...,None]/den
        ddf=(h*h*(ca*ca-sa*sa)[...,None]-df*df)/den
        val+=length*(f@weights);vp+=length*(df@weights);vpp+=length*(ddf@weights)
    az,curv,_,_,_=m.old.turn(v.v,np.pi/2,m.END_R,m.END_E,order)
    c,h=np.cos(az),np.sin(az);f=np.hypot(c,h*sa);den=np.maximum(f,1e-100)
    fv=-h*c*ca*ca*curv/den
    fp=h*h*sa*ca/den
    # Compose P(psi,v); no s derivative differentiates the quadrature endpoints.
    return J(val,vp*psi.s+f*v.s,vp*psi.a+f*v.a,
             vpp*psi.s**2+2*fp*psi.s*v.s+fv*v.s**2+vp*psi.ss+f*v.ss,
             vpp*psi.s*psi.a+fp*(psi.s*v.a+psi.a*v.s)+fv*v.s*v.a+vp*psi.sa+f*v.sa,
             vpp*psi.a**2+2*fp*psi.a*v.a+fv*v.a**2+vp*psi.aa+f*v.aa)


def actual(chart,a,b,theta,order,marked,biased,exact_roll):
    u,v=J(a,s=1.),J(b,a=1.)
    if chart=="cylinder":
        if np.any(np.abs(b)>1+2e-14):
            raise ValueError("cylinder ordinate")
        q,n=profile(u,theta,order,biased)
        f=m.marks(u,v,order) if marked else 0.
        return q[0]+f*n[0],v,q[1]+f*n[1]
    side=1 if chart.endswith("+") else -1
    ps=angle_knob(u,theta,order,biased,exact_roll)
    co,si=trig(ps)
    if chart in ("end+","end-"):
        if np.any((b<0)|(b>m.END_L+2e-14)):
            raise ValueError("roll arclength")
        d=m.end(v,order)[1]*co;q,n=profile(u,theta,order,biased)
        return q[0]-d*n[0],side*(1+height(v,ps,order)),q[1]-d*n[1]
    if chart not in ("cap+","cap-","cap-normal+","cap-normal-","cap-cartesian+","cap-cartesian-"):
        raise ValueError("unknown R756 chart "+str(chart))
    pb,db=m.terminal(order)
    if chart.startswith("cap-cartesian"):
        if np.any((a-m.section_center(order))**2+b**2>(.15*m.CORE)**2):
            raise ValueError("outside common Cartesian cap core")
        return u,J(side*(1+pb)),v
    w=v if chart.startswith("cap-normal") else 1-v
    if np.any((w.v<0)|(w.v>(m.CAP_JOIN if chart.startswith("cap-normal") else 1.)+2e-14)):
        raise ValueError("cap material coordinate")
    d,rho=m.foliation(w,order)
    x,z=star_point(u,co*d,rho,theta,order,biased)
    endheight=height(J(np.full_like(a,m.END_L)),ps,order)
    y=pb+cap_s7((rho-.72)/.18)*(endheight-pb+(d-db)*si)
    return x,side*(1+y),z


def chart_jet(chart,u,v,phase=0.,order=32,markers=True,rotate=True,free_field=None,
              biased=False,exact_roll=True):
    """F,Fu,Fv,Fuu,Fuv,Fvv; chart coordinates are the whole R754 atlas convention.

    biased=False: same original R754 time-zero metric and period.
    biased=True: a separate preloaded reference (upper material half-period
    from material(order,True)); exact_roll=True enables both complete right
    isometric rolls and both true cap collars. Their continuation fills each disk.
    """
    m.old.disk._public()
    a,b,ph=np.broadcast_arrays(np.asarray(u,float),np.asarray(v,float),np.asarray(phase,float))
    if np.any((ph<0)|(ph>m.ANGLE_MAX+2e-14)):
        raise ValueError("R756 angle")
    out=np.empty((ph.size,6,3))
    for theta in np.unique(ph):
        ix=ph.ravel()==theta
        x,y,z=actual(chart,a.ravel()[ix],b.ravel()[ix],float(theta),order,markers,biased,exact_roll)
        if free_field is not None:
            dx,dy,dz=free_field(x,y,z,float(theta));x,y,z=x+dx,y+dy,z+dz
        if rotate:
            ox,oz=m.axis(order);xx,zz=x-ox,z-oz
            c,h=np.cos(theta),np.sin(theta);x,z=ox+c*xx-h*zz,oz+h*xx+c*zz
        out[ix]=gather((x,y,z),np.count_nonzero(ix))
    return out.reshape(a.shape+(6,3))
