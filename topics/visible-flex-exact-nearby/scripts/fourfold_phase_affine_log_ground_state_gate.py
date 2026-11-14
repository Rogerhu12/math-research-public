#!/usr/bin/env python3
"""Uniform real ground-state/log gate for one exact affine R57 parameter box."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

import numpy as np

from fourfold_phase_root_interval import Box


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inputs', type=Path, required=True)
    ap.add_argument('--frozen-direction', type=Path, required=True)
    ap.add_argument('--scalar-certificate', type=Path, required=True)
    ap.add_argument('--core-certificate', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    scalar = json.loads(args.scalar_certificate.read_text())
    core = json.loads(args.core_certificate.read_text())
    origin_sha, direction_sha = digest(args.inputs), digest(args.frozen_direction)
    config = core['configuration']
    if (scalar['origin_inputs_sha256'] != origin_sha
            or config['origin_inputs_sha256'] != origin_sha
            or scalar['frozen_direction_sha256'] != direction_sha
            or config['frozen_direction_sha256'] != direction_sha):
        raise ValueError('both certificates must refer to the same exact affine family')
    if (scalar['exact_parameter_interval'] != config['parameter_interval']
            or scalar['radial_core'] != core['radial_core']
            or not scalar['gate_passed'] or not core['complete']
            or not core['exact_dyadic_radial_coverage'] or core['pending'] or core['failed_cells']):
        raise ValueError('matching parameter intervals and completed real cores are required')
    cells = sorted(core['cells'], key=lambda row: row['radial_interval'][0])
    cursor, end = Fraction(0), Fraction.from_float(core['radial_core'][1])
    for row in cells:
        left, right = map(Fraction.from_float, row['radial_interval'])
        if left != cursor or not left < right <= end or not row['passed']:
            raise ValueError('actual geometric cells have a gap or failed gate')
        cursor = right
    if cursor != end:
        raise ValueError('actual geometric cells do not cover the core')
    with np.load(args.inputs, allow_pickle=False) as frozen:
        highest_frequency = 4*frozen['phase_coefficients'].shape[1]
    arange = np.asarray(scalar['circumference_radius_derivative_ranges'])
    a0, a1, a2 = map(Box, np.maximum(abs(arange[:, 0]), abs(arange[:, 1])))
    g0, g1, g2 = map(Box, scalar['gamma_field_absolute_derivative_bounds'])
    qmin, qmax = Box(scalar['Fz_over_x_lower']), Box(scalar['Fx_vertical_upper'])
    qt, qx = Box(scalar['quotient_angular_Lipschitz_upper']), Box(scalar['quotient_radial_Lipschitz_upper'])
    fmin, fmax = Box(core['support_lower']), Box(core['F_norm_upper'])
    fxmax = Box(core['Fx_norm_upper'])
    tx = Box(max(row['tangent_x_norm_upper'] for row in cells))
    tt = Box(max(row['tangent_theta_norm_upper'] for row in cells))
    if min(float(qmin.lo), float(fmin.lo)) <= 0:
        raise ValueError('positive Q and |F| are necessary for the log quotient')
    qtt = a0*highest_frequency*g1
    qxt = (a2*g0+2*a1*g1+a0*(g2+g0*g1*g1))/2
    ell = qt/qmin+a0/fmin
    ell_theta = qtt/qmin+qt*qt/(qmin*qmin)+3*a0*a0/(fmin*fmin)+a0*tt/fmin
    fx_theta = a1+a0*tx
    ell_x = qxt/qmin+qx*qt/(qmin*qmin)+3*fxmax*a0/(fmin*fmin)+fx_theta/fmin
    report = dict(kind='uniform_real_ground_state_log_gate_for_exact_affine_R57_family',
        origin_inputs_sha256=origin_sha, frozen_direction_sha256=direction_sha,
        source_sha256=digest(Path(__file__)),
        certificate_sha256={str(path): digest(path) for path in
                           [args.scalar_certificate, args.core_certificate]},
        dependency_sha256={'fourfold_phase_root_interval.py': digest(
            Path(__file__).with_name('fourfold_phase_root_interval.py'))},
        exact_parameter_interval=scalar['exact_parameter_interval'],
        exact_parameter_fractions=scalar['exact_parameter_fractions'],
        radial_core=core['radial_core'],
        Q_lower=float(qmin.lo), Q_upper=float(qmax.hi),
        F_norm_lower=float(fmin.lo), F_norm_upper=float(fmax.hi),
        ground_factor_lower=float((qmin/fmax).lo),
        ground_factor_upper=float((qmax/fmin).hi),
        ell_absolute_upper=float(ell.hi),
        ell_theta_absolute_upper=float(ell_theta.hi),
        ell_x_absolute_upper=float(ell_x.hi),
        quotient_theta2_absolute_upper=float(qtt.hi),
        quotient_x_theta_absolute_upper=float(qxt.hi),
        exact_definitions='Q=Fz/x by continuous extension; gstar=Q/|F|>0; uz=x*gstar; ell=dtheta log(gstar)',
        exact_identity='(dtheta-ell) uz=0, including the waist x=0',
        radial_regularity=('F is C4 intersect W5,infinity; Q,gstar,ell are at least C3 '
                           'intersect W4,infinity for each fixed finite angular derivative'),
        limitations=['Only the stated real exact affine family/core; no complex parameter or angle tube',
            'No rounded predictor, independent control box or other original graph is substituted',
            'No actual return, cap, full-frequency inverse, exact metric solution or closed family is supplied'])
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2), flush=True)


if __name__ == '__main__':
    main()
