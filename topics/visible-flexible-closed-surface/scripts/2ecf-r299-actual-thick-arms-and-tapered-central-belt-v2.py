#!/usr/bin/env python3
"""Reconstructed R302 cylinder and two rigid bent fingers, with the C2 pair of holding-frame parameters.

The mathematical construction is unchanged. This source has a new byte identity.
Normals called N are outward in the original horizontal cylinder section, not axial z.
"""
import argparse
import hashlib
import json
from math import cos, pi, sin, sqrt
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.special import beta, betainc

R = 23 / 200
A_ROOT = 233 / 1000
FLAT = 117 / 500
SMALL = 1 / 250
ROOT_H = R * (1 + SMALL * pi / 2)
TUBE = A_ROOT - ROOT_H
TIP_J = beta(.75, .5) / 2
TIP_G = (TUBE - R) / TIP_J
TIP_H = R + 2 * TIP_G
K0 = .2
K1 = (pi - 1.5 * K0) / (pi - 1.5)
ORIGINAL = ((.127, .24, .52, "s5"), (-1.117, .24, .89, "s5"))
NEW_C2 = ((-.3, .24, .85, "s5"), (0., .24, .35, "short"))


def smooth(t):
    return t**3 * (10 + t * (-15 + 6*t))


def angle_integral(v):
    x = np.clip((v - .5) / .5, 0., 1.)
    integral = x * betainc(8, 8, x) - .5 * betainc(9, 8, x)
    return K0*v + (K1-K0) * (.5 * integral + np.maximum(v-1., 0.))


def quarter_integral(fn, end):
    points = [u for u in (.5, 1.) if 0 < u < end]
    return quad(lambda u: fn(angle_integral(u)), 0, end, points=points,
                epsabs=1e-13, epsrel=2e-13)[0]


A_CENTER = quarter_integral(sin, pi/2)
B_CENTER = quarter_integral(cos, pi/2)


def unmodified_gamma(u):
    t = float(u % (2*pi))
    q = int(t // (pi/2)) % 4
    a = t - q * pi/2
    end = pi/2-a if q % 2 else a
    x = A_CENTER - quarter_integral(sin, end)
    y = quarter_integral(cos, end)
    return np.array((x if q in (0, 3) else -x, y if q < 2 else -y, 0.))


def rotation(p, angle):
    p = np.asarray(p)
    c, s = cos(angle), sin(angle)
    return np.stack((c*p[..., 0] - s*p[..., 1], s*p[..., 0] + c*p[..., 1],
                     p[..., 2]), axis=-1)


class Port:
    def __init__(self, index):
        self.idx = index
        self.k = (K0, K1)[index]
        self.width = (.249, .30)[index]
        self.u = .25 + index*pi/2
        self.L = self.width - FLAT
        self.e = self.L/20
        self.level = self.k * (self.width/self.L - .025) / .95
        self.axes = np.array((0., 0., 1.))
        self.hflat = self.bevel(0.)

    def lam(self, x):
        x = abs(x)
        if x <= FLAT:
            return 0.
        q, e = self.level, self.e
        if x < FLAT + e:
            t = (x-FLAT)/e
            return q*e*t**3*(1-t/2)
        if x <= self.width-e:
            return q*(x-FLAT-e/2)
        if x < self.width:
            t = (x-self.width+e)/e
            return q*(self.L-1.5*e)+e*(q*t+(self.k-q)*t**3*(1-t/2))
        return self.k*x

    def old(self, x):
        return -self.k*x*x / (1 + np.sqrt(1-(self.k*x)**2))

    def bevel(self, x):
        x = abs(x)
        if x >= self.width:
            return self.old(x)
        x = max(x, FLAT)
        interior = [t for t in (FLAT+self.e, self.width-self.e) if x < t < self.width]
        def slope(t):
            v = self.lam(t)
            return v/sqrt(1-v*v)
        return self.old(self.width) + quad(slope, x, self.width, points=interior,
                                         epsabs=2e-14, epsrel=2e-13)[0]

    def frame(self, phase):
        beta0 = self.idx*pi/2 + self.k*(.25-phase)
        normal = np.array((cos(beta0), sin(beta0), 0.))
        tangent = np.array((-sin(beta0), cos(beta0), 0.))
        center = (np.array((A_CENTER-1/self.k, 0., 0.)) if self.idx == 0 else
                  np.array((0., B_CENTER-1/self.k, 0.)))
        return rotation(center+normal/self.k, phase), rotation(normal, phase), rotation(tangent, phase)

    def local_offset(self, u):
        off = (np.asarray(u)-self.u+pi) % (2*pi)-pi
        return off, np.sin(self.k*off)/self.k

    def mother(self, phase, z, u):
        point, normal, tangent = self.frame(phase)
        _, x = self.local_offset(u)
        if np.ndim(x):
            bend = np.array([self.bevel(float(item)) for item in np.ravel(x)]).reshape(x.shape)
        else:
            bend = self.bevel(float(x))
        old = self.old(x)
        w = smooth(np.clip((.77-abs(z))/.30, 0, 1))
        y = old + w*(bend-old)
        return point + x[..., None]*tangent + y[..., None]*normal + z*self.axes


def turn(t, omega, law):
    if law == "s5":
        return omega * smooth(t)
    if law != "short":
        raise ValueError("Choose the s5 or short bend")
    e = .05
    if t < e:
        v = t/e
        value = e*v**3*(1-v/2)
    elif t <= 1-e:
        value = t-e/2
    else:
        v = (1-t)/e
        value = 1-e-e*v**3*(1-v/2)
    return omega * value/(1-e)


def surface_rings(index, law="s5", omega=None, first=.24, last=None, n=40):
    """Rows are center displacement in (normal,tangent), circle radius, and axis turn angle."""
    if omega is None:
        omega = ORIGINAL[index][0]
    if last is None:
        last = ORIGINAL[index][2]
    length = .78 if law == "s5" else .43
    th = np.linspace(0, pi/2, n)
    rho = A_ROOT - R*(np.sin(th) + SMALL*pi/2*betainc(.25, .75, np.sin(th)**2))
    height = R*(1-np.cos(th) + SMALL*pi/2*betainc(.75, .25, np.sin(th)**2))
    rings = [[float(d), 0., float(r), 0.] for d, r in zip(height, rho)]
    rings.extend([ROOT_H+t*first, 0., TUBE, 0.] for t in np.linspace(0, 1, n)[1:])
    def arc(t, fn):
        stops = [v for v in (.05, .95) if v < t] if law == "short" else []
        return length*quad(lambda v: fn(turn(v, omega, law)), 0., t, points=stops,
                           epsabs=2e-13, epsrel=2e-13)[0]
    for t in np.linspace(0, 1, n)[1:]:
        rings.append([ROOT_H+first+arc(t, cos), arc(t, sin), TUBE, turn(t, omega, law)])
    d, y = rings[-1][:2]
    c, s = cos(omega), sin(omega)
    rings.extend([d+last*t*c, y+last*t*s, TUBE, omega] for t in np.linspace(0, 1, n)[1:])
    d, y = rings[-1][:2]
    for angle in th[1:]:
        rho = TUBE-R*(1-cos(angle))-TIP_G*TIP_J*betainc(.75, .5, sin(angle)**2)
        height = R*sin(angle)+2*TIP_G*sqrt(sin(angle))
        rings.append([d+height*c, y+height*s, max(rho, 0.), omega])
    rings[-1][2] = 0.
    return np.asarray(rings)


def points(port, phase, rings, chi):
    point, normal, tangent = port.frame(phase)
    base = point + port.hflat*normal
    d, y, r, angle = rings.T
    center = base+d[:, None]*normal+y[:, None]*tangent
    other = np.cos(angle)[:, None]*tangent - np.sin(angle)[:, None]*normal
    angle = np.asarray(chi)
    return center[:, None, :] + r[:, None, None]*(np.cos(angle)[None, :, None]*other[:, None, :]
               + np.sin(angle)[None, :, None]*port.axes)


def holding_frame(xyz, holding, phase, initial=.5):
    """One global rigid motion applied to every part of the complete closed surface."""
    if holding == -1:
        return np.asarray(xyz)
    port = Port(holding) if isinstance(holding, int) else holding
    origin, n, t = port.frame(phase)
    anchor, nn, tt = port.frame(initial)
    displacement = np.asarray(xyz) - origin
    return anchor+(displacement@n)[..., None]*nn + (displacement@t)[..., None]*tt + displacement[..., 2, None]*port.axes


def run(path):
    rows = []
    for name, params in (("R302", ORIGINAL), ("C2", NEW_C2)):
        for i, (omega, first, last, law) in enumerate(params):
            port = Port(i)
            rings = surface_rings(i, law, omega, first, last)
            tips = [points(port, phase, rings[-1:], [0])[0, 0] for phase in (0., .5)]
            np.testing.assert_allclose(holding_frame(tips[0], i, 0.), tips[1], atol=4e-14)
            rows.append(dict(pair=name, index=i, law=law, args=[omega, first, last],
                             flatFaceOffset=port.hflat, tipDisplacement=rings[-1,:2].tolist(),
                             tips=[v.tolist() for v in tips]))
    out = dict(entrySHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               schema="reconstructed-R302-and-C2-physical-positions-v2", R=R, rootHeight=ROOT_H,
               tube=TUBE, tipHeight=TIP_H, halfHeight=.78, rows=rows)
    with path.open("x") as f:
        json.dump(out, f, indent=2)
        f.write("\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    run(parser.parse_args().output)
