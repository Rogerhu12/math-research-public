#!/usr/bin/env python3
"""The same endpoint-defined C2 material spline, evaluated from local residuals.

This is an explicitly new numerical evaluator. It does not replace or certify
the paid infinite flat kernel. Endpoint data and the material mesh are retained;
the old independent-value basis and dense ODE endpoint jets are observed at
specified paid failure locations during the same new finite-design run.
"""
from collections import defaultdict
import hashlib
from pathlib import Path
import time

import numpy as np

BINDINGS = {
    "r582_finite_resonant_radius_only_20261126.py":
        "445e3ac5098cbaaa08f080e1be5d8172e576f72a00b825b2cb000adad83725d2",
    "r582_paid_resonant_field_20261126.py":
        "1b046b20541fcee05d5c8722dfdd5a509e7018348aab7182bec77c0813a8b395",
}
for filename, expected in BINDINGS.items():
    if hashlib.sha256(Path(__file__).with_name(filename).read_bytes()).hexdigest() != expected:
        raise RuntimeError("stable material source binding changed: " + filename)
from r582_finite_resonant_radius_only_20261126 import RadiusOnlyField
from r582_paid_resonant_field_20261126 import endpoint_hermite, LENGTH

SCHEMA = "r582-local-Taylor-right-residual-common-endpoint-material-v1"
COUNTS = defaultdict(int)
DIAGNOSTIC_S = (0.8691932771929971, 0.8716776757406842)


def residual_data(knots, endpoint_jets):
    """Residuals of the unchanged endpoint formula in extended arithmetic.

    They are derived numerical evaluation data, not independent polynomial
    coefficients. The mathematical spline is still defined by its shared
    endpoint value/first/second jets. No floating interpolation error bound is
    asserted; long-double guard bits do not remove endpoint-data uncertainty.
    """
    wide = np.longdouble
    h = np.asarray(np.diff(knots), dtype=wide)
    left = np.asarray(endpoint_jets[:-1], dtype=wide)
    right = np.asarray(endpoint_jets[1:], dtype=wide)
    hh = h[:, None]
    r0 = right[:, :, 0] - left[:, :, 0] - hh * left[:, :, 1] - (hh * hh / 2) * left[:, :, 2]
    r1 = hh * (right[:, :, 1] - left[:, :, 1] - hh * left[:, :, 2])
    r2 = hh * hh * (right[:, :, 2] - left[:, :, 2])
    return h, left, np.stack((r0, r1, r2), axis=2)


def residual_hermite(knots, endpoint_jets, prepared, positions):
    """Value and actual 1/2 derivatives of one common endpoint quintic.

    P(t)=v0+h*t*d0+h^2*t^2*dd0/2+R0*H01+R1*H11+R2*H21.
    Every derivative below is obtained by differentiating this one polynomial.
    Literal knots return their shared input jets exactly in binary64. This is
    an endpoint-consistent evaluation convention, not a roundoff certificate.
    """
    x = np.atleast_1d(np.asarray(positions, dtype=float))
    if np.any(x < knots[0]) or np.any(x > knots[-1]):
        raise ValueError("stable material query outside the complete interval")
    index = np.clip(np.searchsorted(knots, x, side="right") - 1, 0, len(knots) - 2)
    widths, all_left, all_residual = prepared
    h, left, residual = widths[index], all_left[index], all_residual[index]
    t = (np.asarray(x, dtype=np.longdouble) - np.asarray(knots[index], dtype=np.longdouble)) / h
    # Each row is H01, H11, H21 or its actual t derivative.
    b0 = np.stack((t**3*(10+t*(-15+6*t)), t**3*(-4+t*(7-3*t)),
                   t**3*(np.longdouble('.5')+t*(-1+np.longdouble('.5')*t))), axis=1)
    b1 = np.stack((t*t*(30+t*(-60+30*t)), t*t*(-12+t*(28-15*t)),
                   t*t*(np.longdouble('1.5')+t*(-4+np.longdouble('2.5')*t))), axis=1)
    b2 = np.stack((t*(60+t*(-180+120*t)), t*(-24+t*(84-60*t)),
                   t*(3+t*(-12+10*t))), axis=1)
    hh, tt = h[:, None], t[:, None]
    output = np.empty((len(x), 2, 3), dtype=np.longdouble)
    output[:, :, 0] = (left[:, :, 0] + hh*tt*left[:, :, 1]
        + hh*hh*tt*tt/2*left[:, :, 2] + np.einsum('ij,ikj->ik', b0, residual))
    output[:, :, 1] = (left[:, :, 1] + hh*tt*left[:, :, 2]
        + np.einsum('ij,ikj->ik', b1, residual)/hh)
    output[:, :, 2] = left[:, :, 2] + np.einsum('ij,ikj->ik', b2, residual)/(hh*hh)
    result = np.asarray(output, dtype=float)
    exact_left = x == knots[index]
    result[exact_left] = endpoint_jets[index[exact_left]]
    exact_right = x == knots[index+1]
    result[exact_right] = endpoint_jets[index[exact_right]+1]
    return result.reshape(len(x), 6)


class StableField(RadiusOnlyField):
    def __init__(self, paid, prior_chart, args, deadline):
        super().__init__(paid, prior_chart, args, deadline)
        started = time.monotonic()
        self.prepared_residuals = residual_data(self.material_knots, self.material_endpoint_jets)
        self.residual_preparation_seconds = time.monotonic() - started
        COUNTS['residual_preparation_cells'] += len(self.material_knots)-1
        self.diagnostics = self.local_diagnostics()

    def evaluate(self, positions):
        self.check()
        self.counts['material_Hermite_radial_queries'] += np.asarray(positions).size
        COUNTS['stable_material_radial_queries'] += np.asarray(positions).size
        return residual_hermite(self.material_knots, self.material_endpoint_jets,
                                self.prepared_residuals, positions)

    def local_diagnostics(self):
        """Small new observations at old failure points; never a preflight run."""
        started = time.monotonic()
        locations = set(DIAGNOSTIC_S)
        for s in DIAGNOSTIC_S:
            i = int(np.clip(np.searchsorted(self.material_knots, s, side='right')-1,
                            0, len(self.material_knots)-2))
            a, b = self.material_knots[i:i+2]
            locations.update((float(a), float(b), float((a+b)/2)))
        points = np.asarray(sorted(locations))
        old = endpoint_hermite(self.material_knots, self.material_endpoint_jets, points)
        stable = self.evaluate(points)
        dense = self.tail.evaluate(points)
        output = []
        epsilon = (.18+self.args.initial_epsilon)-.18
        for j, s in enumerate(points):
            i = int(np.clip(np.searchsorted(self.material_knots, s, side='right')-1,
                            0, len(self.material_knots)-2))
            a, b = self.material_knots[i:i+2]
            width = float(b-a)
            endpoint = self.material_endpoint_jets[i:i+2]
            residual = self.prepared_residuals[2][i]
            u = float((.2/(LENGTH-s))**2)
            reference = self.tail.actual.coefficients(u)
            a_s,z_s = float(reference['a_s']),float(reference['z_s'])
            speed = float(np.hypot(a_s,z_s))
            output.append({'s':float(s), 'u':float((.2/(LENGTH-s))**2),
                'material_interval_index':i, 'left_s':float(a), 'right_s':float(b),
                'interval_width':width, 'literal_endpoint':bool(s==a or s==b),
                'left_jets_A_As_Ass_C_Cs_Css':endpoint[0].ravel().tolist(),
                'right_jets_A_As_Ass_C_Cs_Css':endpoint[1].ravel().tolist(),
                'old_independent_basis_jets':old[j].tolist(),
                'new_Taylor_residual_jets':stable[j].tolist(),
                'dense_value_with_ODE_endpoint_jets':dense[j].tolist(),
                'stable_minus_dense_endpoint_jets':(stable[j]-dense[j]).tolist(),
                'stable_minus_old_basis_jets':(stable[j]-old[j]).tolist(),
                'right_residuals_R0_R1_R2_by_A_C':np.asarray(residual,dtype=float).tolist(),
                'residuals_divided_by_width_squared':np.asarray(residual/width**2,dtype=float).tolist(),
                'binary64_epsilon_times_max_endpoint_value_over_h_squared':
                    float(np.finfo(float).eps*np.max(abs(endpoint[:,:,0]))/width**2),
                'fixed_nonround_predictor_epsilon':epsilon,
                'original_frozen_reference_first_jets_a_s_z_s':[a_s,z_s],
                'original_frozen_reference_meridian_speed':speed,
                'epsilon_dense_A_s_over_original_a_s':float(epsilon*dense[j,1]/a_s),
                'epsilon_dense_C_s_over_original_z_s':float(epsilon*dense[j,4]/z_s),
                'epsilon_stable_A_s_over_original_a_s':float(epsilon*stable[j,1]/a_s),
                'epsilon_stable_C_s_over_original_z_s':float(epsilon*stable[j,4]/z_s),
                'epsilon_dense_first_jets_over_original_meridian_speed':
                    (epsilon*dense[j,[1,4]]/speed).tolist(),
                'epsilon_stable_first_jets_over_original_meridian_speed':
                    (epsilon*stable[j,[1,4]]/speed).tolist(),
                'reference_ratios_are_not_the_current_finite_trial_metric':True,
                'roundoff_scale_is_not_a_rigorous_error_bound':True})
        COUNTS['diagnostic_points'] += len(points)
        return {'old_paid_failure_locations_preserved':list(DIAGNOSTIC_S),
            'points':output, 'elapsed_seconds':time.monotonic()-started,
            'dense_endpoint_derivatives_are_ODE_jets_not_dense_polynomial_derivatives':True,
            'no_local_scientific_precomputation':True,
            'does_not_assert_the_failure_was_only_Hermite_roundoff':True}

    def receipt(self):
        result = super().receipt()
        result['stable_material_evaluator'] = {
            'schema':SCHEMA,
            'same_mathematical_common_endpoint_quintic_and_material_knots':True,
            'extended_arithmetic_mantissa_bits':int(np.finfo(np.longdouble).nmant),
            'literal_knot_queries_return_shared_endpoint_jets':True,
            'independent_O_value_terms_are_not_subtracted_after_division_by_h_squared':True,
            'endpoint_data_error_is_not_removed_or_certified':True,
            'infinite_reference_C2_error_certified':False,
            'residual_preparation_seconds':self.residual_preparation_seconds,
            'new_counts':dict(COUNTS), 'local_failure_diagnostics':self.diagnostics}
        return result
