#!/usr/bin/env python3
"""Actual beta bulk integral, split at every exact positive/negative knot."""
from __future__ import annotations
import argparse
from bisect import bisect_right
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import time
import numpy as np
from flint import arb, acb, acb_series, ctx
from fourfold_phase_beta_interval import (BallTarget, ball_record, series_constant,
    array_derivative, vector_dot, vector_cross, primitive_fourier_budget)


def exact_arb(value):
    q = Fraction(value)
    return arb(q.numerator)/q.denominator


def real_interval(left, right):
    return exact_arb(left).union(exact_arb(right))


def complex_pad(value, fee):
    error = arb(0, arb(fee).upper())
    return acb(value)+acb(error, error)


def ordinary_dot(left, right):
    return sum((left[j]*right[j] for j in range(3)), acb(0))


class BulkTarget(BallTarget):
    def __init__(self, snapshot, nodes, angles, tail_radius, E_radius, tail_sigma):
        super().__init__(snapshot, nodes, angles)
        self.tail_radius, self.E_radius, self.tail_sigma = tail_radius, E_radius, tail_sigma
        self.cell, self.span_cache = None, {}
        self.evaluations, self.failed_analytic_evaluations = 0, 0

    def set_cell(self, left, right):
        left, right = Fraction(left), Fraction(right)
        if not left < right:
            raise ValueError("nonpositive exact knot cell")
        self.cell = left, right

    def explicit_germ(self, spline, center, direction, side=1):
        if self.cell is None:
            raise ValueError("fix an exact physical knot cell first")
        left, right = self.cell
        if side == -1:
            left, right = -right, -left
        midpoint = (left+right)/2
        knots = [Fraction.from_float(float(x)) for x in spline.knots_float]
        span = bisect_right(knots, midpoint)-1
        if not knots[span] <= left < right <= knots[span+1]:
            raise ValueError("physical cell crosses an exact scalar span")
        key = id(spline), span, ctx.prec
        if key not in self.span_cache:
            # A fixed exact midpoint of this scalar span permits cache reuse
            # even when another spline splits it into many tiny common cells.
            anchor = exact_arb((knots[span]+knots[span+1])/2)
            old_cap, ctx.cap = ctx.cap, max(ctx.cap, spline.degree+1)
            x = acb_series([acb(anchor), 1])
            shape = spline.coefficients.shape[1:]
            polynomials = np.empty(shape, object)
            for index in np.ndindex(shape):
                work = [series_constant(spline.coefficients[(span-spline.degree+j,)+index])
                        for j in range(spline.degree+1)]
                for level in range(1, spline.degree+1):
                    for j in range(spline.degree, level-1, -1):
                        kk = span-spline.degree+j
                        weight = (x-spline.knots[kk])/(spline.knots[kk+spline.degree-level+1]-spline.knots[kk])
                        work[j] = (1-weight)*work[j-1]+weight*work[j]
                polynomials[index] = [work[spline.degree][n] for n in range(spline.degree+1)]
            ctx.cap = old_cap
            self.span_cache[key] = anchor, polynomials
        anchor, polynomials = self.span_cache[key]
        delta = acb_series([side*acb(center)-anchor, side*acb(direction)])
        out = np.empty(polynomials.shape, object)
        for index in np.ndindex(polynomials.shape):
            coefficients = polynomials[index]
            value = series_constant(coefficients[-1])
            for coefficient in coefficients[-2::-1]:
                value = coefficient+delta*value
            out[index] = value
        return out.item() if not out.shape else out

    def scalars(self, center, direction):
        plus = lambda sp: self.explicit_germ(sp, center, direction, 1)
        minus = lambda sp: self.explicit_germ(sp, center, direction, -1)
        bp, bm, pp, pm = plus(self.base), minus(self.base), plus(self.raw), minus(self.raw)
        beta, gamma = np.empty(self.modes, object), np.empty(self.modes, object)
        for j in range(self.modes):
            beta[j] = (pp[j, 0]*bp**3+pm[j, 0]*bm**3)/2
            gamma[j] = (pp[j, 1]*bp**2-pm[j, 1]*bm**2)/2
        radius = (bp+bm+plus(self.shift)+minus(self.shift))/2
        for alpha, sp in zip(self.alpha, self.means):
            radius += alpha*(plus(sp)+minus(sp))/2
        height = series_constant(0)
        for alpha, sp in zip([arb(1)]+self.alpha, self.height_integrals):
            height += alpha*(plus(sp)-minus(sp))/2
        return beta, gamma, radius, height

    def complete_data(self, radial):
        budget = self.analytic_input_budget(radial, self.tail_radius, self.tail_sigma, self.E_radius)
        budget["real_input"] = radial.imag == 0
        coefficient, radius = self.primitive(radial, 1)
        first = array_derivative(coefficient)
        E = sum((vector_dot(first[k], first[(-k) % self.nodes]) for k in range(self.nodes)), series_constant(0))
        E = acb_series([complex_pad(E[n], budget["E_error"]/self.E_radius**n)
                        for n in range(E.prec)], prec=E.prec)
        ar, arr, Er = radius.derivative(), radius.derivative().derivative(), E.derivative()
        K = (ar*Er-2*arr*E)/(2*radius*E**2)
        K0, Kp = K[0], K[1]
        if budget["real_input"]:
            K0, Kp = acb(K0.real), acb(Kp.real)
        return coefficient, K0, Kp, budget

    def physical_fields(self, coefficient, budget, angular_sigma=None):
        width = None if angular_sigma is None else angular_sigma+arb.pi()/self.angles
        errors = budget["field_errors"]
        if width is not None:
            errors, _ = primitive_fourier_budget(self.nodes, self.tail_sigma, width, self.tail_radius,
                budget["radius_bound"], budget["height_bound"], budget["tangent_bound"])
        sources = [coefficient, self.angular(coefficient), self.angular(coefficient, 2)]
        fields = {}
        for ar, at in ((0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (0, 2)):
            values = np.empty(sources[at].shape, object)
            for key in np.ndindex(values.shape):
                values[key] = math.factorial(ar)*sources[at][key][ar]
            base_fee = math.factorial(ar)*errors[at]/self.tail_radius**ar
            real_fee, imaginary_fee = [base_fee]*3, [base_fee]*3
            if width is not None:
                if not budget["real_input"]:
                    raise ValueError("angular domain cover requires real radial interval")
                for k in range(self.nodes):
                    mode = abs(k if k < self.nodes//2 else k-self.nodes)
                    re = mode*arb.pi()/self.angles+(mode*angular_sigma).cosh()-1
                    im = (mode*angular_sigma).sinh()
                    for j in range(3):
                        real_fee[j] += abs(values[k, j])*re
                        imaginary_fee[j] += abs(values[k, j])*im
            padded = np.empty((self.angles, 3), object)
            padded.fill(acb(0))
            for k in range(self.nodes):
                signed = k if k < self.nodes//2 else k-self.nodes
                padded[signed % self.angles] = values[k]
            samples = self.fourier.fft(padded, inverse=True)*self.angles
            for key in np.ndindex(samples.shape):
                if width is not None:
                    samples[key] = acb(samples[key].real+arb(0, real_fee[key[1]].upper()),
                                       arb(0, imaginary_fee[key[1]].upper()))
                elif budget["real_input"]:
                    samples[key] = acb(samples[key].real+arb(0, base_fee.upper()))
                else:
                    samples[key] = complex_pad(samples[key], base_fee)
            fields[(ar, at)] = samples
        return fields

    def density_values(self, radial, analytic=False, angular_sigma=None, waist=False):
        self.evaluations += 1
        coefficient, K, Kp, budget = self.complete_data(radial)
        if not (-K).real > 0:
            raise ValueError("negative target curvature gate failed")
        kappa = (-K).sqrt(analytic=True)
        fields = self.physical_fields(coefficient, budget, angular_sigma)
        F, X, Frr, Y, Frt, Ftt = [fields[key] for key in
            ((0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (0, 2))]
        result = []
        for j in range(self.angles):
            normal = vector_cross(Y[j], X[j])
            nr1, nr2 = vector_cross(Frt[j], X[j]), vector_cross(Y[j], Frr[j])
            nt1, nt2 = vector_cross(Ftt[j], X[j]), vector_cross(Y[j], Frt[j])
            nr, nt = [nr1[k]+nr2[k] for k in range(3)], [nt1[k]+nt2[k] for k in range(3)]
            area2, radius2, support = ordinary_dot(normal, normal), ordinary_dot(F[j], F[j]), ordinary_dot(normal, F[j])
            if any(not z.real > 0 for z in (area2, radius2, support)):
                raise ValueError("area/radius/support denominator gate failed")
            l, m, n = [ordinary_dot(normal, w[j]) for w in (Frr, Frt, Ftt)]
            a, b, c = -n/area2, m/area2, -l/area2
            if not a.real > 0:
                raise ValueError("actual zeta^2 a denominator gate failed")
            omega, chat = ((l*n-m*m)/area2**2-K)/a, (b*b+K)/a
            FX, FY = ordinary_dot(F[j], X[j]), ordinary_dot(F[j], Y[j])
            d = (a*(ordinary_dot(X[j], X[j])-FX*FX/radius2)
                 +2*b*(ordinary_dot(X[j], Y[j])-FX*FY/radius2)
                 +c*(ordinary_dot(Y[j], Y[j])-FY*FY/radius2))/radius2
            lzr = ordinary_dot(nr, F[j])/support-ordinary_dot(normal, nr)/area2-FX/radius2
            lzt = ordinary_dot(nt, F[j])/support-ordinary_dot(normal, nt)/area2-FY/radius2
            fr, ft = Kp/(2*K)-2*lzr, -2*lzt
            if waist:
                if not X[j, 2].real > 0:
                    raise ValueError("waist Fz/r derivative lower bound failed")
                ell = Frt[j, 2]/X[j, 2]-FY/radius2
            else:
                if not F[j, 2].real > 0:
                    raise ValueError("actual Fz denominator gate failed")
                ell = Y[j, 2]/F[j, 2]-FY/radius2
            value = (d+omega*(ell*ell+ell*ft)-(a*fr*fr+2*b*fr*ft+chat*ft*ft)/4)/kappa
            if not value.is_finite():
                raise ValueError("nonfinite actual density")
            result.append(value)
        return result

    def mean_callback(self, radial, analytic):
        try:
            return sum(self.density_values(radial, analytic), acb(0))/self.angles
        except (ValueError, ZeroDivisionError, OverflowError):
            self.failed_analytic_evaluations += 1
            return acb("nan")

    def angular_domain(self, left, right, sigma, waist=False):
        values = self.density_values(acb(real_interval(left, right)), True, sigma, waist)
        bound = max(abs(value).upper() for value in values)
        error = 2*bound*(-sigma*self.angles).exp()/(1-(-sigma*self.angles).exp())
        return bound, error.upper()

    def waist_cap(self, width):
        self.set_cell(Fraction(0), width)
        values = self.density_values(acb(real_interval(0, width)), angular_sigma=arb(0), waist=True)
        bound = max(abs(value).upper() for value in values)
        return arb(0, (exact_arb(width)*bound).upper()), bound


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--frozen-inputs", type=Path, required=True)
    ap.add_argument("--fixed-cut", default="1072423152036779/4503599627370496")
    ap.add_argument("--waist-width", default="1/1048576")
    ap.add_argument("--bits", type=int, default=128)
    ap.add_argument("--quarter-nodes", type=int, default=256)
    ap.add_argument("--angles", type=int, default=1024)
    ap.add_argument("--sigma", default=".02")
    ap.add_argument("--tail-radius", default=".003")
    ap.add_argument("--E-radius", default=".0025")
    ap.add_argument("--tail-sigma", default=".32")
    ap.add_argument("--absolute-tolerance", default=".0002")
    ap.add_argument("--eval-limit", type=int, default=64)
    ap.add_argument("--cell-depth", type=int, default=18)
    ap.add_argument("--engine", choices=("arb", "box"), default="box")
    ap.add_argument("--start-cell", type=int, default=0)
    ap.add_argument("--max-cells", type=int)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    ctx.prec, ctx.cap = args.bits, 4
    target_class = BulkTarget
    if args.engine == "box":
        from fourfold_phase_beta_bulk_box import FastBulkTarget
        target_class = FastBulkTarget
    target = target_class(args.frozen_inputs, args.quarter_nodes, args.angles,
                          arb(args.tail_radius), arb(args.E_radius), arb(args.tail_sigma))
    cut, waist = Fraction(args.fixed_cut), Fraction(args.waist_width)
    knots = {Fraction(0), cut}
    for key, values in target.frozen.items():
        if key.endswith("_knots"):
            for value in values:
                q = abs(Fraction.from_float(float(value)))
                if 0 < q < cut:
                    knots.add(q)
    if not 0 < waist < sorted(knots)[1]:
        raise ValueError("waist cap does not stay within the first common scalar span")
    knots.add(waist)
    points = sorted(knots)
    cells = [(a, b) for a, b in zip(points, points[1:]) if a >= waist]
    report = {"kind": "directed_phase_bulk_integral", "complete": False,
        "input_sha256": hashlib.sha256(args.frozen_inputs.read_bytes()).hexdigest(),
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "native_source_sha256": hashlib.sha256(Path(__file__).with_name("fourfold_phase_beta_interval.py").read_bytes()).hexdigest(),
        "fixed_cut": str(cut), "waist_width": str(waist), "bits": args.bits, "quarter_nodes": args.quarter_nodes,
        "angles": args.angles, "sigma": args.sigma, "engine": args.engine, "radial_cells_total": len(cells),
        "per_original_cell_tolerance": args.absolute_tolerance, "accepted_cells": [], "failed_cells": [],
        "start_cell": args.start_cell, "subdivision_count": 0,
        "limitations": ["Partial covers are not complete bulk or beta certificates", "No full PDE network or exact nonlinear family is asserted"]}
    if args.engine == "box":
        report["box_source_sha256"] = hashlib.sha256(Path(__file__).with_name("fourfold_phase_beta_bulk_box.py").read_bytes()).hexdigest()
    started = time.monotonic()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    def save():
        report["wall_seconds"] = time.monotonic()-started
        report["callback_evaluations"] = target.evaluations
        report["failed_analytic_evaluations"] = target.failed_analytic_evaluations
        args.out.write_text(json.dumps(report, indent=2)+"\n")
    if args.start_cell == 0:
        cap, bound = target.waist_cap(waist)
        report["waist_integral"], report["waist_density_bound"] = ball_record(cap), ball_record(bound)
        save()
        print(json.dumps({"stage": "waist", "integral": cap.str(16)}), flush=True)
    sigma, tolerance = arb(args.sigma), arb(args.absolute_tolerance)
    stop = len(cells) if args.max_cells is None else min(len(cells), args.start_cell+args.max_cells)
    for index in range(args.start_cell, stop):
        base_left, base_right = cells[index]
        target.set_cell(base_left, base_right)
        pending = [(base_left, base_right, 0)]
        while pending:
            left, right, depth = pending.pop()
            before = target.evaluations
            length = exact_arb(right-left)
            local_tolerance = tolerance*length/exact_arb(base_right-base_left)
            try:
                bound, angular = target.angular_domain(left, right, sigma)
                if not length*angular < local_tolerance/2:
                    raise ValueError("complete angular fee exceeds its cell budget")
                whole = target.mean_callback(acb(real_interval(left, right)), False)
                direct = whole.real*length+arb(0, (length*angular).upper())
                if direct.is_finite() and direct.rad() < local_tolerance:
                    value, method = direct, "continuous_interval_range"
                else:
                    integral = acb.integral(target.mean_callback, acb(exact_arb(left)), acb(exact_arb(right)),
                        abs_tol=local_tolerance/2, rel_tol=arb("1e-10"), eval_limit=args.eval_limit,
                        deg_limit=32, depth_limit=20)
                    if not integral.is_finite() or not integral.real.rad() < local_tolerance/2:
                        raise ValueError("validated complex quadrature did not meet cell budget")
                    value, method = integral.real+arb(0, (length*angular).upper()), "Arb_validated_complex_integration"
                report["accepted_cells"].append({"index": index, "left": str(left), "right": str(right),
                    "depth": depth, "integral": ball_record(value), "method": method,
                    "complex_angle_density_bound": ball_record(bound),
                    "angular_integral_error": ball_record((length*angular).upper()),
                    "evaluations": target.evaluations-before})
                print(json.dumps({"stage": "cell", "index": index, "depth": depth,
                                  "integral": value.str(16), "evaluations": target.evaluations-before}), flush=True)
            except Exception as exc:
                if depth < args.cell_depth:
                    mid = (left+right)/2
                    pending.extend([(mid, right, depth+1), (left, mid, depth+1)])
                    report["subdivision_count"] += 1
                    report["latest_subdivision"] = {"index": index, "left": str(left), "right": str(right), "reason": repr(exc)}
                else:
                    report["failed_cells"].append({"index": index, "left": str(left), "right": str(right), "error": repr(exc)})
            save()
    total = sum((arb(row["integral"]["ball"]) for row in report["accepted_cells"]), arb(0))
    if "waist_integral" in report:
        total += arb(report["waist_integral"]["ball"])
    report["enclosed_integral_over_recorded_cover"] = ball_record(total)
    report["complete"] = args.start_cell == 0 and stop == len(cells) and not report["failed_cells"] and "waist_integral" in report
    save()


if __name__ == "__main__":
    main()
