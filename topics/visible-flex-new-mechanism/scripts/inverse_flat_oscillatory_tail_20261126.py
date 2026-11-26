#!/usr/bin/env python3
"""New inverse-design identity with the fixed R566 oscillatory cap tail.

The nonround-core background becomes exactly the R566 radial graph before
the final 0.08 of the meridian. Free corrections remain allowed throughout
every s < L; only the attached open disk r < 0.22 is fixed. This is a search
over rotational target metrics, not frozen-metric refinement.

Scientific execution belongs to the public Actions workflow. The imported
v2 solver source is hash-bound; its currently running physical identity is
not modified by this file.
"""
import argparse
from dataclasses import asdict, dataclass, replace
import hashlib
import json
from pathlib import Path
import time

import numpy as np
from scipy.integrate import quad
from scipy.optimize import least_squares

REFERENCE_SHA256 = "e25dff6a411e8edc485babe6545087cfbea2b6d16cd804e6dcb51f17d8fab319"
REFERENCE_PATH = Path(__file__).with_name("inverse_rotational_metric_20261126.py")
if hashlib.sha256(REFERENCE_PATH.read_bytes()).hexdigest() != REFERENCE_SHA256:
    raise RuntimeError("R566 model requires its explicitly bound v2 reference source")

import inverse_rotational_metric_20261126 as reference

Dual = reference.Dual
dot = reference.dot
cross = reference.cross
primitive = reference.primitive
emit = reference.emit
DesignClockLimit = reference.DesignClockLimit

SCHEMA = "inverse-rotational-metric-r566-tail-v1"
TAIL_A = 0.1
TAIL_ELL = 0.2
TAIL_EXTENT = 0.08
TAIL_RADIUS = 0.22
QUADRATURE_DELTA_CUT = 0.03
QUADRATURE_HEIGHT_ABS_TARGET = 1e-14
K0 = (75 / 8) * np.exp(-2.5) + 256 * np.exp(-4)


@dataclass(frozen=True)
class Parameters(reference.Parameters):
    # Zero removes v2's frozen circular suffix. The flat disk is attached at L.
    cap_collar_width: float = 0.0


def tail_height_and_jets(par, s):
    """Numerical evaluation of the one fixed analytic height definition.

    Mathematically H(r) = -integral_rc^r w(t) dt for every r > rc.
    For height values only, omitting delta <= 0.03 has a rigorous absolute
    bound A*ell*delta_cut*exp(-1/delta_cut). Slopes are evaluated from the
    full analytic formula, not from a cut-off height or spline. QUADPACK's
    accumulated error estimate is reported separately and is not a proof.
    """
    delta = (par.length - s) / TAIL_ELL
    positive = delta > 0
    slope = np.zeros_like(s)
    radial_slope_derivative = np.zeros_like(s)
    d = delta[positive]
    phase = d ** -2
    log_factor = -(2 - np.sin(phase)) / d
    log_first = (2 - np.sin(phase)) / d ** 2 - 2 * np.cos(phase) / d ** 4
    with np.errstate(under="ignore"):
        slope[positive] = TAIL_A * np.exp(log_factor)
        radial_slope_derivative[positive] = slope[positive] * log_first / TAIL_ELL

    maximum = float(np.max(delta))
    cut = min(QUADRATURE_DELTA_CUT, maximum)
    omitted_bound = TAIL_A * TAIL_ELL * cut * np.exp(-1 / cut) if cut > 0 else 0.0
    height = np.zeros_like(s)
    total_error, intervals = 0.0, 0
    if maximum > cut:
        quarter = np.pi / 2
        kfirst = max(1, int(np.ceil(1 / maximum ** 2 / quarter)))
        klast = int(np.floor(1 / cut ** 2 / quarter))
        oscillation_breaks = 1 / np.sqrt(np.arange(kfirst, klast + 1) * quarter)
        requested = delta[delta > cut]
        breaks = np.unique(np.r_[cut, maximum, requested,
                                 oscillation_breaks[(oscillation_breaks > cut)
                                                    & (oscillation_breaks < maximum)]])
        intervals = len(breaks) - 1
        absolute_per_interval = QUADRATURE_HEIGHT_ABS_TARGET / (
            TAIL_A * TAIL_ELL * max(intervals, 1))

        def integrand(value):
            return np.exp(-(2 - np.sin(value ** -2)) / value)

        increments, estimates = [], []
        for left, right in zip(breaks[:-1], breaks[1:]):
            value, error = quad(integrand, left, right,
                                epsabs=absolute_per_interval, epsrel=1e-13, limit=100)
            increments.append(value)
            estimates.append(error)
        cumulative = np.r_[0.0, np.cumsum(increments)]
        selected = delta > cut
        height[selected] = -TAIL_A * TAIL_ELL * cumulative[np.searchsorted(breaks, delta[selected])]
        total_error = TAIL_A * TAIL_ELL * float(np.sum(estimates))
    receipt = {
        "mathematical_formula": "w=A*exp(-(2-sin(delta^-2))/delta), H=-integral(w dr)",
        "delta_definition": "(r-rc)/ell=(L-s)/ell for the exact tail background",
        "height_quadrature_delta_cut": cut,
        "omitted_height_upper_bound": float(omitted_bound),
        "quadrature_height_absolute_target": QUADRATURE_HEIGHT_ABS_TARGET,
        "sum_of_QUADPACK_absolute_error_estimates": total_error,
        "quadrature_intervals": intervals,
        "quadrature_error_is_not_interval_certification": True,
        "mathematical_input_is_not_truncated_at_quadrature_cut": True,
        "analytic_slopes_used": True,
    }
    # H_s=w because r_s=-1; H_ss=-w_r.
    return height[:, None], slope[:, None], -radial_slope_derivative[:, None], receipt


class Model(reference.Model):
    def __init__(self, par, radial_nodes, theta_nodes):
        # An adaptive solver may pass its explicit full-domain radial node array.
        # The physical basis and coefficient order never depend on these nodes.
        radial_positions = None
        if not np.isscalar(radial_nodes):
            radial_positions = np.asarray(radial_nodes, dtype=float)
            if (radial_positions.ndim != 1 or len(radial_positions) < 5
                    or not np.all(np.isfinite(radial_positions))
                    or not np.all(np.diff(radial_positions) > 0)
                    or radial_positions[0] != 0 or radial_positions[-1] != par.length):
                raise ValueError("explicit radial nodes must increase strictly from 0 to L")
            radial_nodes = len(radial_positions)
        if par.cap_collar_width != 0 or par.cap_disk_radius != TAIL_RADIUS:
            raise ValueError("this identity uses no frozen suffix and the fixed R566 radius 0.22")
        if par.length - TAIL_EXTENT <= par.core_collar_end:
            raise ValueError("R566 background tail must follow a positive core blend interval")
        if (par.length - par.core_collar_end) / TAIL_ELL <= 3:
            raise ValueError("free endpoint envelope must decay faster than exp(-3/delta)")
        super().__init__(par, radial_nodes, theta_nodes)
        self.explicit_radial_sampling = radial_positions is not None
        if radial_positions is not None:
            self.s = radial_positions.copy()
            self.w, self.wm, self.wd, self.wdd, self.bases = reference.radial_data(par, self.s)
            angular = 2 * np.arange(1, par.modes + 1)[:, None]
            sine = np.sin(angular * self.theta)
            cosine = angular * np.cos(angular * self.theta)
            self.angular_bases = [np.einsum("rj,mt->rtjm", b, sine).reshape(self.nr, self.nt, -1)
                                  for b in self.bases]
            self.theta_basis = np.einsum("rj,mt->rtjm", self.bases[0], cosine).reshape(self.nr, self.nt, -1)
        background_par = replace(par, cap_collar_width=TAIL_EXTENT)
        self.bg_w, self.bg_wm, self.bg_wd, self.bg_wdd, _ = reference.radial_data(background_par, self.s)
        self.tail_height, self.tail_height1, self.tail_height2, self.tail_quadrature = tail_height_and_jets(par, self.s)
        self.tail_start = par.length - TAIL_EXTENT
        self.endpoint_decay_rate = (par.length - par.core_collar_end) / TAIL_ELL

    def geometry(self, q, differentiate=True, ignore_clock=False):
        """v2 analytic spatial jets with the declared R566 background replaced.

        The unit tangent, periodic primitive, forward parameter derivative,
        actual fundamental forms and shape operator are the same formulas
        as the hash-bound reference. Only physical background profiles and
        the endpoint of the freely varying radial basis have changed.
        """
        q = np.asarray(q, dtype=float)
        key = q.tobytes()
        if self.cache_key == key and (not differentiate or self.cache["E"].size):
            return self.cache
        if not ignore_clock and self.deadline is not None and time.monotonic() >= self.deadline:
            raise DesignClockLimit("declared Actions segment reached; R566 design is not complete")
        if q.shape != (self.size,) or not np.all(np.isfinite(q)):
            raise ValueError("invalid physical parameter vector")
        self.cache, self.cache_key = None, None
        nd = self.size if differentiate else 0

        def constant(value):
            value = np.asarray(value, dtype=float)
            return Dual(value, np.zeros(value.shape + (nd,)))

        def linear(basis, start, base=0.0):
            count = basis.shape[-1]
            value = base + np.einsum("...k,k->...", basis, q[start:start + count])
            derivative = np.zeros(np.shape(value) + (nd,))
            if nd:
                derivative[..., start:start + count] = basis
            return Dual(value, derivative)

        def radial(index, start):
            return linear(self.bases[index][:, None, :], start)

        h = constant(q[-1])
        if nd:
            h.d[-1] = 1
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

    def summary(self, q):
        report = super().summary(q)
        report["R566_tail_identity"] = {
            "background_tail_s_interval": [self.tail_start, self.par.length],
            "background_tail_r_interval": [TAIL_RADIUS, TAIL_RADIUS + TAIL_EXTENT],
            "nonradial_corrections_allowed_at_every_interior_tail_point": True,
            "flat_disk_is_attached_at_s": self.par.length,
            "exact_background_tail_at_zero_nonheight_coordinates": bool(np.all(np.asarray(q)[:-1] == 0)),
            "background_graph_Hessian_upper_bound": float(K0),
            "background_graph_patch_reach_lower_bound": float(1 / K0),
            "free_endpoint_exponential_rate_in_delta": self.endpoint_decay_rate,
            "R566_bound_does_not_certify_a_perturbed_candidate_or_cross_block_pairs": True,
        }
        report["tail_height_quadrature"] = self.tail_quadrature
        report["radial_sampling"] = {
            "explicit_radial_sampling": self.explicit_radial_sampling,
            "positions": self.s.tolist(),
            "physical_family_is_independent_of_sampling_nodes": True,
        }
        return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for option, default in (("radial-basis", 8), ("modes", 4), ("radial-nodes", 49),
                            ("theta-nodes", 96), ("outer", 3), ("nfev", 60), ("verify-multiplier", 2)):
        parser.add_argument("--" + option, type=int, default=default)
    for option, default in (("cap-height", .22), ("length", .9), ("core-p", .85), ("core-q", .15),
                            ("rounding-radius", .15), ("curvature-weight", .05), ("shape-weight", .1),
                            ("regularization", 1e-5), ("maximum-seconds", 2400.0)):
        parser.add_argument("--" + option, type=float, default=default)
    parser.add_argument("--directional-check", action="store_true")
    parser.add_argument("--seed-json", help="JSON coordinate vector; reuse from v2 changes its physical identity")
    args = parser.parse_args()
    started = time.monotonic()
    par = Parameters(p=args.core_p, q=args.core_q, offset=args.rounding_radius, length=args.length,
                     radial_count=args.radial_basis, modes=args.modes)
    model = Model(par, args.radial_nodes, args.theta_nodes)
    model.deadline = started + args.maximum_seconds
    q = model.initial(args.cap_height)
    if args.seed_json:
        with open(args.seed_json, encoding="utf-8") as source:
            q = np.asarray(json.load(source), dtype=float)
    lower, upper = model.bounds()
    if q.shape != (model.size,) or not np.all(np.isfinite(q)) or np.any(q < lower) or np.any(q > upper):
        raise ValueError("seed must be a finite in-bounds vector in the declared R566 identity")
    definition = {
        "schema": SCHEMA, "parameters": asdict(par), "solver": vars(args),
        "reference_source_sha256": REFERENCE_SHA256,
        "this_source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "coordinate_order": ["u radial-major sin2..sin2m", "v radial-major sin2..sin2m",
                             "log-radius", "height-displacement", "cap-height"],
        "free_radial_step": "W=exp(-1/x)/(exp(-1/x)+exp(-1/(1-x))); x=(s-left)/(L-left)",
        "free_radial_envelope": "4*W*(1-W), positive for every left<s<L; zero exterior",
        "background_step": "same C-infinity step, but its right endpoint is L-0.08",
        "background_tail": {
            "radius": "0.22+L-s", "height": "h_cap-integral_0.22^radius w(r) dr",
            "w": "0.1*exp(-(2-sin(delta^-2))/delta)", "delta": "(r-0.22)/0.2",
            "formula_extends_to_all_r_above_rc_for_middle_blend": True,
            "R566_Hessian_bound_only_for_r_le_0p30": True,
        },
        "open_hold_disk": "r<0.22 at z=h_cap; exact after attachment at s=L",
        "outer_tail_jets": "background blend is already exactly one at s=L-0.08; no finite jet truncation",
        "basis_degree": 5,
        "position": "a*zero-mean periodic primitive(T)+z*ez",
        "T": "(-sin(theta+u),cos(theta+u),v)/sqrt(1+v*v)",
        "target_during_design": "g=mean_theta(E)*ds^2+a^2*dtheta^2; allowed to vary",
        "parameter_Jacobian": "v2 vectorized forward differential through analytic spatial jets",
        "new_physical_identity_relative_to_v2": True,
        "v2_seed_reuse_is_only_initialization_not_same_metric_or_same_surface": bool(args.seed_json),
        "all_product_grid_points_in_metric_residual": True,
        "finite_angular_quadrature_is_not_continuous_space_certification": True,
        "R566_is_not_an_existence_theorem_for_a_nonradial_equal_metric_branch": True,
        "old_scopes_replayed": False, "README_completion_claim": False,
    }
    emit("INVERSE_DESIGN_DEFINITION", definition)
    emit("INVERSE_DESIGN_INITIAL", model.summary(q))
    kwargs = {"curvature_weight": args.curvature_weight, "shape_weight": args.shape_weight,
              "regularization": args.regularization}
    termination = "declared_outer_iterations_returned"
    completed_outer = 0
    try:
        if args.directional_check:
            direction = np.sin(np.arange(model.size) + .37)
            direction /= np.linalg.norm(direction)
            step = 1e-6
            analytic = model.residual(q, jacobian=True, **kwargs) @ direction
            finite = (model.residual(q + step * direction, **kwargs)
                      - model.residual(q - step * direction, **kwargs)) / (2 * step)
            relative = float(np.linalg.norm(analytic - finite) / max(np.linalg.norm(finite), 1e-14))
            emit("INVERSE_DESIGN_DIRECTIONAL_DERIVATIVE", {
                "relative_l2_difference": relative, "step": step,
                "same_actual_residual": True, "scientific_cost_is_in_this_run": True})
            if not relative < 3e-4:
                raise ArithmeticError("R566 full-domain parameter derivative failed its directional check")
        for outer in range(args.outer):
            result = least_squares(lambda x: model.residual(x, **kwargs), q,
                                   jac=lambda x: model.residual(x, jacobian=True, **kwargs),
                                   bounds=(lower, upper), x_scale="jac", tr_solver="lsmr",
                                   max_nfev=args.nfev, ftol=1e-10, xtol=1e-10, gtol=1e-9,
                                   tr_options={"maxiter": 180, "atol": 1e-8, "btol": 1e-8})
            q = result.x.copy()
            completed_outer += 1
            emit("INVERSE_DESIGN_OUTER", {
                "outer": outer, "status": int(result.status), "success": bool(result.success),
                "message": str(result.message), "nfev": int(result.nfev), "njev": int(result.njev),
                "cost": float(result.cost), "optimality": float(result.optimality),
                "elapsed_seconds": time.monotonic() - started, "geometry": model.summary(q),
                "coordinates": q.tolist(), "optimizer_success_is_not_geometric_acceptance": True})
            eta = model.eta(q)
            maximum = float(np.max(eta))
            if maximum > 0:
                radial_max = np.max(eta, axis=1, keepdims=True)
                hot = (eta >= .8 * maximum) | (eta >= .95 * radial_max)
                model.metric_weights = np.minimum(model.metric_weights * np.where(hot, 4.0, 1.0), 1e4)
    except DesignClockLimit as error:
        termination = "segment_time_checkpoint_not_completed"
        if model.last_completed_q is not None:
            q = model.last_completed_q.copy()
        emit("INVERSE_DESIGN_TIME_CHECKPOINT", {
            "message": str(error), "coordinates": q.tolist(),
            "completed_outer": completed_outer, "elapsed_seconds": time.monotonic() - started,
            "this_is_not_an_OptimizeResult": True, "README_completion_claim": False})
    except Exception as error:
        emit("INVERSE_DESIGN_ERROR_CHECKPOINT", {
            "type": type(error).__name__, "message": str(error),
            "coordinates": (model.last_completed_q if model.last_completed_q is not None else q).tolist(),
            "completed_outer": completed_outer, "elapsed_seconds": time.monotonic() - started,
            "README_completion_claim": False})
        raise
    final = {
        "definition": definition, "coordinates": q.tolist(), "coarse": model.summary(q),
        "termination": termination, "completed_outer": completed_outer,
        "not_a_frozen_metric_refinement_claim": True, "all_pair_reach_not_checked": True,
        "complete": False}
    if args.verify_multiplier > 1:
        refined = Model(par, (args.radial_nodes - 1) * args.verify_multiplier + 1,
                        args.theta_nodes * args.verify_multiplier)
        final["same_coefficients_finer_evaluation"] = refined.summary(q)
    final["elapsed_seconds"] = time.monotonic() - started
    raw = json.dumps(final, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    emit("INVERSE_DESIGN_FINAL", final)
    emit("INVERSE_DESIGN_FINAL_IDENTITY", {"JSON_bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()})


if __name__ == "__main__":
    main()

