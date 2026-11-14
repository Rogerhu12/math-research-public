#!/usr/bin/env python3
"""Reuse a complete finite-map height sensitivity certificate for a new w packet.

Only certified upper bounds are reused, on a superset of every physical
overlap. The target finite map is the one named by the sensitivity report,
not the map whose grid indexes the new packet. This is a separate w-width
budget, not a residual certificate or evidence for a different finite map.
"""
import argparse
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
spec = importlib.util.spec_from_file_location('reuse_grid', HERE/'db6f-root-transfer-background.py')
transfer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(transfer)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_data(path, expected):
    raw = path.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == expected
    return gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ['packet', 'source-manifest', 'sensitivity', 'out']:
        ap.add_argument('--'+name, type=Path, required=True)
    ap.add_argument('--budget', default='2e-10')
    args = ap.parse_args()
    budget = Q(args.budget)
    assert budget > 0
    packet = json.loads(args.packet.read_text())
    assert packet['finished'] is True
    assert packet['finite_tail_manifest_sha256'] == sha(args.source_manifest)
    source_meta, nodes = transfer.grid(args.source_manifest)
    sensitivity = json.loads(args.sensitivity.read_text())
    target_manifest = Path(sensitivity['manifest'])
    assert sha(target_manifest) == sensitivity['manifest_sha256']
    target_meta = json.loads(target_manifest.read_text())
    p, q = source_meta['parameters'], target_meta['parameters']
    assert all(p.get(k) == q.get(k) for k in set(p)|set(q)
               if k not in transfer.NUMERICAL_KEYS)
    row_path = args.sensitivity.parent/sensitivity['row_file']
    old = json.loads(read_data(row_path, sensitivity['row_sha256']))
    assert len(old) == sensitivity['checked_rows']
    # These endpoints are nearest-binary evaluations of exact Fractions in
    # the reviewed diagnostic. One outward nextafter contains each exact
    # endpoint and therefore cannot discard a real intersection.
    left = np.array([np.nextafter(d['r_left'], -np.inf) for d in old])
    right = np.array([np.nextafter(d['r_right'], np.inf) for d in old])
    weight = np.array([d['residual_sensitivity_upper'] for d in old])
    assert np.isfinite(left).all() and np.isfinite(right).all()
    assert np.isfinite(weight).all() and np.all(weight >= 0)
    data_path = args.packet.parent/packet['data_file']
    with np.load(io.BytesIO(read_data(data_path, packet['data_sha256'])), allow_pickle=False) as data:
        arrays = {k: data[k].copy() for k in data.files}
    rows = []
    for row, span_value in enumerate(arrays['span_index']):
        span = int(span_value)
        assert -1 <= span < len(nodes)-2
        a, b = Q(float(arrays['u_left'][row])), Q(float(arrays['u_right'][row]))
        assert 0 <= a < b <= 1
        origin, length = nodes[span+1], nodes[span+2]-nodes[span+1]
        lo, hi = origin+length*a, origin+length*b
        assert Q(q['rCuff']) <= lo < hi <= Q(q['rCut'])
        mask = ((right >= float(transfer.fraction_vectors([lo]).lo[0]))
                & (left <= float(transfer.fraction_vectors([hi]).hi[0])))
        assert np.any(mask)
        widths = [Q(float(y))-Q(float(x)) for x, y in
                  zip(arrays['w_lo'][row], arrays['w_hi'][row])]
        assert all(x >= 0 for x in widths)
        rem = Q(float(arrays['w_remainder'][row]))
        assert rem >= 0
        delta = rem+sum(widths, Q(0))/2
        W = Q(float(np.max(weight[mask])))
        cost = delta*W
        rows.append(dict(row=row, span=span, u_left=float(a), u_right=float(b),
            delta_w_upper=float(transfer.fraction_vectors([delta]).hi[0]),
            sensitivity_upper=float(W),
            metric_uncertainty_budget_upper=float(transfer.fraction_vectors([cost]).hi[0]),
            above_requested_budget=cost > budget))
    report = dict(status='conditional-width-budget-for-the-named-sensitivity-map', scope=__doc__,
        script_sha256=sha(Path(__file__)), packet_sha256=sha(args.packet),
        packet_data_sha256=sha(data_path), source_manifest_sha256=sha(args.source_manifest),
        target_finite_manifest=str(target_manifest), target_finite_manifest_sha256=sha(target_manifest),
        sensitivity_report_sha256=sha(args.sensitivity), sensitivity_rows_sha256=sha(row_path),
        requested_budget_exact=str(budget), rows=rows,
        maximum_budget_upper=max(x['metric_uncertainty_budget_upper'] for x in rows),
        rows_above_budget=sum(x['above_requested_budget'] for x in rows),
        complete_metric_certified=False, background_supplier_certified_here=False,
        valid_for_other_finite_maps=False)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps({k: report[k] for k in ['status', 'maximum_budget_upper', 'rows_above_budget']}))


if __name__ == '__main__':
    main()
