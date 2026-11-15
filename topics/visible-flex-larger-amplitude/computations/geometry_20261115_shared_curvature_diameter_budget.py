#!/usr/bin/env python3
"""Same-field closed-chart curvature and complete-image diameter budgets.

Consumes the frozen complete active and two-cap interval components, plus the
unchanged original shared cover.  It does not evaluate a new field, its jets,
the target metric, a native equation, or a pair-separation problem.

D always means diam(F_0(M)).  A common all-phase enclosure is reported
separately and may only supply a conservative upper bound for D.  The original
tau is copied exactly, never selected again.  Chartwise curvature and K*tau
do not discharge global C2 seams, embedding, reach, held, or metric duties.
All rational arithmetic is restricted to the named public Actions repository.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import struct
import time


HERE = Path(__file__).resolve().parent
REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "same-shared-field-closed-chart-curvature-and-complete-image-scale-v1"
MIXED_NAME = "geometry_20261115_complete_mixed_phase_component.py"
CAP_NAME = "geometry_20261115_fixed_cap_rational_balls.py"
SOURCE_PINS = {
    MIXED_NAME:
        "dbdedb450ca2280f37802258377e5fd8728b9f20ce2545f22ec141b6965bc3ed",
    CAP_NAME:
        "a3ada50b5389a075f1da2d2237269a1a1ccc83c29aa35bc889d721eac0e2552e",
    "geometry_20261115_shared_active_interval_balls.py":
        "675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b",
}
README_RATIO = "3/100"


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("Scientific arithmetic is restricted to the named public Actions repository")


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       allow_nan=False)+"\n").encode()


def receipt(path):
    p = Path(path)
    h, size = hashlib.sha256(), 0
    with p.open("rb") as stream:
        for raw in iter(lambda: stream.read(1048576), b""):
            h.update(raw)
            size += len(raw)
    return dict(file=p.name, bytes=size, sha256=h.hexdigest())


def write_json(path, value, compressed=False):
    raw = canonical(value)
    if compressed:
        with path.open("xb") as stream:
            with gzip.GzipFile(filename="", mode="wb", fileobj=stream, mtime=0) as z:
                z.write(raw)
    else:
        with path.open("xb") as stream:
            stream.write(raw)
    out = receipt(path)
    if compressed:
        out.update(decoded_bytes=len(raw), decoded_sha256=digest(raw))
    return out


def load_bound_module(path, expected, name):
    if digest(path.read_bytes()) != expected:
        raise ValueError("Frozen consumer source changed: "+path.name)
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def q(value):
    if isinstance(value, bool) or not isinstance(value, (str, int)):
        raise ValueError("Exact certificate values must be integers or rational strings")
    return F(value)


def interval_record(value):
    lo, hi = q(value["lower"]), q(value["upper"])
    if lo > hi:
        raise ValueError("Reversed interval")
    return lo, hi


def original_number(record, caps):
    value = record["original_json_number"]
    actual = caps.exact_stored(value)
    if str(actual) != record["exact"]:
        raise ValueError("Stored original number has another exact value")
    expected = struct.pack("<d", value).hex() if isinstance(value, float) else None
    if record["float64le_hex"] != expected:
        raise ValueError("Stored original number has another binary64 identity")
    return actual


class EventStream:
    def __init__(self, path):
        self.path = path
        self.raw = path.open("xb")
        self.z = gzip.GzipFile(filename="", mode="wb", fileobj=self.raw, mtime=0)
        self.records = 0

    def write(self, record):
        self.z.write(canonical(record))
        self.records += 1

    def close(self):
        if self.z is not None:
            self.z.close()
            self.raw.close()
            self.z = None


class ImageBounds:
    """Union of complete position balls; rotations are about the original z axis."""
    def __init__(self, sqrt_upper, bits, image_kind):
        self.sqrt_upper, self.bits = sqrt_upper, bits
        self.image_kind = image_kind
        self.count = 0
        self.lower, self.upper = [None]*3, [None]*3
        self.origin_radius = F(0)
        self.horizontal_radius = F(0)

    def add(self, center, radius, box=None):
        center = tuple(center)
        if len(center) != 3 or radius < 0:
            raise ValueError("A complete three-dimensional position ball is required")
        lo = [v-radius for v in center]
        hi = [v+radius for v in center]
        if box is not None:
            if len(box) != 3:
                raise ValueError("A complete Cartesian position box is required")
            for j, (a, b) in enumerate(box):
                if a > b:
                    raise ValueError("Reversed Cartesian position box")
                lo[j], hi[j] = max(lo[j], a), min(hi[j], b)
                if lo[j] > hi[j]:
                    raise ValueError("The same position ball and box are disjoint")
        for j in range(3):
            self.lower[j] = lo[j] if self.lower[j] is None else min(self.lower[j], lo[j])
            self.upper[j] = hi[j] if self.upper[j] is None else max(self.upper[j], hi[j])
        norm = self.sqrt_upper(sum((v*v for v in center), F(0)), self.bits)
        horizontal = self.sqrt_upper(center[0]**2+center[1]**2, self.bits)
        self.origin_radius = max(self.origin_radius, norm+radius)
        self.horizontal_radius = max(self.horizontal_radius, horizontal+radius)
        self.count += 1

    def report(self, complete):
        if self.count == 0:
            return None
        diagonal_squared = sum(((b-a)**2 for a, b in zip(self.lower, self.upper)), F(0))
        diagonal = self.sqrt_upper(diagonal_squared, self.bits)
        twice_origin_radius = 2*self.origin_radius
        cylinder_squared = 4*self.horizontal_radius**2+(self.upper[2]-self.lower[2])**2
        cylinder = self.sqrt_upper(cylinder_squared, self.bits)
        family = min(twice_origin_radius, cylinder)
        phase_zero = min(diagonal, family)
        return dict(
            image_kind=self.image_kind,
            complete_declared_image_coverage=complete,
            position_domains=self.count,
            phase_zero_cartesian_box=[[str(a), str(b)] for a, b in zip(self.lower, self.upper)],
            phase_zero_box_diagonal_squared=str(diagonal_squared),
            phase_zero_box_diagonal_upper=str(diagonal),
            common_origin_radius_upper=str(self.origin_radius),
            common_horizontal_radius_upper=str(self.horizontal_radius),
            common_axis_origin=["0", "0", "0"],
            all_phase_twice_origin_radius_upper=str(twice_origin_radius),
            all_phase_cylinder_diameter_squared=str(cylinder_squared),
            all_phase_cylinder_diameter_upper=str(cylinder),
            covered_subset_all_phase_diameter_upper=str(family),
            covered_subset_phase_zero_diameter_upper=str(phase_zero),
            all_phase_common_diameter_upper=str(family) if complete else None,
            phase_zero_complete_image_diameter_upper=str(phase_zero) if complete else None,
            D_definition=("diam(F_0(M)); the entire marked phase-zero image, not a core or a material displacement"
                          if self.image_kind == "original_marked_image"
                          else "Diameter of the original unmarked base image; this is not the README marked D"),
            all_phase_bound_changes_D_definition=False,
            scope=("Complete declared image position cover; no C2, immersion or embedding claim"
                   if complete else
                   "Inspected position domains only; the displayed subset bounds do not bound the complete field"))


def cap_box_from_path(path, radius):
    if not isinstance(path, str) or any(c not in "0123" for c in path):
        raise ValueError("Invalid inherited quadtree path")
    box = ((-radius, radius), (-radius, radius))
    for c in path:
        (xl, xh), (yl, yh) = box
        xm, ym = (xl+xh)/2, (yl+yh)/2
        box = (((xl, xm), (yl, ym)), ((xm, xh), (yl, ym)),
               ((xl, xm), (ym, yh)), ((xm, xh), (ym, yh)))[int(c)]
    return box


def minimum_radius_squared(box):
    return sum((F(0) if a <= 0 <= b else min(a*a, b*b) for a, b in box), F(0))


def verify_cap_partition(fixed, caps):
    """Exact full quadtree leaf cover; equality with the disk is retained."""
    binding = fixed["input_binding"]
    radius = original_number(binding["cuff"], caps)
    if radius <= 0:
        raise ValueError("The original cuff radius must be positive")
    depth = fixed["parameters"]["depth"]
    if isinstance(depth, bool) or not isinstance(depth, int) or not 0 <= depth <= 30:
        raise ValueError("Invalid inherited complete cap depth")
    partition = fixed["exact_closed_disk_partition"]
    if (q(partition["radius"]) != radius
            or partition["root_box"] != [[str(-radius), str(radius)] for _ in range(2)]
            or partition["shared_box_boundaries_deliberately_covered_more_than_once"] is not True
            or partition["only_strictly_disjoint_closed_boxes_omitted"] is not True):
        raise ValueError("The original complete cap domain changed")
    by_side = {"upper": {}, "lower": {}}
    for cell in fixed["cap_cells"]:
        side, path = cell["cap"], cell["dyadic_path"]
        if side not in by_side or path in by_side[side] or len(path) != depth:
            raise ValueError("Duplicate or invalid complete cap leaf")
        box = cap_box_from_path(path, radius)
        if (cell["cell_id"] != side+"/"+path
                or cell["parameter_box_xy"] != [[str(a), str(b)] for a, b in box]
                or cell["parameter_domain"] != "This closed box intersected with the unchanged closed cuff disk"
                or minimum_radius_squared(box) > radius*radius):
            raise ValueError("A retained cap domain differs from its real closed disk leaf")
        by_side[side][path] = box
    if set(by_side["upper"]) != set(by_side["lower"]):
        raise ValueError("The two complete caps have different leaf universes")
    retained = set(by_side["upper"])
    if (len(retained) != partition["retained_xy_cells"]
            or 2*len(retained) != fixed["fixed_cap_cells"]):
        raise ValueError("The complete cap partition count changed")
    leaves = set(retained)
    for row in partition["omitted_outside_boxes"]:
        path = row["path"]
        box = cap_box_from_path(path, radius)
        lower = minimum_radius_squared(box)
        if (path in leaves or len(path) > depth or row["depth"] != len(path)
                or row["box"] != [[str(a), str(b)] for a, b in box]
                or q(row["minimum_squared_radius"]) != lower or lower <= radius*radius):
            raise ValueError("An omitted closed cap box has no exact disjointness proof")
        leaves.add(path)
    for path in leaves:
        if any(path[:j] in leaves for j in range(len(path))):
            raise ValueError("The inherited cap leaves overlap by strict ancestry")
    coverage_weight = sum((4**(depth-len(path)) for path in leaves), 0)
    if coverage_weight != 4**depth:
        raise ValueError("The inherited full root square has an unaccounted quadtree region")
    return radius, by_side, dict(
        full_root_square_accounted_for=True, both_closed_disks_accounted_for=True,
        retained_xy_cells=len(retained), omitted_strictly_outside_cells=len(leaves)-len(retained),
        all_leaf_paths_prefix_free=True, exact_four_adic_weight=coverage_weight,
        root_four_adic_weight=4**depth, tangent_and_shared_boundary_points_retained=True)


def marker_definitions(binding, caps):
    markers, seen = [], set()
    for row in binding["marker_definitions"]:
        index = row["index"]
        if index in seen or not isinstance(row["upper"], bool):
            raise ValueError("Malformed actual cap marker identity")
        seen.add(index)
        center = tuple(original_number(x, caps) for x in row["center"])
        radius = original_number(row["radius"], caps)
        height = original_number(row["height"], caps)
        if len(center) != 2 or radius <= 0:
            raise ValueError("Invalid actual marker graph parameters")
        if q(row["exact_graph_derivative_kappa"]) != 8*height/(radius*radius):
            raise ValueError("The marker graph derivative does not match its actual height and radius")
        markers.append(dict(index=index, upper=row["upper"], center=center,
                            radius=radius, height=height))
    return markers


def cap_bounds(cell, markers, caps):
    box = tuple(tuple(map(q, pair)) for pair in cell["parameter_box_xy"])
    own = [m for m in markers if m["upper"] == (cell["cap"] == "upper")]
    touching = [m for m in own
                if caps.minimum_distance_squared(box, m["center"]) <= m["radius"]**2]
    Hessian = sum((8*abs(m["height"])/(m["radius"]**2) for m in touching), F(0))
    gradient = sum((8*abs(m["height"])/m["radius"] for m in touching), F(0))
    d = cell["bound_derivation"]
    halfdiag_squared = sum((((b-a)/2)**2 for a, b in box), F(0))
    planar_radius = q(d["planar_half_diagonal_upper"])
    if (cell["touching_marker_indices"] != [m["index"] for m in touching]
            or q(d["graph_Hessian_operator_upper"]) != Hessian
            or q(d["graph_gradient_norm_upper"]) != gradient
            or q(d["planar_half_diagonal_squared"]) != halfdiag_squared
            or planar_radius < 0 or planar_radius**2 < halfdiag_squared):
        raise ValueError("The cap derivative bound is not its complete actual touching-support sum")
    position = tuple(map(q, cell["fixed_position"]))
    radius = q(cell["fixed_position_radius"])
    if len(position) != 3 or radius < 0:
        raise ValueError("Invalid complete cap position ball")
    # The graph exists on the whole containing rectangle, so the segment
    # from its midpoint is legitimate even if that midpoint is outside disk.
    z_error = gradient*planar_radius
    cartesian = (box[0], box[1], (position[2]-z_error, position[2]+z_error))
    return position, radius, cartesian, Hessian, dict(
        cell_id=cell["cell_id"], cap=cell["cap"],
        graph_Hessian_operator_upper=str(Hessian),
        principal_curvature_absolute_upper=str(Hessian),
        bound_is_nonstrict=True,
        denominator_bound="Q=I+grad(b) grad(b)^T >= I, sqrt(1+|grad(b)|^2) >= 1",
        complete_touching_marker_indices=[m["index"] for m in touching],
        stored_normal_evaluator_kappa_used=False)


def active_curvature_record(row, K):
    out = dict(cell_id=row["cell_id"], ordinal=row["ordinal"],
               actual_closed_domain=[row["closed_radial_interval"],
                                     row["closed_normalized_physical_angle_interval"]],
               piece_kind=row["piece_kind"], sheet=row["sheet"],
               current_K=None if K is None else str(K), paid=False)
    if K is None:
        out["reason"] = "the_actual_active_producer_did_not_request_R279"
        return out
    record = row.get("R279")
    if record is None:
        out.update(reason="no_complete_R279_record_for_this_actual_closed_cell",
                   actual_evaluation_exception=row.get("ball_evaluation_exception"))
        return out
    if q(record["K"]) != K:
        raise ValueError("A closed cell used another proposed curvature bound")
    d = q(row["squared_cross_lower"])
    a, b = interval_record(record["A_K"]), interval_record(record["B_K"])
    paid = d > 0 and a[0] > 0 and b[0] > 0
    if record["strict_curvature_bound"] is not paid:
        raise ValueError("The R279 flag disagrees with its actual strict interval lower bounds")
    out.update(paid=paid, squared_cross_lower=str(d), A_K=record["A_K"], B_K=record["B_K"],
               reason="R279_strict_closed_chart_bound" if paid else "R279_current_enclosure_unresolved",
               unresolved_enclosure_is_not_geometric_failure=True)
    return out


def scale_comparison(bound, tau, K, original, binding):
    D = q(bound["phase_zero_complete_image_diameter_upper"])
    ratio = q(README_RATIO)
    old_D = original["conditional_diameter"]["marked_upper"]
    old_D_exact = F(*old_D.as_integer_ratio()) if isinstance(old_D, float) else F(old_D)
    old_K_value = original["supplied_envelopes"]["curvature"]
    old_K = F(*old_K_value.as_integer_ratio()) if isinstance(old_K_value, float) else F(old_K_value)
    base_value = original["marker_budget"]["required_unmarked_reach"]
    base_tau = F(*base_value.as_integer_ratio()) if isinstance(base_value, float) else F(base_value)
    product = None if K is None else K*tau
    return dict(
        original_marked_tau_exact=str(tau),
        original_marked_tau_binary64=original["marker_budget"]["target_reach"],
        original_marked_tau_reselected=False, README_fraction=str(ratio),
        complete_F0_D_upper=str(D), README_required_reach_upper=str(ratio*D),
        tau_minus_README_required_upper=str(tau-ratio*D),
        original_tau_at_least_3_percent_of_certified_D_upper=(tau >= ratio*D),
        original_cover_marked_D_upper_exact=str(old_D_exact),
        independent_D_upper_no_larger_than_original_cover_D=(D <= old_D_exact),
        whole_closed_chart_K=None if K is None else str(K),
        K_times_original_marked_tau=None if product is None else str(product),
        K_times_tau_lt_one=None if product is None else product < 1,
        K_times_tau_le_one=None if product is None else product <= 1,
        equality_not_silently_changed_to_a_strict_original_gate=True,
        original_unmarked_K_exact=str(old_K),
        original_required_unmarked_tau_exact=str(base_tau),
        original_unmarked_K_times_tau_exact=str(old_K*base_tau),
        original_static_R24_path_unchanged=True,
        original_active_K_matches_supplied_unmarked_K=binding["active_R279_K_matches_original_cover"],
        scope="K*tau only supplies the local curvature-radius budget, conditional on actual C2 gluing; it is not a point-pair, embedding or reach proof")


def run(args):
    require_actions()
    if args.out.exists():
        raise FileExistsError("Use a new output directory")
    if (not 16 <= args.sqrt_bits <= 4096 or args.max_active_cells < 1
            or args.budget_seconds < 1):
        raise ValueError("Invalid explicit resource parameters")
    args.out.mkdir(parents=True)
    large = args.out/"large-arrays"
    large.mkdir()
    events = None
    started = time.monotonic()
    try:
        code = args.code_directory.resolve()
        sources = {}
        for name, expected in SOURCE_PINS.items():
            raw = (code/name).read_bytes()
            if digest(raw) != expected:
                raise ValueError("Frozen defining source changed: "+name)
            sources[name] = dict(bytes=len(raw), sha256=expected)
        mixed = load_bound_module(code/MIXED_NAME, SOURCE_PINS[MIXED_NAME], "_scale_bound_mixed")
        caps = load_bound_module(code/CAP_NAME, SOURCE_PINS[CAP_NAME], "_scale_bound_caps")
        sqrt_upper, inherited_sources = caps.load_sqrt_kernel(code)
        active, fixed, expression, cap_cells, cells_path, tau, binding = mixed.bind_inputs(args)
        original, _ = mixed.read_bound(args.original_cover, args.original_cover_sha256)
        radius, _, partition = verify_cap_partition(fixed, caps)
        markers = marker_definitions(fixed["input_binding"], caps)
        H = original_number(fixed["input_binding"]["cap_height"], caps)
        raw_K = active["parameters"]["curvature_upper"]
        Kactive = None if raw_K is None else q(raw_K)
        if Kactive is not None and Kactive <= 0:
            raise ValueError("The actual R279 proposal must be positive")
        full_binding = dict(
            schema=SCHEMA+"-binding", source_sha256=digest(Path(__file__).read_bytes()),
            direct_sources=sources, inherited_exact_sqrt_and_cap_sources=inherited_sources,
            complete_existing_component_binding=binding,
            exact_finite_expression_identity=expression,
            original_tau_changed=False, original_g_changed=False,
            no_new_native_RHS_J_ODE_FFT_Arb_jet_or_pair_evaluation=True)
        input_file = write_json(large/"input-binding.json.gz", full_binding, compressed=True)
        input_file["file"] = "large-arrays/"+input_file["file"]
        events = EventStream(large/"all-closed-chart-curvature-and-position-domains.jsonl.gz")
        marked = ImageBounds(sqrt_upper, args.sqrt_bits, "original_marked_image")
        unmarked = ImageBounds(sqrt_upper, args.sqrt_bits, "original_unmarked_base_image")
        cap_K = {"upper": F(0), "lower": F(0)}
        for cell in cap_cells:
            c, r, box, k, evidence = cap_bounds(cell, markers, caps)
            marked.add(c, r, box)
            cap_K[cell["cap"]] = max(cap_K[cell["cap"]], k)
            events.write(dict(kind="actual_fixed_cap_closed_cell", **evidence))
        for side in (-1, 1):
            unmarked.add((F(0), F(0), side*H), radius,
                         ((-radius, radius), (-radius, radius), (side*H, side*H)))
        planned = active["planned_closed_cells"]
        count = position_count = R279_count = 0
        stop = None
        for row in mixed.active_rows(cells_path, active, expression):
            if count >= args.max_active_cells or time.monotonic()-started >= args.budget_seconds:
                stop = "resource_budget_before_next_complete_active_cell"
                break
            evidence = active_curvature_record(row, Kactive)
            position_available = "moving_position" in row and "moving_position_radius" in row
            if position_available:
                center = tuple(map(q, row["moving_position"]))
                r = q(row["moving_position_radius"])
                box_record = row.get("position_interval_box")
                box = None if box_record is None else tuple(interval_record(v) for v in box_record)
                marked.add(center, r, box)
                unmarked.add(center, r, box)
                position_count += 1
            evidence.update(
                kind="actual_active_closed_cell", complete_position_bound_available=position_available,
                source_decoded_cell_canonical_sha256=digest(canonical(row)))
            events.write(evidence)
            R279_count += int(evidence["paid"])
            count += 1
        if count == active["exported_closed_cells"] and count != planned and stop is None:
            stop = "actual_active_producer_did_not_export_its_entire_parameter_partition"
        complete = count == planned
        if complete and (active["completed"] is not True or count != active["exported_closed_cells"]):
            raise ValueError("The active completion metadata differs from its full streamed partition")
        all_positions = complete and position_count == planned
        active_curvature_paid = complete and Kactive is not None and R279_count == planned
        all_chart_K = max(Kactive, *cap_K.values()) if active_curvature_paid else None
        position_report = marked.report(all_positions)
        unmarked_report = unmarked.report(all_positions)
        comparisons = None
        if all_positions:
            comparisons = scale_comparison(position_report, tau, all_chart_K, original, binding)
        seams = dict(
            actual_global_C2_seam_certificate_consumed=False,
            global_C2_seams_discharged_here=False,
            available_literal_reflection_trace_records=expression["literal_reflection_trace_conditions"],
            complete_material_density_lower=expression["complete_material_density_lower"],
            same_finite_expression_node_and_patch_identities_bound=True,
            schema_or_position_ball_success_is_not_a_C2_seam_proof=True,
            remaining_responsibilities=[
                "Actual complete shared-node radial seams, including the full cut patch in a legitimate common chart.",
                "Actual reflected prefix seam identities and full common angular/material chart identities.",
                "Actual collar/fixed-cap gluing and marker support away from the shared cuff for the declared entire family."],
            conditional_conclusion="If these actual C2 gluing responsibilities hold, the complete closed-chart bound is the whole-surface principal-curvature bound; R248 then transfers it through the actual image-rotation/fixed-cap family.")
        events.close()
        detail = receipt(events.path)
        detail["file"] = "large-arrays/"+detail["file"]
        result = dict(
            schema=SCHEMA, completed=True, source_sha256=full_binding["source_sha256"],
            input_binding=input_file, complete_cell_records=detail,
            parameters=dict(sqrt_bits=args.sqrt_bits, max_active_cells=args.max_active_cells,
                            budget_seconds=args.budget_seconds),
            complete_two_cap_partition=partition,
            active_coverage=dict(planned_closed_cells=planned, inspected_closed_cells=count,
                complete_parameter_partition_inspected=complete,
                valid_position_domains=position_count,
                unbounded_position_domains=count-position_count,
                unvisited_cell_ordinals=None if complete else [count, planned],
                resource_stop=stop),
            curvature=dict(
                actual_active_proposed_K=None if Kactive is None else str(Kactive),
                active_R279_paid_closed_cells=R279_count,
                active_R279_unresolved_closed_cells=count-R279_count,
                all_active_closed_charts_certified=active_curvature_paid,
                cap_principal_curvature_upper={s:str(v) for s,v in cap_K.items()},
                cap_bound_uses_complete_actual_support_sums_not_nominal_kappa=True,
                all_closed_chart_curvature_bound_certified=active_curvature_paid,
                all_closed_chart_abs_kappa_nonstrict_upper=None if all_chart_K is None else str(all_chart_K),
                cap_nonstrict_bound_not_relabeled_as_strict=True,
                all_phase_chartwise_bound_uses_actual_active_image_rotation_and_fixed_caps=True),
            complete_marked_image_position_cover_certified=all_positions,
            marked_position_enclosures=position_report,
            unmarked_base_position_enclosures=unmarked_report,
            full_surface_D0_upper_certified=all_positions,
            D0_definition="diameter of the entire phase-zero marked closed image F_0(M)",
            D0_not_core_diameter_or_displacement_or_all_phase_supremum=True,
            all_phase_common_bound_is_separate_and_only_a_conservative_bound_for_D0=True,
            original_tau_and_scale_comparison=comparisons,
            actual_seam_responsibility=seams,
            full_surface_curvature_certified=False,
            continuous_reach_interval_certificate=False,
            all_phase_embedding_certified=False,
            held_or_delta_E_certified=False,
            all_domain_relative_metric_certified=False,
            original_solver_refinement_or_acceptance_gates_changed=False,
            original_static_base_R24_and_complete_pair_responsibilities_preserved=True,
            task_completed=False, elapsed_seconds=time.monotonic()-started)
        raw = canonical(result)
        with (args.out/"result.json").open("xb") as stream:
            stream.write(raw)
        print(json.dumps(dict(
            event="same_field_closed_chart_curvature_and_complete_image_scale",
            source_sha256=result["source_sha256"], result_bytes=len(raw), result_sha256=digest(raw),
            active_cells=count, planned_active_cells=planned, complete_two_caps=True,
            all_closed_chart_curvature_bound_certified=active_curvature_paid,
            full_surface_D0_upper_certified=all_positions,
            full_surface_curvature_certified=False, actual_reach_certified=False,
            task_completed=False), sort_keys=True, separators=(",", ":")), flush=True)
        return result
    except BaseException as error:
        if events is not None:
            events.close()
        failure = dict(schema=SCHEMA+"-failure", source_sha256=digest(Path(__file__).read_bytes()),
            exception_type=type(error).__name__, message=str(error),
            full_surface_certified=False, actual_reach_certified=False, task_completed=False)
        if not (args.out/"failure.json").exists():
            write_json(args.out/"failure.json", failure)
        raise
    finally:
        if events is not None:
            events.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("active-result", "fixed-caps", "original-cover"):
        parser.add_argument("--"+name, type=Path, required=True)
        parser.add_argument("--"+name+"-sha256", required=True)
    parser.add_argument("--code-directory", type=Path, default=HERE)
    parser.add_argument("--sqrt-bits", type=int, default=128)
    parser.add_argument("--max-active-cells", type=int, default=1_000_000)
    parser.add_argument("--budget-seconds", type=int, default=3600)
    parser.add_argument("--out", type=Path, required=True)
    run(parser.parse_args())


if __name__ == "__main__":
    main()
