#!/usr/bin/env python3
"""Positive-normal fixed-g prefix BVP, with a LINEAR tail starter only.

The exact changed dependent variables are eta=log(n/n_ref),zeta=m/n_ref.
No curvature is clipped, no target metric is changed, and no nonlinear DN
or closed surface is claimed by this initializer.  Original native cubic
data and a separately specified physical n,m Hermite reconstruction are
both retained; their distinction is explicit in the report.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import copy
import gzip
import importlib.util
import io
import json
from pathlib import Path
import sys
import numpy as np
from fd2d_gc_logshape_stable import LogShapeGC
from fd2d_gc_intrinsic import identity, LD, FixedNormalReference

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('fd2d_log_bvp_base', HERE/'fd2d-gc-bvp-linear-start.py')
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)
original_initial_field = base.initial_field


class PositiveProblem(base.Problem):
    def __init__(self, flow, core, linear):
        self.flow, self.core, self.K, self.q = flow, core, flow.K, flow.dimension
        _, self.central_weighted_means = flow.central_reference_directions()
        self.central_point_directions = np.cos(flow.theta[:, None]*flow.frequencies)-self.central_weighted_means
        self.central_n = 1/np.asarray(core.reference_radius(flow.theta), dtype=LD)
        self.starter = base.FiniteLinearTailStarter(linear, self.K)
        self.tail = base.ProjectedTailPort(flow, self.starter)
        self.height_scale = self.starter.height_scale
        self.seed = self.central_target(np.zeros(self.K), jacobian=False)[0]
        physical = flow.fields(0., self.seed)['n'][:, 0]
        self.seed_projection = dict(maximum_n_projection_difference=float(abs(physical-self.central_n).max()),
            maximum_m_projection_difference=0.,
            material_total_turn_projection_difference=float(2*np.pi*flow.a0*np.mean(flow.u_theta*(physical-self.central_n))))
        self._tail_height = self._tail_target = self._tail_tangent = None

    def central_target(self, d, jacobian=False):
        n = self.central_n+self.central_point_directions@np.asarray(d, dtype=LD)
        if np.any(n <= 0):
            raise FloatingPointError('The requested central curvature is not positive')
        a, ap, _ = self.flow.profile(0.)
        nr = np.sqrt(1-ap[0]*ap[0])/a[0]
        values = np.column_stack((np.log(n/nr), np.zeros_like(n)))
        target = self.flow.encode(values)
        tangent = None
        if jacobian:
            point = np.zeros((self.flow.work, 2, self.K), dtype=LD)
            point[:, 0] = self.central_point_directions/n[:, None]
            tangent = self.flow.encode(point)
        return target, tangent

    def tail_target(self, height, jacobian=False):
        height = np.asarray(height, dtype=float)
        if self._tail_height is None or not np.array_equal(height, self._tail_height):
            _, _, diagnostic = self.tail.evaluate(height)
            port = self.tail.cached_port
            u = self.tail.material_coordinate()
            value = port.evaluate(u)
            if np.any(value['n'] <= 0):
                raise FloatingPointError('The tail positive-n branch has failed')
            a, ap, _ = self.flow.profile(self.flow.candidate.end)
            nr = np.sqrt(1-ap[0]*ap[0])/a[0]
            target = self.flow.encode(np.column_stack((np.log(value['n']/nr), value['m']/nr)))
            self._tail_height, self._tail_target, self._tail_tangent = height.copy(), target, None
            self._tail_physical, self._tail_nr, self._tail_diagnostic = value, nr, diagnostic
        if jacobian and self._tail_tangent is None:
            columns = []
            for k in range(self.K):
                direction = np.zeros(self.K)
                direction[k] = 1
                tangent = self.tail.cached_port.jvp(self.tail.material_coordinate(), direction)
                columns.append(self.flow.encode(np.column_stack((tangent['n']/self._tail_physical['n'], tangent['m']/self._tail_nr))))
            self._tail_tangent = np.column_stack(columns)
        return self._tail_target, self._tail_tangent if jacobian else None, self._tail_diagnostic

    def bc(self, ya, yb, p):
        central, _ = self.central_target(p[:self.K])
        target, _, _ = self.tail_target(self.height(p))
        return np.r_[ya-central, yb[1:]-target[1:]]

    def bc_jac(self, ya, yb, p):
        _, central = self.central_target(p[:self.K], jacobian=True)
        _, tangent, _ = self.tail_target(self.height(p), jacobian=True)
        rows = 2*self.q-1
        left, right = np.zeros((rows, self.q)), np.zeros((rows, self.q))
        params = np.zeros((rows, 2*self.K))
        left[:self.q] = np.eye(self.q)
        right[self.q:, 1:] = np.eye(self.q-1)
        params[:self.q, :self.K] = -central
        params[self.q:, self.K:] = -tangent[1:]*self.height_scale
        return left, right, params

    def diagnostics(self, x, y, p):
        target, _, tail = self.tail_target(self.height(p))
        fields = self.flow.fields(x, y)
        end = self.flow.fields(self.flow.candidate.end, y[:, -1])
        delta = np.column_stack((end['n'][:, 0]-self._tail_physical['n'], end['m'][:, 0]-self._tail_physical['m']))
        coefficients = self.flow.encode(delta)
        return dict(boundary_maximum=float(abs(self.bc(y[:, 0], y[:, -1], p)).max()),
                    omitted_constant_n_cut_difference=float(coefficients[0]),
                    omitted_constant_eta_cut_difference=float(y[0, -1]-target[0]),
                    all_cut_coefficients_maximum_difference=float(abs(coefficients).max()),
                    core_parameter_l1=float(abs(p[:self.K]).sum()),
                    core_parameter_maximum=float(abs(p[:self.K]).max()),
                    maximum_worker_height=float(abs(self.height(p)).max()),
                    minimum_n_grid=float(fields['n'].min()),
                    maximum_abs_native_eta=float(abs(fields['eta']).max()),
                    maximum_abs_native_zeta=float(abs(fields['zeta']).max()), tail=tail)


def initial_log_field(problem, x, anchor):
    proxy = copy.copy(problem)
    proxy.seed = problem.flow.encode(np.column_stack((problem.central_n, np.zeros_like(problem.central_n))))
    y, p = original_initial_field(proxy, x, anchor)
    nm = problem.flow.decode(y)
    a, ap, _ = problem.flow.profile(x)
    nr = np.sqrt(1-ap*ap)/a
    if np.any(nm[:, 0] <= 0):
        raise FloatingPointError('The actual raw initializer is not positive')
    native = np.stack((np.log(nm[:, 0]/nr), nm[:, 1]/nr), axis=1)
    state = problem.flow.encode(native)
    state[:, 0] = problem.seed
    return state, p


def residual_screen(flow, sol):
    x = np.unique(np.r_[sol.x, (sol.x[:-1]+sol.x[1:])/2])
    worst_n, worst_m, minimum = 0., 0., np.inf
    for offset in range(0, len(x), 12):
        s = x[offset:offset+12]
        v = flow.physical_values_and_derivatives(s, sol.sol(s), sol.sol(s, 1))
        f, yp, dx = v['fields'], v['first'], v['angular']
        Rn = yp[:, 0]-f['advection']*dx[:, 0]-f['inverse_b']*dx[:, 1]-f['c']*(f['l']-f['n'])
        Rm = yp[:, 1]-f['advection']*dx[:, 1]-f['inverse_b']*dx[:, 2]+2*f['c']*f['m']
        worst_n, worst_m = max(worst_n, float(abs(Rn).max())), max(worst_m, float(abs(Rm).max()))
        minimum = min(minimum, float(f['n'].min()))
    return dict(radial_samples=len(x), angular_samples=flow.work, Rn_maximum=worst_n, Rm_maximum=worst_m,
                minimum_n=minimum, physical_variables='n=n_ref*exp(eta),m=n_ref*zeta',
                actual_chain_rule_on_native_piecewise_polynomial=True,
                continuous_certificate=False)


def load_npz(path):
    path = Path(path)
    return np.load(io.BytesIO(gzip.decompress(path.read_bytes()))) if path.suffix == '.gz' else np.load(path)


def export_physical_field(report, stem):
    data = load_npz(report['field']['path'])
    candidate = base.Candidate(json.loads(Path(report['candidate']['path']).read_text()))
    core = base.BalancedOvalCore()
    # Double the representable physical angular band without enlarging the
    # already solved native system.  Projection error is explicitly recorded.
    old_K = (data['values'].shape[0]-1)//2
    high = LogShapeGC(candidate, 4*old_K+3, 2, reference=FixedNormalReference(core),
                       blend_interval=report['chart']['blend_interval'])
    def pad(values):
        result = np.zeros((high.dimension, values.shape[1]))
        result[:old_K+1] = values[:old_K+1]
        result[high.K+1:high.K+1+old_K] = values[old_K+1:]
        return result
    outputs, projection = {}, 0.
    for prefix, key, first_key, coordinate_key in [('', 'values', 'first', 'mesh'),
                                                  ('midpoint_', 'midpoint_values', 'midpoint_first', 'midpoint')]:
        mesh, values, first = data[coordinate_key], pad(data[key]), pad(data[first_key])
        physical_values, physical_first = [], []
        for offset in range(0, len(mesh), 12):
            stop = offset+12
            result = high.physical_values_and_derivatives(mesh[offset:stop], values[:, offset:stop], first[:, offset:stop])
            v, d = high.encode(result['values']), high.encode(result['first'])
            projection = max(projection, float(abs(high.decode(v)-result['values']).max()))
            physical_values.append(v)
            physical_first.append(d)
        outputs[prefix+'values'] = np.concatenate(physical_values, axis=1)
        outputs[prefix+'first'] = np.concatenate(physical_first, axis=1)
    report['physical_field'] = base.write_npz(stem.with_name(stem.name+'-physical-field.npz'),
        mesh=data['mesh'], midpoint=data['midpoint'], parameters=data['parameters'], **outputs)
    report['physical_field'].update(maximum_mode=high.maximum_mode,
        node_projection_maximum_difference=projection,
        definition='Shared binary64 physical n,m values/true first jets define a separate C1 cubic Hermite field; include all reconstruction residual in R119.')


if __name__ == '__main__':
    base.BlendedIntrinsicGC, base.Problem = LogShapeGC, PositiveProblem
    base.initial_field, base.residual_screen = initial_log_field, residual_screen
    base.__doc__, base.__file__ = __doc__, __file__
    base.main()
    stem = Path(sys.argv[sys.argv.index('--out-prefix')+1])
    output = stem.with_name(stem.name+'-report.json')
    report = json.loads(output.read_text())
    report['native_state_representation'] = LogShapeGC.state_representation
    report['base_driver'] = identity(HERE/'fd2d-gc-bvp-linear-start.py')
    report['positive_normal_provider'] = identity(HERE/'fd2d_gc_logshape.py')
    report['stable_background_subtraction'] = identity(HERE/'fd2d_gc_logshape_stable.py')
    if 'field' in report:
        try:
            export_physical_field(report, stem)
        except Exception as exc:
            report['physical_export_failure'] = dict(type=type(exc).__name__, message=str(exc))
    output.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
