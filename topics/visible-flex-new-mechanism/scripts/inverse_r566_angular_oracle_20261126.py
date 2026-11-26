#!/usr/bin/env python3
"""Independent R566 arbitrary-angle value and exact parameter-Jacobian interface.

The periodic primitive and Ebar use one declared complete uniform FFT rule.
Actual inequality points may have arbitrary angles and retain their own
identity. No peak search, optimizer or new scientific request is launched by
this module. Scientific evaluation belongs to a subsequent identified Actions
scope. Fourier approximation and continuous physical quantities stay distinct.
"""
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import time

import numpy as np

BLOCK_SOURCE_SHA256 = "c0ab647ed2c6c0647c9031995696d40bc2c6717b893f67cf7c6a345c5366ef6b"
if hashlib.sha256(Path(__file__).with_name("inverse_r566_block_jacobian_20261126.py").read_bytes()).hexdigest() != BLOCK_SOURCE_SHA256:
    raise RuntimeError("angular oracle requires the declared block-AD source")
import inverse_r566_block_jacobian_20261126 as blocked

physical, hard = blocked.physical, blocked.hard
Dual, dot, cross, primitive = blocked.Dual, blocked.dot, blocked.cross, blocked.primitive
DesignClockLimit = blocked.DesignClockLimit
SCHEMA = "r566-independent-FFT-and-arbitrary-angular-constraint-points-v1"


class UniformJetModel(blocked.Model):
    def geometry(self, q, differentiate=True, ignore_clock=False, parameter_indices=None):
        """v2 analytic spatial jets with the declared R566 background replaced.

        The unit tangent, periodic primitive, forward parameter derivative,
        actual fundamental forms and shape operator are the same formulas
        as the hash-bound reference. Only physical background profiles and
        the endpoint of the freely varying radial basis have changed.
        """
        q = np.asarray(q, dtype=float)
        indices = (np.arange(self.size, dtype=int) if parameter_indices is None
                   else np.asarray(parameter_indices, dtype=int)) if differentiate else np.empty(0, dtype=int)
        if (indices.ndim != 1 or np.any(indices < 0) or np.any(indices >= self.size)
                or len(np.unique(indices)) != len(indices)):
            raise ValueError("invalid selected parameter directions")
        key = (q.tobytes(), tuple(indices.tolist()))
        if self.cache_key == key:
            return self.cache
        if not ignore_clock and self.deadline is not None and time.monotonic() >= self.deadline:
            raise DesignClockLimit("declared Actions segment reached; R566 design is not complete")
        if q.shape != (self.size,) or not np.all(np.isfinite(q)):
            raise ValueError("invalid physical parameter vector")
        self.cache, self.cache_key = None, None
        nd = len(indices)

        def constant(value):
            value = np.asarray(value, dtype=float)
            return Dual(value, np.zeros(value.shape + (nd,)))

        def linear(basis, start, base=0.0):
            count = basis.shape[-1]
            value = base + np.einsum("...k,k->...", basis, q[start:start + count])
            derivative = np.zeros(np.shape(value) + (nd,))
            if nd:
                mask = (indices >= start) & (indices < start + count)
                derivative[..., mask] = basis[..., indices[mask] - start]
            return Dual(value, derivative)

        def radial(index, start):
            return linear(self.bases[index][:, None, :], start)

        h = constant(q[-1])
        if nd:
            h.d[indices == self.size - 1] = 1
        uc = self.core["u"][None, :]
        u = linear(self.angular_bases[0], 0, self.bg_wm * uc)
        us = linear(self.angular_bases[1], 0, -self.bg_wd * uc)
        uss = linear(self.angular_bases[2], 0, -self.bg_wdd * uc)
        ut = linear(self.theta_basis, 0, self.bg_wm * self.core["utheta"][None, :])
        v, vs, vss = [linear(b, self.block) for b in self.angular_bases]
        vt = linear(self.theta_basis, self.block)
        phase = u + self.theta[None, :]
        sine, cosine = phase.sin(), phase.cos()
        normalizer = (1 + v * v) ** -.5
        hs = -v * vs * normalizer ** 3
        hss = (2 * v * v - 1) * vs * vs * normalizer ** 5 - v * vss * normalizer ** 3
        ht = -v * vt * normalizer ** 3
        ring = (-sine, cosine)
        ring1 = (-cosine, -sine)
        t = tuple(a * normalizer for a in ring) + (v * normalizer,)
        ts = tuple(a1 * us * normalizer + a * hs for a, a1 in zip(ring, ring1)) + (vs * normalizer + v * hs,)
        tss = tuple((a1 * uss - a * us * us) * normalizer + 2 * a1 * us * hs + a * hss
                    for a, a1 in zip(ring, ring1)) + (vss * normalizer + 2 * vs * hs + v * hss,)
        tt = tuple(a1 * (1 + ut) * normalizer + a * ht
                   for a, a1 in zip(ring, ring1)) + (vt * normalizer + v * ht,)

        astart = 2 * self.block
        alpha, alphas, alphass = [radial(i, astart) for i in range(3)]
        exp_alpha = alpha.exp()
        tail = self.par.cap_disk_radius + self.par.length - self.s[:, None]
        abase = self.bg_wm * self.core["a0"] + self.bg_w * tail
        abase1 = self.bg_wd * (tail - self.core["a0"]) - self.bg_w
        abase2 = self.bg_wdd * (tail - self.core["a0"]) - 2 * self.bg_wd
        radius = exp_alpha * abase
        radius1 = exp_alpha * (abase1 + abase * alphas)
        radius2 = exp_alpha * (abase2 + 2 * abase1 * alphas + abase * (alphass + alphas * alphas))

        zstart = astart + self.par.radial_count
        central = self.par.core_half_width + self.s[:, None]
        tail_z = h + self.tail_height
        z = self.bg_wm * central + self.bg_w * tail_z + radial(0, zstart)
        z1 = (self.bg_wm + self.bg_wd * (tail_z - central)
              + self.bg_w * self.tail_height1 + radial(1, zstart))
        z2 = (-2 * self.bg_wd + self.bg_wdd * (tail_z - central)
              + 2 * self.bg_wd * self.tail_height1
              + self.bg_w * self.tail_height2 + radial(2, zstart))

        p, ps, pss = [tuple(primitive(field) for field in fields) for fields in (t, ts, tss)]
        position = tuple(radius * pi + (z if i == 2 else 0) for i, pi in enumerate(p))
        xs = tuple(radius1 * pi + radius * psi + (z1 if i == 2 else 0)
                   for i, (pi, psi) in enumerate(zip(p, ps)))
        xss = tuple(radius2 * pi + 2 * radius1 * psi + radius * pssi + (z2 if i == 2 else 0)
                    for i, (pi, psi, pssi) in enumerate(zip(p, ps, pss)))
        eactual, factual = dot(xs, xs), dot(xs, t)
        ebar = eactual.mean_theta()
        edenom = ebar.floor(1e-14)
        e, f = eactual / edenom - 1, factual / edenom ** .5
        det = eactual - factual * factual
        area = det.floor(1e-24) ** .5
        normal = tuple(component / area for component in cross(xs, t))
        second_l = dot(normal, xss)
        second_m = dot(normal, ts)
        second_n = dot(normal, tt) / radius
        determinant = det.floor(1e-24)
        trace = (second_l + eactual * second_n - 2 * factual * second_m) / determinant
        product = (second_l * second_n - second_m * second_m) / determinant
        discriminant = (trace * trace / 4 - product).floor(0)
        root = (discriminant + 1e-16) ** .5
        curvature = (trace / 2 + root, trace / 2 - root)
        values = {"position": position, "Xs": xs, "T": t, "E": eactual, "F": factual,
                  "Ebar": ebar, "e": e, "f": f, "det": det, "area": radius * area,
                  "radius": radius, "normal": normal, "curvature": curvature}
        if not all(np.all(np.isfinite(values[name].v)) for name in ("E", "e", "f", "det")):
            raise FloatingPointError("nonfinite actual geometry")
        values["__primitive_jets"] = (p, ps, pss)
        values["__radial_jets"] = (radius, radius1, radius2, z, z1, z2)
        values["__tangent_values"] = tuple(tuple(field.v for field in order) for order in (t, ts, tss))
        self.cache_key, self.cache = key, values
        self.last_completed_q = q.copy()
        return values


@dataclass
class FourierField:
    coefficients: np.ndarray
    parameter_coefficients: np.ndarray

    @classmethod
    def from_real_primitive(cls, field):
        n = field.v.shape[1]
        value = np.fft.fft(field.v, axis=1) / n
        derivative = (np.fft.fft(field.d, axis=1) / n if field.size
                      else np.zeros(value.shape + (0,), dtype=complex))
        return cls(value, derivative)

    def evaluate(self, radial_indices, angles, frequencies, batch_size=64,
                 angular_derivative_order=0):
        npoint = len(angles)
        nd = self.parameter_coefficients.shape[-1]
        values = np.empty((npoint, 1))
        derivatives = np.empty((npoint, 1, nd))
        multiplier = (1j * frequencies) ** angular_derivative_order
        for first in range(0, npoint, batch_size):
            last = min(first + batch_size, npoint)
            index = radial_indices[first:last]
            phase = np.exp(1j * angles[first:last, None] * frequencies[None, :]) * multiplier[None, :]
            values[first:last, 0] = np.sum(self.coefficients[index] * phase, axis=1).real
            if nd:
                derivatives[first:last, 0, :] = np.einsum(
                    "nkd,nk->nd", self.parameter_coefficients[index], phase).real
        return Dual(values, derivatives)


class PointSet:
    """Actual material points, independent of the uniform FFT sample count."""
    def __init__(self, oracle, radial_indices, angles):
        started = time.monotonic()
        self.oracle_identity = oracle.identity
        raw_indices = np.asarray(radial_indices)
        self.radial_indices = np.asarray(radial_indices, dtype=int)
        angles = np.asarray(angles, dtype=float)
        if (self.radial_indices.ndim != 1 or angles.shape != self.radial_indices.shape
                or not np.all(raw_indices == self.radial_indices)
                or not len(angles) or not np.all(np.isfinite(angles))
                or np.any(self.radial_indices < 0) or np.any(self.radial_indices >= oracle.uniform.nr)):
            raise ValueError("invalid actual (radial index, theta) constraint points")
        self.angles = np.mod(angles, 2 * np.pi)
        unique_angles, back = np.unique(self.angles, return_inverse=True)
        unique_core = physical.reference.rounded_core(oracle.uniform.par, unique_angles)
        self.core = {name: value if np.ndim(value) == 0 else value[back]
                     for name, value in unique_core.items()}
        near_index = np.rint(self.angles * oracle.uniform.nt / (2 * np.pi)).astype(int) % oracle.uniform.nt
        # Only exact equality permits a gather. A merely nearby peak remains
        # its true angle and uses Fourier evaluation; no silent grid snapping.
        self.uniform_indices = np.where(self.angles == oracle.uniform.theta[near_index], near_index, -1)
        modes = 2 * np.arange(1, oracle.uniform.par.modes + 1)
        sine = np.sin(self.angles[:, None] * modes[None, :])
        cosine = np.cos(self.angles[:, None] * modes[None, :]) * modes[None, :]
        self.angular_bases = [np.einsum("nj,nm->njm", basis[self.radial_indices], sine)
                              .reshape(len(angles), 1, -1) for basis in oracle.uniform.bases]
        self.theta_basis = np.einsum("nj,nm->njm", oracle.uniform.bases[0][self.radial_indices], cosine)
        self.theta_basis = self.theta_basis.reshape(len(angles), 1, -1)
        payload = {"radial_positions": oracle.uniform.s[self.radial_indices].tolist(),
                   "theta": self.angles.tolist()}
        raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
        self.identity = hashlib.sha256(raw).hexdigest()
        self.size = len(angles)
        oracle.counts["point_sets_prepared"] += 1
        oracle.counts["exact_core_arclength_points_prepared"] += len(unique_angles)
        oracle.counts["point_set_seconds"] += time.monotonic() - started

    def subset(self, oracle, selected):
        selected = np.asarray(selected, dtype=int)
        answer = object.__new__(PointSet)
        answer.oracle_identity = self.oracle_identity
        answer.radial_indices, answer.angles = self.radial_indices[selected], self.angles[selected]
        answer.uniform_indices = self.uniform_indices[selected]
        answer.core = {name: value if np.ndim(value) == 0 else value[selected]
                       for name, value in self.core.items()}
        answer.angular_bases = [basis[selected] for basis in self.angular_bases]
        answer.theta_basis = self.theta_basis[selected]
        answer.size = len(selected)
        raw = json.dumps({"parent_point_set_SHA256": self.identity,
                          "selected_indices": selected.tolist()}, sort_keys=True, separators=(",", ":")).encode()
        answer.identity = hashlib.sha256(raw).hexdigest()
        oracle.counts["point_subsets_created"] += 1
        return answer


@dataclass
class PreparedState:
    oracle_identity: str
    q: np.ndarray
    parameter_indices: np.ndarray
    primitives: tuple
    radial_jets: tuple
    mean_E: Dual
    uniform_summary: dict
    uniform_fields: dict
    uniform_tangent_values: tuple


def sampled_summary(g, fft_nodes):
    e, f = g["e"].v, g["f"].v
    eta = .5 * (np.abs(e) + np.sqrt(e * e + 4 * f * f))
    return {"fft_nodes": fft_nodes, "sampled_eta_max": float(np.max(eta)),
            "sampled_det_min": float(np.min(g["det"].v)),
            "sampled_mean_E_min": float(np.min(g["Ebar"].v)),
            "sampled_mean_E_max": float(np.max(g["Ebar"].v)),
            "sampled_curvature_max": max(float(np.max(np.abs(k.v))) for k in g["curvature"]),
            "primitive_and_mean_quadrature_error_certified": False,
            "continuous_angular_peak_coverage_certified": False}


class AngularOracle:
    def __init__(self, par, radial_positions, fft_nodes, batch_size=64):
        self.uniform = UniformJetModel(par, radial_positions, fft_nodes)
        self.frequencies = np.fft.fftfreq(fft_nodes, d=1.0 / fft_nodes)
        self.batch_size = int(batch_size)
        if self.batch_size < 1:
            raise ValueError("positive Fourier point batch required")
        raw = json.dumps({"parameters": vars(par), "s": self.uniform.s.tolist(),
                          "fft_nodes": fft_nodes}, sort_keys=True, separators=(",", ":")).encode()
        self.identity = hashlib.sha256(raw).hexdigest()
        self.counts = {"point_sets_prepared": 0, "point_subsets_created": 0,
                       "exact_core_arclength_points_prepared": 0,
                       "FFT_states_prepared": 0, "uniform_geometries_prepared": 0,
                       "primitive_Fourier_fields_prepared": 0,
                       "point_evaluations": 0, "point_values_evaluated": 0,
                       "point_parameter_directions_evaluated": 0,
                       "uniform_points_gathered": 0, "nonuniform_points_summed": 0,
                       "diagnostic_uniform_FFTs": 0,
                       "point_set_seconds": 0.0, "prepare_seconds": 0.0, "point_seconds": 0.0}
        self.prepared_key, self.prepared = None, None

    def points(self, radial_indices, angles):
        return PointSet(self, radial_indices, angles)

    def release(self):
        self.prepared_key, self.prepared = None, None
        self.uniform.cache_key, self.uniform.cache = None, None

    def prepare(self, q, parameter_indices=()):
        q = np.asarray(q, dtype=float)
        indices = np.asarray(parameter_indices, dtype=int)
        key = (q.tobytes(), tuple(indices.tolist()))
        if key == self.prepared_key:
            return self.prepared
        self.release()
        started = time.monotonic()
        g = self.uniform.geometry(q, differentiate=bool(len(indices)),
                                  ignore_clock=True, parameter_indices=indices)
        primitives = tuple(tuple(FourierField.from_real_primitive(field) for field in order)
                           for order in g["__primitive_jets"])
        state = PreparedState(self.identity, q.copy(), indices.copy(), primitives,
                              g["__radial_jets"], g["Ebar"], sampled_summary(g, self.uniform.nt),
                              {name: value for name, value in g.items() if not name.startswith("__")},
                              g["__tangent_values"])
        self.prepared_key, self.prepared = key, state
        self.uniform.cache_key, self.uniform.cache = None, None
        self.counts["FFT_states_prepared"] += 1
        self.counts["uniform_geometries_prepared"] += 1
        self.counts["primitive_Fourier_fields_prepared"] += 9
        self.counts["prepare_seconds"] += time.monotonic() - started
        return state

    def evaluate(self, state, points, return_interpolation_diagnostics=False):
        if state.oracle_identity != self.identity or points.oracle_identity != self.identity:
            raise ValueError("prepared Fourier state and actual points belong to another model")
        started = time.monotonic()
        q, indices = state.q, state.parameter_indices
        nd = len(indices)
        idx = points.radial_indices
        on_grid = points.uniform_indices >= 0
        if np.any(on_grid) and not np.all(on_grid):
            pieces = []
            for selected in (np.flatnonzero(on_grid), np.flatnonzero(~on_grid)):
                subset = points.subset(self, selected)
                pieces.append((selected, self.evaluate(state, subset, return_interpolation_diagnostics)))

            def merge_field(name, component=None):
                value, derivative = np.empty((points.size, 1)), np.empty((points.size, 1, nd))
                for selected, fields in pieces:
                    field = fields[name] if component is None else fields[name][component]
                    value[selected], derivative[selected] = field.v, field.d
                return Dual(value, derivative)

            merged = {name: tuple(merge_field(name, c) for c in range(len(field)))
                      if isinstance(field, tuple) else merge_field(name)
                      for name, field in state.uniform_fields.items()}
            if return_interpolation_diagnostics:
                merged["__interpolation_diagnostics"] = {
                    "parts": [fields["__interpolation_diagnostics"] for _, fields in pieces],
                    "actual_point_set_SHA256": points.identity,
                    "these_are_point_observations_not_a_uniform_Fourier_tail_certificate": True}
            return merged
        if np.all(on_grid):
            column = points.uniform_indices

            def gather(field):
                selected_column = np.zeros_like(column) if field.v.shape[1] == 1 else column
                return Dual(field.v[idx, selected_column][:, None],
                            field.d[idx, selected_column][:, None, :])

            values = {name: tuple(gather(component) for component in field)
                      if isinstance(field, tuple) else gather(field)
                      for name, field in state.uniform_fields.items()}
            if return_interpolation_diagnostics:
                diagnostics = []
                for order, actual_order in zip(state.primitives, state.uniform_tangent_values):
                    maxima = []
                    for spectral, actual in zip(order, actual_order):
                        derivative_grid = np.fft.ifft(
                            spectral.coefficients * (1j * self.frequencies)[None, :] * self.uniform.nt,
                            axis=1).real
                        maxima.append(float(np.max(np.abs(derivative_grid[idx, column] - actual[idx, column]))))
                    diagnostics.append(maxima)
                self.counts["diagnostic_uniform_FFTs"] += 9
                values["__interpolation_diagnostics"] = {
                    "sampled_Ptheta_minus_T_component_max": diagnostics[0],
                    "sampled_Ps_theta_minus_Ts_component_max": diagnostics[1],
                    "sampled_Pss_theta_minus_Tss_component_max": diagnostics[2],
                    "these_are_point_observations_not_a_uniform_Fourier_tail_certificate": True,
                    "FFT_nodes": self.uniform.nt, "actual_point_set_SHA256": points.identity}
            self.counts["point_evaluations"] += 1
            self.counts["point_values_evaluated"] += points.size
            self.counts["point_parameter_directions_evaluated"] += points.size * nd
            self.counts["uniform_points_gathered"] += points.size
            self.counts["point_seconds"] += time.monotonic() - started
            return values

        def linear(basis, start, base=0.0):
            count = basis.shape[-1]
            value = base + np.einsum("...k,k->...", basis, q[start:start + count])
            derivative = np.zeros(value.shape + (nd,))
            if nd:
                mask = (indices >= start) & (indices < start + count)
                derivative[..., mask] = basis[..., indices[mask] - start]
            return Dual(value, derivative)

        def at_points(field):
            return Dual(field.v[idx], field.d[idx])

        uc = points.core["u"][:, None]
        wm, wd, wdd = [getattr(self.uniform, name)[idx] for name in ("bg_wm", "bg_wd", "bg_wdd")]
        u = linear(points.angular_bases[0], 0, wm * uc)
        us = linear(points.angular_bases[1], 0, -wd * uc)
        uss = linear(points.angular_bases[2], 0, -wdd * uc)
        ut = linear(points.theta_basis, 0, wm * points.core["utheta"][:, None])
        v, vs, vss = [linear(b, self.uniform.block) for b in points.angular_bases]
        vt = linear(points.theta_basis, self.uniform.block)
        phase = u + points.angles[:, None]
        sine, cosine = phase.sin(), phase.cos()
        normalizer = (1 + v * v) ** -.5
        hs = -v * vs * normalizer ** 3
        hss = (2 * v * v - 1) * vs * vs * normalizer ** 5 - v * vss * normalizer ** 3
        ht = -v * vt * normalizer ** 3
        ring, ring1 = (-sine, cosine), (-cosine, -sine)
        t = tuple(a * normalizer for a in ring) + (v * normalizer,)
        ts = tuple(a1 * us * normalizer + a * hs for a, a1 in zip(ring, ring1)) + (vs * normalizer + v * hs,)
        tss = tuple((a1 * uss - a * us * us) * normalizer + 2 * a1 * us * hs + a * hss
                    for a, a1 in zip(ring, ring1)) + (vss * normalizer + 2 * vs * hs + v * hss,)
        tt = tuple(a1 * (1 + ut) * normalizer + a * ht for a, a1 in zip(ring, ring1)) + (vt * normalizer + v * ht,)
        p, ps, pss = [tuple(field.evaluate(idx, points.angles, self.frequencies, self.batch_size)
                             for field in order) for order in state.primitives]
        radius, radius1, radius2, z, z1, z2 = [at_points(field) for field in state.radial_jets]
        position = tuple(radius * pi + (z if i == 2 else 0) for i, pi in enumerate(p))
        xs = tuple(radius1 * pi + radius * psi + (z1 if i == 2 else 0)
                   for i, (pi, psi) in enumerate(zip(p, ps)))
        xss = tuple(radius2 * pi + 2 * radius1 * psi + radius * pssi + (z2 if i == 2 else 0)
                    for i, (pi, psi, pssi) in enumerate(zip(p, ps, pss)))
        eactual, factual = dot(xs, xs), dot(xs, t)
        # This is the same complete uniform quadrature mean and its exact
        # parameter derivative. Never average the nonuniform constraint points.
        ebar = at_points(state.mean_E)
        edenom = ebar.floor(1e-14)
        e, f = eactual / edenom - 1, factual / edenom ** .5
        det = eactual - factual * factual
        area = det.floor(1e-24) ** .5
        normal = tuple(component / area for component in cross(xs, t))
        second_l = dot(normal, xss)
        second_m = dot(normal, ts)
        second_n = dot(normal, tt) / radius
        determinant = det.floor(1e-24)
        trace = (second_l + eactual * second_n - 2 * factual * second_m) / determinant
        product = (second_l * second_n - second_m * second_m) / determinant
        discriminant = (trace * trace / 4 - product).floor(0)
        root = (discriminant + 1e-16) ** .5
        values = {"position": position, "Xs": xs, "T": t, "E": eactual, "F": factual,
                  "Ebar": ebar, "e": e, "f": f, "det": det, "area": radius * area,
                  "radius": radius, "normal": normal, "curvature": (trace / 2 + root, trace / 2 - root)}
        if not all(np.all(np.isfinite(values[name].v)) for name in ("E", "e", "f", "det")):
            raise FloatingPointError("nonfinite arbitrary-angle actual field values")
        if return_interpolation_diagnostics:
            diagnostics = []
            for order, true_fields in zip(state.primitives, (t, ts, tss)):
                maxima = []
                for spectral, actual in zip(order, true_fields):
                    derivative = spectral.evaluate(idx, points.angles, self.frequencies,
                                                   self.batch_size, angular_derivative_order=1)
                    maxima.append(float(np.max(np.abs(derivative.v - actual.v))))
                diagnostics.append(maxima)
            values["__interpolation_diagnostics"] = {
                "sampled_Ptheta_minus_T_component_max": diagnostics[0],
                "sampled_Ps_theta_minus_Ts_component_max": diagnostics[1],
                "sampled_Pss_theta_minus_Tss_component_max": diagnostics[2],
                "these_are_point_observations_not_a_uniform_Fourier_tail_certificate": True,
                "FFT_nodes": self.uniform.nt, "actual_point_set_SHA256": points.identity}
        self.counts["point_evaluations"] += 1
        self.counts["point_values_evaluated"] += points.size
        self.counts["point_parameter_directions_evaluated"] += points.size * nd
        self.counts["nonuniform_points_summed"] += points.size
        self.counts["point_seconds"] += time.monotonic() - started
        return values


class PointRows:
    """Values and exact block parameter columns at every declared actual point.

    This class does not find peaks, claim coverage, or accept optimizer steps.
    A later driver must supply full scanning and exchange/acceptance rules.
    It intentionally does not replace Ebar by a point-set average.
    """
    def __init__(self, oracle, points, phase="metric", mean_floor=.25,
                 det_floor=.1, margin=.001, block_size=16, deadline=None):
        if phase not in ("metric", "geometry_restoration"):
            raise ValueError("unknown hard-constraint phase")
        if mean_floor <= 0 or det_floor <= 0 or block_size < 1:
            raise ValueError("positive floors and AD block size required")
        self.oracle, self.points, self.phase = oracle, points, phase
        self.mean_floor, self.det_floor, self.margin = mean_floor, det_floor, margin
        self.block_size, self.deadline = int(block_size), deadline
        self.key, self.values, self.jacobian = None, None, None
        self.counts = {"value_keys": 0, "complete_jacobians": 0, "direction_blocks": 0,
                       "maximum_value_reconstruction_difference": 0.0,
                       "value_seconds": 0.0, "jacobian_seconds": 0.0}

    def check_time(self):
        if self.deadline is not None and time.monotonic() >= self.deadline:
            raise hard.EndSegment("angular-oracle interface reached its declared scientific clock")

    def groups(self, g, extra):
        groups = hard.fields_for_geometry(g, self.oracle.uniform.par, self.mean_floor, self.det_floor)
        groups = {name: field - (0 if name == "positive_height" else self.margin)
                  for name, field in groups.items()}
        flags = {name: self.phase == "geometry_restoration" for name in groups}
        if self.phase == "metric":
            norm = (g["e"] * g["e"] + 4 * g["f"] * g["f"] + 1e-24) ** .5
            groups["metric_plus"] = extra - (norm + g["e"]) / 2
            groups["metric_minus"] = extra - (norm - g["e"]) / 2
            flags.update(metric_plus=True, metric_minus=True)
        return groups, flags

    def fun(self, value):
        value = np.asarray(value, dtype=float)
        key = value.tobytes()
        if key == self.key:
            return self.values
        self.check_time()
        started = time.monotonic()
        state = self.oracle.prepare(value[:-1])
        g = self.oracle.evaluate(state, self.points)
        groups, _ = self.groups(g, float(value[-1]))
        values = np.concatenate([field.v.ravel() for field in groups.values()])
        if self.phase == "geometry_restoration":
            values = values + float(value[-1])
        if not np.all(np.isfinite(values)):
            raise FloatingPointError("nonfinite arbitrary-point hard inequalities")
        self.key, self.values, self.jacobian = key, values, None
        self.counts["value_keys"] += 1
        self.counts["value_seconds"] += time.monotonic() - started
        return values

    def jac(self, value):
        value = np.asarray(value, dtype=float)
        self.fun(value)
        if self.jacobian is not None:
            return self.jacobian
        started = time.monotonic()
        size = self.oracle.uniform.size
        answer = np.empty((len(self.values), size + 1))
        for first in range(0, size, self.block_size):
            self.check_time()
            indices = np.arange(first, min(first + self.block_size, size))
            state = self.oracle.prepare(value[:-1], indices)
            g = self.oracle.evaluate(state, self.points)
            groups, flags = self.groups(g, float(value[-1]))
            reconstructed = np.concatenate([field.v.ravel() for field in groups.values()])
            if self.phase == "geometry_restoration":
                reconstructed = reconstructed + float(value[-1])
            error = float(np.max(np.abs(reconstructed - self.values)))
            self.counts["maximum_value_reconstruction_difference"] = max(
                self.counts["maximum_value_reconstruction_difference"], error)
            if error > 1e-12 * max(1.0, float(np.max(np.abs(self.values)))):
                raise ArithmeticError("arbitrary-point block AD changed actual values or row identity")
            answer[:, indices] = np.vstack([field.d.reshape(-1, len(indices)) for field in groups.values()])
            if first == 0:
                answer[:, -1] = np.concatenate([
                    np.full(field.v.size, float(flag)) for field, flag in zip(groups.values(), flags.values())])
            self.counts["direction_blocks"] += 1
            self.oracle.release()
            del state, g, groups, reconstructed
        if not np.all(np.isfinite(answer)):
            raise FloatingPointError("nonfinite arbitrary-point exact parameter Jacobian")
        self.jacobian = answer
        self.counts["complete_jacobians"] += 1
        self.counts["jacobian_seconds"] += time.monotonic() - started
        return answer

