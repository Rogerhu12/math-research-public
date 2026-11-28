#!/usr/bin/env python3
"""R747 offset-arclength action and full closed-surface physical two-jets.

Both chart_jet and legacy_chart_jet use precisely the same material charts
and initial physical target. All actual evaluation is on public Actions.
"""
import numpy as np
import r746_axial_translation_closed_two_jets as axial
import r744_extruded_closed_two_jets as old
from r742_tilted_disk_two_jets import J, unary, cap_s7, gather


RADIUS = old.PLANAR_TURN
JOIN = .00025
RAMP = .0005
LAST = JOIN + RAMP/2
CAP_ONLY = axial.EndModes(0., 0., .75, .50)
REFERENCE = axial.REFERENCE


def angular_data(s, order):
    """Lift of clockwise turning, its arclength derivative k, and k' (no quadrature)."""
    s = np.asarray(s,dtype=float)
    lh,m0,m1,rtop,half,*_ = old.profile_constants(order)
    lap = np.floor(s/(2*half))
    pos = np.mod(s,2*half)
    lower = pos>half
    z = np.where(lower,2*half-pos,pos)
    angle = np.zeros_like(z)
    k = np.zeros_like(z)
    kp = np.zeros_like(z)
    for mask, length, ccw in (((z>lh)&(z<=m0),np.pi/2,True),
                              ((z>m1)&(z<=rtop),np.pi,False)):
        arc = m0-z[mask] if ccw else z[mask]-m1
        end = RADIUS*length+old.PLANAR_BLEND
        a = old.disk.softened_angle(arc,end,old.PLANAR_BLEND,1/RADIUS)
        w = np.clip(np.minimum(arc,end-arc)/old.PLANAR_BLEND,0,1)
        ks = (30*w*w*(1-w)**2*np.where(arc<end/2,1.,-1.)
              /(RADIUS*old.PLANAR_BLEND))
        angle[mask] = np.pi/2-a if ccw else a
        k[mask] = old.disk.s5(w)/RADIUS
        kp[mask] = -ks if ccw else ks
    mask = (z>m0)&(z<=m1)
    x = z[mask]-m0-1
    angle[mask] = np.pi/2-old.disk.beta(x)
    k[mask] = -old.disk.curvature(x)
    local = (x-old.disk.HOLD)/old.disk.BEND
    d = np.clip(np.minimum(local,1-local)/old.disk.EDGE,0,1)
    max_bend = np.pi/(2*old.disk.BEND*(1-old.disk.EDGE))
    kp[mask] = (-max_bend*30*d*d*(1-d)**2*np.where(local<.5,1.,-1.)
                /(old.disk.BEND*old.disk.EDGE))
    angle[z>rtop] = np.pi
    return (2*np.pi*lap+np.where(lower,2*np.pi-angle,angle), k,
            np.where(lower,-kp,kp))


def lifted(u, order):
    a,k,kp = angular_data(u.v,order)
    return unary(u,a,k,kp)


def angular_shift(u, d, theta, weight, order):
    """Invert the monotone lifted arclength, then implicitly differentiate twice."""
    a0 = lifted(u,order)
    advance = theta*(RADIUS-d)*weight
    if np.all(advance.v==0.) and np.all(theta==0.):
        return u
    # The derivative of s-d*Theta is >=1-.109/.15>.27 throughout this atlas.
    lo = np.asarray(u.v,dtype=float).copy()
    hi = lo+advance.v/.26
    pos = np.minimum(hi,np.maximum(lo,lo+advance.v))
    active = np.ones_like(pos,dtype=bool)
    for _ in range(58):
        if not np.any(active):
            break
        ang,k,_ = angular_data(pos,order)
        err = pos-u.v-d.v*(ang-a0.v)-advance.v
        active &= (np.abs(err)>7e-15*(1+np.abs(pos)))
        lo = np.where(active&(err<0),pos,lo)
        hi = np.where(active&(err>0),pos,hi)
        new = pos-err/(1-d.v*k)
        new = np.where((new>lo)&(new<hi),new,(lo+hi)/2)
        pos = np.where(active,new,pos)
    ang,k,kp = angular_data(pos,order)
    denom = 1-d.v*k
    rhs = u-d*a0+advance
    su = (rhs.s+d.s*ang)/denom
    sv = (rhs.a+d.a*ang)/denom
    first = J(pos,su,sv)
    residue = first-d*unary(first,ang,k,kp)-rhs
    return J(pos,su,sv,-residue.ss/denom,-residue.sa/denom,-residue.aa/denom)


def cap_leaf(w, order):
    """A full nested cap foliation; w is zero on the rim and one at its center."""
    t = np.clip((w.v-JOIN)/RAMP,0,1)
    smooth = old.disk.s5(t)
    slope = 1-smooth
    x = np.where(w.v<=JOIN,w.v,JOIN+RAMP*(t-2.5*t**4+3*t**5-t**6))
    j = unary(w,x,slope,-30*t*t*(1-t)**2/RAMP)
    p_end,d_end = old.end_limits(order)
    rho = 1-(w-j)/(1-LAST)
    return d_end+j,rho


def polar_point(u,d,rho,order):
    q,n = old.profile(u,order)
    return (old.CENTER_X+rho*(q[0]-d*n[0]-old.CENTER_X),
            rho*(q[1]-d*n[1]))


def sphere_chart(chart,u,v,phase,modes,order,legacy):
    if chart=="cylinder":
        return axial.source_chart(chart,u,v,phase,modes,order)
    if chart in ("end+","end-"):
        if legacy:
            return axial.source_chart(chart,u,v,phase,modes,order)
        if np.any((v.v<0)|(v.v>old.END_LENGTH+2e-14)):
            raise ValueError("outward rolling arclength outside end")
        p,d = old.end_offsets(v,order)
        s = angular_shift(u,d,phase,J(1.),order)
        q,n = old.profile(s,order)
        x,z = [q[i]-d*n[i] for i in range(2)]
        p_end,_ = old.end_limits(order)
        w = p/p_end
        bell = 4*w*(1-w)
        sq = bell*bell
        sg = 1 if chart.endswith("+") else -1
        amp = modes.roll_plus if sg==1 else modes.roll_minus
        y = sg*(1+p+amp*np.sin(phase)*sq*sq*(1+.2*x+.1*z))
        return x,y,z
    if chart not in ("cap+","cap-","cap-normal+","cap-normal-",
                     "cap-cartesian+","cap-cartesian-"):
        raise ValueError("unknown R747 chart "+str(chart))
    sg = 1 if chart.endswith("+") else -1
    p_end,_ = old.end_limits(order)
    if chart.startswith("cap-cartesian"):
        # This independent regular chart is restricted to the open core w>.75,
        # where the angular transport is identically zero. The complete cap,
        # including its complement, is covered by cap±. Legacy uses the same core.
        x,z = u,v
    else:
        if chart.startswith("cap-normal"):
            if np.any((v.v<0)|(v.v>JOIN+2e-14)):
                raise ValueError("R747 normal rim collar coordinate outside chart")
            w = v
        else:
            if np.any((v.v<0)|(v.v>1+2e-14)):
                raise ValueError("R747 cap radial fraction outside chart")
            w = 1-v
        d,rho = cap_leaf(w,order)
        weight = 1-cap_s7((w-.25)/.50)
        s = u if legacy else angular_shift(u,d,phase,weight,order)
        x,z = polar_point(s,d,rho,order)
    amp = modes.cap_plus if sg==1 else modes.cap_minus
    y = sg*(1+p_end+axial.cap_displacement(x,z,amp*np.sin(phase)))
    return x,y,z


def physical(chart,u,v,phase,order,modes,free_field,rotate,legacy):
    old.disk._public()
    a,b,theta = np.broadcast_arrays(np.asarray(u,dtype=float),np.asarray(v,dtype=float),
                                    np.asarray(phase,dtype=float))
    if np.any((theta<0)|(theta>np.pi/2+2e-14)):
        raise ValueError("angle outside R746/R747 range")
    ph = theta.ravel()
    x,y,z = sphere_chart(chart,J(a.ravel(),s=1.),J(b.ravel(),a=1.),
                         ph,modes,order,legacy)
    if free_field is not None:
        dx,dy,dz = free_field(x,y,z,ph)
        x,y,z = x+dx,y+dy,z+dz
    if rotate:
        ox,oz = axial.axis(order)
        c,ss = np.cos(ph),np.sin(ph)
        xx,zz = x-ox,z-oz
        x,z = ox+c*xx-ss*zz,oz+ss*xx+c*zz
    return gather((x,y,z),a.size).reshape(a.shape+(6,3))


def chart_jet(chart,u,v,phase=0.,order=32,modes=REFERENCE,free_field=None,rotate=True):
    """R747 physical jets (F,Fu,Fv,Fuu,Fuv,Fvv). For the pre-rotation field set rotate=False.

    cylinder: u=s,v=y. end±: u=s,v=outward arclength. cap±: u=s,v=1-w
    from center to rim in the R747 foliation. cap-normal±: u=s,v=w in
    [0,.00025]. cap-cartesian±: u=x,v=z ONLY in the regular interior
    core w>.75, where angular transport vanishes. See the paper for its
    boundary, a scaled star disk. Pre-rotation free_field is a common
    three-component two-jet function across all charts as in R746.
    """
    return physical(chart,u,v,phase,order,modes,free_field,rotate,False)


def legacy_chart_jet(chart,u,v,phase=0.,order=32,modes=REFERENCE,free_field=None,rotate=True):
    """Original R746 phase map pulled back by exactly the same fixed R747 material atlas."""
    return physical(chart,u,v,phase,order,modes,free_field,rotate,True)
