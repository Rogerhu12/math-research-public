#!/usr/bin/env python3
"""R282 local owner for the exact same shared-field collar and fixed caps.

This is a library for the independent complete space/phase combiner. It uses
all actual collar Hermite/Fourier coefficients and the first exact B cell.
Its graph is in common material theta, not in the physical input phi. A
strict local receipt covers only its stated closed space/phase product.
No actual accepted field is manufactured and no native or global gate changes.
"""
from __future__ import annotations

from fractions import Fraction as F
import hashlib
import json
import os

SCHEMA = "R282-same-shared-field-local-cuff-cross-Gram-owner-v1"
CONSTANT_SCHEMA = "R282-complete-collar-and-shared-B-uniform-local-constants-v1"
REPOSITORY = "Rogerhu12/math-research-public"


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("Evaluate local geometry only in the named public Actions repository")


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       allow_nan=False)+"\n").encode()


def strings(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {key: strings(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [strings(item) for item in value]
    return value


def minimum_squared_radius(box):
    return sum((F(0) if lo <= 0 <= hi else min(lo*lo, hi*hi)
                for lo, hi in box), F(0))


def linear_lower(vector, box):
    return sum((coefficient*(lo if coefficient >= 0 else hi)
                for coefficient, (lo, hi) in zip(vector, box)), F(0))


def rational_unit_centre(box, sqrt_upper, bits):
    """Rational RP1 unit vector, tending to the box centre direction.

    The centre need not belong to the cap. Only the later full-domain
    inequalities certify membership. No floating atan2 or normalisation.
    """
    x, y = ((lo+hi)/2 for lo, hi in box)
    if x == 0 and y == 0:
        return None
    length = sqrt_upper(x*x+y*y, bits)
    if x >= 0:
        t = y/(length+x)
        denominator = 1+t*t
        e = ((1-t*t)/denominator, 2*t/denominator)
        chart = "t"
    else:
        t = y/(length-x)
        denominator = 1+t*t
        e = ((t*t-1)/denominator, 2*t/denominator)
        chart = "u"
    if e[0]*e[0]+e[1]*e[1] != 1:
        raise AssertionError("The local chart centre is not an exact rational unit vector")
    return e, dict(construction_chart=chart, rational_parameter=str(t),
                   cap_box_centre=[str(x), str(y)],
                   centre_length_upper=str(length), sqrt_bits=bits)


class CuffOwner:
    def __init__(self, field, markers, active_module, kernel, *,
                 sqrt_bits, max_constant_levels):
        require_actions()
        if sqrt_bits < 16 or max_constant_levels < 1:
            raise ValueError("Use explicit positive local resource/precision budgets")
        self.field, self.M, self.kernel = field, active_module, kernel
        self.sqrt_bits = sqrt_bits
        self.max_constant_levels = max_constant_levels
        self.R = field.cuff
        self.h = field.inner-field.cuff
        self.hB = field.B.radii[1]-field.B.radii[0]
        self.H = field.B.nodal[0][0]
        if not (self.R > 0 and self.h > 0 and self.hB > 0):
            raise ValueError("Preserve the original positive cuff and exact widths")
        if field.B.nodal[0] != (self.H, F(0), F(0)):
            raise ValueError("The shared background has different literal cuff jets")
        if field.rho_lower <= 0:
            raise ValueError("The original full material-circle certificate is required")
        coefficients = field.tail_coefficients(-1)
        background = tuple(field.B.coefficients[0])
        if (len(coefficients) != field.frequency_count or len(background) != 6
                or background[:3] != (self.H, F(0), F(0))):
            raise ValueError("Keep the actual complete collar and first B polynomial")
        for coordinates in coefficients:
            if len(coordinates) != 3:
                raise ValueError("All three Cartesian coordinates are required")
            for parts in coordinates:
                if len(parts) != 2 or any(len(poly) != 6 for poly in parts):
                    raise ValueError("Keep real/imaginary parts and all six powers")
                if any(any(value != 0 for value in poly[:3]) for poly in parts):
                    raise ValueError("The actual collar left 0/1/2 jets are not zero")
        self.markers = markers
        self.background = background
        self.coefficient_payload = strings(dict(
            schema=CONSTANT_SCHEMA,
            full_frequency_count=field.frequency_count,
            collar_coefficients_frequency_coordinate_realimag_power=coefficients,
            first_shared_B_power_coefficients=background,
            collar_width=self.h, first_B_width=self.hB, cuff=self.R,
            original_inner_FFT_node=field.node_records[0],
            derivative_definition="Exact derivatives of these complete real Hermite polynomials",
            zero_mode_mean_and_Nyquist_retained=True,
            no_RFFT_normalisation_factor_changed=True))
        self.coefficient_sha = hashlib.sha256(canonical(self.coefficient_payload)).hexdigest()
        L = {j: F(0) for j in range(3, 6)}
        T = {j: F(0) for j in range(3, 6)}
        magnitude_records = []
        for k, coordinates in enumerate(coefficients):
            entry = []
            for j in range(3, 6):
                squared = sum((coordinates[c][part][j]**2
                               for c in range(3) for part in range(2)), F(0))
                upper = kernel.sqrt_upper(squared, sqrt_bits)
                L[j] += upper
                T[j] += k*upper
                entry.append(dict(power=j, squared_complex_vector_norm=str(squared),
                                  vector_norm_upper=str(upper)))
            magnitude_records.append(dict(frequency=k, powers=entry))
        self.L, self.T = L, T
        self.magnitude_records = magnitude_records
        self.constants = {side: self.make_constants(side)
                          for side in ("upper", "lower")}

    def make_constants(self, side):
        own = [row for row in self.markers if row["upper"] is (side == "upper")]
        marker_identity = strings([dict(index=row["index"], center=row["center"],
                                       radius=row["radius"], amplitude=row["amplitude"])
                                   for row in own])
        structural = all(self.R > row["radius"]
                         and sum(x*x for x in row["center"]) < (self.R-row["radius"])**2
                         for row in own)
        result = dict(side=side, certified=False, marker_definitions=marker_identity,
                      all_marker_supports_strictly_inside_original_disk=structural,
                      complete_coefficient_payload_sha256=self.coefficient_sha,
                      refinements=[])
        if not structural:
            result["reason"] = "no_literal_marker_free_cuff_annulus_claimed"
            return result
        for level in range(self.max_constant_levels):
            bits = self.sqrt_bits+level
            support = [self.kernel.sqrt_upper(sum(x*x for x in row["center"]), bits)
                       + row["radius"] for row in own]
            outer = max(support, default=F(0))
            gap = self.R-outer
            entry = dict(level=level, effective_sqrt_bits=bits,
                         marker_support_radius_upper=str(outer), gap_lower=str(gap))
            if gap <= 0:
                entry["reason"] = "outward_sqrt_not_yet_resolving_the_true_strict_support"
                result["refinements"].append(entry)
                continue
            # These are local chart sizes, not a change of physical geometry,
            # target reach, g, a scientific tolerance, or a solver budget.
            delta = min(self.R, self.h, self.hB, gap)/(4*(1 << level))
            omega = F(1, 8*(1 << level))
            Mr = sum((j*self.L[j]*delta**(j-1)/self.h**j
                      + j*abs(self.background[j])*delta**(j-1)/self.hB**j
                      for j in range(3, 6)), F(0))
            Mt = sum((self.T[j]*delta**j/self.h**j for j in range(3, 6)), F(0))
            Eu, Ev = omega+Mr, delta/self.R+omega+Mt/self.R
            squared = Eu*Eu+Ev*Ev
            epsilon = self.kernel.sqrt_upper(squared, bits)
            margin = 1-2*epsilon-epsilon*epsilon
            entry.update(delta=str(delta), omega=str(omega), Mr=str(Mr),
                         Mtheta=str(Mt), first_column_error_upper=str(Eu),
                         second_column_error_upper=str(Ev),
                         epsilon_squared_upper=str(squared), epsilon_upper=str(epsilon),
                         cross_Gram_lower=str(margin), certified=margin > 0)
            result["refinements"].append(entry)
            if margin > 0:
                result.update(certified=True, selected=entry,
                              reason="R282_complete_coefficient_uniform_all_phase_derivative_bound")
                return result
        result["reason"] = "local_constant_resource_budget_unresolved_not_geometric_failure"
        return result

    def report(self):
        return dict(schema=CONSTANT_SCHEMA,
                    coefficient_payload_sha256=self.coefficient_sha,
                    full_frequency_count=self.field.frequency_count,
                    complete_vector_norm_bounds=self.magnitude_records,
                    L_by_power={str(j): str(v) for j, v in self.L.items()},
                    T_by_power={str(j): str(v) for j, v in self.T.items()},
                    per_side=self.constants,
                    common_material_angle="theta = Phi(2*pi*q) + alpha, modulo 2*pi",
                    physical_angle_not_identified_with_cap_polar_angle=True,
                    entire_rank_paid_by_local_constant_alone=False,
                    full_surface_certified=False)

    def material_direction(self, angular, chart, phase):
        M = self.M
        q = M.interval(*angular)
        phi = (2*M.arb.pi())*q
        # Keep the physical angle as a separate value. Do not depend on an
        # extension type's possible in-place addition/alias behaviour.
        theta = phi+M.arb(0)
        for m, density in enumerate(self.field.density, 1):
            theta = theta+M.ball(density/F(2*m))*(2*m*phi).sin()
        a, b = phase
        if not (-1 <= a <= b <= 1) or chart not in ("t", "u"):
            raise ValueError("Use one of the two original closed RP1 charts")
        z = M.interval(a, b)
        low_squared = F(0) if a <= 0 <= b else min(a*a, b*b)
        squared = M.interval(low_squared, max(a*a, b*b))
        denominator = 1+squared
        cosine = (1-squared)/denominator if chart == "t" else (squared-1)/denominator
        sine = (2*z)/denominator
        c, s = theta.cos(), theta.sin()
        direction = (cosine*c-sine*s, sine*c+cosine*s)
        return direction, dict(
            material_Phi_interval=M.encode_interval(theta),
            phase_cos_interval=M.encode_interval(cosine),
            phase_sin_interval=M.encode_interval(sine),
            current_material_direction=[M.encode_interval(v) for v in direction],
            original_complete_rho_lower=str(self.field.rho_lower),
            deformed_XY_direction_used_as_material_angle=False)

    def test(self, active, radial, angular, cap, cap_box, chart, phase, depth):
        record = dict(schema=SCHEMA, certified=False,
                      covers_only_stated_closed_space_phase_product=True,
                      original_distinct_material_point_responsibility=True,
                      same_point_identified_only_by_original_cuff_quotient=True)
        if active["sheet"] != cap["cap"] or active["piece_kind"] != "collar":
            record["reason"] = "not_the_same_original_cuff_chart"
            return record
        side = active["sheet"]
        constants = self.constants[side]
        if not constants["certified"]:
            record["reason"] = constants["reason"]
            return record
        chosen = constants["selected"]
        delta, omega = F(chosen["delta"]), F(chosen["omega"])
        radial_min = minimum_squared_radius(cap_box)
        record.update(side=side, constant_level=chosen["level"],
                      complete_coefficient_payload_sha256=self.coefficient_sha,
                      cross_Gram_lower=chosen["cross_Gram_lower"],
                      cap_box_minimum_squared_radius=str(radial_min))
        if not (self.R <= radial[0] <= radial[1] <= self.R+delta
                and radial_min >= (self.R-delta)**2):
            record["reason"] = "the_entire_spatial_product_is_not_in_the_marker_free_radial_chart"
            return record
        # The cap domain is still the box intersected with the original disk.
        # Do not require its containing box to lie inside that disk.
        centre = rational_unit_centre(cap_box, self.kernel.sqrt_upper,
                                      self.sqrt_bits+depth)
        if centre is None:
            record["reason"] = "no_nonzero_parameter_centre_for_this_local_chart"
            return record
        e, construction = centre
        perpendicular = (-e[1], e[0])
        vectors = (e,
                   (omega*e[0]-perpendicular[0], omega*e[1]-perpendicular[1]),
                   (omega*e[0]+perpendicular[0], omega*e[1]+perpendicular[1]))
        cap_margins = [linear_lower(vector, cap_box) for vector in vectors]
        record.update(common_chart_unit_centre=list(map(str, e)),
                      centre_construction=construction,
                      chart=dict(radial_coordinate="u=r-R", angular_coordinate="v=R*(theta-theta_c)",
                                 cuff=str(self.R), delta=str(delta), omega=str(omega)),
                      fixed_full_box_sector_lower=list(map(str, cap_margins)),
                      full_cap_disk_intersection_retained=True)
        if any(value <= 0 for value in cap_margins):
            record["reason"] = "fixed_cap_closed_subdomain_not_strictly_inside_this_sector"
            return record
        direction, angle_record = self.material_direction(angular, chart, phase)
        inequalities = [sum((self.M.ball(coefficient)*value
                             for coefficient, value in zip(vector, direction)), self.M.arb(0))
                        for vector in vectors]
        enclosures = [self.M.encode_interval(value) for value in inequalities]
        active_margins = [F(item["lower"]) for item in enclosures]
        record.update(material_angle_mapping=angle_record,
                      moving_full_product_sector_intervals=enclosures)
        if any(value <= 0 for value in active_margins):
            record["reason"] = "moving_material_angle_and_phase_not_inside_the_same_sector"
            return record
        record.update(certified=True,
                      reason="R282_strict_cross_Gram_and_complete_same_material_chart_membership",
                      all_distinct_material_pairs_have_nonzero_chord_and_endpoint_tangent_components=True,
                      normal_ball_precondition_added=False,
                      global_curvature_or_reach_paid_here=False)
        return record
