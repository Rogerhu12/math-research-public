"""R743 weak-source disk with an early long S and its forced cylindrical sectors."""
import hashlib
import importlib.util
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
EARLY = .050
LENGTH = .552
LEG = .138
BASE_LEG = .018
STRETCH = LEG/BASE_LEG
FORCED_END = EARLY + LEG*.0005
CUTOFF = .035
CUTOFF_WIDTH = .010
WEIGHT_START, WEIGHT_WIDTH = .145, .410
R740_PINS = {
    "r740_weak_material_disk.py": "0dbb3fb63f941f733f62350b9e3063c773df1f07b210d51f29ff4adc16ec96cb",
    "r740_material_rotation_space.py": "6121a9463ce13505177387b40e59a6fd2ea5d983d4f12d2b856592768bd66a94",
}


def pinned(name):
    path = HERE/name
    if hashlib.sha256(path.read_bytes()).hexdigest() != R740_PINS[name]:
        raise ValueError("different underlying native operator: "+name)
    spec = importlib.util.spec_from_file_location("_r743_"+path.stem,path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


weak = pinned("r740_weak_material_disk.py")
space = pinned("r740_material_rotation_space.py")
gate = weak.pulse.gate
space.GLOBAL_BREAKS = np.array([0.,.050,.119,.188,.326,.464,.533,.602,.662,.721,space.TOTAL])
space.FILLET_BREAKS = np.array([.030,.140,.235,.326,.425,.530,.602,.663,.719,space.TOTAL])
space.NP_GLOBAL = len(space.GLOBAL_BREAKS)+2
space.NP_LOCAL = len(space.FILLET_BREAKS)+2
weak.S_START,weak.LENGTH,weak.LEG = EARLY,LENGTH,LEG
weak.GLOBAL_BREAKS,weak.FILLET_BREAKS = space.GLOBAL_BREAKS,space.FILLET_BREAKS
original_psi = weak.physical.physical_psi


def early_psi(d, order):
    """The original true profile on [0,.035] and zero after .045, with two derivatives."""
    d = np.asarray(d,dtype=float)
    x = d.ravel()
    out = [np.zeros_like(x) for i in range(3)]
    active = x < CUTOFF+CUTOFF_WIDTH
    if np.any(active):
        y = x[active]
        p,pd,pdd = original_psi(y,order)
        z = (y-CUTOFF)/CUTOFF_WIDTH
        f = 1-gate(z)
        fd = -gate(z,1)/CUTOFF_WIDTH
        fdd = -gate(z,2)/CUTOFF_WIDTH**2
        for target,value in zip(out,(p*f,pd*f+p*fd,pdd*f+2*pd*fd+p*fdd),strict=True):
            target[active] = value
    return tuple(t.reshape(d.shape) for t in out)


weak.physical.physical_psi = early_psi
weak.fields.physical_psi = early_psi


def physical_breaks(shift=None):
    unit = np.array([0.,.0005,.0015,.5,.9985,.9995,1.])
    if shift is not None:
        unit = np.sort(np.r_[unit,unit[:-1]+shift*np.diff(unit)])
    splits = [0.,CUTOFF,CUTOFF+CUTOFF_WIDTH,EARLY,EARLY+LENGTH,weak.FILLET_START,space.TOTAL]
    for begin,width in ((EARLY,LEG),(EARLY+LEG,2*LEG),(EARLY+3*LEG,LEG)):
        splits.extend(begin+width*unit)
    splits.extend(weak.FILLET_START+weak.physical.L*unit)
    z = np.array([0.,.002,.004,.5,.996,.998,1.])
    if shift is not None:
        z = np.sort(np.r_[z,z[:-1]+shift*np.diff(z)])
    for begin,width in ((CUTOFF,CUTOFF_WIDTH),(FORCED_END,.040),
                        (WEIGHT_START,WEIGHT_WIDTH),(space.FILLET_BREAKS[0],.040)):
        splits.extend(begin+width*z)
    return np.unique(splits)


weak.material_breaks = physical_breaks


class LongMeridian:
    """Dilation of the C3 reference angle and both integrated profile coordinates."""
    def __init__(self, original):
        self.original = original
        self.advance = STRETCH*original.advance

    def native(self, ell):
        return np.clip(np.asarray(ell)/STRETCH,0.,4*BASE_LEG)

    def angle_jet(self, ell):
        th,k,ks = self.original.angle_jet(self.native(ell))
        return th,k/STRETCH,ks/STRETCH**2

    def profile(self, ell):
        x,u,xl,ul,xll,ull = self.original.profile(self.native(ell))
        return (weak.physical.W+EARLY+(x-weak.START_X)*STRETCH,STRETCH*u,
                xl,ul,xll/STRETCH,ull/STRETCH)


class EarlyProfile:
    def __init__(self, old):
        self.previous = old
        self.s = LongMeridian(old.s)
        self.order = old.order
        self.ub = old.ub
        self.fillet_shift = weak.physical.W+EARLY+self.s.advance-(weak.START_X+old.s.advance)
        self.endx = old.endx+self.fillet_shift

    def read(self, r):
        r = np.asarray(r,dtype=float)
        shape = r.shape
        r = r.ravel()
        ell,er,err = space.ell_data(r)
        x = weak.physical.W+ell
        u = np.zeros_like(ell)
        xl,ul = np.ones_like(ell),np.zeros_like(ell)
        xll,ull = np.zeros_like(ell),np.zeros_like(ell)
        on_s = (ell>EARLY)&(ell<=weak.FILLET_START)
        if np.any(on_s):
            local = np.clip(ell[on_s]-EARLY,0.,LENGTH)
            for dst,value in zip((x,u,xl,ul,xll,ull),self.s.profile(local),strict=True):
                dst[on_s] = value
        xr,ur = xl*er,ul*er
        xrr,urr = xll*er**2+xl*err,ull*er**2+ul*err
        bend = ell>weak.FILLET_START
        if np.any(bend):
            old = self.previous.read(r[bend])
            for dst,v in zip((x,u,xr,ur,xrr,urr),old[:6],strict=True):
                dst[bend] = v
            x[bend] += self.fillet_shift
        return tuple(t.reshape(shape) for t in (x,u,xr,ur,xrr,urr,ell))


def fixed_radius_weight(r):
    ell,er,err = space.ell_data(r)
    v = (ell-WEIGHT_START)/WEIGHT_WIDTH
    return (gate(v),gate(v,1)*er/WEIGHT_WIDTH,
            gate(v,2)*(er/WEIGHT_WIDTH)**2+gate(v,1)*err/WEIGHT_WIDTH)


def native_columns(frame, build):
    space.install(frame,build)
    ell,er,_ = space.ell_data(frame.r)
    _,kind,v = build.ring.label(frame.s)
    w,wv,_ = weak.physical.native_w(v)
    vs = np.where(kind==0,build.ring.length,np.where(kind==2,-build.ring.length,0.))
    w = np.where(vs==0,0.,w)
    ws = wv*vs
    z = (ell-FORCED_END)/.040
    f = gate(z)
    mask = w+(1-w)*f
    mask_r = (1-w)*gate(z,1)*er/.040
    mask_s = ws*(1-f)
    original = frame.B
    frame.Br = mask[:,None]*frame.Br+mask_r[:,None]*original
    frame.Bs = mask[:,None]*frame.Bs+mask_s[:,None]*original
    frame.B = mask[:,None]*original


weak.install = native_columns


class R743Frame(weak.R740Frame):
    """Three native rotation axes on the R743 material and its unchanged sectors."""


class R743Build(weak.R740Build):
    frame_type = R743Frame

    def __init__(self,baseline=weak.BASELINE,modes=8192,steps=12,order=48):
        super().__init__(baseline=baseline,modes=modes,steps=steps,order=order)
        self.profile = EarlyProfile(self.profile)
        self.integration_ell_breaks = np.unique(np.r_[self.integration_ell_breaks,physical_breaks(),
               space.GLOBAL_BREAKS,space.FILLET_BREAKS])
        self.identity.update(source="R743 weak early long reverse meridian directly followed by the fillet",
                a=CUTOFF,reverse_start_x=weak.physical.W+EARLY,early_ell=EARLY,
                straight_buffer=EARLY-(CUTOFF+CUTOFF_WIDTH),
                bump_flat_after=CUTOFF+CUTOFF_WIDTH,
                post_s_straight=0.,reverse_length=LENGTH,reverse_leg=LEG,meridian_stretch=STRETCH,
                forced_end_ell=FORCED_END,
                true_fillet_x_translation=weak.physical.W+EARLY+self.profile.s.advance-
                    (weak.physical.W+weak.physical.A),
                transfer_window_ell=[WEIGHT_START,WEIGHT_START+WEIGHT_WIDTH],
                all_column_radial_knots=space.GLOBAL_BREAKS.tolist(),
                pulse_radial_knots=space.FILLET_BREAKS.tolist())

    def nodes(self,level,purpose):
        r,s = super().nodes(level,purpose)
        direct = np.array([-.84625,-.30675,.30675,.84625])
        primary = np.r_[(direct+1)/self.ring.length,(3+self.ring.LU-direct)/self.ring.length]
        us = np.array([.0005,.01,.25,.5,.75,.99,.9995])
        ends = np.r_[(2+self.ring.LU*us)/self.ring.length,(4+self.ring.LU+self.ring.LU*us)/self.ring.length]
        return np.unique(np.r_[r,self.radius_at([.021,FORCED_END])]),np.unique(np.mod(np.r_[s,primary,ends],1.))

    @property
    def seed_identity(self):
        info = super().seed_identity
        for name in ("r742_native_tsqr.py","r743_early_material_disk.py","r743_native_disk_solver.py"):
            info["physics_sha256"][name] = hashlib.sha256((HERE/name).read_bytes()).hexdigest()
        return info
