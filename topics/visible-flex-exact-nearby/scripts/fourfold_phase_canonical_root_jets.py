#!/usr/bin/env python3
"""Directed finite canonical root jets of the actual grounded R37 operator.

This pays finite jets at the true moving root, not a whole canonical collar.
The angle variable is physical theta.  All radial derivatives are taken in
the one actual common polynomial germ containing the certified root family.
The infinite position primitive is paid before its exact angular ODE is used.
"""
from __future__ import annotations

import argparse
from collections import deque
from fractions import Fraction
import hashlib
import gzip
import json
import math
from pathlib import Path
import time

from flint import acb, acb_series, arb, ctx

from fourfold_phase_beta_affine import load_definition
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import (
    add_real_cauchy_error, ball_record, series_constant, series_real,
)
from fourfold_phase_beta_parameter_germ import ParameterGermBallTarget, provenance
from fourfold_time_angle_jets import TimeAngleJet as Jet


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def trim(value, m, n):
    if m > value.m or n > value.n or min(m, n) < 1:
        raise ValueError("cannot fill unknown Taylor coefficients with zero")
    return Jet([[value.coefficient(i, j) for i in range(m)] for j in range(n)],
               time_precision=m, angle_precision=n)


def real_jet(value):
    return Jet([[acb(value.coefficient(i, j).real) for i in range(value.m)]
                for j in range(value.n)], time_precision=value.m, angle_precision=value.n)


def derivative(value, axis):
    if axis == "radial":
        if value.m < 2:
            raise ValueError("unknown radial derivative")
        return Jet([[(i+1)*value.coefficient(i+1, j) for i in range(value.m-1)]
                    for j in range(value.n)], time_precision=value.m-1, angle_precision=value.n)
    if axis == "angle":
        if value.n < 2:
            raise ValueError("unknown angular derivative")
        return Jet([[(j+1)*value.coefficient(i, j+1) for i in range(value.m)]
                    for j in range(value.n-1)], time_precision=value.m, angle_precision=value.n-1)
    raise ValueError("unknown derivative axis")


def along_shear(value, q, scale):
    """D=-partial_r+q partial_theta=(1/scale)partial_w+q partial_theta."""
    m, n = value.m-1, value.n-1
    return (trim(derivative(value, "radial"), m, n)/scale
            +trim(q, m, n)*trim(derivative(value, "angle"), m, n))


def root_series(value, n):
    if n > value.n:
        raise ValueError("unknown root angular jet")
    return acb_series([value.coefficient(0, j) for j in range(n)], prec=n)


def real_series_exp(value):
    """Coefficient recurrence with the real exponential branch kept exact.

    Native power-series Newton steps may widen the constant coefficient on
    interval inputs.  This recurrence fixes it at exp(value[0]) and propagates
    every retained angular coefficient by the exact differential identity.
    """
    output = [acb(value[0].real.exp())]
    for j in range(1, value.prec):
        output.append(sum((k*value[k]*output[j-k] for k in range(1, j+1)), acb(0))/j)
    return acb_series(output, prec=value.prec)


def time_function(value, operation):
    """Formal time recurrence, with no Newton cancellation of interval zero."""
    m = value.prec
    f = [value[i] for i in range(m)]
    if operation == "exp":
        g = [f[0].exp()]
        for j in range(1, m):
            g.append(sum((k*f[k]*g[j-k] for k in range(1, j+1)), acb(0))/j)
    else:
        inverse = [1/f[0]]
        for j in range(1, m):
            inverse.append(-inverse[0]*sum((f[k]*inverse[j-k] for k in range(1, j+1)), acb(0)))
        if operation == "inverse":
            g = inverse
        elif operation == "log":
            g = [f[0].log()]
            for j in range(1, m):
                g.append(sum((k*f[k]*inverse[j-k] for k in range(1, j+1)), acb(0))/j)
        else:
            raise ValueError("unsupported finite root-jet function")
    return acb_series(g, prec=m)


def jet_function(value, operation):
    old = ctx.cap
    ctx.cap = value.m
    try:
        f = [acb_series([value.coefficient(i, j) for i in range(value.m)], prec=value.m)
             for j in range(value.n)]
        zero = series_constant(0, value.m)
        if operation == "exp":
            g = [time_function(f[0], "exp")]
            for j in range(1, value.n):
                g.append(sum((k*f[k]*g[j-k] for k in range(1, j+1)), zero)/j)
        else:
            inverse = [time_function(f[0], "inverse")]
            for j in range(1, value.n):
                inverse.append(-inverse[0]*sum((f[k]*inverse[j-k] for k in range(1, j+1)), zero))
            if operation == "inverse":
                g = inverse
            elif operation == "log":
                g = [time_function(f[0], "log")]
                for j in range(1, value.n):
                    g.append(sum((k*f[k]*inverse[j-k] for k in range(1, j+1)), zero)/j)
            else:
                raise ValueError("unsupported rectangular root-jet function")
        return Jet([[g[j][i] for i in range(value.m)] for j in range(value.n)],
                   time_precision=value.m, angle_precision=value.n)
    finally:
        ctx.cap = old


def jet_sin_cos(value):
    plus = jet_function(acb(0, 1)*value, "exp")
    minus = jet_function(acb(0, -1)*value, "exp")
    return real_jet((plus-minus)/acb(0, 2)), real_jet((plus+minus)/2)


def dot(left, right):
    return sum((x*y for x, y in zip(left, right)), 0)


def cross(left, right):
    return [left[1]*right[2]-left[2]*right[1],
            left[2]*right[0]-left[0]*right[2],
            left[0]*right[1]-left[1]*right[0]]


def root_family(target, certificate):
    saved = json.loads(Path(certificate).read_text())
    if not saved.get("proved"):
        raise ValueError("unproved moving-root input")
    if saved["origin_inputs_sha256"] != target.parameter_definition["origin_inputs"]["sha256"]:
        raise ValueError("root origin mismatch")
    if saved["frozen_direction_sha256"] != target.parameter_definition["direction"]["sha256"]:
        raise ValueError("root direction mismatch")
    left, right = map(Fraction, saved["exact_parameter_interval"])
    if not left <= target.parameter_interval[0] <= target.parameter_interval[1] <= right:
        raise ValueError("requested parameter family exceeds the proved root family")
    lo, hi = map(Fraction, saved["transported_root_interval_exact"])
    root = exact_arb(lo).union(exact_arb(hi))
    # NativeSpline.germ selects by a binary midpoint. Check that every physical
    # and reflected scalar polynomial uses one common actual interior span.
    spans = []
    splines = [target.raw, target.raw_direction, target.base, target.shift,
               *target.means, *target.height_integrals]
    for spline in splines:
        for sign in (-1, 1):
            c = sign*root
            selector = float(c.mid())
            index = int(__import__("bisect").bisect_right(spline.knots_float, selector)-1)
            if not (arb(spline.knots[index]) < c and c < arb(spline.knots[index+1])):
                raise ValueError("root box is not strictly in one common polynomial span")
            spans.append({"sign": sign, "left": str(Fraction(float(spline.knots_float[index]))),
                          "right": str(Fraction(float(spline.knots_float[index+1])))})
    return root, spans


class CanonicalRootModel:
    def __init__(self, object_path, half_width, root_certificate, *, nodes=512,
                 angular_order=4, scale=Fraction(1, 1024)):
        self.order = angular_order
        self.n = angular_order+4
        self.m = 5
        self.scale = exact_arb(scale)
        self.target = ParameterGermBallTarget(object_path, half_width, nodes, nodes)
        self.root, self.spans = root_family(self.target, root_certificate)
        old = ctx.cap
        ctx.cap = max(8, self.m+3)
        try:
            self.budget = self.target.analytic_input_budget(
                self.root, arb(".003"), arb(".32"), arb(".0025"))
            self.coefficient, self.radius, self.E, self.C, self.K = self.target.target(
                self.root, self.scale, self.budget)
            self.beta, self.gamma, _, _ = self.target.scalars(acb(self.root), -self.scale)
            # Exact K(t)=0 is used only after the true infinite E coefficients
            # have been enclosed. No interval K[0]/w division is performed.
            self.kappa = acb_series([-self.K[j+1]/self.scale for j in range(4)], prec=4)
        finally:
            ctx.cap = old
        if not self.kappa[0].real > 0:
            raise ValueError("unresolved positive simple-root curvature quotient")

    def lift(self, value, m=None, n=None):
        return Jet.from_time_series(value, time_precision=m or self.m,
                                    angle_precision=n or self.n)

    def phases(self, angle):
        theta = Jet.constant(acb(angle), time_precision=self.m, angle_precision=self.n+1)
        theta = theta+Jet.variable("angle", time_precision=self.m, angle_precision=self.n+1)
        plus = jet_function(acb(0, 4)*theta, "exp")
        minus = jet_function(acb(0, -4)*theta, "exp")
        ep = em = Jet.constant(1, time_precision=self.m, angle_precision=self.n+1)
        B = G = Jet.constant(0, time_precision=self.m, angle_precision=self.n+1)
        for b, g in zip(self.beta, self.gamma):
            ep, em = ep*plus, em*minus
            sine = (ep-em)/acb(0, 2)
            B = B+self.lift(b, n=self.n+1)*sine
            G = G+self.lift(g, n=self.n+1)*sine
        return real_jet(B), real_jet(G)

    def position(self, angle, T):
        old = ctx.cap
        ctx.cap = self.m
        try:
            first = [series_constant(0, self.m) for _ in range(3)]
            for k, frequency in enumerate(self.target.frequency):
                phase = (acb(0, frequency)*acb(angle.mid())).exp()
                for component in range(3):
                    value = acb_series([self.coefficient[k, component][j]
                                        for j in range(self.m)], prec=self.m)
                    first[component] += value*phase
            first = [add_real_cauchy_error(series_real(value),
                         self.budget["field_errors"][0], self.scale,
                         self.budget["radial_radius"]) for value in first]
            aT = [self.lift(self.radius)*value for value in T]
            # Transport every radial coefficient from the true midpoint by
            # F_theta=aT-Jrot F.  For Z=F-F(mid), the forcing is aT-Jrot F(mid).
            # Exact real rotations give error0 <= h M0+h^2 M1/2 and the
            # symmetric error1; the vertical equation gives h M2.  This pays
            # the whole angular interval without boxing each Fourier phase.
            h = angle.rad().upper()
            middle = first
            padded = [[], [], []]
            for i in range(self.m):
                forcing = [aT[j].coefficient(i, 0).real for j in range(3)]
                sizes = [abs(forcing[0]+middle[1][i].real).upper(),
                         abs(forcing[1]-middle[0][i].real).upper(),
                         abs(forcing[2]).upper()]
                fees = [(h*sizes[0]+h*h*sizes[1]/2).upper(),
                        (h*sizes[1]+h*h*sizes[0]/2).upper(), (h*sizes[2]).upper()]
                for j in range(3):
                    padded[j].append(acb(middle[j][i].real+arb(0, fees[j])))
            first = [acb_series(padded[j], prec=self.m) for j in range(3)]
            rows = [[first[j]] for j in range(3)]
            for k in range(1, self.n):
                forcing = [acb_series([aT[j].coefficient(i, k-1)
                                      for i in range(self.m)], prec=self.m) for j in range(3)]
                rows[0].append((forcing[0]+rows[1][k-1])/k)
                rows[1].append((forcing[1]-rows[0][k-1])/k)
                rows[2].append(forcing[2]/k)
            return [real_jet(Jet([[rows[j][k][i] for i in range(self.m)]
                                 for k in range(self.n)],
                                time_precision=self.m, angle_precision=self.n)) for j in range(3)]
        finally:
            ctx.cap = old

    def evaluate(self, angle):
        old = ctx.cap
        ctx.cap = max(self.n+2, self.m+2)
        try:
            B, G = self.phases(angle)
            sb, cb = jet_sin_cos(trim(B, self.m, self.n))
            sg, cg = jet_sin_cos(trim(G, self.m, self.n))
            T = [-sb*cg, cb*cg, sg]
            F = self.position(angle, T)
            m, n = self.m-1, self.n
            keep = lambda v: trim(v, m, n)
            a = self.lift(self.radius, m=m)
            ar = -self.lift(self.radius.derivative(), m=m)/self.scale
            bt, gt = keep(derivative(B, "angle")), keep(derivative(G, "angle"))
            br = -trim(derivative(B, "radial"), m, n)/self.scale
            gr = -trim(derivative(G, "radial"), m, n)/self.scale
            sb, cb, sg, cg = map(keep, (sb, cb, sg, cg))
            T = list(map(keep, T))
            Tt = [-cb*cg*(1+bt)+sb*sg*gt,
                  -sb*cg*(1+bt)-cb*sg*gt, cg*gt]
            Tr = [-cb*cg*br+sb*sg*gr, -sb*cg*br-cb*sg*gr, cg*gr]
            X = [-derivative(v, "radial")/self.scale for v in F]
            F = list(map(keep, F))
            Y = [a*v for v in T]
            h = -sb*X[0]+cb*X[1]
            v = -cb*X[0]-sb*X[1]
            Q = cg*X[2]-sg*h
            W = real_jet(Q*Q+v*v)
            D = real_jet((1+bt)*cg*Q-gt*v)
            M = real_jet(br*cg*Q-gr*v)
            H = real_jet(dot(cross(T, X), F))
            kappa = self.lift(self.kappa, m=m)
            for name, value in (("Fz", F[2]), ("W", W), ("D", D), ("H", H), ("kappa", kappa)):
                if not value.coefficient(0, 0).real > 0:
                    raise ValueError("unresolved positive root factor "+name)
                constant = value.coefficient(0, 0).real
                if not 4*constant.rad() < constant.mid():
                    raise ValueError("root factor needs a narrower angular box: "+name)
            q = real_jet(M*jet_function(D, "inverse"))
            # U=alpha*(kappa*eta), V=(kappa*eta)/alpha.  Cancel all
            # Fz/H powers in V before interval arithmetic, as in R64.
            logk, logz, logw, logh, logd = [jet_function(z, "log") for z in (kappa, F[2], W, H, D)]
            logU = real_jet(logk+4*logz+2*logw-4*logh)
            logV = real_jet(logk+2*logw-2*logd)
            nf = self.order+1
            qtheta = derivative(q, "angle")
            ja = root_series(qtheta, nf)
            jb = root_series(along_shear(qtheta, q, self.scale), nf)/2
            jc = root_series(along_shear(along_shear(qtheta, q, self.scale), q, self.scale), nf)/6
            def log_coefficients(value):
                first = along_shear(value, q, self.scale)
                second = along_shear(first, q, self.scale)
                third = along_shear(second, q, self.scale)
                return [root_series(first, nf), root_series(second, nf)/2,
                        root_series(third, nf)/6]
            ss, vv = log_coefficients(logU), log_coefficients(logV)
            h1, h2, h3 = [vv[j]/2-[ja, jb, jc][j] for j in range(3)]
            d1, d2, d3 = h1, h2+h1*h1/2, h3+h1*h2+h1**3/6
            c = 2*d1/5
            e = 2*d2/7-d1*d1/25
            f = 2*d3/9-2*d1*d2/35+4*d1**3/375
            l1 = (ss[0]-c)/2
            l2 = (ss[1]-e+c*c/2)/2
            l3 = (ss[2]-f+c*e-c**3/3)/2
            L1, L2 = l1, l2-c*l1
            L3 = l3-2*c*l2+(2*c*c-e)*l1
            u0, w0 = root_series(logU, nf+2), root_series(logV, nf+2)
            hh, lb0 = -u0/4, (u0+w0)/2
            q1 = -real_series_exp(w0)*(hh.derivative().derivative()+hh.derivative()**2+lb0.derivative()*hh.derivative())
            q1 = acb_series([q1[j] for j in range(nf)], prec=nf)
            v0 = -L2-L1*L1/4
            v1 = q1-3*L3-L1*L2
            yprime = real_series_exp(-w0/2)
            yprime_inv = real_series_exp(w0/2)
            logY = real_jet(logz-jet_function(real_jet(dot(F, F)), "log")/2)
            y0 = root_series(logY, nf+2)
            height = real_series_exp(y0-u0/4)
            source_factor = real_series_exp(y0-u0/4+w0/2)
            flux_factor = real_series_exp(-u0/4+w0/2)
            jets = {}
            for name, value in (("V_root", v0), ("V_xi_root", v1),
                                ("root_momentum_shear", L1/2),
                                ("physical_height", height), ("source_root_factor", source_factor),
                                ("grounded_flux_root_factor", flux_factor)):
                output = []
                for j in range(nf):
                    output.append(ball_record(value[0].real))
                    if j+1 < nf:
                        derivative_value = value.derivative()
                        value = derivative_value*acb_series([yprime_inv[k] for k in range(derivative_value.prec)],
                                                          prec=derivative_value.prec)
                jets[name+"_canonical_angle_derivatives"] = output
            root_value = lambda v: ball_record(v.coefficient(0, 0).real)
            return {"angle_box": ball_record(angle), "alpha": ball_record(((u0[0]-w0[0])/2).real.exp()),
                    "B": ball_record(((u0[0]+w0[0])/2).real.exp()), "q": root_value(q),
                    "Y_prime": ball_record(yprime[0].real),
                    "t0": ball_record((-u0[0]/4).real.exp()),
                    "physical_n": root_value(-a*a*D), "physical_support_numerator": root_value(a*H),
                    "physical_Fz": root_value(F[2]), "D": root_value(D), "W": root_value(W), **jets}
        finally:
            ctx.cap = old


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--object", type=Path, default=Path("data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json"))
    parser.add_argument("--half-width", default="1/2500000")
    parser.add_argument("--root-certificate", type=Path, default=Path("data/phase_ring_continuation/type_fixed_step02_d5_step5_local_parameter_root_jets_h5e7.json"))
    parser.add_argument("--nodes", type=int, default=512)
    parser.add_argument("--order", type=int, default=4)
    parser.add_argument("--cells", type=int, default=256)
    parser.add_argument("--max-depth", type=int, default=10)
    parser.add_argument("--first-cell", type=int, default=0)
    parser.add_argument("--last-cell", type=int)
    parser.add_argument("--bits", type=int, default=224)
    parser.add_argument("--point", help="diagnostic physical angle as a rational multiple of pi")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    ctx.prec, ctx.cap = args.bits, max(10, args.order+6)
    started = time.monotonic()
    model = CanonicalRootModel(args.object, Fraction(args.half_width), args.root_certificate,
                               nodes=args.nodes, angular_order=args.order)
    dependencies = ["fourfold_phase_beta_affine.py", "fourfold_phase_beta_interval.py",
                    "fourfold_phase_beta_parameter_germ.py", "fourfold_phase_beta_bulk_interval.py",
                    "fourfold_time_angle_jets.py"]
    adapter_identity = provenance(model.target, args.object)
    adapter_source = adapter_identity.pop("source_sha256")
    adapter_dependencies = adapter_identity.pop("dependency_sha256")
    adapter_dependencies.update({p: sha(Path(__file__).parent/p) for p in dependencies})
    report = {"kind": "actual_grounded_canonical_root_finite_jets", "proved": False,
              "source_sha256": sha(__file__), "dependency_sha256": adapter_dependencies,
              "parameter_adapter_source_sha256": adapter_source,
              "root_certificate_path": str(args.root_certificate), "root_certificate_sha256": sha(args.root_certificate),
              **adapter_identity, "root": ball_record(model.root),
              "common_scalar_spans": model.spans, "nodes": args.nodes, "canonical_angle_order": args.order,
              "bits": args.bits, "radial_scale": "1/1024",
              "primitive_infinite_error": ball_record(model.budget["field_errors"][0]),
              "E_infinite_error": ball_record(model.budget["E_error"]),
              "kappa_root": ball_record(model.kappa[0].real), "cells": [],
              "initial_angle_cells": args.cells, "maximum_bisection_depth": args.max_depth,
              "positive_factor_relative_radius_gate": "1/4",
              "failed_cells": []}
    def save():
        args.out.parent.mkdir(parents=True, exist_ok=True)
        temporary = args.out.with_suffix(args.out.suffix+".tmp")
        opener = gzip.open if str(args.out).endswith(".gz") else open
        with opener(temporary, "wt") as stream:
            json.dump(report, stream, indent=2)
            stream.write("\n")
        temporary.replace(args.out)
    last = args.cells if args.last_cell is None else args.last_cell
    if args.point is not None:
        angle = exact_arb(Fraction(args.point))*arb.pi()
        report["cells"].append(model.evaluate(angle))
        report["scope"] = "one exact angle only; not a full-angle certificate"
    else:
        if not 0 <= args.first_cell < last <= args.cells:
            raise ValueError("invalid angular cell interval")
        queue = deque((Fraction(j, args.cells), Fraction(j+1, args.cells), 0)
                      for j in range(args.first_cell, last))
        attempts = 0
        while queue:
            left, right, depth = queue.popleft()
            attempts += 1
            angle = (exact_arb((left+right)/4)+arb(0, exact_arb((right-left)/4)))*arb.pi()
            try:
                row = model.evaluate(angle)
                row["exact_quarter_interval"] = [str(left), str(right)]
                row["bisection_depth"] = depth
                report["cells"].append(row)
            except (ValueError, ZeroDivisionError) as exc:
                if depth < args.max_depth:
                    middle = (left+right)/2
                    queue.appendleft((middle, right, depth+1))
                    queue.appendleft((left, middle, depth+1))
                else:
                    report["failed_cells"].append({"interval": [str(left), str(right)], "reason": str(exc)})
            report["seconds"] = time.monotonic()-started
            report["attempts"] = attempts
            report["pending"] = [[str(a), str(b), d] for a, b, d in queue]
            if attempts % 128 == 0:
                save()
                print(json.dumps({"cells": len(report["cells"]), "attempts": attempts,
                                  "pending": len(queue), "failed": len(report["failed_cells"]),
                                  "seconds": report["seconds"]}), flush=True)
        report["cells"].sort(key=lambda row: Fraction(row["exact_quarter_interval"][0]))
        cursor = Fraction(args.first_cell, args.cells)
        for row in report["cells"]:
            left, right = map(Fraction, row["exact_quarter_interval"])
            if left != cursor:
                raise ValueError("directed root jet cover has a gap or overlap")
            cursor = right
        report["proved"] = (args.first_cell == 0 and last == args.cells
                            and cursor == 1 and not report["failed_cells"])
        report["scope"] = "all physical theta by exact D4 quarter-period and continuous interval cells" if report["proved"] else "partial exact angular cell range"
        if report["proved"]:
            upper = lambda record: arb(record["upper"]).upper()
            lower = lambda record: arb(record["lower"]).lower()
            norm = lambda record: max(abs(lower(record)), abs(upper(record)))
            report["uniform_bounds"] = {}
            for name in ("V_root", "V_xi_root", "root_momentum_shear", "physical_height",
                         "source_root_factor", "grounded_flux_root_factor"):
                key = name+"_canonical_angle_derivatives"
                report["uniform_bounds"][key] = [ball_record(max(norm(row[key][j]) for row in report["cells"]))
                                                          for j in range(args.order+1)]
            for name in ("alpha", "B", "Y_prime", "t0", "physical_Fz", "D", "W"):
                report["uniform_bounds"][name] = {
                    "lower": ball_record(min(lower(row[name]) for row in report["cells"])),
                    "upper": ball_record(max(upper(row[name]) for row in report["cells"]))}
            means = [arb(0), arb(0)]
            for row in report["cells"]:
                a, b = map(Fraction, row["exact_quarter_interval"])
                means[0] += exact_arb(b-a)*lower(row["Y_prime"])
                means[1] += exact_arb(b-a)*upper(row["Y_prime"])
            report["canonical_circumference"] = {
                "lower": ball_record((2*arb.pi()*means[0]).lower()),
                "upper": ball_record((2*arb.pi()*means[1]).upper())}
            report["canonical_full_circle_frequency"] = {
                "lower": ball_record((1/means[1]).lower()), "upper": ball_record((1/means[0]).upper())}
    report["seconds"] = time.monotonic()-started
    save()
    print(json.dumps({"proved": report["proved"], "cells": len(report["cells"]), "seconds": report["seconds"]}), flush=True)


if __name__ == "__main__":
    main()
