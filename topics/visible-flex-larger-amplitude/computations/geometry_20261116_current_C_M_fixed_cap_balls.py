#!/usr/bin/env python3
"""R451 current finite-M fixed-cap Cartesian six-jets and exact rational balls.

Consume the actual unchanged R409 seven-tuple and its R413 target attachment.
The old fixed-cap binder/main is never called.  Only its pure disk_partition,
graph_at and cap_cell are reused, with indices explicitly derived from the
current complete marker-list order and graph_kappa=8*A/R**2.  The original
sqrt_upper is loaded directly, without the old source/geometry binder.

All actual interval arithmetic is public-Actions-only.  This requestless API
does not produce an accepted BVP, moving cover, full metric/reach/held result,
or any claim about binary64 rendering error.  No scientific execution occurred
in preparing this source or its conditional proof.
Author: OpenAI / ChatGPT amplitude agent, 2026-11-15.
"""
from __future__ import annotations

import copy
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import struct
import sys

REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "R451-current-C-complete-M-fixed-cap-rational-six-jets-and-balls-v1"
CELL_SCHEMA = SCHEMA + "-cell"
SHARED_NAME = "geometry_20261116_current_C_ten_M_shared_field.py"
SHARED_SHA = "db1f6fd39bef3d9ce2543276771cbcea1c2432a7221b8f295ed5b553b2171f87"
SHARED_SCHEMA = "R442-current-C-frozen-M-shared-background-complete-field-v1"
ATLAS_NAME = "geometry_20261116_current_C_M_original_cuff_atlas.py"
ATLAS_SHA = "97e4a49f0a9913094dec5f78b173437028f553a5bf0aa36f0b0b9d53929a9621"
ATLAS_SCHEMA = "R451-current-C-complete-M-original-cuff-target-atlas-binding-v1"
CAP_NAME = "geometry_20261115_fixed_cap_rational_balls.py"
CAP_SHA = "a3ada50b5389a075f1da2d2237269a1a1ccc83c29aa35bc889d721eac0e2552e"
SQRT_NAME = "root_mixed_phase_normal_balls.py"
SQRT_SHA = "ecea0ef58aa5755270807596da5512552ac52fab27e90492fcf85fab095716c6"
SOURCE_PINS = {SHARED_NAME: SHARED_SHA, ATLAS_NAME: ATLAS_SHA,
               CAP_NAME: CAP_SHA, SQRT_NAME: SQRT_SHA}
JET_NAMES = ("value", "x", "y", "xx", "xy", "yy")


def actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("Run this exact cap arithmetic only in the named public Actions")


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False) + "\n").encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def receipt(path):
    path = Path(path)
    raw = path.read_bytes()
    return dict(file=path.name, bytes=len(raw), sha256=sha(raw))


def exact(value):
    if type(value) is bool:
        raise ValueError("A Boolean is not an exact coordinate")
    if isinstance(value, Q):
        return value
    if type(value) is int:
        return Q(value)
    if type(value) is float and math.isfinite(value):
        return Q.from_float(value)
    if type(value) is str:
        return Q(value)
    raise ValueError("Use an exact rational or a finite original binary64 word")


def original_word(value):
    if type(value) not in (int, float) or not math.isfinite(value):
        raise ValueError("The current plan needs its original finite numeric word")
    return struct.pack("<d", float(value)).hex()


def equal_literal(a, b):
    return canonical(a) == canonical(b)


def frozen_module(directory, name, expected, module_name):
    path = (Path(directory) / name).resolve()
    row = receipt(path)
    if row["sha256"] != expected:
        raise ValueError("The actual defining or pure-kernel source differs: " + name)
    for module in tuple(sys.modules.values()):
        other = getattr(module, "__file__", None)
        if other is not None and Path(other).resolve() == path:
            return module, row
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError("Cannot load the pinned source: " + name)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        sys.modules.pop(module_name, None)
        raise
    return module, row


def actual_shared_module(directory, assembly):
    """Bind the class which really owns A, not the first same-path module.

    R416 may load the frozen R409 file under its own module name after another
    consumer has already loaded that path.  Equal source bytes do not make
    separately created Python class objects identical.
    """
    path = (Path(directory) / SHARED_NAME).resolve()
    row = receipt(path)
    cls = type(assembly)
    module = sys.modules.get(cls.__module__)
    actual_file = getattr(module, "__file__", None)
    if (row["sha256"] != SHARED_SHA or module is None
            or actual_file is None or Path(actual_file).resolve() != path
            or getattr(module, "CurrentSharedAssembly", None) is not cls):
        raise ValueError("The live assembly class is not owned by its actual pinned R409 module")
    return module, row


# Closed rational intervals.  No endpoints are formed through float/decimal
# midpoint conversion, and every signed marker is retained in every sum.
def iv(lo, hi=None):
    lo = exact(lo)
    hi = lo if hi is None else exact(hi)
    if lo > hi:
        raise ValueError("Reversed closed rational interval")
    return (lo, hi)


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def neg(a):
    return (-a[1], -a[0])


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    values = (a[0]*b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1])
    return (min(values), max(values))


def scale(a, c):
    return mul(a, iv(c))


def square(a):
    if a[0] <= 0 <= a[1]:
        return (Q(0), max(a[0]*a[0], a[1]*a[1]))
    return (min(a[0]*a[0], a[1]*a[1]), max(a[0]*a[0], a[1]*a[1]))


def positive_part(a):
    return (max(Q(0), a[0]), max(Q(0), a[1]))


def nonnegative_power(a, n):
    if type(n) is not int or n < 0 or a[0] < 0:
        raise ValueError("A nonnegative interval and integer power are required")
    return (a[0]**n, a[1]**n)


def reciprocal_positive(a):
    if a[0] <= 0:
        raise ValueError("The proved positive interval denominator is required")
    return (1/a[1], 1/a[0])


def encode(a):
    return dict(lower=str(a[0]), upper=str(a[1]))


def encode_vector(v):
    return [encode(a) for a in v]


def sqrt_interval(a, kernel, bits):
    if a[0] < 0:
        raise ValueError("A nonnegative exact interval is required")
    upper = kernel(a[1], bits)
    if not a[0]:
        lower = Q(0)
    else:
        lower = a[0]/kernel(a[0], bits)
    return (lower, upper)


def graph_six_jets(box, markers):
    """Enclose b,bx,by,bxx,bxy,byy on the whole rectangle.

    The formulas are globally valid for t_+**4, including t=0, since this
    one-variable function is C3.  This is not differentiating the max branch
    with a falsely smooth max derivative.
    """
    x, y = box
    out = [iv(0) for _ in JET_NAMES]
    for row in markers:
        dx, dy = sub(x, iv(row["center"][0])), sub(y, iv(row["center"][1]))
        R2 = row["radius"]**2
        A = row["amplitude"]
        t = positive_part(sub(iv(1), scale(add(square(dx), square(dy)), 1/R2)))
        t2, t3, t4 = (nonnegative_power(t, n) for n in (2, 3, 4))
        k = -8*A/R2
        h = 48*A/(R2*R2)
        values = (
            scale(t4, A),
            scale(mul(dx, t3), k),
            scale(mul(dy, t3), k),
            add(scale(t3, k), scale(mul(square(dx), t2), h)),
            scale(mul(mul(dx, dy), t2), h),
            add(scale(t3, k), scale(mul(square(dy), t2), h)))
        out = [add(a, b) for a, b in zip(out, values)]
    return tuple(out)


def geometric_six_jets(box, height, side, graph):
    b, bx, by, bxx, bxy, byy = graph
    zero, one = iv(0), iv(1)
    return dict(
        value=encode_vector((box[0], box[1], scale(add(iv(height), b), side))),
        x=encode_vector((one, zero, scale(bx, side))),
        y=encode_vector((zero, one, scale(by, side))),
        xx=encode_vector((zero, zero, scale(bxx, side))),
        xy=encode_vector((zero, zero, scale(bxy, side))),
        yy=encode_vector((zero, zero, scale(byy, side))))


def curvature_and_normal(graph, side, sqrt_upper, bits, Hessian_upper):
    _, bx, by, bxx, bxy, byy = graph
    one = iv(1)
    gxx, gxy, gyy = add(one, square(bx)), mul(bx, by), add(one, square(by))
    area2 = add(add(one, square(bx)), square(by))
    area = sqrt_interval(area2, sqrt_upper, bits)
    inv_area, inv_area2 = reciprocal_positive(area), reciprocal_positive(area2)
    metric = ((gxx, gxy), (gxy, gyy))
    Hessian = ((bxx, bxy), (bxy, byy))
    second = tuple(tuple(mul(a, inv_area) for a in row) for row in Hessian)
    inverse_metric = ((mul(gyy, inv_area2), neg(mul(gxy, inv_area2))),
                      (neg(mul(gxy, inv_area2)), mul(gxx, inv_area2)))
    shape = tuple(tuple(
        add(mul(inverse_metric[i][0], second[0][j]),
            mul(inverse_metric[i][1], second[1][j]))
        for j in range(2)) for i in range(2))
    mean_num = add(sub(mul(gyy, bxx), scale(mul(gxy, bxy), 2)), mul(gxx, byy))
    mean = scale(mul(mean_num, reciprocal_positive(mul(area2, area))), Q(1, 2))
    gaussian = mul(sub(mul(bxx, byy), square(bxy)),
                   reciprocal_positive(nonnegative_power(area2, 2)))
    normal = (mul(neg(bx), inv_area), mul(neg(by), inv_area), scale(inv_area, side))
    return dict(
        induced_metric=[[encode(a) for a in row] for row in metric],
        exact_metric_definition="I+Db_side tensor Db_side",
        squared_area_density=encode(area2),
        squared_area_density_exact_lower_at_least_one=True,
        unit_normal=encode_vector(normal),
        normal_definition="(-bx,-by,side)/sqrt(1+bx^2+by^2)",
        oriented_second_fundamental_form=[[encode(a) for a in row] for row in second],
        second_form_convention="II_ij = unit_normal dot F_ij = b_ij/sqrt(1+|Db|^2)",
        shape_operator=[[encode(a) for a in row] for row in shape],
        shape_operator_convention="g^{-1} II; principal curvatures are its real eigenvalues",
        mean_curvature=encode(mean), Gaussian_curvature=encode(gaussian),
        both_principal_curvature_absolute_upper=str(Hessian_upper),
        principal_bound_uses_symmetric_g_inverse_half_conjugation=True,
        complete_surface_curvature_or_reach_bound=False)


def dyadic_box(cuff, path):
    if not isinstance(path, str) or any(c not in "0123" for c in path):
        raise ValueError("Use the complete original Cartesian quadtree path")
    x, y = (-cuff, cuff), (-cuff, cuff)
    for c in path:
        xm, ym = (x[0]+x[1])/2, (y[0]+y[1])/2
        if c in "01":
            y = (y[0], ym)
        else:
            y = (ym, y[1])
        if c in "02":
            x = (x[0], xm)
        else:
            x = (xm, x[1])
    return (x, y)


class CurrentTenFixedCaps:
    """A separate bound consumer; never mutate the existing seven objects."""
    def __init__(self, bundle, atlas, attachment, computations):
        actions()
        if not isinstance(bundle, (tuple, list)) or len(bundle) != 7:
            raise ValueError("Use the actual complete unchanged R409 seven-tuple")
        paths, plan, assembly, target, saved, A, bindings = bundle
        Shared, shared_row = actual_shared_module(computations, A)
        Atlas, atlas_row = frozen_module(computations, ATLAS_NAME, ATLAS_SHA,
                                         "_R417_original_C_cuff")
        self.cap, cap_row = frozen_module(computations, CAP_NAME, CAP_SHA,
                                          "_R417_pure_old_cap")
        sqrt, sqrt_row = frozen_module(computations, SQRT_NAME, SQRT_SHA,
                                       "_R417_pure_sqrt")
        self.sqrt_upper = sqrt.sqrt_upper
        current_attachment = Atlas.bind_loaded_shared_bundle(bundle, atlas)
        if (not equal_literal(current_attachment, attachment)
                or attachment.get("schema") != ATLAS_SCHEMA + "-same-field-attachment"
                or attachment.get("exact_original_cuff_target_twojet_compatibility") is not True
                or not isinstance(A, Shared.CurrentSharedAssembly)
                or A.saved is not saved or A.plan is not plan
                or not equal_literal(A.shared_background_geometry,
                                     plan["shared_background_geometry"])
                or assembly["mean_gauge"]["whole_lower_sheet_reflected"] is not True
                or assembly["core_and_hold_gauge"]["native_cap_rotation_axis_xy"] != [0., 0.]):
            raise ValueError("This cap consumer and the actual R409/R413 owners differ")
        cuff, height = exact(plan["cuff"]), exact(plan["cap_height"])
        if (cuff <= 0 or original_word(A.cuff) != original_word(plan["cuff"])
                or exact(A.shared_background.radii[0]) != cuff
                or exact(A.shared_background.nodal[0][0]) != height):
            raise ValueError("Retain the exact actual cap radius and original height datum")
        rows = plan["fixed_cap"]["markers"]
        if (not isinstance(rows, list)
                or len(rows) != atlas["fixed_caps"]["marker_count"]
                or atlas["fixed_caps"]["cap_height_exact"] != str(height)):
            raise ValueError("Keep the complete cap list and the R413 original height")
        markers, original_rows, marker_binding = [], copy.deepcopy(rows), []
        for index, row in enumerate(rows):
            if (not isinstance(row, dict) or set(row) != {"upper", "center", "radius", "height"}
                    or type(row["upper"]) is not bool
                    or not isinstance(row["center"], list) or len(row["center"]) != 2):
                raise ValueError("A current marker has only its actual four R409 fields")
            for value in row["center"] + [row["radius"], row["height"]]:
                original_word(value)
            center = tuple(exact(x) for x in row["center"])
            radius, amplitude = exact(row["radius"]), exact(row["height"])
            if not 0 < radius < cuff or sum(x*x for x in center) >= (cuff-radius)**2:
                raise ValueError("The unchanged R409 strict inside-support condition differs")
            markers.append(dict(index=index, upper=row["upper"], center=center,
                                radius=radius, amplitude=amplitude,
                                graph_kappa=8*amplitude/(radius*radius)))
            marker_binding.append(dict(
                current_marker_list_index=index, upper=row["upper"],
                center_exact=list(map(str, center)), radius_exact=str(radius),
                amplitude_exact=str(amplitude), derived_graph_kappa=str(8*amplitude/(radius*radius)),
                original_float64le=[original_word(x) for x in
                                    row["center"] + [row["radius"], row["height"]]],
                index_is_original_list_position_not_a_legacy_field=True,
                stored_legacy_kappa_consumed=False))
        self.cuff, self.height, self.markers = cuff, height, tuple(markers)
        self.sources = {SHARED_NAME: shared_row, ATLAS_NAME: atlas_row,
                        CAP_NAME: cap_row, SQRT_NAME: sqrt_row,
                        Path(__file__).name: receipt(__file__)}
        self.binding = dict(
            schema=SCHEMA + "-same-field-binding",
            source=receipt(__file__), direct_sources=copy.deepcopy(self.sources),
            current_original_shared_binding_sha256=sha(canonical(bindings)),
            original_shared_binding=copy.deepcopy(bindings),
            original_shared_files={key: receipt(path) for key, path in paths.items()},
            R413_atlas_sha256=sha(Atlas.canonical(atlas)),
            R413_attachment=copy.deepcopy(current_attachment),
            original_cuff=copy.deepcopy(atlas["original_cuff"]),
            exact_height=str(height), original_cap_height_word=original_word(plan["cap_height"]),
            renderer_height_word=original_word(A.cap_height),
            renderer_height_minus_exact_datum=str(exact(A.cap_height)-height),
            renderer_height_projection_not_a_new_geometry_gate=True,
            fixed_cap_definition_sha256=sha(canonical(plan["fixed_cap"])),
            original_marker_rows=original_rows, markers=marker_binding,
            inherited_cap_flat_inner_annulus=copy.deepcopy(atlas["fixed_caps"]["complete_flat_inner_annulus"]),
            original_complete_ten_target=copy.deepcopy(target["complete_current_ten_target"]),
            exact_cap_definition="F_side(x,y)=(x,y,side*(H+b_side(x,y)))",
            no_current_profile_or_target_parameter_replaced=True,
            graph_derivatives_not_stored_renderer_kappa=True,
            same_original_material_Cartesian_frame_no_phase_rotation=True,
            original_seven_tuple_and_its_unpaid_flags_unchanged=True,
            full_field_arrays_and_acceptance_owned_by_original_R400_R409_loaders=True,
            old_cap_main_bind_geometry_and_load_sqrt_kernel_called=False,
            new_native_or_BVP_acceptance=False)
        self.binding_sha256 = sha(canonical(self.binding))

    def describe(self):
        return copy.deepcopy(self.binding)

    def cell(self, path, upper, sqrt_bits=128):
        actions()
        if type(upper) is not bool or type(sqrt_bits) is not int or not 16 <= sqrt_bits <= 4126:
            raise ValueError("Use the actual cap side and explicit rational sqrt precision")
        box = dyadic_box(self.cuff, path)
        if self.cap.minimum_distance_squared(box, (Q(0), Q(0))) > self.cuff*self.cuff:
            raise ValueError("This closed quadtree box is strictly outside the original disk")
        own = [row for row in self.markers if row["upper"] is upper]
        # cap_cell and graph_at are original pure functions, unchanged.
        balls = self.cap.cap_cell(path, box, upper, self.height, self.markers,
                                  self.sqrt_upper, sqrt_bits)
        graph = graph_six_jets(box, own)
        side = 1 if upper else -1
        Hbound = exact(balls["bound_derivation"]["graph_Hessian_operator_upper"])
        return dict(
            schema=CELL_SCHEMA, source_sha256=self.sources[Path(__file__).name]["sha256"],
            same_field_binding_sha256=self.binding_sha256,
            original_ball_record=balls,
            Cartesian_six_jets=geometric_six_jets(box, self.height, side, graph),
            graph_six_jets={name:encode(value) for name,value in zip(JET_NAMES,graph)},
            curvature=curvature_and_normal(graph, side, self.sqrt_upper, sqrt_bits, Hbound),
            all_current_side_markers_summed=True,
            C3_positive_part_makes_second_derivatives_valid_at_support_boundary=True,
            parameter_rectangle_enclosures_also_cover_its_closed_disk_intersection=True,
            exact_cap_target_relative_metric_error_zero_by_definition=True,
            accurate_active_target_metric_unpaid=True,
            finite_renderer_rounding_error_enclosed=False,
            full_surface_or_reach_or_held_certified=False)

    def cover(self, depth, sqrt_bits=128, max_cells=1000000, budget_check=None):
        """Complete two-cap cover, or an explicit actual unfinished suffix.

        budget_check, if supplied, is the caller's resource/interruption check.
        It receives no mathematical residual and introduces no acceptance test.
        All detailed cells are returned only for current Actions temporary use;
        no CLI transport, artifact upload, split encoding or cleanup is added.
        """
        actions()
        if (type(depth) is not int or not 0 <= depth <= 30
                or type(sqrt_bits) is not int or not 16 <= sqrt_bits <= 4096
                or type(max_cells) is not int or max_cells < 2
                or 2*4**depth > max_cells
                or (budget_check is not None and not callable(budget_check))):
            raise ValueError("The explicit worst-case two-cap grid/precision budget is unavailable")
        result = dict(
            schema=SCHEMA, source=receipt(__file__), source_pins=copy.deepcopy(self.sources),
            input_binding=self.describe(),
            parameters=dict(depth=depth, sqrt_bits_base=sqrt_bits,
                            effective_sqrt_bits=sqrt_bits+depth, max_cells=max_cells),
            completed=False, partition_completed=False, cap_cells=[], error=None,
            cap_order=["upper","lower"], complete_two_cap_six_jets_balls_curvature=False,
            explicit_interval_execution=True, phase_sampling_used=False,
            all_phase_fixed_caps_identical=True, no_new_scientific_acceptance_gate=True,
            exact_original_cuff_target_attachment_retained=True,
            complete_active_sheet_or_pair_cover=False, whole_surface_metric_proved=False,
            full_surface_curvature_or_reach_or_held_proved=False,
            finite_renderer_rounding_error_enclosed=False, new_BVP_or_native_acceptance=False,
            task_completed=False)
        retained = None
        cursor = 0
        try:
            if budget_check is not None:
                budget_check()
            retained, omitted = self.cap.disk_partition(self.cuff, depth)
            paths = [path for path, box in retained]
            result.update(partition_completed=True, exact_closed_disk_partition=dict(
                radius=str(self.cuff), root_box=[[str(-self.cuff),str(self.cuff)]]*2,
                retained_paths=paths, retained_xy_cells=len(paths),
                omitted_outside_boxes=omitted,
                only_strictly_disjoint_closed_boxes_omitted=True,
                shared_closed_edges_deliberately_overlapped=True),
                planned_fixed_cap_cells=2*len(paths))
            for upper in (True, False):
                for path in paths:
                    if budget_check is not None:
                        budget_check()
                    row = self.cell(path, upper, sqrt_bits+depth)
                    result["cap_cells"].append(row)
                    cursor += 1
            result.update(completed=True, complete_two_cap_six_jets_balls_curvature=True,
                          completed_fixed_cap_cells=cursor, pending=None)
        except BaseException as error:
            result["error"] = dict(type=type(error).__name__, message=str(error))
            result["actual_exception_class"] = type(error).__name__
            result["completed_fixed_cap_cells"] = cursor
            if retained is None:
                result["pending"] = dict(entire_upper_and_lower_closed_disks=True,
                    exact_partition_not_returned=True)
            else:
                total = 2*len(retained)
                next_side = "upper" if cursor < len(retained) else "lower"
                next_path = retained[cursor % len(retained)][0] if cursor < total else None
                result["pending"] = dict(
                    concatenated_cap_order_then_retained_path_indices_half_open=[cursor,total],
                    next_cap=next_side if cursor < total else None, next_path=next_path,
                    every_remaining_address_explicitly_defined_by_returned_path_list=True,
                    unchanged_parameter_domain="both original closed cuff disks",
                    no_unfinished_cell_claimed_complete=True)
        return result


def bind_loaded_shared_bundle(bundle, atlas, attachment, computations):
    """Return an independent API object; do not replace any R409 tuple member."""
    return CurrentTenFixedCaps(bundle, atlas, attachment, computations)
