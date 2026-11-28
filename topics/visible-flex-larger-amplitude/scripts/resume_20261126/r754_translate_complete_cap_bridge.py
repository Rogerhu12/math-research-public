#!/usr/bin/env python3
"""R754 full-cap material transport with an exact Euclidean bridge across both rolls.

The step composition converges to the smooth Eulerian velocity specified in the
paper. On the complete protected rectangular cap slab its returned material
two-jet is already the true rigid translation for every positive step count.
"""
import numpy as np

import r754_coherent_mirror_bowed_walls_two_jets as m
from r742_tilted_disk_two_jets import J, cap_s7, gather


def compose(field,u,v):
    return J(field.v,field.s*u.s+field.a*v.s,field.s*u.a+field.a*v.a,
             field.ss*u.s*u.s+2*field.sa*u.s*v.s+field.aa*v.s*v.s+field.s*u.ss+field.a*v.ss,
             field.ss*u.s*u.a+field.sa*(u.s*v.a+u.a*v.s)+field.aa*v.s*v.a+field.s*u.sa+field.a*v.sa,
             field.ss*u.a*u.a+2*field.sa*u.a*v.a+field.aa*v.a*v.a+field.s*u.aa+field.a*v.aa)


def unpack(u):
    return np.stack(np.broadcast_arrays(*u.parts()),axis=-1)


def planar(u,v,theta,order,rigid_left):
    x,_,z=m.actual("cap+",u,v,theta,order,False,rigid_left)
    return x,z


def weight(x,rigid_left):
    right=1-cap_s7(x/.08)
    return right if rigid_left else cap_s7((x+.80)/.15)*right


def inverse_position(s,r,x,z,theta,order,rigid_left):
    s=np.asarray(s).copy()
    r=np.asarray(r).copy()
    for _ in range(22):
        fx,fz=planar(s,r,theta,order,rigid_left)
        ex,ez=fx.v-x,fz.v-z
        bad=np.maximum(np.abs(ex),np.abs(ez))>5e-13
        if not np.any(bad):
            return s,r,fx,fz
        det=fx.s*fz.a-fx.a*fz.s
        ds=(fz.a*ex-fx.a*ez)/det
        dr=(fx.s*ez-fz.s*ex)/det
        # Small angular/time steps leave the exact inverse close to the old label.
        # Limit large steps near the sharply changing, regular star radius chart.
        damping=np.minimum(1.,.03/np.maximum(1e-40,np.maximum(np.abs(ds),np.abs(dr))))
        s=np.where(bad,s-damping*ds,s)
        r=np.where(bad,np.clip(r-damping*dr,0.,1.),r)
    raise ArithmeticError("cap label inverse needs a finer time partition")


def inverse_jets(pos_s,pos_r,fx,fz,px,pz):
    det=fx.s*fz.a-fx.a*fz.s
    solve=lambda x,z:((fz.a*x-fx.a*z)/det,(fx.s*z-fz.s*x)/det)
    su,ru=solve(px.s,pz.s)
    sv,rv=solve(px.a,pz.a)
    s,r=J(pos_s,su,sv),J(pos_r,ru,rv)
    ex,ez=compose(fx,s,r),compose(fz,s,r)
    suu,ruu=solve(px.ss-ex.ss,pz.ss-ez.ss)
    suv,ruv=solve(px.sa-ex.sa,pz.sa-ez.sa)
    svv,rvv=solve(px.aa-ex.aa,pz.aa-ez.aa)
    return J(pos_s,su,sv,suu,suv,svv),J(pos_r,ru,rv,ruu,ruv,rvv)


def split(u,mask):
    return J(*[np.broadcast_to(a,np.shape(u.v))[mask] for a in u.parts()])


def merge(old,new,mask):
    out=unpack(old).copy()
    out[mask]=unpack(new)
    return J(*out.T)


def transported(a,b,theta,order,steps,rigid_left):
    u=J(a,s=np.ones_like(a));v=J(b,a=np.ones_like(a))
    p0x,p0z=planar(a,b,0.,order,rigid_left)
    # All initial points in the protected slab follow pure translation;
    # the same formula holds tangent to either outer roll throughout the collar.
    fixed=(p0x.v<=0.) if rigid_left else (p0x.v>=-.65)&(p0x.v<=0.)
    pole=b<.15
    live=~(fixed|pole)
    result_x,result_z=planar(a,b,theta,order,rigid_left)
    result_x=merge(result_x,split(p0x,fixed)+m.old.PLANAR_TURN*theta,fixed)
    result_z=merge(result_z,split(p0z,fixed),fixed)
    if not np.any(live) or theta==0.:
        return result_x,result_z
    u,v=split(u,live),split(v,live)
    px,pz=split(p0x,live),split(p0z,live)
    tau=2*np.arcsin(np.sqrt(np.clip(theta/m.ANGLE_MAX,0.,1.)))/np.pi
    prior=0.
    for j in range(1,steps+1):
        current=m.ANGLE_MAX*np.sin((np.pi/2)*tau*(j/steps))**2
        next_x,next_z=planar(u.v,v.v,current,order,rigid_left)
        rx,rz=compose(next_x,u,v),compose(next_z,u,v)
        wh=weight(px-m.old.PLANAR_TURN*prior,rigid_left)
        mapped_x=rx+wh*(px+m.old.PLANAR_TURN*(current-prior)-rx)
        mapped_z=rz+wh*(pz-rz)
        change=wh.v>0.
        if j<steps and np.any(change):
            sx,sy,fx,fz=inverse_position(u.v[change],v.v[change],
                mapped_x.v[change],mapped_z.v[change],current,order,rigid_left)
            su,sv=inverse_jets(sx,sy,fx,fz,split(mapped_x,change),split(mapped_z,change))
            u,v=merge(u,su,change),merge(v,sv,change)
        px,pz=mapped_x,mapped_z
        prior=current
    return merge(result_x,px,live),merge(result_z,pz,live)


def chart_jet(chart,u,v,phase=0.,order=32,steps=32,markers=True,rotate=True,free_field=None,rigid_left=False):
    """Full second material chart registration; phases broadcast as for R754.

    Integer steps controls the convergent time composition outside the exact
    bridge. The full mathematical registration is its smooth transport limit.
    Raw and transport entries agree on all non-cap charts, the whole cap-normal
    collar and the regular Cartesian core. With rigid_left=True, all of the
    original cap at x<=0 shares the same translation and has exact metric.
    """
    if chart not in ("cap+","cap-"):
        return m.chart_jet(chart,u,v,phase,order,markers,rotate,free_field,rigid_left)
    m.old.disk._public()
    if not isinstance(steps,int) or steps<1:
        raise ValueError("positive time-composition count")
    a,b,t=np.broadcast_arrays(np.asarray(u,float),np.asarray(v,float),np.asarray(phase,float))
    if np.any((t<0)|(t>m.ANGLE_MAX+2e-14)|(b<0)|(b>1+2e-14)):
        raise ValueError("R754 cap coordinates or phase")
    out=np.empty((t.size,6,3))
    for theta in np.unique(t):
        mask=t.ravel()==theta
        x,z=transported(a.ravel()[mask],b.ravel()[mask],float(theta),order,steps,rigid_left)
        y=J((1 if chart=="cap+" else -1)*(1+m.terminal(order)[0]))
        if free_field is not None:
            dx,dy,dz=free_field(x,y,z,float(theta));x,y,z=x+dx,y+dy,z+dz
        if rotate:
            ox,oz=m.axis(order)
            co,si=np.cos(theta),np.sin(theta)
            xx,zz=x-ox,z-oz
            x,z=ox+co*xx-si*zz,oz+si*xx+co*zz
        out[mask]=gather((x,y,z),np.count_nonzero(mask))
    return out.reshape(t.shape+(6,3))
