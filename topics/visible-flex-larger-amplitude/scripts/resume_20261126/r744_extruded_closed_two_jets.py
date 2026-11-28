#!/usr/bin/env python3
"""R744 extruded closed C2 reference with a uniform normal tube.

Complete direct physical two-jets, ordered F, F_u, F_v, F_uu, F_uv, F_vv
in the two indicated chart coordinates. Parametrize the central cylinder
with periodic planar profile arclength u and transverse Cartesian y=v.
"""
from functools import lru_cache
import numpy as np

import r740_rolled_disk_seed as disk
from r742_tilted_disk_two_jets import J, unary, trig, cap_s7, gather


HEIGHT=.17
CENTER_X=.595
PLANAR_TURN=.15
PLANAR_BLEND=.001
END_TURN=.108
END_BLEND=.0005
END_LENGTH=END_TURN*np.pi/2+END_BLEND
CAP_NORMAL_CHART_WIDTH=.0005
ACTIVE_ANGLE_RADIUS=1.01


def turn(s,angle,r,blend,order):
    total=r*angle+blend
    alpha=disk.softened_angle(s,total,blend,1/r)
    d=np.clip(np.minimum(s,total-s)/blend,0,1)
    k=disk.s5(d)/r
    kp=30*d**2*(1-d)**2*np.where(s<total/2,1.,-1.)/(r*blend)
    ac,asi=disk.integrals(s,(0,blend,total-blend,total),
                  lambda z:disk.softened_angle(z,total,blend,1/r),order)
    return alpha,k,kp,ac,asi


@lru_cache(maxsize=None)
def profile_constants(order):
    qlen=PLANAR_TURN*np.pi/2+PLANAR_BLEND
    ulen=PLANAR_TURN*np.pi+PLANAR_BLEND
    _,_,_,lc,ls=turn(np.asarray(qlen),np.pi/2,PLANAR_TURN,PLANAR_BLEND,order)
    _,_,_,rc,rs=turn(np.asarray(ulen),np.pi,PLANAR_TURN,PLANAR_BLEND,order)
    ux,vx=disk.bent_curve(np.asarray(1.),order)
    left_h=float(HEIGHT-ls);right_h=float(HEIGHT+vx+rc)
    left_x=float(-1-lc);right_x=float(ux+rs)
    main0=left_h+qlen;main1=main0+2;rtop=main1+ulen
    return left_h,main0,main1,rtop,rtop+right_h,left_x,right_x,float(ux),float(HEIGHT+vx)


def profile_coordinates(arclength,order=32):
    """Positions, oriented tangents, outward normals and signed k, k_s."""
    disk._public()
    s=np.asarray(arclength,dtype=float)
    sh=s.shape;s=s.ravel()
    lh,m0,m1,rtop,half,lx,rx,ux,uz=profile_constants(order)
    point=np.empty((len(s),2));tt=np.empty_like(point)
    k=np.zeros(len(s));kp=np.zeros(len(s))
    phase=np.mod(s,2*half)
    low=phase>half
    z=np.where(low,2*half-phase,phase)
    wall=z<=lh
    point[wall,0]=lx;point[wall,1]=z[wall]
    tt[wall]=[0.,1.]
    left=(z>lh)&(z<=m0)
    a,kl,klp,c,sn=turn(m0-z[left],np.pi/2,PLANAR_TURN,PLANAR_BLEND,order)
    point[left,0]=-1-c;point[left,1]=HEIGHT-sn
    tt[left,0]=np.cos(a);tt[left,1]=np.sin(a)
    k[left]=kl;kp[left]=-klp
    middle=(z>m0)&(z<=m1)
    x=z[middle]-m0-1
    cu,cv=disk.bent_curve(x,order)
    angle=disk.beta(x);bend=disk.curvature(x)
    v=(x-disk.HOLD)/disk.BEND
    d=np.clip(np.minimum(v,1-v)/disk.EDGE,0,1)
    bk=(np.pi/(2*disk.BEND*(1-disk.EDGE)))*30*d**2*(1-d)**2
    bk*=np.where(v<.5,1.,-1.)/(disk.BEND*disk.EDGE)
    point[middle,0]=cu;point[middle,1]=HEIGHT+cv
    tt[middle,0]=np.cos(angle);tt[middle,1]=np.sin(angle)
    k[middle]=-bend;kp[middle]=-bk
    right=(z>m1)&(z<=rtop)
    a,kr,krp,c,sn=turn(z[right]-m1,np.pi,PLANAR_TURN,PLANAR_BLEND,order)
    point[right,0]=ux+sn;point[right,1]=uz+c
    tt[right,0]=np.sin(a);tt[right,1]=np.cos(a)
    k[right]=kr;kp[right]=krp
    wall2=z>rtop
    point[wall2,0]=rx;point[wall2,1]=half-z[wall2]
    tt[wall2]=[0.,-1.]
    point[low,1]*=-1;tt[low,0]*=-1;kp[low]*=-1
    nn=np.column_stack((-tt[:,1],tt[:,0]))
    return (point.reshape(sh+(2,)),tt.reshape(sh+(2,)),nn.reshape(sh+(2,)),
            k.reshape(sh),kp.reshape(sh))


def profile(u,order):
    pt,T,n,k,kp=profile_coordinates(u.v,order)
    q=[unary(u,pt[:,i],T[:,i],-k*n[:,i]) for i in range(2)]
    normal=[unary(u,n[:,i],k*T[:,i],kp*T[:,i]-k*k*n[:,i]) for i in range(2)]
    return q,normal


def end_offsets(v,order):
    a,k,_,p,d=turn(v.v,np.pi/2,END_TURN,END_BLEND,order)
    return unary(v,p,np.cos(a),-k*np.sin(a)),unary(v,d,np.sin(a),k*np.cos(a))


@lru_cache(maxsize=None)
def end_limits(order):
    a,k,kp,p,d=turn(np.asarray(END_LENGTH),np.pi/2,END_TURN,END_BLEND,order)
    return float(p),float(d)


def slice_j(j,mask):
    return J(*(v[mask] if np.ndim(v) else v for v in j.parts()))


def apply_phase_chart(u,y,phase,order):
    """Smooth disk rotation in the two large flat charts, identity elsewhere."""
    lh,m0,m1,rtop,half,*_=profile_constants(order)
    s=np.mod(u.v,2*half)
    low=s>half
    # These local arclength coordinates extend at least .01 into all four joins.
    sign=np.where(low,-1.,1.)
    x=J(np.where(low,2*half-s,s)-m0-1,
        *(sign*q for q in u.parts()[1:]))
    r2=x*x+y*y
    # The weight is constant near r=0; avoid differentiating sqrt there.
    radius=np.sqrt(np.maximum(.25,r2.v))
    live=r2.v>.25
    r=unary(r2,radius,np.where(live,.5/radius,0.),
                     np.where(live,-.25/radius**3,0.))
    weight=1-cap_s7((r-1)/(ACTIVE_ANGLE_RADIUS-1))
    cc,ss=trig(weight*phase)
    xx=x*cc+y*ss
    yy=-x*ss+y*cc
    # Lift periodic profile arclength continuously near dividers where weight=0.
    su=u+(xx-x)*sign
    return su,yy,x,r2,low



def sine_window(t):
    inside=(t.v>0)&(t.v<1)
    p=np.pi*np.clip(t.v,0,1)
    sn=np.sin(p);cs=np.cos(p)
    return unary(t,np.where(inside,sn**4,0),
              np.where(inside,4*np.pi*sn**3*cs,0),
              np.where(inside,4*np.pi**2*(3*sn**2*cs**2-sn**4),0))


def gap_height(u,y,amplitude,order):
    """Actual normal displacement on an interior constant-curvature upper/right turn."""
    _,_,m1,_,half,*_=profile_constants(order)
    sigma=np.mod(u.v,2*half)
    low=sigma>half
    sign=np.where(low,-1.,1.)
    pos=J(np.where(low,2*half-sigma,sigma),*(sign*v for v in u.parts()[1:]))
    start=m1+PLANAR_TURN*np.pi/3+PLANAR_BLEND/2
    a=sine_window((pos-start)/(PLANAR_TURN*np.pi/3))
    g=1-4*y*y
    z=np.maximum(g.v,0)
    fourth=unary(g,z**4,4*z**3,12*z*z)
    return amplitude*a*y*y*fourth


def deformed_cylinder_jet(s,y,normal_data,order=32):
    """Base physical free graph. normal_data has (...,6) for f and its derivatives.

    At closed joins and fixed disks use a genuine supported correction.
    This open-chart function deliberately does not change the other charts.
    """
    disk._public()
    aa,bb=np.broadcast_arrays(np.asarray(s,dtype=float),np.asarray(y,dtype=float))
    vals=np.broadcast_to(np.asarray(normal_data,dtype=float),aa.shape+(6,)).reshape(-1,6)
    u=J(aa.ravel(),s=1.);v=J(bb.ravel(),a=1.)
    q,n=profile(u,order)
    f=J(*vals.T)
    return gather((q[0]+f*n[0],v,q[1]+f*n[1]),len(u.v)).reshape(aa.shape+(6,3))

def s_and_y(u,y,order,gap_amplitude=0.):
    """Same material chart through |y|=1, using outward shoulder arclength."""
    q,n=profile(u,order)
    ext=np.abs(y.v)>1
    # Tangent and first two jets of the straight transverse extension agree
    # at zero because the turn starts with zero curvature.
    sg=np.where(y.v<0,-1.,1.)
    v=y*sg-1
    v=J(np.maximum(v.v,0),*(np.where(ext,w,0.) for w in v.parts()[1:]))
    p,d=end_offsets(v,order)
    yy=y+sg*(p-v)
    shift=gap_height(u,y,gap_amplitude,order)-d if gap_amplitude else -d
    return q[0]+shift*n[0],yy,q[1]+shift*n[1]


def active_chart(chart,u,v,phase,order,markers,gap_amplitude):
    """Central cylinder or one true turned cap shoulder."""
    if chart=="cylinder":
        ym=v
    else:
        ym=(1+v)*(1 if chart=="end+" else -1)
    su,yy,x,r2,lower=apply_phase_chart(u,ym,phase,order)
    X,Y,Z=s_and_y(su,yy,order,gap_amplitude)
    cp=np.cos(phase);sp=np.sin(phase)
    X,Y=X*cp-Y*sp,X*sp+Y*cp
    if markers:
        for cx,cy,rad in disk.MARKERS:
            dx=x-cx;dy=ym-cy;z=1-(dx*dx+dy*dy)/(rad*rad)
            h=np.where(~lower,np.maximum(z.v,0),0.)
            Z+=unary(z,1e-4*rad**2*h**3,3e-4*rad**2*h**2,6e-4*rad**2*h)
    return X,Y,Z


def chart_jet(chart,u,v,phase=0.,order=32,markers=True,gap_amplitude=0.):
    """All physical 2-jets; chart names and coordinate order are in R744.

    cylinder: u=periodic profile arclength, v=y in [-1,1].
    end+/end-: same u, v=outward rolling arclength in [0,END_LENGTH].
    cap+/cap-: same u, v=star radius fraction in [0,1] (singular only at its polar origin).
    cap-normal+/cap-normal-: same u, v=extra inward planar offset at the common rim.
    """
    disk._public()
    a,b,ph=np.broadcast_arrays(np.asarray(u,dtype=float),np.asarray(v,dtype=float),
                               np.asarray(phase,dtype=float))
    sh=a.shape;u=J(a.ravel(),s=1.);v=J(b.ravel(),a=1.);ph=ph.ravel()
    if chart=="cylinder" or chart in ("end+","end-"):
        if chart=="cylinder" and np.any(np.abs(v.v)>1+2e-14):
            raise ValueError("cylinder transverse coordinate")
        if chart!="cylinder" and np.any((v.v<0)|(v.v>END_LENGTH+2e-14)):
            raise ValueError("turned end arclength")
        points=active_chart(chart,u,v,ph,order,markers,gap_amplitude)
    elif chart in ("cap+","cap-","cap-normal+","cap-normal-"):
        p,d=end_limits(order);sg=1 if chart.endswith("+") else -1
        q,n=profile(u,order)
        if chart.startswith("cap-normal"):
            if np.any((v.v<0)|(v.v>CAP_NORMAL_CHART_WIDTH+2e-14)):
                raise ValueError("planar collar coordinate")
            X=q[0]-(d+v)*n[0];Z=q[1]-(d+v)*n[1]
        else:
            if np.any((v.v<0)|(v.v>1+2e-14)):
                raise ValueError("flat cap radial fraction")
            X=CENTER_X+v*(q[0]-d*n[0]-CENTER_X)
            Z=v*(q[1]-d*n[1])
        Y=J(sg*(1+p))
        cp=np.cos(ph);sp=np.sin(ph)
        points=X*cp-Y*sp,X*sp+Y*cp,Z
    else:
        raise ValueError("unknown R744 chart "+str(chart))
    return gather(points,len(u.v)).reshape(sh+(6,3))


def disk_jet(radius,theta,phase=0.,side=1,order=32,markers=True):
    """The two actual unit disks; their polar derivatives are returned."""
    from r742_tilted_disk_two_jets import HORIZONTAL, disk_jet as genuine_disk
    return genuine_disk(radius,theta,design=HORIZONTAL,phase=phase,side=side,
                        order=order,markers=markers)


def cap_cartesian(x,z,side=1,phase=0.):
    """Regular plane chart (including cap center), restricted to the filled star domain."""
    disk._public()
    xx,zz,ph=np.broadcast_arrays(np.asarray(x,dtype=float),np.asarray(z,dtype=float),
                                 np.asarray(phase,dtype=float))
    sh=xx.shape;x=J(xx.ravel(),s=1.);z=J(zz.ravel(),a=1.)
    p,_=end_limits(32)
    y=J(side*(1+p))
    c=np.cos(ph.ravel());s=np.sin(ph.ravel())
    return gather((x*c-y*s,x*s+y*c,z),len(x.v)).reshape(sh+(6,3))
