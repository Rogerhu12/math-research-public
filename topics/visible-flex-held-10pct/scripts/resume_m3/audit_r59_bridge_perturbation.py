#!/usr/bin/env python3
"""Read-only finite diagnostic of the R59 full short-bridge perturbation.

Uses the actual PPoly field, same source model, full angular chart/reference lift,
and fixed mean-velocity rule. No BVP or tail solver is called. The reference
constants use high precision true integrals; reference queries use finite GL64
quadrature and actual mean height uses the original segmentwise GL6 query.
These are numerical diagnostics, never a continuous R59 certificate.
"""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from fractions import Fraction
import sys
import mpmath as mp
import numpy as np

def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

class ExactBridgeReference:
    def __init__(self, cut):
        mp.mp.dps = 60
        def real(value):
            z = Fraction.from_float(float(value))
            return mp.mpf(z.numerator)/z.denominator
        R, w, wr = (real(cut[key]) for key in
                    ("radius", "backgroundSlope", "backgroundSecond"))
        pt = mp.atan2(1, w)
        peak = pt+(mp.pi/2-pt)/5
        eps = peak-pt
        ps = wr/(1+w*w)**mp.mpf("1.5")
        L1, L3 = 3*peak/8, 2*eps/(-ps)
        phi1 = lambda t: peak*(3*t*t-2*t*t*t)
        phi3 = lambda t: peak-eps*t*t
        S1 = mp.quad(lambda t: mp.sin(phi1(t)), [0, 1])
        S3 = mp.quad(lambda t: mp.sin(phi3(t)), [0, 1])
        C1 = mp.quad(lambda t: mp.cos(phi1(t)), [0, 1])
        C3 = mp.quad(lambda t: mp.cos(phi3(t)), [0, 1])
        L2 = (1-R-L1*S1-L3*S3)/mp.sin(peak)
        if L2 <= 0:
            raise ValueError("No reference plateau")
        self.L1, self.L2, self.L3 = map(float, (L1, L2, L3))
        self.L = float(L1+L2+L3)
        self.peak, self.eps = float(peak), float(eps)
        self.height = float(L1*C1+L2*mp.cos(peak)+L3*C3)
        self.drop1, self.rise1 = float(L1*S1), float(L1*C1)
        self.drop2 = float(L2*mp.sin(peak))
        self.rise2 = float(L2*mp.cos(peak))
        self.g, self.gw = np.polynomial.legendre.leggauss(64)
        self.metadata = dict(
            constant_rule="mpmath 60 decimal digits; true integral numerical evaluation",
            partial_query_rule="64 point Gauss-Legendre; no outward error bound",
            lengths=[self.L1, self.L2, self.L3], length=self.L, height=self.height)

    def partial(self, u, part, trig):
        t = np.asarray(u)[:, None]*(1+self.g)/2
        phi = self.peak*(3*t*t-2*t*t*t) if part == 1 else self.peak-self.eps*t*t
        values = np.sin(phi) if trig == "sin" else np.cos(phi)
        return np.asarray(u)/2*(values@self.gw)

    def jets(self, xi, theta, z0):
        xi = np.atleast_1d(np.asarray(xi, float))
        u = np.clip(xi/self.L1, 0, 1)
        t = np.clip((xi-self.L1-self.L2)/self.L3, 0, 1)
        plateau = np.clip(xi-self.L1, 0, self.L2)
        first = xi <= self.L1
        last = xi > self.L1+self.L2
        phi = np.where(first, self.peak*(3*u*u-2*u*u*u),
                       np.where(last, self.peak-self.eps*t*t, self.peak))
        phip = np.where(first, 6*self.peak*u*(1-u)/self.L1,
                        np.where(last, -2*self.eps*t/self.L3, 0))
        a = 1-self.L1*self.partial(u, 1, "sin")-plateau*np.sin(self.peak)-self.L3*self.partial(t, 3, "sin")
        h = self.L1*self.partial(u, 1, "cos")+plateau*np.cos(self.peak)+self.L3*self.partial(t, 3, "cos")
        ap, hp = -np.sin(phi), np.cos(phi)
        app, hpp = -np.cos(phi)*phip, -np.sin(phi)*phip
        er = np.stack((np.cos(theta), np.sin(theta), np.zeros_like(theta)), axis=-1)
        et = np.stack((-np.sin(theta), np.cos(theta), np.zeros_like(theta)), axis=-1)
        ez = np.zeros_like(er); ez[:, :, 2] = 1
        b = lambda values: np.asarray(values)[:, None, None]
        return dict(
            a=a, ap=ap, pos=b(a)*er+b(z0+h)*ez,
            sx=b(ap)*er+b(hp)*ez, st=b(a)*et,
            sxx=b(app)*er+b(hpp)*ez, sxt=b(ap)*et, stt=-b(a)*er,
            normal=b(np.cos(phi))*er+b(np.sin(phi))*ez)

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source-run", type=Path, required=True)
    p.add_argument("--physical", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--support-dir", type=Path, default=Path(__file__).resolve().parent)
    p.add_argument("--angular", type=int, default=512)
    p.add_argument("--mean-nodes", type=int, default=512)
    p.add_argument("--radial", type=int, default=151)
    p.add_argument("--batch", type=int, default=8)
    a = p.parse_args()
    if min(a.angular, a.mean_nodes) < 16 or a.radial < 2 or a.batch < 1:
        raise ValueError("Invalid diagnostic grid")
    adapter = module("_bridge_actual_adapter", a.support_dir/"actual_m3_metric_model.py")
    loader = module("_bridge_physical_loader", a.support_dir/"audit_full_relative_metric.py")
    o = adapter.load_model({"source_run": str(a.source_run.resolve())})
    physical = loader.load_physical(a.physical)
    o.initial(physical.p)
    f = o.flow(physical.p[0])
    spec = f.cfg["prefix_bridge"]
    if spec != {"kind": "turn_plateau_v1", "curvature": 4, "peak_fraction": .2}:
        raise ValueError("R59 reference requires the unchanged curvature-4 bridge")
    ref = ExactBridgeReference(f.port_data["cut"])
    prefix_end, end = float(f.prefix_end), float(f.end)
    scale = float(f.bridge.L/ref.L)
    knots = physical.x[(physical.x >= prefix_end) & (physical.x <= end)]
    mids = (physical.x[:-1]+physical.x[1:])/2
    mids = mids[(mids >= prefix_end) & (mids <= end)]
    ss = np.unique(np.r_[np.linspace(prefix_end, end, a.radial), knots, mids])
    # Same old positive segment quadrature rule and fixed mean N; it does not
    # redefine or reset the mean at the bridge inlet.
    hh = f.height_integral(physical, np.r_[prefix_end, ss], a.mean_nodes, 6)
    z0, heights = float(hh[0]), hh[1:]
    B, B1, B2 = f.basis(a.angular)
    _, B1m, B2m = f.basis(a.mean_nodes)
    psi = 2*np.pi*np.arange(a.angular)/a.angular
    maxima, minima = {}, {}
    def record(name, value, s, theta, kind="max"):
        table = maxima if kind == "max" else minima
        flat = np.argmax(value) if kind == "max" else np.argmin(value)
        i, j = np.unravel_index(flat, value.shape)
        vv = float(value[i, j])
        old = table.get(name)
        if old is None or (vv > old["value"] if kind == "max" else vv < old["value"]):
            table[name] = dict(value=vv, s=float(s[i]), xi=float((s[i]-prefix_end)/scale),
                               psi=float(psi[j]), theta=float(theta[i, j]))
    for start in range(0, len(ss), a.batch):
        s = ss[start:start+a.batch]
        Y, Yp, Ypp = (physical.sol(s, order) for order in (0, 1, 2))
        fr, sp, dW = f.velocity_s(s, Y, Yp, B1, B2)
        if a.angular == a.mean_nodes:
            frm, dWm = fr, dW
        else:
            frm, _, dWm = f.velocity_s(s, Y, Yp, B1m, B2m)
        mean = np.mean(frm["V"][:, :, 2], axis=1)
        mean2 = np.mean(dWm[:, :, 2], axis=1)
        g = fr["geo"]
        rho, v, d, dd = g["rho"], g["v"], fr["d"], fr["dd"]
        b = lambda values: np.asarray(values)[:, :, None]
        pos = g["pos"]+o.q*f.values(Y, B)
        pos[:, :, 2] += heights[start:start+len(s), None]
        Fsc = g["s1"]+o.q*f.values(Yp, B)
        Fsc[:, :, 2] += mean[:, None]
        Fssc = g["s2"]+o.q*f.values(Ypp, B)
        Fssc[:, :, 2] += mean2[:, None]
        Fs = Fsc-b(v)*d
        Ft = d/b(rho)
        Ftt = dd/b(rho)**2-d*b(g["rhop"])/b(rho)**3
        Fst = (sp-b(g["vp"])*d-b(v)*dd)/b(rho)
        Fss = Fssc-2*b(v)*sp+b(v)**2*dd+b(v*g["vp"]-g["vs"])*d
        # Affine pullback only; true material angle remains unchanged.
        Fx, Fxx, Fxt = scale*Fs, scale*scale*Fss, scale*Fst
        rr = ref.jets((s-prefix_end)/scale, g["theta"], z0)
        V, Vx, Vt = pos-rr["pos"], Fx-rr["sx"], Ft-rr["st"]
        Vxx, Vxt, Vtt = Fxx-rr["sxx"], Fxt-rr["sxt"], Ftt-rr["stt"]
        aa, av = rr["a"][:, None, None], rr["ap"][:, None, None]
        H00, H01, H11 = Vxx, (Vxt-av/aa*Vt)/aa, (Vtt+aa*av*Vx)/aa**2
        norm = lambda q: np.linalg.norm(q, axis=-1)
        eta1 = np.sqrt(norm(Vx)**2+norm(Vt/aa)**2)
        eta2 = np.sqrt(norm(H00)**2+2*norm(H01)**2+norm(H11)**2)
        nraw = np.cross(Ft, Fx)
        normal = nraw/norm(nraw)[:, :, None]
        E, FF, G = np.sum(Fx*Fx, -1), np.sum(Fx*Ft, -1), np.sum(Ft*Ft, -1)
        L, M, NN = np.sum(Fxx*normal, -1), np.sum(Fxt*normal, -1), np.sum(Ftt*normal, -1)
        detI = E*G-FF*FF
        tr = (L*G-2*M*FF+NN*E)/detI
        detII = (L*NN-M*M)/detI
        kappa = (np.abs(tr)+np.sqrt(np.maximum(0, tr*tr-4*detII)))/2
        for name, value in [
            ("V", norm(V)), ("eta1", eta1), ("eta2", eta2),
            ("H00", norm(H00)), ("H01", norm(H01)), ("H11", norm(H11)),
            ("actual_radius", norm(pos)), ("actual_kappa", kappa)]:
            record(name, value, s, g["theta"])
        for name, value in [
            ("actual_support", np.sum(pos*normal, -1)),
            ("normal_alignment", np.sum(normal*rr["normal"], -1)),
            ("area", norm(nraw))]:
            record(name, value, s, g["theta"], "min")
    limits = dict(V=.13, eta1=.12, eta2=5.5)
    report = dict(
        status="finite_geometry_diagnostic_completed",
        continuous_certificate=False, actual_model_loaded_without_solver=True,
        source_run=str(a.source_run.resolve()), source_run_sha256=sha(a.source_run),
        physical_path=str(a.physical.resolve()), physical_sha256=sha(a.physical),
        actual_model=o.relative_metric_loader_record,
        angular=a.angular, mean_nodes=a.mean_nodes, radial_samples=len(ss),
        radial_rule="151 uniform bridge sections plus actual knots and midpoints",
        mean_rule="same finite angular mean; existing positive per-segment GL6 height query",
        mean_height_caveat="No quadrature or continuous evaluation remainder certified",
        actual_p=physical.p.tolist(),
        bridge_entry_s=prefix_end, bridge_end_s=end,
        z0=z0, cut_mean_height=float(heights[-1]),
        affine_reference_scale=scale, reference=ref.metadata,
        maxima=maxima, minima=minima,
        sufficient_window=limits,
        sampled_window_tests={**{k:maxima[k]["value"] <= v for k,v in limits.items()},
                              "entry_height": .35 <= z0 <= .51},
        source_sha256=sha(__file__))
    # Keep a small diagnostic summary visible through the existing live worker.
    report["diagnostics"] = {key: report[key] for key in
        ("maxima", "minima", "sampled_window_tests", "z0", "cut_mean_height",
         "radial_samples", "angular", "mean_nodes", "continuous_certificate")}
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report["diagnostics"]))

if __name__ == "__main__":
    main()

