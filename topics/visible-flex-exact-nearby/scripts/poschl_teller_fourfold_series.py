#!/usr/bin/env python3
"""Finite-order fourfold diagnostics for R16; all reported numbers are floating.

The theorem uses the whole-line inverse.  This exploratory program uses an
eighth-order finite-difference even half-line BVP and a finite Robin endpoint.
It outputs all angular modes of each finite polynomial and evaluates actual
quintic spline derivatives separately from the reconstruction ODE jets.
Neither output is an interval certificate or an exact nonlinear surface.
"""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path
import numpy as np
import scipy
from scipy.integrate import solve_ivp
from scipy.interpolate import make_interp_spline
from scipy.sparse import coo_matrix, bmat, csc_matrix, diags
from scipy.sparse.linalg import splu

MU = math.sqrt(2.0)
N0 = 4
A = 2.0 + MU / N0


def finite_difference(points, length, first_shift=0):
    """Eight-order local differentiation with exact even/odd reflection at 0."""
    from sympy import finite_diff_weights
    x = np.linspace(0.0, length, points)
    step = x[1] - x[0]
    cache = {}
    matrices = []
    for degree, parity in [(1, 1), (1, -1), (2, 1)]:
        rows, cols, data = [], [], []
        for i in range(points):
            if degree == 1 and parity == 1 and i == 0:
                continue
            start = -4+first_shift if degree == 1 and i != 0 else -4
            if i+start+8 < points:
                offsets = tuple(range(start, start+9))
            else:
                offsets = tuple(range(points - 9 - i, points - i))
            key = degree, offsets
            if key not in cache:
                cache[key] = [float(v) for v in
                              finite_diff_weights(degree, offsets, 0)[degree][-1]]
            for off, weight in zip(offsets, cache[key]):
                j = i + off
                factor = 1.0
                if j < 0:
                    j, factor = -j, parity
                rows.append(i)
                cols.append(j)
                data.append(factor * weight / step ** degree)
        matrices.append(coo_matrix((data, (rows, cols)),
                                  shape=(points, points)).tocsc())
    return x, matrices


def bump(x, radius):
    x = np.asarray(x)
    t = 1.0 - (x / radius) ** 2
    value = np.zeros_like(x)
    derivative = np.zeros_like(x)
    inside = t > 0.0
    value[inside] = np.exp(1.0 - 1.0 / t[inside])
    derivative[inside] = (-2.0 * x[inside] / radius ** 2 /
                          t[inside] ** 2 * value[inside])
    return value, derivative


def build_series(order=7, points=1601, length=8.0, mean="depth",
                 bump_radius=0.125, progress=None, mu_scale=1.0):
    mu = MU * mu_scale
    strength = mu*mu + mu/N0
    if order < 3 or order % 2 != 1 or points < 33:
        raise ValueError("odd order >=3 and at least 33 radial points required")
    x, (de, do, d2e) = finite_difference(points, length)
    sech2 = 1.0 / np.cosh(x) ** 2
    q = mu*mu - strength * sech2

    def rhs(t, state):
        h, v, z, ha, va, za, zb = state
        qt = mu*mu - strength / math.cosh(t) ** 2
        ph = float(bump(np.array([t]), bump_radius)[0][0])
        return [v, qt*h, 1/h**2, va,
                qt*ha-h/math.cosh(t)**2, -2*ha/h**3, -2*ph/h**2]

    background = solve_ivp(rhs, (0.0, length),
                           [1., 0., 0., 0., 0., 0., 0.],
                           method="DOP853", rtol=2e-13, atol=2e-14,
                           max_step=min(0.08, bump_radius/5), dense_output=True)
    if not background.success:
        raise RuntimeError(background.message)
    h, v, z, ha, va, za, zb = background.sol(x)
    a, w = 1/h, v/h
    y = np.cosh(x) ** (-N0*mu)
    yp = -N0*mu*np.tanh(x)*y
    u = y/h
    up = (yp-w*y)/h
    seed_c = np.stack([u, -u/N0, w*y-yp/N0**2])
    seed_d = np.stack([up, -up/N0, w*(yp-w*y)])
    if mean == "depth":
        vc = np.stack([-ha/h**2, np.zeros_like(x), za])
        vd = np.stack([-va/h**2+2*ha*v/h**3,
                       np.zeros_like(x), -2*ha/h**3])
    elif mean == "bump":
        ph, php = bump(x, bump_radius)
        vc = np.stack([-a*ph, np.zeros_like(x), zb])
        vd = np.stack([a*w*ph-a*php, np.zeros_like(x), -2*a*a*ph])
    else:
        raise ValueError("mean must be depth or bump")
    mean_field = (vc, vd)
    fields = {1: {N0: (seed_c, seed_d)}}
    angles = max(64, 8*order)
    phi = 2*np.pi*np.arange(angles)/angles
    trig = {k: (np.cos(k*phi), np.sin(k*phi))
            for k in range(order+1)}

    def jets(field):
        dx = np.zeros((points, angles, 3))
        dt = np.zeros_like(dx)
        for m, (c, cd) in field.items():
            co, si = trig[m//N0]
            dx[:, :, 0] += cd[0, :, None]*co
            dx[:, :, 1] += cd[1, :, None]*si
            dx[:, :, 2] += cd[2, :, None]*co
            dt[:, :, 0] -= (m*c[0]+c[1])[:, None]*si
            dt[:, :, 1] += (c[0]+m*c[1])[:, None]*co
            dt[:, :, 2] -= (m*c[2])[:, None]*si
        return dx, dt

    def extract(xx, xt, tt, max_index):
        fft_xx = np.fft.rfft(xx, axis=1)/angles
        fft_xt = np.fft.rfft(xt, axis=1)/angles
        fft_tt = np.fft.rfft(tt, axis=1)/angles
        return {N0*k: (-2*fft_tt[:, k].real,
                       2*fft_xt[:, k].imag,
                       -2*fft_xx[:, k].real)
                for k in range(1, max_index+1)}

    def quadratic(j):
        xx = np.zeros((points, angles))
        xt = np.zeros_like(xx)
        tt = np.zeros_like(xx)
        field_jets = {i: jets(fields[i]) for i in range(1, j)}
        for i in range(1, j):
            ax, at = field_jets[i]
            bx, bt = field_jets[j-i]
            xx += np.sum(ax*bx, axis=2)
            xt += np.sum(ax*bt, axis=2)
            tt += np.sum(at*bt, axis=2)
        return extract(xx, xt, tt, j)

    def eliminate(m, pqr):
        p, qmix, r = pqr
        c = h*p/2
        cp = de@c
        j = v*c+h*cp-m*h*h*qmix
        f = m*m*h*h*r/2-do@j
        return c, cp, j, f

    zx, zt = jets(fields[1])
    vx, vt = jets({0: mean_field})
    unit_pqr = extract(2*np.sum(zx*vx, axis=2),
                       np.sum(zx*vt+vx*zt, axis=2),
                       2*np.sum(zt*vt, axis=2), 1)[N0]
    unit_f = eliminate(N0, unit_pqr)[3]
    # Simpson quadrature fixes the complement; the discrete border multiplier
    # determines the finite-BVP compatibility correction itself.
    weights = np.ones(points)
    if points % 2 == 1:
        weights[1:-1:2] = 4
        weights[2:-1:2] = 2
        weights *= (x[1]-x[0])/3
    else:
        weights[0] = weights[-1] = 0.5
        weights *= x[1]-x[0]
    row = weights*y
    solvers = {}
    records = []

    def solve_eta(m, f):
        if m not in solvers:
            mat = (-d2e+diags(m*m*q)).tolil()
            mat[-1, :] = de.getrow(points-1)
            mat[-1, -1] += m*mu
            mat = mat.tocsc()
            if m == N0:
                border = y.copy()
                border[-1] = 0
                mat = bmat([[mat, csc_matrix(border[:, None])],
                            [csc_matrix(row[None, :]), csc_matrix((1, 1))]],
                           format="csc")
            solvers[m] = splu(mat)
        right = f.copy()
        right[-1] = 0
        if m == N0:
            answer = solvers[m].solve(np.r_[right, 0.])
            return answer[:-1], float(answer[-1])
        return solvers[m].solve(right), 0.0

    _, unit_multiplier = solve_eta(N0, unit_f)
    if abs(unit_multiplier) < 1e-8:
        raise RuntimeError("lost discrete mean transversality")
    exact_norm = float(np.sum(weights*y*y))
    initial_record = dict(
        mean=mean, bump_radius=bump_radius,
        discrete_mean_multiplier=unit_multiplier,
        direct_projection=float(np.sum(weights*y*unit_f)),
        kernel_half_norm_squared=exact_norm,
        depth_expected_normalized_projection=128*mu/(8*mu+1),
    )

    def reconstruct(m, pqr, eta):
        c, cp, j, f = eliminate(m, pqr)
        ep = de@eta
        ur = eta/h
        urp = (ep-w*eta)/h
        ut = (c-ur)/m
        utp = (cp-urp)/m
        uz = w*eta-ep/m**2+j/m**2
        uzp = w*(ep-w*eta)+h*h*pqr[2]/2
        return np.stack([ur, ut, uz]), np.stack([urp, utp, uzp])

    for degree in range(2, order+1):
        sources = quadratic(degree)
        alpha = None
        critical_multiplier = None
        if degree % 2:
            base_f = eliminate(N0, sources[N0])[3]
            _, base_multiplier = solve_eta(N0, base_f)
            alpha = -base_multiplier/unit_multiplier
            fields[degree-1][0] = (alpha*vc, alpha*vd)
            sources[N0] = tuple(a0+alpha*a1
                                for a0, a1 in zip(sources[N0], unit_pqr))
        fields[degree] = {}
        for k in range(1 if degree % 2 else 2, degree+1, 2):
            m = N0*k
            f = eliminate(m, sources[m])[3]
            eta, multiplier = solve_eta(m, f)
            fields[degree][m] = reconstruct(m, sources[m], eta)
            if m == N0:
                critical_multiplier = multiplier
        magnitude = max(float(np.max(np.linalg.norm(c, axis=0)))
                        for c, _ in fields[degree].values())
        rec = dict(order=degree, mean_previous=alpha,
                   critical_multiplier=critical_multiplier,
                   maximum_coefficient_norm_sample=magnitude)
        records.append(rec)
        if progress is not None:
            progress(rec)
    return dict(x=x, h=h, v=v, z=z, q=q, fields=fields,
                parameters=dict(order=order, points=points, length=length,
                                mu=mu, A=strength, mean=mean, bump_radius=bump_radius, mu_scale=mu_scale),
                transversality=initial_record, recursion=records)



class IntegratedMeanHeight:
    """An actual spline map whose mean height is integrated from its slope."""
    def __init__(self, component_spline, slope_spline):
        self.component_spline = component_spline
        self.slope_spline = slope_spline
        self.primitive = slope_spline.antiderivative()
        self.origin = float(self.primitive(0.))

    def __call__(self, x, nu=0):
        result = self.component_spline(x, nu=nu)
        if nu == 0:
            result[..., 2] = self.primitive(x)-self.origin
        else:
            result[..., 2] = self.slope_spline(x, nu=nu-1)
        return result

def make_candidate(series, epsilon, order=None):
    """Return actual C4 quintic spline scalar fields on [-L,L]."""
    if order is None:
        order = series["parameters"]["order"]
    x = series["x"]
    coeffs = {0: np.stack([1/series["h"], np.zeros_like(x), series["z"]])}
    mean_z_slope = 1/series["h"]**2
    for degree in range(1, order+1):
        for mode, (c, cd) in series["fields"][degree].items():
            if mode == 0:
                mean_z_slope += epsilon**degree*cd[2]
            if mode not in coeffs:
                coeffs[mode] = np.zeros_like(c)
            coeffs[mode] += epsilon**degree*c
    full_x = np.r_[-x[:0:-1], x]
    splines = {}
    for mode, c in coeffs.items():
        reflected = c[:, :0:-1].copy()
        reflected[2] *= -1
        full_c = np.concatenate([reflected, c], axis=1)
        component = make_interp_spline(full_x, full_c.T, k=5)
        if mode == 0:
            slope = np.r_[mean_z_slope[:0:-1], mean_z_slope]
            component = IntegratedMeanHeight(
                component, make_interp_spline(full_x, slope, k=5))
        splines[mode] = component
    return dict(splines=splines, epsilon=epsilon, order=order,
                length=float(x[-1]))


def evaluate_candidate(candidate, x, theta, cartesian=True):
    """Values, Fx,Ftheta,Fxx,Fxtheta,Fthetatheta; arrays (nx,ntheta,3).

    Mean height is the actual integral of a quintic slope spline, avoiding
    differentiation of a nearly constant polar height.

    The evaluated derivatives are derivatives of the actual quintic splines,
    not substituted ODE jets.  Endpoints are finite BVP endpoints, not poles.
    """
    x, theta = np.atleast_1d(x), np.atleast_1d(theta)
    out = [np.zeros((x.size, theta.size, 3)) for _ in range(6)]
    for m, spline in candidate["splines"].items():
        c, cx, cxx = (spline(x, nu=k).T for k in range(3))
        co = np.cos(m*theta)[None, :]
        si = np.sin(m*theta)[None, :]
        u, t, w = (v[:, None] for v in c)
        ux, tx, wx = (v[:, None] for v in cx)
        uxx, txx, wxx = (v[:, None] for v in cxx)
        out[0] += np.stack([u*co, t*si, w*co], axis=-1)
        out[1] += np.stack([ux*co, tx*si, wx*co], axis=-1)
        out[2] += np.stack([-(m*u+t)*si, (u+m*t)*co, -m*w*si], axis=-1)
        out[3] += np.stack([uxx*co, txx*si, wxx*co], axis=-1)
        out[4] += np.stack([-(m*ux+tx)*si, (ux+m*tx)*co, -m*wx*si], axis=-1)
        out[5] += np.stack([-((m*m+1)*u+2*m*t)*co,
                           -(2*m*u+(m*m+1)*t)*si, -m*m*w*co], axis=-1)
    if cartesian:
        co, si = np.cos(theta)[None, :], np.sin(theta)[None, :]
        for j in range(6):
            radial, angular = out[j][:, :, 0].copy(), out[j][:, :, 1].copy()
            out[j][:, :, 0] = co*radial-si*angular
            out[j][:, :, 1] = si*radial+co*angular
    return tuple(out)


def metric_diagnostic(series, epsilon, order, core=3., samples=1201, angles=96):
    candidate = make_candidate(series, epsilon, order)
    x = np.linspace(0., min(core, candidate["length"]), samples)
    angles = max(angles, 4*max(candidate["splines"]))
    theta = 2*np.pi*np.arange(angles)/angles
    _, fx, ft, *_ = evaluate_candidate(candidate, x, theta, cartesian=False)
    exx, ext, ett = (np.sum(a*b, axis=-1)
                     for a, b in ((fx, fx), (fx, ft), (ft, ft)))
    # Normalize against the actual angular mean, which is the output metric.
    mean_xx = np.mean(exx, axis=1)[:, None]
    mean_tt = np.mean(ett, axis=1)[:, None]
    ea = (exx-mean_xx)/mean_xx
    eb = ext/np.sqrt(mean_xx*mean_tt)
    ec = (ett-mean_tt)/mean_tt
    center = (ea+ec)/2
    rad = np.sqrt(((ea-ec)/2)**2+eb*eb)
    norm = np.maximum(np.abs(center-rad), np.abs(center+rad))
    peak = np.unravel_index(np.argmax(norm), norm.shape)
    values = evaluate_candidate(candidate, x, theta, cartesian=False)[0]
    diameter = 2*float(np.max(np.linalg.norm(values, axis=2)))
    at_zero = evaluate_candidate(candidate, [0.], [0., np.pi/N0], cartesian=False)[0]
    waist_gap = float(at_zero[0, 0, 0]-at_zero[0, 1, 0])
    return dict(epsilon=epsilon, order=order, core=core,
                diameter_sample=diameter, waist_signed_radial_gap=waist_gap,
                waist_signed_gap_over_sampled_diameter=waist_gap/diameter,
                samples=samples, angles=angles,
                metric_operator_norm_sample=float(norm[peak]),
                at_x=float(x[peak[0]]), at_theta=float(theta[peak[1]]),
                minimum_mean_xx=float(mean_xx.min()),
                minimum_mean_tt=float(mean_tt.min()))


def save_series(series, path):
    data = {key: series[key] for key in ["x", "h", "v", "z", "q"]}
    for degree, modes in series["fields"].items():
        for mode, (c, cd) in modes.items():
            data[f"c_{degree}_{mode}"] = c
            data[f"d_{degree}_{mode}"] = cd
    data["metadata"] = np.array(json.dumps({k: series[k] for k in
                                          ["parameters", "transversality", "recursion"]}))
    np.savez_compressed(path, **data)


def load_series(path):
    with np.load(path, allow_pickle=False) as data:
        series = json.loads(str(data["metadata"]))
        for key in ["x", "h", "v", "z", "q"]:
            series[key] = data[key].copy()
        fields = {}
        for key in data.files:
            if key.startswith("c_"):
                _, degree, mode = key.split("_")
                fields.setdefault(int(degree), {})[int(mode)] = (
                    data[key].copy(), data[f"d_{degree}_{mode}"].copy())
        series["fields"] = fields
    return series


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--order", type=int, default=7)
    ap.add_argument("--points", type=int, default=1601)
    ap.add_argument("--length", type=float, default=8.)
    ap.add_argument("--mu-scale", type=float, default=1.)
    ap.add_argument("--mean", choices=["depth", "bump"], default="depth")
    ap.add_argument("--bump-radius", type=float, default=.125)
    ap.add_argument("--epsilons", type=float, nargs="+", default=[.05, .075, .1])
    ap.add_argument("--core", type=float, default=3.)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--save-series", type=Path)
    args = ap.parse_args()
    series = build_series(args.order, args.points, args.length, args.mean,
                          args.bump_radius,
                          progress=lambda rec: print(json.dumps(rec), flush=True),
                          mu_scale=args.mu_scale)
    diagnostics = []
    for degree in range(1, args.order+1, 2):
        for eps in args.epsilons:
            diagnostics.append(metric_diagnostic(series, eps, degree, args.core))
    report = {k: series[k] for k in ["parameters", "transversality", "recursion"]}
    report.update(kind="floating_diagnostic_not_proof",
                  versions=dict(numpy=np.__version__, scipy=scipy.__version__),
                  limitations=[
                      "Finite Robin endpoint approximates the true whole-line inverse.",
                      "Eighth-order finite differences have no interval error bounds.",
                      "Metric diagnostics use actual quintic spline derivatives.",
                      "Finite radial and angular samples do not bound continuous suprema.",
                      "No true fixed flat caps, no nonlinear exact isometry, no certified reach."],
                  diagnostics=diagnostics)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n")
    if args.save_series:
        save_series(series, args.save_series)
    print(json.dumps(dict(report=str(args.out), diagnostics=diagnostics)), flush=True)


if __name__ == "__main__":
    main()
