#!/usr/bin/env python3
"""Actual two-end finite Frenet BVP retaining the first 32 R225 core modes.

Core modes 33..M are unknown support coefficients. This is a new metric/core,
not same-g refinement of R225. The endpoint removes an axisymmetric WKB
growing projection of each high mode; it does not assert an exact stable
manifold or complete closure. No filtering or altered RHS is used.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import gzip
import hashlib
import importlib.util
import json
import math
import time
from fractions import Fraction
from pathlib import Path
import numpy as np
import scipy
from scipy.integrate import solve_bvp
import scipy.integrate._bvp as bvp_backend
from scipy.interpolate import CubicHermiteSpline, interp1d
from scipy.sparse.linalg import splu

HERE = Path(__file__).resolve().parent


def module(name, file):
    spec = importlib.util.spec_from_file_location(name, HERE / file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


outward = module('highcore_outward', 'geometry_20261114_r225_outward_probe.py')
flat = module('highcore_flat', 'alternative-neck-flatturn.py')


def domain_safe_newton(n, m, h, col_fun, bc, jac, y, p, B, bvp_tol, bc_tol):
    """Backtrack the original collocation residual without accepting NaN.

    Uses the affine-invariant Newton merit employed by scipy.solve_bvp.
    Compared with SciPy 1.17.0's four backtracks, allow sixteen and retain
    the previous valid iterate if none is admissible. The differential
    equation and collocation equations themselves are unchanged.
    """
    tol_r = (2/3)*h*.05*bvp_tol
    col_res, ymid, f, fmid = col_fun(y, p)
    bc_res = bc(y[:, 0], y[:, -1], p)
    residual = np.r_[col_res.ravel(order='F'), bc_res]
    njev = 0
    recompute = True
    singular = False
    for iteration in range(20):
        if not np.all(np.isfinite(residual)):
            print(json.dumps(dict(event='newton_invalid_current', iteration=iteration)), flush=True)
            return y, p, True
        if recompute:
            J = jac(y, p, ymid, f, fmid, bc_res)
            njev += 1
            try:
                lu = splu(J)
            except RuntimeError:
                singular = True
                break
            step = lu.solve(residual)
            cost = float(step @ step)
        ys = step[:m*n].reshape((n, m), order='F')
        ps = step[m*n:]
        alpha = 1.
        accepted = False
        for trial in range(17):
            yn = y-alpha*ys
            pn = p-alpha*ps
            if B is not None:
                yn[:, 0] = B @ yn[:, 0]
            crn, ymn, fn, fmn = col_fun(yn, pn)
            bcn = bc(yn[:, 0], yn[:, -1], pn)
            rn = np.r_[crn.ravel(order='F'), bcn]
            if np.all(np.isfinite(rn)):
                sn = lu.solve(rn)
                cn = float(sn @ sn)
                if cn < (1-.4*alpha)*cost or (cn == 0 and cost == 0):
                    accepted = True
                    break
            alpha *= .5
        if not accepted:
            print(json.dumps(dict(event='newton_backtracking_failed', iteration=iteration,
                                  max_bc=float(np.max(abs(bc_res))),
                                  max_collocation=float(np.max(abs(col_res))))), flush=True)
            break
        y, p = yn, pn
        col_res, ymid, f, fmid, bc_res, residual = crn, ymn, fn, fmn, bcn, rn
        print(json.dumps(dict(event='newton', iteration=iteration, alpha=alpha,
                              max_bc=float(np.max(abs(bc_res))),
                              max_collocation=float(np.max(abs(col_res))))), flush=True)
        if np.all(abs(col_res) < tol_r*(1+abs(fmid))) and np.all(abs(bc_res) < bc_tol):
            break
        if njev >= 8:
            break
        if alpha == 1:
            step, cost, recompute = sn, cn, False
        else:
            recompute = True
    return y, p, singular


def read(path):
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw)


def resize(y, old, new):
    y = np.asarray(y)
    return np.concatenate((y[:new+1], y[old+1:old+new+1], y[2*old+1:2*old+new+2]))


def make_profile(law, coast, target, curvature):
    old = outward.control.HermiteOutward(law['velocity'], law['length'], law['k0']).profile
    start = law['length']
    a0, v0, acc0 = old(start)
    assert abs(acc0) < 1e-12
    seg = flat.turn(math.asin(v0), math.asin(target), curvature)
    join = start + coast
    ajoin = a0 + v0 * coast
    end = join + seg['length']

    def profile(s):
        if s <= start:
            return old(s)
        if s <= join:
            return a0 + v0 * (s-start), v0, 0.
        if s >= end:
            return ajoin + seg['dr'] + target*(s-end), target, 0.
        u = (s-join)/seg['length']
        theta = float(flat.phase(seg, u))
        theta_s = np.sign(seg['p1']-seg['p0'])*seg['K']*float(flat.ramp(u, seg['turn_ramp'])[0])
        return ajoin + seg['length']*float(flat.integral(seg, u)), math.sin(theta), math.cos(theta)*theta_s
    return profile, dict(coast=coast, target_speed=target, turn=seg, join=join, whole_turn_end=end)


class BatchedFlow:
    def __init__(self, probe):
        self.q = probe
        self.calls = self.jacobians = 0
        self.started = time.time()
        self.profiles = {}
        self.checkpoint = None

    def __call__(self, x, y):
        self.calls += 1
        q = self.q
        M = q.M
        r, t, z = y[:M+1].T, y[M+1:2*M+1].T, y[2*M+1:].T
        R, T = r @ q.C, t @ q.Sn[1:]
        Rp, Tp, Zp = r @ q.C1, t @ q.S1[1:], z @ q.C1
        Rpp, Tpp, Zpp = r @ q.C2, t @ q.S2[1:], z @ q.C2
        d = np.stack((Rp-T, Tp+R, Zp), axis=-1)
        dd = np.stack((Rpp-2*Tp-R, Tpp+2*Rp-T, Zpp), axis=-1)
        lam2 = np.sum(d*d, axis=-1)
        tangent = d / np.sqrt(lam2)[..., None]
        normal_raw = dd - np.sum(dd*tangent, axis=-1)[..., None]*tangent
        nn = np.sqrt(np.sum(normal_raw*normal_raw, axis=-1))
        normal = normal_raw / nn[..., None]
        binormal = np.cross(tangent, normal)
        cache_key = np.asarray(x, dtype=float).tobytes()
        if cache_key not in self.profiles:
            self.profiles[cache_key] = np.asarray([q.profile(float(s)) for s in x])
        prof = self.profiles[cache_key]
        alpha = -prof[:, 1, None] / (prof[:, 0, None]*(nn/lam2))
        # Invalid trial points remain invalid. scipy's backtracking sees NaN;
        # no clipped square root, spectral filter, or changed PDE is used.
        with np.errstate(invalid='ignore'):
            velocity = alpha[..., None]*normal + np.sqrt(1-alpha*alpha)[..., None]*binormal
        rr = (2/q.N)*(velocity[..., 0] @ q.C.T)
        rr[:, 0] *= .5
        tt = (2/q.N)*(velocity[..., 1] @ q.Sn[1:].T)
        zz = (2/q.N)*(velocity[..., 2] @ q.C.T)
        zz[:, 0] *= .5
        return np.concatenate((rr, tt, zz), axis=1).T

    def jac(self, x, y):
        self.jacobians += 1
        if self.checkpoint is not None and x[0] == 0:
            snapshot = dict(scope='Unconverged Newton iterate; no solver success is implied.',
                            M=self.q.M, N=self.q.N, mesh=x.tolist(), states=y.T.tolist(),
                            rhs=self(x, y).T.tolist(), jacobian_call=self.jacobians)
            self.checkpoint.write_bytes(gzip.compress((json.dumps(snapshot)+'\n').encode(), mtime=0))
        n, m = y.shape
        ans = np.empty((n, n, m))
        h = 1e-25
        for j in range(n):
            yc = y.astype(complex)
            yc[j] += 1j*h
            ans[:, j] = self(x, yc).imag/h
        print(json.dumps(dict(event='jacobian', count=self.jacobians, nodes=m,
                              seconds=time.time()-self.started)), flush=True)
        return ans


def main():
    source_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    ap = argparse.ArgumentParser()
    ap.add_argument('--seed', type=Path, required=True)
    ap.add_argument('--M', type=int, default=48)
    ap.add_argument('--N', type=int, default=512)
    ap.add_argument('--end', type=float, default=.98)
    ap.add_argument('--coast', type=float, default=.05)
    ap.add_argument('--target-speed', type=float, default=-.6)
    ap.add_argument('--curvature', type=float, default=4.)
    ap.add_argument('--base-step', type=float, default=.0125)
    ap.add_argument('--refined-start', type=float, default=.7)
    ap.add_argument('--prefix-refined-step', type=float, default=.003125)
    ap.add_argument('--turn-step', type=float, default=.002)
    ap.add_argument('--tol', type=float, default=2e-6)
    ap.add_argument('--max-nodes', type=int, default=180)
    ap.add_argument('--terminal', choices=['wkb', 'cone'], default='wkb')
    ap.add_argument('--warm', type=Path)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    seed_hash = hashlib.sha256(args.seed.read_bytes()).hexdigest()
    seed = read(args.seed)
    if not 32 < args.M <= seed['M']:
        raise ValueError('Keep all 32 core modes and at least one unknown higher core mode')
    identity = seed['metric_identity']
    c = np.array([float(Fraction(v)) for v in identity['coefficients_rational']])
    law = identity['law']
    q = outward.FullCoreProbe(c, args.M, args.N, law['velocity'], law['length'], law['k0'])
    q.profile, turn = make_profile(law, args.coast, args.target_speed, args.curvature)
    assert turn['join'] < args.end <= turn['whole_turn_end']
    oldM = seed['M']
    ss = np.r_[seed['entrance_s'], seed['stable_turn_s'][1:]]
    yy = np.array([resize(v, oldM, args.M) for v in seed['entrance_states'] + seed['stable_turn_states'][1:]])
    unique = np.r_[True, np.diff(ss) > 1e-14]
    ss, yy = ss[unique], yy[unique]
    ff = np.array([q.fun(float(s), y) for s, y in zip(ss, yy)])
    interp = interp1d(ss, yy, axis=0, kind='linear')
    join = turn['join']
    mesh = np.unique(np.r_[np.linspace(0, args.refined_start, int(np.ceil(args.refined_start/args.base_step))+1),
                           np.linspace(args.refined_start, join, int(np.ceil((join-args.refined_start)/args.prefix_refined_step))+1),
                           np.linspace(join, args.end, int(np.ceil((args.end-join)/args.turn_step))+1),
                           law['length']])
    def seed_at(points):
        points = np.asarray(points)
        guess = interp(np.minimum(points, ss[-1]))
        after = points > ss[-1]
        # Homothetic latitude extension is only an initial guess. It keeps a
        # valid Frenet point domain without propagating truncated high modes.
        # Its nonzero metric/PDE residual is subsequently solved, not hidden.
        aa = q.profile(float(ss[-1]))[0]
        anchor = yy[-1].copy()
        mean_index = 2*args.M+1
        anchor_mean = anchor[mean_index]
        anchor[mean_index] = 0
        for i in np.flatnonzero(after):
            rnow, vnow, _ = q.profile(float(points[i]))
            guess[i] = (rnow/aa)*anchor
            guess[i, mean_index] = anchor_mean + (points[i]-ss[-1])*math.sqrt(1-vnow*vnow)
        return guess
    initial = seed_at(mesh)
    if args.warm:
        warm = read(args.warm)
        if warm['M'] != args.M:
            raise ValueError('Warm M differs')
        wp = CubicHermiteSpline(warm['mesh'], np.array(warm['states']), np.array(warm['rhs']), axis=0)
        within = mesh <= warm['mesh'][-1]
        initial[within] = wp(mesh[within])
        initial[~within] = np.array(warm['states'][-1]) + (mesh[~within]-warm['mesh'][-1])[:, None]*np.array(warm['rhs'][-1])
    flow = BatchedFlow(q)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    flow.checkpoint = args.out.with_name(args.out.name.removesuffix('.json.gz')+'-newton-checkpoint.json.gz')
    for refinement in range(8):
        f0 = flow(mesh, initial.T)
        if not np.all(np.isfinite(f0)):
            bad = mesh[np.any(~np.isfinite(f0), axis=0)]
            raise FloatingPointError(f'Initial node domain is invalid at {bad.tolist()}')
        h = np.diff(mesh)
        mids = .5*(mesh[:-1]+mesh[1:])
        ymid = .5*(initial[:-1]+initial[1:])-(h[:, None]/8)*(f0[:, 1:]-f0[:, :-1]).T
        bad = np.any(~np.isfinite(flow(mids, ymid.T)), axis=0)
        if not np.any(bad):
            break
        added = mids[bad]
        if len(mesh)+len(added) > args.max_nodes:
            raise FloatingPointError('Initial collocation midpoint needs more than max-nodes')
        mesh = np.unique(np.r_[mesh, added])
        initial = seed_at(mesh)
    else:
        raise FloatingPointError('Could not construct valid collocation midpoint seed')
    # Independent entry-point check: same mathematical RHS before invoking BVP.
    test = flow(mesh[:5], initial[:5].T).T
    batched_error = max(float(np.max(abs(a-b))) for a, b in zip(test, [q.fun(float(s), y) for s, y in zip(mesh[:5], initial[:5])]))
    if batched_error > 2e-13:
        raise ArithmeticError(f'Batched RHS mismatch {batched_error}')
    M = args.M
    freq = q.freq[1:]
    high = np.arange(33, M+1)
    aend, vend, accend = q.profile(args.end)
    beta = np.sqrt(1-vend*vend)
    nn = 2*high
    if args.terminal == 'wkb':
        if accend >= 0:
            raise ValueError('WKB terminal needs a genuinely positive-Gauss-curvature endpoint')
        A = -accend/beta
        B = (accend + (nn*nn-vend*vend)/aend)/beta
        lamplus = (vend/aend + np.sqrt((vend/aend)**2 + 4*A*B))/2
        left_zeta = B/lamplus
        left_eta = np.ones_like(left_zeta)
        norm = np.sqrt(left_zeta**2+1)
        left_zeta /= norm
        left_eta /= norm
    else:
        left_zeta = np.ones(len(high))
        left_eta = np.zeros(len(high))
        lamplus = np.zeros(len(high))
    br = left_zeta*vend-left_eta*beta
    bz = left_zeta*beta+left_eta*vend

    def bc(ya, yb):
        return np.r_[ya[0]-1, ya[1:33]-c,
                     ya[M+1:2*M+1]+freq*ya[1:M+1], ya[2*M+1:],
                     br*yb[high]+bz*yb[2*M+1+high]]

    def bcjac(ya, yb):
        left = np.zeros((q.n, q.n))
        right = np.zeros_like(left)
        left[:33, :33] = np.eye(33)
        idx = np.arange(M)
        left[33+idx, 1+idx] = freq
        left[33+idx, M+1+idx] = 1
        idx = np.arange(M+1)
        left[33+M+idx, 2*M+1+idx] = 1
        idx = np.arange(len(high))
        right[34+2*M+idx, high] = br
        right[34+2*M+idx, 2*M+1+high] = bz
        return left, right

    begin = time.time()
    print(json.dumps(dict(event='start', M=M, N=args.N, nodes=len(mesh), end=args.end,
                          initial_bc=float(np.max(abs(bc(initial[0], initial[-1])))),
                          rhs_crosscheck=batched_error,
                          terminal_lamplus_range=[float(lamplus.min()), float(lamplus.max())])), flush=True)
    bvp_backend.solve_newton = domain_safe_newton
    sol = solve_bvp(flow, bc, mesh, initial.T, fun_jac=flow.jac, bc_jac=bcjac,
                    tol=args.tol, bc_tol=1e-11, max_nodes=args.max_nodes, verbose=2)
    actual_c = sol.y[1:M+1, 0]
    q.coefficients = actual_c
    q.rho0 = 1 + ((1-q.freq[1:]**2)*actual_c) @ q.C[1:]
    q.hmajor = 1+float(actual_c.sum())
    q.hminor = 1+float(np.sum(actual_c*(-1.)**np.arange(1, M+1)))
    q.gap = q.hmajor-q.hminor
    q.witness = np.array([0., q.hmajor, 0.])
    extra = actual_c[32:]
    eps = float(np.sum((1+2*high)*abs(extra)))
    rho_fee = float(np.sum(((2*high)**2-1)*abs(extra)))
    rows = []
    for s, y in zip(sol.x, sol.y.T):
        try:
            rows.append(q.stats(float(s), y))
        except Exception as exc:
            rows.append(dict(s=float(s), diagnostic_error=repr(exc)))
    good = [r for r in rows if 'metric_sample' in r]
    report = dict(scope=__doc__, status=int(sol.status), message=sol.message,
                  success=bool(sol.success), M=M, N=args.N, end=args.end,
                  seconds=time.time()-begin, flow_calls=flow.calls,
                  jacobian_calls=flow.jacobians, batched_rhs_crosscheck=batched_error,
                  seed_sha256=seed_hash, scipy_version=scipy.__version__,
                  original_metric_identity=identity, turn=turn,
                  terminal=dict(kind=args.terminal, modes=high.tolist(), r_weights=br.tolist(),
                                z_weights=bz.tolist(), axisymmetric_growing_rates=lamplus.tolist()),
                  parameters=vars(args) | {'seed':str(args.seed),'warm':str(args.warm) if args.warm else None,'out':str(args.out)},
                  mesh=sol.x.tolist(), states=sol.y.T.tolist(), rhs=flow(sol.x, sol.y).T.tolist(),
                  collocation_rms_max=float(np.max(sol.rms_residuals)),
                  boundary_residual_max=float(np.max(abs(bc(sol.y[:, 0], sol.y[:, -1])))),
                  core=dict(original_first_32_preserved_in_boundary_equations=True,
                            high_support_coefficients=extra.tolist(),
                            coefficient_max=float(np.max(abs(extra))),
                            uniform_core_displacement_fee=eps,
                            rho_uniform_fee=rho_fee,
                            core_witness_gap_fee=2*eps,
                            new_axis_support_gap=q.gap,
                            rho_sample_min=float(q.rho0.min()),
                            rho_sample_max=float(q.rho0.max())),
                  rows=rows,
                  summary=dict(valid_sample_rows=len(good),
                               metric_sample=max((r['metric_sample'] for r in good), default=None),
                               kappa_sample=max((r['surface_kappa_sample'] for r in good), default=None),
                               reflected_prefix_D_sample=2*max((r['ball_radius_max'] for r in good), default=0),
                               smallest_domain_margin=min((r['margin'] for r in good), default=None)),
                  source_sha256=source_hash)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    encoded = (json.dumps(report, indent=2)+'\n').encode()
    args.out.write_bytes(gzip.compress(encoded, mtime=0) if args.out.suffix=='.gz' else encoded)
    print(json.dumps({k: report[k] for k in ('success','status','message','seconds','collocation_rms_max','boundary_residual_max','core','summary')}), flush=True)


if __name__ == '__main__':
    main()
