#!/usr/bin/env python3
"""Complete same-field mixed responsibility with the independent R282 owner.

Every original rank retains both closed RP1 phase roots. Refinement splits
real spatial parameter intervals and phase intervals, never a displayed
worst list. Local proof applies only to its certified leaf product; the
original R281 alternatives remain OR branches for all other leaves.
Actual accepted inputs are required by the unchanged shared-field loader.
Temporary recomputable payloads belong only in the runner, not Git/Release.
"""
from __future__ import annotations

import argparse
from collections import OrderedDict
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
from types import SimpleNamespace
import time
import traceback

HERE = Path(__file__).resolve().parent
REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "same-shared-field-complete-mixed-local-and-phase-responsibility-v1"
OWNER_NAME = "geometry_20261115_local_cuff_cross_gram_owner.py"
OWNER_SHA = "0b52a408e08a12c1a16594658510b589ce20d9b2a75430ed5676869e12290456"
SOURCE_PINS = {
    "geometry_20261115_shared_active_interval_balls.py":
        "675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b",
    "geometry_20261115_complete_mixed_phase_component.py":
        "dbdedb450ca2280f37802258377e5fd8728b9f20ce2545f22ec141b6965bc3ed",
    "geometry_20261115_fixed_cap_rational_balls.py":
        "a3ada50b5389a075f1da2d2237269a1a1ccc83c29aa35bc889d721eac0e2552e",
}


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("Run the certificate arithmetic only in the named public Actions repository")


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       allow_nan=False)+"\n").encode()


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def file_receipt(path):
    size, h = 0, hashlib.sha256()
    with Path(path).open("rb") as stream:
        for data in iter(lambda: stream.read(1048576), b""):
            size += len(data)
            h.update(data)
    return dict(file=str(Path(path).name), bytes=size, sha256=h.hexdigest())


def write_json(path, value, *, compressed=False):
    raw = canonical(value)
    with Path(path).open("xb") as stream:
        if compressed:
            with gzip.GzipFile(filename="", fileobj=stream, mode="wb", mtime=0) as output:
                output.write(raw)
        else:
            stream.write(raw)
    receipt = file_receipt(path)
    if compressed:
        receipt.update(decoded_bytes=len(raw), decoded_sha256=digest(raw))
    return receipt


def load_module(path, expected, name):
    raw = Path(path).read_bytes()
    if digest(raw) != expected:
        raise ValueError("A defining source differs: "+Path(path).name)
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def scope(node):
    return dict(phase_chart=node["chart"], closed_phase_interval=list(map(str, node["phase"])),
                closed_radial_interval=list(map(str, node["radial"])),
                closed_normalized_physical_angle_interval=list(map(str, node["angular"])),
                cap_parameter_box_xy=[list(map(str, value)) for value in node["box"]],
                cap_domain="This exact closed box intersected with the original closed cuff disk",
                path=node["path"], depth=node["depth"], spatial_depth=node["spatial_depth"])


def split_node(node):
    """Round-robin refinement of all four spatial axes and phase.

    Both children are closed; their shared endpoint belongs to both. This
    scheduling choice changes resource use, not any mathematical gate.
    """
    axis = node["depth"] % 5
    if axis == 0:
        interval = node["radial"]
    elif axis == 1:
        interval = node["angular"]
    elif axis < 4:
        interval = node["box"][axis-2]
    else:
        interval = node["phase"]
    midpoint = (interval[0]+interval[1])/2
    children = []
    for k, child_interval in enumerate(((interval[0], midpoint), (midpoint, interval[1]))):
        child = dict(node)
        child.update(path=node["path"]+str(k), depth=node["depth"]+1,
                     spatial_depth=node["spatial_depth"]+(axis != 4))
        if axis == 0:
            child["radial"] = child_interval
        elif axis == 1:
            child["angular"] = child_interval
        elif axis < 4:
            box = list(node["box"])
            box[axis-2] = child_interval
            child["box"] = tuple(box)
        else:
            child["phase"] = child_interval
        children.append(child)
    return axis, midpoint, children


class EventStream:
    def __init__(self, path):
        self.raw = Path(path).open("xb")
        self.gzip = gzip.GzipFile(filename="", fileobj=self.raw, mode="wb", mtime=0)
        self.count = 0

    def write(self, value):
        self.gzip.write(canonical(dict(event_ordinal=self.count, **value)))
        self.count += 1

    def close(self):
        self.gzip.close()
        self.raw.close()


class CompleteCombiner:
    def __init__(self, args, M, C, B, phase, previous, kernel, owner_module,
                 field, expression, markers, height, tau, local, stream, started):
        self.args, self.M, self.C, self.B = args, M, C, B
        self.phase, self.previous, self.kernel = phase, previous, kernel
        self.O, self.field, self.expression = owner_module, field, expression
        self.markers, self.height, self.tau = markers, height, tau
        self.local, self.stream, self.started = local, stream, started
        self.nodes = self.fresh_active_evaluations = self.fresh_cap_evaluations = 0
        self.spatial_cache = OrderedDict()
        self.expected_nodes = {row["index"]: row for row in expression["native_complete_FFT_nodes"]}
        self.emitted_spatial = set()

    def check_nodes(self):
        for index, actual in self.field.node_records.items():
            if index not in self.expected_nodes:
                raise ValueError("An actual FFT node lacks the existing expression identity; do not relabel a new field")
            if actual != self.expected_nodes[index]:
                raise ValueError("A complete native FFT node changed from the bound finite field")

    def resource_reason(self):
        if self.nodes >= self.args.max_nodes:
            return "complete_space_phase_node_budget"
        if time.monotonic()-self.started >= self.args.budget_seconds:
            return "complete_space_phase_time_budget"
        return None

    def spatial_data(self, rank, active, cap, node):
        # Phase-only refinement reuses these exact same valid spatial balls.
        # Spatial refinement raises precision. The actual values and source
        # identity are retained in the event stream, not inferred from a flag.
        precision = self.args.precision_bits+node["spatial_depth"]
        bits = self.args.sqrt_bits+node["spatial_depth"]
        key_data = dict(rank=rank, active_cell_id=active["cell_id"], cap_cell_id=cap["cell_id"],
                        radial=list(map(str, node["radial"])), angular=list(map(str, node["angular"])),
                        box=[list(map(str, v)) for v in node["box"]],
                        precision_bits=precision, sqrt_bits=bits)
        key = digest(canonical(key_data))
        if key in self.spatial_cache:
            self.spatial_cache.move_to_end(key)
            return self.spatial_cache[key]
        self.M.ctx.prec = precision
        root_radial = tuple(map(F, active["closed_radial_interval"]))
        root_angle = tuple(map(F, active["closed_normalized_physical_angle_interval"]))
        root_box = tuple(tuple(map(F, v)) for v in cap["parameter_box_xy"])
        if node["radial"] == root_radial and node["angular"] == root_angle:
            moving = active
            moving_origin = "original_whole_active_cell_ball"
        else:
            self.fresh_active_evaluations += 1
            try:
                moving = self.M.certify_cell(
                    self.field, self.field.pieces[active["piece_index"]],
                    node["radial"], node["angular"], active["sheet"] == "lower",
                    self.kernel.sqrt_upper, bits, None)
            except (ArithmeticError, ValueError) as error:
                moving = dict(normal_ball_certified=False,
                              ball_evaluation_exception=dict(type=type(error).__name__, message=str(error)))
            self.check_nodes()
            moving_origin = "same_exact_field_full_subcell_interval_evaluation"
        if node["box"] == root_box:
            fixed = cap
            fixed_origin = "original_whole_fixed_cap_cell_ball"
        else:
            self.fresh_cap_evaluations += 1
            fixed = self.C.cap_cell("R282/"+key, node["box"], cap["cap"] == "upper",
                                    self.height, self.markers, self.kernel.sqrt_upper, bits)
            fixed_origin = "same_original_graph_cap_subcell_bound"
        data = dict(spatial_id=key, spatial_scope=key_data, moving=moving, fixed=fixed,
                    moving_origin=moving_origin, fixed_origin=fixed_origin,
                    R280=None, R281_catalog=None)
        if moving.get("normal_ball_certified") is True:
            row = dict(name="rank-"+str(rank)+"/spatial-"+key, tau=str(self.tau))
            for prefix, value in (("moving", moving), ("fixed", fixed)):
                for suffix in ("position", "position_radius", "normal_centre", "normal_radius"):
                    row[prefix+"_"+suffix] = value[prefix+"_"+suffix]
            base = self.previous.evaluate_joint(row, bits, self.kernel)
            data["R281_input"] = row
            data["R280"] = base
            if not base["all_phase_distance_or_no_double_normal_pass"]:
                data["R281_catalog"] = self.phase.catalog_for(row, base, self.kernel)
        if key not in self.emitted_spatial:
            self.stream.write(dict(kind="complete_spatial_ball_and_original_phase_catalog",
                                   rank=rank, **data))
            self.emitted_spatial.add(key)
        self.spatial_cache[key] = data
        while len(self.spatial_cache) > self.args.cache_entries:
            self.spatial_cache.popitem(last=False)
        return data

    def phase_test(self, data, node):
        if data["R280"] is None:
            return dict(certified=False, reason="unit_normal_ball_not_available_for_original_R281",
                        spatial_id=data["spatial_id"])
        base = data["R280"]
        if base["all_phase_distance_or_no_double_normal_pass"]:
            return dict(certified=True, owner="original_R280_R62_full_circle_OR",
                        reason="An_original_full_circle_gate_already_covers_this_leaf",
                        spatial_id=data["spatial_id"],
                        original_non_strict_full_circle_distance_alternative_retained=True)
        tests = {}
        for gate in self.phase.GATE_ORDER:
            entry = data["R281_catalog"][node["chart"]][gate]
            polynomial = list(map(F, entry["ascending_coefficients_padded_to_degree_four"]))
            sequence = [list(map(F, v)) for v in entry["sturm"]["sequence"]]
            tests[gate] = self.phase.strict_interval(
                polynomial, sequence, node["phase"][0], node["phase"][1], self.kernel)
        passing = [gate for gate in self.phase.GATE_ORDER if tests[gate]["strict_positive"]]
        return dict(certified=bool(passing), owner="original_R281_closed_interval_OR",
                    spatial_id=data["spatial_id"], exact_gate_tests=tests, passing_gates=passing,
                    selected_gate=passing[0] if passing else None)

    def pair(self, rank, active, cap):
        radial = tuple(map(F, active["closed_radial_interval"]))
        angular = tuple(map(F, active["closed_normalized_physical_angle_interval"]))
        box = tuple(tuple(map(F, v)) for v in cap["parameter_box_xy"])
        stack = [dict(chart=chart, phase=(F(-1), F(1)), radial=radial, angular=angular,
                      box=box, path="", depth=0, spatial_depth=0)
                 for chart in ("u", "t")]
        self.stream.write(dict(kind="pair_begin", rank=rank,
                               active_cell_id=active["cell_id"], fixed_cell_id=cap["cell_id"],
                               complete_roots=[scope(v) for v in reversed(stack)]))
        counts = dict(local=0, original_phase=0, empty=0, unresolved=0, splits=0)
        stopped = None
        while stack:
            reason = self.resource_reason()
            if reason:
                stopped = reason
                # The unvisited stack is an exact terminal cover of every
                # remaining domain, not a sampled collection of bad examples.
                for node in reversed(stack):
                    counts["unresolved"] += 1
                    self.stream.write(dict(kind="terminal_leaf", rank=rank, scope=scope(node),
                                           certified=False, owner=None, reason=reason,
                                           untested_due_to_resource=True))
                stack.clear()
                break
            node = stack.pop()
            self.nodes += 1
            self.M.ctx.prec = self.args.precision_bits+node["depth"]
            if self.O.minimum_squared_radius(node["box"]) > self.field.cuff**2:
                counts["empty"] += 1
                self.stream.write(dict(kind="terminal_leaf", rank=rank, scope=scope(node),
                                       certified=True, owner="exact_empty_cap_disk_intersection",
                                       minimum_squared_radius=str(self.O.minimum_squared_radius(node["box"])),
                                       original_cuff_squared=str(self.field.cuff**2)))
                continue
            try:
                local = self.local.test(active, node["radial"], node["angular"], cap,
                                        node["box"], node["chart"], node["phase"], node["depth"])
            except (ArithmeticError, ValueError) as error:
                local = dict(certified=False, reason="local_interval_membership_unresolved",
                             exception=dict(type=type(error).__name__, message=str(error)))
            if local["certified"]:
                counts["local"] += 1
                self.stream.write(dict(kind="terminal_leaf", rank=rank, scope=scope(node),
                                       certified=True, owner="R282_same_material_local_cross_Gram",
                                       local=local))
                continue
            spatial = self.spatial_data(rank, active, cap, node)
            phase = self.phase_test(spatial, node)
            if phase["certified"]:
                counts["original_phase"] += 1
                self.stream.write(dict(kind="terminal_leaf", rank=rank, scope=scope(node),
                                       certified=True, owner=phase["owner"], local_attempt=local,
                                       original_phase=phase))
                continue
            if node["depth"] >= self.args.max_depth:
                counts["unresolved"] += 1
                self.stream.write(dict(kind="terminal_leaf", rank=rank, scope=scope(node),
                                       certified=False, owner=None, local_attempt=local,
                                       original_phase=phase, reason="space_phase_depth_budget",
                                       unresolved_means_geometric_failure=False))
                continue
            axis, midpoint, children = split_node(node)
            counts["splits"] += 1
            self.stream.write(dict(kind="split", rank=rank, scope=scope(node),
                                   split_axis=("r", "q", "cap_x", "cap_y", "phase")[axis],
                                   midpoint=str(midpoint), complete_closed_children=[scope(v) for v in children],
                                   local_attempt=local, original_phase=phase,
                                   shared_endpoint_deliberately_covered_twice=True))
            stack.extend(reversed(children))
        result = dict(rank=rank, complete_two_chart_domain_accounted_for=True,
                      complete_component_paid=counts["unresolved"] == 0,
                      counts=counts, resource_stop=stopped)
        self.stream.write(dict(kind="pair_end", **result))
        return result


def verify_reconstructed_field(field, expression, binding):
    if field.binding != binding["complete_field_binding"]:
        raise ValueError("The reconstructed actual field binding changed")
    if field.A.shared_background_geometry != binding["shared_background_geometry"]:
        raise ValueError("The original shared geometry changed")
    actual = field.expression_identity()
    excluded = {"native_complete_FFT_nodes", "all_native_nodes_evaluated_and_bound"}
    if {k: v for k, v in actual.items() if k not in excluded} != {
            k: v for k, v in expression.items() if k not in excluded}:
        raise ValueError("The exact finite expression differs beyond the lazily loaded FFT node list")


def run(args):
    require_actions()
    if args.out.exists():
        raise FileExistsError("Use a new output directory and preserve earlier results")
    if not (64 <= args.precision_bits <= 8192 and 16 <= args.sqrt_bits <= 4096
            and args.max_depth >= 0 and args.max_constant_levels > 0
            and args.max_nodes >= 2 and args.max_pairs > 0
            and args.cache_entries > 0 and args.budget_seconds > 0):
        raise ValueError("Invalid explicit resource parameters")
    code = args.code_directory.resolve()
    closure = {**SOURCE_PINS, OWNER_NAME: OWNER_SHA}
    sources = {}
    for name, expected in closure.items():
        raw = (code/name).read_bytes()
        if digest(raw) != expected:
            raise ValueError("A bound defining source changed: "+name)
        sources[name] = dict(bytes=len(raw), sha256=expected)
    M = load_module(code/"geometry_20261115_shared_active_interval_balls.py",
                    SOURCE_PINS["geometry_20261115_shared_active_interval_balls.py"], "_r282_active")
    B = load_module(code/"geometry_20261115_complete_mixed_phase_component.py",
                    SOURCE_PINS["geometry_20261115_complete_mixed_phase_component.py"], "_r282_bound_mixed")
    C = load_module(code/"geometry_20261115_fixed_cap_rational_balls.py",
                    SOURCE_PINS["geometry_20261115_fixed_cap_rational_balls.py"], "_r282_caps")
    O = load_module(code/OWNER_NAME, OWNER_SHA, "_r282_local_owner")
    phase, previous, kernel = B.load_phase(code)
    active, fixed, expression, cap_cells, cell_path, tau, binding = B.bind_inputs(args)
    geometry, background, _, defining_sources = M.initialise_runtime(code)
    old_precision = M.ctx.prec
    started = time.monotonic()
    args.out.mkdir(parents=True)
    large = args.out/"large-arrays"
    large.mkdir()
    stream = None
    try:
        M.ctx.prec = active["parameters"]["effective_precision_bits"]
        field = M.ExactFiniteField(geometry.load_shared_bundle(args), background)
        verify_reconstructed_field(field, expression, binding)
        cap_args = SimpleNamespace(plan=field.paths["plan"],
                                   plan_sha256=fixed["input_binding"]["plan"]["sha256"],
                                   assembly=field.paths["assembly"],
                                   assembly_sha256=fixed["input_binding"]["assembly"]["sha256"])
        cuff, height, markers, cap_binding = C.bind_geometry(cap_args)
        if cap_binding != fixed["input_binding"] or cuff != field.cuff or height != field.B.nodal[0][0]:
            raise ValueError("The local owner uses a different actual cap or shared-B cuff")
        local = O.CuffOwner(field, markers, M, kernel, sqrt_bits=args.sqrt_bits,
                            max_constant_levels=args.max_constant_levels)
        expected_nodes = {row["index"]: row for row in expression["native_complete_FFT_nodes"]}
        for index, actual in field.node_records.items():
            if index not in expected_nodes or actual != expected_nodes[index]:
                raise ValueError("The actual collar FFT coefficients do not have the bound source-field identity")
        source_identity = dict(source_sha256=digest(Path(__file__).read_bytes()),
                               sources=sources, exact_field_defining_sources=defining_sources,
                               inherited_phase_sources=B.SOURCE_PINS)
        bound = dict(schema=SCHEMA+"-binding", **source_identity,
                     inherited_complete_mixed_binding=binding,
                     actual_same_full_field_reconstructed=True,
                     same_original_cap_binding=cap_binding,
                     no_new_native_solve_or_target_g_or_tau=True,
                     local_owner_proof="R282-local-cross-Gram-cuff-charts-and-complete-phase-responsibility.md",
                     complete_closed_leaf_coverage_required_not_worst_examples=True)
        input_receipt = write_json(args.out/"input-binding.json", bound)
        coefficients = write_json(large/"complete-collar-coefficients.json.gz",
                                  local.coefficient_payload, compressed=True)
        coefficients["file"] = "large-arrays/"+coefficients["file"]
        constant_receipt = write_json(large/"local-cuff-constants.json.gz", local.report(), compressed=True)
        constant_receipt["file"] = "large-arrays/"+constant_receipt["file"]
        stream = EventStream(large/"complete-space-phase-responsibility.jsonl.gz")
        combine = CompleteCombiner(args, M, C, B, phase, previous, kernel, O, field,
                                   expression, markers, height, tau, local, stream, started)
        combine.check_nodes()
        planned = active["planned_closed_cells"]*len(cap_cells)
        processed = paid = 0
        totals = dict(local=0, original_phase=0, empty=0, unresolved=0, splits=0)
        stop_reason = None
        for a in B.active_rows(cell_path, active, expression):
            for cap_index, cap in enumerate(cap_cells):
                if processed >= args.max_pairs:
                    stop_reason = "original_pair_resource_budget"
                    break
                if combine.resource_reason():
                    stop_reason = combine.resource_reason()
                    break
                rank = a["ordinal"]*len(cap_cells)+cap_index
                if rank != processed:
                    raise AssertionError("The complete original rank sequence has a gap")
                result = combine.pair(rank, a, cap)
                processed += 1
                paid += int(result["complete_component_paid"])
                for key in totals:
                    totals[key] += result["counts"][key]
                if result["resource_stop"]:
                    stop_reason = result["resource_stop"]
                    break
            if stop_reason:
                break
        combine.check_nodes()
        if processed != planned and stop_reason is None:
            stop_reason = "original_active_stream_is_a_preserved_partial_partition"
        stream.close()
        stream = None
        ledger = file_receipt(large/"complete-space-phase-responsibility.jsonl.gz")
        ledger["file"] = "large-arrays/"+ledger["file"]
        used_nodes = write_json(large/"actual-used-FFT-node-identities.json",
                               dict(actual_nodes=[field.node_records[k] for k in sorted(field.node_records)],
                                    every_used_node_matches_the_original_expression=True))
        used_nodes["file"] = "large-arrays/"+used_nodes["file"]
        enumeration_complete = processed == planned
        result = dict(schema=SCHEMA, completed=True, **source_identity,
                      input_binding=input_receipt, complete_coefficients=coefficients,
                      local_constants=constant_receipt, complete_responsibility_ledger=ledger,
                      actual_used_FFT_nodes=used_nodes,
                      parameters={key: getattr(args, key) for key in
                                  ("precision_bits", "sqrt_bits", "max_depth", "max_constant_levels",
                                   "max_nodes", "max_pairs", "cache_entries", "budget_seconds")},
                      planned_original_cartesian_pairs=planned, processed_original_pairs=processed,
                      fully_paid_original_pairs=paid, complete_rank_enumeration=enumeration_complete,
                      complete_mixed_component_paid=enumeration_complete and paid == planned,
                      leaf_totals=totals, processed_space_phase_nodes=combine.nodes,
                      newly_evaluated_active_subcells=combine.fresh_active_evaluations,
                      newly_evaluated_fixed_cap_subcells=combine.fresh_cap_evaluations,
                      unvisited_original_pair_suffix=None if enumeration_complete else [processed, planned],
                      resource_stop=stop_reason,
                      processed_pair_phase_roots_and_closed_spatial_endpoints_accounted_for=True,
                      local_constant_does_not_pay_an_entire_rank=True,
                      old_static_base_R24_route_and_all_old_gates_unchanged=True,
                      original_target_reach_exact=str(tau),
                      global_curvature_or_active_active_or_fixed_fixed_responsibility_paid=False,
                      full_surface_certified=False, actual_reach_certified=False,
                      same_g_nonlinear_acceptance_created=False, task_completed=False,
                      elapsed_seconds=time.monotonic()-started)
        final_receipt = write_json(args.out/"result.json", result)
        print(json.dumps(dict(event="complete_local_and_phase_component_finished",
                              schema=SCHEMA, output_sha256=final_receipt["sha256"],
                              output_bytes=final_receipt["bytes"],
                              planned_pairs=planned, processed_pairs=processed, paid_pairs=paid,
                              complete_mixed_component_paid=result["complete_mixed_component_paid"],
                              leaf_totals=totals, resource_stop=stop_reason,
                              full_surface_certified=False, actual_reach_certified=False),
                         sort_keys=True, separators=(",", ":")), flush=True)
    except BaseException as error:
        if stream is not None:
            stream.close()
            stream = None
        write_json(args.out/"failure.json", dict(schema=SCHEMA+"-failure",
                   exception=dict(type=type(error).__name__, message=str(error)),
                   traceback=traceback.format_exc(), partial_outputs_preserved=True,
                   complete_component_claimed=False, geometric_failure_inferred=False))
        raise
    finally:
        if stream is not None:
            stream.close()
        M.ctx.prec = old_precision


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("directory", "source-directory", "descriptor", "checkpoint", "port", "config",
                 "tail-response", "complete", "source-topic", "out"):
        parser.add_argument("--"+name, type=Path, required=True)
    for name in ("active-result", "fixed-caps", "original-cover"):
        parser.add_argument("--"+name, type=Path, required=True)
        parser.add_argument("--"+name+"-sha256", required=True)
    parser.add_argument("--basename", default="surface")
    parser.add_argument("--source-basename", default="surface")
    parser.add_argument("--code-directory", type=Path, default=HERE)
    parser.add_argument("--precision-bits", type=int, default=192)
    parser.add_argument("--sqrt-bits", type=int, default=128)
    parser.add_argument("--max-depth", type=int, default=25)
    parser.add_argument("--max-constant-levels", type=int, default=32)
    parser.add_argument("--max-nodes", type=int, default=1000000)
    parser.add_argument("--max-pairs", type=int, default=1000000)
    parser.add_argument("--cache-entries", type=int, default=32)
    parser.add_argument("--budget-seconds", type=int, default=3600)
    run(parser.parse_args())


if __name__ == "__main__":
    main()
