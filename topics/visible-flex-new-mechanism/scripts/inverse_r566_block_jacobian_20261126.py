#!/usr/bin/env python3
"""The same R566 analytic spatial jets, with selected forward-AD directions.

The geometry body after the parameter seed construction is copied verbatim
from the hash-bound physical model. No spatial finite differences are used.
Only the number/identity of forward parameter directions and cache key change.
Rows are evaluated without AD for line searches; exact block columns are
assembled on demand for SLSQP's Jacobian.
"""
import hashlib
from pathlib import Path
import time

import numpy as np

PHYSICAL_SOURCE_SHA256 = "b9c778fbeafb0d9beb061b3f472b8db1661daec5a78a63eb886a8e4770574f9b"
HARD_SOURCE_SHA256 = "befd444bfb96efc6721d1b0bad20deb25b32e915c1f789ab4d285085c2afcce4"
for filename, expected in (("inverse_flat_oscillatory_tail_20261126.py", PHYSICAL_SOURCE_SHA256),
                           ("inverse_hard_exchange_resume_20261126.py", HARD_SOURCE_SHA256)):
    if hashlib.sha256(Path(__file__).with_name(filename).read_bytes()).hexdigest() != expected:
        raise RuntimeError("blocked Jacobian requires its declared source: " + filename)
import inverse_flat_oscillatory_tail_20261126 as physical
import inverse_hard_exchange_resume_20261126 as hard

Dual, dot, cross, primitive = physical.Dual, physical.dot, physical.cross, physical.primitive
DesignClockLimit = physical.DesignClockLimit
SCHEMA = "r566-selected-forward-directions-and-value-only-line-search-v1"


class Model(physical.Model):
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
        self.cache_key, self.cache = key, values
        self.last_completed_q = q.copy()
        return values


def reduced_values(field):
    """Exactly the value order of hard.reduced_rows, including all orbit nodes."""
    nr, nt = field.v.shape
    if nt == 1:
        return field.v.ravel()
    if nt % 4:
        raise ValueError("full angular grid must be divisible by four")
    j = np.arange(nt // 4 + 1)
    orbit = np.stack((j, (-j) % nt, (nt // 2 - j) % nt, (nt // 2 + j) % nt), axis=-1)
    choices = np.argmin(field.v[:, orbit], axis=-1)
    index = orbit[np.arange(len(j))[None, :], choices]
    return field.v[np.arange(nr)[:, None], index].ravel()


class NonlinearRows:
    """Hard inequalities unchanged; value and derivative work explicitly counted."""
    block_size = 16

    def __init__(self, model, mean_floor, det_floor, phase, deadline, margin):
        self.model, self.mean_floor, self.det_floor = model, mean_floor, det_floor
        self.phase, self.deadline, self.margin = phase, deadline, margin
        self.key, self.values, self.jacobian = None, None, None
        self.evaluations = 0
        self.jacobian_evaluations = 0
        self.directional_block_evaluations = 0

    def groups(self, g, extra):
        groups = hard.fields_for_geometry(g, self.model.par, self.mean_floor, self.det_floor)
        groups = {name: field - (0 if name == "positive_height" else self.margin)
                  for name, field in groups.items()}
        flags = {name: self.phase == "geometry_restoration" for name in groups}
        if self.phase != "geometry_restoration":
            norm = (g["e"] * g["e"] + 4 * g["f"] * g["f"] + 1e-24) ** .5
            groups["metric_plus"] = extra - (norm + g["e"]) / 2
            groups["metric_minus"] = extra - (norm - g["e"]) / 2
            flags.update(metric_plus=True, metric_minus=True)
        return groups, flags

    def check_time(self):
        if time.monotonic() >= self.deadline:
            raise hard.EndSegment("scientific clock reached before the next exact block evaluation")

    def fun(self, value):
        value = np.asarray(value, dtype=float)
        key = value.tobytes()
        if key == self.key:
            return self.values
        self.check_time()
        g = self.model.geometry(value[:-1], differentiate=False, ignore_clock=True)
        groups, _ = self.groups(g, float(value[-1]))
        values = np.concatenate([reduced_values(field) for field in groups.values()])
        if self.phase == "geometry_restoration":
            # Preserve the old floating active-row selection: choose the
            # orbit minimum before adding the common uniform slack.
            values = values + float(value[-1])
        if not np.all(np.isfinite(values)):
            raise FloatingPointError("nonfinite actual hard-constraint values")
        self.key, self.values, self.jacobian = key, values, None
        self.evaluations += 1
        return values

    def jac(self, value):
        value = np.asarray(value, dtype=float)
        self.fun(value)
        if self.jacobian is not None:
            return self.jacobian
        started = time.monotonic()
        q, extra = value[:-1], float(value[-1])
        jacobian = np.empty((len(self.values), self.model.size + 1))
        reconstruction_difference = 0.0
        blocks = 0
        for first in range(0, self.model.size, self.block_size):
            self.check_time()
            indices = np.arange(first, min(first + self.block_size, self.model.size))
            g = self.model.geometry(q, differentiate=True, ignore_clock=True,
                                    parameter_indices=indices)
            groups, flags = self.groups(g, extra)
            rows = [hard.reduced_rows(field) for field in groups.values()]
            reconstructed = np.concatenate([row[0] for row in rows])
            if self.phase == "geometry_restoration":
                reconstructed = reconstructed + extra
            difference = float(np.max(np.abs(reconstructed - self.values)))
            reconstruction_difference = max(reconstruction_difference, difference)
            if difference > 1e-12 * max(1.0, float(np.max(np.abs(self.values)))):
                raise ArithmeticError("blocked AD changed the actual inequality values or row order")
            jacobian[:, indices] = np.vstack([row[1] for row in rows])
            if blocks == 0:
                jacobian[:, -1] = np.concatenate([
                    np.full(len(row[0]), float(flag)) for row, flag in zip(rows, flags.values())])
            blocks += 1
            self.directional_block_evaluations += 1
            # Release the block before constructing the next one. The full
            # assembled Jacobian is the only object with all parameter columns.
            self.model.cache, self.model.cache_key = None, None
            del g, groups, rows, reconstructed
        if not np.all(np.isfinite(jacobian)):
            raise FloatingPointError("nonfinite exact assembled constraint Jacobian")
        self.jacobian = jacobian
        self.jacobian_evaluations += 1
        hard.emit("JOINT_BUDGET_JACOBIAN", {
            "operator_schema": SCHEMA, "phase": self.phase,
            "constraint_radial_nodes": self.model.nr, "constraint_theta_nodes": self.model.nt,
            "inequality_rows": len(self.values), "physical_parameter_columns": self.model.size,
            "block_size": self.block_size, "blocks_this_jacobian": blocks,
            "value_evaluations_this_outer": self.evaluations,
            "jacobian_evaluations_this_outer": self.jacobian_evaluations,
            "directional_block_evaluations_this_outer": self.directional_block_evaluations,
            "maximum_value_reconstruction_difference": reconstruction_difference,
            "seconds_this_jacobian": time.monotonic() - started,
            "finite_difference_parameter_Jacobian": False})
        return jacobian

