#!/usr/bin/env python3
"""True whole-angle complex root potential and canonical inverse-strip input.

This kernel keeps complex values throughout.  The real_jet projection used
by real-axis R83 is deliberately not used on complex angles.
"""
from __future__ import annotations

import argparse
from collections import deque
from fractions import Fraction
import gzip
import hashlib
import json
import math
from pathlib import Path
import time

from flint import acb, acb_series, arb, ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record, primitive_fourier_budget, series_constant
from fourfold_phase_beta_parameter_germ import provenance
from fourfold_phase_canonical_root_jets import (
    CanonicalRootModel, along_shear, cross, derivative, dot, jet_function,
    root_series, trim,
)
from fourfold_time_angle_jets import TimeAngleJet as Jet


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    with (gzip.open(path, "rt") if str(path).endswith(".gz") else Path(path).open()) as f:
        return json.load(f)


def sin_cos(value):
    plus = jet_function(acb(0, 1)*value, "exp")
    minus = jet_function(acb(0, -1)*value, "exp")
    return (plus-minus)/acb(0, 2), (plus+minus)/2


class ComplexRootModel(CanonicalRootModel):
    def __init__(self, object_path, half_width, root_certificate, strip, *, nodes=512):
        super().__init__(object_path, half_width, root_certificate, nodes=nodes, angular_order=0)
        self.strip = exact_arb(strip)
        if not 0 < 4*self.strip < self.budget["sigma_normalized_x"]:
            raise ValueError("the physical complex-angle strip exceeds the Fourier input domain")
        self.complex_errors, self.complex_finite = primitive_fourier_budget(
            nodes, self.budget["sigma_normalized_x"], 4*self.strip, self.budget["radial_radius"],
            self.budget["radius_bound"], self.budget["height_bound"], self.budget["tangent_bound"])

    def complex_phases(self, angle):
        """Centered finite trigonometric Taylor expansion with full remainder.

        The angular derivative jets are evaluated as functions on the whole
        rectangle.  Summation at the center retains exact cancellations among
        distinct Fourier modes; the discarded finite Taylor terms are bounded
        by the complex line-segment Lagrange remainder for each actual mode.
        No midpoint phase is substituted for the true phase on the rectangle.
        """
        n, degree = self.n+1, 8
        center = acb(angle.real.mid(), angle.imag.mid())
        delta = angle-center
        h = (angle.real.rad()**2+angle.imag.rad()**2).sqrt().upper()
        vertical = (abs(center.imag)+angle.imag.rad()).upper()
        length = n+degree
        expansions = [[[acb(0) for _ in range(self.m)] for _ in range(length)]
                      for _ in range(2)]
        remainders = [[[arb(0) for _ in range(self.m)] for _ in range(n)]
                      for _ in range(2)]
        for mode, (beta, gamma) in enumerate(zip(self.beta, self.gamma), 1):
            frequency = 4*mode
            ip, im = acb(0, frequency), acb(0, -frequency)
            ep, em = (ip*center).exp(), (im*center).exp()
            pp = pm = acb(1)
            modulus = (frequency*vertical).exp()
            for j in range(length):
                sine = (pp*ep-pm*em)/(acb(0, 2)*math.factorial(j))
                for component, series in enumerate((beta, gamma)):
                    for i in range(self.m):
                        expansions[component][j][i] += series[i]*sine
                pp, pm = pp*ip, pm*im
            for j in range(n):
                remainder = (modulus*frequency**(j+degree+1)*h**(degree+1)
                             /(math.factorial(j)*math.factorial(degree+1)))
                for component, series in enumerate((beta, gamma)):
                    for i in range(self.m):
                        remainders[component][j][i] += abs(series[i])*remainder
        output = []
        for component in range(2):
            rows = []
            for j in range(n):
                row = []
                for i in range(self.m):
                    value = acb(0)
                    for k in range(degree, -1, -1):
                        value = value*delta+math.comb(j+k,j)*expansions[component][j+k][i]
                    fee = remainders[component][j][i].upper()
                    row.append(value+acb(arb(0,fee),arb(0,fee)))
                rows.append(row)
            output.append(Jet(rows,time_precision=self.m,angle_precision=n))
        return tuple(output)

    def complex_position(self, angle, tangent):
        old, ctx.cap = ctx.cap, self.m
        try:
            first = [series_constant(0, self.m) for _ in range(3)]
            center = acb(angle.real.mid(), angle.imag.mid())
            for k, frequency in enumerate(self.target.frequency):
                phase = (acb(0, frequency)*center).exp()
                for component in range(3):
                    first[component] += acb_series(
                        [self.coefficient[k, component][j] for j in range(self.m)], prec=self.m)*phase
            for component in range(3):
                coefficients = []
                for j in range(self.m):
                    error = (self.complex_errors[0]*(self.scale/self.budget["radial_radius"])**j).upper()
                    coefficients.append(first[component][j]+acb(arb(0, error), arb(0, error)))
                first[component] = acb_series(coefficients, prec=self.m)
            # True holomorphic angular ODE, coefficient by coefficient in r:
            # Z'=G-Jrot Z, Z(center)=0.  On a rectangular angle box,
            # |cos(delta)|<=exp(h_im), |sin(delta)|<=|delta|exp(h_im).
            # This avoids independently boxing all Fourier phases over a
            # complex rectangle, which destroys real geometric cancellation.
            aT = [self.lift(self.radius)*v for v in tangent]
            hr, hi = angle.real.rad().upper(), angle.imag.rad().upper()
            h = (hr*hr+hi*hi).sqrt().upper()
            rotation = hi.exp().upper()
            padded = [[], [], []]
            for i in range(self.m):
                force = [aT[j].coefficient(i, 0) for j in range(3)]
                sizes = [abs(force[0]+first[1][i]).upper(),
                         abs(force[1]-first[0][i]).upper(), abs(force[2]).upper()]
                fees = [(rotation*(h*sizes[0]+h*h*sizes[1]/2)).upper(),
                        (rotation*(h*sizes[1]+h*h*sizes[0]/2)).upper(),
                        (h*sizes[2]).upper()]
                for j in range(3):
                    padded[j].append(first[j][i]+acb(arb(0, fees[j]), arb(0, fees[j])))
            first = [acb_series(padded[j], prec=self.m) for j in range(3)]
            rows = [[first[j]] for j in range(3)]
            for k in range(1, self.n):
                force = [acb_series([aT[j].coefficient(i, k-1) for i in range(self.m)], prec=self.m)
                         for j in range(3)]
                rows[0].append((force[0]+rows[1][k-1])/k)
                rows[1].append((force[1]-rows[0][k-1])/k)
                rows[2].append(force[2]/k)
            return [Jet([[rows[j][k][i] for i in range(self.m)] for k in range(self.n)],
                        time_precision=self.m, angle_precision=self.n) for j in range(3)]
        finally:
            ctx.cap = old

    def complex_root(self, angle):
        old, ctx.cap = ctx.cap, max(self.n+3, self.m+3)
        try:
            B, G = self.complex_phases(angle)
            sb, cb = sin_cos(trim(B, self.m, self.n))
            sg, cg = sin_cos(trim(G, self.m, self.n))
            T = [-sb*cg, cb*cg, sg]
            F = self.complex_position(angle, T)
            m, n = self.m-1, self.n
            keep = lambda v: trim(v, m, n)
            bt, gt = keep(derivative(B, "angle")), keep(derivative(G, "angle"))
            br = -trim(derivative(B, "radial"), m, n)/self.scale
            gr = -trim(derivative(G, "radial"), m, n)/self.scale
            sb, cb, sg, cg = map(keep, (sb, cb, sg, cg))
            T = list(map(keep, T))
            X = [-derivative(v, "radial")/self.scale for v in F]
            F = list(map(keep, F))
            h = -sb*X[0]+cb*X[1]
            v = -cb*X[0]-sb*X[1]
            Q = cg*X[2]-sg*h
            W = Q*Q+v*v
            D = (1+bt)*cg*Q-gt*v
            M = br*cg*Q-gr*v
            H = dot(cross(T, X), F)
            kappa = self.lift(self.kappa, m=m, n=n)
            factors = {"Fz": F[2], "W": W, "D": D, "H": H, "kappa": kappa}
            for name, value in factors.items():
                z = value.coefficient(0, 0)
                if not z.real > 0:
                    raise ValueError("complex root branch not in the right half-plane: "+name)
                radius = z.real.rad()+z.imag.rad()
                center = acb(z.real.mid(), z.imag.mid())
                if not 8*radius < abs(center).lower():
                    raise ValueError("complex root factor rectangle is too wide: "+name)
            invD = jet_function(D, "inverse")
            q = M*invD
            lk, lz, lw, lh, ld = [jet_function(v, "log") for v in (kappa, F[2], W, H, D)]
            logU, logV = lk+4*lz+2*lw-4*lh, lk+2*lw-2*ld
            DU, DV = along_shear(logU, q, self.scale), along_shear(logV, q, self.scale)
            DDU, DDV = along_shear(DU, q, self.scale), along_shear(DV, q, self.scale)
            qt = derivative(q, "angle")
            Dqt = along_shear(qt, q, self.scale)
            s1, s2 = root_series(DU, 1), root_series(DDU, 1)/2
            h1 = root_series(DV, 1)/2-root_series(qt, 1)
            h2 = root_series(DDV, 1)/4-root_series(Dqt, 1)/2
            d1, d2 = h1, h2+h1*h1/2
            cc, ee = 2*d1/5, 2*d2/7-d1*d1/25
            l1, l2 = (s1-cc)/2, (s2-ee+cc*cc/2)/2
            v0 = (-l2+cc*l1-l1*l1/4)[0]
            kp = kappa.coefficient(0, 0)
            yp = D.coefficient(0, 0)/(kp.sqrt()*W.coefficient(0, 0))
            if not yp.real > 0:
                raise ValueError("actual canonical root angle has unresolved positive real derivative")
            if not 2*yp.real.rad() < yp.real.mid():
                raise ValueError("canonical positive real derivative needs a smaller rectangle")
            return {
                "positive_real_factors": {name: ball_record(value.coefficient(0, 0).real)
                                          for name, value in factors.items()},
                "factor_moduli": {name: ball_record(abs(value.coefficient(0, 0)).upper())
                                  for name, value in factors.items()},
                "Y_prime_real": ball_record(yp.real), "Y_prime_modulus": ball_record(abs(yp).upper()),
                "v0_modulus": ball_record(abs(v0).upper())}
        finally:
            ctx.cap = old


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--object", type=Path, default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json"))
    parser.add_argument("--root-certificate", type=Path, default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_step5_local_parameter_root_jets_h5e7.json"))
    parser.add_argument("--root-full-cover", type=Path, default=Path(
        "notes/2026-11-12-actual-canonical-root-full-cover.json.gz"))
    parser.add_argument("--half-width", type=Fraction, default=Fraction(1, 2500000))
    parser.add_argument("--strip", type=Fraction, default=Fraction(1, 256))
    parser.add_argument("--angle-cells", type=int, default=256)
    parser.add_argument("--vertical-cells", type=int, default=16)
    parser.add_argument("--first-cell", type=int, default=0)
    parser.add_argument("--last-cell", type=int, default=128)
    parser.add_argument("--max-depth", type=int, default=10)
    parser.add_argument("--continue-after-failure", action="store_true")
    parser.add_argument("--nodes", type=int, default=512)
    parser.add_argument("--bits", type=int, default=256)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if (args.angle_cells % 2 or args.vertical_cells < 1 or
            not 0 <= args.first_cell < args.last_cell <= args.angle_cells//2):
        raise ValueError("invalid exact half-quarter angular range")
    ctx.prec, ctx.cap = args.bits, 12
    start = time.monotonic()
    model = ComplexRootModel(args.object, args.half_width, args.root_certificate,
                             args.strip, nodes=args.nodes)
    full = read(args.root_full_cover)
    identity = provenance(model.target, args.object)
    if (not full["proved"] or full["exact_parameter_interval"] != identity["exact_parameter_interval"]
            or full["origin_inputs_sha256"] != identity["origin_inputs_sha256"]
            or full["direction_sha256"] != identity["direction_sha256"]
            or full["root_certificate_sha256"] != sha(args.root_certificate)):
        raise ValueError("root circumference and complex germ belong to different actual families")
    report = {
        "kind": "actual_complex_root_potential_and_canonical_inverse_strip",
        "proved": False, "source_sha256": sha(__file__), "object": identity,
        "dependencies": {name: sha(Path(__file__).parent/name) for name in (
            "fourfold_phase_canonical_root_jets.py", "fourfold_time_angle_jets.py",
            "fourfold_phase_beta_interval.py", "fourfold_phase_beta_bulk_interval.py",
            "fourfold_phase_beta_parameter_germ.py")},
        "root_full_cover_sha256": sha(args.root_full_cover),
        "root_certificate_sha256": sha(args.root_certificate),
        "exact_physical_angle_strip": str(args.strip), "angle_cells": args.angle_cells,
        "vertical_cells": args.vertical_cells,
        "complex_cover_symmetry": "upper strip rectangles; exact Schwarz conjugation and D4 reflection fill the full strip",
        "first_cell": args.first_cell, "last_cell": args.last_cell, "bits": args.bits,
        "complex_primitive_uniform_error": ball_record(model.complex_errors[0]),
        "phase_enclosure": "degree-eight centered actual finite trigonometric Taylor expansion plus line-segment remainder",
        "position_enclosure": "true midpoint Fourier primitive plus complex angular ODE Duhamel bound, with exp(imaginary half-width)",
        "cells": [], "failed_cells": [], "attempts": 0,
        "scope": ["Complex values are kept through all geometry and log derivatives.",
                  "All bounds concern the actual common affine parameter box and true roots.",
                  "The canonical inverse-strip conclusion additionally uses the stated analytic injectivity proof.",
                  "No full feedback cutoff or nonlinear zero is asserted."]}
    queue = deque((Fraction(j, args.angle_cells), Fraction(j+1, args.angle_cells),
                   args.strip*k/args.vertical_cells, args.strip*(k+1)/args.vertical_cells, 0)
                  for k in range(args.vertical_cells)
                  for j in range(args.first_cell, args.last_cell))
    def save():
        report["seconds"] = time.monotonic()-start
        report["pending"] = [[str(a), str(b), str(c), str(d), depth] for a, b, c, d, depth in queue]
        args.out.parent.mkdir(parents=True, exist_ok=True)
        temp = args.out.with_suffix(args.out.suffix+".tmp")
        with (gzip.open(temp, "wt") if str(args.out).endswith(".gz") else temp.open("w")) as f:
            json.dump(report, f, indent=2)
            f.write("\n")
        temp.replace(args.out)
    while queue:
        left, right, imag_left, imag_right, depth = queue.popleft()
        report["attempts"] += 1
        real = (exact_arb((left+right)/4)+arb(0, exact_arb((right-left)/4)))*arb.pi()
        imaginary = exact_arb((imag_left+imag_right)/2)+arb(0, exact_arb((imag_right-imag_left)/2))
        angle = acb(real, imaginary)
        try:
            row = model.complex_root(angle)
            row["exact_quarter_interval"] = [str(left), str(right)]
            row["exact_imaginary_interval"] = [str(imag_left), str(imag_right)]
            row["bisection_depth"] = depth
            report["cells"].append(row)
        except (ValueError, ZeroDivisionError) as exc:
            if depth < args.max_depth:
                mid = (left+right)/2
                queue.appendleft((mid, right, imag_left, imag_right, depth+1))
                queue.appendleft((left, mid, imag_left, imag_right, depth+1))
            else:
                report["failed_cells"].append({"interval": [str(left), str(right)],
                    "imaginary_interval": [str(imag_left), str(imag_right)], "reason": str(exc)})
                if not args.continue_after_failure:
                    save()
                    print(json.dumps({"stopped_on_unresolved_rectangle": report["failed_cells"][-1],
                                      "accepted": len(report["cells"])}), flush=True)
                    return
        if report["attempts"] % 32 == 0:
            save()
            print(json.dumps({"attempts": report["attempts"], "accepted": len(report["cells"]),
                              "pending": len(queue), "failed": len(report["failed_cells"]),
                              "seconds": report["seconds"]}), flush=True)
    for k in range(args.vertical_cells):
        imag = [str(args.strip*k/args.vertical_cells), str(args.strip*(k+1)/args.vertical_cells)]
        cursor = Fraction(args.first_cell, args.angle_cells)
        rows = [r for r in report["cells"] if r["exact_imaginary_interval"] == imag]
        for row in sorted(rows, key=lambda r: Fraction(r["exact_quarter_interval"][0])):
            a, b = map(Fraction, row["exact_quarter_interval"])
            if a != cursor:
                raise ValueError("complex root actual angular cover has a gap or overlap")
            cursor = b
        if cursor != Fraction(args.last_cell, args.angle_cells):
            raise ValueError("a complex root vertical slab is incomplete")
    report["proved"] = (args.first_cell == 0 and args.last_cell == args.angle_cells//2
                        and cursor == Fraction(1, 2) and not report["failed_cells"])
    if report["proved"]:
        lo = lambda r: arb(r["lower"]).lower()
        hi = lambda r: arb(r["upper"]).upper()
        yp = min(lo(r["Y_prime_real"]) for r in report["cells"])
        modulus = max(hi(r["v0_modulus"]) for r in report["cells"])
        qlo = lo(full["canonical_full_circle_frequency"]["lower"])
        qhi = hi(full["canonical_full_circle_frequency"]["upper"])
        canonical_strip = (qlo*yp*model.strip/2).lower()
        report["uniform_bounds"] = {
            "Y_prime_real_lower": ball_record(yp),
            "v0_complex_modulus_upper": ball_record(modulus),
            "full_circle_frequency_lower": ball_record(qlo),
            "full_circle_frequency_upper": ball_record(qhi),
            "canonical_normalized_angle_strip": ball_record(canonical_strip),
            "actual_nonzero_fourfold_Fourier_coefficient_rule":
                "abs(v0[4*k]) <= v0_complex_modulus_upper * exp(-4*canonical_normalized_angle_strip*abs(k))"}
    save()
    print(json.dumps({"proved": report["proved"], "accepted": len(report["cells"]),
                      "seconds": report["seconds"]}), flush=True)


if __name__ == "__main__":
    main()
