#!/usr/bin/env python3
"""Freeze an accepted actual design without changing its fields or metric.

The complete numerical x/y/cubic and physical quintic pieces are reused by
their original hashes. Only the three design offsets are removed from p;
their already accepted final physical profile is used by the real Fixed
factory. The original collocation RMS and all fixed boundary conditions are
evaluated again before writing a fixed view. No Newton step, tail worker,
resampling, or new physical solution is produced. This is a finite-problem
representation change, not an infinite closure or a refinement result.
"""
from __future__ import annotations
import argparse
import copy
import gzip
import hashlib
import io
import json
import os
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
PHYSICAL_KEYS = ('frozen_profile', 'physical_tail_parameters', 'physical_tail_cut',
                 'angular_chart', 'chart_reference_coefficients',
                 'chart_reference_frequencies', 'gauge_amplitude', 'meridian_length')


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def document(path):
    path = Path(path)
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def write_json(path, value):
    data = (json.dumps(value, indent=2, allow_nan=False) + '\n').encode()
    if path.suffix == '.gz':
        data = gzip.compress(data, mtime=0)
    if path.exists() or len(data) >= 5_000_000:
        raise ValueError('Output exists or exceeds the file limit: ' + str(path))
    temporary = path.with_name(path.name + '.tmp')
    temporary.write_bytes(data)
    temporary.replace(path)
    return dict(file=str(path), sha256=digest(path), bytes=len(data))


class Completed(BaseException):
    """Exit the original driver before its solve/write/postprocess pipeline."""


def main():
    parser = argparse.ArgumentParser(add_help=False, description=__doc__)
    parser.add_argument('--design-checkpoint', type=Path, required=True)
    parser.add_argument('--design-raw', type=Path, required=True)
    parser.add_argument('--design-tail', type=Path, required=True)
    parser.add_argument('--fixed-view-prefix', type=Path, required=True)
    parser.add_argument('--allow-fixed-input-for-identity-check', action='store_true')
    parser.add_argument('--radial-batch-size', type=int, default=16)
    options, remaining = parser.parse_known_args()
    prefix = options.fixed_view_prefix
    if (prefix.parent.resolve() != options.design_raw.parent.resolve() or
            prefix.parent.resolve() != options.design_checkpoint.parent.resolve()):
        raise ValueError('Use the original data directory so all existing chunks retain their identity')
    reserved = [prefix.with_suffix('.json.gz')] + [Path(str(prefix) + ending) for ending in
        ('-raw-collocation.json.gz', '-report.json', '-raw-p-000.npy.gz',
         '-raw-rms-000.npy.gz', '-loader-frozen-profile.json')]
    if any(path.exists() for path in reserved):
        raise ValueError('Use a fresh fixed-view prefix')
    if any(key in remaining for key in ('--postprocess-only', '--check-only', '--warm-scale')):
        raise ValueError('This conversion must reach the real residual inspection')
    saved, record, tail = (document(path) for path in
                          (options.design_checkpoint, options.design_raw, options.design_tail))
    hashes = {str(path): digest(path) for path in
              (Path(__file__), options.design_checkpoint, options.design_raw, options.design_tail)}
    if (not saved.get('solver_success') or saved.get('audit_pending', True) or
            not saved['config'].get('actual_nonlinear_tail') or not record.get('solver_success') or
            record.get('raw_collocation_only') is not True or record.get('physical_surface') is not False):
        raise ValueError('A formally accepted, audited actual design and its original raw state are required')
    if saved['raw_collocation_checkpoint']['sha256'] != hashes[str(options.design_raw)]:
        raise ValueError('The accepted physical state links a different raw checkpoint')
    ident = record['identity']
    context = ident.get('coupling_context', {})
    if not context.get('actual_nonlinear_tail'):
        raise ValueError('Missing complete actual coupling identity')
    for a, b in (('gauge', 'gauge_amplitude'), ('profile', 'frozen_profile'),
                 ('physical_tail_parameters', 'physical_tail_parameters'),
                 ('physical_tail_cut', 'physical_tail_cut'),
                 ('reference_coefficients', 'chart_reference_coefficients'),
                 ('reference_frequencies', 'chart_reference_frequencies')):
        if canonical(ident[a]) != canonical(saved[b]):
            raise ValueError('Accepted physical/raw identity differs: ' + a)
    if ident['numerical_reference_knots'] != saved['numerical_meridian_chart']['reference_t']:
        raise ValueError('The original numerical chart differs')
    design = saved.get('actual_augmented_continuation')
    fixed_input = bool(saved['config'].get('fixed_metric'))
    if fixed_input:
        if not options.allow_fixed_input_for_identity_check or not ident['fixed']:
            raise ValueError('Already fixed inputs require the explicit identity-check option')
    elif (not design or design.get('final_physical_profile') != saved['frozen_profile'] or ident['fixed']):
        raise ValueError('An accepted augmented design with its final physical profile is required')
    if saved['angular_chart'] != 'general-support-core-blend-v1':
        raise ValueError('Unsupported material chart')
    if (saved['frozen_profile'].get('ramp_law') != 'hermite_boost_neck' or
            saved['physical_tail_cut'].get('_prefix_bridge', {}).get('kind') != 'finite_neck_terminal_v1'):
        raise ValueError('The stored neck and negative-sigma terminal bridge are required')
    for name in ('root_actual_bounded_neck.py', 'root_actual_neck_bvp.py',
                 'root_actual_fixed_refinement.py', 'geometric-fixed-dual-prefix.py',
                 'root_dual_core_bvp.py', 'root_neck_chart.py', 'root_raw_collocation.py',
                 'root_radial_batching.py', 'strong_actual_augmented_core.py'):
        hashes[str(HERE / name)] = digest(HERE / name)
    for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
        os.environ[key] = '1'
    import gc
    import numpy as np
    from scipy.integrate import _bvp
    from scipy.interpolate import PPoly
    from types import SimpleNamespace
    import root_actual_bounded_neck as bounded
    import root_raw_collocation as raw
    import root_radial_batching as radial
    from strong_actual_augmented_core import LAYOUT

    arrays = {}
    for name, item in record['arrays'].items():
        if item['dtype'] != 'float64':
            raise ValueError('Expected original binary64 raw arrays')
        flat = np.empty(int(np.prod(item['shape'])), dtype=np.float64)
        end = 0
        for chunk in item['chunks']:
            if chunk['first'] != end or Path(chunk['file']).name != chunk['file']:
                raise ValueError('Invalid raw chunk layout')
            file = options.design_raw.parent / chunk['file']
            if digest(file) != chunk['sha256']:
                raise ValueError('Raw chunk SHA mismatch')
            hashes[str(file)] = chunk['sha256']
            block = np.load(io.BytesIO(gzip.decompress(file.read_bytes())), allow_pickle=False)
            if block.dtype != np.float64 or block.shape != (chunk['count'],):
                raise ValueError('Raw chunk shape or dtype changed')
            flat[end:end+len(block)] = block
            end += len(block)
        if end != flat.size or not np.isfinite(flat).all():
            raise ValueError('Incomplete or nonfinite raw state')
        arrays[name] = flat.reshape(item['shape'])
    M, nodes = int(saved['modes']), len(arrays['x'])
    n = 3*M+1
    if (arrays['y'].shape != (n, nodes) or arrays['cubic'].shape != (4, nodes-1, n) or
            arrays['rms'].shape != (nodes-1,) or
            arrays['p'].shape != (M if fixed_input else M+3,) or
            not np.array_equal(arrays['p'], record['parameter_state']) or
            not np.array_equal(arrays['p'], saved['parameters']) or
            not np.all(np.diff(arrays['x']) > 0)):
        raise ValueError('Unexpected complete raw dimensions or parameter copies')
    if not fixed_input and ident['parameter_layout'] != LAYOUT:
        raise ValueError('Unrecognized augmented design parameter layout')
    fixed_p = arrays['p'][:M].copy()
    height = -float(saved['gauge_amplitude'])*arrays['y'][2*M+1:, -1]
    request, response = tail['request'], tail['response']
    if np.asarray(request['height'], dtype=np.float64).tobytes() != height.tobytes():
        raise ValueError('The stored final tail is not at the exact complete raw H')
    if (not request.get('jacobian') or not request.get('audit') or not response.get('converged') or
            not response.get('audit') or response['residual'] > tail['config']['solveTolerance'] or
            len(response['heightJetJacobian']) != (3*M+2)*M or
            tail.get('source_sha256') != saved['actual_tail']['source_sha256']):
        raise ValueError('A complete accepted final tail Jacobian and audit are required')
    for key, value in saved['physical_tail_parameters'].items():
        if tail['config'].get(key) != value:
            raise ValueError('Tail physical parameter differs: ' + key)
    for key in ('modes', 'spacing', 'depth', 'steps', 'shootingParts', 'linearFar', 'linearSteps',
                'quadrature', 'solveTolerance', 'projectionFloor', 'auditSteps', 'cuspAwareFlow', 'actualCuspGrid'):
        if tail['config'].get(key) != saved['actual_tail']['config'].get(key):
            raise ValueError('Tail finite configuration differs: ' + key)
    end = 0
    for chunk in saved['pp_coefficient_chunks']:
        if Path(chunk['file']).name != chunk['file'] or chunk['state_first'] != end:
            raise ValueError('Incomplete physical quintic chunk coverage')
        file = options.design_checkpoint.parent / chunk['file']
        if file.stat().st_size != chunk['bytes'] or digest(file) != chunk['sha256']:
            raise ValueError('The physical quintic chunk changed')
        hashes[str(file)] = chunk['sha256']
        end = chunk['state_last_exclusive']
    if end != n:
        raise ValueError('Physical quintic does not cover all states and mean')

    def fixed_argument(name, value):
        value = str(value)
        if name in remaining:
            if remaining[remaining.index(name)+1] != value:
                raise ValueError('Argument changes the accepted problem: ' + name)
        else:
            remaining.extend([name, value])

    loader_prefix = Path(str(prefix) + '-loader')
    for name, value in (('--fixed-reference', options.design_checkpoint),
                        ('--raw-collocation-restart', options.design_raw),
                        ('--q', repr(ident['gauge'])), ('--modes', M), ('--angular', ident['angular']),
                        ('--tol', repr(ident['tol'])), ('--client', context['client']),
                        ('--coupling', context['coupling']),
                        ('--actual-tail-tol', repr(context['actual_tail_tolerance'])),
                        ('--meridian-chart', 'all-knots'), ('--second-control', 'boost_length'),
                        ('--nodes', 0), ('--out-prefix', loader_prefix)):
        fixed_argument(name, value)
    if '--tail-config' not in remaining or '--source-topic' not in remaining or '--port' not in remaining:
        raise ValueError('Supply the original tail-config, source-topic and physical port')
    config = Path(remaining[remaining.index('--tail-config')+1])
    if digest(config) != context['tail_config_sha256']:
        raise ValueError('The original actual tail-config bytes differ')
    hashes[str(config)] = digest(config)
    defaults = radial.value.__defaults__, radial.state_jacobian.__defaults__
    if defaults != ((48,), (48,)) or not 1 <= options.radial_batch_size <= 48:
        raise ValueError('Unexpected original radial batching interface')
    radial.value.__defaults__ = radial.state_jacobian.__defaults__ = (options.radial_batch_size,)
    original_loader, original_read = bounded.adapter.module, raw.read
    counters = dict(raw_restorations=0, residual_checks=0, tail_start_attempts=0)
    started = time.monotonic()

    def mapped_read(path, obj, args):
        if Path(path).resolve() != options.design_raw.resolve():
            return original_read(path, obj, args)
        counters['raw_restorations'] += 1
        if not obj.fixed or obj.tail is not None or obj.M != M or obj.nt != ident['angular']:
            raise ValueError('Expected the real Fixed/Actual factory before any tail worker')
        obj._neck_knots = np.asarray(ident['numerical_reference_knots'], dtype=float).copy()
        obj.chart_breaks = obj._neck_knots.copy()
        obj._flow = obj._flow_key = obj._core_key = obj._initial = None
        obj.select(fixed_p)
        actual_identity = raw.identity(obj, args)
        for key in ('modes', 'angular', 'gauge', 'profile', 'physical_tail_parameters',
                    'physical_tail_cut', 'reference_coefficients', 'reference_frequencies',
                    'tol', 'bc_tol', 'numerical_reference_knots'):
            if canonical(actual_identity[key]) != canonical(ident[key]):
                raise ValueError('Real fixed factory changed accepted identity: ' + key)
        new_context = actual_identity['coupling_context']
        for key in ('actual_nonlinear_tail', 'tail_config_sha256', 'client', 'coupling', 'actual_tail_tolerance'):
            if new_context[key] != context[key]:
                raise ValueError('Actual fixed context changed: ' + key)
        sol = SimpleNamespace(x=arrays['x'], y=arrays['y'], p=fixed_p,
                              sol=PPoly.construct_fast(arrays['cubic'], arrays['x'], extrapolate=True, axis=1),
                              rms_residuals=arrays['rms'], status=record['status'],
                              success=record['solver_success'], message=record['message'], niter=record['niter'])
        return sol, record

    def guard(self):
        counters['tail_start_attempts'] += 1
        raise RuntimeError('A tail worker is forbidden in this frozen representation change')

    def inspect(self, fun, bc, x, y, p, **kwargs):
        counters['residual_checks'] += 1
        if not self.fixed or self.tail is not None:
            raise ValueError('The real fixed actual loader was not selected')
        for name, current, accepted in (('x', x, arrays['x']), ('y', y, arrays['y']), ('p', p, fixed_p)):
            if current.tobytes() != accepted.tobytes():
                raise ValueError('The complete original field changed: ' + name)
        if self.tail_height(y[:, -1]).tobytes() != height.tobytes():
            raise ValueError('The live fixed bridge changed complete H')
        slope = np.asarray(response['jets']['slope'])
        JH = np.asarray(response['heightJetJacobian']).reshape(3*M+2, M)[:M].copy()

        def actual_boundary(value):
            if self.tail_height(value).tobytes() != height.tobytes():
                raise ValueError('Stored exact tail may only be evaluated at its complete original H')
            return slope, JH

        self.tail_boundary = actual_boundary
        self.select(p)
        self.initial(p)
        flow = self.flow()
        if not np.array_equal(self._core.coefficients, saved['core']['coefficients']):
            raise ValueError('Full core parameters do not reproduce the accepted support')
        if (flow.cfg != saved['frozen_profile'] or abs(flow.end-saved['meridian_length']) > 2e-13 or
                not np.allclose(flow.breaks, saved['numerical_meridian_chart']['physical_s'], rtol=0, atol=2e-13)):
            raise ValueError('Final physical profile, meridian length or physical knots changed')
        h = np.diff(x)
        cr, ym, ff, fm = _bvp.collocation_fun(fun, y, p, x, h)
        original_cubic = PPoly.construct_fast(arrays['cubic'], x, extrapolate=True, axis=1)
        rms = _bvp.estimate_rms_residuals(fun, original_cubic, x, h, p, 1.5*cr/h, fm)
        br = bc(y[:, 0], y[:, -1], p)
        if br.shape != (n+M,):
            raise ValueError('Expected all original fixed inlet and terminal boundary equations')
        physical_bc = float(np.max(abs(br[n:]*self.bcweights)))
        rms_difference = float(np.max(abs(rms-arrays['rms'])))
        if (not np.isfinite(rms).all() or float(np.max(rms)) > ident['tol'] or
                float(np.max(abs(br))) > ident['bc_tol'] or
                physical_bc > context['actual_tail_tolerance'] or rms_difference > 2e-11):
            raise ValueError('Frozen raw state failed an unchanged original RMS or boundary gate')
        report = dict(scope=__doc__, nonlinear_solve_run=False, tail_worker_started=False,
                      identity_check_only=fixed_input, complete_H_bitwise_equal=True,
                      raw_x_y_cubic_unchanged=True, physical_quintics_unchanged=True,
                      all_core_coefficients_unchanged=True, gauge_unchanged=True,
                      original_numerical_reference_unchanged=True, eight_physical_data_unchanged=True,
                      original_parameter_count=len(arrays['p']), fixed_parameter_count=M,
                      rms_max=float(np.max(rms)), original_rms_max=float(np.max(arrays['rms'])),
                      rms_array_max_difference=rms_difference, rms_array_bitwise_equal=rms.tobytes()==arrays['rms'].tobytes(),
                      all_boundary_max=float(np.max(abs(br))), true_physical_boundary_max=physical_bc,
                      nodes=nodes, modes=M, angular=self.nt, source_sha256=hashes.copy(),
                      fixed_factory_provenance=copy.deepcopy(self.fixed_metric_provenance),
                      counters=counters.copy(), seconds=time.monotonic()-started)
        mapped = copy.deepcopy(record)
        mapped['identity'] = raw.identity(self, SimpleNamespace(tol=ident['tol']))
        mapped['parameter_state'] = p.tolist()
        mapped['provenance']['frozen_design_view'] = copy.deepcopy(report)
        mapped['original_writer_sha256'] = mapped['writer_sha256']
        mapped['writer_sha256'] = digest(__file__)
        mapped['scope'] = __doc__ + '\nOriginal raw chunks are shared without changing their bytes.'
        for name, array in (('p', p), ('rms', rms)):
            if array.shape == arrays[name].shape and array.tobytes() == arrays[name].tobytes():
                continue
            stream = io.BytesIO()
            np.save(stream, np.asarray(array, dtype=np.float64).ravel(), allow_pickle=False)
            file = Path(str(prefix) + '-raw-' + name + '-000.npy.gz')
            data = gzip.compress(stream.getvalue(), mtime=0)
            if file.exists() or len(data) >= 5_000_000:
                raise ValueError('Existing or oversized mapped raw piece')
            file.write_bytes(data)
            mapped['arrays'][name] = dict(shape=list(array.shape), dtype='float64', chunks=[
                dict(file=file.name, first=0, count=int(array.size), sha256=digest(file))])
        raw_path = Path(str(prefix) + '-raw-collocation.json.gz')
        raw_link = write_json(raw_path, mapped)
        raw_link.update(nodes=nodes, solver_success=True, physical_surface=False)
        output = copy.deepcopy(saved)
        output['config']['fixed_metric'] = True
        output['base_profile'] = copy.deepcopy(saved['frozen_profile'])
        output['parameters'] = p.tolist()
        output['parameter_layout'] = mapped['identity']['parameter_layout']
        output['raw_collocation_checkpoint'] = raw_link
        output['fixed_metric_provenance'] = copy.deepcopy(self.fixed_metric_provenance)
        output['frozen_design_view'] = copy.deepcopy(report)
        output['scope'] = __doc__
        for key in ('actual_augmented_continuation', 'prescribed_actual_core'):
            if key in output:
                output.setdefault('original_design_provenance', {})[key] = output.pop(key)
        for key in PHYSICAL_KEYS:
            if canonical(output[key]) != canonical(saved[key]):
                raise ValueError('Frozen view changed a physical field: ' + key)
        main_link = write_json(prefix.with_suffix('.json.gz'), output)
        report.update(output=main_link, raw_output=raw_link)
        write_json(Path(str(prefix) + '-report.json'), report)
        print(json.dumps(dict(event='actual_fixed_design_view_verified', output=main_link,
                              rms=report['rms_max'], true_bc=physical_bc, counters=counters)), flush=True)
        del cr, ym, ff, fm
        gc.collect()
        raise Completed()

    def load(name, path):
        loaded = original_loader(name, path)
        if Path(path).name == 'root_dual_core_bvp.py':
            original_main = loaded.main

            def entry():
                factory = loaded.make_dual

                def instrument(*args, **kwargs):
                    cls = factory(*args, **kwargs)
                    cls.ensure_tail, cls.solve_coupled = guard, inspect
                    return cls

                loaded.make_dual = instrument
                return original_main()

            loaded.main = entry
        return loaded

    bounded.adapter.module, raw.read = load, mapped_read
    previous_argv = sys.argv
    sys.argv = [sys.argv[0]] + remaining
    completed = False
    try:
        try:
            bounded.main()
        except Completed:
            completed = True
    finally:
        bounded.adapter.module, raw.read = original_loader, original_read
        radial.value.__defaults__, radial.state_jacobian.__defaults__ = defaults
        sys.argv = previous_argv
    if not completed or counters != dict(raw_restorations=1, residual_checks=1, tail_start_attempts=0):
        raise RuntimeError('The complete fixed-state verification did not finish without a worker')


if __name__ == '__main__':
    main()
