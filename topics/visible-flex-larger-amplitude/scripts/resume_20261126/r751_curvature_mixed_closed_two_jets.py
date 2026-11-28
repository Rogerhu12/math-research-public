#!/usr/bin/env python3
"""R751 true closed curvature-mixed unit-speed section and full rolled/capped two-jet.

One rotating source section is constructed per scalar physical phase.
Both complete ends and their nonplanar cap collars are included. Material target
is the genuine original roll at phase zero in the same cap coordinates.
"""
from functools import lru_cache
import numpy as np

import r744_extruded_closed_two_jets as old
import r746_axial_translation_closed_two_jets as axial
import r747_offset_arclength_closed_two_jets as angular
from r742_tilted_disk_two_jets import J, unary, gather


ETA = 1.e-12
C_MAX = 1.00001
PLATEAU = .00015
BOOST_WIDTH = .00018
CAP_STRAIGHT = .0001
CAP_TURN = .0012
FLATTEN = .0001
CAP_CLOCK_LIMIT = CAP_TURN + FLATTEN/2
CORE_RADIUS = .0001


def phase_weight(theta):
    return old.disk.s7(np.clip((theta-.8)/.2,0,1))


def offsets(order):
    lh,m0,m1,top,half,*_ = old.profile_constants(order)
    h,b,e = old.disk.HOLD,old.disk.BEND,old.disk.EDGE*old.disk.BEND
    bends = (m0+1+h,m0+1+h+e,m0+1+h+b-e,m0+1+h+b)
    upper = (0.,lh,lh+old.PLANAR_BLEND,m0-old.PLANAR_BLEND,m0,*bends,
             m1,m1+old.PLANAR_BLEND,top-old.PLANAR_BLEND,top,half)
    return 2*half, np.asarray((*upper,*(2*half-x for x in upper[-2::-1]))), m0,m1,top


def bump(s,a,length):
    t = (s-a)/length
    live = (t>0)&(t<1)
    sn = np.sin(np.pi*np.clip(t,0,1));cs = np.cos(np.pi*np.clip(t,0,1))
    gain = np.pi/length
    return (np.where(live,sn**4,0.),np.where(live,4*gain*sn**3*cs,0.),
            np.where(live,4*gain**2*(3*sn**2*cs**2-sn**4),0.))


def tail_integrand(t):
    z = np.clip((t-PLATEAU)/(BOOST_WIDTH-PLATEAU),0,1)
    retain = 1-old.disk.s5(z)
    scale = np.clip(t/old.PLANAR_BLEND,0,1)
    k = old.disk.s5(scale)/old.PLANAR_TURN
    kp = 30*scale**2*(1-scale)**2/(old.PLANAR_BLEND*old.PLANAR_TURN)
    return retain*k,retain*kp-30*z**2*(1-z)**2*k/(BOOST_WIDTH-PLATEAU)


def late_angle(pos,top):
    # The integrand is a degree <=10 polynomial on each of the two pieces.
    # Six-node Gaussian integration is exact for its mathematical coefficients.
    d = np.minimum(np.abs(pos-top),BOOST_WIDTH)
    nodes,weights = old.disk.rule(6)
    val = np.zeros_like(d)
    for lo,hi in ((0.,PLATEAU),(PLATEAU,BOOST_WIDTH)):
        start = np.clip(d,lo,hi)
        length = hi-start
        kk,_ = tail_integrand(start[...,None]+length[...,None]*nodes)
        val += length*(kk@weights)
    k,kp = tail_integrand(d)
    return val,np.where(pos<top,k,-k),-kp


@lru_cache(maxsize=128)
def settings(theta,order):
    period,knots,m0,m1,top = offsets(order)
    delta = old.PLANAR_TURN*theta
    ranges = ((m0+.40,.40),(top+.05,.30))
    cuts = [0.,period,*knots,*np.mod(knots-delta,period),
            top-BOOST_WIDTH,top-PLATEAU,top,top+PLATEAU,top+BOOST_WIDTH]
    for a,length in ranges:
        cuts.extend((a,a+length))
    cuts = np.unique(cuts)
    nodes,weights = old.disk.rule(order)
    widths = np.diff(cuts)
    grid = cuts[:-1,None]+widths[:,None]*nodes
    weights = (widths[:,None]*weights).ravel()
    grid = grid.ravel()
    base,_,_ = angular.angular_data(grid+delta,order)
    raw,_,_ = angle_difference(grid,theta,np.zeros(2),ranges,top,period,order)
    functions = np.column_stack([bump(grid,*ran)[0] for ran in ranges])
    coefs = np.zeros(2)
    for _ in range(10):
        e = raw+functions@coefs
        h = base+e/2
        correction = 2*np.sin(e/2)
        residual = np.array([np.dot(weights,correction*np.cos(h)),
                             np.dot(weights,-correction*np.sin(h))])
        normals = np.stack((np.cos(base+e),-np.sin(base+e)))
        deriv = (normals*weights)@functions
        step = np.linalg.solve(deriv,residual)
        coefs -= step
        if np.max(np.abs(step))<3e-20:
            break
    return period,cuts,ranges,top,coefs


def angle_difference(s,theta,coefs,ranges,top,period,order):
    pos = np.mod(s,period)
    a,k,kp = angular.angular_data(s,order)
    b,l,lp = angular.angular_data(s+old.PLANAR_TURN*theta,order)
    diff = [ETA*(a-b+theta),ETA*(k-l),ETA*(kp-lp)]
    weight = phase_weight(theta)*(C_MAX-ETA)
    for i,z in enumerate(late_angle(pos,top)):
        diff[i] += weight*z
    for c,ran in zip(coefs,ranges):
        for i,z in enumerate(bump(pos,*ran)):
            diff[i] += c*z
    return diff


def corrections(s,theta,order):
    period,cuts,ranges,top,coefs = settings(theta,order)
    p = np.mod(s,period)
    # Integrate the small tangent difference rather than subtracting two
    # nearly equal full period integrals.
    def delta_t(z):
        full,_,_ = angular.angular_data(z+old.PLANAR_TURN*theta,order)
        diff = angle_difference(z,theta,coefs,ranges,top,period,order)[0]
        amp = 2*np.sin(diff/2)
        return amp*np.cos(full+diff/2),-amp*np.sin(full+diff/2)
    nodes,weights = old.disk.rule(order)
    spans = np.diff(cuts)
    mesh = cuts[:-1,None]+spans[:,None]*nodes
    x,z = delta_t(mesh)
    px = np.r_[0.,np.cumsum(spans*(x@weights))]
    pz = np.r_[0.,np.cumsum(spans*(z@weights))]
    i = np.minimum(np.searchsorted(cuts,p,side="right")-1,len(spans)-1)
    width = p-cuts[i]
    x,z = delta_t(cuts[i][...,None]+width[...,None]*nodes)
    return np.stack((px[i]+width*(x@weights),pz[i]+width*(z@weights)),axis=-1)


@lru_cache(maxsize=128)
def anchor(theta,order):
    return corrections(np.asarray([axial.grip_arclength(.55,order)]),theta,order)[0]


def profile(u,theta,order):
    period,_,ranges,top,coef = settings(theta,order)
    unique,inverse = np.unique(u.v,return_inverse=True)
    sample = unique+old.PLANAR_TURN*theta
    q,_,_,_,_ = old.profile_coordinates(sample,order)
    a,k,kp = angular.angular_data(sample,order)
    e,ep,epp = angle_difference(unique,theta,coef,ranges,top,period,order)
    q = q+corrections(unique,theta,order)-anchor(theta,order)
    t = np.column_stack((np.sin(a+e),np.cos(a+e)))
    n = np.column_stack((-t[:,1],t[:,0]))
    k,kp = k+ep,kp+epp
    q,t,n,k,kp = (a[inverse] for a in (q,t,n,k,kp))
    return ([unary(u,q[:,i],t[:,i],-k*n[:,i]) for i in range(2)],
            [unary(u,n[:,i],k*t[:,i],kp*t[:,i]-k*k*n[:,i]) for i in range(2)])


def outer_roll(v,c,order):
    p,d = old.end_offsets(v,order)
    if c==1.:
        return p,d
    eta,k,_,_,_ = old.turn(v.v,np.pi/2,old.END_TURN,old.END_BLEND,order)
    gain = np.sqrt(np.maximum(0.,(c-1)*(c+1)+np.cos(eta)**2))/c
    nodes,weights = old.disk.rule(order)
    total = np.zeros_like(v.v)
    for lo,hi in zip((0.,old.END_BLEND,old.END_LENGTH-old.END_BLEND),
                     (old.END_BLEND,old.END_LENGTH-old.END_BLEND,old.END_LENGTH)):
        span = np.clip(v.v-lo,0,hi-lo)
        a = old.disk.softened_angle(lo+span[...,None]*nodes,old.END_LENGTH,old.END_BLEND,1/old.END_TURN)
        total += span*(np.sqrt((c-1)*(c+1)+np.cos(a)**2)@weights)/c
    return unary(v,total,gain,-np.sin(eta)*np.cos(eta)*k/(c*c*gain)),d/c


def cap_profile(w,c,order):
    """Cap leaves use the original inward material distance near the rim."""
    b = np.asarray([old.END_LENGTH])
    p,d = outer_roll(J(b),c,order)
    tilt = np.arctan2(np.sqrt((c-1)*(c+1)),1.)
    end = np.clip(w.v,0,CAP_TURN)
    z = np.clip((end-CAP_STRAIGHT)/(CAP_TURN-CAP_STRAIGHT),0,1)
    angle = tilt*(1-old.disk.s5(z))
    deriv = -tilt*30*z*z*(1-z)**2/(CAP_TURN-CAP_STRAIGHT)
    ds,ys = old.disk.integrals(end,(0.,CAP_STRAIGHT,CAP_TURN),
        lambda t:tilt*(1-old.disk.s5(np.clip((t-CAP_STRAIGHT)/(CAP_TURN-CAP_STRAIGHT),0,1))),order)
    a = np.clip((w.v-CAP_TURN)/FLATTEN,0,1)
    j = np.where(w.v<=CAP_TURN,w.v,CAP_TURN+FLATTEN*(a-2.5*a**4+3*a**5-a**6))
    slope = 1-old.disk.s5(a)
    second = -30*a*a*(1-a)**2/FLATTEN
    clock = unary(w,j,slope,second)
    tail = np.maximum(0.,j-CAP_TURN)
    dist = unary(w,d.v[0]+ds+tail,slope*np.cos(angle),second*np.cos(angle)-np.sin(angle)*deriv)
    height = unary(w,p.v[0]+ys,np.sin(angle),np.cos(angle)*deriv)
    shrink = 1-(w-clock)/(1-CAP_CLOCK_LIMIT)
    return dist,height,shrink


def cap_point(u,d,rho,theta,order):
    q,n = profile(u,theta,order)
    gx = q[0]-d*n[0]-old.CENTER_X
    gz = q[1]-d*n[1]
    norm2 = gx*gx+gz*gz
    r = np.sqrt(norm2.v)
    radius = unary(norm2,r,.5/r,-.25/r**3)
    radial_weight = angular.cap_s7((rho-.40)/.30)
    radius_out = rho*(CORE_RADIUS+radial_weight*(radius-CORE_RADIUS))
    period,*_ = offsets(order)
    shifted = u.v+old.PLANAR_TURN*theta
    distinct,inverse = np.unique(shifted,return_inverse=True)
    q0,_,n0,_,_ = old.profile_coordinates(distinct,order)
    _,end_d = old.end_limits(order)
    original = (q0-(end_d+CAP_CLOCK_LIMIT)*n0)[inverse]
    original[:,0] -= old.CENTER_X
    pos = np.mod(shifted,period)
    reference = np.where(pos<=period/2,1.,-1.)*np.arctan2(np.abs(original[:,1]),original[:,0])
    reference -= 2*np.pi*np.floor(shifted/period)
    drift = np.arctan2(original[:,0]*gz.v-original[:,1]*gx.v,
                       original[:,0]*gx.v+original[:,1]*gz.v)
    angular_value = reference+drift
    den = norm2.v
    pu = (gx.v*gz.s-gz.v*gx.s)/den
    pv = (gx.v*gz.a-gz.v*gx.a)/den
    puu = (gx.v*gz.ss-gz.v*gx.ss-pu*norm2.s)/den
    pvv = (gx.v*gz.aa-gz.v*gx.aa-pv*norm2.a)/den
    puv = (gx.a*gz.s+gx.v*gz.sa-gz.a*gx.s-gz.v*gx.sa-pu*norm2.a)/den
    real_angle = J(angular_value,pu,pv,puu,puv,pvv)
    common_angle = np.pi-2*np.pi*u/period
    alpha = common_angle+angular.cap_s7((rho-.15)/.20)*(real_angle-common_angle)
    from r742_tilted_disk_two_jets import trig
    co,si = trig(alpha)
    return old.CENTER_X+radius_out*co,radius_out*si


def one_phase(chart,aa,bb,theta,order,rotate,free_field):
    u,v = J(aa,s=1.),J(bb,a=1.)
    c = 1+(C_MAX-1)*phase_weight(theta)**2
    if chart=="cylinder":
        if np.any(np.abs(bb)>1+2e-14):
            raise ValueError("cylinder ordinate")
        q,_ = profile(u,theta,order)
        x,y,z = q[0],v,q[1]
    elif chart in ("end+","end-"):
        if np.any((bb<0)|(bb>old.END_LENGTH+2e-14)):
            raise ValueError("rolled arclength")
        sg = 1 if chart.endswith("+") else -1
        q,n = profile(u,theta,order)
        p,d = outer_roll(v,c,order)
        x,y,z = q[0]-d*n[0],sg*(1+p),q[1]-d*n[1]
    elif chart in ("cap+","cap-","cap-normal+","cap-normal-","cap-cartesian+","cap-cartesian-"):
        sg = 1 if chart.endswith("+") else -1
        if chart.startswith("cap-cartesian"):
            # This disk is common in the pre-rotation material and physical planes.
            if np.any((aa-old.CENTER_X)**2+bb**2>(.15*CORE_RADIUS)**2):
                raise ValueError("Cartesian cap coordinate outside the common core")
            x,z = u,v
            _,p,_ = cap_profile(J(np.ones_like(bb)),c,order)
        else:
            w = v if chart.startswith("cap-normal") else 1-v
            limit = CAP_TURN if chart.startswith("cap-normal") else 1.
            if np.any((w.v<0)|(w.v>limit+2e-14)):
                raise ValueError("cap leaf coordinate")
            d,p,rho = cap_profile(w,c,order)
            x,z = cap_point(u,d,rho,theta,order)
        y = sg*(1+p+axial.cap_displacement(x,z,(.75 if sg==1 else .50)*np.sin(theta)))
    else:
        raise ValueError("unknown R751 chart "+str(chart))
    if free_field is not None:
        dx,dy,dz=free_field(x,y,z,theta)
        x,y,z=x+dx,y+dy,z+dz
    if rotate:
        ox,oz=axial.axis(order)
        co,si=np.cos(theta),np.sin(theta)
        xx,zz=x-ox,z-oz
        x,z=ox+co*xx-si*zz,oz+si*xx+co*zz
    return gather((x,y,z),len(aa))


def chart_jet(chart,u,v,phase=0.,order=32,rotate=True,free_field=None):
    """World or pre-rotation six-jet; cap± uses fraction 1-w increasing to the rim.

    cap-normal± uses inward material w up to .0012. cap-cartesian± uses
    fixed pre-rotation plane coordinates in the common interior disk of
    radius .15*CORE_RADIUS about (old.CENTER_X,0). The polar and Cartesian
    charts agree there at all phases. Cylinder/roll coordinates are R746's.
    """
    old.disk._public()
    a,b,t = np.broadcast_arrays(np.asarray(u,float),np.asarray(v,float),np.asarray(phase,float))
    if np.any((t<0)|(t>np.pi/2+2e-14)):
        raise ValueError("physical phase outside declared interval")
    out = np.empty((t.size,6,3))
    for angle in np.unique(t):
        selected = t.ravel()==angle
        out[selected] = one_phase(chart,a.ravel()[selected],b.ravel()[selected],
                                  float(angle),order,rotate,free_field)
    return out.reshape(t.shape+(6,3))


def small_ratio_jet(s,v,phase,side=1,order=32,rotate=True):
    """Exact local candidate on a phase/area where k_new=ETA*k_initial.

    In pre-rotation coordinates this is the supported proportional branch
    before its first meridian singularity. The caller selects a true original
    shifted-straight, unboosted material section away from closure bumps.
    """
    old.disk._public()
    if not 0<=phase<=np.pi/2 or side not in (-1,1):
        raise ValueError("physical phase or end side")
    aa,bb=np.broadcast_arrays(np.asarray(s,float),np.asarray(v,float))
    if np.any((bb<0)|(bb>old.END_BLEND*ETA**(1/3)/8)):
        raise ValueError("outside explicit small-ratio width")
    u,w=J(aa.ravel(),s=1.),J(bb.ravel(),a=1.)
    q,n=profile(u,float(phase),order)
    _,d=old.end_offsets(w,order)
    nodes,weights=old.disk.rule(order)
    def cosine(x):
        a=old.disk.softened_angle(x,old.END_LENGTH,old.END_BLEND,1/old.END_TURN)
        return np.sqrt(1-(np.sin(a)/ETA)**2)
    a,rate,_,_,_=old.turn(w.v,np.pi/2,old.END_TURN,old.END_BLEND,order)
    pp=cosine(w.v)
    p=unary(w,w.v*(cosine(w.v[:,None]*nodes)@weights),pp,
        -np.sin(a)*np.cos(a)*rate/(ETA**2*pp))
    x,y,z=q[0]-d*n[0]/ETA,side*(1+p),q[1]-d*n[1]/ETA
    if rotate:
        ox,oz=axial.axis(order)
        co,si=np.cos(phase),np.sin(phase)
        dx,dz=x-ox,z-oz
        x,z=ox+co*dx-si*dz,oz+si*dx+co*dz
    return gather((x,y,z),aa.size).reshape(aa.shape+(6,3))
