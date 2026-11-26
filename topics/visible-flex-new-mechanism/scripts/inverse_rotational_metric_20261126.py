#!/usr/bin/env python3
"""Full-domain inverse rotational metric design; reconstructed source revision 2.

The unpublished first implementation was lost with its temporary environment,
before any scientific execution. This revision implements the same declared
physical family using vectorized forward parameter differentiation of analytic
spatial jets. Scientific runs belong to the public Actions workflow. A design
changes its target metric; this program never claims frozen-metric convergence.
"""
import argparse
from dataclasses import asdict, dataclass
import hashlib
import json
import math
import time

import numpy as np
from scipy.interpolate import BSpline
from scipy.optimize import brentq, least_squares
from scipy.special import ellipe, ellipeinc, expit

SCHEMA = "inverse-rotational-metric-v2-reconstructed-after-environment-loss"


def emit(tag, value):
    print(tag + " " + json.dumps(value, sort_keys=True, separators=(",", ":"),
                                allow_nan=False), flush=True)


class Dual:
    """First parameter differential; final array axis is the coordinate axis."""
    __array_priority__ = 1000

    def __init__(self, value, derivative):
        self.v = np.asarray(value, dtype=float)
        self.d = np.asarray(derivative, dtype=float)

    @property
    def size(self):
        return self.d.shape[-1]

    def coerce(self, other):
        if isinstance(other, Dual):
            return other
        value = np.asarray(other, dtype=float)
        return Dual(value, np.zeros(value.shape + (self.size,)))

    def __add__(self, other):
        other = self.coerce(other)
        return Dual(self.v + other.v, self.d + other.d)

    __radd__ = __add__

    def __neg__(self):
        return Dual(-self.v, -self.d)

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) + (-self)

    def __mul__(self, other):
        other = self.coerce(other)
        return Dual(self.v * other.v,
                    self.d * other.v[..., None] + self.v[..., None] * other.d)

    __rmul__ = __mul__

    def __pow__(self, exponent):
        value = self.v ** exponent
        return Dual(value, (exponent * self.v ** (exponent - 1))[..., None] * self.d)

    def __truediv__(self, other):
        return self * (self.coerce(other) ** -1)

    def __rtruediv__(self, other):
        return self.coerce(other) * (self ** -1)

    def sin(self):
        return Dual(np.sin(self.v), np.cos(self.v)[..., None] * self.d)

    def cos(self):
        return Dual(np.cos(self.v), -np.sin(self.v)[..., None] * self.d)

    def exp(self):
        value = np.exp(self.v)
        return Dual(value, value[..., None] * self.d)

    def absolute(self):
        return Dual(np.abs(self.v), np.sign(self.v)[..., None] * self.d)

    def floor(self, minimum):
        return Dual(np.maximum(self.v, minimum), (self.v > minimum)[..., None] * self.d)

    def mean_theta(self):
        return Dual(np.mean(self.v, axis=1, keepdims=True),
                    np.mean(self.d, axis=1, keepdims=True))


def dot(left, right):
    return sum(a * b for a, b in zip(left, right))


def cross(left, right):
    a, b, c = left
    x, y, z = right
    return (b * z - c * y, c * x - a * z, a * y - b * x)


def primitive(field):
    """FFT quadrature for the exact zero-mean periodic primitive definition."""
    n = field.v.shape[1]
    frequencies = np.fft.fftfreq(n, d=1.0 / n)
    multiplier = np.zeros(n, dtype=complex)
    multiplier[1:] = 1.0 / (1j * frequencies[1:])
    value = np.fft.ifft(np.fft.fft(field.v, axis=1) * multiplier[None, :], axis=1).real
    if field.size:
        derivative = np.fft.ifft(np.fft.fft(field.d, axis=1)
                                 * multiplier[None, :, None], axis=1).real
    else:
        derivative = np.zeros(value.shape + (0,))
    return Dual(value, derivative)


@dataclass(frozen=True)
class Parameters:
    p: float = .85
    q: float = .15
    offset: float = .15
    length: float = .9
    radial_count: int = 8
    modes: int = 4
    core_half_width: float = .02
    core_collar_end: float = .036
    cap_collar_width: float = .054
    cap_disk_radius: float = .22
    reach_target: float = .061
    ball_radius: float = 1.01
    strip_half_width: float = .38999


def rounded_core(par, theta):
    if not (par.p >= par.q > 0 and par.offset > 0):
        raise ValueError("core requires p >= q > 0 and positive rounding radius")
    m = 1 - (par.q / par.p) ** 2
    a0 = 2 * par.p * ellipe(m) / np.pi + par.offset

    def phase(u):
        value = math.atan2(par.p * math.sin(u), par.q * math.cos(u))
        return value + 2 * np.pi if u > np.pi else value

    initial_elliptic = ellipeinc(np.pi / 2, m)

    def arclength(u):
        return par.p * (ellipeinc(u + np.pi / 2, m) - initial_elliptic) + par.offset * phase(u)

    anomaly = np.array([0.0 if angle == 0 else brentq(
        lambda u: arclength(u) - a0 * angle, 0, 2 * np.pi, xtol=5e-15)
        for angle in theta])
    phi = np.array([phase(u) for u in anomaly])
    rho = par.offset + (par.p ** 2 * np.sin(anomaly) ** 2
                        + par.q ** 2 * np.cos(anomaly) ** 2) ** 1.5 / (par.p * par.q)
    gamma = np.column_stack((par.p * np.cos(anomaly) + par.offset * np.cos(phi),
                             par.q * np.sin(anomaly) + par.offset * np.sin(phi)))
    return {"a0": float(a0), "u": phi - theta, "utheta": a0 / rho - 1,
            "gamma": gamma, "reach": par.offset + par.q ** 2 / par.p}


def radial_data(par, s):
    left, right = par.core_collar_end, par.length - par.cap_collar_width
    width = right - left
    if width <= 0 or par.radial_count < 6:
        raise ValueError("positive transition width and at least six radial controls required")
    x = (s - left) / width
    active = (x > 0) & (x < 1)
    w = np.where(x >= 1, 1.0, 0.0)
    wm = 1 - w
    wd, wdd = np.zeros_like(s), np.zeros_like(s)
    y = x[active]
    ell = -1 / y + 1 / (1 - y)
    w[active], wm[active] = expit(ell), expit(-ell)
    ell1 = (y ** -2 + (1 - y) ** -2) / width
    ell2 = (-2 * y ** -3 + 2 * (1 - y) ** -3) / width ** 2
    product = w[active] * wm[active]
    wd[active] = product * ell1
    wdd[active] = product * (ell2 + (wm[active] - w[active]) * ell1 ** 2)
    envelope = 4 * w * wm
    envelope1 = 4 * wd * (wm - w)
    envelope2 = 4 * wdd * (wm - w) - 8 * wd ** 2
    degree, n = 5, par.radial_count
    knots = np.r_[np.zeros(degree + 1), np.linspace(0, 1, n - degree + 1)[1:-1],
                  np.ones(degree + 1)]
    spline = BSpline(knots, np.eye(n), degree, extrapolate=False)
    clipped = np.clip(x, 0, 1)
    b, b1, b2 = spline(clipped), spline(clipped, 1) / width, spline(clipped, 2) / width ** 2
    bases = (envelope[:, None] * b,
             envelope1[:, None] * b + envelope[:, None] * b1,
             envelope2[:, None] * b + 2 * envelope1[:, None] * b1 + envelope[:, None] * b2)
    return w[:, None], wm[:, None], wd[:, None], wdd[:, None], bases


class DesignClockLimit(RuntimeError):
    pass


class Model:
    def __init__(self, par, radial_nodes, theta_nodes):
        if radial_nodes < 5 or theta_nodes < 4 * par.modes + 4 or theta_nodes % 2:
            raise ValueError("positive resolved radial grid and an even angular grid required")
        self.par = par
        self.s = np.linspace(0, par.length, radial_nodes)
        self.theta = np.arange(theta_nodes) * (2 * np.pi / theta_nodes)
        self.nr, self.nt = radial_nodes, theta_nodes
        self.core = rounded_core(par, self.theta)
        self.w, self.wm, self.wd, self.wdd, self.bases = radial_data(par, self.s)
        angular = 2 * np.arange(1, par.modes + 1)[:, None]
        sine, cosine = np.sin(angular * self.theta), angular * np.cos(angular * self.theta)
        self.angular_bases = [np.einsum("rj,mt->rtjm", b, sine).reshape(radial_nodes, theta_nodes, -1)
                              for b in self.bases]
        self.theta_basis = np.einsum("rj,mt->rtjm", self.bases[0], cosine).reshape(radial_nodes, theta_nodes, -1)
        self.block = par.radial_count * par.modes
        self.size = 2 * self.block + 2 * par.radial_count + 1
        self.metric_weights = np.ones((radial_nodes, theta_nodes))
        self.cache_key = None
        self.cache = None
        self.deadline = None
        self.last_completed_q = None

    def initial(self, cap_height):
        q = np.zeros(self.size)
        q[-1] = cap_height
        return q

    def bounds(self):
        lower, upper = -12 * np.ones(self.size), 12 * np.ones(self.size)
        start = 2 * self.block
        lower[start:start + self.par.radial_count] = -1.5
        upper[start:start + self.par.radial_count] = 1.5
        lower[start + self.par.radial_count:-1] = -1
        upper[start + self.par.radial_count:-1] = 1
        lower[-1], upper[-1] = .08, .8
        return lower, upper

    def geometry(self, q, differentiate=True, ignore_clock=False):
        q = np.asarray(q, dtype=float)
        key = q.tobytes()
        if self.cache_key == key and (not differentiate or self.cache["E"].size):
            return self.cache
        if not ignore_clock and self.deadline is not None and time.monotonic() >= self.deadline:
            raise DesignClockLimit("declared 2400-second Actions segment reached; current design is not complete")
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
        u = linear(self.angular_bases[0], 0, self.wm * uc)
        us = linear(self.angular_bases[1], 0, -self.wd * uc)
        uss = linear(self.angular_bases[2], 0, -self.wdd * uc)
        ut = linear(self.theta_basis, 0, self.wm * self.core["utheta"][None, :])
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
        abase = self.wm * self.core["a0"] + self.w * tail
        abase1 = self.wd * (tail - self.core["a0"]) - self.w
        abase2 = self.wdd * (tail - self.core["a0"]) - 2 * self.wd
        radius = exp_alpha * abase
        radius1 = exp_alpha * (abase1 + abase * alphas)
        radius2 = exp_alpha * (abase2 + 2 * abase1 * alphas + abase * (alphass + alphas * alphas))
        zstart = astart + self.par.radial_count
        central = self.par.core_half_width + self.s[:, None]
        z = self.wm * central + self.w * h + radial(0, zstart)
        z1 = self.wm + self.wd * (h - central) + radial(1, zstart)
        z2 = -2 * self.wd + self.wdd * (h - central) + radial(2, zstart)
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

    def residual(self, q, jacobian=False, curvature_weight=.05, shape_weight=.1, regularization=1e-5):
        g = self.geometry(q, differentiate=True)
        count = self.nr * self.nt
        weights = np.sqrt(self.metric_weights / count)
        components = [g["e"] * weights, g["f"] * (np.sqrt(2) * weights)]
        components.extend((k.absolute() * self.par.reach_target - 1).floor(0)
                          * (curvature_weight / np.sqrt(count)) for k in g["curvature"])
        x, y, z = g["position"]
        nz = g["normal"][2]
        penalties = [dot(g["position"], g["position"]) / self.par.ball_radius ** 2 - 1,
                     y * y / self.par.strip_half_width ** 2 - 1,
                     (self.par.core_half_width - z) / self.par.reach_target,
                     nz * nz - z * z / self.par.reach_target ** 2]
        components.extend(penalty.floor(0) * (shape_weight / np.sqrt(count)) for penalty in penalties)
        components.append((1 - g["Ebar"] / .04).floor(0) * (shape_weight / np.sqrt(self.nr)))
        if jacobian:
            answer = np.vstack([component.d.reshape(-1, self.size) for component in components]
                               + [regularization * np.eye(self.size)])
        else:
            answer = np.concatenate([component.v.ravel() for component in components]
                                    + [regularization * np.asarray(q)])
        if not np.all(np.isfinite(answer)):
            raise FloatingPointError("nonfinite complete residual or its parameter derivative")
        return answer

    def eta(self, q):
        g = self.geometry(q, differentiate=False, ignore_clock=True)
        e, f = g["e"].v, g["f"].v
        return .5 * (np.abs(e) + np.sqrt(e * e + 4 * f * f))

    def summary(self, q):
        g = self.geometry(q, differentiate=False, ignore_clock=True)
        eta = self.eta(q)
        peak = np.unravel_index(np.argmax(eta), eta.shape)
        xyz = np.stack([component.v for component in g["position"]], axis=-1)
        tangent = np.stack([component.v for component in g["T"]], axis=-1)
        spectrum = np.fft.fft(tangent, axis=1) / self.nt
        frequencies = np.fft.fftfreq(self.nt, 1 / self.nt)
        high = np.abs(frequencies) >= self.nt / 3
        e, f = g["e"].v, g["f"].v
        kmax = max(float(np.max(np.abs(k.v))) for k in g["curvature"])
        return {"radial_nodes": self.nr, "theta_nodes": self.nt, "eta_max": float(np.max(eta)),
                "eta_peak": {"s": float(self.s[peak[0]]), "theta": float(self.theta[peak[1]])},
                "metric_e_max": float(np.max(np.abs(e))), "metric_f_max": float(np.max(np.abs(f))),
                "metric_rms": float(np.sqrt(np.mean(e * e + 2 * f * f))),
                "principal_curvature_abs_max": kmax, "core_reach_exact_formula": self.core["reach"],
                "ball_radius_max": float(np.max(np.linalg.norm(xyz, axis=-1))),
                "abs_y_max": float(np.max(np.abs(xyz[..., 1]))), "z_min": float(np.min(xyz[..., 2])),
                "Ebar_min": float(np.min(g["Ebar"].v)), "Ebar_max": float(np.max(g["Ebar"].v)),
                "actual_E_minus_F2_min": float(np.min(g["det"].v)),
                "actual_area_min": float(np.min(g["area"].v)),
                "radius_min": float(np.min(g["radius"].v)),
                "mirror_necessary_violation_max": float(np.max(g["normal"][2].v ** 2
                                                   - xyz[..., 2] ** 2 / self.par.reach_target ** 2)),
                "T_numerical_circle_mean_max": float(np.max(np.linalg.norm(np.mean(tangent, axis=1), axis=-1))),
                "T_high_frequency_coefficient_l1_max": float(np.max(np.sum(np.linalg.norm(spectrum[:, high, :], axis=-1), axis=1))),
                "core_FFT_position_error_max": float(np.max(np.linalg.norm(xyz[0, :, :2] - self.core["gamma"], axis=-1))),
                "metric_floor_used": bool(np.min(g["Ebar"].v) <= 1e-14),
                "curvature_det_floor_used": bool(np.min(g["det"].v) <= 1e-24),
                "finite_grid_observation_only": True, "all_pair_reach_certified": False,
                "fixed_metric_refinement_demonstrated": False, "README_completion_claim": False}


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
    parser.add_argument("--seed-json", help="JSON array in this model's coordinate order only")
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
        raise ValueError("seed must be a finite in-bounds vector in the declared new identity")
    definition = {"schema": SCHEMA, "parameters": asdict(par), "solver": vars(args),
                  "coordinate_order": ["u radial-major sin2..sin2m", "v radial-major sin2..sin2m",
                                       "log-radius", "height-displacement", "cap-height"],
                  "radial_step": "exp(-1/x)/(exp(-1/x)+exp(-1/(1-x))) with constant exterior",
                  "radial_envelope": "4*W*(1-W)", "basis_degree": 5,
                  "position": "a*zero-mean periodic primitive(T)+z*ez",
                  "T": "(-sin(theta+u),cos(theta+u),v)/sqrt(1+v*v)",
                  "target_during_design": "g=mean_theta(E)*ds^2+a^2*dtheta^2; allowed to vary",
                  "parameter_Jacobian": "vectorized forward differential through analytic spatial jets",
                  "all_product_grid_points_in_metric_residual": True,
                  "reconstructed_after_environment_loss_before_any_scientific_run": True,
                  "old_scopes_replayed": False, "README_completion_claim": False}
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
            emit("INVERSE_DESIGN_DIRECTIONAL_DERIVATIVE", {"relative_l2_difference": relative,
                  "step": step, "same_actual_residual": True, "scientific_cost_is_in_this_run": True})
            if not relative < 3e-4:
                raise ArithmeticError("full-domain parameter derivative failed the scientific directional check")
        for outer in range(args.outer):
            result = least_squares(lambda x: model.residual(x, **kwargs), q,
                                   jac=lambda x: model.residual(x, jacobian=True, **kwargs),
                                   bounds=(lower, upper), x_scale="jac", tr_solver="lsmr",
                                   max_nfev=args.nfev, ftol=1e-10, xtol=1e-10, gtol=1e-9,
                                   tr_options={"maxiter": 180, "atol": 1e-8, "btol": 1e-8})
            q = result.x.copy()
            completed_outer += 1
            emit("INVERSE_DESIGN_OUTER", {"outer": outer, "status": int(result.status),
                  "success": bool(result.success), "message": str(result.message),
                  "nfev": int(result.nfev), "njev": int(result.njev), "cost": float(result.cost),
                  "optimality": float(result.optimality), "elapsed_seconds": time.monotonic() - started,
                  "geometry": model.summary(q), "coordinates": q.tolist(),
                  "optimizer_success_is_not_geometric_acceptance": True})
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
        emit("INVERSE_DESIGN_TIME_CHECKPOINT", {"message": str(error), "coordinates": q.tolist(),
              "completed_outer": completed_outer, "elapsed_seconds": time.monotonic() - started,
              "this_is_not_an_OptimizeResult": True, "README_completion_claim": False})
    except Exception as error:
        emit("INVERSE_DESIGN_ERROR_CHECKPOINT", {"type": type(error).__name__, "message": str(error),
              "coordinates": (model.last_completed_q if model.last_completed_q is not None else q).tolist(),
              "completed_outer": completed_outer, "elapsed_seconds": time.monotonic() - started,
              "README_completion_claim": False})
        raise
    final = {"definition": definition, "coordinates": q.tolist(), "coarse": model.summary(q),
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
