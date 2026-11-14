#!/usr/bin/env python3
"""Replace unnecessarily wide w rows by a certified physical point bound.

For one exact physical interval J and one binary source point x*, let
R* enclose r(x*) and W* enclose w(x*).  If |dw/dr| <= K on the connecting
physical segment, then W* + [-K*d,K*d] encloses w(J), where d is the exact
maximum distance between endpoints of J and R*.  No inverse or source
branch is assumed exact.  The existing polynomial is retained unless
the constant point enclosure has smaller full-width working uncertainty.

The file does not change the physical partition or any wr coefficient.
Its output still needs the actual continuous metric/curvature consumer.
"""
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

from db6f_tail_interval_elementary import I, qbounds
from db6f_tail_interval_source import Jet
from db6f_tail_integrated import IntegratedTail


HERE = Path(__file__).resolve().parent
SUPPLIER = HERE / 'db6f-tail-background-packet-totalwidth.py'
SPEC = importlib.util.spec_from_file_location('db6f_point_supplier', SUPPLIER)
supplier = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(supplier)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw)


def load_packet(meta_path, meta):
    path = Path(meta['data_file'])
    if not path.is_absolute():
        path = meta_path.parent / path
    if sha(path) != meta['data_sha256']:
        raise ValueError('input packet data hash mismatch')
    raw = path.read_bytes()
    if raw[:2] == b'\x1f\x8b':
        raw = gzip.decompress(raw)
    with np.load(io.BytesIO(raw), allow_pickle=False) as data:
        arrays = {name: data[name].copy() for name in data.files}
    return path, arrays


def exact_width(lo, hi):
    return Q(float(hi)) - Q(float(lo))


def row_uncertainty(arrays, row):
    # This conservative work measure uses full coefficient widths.
    return Q(float(arrays['w_remainder'][row])) + sum(
        (exact_width(lo, hi) for lo, hi in
         zip(arrays['w_lo'][row], arrays['w_hi'][row])), Q(0))


def point_enclosure(background, rl, rr):
    profile = background.proposal_profile((rl + rr)/2)
    x = float(profile.approximate_inverse(float((rl + rr)/2)))
    if not np.isfinite(x) or not 0 <= x <= 1:
        raise ArithmeticError('point proposal leaves the source profile')
    radius_value = profile.point(x)
    value = background.source.evaluate(profile.n, profile.j,
                                       Jet.variable(I(x), 0))['w'].c[0]
    rlo, rhi = Q(float(radius_value.lo)), Q(float(radius_value.hi))
    distance = max(abs(a-b) for a in [rl, rr] for b in [rlo, rhi])
    # This test certifies the entire connection lies on the inner side.
    # The n label of the approximate proposal alone would not suffice.
    inner = (background.inner_threshold is not None and
             max(rr, rhi) <= Q(background.inner_threshold))
    bound = Q(601, 100) if inner else Q(24)
    error = qbounds(bound*distance)
    enclosure = value + I(-float(error.hi), float(error.hi))
    if not np.isfinite(float(enclosure.lo)) or not np.isfinite(float(enclosure.hi)):
        raise ArithmeticError('nonfinite point Lipschitz enclosure')
    return enclosure, {'source_cell': profile.n, 'source_segment': profile.j,
                       'source_x': x, 'physical_distance_upper': float(qbounds(distance).hi),
                       'derivative_bound_rational': [bound.numerator, bound.denominator]}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--packet', type=Path, required=True)
    ap.add_argument('--manifest', type=Path, required=True)
    ap.add_argument('--primitive', type=Path, required=True)
    ap.add_argument('--calibrations', type=Path, required=True)
    ap.add_argument('--out-prefix', type=Path, required=True)
    ap.add_argument('--minimum-width', type=float, default=1e-6)
    args = ap.parse_args()
    if not np.isfinite(args.minimum_width) or args.minimum_width < 0:
        raise ValueError('minimum working width must be finite and nonnegative')
    started = time.time()
    original = read(args.packet)
    if not original.get('finished'):
        raise ValueError('input packet selection is not finished')
    if (original.get('global_background_wr_absolute_bound') != 24 or
            original.get('background_curvature_bound') != 6):
        raise ValueError('packet lacks the reviewed background derivative-bound assumptions')
    if sha(args.manifest) != original['finite_tail_manifest_sha256']:
        raise ValueError('input packet belongs to another finite map')
    if sha(args.primitive) != original['primitive_sha256']:
        raise ValueError('input packet uses a different radial primitive')
    background = supplier.Background(args.primitive, args.calibrations)
    if original['background_definition_hashes'] != background.data['inputs']:
        raise ValueError('input packet background definition differs')
    tail = IntegratedTail(args.manifest)
    nodes = supplier.exact_nodes(tail)
    data_path, arrays = load_packet(args.packet, original)
    count = len(arrays['span_index'])
    if count != original['rows'] or any(len(x) != count for x in arrays.values()):
        raise ValueError('packet row counts differ')
    changes = []
    for row in range(count):
        span = int(arrays['span_index'][row])
        if span == -1:
            continue
        if not 0 <= span < len(nodes)-1:
            raise ValueError('invalid physical span index')
        ul, ur = Q(float(arrays['u_left'][row])), Q(float(arrays['u_right'][row]))
        if not Q(0) <= ul < ur <= Q(1):
            raise ValueError('invalid local physical interval')
        before = row_uncertainty(arrays, row)
        if before <= Q(args.minimum_width):
            continue
        length = nodes[span+1] - nodes[span]
        rl, rr = nodes[span]+length*ul, nodes[span]+length*ur
        replacement, detail = point_enclosure(background, rl, rr)
        after = exact_width(replacement.lo, replacement.hi)
        if after >= before:
            continue
        arrays['w_lo'][row].fill(0)
        arrays['w_hi'][row].fill(0)
        arrays['w_lo'][row, 0] = float(replacement.lo)
        arrays['w_hi'][row, 0] = float(replacement.hi)
        arrays['w_remainder'][row] = 0.
        changes.append({'row': row, 'span': span,
                        'u_left': float(ul), 'u_right': float(ur),
                        'old_total_width_upper': float(qbounds(before).hi),
                        'new_total_width_upper': float(qbounds(after).hi), **detail})
    output_path = supplier.write_npz(str(args.out_prefix), arrays)
    report = dict(original)
    report['status'] = 'point-lipschitz-background-packet-pending-independent-review'
    report['scope'] = __doc__
    report['parent_packet_file'] = str(args.packet)
    report['parent_packet_sha256'] = sha(args.packet)
    report['parent_data_file'] = str(data_path)
    report['parent_data_sha256'] = sha(data_path)
    report['data_file'] = output_path.name
    report['data_sha256'] = sha(output_path)
    report['files'] = [{'data_file': str(output_path), 'sha256': sha(output_path),
                        'rows': count, 'bytes': output_path.stat().st_size}]
    report['point_lipschitz'] = {'script_sha256': sha(__file__),
        'supplier_sha256': sha(SUPPLIER), 'minimum_working_width': args.minimum_width,
        'changed_rows': changes, 'physical_partition_unchanged': True,
        'all_wr_coefficients_and_remainders_unchanged': True,
        'original_auxiliary_source_and_radial_residual_columns_unchanged': True,
        'remaining_over_working_width': sum(row_uncertainty(arrays, k) > Q(args.minimum_width)
                                           for k in range(count))}
    report['maximum_w_total_uncertainty'] = max(
        float(qbounds(row_uncertainty(arrays, k)).hi) for k in range(count))
    report['maximum_w_remainder'] = float(np.max(arrays['w_remainder']))
    report['parent_unmet_tolerance_rows'] = original.get('unmet_tolerance_rows')
    report['unmet_tolerance_rows'] = None
    report['seconds'] = time.time()-started
    report['finished'] = True
    Path(str(args.out_prefix)+'.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({'finished': True, 'rows': count, 'changed_rows': len(changes),
                      'maximum_w_total_uncertainty': report['maximum_w_total_uncertainty'],
                      'remaining_over_working_width': report['point_lipschitz']['remaining_over_working_width'],
                      'seconds': report['seconds']}))


if __name__ == '__main__':
    main()
