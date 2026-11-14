#!/usr/bin/env python3
"""Independently check the four point replacements and their metric budget.

This audits the frozen raw2 artifacts. The sensitivity report concerns the
M12 uniform finite map only; it is not a metric residual certificate and is
not transferred to either adaptive finite map.
"""
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from db6f_tail_interval_elementary import I, qbounds
from db6f_tail_interval_source import Jet
from db6f_tail_integrated import IntegratedTail

TOPIC = HERE.parent
NOTES = TOPIC/'notes'
STEM = '2026-11-09-db6f-'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(name):
    path = NOTES/(STEM+name)
    raw = path.read_bytes()
    return path, json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw)


def arrays(path, meta):
    data_path = path.parent/meta['data_file']
    assert sha(data_path) == meta['data_sha256']
    raw = data_path.read_bytes()
    if raw[:2] == b'\x1f\x8b':
        raw = gzip.decompress(raw)
    with np.load(io.BytesIO(raw), allow_pickle=False) as data:
        return {k: data[k].copy() for k in data.files}


def main():
    old_path, old = read('tail-background-lowmetric-raw2.json')
    new_path, new = read('tail-background-lowmetric-raw2-point.json')
    replay_path, replay = read('audit-raw2-point-replay.json')
    aa, bb, cc = [arrays(p, d) for p, d in [(old_path, old), (new_path, new), (replay_path, replay)]]
    assert aa.keys() == bb.keys() == cc.keys()
    assert all(np.array_equal(bb[k], cc[k]) for k in bb)
    assert new['point_lipschitz'] == replay['point_lipschitz']
    changed = [int(x['row']) for x in new['point_lipschitz']['changed_rows']]
    assert len(changed) == 4 and len(set(changed)) == 4
    for key in aa:
        if key in ['w_lo', 'w_hi', 'w_remainder']:
            keep = np.ones(len(aa[key]), dtype=bool)
            keep[changed] = False
            assert np.array_equal(aa[key][keep], bb[key][keep])
        else:
            assert np.array_equal(aa[key], bb[key])

    # This rational comparison pays the inner background derivative bound.
    assert Q(36)*(1+Q(1, 49**2))**3 < Q(601, 100)**2
    supplier_path = HERE/'db6f-tail-background-packet-totalwidth.py'
    spec = importlib.util.spec_from_file_location('audit_point_source', supplier_path)
    supplier = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(supplier)
    primitive = NOTES/(STEM+'tail-background-primitive-stable-depth4.json.gz')
    calibration = NOTES/(STEM+'tail-finite-source-calibrations.json')
    background = supplier.Background(primitive, calibration)
    manifest = NOTES/(STEM+'tail-int2-flat17-m8-q10-n8-s32-manifest.json')
    tail = IntegratedTail(manifest)
    nodes = supplier.exact_nodes(tail)
    primitive_checks = []
    for detail in new['point_lipschitz']['changed_rows']:
        row, span = detail['row'], detail['span']
        lo = nodes[span]+(nodes[span+1]-nodes[span])*Q(float(bb['u_left'][row]))
        hi = nodes[span]+(nodes[span+1]-nodes[span])*Q(float(bb['u_right'][row]))
        source = next(p for p in background.profiles
                      if (p.n, p.j) == (detail['source_cell'], detail['source_segment']))
        x = detail['source_x']
        assert 0 <= Q(x) <= 1
        rp = source.point(x)
        wp = background.source.evaluate(source.n, source.j, Jet.variable(I(x), 0))['w'].c[0]
        distances = [abs(s-t) for s in [lo, hi] for t in [Q(float(rp.lo)), Q(float(rp.hi))]]
        distance = max(distances)
        K = Q(*detail['derivative_bound_rational'])
        assert K in [Q(601, 100), Q(24)]
        if K == Q(601, 100):
            assert max(hi, Q(float(rp.hi))) <= Q(background.inner_threshold)
        assert Q(float(bb['w_lo'][row, 0])) <= Q(float(wp.lo))-K*distance
        assert Q(float(bb['w_hi'][row, 0])) >= Q(float(wp.hi))+K*distance
        assert np.all(bb['w_lo'][row, 1:] == 0) and np.all(bb['w_hi'][row, 1:] == 0)
        assert bb['w_remainder'][row] == 0
        primitive_checks.append(dict(row=row, span=span, exact_corner_distance_check=True,
                                     exact_constant_inclusion_check=True,
                                     derivative_bound_rational=[K.numerator, K.denominator]))

    budget_path, budgets = read('audit-background-metric-budget-m12.rows.json.gz')
    bleft = np.array([np.nextafter(d['r_left'], -np.inf) for d in budgets])
    bright = np.array([np.nextafter(d['r_right'], np.inf) for d in budgets])
    sensitivities = np.array([d['residual_sensitivity_upper'] for d in budgets])
    _, unmet = read('tail-background-lowmetric-raw2-unmet.json')
    budget_checks = []
    for item in unmet['bad']:
        row, span = item['row'], item['span']
        lo = nodes[span]+(nodes[span+1]-nodes[span])*Q(float(bb['u_left'][row]))
        hi = nodes[span]+(nodes[span+1]-nodes[span])*Q(float(bb['u_right'][row]))
        # Expanded binary endpoints select a superset of every physical
        # overlap. Each stored sensitivity bounds the whole M12 base span.
        mask = (bright >= float(qbounds(lo).lo)) & (bleft <= float(qbounds(hi).hi))
        assert np.any(mask)
        sensitivity = Q(float(np.max(sensitivities[mask])))
        width = Q(float(bb['w_remainder'][row])) + sum(
            (Q(float(y))-Q(float(x)) for x, y in zip(bb['w_lo'][row], bb['w_hi'][row])), Q(0))/2
        value = width*sensitivity
        budget_checks.append(dict(span=span, row=row, delta_w_upper=float(qbounds(width).hi),
            sensitivity_upper=float(sensitivity), metric_uncertainty_budget_upper=float(qbounds(value).hi),
            below_two_e_minus_ten=value < Q(2, 10**10)))

    report = dict(status='PASS-method-rational-inclusion-and-complete-replay',
        source_script_sha256=sha(HERE/'db6f-tail-background-point-lipschitz.py'),
        source_note_sha256=sha(NOTES/(STEM+'tail-background-point-lipschitz.md')),
        input_packet_sha256=sha(old_path), output_packet_sha256=sha(new_path),
        replay_packet_sha256=sha(replay_path), all_output_arrays_identical=True,
        all_non_w_arrays_bitwise_unchanged=True, all_other_w_rows_bitwise_unchanged=True,
        total_rows=len(bb['span_index']), changed_rows=primitive_checks,
        inner_derivative_rational_inequality_checked=True,
        uniform_m12_sensitivity_rows_sha256=sha(budget_path),
        six_former_working_width_misses=budget_checks,
        scope='Point packages for the same frozen g. Sensitivity budget is for M12 uniform only; '
              'no complete metric residual, adaptive-grid bound, curvature or G5 claim.',
        script_sha256=sha(Path(__file__)))
    output = NOTES/(STEM+'audit-point-lipschitz-check.json')
    output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(dict(status=report['status'], rows=report['total_rows'], changed=len(changed),
        max_six_budget=max(x['metric_uncertainty_budget_upper'] for x in budget_checks),
        all_six_below_2e_10=all(x['below_two_e_minus_ten'] for x in budget_checks))))


if __name__ == '__main__':
    main()
