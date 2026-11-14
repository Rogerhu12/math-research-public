#!/usr/bin/env python3
"""R78: actual diameter and a point-to-whole-surface phase witness.

Only the old body cells whose norm bound is too wide are refined.  The new
point-to-surface certificate covers every common scalar span in [0,1/4],
every real angle, the same exact affine parameter box, and the infinite R33
primitive.  Existing complete exterior height bounds cover the rest of the
closed surface.  No material-point gap is substituted for a Hausdorff bound.
The auxiliary rotated images are not claimed to be a noncongruent flex.
"""
from __future__ import annotations

import argparse
from collections import deque
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import time

import numpy as np
from flint import arb, acb, ctx

from fourfold_phase_beta_bulk_interval import exact_arb, real_interval
from fourfold_phase_beta_bulk_box import (
    Box, CBox, zeros, arb_box, reduce_box, square_box)
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_parameter_germ import provenance
from fourfold_phase_positive_family_outer import StablePositiveFamily


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                     ensure_ascii=False).encode()).hexdigest()


def read(path):
    with (gzip.open(path, "rt") if str(path).endswith(".gz") else open(path)) as f:
        return json.load(f)


def lo(record):
    return arb(record["lower"]).lower()


def hi(record):
    return arb(record["upper"]).upper()


def bitem(value, index):
    return Box(value.lo[index], value.hi[index])


class ShapeTarget(StablePositiveFamily):
    def prepare_angles(self):
        gap = arb.pi() / (4 * self.angles)
        sine, cosine = [], []
        for j in range(self.sample_count):
            angle = arb.pi() * j / (2 * self.angles) + arb(0, gap.upper())
            sine.append(arb_box(angle.sin()))
            cosine.append(arb_box(angle.cos()))
        self.physical_sines = Box(np.array([x.lo for x in sine]), np.array([x.hi for x in sine]))
        self.physical_cosines = Box(np.array([x.lo for x in cosine]), np.array([x.hi for x in cosine]))
        self.normalized_modes = np.asarray(self.frequency, dtype=int) // 4
        self.gap_weights = arb_box(arb.pi() / self.angles) * Box(
            np.abs(self.normalized_modes).reshape(-1, 1))

    def physical_common_domain(self):
        splines = [self.base, self.shift, self.raw, self.raw_direction,
                   *self.means, *self.height_integrals]
        left, right = None, None
        for spline in splines:
            knots = [Fraction.from_float(float(x)) for x in spline.knots_float]
            a, b = knots[spline.degree], knots[-spline.degree-1]
            a, b = max(a, -b), min(b, -a)
            left = a if left is None else max(left, a)
            right = b if right is None else min(right, b)
        if not left < 0 < Fraction(1, 4) < right:
            raise ValueError("the true reflected scalar domains do not cover the geometry task")
        return left, right

    def position_boxes(self, left, right):
        self.set_cell(left, right)
        radial = acb(real_interval(left, right))
        coefficients, _ = self.finite_data(radial)
        values = coefficients[0]
        # This is the true infinite primitive error on the entire angular cell.
        error = self.tail_errors(radial, arb.pi()/self.angles)[0]
        magnitude = Box(values.magnitude_upper())
        fee = arb_box(error) + reduce_box(magnitude * self.gap_weights)
        data = zeros((self.angles, 3))
        data[self.normalized_modes % self.angles] = values
        samples = (self.fast_fourier.fft(data, inverse=True) * self.angles)[:self.sample_count]
        if np.any(samples.imag.lo > 0) or np.any(samples.imag.hi < 0):
            raise ValueError("the real finite position lost its reality enclosure")
        result = samples.real + Box(-fee.hi, fee.hi)
        if not np.all(np.isfinite(result.lo)) or not np.all(np.isfinite(result.hi)):
            raise ValueError("nonfinite full real position enclosure")
        return result, error, fee.hi.tolist()

    def exact_radial_point(self, point, scalar_cell, angle_half_quarter=False):
        self.set_cell(*scalar_cell)
        radial = acb(exact_arb(point))
        coefficients, _ = self.finite_data(radial)
        multiplier = (-1.)**self.normalized_modes if angle_half_quarter else np.ones(self.nodes)
        value = (coefficients[0] * CBox(multiplier.reshape(-1, 1))).sum()
        error = self.tail_errors(radial)[0]
        if np.any(value.imag.lo > 0) or np.any(value.imag.hi < 0):
            raise ValueError("the selected exact-angle point lost reality")
        return value.real + Box(-arb_box(error).hi, arb_box(error).hi), error

    def distance_lower_squared(self, position, witness_radius):
        fr, ft, z = [bitem(position, (slice(None), j)) for j in range(3)]
        x = self.physical_cosines*fr-self.physical_sines*ft
        y = self.physical_sines*fr+self.physical_cosines*ft
        # The half-quarter chart plus exact D4 reflections and four rotations
        # covers the entire real angle.  Reflections preserve distance to the
        # x axis; test all four quarter-rotated target points explicitly.
        lower = []
        for px, py in ((witness_radius, Box(0.)), (Box(0.), witness_radius),
                       (-witness_radius, Box(0.)), (Box(0.), -witness_radius)):
            d2 = square_box(x-px)+square_box(y-py)+square_box(z)
            lower.append(float(np.min(d2.lo)))
        return min(lower)


def spline_partition(target, left, right):
    points = {Fraction(left), Fraction(right)}
    for key, values in target.frozen.items():
        if key.endswith("_knots"):
            points.update(q for q in (abs(Fraction.from_float(float(x))) for x in values)
                          if left < q < right)
    return sorted(points)


def containing_span(target, point):
    points = spline_partition(target, Fraction(0), Fraction(3))
    for a, b in zip(points, points[1:]):
        if a <= point <= b:
            return a, b
    raise ValueError("selected point has no exact common scalar span")


def exact_cover(rows, left, right):
    cursor = Fraction(left)
    for row in sorted(rows, key=lambda r: Fraction(r["radial_interval"][0])):
        a, b = map(Fraction, row["radial_interval"])
        if a != cursor or not a < b:
            raise ValueError("a claimed exact radial cover has a gap or overlap")
        cursor = b
    if cursor != Fraction(right):
        raise ValueError("a claimed radial cover stops early")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--center-object", type=Path,
                    default=Path("data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step4_object.json"))
    ap.add_argument("--half-width", type=Fraction, default=Fraction(1, 2000000))
    ap.add_argument("--closed", type=Path,
                    default=Path("notes/2026-11-12-actual-closed-approximate-exterior.json"))
    ap.add_argument("--robin", type=Path,
                    default=Path("notes/2026-11-12-actual-exterior-robin-certificate.json"))
    ap.add_argument("--diameter-target", type=Fraction, default=Fraction(2553, 1000))
    ap.add_argument("--separation-target", type=Fraction, default=Fraction(13, 100))
    ap.add_argument("--quarter-nodes", type=int, default=256)
    ap.add_argument("--angles", type=int, default=1024)
    ap.add_argument("--bits", type=int, default=192)
    ap.add_argument("--max-depth", type=int, default=15)
    ap.add_argument("--max-attempts", type=int, default=6000)
    ap.add_argument("--resume", action="store_true")
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    if args.bits < 128 or args.angles < args.quarter_nodes or args.angles % 4:
        raise ValueError("insufficient precision or angular grid")
    ctx.prec, ctx.cap = args.bits, 4
    started = time.monotonic()
    closed, robin = read(args.closed), read(args.robin)
    if not closed.get("complete") or not robin.get("complete"):
        raise ValueError("complete actual exterior inputs are required")
    if sha(args.closed) not in robin["input_sha256"].values():
        raise ValueError("the true-tail report does not bind the actual closed background")
    inputs = {}
    for path, digest in closed["input_sha256"].items():
        if sha(path) != digest:
            raise ValueError("an actual complete geometry report changed: "+path)
        inputs[path] = read(path)
    target = ShapeTarget(args.center_object, args.half_width, args.quarter_nodes,
                         args.angles, arb(".003"), arb(".0025"), arb(".32"))
    target.prepare_angles()
    domain = target.physical_common_domain()
    identity = provenance(target, args.center_object)
    for key in ("origin_inputs_sha256", "direction_sha256", "exact_parameter_interval"):
        if identity[key] != closed[key] or identity[key] != robin[key]:
            raise ValueError("the diameter/witness and actual exterior objects differ")
    identity.pop("dependency_sha256")
    identity["source_sha256"] = sha(__file__)
    dependencies = [
        "fourfold_phase_positive_family_outer.py", "fourfold_phase_actual_positive_cap.py",
        "fourfold_phase_beta_parameter_germ.py", "fourfold_phase_beta_parameter_root.py",
        "fourfold_phase_beta_bulk_box.py", "fourfold_phase_beta_bulk_interval.py",
        "fourfold_phase_beta_interval.py", "fourfold_phase_beta_affine.py",
        "fourfold_phase_beta_combine.py", "fourfold_phase_root_interval.py",
        "fourfold_phase_uniform_tail.py", "fourfold_interval_scalar.py"]
    dependency_sha = {p: sha(Path(__file__).with_name(p)) for p in dependencies}
    limit_norm2 = (exact_arb(args.diameter_target)/2)**2
    limit_distance2 = exact_arb(args.separation_target)**2
    if not limit_norm2 > 0 or not limit_distance2 > 0:
        raise ValueError("positive geometric targets are required")

    selected, inherited, queue = [], [], deque()
    finite_height_lower = None
    graft = None
    for path, report in inputs.items():
        if "natural-graft" in path:
            graft = report
        if "cells" not in report or not report["cells"] or "real_geometry" not in report["cells"][0]:
            continue
        for index, row in enumerate(report["cells"]):
            item = dict(report=path, index=index, row_sha256=canonical_sha(row),
                        radial_interval=row["radial_interval"],
                        norm2_upper=row["real_geometry"]["norm2"][1])
            if arb(item["norm2_upper"]) > limit_norm2:
                selected.append(item)
                queue.append(dict(kind="diameter", parent=len(selected)-1,
                                  left=item["radial_interval"][0],
                                  right=item["radial_interval"][1], depth=0))
            else:
                inherited.append(item)
            if Fraction(row["radial_interval"][0]) >= Fraction(1, 4):
                z = arb(row["real_geometry"]["Fz"][0])
                finite_height_lower = z if finite_height_lower is None else min(finite_height_lower, z)
    if graft is None or finite_height_lower is None:
        raise ValueError("the actual external components are missing")
    if any(not domain[0] <= Fraction(task["left"]) < Fraction(task["right"]) <= domain[1]
           for task in queue):
        raise ValueError("a selected body cell leaves the true scalar domain")
    waist_span = containing_span(target, Fraction(0))
    point, point_error = target.exact_radial_point(Fraction(0), waist_span, True)
    witness_radius = bitem(point, 0)
    if not float(witness_radius.lo) > 0:
        raise ValueError("the actual waist witness is not on the positive axis")
    peak_r = Fraction(281, 500)
    peak, peak_error = target.exact_radial_point(peak_r, containing_span(target, peak_r))
    peak_norm2_lower = arb(float(reduce_box(square_box(peak)).lo))
    if not peak_norm2_lower > 0:
        raise ValueError("the diameter lower witness failed")
    separation_points = spline_partition(target, Fraction(0), Fraction(1, 4))
    for a, b in zip(separation_points, separation_points[1:]):
        queue.append(dict(kind="separation", parent=None, left=str(a), right=str(b), depth=0))

    geometry = closed["closed_approximate_geometry"]
    displacement = hi(robin["added_actual_geometry"]["Cartesian_displacement_upper"])
    graft_height_lower = (lo(graft["entry"]["height"][0])
                          - arb.pi()*hi(graft["entry"]["radius"][0])/2).lower()
    remote_height_lower = (lo(geometry["final_height_lower"])
                           -hi(geometry["radial_height_increase"])
                           -hi(geometry["connector_height_increase"])
                           -hi(geometry["tail_height_increase"])-displacement).lower()
    exterior_height_lower = min(finite_height_lower, graft_height_lower, remote_height_lower)
    if not exterior_height_lower > exact_arb(args.separation_target):
        raise ValueError("the complete exterior does not leave the witness ball vertically")

    base = dict(kind="actual_closed_diameter_and_whole_surface_phase_separation", complete=False,
                **identity, dependency_sha256=dependency_sha,
                input_sha256={str(args.closed):sha(args.closed),str(args.robin):sha(args.robin)},
                exact_reflected_scalar_domain=list(map(str,domain)),
                bits=args.bits, quarter_nodes=args.quarter_nodes, angular_boxes=args.angles,
                diameter_target=str(args.diameter_target), separation_target=str(args.separation_target),
                selected_old_body_cells=selected, inherited_old_body_cells=inherited,
                initial_separation_spans=len(separation_points)-1,
                witness=dict(phase_angle="pi/4", material_r="0", material_theta="-pi/4",
                    Cartesian_point="(waist_radius,0,0) in R_(pi/4) S",
                    radius=[float(witness_radius.lo),float(witness_radius.hi)],
                    infinite_primitive_error=ball_record(point_error)),
                diameter_lower_witness=dict(material_r=str(peak_r),material_theta="0",
                    norm2_lower=ball_record(peak_norm2_lower),
                    infinite_primitive_error=ball_record(peak_error)),
                exterior_separation={k:ball_record(v) for k,v in dict(
                    finite_body_height_lower=finite_height_lower,
                    graft_height_lower=graft_height_lower,
                    remote_tail_height_lower=remote_height_lower,
                    complete_exterior_height_lower=exterior_height_lower).items()},
                diameter_cells=[], separation_cells=[], failed_cells=[], attempts=0,
                limitations=[
                    "The current actual closed background is approximate, not an exact isometric family.",
                    "The auxiliary phase images are rigid rotations as sets; their delta_E is zero.",
                    "The separation is from one actual point to the whole other surface, not a paired material-point gap.",
                    "The true infinite primitive, complete angular gaps, exact radial spans and full exterior are included.",
                    "Final nonlinear C0 corrections and a noncongruent fixed-H family must still be supplied."
                ])
    if args.resume:
        old = read(args.out)
        for key in ("source_sha256","dependency_sha256","input_sha256","exact_parameter_interval",
                    "center_object_sha256","bits","quarter_nodes","angular_boxes",
                    "diameter_target","separation_target"):
            if old[key] != base[key]:
                raise ValueError("resume identity mismatch: "+key)
        if old["complete"]:
            raise ValueError("the saved certificate is already complete")
        base = old
        queue = deque(old["pending"])
    previous_seconds = base.get("elapsed_seconds",0.)
    def save():
        base["pending"] = list(queue)
        base["elapsed_seconds"] = previous_seconds+time.monotonic()-started
        args.out.parent.mkdir(parents=True,exist_ok=True)
        with (gzip.open(args.out,"wt") if str(args.out).endswith(".gz") else open(args.out,"w")) as f:
            json.dump(base,f,ensure_ascii=False,indent=2);f.write("\n")
    save()
    while queue and base["attempts"] < args.max_attempts:
        task = queue.popleft()
        a,b=Fraction(task["left"]),Fraction(task["right"])
        base["attempts"] += 1
        try:
            position,error,fees=target.position_boxes(a,b)
            if task["kind"] == "diameter":
                value=arb(float(np.max(reduce_box(square_box(position),axis=1).hi)))
                passed=value < limit_norm2
                data=dict(norm2_upper=ball_record(value))
            else:
                value=arb(target.distance_lower_squared(position,witness_radius))
                passed=value > limit_distance2
                data=dict(distance_squared_lower=ball_record(value))
            if not passed:
                raise ValueError("the continuous geometry interval is wider than the strict target")
            row=dict(radial_interval=[str(a),str(b)],depth=task["depth"],parent=task["parent"],
                     infinite_primitive_error=ball_record(error),
                     full_component_error_and_angular_gap=fees,**data)
            base[task["kind"]+"_cells"].append(row)
        except (ValueError,OverflowError,ZeroDivisionError) as exc:
            if task["depth"] < args.max_depth:
                mid=(a+b)/2
                queue.appendleft(dict(task,left=str(mid),right=str(b),depth=task["depth"]+1))
                queue.appendleft(dict(task,left=str(a),right=str(mid),depth=task["depth"]+1))
            else:
                base["failed_cells"].append(dict(task,reason=str(exc)))
        # Do not retain all per-subdivision scalar germs during a long cover.
        target.fast_cell_cache.clear()
        if base["attempts"] % 10 == 0:
            save()
            print(json.dumps(dict(attempts=base["attempts"],pending=len(queue),
                                  diameter=len(base["diameter_cells"]),
                                  separation=len(base["separation_cells"]),
                                  failed=len(base["failed_cells"])),ensure_ascii=False),flush=True)
    if not queue and not base["failed_cells"]:
        for parent,row in enumerate(selected):
            exact_cover([r for r in base["diameter_cells"] if r["parent"]==parent],
                        *map(Fraction,row["radial_interval"]))
        exact_cover(base["separation_cells"],Fraction(0),Fraction(1,4))
        norm2_values=[arb(row["norm2_upper"]) for row in inherited]
        norm2_values += [hi(row["norm2_upper"]) for row in base["diameter_cells"]]
        radius_bound=max([hi(geometry["core_norm_upper"]),hi(geometry["graft_norm_upper"]),
                          hi(geometry["tail_norm_upper"])+displacement,
                          max(norm2_values).sqrt().upper()])
        diameter_upper=(2*radius_bound).upper()
        diameter_lower=(2*peak_norm2_lower.sqrt()).lower()
        # Separate length and squared-length quantities before their minimum.
        core_distance_lower=min(lo(row["distance_squared_lower"])
                                for row in base["separation_cells"]).sqrt().lower()
        distance_lower=min(exterior_height_lower,core_distance_lower)
        ratio=(distance_lower/diameter_upper).lower()
        epsilon=arb(1)/1000
        correction_margin=(distance_lower-2*epsilon
                           -(diameter_upper+2*epsilon)/20).lower()
        if not (diameter_upper < exact_arb(args.diameter_target)
                and distance_lower > exact_arb(args.separation_target)
                and ratio > arb(1)/20 and correction_margin > 0):
            raise ValueError("the complete geometric target or C0 stability margin failed")
        base["certified_geometry"]={k:ball_record(v) for k,v in dict(
            diameter_lower=diameter_lower,diameter_upper=diameter_upper,
            point_to_complete_surface_distance_lower=distance_lower,
            Hausdorff_over_diameter_lower=ratio,
            each_endpoint_C0_budget=epsilon,
            post_C0_five_percent_absolute_margin=correction_margin).items()}
        base["complete"]=True
    save()
    print(json.dumps(dict(complete=base["complete"],report_sha256=sha(args.out),
                         attempts=base["attempts"],failed=len(base["failed_cells"]),
                         elapsed_seconds=base["elapsed_seconds"])),flush=True)
    if not base["complete"]:
        raise SystemExit("the geometry cover remains incomplete; resume the saved queue")


if __name__=="__main__":
    main()
