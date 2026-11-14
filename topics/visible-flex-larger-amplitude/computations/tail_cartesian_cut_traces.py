#!/usr/bin/env python3
"""Convert complete saved source-cut jets to Cartesian polar trace diagnostics.

Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.

Only the small, completed tail response is read. No tail factory, BVP,
Jacobian, phase change, mean deletion, or closure projection is performed.
The displayed curve and trace bounds use floating quadrature/samples and are
not a continuous Cartesian certificate. Exact rational positivity guards
refer only to the represented binary-rational Fourier input.
"""
from __future__ import annotations

import os
for _name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_name] = "1"

import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from math import factorial
from pathlib import Path
import resource
import time

import numpy as np


class Jet:
    """Taylor coefficients in theta, including the constant coefficient."""

    def __init__(self, coefficients):
        self.c = np.asarray(coefficients, dtype=float)

    @classmethod
    def derivatives(cls, derivatives):
        return cls([x / factorial(j) for j, x in enumerate(derivatives)])

    def constant(self, value):
        out = np.zeros_like(self.c)
        out[0] = value
        return Jet(out)

    def __add__(self, other):
        other = other if isinstance(other, Jet) else self.constant(other)
        n = min(len(self.c), len(other.c))
        return Jet(self.c[:n] + other.c[:n])

    __radd__ = __add__

    def __neg__(self):
        return Jet(-self.c)

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        if not isinstance(other, Jet):
            return Jet(self.c * other)
        n = min(len(self.c), len(other.c))
        return Jet([sum(self.c[k] * other.c[j-k] for k in range(j+1))
                    for j in range(n)])

    __rmul__ = __mul__

    def reciprocal(self):
        out = [1 / self.c[0]]
        for j in range(1, len(self.c)):
            out.append(-sum(self.c[k] * out[j-k] for k in range(1, j+1))
                       / self.c[0])
        return Jet(out)

    def __truediv__(self, other):
        return self * (other.reciprocal() if isinstance(other, Jet) else 1 / other)

    def __rtruediv__(self, other):
        return self.reciprocal() * other

    def __pow__(self, power):
        if power < 0:
            return self.reciprocal() ** (-power)
        out = self.constant(1)
        for _ in range(power):
            out = out * self
        return out

    def sqrt(self):
        out = [np.sqrt(self.c[0])]
        for j in range(1, len(self.c)):
            out.append((self.c[j] - sum(out[k] * out[j-k]
                                       for k in range(1, j))) / (2 * out[0]))
        return Jet(out)

    def diff(self, count=1):
        out = self
        for _ in range(count):
            out = Jet([j * out.c[j] for j in range(1, len(out.c))])
        return out


def dot(x, y):
    return x[0] * y[0] + x[1] * y[1]


def det(x, y):
    return x[0] * y[1] - x[1] * y[0]


def vadd(x, y):
    return [x[0] + y[0], x[1] + y[1]]


def scale(s, x):
    return [s * x[0], s * x[1]]


def primitive(values, theta):
    """Unprojected Fourier primitive, retaining the mean linear drift."""
    size = len(theta)
    hat = np.fft.fft(values, axis=0) / size
    frequency = np.fft.fftfreq(size, 1/size)
    denominator = 1j * frequency
    denominator[0] = 1
    shape = (size,) + (1,) * (values.ndim - 1)
    coefficients = hat / denominator.reshape(shape)
    coefficients[0] = 0
    periodic = np.fft.ifft(coefficients * size, axis=0).real
    return periodic - periodic[0] + theta.reshape(shape) * hat[0].real


def cosine_jet(coefficients, modes, theta, order, mean=0):
    derivatives = []
    for j in range(order+1):
        value = np.cos(theta[:, None] * modes + j * np.pi/2) @ (
            coefficients * modes**j)
        if j == 0:
            value += mean
        derivatives.append(value)
    return Jet.derivatives(derivatives)


def encoded_fraction(value):
    return {"exact": str(value), "decimal": float(value)}


def rational_guards(jets, spacing):
    """All-angle exact l1 bounds for the represented finite Fourier data."""
    f = Fraction.from_float
    radius, E = f(jets["radius"]), f(jets["E"])
    H = list(map(f, jets["height"]))
    P = list(map(f, jets["slope"]))
    Q = list(map(f, jets["second"]))
    modes = [spacing * (j+1) for j in range(len(H))]
    sums = lambda values, order: sum((abs(x) * m**order
                                     for x, m in zip(values, modes)), Fraction(0))
    h1, h2 = sums(H, 1), sums(H, 2)
    p0, q0 = f(jets["meanSlope"]), f(jets["meanSecond"])
    p_max = abs(p0) + sums(P, 0)
    a2_min = radius**2 - h1**2
    nz2_min = 1 - p_max**2/E - h1**2/radius**2
    leading_min = p0 - sums(P, 0) - E*h2/radius
    gamma_numerator_min = 1 - p_max*radius*h2/a2_min
    assert min(a2_min, nz2_min, leading_min, gamma_numerator_min) > 0
    return {
        "scope": "Exact for represented binary-rational source jets only; not a real-profile or closure certificate.",
        "height_derivative_l1_bounds": [encoded_fraction(sums(H, j)) for j in range(5)],
        "nonmean_slope_derivative_l1_bounds": [encoded_fraction(sums(P, j)) for j in range(4)],
        "nonmean_second_derivative_l1_bounds": [encoded_fraction(sums(Q, j)) for j in range(3)],
        "complete_slope_abs_upper": encoded_fraction(p_max),
        "complete_second_abs_upper": encoded_fraction(abs(q0) + sums(Q, 0)),
        "a_squared_lower": encoded_fraction(a2_min),
        "normal_vertical_squared_lower": encoded_fraction(nz2_min),
        "mean_turn_derivative_numerator_lower": encoded_fraction(leading_min),
        "tangent_turn_numerator_lower": encoded_fraction(gamma_numerator_min),
    }


def maxabs(value):
    return float(np.max(np.abs(value)))


def angle_derivatives(trace, angle_speed):
    first = trace.c[1] / angle_speed.c[0]
    second = (2*trace.c[2]*angle_speed.c[0]
              - trace.c[1]*angle_speed.c[1]) / angle_speed.c[0]**3
    return trace.c[0], first, second


def extension_bound(rmin, radius_d1, radius_d2, U, V, W, c1, c2, length=.1):
    ratio = -length*c2/c1
    if c1 > 0 and c2 < 0 and 1.5 <= ratio <= 3:
        amean, bmean = abs(c2), c1
    else:
        amean = 1.5*abs(c1)/length + abs(c2)
        bmean = abs(c1) + 4*length*abs(c2)/27
    A = amean + 20*U[0]/length**2 + 12*V[0]/length + 2*W[0]
    B = bmean + 5*U[0]/length + 2*V[0] + length*W[0]/4
    C = U[1] + 2*length*V[1]/5 + length**2*W[1]/20
    D = 5*U[1]/length + 2*V[1] + length*W[1]/4
    F = U[2] + 2*length*V[2]/5 + length**2*W[2]/20
    cross = (D+radius_d1*A)/rmin + (C+radius_d1*B)/rmin**2
    angular = (F+2*radius_d1*D+radius_d1**2*A+radius_d2*B)/rmin**2+B/rmin
    return {"scope": "R27 expression evaluated on sampled bounds; not an all-angle bound.",
            "width": length, "alpha": ratio,
            "A": A, "B": B, "C": C, "D": D, "E": F,
            "cross": cross, "angular": angular, "exterior_curvature_expression": max(A, angular)+cross}


def audit(jets, spacing, size):
    theta = 2*np.pi*np.arange(size)/size
    modes = spacing*np.arange(1, len(jets["height"])+1)
    r, E, Ep = (float(jets[key]) for key in ("radius", "E", "Ep"))
    H = cosine_jet(np.asarray(jets["height"]), modes, theta, 4)
    P = cosine_jet(np.asarray(jets["slope"]), modes, theta, 3, jets["meanSlope"])
    Q = cosine_jet(np.asarray(jets["second"]), modes, theta, 2, jets["meanSecond"])
    Ht, Htt, Pt = H.diff(), H.diff(2), P.diff()
    a = (r*r-Ht*Ht).sqrt()
    determinant = (E*a*a-r*r*P*P).sqrt()
    b, c = -P*Ht/a, -determinant/a
    nz2 = 1-P*P/E-Ht*Ht/(r*r)
    turn = (1+P*r*Htt/(a*a))/(E*nz2).sqrt()
    angle = np.pi/2 + primitive(turn.c[0], theta)
    tangent0 = np.c_[np.cos(angle), np.sin(angle)]
    normal0 = np.c_[-tangent0[:, 1], tangent0[:, 0]]
    tangent = [Jet.derivatives([tangent0[:, j], turn.c[0]*normal0[:, j],
                               turn.c[1]*normal0[:, j]-turn.c[0]**2*tangent0[:, j]])
               for j in range(2)]
    normal = [-tangent[1], tangent[0]]
    ar = (r-Ht*Pt)/a
    br = -(Q*Ht+P*Pt)/a+P*Ht*ar/(a*a)
    Dr = (Ep*a*a+E*(2*r-2*Ht*Pt)-2*r*P*P-2*r*r*P*Q)/(2*determinant)
    cr = -Dr/a+determinant*ar/(a*a)
    turn_r = (b*turn+c.diff())/a
    Xtheta = scale(a, tangent)
    Xr = vadd(scale(b, tangent), scale(c, normal))
    Xtheta2 = vadd(scale(a.diff(), tangent), scale(a*turn, normal))
    Xrtheta = vadd(scale(ar, tangent), scale(a*turn_r, normal))
    Xrr = vadd(scale(br-c*turn_r, tangent), scale(b*turn_r+cr, normal))
    U = np.stack([q.c[0] for q in Xtheta], axis=1)
    position = primitive(U, theta)
    center = .5*(position[0]+position[size//2])
    Y = [Jet.derivatives([position[:, j]-center[j], Xtheta[j].c[0],
                          Xtheta2[j].c[0]]) for j in range(2)]
    radius = dot(Y, Y).sqrt()
    er = scale(1/radius, Y)
    et, en = dot(er, tangent), dot(er, normal)
    xi = en/c
    eta = (et-b*xi)/a
    qt = Ht/a
    qn = (P-b*qt)/c
    gradient = vadd(scale(qt, tangent), scale(qn, normal))
    Krr = Q-dot(gradient, Xrr)
    Krt = Pt-dot(gradient, Xrtheta)
    Ktt = Htt-dot(gradient, Xtheta2)
    a1 = P*xi+Ht*eta
    a2 = Krr*xi*xi+2*Krt*xi*eta+Ktt*eta*eta
    polar_speed = det(Y, Xtheta)/(radius*radius)
    traces = [angle_derivatives(x, polar_speed) for x in (H, a1, a2)]
    radii = angle_derivatives(radius, polar_speed)
    references = [0., float(jets["backgroundSlope"]), float(jets["backgroundSecond"])]
    trace_bounds = [[maxabs(values[j]-(references[i] if j == 0 else 0))
                     for j in range(3)] for i, values in enumerate(traces)]
    shape = np.stack([q.c[0] for q in Xr], axis=1)
    J = np.stack([shape, U], axis=2)
    K = np.empty((size, 2, 2))
    K[:, 0, 0], K[:, 0, 1], K[:, 1, 0], K[:, 1, 1] = (
        Krr.c[0], Krt.c[0], Krt.c[0], Ktt.c[0])
    Jinv = np.linalg.inv(J)
    Hess = np.transpose(Jinv, (0, 2, 1))@K@Jinv
    gxy = np.stack([q.c[0] for q in gradient], axis=1)
    metric = np.eye(2)[None, :, :]+gxy[:, :, None]*gxy[:, None, :]
    shape_operator = np.linalg.solve(metric, Hess)/np.sqrt(1+np.sum(gxy*gxy, axis=1))[:, None, None]
    principal = np.linalg.eigvals(shape_operator)
    direct_radial = np.einsum('ni,nij,nj->n', np.stack([q.c[0] for q in er], axis=1),
                             Hess, np.stack([q.c[0] for q in er], axis=1))
    projected_metric = np.transpose(J, (0, 2, 1))@J
    expected = np.empty_like(projected_metric)
    expected[:, 0, 0] = E-P.c[0]**2
    expected[:, 0, 1] = expected[:, 1, 0] = -P.c[0]*Ht.c[0]
    expected[:, 1, 1] = r*r-Ht.c[0]**2
    tangent_compatibility = b.diff()-c*turn-ar
    half_symmetry = np.roll(position, -size//2, axis=0)+position-2*center
    closure_vector = 2*np.pi*np.mean(U, axis=0)
    result = {
        "angular": size,
        "scope": "Uncorrected saved cut, numerical Fourier primitive and samples. No exact closure or extension certificate.",
        "complete_mean_slope": jets["meanSlope"], "complete_mean_second": jets["meanSecond"],
        "gamma_theta_range": [float(np.min(turn.c[0])), float(np.max(turn.c[0]))],
        "gamma_theta_minus_one_abs_max": maxabs(turn.c[0]-1),
        "gamma_theta_derivative_abs_max": [maxabs(turn.c[1]), maxabs(2*turn.c[2])],
        "angle_holonomy_error": float(2*np.pi*(np.mean(turn.c[0])-1)),
        "planar_curve_closure_vector": closure_vector.tolist(),
        "planar_curve_closure_error": float(np.linalg.norm(closure_vector)),
        "central_symmetry_error": float(np.max(np.linalg.norm(half_symmetry, axis=1))),
        "normal_vertical_squared_min": float(np.min(nz2.c[0])),
        "projected_metric_determinant_min": float(np.min(determinant.c[0]**2)),
        "polar_angle_speed_range": [float(np.min(polar_speed.c[0])), float(np.max(polar_speed.c[0]))],
        "polar_angle_speed_theta_derivative_max": maxabs(polar_speed.c[1]),
        "cartesian_radius_range": [float(np.min(radii[0])), float(np.max(radii[0]))],
        "cartesian_radius_angle_derivative_max": [maxabs(radii[1]), maxabs(radii[2])],
        "cartesian_trace_references": references,
        "cartesian_trace_deviation_angle_derivative_bounds": trace_bounds,
        "cartesian_trace_ranges": [[float(np.min(v[0])), float(np.max(v[0]))] for v in traces],
        "horizontal_gradient_abs_max": float(np.max(np.linalg.norm(gxy, axis=1))),
        "graph_hessian_norm_max": float(np.max(abs(np.linalg.eigvalsh(Hess)))),
        "principal_curvature_abs_max": float(np.max(abs(principal))),
        "algebraic_checks": {
            "projected_metric_error": maxabs(projected_metric-expected),
            "tangent_compatibility_error": maxabs(tangent_compatibility.c[0]),
            "radial_hessian_two_formulas_error": maxabs(direct_radial-a2.c[0]),
        },
    }
    result["sampled_R27_expression"] = extension_bound(
        result["cartesian_radius_range"][0], *result["cartesian_radius_angle_derivative_max"],
        *trace_bounds, references[1], references[2])
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--response", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--angular", type=int, nargs="+", default=[512, 1024])
    args = parser.parse_args()
    started = time.time()
    rawbytes = args.response.read_bytes()
    raw = json.loads(gzip.decompress(rawbytes) if args.response.suffix == ".gz" else rawbytes)
    response, cfg = raw["response"], raw["config"]
    if not response["converged"]:
        raise ValueError("A formally completed response is required")
    jets = response["jets"]
    if raw["request"]["height"] != jets["height"]:
        raise ValueError("Complete request height and returned height differ")
    spacing = int(cfg["spacing"])
    if spacing % 2:
        raise ValueError("The recorded half-turn symmetry requires even physical frequencies")
    if any(N % 2 or N <= 8*spacing*len(jets["height"]) for N in args.angular):
        raise ValueError("Use even angular sizes larger than eight times the highest input mode")
    output = {
        "author": "tail_refinement (GPT-6 Astra Pro, AI-assisted)",
        "scope": __doc__,
        "actual_cartesian_certificate": False,
        "exact_mean_turn_root_applied": False,
        "response": str(args.response), "response_sha256": hashlib.sha256(rawbytes).hexdigest(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "response_residual": response["residual"], "modes": len(jets["height"]), "spacing": spacing,
        "represented_input_all_angle_guards": rational_guards(jets, spacing),
        "rows": [audit(jets, spacing, N) for N in args.angular],
    }
    output["wall_seconds"] = time.time()-started
    output["peak_rss_kib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    args.out.write_text(json.dumps(output, indent=2)+"\n")
    print(json.dumps({key: output[key] for key in ("response_sha256", "rows", "wall_seconds", "peak_rss_kib")}))


if __name__ == "__main__":
    main()
