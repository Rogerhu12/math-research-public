#!/usr/bin/env python3
"""Use a saved complete linear response as an explicit new-design warm guess.

The successful source checkpoint remains the only claimed solution. This
adapter changes only the initial guess of the existing same-chart triple or
free-q4 solver. Nonlinear equations, domain checks, tolerance and acceptance
are unchanged. Optional inspection evaluates the whole finite collocation
mesh and an explicitly defined C2 cubic warm image, without a Newton factor.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import argparse
import gc
import gzip
import hashlib
import io
import json
from pathlib import Path
import sys
import types
from types import SimpleNamespace
import numpy as np
from scipy.integrate import _bvp
from scipy.interpolate import CubicSpline

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def principal(Fs, Fp, Fss, Fsp, Fpp):
    normal = np.cross(Fs, Fp)
    area = np.linalg.norm(normal, axis=2)
    normal /= area[:, :, None]
    E = np.sum(Fs*Fs, axis=2)
    F = np.sum(Fs*Fp, axis=2)
    G = np.sum(Fp*Fp, axis=2)
    L = np.sum(Fss*normal, axis=2)
    M = np.sum(Fsp*normal, axis=2)
    N = np.sum(Fpp*normal, axis=2)
    det = E*G-F*F
    H = (G*L-2*F*M+E*N)/(2*det)
    K = (L*N-M*M)/det
    discriminant = np.maximum(H*H-K, 0.)
    return np.maximum(abs(H+np.sqrt(discriminant)), abs(H-np.sqrt(discriminant))), area


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--tangent-response', type=Path, required=True)
    parser.add_argument('--tangent-direction', choices=('boost_speed', 'actual_q4'), required=True)
    parser.add_argument('--tangent-inspect-output', type=Path)
    opts, remaining = parser.parse_known_args()
    sys.argv = [sys.argv[0]] + remaining
    if '--third-support' not in remaining or '--restart' not in remaining:
        raise ValueError('An explicit c6 target and successful restart are required')
    target = float(remaining[remaining.index('--third-support')+1])
    restart = Path(remaining[remaining.index('--restart')+1])
    response = json.loads(opts.tangent_response.read_text())
    companion = opts.tangent_response.with_name(opts.tangent_response.stem+'-inspection-summary.json')
    provenance = json.loads(companion.read_text())
    if (not response.get('inspection_only') or response.get('nonlinear_solution')
            or provenance['warm_start']['metadata_sha256'] != sha(restart)):
        raise ValueError('The response must refer to the same successful restart')
    row = next(row for row in response['rows'] if row['direction']==opts.tangent_direction)
    array_records = response['exchange_diagnostic']['warm_only_tangent_arrays']
    input_hashes = {str(f): sha(f) for f in (opts.tangent_response, companion, restart, Path(__file__))}

    def load_array(suffix):
        records = [r for r in array_records if r['file'].endswith(suffix+'.npy.gz')]
        if len(records) != 1:
            raise ValueError('Ambiguous response array '+suffix)
        record = records[0]
        path = Path(record['file'])
        payload = path.read_bytes()
        if hashlib.sha256(payload).hexdigest() != record['sha256']:
            raise ValueError('Response array hash differs')
        input_hashes[str(path)] = record['sha256']
        return np.load(io.BytesIO(gzip.decompress(payload)), allow_pickle=False)

    base_t = load_array('-t')
    base_y = load_array('-warm-y')
    base_p = load_array('-warm-p')
    # Avoid matching the separate h/2 direction checkpoint.
    name = '-direction-'+opts.tangent_direction
    records = [r for r in array_records if r['file'].endswith(name+'.npy.gz')
               and not r['file'].endswith('-half'+name+'.npy.gz')]
    if len(records) != 1:
        raise ValueError('Ambiguous complete response direction')
    record = records[0];path = Path(record['file']);payload = path.read_bytes()
    if hashlib.sha256(payload).hexdigest() != record['sha256']:
        raise ValueError('Complete direction hash differs')
    input_hashes[str(path)] = record['sha256']
    direction = np.load(io.BytesIO(gzip.decompress(payload)), allow_pickle=False)
    dc6 = float(row['core_derivative'][2])
    c0 = np.asarray(response['baseline']['coefficients'])
    step = (target-c0[2])/dc6
    adapter = HERE/('strong_triple_same_chart_bvp.py' if opts.tangent_direction=='boost_speed'
                   else 'strong_free_q4_bvp.py')
    adapter_source = adapter.read_text()
    input_hashes[str(adapter)] = hashlib.sha256(adapter_source.encode()).hexdigest()

    def form_guess(obj, t, y, p, record, saved):
        n, m = base_y.shape
        if (obj.M != response['modes'] or obj.nt != response['angular']
                or obj.q != c0[0] or n != obj.n or len(t) != m):
            raise ValueError('The response state dimension/gauge/mesh differs')
        if obj.cfg != provenance['base_profile']:
            raise ValueError('The numerical chart base profile must remain the response base')
        if np.max(abs(t-base_t)) > 2e-12:
            raise ValueError('The numerical reference meridian coordinates changed')
        np.testing.assert_array_equal(obj.ref_coeff, response['baseline']['numerical_reference_coefficients'])
        if saved.rec['frozen_profile'] != response['baseline']['profile']:
            raise ValueError('The successful physical profile differs')
        dp = direction[n*m:]
        proposed = p.copy()
        proposed[:2] = base_p[:2]+step*dp[:2]
        proposed[3:] = base_p[3:]+step*dp[3:]
        if opts.tangent_direction == 'boost_speed':
            proposed[2] = (saved.rec['frozen_profile']['boost_speed']
                           -obj.cfg['boost_speed']+step)
        else:
            proposed[2] = (c0[1]+step)/obj.pscale[1]
        guess = base_y+step*direction[:n*m].reshape((n, m), order='F')
        obj.select(proposed)
        f = obj.flow(proposed[0])
        s, _ = obj.chart(t, proposed[0])
        correction = obj.initial(proposed)-guess[:, 0]
        guess += correction[:, None]*np.maximum(0., 1-s/(f.Tu/2))[None, :]**3
        predicted_core = c0+step*np.asarray(row['core_derivative'])
        if np.max(abs(obj._core.coefficients-predicted_core)) > 2e-16:
            raise ValueError('Actual warm core does not match the recorded tangent')
        info = dict(scope=__doc__, warm_only=True, source_solution=str(restart),
                    source_sha256=input_hashes.copy(), external_direction=opts.tangent_direction,
                    direction_step=step, target_c6=target, predicted_core=predicted_core.tolist(),
                    predicted_profile=dict(f.cfg), finite_state_shape=list(guess.shape),
                    numerical_t_max_difference=float(np.max(abs(t-base_t))),
                    exact_inlet_second_order_correction_max=float(np.max(abs(correction))),
                    correction_definition='The same C2 cubic cutoff as the production warm loader; explicitly an additional initial-guess deformation.',
                    solver_equations_changed=False, tolerance_changed=False)
        record['full_tangent_warm'] = info
        obj.design_provenance['full_tangent_warm'] = info
        obj._strong_tangent_info = info
        obj._strong_baseline_parameters = p.copy()
        # The triple/free-q4 p2 layout is already correct in p; baseline p0/1
        # and all free core modes are inherited from the successful source.
        obj._strong_baseline_parameters[:2] = base_p[:2]
        obj._strong_baseline_parameters[3:] = base_p[3:]
        return t, guess, proposed, record

    def geometry(obj, t, y, p):
        obj.select(p)
        f = obj.flow(p[0])
        s_nodes, _ = obj.chart(t, p[0])
        poly = CubicSpline(s_nodes, y, axis=1)
        sol = SimpleNamespace(x=s_nodes, y=y, p=p, sol=poly)
        s = np.unique(np.r_[np.linspace(0., f.end, 241), f.breakpoints, f.end])
        prefix = f._alternative_neck
        boost_end = max(segment['s1'] for segment in prefix.segments if segment['kind']=='boost')
        for segment in prefix.segments:
            if segment['kind']=='boost' or (
                    segment.get('s0', f.end) >= boost_end-1e-12
                    and segment.get('s0', f.end) < prefix.loop_begin):
                s = np.unique(np.r_[s, segment['s0']+segment['length']*np.linspace(0., 1., 33)])
        N = 256
        heights = f.height_integral(sol, s, N, 6)
        B, B1, B2 = f.basis(N)
        maximum = 0.
        diameter = 0.
        height_max = 0.
        margin = 1.
        area_min = np.inf
        witness = None
        for first in range(0, len(s), 8):
            sl = slice(first, first+8);ss = s[sl]
            Y, Yp, Ypp = poly(ss), poly(ss, 1), poly(ss, 2)
            frame, Fsp, dW = f.velocity_s(ss, Y, Yp, B1, B2)
            g = frame['geo']
            Fs = g['s1']+obj.q*f.values(Yp, B)
            Fs[:, :, 2] += np.mean(frame['V'][:, :, 2], axis=1)[:, None]
            Fss = g['s2']+obj.q*f.values(Ypp, B)
            Fss[:, :, 2] += np.mean(dW[:, :, 2], axis=1)[:, None]
            kappa, area = principal(Fs, frame['d'], Fss, Fsp, frame['dd'])
            points = g['pos']+obj.q*f.values(Y, B)
            points[:, :, 2] += heights[sl, None]
            index = np.unravel_index(np.argmax(kappa), kappa.shape)
            if kappa[index] > maximum:
                maximum = float(kappa[index])
                witness = dict(s=float(ss[index[0]]), psi=float(index[1]*2*np.pi/N))
            diameter = max(diameter, 2*float(np.linalg.norm(points, axis=2).max()))
            height_max = max(height_max, float(abs(points[:, :, 2]).max()))
            margin = min(margin, float(frame['margin'].min()))
            area_min = min(area_min, float(area.min()))
        return dict(scope='Explicit C2 cubic interpolation of the complete warm coefficients in physical s, with the production mean-height integral. This is an unsolved warm image, not the final PDE-jet quintic reconstruction or a curvature/reach certificate.',
                    radial_samples=len(s), angular=N, diameter_sample=diameter,
                    kappa_sample=maximum, kappa_times_D_sample=maximum*diameter,
                    reciprocal_kappa_D_sample=1/(maximum*diameter),
                    height_max_sample=height_max, frenet_margin_min_sample=margin,
                    area_min_sample=area_min, curvature_witness=witness)

    def inspect(fun, bc, x, y, p, **kw):
        obj = fun.__self__
        result = dict(scope=__doc__, inspection_only=True, nonlinear_solution=False,
                      warm=obj._strong_tangent_info, modes=obj.M, angular=obj.nt,
                      nodes=len(x), source_sha256=input_hashes.copy())
        try:
            h = np.diff(x)
            cr, ym, ff, fm = _bvp.collocation_fun(fun, y, p, x, h)
            br = bc(y[:, 0], y[:, -1], p)
            spline = _bvp.create_spline(y, ff, x, h)
            rms = _bvp.estimate_rms_residuals(fun, spline, x, h, p, 1.5*cr/h, fm)
            result['finite_domain_passed'] = True
            result['full_collocation'] = dict(
                scaled_max=float(np.max(abs(cr)/(h[None, :]*(1+abs(fm))))),
                boundary_max=float(np.max(abs(br))),
                inlet_max=float(np.max(abs(br[:obj.n]))),
                terminal_max=float(np.max(abs(br[obj.n:]))),
                rms_max=float(np.max(rms)),
                radial_sites_evaluated=len(x)+3*(len(x)-1),
                scope='All nodes, Simpson midpoints and both residual-quadrature sites of every interval; finite angular resolution only, no continuous domain enclosure.')
            gc.collect()
            result['baseline_cubic_geometry'] = geometry(
                obj, base_t, base_y, obj._strong_baseline_parameters)
            gc.collect()
            result['warm_cubic_geometry'] = geometry(obj, x, y, p)
        except (FloatingPointError, ValueError) as error:
            result['finite_domain_passed'] = False
            result['inspection_error'] = repr(error)
        opts.tangent_inspect_output.write_text(json.dumps(result, indent=2)+'\n')
        print(json.dumps(result), flush=True)
        raise RuntimeError('Full tangent warm inspection complete; no BVP requested')

    def install(runner):
        load = runner.module

        def module(name, path):
            loaded = load(name, path)
            if Path(path).name != 'root_dual_core_bvp.py':
                return loaded
            original_main = loaded.main

            def entry():
                original_factory = loaded.make_dual

                def factory(*args, **kwargs):
                    Base = original_factory(*args, **kwargs)

                    class TangentWarm(Base):
                        def restart_from(self, saved, pullback, nodes, scale='linear'):
                            t, y, p, record = super().restart_from(saved, pullback, nodes, scale)
                            return form_guess(self, t, y, p, record, saved)

                    return TangentWarm

                loaded.make_dual = factory
                original_main()

            loaded.main = entry
            if opts.tangent_inspect_output:
                loaded.solve_bvp = inspect
            return loaded

        runner.module = module

    anchor = 'runner.module=module;runner.main()'
    if adapter_source.count(anchor) != 1:
        raise ValueError('Production adapter entry changed')
    source = adapter_source.replace(anchor,
        'runner.module=module;_tangent_install(runner);runner.main()')
    module = types.ModuleType('strong_saved_tangent_entry')
    module.__file__ = str(adapter)
    module.__dict__['_tangent_install'] = install
    exec(compile(source, str(adapter), 'exec'), module.__dict__)
    module.main()


if __name__ == '__main__':
    main()
