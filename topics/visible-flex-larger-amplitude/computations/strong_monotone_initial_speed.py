#!/usr/bin/env python3
"""Optional monotone first-piece Bernstein front-loading, default unchanged.

A nonzero initial_speed_frontload changes the physical metric. Its default
degree is22, held fixed when taking the physical lambda derivative. The
lambda=0 path delegates every original provider operation without converting
old polynomial coefficients. Install after any angle/pulse hook on the actual
loaded provider. Nonzero front-loading and nonzero pulse are deliberately
separate candidates in this first interface; no combined law is implied.

The mathematical family and its domain are proved in
notes/2026-11-12-strong-monotone-bernstein-initial-speed.md.
This source alone is not evidence of a new actual coupled solution.
"""
from __future__ import annotations
import math
import numpy as np


def elevated_cubic_controls(degree, kS, V):
    """Exact degree elevation formula, evaluated in float64."""
    source = (0., kS/3., V, V)
    result = []
    for j in range(degree+1):
        denominator = math.comb(degree, j)
        terms = [
            source[k]*math.comb(3, k)*math.comb(degree-3, j-k)/denominator
            for k in range(max(0, j-(degree-3)), min(3, j)+1)
        ]
        result.append(math.fsum(terms))
    # These entries have explicit common endpoint formulas; avoid introducing
    # roundoff differences into the shared endpoint derivative constraints.
    result[0], result[1], result[-2], result[-1] = 0., kS/degree, V, V
    return result


def bernstein(controls, u):
    """De Casteljau evaluation with finite-degree, shape-preserving storage."""
    u = np.asarray(u)
    dtype = np.result_type(u.dtype, np.float64)
    values = np.asarray(controls, dtype=dtype).reshape(
        (len(controls),)+(1,)*u.ndim) + np.zeros_like(u, dtype=dtype)
    for count in range(len(controls)-1, 0, -1):
        values[:count] = (1-u)*values[:count] + u*values[1:count+1]
    return values[0]


def physical_piece(a0, delta, V, k0, weight, degree=22):
    """Construct one declared new physical piece; return serializable metadata.

    The nonnegative derivative-control gate also validates small negative
    lambda values used by centered physical finite differences. It does not
    extrapolate the convex-combination theorem beyond its proved interval.
    """
    values = (a0, delta, V, k0, weight)
    if not all(math.isfinite(float(v)) for v in values):
        raise ValueError("Nonfinite first-piece parameter")
    if not (a0 > 0 and delta > 0 and 0 < V < 1 and k0 > 0):
        raise ValueError("Invalid physical first-piece domain")
    if int(degree) != degree or not 4 <= degree <= 64:
        raise ValueError("Front-loading degree must be one fixed integer4..64")
    degree = int(degree)
    A = (1-weight)/2 + weight*(degree-1)/(degree+1)
    B = (1-weight)/12 + weight/(degree*(degree+1))
    if A <= 0 or B < 0:
        raise ValueError("Front-loading length coefficients leave the explicit domain")
    length = 2*delta/(A*V + math.sqrt((A*V)**2 + 4*B*k0*delta))
    if not math.isfinite(length) or length <= 0:
        raise ValueError("Invalid front-loaded physical length")
    kS = k0*length
    baseline = elevated_cubic_controls(degree, kS, V)
    endpoint = [0., kS/degree, *([V]*(degree-1))]
    if weight == 1.:
        controls = endpoint
    else:
        controls = [a+weight*(b-a) for a, b in zip(baseline, endpoint)]
    controls[0], controls[1], controls[-2], controls[-1] = 0., kS/degree, V, V
    differences = [controls[j+1]-controls[j] for j in range(degree)]
    if min(differences) < 0:
        raise ValueError("Actual Bernstein velocity derivative controls are not nonnegative")
    if not all(math.isfinite(c) and 0 <= c <= V for c in controls):
        raise ValueError("Actual Bernstein speed hull leaves [0,V]")
    derivative = [degree*value/length for value in differences]
    radius = [a0+length*math.fsum(controls[:j])/(degree+1)
        for j in range(degree+2)]
    if abs(radius[-1]-(a0+delta)) > 2e-13*max(1., abs(a0+delta)):
        raise ValueError("The new first piece failed its original radius increment")
    return dict(length=length, strong_initial_speed_frontload=float(weight),
        strong_initial_speed_frontload_degree=degree,
        strong_initial_speed_frontload_velocity_controls=controls,
        strong_initial_speed_frontload_radius_controls=radius,
        strong_initial_speed_frontload_acceleration_controls=derivative,
        strong_initial_speed_frontload_nonnegative_derivative_hull=True)


def install(provider):
    if getattr(provider, "_strong_initial_speed_frontload_installed", False):
        return
    old_velocity, old_jet, old_prefix = (
        provider.velocity, provider.piece_jet, provider.NeckPrefix)

    def velocity(segment, u):
        if segment.get("strong_initial_speed_frontload", 0.) == 0.:
            return old_velocity(segment, u)
        return bernstein(segment["strong_initial_speed_frontload_velocity_controls"], u)

    def piece_jet(segment, u):
        if segment.get("strong_initial_speed_frontload", 0.) == 0.:
            return old_jet(segment, u)
        return tuple(bernstein(segment["strong_initial_speed_frontload_"+key+"_controls"], u)
            for key in ("radius", "velocity", "acceleration"))

    class MonotoneInitialPrefix(old_prefix):
        def append(self, segment):
            if segment["kind"] == "hermite" and not self.segments:
                weight = float(self.cfg.get("initial_speed_frontload", 0.))
                if not math.isfinite(weight):
                    raise ValueError("Nonfinite initial speed front-loading")
                if weight != 0.:
                    if float(self.cfg.get("initial_speed_pulse", 0.)) != 0.:
                        raise ValueError("Choose the explicit pulse or monotone law, not an undeclared combination")
                    degree = self.cfg.get("initial_speed_frontload_degree", 22)
                    data = physical_piece(segment["a0"], float(self.cfg["delta"]),
                        segment["v1"], segment["k0"], weight, degree)
                    self.S = data["length"]
                    segment = dict(segment, **data)
            return super().append(segment)

    provider.velocity = velocity
    provider.piece_jet = piece_jet
    provider.NeckPrefix = MonotoneInitialPrefix
    provider._strong_initial_speed_frontload_installed = True


def install_globals(namespace):
    from types import SimpleNamespace
    proxy = SimpleNamespace(**namespace)
    install(proxy)
    for name in ("velocity", "piece_jet", "NeckPrefix",
            "_strong_initial_speed_frontload_installed"):
        namespace[name] = getattr(proxy, name)
