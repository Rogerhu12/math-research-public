"""A finite, global alternative to R746, on its original free disk and original boundary."""
from types import SimpleNamespace
import numpy as np
import r750_rigid_annulus as new


def quaternion(a,ar,az):
    w=.5*np.sqrt(1+np.trace(a,axis1=-2,axis2=-1))
    if len(w) and (not np.isfinite(w).all() or w.min()<.25):
        raise ArithmeticError('R754 absolute rotation exceeds the proved sub-pi chart')
    v=new.cross_part(a)/(4*w[:,None])
    def d(b):
        dw=np.trace(b,axis1=-2,axis2=-1)/(8*w)
        dv=new.cross_part(b)/(4*w[:,None])-v*(dw/w)[:,None]
        return np.column_stack((dw,dv))
    return np.stack((np.column_stack((w,v)),d(ar),d(az)))


def install(frame,build,phase,ell,er):
    ix=np.flatnonzero(ell>new.early.EARLY) if phase else np.empty(0,dtype=int)
    frame.wide_nodes=ix
    if not len(ix):
        frame.wide_old=np.empty((3,0,4));frame.wide_new=np.empty((3,0,4));frame.wide_ax=np.empty((3,0,4));return
    q=new.turn(phase);lo,hi=new.BLEND
    t=SimpleNamespace(r=frame.r[ix],s=frame.s[ix],base=np.broadcast_to(q,(len(ix),3,3)).copy(),
                      br=np.zeros((len(ix),3,3)),bs=np.zeros((len(ix),3,3)))
    e=ell[ix];inside=np.flatnonzero(e<hi)
    if len(inside):new.meridian_seed(t,build,phase,inside,e[inside])
    mid=(e>lo)&(e<hi)
    if np.any(mid):
        u=(e[mid]-lo)/(hi-lo);g=new.early.gate(u);gr=new.early.gate(u,1)*er[ix][mid]/(hi-lo)
        t.base[mid],t.br[mid],t.bs[mid]=new.relative_blend(t.base[mid],t.br[mid],t.bs[mid],q,g,gr)
    # This separate candidate limits the whole nonzero annular curl by using
    # only the actual change of tangent angle, never its curvature derivative.
    ax0,ax1=.065,new.weak.FILLET_START
    g,gd=new.flat_step((e-ax0)/(ax1-ax0))
    delta,ds=build.target(phase).angular_data(t.s)
    phi=.5074*phase
    angle=delta+g*(phi-delta)
    axial,axial_a=new.weak.fields.rotation(angle,0)
    ar=gd*er[ix]*(phi-delta)/(ax1-ax0)
    az=(1-g)*ds
    frame.wide_ax=quaternion(axial,ar[:,None,None]*axial_a,az[:,None,None]*axial_a)
    frame.wide_old=quaternion(frame.base[ix],frame.br[ix],frame.bs[ix])
    frame.wide_new=quaternion(t.base,t.br,t.bs)


def weight(a):
    # A finite alternative is explicitly tested; every global tangent column
    # vanishes at zero, so old Householder blocks off the compact releases survive.
    return a*a*(3-2*a)


def factor(q,amount):
    h=weight(amount)
    unit=q[0]
    raw=h*unit.copy();raw[:,0]+=1-h
    scale=np.sqrt(np.sum(raw*raw,axis=-1))  # analytic also for complex-step
    n=raw/scale[:,None]
    k=new.skew(n[:,1:]);m=np.eye(3)+2*n[:,0,None,None]*k+2*k@k
    def diff(dq):
        d=h*dq
        dn=(d-n*np.sum(n*d,axis=-1)[:,None])/scale[:,None]
        dk=new.skew(dn[:,1:])
        return 2*(dn[:,0,None,None]*k+n[:,0,None,None]*dk+dk@k+k@dk)
    return m,diff(q[1]),diff(q[2])


def correction(old,fresh,a):
    x,xr,xs=factor(old,a);y,yr,ys=factor(fresh,a)
    xt=np.swapaxes(x,-1,-2)
    return y@xt,yr@xt+y@np.swapaxes(xr,-1,-2),ys@xt+y@np.swapaxes(xs,-1,-2)


def center(physical,phase,amount,axial):
    if (amount==0 and axial==0) or phase==0:return physical
    before=new.weak.fields.rotation(np.array([-.5*np.pi*phase]),1)[0]
    after=new.turn(phase)[None];zero=np.zeros_like(before)
    old=quaternion(before,zero,zero);fresh=quaternion(after,zero,zero)
    d=np.eye(3)
    for value in (amount,axial):
        if value!=0:d=correction(old,fresh,value)[0][0]@d
    return (physical[0],*(v@d.T for v in physical[1:]))
