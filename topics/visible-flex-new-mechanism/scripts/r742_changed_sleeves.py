"""R742 weak ring with a genuine negatively curved guard on every nonzero basal bend."""
from pathlib import Path
import hashlib
import importlib.util
import numpy as np

HERE = Path(__file__).resolve().parent
WEAK_SHA = "0dbb3fb63f941f733f62350b9e3063c773df1f07b210d51f29ff4adc16ec96cb"
weak_path = HERE/"r740_weak_material_disk.py"
if hashlib.sha256(weak_path.read_bytes()).hexdigest() != WEAK_SHA:
    raise ValueError("the original weak disk formula changed")
spec = importlib.util.spec_from_file_location("_r742_weak_source",weak_path)
weak = importlib.util.module_from_spec(spec)
spec.loader.exec_module(weak)
old_collar = weak.fields.collar_jets
physical = weak.physical
col,vec = physical.col,physical.vec
DEPTH_JOIN = .0008
CUTOFF = .505
WIDTH = .025
ANGULAR_RAMP = .023


def step(t):
    """Septic increasing cutoff with three continuous zero endpoint derivatives."""
    t = np.asarray(t,dtype=float)
    z = np.clip(t,0.,1.)
    h = np.minimum(z,1-z)
    lo = h**4*(35+h*(-84+h*(70-20*h)))
    v = np.where(z<=.5,lo,1-lo)
    d = 140*z**3*(1-z)**3
    dd = 420*z**2*(1-z)**2*(1-2*z)
    return v,d,dd


def support(ring,s):
    """f,f_sigma,f_sigmasigma in dimensional native ring arclength."""
    _,kind,v = ring.label(s)
    primary = (kind==0)|(kind==2)
    orientation = np.where(kind==0,1.,np.where(kind==2,-1.,0.))
    distance = abs(v)
    derivative = np.sign(v)*orientation
    # f=-1 on the whole U, including its truly straight end germ.
    z = (distance-(1-ANGULAR_RAMP))/ANGULAR_RAMP
    value,d1,d2 = step(z)
    f = -np.where(primary,value,1.)
    fs = np.where(primary,-d1*derivative/ANGULAR_RAMP,0.)
    fss = np.where(primary,-d2/ANGULAR_RAMP**2,0.)
    for begin,sign in ((.205,1.),(.846,-1.)):
        end = begin+.102
        a,ad,add = step(1+(distance-begin)/ANGULAR_RAMP)
        b,bd,bdd = step(1+(end-distance)/ANGULAR_RAMP)
        scale = sign*derivative/weak.B0
        f += scale*a*b
        fs += scale*derivative*(ad*b-a*bd)/ANGULAR_RAMP
        fss += scale*(add*b-2*ad*bd+a*bdd)/ANGULAR_RAMP**2
    return f,fs,fss


def depth(d):
    """Exact x-ray jet until x=.0008, matched positive acceleration, then a compact cutoff."""
    d = np.asarray(d,dtype=float)
    shape = d.shape
    x,indices = np.unique(d.ravel(),return_inverse=True)
    base = np.clip(x,0.,DEPTH_JOIN)
    t,_,td,tdd = physical.time_from_x(base)
    p = t**4
    v = 4*t**3*td
    acc = 12*t**2*td**2+4*t**3*tdd
    dx = np.maximum(x-DEPTH_JOIN,0.)
    p = p+dx*v+.5*dx**2*acc
    v = v+dx*acc
    cut,first,second = step(1-(x-CUTOFF)/WIDTH)
    first,second = -first/WIDTH,second/WIDTH**2
    # The value after the cutoff is exactly zero, including both derivatives.
    out = (p*cut,v*cut+p*first,acc*cut+2*v*first+p*second)
    return tuple(a[indices].reshape(shape) for a in out)


def ring_jets(ring,d,s):
    """Jets in dimensional (x,sigma), with the actual full periodic f."""
    gamma,T,N,k,ks = ring.jets(s)
    f,fs,fss = support(ring,s)
    p,px,pxx = depth(d)
    b,bx,bs = p*f,px*f,p*fs
    bxx,bxs,bss = pxx*f,px*fs,p*fss
    speed = 1+k*b
    zero = np.zeros_like(d)
    return (vec(physical.W+d,gamma-col(b)*N),
            vec(np.ones_like(d),-col(bx)*N),
            vec(zero,col(speed)*T-col(bs)*N),
            vec(zero,-col(bxx)*N),
            vec(zero,col(k*bx)*T-col(bxs)*N),
            vec(zero,col(ks*b+2*k*bs)*T+col(k*speed-bss)*N))


def collar_jets(build,phase,d,s,actual):
    """Carry every rigid open piece, and use the original true moving Cauchy jets."""
    d,s = np.broadcast_arrays(np.asarray(d,dtype=float),np.asarray(s,dtype=float))
    ring = build.target(phase)
    result = list(ring_jets(ring,d,s))
    if not actual or phase==0:
        return tuple(result)
    _,kind,v = ring.label(s)
    orientation = np.where(kind==0,1.,np.where(kind==2,-1.,0.))
    native = abs(v)
    # The varying Cauchy datum is inside [.206,.306] and [.847,.947].
    # The transition used here lies strictly inside the f=1/k_* plateau,
    # the old w=1 plateau and the Cauchy domain on which the motion is rigid.
    for center in (.206,.847):
        width = .0001
        a,ad,add = step((native-center+.00028)/width)
        b,bd,bdd = step((center+.10028-native)/width)
        g = a*b*(orientation!=0)
        use = g>0
        if not np.any(use):
            continue
        old = old_collar(build,phase,d[use],s[use],True)
        # Preserve the calculated small Cauchy terms on its complete inner zone.
        inner = g[use]==1
        for val,past in zip(result,old,strict=True):
            val[use] = np.where(inner[...,None],past,val[use])
        transition = use & (g<1)
        if np.any(transition):
            orient = np.sign(v[transition])*orientation[transition]
            gs = orient*(ad[transition]*b[transition]-a[transition]*bd[transition])/width
            gss = (add[transition]*b[transition]-2*ad[transition]*bd[transition]
                   +a[transition]*bdd[transition])/width**2
            zero = np.zeros_like(gs)
            difference = [past[~inner]-val[transition] for past,val in zip(old,result,strict=True)]
            mix = weak.fields.product((g[transition],zero,gs,zero,zero,gss),difference)
            for dst,term in zip(result,mix,strict=True):
                dst[transition] += term
    return tuple(result)


weak.fields.collar_jets = collar_jets


class R742Frame(weak.R740Frame):
    """Native all-column field on the complete changed source and true open collar."""


class R742Build(weak.R740Build):
    frame_type = R742Frame

    def __init__(self,baseline=weak.BASELINE,modes=8192,steps=12,order=48):
        super().__init__(baseline=baseline,modes=modes,steps=steps,order=order)
        self.integration_ell_breaks = np.unique(np.r_[self.integration_ell_breaks,
                  DEPTH_JOIN,CUTOFF,CUTOFF+WIDTH*np.array([.25,.5,.75,1.])])
        self.identity.update(source="R742 full native weak ring with nonflat basal guards",
                 depth_join=DEPTH_JOIN,guard_end=CUTOFF,guard_cutoff_width=WIDTH,
                 angular_taper=ANGULAR_RAMP,physical_U_coefficient=-1.,
                 core_fillet_unchanged=True,transfer_window_ell=[.04,.47])

    def geometry(self,r,s):
        r,s = np.broadcast_arrays(r,s)
        vals,angle = super().geometry(r,s)
        _,_,xr,_,xrr,_,ell = self.profile.read(r)
        use = (r>=physical.R0)&(ell<=CUTOFF+WIDTH)
        if not np.any(use):
            return vals,angle
        g,px,ps,pxx,pxs,pss = ring_jets(self.ring,ell[use],s[use])
        per = self.ring.length
        raw = (g,col(xr[use])*px,per*ps,
               col(xr[use]**2)*pxx+col(xrr[use])*px,per*col(xr[use])*pxs,per**2*pss)
        for dst,fresh in zip(vals,raw,strict=True):
            dst[use] = fresh
        return vals,angle

    def nodes(self,level,purpose):
        r,s = super().nodes(level,purpose)
        sh = {"train":.5,"validation":.319,"qualification":.173}[purpose]
        v = [-.84625,-.30675,.30675,.84625]
        for c in (.205,.846):
            for scale in (-1.,1.):
                for label,sgn in ((c,-1.),(c+.102,1.)):
                    v.extend(scale*(label+sgn*ANGULAR_RAMP*np.array([0.,sh,1.])))
        for scale in (-1.,1.):
            v.extend(scale*(1-ANGULAR_RAMP*np.array([0.,sh,1.])))
        v=np.asarray(v)
        extra = np.r_[(1+v)/self.ring.length,(3+self.ring.LU-v)/self.ring.length]
        return np.unique(np.r_[r,self.radius_at([DEPTH_JOIN*sh,DEPTH_JOIN,CUTOFF+sh*WIDTH,CUTOFF+WIDTH])]),np.unique(np.mod(np.r_[s,extra],1.))

    @property
    def seed_identity(self):
        info = super().seed_identity
        for name in ("r742_changed_sleeves.py","r742_native_tsqr.py","r742_native_disk_solver.py"):
            info["physics_sha256"][name] = hashlib.sha256((HERE/name).read_bytes()).hexdigest()
        return info
