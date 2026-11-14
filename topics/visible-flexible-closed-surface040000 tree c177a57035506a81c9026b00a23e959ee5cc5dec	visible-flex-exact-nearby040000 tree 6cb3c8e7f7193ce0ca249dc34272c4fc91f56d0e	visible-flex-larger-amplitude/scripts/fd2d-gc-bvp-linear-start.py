#!/usr/bin/env python3
"""Actual finite fixed-g GC BVP with a labelled linear-tail initializer.

This computes the nonlinear PREFIX equations.  The tail height-to-slope
operator is only the selected finite LINEAR graph, so a returned root is
an initializer, never a solved nonlinear tail or a closed strong surface.
The constant n cut equation omitted by the finite boundary count is always
reported explicitly, together with angular monodromy and full sampled
Codazzi residuals.  No hidden replacement of a true nonlinear boundary.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import gzip
import io
import json
from pathlib import Path
import time
import traceback
import numpy as np
from scipy.integrate import solve_bvp
from fd2d_frozen_ellipse_candidate import Candidate
from fd2d_balanced_oval_core import BalancedOvalCore
from fd2d_gc_intrinsic import FixedNormalReference, identity, LD, PI
from fd2d_gc_blended import BlendedIntrinsicGC
from fd2d_gc_bvp_ports import FiniteLinearTailStarter, ProjectedTailPort
import fd2d_gc_bvp_newton as newton

HERE = Path(__file__).resolve().parent


def write_npz(path, **arrays):
    buffer = io.BytesIO()
    np.savez_compressed(buffer, **arrays)
    data = buffer.getvalue()
    if len(data) > 1_000_000:
        path = path.with_name(path.name+'.gz')
        data = gzip.compress(data, compresslevel=6)
    if len(data) >= 5_000_000:
        raise ValueError('The individual checkpoint is too large; split it before saving')
    temporary = path.with_name(path.name+'.tmp')
    temporary.write_bytes(data)
    temporary.replace(path)
    return identity(path)


class Problem:
    def __init__(self, flow, core, linear):
        self.flow, self.core = flow, core
        self.K, self.q = flow.K, flow.dimension
        self.seed, self.seed_projection = flow.central_state(core)
        self.central_directions, self.central_weighted_means = flow.central_reference_directions()
        self.starter = FiniteLinearTailStarter(linear, self.K)
        self.tail = ProjectedTailPort(flow, self.starter)
        self.height_scale = self.starter.height_scale

    def height(self, parameters):
        return parameters[self.K:]*self.height_scale

    def fun(self, s, y, p):
        return self.flow.rhs(s, y)

    def fun_jac(self, s, y, p):
        return self.flow.jacobian(s, y), np.zeros((self.q, len(p), y.shape[1]))

    def bc(self, ya, yb, p):
        target, _, diagnostic = self.tail.evaluate(self.height(p))
        if diagnostic['minimum_n'] <= 0:
            raise FloatingPointError('The selected positive n branch is invalid at the tail port')
        return np.r_[ya-self.seed-self.central_directions@p[:self.K], yb[1:]-target[1:]]

    def bc_jac(self, ya, yb, p):
        target, tangent, _ = self.tail.evaluate(self.height(p), jacobian=True)
        rows = 2*self.q-1
        left, right = np.zeros((rows, self.q)), np.zeros((rows, self.q))
        params = np.zeros((rows, 2*self.K))
        left[:self.q] = np.eye(self.q)
        right[self.q:, 1:] = np.eye(self.q-1)
        params[:self.q, :self.K] = -self.central_directions
        params[self.q:, self.K:] = -tangent[1:]*self.height_scale
        return left, right, params

    def diagnostics(self, x, y, p):
        target, _, tail = self.tail.evaluate(self.height(p))
        n = self.flow.decode(y)[:, 0]
        return dict(boundary_maximum=float(abs(self.bc(y[:, 0], y[:, -1], p)).max()),
                    omitted_constant_n_cut_difference=float(y[0, -1]-target[0]),
                    all_cut_coefficients_maximum_difference=float(abs(y[:, -1]-target).max()),
                    core_parameter_l1=float(abs(p[:self.K]).sum()),
                    core_parameter_maximum=float(abs(p[:self.K]).max()),
                    maximum_worker_height=float(abs(self.height(p)).max()),
                    minimum_n_grid=float(n.min()), tail=tail)


def initial_mesh(candidate, max_step, blend):
    knots = sorted(set([float(x) for x in candidate.breaks]+list(blend)))
    return np.unique(np.concatenate([np.linspace(a, b, max(1, int(np.ceil((b-a)/max_step)))+1)
                                     for a, b in zip(knots[:-1], knots[1:])]))


def initial_field(problem, x, anchor):
    f, core = problem.flow, problem.core
    aa, ap, _ = f.profile(x)
    rotational = np.sqrt(1-ap*ap)/aa
    initial = f.decode(problem.seed)
    core_ratio = initial[:, 0]*f.a0
    material_nodes = np.r_[np.asarray(f.u, dtype=float), 2*np.pi]
    end = f.candidate.end
    anchor_s, anchor_n, anchor_m, anchor_rot = None, None, None, None
    if anchor is not None:
        data = np.load(anchor)
        old_mode = int(data['modes'])
        old_K = old_mode//2
        state = data['state'][:2*old_K+1]
        nc = np.r_[state[0], 2*state[1::2]]
        mc = -2*state[2::2]
        phase = np.asarray(f.theta[:, None], dtype=LD)*(2*np.arange(1, old_K+1))
        anchor_n = nc[0]+np.cos(phase)@nc[1:]
        anchor_m = np.sin(phase)@mc
        anchor_s = float(data['s'])
        a, v, _ = f.profile(anchor_s)
        anchor_rot = np.sqrt(1-v[0]*v[0])/a[0]
        if np.any(anchor_n <= 0):
            raise FloatingPointError('The retained finite anchor is outside the positive n chart')
    values = np.zeros((f.work, 2, len(x)), dtype=LD)
    for index, s in enumerate(x):
        U = np.asarray(f.coordinates(float(s))['u'][:, 0], dtype=float)
        seed_ratio = np.interp(U, material_nodes, np.asarray(np.r_[core_ratio, core_ratio[0]], dtype=float))
        if anchor_s is not None:
            an = np.interp(U, material_nodes, np.asarray(np.r_[anchor_n/anchor_rot, anchor_n[0]/anchor_rot], dtype=float))
            am = np.interp(U, material_nodes, np.asarray(np.r_[anchor_m, anchor_m[0]], dtype=float))
            if s <= anchor_s:
                t = np.clip((s-.2)/(anchor_s-.2), 0, 1)
                ratio = (1-t)*seed_ratio+t*an
                mixed = t*am*rotational[index]/anchor_rot
            else:
                t = (s-anchor_s)/(end-anchor_s)
                weight = t*t*(3-2*t)
                ratio = (1-weight)*an+weight
                mixed = (1-weight)*am*rotational[index]/anchor_rot
        else:
            t = np.clip((s-.2)/(end-.2), 0, 1)
            weight = t*t*(3-2*t)
            ratio, mixed = (1-weight)*seed_ratio+weight, np.zeros_like(seed_ratio)
        values[:, 0, index], values[:, 1, index] = rotational[index]*ratio, mixed
    y = f.encode(values)
    y[:, 0] = problem.seed
    return y, np.zeros(2*f.K)


def residual_screen(flow, sol):
    x = np.unique(np.r_[sol.x, (sol.x[:-1]+sol.x[1:])/2])
    worst_n, worst_m, minimum = 0., 0., np.inf
    for offset in range(0, len(x), 12):
        s = x[offset:offset+12]
        y, yp = sol.sol(s), sol.sol(s, 1)
        f = flow.fields(s, y)
        true_derivative = flow.decode(yp)
        angular = flow.derivative(np.stack((f['n'], f['m'], f['l']), axis=1))
        Rn = true_derivative[:, 0]-f['advection']*angular[:, 0]-f['inverse_b']*angular[:, 1]-f['c']*(f['l']-f['n'])
        Rm = true_derivative[:, 1]-f['advection']*angular[:, 1]-f['inverse_b']*angular[:, 2]+2*f['c']*f['m']
        worst_n, worst_m = max(worst_n, float(abs(Rn).max())), max(worst_m, float(abs(Rm).max()))
        minimum = min(minimum, float(f['n'].min()))
    return dict(radial_samples=len(x), angular_samples=flow.work,
                Rn_maximum=worst_n, Rm_maximum=worst_m, minimum_n=minimum,
                includes_unprojected_angular_equations=True,
                uses_true_piecewise_polynomial_radial_derivative=True,
                continuous_certificate=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--candidate', type=Path, required=True)
    parser.add_argument('--linear-tail', type=Path, required=True)
    parser.add_argument('--out-prefix', type=Path, required=True)
    parser.add_argument('--anchor', type=Path)
    parser.add_argument('--modes', type=int, default=95)
    parser.add_argument('--oversample', type=int, default=2)
    parser.add_argument('--blend', type=float, nargs=2, default=[.58, 1.40])
    parser.add_argument('--mesh-step', type=float, default=.025)
    parser.add_argument('--max-nodes', type=int, default=400)
    parser.add_argument('--tol', type=float, default=1e-4)
    parser.add_argument('--bc-tol', type=float, default=2e-7)
    args = parser.parse_args()
    stem = args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):
        raise FileExistsError('Use an unused BVP output prefix')
    begin = time.monotonic()
    candidate = Candidate(json.loads(args.candidate.read_text()))
    core = BalancedOvalCore()
    flow = BlendedIntrinsicGC(candidate, args.modes, args.oversample,
                             reference=FixedNormalReference(core), blend_interval=args.blend)
    problem = Problem(flow, core, json.loads(args.linear_tail.read_text()))
    x = initial_mesh(candidate, args.mesh_step, args.blend)
    y, p = initial_field(problem, x, args.anchor)
    report = dict(schema='fd2d-fixed-g-gc-linear-tail-initializer-v1', scope=__doc__,
        source=identity(__file__), intrinsic=identity(HERE/'fd2d_gc_intrinsic.py'),
        blended_intrinsic=identity(HERE/'fd2d_gc_blended.py'), ports=identity(HERE/'fd2d_gc_bvp_ports.py'),
        tail_gc_provider=identity(HERE/'fd2d_metric_tail_gc_port.py'), newton=identity(HERE/'fd2d_gc_bvp_newton.py'),
        core=identity(HERE/'fd2d_balanced_oval_core.py'), candidate=identity(args.candidate),
        linear_tail=identity(args.linear_tail), anchor=identity(args.anchor) if args.anchor else None,
        chart=flow.chart_definition(), maximum_mode=args.modes, angular_grid=flow.work,
        intrinsic_dimension=flow.dimension, initial_nodes=len(x), maximum_nodes=args.max_nodes,
        tolerances=dict(collocation=args.tol, boundary=args.bc_tol), central_projection=problem.seed_projection,
        nonlinear_tail_solved=False, closed_surface=False, initial=problem.diagnostics(x, y, p), events=[])
    report_path = stem.with_name(stem.name+'-report.json')
    progress_path = stem.with_name(stem.name+'-progress.jsonl')
    report_path.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    write_npz(stem.with_name(stem.name+'-initial.npz'), mesh=x, values=y, parameters=p)
    def observe(event, h, state, parameters, data, statistics):
        mesh = np.r_[0., np.cumsum(h)]
        row = dict(event=event, seconds=time.monotonic()-begin, nodes=len(mesh),
                   residual_maximum=float(abs(data[0]).max()), statistics=statistics,
                   **problem.diagnostics(mesh, state, parameters))
        if event == 'accepted':
            row['checkpoint'] = write_npz(stem.with_name(stem.name+'-accepted-current.npz'),
                                          mesh=mesh, values=state, parameters=parameters,
                                          rhs_nodes=data[3], central_weighted_means=problem.central_weighted_means)
        with progress_path.open('a') as stream:
            stream.write(json.dumps(row, allow_nan=False)+'\n')
        print(json.dumps({key:row[key] for key in ('event','seconds','nodes','residual_maximum',
              'boundary_maximum','omitted_constant_n_cut_difference','core_parameter_l1',
              'maximum_worker_height','minimum_n_grid')}, allow_nan=False), flush=True)
    newton.install(observe)
    print(json.dumps(dict(event='start', maximum_mode=args.modes, dimension=flow.dimension,
                          nodes=len(x), chart=flow.chart_definition(), scope=problem.starter.scope)), flush=True)
    try:
        sol = solve_bvp(problem.fun, problem.bc, x, y, p, fun_jac=problem.fun_jac,
                        bc_jac=problem.bc_jac, tol=args.tol, bc_tol=args.bc_tol,
                        max_nodes=args.max_nodes, verbose=0)
        report.update(solver_success=bool(sol.success), solver_status=int(sol.status), message=sol.message,
                      iterations=int(sol.niter), final_nodes=len(sol.x), maximum_rms_residual=float(np.max(sol.rms_residuals)),
                      final=problem.diagnostics(sol.x, sol.y, sol.p), residual_screen=residual_screen(flow, sol),
                      parameters=dict(central_curvature=sol.p[:flow.K].tolist(), worker_height=problem.height(sol.p).tolist()))
        # These shared true interpolation jets define a C1 Hermite field;
        # RHS values are retained separately and are not substituted for it.
        report['field'] = write_npz(stem.with_name(stem.name+'-field.npz'),
            mesh=sol.x, values=sol.y, first=sol.sol(sol.x, 1), rhs=problem.fun(sol.x, sol.y, sol.p),
            midpoint=(sol.x[:-1]+sol.x[1:])/2,
            midpoint_values=sol.sol((sol.x[:-1]+sol.x[1:])/2),
            midpoint_first=sol.sol((sol.x[:-1]+sol.x[1:])/2, 1),
            parameters=sol.p, central_weighted_means=problem.central_weighted_means)
        report['polynomial'] = write_npz(stem.with_name(stem.name+'-polynomial.npz'),
                                        breaks=sol.sol.x, coefficients=sol.sol.c)
    except Exception as exc:
        report.update(solver_success=False, exception=dict(type=type(exc).__name__, message=str(exc),
                                                           traceback=traceback.format_exc()))
    report.update(seconds=time.monotonic()-begin, rhs_calls=flow.calls, jvp_calls=flow.jvp_calls,
                  newton_statistics=dict(newton.STATS))
    report_path.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps({key:report.get(key) for key in ('solver_success','solver_status','message',
          'exception','final_nodes','maximum_rms_residual','final','residual_screen','seconds')}, allow_nan=False), flush=True)


if __name__ == '__main__':
    main()
