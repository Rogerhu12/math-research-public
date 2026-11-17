#!/usr/bin/env python3
"""New-width true-core oracle using all controls from an accepted raw state.

Only the planar core is redesigned here.  No new prefix/tail BVP or
surface metric is solved or asserted.  Exact global rho bounds and finite
true inverse/jet source-error bounds are kept separate.  The source and
original material-atlas identities are checked before evaluating the core.
"""
import argparse
from fractions import Fraction as F
import gzip
import json
import math
from pathlib import Path
import sys
import time

import numpy as np

from generic_raw_core_intervals import (
    GeneralExactRawM3Core, fixed_atlas_identity, control_curvature_enclosure, RAW_KIND, RAW_PATH,
)
import integral_core_intervals as ri
from certify_protected_arc_curvature_dual import decimal, show
from m3_integral_prefix import round_core_type, _same_recorded_sources, sha, RAW_ROUND
from prefix_true_profile import TruePrefix


def accepted_record(path):
    here = Path(__file__).resolve().parent
    sys.path.insert(0, str(here.parent/'resume_m3'))
    from couple_m3_smallcut_secant import accepted_anchor
    record = json.load(gzip.open(path, 'rt'))
    accepted_anchor(record, path)
    if (record['config']['core_kind'] != RAW_KIND or record['core_control_path'] != RAW_PATH
            or not record['config']['exact_core_lift']):
        raise ValueError('A complete accepted raw integral-core source is required')
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--checkpoint', type=Path, required=True)
    parser.add_argument('--atlas-anchor', type=Path, required=True)
    parser.add_argument('--primary-transition', type=float, default=.32)
    parser.add_argument('--control-transition', type=float, default=.4)
    parser.add_argument('--homotopy', type=float, default=1.)
    parser.add_argument('--control-panels', type=int, default=256)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    began = time.monotonic()
    here = Path(__file__).resolve().parent
    record, anchor = accepted_record(args.checkpoint), accepted_record(args.atlas_anchor)
    identity = fixed_atlas_identity(record, anchor_record=anchor)
    library_sources = sorted(RAW_ROUND.glob('*.py'))
    _same_recorded_sources(record, library_sources)
    _same_recorded_sources(anchor, library_sources)
    settings = dict(record['core_round_settings'])
    settings.update(transition=args.primary_transition, control_transition=args.control_transition,
                    homotopy=args.homotopy)
    if (settings['halfwidth'] != .21 or settings['center'] != math.pi/3
            or settings['bimodal_eta'] != 0. or settings['lock_fundamental'] is not True):
        raise ValueError('The declared design must retain a=.21 and the even eta=0 m3 convention')
    controls = np.asarray(record['parameters'][1:], float)*np.asarray(record['central_correction_scales'], float)
    if len(controls) != record['config']['modes']-1:
        raise ValueError('The complete source control vector is required')
    Core = round_core_type(RAW_ROUND, RAW_PATH)
    numerical = Core(record['actual_primary_amplitude'], controls, 3, arc_nodes=1024, **settings)
    assert np.array_equal(np.asarray(numerical.corrections), controls)
    provenance = dict(core_kind=RAW_KIND, core_control_path=RAW_PATH,
                      core_round_settings=settings, physical_controls=controls.tolist(),
                      core_projection_order_J=len(controls)+1)
    exact = GeneralExactRawM3Core(numerical, provenance)
    bounds = exact.global_bounds
    assert bounds['rho_lower'] > 0, 'No inverse certificate without a true global rho lower bound'
    control_bound = control_curvature_enclosure(exact, args.control_panels)
    sharp_rho = (1-8*exact.q+exact.q*exact.lam*exact.beta[0]+control_bound['whole_angle_enclosure'][0],
                 1+8*exact.q+control_bound['whole_angle_enclosure'][1])
    assert sharp_rho[0] > 0
    # New widths change the physical planar core.  The frozen source fields
    # above only identify the candidate meridian metric, not an isometry.
    offsets = np.unique(np.r_[0., -.21, .21,
        -(.21+args.primary_transition), .21+args.primary_transition,
        -(.21+args.control_transition), .21+args.control_transition,
        -.37, .37])
    normals = np.r_[0., numerical.center+offsets, numerical.T]
    psi = 2*np.pi*np.arange(1, 12, 2)/12
    material = np.unique(np.r_[numerical.arc(normals), psi-.32*np.sin(3*psi)/3])
    source = numerical.rho_material_jets(material)
    rho, rho1 = source['rho'], source['rho_phi']
    third = -source['Ft']/rho[:, None]**2+source['normal']*rho1[:, None]/rho[:, None]**3
    source_jets = dict(position=source['F'], tangent=source['Ft'], second=source['Ftt'], third=third)
    maxima = {key: F(0) for key in source_jets}
    arc_error, inverse_error = F(0), F(0)
    for i, theta in enumerate(material):
        values = exact.material_enclosure(float(theta), float(source['phi'][i]))
        arc_error = max(arc_error, values['arc_residual_upper'])
        inverse_error = max(inverse_error, values['inverse_normal_error_upper'])
        for key, array in source_jets.items():
            error = sum(ri.magnitude(ri.sub(v, ri.point(F.from_float(float(array[i, j])))))
                        for j, v in enumerate(values[key]))
            maxima[key] = max(maxima[key], error)
    physical = anchor['physical_tail_parameters']
    atlas = TruePrefix(anchor['frozen_profile'],
                       dict(radius=physical['rCut'], backgroundSlope=physical['wCut']),
                       anchor['meridian_length'])
    center = exact._normal_jets_local(exact.L, ri.point(0))
    radius = 1+8*exact.q
    sinL, cosL = ri.signed_sincos(exact.L)
    center_xy = tuple(ri.sub(v, ri.scale(n, radius))
                      for v, n in zip(center['position'], (cosL, sinL)))
    expected_center_xy = tuple(ri.scale(ri.mul(exact.center_per_q, n), -exact.q)
                               for n in (cosL, sinL))
    center_formula_error = sum(ri.magnitude(ri.sub(v, w)) for v, w in zip(center_xy, expected_center_xy))
    protected_rho_error = ri.magnitude(ri.sub(center['rho'], ri.point(radius)))
    if exact.lam == 1:
        assert center_formula_error < F(1, 10**50) and protected_rho_error < F(1, 10**50)
    paths = [Path(__file__), here/'generic_raw_core_intervals.py', here/'integral_core_intervals.py',
             here/'fast_integral_core_intervals.py', here/'certify_protected_arc_curvature_dual.py',
             here/'m3_integral_prefix.py', here/'prefix_true_profile.py', here/'certify_background_sharp.py',
             here.parent/'resume_m3/couple_m3_smallcut_secant.py', *library_sources]
    dec = lambda x: decimal(x, True)
    result = dict(scope=__doc__, command=sys.argv,
        source_sha256={str(p.resolve()): sha(p) for p in paths},
        checkpoint_sha256=sha(args.checkpoint), atlas_anchor_sha256=sha(args.atlas_anchor),
        raw_library_manifest_sha256=sha(RAW_ROUND/'manifest.json'),
        source_checkpoint_acceptance_reused=True,
        source_actual_amplitude=record['actual_primary_amplitude'],
        source_homotopy=record['core_round_settings']['homotopy'],
        design_settings=settings, core_kind=RAW_KIND, core_control_path=RAW_PATH,
        exact_inputs=dict(q=str(exact.q), homotopy=str(exact.lam),
            full_physical_controls=[str(v) for v in exact.c],
            control_count=len(exact.c), projection_order_J=exact.M,
            halfwidth=str(exact.primary.a), primary_transition=str(exact.primary.b),
            control_transition=str(exact.controls.b), center='pi/3',
            widths_follow_source_decimal_roundtrip=True,
            amplitude_homotopy_controls_exact_binary64=True),
        newly_integrated_constants=dict(beta=show(exact.beta), circle_center_per_q=show(exact.center_per_q),
            R32_or_R38_numeric_constants_reused=False),
        raw_projection=dict(gram_entries=tuple(show(v) for v in exact.projection_certificate['gram']),
            determinant=show(exact.projection_certificate['determinant']),
            interval_substitution_residual_upper=dec(exact.projection_certificate['interval_substitution_residual_upper']),
            source_coefficient_error_upper=dec(exact.source_coefficient_error_upper),
            exact_column_independent_of_total_J=True, higher_moment_inverse=False),
        complex_primitive_remainders=dict(primary_degree=exact.primary.degree,
            primary_maximum_frequency=exact.primary.maximum_frequency,
            primary_error_upper=dec(exact.primary.complete_remainder()),
            control_degree=exact.controls.degree, control_maximum_frequency=exact.controls.maximum_frequency,
            control_error_upper=dec(exact.controls.complete_remainder()),
            requested_absolute_error=str(exact.primary.requested_error)),
        global_true_core_bounds={key: ([dec(v) for v in value] if isinstance(value, list)
                                      else decimal(value, key != 'rho_lower'))
                                for key, value in bounds.items()},
        whole_angle_control_curvature=dict(panels=control_bound['panels'],
            exact_midpoint_value_hull=show(control_bound['exact_midpoint_value_hull']),
            global_derivative_upper=dec(control_bound['lipschitz_upper']),
            complete_panel_remainder_upper=dec(control_bound['whole_panel_remainder']),
            enclosure=show(control_bound['whole_angle_enclosure']),
            absolute_upper=dec(control_bound['absolute_upper']),
            below_R38_control_threshold=control_bound['absolute_upper'] < F(2, 25),
            combined_true_rho=show(sharp_rho),
            bound_does_not_depend_on_q=True),
        exact_lambda_one_circle_identity=dict(applicable=exact.lam == 1,
            radius=str(radius), center_formula_interval_width_upper=dec(center_formula_error),
            protected_center_rho_error_upper=dec(protected_rho_error),
            whole_arc_identity='At lambda=1, chi_primary=1 and W_control=0 throughout abs(phi-pi/3)<=a; rho=1+8q and center=-q*Cstar*n(pi/3).'),
        finite_points=dict(count=len(material),
            recipe='Source arc of normal 0,T,center plus 0,+/-a,+/-(a+bp),+/-(a+bc),+/-.37; six odd pi/6 chart angles with e=.32; unique exact binary64 material targets.',
            material_targets_sha256=__import__('hashlib').sha256(material.tobytes()).hexdigest(),
            true_arc_residual_upper=dec(arc_error), true_inverse_normal_error_upper=dec(inverse_error),
            true_material_jet_source_error_upper={key: dec(value) for key, value in maxima.items()},
            no_uniform_source_error_claim=True),
        fixed_material_atlas=dict(identity_sha256=identity['identity_sha256'],
            unchanged_source_and_anchor_physical_fields=True,
            material_length=anchor['meridian_length'], core_design_fields_excluded_from_metric_identity=True,
            true_atlas_report=atlas.report(),
            identity_does_not_certify_new_core_isometry=True),
        bvp_solves=0, full_surface_or_prefix_metric_certificate=False,
        unpaid=['Actual lambda=1 prefix and nonlinear tail satisfying their original gates.',
                'Uniform angular principal/remainder bounds for this new complete control vector.',
                'Complete fixed-g metric, C2 closure, geometry and convergent refinement.'],
        seconds=time.monotonic()-began)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({key: result[key] for key in ('newly_integrated_constants', 'global_true_core_bounds',
        'finite_points', 'complex_primitive_remainders', 'seconds')}, ensure_ascii=False), flush=True)


if __name__ == '__main__':
    main()
