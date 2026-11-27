#!/usr/bin/env python3
"""Strict actual-run10 input for accurate normal-chain/physical-sixjet work.

This module reads complete existing reports, immutable root packets, every
selected-point angle and every original stage. It never fabricates missing
roots or upgrades a recorded angular order. It unpacks the entire actual
current free point on the unchanged M160/J923 layout; it does not run the
working normal solver or replay a physical field.

Scientific scalar/context and array reads are Actions-only. This complete
input is not itself an accurate root, quadrature or geometry certificate.
"""
from __future__ import annotations

import ast
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys

SCHEMA = "actual-run10-complete-normal-packet-accurate-field-input-v1"
TOPIC = "topics/visible-flex-larger-amplitude"
SCRIPT_DIRECTORY = "scripts/resume_20261126"
PINS = {
    "reader": ("read_run10_detached_closure_so3_report.py",
        "2efa4b1d7df920fb616b51988bc29730aa18b29ba57dc0a943d36cdcf87b3e8e"),
    "driver": ("fullclosed_run10_detached_closure_so3_qp.py",
        "c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1"),
    "packets": ("immutable_closure_values_normal_root_packets.py",
        "31f66203897cde00ca537f500209296ce2e42605f06a3cbbb1221e502e298805"),
    "normal": ("so3_reference_centred_closure_values_normal_lift_operator.py",
        "6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4"),
    "base": ("so3_supported_smooth_triangle_meridian_operator.py",
        "6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865"),
    "reference": ("so3_axisymmetric_reference.py",
        "4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3"),
    "continuous": ("so3_axisymmetric_continuous_integrand.py",
        "a846d373421df655da3bbba2491847b0cd016ae6db09b5d4176be227b2bc9ce6"),
    "reference_fees": ("run10_reference_seed_angular_profile_error_bounds.py",
        "91fd1fb0148c7dde3260bdcfed61b057033d308517960bdb86454cc1e96ab3a1"),
    "mean_integrals": ("run10_reference_accurate_mean_residuals.py",
        "19fd82f3d746cce4b7de474f42aeb4192e4e1cec8e38c375148bcd4a9ab51a38"),
}
ACTUAL_TARGET = "e7110482f9bd2eb723e96c99f5bbaa8a85aa11a81519c5204a296fb1bad9a049"
ACTUAL_REFERENCE = "081bdf939b7bdc6d5dfb54bce955fdfbcda90a8cef3668388a8874272e594af5"
ACTUAL_CHART = "90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e"
NORMAL_SCHEMA = "complete-R711-reference-centred-detached-closure-values-analytic-frame-J3-normal-layer-v1"
BASE_SCHEMA = "complete-supported-smooth-triangle-reference-so3-meridian-with-core-lift-v1"


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Actual accurate-field input reads require the public Actions")


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
        allow_nan=False).encode()).hexdigest()


def copy_json(value):
    return json.loads(json.dumps(value, allow_nan=False))


def file_record(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path), bytes=path.stat().st_size)


def valid_digest(value):
    return (isinstance(value, str) and len(value) == 64
        and all(c in "0123456789abcdef" for c in value))


def array_sha(value):
    import numpy as np
    value = np.ascontiguousarray(value)
    h = hashlib.sha256(str(value.dtype).encode())
    h.update(json.dumps(list(value.shape)).encode())
    h.update(value.tobytes())
    return h.hexdigest()


def load(name, path, digest):
    if sha(path) != digest:
        raise ValueError("The complete bound source differs: "+str(path))
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    if sha(module.__file__) != digest or sha(path) != digest:
        raise ValueError("A complete module changed during source loading")
    return module


def load_source_pins(path):
    tree = ast.parse(Path(path).read_text())
    matches = [node.value for node in tree.body if isinstance(node, ast.Assign)
        and any(isinstance(target, ast.Name) and target.id == "SOURCE_PINS"
                for target in node.targets)]
    if len(matches) != 1:
        raise ValueError("The actual driver must retain its single complete source registry")
    return ast.literal_eval(matches[0])


class ActualDataUnavailable(Exception):
    """An actual completed input is absent; no scientific value was supplied."""


class VerifiedFiles:
    def __init__(self):
        self.used = {}

    def verify(self, record):
        if (not isinstance(record, dict) or not isinstance(record.get("path"), str)
                or not valid_digest(record.get("sha256")) or type(record.get("bytes")) is not int
                or record["bytes"] < 0):
            raise ValueError("Keep a complete path, byte count and whole-file identity")
        path = Path(record["path"]).resolve()
        normalized = dict(path=str(path), bytes=record["bytes"], sha256=record["sha256"])
        old = self.used.get(str(path))
        if old is not None and old != normalized:
            raise ValueError("One physical input path was declared with incompatible whole identities")
        actual = file_record(path)
        if actual != normalized:
            raise ValueError("Changed complete actual input: "+str(path))
        self.used[str(path)] = normalized
        return path

    def add(self, path):
        record = file_record(path)
        self.verify(record)
        return record

    def json(self, record):
        path = self.verify(record)
        content = path.read_bytes()
        if len(content) != record["bytes"] or hashlib.sha256(content).hexdigest() != record["sha256"]:
            raise ValueError("The actual JSON snapshot changed during its read")
        result = json.loads(content)
        self.verify(record)
        return result

    def recheck(self):
        for record in tuple(self.used.values()):
            self.verify(record)

    def protect_output(self, directory):
        out = Path(directory).resolve()
        for record in self.used.values():
            source = Path(record["path"])
            if out == source or out in source.parents:
                raise ValueError("Output may not contain or replace any complete consumed source or input")
        return out


class ActualNormalPacketPoint:
    """One genuinely recorded complete point and all its actual angular packets."""

    def __init__(self, args):
        require_actions()
        import numpy as np
        self.np = np
        self.repo = Path(args.repo).resolve()
        self.topic = self.repo/TOPIC
        self.used = VerifiedFiles()
        self.used.add(__file__)
        self.paths = {role: self.topic/SCRIPT_DIRECTORY/name
                      for role, (name, _) in PINS.items()}
        for role, (_, digest) in PINS.items():
            record = self.used.add(self.paths[role])
            if record["sha256"] != digest:
                raise ValueError("The complete source-specific accurate-input role changed: "+role)
        self.reader = load("_normal_fee_run10_reader", self.paths["reader"], PINS["reader"][1])
        self.packet_module = load("_normal_fee_actual_packets", self.paths["packets"], PINS["packets"][1])
        self.reference_module = load("_normal_fee_actual_reference", self.paths["reference"], PINS["reference"][1])
        self.continuous_module = load("_normal_fee_exact_scalar", self.paths["continuous"], PINS["continuous"][1])
        self.seed_fees = load("_normal_fee_reference_math", self.paths["reference_fees"], PINS["reference_fees"][1])
        self.report_record = self.used.add(args.report)
        expected_report = getattr(args, "report_sha256", None)
        if expected_report is not None and expected_report != self.report_record["sha256"]:
            raise ValueError("The requested immutable actual report identity differs")
        self.report = raw = self.used.json(self.report_record)
        self.pure = pure = self.reader.read_report(self.repo, self.report_record["path"],
                                                  verify_final_bundle=False)
        if (pure.get("report_sha256") != self.report_record["sha256"]
                or raw.get("source_sha256") != PINS["driver"][1]
                or pure.get("actual_driver_sha256") != PINS["driver"][1]):
            raise ValueError("The actual complete reader and scientific report differ")
        roles = load_source_pins(self.paths["driver"])
        if len(roles) != 75 or raw.get("source_sha256_by_role") != {k: v[1] for k, v in roles.items()}:
            raise ValueError("Retain every actual complete scientific source role")
        self.runtime_source_records = {}
        for role, (relative, digest) in roles.items():
            record = self.used.add(self.topic/relative)
            if record["sha256"] != digest:
                raise ValueError("Changed full scientific role: "+role)
            self.runtime_source_records[role] = record
        self.model = copy_json(raw["representation"])
        self.model_identity = canonical(self.model)
        self.base_model = self.model["base_complete_model"]
        self.reference_model = self.base_model["complete_axisymmetric_reference_model"]
        self.seed = copy_json(raw["supported_unit_seed_definition"])
        self.seed_identity = canonical(self.seed)
        if (self.model_identity != raw["model_identity_sha256"]
                or self.model.get("schema") != NORMAL_SCHEMA
                or self.model.get("source_sha256") != PINS["normal"][1]
                or self.base_model.get("schema") != BASE_SCHEMA
                or self.base_model.get("source_sha256") != PINS["base"][1]
                or canonical(self.base_model) != self.model.get("base_model_identity_sha256")
                or canonical(self.reference_model) != ACTUAL_REFERENCE
                or self.reference_model.get("fixed_chart_core_sha256") != ACTUAL_CHART
                or self.seed_identity != raw.get("supported_unit_seed_identity_sha256")
                or self.base_model.get("fixed_supported_unit_seed_model") != self.seed
                or raw.get("independent_fixed_target_definition_identity_sha256") != ACTUAL_TARGET):
            raise ValueError("Bind the complete same-point normal/base/frozen-reference/target chain")
        if (raw.get("M") != 160 or raw.get("J") != 923 or raw.get("N") != 2048
                or self.model.get("implicit_control_dimension") != 6
                or self.model.get("normal_increment_dimension") != 3
                or self.model.get("normal_stage_count") != 32):
            raise ValueError("This actual producer retains the complete original run10 layout and 32 stages")
        self.partition = [F(v) for v in self.model["exact_normal_step_nodes"]]
        if (len(self.partition) != 33 or self.partition[0] != 0 or self.partition[-1] != 1
                or any(a >= b for a, b in zip(self.partition, self.partition[1:]))):
            raise ValueError("The exact complete common normal partition changed")
        self.packet_module.validate_entry_report(raw, reread_packets=True, reread_arrays=True)
        metadata = raw["normal_root_packets"]
        snapshots = metadata["snapshots"]
        selected_identity = getattr(args, "snapshot_identity_sha256", None)
        if selected_identity is not None:
            matches = [item for item in snapshots if item["snapshot_identity_sha256"] == selected_identity]
            if len(matches) != 1:
                raise ActualDataUnavailable("The explicitly requested actual immutable snapshot is absent")
            selected = matches[0]
        else:
            complete = [item for item in snapshots
                if item["summary"].get("all_required_angle_roots_recorded") is True
                and item["summary"].get("current_full_point_sha256") is not None]
            if not complete:
                raise ActualDataUnavailable("No actual point has all required complete normal angle roots")
            selected = complete[-1]
        self.snapshot_record = copy_json(selected["snapshot_file"])
        self.snapshot = self.used.json(self.snapshot_record)
        summary = self.packet_module.validate_snapshot(self.snapshot, model=self.model,
            operator_source_sha256=PINS["normal"][1], caller_source_sha256=PINS["driver"][1],
            reread_packets=True, reread_arrays=True)
        if summary != selected["summary"]:
            raise ValueError("The complete selected immutable snapshot changed")
        d = self.snapshot["definition"]
        if d.get("all_required_angle_roots_recorded") is not True:
            raise ActualDataUnavailable("The selected actual point lacks original required angle roots")
        self.point_sha256 = d["current_full_point_sha256"]
        self.required_angles = tuple(d["required_literal_angle_hex"])
        self.angles = tuple(d["cache_literal_angle_hex"])
        self.angle_records = {item["literal_angle_hex"]: copy_json(item) for item in d["angle_packets"]}
        if (len(self.angle_records) != len(self.angles)
                or not set(self.required_angles) <= set(self.angles)):
            raise ValueError("No original actual required or cached angle may be dropped")
        self.point_record = copy_json(d["current_point_file"])
        self.x = self._read_npz(self.point_record["arrays_file"],
                               [self.point_record["array"]])["x"]
        if array_sha(self.x) != self.point_sha256:
            raise ValueError("The full selected current free-point words differ")
        self.carrier_record = copy_json(metadata["fixed_working_carrier"])
        self.carrier = self._read_npz(self.carrier_record["arrays_file"],
                                     self.carrier_record["arrays"])
        self.operator_metadata_record = copy_json(d["operator_metadata_snapshot"])
        self.operator_metadata = self.used.json(self.operator_metadata_record)
        self.calibration_records = copy_json(d["actual_reference_calibration_files"])
        for record in self.calibration_records:
            self.used.verify(record["immutable_copy"])
        current = pure["actual_public_reference_input_binding"]
        if (current.get("actual_fixed_target_definition_identity_sha256") != ACTUAL_TARGET
                or current.get("actual_reference_model_identity_sha256") != ACTUAL_REFERENCE
                or current.get("actual_fixed_chart_core_sha256") != ACTUAL_CHART):
            raise ValueError("The actual six-file public-input contract differs")
        self.input_records = copy_json(current["complete_current_input_files"])
        for record in self.input_records.values():
            self.used.verify(record)
        self.used.verify(current["actual_binding_file"])
        keys = dict(reference_bundle="current_reference_bundle", carrier="current_carrier",
            node_report="current_node_report", scalar_input="current_scalar_input",
            preparation_report="current_preparation_report")
        context_args = {k: self.input_records[v]["path"] for k, v in keys.items()}
        if type(args.panels) is not int or args.panels < 1:
            raise ValueError("Use an explicit positive complete scalar enclosure panel count")
        self.context = self.reference_module.AxisymmetricReferenceContext.from_files(
            repo=self.repo, panels=args.panels, **context_args)
        if (self.context.model != self.reference_model or self.context.identity != ACTUAL_REFERENCE
                or self.context.scalar_definition != self.base_model["fixed_scalar_profile_definition"]
                or self.context.scalar_identity != self.base_model["fixed_scalar_metric_identity_sha256"]):
            raise ValueError("The whole accurate scalar/chart context changed the actual frozen target")
        self.M, self.J, self.n, self.K = 160, 923, 482, 3
        free_rows = np.array([i for i in range(3*self.J)
            if i not in (0, 3*(self.J-1), 3*(self.J-1)+1)], dtype=np.int64)
        core_count = self.M-self.K
        expected_size = core_count+len(free_rows)*self.n+1
        if (self.x.shape != (expected_size,) or raw.get("original_variables") != expected_size
                or self.x.dtype != np.dtype("float64") or not np.isfinite(self.x).all()):
            raise ValueError("Use the complete actual full current point on the unchanged source layout")
        # Exact literal unpack of the complete bound base's public layout.
        self.core = np.concatenate((self.context.core[:3], self.x[:core_count]))
        omega = np.zeros((3*self.J, self.n), dtype=np.float64)
        omega[free_rows] = self.x[core_count:-1].reshape(len(free_rows), self.n)
        self.omega = omega.reshape(self.J, 3, self.n)
        self.height = float(self.x[-1])
        self.initial_point = np.concatenate((self.context.core[3:],
            np.zeros(len(free_rows)*self.n, dtype=np.float64),
            np.array([float.fromhex(self.seed["initial_height_hex"])], dtype=np.float64)))
        self.reference_point_sha256 = array_sha(self.initial_point)
        if self.reference_point_sha256 != self.model["reference_centering_definition"]["original_reference_point_sha256"]:
            raise ValueError("The entire frozen original point was not recovered exactly")
        for array in (self.x, self.core, self.omega, self.initial_point):
            array.setflags(write=False)
        self.scalar = self.continuous_module.ScalarWholeInterval(self)
        self.seed_rows, self.seed_row_sources = self._read_complete_seed_candidates(pure)
        if any(angle not in self.seed_rows for angle in self.angles):
            raise ActualDataUnavailable("A recorded normal angle lacks a genuinely returned fixed-reference mean candidate")
        self._packet_cache = {}
        self.binding = dict(schema=SCHEMA, source_sha256=sha(__file__),
            scientific_report=self.report_record, complete_pure_reader_sha256=PINS["reader"][1],
            actual_driver_sha256=PINS["driver"][1], actual_source_commit=raw["source_commit"],
            actual_run_id=raw.get("github_run_id"), model_identity_sha256=self.model_identity,
            complete_model=self.model, exact_fixed_target_identity_sha256=ACTUAL_TARGET,
            actual_reference_model_identity_sha256=ACTUAL_REFERENCE,
            fixed_scalar_metric_identity_sha256=self.context.scalar_identity,
            actual_snapshot_identity_sha256=self.snapshot["snapshot_identity_sha256"],
            actual_snapshot_file=self.snapshot_record, current_full_point_sha256=self.point_sha256,
            current_point_arrays_file=self.point_record["arrays_file"],
            exact_common_normal_partition=[str(v) for v in self.partition],
            full_stage_count=32, complete_required_literal_angles=list(self.required_angles),
            complete_cached_literal_angles=list(self.angles),
            all_cached_angles_retained=True, current_point_is_original_reference=bool(np.array_equal(self.x,self.initial_point)),
            actual_original_reference_point_sha256=self.reference_point_sha256,
            actual_packet_matrix_orders_are_not_upgraded=True,
            existing_calibration_files=self.calibration_records,
            complete_actual_working_carrier=self.carrier_record,
            complete_six_actual_inputs=self.input_records,
            original_current_core_sha256=array_sha(self.core),
            original_current_omega_sha256=array_sha(self.omega),
            original_current_H_hex=self.height.hex(),
            complete_actual_seed_candidate_sources=self.seed_row_sources,
            source_sha256_by_role={role: value[1] for role,value in PINS.items()},
            full_scientific_runtime_source_records=self.runtime_source_records,
            no_new_working_field_J_or_normal_root_evaluation=True,
            accurate_scalar_context_may_be_evaluated=True,
            accepted_outer_point_not_inferred_from_cache=True,
            literal_node_coverage_is_not_whole_angle_coverage=True,
            reference_root_or_normal_root_or_physical_sixjet_fee_paid_here=False)
        self.identity = canonical(self.binding)
        self.used.recheck()

    def _read_npz(self, record, descriptors):
        require_actions()
        np = self.np
        path = self.used.verify(record)
        expected = {d["name"]: d for d in descriptors}
        if len(expected) != len(descriptors):
            raise ValueError("Duplicate immutable array name")
        self.packet_module.validate_arrays_file(record, descriptors)
        with np.load(path, allow_pickle=False) as data:
            if set(data.files) != set(expected):
                raise ValueError("Keep every complete declared immutable array, without extras")
            result = {}
            for name, d in expected.items():
                a = np.array(data[name], copy=True)
                if (list(a.shape) != d["shape"] or str(a.dtype) != d["dtype"]
                        or array_sha(a) != d["array_sha256"]
                        or (a.dtype.kind == "f" and not np.isfinite(a).all())):
                    raise ValueError("An immutable actual array changed: "+name)
                a.setflags(write=False)
                result[name] = a
        self.used.verify(record)
        return result

    def _read_complete_seed_candidates(self, pure):
        require_actions()
        np = self.np
        latest = self.report.get("latest_operator_metadata", {})
        seed_meta = latest.get("base_complete_metadata", {}).get("fixed_supported_unit_seed")
        if not isinstance(seed_meta, dict) or pure.get("seed_diagnostics") is None:
            raise ActualDataUnavailable("No actual completed fixed-reference mean batches exist")
        records = seed_meta.get("mean_batch_records")
        if records != pure["seed_diagnostics"].get("mean_batch_records"):
            raise ValueError("The complete pure and actual fixed-reference batch lists differ")
        rows, provenance = {}, []
        vector_keys = self.seed_fees.MEAN_VECTOR_KEYS
        scalar_keys = self.seed_fees.MEAN_SCALAR_KEYS
        for index, batch in enumerate(records):
            record = batch["runner_raw_arrays"]
            path = self.used.verify(record)
            angles = batch["literal_angle_hex"]
            with np.load(path, allow_pickle=False) as data:
                if (str(data["seed_model_identity"].item()) != self.seed_identity
                        or [float(v).hex() for v in data["phi"]] != angles):
                    raise ValueError("An actual complete mean batch changed seed or angle order")
                arrays = {}
                for name in vector_keys+scalar_keys:
                    a = np.array(data[name], copy=True)
                    expected = (len(angles), 3) if name in vector_keys else (len(angles),)
                    if (a.shape != expected or a.dtype.kind != "f" or a.dtype.itemsize != 8
                            or not np.isfinite(a).all()):
                        raise ValueError("A full actual fixed-reference candidate array is missing")
                    arrays[name] = a
            self.used.verify(record)
            source = dict(actual_completed_batch_index=index, runner_raw_arrays=copy_json(record),
                literal_angle_hex=list(angles), complete_original_batch_metadata=copy_json(batch))
            provenance.append(source)
            for i, angle in enumerate(angles):
                if angle in rows:
                    raise ValueError("The original fixed-reference provider records each missing literal angle once")
                candidate = dict(literal_phi_hex=angle)
                for name in vector_keys:
                    candidate[name] = [float(v).hex() for v in arrays[name][i]]
                for name in scalar_keys:
                    candidate[name] = float(arrays[name][i]).hex()
                candidate["actual_completed_batch_index"] = index
                candidate["actual_raw_batch_sha256"] = record["sha256"]
                rows[angle] = candidate
        return rows, provenance

    def packet(self, angle):
        require_actions()
        if angle not in self.angle_records:
            raise ValueError("Use an actually recorded literal angle; do not synthesize a root")
        if angle in self._packet_cache:
            return self._packet_cache[angle]
        item = self.angle_records[angle]
        packet = self.used.json(item["packet_file"])
        summary = self.packet_module.validate_packet(packet, model=self.model,
            operator_source_sha256=PINS["normal"][1], caller_source_sha256=PINS["driver"][1],
            point_sha256=self.point_sha256, angle_hex=angle, reread_arrays=True)
        if summary["packet_identity_sha256"] != item["packet_identity_sha256"]:
            raise ValueError("The actual angle packet changed after snapshot binding")
        arrays = self._read_npz(packet["arrays_file"], packet["definition"]["arrays"])
        result = dict(packet=packet, arrays=arrays, actual_summary=summary,
            original_packet_file=copy_json(item["packet_file"]))
        self._packet_cache[angle] = result
        return result

    def recheck(self):
        self.used.recheck()
        if self.point_sha256 != array_sha(self.x):
            raise ValueError("The selected entire current point was modified")
        return True

    def metadata(self):
        return dict(schema=SCHEMA, source_sha256=sha(__file__), binding=self.binding,
            binding_identity_sha256=self.identity, actual_angle_packets_read=len(self._packet_cache),
            all_required_angle_count=len(self.required_angles), all_cached_angle_count=len(self.angles),
            all_original_stages_per_angle=32, physical_F_J_root_reads=0,
            exact_field_or_geometry_certified=False)
