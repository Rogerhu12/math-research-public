#!/usr/bin/env python3
"""R111: true whole-parameter finite-cap form comparison.

The body uses a genuine complex-parameter Cauchy disk and complete infinite
primitive enclosures. The graft uses the full real Wiener enclosure. Nothing
in this file deletes complex parameter parts merely because r is real.
A complete requested subrange is not declared a complete cap. Native
execution and its output are required before any numerical bound is usable.
"""
from __future__ import annotations

import argparse
from bisect import bisect_right
from fractions import Fraction
import gzip
import json
import math
from pathlib import Path
import time

import numpy as np
from flint import arb, acb, ctx

from fourfold_phase_beta_affine import load_definition
from fourfold_phase_beta_parameter_germ import ParameterGermMixin
from fourfold_phase_beta_bulk_interval import BulkTarget, exact_arb, real_interval
from fourfold_phase_beta_bulk_box import (
    CBox, Box, cstack, zeros, cdot, arb_box, reduce_box, stack, complex_sincos)
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_uniform_tail import up
from fourfold_phase_cap_scaled_body import (
    ScaledBodyForm, common_cells, poly_eval, poly_derivative,
    poly_multiply, poly_subtract, magnitude)
from fourfold_phase_cap_energy_interval import sha
from fourfold_phase_natural_exterior_graft import NaturalGraft
from fourfold_phase_cap_wiener_box import real_wiener_form, real_part


def save(path, report):
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(report, indent=2)+"\n").encode()
    if path.suffix == ".gz":
        raw = gzip.compress(raw, mtime=0)
    temporary = path.with_suffix(path.suffix+".tmp")
    temporary.write_bytes(raw)
    temporary.replace(path)


def require_nonzero(value, name):
    """Each complex rectangle must exclude zero; returns a directed lower bound."""
    if not np.all(np.isfinite(value.magnitude_upper())):
        raise ValueError("nonfinite actual "+name)
    def distance(interval):
        return np.where(interval.lo > 0, interval.lo,
                        np.where(interval.hi < 0, -interval.hi, 0.))
    lower = np.maximum(distance(value.real), distance(value.imag))
    if not np.all(lower > 0):
        raise ValueError("actual complex parameter chart has unresolved "+name)
    return arb(float(np.min(lower)))


class ParameterDiskBody(ScaledBodyForm):
    direction_scalars = ParameterGermMixin.direction_scalars

    def __init__(self, object_path, disk_radius, complex_disk, nodes, angles):
        self.disk_radius = Fraction(disk_radius)
        r = exact_arb(self.disk_radius)
        self.offset = acb(arb(0, r), arb(0, r)) if complex_disk else acb(0)
        self.real_parameter = not complex_disk
        super().__init__(object_path, nodes, angles,
                         arb(".003"), arb(".0025"), arb(".32"))
        definition, _, direction, center = load_definition(object_path)
        ParameterGermMixin.initialize_parameter(
            self, object_path, self.disk_radius, definition, direction, center)

    def scalars(self, center, direction):
        # Parent already contains the EXACT affine center. Add only offset,
        # not a second copy of the center parameter.
        original = super().scalars(center, direction)
        derivative = self.direction_scalars(center, direction)
        answer = []
        for value, change in zip(original, derivative):
            if isinstance(value, np.ndarray):
                row = np.empty(value.shape, object)
                for index in np.ndindex(value.shape):
                    row[index] = value[index]+self.offset*change[index]
                answer.append(row)
            else:
                answer.append(value+self.offset*change)
        return tuple(answer)

    def set_cell(self, left, right):
        cell = Fraction(left), Fraction(right)
        if self.cell == cell and hasattr(self, "ratio_polynomials"):
            return
        self.fast_cell_cache.clear()
        self.span_cache.clear()
        BulkTarget.set_cell(self, *cell)
        anchor = exact_arb((cell[0]+cell[1])/2)
        old_cap, ctx.cap = ctx.cap, 21
        try:
            scalar = self.scalars(acb(anchor), 1)
            parts = []
            for group in scalar:
                if isinstance(group, np.ndarray):
                    array = group
                else:
                    array = np.empty((), object)
                    array[()] = group
                shape = (21,)+array.shape
                rl, rh, il, ih = [np.zeros(shape) for _ in range(4)]
                for index in np.ndindex(array.shape):
                    for n in range(21):
                        z = array[index][n]
                        re, im = arb_box(z.real), arb_box(z.imag)
                        rl[(n,)+index], rh[(n,)+index] = re.lo, re.hi
                        il[(n,)+index], ih[(n,)+index] = im.lo, im.hi
                parts.append(CBox(Box(rl.reshape(21, -1), rh.reshape(21, -1)),
                                  Box(il.reshape(21, -1), ih.reshape(21, -1))))
            self.anchor = anchor
            self.scalar_poly = CBox(
                Box(np.concatenate([v.real.lo for v in parts], 1),
                    np.concatenate([v.real.hi for v in parts], 1)),
                Box(np.concatenate([v.imag.lo for v in parts], 1),
                    np.concatenate([v.imag.hi for v in parts], 1)))
        finally:
            ctx.cap = old_cap
        self.scalar_abs = self.scalar_poly.magnitude_upper()
        a, z = self.scalar_poly[:, -2], self.scalar_poly[:, -1]
        require_nonzero(a[0], "radius at scalar anchor")
        ar, zr = poly_derivative(a), poly_derivative(z)
        arr, zrr = poly_derivative(ar), poly_derivative(zr)
        aa = poly_multiply(a, a)
        l0 = float((ar[0]/a[0]).to_acb().real.mid())
        c0 = float((zr[0]/(a[0]*a[0])).to_acb().real.mid())
        if not math.isfinite(l0) or not math.isfinite(c0):
            raise ValueError("no finite exact dyadic ratio reorganizer")
        self.ratio_polynomials = dict(
            L0=l0, C0=c0,
            L_remainder=poly_subtract(ar, l0*a),
            C_remainder=poly_subtract(zr, c0*aa),
            Lprime_numerator=poly_subtract(poly_multiply(a, arr), poly_multiply(ar, ar)),
            Cprime_numerator=poly_subtract(poly_multiply(a, zrr), 2*poly_multiply(ar, zr)))

    def normalized_data(self, radial):
        primitive, radius = self.unit_finite_data(radial)
        amin = require_nonzero(radius[0], "radius")
        errors = self.unit_tail_errors(radial)
        L, Lp, C, Cp, ia = self.scalar_ratios(radial, radius)
        reverse = (-np.arange(self.nodes)) % self.nodes
        u = L*primitive[0]+primitive[1]
        ur = Lp*primitive[0]+L*primitive[1]+primitive[2]
        ebar = 2*L*u[0, 0]+cdot(u, u[reverse]).sum()
        ebar_r = 2*Lp*u[0, 0]+2*L*ur[0, 0]+2*cdot(u, ur[reverse]).sum()
        eps = [arb_box(math.factorial(j)*errors[0]/self.tail_radius**j) for j in range(3)]
        Labs, Lpabs = magnitude(L), magnitude(Lp)
        eu = Labs*eps[0]+eps[1]
        eur = Lpabs*eps[0]+Labs*eps[1]+eps[2]
        Mu = Box(np.max(reduce_box(Box(u.magnitude_upper())).hi))
        Mur = Box(np.max(reduce_box(Box(ur.magnitude_upper())).hi))
        fee0 = 2*Labs*eu+3*(2*Mu*eu+eu*eu)
        fee1 = 2*Lpabs*eu+2*Labs*eur+6*(Mu*eur+Mur*eu+eu*eur)
        real = self.real_parameter and radial.imag == 0
        ebar, ebar_r = ebar.pad(fee0, real), ebar_r.pad(fee1, real)
        a = radius[0]
        Ebar = L*L+a*a*C*C+ebar
        emin = require_nonzero(Ebar, "E/radius^2")
        K = (C*C*(L*L-Lp)+L*C*Cp
             +(L*ebar_r-2*Lp*ebar)*ia*ia/2)/(Ebar*Ebar)
        if real:
            K = CBox(K.real)
        if not np.all(np.isfinite(K.magnitude_upper())):
            raise ValueError("nonfinite complete true target curvature")
        self.chart_minima = dict(radius=ball_record(amin), Ebar=ball_record(emin))
        return primitive, K, errors, real, (L, Lp, C, Cp, ia)

    def unit_fields(self, radial, coefficient, errors, real, sigma=None):
        if sigma is None or not sigma == 0:
            raise ValueError("this parameter proof requires a complete REAL angular cover")
        gap = arb.pi()/self.angles
        errors = self.unit_tail_errors(radial, gap)
        mode = np.abs(np.asarray(self.frequency)//4)
        variation = stack([arb_box(int(k)*gap) for k in mode]).reshape(-1, 1)
        fields = []
        for j in range(2):
            values = coefficient[j]
            fee = arb_box(math.factorial(j)*errors[0]/self.tail_radius**j)
            data = zeros((self.angles, 3))
            data[(np.asarray(self.frequency)//4) % self.angles] = values
            samples = (self.fast_fourier.fft(data, inverse=True)*self.angles)[:self.sample_count]
            total = fee+reduce_box(Box(values.magnitude_upper())*variation)
            # A complex parameter gives genuinely complex samples. Preserve
            # their imaginary centers, including the complete angular fee.
            fields.append(samples.pad(total, real))
        key = sigma.str(35)
        if key not in self.angle_shift_cache:
            delta = CBox(Box(-arb_box(gap).hi, arb_box(gap).hi))
            s, c = complex_sincos(CBox(np.arange(1, self.modes+1))*delta)
            s, c = s.reshape(-1, 1), c.reshape(-1, 1)
            ss, cc = self.angle_sines, self.angle_cosines
            self.angle_shift_cache[key] = ss*c+cc*s, cc*c-ss*s
        return fields

    def akb(self, left, right):
        p = self.form_parts(acb(real_interval(left, right)), arb(0))
        D, M, W, H, Z, K = [p[k] for k in ("D", "M", "W", "H", "Z", "K")]
        dmin, hmin = require_nonzero(D, "D/radius^2"), require_nonzero(H, "H/radius")
        alpha = Z*Z*D/(H*H)
        drift = -M/D
        kappa = Z*Z*W*W*K/(D*H*H)
        for value in (alpha, drift, kappa):
            if not np.all(np.isfinite(value.magnitude_upper())):
                raise ValueError("nonfinite actual grounded form")
        if p["real"]:
            alpha, drift, kappa = [CBox(v.real) for v in (alpha, drift, kappa)]
            if not np.all(alpha.real.lo > 0) or not np.all(kappa.real.lo > 0):
                raise ValueError("real center form positivity unresolved")
        self.chart_minima.update(D2=ball_record(dmin), H1=ball_record(hmin))
        return alpha, kappa, drift


def body_comparison(center, disk, left, right, eta, radius):
    a0, k0, b0 = center.akb(left, right)
    A = (a0.real.lo+a0.real.hi)/2
    K = (k0.real.lo+k0.real.hi)/2
    B = (b0.real.lo+b0.real.hi)/2
    if not np.all(np.isfinite(A+K+B)) or not np.all(A > 0) or not np.all(K > 0):
        raise ValueError("positive finite dyadic normalization not selected")
    sA = stack([arb_box(arb(float(x)).sqrt()) for x in A])
    sK = stack([arb_box(arb(float(x)).sqrt()) for x in K])
    afloor = arb(float(np.min((a0.real/Box(A)).lo)))
    kfloor = arb(float(np.min((k0.real/Box(K)).lo)))
    drift = Box((b0-CBox(B)).magnitude_upper())*sA/sK
    t = arb(float(np.max(drift.hi)))
    m = (min(afloor, kfloor)/(1+t)**2).lower()
    if not m > 0:
        raise ValueError("normalized real center coercivity unresolved")
    a, k, b = disk.akb(left, right)
    db = b-CBox(B)
    c11 = a/CBox(A)
    c12 = a*db/CBox(sA*sK)
    c22 = k/CBox(K)+a*db*db/CBox(K)
    rows = np.maximum(up(c11.magnitude_upper()+c12.magnitude_upper()),
                      up(c12.magnitude_upper()+c22.magnitude_upper()))
    M = arb(float(np.max(rows)))
    epsilon = (M/m*exact_arb(eta)/exact_arb(radius-eta)).upper()
    if not epsilon.is_finite():
        raise ValueError("nonfinite whole-parameter Cauchy fee")
    return dict(relative_form_error=ball_record(epsilon),
                normalized_center_coercivity=ball_record(m),
                complex_parameter_form_modulus=ball_record(M),
                center_drift_normalization=ball_record(t),
                complex_chart_minima=disk.chart_minima)


class WholeFamilyGraft(NaturalGraft):
    def whole_angle_values(self, left, right):
        jets = self.jets(left-3, right-3)
        a = real_part(jets["radius"][0])
        L = real_part(jets["log_radius"][1])
        Lp = 2*real_part(jets["log_radius"][2])
        C = real_part(jets["slope_ratio"][0])
        Cp = real_part(jets["slope_ratio"][1])
        beta = [[math.factorial(j)*real_part(v[j]) for v in jets["beta"]] for j in range(3)]
        gamma = [[math.factorial(j)*real_part(v[j]) for v in jets["gamma"]] for j in range(3)]
        return real_wiener_form(a, self.Z_global, L, Lp, C, Cp, beta, gamma)


def graft_comparison(graft, left, right):
    values, _ = graft.whole_angle_values(left, right)
    u, v, w = values[:3]
    A = arb(float(u.mid()))
    b = arb(float((v/A).mid()))
    K = arb(float((w-A*b*b).mid()))
    if not A > 0 or not K > 0:
        raise ValueError("graft dyadic reference not positive")
    e11 = u/A-1
    e12 = (v-b*u)/(A*K).sqrt()
    e22 = (w-2*b*v+b*b*u)/K-1
    t = max((abs(e11)+abs(e12)).upper(), (abs(e12)+abs(e22)).upper())
    if not t < 1:
        raise ValueError("whole-family graft reference variation reaches one")
    epsilon = (2*t/(1-t)).upper()
    return dict(relative_form_error=ball_record(epsilon),
                full_family_reference_relative_radius=ball_record(t),
                exact_reference_A=ball_record(A),
                exact_reference_drift=ball_record(b),
                exact_reference_K=ball_record(K),
                full_angle_form_boxes=list(map(ball_record, values[:3])))


def cover_complete(rows, left, right):
    cursor = left
    for row in sorted(rows, key=lambda x: Fraction(x["radial_interval"][0])):
        a, b = map(Fraction, row["radial_interval"])
        if a != cursor or not a < b:
            return False
        cursor = b
    return cursor == right


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--object", type=Path, default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json"))
    p.add_argument("--half-width", type=Fraction, default=Fraction(1, 10**9))
    p.add_argument("--parameter-radius", type=Fraction, default=Fraction(1, 10000))
    p.add_argument("--relative-target", type=Fraction, default=Fraction(1, 500))
    p.add_argument("--part", choices=("body", "graft", "both"), default="both")
    p.add_argument("--body-left", type=Fraction, default=Fraction(1, 4))
    p.add_argument("--body-right", type=Fraction, default=Fraction(3))
    p.add_argument("--primitive-nodes", type=int, default=512)
    p.add_argument("--angles", type=int, default=1024)
    p.add_argument("--graft-certificate", type=Path, default=Path(
        "notes/2026-11-12-R111-actual-whole-family-graft.json"))
    p.add_argument("--compute-graft", action="store_true",
                   help="compute a new native graft cover instead of consuming the paid exact certificate")
    p.add_argument("--max-depth", type=int, default=14)
    p.add_argument("--bits", type=int, default=192)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    if not 0 < args.half_width < args.parameter_radius or not 0 < args.relative_target < 1:
        raise ValueError("positive eta<parameter-radius and target<1 required")
    if not Fraction(1, 4) <= args.body_left < args.body_right <= 3:
        raise ValueError("the requested body range must lie in [1/4,3]")
    if args.angles < args.primitive_nodes or args.angles & (args.angles-1):
        raise ValueError("angular FFT must be power of two and retain every primitive mode")
    ctx.prec, ctx.cap = args.bits, 8
    started, cpu = time.monotonic(), time.process_time()
    definition, _, _, delta = load_definition(args.object)
    rows, failed, rejected = [], [], []
    report = dict(
        kind="actual_full_parameter_finite_cap_relative_form",
        complete=False, cap_form_comparison_complete=False,
        full_PDE_inverse_complete=False, nonlinear_family_complete=False,
        source_sha256=sha(__file__), object_path=str(args.object),
        object_sha256=sha(args.object),
        origin_sha256=definition["origin_inputs"]["sha256"],
        direction_sha256=definition["direction"]["sha256"],
        exact_center=str(delta), exact_half_width=str(args.half_width),
        exact_parameter_interval=[str(delta-args.half_width), str(delta+args.half_width)],
        complex_offset_disk_radius=str(args.parameter_radius),
        enclosing_complex_offset_square="[-rho,rho]+i[-rho,rho]",
        relative_error_target=str(args.relative_target), requested_part=args.part,
        requested_body_interval=[str(args.body_left), str(args.body_right)],
        primitive_nodes=args.primitive_nodes, angular_nodes=args.angles, bits=args.bits,
        intervals=rows, unresolved_intervals=failed, rejected_parent_boxes=rejected,
        dependency_sha256={n: sha(Path(__file__).with_name(n)) for n in (
            "fourfold_phase_beta_affine.py", "fourfold_phase_beta_parameter_germ.py",
            "fourfold_phase_beta_interval.py", "fourfold_phase_beta_bulk_interval.py",
            "fourfold_phase_beta_bulk_box.py", "fourfold_phase_root_interval.py",
            "fourfold_phase_uniform_tail.py", "fourfold_phase_cap_scaled_body.py",
            "fourfold_phase_cap_energy_interval.py", "fourfold_phase_cap_wiener_box.py",
            "fourfold_phase_natural_exterior_graft.py", "fourfold_phase_exterior_entry_jet.py")})
    def checkpoint():
        report["wall_seconds"] = time.monotonic()-started
        report["CPU_seconds"] = time.process_time()-cpu
        save(args.out, report)
    def run_piece(kind, left, right, evaluate, span=None):
        pending = [(left, right, 0)]
        while pending:
            a, b, depth = pending.pop()
            try:
                row = evaluate(a, b)
                error = arb(row["relative_form_error"]["ball"])
                if not error <= exact_arb(args.relative_target):
                    raise ValueError("relative form fee exceeds target: "+error.str(15))
                row.update(kind=kind, radial_interval=[str(a), str(b)],
                           subdivision_depth=depth)
                if span is not None:
                    row["true_common_span"] = list(map(str, span))
                rows.append(row)
            except (ValueError, ZeroDivisionError, OverflowError) as exc:
                item = dict(kind=kind, radial_interval=[str(a), str(b)],
                            subdivision_depth=depth, reason=str(exc))
                if depth >= args.max_depth:
                    failed.append(item)
                else:
                    rejected.append(item)
                    mid = (a+b)/2
                    pending.extend([(mid, b, depth+1), (a, mid, depth+1)])
            report["pending_current_piece"] = [[str(a), str(b), d] for a, b, d in pending]
            checkpoint()
        print(json.dumps(dict(kind=kind, piece=[str(left), str(right)],
                              accepted=len(rows), unresolved=len(failed))), flush=True)

    checkpoint()
    if args.part in ("body", "both"):
        center = ParameterDiskBody(args.object, args.parameter_radius, False,
                                   args.primitive_nodes, args.angles)
        disk = ParameterDiskBody(args.object, args.parameter_radius, True,
                                 args.primitive_nodes, args.angles)
        common = common_cells(center)
        cuts = sorted({args.body_left, args.body_right}
                      | {x for x in common if args.body_left < x < args.body_right})
        for left, right in zip(cuts, cuts[1:]):
            k = bisect_right(common, (left+right)/2)-1
            span = common[k:k+2]
            try:
                center.set_cell(*span)
                disk.set_cell(*span)
            except (ValueError, ZeroDivisionError, OverflowError) as exc:
                failed.append(dict(kind="body", radial_interval=[str(left), str(right)],
                                   stage="exact scalar germ setup", reason=str(exc)))
                checkpoint()
                break
            run_piece("body", left, right,
                      lambda a, b: body_comparison(center, disk, a, b,
                                                  args.half_width, args.parameter_radius), span)
            if failed:
                break
    if args.part in ("graft", "both") and not failed:
        if args.compute_graft:
            graft = WholeFamilyGraft(args.object, args.half_width, Fraction(1, 8))
            run_piece("graft", Fraction(3), Fraction(25, 8),
                      lambda a, b: graft_comparison(graft, a, b))
        else:
            paid = json.loads(args.graft_certificate.read_text())
            if (paid.get("kind") != "actual_R66_whole_family_natural_graft_parameter_form_comparison"
                    or not paid.get("complete") or not paid.get("whole_eta_graft_complete")
                    or paid["source_sha256"] != sha(Path(__file__).with_name("fourfold_phase_graft_parameter_exact.mjs"))
                    or paid["input_sha256"] != sha(paid["input_path"])):
                raise ValueError("the paid actual graft certificate or source identity changed")
            original_entry = json.loads(Path(paid["input_path"]).read_text())
            if (original_entry["origin_inputs_sha256"] != definition["origin_inputs"]["sha256"]
                    or original_entry["direction_sha256"] != definition["direction"]["sha256"]
                    or original_entry["entry"]["cut"] != "3"):
                raise ValueError("the paid graft belongs to a different actual affine family")
            parameter = list(map(Fraction, paid["original_parameter_interval"]))
            if not parameter[0] <= delta-args.half_width < delta+args.half_width <= parameter[1]:
                raise ValueError("requested family is outside the paid graft parameter box")
            denominator = int(paid["exact_interval_endpoint_denominator"])
            if denominator != 10**60:
                raise ValueError("unexpected directed graft arithmetic scale")
            maximum_paid = Fraction(0)
            for a, b, numerator in paid["intervals"]:
                value = Fraction(int(numerator), denominator)
                if not 0 <= value <= args.relative_target:
                    raise ValueError("the actual paid graft fee exceeds this requested target")
                maximum_paid = max(maximum_paid, value)
                rows.append(dict(kind="graft", radial_interval=[a, b],
                    relative_form_error=ball_record(exact_arb(value)),
                    method="previously executed full-parameter exact BigInt Wiener cover"))
            if (len(paid["intervals"]) != paid["accepted_intervals"]
                    or not cover_complete([x for x in rows if x["kind"] == "graft"], Fraction(3), Fraction(25, 8))):
                raise ValueError("the paid graft exact interval cover is incomplete")
            report["paid_graft_certificate_path"] = str(args.graft_certificate)
            report["paid_graft_certificate_sha256"] = sha(args.graft_certificate)
            report["paid_graft_maximum"] = str(maximum_paid)
            checkpoint()
    body_rows = [x for x in rows if x["kind"] == "body"]
    graft_rows = [x for x in rows if x["kind"] == "graft"]
    body_ok = cover_complete(body_rows, args.body_left, args.body_right)
    graft_ok = cover_complete(graft_rows, Fraction(3), Fraction(25, 8))
    report["complete"] = not failed and (
        args.part == "body" and body_ok or args.part == "graft" and graft_ok
        or args.part == "both" and body_ok and graft_ok)
    report["cap_form_comparison_complete"] = bool(
        report["complete"] and args.part == "both"
        and args.body_left == Fraction(1, 4) and args.body_right == 3)
    if rows:
        report["maximum_relative_form_error"] = ball_record(
            max(arb(x["relative_form_error"]["ball"]).upper() for x in rows))
    report["scope"] = (
        "Finite positive body/graft relative form only, all real angles and the declared "
        "whole parameter interval. The same actual nonnegative tail is held on both sides "
        "as in R111. No whole DN matrix, infinite Schur inverse or nonlinear solution is asserted.")
    checkpoint()
    print(json.dumps(dict(complete=report["complete"],
                          cap_form_comparison_complete=report["cap_form_comparison_complete"],
                          maximum_relative_form_error=report.get("maximum_relative_form_error"),
                          wall_seconds=report["wall_seconds"])), flush=True)
    if not report["complete"]:
        raise SystemExit("the requested true parameter cover is incomplete")


if __name__ == "__main__":
    main()
