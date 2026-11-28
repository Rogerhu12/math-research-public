"""Physical three-curl frame on the R750 annulus, with the original two open boundaries."""
import hashlib
from pathlib import Path

import numpy as np
import r750_rigid_annulus as old
import r760_meridian_moments as moments
import r760_angular_shoulders as shoulders
import r760_triple_period as triple

weak,space=old.weak,old.space
HERE=Path(__file__).resolve().parent


def axial_jet(build,phase,ell,s,small=False):
    build.set_phase(phase)
    inside=(ell<=weak.FILLET_START)
    state=build.r760_states[phase][bool(small)]
    theta,dtheta,o,do=moments.mixture(build,ell-moments.START,build.r760_profile,state)
    has_period=build.r760_three_periods and phase<=.08
    lo,hi=(weak.FILLET_START,old.FLAT_START) if has_period else (.065,weak.FILLET_START)
    v,vd=old.flat_step((ell-lo)/(hi-lo))
    delta,ds=build.target(phase).angular_data(s)
    tip=.5074*phase
    psi=delta+v*(tip-delta)
    pl=vd*(tip-delta)/(hi-lo);ps=(1-v)*ds
    ts=np.zeros_like(theta)
    if has_period:
        theta=o.copy();dtheta=do.copy()
        if np.any(inside):
            coeff,der=triple.lookup(build,phase,s[inside])
            c,b,a=coeff.T;cs,bs,az=der.T
            g=o[inside]/.16;gp=do[inside]/.16
            theta[inside]=c*o[inside]+b*g*g
            dtheta[inside]=c*do[inside]+2*b*g*gp
            ts[inside]=build.ring.length*(cs*o[inside]+bs*g*g)
            psi[inside]+=a*g;pl[inside]+=a*gp;ps[inside]+=build.ring.length*az*g
    _,t,n,k,ks=build.ring.jets(s);per=build.ring.length
    a,aa=weak.fields.rotation(psi,0)
    t=np.einsum('nij,nj->ni',a[:,1:,1:],t)
    n=np.einsum('nij,nj->ni',a[:,1:,1:],n)
    e=np.zeros_like(a);e[:,0,0]=1.;e[:,1:,1]=t;e[:,1:,2]=n
    de=np.zeros_like(e);de[:,1:,1]=n;de[:,1:,2]=-t
    h,ha=weak.fields.rotation(theta-o,1)
    et=weak.fields.trans(e);det=weak.fields.trans(de)
    u=e@h@et
    e_term=(de@h@et+e@h@det)@a
    h_term=e@ha@et@a
    x_term=u@aa
    r=u@a
    rl=pl[:,None,None]*(e_term+x_term)+(dtheta-do)[:,None,None]*h_term
    rs=(k*per+ps)[:,None,None]*e_term+ps[:,None,None]*x_term+ts[:,None,None]*h_term
    return (r,rl,rs),(theta,dtheta,o,pl,ps/per,t,n,k,ks,ts/per)


def replace_bulk(frame,build,phase,small):
    if not phase:return
    ell,er,_=space.ell_data(frame.r)
    # True vertical band starts before the Cartesian center chart.
    end=ell>=old.FLAT_START
    frame.base[end]=old.turn(phase);frame.br[end]=0.;frame.bs[end]=0.
    ix=np.flatnonzero((ell>moments.START)&~end)
    if len(ix):
        (a,b,c),_=axial_jet(build,phase,ell[ix],frame.s[ix],small)
        frame.base[ix]=a;frame.br[ix]=er[ix,None,None]*b;frame.bs[ix]=c


class R760Frame(old.R750Frame):
    def __init__(self,build,phase,r,s,degree):
        # Keep the real two-edge basis and nonzero outer Cauchy fields.
        # Only the zero-control bulk orientation changes.
        build.set_phase(phase)
        # Reuse R743's physical coframe and the frozen R750 coefficient construction.
        # A fresh row does not require computing R750's discarded meridian seed.
        old.early.R743Frame.__init__(self,build,phase,r,s,degree)
        ell,er,_=space.ell_data(self.r)
        old.add_releases(self,build,ell,er)
        mask,dm=old.flat_step((old.FREE_END-ell)/old.FREE_WIDTH)
        self.Br=mask[:,None]*self.Br-(dm*er/old.FREE_WIDTH)[:,None]*self.B
        self.Bs=mask[:,None]*self.Bs
        self.B=mask[:,None]*self.B
        shoulders.install(self,build)
        replace_bulk(self,build,phase,build.r760_small)

    @classmethod
    def from_paid(cls,parent,build,phase):
        if type(parent) is not old.R750Frame:raise TypeError('expected an original R750 native frame')
        build.set_phase(phase)
        out=cls.__new__(cls);vars(out).update(vars(parent))
        out.base,out.br,out.bs=(a.copy() for a in (parent.base,parent.br,parent.bs))
        shoulders.install(out,build)
        replace_bulk(out,build,phase,build.r760_small)
        return out


class R760Build(old.R750Build):
    frame_type=R760Frame

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.install_moments()

    @classmethod
    def from_paid(cls,parent,profile=None):
        if type(parent) is not old.R750Build:raise TypeError('expected an original R750 source build')
        out=cls.__new__(cls);vars(out).update(vars(parent));out.identity=dict(parent.identity)
        out.install_moments(profile)
        return out

    def install_moments(self,profile=None):
        self.r760_profile=moments.solve_profile(self) if profile is None else profile
        self.r760_states={};self.r760_small=False;self.r760_three_periods=True;self.r760_label_states={}
        self.integration_ell_breaks=np.unique(np.r_[self.integration_ell_breaks,
                 self.r760_profile['ell_breaks'],.065,weak.FILLET_START])
        self.identity.update(seed='R760 continuous two-moment meridian and its real full curl',
            target_tip_motion='unchanged R750 -.42 sqrt(lambda) plus Q about the two true ring centers',
            high_profile={k:float(self.r760_profile[k]) for k in ('b','dwell_minus','dwell_plus')})

    def set_phase(self,phase):
        if phase not in self.r760_states:
            self.r760_states[phase]={False:moments.phase_parameters(self,phase,self.r760_profile)}
            if phase<=.08:
                self.r760_states[phase][True]=moments.phase_parameters(self,phase,self.r760_profile,small=True)

    def nodes(self,level,purpose):
        r,s=super().nodes(level,purpose)
        cuts=self.r760_profile['ell_breaks']
        shift={'train':.5,'validation':.319,'qualification':.173}[purpose]
        return (np.unique(np.r_[r,self.radius_at(np.r_[cuts,cuts[:-1]+shift*np.diff(cuts)])]),
                np.unique(np.r_[s,shoulders.true_angles(self,purpose)]))

    @property
    def seed_identity(self):
        out=super().seed_identity
        for name in ('r760_meridian_moments.py','r760_full_annulus_frame.py','r760_angular_shoulders.py','r760_triple_period.py','r760_relative_material_rows.py'):
            out['physics_sha256'][name]=hashlib.sha256((HERE/name).read_bytes()).hexdigest()
        return out


def six_jet_and_curl(frame,build,phase,small=False):
    ell,er,err=space.ell_data(frame.r)
    ix=np.flatnonzero((ell>moments.START)&(ell<old.FLAT_START))
    core=np.flatnonzero(ell>=old.FLAT_START)
    if not len(ix) or not len(core):raise ValueError('both real free annulus and full planar end are required')
    raw=tuple(v.reshape(-1,3) for v in frame.read(frame.q0,output=True))
    _,z=axial_jet(build,phase,ell[ix],frame.s[ix],small)
    th,dt,o,pl,ps,t,n,k,ks,ts=z
    _,u,*_=build.profile.read(frame.r[ix]);sp=1+k*u
    per=build.ring.length;scale=er[ix];st=np.sin(th);ct=np.cos(th)
    d=lambda v:np.asarray(v)[:,None]
    vec=weak.physical.vec;zero=np.zeros(len(th))
    l=vec(ct,-d(st)*n);sl=vec(zero,d(sp)*t)
    ll=vec(-st*dt,-d(ct*dt)*n+d(st*pl)*t)
    ls=vec(-st*ts,d(st*(k+ps))*t-d(ct*ts)*n)
    ss=vec(zero,d(ks*u)*t+d(sp*(k+ps))*n)
    curl=vec(st*ts,d(k*np.sin(o)-(k+ps)*st)*t+d(sp*pl+ct*ts)*n)
    expected=(d(scale*per)*curl,d(scale)*l,per*sl,d(scale*per)*ls,
              d(err[ix])*l+d(scale**2)*ll,per**2*ss)
    errors=[float(np.max(np.linalg.norm(actual[ix]-want,axis=1))) for actual,want in zip(raw,expected,strict=True)]
    q=old.turn(phase);_,pr,ps0,prr,prs,pss=frame.j0
    tip=(np.zeros((len(core),3)),*(a[core]@q.T for a in (pr,ps0,prs,prr,pss)))
    end_errors=[float(np.max(np.linalg.norm(actual[core]-want,axis=1))) for actual,want in zip(raw,tip,strict=True)]
    if not np.isfinite(errors+end_errors).all() or max(errors+end_errors)>3.e-8:
        raise ArithmeticError('actual R760 three-curl or five rotation jets disagree with the material formula')
    return dict(native_free_rows=len(ix),true_rigid_rows=len(core),five_and_curl_errors=errors,
                rigid_five_and_curl_errors=end_errors,native_curl_peak=float(np.linalg.norm(curl,axis=1).max()),
                peak_radial_turn=float(np.sqrt(dt**2+(st*pl)**2).max()),
                original_angular_curl_and_both_boundary_integrals_still_required=True)


def merge_original_tensor(parent,build,phase,r,s):
    """The real old tensor is contained in the new one. Build only genuinely missing geometry."""
    r=np.asarray(r);s=np.asarray(s)
    ro=parent.r.reshape(parent.shape)[:,0];so=parent.s.reshape(parent.shape)[0]
    ri=np.searchsorted(r,ro);si=np.searchsorted(s,so)
    if (np.any(ri>=len(r)) or np.any(si>=len(s)) or not np.array_equal(r[ri],ro)
            or not np.array_equal(s[si],so)):raise ValueError('new mesh lost original R750 tensor points')
    rows=(ri[:,None]*len(s)+si).ravel()
    rr,ss=np.broadcast_arrays(r[:,None],s[None,:]);rr=rr.ravel();ss=ss.ravel()
    out=R760Frame.__new__(R760Frame)
    out.shape=(len(r),len(s));out.r=rr;out.s=ss;out.degree=parent.degree
    out.source_min=parent.source_min
    nc=len(shoulders.tags(parent.degree));out.ncols=3*nc;out.q0=np.zeros(3*nc)
    names=('base','br','bs','B','Br','Bs','det','phi','phip')
    for name in names:
        data=getattr(parent,name)
        tail=(nc,) if name in ('B','Br','Bs') else data.shape[1:]
        setattr(out,name,np.empty((len(rr),*tail),dtype=data.dtype))
    out.j0=tuple(np.empty((len(rr),3)) for _ in range(6))
    def write(ids,fr):
        for name in names:getattr(out,name)[ids]=getattr(fr,name)
        for a,b in zip(out.j0,fr.j0,strict=True):a[ids]=b
        out.source_min=min(out.source_min,fr.source_min)
    for lo in range(0,len(rows),512):
        sl=slice(lo,lo+512)
        tiny=old.R750Frame.__new__(old.R750Frame)
        tiny.shape=(len(rows[sl]),);tiny.source_min=parent.source_min
        tiny.degree=parent.degree;tiny.r=parent.r[sl];tiny.s=parent.s[sl]
        tiny.j0=tuple(a[sl] for a in parent.j0)
        for name in names:setattr(tiny,name,getattr(parent,name)[sl])
        extended=R760Frame.from_paid(tiny,build,phase)
        write(rows[sl],extended)
    missing=np.setdiff1d(np.arange(len(rr)),rows,assume_unique=True)
    for lo in range(0,len(missing),512):
        ix=missing[lo:lo+512];write(ix,R760Frame(build,phase,rr[ix],ss[ix],parent.degree))
    out.parent_material_rows=len(rows);out.new_material_rows=len(missing)
    return out


def release_probe(build,phase):
    base=weak.physical.H
    ell=np.array([.00005,.05014,.188,.188])
    v=np.array([.2061,.84625,.9474,.9474])
    ss=(3+build.ring.LU-v)/build.ring.length
    ss[-1]=(1+v[-1])/build.ring.length
    f=R760Frame(build,phase,build.radius_at(ell),ss,3)
    oldn=len(old.space.tagged_terms(3));n750=len(old.tags(3))
    released=np.max(np.abs(f.B[:2,oldn:n750]),axis=1)
    if np.min(released)<=0:raise ArithmeticError('lost a genuine R752 radial column')
    value=np.max(abs(f.B[2:,n750:]),axis=1)
    angular=np.max(abs(f.Bs[2:,n750:]),axis=1)
    if np.min(value)<.99 or np.min(angular)<8e3*build.ring.length:
        raise ArithmeticError('true narrow R750 angle peak lacks independent value and derivative controls')
    return dict(phase=phase,ell=ell,labels=v,radius=f.r,angles=f.s,old_radial_support=released,
                actual_native_w_centre_values=value,actual_native_w_centre_angle_derivative=angular,
                full_native_curl=f.curl(f.q0),column_count=f.ncols)
