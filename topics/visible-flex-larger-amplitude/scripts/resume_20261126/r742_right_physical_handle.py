#!/usr/bin/env python3
"""Independent R742 right physical handles; original R742 sources remain intact."""
from dataclasses import dataclass
import numpy as np
import r742_tilted_disk_two_jets as r


@dataclass(frozen=True)
class RightDesign(r.Design):
    right_handle: float=0.


def from_design(d,right):
    return RightDesign(d.gamma,d.height,d.shift,d.join,d.end_height,.14,
                       d.lateral,d.vertical,right)


def shoulder_jet(u,theta,design,normalized=True,phase=0.,side=1,order=32):
    if not isinstance(design,RightDesign):
        return r.shoulder_jet(u,theta,design,normalized,phase,side,order)
    a,th,ph,si=np.broadcast_arrays(np.asarray(u,dtype=float),np.asarray(theta,dtype=float),
                                    np.asarray(phase,dtype=float),np.asarray(side))
    sh=a.shape;a=a.ravel();th=th.ravel();ph=ph.ravel();si=si.ravel()
    factor=design.length if normalized else 1.
    material=a*factor
    out=r.shoulder_jet(a,th,design,normalized,ph,si,order)
    m=(material>r.base.A_LENGTH)&(material<=r.base.A_LENGTH+design.join)
    if np.any(m):
        s=r.J(material[m],s=factor);angle=r.J(th[m]-ph[m],a=1.)
        rb,tb=r.base.rolled_radii(r.base.A_LENGTH,order)
        x0,y,z0,x,c,b=r.first(rb,tb,angle,design,order)
        left=r.cap_s7((-.20-x)/.55);right=r.cap_s7((x-.70)/.30)
        h=design.join+design.left_handle*left+design.right_handle*right
        t=(s-r.base.A_LENGTH)/design.join
        t.v=np.clip(t.v,0,1)
        p=r.clock(t,h,design.join)
        S=r.cap_s7(p)
        v=p.v
        G0=v*(1-v)**4*(1+v*(4+v*(10+2.5*v)))
        sp=140*(v*(1-v))**3
        spp=420*(v*(1-v))**2*(1-2*v)
        G=r.unary(p,G0,1-r.base.s7(v)-sp/2,-sp-spp/2)
        X=(1-S)*x0+S*(r.base.ELL_SCALE*x+design.shift)+h*G*b
        Z=(1-S)*z0+S*design.end_height+h*(S-p+G-G*c)
        if design.lateral or design.vertical:
            hv=p*(1-p)
            window=256*hv*hv*hv*hv
            X+=design.lateral*left*window
            Z+=design.vertical*left*window
        out[m]=r._rotate(r.gather(r.mirror_coordinates(X,y,Z,design,si[m]),len(v)),ph[m])
    return out.reshape(sh+(6,3))


DESIGNS={name+"-left14-right"+str(v):from_design(d,v)
         for name,d in (("tilt32",r.TILT32),("tilt44",r.TILT44))
         for v in (0.,.18,.30,.42)}
