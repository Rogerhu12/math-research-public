#!/usr/bin/env python3
"""Continue actual core coefficients while keeping the representation gauge.

The prescribed q1/q4/c6 and the full saved tangent field define a new-design
warm guess. Reference charts, coefficient units and the gauge remain fixed.
The production triple BVP and its acceptance rules still solve delta/LB/vp
and all c8+ modes. A warm prediction is never an accepted surface.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import ast
import gc
import gzip
import hashlib
import io
import json
from pathlib import Path
import sys
import textwrap
import types
from types import SimpleNamespace
import numpy as np
from scipy.integrate import _bvp
from scipy.interpolate import CubicSpline
import strong_tangent_warm_bvp as prior_warm

HERE = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def document(path):
    path = Path(path)
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--response-data', type=Path, required=True)
    parser.add_argument('--candidate-name', required=True)
    parser.add_argument('--candidate-q-step', type=float, required=True)
    parser.add_argument('--tangent-inspect-output', type=Path)
    opts, remaining = parser.parse_known_args()
    if '--restart' not in remaining or '--q' not in remaining:
        raise ValueError('The successful source checkpoint and explicit fixed gauge are required')
    restart = Path(remaining[remaining.index('--restart')+1])
    final = document(restart)
    response = document(opts.response_data)
    if (not final.get('solver_success') or final.get('audit_pending', True)
            or not response.get('finished') or not response.get('inspection_only')
            or response.get('nonlinear_solution')):
        raise ValueError('An audited accepted source and a completed tangent response are required')
    if digest(restart) != response['source_sha256'][response['final_checkpoint']]:
        raise ValueError('The tangent response belongs to another physical checkpoint')
    gauge = float(remaining[remaining.index('--q')+1])
    if gauge != response['baseline']['gauge_amplitude']:
        raise ValueError('The representation gauge must stay fixed')
    matches = [row for row in response['candidate_predictions']
               if row['name'] == opts.candidate_name
               and row['actual_q1_step'] == opts.candidate_q_step]
    if len(matches) != 1:
        raise ValueError('The full-field candidate selection is ambiguous')
    candidate = matches[0]
    if not set(candidate['weights']) <= {'actual_q1', 'actual_q4', 'actual_c6'}:
        raise ValueError('This warm adapter only combines prescribed-core directions')
    target = np.asarray(candidate['predicted_actual_core'][:3], float)
    if '--third-support' in remaining:
        if float(remaining[remaining.index('--third-support')+1]) != target[2]:
            raise ValueError('The explicit third support differs from the recorded candidate')
    else:
        remaining += ['--third-support', repr(float(target[2]))]
    if '--workflow' not in remaining:
        remaining += ['--workflow', 'triple']
    elif remaining[remaining.index('--workflow')+1] != 'triple':
        raise ValueError('This is a three-control production problem')
    sys.argv = [sys.argv[0]]+remaining
    raw_path = Path(response['raw_baseline'])
    raw_record = document(raw_path)
    if (digest(raw_path) != response['source_sha256'][str(raw_path)]
            or not raw_record.get('solver_success')
            or final['raw_collocation_checkpoint']['sha256'] != digest(raw_path)):
        raise ValueError('The exact accepted raw baseline differs')
    input_paths = [Path(__file__), opts.response_data, restart, raw_path,
                   HERE/'strong_triple_same_chart_bvp.py', HERE/'strong_tangent_warm_bvp.py']
    hashes = {str(path): digest(path) for path in input_paths}

    def raw_array(name):
        item = raw_record['arrays'][name]
        answer = np.empty(int(np.prod(item['shape'])), float)
        end = 0
        for chunk in item['chunks']:
            path = raw_path.parent/chunk['file']
            if Path(chunk['file']).name != chunk['file'] or chunk['first'] != end or digest(path) != chunk['sha256']:
                raise ValueError('Invalid raw array chunk')
            with gzip.open(path, 'rb') as stream:
                value = np.load(stream, allow_pickle=False)
            if value.size != chunk['count']:
                raise ValueError('Invalid raw array chunk size')
            answer[end:end+len(value)] = value
            end += len(value)
            hashes[str(path)] = chunk['sha256']
        if end != answer.size:
            raise ValueError('Incomplete raw baseline')
        return answer.reshape(item['shape'])

    base_t, base_y, base_p = (raw_array(name) for name in ('x', 'y', 'p'))
    n, m = base_y.shape
    total = np.zeros(n*m+len(base_p))
    for name, weight in candidate['weights'].items():
        match = [a for a in response['tangent_arrays']
                 if a['file'].endswith('-direction-'+name+'.npy.gz')
                 and not a['file'].endswith('-half-direction-'+name+'.npy.gz')]
        if len(match) != 1:
            raise ValueError('Missing or ambiguous complete tangent direction')
        item = match[0]
        path = Path(item['file'])
        if digest(path) != item['sha256']:
            raise ValueError('Tangent field hash mismatch')
        with gzip.open(path, 'rb') as stream:
            direction = np.load(stream, allow_pickle=False)
        if direction.shape != total.shape:
            raise ValueError('The tangent field dimension differs')
        total += weight*direction
        hashes[str(path)] = item['sha256']
    # Reuse precisely the already documented warm-cubic geometry function.
    old_path = HERE/'strong_tangent_warm_bvp.py'
    old_text = old_path.read_text()
    tree = ast.parse(old_text)
    functions = [node for node in ast.walk(tree)
                 if isinstance(node, ast.FunctionDef) and node.name == 'geometry']
    if len(functions) != 1:
        raise ValueError('Warm geometry helper became ambiguous')
    node = functions[0]
    geometry_source = textwrap.dedent('\n'.join(old_text.splitlines()[node.lineno-1:node.end_lineno]))
    namespace = dict(np=np, CubicSpline=CubicSpline, SimpleNamespace=SimpleNamespace,
                     principal=prior_warm.principal)
    exec(compile(geometry_source, str(old_path), 'exec'), namespace)
    geometry = namespace['geometry']

    def form_guess(obj, t, y, p, record, saved):
        identity = raw_record['identity']
        if (obj.M != response['modes'] or obj.nt != response['angular']
                or obj.q != identity['gauge'] or obj.cfg != final['base_profile']
                or saved.rec['frozen_profile'] != response['baseline']['profile']
                or obj.port['parameters'] != identity['physical_tail_parameters']
                or obj.port['cut'] != identity['physical_tail_cut']):
            raise ValueError('Physical source, numerical base, dimensions or gauge differ')
        np.testing.assert_array_equal(obj.ref_coeff, identity['reference_coefficients'])
        np.testing.assert_array_equal(obj._neck_knots, identity['numerical_reference_knots'])
        if list(obj.ref_frequencies) != identity['reference_frequencies']:
            raise ValueError('Angular reference frequencies changed')
        proposed = base_p+total[n*m:]
        guess = base_y+total[:n*m].reshape((n, m), order='F')
        obj.select(proposed)
        f = obj.flow(proposed[0])
        for name, value in candidate['physical_profile'].items():
            actual = f.cfg[name]
            if isinstance(value, (int, float)) and not isinstance(value, bool):
                if abs(actual-value) > 3e-14*max(1., abs(value)):
                    raise ValueError('The predicted physical control differs: '+name)
            elif actual != value:
                raise ValueError('The predicted physical profile differs: '+name)
        s, unused = obj.chart(base_t, proposed[0])
        correction = obj.initial(proposed)-guess[:, 0]
        guess += correction[:, None]*np.maximum(0., 1-s/(f.Tu/2))[None, :]**3
        if np.max(abs(obj._core.coefficients-candidate['predicted_actual_core'])) > 3e-16:
            raise ValueError('Actual warm core differs from the complete tangent prediction')
        info = dict(scope=__doc__, warm_only=True, source_solution=str(restart),
            source_sha256=hashes.copy(), source_raw=str(raw_path), candidate=candidate,
            fixed_representation_gauge=gauge, prescribed_actual_support=target.tolist(),
            unchanged_reference_coefficients=obj.ref_coeff.tolist(),
            unchanged_numerical_reference_knots=obj._neck_knots.tolist(),
            finite_state_shape=list(guess.shape), predicted_profile=dict(f.cfg),
            exact_inlet_correction_max=float(np.max(abs(correction))),
            geometry_helper_sha256=hashlib.sha256(geometry_source.encode()).hexdigest(),
            solver_formulas_changed=False, physical_design_changed=True,
            tolerance_changed=False)
        record['full_multicore_tangent_warm'] = info
        obj.design_provenance['full_multicore_tangent_warm'] = info
        obj._strong_tangent_info = info
        return base_t.copy(), guess, proposed, record

    def inspect(fun, bc, x, y, p, **kwargs):
        obj = fun.__self__
        report = dict(scope=__doc__, inspection_only=True, nonlinear_solution=False,
            warm=obj._strong_tangent_info, modes=obj.M, angular=obj.nt, nodes=len(x),
            source_sha256=hashes.copy())
        try:
            h = np.diff(x)
            cr, ym, ff, fm = _bvp.collocation_fun(fun, y, p, x, h)
            br = bc(y[:, 0], y[:, -1], p)
            spline = _bvp.create_spline(y, ff, x, h)
            rms = _bvp.estimate_rms_residuals(fun, spline, x, h, p, 1.5*cr/h, fm)
            report['finite_domain_passed'] = True
            report['full_collocation'] = dict(scaled_max=float(np.max(abs(cr)/(h[None, :]*(1+abs(fm))))),
                boundary_max=float(np.max(abs(br))), rms_max=float(np.max(rms)),
                radial_sites_evaluated=len(x)+3*(len(x)-1))
            gc.collect()
            report['baseline_cubic_geometry'] = geometry(obj, base_t, base_y, base_p)
            gc.collect()
            report['warm_cubic_geometry'] = geometry(obj, x, y, p)
        except (FloatingPointError, ValueError) as error:
            report.update(finite_domain_passed=False, inspection_error=repr(error))
        opts.tangent_inspect_output.write_text(json.dumps(report, indent=2)+'\n')
        print(json.dumps(report), flush=True)
        raise RuntimeError('Multicore warm inspection complete; no nonlinear solve requested')

    def install(runner):
        load = runner.module

        def module(name, path):
            loaded = load(name, path)
            if Path(path).name != 'root_dual_core_bvp.py':
                return loaded
            original_main = loaded.main

            def run_entry():
                original_factory = loaded.make_dual

                def factory(*args, **kwargs):
                    Base = original_factory(*args, **kwargs)
                    from fixed_metric_mode3_core import PlanarSupportCore

                    class Multicore(Base):
                        def __init__(self, *a, **k):
                            super().__init__(*a, **k)
                            self.prescribed = target.copy()
                            self._core_key = None
                            self._initial = None
                            self.design_provenance.update(scope=__doc__,
                                prescribed_support=target.tolist(), representation_gauge=self.q,
                                actual_primary_is_independent_of_gauge=True,
                                adapter_sha256=hashes[str(Path(__file__))])
                            self.raw_recovery_context = dict(kind='triple-actual-core-fixed-gauge-v1',
                                prescribed_actual_support=target.tolist(), gauge=self.q,
                                reference_coefficients=self.ref_coeff.tolist(),
                                reference_frequencies=list(self.ref_frequencies),
                                control_names=list(self.control_names))

                        def initial(self, p):
                            self.select(p)
                            key = tuple(self.prescribed)+tuple(np.asarray(p[3:], float))
                            if key != self._core_key:
                                corrections = np.zeros(self.M-1)
                                corrections[:2] = self.prescribed[1:]
                                corrections[2:] = np.asarray(p[3:])*self.pscale[2:]
                                core = PlanarSupportCore(self.prescribed[0], corrections, 2)
                                f = self.flow(p[0])
                                N = max(2048, 128*self.M)
                                gi = f.general_core_chart.inlet_geometry(N)
                                exact = core.evaluate(gi['theta'])
                                B, B1, B2 = f.basis(N)
                                self._initial = f.project((exact['F']-gi['pos'])[None, :, :], B)[:, 0]/self.q
                                J = f.project(core.parameter_derivatives(gi['theta']), B)
                                self._initial_jac = np.zeros((self.n, self.M))
                                self._initial_jac[:, 3:] = J[:, 3:]*self.pscale[None, 2:]/self.q
                                first = gi['p1']+self.q*f.values(self._initial[:, None], B1)[0]
                                second = gi['p2']+self.q*f.values(self._initial[:, None], B2)[0]
                                mapped = gi['pos']+self.q*f.values(self._initial[:, None], B)[0]
                                true1 = exact['Ft']*gi['rho'][:, None]
                                true2 = exact['Ftt']*gi['rho'][:, None]**2+exact['Ft']*gi['rhop'][:, None]
                                error = np.sum(first*first, axis=1)/gi['rho']**2-1
                                self._inlet_metrics = dict(position=float(np.linalg.norm(mapped-exact['F'], axis=1).max()),
                                    first=float(np.linalg.norm(first-true1, axis=1).max()),
                                    second=float(np.linalg.norm(second-true2, axis=1).max()),
                                    metric_l1=float(np.sum(abs(np.fft.fft(error)/N))))
                                self._core, self._core_key = core, key
                                self.support_amplitude = float(self.prescribed[0])
                            return self._initial

                        def restart_from(self, saved, pullback, nodes, scale='linear'):
                            t, y, p = base_t.copy(), base_y.copy(), base_p.copy()
                            record = dict(scope='Exact accepted raw baseline plus a complete first-order design prediction; no angular or radial reinterpolation of baseline coefficients.',
                                amplitude_scaling='fixed-gauge-full-field-tangent', amplitude_ratio=1.)
                            return form_guess(self, t, y, p, record, saved)

                        def prepare_recovery_output(self, out):
                            super().prepare_recovery_output(out)
                            out['requested_actual_primary'] = float(self.prescribed[0])
                            out['secondary_law_applies_to_actual_core'] = False
                            out['fixed_gauge_continuation'] = True

                    return Multicore

                loaded.make_dual = factory
                original_main()

            loaded.main = run_entry
            if opts.tangent_inspect_output:
                loaded.solve_bvp = inspect
            return loaded

        runner.module = module

    adapter = HERE/'strong_triple_same_chart_bvp.py'
    source = adapter.read_text()
    anchor = 'runner.module=module;runner.main()'
    if source.count(anchor) != 1:
        raise ValueError('The production same-chart entry changed')
    source = source.replace(anchor, 'runner.module=module;_tangent_install(runner);runner.main()')
    module = types.ModuleType('strong_multicore_tangent_entry')
    module.__file__ = str(adapter)
    module.__dict__['_tangent_install'] = install
    exec(compile(source, str(adapter), 'exec'), module.__dict__)
    module.main()
    if opts.tangent_inspect_output and not opts.tangent_inspect_output.exists():
        raise RuntimeError('The requested full-field inspection did not reach its entry')


if __name__ == '__main__':
    main()
