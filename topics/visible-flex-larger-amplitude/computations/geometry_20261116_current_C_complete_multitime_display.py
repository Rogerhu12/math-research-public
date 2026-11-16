#!/usr/bin/env python3
"""R461 finite display meshes of an actual accurately defined current field.

This is a display consumer, not a BVP, metric, reach, held or full-time test.
Every active vertex is enclosed by the current accurate-cut interpreter;
the old numerical A renderer is never used.  Coordinate projection happens
only after interval evaluation.  Each PLY vertex stores three outward error
radii in addition to its binary64 coordinates.  Original absolute-clock and
temporary-data ownership remain with the real same-job caller.

All mathematical imports and evaluations are public Actions only.  This
source was prepared by text work; no local import, AST, compile or science.
Author: OpenAI ChatGPT /root/amplitude (AI), 2026-11-16.
"""
from __future__ import annotations

import argparse
from bisect import bisect_left
import copy
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import signal
import struct
import sys
import time
import traceback
from types import SimpleNamespace

REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "R461-current-accurate-closed-multitime-display-v1"
INPUT_SCHEMA = SCHEMA + "-input"
SUMMARY_LIMIT = 90000
FILE_LIMIT = 5000000                 # strict less-than, for every owned file
VERTEX = struct.Struct("<6dB")       # xyz, outward ex/ey/ez, piece label
FACE = struct.Struct("<B3i")
DEFAULT_TIMES = ("0", "1/2", "1")
DEFAULT_GRID = dict(prefix_intervals=8, tail_intervals=8,
                    cap_intervals=4, angular_intervals=32)
MATERIAL_NAME = "geometry_20261116_current_C_actual202_M_common_material_phase.py"
MATERIAL_SHA = "059d0df3ab5957b8ba5adf69e305ee4663ba06378242fe4c5f2116bab437af41"
ACTIVE_NAME = "geometry_20261115_shared_active_interval_balls.py"
ACTIVE_SHA = "675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b"
FAMILIES = {
    "current112": dict(
        schema="R416-current-C-ten450-accurate-cut-atlas-field-v1",
        cut="geometry_20261115_current_C_accurate_cut_patch.py",
        cut_sha="28417b93fc4fa7780e049ab7d8c4d98e4f51412afd1ced5fc36558ae1e0d837b",
        shared="geometry_20261115_current_C_ten450_shared_field.py",
        shared_sha="6a5f949a0422d0a4794c270140a777af1b2e2f7c73f99ef99e0601fdc634d6f3",
        atlas="geometry_20261115_current_C_original_cuff_target_atlas.py",
        atlas_sha="02bb0c70198c54e4ebe8d0fa2ebb6f74d0b17a6193378b0169746926a3b52fd2",
        caps="geometry_20261115_current_C_ten450_fixed_cap_balls.py",
        caps_sha="0ff1fa60a619a7df8e58e72e240dc42e99850eacd05b6426cc70e9083f76afae"),
    "resolution112": dict(
        schema="R441-current-C-resolution450-accurate-cut-atlas-field-v1",
        cut="geometry_20261116_current_C_resolution_accurate_cut_patch.py",
        cut_sha="8811f89c7395bb4aed1adabe6c6825c801e1e41a9d80d416b0a4746596ae9a52",
        shared="geometry_20261116_current_C_ten450_resolution_shared_field.py",
        shared_sha="1ceda9d32cfcf50e28e737cd0aee981cb8dc2329027aa2967d08532a1ea6e935",
        atlas="geometry_20261116_current_C_resolution_original_cuff_atlas.py",
        atlas_sha="d0b03a367f3ece13b06949d5218a992e6ee3e9a41364499070d3f5f475a150a0",
        caps="geometry_20261116_current_C_resolution_fixed_cap_balls.py",
        caps_sha="ca53bdc5c0cdd5764065301f0edb1259d083fdffa9f3d767a5a38b4a7cafe364"),
    "completeM": dict(
        schema="R451-current-C-complete-M-accurate-cut-atlas-field-v1",
        cut="geometry_20261116_current_C_M_accurate_cut_patch.py",
        cut_sha="747b9d1f77b307529aeb65e3ad31e831b9f54238916bcae23fa578efd6a76492",
        shared="geometry_20261116_current_C_ten_M_shared_field.py",
        shared_sha="db1f6fd39bef3d9ce2543276771cbcea1c2432a7221b8f295ed5b553b2171f87",
        atlas="geometry_20261116_current_C_M_original_cuff_atlas.py",
        atlas_sha="97e4a49f0a9913094dec5f78b173437028f553a5bf0aa36f0b0b9d53929a9621",
        caps="geometry_20261116_current_C_M_fixed_cap_balls.py",
        caps_sha="21f755aad5bb5616356005f575db76c1a6826b3a33197a14e1d6910aa069984a"),
}
ORIGINS = {
    "current-C-continuous-ten-full453-frozen450-owned-process-launch-v1": (
        "6ff21118040ad4006ae8170923996ee11e34163ce38fc460dd6aa23f972fcd66",
        "request193-owned-job-science-deadline-v1"),
    "current-C-continuous-ten-joint-full453-frozen450-owned-process-launch-v1": (
        "cb05724bbedf71951524d187d242c1783d244bc729241ec91a91e0a9cf8f02d7",
        "request203-owned-job-science-deadline-v1"),
    "R449-actual202-accurate-ten-full453-frozen450-owned-process-launch-v1": (
        "227ef601ad910cb424f115cf93f8bb55e56dc74be5bb451839dab06f0ce627c7",
        "request205-owned-job-science-deadline-v1"),
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY
            and bool(os.environ.get("GITHUB_RUN_ID"))
            and bool(os.environ.get("GITHUB_SHA")),
            "All current-field evaluation belongs to the named public Actions")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=True, allow_nan=False) + "\n").encode("ascii")


def identity(value):
    raw = canonical(value)
    return dict(canonical_bytes=len(raw), canonical_sha256=sha(raw))


def receipt(path):
    path = Path(path).resolve(strict=True)
    digest, size = hashlib.sha256(), 0
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1048576), b""):
            size += len(block)
            digest.update(block)
    return dict(file=str(path), bytes=size, sha256=digest.hexdigest())


def same_payload(a, b):
    return (isinstance(a, dict) and isinstance(b, dict)
            and a.get("bytes") == b.get("bytes")
            and a.get("sha256") == b.get("sha256"))


def read(path, expected=None):
    row = receipt(path)
    if isinstance(expected, str):
        require(row["sha256"] == expected, "Actual file SHA differs: " + str(path))
    elif expected is not None:
        require(same_payload(row, expected), "Actual file bytes/SHA differ: " + str(path))
    return json.loads(Path(path).read_bytes()), row


def contained(path, root, *, exists=True):
    path, root = Path(path).resolve(), Path(root).resolve()
    require(path != root and path.is_relative_to(root),
            "Use a genuine child of the actual owned namespace")
    require(not exists or path.exists(), "The actual required payload no longer exists")
    return path


def write(path, value):
    raw = canonical(value)
    if len(raw) >= FILE_LIMIT:
        raise ResourceStop("An owned metadata file would exceed the strict per-file limit")
    with Path(path).open("xb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    return receipt(path)


def exact(value):
    require(type(value) in (str, int), "Use explicit rational strings or integer coordinates")
    return Q(value)


def integer(value, label, minimum=1):
    require(type(value) is int and value >= minimum, "Invalid explicit integer: " + label)
    return value


def positive(value, label):
    require(type(value) in (int, float) and math.isfinite(value) and value > 0,
            "Invalid explicit positive resource: " + label)
    return float(value)


def current_job(value):
    require(value.get("run_id") == os.environ["GITHUB_RUN_ID"]
            and value.get("source_commit") == os.environ["GITHUB_SHA"],
            "Use the actual current job's defining inputs")


def load_source(directory, name, expected):
    path = (Path(directory) / name).resolve(strict=True)
    row = receipt(path)
    require(row["sha256"] == expected, "The explicit current source differs: " + name)
    module_name = "_R461_" + name[:-3]
    spec = importlib.util.spec_from_file_location(module_name, path)
    require(spec is not None and spec.loader is not None, "Unable to load the actual source")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        sys.modules.pop(module_name, None)
        raise
    return module, row


class ResourceStop(RuntimeError):
    pass


class ExternalStop(RuntimeError):
    pass


class LimitedWriter:
    """A gzip sink refuses the crossing block before it reaches the file."""
    def __init__(self, stream):
        self.stream = stream

    def write(self, raw):
        if self.stream.tell()+len(raw) >= FILE_LIMIT:
            raise ResourceStop("The next compressed block would reach the strict per-file limit")
        return self.stream.write(raw)

    def tell(self):
        return self.stream.tell()

    def flush(self):
        return self.stream.flush()


def upward(value):
    """One finite outward nonnegative binary64 radius; exact check after RN."""
    require(value >= 0, "An error radius cannot be negative")
    result = float(value)
    if not math.isfinite(result):
        raise ArithmeticError("A finite binary64 display-error radius is unavailable")
    if Q.from_float(result) < value:
        result = math.nextafter(result, math.inf)
    if not math.isfinite(result) or Q.from_float(result) < value:
        raise ArithmeticError("An outward finite display-error radius is unavailable")
    return result


def float_record(value):
    return dict(value=value, float64le=struct.pack("<d", value).hex())


class VertexErrors:
    def __init__(self):
        self.count = 0
        self.values = {key: [Q(0)]*3 for key in
                       ("evaluation_halfwidth", "midpoint_projection", "total_point_error")}
        self.addresses = {key: [None]*3 for key in self.values}
        self.stored = [0.0]*3

    def vertex(self, boxes, label, address):
        coordinates, radii = [], []
        for axis, (lo, hi) in enumerate(boxes):
            require(lo <= hi, "The actual point enclosure is reversed")
            middle = (lo+hi)/2
            coordinate = float(middle)
            if not math.isfinite(coordinate):
                raise ArithmeticError("The actual point has no finite binary64 display coordinate")
            projected = Q.from_float(coordinate)
            halfwidth = (hi-lo)/2
            rounding = abs(projected-middle)
            total = max(abs(projected-lo), abs(projected-hi))
            radius = upward(total)
            for key, value in (("evaluation_halfwidth", halfwidth),
                               ("midpoint_projection", rounding),
                               ("total_point_error", total)):
                if value > self.values[key][axis] or self.addresses[key][axis] is None:
                    self.values[key][axis] = value
                    self.addresses[key][axis] = copy.deepcopy(address)
            self.stored[axis] = max(self.stored[axis], radius)
            coordinates.append(coordinate)
            radii.append(radius)
        self.count += 1
        return VERTEX.pack(*(coordinates+radii), label)

    def describe(self):
        return dict(projected_vertices=self.count,
            axes=["x", "y", "z"],
            maxima={key:dict(outward_binary64=[float_record(upward(v)) for v in values],
                            maximizing_vertex_addresses=self.addresses[key])
                    for key, values in self.values.items()},
            largest_stored_per_vertex_radii=[float_record(v) for v in self.stored],
            exact_maxima_identity=identity({key:list(map(str, values))
                                           for key, values in self.values.items()}),
            per_vertex_enclosure="exact_Q(display_coordinate) +/- exact_Q(stored_error_radius)",
            errors_cover_declared_field_point_enclosure_and_final_projection=True,
            solver_error_native_trajectory_error_or_normalization_error_included=False,
            triangle_interior_Hausdorff_C2_or_all_t_error_bound=False)


class Display:
    def __init__(self, spec, input_row=None):
        actions()
        require(spec.get("schema") == INPUT_SCHEMA and spec.get("repository") == REPOSITORY,
                "Use the independent R461 input contract")
        current_job(spec)
        self.spec = copy.deepcopy(spec)
        self.started = time.monotonic()
        self.namespace = contained(spec["namespace"], os.environ["RUNNER_TEMP"])
        self.out = contained(spec["out"], self.namespace, exists=False)
        require(not self.out.exists(), "Display owns only a fresh independent output directory")
        self.out.mkdir(parents=True, exist_ok=False)
        self.times = [exact(v) for v in spec.get("times", DEFAULT_TIMES)]
        require(1 <= len(self.times) <= 16 and len(set(self.times)) == len(self.times)
                and all(0 <= v <= 1 for v in self.times),
                "Supply distinct actual display times in the original closed interval")
        self.grid = dict(DEFAULT_GRID)
        supplied_grid = spec.get("grid", {})
        require(set(supplied_grid) <= set(self.grid), "Unknown display-grid field")
        self.grid.update(supplied_grid)
        for key, value in self.grid.items():
            integer(value, key, 3 if key == "angular_intervals" else 1)
        self.frame = spec.get("angular_frame", "physical-angle-image")
        require(self.frame in ("physical-angle-image", "first-material"),
                "Choose an explicit physical-image or actual first-material frame")
        precision = spec["precision"]
        self.bits = integer(precision["interval_bits"], "interval_bits", 16)
        self.sqrt_bits = integer(precision["sqrt_bits"], "sqrt_bits", 1)
        self.inverse_steps = integer(precision["max_inverse_steps"], "max_inverse_steps", 0)
        require(self.bits <= 4096 and self.sqrt_bits <= 4096 and self.inverse_steps <= 4096,
                "Keep an explicit finite display precision/work contract")
        budget = spec["budget"]
        self.seconds = positive(budget["seconds"], "display seconds")
        self.shutdown = positive(budget["shutdown_seconds"], "shutdown seconds")
        self.min_free = integer(budget["min_free_bytes"], "min_free_bytes", 0)
        self.deadline = None
        self.bound = False
        self.old_precision = None
        self.ctx = None
        self.current_stats = None
        self.report = dict(schema=SCHEMA, repository=REPOSITORY,
            run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
            source=receipt(__file__), input=input_row, input_value_identity=identity(spec),
            completed=False, completion_scope="finite display samples only",
            times=list(map(str, self.times)), angular_frame=self.frame,
            grid=copy.deepcopy(self.grid), precision=copy.deepcopy(precision),
            explicit_budget=copy.deepcopy(budget), original_absolute_clock_reset=False,
            frames=[], stage="binding", current_frame=None,
            resource_partial=False, external_interruption=False, error=None,
            pending=dict(time_indices_half_open=[0, len(self.times)], binding_not_complete=True),
            all_times_continuum_or_geometric_certificate=False,
            new_BVP_native_metric_reach_held_or_final_acceptance=False,
            published_or_uploaded_display_data=False,
            cleanup=dict(performed=False, authority="same-job host after necessary readback and quiet",
                         producer_deletes_no_inputs_or_outputs=True),
            lifecycle=dict(children_started=0, scientific_modules_not_imported_locally=True,
                           upstream_process_quiet_not_invented_by_this_consumer=True))

    def check(self):
        if time.monotonic()-self.started >= self.seconds:
            raise ResourceStop("Explicit display-work budget exhausted")
        if self.deadline is not None and time.time() >= self.deadline-self.shutdown:
            raise ResourceStop("Original job science deadline/shutdown reserve reached")
        st = os.statvfs(self.out)
        if st.f_bavail*st.f_frsize < self.min_free:
            raise ResourceStop("Actual owned display free-space reserve reached")

    def bind(self):
        self.check()
        s = self.spec
        origin_path = contained(s["origin_launch_directory"], self.namespace) / "result.json"
        origin, origin_id = read(origin_path, s["origin_launch_result_sha256"])
        current_job(origin)
        pair = ORIGINS.get(origin.get("schema"))
        require(pair is not None and origin.get("source_sha256") == pair[0],
                "Register the real original193, joint203 or actual202205 origin")
        deadline_path = contained(s["job_deadline"], self.namespace)
        deadline, deadline_id = read(deadline_path, s["job_deadline_sha256"])
        current_job(deadline)
        require(same_payload(deadline_id, origin.get("actual_job_deadline"))
                and deadline.get("schema") == pair[1]
                and deadline.get("recipe_sha256") == origin.get("recipe", {}).get("sha256")
                and deadline.get("science_seconds_from_namespace") == 18900
                and deadline.get("readback_reserve_seconds") == 2700,
                "Use the exact original origin-clock receipt, never a new start time")
        self.deadline = positive(deadline["namespace_created_unix_seconds"], "original start") + 18900
        self.report.update(actual_origin_launch=origin_id, actual_original_deadline=deadline_id,
            absolute_science_deadline_unix_seconds=self.deadline,
            original_readback_reserve_seconds=2700)
        self.check()
        family = FAMILIES[s["field_family"]]
        shared_dir = contained(s["shared_directory"], self.namespace)
        atlas_path = contained(s["atlas"], self.namespace)
        require(not self.out.is_relative_to(shared_dir) and not shared_dir.is_relative_to(self.out),
                "Display output must not overlap the current shared-field input tree")
        shared, shared_id = read(shared_dir/"result.json", s["shared_result_sha256"])
        current_job(shared)
        require(shared.get("completed") is True
                and shared.get("source", {}).get("sha256") == family["shared_sha"],
                "Use an actual complete same-job shared expression, not a prospective field")
        from flint import ctx
        self.ctx, self.old_precision = ctx, ctx.prec
        ctx.prec = self.bits
        Cut, cut_id = load_source(s["computations"], family["cut"], family["cut_sha"])
        Atlas, atlas_source = load_source(s["computations"], family["atlas"], family["atlas_sha"])
        Caps, caps_source = load_source(s["computations"], family["caps"], family["caps_sha"])
        Material, material_source = load_source(s["computations"], MATERIAL_NAME, MATERIAL_SHA)
        self.check()
        arguments = SimpleNamespace(computations=Path(s["computations"]), directory=shared_dir,
            result_sha256=s["shared_result_sha256"], sqrt_bits=self.sqrt_bits,
            interval_bits=self.bits, proof_directory=Path(s["proof_directory"]),
            checkpoint_directory=None if s.get("checkpoint_directory") is None else
                contained(s["checkpoint_directory"], self.namespace))
        self.current = Cut.load_accurate_cut_field(arguments)
        require(self.current.schema == family["schema"], "The actual accurate-field family differs")
        self.Active = self.current.Active
        active_id = receipt(self.Active.__file__)
        require(Path(active_id["file"]).name == ACTIVE_NAME and active_id["sha256"] == ACTIVE_SHA,
                "Retain the complete original six-jet interpreter")
        self.check()
        bundle = self.current.source_bundle
        paths, plan, assembly, target, saved, A, bindings = bundle
        current_job(saved.checkpoint.manifest)
        for path in paths.values():
            contained(path, self.namespace)
        normalization = saved.inlet_normalization
        require(normalization.get("exact_real_shared_node_inlet_reflection_C2") is True,
                "The original current shared normal-form definition must remain explicit")
        atlas, atlas_id = read(atlas_path, s["atlas_sha256"])
        attachment = Atlas.bind_loaded_shared_bundle(bundle, atlas)
        self.Caps, self.caps = Caps, Caps.bind_loaded_shared_bundle(
            bundle, atlas, attachment, s["computations"])
        if self.frame == "first-material":
            first = s["first_material"]
            material_path = contained(first["record"], self.namespace)
            first_plan = contained(first["plan"], self.namespace)
            first_assembly = contained(first["assembly"], self.namespace)
            self.material = Material.bind_loaded_common_material(self.current,
                first_material_transport=material_path,
                first_material_sha256=first["record_sha256"], first_plan=first_plan,
                first_assembly=first_assembly, budget_check=self.check)
            self.current_angle = self.material.current_angle
            first_identity = write(self.out/"first-material-binding.json", self.material.describe())
        else:
            require(not s.get("first_material"),
                    "Physical-image mode does not silently consume or fabricate a first-material record")
            self.material = None
            self.current_angle = Material.MaterialAngle(self.current.field.core,
                self.current.field.rho_lower, dict(actual_checkpoint=saved.checkpoint.receipt,
                    exact_core_coefficients=identity(list(map(str, self.current.field.core)))))
            first_identity = None
        self.current_field = self.current.field
        self.report.update(field_family=s["field_family"], actual_shared_result=shared_id,
            actual_current_checkpoint=copy.deepcopy(saved.checkpoint.receipt),
            actual_current_checkpoint_driver=copy.deepcopy(saved.checkpoint.manifest["actual_driver_source"]),
            accurate_target_identity=copy.deepcopy(self.current.target.binding["complete_target_identity"]),
            actual_atlas=atlas_id, actual_first_material_binding=first_identity,
            sources=dict(accurate_cut=cut_id, atlas=atlas_source, caps=caps_source,
                         material=material_source, complete_six_jet=active_id),
            current_field_modes=self.current_field.M,
            complete_original_active_piece_count=len(self.current.pieces),
            original_normalization_identity=identity(normalization),
            current_shared_normal_form_used=True, old_A_numeric_or_phase_jets_used=False,
            exact_cut_C_coefficients_never_projected_into_geometry=True,
            original_normalization_vs_parent_BVP_error_certified=False,
            fixed_cap_count=2, actual_marker_count=len(self.caps.markers),
            cap_definition="(x,y,side*(H+b_side(x,y))); all signed markers; no cap phase rotation",
            frame_scope=("same image under complete current-angle reparameterization; not fixed first-q vertices"
                         if self.material is None else "actual first-material q vertices through bound R457 inverse"))
        self.report["actual_field_binding"] = write(self.out/"accurate-field-binding.json", self.current.binding)
        self.report["actual_caps_binding"] = write(self.out/"caps-binding.json", self.caps.describe())
        self.report["actual_exact_cut_definition"] = write(self.out/"accurate-cut-definition.json", self.current.model.definition)
        self.bound = True
        self.check()

    def build_plan(self):
        f, g = self.current_field, self.grid
        # Bound requested allocations before constructing any range or ring.
        # At most two extra mandatory tail stations (inner, cut_start) occur.
        upper_ring_bound = g["prefix_intervals"]+g["tail_intervals"]+g["cap_intervals"]+3
        full_ring_bound = 2*upper_ring_bound-1
        vertex_bound = full_ring_bound*g["angular_intervals"]+2
        face_bound = 2*full_ring_bound*g["angular_intervals"]
        if VERTEX.size*vertex_bound+FACE.size*face_bound+4096 >= FILE_LIMIT:
            raise ResourceStop("The explicit worst-case display allocation exceeds the per-file capacity")
        prefix = [(index, piece) for index, piece in enumerate(self.current.pieces)
                  if piece["kind"] == "prefix"]
        tail = [(index, piece) for index, piece in enumerate(self.current.pieces)
                if piece["kind"] != "prefix"]
        def select(rows, radius):
            position = bisect_left([piece["right"] for _, piece in rows], radius)
            require(position < len(rows), "A planned point is outside the actual piece list")
            index, piece = rows[position]
            require(piece["left"] <= radius <= piece["right"], "The actual closed piece does not contain the point")
            return index
        rings = []
        for i in range(g["prefix_intervals"]+1):
            radius = f.x[-1]*Q(i, g["prefix_intervals"])
            rings.append(dict(kind="prefix", radius=radius, piece_index=select(prefix, radius)))
        radii = {f.cuff+(f.cut-f.cuff)*Q(i, g["tail_intervals"])
                 for i in range(g["tail_intervals"]+1)}
        radii.update((f.inner, f.cut_start, f.cut, f.cuff))
        for radius in sorted(radii, reverse=True):
            if radius == f.cut:
                continue  # exact common-cut value is represented by the prefix endpoint
            rings.append(dict(kind="cap" if radius == f.cuff else "tail", radius=radius,
                              piece_index=None if radius == f.cuff else select(tail, radius)))
        for i in range(g["cap_intervals"]-1, 0, -1):
            rings.append(dict(kind="cap", radius=f.cuff*Q(i, g["cap_intervals"]), piece_index=None))
        self.rings, self.N = rings, g["angular_intervals"]
        self.R = 2*len(rings)-1
        self.V, self.F = self.R*self.N+2, 2*self.R*self.N
        require(self.V < 2**31, "Display face indices require signed int32 representation")
        upper_size = VERTEX.size*self.V+FACE.size*self.F+4096
        if upper_size >= FILE_LIMIT:
            raise ResourceStop("The explicit display grid exceeds the strict uncompressed per-file capacity")
        self.plan = dict(schema=SCHEMA+"-display-plan", angular_intervals=self.N,
            angular_points=[str(Q(j,self.N)) for j in range(self.N)],
            upper_rings=[dict(row, radius=str(row["radius"])) for row in rings],
            full_ring_order="lower upper-ring indices U-1..1, then upper indices 0..U-1",
            poles_after_all_rings=["lower", "upper"],
            ring_count=self.R, vertices=self.V, faces=self.F,
            vertex_bytes=VERTEX.size, face_bytes=FACE.size,
            uncompressed_bytes_upper=upper_size, strict_per_file_bytes_limit=FILE_LIMIT,
            complete_original_piece_list_identity=identity([
                {k:str(v) if isinstance(v,Q) else v for k,v in p.items()} for p in self.current.pieces]),
            display_evaluated_piece_indices=sorted({r["piece_index"] for r in rings if r["piece_index"] is not None}),
            all_original_pieces_remain_in_defining_field=True,
            all_pieces_sampled_or_continuum_covered_by_display=False,
            selected_cut_value="prefix endpoint of actual accurate common cut",
            selected_cuff_value="same-source fixed cap graph on exact original cuff",
            shared_equator="actual current shared normalize_inlet normal form; no new projection",
            combinatorial_ring_faces_are_format_only=True,
            topology_or_face_area_used_as_acceptance_gate=False)
        self.report["actual_display_plan"] = write(self.out/"display-plan.json", self.plan)
        self.report.update(planned_vertices_per_time=self.V, planned_faces_per_time=self.F,
                           actual_display_piece_count=len(self.plan["display_evaluated_piece_indices"]))

    def cap_point(self, radius, eta, upper):
        A = self.Active
        if radius == 0:
            box = ((Q(0),Q(0)), (Q(0),Q(0)))
        else:
            box = (A.bounds(A.ball(radius)*eta.cos()), A.bounds(A.ball(radius)*eta.sin()))
        markers = [row for row in self.caps.markers if row["upper"] is upper]
        graph = self.Caps.graph_six_jets(box, markers)
        value = self.Caps.geometric_six_jets(box, self.caps.height, 1 if upper else -1, graph)["value"]
        return tuple((Q(v["lower"]),Q(v["upper"])) for v in value)

    def active_point(self, row, inverse, cosine, sine):
        A = self.Active
        piece = self.current.pieces[row["piece_index"]]
        # R447 uses this full real lift too.  The convenience current.evaluate
        # wrapper restricts q to [0,1], so it must not discard a periodic lift.
        values = self.current_field.evaluate(piece, (row["radius"],row["radius"]),
                                            A.bounds(inverse), False)
        x,y,z = (v.d[0] for v in values)
        return (A.bounds(cosine*x-sine*y), A.bounds(sine*x+cosine*y), A.bounds(z))

    def render(self, index):
        A, t, N = self.Active, self.times[index], self.N
        self.report["stage"] = "display-frame"
        row = dict(index=index, time=str(t), completed=False, stage="angle-inclusions",
            angle_inclusions_completed=0, planned_angle_inclusions=N,
            ring_pairs_completed=0, planned_ring_pairs=len(self.rings)*N,
            poles_completed=0, active_interpreter_calls=0, cap_graph_calls=0,
            inverse_maximum_iterations=0, inverse_stop_counts={},
            inverse_enclosure_width_upper=None, files={}, error=None)
        self.report["current_frame"] = row
        stats = VertexErrors()
        self.current_stats = stats
        alpha = A.arb.pi()*A.ball(t)/2
        cosine, sine = alpha.cos(), alpha.sin()
        etas, inverses, widths = [], [], []
        for j in range(N):
            self.check()
            q = A.ball(Q(j,N))
            eta = 2*A.arb.pi()*q if self.material is None else self.material.first_angle.derivatives(A,q,0)[0]
            inverse, actual = self.current_angle.inverse_enclosure(A, eta-alpha,
                                                                 self.inverse_steps, self.check)
            etas.append(eta); inverses.append(inverse)
            lo,hi = A.bounds(inverse)
            widths.append(hi-lo)
            row["inverse_maximum_iterations"] = max(row["inverse_maximum_iterations"], actual["finite_inclusion_iterations"])
            key = actual["stop"]
            row["inverse_stop_counts"][key] = row["inverse_stop_counts"].get(key,0)+1
            row["angle_inclusions_completed"] = j+1
            row["inverse_enclosure_width_upper"] = float_record(upward(max(widths)))
        upper, lower = [], []
        row["stage"] = "point-enclosures-and-projections"
        for i, ring in enumerate(self.rings):
            ur, lr = [], []
            for j in range(N):
                self.check()
                address = dict(time_index=index, upper_ring_index=i, angular_index=j)
                if ring["kind"] == "cap":
                    up = self.cap_point(ring["radius"], etas[j], True)
                    down = self.cap_point(ring["radius"], etas[j], False)
                    row["cap_graph_calls"] += 2
                    ul, ll = 2, 3
                else:
                    up = self.active_point(ring, inverses[j], cosine, sine)
                    down = (up[0],up[1],(-up[2][1],-up[2][0]))
                    row["active_interpreter_calls"] += 1
                    ul = ll = 0 if ring["kind"] == "prefix" else 1
                ur.append(stats.vertex(up,ul,dict(address,side="upper")))
                if i:
                    lr.append(stats.vertex(down,ll,dict(address,side="lower")))
                row["ring_pairs_completed"] = i*N+j+1
            upper.append(b"".join(ur)); lower.append(b"".join(lr))
        poles = []
        row["stage"] = "pole-enclosures-and-projections"
        for is_upper in (False,True):
            self.check()
            boxes = self.cap_point(Q(0),A.arb(0),is_upper)
            row["cap_graph_calls"] += 1
            poles.append(stats.vertex(boxes,2 if is_upper else 3,
                         dict(time_index=index,pole="upper" if is_upper else "lower")))
            row["poles_completed"] += 1
        row["vertex_errors"] = stats.describe()
        row["stage"] = "bounded-ply-write"
        name = "display-%03d" % index
        raw_path = self.out/(name+".ply")
        header = ("ply\nformat binary_little_endian 1.0\n"
            "comment R461 finite samples of current accurate field; not a geometric certificate\n"
            "comment error_x/y/z enclose declared-expression point plus final coordinate projection\n"
            "element vertex %d\nproperty double x\nproperty double y\nproperty double z\n"
            "property double error_x\nproperty double error_y\nproperty double error_z\n"
            "property uchar piece\nelement face %d\nproperty list uchar int vertex_indices\nend_header\n" % (self.V,self.F)).encode("ascii")
        expected = len(header)+VERTEX.size*self.V+FACE.size*self.F
        if expected >= FILE_LIMIT:
            raise ResourceStop("The actual uncompressed PLY exceeds the strict per-file capacity")
        with raw_path.open("xb") as stream:
            stream.write(header)
            for raw in list(reversed(lower[1:]))+upper+poles:
                self.check();stream.write(raw)
            for i in range(self.R-1):
                self.check()
                for j in range(N):
                    a,b,c,d = i*N+j,i*N+(j+1)%N,(i+1)*N+j,(i+1)*N+(j+1)%N
                    stream.write(FACE.pack(3,a,b,c));stream.write(FACE.pack(3,b,d,c))
            for j in range(N):
                stream.write(FACE.pack(3,self.R*N,(j+1)%N,j))
                stream.write(FACE.pack(3,self.R*N+1,(self.R-1)*N+j,(self.R-1)*N+(j+1)%N))
            stream.flush();os.fsync(stream.fileno())
        raw_id = receipt(raw_path)
        require(raw_id["bytes"] == expected, "The original declared PLY layout was not completely written")
        row["files"]["uncompressed"] = raw_id
        row["stage"] = "bounded-gzip-write"
        compressed_path = self.out/(name+".ply.gz")
        with raw_path.open("rb") as source, compressed_path.open("xb") as output:
            with gzip.GzipFile(filename="",mode="wb",fileobj=LimitedWriter(output),mtime=0,compresslevel=6) as compressed:
                while True:
                    self.check()
                    block = source.read(65536)
                    if not block:
                        break
                    compressed.write(block)
            output.flush();os.fsync(output.fileno())
        compressed_id = receipt(compressed_path)
        if compressed_id["bytes"] >= FILE_LIMIT:
            raise ResourceStop("The actual gzip file exceeds its strict per-file capacity")
        row["files"]["gzip"] = compressed_id
        row.update(completed=True,stage="complete",vertices=self.V,faces=self.F,
            all_stored_vertex_error_radii_outward=True,
            finite_inverse_inclusion_is_not_an_exact_midpoint_inverse=True,
            every_defining_mode_retained_at_sampled_points=True,
            all_spatial_cells_or_times_evaluated=False,
            polygonal_face_interiors_or_topological_embedding_certified=False)
        self.report["frames"].append(copy.deepcopy(row))
        self.report["current_frame"] = None
        self.current_stats = None

    def finish_pending(self):
        completed = len(self.report["frames"])
        current = self.report["current_frame"]
        if current is not None:
            current["vertex_error_statistics_initialized"] = self.current_stats is not None
            current["vertex_errors"] = (None if self.current_stats is None
                                        else self.current_stats.describe())
            current["pending"] = dict(
                angle_index_suffix=[current["angle_inclusions_completed"],current["planned_angle_inclusions"]],
                upper_ring_major_pair_suffix=[current["ring_pairs_completed"],current["planned_ring_pairs"]],
                pole_suffix=[current["poles_completed"],2],
                file_writes_complete=current["completed"], actual_stage=current["stage"],
                addresses_defined_by_actual_display_plan=True)
        self.report["pending"] = None if self.report["completed"] else dict(
            first_not_complete_time_index=completed,
            unstarted_time_index_suffix=[completed+(1 if current is not None else 0),len(self.times)],
            current_frame_present=current is not None, binding_completed=self.bound,
            all_unvisited_continuous_space_time_is_outside_display_scope=True)

    def run(self):
        previous_handlers = {}
        def interrupt(number, frame):
            raise ExternalStop("Actual external signal " + str(number))
        try:
            for number in (signal.SIGTERM,signal.SIGINT):
                previous_handlers[number] = signal.getsignal(number)
                signal.signal(number,interrupt)
            self.bind()
            self.report["stage"] = "display-plan"
            self.build_plan()
            self.current_stats = None
            for index in range(len(self.times)):
                self.check()
                self.render(index)
            self.report.update(completed=True,stage="complete")
        except BaseException as exc:
            self.report.update(resource_partial=isinstance(exc,ResourceStop),
                external_interruption=isinstance(exc,ExternalStop),
                error=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc()))
            if self.report["current_frame"] is not None:
                self.report["current_frame"]["error"] = copy.deepcopy(self.report["error"])
        finally:
            if self.ctx is not None and self.old_precision is not None:
                self.ctx.prec = self.old_precision
            for number, handler in previous_handlers.items():
                signal.signal(number,handler)
        self.finish_pending()
        self.report["elapsed_seconds"] = time.monotonic()-self.started
        self.report["remaining_original_science_seconds"] = None if self.deadline is None else max(0.0,self.deadline-time.time())
        self.report["owned_files"] = [receipt(p) for p in sorted(self.out.iterdir()) if p.is_file()]
        self.report["owned_files_below_strict_limit"] = all(r["bytes"] < FILE_LIMIT for r in self.report["owned_files"])
        result_id = write(self.out/"result.json",self.report)
        necessary = dict(self.report, original_result=result_id,
            readback_scope="all finite display statuses and per-file componentwise error maxima; per-vertex radii in temporary PLY only",
            raw_display_or_large_field_data_in_log=False,
            host_must_wait_for_actual_consumer_exit_before_retiring_raw=True)
        raw = canonical(necessary)
        if len(raw) > SUMMARY_LIMIT:
            print(json.dumps(dict(schema=SCHEMA+"-necessary-over-budget",original_result=result_id,
                attempted_bytes=len(raw),attempted_sha256=sha(raw),complete_necessary_readback=False,
                temporary_outputs_not_deleted=True),sort_keys=True),flush=True)
            return self.report,70
        summary_id = write(self.out/"necessary-summary.json",necessary)
        print("BEGIN_R461_CURRENT_MULTITIME_DISPLAY_NECESSARY",flush=True)
        print(raw.decode("ascii"),end="",flush=True)
        print("END_R461_CURRENT_MULTITIME_DISPLAY_NECESSARY",flush=True)
        print(json.dumps(dict(event="R461-necessary-summary-identity",summary=summary_id),sort_keys=True),flush=True)
        write(self.out/"necessary-readback-complete.json",dict(schema=SCHEMA+"-necessary-complete",
            summary=summary_id, original_result=result_id, producer_source=receipt(__file__),
            original_clock_reset=False, display_completed=self.report["completed"],
            raw_cleanup_performed=False, host_still_responsible_for_actual_process_quiet=True))
        return self.report,(0 if self.report["completed"] else 124 if self.report["resource_partial"] else 2)


def produce(spec, *, input_receipt=None):
    """Called only by a real owned same-job host; no process or cleanup here."""
    return Display(spec,input_receipt).run()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input",type=Path,required=True)
    parser.add_argument("--input-sha256",required=True)
    args = parser.parse_args(argv)
    actions()
    value,row = read(args.input,args.input_sha256)
    _,code = produce(value,input_receipt=row)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
