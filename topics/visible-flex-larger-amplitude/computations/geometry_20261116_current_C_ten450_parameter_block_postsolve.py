#!/usr/bin/env python3
"""R437: actual post-radial parameter choice on the frozen R438 five stages.

This independent source imports the exact frozen R438 lifecycle and scientific
CLI bodies. It creates the first H/W/marker words only after the actual current
radial replay, or reuses the first same-job words on a genuine refined450.
No numeric field, accepted checkpoint, clock, or future result is fabricated.
All scientific work is restricted to the named repository Actions.
Author: AI, 2026-11-16.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import textwrap
import traceback

REPO = "Rogerhu12/math-research-public"
SCHEMA = "R437-current-ten450-first-or-frozen-construction-block-postsolve-v1"
INPUT_SCHEMA = SCHEMA + "-input-v1"
BASE_NAME = "geometry_20261116_current_C_ten450_original_or_refined_block_postsolve.py"
BASE_SHA = "5bb2ee1d9526a10ec707d1106763e4ebe94599d7e5152f726864a6812ba8af95"
HELPER = "geometry_20261116_current_C_ten450_closed_parameter_policy.py"
HELPER_SHA = "d7d01460f5a22f4fa2ca75ad36475688d65a465ba488d9caff65cb5ef13fb871"
HELPER_SCHEMA = "R437-current-ten450-explicit-closed-parameter-policy-v1"
JOINT_LAUNCH = "geometry_20261116_continuous_ten_joint_full453_frozen450_launch.py"
JOINT_LAUNCH_SHA = "cb05724bbedf71951524d187d242c1783d244bc729241ec91a91e0a9cf8f02d7"
JOINT_DRIVER = "geometry_20261116_continuous_ten_joint_full453_frozen450_physical_dn.py"
JOINT_DRIVER_SHA = "5400aa4a724b0403e6a89db2ea056f489dc336e685fa85e2ef1ef0fc51569592"
JOINT_UPSTREAM_SCHEMA = "current-C-continuous-ten-joint-full453-frozen450-owned-process-launch-v1"
JOINT_DRIVER_SCHEMA = "current-C-continuous-ten-joint-live-full453-to-frozen450-physical-DN-v1"
JOINT_DEADLINE_SCHEMA = "request203-owned-job-science-deadline-v1"
PARAMETERS = ("construction_parameters", "held_witnesses")
CONSTRUCTION_FIELDS = ("cut_correction_width", "cap_height", "fixed_cap")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def identity(path):
    path = Path(path).resolve(strict=True)
    raw = path.read_bytes()
    return dict(file=str(path), bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())


def exact_replace(text, old, new):
    require(text.count(old) == 1, "Frozen source fragment must occur exactly once")
    return text.replace(old, new, 1)


def load_original():
    path = Path(__file__).resolve().with_name(BASE_NAME)
    actual = identity(path)
    require(actual["sha256"] == BASE_SHA, "Keep the exact original R438 source")
    name = "_r437_original_r438_owned_procedure"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        sys.modules.pop(name, None)
        raise
    return module, path.read_text(encoding="utf-8"), actual


BASE, ORIGINAL_TEXT, ORIGINAL_SOURCE = load_original()
STAGES = BASE.STAGES
C_FILES = BASE.C_FILES
RESULT_SCHEMAS = BASE.RESULT_SCHEMAS
RESULT_SOURCES = BASE.RESULT_SOURCES
PINS = dict(BASE.PINS)
PINS[HELPER] = HELPER_SHA
PINS[BASE_NAME] = BASE_SHA
PINS[JOINT_LAUNCH] = JOINT_LAUNCH_SHA
PINS[JOINT_DRIVER] = JOINT_DRIVER_SHA
# These genuine original API names are exported for the independently bound
# R425 launcher. Its registration must name this new source and schema.
for _name in ("actions", "read", "write", "receipt", "same_payload", "contained",
              "current_identity", "proc_record", "same_process", "group_rows",
              "OwnedChild", "mesh_launch_quiet", "bound_frozen450_metadata"):
    globals()[_name] = getattr(BASE, _name)


VALIDATION_CONSTRUCTION = """    policy = value.get("construction_policy")
    require(isinstance(policy, dict) and set(policy) == {"file", "sha256"}
            and isinstance(policy["file"], str) and policy["file"]
            and isinstance(policy["sha256"], str) and len(policy["sha256"]) == 64,
            "Use the exact small R437 parameter policy, not an invented inline H")
    require("construction" not in value,
            "The original input has no prefilled H/markers or hidden placeholder")
    mode = value.get("construction_mode")
    require(mode in ("initial-construction", "reuse-construction"),
            "Choose one explicit first-field or same-word reuse branch")
    if mode == "reuse-construction":
        first = value.get("first_construction_freeze")
        require(isinstance(first, dict) and set(first) == {"file", "sha256"}
                and isinstance(first["file"], str) and first["file"]
                and isinstance(first["sha256"], str) and len(first["sha256"]) == 64,
                "A mesh successor consumes the actual first complete freeze file")
        material = value.get("first_material_transport")
        require(isinstance(material, dict) and set(material) == {"file", "sha256"}
                and isinstance(material["file"], str) and material["file"]
                and isinstance(material["sha256"], str) and len(material["sha256"]) == 64,
                "Reuse consumes the real first Phi/registration/normalization definition")
    else:
        require("first_construction_freeze" not in value and "first_material_transport" not in value,
                "Do not label a new first-field choice as an inherited freeze")
    require(isinstance(resources.get("parameter_budgets_seconds"), dict)
            and set(resources["parameter_budgets_seconds"]) ==
                {"construction_parameters", "held_witnesses"},
            "Declare both additional work caps inside the same original clock")
    for key in ("construction_parameters", "held_witnesses"):
        positive_number(resources["parameter_budgets_seconds"][key], key)
    resolution = value.get("witness_resolution")
    require(isinstance(resolution, dict) and set(resolution) == {"interval_bits", "sqrt_bits"}
            and type(resolution["interval_bits"]) is int and 64 <= resolution["interval_bits"] <= 8192
            and type(resolution["sqrt_bits"]) is int and 16 <= resolution["sqrt_bits"] <= 4096,
            "Keep explicit original work precision for resolving the declared witness table")
"""

# The two small derived metadata/lifecycle functions are formed from frozen
# source text. Their complete replacement lists are part of this source; they
# are not alternative scientific algorithms and do not edit the old module.
_vstart = ORIGINAL_TEXT.index("def validate_spec(value):\n")
_vend = ORIGINAL_TEXT.index("\ndef pin_sources(", _vstart)
_validate_original = ORIGINAL_TEXT[_vstart:_vend]
_cstart = _validate_original.index('    construction = value.get("construction")\n')
_cend = _validate_original.index('    for name, keys in (("metric", METRIC_PARAMETERS)', _cstart)
_validate_view = exact_replace(
    _validate_original, _validate_original[_cstart:_cend], VALIDATION_CONSTRUCTION)
_validate_view = exact_replace(_validate_view,
    "Select one explicit original193 or frozen-source R431 upstream branch",
    "Select one explicit original193, joint203, or frozen-source R431 upstream branch")
_validation_environment = dict(vars(BASE))
_validation_environment["INPUT_SCHEMA"] = INPUT_SCHEMA
_validation_environment["UPSTREAM_KINDS"] = BASE.UPSTREAM_KINDS + ("joint203-frozen450",)
exec(compile(_validate_view, str(Path(__file__).resolve()) + ":R438-validation-view", "exec"),
     _validation_environment)
validate_spec = _validation_environment["validate_spec"]


def pin_sources(computations):
    records = BASE.pin_sources(computations)
    for name in (BASE_NAME, HELPER, JOINT_LAUNCH, JOINT_DRIVER):
        item = identity(Path(computations) / name)
        require(item["sha256"] == PINS[name], "Frozen explicit source branch differs: " + name)
        records[name] = item
    return records


# The new joint provider is a distinct actual producer/source/deadline tuple.
# All original two-phase acceptance, live writer and raw-file binding checks
# are copied verbatim into this function view; no old tuple is renamed.
_bstart = ORIGINAL_TEXT.index("    def bind_original193(self):\n")
_bend = ORIGINAL_TEXT.index("\n    def skip(self,", _bstart)
_bind_original = textwrap.dedent(ORIGINAL_TEXT[_bstart:_bend])
_bind_joint = exact_replace(_bind_original, "def bind_original193(", "def bind_joint203(")
_joint_environment = dict(vars(BASE))
_joint_environment.update(PINS=PINS, pin_sources=pin_sources,
    LAUNCH=JOINT_LAUNCH, DRIVER=JOINT_DRIVER,
    UPSTREAM_SCHEMA=JOINT_UPSTREAM_SCHEMA, DRIVER_SCHEMA=JOINT_DRIVER_SCHEMA,
    DEADLINE_SCHEMA=JOINT_DEADLINE_SCHEMA)
exec(compile(_bind_joint, str(Path(__file__).resolve()) + ":explicit-joint203-origin-view", "exec"),
     _joint_environment)
bind_joint203 = _joint_environment["bind_joint203"]

_istart = ORIGINAL_TEXT.index("    def invoke(self, name, make_command, result_name=\"result.json\"):\n")
_iend = ORIGINAL_TEXT.index("\n    def producer_completed(", _istart)
_invoke_original = textwrap.dedent(ORIGINAL_TEXT[_istart:_iend])
_invoke_view = exact_replace(_invoke_original, "def invoke(", "def invoke_parameter(")
require(_invoke_view.count('self.report["stages"]') == 1,
        "Keep the original single actual row lookup")
_invoke_view = _invoke_view.replace('self.report["stages"]', 'self.report["parameter_actions"]')
require(_invoke_view.count('self.spec["resources"]["stage_budgets_seconds"]') == 2,
        "Keep both original work-cap references")
_invoke_view = _invoke_view.replace('self.spec["resources"]["stage_budgets_seconds"]',
                                    'self.spec["resources"]["parameter_budgets_seconds"]')
require(_invoke_view.count("self.skip(") == 4, "Keep all original skip branches")
_invoke_view = _invoke_view.replace("self.skip(", "self.skip_parameter(")
_parameter_environment = dict(vars(BASE))
_parameter_environment.update(PINS=PINS,
    RESULT_SOURCES={name: HELPER for name in PARAMETERS},
    RESULT_SCHEMAS={name: HELPER_SCHEMA for name in PARAMETERS})
exec(compile(_invoke_view, str(Path(__file__).resolve()) + ":R438-owned-parameter-view", "exec"),
     _parameter_environment)
invoke_parameter = _parameter_environment["invoke_parameter"]
VIEW_IDENTITIES = {
    "original_validate_fragment_sha256": hashlib.sha256(_validate_original.encode()).hexdigest(),
    "independent_validate_fragment_sha256": hashlib.sha256(_validate_view.encode()).hexdigest(),
    "original_owned_invoke_fragment_sha256": hashlib.sha256(_invoke_original.encode()).hexdigest(),
    "independent_owned_parameter_fragment_sha256": hashlib.sha256(_invoke_view.encode()).hexdigest(),
    "original_two_phase_origin_fragment_sha256": hashlib.sha256(_bind_original.encode()).hexdigest(),
    "explicit_joint203_origin_fragment_sha256": hashlib.sha256(_bind_joint.encode()).hexdigest(),
    "joint203_original_acceptance_and_checkpoint_body_changed": False,
    "scientific_R438_run_and_all_five_CLI_bodies_changed": False,
    "owned_process_stop_wait_and_absolute_clock_body_changed": False,
}


class ConstructionUnavailable(RuntimeError):
    """A required actual constructor was not produced; not a geometric refutation."""


class Procedure(BASE.Procedure):
    invoke_parameter = invoke_parameter

    def __init__(self, spec, spec_id):
        # Only this new procedure's in-memory derived constructor is added.
        # The hashed original small input file is never modified.
        super().__init__(copy.deepcopy(spec), spec_id)

    def persist(self):
        self.report["schema"] = SCHEMA
        self.report["source"] = identity(__file__)
        self.report["original_R438_procedure"] = ORIGINAL_SOURCE
        self.report["original_R438_explicit_source_views"] = VIEW_IDENTITIES
        self.report.setdefault("parameter_actions",
            [dict(name=name, started=False, status="not-started") for name in PARAMETERS])
        self.report.setdefault("actual_selected_construction", None)
        self.report.setdefault("actual_witness_plan", None)
        self.report.setdefault("actual_material_transport", None)
        self.report.setdefault("parameter_choice_is_not_geometric_acceptance", True)
        self.report.setdefault("all_five_original_scientific_stages_preserved", True)
        self.report.setdefault("raw_first_freeze_must_live_through_same_g_mesh", True)
        self.report.setdefault("construction_clock_or_resource_allowance_not_restarted", True)
        self.report.setdefault("material_pullback_or_conjugacy_executed", False)
        self.report.setdefault("same_closed_g_not_inferred_from_construction_equality", True)
        super().persist()

    def bind(self):
        # Each explicit original/refined/joint branch establishes the current
        # accepted450, its real origin deadline, same C and source ledgers.
        # Explicit unbound call also supports the original held launcher's
        # metadata-only OriginalBindingView; it is not a Procedure subclass.
        if self.spec["upstream_kind"] == "joint203-frozen450":
            self.report["selected_upstream_kind"] = "joint203-frozen450"
            self.report["old_parent_geometry_certificates_reused"] = False
            result = bind_joint203(self)
        else:
            result = BASE.Procedure.bind(self)
        helper = identity(Path(self.spec["computations"]) / HELPER)
        require(helper["sha256"] == HELPER_SHA, "Keep the independently frozen R437 policy helper")
        self.report["parameter_source_pins"] = {
            HELPER: helper, BASE_NAME: ORIGINAL_SOURCE,
            JOINT_LAUNCH: identity(Path(self.spec["computations"]) / JOINT_LAUNCH),
            JOINT_DRIVER: identity(Path(self.spec["computations"]) / JOINT_DRIVER)}
        for name, item in self.report["parameter_source_pins"].items():
            require(item["sha256"] == PINS[name], "Keep the complete declared source closure")
        policy_path = contained(self.spec["construction_policy"]["file"],
                                self.namespace, exists=True)
        policy, pid = read(policy_path, self.spec["construction_policy"]["sha256"])
        require(pid["bytes"] <= 90000
                and policy.get("schema") == HELPER_SCHEMA + "-recipe-v1",
                "Read the original one small declared policy")
        self.report["actual_construction_policy"] = pid
        self.persist()
        return result

    def skip_parameter(self, name, reason):
        row = next(r for r in self.report["parameter_actions"] if r["name"] == name)
        row.update(status="not-started", unstarted_reason=reason)
        self.persist()
        return None

    def parameter_spec(self, operation, out, seconds):
        s = self.spec
        origin = (Path(s["origin_launch_directory"]).resolve()
                  if s["upstream_kind"] == "R431-refined450"
                  else Path(s["upstream_launch_directory"]).resolve())
        origin_id = receipt(origin / "result.json")
        value = dict(schema=HELPER_SCHEMA + "-input-v1", operation=operation,
            namespace=str(self.namespace), computations=str(Path(s["computations"]).resolve()),
            origin_launch_directory=str(origin), origin_result_sha256=origin_id["sha256"],
            job_deadline=str(Path(s["job_deadline"]).resolve()),
            job_deadline_sha256=s["job_deadline_sha256"],
            checkpoint_directory=str(self.cpdir), checkpoint_sha256=self.cp_id["sha256"],
            policy=str(Path(s["construction_policy"]["file"]).resolve()),
            policy_sha256=s["construction_policy"]["sha256"],
            resources=dict(budget_seconds=seconds,
                           free_bytes_reserve=s["resources"]["free_bytes_reserve"]),
            out=str(out))
        if operation == "initial-construction":
            radial = self.out / "radial_replay"
            value.update(radial_directory=str(radial),
                         radial_result_sha256=receipt(radial / "result.json")["sha256"])
        elif operation == "reuse-construction":
            first = s["first_construction_freeze"]
            material = s["first_material_transport"]
            value.update(first_construction_freeze=str(Path(first["file"]).resolve()),
                         first_construction_freeze_sha256=first["sha256"],
                         first_material_transport=str(Path(material["file"]).resolve()),
                         first_material_transport_sha256=material["sha256"])
        else:
            shared = self.out / "shared_field"
            atlas = self.out / "original_cuff_atlas" / "original-cuff-target-atlas.json"
            value.update(shared_directory=str(shared),
                         shared_result_sha256=receipt(shared / "result.json")["sha256"],
                         cuff_atlas=str(atlas), cuff_atlas_sha256=receipt(atlas)["sha256"],
                         proof_directory=str(Path(s["proof_directory"]).resolve()),
                         witness_resolution=s["witness_resolution"],
                         construction_mode=s["construction_mode"])
            first = (self.report["actual_selected_construction"]["outputs"]["first_construction_freeze"]
                     if s["construction_mode"] == "initial-construction"
                     else s["first_construction_freeze"])
            value.update(first_construction_freeze=str(Path(first["file"]).resolve()),
                         first_construction_freeze_sha256=first["sha256"])
            if s["construction_mode"] == "reuse-construction":
                material = s["first_material_transport"]
                value.update(first_material_transport=str(Path(material["file"]).resolve()),
                             first_material_transport_sha256=material["sha256"])
        return value

    def parameter_command(self, name, operation, out, seconds):
        value = self.parameter_spec(operation, out, seconds)
        item = write(self.out / (name + "-input.json"), value)
        row = next(r for r in self.report["parameter_actions"] if r["name"] == name)
        row["actual_parameter_input"] = item
        self.persist()
        return [sys.executable, "-u", str(Path(self.spec["computations"]) / HELPER),
                "--input", item["file"], "--input-sha256", item["sha256"]]

    def parameter_complete(self, name, result):
        row = next(r for r in self.report["parameter_actions"] if r["name"] == name)
        # A completed original helper result is consumed from the real file.
        # The helper's separate stdout limit is not a new scientific gate.
        metadata_only_overflow = (row.get("actual_child_exit") == 70
            and isinstance(result, dict) and result.get("completed") is True
            and result.get("error") is None)
        row["completed_parameter_file_with_stdout_overflow"] = metadata_only_overflow
        good = (isinstance(result, dict) and result.get("completed") is True
            and result.get("returned") is True
            and result.get("error") is None
            and result.get("resource_partial") is False
            and result.get("external_interruption") is False
            and (row.get("actual_child_exit") == 0 or metadata_only_overflow)
            and row.get("resource_stop") is None and row.get("external_interruption") is None
            and row.get("owned_process", {}).get("owned_group_quiescent") is True)
        self.persist()
        return good

    def select_construction(self):
        s = self.spec
        operation = s["construction_mode"]
        result = self.invoke_parameter("construction_parameters",
            lambda out, seconds: self.parameter_command("construction_parameters", operation, out, seconds))
        if not self.parameter_complete("construction_parameters", result):
            self.skip_parameter("held_witnesses", "actual-construction-not-produced")
            for stage in STAGES[1:]:
                self.skip(stage, "actual-R437-construction-not-produced")
            raise ConstructionUnavailable("The required actual first or frozen construction was not produced")
        path = self.out / "construction_parameters" / "r413-construction.json"
        value, rid = read(path)
        require(same_payload(rid, result["outputs"]["r413_construction"])
                and value.get("schema") ==
                    "R413-current-C-original-cuff-target-atlas-binding-v1-construction-v1"
                and value.get("checkpoint_sha256") == self.cp_id["sha256"],
                "Use the generated plan for this actual selected450")
        construction = {key: value[key] for key in CONSTRUCTION_FIELDS}
        require(construction == result["actual_construction"],
                "The actual helper constructor and original R413 payload differ")
        self.spec["construction"] = construction
        self.report["actual_selected_construction"] = dict(
            original_helper_result=receipt(path.parent / "result.json"),
            original_R413_construction=rid, operation=operation,
            complete_construction_words=result["complete_construction_words"],
            actual_construction=construction, outputs=result["outputs"],
            first_height_selection=result.get("height_selection"),
            original_first_freeze=result.get("first_construction_freeze"),
            original_first_material_transport=result.get("first_material_transport"),
            current_complete112_material_definition_identity=result.get(
                "actual_complete112_material_definition_identity"),
            first_and_current_core_words_equal=result.get("first_and_current_core_words_equal"),
            construction_equality_does_not_certify_common_material_metric=True,
            no_unrecorded_in_memory_height_or_marker_choice=True)
        self.persist()

    def select_witnesses(self):
        result = self.invoke_parameter("held_witnesses",
            lambda out, seconds: self.parameter_command("held_witnesses", "held-witnesses", out, seconds))
        if isinstance(result, dict) and result.get("actual_material_transport") is not None:
            self.report["actual_material_transport"] = result["actual_material_transport"]
        if self.parameter_complete("held_witnesses", result):
            path = self.out / "held_witnesses" / "r425-witness-plan.json"
            value, rid = read(path)
            require(same_payload(rid, result["outputs"]["r425_witness_plan"])
                    and value.get("schema") ==
                        "R425-current-accurate-active-quarter-turn-witness-plan-v1",
                    "Use the actual same-field witness plan")
            self.report["actual_witness_plan"] = dict(
                original_helper_result=receipt(path.parent / "result.json"),
                witness_plan=rid, complete_explicit_points=value["points"],
                held_distance_or_deltaE_proved=False)
        self.report["witness_failure_does_not_gate_metric_or_reach"] = True
        self.persist()

    def invoke(self, name, make_command, result_name="result.json"):
        result = super().invoke(name, make_command, result_name)
        if name == "radial_replay":
            if not self.producer_completed(name, result):
                self.skip_parameter("construction_parameters", "complete-actual-radial-not-available")
                self.skip_parameter("held_witnesses", "complete-actual-radial-not-available")
                for stage in STAGES[1:]:
                    self.skip(stage, "complete-actual-radial-required-before-first-construction")
                raise ConstructionUnavailable("No complete actual radial replay exists for this field")
            self.select_construction()
        elif name == "shared_field" and self.producer_completed(name, result):
            # These explicit points do not certify held separation and are not
            # a precondition for either independent geometric consumer.
            try:
                self.select_witnesses()
            except BaseException as error:
                self.report["witness_plan_error"] = dict(
                    type=type(error).__name__, message=str(error),
                    traceback=traceback.format_exc(), mathematical_rejection_not_inferred=True)
                self.report["witness_failure_does_not_gate_metric_or_reach"] = True
                self.persist()
        return result

    def finish(self):
        for row in self.report["parameter_actions"]:
            if not row["started"] and "unstarted_reason" not in row:
                row["unstarted_reason"] = "preceding-actual-dependency-or-procedure-stop"
        self.report["unstarted_parameter_action_names"] = [
            r["name"] for r in self.report["parameter_actions"] if not r["started"]]
        super().finish()


def main(argv=None):
    actions()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--input-sha256", required=True)
    args = parser.parse_args(argv)
    spec, original = read(args.input, args.input_sha256)
    validate_spec(spec)
    procedure = Procedure(spec, original)
    procedure.install()
    try:
        procedure.run()
    except BaseException as error:
        procedure.report["error"] = dict(type=type(error).__name__, message=str(error),
            traceback=traceback.format_exc(), mathematical_rejection_not_inferred=True)
    finally:
        procedure.finish()
    rid = receipt(procedure.out / "procedure.json")
    print(json.dumps(dict(event="R437-actual-parameter-block-postsolve-returned",
        schema=SCHEMA, original_result=rid,
        upstream_finite450_acceptance_observed=procedure.report["upstream_finite450_acceptance_observed"],
        unstarted_stage_names=procedure.report["unstarted_stage_names"],
        unstarted_parameter_action_names=procedure.report["unstarted_parameter_action_names"],
        all_owned_children_quiescent=procedure.report["all_owned_children_quiescent"],
        error=procedure.report["error"], cleanup_performed=False,
        complete_task_certified=False), ensure_ascii=True, separators=(",", ":")), flush=True)
    if procedure.signals:
        return 128 + procedure.signals[0]["number"]
    return 0 if procedure.report["error"] is None and procedure.report["all_owned_children_quiescent"] else 2


if __name__ == "__main__":
    raise SystemExit(main())

