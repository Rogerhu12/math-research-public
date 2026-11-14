#!/usr/bin/env python3
"""One full Jacobian at an accepted triple-design raw collocation state.

Actual q1/q4/c6 inlet columns are differentiated at fixed representation
gauge, reference angle chart and numerical meridian reference. Delta/LB/vp
and every higher core mode respond through the unchanged full collocation
system. No nonlinear solve, new surface, or fixed-g refinement is claimed.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import gc
import gzip
import hashlib
import io
import json
import math
from pathlib import Path
import resource
import sys
import time
from types import SimpleNamespace
import numpy as np
import scipy.integrate as integrate
from scipy.integrate import _bvp
import root_block_collocation as blocks
import root_radial_batching as radial
import root_raw_collocation as raw
import strong_triple_same_chart_bvp as entry

HERE = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def memory():
    result = dict(peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    for line in Path('/proc/self/status').read_text().splitlines():
        if line.startswith('VmRSS:'):
            result['rss_kib'] = int(line.split()[1])
    return result


def condition(matrix):
    singular = np.linalg.svd(matrix, compute_uv=False)
    return dict(dimension=list(matrix.shape), sigma_max=float(singular[0]),
                sigma_min=float(singular[-1]),
                condition_2=float(singular[0]/singular[-1]))


def save_array(prefix, name, value):
    stream = io.BytesIO()
    np.save(stream, np.asarray(value), allow_pickle=False)
    payload = gzip.compress(stream.getvalue(), mtime=0)
    path = Path(str(prefix)+'-'+name+'.npy.gz')
    if path.exists() or len(payload) >= 5_000_000:
        raise ValueError('Existing or oversized response array '+str(path))
    path.write_bytes(payload)
    return dict(file=str(path), sha256=hashlib.sha256(payload).hexdigest(),
                bytes=len(payload), shape=list(np.shape(value)))


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--response-output', type=Path, required=True)
    parser.add_argument('--response-final-checkpoint', type=Path, required=True)
    parser.add_argument('--response-fields', default='vu,descending_turn_curvature')
    parser.add_argument('--radial-batch-size', type=int, default=16)
    parser.add_argument('--collocation-batch-size', type=int, default=12)
    opts, remaining = parser.parse_known_args()
    if opts.response_output.exists():
        raise ValueError('A fresh response output is required')
    if '--raw-collocation-restart' not in remaining:
        raise ValueError('Use the final accepted raw collocation checkpoint')
    raw_path = Path(remaining[remaining.index('--raw-collocation-restart')+1])
    payload = opts.response_final_checkpoint.read_bytes()
    final = json.loads(gzip.decompress(payload) if opts.response_final_checkpoint.suffix == '.gz' else payload)
    if not final.get('solver_success') or final.get('audit_pending', True):
        raise ValueError('The linked final physical checkpoint is not accepted and audited')
    if final['raw_collocation_checkpoint']['sha256'] != digest(raw_path):
        raise ValueError('The final physical package names a different raw state')
    if not 1 <= opts.radial_batch_size <= 48 or not 1 <= opts.collocation_batch_size <= 24:
        raise ValueError('Only the already compared smaller batches are allowed')
    prefix = opts.response_output.with_suffix('')
    names = ('strong_triple_control_response.py', 'strong_triple_same_chart_bvp.py',
             'strong_neck_bvp.py', 'strong_flow_lru.py', 'root_triple_core_bvp.py',
             'root_dual_core_bvp.py', 'root_block_collocation.py',
             'root_radial_batching.py', 'strong_block_qr.py', 'root_raw_collocation.py')
    hashes = {name: digest(HERE/name) for name in names}
    hashes[str(opts.response_final_checkpoint)] = digest(opts.response_final_checkpoint)
    hashes[str(raw_path)] = digest(raw_path)
    functions = (radial.value, radial.state_jacobian, blocks.prepare_sys)
    defaults = tuple(f.__defaults__ for f in functions)
    if defaults != ((48,), (48,), (24,)):
        raise ValueError('Original batching defaults changed')
    radial.value.__defaults__ = radial.state_jacobian.__defaults__ = (opts.radial_batch_size,)
    blocks.prepare_sys.__defaults__ = (opts.collocation_batch_size,)
    original_solve = integrate.solve_bvp

    def inspect(fun, bc, x, y, p, **kwargs):
        started = time.time()
        obj = fun.__self__
        if tuple(obj.control_names) != ('delta', 'boost_length', 'boost_speed'):
            raise ValueError('The exact triple layout is required')
        solution, raw_record = raw.read(raw_path, obj, SimpleNamespace(tol=kwargs['tol']))
        if not solution.success:
            raise ValueError('The raw nonlinear solve was not accepted')
        equal = {name: bool(np.array_equal(value, getattr(solution, name)))
                 for name, value in (('x', x), ('y', y), ('p', p))}
        if not all(equal.values()):
            raise ValueError('Solver entry is not the exact accepted raw state')
        if raw_record['identity']['profile'] != final['frozen_profile']:
            raise ValueError('Raw/final physical profiles differ')
        obj.select(p)
        obj.initial(p)
        n, m, k = y.shape[0], len(x), len(p)
        h = np.diff(x)
        c0 = np.asarray(obj._core.coefficients).copy()
        if not np.array_equal(c0, final['core']['coefficients']):
            raise ValueError('Actual accepted core coefficients differ')
        if obj.q != final['gauge_amplitude'] or not np.array_equal(obj.ref_coeff, final['chart_reference_coefficients']):
            raise ValueError('Representation gauge or angular reference changed')
        if not np.array_equal(obj._neck_knots, final['numerical_meridian_chart']['reference_t']):
            raise ValueError('Numerical meridian reference changed')
        initial_profile = dict(obj.flow(p[0]).cfg)

        def bounded_jac(*args):
            try:
                return kwargs['fun_jac'](*args)
            finally:
                gc.collect()

        col, jac = blocks.prepare_sys(n, m, k, fun, bc, bounded_jac,
                                     kwargs['bc_jac'], x, h)
        cr, ym, ff, fm = col(y, p)
        br = bc(y[:, 0], y[:, -1], p)
        baseline = dict(profile=initial_profile, coefficients=c0.tolist(),
            gauge_amplitude=obj.q, numerical_reference_coefficients=obj.ref_coeff.tolist(),
            numerical_reference_knots=obj._neck_knots.tolist(),
            scaled_collocation_max=float(np.max(abs(cr)/(h[None, :]*(1+abs(fm))))),
            boundary_max=float(np.max(abs(br))), raw_state_bitwise_equal=equal,
            accepted_rms_max=float(np.max(solution.rms_residuals)))
        print(json.dumps(dict(event='triple_response_jacobian_begin', nodes=m,
            modes=obj.M, angular=obj.nt, baseline=baseline, **memory())), flush=True)
        begin = time.time()
        matrix = jac(y, p, ym, ff, fm, br)
        jac_seconds = time.time()-begin
        begin = time.time()
        factor = blocks.DirectBlockQRFactor(matrix, n, m, k)
        factor_seconds = time.time()-begin
        gc.collect()
        print(json.dumps(dict(event='triple_response_factor', nodes=m,
            jacobian_seconds=jac_seconds, factor_seconds=factor_seconds, **memory())), flush=True)
        packed, unused_pivots = factor.final_lu
        coarse = (np.tril(packed, -1)+np.eye(len(packed)))@np.triu(packed)
        units = np.r_[np.full(2*n, obj.q), np.ones(3), obj.pscale[2:]]
        root_condition = dict(scope='Balanced QR endpoint/parameter matrix only; not the full global Jacobian or a geometric fold certificate.',
            numerical_units=condition(coarse),
            physical_correction_and_control_units=condition(coarse/units[None, :]),
            column_units=units.tolist())
        rows, arrays, directions = [], [], {}

        def residual_vector():
            cr0, unused_mid, unused_f, unused_fm = col(y, p)
            return np.r_[cr0.ravel(order='F'), bc(y[:, 0], y[:, -1], p)]

        def record(name, forcing, half=None, widths=None, inlet_check=None):
            direction = -factor.solve(forcing)
            dp = direction[n*m:]
            dc = np.zeros(obj.M)
            dc[3:] = dp[3:]*obj.pscale[2:]
            inlet_index = dict(actual_q1=0, actual_q4=1, actual_c6=2).get(name)
            if inlet_index is not None:
                dc[inlet_index] = 1.
            ay = abs(direction[:n*m]).reshape(m, n)
            ap = abs(dp)
            scale = 0.
            for lo in range(0, m-1, 16):
                hi = min(lo+16, m-1)
                denom = (np.einsum('mij,mj->mi', abs(matrix.a[lo:hi]), ay[lo:hi])
                         +np.einsum('mij,mj->mi', abs(matrix.b[lo:hi]), ay[lo+1:hi+1])
                         +np.einsum('mik,k->mi', abs(matrix.c[lo:hi]), ap)
                         +abs(forcing[lo*n:hi*n]).reshape(hi-lo, n))
                scale = max(scale, float(denom.max()))
            scale = max(scale, float(np.max(abs(matrix.boundary_a)@ay[0]
                +abs(matrix.boundary_b)@ay[-1]+abs(matrix.boundary_p)@ap
                +abs(forcing[n*(m-1):]))), np.finfo(float).tiny)
            edge = np.r_[direction[:n], direction[n*(m-1):n*m], dp]
            exchanged = coarse.copy()
            exchanged[:, 2*n+2] = -coarse@edge
            exchange_units = units.copy()
            exchange_units[2*n+2] = 1.
            row = dict(direction=name, parameter_derivative=dp.tolist(),
                physical_profile_derivative={key: float(dp[j]) for j, key in enumerate(obj.control_names)},
                core_derivative=dc.tolist(),
                equation_relative_backward_error=float(np.max(abs(matrix.matvec(direction)+forcing))/scale),
                physical_correction_derivative_max=float(np.max(abs(direction[:n*m]))*obj.q),
                correction_scope='q*dy is the correction field only; total positions also include the changing reference geometry.',
                vp_column_exchange=dict(determinant_ratio=float(-dp[2]),
                    physical_units=condition(exchanged/exchange_units[None, :]),
                    scope='Replace the vp unknown by one unit of this actual external direction at the unchanged baseline; no nonlinear solution.'))
            if inlet_index is None:
                row['physical_profile_derivative'][name] = 1.
            if inlet_check is not None:
                row['inlet_analytic_vs_centered_check'] = inlet_check
            if half is not None:
                second = -factor.solve(half)
                scale_vector = np.r_[np.full(n*m, obj.q), np.ones(3), obj.pscale[2:]]
                first_scaled, second_scaled = scale_vector*direction, scale_vector*second
                row['finite_difference_steps'] = widths
                row['half_step_response_relative_difference'] = float(np.max(abs(first_scaled-second_scaled))/max(np.max(abs(first_scaled)), np.finfo(float).tiny))
                arrays.append(save_array(prefix, 'half-direction-'+name, second))
            arrays.append(save_array(prefix, 'direction-'+name, direction))
            directions[name] = direction
            rows.append(row)
            print(json.dumps(dict(event='triple_control_response', **row)), flush=True)

        obj.select(p)
        obj.initial(p)
        flow = obj.flow(p[0])
        angular = max(2048, 128*obj.M)
        inlet = flow.general_core_chart.inlet_geometry(angular)
        basis, unused_b1, unused_b2 = flow.basis(angular)
        derivatives = flow.project(obj._core.parameter_derivatives(inlet['theta']), basis)/obj.q
        from fixed_metric_mode3_core import PlanarSupportCore
        for name, index in (('actual_q1', 0), ('actual_q4', 1), ('actual_c6', 2)):
            forcing = np.zeros(n*m+k)
            forcing[n*(m-1):n*m] = -derivatives[:, index]
            width = 2e-6*max(.1, abs(c0[index]))
            cp, cm = c0.copy(), c0.copy()
            cp[index] += width
            cm[index] -= width
            plus = PlanarSupportCore(cp[0], cp[1:], 2).evaluate(inlet['theta'])['F']
            minus = PlanarSupportCore(cm[0], cm[1:], 2).evaluate(inlet['theta'])['F']
            finite = flow.project(((plus-minus)/(2*width))[None, :, :], basis)[:, 0]/obj.q
            discrepancy = float(np.max(abs(finite-derivatives[:, index])))
            normalized = discrepancy/max(1., float(np.max(abs(derivatives[:, index]))))
            if normalized > 2e-7:
                raise RuntimeError('Actual prescribed-core derivative check failed')
            record(name, forcing, inlet_check=dict(width=width, max_abs=discrepancy,
                max_normalized=normalized, gauge_and_reference_fixed=True))
        for field in filter(None, opts.response_fields.split(',')):
            if field in obj.control_names or field not in obj.cfg:
                raise ValueError('An external physical field is required: '+field)
            original_value = obj.cfg[field]
            width = 2e-6*max(.1, abs(original_value))
            differences = []
            try:
                for step in (width, width/2):
                    obj.cfg[field] = original_value+step
                    obj._flow_key = None
                    plus = residual_vector()
                    gc.collect()
                    obj.cfg[field] = original_value-step
                    obj._flow_key = None
                    minus = residual_vector()
                    gc.collect()
                    differences.append((plus-minus)/(2*step))
            finally:
                obj.cfg[field] = original_value
                obj._flow_key = None
                obj.select(p)
                obj.flow(p[0])
                obj.initial(p)
                gc.collect()
            record(field, differences[0], differences[1], [width, width/2])
        # These are only local combinations of complete solved tangent fields.
        # The c6-held path and the alternative free-q4 path can be compared
        # without inventing a physical-control derivative at another state.
        candidates = []
        by_name = {row['direction']: row for row in rows}
        for dq in (.0025, .005):
            choices = [('q4-linear-c6-held', dict(actual_q1=dq, actual_q4=-dq/(10*math.sqrt(2))))]
            q4_response = by_name['actual_q4']['parameter_derivative'][2]
            c6_response = by_name['actual_c6']['parameter_derivative'][2]
            if abs(q4_response) > 1e-14:
                q4_step = -dq*by_name['actual_q1']['parameter_derivative'][2]/q4_response
                choices.append(('free-q4-vp-fixed-c6-held', dict(actual_q1=dq, actual_q4=q4_step)))
            if abs(c6_response) > 1e-14:
                weights = dict(actual_q1=dq, actual_q4=-dq/(10*math.sqrt(2)))
                weights['actual_c6'] = -sum(weight*by_name[key]['parameter_derivative'][2] for key, weight in weights.items())/c6_response
                choices.append(('q4-linear-vp-fixed-natural-c6', weights))
            for name, weights in choices:
                direction = sum(weight*directions[key] for key, weight in weights.items())
                dp = direction[n*m:]
                dc = sum(weight*np.asarray(by_name[key]['core_derivative']) for key, weight in weights.items())
                proposed = c0+dc
                profile = dict(initial_profile)
                for j, key in enumerate(obj.control_names):
                    profile[key] += float(dp[j])
                try:
                    core = PlanarSupportCore(proposed[0], proposed[1:], 2)
                    core_result = dict(valid=True, summary=core.summary())
                except (ValueError, FloatingPointError) as error:
                    core_result = dict(valid=False, error=repr(error))
                item = dict(name=name, actual_q1_step=dq, weights=weights,
                    physical_profile=profile, predicted_actual_core=proposed.tolist(),
                    core=core_result, scope='Full linear tangent predictor only; nonlinear field/domain/geometry and acceptance remain unpaid.')
                candidates.append(item)
        result = dict(scope=__doc__, finished=True, inspection_only=True, nonlinear_solution=False,
            final_checkpoint=str(opts.response_final_checkpoint), raw_baseline=str(raw_path),
            modes=obj.M, angular=obj.nt, nodes=m, baseline=baseline, rows=rows,
            reduced_root_condition=root_condition, tangent_arrays=arrays,
            candidate_predictions=candidates, source_sha256=hashes,
            radial_batch_size=opts.radial_batch_size, collocation_batch_size=opts.collocation_batch_size,
            jacobian_seconds=jac_seconds, factor_seconds=factor_seconds,
            seconds=time.time()-started, memory=memory())
        opts.response_output.write_text(json.dumps(result, indent=2)+'\n')
        raise RuntimeError('Triple response inspection complete; no nonlinear solve requested')

    integrate.solve_bvp = inspect
    sys.argv = [sys.argv[0]]+remaining
    try:
        entry.main()
        if not opts.response_output.exists() or not json.loads(opts.response_output.read_text()).get('finished'):
            raise RuntimeError('Triple response did not complete')
    finally:
        integrate.solve_bvp = original_solve
        for function, default in zip(functions, defaults):
            function.__defaults__ = default


if __name__ == '__main__':
    main()
