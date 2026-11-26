#!/usr/bin/env python3
"""Unaccepted full-state secant initializer for the original R53 delta design.

Two actual accepted original linear-DN fields at the same M are evaluated with
their saved computational-t cubic PPoly on a common actual grid: the union when
it fits the original node budget, otherwise the right field's original grid.
Original p[0] is an ADDITIVE delta increment; the other original support
coordinates retain their identical pscale. No geometry, boundary, metric or
solver acceptance is assigned to the extrapolated nodal data.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import sys


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def option(record, flag):
    command = record['command']
    if command.count(flag) != 1:
        raise ValueError('Expected one original command option: '+flag)
    return command[command.index(flag)+1]


def accepted_original(path, repo):
    """Validate a real portable design return; this never accepts a predictor."""
    import numpy as np
    path, repo = Path(path).resolve(), Path(repo).resolve()
    scripts = repo/'topics/visible-flex-held-10pct/scripts'
    sys.path.insert(0, str(scripts/'resume_20261126'))
    from material_design_continue import original_finite_checks, complete_initializer
    record = read(path)
    if (record.get('model_kind') is not None or record.get('fixed_metric') or
            record.get('fixed_metric_refinement') or record.get('actual_tail_requested') or
            record.get('original_actual_nonlinear_tail') or
            not original_finite_checks(record)['solver_and_boundary_pass'] or
            not complete_initializer(path, record)):
        raise ValueError('Require an actual accepted original portable design return')
    metric = record.get('prefix_audit', {}).get('metric_l1')
    if (not isinstance(metric, (int, float)) or isinstance(metric, bool)
            or not math.isfinite(metric) or not 0 <= metric <= 1e-6):
        raise ValueError('Source did not pass its original full metric gate')
    for group in ('source_hashes', 'inputs'):
        if not isinstance(record.get(group), dict) or not record[group]:
            raise ValueError('Missing actual source/input provenance')
        for filename, expected in record[group].items():
            if digest(filename) != expected:
                raise ValueError('Changed recorded source or input: '+filename)
    portable = (scripts/'resume_m3/portable_prefix_continue.py').resolve()
    provider = (scripts/'resume_m3/material_support_factory.py').resolve()
    if (Path(record['command'][1]).resolve() != portable
            or record['source_hashes'].get(str(portable)) != digest(portable)
            or Path(option(record, '--core-module')).resolve() != provider
            or record['inputs'].get(str(provider)) != digest(provider)):
        raise ValueError('The source is not the declared original R53 portable provider')
    if any(flag in record['command'] for flag in
           ('--tail-config', '--skip-audit', '--probe-only')):
        raise ValueError('Only the actually audited original linear-DN design is allowed')
    settings = read(option(record, '--core-config'))
    lam = settings.get('homotopy')
    if (settings != record['core_settings'] or not isinstance(lam, (int, float))
            or isinstance(lam, bool) or not math.isfinite(lam) or not 0 < lam <= 1):
        raise ValueError('Expected a positive original material homotopy')
    profile = read(option(record, '--profile'))
    chart = read(option(record, '--chart'))
    port = read(option(record, '--port'))
    cut = dict(port['cut'], _prefix_bridge=profile['prefix_bridge'])
    if (profile != record['physical_profile'] or chart != record['angular_chart']
            or port['parameters'] != record['physical_tail_parameters']
            or cut != record['physical_tail_cut']):
        raise ValueError('Source profile, chart or full physical port differs')
    modes = int(record['modes'])
    mean_nodes = record.get('prefix_audit', {}).get('samples_psi')
    if (not isinstance(mean_nodes, int) or isinstance(mean_nodes, bool)
            or mean_nodes < 16*(3*modes+1)):
        raise ValueError('Source actual Cartesian audit/mean quadrature is inadequate')
    raw_path = path.parent/record['raw_return']['file']
    with np.load(raw_path, allow_pickle=False) as raw_file:
        raw = {key: raw_file[key].copy() for key in
               ('x', 'y', 'p', 'pscale', 'cubic_x', 'cubic_c', 'rms')}
    x, y, p, scale = (raw[key] for key in ('x', 'y', 'p', 'pscale'))
    if (modes < 1 or x.ndim != 1 or len(x) < 2 or y.shape != (3*modes+1, len(x))
            or p.shape != (modes,) or scale.shape != (modes-1,)
            or raw['cubic_c'].shape != (4, len(x)-1, 3*modes+1)
            or raw['rms'].shape != (len(x)-1,)
            or not np.array_equal(raw['cubic_x'], x)
            or not all(np.all(np.isfinite(value)) for value in raw.values())
            or not np.all(np.diff(x) > 0) or x[0] != 0. or x[-1] != 1.
            or not np.all(scale > 0)
            or not np.array_equal(scale, np.asarray(record['parameter_scales']))
            or not np.array_equal(p, np.asarray(record['raw_return']['parameters']))
            or record['raw_return']['nodes'] != len(x)
            or float(np.max(raw['rms'])) != record['raw_return']['rms']
            or float(np.min(raw['rms'])) < 0):
        raise ValueError('Source raw PPoly, nodal data or original parameter scales disagree')
    with np.load(path.parent/'physical.npz', allow_pickle=False) as physical:
        if (physical['x'].shape != x.shape
                or physical['c'].shape != (6, len(x)-1, 3*modes+1)
                or not np.array_equal(physical['p'], p)
                or not all(np.all(np.isfinite(physical[key])) for key in ('x', 'c', 'p'))
                or not np.all(np.diff(physical['x']) > 0)):
            raise ValueError('Complete saved physical C2 source has inconsistent shape or parameters')
    if record['frozen_profile'] != dict(profile, delta=profile['delta']+float(p[0])):
        raise ValueError('The recorded delta is not the original additive parameter')
    if (port['modes'] != [3*(j+1) for j in range(modes)]
            or len(port['linearSlope']) != modes
            or int(option(record, '--modes')) != modes
            or float(option(record, '--amplitude')) != record['gauge_q']
            or float(option(record, '--warp-reference')) != record['warp_reference']):
        raise ValueError('Original state/port/gauge dimensions disagree')
    return record, raw


def same_design_contract(left, right):
    for key in ('physical_profile', 'physical_tail_parameters', 'physical_tail_cut',
                'angular_chart', 'gauge_q', 'warp_reference', 'modes', 'angular',
                'parameter_scales', 'source_hashes', 'gates'):
        if left[key] != right[key]:
            raise ValueError('Secant sources differ in the common design contract: '+key)
    for flag in ('--source-topic', '--short-bridge', '--profile', '--chart', '--port',
                 '--core-module', '--audit-angular'):
        if option(left, flag) != option(right, flag):
            raise ValueError('Secant sources use different original command inputs: '+flag)
    for flag in ('--profile', '--chart', '--port', '--core-module'):
        name = str(Path(option(left, flag)).resolve())
        if left['inputs'][name] != right['inputs'][name]:
            raise ValueError('Secant source input bytes differ: '+flag)
    left_settings = {k: v for k, v in left['core_settings'].items() if k != 'homotopy'}
    right_settings = {k: v for k, v in right['core_settings'].items() if k != 'homotopy'}
    if left_settings != right_settings:
        raise ValueError('Only the material homotopy may differ in core settings')
    if left['prefix_audit']['samples_psi'] != right['prefix_audit']['samples_psi']:
        raise ValueError('The two actual source Cartesian mean quadratures differ')


def predict(repo, left_path, right_path, target, outdir):
    import numpy as np
    from scipy.interpolate import PPoly
    left_path, right_path = Path(left_path).resolve(), Path(right_path).resolve()
    out = Path(outdir).resolve()
    left, lraw = accepted_original(left_path, repo)
    right, rraw = accepted_original(right_path, repo)
    same_design_contract(left, right)
    ll, lr = (float(record['core_settings']['homotopy']) for record in (left, right))
    if not (math.isfinite(target) and 0 < ll < lr < target <= 1):
        raise ValueError('Require increasing accepted lambda pair and a later target <= 1')
    if not np.array_equal(lraw['pscale'], rraw['pscale']):
        raise ValueError('Original support scales differ')
    x = np.unique(np.concatenate((lraw['x'], rraw['x'])))
    union_nodes, right_nodes = len(x), len(rraw['x'])
    max_nodes = right['gates']['max_nodes']
    if right_nodes > max_nodes:
        raise ValueError('The actual right field itself exceeds the original node budget')
    grid_rule = 'actual_grid_union'
    if union_nodes > max_nodes:
        x = rraw['x'].copy()
        grid_rule = 'right_original_grid_budget_fallback'
    values = []
    nodal_errors = []
    for raw in (lraw, rraw):
        pp = PPoly.construct_fast(raw['cubic_c'], raw['cubic_x'],
                                  axis=1, extrapolate=False)
        original_values = pp(raw['x'])
        error = float(np.max(np.abs(original_values-raw['y'])))
        allowance = 32*np.finfo(float).eps*max(1., float(np.max(np.abs(raw['y']))))
        if not np.all(np.isfinite(original_values)) or error > allowance:
            raise ValueError('Saved original cubic does not reproduce its recorded nodes')
        nodal_errors.append(error)
        values.append(pp(x))
    beta = (target-lr)/(lr-ll)
    y = values[1]+beta*(values[1]-values[0])
    p = rraw['p']+beta*(rraw['p']-lraw['p'])
    if not np.all(np.isfinite(y)) or not np.all(np.isfinite(p)):
        raise FloatingPointError('The unaccepted secant initializer is not finite')
    out.mkdir(parents=True, exist_ok=False)
    destination = out/'initial.npz'
    np.savez_compressed(destination, x=x, y=y, p=p, pscale=rraw['pscale'])
    def provenance(path, record):
        return dict(run=str(path), run_sha256=digest(path),
            homotopy=record['core_settings']['homotopy'],
            raw=str(path.parent/record['raw_return']['file']),
            raw_sha256=record['raw_return']['sha256'],
            physical=str(path.parent/'physical.npz'), physical_sha256=record['physical_sha256'],
            actual_delta=record['frozen_profile']['delta'], nodes=record['raw_return']['nodes'],
            rms=record['raw_return']['rms'], metric=record['prefix_audit']['metric_l1'],
            physical_bc=record['prefix_audit']['physical_bc_max'])
    record = dict(scope=__doc__, status='unaccepted_secant_initializer_ready',
        record_kind='unaccepted_nodal_initializer', accepted_bvp=False,
        initializer_is_accepted_solution=False, solver_invoked=False, solver_success=None,
        physical_metric_gate_paid=False, physical_boundary_gate_paid=False,
        domain_gate_paid=False, true_tail_paid=False, fixed_metric_refinement=False,
        complete_surface=False, left=provenance(left_path, left), right=provenance(right_path, right),
        target_lambda=target, secant_beta=beta, modes=right['modes'], nodes=len(x),
        grid_rule=grid_rule, union_nodes=union_nodes, right_nodes=right_nodes,
        max_nodes=max_nodes,
        gauge_q=right['gauge_q'], warp_reference=right['warp_reference'],
        mean_nodes=right['prefix_audit']['samples_psi'],
        coordinate='Common computational t; saved original cubic PPoly, no spline refit',
        parameter_zero_meaning='additive delta increment',
        remaining_parameters='Original R53 support coordinates with identical saved pscale',
        source_nodal_evaluation_roundoff=nodal_errors,
        predicted_delta=right['physical_profile']['delta']+float(p[0]),
        max_state_increment_from_right=float(np.max(np.abs(y-values[1]))),
        max_parameter_increment_from_right=float(np.max(np.abs(p-rraw['p']))),
        source_hashes={str(Path(__file__).resolve()): digest(__file__),
            str(Path(repo).resolve()/'topics/visible-flex-held-10pct/scripts/resume_20261126/material_design_continue.py'):
            digest(Path(repo)/'topics/visible-flex-held-10pct/scripts/resume_20261126/material_design_continue.py')},
        result=dict(initial_raw=str(destination), initial_raw_sha256=digest(destination)),
        acceptance_required='Original portable initial-domain check, actual BVP/RMS, physical BC and full metric audit')
    (out/'predictor.json').write_text(json.dumps(record, indent=2, allow_nan=False)+'\n')
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'left-run', 'right-run', 'outdir'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--target-lambda', type=float, required=True)
    args = parser.parse_args()
    result = predict(args.repo, args.left_run, args.right_run, args.target_lambda, args.outdir)
    print(json.dumps(result, allow_nan=False))


if __name__ == '__main__':
    main()
