#!/usr/bin/env python3
"""Independent R86 full-flat-disk marker on the exact R82 activity field.

The old canonical marker and its constructor are unchanged and are never
given the larger amplitude.  The new amplitude is an exact Fraction:
1600 times the old literal epsilon.  It has a 57-bit numerator and must NOT
be replaced in the mathematical definition by float(epsilon).

All float jets below are numerical evaluations of that declared rational
function.  The exact scalar transfer uses Fraction, preserves the old full
field/mean/height, and does not recompute any prefix or tail certificate.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from actual_closed_map_v2 import ActualClosedMapV2


RUN_SHA = '1ad1682601655468ecacfe22867d20fe849e87406fac64f1d3b3f9c36ab63891'
BUNDLE_SHA = '3b312be557d67cda05624e41d46266925fbe3836c48759c613ede6cf52c70b98'
GEOMETRY_SHA = '57480474eab2110d41053fee5ada0f02548dbb1b9e2fbaf56b9a16ce9fea742c'
QUERY_SHA = '877e68d97868524ed3cde4bca1090fbe8a4a207370e7b6c761da2b5963378cab'
MAP_SHA = '3742d3041daad388cc26d63fb7e4300732459f076327938a39ef92b7f3603ee5'
CANONICAL_SHA = '06c97cc20934e08b217dfa04891145e61e1f926c35a8a1c88eee05cd1c8c1060'
OLD_RADIUS = Q(900719925474099, 36028797018963968)
OLD_EPSILON = Q(4722366482869643, 75557863725914323419136)
HALF_COLUMN = Q(5764607523034235, 2305843009213693952)
CUT_WIDTH = Q(1080863910568919, 9007199254740992)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def checked(path, expected):
    path = Path(path).resolve()
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected:
        raise ValueError('Frozen actual input changed: '+str(path))
    return json.loads(raw)


class FullDiskBudgetMarker:
    """A separate exact marker definition with its own proved R86 budget.

    This class does not subclass, alter, or bypass UniversalThreefoldMarker.
    The new gate is a theorem hypothesis: 0<r<=flat_radius, 0<epsilon<=r^2/25.
    This alone gives a local curvature bound, not a whole-surface certificate.
    """
    def __init__(self, radius, epsilon, flat_radius):
        self.radius_exact = Q(radius)
        self.epsilon_exact = Q(epsilon)
        self.flat_radius_exact = Q(flat_radius)
        r, eps = self.radius_exact, self.epsilon_exact
        if not 0 < r <= self.flat_radius_exact or not 0 < eps <= r*r/25:
            raise ValueError('The independently proved R86 disk/amplitude gate failed')
        self.radius = float(r)
        if not math.isfinite(self.radius) or Q(self.radius) != r:
            raise ValueError('This evaluator requires an exactly representable literal radius')
        self._epsilon_evaluation_only = float(eps)
        if not math.isfinite(self._epsilon_evaluation_only):
            raise ValueError('Finite evaluation amplitude required')

    def jets(self, x, y):
        """Binary64 evaluation only; the defining epsilon is epsilon_exact."""
        x, y = float(x), float(y)
        if not math.isfinite(x) or not math.isfinite(y):
            raise ValueError('Finite Cartesian coordinates required')
        r, eps = self.radius, self._epsilon_evaluation_only
        xx, yy = x/r, y/r
        if not math.isfinite(xx) or not math.isfinite(yy) or math.hypot(xx, yy) >= 1:
            return 0., np.zeros(2), np.zeros((2, 2))
        z = complex(xx, yy)
        denominator = 1-z**3/2
        h = (z**3/denominator).real
        first = 3*z*z/(denominator*denominator)
        second = 6*z/(denominator*denominator)+9*z**4/(denominator**3)
        gh = np.asarray([first.real, -first.imag])/r
        Hh = np.asarray([[second.real, -second.imag],
                         [-second.imag, -second.real]])/(r*r)
        v = np.asarray([xx, yy])
        u = 1-xx*xx-yy*yy
        b = u**3
        gb = -6*u*u*v/r
        Hb = (24*u*np.outer(v, v)-6*u*u*np.eye(2))/(r*r)
        value = eps*b*h
        gradient = eps*(b*gh+h*gb)
        hessian = eps*(b*Hh+h*Hb+np.outer(gb, gh)+np.outer(gh, gb))
        if not (math.isfinite(value) and np.all(np.isfinite(gradient))
                and np.all(np.isfinite(hessian))):
            raise FloatingPointError('Nonfinite marker evaluation; no map accepted')
        return float(value), gradient, hessian

    def moment_coefficient(self, j):
        """The exact new B_(3j)/pi; all harmonics are retained."""
        if not isinstance(j, int) or isinstance(j, bool) or j < 1:
            raise ValueError('A positive integer harmonic index is required')
        n = 3*j
        return (6*self.epsilon_exact*Q(1, 2**(j-1))*self.radius_exact**(n+2)
                /((n+1)*(n+2)*(n+3)*(n+4)))

    def metadata(self):
        r, eps = self.radius_exact, self.epsilon_exact
        old_limit_at_new_radius = min(Q(1,100000), r*r/10000)
        return dict(
            marker_kind='R86-independent-full-disk-rational-budget-marker',
            definition='epsilon_exact*(1-|z/r|^2)_+^3*Re((z/r)^3/(1-(z/r)^3/2))',
            radius_exact=str(r), epsilon_exact=str(eps),
            epsilon_numerator_bits=eps.numerator.bit_length(),
            epsilon_exactly_representable_as_binary64=(Q(float(eps)) == eps),
            epsilon_float_is_evaluation_only=True,
            flat_disk_radius_exact=str(self.flat_radius_exact),
            new_local_budget_gate='0<r<=flat_radius; 0<epsilon<=r^2/25',
            original_canonical_class_unmodified=True,
            original_canonical_constructor_would_accept=(0 < eps <= old_limit_at_new_radius),
            all_harmonics_retained=True, boundary_Cartesian_two_jet_exactly_zero=True,
            height_absolute_upper_exact=str(2*eps),
            gradient_norm_upper_exact=str(24*eps/r),
            Hessian_operator_upper_exact=str(252*eps/r**2),
            first_cap_moment_divided_by_pi_exact=str(self.moment_coefficient(1)),
            cap_target_metric='dx^2+dy^2+df_new^2, fixed at every phase',
            numerical_evaluation_is_a_continuous_certificate=False)


class ActualClosedFullDiskMarker:
    """Explicit new family: R82 outside the disks, new fixed graph on both disks.

    The composition keeps the original model and marker intact.  Its disk
    values are F_R82 + side*(f_new-f_old)*e_z, with the corresponding complete
    Cartesian first and second derivatives.  This is a new design and a new
    target metric on the disks, not refinement of the old marked target.
    """
    def __init__(self, source_run, geometry_bundle, node_check, old_geometry_report):
        source_run, geometry_bundle = map(Path, (source_run, geometry_bundle))
        if sha(source_run) != RUN_SHA or sha(geometry_bundle) != BUNDLE_SHA:
            raise ValueError('This actual-family entry is bound to the R82/R83 field')
        here = Path(__file__).resolve().parent
        if (sha(here/'actual_closed_map_v2.py') != MAP_SHA
                or sha(here/'universal_threefold_marker.py') != CANONICAL_SHA):
            raise ValueError('The original map or canonical marker source changed')
        old = checked(old_geometry_report, GEOMETRY_SHA)
        if (old['status'] != 'actual_complete_marked_column_closed_C2_geometry_certified'
                or old['actual_query']['sha256'] != QUERY_SHA
                or old['geometry_bundle']['sha256'] != BUNDLE_SHA
                or old['source_run']['sha256'] != RUN_SHA
                or Q(old['cut_width_exact']) != CUT_WIDTH
                or Q(old['cylinder_half_length_exact_binary']) != HALF_COLUMN):
            raise ValueError('The actual R82 geometry and literal design do not match')
        base = ActualClosedMapV2(
            source_run, geometry_bundle, node_check,
            marker_strength=0., cylinder_half_length=float(HALF_COLUMN),
            cut_width=float(CUT_WIDTH), canonical_r67_marker=True)
        try:
            old_marker = base.r67_marker.metadata()
            if (old_marker != old['canonical_marker']
                    or Q(old_marker['radius_exact_binary']) != OLD_RADIUS
                    or Q(old_marker['amplitude_exact_binary']) != OLD_EPSILON
                    or Q(base.a) != 2*OLD_RADIUS):
                raise ValueError('The old exact marker/full flat-disk identity changed')
            radius = Q(base.a)
            epsilon = 1600*OLD_EPSILON
            self.fixed_marker = FullDiskBudgetMarker(radius, epsilon, radius)
            self.old_geometry = old
            self.old_geometry_report = dict(path=str(Path(old_geometry_report).resolve()),
                                           sha256=GEOMETRY_SHA)
            self.geometry_transfer = self._transfer(old, radius, epsilon)
            if self.fixed_marker.metadata()['original_canonical_constructor_would_accept']:
                raise ValueError('The explicitly distinct R86 design was not selected')
        except BaseException:
            base.close()
            raise
        self.base = base
        self.canonical_r67_marker = False

    @staticmethod
    def _transfer(old, radius, epsilon):
        zlow, zhigh = map(Q, old['cap_height_after_column_exact_interval'])
        whole_rho = Q(old['whole_radius_upper']['upper_exact'])
        whole_sigma = Q(old['whole_support_lower']['lower_exact'])
        whole_K = Q(old['whole_principal_curvature_upper']['upper_exact'])
        gradient = 24*epsilon/radius
        # sqrt(1+x)<=1+x/2 for x>=0; all following arithmetic is rational.
        support = (zlow-26*epsilon)/(1+gradient**2/2)
        radius_squared = radius**2+(zhigh+2*epsilon)**2
        curvature = 252*epsilon/radius**2
        if (zlow <= 2*epsilon or support < whole_sigma
                or radius_squared > whole_rho**2 or curvature > whole_K
                or whole_K != Q(123,10)):
            raise ValueError('The actual new cap does not preserve all R82 scalar bounds')
        old_B = OLD_EPSILON*OLD_RADIUS**5/140
        new_B = epsilon*radius**5/140
        if new_B != 51200*old_B:
            raise ValueError('The exact rational new marker identity changed')
        return dict(
            proof='R86 analytic graph replacement and exact scalar transfer',
            cap_support_lower_exact=str(support),
            cap_radius_squared_upper_exact=str(radius_squared),
            cap_curvature_upper_exact=str(curvature),
            whole_radius_upper_exact=str(whole_rho),
            whole_support_lower_exact=str(whole_sigma),
            whole_principal_curvature_upper_exact=str(whole_K),
            whole_diameter_upper=old['whole_diameter_upper'],
            whole_reach_lower=old['whole_reach_lower'],
            reach_over_initial_diameter_lower=old['reach_over_initial_diameter_lower'],
            same_R82_global_scalar_bounds_preserved=True,
            B3_multiplier_exact='51200',
            B3_multiplier_is_not_a_Hausdorff_multiplier=True,
            source_cap_height_is_same_true_primitive_not_midpoint=True,
            prefix_tail_polynomials_or_certificates_recomputed=False)

    def __getattr__(self, name):
        if name in ('r67_marker', 'marker_strength', 'marker_radius'):
            raise AttributeError('R86 has a distinct marker contract; use fixed_marker and metadata')
        return getattr(self.base, name)

    def marker(self, x, y):
        return self.fixed_marker.jets(x, y)

    def prefix_jets(self, s, theta, phase=0.):
        return self.base.prefix_jets(s, theta, phase)

    def disk_jets(self, x, y, side=1):
        X, J, H = self.base.disk_jets(x, y, side)
        old_f, old_g, old_H = self.base.marker(x, y)
        new_f, new_g, new_H = self.marker(x, y)
        X, J, H = X.copy(), J.copy(), H.copy()
        X[2] += side*(new_f-old_f)
        J[2] += side*(new_g-old_g)
        H[2] += side*(new_H-old_H)
        return X, J, H

    def tail_jets(self, R, theta, side=1, phase=0.):
        R, theta = float(R), float(theta)
        if side not in (-1, 1) or not 0 <= R <= self.base.Rcut:
            raise ValueError('Outside the actual closed tail')
        if R >= self.base.a:
            # The new marker has exactly zero Cartesian two-jet at R=a.
            return self.base.tail_jets(R, theta, side, phase)
        er = np.asarray([math.cos(theta), math.sin(theta)])
        et = np.asarray([-math.sin(theta), math.cos(theta)])
        X, J, H = self.disk_jets(*(R*er), side=side)
        radial = J@er
        radial2 = np.einsum('kij,i,j->k', H, er, er)
        angular = J@(R*et)
        angular2 = np.einsum('kij,i,j->k', H, R*et, R*et)-J@(R*er)
        mixed = np.einsum('kij,i,j->k', H, er, R*et)+J@et
        return X, radial, radial2, angular, angular2, mixed

    def metadata(self):
        return dict(
            construction='R82 outside both full flat disks; replace fixed canonical caps by the exact R86 rational graphs',
            canonical_r67_marker=False,
            original_canonical_query_contract_is_applicable=False,
            original_query_sha256=QUERY_SHA,
            original_geometry_report=self.old_geometry_report,
            original_map_source_sha256=MAP_SHA,
            original_canonical_source_sha256=CANONICAL_SHA,
            new_marker=self.fixed_marker.metadata(),
            exact_geometry_transfer=self.geometry_transfer,
            disk_target_changed_once_at_design=True,
            target_metric_fixed_for_all_phases=True,
            old_target_fixed_problem_refinement_claimed=False,
            all_boundary_Cartesian_two_jets_preserved=True,
            complete_tail_metric_claimed=False,
            actual_lambda_one_or_held_claimed=False,
            readme_completion_claimed=False)

    def close(self):
        self.base.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('source-run', 'geometry-bundle', 'node-check', 'old-geometry-report', 'out'):
        parser.add_argument('--'+key, type=Path, required=True)
    args = parser.parse_args()
    model = ActualClosedFullDiskMarker(
        args.source_run, args.geometry_bundle, args.node_check, args.old_geometry_report)
    try:
        report = model.metadata()
        report['source_sha256'] = sha(__file__)
        report['entry_constructor_actually_returned'] = True
        report['new_full_numerical_query_or_mesh_claimed'] = False
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
        print(json.dumps(dict(output=str(args.out.resolve()), sha256=sha(args.out))), flush=True)
    finally:
        model.close()


if __name__ == '__main__':
    main()
