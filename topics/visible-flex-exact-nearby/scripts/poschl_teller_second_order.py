#!/usr/bin/env python3
"""Floating diagnostics for the rigorous second-order construction in R8.

The theorem defines eta by the true whole-line L_6 inverse.  This program
approximates it with a finite-interval even Robin BVP.  No output is an
interval certificate, a global norm bound, or a proof of nonlinear existence.
The metric diagnostic differentiates the saved scalar BVP polynomial itself;
the exact-ODE-jet diagnostic is reported separately for comparison.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
import scipy
from scipy.integrate import solve_ivp, solve_bvp

MU = math.sqrt(2.0)
N = 3
M = 6
A = 2.0 + MU / 3.0
KANG = N - 1.0 / N


def source(x, h, v):
    """Analytic source formulas; also accepts complex jets for differentiation."""
    q = 2.0 - A / np.cosh(x) ** 2
    w = v / h
    p = np.sqrt(1.0 + v * v)
    y = np.cosh(x) ** (-N * MU)
    yp = -N * MU * np.tanh(x) * y
    u = y / h
    up = (yp - w * y) / h
    upp = (((N * N - 1.0) * q + 2.0 * w * w) * y
           - 2.0 * w * yp) / h
    z = w * y - yp / (N * N)
    zp = w * (yp - w * y)
    zpp = ((q - 2.0 * w * w) * yp
           + ((N * N - 2.0) * w * q + 2.0 * w ** 3) * y)

    psrc = 0.5 * (KANG ** 2 * u * u + N * N * z * z)
    psrcp = KANG ** 2 * u * up + N * N * z * zp
    psrcpp = (KANG ** 2 * (up * up + u * upp)
              + N * N * (zp * zp + z * zpp))
    aux = KANG * u * up + N * z * zp
    auxp = KANG * (up * up + u * upp) + N * (zp * zp + z * zpp)
    c = 0.5 * h * psrc
    cp = 0.5 * (v * psrc + h * psrcp)
    cpp = 0.5 * (q * h * psrc + 2.0 * v * psrcp + h * psrcpp)
    j = h * v * psrc + 0.5 * h * h * psrcp - 0.5 * M * h * h * aux
    jp = ((v * v + q * h * h) * psrc
          + 2.0 * h * v * psrcp + 0.5 * h * h * psrcpp
          - M * h * v * aux - 0.5 * M * h * h * auxp)
    quadratic_x = (1.0 - 1.0 / (N * N)) * up * up + zp * zp
    f = -(M * M / 4.0) * h * h * quadratic_x - jp
    return dict(h=h, v=v, p=p, q=q, w=w, y=y, yp=yp,
                u=u, up=up, upp=upp, z=z, zp=zp, zpp=zpp,
                P=psrc, Pp=psrcp, Ppp=psrcpp,
                C=c, Cp=cp, Cpp=cpp, J=j, Jp=jp, f=f)


def scalar_second_field(s, eta, ep, epp, eppp, fprime, jsecond):
    h, v, q, w = (s[k] for k in ("h", "v", "q", "w"))
    qp = 2.0 * A * np.tanh(s["x"]) / np.cosh(s["x"]) ** 2
    wp = q - w * w
    wpp = qp - 2.0 * w * wp
    ur = eta / h
    urp = (ep - w * eta) / h
    urpp = (epp - 2.0 * w * ep + (2.0 * w * w - q) * eta) / h
    ut = (s["C"] - ur) / M
    utp = (s["Cp"] - urp) / M
    utpp = (s["Cpp"] - urpp) / M
    uz = w * eta - ep / (M * M) + s["J"] / (M * M)
    uzp = wp * eta + w * ep - epp / (M * M) + s["Jp"] / (M * M)
    uzpp = (wpp * eta + 2.0 * wp * ep + w * epp
            - eppp / (M * M) + jsecond / (M * M))
    return np.stack([ur, ut, uz]), np.stack([urp, utp, uzp]), np.stack([urpp, utpp, uzpp])


def frame_jets(c, cx, cxx, frequency, theta):
    """Value and coordinate jets in the orthonormal moving cylindrical frame."""
    co = np.cos(frequency * theta)[None, :]
    si = np.sin(frequency * theta)[None, :]
    ar, at, az = (c[k, :, None] for k in range(3))
    ax, tx, zx = (cx[k, :, None] for k in range(3))
    axx, txx, zxx = (cxx[k, :, None] for k in range(3))
    k = frequency
    value = np.stack([ar * co, at * si, az * co], axis=-1)
    dx = np.stack([ax * co, tx * si, zx * co], axis=-1)
    dxx = np.stack([axx * co, txx * si, zxx * co], axis=-1)
    dt = np.stack([-(k * ar + at) * si,
                   (ar + k * at) * co, -k * az * si], axis=-1)
    dxt = np.stack([-(k * ax + tx) * si,
                    (ax + k * tx) * co, -k * zx * si], axis=-1)
    dtt = np.stack([-((k * k + 1) * ar + 2 * k * at) * co,
                    -(2 * k * ar + (k * k + 1) * at) * si,
                    -k * k * az * co], axis=-1)
    return value, dx, dt, dxx, dxt, dtt


def tensor_operator_norm(a, b, c):
    radius = np.sqrt((0.5 * (a - c)) ** 2 + b * b)
    center = 0.5 * (a + c)
    return np.maximum(np.abs(center + radius), np.abs(center - radius))


def norm_arrays(jets, s):
    val, dx, dt, dxx, dxt, dtt = jets
    h, v, p, q, w = (s[k][:, None] for k in ("h", "v", "p", "q", "w"))
    lam = h * h / p
    gx = q * h * v / (p * p) - 2.0 * w
    gt = h * v / (p * p)
    du = lam[..., None] * dx
    dv = h[..., None] * dt
    aa = np.sum(du * du, axis=-1)
    bb = np.sum(du * dv, axis=-1)
    cc = np.sum(dv * dv, axis=-1)
    grad = np.sqrt(tensor_operator_norm(aa, bb, cc))
    h11 = (lam * lam)[..., None] * (dxx - gx[..., None] * dx)
    h12 = (lam * h)[..., None] * (dxt + w[..., None] * dt)
    h22 = (h * h)[..., None] * (dtt - gt[..., None] * dx)
    # Frobenius of this vector-valued bilinear tensor is an upper bound for
    # its bilinear operator norm at the sampled point.
    hess_frob = np.sqrt(np.sum(h11 * h11 + 2 * h12 * h12 + h22 * h22, axis=-1))
    return np.linalg.norm(val, axis=-1), grad, hess_frob


def update_peak(record, key, values, x, theta=None):
    flat = int(np.argmax(values))
    at = np.unravel_index(flat, values.shape)
    value = float(values[at])
    old = record.get(key)
    if old is None or value > old["value"]:
        entry = dict(value=value, x=float(x[at[0]]))
        if theta is not None and len(at) > 1:
            entry["theta"] = float(theta[at[1]])
        record[key] = entry


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--length", type=float, default=8.0)
    ap.add_argument("--bvp-tol", type=float, default=1e-10)
    ap.add_argument("--radial-samples", type=int, default=1601)
    ap.add_argument("--angles", type=int, default=96)
    ap.add_argument("--out", type=Path, default=Path(
        "topics/visible-flex-exact-nearby/notes/2026-11-10-poschl-teller-second-order-diagnostic.json"))
    args = ap.parse_args()

    def background_rhs(x, state):
        h, v, z = state
        q = 2.0 - A / math.cosh(x) ** 2
        return [v, q * h, 1.0 / (h * h)]

    background = solve_ivp(background_rhs, (0.0, args.length), [1.0, 0.0, 0.0],
                           method="DOP853", rtol=2e-13, atol=2e-14, dense_output=True)
    if not background.success:
        raise RuntimeError(background.message)

    def get_source(x):
        hvz = background.sol(x)
        return source(np.asarray(x), hvz[0], hvz[1])

    def rhs(x, state):
        s = get_source(x)
        return np.vstack([state[1], M * M * s["q"] * state[0] - s["f"]])

    def jac(x, state):
        s = get_source(x)
        out = np.zeros((2, 2, x.size))
        out[0, 1] = 1.0
        out[1, 0] = M * M * s["q"]
        return out

    def bc(left, right):
        return np.array([left[1], right[1] + M * MU * right[0]])

    mesh = np.linspace(0.0, args.length, 401)
    solution = solve_bvp(rhs, bc, mesh, np.zeros((2, mesh.size)),
                         fun_jac=jac, tol=args.bvp_tol, bc_tol=1e-12,
                         max_nodes=20000, verbose=0)
    if not solution.success:
        raise RuntimeError(solution.message)

    xgrid = np.unique(np.concatenate([
        np.linspace(0.0, args.length, args.radial_samples),
        solution.x,
        0.5 * (solution.x[:-1] + solution.x[1:])]))
    theta = 2.0 * math.pi * np.arange(args.angles) / args.angles
    epsilons = [0.01, 0.05, 0.1]
    report = dict(
        kind="floating_diagnostic_not_proof",
        theorem="R8 true whole-line inverse; finite BVP below is only an approximation",
        parameters=dict(mu=MU, A=A, first_mode=N, second_mode=M,
                        length=args.length, bvp_tol=args.bvp_tol,
                        radial_samples=int(xgrid.size), angular_samples=args.angles,
                        epsilons=epsilons),
        versions=dict(numpy=np.__version__, scipy=scipy.__version__),
        background=dict(method="DOP853", rtol=2e-13, atol=2e-14,
                        nfev=background.nfev, success=background.success),
        bvp=dict(success=solution.success, message=solution.message,
                 niter=solution.niter, nodes=int(solution.x.size),
                 max_rms_residual=float(np.max(solution.rms_residuals)),
                 boundary="eta'(0)=0; eta'(L)+6sqrt(2)eta(L)=0",
                 boundary_residual=bc(solution.y[:, 0], solution.y[:, -1]).tolist(),
                 eta_at_zero=float(solution.sol(0.0)[0])),
        limitations=[
            "No directed rounding or interval arithmetic.",
            "Finite interval Robin condition approximates the true whole-line inverse.",
            "Metric values use derivatives of the scalar cubic BVP polynomial itself.",
            "Raw cubic spline jets are not claimed to define a global C2 vector field.",
            "ODE-jet norm diagnostics approximate the smooth exact field from R8.",
            "Only finite sampled x/theta grids; no certified global supremum.",
            "No claim of exact nonlinear isometry, fixed open caps, or 5% bending."],
        scalar={}, fields={"Z": {}, "Y_raw_polynomial": {}, "Y_ODE_jets": {}},
        epsilon_diagnostics={str(e): {} for e in epsilons})

    for start in range(0, xgrid.size, 64):
        x = xgrid[start:start + 64]
        s = get_source(x)
        s["x"] = x
        eta = solution.sol(x)[0]
        ep = solution.sol(x, 1)[0]
        epp = solution.sol(x, 2)[0]
        eppp = solution.sol(x, 3)[0]
        state_ep = solution.sol(x)[1]
        qp = 2.0 * A * np.tanh(x) / np.cosh(x) ** 2
        step = 1e-25
        cs = source(x + 1j * step,
                    s["h"] + 1j * step * s["v"],
                    s["v"] + 1j * step * s["q"] * s["h"])
        fp = np.imag(cs["f"]) / step
        jpp = np.imag(cs["Jp"]) / step
        ode_epp = M * M * s["q"] * eta - s["f"]
        ode_eppp = M * M * (qp * eta + s["q"] * ep) - fp

        for key, vals in [
            ("abs_eta", np.abs(eta)), ("abs_eta_prime", np.abs(ep)),
            ("abs_source", np.abs(s["f"])),
            ("actual_scalar_ode_defect", np.abs(-epp + M * M * s["q"] * eta - s["f"])),
            ("spline_first_derivative_vs_state", np.abs(ep - state_ep))]:
            update_peak(report["scalar"], key, vals, x)

        zc = np.stack([s["u"], -s["u"] / N, s["z"]])
        zcx = np.stack([s["up"], -s["up"] / N, s["zp"]])
        zcxx = np.stack([s["upp"], -s["upp"] / N, s["zpp"]])
        yc, ycx, ycxx = scalar_second_field(s, eta, ep, epp, eppp, fp, jpp)
        yoc, yocx, yocxx = scalar_second_field(s, eta, ep, ode_epp, ode_eppp, fp, jpp)
        zj = frame_jets(zc, zcx, zcxx, N, theta)
        yj = frame_jets(yc, ycx, ycxx, M, theta)
        yoj = frame_jets(yoc, yocx, yocxx, M, theta)
        for label, jets in [("Z", zj), ("Y_raw_polynomial", yj), ("Y_ODE_jets", yoj)]:
            for key, vals in zip(["C0", "C1_operator", "C2_Frobenius_upper"],
                                 norm_arrays(jets, s)):
                update_peak(report["fields"][label], key, vals, x, theta)

        h, v, p = (s[k][:, None] for k in ("h", "v", "p"))
        zeros = np.zeros_like(h)
        xx = np.stack([-v / h**2, zeros, 1.0 / h**2], axis=-1)
        xt = np.stack([zeros, 1.0 / h, zeros], axis=-1)
        zx, zt, yx, yt = zj[1], zj[2], yj[1], yj[2]
        yox, yot = yoj[1], yoj[2]
        base_e = p**2 / h**4
        base_g = 1.0 / h**2
        mean_zx = 0.5 * np.sum(zcx * zcx, axis=0)[:, None]
        mean_yx = 0.5 * np.sum(ycx * ycx, axis=0)[:, None]
        mean_yox = 0.5 * np.sum(yocx * yocx, axis=0)[:, None]

        def mean_angular(c, k):
            ar, at, az = c
            return 0.5 * ((k * ar + at)**2 + (ar + k * at)**2 + (k * az)**2)[:, None]
        mean_zt = mean_angular(zc, N)
        mean_yt = mean_angular(yc, M)
        mean_yot = mean_angular(yoc, M)

        q2e = 2.0 * np.sum(xx * yx, axis=-1) + np.sum(zx*zx, axis=-1) - mean_zx
        q2f = (np.sum(xx * yt, axis=-1) + np.sum(xt * yx, axis=-1)
               + np.sum(zx * zt, axis=-1))
        q2g = 2.0 * np.sum(xt * yt, axis=-1) + np.sum(zt*zt, axis=-1) - mean_zt
        q2norm = tensor_operator_norm(q2e / base_e, q2f / np.sqrt(base_e * base_g), q2g / base_g)
        update_peak(report["scalar"], "quadratic_cancellation_defect_relative", q2norm, x, theta)

        for eps in epsilons:
            rec = report["epsilon_diagnostics"][str(eps)]
            fx = xx + eps*zx + eps*eps*yx
            ft = xt + eps*zt + eps*eps*yt
            gb_e = base_e + eps*eps*mean_zx + eps**4*mean_yx
            gb_g = base_g + eps*eps*mean_zt + eps**4*mean_yt
            re = np.sum(fx*fx, axis=-1) - gb_e
            rf = np.sum(fx*ft, axis=-1)
            rg = np.sum(ft*ft, axis=-1) - gb_g
            rnorm = tensor_operator_norm(re/gb_e, rf/np.sqrt(gb_e*gb_g), rg/gb_g)
            update_peak(rec, "actual_nonzero_metric_relative", rnorm, x, theta)

            c3e = 2.0*np.sum(zx*yx, axis=-1)
            c3f = np.sum(zx*yt + yx*zt, axis=-1)
            c3g = 2.0*np.sum(zt*yt, axis=-1)
            c4e = np.sum(yx*yx, axis=-1) - mean_yx
            c4f = np.sum(yx*yt, axis=-1)
            c4g = np.sum(yt*yt, axis=-1) - mean_yt
            xe = eps**2*q2e + eps**3*c3e + eps**4*c4e
            xf = eps**2*q2f + eps**3*c3f + eps**4*c4f
            xg = eps**2*q2g + eps**3*c3g + eps**4*c4g
            consistency = tensor_operator_norm((re-xe)/gb_e, (rf-xf)/np.sqrt(gb_e*gb_g), (rg-xg)/gb_g)
            update_peak(rec, "direct_vs_expansion_roundoff_relative", consistency, x, theta)

            fxo = xx + eps*zx + eps*eps*yox
            fto = xt + eps*zt + eps*eps*yot
            gbo_e = base_e + eps*eps*mean_zx + eps**4*mean_yox
            gbo_g = base_g + eps*eps*mean_zt + eps**4*mean_yot
            roe = np.sum(fxo*fxo, axis=-1) - gbo_e
            rof = np.sum(fxo*fto, axis=-1)
            rog = np.sum(fto*fto, axis=-1) - gbo_g
            ron = tensor_operator_norm(roe/gbo_e, rof/np.sqrt(gbo_e*gbo_g), rog/gbo_g)
            update_peak(rec, "ODE_jet_nonzero_metric_relative", ron, x, theta)
            delta = tuple(eps*a + eps*eps*b for a, b in zip(zj, yoj))
            for key, vals in zip(["correction_C0", "correction_C1_operator",
                                  "correction_C2_Frobenius_upper"], norm_arrays(delta, s)):
                update_peak(rec, key, vals, x, theta)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(dict(output=str(args.out), bvp=report["bvp"], scalar=report["scalar"],
                          fields=report["fields"],
                          epsilon_diagnostics=report["epsilon_diagnostics"]),
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
