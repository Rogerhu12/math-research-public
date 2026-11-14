#!/usr/bin/env python3
"""Actual second-form type and fixed-cut characteristic sensitivities.

Floating diagnostics only. No radial metric is substituted for the actual
surface. Fixed-cut ray return is not the full turning/elliptic boundary map.
All mean columns differentiate the same loaded actual spline.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq, linprog

import poschl_teller_fourfold_series as ps
from fourfold_newton_refined import SplineNewton


def load(path):
    with np.load(path, allow_pickle=False) as f:
        if "metadata" in f.files and "vector" in f.files:
            meta = json.loads(str(f["metadata"]))
            vector = f["vector"]
        else:
            meta = None
    if meta is None:
        series = ps.load_series(path)
        return ps.make_candidate(series, 1., 1), None, None
    solver = SplineNewton(**meta["parameters"])
    return solver.candidate(vector, meta["epsilon"]), solver, vector


def evaluate_local(candidate, x, theta, third=False):
    """Same actual spline, caching only its scalar radial coefficients."""
    x, theta = np.atleast_1d(x), np.atleast_1d(theta)
    key = float(x[0]) if len(x) == 1 else None
    saved = candidate.get("_diagnostic_radial_cache")
    if key is not None and saved is not None and saved[0] == key:
        coefficients = saved[1]
    else:
        coefficients = [(m, [spline(x, nu=j).T for j in range(3)])
                        for m, spline in candidate["splines"].items()]
        if key is not None:
            candidate["_diagnostic_radial_cache"] = (key, coefficients)
    out = [np.zeros((x.size, theta.size, 3)) for _ in range(9 if third else 6)]
    for m, fields in coefficients:
        co, si = np.cos(m*theta)[None, :], np.sin(m*theta)[None, :]
        (u, t, w), (ux, tx, wx), (uxx, txx, wxx) = [
            tuple(v[:, None] for v in field) for field in fields]
        out[0] += np.stack([u*co, t*si, w*co], axis=-1)
        out[1] += np.stack([ux*co, tx*si, wx*co], axis=-1)
        out[2] += np.stack([-(m*u+t)*si, (u+m*t)*co, -m*w*si], axis=-1)
        out[3] += np.stack([uxx*co, txx*si, wxx*co], axis=-1)
        out[4] += np.stack([-(m*ux+tx)*si, (ux+m*tx)*co, -m*wx*si], axis=-1)
        out[5] += np.stack([-((m*m+1)*u+2*m*t)*co,
                           -(2*m*u+(m*m+1)*t)*si, -m*m*w*co], axis=-1)
        if third:
            out[6] += np.stack([-(m*uxx+txx)*si, (uxx+m*txx)*co,
                                -m*wxx*si], axis=-1)
            out[7] += np.stack([-((m*m+1)*ux+2*m*tx)*co,
                               -(2*m*ux+(m*m+1)*tx)*si, -m*m*wx*co], axis=-1)
            out[8] += np.stack([(m*(m*m+3)*u+(3*m*m+1)*t)*si,
                               -((3*m*m+1)*u+m*(m*m+3)*t)*co,
                               m**3*w*si], axis=-1)
    return tuple(out)


def tensors(candidate, x, theta, angular=False):
    fields = evaluate_local(candidate, x, theta, third=angular)
    f, fx, ft, fxx, fxt, ftt = fields[:6]
    raw = np.cross(ft, fx)
    jac = np.linalg.norm(raw, axis=-1)
    normal = raw / jac[..., None]
    L = np.sum(normal * fxx, axis=-1)
    M = np.sum(normal * fxt, axis=-1)
    N = np.sum(normal * ftt, axis=-1)
    jets = (fx, ft, fxx, fxt, ftt, normal, jac)
    if angular:
        raw_t = np.cross(ftt, fx)+np.cross(ft, fxt)
        normal_t = (raw_t-normal*np.sum(normal*raw_t, axis=-1)[..., None])/jac[..., None]
        dL = np.sum(normal_t*fxx+normal*fields[6], axis=-1)
        dM = np.sum(normal_t*fxt+normal*fields[7], axis=-1)
        dN = np.sum(normal_t*ftt+normal*fields[8], axis=-1)
        jets += (dL, dM, dN)
    return L, M, N, jets


def scan(candidate, x, theta):
    L, M, N, _ = tensors(candidate, x, theta)
    det = L*N-M*M
    return [dict(x=float(r), detII_min=float(det[i].min()),
                 detII_max=float(det[i].max()), N_min=float(N[i].min()),
                 N_max=float(N[i].max()),
                 sampled_all_hyperbolic=bool(det[i].max() < 0),
                 sampled_N_strict_negative=bool(N[i].max() < 0))
            for i, r in enumerate(x)]


def ray_coefficients(candidate, solver, x, theta, sign, derivatives=False):
    L, M, N, jets = tensors(candidate, [x], theta, angular=derivatives)
    L, M, N = L[0], M[0], N[0]
    q2 = M*M-L*N
    if q2.min() <= 0 or np.max(N) >= 0:
        raise ValueError("actual ray leaves sampled strictly hyperbolic N<0 chart")
    q = np.sqrt(q2)
    velocity = (-M+sign*q)/N
    if not derivatives:
        return velocity
    fx, ft, fxx, fxt, ftt, normal, jac = [v[0] for v in jets[:7]]
    Lt, Mt, Nt = [v[0] for v in jets[7:]]
    qt = (2*M*Mt-N*Lt-L*Nt)/(2*q)
    velocity_t = (-Mt+sign*qt)/N-velocity*Nt/N
    gxx = np.sum(fx*fx, axis=-1)
    gxt = np.sum(fx*ft, axis=-1)
    gtt = np.sum(ft*ft, axis=-1)
    columns = []
    for mean in solver.mean_splines:
        v, vx, vxx = [mean(np.array([x]), nu=j)[0] for j in range(3)]
        vt = np.array([0., v[0], 0.])
        vxt = np.array([0., vx[0], 0.])
        vtt = np.array([-v[0], 0., 0.])
        nx = normal@vx
        nt = normal@vt
        cx = (gtt*nx-gxt*nt)/(jac*jac)
        ct = (gxx*nt-gxt*nx)/(jac*jac)
        dn = -cx[:, None]*fx-ct[:, None]*ft
        dL = normal@vxx+np.sum(dn*fxx, axis=-1)
        dM = normal@vxt+np.sum(dn*fxt, axis=-1)
        dN = normal@vtt+np.sum(dn*ftt, axis=-1)
        dq = (2*M*dM-N*dL-L*dN)/(2*q)
        columns.append((-dM+sign*dq)/N-velocity*dN/N)
    return velocity, np.array(columns), velocity_t


def return_map(candidate, solver, cut, theta, angular_step, tolerance):
    count = len(theta)
    means = solver.mean_count
    initial = np.zeros((means+2, count))
    initial[0] = theta
    initial[1] = 1.
    calls = [0]

    def run(start, finish, sign, value):
        def fun(x, flat):
            calls[0] += 1
            val = flat.reshape(means+2, count)
            th = val[0]
            speed, columns, dtheta = ray_coefficients(candidate, solver, x, th, sign, True)
            ans = np.empty_like(val)
            ans[0] = speed
            ans[1] = dtheta*val[1]
            ans[2:] = dtheta[None, :]*val[2:]+columns
            return ans.ravel()
        result = solve_ivp(fun, (start, finish), value.ravel(), method="DOP853",
                           rtol=tolerance, atol=tolerance/20,
                           max_step=abs(finish-start)/50)
        if not result.success:
            raise RuntimeError(result.message)
        return result.y[:, -1].reshape(means+2, count)

    # N<0: sign - gives the positive reference angular velocity.
    middle = run(-cut, cut, -1., initial)
    final = run(cut, -cut, +1., middle)
    displacement = final[0]-theta
    columns = final[2:].T
    rec = dict(cut=float(cut), initial_angles=theta.tolist(),
               displacement=displacement.tolist(),
               displacement_min=float(displacement.min()),
               displacement_max=float(displacement.max()),
               angular_jacobian_min=float(final[1].min()),
               angular_jacobian_max=float(final[1].max()),
               mean_parameter_columns=columns.tolist(),
               mean_column_min=columns.min(axis=0).tolist(),
               mean_column_max=columns.max(axis=0).tolist(),
               rhs_calls=calls[0], angular_derivative="exact derivative of finite Fourier fields",
               ode_rtol=tolerance,
               meaning="fixed-cut hyperbolic round trip, not full turning reflection")
    height = np.array([sp(np.array([solver.length]))[0, 2]
                       for sp in solver.mean_splines])
    waist = np.array([sp(np.array([0.]))[0, 0] for sp in solver.mean_splines])
    rec["mean_height_column"] = height.tolist()
    rec["mean_waist_radius_column"] = waist.tolist()
    for label, constraints in [("unconstrained", []), ("fixed_mean_height", [height]),
                               ("fixed_height_and_radius", [height, waist])]:
        objective = np.r_[np.zeros(means), -1.]
        ub = np.column_stack([-columns, np.ones(count)])
        eq = None if not constraints else np.column_stack(
            [np.array(constraints), np.zeros(len(constraints))])
        solved = linprog(objective, A_ub=ub, b_ub=np.zeros(count),
                         A_eq=eq, b_eq=None if eq is None else np.zeros(len(eq)),
                         bounds=[(-1., 1.)]*means+[(None, None)], method="highs")
        if solved.success:
            direction = solved.x[:-1]
            rec[label] = dict(direction=direction.tolist(),
                              sampled_pointwise_min=float((columns@direction).min()),
                              sampled_pointwise_max=float((columns@direction).max()),
                              constraint_residual=[] if eq is None else
                              (np.array(constraints)@direction).tolist())
    return rec


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--candidate", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--angles", type=int, default=256)
    ap.add_argument("--xmax", type=float, default=.6)
    ap.add_argument("--xcount", type=int, default=121)
    ap.add_argument("--turn-bracket", type=float, nargs=2, default=[.23, .24])
    ap.add_argument("--rays", type=int, default=32)
    ap.add_argument("--cut", type=float, default=.20)
    ap.add_argument("--angular-step", type=float, default=2e-5)
    ap.add_argument("--tolerance", type=float, default=2e-8)
    ap.add_argument("--no-rays", action="store_true")
    args = ap.parse_args()
    candidate, solver, vector = load(args.candidate)
    print(json.dumps({"progress": "actual spline loaded"}), flush=True)
    theta = (np.pi/2)*np.arange(args.angles)/args.angles
    report = dict(kind="floating_actual_second_form_diagnostic_not_proof",
                  candidate=args.candidate.name,
                  sha256=hashlib.sha256(args.candidate.read_bytes()).hexdigest(),
                  angular_period=float(np.pi/2),
                  scan=scan(candidate, np.linspace(0., args.xmax, args.xcount), theta),
                  limitations=[
                      "ordinary floating arithmetic and finite angular/radial samples",
                      "detII and N refer to the actual loaded spline, not angular mean metric",
                      "fixed-cut ray return excludes both turning regions and elliptic tails",
                      "mean columns preserve saved nonmean coefficients, not nonlinear equations",
                      "no exact solution, fixed caps, rotation-number or inverse certificate"])
    roots = []
    for th in theta:
        def f(x):
            L, M, N, _ = tensors(candidate, [x], [th])
            return float((L*N-M*M)[0, 0])
        lo, hi = args.turn_bracket
        if f(lo)*f(hi) >= 0:
            roots = []
            break
        roots.append(brentq(f, lo, hi, xtol=2e-14))
    if roots:
        report["turning_roots_sample"] = dict(min=float(min(roots)), max=float(max(roots)),
                                             roots=roots,
                                             uniqueness_proved=False)
    print(json.dumps({"progress": "type scan and turning roots finished",
                      "turning_range": None if not roots else [min(roots), max(roots)]}),
          flush=True)
    if not args.no_rays:
        if solver is None:
            raise ValueError("ray sensitivities currently require new SplineNewton metadata")
        theta_ray = (np.pi/2)*np.arange(args.rays)/args.rays
        report["fixed_cut_return"] = return_map(candidate, solver, args.cut, theta_ray,
                                                 args.angular_step, args.tolerance)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({k: v for k, v in report.items()
                      if k not in ["scan", "turning_roots_sample", "fixed_cut_return"]}))
    if roots:
        print(json.dumps({"turning_range": [min(roots), max(roots)]}))
    if "fixed_cut_return" in report:
        print(json.dumps({k: v for k, v in report["fixed_cut_return"].items()
                          if k not in ["initial_angles", "displacement",
                                       "mean_parameter_columns"]}))


if __name__ == "__main__":
    main()
