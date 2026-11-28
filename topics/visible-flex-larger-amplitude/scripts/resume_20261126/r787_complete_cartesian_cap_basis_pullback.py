"""R787 canonical polar-column pullback on the two regular Cartesian cap charts.

Every original coefficient is shared by all chart descriptions.  In the
interior the original angular tensor has compact support and the Cartesian
world columns are already the entire field. Its annular overlap uses the true
inverse of the R787 cap projection, including both material derivatives.
"""
from functools import lru_cache

import numpy as np

import r787_long_left_wall_and_complete_initial_disks as wall
import r787_preloaded_two_complete_caps_and_four_returning_meridians as geometry
from r742_tilted_disk_two_jets import J


def parallel(station, depth, order):
    curve, normal = wall.parts(J(station, s=1.), order)
    offset = wall.m.terminal(order)[1]+wall.origin.LIP+depth
    return curve[0]-offset*normal[0], curve[1]-offset*normal[1]


@lru_cache(maxsize=12)
def regular_ray_grid(order):
    half = wall.old.material(order, True)[-1]
    s = np.linspace(0., half, 1025)
    x, z = parallel(s, wall.RIM_TURN, order)
    cx = wall.m.section_center(order)
    angle = np.arctan2(np.maximum(z.v, 0.), x.v-cx)
    angle[0], angle[-1] = np.pi, 0.
    return half, s, angle, cx


def station_on_ray(angle, depth, order):
    half, grid, angles, cx = regular_ray_grid(order)
    s = np.interp(-angle, -angles, grid)
    lo, hi = np.zeros_like(s), np.full_like(s, half)
    for _ in range(55):
        x, z = parallel(s, depth, order)
        dx = x.v-cx
        rad2 = dx*dx+z.v*z.v
        phi = np.arctan2(np.maximum(z.v, 0.), dx)
        err = phi-angle
        mask = (angle>0.) & (angle<np.pi)
        if not np.any(mask & (abs(err)>4.e-15)):
            break
        lo = np.where((err>0.) & mask,s,lo)
        hi = np.where((err<0.) & mask,s,hi)
        dphi = (dx*z.s-z.v*x.s)/rad2
        step = s-np.divide(err,dphi,out=np.zeros_like(s),where=dphi<0.)
        good = (dphi<0.) & (step>lo) & (step<hi)
        s = np.where(mask & (abs(err)>4.e-15),np.where(good,step,(lo+hi)/2),s)
    s = np.where(angle==np.pi,0.,np.where(angle==0.,half,s))
    x, z = parallel(s, depth, order)
    return s, np.hypot(x.v-cx,z.v)


def coordinate_normal(s, w, x, z, order):
    f,h = wall.cap_projection("cap-normal+",s,w,order)
    dx,dz=f.v-x,h.v-z
    det=f.s*h.a-f.a*h.s
    ds=(h.a*dx-f.a*dz)/det
    dw=(-h.s*dx+f.s*dz)/det
    return ds,dw,np.maximum(abs(dx),abs(dz))


def resolve_rim(x,z,angle,s,w,order):
    # The physical Cartesian overlaps presently meet the homothetic portion.
    # This separate solve also admits every regular point of the thin true
    # normal strip, where radial scaling alone is not the inverse chart.
    for _ in range(12):
        ds,dw,error=coordinate_normal(s,w,x,z,order)
        if np.all(error<3.e-14):
            break
        keep=error>=3.e-14
        s=np.where(keep,s-ds,s); w=np.where(keep,w-dw,w)
    _,_,error=coordinate_normal(s,w,x,z,order)
    bad=(error>3.e-12) | ~np.isfinite(error)
    if np.any(bad):
        rr=wall.RESIDUAL_NORMAL; ramp=wall.RADIAL_RAMP
        cx=wall.m.section_center(order);wanted=np.hypot(x[bad]-cx,z[bad])
        lo=np.zeros_like(wanted);hi=np.full_like(wanted,rr+ramp+1.e-10)
        for _ in range(48):
            u=(lo+hi)/2
            t=np.clip((u-rr)/ramp,0.,1.)
            j=np.where(u<rr,u,rr+ramp*(t-2.5*t**4+3*t**5-t**6))
            rho=1-(u-j)/(1-wall.RIM_TURN)
            ss,r=station_on_ray(angle[bad],j,order)
            inside=r*rho>wanted
            lo=np.where(inside,u,lo);hi=np.where(inside,hi,u)
        w[bad]=(lo+hi)/2
        t=np.clip((w[bad]-rr)/ramp,0.,1.)
        j=np.where(w[bad]<rr,w[bad],rr+ramp*(t-2.5*t**4+3*t**5-t**6))
        ss,_=station_on_ray(angle[bad],j,order)
        half=regular_ray_grid(order)[0]
        s[bad]=np.where(z[bad]<0.,2*half-ss,ss)
    return s,1-w


def inverse_twojet(f,h):
    det=f.s*h.a-f.a*h.s
    if np.any(~np.isfinite(det)) or np.any(abs(det)<1.e-13):
        raise ArithmeticError("nonregular R787 polar cap coordinate at a live Cartesian tensor")
    def solve(x,z):
        return (h.a*x-f.a*z)/det,(-h.s*x+f.s*z)/det
    sx,vx=solve(1.,0.);sz,vz=solve(0.,1.)
    def second(a,b,c,d):
        return solve(-(f.ss*a*c+f.sa*(a*d+b*c)+f.aa*b*d),
                     -(h.ss*a*c+h.sa*(a*d+b*c)+h.aa*b*d))
    sxx,vxx=second(sx,vx,sx,vx)
    sxz,vxz=second(sx,vx,sz,vz)
    szz,vzz=second(sz,vz,sz,vz)
    return sx,vx,sz,vz,sxx,vxx,sxz,vxz,szz,vzz


@lru_cache(maxsize=384)
def inverse_rows(x_words,z_words,order):
    x=np.frombuffer(x_words,dtype="<f8");z=np.frombuffer(z_words,dtype="<f8")
    half,_,_,cx=regular_ray_grid(order)
    r=np.hypot(x-cx,z)
    nz=np.flatnonzero(r>0.)
    angle=np.arctan2(abs(z[nz]),x[nz]-cx)
    s,outer=station_on_ray(angle,wall.RIM_TURN,order)
    # w >= .0008 is the exact homothety of the last inward parallel.
    v=(1-wall.RIM_TURN)*r[nz]/outer
    # In the inherited R764 dictionary the end tensor's last transverse
    # limit is B+E+L+.145, so all polar-specific values and two-jets are zero
    # for 1-v >= .145.  The centered pole lies strictly in this open region.
    use=v>=1-.145-1.e-11
    ids=nz[use];s=s[use].copy();v=v[use].copy();angle=angle[use]
    if not len(ids):
        return ids,None,None,None
    s=np.where(z[ids]<0.,2*half-s,s)
    rim=v>=1-wall.RESIDUAL_NORMAL-wall.RADIAL_RAMP-1.e-11
    if np.any(rim):
        sr,vr=resolve_rim(x[ids][rim],z[ids][rim],angle[rim],s[rim],
                          1-v[rim],order)
        s[rim],v[rim]=sr,vr
    f,h=wall.cap_projection("cap+",s,v,order)
    error=np.maximum(abs(f.v-x[ids]),abs(h.v-z[ids]))
    if np.any(~np.isfinite(error)) or np.any(error>1.e-11):
        raise ArithmeticError("R787 Cartesian cap did not invert its actual polar projection")
    return ids,s,v,inverse_twojet(f,h)


def pullback(columns,derivatives):
    sx,vx,sz,vz,sxx,vxx,sxz,vxz,szz,vzz=(v[:,None] for v in derivatives)
    val,bs,bv,bss,bsv,bvv=np.moveaxis(columns,1,0)
    def mixed(a,b,c,d,ss,vv):
        return bss*a*c+bsv*(a*d+b*c)+bvv*b*d+bs*ss+bv*vv
    return np.stack((val,bs*sx+bv*vx,bs*sz+bv*vz,
                     mixed(sx,vx,sx,vx,sxx,vxx),
                     mixed(sx,vx,sz,vz,sxz,vxz),
                     mixed(sz,vz,sz,vz,szz,vzz)),axis=1)


def polar_basis(chart,a,b,order,mode,na,nr,ref,orig):
    """Evaluate the same complete native physical columns at Cartesian (X,Z)."""
    x=np.ascontiguousarray(a,dtype="<f8");z=np.ascontiguousarray(b,dtype="<f8")
    sign=chart[-1];cart="cap-cartesian"+sign
    out=orig(cart,x,z,order,mode,na,nr,ref)
    if mode=="rigid_caps":
        return out
    ids,s,v,derivatives=inverse_rows(x.tobytes(),z.tobytes(),order)
    if len(ids):
        key="cap"+sign
        f0=geometry.chart_jet(key,s,v,0.,order)
        original=orig(key,s,v,order,mode,na,nr,f0)
        out[ids]=pullback(original,derivatives)
    return out
