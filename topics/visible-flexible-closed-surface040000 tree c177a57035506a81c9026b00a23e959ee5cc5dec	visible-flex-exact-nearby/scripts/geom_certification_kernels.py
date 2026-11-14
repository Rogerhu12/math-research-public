#!/usr/bin/env python3
"""Exact scalar budgets and reference kernels for visible-flexible-closed-surface.

The default JSON uses rational arithmetic for the phase-anchor obstruction and
for broad C2 cap bumps. It does not assert existence of a complete flexible
surface. The floating-point kernels implement the proved formulas in the
companion note; callers must supply outward error bounds and control rounding
before using their output as a formal interval certificate.

Run: python scripts/geom_certification_kernels.py
Optional: --model-summary /path/to/closed_model.json
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import json
import math
from pathlib import Path
from typing import Iterable


def frac_text(v: F) -> dict:
    return {"exact": str(v), "decimal": float(v)}


def anchor_budget(a: F, radius: F, height_lower: F | None = None) -> dict:
    """S_alpha=R_-alpha B union C; graph cap 0<=zeta<=a on round disk."""
    D_lower = 2 * radius
    reason = "Two opposite points of the cap boundary circle."
    if height_lower is not None and 2 * height_lower > D_lower:
        D_lower = 2 * height_lower
        reason = "Cap planes at +H and -H with H at least the supplied lower bound."
    ratio_upper = a / D_lower
    return {
        "amplitude_upper": frac_text(a),
        "diameter_lower": frac_text(D_lower),
        "diameter_lower_reason": reason,
        "delta_over_D_upper": frac_text(ratio_upper),
        "strictly_fails_0_05_threshold": ratio_upper < F(1,20),
        "proof_scope": "Conditional exact theorem for the stated union/rotation and graph-cap architecture."
    }


def cap_bump_budget(a: F, b: F, c: F, radius: F, rho: F) -> dict:
    """zeta=a*(1-|x-c|^2/b^2)^3_+; one off-axis cap bump.

    |Hess zeta|<=6*a/b^2; the graph's tangent-chord quotient is >=1/K.
    Assumes the remaining annulus has horizontal radius >=radius for the
    support-to-band pair-separation check. That assumption is NOT automatic.
    """
    K = 6*a/(b*b)
    separation = radius-c-b
    return {
        "a": frac_text(a), "support_radius_b": frac_text(b),
        "center_offset_c": frac_text(c), "disk_radius": frac_text(radius),
        "requested_rho": frac_text(rho), "hessian_upper": frac_text(K),
        "within_cap_tangent_chord_lower": frac_text(1/K),
        "support_band_radial_separation_lower": frac_text(separation),
        "within_cap_pass": 1/K >= rho,
        "support_band_pair_pass_if_annulus_radius_ge_disk_radius": separation >= 2*rho,
        "half_turn_cap_Hausdorff_equals_a_if_conditions_hold": (c+b < radius and 2*c-b >= a),
        "scope": "Only a cap design budget; no complete surface, flex, global reach, or optimal-rigid Hausdorff lower bound is claimed."
    }


def two_module_ellipse_budget(R: F, r: F, h_squared: F, witness_fraction: F) -> dict:
    """Conditional diameter witness for orthogonally oriented upper/lower modules."""
    if not (0 < r <= R and h_squared > 0 and 0 <= witness_fraction <= 1):
        raise ValueError('Require 0<r<=R, h_squared>0, and 0<=witness_fraction<=1')
    D0sq = 4*(R*R+h_squared)
    D1sq = max(4*R*R+h_squared,2*(R*R+r*r)+4*h_squared)
    q = D1sq/D0sq
    required = witness_fraction-F(1,10)
    approx = max(0., (float(witness_fraction)-math.sqrt(float(q)))/2)
    lower = F(math.floor(approx*10**7),10**7)
    while lower > 0 and not (witness_fraction-2*lower > 0 and q < (witness_fraction-2*lower)**2):
        lower -= F(1,10**7)
    assert lower >= 0
    return {
        "R": frac_text(R), "r": frac_text(r), "h_squared": frac_text(h_squared),
        "D0_upper_squared": frac_text(D0sq), "D1_upper_squared": frac_text(D1sq),
        "D1_upper_over_D0_upper_squared": frac_text(q),
        "initial_actual_point_pair_fraction_required": frac_text(witness_fraction),
        "delta_over_D0_lower_if_envelopes_and_witness_hold_approx": approx,
        "delta_over_D0_verified_rational_lower": str(lower),
        "passes_0_05_by_exact_squared_comparison": required >= 0 and q <= required*required,
        "not_excluded_by_cylinder_reach_003_necessary_condition": cylinder_witness_not_excluded(R,h_squared,witness_fraction,F(3,100)),
        "scope": "Conditional geometric lower bound only. All envelopes, actual witness points, exact flexibility, and global reach still need construction/verification."
    }


def cylinder_witness_not_excluded(R: F, h_squared: F, w: F, tau: F) -> bool:
    """Exact necessary test from the closed-surface interior rolling-ball bound.

    D >= 2*w*sqrt(R^2+h^2), reach >= tau*D. For C=1/4-tau-tau^2>0,
    the polynomial C*D^2+2*tau*(R+h)*D-(R^2+h^2) is increasing for D>=0.
    At the proposed lower D this becomes 4*C*w^2+4*tau*w*u-1 <= 0,
    where u=(R+sqrt(h_squared))/sqrt(R^2+h_squared). The comparisons below
    eliminate its square roots only after checking both required signs.
    True means NOT EXCLUDED by this one necessary condition; never existence.
    """
    if not (R>0 and h_squared>0 and 0<=w<=1 and 0<tau<F(1,10)):
        raise ValueError('Invalid cylinder-budget parameters')
    C=F(1,4)-tau-tau*tau
    S2=R*R+h_squared
    rho_lower_sq=4*tau*tau*w*w*S2
    if rho_lower_sq>min(R*R,h_squared):
        return False
    A=1-4*C*w*w
    if A<0:
        return False
    B=S2*(A*A-16*tau*tau*w*w)
    if B<0:
        return False
    return (32*tau*tau*w*w*R)**2*h_squared <= B*B


def rigid_cell_lower(h_center_lower: float, source_radius_upper: float,
                     angular_radius_upper: float, translation_radius_upper: float,
                     source_cover_upper: float, target_cover_upper: float) -> float:
    """Reference lower bound over a rotation/translation cell.

    h_center_lower bounds exact Hausdorff distance of the finite sample clouds
    at the cell center. angular_radius_upper is the maximum SO(3) angle from
    cell center, in [0,pi]. Reflections need a second component, not omission.
    """
    if not 0 <= angular_radius_upper <= math.pi:
        raise ValueError("angular_radius_upper must lie in [0, pi]")
    motion = 2*source_radius_upper*math.sin(angular_radius_upper/2)
    return max(0.0, h_center_lower-motion-translation_radius_upper
               -source_cover_upper-target_cover_upper)


def euler_cell_angular_radius(halfwidths: Iterable[float]) -> float:
    """For Q=Rz(a) Ry(b) Rx(c); covers O(3) using Q and QJ separately."""
    values = tuple(halfwidths)
    if len(values) != 3 or any(w < 0 for w in values):
        raise ValueError("three nonnegative halfwidths required")
    return min(math.pi,sum(values))


def pair_box_margin(chord_center_norm: float, normal_dot_center_abs: float,
                    chord_error_upper: float, normal_error_upper: float,
                    rho: float) -> float:
    """Reference bound on |q-p|^2-2*rho*|(q-p).n(p)| for an off-diagonal box.

    The two first inputs need lower/upper outward controls respectively in a
    formal verifier. Supply norm as a true center norm (or use a fully interval
    version); this floating-point function alone is not a proof program.
    """
    dl = max(0.0,chord_center_norm-chord_error_upper)
    normal_upper = (normal_dot_center_abs+chord_error_upper
                    +(chord_center_norm+chord_error_upper)*normal_error_upper)
    return dl*dl-2*rho*normal_upper


def local_geodesic_quotient_lower(K: float, ell0: float) -> float:
    """For all pairs joined by a surface geodesic of length <=ell0<=pi/K."""
    if K <= 0 or ell0 < 0 or K*ell0 > math.pi:
        raise ValueError("Require K>0 and 0<=K*ell0<=pi")
    x = K*ell0/2
    sinc = 1.0 if x == 0 else math.sin(x)/x
    return sinc*sinc/K


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--model-summary",type=Path)
    args = p.parse_args()
    out = {
        "status": "Intermediate proved scalar consequences only; task incomplete.",
        "current_R35_without_height_estimate": anchor_budget(F.from_float(.94)/20000,F.from_float(.86)),
        "current_R35_conditional_H_ge_4": anchor_budget(F.from_float(.94)/20000,F.from_float(.86),F(4)),
        "broad_cap_dimensionless_budget": cap_bump_budget(F(1,20),F(1,10),F(1,10),F(3,10),F(3,100)),
        "two_module_ellipse_budget": two_module_ellipse_budget(F(1),F(3,10),F(91,150),F(24,25)),
        "two_module_aspect_two_budget": two_module_ellipse_budget(F(1),F(1,2),F(1,2),F(97,100)),
        "old_098_witness_jointly_excluded": two_module_ellipse_budget(F(1),F(3,10),F(91,150),F(49,50)),
        "certification_kernel_scope": "Floating point reference formulas; no outward interval arithmetic or global covering engine implemented."
    }
    if args.model_summary:
        d = json.loads(args.model_summary.read_text())
        cap = d["cap"]
        a = F(str(cap["rigorous_extra_height_bound"]))
        radius = F(str(d["end_radius"]))
        out["loaded_model_no_height_needed"] = anchor_budget(a,radius)
        out["loaded_summary"] = {
            "file": str(args.model_summary),
            "phase_family": d["phase_family"],
            "cap_plane_height_reported_numerical": d["cap_plane_height"],
            "phase_family_requires_independent_source_review": True
        }
    print(json.dumps(out,ensure_ascii=False,indent=2))


if __name__ == "__main__":
    main()
