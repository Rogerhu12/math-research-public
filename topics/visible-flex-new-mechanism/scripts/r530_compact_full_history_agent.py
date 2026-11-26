#!/usr/bin/env python3
"""Finite-scale R530 endpoint exploration from the original R56/R73 formulas.

Research implementation, not a certificate.  No stored profile coefficients,
old runs, response-rank claims, or frozen-geometry replacements are used.
All copies, all second history and the three exact ruling projections of the
third history enter one 27-state ODE.  Full third/fourth endpoints still require
their separate recovery after a candidate trajectory has been found.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import comb, cos, pi, sin, sqrt
import json
import time

import numpy as np
from numpy.polynomial.legendre import leggauss, legvander
from scipy.integrate import solve_ivp
import sympy as sp


class DomainExit(RuntimeError):
    pass


class Jet:
    """Value and first two true time derivatives (not Taylor coefficients)."""
    __array_priority__ = 10000
    def __init__(self, value, first=0.0, second=0.0):
        self.a = (np.asarray(value), np.asarray(first), np.asarray(second))

    @staticmethod
    def coerce(x):
        return x if isinstance(x, Jet) else Jet(x)

    def __add__(self, other):
        b = self.coerce(other).a
        return Jet(*(self.a[j] + b[j] for j in range(3)))

    __radd__ = __add__

    def __neg__(self):
        return Jet(*(-a for a in self.a))

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        a, b = self.a, self.coerce(other).a
        return Jet(a[0]*b[0], a[1]*b[0]+a[0]*b[1],
                   a[2]*b[0]+2*a[1]*b[1]+a[0]*b[2])

    __rmul__ = __mul__

    def reciprocal(self):
        a = self.a
        return Jet(1/a[0], -a[1]/a[0]**2,
                   2*a[1]**2/a[0]**3-a[2]/a[0]**2)

    def __truediv__(self, other):
        return self * self.coerce(other).reciprocal()

    def __rtruediv__(self, other):
        return self.coerce(other) / self

    def dt(self):
        # Its second derivative is unused everywhere below.
        return Jet(self.a[1], self.a[2], 0.0)


def jstack(values):
    values = [Jet.coerce(x) for x in values]
    out = []
    for order in range(3):
        arrays = np.broadcast_arrays(*(v.a[order] for v in values))
        out.append(np.stack(arrays, axis=-2))
    return Jet(*out)


def jdot(a, b):
    a, b = Jet.coerce(a), Jet.coerce(b)
    c = a*b
    return Jet(*(np.sum(x, axis=-2) for x in c.a))


def vdot(a, b):
    return np.sum(a*b, axis=-2)


def omega_apply(k, vector):
    """Omega(k) V for columns (T,N,B)."""
    if isinstance(vector, Jet):
        k = Jet.coerce(k)
        vv = [Jet(*(a[..., j, :] for a in vector.a)) for j in range(3)]
        return jstack((-k*vv[1], k*vv[0]+vv[2], -vv[1]))
    return np.stack((-k*vector[..., 1, :],
                     k*vector[..., 0, :]+vector[..., 2, :],
                     -vector[..., 1, :]), axis=-2)


@lru_cache(None)
def gauss_right_matrix(n):
    x, w = leggauss(n)
    v = legvander(x, n+1)
    ints = np.empty((n, n))
    ints[:, 0] = 1-x
    for j in range(1, n):
        ints[:, j] = (v[:, j-1]-v[:, j+1])/(2*j+1)
    coeff = ((2*np.arange(n)+1)/2)[:, None] * v[:, :n].T*w
    return x, w, ints@coeff


@lru_cache(None)
def bump_derivative_functions():
    q = sp.symbols("q")
    f = sp.exp(-1/(1-q*q))
    return tuple(sp.lambdify(q, sp.diff(f, q, j), "numpy")
                 for j in range(5))


def exact_copy_graph():
    """Sixteen disjoint 11-node positive graphs with identical 0..10 moments."""
    base = [Fraction(j-5, 12) for j in range(11)]
    shift_unit = Fraction(1, 10000)
    for _ in range(20):
        positions, weights = [], []
        for rotation in range(16):
            nodes = [t+rotation*shift_unit for t in base]
            wr = []
            for i, ti in enumerate(nodes):
                wi = Fraction(0)
                for x in base:
                    val = Fraction(1, 11)
                    for m, tm in enumerate(nodes):
                        if m != i:
                            val *= (x-tm)/(ti-tm)
                    wi += val
                wr.append(wi)
            positions.append(nodes)
            weights.append(wr)
        if all(w > 0 for row in weights for w in row):
            # Each entire 32-packet block has width 116*w < shift_unit.
            return positions, weights, float(shift_unit)/250
        shift_unit /= 2
    raise RuntimeError("No positive graph obtained; no candidate was run.")


def derivative_product(a, b, order):
    return sum(comb(order, j)*a[j]*b[order-j] for j in range(order+1))


def polynomial_jets(coefficients, x, count=4):
    c = np.asarray(coefficients, dtype=float)
    out = []
    for _ in range(count):
        out.append(np.polynomial.polynomial.polyval(x, c))
        c = np.arange(1, len(c))*c[1:] if len(c)>1 else np.array([0.])
    return out


@dataclass
class ProfileGrid:
    order: int = 24
    gap_order: int = 12
    center: float = 10.0

    def __post_init__(self):
        positions, weights, width = exact_copy_graph()
        self.width = width
        self.copy_positions = positions
        self.copy_weights = weights
        self.blocks = 176
        self.block_weights = np.array([float(weights[r][j])
                                      for r in range(16) for j in range(11)])
        offsets = np.array([self.center+float(positions[r][j])
                            for r in range(16) for j in range(11)])
        packet_centers = np.array([15*j+3*m-57 for j in range(8)
                                   for m in range(4)])*width
        self.segments = []
        nodes, quadrature, ids, mother_x = [], [], [], []
        fcoef, gcoef, rho4 = [], [], []
        cursor = 0
        for packet, pc in enumerate(packet_centers):
            if packet:
                left, right = packet_centers[packet-1]+width, pc-width
                n = self.gap_order
                xn, wn, jm = gauss_right_matrix(n)
                local = (left+right)/2+(right-left)/2*xn
                self.segments.append((slice(cursor, cursor+n), (right-left)/2, jm))
                nodes.extend(local); quadrature.extend((right-left)/2*wn)
                ids.extend([-1]*n); mother_x.extend([0.]*n)
                fcoef.extend([0.]*n); gcoef.extend([0.]*n); rho4.extend([0.]*n)
                cursor += n
            xn, wn, jm = gauss_right_matrix(self.order)
            self.segments.append((slice(cursor, cursor+self.order), width, jm))
            nodes.extend(pc+width*xn); quadrature.extend(width*wn)
            ids.extend([packet]*self.order); mother_x.extend(xn)
            macro, micro = divmod(packet, 4)
            amp = (-1)**macro*comb(7, macro)**(1/3)
            af = amp*(1 if micro==0 else sqrt(3) if micro==2 else 0)
            ag = amp*(sqrt(3) if micro==1 else 1 if micro==3 else 0)
            fcoef.extend([af]*self.order); gcoef.extend([ag]*self.order)
            rho4.extend([(af*af+ag*ag)**2]*self.order)
            cursor += self.order
        self.y = offsets[:, None]+np.asarray(nodes)[None, :]
        self.quad = np.asarray(quadrature)
        self.rho4 = np.broadcast_to(np.asarray(rho4), self.y.shape)
        active = np.array(ids)>=0
        mother_x = np.asarray(mother_x)
        raw = np.zeros((5, cursor))
        funcs = bump_derivative_functions()
        with np.errstate(over="ignore", under="ignore", invalid="raise"):
            for j, fun in enumerate(funcs):
                raw[j, active] = fun(mother_x[active])/width**j
        self.raw = np.broadcast_to(raw[:, None, :], (5, self.blocks, cursor)).copy()
        fbase, gbase = raw*np.asarray(fcoef), raw*np.asarray(gcoef)
        fs, gs = [], []
        for r in range(16):
            theta = (r % 8)*pi/4
            reflection = 1 if r<8 else -1
            fr = cos(theta)*fbase-sin(theta)*reflection*gbase
            gr = sin(theta)*fbase+cos(theta)*reflection*gbase
            for _ in range(11):
                fs.append(fr); gs.append(gr)
        self.f = np.stack(fs, axis=1)
        self.g = np.stack(gs, axis=1)
        _, ck = self.acceleration_coefficients(1., 0., 0.)
        if not (np.isfinite(ck) and ck>0):
            raise RuntimeError("Nonpositive raw Ck in profile construction.")
        amplitude = ck**(-.25)
        self.raw *= amplitude; self.f *= amplitude; self.g *= amplitude
        self.amplitude = amplitude
        self.q_basis = self._make_q_basis()
        y = self.y
        self.third_test = np.stack((self.g[4],
                                  y*self.g[4]+2*self.g[3],
                                  y*y*self.g[4]+4*y*self.g[3]))
        self.y_limits = (float(np.min(self.y)-width),
                         float(np.max(self.y)+width))

    def integral(self, f):
        arr = np.sum(f*self.quad, axis=-1)
        return np.sum(arr*self.block_weights, axis=-1)

    def right(self, f):
        """One true block right anchor; complete-block tails vanish by R521."""
        result = np.empty_like(f)
        suffix = np.zeros(f.shape[:-1])
        for sl, scale, jm in reversed(self.segments):
            vals = f[..., sl]
            result[..., sl] = scale*np.matmul(vals, jm.T)+suffix[..., None]
            suffix += np.sum(vals*self.quad[sl], axis=-1)
        return result

    def right_jet(self, f):
        return Jet(*(self.right(a) for a in f.a))

    def acceleration_coefficients(self, h, k, eta):
        d = h*eta-k
        e = h*self.y+d
        q = 1+e*e
        ff = q*self.raw[2]-2*h*e*self.raw[1]+2*h*h*self.raw[0]
        common = self.rho4*ff**4/q**2
        ch = self.integral((1-e*e-2*k*e)*common)/(3072*h**6)
        ck = self.integral(e*common)/(3072*h**5)
        return float(ch), float(ck)

    def _make_q_basis(self):
        f, g, x = self.f, self.g, self.y
        d0 = [derivative_product(f, f, j)-derivative_product(g, g, j)
              for j in range(4)]
        d01 = [derivative_product(f, f[1:], j)-derivative_product(g, g[1:], j)
               for j in range(4)]
        d11 = [derivative_product(f[1:], f[1:], j)
               -derivative_product(g[1:], g[1:], j) for j in range(4)]
        q22 = [derivative_product(f[2:], f[2:], j)
               -derivative_product(g[2:], g[2:], j) for j in range(3)]
        den0 = q22
        den1 = [x*q22[0], q22[0]+x*q22[1], 2*q22[1]+x*q22[2]]
        den2 = [x*x*q22[0]+2*d11[0],
                2*x*q22[0]+x*x*q22[1]+2*d11[1],
                2*q22[0]+4*x*q22[1]+x*x*q22[2]+2*d11[2]]
        tails = [[self.right(a[0]), -a[0], -a[1], -a[2]]
                 for a in (den0, den1, den2)]
        all_q = []
        for basis in np.eye(8):
            p0,p1,p2,t1,r1,s1,s0,r0 = basis
            t0 = p0/4+s1/2
            coeffs = ([ -p1/2, -p2 ],
                      [ p0, p1, p2 ],
                      [r1, s1-p0/2, t1-p1/2, -p2/2],
                      [r0, r1, -p0/4],
                      [s0, s1, -p1/4],
                      [t0, t1, -p2/4])
            factors = (d0, d01, d11, *tails)
            qjet = np.zeros((4, *x.shape))
            for coeff, factor in zip(coeffs, factors):
                cc = polynomial_jets(coeff, x)
                for j in range(4):
                    qjet[j] += derivative_product(cc, factor, j)
            all_q.append(qjet)
        return np.asarray(all_q)


def matrix_density(h, k, eta, gamma, upsilon):
    d = h*eta-k
    ds = gamma*eta-upsilon/2
    q = 1+d*d
    a1 = 2*k*eta-(k*k+1)/h
    a0 = k*eta*eta-(k*k+1)*eta/h
    p0, p1, p2 = -k*q/(2*h), -k*d, -k*h/2
    common = gamma*q/h-2*d*ds
    r0 = (a0*q+ds/h**2*common)/(8*h)
    r1 = (a1*q+gamma/h**2*common)/(8*h)
    s0 = (a0*d-ds*ds/h**2)/4
    s1 = (a1*d-gamma*ds/h**2)/4
    t1 = (h*a1-gamma*gamma/h**2)/8
    return np.array((p0,p1,p2,t1,r1,s1,s0,r0))


def phi_mixed(grid, m, f, q):
    """R69 Phi_m(f,q), retaining all three true right tails."""
    p0,p1,p2,t1,r1,s1,s0,r0 = m
    x = grid.y
    t0 = p0/4+s1/2
    a0 = -p1/2-p2*x
    a1 = p0+p1*x+p2*x*x
    a2 = r1+(s1-p0/2)*x+(t1-p1/2)*x*x-p2*x**3/2
    b0 = r0+r1*x-p0*x*x/4
    b1 = s0+s1*x-p1*x*x/4
    b2 = t0+t1*x-p2*x*x/4
    prod = f[2]*q[2]
    return (a0*f[0]*q[0]+a1*(f[0]*q[1]+f[1]*q[0])/2
            +a2*f[1]*q[1]+b0*grid.right(prod)
            +b1*grid.right(x*prod)
            +b2*grid.right(x*x*prod+2*f[1]*q[1]))


def first_numerator(grid, q, h, k, eta):
    """The first four x-jets of the R56 first-field numerator."""
    z, e = eta + grid.y, None
    e = h*z-k
    zero = q[0]*0
    return (jstack((-q[1]/2, zero, h*q[0]-e*q[1]/2)),
            jstack((-q[2]/2, zero, h*q[1]/2-e*q[2]/2)),
            jstack((-q[3]/2, zero, -e*q[3]/2)),
            jstack((-q[4]/2, zero, -h*q[3]/2-e*q[4]/2)))


def static_numerator(grid, q, h, k, eta):
    """Value x-jets 0..2 for a fixed profile with derivatives 0..3."""
    z, e = grid.y+eta, h*(grid.y+eta)-k
    zero = np.zeros_like(q[0])
    return (np.stack((-q[1]/2, zero, h*q[0]-e*q[1]/2), axis=-2),
            np.stack((-q[2]/2, zero, h*q[1]/2-e*q[2]/2), axis=-2),
            np.stack((-q[3]/2, zero, -e*q[3]/2), axis=-2))


def static_covariant(grid, q, h, k, eta, gamma, upsilon):
    """The exact fixed-profile covariant time derivatives of x-jets 0,1."""
    z = grid.y+eta
    es = gamma*z-upsilon/2
    zero = np.zeros_like(q[0])
    return (np.stack((zero, h*(q[0]-z*q[1]/2),
                      gamma*q[0]-es*q[1]/2), axis=-2),
            np.stack((zero, h*(q[1]/2-z*q[2]/2),
                      gamma*q[1]/2-es*q[2]/2), axis=-2))


def local_fields(grid, h0, k0, eta0, gamma0, upsilon0, a, b):
    """True second local field and its true time derivative, retaining tails."""
    h = Jet(h0, gamma0, a)
    k = Jet(k0, upsilon0, b)
    eta = Jet(eta0, upsilon0/(2*h0),
              b/(2*h0)-upsilon0*gamma0/(2*h0*h0))
    gamma = h.dt()
    es = gamma*(grid.y+eta)-k.dt()/2
    z, e = grid.y+eta, h*(grid.y+eta)-k
    vf = first_numerator(grid, grid.f, h, k, eta)
    vg = first_numerator(grid, grid.g, h, k, eta)
    cf = tuple(v.dt()+omega_apply(k, v) for v in vf[:3])
    cg = tuple(v.dt()+omega_apply(k, v) for v in vg[:3])

    def ddot(i, j):
        return jdot(vf[i], vf[j])-jdot(vg[i], vg[j])

    def cdot(i, j):
        return jdot(cf[i], vf[j])-jdot(cg[i], vg[j])

    tx = (ddot(1, 1), 2*ddot(1, 2),
          2*(ddot(2, 2)+ddot(1, 3)))
    p = (grid.right_jet(tx[0])/(2*h), -tx[0]/(2*h),
         -tx[1]/(2*h), -tx[2]/(2*h))
    bb = (ddot(0, 0)/(2*h), ddot(0, 1)/h,
          (ddot(1, 1)+ddot(0, 2))/h,
          (3*ddot(1, 2)+ddot(0, 3))/h)
    tsx = (cdot(0, 1), cdot(1, 1)+cdot(0, 2),
           cdot(2, 1)+2*cdot(1, 2)+cdot(0, 3))
    ee = tuple(-tsx[r]/(2*h)+(es*p[r+1]+r*gamma*p[r])/(2*h)
               +gamma*bb[r+1]/(2*h)-p[r].dt()/2 for r in range(3))
    vk = (jstack((ee[0]/h, z*p[0]+bb[0], e*ee[0]/h)),
          jstack((ee[1]/h, p[0]+z*p[1]+bb[1], ee[0]+e*ee[1]/h)),
          jstack((ee[2]/h, 2*p[1]+z*p[2]+bb[2],
                  2*ee[1]+e*ee[2]/h)))
    kvals = tuple(v.a[0] for v in vk)
    kc = tuple(v.a[1]+omega_apply(k0, v.a[0]) for v in vk[:2])
    gvals = tuple(v.a[0] for v in vg)
    gc = tuple(v.a[0] for v in cg)
    return gvals, gc, kvals, kc


def evaluate_local(grid, h, k, eta, gamma, upsilon, a, b, history,
                   want_ruling=True, want_third=True):
    """Original R56 ruling without T/chi; exact three R73 T derivatives."""
    gy, gc, kvals, kc = local_fields(grid, h, k, eta, gamma, upsilon, a, b)
    z = grid.y+eta
    e = h*z-k
    es = gamma*z-upsilon/2
    q = 1+e*e
    density = matrix_density(h, k, eta, gamma, upsilon)
    qa = np.einsum('i,ijbn->jbn', history, grid.q_basis)
    qm = np.einsum('i,ijbn->jbn', density, grid.q_basis)
    ruling, third = None, None

    if want_third:
        tx = vdot(gy[1], kvals[1])
        jj = vdot(gy[0], kvals[0])
        pp, bb = grid.right(tx)/(2*h), jj/(2*h)
        ps = grid.right(vdot(gc[1], kvals[1])+vdot(gy[1], kc[1]))/(2*h)-gamma*pp/h
        bs = (vdot(gc[0], kvals[0])+vdot(gy[0], kc[0]))/(2*h)-gamma*bb/h
        ts = vdot(gc[0], kc[0])
        geom = k*z*z-(k*k+1)*z/h
        ell = ts/(2*h*h)+geom*pp-es*ps/(h*h)+(k*z-(k*k+1)/h)*bb-gamma*bs/(h*h)
        je = grid.right(q*grid.g[2]*qm[2]+2*h*h*grid.g[1]*qm[1])
        psi = ((upsilon/(2*h)-gamma*k/(h*h))*grid.g[1]*qm[0]/4
               -gamma*q*grid.g[1]*qm[1]/(8*h**3)-es*je/(8*h**3))
        cc = ell-psi
        minus_ma = phi_mixed(grid, density, grid.g, qa)
        third = grid.integral(grid.third_test*(cc-minus_ma)[None, :, :])

    if want_ruling:
        ya = static_numerator(grid, qa, h, k, eta)
        ca = static_covariant(grid, qa, h, k, eta, gamma, upsilon)
        ym = static_numerator(grid, qm, h, k, eta)
        vv = tuple(kvals[j]-ya[j] for j in range(3))
        vc = tuple(kc[j]-ca[j]-ym[j] for j in range(2))
        tx = vdot(gy[1], vv[1])
        pp, bb = -grid.right(tx)/h, -vdot(gy[0], vv[0])/h
        px = tx/h
        pxx = (vdot(gy[2], vv[1])+vdot(gy[1], vv[2]))/h
        bx = -(vdot(gy[1], vv[0])+vdot(gy[0], vv[1]))/h
        bxx = -(vdot(gy[2], vv[0])+2*vdot(gy[1], vv[1])+vdot(gy[0], vv[2]))/h
        txxs = vdot(gc[1], vv[1])+vdot(gy[1], vc[1])
        ps = -grid.right(txxs)/h-gamma*pp/h
        psx = txxs/h-gamma*px/h
        tsx = -(vdot(gc[0], vv[1])+vdot(vc[0], gy[1]))
        tsxx = -(vdot(gc[1], vv[1])+vdot(gc[0], vv[2])
                 +vdot(vc[1], gy[1])+vdot(vc[0], gy[2]))
        ee = -tsx/(2*h)+es*px/(2*h)+gamma*bx/(2*h)-ps/2
        ex = -tsxx/(2*h)+(gamma*px+es*pxx)/(2*h)+gamma*bxx/(2*h)-psx/2
        wlocal_x = np.stack((ex/h, pp+z*px+bx, ee+e*ex/h), axis=-2)
        ruling = -grid.integral(vdot(vv[1], vv[1])+2*vdot(gy[1], wlocal_x))/h
    return ruling, third


ODD = np.array((0, 2, 7, 5))
EVEN = np.array((1, 3, 4, 6))


class R530ODE:
    def __init__(self, grid, nu):
        self.grid, self.nu = grid, np.asarray(nu, dtype=float)
        self.calls = 0
        self.max_acceleration = 0.

    def __call__(self, s, state):
        h,k,eta,gamma,upsilon = state[:5]
        if not np.all(np.isfinite(state)) or h <= 0:
            raise DomainExit(f"Nonpositive height or nonfinite state at s={s}")
        ylo = self.grid.y_limits[0]
        for sign in (1, -1):
            zlo = ylo+sign*eta
            if min(zlo, h*zlo-sign*k, h*h*zlo*zlo-1-k*k) <= 0:
                raise DomainExit(f"Legal common domain exited at s={s}")
        ap, tp, am, tm = state[5:13], state[13:16], state[16:24], state[24:27]
        fp, _ = evaluate_local(self.grid,h,k,eta,gamma,upsilon,0.,0.,ap,
                               want_third=False)
        fm, _ = evaluate_local(self.grid,h,-k,-eta,-gamma,upsilon,0.,0.,am,
                               want_third=False)
        dp, dm = h*eta-k, -h*eta+k
        wp = np.array(((1+dp*dp)/(4*h),dp/2,h/4))
        wm = np.array(((1+dm*dm)/(4*h),dm/2,h/4))
        fp -= 4*wp@tp+2*wp@self.nu
        fm -= 4*wm@tm+2*wm@self.nu
        hp,kp = self.grid.acceleration_coefficients(h,k,eta)
        hm,km = self.grid.acceleration_coefficients(h,-k,-eta)
        a,b = np.linalg.solve(np.array(((hp,kp),(hm,-km))), -np.array((fp,fm)))
        _, gp = evaluate_local(self.grid,h,k,eta,gamma,upsilon,a,b,ap,
                               want_ruling=False)
        _, gm = evaluate_local(self.grid,h,-k,-eta,-gamma,upsilon,a,-b,am,
                               want_ruling=False)
        result = np.zeros_like(state)
        result[:5] = gamma,upsilon,upsilon/(2*h),a,b
        result[5:13] = matrix_density(h,k,eta,gamma,upsilon)
        result[13:16] = gp
        result[16:24] = -matrix_density(h,-k,-eta,-gamma,upsilon)
        result[24:27] = -gm
        if len(state)>27:
            frame = state[27:36].reshape(3,3)
            om = np.array(((0.,-k,0.),(k,0.,1.),(0.,-1.,0.)))
            result[27:36] = (frame@om).ravel()
            result[36:39] = h*h*frame[:,0]
        self.calls += 1
        self.max_acceleration = max(self.max_acceleration,abs(a),abs(b))
        return result


def check_coefficients(grid):
    state = (1.17,.23,.08,.11,-.31)
    aa = np.array((.02,-.013,.017,.019,-.007,.011,-.009,.014))*grid.width
    r0,t0 = evaluate_local(grid,*state,0.,0.,aa)
    rh,th = evaluate_local(grid,*state,1.,0.,aa)
    rk,tk = evaluate_local(grid,*state,0.,1.,aa)
    coeff = grid.acceleration_coefficients(*state[:3])
    return {"geometry":state,"quadrature_order":grid.order,
            "packet_width":grid.width,"common_amplitude":grid.amplitude,
            "direct_coefficients":[float(rh-r0),float(rk-r0)],
            "positive_integral_coefficients":list(coeff),
            "relative_coefficient_error":float(np.linalg.norm(np.array((rh-r0,rk-r0))-coeff)/np.linalg.norm(coeff)),
            "local_ruling":float(r0),"third_derivative":t0.tolist(),
            "third_accel_derivatives":[(th-t0).tolist(),(tk-t0).tolist()]}


def integrate_candidate(grid,args):
    state = np.zeros(39)
    state[:5] = args.height,0.,0.,0.,args.speed
    state[5+ODD] = np.asarray(args.odd)*grid.width
    state[16+ODD] = np.asarray(args.odd)*grid.width
    state[27:36] = np.eye(3).ravel()
    ode = R530ODE(grid,args.nu)
    solution = solve_ivp(ode,(0.,args.length),state,rtol=args.rtol,atol=args.atol,
                         max_step=args.length/args.steps,dense_output=True,
                         method='DOP853')
    out = {"success":solution.success,"message":solution.message,
           "calls":ode.calls,"length":float(solution.t[-1]),
           "height":args.height,"speed":args.speed,"nu":args.nu,
           "initial_odd_scaled_by_width":args.odd,
           "final_geometry":solution.y[:5,-1].tolist(),
           "odd_endpoint":solution.y[5+ODD,-1].tolist(),
           "even_endpoint":solution.y[5+EVEN,-1].tolist(),
           "max_acceleration":ode.max_acceleration}
    sample = solution.sol(np.linspace(0,solution.t[-1],max(101,5*args.steps)))
    h,eta = sample[0],sample[2]
    frames = sample[27:36].T.reshape(-1,3,3)
    alpha = sample[36:39].T
    normals = frames[:,:,1]
    edges = []
    for edge in grid.y_limits:
        edges.append(alpha+h[:,None]/(edge+eta)[:,None]*normals)
        edges.append(alpha-h[:,None]/(edge-eta)[:,None]*normals)
    points = np.concatenate(edges,axis=0)
    c3 = (points[:,2].min()+points[:,2].max())/2
    radius = np.linalg.norm(points-np.array((0.,0.,c3)),axis=1).max()
    out["sampled_radius_about_B_axis_center"] = float(radius)
    out["B_axis_center"] = float(c3)
    out["sampled_height_range"] = [float(h.min()),float(h.max())]
    out["frame_orthogonality_defect"] = float(np.linalg.norm(frames[-1].T@frames[-1]-np.eye(3)))
    out["warning"] = "Finite quadrature/ODE evidence only; no exact root, fourth period, pose, or reach lower bound."
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode',choices=('check','integrate'))
    parser.add_argument('--order',type=int,default=24)
    parser.add_argument('--gap-order',type=int,default=12)
    parser.add_argument('--center',type=float,default=10.)
    parser.add_argument('--height',type=float,default=1.)
    parser.add_argument('--speed',type=float,default=1.)
    parser.add_argument('--length',type=float,default=1.e-4)
    parser.add_argument('--nu',type=float,nargs=3,default=(0.,0.,0.))
    parser.add_argument('--odd',type=float,nargs=4,default=(0.,0.,0.,0.))
    parser.add_argument('--rtol',type=float,default=1.e-6)
    parser.add_argument('--atol',type=float,default=1.e-9)
    parser.add_argument('--steps',type=int,default=4)
    args = parser.parse_args()
    started = time.time()
    grid = ProfileGrid(args.order,args.gap_order,args.center)
    if args.mode == 'check':
        out = check_coefficients(grid)
    else:
        out = integrate_candidate(grid,args)
    out['elapsed_seconds'] = time.time()-started
    print(json.dumps(out,ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()

