#!/usr/bin/env python3
"""Exact continuous balls for the two fixed caps of one bound shared-B field.

This consumes an actual existing plan/assembly; it never manufactures a field.
Only the inherited RefinedAssembly.cap graph is certified here.  Moving cells,
mixed pair enumeration, curvature of the whole surface, R241, held, same-g and
reach remain outside this producer.  In particular this is not a replacement
for the original static-base/R24 cover or a new native acceptance condition.

Run scientific arithmetic only in the named public repository's Actions.
Complete output is temporary/recomputable under repository rule 15.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import struct


HERE = Path(__file__).resolve().parent
REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "same-shared-field-two-fixed-cap-rational-balls-v1"
PLAN_SCHEMA = "shared-background-complete-material-finite-closed-plan-v1"
ASSEMBLY_SCHEMA = "shared-background-complete-material-finite-closed-assembly-v1"
SOURCE_PINS = {
    "root_mixed_phase_normal_balls.py":
        "ecea0ef58aa5755270807596da5512552ac52fab27e90492fcf85fab095716c6",
    "exact_20261114_refined_tail_adapter.py":
        "6b06db6c7c96078b9fabe403a0b3ade14f8b30b07a78b565ed299c77f840d937",
    "geometry_20261114_large_core_closed_assembly.py":
        "e70d27a92bf153e49e50016706db854b339d96d3414d7f4c00a5993e1f7609c0",
    "geometry_20261114_shared_background_closed_assembly.py":
        "ac635c11aa31925a4175876ffa2c8b959766629aebf9e3abaf97a68ca0e096cb",
}


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("Scientific arithmetic is restricted to this public repository's Actions")


def sha_bytes(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical_sha(value):
    return sha_bytes(json.dumps(value, sort_keys=True, separators=(",", ":"),
                               allow_nan=False).encode())


def unique_object(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError("Duplicate JSON key: " + key)
        out[key] = value
    return out


def read_bound(path, expected):
    raw = Path(path).read_bytes()
    digest = sha_bytes(raw)
    if digest != expected:
        raise ValueError("The supplied actual input changed: " + str(path))
    decoded = gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw
    value = json.loads(decoded, object_pairs_hook=unique_object,
                       parse_constant=lambda text: (_ for _ in ()).throw(
                           ValueError("Nonfinite JSON token: " + text)))
    return value, dict(file=Path(path).name, bytes=len(raw), sha256=digest,
                       decoded_bytes=len(decoded), decoded_sha256=sha_bytes(decoded))


def exact_stored(value):
    """Interpret the original JSON number exactly as its stored binary64 value.

    A decimal-looking JSON float is NOT reinterpreted as an exact decimal.
    Integer tokens are exact integers.  Input strings are not source parameters.
    """
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("Expected an actual source-plan finite JSON number")
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError("Nonfinite source parameter")
        return F(*value.as_integer_ratio())
    return F(value)


def original_number(value):
    return dict(original_json_number=value, exact=str(exact_stored(value)),
                float64le_hex=(struct.pack("<d", value).hex()
                               if isinstance(value, float) else None))


def load_sqrt_kernel(source_directory):
    receipts = {}
    for name, expected in SOURCE_PINS.items():
        path = Path(source_directory) / name
        raw = path.read_bytes()
        if sha_bytes(raw) != expected:
            raise ValueError("A frozen defining/kernel source changed: " + name)
        receipts[name] = dict(bytes=len(raw), sha256=expected)
    path = Path(source_directory) / "root_mixed_phase_normal_balls.py"
    spec = importlib.util.spec_from_file_location("fixed_cap_exact_sqrt_kernel", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.sqrt_upper, receipts


def bind_geometry(args):
    plan, plan_receipt = read_bound(args.plan, args.plan_sha256)
    assembly, assembly_receipt = read_bound(args.assembly, args.assembly_sha256)
    if (plan.get("schema") != PLAN_SCHEMA or assembly.get("schema") != ASSEMBLY_SCHEMA
            or plan.get("finished") is not True or assembly.get("finished") is not True):
        raise ValueError("This thin producer consumes the actual existing shared-B plan/assembly schemas")
    if assembly["inputs"]["plan"]["sha256"] != plan_receipt["sha256"]:
        raise ValueError("The actual shared assembly references another plan")
    geometry = plan["shared_background_geometry"]
    if geometry != assembly["shared_background_geometry"]:
        raise ValueError("The plan and assembly identify different finite fields")
    if geometry["wrapper_sha256"] != SOURCE_PINS["geometry_20261114_shared_background_closed_assembly.py"]:
        raise ValueError("Unsupported shared-field defining source")
    if geometry["fixed_cap_definition_sha256"] != canonical_sha(plan["fixed_cap"]):
        raise ValueError("The original fixed-cap definition changed")
    if assembly["mean_gauge"]["whole_lower_sheet_reflected"] is not True:
        raise ValueError("The source graph's lower-cap reflection is not the declared one")
    height = exact_stored(assembly["mean_gauge"]["upper_cap_height"])
    if height != exact_stored(geometry["original_cap_height"]):
        raise ValueError("A new cap-height gauge was introduced")
    cuff = exact_stored(plan["cuff"])
    if cuff <= 0:
        raise ValueError("The inherited source requires a positive cap radius")
    # Any finite original H is valid for these local graph balls.  Separation
    # of the two caps and the whole-surface geometry remain the original gates.
    markers, definitions, seen = [], [], set()
    for row in plan["fixed_cap"]["markers"]:
        if not isinstance(row["upper"], bool) or len(row["center"]) != 2:
            raise ValueError("Malformed inherited marker row")
        key = row["index"]
        if isinstance(key, bool) or not isinstance(key, int) or key in seen:
            raise ValueError("Marker indices must be distinct integers")
        seen.add(key)
        center = tuple(exact_stored(x) for x in row["center"])
        radius, amplitude = exact_stored(row["radius"]), exact_stored(row["height"])
        if radius <= 0:
            raise ValueError("A marker support radius is not positive")
        graph_kappa = 8*amplitude/(radius*radius)
        marker = dict(index=key, upper=row["upper"], center=center,
                      radius=radius, amplitude=amplitude, graph_kappa=graph_kappa)
        markers.append(marker)
        nominal = exact_stored(row["kappa"])
        definitions.append(dict(index=key, upper=row["upper"],
            center=[original_number(x) for x in row["center"]],
            radius=original_number(row["radius"]), height=original_number(row["height"]),
            stored_normal_evaluator_kappa=original_number(row["kappa"]),
            exact_graph_derivative_kappa=str(graph_kappa),
            stored_kappa_equals_graph_derivative=(nominal == graph_kappa),
            stored_kappa_minus_graph_derivative=str(nominal-graph_kappa),
            support_strictly_inside_own_cap=(cuff > radius and
                sum(x*x for x in center) < (cuff-radius)**2)))
    binding = dict(plan=plan_receipt, assembly=assembly_receipt,
        shared_background_geometry=geometry,
        fixed_cap_definition_sha256=canonical_sha(plan["fixed_cap"]),
        cap_height=original_number(assembly["mean_gauge"]["upper_cap_height"]),
        cuff=original_number(plan["cuff"]), marker_definitions=definitions,
        common_rotation_axis_xy=["0", "0"],
        coordinate_frame="Original canonical cap frame; no transform, normalization, reflection change or new fit",
        recorded_registration_sha256=geometry["recorded_single_global_planar_registration_sha256"],
        definition="(x,y,+/-[H+sum A_j max(0,1-|xy-c_j|^2/R_j^2)^4]) on x^2+y^2<=cuff^2",
        renderer_cap_positions_recomputed=False,
        stored_normal_evaluator_kappa_used_as_derivative=False,
        original_target_metric_changed=False)
    return cuff, height, markers, binding


def minimum_distance_squared(box, point):
    total = F(0)
    for (lo, hi), value in zip(box, point):
        gap = lo-value if value < lo else value-hi if value > hi else F(0)
        total += gap*gap
    return total


def disk_partition(radius, depth):
    """Closed quadtree boxes, including tangent boxes; no circle sampling."""
    retained, omitted = [], []
    stack = [("", ((-radius, radius), (-radius, radius)), 0)]
    while stack:
        path, box, level = stack.pop()
        lower = minimum_distance_squared(box, (F(0), F(0)))
        if lower > radius*radius:
            omitted.append(dict(path=path, depth=level,
                box=[[str(x) for x in interval] for interval in box],
                minimum_squared_radius=str(lower),
                reason="closed_box_is_strictly_outside_the_original_closed_disk"))
            continue
        if level == depth:
            retained.append((path, box))
            continue
        (xl, xh), (yl, yh) = box
        xm, ym = (xl+xh)/2, (yl+yh)/2
        children = [((xl, xm), (yl, ym)), ((xm, xh), (yl, ym)),
                    ((xl, xm), (ym, yh)), ((xm, xh), (ym, yh))]
        for index in range(3, -1, -1):
            stack.append((path+str(index), children[index], level+1))
    return retained, omitted


def graph_at(point, markers):
    height, gradient = F(0), [F(0), F(0)]
    for row in markers:
        displacement = [point[i]-row["center"][i] for i in range(2)]
        u = sum(v*v for v in displacement)/(row["radius"]**2)
        if u >= 1:
            continue
        v = 1-u
        height += row["amplitude"]*v**4
        for i in range(2):
            gradient[i] -= row["graph_kappa"]*displacement[i]*v**3
    return height, gradient


def cap_cell(path, box, upper, height, markers, sqrt_upper, bits):
    own = [row for row in markers if row["upper"] is upper]
    touching = [row for row in own
                if minimum_distance_squared(box, row["center"]) <= row["radius"]**2]
    center = tuple((lo+hi)/2 for lo, hi in box)
    planar_radius_squared = sum(((hi-lo)/2)**2 for lo, hi in box)
    planar_radius = sqrt_upper(planar_radius_squared, bits)
    gradient_upper = sum((8*abs(row["amplitude"])/row["radius"] for row in touching), F(0))
    Hessian_upper = sum((8*abs(row["amplitude"])/(row["radius"]**2) for row in touching), F(0))
    graph_height, gradient = graph_at(center, own)
    side = 1 if upper else -1
    position = (center[0], center[1], side*(height+graph_height))
    numerator = (-gradient[0], -gradient[1], F(side))
    normal_squared = sum(v*v for v in numerator)
    normal_length_upper = sqrt_upper(normal_squared, bits)
    normal_center = tuple(v/normal_length_upper for v in numerator)
    # sqrt(s) >= s/L+, so 1-s/(L+)^2 bounds the exact normalization error.
    normal_center_error = 1-normal_squared/(normal_length_upper**2)
    position_radius = planar_radius*sqrt_upper(1+gradient_upper**2, bits)
    normal_variation = Hessian_upper*planar_radius
    normal_radius = normal_variation+normal_center_error
    return dict(cell_id=("upper/" if upper else "lower/")+path,
        cap="upper" if upper else "lower", phase_motion="fixed",
        dyadic_path=path, parameter_box_xy=[[str(v) for v in interval] for interval in box],
        parameter_domain="This closed box intersected with the unchanged closed cuff disk",
        center_need_not_be_a_point_of_the_intersection=True,
        fixed_position=list(map(str, position)), fixed_position_radius=str(position_radius),
        fixed_normal_centre=list(map(str, normal_center)), fixed_normal_radius=str(normal_radius),
        normal_orientation="Upward upper cap; downward reflected lower cap",
        touching_marker_indices=[row["index"] for row in touching],
        bound_derivation=dict(planar_half_diagonal_squared=str(planar_radius_squared),
            planar_half_diagonal_upper=str(planar_radius),
            graph_gradient_norm_upper=str(gradient_upper),
            graph_Hessian_operator_upper=str(Hessian_upper),
            exact_center_graph_gradient=list(map(str, gradient)),
            exact_normal_numerator=list(map(str, numerator)),
            exact_normal_numerator_squared=str(normal_squared),
            normal_length_upper=str(normal_length_upper),
            normal_center_normalization_error_upper=str(normal_center_error),
            normal_variation_upper=str(normal_variation),
            sqrt_bits=bits))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--plan-sha256", required=True)
    parser.add_argument("--assembly", type=Path, required=True)
    parser.add_argument("--assembly-sha256", required=True)
    parser.add_argument("--source-directory", type=Path, default=HERE)
    parser.add_argument("--depth", type=int, required=True)
    parser.add_argument("--sqrt-bits", type=int, default=128)
    parser.add_argument("--max-cells", type=int, default=1_000_000)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    require_actions()
    if args.out.exists():
        raise FileExistsError("Refusing to replace an existing output")
    if args.depth < 0 or not 16 <= args.sqrt_bits <= 4096 or args.max_cells < 2:
        raise ValueError("Invalid declared resource/precision parameters")
    # This is an explicit worst-case resource limit, not a geometric test.
    if args.depth > 30 or 2*4**args.depth > args.max_cells:
        raise ValueError("Requested full two-cap grid exceeds the explicit cell budget; no geometry conclusion")
    sqrt_upper, sources = load_sqrt_kernel(args.source_directory)
    cuff, height, markers, binding = bind_geometry(args)
    retained, omitted = disk_partition(cuff, args.depth)
    bits = args.sqrt_bits+args.depth
    cells = [cap_cell(path, box, upper, height, markers, sqrt_upper, bits)
             for upper in (True, False) for path, box in retained]
    result = dict(schema=SCHEMA, completed=True, source_sha256=sha_bytes(Path(__file__).read_bytes()),
        source_pins=sources, input_binding=binding,
        parameters=dict(depth=args.depth, sqrt_bits_base=args.sqrt_bits,
            effective_sqrt_bits=bits, precision_rule="base_bits+depth", max_cells=args.max_cells),
        exact_closed_disk_partition=dict(radius=str(cuff),
            root_box=[[str(-cuff), str(cuff)] for _ in range(2)],
            retained_xy_cells=len(retained), omitted_outside_boxes=omitted,
            shared_box_boundaries_deliberately_covered_more_than_once=True,
            only_strictly_disjoint_closed_boxes_omitted=True),
        cap_cells=cells, fixed_cap_cells=len(cells),
        complete_two_fixed_cap_position_and_unit_normal_balls=True,
        mathematical_field_defined_by_exact_stored_plan_parameters=True,
        outward_binary64_renderer_error_certificate_created=False,
        moving_cells_supplied=False, complete_mixed_pair_cover=False,
        original_R241_R24_held_or_native_acceptance_changed=False,
        original_tau_or_diameter_chosen_or_changed=False,
        full_surface_certified=False, actual_reach_certified=False, task_completed=False,
        limitations=[
            "Correct balls only for the two inherited fixed graph caps; no accepted field or moving-ball evidence is manufactured.",
            "R281 needs separately correct moving balls, the common original cap frame, the unchanged reach target, and complete mixed-pair responsibility.",
            "The legacy static-base/R24 route and all its gates remain available and unmodified.",
            "These balls enclose the exact real finite graph defined by the stored parameters; they do not bound floating renderer evaluations or certify seams, the complete surface metric, curvature or reach.",
            "The independent stored kappa is reported but is not substituted for the derivative of the actual height/radius graph."])
    raw = (json.dumps(result, sort_keys=True, separators=(",", ":"), allow_nan=False)+"\n").encode()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("xb") as stream:
        stream.write(raw)
    print(json.dumps(dict(event="actual_fixed_cap_rational_balls_completed", schema=SCHEMA,
        source_sha256=result["source_sha256"], plan_sha256=binding["plan"]["sha256"],
        assembly_sha256=binding["assembly"]["sha256"],
        output_bytes=len(raw), output_sha256=sha_bytes(raw),
        fixed_cap_cells=len(cells), depth=args.depth, effective_sqrt_bits=bits,
        complete_mixed_pair_cover=False, full_surface_certified=False, actual_reach_certified=False),
        sort_keys=True, separators=(",", ":")), flush=True)


if __name__ == "__main__":
    main()
