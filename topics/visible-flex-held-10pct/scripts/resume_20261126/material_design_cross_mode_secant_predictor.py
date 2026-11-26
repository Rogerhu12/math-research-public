#!/usr/bin/env python3
"""Unaccepted original-R53 secant using a complete lower-M reference lift.

Both sources must be real accepted original portable linear-DN design returns.
Only the left field is embedded to the right M. Its own lambda, additive delta,
complete support core and computational radial chart define that lift. The
right saved cubic is evaluated on the union grid, or its own grid if the union
exceeds its original node budget. No solver, DN, accepted reexpression, cubic
refit or physical export is produced. Run in a fresh process: the original
read-only geometry loader installs source classes globally.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import argparse
import copy
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import traceback

import numpy as np
from scipy.interpolate import PPoly


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


def write(path, value):
    temporary = path.with_suffix(path.suffix+'.tmp')
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')
    temporary.replace(path)


def array_identity(value):
    value = np.ascontiguousarray(value)
    return dict(shape=list(value.shape), dtype=value.dtype.str,
                sha256=hashlib.sha256(value.tobytes()).hexdigest())


def same_physical_design(left, right, option):
    """The only numerical resolution differences here are explicit, not hidden."""
    for key in ('physical_profile', 'physical_tail_parameters', 'physical_tail_cut',
                'angular_chart', 'gauge_q', 'warp_reference', 'source_hashes', 'gates'):
        if left[key] != right[key]:
            raise ValueError('The original physical/design contract differs: '+key)
    for flag in ('--source-topic', '--short-bridge', '--profile', '--chart',
                 '--core-module', '--audit-angular'):
        if option(left, flag) != option(right, flag):
            raise ValueError('The original command definitions differ: '+flag)
    for flag in ('--profile', '--chart', '--core-module'):
        filename = str(Path(option(left, flag)).resolve())
        if left['inputs'][filename] != right['inputs'][filename]:
            raise ValueError('The actual source input bytes differ: '+flag)
    settings = [{key: value for key, value in rec['core_settings'].items()
                 if key != 'homotopy'} for rec in (left, right)]
    if settings[0] != settings[1]:
        raise ValueError('Only lambda may differ in the original R53 core settings')
    if not 0 < int(left['modes']) < int(right['modes']):
        raise ValueError('This entry requires a genuinely lower-M accepted left source')
    if int(right['angular']) < int(left['angular']):
        raise ValueError('The right source must not lower the original angular resolution')


def saved_cubic(raw):
    pp = PPoly.construct_fast(raw['cubic_c'], raw['cubic_x'],
                              axis=1, extrapolate=False)
    values = pp(raw['x'])
    error = float(np.max(np.abs(values-raw['y'])))
    allowance = 32*np.finfo(float).eps*max(1., float(np.max(np.abs(raw['y']))))
    if not np.all(np.isfinite(values)) or error > allowance:
        raise ValueError('An actual saved cubic does not reproduce its own raw nodes')
    return pp, error


def evaluate_lifted_left(pp, t, old, new, old_p, new_p, difference, lift):
    """Evaluate the original full lift directly; never fit a new left cubic."""
    s, ds = old.chart(t, old_p[0])
    new_s, new_ds = new.chart(t, new_p[0])
    if not np.array_equal(s, new_s) or not np.array_equal(ds, new_ds):
        raise ValueError('The left mode embedding changed its literal radial chart')
    weight = lift.lift_weights(new.flow(new_p[0]), s)[0]
    result = lift.embed(pp(t), old.M, new.M)+weight[None, :]*difference[:, None]
    if not np.all(np.isfinite(result)):
        raise FloatingPointError('The full left lift is nonfinite')
    return result


def reference_geometry_check(old, new, old_p, new_p, source_t, physical_path, difference, lift):
    """The original transfer's finite six-jet check, using its original 1e-7 gate."""
    with np.load(physical_path, allow_pickle=False) as saved:
        if not np.array_equal(saved['p'], old_p):
            raise ValueError('The left physical parameters differ from its actual raw')
        pp = PPoly.construct_fast(saved['c'].copy(), saved['x'].copy(),
                                  axis=1, extrapolate=False)
    f0, f1 = old.flow(old_p[0]), new.flow(new_p[0])
    # These are reference checks, not a new accepted collocation field or
    # continuous C2 certificate. The same literal left mean would be shared.
    source_s = old.chart(source_t, old_p[0])[0]
    sample = np.unique(np.r_[np.linspace(0, f0.end, 65),
        f0.prefix_end*np.array([.5, .6, .7, .8, .9]),
        source_s[::max(1, len(source_s)//32)]])
    N = max(2048, 32*(3*new.M+1))
    B0, D0, DD0 = f0.basis(N)
    B1, D1, DD1 = f1.basis(N)
    checks = {name: 0. for name in
              ('position', 'psi', 'psi_psi', 's', 's_psi', 's_s', 'rho')}
    for start in range(0, len(sample), 16):
        z = sample[start:start+16]
        v0, u0, uu0 = pp(z), pp(z, 1), pp(z, 2)
        w, w1, w2 = lift.lift_weights(f1, z)
        values = [lift.embed(value, old.M, new.M)+weight[None, :]*difference[:, None]
                  for value, weight in ((v0, w), (u0, w1), (uu0, w2))]
        v1, u1, uu1 = values
        g0, g1 = f0.geo(z, N), f1.geo(z, N)
        radius_gap = g0['rho']-g1['rho']
        if not np.all(np.isfinite(radius_gap)):
            raise FloatingPointError('Nonfinite original reference-radius check')
        checks['rho'] = max(checks['rho'], float(np.max(abs(radius_gap))))
        for name, key, a, b, ba, bb in (
                ('position', 'pos', v0, v1, B0, B1),
                ('psi', 'p1', v0, v1, D0, D1),
                ('psi_psi', 'p2', v0, v1, DD0, DD1),
                ('s', 's1', u0, u1, B0, B1),
                ('s_psi', 'sp', u0, u1, D0, D1),
                ('s_s', 's2', uu0, uu1, B0, B1)):
            delta = g1[key]+new.q*f1.values(b, bb)-g0[key]-old.q*f0.values(a, ba)
            if not np.all(np.isfinite(delta)):
                raise FloatingPointError('Nonfinite original reference-jet check: '+name)
            checks[name] = max(checks[name],
                float(np.max(np.linalg.norm(delta, axis=2))))
    if not all(math.isfinite(value) and value <= 1e-7 for value in checks.values()):
        raise FloatingPointError('The original finite reference lift check failed: '+str(checks))
    return dict(reference_two_jet_checks=checks, check_s=len(sample), check_angular=N,
                threshold=1e-7, meridian_two_jets_checked=True,
                reported_jets_scope='The reported raw reference jets omit the common mean-height term, as in the original transfer',
                common_mean_height_scope='Keeping the same literal left frame, mean rule and primitive origin is a common-reference reconstruction condition; no new mean integral is evaluated here',
                mean_height_integral_evaluated=False,
                full_cartesian_error_certified=False,
                continuous_certificate=False, accepted_bvp=False)


def predict(repo, left_path, right_path, target, outdir):
    target = float(target)
    if not math.isfinite(target) or not 0 < target <= 1:
        raise ValueError('A finite target lambda in (0,1] is required')
    repo = Path(repo).resolve()
    left_path, right_path, out = map(lambda value: Path(value).resolve(),
                                     (left_path, right_path, outdir))
    if out == repo or repo in out.parents:
        raise ValueError('Generated arrays must remain outside the repository')
    out.mkdir(parents=True, exist_ok=False)
    scripts = repo/'topics/visible-flex-held-10pct/scripts'
    current = scripts/'resume_20261126'
    resume = scripts/'resume_m3'
    state = dict(scope=__doc__, status='preparing',
        record_kind='unaccepted_cross_mode_nodal_initializer',
        accepted_bvp=False, initializer_is_accepted_solution=False,
        solver_invoked=False, solver_success=None,
        physical_metric_gate_paid=False, physical_boundary_gate_paid=False,
        domain_gate_paid=False, true_tail_paid=False, fixed_metric_refinement=False,
        complete_surface=False, target_lambda=target,
        source_hashes={str(Path(__file__).resolve()): digest(__file__)})
    path = out/'predictor.json'
    try:
        helper_files = {
            'accepted': current/'material_design_secant_predictor.py',
            'geometry': resume/'actual_m3_metric_model.py',
            'lift': resume/'prepare_lifted_mode_restart.py'}
        for filename in (*helper_files.values(), current/'material_design_continue.py',
                         resume/'round_raw_lib/exact_core_lift.py',
                         resume/'round_raw_lib/analytic_adaptive_core_jac.py',
                         scripts/'resume_transfer/material_flattened_support_core.py'):
            state['source_hashes'][str(filename)] = digest(filename)
        api = module('_cross_mode_actual_sources', helper_files['accepted'])
        left, lraw = api.accepted_original(left_path, repo)
        right, rraw = api.accepted_original(right_path, repo)
        same_physical_design(left, right, api.option)
        ll, lr = [float(rec['core_settings']['homotopy']) for rec in (left, right)]
        if not (math.isfinite(target) and 0 < ll < lr < target <= 1):
            raise ValueError('Require increasing actual accepted lambdas and a later target <= 1')
        left_pp, left_nodal_error = saved_cubic(lraw)
        right_pp, right_nodal_error = saved_cubic(rraw)
        x = np.unique(np.r_[lraw['x'], rraw['x']])
        union_nodes, right_nodes = len(x), len(rraw['x'])
        max_nodes = right['gates']['max_nodes']
        if (not isinstance(max_nodes, int) or isinstance(max_nodes, bool)
                or max_nodes < right_nodes):
            raise ValueError('The actual right grid exceeds its declared original node budget')
        grid_rule = 'actual_grid_union'
        if union_nodes > max_nodes:
            x = rraw['x'].copy()
            grid_rule = 'right_original_grid_budget_fallback'

        geometry = module('_cross_mode_original_geometry', helper_files['geometry'])
        lift = module('_cross_mode_original_lift', helper_files['lift'])
        old = geometry.load_model(dict(source_run=str(left_path)))
        if old.fixed or old.M != left['modes'] or not np.array_equal(old.pscale, lraw['pscale']):
            raise ValueError('The left original design coordinates or parameter scales changed')
        old_p = lraw['p']
        old_initial = old.initial(old_p).copy()
        old_core = old._core
        if not hasattr(old_core, 'original') or old_core.homotopy != ll:
            raise ValueError('The left complete positive-lambda R53 core changed')
        port_path = Path(api.option(right, '--port')).resolve()
        port = json.loads(port_path.read_text())
        port['cut']['_prefix_bridge'] = left['physical_profile']['prefix_bridge']
        port['_sha256'] = digest(port_path)
        if (port['parameters'] != left['physical_tail_parameters']
                or port['cut'] != left['physical_tail_cut']):
            raise ValueError('The larger right port changed the left physical tail geometry')
        new = type(old)(copy.deepcopy(old.cfg), port, old.q, int(right['modes']),
                        int(right['angular']), False, float(left['warp_reference']))
        new.bcweights = np.full(new.M,
            left['gates']['physical_bc_tol']/left['gates']['bc_tol'])
        if not np.array_equal(new.pscale, rraw['pscale']):
            raise ValueError('The actual right scales differ from the original larger-M constructor')
        new_p = np.zeros(new.M)
        new_p[0] = old_p[0]
        new_p[1:old.M] = old_p[1:]*old.pscale/new.pscale[:old.M-1]
        new_initial = new.initial(new_p).copy()
        difference = new_initial-lift.embed(old_initial, old.M, new.M)
        for key in ('chart_join', 'chart_reference_prefix', 'chart_breaks'):
            if not np.array_equal(np.asarray(getattr(old, key)), np.asarray(getattr(new, key))):
                raise ValueError('The left literal radial chart changed at larger M: '+key)
        if new.flow(new_p[0]).end != old.flow(old_p[0]).end:
            raise ValueError('The left physical meridian range changed')
        physical_old = np.asarray(old_core.original.coefficients)
        physical_new = np.asarray(new._core.original.coefficients)
        if physical_old.shape != (old.M,) or physical_new.shape != (new.M,):
            raise ValueError('The complete original support coefficient layout changed')
        if not all(np.all(np.isfinite(value)) for value in
                   (new_p, difference, physical_old, physical_new)):
            raise FloatingPointError('Nonfinite larger-M support coordinates or inlet projection')
        control_gap = physical_new[:old.M]-physical_old
        added = physical_new[old.M:]
        if not np.all(added == 0.):
            raise ValueError('The larger left support core did not zero-extend its new coefficients')
        state['left_lift'] = dict(
            source_run=str(left_path), source_run_sha256=digest(left_path),
            source_raw_sha256=left['raw_return']['sha256'],
            source_physical_sha256=left['physical_sha256'],
            old_modes=old.M, new_modes=new.M, old_angular=old.nt, new_angular=new.nt,
            exact_lift_coefficient=1, left_homotopy=ll,
            preserved_additive_delta=float(new_p[0]),
            actual_delta=left['frozen_profile']['delta'],
            mean_nodes=left['prefix_audit']['samples_psi'],
            larger_port=str(port_path), larger_port_sha256=digest(port_path),
            complete_support_old=array_identity(physical_old),
            complete_support_embedded=array_identity(physical_new),
            original_support_scales=array_identity(old.pscale),
            target_support_scales=array_identity(new.pscale),
            actual_common_support_bitwise_equal=bool(np.array_equal(physical_new[:old.M], physical_old)),
            actual_common_support_roundtrip_l1=float(np.sum(abs(control_gap))),
            actual_common_support_roundtrip_linf=float(np.max(abs(control_gap))),
            added_support_coefficients_zero=True,
            roundtrip_exact_equality_is_an_acceptance_gate=False,
            projection_difference=array_identity(difference),
            inlet_projection_change_max=float(np.max(abs(difference))),
            accepted_bvp=False, metric_gate_paid=False,
            stored_representation='No new cubic, physical interpolant or accepted run is constructed')
        state['left_lift']['reference_check'] = reference_geometry_check(
            old, new, old_p, new_p, lraw['x'], left_path.parent/'physical.npz', difference, lift)
        left_values = evaluate_lifted_left(
            left_pp, x, old, new, old_p, new_p, difference, lift)
        right_values = right_pp(x)
        beta = (target-lr)/(lr-ll)
        y = right_values+beta*(right_values-left_values)
        p = rraw['p']+beta*(rraw['p']-new_p)
        if not np.all(np.isfinite(y)) or not np.all(np.isfinite(p)):
            raise FloatingPointError('The unaccepted cross-M secant is nonfinite')
        destination = out/'initial.npz'
        np.savez_compressed(destination, x=x, y=y, p=p, pscale=rraw['pscale'])

        def provenance(filename, rec):
            return dict(run=str(filename), run_sha256=digest(filename),
                homotopy=rec['core_settings']['homotopy'], modes=rec['modes'],
                angular=rec['angular'], actual_delta=rec['frozen_profile']['delta'],
                mean_nodes=rec['prefix_audit']['samples_psi'],
                raw_sha256=rec['raw_return']['sha256'],
                physical_sha256=rec['physical_sha256'], nodes=rec['raw_return']['nodes'],
                rms=rec['raw_return']['rms'], metric=rec['prefix_audit']['metric_l1'],
                physical_bc=rec['prefix_audit']['physical_bc_max'])
        state.update(status='unaccepted_cross_mode_secant_initializer_ready',
            left=provenance(left_path, left), right=provenance(right_path, right),
            modes=right['modes'], angular=right['angular'], nodes=len(x),
            secant_beta=beta, grid_rule=grid_rule, union_nodes=union_nodes,
            right_nodes=right_nodes, max_nodes=max_nodes,
            gauge_q=right['gauge_q'], warp_reference=right['warp_reference'],
            target_original_mean_nodes=right['prefix_audit']['samples_psi'],
            source_mean_rules_equal=bool(left['prefix_audit']['samples_psi'] ==
                                         right['prefix_audit']['samples_psi']),
            mean_scope='Both actual source means remain their original definitions. This is design-state extrapolation; the target mean must be reconstructed and audited from the new target field.',
            coordinate='Common computational t; left original cubic plus its own complete physical lift, right original cubic',
            parameter_zero_meaning='additive delta increment',
            remaining_parameters='Original normal-angle support coordinates in the actual right pscale; not phase controls',
            predicted_delta=right['physical_profile']['delta']+float(p[0]),
            source_nodal_evaluation_roundoff=dict(left=left_nodal_error, right=right_nodal_error),
            max_state_increment_from_right=float(np.max(abs(y-right_values))),
            max_parameter_increment_from_right=float(np.max(abs(p-rraw['p']))),
            result=dict(initial_raw=str(destination), initial_raw_sha256=digest(destination)),
            acceptance_required='Original portable initial-domain, actual BVP/RMS, physical BC and full metric gates, all recomputed')
        write(path, state)
        return state
    except Exception as error:
        state.update(status='cross_mode_predictor_error', error=repr(error),
                     traceback=traceback.format_exc())
        write(path, state)
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'left-run', 'right-run', 'outdir'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--target-lambda', type=float, required=True)
    args = parser.parse_args()
    value = predict(args.repo, args.left_run, args.right_run, args.target_lambda, args.outdir)
    print(json.dumps({key: value[key] for key in
        ('status', 'modes', 'nodes', 'target_lambda', 'secant_beta', 'grid_rule', 'result')},
        allow_nan=False))


if __name__ == '__main__':
    main()
