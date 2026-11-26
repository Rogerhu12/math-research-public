#!/usr/bin/env python3
"""Finite R582 design with explicit local columns following its actual tail.

The first 80 coordinates and final height retain the original physical
meaning. Sixteen added coordinates multiply the actual frozen material
seed by four C-infinity onset functions and sine modes 2 and 4. They are
new inverse-design variables, not an assertion of an exact flat branch.
The parametric spatial geometry and selected-parameter AD are unchanged.
"""
from dataclasses import replace
from collections import defaultdict
import hashlib
from pathlib import Path
import time

import numpy as np

BINDINGS = {
    "r582_finite_resonant_model_20261126.py":
        "584f02a67af1c0e87a68dac629d6e17b9b1bad93cef2c4c65b5a3b0c2253639f",
    "r582_stable_material_field_20261126.py":
        "070acb1c46a4df055e84722227916a2997f3b6bba9bfaa3cc8c0ba820b8f71e8",
    "inverse_r566_block_jacobian_20261126.py":
        "c0ab647ed2c6c0647c9031995696d40bc2c6717b893f67cf7c6a345c5366ef6b",
    "r582_paid_resonant_field_20261126.py":
        "1b046b20541fcee05d5c8722dfdd5a509e7018348aab7182bec77c0813a8b395",
}
for filename, expected in BINDINGS.items():
    if hashlib.sha256(Path(__file__).with_name(filename).read_bytes()).hexdigest() != expected:
        raise RuntimeError("finite resonant model source binding differs: " + filename)
import inverse_r566_block_jacobian_20261126 as blocked
from r582_paid_resonant_field_20261126 import REFERENCE_CONTROL, REFERENCE_CORE_RADIUS
from r582_actual_circle_seed_and_return_20261126 import compact_bump
from r582_continuous_mean_profile_20261126 import ContinuousMean

physical, hard = blocked.physical, blocked.hard
Dual, dot, cross, primitive = blocked.Dual, blocked.dot, blocked.cross, blocked.primitive
DesignClockLimit = blocked.DesignClockLimit
Parameters = physical.Parameters
SCHEMA = "r582-stable-material-local-tail-columns-parametric-finite-design-v1"
TAIL_GATES = ((.78,.82),(.82,.84),(.84,.86),(.86,.88))
TAIL_MODES = (2,4)
TAIL_COLUMN_COUNT = len(TAIL_GATES)*len(TAIL_MODES)
TAIL_EXTRA_COUNT = 2*TAIL_COLUMN_COUNT
ORIGINAL_COORDINATES_WITHOUT_HEIGHT = 80
COUNTS = defaultdict(int)


class Model(blocked.Model):
    def __init__(self, par, radial_nodes, theta_nodes, field):
        if (par.q != .18 or par.offset != .2 or par.p < par.q
                or par.length != .9 or par.radial_count != 8 or par.modes != 4
                or par.cap_disk_radius != .22 or par.core_collar_end != .036
                or par.cap_collar_width != 0 or par.core_half_width != .02):
            raise ValueError("finite seed only binds its identified actual circular reference")
        s = np.linspace(0., par.length, int(radial_nodes)) if np.isscalar(radial_nodes) else np.asarray(radial_nodes, dtype=float)
        if (s.ndim != 1 or len(s) < 5 or s[0] != 0 or s[-1] != par.length
                or not np.all(np.isfinite(s)) or not np.all(np.diff(s) > 0)
                or theta_nodes < 4 * par.modes + 4 or theta_nodes % 4):
            raise ValueError("finite model needs a complete increasing grid and fourfold angular sampling")
        self.par, self.s, self.field = par, s.copy(), field
        self.nr, self.nt = len(s), int(theta_nodes)
        COUNTS["attempted_model_grid_constructions"] += 1
        COUNTS["model_radial_points_prepared"] += self.nr
        self.theta = np.arange(self.nt) * (2 * np.pi / self.nt)
        self.core = physical.reference.rounded_core(par, self.theta)
        self.w, self.wm, self.wd, self.wdd, self.bases = physical.reference.radial_data(par, self.s)
        angular = 2 * np.arange(1, par.modes + 1)[:, None]
        self.sine, self.cosine = np.sin(angular * self.theta), angular * np.cos(angular * self.theta)
        self.block, self.size = par.radial_count * par.modes, 2 * par.radial_count * par.modes + 2 * par.radial_count + 1
        self.metric_weights = np.ones((self.nr, self.nt))
        self.cache_key, self.cache, self.deadline, self.last_completed_q = None, None, None, None
        bgpar = replace(par, cap_collar_width=physical.TAIL_EXTENT)
        self.bg_w, self.bg_wm, self.bg_wd, self.bg_wdd, _ = physical.reference.radial_data(bgpar, self.s)
        self.tail_height, self.tail_height1, self.tail_height2, self.tail_quadrature = physical.tail_height_and_jets(par, self.s)
        self.tail_start = par.length - physical.TAIL_EXTENT
        self.endpoint_decay_rate = (par.length - par.core_collar_end) / physical.TAIL_ELL
        self.explicit_radial_sampling = True
        self.epsilon = par.p - par.q
        uj, vj = field.angular_radial_jets(self.s, self.bg_wm, self.bg_wd, self.bg_wdd)
        sine2, cosine2 = np.sin(2 * self.theta)[None, :], 2 * np.cos(2 * self.theta)[None, :]
        self.seed_u = [self.epsilon * uj[:, i, None] * sine2 for i in range(3)]
        self.seed_v = [self.epsilon * vj[:, i, None] * sine2 for i in range(3)]
        self.seed_ut = self.epsilon * uj[:, 0, None] * cosine2
        self.seed_vt = self.epsilon * vj[:, 0, None] * cosine2
        bump = compact_bump(self.s)
        self.mean_control_alpha = [REFERENCE_CONTROL[0] * bump[:, i, None] for i in range(3)]
        self.mean_control_z = [REFERENCE_CONTROL[1] * bump[:, i, None] for i in range(3)]
        # Original prefix q[0:80] is literal; new u/v coefficients precede
        # the unchanged final height. At zero new coefficients the old q embeds.
        self.size = 81 + TAIL_EXTRA_COUNT
        self.tail_sine = np.sin(np.asarray(TAIL_MODES)[:,None]*self.theta)
        self.tail_cosine = np.asarray(TAIL_MODES)[:,None]*np.cos(np.asarray(TAIL_MODES)[:,None]*self.theta)
        self.tail_bases_u = [np.empty((self.nr,len(TAIL_GATES))) for _ in range(3)]
        self.tail_bases_v = [np.empty((self.nr,len(TAIL_GATES))) for _ in range(3)]
        for j,(left,right) in enumerate(TAIL_GATES):
            chi,comp,d1,d2 = ContinuousMean.step_jets(self.s,left,right)
            for radial,output in ((self.epsilon*uj,self.tail_bases_u),
                                  (self.epsilon*vj,self.tail_bases_v)):
                output[0][:,j] = chi*radial[:,0]
                output[1][:,j] = d1*radial[:,0]+chi*radial[:,1]
                output[2][:,j] = d2*radial[:,0]+2*d1*radial[:,1]+chi*radial[:,2]
        self.geometry_value_calls = self.geometry_AD_calls = self.geometry_parameter_directions = 0

    def bounds(self):
        lower,upper = -12*np.ones(self.size),12*np.ones(self.size)
        lower[64:72],upper[64:72] = -1.5,1.5
        lower[72:80],upper[72:80] = -1.,1.
        lower[80:-1],upper[80:-1] = -2.,2.
        lower[-1],upper[-1] = .08,.8
        return lower,upper

    @staticmethod
    def coordinate_scope():
        return {"physical_coordinate_count":81+TAIL_EXTRA_COUNT,
            "old_prefix_entries":80,"old_height_is_final_coordinate":True,
            "new_tail_entries":TAIL_EXTRA_COUNT,"new_tail_mode_order":list(TAIL_MODES),
            "new_tail_onset_intervals":[list(x) for x in TAIL_GATES],
            "tail_coefficient_order":"u then v; onset-major, angle-mode-minor",
            "tail_columns_include_current_fixed_epsilon":True,
            "tail_columns_use_same_material_field_value_and_two_derivatives":True,
            "zero_extra_columns_embed_the_identified_original_q":True,
            "tail_columns_are_zero_through_s_0_78_and_share_zero_seed_suffix":True,
            "new_columns_do_not_certify_the_infinite_flat_kernel_or_fixed_g_family":True}

    def geometry(self, q, differentiate=True, ignore_clock=False, parameter_indices=None):
        """Same parametric geometry, with the frozen predictor and 16 new columns.

        The position primitive and metric/curvature formulas are retained.
        The new material seed's actual C2 Hermite derivatives and the
        explicit onset-product jets are used.
        The q derivative is selected forward AD; p and the seed are fixed
        during each stage. No division by a_s or z_s occurs here.
        """
        q = np.asarray(q, dtype=float)
        indices = (np.arange(self.size, dtype=int) if parameter_indices is None
                   else np.asarray(parameter_indices, dtype=int)) if differentiate else np.empty(0, dtype=int)
        if (indices.ndim != 1 or np.any(indices < 0) or np.any(indices >= self.size)
                or len(np.unique(indices)) != len(indices)):
            raise ValueError("invalid selected parameter directions")
        key = (q.tobytes(), tuple(indices.tolist()))
        if self.cache_key == key:
            COUNTS["geometry_cache_hits"] += 1
            return self.cache
        if not ignore_clock and self.deadline is not None and time.monotonic() >= self.deadline:
            raise DesignClockLimit("declared Actions segment reached; R566 design is not complete")
        if q.shape != (self.size,) or not np.all(np.isfinite(q)):
            raise ValueError("invalid physical parameter vector")
        self.cache, self.cache_key = None, None
        self.geometry_value_calls += int(not differentiate)
        self.geometry_AD_calls += int(differentiate)
        self.geometry_parameter_directions += len(indices)
        COUNTS["attempted_geometry_value_calls"] += int(not differentiate)
        COUNTS["attempted_geometry_AD_blocks"] += int(differentiate)
        COUNTS["geometry_spatial_points_requested"] += self.nr * self.nt
        COUNTS["geometry_parameter_direction_points_requested"] += self.nr * self.nt * len(indices)
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

        def angular(index, start, base=0., theta_derivative=False):
            basis = self.bases[index]
            trigonometric = self.cosine if theta_derivative else self.sine
            coefficients = q[start:start + self.block].reshape(self.par.radial_count, self.par.modes)
            value = base + (basis @ coefficients) @ trigonometric
            derivative = np.zeros(value.shape + (nd,))
            if nd:
                mask = (indices >= start) & (indices < start + self.block)
                local = indices[mask] - start
                derivative[..., mask] = (basis[:, local // self.par.modes][:, None, :]
                    * trigonometric[local % self.par.modes, :].T[None, :, :])
            if start not in (0,self.block):
                raise ValueError("local tail columns requested outside angular fields")
            extra_start = 80 if start == 0 else 80+TAIL_COLUMN_COUNT
            extra_basis = (self.tail_bases_u if start == 0 else self.tail_bases_v)[index]
            extra_trig = self.tail_cosine if theta_derivative else self.tail_sine
            extra_coefficients = q[extra_start:extra_start+TAIL_COLUMN_COUNT].reshape(len(TAIL_GATES),len(TAIL_MODES))
            value = value + (extra_basis @ extra_coefficients) @ extra_trig
            if nd:
                mask = (indices >= extra_start) & (indices < extra_start+TAIL_COLUMN_COUNT)
                local = indices[mask]-extra_start
                derivative[...,mask] = (extra_basis[:,local//len(TAIL_MODES)][:,None,:]
                    * extra_trig[local%len(TAIL_MODES),:].T[None,:,:])
            return Dual(value, derivative)

        h = constant(q[-1])
        if nd:
            h.d[indices == self.size - 1] = 1
        uc = self.core["u"][None, :]
        u = angular(0, 0, self.bg_wm * uc + self.seed_u[0])
        us = angular(1, 0, -self.bg_wd * uc + self.seed_u[1])
        uss = angular(2, 0, -self.bg_wdd * uc + self.seed_u[2])
        ut = angular(0, 0, self.bg_wm * self.core["utheta"][None, :]
                     + self.seed_ut, theta_derivative=True)
        v, vs, vss = [angular(i, self.block, self.seed_v[i]) for i in range(3)]
        vt = angular(0, self.block, self.seed_vt, theta_derivative=True)
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
        alpha, alphas, alphass = [radial(i, astart) + self.mean_control_alpha[i] for i in range(3)]
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
        z = (self.bg_wm * central + self.bg_w * tail_z + radial(0, zstart)
             + self.mean_control_z[0])
        z1 = (self.bg_wm + self.bg_wd * (tail_z - central)
              + self.bg_w * self.tail_height1 + radial(1, zstart) + self.mean_control_z[1])
        z2 = (-2 * self.bg_wd + self.bg_wdd * (tail_z - central)
              + 2 * self.bg_wd * self.tail_height1
              + self.bg_w * self.tail_height2 + radial(2, zstart) + self.mean_control_z[2])

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

