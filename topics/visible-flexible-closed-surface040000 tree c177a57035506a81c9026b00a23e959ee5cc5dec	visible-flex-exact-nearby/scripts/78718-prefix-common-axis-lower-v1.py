#!/usr/bin/env python3
"""Exact point rejection for an ACTUAL common-cut prefix and exact bridge.

Read-only: no candidate solver, tail solve, exporter, or geometry producer.
The exact lower applies to every extension retaining this fixed prefix.  It
does not assert that a complete closed surface or an infinite tail exists.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import time

import numpy as np

HERE = Path(__file__).resolve().parent
SOURCE_SHA256 = {
    '78718-prefix-nodal-axis-lower-v1.py': '661bc0daf17b303cfc3c093b9f913b9f003f68f0463b24bda0557ad72c48cbf8',
    'db6f-root-exact-bridge.py': 'f5d10784f58fa5008220354665de710ab4991b795f1b902e26a70ca44f382fd1',
    'db6f_tail_integrated.py': '4714e67860c80ecffc691d0d1e797bf5e8fa62062a4292730646abdf7f6e87ae',
    '78718-production-stage-record-v1.py': '4c87bc4496ddeb14c66310777c3b7c98e78d19df70cfb94f5971699999ac2dc9',
}
BUDGET = Q(1, 500_000_000)


def require(value, message):
    if not value:
        raise ValueError(message)


def identity(path):
    path = Path(path).resolve()
    content = path.read_bytes()
    return {'path': str(path), 'bytes': len(content),
            'sha256': hashlib.sha256(content).hexdigest()}


def verify(row):
    path = row.get('path', row.get('file'))
    actual = identity(path)
    require(actual['bytes'] == row['bytes'] and actual['sha256'] == row['sha256'],
            'Changed bound file: '+str(path))
    return actual


def module(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE/filename)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def read(path):
    return json.loads(Path(path).read_text())


def run(args):
    started = time.monotonic()
    require(not args.out.exists(), 'Refuse to replace a prior exact report')
    sources = []
    for name, expected in SOURCE_SHA256.items():
        row = identity(HERE/name)
        require(row['sha256'] == expected, 'Changed defining source: '+name)
        sources.append(row)
    old = module('common_axis_prior_exact_point', '78718-prefix-nodal-axis-lower-v1.py')
    for name, expected in old.SOURCE_SHA256.items():
        row = identity(HERE/name)
        require(row['sha256'] == expected, 'Changed exact prefix definition: '+name)
        sources.append(row)
    storage = module('common_axis_lossless_storage', '78718-prefix-storage-v1.py')
    bridge_code = module('common_axis_exact_bridge', 'db6f-root-exact-bridge.py')
    paths = [args.common_map, args.geometry, args.target, args.metric_certificate,
             args.tail_manifest, args.bridge, args.point_report, args.common_observation]
    inputs = [identity(p) for p in paths]
    common, target, metric, tail, bridge, prior, observed = [read(p) for p in
        [args.common_map, args.target, args.metric_certificate, args.tail_manifest,
         args.bridge, args.point_report, args.common_observation]]
    base, payload, data_bindings = storage.read_payload(args.geometry, verify_arrays=True)
    inputs.extend(verify(row) for row in data_bindings)
    inputs.extend(verify(row) for row in prior['input_bindings'])
    require(prior['schema'] == '78718-prefix-nodal-axis-exact-lower-v1' and
            prior['script']['sha256'] == SOURCE_SHA256['78718-prefix-nodal-axis-lower-v1.py'],
            'Unexpected previous exact point report')
    for row in prior['source_bindings']:
        verify(row)
    require(common['representation'] == 'exact-common-cut-prefix' and
            common['common_cut_implementation_sha256'] == old.SOURCE_SHA256['78718-prefix-common-cut-storage-v1.py'] and
            common['tail_reader_sha256'] == SOURCE_SHA256['db6f_tail_integrated.py'] and
            common['exact_common_cut_C2_by_definition'] is True,
            'Different common-cut definition')
    bound_pairs = [(args.geometry, common['base_geometry'], common['base_geometry_sha256']),
                   (args.tail_manifest, common['tail_manifest'], common['tail_manifest_sha256']),
                   (args.bridge, common['bridge_parameter_certificate'], common['bridge_parameter_certificate_sha256'])]
    for path, named_path, digest in bound_pairs:
        require(Path(path).resolve() == Path(named_path).resolve() and
                identity(path)['sha256'] == digest, 'Common-cut input identity mismatch')
    require(base['ell'] == 0. and base['mirror_inlet_C2_exact'] is True and
            common['nodes'] == base['nodes'] and common['modes'] >= base['modes'],
            'Different base dimensions or inlet definition')
    for key, path in [('geometry_sha256', args.geometry), ('target_sha256', args.target),
                      ('tail_manifest_sha256', args.tail_manifest),
                      ('metric_certificate_sha256', args.metric_certificate)]:
        require(bridge[key] == identity(path)['sha256'], 'Bridge input mismatch: '+key)
    require(target['geometry_sha256'] == identity(args.geometry)['sha256'] and
            metric['geometry_sha256'] == identity(args.geometry)['sha256'] and
            metric['target_sha256'] == identity(args.target)['sha256'],
            'Frozen target/metric identity mismatch')
    require(bridge['script_sha256'] == SOURCE_SHA256['db6f-root-exact-bridge.py'] and
            bridge['unique_root_in_box'] is True, 'Wrong exact bridge source or status')
    # Reverify the rational root enclosure without its untrusted Decimal seed.
    b = bridge_code
    c = Q.from_float(tail['parameters']['rCut'])
    w = Q.from_float(tail['parameters']['wCut'])
    require(Q(59,100) < c < Q(61,100) and w == Q(1,2), 'Wrong physical cut')
    pi = 16*b.atan(Q(1,5))-4*b.atan(Q(1,239))
    pt = b.hull(pi/2-b.atan(w))
    ps = b.hull((-7*w/c)/(b.J(1+w*w)*b.sqrtq(1+w*w)))
    L = b.J(Q(bridge['exact_L']['lo']), Q(bridge['exact_L']['hi']))
    require(L.lo < L.hi and b.enc(pt) == bridge['exact_pt'] and
            b.enc(ps) == bridge['exact_ps'], 'Changed bridge phase intervals')
    peak = b.phase_upper(L, pt, ps)
    left, right = b.gap(L.lo, pt, ps, c), b.gap(L.hi, pt, ps, c)
    require(peak < pi.lo/2 and Q(3,5) < L.lo < L.hi < Q(7,10) and
            left.hi < 0 < right.lo and pt.lo > 1 and ps.hi < 0 and pi.hi < 4,
            'Rational bridge root proof failed')
    require(b.enc(left) == bridge['gap_at_left'] and b.enc(right) == bridge['gap_at_right'] and
            bridge['gap_derivative_lower_exact'] == '1/8', 'Bridge root proof record changed')
    lam = Q(target['frozen_total_end'])/(Q(target['exact_prefix_end'])+L)
    require(lam.lo > 0 and b.enc(lam) == bridge['arclength_rescale'], 'Arclength scale mismatch')
    # The true tool observation records the actual successful producer, but
    # the inequality below is proved again from its unchanged defining bytes.
    require(observed['status'] == 'observed-process-completed' and
            observed['stage_id'] == 'common-cut' and observed['actual_exit_code'] == 0 and
            observed['observer'] == '/root/numerical_recovery' and
            bool(observed['tool_receipt']) and observed['expected_outputs_present'] is True,
            'Missing genuine successful common-cut producer observation')
    recorded_files = {r['path']: verify(r) for r in observed['files_after']}
    require(str(args.common_map.resolve()) in recorded_files and
            str(args.bridge.resolve()) in recorded_files and
            str(args.tail_manifest.resolve()) in recorded_files,
            'Producer did not close these exact outputs')
    inputs.extend(recorded_files.values())
    for path, digest in [(base['checkpoint'], base['checkpoint_sha256']),
                         (tail['input'], tail['inputSHA256'])]:
        row = identity(path)
        require(row['sha256'] == digest, 'Changed original CP or own tail packet')
        inputs.append(row)
    with np.load(io.BytesIO(gzip.decompress(payload)), allow_pickle=False) as raw:
        mesh, jets = raw['mesh'], raw['jets']
    require(jets.shape == (3, base['nodes'], 3*base['modes']+2) and
            mesh.shape == (base['nodes'],) and np.isfinite(jets).all() and
            np.isfinite(mesh).all() and np.all(np.diff(mesh)>0), 'Bad defining prefix arrays')
    start, node = common['correction_start_index'], prior['witness']['native_node_index']
    require(type(start) is int and type(node) is int and 0 < node < start < len(mesh)-1,
            'Witness is not strictly before the actual correction support')
    require(common['correction_width_requested'] == .15 and
            start == int(np.searchsorted(mesh, mesh[-1]-.15)), 'Changed support rule')
    axis = prior['witness']['psi_exact']
    require(axis in ('0', 'pi/3'), 'Not an exact symmetry axis')
    point = old.nodal_axis(jets, node, base['modes'], axis == 'pi/3')
    require(str(point['E']) == prior['witness']['metric_ss']['exact'] and
            str(Q.from_float(float(mesh[node]))) == prior['witness']['s']['exact'],
            'Saved exact point does not recompute from this common-map base')
    # For frozen radial coordinate sigma=lambda*s, F_*s=lambda F_sigma.
    # At either symmetry axis the angular chart's radial derivative vanishes,
    # and the final target g_ss is exactly 1.
    lower, upper = lam.lo*lam.lo*point['E']-1, lam.hi*lam.hi*point['E']-1
    require(0 < lower <= upper, 'This positive-signed Rayleigh argument is inapplicable')
    report = {
        'schema': '78718-common-prefix-exact-axis-lower-v1',
        'status': 'ACTUAL_COMMON_PREFIX_EXCEEDS_ORIGINAL_2E_MINUS_9',
        'script': identity(__file__),
        'source_bindings': list({r['path']:r for r in sources}.values()),
        'input_bindings': list({r['path']:r for r in inputs}.values()),
        'witness_node': node, 'axis_exact': axis,
        'frozen_coordinate_exact': str(Q.from_float(float(mesh[node]))),
        'actual_correction_start_index': start,
        'actual_correction_start_exact': str(Q.from_float(float(mesh[start]))),
        'base_metric_ss_exact': str(point['E']), 'arclength_rescale': b.enc(lam),
        'final_target_metric_ss_exact': '1',
        'final_signed_metric_ss_difference_enclosure': {
            'lower_exact': str(lower), 'upper_exact': str(upper),
            'lower_display': old.rational_bounds(lower)['lower'],
            'upper_display': old.rational_bounds(upper)['upper']},
        'original_budget_exact': str(BUDGET),
        'exceeds_original_budget': lower > BUDGET,
        'bridge_exact_root_reverified': True,
        'common_cut_support_identity_verified': True,
        'scope': {
            'actual_common_cut_prefix_definition': True,
            'final_exact_bridge_target': True,
            'every_extension_preserving_this_prefix_fails_original_budget': lower > BUDGET,
            'complete_closed_surface_constructed_or_certified': False,
            'no_go_for_other_candidate_or_exact_infinite_isometry': False},
        'solver_calls': 0, 'tail_calls': 0, 'geometry_producer_calls': 0,
        'seconds': time.monotonic()-started}
    for row in [report['script'], *report['source_bindings'], *report['input_bindings']]:
        require(identity(row['path']) == row, 'Defining bytes changed during exact verification')
    require(report['exceeds_original_budget'], 'This point does not reject the original budget')
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True)+'\n')
    print(json.dumps({'status': report['status'], 'output': identity(args.out),
        'point_lower': report['final_signed_metric_ss_difference_enclosure']['lower_display'],
        'exceeds_original_budget': True, 'witness_node': node,
        'actual_correction_start_index': start, 'solver_calls': 0}, sort_keys=True))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for option in ['common-map', 'geometry', 'target', 'metric-certificate',
                   'tail-manifest', 'bridge', 'point-report', 'common-observation', 'out']:
        p.add_argument('--'+option, type=Path, required=True)
    run(p.parse_args())


if __name__ == '__main__':
    main()
