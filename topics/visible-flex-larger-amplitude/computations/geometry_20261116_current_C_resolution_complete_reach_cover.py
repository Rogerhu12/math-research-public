#!/usr/bin/env python3
"""R422: the complete closed pair universe of the actual R416/R417 field.

This is an independent geometry consumer, not a native solver or new native
acceptance gate.  The real R400 accepted450/R409 input guards are retained.
R416 supplies the independent exact cut patch and all active six jets; R417
and R413 bind the complete unchanged Cartesian graph caps and original cuff.
R279, R241, R280/R281 and R282 are reused for their proved responsibilities.
No old finite-field loader, sampled mesh, old reach result or old target is
relabelled as the current field.  All mathematical execution is Actions-only.

Full cell/pair/phase ledgers are temporary runner outputs.  Return one genuine
necessary summary of at most 90000 bytes, without splitting or encoding raw.
Author: OpenAI / ChatGPT geometry agent, 2026-11-15.
"""
from __future__ import annotations

import argparse
from collections import Counter, OrderedDict
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
from types import SimpleNamespace

REPOSITORY = "Rogerhu12/math-research-public"
HERE = Path(__file__).resolve().parent
SCHEMA = "R441-current-C-resolution450-complete-closed-reach-cover-v1"
LIMIT = 90000
CUT = "geometry_20261116_current_C_resolution_accurate_cut_patch.py"
CUFF = "geometry_20261116_current_C_resolution_original_cuff_atlas.py"
CAP = "geometry_20261116_current_C_resolution_fixed_cap_balls.py"
ACTIVE = "geometry_20261115_shared_active_interval_balls.py"
LOCAL = "geometry_20261115_local_cuff_cross_gram_owner.py"
PHASE = "geometry_20261115_rational_phase_cover.py"
JOINT = "geometry_20261115_joint_phase_normal_balls.py"
KERNEL = "root_mixed_phase_normal_balls.py"
DIAMETER = "geometry_20261115_shared_curvature_diameter_budget.py"
SOURCE_PINS = {
    CUT: "8811f89c7395bb4aed1adabe6c6825c801e1e41a9d80d416b0a4746596ae9a52",
    CUFF: "d0b03a367f3ece13b06949d5218a992e6ee3e9a41364499070d3f5f475a150a0",
    CAP: "ca53bdc5c0cdd5764065301f0edb1259d083fdffa9f3d767a5a38b4a7cafe364",
    ACTIVE: "675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b",
    LOCAL: "0b52a408e08a12c1a16594658510b589ce20d9b2a75430ed5676869e12290456",
    PHASE: "f6214d1dc66f9890e99f5d9bbbc93fa0e6524acd6ac879f0058ea023ebc17537",
    JOINT: "c5548f28bfe56a283403a7d16e1879c1c1243d0a0bc80761586fe50e1aec1466",
    KERNEL: "ecea0ef58aa5755270807596da5512552ac52fab27e90492fcf85fab095716c6",
    DIAMETER: "b1c2dfb9bd99c0777805da938c38e428da32db8ed5fa6238c9433ed9aede5ad0",
}


def actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("Execute geometric arithmetic only in the named public Actions")


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
        ensure_ascii=False, allow_nan=False) + "\n").encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def identity(value):
    raw = canonical(value)
    return dict(canonical_bytes=len(raw), canonical_sha256=sha(raw))


def strings(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {key: strings(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [strings(item) for item in value]
    return value


def rational(value):
    if isinstance(value, bool) or not isinstance(value, (Q, str, int)):
        raise ValueError("Use exact rational text for proposed constants")
    return Q(value)


def receipt(path, root=None):
    path = Path(path)
    size, digest = 0, hashlib.sha256()
    with path.open("rb") as stream:
        for raw in iter(lambda: stream.read(1048576), b""):
            size += len(raw)
            digest.update(raw)
    return dict(file=str(path.relative_to(root)) if root is not None else path.name,
                bytes=size, sha256=digest.hexdigest())


def write(path, value, root):
    raw = canonical(strings(value))
    with Path(path).open("xb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    return receipt(path, root)


def load(directory, name):
    actions()
    path = (Path(directory) / name).resolve()
    row = receipt(path)
    if row["sha256"] != SOURCE_PINS[name]:
        raise ValueError("A defining source differs: " + name)
    module_name = "_R422_" + name[:-3]
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError("Missing pinned module loader")
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
        self.requested_signal = None
        self.cell_attempts = self.pair_attempts = 0

    def signal(self, number, _frame):
        # Do not interrupt a ledger/retirement transaction midway.  The next
        # explicit boundary preserves the entire unretired current stack.
        self.requested_signal = number

    def check(self, kind=None):
        if self.requested_signal is not None:
            raise Stop("external_signal_" + str(self.requested_signal))
        if time.monotonic() - self.start >= self.args.budget_seconds:
            raise Stop("declared_whole_consumer_wall_budget")
        if shutil.disk_usage(self.args.out).free < self.args.free_bytes_reserve:
            raise Stop("owned_output_disk_reserve")
        if kind == "cell" and self.cell_attempts >= self.args.max_cells:
            raise Stop("closed_curvature_cell_attempt_budget")
        if kind == "pair" and self.pair_attempts >= self.args.max_pair_nodes:
            raise Stop("complete_pair_space_phase_node_budget")


class Ledger:
    def __init__(self, path, root):
        self.path, self.root = Path(path), Path(root)
        self.raw = self.path.open("xb")
        self.z = gzip.GzipFile(filename="", fileobj=self.raw, mode="wb", mtime=0)
        self.rows = self.decoded_bytes = 0
        self.digest = hashlib.sha256()

    def add(self, row):
        raw = canonical(strings(dict(ordinal=self.rows, **row)))
        self.z.write(raw)
        self.z.flush()
        self.digest.update(raw)
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
                    decoded_bytes=self.decoded_bytes, decoded_sha256=self.digest.hexdigest())


def iv(row):
    a, b = Q(row["lower"]), Q(row["upper"])
    if a > b:
        raise ValueError("Reversed actual interval")
    return a, b


def norm_upper(rows, sqrt_upper, bits):
    return sqrt_upper(sum((max(abs(a), abs(b)) ** 2 for a, b in map(iv, rows)), Q(0)), bits)


def phase_distance(pair, kernel, bits, tau):
    """R37 full-circle distance; no normal or phase sample is required."""
    p, q = pair[0]["center"], pair[1]["center"]
    A = sum(x*x for x in p[:2]) + sum(x*x for x in q[:2]) + (q[2]-p[2])**2
    B, C = q[0]*p[0]+q[1]*p[1], -q[0]*p[1]+q[1]*p[0]
    lower = max(Q(0), A-2*kernel.sqrt_upper(B*B+C*C, bits))
    threshold = 2*tau + pair[0]["radius"] + pair[1]["radius"]
    return dict(certified=lower >= threshold*threshold,
        owner="R37_complete_circle_distance", squared_lower=str(lower),
        squared_required=str(threshold*threshold), equality_retained=True,
        entire_phase_circle_not_endpoints=True)


def static_gates(pair, kernel, bits, tau):
    """R37/R280 at the same phase: distance OR both old ends OR joint."""
    a, b = pair
    d = tuple(y-x for x, y in zip(a["center"], b["center"]))
    d2 = kernel.dot(d, d)
    D = kernel.sqrt_upper(d2, bits)
    e = a["radius"] + b["radius"]
    distance = d2 >= (2*tau+e)**2
    margins = []
    for cell in pair:
        if cell["normal"] is None:
            margins.append(None)
            continue
        n, eta = cell["normal"], cell["normal_radius"]
        if not kernel.normal_ball_possible(n, eta):
            raise ValueError("The bound normal ball cannot contain a unit vector")
        cross2 = d2*kernel.dot(n, n)-kernel.dot(d, n)**2
        margins.append(cross2-(e+eta*D)**2)
    joint = None if any(x is None for x in margins) else sum(margins, Q(0))
    gates = dict(distance=distance,
        left=margins[0] is not None and margins[0] > 0,
        right=margins[1] is not None and margins[1] > 0,
        joint=joint is not None and joint > 0)
    return dict(certified=any(gates.values()), owner="R37_R280_static_OR",
        gates=gates, squared_center_distance=str(d2), center_distance_upper=str(D),
        distance_squared_margin=str(d2-(2*tau+e)**2),
        endpoint_squared_margins=[None if x is None else str(x) for x in margins],
        joint_squared_margin=None if joint is None else str(joint),
        zero_chord_also_excluded_by_each_passing_static_gate=True)


def phase_row(left, right, tau):
    if left["normal"] is None or right["normal"] is None:
        return None
    row = dict(tau=str(tau))
    for prefix, cell in (("moving", left), ("fixed", right)):
        row[prefix+"_position"] = list(map(str, cell["center"]))
        row[prefix+"_position_radius"] = str(cell["radius"])
        row[prefix+"_normal_centre"] = list(map(str, cell["normal"]))
        row[prefix+"_normal_radius"] = str(cell["normal_radius"])
    return row


def circular_difference_upper(a, b):
    """Exact supremum on two closed period-one intervals, including 0=1."""
    lo, hi = b[0]-a[1], b[1]-a[0]
    if not -1 <= lo <= hi <= 1:
        raise ValueError("Use actual normalized physical-angle cells")
    distance = lambda x: min(abs(x), abs(x-1), abs(x+1))
    result = max(distance(lo), distance(hi))
    if lo <= Q(1, 2) <= hi or lo <= Q(-1, 2) <= hi:
        result = Q(1, 2)
    return result


def cell_scope(cell, caps_module, cuff):
    if cell["kind"] == "active":
        return dict(kind="active", sheet="lower" if cell["lower"] else "upper",
            piece_index=cell["piece_index"], root_cell_id=cell["root_cell_id"],
            radial=list(map(str, cell["radial"])),
            normalized_physical_angle=list(map(str, cell["angular"])))
    return dict(kind="cap", side="upper" if cell["upper"] else "lower",
        root_cell_id=cell["root_cell_id"], quadtree_path=cell["cap_path"],
        Cartesian_box=strings(caps_module.dyadic_box(cuff, cell["cap_path"])),
        domain="this entire closed rectangle intersected with the original closed cuff disk")


def node_scope(node, caps_module, cuff):
    out = dict(path=node["path"], depth=node["depth"], spatial_depth=node["spatial_depth"],
        left=cell_scope(node["left"], caps_module, cuff),
        right=cell_scope(node["right"], caps_module, cuff))
    if node.get("chart") is not None:
        out.update(phase_chart=node["chart"], closed_phase_interval=list(map(str, node["phase"])))
    else:
        out["phase_responsibility"] = "AA common rotation or CC fixed; the static pair covers all real phases"
    return out


def split_cell(cell, coordinate):
    if cell["kind"] == "cap":
        return [dict(cell, cap_path=cell["cap_path"]+str(i)) for i in range(4)]
    interval = cell[coordinate]
    middle = sum(interval, Q(0))/2
    return [dict(cell, **{coordinate: value}) for value in
        ((interval[0], middle), (middle, interval[1]))]


def split_pair(node, family):
    if family == "AA":
        choices = (("left", "radial"), ("left", "angular"),
                   ("right", "radial"), ("right", "angular"))
    elif family == "CC":
        choices = (("left", "cap"), ("right", "cap"))
    else:
        choices = (("left", "radial"), ("left", "angular"),
                   ("right", "cap"), ("phase", None))
    side, coordinate = choices[node["depth"] % len(choices)]
    if side == "phase":
        a, b = node["phase"]
        middle = (a+b)/2
        values = ((a, middle), (middle, b))
    else:
        values = split_cell(node[side], coordinate)
    children = []
    for index, value in enumerate(values):
        child = dict(node, path=node["path"]+str(index), depth=node["depth"]+1,
                     spatial_depth=node["spatial_depth"]+(side != "phase"))
        child["phase" if side == "phase" else side] = value
        children.append(child)
    return dict(endpoint=side, coordinate=coordinate,
        all_children_closed=True, shared_boundaries_retained=True), children


class CurrentGeometry:
    def __init__(self, args, modules, current, caps, spatial):
        self.args, self.current, self.field, self.caps = args, current, current.field, caps
        self.M, self.Cap = current.Active, modules[CAP]
        self.kernel, self.spatial = modules[KERNEL], spatial
        self.cache = OrderedDict()
        self.fresh_active = self.fresh_cap = 0
        self.K, self.tau = rational(args.curvature_upper), rational(args.target_reach)
        self.outward = self.validate_meridian()
        self.piece_U = {i: None for i in range(len(self.field.pieces))}
        self.piece_V = {i: None for i in range(len(self.field.pieces))}
        self.meridian = None
        self.curvature_complete = False
        self.derivatives_complete = False
        self.cap_global = {}
        for upper in (False, True):
            own = [m for m in caps.markers if m["upper"] is upper]
            self.cap_global[upper] = dict(
                Hessian=sum((8*abs(m["amplitude"])/m["radius"]**2 for m in own), Q(0)),
                gradient=sum((8*abs(m["amplitude"])/m["radius"] for m in own), Q(0)),
                marker_indices=[m["index"] for m in own])

    def validate_meridian(self):
        pieces = self.field.pieces
        prefix = [i for i, p in enumerate(pieces) if p["kind"] == "prefix"]
        radial = [i for i, p in enumerate(pieces) if p["kind"] != "prefix"]
        if not prefix or not radial:
            raise ValueError("Retain the complete actual prefix and radial pieces")
        prefix.sort(key=lambda i: pieces[i]["left"])
        radial.sort(key=lambda i: pieces[i]["right"], reverse=True)
        cursor = Q(0)
        for i in prefix:
            p = pieces[i]
            if p["left"] != cursor or not p["left"] < p["right"]:
                raise ValueError("The actual prefix has a gap or a degenerate piece")
            cursor = p["right"]
        if cursor != self.field.x[-1]:
            raise ValueError("The real prefix end changed")
        cursor = self.field.cut
        for i in radial:
            p = pieces[i]
            if p["right"] != cursor or not p["left"] < p["right"]:
                raise ValueError("The original outward radial chain has a gap")
            cursor = p["left"]
        if cursor != self.field.cuff:
            raise ValueError("The actual closed radial chain does not reach the original cuff")
        return [(i, 1) for i in prefix] + [(i, -1) for i in radial]

    def empty(self, cell):
        if cell["kind"] == "active":
            return False
        box = self.Cap.dyadic_box(self.caps.cuff, cell["cap_path"])
        return self.caps.cap.minimum_distance_squared(box, (Q(0), Q(0))) > self.caps.cuff**2

    def data(self, cell, spatial_depth, curvature=False):
        bits = self.args.sqrt_bits+spatial_depth
        precision = self.args.interval_bits+spatial_depth
        self.M.ctx.prec = precision
        description = cell_scope(cell, self.Cap, self.caps.cuff)
        key = sha(canonical(dict(cell=description, precision_bits=precision,
            sqrt_bits=bits, R279_K=str(self.K) if curvature else None)))
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        if self.empty(cell):
            data = dict(empty=True, spatial_id=key, scope=description)
            raw = dict(kind="exact_empty_closed_disk_intersection", **data)
        elif cell["kind"] == "active":
            self.fresh_active += 1
            p = self.field.pieces[cell["piece_index"]]
            record = self.M.certify_cell(self.field, p, cell["radial"], cell["angular"],
                cell["lower"], self.kernel.sqrt_upper, bits, self.K if curvature else None)
            record.update(piece_index=cell["piece_index"], piece_kind=p["kind"],
                sheet="lower" if cell["lower"] else "upper", cell_id=cell["root_cell_id"])
            normal = tuple(map(Q, record["moving_normal_centre"])) if record["normal_ball_certified"] else None
            data = dict(empty=False, spatial_id=key, scope=description,
                center=tuple(map(Q, record["moving_position"])), radius=Q(record["moving_position_radius"]),
                normal=normal, normal_radius=Q(record["moving_normal_radius"]) if normal is not None else None,
                position_box=tuple(map(iv, record["position_interval_box"])), original=record,
                U=norm_upper(record["six_jets"]["u"], self.kernel.sqrt_upper, bits),
                V=norm_upper(record["six_jets"]["q"], self.kernel.sqrt_upper, bits),
                regular=Q(record["squared_cross_lower"]) > 0,
                curvature_paid=record.get("R279", {}).get("strict_curvature_bound") is True)
            raw = dict(kind="original_675_complete_closed_active_cell", **data,
                exact_field="R416 independent accurate cut field; old source_bundle A renderer not used")
        else:
            self.fresh_cap += 1
            record = self.caps.cell(cell["cap_path"], cell["upper"], bits)
            ball = record["original_ball_record"]
            data = dict(empty=False, spatial_id=key, scope=description,
                center=tuple(map(Q, ball["fixed_position"])), radius=Q(ball["fixed_position_radius"]),
                normal=tuple(map(Q, ball["fixed_normal_centre"])), normal_radius=Q(ball["fixed_normal_radius"]),
                position_box=tuple(map(iv, record["Cartesian_six_jets"]["value"])), original=record,
                regular=True, curvature_paid=Q(record["curvature"]["both_principal_curvature_absolute_upper"]) <= self.K)
            raw = dict(kind="original_R417_complete_closed_cap_cell", **data)
        self.spatial.add(raw)
        self.cache[key] = data
        while len(self.cache) > self.args.cache_entries:
            self.cache.popitem(last=False)
        return data

    def record_derivatives(self, cell, data):
        if cell["kind"] != "active" or data["empty"]:
            return
        index = cell["piece_index"]
        for target, key in ((self.piece_U, "U"), (self.piece_V, "V")):
            target[index] = data[key] if target[index] is None else max(target[index], data[key])

    def finish_meridian(self, complete):
        self.derivatives_complete = complete and all(v is not None for v in self.piece_U.values())
        if not self.derivatives_complete:
            return None
        offset, rows = Q(0), {}
        for index, direction in self.outward:
            piece = self.field.pieces[index]
            U = self.piece_U[index]
            length = U*(piece["right"]-piece["left"])
            rows[index] = dict(offset=offset, U=U, direction=direction,
                               left=piece["left"], right=piece["right"], length=length)
            offset += length
        self.meridian = rows
        return dict(outward_chain=[dict(piece_index=i, **rows[i]) for i, _ in self.outward],
            signed_lower_sheet_is_negative_outward_coordinate=True,
            maximum_angular_speed=max(self.piece_V.values()),
            piece_angular_speeds=self.piece_V,
            common_physical_q_seam_identification="R400/R409/R416 use the same original Phi and physical phi at every active seam",
            prefix_s_and_radial_r_scales_not_identified=True,
            exact_coordinate_transitions_paid_by_R409_and_R416=True)

    def signed_S(self, cell):
        row = self.meridian[cell["piece_index"]]
        lo, hi = cell["radial"]
        a, b = ((lo-row["left"], hi-row["left"]) if row["direction"] == 1 else
                (row["right"]-hi, row["right"]-lo))
        interval = (row["offset"]+row["U"]*a, row["offset"]+row["U"]*b)
        return (-interval[1], -interval[0]) if cell["lower"] else interval

    def short_path(self, family, left, right):
        if not self.curvature_complete:
            return dict(certified=False, reason="whole_actual_curvature_bound_not_paid")
        pi_lower, _ = self.M.bounds(self.M.arb.pi())
        if family == "AA" and self.meridian is not None:
            a, b = self.signed_S(left), self.signed_S(right)
            radial = max(abs(x-y) for x in a for y in b)
            angular = circular_difference_upper(left["angular"], right["angular"])
            V = max(self.piece_V.values())
            length = radial + V*angular
            detail = dict(signed_path_coordinate_intervals=[list(map(str, a)), list(map(str, b))],
                radial_path_upper=str(radial), complete_q_circle_difference_upper=str(angular),
                complete_angular_speed_upper=str(V),
                common_material_inverse_transport_then_common_rotation=True,
                physical_q_shift_identified_with_material_theta_shift=False)
        elif family == "CC" and left["upper"] == right["upper"]:
            a = self.Cap.dyadic_box(self.caps.cuff, left["cap_path"])
            b = self.Cap.dyadic_box(self.caps.cuff, right["cap_path"])
            distance2 = sum((max(abs(x-y) for x in u for y in v)**2 for u, v in zip(a, b)), Q(0))
            gradient = self.cap_global[left["upper"]]["gradient"]
            length = self.kernel.sqrt_upper((1+gradient**2)*distance2, self.args.sqrt_bits)
            detail = dict(straight_parameter_segment_in_the_same_convex_closed_disk=True,
                squared_Cartesian_parameter_distance_upper=str(distance2),
                complete_side_gradient_upper=str(gradient))
        else:
            return dict(certified=False, reason="no_actual_common_path_of_this_type_asserted")
        return dict(certified=self.K*length < pi_lower, owner="R241_uniform_actual_short_path",
            complete_closed_path_length_upper=str(length), K=str(self.K),
            exact_lower_bound_for_pi=str(pi_lower), strict_K_length_below_pi=self.K*length < pi_lower,
            different_material_points_only_with_original_quotient=True, **detail)

    def same_cap_graph(self, left, right):
        if left["kind"] != "cap" or right["kind"] != "cap" or left["upper"] != right["upper"]:
            return dict(certified=False, reason="not_the_same_exact_Cartesian_graph_disk")
        row = self.cap_global[left["upper"]]
        return dict(certified=row["Hessian"]*self.tau <= 1,
            owner="R24_same_graph_convex_disk_normal_chord_and_injectivity",
            complete_side_Hessian_upper=str(row["Hessian"]), tau=str(self.tau),
            Hessian_times_tau=str(row["Hessian"]*self.tau),
            complete_marker_indices=row["marker_indices"], overlapping_and_negative_markers_retained=True,
            exact_same_Cartesian_point_identified_only_as_the_same_material_point=True,
            R24_weak_marker_transfer_or_support_distance_claimed=False)


class Roots:
    """The exact original closed active grid plus the two whole cap disks."""
    def __init__(self, geometry, depth):
        self.G, self.depth = geometry, depth
        self.division = 1 << depth
        self.per_piece = self.division*self.division
        self.per_sheet = len(geometry.field.pieces)*self.per_piece
        self.active_count = 2*self.per_sheet
        self.count = self.active_count+2
        self.AA = self.active_count*(self.active_count+1)//2
        self.CC = 3
        self.AC = 2*self.active_count
        self.pair_count = self.AA+self.CC+self.AC

    def cell(self, index):
        if not 0 <= index < self.count:
            raise IndexError("Root outside the complete fixed universe")
        if index >= self.active_count:
            upper = index == self.active_count
            return dict(kind="cap", upper=upper, cap_path="",
                root_cell_id="cap/"+("upper" if upper else "lower"))
        side, within = divmod(index, self.per_sheet)
        piece_index, within = divmod(within, self.per_piece)
        ri, qi = divmod(within, self.division)
        piece = self.G.field.pieces[piece_index]
        a, b = piece["left"], piece["right"]
        radial = (a+(b-a)*Q(ri, self.division), a+(b-a)*Q(ri+1, self.division))
        angular = (Q(qi, self.division), Q(qi+1, self.division))
        return dict(kind="active", lower=bool(side), piece_index=piece_index,
            radial=radial, angular=angular,
            root_cell_id=f"{'lower' if side else 'upper'}/{piece_index}/{ri}/{qi}")

    def pairs(self):
        rank = 0
        for i in range(self.active_count):
            for j in range(i, self.active_count):
                yield rank, "AA", i, j
                rank += 1
        for i in range(self.active_count, self.count):
            for j in range(i, self.count):
                yield rank, "CC", i, j
                rank += 1
        for i in range(self.active_count):
            for j in range(self.active_count, self.count):
                yield rank, "AC", i, j
                rank += 1
        if rank != self.pair_count:
            raise AssertionError("The complete root-pair enumeration lost a rank")

    def describe(self):
        return dict(active_depth=self.depth, division=self.division,
            original_675_cell_specs_index_order_retained=True,
            active_cells=self.active_count, cap_roots=2, total_closed_roots=self.count,
            active_pieces=strings(self.G.field.pieces),
            both_reflected_sheets=True, full_closed_physical_q_interval=["0", "1"],
            every_piece_including_collars_and_accurate_cut_patch=True,
            cap_domains="both complete original Cartesian disks, not their bounding squares",
            AA_unordered_including_same_cell=self.AA,
            CC_unordered_including_same_cap=self.CC, AC_full_cartesian_product=self.AC,
            pair_count=self.pair_count,
            rank_order="all AA i<=j, then all CC i<=j, then all AC in lexicographic root order",
            diagonal_material_quotient_retained=True,
            witness_or_old_bad_pair_list_used_as_universe=False)


class CurvatureCover:
    def __init__(self, geometry, roots, budget, ledger, image):
        self.G, self.roots, self.B, self.ledger, self.image = geometry, roots, budget, ledger, image
        self.cursor, self.stack = 0, []
        self.counts = Counter()
        self.positions_complete = self.derivatives_complete = self.regular_complete = True
        self.stop_reason = None

    def pending(self):
        return dict(current_root_index=self.cursor if self.stack else None,
            current_complete_unretired_frontier=[dict(path=n["path"], depth=n["depth"],
                cell=cell_scope(n["cell"], self.G.Cap, self.G.caps.cuff)) for n in reversed(self.stack)],
            unvisited_root_suffix=[self.cursor+int(bool(self.stack)), self.roots.count],
            terminal_unpaid_count=self.counts["unpaid"],
            terminal_unpaid_addresses="all original terminal records in the complete curvature ledger",
            boundary_points_never_omitted=True)

    def run(self):
        while self.cursor < self.roots.count:
            if not self.stack:
                self.stack = [dict(cell=self.roots.cell(self.cursor), path="", depth=0)]
            while self.stack:
                self.B.check("cell")
                node = self.stack[-1]  # Retire only after the complete event is written.
                self.B.cell_attempts += 1
                data, error = None, None
                try:
                    data = self.G.data(node["cell"], node["depth"], curvature=True)
                except (ArithmeticError, ValueError) as exc:
                    error = dict(type=type(exc).__name__, message=str(exc))
                empty = data is not None and data["empty"]
                paid = empty or (data is not None and data["regular"] and data["curvature_paid"])
                scope = dict(root_index=self.cursor, path=node["path"], depth=node["depth"],
                    cell=cell_scope(node["cell"], self.G.Cap, self.G.caps.cuff))
                if not paid and node["depth"] < self.G.args.curvature_max_depth:
                    coordinate = "radial" if node["depth"] % 2 == 0 else "angular"
                    children = [dict(cell=c, path=node["path"]+str(i), depth=node["depth"]+1)
                        for i, c in enumerate(split_cell(node["cell"], coordinate))]
                    self.ledger.add(dict(kind="curvature_closed_split", scope=scope,
                        original_spatial_id=None if data is None else data["spatial_id"],
                        evaluation_error=error,
                        children=[dict(path=c["path"], depth=c["depth"],
                            cell=cell_scope(c["cell"], self.G.Cap, self.G.caps.cuff)) for c in children],
                        no_failed_lower_bound_interpreted_as_geometric_refutation=True))
                    self.stack.pop()
                    self.stack.extend(reversed(children))
                    self.counts["splits"] += 1
                    continue
                self.ledger.add(dict(kind="curvature_closed_terminal", scope=scope,
                    paid=paid, empty_disk_intersection=empty,
                    original_spatial_id=None if data is None else data["spatial_id"],
                    evaluation_error=error,
                    reason=("R279_or_R417_complete_closed_bound" if paid else
                            "declared_refinement_depth_unpaid_not_curvature_failure")))
                if not empty:
                    if data is None:
                        self.positions_complete = self.regular_complete = False
                        if node["cell"]["kind"] == "active":
                            self.derivatives_complete = False
                    else:
                        self.image.add(data["center"], data["radius"], data["position_box"])
                        self.G.record_derivatives(node["cell"], data)
                        self.regular_complete = self.regular_complete and data["regular"]
                self.counts["empty" if empty else "paid" if paid else "unpaid"] += 1
                self.stack.pop()
            self.cursor += 1
        self.G.curvature_complete = self.counts["unpaid"] == 0 and self.regular_complete
        return self.report()

    def report(self):
        complete = self.cursor == self.roots.count and not self.stack
        self.G.curvature_complete = complete and self.counts["unpaid"] == 0 and self.regular_complete
        meridian = self.G.finish_meridian(complete and self.derivatives_complete)
        return dict(all_original_closed_roots_accounted_for=complete,
            processed_original_roots=self.cursor, planned_original_roots=self.roots.count,
            counts=dict(self.counts), actual_cell_attempts=self.B.cell_attempts,
            full_closed_immersion_proved=complete and self.regular_complete,
            full_closed_K_proved=self.G.curvature_complete, K=str(self.G.K),
            strict_R279_for_active_and_original_nonstrict_cap_Hessian_bound=True,
            full_first_jet_path_envelopes=self.G.derivatives_complete,
            meridian_path_envelope=strings(meridian),
            full_phase_curvature_reduction="R248 actual material inverse transport and common rigid rotation on active pieces; caps fixed",
            whole_phase_curvature_paid=self.G.curvature_complete,
            diameter=self.image.report(complete and self.positions_complete),
            original_K_not_reselected=True, pending=self.pending())


class PairCover:
    def __init__(self, args, G, roots, budget, ledger, modules, local):
        self.args, self.G, self.roots, self.B, self.ledger = args, G, roots, budget, ledger
        self.phase, self.joint, self.kernel, self.local = modules[PHASE], modules[JOINT], modules[KERNEL], local
        self.rank, self.current, self.stack = 0, None, []
        self.counts, self.families = Counter(), {k: Counter() for k in ("AA", "CC", "AC")}
        self.current_counts = Counter()
        self.catalog_cache = OrderedDict()

    def pending(self):
        return dict(current_unretired_root_pair=copy.deepcopy(self.current),
            current_complete_unretired_frontier=[node_scope(n, self.G.Cap, self.G.caps.cuff)
                                                 for n in reversed(self.stack)],
            unvisited_rank_suffix=[self.rank+int(self.current is not None), self.roots.pair_count],
            terminal_unpaid_leaves=self.counts["unpaid"],
            terminal_unpaid_addresses="all original terminal records in the complete pair ledger",
            original_pair_universe=self.roots.describe(),
            no_unvisited_pair_or_same_point_product_discarded=True)

    def phase_test(self, left, right, node):
        simple = phase_distance((left, right), self.kernel,
            self.args.sqrt_bits+node["spatial_depth"], self.G.tau)
        if simple["certified"]:
            return simple
        row = phase_row(left, right, self.G.tau)
        if row is None:
            return dict(certified=False, reason="a_complete_unit_normal_ball_is_unavailable",
                original_full_circle_distance=simple)
        key = (left["spatial_id"], right["spatial_id"])
        if key not in self.catalog_cache:
            base = self.joint.evaluate_joint(row, self.args.sqrt_bits+node["spatial_depth"], self.kernel)
            catalog = None if base["all_phase_distance_or_no_double_normal_pass"] else self.phase.catalog_for(row, base, self.kernel)
            self.catalog_cache[key] = (base, catalog)
            self.ledger.add(dict(kind="original_R280_R281_complete_phase_catalog",
                rank=self.rank, spatial_ids=list(key), original_input=row,
                original_full_R280_record=base, original_two_chart_catalog=catalog))
            while len(self.catalog_cache) > self.args.cache_entries:
                self.catalog_cache.popitem(last=False)
        self.catalog_cache.move_to_end(key)
        base, catalog = self.catalog_cache[key]
        if base["all_phase_distance_or_no_double_normal_pass"]:
            return dict(certified=True, owner="original_R280_full_circle_OR",
                original_full_circle_distance=simple, spatial_ids=list(key),
                original_non_strict_distance_and_both_single_ends_and_joint_retained=True)
        tests = {}
        for gate in self.phase.GATE_ORDER:
            entry = catalog[node["chart"]][gate]
            poly = list(map(Q, entry["ascending_coefficients_padded_to_degree_four"]))
            sequence = [list(map(Q, p)) for p in entry["sturm"]["sequence"]]
            tests[gate] = self.phase.strict_interval(poly, sequence, *node["phase"], self.kernel)
        passing = [gate for gate in self.phase.GATE_ORDER if tests[gate]["strict_positive"]]
        return dict(certified=bool(passing), owner="original_R281_closed_phase_OR",
            passing_gates=passing, selected_gate=passing[0] if passing else None,
            original_gate_tests=tests, spatial_ids=list(key))

    def evaluate(self, family, node):
        left_cell, right_cell = node["left"], node["right"]
        if self.G.empty(left_cell) or self.G.empty(right_cell):
            return dict(certified=True, owner="strictly_empty_original_cap_disk_intersection")
        if family == "CC":
            graph = self.G.same_cap_graph(left_cell, right_cell)
            if graph["certified"]:
                return graph
        if family != "AC":
            path = self.G.short_path(family, left_cell, right_cell)
            if path["certified"]:
                return path
        else:
            self.G.M.ctx.prec = self.args.interval_bits+node["depth"]
            piece = self.G.field.pieces[left_cell["piece_index"]]
            active = dict(sheet="lower" if left_cell["lower"] else "upper", piece_kind=piece["kind"])
            cap = dict(cap="upper" if right_cell["upper"] else "lower")
            box = self.G.Cap.dyadic_box(self.G.caps.cuff, right_cell["cap_path"])
            local = self.local.test(active, left_cell["radial"], left_cell["angular"],
                cap, box, node["chart"], node["phase"], node["depth"])
            if local["certified"]:
                return dict(certified=True, owner="original_R282_same_material_cuff_cross_Gram", original_local=local)
        left = self.G.data(left_cell, node["spatial_depth"])
        right = self.G.data(right_cell, node["spatial_depth"])
        if left["empty"] or right["empty"]:
            return dict(certified=True, owner="strictly_empty_original_cap_disk_intersection")
        if family == "AC":
            record = self.phase_test(left, right, node)
            record["original_local_attempt"] = local
        else:
            record = static_gates((left, right), self.kernel,
                self.args.sqrt_bits+node["spatial_depth"], self.G.tau)
            record["actual_short_path_attempt"] = path
            if family == "CC":
                record["same_graph_attempt"] = graph
            record["simultaneous_motion"] = "both-active-common-rotation" if family == "AA" else "both-caps-fixed"
            record["spatial_ids"] = [left["spatial_id"], right["spatial_id"]]
        return record

    def run(self):
        for rank, family, i, j in self.roots.pairs():
            if rank != self.rank:
                raise AssertionError("A complete original rank was skipped")
            self.B.check()
            if self.rank >= self.args.max_pairs:
                raise Stop("complete_root_pair_budget")
            self.current = dict(rank=rank, family=family, left_root=i, right_root=j)
            self.current_counts = Counter()
            base = dict(left=self.roots.cell(i), right=self.roots.cell(j), path="", depth=0,
                        spatial_depth=0, chart=None)
            self.stack = ([dict(base, chart=c, phase=(Q(-1), Q(1))) for c in ("u", "t")]
                          if family == "AC" else [base])
            self.ledger.add(dict(kind="root_pair_begin", **self.current,
                complete_closed_roots=[node_scope(n, self.G.Cap, self.G.caps.cuff) for n in reversed(self.stack)]))
            while self.stack:
                self.B.check("pair")
                node = self.stack[-1]
                self.B.pair_attempts += 1
                try:
                    record = self.evaluate(family, node)
                except (ArithmeticError, ValueError) as exc:
                    record = dict(certified=False, owner=None,
                        reason="actual_closed_interval_evaluation_unresolved",
                        exception=dict(type=type(exc).__name__, message=str(exc)),
                        geometric_failure_inferred=False)
                scope = node_scope(node, self.G.Cap, self.G.caps.cuff)
                if record["certified"] or node["depth"] >= self.args.pair_max_depth:
                    paid = record["certified"]
                    self.ledger.add(dict(kind="root_pair_terminal", **self.current, scope=scope,
                        paid=paid, original_gate_record=record,
                        reason="proved_original_geometric_alternative" if paid else "declared_space_phase_depth_unpaid"))
                    label = record["owner"] if paid else "unpaid"
                    self.current_counts[label] += 1
                    self.counts[label] += 1
                    self.families[family][label] += 1
                    self.stack.pop()
                    continue
                split, children = split_pair(node, family)
                self.ledger.add(dict(kind="root_pair_closed_split", **self.current,
                    scope=scope, split=split, original_attempt=record,
                    complete_children=[node_scope(c, self.G.Cap, self.G.caps.cuff) for c in children]))
                self.stack.pop()
                self.stack.extend(reversed(children))
                self.current_counts["splits"] += 1
                self.counts["splits"] += 1
                self.families[family]["splits"] += 1
            paid = self.current_counts["unpaid"] == 0
            self.ledger.add(dict(kind="root_pair_end", **self.current,
                complete_closed_product_accounted_for=True, complete_pair_paid=paid,
                counts=dict(self.current_counts)))
            self.families[family]["root_pairs_processed"] += 1
            self.families[family]["root_pairs_paid"] += int(paid)
            self.counts["root_pairs_processed"] += 1
            self.counts["root_pairs_paid"] += int(paid)
            self.rank += 1
            self.current = None
        return self.report()

    def report(self):
        complete = self.rank == self.roots.pair_count and self.current is None and not self.stack
        return dict(complete_root_rank_enumeration=complete,
            processed_root_pairs=self.rank, planned_root_pairs=self.roots.pair_count,
            complete_pair_responsibility_paid=complete and self.counts["unpaid"] == 0,
            all_space_phase_nodes_attempted=self.B.pair_attempts,
            counts=dict(self.counts), by_family={key:dict(value) for key,value in self.families.items()},
            AA_and_CC_use_no_one_endpoint_phase_rotation=True,
            AC_both_closed_RP1_roots_preserved=True,
            local_cuff_owner_pays_only_actual_membership_leaves=True,
            whole_rank_not_exempted_for_containing_a_zero_chord=True,
            pending=self.pending())


def validate(args):
    K, tau = rational(args.curvature_upper), rational(args.target_reach)
    if K <= 0 or tau <= 0:
        raise ValueError("Declare positive proposed K and tau; neither is inferred or tuned here")
    depth = max(args.curvature_max_depth, args.pair_max_depth)
    if (not 0 <= args.active_depth <= 30 or not 0 <= depth <= 60
            or min(args.curvature_max_depth, args.pair_max_depth) < 0
            or not 64 <= args.interval_bits <= 8192-depth
            or not 16 <= args.sqrt_bits <= 4126-depth
            or args.max_cells < 1 or args.max_pair_nodes < 1 or args.max_pairs < 1
            or args.cache_entries < 1 or args.max_constant_levels < 1
            or not math.isfinite(args.budget_seconds) or args.budget_seconds <= 0
            or args.free_bytes_reserve < 0):
        raise ValueError("Invalid explicit geometry resource parameters")
    if args.out.exists():
        raise FileExistsError("Use a fresh owned output directory")


def necessary_summary(result, result_receipt):
    curvature = result.get("curvature")
    pairs = result.get("pairs")
    out = dict(schema=SCHEMA+"-necessary-summary", result=result_receipt,
        source=result["source"], run_id=result["run_id"], source_commit=result["source_commit"],
        stage=result["stage"], resource_partial=result["resource_partial"],
        resource_reason=result["resource_reason"], error=result["error"],
        binding=result.get("input_binding"), parameters=result["parameters"],
        complete_pair_universe=result.get("universe_counts"), ledgers=result.get("ledgers", {}),
        unstarted_scope=result["unstarted_scope"],
        other_actual_output_members=result.get("members", {}),
        accurate_family_embedding_and_reach_certified=result["accurate_family_embedding_and_reach_certified"],
        accurate_family_reach_lower=result["accurate_family_reach_lower"],
        K_times_tau=result["K_times_tau"], original_nonstrict_curvature_radius_gate=result["curvature_radius_gate"],
        original_tau_reselected=False, diameter=result.get("diameter"),
        README_reach_fraction_paid=result["README_reach_fraction_paid"],
        original_native_or_BVP_acceptance_changed=False,
        remaining_original_responsibilities=result["remaining_original_responsibilities"],
        elapsed_seconds=result["elapsed_seconds"], external_signal=result["external_signal"],
        no_raw_ledger_or_array_body_returned=True,
        full_ledger_SHA_and_count_are_not_a_local_per_value_audit=True,
        actual_field_source_and_current_G_root_family_not_replaced=True,
        original_static_base_R24_route_unchanged_but_not_assumed_paid=True,
        task_completed=False)
    if curvature is not None:
        out["curvature"] = {key: curvature[key] for key in (
            "all_original_closed_roots_accounted_for", "processed_original_roots", "planned_original_roots",
            "counts", "actual_cell_attempts", "full_closed_immersion_proved", "full_closed_K_proved", "K",
            "full_first_jet_path_envelopes", "whole_phase_curvature_paid", "pending")}
        out["curvature"]["full_meridian_envelope_identity"] = (
            None if curvature["meridian_path_envelope"] is None else identity(curvature["meridian_path_envelope"]))
    if pairs is not None:
        out["pairs"] = {key:pairs[key] for key in (
            "complete_root_rank_enumeration", "processed_root_pairs", "planned_root_pairs",
            "complete_pair_responsibility_paid", "all_space_phase_nodes_attempted", "counts", "by_family")}
        pending = copy.deepcopy(pairs["pending"])
        universe = pending.pop("original_pair_universe")
        pending["full_universe_identity"] = identity(universe)
        out["pairs"]["pending"] = pending
    return out


def produce(args):
    actions()
    validate(args)
    args.out.mkdir(parents=True, exist_ok=False)
    large = args.out/"large-arrays"
    large.mkdir()
    budget = Budget(args)
    previous_handlers = {}
    for number in (signal.SIGTERM, signal.SIGINT):
        previous_handlers[number] = signal.getsignal(number)
        signal.signal(number, budget.signal)
    old_precision = None
    saved_runtime_context = None
    modules, sources, members, ledgers = {}, {}, {}, {}
    current = G = roots = cover = pairs = None
    spatial = curvature_ledger = pair_ledger = None
    curvature = pair_report = diameter = None
    error = stop_reason = binding_receipt = None
    stage = "input_binding_and_actual_source_load"
    try:
        budget.check()
        for name in SOURCE_PINS:
            if name == ACTIVE:
                row = receipt(args.computations/name)
                if row["sha256"] != SOURCE_PINS[name]:
                    raise ValueError("The exact six-jet helper differs")
                sources[name] = row
            else:
                modules[name], sources[name] = load(args.computations, name)
        from flint import ctx
        old_precision = ctx.prec
        saved_runtime_context = ctx
        actual_args = SimpleNamespace(**vars(args))
        actual_args.interval_bits = args.interval_bits + max(args.curvature_max_depth, args.pair_max_depth)
        current = modules[CUT].load_accurate_cut_field(actual_args)
        M = current.Active
        if (Path(M.__file__).resolve() != (args.computations/ACTIVE).resolve()
                or receipt(M.__file__)["sha256"] != SOURCE_PINS[ACTIVE]):
            raise ValueError("The actual current field does not own the pinned six-jet helper")
        M.ctx.prec = args.interval_bits
        atlas, atlas_receipt = modules[CUFF].bound_json(args.cuff_atlas, args.cuff_atlas_sha256)
        attachment = modules[CUFF].bind_loaded_shared_bundle(current.source_bundle, atlas)
        caps = modules[CAP].bind_loaded_shared_bundle(current.source_bundle, atlas, attachment, args.computations)
        if caps.cuff != current.field.cuff or caps.height != current.field.B.nodal[0][0]:
            raise ValueError("Current active and fixed-cap cuff data differ")
        sources[Path(__file__).name] = receipt(__file__)
        spatial = Ledger(large/"complete-spatial-enclosures.jsonl.gz", args.out)
        curvature_ledger = Ledger(large/"complete-curvature-cover.jsonl.gz", args.out)
        pair_ledger = Ledger(large/"complete-pair-space-phase-cover.jsonl.gz", args.out)
        G = CurrentGeometry(args, modules, current, caps, spatial)
        roots = Roots(G, args.active_depth)
        members["complete_root_universe"] = write(large/"complete-root-universe.json", roots.describe(), args.out)
        budget.check()
        local = modules[LOCAL].CuffOwner(G.field, caps.markers, M, modules[KERNEL],
            sqrt_bits=args.sqrt_bits, max_constant_levels=args.max_constant_levels)
        members["actual_collar_coefficients"] = write(large/"actual-complete-collar-coefficients.json",
            local.coefficient_payload, args.out)
        members["actual_cuff_constants"] = write(large/"actual-cuff-local-constants.json", local.report(), args.out)
        members["same_accurate_cut_DAG"] = write(large/"same-accurate-cut-DAG.json", current.model.definition, args.out)
        members["complete_original_target_binding"] = write(large/"complete-original-ten-target-binding.json",
            current.target.binding, args.out)
        members["current_cap_binding"] = write(large/"current-complete-cap-binding.json", caps.describe(), args.out)
        binding = dict(schema=SCHEMA+"-input-binding", source=sources[Path(__file__).name],
            direct_sources=sources, actual_R416_binding=copy.deepcopy(current.binding),
            original_seven_tuple_binding=copy.deepcopy(current.source_bundle[-1]),
            R413_atlas=atlas_receipt, R413_attachment=copy.deepcopy(attachment),
            R417_full_marker_and_graph_binding_identity=identity(caps.describe()),
            genuine_accepted450_checkpoint=copy.deepcopy(current.binding["actual_450_checkpoint"]),
            original_ten_target_binding_identity=identity(current.target.binding),
            proposed_constants=dict(K=args.curvature_upper, tau=args.target_reach),
            constants_are_explicit_recipe_inputs_not_chosen_by_this_consumer=True,
            original_K_and_tau_not_tuned_from_an_output=True,
            R418_relative_metric_or_complete_E_query_result_required=False,
            old_source_bundle_A_used_only_for_original_provenance_not_new_patch_evaluation=True,
            phase_family="R248: actual common material inverse shift and common active rotation; both marked Cartesian caps fixed",
            all_real_phases_covered_not_only_t_endpoints=True,
            original_mean_Nyquist_FFT_Phi_and_shared_B_retained=True,
            original_scalar_target_not_replaced_by_Bprime_or_induced_metric=True,
            old_static_R24_source_and_results_unchanged_and_not_relabelled=True,
            no_new_native_or_BVP_acceptance_gate=True, members=copy.deepcopy(members))
        binding_receipt = write(args.out/"input-binding.json", binding, args.out)
        image = modules[DIAMETER].ImageBounds(modules[KERNEL].sqrt_upper, args.sqrt_bits,
                                             "original_marked_image")
        cover = CurvatureCover(G, roots, budget, curvature_ledger, image)
        pairs = PairCover(args, G, roots, budget, pair_ledger, modules, local)
        stage = "complete_closed_curvature_and_path_envelopes"
        curvature = cover.run()
        stage = "complete_AA_CC_AC_pair_cover"
        pair_report = pairs.run()
        stage = "complete_attempt_finished"
    except Stop as exc:
        stop_reason = str(exc)
    except BaseException as exc:
        error = dict(type=type(exc).__name__, message=str(exc), stage=stage,
            geometric_failure_or_native_rejection_inferred=False)
    finally:
        # These reports preserve the current node before retirement, all DFS
        # siblings and every untouched root/pair suffix after any caught stop.
        if cover is not None:
            try:
                curvature = cover.report()
                diameter = curvature["diameter"]
            except BaseException as exc:
                if error is None:
                    error = dict(type=type(exc).__name__, message=str(exc), stage="curvature_report")
        if pairs is not None:
            try:
                pair_report = pairs.report()
            except BaseException as exc:
                if error is None:
                    error = dict(type=type(exc).__name__, message=str(exc), stage="pair_report")
        for name, ledger in (("complete_spatial_enclosures", spatial),
                             ("complete_curvature_cover", curvature_ledger),
                             ("complete_pair_space_phase_cover", pair_ledger)):
            if ledger is not None:
                try:
                    ledgers[name] = ledger.close()
                except BaseException as exc:
                    ledgers[name] = dict(file=str(ledger.path.relative_to(args.out)),
                        closure_error=dict(type=type(exc).__name__, message=str(exc)),
                        complete_bytes_not_claimed=True)
                    if error is None:
                        error = dict(type=type(exc).__name__, message=str(exc), stage="ledger_close")
        if current is not None:
            try:
                members["actual_used_complete_field_identity"] = write(large/"actual-used-complete-field-identity.json",
                    current.expression_identity(), args.out)
            except BaseException as exc:
                if error is None:
                    error = dict(type=type(exc).__name__, message=str(exc), stage="final_field_identity")
        if saved_runtime_context is not None and old_precision is not None:
            saved_runtime_context.prec = old_precision
        for number, handler in previous_handlers.items():
            signal.signal(number, handler)
    K, tau = rational(args.curvature_upper), rational(args.target_reach)
    curvature_paid = curvature is not None and curvature["full_closed_K_proved"] and curvature["full_closed_immersion_proved"]
    pair_paid = pair_report is not None and pair_report["complete_pair_responsibility_paid"]
    reached = error is None and stop_reason is None and curvature_paid and pair_paid and K*tau <= 1
    D = None if diameter is None else diameter["phase_zero_complete_image_diameter_upper"]
    ratio_paid = reached and D is not None and tau >= Q(3, 100)*Q(D)
    counts = None
    if roots is not None:
        counts = dict(active_cells=roots.active_count, cap_roots=2,
            AA=roots.AA, CC=roots.CC, AC=roots.AC, all_root_pairs=roots.pair_count,
            full_universe=members.get("complete_root_universe"))
    result = dict(schema=SCHEMA, source=receipt(__file__),
        run_id=os.environ.get("GITHUB_RUN_ID"), source_commit=os.environ.get("GITHUB_SHA"),
        stage=stage, error=error, resource_partial=stop_reason is not None,
        resource_reason=stop_reason, external_signal=budget.requested_signal,
        input_binding=binding_receipt, members=members, ledgers=ledgers, universe_counts=counts,
        unstarted_scope=dict(
            input_binding_incomplete=binding_receipt is None,
            all_closed_field_and_pair_responsibility_unbound=roots is None,
            curvature_root_suffix=[0, roots.count] if roots is not None and cover is None else None,
            complete_pair_rank_suffix=[0, roots.pair_count] if roots is not None and pairs is None else None),
        parameters={key:getattr(args, key) for key in (
            "curvature_upper", "target_reach", "active_depth", "curvature_max_depth", "pair_max_depth",
            "interval_bits", "sqrt_bits", "max_cells", "max_pair_nodes", "max_pairs", "cache_entries",
            "max_constant_levels", "budget_seconds", "free_bytes_reserve")},
        curvature=curvature, pairs=pair_report, diameter=diameter,
        accurate_family_embedding_and_reach_certified=bool(reached),
        accurate_family_reach_lower=str(tau) if reached else None,
        K_times_tau=str(K*tau), curvature_radius_gate=K*tau <= 1,
        original_K_and_tau_not_reselected=True, README_reach_fraction_paid=bool(ratio_paid),
        README_D_definition="diameter of the entire marked closed F_0 image",
        original_static_base_R24_route_unchanged_and_not_assumed_paid=True,
        original_native_or_BVP_acceptance_changed=False,
        remaining_original_responsibilities=[
            "Any unpaid closed curvature cell and every pending full root-pair/space-phase address",
            "The same original accurate target full-domain relative metric requirement",
            "Held-set interior and diameter, complete-image Hausdorff hold and Euclidean noncongruence including reflections",
            "Original numerical-shadow, RK-trajectory and new-exact-field comparison responsibilities",
            "All original topic final standards and subsequent same-g refinement"],
        output_policy="Owned temporary runner ledgers only; no cleanup, artifacts, raw split or encoded transport",
        full_ledgers_are_not_claimed_as_locally_recomputed_or_returned_raw=True,
        current_source_object_is_not_the_old_rounded_renderer=True,
        elapsed_seconds=time.monotonic()-budget.start, task_completed=False)
    result_receipt = write(args.out/"result.json", result, args.out)
    summary = necessary_summary(result, result_receipt)
    raw = canonical(summary)
    if len(raw) > LIMIT:
        print(json.dumps(dict(schema=SCHEMA+"-summary-over-budget", attempted_bytes=len(raw),
            attempted_sha256=sha(raw), result=result_receipt,
            complete_necessary_readback=False, outputs_not_deleted=True), separators=(",", ":")), flush=True)
        return 70
    summary_receipt = write(args.out/"necessary-summary.json", summary, args.out)
    print("BEGIN_R422_CURRENT_C_COMPLETE_REACH_SUMMARY", flush=True)
    print(raw.decode(), end="", flush=True)
    print("END_R422_CURRENT_C_COMPLETE_REACH_SUMMARY", flush=True)
    print(json.dumps(dict(event="R422-necessary-summary-identity", **summary_receipt),
                     separators=(",", ":")), flush=True)
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as stream:
            stream.write("closed_reach_summary="+str(args.out/"necessary-summary.json")+"\n")
            stream.write("closed_reach_summary_bytes="+str(summary_receipt["bytes"])+"\n")
            stream.write("closed_reach_summary_sha256="+summary_receipt["sha256"]+"\n")
    if budget.requested_signal is not None:
        return 128+budget.requested_signal
    return 0 if error is None else 1


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--computations", type=Path, default=HERE)
    parser.add_argument("--directory", type=Path, required=True)
    parser.add_argument("--result-sha256", required=True)
    parser.add_argument("--checkpoint-directory", type=Path)
    parser.add_argument("--proof-directory", type=Path)
    parser.add_argument("--cuff-atlas", type=Path, required=True)
    parser.add_argument("--cuff-atlas-sha256", required=True)
    parser.add_argument("--curvature-upper", required=True)
    parser.add_argument("--target-reach", required=True)
    parser.add_argument("--active-depth", type=int, required=True)
    parser.add_argument("--curvature-max-depth", type=int, required=True)
    parser.add_argument("--pair-max-depth", type=int, required=True)
    parser.add_argument("--interval-bits", type=int, required=True)
    parser.add_argument("--sqrt-bits", type=int, required=True)
    parser.add_argument("--max-cells", type=int, required=True)
    parser.add_argument("--max-pair-nodes", type=int, required=True)
    parser.add_argument("--max-pairs", type=int, required=True)
    parser.add_argument("--cache-entries", type=int, default=32)
    parser.add_argument("--max-constant-levels", type=int, default=32)
    parser.add_argument("--budget-seconds", type=float, required=True)
    parser.add_argument("--free-bytes-reserve", type=int, default=2147483648)
    parser.add_argument("--out", type=Path, required=True)
    return produce(parser.parse_args(argv))


if __name__ == "__main__":
    raise SystemExit(main())
