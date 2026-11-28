#!/usr/bin/env python3
"""Continuous third activity/core flux intervals for one genuine 7a Cartesian map.

This supplies numerical coefficients for the existing R6/R67 short-cylinder
choice. It does not reprove that criterion, invent a tail, or certify the
whole closed surface. Every original Fourier mode, finite mean, exact core
lift and center repair is retained. With a genuine full-height tail bundle,
the original complete cut correction is retained as well. Original and
actual coupled sources use their separate already reviewed acceptance gates.

The original NewMetric/CutMetric field-building statements are compiled in
an independent namespace with only the final return changed to X, Xs, Xpsi.
No original source, loader gate or mathematical field is patched. Complete
three-jets and D2 bound the second derivatives of the flux integrands.
"""
import os
for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_key] = "1"

import argparse
from fractions import Fraction as Q
import hashlib
import inspect
import json
from pathlib import Path
import resource
import sys
import textwrap
import time
import traceback

import numpy as np

HERE = Path(__file__).resolve().parent
GEO = HERE.parent / "geometry"
sys.path[:0] = [str(HERE), str(GEO)]
import cartesian_prefix_metric as metric
import cartesian_prefix_cut_metric as cut_metric
import chord_coupled_prefix_continuous as coupled
from cartesian_prefix_interval_geometry import SCRIPTS, save, sha

I = metric.I
SCHEMA = "actual-Cartesian-third-activity-core-flux-v1"


def display(value):
    return [float(value.x[0]), float(value.x[1])]


def absolute_upper(value):
    if not value.finite():
        raise ArithmeticError("A complete moment enclosure is not finite")
    return float(np.max(np.maximum(np.abs(value.x[0]), np.abs(value.x[1]))))


def widen(value, error):
    radius = float(error.x[1])
    if not np.isfinite(radius) or radius < 0:
        raise ArithmeticError("The continuous integration error is invalid")
    return value + I(-radius, radius)


def separate_from_zero(value):
    return bool(float(value.x[0]) > 0 or float(value.x[1]) < 0)


def complete_field_evaluator(with_cut):
    """Reuse the exact old field builder; discard only its Gram output code."""
    cls = cut_metric.CutMetric if with_cut else metric.NewMetric
    original = inspect.getsource(cls.evaluate)
    marker = "        Xs,Xp=field(1,0),field(0,1)\n"
    if original.count(marker) != 1 or original.count("    def evaluate(") != 1:
        raise ValueError("The reviewed complete-field evaluator changed")
    source = original[:original.index(marker)]
    source = source.replace("    def evaluate(", "    def complete_fields(", 1)
    source += "        return field(0,0),field(1,0),field(0,1)\n"
    source = textwrap.dedent(source)
    namespace = dict(cls.evaluate.__globals__)
    exec(compile(source, str(Path(__file__).resolve())+"::complete_fields", "exec"), namespace)
    return namespace["complete_fields"], dict(
        original_class=cls.__name__, original_file=str(Path(inspect.getfile(cls)).resolve()),
        original_file_sha256=sha(inspect.getfile(cls)),
        original_evaluate_sha256=hashlib.sha256(original.encode()).hexdigest(),
        compiled_field_return_sha256=hashlib.sha256(source.encode()).hexdigest(),
        original_field_builder_statements_unchanged=True,
        only_Gram_output_replaced_by_complete_fields=True,
        original_module_or_loader_patched=False,
        complete_core_center_and_optional_cut_retained=True)


def coordinate(value, index):
    return value.item((slice(None), index))


def third_real(x, y):
    return x*x*x - 3*x*y*y


def density(fields, core=False):
    X, Xs, Xp = fields
    x, y, z = (coordinate(X, j) for j in range(3))
    xp, yp = coordinate(Xp, 0), coordinate(Xp, 1)
    if core:
        area = x*yp - y*xp
        return third_real(x, y)*area/5, area
    xs, ys = coordinate(Xs, 0), coordinate(Xs, 1)
    vertical_area = xp*ys - yp*xs
    return 2*z*third_real(x, y)*vertical_area, vertical_area


class MomentVerifier:
    def __init__(self, verifier, with_cut):
        self.v = verifier
        self.fields, self.extraction = complete_field_evaluator(with_cut)
        self.N = verifier.N
        self.width = verifier.tables["angular_width"]
        self.sector_length = self.width*self.N
        if (verifier.record.get("angular_sector") != "[0,2*pi/3]"
                or verifier.record.get("right_sector_endpoint_gram_equals_left_exactly") is not True
                or np.any(verifier.pm % 3 != 1) or np.any(verifier.hm % 3 != 0)
                or float(self.width.x[0]) <= 0):
            raise ValueError("The actual complete threefold angular sector is required")
        # CutMetric's own proof loop restricts its grid to the cut strip.
        # The activity integral must instead include the WHOLE original prefix.
        grid = set(verifier.field.x + verifier.target.grid + [verifier.width])
        if with_cut:
            grid.add(verifier.cut_start)
        self.grid = sorted(grid)
        if (self.grid[0] != Q(0) or self.grid[-1] != verifier.target.end
                or any(b <= a for a, b in zip(self.grid[:-1], self.grid[1:]))):
            raise ValueError("The full common-jet prefix domain is not covered")

    def evaluate(self, left, right, tag, axis, core=False):
        fields = self.fields(self.v, left, right, tag, axis)
        value, determinant = density(fields, core=core)
        if not all(getattr(value, order).finite() for order in ("v", "d", "d2")):
            raise ArithmeticError("The complete moment D2 jet is not finite")
        return value, determinant

    def prefix_span(self, left, right):
        h, middle = right-left, (left+right)/2
        point, _ = self.evaluate(middle, middle, "point", "radial")
        radial, _ = self.evaluate(left, right, "box", "radial")
        angular, _ = self.evaluate(left, right, "box", "angular")
        R, B = absolute_upper(radial.d2), absolute_upper(angular.d2)
        hI = I.rational(h)
        approximation = hI*self.width*point.v.sum()
        radial_error = self.sector_length*I.rational(h**3)*I(R)/24
        angular_error = hI*self.sector_length*self.width.sq()*I(B)/12
        # The scalar third flux is exactly 2*pi/3 periodic. The factor 2
        # for the lower reflected prefix is already present in density().
        enclosure = 3*widen(approximation, radial_error+angular_error)
        return enclosure, dict(
            radial_exact=[str(left), str(right)], radial_display=[float(left), float(right)],
            full_circle_two_reflected_prefix_flux_interval=display(enclosure),
            sector_midpoint_periodic_trapezoid_interval=display(approximation),
            complete_radial_second_absolute_upper=R,
            complete_angular_second_absolute_upper=B,
            sector_radial_midpoint_error_upper=float(radial_error.x[1]),
            sector_angular_trapezoid_error_upper=float(angular_error.x[1]),
            includes_full_finite_mean=True, includes_core_lift_and_center=True,
            sampled_maximum_substituted_for_continuous_bound=False)

    def core(self):
        point, _ = self.evaluate(Q(0), Q(0), "point", "angular", core=True)
        angular, determinant = self.evaluate(Q(0), Q(0), "box", "angular", core=True)
        bound = absolute_upper(angular.d2)
        approximation = self.width*point.v.sum()
        error = self.sector_length*self.width.sq()*I(bound)/12
        value = 3*widen(approximation, error)
        return value, dict(real_m3_boundary_flux_interval=display(value),
            real_m3_separated_from_zero=separate_from_zero(value),
            formula="(1/5) integral Re((x+i*y)^3)*(x*y_psi-y*x_psi) dpsi",
            whole_circle_threefold_factor=3,
            complete_angular_second_absolute_upper=bound,
            full_circle_trapezoid_error_upper=float((3*error).x[1]),
            planar_origin_orientation_determinant_lower=float(np.min(determinant.v.x[0])),
            actual_inlet_of_same_complete_Cartesian_map_used=True,
            imaginary_moment_assumed_zero=False,
            core_convexity_or_closed_curve_theorem_reproved=False)


def conditional_tail_bound(Z, radius, pi_interval):
    """Only after a same-field injective graph, r=R and height/radius proof.

    Both reflected tails give |A3_tail| <= 2 Z int_disk r^3 dA
    = 4*pi*Z*radius^5/5. This helper does not validate those premises and
    is deliberately not called by the prefix/core-only command below.
    """
    if float(Z.x[0]) < 0 or float(radius.x[0]) < 0:
        raise ValueError("Nonnegative actual tail envelope bounds are required")
    return 4*pi_interval*Z*radius**5/5


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--tables", type=Path, required=True)
    ap.add_argument("--outdir", type=Path, required=True)
    ap.add_argument("--bundle", type=Path,
                    help="genuine full-height tail bundle, to include its entire prefix cut repair")
    ap.add_argument("--coupling-summary", type=Path, required=True)
    ap.add_argument("--cut-width", type=float, default=.04)
    ap.add_argument("--radial-parts", type=int, default=1)
    args = ap.parse_args()
    out, tables = args.outdir.resolve(), args.tables.resolve()
    repo = SCRIPTS.parents[2]
    if out == repo or repo in out.parents or args.radial_parts < 1:
        raise ValueError("Use a fresh external data directory and positive radial subdivision")
    out.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    coupled.check_reviewed_algebra()
    context = coupled.CoupledContext(args.coupling_summary, "third-activity-moment") if args.coupling_summary else None
    if context is not None:
        context.execution = dict(entry=str(Path(__file__).resolve()), entry_sha256=sha(__file__),
            original_acceptance_gate_replaced=False, actual_phase="third-activity-moment")
    write = context.save if context is not None else save
    report = dict(schema=SCHEMA, status="loading_actual_complete_moment_source", scope=__doc__,
        source_sha256=sha(__file__), tables=dict(path=str(tables), sha256=sha(tables)),
        prefix_flux_certified=False, core_flux_certified=False,
        complete_tail_moment_certified=False, whole_active_coefficient_certified=False,
        euclidean_noncongruence_certified=False, complete_surface=False,
        mathematical_completion=False, nonlinear_solver_invoked=False, full_J_assembled=False)
    write(out/"summary.json", report)
    try:
        if context is None:
            verifier = (cut_metric.CutMetric(tables, args.bundle, out, args.cut_width)
                        if args.bundle else metric.NewMetric(tables))
        else:
            verifier = (coupled.CoupledCutMetric(tables, args.bundle, out, context, args.cut_width)
                        if args.bundle else coupled.CoupledNewMetric(tables, context))
        moment = MomentVerifier(verifier, args.bundle is not None)
        source = verifier.record
        physical_path = Path(source["source_run"]).resolve().parent/"physical.npz"
        physical_sha = sha(physical_path)
        expected_physical_sha = context.physical_sha() if context else source["physical_sha256"]
        if physical_sha != expected_physical_sha:
            raise ValueError("The currently verified physical source changed")
        paths = (Path(__file__).resolve(), Path(metric.__file__).resolve(),
                 Path(cut_metric.__file__).resolve(), Path(coupled.__file__).resolve(),
                 GEO/"cartesian_prefix_metric_target.py",
                 SCRIPTS/"resume_m3/certify_bridge_metric_fourier_taylor.py",
                 SCRIPTS/"resume_m3/certify_r59_fixed_mean_ranges.py",
                 SCRIPTS/"finite_closure/m3_m8_closed_map/interval_geometry_kernel.py")
        source_hashes = dict(source["source_hashes"])
        source_hashes.update({str(path):sha(path) for path in paths})
        report.update(status="continuous_prefix_and_core_moment_running",
            source_kind=(coupled.SOURCE_KIND if context else "actual_original_R53_design"),
            source_run=source["source_run"], source_run_sha256=source["source_run_sha256"],
            physical_file=dict(path=str(physical_path), sha256=physical_sha),
            physical_sha256=physical_sha,
            defining_jets=source["defining_jets"], angular_tables=source["angular_tables"],
            mean_nodes=source["mean_nodes"], modes=source["modes"],
            homotopy=source.get("homotopy"), angular_boxes_per_sector=moment.N,
            source_hashes=source_hashes, field_extraction=moment.extraction,
            complete_cut_correction_included=args.bundle is not None,
            original_finite_mean_and_all_modes_retained=True,
            original_geometry_source_or_gates_modified=False,
            continuous_error_rule="radial midpoint L*h^3*sup|Fss|/24 plus periodic angular trapezoid h*L*dpsi^2*sup|Fpsipsi|/12; full-circle factor 3",
            scalar_threefold_periodicity="z, Re(w^3) and the planar determinant are each invariant under simultaneous horizontal rotation by 2*pi/3",
            full_prefix_radial_domain_exact=[str(moment.grid[0]), str(moment.grid[-1])])
        if args.bundle:
            report.update(bundle=dict(path=str(args.bundle.resolve()), sha256=sha(args.bundle)),
                complete_cut_definition=verifier.cut_definition,
                complete_cut_data=verifier.cut_data,
                tail_projection_injectivity_not_inferred=True,
                tail_nearcut_identity_not_inferred=True)
        core, core_report = moment.core()
        report.update(core_flux=core_report, core_flux_certified=True)
        leaves, total = [], I(0)
        exact_cover = []
        for parent_left, parent_right in zip(moment.grid[:-1], moment.grid[1:]):
            width = (parent_right-parent_left)/args.radial_parts
            for part in range(args.radial_parts):
                left, right = parent_left+part*width, parent_left+(part+1)*width
                value, row = moment.prefix_span(left, right)
                total += value
                leaves.append(row)
                exact_cover.append((left, right))
                if len(leaves) % 16 == 0:
                    report.update(completed_radial_leaves=len(leaves),
                        current_prefix_flux_interval=display(total),
                        seconds=time.monotonic()-started)
                    write(out/"summary.json", report)
                    print(json.dumps(dict(stage="continuous_third_flux", leaves=len(leaves),
                        interval=display(total), seconds=report["seconds"])), flush=True)
        if (not exact_cover or exact_cover[0][0] != Q(0)
                or exact_cover[-1][1] != verifier.target.end
                or any(a[1] != b[0] for a, b in zip(exact_cover[:-1], exact_cover[1:]))):
            raise AssertionError("The actual original prefix was not covered exactly once")
        leaf_path = out/"complete-prefix-moment-leaves.json"
        save(leaf_path, dict(source_run_sha256=source["source_run_sha256"],
            complete_original_domain_covered_once=True, leaves=leaves))
        candidates = []
        for length in (Q(1, 200), Q(1, 100)):
            value = total+I.rational(length)*core
            candidates.append(dict(total_inserted_cylinder_length_exact=str(length),
                prefix_plus_cylinder_real_coefficient_interval=display(value),
                tail_coefficient_not_included=True,
                whole_activity_nonzero_certified=False))
        report.update(status="continuous_actual_prefix_and_core_third_flux_enclosed",
            prefix_flux_certified=True, core_flux_certified=True,
            real_prefix_flux_interval=display(total),
            real_prefix_flux_separated_from_zero=separate_from_zero(total),
            complete_prefix_domain_covered_once=True, radial_leaves=len(leaves),
            all_actual_shared_jet_and_repair_joins_retained=True,
            prefix_leaves=dict(path=str(leaf_path), sha256=sha(leaf_path)),
            candidate_total_cylinder_lengths=candidates,
            tail_bound_available_only_after_actual_same_field_geometry="4*pi*Z*r_star^5/5, requiring complete injective planar projection, radius identity r=R, |z|<=Z and r_xy<=r_star",
            actual_short_cylinder_length_selected=False,
            maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            seconds=time.monotonic()-started)
        write(out/"summary.json", report)
        print(json.dumps({key:report[key] for key in
            ("status", "real_prefix_flux_interval", "core_flux", "radial_leaves", "seconds")}), flush=True)
    except Exception as error:
        (out/"exception.txt").write_text(traceback.format_exc())
        report.update(status="moment_interval_execution_failed", error=repr(error),
            prefix_flux_certified=False, seconds=time.monotonic()-started)
        write(out/"summary.json", report)
        raise


if __name__ == "__main__":
    main()
