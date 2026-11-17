#!/usr/bin/env python3
"""Validate true raw-core primitives at actual source inverse points.

Finite point comparisons exercise the new rational integral oracle and
the old fixed-physical-input atlas.  They are not a full metric bound,
continuous angular approximation, new BVP, or closed-map certificate.
"""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
import sys
import time

import numpy as np

from m3_integral_prefix import load_integral_prefix, sha
from integral_core_intervals import (
    ExactRawM3Core, magnitude, sub, point, R32_SOURCE_SHA256, SERIES_DEGREE,
)
from certify_protected_arc_curvature_dual import decimal, show
from prefix_true_profile import TruePrefix


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('source-topic', 'short-bridge', 'checkpoint', 'port', 'out'):
        p.add_argument('--'+key, type=Path, required=True)
    args = p.parse_args()
    began = time.monotonic()
    here = Path(__file__).resolve().parent
    assert sha(here/'certify_m3_large_circle_window.py') == R32_SOURCE_SHA256
    record, obj, flow, sol, _ = load_integral_prefix(
        args.source_topic, args.short_bridge, args.checkpoint, args.port, 256)
    numerical = obj._core
    exact = ExactRawM3Core(numerical, obj.integral_reader_provenance)
    bounds = exact.global_bounds
    assert bounds['rho_lower'] > 0
    # Source values select exact binary64 target material points only.
    # They are not used as enclosure endpoints or proved extrema.
    normal_offsets = np.array([-.37, -.29, -.21, 0., .21, .29, .37])
    normal_points = np.r_[0., numerical.center+normal_offsets, numerical.T]
    psi = 2*np.pi*np.arange(1, 12, 2)/12
    targets = np.unique(np.r_[numerical.arc(normal_points),
                              psi-float(flow.warp_e)*np.sin(3*psi)/3])
    source = numerical.rho_material_jets(targets)
    rho, rho1 = source['rho'], source['rho_phi']
    third = -source['Ft']/rho[:, None]**2+source['normal']*rho1[:, None]/rho[:, None]**3
    source_jets = dict(position=source['F'], tangent=source['Ft'], second=source['Ftt'], third=third)
    maximum_errors = {key: F(0) for key in source_jets}
    arc_error, inverse_error = F(0), F(0)
    rows = []
    for i, theta in enumerate(targets):
        values = exact.material_enclosure(float(theta), float(source['phi'][i]))
        errors = {}
        for key, array in source_jets.items():
            # L1 bounds the Euclidean error.  All source outputs are fixed
            # binary64 numbers; their exact real discrepancy is enclosed.
            error = sum(magnitude(sub(v, point(F.from_float(float(array[i, j])))))
                        for j, v in enumerate(values[key]))
            errors[key] = error
            maximum_errors[key] = max(maximum_errors[key], error)
        arc_error = max(arc_error, values['arc_residual_upper'])
        inverse_error = max(inverse_error, values['inverse_normal_error_upper'])
        rows.append(dict(material_target=float(theta), source_phi=float(source['phi'][i]),
                         true_arc_residual_upper=decimal(values['arc_residual_upper'], True),
                         true_inverse_normal_error_upper=decimal(values['inverse_normal_error_upper'], True),
                         source_jet_error_upper={key: decimal(value, True) for key, value in errors.items()}))
    physical = record['physical_tail_parameters']
    atlas = TruePrefix(record['frozen_profile'],
                       dict(radius=physical['rCut'], backgroundSlope=physical['wCut']),
                       record['meridian_length'])
    paths = [here/'integral_core_intervals.py', Path(__file__),
             here/'certify_protected_arc_curvature_dual.py',
             here/'certify_m3_large_circle_window.py', here/'m3_integral_prefix.py',
             here/'prefix_true_profile.py', here/'certify_background_sharp.py']
    result = dict(
        scope=__doc__, command=sys.argv, sources_sha256={str(f): sha(f) for f in paths},
        checkpoint_sha256=sha(args.checkpoint), port_sha256=sha(args.port),
        source_protocol=obj.integral_reader_provenance,
        exact_input_conventions=dict(
            q=str(exact.q), homotopy=str(exact.lam), physical_controls=[str(v) for v in exact.c],
            primary_halfwidth='21/100', primary_transition='2/25',
            control_transition=str(exact.controls.b), center='pi/3',
            moment_projection='Exact defining two-by-two mean/primary inverse, using its rational source coefficient enclosure',
            R32_constants_reused=True, complex_integral_taylor_degree=SERIES_DEGREE,
            finite_source_values_are_not_assumed_exact_integrals=True),
        global_true_core_bounds={key: ([decimal(v, True) for v in value] if isinstance(value, list)
                                         else decimal(value, key != 'rho_lower'))
                                for key, value in bounds.items()},
        finite_point_count=len(targets), target_material_values=targets.tolist(),
        maximum_true_arc_residual_upper=decimal(arc_error, True),
        maximum_true_inverse_normal_error_upper=decimal(inverse_error, True),
        maximum_true_material_jet_source_error_upper={key: decimal(v, True) for key, v in maximum_errors.items()},
        finite_point_details=rows,
        fixed_physical_atlas=atlas.report(),
        fixed_atlas_anchor_checkpoint_sha256=sha(args.checkpoint),
        bvp_solves=0, angular_or_radial_full_domain_boxes=0,
        continuous_metric_certificate=False,
        unpaid=['Uniform angular approximation of the integral core and its first jets.',
                'Principal finite-map metric and radial error over all shared spans.',
                'Current tail seam repair and full closed-map metric and geometry.',
                'Fixed-g convergence of actual accepted refined maps.'],
        seconds=time.monotonic()-began)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({key: result[key] for key in (
        'finite_point_count', 'global_true_core_bounds', 'maximum_true_arc_residual_upper',
        'maximum_true_inverse_normal_error_upper', 'maximum_true_material_jet_source_error_upper', 'seconds')}), flush=True)


if __name__ == '__main__':
    main()
