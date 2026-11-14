#!/usr/bin/env python3
"""R251: one exact shared-node cell, with Arb Bernstein/Laurent enclosures.

All scientific evaluation runs only in the public repository's Actions.
This primitive proves four strict polynomial inequalities conditional on
the supplied scalar-square envelopes. It never verifies those envelopes,
accepts a BVP, substitutes a different metric, or certifies a closed surface.

The exact field is the real quintic through all shared binary nodal jets.
Ordinary floating evaluator error is deliberately a separate obligation.
This file was reconstructed after the local execution environment failed;
its identity is new and does not assert equality with an unavailable file.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import gzip
import hashlib
import json
from math import comb, isfinite
import os
from pathlib import Path
import time

import flint
from flint import arb, acb, arb_poly, acb_poly, fmpq, ctx

SCHEMA = "R251-Arb-Bernstein-Laurent-single-cell-v2"
PACKET_SCHEMA = "exact-shared-node-operator-cell-input-v1"


def actions_only():
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Scientific evaluation is restricted to this public repository's Actions")


def exact(value):
    if isinstance(value, Fraction):
        return value
    if isinstance(value, float):
        if not isfinite(value):
            raise ValueError("Nonfinite binary input")
        return Fraction.from_float(value)
    return Fraction(value)


def ball(value):
    if isinstance(value, arb):
        return value
    value = exact(value)
    return arb(fmpq(value.numerator, value.denominator))


def canonical_sha(value):
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"),
                     ensure_ascii=False, allow_nan=False).encode()
    return hashlib.sha256(raw).hexdigest()


def file_sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def exact_endpoint(value):
    if not value.is_finite() or not value.is_exact():
        raise ValueError("An exact finite Arb endpoint is required")
    return str(value.fmpq())


def ball_record(value):
    value = ball(value)
    if not value.is_finite():
        return dict(finite=False, enclosure=str(value))
    return dict(finite=True, lower=exact_endpoint(value.lower()),
                upper=exact_endpoint(value.upper()), enclosure=value.str(40))


def minimum_lower(values):
    values = list(values)
    if not values or any(not value.is_finite() for value in values):
        raise ValueError("A nonempty finite enclosure list is required")
    result = values[0].lower()
    for value in values[1:]:
        candidate = value.lower()
        if candidate < result:
            result = candidate
    return result


def exact_hermite_controls(left, right, nodal):
    """All r/t/z coefficients, with exact rational physical h."""
    h = exact(right) - exact(left)
    if h <= 0 or len(nodal) != 3 or any(len(pair) != 2 for pair in nodal):
        raise ValueError("Supply a positive cell and three pairs of full nodal jets")
    n = len(nodal[0][0])
    if any(len(row) != n for pair in nodal for row in pair):
        raise ValueError("All shared nodal jets have the same full state dimension")
    result = [[] for _ in range(6)]
    for k in range(n):
        y0, y1 = (exact(nodal[0][j][k]) for j in (0, 1))
        v0, v1 = (exact(nodal[1][j][k]) for j in (0, 1))
        a0, a1 = (exact(nodal[2][j][k]) for j in (0, 1))
        values = (y0, y0+h*v0/5, y0+2*h*v0/5+h*h*a0/20,
                  y1-2*h*v1/5+h*h*a1/20, y1-h*v1/5, y1)
        for row, value in zip(result, values):
            row.append(ball(value))
    return result


def split_controls(controls, t):
    t = ball(t)
    levels = [[list(row) for row in controls]]
    while len(levels[-1]) > 1:
        previous = levels[-1]
        levels.append([[(1-t)*a+t*b for a, b in zip(left, right)]
                       for left, right in zip(previous[:-1], previous[1:])])
    return [level[0] for level in levels], [level[-1] for level in reversed(levels)]


def restrict_controls(controls, lower, upper):
    lower, upper = exact(lower), exact(upper)
    if not 0 <= lower < upper <= 1:
        raise ValueError("The requested interval must lie inside the original cell")
    if upper < 1:
        controls = split_controls(controls, upper)[0]
    if lower > 0:
        controls = split_controls(controls, lower/upper)[1]
    return controls


def scalar_power_to_bernstein(power):
    degree = len(power)-1
    return [sum((ball(power[k])*ball(Fraction(comb(j, k), comb(degree, k)))
                 for k in range(j+1)), arb(0)) for j in range(degree+1)]


@dataclass
class BernsteinLaurent:
    """Real coefficients of e^(2 i k phi), radially in Bernstein basis.

    Intermediate i*T and i*B are imaginary-valued, with real antisymmetric
    Laurent coefficients. The four final functions are real by the exact
    algebraic construction, not by a numerical imaginary-part test.
    """
    controls: list
    width: int

    @property
    def degree(self):
        return len(self.controls)-1

    @classmethod
    def constant(cls, value):
        return cls([arb_poly([ball(value)])], 0)

    @classmethod
    def scalar(cls, values):
        return cls([arb_poly([ball(value)]) for value in values], 0)

    def elevate(self, degree):
        if degree < self.degree:
            raise ValueError("Degree reduction would discard information")
        if degree == self.degree:
            return self
        p, q = self.degree, degree-self.degree
        result = []
        for k in range(degree+1):
            value = arb_poly([])
            for i in range(max(0, k-q), min(p, k)+1):
                weight = Fraction(comb(p, i)*comb(q, k-i), comb(degree, k))
                value = value+self.controls[i]*ball(weight)
            result.append(value)
        return BernsteinLaurent(result, self.width)

    def widen(self, width):
        if width < self.width:
            raise ValueError("Angular truncation is forbidden")
        return BernsteinLaurent(
            [p.left_shift(width-self.width) for p in self.controls], width)

    def __neg__(self):
        return BernsteinLaurent([-p for p in self.controls], self.width)

    def __add__(self, other):
        if not isinstance(other, BernsteinLaurent):
            other = BernsteinLaurent.constant(other)
        degree, width = max(self.degree, other.degree), max(self.width, other.width)
        a, b = self.elevate(degree).widen(width), other.elevate(degree).widen(width)
        return BernsteinLaurent([x+y for x, y in zip(a.controls, b.controls)], width)

    __radd__ = __add__

    def __sub__(self, other):
        return self+(-other if isinstance(other, BernsteinLaurent)
                     else BernsteinLaurent.constant(-ball(other)))

    def __rsub__(self, other):
        return (-self)+other

    def __mul__(self, other):
        if not isinstance(other, BernsteinLaurent):
            value = ball(other)
            return BernsteinLaurent([p*value for p in self.controls], self.width)
        p, q = self.degree, other.degree
        result = [arb_poly([]) for _ in range(p+q+1)]
        if other is self:
            for i in range(p+1):
                for j in range(i, p+1):
                    weight = Fraction(comb(p, i)*comb(p, j), comb(2*p, i+j))
                    if i != j:
                        weight *= 2
                    result[i+j] = result[i+j]+self.controls[i]*self.controls[j]*ball(weight)
        else:
            for i in range(p+1):
                for j in range(q+1):
                    weight = Fraction(comb(p, i)*comb(q, j), comb(p+q, i+j))
                    result[i+j] = result[i+j]+self.controls[i]*other.controls[j]*ball(weight)
        return BernsteinLaurent(result, self.width+other.width)

    __rmul__ = __mul__

    def derivative_s(self, physical_width):
        if self.degree == 0:
            return BernsteinLaurent.constant(0)
        scale = ball(self.degree)/ball(physical_width)
        return BernsteinLaurent([(b-a)*scale for a, b in
                                 zip(self.controls[:-1], self.controls[1:])], self.width)

    def i_derivative_phi(self):
        return BernsteinLaurent(
            [arb_poly([-2*(j-self.width)*p[j] for j in range(2*self.width+1)])
             for p in self.controls], self.width)

    def at_radial(self, t):
        values = self.controls[:]
        t = ball(t)
        while len(values) > 1:
            values = [(1-t)*a+t*b for a, b in zip(values[:-1], values[1:])]
        return values[0]


def cosine_laurent(values):
    M = len(values)-1
    coefficients = [arb(0) for _ in range(2*M+1)]
    coefficients[M] = ball(values[0])
    for m in range(1, M+1):
        coefficients[M-m] = coefficients[M+m] = ball(values[m])/2
    return arb_poly(coefficients)


def i_sine_laurent(values):
    M = len(values)
    coefficients = [arb(0) for _ in range(2*M+1)]
    for m, value in enumerate(values, 1):
        coefficients[M+m], coefficients[M-m] = ball(value)/2, -ball(value)/2
    return arb_poly(coefficients)


def physical_metric_polynomials(controls, width, M):
    if len(controls) != 6 or any(len(row) != 3*M+2 for row in controls):
        raise ValueError("Retain every physical coefficient, including z0")
    R = BernsteinLaurent([cosine_laurent(row[:M+1]) for row in controls], M)
    JT = BernsteinLaurent([i_sine_laurent(row[M+1:2*M+1]) for row in controls], M)
    Z = BernsteinLaurent([cosine_laurent(row[2*M+1:]) for row in controls], M)
    Rs, JTs, Zs = (p.derivative_s(width) for p in (R, JT, Z))
    JPr = R.i_derivative_phi()-JT
    Pt = -JT.i_derivative_phi()+R
    JPz = Z.i_derivative_phi()
    E = Rs*Rs-JTs*JTs+Zs*Zs
    C = -JPr*JPr+Pt*Pt-JPz*JPz
    JB = Rs*JPr+JTs*Pt+Zs*JPz
    return E, JB, C


class AngularCertificate:
    """Rigorous uniform evaluations by Bluestein and Arb polynomial products."""
    def __init__(self, full_circle_points=2048, max_full_circle_points=32768):
        if (full_circle_points < 4 or full_circle_points % 2 or
                max_full_circle_points < full_circle_points):
            raise ValueError("Use a positive even full-circle grid")
        self.first = int(full_circle_points)
        self.maximum = int(max_full_circle_points)
        self.cache = {}

    @staticmethod
    def root(numerator, denominator):
        sn, cs = arb.sin_cos_pi_fmpq(fmpq(numerator, denominator))
        return acb(cs, sn)

    def data(self, width, L):
        key = (width, L, int(ctx.prec))
        if key not in self.cache:
            chirp = [self.root(k*k, L) for k in range(-width, width+1)]
            kernel = acb_poly([self.root(-k*k, L)
                               for k in range(-width, L+width)])
            output = [self.root(j*j, L) for j in range(L)]
            self.cache[key] = chirp, kernel, output
        return self.cache[key]

    def values(self, polynomial, width, full_circle_points, derivative=False):
        L = full_circle_points//2
        chirp, kernel, output = self.data(width, L)
        coefficients = []
        for i, k in enumerate(range(-width, width+1)):
            value = acb(polynomial[i])*chirp[i]
            if derivative:
                value = value*acb(0, 2*k)
            coefficients.append(value)
        product = acb_poly(coefficients)*kernel
        answer = [product[j+2*width]*output[j] for j in range(L)]
        if any(not value.is_finite() or not value.imag.contains(0) for value in answer):
            raise ArithmeticError("A final real Laurent evaluation lost its finite real enclosure")
        return [value.real for value in answer]

    def certify(self, polynomial, width):
        S2 = sum((ball((2*k)**2)*polynomial[k+width].abs_upper()
                  for k in range(-width, width+1)), arb(0)).upper()
        points = self.first
        while True:
            values = self.values(polynomial, width, points)
            derivatives = self.values(polynomial, width, points, derivative=True)
            delta = (arb.pi()/points).upper()
            lowers = [v-delta*d.abs_upper()-delta*delta*S2/2
                      for v, d in zip(values, derivatives)]
            lower = minimum_lower(lowers)
            sampled = minimum_lower(values)
            result = dict(certified=bool(lower > 0),
                full_circle_points=points, distinct_pi_periodic_points=points//2,
                integer_angular_bandwidth=2*width, lower=ball_record(lower),
                sampled_lower=ball_record(sampled), second_derivative_l1_upper=ball_record(S2),
                nearest_angle_gap_upper=ball_record(delta),
                arithmetic="Arb enclosures; native polynomial Bluestein convolution; no ordinary FFT",
                theorem="R251 Bernstein convex hull and full-coefficient angular Taylor remainder")
            if result["certified"] or sampled <= 0 or 2*points > self.maximum:
                return result
            points *= 2


def build_operator_functions(controls, cell_width, core, lower, upper, eta, M):
    eta = ball(eta)
    if not bool(eta > 0) or not bool(eta < 1):
        raise ValueError("The exact requested eta must lie strictly between zero and one")
    E, JB, C = physical_metric_polynomials(controls, cell_width, M)
    density = [Fraction(1)]+[(1-4*m*m)*exact(value) for m, value in enumerate(core, 1)]
    rho = BernsteinLaurent([cosine_laurent(density)], len(core))
    rho2 = rho*rho
    L, U = BernsteinLaurent.scalar(lower), BernsteinLaurent.scalar(upper)
    Uplus, Uminus = BernsteinLaurent.constant(1+eta)-E, E-BernsteinLaurent.constant(1-eta)
    negative_B2 = JB*JB
    functions = dict(Uplus=Uplus, Uminus=Uminus,
        Dplus=Uplus*((L*rho2)*(1+eta)-C)+negative_B2,
        Dminus=Uminus*(C-(U*rho2)*(1-eta))+negative_B2)
    return functions, rho


def certify_cell(controls, cell_width, core, lower, upper, eta, M, *,
                 angular=None, known_density=None):
    actions_only()
    angular = angular or AngularCertificate()
    functions, rho = build_operator_functions(controls, cell_width, core, lower, upper, eta, M)
    core_sha = canonical_sha([str(exact(value)) for value in core])
    if known_density is None:
        density = angular.certify(rho.controls[0], rho.width)
        density["complete_core_sha256"] = core_sha
    else:
        if (known_density.get("certified") is not True or
                known_density.get("complete_core_sha256") != core_sha):
            raise ValueError("A reusable density certificate must bind this full exact core")
        density = known_density
    scalar_lower = minimum_lower([ball(x) for x in lower])
    scalar_upper_positive = minimum_lower([ball(x) for x in upper])
    rows = {}
    for name, polynomial in functions.items():
        worst = None
        tested = 0
        success = True
        largest_grid = 0
        for i, control in enumerate(polynomial.controls):
            report = angular.certify(control, polynomial.width)
            tested += 1
            largest_grid = max(largest_grid, report["full_circle_points"])
            value = Fraction(report["lower"]["lower"])
            if worst is None or value < worst[0]:
                worst = value, i, report
            if not report["certified"]:
                success = False
                break
        rows[name] = dict(certified=success, radial_degree=polynomial.degree,
            integer_angular_bandwidth=2*polynomial.width, controls_tested=tested,
            controls_total=len(polynomial.controls), largest_full_circle_grid=largest_grid,
            worst_control=worst[1], worst=worst[2])
    passed = bool(density["certified"] and scalar_lower > 0 and
                  scalar_upper_positive > 0 and all(v["certified"] for v in rows.values()))
    return dict(schema=SCHEMA, certified_under_scalar_envelopes=passed,
        scalar_envelopes_verified_here=False, complete_core_sha256=core_sha,
        complete_density=density, scalar_lower_Bernstein_hull=ball_record(scalar_lower),
        scalar_upper_Bernstein_positive_hull=ball_record(scalar_upper_positive),
        four_positive_functions=rows, exact_requested_eta=str(exact(eta)),
        full_physical_state_retained=True, full_mean_height_retained=True,
        angular_mode_truncation_used=False, all_radial_and_angular_points_covered_conditionally=passed,
        exact_real_shared_node_field=True, literal_floating_evaluator_error_verified=False,
        closed_surface_certified=False, task_completed=False)


def point_failure_witness(controls, cell_width, core, scalar_at_midpoint, eta, M,
                          angular, points=None):
    """A negative upper endpoint at a true point is a genuine failure witness.

    A failed Bernstein or scalar-envelope check alone is never such a witness.
    """
    actions_only()
    a2 = scalar_at_midpoint*scalar_at_midpoint
    functions, _ = build_operator_functions(controls, cell_width, core, [a2], [a2], eta, M)
    points = angular.first if points is None else int(points)
    for name, function in functions.items():
        polynomial = function.at_radial(Fraction(1, 2))
        for j, value in enumerate(angular.values(polynomial, function.width, points)):
            if value.upper() < 0:
                return dict(proved_failure_of_strict_eta_bound=True, function=name,
                    radial_fraction="1/2", phi_over_pi=str(Fraction(2*j, points)),
                    full_circle_points=points, value=ball_record(value),
                    uses_actual_scalar_value=True, uses_a_Bernstein_control_as_a_point=False)
    return None


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw)


def write(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(data, indent=2, ensure_ascii=False, allow_nan=False)+"\n").encode()
    path.write_bytes(gzip.compress(raw, mtime=0) if path.suffix == ".gz" else raw)


def main():
    actions_only()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--packet", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--precision", type=int, default=160)
    parser.add_argument("--angular-points", type=int, default=2048)
    parser.add_argument("--max-angular-points", type=int, default=32768)
    args = parser.parse_args()
    if args.precision < 80:
        raise ValueError("Use at least 80-bit Arb working precision")
    ctx.prec = args.precision
    packet = read(args.packet)
    if packet.get("schema") != PACKET_SCHEMA:
        raise ValueError("Unknown exact cell packet")
    left, right = map(exact, packet["physical_cell"])
    controls = exact_hermite_controls(left, right, packet["physical_nodal_jets"])
    a, b = map(exact, packet.get("check_interval", packet["physical_cell"]))
    controls = restrict_controls(controls, (a-left)/(right-left), (b-left)/(right-left))
    envelope = packet["scalar_square_envelopes"]
    begin = time.monotonic()
    result = certify_cell(controls, b-a, packet["complete_core_coefficients"],
        envelope["lower_Bernstein"], envelope["upper_Bernstein"], packet["eta"],
        int(packet["field_modes"]),
        angular=AngularCertificate(args.angular_points, args.max_angular_points))
    result.update(source_sha256=file_sha(__file__), packet_sha256=file_sha(args.packet),
        flint_version=flint.__version__, working_precision_bits=int(ctx.prec),
        physical_cell=list(map(str, (left, right))), checked_interval=list(map(str, (a, b))),
        scalar_envelope_identity=envelope.get("identity"),
        external_envelope_claim_treated_as_proof=False,
        input_source_identity=packet.get("source_identity"), seconds=time.monotonic()-begin)
    write(args.out, result)
    print(json.dumps(dict(event="R251_single_cell", output=str(args.out),
        certified_under_scalar_envelopes=result["certified_under_scalar_envelopes"],
        scalar_envelopes_verified_here=False, seconds=result["seconds"])), flush=True)
    raise SystemExit(0 if result["certified_under_scalar_envelopes"] else 2)


if __name__ == "__main__":
    main()
