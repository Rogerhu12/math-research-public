"""R128: an exact flat-annulus tail, with actual Cartesian two-jets.

The mathematical map is defined by the integrals in R128.  This module evaluates
those integrals by Gauss--Legendre quadrature; quadrature error is not silently
identified with the exact definition.  No old nonflat metric or DN state is used.

Coordinates: material (r,u), upper meridian s=a-r, inward normal e1 cross e2.
The parameter ``phase`` rotates space and counter-rotates material u.  The whole
r <= flat_radius collar is fixed pointwise for every amplitude and phase.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
import numpy as np


@lru_cache(maxsize=8)
def _gauss(order):
    return np.polynomial.legendre.leggauss(int(order))


def smoothstep9(t):
    """C4 clipped step, with its first two derivatives in t."""
    t = np.asarray(t, dtype=float)
    q = np.clip(t, 0.0, 1.0)
    s = q**5 * (126.0 + q * (-420.0 + q * (540.0 + q * (-315.0 + 70.0*q))))
    inside = (t > 0.0) & (t < 1.0)
    first = np.where(inside, 630.0*q**4*(1.0-q)**4, 0.0)
    second = np.where(inside, 2520.0*q**3*(1.0-q)**3*(1.0-2.0*q), 0.0)
    return s, first, second


def _rotate(v, phase):
    c, s = np.cos(phase), np.sin(phase)
    z = np.array(v, copy=True)
    z[..., 0] = c*v[..., 0] - s*v[..., 1]
    z[..., 1] = s*v[..., 0] + c*v[..., 1]
    return z


@dataclass(frozen=True)
class FlatDevelopableTail:
    amplitude: float = 1.0
    cut_radius: float = 0.8
    cuff_radius: float = 0.32
    flat_radius: float = 0.34
    plane_height: float = 1.25
    quadrature_order: int = 96

    def __post_init__(self):
        if not (0 < self.cuff_radius < self.flat_radius < self.cut_radius):
            raise ValueError("Require 0 < cuff_radius < flat_radius < cut_radius")
        if not (0 <= self.amplitude < np.pi/2):
            raise ValueError("This embedded convex branch requires 0 <= amplitude < pi/2")

    @property
    def width(self):
        return self.cut_radius - self.flat_radius

    @property
    def exact_curvature_max(self):
        return self.amplitude * (315.0/128.0) / self.width

    def curve(self, y):
        """Unit-speed generating curve and exact local derivative formulas.

        X is odd, Z is even.  The returned X,Z and parameter derivatives are
        quadrature evaluations; alpha/kappa and local jets are direct formulas.
        The extension beyond cut_radius consists of tangent rays.
        """
        y = np.asarray(y, dtype=float)
        sign = np.sign(y)
        v = np.maximum(np.abs(y)-self.flat_radius, 0.0)/self.width
        v0 = np.minimum(v, 1.0)
        s, st, stt = smoothstep9(v)
        alpha = sign*self.amplitude*s
        alpha_A = sign*s
        kappa = self.amplitude*st/self.width
        kappa_A = st/self.width
        kappa_y = sign*self.amplitude*stt/self.width**2
        nodes, weights = _gauss(self.quadrature_order)
        q = v0[..., None]*(nodes+1.0)/2.0
        sq, _, _ = smoothstep9(q)
        angle = self.amplitude*sq
        scale = self.width*v0/2.0
        # cos(angle)-1 is evaluated without losing its small-amplitude part.
        dx = scale*(np.sum((-2*np.sin(angle/2)**2)*weights, axis=-1))
        z = scale*(np.sum(np.sin(angle)*weights, axis=-1))
        dx_A = scale*np.sum((-np.sin(angle)*sq)*weights, axis=-1)
        z_A = scale*np.sum((np.cos(angle)*sq)*weights, axis=-1)
        beyond = self.width*np.maximum(v-1.0, 0.0)
        dx += beyond*(np.cos(self.amplitude)-1.0)
        z += beyond*np.sin(self.amplitude)
        dx_A -= beyond*np.sin(self.amplitude)
        z_A += beyond*np.cos(self.amplitude)
        return dict(X=y+sign*dx, Z=z, X_A=sign*dx_A, Z_A=z_A,
                    alpha=alpha, alpha_A=alpha_A, kappa=kappa,
                    kappa_A=kappa_A, kappa_y=kappa_y,
                    cos_alpha=np.cos(alpha), sin_alpha=np.sin(alpha))

    def evaluate(self, r, u, *, phase=0.0):
        """Actual upper map, complete (s,u) and (r,u) two-jets and shape.

        All shape entries are orthonormal (e1=X_s,e2=X_u/r).  In particular,
        n or l may vanish: this function does not divide by either quantity.
        ``gc_values`` follows the existing [n,m,X,e1,e2,N] layout.
        """
        r, u = np.broadcast_arrays(np.asarray(r, float), np.asarray(u, float))
        th = u-phase
        sn, cs = np.sin(th), np.cos(th)
        curve = self.curve(r*sn)
        ca, sa = curve['cos_alpha'], curve['sin_alpha']
        kappa = curve['kappa']
        zeros, ones = np.zeros_like(r), np.ones_like(r)
        ex = np.stack((ones, zeros, zeros), axis=-1)
        tangent = np.stack((zeros, ca, -sa), axis=-1)
        normal = np.stack((zeros, -sa, -ca), axis=-1)
        tangent_y = kappa[..., None]*normal
        X = np.stack((r*cs, curve['X'], self.plane_height-curve['Z']), axis=-1)
        Xr = cs[..., None]*ex+sn[..., None]*tangent
        Xu = r[..., None]*(-sn[..., None]*ex+cs[..., None]*tangent)
        Xrr = sn[..., None]**2*tangent_y
        Xru = -sn[..., None]*ex+cs[..., None]*tangent+(r*sn*cs)[..., None]*tangent_y
        Xuu = (-r*cs)[..., None]*ex+(-r*sn)[..., None]*tangent+(r*r*cs*cs)[..., None]*tangent_y
        vectors = dict(X=X, X_r=Xr, X_u=Xu, X_rr=Xrr, X_ru=Xru, X_uu=Xuu,
                       X_s=-Xr, X_ss=Xrr, X_su=-Xru,
                       e1=-Xr, e2=Xu/r[..., None], N=normal)
        vectors = {key: _rotate(value, phase) for key, value in vectors.items()}
        l, m, n = kappa*sn*sn, -kappa*sn*cs, kappa*cs*cs
        result = dict(vectors, r=r, u=u, phase=phase, alpha=curve['alpha'],
                      kappa=kappa, l=l, m=m, n=n,
                      outward_normal=-vectors['N'], H=curve['Z'])
        result['gc_values'] = np.concatenate((n[...,None], m[...,None], vectors['X'],
                                              vectors['e1'], vectors['e2'], vectors['N']),axis=-1)
        result['height_jet'] = dict(
            H=curve['Z'], Hr=sn*sa, Hu=r*cs*sa,
            Hrr=sn*sn*kappa*ca,
            Hru=cs*sa+r*sn*cs*kappa*ca,
            Huu=-r*sn*sa+r*r*cs*cs*kappa*ca)
        return result

    def amplitude_jvp(self, r, u, *, phase=0.0):
        """Exact amplitude derivative formulas; only position integrals use GL."""
        r, u = np.broadcast_arrays(np.asarray(r, float), np.asarray(u, float))
        sn, cs = np.sin(u-phase), np.cos(u-phase)
        q = self.curve(r*sn)
        zeros = np.zeros_like(r)
        tangent = np.stack((zeros, q['cos_alpha'], -q['sin_alpha']), axis=-1)
        normal = np.stack((zeros, -q['sin_alpha'], -q['cos_alpha']), axis=-1)
        d_tangent = q['alpha_A'][...,None]*normal
        d_normal = -q['alpha_A'][...,None]*tangent
        d_tangent_y = q['kappa_A'][...,None]*normal+q['kappa'][...,None]*d_normal
        dX = np.stack((zeros, q['X_A'], -q['Z_A']),axis=-1)
        dXr = sn[...,None]*d_tangent
        dXu = (r*cs)[...,None]*d_tangent
        dXrr = sn[...,None]**2*d_tangent_y
        dXru = cs[...,None]*d_tangent+(r*sn*cs)[...,None]*d_tangent_y
        dXuu = (-r*sn)[...,None]*d_tangent+(r*r*cs*cs)[...,None]*d_tangent_y
        vec = dict(X=dX, X_r=dXr, X_u=dXu, X_rr=dXrr, X_ru=dXru, X_uu=dXuu,
                   X_s=-dXr, X_ss=dXrr, X_su=-dXru, e1=-dXr,
                   e2=dXu/r[...,None], N=d_normal)
        vec = {key:_rotate(value,phase) for key,value in vec.items()}
        l, m, n = q['kappa_A']*sn*sn, -q['kappa_A']*sn*cs, q['kappa_A']*cs*cs
        vec.update(l=l,m=m,n=n)
        vec['gc_values'] = np.concatenate((n[...,None],m[...,None],vec['X'],vec['e1'],vec['e2'],vec['N']),axis=-1)
        return vec

    def cut_port(self, u, *, phase=0.0):
        return self.evaluate(self.cut_radius,u,phase=phase)

    def real_height_coefficients(self, modes=32, angles=8192):
        u = 2*np.pi*np.arange(int(angles))/int(angles)
        h = self.cut_port(u)['H']
        return dict(mean=float(h.mean()),
                    real_even_cosine=[float(2*np.mean(h*np.cos(2*k*u))) for k in range(1,int(modes)+1)])
