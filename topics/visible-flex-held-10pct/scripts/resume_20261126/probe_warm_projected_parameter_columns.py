#!/usr/bin/env python3
"""Read actual v2/v3 zero-control anchor columns without a BVP solve.

The complete exact core lift is retained. Initial Fourier projection alone
does not measure the full differential operator or its inverse. Each family
is constructed in a separate process to isolate the original global factory
installation. Only the already accepted lambda=.002 anchor is eligible.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import copy
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import subprocess
import sys
import time
import traceback
import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def write(path, value):
    path = Path(path)
    temp = path.with_suffix('.tmp')
    temp.write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')
    temp.replace(path)


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


def checked_raw(path, record):
    raw = path.parent/record['raw_return']['file']
    if sha(raw) != record['raw_return']['sha256']:
        raise ValueError('Actual accepted raw bytes changed')
    with np.load(raw, allow_pickle=False) as saved:
        values = {key: saved[key].copy() for key in saved.files}
    if np.any(values['p'] != 0):
        raise ValueError('Only the actual zero-control anchor may be diagnosed')
    return raw, values


def anchors(repo, source_path):
    current = repo/'topics/visible-flex-held-10pct/scripts/resume_20261126'
    sys.path.insert(0, str(current))
    new_model = module('_probe_columns_validator_v3', current/'warm_fixed_m3_model_v3.py')
    newer = new_model.accepted_input(source_path)
    if (newer['homotopy'] != .002 or newer['warm_definition']['homotopy'] != .002
            or newer['acceptance_kind'] != 'same_cartesian_map_verified_reexpression'
            or newer['solver_invoked'] is not False or newer['mean_nodes'] != 1168):
        raise ValueError('Require the actual accepted lambda=.002 v3 zero-control reexpression')
    old_path = Path(newer['basis_anchor_v2_run']).resolve()
    old_model = module('_probe_columns_validator_v2', current/'warm_fixed_m3_model_v2.py')
    older = old_model.accepted_input(old_path)
    if sha(old_path) != newer['basis_anchor_v2_sha256']:
        raise ValueError('The accepted v2 source bytes changed')
    if (older['homotopy'] != .002 or older['mean_nodes'] != 1168
            or older['modes'] != newer['modes'] or older['angular'] != newer['angular']):
        raise ValueError('The actual anchor dimensions/lambda/mean differ')
    for key in ('frozen_profile', 'physical_tail_parameters', 'physical_tail_cut',
                'angular_chart', 'gauge_q', 'warp_reference', 'frozen_radial_chart',
                'bc_normalization', 'origin_design_run', 'origin_design_sha256'):
        if older[key] != newer[key]:
            raise ValueError('The common physical problem changed: '+key)
    old_raw, a = checked_raw(old_path, older)
    new_raw, b = checked_raw(source_path, newer)
    for key in ('x', 'y', 'p', 'pscale', 'rms'):
        if not np.array_equal(a[key], b[key]):
            raise ValueError('The actual zero-control raw fields differ: '+key)
    return current, {'v2': (old_path, older, old_raw),
                     'v3': (source_path, newer, new_raw)}, b


def spectrum(matrix):
    matrix = np.asarray(matrix, dtype=float)
    if matrix.ndim != 2 or not np.all(np.isfinite(matrix)):
        raise FloatingPointError('Nonfinite/invalid actual diagnostic matrix')
    values = np.linalg.svd(matrix, compute_uv=False)
    top = float(values[0]) if len(values) else 0.
    bottom = float(values[-1]) if len(values) else 0.
    threshold = np.finfo(float).eps*max(matrix.shape, default=1)*top
    near_floor = bool(bottom <= threshold)
    ratio = top/bottom if bottom > 0 else None
    if ratio is not None and not math.isfinite(ratio):
        ratio = None
    return dict(shape=list(matrix.shape), singular_values=values.tolist(),
        column_l2=np.linalg.norm(matrix, axis=0).tolist(),
        column_max_abs=np.max(abs(matrix), axis=0).tolist(),
        numerical_rank=int(np.count_nonzero(values > threshold)),
        floating_rank_threshold=threshold, smallest_near_roundoff_floor=near_floor,
        condition_estimate=ratio, certified_positive_lower_bound=False,
        warning='Binary64 finite-matrix diagnostic; bottom singular values near the floor are not strict bounds')


def jet_matrix(values):
    values = np.asarray(values)
    # Each parameter column uses the actual uniform-material-angle average.
    return values.transpose(1, 2, 0).reshape(-1, values.shape[0])/math.sqrt(values.shape[1])


def gap(a, b):
    a, b = np.asarray(a), np.asarray(b)
    if not np.all(np.isfinite(a)) or not np.all(np.isfinite(b)):
        raise FloatingPointError('Nonfinite derivative comparison')
    error = float(np.max(abs(a-b)))
    scale = float(np.max(abs(a)))
    return dict(max_abs_error=error, max_abs_analytic=scale,
                relative_max_error=error/scale if scale > 0 else None,
                bitwise_equal=bool(np.array_equal(a, b)))


def compact_spectrum(value):
    singular = value['singular_values']
    return {key: value[key] for key in ('shape', 'numerical_rank',
        'floating_rank_threshold', 'smallest_near_roundoff_floor', 'condition_estimate')} | {
        'largest_singular_value': singular[0], 'smallest_singular_value': singular[-1],
        'certified_positive_lower_bound': False}


def compact_family(value):
    result = {key: value[key] for key in ('family', 'source_run', 'source_run_sha256',
        'raw_sha256', 'physical_sha256', 'modes', 'angular', 'homotopy',
        'frozen_mean_nodes', 'numerical_gauge', 'parameter_contract',
        'local_arrays', 'Newton_rejection_classification',
        'diagnostic_auxiliary_domain_guard') if key in value}
    if 'inlet' in value:
        inlet = value['inlet']
        result['inlet'] = {key: compact_spectrum(inlet[key]) for key in
            ('physical_coefficient_columns', 'full_C2_discrete_L2_stack',
             'represented_C2_discrete_L2_stack')}
        result['inlet']['exact_lift_retained'] = True
        result['inlet']['analytic_vs_literal_reprojection'] = inlet['analytic_vs_literal_reprojection']
        for block in ('full_core', 'represented_fourier', 'exact_lift_remainder'):
            result['inlet'][block] = {key: compact_spectrum(item) for key, item in inlet[block].items()}
    if 'actual_fixed_field_columns' in value:
        columns = value['actual_fixed_field_columns']
        result['actual_fixed_field_columns'] = {key: compact_spectrum(columns[key]) for key in
            ('combined_physical_rhs_samples', 'physical_BC_parameter_columns',
             'physical_terminal_BC_direct_parameter_columns', 'physical_terminal_BC_state_columns')}
        result['actual_fixed_field_columns']['raw_indices'] = columns['raw_indices']
    if 'selected_centered_FD_checks' in value:
        result['selected_centered_FD_checks'] = value['selected_centered_FD_checks']
    return result


def run_family(args, output, event):
    current, sources, raw = anchors(args.repo, args.source_run)
    source_path, record, raw_path = sources[args.family]
    model = module('_probe_columns_active_'+args.family,
                   current/('warm_fixed_m3_model_'+args.family+'.py'))
    design, origin, signature, _ = model.bootstrap(record['origin_design_run'])
    if signature != record['frozen_source_signature']:
        raise ValueError('The accepted numerical source signature changed')
    obj = model.build_model(design, origin, record)
    x, y, p = (raw[key] for key in ('x', 'y', 'p'))
    initial = obj.initial(p).copy()
    core, flow = obj._core, obj.flow(p[0])
    if (not obj.fixed or np.any(core.controls != 0) or not core._zero
            or not np.array_equal(raw['pscale'], obj.pscale)):
        raise ValueError('The reconstructed actual zero-control phase contract differs')
    if obj.q != record['gauge_q'] or record['mean_nodes'] != 1168:
        raise ValueError('The actual gauge or frozen mean changed')
    scale = float(record['warm_definition']['phase_control_scale'])
    lower, upper = math.log(1e-7/obj.q), math.log(.124/obj.q)
    output['result'].update(family=args.family, source_run=str(source_path),
        source_run_sha256=sha(source_path), raw_path=str(raw_path), raw_sha256=sha(raw_path),
        physical_sha256=record['physical_sha256'], modes=obj.M, angular=obj.nt,
        homotopy=record['homotopy'], frozen_mean_nodes=1168,
        numerical_gauge=obj.q, frozen_radial_chart=record['frozen_radial_chart'],
        parameter_contract=dict(d_equals_phase_scale_times_p=True, phase_scale=scale,
            p0_is_a_real_first_phase_control=True, q_aux_is_not_the_Y_gauge=True,
            original_open_q_aux_domain=[1e-7, .124],
            p0_open_domain_numeric=[lower, upper],
            d1_open_domain_numeric=[scale*lower, scale*upper],
            q_aux_at_anchor=float(obj.support_amplitude),
            d1_at_anchor=float(core.controls[0]), domain_removed=False),
        frozen_bindings={key: record[key] for key in model.CONTRACT_KEYS},
        provider_bindings=model.provider_bindings())
    # This is the source's actual WarpedBVP inlet projection grid. The
    # authentic _initial_jac below is retained independently of this check.
    N = max(2048, 128*obj.M)
    angular = flow.angular(N)
    bases = flow.basis(N)
    chain = np.r_[obj.support_amplitude, obj.pscale]
    derivatives = core.jet_parameter_derivatives(angular[1])
    full = [derivatives[0], derivatives[1]*angular[2][None, :, None],
            derivatives[2]*angular[2][None, :, None]**2
            + derivatives[1]*angular[3][None, :, None]]
    full = [values*chain[:, None, None] for values in full]
    inlet_jac = obj._initial_jac.copy()
    represented = [flow.values(obj.q*inlet_jac, basis) for basis in bases]
    remainder = [a-b for a, b in zip(full, represented)]
    physical_projection = flow.project(full[0], bases[0])
    output['result']['inlet'] = dict(actual_projection_nodes=N,
        physical_coefficient_columns=spectrum(obj.q*inlet_jac),
        analytic_vs_literal_reprojection=gap(obj.q*inlet_jac, physical_projection),
        full_core={name: spectrum(jet_matrix(value)) for name, value in
                   zip(('position', 'first', 'second'), full)},
        represented_fourier={name: spectrum(jet_matrix(value)) for name, value in
                             zip(('position', 'first', 'second'), represented)},
        exact_lift_remainder={name: spectrum(jet_matrix(value)) for name, value in
                             zip(('position', 'first', 'second'), remainder)},
        full_C2_discrete_L2_stack=spectrum(np.vstack([jet_matrix(v) for v in full])),
        represented_C2_discrete_L2_stack=spectrum(np.vstack([jet_matrix(v) for v in represented])),
        exact_lift_retained=True,
        scope='Only the correction is Fourier represented; all three remainder jets remain in the original a*chi exact core lift. The inlet projection alone is not the full BVP parameter map.')
    event('actual_inlet_parameter_columns_measured', family=args.family, nodes=N)
    physical_s = obj.chart(x, p[0])[0]
    target_s = np.r_[0., .25*flow.prefix_end, .5*flow.prefix_end,
                     .7*flow.prefix_end, .9*flow.prefix_end, flow.prefix_end, flow.end]
    indices = np.unique([int(np.argmin(abs(physical_s-value))) for value in target_s])
    xt, yt = x[indices], y[:, indices]
    _, rhs_parameters = obj.fun_jac(xt, yt, p)
    _, ds = obj.chart(xt, p[0])
    physical_rhs = obj.q*rhs_parameters/ds[None, None, :]
    A, B, P = obj.bc_jac(y[:, 0], y[:, -1], p)
    physical_P = P.copy()
    physical_P[:obj.n] *= obj.q
    physical_P[obj.n:] *= obj.bcweights[:, None]
    physical_B = B[obj.n:]*obj.bcweights[:, None]
    bc_value = obj.bc(y[:, 0], y[:, -1], p)
    output['result']['actual_fixed_field_columns'] = dict(
        raw_indices=indices.tolist(), physical_s=physical_s[indices].tolist(),
        physical_rhs=[dict(raw_index=int(i), physical_s=float(physical_s[i]),
                           **spectrum(physical_rhs[:, :, k])) for k, i in enumerate(indices)],
        combined_physical_rhs_samples=spectrum(physical_rhs.transpose(0, 2, 1).reshape(-1, obj.M)),
        physical_BC_parameter_columns=spectrum(physical_P),
        physical_inlet_BC_parameter_columns=spectrum(physical_P[:obj.n]),
        physical_terminal_BC_direct_parameter_columns=spectrum(physical_P[obj.n:]),
        physical_terminal_BC_state_columns=spectrum(physical_B),
        original_scaled_BC_max=float(np.max(abs(bc_value))),
        physical_terminal_BC_max=float(np.max(abs(bc_value[obj.n:]*obj.bcweights))),
        exact_lift_window=[.5, .9],
        terminal_scope='At fixed terminal state the original exact lift vanishes. A zero direct terminal parameter block does not imply a zero parameter effect through the interior ODE. No sensitivity equation or BVP inverse is solved.')
    event('actual_rhs_and_BC_parameter_columns_measured', family=args.family, raw_points=len(indices))
    fd_results = []
    columns = sorted(set(j for j in (0, 1, obj.M//2, obj.M-1) if 0 <= j < obj.M))
    for j in columns:
        for step in (1e-5, 2e-6):
            plus, minus = p.copy(), p.copy()
            plus[j] += step
            minus[j] -= step
            ip, im = obj.initial(plus).copy(), obj.initial(minus).copy()
            rp, rm = obj.fun(xt, yt, plus), obj.fun(xt, yt, minus)
            bp = obj.bc(y[:, 0], y[:, -1], plus)
            bm = obj.bc(y[:, 0], y[:, -1], minus)
            db = (bp-bm)/(2*step)
            db[:obj.n] *= obj.q
            db[obj.n:] *= obj.bcweights
            fd_results.append(dict(column=j, step=step,
                inlet=gap(obj.q*inlet_jac[:, j], obj.q*(ip-im)/(2*step)),
                physical_rhs=gap(physical_rhs[:, j, :], obj.q*(rp-rm)/(2*step)/ds[None, :]),
                physical_BC=gap(physical_P[:, j], db)))
        obj.initial(p)
        event('actual_selected_parameter_column_FD_checked', family=args.family, column=j)
    output['result']['selected_centered_FD_checks'] = fd_results
    output['result']['diagnostic_auxiliary_domain_guard'] = copy.deepcopy(obj.auxiliary_domain_guard)
    output['result']['Newton_rejection_classification'] = dict(
        newton_invoked=False, trial_failures_observed=0,
        actual_running_Newton_stats_not_observed_by_this_probe=True,
        categories=['auxiliary exponential precheck', 'original q_aux open interval',
                    'original core curvature positivity', 'original Frenet domain'],
        scope='These domain categories are distinct; projection singular values are not a domain rejection. No gate is removed or widened.')
    arrays = dict(initial=initial, physical_inlet_parameters=obj.q*inlet_jac,
        full_core_position=full[0], full_core_first=full[1], full_core_second=full[2],
        physical_rhs_parameters=physical_rhs, physical_BC_parameters=physical_P,
        physical_terminal_state_columns=physical_B, raw_indices=indices, physical_s=physical_s[indices])
    array_path = args.outdir/'actual-column-arrays.npz'
    np.savez_compressed(array_path, **arrays)
    output['result']['local_arrays'] = dict(path=str(array_path), sha256=sha(array_path))
    output['status'] = 'read_only_actual_parameter_columns_complete'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--source-run', type=Path, required=True)
    parser.add_argument('--outdir', type=Path, required=True)
    parser.add_argument('--family', choices=('v2', 'v3'), help=argparse.SUPPRESS)
    args = parser.parse_args()
    args.repo, args.source_run, args.outdir = (p.resolve() for p in
                                            (args.repo, args.source_run, args.outdir))
    if args.outdir == args.repo or args.repo in args.outdir.parents:
        raise ValueError('Actual arrays must remain outside the repository')
    args.outdir.mkdir(parents=True, exist_ok=False)
    start = time.monotonic()
    output = dict(status='preparing', scope=__doc__, source_hashes={str(Path(__file__).resolve()): sha(__file__)},
        stages=[], results=[], progress={}, result={}, error=None,
        BVP_invoked=False, DN_invoked=False, BVP_inverse_measured=False,
        finite_acceptance_changed=False, complete_surface=False)
    def save():
        output['elapsed'] = time.monotonic()-start
        report = args.outdir/'probe.json'
        write(report, output)
        summary = {key: output[key] for key in ('status', 'error', 'progress',
            'stages', 'elapsed', 'source_hashes', 'BVP_invoked', 'DN_invoked',
            'BVP_inverse_measured', 'finite_acceptance_changed', 'complete_surface')}
        summary['result'] = compact_family(output['result']) if args.family else copy.deepcopy(output['result'])
        summary['results'] = [dict(family=item['family'], result=compact_family(item['result']))
                              for item in output['results']]
        summary['result']['full_diagnostic'] = dict(path=str(report), sha256=sha(report))
        if output.get('exception'):
            summary['exception'] = output['exception']
        write(args.outdir/'summary.json', summary)
    def event(name, **details):
        output['progress'] = dict(event=name, **details)
        save()
        print(json.dumps(dict(event=name, elapsed=time.monotonic()-start, **details)), flush=True)
    try:
        if args.family:
            run_family(args, output, event)
        else:
            current, sources, _ = anchors(args.repo, args.source_run)
            output['result']['source_identity'] = {key: dict(run=str(value[0]), run_sha256=sha(value[0]),
                raw=str(value[2]), raw_sha256=sha(value[2])) for key, value in sources.items()}
            output['result']['identical_actual_zero_control_raw_fields'] = True
            for family in ('v2', 'v3'):
                folder = args.outdir/family
                command = [sys.executable, '-u', str(Path(__file__).resolve()), '--repo', str(args.repo),
                    '--source-run', str(args.source_run), '--outdir', str(folder), '--family', family]
                event('starting_isolated_read_only_family', family=family)
                with (args.outdir/(family+'.log')).open('x') as stream:
                    child = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT)
                    while child.poll() is None:
                        time.sleep(15)
                        try:
                            latest = read(folder/'summary.json')
                            output['progress'] = dict(event='isolated_family_running', family=family,
                                actual_status=latest['status'], actual_progress=latest['progress'])
                            save()
                        except (OSError, ValueError):
                            pass
                value = read(folder/'probe.json')
                output['stages'].append(dict(family=family, returncode=child.returncode,
                    report=str(folder/'probe.json'), sha256=sha(folder/'probe.json'), status=value['status']))
                if child.returncode or value['status'] != 'read_only_actual_parameter_columns_complete':
                    raise ValueError('Actual '+family+' diagnostic failed: '+str(value.get('error')))
                output['results'].append(dict(family=family, result=value['result']))
                event('isolated_read_only_family_finished', family=family)
            left, right = (read(args.outdir/f/'probe.json')['result'] for f in ('v2', 'v3'))
            with np.load(left['local_arrays']['path'], allow_pickle=False) as a, np.load(right['local_arrays']['path'], allow_pickle=False) as b:
                output['result']['shared_anchor_checks'] = {key: gap(a[key], b[key]) for key in
                    ('initial', 'physical_terminal_state_columns', 'raw_indices', 'physical_s')}
            output['result']['scope_limit'] = ('Actual fixed-field parameter columns at the accepted lambda=.002 anchor; complete exact core lift retained. No collocation inverse, continuation result, residual pass, or existence/nonexistence conclusion follows from these singular values.')
            output['status'] = 'read_only_actual_anchor_projection_comparison_complete'
        save()
        return 0
    except Exception as error:
        output.update(status='error', error=repr(error), exception=traceback.format_exc()[-8000:])
        save()
        print(json.dumps(dict(event='error', error=repr(error))), flush=True)
        return 2


if __name__ == '__main__':
    sys.exit(main())
