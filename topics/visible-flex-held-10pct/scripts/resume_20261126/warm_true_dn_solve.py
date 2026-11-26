#!/usr/bin/env python3
"""Original finite nonlinear DN on an actually accepted warm lambda-one model.

The physical profile, complete anchor support, lambda=1 core family, gauge,
material chart, mean1168 and BC normalization .02 remain frozen. The p0
coordinate is log(q_aux/gauge_q), never a change of delta. This changes the
source's linear boundary problem to the original nonlinear finite-tail DN;
it is not a refinement of the original linear problem or a closure proof.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import argparse
import copy
import gc
import gzip
import hashlib
import importlib.util
import inspect
import json
import math
from pathlib import Path
import resource
import shutil
import sys
import threading
import time
import traceback
from types import SimpleNamespace
import numpy as np
from scipy.integrate import solve_bvp

WARM_KIND = 'warm-supported-material-phase-fixed-metric'
WARM_KIND_V2 = WARM_KIND+'-v2'
KIND = WARM_KIND+'-actual-dn'


def sha(path):
    value = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024*1024), b''):
            value.update(block)
    return value.hexdigest()


def load(path):
    return json.loads(Path(path).read_text())


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result


def write(path, value):
    path = Path(path)
    temporary = path.with_suffix(path.suffix+'.tmp')
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')
    temporary.replace(path)


def finite_leq(value, bound):
    return isinstance(value, (int, float)) and math.isfinite(value) and 0 <= value <= bound


def diagnostic_json(value):
    """Keep failed numerical returns recordable without accepting nonfinite data."""
    if isinstance(value, dict):
        return {key: diagnostic_json(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [diagnostic_json(item) for item in value]
    if isinstance(value, (float, np.floating)) and not math.isfinite(value):
        return 'nonfinite:'+str(value)
    return value


def model_path(repo, source):
    """Resolve the explicitly declared phase-coordinate contract."""
    name = {WARM_KIND: 'warm_fixed_m3_model.py',
            WARM_KIND_V2: 'warm_fixed_m3_model_v2.py'}.get(source.get('model_kind'))
    if name is None:
        raise ValueError('Unknown warm phase-coordinate model; no implicit reinterpretation')
    return Path(repo)/'topics/visible-flex-held-10pct/scripts/resume_20261126'/name


def validate_warm_source(repo, source_run):
    """Validate a real accepted lambda-one input; perform no numerical solve."""
    repo, source_run = Path(repo).resolve(), Path(source_run).resolve()
    source = load(source_run)
    if (source.get('model_kind') not in (WARM_KIND, WARM_KIND_V2)
            or source.get('fixed_metric') is not True
            or source.get('homotopy') != 1.
            or source.get('warm_definition', {}).get('homotopy') != 1.):
        raise ValueError('A real accepted warm lambda=1 model is required; no substitute is generated')
    if (source.get('terminal_kind') != 'original_linear_dn'
            or source.get('original_actual_nonlinear_tail')
            or source.get('actual_tail_requested')):
        raise ValueError('This first nonlinear-DN handoff requires its declared linear source')
    if source.get('model_kind') == WARM_KIND_V2:
        validator = module('_warm_v2_actual_input_gate', model_path(repo, source))
        # A verified same-map reexpression preserves its original solver
        # provenance; it is never relabelled as a new BVP return here.
        source = validator.accepted_input(source_run, require_lambda_one=True)
    elif (source.get('error') or source.get('status') != 'audited_finite_linear_candidate'
          or source.get('finite_linear_candidate_pass') is not True
          or source.get('solver_success') is not True
          or source.get('raw_return', {}).get('success') is not True):
        raise ValueError('The source has not actually passed its complete finite linear acceptance gate')
    if source.get('mean_nodes') != 1168 or source.get('bc_normalization') != .02:
        raise ValueError('The declared mean1168 and BC .02 must be retained')
    gates = source['gates']
    for key, upper in (('tol', 1e-6), ('bc_tol', 1e-7), ('physical_bc_tol', 2e-9)):
        if not finite_leq(gates.get(key), upper) or gates[key] == 0:
            raise ValueError('The source loosened an original gate: '+key)
    for value, bound in ((source['raw_return'].get('rms'), gates['tol']),
                         (source.get('original_scaled_bc_max'), gates['bc_tol']),
                         (source.get('linear_dn_physical_bc_max'), gates['physical_bc_tol'])):
        if not finite_leq(value, bound):
            raise ValueError('The source did not actually meet a recorded residual or boundary gate')
    modes = int(source['modes'])
    floor = 16*(3*modes+1)
    rows = source.get('metric_diagnostics')
    if (not isinstance(rows, list) or not rows or
            any(row.get('angular', 0) < floor or
                not finite_leq(row.get('legacy_max_component_fft_l1'), 1e-6) or
                not finite_leq(row.get('sample_operator_max'), 1e-6) for row in rows)):
        raise ValueError('The actual source metric audits failed or omit the original angular floor')
    for name, expected in source.get('source_hashes', {}).items():
        if sha(name) != expected:
            raise ValueError('A source model/step file changed: '+name)
    current = repo/'topics/visible-flex-held-10pct/scripts/resume_20261126'
    provider_name = ('warm_supported_core_factory_v2.py'
                     if source['model_kind'] == WARM_KIND_V2 else 'warm_supported_core_factory.py')
    if sha(current/provider_name) != source['warm_provider_sha256']:
        raise ValueError('The source warm core provider changed')
    if (source['model_kind'] == WARM_KIND_V2 and
            sha(current/'warm_supported_core_factory.py') != source['warm_geometry_base_sha256']):
        raise ValueError('The complete supported-core geometry implementation changed')
    files = {
        source_run.parent/source['raw_return']['file']: source['raw_return']['sha256'],
        source_run.parent/'physical.npz': source['physical_sha256'],
        Path(source['linear_port_path']): source['linear_port_sha256'],
        Path(source['origin_design_run']): source['origin_design_sha256'],
    }
    if source.get('relative_metric_sha256'):
        files[source_run.parent/'relative-metric.json'] = source['relative_metric_sha256']
    for path, expected in files.items():
        if sha(path) != expected:
            raise ValueError('An actual source field or binding changed: '+str(path))
    if source['gauge_q'] != source['warm_definition']['gauge_q']:
        raise ValueError('The source gauge and auxiliary carrier differ')
    return source


def load_model(config):
    """Read-only full geometry adapter for this actual-DN result, without a DN call."""
    path = Path(config['source_run']).resolve()
    record = load(path)
    if record.get('model_kind') != KIND or record.get('terminal_kind') != 'original_actual_nonlinear_dn':
        raise ValueError('Expected this declared warm actual-DN result')
    repo = Path(config.get('repo', record['repository']))
    source_path = Path(record['linear_source_run'])
    if sha(source_path) != record['linear_source_run_sha256']:
        raise ValueError('The accepted linear anchor run changed')
    source = validate_warm_source(repo, source_path)
    for key in ('frozen_profile', 'warm_definition', 'angular_chart', 'gauge_q',
                'warp_reference', 'mean_nodes', 'bc_normalization', 'modes', 'angular',
                'physical_tail_parameters', 'physical_tail_cut', 'linear_port_path',
                'linear_port_sha256', 'origin_design_run', 'origin_design_sha256'):
        if record[key] != source[key]:
            raise ValueError('Frozen actual-DN geometry changed: '+key)
    if record.get('linear_source_model_kind') != source['model_kind']:
        raise ValueError('The original phase-coordinate contract changed')
    for key in ('frozen_radial_chart', 'warm_geometry_base_sha256'):
        if record.get(key) != source.get(key):
            raise ValueError('The frozen versioned geometry changed: '+key)
    warm_model = module('_warm_actual_read_geometry', model_path(repo, source))
    obj = warm_model.load_model(dict(source_run=str(source_path)))
    obj.relative_metric_loader_record = dict(model_kind=KIND, fixed_metric=True,
        parameter_zero_meaning='log(q_aux/gauge_q)', mean_nodes=1168,
        source_run=str(path), source_run_sha256=sha(path),
        scope='The identical warm geometry; its nonlinear boundary is not evaluated by this read-only adapter',
        bvp_or_tail_solver_invoked=False, complete_surface=False)
    return obj


def last_scalar_event(path):
    if not path.exists():
        return None
    with path.open('rb') as stream:
        stream.seek(max(0, path.stat().st_size-32768))
        lines = stream.read().decode('utf-8', 'replace').splitlines()
    for line in reversed(lines):
        try:
            value = json.loads(line)
            if isinstance(value, dict):
                return {key: (str(item) if isinstance(item, float) and not math.isfinite(item) else item)
                        for key, item in value.items()
                        if item is None or isinstance(item, (str, bool, int, float))}
        except ValueError:
            pass
    return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'work', 'source-run', 'native-source', 'base-tail-config', 'tail-config', 'outdir'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--tail-warmup', type=float, nargs='*', default=[.25, .5, .75, .9])
    parser.add_argument('--audit-angular', type=int, nargs='+')
    parser.add_argument('--rhs-block', type=int, default=8)
    parser.add_argument('--max-nodes', type=int, default=6000)
    parser.add_argument('--verbose', type=int, default=2)
    args = parser.parse_args()
    repo, work, out = args.repo.resolve(), args.work.resolve(), args.outdir.resolve()
    source_path, native = args.source_run.resolve(), args.native_source.resolve()
    if (work not in out.parents or work not in source_path.parents or work not in native.parents
            or args.rhs_block < 1 or args.max_nodes < 2):
        raise ValueError('Use owned work paths and positive numerical settings')
    if (args.tail_warmup != sorted(set(args.tail_warmup))
            or not all(math.isfinite(factor) and 0 < factor < 1 for factor in args.tail_warmup)):
        raise ValueError('Warm factors must be explicitly increasing in (0,1)')
    out.mkdir(parents=True, exist_ok=False)
    lock, done = threading.RLock(), threading.Event()
    begin = time.monotonic()
    tail = monitor = None
    record = dict(scope=__doc__, status='validating_actual_lambda_one', model_kind=KIND,
        repository=str(repo), command=[sys.executable, *sys.argv],
        solver_success=False, finite_actual_dn_candidate_pass=False,
        fixed_metric=True, fixed_core=False, fixed_metric_refinement=False,
        fixed_metric_design_continuation=False, boundary_problem_changed=True,
        terminal_kind='original_actual_nonlinear_dn', actual_tail_requested=True,
        original_actual_nonlinear_tail=True, parameter_zero_meaning='log(q_aux/gauge_q)',
        complete_surface=False, C2_convergence_proven=False,
        full_Cartesian_seam_paid=False, stages=[], actual_outer_checks=[], progress={})

    def save():
        with lock:
            record['elapsed'] = time.monotonic()-begin
            write(out/'run.json', diagnostic_json(record))
            summary = {key: record[key] for key in
                ('scope', 'status', 'solver_success', 'finite_actual_dn_candidate_pass',
                 'complete_surface', 'error', 'result') if key in record}
            summary.update(progress=record['progress'], stages=record['stages'][-6:])
            summary = diagnostic_json(summary)
            if len(json.dumps(summary).encode()) > 24000:
                raise RuntimeError('Compact true-DN summary exceeded its declared 24 KiB ceiling')
            write(out/'summary.json', summary)

    def event(name, **data):
        with lock:
            row = dict(event=name, elapsed=time.monotonic()-begin,
                maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, **data)
            row = diagnostic_json(row)
            with (out/'events.jsonl').open('a') as stream:
                stream.write(json.dumps(row, allow_nan=False)+'\n')
            record['progress']['last_actual_event'] = row
            save()
        print(json.dumps(row, allow_nan=False), flush=True)

    save()
    try:
        source = validate_warm_source(repo, source_path)
        scripts = repo/'topics/visible-flex-held-10pct/scripts'
        current, resume = scripts/'resume_20261126', scripts/'resume_m3'
        warm_model = module('_warm_actual_source_geometry', model_path(repo, source))
        obj = warm_model.load_model(dict(source_run=str(source_path)))
        coupler = sys.modules['_metric_coupler']
        if (not obj.fixed or obj.cfg != source['frozen_profile'] or
                obj.q != source['gauge_q'] or not np.array_equal(obj.bcweights, np.full(obj.M, .02))):
            raise ValueError('The warm model did not preserve fixed metric, gauge or BC normalization')
        base_cfg, cfg = load(args.base_tail_config), load(args.tail_config)
        projected_cfg = {k: v for k, v in cfg.items()
                         if k not in ('traceFile', 'chordMaxCorrections', 'initialCheckpoint')}
        if projected_cfg != base_cfg or cfg.get('chordMaxCorrections') != 3:
            raise ValueError('Only the declared trace/warm checkpoint/chord runtime fields may differ')
        port = load(source['linear_port_path'])
        if port['source']['config_sha256'] != sha(args.base_tail_config):
            raise ValueError('Tail settings differ from the source linear port configuration')
        if (cfg['modes'] != obj.M or cfg['spacing'] != 3
                or cfg['quadrature'] <= 4*obj.M*3 or cfg['solveTolerance'] != 2e-9
                or any(k in cfg and cfg[k] != v for k, v in source['physical_tail_parameters'].items())):
            raise ValueError('The original tail dimensions, physical metric or tolerance changed')
        manifest_path = native/'native-manifest.json'
        manifest = load(manifest_path)
        for key, expected in dict(M=obj.M, spacing=3, quadrature=cfg['quadrature'],
                                  steps=cfg['steps'], projectionFloor=.05,
                                  orientation=1, cuspAwareFlow=True).items():
            if manifest['fixed_scope'][key] != expected:
                raise ValueError('Native fixed scope differs: '+key)
        if manifest['execution_provider']['workers'] != 2:
            raise ValueError('This entry retains the declared two native workers')
        for ref in [*manifest['owned_sources'], *manifest['native_files'].values()]:
            if sha(ref['path']) != ref['sha256']:
                raise ValueError('An original native source or binary changed: '+ref['path'])
        record.update({key: copy.deepcopy(source[key]) for key in
            ('frozen_profile', 'warm_definition', 'angular_chart', 'gauge_q', 'warp_reference',
             'mean_nodes', 'bc_normalization', 'modes', 'angular', 'origin_design_run',
             'origin_design_sha256', 'frozen_source_signature', 'physical_tail_parameters',
             'physical_tail_cut', 'linear_port_path', 'linear_port_sha256', 'warm_provider_sha256')})
        for key in ('frozen_radial_chart', 'warm_geometry_base_sha256'):
            if key in source:
                record[key] = copy.deepcopy(source[key])
        gates = dict(source['gates'], max_nodes=args.max_nodes,
                     tail_solve_tolerance=2e-9, original_outer_budget=8)
        audit_angular = sorted(set(max(16*(3*obj.M+1), int(n)) for n in
            (args.audit_angular or source.get('actual_audit_angular') or [16*(3*obj.M+1)])))
        record.update(linear_source_run=str(source_path), linear_source_run_sha256=sha(source_path),
            linear_source_model_kind=source['model_kind'],
            linear_source_acceptance_kind=source.get('acceptance_kind', 'actual_warm_bvp_return'),
            linear_source_solver_invoked=source.get('solver_invoked', True),
            source_raw_sha256=source['raw_return']['sha256'], source_physical_sha256=source['physical_sha256'],
            gates=gates, actual_audit_angular=audit_angular,
            source_hashes={str(path): sha(path) for path in
                (Path(__file__), model_path(repo, source), current/'warm_supported_core_factory.py',
                 resume/'portable_prefix_continue.py', current/'streamed_release_prefix_driver.py',
                 manifest_path, args.base_tail_config, args.tail_config)},
            tail_settings=str(args.tail_config.resolve()), tail_settings_sha256=sha(args.tail_config),
            native_manifest=str(manifest_path), native_manifest_sha256=sha(manifest_path),
            warm_height_arithmetic='numpy: H * factor**np.arange(1,M+1)',
            same_complete_problem_as_source=False)
        if source['model_kind'] == WARM_KIND_V2:
            for path in (current/'warm_supported_core_factory_v2.py',
                         current/'warm_auxiliary_domain_guard.py', current/'warm_fixed_m3_model.py'):
                record['source_hashes'][str(path)] = sha(path)
        raw_path = source_path.parent/source['raw_return']['file']
        with np.load(raw_path, allow_pickle=False) as data:
            x, y, par, scale = (data[key].copy() for key in ('x', 'y', 'p', 'pscale'))
        if (y.shape != (obj.n, len(x)) or par.shape != (obj.M,)
                or not np.array_equal(scale, obj.pscale)):
            raise ValueError('The actual phase raw dimensions or auxiliary parameter scales differ')
        obj.initial(par)
        if obj._core.homotopy != 1.:
            raise ValueError('The reconstructed actual core has not reached lambda=1')
        class ActualWarmBVP(coupler.TailMixin, type(obj)):
            def terminal(self, value, parameters):
                self.initial(parameters)
                return super().terminal(value, parameters)
        obj.__class__ = ActualWarmBVP
        # The mixin is the existing original terminal/Jacobian. Its ordinary
        # seam_audit has a different finite mean rule and is not used below.
        os.environ.update(VISIBLE_FLEX_NATIVE_MANIFEST=str(manifest_path),
            VISIBLE_FLEX_NATIVE_MANIFEST_SHA256=sha(manifest_path),
            VISIBLE_FLEX_NATIVE_RUN_DIR=str(Path(cfg['traceFile']).parent/'native-runs'),
            VISIBLE_FLEX_SPARSE_PYTHON=sys.executable,
            VISIBLE_FLEX_SPARSE_LINEAR_HELPER=str(scripts/
                'nonlinear_tail/m3_sparse_shooting_deliverable/sparse_shooting_linear.py'))
        for key in ('LD_PRELOAD', 'LD_LIBRARY_PATH'):
            os.environ.pop(key, None)
        Path(os.environ['VISIBLE_FLEX_NATIVE_RUN_DIR']).mkdir(parents=True, exist_ok=True)
        record['status'] = 'initializing_original_tail'
        save()

        def watch():
            while not done.wait(15):
                try:
                    value = last_scalar_event(Path(cfg['traceFile']))
                    if value is not None:
                        with lock:
                            record['progress']['last_actual_worker_trace'] = value
                            save()
                except (OSError, ValueError):
                    pass

        monitor = threading.Thread(target=watch, daemon=True)
        monitor.start()
        client = module('_warm_actual_native_client', native/'scripts/950f-tail-client-v3.py')
        tail = client.WeightedTailPort(args.tail_config, native/'repro/source-root', out/'tail', node_heap=2048)
        obj.tail = tail
        record['linear_dn_ready_max_difference'] = float(abs(tail.linearD-np.asarray(port['linearSlope'][:obj.M])).max())
        for key, expected in source['physical_tail_parameters'].items():
            if tail.ready['parameters'].get(key) != expected:
                raise ValueError('The actual factory physical parameter differs: '+key)
        for key in ('radius', 'backgroundSlope', 'backgroundSecond', 'E', 'Ep'):
            if tail.ready['cut'][key] != source['physical_tail_cut'][key]:
                raise ValueError('The original actual worker cut differs: '+key)
        write(out/'tail-ready.json', tail.ready)
        record.update(tail_ready_sha256=sha(out/'tail-ready.json'),
                      worker_physical_parameters_match=True)

        def height_binding(tag, height, raw_file, physical_file):
            path = out/('height-target-'+tag+'.json')
            item = dict(candidate_H=np.asarray(height, float).tolist(), modes=obj.M,
                gauge_q=obj.q, height_formula='bridge.sigma * fixed gauge_q * Y_height_at_cut',
                parameter_zero_meaning='log(q_aux/gauge_q)',
                linear_source_run=str(source_path), linear_source_run_sha256=sha(source_path),
                raw=str(raw_file), raw_sha256=sha(raw_file),
                physical=str(physical_file), physical_sha256=sha(physical_file),
                mean_nodes=1168, tag=tag,
                scope='Actual unscaled Dirichlet candidate from this complete saved prefix field; not an acceptance claim')
            write(path, item)
            return path

        def accepted_tail(height, *, jacobian, binding, factor, name):
            response = tail.solve(height, jacobian=jacobian, audit=True)
            if (response.get('converged') is not True or response.get('failed')
                    or not finite_leq(response.get('residual'), 2e-9)
                    or not isinstance(response.get('audit'), dict)):
                raise FloatingPointError('The original audited nonlinear tail gate failed')
            for key in ('height', 'slope', 'second'):
                values = np.asarray(response['jets'][key], float)
                if values.shape != (obj.M,) or not np.all(np.isfinite(values)):
                    raise ValueError('Incomplete actual cut jets: '+key)
            if jacobian:
                values = np.asarray(response.get('heightJetJacobian'), float)
                if values.shape != ((3*obj.M+2)*obj.M,) or not np.all(np.isfinite(values)):
                    raise ValueError('The complete original height Jacobian did not return')
            packet = out/f'tail_{tail.calls:04d}.json.gz'
            with gzip.open(packet, 'rt') as stream:
                saved = json.load(stream)
            expected = np.asarray(height, float).tolist()
            if (saved['request']['height'] != expected
                    or saved['response']['checkpoint']['cutHeight'] != expected
                    or saved['request']['audit'] is not True
                    or (jacobian and saved['request']['jacobian'] is not True)):
                raise ValueError('The saved original tail packet does not bind this exact requested height')
            row = dict(name=name, factor=factor, full_height=(factor == 1.),
                requested_jacobian=jacobian, residual=response['residual'], converged=True,
                packet=str(packet), packet_sha256=sha(packet),
                height_reference=str(binding), height_reference_sha256=sha(binding),
                height_reference_key='candidate_H', height_arithmetic='numpy')
            with lock:
                record['stages'].append(row)
                save()
            event('actual_tail_return', **row)
            return response, packet

        H = obj.bridge.sigma*obj.q*y[obj.iz:, -1]
        binding = height_binding('initial', H, raw_path, source_path.parent/'physical.npz')
        record.update(candidate_H=H.tolist(), initial_height_reference=str(binding),
                      status='original_true_dn_warmup')
        save()
        for factor in args.tail_warmup:
            accepted_tail(H*factor**np.arange(1, obj.M+1), jacobian=False,
                          binding=binding, factor=factor, name='initial_warm')
        response, packet = accepted_tail(H, jacobian=True, binding=binding, factor=1., name='initial_full_H')
        from f6curve_domain_newton import install, STATS
        install()
        portable = module('_warm_original_portable_guard', resume/'portable_prefix_continue.py')
        portable.install_rms_domain_guard()
        import f6curve_domain_newton as domain_newton
        before = inspect.getsource(domain_newton.solve_newton)
        marker = '            try:factor=splu(jac(y,p,ym,ff,fm,br))'
        if before.count(marker) != 1:
            raise ValueError('The original Newton refresh source changed')
        after = before.replace(marker, '            factor=None  # stale LU is not used on this refresh\n'+marker)
        exec(compile(after, str(Path(__file__).resolve())+'::released_newton', 'exec'), domain_newton.__dict__)
        domain_newton.install()
        batching = module('_warm_actual_bounded_rhs', current/'streamed_release_prefix_driver.py')
        record['resource_execution'] = dict(radial_block=args.rhs_block,
            original_newton_sha256=hashlib.sha256(before.encode()).hexdigest(),
            executed_newton_sha256=hashlib.sha256(after.encode()).hexdigest(),
            stale_unused_LU_released=True, original_gates_relaxed=False,
            floating_point_bit_identity_claimed=False)
        jac_count = 0
        original_jac = batching.split_jac(obj.fun_jac, args.rhs_block)
        def jacobian(t, values, parameters):
            nonlocal jac_count
            jac_count += 1
            temp = out/'last-jac-input.tmp.npz'
            np.savez_compressed(temp, x=t, y=values, p=parameters, pscale=obj.pscale)
            temp.replace(out/'last-jac-input.npz')
            event('jacobian_start', count=jac_count, nodes=len(t), snapshot_status='unaccepted Newton input only')
            answer = original_jac(t, values, parameters)
            event('jacobian_return', count=jac_count, nodes=len(t))
            return answer
        options = dict(tol=gates['tol'], bc_tol=gates['bc_tol'], max_nodes=args.max_nodes,
                       fun_jac=jacobian, bc_jac=obj.bc_jac, verbose=args.verbose)
        for outer in range(8):
            record.update(status='original_affine_inner_bvp', current_outer=outer)
            save()
            obj.tail = coupler.AffineTailForInnerBVP(H, response, obj.M)
            try:
                gc.collect()
                sol = solve_bvp(batching.split_rhs(obj.fun, args.rhs_block), obj.bc, x, y, par, **options)
            finally:
                obj.tail = tail
            raw = out/f'inner-{outer:02d}.npz'
            np.savez_compressed(raw, x=sol.x, y=sol.y, p=sol.p, cubic_c=sol.sol.c,
                                cubic_x=sol.sol.x, rms=sol.rms_residuals, pscale=obj.pscale)
            obj.initial(sol.p)
            candidate = obj.bridge.sigma*obj.q*sol.y[obj.iz:, -1]
            record.update(solver_success=bool(sol.success),
                raw_return=dict(file=raw.name, sha256=sha(raw), success=bool(sol.success),
                    status=int(sol.status), message=str(sol.message), nodes=len(sol.x),
                    rms=float(np.max(sol.rms_residuals)), parameters=sol.p.tolist(),
                    candidate_H=candidate.tolist(), actual_q_aux=float(obj.support_amplitude)),
                candidate_H=candidate.tolist(), returned_phase_controls=obj._core.controls.tolist(),
                domain_newton_stats=dict(STATS))
            save()
            if not sol.success:
                raise FloatingPointError('The original inner BVP did not converge')
            flow = obj.flow(sol.p[0])
            physical = SimpleNamespace(x=obj.chart(sol.x, sol.p[0])[0], y=sol.y, p=sol.p)
            physical.sol = flow.c2_interpolant(physical)
            physical_file = out/f'physical-{outer:02d}.npz'
            np.savez_compressed(physical_file, x=physical.x, c=physical.sol.c, p=sol.p)
            binding = height_binding(f'outer-{outer:02d}', candidate, raw, physical_file)
            record['status'] = 'original_actual_candidate_check'
            save()
            actual, packet = accepted_tail(candidate, jacobian=True, binding=binding,
                                           factor=1., name=f'outer_{outer:02d}_full_H')
            defect = float(abs(obj.bc(sol.y[:, 0], sol.y[:, -1], sol.p)).max())
            physical_bc = float(abs(obj.terminal(sol.y[:, -1], sol.p)*obj.bcweights).max())
            row = dict(outer=outer, actual_bc=defect, physical_bc=physical_bc,
                actual_tail=actual['residual'], raw_sha256=sha(raw), physical_sha256=sha(physical_file),
                height_reference=str(binding), height_reference_sha256=sha(binding),
                packet=str(packet), packet_sha256=sha(packet))
            record['actual_outer_checks'].append(row)
            save()
            event('actual_outer_check', **row)
            if defect <= gates['bc_tol'] and physical_bc <= gates['physical_bc_tol']:
                break
            x, y, par, H, response = sol.x, sol.y, sol.p, candidate, actual
        else:
            raise FloatingPointError('The original eight-outer actual boundary gate failed')
        shutil.copyfile(physical_file, out/'physical.npz')
        record['physical_sha256'] = sha(out/'physical.npz')
        record['actual_scaled_bc_max'], record['actual_physical_bc_max'] = defect, physical_bc
        record['status'] = 'auditing_actual_frozen_mean_map'
        save()
        metric_audit = module('_warm_actual_metric', resume/'audit_full_relative_metric.py')
        report = metric_audit.audit_loaded_model(obj, metric_audit.load_physical(out/'physical.npz'),
            angular=audit_angular, mean_nodes=1168, batch=8, target=1e-6)
        write(out/'relative-metric.json', report)
        record.update(relative_metric_sha256=sha(out/'relative-metric.json'), metric_diagnostics=report['rows'])
        # Same original cut formulas and angular audit, with the actual frozen
        # mean1168 used in BOTH the physical map and all mean mismatch fields.
        flow = obj.flow(sol.p[0])
        s = np.array([flow.end])
        Y, Yp, Ypp = (physical.sol(s, order) for order in (0, 1, 2))
        n = max(512, 64*obj.M)
        B, B1, B2 = flow.basis(n)
        fr, sp, dW = flow.velocity_s(s, Y, Yp, B1, B2)
        _, mean_B1, mean_B2 = flow.basis(1168)
        mean_fr, _, mean_dW = flow.velocity_s(s, Y, Yp, mean_B1, mean_B2)
        mean = np.mean(mean_fr['V'][:, :, 2], axis=1)
        mean_s = np.mean(mean_dW[:, :, 2], axis=1)
        g = fr['geo']
        chart_error = max(float(abs(g[key]).max()) for key in ('e', 'v', 'vs', 'vp'))
        if chart_error != 0.:
            raise ValueError('The original identity cut chart is required by the seam formulas')
        Fs = g['s1']+obj.q*flow.values(Yp, B)
        Fss = g['s2']+obj.q*flow.values(Ypp, B)
        Fs[:, :, 2] += mean[:, None]
        Fss[:, :, 2] += mean_s[:, None]
        Ft, Ftt, Fst = fr['d'], fr['dd'], sp
        aa, ap, _ = flow.profile(s)
        E0, F0, G0 = np.sum(Fs*Fs, axis=2), np.sum(Fs*Ft, axis=2), np.sum(Ft*Ft, axis=2)
        errors = np.stack((E0-1., F0/aa[:, None], G0/aa[:, None]**2-1.), axis=2)
        Es, Et = 2*np.sum(Fs*Fss, axis=2), 2*np.sum(Fs*Fst, axis=2)
        Fsmetric = np.sum(Fss*Ft+Fs*Fst, axis=2)
        Ftmetric = np.sum(Fst*Ft+Fs*Ftt, axis=2)
        Gs, Gt = 2*np.sum(Ft*Fst, axis=2), 2*np.sum(Ft*Ftt, axis=2)
        c1 = np.stack((Es, Et, Fsmetric/aa[:, None]-ap[:, None]*F0/aa[:, None]**2,
            Ftmetric/aa[:, None], Gs/aa[:, None]**2-2*ap[:, None]*G0/aa[:, None]**3,
            Gt/aa[:, None]**2), axis=2)
        # The just-accepted candidate already has the original audited full-J
        # packet at this exact unchanged H. Reuse that packet for read-only
        # cut diagnostics; do not solve the identical tail a second time.
        final = actual
        record['seam_reuses_same_accepted_full_H_packet'] = True
        jets = final['jets']
        E, sigma = jets['E'], obj.bridge.sigma
        r_ss = -jets['Ep']/(2*E**2)
        expected = (jets['meanSlope']/math.sqrt(E),
                    sigma*(jets['meanSecond']/E+jets['meanSlope']*r_ss))
        second = sigma*(np.asarray(jets['second'])/E+np.asarray(jets['slope'])*r_ss)
        seam = dict(mean_nodes=1168, angular_samples=n, cut_chart_error=chart_error,
            mean_first_actual=float(mean[0]), mean_second_actual=float(mean_s[0]),
            mean_first_expected=expected[0], mean_second_expected=expected[1],
            mean_first_mismatch=float(mean[0])-expected[0],
            mean_second_mismatch=float(mean_s[0])-expected[1],
            nonmean_first_mismatch=float(abs(obj.q*Yp[obj.iz:, 0]-np.asarray(jets['slope'])/math.sqrt(E)).max()),
            nonmean_second_mismatch=float(abs(obj.q*Ypp[obj.iz:, 0]-second).max()),
            cut_metric_fft_l1=float(np.sum(abs(np.fft.fft(errors, axis=1)/n), axis=1).max()),
            cut_metric_c1_fft_l1=float(np.sum(abs(np.fft.fft(c1, axis=1)/n), axis=1).max()),
            tail_converged=True, tail_shooting_residual=final['residual'],
            tail_packet=str(packet), tail_packet_sha256=sha(packet),
            scope='Actual frozen-mean1168 numerical map and original mean/nonmean cut formulas. '
                  'These finite diagnostics are not a complete Cartesian seam or infinite closure certificate.')
        write(out/'frozen-mean-seam.json', seam)
        metric_pass = bool(report['rows'] and all(
            finite_leq(row['legacy_max_component_fft_l1'], 1e-6) and
            finite_leq(row['sample_operator_max'], 1e-6) for row in report['rows']))
        accepted = bool(sol.success and finite_leq(record['raw_return']['rms'], gates['tol'])
            and finite_leq(defect, gates['bc_tol']) and finite_leq(physical_bc, gates['physical_bc_tol'])
            and metric_pass and finite_leq(final['residual'], 2e-9))
        record.update(status='audited_finite_actual_dn_candidate', tail_seam=seam,
            frozen_mean_seam_sha256=sha(out/'frozen-mean-seam.json'),
            finite_actual_dn_candidate_pass=accepted, tail_calls=tail.calls,
            result=dict(original_nonlinear_DN_accepted=accepted,
                raw_sha256=record['raw_return']['sha256'], physical_sha256=record['physical_sha256'],
                actual_bc_max=defect, physical_bc_max=physical_bc, tail_residual=final['residual'],
                metric_max=max(row['legacy_max_component_fft_l1'] for row in report['rows']),
                height_reference=str(binding), full_height_record=str(packet),
                mean_first_mismatch=seam['mean_first_mismatch'], mean_second_mismatch=seam['mean_second_mismatch'],
                full_Cartesian_seam_paid=False, complete_surface=False))
        save()
        event('actual_dn_terminal', accepted=accepted, actual_bc=defect,
              physical_bc=physical_bc, metric_pass=metric_pass, tail_residual=final['residual'])
        return 0 if accepted else 2
    except Exception as error:
        record.update(status='actual_dn_stage_failed', error=repr(error),
                      exception=traceback.format_exc().splitlines()[-32:],
                      tail_calls=tail.calls if tail is not None else 0)
        save()
        event('error', error=repr(error))
        return 2
    finally:
        done.set()
        if monitor is not None:
            monitor.join(timeout=2)
        if tail is not None:
            tail.close()


if __name__ == '__main__':
    sys.exit(main())
