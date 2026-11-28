#!/usr/bin/env python3
"""R754 coherent upper/lower axial motion with two fixed-length closing walls.

Full physical two-jets on a common closed material cylinder/end/cap atlas.
Use theta in [0,.90] (new reference and range, independent of R746/751).
"""
from functools import lru_cache
import numpy as np
import r744_extruded_closed_two_jets as old
from r742_tilted_disk_two_jets import J, unary, trig, cap_s7, gather


HEIGHT=.71
ANGLE_MAX=.90
SHIFT_MAX=.135
Z_LEFT=.41
Z_RIGHT=.60
LEFT_LENGTH=2*(Z_LEFT+SHIFT_MAX)
RIGHT_LENGTH=2*Z_RIGHT
CLOCK_EDGE=.01
END_R=.132
END_E=.0005
END_L=END_R*np.pi/2+END_E
CAP_JOIN=.001
CAP_RAMP=.001
CAP_EXTRA=CAP_JOIN+CAP_RAMP/2
CORE=.003
MARKS=((.25,0.,.002),(.55,0.,.003),(.85,0.,.004),(.55,.33,.005))


@lru_cache(maxsize=32)
def constants(order):
    lh,m0,m1,rtop,old_half,xl,xr,ux,uz=old.profile_constants(order)
    left_top=lh+HEIGHT-old.HEIGHT
    right_top=old_half-rtop+HEIGHT-old.HEIGHT
    start=left_top-Z_LEFT
    stop=start+rtop-lh
    core_len=stop+right_top-Z_RIGHT
    half=LEFT_LENGTH/2+core_len+RIGHT_LENGTH/2
    return lh,m0,m1,rtop,xl,xr,ux,uz+HEIGHT-old.HEIGHT,start,stop,core_len,half


def clock(t):
    """Symmetric normalized monotone clock with zero derivative at both full-wall ends."""
    e=CLOCK_EDGE
    w=old.disk.softened_angle(t,1.,e,1/(1-e))
    z=np.clip(np.minimum(t,1-t)/e,0,1)
    d=old.disk.s5(z)/(1-e)
    dd=30*z*z*(1-z)**2*np.where(t<.5,1.,-1.)/(e*(1-e))
    return w,d,dd


def wall_angle(a,length,amp):
    w,wp,wpp=clock(a/length)
    ang=2*np.pi*w
    d=2*np.pi*wp/length
    dd=2*np.pi*wpp/length**2
    return amp*np.sin(ang),amp*np.cos(ang)*d,amp*(np.cos(ang)*dd-np.sin(ang)*d*d)


def wall_integrals(a,length,amp,order):
    return old.disk.integrals(a,(0.,CLOCK_EDGE*length,length/2),
                             lambda z:wall_angle(z,length,amp)[0],order)


@lru_cache(maxsize=512)
def wall_amplitude(length,height,order):
    if abs(height-length/2)<4e-16:
        return 0.
    lo,hi=0.,1.2
    for _ in range(56):
        m=(lo+hi)/2
        vertical,_=wall_integrals(np.asarray(length/2),length,m,order)
        if vertical>height:
            lo=m
        else:
            hi=m
    return (lo+hi)/2


def profile_data(s,theta,order,rigid_left=False):
    old.disk._public()
    lh,m0,m1,rtop,xl,xr,ux,uz,start,stop,core_len,half=constants(order)
    shift=old.PLANAR_TURN*theta
    pos=np.mod(s,2*half)
    lower=pos>half
    u=np.where(lower,2*half-pos,pos)
    left=u<LEFT_LENGTH/2
    right=u>LEFT_LENGTH/2+core_len
    middle=~(left|right)
    q=np.zeros(u.shape+(2,));T=np.zeros_like(q);k=np.zeros_like(u);kp=np.zeros_like(u)
    for mask,length,height,xx,side in ((left,LEFT_LENGTH,Z_LEFT if rigid_left else Z_LEFT+shift,xl+shift if rigid_left else xl,-1.),
                                      (right,RIGHT_LENGTH,Z_RIGHT-shift,xr,1.)):
        a=LEFT_LENGTH/2-u[mask] if side==-1. else u[mask]-LEFT_LENGTH/2-core_len
        amp=wall_amplitude(length,float(height),order)
        az,azp,azpp=wall_angle(a,length,amp)
        vertical,horizontal=wall_integrals(a,length,amp,order)
        q[mask,0]=xx+side*horizontal;q[mask,1]=height-vertical
        T[mask,0]=np.sin(az);T[mask,1]=-side*np.cos(az)
        k[mask]=-azp;kp[mask]=-side*azpp
    coordinate=u[middle]-LEFT_LENGTH/2
    translate=(coordinate<=start+m0-lh+.5) if rigid_left else np.zeros_like(coordinate,dtype=bool)
    z=coordinate+np.where(translate,0.,shift)
    t=lh+np.clip(z-start,0,rtop-lh)
    old_q,old_t,old_n,ko,kpo=old.profile_coordinates(t,order)
    old_q[...,1]+=HEIGHT-old.HEIGHT
    low=z<start;high=z>stop
    old_q[low,0]=xl;old_q[low,1]=Z_LEFT+z[low]
    old_q[high,0]=xr;old_q[high,1]=Z_RIGHT+core_len-z[high]
    old_t[low]=[0.,1.];old_t[high]=[0.,-1.]
    ko[low|high]=0.;kpo[low|high]=0.
    old_q[translate,0]+=shift
    q[middle]=old_q;T[middle]=old_t;k[middle]=ko;kp[middle]=kpo
    q[lower,1]*=-1;T[lower,0]*=-1;kp[lower]*=-1
    n=np.stack((-T[...,1],T[...,0]),axis=-1)
    return q,T,n,k,kp


def profile(u,theta,order,rigid_left=False):
    ss,ix=np.unique(u.v,return_inverse=True)
    q,T,n,k,kp=(a[ix] for a in profile_data(ss,theta,order,rigid_left))
    return ([unary(u,q[:,i],T[:,i],-k*n[:,i]) for i in range(2)],
            [unary(u,n[:,i],k*T[:,i],kp*T[:,i]-k*k*n[:,i]) for i in range(2)])


@lru_cache(maxsize=64)
def axis(order):
    lh,m0,m1,rtop,xl,xr,ux,uz,start,stop,core_len,half=constants(order)
    old_q,t,n,_,_=old.profile_coordinates(np.asarray(m1+.1),order)
    p=old_q-old.PLANAR_TURN*n
    return float(p[0]),float(p[1]+HEIGHT-old.HEIGHT)


def grip_s(alpha,order):
    lh,m0,m1,rtop,xl,xr,ux,uz,start,*_=constants(order)
    return LEFT_LENGTH/2+start+m1-lh+old.PLANAR_BLEND/2+old.PLANAR_TURN*alpha


def section_center(order):
    return constants(order)[6]+old.PLANAR_TURN


def end(v,order):
    ang,k,_,p,d=old.turn(v.v,np.pi/2,END_R,END_E,order)
    return unary(v,p,np.cos(ang),-k*np.sin(ang)),unary(v,d,np.sin(ang),k*np.cos(ang))


@lru_cache(maxsize=32)
def terminal(order):
    p,d=end(J(np.asarray([END_L])),order)
    return float(p.v[0]),float(d.v[0])


def foliation(w,order):
    z=np.clip((w.v-CAP_JOIN)/CAP_RAMP,0,1)
    clock=np.where(w.v<CAP_JOIN,w.v,CAP_JOIN+CAP_RAMP*(z-2.5*z**4+3*z**5-z**6))
    j=unary(w,clock,1-old.disk.s5(z),-30*z*z*(1-z)**2/CAP_RAMP)
    p,db=terminal(order)
    return db+j,1-(w-j)/(1-CAP_EXTRA)


def star_point(u,d,rho,theta,order,rigid_left=False):
    q,n=profile(u,theta,order,rigid_left)
    cx=section_center(order)
    gx,gz=q[0]-d*n[0]-cx,q[1]-d*n[1]
    norm=gx*gx+gz*gz
    r=np.sqrt(norm.v)
    radius=unary(norm,r,.5/r,-.25/r**3)
    rr=rho*(CORE+cap_s7((rho-.4)/.3)*(radius-CORE))
    half=constants(order)[-1]
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


def marks(u,y,order):
    q,_=profile(u,0.,order)
    active=(u.v%(2*constants(order)[-1])>=grip_s(.10,order))&(u.v%(2*constants(order)[-1])<=grip_s(1.05,order))
    value=J(np.zeros_like(u.v))
    for alpha,y0,rad in MARKS:
        p=profile_data(np.asarray([grip_s(alpha,order)]),0.,order)[0][0]
        dx,dz=q[0]-p[0],q[1]-p[1]
        h=1-(dx*dx+dz*dz+(y-y0)*(y-y0))/rad**2
        z=np.where(active,np.maximum(h.v,0.),0.)
        coeff=1e-5*rad**2
        value+=unary(h,coeff*z**3,3*coeff*z*z,6*coeff*z)
    return value


def actual(chart,aa,bb,theta,order,marked,rigid_left=False):
    u,v=J(aa,s=1.),J(bb,a=1.)
    if chart=="cylinder":
        if np.any(np.abs(bb)>1+2e-14):
            raise ValueError("cylinder ordinate")
        q,n=profile(u,theta,order,rigid_left)
        f=marks(u,v,order) if marked else 0.
        return q[0]+f*n[0],v,q[1]+f*n[1]
    if chart in ("end+","end-"):
        if np.any((bb<0)|(bb>END_L+2e-14)):
            raise ValueError("rolled arclength")
        p,d=end(v,order);q,n=profile(u,theta,order,rigid_left)
        return q[0]-d*n[0],(1 if chart.endswith("+") else -1)*(1+p),q[1]-d*n[1]
    if chart not in ("cap+","cap-","cap-normal+","cap-normal-","cap-cartesian+","cap-cartesian-"):
        raise ValueError("unknown R754 chart "+str(chart))
    side=1 if chart.endswith("+") else -1
    p,_=terminal(order)
    if chart.startswith("cap-cartesian"):
        if np.any((aa-section_center(order))**2+bb**2>(.15*CORE)**2):
            raise ValueError("outside common Cartesian cap core")
        return u,J(side*(1+p)),v
    w=v if chart.startswith("cap-normal") else 1-v
    if np.any((w.v<0)|(w.v>(CAP_JOIN if chart.startswith("cap-normal") else 1.)+2e-14)):
        raise ValueError("cap material coordinate")
    d,rho=foliation(w,order)
    x,z=star_point(u,d,rho,theta,order,rigid_left)
    return x,J(side*(1+p)),z


def chart_jet(chart,u,v,phase=0.,order=32,markers=True,rotate=True,free_field=None,rigid_left=False):
    """F,Fu,Fv,Fuu,Fuv,Fvv on a full closed material atlas.

    cylinder u=periodic s,v=y; end± u=s,v=outward arclength; cap± u=s,
    v=1-w (rim at 1); cap-normal± u=s,v=w until .001; cap-cartesian±
    u=x,v=z in the common core. free_field returns three additional J
    coordinates in the pre-rotation frame. rigid_left=True keeps the entire
    original left wing under the coherent physical translation, retaining
    exactly the same initial surface as the two-moving-wall reference.
    """
    old.disk._public()
    a,b,t=np.broadcast_arrays(np.asarray(u,float),np.asarray(v,float),np.asarray(phase,float))
    if np.any((t<0)|(t>ANGLE_MAX+2e-14)):
        raise ValueError("R754 physical angle")
    out=np.empty((t.size,6,3))
    for theta in np.unique(t):
        selected=t.ravel()==theta
        x,y,z=actual(chart,a.ravel()[selected],b.ravel()[selected],float(theta),order,markers,rigid_left)
        if free_field is not None:
            dx,dy,dz=free_field(x,y,z,float(theta));x,y,z=x+dx,y+dy,z+dz
        if rotate:
            ox,oz=axis(order)
            co,si=np.cos(theta),np.sin(theta);xx,zz=x-ox,z-oz
            x,z=ox+co*xx-si*zz,oz+si*xx+co*zz
        out[selected]=gather((x,y,z),np.count_nonzero(selected))
    return out.reshape(a.shape+(6,3))


def flat_material_s(x,upper=True,order=32):
    """True initially horizontal main-disk x label, before either coherent shift."""
    lh,m0,m1,rtop,xl,xr,ux,uz,start,stop,core_len,half=constants(order)
    top=LEFT_LENGTH/2+start+m0-lh+1+np.asarray(x)
    return top if upper else 2*half-top
