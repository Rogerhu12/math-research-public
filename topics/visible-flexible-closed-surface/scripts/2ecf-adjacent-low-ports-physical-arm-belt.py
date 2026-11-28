#!/usr/bin/env python3
"""Actual adjacent low-circle branches and two complete positive-turn arms, registered to the R262 physical material angle."""
import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path
import numpy as np


def module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


PROFILE = "adjacent-k063-115-105"


def setup(arms, arc, geo, low, anchor, half=.780):
    if low != .63 or half not in (.545, .660, .780):
        raise ValueError("Unknown adjacent-port physical geometry")
    curve=arc.NormalCurve()
    k=arc.LOW
    eta=arc.PHASE
    A=curve.A
    specs=((1.45,1.15,"short"),(1.45,1.05,"short"))

    class Port(arms.Port):
        def __init__(self, i):
            self.idx = i
            self.k = k
            self.width = .27
            self.u = eta/2 + i*arc.PERIOD - anchor
            self.L = self.width - arms.FLAT
            self.e = self.L / 20
            self.level = self.k * (self.width/self.L - .025) / .95
            self.axes = np.array((0., 0., 1.))
            self.hflat = self.bevel(0.)

        def frame(self, eta):
            ref = self.idx*arc.PERIOD - anchor
            angle = ref + self.k*(arc.PHASE/2-eta)
            n = np.array([np.cos(angle), np.sin(angle), 0.])
            t = np.array([-np.sin(angle), np.cos(angle), 0.])
            center = (A-1/self.k)*np.array([np.cos(ref), np.sin(ref), 0.])
            return tuple(arms.rotation(p, eta) for p in (center+n/self.k, n, t))

    return [Port(0), Port(1)], specs


def components(arms, arc, geo, low, anchor, half, phase, angles, radial, bend, chi_count):
    """Return actual part positions, in physical (u,z) labels; both signs of z included."""
    ports, specs = setup(arms, arc, geo, low, anchor, half)
    flat = {.545: .235, .660: .350, .780: .470}[half]
    end = flat+.30
    u = np.arange(angles)*(2*np.pi/angles)
    for p in ports:
        side = np.arcsin(p.k*np.array([0., arms.A_ROOT, arms.FLAT, p.width]))/p.k
        u = np.concatenate((u, p.u-side, p.u+side))
    u = np.unique(np.mod(u, 2*np.pi))
    z = np.unique(np.r_[np.linspace(-half, half, 2*radial+1), -end,-flat,-arms.A_ROOT,0.,arms.A_ROOT,flat,end])
    curve=arc.NormalCurve()
    p=curve.at(u-phase,anchor)[0]
    raw=arms.rotation(np.column_stack((p.real,p.imag,np.zeros_like(p.real))),phase)
    X = np.broadcast_to(raw[None,:,:], (len(z),len(u),3)).copy()
    X[:,:,2] = z[:,None]
    keep = np.ones(X.shape[:2],bool)
    for p in ports:
        du, x = p.local_offset(u)
        use = abs(du) <= np.arcsin(p.k*p.width)/p.k
        x = x[use]
        origin, n, t = p.frame(phase)
        h = p.old(x)
        hbar = np.asarray([p.bevel(item) for item in x])
        w = arms.smooth(np.clip((end-abs(z))/.30, 0., 1.))
        X[:,use,:] = (origin+x[None,:,None]*t+
                        (h[None,:]+w[:,None]*(hbar-h)[None,:])[:,:,None]*n+
                        z[:,None,None]*p.axes)
        keep[:,use] &= (z[:,None]**2 + x[None,:]**2 >= arms.A_ROOT**2)
    zi, ui = np.nonzero(keep)
    yield "belt", X[keep], np.column_stack((z[zi],u[ui]))
    chi = np.arange(chi_count)*(2*np.pi/chi_count)
    for i,(p,(omega,last,law)) in enumerate(zip(ports,specs)):
        rings = arms.surface_rings(i,law,omega,.24,last,bend)
        pts = arms.points(p,phase,rings,chi)
        rid, cid = np.indices(pts.shape[:2])
        yield "arm"+str(i), pts.reshape(-1,3), np.column_stack((rid.ravel(),chi[cid.ravel()]))


def main(a):
    arms = module(a.arms, "physR302")
    arc = module(a.arc, "physR262Arc")
    geo = module(a.comparison, "physD3")
    ports, specs = setup(arms, arc, geo, a.low, a.anchor, a.half)
    labels = []
    for eta in (0.,arc.PHASE/2,arc.PHASE):
        rows = []
        for name,points,uv in components(arms,arc,geo,a.low,a.anchor,a.half,eta,192,22,30,48):
            rows.append(dict(part=name,n=len(points),lo=points.min(axis=0).tolist(),hi=points.max(axis=0).tolist()))
        labels.append(dict(phase=eta,parts=rows))
    proof = dict(halfHeight=a.half, flatHalfHeight=a.half-.31, taperWidth=.30, collar=.01,
                 shoulderRadius=.115, mouthRadius=.233, fingerBallUpperHeight=.348,
                 materialCenters=[p.u for p in ports], arms=specs)
    report = dict(schema="physical-adjacent-suite-k063-eta115-v1",sourceSHA=sha(__file__),
                  armSourceSHA=sha(a.arms),arcSourceSHA=sha(a.arc),angularSourceSHA=sha(a.comparison),
                  definition=proof,finitePositionSamples=labels)
    with a.out.open("x") as f:
        json.dump(report,f,indent=2)
        f.write("\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    for name in ("arms","arc","comparison","out"):
        parser.add_argument("--"+name,required=True,type=Path)
    parser.add_argument("--low",type=float,choices=(.63,),default=.63)
    parser.add_argument("--anchor",type=float,default=np.pi/3)
    parser.add_argument("--half",type=float,choices=(.545,.660,.780),default=.780)
    main(parser.parse_args())
