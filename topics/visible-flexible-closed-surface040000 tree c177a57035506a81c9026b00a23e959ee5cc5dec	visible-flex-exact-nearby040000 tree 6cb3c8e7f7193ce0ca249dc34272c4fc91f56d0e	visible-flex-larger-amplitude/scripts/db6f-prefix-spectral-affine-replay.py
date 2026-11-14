#!/usr/bin/env python3
"""Spectral-coordinate affine M14 diagnostic; never an actual coupled solve.

The mathematical baseline is frozen db6f-prefix-affine-replay.py. Only its
solve_bvp callable is replaced by the reviewed positive-diagonal conjugacy.
No tail client is instantiated. The old actual DN/J is frozen provenance.
"""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import argparse
import ast
import gzip
import hashlib
import importlib.util
import inspect
import json
import math
import sys
import time
from pathlib import Path
from types import SimpleNamespace

import numpy as np

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
REPO = TOPIC.parents[1]
SCOPE = 'Frozen-affine-DN spectral collocation diagnostic only; not a new actual coupled prefix or a closed surface.'
FLAGS = {'actual_nonlinear_tail': False, 'frozen_affine_dn': True}
PHYSICAL_FIELDS = ('angular_chart', 'chart', 'frozen_profile', 'physical_tail_parameters',
                   'physical_tail_cut', 'warp_reference_q')
SETTINGS = {'modes': 14, 'angular': 512, 'tol': 2e-9, 'bc_tol': 1e-8,
            'physical_bc_tol': 2e-11, 'max_nodes': 6500}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def identity(path):
    p = Path(path).resolve()
    sha = hashlib.sha256()
    with p.open('rb') as f:
        for part in iter(lambda: f.read(1048576), b''):
            sha.update(part)
    return {'path': str(p), 'bytes': p.stat().st_size, 'sha256': sha.hexdigest()}


def verify(row):
    require(identity(row['path']) == row, 'Changed bound input: ' + row['path'])


def read(path):
    p = Path(path)
    data = p.read_bytes()
    return json.loads(gzip.decompress(data) if p.suffix == '.gz' else data)


def write_json(path, value, *, exclusive=False):
    data = (json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + '\n').encode()
    require(len(data) < 1000000, 'Diagnostic metadata exceeds 1 MB')
    with Path(path).open('xb' if exclusive else 'wb') as f:
        f.write(data)


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def number(value):
    return type(value) in (int, float) and math.isfinite(value)


def vector(value, n):
    return isinstance(value, list) and len(value) == n and all(number(v) for v in value)


def source_function(path, qualname):
    """Pure AST source identity; no import or candidate initialization."""
    p = Path(path).resolve()
    text = p.read_text()
    matches = []
    def walk(body, prefix=''):
        for node in body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                name = prefix + node.name
                if name == qualname:
                    matches.append(node)
                inner = name + ('.' if isinstance(node, ast.ClassDef) else '.<locals>.')
                walk(node.body, inner)
    walk(ast.parse(text).body)
    require(len(matches) == 1, 'Ambiguous source callback: ' + qualname)
    node = matches[0]
    require(isinstance(node, ast.FunctionDef) and not node.decorator_list, 'Unexpected callback definition')
    source = '\n'.join(text.splitlines()[node.lineno - 1:node.end_lineno]).rstrip()
    return {'file': identity(p), 'qualname': qualname, 'first_line': node.lineno,
            'source_sha256_rstrip': hashlib.sha256(source.encode()).hexdigest()}


def check_callback(function, expected):
    fn = getattr(function, '__func__', function)
    verify(expected['file'])
    require(Path(inspect.getfile(fn)).resolve() == Path(expected['file']['path'])
            and fn.__qualname__ == expected['qualname']
            and fn.__code__.co_firstlineno == expected['first_line'], 'Unexpected running callback identity')
    digest = hashlib.sha256(inspect.getsource(fn).rstrip().encode()).hexdigest()
    require(digest == expected['source_sha256_rstrip'], 'Running callback source differs')
    return {**expected, 'runtime_module': fn.__module__, 'signature': str(inspect.signature(fn))}


def validate_inputs(launch):
    """Metadata/hash checks only; safe for the pure preparer."""
    require(launch['schema'] == 'db6f-spectral-affine-m14q512-v1', 'Wrong spectral diagnostic launch')
    require(canonical(launch['settings']) == canonical(SETTINGS)
            and canonical(launch['scope_flags']) == canonical(FLAGS), 'Changed original settings or scope')
    for row in launch['bindings']:
        verify(row)
    for key in ('checkpoint', 'frozen_tail', 'linear_port', 'profile', 'chart', 'tail_config'):
        verify(launch[key])
    rec, packet, port = [read(launch[key]['path']) for key in ('checkpoint', 'frozen_tail', 'linear_port')]
    cfg = rec['config']
    require(rec['solver_success'] is True and cfg['actual_nonlinear_tail'] is True
            and cfg['fixed_metric'] is True, 'Source is not the true fixed-metric M14 solution')
    for key in ('modes', 'angular', 'tol', 'bc_tol', 'physical_bc_tol'):
        require(canonical(cfg[key]) == canonical(SETTINGS[key]), 'Wrong original prefix parameter: ' + key)
    require(canonical({key: rec[key] for key in PHYSICAL_FIELDS}) == canonical(launch['frozen_physical_fields']),
            'One of the six original restart fields changed')
    require(canonical(rec['gauge_amplitude']) == canonical(launch['gauge_amplitude'])
            and rec['physical_port_sha256'] == launch['linear_port']['sha256'], 'Gauge or physical port changed')
    require(canonical(rec['frozen_profile']) == canonical(read(launch['profile']['path']))
            and canonical(rec['chart']) == canonical(read(launch['chart']['path']))
            and canonical(rec['tail_config']) == canonical(read(launch['tail_config']['path']))
            and canonical(rec['tail_config']) == canonical(packet['config']), 'Original profile/chart/config identity differs')
    require(canonical(rec['physical_tail_parameters']) == canonical(port['parameters'])
            and canonical(rec['physical_tail_cut']) == canonical(port['cut']), 'Original linear-port physical definition differs')
    tailpath = Path(launch['checkpoint']['path']).parent / rec['tail_seam']['tail_record']
    require(tailpath.resolve() == Path(launch['frozen_tail']['path']), 'DN/J is not this prefix own final seam packet')
    response, request = packet['response'], packet['request']
    require(response['converged'] is True and number(response['residual'])
            and 0 <= response['residual'] < 2e-9
            and request['jacobian'] is True and request['audit'] is True,
            'Original final DN/J/audit is not genuinely successful')
    M = SETTINGS['modes']
    require(vector(request['height'], M)
            and vector(response['heightJetJacobian'], (3*M+2)*M), 'Wrong original physical H/J shape')
    jets = response['jets']
    scalars = {'radius','backgroundSlope','backgroundSecond','E','Ep','meanSlope','meanSecond',
               'meanSlopeCorrection','meanSecondCorrection','minLeading','minD','endpointFullD','endpointPhi','formalCurvature'}
    require(set(jets) == scalars | {'height','slope','second'}
            and all(number(jets[k]) for k in scalars)
            and all(vector(jets[k], M) for k in ('height','slope','second')), 'Wrong original 17-jet schema')
    audit_keys = {'fullD','normalizedFullDefect','minLeading','minD','formalCurvature','maxPhysicalPV','actualMetric','holonomy'}
    require(set(response['audit']) == audit_keys and all(number(v) for v in response['audit'].values()),
            'Wrong original eight-audit schema')
    require(canonical(packet['source_sha256']) == canonical(launch['frozen_tail_sources']), 'Original eight-source tail identity differs')
    require(canonical(response['checkpoint']['cutHeight']) == canonical(request['height']), 'Original true-tail physical label differs')
    require(rec['tail_seam']['tail_converged'] is True
            and rec['tail_seam']['tail_shooting_residual'] == response['residual'], 'Recorded own seam success differs')
    for chunk in rec['pp_coefficient_chunks']:
        row = identity(Path(launch['checkpoint']['path']).parent / chunk['file'])
        require(row['bytes'] == chunk['bytes'] and row['sha256'] == chunk['sha256'], 'Original coefficient chunk changed')
    return rec, packet, port


def boundary_diagnostics(obj, y, par):
    """The original scaled BC and its original physical terminal formula."""
    values = np.asarray(obj.bc(y[:, 0], y[:, -1], par))
    flow = obj.flow(par[0])
    dy = flow.fun(np.array([flow.end]), y[:, -1].astype(np.longdouble)[:, None], par)[:, 0]
    height = obj.bridge.sigma * obj.q * y[obj.iz:, -1]
    slope = np.asarray(obj.tail.solve(height, jacobian=False)['jets']['slope'])
    raw = np.asarray(obj.q * dy[obj.iz:] - slope / math.sqrt(obj.port['cut']['E']), float)
    require(np.all(np.isfinite(values)) and np.all(np.isfinite(raw)), 'Nonfinite original physical BC')
    return {'original_scaled_bc_linf': float(np.max(abs(values))),
            'original_inlet_bc_linf': float(np.max(abs(values[:obj.n]))),
            'original_physical_terminal_bc_linf': float(np.max(abs(raw))),
            'scope': 'Original formulas only; no new geometric threshold or true DN evaluation.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--launch', type=Path, required=True)
    args = parser.parse_args()
    launch = read(args.launch)
    rec_meta, actual, port = validate_inputs(launch)
    require(Path(launch['launch_path']).resolve() == args.launch.resolve(), 'Wrong launch path')
    require(launch['command'] == [sys.executable, str(Path(__file__).resolve()), '--launch', str(args.launch.resolve())],
            'Unexpected actual runner argv identity')
    out_prefix = Path(launch['out_prefix'])
    repro = Path(str(out_prefix) + '-reproduction.json')
    summary_path = Path(str(out_prefix) + '-summary.json')
    require(not repro.exists() and not summary_path.exists()
            and not out_prefix.with_suffix('.json.gz').exists()
            and not list(out_prefix.parent.glob(out_prefix.name + '_coeff_*.npy.gz')), 'Output stem already has diagnostic results')
    begin = time.monotonic()
    manifest = {'status': 'STARTING_FROZEN_AFFINE_DIAGNOSTIC', 'scope': SCOPE, **FLAGS,
                'launch': identity(args.launch), 'settings': SETTINGS,
                'checkpoint': launch['checkpoint'], 'frozen_actual_tail': launch['frozen_tail'],
                'source_bindings': launch['bindings'], 'actual_new_DN_calls': 0,
                'process_exit_scope': 'This file records program status only; actual tool exit requires a separate observer.'}
    write_json(repro, manifest, exclusive=True)
    summary = dict(manifest)
    solver_records = []
    requested_exit = 2
    try:
        runner = module('spectral_affine_original_runner', HERE / 'db6f-prefix-flat-coupled.py').m
        runner.adaptive.old.install_source(Path(launch['source_root']))
        from curve_stable_prefix_bvp import load_checkpoint, save_checkpoint
        import f6curve_domain_newton as domain_newton
        import scipy.integrate._bvp as scipy_bvp
        rec = load_checkpoint(launch['checkpoint']['path'])
        require(np.asarray(rec['pp_coefficients']).shape == (6, len(rec['mesh'])-1, 43)
                and np.all(np.isfinite(rec['pp_coefficients'])), 'Original physical coefficients invalid')
        port['_sha256'] = launch['linear_port']['sha256']
        _, Base = runner.adaptive.build_classes(rec['chart'])
        class BVP(runner.TailMixin, Base):
            pass
        cfg = rec['config']
        obj = BVP(rec['frozen_profile'], port, rec['gauge_amplitude'],
                  cfg['modes'], cfg['angular'], True, rec['warp_reference_q'])
        obj.bcweights = np.full(obj.M, cfg['physical_bc_tol']/cfg['bc_tol'])
        initializer = module('spectral_affine_original_initializer', HERE / 'db6f-prefix-preserve-restart.py')
        x, y, par, restart = initializer.restart(obj, Path(launch['checkpoint']['path']), rec['chart'])
        obj.tail = runner.AffineTailForInnerBVP(actual['request']['height'], actual['response'], obj.M)
        flow = obj.flow(par[0])
        callbacks = {'fun': obj.fun, 'fun_jac': obj.fun_jac, 'bc': obj.bc, 'bc_jac': obj.bc_jac,
                     'terminal': obj.terminal, 'initial': obj.initial, 'chart': obj.chart,
                     'physical_fun': flow.fun, 'physical_fun_jac': flow.fun_jac,
                     'physical_c2_interpolant': flow.c2_interpolant, 'affine_dn': obj.tail.solve,
                     'restart': initializer.restart, 'save_checkpoint': save_checkpoint,
                     'domain_install': domain_newton.install, 'domain_solve_newton': domain_newton.solve_newton}
        runtime_callbacks = {key: check_callback(fn, launch['callbacks'][key]) for key, fn in callbacks.items()}
        startheight = obj.bridge.sigma * obj.q * y[obj.iz:, -1]
        initial_bc = boundary_diagnostics(obj, y, par)
        spectral = module('reviewed_spectral_conjugacy', HERE / 'db6f-root-spectral-collocation-v2.py')
        weights = spectral.power2_weights(obj.M)
        require(canonical(weights.tolist()) == canonical(launch['weights']), 'Frozen spectral weights differ')
        solve_bvp, solver_records = spectral.make_solver(weights)
        domain_newton.install()
        require(scipy_bvp.solve_newton is domain_newton.solve_newton,
                'The running SciPy Newton is not the original installed domain-aware function')
        runtime_newton = check_callback(scipy_bvp.solve_newton, launch['callbacks']['domain_solve_newton'])
        require(list(inspect.signature(scipy_bvp.solve_newton).parameters)
                == ['n','m','h','col_fun','bc','jac','y','p','B','bvp_tol','bc_tol'], 'Runtime Newton signature differs')
        manifest.update(status='RUNNING_FROZEN_AFFINE_DIAGNOSTIC', restart=restart,
                        initial_nodes=len(x), initial_boundary=initial_bc, runtime_callbacks=runtime_callbacks,
                        runtime_newton_after_install=runtime_newton, runtime_newton_identity_is_original=True)
        write_json(repro, manifest)
        print(json.dumps({'event': 'start_spectral_affine_diagnostic', **FLAGS, 'modes': obj.M,
                          'angular': obj.nt, 'nodes': len(x), 'tol': SETTINGS['tol']}), flush=True)
        # The sole change to the baseline mathematical solve is this callable.
        sol = solve_bvp(obj.fun, obj.bc, x, y, par, tol=SETTINGS['tol'],
                        bc_tol=cfg['bc_tol'], max_nodes=SETTINGS['max_nodes'],
                        fun_jac=obj.fun_jac, bc_jac=obj.bc_jac, verbose=2)
        require(scipy_bvp.solve_newton is domain_newton.solve_newton, 'Runtime Newton changed during collocation')
        flow = obj.flow(sol.p[0]); obj.initial(sol.p)
        physical = SimpleNamespace(x=obj.chart(sol.x, sol.p[0])[0], y=sol.y, p=sol.p)
        physical.sol = flow.c2_interpolant(physical)
        require(np.all(np.isfinite(physical.sol.c)), 'Nonfinite original physical C2 coefficients')
        out = {key: rec[key] for key in ('angular_chart','chart','warp_reference_q','frozen_profile',
                    'gauge_amplitude','physical_port_sha256','physical_tail_parameters','physical_tail_cut','tail_config')}
        out.update(scope=SCOPE, **FLAGS, config=dict(cfg, **FLAGS), actual_primary_amplitude=obj.support_amplitude,
                   meridian_length=flow.end, parameters=sol.p.tolist(), central_correction_scales=obj.pscale.tolist(),
                   nodes=len(sol.x), solver_success=bool(sol.success), message=sol.message,
                   max_rms_collocation_residual=float(np.max(sol.rms_residuals)),
                   newton_domain_audit=dict(domain_newton.STATS), mesh=physical.x.tolist(),
                   pp_coefficients=physical.sol.c, restart_mesh_diagnostics=restart,
                   frozen_actual_tail=launch['frozen_tail']['path'], frozen_actual_tail_sha256=launch['frozen_tail']['sha256'],
                   spectral_coordinate_audit=sol.spectral_coordinate_audit,
                   original_boundary=boundary_diagnostics(obj, sol.y, sol.p), actual_new_DN_calls=0)
        save_checkpoint(out_prefix.with_suffix('.json.gz'), out)
        out['summary'] = runner.adaptive.audit(obj, physical, max(1024, 64*obj.M))
        out['summary'].update(scope=SCOPE, **FLAGS)
        out['frozen_dn_height_change_linf'] = float(np.max(abs(
            obj.bridge.sigma*obj.q*physical.y[obj.iz:, -1]-startheight)))
        out['seconds'] = time.monotonic()-begin
        saved = save_checkpoint(out_prefix.with_suffix('.json.gz'), out)
        summary = {key: value for key, value in saved.items() if key != 'mesh'}
        manifest.update(status='RETURNED_FROZEN_AFFINE_DIAGNOSTIC', success=bool(sol.success),
                        nodes=len(sol.x), sampled_prefix_metric=out['summary']['metric_l1'],
                        original_physical_rms_max=out['max_rms_collocation_residual'],
                        original_boundary=out['original_boundary'],
                        frozen_dn_height_change_linf=out['frozen_dn_height_change_linf'],
                        spectral_coordinate_audit=sol.spectral_coordinate_audit,
                        checkpoint_output=identity(out_prefix.with_suffix('.json.gz')),
                        coefficient_outputs=[identity(out_prefix.parent / row['file']) for row in saved['pp_coefficient_chunks']])
        requested_exit = 0 if sol.success else 2
    except Exception as error:
        manifest.update(status='FROZEN_AFFINE_DIAGNOSTIC_EXCEPTION', success=False,
                        error_type=type(error).__name__, error=repr(error))
        summary = {key: value for key, value in manifest.items() if key != 'source_bindings'}
        print(json.dumps({'event': 'spectral_affine_exception', **FLAGS, 'error': repr(error)}), flush=True)
    manifest.update(seconds=time.monotonic()-begin, spectral_solver_records=solver_records,
                    requested_process_exit_code=requested_exit)
    summary.update(scope=SCOPE, **FLAGS, actual_new_DN_calls=0, requested_process_exit_code=requested_exit)
    write_json(repro, manifest)
    write_json(summary_path, summary, exclusive=True)
    print(json.dumps({'event': 'spectral_affine_program_result', **FLAGS,
                      'status': manifest['status'], 'success': manifest.get('success', False),
                      'requested_process_exit_code': requested_exit}), flush=True)
    return requested_exit


if __name__ == '__main__':
    sys.exit(main())
