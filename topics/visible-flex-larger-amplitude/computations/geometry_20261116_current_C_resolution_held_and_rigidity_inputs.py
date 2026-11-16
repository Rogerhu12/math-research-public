#!/usr/bin/env python3
"""Current accurate-C whole-image held and R238 rigidity inputs, source-only.

The actual R416 field and R417 caps are used directly.  No old mesh point,
rounded renderer envelope, current reach/metric success, or old cut ap/app is
substituted.  R254 pure prefix kernels and R274 common-background cancellation
are retained.  Every actual calculation is restricted to public Actions.
This component does not create an accepted450 or certify global embedding.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import shutil
import signal
import sys
import time

REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "R441-current-C-resolution450-whole-image-held-and-planar-germ-inputs-v1"
LIMIT = 90000
CUT = "geometry_20261116_current_C_resolution_accurate_cut_patch.py"
CUFF = "geometry_20261116_current_C_resolution_original_cuff_atlas.py"
CAP = "geometry_20261116_current_C_resolution_fixed_cap_balls.py"
ACTIVE = "geometry_20261115_shared_active_interval_balls.py"
PREFIX = "geometry_20261114_prefix_exact_nonplanarity.py"
KERNEL = "root_mixed_phase_normal_balls.py"
DIAMETER = "geometry_20261115_shared_curvature_diameter_budget.py"
SOURCE_PINS = {
    CUT: "8811f89c7395bb4aed1adabe6c6825c801e1e41a9d80d416b0a4746596ae9a52",
    CUFF: "d0b03a367f3ece13b06949d5218a992e6ee3e9a41364499070d3f5f475a150a0",
    CAP: "ca53bdc5c0cdd5764065301f0edb1259d083fdffa9f3d767a5a38b4a7cafe364",
    ACTIVE: "675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b",
    PREFIX: "a40dc7a50d90694006342ec964f18fac90bb2743ad622e1b715d920d376c1aa6",
    KERNEL: "ecea0ef58aa5755270807596da5512552ac52fab27e90492fcf85fab095716c6",
    DIAMETER: "b1c2dfb9bd99c0777805da938c38e428da32db8ed5fa6238c9433ed9aede5ad0",
}
TAIL_FRACTIONS = (Q(0), Q(1), Q(1, 2), *(Q(j, 15) for j in range(1, 15)))
CARDINAL_COS = (Q(1), Q(0), Q(-1), Q(0))
CARDINAL_SIN = (Q(0), Q(1), Q(0), Q(-1))
CIRCLE_DIFFERENCES = ((Q(-1), Q(1), Q(0)),
                      (Q(-2), Q(0), Q(0)), (Q(-1), Q(-1), Q(0)))


def actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("Use the named public repository's Actions for scientific arithmetic")


def temporary_output(args):
    value = os.environ.get("RUNNER_TEMP")
    if not value:
        raise ValueError("An actual runner temporary directory is required")
    temporary = Path(value).resolve()
    output = Path(args.out).resolve()
    if (not temporary.is_dir() or output == temporary
            or temporary not in output.parents):
        raise ValueError("Keep this owned output strictly inside actual RUNNER_TEMP")
    for name in ("computations", "directory", "witness_plan", "cuff_atlas",
                 "checkpoint_directory", "proof_directory"):
        path = getattr(args, name, None)
        if path is not None:
            original = Path(path).resolve()
            if original == output or output in original.parents:
                raise ValueError("The owned output cannot contain an actual input: " + name)
    source = Path(__file__).resolve()
    if source == output or output in source.parents:
        raise ValueError("The owned output cannot contain this defining source")
    if output.exists():
        raise FileExistsError("Use a fresh owned output; do not overwrite earlier evidence")
    return output


def strings(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {key: strings(v) for key, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [strings(v) for v in value]
    return value


def canonical(value):
    return (json.dumps(strings(value), sort_keys=True, ensure_ascii=False,
                       separators=(",", ":"), allow_nan=False) + "\n").encode()


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def identity(value):
    raw = canonical(value)
    return dict(canonical_bytes=len(raw), canonical_sha256=digest(raw))


def receipt(path, root=None):
    path = Path(path)
    h, size = hashlib.sha256(), 0
    with path.open("rb") as stream:
        for raw in iter(lambda: stream.read(1048576), b""):
            h.update(raw)
            size += len(raw)
    return dict(file=str(path.relative_to(root)) if root is not None else path.name,
                bytes=size, sha256=h.hexdigest())


def write(path, value, root):
    raw = canonical(value)
    with Path(path).open("xb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    return receipt(path, root)


def rational(value):
    if isinstance(value, bool) or not isinstance(value, (str, int, Q)):
        raise ValueError("Supply exact rational strings or integers, never inferred float values")
    return Q(value)


def load(directory, name):
    actions()
    path = (Path(directory) / name).resolve()
    row = receipt(path)
    if row["sha256"] != SOURCE_PINS[name]:
        raise ValueError("A defining source differs: " + name)
    module_name = "_R425_" + name[:-3]
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError("No loader for actual pinned source")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        sys.modules.pop(module_name, None)
        raise
    return module, row


class Stop(RuntimeError):
    pass


class Budget:
    def __init__(self, args):
        self.args, self.start = args, time.monotonic()
        self.signal_number = None
        self.counts = dict(position_cells=0, prefix_points=0, tail_witnesses=0)

    def signal(self, number, _frame):
        self.signal_number = number

    def check(self, kind=None):
        if self.signal_number is not None:
            raise Stop("external_signal_" + str(self.signal_number))
        if time.monotonic() - self.start >= self.args.budget_seconds:
            raise Stop("declared_whole_consumer_wall_budget")
        if shutil.disk_usage(self.args.out).free < self.args.free_bytes_reserve:
            raise Stop("owned_output_disk_reserve")
        if kind is not None:
            maximum = getattr(self.args, "max_" + kind)
            if self.counts[kind] >= maximum:
                raise Stop(kind + "_work_budget")

    def begin(self, kind):
        self.check(kind)
        self.counts[kind] += 1


class Ledger:
    def __init__(self, path, root):
        self.path, self.root = Path(path), Path(root)
        self.raw = self.path.open("xb")
        self.z = gzip.GzipFile(filename="", fileobj=self.raw, mode="wb", mtime=0)
        self.rows, self.decoded_bytes, self.hash = 0, 0, hashlib.sha256()

    def add(self, row):
        raw = canonical(dict(ordinal=self.rows, **row))
        self.z.write(raw)
        self.z.flush()
        self.hash.update(raw)
        self.decoded_bytes += len(raw)
        self.rows += 1

    def close(self):
        if self.z is not None:
            self.z.close()
            self.raw.flush()
            os.fsync(self.raw.fileno())
            self.raw.close()
            self.z = None
        return dict(**receipt(self.path, self.root), rows=self.rows,
                    decoded_bytes=self.decoded_bytes,
                    decoded_sha256=self.hash.hexdigest())


def sqrt_lower(value, sqrt_upper, bits):
    value = Q(value)
    if value < 0:
        raise ValueError("A squared distance cannot be negative")
    return Q(0) if value == 0 else value / sqrt_upper(value, bits)


def interval_box(row):
    result = [(Q(v["lower"]), Q(v["upper"])) for v in row]
    if len(result) != 3 or any(a > b for a, b in result):
        raise ValueError("Use a complete ordered Cartesian position box")
    return result


def box_ball(box, sqrt_upper, bits):
    center = tuple((a + b) / 2 for a, b in box)
    radius = sqrt_upper(sum(((b - a) ** 2 / 4 for a, b in box), Q(0)), bits)
    return center, radius


def exact_marker_inputs(caps, prefix_kernel):
    """The actual R238 four-support algebra; failure is only this method's unpaid input."""
    rows = caps.markers
    centers = [tuple(row["center"]) + ((1 if row["upper"] else -1) * caps.height,)
               for row in rows]
    radii = [row["radius"] for row in rows]
    per_marker = []
    for row, center in zip(rows, centers):
        radius = row["radius"]
        per_marker.append(dict(index=row["index"], upper=row["upper"],
            exact_support_center=center, exact_radius=radius,
            exact_graph_amplitude=row["amplitude"], radius_positive=radius > 0,
            amplitude_nonzero=row["amplitude"] != 0,
            strictly_inside_original_cuff=(0 < radius < caps.cuff and
                sum(x*x for x in row["center"]) < (caps.cuff-radius)**2)))
    pairs = []
    for i in range(len(rows)):
        for j in range(i + 1, len(rows)):
            if rows[i]["upper"] is rows[j]["upper"]:
                d2 = sum((centers[i][k] - centers[j][k]) ** 2 for k in range(2))
                margin = d2 - (radii[i] + radii[j]) ** 2
                pairs.append(dict(indices=[i, j], squared_separation_margin=margin,
                                  strictly_disjoint=margin > 0))
    determinant = None
    if len(rows) == 4:
        v = [prefix_kernel.sub(centers[i], centers[3]) for i in range(3)]
        determinant = prefix_kernel.dot(v[0], prefix_kernel.cross(v[1], v[2]))
    flags = dict(exactly_original_R238_four_markers=len(rows) == 4,
        all_radii_distinct=len(set(radii)) == len(rows),
        all_positive_and_nonzero=all(r["radius_positive"] and r["amplitude_nonzero"] for r in per_marker),
        all_supports_strictly_inside=all(r["strictly_inside_original_cuff"] for r in per_marker),
        all_same_cap_supports_strictly_disjoint=all(r["strictly_disjoint"] for r in pairs),
        support_centers_affinely_independent=determinant is not None and determinant != 0)
    return dict(per_marker=per_marker, same_cap_pairs=pairs,
        exact_support_center_determinant=determinant, conditions=flags,
        R238_marker_algebra_paid=all(flags.values()),
        all_current_markers_retained=True, negative_amplitude_not_excluded=True,
        positive_H_not_required=True, peak_tops_not_used_as_support_centers=True,
        other_marker_layouts_not_refuted_by_failure=True,
        actual_closed_embedding_paid=False)


def witness_points(args, current, sqrt_upper, budget):
    raw = args.witness_plan.read_bytes()
    if len(raw) > LIMIT or digest(raw) != args.witness_plan_sha256:
        raise ValueError("Bind the complete small actual witness parameter plan")
    plan = json.loads(raw)
    if (not isinstance(plan, dict) or set(plan) != {"schema", "points"}
            or plan["schema"] != "R425-current-accurate-active-quarter-turn-witness-plan-v1"
            or not isinstance(plan["points"], list) or not plan["points"]):
        raise ValueError("Explicit nonempty current active point parameters are required")
    result = []
    for index, row in enumerate(plan["points"]):
        budget.check()
        if (not isinstance(row, dict) or set(row) != {"piece_index", "radial", "q", "lower"}
                or type(row["piece_index"]) is not int or type(row["lower"]) is not bool
                or not 0 <= row["piece_index"] < len(current.field.pieces)):
            raise ValueError("A witness must name an actual complete current piece and side")
        p = current.field.pieces[row["piece_index"]]
        r, q = rational(row["radial"]), rational(row["q"])
        if not p["left"] <= r <= p["right"] or not 0 <= q <= 1:
            raise ValueError("A point left its actual closed current parameter piece")
        values = current.evaluate(p, (r, r), (q, q), row["lower"])
        center, radius, box = current.Active.vector_ball(
            tuple(v.d[0] for v in values), sqrt_upper, args.sqrt_bits)
        center, radius = tuple(Q(x) for x in center), Q(radius)
        rotated = (-center[1], center[0], center[2])
        result.append(dict(index=index, actual_parameters=copy.deepcopy(row),
            actual_piece=strings(p), phase0_position_center=center,
            phase0_position_radius=radius, phase0_position_box=box,
            quarter_turn_center=rotated, quarter_turn_radius=radius,
            exact_rotation="(x,y,z) -> (-y,x,z), alpha=pi/2, t=1",
            membership="R248 material inverse transport places the rotated actual active point in F_1(M)",
            material_point_displacement_used_as_Hausdorff=False,
            additional_floating_rotation_error=0))
    return result, receipt(args.witness_plan)


class PositionCover:
    """All current active pieces and both closed graph disks; no reach precondition."""
    def __init__(self, current, caps, Cap, Diameter, sqrt_upper, args, budget, ledger, witnesses):
        self.current, self.caps, self.Cap = current, caps, Cap
        self.sqrt_upper, self.args, self.budget, self.ledger = sqrt_upper, args, budget, ledger
        self.witnesses = witnesses
        self.division = 2 ** args.active_depth
        self.active_count = 2 * len(current.field.pieces) * self.division ** 2
        self.root_count = self.active_count + 2
        self.root_index, self.stack = 0, []
        self.completed, self.terminal, self.empty = False, 0, 0
        self.goal_unpaid = 0
        self.minimum = [None] * len(witnesses)
        self.limiting = [None] * len(witnesses)
        self.image = Diameter.ImageBounds(sqrt_upper, args.sqrt_bits, "original_marked_image")

    def root(self, index):
        if index >= self.active_count:
            return dict(kind="cap", upper=index == self.active_count,
                        path="", depth=0, root=index)
        n, d = len(self.current.field.pieces), self.division
        side, remainder = divmod(index, n * d * d)
        piece_index, remainder = divmod(remainder, d * d)
        i, j = divmod(remainder, d)
        p = self.current.field.pieces[piece_index]
        a, b = p["left"], p["right"]
        return dict(kind="active", lower=bool(side), piece_index=piece_index,
            radial=(a+(b-a)*Q(i,d), a+(b-a)*Q(i+1,d)),
            angular=(Q(j,d), Q(j+1,d)), path="", depth=0, root=index)

    def children(self, cell):
        if cell["kind"] == "cap":
            return [dict(cell, path=cell["path"]+str(i), depth=cell["depth"]+1)
                    for i in range(4)]
        key = "radial" if cell["depth"] % 2 == 0 else "angular"
        a, b = cell[key]
        middle = (a+b)/2
        return [dict(cell, **{key: interval}, path=cell["path"]+str(i),
                     depth=cell["depth"]+1)
                for i, interval in enumerate(((a,middle),(middle,b)))]

    def enclosure(self, cell):
        if cell["kind"] == "cap":
            box = self.Cap.dyadic_box(self.caps.cuff, cell["path"])
            if self.caps.cap.minimum_distance_squared(box, (Q(0),Q(0))) > self.caps.cuff**2:
                return None
            raw = self.caps.cell(cell["path"], cell["upper"], self.args.sqrt_bits)
            box3 = interval_box(raw["Cartesian_six_jets"]["value"])
            center, radius = box_ball(box3, self.sqrt_upper, self.args.sqrt_bits)
            return dict(center=center, radius=radius, box=box3,
                        current_cap_cell=raw, domain="closed rectangle intersected with original closed disk")
        piece = self.current.field.pieces[cell["piece_index"]]
        values = self.current.evaluate(piece, cell["radial"], cell["angular"], cell["lower"])
        center, radius, box = self.current.Active.vector_ball(
            tuple(v.d[0] for v in values), self.sqrt_upper, self.args.sqrt_bits)
        return dict(center=tuple(Q(v) for v in center), radius=Q(radius),
            box=interval_box(box), exact_piece=strings(piece),
            current_active_value_intervals=box,
            derivatives_not_used_as_reach_or_metric_evidence=True)

    def run(self):
        while self.root_index < self.root_count:
            if not self.stack:
                self.stack = [self.root(self.root_index)]
            while self.stack:
                self.budget.begin("position_cells")
                cell = self.stack[-1]
                data = self.enclosure(cell)
                if data is None:
                    self.ledger.add(dict(kind="empty_closed_disk_intersection", cell=cell,
                                         strict_outside_test=True))
                    self.empty += 1
                    self.stack.pop()
                    continue
                refine = (data["radius"] > self.args.position_radius_goal
                          and cell["depth"] < self.args.position_max_depth)
                if refine:
                    children = self.children(cell)
                    self.ledger.add(dict(kind="complete_closed_split", cell=cell,
                        enclosure=data, all_children=children))
                    self.stack.pop()
                    self.stack.extend(reversed(children))
                    continue
                distance_rows = []
                next_minimum, next_limiting = list(self.minimum), list(self.limiting)
                for index, witness in enumerate(self.witnesses):
                    square = sum((data["center"][j]-witness["quarter_turn_center"][j])**2
                                 for j in range(3))
                    center_lower = sqrt_lower(square, self.sqrt_upper, self.args.sqrt_bits)
                    bound = max(Q(0), center_lower-data["radius"]-witness["quarter_turn_radius"])
                    distance_rows.append(dict(witness=index, center_distance_squared=square,
                        center_distance_lower=center_lower, full_image_cell_distance_lower=bound))
                    if next_minimum[index] is None or bound < next_minimum[index]:
                        next_minimum[index] = bound
                        next_limiting[index] = copy.deepcopy(cell)
                resolution = data["radius"] <= self.args.position_radius_goal
                self.ledger.add(dict(kind="complete_closed_position_terminal", cell=cell,
                    enclosure=data, all_witness_distance_bounds=distance_rows,
                    work_resolution_met=resolution,
                    valid_enclosure_does_not_require_work_resolution=True))
                self.image.add(data["center"], data["radius"], data["box"])
                self.minimum, self.limiting = next_minimum, next_limiting
                self.terminal += 1
                self.goal_unpaid += not resolution
                self.stack.pop()
            self.root_index += 1
        self.completed = True

    def report(self):
        diameter = self.image.report(self.completed)
        values = [v for v in self.minimum if v is not None]
        delta = max(values) if self.completed and len(values) == len(self.witnesses) else None
        Hlower = 2*sqrt_lower(self.caps.cuff**2+self.caps.height**2,
                            self.sqrt_upper, self.args.sqrt_bits)
        D = (None if diameter is None else diameter["phase_zero_complete_image_diameter_upper"])
        D = None if D is None else Q(D)
        return dict(whole_closed_position_cover_completed=self.completed,
            active_root_count=self.active_count, fixed_cap_root_count=2,
            total_roots=self.root_count, completed_roots=self.root_index,
            terminal_position_domains=self.terminal, strict_empty_disk_intersections=self.empty,
            work_resolution_unpaid_terminals=self.goal_unpaid,
            all_requested_work_resolution_met=self.completed and self.goal_unpaid == 0,
            per_witness_visited_subset_distance_lower=self.minimum,
            per_witness_limiting_visited_domain=self.limiting,
            visited_subset_minimum_is_not_global_unless_complete=True,
            whole_image_Hausdorff_witness_lower=delta,
            delta_hold_lower=delta, whole_marked_F0_D=diameter,
            fixed_hold=dict(domain="union of both original closed fixed graph disks",
                closed_with_nonempty_relative_interior=True,
                pointwise_fixed_for_entire_phase_family=True,
                exact_boundary_points=[(self.caps.cuff,Q(0),self.caps.height),
                                       (-self.caps.cuff,Q(0),-self.caps.height)],
                diameter_lower=Hlower, positive_cap_height_not_assumed=True),
            held_ratio_lower=(delta/D if delta is not None and D is not None and D>0 else None),
            fixed_hold_ratio_lower=(Hlower/D if D is not None and D>0 else None),
            README_held_fraction_paid=(delta is not None and D is not None and D>0 and 5*delta>=D),
            README_fixed_H_fraction_paid=(D is not None and D>0 and 5*Hlower>=D),
            whole_image_change_proved=delta is not None and delta>0,
            pending=dict(current_root=self.root_index if not self.completed else None,
                complete_closed_frontier=copy.deepcopy(self.stack),
                unvisited_root_half_open_suffix=[self.root_index+(1 if self.stack else 0),self.root_count]),
            reach_or_metric_success_required=False, actual_embedding_certified=False)


class PrefixProof:
    """R254 exact kernels on this already bound current shared nodal instance."""
    def __init__(self, field, kernel, args, budget, ledger):
        self.field, self.kernel, self.args = field, kernel, args
        self.budget, self.ledger = budget, ledger
        self.synthesis = kernel.NodeAngles(field.M, field.nodal)
        L = 2*field.M+1
        values = list(kernel.CARDINAL) + [(Q(1-k*k,1+k*k),Q(2*k,1+k*k))
                                         for k in range(-L,L+1)]
        self.angles, seen = [], set()
        for angle in values:
            angle = tuple(angle)
            if angle not in seen:
                self.angles.append(angle)
                seen.add(angle)
        self.radial = tuple(kernel.RADIAL)
        self.cell, self.cursor = 0, 0
        self.search = None
        self.cells = []
        self.completed = False

    def run(self):
        while self.cell < len(self.field.x)-1:
            self.budget.check()
            if self.search is None:
                self.search = self.kernel.AffineWitness()
                self.cursor = 0
            left, right = self.field.x[self.cell:self.cell+2]
            count = len(self.angles)*len(self.radial)
            found = False
            while self.cursor < count:
                self.budget.begin("prefix_points")
                ia, ir = divmod(self.cursor,len(self.radial))
                angle, unit = self.angles[ia], self.radial[ir]
                l = self.synthesis.at(self.cell,angle)
                r = self.synthesis.at(self.cell+1,angle)
                point = self.kernel.hermite_position(l,r,right-left,unit)
                parameter = dict(radial_fraction=str(unit), exact_s=str(left+(right-left)*unit),
                                 cos_phi=str(angle[0]),sin_phi=str(angle[1]))
                found = self.search.add(point,parameter)
                self.cursor += 1
                if found:
                    break
            item = dict(cell=self.cell, exact_left=left, exact_right=right,
                all_complete_grid_candidates_available=count, attempted_candidates=self.cursor,
                nonzero_four_point_witness=found,
                exact_planar_cell_by_complete_grid=(not found and self.cursor == count),
                exact_witness=self.search.record(),
                whole_original_3Mplus2_state_and_z0_retained=True,
                current_shared_nodal_instance_not_rounded_PPoly=True,
                original_R254_kernel_functions=["NodeAngles.at","hermite_position","AffineWitness.add"],
                post_registration_and_reflection_preserve_affine_dimension=True)
            self.ledger.add(dict(kind="complete_current_prefix_cell", **item))
            self.cells.append({k:item[k] for k in ("cell","exact_left","exact_right",
                "attempted_candidates","nonzero_four_point_witness","exact_planar_cell_by_complete_grid")})
            self.cell += 1
            self.synthesis.discard_before(self.cell)
            self.search = None
            self.cursor = 0
        self.completed = True

    def report(self):
        return dict(total_original_cells=len(self.field.x)-1, completed_cells=self.cell,
            complete_cell_search=self.completed,
            whole_prefix_no_planar_parameter_open_piece_proved=(self.completed and
                all(r["nonzero_four_point_witness"] for r in self.cells)),
            completed_cell_status=self.cells,
            exact_planar_cell_indices=[r["cell"] for r in self.cells if r["exact_planar_cell_by_complete_grid"]],
            complete_grid=dict(circle_points=len(self.angles),radial_fractions=self.radial,
                angles=self.angles, extra_cardinal_points_do_not_replace_complete_grid=True),
            pending=dict(current_cell=None if self.completed else self.cell,
                next_candidate_index=self.cursor,
                current_candidate_half_open_suffix=[self.cursor,len(self.angles)*len(self.radial)]
                    if self.search is not None else None,
                exact_current_affine_basis=None if self.search is None else self.search.record(),
                unvisited_cell_half_open_suffix=[self.cell+(1 if self.search is not None else 0),len(self.field.x)-1]),
            no_old_checkpoint_schema_or_success_flag_substituted=True,
            whole_closed_embedding_or_delta_E_paid=False)


def scalar_polynomial_derivative(coefficients, unit, derivative, width):
    value = Q(0)
    for degree in range(len(coefficients)-1,derivative-1,-1):
        factor = 1
        for k in range(derivative):
            factor *= degree-k
        value = value*unit + factor*coefficients[degree]
    return value/(width**derivative)


class TailProof:
    """R274/R258 same-radius differences with actual R416 real cut multipliers.

    B and its three cut-jet corrections cancel symbolically.  No B mean is
    removed from the field itself.  Fixed C root uncertainty remains in every
    cut multiplier; increasing arithmetic precision does not narrow that family.
    """
    def __init__(self,current,prefix_kernel,args,budget,ledger):
        self.current,self.field,self.M = current,current.field,current.Active
        self.kernel,self.args,self.budget,self.ledger = prefix_kernel,args,budget,ledger
        self.groups, by_key = [], {}
        for index,p in enumerate(self.field.pieces):
            if p["kind"] == "prefix":
                continue
            key = (p["tail_span"],p["cut_patch"])
            if key not in by_key:
                group = dict(index=len(self.groups), tail_span=key[0],cut_patch=key[1],
                    left=p["left"],right=p["right"],actual_piece_indices=[index])
                by_key[key]=group
                self.groups.append(group)
            else:
                group=by_key[key]
                if group["right"] != p["left"]:
                    raise ValueError("A grouped original radial polynomial domain has a gap")
                group["right"]=p["right"]
                group["actual_piece_indices"].append(index)
        self.group,self.cursor,self.completed = 0,0,False
        self.records,self.attempts = [],[]
        self.cache_span,self.cache_polynomials = None,None
        self.delta,self.cut_binding = None,None

    def polynomials(self,span):
        if self.cache_span == span:
            return self.cache_polynomials
        source=self.field.tail_coefficients(span)
        matrices=[[[Q(0) for _ in range(6)] for _ in range(3)] for _ in range(3)]
        for k,coordinates in enumerate(source):
            for j in range(1,4):
                c=CARDINAL_COS[(k*j)%4]-1
                s=CARDINAL_SIN[(k*j)%4]
                for coordinate,(re,im) in enumerate(coordinates):
                    sign=1 if coordinate<2 else -1
                    for power in range(6):
                        matrices[j-1][coordinate][power]+=sign*(c*re[power]-s*im[power])
        self.cache_span,self.cache_polynomials=span,matrices
        return matrices

    def base(self,span,radius,derivative=0):
        a,b=((self.field.cuff,self.field.inner) if span<0
             else (self.field.radii[span],self.field.radii[span+1]))
        unit=(radius-a)/(b-a)
        if not 0<=unit<=1:
            raise ValueError("A same-radius witness left its exact original shared span")
        factor=radius if derivative==0 else Q(1) if derivative==1 else Q(0)
        coefficients=self.polynomials(span)
        return [[scalar_polynomial_derivative(coefficients[j][k],unit,derivative,b-a)
                 +factor*CIRCLE_DIFFERENCES[j][k] for k in range(3)] for j in range(3)]

    def prepare_cut(self):
        if self.delta is not None:
            return
        self.budget.check()
        synthesis=self.kernel.NodeAngles(self.field.M,self.field.nodal)
        values=[synthesis.at(len(self.field.x)-1,a) for a in self.kernel.CARDINAL]
        differences=[[[values[j+1][d][k]-values[0][d][k] for k in range(3)]
                       for j in range(3)] for d in range(3)]
        beta=self.M.ball(self.field.beta)
        co,si=beta.cos(),beta.sin()
        worlds=[]
        for d in range(3):
            rows=[]
            for x,y,z in differences[d]:
                rows.append([co*self.M.ball(x)+si*self.M.ball(y),
                             -si*self.M.ball(x)+co*self.M.ball(y),self.M.ball(z)])
            worlds.append(rows)
        mult=self.field.cut_multipliers
        m1=mult["target_first_multiplier"].d[0]
        m2=mult["target_second_multiplier"].d[0]
        m3=mult["target_first_in_second_multiplier"].d[0]
        target=[worlds[0],[[m1*v for v in row] for row in worlds[1]],
                [[m2*worlds[2][j][k]-m3*worlds[1][j][k] for k in range(3)]
                 for j in range(3)]]
        native=[self.base(len(self.field.radii)-2,self.field.cut,d) for d in range(3)]
        self.delta=[[[target[d][j][k]-self.M.ball(native[d][j][k])
                       for k in range(3)] for j in range(3)] for d in range(3)]
        self.cut_binding=dict(
            source_cut_model=self.current.model.compact_identity(),
            actual_complete_prefix_cut_differences=differences,
            actual_exact_native_cut_differences=native,
            exact_rotation_angle=self.field.beta,
            actual_rotation_enclosures=[self.M.encode_interval(co),self.M.encode_interval(si)],
            accurate_C_multiplier_enclosures={key:self.M.encode_interval(value.d[0])
                                               for key,value in mult.items()},
            full_cut_difference_enclosures=[[[self.M.encode_interval(v) for v in row]
                                             for row in order] for order in self.delta],
            old_numeric_ap_app_not_used=True,
            full_same_radius_B_and_cut_B_jets_cancel_only_from_differences=True,
            full_Fourier_mean_and_Nyquist_not_removed_from_field=True)

    def determinant(self,group,radius):
        base=self.base(group["tail_span"],radius)
        if not group["cut_patch"]:
            value=self.kernel.dot(base[0],self.kernel.cross(base[1],base[2]))
            return dict(arithmetic="exact-rational",exact_determinant=value,
                nonzero=value!=0,strict_sign=(1 if value>0 else -1 if value<0 else 0),
                exact_same_radius_difference_matrix=base)
        self.prepare_cut()
        t=(radius-self.field.cut_start)/self.field.width
        if not 0<=t<=1:
            raise ValueError("A cut-correction witness is outside its actual exact width")
        W=self.field.width
        weights=(t**3*(10-15*t+6*t*t),W*t**3*(-4+7*t-3*t*t),
                 W*W*t**3*(1-2*t+t*t)/2)
        matrix=[[self.M.ball(base[j][k])+sum((self.M.ball(weights[d])*self.delta[d][j][k]
                   for d in range(3)),self.M.arb(0)) for k in range(3)] for j in range(3)]
        value=self.M.dot(matrix[0],self.M.cross(matrix[1],matrix[2]))
        lo,hi=self.M.bounds(value)
        return dict(arithmetic="rigorous-current-C-real-coefficient-interval",
            determinant_enclosure=dict(lower=lo,upper=hi),nonzero=lo>0 or hi<0,
            strict_sign=1 if lo>0 else -1 if hi<0 else None,
            actual_same_radius_difference_intervals=[
                [self.M.encode_interval(v) for v in row] for row in matrix],
            actual_cut_binding_identity=identity(self.cut_binding),
            a_zero_containing_interval_is_not_an_exact_zero=True)

    def run(self):
        while self.group<len(self.groups):
            group=self.groups[self.group]
            found=False
            while self.cursor<len(TAIL_FRACTIONS):
                self.budget.begin("tail_witnesses")
                unit=TAIL_FRACTIONS[self.cursor]
                radius=group["left"]+(group["right"]-group["left"])*unit
                value=self.determinant(group,radius)
                row=dict(group=copy.deepcopy(group),candidate_index=self.cursor,
                    radial_fraction=unit,exact_radius=radius,**value)
                self.ledger.add(dict(kind="actual_current_tail_cardinal_attempt",**row))
                self.attempts.append({key:row[key] for key in
                    ("candidate_index","radial_fraction","exact_radius","arithmetic","nonzero","strict_sign")})
                self.cursor+=1
                if value["nonzero"]:
                    found=True
                    break
            item=dict(group=copy.deepcopy(group),all_original_pieces_covered_by_same_polynomial=True,
                common_B_refinement_transferred_by_R274=True,attempts=copy.deepcopy(self.attempts),
                nonzero_polynomial_witness_found=found,
                exact_cardinal_polynomial_identically_zero=(not found and not group["cut_patch"]
                    and self.cursor==len(TAIL_FRACTIONS)),
                failure_does_not_prove_a_planar_surface=True)
            self.ledger.add(dict(kind="complete_current_tail_polynomial_group",**item))
            self.records.append(item)
            self.group+=1
            self.cursor=0
            self.attempts=[]
        self.completed=True

    def report(self):
        return dict(total_polynomial_groups=len(self.groups),completed_groups=self.group,
            complete_group_attempts=self.completed,
            whole_tail_collar_patch_no_planar_parameter_open_piece_proved=(self.completed and
                all(r["nonzero_polynomial_witness_found"] for r in self.records)),
            all_original_radial_piece_count=sum(len(g["actual_piece_indices"]) for g in self.groups),
            complete_groups=self.groups,completed_group_status=self.records,
            R274_common_B_cancellation_exact=True,
            patched_coefficients_from_same_R416_C_DAG=True,
            numerical_ap_app_or_new_root_midpoints_used=False,
            prefix_full_material_map_cardinal_identity_and_positive_density_retained=True,
            lower_reflection_and_all_material_phases_transferred_by_R248=True,
            pending=dict(current_group=None if self.completed else self.group,
                next_candidate_index=self.cursor,current_completed_attempts=self.attempts,
                remaining_current_candidate_half_open_suffix=[self.cursor,len(TAIL_FRACTIONS)]
                    if not self.completed else None,
                unvisited_group_half_open_suffix=[self.group+(1 if self.cursor else 0),len(self.groups)]),
            actual_closed_embedding_or_delta_E_certified=False)


def compact_prefix(report, original_member):
    pending=copy.deepcopy(report["pending"])
    basis=pending.pop("exact_current_affine_basis")
    pending["current_affine_basis_original_member"]=original_member if basis is not None else None
    pending["current_affine_basis_identity"]=None if basis is None else identity(basis)
    return dict(total_original_cells=report["total_original_cells"],
        completed_cells=report["completed_cells"],complete_cell_search=report["complete_cell_search"],
        whole_prefix_no_planar_parameter_open_piece_proved=report[
            "whole_prefix_no_planar_parameter_open_piece_proved"],
        exact_planar_cell_indices=report["exact_planar_cell_indices"],
        exact_nonplanar_completed_cells=sum(r["nonzero_four_point_witness"]
                                            for r in report["completed_cell_status"]),
        actual_completed_point_count=sum(r["attempted_candidates"] for r in report["completed_cell_status"]),
        complete_grid_and_per_cell_witnesses_original_member=original_member,
        pending=pending)


def compact_tail(report, original_member):
    successful_ranges=[]
    failed=[]
    candidate_counts={}
    arithmetic_counts={}
    sign_counts={}
    successes=successful_pieces=completed_attempts=0
    for item in report["completed_group_status"]:
        completed_attempts+=len(item["attempts"])
        if not item["nonzero_polynomial_witness_found"]:
            # Keep every failed group, its original piece addresses and every
            # attempted candidate.  An extreme failure list may still exceed
            # LIMIT and must take the existing honest readback-70 branch.
            failed.append(copy.deepcopy(item))
            continue
        index=item["group"]["index"]
        if successful_ranges and successful_ranges[-1][1]==index:
            successful_ranges[-1][1]=index+1
        else:
            successful_ranges.append([index,index+1])
        successes+=1
        successful_pieces+=len(item["group"]["actual_piece_indices"])
        attempt=item["attempts"][-1]
        for counts,key in ((candidate_counts,attempt["candidate_index"]),
                           (arithmetic_counts,attempt["arithmetic"]),
                           (sign_counts,attempt["strict_sign"])):
            counts[key]=counts.get(key,0)+1
    pending=copy.deepcopy(report["pending"])
    current=pending["current_group"]
    pending["current_group_definition"]=(None if current is None
        else copy.deepcopy(report["complete_groups"][current]))
    return dict(total_polynomial_groups=report["total_polynomial_groups"],
        completed_groups=report["completed_groups"],complete_group_attempts=report["complete_group_attempts"],
        whole_tail_collar_patch_no_planar_parameter_open_piece_proved=report[
            "whole_tail_collar_patch_no_planar_parameter_open_piece_proved"],
        all_original_radial_piece_count=report["all_original_radial_piece_count"],
        completed_attempt_count=completed_attempts,
        successful_group_count=successes,
        successful_group_indices_half_open_ranges=successful_ranges,
        successful_original_radial_piece_count=successful_pieces,
        successful_candidate_index_counts=[dict(candidate_index=key,count=candidate_counts[key])
                                           for key in sorted(candidate_counts)],
        successful_arithmetic_counts=arithmetic_counts,
        successful_strict_sign_counts=[dict(strict_sign=key,count=sign_counts[key])
                                       for key in sorted(sign_counts)],
        completed_unproved_group_count=len(failed),completed_unproved_groups=failed,
        complete_group_definitions_identity=identity(report["complete_groups"]),
        complete_original_group_status_identity=identity(report["completed_group_status"]),
        all_nonzero_witness_matrices_and_complete_groups_original_member=original_member,
        successful_payload_scope=("Successful group definitions, all piece lists and individual "
            "witness attempts stay in the identified complete temporary result and ledger. "
            "Only their complete group-index ranges, counts and actual attempt distributions "
            "are returned here; their individual numerical witnesses are not claimed returned."),
        pending=pending)


def produce(args):
    actions()
    for name in ("computations","directory","witness_plan","cuff_atlas","out"):
        setattr(args,name,Path(getattr(args,name)))
    args.out=temporary_output(args)
    args.position_radius_goal=rational(args.position_radius_goal)
    if (not 0<=args.active_depth<=30 or args.position_max_depth<0
            or not 64<=args.interval_bits<=8192 or not 16<=args.sqrt_bits<=4096
            or args.position_radius_goal<=0 or not math.isfinite(args.budget_seconds)
            or args.budget_seconds<=0 or args.free_bytes_reserve<0
            or min(args.max_position_cells,args.max_prefix_points,args.max_tail_witnesses)<=0):
        raise ValueError("Use finite explicit work resources, not inferred scientific thresholds")
    args.out.mkdir(parents=True)
    large=args.out/"large-arrays"
    large.mkdir()
    budget=Budget(args)
    previous_handlers={number:signal.getsignal(number) for number in (signal.SIGTERM,signal.SIGINT)}
    for number in previous_handlers:
        signal.signal(number,budget.signal)
    current=caps=position=prefix=tail=None
    binding=marker=witnesses=None
    saved_runtime_context=None
    members,sources,ledgers={}, {}, {}
    error=stop=None
    stage="binding"
    try:
        budget.check()
        for name,expected in SOURCE_PINS.items():
            record=receipt(args.computations/name)
            if record["sha256"]!=expected:
                raise ValueError("An actual complete defining source changed: "+name)
            sources[name]=record
        Cut,_=load(args.computations,CUT)
        Cuff,_=load(args.computations,CUFF)
        Cap,_=load(args.computations,CAP)
        Prefix,_=load(args.computations,PREFIX)
        Kernel,_=load(args.computations,KERNEL)
        Diameter,_=load(args.computations,DIAMETER)
        from flint import ctx
        saved_runtime_context=(ctx,ctx.prec)
        current=Cut.load_accurate_cut_field(args)
        active_path=Path(current.Active.__file__).resolve()
        if (active_path!=(args.computations/ACTIVE).resolve()
                or receipt(active_path)["sha256"]!=SOURCE_PINS[ACTIVE]):
            raise ValueError("The actual current six-jet module has another source owner")
        budget.check()
        atlas,atlas_row=Cuff.bound_json(args.cuff_atlas,args.cuff_atlas_sha256)
        attachment=Cuff.bind_loaded_shared_bundle(current.source_bundle,atlas)
        caps=Cap.bind_loaded_shared_bundle(current.source_bundle,atlas,attachment,args.computations)
        marker=exact_marker_inputs(caps,Prefix)
        witnesses,witness_row=witness_points(args,current,Kernel.sqrt_upper,budget)
        binding=dict(schema=SCHEMA+"-same-field-binding",source=receipt(__file__),sources=sources,
            complete_current_field_binding=copy.deepcopy(current.binding),
            original_R409_result=receipt(args.directory/"result.json"),
            actual_R413_atlas=atlas_row,current_R413_attachment=attachment,
            complete_current_cap_binding=caps.describe(),witness_plan=witness_row,
            current_actual_target_identity=copy.deepcopy(current.target.binding["complete_target_identity"]),
            no_old_renderer_or_position_packet_used=True,
            same_C_root_family_and_all10_parameters_retained=True,
            current_field_not_old_seven_tuple_renderer=True,
            reach_metric_success_not_required=True,
            resources=dict(active_depth=args.active_depth,position_max_depth=args.position_max_depth,
                position_radius_goal=str(args.position_radius_goal),interval_bits=args.interval_bits,
                sqrt_bits=args.sqrt_bits,max_position_cells=args.max_position_cells,
                max_prefix_points=args.max_prefix_points,max_tail_witnesses=args.max_tail_witnesses,
                whole_budget_seconds=args.budget_seconds,free_bytes_reserve=args.free_bytes_reserve))
        members["input_binding"]=write(args.out/"input-binding.json",binding,args.out)
        members["all_markers"]=write(args.out/"actual-complete-marker-conditions.json",marker,args.out)
        members["actual_witness_points"]=write(args.out/"actual-accurate-quarter-turn-points.json",witnesses,args.out)
        members["complete_field_piece_universe"]=write(large/"complete-current-piece-universe.json",
            dict(actual_complete_pieces=current.field.pieces,both_reflected_sheets=True,
                 fixed_caps=["upper","lower"],witnesses=identity(witnesses)),args.out)
        ledgers["positions"]=Ledger(large/"complete-current-position-cover.jsonl.gz",args.out)
        ledgers["prefix"]=Ledger(large/"complete-current-prefix-nonplanarity.jsonl.gz",args.out)
        ledgers["tail"]=Ledger(large/"complete-current-tail-nonplanarity.jsonl.gz",args.out)
        position=PositionCover(current,caps,Cap,Diameter,Kernel.sqrt_upper,args,budget,ledgers["positions"],witnesses)
        prefix=PrefixProof(current.field,Prefix,args,budget,ledgers["prefix"])
        tail=TailProof(current,Prefix,args,budget,ledgers["tail"])
        stage="whole_closed_position_cover"
        position.run()
        stage="complete_prefix_nonplanarity"
        prefix.run()
        stage="complete_tail_collar_patch_nonplanarity"
        tail.run()
        stage="all_requested_consumption_returned"
    except Stop as exc:
        stop=dict(type=type(exc).__name__,message=str(exc),stage=stage)
    except Exception as exc:
        error=dict(type=type(exc).__name__,message=str(exc),stage=stage)
    finally:
        for name,ledger in ledgers.items():
            members["ledger_"+name]=ledger.close()
        for number,handler in previous_handlers.items():
            signal.signal(number,handler)
        if saved_runtime_context is not None:
            context,old_precision=saved_runtime_context
            context.prec=old_precision

    # All serializations below use original exact endpoint data.  No field
    # evaluator is called after restoring its arithmetic context.
    p_report=None if position is None else position.report()
    pre_report=None if prefix is None else prefix.report()
    tail_report=None if tail is None else tail.report()
    if p_report is not None:
        members["position_result"]=write(args.out/"whole-image-position-result.json",p_report,args.out)
    if pre_report is not None:
        members["prefix_result"]=write(large/"complete-prefix-proof-result.json",pre_report,args.out)
    if tail_report is not None:
        members["tail_result"]=write(large/"complete-tail-proof-result.json",tail_report,args.out)
        if tail.cut_binding is not None:
            members["accurate_cut_difference_binding"]=write(large/"actual-current-C-cut-differences.json",
                                                           tail.cut_binding,args.out)
    if current is not None:
        members["actual_used_field_identity"]=write(large/"actual-used-complete-field-identity.json",
                                                   current.expression_identity(),args.out)
    all_germs=(pre_report is not None and tail_report is not None
        and pre_report["whole_prefix_no_planar_parameter_open_piece_proved"]
        and tail_report["whole_tail_collar_patch_no_planar_parameter_open_piece_proved"])
    has_change=p_report is not None and p_report["whole_image_change_proved"]
    markers_paid=marker is not None and marker["R238_marker_algebra_paid"]
    conditional=bool(all_germs and has_change and markers_paid)
    result=dict(schema=SCHEMA,source=receipt(__file__),source_pins=SOURCE_PINS,
        actual_input_binding_identity=None if binding is None else identity(binding),
        producer_elapsed_seconds=time.monotonic()-budget.start,
        time_includes_input_binding_and_setup=True,budget_is_boundary_checked_not_hard_kill=True,
        current_stage=stage,error=error,resource_stop=stop,
        resource_partial=stop is not None,external_signal=budget.signal_number,
        actual_work_counts=budget.counts,position=p_report,prefix=pre_report,tail=tail_report,
        marker_conditions=marker,actual_witness_parameters_and_boxes=witnesses,
        all_requested_consumption_returned=stage=="all_requested_consumption_returned",
        complete_current_active_nonplanarity_proved=all_germs,
        same_field_R238_marker_conditions_paid=markers_paid,
        same_field_whole_continuous_image_change_proved=has_change,
        all_R238_hypotheses_except_global_embedding_paid=conditional,
        conditional_Euclidean_quotient_distance_strictly_positive_if_same_field_embedding=conditional,
        orthogonal_group_includes_reflections=True,
        quantitative_delta_E_lower_not_computed=True,
        actual_global_closed_embedding_certified=False,actual_delta_E_certified=False,
        actual_reach_or_metric_or_same_g_refinement_certified=False,
        original_native_RK_to_current_accurate_field_error_certified=False,
        no_new_native_BVP_or_parent_acceptance=True,task_completed=False,
        unstarted_scope=dict(
            original_full_binding_unpaid=current is None or binding is None,
            whole_closed_positions_unstarted=budget.counts["position_cells"]==0,
            all_prefix_cells_unstarted=budget.counts["prefix_points"]==0,
            all_tail_collar_patch_groups_unstarted=budget.counts["tail_witnesses"]==0),
        members=members,
        large_payload_scope="Temporary complete own ledgers/identities only; no raw encoding, split transport, artifacts, Git or Release data")
    result_row=write(args.out/"result.json",result,args.out)
    summary={key:value for key,value in result.items()
             if key not in ("prefix","tail","actual_witness_parameters_and_boxes","source_pins")}
    summary["original_result"]=result_row
    summary["complete_defining_sources_identity"]=identity(SOURCE_PINS)
    summary["prefix"]=(None if pre_report is None else compact_prefix(pre_report,members["prefix_result"]))
    summary["tail"]=(None if tail_report is None else compact_tail(tail_report,members["tail_result"]))
    summary["witness_points_original_member"]=members.get("actual_witness_points")
    summary["scientific_scope"]=("All original active pieces, both reflected sheets, both entire marked caps and complete F0 D. "
        "Prefix R254 kernels; tail R274 same-radius cancellation with current accurate C cut multipliers. "
        "Exact witnesses remain temporary and are identified, not claimed locally read row by row. "
        "Positive delta_E remains conditional on the same field's actual global embedding.")
    payload=canonical(summary)
    if len(payload)>LIMIT:
        fallback=dict(schema=SCHEMA+"-necessary-readback-over-budget",attempted_bytes=len(payload),
            attempted_sha256=digest(payload),original_result=result_row,
            complete_necessary_readback=False,scientific_result_not_replaced=True,
            actual_global_closed_embedding_certified=False,actual_delta_E_certified=False)
        write(args.out/"necessary-readback-over-budget.json",fallback,args.out)
        print("BEGIN_R425_CURRENT_C_HELD_RIGIDITY_SUMMARY",flush=True)
        print(canonical(fallback).decode(),end="",flush=True)
        print("END_R425_CURRENT_C_HELD_RIGIDITY_SUMMARY",flush=True)
        return 70
    path=args.out/"necessary-summary.json"
    with path.open("xb") as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())
    print("BEGIN_R425_CURRENT_C_HELD_RIGIDITY_SUMMARY",flush=True)
    print(payload.decode(),end="",flush=True)
    print("END_R425_CURRENT_C_HELD_RIGIDITY_SUMMARY",flush=True)
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"],"a",encoding="utf-8") as stream:
            stream.write("current_held_summary="+str(path)+"\n")
            stream.write("current_held_summary_bytes="+str(len(payload))+"\n")
            stream.write("current_held_summary_sha256="+digest(payload)+"\n")
    if budget.signal_number is not None:
        return 128+budget.signal_number
    return 1 if error is not None else 0


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--computations",type=Path,required=True)
    parser.add_argument("--directory",type=Path,required=True)
    parser.add_argument("--result-sha256",required=True)
    parser.add_argument("--checkpoint-directory",type=Path)
    parser.add_argument("--proof-directory",type=Path)
    parser.add_argument("--cuff-atlas",type=Path,required=True)
    parser.add_argument("--cuff-atlas-sha256",required=True)
    parser.add_argument("--witness-plan",type=Path,required=True)
    parser.add_argument("--witness-plan-sha256",required=True)
    parser.add_argument("--active-depth",type=int,required=True)
    parser.add_argument("--position-max-depth",type=int,required=True)
    parser.add_argument("--position-radius-goal",required=True)
    parser.add_argument("--interval-bits",type=int,required=True)
    parser.add_argument("--sqrt-bits",type=int,required=True)
    parser.add_argument("--max-position-cells",type=int,required=True)
    parser.add_argument("--max-prefix-points",type=int,required=True)
    parser.add_argument("--max-tail-witnesses",type=int,required=True)
    parser.add_argument("--budget-seconds",type=float,required=True)
    parser.add_argument("--free-bytes-reserve",type=int,default=2147483648)
    parser.add_argument("--out",type=Path,required=True)
    return produce(parser.parse_args(argv))


if __name__=="__main__":
    raise SystemExit(main())
