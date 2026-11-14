#!/usr/bin/env python3
"""Small independent polynomial/dispatch checks, never a PDE or new surface."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from types import SimpleNamespace
import numpy as np

import strong_monotone_initial_speed as candidate

SELF_SHA = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def old_velocity(segment, u):
    u = np.asarray(u)
    V, a = segment["v1"], segment["k0"]*segment["length"]
    return V*u*u*(3-2*u) + a*u*(1-u)**2


def old_jet(segment, u):
    u = np.asarray(u)
    S, V, a = segment["length"], segment["v1"], segment["k0"]*segment["length"]
    radius = segment["a0"]+S*(V*u**3*(2-u)/2+a*u*u*(6-8*u+3*u*u)/12)
    derivative = 6*V*u*(1-u)+a*(1-u)*(1-3*u)
    return radius, old_velocity(segment, u), derivative/S


class OriginalPrefix:
    def __init__(self, cfg):
        self.cfg, self.segments = dict(cfg), []
        self.S = None
    def append(self, segment):
        self.segments.append(segment)
        return segment


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError("Use a fresh fixture output")
    checks, rows = {}, []
    delta, V, k0, a0 = .16208113625386517, .3198, .45, 1.
    S3 = 2*delta/(V/2+np.sqrt(V*V/4+k0*delta/3))
    segment = dict(kind="hermite", a0=a0, v1=V, k0=k0, length=float(S3))
    provider = SimpleNamespace(velocity=old_velocity, piece_jet=old_jet, NeckPrefix=OriginalPrefix)
    nodes = np.linspace(0., 1., 65)
    before = [value.tobytes() for value in old_jet(segment, nodes)]
    candidate.install(provider)
    for index, cfg in enumerate(({"delta": delta}, {"delta": delta, "initial_speed_frontload": 0.})):
        obj = provider.NeckPrefix(cfg)
        obj.append(segment)
        checks["default_dispatch_"+str(index)] = (
            obj.segments[0] is segment
            and [value.tobytes() for value in provider.piece_jet(segment, nodes)] == before
            and provider.velocity(segment, nodes).tobytes() == old_velocity(segment, nodes).tobytes())
    gauss, weights = np.polynomial.legendre.leggauss(40)
    u = np.r_[0., 1e-8, .01, .17, .5, .83, .99, 1.]
    for degree in (4, 6, 10, 22):
        for weight in (-1e-5, 1e-5, .1, .5, 1.):
            piece = candidate.physical_piece(a0, delta, V, k0, weight, degree)
            S = piece["length"]
            a = k0*S
            actual = dict(segment, **piece)
            r, v, acceleration = provider.piece_jet(actual, u)
            # A separate closed-form derivative, with no degree-elevation or
            # de-Casteljau calls, checks the two actual polynomial components.
            cubic = V*u*u*(3-2*u)+a*u*(1-u)**2
            cubic_derivative = 6*V*u*(1-u)+a*(1-u)*(1-3*u)
            degree_v = V*(1-(1-u)**degree-degree*u*(1-u)**(degree-1))+a*u*(1-u)**(degree-1)
            C = degree*((degree-1)*V-a)
            degree_derivative = (1-u)**(degree-2)*(a+C*u)
            expected_v = (1-weight)*cubic+weight*degree_v
            expected_acceleration = ((1-weight)*cubic_derivative+weight*degree_derivative)/S
            # 40-point Gauss integrates these degree<=22 polynomials; each
            # radius is independently reconstructed from the velocity.
            radial = []
            for endpoint in u:
                sample = endpoint*(gauss+1)/2
                speed = provider.velocity(actual, sample)
                radial.append(a0+S*endpoint*np.dot(weights, speed)/2)
            radius_error = float(np.max(abs(r-np.asarray(radial))))
            speed_error = float(np.max(abs(v-expected_v)))
            acceleration_error = float(np.max(abs(acceleration-expected_acceleration)))
            endpoint_error = float(max(abs(r[0]-a0), abs(r[-1]-a0-delta),
                abs(v[0]), abs(v[-1]-V), abs(acceleration[0]-k0), abs(acceleration[-1])))
            residual = abs(((1-weight)/2+weight*(degree-1)/(degree+1))*V*S
                +((1-weight)/12+weight/(degree*(degree+1)))*k0*S*S-delta)
            passed = max(radius_error, speed_error, acceleration_error, endpoint_error, residual) < 2e-12
            key = f"degree{degree}-lambda{weight}"
            checks[key] = bool(passed)
            rows.append(dict(degree=degree, weight=weight, length=S,
                radius_integral_error=radius_error, speed_closed_form_error=speed_error,
                acceleration_closed_form_error=acceleration_error,
                endpoint_jet_error=endpoint_error, increment_equation_error=float(residual),
                minimum_derivative_control=min(piece["strong_initial_speed_frontload_acceleration_controls"])))
    rejected = False
    try:
        candidate.physical_piece(a0, delta, V, k0, 2., 22)
    except ValueError:
        rejected = True
    checks["outside_monotone_domain_rejected"] = rejected
    rejected = False
    try:
        obj = provider.NeckPrefix(dict(delta=delta, initial_speed_frontload=.1, initial_speed_pulse=.01))
        obj.append(segment)
    except ValueError:
        rejected = True
    checks["undeclared_pulse_combination_rejected"] = rejected
    record = dict(scope=__doc__, finished=True, passed=all(checks.values()), checks=checks, rows=rows,
        source_sha256={str(Path(__file__)):SELF_SHA,
            str(Path(candidate.__file__)):hashlib.sha256(Path(candidate.__file__).read_bytes()).hexdigest()},
        PDE_RHS_calls=0, Node_processes=0, actual_provider_loader_checked=False,
        new_solution=False, background_only=True,
        numerical_tolerances_are_fixture_comparison_only=True)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("x") as stream:
        json.dump(record, stream, indent=2, allow_nan=False)
        stream.write("\n")
    print(json.dumps(dict(event="monotone_initial_piece_fixture", passed=record["passed"],
        output=str(args.out), checks=len(checks), actual_solution=False)), flush=True)
    if not record["passed"]:
        raise ValueError("Independent polynomial/dispatch fixture failed")


if __name__ == "__main__":
    main()
