#!/usr/bin/env python3
"""Refine a saved finite neck at fixed metric with tighter Newton residuals.

The first-order collocation stopping test is tightened independently of the
unchanged requested mesh residual tolerance. This tests whether endpoint
integration inconsistency creates the hidden second-derivative lobes of the
saved C2 quintic. It does not replace derivatives by pointwise PDE values.
All support coefficients are solved fields; no meridian design is varied.
The finite linear tail condition remains finite and is not exact closure.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import types
import time
from types import SimpleNamespace
import numpy as np
import root_radial_batching as radial

HERE = Path(__file__).resolve().parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def read(path):
    with gzip.open(path, 'rt') if path.suffix == '.gz' else path.open() as f:
        return json.load(f)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':')).encode()


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--fixed-reference', type=Path, required=True)
    parser.add_argument('--newton-residual-factor', type=float, default=1e-4)
    parser.add_argument('--frozen-port', type=Path)
    parser.add_argument('--linear-solver', choices=('sparse-lu', 'block-qr', 'direct-block-qr'), default='sparse-lu')
    parser.add_argument('--newton-progress', action='store_true')
    opts, remaining = parser.parse_known_args()
    if not 0 < opts.newton_residual_factor <= 1:
        raise ValueError('Newton residual factor must tighten the stopping test')
    ref = read(opts.fixed_reference)
    if not ref.get('solver_success'):
        raise ValueError('A successful fixed reference is required')
    if ref['config'].get('actual_nonlinear_tail'):
        raise ValueError('This adapter must not replace an actual nonlinear tail by a linear one')
    if ref.get('angular_chart') != 'general-support-core-blend-v1':
        raise ValueError('The reference must use the recorded general core chart')

    def argument(name):
        return Path(remaining[remaining.index(name) + 1])

    out = argument('--out-prefix')
    out.parent.mkdir(parents=True, exist_ok=True)
    utility = load('root_c2_fixed_utility', HERE / 'geometric-fixed-dual-prefix.py')
    _, port_check = utility.verify_port(ref, argument('--port'), opts.frozen_port)
    profile = ref['frozen_profile']
    gauge = float(ref['gauge_amplitude'])
    if '--profile' in remaining:
        if canonical(json.loads(argument('--profile').read_text())) != canonical(profile):
            raise ValueError('Physical profile changed')
    else:
        profile_file = out.with_name(out.name + '-frozen-profile.json')
        profile_file.write_text(json.dumps(profile, indent=2) + '\n')
        remaining += ['--profile', str(profile_file)]
    if '--q' in remaining:
        if float(remaining[remaining.index('--q') + 1]) != gauge:
            raise ValueError('Gauge changed')
    else:
        remaining += ['--q', repr(gauge)]
    if '--restart' not in remaining:
        remaining += ['--restart', str(opts.fixed_reference)]
    if '--warm-scale' in remaining:
        raise ValueError('No warm amplitude deformation is permitted in fixed-g refinement')
    if '--newton-backend' not in remaining:
        remaining += ['--newton-backend', 'refresh']
    elif remaining[remaining.index('--newton-backend') + 1] != 'refresh':
        raise ValueError('Use the owned refresh backend for the stated stopping test')
    provenance = dict(
        fixed_reference=str(opts.fixed_reference),
        fixed_reference_sha256=hashlib.sha256(opts.fixed_reference.read_bytes()).hexdigest(),
        fixed_data_sha256={key: hashlib.sha256(canonical(ref[key])).hexdigest()
                          for key in ('frozen_profile', 'physical_tail_parameters',
                                      'physical_tail_cut', 'chart_reference_coefficients',
                                      'chart_reference_frequencies', 'gauge_amplitude',
                                      'meridian_length')},
        newton_residual_factor=opts.newton_residual_factor,
        linear_solver=opts.linear_solver,
        newton_progress_and_gc=opts.newton_progress,
        port_verification=port_check,
        wrapper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        scope=__doc__)
    if opts.linear_solver != 'sparse-lu':
        provenance['block_qr_sha256'] = hashlib.sha256((HERE / 'strong_block_qr.py').read_bytes()).hexdigest()
    if opts.linear_solver == 'direct-block-qr':
        provenance['direct_block_sha256'] = hashlib.sha256((HERE / 'root_block_collocation.py').read_bytes()).hexdigest()
        import root_block_collocation
        root_block_collocation.install()
    root = load('root_c2_dual', HERE / 'root_dual_core_bvp.py')
    factory = root.make_dual
    original_loader = root.module

    def fixed_factory(adaptive, charts, chart, *unused, **kwargs):
        Base = utility.make_fixed(SimpleNamespace(make_dual=factory), adaptive, charts,
                                  chart, ref['chart_reference_coefficients'],
                                  ref['chart_reference_frequencies'])

        class Fixed(Base):
            def __init__(self, cfg, port, q, M, angular):
                self.ref_frequencies = list(ref['chart_reference_frequencies'])
                if canonical(cfg) != canonical(profile) or q != gauge:
                    raise ValueError('Fixed physical data changed')
                super().__init__(cfg, port, q, M, angular)
                for key, value in [('physical_tail_parameters', self.port['parameters']),
                                   ('physical_tail_cut', self.port['cut'])]:
                    if canonical(value) != canonical(ref[key]):
                        raise ValueError('Fixed tail datum changed: ' + key)
                if abs(self.flow().end - ref['meridian_length']) > 2e-13:
                    raise ValueError('Physical meridian length changed')
                self.fixed_metric_provenance = provenance

            def restart_from(self, saved, pullback, nodes, warm_scale):
                return self.restart_fixed(saved, pullback, nodes)

            def fun(self, t, y, p):
                f = self.flow()
                s, ds = self.chart(t, 0.)
                return ds[None, :] * radial.value(f, s, y, p, batch_size=24)

            def fun_jac(self, t, y, p):
                f = self.flow()
                s, ds = self.chart(t, 0.)
                J = radial.state_jacobian(f, s, y, p, batch_size=24)
                J *= ds[None, None, :]
                return J, np.zeros((self.n, self.M, len(t)))

        return Fixed

    def module(name, path):
        if Path(path).name != 'root_domain_newton.py':
            return original_loader(name, path)
        source = Path(path).read_text()
        old = 'threshold = h*(bvp_tol/30.)'
        if source.count(old) != 1:
            raise ValueError('Newton stopping test changed; refusing textual transform')
        new = old + '*' + repr(opts.newton_residual_factor)
        transformed = source.replace(old, new)
        if opts.linear_solver != 'sparse-lu':
            factor_old = 'factor = splu(jac(y, p, ym, ff, fm, br))'
            factor_new = 'factor = None\n                factor = _root_block_factor(jac(y, p, ym, ff, fm, br), n, m, len(p))'
            if transformed.count(factor_old) != 1:
                raise ValueError('Newton factor site changed; refusing transform')
            transformed = transformed.replace(factor_old, factor_new)
            provenance['factor_transform'] = dict(old=factor_old, new=factor_new)
        if opts.newton_progress:
            progress_old = '        residual, cr, ym, ff, fm, br = data\n'
            progress_new = progress_old + (
                '        collected = _root_gc.collect()\n'
                '        print(_root_json.dumps(dict(event="newton_iteration", iteration=iteration, nodes=m, '
                'scaled_collocation=float(np.max(abs(cr)/(h[None,:]*(1+abs(fm))))), '
                'boundary=float(np.max(abs(br))), collected=collected, '
                'peak_rss_kib=_root_resource.getrusage(_root_resource.RUSAGE_SELF).ru_maxrss)), flush=True)\n')
            if transformed.count(progress_old) != 1:
                raise ValueError('Newton iteration site changed; refusing progress transform')
            transformed = transformed.replace(progress_old, progress_new)
            provenance['progress_transform'] = dict(old=progress_old, new=progress_new)
        m = types.ModuleType(name)
        m.__file__ = str(path)
        sys.modules[name] = m
        exec(compile(transformed, str(path), 'exec'), m.__dict__)
        if opts.newton_progress:
            import gc
            import resource
            m._root_gc, m._root_resource, m._root_json = gc, resource, json
        if opts.linear_solver != 'sparse-lu':
            if opts.linear_solver == 'direct-block-qr':
                from root_block_collocation import DirectBlockQRFactor as BlockQRFactor
            else:
                from strong_block_qr import BlockQRFactor
            import resource
            def factor(matrix, n, nodes, k):
                start = time.time()
                result = BlockQRFactor(matrix, n, nodes, k)
                elapsed = time.time() - start
                m.STATS['block_qr_factorizations'] = m.STATS.get('block_qr_factorizations', 0) + 1
                m.STATS['block_qr_seconds'] = m.STATS.get('block_qr_seconds', 0.) + elapsed
                print(json.dumps(dict(event='block_qr_factor', n=n, nodes=nodes, seconds=elapsed,
                                      peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)), flush=True)
                return result
            m._root_block_factor = factor
            m.STATS['linear_factor_kind'] = opts.linear_solver
        m.STATS['collocation_threshold_factor'] = opts.newton_residual_factor
        provenance['newton_transform'] = dict(
            original_sha256=hashlib.sha256(source.encode()).hexdigest(), old=old, new=new,
            transformed_sha256=hashlib.sha256(transformed.encode()).hexdigest())
        return m

    root.make_dual = fixed_factory
    root.module = module
    sys.argv = [sys.argv[0]] + remaining
    root.main()


if __name__ == '__main__':
    main()
