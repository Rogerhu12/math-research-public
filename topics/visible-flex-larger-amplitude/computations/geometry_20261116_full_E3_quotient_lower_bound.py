#!/usr/bin/env python3
"""R517: exact rational E(3) lower bounds from a complete actual R425 cover.

API only.  No new request, owned launcher, solver gate or field is created.
The caller must supply its original absolute-clock budget callback.  Every
scientific operation is restricted to this repository's public Actions.
The R516 theorem is used; no local experiment, fixture or performance claim.
"""
from __future__ import annotations

import copy
from fractions import Fraction as Q
import gzip
import hashlib
import json
from math import isqrt
import os
from pathlib import Path
import traceback

REPOSITORY = "Rogerhu12/math-research-public"
HERE = Path(__file__).resolve().parent
SCHEMA = "R517-complete-R425-image-full-E3-rational-lower-bound-v1"
LIMIT = 90000
R425_NAME = "geometry_20261115_current_C_ten_held_and_rigidity_inputs.py"
R425_SHA = "c87b3a9b9d17f74d8c4f4066f65318e50fed5a56143f620628049a86dcf77ef2"
R425_SCHEMA = "R425-current-C-ten450-whole-image-held-and-planar-germ-inputs-v1"
CAP_NAME = "geometry_20261115_current_C_ten450_fixed_cap_balls.py"
CAP_SHA = "0ff1fa60a619a7df8e58e72e240dc42e99850eacd05b6426cc70e9083f76afae"
CAP_SCHEMA = "R417-current-ten450-fixed-cap-rational-six-jets-and-balls-v1"
R516 = dict(file="R516-finite-full-E3-cover-and-quantitative-quotient-distance.md",
    bytes=16623, sha256="3f6b5ea376a83c251ec738e545a1b75f59b5d414ff6b5494b1c999951f028e85")


def actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("Scientific arithmetic is only allowed in the named public Actions")


def rational(value):
    if isinstance(value, bool) or not isinstance(value, (str, int, Q)):
        raise ValueError("Use exact rational strings/integers, never inferred floating point values")
    return Q(value)


def strings(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {key: strings(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [strings(item) for item in value]
    return value


def canonical(value):
    return (json.dumps(strings(value), ensure_ascii=False, sort_keys=True,
        separators=(",", ":"), allow_nan=False) + "\n").encode("utf-8")


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def identity(value):
    raw = canonical(value)
    return dict(canonical_bytes=len(raw), canonical_sha256=digest(raw))


def equal(a, b):
    return canonical(a) == canonical(b)


def unique_object(items):
    result = {}
    for key, value in items:
        if key in result:
            raise ValueError("Duplicate JSON object key: " + key)
        result[key] = value
    return result


def decode(raw):
    return json.loads(raw, object_pairs_hook=unique_object,
        parse_constant=lambda token: (_ for _ in ()).throw(ValueError("Nonfinite JSON: " + token)))


def file_receipt(path, check=lambda: None, root=None):
    path = Path(path)
    h, size = hashlib.sha256(), 0
    with path.open("rb") as stream:
        while True:
            check()
            raw = stream.read(1048576)
            if not raw:
                break
            h.update(raw)
            size += len(raw)
    return dict(file=str(path.relative_to(root)) if root is not None else path.name,
        bytes=size, sha256=h.hexdigest())


def member_path(root, descriptor):
    if not isinstance(descriptor, dict) or not isinstance(descriptor.get("file"), str):
        raise ValueError("An actual complete member receipt is required")
    rel = Path(descriptor["file"])
    if rel.is_absolute() or ".." in rel.parts or not rel.parts:
        raise ValueError("A member must remain within its actual R425 directory")
    path = (root / rel).resolve()
    if path == root or root not in path.parents:
        raise ValueError("A member escaped its actual R425 directory")
    return path


def bound_member(root, descriptor, work, *, parse=True):
    path = member_path(root, descriptor)
    actual = file_receipt(path, work.check, root)
    if any(actual[key] != descriptor[key] for key in ("file", "bytes", "sha256")):
        raise ValueError("An actual complete R425 member differs: " + descriptor["file"])
    if not parse:
        return path, actual
    work.check()
    raw = path.read_bytes()
    if len(raw) != actual["bytes"] or digest(raw) != actual["sha256"]:
        raise ValueError("The actual member changed during its read")
    return decode(raw), actual


def vector(value):
    if not isinstance(value, (list, tuple)) or len(value) != 3:
        raise ValueError("Retain three exact Cartesian coordinates")
    return tuple(rational(item) for item in value)


def ball(center, radius, provenance):
    radius = rational(radius)
    if radius < 0:
        raise ValueError("A containing ball radius cannot be negative")
    return dict(center=vector(center), radius=radius, provenance=copy.deepcopy(provenance))


def rotate_quarter(center):
    return -center[1], center[0], center[2]


def square_distance(a, b):
    return sum(((x-y)*(x-y) for x, y in zip(a, b)), Q(0))


def sqrt_bounds(value, bits):
    """R516.22, exact integer arithmetic.  No hardware square root."""
    actions()
    value = rational(value)
    if value < 0 or type(bits) is not int or bits < 0:
        raise ValueError("Use a nonnegative rational and explicit nonnegative square-root bits")
    scale = 1 << bits
    numerator = value.numerator << (2*bits)
    k = isqrt(numerator // value.denominator)
    lower = Q(k, scale)
    upper = lower if k*k*value.denominator == numerator else Q(k+1, scale)
    return lower, upper


class Stop(RuntimeError):
    """A caller can rethrow its original budget exception as this type."""


class Work:
    def __init__(self, check_budget, *, max_boxes, max_distances, max_cover_balls):
        actions()
        if not callable(check_budget):
            raise ValueError("Supply the original caller's absolute-clock budget callback")
        for value in (max_boxes, max_distances, max_cover_balls):
            if type(value) is not int or value <= 0:
                raise ValueError("Resource maxima must be explicit positive integers")
        self.external = check_budget
        self.limits = dict(boxes=max_boxes, distances=max_distances, cover_balls=max_cover_balls)
        self.counts = dict(boxes=0, distances=0, cover_balls=0)
        self.cursor = dict(stage="input-binding", current_member=None, next_ordinal=None)
        self.observed_original = {}

    def check(self):
        self.external()

    def begin(self, kind):
        self.check()
        if self.counts[kind] >= self.limits[kind]:
            raise Stop("declared_" + kind + "_work_limit")
        self.counts[kind] += 1


class DecisionLedger:
    def __init__(self, path, root):
        self.path, self.root = Path(path), Path(root)
        self.file = self.path.open("xb")
        self.stream = gzip.GzipFile(filename="", fileobj=self.file, mode="wb", mtime=0)
        self.rows, self.bytes, self.hash = 0, 0, hashlib.sha256()

    def add(self, value):
        raw = canonical(dict(ordinal=self.rows, **value))
        self.stream.write(raw)
        self.stream.flush()
        self.hash.update(raw)
        self.bytes += len(raw)
        self.rows += 1

    def close(self):
        if self.stream is not None:
            self.stream.close()
            self.file.flush()
            os.fsync(self.file.fileno())
            self.file.close()
            self.stream = None
        row = file_receipt(self.path, root=self.root)
        row.update(rows=self.rows, decoded_bytes=self.bytes, decoded_sha256=self.hash.hexdigest())
        return row


class BoundImages:
    """Created from a complete actual R425 result, not a supplied success flag."""
    def __init__(self):
        self.cover0, self.cover1 = [], []
        self.witness0, self.witness1 = [], []
        self.binding = None
        self.R0 = self.R1 = self.D_upper = None


def exact_cap_point(cap_binding, parameter):
    """Actual R417 graph, summing every same-side marker including overlaps."""
    actions()
    if (not isinstance(parameter, dict) or set(parameter) != {"x", "y", "upper"}
            or type(parameter["upper"]) is not bool):
        raise ValueError("A cap member uses exact x/y and an explicit actual side")
    x, y = rational(parameter["x"]), rational(parameter["y"])
    cuff = rational(cap_binding["original_cuff"]["exact_rational"])
    if cuff <= 0 or x*x+y*y > cuff*cuff:
        raise ValueError("The actual cap point is outside its original closed disk")
    H = rational(cap_binding["exact_height"])
    total = Q(0)
    selected = []
    for row in cap_binding["markers"]:
        if row["upper"] is not parameter["upper"]:
            continue
        center = tuple(rational(value) for value in row["center_exact"])
        if len(center) != 2:
            raise ValueError("The complete original marker center changed")
        radius = rational(row["radius_exact"])
        amplitude = rational(row["amplitude_exact"])
        if radius <= 0:
            raise ValueError("The actual marker radius is not positive")
        t = max(Q(0), 1-((x-center[0])**2+(y-center[1])**2)/(radius*radius))
        total += amplitude*t**4
        selected.append(row["current_marker_list_index"])
    side = 1 if parameter["upper"] else -1
    point = (x, y, side*(H+total))
    return ball(point, Q(0), dict(kind="actual-fixed-cap-member",
        actual_parameters=copy.deepcopy(parameter), same_side_marker_indices=selected,
        complete_graph_formula="side*(H+sum A*max(0,1-distance_squared/R^2)^4)",
        support_center_not_substituted_for_surface_point=True,
        fixed_at_both_endpoint_phases=True))


def bind_r425(*, computations, directory, result_sha256, cap_points, sqrt_bits, work):
    actions()
    computations, root = Path(computations).resolve(), Path(directory).resolve()
    if computations != HERE:
        raise ValueError("Place this API beside its actual bound scientific sources")
    if not isinstance(cap_points, list) or not cap_points:
        raise ValueError("This quantitative method requires explicit actual cap member points")
    sources = {}
    for name, expected in ((R425_NAME, R425_SHA), (CAP_NAME, CAP_SHA)):
        sources[name] = file_receipt(computations/name, work.check)
        if sources[name]["sha256"] != expected:
            raise ValueError("This first API registers only the exact original R425/R417 source: " + name)
    work.cursor.update(stage="read-result", current_member="result.json")
    raw = (root/"result.json").read_bytes()
    if digest(raw) != result_sha256:
        raise ValueError("Bind the complete actual R425 result bytes")
    result = decode(raw)
    work.observed_original = dict(
        actual_R425_result=dict(file="result.json", bytes=len(raw), sha256=digest(raw)),
        original_result_status={key: copy.deepcopy(result[key]) for key in
            ("schema", "source", "current_stage", "error", "resource_stop",
             "resource_partial", "unstarted_scope") if key in result})
    if "position" in result:
        observed_position = result["position"]
        work.observed_original["position_from_original_result"] = (
            {key: copy.deepcopy(observed_position[key]) for key in
                ("whole_closed_position_cover_completed", "completed_roots", "total_roots",
                 "fixed_cap_root_count", "terminal_position_domains",
                 "strict_empty_disk_intersections", "pending", "error", "resource_stop")
                if key in observed_position}
            if isinstance(observed_position, dict) else copy.deepcopy(observed_position))
    if (result.get("schema") != R425_SCHEMA
            or result.get("source", {}).get("file") != R425_NAME
            or result.get("source", {}).get("sha256") != R425_SHA):
        raise ValueError("Do not relabel a generated-view or another producer result as original R425")
    members = result["members"]
    work.cursor.update(stage="read-binding", current_member=members["input_binding"]["file"])
    binding, binding_receipt = bound_member(root, members["input_binding"], work)
    if (binding.get("schema") != R425_SCHEMA+"-same-field-binding"
            or binding.get("source", {}).get("file") != R425_NAME
            or binding.get("source", {}).get("sha256") != R425_SHA
            or not equal(identity(binding), result["actual_input_binding_identity"])
            or binding["sources"][CAP_NAME]["sha256"] != CAP_SHA):
        raise ValueError("The complete R425 field/cap input binding differs")
    position, position_receipt = bound_member(root, members["position_result"], work)
    if not equal(position, result["position"]):
        raise ValueError("Retain the complete actual position result, not a summary subset")
    work.observed_original["actual_complete_position_member"] = position_receipt
    work.observed_original["position_member_equals_original_result"] = True
    pending = position["pending"]
    if (position.get("whole_closed_position_cover_completed") is not True
            or position["completed_roots"] != position["total_roots"]
            or position["fixed_cap_root_count"] != 2
            or pending["current_root"] is not None
            or pending["complete_closed_frontier"] != []
            or pending["unvisited_root_half_open_suffix"] !=
                [position["total_roots"], position["total_roots"]]):
        raise ValueError("The original whole closed image cover remains unpaid")
    cap_binding = binding["complete_current_cap_binding"]
    attachment = binding["current_R413_attachment"]
    if (cap_binding.get("schema") != CAP_SCHEMA+"-same-field-binding"
            or cap_binding["source"]["file"] != CAP_NAME
            or cap_binding["source"]["sha256"] != CAP_SHA
            or not equal(cap_binding["R413_attachment"], attachment)
            or not equal(cap_binding["original_shared_binding"],
                attachment["original_shared_binding"])
            or not equal(cap_binding["original_complete_ten_target"],
                binding["current_actual_target_identity"])
            or not equal(binding["complete_current_field_binding"]["current_target_identity"],
                binding["current_actual_target_identity"])):
        raise ValueError("Actual caps and the complete current field must have one original owner")
    actual_points, points_receipt = bound_member(root, members["actual_witness_points"], work)
    if not equal(actual_points, result["actual_witness_parameters_and_boxes"]):
        raise ValueError("Keep the actual member-point boxes, not inferred sampled positions")
    images = BoundImages()
    for i, row in enumerate(actual_points):
        work.check()
        if row["index"] != i:
            raise ValueError("Original active witness indices changed")
        p0 = ball(row["phase0_position_center"], row["phase0_position_radius"],
            dict(kind="actual-active-member", original_index=i,
                actual_parameters=copy.deepcopy(row["actual_parameters"])))
        p1 = ball(row["quarter_turn_center"], row["quarter_turn_radius"], p0["provenance"])
        if p1["center"] != rotate_quarter(p0["center"]) or p1["radius"] != p0["radius"]:
            raise ValueError("The actual R425 quarter turn was changed")
        images.witness0.append(p0)
        images.witness1.append(p1)
    cap_members = []
    for i, parameter in enumerate(cap_points):
        work.cursor = dict(stage="cap-member-evaluation", current_cap_point=i,
            actual_cap_parameter=copy.deepcopy(parameter), total_cap_point_count=len(cap_points),
            unvisited_cap_point_half_open_suffix=[i, len(cap_points)])
        work.check()
        row = exact_cap_point(cap_binding, parameter)
        cap_members.append(row)
        images.witness0.append(row)
        images.witness1.append(copy.deepcopy(row))
    descriptor = members["ledger_positions"]
    path, stored_receipt = bound_member(root, descriptor, work, parse=False)
    decoded_hash, decoded_bytes, rows = hashlib.sha256(), 0, 0
    terminals = empty = split = 0
    work.cursor = dict(stage="position-ledger", current_member=descriptor["file"],
        next_ordinal=0, declared_rows=descriptor["rows"], decoded_prefix_bytes=0)
    with gzip.open(path, "rb") as stream:
        while True:
            work.check()
            raw_line = stream.readline()
            if not raw_line:
                break
            row = decode(raw_line)
            if row.get("ordinal") != rows:
                raise ValueError("The complete original position ledger row order changed")
            kind = row["kind"]
            if kind == "complete_closed_position_terminal":
                work.begin("cover_balls")
                cell, enclosure = row["cell"], row["enclosure"]
                if cell.get("kind") not in ("active", "cap"):
                    raise ValueError("Unknown actual closed position cell")
                item = ball(enclosure["center"], enclosure["radius"],
                    dict(original_ordinal=rows, actual_cell=copy.deepcopy(cell)))
                other = ball(rotate_quarter(item["center"]) if cell["kind"] == "active"
                    else item["center"], item["radius"], item["provenance"])
                images.cover0.append(item)
                images.cover1.append(other)
                terminals += 1
            elif kind == "empty_closed_disk_intersection":
                if row.get("strict_outside_test") is not True or row["cell"].get("kind") != "cap":
                    raise ValueError("Only the producer's strict outside-disk cells may be absent")
                empty += 1
            elif kind == "complete_closed_split":
                split += 1
            else:
                raise ValueError("Unknown original position-ledger record: " + str(kind))
            decoded_hash.update(raw_line)
            decoded_bytes += len(raw_line)
            rows += 1
            work.cursor.update(next_ordinal=rows, decoded_prefix_bytes=decoded_bytes)
    if (rows != descriptor["rows"] or decoded_bytes != descriptor["decoded_bytes"]
            or decoded_hash.hexdigest() != descriptor["decoded_sha256"]
            or terminals != position["terminal_position_domains"]
            or empty != position["strict_empty_disk_intersections"]
            or not images.cover0):
        raise ValueError("The entire actual stored/decoded closed cover was not retained")
    images.R0 = images.R1 = Q(0)
    for i, (a, b) in enumerate(zip(images.cover0, images.cover1)):
        work.cursor = dict(stage="complete-image-norm", next_cover_index=i,
            complete_cover_count=len(images.cover0))
        work.check()
        images.R0 = max(images.R0, sqrt_bounds(square_distance(a["center"], (0,0,0)), sqrt_bits)[1]+a["radius"])
        images.R1 = max(images.R1, sqrt_bounds(square_distance(b["center"], (0,0,0)), sqrt_bits)[1]+b["radius"])
    diameter = position.get("whole_marked_F0_D")
    if diameter is not None:
        images.D_upper = rational(diameter["phase_zero_complete_image_diameter_upper"])
        if images.D_upper <= 0:
            raise ValueError("A requested diameter ratio needs the actual positive full-image bound")
    images.binding = dict(schema=SCHEMA+"-bound-complete-images",
        actual_R425_result=dict(file="result.json", bytes=len(raw), sha256=digest(raw)),
        actual_input_binding=binding_receipt, actual_position_result=position_receipt,
        actual_member_points=points_receipt, actual_position_ledger=copy.deepcopy(descriptor),
        stored_ledger_receipt=stored_receipt, decoded_rows=rows,
        decoded_bytes=decoded_bytes, decoded_sha256=decoded_hash.hexdigest(),
        complete_original_binding_identity=identity(binding),
        complete_current_field_binding=copy.deepcopy(binding["complete_current_field_binding"]),
        complete_cap_binding_identity=identity(cap_binding),
        actual_target_identity=copy.deepcopy(binding["current_actual_target_identity"]),
        original_R413_attachment_identity=identity(attachment),
        source_records=sources, complete_terminal_balls=terminals,
        strict_empty_disk_cells=empty, complete_split_rows=split,
        active_member_count=len(actual_points), explicit_cap_members=cap_members,
        cap_member_counts=dict(upper=sum(p["upper"] for p in cap_points),
            lower=sum(not p["upper"] for p in cap_points)),
        all_cap_side_markers_including_negative_and_overlapping_summed=True,
        S1_rule="active center (-y,x,z), cap center unchanged; every radius unchanged",
        original_complete_cover_work_resolution_required=False,
        original_reach_metric_germ_or_embedding_success_required=False,
        source_generated_views_registered=False,
        fixed_member_plan_not_claimed_dense=True,
        fixed_C_enclosure_convergence_not_claimed=True)
    work.cursor = dict(stage="complete-input-binding")
    return images


def quaternion_matrix(chart, coordinates, reflection):
    """All four largest-coordinate charts, right-multiplied by J if requested."""
    actions()
    if (type(chart) is not int or not 0 <= chart < 4
            or type(reflection) is not bool or len(coordinates) != 3):
        raise ValueError("Use one of the eight complete orthogonal charts")
    free = tuple(rational(value) for value in coordinates)
    if any(value < -1 or value > 1 for value in free):
        raise ValueError("Quaternion free coordinates stay in the full closed unit cube")
    v, iterator = [], iter(free)
    for i in range(4):
        v.append(Q(1) if i == chart else next(iterator))
    w, x, y, z = v
    n = sum((a*a for a in v), Q(0))
    rows = [
        [w*w+x*x-y*y-z*z, 2*(x*y-w*z), 2*(x*z+w*y)],
        [2*(x*y+w*z), w*w-x*x+y*y-z*z, 2*(y*z-w*x)],
        [2*(x*z-w*y), 2*(y*z+w*x), w*w-x*x-y*y+z*z],
    ]
    return tuple(tuple(value/n*(-1 if reflection and j == 0 else 1)
        for j, value in enumerate(row)) for row in rows)


def transform(matrix, translation, point):
    return tuple(sum((matrix[i][j]*point[j] for j in range(3)), Q(0))
        + translation[i] for i in range(3))


def center_bound(images, cell, sqrt_bits, work):
    """Every witness is minimized over every target ball before it is usable."""
    endpoints = cell["box"]
    centers = tuple((a+b)/2 for a, b in endpoints)
    half = tuple((b-a)/2 for a, b in endpoints)
    matrix = quaternion_matrix(cell["chart"], centers[:3], cell["reflection"])
    shift = centers[3:]
    eta, beta = min(Q(2), 2*sum(half[:3], Q(0))), sum(half[3:], Q(0))
    global_lower, limiting = Q(0), None
    completed_witnesses = [0, 0]
    for direction, witnesses, target in (
            ("forward", images.witness1, images.cover0),
            ("reverse", images.witness0, images.cover1)):
        for i, witness in enumerate(witnesses):
            current_minimum, current_target = None, None
            witness_center = (transform(matrix, shift, witness["center"])
                if direction == "forward" else witness["center"])
            for j, target_ball in enumerate(target):
                work.cursor = dict(stage="box-center-complete-target-minimum",
                    root_index=cell["root_index"], chart=cell["chart"],
                    reflection=cell["reflection"], box_path=cell["path"],
                    direction=direction, actual_witness_index=i,
                    witness_count=len(witnesses), next_target_ball_index=j,
                    complete_target_ball_count=len(target),
                    unvisited_target_half_open_suffix=[j, len(target)],
                    visited_target_minimum=current_minimum,
                    visited_target_minimum_is_not_global=True,
                    completed_witness_counts=list(completed_witnesses))
                work.begin("distances")
                target_center = (target_ball["center"] if direction == "forward"
                    else transform(matrix, shift, target_ball["center"]))
                low = sqrt_bounds(square_distance(witness_center, target_center), sqrt_bits)[0]
                bound = max(Q(0), low-witness["radius"]-target_ball["radius"])
                if current_minimum is None or bound < current_minimum:
                    current_minimum, current_target = bound, j
            # Nonempty complete cover was already established by the binding.
            if current_minimum is None:
                raise ValueError("A complete image cover cannot be empty")
            completed_witnesses[0 if direction == "forward" else 1] += 1
            if current_minimum > global_lower:
                global_lower = current_minimum
                limiting = dict(direction=direction, actual_witness_index=i,
                    complete_target_minimizer_index=current_target,
                    witness_provenance=copy.deepcopy(witness["provenance"]),
                    target_ball_provenance=copy.deepcopy(target[current_target]["provenance"]))
    lower = max(Q(0), global_lower-eta*images.R1-beta)
    work.cursor = dict(stage="complete-box-bound", root_index=cell["root_index"],
        box_path=cell["path"], all_original_targets_visited_for_all_witnesses=True)
    return dict(center_orthogonal_matrix=matrix, center_translation=shift,
        center_complete_bidirectional_lower=global_lower,
        orthogonal_operator_variation_upper=eta, translation_variation_upper=beta,
        complete_S1_norm_upper=images.R1, complete_box_lower=lower,
        limiting_positive_center_witness=limiting,
        completed_witness_counts=completed_witnesses)


class TransformCover:
    def __init__(self, images, gamma, sqrt_bits, max_depth, work, ledger):
        actions()
        if not isinstance(images, BoundImages) or images.binding is None:
            raise ValueError("Use the actual complete image binding")
        self.gamma, self.images = rational(gamma), images
        if self.gamma <= 0:
            raise ValueError("The requested lower bound must be an explicit positive rational")
        if type(max_depth) is not int or max_depth < 0:
            raise ValueError("The transform depth is an explicit nonnegative work limit")
        self.sqrt_bits, self.max_depth = sqrt_bits, max_depth
        self.work, self.ledger = work, ledger
        self.B = images.R0+images.R1+self.gamma
        self.root_box = ((Q(-1), Q(1)),)*3+((-self.B, self.B),)*3
        self.root_index, self.stack = 0, []
        self.paid, self.splits, self.minimum_paid = 0, 0, None
        self.last_complete_bound, self.completed = None, False

    def root(self, index):
        return dict(root_index=index, chart=index % 4, reflection=bool(index // 4),
            path="", depth=0, box=self.root_box)

    def children(self, cell):
        axis = cell["depth"] % 6
        a, b = cell["box"][axis]
        middle = (a+b)/2
        children = []
        for side, interval in enumerate(((a, middle), (middle, b))):
            box = list(cell["box"])
            box[axis] = interval
            children.append(dict(cell, path=cell["path"]+str(side),
                depth=cell["depth"]+1, box=tuple(box)))
        return axis, children

    def run(self):
        while self.root_index < 8:
            if not self.stack:
                self.stack.append(self.root(self.root_index))
            while self.stack:
                cell = self.stack[-1]
                self.work.cursor = dict(stage="next-transform-box",
                    root_index=self.root_index, box_path=cell["path"])
                self.work.begin("boxes")
                bound = center_bound(self.images, cell, self.sqrt_bits, self.work)
                self.last_complete_bound = dict(actual_box=copy.deepcopy(cell), **bound)
                if bound["complete_box_lower"] >= self.gamma:
                    self.ledger.add(dict(kind="complete_transform_box_paid",
                        actual_box=cell, bound=bound,
                        requested_gamma=self.gamma, complete_closed_box_included=True))
                    self.paid += 1
                    self.minimum_paid = (bound["complete_box_lower"] if self.minimum_paid is None
                        else min(self.minimum_paid, bound["complete_box_lower"]))
                    self.stack.pop()
                    continue
                if cell["depth"] >= self.max_depth:
                    self.ledger.add(dict(kind="current_box_depth_work_limit",
                        actual_box=cell, bound=bound, requested_gamma=self.gamma,
                        insufficient_lower_bound_is_not_a_congruence_or_impossibility_result=True))
                    raise Stop("declared_transform_depth_work_limit")
                axis, children = self.children(cell)
                self.ledger.add(dict(kind="complete_closed_transform_split",
                    actual_box=cell, actual_parent_bound=bound,
                    split_axis=axis, all_closed_children=children,
                    shared_bisection_boundary_in_both_children=True))
                # The parent leaves the stack only after both children are recorded.
                self.stack[-1:] = list(reversed(children))
                self.splits += 1
            self.root_index += 1
        self.completed = True

    def report(self):
        return dict(
            complete_orthogonal_group_including_reflections=True,
            root_count=8, completed_roots=self.root_index,
            root_definition=dict(charts="v_i=1, other three coordinates in [-1,1], i=0..3",
                components="R(v) and R(v)*diag(-1,1,1)",
                actual_root_box=self.root_box,
                root_order="reflection false charts0..3, then true charts0..3"),
            complete_S0_norm_upper=self.images.R0,
            complete_S1_norm_upper=self.images.R1,
            actual_translation_bound=self.B, requested_gamma=self.gamma,
            outside_translation_cube_strict_lower=self.gamma,
            outside_cube_uses_entire_nonempty_images=True,
            whole_closed_transform_cover_completed=self.completed,
            complete_paid_boxes=self.paid, complete_closed_splits=self.splits,
            minimum_complete_paid_box_lower=self.minimum_paid,
            actual_last_complete_box_bound=self.last_complete_bound,
            global_quotient_distance_lower=self.gamma if self.completed else None,
            delta_E_lower=self.gamma if self.completed else None,
            complete_F0_diameter_upper=self.images.D_upper,
            delta_E_over_D_lower=(self.gamma/self.images.D_upper
                if self.completed and self.images.D_upper is not None else None),
            stronger_five_percent_ratio_paid=(bool(20*self.gamma >= self.images.D_upper)
                if self.completed and self.images.D_upper is not None else None),
            pending=dict(
                current_root=self.root_index if self.stack else None,
                complete_closed_frontier=copy.deepcopy(self.stack),
                unvisited_root_half_open_suffix=[
                    self.root_index+(1 if self.stack else 0), 8],
                unvisited_roots=[self.root(i) for i in
                    range(self.root_index+(1 if self.stack else 0), 8)],
                actual_distance_or_input_cursor=copy.deepcopy(self.work.cursor)),
            fixed_C_and_fixed_witnesses_not_promised_to_resolve_positive_gap=True,
            no_solver_or_metric_or_embedding_gate_added=True,
            actual_global_embedding_or_reach_or_same_g_convergence_paid=False)


def write_member(root, name, value):
    raw = canonical(value)
    path = root/name
    with path.open("xb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    return dict(file=name, bytes=len(raw), sha256=digest(raw))


def output_directory(out, directory, computations):
    value = os.environ.get("RUNNER_TEMP")
    if not value:
        raise ValueError("Use an actual public runner temporary directory")
    temporary, root = Path(value).resolve(), Path(out).resolve()
    if (not temporary.is_dir() or root == temporary or temporary not in root.parents
            or root.exists()):
        raise ValueError("Use a fresh own output strictly inside actual RUNNER_TEMP")
    for path in (Path(directory).resolve(), Path(computations).resolve(), Path(__file__).resolve()):
        if path == root or root in path.parents:
            raise ValueError("The output cannot own an original field, input or source")
    return root


def produce(*, computations, directory, result_sha256, out, cap_points,
            desired_gamma, sqrt_bits, max_boxes, max_distance_evaluations,
            max_cover_balls, max_depth, check_budget, caller_clock_identity):
    """Run in Actions under the caller's ORIGINAL clock.

    check_budget must use the existing absolute deadline, reserve and signal
    handling. It may raise Stop (or rethrow its original resource exception
    as Stop without changing its message). Other exceptions are preserved as
    errors, with the complete unfinished scope. No owned-process or cleanup
    success is inferred by this library.
    """
    actions()
    if type(sqrt_bits) is not int or not 0 <= sqrt_bits <= 8192:
        raise ValueError("Use an explicit square-root work precision")
    if not isinstance(caller_clock_identity, dict) or not caller_clock_identity:
        raise ValueError("Record the actual caller's original clock provenance")
    desired_gamma = rational(desired_gamma)
    if desired_gamma <= 0 or type(max_depth) is not int or max_depth < 0:
        raise ValueError("Use a positive exact candidate bound and an explicit depth work limit")
    root = output_directory(out, directory, computations)
    root.mkdir()
    large = root/"large-arrays"
    large.mkdir()
    work = Work(check_budget, max_boxes=max_boxes,
        max_distances=max_distance_evaluations, max_cover_balls=max_cover_balls)
    images = cover = ledger = None
    members = {}
    error = resource = None
    stage = "complete-original-input-binding"
    request_scope = dict(
        actual_original_directory=str(Path(directory).resolve()),
        actual_original_result_sha256=result_sha256,
        explicit_cap_point_plan=copy.deepcopy(cap_points),
        desired_gamma=desired_gamma, sqrt_bits=sqrt_bits,
        max_boxes=max_boxes, max_distance_evaluations=max_distance_evaluations,
        max_cover_balls=max_cover_balls, max_depth=max_depth,
        caller_clock_identity=copy.deepcopy(caller_clock_identity))
    try:
        work.check()
        members["request_scope"] = write_member(root, "actual-input-scope.json", request_scope)
        images = bind_r425(computations=computations, directory=directory,
            result_sha256=result_sha256, cap_points=cap_points, sqrt_bits=sqrt_bits, work=work)
        members["complete_image_binding"] = write_member(root, "complete-image-binding.json", images.binding)
        members["all_member_balls"] = write_member(root, "large-arrays/all-actual-member-balls.json",
            dict(phase0=images.witness0, phase1=images.witness1,
                same_fixed_caps_in_both_phases=True))
        ledger = DecisionLedger(large/"complete-transform-decisions.jsonl.gz", root)
        cover = TransformCover(images, desired_gamma, sqrt_bits, max_depth, work, ledger)
        stage = "complete-eight-root-transform-cover"
        cover.run()
        stage = "complete-requested-quotient-bound"
    except Stop as exc:
        resource = dict(type=type(exc).__name__, message=str(exc), stage=stage,
            original_caller_cause=(None if exc.__cause__ is None else dict(
                type=type(exc.__cause__).__name__, message=str(exc.__cause__))))
    except Exception as exc:
        error = dict(type=type(exc).__name__, message=str(exc), stage=stage,
            complete_traceback=traceback.format_exc())
    finally:
        if ledger is not None:
            members["complete_transform_decisions"] = ledger.close()
    result = dict(schema=SCHEMA, source=file_receipt(__file__), proof=R516,
        repository=REPOSITORY, run_id=os.environ.get("GITHUB_RUN_ID"),
        source_commit=os.environ.get("GITHUB_SHA"),
        current_stage=stage, error=error, resource_stop=resource,
        resources=dict(limits=work.limits, actual_counts=work.counts,
            max_depth=max_depth, sqrt_bits=sqrt_bits),
        caller_clock_identity=copy.deepcopy(caller_clock_identity),
        actual_clock_checked_only_by_supplied_original_callback=True,
        new_science_clock_or_owned_process_created=False,
        complete_original_input_binding_returned=images is not None,
        observed_original_source=copy.deepcopy(work.observed_original),
        complete_original_images=(None if images is None else dict(
            terminal_cover_balls=len(images.cover0),
            phase0_member_balls=len(images.witness0), phase1_member_balls=len(images.witness1),
            complete_S0_norm_upper=images.R0, complete_S1_norm_upper=images.R1,
            source_result=images.binding["actual_R425_result"],
            input_binding=images.binding["actual_input_binding"],
            position_result=images.binding["actual_position_result"],
            original_complete_position_ledger=images.binding["actual_position_ledger"],
            original_active_member_count=images.binding["active_member_count"],
            actual_cap_member_counts=images.binding["cap_member_counts"],
            complete_binding_identity=identity(images.binding))),
        transform_cover=None if cover is None else cover.report(),
        unfinished_before_transform_cover=(None if cover is not None else dict(
            actual_input_cursor=copy.deepcopy(work.cursor),
            whole_eight_orthogonal_charts_and_complete_translation_domain_unstarted=True,
            translation_bound_unavailable_without_complete_original_images=images is None)),
        members=members,
        raw_payloads_are_same_job_temporary_and_not_uploaded=True,
        original_field_or_parent_or_R425_members_removed=False,
        generated_R425_views_or_future_workflow_registered=False,
        actual_owned_process_quiescence_observed=False,
        actual_embedding_reach_metric_native_acceptance_or_task_completion=False)
    result_row = write_member(root, "result.json", result)
    summary = dict(result, actual_result=result_row,
        necessary_scope="All transform frontier/root suffix/current witness-target cursor/errors; "
            "successful complete-image and decision payloads identified, not re-encoded or split.")
    payload = canonical(summary)
    if len(payload) > LIMIT:
        fallback = dict(schema=SCHEMA+"-necessary-over-budget",
            attempted_bytes=len(payload), attempted_sha256=digest(payload),
            actual_result=result_row, complete_necessary_readback=False,
            original_scientific_result_not_replaced=True, raw_retained=True,
            quiescent_or_cleanup_allowed=False)
        row = write_member(root, "necessary-over-budget.json", fallback)
        print("BEGIN_R517_FULL_E3_NECESSARY", flush=True)
        print(canonical(fallback).decode(), end="", flush=True)
        print("END_R517_FULL_E3_NECESSARY", flush=True)
        return dict(exit_code=70, original_result=result_row, necessary=row,
            complete_necessary_readback=False)
    row = write_member(root, "necessary-summary.json", summary)
    print("BEGIN_R517_FULL_E3_NECESSARY", flush=True)
    print(payload.decode(), end="", flush=True)
    print("END_R517_FULL_E3_NECESSARY", flush=True)
    return dict(exit_code=1 if error is not None else 2 if resource is not None else 0,
        original_result=result_row, necessary=row, complete_necessary_readback=True,
        original_caller_must_observe_true_quiescence_before_any_cleanup=True)
