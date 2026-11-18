#!/usr/bin/env python3
"""One predeclared physical-parameter Jacobian diagnostic, with no solve.

--prepare is read-only metadata/array inspection plus a fresh plan/command.
--run-plan is a separate numerical operation. It constructs the same new M8
trace core directly and reads the saved safe initial x/y/p; it does not repeat
the old-map reprojection, initializer diagnostics, BVP, tail, or failed audit.
Ten literal original node indices and three literal physical central-difference
steps are fixed before any evaluation. A domain rejection ends the diagnostic;
there is no alternate step, point selection, parameter search, or gate change.

The seven core-control columns and stored inlet Jacobian are analytic. The
existing delta column of fun_jac itself uses its original centered difference;
that column is labeled separately. This is a finite numerical consistency
check, not a continuous derivative certificate or a new accepted solution.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import copy
import gzip
import hashlib
import importlib.metadata
import json
import math
from pathlib import Path
import sys
import time
import traceback
import numpy as np

HERE = Path(__file__).resolve().parent
WORK = HERE.parents[4]
PARENT = WORK/'m3_work/q060-circle-trace-lobatto-guard-v1/lobatto-launch-plan.json'
PARENT_SHA = 'da2c3d945ac45fcb04dc456c7e00283fb1c8b9bdbe4d2fe5fb5d3c8687c2374b'
INITIAL = WORK/'m3_work/q060-circle-trace-coupled-v1/inner-00-entry.json.gz'
INITIAL_SHA = 'a2fced8cb9864fb9c3190d999d5a5a0e09ed08779c1efa867808bb088a6231f4'
FINAL = WORK/'m3_work/q060-circle-trace-lobatto-guard-v1/inner-00-returned.json.gz'
FINAL_SHA = '6961706a8a9f7c50decf735b2e75f88f51c89a9138ba6830a11e86958044a4f0'
FAILED_CP = FINAL.with_name('seed.json.gz')
FAILED_CP_SHA = '5244dcd8636c586376aa1bc824593a87453933e3f006049d5f87edfa4e0a3a60'
TERMINAL = HERE/'q060_circle_trace_lobatto_guard_terminal.json'
TERMINAL_SHA = 'b35c3a5e1194115fed6a7a019c55031d04aa1d71ce381312bceb97944a89e9d9'
OBSERVER = HERE.parent/'resume_n4/observe_command_live.py'
NODE_INDICES = (0, 5, 17, 33, 65, 97, 129, 193, 257, 270)
STEP_EXPONENTS = (-20, -21, -22)
LABELS = ('delta', 'c_B2', 'c_B3', 'c_B4', 'c_B5', 'c_B6', 't_T', 'u_U')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ref(path):
    return dict(path=str(Path(path).resolve()), sha256=sha(path))


def load(path):
    path = Path(path)
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw)


def binary_sha(value):
    return hashlib.sha256(np.asarray(value, dtype='float64').tobytes()).hexdigest()


def payload_sha(value):
    text = json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)
    return hashlib.sha256(text.encode()).hexdigest()


def write_json(path, value):
    with Path(path).open('x') as stream:
        json.dump(value, stream, indent=2, allow_nan=False)
        stream.write('\n')


def check_sources(sources):
    for path, expected in sources.items():
        if sha(path) != expected:
            raise ValueError('Changed bound source/input: ' + path)


def check_payload(plan):
    value = copy.deepcopy(plan)
    expected = value.pop('identity_sha256')
    if payload_sha(value) != expected:
        raise ValueError('Plan payload identity changed')


def physical_parameters(p, scales, base_delta):
    return np.r_[base_delta + p[0], p[1:] * scales]


def final_readonly_summary(initial, returned, checkpoint):
    """Only stored scalar/array arithmetic; no chart, core, RHS or interpolation."""
    x = np.asarray(returned['x'], float)
    rms = np.asarray(returned['rms_residuals'], float)
    s = np.asarray(checkpoint['mesh'], float)
    p = np.asarray(returned['p'], float)
    scales = np.asarray(returned['parameter_scales'], float)
    if x.shape != (2431,) or rms.shape != (2430,) or s.shape != x.shape:
        raise ValueError('The reviewed returned mesh/RMS identity changed')
    if not np.all(np.isfinite(rms)) or np.min(rms) < 0:
        raise ValueError('Invalid stored RMS scalars')
    if binary_sha(p) != binary_sha(checkpoint['parameters']):
        raise ValueError('Returned and physical-checkpoint parameters differ')
    if binary_sha(scales) != binary_sha(checkpoint['central_correction_scales']):
        raise ValueError('Returned and physical-checkpoint scales differ')
    c = p[1:] * scales
    if binary_sha(c) != binary_sha(checkpoint['physical_controls']):
        raise ValueError('Returned physical controls differ')
    base_delta = initial['base_frozen_profile']['delta']
    oldp = np.asarray(initial['p'], float)
    oldphysical = physical_parameters(oldp, scales, base_delta)
    finalphysical = physical_parameters(p, scales, base_delta)
    order = sorted(range(len(rms)), key=lambda i: (-float(rms[i]), i))[:12]
    rows = [dict(index=int(i), t_left=float(x[i]), t_right=float(x[i+1]),
                 saved_physical_s_left=float(s[i]), saved_physical_s_right=float(s[i+1]),
                 saved_rms=float(rms[i])) for i in order]
    return dict(
        solver_success=returned['solver_success'], status=returned['status'],
        message=returned['message'], nodes=len(x), intervals=len(rms),
        maximum_saved_rms=float(np.max(rms)), largest_saved_RMS_intervals=rows,
        saved_rms_binary64_sha256=binary_sha(rms),
        physical_mesh_scope='The failed physical checkpoint stores the physical s corresponding to these returned node indices; no chart was reevaluated here.',
        parameter_rows=[dict(index=j, name=LABELS[j],
            physical_units_per_parameter=float(1. if j == 0 else scales[j-1]),
            initial_parameter=float(oldp[j]), final_parameter=float(p[j]),
            initial_physical_value=float(oldphysical[j]), final_physical_value=float(finalphysical[j]),
            physical_change=float(finalphysical[j]-oldphysical[j])) for j in range(8)],
        component_residual_location=None,
        component_residual_scope='The returned record stores interval RMS scalars, not component collocation residuals or each Lobatto residual vector. No component, Fourier mode, or angular worst point is inferred.',
        final_state_reevaluated=False, final_state_differenced=False,
        complete_metric_available=False, accepted_state=False)


def prepare(directory):
    fixed = {str(PARENT): PARENT_SHA, str(INITIAL): INITIAL_SHA, str(FINAL): FINAL_SHA,
             str(FAILED_CP): FAILED_CP_SHA, str(TERMINAL): TERMINAL_SHA}
    check_sources(fixed)
    parent = load(PARENT)
    check_payload(parent)
    check_sources(parent['source_sha256'])
    initial, returned, cp = load(INITIAL), load(FINAL), load(FAILED_CP)
    x, y, p = (np.asarray(initial[k], float) for k in ('x', 'y', 'p'))
    scales = np.asarray(initial['parameter_scales'], float)
    design = parent['design']
    if x.shape != (271,) or y.shape != (25, 271) or p.shape != (8,) or scales.shape != (7,):
        raise ValueError('Use the saved safe M8 initial state, without interpolation')
    if p[0] != 0. or initial['fixed_metric'] is not False:
        raise ValueError('The new fixed=False initial p0 must be zero')
    if (initial['base_frozen_profile'] != design['physical_profile'] or
        initial['core_round_settings'] != design['new_core_settings'] or
        initial['q_gauge'] != design['new_q']['binary64']):
        raise ValueError('Saved initial physical design differs')
    if (binary_sha(y) != parent['initial_hashes']['state_binary64_sha256'] or
        binary_sha(p) != parent['initial_hashes']['parameter_binary64_sha256'] or
        binary_sha(scales) != binary_sha(parent['initial_parameter_scales']) or
        binary_sha(p[1:]*scales) != binary_sha(parent['initial_physical_controls'])):
        raise ValueError('Saved initial full state/parameters/scales/controls changed')
    oldplan = initial['plan']
    if sha(oldplan['path']) != oldplan['sha256']:
        raise ValueError('The original raw-entry producer plan changed')
    references = dict(parent_plan=ref(PARENT), original_entry_producer_plan=oldplan,
        safe_initial_raw=ref(INITIAL), failed_returned_raw=ref(FINAL),
        failed_physical_checkpoint=ref(FAILED_CP), published_terminal_record=ref(TERMINAL),
        chart=design['original_chart'], linear_port=design['physical_port'],
        physical_profile=parent['profile'], original_reference_binding=design['old_reference_binding'])
    for item in references.values():
        if sha(item['path']) != item['sha256']:
            raise ValueError('Changed diagnostic input: '+item['path'])
    binding = load(design['old_reference_binding']['path'])
    source_map = {**parent['source_sha256'], **fixed,
                  str(Path(__file__).resolve()): sha(__file__)}
    directory = Path(directory).resolve()
    if directory.exists():
        raise FileExistsError('Use a new diagnostic directory')
    steps = [math.ldexp(1., e) for e in STEP_EXPONENTS]
    plan = dict(scope=__doc__, source_sha256=source_map, inputs=references,
        construction=dict(source_topic=binding['source_topic'],
            short_bridge=binding['short_bridge'], settings=copy.deepcopy(design['new_core_settings']),
            q=initial['q_gauge'], warp_reference_q=design['warp_reference_q'],
            modes=8, angular=256, fixed=False, physical_profile=initial['base_frozen_profile'],
            physical_BC_tolerance=2e-9, BC_tolerance=1e-7,
            procedure='The same RawDiagnosticEnvironment, fresh trace factory, fresh Flow/Base, exact lift once at (.5,.9), and existing analytic_adaptive_core_jac. Read saved x/y/p directly; do not call old native_reference, restart, reprojection, initializer diagnostic, BC, terminal, audit, mean-height, BVP or actual tail.'),
        safe_initial=dict(x_binary64_sha256=binary_sha(x), y_binary64_sha256=binary_sha(y),
            p_binary64_sha256=binary_sha(p), parameter_scales=scales.tolist(),
            physical_controls=(p[1:]*scales).tolist(),
            node_indices=list(NODE_INDICES), normalized_nodes=x[list(NODE_INDICES)].tolist(),
            selected_y_binary64_sha256=binary_sha(y[:, list(NODE_INDICES)]),
            saved_complete_H_binary64_sha256=parent['initial_hashes']['full_H_binary64_sha256']),
        finite_difference=dict(parameter_labels=list(LABELS), physical_step_exponents=list(STEP_EXPONENTS),
            physical_steps=steps, loop_order='parameter 0..7, then exponents -20,-21,-22; plus before minus',
            input_rule='Hold the selected original normalized t and saved Y fixed. p0 perturbation is h; control perturbation is h/pscale. The original delta-dependent chart is evaluated by the original fun, not frozen in physical s.',
            units='delta=base_frozen_profile.delta+p0; c_j=pscale_j*p_j, including the physical t_T and u_U trace coefficients.',
            nominal_estimator='(F(p_plus)-F(p_minus))/(2*h), compared to fun_jac parameter column / physical_units_per_parameter; the same for initial(p) and stored _initial_jac.',
            encoded_estimator='Also divide by the actual binary64 physical_value_plus-physical_value_minus, recording both steps, center drift, and actual p±/c±. This is a rounding diagnostic, not a changed stencil.',
            domain_policy='Each original initial/core and fun/frame gate must pass. Any rejected or nonfinite evaluation ends the diagnostic, preserving completed rows and the exception; never shrink h or replace points.',
            baseline_parameter_column_kind=['Existing original centered-difference delta column']+['Analytic integral-core control column']*7,
            existing_delta_column_step=2e-6*max(.1, initial['base_frozen_profile']['delta']),
            error_reports='Absolute maximum, maximum / max(1, max|analytic|), maximum / max(max|analytic|, max|FD|, 1e-300), and exact component/node location; no new acceptance tolerance.'),
        final_readonly=final_readonly_summary(initial, returned, cp),
        scipy=dict(version=importlib.metadata.version('scipy'),
            source=[dict(path=k,sha256=v) for k,v in source_map.items() if k.endswith('/scipy/integrate/_bvp.py')]),
        diagnostic_output=str(directory/'diagnostic.json'), arrays_output=str(directory/'diagnostic-arrays.npz'),
        events_output=str(directory/'diagnostic-events.jsonl'),
        metadata_only=True, new_core_evaluated=False, numerical_jacobian_probe_executed=False,
        BVP_solver_invoked=False, actual_tail_solver_invoked=False,
        final_state_reevaluated=False, mean_height_reconstructed=False)
    plan['identity_sha256'] = payload_sha(plan)
    directory.mkdir(parents=True)
    path = directory/'launch-plan.json'
    write_json(path, plan)
    command = [sys.executable, str(Path(__file__).resolve()), '--run-plan', str(path)]
    observer = [sys.executable, str(OBSERVER), '--out', str(directory/'resource.json'),
                '--log', str(directory/'stdout.log'), '--', *command]
    write_json(directory/'launch-command.json', dict(plan=ref(path), command=command,
                                                    observer_command=observer))
    print(json.dumps(dict(metadata_only=True, plan=ref(path), identity_sha256=plan['identity_sha256'],
        source_inputs=len(source_map), references=len(references), node_indices=list(NODE_INDICES),
        physical_steps=steps, no_numerical_probe=True)), flush=True)


def build_model(plan, counters):
    """Production equations/classes, with unreachable solve paths forbidden."""
    import scipy.integrate
    from scipy.integrate import _bvp
    def forbidden_bvp(*args, **kwargs):
        counters['BVP_attempts'] += 1
        raise RuntimeError('This diagnostic may not invoke a BVP solver')
    scipy.integrate.solve_bvp = forbidden_bvp
    _bvp.solve_bvp = forbidden_bvp
    from m3_raw_diagnostic_model import RawDiagnosticEnvironment
    cfg = plan['construction']
    chart = load(plan['inputs']['chart']['path'])
    port = load(plan['inputs']['linear_port']['path'])
    port['_sha256'] = plan['inputs']['linear_port']['sha256']
    settings = copy.deepcopy(cfg['settings'])
    env = RawDiagnosticEnvironment(cfg['source_topic'], cfg['short_bridge']['path'], chart, settings)
    from plateau_core import PlateauSupportCore
    from circle_trace_replacement_core import make_core_class
    Core = make_core_class(PlateauSupportCore)
    factory = lambda amplitude, corrections=(), base_mode=3: Core(
        amplitude, corrections, base_mode, arc_nodes=1024, **settings)
    __import__('fixed_metric_mode3_core').PlanarSupportCore = factory
    __import__('fixed_metric_mode3_bvp').PlanarSupportCore = factory
    Flow, Base = env.coupler.adaptive.build_classes(chart)
    from exact_core_lift import install_core_lift
    from analytic_adaptive_core_jac import install as install_parameter_jac
    Lift = install_core_lift(Flow, Base, window=(.5, .9))
    install_parameter_jac(Lift)
    class BVP(env.coupler.TailMixin, Lift):
        pass
    class ForbiddenTail:
        def solve(self, *args, **kwargs):
            counters['tail_attempts'] += 1
            raise RuntimeError('This diagnostic may not invoke even an affine tail')
    obj = BVP(copy.deepcopy(cfg['physical_profile']), port, cfg['q'], cfg['modes'],
              cfg['angular'], cfg['fixed'], cfg['warp_reference_q'])
    obj.bcweights = np.full(cfg['modes'], cfg['physical_BC_tolerance']/cfg['BC_tolerance'])
    obj.tail = ForbiddenTail()
    for path, actual in env.sources.items():
        if plan['source_sha256'].get(path) != actual:
            raise ValueError('Model loaded an unbound or changed source: '+path)
    return obj, Core


def difference_summary(analytic, finite, selected_nodes):
    diff = np.abs(finite-analytic)
    ix = np.unravel_index(int(np.argmax(diff)), diff.shape)
    peak = float(diff[ix])
    amax, fmax = float(np.max(np.abs(analytic))), float(np.max(np.abs(finite)))
    where = dict(component=int(ix[0]))
    if analytic.ndim == 2:
        where.update(selected_node_position=int(ix[1]), original_node_index=int(selected_nodes[ix[1]]))
    return dict(maximum_absolute_difference=peak, analytic_maximum_absolute=amax,
        finite_difference_maximum_absolute=fmax, mixed_scale_difference=peak/max(1., amax),
        relative_scale_difference=peak/max(amax, fmax, 1e-300), largest_difference_at=where)


def execute(plan_path):
    plan_path = Path(plan_path).resolve()
    plan = load(plan_path)
    check_payload(plan)
    check_sources(plan['source_sha256'])
    for item in plan['inputs'].values():
        if sha(item['path']) != item['sha256']:
            raise ValueError('Changed planned input: '+item['path'])
    if plan['safe_initial']['node_indices'] != list(NODE_INDICES):
        raise ValueError('The fixed node selection changed')
    if plan['finite_difference']['physical_step_exponents'] != list(STEP_EXPONENTS):
        raise ValueError('The predeclared stencil changed')
    for key in ('diagnostic_output', 'arrays_output', 'events_output'):
        if Path(plan[key]).exists():
            raise FileExistsError('The planned diagnostic already began')
    began = time.monotonic()
    counters = dict(BVP_attempts=0, tail_attempts=0, original_fun_evaluations=0,
                    original_fun_jac_evaluations=0, original_initial_evaluations=0)
    result = dict(scope=__doc__, plan=ref(plan_path), plan_identity_sha256=plan['identity_sha256'],
        source_sha256=plan['source_sha256'], finite_difference=plan['finite_difference'],
        final_readonly=plan['final_readonly'], completed=False, rows=[], counters=counters,
        BVP_solver_invoked=False, actual_tail_solver_invoked=False, mean_height_reconstructed=False,
        final_state_reevaluated=False, original_initial_reprojection_repeated=False)
    arrays = {}
    def event(name, **fields):
        row = dict(event=name, utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), **fields)
        with Path(plan['events_output']).open('a') as stream:
            stream.write(json.dumps(row, separators=(',', ':'), allow_nan=False)+'\n')
        print(json.dumps(row, separators=(',', ':'), allow_nan=False), flush=True)
    event('diagnostic_started', plan=ref(plan_path))
    stage = 'construct_original_model'
    try:
        initial = load(plan['inputs']['safe_initial_raw']['path'])
        x, full_y, p = (np.asarray(initial[k], float) for k in ('x', 'y', 'p'))
        indices = np.asarray(NODE_INDICES, int)
        t, y = x[indices].copy(), full_y[:, indices].copy()
        obj, Core = build_model(plan, counters)
        scales = np.asarray(obj.pscale, float)
        units = np.r_[1., scales]
        if binary_sha(scales) != binary_sha(plan['safe_initial']['parameter_scales']):
            raise ValueError('Actual constructor parameter scales changed')
        if (binary_sha(p) != plan['safe_initial']['p_binary64_sha256'] or
            binary_sha(full_y) != plan['safe_initial']['y_binary64_sha256'] or
            binary_sha(x) != plan['safe_initial']['x_binary64_sha256'] or
            binary_sha(y) != plan['safe_initial']['selected_y_binary64_sha256']):
            raise ValueError('Saved baseline arrays changed')
        stage = 'baseline_initial'
        baseline_initial = obj.initial(p).copy()
        counters['original_initial_evaluations'] += 1
        if not isinstance(obj._core, Core):
            raise ValueError('The new factory was not captured by the new class')
        if (obj.support_amplitude != plan['construction']['q'] or
            binary_sha(p[1:]*scales) != binary_sha(plan['safe_initial']['physical_controls']) or
            binary_sha(obj._core.c) != binary_sha(plan['safe_initial']['physical_controls'])):
            raise ValueError('Actual baseline core amplitude/controls changed')
        analytic_initial = obj._initial_jac.copy()/units[None, :]
        stage = 'baseline_fun'
        baseline_fun = obj.fun(t, y, p)
        counters['original_fun_evaluations'] += 1
        stage = 'baseline_fun_jac'
        state_jac, parameter_jac = obj.fun_jac(t, y, p)
        counters['original_fun_jac_evaluations'] += 1
        analytic_fun = parameter_jac/units[None, :, None]
        for value in (baseline_initial, baseline_fun, state_jac, analytic_initial, analytic_fun):
            if not np.all(np.isfinite(value)):
                raise FloatingPointError('Nonfinite baseline derivative/value')
        arrays.update(selected_t=t, selected_y=y, parameters=p, physical_units=units,
            baseline_fun=baseline_fun, baseline_initial=baseline_initial,
            parameter_jac_original=parameter_jac, parameter_jac_physical=analytic_fun,
            initial_jac_physical=analytic_initial)
        result['baseline'] = dict(original_domains_passed=True, selected_nodes=t.tolist(),
            parameter_scales=scales.tolist(), physical_controls=(p[1:]*scales).tolist(),
            fixed_q=obj.support_amplitude,
            numerical_core_guard=dict(rho_lower_conservative=float(obj._core.rho_lower),
                rho_min_sample=float(obj._core.rho_min_sample),
                positivity_grid_per_sector=int(obj._core.positivity_grid_per_sector),
                scope='Stored original numerical guard attributes; not an interval certificate or a new angular scan.'),
            baseline_fun_binary64_sha256=binary_sha(baseline_fun),
            baseline_initial_binary64_sha256=binary_sha(baseline_initial),
            parameter_jac_binary64_sha256=binary_sha(parameter_jac),
            parameter_jac_shape=list(parameter_jac.shape), state_jac_shape=list(state_jac.shape),
            state_jac_scope='The original fun_jac returns it as well; finite checked only, not independently tested here.')
        event('baseline_domains_and_columns_available', parameter_jac_shape=list(parameter_jac.shape))
        base_delta = plan['construction']['physical_profile']['delta']
        basephysical = physical_parameters(p, scales, base_delta)
        for j, label in enumerate(LABELS):
            for exponent in STEP_EXPONENTS:
                h = math.ldexp(1., exponent)
                step = h/units[j]
                plus, minus = p.copy(), p.copy()
                plus[j] += step
                minus[j] -= step
                physical_plus = physical_parameters(plus, scales, base_delta)
                physical_minus = physical_parameters(minus, scales, base_delta)
                denominator = float(physical_plus[j]-physical_minus[j])
                if not math.isfinite(denominator) or denominator <= 0:
                    raise FloatingPointError('Physical encoded central stencil collapsed')
                result['active_stencil'] = dict(parameter=j, name=label, exponent=exponent,
                    physical_step=h, parameter_plus=plus.tolist(), parameter_minus=minus.tolist(),
                    physical_plus=physical_plus.tolist(), physical_minus=physical_minus.tolist())
                key = f'p{j}_e{abs(exponent)}'
                stage = f'parameter_{j}_exponent_{exponent}_plus_original_domain'
                ip = obj.initial(plus).copy()
                counters['original_initial_evaluations'] += 1
                arrays[key+'_initial_plus'] = ip
                fp = obj.fun(t, y, plus)
                counters['original_fun_evaluations'] += 1
                arrays[key+'_fun_plus'] = fp
                stage = f'parameter_{j}_exponent_{exponent}_minus_original_domain'
                im = obj.initial(minus).copy()
                counters['original_initial_evaluations'] += 1
                arrays[key+'_initial_minus'] = im
                fm = obj.fun(t, y, minus)
                counters['original_fun_evaluations'] += 1
                arrays[key+'_fun_minus'] = fm
                for value in (ip, im, fp, fm):
                    if not np.all(np.isfinite(value)):
                        raise FloatingPointError('Nonfinite perturbed original value')
                fd_fun, fd_initial = (fp-fm)/(2*h), (ip-im)/(2*h)
                encoded_fun, encoded_initial = (fp-fm)/denominator, (ip-im)/denominator
                arrays.update({key+'_fun_plus':fp, key+'_fun_minus':fm,
                               key+'_initial_plus':ip, key+'_initial_minus':im,
                               key+'_fun_fd_nominal':fd_fun, key+'_initial_fd_nominal':fd_initial,
                               key+'_fun_fd_encoded':encoded_fun, key+'_initial_fd_encoded':encoded_initial})
                row = dict(parameter=j, name=label, physical_step=h, physical_step_exponent=exponent,
                    parameter_step=step, parameter_plus=float(plus[j]), parameter_minus=float(minus[j]),
                    physical_base=float(basephysical[j]), physical_plus=float(physical_plus[j]),
                    physical_minus=float(physical_minus[j]),
                    actual_physical_plus_step=float(physical_plus[j]-basephysical[j]),
                    actual_physical_minus_step=float(basephysical[j]-physical_minus[j]),
                    encoded_physical_denominator=denominator,
                    encoded_physical_center_drift=float((physical_plus[j]-basephysical[j])+(physical_minus[j]-basephysical[j]))/2,
                    original_domains_passed=True,
                    fun_nominal=difference_summary(analytic_fun[:,j,:], fd_fun, NODE_INDICES),
                    fun_encoded=difference_summary(analytic_fun[:,j,:], encoded_fun, NODE_INDICES),
                    initial_nominal=difference_summary(analytic_initial[:,j], fd_initial, NODE_INDICES),
                    initial_encoded=difference_summary(analytic_initial[:,j], encoded_initial, NODE_INDICES))
                result['rows'].append(row)
                event('fixed_stencil_completed', parameter=j, exponent=exponent,
                      fun_difference=row['fun_nominal']['maximum_absolute_difference'],
                      initial_difference=row['initial_nominal']['maximum_absolute_difference'])
        stage = 'restore_original_baseline'
        restored_initial = obj.initial(p).copy()
        counters['original_initial_evaluations'] += 1
        restored_fun = obj.fun(t, y, p)
        counters['original_fun_evaluations'] += 1
        if counters['BVP_attempts'] or counters['tail_attempts']:
            raise RuntimeError('A forbidden solver path was attempted')
        if binary_sha(y) != plan['safe_initial']['selected_y_binary64_sha256']:
            raise ValueError('Selected fixed state was mutated')
        result['restored_baseline'] = dict(
            initial_binary64_equal=binary_sha(restored_initial)==binary_sha(baseline_initial),
            fun_binary64_equal=binary_sha(restored_fun)==binary_sha(baseline_fun),
            initial_maximum_difference=float(np.max(np.abs(restored_initial-baseline_initial))),
            fun_maximum_difference=float(np.max(np.abs(restored_fun-baseline_fun))))
        result['completed'] = True
        result['numerical_probe_scope'] = 'One original initial state, ten fixed original nodes, 24 predeclared physical stencils. No matrix condition number or BVP convergence is inferred from these column differences.'
    except Exception as error:
        result['failure'] = dict(stage=stage, type=type(error).__name__, message=str(error),
                                 traceback=traceback.format_exc(), automatic_retry=False)
        event('diagnostic_failed', stage=stage, error=repr(error), completed_stencils=len(result['rows']))
    check_sources(plan['source_sha256'])
    if arrays:
        with Path(plan['arrays_output']).open('xb') as stream:
            np.savez_compressed(stream, **arrays)
        result['arrays'] = ref(plan['arrays_output'])
        result['array_scope'] = 'Scratch only; full finite values and derivative arrays, reproducible from the bound inputs and source.'
    result['seconds'] = time.monotonic()-began
    result['exit_status_requested'] = 0 if result['completed'] else 2
    result['counters_scope'] = 'Explicit top-level diagnostic calls; original fun_jac internally calls fun for its unchanged delta column, and original fun invokes initial. These internal calls are not added to the top-level counters.'
    write_json(plan['diagnostic_output'], result)
    event('diagnostic_record_saved', output=ref(plan['diagnostic_output']), completed=result['completed'])
    return result['exit_status_requested']


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--prepare', type=Path)
    group.add_argument('--run-plan', type=Path)
    args = parser.parse_args()
    if args.prepare:
        prepare(args.prepare)
        return 0
    return execute(args.run_plan)


if __name__ == '__main__':
    raise SystemExit(main())
