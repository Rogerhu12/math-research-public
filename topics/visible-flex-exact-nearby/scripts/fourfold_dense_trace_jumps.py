#!/usr/bin/env python3
"""Exact dyadic jumps of saved DOP853 dense reference polynomials.

This certifies a finite, explicitly defined reference curve, not an ODE solution.
Every binary64 input is interpreted exactly as a rational number.  In particular
the saved step h is never silently replaced by a subtraction of saved endpoints.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import io
import json
import math
from pathlib import Path

import numpy as np


def frac(x):
    return Fraction.from_float(float(x))


def upper(q: Fraction) -> float:
    value = float(q)
    if not math.isfinite(value):
        raise ValueError("non-finite rational enclosure")
    if frac(value) < q:
        value = math.nextafter(value, math.inf)
    assert frac(value) >= q
    return value


def ratio(q):
    return {"numerator": str(q.numerator), "denominator": str(q.denominator)}


def dense_value(y_old, coefficients, z):
    if z == 0:
        return y_old
    if z == 1:
        return y_old + coefficients[0]
    value = Fraction(0)
    for i, coefficient in enumerate(reversed(coefficients)):
        value = (value + coefficient) * (z if i % 2 == 0 else 1 - z)
    return value + y_old


def verify(trace: Path):
    raw = trace.read_bytes()
    payload = gzip.decompress(raw) if trace.suffix == ".gz" else raw
    with np.load(io.BytesIO(payload), allow_pickle=False) as data:
        arrays = {key: data[key].copy() for key in data.files}
    times = arrays["accepted_tau"]
    states = arrays["accepted_state"]
    told = arrays["dense_t_old"]
    h = arrays["dense_h"]
    yold = arrays["dense_y_old"]
    coefficients = arrays["dense_F"]
    steps = len(times) - 1
    if states.ndim != 3 or states.shape[0] != steps + 1:
        raise ValueError("accepted state shape")
    components, rays = states.shape[1:]
    if yold.shape != (steps, components, rays):
        raise ValueError("dense initial shape")
    if coefficients.shape != (steps, 7, components, rays):
        raise ValueError("dense polynomial shape")
    if h.shape != (steps,) or told.shape != (steps,):
        raise ValueError("dense time shape")
    if not np.array_equal(told, times[:-1]):
        raise ValueError("saved dense origin differs from accepted step origin")
    if not np.array_equal(yold, states[:-1]):
        raise ValueError("saved dense initial value differs from accepted state")
    if not all(np.all(np.isfinite(a)) for a in [times, states, told, h, yold, coefficients]):
        raise ValueError("non-finite saved input")
    if np.any(h == 0):
        raise ValueError("zero dense step")

    totals = [[Fraction(0) for _ in range(rays)] for _ in range(components)]
    maxima = [Fraction(0) for _ in range(components)]
    step_reports = []
    nonunit = []
    max_h_error = Fraction(0)
    nonzero = 0
    for i in range(steps):
        delta = frac(times[i + 1]) - frac(times[i])
        saved_h = frac(h[i])
        z = delta / saved_h
        if z != 1:
            nonunit.append({"step": i, "z_minus_one": ratio(z - 1)})
        max_h_error = max(max_h_error, abs(saved_h - delta))
        step_maxima = [Fraction(0) for _ in range(components)]
        for component in range(components):
            for ray in range(rays):
                cs = [frac(value) for value in coefficients[i, :, component, ray]]
                endpoint = dense_value(frac(yold[i, component, ray]), cs, z)
                jump = frac(states[i + 1, component, ray]) - endpoint
                absolute = abs(jump)
                totals[component][ray] += absolute
                step_maxima[component] = max(step_maxima[component], absolute)
                maxima[component] = max(maxima[component], absolute)
                nonzero += bool(jump)
        step_reports.append({"step": i, "component_absolute_jump_upper": [upper(q) for q in step_maxima]})

    total_maxima = [max(row) for row in totals]
    return {
        "status": "exact_finite_reference_jump_certificate",
        "scope": "No ODE residual, true-flow, or initial-H estimate is asserted.",
        "trace": str(trace),
        "trace_sha256": hashlib.sha256(raw).hexdigest(),
        "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "steps": steps,
        "rays": rays,
        "components": components,
        "component_interpretation": ["theta", "log_J", "fixed_x_parameter_variation"][:components],
        "dense_origins_exactly_match_accepted_origins": True,
        "dense_initial_states_exactly_match_accepted_states": True,
        "max_saved_h_minus_exact_endpoint_difference_upper": upper(max_h_error),
        "nonunit_endpoint_coordinates": nonunit,
        "nonzero_scalar_jump_count": int(nonzero),
        "maximum_single_absolute_jump_upper": [upper(q) for q in maxima],
        "maximum_per_ray_sum_of_absolute_jumps_upper": [upper(q) for q in total_maxima],
        "exact_maximum_per_ray_sum": [ratio(q) for q in total_maxima],
        "per_component_per_ray_sum_upper": [[upper(q) for q in row] for row in totals],
        "per_step": step_reports,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--trace", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    report = verify(args.trace)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    output = json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False).encode() + b"\n"
    if args.out.suffix == ".gz":
        output = gzip.compress(output, mtime=0)
    args.out.write_bytes(output)
    print(json.dumps({key: report[key] for key in ["trace_sha256", "steps", "rays", "nonzero_scalar_jump_count", "maximum_per_ray_sum_of_absolute_jumps_upper"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
