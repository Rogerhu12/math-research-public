#!/usr/bin/env python3
"""R98 rational time constants for one genuine own fixed prefix/cut/cylinder.

Reuse the frozen complete-prefix C2 reader and its exact active-span Hermite
algebra.  Read all existing true angular orders 0..3 unchanged; add a new
global angular-four majorant using the complete original support and Gamma5.
The input is an actually accepted own fixed return, never a design predictor.

No prefix solve, native flow, mean construction, angular integration or old
tail is executed.  Complete finite-tail, deep-collar and Cartesian-disk time
bounds are explicitly pending; this component cannot assert a whole-map M2.
All actual journals and coefficient data remain outside every source tree.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'

import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import sys
import time
from types import SimpleNamespace

import numpy as np

HERE = Path(__file__).resolve().parent
ANALYTIC = HERE.parent/'analytic'
SCRIPTS = HERE.parents[1]
REPO = SCRIPTS.parents[2]
sys.path.insert(0, str(HERE))
import rational_time_jet_bounds as bounds

PREFIX_READER = ANALYTIC/'qr_fixed_complete_prefix_c2.py'
PREFIX_READER_SHA = '70069b8367d80063f3ef085d2e3a41e68c0cca7a6c85408bd3ab95cb18a03a86'
PAIR_GATE = HERE/'qr_fixed_complete_tail_c2.py'
PAIR_GATE_SHA = '1808a976bf4082fbe9b339fb24fdd7b87f3d29d36be05d15bcfdb7c7f24cc00e'
PAIR_ALGEBRA = ANALYTIC/'prefix_physical_theta_c2_bounds.py'
PAIR_ALGEBRA_SHA = 'f45298d263a09cca3b015b8f61fdfed2033167180867d667574cdd018cae560c'
SCHEMA = 'genuine-own-fixed-prefix-cut-cylinder-rational-R98-time-bounds-v1'
SCALAR_KEYS = ('coordinate_C2_time_second', 'normalized_jacobian_time_second',
               'normalized_jacobian_time_first')
COMPLETE_COMPONENTS = ('upper_prefix_and_cut', 'lower_reflected_prefix_and_cut',
                       'central_cylinder')
PENDING_COMPONENTS = ('upper_complete_finite_tail', 'lower_reflected_complete_finite_tail',
    'upper_deep_collar', 'lower_reflected_deep_collar',
    'upper_cartesian_marker_disk', 'lower_cartesian_marker_disk')


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda:stream.read(1024*1024), b''):
            digest.update(block)
    return digest.hexdigest()


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path))


def encode(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {str(key):encode(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [encode(item) for item in value]
    return value


def write(path, value):
    path = Path(path)
    temporary = path.with_name(path.name+'.tmp')
    with temporary.open('w') as stream:
        json.dump(encode(value), stream, indent=2, allow_nan=False)
        stream.write('\n'); stream.flush(); os.fsync(stream.fileno())
    temporary.replace(path)


def module(name, path, digest):
    if sha(path) != digest:
        raise ValueError('The reviewed true-field provider changed: '+str(path))
    previous = sys.modules.get(name)
    if previous is not None:
        if Path(previous.__file__).resolve() != Path(path).resolve():
            raise ValueError('Use a fresh process for this genuine source tree')
        return previous
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value; spec.loader.exec_module(value)
    return value


def new_fourth(field, core, original):
    """Add just the missing order, without rebuilding any old angular data."""
    projection = original.projection(field)
    proj4 = sum((abs(value)*original.weight(key, 4) for key, value in projection.items()), Q(0))
    raw4 = [sum((abs(original.fq(field['data']['jets'][r,j,0]))
        *original.weight(key, 4) for j, key in enumerate(field['keys'])), Q(0)) for r in range(3)]
    radial = [original.fq(field['data']['lift_jets'][r,0,0]) for r in range(3)]
    extra = bounds.angular_fourth(core, original.fq(field['data']['E0']),
        original.fq(field['data']['Epp']), proj4, raw4, radial)
    lift = list(field['lift_absolute'])+[extra['lift_fourth']]
    center = list(field['center_absolute'])+[extra['center_fourth']]
    cut = [[sum((max(map(abs, interval))*original.weight(key,j)
        for key, interval in field['cut_intervals'][r].items()), Q(0))
        for r in range(3)] for j in range(5)]
    if len(lift) != 5 or len(center) != 5 or any(len(row) != 3 for row in center+cut):
        raise ArithmeticError('A complete angular-four correction is missing')
    return dict(lift=lift, center=center, cut=cut, new_fourth=extra,
        old_angular_orders=[0,1,2,3], new_angular_orders=[4],
        old_interval_table_relabelled=False, all_projection_and_cut_modes_retained=True)


def span_bounds(field, polynomial, angular, left, right, algebra, original):
    W, CW = original.bounds.radial_weights(left, right,
        center_width=field['center_width'], end=field['end'], cut_width=field['cut_width'],
        algebra=algebra)
    raw = [[algebra.bernstein_abs(poly) for poly in polynomial['jets'][r]] for r in range(3)]
    lift = [algebra.bernstein_abs(polynomial['lift_jets'][r][0]) for r in range(3)]
    chart = [algebra.bernstein_abs(polynomial['chart_jets'][r][0]) for r in range(3)]
    same = {}
    for r, j in bounds.NEEDED:
        same[r, j] = (sum((size*original.weight(key,j)
            for size, key in zip(raw[r], field['keys'])), Q(0))
            +lift[r]*angular['lift'][j]
            +sum((W[r][i]*angular['center'][j][i]+CW[r][i]*angular['cut'][j][i]
                  for i in range(3)), Q(0)))
    physical, inverse = bounds.physical_theta_jets(same, chart)
    return dict(same_psi=same, physical_theta=physical, chart_absolute=chart,
                inverse_chart=inverse)


def make_target(source, continuous):
    """Use the unchanged actual fixed g, without rebuilding a finite mean."""
    reader = sys.modules['qr_fixed_actual_cartesian_prefix']
    bases = continuous.proof_modules(source['context'])
    original = bases['metric']
    obj = reader.model.load_model(dict(source_run=source['source_run']['path'], repo=str(reader.REPO)))
    with np.load(source['physical']['path'], allow_pickle=False) as saved:
        parameters = saved['p'].copy()
    obj.initial(parameters)
    target = original.FrozenTarget(obj.flow(parameters[0]), source['record'])
    return target, original.I, original


def positive_radius(target, I, left, right, depth=0):
    """Exact-cover positive lower bound from the original outward g oracle."""
    query = I(I.rational(left).x[0], I.rational(right).x[1])
    radius = target.jets(query, left, right)[0]
    if not radius.finite():
        raise ArithmeticError('The original true target radius oracle returned a nonfinite enclosure')
    lower = Q.from_float(float(radius.x[0]))
    if lower > 0:
        return lower, 1
    if depth >= 24:
        raise ArithmeticError('A positive true target radius remains unresolved after exact bisection')
    middle = (left+right)/2
    lo, n = positive_radius(target, I, left, middle, depth+1)
    hi, m = positive_radius(target, I, middle, right, depth+1)
    return min(lo, hi), n+m


def cylinder_bounds(core, phase_end, curvature, half_length):
    G = core['gamma_material_derivatives']
    P = {key:Q(0) for key in bounds.NEEDED}
    for j in range(5):
        P[0,j] = G[j]
    # Its vertical position is fixed in time. Including it is a harmless
    # explicit overestimate in the full-vector generator bound.
    P[0,0] += half_length
    P[1,0] = Q(1)
    return bounds.time_bounds(P, phase_end=phase_end, curvature=curvature,
        center_norm=core['held_circle_center_norm_upper'], radius_lower=Q(1))


def loaded_mathematical_sources(roots):
    """Bind the actual original and current Python providers used this turn."""
    paths = set()
    for value in tuple(sys.modules.values()):
        filename = getattr(value, '__file__', None)
        if filename is None:
            continue
        path = Path(filename).resolve()
        if path.suffix == '.py' and path.is_file() and any(root in path.parents for root in roots):
            paths.add(path)
    return {str(path):sha(path) for path in sorted(paths)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('source-run', 'tables', 'cut', 'outdir'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--phase-end', type=Q, required=True)
    parser.add_argument('--held-width', type=Q, default=Q(27,50))
    parser.add_argument('--cylinder-half-length', type=float, default=.0025)
    args = parser.parse_args()
    if (args.phase_end <= 0 or args.held_width <= 0
            or not np.isfinite(args.cylinder_half_length) or args.cylinder_half_length <= 0):
        raise ValueError('Use an explicit positive affine phase, grip and actual cylinder')
    out = args.outdir.resolve()
    if out == REPO or REPO in out.parents:
        raise ValueError('All actual time-bound inputs and journals stay outside git')
    if sha(PAIR_ALGEBRA) != PAIR_ALGEBRA_SHA:
        raise ValueError('The original exact radial-weight algebra needs an explicit new review')
    original = module('_actual_R98_complete_prefix_reader', PREFIX_READER, PREFIX_READER_SHA)
    gate = module('_actual_R98_complete_source_gate', PAIR_GATE, PAIR_GATE_SHA)
    if original.PAIR_SHA != PAIR_GATE_SHA:
        raise ValueError('The complete prefix and actual pair gates disagree')
    # Reuse the full genuine gate on one own return. This is an identity
    # source validation only; no self-difference or refinement claim is made.
    source, duplicate, agreement, algebra, roots = gate.accepted_pair(SimpleNamespace(
        left_source_run=args.source_run.resolve(), right_source_run=args.source_run.resolve(),
        left_coupling_summary=None))
    del duplicate
    if source['role'] != 'own_accepted_QR_fixed_metric_return':
        raise ValueError('Require one genuine own fixed return, without an anchor relabel')
    if any(out == root or root in out.parents for root in roots):
        raise ValueError('Time-bound outputs cannot be inside any preserved numerical tree')
    field = original.load_field(source, args.tables, args.cut, agreement['fixed_problem'])
    problem = agreement['fixed_problem']
    settings = problem['core_settings']
    lam, S, b, k, blend = (original.fq(settings[key]) for key in
        ('homotopy', 'halfwidth', 'transition', 'target_curvature', 'curvature_blend'))
    if lam != 1 or blend != 1:
        raise ValueError('The held generator requires the actual complete lambda-one circle')
    margin = S-(args.phase_end+args.held_width)/2
    if margin <= 0:
        raise ValueError('The entire actual grip sweep must lie strictly inside the true window')
    core = bounds.true_core_bounds(field['core_coefficients'], homotopy=lam,
        halfwidth=S, transition=b, curvature=k)
    angular = new_fourth(field, core, original)
    continuous = sys.modules['_qr_tail_pair_fixed_continuous']
    target, I, target_api = make_target(source, continuous)
    grid = sorted(set(field['x']+target.grid+[field['center_width'], field['end']-field['cut_width']]))
    if grid[0] != 0 or grid[-1] != field['end'] or target.end != field['end']:
        raise ValueError('The complete finite field and true target domains differ')
    out.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    h = original.fq(args.cylinder_half_length)
    report = dict(schema=SCHEMA, status='actual_prefix_time_bounds_running',
        actual_source=gate.source_metadata(source), fixed_problem=problem,
        field_definition=field['identity'], true_target=target.definition,
        phase_end_exact=str(args.phase_end), held_width_exact=str(args.held_width),
        affine_phase='alpha(t)=phase_end*t', cylinder_half_length_exact=str(h),
        strict_circle_window_margin_exact=str(margin), true_core_bounds=core,
        angular_four_extension=angular, coordinate_domain='physical (s,theta)',
        physical_s_range=['0',str(field['end'])], full_theta_range='all real theta modulo 2*pi',
        all_actual_modes_and_final_finite_mean_retained=True,
        actual_tail_time_bounds_inherited=False, old_angular_table_relabelled=False,
        original_source_gate_reused_as_identity_only=True,
        exact_common_grid_sha256=hashlib.sha256(('\n'.join(map(str,grid))+'\n').encode()).hexdigest(),
        total_spans=len(grid)-1, completed_spans=0, target_radius_cells=0,
        complete_components=[], pending_components=list(COMPLETE_COMPONENTS+PENDING_COMPONENTS),
        prefix_cut_cylinder_time_constants_certified=False, whole_surface_time_constants_certified=False,
        time_interpolation_executed=False, BVP_or_native_called=False, C2_limit_proved=False,
        per_span_receipt='Three exact time constants and positive frame lower bounds; full temporary derivative majorants are reproducible from the bound complete inputs.',
        source_hashes=loaded_mathematical_sources(roots))
    for path in (Path(__file__), Path(bounds.__file__), PREFIX_READER, PAIR_GATE, PAIR_ALGEBRA,
                 Path(algebra.__file__), Path(target_api.__file__),
                 Path(sys.modules['cartesian_prefix_metric_target'].__file__)):
        report['source_hashes'][str(path.resolve())] = sha(path)
    write(out/'summary.json', report)
    polynomials = original.RadialPolynomials(field, algebra)
    maxima = {key:Q(0) for key in SCALAR_KEYS}
    records = out/'complete-prefix-time-spans.jsonl'
    try:
        with records.open('x') as stream:
            for index, (left,right) in enumerate(zip(grid[:-1],grid[1:])):
                result = span_bounds(field, polynomials.span(left,right), angular,
                    left, right, algebra, original)
                a, cells = positive_radius(target, I, left, right)
                temporal = bounds.time_bounds(result['physical_theta'], phase_end=args.phase_end,
                    curvature=k, center_norm=core['held_circle_center_norm_upper'], radius_lower=a)
                for key in SCALAR_KEYS:
                    maxima[key] = max(maxima[key], temporal[key])
                computed = dict(derivative_bounds=result,time_bounds=temporal)
                computed_bytes = json.dumps(encode(computed),sort_keys=True,
                    separators=(',',':'),allow_nan=False).encode()
                row = dict(index=index, left=left, right=right, target_radius_cells=cells,
                    time_constants={key:temporal[key] for key in SCALAR_KEYS},
                    true_target_radius_lower=a,
                    material_chart_rho_lower=result['inverse_chart']['rho_lower'],
                    recomputable_full_majorant_sha256=hashlib.sha256(computed_bytes).hexdigest())
                stream.write(json.dumps(encode(row), separators=(',',':'), allow_nan=False)+'\n')
                stream.flush(); os.fsync(stream.fileno())
                report.update(completed_spans=index+1, seconds=time.monotonic()-started,
                    target_radius_cells=report['target_radius_cells']+cells,
                    partial_prefix_maxima=maxima)
                if (index+1)%20 == 0:
                    write(out/'summary.json', report)
                    print(json.dumps(dict(completed_spans=index+1,total_spans=len(grid)-1,
                        seconds=report['seconds'])), flush=True)
        if report['completed_spans'] != report['total_spans']:
            raise ArithmeticError('The exact complete physical prefix cover was not finished')
        cylinder = cylinder_bounds(core, args.phase_end, k, h)
        combined = {key:max(maxima[key],cylinder[key]) for key in SCALAR_KEYS}
        for name in ('table_report','cut_report','defining_jets','angular_tables','cut_data','geometry_bundle'):
            original.check(field['identity'][name])
        for key in ('source_run','raw','physical','final_height_binding','final_packet',
                    'runtime','baseline','port','native_manifest'):
            gate.checked_path(source[key])
        for path,digest in report['source_hashes'].items():
            if sha(path) != digest:
                raise ValueError('A bound mathematical source changed during the complete cover')
        report.update(status='actual_prefix_cut_cylinder_R98_time_constants_certified',
            prefix_cut_cylinder_time_constants_certified=True,
            complete_components=list(COMPLETE_COMPONENTS), pending_components=list(PENDING_COMPONENTS),
            prefix_time_constants=maxima, cylinder_time_constants=cylinder,
            combined_prefix_cut_cylinder_time_constants=combined,
            exact_full_coverage_checked=True, actual_span_records=ref(records),
            all_bound_inputs_rechecked=True, seconds=time.monotonic()-started,
            maximum_rss_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        report.pop('partial_prefix_maxima', None)
        write(out/'summary.json', report)
        print(json.dumps(dict(status=report['status'], summary=ref(out/'summary.json'),
            actual_prefix_complete=True, whole_surface_time_constants_certified=False,
            pending_components=list(PENDING_COMPONENTS))), flush=True)
    except BaseException as error:
        report.update(status='actual_prefix_time_bound_execution_incomplete',
            actual_exception_type=type(error).__name__, actual_exception=str(error),
            seconds=time.monotonic()-started)
        if records.exists():
            report['actual_partial_span_records'] = ref(records)
        write(out/'summary.json', report)
        raise


if __name__ == '__main__':
    main()
