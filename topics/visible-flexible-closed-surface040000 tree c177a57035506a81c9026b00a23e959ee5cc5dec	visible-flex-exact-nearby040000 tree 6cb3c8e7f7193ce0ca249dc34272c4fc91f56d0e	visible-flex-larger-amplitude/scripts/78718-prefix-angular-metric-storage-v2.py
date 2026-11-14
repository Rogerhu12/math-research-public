#!/usr/bin/env python3
# New 78718 explicit storage adaptation; original mathematical source is retained below.
"""First-tier angular refinement for one fixed common-cut prefix and target.

Requires a complete, reviewed certificate from the original coefficient-first
prefix backend and its reviewed analytic target/unique bridge certificate.
An inherited strict bound is reused whenever it already meets the budget.
Otherwise the original interval bound is computed, then only failing angular
arcs are bisected. No radial refinement, Taylor-angle method, ODE solve or new
map is performed. A local selection never emits a whole-prefix metric field.
"""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import io
import json
import math
from pathlib import Path
import resource
import sys
import time
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SOURCES = {
    '78718-prefix-metric-budget-storage-v2.py': '18599b65771eae53199442589547105292489c323aac333e5eee6f2dacadb3aa',
    '78718-prefix-metric-polynomial-storage-v1.py': 'd290543f75224509fef8287db838265540a74b7caec38d7b9f34cea563d8359e',
    '78718-prefix-continuous-hermite-storage-v1.py': '09e8c748c7cc49347876d849029e835a8cd0e5f097d36eaf6cf2fd7c0f2ddc18',
    'db6f-audit-tail-metric-curvature.py': 'ed175aacdb2ba3e84d7c397d121e90c2a6a1492d05f5efdb646690481d302670',
    '78718-prefix-metric-supplier-storage-v1.py': 'f2d8e79504a2a3895ec8705457eabe46321e80b68b8e7c7de11f13015d160ff3',
    '78718-prefix-common-cut-storage-v1.py': '34b0b92c6f4d92bd497f3d84d28cbd73cb29271e36b240d3a19795987f057d43',
    'db6f-root-exact-bridge.py': 'f5d10784f58fa5008220354665de710ab4991b795f1b902e26a70ca44f382fd1',
    'db6f_tail_integrated.py': '4714e67860c80ecffc691d0d1e797bf5e8fa62062a4292730646abdf7f6e87ae',
    '78718-prefix-angular-arithmetic-storage-v2.py': '4977cb407bc9cdd64a580c999727a9978bf4041011e89cab192be7ecd2c2f5dd',
    '78718-prefix-storage-v1.py': '83cf59cfe5ab373421e53d0c0d8d2274edfc6a6b266fc2ab6161274b474a4329',
    '78718-prefix-byte-shards-v1.py': 'e23153ae6b364854a24acc464be97921b134f7e25024e82c8c91995ca2f96f39',
}


def check(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec)
    sys.modules[name] = obj
    spec.loader.exec_module(obj)
    return obj


def locate(name, anchor=None):
    path = Path(name)
    candidates = [path, ROOT/path, ROOT/'notes'/path.name]
    if anchor is not None:
        candidates = [path, Path(anchor)/path.name, Path(anchor)/path]+candidates[1:]
    for candidate in candidates:
        if candidate.exists():
            return candidate.resolve()
    raise FileNotFoundError(name)


def read(path):
    payload = Path(path).read_bytes()
    return json.loads(gzip.decompress(payload) if payload[:2] == b'\x1f\x8b' else payload)


def positive_binary(value, name, zero=False):
    check(isinstance(value, (int, float)) and math.isfinite(value) and
          (value >= 0 if zero else value > 0), 'Invalid '+name)
    return Q(value)


def record(value):
    value = Q(value)
    display = float(value)
    if Q(display) < value:
        display = math.nextafter(display, math.inf)
    return dict(exact=str(value), upper_display=display)


class Rows:
    """Small immutable gzip shards; the final report is written only at success."""
    def __init__(self, out, label):
        self.out, self.label, self.buffer, self.files = out, label, [], []
        check(not list(out.parent.glob(out.stem+'.'+label+'.part*.json.gz')), 'Output shards already exist')

    def add(self, row):
        self.buffer.append(row)
        if len(self.buffer) >= 512:
            self.flush()

    def flush(self):
        if not self.buffer:
            return
        name = self.out.stem+'.'+self.label+'.part%03d.json.gz' % len(self.files)
        path = self.out.parent/name
        check(not path.exists(), 'Output shard exists')
        payload = gzip.compress(json.dumps(self.buffer, separators=(',', ':'), allow_nan=False).encode(), mtime=0)
        check(len(payload) < 5_000_000, 'Output shard exceeds repository size bound')
        path.write_bytes(payload)
        self.files.append(dict(file=name, sha256=sha(path), bytes=len(payload), rows=len(self.buffer)))
        self.buffer = []


def validate_inputs(args):
    for name, digest in SOURCES.items():
        check(sha(HERE/name) == digest, 'Frozen mathematical implementation changed: '+name)
    meta, target, baseline, bridge = [read(path) for path in
        (args.geometry, args.target, args.baseline, args.bridge)]
    check(meta.get('representation') == 'exact-common-cut-prefix' and
          meta['common_cut_implementation_sha256'] == SOURCES['78718-prefix-common-cut-storage-v1.py'],
          'This storage implementation requires the reviewed common-cut storage definition')
    base_path = locate(meta['base_geometry'], args.geometry.parent)
    check(sha(base_path) == meta['base_geometry_sha256'], 'Changed base prefix')
    original = read(base_path)
    for key in ('frozen_profile', 'chart', 'warp_reference_q', 'ell'):
        check(meta[key] == original[key], 'Changed copied target/coordinate definition '+key)
    check(meta['ell'] == 0 and int(meta['modes']) >= 1, 'Unsupported common-cut chart or Fourier basis')
    storage = module('prefix_angular_jet_storage', HERE/'78718-prefix-storage-v1.py')
    loaded_base, geometry_payload, storage_bindings = storage.read_payload(base_path, verify_arrays=True)
    check(json.dumps(loaded_base, sort_keys=True, allow_nan=False) ==
          json.dumps(original, sort_keys=True, allow_nan=False), 'Base metadata changed during storage read')
    check(hashlib.sha256(geometry_payload).hexdigest() == original['data_sha256'] == meta['data_sha256'],
          'Changed exact geometry arrays')
    check(json.dumps(original.get('data_storage'), sort_keys=True, allow_nan=False) ==
          json.dumps(meta.get('data_storage'), sort_keys=True, allow_nan=False),
          'Common-cut storage reference differs from its defining base')
    check(meta['tail_reader_sha256'] == SOURCES['db6f_tail_integrated.py'], 'Changed tail representation')
    tail_path = locate(meta['tail_manifest'], args.geometry.parent)
    check(sha(tail_path) == meta['tail_manifest_sha256'], 'Changed common-cut tail')
    tail = read(tail_path)
    check(tail.get('finished') is True, 'Unfinished finite tail')
    # Hash payloads without decoding them when the old global bound suffices.
    for item in tail['files']:
        path = locate(item['path'], tail_path.parent)
        check(sha(path) == item['sha256'] and path.stat().st_size == item['bytes'], 'Changed tail data shard')
    check(meta['bridge_parameter_certificate_sha256'] == sha(args.bridge) and
          sha(locate(meta['bridge_parameter_certificate'], args.geometry.parent)) == sha(args.bridge),
          'Common-cut map and exact-target bridge differ')
    check(bridge['script_sha256'] == SOURCES['db6f-root-exact-bridge.py'] and
          bridge['unique_root_in_box'] is True and
          bridge['geometry_sha256'] == sha(base_path) and
          bridge['target_sha256'] == sha(args.target), 'Wrong exact bridge/target binding')
    check(Q(bridge['arclength_rescale']['lo']) > 0 and
          Q(bridge['arclength_rescale']['lo']) <= Q(bridge['arclength_rescale']['hi']), 'Invalid exact bridge rescale')
    cut, slope = Q(tail['parameters']['rCut']), Q(tail['parameters']['wCut'])
    check(cut > 0 and cut == Q(bridge['physical_cut_radius_exact']) and
          slope == Q(bridge['physical_cut_slope_exact']) and
          -7*slope/cut == Q(bridge['physical_cut_second_derivative_exact']), 'Different physical cut target')
    eta = positive_binary(bridge['relative_target_metric_difference_upper'], 'target transfer bound', zero=True)
    check(target['geometry_sha256'] == sha(base_path) and
          target['frozen_profile'] == original['frozen_profile'] and
          target['script_sha256'] == SOURCES['78718-prefix-metric-supplier-storage-v1.py'] and
          target['arithmetic_backend_sha256'] == SOURCES['78718-prefix-metric-polynomial-storage-v1.py'] and
          target['prefix_bridge_extension_guard_passed'] is True, 'Wrong reviewed analytic target packet')
    extractor = locate(original['source_root'])/'topics/large-amplitude-twist-flex/scripts/f6curve_bidirectional_bridge.py'
    check(sha(extractor) == target['bridge_parameter_extractor_sha256'], 'Changed bridge constant extractor')
    target_data = locate(target['data_file'], args.target.parent)
    check(sha(target_data) == target['data_sha256'], 'Changed analytic target arrays')
    with np.load(io.BytesIO(gzip.decompress(target_data.read_bytes())), allow_pickle=False) as data:
        raw = {name: data[name] for name in data.files}
    with np.load(io.BytesIO(gzip.decompress(geometry_payload)), allow_pickle=False) as data:
        mesh = data['mesh']
    check(mesh.ndim == 1 and len(mesh) >= 2 and np.isfinite(mesh).all() and
          np.all(np.diff(mesh) > 0), 'Invalid exact geometry mesh')
    left, right = raw['left'], raw['right']
    check(left.ndim == 1 and left.shape == right.shape and len(left) > 0 and
          np.isfinite(left).all() and np.isfinite(right).all() and np.all(right > left), 'Invalid target intervals')
    check(left[0] == mesh[0] and right[-1] == mesh[-1] and np.array_equal(right[:-1], left[1:]),
          'Target does not exactly partition the complete prefix')
    check(target['intervals'] == len(left), 'Target interval ledger differs')
    indices = np.clip(np.searchsorted(mesh, left, side='right')-1, 0, len(mesh)-2)
    check(np.all(left >= mesh[indices]) and np.all(right <= mesh[indices+1]), 'Target crosses a geometry polynomial knot')
    check(baseline['geometry_sha256'] == sha(args.geometry) and
          baseline['geometry_data_sha256'] == hashlib.sha256(geometry_payload).hexdigest() and
          baseline['target_sha256'] == sha(args.target) and
          baseline['target_data_sha256'] == sha(target_data) and
          baseline['script_sha256'] == SOURCES['78718-prefix-metric-polynomial-storage-v1.py'] and
          baseline['backend_sha256'] == SOURCES['78718-prefix-continuous-hermite-storage-v1.py'], 'Baseline belongs to another map/target/backend')
    check(baseline['entire_prefix_covered'] is True and
          baseline['intervals_checked'] == baseline['intervals'] == len(left), 'Incomplete original certificate')
    old_upper = positive_binary(baseline['metric_operator_upper'], 'old complete metric upper', zero=True)
    a_lower = positive_binary(baseline['minimum_a_lower'], 'old a lower')
    rho_lower = positive_binary(baseline['minimum_chart_rho_lower'], 'old rho lower')
    return meta, raw, baseline, eta, old_upper, a_lower, rho_lower, storage_bindings


def trig_table(backend, modes, left, right):
    """Same reviewed endpoint Taylor/critical-point range, with periodic cache keys."""
    out = []
    for cosine in (True, False):
        low, high = [], []
        for j in range(1, modes+1):
            a, b = j*left, j*right
            # trig_point itself begins with this exact reduction. Canonical
            # keys only avoid repeating the same rational Taylor evaluation.
            ea = backend.base.trig_point((a+1) % 2-1, cosine)
            eb = backend.base.trig_point((b+1) % 2-1, cosine)
            lo, hi = min(ea[0], eb[0]), max(ea[1], eb[1])
            maximum, minimum = (Q(0), Q(1)) if cosine else (Q(1, 2), Q(3, 2))
            if backend.base.ceil((a-maximum)/2) <= backend.base.floor((b-maximum)/2):
                hi = 1.
            if backend.base.ceil((a-minimum)/2) <= backend.base.floor((b-minimum)/2):
                lo = -1.
            low.append([lo]); high.append([hi])
        out.append(backend.I(np.array(low), np.array(high)))
    return tuple(out)


def verify_rows(out, files, raw, selected, eta, budget):
    """Reread every written leaf, checking exact requested-domain coverage."""
    position, cursor, count, maximum, worst = 0, Q(0), 0, Q(0), None
    for item in files:
        path = out.parent/item['file']
        check(sha(path) == item['sha256'], 'Changed written leaf shard')
        rows = read(path)
        check(len(rows) == item['rows'], 'Written leaf count mismatch')
        for row in rows:
            check(position < len(selected), 'Extra parent interval')
            index = selected[position]
            check(row['interval'] == index and Q(row['radial_local_left']) == 0 and
                  Q(row['radial_local_right']) == 1 and
                  Q(row['s_left_exact']) == Q(float(raw['left'][index])) and
                  Q(row['s_right_exact']) == Q(float(raw['right'][index])), 'Wrong physical parent leaf')
            left, right = Q(row['angle_pi_left']), Q(row['angle_pi_right'])
            check(left == cursor and left < right <= 2, 'Angular overlap or uncovered slice')
            source, target = Q(row['source_metric_upper_exact']), Q(row['exact_target_metric_upper_exact'])
            check(source >= 0 and target == source*(1+eta)+eta and
                  row['target_met'] == (target <= budget), 'Wrong exact target transfer or budget comparison')
            check(Q(row['a_lower_exact']) > 0 and Q(row['rho_lower_exact']) > 0, 'Unpaid positive denominator')
            if target > maximum:
                maximum, worst = target, dict(interval=index, angle_pi_left=str(left), angle_pi_right=str(right))
            count += 1
            cursor = right
            if cursor == 2:
                position += 1; cursor = Q(0)
    check(position == len(selected) and cursor == 0, 'Requested domain is not fully covered')
    return dict(leaves=count, exact_target_max=maximum, worst=worst)


def run(args):
    started = time.monotonic()
    check(not args.out.exists(), 'Output report already exists')
    budget = Q(args.budget)
    check(budget > 0 and args.initial_arcs > 0 and args.max_depth >= 0 and
          args.progress_every >= 0, 'Invalid positive budget or angular limits')
    meta, raw, baseline, eta, old_upper, old_a, old_rho, storage_bindings = validate_inputs(args)
    check(budget > eta, 'Requested budget leaves no room under this fixed bridge transfer bound')
    total = len(raw['left'])
    selected = list(range(total)) if args.intervals is None else sorted(set(args.intervals))
    check(selected and all(0 <= i < total for i in selected), 'Invalid selected target intervals')
    # All heavy geometric construction stays lazy. A loose-budget inherited
    # full-domain check only hashes data and validates the exact partition.
    helper = module('prefix_angular_reviewed_local', HERE/'78718-prefix-metric-budget-storage-v2.py')
    backend, poly, I, P = helper.backend, helper.poly, helper.I, helper.P
    geom = None
    leaves, summaries = Rows(args.out, 'rows'), Rows(args.out, 'intervals')
    counts = dict(inherited_global=0, original_interval=0, angular=0, original_fallback=0)
    computed_intervals, arc_evaluations = 0, 0
    source_max, a_min, rho_min = Q(0), old_a, old_rho

    def transferred(bound):
        return Q(bound)*(1+eta)+eta

    def emit(index, left, right, depth, bound, kind, alo, rlo, candidate=None):
        nonlocal source_max, a_min, rho_min
        bound, alo, rlo = Q(bound), Q(alo), Q(rlo)
        target = transferred(bound)
        row = dict(interval=index, radial_local_left='0', radial_local_right='1',
            s_left_exact=str(Q(float(raw['left'][index]))), s_right_exact=str(Q(float(raw['right'][index]))),
            angle_variable='phi=3*psi; endpoints in units of pi', angle_pi_left=str(left), angle_pi_right=str(right),
            depth=depth, proof_kind=kind, source_metric_upper_exact=str(bound),
            exact_target_metric_upper_exact=str(target), a_lower_exact=str(alo), rho_lower_exact=str(rlo),
            target_met=target <= budget, candidate_arc=candidate)
        leaves.add(row); counts[kind] += 1
        source_max, a_min, rho_min = max(source_max, bound), min(a_min, alo), min(rho_min, rlo)

    for number, index in enumerate(selected):
        if args.progress_every and number and number % args.progress_every == 0:
            print(json.dumps(dict(progress_intervals=number, requested_intervals=len(selected),
                original_interval_evaluations=computed_intervals, angular_evaluations=arc_evaluations)), flush=True)
        if transferred(old_upper) <= budget:
            emit(index, Q(0), Q(2), 0, old_upper, 'inherited_global', old_a, old_rho)
            summaries.add(dict(interval=index, original_global_reused=True, original_interval_recomputed=False))
            continue
        if geom is None:
            common = module('prefix_angular_common_cut', HERE/'78718-prefix-common-cut-storage-v1.py')
            common.install(poly.base)
            geom = poly.base.ExactHermite(args.geometry)
        A, e, ep = [poly.target_scalar(raw, name, index) for name in ('a', 'e', 'ep')]
        cosine = P(I(np.array([[.5, 0., .5]])), -1, 0)
        sine = P(I(np.array([[.5, 0., -.5]])), -1, 1)
        rho, theta_s = P.scalar(1.)-e*cosine, ep*sine*backend.qbounds(Q(-1, 3))
        aa = A*A
        targets = [P.scalar(1.)+aa*theta_s*theta_s, aa*theta_s*rho, aa*rho*rho]
        actual = poly.geometry_coefficients(geom, float(raw['left'][index]), float(raw['right'][index]))
        residuals = [a-b for a, b in zip(actual, targets)]
        legacy = helper.traditional(A, e, ep, residuals)
        local_upper = min(old_upper, positive_binary(legacy['operator_upper'], 'recomputed interval upper', zero=True))
        local_a, local_rho = Q(legacy['a_lower']), Q(legacy['rho_lower'])
        check(local_a > 0 and local_rho > 0, 'Original interval denominator bound failed')
        computed_intervals += 1
        if transferred(local_upper) <= budget:
            emit(index, Q(0), Q(2), 0, local_upper, 'original_interval', local_a, local_rho)
            summaries.add(dict(interval=index, original_global_reused=False, original_interval_recomputed=True,
                               original_interval=legacy, angular_evaluations=0))
            continue
        pending = [(Q(2*k, args.initial_arcs), Q(2*(k+1), args.initial_arcs), 0)
                   for k in reversed(range(args.initial_arcs))]
        initial_max, evaluated, denied = Q(0), 0, 0
        while pending:
            left, right, depth = pending.pop()
            trig = trig_table(backend, 2*geom.M, left, right)
            av, rv = backend.value_range(A), backend.value_range(rho, trig)
            alo, rlo = Q(float(av.lo)), Q(float(np.min(rv.lo)))
            candidate = None
            if alo > 0 and rlo > 0:
                detail = helper.angular_bound(A, rho, theta_s, residuals, trig)
                arc_upper = positive_binary(detail['operator_upper'], 'angular interval upper', zero=True)
                candidate = dict(operator_upper_exact=str(arc_upper),
                                 component_abs_upper=detail['component_abs_upper'])
                if depth == 0:
                    initial_max = max(initial_max, arc_upper)
                chosen = min(local_upper, arc_upper)
            else:
                denied += 1
                chosen = local_upper
            evaluated += 1; arc_evaluations += 1
            if transferred(chosen) <= budget or depth == args.max_depth:
                if candidate is not None and Q(candidate['operator_upper_exact']) <= local_upper:
                    emit(index, left, right, depth, chosen, 'angular', alo, rlo, candidate)
                else:
                    emit(index, left, right, depth, local_upper, 'original_fallback', local_a, local_rho, candidate)
            else:
                middle = (left+right)/2
                pending.extend([(middle, right, depth+1), (left, middle, depth+1)])
        summaries.add(dict(interval=index, original_global_reused=False, original_interval_recomputed=True,
            original_interval=legacy, initial_uniform_arc_upper=record(initial_max) if denied == 0 else None,
            angular_evaluations=evaluated, local_denominator_failures=denied))
    leaves.flush(); summaries.flush()
    verified = verify_rows(args.out, leaves.files, raw, selected, eta, budget)
    check(verified['exact_target_max'] == transferred(source_max), 'Written maximum differs from computation')
    complete = selected == list(range(total))
    result = dict(status='complete-prefix-refinement' if complete else 'selected-interval-refinement-only',
        scope=__doc__, finished=True, script_sha256=sha(__file__), mathematical_source_sha256=SOURCES,
        inputs={key: dict(file=str(path), sha256=sha(path)) for key, path in
                {'geometry': args.geometry, 'target': args.target, 'baseline': args.baseline, 'bridge': args.bridge}.items()},
        geometry_sha256=sha(args.geometry), geometry_data_sha256=meta['data_sha256'],
        geometry_storage_bindings=storage_bindings,
        target_sha256=sha(args.target), target_data_sha256=baseline['target_data_sha256'],
        bridge_transfer_eta=record(eta), exact_target_transfer_formula='epsilon*(1+eta)+eta',
        requested_budget=record(budget), target_intervals=total, processed_intervals=len(selected),
        requested_intervals=None if complete else selected, initial_arcs=args.initial_arcs, maximum_bisection_depth=args.max_depth,
        row_files=leaves.files, interval_summary_files=summaries.files, exact_partition_reread_verified=True,
        requested_domain_covered=True, entire_prefix_covered=complete,
        selected_source_metric_upper=record(source_max), selected_exact_target_metric_upper=record(transferred(source_max)),
        target_met_on_requested_domain=transferred(source_max) <= budget,
        entire_prefix_target_met=complete and transferred(source_max) <= budget,
        minimum_a_lower=float(a_min), minimum_chart_rho_lower=float(rho_min),
        proof_leaf_counts=counts, leaves=verified['leaves'], worst_leaf=verified['worst'],
        original_interval_evaluations=computed_intervals, angular_evaluations=arc_evaluations,
        full_geometry_constructed=geom is not None, angular_Taylor_implemented=False, radial_refinement_performed=False,
        target_supplier_independently_reproved_here=False, exact_bridge_root_recomputed_here=False,
        conditional_on_reviewed_target_bridge_and_baseline=True, complete_closed_surface=False,
        fixed_g_convergence_gate_5_paid=False, seconds=time.monotonic()-started,
        peak_process_rss_bytes=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)*1024)
    if complete:
        # Compatible source-target field for the existing closed-budget
        # interface. Its eta transfer must still be applied exactly once.
        result['metric_operator_upper'] = float(source_max)
        result['exact_target_metric_operator_upper'] = record(transferred(source_max))
    payload = json.dumps(result, indent=2, allow_nan=False)+'\n'
    check(len(payload.encode()) < 1_000_000, 'Report metadata exceeds compact JSON limit')
    args.out.write_text(payload)
    print(json.dumps({key: result[key] for key in ('status', 'processed_intervals', 'leaves',
        'selected_source_metric_upper', 'selected_exact_target_metric_upper', 'target_met_on_requested_domain',
        'full_geometry_constructed', 'original_interval_evaluations', 'angular_evaluations', 'seconds')}))


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ('geometry', 'target', 'baseline', 'bridge', 'out'):
        ap.add_argument('--'+name, type=Path, required=True)
    ap.add_argument('--budget', required=True, help='Exact rational/decimal bound for the original exact target g')
    ap.add_argument('--intervals', type=int, nargs='+', help='Explicit local selection; omit for complete prefix coverage')
    ap.add_argument('--initial-arcs', type=int, default=128)
    ap.add_argument('--max-depth', type=int, default=4)
    ap.add_argument('--progress-every', type=int, default=100)
    run(ap.parse_args())
