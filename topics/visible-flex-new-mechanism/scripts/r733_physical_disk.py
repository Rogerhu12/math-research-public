"""R733 entire fixed-source disk in the R732 Cartesian chart, with the real S inserted."""
import hashlib
from pathlib import Path

import numpy as np

from r688_actual_r664_window_collars import mollifier_cdf
from r732_compensated_pulses import B0, gate
from r732_disk_fields import Frame, rotation
from r688_true_caps_and_reference_sections import sym_step
from r732_physical_disk import A, ANGULAR_KNOTS, DU, L, R0, W, Build
from r733_inserted_meridian import ANGLE, BUFFER, LEG, LENGTH, START_X, InsertedMeridian


S_START = A + BUFFER
FILLET_START = S_START + LENGTH
TOTAL = FILLET_START + L


def material_breaks(shift):
    """Physical arclength since the original giving circle. Include every real break."""
    split = [0., A, S_START, FILLET_START, TOTAL]
    for start, width in ((S_START,LEG),(S_START+LEG,2*LEG),(S_START+3*LEG,LEG)):
        cuts = np.array([0.,.0005,.0015,.5,.9985,.9995,1.])
        split.extend(start + width*cuts)
        if shift is not None:
            split.extend(start + width*(cuts[:-1] + shift*np.diff(cuts)))
    f = np.asarray(ANGULAR_KNOTS)
    split.extend(FILLET_START + L*f)
    if shift is not None:
        split.extend(FILLET_START + L*(f[:-1] + shift*np.diff(f)))
    return np.unique(np.clip(split,0.,TOTAL))


class R733Profile:
    def __init__(self, old, order):
        self.old = old
        self.s = InsertedMeridian(order)
        self.ub = old.ub
        self.endx = old.endx + self.s.fillet_translation
        self.order = order

    def read(self, r):
        r = np.asarray(r, dtype=float)
        t = np.clip((r-R0)/(1-R0),0.,1.)
        c = DU*(1-R0)/R0
        h = TOTAL-c
        ell = (1-t)*(c+h*(1+t+t*t))
        dr = -(c+3*h*t*t)/(1-R0)
        ddr = -6*h*t/(1-R0)**2
        # The R732 ring left normal is outward. Its geometry uses gamma-u*N,
        # hence the native R733 signed inward distance is passed unchanged.
        x = W+ell
        u = np.zeros_like(r)
        xl = np.ones_like(r)
        ul = np.zeros_like(r)
        xll = np.zeros_like(r)
        ull = np.zeros_like(r)
        shape = r.shape
        # Keep scalar and array input contracts identical to the physical disk.
        e, x, u, xl, ul, xll, ull = [
            np.asarray(z).reshape(-1) for z in (ell,x,u,xl,ul,xll,ull)]
        m = (e>S_START) & (e<=FILLET_START)
        if np.any(m):
            local = np.clip(e[m]-S_START,0.,LENGTH)
            for dst, values in zip((x,u,xl,ul,xll,ull), self.s.profile(local), strict=True):
                dst[m] = values
        bend = e>FILLET_START
        if np.any(bend):
            local = np.clip(e[bend]-FILLET_START,0.,L)
            z, inv = np.unique(local,return_inverse=True)
            ids = np.clip(np.searchsorted(self.old.nodes,z,side="right")-1,0,len(self.old.nodes)-2)
            pos = np.empty((len(z),2))
            for i in np.unique(ids):
                take = ids==i
                pos[take] = self.old.prefix[i] + self.old.inc(self.old.nodes[i],z[take])
            p = pos[inv.reshape(-1)]
            x[bend] = START_X + self.s.advance + p[:,0]
            u[bend] = p[:,1]
            y = local/L
            angle = (np.pi/2)*sym_step(y)
            curv = (np.pi/2)*(mollifier_cdf((y-.001)/.0005)-mollifier_cdf((y-.999)/.0005))/(.998*L)
            # The true fillet has a constant vertical open end.
            cc = np.where(y>=.9995,0.,np.cos(angle))
            ss = np.where(y>=.9995,1.,np.sin(angle))
            xl[bend],ul[bend] = cc,ss
            xll[bend],ull[bend] = -curv*ss,curv*cc
        x,u,xl,ul,xll,ull = [z.reshape(shape) for z in (x,u,xl,ul,xll,ull)]
        return x,u,xl*dr,ul*dr,xll*dr**2+xl*ddr,ull*dr**2+ul*ddr,ell


class R733Frame(Frame):
    """Rotate each native S generator through the fixed-g active-pulse angle."""
    def __init__(self, build, phase, r, s, degree):
        super().__init__(build,phase,r,s,degree)
        if phase == 0:
            return
        x,u,xr,ur,xrr,urr,ell = build.profile.read(self.r)
        mask = (ell>S_START) & (ell<FILLET_START)
        if not np.any(mask):
            return
        ss = self.s[mask]
        ring = build.target(phase)
        _, kind, v = ring.label(ss)
        prim = (kind==0)|(kind==2)
        if not np.any(prim):
            return
        # All active main-pulse interiors are on this plateau. The two U arcs
        # and neighborhoods of the stationary joins have eta=0.
        dv = np.where(kind==0,ring.length,np.where(kind==2,-ring.length,0.))
        # Keep the same ratio across the long zero-curvature primary plateaus.
        # Only the two actual terminal straight intervals taper back to the U shape.
        a = (abs(v)-.949)/.05
        az = (1-gate(a))*prim
        az_s = -gate(a,1)*np.sign(v)*dv/.05
        ratio = B0/(B0+phase*.920/(.100*.998))
        rho = 1+(ratio-1)*az
        rho_s = (ratio-1)*az_s
        local = np.clip(ell[mask]-S_START,0.,LENGTH)
        theta, curve, unused = build.profile.s.angle_jet(local)
        st, ct = np.sin(theta),np.cos(theta)
        cc = np.sqrt(1-(rho*st)**2)
        # ell is decreasing in r. The actual source S is unit-speed in ell.
        ell_r = -np.hypot(xr[mask],ur[mask])
        angle = np.where(az==0,0.,np.arcsin(rho*st)-theta)
        angle_r = np.where(az==0,0.,(rho*ct/cc-1)*curve*ell_r)
        angle_s = rho_s*st/cc
        _,T,N,k,_ = ring.jets(ss)
        count = len(ss)
        E = np.zeros((count,3,3)); E[:,0,0]=1
        E[:,1:,1]=T; E[:,1:,2]=N
        Es = np.zeros_like(E)
        Es[:,1:,1]=(k*ring.length)[:,None]*N
        Es[:,1:,2]=-(k*ring.length)[:,None]*T
        V,D = rotation(angle,1)
        Et = np.swapaxes(E,-1,-2)
        K = E@V@Et
        Kt = E@D@Et
        Ks = Es@V@Et + E@V@np.swapaxes(Es,-1,-2) + angle_s[:,None,None]*Kt
        # Outside the angular transition, the identity must stay exactly the
        # already-paid rigid U frame. Skip zero masks rather than multiply E E^T.
        keep = az!=0
        idx = np.flatnonzero(mask)[keep]
        base = self.base[idx]
        self.br[idx] = (angle_r[:,None,None]*Kt)[keep]@base + K[keep]@self.br[idx]
        self.bs[idx] = Ks[keep]@base + K[keep]@self.bs[idx]
        self.base[idx] = K[keep]@base


class R733Build(Build):
    """Same compensated boundary pulses, independent whole physical source and receipt identity."""
    frame_type = R733Frame

    def __init__(self, baseline=.100, modes=8192, steps=12, order=48):
        super().__init__(baseline=baseline,modes=modes,steps=steps,order=order)
        self.profile = R733Profile(self.profile,order)
        self.integration_ell_breaks = material_breaks(None)
        self.identity.update(source="R733 circumferential reverse meridians",
                             reverse_start_x=START_X,reverse_leg=LEG,reverse_angle=ANGLE,
                             straight_buffer=BUFFER,reverse_length=LENGTH,
                             meridian_to_core=TOTAL,fillet_start_ell=FILLET_START,
                             true_fillet_x_translation=self.profile.s.fillet_translation)

    def radius_at(self, ell):
        target = np.asarray(ell,dtype=float)
        if np.any((target<0)|(target>TOTAL+1.e-14)):
            raise ValueError("arclength outside the whole R733 meridian")
        lo = np.zeros_like(target)
        hi = np.ones_like(target)
        c = DU*(1-R0)/R0
        h = TOTAL-c
        for _ in range(54):
            mid = (lo+hi)/2
            gap = (1-mid)*(c+h*(1+mid+mid*mid))
            lo = np.where(gap>target,mid,lo)
            hi = np.where(gap>target,hi,mid)
        return R0+(1-R0)*(lo+hi)/2

    def nodes(self, level, purpose):
        r,s = super().nodes(level,purpose)
        shift = {"train":.5,"validation":.319,"qualification":.173}[purpose]
        actual = self.radius_at(material_breaks(shift))
        z = np.array([0.,.002,.004,.5,.996,.998,1.])
        z = np.r_[z,z[:-1]+shift*np.diff(z)]
        vv = .949 + .05*z
        vv = np.r_[-vv,vv]
        angles = np.r_[(vv+1)/self.ring.length,(3+self.ring.LU-vv)/self.ring.length]
        return np.unique(np.r_[r,actual]), np.unique(np.r_[s,np.mod(angles,1.)])

    @property
    def seed_identity(self):
        data = super().seed_identity
        here = Path(__file__).resolve().parent
        for name in ("r733_inserted_meridian.py","r733_physical_disk.py"):
            data["physics_sha256"][name] = hashlib.sha256((here/name).read_bytes()).hexdigest()
        return data
