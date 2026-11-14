#!/usr/bin/env python3
"""Continuous two-tail differences, including each exact R6 collar.

The physical radial partitions and ambient Fourier labels are merged.
Different retained mode counts are padded by exact zero.  The identical
rotational background cancels; its common identity remains an explicit
mathematical premise supported by the checked physical metadata and R21.
The closed upper-tail height gauge is reported separately.  No ODE, DN,
BVP or replacement of actual derivatives by source equations is involved.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'OMP_NUM_THREADS'):
    os.environ[_key] = '1'

import argparse
import bisect
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
spec = importlib.util.spec_from_file_location('fd2d_tail_difference_stream',
                                            HERE / 'db6f-audit-tail-stream.py')
stream = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = stream
spec.loader.exec_module(stream)
I, qbounds, stack = stream.I, stream.qbounds, stream.base.stack
up = stream.frozen.up

PHYSICAL_KEYS = (
    'rCut', 'wCut', 'width', 'curvatureBound', 'delta0', 'R', 'a',
    'etaPower', 'etaRatioAtN0', 'orientation', 'prefixR', 'prefixEnd',
    'prefixReturnStart', 'protectCell', 'calibrationSteps', 'warpSteps',
    'quadratureTolerance', 'slopeCap', 'capTransition', 'capMode',
    'cuspAwareQuadrature', 'valleyControls', 'pulseCaps', 'valleyCaps',
    'warpWeightLevels', 'rCuff', 'epsilonScale', 'flatOuterThroughCell',
    'flatOuterStartSegment', 'flatSlope', 'rejoinR20At', 'rejoinIndexOffset')
M12_SHA = 'cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104'


def identity(path):
    path = Path(path)
    return dict(file=str(path.resolve()), bytes=path.stat().st_size,
                sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def qvector(values):
    enclosed = [qbounds(v) for v in values]
    return I(np.array([float(x.lo) for x in enclosed])[:, None],
             np.array([float(x.hi) for x in enclosed])[:, None])


def affine_compose(coefficients, a, b):
    # coefficients: [batch, Fourier label, power].  Substitute t=a+b*u.
    degree = coefficients.lo.shape[-1] - 1
    ap, bp = [I(np.ones(a.lo.shape))], [I(np.ones(b.lo.shape))]
    for _ in range(degree):
        ap.append(ap[-1] * a)
        bp.append(bp[-1] * b)
    out = []
    for j in range(degree + 1):
        value = I(np.zeros(coefficients.lo.shape[:-1]))
        for k in range(j, degree + 1):
            value = value + coefficients[..., k] * math.comb(k, j) * ap[k-j]
        out.append(value * bp[j])
    return stack(out, -1)


def bernstein(coefficients):
    degree = coefficients.lo.shape[-1] - 1
    out = []
    for k in range(degree + 1):
        value = I(np.zeros(coefficients.lo.shape[:-1]))
        for j in range(k + 1):
            value = value + coefficients[..., j] * qbounds(Q(math.comb(k, j), math.comb(degree, j)))
        out.append(value)
    return stack(out, -1)


def coefficient_bounds(coefficients, modes, planar_count):
    b = bernstein(coefficients).abs().hi
    result = {}
    for angular_order in range(3):
        components = []
        for begin, end in ((0, planar_count), (planar_count, len(modes))):
            total = np.zeros((len(b), b.shape[-1]))
            for column in range(begin, end):
                weight = int(abs(modes[column]) ** angular_order)
                total = up(total + up(b[:, column, :] * weight))
            components.append(np.max(total, axis=1))
        result[angular_order] = (components[0], components[1],
                                 up(components[0] + components[1]))
    return result


class ComparedTail:
    def __init__(self, manifest, union_labels):
        self.geometry = stream.StreamingExactIntegratedTail(manifest)
        g = self.geometry
        self.nodes = [g.cuff] + list(g.rq)
        own_labels = ([('planar', int(m)) for m in g.reader.planar_modes]
                      + [('height', int(m)) for m in g.reader.height_modes])
        lookup = {key: index for index, key in enumerate(union_labels)}
        self.columns = np.array([lookup[label] for label in own_labels])
        self.width = len(union_labels)

    def block(self, intervals):
        rows = [[], [], []]
        alpha, beta = [], []
        for left, right in intervals:
            index = bisect.bisect_right(self.nodes, left) - 1
            if not (0 <= index < len(self.nodes)-1
                    and self.nodes[index] <= left < right <= self.nodes[index+1]):
                raise ValueError('The common interval is not contained in an own span')
            length = self.nodes[index+1] - self.nodes[index]
            alpha.append((left - self.nodes[index]) / length)
            beta.append((right - left) / length)
            raw = (self.geometry.collar if index == 0
                   else self.geometry.span_polys(index-1))
            for order in range(3):
                p = raw[order]
                low = np.zeros((self.width, p.lo.shape[0]))
                high = np.zeros_like(low)
                low[self.columns] = p.lo.T
                high[self.columns] = p.hi.T
                rows[order].append(I(low, high))
        a, b = qvector(alpha), qvector(beta)
        return [affine_compose(stack(group, 0), a, b) for group in rows]


def finite_upper(value):
    return float(np.max(value.hi))


def intrinsic_tail_bounds(report, old_meta, old_bounds, difference_bounds, prefix_mean_bound):
    """Use R21 only when the actual old manifest is the R21 first critical M12."""
    if report['old']['sha256'] != M12_SHA:
        return dict(status='NOT_APPLIED', reason='Old map is not the specified R21 M12 reference')
    cuff = Q(float(old_meta['parameters']['rCuff']))
    radius_max = Q(float(old_meta['parameters']['rCut']))
    old_relative_metric_bound = Q(3, 10**8)  # safely exceeds R21's complete bound
    m = qbounds((1-old_relative_metric_bound)*cuff*cuff)
    first = (I(difference_bounds['r1theta0']['total']).square()
             + I(difference_bounds['r0theta1']['total']).square()).sqrt()
    eta = first / m.sqrt()
    # Sum bounds are valid for the Euclidean bilinear operator norm.
    du2 = (I(difference_bounds['r2theta0']['total'])
           + 2*I(difference_bounds['r1theta1']['total'])
           + I(difference_bounds['r0theta2']['total']))
    # R21's identical rotational background has |w|<=16/15 and |kappa|<=6,
    # hence |w_r|<=6*(1+(16/15)^2)^(3/2)<19.  The other background jets
    # have norms |X_rtheta|=1 and |X_thetatheta|=r.
    old2 = (19 + I(old_bounds['r2theta0']['total'])
            + 2*(1 + I(old_bounds['r1theta1']['total']))
            + qbounds(radius_max) + I(old_bounds['r0theta2']['total']))
    beta = (du2 + eta * old2) / m
    out = dict(status='ACTUAL_TAIL_DERIVATIVE_COMPARISON_ON_REPORTED_COVERAGE',
               old_actual_metric_lower_eigenvalue=float(m.lo),
               old_metric_lower_eigenvalue_exact=str((1-old_relative_metric_bound)*cuff*cuff),
               eta_upper=finite_upper(eta), beta_upper=finite_upper(beta),
               raw_covariant_numerator_upper=finite_upper(du2 + eta*old2),
               old_coordinate_second_bilinear_upper=finite_upper(old2),
               formula='eta=||du||coord/sqrt(m); beta <= (||D2u||coord+eta*||D2X||coord)/m; dX Gamma_h=P_TX D2X',
               background_reference='R21 and notes/2026-11-09-db6f-audit-entire-background-curvature.md',
               positions_include_common_cut_gauge=False,
               closed_surface_geometric_transfer=False)
    if prefix_mean_bound is not None:
        eps = (qbounds(prefix_mean_bound)
               + I(difference_bounds['r0theta0']['planar'])
               + 2*I(difference_bounds['r0theta0']['height']))
        out.update(epsilon_closed_upper_tail_upper=finite_upper(eps),
                   prefix_mean_difference_supplied_exact=str(prefix_mean_bound),
                   position_formula='|Delta mean(prefix cut)|+|Delta Vh|+2 sup|Delta Vz|',
                   positions_include_common_cut_gauge=True,
                   position_bound_is_conditional_on_supplied_prefix_mean=True)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--old', type=Path, required=True)
    ap.add_argument('--new', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--batch', type=int, default=64)
    ap.add_argument('--limit', type=int)
    ap.add_argument('--rows', type=Path)
    ap.add_argument('--prefix-mean-difference-upper', type=Q)
    args = ap.parse_args()
    if args.out.exists() or (args.rows is not None and args.rows.exists()):
        raise FileExistsError('Use a new output name')
    if args.batch <= 0 or (args.limit is not None and args.limit <= 0):
        raise ValueError('Positive batch and optional limit required')
    if args.prefix_mean_difference_upper is not None and args.prefix_mean_difference_upper < 0:
        raise ValueError('Nonnegative prefix cut mean bound required')
    started = time.monotonic()
    metas = [json.loads(path.read_text()) for path in (args.old, args.new)]
    for key in PHYSICAL_KEYS:
        if metas[0]['parameters'].get(key) != metas[1]['parameters'].get(key):
            raise ValueError('Different physical background parameter: ' + key)
    planar = sorted({int(m) for meta in metas for m in meta['format']['planarModes']})
    height = sorted({int(m) for meta in metas for m in meta['format']['heightModes']})
    labels = [('planar', m) for m in planar] + [('height', m) for m in height]
    modes = planar + height
    tails = [ComparedTail(path, labels) for path in (args.old, args.new)]
    if (tails[0].nodes[0] != tails[1].nodes[0]
            or tails[0].nodes[-1] != tails[1].nodes[-1]):
        raise ValueError('Different exact cuff or outer radius')
    common = sorted(set(tails[0].nodes + tails[1].nodes))
    total = len(common)-1
    stop = min(total, args.limit) if args.limit is not None else total
    keys = [f'r{j}theta{k}' for j in range(3) for k in range(3-j)]
    summaries = [{key: dict(planar=0., height=0., total=0.) for key in keys}
                 for _ in range(2)]
    row_file = gzip.open(args.rows, 'wt', encoding='utf8') if args.rows else None
    try:
        for begin in range(0, stop, args.batch):
            end = min(stop, begin+args.batch)
            intervals = list(zip(common[begin:end], common[begin+1:end+1]))
            blocks = [tail.block(intervals) for tail in tails]
            own_rows = [dict(index=begin+k, left_exact=str(left), right_exact=str(right),
                             difference={}, old_perturbation={})
                        for k, (left, right) in enumerate(intervals)]
            for order in range(3):
                diff = blocks[1][order] - blocks[0][order]
                for side, coefficients in enumerate((diff, blocks[0][order])):
                    bounds = coefficient_bounds(coefficients, modes, len(planar))
                    for angular_order in range(3-order):
                        key = f'r{order}theta{angular_order}'
                        for component, values in zip(('planar', 'height', 'total'), bounds[angular_order]):
                            summaries[side][key][component] = max(summaries[side][key][component], float(np.max(values)))
                        for k in range(len(intervals)):
                            target = own_rows[k]['difference' if side == 0 else 'old_perturbation']
                            target[key] = {component: float(values[k]) for component, values
                                           in zip(('planar', 'height', 'total'), bounds[angular_order])}
            if row_file:
                for row in own_rows:
                    row_file.write(json.dumps(row, separators=(',', ':'), allow_nan=False)+'\n')
            if begin == 0 or end == stop or end % (16*args.batch) == 0:
                print(json.dumps(dict(event='tail-difference-progress', done=end, total=stop,
                                      seconds=time.monotonic()-started)), flush=True)
    finally:
        if row_file:
            row_file.close()
    report = dict(status='CONTINUOUS_ACTUAL_TAIL_DIFFERENCE', old=identity(args.old),
                  new=identity(args.new), script=identity(__file__),
                  sources={name: identity(HERE/name) for name in
                           ('db6f-audit-tail-stream.py', 'db6f-audit-tail-metric-curvature.py',
                            'db6f_tail_integrated.py', 'db6f-audit-metric-polynomial.py',
                            'db6f-audit-continuous-hermite.py')},
                  exact_domain=[str(common[0]), str(common[-1])],
                  common_spans_total=total, covered_spans=stop,
                  entire_tail_and_own_collar_covered=stop == total,
                  includes_each_own_R6_collar=True, physical_parameters_checked=list(PHYSICAL_KEYS),
                  common_rotational_background_identity_is_mathematical_premise=True,
                  difference_bounds=summaries[0], old_perturbation_bounds=summaries[1],
                  union_planar_modes=planar, union_height_modes=height,
                  angular_sampling_used=False, finite_comparison_only=True,
                  new_isometric_solution=False, whole_surface_metric=False,
                  seconds=time.monotonic()-started)
    report['intrinsic_comparison'] = intrinsic_tail_bounds(
        report, metas[0], summaries[1], summaries[0], args.prefix_mean_difference_upper)
    if args.rows:
        report['continuous_rows'] = identity(args.rows)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(output=str(args.out), covered=stop, total=total,
                          difference_bounds={key: value['total'] for key, value in summaries[0].items()},
                          intrinsic=report['intrinsic_comparison'], seconds=report['seconds']), indent=2))


if __name__ == '__main__':
    main()
