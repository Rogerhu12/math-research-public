"""R746 exact developable seed on the real R743 plane and its full open end band."""
import hashlib
from pathlib import Path

import numpy as np

import r743_early_material_disk as early

weak = early.weak
space = early.space
BLEND_START = .630
BLEND_END = .755
HERE = Path(__file__).resolve().parent


def source_angle(build, phase, y):
    """Use the original material Y, with the exact horizontal continuations of the weak source."""
    line = build.ring.line
    offset = np.asarray(y)-build.ring.origin[0]
    v = offset.copy()
    # |v-(Y0(v)-Ym)| <= 1-cos(.0052) < .000014 on either unit half.
    # The true angle is constant off these padded ramp windows.
    a = abs(offset)
    moving = ((a>.2049)&(a<.3071))|((a>.8459)&(a<.9481))
    inverse_residual = 0.
    if np.any(moving):
        goal = y[moving]
        label = v[moving]
        for i in range(3):
            label = label + (goal-line.position(label)[:,0])
        residual = goal-line.position(label)[:,0]
        inverse_residual = float(np.max(abs(residual)))
        if not np.isfinite(inverse_residual) or inverse_residual>4.e-13:
            raise ArithmeticError("R746 true-material Y inverse did not close")
        v[moving] = label
    beta = phase*weak.ring.angles(v,1.)
    beta_y = phase*weak.ring.line_k(v,1.)/np.cos(weak.ring.angles(v,0.))
    return beta,beta_y,inverse_residual


def trans(a):
    return np.swapaxes(a,-1,-2)


def axis_jet(axis, angle, radial, angular):
    m,ma=weak.fields.rotation(angle,axis)
    return m,radial[:,None,None]*ma,angular[:,None,None]*ma


def compose(left, right):
    a,ar,az=left
    b,br,bz=right
    return a@b,ar@b+a@br,az@b+a@bz


def core_jet(phase, beta, br, bs, w, wr):
    theta=.5*np.pi*phase
    zero=np.zeros_like(beta)
    first=axis_jet(1,-w*theta,-wr*theta,zero)
    second=axis_jet(2,-w*beta,-wr*beta-w*br,-w*bs)
    return compose(first,second)


def annulus_jet(frame, build, phase, indices, w, wr):
    """Extract the frozen signed meridian rotation and its two actual derivatives on the fillet."""
    s=frame.s[indices]
    target=build.target(phase)
    delta,ds=target.angular_data(s)
    c=target.length
    _,t,n,k,_=target.jets(s)
    e=np.zeros((len(s),3,3))
    es=np.zeros_like(e)
    e[:,0,0]=1.
    e[:,1:,1],e[:,1:,2]=t,n
    es[:,1:,1]=(k*c)[:,None]*n
    es[:,1:,2]=-(k*c)[:,None]*t
    et,est=trans(e),trans(es)
    x,xa=weak.fields.rotation(delta,0)
    xt,xst=trans(x),trans(ds[:,None,None]*xa)
    b=frame.base[indices]
    native=et@b@xt@e
    native_r=et@frame.br[indices]@xt@e
    native_s=est@b@xt@e+et@(frame.bs[indices]@xt+b@xst)@e+et@b@xt@es
    sn,cs=native[:,0,2],native[:,0,0]
    squared=sn*sn+cs*cs
    if not np.isfinite(squared).all() or np.min(squared)<.999999:
        raise ArithmeticError("annular source rotation no longer has its genuine meridian axis")
    angle=np.arctan2(sn,cs)
    def derivative(a):
        return (cs*a[:,0,2]-sn*a[:,0,0])/squared
    ar,ass=derivative(native_r),derivative(native_s)
    ref=weak.fields.rotation(angle,1)[0]
    if np.max(abs(native-ref))>1.e-10:
        raise ArithmeticError("R746 blend must start with the original axis-separated R743 fillet frame")
    h=1-w
    turn,tr,ts=axis_jet(1,h*angle,h*ar-wr*angle,h*ass)
    carried=(e@turn@et,e@tr@et,es@turn@et+e@ts@et+e@turn@est)
    axial=axis_jet(0,h*delta,-wr*delta,h*ds)
    return compose(carried,axial)


class R746Frame(early.R743Frame):
    def __init__(self,build,phase,r,s,degree):
        super().__init__(build,phase,r,s,degree)
        self.max_y_inverse_residual=0.
        if phase==0:
            return
        ell,er,_=space.ell_data(self.r)
        indices=np.flatnonzero(ell>BLEND_START)
        if not len(indices):
            return
        rr=ell[indices]
        v=(rr-BLEND_START)/(BLEND_END-BLEND_START)
        w=early.gate(v)
        wr=early.gate(v,1)*er[indices]/(BLEND_END-BLEND_START)
        p,pr,ps,*_=self.j0
        beta,by,res=source_angle(build,phase,p[indices,1])
        self.max_y_inverse_residual=res
        core=core_jet(phase,beta,by*pr[indices,1],by*ps[indices,1],w,wr)
        # Do not extract the original core fade as a meridian angle. Its old seed
        # is replaced completely on this physical end region.
        mid=w<1.
        combined=[a.copy() for a in core]
        if np.any(mid):
            tail=annulus_jet(self,build,phase,indices[mid],w[mid],wr[mid])
            mixed=compose(tuple(a[mid] for a in core),tail)
            for dst,val in zip(combined,mixed,strict=True):
                dst[mid]=val
        self.base[indices],self.br[indices],self.bs[indices]=combined


class R746Build(early.R743Build):
    frame_type=R746Frame

    def __init__(self,baseline=weak.BASELINE,modes=8192,steps=12,order=48):
        super().__init__(baseline=baseline,modes=modes,steps=steps,order=order)
        self.identity.update(seed="R746 physical-Y developable planar frame with a free integral translation",
                             seed_angle="pi*lambda/2",seed_fillet_window=[BLEND_START,BLEND_END],
                             planar_y_source="R743 actual native Y including both horizontal ends")
        cuts=np.array([0.,.002,.004,.5,.996,.998,1.])
        self.integration_ell_breaks=np.unique(np.r_[self.integration_ell_breaks,
                BLEND_START+(BLEND_END-BLEND_START)*cuts])

    def nodes(self,level,purpose):
        r,s=super().nodes(level,purpose)
        shift={"train":.5,"validation":.319,"qualification":.173}[purpose]
        knots=np.array([0.,.002,.004,.5,.996,.998,1.])
        blend=np.r_[knots,knots[:-1]+shift*np.diff(knots)]
        extra=np.r_[BLEND_START+(BLEND_END-BLEND_START)*blend,
                    space.TOTAL-weak.physical.L*.00025]
        return np.unique(np.r_[r,self.radius_at(extra)]),s

    @property
    def seed_identity(self):
        info=super().seed_identity
        for name in ("r746_physical_core_seed.py","r746_native_disk_solver.py"):
            info["physics_sha256"][name]=hashlib.sha256((HERE/name).read_bytes()).hexdigest()
        return info


def centre_jets(original,build,phase,q,degree,mean):
    """The material Y angle is identically zero on an open neighbourhood of the actual Cartesian centre."""
    n=3*(degree+1)*(degree+2)//2
    physical,source=original(build,phase,q[:n],degree,mean)
    turn=weak.fields.rotation(np.asarray(-.5*np.pi*phase),1)[0]
    return (physical[0],*(v@turn.T for v in physical[1:])),source


def check_zero_seed(frame,build,phase):
    """Read the actual existing native frame rows, with no Jacobian or new fit."""
    ell=space.ell_data(frame.r)[0]
    true_flat=(frame.r<=weak.physical.R0)|(ell>space.TOTAL-weak.physical.L*.000499)
    ids=np.flatnonzero(true_flat)
    central=int(np.sum(frame.r[ids]<=weak.physical.R0))
    strip=len(ids)-central
    if not central or not strip:
        raise ValueError("both the actual disk and a true terminal open flat band must be tested")
    # Read only the selected frozen base and its two derivatives at q=0.
    m,mr,ms=frame.base[ids],frame.br[ids],frame.bs[ids]
    p,pr,ps,prr,prs,pss=(v[ids] for v in frame.j0)
    actual=(weak.fields.apply(m,pr),weak.fields.apply(m,ps),
            weak.fields.apply(mr,pr)+weak.fields.apply(m,prr),
            weak.fields.apply(ms,pr)+weak.fields.apply(m,prs),
            weak.fields.apply(ms,ps)+weak.fields.apply(m,pss))
    beta,by,inv=source_angle(build,phase,p[:,1])
    th=.5*np.pi*phase
    cb,sb=np.cos(beta),np.sin(beta)
    tangent=np.column_stack((sb*np.cos(th),cb,sb*np.sin(th)))
    ruling=np.array([-np.sin(th),0.,np.cos(th)])
    tangent_y=by[:,None]*np.column_stack((cb*np.cos(th),-sb,cb*np.sin(th)))
    def first(v):
        return tangent*v[:,1,None]+ruling*v[:,2,None]
    def second(v,a,b):
        return first(v)+tangent_y*(a[:,1]*b[:,1])[:,None]
    expected=(first(pr),first(ps),second(prr,pr,pr),second(prs,pr,ps),second(pss,ps,ps))
    errors=[float(np.max(np.linalg.norm(u-v,axis=-1))) for u,v in zip(actual,expected,strict=True)]
    curl=(weak.fields.apply(mr,ps)-weak.fields.apply(ms,pr))/frame.det[ids,None]
    peak=float(np.max(np.linalg.norm(curl,axis=-1)))
    if not np.isfinite([*errors,peak,inv]).all() or max(errors)>1.e-9 or peak>1.e-9:
        raise ArithmeticError("zero seed differs from its explicit measured physical planar formula")
    return dict(planar_disk_rows=central,true_end_band_rows=strip,
                physical_first_and_second_errors=errors,cartesian_three_curl_max=peak,
                by_axis=np.abs(curl).max(axis=0).tolist(),material_y_inverse_residual=inv)
