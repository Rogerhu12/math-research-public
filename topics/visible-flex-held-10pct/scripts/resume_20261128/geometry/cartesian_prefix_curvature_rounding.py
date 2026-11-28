#!/usr/bin/env python3
"""Pay the exact rational 123/10 curvature budget of a complete new-map cover.

The first geometry pass uses a literal binary64 threshold. Its strictly
positive PSD determinant margin and a coarse proved metric-trace upper bound
permit a tiny exact rational decrease. This is an algebraic postprocessing of
the same complete interval data, not a rerun or a change to the finite map.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path
import sys

import numpy as np

SCRIPTS = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(SCRIPTS/'finite_closure/m3_m8_closed_map'))
import interval_geometry_kernel as K
from m3_interval_center import lift_weights


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def absolute(pair):
    return np.maximum(np.abs(pair[0]), np.abs(pair[1]))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--certificate', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    report = json.loads(args.certificate.read_text())
    if (report.get('status') != 'continuous_new_prefix_geometry_certified'
            or report.get('continuous_prefix_geometry_certified') is not True
            or report['failed_boxes'] != 0):
        raise ValueError('Require the actual complete new-map geometric cover')
    for path, digest in report['source_hashes'].items():
        if sha(path) != digest:
            raise ValueError('A bound continuous-cover source changed: '+path)
    folder = args.certificate.resolve().parent
    paths = [folder/'actual-prefix-exact-defining-jets.npz',
             folder/'actual-prefix-true-core-angular-ranges.npz']
    expected = [report['defining_jets_sha256'], report['true_core_angular_ranges_sha256']]
    if any(sha(path) != digest for path, digest in zip(paths, expected)):
        raise ValueError('The bound complete interval data changed')
    with np.load(paths[0], allow_pickle=False) as data:
        knots, jets, lift = (data[name].copy() for name in ('knots', 'jets', 'lift_jets'))
        pm, hm = data['planar_modes'].copy(), data['height_modes'].copy()
        width = float(data['center_width'])
    with np.load(paths[1], allow_pickle=False) as data:
        centers, angular_lifts = data['center'].copy(), data['lift'].copy()
    if not (jets.shape[0] == 3 and jets.shape[2] == len(knots)
            and lift.shape == (3, 1, len(knots))
            and centers.shape == (2, 3, 3, report['angular_boxes'], 3)
            and angular_lifts.shape == (3, 2, report['angular_boxes'], 3)):
        raise ValueError('Incomplete same-map Cartesian interval arrays')
    if not all(np.all(np.isfinite(x)) for x in (jets, lift, centers, angular_lifts)):
        raise ValueError('Nonfinite bound data')
    P = len(pm)
    first_bounds = []
    for radial, angular in ((1, 0), (0, 1)):
        bs = K.hermite_bernstein(knots, jets, radial)
        c = np.max(absolute(bs), axis=(0, 2))
        planar = K.interval_sum_terms(K.scale(K.exact(c[:P]), np.abs(pm)**angular), 0)[1]
        height = K.interval_sum_terms(K.scale(K.exact(c[P:]), np.abs(hm)**angular), 0)[1]
        value = K.exact(np.array([planar, planar, height]))
        bs = K.hermite_bernstein(knots, lift, radial)
        r = float(np.max(absolute(bs)))
        h = np.max(np.maximum(abs(angular_lifts[angular, 0]),
                              abs(angular_lifts[angular, 1])), axis=0)
        value = K.add(value, K.scale(K.exact(h), r))
        weights = lift_weights(np.array([0.]), np.array([width]), width, radial)
        wb = absolute(weights)[0]
        for j in range(3):
            d = np.max(np.maximum(abs(centers[0, angular, j]),
                                  abs(centers[1, angular, j])), axis=0)
            value = K.add(value, K.scale(K.exact(d), float(wb[j])))
        first_bounds.append(value[1])
    trace = K.exact(0.)
    for value in first_bounds:
        trace = K.add(trace, K.interval_sum_terms(K.square(K.exact(value)), 0))
    B = math.ceil(float(trace[1]))
    if B <= 0:
        raise ArithmeticError('A positive metric trace upper bound is required')
    old = Q.from_float(report['thresholds']['curvature'])
    target = Q(123, 10)
    determinant = Q.from_float(report['bounds']['curvature_psd_determinant_lower'])
    diagonal = Q.from_float(report['bounds']['curvature_psd_diagonal_lower'])
    if determinant <= 0 or diagonal <= 0:
        raise ArithmeticError('Strict complete PSD margins are required')
    epsilon = max(Q(0), old-target)
    eigen_lower = determinant/(2*old*B)
    remaining = eigen_lower-epsilon*B
    if remaining <= 0:
        raise ArithmeticError('The exact rational curvature threshold is unresolved')
    result = dict(status='same_new_prefix_exact_rational_curvature_budget_certified',
        source_certificate=str(args.certificate.resolve()), source_certificate_sha256=sha(args.certificate),
        source_sha256=sha(__file__), data_sha256={str(p): sha(p) for p in paths},
        exact_old_binary_curvature=str(old), exact_target_curvature=str(target),
        complete_metric_trace_integer_upper=B,
        complete_first_cartesian_jet_component_upper=[v.tolist() for v in first_bounds],
        exact_old_psd_determinant_lower=str(determinant),
        exact_parameter_coordinate_eigenvalue_lower=str(eigen_lower),
        exact_threshold_decrease=str(epsilon), exact_remaining_psd_lower=str(remaining),
        continuous_prefix_absolute_curvature_at_most_12p3=True,
        proof=('For A=K_old*g +/- II, positivity is already proved on every box. '
               'Since -K_old*g < II < K_old*g and trace(g)<=B, trace(A)<=2*K_old*B. '
               'Thus lambda_min(A)>=det(A)/trace(A)>=d/(2*K_old*B). '
               'Subtracting (K_old-123/10)*g costs at most epsilon*B; the exact '
               'remaining lower bound is positive.'),
        map_changed=False, metric_certificate=False, closed_surface=False)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    print(json.dumps({key: result[key] for key in ('status', 'complete_metric_trace_integer_upper',
          'exact_threshold_decrease', 'exact_remaining_psd_lower')}))


if __name__ == '__main__':
    main()
