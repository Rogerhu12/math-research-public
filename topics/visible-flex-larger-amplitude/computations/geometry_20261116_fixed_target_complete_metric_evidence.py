#!/usr/bin/env python3
"""R459 actual fixed-target, whole-closed-domain metric refinement evidence.

measure loads a genuine R416/R441/R451 field, the complete same-C target,
the actual first R437/R452 material record, and both actual cap graphs. It
encloses the two-dimensional relative operator norm, not an eta pass count.
The complete base-circle sweep transfers to all phases by the exact common
material diffeomorphism; an explicitly requested t grid is also really queried.
compare consumes completed or partial actual measurements. Interval overlap
is undecided, never a new BVP, native, refinement, or geometry rejection.

No fixture, mathematical source mutation, subprocess, raw deletion, or new
clock is introduced. Every arithmetic action executes only in public Actions.
Author: geometry agent (AI), 2026-11-16.
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
import struct
import sys
import time
from types import SimpleNamespace

REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "R459-same-accurate-closed-target-complete-relative-metric-evidence-v1"
INPUT_SCHEMA = SCHEMA + "-measure-input-v1"
SERIES_SCHEMA = SCHEMA + "-actual-series-v1"
SERIES_INPUT = SCHEMA + "-compare-input-v1"
SUMMARY_LIMIT = 90000
MATERIAL_NAME = "geometry_20261116_current_C_actual202_M_common_material_phase.py"
MATERIAL_SHA = "059d0df3ab5957b8ba5adf69e305ee4663ba06378242fe4c5f2116bab437af41"
MATERIAL_SCHEMA = "R457-current-C-actual202-capable-complete-M-common-material-phase-v1"
FAMILIES = {
    "original112": dict(
        file="geometry_20261115_current_C_ten_live_query_complete_metric.py",
        sha256="77be1d98c7401c4d0962adae7b824fd22c66b3a0127885b080859edc0f4a7892",
        schema="R426-current-C-accurate-ten-complete-closed-relative-metric-live-queries-v1"),
    "resolution112": dict(
        file="geometry_20261116_current_C_resolution_live_query_complete_metric.py",
        sha256="fd263af28a7d55a7246a49283d367e420786f48f16556dd5a7d61406b1c8459b",
        schema="R441-current-C-resolution450-complete-relative-metric-live-queries-v1"),
    "completeM": dict(
        file="geometry_20261116_current_C_M_live_query_complete_metric.py",
        sha256="fc35c6408aacbf2131a89fbac37ca4ae98c1665d9fbdc4ba78a50a43ca7f3a47",
        schema="R451-current-C-complete-M-relative-metric-live-queries-v1"),
}
DEADLINES = {
    "request193-owned-job-science-deadline-v1",
    "request203-owned-job-science-deadline-v1",
    "request205-owned-job-science-deadline-v1",
}
WORK_KEYS = {
    "budget_seconds", "free_bytes_reserve", "interval_bits", "sqrt_bits",
    "initial_angular_depth", "max_depth", "max_cells", "measurement_width_goal",
    "metric_reference_eta", "max_inverse_steps", "max_phase_query_cells",
}
QUERY_KEYS = {
    "precision_bits", "integral_absolute_bits", "integral_relative_bits",
    "analytic_guard_bits", "integral_evaluation_limit", "value_width_bits",
    "integral_max_depth", "inverse_max_depth", "max_panels", "max_nodes", "budget_seconds",
}
RESOLUTION_KEYS = (
    "field_modes", "field_angular_quadrature", "native_quadrature",
    "native_steps_per_stage", "material_angles", "physical_angles", "native_stage_count",
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
            "All evaluation and comparison arithmetic belongs to this public Actions repository")


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
        ensure_ascii=False, allow_nan=False) + "\n").encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def value_identity(value):
    raw = canonical(value)
    return dict(bytes=len(raw), sha256=sha(raw))


def receipt(path):
    path = Path(path).resolve(strict=True)
    h, size = hashlib.sha256(), 0
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1048576), b""):
            h.update(block); size += len(block)
    return dict(file=str(path), bytes=size, sha256=h.hexdigest())


def same_payload(a, b):
    return (isinstance(a, dict) and isinstance(b, dict)
            and a.get("bytes") == b.get("bytes") and a.get("sha256") == b.get("sha256"))


def unique(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "An input JSON key was duplicated: " + key)
        result[key] = value
    return result


def read_bound(path, expected):
    actual = receipt(path)
    require(actual["sha256"] == expected if isinstance(expected, str)
            else same_payload(actual, expected), "The actual file bytes/SHA differ: " + str(path))
    raw = Path(path).read_bytes()
    return json.loads(raw, object_pairs_hook=unique,
        parse_constant=lambda value: (_ for _ in ()).throw(ValueError("Nonfinite JSON token: " + value))), actual


def read_descriptor(row):
    require(isinstance(row, dict) and set(row) == {"file", "bytes", "sha256"},
            "Use an actual complete file/bytes/SHA descriptor")
    return read_bound(row["file"], row)


def write(path, value):
    path = Path(path)
    with path.open("xb") as stream:
        stream.write(canonical(value)); stream.flush(); os.fsync(stream.fileno())
    return receipt(path)


def rat(value):
    require(type(value) in (int, str, Q), "Use exact rational text, not silently rounded float bounds")
    return Q(value)


def finite_positive(value, label):
    require(type(value) in (int, float) and math.isfinite(value) and value > 0,
            "Use an explicit finite positive work resource: " + label)
    return float(value)


def word(value):
    value = float(value)
    require(math.isfinite(value), "A defining numerical word must be finite")
    return struct.pack("<d", value).hex()


def pair(value):
    require(isinstance(value, (list, tuple)) and len(value) == 2,
            "A closed interval requires both exact endpoints")
    a, b = map(rat, value)
    require(a <= b, "A closed interval is reversed")
    return a, b


def encode(bounds):
    return None if bounds is None else list(map(str, bounds))


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def subtract(a, b):
    return a[0]-b[1], a[1]-b[0]


def multiply(a, b):
    values = [x*y for x in a for y in b]
    return min(values), max(values)


def divide_positive(a, b):
    require(b[0] > 0, "A proved positive target denominator is required")
    return multiply(a, (1/b[1], 1/b[0]))


def square(a):
    return (Q(0) if a[0] <= 0 <= a[1] else min(x*x for x in a), max(x*x for x in a))


def absolute(a):
    return (Q(0) if a[0] <= 0 <= a[1] else min(map(abs, a)), max(map(abs, a)))


def sqrt_point_bounds(value, bits):
    """Exact integer square root: no positive interval is rounded to a ball."""
    require(value >= 0, "Square-root input must be nonnegative")
    denominator = 1 << bits
    floor = math.isqrt((value.numerator << (2*bits)) // value.denominator)
    lo = Q(floor, denominator)
    return lo, lo if lo*lo == value else Q(floor+1, denominator)


def relative_norm(E, B, C, g11, g22, bits):
    """Enclose |tr/2|+sqrt(((a-c)/2)^2+b^2) with rational endpoints.

    The quantity is exactly the symmetric generalized-Gram operator norm.
    Correlations are dropped only outward; no coefficient midpoint is chosen.
    """
    if g11[0] <= 0 or g22[0] <= 0:
        return dict(available=False, reason="accurate_target_positive_diagonal_unresolved",
                    target_diagonal=[encode(g11), encode(g22)])
    require(E[1] >= 0 and C[1] >= 0, "An outward Gram diagonal contradicts its exact squared norm")
    E, C = (max(Q(0), E[0]), E[1]), (max(Q(0), C[0]), C[1])
    a = subtract(divide_positive(E, g11), (Q(1), Q(1)))
    c = subtract(divide_positive(C, g22), (Q(1), Q(1)))
    half = (Q(1, 2), Q(1, 2))
    p, d = multiply(add(a, c), half), multiply(subtract(a, c), half)
    b2 = divide_positive(square(B), multiply(g11, g22))
    radicand = add(square(d), b2)
    root = sqrt_point_bounds(radicand[0], bits)[0], sqrt_point_bounds(radicand[1], bits)[1]
    answer = add(absolute(p), root)
    return dict(available=True, norm_interval=encode(answer),
        Gram=[encode(E), encode(B), encode(C)], target_diagonal=[encode(g11), encode(g22)],
        normalized_diagonal=[encode(a), encode(c)], normalized_off_diagonal_square=encode(b2),
        formula="abs((a+c)/2)+sqrt(((a-c)/2)^2+b^2)",
        exact_rational_endpoint_arithmetic=True, square_root_bits=bits,
        operator_norm_not_componentwise_error=True, no_target_or_Gram_midpoint_selected=True)


def load_source(directory, name, expected):
    path = (Path(directory)/name).resolve(strict=True)
    source = receipt(path)
    require(source["sha256"] == expected, "A complete defining source differs: " + name)
    for module in tuple(sys.modules.values()):
        other = getattr(module, "__file__", None)
        if other is not None and Path(other).resolve() == path:
            return module, source
    tag = "_r459_"+name[:-3]
    spec = importlib.util.spec_from_file_location(tag, path)
    require(spec is not None and spec.loader is not None, "The pinned module has no loader")
    module = importlib.util.module_from_spec(spec); sys.modules[tag] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        sys.modules.pop(tag, None)
        raise
    return module, source


class ResourceStop(RuntimeError):
    pass


class Budget:
    def __init__(self, namespace, deadline, work, started):
        self.namespace = Path(namespace).resolve(strict=True)
        self.deadline = deadline["namespace_created_unix_seconds"] + deadline["science_seconds_from_namespace"]
        self.started = started
        self.end = started + finite_positive(work["budget_seconds"], "budget_seconds")
        self.free = work["free_bytes_reserve"]
        self.signal_number = None
        self.original_handlers = {}

    def check(self):
        if self.signal_number is not None:
            raise ResourceStop("actual_external_signal_"+str(self.signal_number))
        if time.time() >= self.deadline:
            raise ResourceStop("original_same_job_absolute_science_deadline_reached")
        if time.monotonic() >= self.end:
            raise ResourceStop("declared_metric_measurement_work_budget_reached")
        if shutil.disk_usage(self.namespace).free < self.free:
            raise ResourceStop("owned_output_free_space_reserve_reached")

    def install(self):
        def stop(number, frame):
            self.signal_number = number
            # Preserve atomic stack/ledger bookkeeping. The next host check
            # stops; the external owned launcher still owns TERM/KILL limits.
        for number in (signal.SIGTERM, signal.SIGINT):
            self.original_handlers[number] = signal.getsignal(number)
            signal.signal(number, stop)

    def restore(self):
        for number, handler in self.original_handlers.items():
            signal.signal(number, handler)

    def remaining(self):
        return max(0.0, min(self.end-time.monotonic(), self.deadline-time.time()))


class Journal:
    def __init__(self, path):
        self.path = Path(path)
        self.stream = gzip.open(self.path, "xb")
        self.rows = 0
        self.digest = hashlib.sha256()
        self.decoded_bytes = 0
        self.closed = None

    def append(self, row):
        raw = canonical(row)
        self.stream.write(raw)
        self.digest.update(raw); self.decoded_bytes += len(raw); self.rows += 1

    def close(self):
        if self.closed is None:
            self.stream.close()
            self.closed = dict(**receipt(self.path), rows=self.rows,
                decoded_bytes=self.decoded_bytes, decoded_sha256=self.digest.hexdigest())
        return self.closed


def current_identity(value):
    require(value.get("repository") == REPOSITORY
            and value.get("run_id") == os.environ.get("GITHUB_RUN_ID")
            and value.get("source_commit") == os.environ.get("GITHUB_SHA"),
            "Consume actual files from this same immutable-source Actions job")


def inside(path, namespace, exists=True):
    path = Path(path).resolve(strict=exists)
    require(path != namespace and path.is_relative_to(namespace),
            "Actual field inputs and outputs must remain under their owned namespace")
    return path


def validate_input(data):
    required = {"schema", "label", "namespace", "computations", "proof_directory", "job_deadline",
                "first_material_transport", "first_plan", "first_assembly", "field", "work",
                "c_queries", "time_grid", "out"}
    require(set(data) == required and data["schema"] == INPUT_SCHEMA,
            "Use the exact independently declared R459 measurement input")
    require(isinstance(data["label"], str) and data["label"], "Keep an explicit measurement label")
    namespace = Path(data["namespace"]).resolve(strict=True)
    runner = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    require(namespace != runner and namespace.is_relative_to(runner),
            "The existing owned namespace must be under actual RUNNER_TEMP")
    out = inside(data["out"], namespace, exists=False)
    require(not out.exists(), "Keep every prior result; this output must be fresh")
    work = data["work"]
    require(isinstance(work, dict) and set(work) == WORK_KEYS, "Declare every measurement work resource")
    for key in WORK_KEYS-{"budget_seconds", "measurement_width_goal", "metric_reference_eta"}:
        require(type(work[key]) is int, "A work count must be an explicit integer: "+key)
    require(work["free_bytes_reserve"] > 0 and 64 <= work["interval_bits"] <= 8192
            and 32 <= work["sqrt_bits"] <= 8192 and 0 <= work["initial_angular_depth"] <= 20
            and 0 <= work["max_depth"] <= 30 and work["max_cells"] > 0
            and 0 <= work["max_inverse_steps"] <= 4096 and work["max_phase_query_cells"] > 0,
            "Use finite explicit measurement resources")
    finite_positive(work["budget_seconds"], "budget_seconds")
    require(rat(work["measurement_width_goal"]) >= 0
            and 0 < rat(work["metric_reference_eta"]) < 1,
            "The measurement work goal and declared metric reference have distinct roles")
    require(isinstance(data["c_queries"], dict) and set(data["c_queries"]) == QUERY_KEYS,
            "Keep every original live-C query work parameter")
    field = data["field"]
    require(isinstance(field, dict) and set(field) == {
        "family", "directory", "result_sha256", "checkpoint_directory", "cuff_atlas", "continuous_e_result"}
        and field["family"] in FAMILIES, "Use one complete registered accurate-field family")
    grid = data["time_grid"]
    require(isinstance(grid, dict) and set(grid) == {"subdivisions", "witnesses"}
            and type(grid["subdivisions"]) is int and grid["subdivisions"] > 0
            and isinstance(grid["witnesses"], list) and len(grid["witnesses"]) > 0,
            "Specify actual full [0,1] t-grid work and at least one common-coordinate witness")
    for row in grid["witnesses"]:
        require(isinstance(row, dict) and set(row) == {"kind", "coordinate", "q", "lower"}
                and row["kind"] in ("prefix", "radial") and type(row["lower"]) is bool
                and 0 <= rat(row["q"]) <= 1,
                "Retain the full exact common-coordinate witness and side")
        coordinate = rat(row["coordinate"])
        require(coordinate >= 0 and (row["kind"] != "prefix" or coordinate <= 1),
                "Prefix coordinates are common public u in [0,1]")
    for row in (data["job_deadline"], data["first_material_transport"], data["first_plan"],
                data["first_assembly"], field["cuff_atlas"], field["continuous_e_result"]):
        require(isinstance(row, dict) and set(row) == {"file", "bytes", "sha256"},
                "Keep the complete actual input descriptor")
        path = inside(row["file"], namespace)
        require(not path.is_relative_to(out), "The new output must not own an actual input")
    for key in ("directory", "checkpoint_directory"):
        path = inside(field[key], namespace)
        require(not path.is_relative_to(out) and not out.is_relative_to(path),
                "New output and original complete fields must be disjoint")
    return namespace, out


def actual_resolution(cp, field):
    if isinstance(cp.manifest.get("actual_resolution"), dict):
        values = copy.deepcopy(cp.manifest["actual_resolution"])
    else:
        cfg = cp.native_configuration
        boundary = cp.manifest["original_physical_boundary_description"]
        values = dict(field_modes=field.M, field_angular_quadrature=cp.raw["N"],
            native_quadrature=cfg["quadrature"], native_steps_per_stage=cfg["steps"],
            material_angles=boundary["material_angles"], physical_angles=boundary["physical_angles"],
            native_stage_count=576)
    require(set(values) == set(RESOLUTION_KEYS)
            and all(type(v) is int and v > 0 for v in values.values())
            and values["field_modes"] == field.M,
            "Keep the actual complete resolution record, not a requested future factor")
    return values


class Measurement:
    def __init__(self, data, input_id, started):
        self.data, self.input_id, self.started = data, input_id, started
        self.namespace, self.out = validate_input(data)
        self.out.mkdir(parents=True)
        self.large = self.out/"large-arrays"; self.large.mkdir()
        self.sources, self.members = {}, {}
        self.Metric = self.M = self.Kernel = self.current = self.tail = self.common = None
        self.cap = self.binding = self.plan = self.budget = None
        self.old_precision = None
        self.original_context = None
        self.cells = Journal(self.large/"complete-relative-error-cells.jsonl.gz")
        self.phases = Journal(self.large/"actual-t-grid-point-queries.jsonl.gz")
        self.phase = "actual_input_and_deadline_binding"
        self.stop = self.error = None
        self.active_root = self.current_cell = None
        self.stack = []
        self.next_rank = 0
        self.visited = self.terminal = self.terminal_without_bound = self.width_unresolved = 0
        self.upper_retired = Q(0)
        self.lower = Q(0); self.lower_witness = None
        self.phase_count = 0; self.phase_failed = []
        self.phase_work_stop = None
        self.phase_cursor = dict(time_index=0, witness_index=0, piece_position=0)
        self.phase_complete = False
        self.closed_complete = False

    def update_lower(self, lower, address):
        if lower > self.lower:
            self.lower = lower; self.lower_witness = copy.deepcopy(address)

    def bind(self):
        data = self.data
        first, first_id = read_descriptor(data["first_material_transport"])
        current_identity(first)
        deadline, deadline_id = read_descriptor(data["job_deadline"])
        current_identity(deadline)
        require(same_payload(first["original_deadline"], deadline_id)
                and deadline.get("schema") in DEADLINES
                and deadline.get("science_seconds_from_namespace") == 18900
                and deadline.get("readback_reserve_seconds") == 2700
                and type(deadline.get("namespace_created_unix_seconds")) in (int, float)
                and math.isfinite(deadline["namespace_created_unix_seconds"]),
                "Use the original actual first-material deadline without restarting it")
        self.deadline_id, self.deadline_values = deadline_id, deadline
        self.budget = Budget(self.namespace, deadline, data["work"], self.started)
        self.budget.install(); self.budget.check()
        family = FAMILIES[data["field"]["family"]]
        metric, sid = load_source(data["computations"], family["file"], family["sha256"])
        require(metric.SCHEMA == family["schema"], "The actual registered metric source schema differs")
        self.Metric = metric; self.sources[family["file"]] = sid
        loaded = {}
        for key in ("CUT_NAME", "PREFIX_NAME", "KERNEL_NAME", "C_NAME", "CUFF_NAME", "CAP_NAME", "LIVE_NAME"):
            name = getattr(metric, key)
            loaded[key], self.sources[name] = metric.load(data["computations"], name)
            self.budget.check()
        Material, self.sources[MATERIAL_NAME] = load_source(data["computations"], MATERIAL_NAME, MATERIAL_SHA)
        require(Material.SCHEMA == MATERIAL_SCHEMA, "The current complete material API differs")
        field = data["field"]; work = data["work"]
        args = SimpleNamespace(computations=Path(data["computations"]),
            directory=Path(field["directory"]), result_sha256=field["result_sha256"],
            checkpoint_directory=Path(field["checkpoint_directory"]),
            proof_directory=Path(data["proof_directory"]),
            interval_bits=work["interval_bits"]+work["max_depth"], sqrt_bits=work["sqrt_bits"],
            continuous_e_result=Path(field["continuous_e_result"]["file"]),
            continuous_e_result_sha256=field["continuous_e_result"]["sha256"],
            budget_seconds=self.budget.remaining(), out=self.out)
        for key, value in data["c_queries"].items():
            setattr(args, "c_query_"+key, value)
        Live = loaded["LIVE_NAME"]; Live.parameter_record(args)
        from flint import ctx
        self.original_context = ctx
        self.old_precision = ctx.prec
        self.current = loaded["CUT_NAME"].load_accurate_cut_field(args)
        self.M = self.current.Active; self.M.ctx.prec = args.interval_bits
        self.Kernel = loaded["KERNEL_NAME"]
        self.common = Material.bind_loaded_common_material(self.current,
            first_material_transport=data["first_material_transport"]["file"],
            first_material_sha256=data["first_material_transport"]["sha256"],
            first_plan=data["first_plan"]["file"], first_assembly=data["first_assembly"]["file"],
            budget_check=self.budget.check)
        require(same_payload(self.common.binding["actual_first_plan"], data["first_plan"])
                and same_payload(self.common.binding["actual_first_assembly"], data["first_assembly"]),
                "The explicit first plan/assembly descriptors must be the actually loaded files")
        cp = self.current.source_bundle[4].checkpoint
        current_identity(cp.manifest)
        require(cp.k == 0, "Measure the actual completely frozen accepted field")
        self.checkpoint = cp
        atlas, atlas_id = read_descriptor(field["cuff_atlas"])
        Cuff, Caps = loaded["CUFF_NAME"], loaded["CAP_NAME"]
        attachment = Cuff.bind_loaded_shared_bundle(self.current.source_bundle, atlas)
        caps = Caps.bind_loaded_shared_bundle(self.current.source_bundle, atlas, attachment, data["computations"])
        self.cap = metric.cap_metric_identity(self.current, atlas, attachment, caps)
        require(self.cap["same_actual_graph_and_target_expression"] is True
                and self.cap["complete_cap_relative_operator_error_exact"] == "0",
                "Keep both complete actual cap graph targets and their common cuff")
        fixed = metric.ActualCompleteCTarget(loaded["C_NAME"], self.current,
            args.continuous_e_result, args.continuous_e_result_sha256)
        # The original query provider has a local monotonic endpoint. Give it
        # exactly this remaining original allowance, never the original full budget again.
        live_started = time.monotonic()
        self.budget.check()
        args.budget_seconds = self.budget.remaining()
        if args.budget_seconds <= 0:
            raise ResourceStop("original_remaining_allowance_exhausted_before_live_query_binding")
        self.tail = Live.LiveQueryTarget(loaded["C_NAME"], fixed, args, self.out, live_started)
        self.budget.check()
        common = self.common.binding
        fixed_signature = dict(
            first_material_record={key:first_id[key] for key in ("bytes", "sha256")},
            accurate_target=copy.deepcopy(common["accurate_target_across_M"]["common_accurate_target_identity"]),
            actual_complete_C_input_binding=metric.identity(self.tail.expected_binding),
            complete_ten_float64le=copy.deepcopy(common["complete_ten_float64le"]),
            complete_construction_words=copy.deepcopy(common["complete_construction_words"]),
            original_cuff_float64le=common["original_cuff_float64le"],
            time_range=["0", "1"], exact_phase="alpha=pi*t/2",
            coordinate="common first material q; prefix public u; radial original r; Cartesian caps")
        self.resolution = actual_resolution(cp, self.current.field)
        mesh = [word(value) for value in cp.raw["mesh"]]
        mesh_record = dict(schema=SCHEMA+"-actual-final-mesh-words", words=mesh,
            numeric_length_exact=str(self.common.numeric_length),
            all_words_are_actual_final_solver_output=True,
            parent_seed_words_not_claimed_unchanged_at_final_solution=True)
        self.members["actual_final_mesh"] = write(self.large/"actual-final-mesh-words.json", mesh_record)
        for name, value in (("accurate_field", self.current.expression_identity()),
                            ("common_material", self.common.describe()),
                            ("complete_cap_identity", self.cap),
                            ("actual_complete_target", self.tail.describe())):
            self.members[name] = write(self.large/(name+".json"), value)
        cfg = cp.native_configuration
        self.tolerances = dict(
            original_acceptance=copy.deepcopy(cp.manifest["original_acceptance"]),
            original_probe_law=copy.deepcopy(cp.manifest["original_law"]),
            actual_checkpoint_writer=copy.deepcopy(cp.manifest["writer_source"]),
            original_frozen450_documented_thresholds=dict(collocation_rms_max=1e-6,
                boundary_residual_max=1e-11, physical_frozen_control_RMS_max=1e-6),
            actual_native_policy={key:copy.deepcopy(cfg[key]) for key in
                ("max_iterations", "line_search_trials", "nonlinear_tolerance", "sensitivity_eta") if key in cfg},
            actual_final_native_binding_identity=value_identity(cp.manifest["final_native_binding"]),
            actual_final_native_original_scalars={key:copy.deepcopy(cp.manifest["final_native_binding"][key])
                for key in ("actual_call", "original_normalized_residual", "original_meanSlope", "original_meanSecond",
                            "complete_checkpoint_rows", "complete_checkpoint_shape_columns")
                if key in cp.manifest["final_native_binding"]},
            actual_original_H_FD_record=copy.deepcopy(cp.manifest["original_current_H_FD_record"]),
            original_cut_audit_record=copy.deepcopy(cp.manifest["original_physical_cut_audit_record"]),
            ODE_RMS_BC_FD_and_native_residual_are_not_this_global_relative_metric_norm=True,
            tolerance_to_metric_error_transfer_bound_produced=False,
            reaching_original_solver_tolerance_not_relabelled_as_metric_precision_floor=True)
        self.binding = dict(schema=SCHEMA+"-binding", source=receipt(__file__),
            actual_input=self.input_id, direct_sources=copy.deepcopy(self.sources),
            actual_job_deadline=deadline_id, original_deadline_values=deadline,
            actual_field_family=data["field"]["family"],
            actual_checkpoint=copy.deepcopy(cp.receipt), actual_checkpoint_parent=copy.deepcopy(cp.manifest.get("parent")),
            actual_checkpoint_writer=copy.deepcopy(cp.manifest["writer_source"]),
            actual_checkpoint_driver=copy.deepcopy(cp.manifest["actual_driver_source"]),
            current_accurate_field_binding=copy.deepcopy(self.current.binding),
            actual_shared_result=receipt(Path(field["directory"])/"result.json"),
            actual_cuff_atlas=atlas_id, actual_cuff_attachment=copy.deepcopy(attachment),
            original_C_target=copy.deepcopy(self.tail.receipts),
            fixed_closed_target_signature=fixed_signature,
            fixed_closed_target_signature_identity=value_identity(fixed_signature),
            actual_resolution=copy.deepcopy(self.resolution),
            first_and_current_material_definition=copy.deepcopy(common),
            original_tolerance_evidence=copy.deepcopy(self.tolerances),
            full_original_accepted_loader_used=True, old_Gauss_field_not_relabelled_as_C=True,
            same_g_not_reduced_to_matching_ten_words=True)
        self.members["input_binding"] = write(self.large/"input-binding.json", self.binding)
        self.plan = self.Kernel.root_plan(self.current.field, self.current.target, self.tail,
            work["initial_angular_depth"])
        require(self.plan["planned_roots"] > 0, "The actual complete active field has no closed roots")
        self.plan["original_root_algorithm_schema"] = self.plan["schema"]
        self.plan["schema"] = SCHEMA+"-full-active-root-plan"
        self.members["root_plan"] = write(self.large/"full-active-root-plan.json", self.plan)
        self.cells.append(dict(type="identity", binding=self.members["input_binding"], root_plan=self.members["root_plan"]))

    def target(self, piece, radial, angular, *, common_q=False):
        M, Kernel = self.M, self.Kernel
        if common_q:
            phi = self.common.first_angle.derivatives(M, M.interval(*angular), 1)[1]
            local = M.bounds(phi)
            known = M.bounds(self.common.first_angle.global_derivative_interval(M))
            theta = max(local[0], known[0]), min(local[1], known[1])
            require(0 < theta[0] <= theta[1], "The actual first material derivative bounds disagree")
        else:
            value, _ = Kernel.angle_density(self.current.field, M, angular)
            theta = M.bounds(value)
        if piece["kind"] == "prefix":
            jets, radial_metric, target_record = self.current.target.closed_range(*radial)
            if jets[0].lo <= 0:
                return None, dict(reason="accurate_prefix_radius_positive_lower_unresolved", target=target_record)
            g11 = radial_metric.lo, radial_metric.hi
            if common_q:
                scale = self.common.numeric_length
                g11 = multiply(g11, (scale*scale, scale*scale))
            g22 = multiply(square((jets[0].lo, jets[0].hi)), square(theta))
            return (g11, g22), dict(kind="complete_accurate_ten_public_u", target=target_record)
        require(piece["kind"] in ("native", "collar"), "Do not omit an unknown accurate active piece")
        bound = self.tail.bounds(*radial)
        if bound is None:
            return None, dict(reason="same_C_whole_closed_radial_target_unpaid", radial=encode(radial))
        lo, hi, rows = bound
        return ((lo, hi), multiply(square(radial), square(theta))), dict(
            kind="same_complete_C_radial", radial=encode(radial), actual_query_rows=rows,
            geometric_Bprime_not_substituted=True)

    def base_once(self, cell):
        self.budget.check()
        piece = self.current.field.pieces[cell["piece_index"]]
        radial, angular = pair(cell["radial"]), pair(cell["angular"])
        target, target_record = self.target(piece, radial, angular)
        if target is None:
            return dict(available=False, target=target_record)
        values = self.current.evaluate(piece, radial, angular, cell["lower"])
        X, Y = tuple(value.d[1] for value in values), tuple(value.d[2] for value in values)
        E, B, C = (self.M.bounds(self.M.dot(a, b)) for a, b in ((X, X), (X, Y), (Y, Y)))
        result = relative_norm(E, B, C, *target, self.data["work"]["sqrt_bits"])
        result["target"] = target_record
        result["all_current_modes_both_means_and_mixed_jets_used"] = True
        return result

    def base_measure(self, cell):
        report = self.base_once(cell)
        kind = self.current.field.pieces[cell["piece_index"]]["kind"]
        span = None if not report["available"] else pair(report["norm_interval"])
        goal = rat(self.data["work"]["measurement_width_goal"])
        if kind != "prefix" and (span is None or span[1]-span[0] > goal):
            self.budget.check()
            attempt = self.tail.refine(*pair(cell["radial"]), cell=cell)
            if attempt.get("attempted") and attempt.get("complete_closed_query_bound"):
                report = self.base_once(cell)
            report["actual_live_query_attempt"] = attempt
        return report

    def witness_pieces(self, row):
        x = rat(row["coordinate"])
        original = x*self.common.numeric_length if row["kind"] == "prefix" else x
        indices = [i for i, piece in enumerate(self.current.field.pieces)
            if (piece["kind"] == "prefix") == (row["kind"] == "prefix")
            and piece["left"] <= original <= piece["right"]]
        require(indices, "The declared witness has no actual closed piece membership")
        return original, indices

    def phase_grid(self):
        self.phase = "actual_nested_t_grid_point_queries"
        grid, work = self.data["time_grid"], self.data["work"]
        memberships = [self.witness_pieces(row) for row in grid["witnesses"]]
        self.members["phase_grid_plan"] = write(self.large/"phase-grid-plan.json", dict(
            schema=SCHEMA+"-phase-grid-plan", subdivisions=grid["subdivisions"],
            time_formula="t=k/subdivisions; k=0,...,subdivisions, both endpoints included",
            time_range=["0", "1"], witnesses=copy.deepcopy(grid["witnesses"]),
            memberships=[dict(original_radial=str(value), all_closed_piece_indices=indices)
                         for value, indices in memberships],
            full_phase_certificate_not_inferred_from_this_finite_grid=True))
        for k in range(grid["subdivisions"]+1):
            t = Q(k, grid["subdivisions"])
            for j, row in enumerate(grid["witnesses"]):
                radial, indices = memberships[j]
                for at, index in enumerate(indices):
                    self.phase_cursor = dict(time_index=k, witness_index=j, piece_position=at,
                        current_piece_index=index, complete_piece_indices=indices)
                    if self.phase_count >= work["max_phase_query_cells"]:
                        self.phase_work_stop = "declared_phase_query_cell_work_count_reached"
                        return
                    self.budget.check()
                    address = dict(time_index=k, time_exact=str(t), witness_index=j,
                        piece_position=at, piece_index=index, lower=row["lower"])
                    try:
                        values = self.common.evaluate_active_cell(index,
                            (rat(row["coordinate"]), rat(row["coordinate"])),
                            (rat(row["q"]), rat(row["q"])), (t, t), row["lower"],
                            interval_bits=work["interval_bits"]+work["max_depth"],
                            max_inverse_steps=work["max_inverse_steps"])
                        piece = self.current.field.pieces[index]
                        target, target_record = self.target(piece, (radial, radial),
                            (rat(row["q"]), rat(row["q"])), common_q=True)
                        if target is None and piece["kind"] != "prefix":
                            self.tail.refine(radial, radial, cell=dict(address, actual_common_witness=row))
                            target, target_record = self.target(piece, (radial, radial),
                                (rat(row["q"]), rat(row["q"])), common_q=True)
                        if target is None:
                            result = dict(available=False, target=target_record)
                        else:
                            X, Y = values["six_jets"]["u"], values["six_jets"]["q"]
                            E, B, C = (self.M.bounds(self.M.dot(a, b)) for a, b in ((X, X), (X, Y), (Y, Y)))
                            result = relative_norm(E, B, C, *target, work["sqrt_bits"])
                            result["target"] = target_record
                        result["actual_common_material_sixjet_query"] = self.common.encode_active_cell(values)
                    except (ArithmeticError, ValueError, KeyError, TypeError) as error:
                        result = dict(available=False, error=dict(type=type(error).__name__, message=str(error)))
                    self.phases.append(dict(type="point_query_return", address=address, result=result))
                    self.phase_count += 1
                    if result["available"]:
                        self.update_lower(pair(result["norm_interval"])[0], dict(kind="actual_common_phase_point", **address))
                    else:
                        self.phase_failed.append(dict(address=address,
                            reason=result.get("reason") or result.get("target", {}).get("reason"),
                            error=result.get("error")))
                self.phase_cursor = dict(time_index=k, witness_index=j+1, piece_position=0)
            self.phase_cursor = dict(time_index=k+1, witness_index=0, piece_position=0)
        self.phase_complete = not self.phase_failed

    def full_cover(self):
        self.phase = "complete_both_sheet_closed_base_phase_cover"
        work = self.data["work"]
        goal = rat(work["measurement_width_goal"])
        for root in self.Kernel.roots(self.plan):
            self.active_root = root
            self.next_rank = root["rank"]
            self.stack = [dict(cell=root, fallback=None)]
            while self.stack:
                # Never pop the current responsibility before a budget check
                # and the complete prepare/commit replacement of its children.
                self.budget.check()
                if self.visited >= work["max_cells"]:
                    raise ResourceStop("declared_complete_closed_cell_work_count_reached")
                entry = self.stack[-1]
                cell = entry["cell"]
                self.current_cell = cell
                fallback = None if entry["fallback"] is None else pair(entry["fallback"])
                try:
                    report = self.base_measure(cell)
                except (ArithmeticError, ValueError, KeyError, TypeError) as error:
                    report = dict(available=False, error=dict(type=type(error).__name__, message=str(error)))
                self.visited += 1
                bound = pair(report["norm_interval"]) if report["available"] else None
                if fallback is not None:
                    bound = fallback if bound is None else (max(bound[0], fallback[0]), min(bound[1], fallback[1]))
                    require(bound[0] <= bound[1], "A sound parent and child relative-error enclosure became disjoint")
                if bound is not None:
                    self.update_lower(bound[0], dict(kind="uniform_closed_cell_lower", rank=cell["rank"],
                        dyadic_path=cell["dyadic_path"], lower=cell["lower"]))
                refine = (bound is None or bound[1]-bound[0] > goal) and cell["depth"] < work["max_depth"]
                record = dict(type="cell_return", cell=cell, original_evaluation=report,
                    retained_sound_bound=encode(bound), inherited_parent_bound=encode(fallback), split=refine)
                self.cells.append(record)
                if refine:
                    children = self.Kernel.split_cell(cell)
                    replacement = self.stack[:-1]+[
                        dict(cell=child, fallback=encode(bound)) for child in reversed(children)]
                    self.stack = replacement
                else:
                    self.terminal += 1
                    if bound is None:
                        self.terminal_without_bound += 1
                    else:
                        self.upper_retired = max(self.upper_retired, bound[1])
                        if bound[1]-bound[0] > goal:
                            self.width_unresolved += 1
                    self.stack = self.stack[:-1]
                self.current_cell = None
            self.next_rank = root["rank"]+1
            self.active_root = None
        self.closed_complete = True

    def coverage(self):
        if self.plan is None:
            return dict(root_plan_constructed=False, entire_closed_domain_unpaid=True,
                current_phase=self.phase, active_closed_frontier=[], untouched_root_rank_suffix=None), None
        planned = self.plan["planned_roots"]
        suffix_start = self.next_rank+(1 if self.active_root is not None else 0)
        suffix = [suffix_start, planned]
        frontier = copy.deepcopy(self.stack)
        current_included = self.current_cell is None or any(
            entry["cell"] == self.current_cell for entry in frontier)
        require(current_included, "Retain the complete in-flight responsibility in the actual stack")
        pending_bounds = [None if row["fallback"] is None else pair(row["fallback"]) for row in frontier]
        finite = (self.cap is not None and self.tail is not None and self.tail.conditions_proved
                  and self.terminal_without_bound == 0 and suffix[0] == suffix[1]
                  and all(row is not None for row in pending_bounds))
        upper = max([self.upper_retired]+[row[1] for row in pending_bounds if row is not None]) if finite else None
        return dict(root_plan_constructed=True, planned_roots=planned,
            full_original_root_definition=self.members.get("root_plan"),
            active_original_root=copy.deepcopy(self.active_root), active_closed_frontier=frontier,
            untouched_root_rank_suffix=suffix, suffix_upper_exclusive=True,
            visited_cells=self.visited, retired_terminal_cells=self.terminal,
            terminal_cells_without_a_bound=self.terminal_without_bound,
            bounded_terminals_above_work_width_goal=self.width_unresolved,
            completed_all_DFS_work=self.closed_complete,
            every_unpaid_retired_terminal_retained_in_complete_cell_ledger=True,
            parent_bound_remains_valid_over_each_pending_child=True,
            all_closed_domain_has_a_finite_bound=finite,
            whole_geometry_not_inferred_from_visited_samples=True), upper

    def finish(self):
        close_errors = []
        if self.tail is not None:
            try:
                self.members["live_query_ledgers"] = self.tail.close()
            except BaseException as error:
                close_errors.append(dict(scope="live_query", type=type(error).__name__, message=str(error)))
        for name, journal in (("complete_cell_ledger", self.cells), ("actual_phase_point_ledger", self.phases)):
            try:
                self.members[name] = journal.close()
            except BaseException as error:
                close_errors.append(dict(scope=name, type=type(error).__name__, message=str(error)))
        coverage, upper = self.coverage()
        self.members["complete_coverage_and_pending"] = write(self.large/"complete-coverage-and-pending.json", coverage)
        if self.error is not None or close_errors:
            upper = None
        work = self.data["work"]
        complete_bound = upper is not None and self.binding is not None
        if complete_bound and self.lower > upper:
            self.error = dict(type="ArithmeticError", phase="complete_measurement_readout",
                message="Actual lower witnesses contradict the full-domain upper enclosure",
                retained_lower=str(self.lower), retained_upper=str(upper))
            upper, complete_bound = None, False
        fixed = None if self.binding is None else self.binding["fixed_closed_target_signature"]
        result = dict(schema=SCHEMA, repository=REPOSITORY, run_id=os.environ.get("GITHUB_RUN_ID"),
            source_commit=os.environ.get("GITHUB_SHA"), source=receipt(__file__), label=self.data["label"],
            actual_input=self.input_id, phase=self.phase,
            actual_job_deadline=getattr(self, "deadline_id", None),
            fixed_closed_target_signature=fixed,
            actual_checkpoint=None if self.binding is None else self.binding["actual_checkpoint"],
            actual_checkpoint_parent=None if self.binding is None else self.binding["actual_checkpoint_parent"],
            actual_field_family=self.data["field"]["family"],
            actual_resolution=getattr(self, "resolution", None),
            actual_final_mesh=self.members.get("actual_final_mesh"),
            parameters=dict(work=copy.deepcopy(work), c_queries=copy.deepcopy(self.data["c_queries"]),
                time_grid=copy.deepcopy(self.data["time_grid"])),
            global_relative_operator_error=dict(
                norm_definition="sup over the entire closed surface and t in [0,1] of ||g_first^(-1/2)(F_t^*e-g_first)g_first^(-1/2)||_op",
                lower=str(self.lower), upper=None if upper is None else str(upper),
                actual_best_lower_witness=copy.deepcopy(self.lower_witness),
                complete_domain_upper_available=complete_bound,
                every_common_exact_C_root_member_retained=True,
                upper_le_requested_metric_reference=(complete_bound and upper <= rat(work["metric_reference_eta"])),
                reference_eta_exact=str(rat(work["metric_reference_eta"])),
                source_only_eta_pass_count_not_used=True,
                accurately_defined_current_field_not_original_rounded_RK_error=True),
            all_time_transfer=dict(
                actual_common_material_binding_present=self.common is not None,
                actual_complete_two_cap_identity=self.cap is not None,
                complete_base_circle_and_all_reflections_covered=complete_bound,
                whole_time_metric_bound_paid_for_the_bound_accurate_family=complete_bound,
                formula="F_j,t=R_alpha F_j,0(x,Theta_j^(-1)(Theta_first(q)-alpha)); caps fixed",
                relative_operator_norm_invariant_under_exact_congruence=True,
                full_circle_bijection_not_endpoint_or_finite_time_inference=True,
                actual_cuff_cut_and_all_target_atlas_contracts_retained=True,
                embedding_reach_held_or_uniform_refinement_C2_convergence_proved=False),
            actual_time_grid=dict(subdivisions=self.data["time_grid"]["subdivisions"],
                witnesses=copy.deepcopy(self.data["time_grid"]["witnesses"]),
                complete_queries=self.phase_complete, actual_query_cells=self.phase_count,
                next_unvisited_address=copy.deepcopy(self.phase_cursor),
                explicit_phase_work_stop=self.phase_work_stop,
                completed_but_unbounded_queries=copy.deepcopy(self.phase_failed),
                complete_grid_plan=self.members.get("phase_grid_plan"),
                finite_t_grid_not_the_reason_for_whole_time_bound=True),
            coverage=coverage,
            original_tolerance_evidence=getattr(self, "tolerances", None),
            original_native_BVP_FD_fullDN_final_or_acceptance_gate_changed=False,
            scalar_speed_domain_and_infinite_DN_not_proved_here=True,
            original_RK_or_physical_quintic_rounding_error_not_paid_by_new_source_label=True,
            metric_work_width_is_not_a_scientific_acceptance_threshold=True,
            close_errors=close_errors, resource_stop=self.stop, execution_error=self.error,
            elapsed_seconds=time.monotonic()-self.started, members=copy.deepcopy(self.members),
            no_subprocess_started=True, no_raw_payload_deleted=True,
            clock_scope="Original absolute deadline plus explicit cooperative measurement allowance; caller still owns external termination/quiet",
            scientific_task_completion_not_claimed=True)
        return result


def necessary(result):
    if result["schema"] == SERIES_SCHEMA:
        return copy.deepcopy(result)
    keys = ("schema", "repository", "run_id", "source_commit", "source", "label", "actual_input", "phase",
        "actual_job_deadline", "fixed_closed_target_signature", "actual_checkpoint", "actual_checkpoint_parent",
        "actual_field_family", "actual_resolution", "actual_final_mesh", "parameters",
        "global_relative_operator_error", "all_time_transfer", "actual_time_grid", "original_tolerance_evidence",
        "original_native_BVP_FD_fullDN_final_or_acceptance_gate_changed",
        "scalar_speed_domain_and_infinite_DN_not_proved_here",
        "original_RK_or_physical_quintic_rounding_error_not_paid_by_new_source_label",
        "metric_work_width_is_not_a_scientific_acceptance_threshold", "close_errors", "resource_stop",
        "execution_error", "elapsed_seconds", "members", "no_subprocess_started", "no_raw_payload_deleted",
        "clock_scope", "scientific_task_completion_not_claimed")
    summary = {key:copy.deepcopy(result[key]) for key in keys}
    coverage = result["coverage"]
    summary["necessary_coverage"] = {key:copy.deepcopy(value) for key, value in coverage.items()
        if key not in ("active_original_root", "active_closed_frontier")}
    summary["necessary_coverage"]["active_closed_frontier"] = [dict(
        rank=row["cell"]["rank"], dyadic_path=row["cell"]["dyadic_path"], depth=row["cell"]["depth"],
        sound_ancestor_error_bound=row["fallback"])
        for row in coverage.get("active_closed_frontier", [])]
    summary["necessary_coverage"]["full_unpaid_terminal_rows_in_original_ledger_not_all_retransmitted"] = True
    return summary


def emit(directory, result, result_id):
    summary = necessary(result)
    summary["actual_complete_result"] = result_id
    row = write(Path(directory)/"summary.json", summary)
    if row["bytes"] > SUMMARY_LIMIT:
        print(json.dumps(dict(schema=SCHEMA+"-necessary-over-budget", original_summary=row,
            limit=SUMMARY_LIMIT, complete_necessary_emitted=False, original_raw_retained=True,
            no_part_or_encoded_transport=True), separators=(",", ":")), flush=True)
        return 70
    print("BEGIN_R459_FIXED_TARGET_METRIC_EVIDENCE", flush=True)
    print(canonical(summary).decode(), end="", flush=True)
    print("END_R459_FIXED_TARGET_METRIC_EVIDENCE", flush=True)
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as stream:
            for key, value in (("metric_evidence_summary", row["file"]),
                ("metric_evidence_summary_bytes", row["bytes"]),
                ("metric_evidence_summary_sha256", row["sha256"])):
                stream.write(key+"="+str(value)+"\n")
    return 2 if result.get("execution_error") or result.get("close_errors") else 0


def measure(path, expected):
    actions()
    started = time.monotonic()
    data, input_id = read_bound(path, expected)
    run = Measurement(data, input_id, started)
    try:
        run.bind()
        run.phase_grid()
        run.full_cover()
        run.phase = "complete_measurement_readout"
    except ResourceStop as error:
        run.stop = dict(type=type(error).__name__, message=str(error), phase=run.phase,
            mathematical_failure_not_inferred=True)
    except BaseException as error:
        run.error = dict(type=type(error).__name__, message=str(error), phase=run.phase)
    finally:
        if run.budget is not None:
            run.budget.restore()
        if run.original_context is not None and run.old_precision is not None:
            run.original_context.prec = run.old_precision
    result = run.finish()
    result_id = write(run.out/"result.json", result)
    return emit(run.out, result, result_id)


def mesh_words(result):
    descriptor = result.get("actual_final_mesh")
    if descriptor is None:
        return None
    value, _ = read_descriptor(descriptor)
    require(value.get("schema") == SCHEMA+"-actual-final-mesh-words"
            and value.get("all_words_are_actual_final_solver_output") is True,
            "Use the original actual final solver mesh word list")
    values = value["words"]
    require(isinstance(values, list) and all(isinstance(x, str) and len(x) == 16 for x in values),
            "Keep all complete final binary64 mesh words")
    return value


def compare(path, expected):
    actions()
    data, input_id = read_bound(path, expected)
    require(set(data) == {"schema", "namespace", "measurements", "out"} and data["schema"] == SERIES_INPUT,
            "Use the exact actual measurement-series input")
    namespace = Path(data["namespace"]).resolve(strict=True)
    runner = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    require(namespace != runner and namespace.is_relative_to(runner), "Keep same-job owned temporary data")
    out = inside(data["out"], namespace, exists=False)
    require(not out.exists(), "Preserve every previous comparison")
    rows = data["measurements"]
    require(isinstance(rows, list) and rows, "Compare actual returned measurement records only")
    actual_source = receipt(__file__)
    reports, identities, meshes = [], [], []
    for descriptor in rows:
        inside(descriptor["file"], namespace)
        value, row = read_descriptor(descriptor)
        current_identity(value)
        require(value.get("schema") == SCHEMA and same_payload(value.get("source"), actual_source),
                "Every comparison member must be this actual measurement source")
        reports.append(value); identities.append(row); meshes.append(mesh_words(value))
    first_fixed = next((row.get("fixed_closed_target_signature") for row in reports
                        if row.get("fixed_closed_target_signature") is not None), None)
    actual_fixed = all(row.get("fixed_closed_target_signature") is not None
                       and row["fixed_closed_target_signature"] == first_fixed for row in reports)
    actual_clock = all(same_payload(row.get("actual_job_deadline"), reports[0].get("actual_job_deadline"))
                       for row in reports)
    pairs = []
    for index, (old, new) in enumerate(zip(reports, reports[1:])):
        a, b = old["global_relative_operator_error"], new["global_relative_operator_error"]
        compatible = actual_fixed and actual_clock
        bounded = compatible and a["complete_domain_upper_available"] and b["complete_domain_upper_available"]
        strict = bounded and rat(b["upper"]) < rat(a["lower"])
        improved = bounded and rat(b["upper"]) < rat(a["upper"])
        increased = bounded and rat(b["lower"]) > rat(a["upper"])
        change = {}
        if old["actual_resolution"] is not None and new["actual_resolution"] is not None:
            for key in RESOLUTION_KEYS:
                before, after = old["actual_resolution"][key], new["actual_resolution"][key]
                change[key] = dict(before=before, after=after, increased=after > before, nondecreased=after >= before)
        before_grid, after_grid = old["actual_time_grid"], new["actual_time_grid"]
        n0, n1 = before_grid["subdivisions"], after_grid["subdivisions"]
        same_witnesses = before_grid["witnesses"] == after_grid["witnesses"]
        truly_nested = (same_witnesses and n1 >= n0 and n1 % n0 == 0
                        and before_grid["complete_queries"] and after_grid["complete_queries"])
        mesh = None
        m0, m1 = meshes[index], meshes[index+1]
        if m0 is not None and m1 is not None:
            old_words, new_words = m0["words"], m1["words"]
            mesh = dict(previous_node_count=len(old_words), current_node_count=len(new_words),
                previous_complete_words=old["actual_final_mesh"], current_complete_words=new["actual_final_mesh"],
                final_mesh_word_nested=set(old_words).issubset(set(new_words)),
                final_node_count_increased=len(new_words) > len(old_words),
                numeric_prefix_lengths_equal=m0["numeric_length_exact"] == m1["numeric_length_exact"],
                source_seed_contract_does_not_force_adaptive_final_mesh_nesting=True,
                explicit_seed_refinement_and_resource_receipts_owned_by_original_refinement_driver=True)
        parent = new.get("actual_checkpoint_parent")
        actual_parent = isinstance(parent, dict) and same_payload(parent.get("manifest"), old.get("actual_checkpoint"))
        pairs.append(dict(previous_index=index, current_index=index+1,
            same_fixed_closed_target_and_original_clock=compatible,
            previous_error=dict(lower=a["lower"], upper=a["upper"]),
            current_error=dict(lower=b["lower"], upper=b["upper"]),
            strict_real_sup_decrease_proved_by_separated_bounds=bool(strict),
            certified_upper_envelope_improved=bool(improved),
            strict_real_sup_increase_proved_by_separated_bounds=bool(increased),
            actual_sup_comparison=("strict_decrease" if strict else "strict_increase" if increased
                else "undetermined_overlap_or_unpaid_complete_bound"),
            sufficient_interval_separation_not_a_BVP_or_refinement_gate=True,
            distinct_actual_checkpoint=not same_payload(old.get("actual_checkpoint"), new.get("actual_checkpoint")),
            actual_next_solver_parent_is_previous_checkpoint=actual_parent,
            independent_accepted_branches_not_relabelled_as_successive_solver_parents=True,
            actual_resolution_changes=change, actual_final_mesh_comparison=mesh,
            actual_time_grid=dict(previous=n0, current=n1, same_common_witnesses=same_witnesses,
                complete_nested_evaluated_grid=truly_nested,
                strictly_more_actual_times=truly_nested and n1 > n0,
                all_time_bound_still_from_exact_conjugacy_not_the_finite_grid=True)))
    levels = []
    for index, row in enumerate(reports):
        levels.append(dict(index=index, actual_result=identities[index], label=row["label"],
            actual_checkpoint=row["actual_checkpoint"], actual_resolution=row["actual_resolution"],
            actual_final_mesh=row["actual_final_mesh"],
            global_relative_operator_error=row["global_relative_operator_error"],
            actual_time_grid={key:row["actual_time_grid"][key] for key in
                ("subdivisions", "complete_queries", "actual_query_cells", "next_unvisited_address",
                 "explicit_phase_work_stop", "completed_but_unbounded_queries", "complete_grid_plan")},
            complete_pending_record=row["members"].get("complete_coverage_and_pending"),
            original_tolerance_evidence=row["original_tolerance_evidence"],
            resource_stop=row["resource_stop"], execution_error=row["execution_error"], close_errors=row["close_errors"]))
    result = dict(schema=SERIES_SCHEMA, repository=REPOSITORY, run_id=os.environ.get("GITHUB_RUN_ID"),
        source_commit=os.environ.get("GITHUB_SHA"), source=actual_source, actual_input=input_id,
        level_count=len(reports), actual_common_target=actual_fixed, actual_common_original_clock=actual_clock,
        fixed_closed_target_signature=first_fixed, levels=levels, consecutive_comparisons=pairs,
        all_complete_upper_envelopes_strictly_decrease=(len(pairs) > 0 and all(row["certified_upper_envelope_improved"] for row in pairs)),
        all_real_sup_strict_decreases_proved=(len(pairs) > 0 and all(row["strict_real_sup_decrease_proved_by_separated_bounds"] for row in pairs)),
        original_solver_tolerance_used_as_unjustified_metric_floor=False,
        finite_sequence_alone_proves_exact_limit_or_uniform_C2_convergence=False,
        interval_overlap_is_not_a_rejection_or_new_acceptance_gate=True,
        repeated_fixed_eta_passes_not_counted_as_error_decrease=True,
        fixed_material_and_cap_gluing_not_reduced_to_parameter_word_equality=True,
        caller_may_continue_original_refinement_or_tighter_measurement_within_original_budget=True,
        no_subprocess_started=True, no_raw_payload_deleted=True,
        scientific_task_completion_not_claimed=True)
    out.mkdir(parents=True)
    result_id = write(out/"result.json", result)
    return emit(out, result, result_id)


def readback(directory, expected, out):
    actions()
    result, identity = read_bound(Path(directory)/"result.json", expected)
    current_identity(result)
    require(result.get("schema") in (SCHEMA, SERIES_SCHEMA)
            and same_payload(result.get("source"), receipt(__file__)),
            "Read only an actual result from this exact independent source")
    out = Path(out).resolve()
    runner = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    require(not out.exists() and out != runner and out.is_relative_to(runner)
            and not Path(directory).resolve().is_relative_to(out),
            "Use a fresh owned readback directory without owning its input")
    out.mkdir(parents=True)
    # Every necessary object is already in result; big successful scientific
    # ledgers are identified, not reassembled or represented as independently audited.
    return emit(out, result, identity)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="operation", required=True)
    for name in ("measure", "compare"):
        p = sub.add_parser(name); p.add_argument("--input", required=True)
        p.add_argument("--input-sha256", required=True)
    p = sub.add_parser("readback")
    p.add_argument("--directory", required=True); p.add_argument("--result-sha256", required=True)
    p.add_argument("--out", required=True)
    args = parser.parse_args(argv)
    if args.operation == "measure":
        return measure(args.input, args.input_sha256)
    if args.operation == "compare":
        return compare(args.input, args.input_sha256)
    return readback(args.directory, args.result_sha256, args.out)


if __name__ == "__main__":
    raise SystemExit(main())
