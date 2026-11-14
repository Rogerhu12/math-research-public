#!/usr/bin/env python3
"""Continuous Cartesian R27 trace bounds for an R19-corrected saved cut.

Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.

All arithmetic used for inequalities is rational with outward dyadic
rounding. No angular samples or source radial integration are used. The
object certified is a closed cut two-jet constructed from binary-rational
saved E/Ep/r and the exact complete mean root, not an existing exact radial
tail or the real-source metric. The root and full-second correction are
kept explicit and are never silently applied to the saved response.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from math import factorial, isqrt
from pathlib import Path
import resource
import time

import closure_scaled_endpoint_cut_enclosure as cut
import tail_entire_extension_bounds as exterior


BITS = 160
SCALE = 1 << BITS


def down(x):
    x = F(x)
    return F((x.numerator*SCALE)//x.denominator, SCALE)


def up(x):
    return -down(-F(x))


class I:
    """Closed rational interval, outward-rounded after each operation."""

    def __init__(self, lo, hi=None):
        if isinstance(lo, I):
            lo, hi = lo.lo, lo.hi
        if hi is None:
            hi = lo
        self.lo, self.hi = down(lo), up(hi)
        if self.lo > self.hi:
            raise ValueError("Inverted interval")

    def __add__(self, other):
        if isinstance(other, J):
            return NotImplemented
        other = I(other)
        return I(self.lo+other.lo, self.hi+other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        if isinstance(other, J):
            return NotImplemented
        return self + (-I(other))

    def __rsub__(self, other):
        return I(other) + (-self)

    def __mul__(self, other):
        if isinstance(other, J):
            return NotImplemented
        other = I(other)
        products = [self.lo*other.lo, self.lo*other.hi,
                    self.hi*other.lo, self.hi*other.hi]
        return I(min(products), max(products))

    __rmul__ = __mul__

    def reciprocal(self):
        if self.lo <= 0 <= self.hi:
            raise ZeroDivisionError("Interval contains zero")
        return I(1/self.hi, 1/self.lo)

    def __truediv__(self, other):
        if isinstance(other, J):
            return NotImplemented
        return self * I(other).reciprocal()

    def __rtruediv__(self, other):
        return I(other) * self.reciprocal()

    def __pow__(self, power):
        if power < 0:
            return self.reciprocal()**(-power)
        out = I(1)
        for _ in range(power):
            out = out*self
        return out

    def sqrt(self):
        if self.lo < 0:
            raise ValueError("Negative square-root interval")
        low = isqrt((self.lo.numerator*SCALE*SCALE)//self.lo.denominator)
        high = isqrt((self.hi.numerator*SCALE*SCALE)//self.hi.denominator)+1
        return I(F(low, SCALE), F(high, SCALE))

    def absmax(self):
        return max(abs(self.lo), abs(self.hi))


class J:
    """Theta Taylor coefficients; interval coefficient j bounds derivative/j!."""

    def __init__(self, coefficients):
        self.c = [I(q) for q in coefficients]

    def constant(self, value):
        return J([value]+[0]*(len(self.c)-1))

    def __add__(self, other):
        other = other if isinstance(other, J) else self.constant(other)
        return J([a+b for a, b in zip(self.c, other.c)])

    __radd__ = __add__

    def __neg__(self):
        return J([-a for a in self.c])

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        if not isinstance(other, J):
            return J([a*other for a in self.c])
        n = min(len(self.c), len(other.c))
        return J([sum((self.c[k]*other.c[j-k] for k in range(j+1)), I(0))
                  for j in range(n)])

    __rmul__ = __mul__

    def reciprocal(self):
        out = [self.c[0].reciprocal()]
        for j in range(1, len(self.c)):
            out.append(-sum((self.c[k]*out[j-k] for k in range(1, j+1)), I(0))/self.c[0])
        return J(out)

    def __truediv__(self, other):
        return self * (other.reciprocal() if isinstance(other, J) else I(other).reciprocal())

    def __rtruediv__(self, other):
        return self.reciprocal()*other

    def __pow__(self, power):
        if power < 0:
            return self.reciprocal()**(-power)
        out = self.constant(1)
        for _ in range(power):
            out = out*self
        return out

    def sqrt(self):
        out = [self.c[0].sqrt()]
        for j in range(1, len(self.c)):
            out.append((self.c[j]-sum((out[k]*out[j-k] for k in range(1, j)), I(0)))/(2*out[0]))
        return J(out)

    def diff(self, count=1):
        out = self
        for _ in range(count):
            out = J([j*out.c[j] for j in range(1, len(out.c))])
        return out


def encode(value):
    if isinstance(value, I):
        return {"lower": str(value.lo), "upper": str(value.hi),
                "decimal_interval": [float(value.lo), float(value.hi)]}
    value = F(value)
    return {"exact": str(value), "decimal": float(value)}


def l1(values, spacing, order):
    return sum((abs(F.from_float(x))*(spacing*(j+1))**order
                for j, x in enumerate(values)), F(0))


def poly_derivative_norm(poly, order):
    return sum((abs(q)*abs(m)**order for m, q in poly.items()), F(0))


def correction_bounds(jets, spacing, eta):
    """Differentiate R19's exact quotient correction twice on the real circle."""
    f = F.from_float
    r, E, Ep, p0, q0 = [f(jets[key]) for key in ("radius", "E", "Ep", "meanSlope", "meanSecond")]
    height = cut.cosine(F(0), jets["height"], spacing)
    p = cut.cosine(p0, jets["slope"], spacing)
    q = cut.cosine(q0, jets["second"], spacing)
    imag = {m:m*x/r for m, x in height.items()}
    pt = {m:-m*x for m, x in imag.items()}
    imR = cut.plus({m:m*x for m, x in p.items()}, cut.scale(imag, -1))
    B = cut.plus(p, cut.scale(pt, E))
    Fpoly = cut.plus(cut.product(B, q), cut.scale(cut.product(imR, imR), E/r),
                     cut.scale(cut.plus({0:F(1)}, cut.product(imag, imag), cut.product(p, pt)), -Ep/2))
    Jpoly = cut.plus(q, cut.scale(pt, -Ep/2))
    bmin = cut.real_interval(B)[0]-eta
    if bmin <= 0:
        raise ValueError("Corrected Darboux denominator is not positive")
    An = [poly_derivative_norm(Fpoly, j)+eta*poly_derivative_norm(Jpoly, j) for j in range(3)]
    B1, B2 = [poly_derivative_norm(B, j) for j in (1, 2)]
    errors = [An[0]/bmin,
              An[1]/bmin+An[0]*B1/bmin**2,
              An[2]/bmin+2*An[1]*B1/bmin**2+An[0]*B2/bmin**2+2*An[0]*B1**2/bmin**3]
    return errors, {
        "scope": "Exact real-circle C2 bound for the complete Q correction; no log(2) strip assumption.",
        "formula": "Q_exact-Q = -(F+s*(Q-Ep*H_thetatheta/(2*r)))/(P+E*H_thetatheta/r+s)",
        "mean_shift_abs_upper": encode(eta),
        "denominator_lower": encode(bmin),
        "numerator_derivative_bounds": [encode(x) for x in An],
        "denominator_nonconstant_derivative_bounds": [encode(B1), encode(B2)],
        "complete_second_correction_theta_derivative_bounds": [encode(x) for x in errors],
        "full_Darboux_polynomial_derivative_l1": [encode(poly_derivative_norm(Fpoly, j)) for j in range(3)],
    }


def source_jet(values, spacing, order, mean=F(0), corrections=None):
    out = []
    corrections = corrections or [F(0)]*(order+1)
    for j in range(order+1):
        radius = l1(values, spacing, j)+corrections[j]
        center = mean if j == 0 else F(0)
        out.append(I(center-radius, center+radius)/factorial(j))
    return J(out)


def angular_trace(trace, k):
    first = trace.c[1]/k.c[0]
    second = (2*trace.c[2]*k.c[0]-trace.c[1]*k.c[1])/k.c[0]**3
    return [trace.c[0], first, second]


def enclose_cartesian(jets, spacing, eta, q_errors):
    f = F.from_float
    r, E, Ep, w, wr, p0, q0 = [f(jets[key]) for key in
                               ("radius", "E", "Ep", "backgroundSlope", "backgroundSecond", "meanSlope", "meanSecond")]
    H = source_jet(jets["height"], spacing, 4)
    P = source_jet(jets["slope"], spacing, 3, p0, [eta, 0, 0, 0])
    Q = source_jet(jets["second"], spacing, 2, q0, q_errors)
    Ht, Htt, Pt = H.diff(), H.diff(2), P.diff()
    a = (r*r-Ht*Ht).sqrt()
    D = (a*a*E-P*P*r*r).sqrt()
    b, c = -P*Ht/a, -D/a
    nz2 = 1-P*P/E-Ht*Ht/(r*r)
    gamma = (1+P*r*Htt/(a*a))/(nz2*E).sqrt()
    if gamma.c[0].lo <= 0:
        raise ValueError("Strict convexity gate failed")
    eps_gamma = (gamma.c[0]-1).absmax()
    eps_a = l1(jets["height"], spacing, 1)**2/r
    eps_delta = F(11, 7)*eps_gamma
    eps_Y = F(11, 7)*(eps_a+r*eps_delta)
    eps_t = eps_Y+r*eps_delta
    eps_n = eps_Y+r*eps_delta**2/2
    yt, yn = I(-eps_t, eps_t), I(-r-eps_n, -r+eps_n)
    yt1 = a.c[0]+gamma.c[0]*yn
    yn1 = -gamma.c[0]*yt
    Yt = J([yt, yt1, (a.c[1]+gamma.c[1]*yn-gamma.c[0]**2*yt)/2])
    Yn = J([yn, yn1, (-gamma.c[1]*yt-gamma.c[0]*yt1)/2])
    rho = (Yt*Yt+Yn*Yn).sqrt()
    et, en = Yt/rho, Yn/rho
    ar = (r-Ht*Pt)/a
    br = -(Q*Ht+P*Pt)/a+P*Ht*ar/(a*a)
    Dr = (a*a*Ep+(2*r-2*Ht*Pt)*E-P*P*(2*r)-P*Q*(2*r*r))/(2*D)
    cr = -Dr/a+D*ar/(a*a)
    gamma_r = (b*gamma+c.diff())/a
    Xrr_t, Xrr_n = br-c*gamma_r, b*gamma_r+cr
    Xrt_t, Xrt_n = ar, a*gamma_r
    Xtt_t, Xtt_n = a.diff(), a*gamma
    qt = Ht/a
    qn = (P-b*qt)/c
    Krr = Q-qt*Xrr_t-qn*Xrr_n
    Krt = Pt-qt*Xrt_t-qn*Xrt_n
    Ktt = Htt-qt*Xtt_t-qn*Xtt_n
    xi, eta_angle = en/c, (et-b*(en/c))/a
    a1 = P*xi+Ht*eta_angle
    a2 = Krr*xi*xi+2*Krt*xi*eta_angle+Ktt*eta_angle*eta_angle
    k = -a*Yn/(rho*rho)
    if k.c[0].lo <= 0:
        raise ValueError("Actual polar angle is not bounded away from zero")
    radius_derivatives = angular_trace(rho, k)
    traces = [angular_trace(z, k) for z in [H, a1, a2]]
    references = [F(0), w, wr]
    trace_bounds = [[(row[j]-(references[i] if j == 0 else 0)).absmax()
                     for j in range(3)] for i, row in enumerate(traces)]
    radius_bounds = [radius_derivatives[j].absmax() for j in (1, 2)]
    return {
        "rounding_bits": BITS,
        "gamma_interval": encode(gamma.c[0]),
        "gamma_theta_derivative_intervals": [encode(gamma.c[1]), encode(2*gamma.c[2])],
        "normal_vertical_squared_interval": encode(nz2.c[0]),
        "near_circle_bounds": {key: encode(value) for key, value in {
            "epsilon_a": eps_a, "epsilon_Gamma": eps_gamma, "epsilon_delta": eps_delta,
            "epsilon_Y": eps_Y, "epsilon_t": eps_t, "epsilon_n": eps_n}.items()},
        "moving_frame_position_intervals": [encode(yt), encode(yn)],
        "actual_polar_speed_interval": encode(k.c[0]),
        "actual_polar_speed_theta_derivative_interval": encode(k.c[1]),
        "actual_radius_interval": encode(rho.c[0]),
        "actual_radius_angle_derivative_bounds": [encode(x) for x in radius_bounds],
        "actual_trace_angle_derivative_intervals": [[encode(x) for x in row] for row in traces],
        "actual_trace_references": [encode(x) for x in references],
        "actual_trace_deviation_angle_derivative_bounds": [[encode(x) for x in row] for row in trace_bounds],
        "complete_horizontal_gradient_bound": encode((qt.c[0]*qt.c[0]+qn.c[0]*qn.c[0]).sqrt().hi),
    }, rho.c[0].lo, radius_bounds, trace_bounds


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--response", type=Path, required=True)
    parser.add_argument("--cut-enclosure", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--box", type=Path,
                        help="Optional rational R27 box; defaults to the published illustrative box")
    args = parser.parse_args()
    started = time.monotonic()
    raw = args.response.read_bytes()
    packet = json.loads(gzip.decompress(raw) if args.response.suffix == ".gz" else raw)
    response = packet["response"]
    if not response["converged"]:
        raise ValueError("A completed response is required")
    enclosure_bytes = args.cut_enclosure.read_bytes()
    root_report = json.loads(enclosure_bytes)
    digest = hashlib.sha256(raw).hexdigest()
    if root_report["input_sha256"] != digest:
        raise ValueError("The complete-mean-root enclosure uses different input")
    direct = next(row for row in root_report["reports"] if row["interpretation"] == "direct_stored_jet")
    if not direct["holonomy"]["complete_real_mean_root_exists"]:
        raise ValueError("The exact complete mean root was not enclosed")
    jets = response["jets"]
    spacing = int(packet["config"]["spacing"])
    if spacing % 2:
        raise ValueError("Half-turn closure requires even frequencies")
    eta = F(direct["holonomy"]["mean_slope_root_correction_abs_upper"]["exact"])
    corrections, correction_report = correction_bounds(jets, spacing, eta)
    geometry, rmin, radius_bounds, trace_bounds = enclose_cartesian(jets, spacing, eta, corrections)
    box = json.loads(args.box.read_text()) if args.box else exterior.DEFAULT_BOX
    target_traces = [list(map(F, box[key])) for key in
                     ("height_trace_bounds", "slope_trace_bounds", "second_trace_bounds")]
    comparisons = {
        "actual_radius_lower": rmin >= F(box["r_min"]),
        "radius_angle_derivative_bounds": [x <= F(y) for x, y in zip(radius_bounds, box["boundary_radius_derivative_bounds"])],
        "actual_trace_bounds": [[x <= y for x, y in zip(row, target)]
                                for row, target in zip(trace_bounds, target_traces)],
        "reference_slope_interval": F(box["mean_slope_interval"][0]) <= F.from_float(jets["backgroundSlope"]) <= F(box["mean_slope_interval"][1]),
        "reference_second_interval": F(box["mean_second_interval"][0]) <= F.from_float(jets["backgroundSecond"]) <= F(box["mean_second_interval"][1]),
    }
    passes = (comparisons["actual_radius_lower"] and comparisons["reference_slope_interval"]
              and comparisons["reference_second_interval"] and all(comparisons["radius_angle_derivative_bounds"])
              and all(all(row) for row in comparisons["actual_trace_bounds"]))
    output = {
        "author": "tail_refinement (GPT-6 Astra Pro, AI-assisted)",
        "status": "EXACT R27 exterior trace box for the corrected represented cut" if passes else "EXACT enclosure computed, specified R27 box not yet proved",
        "scope": __doc__,
        "represented_corrected_cut_cartesian_certificate": passes,
        "actual_radial_tail_certificate": False,
        "source_real_profile_certificate": False,
        "response": str(args.response), "response_sha256": digest,
        "mean_root_enclosure": str(args.cut_enclosure),
        "mean_root_enclosure_sha256": hashlib.sha256(enclosure_bytes).hexdigest(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "cut_helper_sha256": hashlib.sha256(Path(cut.__file__).read_bytes()).hexdigest(),
        "extension_helper_sha256": hashlib.sha256(Path(exterior.__file__).read_bytes()).hexdigest(),
        "interpretation": "direct_stored_jet; r,E,Ep and nonmean coefficients are exact saved binary rationals",
        "exact_mean_root_applied_as_interval": True,
        "complete_second_correction": correction_report,
        "geometry": geometry,
        "R27_target_box": box,
        "R27_target_box_file": str(args.box) if args.box else None,
        "R27_target_box_sha256": hashlib.sha256(args.box.read_bytes()).hexdigest() if args.box else None,
        "R27_box_comparisons": comparisons,
        "elapsed_seconds": time.monotonic()-started,
        "peak_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "limits": [
            "The original response is unchanged; this constructs a nearby exact closed cut two-jet using a real scalar mean root and complete Q correction.",
            "The radial-second correction may have infinitely many modes; only its complete real-circle C2 bounds are used.",
            "No existence or matching of the complete radial isometric tail follows from this local cut construction.",
            "No inside curvature, inner cuff, global graph, or full closed-surface reach claim is made.",
        ],
    }
    args.out.write_text(json.dumps(output, indent=2)+"\n")
    print(json.dumps({"output": str(args.out), "status": output["status"],
                      "correction_bounds": [float(q) for q in corrections],
                      "radius_lower": float(rmin), "radius_derivatives": list(map(float, radius_bounds)),
                      "trace_bounds": [[float(x) for x in row] for row in trace_bounds],
                      "comparisons": comparisons, "elapsed_seconds": output["elapsed_seconds"],
                      "peak_rss_kib": output["peak_rss_kib"]}))


if __name__ == "__main__":
    main()
