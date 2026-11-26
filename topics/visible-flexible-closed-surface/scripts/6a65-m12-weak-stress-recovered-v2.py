#!/usr/bin/env python3
"""Recoverable numerical weak-moment Cartesian patch for the M12 prefix.

This is a newly reconstructed source identity, not the lost script whose SHA256
was c52e50555ca26497f216140b57f9c88001fa0abaa2ef99c9193679b77720c43f.
Every fit / evaluation records its own source hash. Numerical quadrature only:
no continuous certificate, exact-original-bridge transfer, or refinement proof.
Run all outputs in a temporary directory; do not commit regenerable outputs.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import io
import json
import math
from fractions import Fraction as Q
from pathlib import Path
import time
import numpy as np

LD = np.longdouble
PI = np.arccos(LD(-1))
KS = np.arange(3, 37, 3, dtype=int)
DATA_SHA = "359d491cd592962d467fdd538013977ee9a92070346de41c227d9ca3e1ef3bd0"
META_NAME = "2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json"


def q(x):
    return Q.from_float(float(x))


def ld(x):
    if isinstance(x, Q):
        return LD(x.numerator) / LD(x.denominator)
    return LD(x)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def exact_clamped_spline(chart):
    """The same rational clamped cubic equations as the 78718 supplier."""
    x = list(map(q, chart["knots"]))
    y = list(map(q, chart["values"]))
    n = len(x)
    if x[0] != 0 or x[-1] != 1 or len(y) != n:
        raise ValueError("Invalid chart")
    h = [x[i+1]-x[i] for i in range(n-1)]
    if min(h) <= 0:
        raise ValueError("Non-increasing chart")
    low, dia, upp, rhs = [[Q(0)]*n for _ in range(4)]
    dia[0], upp[0] = 2*h[0], h[0]
    rhs[0] = 6*(y[1]-y[0])/h[0]
    low[-1], dia[-1] = h[-1], 2*h[-1]
    rhs[-1] = 6*(q(chart["final_derivative"])-(y[-1]-y[-2])/h[-1])
    for i in range(1, n-1):
        low[i], dia[i], upp[i] = h[i-1], 2*(h[i-1]+h[i]), h[i]
        rhs[i] = 6*((y[i+1]-y[i])/h[i]-(y[i]-y[i-1])/h[i-1])
    for i in range(1, n):
        fac = low[i]/dia[i-1]
        dia[i] -= fac*upp[i-1]
        rhs[i] -= fac*rhs[i-1]
    z = [Q(0)]*n
    z[-1] = rhs[-1]/dia[-1]
    for i in range(n-2, -1, -1):
        z[i] = (rhs[i]-upp[i]*z[i+1])/dia[i]
    cs = []
    for i in range(n-1):
        cs.append([y[i],
                   (y[i+1]-y[i])/h[i]-h[i]*(2*z[i]+z[i+1])/6,
                   z[i]/2, (z[i+1]-z[i])/(6*h[i])])
    return x, cs


class Source:
    def __init__(self, data, meta):
        if sha(data) != DATA_SHA:
            raise ValueError("M12 binary input SHA256 mismatch")
        self.meta = json.loads(Path(meta).read_text())
        with np.load(io.BytesIO(gzip.decompress(Path(data).read_bytes())),
                     allow_pickle=False) as raw:
            self.mesh64 = raw["mesh"].copy()
            self.mesh = np.asarray(raw["mesh"], dtype=LD)
            nodal = np.asarray(raw["jets"], dtype=LD)
            increments = np.asarray(raw["mean_increments"], dtype=LD)
        self.M = (nodal.shape[2]-2)//3
        if nodal.shape != (3, len(self.mesh), 3*self.M+2):
            raise ValueError("Bad jet shape")
        if self.M != 24 or len(self.mesh) != 2570:
            raise ValueError("Unexpected M12 payload")
        if not np.all(np.diff(self.mesh) > 0):
            raise ValueError("Bad mesh")
        self.h = np.diff(self.mesh)
        y, d, d2 = [a.copy() for a in nodal]
        # Exact definition uses rational cumulative sums. Longdouble here is
        # only numerical evaluation; derivative uses increments themselves.
        y[0, -1] = 0
        y[1:, -1] = np.cumsum(increments, dtype=LD)
        delta = y[1:]-y[:-1]
        delta[:, -1] = increments
        h = self.h[:, None]
        c0, c1, c2 = y[:-1], h*d[:-1], h*h*d2[:-1]/2
        r0 = delta-c1-c2
        r1 = h*(d[1:]-d[:-1])-h*h*d2[:-1]
        r2 = h*h*(d2[1:]-d2[:-1])
        self.power = np.stack([c0, c1, c2, 10*r0-4*r1+r2/2,
                               -15*r0+7*r1-r2, 6*r0-3*r1+r2/2], axis=1)
        sx, sc = exact_clamped_spline(self.meta["chart"])
        self.sx = np.asarray([ld(v) for v in sx])
        self.sc = np.asarray([[ld(v) for v in row] for row in sc])
        self.warp = ld(8*q(self.meta["warp_reference_q"]))
        self.end = self.mesh[-1]
        self.common_start = self.mesh[int(self.meta["correction_start_index"])]

    def chart(self, s):
        x = s/self.end
        if not (0 <= x < LD(".75")):
            raise ValueError("Support enters cutoff; extension needed explicitly")
        j = min(np.searchsorted(self.sx, x, side="right")-1, len(self.sc)-1)
        h = x-self.sx[j]
        c = self.sc[j]
        e = ((c[3]*h+c[2])*h+c[1])*h+c[0]
        ep = ((3*c[3]*h+2*c[2])*h+c[1])/self.end
        return self.warp*e, self.warp*ep

    def coefficients(self, cell, s):
        t = (s-self.mesh[cell])/self.h[cell]
        p = self.power[cell]
        c = p[-1].copy()
        for j in range(4, -1, -1):
            c = c*t+p[j]
        d = 5*p[5]
        for j in range(4, 0, -1):
            d = d*t+j*p[j]
        return c, d/self.h[cell]

    def sample(self, cell, s, psi, co, si, f):
        c, d = self.coefficients(cell, s)
        M = self.M
        freq = np.arange(3, 3*M+1, 3, dtype=LD)
        R = c[0] + c[1:M+1] @ co
        T = c[M+1:2*M+1] @ si
        Xs = np.stack([d[0]+d[1:M+1] @ co,
                       d[M+1:2*M+1] @ si,
                       d[-1]+d[2*M+1:3*M+1] @ co], axis=1)
        Xp = np.stack([-(freq*c[1:M+1]) @ si-T,
                       R+(freq*c[M+1:2*M+1]) @ co,
                       -(freq*c[2*M+1:3*M+1]) @ si], axis=1)
        e, ep = self.chart(s)
        rho = 1-e*np.cos(3*psi)
        nu = -ep*np.sin(3*psi)/3
        if np.min(rho) <= 0:
            raise ArithmeticError("Chart orientation not positive at samples")
        u = psi-e*np.sin(3*psi)/3
        b = nu/rho
        dot = lambda a, z: np.sum(a*z, axis=-1, dtype=LD)
        dss = dot(Xs, Xs)-(1+f*f*nu*nu)
        dsp = dot(Xs, Xp)-f*f*nu*rho
        dpp = dot(Xp, Xp)-f*f*rho*rho
        E = dss-2*b*dsp+b*b*dpp
        Z = (dsp-b*dpp)/(f*rho)
        G = dpp/(f*f*rho*rho)
        return u, rho, Xs-b[:, None]*Xp, Xp/rho[:, None], E, Z, G


def regions(meta):
    cfg = meta["frozen_profile"]
    delta, vu, vd, eps = map(q, [cfg["delta"], cfg["vu"], cfg["vd"], cfg["ramp"]])
    if cfg["direction"] != "outward" or int(cfg["cycles"]) != 1:
        raise ValueError("Only the frozen outward one-cycle profile is implemented")
    tu, td = delta/(vu*(1-eps)), delta/(vd*(1-eps))
    result = []
    for name, t, start, slope, intercept in [
        ("up", tu, Q(0), vu, 1-delta*eps/(2*(1-eps))),
        ("down", td, tu, -vd, 1+delta+vd*tu+delta*eps/(2*(1-eps)))
    ]:
        left = start+t*(eps+(1-2*eps)/20)
        right = start+t*(eps+19*(1-2*eps)/20)
        result.append(dict(name=name, left=left, right=right,
                           slope=slope, intercept=intercept))
    return result


def bump(s, left, right):
    L = right-left
    t = (s-left)/L
    c = t**3*(1-t)**3
    cp = 3*t*t*(1-t)**2*(1-2*t)/L
    cpp = 6*t*(1-t)*(1-5*t+5*t*t)/(L*L)
    return c, cp, cpp


def stress(s, f, slope, left, right, u):
    c, cp, cpp = bump(s, left, right)
    k = KS.astype(LD)
    D = k*k-slope*slope
    v = f*f*cp/D
    vp = (2*f*slope*cp+f*f*cpp)/D
    t1, t2, t3 = ((slope/f)*v-c)/(k*f), v/(f*f), vp/(k*f)
    co, si = np.cos(k[:, None]*u), np.sin(k[:, None]*u)
    A, B, C = t1[:, None]*co, t2[:, None]*si, t3[:, None]*co
    nuclear = np.maximum(np.abs(A+C), np.sqrt((A-C)**2+4*B*B))
    return A, B, C, nuclear, c, cp, co, si


def cartesian_columns(c, cp, co, si, u, psi):
    # All vectors are expressed in the source e_r(psi),e_theta(psi),e_z basis.
    d = u-psi
    er = np.stack([np.cos(d), np.sin(d), np.zeros_like(d)], axis=1)
    et = np.stack([-np.sin(d), np.cos(d), np.zeros_like(d)], axis=1)
    ez = np.zeros_like(er)
    ez[:, 2] = 1
    k = KS.astype(LD)[:, None]
    rs = cp*co[:, :, None]*er[None, :, :]
    ru = c*(-k[:, :, None]*si[:, :, None]*er[None, :, :]
            +co[:, :, None]*et[None, :, :])
    zs = cp*co[:, :, None]*ez[None, :, :]
    zu = -c*k[:, :, None]*si[:, :, None]*ez[None, :, :]
    return np.concatenate([rs, zs]), np.concatenate([ru, zu])


def opmax(E, Z, G):
    return np.max((np.abs(E+G)+np.sqrt((E-G)**2+4*Z*Z))/2)


def exact_budget(coeff, L):
    """Exact rational consequences for the fixed binary64 coefficient vector."""
    r = [q(x) for x in coeff[:12]]
    z = [q(x) for x in coeff[12:]]
    S0 = sum((abs(a)+abs(b) for a, b in zip(r, z)), Q(0))
    S1 = sum(((int(k)+1)*abs(a)+int(k)*abs(b)
              for k, a, b in zip(KS, r, z)), Q(0))
    S2 = sum(((int(k)+1)**2*abs(a)+int(k)**2*abs(b)
              for k, a, b in zip(KS, r, z)), Q(0))
    bounds = dict(W=S0/64, Ws=3*S0/(16*L), Wu=S1/64,
                  Wss=3*S0/(2*L*L), Wsu=3*S1/(16*L), Wuu=S2/64)
    limits = dict(W=Q(41, 10**12), Ws=Q(384, 10**11), Wu=Q(12, 10**10),
                  Wss=Q(24, 10**8), Wsu=Q(113, 10**9), Wuu=Q(365, 10**10))
    norm2 = 4*bounds["Ws"]**2+Q(25, 4)*bounds["Wu"]**2
    d, p = Q(257212, 10**13), Q(9, 10**9)
    return dict(S=[str(x) for x in (S0, S1, S2)],
                S_display=[float(x) for x in (S0, S1, S2)],
                bounds_rational={k:str(v) for k,v in bounds.items()},
                bounds_display={k:float(v) for k,v in bounds.items()},
                strict_limits={k:bounds[k] < v for k,v in limits.items()},
                dW_g_less_than_9e_9=norm2 < p*p,
                original_global_metric_budget_less_than_4_4e_8=
                (norm2 < p*p and d+2*(1+d)*p+p*p < Q(44, 10**9)),
                budget_scope="Conditional on original R21 bounds, lambda<2 and f>=2/5; X+W, not (X o Phi)+W")


def run_region(src, rg, angular, gauss, fit, apply):
    a, b = ld(rg["left"]), ld(rg["right"])
    slope, intercept = ld(rg["slope"]), ld(rg["intercept"])
    if not b < src.common_start or not b/src.end < LD(".75"):
        raise ValueError("Patch reaches unimplemented common correction or cutoff")
    psi = np.arange(angular, dtype=LD)*(2*PI/(3*angular))
    fk = np.arange(3, 3*src.M+1, 3, dtype=LD)
    co, si = np.cos(fk[:, None]*psi), np.sin(fk[:, None]*psi)
    qx, qw = np.polynomial.legendre.leggauss(gauss)
    qx, qw = np.asarray(qx, dtype=LD), np.asarray(qw, dtype=LD)
    bvec, den = np.zeros(12, dtype=LD), np.zeros(12, dtype=LD)
    K = np.zeros((12, 24), dtype=LD) if fit else None
    factors = (1., .5, .25, .125) if apply is not None else ()
    bv = {v:np.zeros(12, dtype=LD) for v in factors}
    mx = {v:LD(0) for v in factors}
    before, dwmax, count = LD(0), LD(0), 0
    first = max(0, np.searchsorted(src.mesh, a, side="right")-1)
    last = min(len(src.mesh)-1, np.searchsorted(src.mesh, b, side="left"))
    for cell in range(first, last):
        left, right = max(a, src.mesh[cell]), min(b, src.mesh[cell+1])
        if right <= left:
            continue
        for xi, wi in zip(qx, qw):
            s = (left+right)/2+(right-left)*xi/2
            rw = (right-left)*wi/2
            f = intercept+slope*s
            u, rho, Xs, Xu, E, Z, G = src.sample(cell, s, psi, co, si, f)
            A, B, C, nuc, c, cp, cku, sku = stress(s, f, slope, a, b, u)
            w = 2*rw*f*rho/angular
            pair = lambda e,z,g: np.sum((A*e+2*B*z+C*g)*w, axis=1, dtype=LD)
            bvec += pair(E, Z, G)
            den += np.sum(nuc*w, axis=1, dtype=LD)
            before = max(before, opmax(E, Z, G))
            count += 1
            if fit or apply is not None:
                Ws, Wu = cartesian_columns(c, cp, cku, sku, u, psi)
            if fit:
                j11 = 2*np.sum(Ws*Xs[None, :, :], axis=2, dtype=LD)
                j12 = (np.sum(Wu*Xs[None, :, :], axis=2, dtype=LD)
                       +np.sum(Ws*Xu[None, :, :], axis=2, dtype=LD))/f
                j22 = 2*np.sum(Wu*Xu[None, :, :], axis=2, dtype=LD)/(f*f)
                K += ((A*w) @ j11.T+2*(B*w) @ j12.T+(C*w) @ j22.T)
            if apply is not None:
                ws = np.sum(apply[:, None, None]*Ws, axis=0, dtype=LD)
                wu = np.sum(apply[:, None, None]*Wu, axis=0, dtype=LD)
                dot = lambda x,y: np.sum(x*y, axis=1, dtype=LD)
                le, lz, lg = 2*dot(Xs,ws), (dot(Xs,wu)+dot(Xu,ws))/f, 2*dot(Xu,wu)/(f*f)
                qe, qz, qg = dot(ws,ws), dot(ws,wu)/f, dot(wu,wu)/(f*f)
                dwmax = max(dwmax, np.max(np.sqrt(qe+qg)))
                for v in factors:
                    ev,zv,gv = E+v*le+v*v*qe,Z+v*lz+v*v*qz,G+v*lg+v*v*qg
                    bv[v] += pair(ev,zv,gv)
                    mx[v] = max(mx[v],opmax(ev,zv,gv))
    out = dict(name=rg["name"], support_rational=[str(rg["left"]),str(rg["right"])],
               support=[float(a),float(b)], radial_nodes=count,
               sampled_metric_before=float(before), moments=[float(x) for x in bvec],
               stress_denominator_over_pi=[float(x) for x in den],
               weak_ratios=[float(x) for x in np.abs(bvec)/den],
               maximum_weak_ratio=float(np.max(np.abs(bvec)/den)))
    if fit:
        K64, b64 = np.asarray(K,dtype=float), np.asarray(bvec,dtype=float)
        scale = np.linalg.norm(K64,axis=1)
        if np.min(scale) <= 0:
            raise ArithmeticError("Zero response row")
        kn, bn = K64/scale[:,None], b64/scale
        coeff, residual, rank, singular = np.linalg.lstsq(kn,-bn,rcond=None)
        out["fit"] = dict(coefficients=coeff.tolist(), coefficients_hex=[x.hex() for x in coeff],
                          rank=int(rank), scaled_singular_values=singular.tolist(),
                          singular_ratio=float(singular[-1]/singular[0]),
                          scaled_linear_residual_max=float(np.max(np.abs(kn@coeff+bn))),
                          exact_cartesian_budget=exact_budget(coeff,rg["right"]-rg["left"]))
    if apply is not None:
        out["sampled_dW_frobenius_max"] = float(dwmax)
        out["actual_steps"] = [
            dict(factor=v,sampled_metric=float(mx[v]),moments=[float(x) for x in bv[v]],
                 maximum_weak_ratio=float(np.max(np.abs(bv[v])/den))) for v in factors]
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data",type=Path,required=True)
    ap.add_argument("--geometry",type=Path)
    ap.add_argument("--out",type=Path,required=True)
    ap.add_argument("--angular",type=int,default=512)
    ap.add_argument("--gauss",type=int,default=8)
    ap.add_argument("--region",choices=["up","down","both"],default="both")
    group=ap.add_mutually_exclusive_group()
    group.add_argument("--cartesian-correction",action="store_true")
    group.add_argument("--apply-correction",type=Path)
    args=ap.parse_args()
    if args.out.exists():
        raise FileExistsError("Use a fresh output path")
    if args.angular < 128 or args.gauss < 2:
        raise ValueError("Insufficient screen nodes")
    geom=args.geometry or Path(__file__).resolve().parent.parent/"notes"/META_NAME
    started=time.monotonic()
    source=Source(args.data,geom)
    apply={}
    if args.apply_correction:
        rec=json.loads(args.apply_correction.read_text())
        if rec["data_sha256"] != DATA_SHA:
            raise ValueError("Correction has another source payload")
        for item in rec["regions"]:
            apply[item["name"]]=np.asarray(item["fit"]["coefficients"],dtype=LD)
    out=dict(status="NUMERICAL_SCREEN_ONLY",source_identity="recovered-v2",
             source_sha256=sha(__file__),data_sha256=sha(args.data),geometry_sha256=sha(geom),
             angular_per_threefold_period=args.angular,gauss_per_source_cell=args.gauss,
             continuous_certificate=False,exact_original_bridge_transfer=False,
             old_source_identity_reproduced=False,
             patch_background="R21 original X, not R114 X composed with Phi",
             regions=[])
    if args.apply_correction:
        out["fit_report_sha256"]=sha(args.apply_correction)
    for rg in regions(source.meta):
        if args.region != "both" and rg["name"] != args.region:
            continue
        if args.apply_correction and rg["name"] not in apply:
            raise ValueError("Requested region missing in fixed coefficient report")
        out["regions"].append(run_region(source,rg,args.angular,args.gauss,
                                         args.cartesian_correction,apply.get(rg["name"])))
    out["seconds"]=time.monotonic()-started
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(out,indent=2,allow_nan=False)+"\n")
    print(json.dumps({k:v for k,v in out.items() if k!="regions"},indent=2))
    for item in out["regions"]:
        print(json.dumps({k:v for k,v in item.items() if k not in ("moments","weak_ratios","stress_denominator_over_pi")},indent=2))


if __name__ == "__main__":
    main()

