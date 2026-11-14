#!/usr/bin/env python3
"""The existing scaled-core connector, made callable as a full C2 profile.

The accepted scalar prefix, original AngleConnector, .985 coast, and original
physical tail bridge are retained. Interior C2 bumps supply explicit design
parameters without moving any core or physical-cut scalar 0/1/2 jet.
This prepares a metric family, not a nonaxisymmetric solution on it.
"""
from __future__ import annotations

import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"

import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np
from strong_20261114_scaled_core_tail_connector import AngleConnector
from geometry_20261114_r225_fixed_profile import FixedProfile

HERE = Path(__file__).resolve().parent


def read(path):
    path = Path(path)
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == ".gz" else raw)


def load_provider():
    spec = importlib.util.spec_from_file_location("full_scalar_original_provider", HERE / "alternative-neck-provider.py")
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


class ScalarBump:
    """width^2 * 64 x^3(1-x)^3, extended by zero; C2 at both ends."""
    def __init__(self, left, right):
        self.left, self.right = float(left), float(right)
        self.width = self.right - self.left
        if self.width <= 0:
            raise ValueError("A scalar-control support must have positive width")

    def jet(self, s):
        x = (float(s) - self.left) / self.width
        if x <= 0 or x >= 1:
            return np.zeros(3)
        return np.array([
            self.width ** 2 * 64 * x ** 3 * (1 - x) ** 3,
            self.width * 64 * (3 * x ** 2 - 12 * x ** 3 + 15 * x ** 4 - 6 * x ** 5),
            64 * (6 * x - 36 * x ** 2 + 60 * x ** 3 - 30 * x ** 4),
        ])


class CompleteProfile:
    def __init__(self, accepted, port, peak_curvature=2.5, tail_modes=None):
        if accepted.get("success") is not True:
            raise ValueError("The prefix must be an accepted actual BVP")
        self.M = int(accepted["M"])
        self.tail_modes = self.M if tail_modes is None else int(tail_modes)
        self.parameter_count = self.tail_modes - self.M + 3
        if self.parameter_count < 3:
            raise ValueError("Resolve at least as many material tail modes as field modes")
        self.fixed_geometry = accepted["fixed_scalar_profile"]["geometry"]
        self.prefix = FixedProfile(self.fixed_geometry)
        self.prefix_end = float(accepted["mesh"][-1])
        self.incoming = tuple(map(float, self.prefix.profile(self.prefix_end)))
        self.turn = AngleConnector(self.incoming, float(peak_curvature))
        self.turn_end = self.prefix_end + self.turn.length
        self.coast_length = (self.turn.end_radius - .35) / .985
        if self.coast_length <= 0:
            raise ValueError("The original coast to radius .35 has nonpositive length")
        self.bridge_start = self.turn_end + self.coast_length
        self.provider = load_provider()
        tagged = self.provider.tagged_port(port, dict(loop_radius=.35, loop_speed=.985,
            loop_curvature=7.5, terminal_peak_fraction=.1))
        self.cut = tagged["cut"]
        self.bridge = self.provider.NeckTerminalBridge(self.cut)
        self.end = self.bridge_start + self.bridge.end
        self.tail_parameters = port["parameters"]
        # Three geographically distinct controls for the equal-mode system.
        # Further mode-mismatch controls are explicit local bumps in the prefix;
        # their rank is a numerical question, never asserted by dimension count.
        intervals = [(.15 * self.prefix_end, .70 * self.prefix_end),
                     (self.prefix_end, self.turn_end),
                     (self.turn_end, self.bridge_start)]
        extra = self.parameter_count - 3
        if extra:
            points = np.linspace(.05 * self.prefix_end, .95 * self.prefix_end, extra + 1)
            intervals.extend(zip(points[:-1], points[1:]))
        self.bumps = [ScalarBump(left, right) for left, right in intervals]
        self.knots = sorted(set([0., *self.prefix.x.tolist(), self.prefix_end,
                                 self.turn_end, self.bridge_start, self.end,
                                 self.prefix_end + self.turn.ei * self.turn.length,
                                 self.prefix_end + (1 - self.turn.eo) * self.turn.length,
                                 *[self.bridge_start + float(s) for s in self.bridge.breaks()],
                                 *[s for bump in self.bumps for s in (bump.left, bump.right)]]))
        self.knots = [s for s in self.knots if 0 <= s <= self.end]

    def base_jet(self, s):
        s = float(s)
        if not 0 <= s <= self.end:
            raise ValueError("Profile evaluation is outside the complete metric interval")
        if s <= self.prefix_end:
            return np.array(self.prefix.profile(s), dtype=float)
        if s <= self.turn_end:
            return np.array(self.turn.profile(s - self.prefix_end), dtype=float)
        if s <= self.bridge_start:
            return np.array([self.turn.end_radius - .985 * (s - self.turn_end), -.985, 0.])
        return np.array([np.asarray(v).item() for v in self.bridge.profile(s - self.bridge_start)])

    def control_jets(self, s):
        return np.stack([bump.jet(s) for bump in self.bumps], axis=1)

    def profile(self, s, parameters=None):
        parameters = np.zeros(self.parameter_count) if parameters is None else np.asarray(parameters)
        if parameters.shape != (self.parameter_count,):
            raise ValueError("Scalar parameter dimension differs from the complete DN count")
        jet = self.base_jet(s) + self.control_jets(s) @ parameters
        if not np.all(np.isfinite(jet)) or jet[0] <= 0 or abs(jet[1]) >= 1:
            raise FloatingPointError("The actual controlled scalar metric left a>0, |a'|<1")
        return tuple(jet)

    def description(self):
        E, Ep = float(self.cut["E"]), float(self.cut["Ep"])
        expected = np.array([self.cut["radius"], -1 / np.sqrt(E), -Ep / (2 * E ** 2)])
        actual = self.base_jet(self.end)
        error = float(np.max(np.abs(actual - expected)))
        if error > 5e-12:
            raise ValueError("The original complete physical-cut scalar jet failed")
        if np.any(self.control_jets(0.) != 0) or np.any(self.control_jets(self.end) != 0):
            raise ValueError("An interior control moved a core or physical-cut jet")
        joins = [
            ("accepted-prefix/turn", np.array(self.prefix.profile(self.prefix_end)),
             np.array(self.turn.profile(0.))),
            ("turn/coast", np.array(self.turn.profile(self.turn.length)),
             np.array([self.turn.end_radius, -.985, 0.])),
            ("coast/finite-bridge", np.array([.35, -.985, 0.]),
             np.array([np.asarray(v).item() for v in self.bridge.profile(0.)])),
            ("finite-bridge/physical-tail", actual, expected),
        ]
        for j, (left, right) in enumerate(zip(self.bridge.segments[:-1], self.bridge.segments[1:])):
            joins.append(("finite-bridge-internal-" + str(j),
                          np.array(self.provider.piece_jet(left, 1.)),
                          np.array(self.provider.piece_jet(right, 0.))))
        join_errors = {name: float(np.max(np.abs(left - right))) for name, left, right in joins}
        if max(join_errors.values()) > 5e-12:
            raise ValueError("A complete scalar 0/1/2 interface differs")
        return dict(scope=__doc__, field_modes=self.M, tail_modes=self.tail_modes,
                    fixed_core_modes=3, state_dimension=3 * self.M + 2,
                    scalar_parameters=self.parameter_count,
                    left_boundary_rows=2 * self.M + 5, right_boundary_rows=self.tail_modes,
                    complete_prefix_geometry=self.fixed_geometry,
                    prefix_end=self.prefix_end, incoming_jet=list(self.incoming),
                    connector=dict(peak_curvature=self.turn.K, initial_curvature=self.turn.k0,
                                   ramp_in=self.turn.ei, ramp_out=self.turn.eo,
                                   length=self.turn.length),
                    turn_end=self.turn_end, coast_length=self.coast_length,
                    bridge_start=self.bridge_start, bridge_length=self.bridge.end,
                    end=self.end, physical_tail_cut=self.cut, physical_tail_parameters=self.tail_parameters,
                    final_scalar_jet=actual.tolist(), final_scalar_jet_error=error,
                    all_added_scalar_012_join_errors=join_errors,
                    control_supports=[[bump.left, bump.right] for bump in self.bumps],
                    control_definition="(right-left)^2 * 64*x^3*(1-x)^3 inside each support, zero outside",
                    core_and_cut_scalar_jets_fixed_for_all_controls=True,
                    nonaxisymmetric_new_field_computed=False, full_DN_solved=False)


class FrozenCompleteProfile:
    """The identical solved scalar metric, with no remaining design control.

All frozen coefficients are used in the same profile formula. Field and
tail frequency may increase together; changing the inlet core then changes
the embedding in canonical material angle, not this scalar metric.
    """
    def __init__(self, designed, parameters, field_modes=None):
        self.designed = designed
        self.frozen_parameters = np.asarray(parameters, dtype=float).copy()
        if self.frozen_parameters.shape != (designed.parameter_count,):
            raise ValueError("Freeze every scalar design parameter")
        self.M = designed.M if field_modes is None else int(field_modes)
        if self.M < designed.M:
            raise ValueError("A fixed-metric refinement cannot discard original field modes")
        self.tail_modes, self.parameter_count = self.M, 0
        self.cut, self.tail_parameters = designed.cut, designed.tail_parameters
        self.end, self.knots = designed.end, designed.knots

    def base_jet(self, s):
        return np.asarray(self.designed.profile(s, self.frozen_parameters))

    def control_jets(self, s):
        return np.zeros((3, 0))

    def profile(self, s, parameters=None):
        if parameters is not None and np.asarray(parameters).shape != (0,):
            raise ValueError("This scalar metric is already frozen")
        return tuple(self.base_jet(s))

    def description(self):
        result = self.designed.description()
        result.update(scope="The complete scalar profile evaluated at the frozen design controls.",
                      field_modes=self.M, tail_modes=self.M, fixed_core_modes=0,
                      state_dimension=3 * self.M + 2, scalar_parameters=0,
                      left_boundary_rows=2 * self.M + 2, right_boundary_rows=self.M,
                      frozen_design_parameters=self.frozen_parameters.tolist(),
                      canonical_material_metric="ds^2 + a(s; frozen_parameters)^2 dtheta^2",
                      same_material_metric_refinement_interface=True)
        return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--accepted", type=Path, required=True)
    p.add_argument("--port", type=Path, required=True)
    p.add_argument("--peak-curvature", type=float, default=2.5)
    p.add_argument("--tail-modes", type=int)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    model = CompleteProfile(read(args.accepted), read(args.port), args.peak_curvature, args.tail_modes)
    result = model.description()
    result.update(accepted_sha256=hashlib.sha256(args.accepted.read_bytes()).hexdigest(),
                  port_sha256=hashlib.sha256(args.port.read_bytes()).hexdigest(),
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: result[key] for key in ("field_modes", "tail_modes", "state_dimension",
                    "scalar_parameters", "left_boundary_rows", "right_boundary_rows", "end",
                    "final_scalar_jet_error", "nonaxisymmetric_new_field_computed")}), flush=True)


if __name__ == "__main__":
    main()
