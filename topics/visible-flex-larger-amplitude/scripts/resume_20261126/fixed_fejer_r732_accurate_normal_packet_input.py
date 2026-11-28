#!/usr/bin/env python3
"""Strict R732 rounded-end length reference input for full normal/physical-sixjet work.

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

SCHEMA = "actual-fixed-fejer-r732-complete-normal-packet-accurate-field-input-v1"
TOPIC = "topics/visible-flex-larger-amplitude"
SCRIPT_DIRECTORY = "scripts/resume_20261126"
PINS = {
    "reader": ("read_r732_R729_report.py", "8f9789804b8413a30135f0300f227ffe48f99608f82048ed6a7a36456fcf4432"),
    "driver": ("r732_R729_qp.py", "82fc9d2442094753a0fe32700cb748a3dd9be3e299d94017d03c6ad8cba92866"),
    "packets": ("r732_root_packets.py", "1180d09db83368f0f0948a57c5ebb32544865108867ccb82dccffa310a2b1141"),
    "normal": ("r732_normal_lift.py", "fe5d60e9d04a886a4f11228a7aa63e52e8756272b39e4dc964d1decefc42d823"),
    "base": ("fixed_fejer_r732_meridian_operator.py", "dbaf58889c3a1ece8489f11eda4e4106c907ff69b43a32b57ebda8f5cdf20222"),
    "field_binding": ("r732_source_binding.py", "875a04f68a14e8a74be4e11cb507a2376436d2bc20a5c406b6e69735fb5910c7"),
    "moment_input": ("fixed_fejer_r732_literal_zero_moment_input.py", "146afb7d6cb97a90f95b5232d5779dc4adda9c5b7147990171d9853aff26db07"),
    "length_kernel": ("fixed_fejer_R732_rounded_end_length_kernel.py", "032b6c68570c75a849daa2a5a335a9546cf31e1c3c0ad8a7ee4eb0dee3cb0420"),
    "seed_reference": ("fixed_fejer_R732_rounded_end_arclength_reference.py", "831447a2d50b54029abcf6cd6d441bca7239771b1fd405463db55e1da7646116"),
    "reference": ("fixed_fejer_axisymmetric_reference.py", "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb"),
    "continuous": ("so3_axisymmetric_continuous_integrand.py", "a846d373421df655da3bbba2491847b0cd016ae6db09b5d4176be227b2bc9ce6"),
    "reference_fees": ("fixed_fejer_reference_seed_angular_profile_error_bounds.py", "0471c626b7850fecf19513d68209e090f88830b89ff8ad7cc62c2d1709a75e5b"),
    "fixed_input_binding": ("fixed_fejer_reference_input_binding.py", "3da43e82722dfb4548ff4e8b454d47ec2626ece76084c7801c0be5b8c989670f"),
}
NORMAL_SCHEMA = "complete-fixed-fejer-r732-detached-meridian-normal-layer-v1"
BASE_SCHEMA = "complete-fixed-fejer-r732-so3-meridian-with-core-lift-v1"

REFERENCE_SCHEMA = "R690-fixed-fejer-axisymmetric-SO3-reference-input-v1"
ACTUAL_SOURCE_ROLE_COUNT = 139


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

R732_PROOF_PATH = "results/R732-rounded-cap-exact-terminal-metric-and-full-reference.md"
R732_PROOF_SHA256 = "02db235b89acd0d950f91fc798b72792d843b096393dc9cf42f451556b5d4ec8"
R732_PROOF_BYTES = 16954
R690_PROOF_PATH = "results/R690-quasimonotone-tail-and-deep-valley-input.md"
R690_PROOF_BYTES = 10831
R690_PROOF_SHA256 = "143ccaf9af8596c1803fc23de7691fa1dea36ec042d86ffafa2cc010b3f0252e"
SEED_SCHEMA = "complete-fixed-fejer-R732-rounded-end-arclength-reference-v1"


def safe_cone_seed_scope(seed, base_model, normal_model, moment_module):
    """Validate the entire new physical definition through the complete Q source.

    This is a source/model check only. No scalar length root or inverse is
    evaluated and none of the old supported-mean certificates is inherited.
    """
    if sha(moment_module.__file__) != PINS["moment_input"][1]:
        raise ValueError("The full source of the actual R732 Q definition changed")
    for name in ("_safe_cone_seed", "_length_definition"):
        if sha(getattr(moment_module, name).__code__.co_filename) != PINS["moment_input"][1]:
            raise ValueError("The original complete pure R732 definition method changed")
    reference = base_model["complete_axisymmetric_reference_model"]
    checked, identity = moment_module._safe_cone_seed(seed,
        reference=reference, reference_id=canonical(reference),
        initial_reference_bundle_sha256=base_model["initial_reference_bundle_sha256"],
        fixed_scalar_metric_identity_sha256=base_model["fixed_scalar_metric_identity_sha256"],
        profile=base_model["fixed_scalar_profile_definition"],
        fixed_chart_core_sha256=base_model["fixed_chart_core_sha256"],
        bubble_nodes=normal_model["frozen_moment_Q_definition"]["exact_relative_bubble_nodes"])
    if (checked != seed or identity != canonical(seed)
            or seed.get("schema") != SEED_SCHEMA
            or seed.get("source_sha256") != PINS["seed_reference"][1]
            or seed.get("length_kernel_source_sha256") != PINS["length_kernel"][1]
            or base_model.get("fixed_safe_cone_unit_seed_model") != seed
            or normal_model.get("fixed_safe_cone_unit_seed_model") != seed
            or base_model.get("fixed_safe_cone_unit_seed_identity_sha256") != identity
            or normal_model.get("fixed_safe_cone_unit_seed_identity_sha256") != identity):
        raise ValueError("The full R732 seed definition differs across the same actual field")
    return copy_json(seed["complete_safe_cone_definition"])


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


def bind_fixed_reference_inputs(raw, entry, module, used):
    """Re-read the complete declared recipe and actual six-file input closure.

    Mathematical recipe, actual generated reference/model, and actual full
    target file have separate identities. None is a future numerical point.
    """
    if (not isinstance(entry, dict)
            or entry.get("schema") != "actual-fixed-fejer-complete-input-entry-binding-v1"
            or raw.get("actual_fixed_reference_input_binding") != entry
            or entry.get("source_sha256") != PINS["field_binding"][1]
            or entry.get("actual_pure_input_binding_source_sha256") != PINS["fixed_input_binding"][1]
            or entry.get("actual_input_producer_source_sha256") != PINS["reference"][1]
            or entry.get("all_six_current_whole_files_reread") is not True):
        raise ValueError("Use the complete source-bound fixed Fejer input entry")
    record = entry.get("actual_binding_file")
    path = used.verify(record)
    payload = used.json(record)
    rebound, checked = module.read_binding(path,
        current_files=entry.get("complete_current_input_files"))
    if (payload != rebound or checked != entry.get("complete_input_validation")
            or checked.get("actual_binding_file") != record
            or checked.get("complete_generated_fixed_chart_verified") is not True
            or checked.get("complete_current_six_files_verified") is not True
            or checked.get("predeclared_deterministic_mathematical_target") is not True):
        raise ValueError("The actual complete fixed-input validation changed")
    target = payload["fixed_target_definition"]
    reference = raw["representation"]["base_complete_model"]["complete_axisymmetric_reference_model"]
    target_identity = canonical(target)
    reference_identity = canonical(reference)
    chart_identity = reference.get("fixed_chart_core_sha256")
    mathematical_identity = canonical(target["mathematical_target_recipe"])
    if (target != raw.get("independent_fixed_target_definition")
            or target_identity != raw.get("independent_fixed_target_definition_identity_sha256")
            or target_identity != entry.get("actual_fixed_target_definition_identity_sha256")
            or target_identity != checked.get("fixed_target_definition_identity_sha256")
            or target.get("complete_current_reference_model") != reference
            or reference.get("schema") != REFERENCE_SCHEMA
            or reference.get("source_sha256") != PINS["reference"][1]
            or reference_identity != entry.get("actual_reference_model_identity_sha256")
            or reference_identity != checked.get("actual_current_model_identity_sha256")
            or chart_identity != entry.get("actual_fixed_chart_core_sha256")
            or chart_identity != checked.get("current_fixed_chart_core_sha256")
            or mathematical_identity != entry.get("mathematical_target_identity_sha256")
            or mathematical_identity != checked.get("mathematical_target_identity_sha256")
            or mathematical_identity != reference.get("mathematical_target_identity_sha256")
            or not all(valid_digest(value) for value in
                (target_identity, reference_identity, chart_identity, mathematical_identity))):
        raise ValueError("Keep the complete recipe, actual reference and target identities distinct and equal to their own definitions")
    files = entry["complete_current_input_files"]
    required = {"current_fixed_input_bundle", "current_node_report",
        "current_scalar_input", "current_reference_bundle", "current_carrier",
        "current_preparation_report"}
    if (not isinstance(files, dict) or set(files) != required
            or files != checked.get("current_input_records")):
        raise ValueError("Retain every complete actual fixed-reference input")
    for value in files.values():
        used.verify(value)
    # These complete records were actually consumed by the fixed-input binder.
    # Do not silently substitute a current checkout path for an original path.
    bound_records = [payload[key] for key in ("fixed_input_preparation_report",
        "fixed_target_definition_file", "new_locations",
        "complete_supplied_location_provenance")]
    for value in bound_records:
        used.verify(value)
    maker_report = used.json(payload["fixed_input_preparation_report"])
    def retain_declared_records(value):
        if isinstance(value, dict):
            if {"path", "bytes", "sha256"} <= set(value):
                used.verify(value)
            for item in value.values():
                retain_declared_records(item)
        elif isinstance(value, list):
            for item in value:
                retain_declared_records(item)
    retain_declared_records(maker_report)
    used.verify(record)
    return dict(entry=copy_json(entry), binding_payload=copy_json(payload),
        exact_fixed_target_identity_sha256=target_identity,
        actual_reference_model_identity_sha256=reference_identity,
        fixed_chart_core_sha256=chart_identity,
        mathematical_target_identity_sha256=mathematical_identity,
        complete_current_input_files=copy_json(files))


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
        self.reader = load("_normal_fee_fixed_fejer_reader", self.paths["reader"], PINS["reader"][1])
        self.packet_module = load("_normal_fee_actual_packets", self.paths["packets"], PINS["packets"][1])
        self.reference_module = load("_normal_fee_actual_reference", self.paths["reference"], PINS["reference"][1])
        self.continuous_module = load("_normal_fee_exact_scalar", self.paths["continuous"], PINS["continuous"][1])
        self.seed_fees = load("_normal_fee_reference_math", self.paths["reference_fees"], PINS["reference_fees"][1])
        self.fixed_input_module = load("_normal_fee_fixed_fejer_inputs",
            self.paths["fixed_input_binding"], PINS["fixed_input_binding"][1])
        self.moment_module = load("_normal_fee_R732_moment_input",
            self.paths["moment_input"], PINS["moment_input"][1])
        self.field_binding_module = load("_normal_fee_R732_actual_metadata",
            self.paths["field_binding"], PINS["field_binding"][1])
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
        if len(roles) != ACTUAL_SOURCE_ROLE_COUNT or raw.get("source_sha256_by_role") != {k: v[1] for k, v in roles.items()}:
            raise ValueError("Retain every actual complete scientific source role")
        self.runtime_source_records = {}
        for role, (relative, digest) in roles.items():
            record = self.used.add(self.topic/relative)
            if record["sha256"] != digest:
                raise ValueError("Changed full scientific role: "+role)
            self.runtime_source_records[role] = record
        self.fixed_reference_scope = bind_fixed_reference_inputs(raw,
            pure.get("actual_fixed_reference_input_binding"), self.fixed_input_module, self.used)
        self.target_identity = self.fixed_reference_scope["exact_fixed_target_identity_sha256"]
        self.reference_identity = self.fixed_reference_scope["actual_reference_model_identity_sha256"]
        self.fixed_chart_identity = self.fixed_reference_scope["fixed_chart_core_sha256"]
        self.mathematical_target_identity = self.fixed_reference_scope["mathematical_target_identity_sha256"]
        self.model = copy_json(raw["representation"])
        self.model_identity = canonical(self.model)
        self.base_model = self.model["base_complete_model"]
        self.reference_model = self.base_model["complete_axisymmetric_reference_model"]
        self.seed = copy_json(raw["safe_cone_seed_definition"])
        self.seed_identity = canonical(self.seed)
        if (self.model_identity != raw["model_identity_sha256"]
                or self.model.get("schema") != NORMAL_SCHEMA
                or self.model.get("source_sha256") != PINS["normal"][1]
                or self.base_model.get("schema") != BASE_SCHEMA
                or self.base_model.get("source_sha256") != PINS["base"][1]
                or canonical(self.base_model) != self.model.get("base_model_identity_sha256")
                or canonical(self.reference_model) != self.reference_identity
                or self.reference_model.get("fixed_chart_core_sha256") != self.fixed_chart_identity
                or self.seed_identity != raw.get("safe_cone_seed_identity_sha256")
                or self.base_model.get("fixed_safe_cone_unit_seed_model") != self.seed
                or raw.get("independent_fixed_target_definition_identity_sha256") != self.target_identity):
            raise ValueError("Bind the complete same-point normal/base/frozen-reference/target chain")
        if (raw.get("M") != 160 or raw.get("J") != 923 or raw.get("N") != 2048
                or self.model.get("implicit_control_dimension") != 6
                or self.model.get("normal_increment_dimension") != 3
                or self.model.get("normal_stage_count") != 32):
            raise ValueError("This actual producer retains the complete original fixed Fejer layout and 32 stages")
        if (roles["seed_reference"][1] != PINS["seed_reference"][1]
                or roles["seed_length_kernel"][1] != PINS["length_kernel"][1]
                or roles["new_moment_input"][1] != PINS["moment_input"][1]):
            raise ValueError("Keep the complete actual R732 provider, length kernel and Q sources")
        self.length_definition = safe_cone_seed_scope(
            self.seed, self.base_model, self.model, self.moment_module)
        self.length_definition_identity = canonical(self.length_definition)
        self.length_theorem_record = self.used.add(self.topic/R732_PROOF_PATH)
        if (self.length_theorem_record["sha256"] != R732_PROOF_SHA256
                or self.length_theorem_record["bytes"] != R732_PROOF_BYTES):
            raise ValueError("The complete R732 mathematical source changed")
        self.tail_theorem_record=self.used.add(self.topic/R690_PROOF_PATH)
        if (self.tail_theorem_record["sha256"]!=R690_PROOF_SHA256
                or self.tail_theorem_record["bytes"]!=R690_PROOF_BYTES):
            raise ValueError("Bind the entire original deep-valley reference definition")
        self.scientific_role_sha256 = {k:v[1] for k,v in roles.items()}
        self.partition = [F(v) for v in self.model["exact_normal_step_nodes"]]
        if (len(self.partition) != 33 or self.partition[0] != 0 or self.partition[-1] != 1
                or any(a >= b for a, b in zip(self.partition, self.partition[1:]))):
            raise ValueError("The exact complete common normal partition changed")
        self.packet_module.validate_entry_report(raw, reread_packets=True, reread_arrays=True)
        metadata = raw["normal_root_packets"]
        snapshots = metadata["snapshots"]
        selected_identity = getattr(args, "snapshot_identity_sha256", None)
        report_selected=pure.get("selected_immutable_R732_reference")
        if selected_identity is None:
            if not isinstance(report_selected,dict):
                raise ActualDataUnavailable("The report-save hook selected no same-outer-point immutable reference")
            selected_identity=report_selected["snapshot_identity_sha256"]
        matches=[item for item in snapshots if item["snapshot_identity_sha256"]==selected_identity]
        if len(matches)!=1:
            raise ActualDataUnavailable("The actual immutable reference/normal snapshot is absent")
        selected=matches[0]
        self.report_selected=(copy_json(report_selected) if isinstance(report_selected,dict)
            and report_selected["snapshot_identity_sha256"]==selected_identity else None)
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
        if (self.operator_metadata.get("current_full_point_sha256")!=self.point_sha256
                or self.operator_metadata.get("model")!=self.model
                or self.operator_metadata.get("model_identity_sha256")!=self.model_identity
                or self.operator_metadata.get("source_sha256")!=PINS["normal"][1]):
            raise ValueError("The selected immutable operator metadata describes another point or field")
        if self.report_selected is not None:
            chosen=self.report_selected
            if (chosen["snapshot_file"]!=self.snapshot_record
                    or chosen["operator_metadata_snapshot"]!=self.operator_metadata_record
                    or chosen["point_sha256"]!=self.point_sha256
                    or chosen["capture_ordinal"]!=d["capture_ordinal"]
                    or chosen["normal_model_identity_sha256"]!=self.model_identity
                    or chosen["seed_model_identity_sha256"]!=self.seed_identity
                    or chosen["mutable_progress_or_other_snapshot_used"] is not False):
                raise ValueError("The selected reader output and the actual immutable record differ")
        self.calibration_records = copy_json(d["actual_reference_calibration_files"])
        for record in self.calibration_records:
            self.used.verify(record["immutable_copy"])
        current = self.fixed_reference_scope["entry"]
        if (current.get("actual_fixed_target_definition_identity_sha256") != self.target_identity
                or current.get("actual_reference_model_identity_sha256") != self.reference_identity
                or current.get("actual_fixed_chart_core_sha256") != self.fixed_chart_identity):
            raise ValueError("The actual six-file fixed Fejer input contract differs")
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
        if (self.context.model != self.reference_model or self.context.identity != self.reference_identity
                or self.context.scalar_definition != self.base_model["fixed_scalar_profile_definition"]
                or self.context.scalar_identity != self.base_model["fixed_scalar_metric_identity_sha256"]):
            raise ValueError("The whole accurate scalar/chart context changed the actual frozen target")
        end=self.seed["working_definition"]["rounded_end"]
        if (F(self.context.law.tail.width)!=F(end["beta_width_exact"])
                or F(self.context.law.tail.kappa)!=F(end["beta_kappa_exact"])
                or end["beta_law_source_sha256"]!=roles["deep_scalar"][1]):
            raise ValueError("The original deep scalar and frozen rounded-end input differ")
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
        self.length_rows, self.length_row_sources = self._read_complete_length_candidates(pure)
        if any(angle not in self.length_rows for angle in self.angles):
            raise ActualDataUnavailable("A recorded normal angle lacks its own-snapshot complete length candidate")
        self._packet_cache = {}
        self.binding = dict(schema=SCHEMA, source_sha256=sha(__file__),
            scientific_report=self.report_record, complete_pure_reader_sha256=PINS["reader"][1],
            actual_driver_sha256=PINS["driver"][1], actual_source_commit=raw["source_commit"],
            actual_run_id=raw.get("github_run_id"), model_identity_sha256=self.model_identity,
            complete_model=self.model, exact_fixed_target_identity_sha256=self.target_identity,
            actual_reference_model_identity_sha256=self.reference_identity,
            fixed_chart_core_sha256=self.fixed_chart_identity,
            mathematical_target_identity_sha256=self.mathematical_target_identity,
            complete_actual_fixed_reference_input_binding=copy_json(current),
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
            complete_actual_length_candidate_sources=self.length_row_sources,
            complete_safe_cone_seed_model=self.seed,
            complete_safe_cone_seed_model_identity_sha256=self.seed_identity,
            complete_safe_cone_length_definition=self.length_definition,
            complete_safe_cone_length_definition_identity_sha256=self.length_definition_identity,
            R732_theorem_source=self.length_theorem_record,R690_theorem_source=self.tail_theorem_record,
            same_snapshot_rounded_end=self.length_diagnostics["rounded_end"],
            report_hook_selected_reference=self.report_selected,
            source_bound_working_terminal_arrays=self.terminal_array_evidence,
            complete_own_snapshot_length_metadata=self.length_diagnostics,
            operator_metadata_snapshot=self.operator_metadata_record,
            selected_snapshot_seed_batches_not_latest_replacements=True,
            complete_own_snapshot_binary_length_members_verified=True,
            saved_working_density_has_descriptor_only_not_raw_values=True,
            old_mean_v_d_w_lambda_arrays_or_certificates_inherited=False,
            accurate_length_root_inverse_or_two_angle_error_paid_here=False,
            working_primitive_equals_integral_of_returned_unit_T0_claimed=False,
            full_reference_parameter_domain=["0", "1"],
            physical_material_domain="0<=s<=S, including all five rounded-end pieces",
            reference_inverse_arclength_is_not_polynomial_in_material_s=True,
            all_922_original_material_cells_retained=True,
            source_sha256_by_role={role: value[1] for role,value in PINS.items()},
            full_scientific_runtime_source_records=self.runtime_source_records,
            no_new_working_field_J_or_normal_root_evaluation=True,
            accurate_scalar_context_may_be_evaluated=True,
            accepted_outer_point_not_inferred_from_cache=True,
            literal_node_coverage_is_not_whole_angle_coverage=True,
            reference_root_or_normal_root_or_physical_sixjet_fee_paid_here=False)
        self.identity = canonical(self.binding)
        self.bound_field_scope = dict(actual_input_identity_sha256=self.identity,
            current_full_point_sha256=self.point_sha256,
            complete_current_model_identity_sha256=self.model_identity,
            complete_seed_model_identity_sha256=self.seed_identity,
            fixed_target_identity_sha256=self.target_identity)
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

    def _read_complete_length_candidates(self, pure):
        """Read all complete length batches belonging to the selected snapshot.

        The latest report may contain later reference cache additions. Those
        additions never fill a hole in this selected immutable snapshot.
        Every saved binary member is read whole; the full density descriptor
        remains a descriptor because the provider did not save density values.
        """
        require_actions()
        np = self.np
        supported = dict(definition=self.seed, identity_sha256=self.seed_identity,
            binding=copy_json(self.report["safe_cone_seed_binding"]))
        if (pure.get("safe_cone_seed_definition") != self.seed
                or pure.get("safe_cone_seed_identity_sha256") != self.seed_identity
                or pure.get("safe_cone_seed_binding") != supported["binding"]):
            raise ValueError("The complete pure report changed the actual frozen length seed")
        seed_meta = self.operator_metadata.get("base_complete_metadata", {}).get(
            "fixed_safe_cone_unit_seed")
        if not isinstance(seed_meta, dict):
            raise ActualDataUnavailable("The selected point has no immutable complete length metadata")
        method = self.field_binding_module.safe_cone_seed_metadata
        if sha(method.__code__.co_filename) != PINS["field_binding"][1]:
            raise ValueError("The complete own-snapshot length reader source changed")
        checked = method(self.operator_metadata, self.model,
            self.scientific_role_sha256, supported)
        for record in checked["complete_actual_whole_files_reread"]:
            self.used.verify(record)
        records = seed_meta.get("length_root_batch_records")
        if (not isinstance(records, list)
                or records != checked.get("length_root_batch_records")):
            raise ValueError("The selected point lost its complete immutable length batches")
        if self.report_selected is not None:
            chosen=self.report_selected
            for saved,own in (("rounded_end","rounded_end"),("length_root_batch_records","length_root_batch_records"),
                    ("literal_angles","completed_batch_literal_angle_hex"),
                    ("complete_length_plan","length_plan"),("working_rule","full_rule")):
                if chosen[saved]!=checked[own]:
                    raise ValueError("The selected report and immutable physical reference input differ: "+own)
        latest = pure.get("seed_diagnostics")
        if isinstance(latest, dict):
            later = latest.get("length_root_batch_records")
            if (not isinstance(later, list) or later[:len(records)] != records
                    or latest.get("fixed_safe_cone_unit_seed_identity_sha256") != self.seed_identity):
                raise ValueError("The selected immutable batches are not the same complete actual prefix")
        plan = checked.get("length_plan")
        if (not isinstance(plan, dict) or "runner_raw_rule" not in plan
                or "runner_raw_description" not in plan):
            raise ActualDataUnavailable("The selected point lacks its complete saved length-rule files")
        description = self.used.json(plan["runner_raw_description"])
        if description != {k:v for k,v in plan.items() if k!="runner_raw_description"}:
            raise ValueError("The entire original length-plan description changed")
        order = self.length_definition["working_order"]
        n = 922*order
        plan_path = self.used.verify(plan["runner_raw_rule"])
        required_plan = {"normalized_nodes", "gauss_u", "gauss_w", "full_points",
            "full_weights", "physical_S", "central_length", "terminal_partition",
            "terminal_primitive_prefix","blend_partition","blend_beta_prefix","model_identity"}
        with np.load(plan_path, allow_pickle=False) as data:
            if set(data.files) != required_plan:
                raise ValueError("Retain every original saved length-rule array")
            for name, shape in (("normalized_nodes",(923,)), ("gauss_u",(order,)),
                    ("gauss_w",(order,)), ("full_points",(n,)), ("full_weights",(n,)),
                    ("physical_S",()),("central_length",())):
                a = np.array(data[name], copy=True)
                if (a.shape != shape or a.dtype != np.dtype("float64")
                        or not np.isfinite(a).all()):
                    raise ValueError("A full actual length-rule member changed shape or finite words")
            end=checked["rounded_end"]["definition"]
            if (plan["rounded_end"]!=end
                    or float(data["central_length"].item()).hex()!=end["central_length_hex"]):
                raise ValueError("Use the selected actual central-length word in the whole length plan")
            terminal={}
            for member,descriptor in (("terminal_partition","turn_partition"),("terminal_primitive_prefix","turn_prefix"),
                    ("blend_partition","blend_partition"),("blend_beta_prefix","blend_prefix")):
                values=np.array(data[member],copy=True)
                desc=end[descriptor]
                if (list(values.shape)!=desc["shape"] or str(values.dtype)!=desc["dtype"]
                        or values.dtype!=np.dtype("float64") or not np.isfinite(values).all()
                        or array_sha(values)!=desc["sha256"]):
                    raise ValueError("The selected rounded-end array differs from the complete descriptor: "+member)
                terminal[member]=values
            turns=terminal["terminal_partition"];blend=terminal["blend_partition"]
            xp=terminal["terminal_primitive_prefix"];bp=terminal["blend_beta_prefix"]
            if (turns.ndim!=1 or blend.ndim!=1 or len(turns)<2 or len(blend)<2
                    or xp.shape!=(len(turns),2) or bp.shape!=(len(blend),1)
                    or turns[0]!=0. or float(turns[-1]).hex()!=end["uf_hex"]
                    or blend[0]!=float(F(1,1000)) or blend[-1]!=float(2*F(1,1000))
                    or not np.all(np.diff(turns)>0) or not np.all(np.diff(blend)>0)
                    or not np.all(xp[0]==0.) or bp[0,0]!=0.
                    or float(xp[-1,0]).hex()!=end["xf_hex"] or float(xp[-1,1]).hex()!=end["hf_hex"]):
                raise ValueError("Bind the original terminal and blend prefixes to their actual complete partitions")
            for member in terminal.values():member.setflags(write=False)
            self.rounded_work_arrays=terminal
            self.terminal_array_evidence=dict(whole_plan_file=copy_json(plan["runner_raw_rule"]),
                selected_operator_metadata_snapshot=copy_json(self.operator_metadata_record),
                terminal_definition=copy_json(end),
                complete_binary_members={name:dict(shape=list(arr.shape),dtype=str(arr.dtype),
                    sha256=array_sha(arr)) for name,arr in terminal.items()},
                physical_S_word=float(data["physical_S"].item()).hex(),
                central_length_word=float(data["central_length"].item()).hex())
            nodes = np.array(data["normalized_nodes"], copy=True)
            if (nodes[0] != 0. or nodes[-1] != 1. or not np.all(np.diff(nodes)>0.)
                    or not np.all(data["gauss_w"]>0.) or not np.all(data["full_weights"]>0.)
                    or array_sha(nodes) != plan["complete_normalized_rule"]["normalized_node_record"]["sha256"]
                    or array_sha(data["full_weights"]) != plan["complete_normalized_rule"]["positive_weight_record"]["sha256"]
                    or float(data["physical_S"].item()).hex() != self.seed["working_definition"]["physical_S_carrier_hex"]
                    or data["model_identity"].shape != ()
                    or data["model_identity"].dtype.kind != "U"
                    or str(data["model_identity"].item()) != self.seed_identity):
                raise ValueError("The entire actual length rule differs from its frozen model/records")
        self.used.verify(plan["runner_raw_rule"])
        rows, provenance = {}, []
        for index, batch in enumerate(records):
            if "runner_raw_arrays" not in batch or "runner_raw_description" not in batch:
                raise ActualDataUnavailable("A selected-point length batch was not completely saved")
            desc = self.used.json(batch["runner_raw_description"])
            if desc != {k:v for k,v in batch.items() if k!="runner_raw_description"}:
                raise ValueError("The whole original scalar-length batch description changed")
            record = batch["runner_raw_arrays"]
            path = self.used.verify(record)
            angles, roots = batch["created_literal_angle_hex"], batch["roots"]
            m = len(angles)
            with np.load(path, allow_pickle=False) as data:
                if set(data.files) != {"angles", "scalar_root_and_jets",
                        "complete_prefixes", "complete_control_jets", "model_identity"}:
                    raise ValueError("Keep all five saved complete length-batch members")
                arrays = {}
                for name, shape in (("angles",(m,)), ("scalar_root_and_jets",(m,3)),
                        ("complete_prefixes",(m,923,3)), ("complete_control_jets",(m,3,6,3))):
                    value = np.array(data[name], copy=True)
                    if (value.shape != shape or value.dtype != np.dtype("float64")
                            or not np.isfinite(value).all()):
                        raise ValueError("A full actual length-batch member changed: "+name)
                    value.setflags(write=False)
                    arrays[name] = value
                if (data["model_identity"].shape != ()
                        or data["model_identity"].dtype.kind != "U"
                        or str(data["model_identity"].item()) != self.seed_identity
                        or [float(v).hex() for v in arrays["angles"]] != angles):
                    raise ValueError("The actual length batch changed model or complete angle order")
                for j,(angle,packet) in enumerate(zip(angles,roots)):
                    if packet["rounded_end"]!=end:
                        raise ValueError("This selected root batch used different rounded-end scalars")
                    root = packet["complete_working_root"]
                    words = [float(root[k]).hex() for k in ("xi","xi_phi","xi_phiphi")]
                    if ([float(v).hex() for v in arrays["scalar_root_and_jets"][j]] != words
                            or array_sha(arrays["complete_prefixes"][j]) != root["full_prefix_record"]["sha256"]
                            or array_sha(arrays["complete_control_jets"][j]) != packet["complete_control_jet_record"]["sha256"]):
                        raise ValueError("Saved whole root/prefix/control words differ from the own-angle packet")
                    if angle in rows:
                        raise ValueError("An immutable complete length cache cannot duplicate an angle")
                    rows[angle] = dict(literal_phi_hex=angle, xi=words[0],
                        xi_phi=words[1], xi_phiphi=words[2],
                        actual_completed_batch_index=index,
                        actual_raw_batch_sha256=record["sha256"],
                        complete_working_root_identity_sha256=root["root_identity_sha256"],
                        complete_working_root_packet_identity_sha256=packet["identity_sha256"])
            self.used.verify(record)
            provenance.append(dict(actual_completed_batch_index=index,
                runner_raw_arrays=copy_json(record),
                runner_raw_description=copy_json(batch["runner_raw_description"]),
                created_literal_angle_hex=list(angles),
                complete_original_batch_metadata=copy_json(batch),
                selected_operator_metadata_snapshot=copy_json(self.operator_metadata_record),
                saved_complete_scalar_root_prefix_and_control_members_verified=True,
                original_unsaved_density_values_not_claimed_read=True))
        if list(rows) != checked["completed_batch_literal_angle_hex"]:
            raise ValueError("Retain every complete own-snapshot length root in its original discovery order")
        self.length_diagnostics = copy_json(checked)
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
        rebound = bind_fixed_reference_inputs(self.report,
            self.fixed_reference_scope["entry"], self.fixed_input_module, self.used)
        if rebound != self.fixed_reference_scope:
            raise ValueError("The full fixed-reference input changed during accurate field work")
        self.used.recheck()
        definition = safe_cone_seed_scope(self.seed, self.base_model, self.model,
            self.moment_module)
        if (definition != self.length_definition
                or canonical(definition) != self.length_definition_identity):
            raise ValueError("The entire R732 length-reference definition changed during accurate work")
        self.used.verify(self.length_theorem_record)
        self.used.verify(self.tail_theorem_record)
        if self.point_sha256 != array_sha(self.x):
            raise ValueError("The selected entire current point was modified")
        return True

    def metadata(self):
        return dict(schema=SCHEMA, source_sha256=sha(__file__), binding=self.binding,
            binding_identity_sha256=self.identity, actual_angle_packets_read=len(self._packet_cache),
            all_required_angle_count=len(self.required_angles), all_cached_angle_count=len(self.angles),
            all_original_stages_per_angle=32, physical_F_J_root_reads=0,
            exact_field_or_geometry_certified=False)
