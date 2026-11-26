#!/usr/bin/env python3
"""Actual m3 native scope and the complete declared finite Fourier map.

This specifies a new polynomial map, not an error-free projection of the
unprojected continuous tail. Every coefficient belongs to the new map and
must enter its continuous metric, curvature and shared-node certificates.
"""
import math


SCHEMA = "actual-m3-native-tail-spectrum-v2"
GEOMETRY_SCHEMA = "actual-m3-native-tail-geometry-v2"


def spectrum_contract(M, N, spacing, degree=None):
    for name, value in (("M", M), ("quadrature", N), ("spacing", spacing)):
        if type(value) is not int or value <= 0:
            raise ValueError("Positive actual integer dimension required: " + name)
    if spacing != 3:
        raise ValueError("This explicit topic map retains its original threefold symmetry")
    available = (N - 4) // 2
    choice = "largest_band_with_original_four_sample_clearance" if degree is None else "explicit_bound_projection_degree"
    degree = available if degree is None else degree
    if type(degree) is not int or not spacing * M + 1 <= degree <= available:
        raise ValueError("Require 3M+1 <= degree and N >= 2*degree+4 for this complete m3 map")
    planar = [m for m in range(-degree, degree + 1) if (m - 1) % spacing == 0]
    height = [spacing * j for j in range(M + 1)]
    # The first-order Cartesian image of every retained state harmonic must
    # remain available to the common cut trace, including both signed modes.
    state_planar = sorted({1, *[1 + sign * spacing * j for j in range(1, M + 1)
                                for sign in (-1, 1)]})
    if not set(state_planar).issubset(planar):
        raise ArithmeticError("The chosen planar list lost a complete state harmonic")
    return {
        "schema": SCHEMA,
        "finite_scope": {"M": M, "quadrature": N, "spacing": spacing},
        "native_independent_quadrature_nodes": N // math.gcd(N, spacing),
        "degree": degree, "available_degree": available, "degree_selection": choice,
        "degree_rule": "All integer m with |m|<=degree and m=1 mod spacing; N>=2*degree+4; degree>=spacing*M+1.",
        "planar_modes": planar, "height_modes": height,
        "complete_state_planar_modes": state_planar,
        "coefficient_count": len(planar) + len(height),
        "all_gram_frequency_bound": 2 * max(max(map(abs, planar)), height[-1]),
        "radial_definition": "Exact quintic Hermite interpolation of the shared literal binary radius knots and complete Cartesian two-jets.",
        "angular_definition": "The saved real planar coefficients multiply exp(i*m*theta); height coefficients multiply cos(m*theta).",
        "coefficient_definition": "Literal coefficients computed from the original N angular samples; this declares a finite map, not an exact Fourier expansion of the continuous source evaluator.",
        "continuous_source_projection_error_assumed_zero": False,
        "old_other_field_metric_bounds_reused": False,
    }


def degree_argument(spectrum):
    selection = spectrum.get("degree_selection")
    if selection == "largest_band_with_original_four_sample_clearance":
        return None
    if selection == "explicit_bound_projection_degree":
        return spectrum["degree"]
    raise ValueError("Unknown declared projection degree rule")


def canonical_contract(spectrum):
    finite = spectrum["finite_scope"]
    expected = spectrum_contract(finite["M"], finite["quadrature"], finite["spacing"],
                                 degree_argument(spectrum))
    if spectrum != expected:
        raise ValueError("The explicit finite Fourier map contract changed")
    return expected


def validate_spectrum_container(data, spectrum, *, stage=False):
    """Require the same exact full lists before any polynomial proof work."""
    canonical_contract(spectrum)
    if data.get("geometrySchema") != GEOMETRY_SCHEMA or data.get("spectrum") != spectrum:
        raise ValueError("Shared geometry uses another explicit finite map contract")
    finite = data["finiteScope"]
    if any(finite.get(key) != value for key, value in spectrum["finite_scope"].items()):
        raise ValueError("Shared geometry differs from the accepted native dimensions")
    if (data.get("degree") != spectrum["degree"]
            or data.get("planarModes") != spectrum["planar_modes"]
            or data.get("heightModes") != spectrum["height_modes"]):
        raise ValueError("A complete declared Fourier frequency list changed")
    if not stage:
        return
    count = spectrum["coefficient_count"]
    nodes, mids = data["nodes"], data["midpoints"]
    if len(nodes) < 2 or len(mids) != len(nodes) - 1:
        raise ValueError("The actual stage has an incomplete radius mesh")
    for point in [*nodes, *mids]:
        if not math.isfinite(point["radiusJS"]) or point["radiusJS"] <= 0:
            raise ValueError("Invalid literal radius in the new stage")
        jets = point["coefficients"]
        if (len(jets) != 3 or any(len(row) != count for row in jets)
                or any(not math.isfinite(value) for row in jets for value in row)):
            raise ValueError("Incomplete finite Cartesian value/first/second jets")
    if any(right["radiusJS"] <= left["radiusJS"] for left, right in zip(nodes[:-1], nodes[1:])):
        raise ValueError("The actual literal-R stage mesh is not increasing")
