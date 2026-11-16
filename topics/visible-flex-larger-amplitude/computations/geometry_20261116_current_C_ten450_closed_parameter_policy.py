#!/usr/bin/env python3
"""R437: explicit first-field cap parameters and same-word mesh reuse.

This independent, requestless Actions helper runs only after a genuine current
full450 checkpoint.  Its initial construction action consumes the complete
original R409 radial replay, before R413 needs W/H/markers.  A mesh successor
reuses the first chosen words; it never reselects H from the refined solution.
The witness action records the first actual material definition/registration
and resolves the declared core points in the actual R416 table. Reuse consumes
that real first definition, but does not pretend to apply a common-angle
pullback when the current solved core changes.
No BVP, metric, reach, held or existence acceptance is created here.
Author: AI, 2026-11-16.
"""

import argparse
import copy
from fractions import Fraction as Q
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
import traceback
from types import SimpleNamespace

REPO = "Rogerhu12/math-research-public"
SCHEMA = "R437-current-ten450-explicit-closed-parameter-policy-v1"
INPUT_SCHEMA = SCHEMA + "-input-v1"
POLICY_SCHEMA = SCHEMA + "-recipe-v1"
FREEZE_SCHEMA = SCHEMA + "-first-construction-freeze-v1"
MATERIAL_SCHEMA = SCHEMA + "-complete112-material-angle-definition-v1"
TRANSPORT_SCHEMA = SCHEMA + "-actual-material-transport-record-v1"
CONSTRUCTION_SCHEMA = "R413-current-C-original-cuff-target-atlas-binding-v1-construction-v1"
WITNESS_SCHEMA = "R425-current-accurate-active-quarter-turn-witness-plan-v1"
ORIGINS = {
    "original193-frozen450": dict(
        schema="current-C-continuous-ten-full453-frozen450-owned-process-launch-v1",
        source_sha256="6ff21118040ad4006ae8170923996ee11e34163ce38fc460dd6aa23f972fcd66",
        deadline_schema="request193-owned-job-science-deadline-v1"),
    "joint203-frozen450": dict(
        schema="current-C-continuous-ten-joint-full453-frozen450-owned-process-launch-v1",
        source_sha256="cb05724bbedf71951524d187d242c1783d244bc729241ec91a91e0a9cf8f02d7",
        deadline_schema="request203-owned-job-science-deadline-v1"),
}
SHARED = "geometry_20261115_current_C_ten450_shared_field.py"
CHECKPOINT = "geometry_20261115_continuous_ten_frozen450_checkpoint.py"
CUT = "geometry_20261115_current_C_accurate_cut_patch.py"
ATLAS = "geometry_20261115_current_C_original_cuff_target_atlas.py"
CAPS = "geometry_20261115_current_C_ten450_fixed_cap_balls.py"
SAVED = "geometry_20261115_continuous_ten_frozen450_saved_prefix.py"
ACTIVE = "geometry_20261115_shared_active_interval_balls.py"
PINS = {
    SHARED: "6a5f949a0422d0a4794c270140a777af1b2e2f7c73f99ef99e0601fdc634d6f3",
    CHECKPOINT: "43f217d1722b9420fad4ba2f507467dda2e28e0a0b61c38adf8db013840e8dae",
    CUT: "28417b93fc4fa7780e049ab7d8c4d98e4f51412afd1ced5fc36558ae1e0d837b",
    ATLAS: "02bb0c70198c54e4ebe8d0fa2ebb6f74d0b17a6193378b0169746926a3b52fd2",
    CAPS: "0ff1fa60a619a7df8e58e72e240dc42e99850eacd05b6426cc70e9083f76afae",
    SAVED: "1c7a2e1c39b0066ae7149ef2e35ff6936a70601f0545369848f04716ad8b4520",
    ACTIVE: "675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b",
}
GEOMETRIC_INTERPRETATION = dict(
    exact_active_field="R416 accurate-C cut patch on the complete current R409 seven-tuple",
    prefix_and_material="R400 complete112 SavedPrefix with original R248 material transport and R249 inlet normalization",
    upper_background_sigma=-1,
    phase="R_alpha F_0(s,theta-alpha), alpha=pi*t/2; fixed caps unchanged",
    cap="F_side=(x,y,side*(H+b_side)); every supplied marker contributes",
    original_target="Same complete accurate C-DAG target and all ten literal parameter words",
    material_scope="First complete112 core/Phi and actual registration/normalization retained; same W/H/markers alone does not prove common-chart full closed metric identity",
    source_sha256=PINS,
)
LIMIT = 90000


def require(condition, message):
    if not condition:
        raise ValueError(message)


def actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPO,
            "All field arithmetic belongs to this public repository Actions")


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=True, allow_nan=False) + "\n").encode("ascii")


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def receipt(path):
    path = Path(path).resolve(strict=True)
    h, count = hashlib.sha256(), 0
    with path.open("rb") as stream:
        for part in iter(lambda: stream.read(1048576), b""):
            count += len(part)
            h.update(part)
    return dict(file=str(path), bytes=count, sha256=h.hexdigest())


def same_payload(a, b):
    return (isinstance(a, dict) and isinstance(b, dict)
            and a.get("bytes") == b.get("bytes")
            and a.get("sha256") == b.get("sha256"))


def value_identity(value):
    raw = canonical(value)
    return dict(canonical_bytes=len(raw), canonical_sha256=digest(raw))


def read(path, expected=None, small=False):
    path = Path(path).resolve(strict=True)
    rid = receipt(path)
    require(expected is None or rid["sha256"] == expected, "Actual file SHA differs: " + str(path))
    require(not small or rid["bytes"] <= LIMIT, "Use one original small parameter document")
    return json.loads(path.read_bytes()), rid


def write(path, value):
    path = Path(path)
    raw = canonical(value)
    with path.open("xb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    return receipt(path)


def contained(path, namespace, exists=True):
    path = Path(path).resolve(strict=exists)
    require(path != namespace and path.is_relative_to(namespace),
            "Use an actual child of the same owned RUNNER_TEMP namespace")
    return path


def same_run(value):
    require(value.get("run_id") == os.environ["GITHUB_RUN_ID"]
            and value.get("source_commit") == os.environ["GITHUB_SHA"],
            "Keep the actual same-job run/source identity")


def load(computations, name):
    path = Path(computations) / name
    rid = receipt(path)
    require(rid["sha256"] == PINS[name], "Frozen source differs: " + name)
    module_name = "_r437_actual_" + name[:-3]
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        sys.modules.pop(module_name, None)
        raise
    return module


def exact(value):
    require(type(value) in (int, float) and math.isfinite(value),
            "Retain a finite JSON binary64 number")
    return Q(value) if type(value) is int else Q.from_float(value)


def word(value):
    return struct.pack("<d", float(value)).hex()


def construction_words(value):
    """Negative zero and every supplied marker word remain visible."""
    require(set(value) == {"cut_correction_width", "cap_height", "fixed_cap"}
            and isinstance(value["fixed_cap"], dict)
            and set(value["fixed_cap"]) == {"markers"}, "Keep only the complete R413 constructor fields")
    exact(value["cut_correction_width"])
    exact(value["cap_height"])
    require(isinstance(value["fixed_cap"]["markers"], list), "Keep the entire marker list")
    rows = []
    for row in value["fixed_cap"]["markers"]:
        require(isinstance(row, dict) and set(row) == {"upper", "center", "radius", "height"}
                and type(row["upper"]) is bool and isinstance(row["center"], list)
                and len(row["center"]) == 2, "Keep each side, full center, radius and amplitude")
        for v in row["center"] + [row["radius"], row["height"]]:
            exact(v)
        rows.append(dict(upper=row["upper"], center_float64le=[word(v) for v in row["center"]],
                         radius_float64le=word(row["radius"]), height_float64le=word(row["height"])))
    return dict(cut_correction_width_float64le=word(value["cut_correction_width"]),
                cap_height_float64le=word(value["cap_height"]), markers=rows)


def material_definition(cp):
    """Exact R675 expression defined by the actual112 saved binary64 words.

    This is defining-data extraction, not evaluation of sin, a field jet,
    a material inverse, a metric bound, or a comparison acceptance gate.
    """
    core = [float(v) for v in cp.arrays["core"]]
    require(len(core) == 112 and all(math.isfinite(v) for v in core),
            "Keep all actual112 material coefficients")
    return dict(schema=MATERIAL_SCHEMA,
        coefficient_count=112, frequencies=[2*m for m in range(1, 113)],
        coefficient_float64le=[word(v) for v in core],
        coefficient_exact_dyadics=[str(exact(v)) for v in core],
        exact_density_coefficients=[str((1-4*m*m)*exact(v))
                                    for m, v in enumerate(core, 1)],
        exact_sine_coefficients=[str(Q(1-4*m*m, 2*m)*exact(v))
                                 for m, v in enumerate(core, 1)],
        formula="Phi(phi)=phi+sum(((1-4*m*m)*Q(core[m-1])/(2*m))*sin(2*m*phi),m=1..112); phi=2*pi*q",
        exact_interpreter=dict(file=ACTIVE, sha256=PINS[ACTIVE]),
        actual_prefix_loader=dict(file=SAVED, sha256=PINS[SAVED]),
        rounded_saved_density_not_substituted_for_exact_coefficients=True,
        current_solved_core_not_determined_only_by_scalar_ten_words=True)


class ResourceStop(RuntimeError):
    pass


class ExternalStop(RuntimeError):
    pass


class Context:
    def __init__(self, spec, input_id, out):
        self.spec, self.out = spec, out
        self.start = time.monotonic()
        self.handlers = {}
        self.report = dict(schema=SCHEMA, source=receipt(__file__), repository=REPO,
            run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
            input=input_id, operation=spec["operation"], completed=False, returned=False,
            error=None, resource_partial=False, external_interruption=False,
            new_BVP_or_geometric_acceptance=False, original_scientific_thresholds_changed=False,
            same_global_clock_restarted=False, any_raw_payload_deleted=False,
            cleanup_allowed=False, outputs={}, pending=[spec["operation"]])

    def interrupted(self, number, frame):
        self.report["signal"] = dict(number=int(number), name=signal.Signals(number).name)
        raise ExternalStop("Observed original owned-child interruption")

    def bind(self):
        s = self.spec
        require(s.get("schema") == INPUT_SCHEMA, "Use the independent R437 input schema")
        require(s["operation"] in ("initial-construction", "reuse-construction", "held-witnesses"),
                "Select one explicit parameter operation")
        temp = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
        self.namespace = contained(s["namespace"], temp)
        require(self.out.is_relative_to(self.namespace), "Keep the output in the original namespace")
        self.computations = Path(s["computations"]).resolve(strict=True)
        self.policy, policy_id = read(s["policy"], s["policy_sha256"], small=True)
        require(self.policy.get("schema") == POLICY_SCHEMA, "Keep the complete explicit parameter policy")
        require(self.policy.get("geometric_interpretation") == GEOMETRIC_INTERPRETATION,
                "Freeze the actual source interpretation as well as W/H/marker words")
        origin_dir = contained(s["origin_launch_directory"], self.namespace)
        origin, origin_id = read(origin_dir / "result.json", s["origin_result_sha256"])
        same_run(origin)
        candidates = [(name, row) for name, row in ORIGINS.items()
                      if origin.get("schema") == row["schema"]
                      and origin.get("source_sha256") == row["source_sha256"]]
        require(len(candidates) == 1,
                "Use an explicitly registered original193 or joint203 launch")
        origin_kind, origin_contract = candidates[0]
        require(origin.get("current_finite_BVP_accepted") is True
                and origin.get("completed_driver_return") is True
                and origin.get("actual_child_exit") == 0
                and origin.get("owned_group_quiescent_before_readback") is True
                and origin.get("resource_stop") is None
                and origin.get("external_interruption") is None,
                "The original complete453/fresh450 origin and owned quiet state remain required")
        deadline_path = contained(s["job_deadline"], self.namespace)
        deadline, did = read(deadline_path, s["job_deadline_sha256"])
        same_run(deadline)
        require(same_payload(did, origin.get("actual_job_deadline"))
                and deadline.get("schema") == origin_contract["deadline_schema"]
                and deadline.get("recipe_sha256") == origin.get("recipe", {}).get("sha256")
                and deadline.get("science_seconds_from_namespace") == 18900
                and deadline.get("readback_reserve_seconds") == 2700,
                "Use the exact original 18900+2700 namespace clock receipt")
        start = deadline.get("namespace_created_unix_seconds")
        require(type(start) in (int, float) and math.isfinite(start) and start > 0,
                "The original namespace start time is an actual finite value")
        self.absolute_deadline = start + deadline["science_seconds_from_namespace"]
        seconds = s["resources"]["budget_seconds"]
        reserve = s["resources"]["free_bytes_reserve"]
        require(type(seconds) in (int, float) and math.isfinite(seconds) and seconds > 0
                and type(reserve) is int and reserve >= 0, "Explicit finite parameter work resources required")
        self.local_seconds, self.free_bytes = seconds, reserve
        self.report.update(policy=policy_id, original_launch=origin_id, original_deadline=did,
            actual_origin_kind=origin_kind, actual_origin_contract=origin_contract,
            original_deadline_values=deadline, explicit_resources=s["resources"],
            absolute_science_deadline_unix_seconds=self.absolute_deadline)
        self.check()
        for sig in (signal.SIGTERM, signal.SIGINT):
            self.handlers[sig] = signal.signal(sig, self.interrupted)
        C = load(self.computations, CHECKPOINT)
        cpdir = contained(s["checkpoint_directory"], self.namespace)
        cp = C.Checkpoint(cpdir, s["checkpoint_sha256"], self.computations).require_frozen450()
        same_run(cp.manifest)
        self.cp, self.cpdir = cp, cpdir
        self.material = material_definition(cp)
        self.target_id = value_identity(cp.target_identity)
        self.cuff_value = cp.target_identity["original_complete_C_input_binding"]["physical_parameters"]["rCuff"]
        require(type(self.cuff_value) is float, "Retain the original current-C binary64 cuff word")
        self.cuff = exact(self.cuff_value)
        self.report.update(actual_checkpoint=cp.receipt, current_target_identity=self.target_id,
            complete_ten_float64le=cp.manifest["complete_ten_float64le"],
            complete_ten_exact_dyadics=cp.manifest["complete_ten_exact_dyadics"],
            original_cuff=dict(value=self.cuff_value, float64le=word(self.cuff_value), exact=str(self.cuff)),
            actual_driver_source=cp.manifest["actual_driver_source"],
            actual_complete112_material_definition_identity=value_identity(self.material),
            actual_complete112_core_array_identity=cp.arrays["array_identity"]["core"],
            material_pullback_or_conjugacy_executed=False,
            same_closed_g_not_inferred_from_construction_equality=True,
            source_pins={name:receipt(self.computations / name) for name in PINS})
        for name, record in self.report["source_pins"].items():
            require(record["sha256"] == PINS[name], "Frozen direct source differs: " + name)
        self.check()

    def check(self):
        if time.time() >= self.absolute_deadline or time.monotonic()-self.start >= self.local_seconds:
            raise ResourceStop("Original absolute clock or explicit parameter-work allowance exhausted")
        if shutil.disk_usage(self.out).free < self.free_bytes:
            raise ResourceStop("Original owned temporary disk reserve reached")

    def emit_construction(self, construction):
        words = construction_words(construction)
        value = dict(construction, schema=CONSTRUCTION_SCHEMA,
                     checkpoint_sha256=self.cp.receipt["sha256"], cuff=self.cuff_value)
        rid = write(self.out / "r413-construction.json", value)
        self.report["outputs"]["r413_construction"] = rid
        self.report["actual_construction"] = construction
        self.report["complete_construction_words"] = words

    def initial(self):
        p, s, cp = self.policy, self.spec, self.cp
        require(p["construction"]["height_rule"] == "first-current-shared-B-at-native-inner-then-RN64",
                "Use the explicitly selected new cap-height rule")
        require(p["construction"]["width_binary64_decimal"] == "0.01"
                and p["construction"]["marker_scale_exact_text"] == "1/160"
                and p["construction"]["marker_rule"] == "original-four-weak-marker-operation-order",
                "Keep the disclosed old free choices and their actual operation order")
        Shared = load(self.computations, SHARED)
        # Only original R409 modules and its exact radial packet/FFT routine
        # are reused.  No SavedPrefix second jets or new BVP are requested.
        np, Saved, Background, Parity, sources = Shared.runtime(self.computations)
        radial_dir = contained(s["radial_directory"], self.namespace)
        replay = Shared.CurrentRadialReadout(radial_dir, s["radial_result_sha256"], cp, np)
        self.check()
        M = 112
        require(cp.arrays["physical"].shape[1] == 338 and len(cp.arrays["core"]) == M,
                "Keep all original physical rows and all112 core coefficients")
        core = [Q.from_float(float(v)) for v in cp.arrays["core"]]
        state = [Q.from_float(float(v)) for v in cp.arrays["physical"][-1, 2*M+1:]]
        require(len(state) == M+1, "Retain z0 and all112 terminal z coefficients")
        mean = state[0] + sum((Q(1-4*m*m, 2)*core[m-1]*state[m]
                              for m in range(1, M+1)), Q(0))
        coefficients = replay.defining_node_coefficients(len(replay.rows)-1)
        tail_mean = Q.from_float(float(coefficients[0, 0, 2].real))
        sigma = Q(-1)
        offset = mean - sigma*tail_mean
        bg_cut = exact(replay.rows[-1]["backgroundRKInnerAnchor"])
        bg_inner = exact(replay.rows[0]["backgroundRKInnerAnchor"])
        height_exact = offset - sigma*(bg_cut-bg_inner)
        height = float(height_exact)
        require(math.isfinite(height), "The declared binary64 cap datum did not form finitely")
        cuff, k = self.cuff_value, float(Q(p["construction"]["marker_scale_exact_text"]))
        width = float(p["construction"]["width_binary64_decimal"])
        centers = [[cuff/2, 0.], [0., cuff/2], [-cuff/2, 0.], [0., 0.]]
        markers = [dict(upper=(i < 4), center=centers[i-1], radius=cuff/(8*i),
                        height=k*cuff*cuff/512) for i in range(1, 5)]
        construction = dict(cut_correction_width=width, cap_height=height,
                            fixed_cap=dict(markers=markers))
        words = construction_words(construction)
        self.check()
        selected = dict(schema=FREEZE_SCHEMA, source=receipt(__file__), repository=REPO,
            run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
            policy=self.report["policy"], original_deadline=self.report["original_deadline"],
            initial_checkpoint=cp.receipt, current_target_identity=self.target_id,
            complete_ten_float64le=cp.manifest["complete_ten_float64le"],
            original_cuff=self.report["original_cuff"], actual_construction=construction,
            complete_construction_words=words,
            initial_complete112_material_definition=self.material,
            initial_core_array_identity=cp.arrays["array_identity"]["core"],
            initial_fullDN_member=cp.manifest["members"]["fullDN"],
            geometric_interpretation=copy.deepcopy(GEOMETRIC_INTERPRETATION),
            actual_R409_runtime_sources=sources,
            selected_initial_driver_source=cp.manifest["actual_driver_source"],
            complete_current_radial_result=receipt(radial_dir / "result.json"),
            complete_current_radial_metadata=receipt(replay.complete_path),
            height_selection=dict(rule=p["construction"]["height_rule"],
                complete112_terminal_mean_exact=str(mean), cut_radial_DC_exact=str(tail_mean),
                upper_sigma_exact=str(sigma), shared_offset_exact=str(offset),
                original_background_cut_exact=str(bg_cut), original_background_inner_exact=str(bg_inner),
                first_native_inner_radius_exact=str(exact(float(replay.r[0]))),
                pre_round_cap_height_exact=str(height_exact), chosen_cap_height=height,
                chosen_cap_height_float64le=word(height), chosen_cap_height_exact=str(exact(height)),
                projection_difference_Qbinary64_minus_selected_exact=str(exact(height)-height_exact),
                no_positive_height_nudge_or_hidden_fallback=True,
                nonzero_support_center_determinant_or_held_ratio_not_claimed=True),
            weak_marker_scale=dict(exact_text=p["construction"]["marker_scale_exact_text"],
                actual_binary64=k, actual_float64le=word(k), actual_exact_dyadic=str(exact(k))),
            choice_is_new_geometric_experiment_not_old_height_transfer=True,
            old_R24_example_not_a_current_reach_certificate=True,
            future_mesh_reuses_every_construction_word=True,
            shared_registration_and_inlet_normalization_not_yet_produced=True,
            full_closed_g_reuse_still_requires_actual_common_material_pullback=True,
            all_original_domain_metric_reach_held_and_final_responsibilities_unpaid=True)
        fid = write(self.out / "first-construction-freeze.json", selected)
        self.report["outputs"]["first_construction_freeze"] = fid
        self.report["height_selection"] = selected["height_selection"]
        self.report["weak_marker_scale"] = selected["weak_marker_scale"]
        self.emit_construction(construction)

    def first_construction(self):
        s = self.spec
        path = contained(s["first_construction_freeze"], self.namespace)
        first, fid = read(path, s["first_construction_freeze_sha256"], small=True)
        same_run(first)
        require(first.get("schema") == FREEZE_SCHEMA
                and same_payload(first.get("source"), receipt(__file__))
                and same_payload(first.get("original_deadline"), self.report["original_deadline"])
                and same_payload(first.get("policy"), self.report["policy"]),
                "Reuse the original same-source choice on the same original clock")
        require(first.get("current_target_identity") == self.target_id
                and first.get("complete_ten_float64le") == self.cp.manifest["complete_ten_float64le"]
                and first.get("original_cuff") == self.report["original_cuff"]
                and first.get("geometric_interpretation") == GEOMETRIC_INTERPRETATION,
                "A mesh successor freezes the complete same ten target and original cuff")
        construction = copy.deepcopy(first["actual_construction"])
        require(construction_words(construction) == first["complete_construction_words"],
                "Every actual H/W/side/center/radius/amplitude word remains unchanged")
        require(first["initial_complete112_material_definition"]["schema"] == MATERIAL_SCHEMA,
                "Consume the complete actual first material definition")
        return first, fid, construction

    def first_transport(self, first, fid):
        s = self.spec
        path = contained(s["first_material_transport"], self.namespace)
        old, oid = read(path, s["first_material_transport_sha256"])
        same_run(old)
        require(old.get("schema") == TRANSPORT_SCHEMA
                and same_payload(old.get("source"), receipt(__file__))
                and same_payload(old.get("first_construction_freeze"), fid)
                and same_payload(old.get("original_deadline"), self.report["original_deadline"])
                and old.get("definition_capture_complete") is True
                and old.get("initial_capture") is True
                and old.get("complete112_material_definition") ==
                    first["initial_complete112_material_definition"],
                "Consume the actual complete first material/registration record, not its old digest alone")
        for key in ("single_global_planar_registration", "inlet_normalization",
                    "mean_gauge", "core_and_hold_gauge", "phase_rule"):
            require(key in old, "Keep the original first shared-field definition: " + key)
        return old, oid

    def reuse(self):
        first, fid, construction = self.first_construction()
        old, oid = self.first_transport(first, fid)
        self.report.update(first_construction_freeze=fid,
            first_material_transport=oid,
            no_new_height_or_marker_reselection=True,
            first_height_selection_identity=value_identity(first["height_selection"]),
            original_initial_checkpoint=first["initial_checkpoint"],
            first_material_definition_identity=value_identity(old["complete112_material_definition"]),
            first_and_current_core_words_equal=(old["complete112_material_definition"][
                "coefficient_float64le"] == self.material["coefficient_float64le"]),
            first_material_definition_really_read=True,
            current_R409_still_uses_current_solved_core=True,
            material_word_difference_is_not_a_solver_or_geometry_rejection=True,
            actual_common_material_pullback_still_unpaid=True)
        self.emit_construction(construction)

    def capture_material_transport(self, current):
        """Save real first data; later compare records without imposing equality.

        Original normalization includes current field-dependent data and may
        be large. It stays in the owned temporary record; only its identity,
        origin and explicit scope enter the necessary summary.
        """
        s = self.spec
        paths, plan, assembly, target, saved, A, bindings = current.source_bundle
        first, fid, construction = self.first_construction()
        require(construction_words({key: plan[key] for key in
                    ("cut_correction_width", "cap_height", "fixed_cap")}) ==
                    first["complete_construction_words"],
                "The actual shared field consumes every first construction word")
        mode = s["construction_mode"]
        require(mode in ("initial-construction", "reuse-construction"),
                "The material capture states its actual construction branch")
        initial = mode == "initial-construction"
        if initial:
            require(same_payload(first["initial_checkpoint"], self.cp.receipt)
                    and first["initial_complete112_material_definition"] == self.material,
                    "First material capture belongs to the actual first checkpoint")
        fields = ("single_global_planar_registration", "inlet_normalization",
                  "mean_gauge", "core_and_hold_gauge")
        record = dict(schema=TRANSPORT_SCHEMA, source=receipt(__file__), repository=REPO,
            run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
            original_deadline=self.report["original_deadline"],
            first_construction_freeze=fid, current_checkpoint=self.cp.receipt,
            current_target_identity=self.target_id,
            complete_ten_float64le=self.cp.manifest["complete_ten_float64le"],
            complete_construction_words=first["complete_construction_words"],
            complete112_material_definition=self.material,
            actual_core_array_identity=self.cp.arrays["array_identity"]["core"],
            actual_shared_expression_files={key: receipt(path) for key, path in paths.items()},
            accurate_R416_binding_identity=value_identity(current.binding),
            phase_rule=copy.deepcopy(plan["phase_rule"]),
            definition_capture_complete=True, initial_capture=initial,
            material_pullback_or_conjugacy_executed=False,
            whole_closed_same_g_not_certified=True,
            whole_record_equality_is_metadata_not_an_extra_scientific_gate=True,
            **{key: copy.deepcopy(assembly[key]) for key in fields})
        comparisons = None
        if not initial:
            old, oid = self.first_transport(first, fid)
            comparisons = dict(first_material_transport=oid,
                complete_first_material_definition_consumed=True,
                complete112_core_words_equal=(old["complete112_material_definition"][
                    "coefficient_float64le"] == self.material["coefficient_float64le"]),
                original_record_equal={key: old[key] == record[key] for key in
                    fields + ("phase_rule",)},
                differing_provenance_not_interpreted_as_a_mathematical_difference=True,
                same_C_and_ten_and_construction_not_a_common_chart_certificate=True,
                current_R409_still_uses_current_material_definition=True,
                actual_common_material_pullback_unpaid=True,
                any_comparison_false_does_not_gate_original_scientific_consumers=True)
            record["comparison_to_real_first_transport"] = comparisons
        name = "first-material-transport.json" if initial else "current-material-transport.json"
        rid = write(self.out / name, record)
        self.report["outputs"]["first_material_transport" if initial else "current_material_transport"] = rid
        self.report["actual_material_transport"] = dict(
            original_record=rid, first_construction_freeze=fid,
            initial_capture=initial, complete112_material_definition_identity=value_identity(self.material),
            original_shared_field_definition_identities={key: value_identity(record[key])
                for key in fields + ("phase_rule",)},
            definition_capture_complete=True, comparisons=comparisons,
            full_closed_g_reuse_still_requires_actual_common_material_pullback=True,
            no_field_or_target_was_replaced_by_the_first_records=True)

    def witnesses(self):
        s = self.spec
        rule = self.policy["witnesses"]
        require(rule == dict(rule="actual-core-zero-physical-cardinal-upper",
                             radial_exact="0", physical_q_exact=["0", "1/4", "1/2", "3/4"], lower=False),
                "Keep the complete declared finite witness set without outcome-based selection")
        Cut, Atlas = load(self.computations, CUT), load(self.computations, ATLAS)
        directory = contained(s["shared_directory"], self.namespace)
        atlas_path = contained(s["cuff_atlas"], self.namespace)
        atlas, aid = read(atlas_path, s["cuff_atlas_sha256"])
        resolution = s["witness_resolution"]
        require(isinstance(resolution, dict) and set(resolution) == {"interval_bits", "sqrt_bits"}
                and type(resolution["interval_bits"]) is int
                and 64 <= resolution["interval_bits"] <= 8192
                and type(resolution["sqrt_bits"]) is int
                and 16 <= resolution["sqrt_bits"] <= 4096,
                "Use explicit original interval/square-root work parameters")
        args = SimpleNamespace(computations=self.computations, directory=directory,
            result_sha256=s["shared_result_sha256"], checkpoint_directory=self.cpdir,
            proof_directory=Path(s["proof_directory"]).resolve(strict=True),
            interval_bits=resolution["interval_bits"],
            sqrt_bits=resolution["sqrt_bits"])
        current = Cut.load_accurate_cut_field(args)
        attached = Atlas.bind_loaded_shared_bundle(current.source_bundle, atlas)
        require(same_payload(current.source_bundle[4].checkpoint.receipt, self.cp.receipt),
                "Resolve points on this actual current accepted450 field")
        self.capture_material_transport(current)
        candidates = [(i, piece) for i, piece in enumerate(current.field.pieces)
                      if piece["kind"] == "prefix" and piece["left"] == Q(0)]
        require(len(candidates) == 1 and candidates[0][1]["right"] > 0,
                "Resolve the genuine positive first core cell, not an old mesh vertex index")
        index, piece = candidates[0]
        points = [dict(piece_index=index, radial=rule["radial_exact"], q=q, lower=rule["lower"])
                  for q in rule["physical_q_exact"]]
        self.check()
        plan = dict(schema=WITNESS_SCHEMA, points=points)
        pid = write(self.out / "r425-witness-plan.json", plan)
        self.report.update(actual_current_shared_result=receipt(directory / "result.json"),
            actual_R413_atlas=aid, same_field_attachment_identity=value_identity(attached),
            accurate_R416_binding_identity=value_identity(current.binding),
            resolved_actual_piece=dict(index=index, kind=piece["kind"],
                exact_left=str(piece["left"]), exact_right=str(piece["right"])),
            complete_explicit_witness_points=points,
            explicit_witness_resolution=resolution,
            no_field_point_enclosure_or_Hausdorff_distance_computed_here=True,
            whole_image_lower_bound_still_requires_original_R425_cover=True)
        self.report["outputs"]["r425_witness_plan"] = pid

    def run(self):
        self.bind()
        if self.spec["operation"] == "initial-construction":
            self.initial()
        elif self.spec["operation"] == "reuse-construction":
            self.reuse()
        else:
            self.witnesses()
        self.check()
        self.report.update(completed=True, pending=[])

    def finish(self):
        for number, handler in self.handlers.items():
            signal.signal(number, handler)
        self.report.update(returned=True, elapsed_seconds=time.monotonic()-self.start)
        result = write(self.out / "result.json", self.report)
        raw = canonical(self.report)
        if len(raw) > LIMIT:
            fallback = dict(schema=SCHEMA+"-necessary-over-budget-v1", actual_result=result,
                actual_necessary_bytes=len(raw), hard_limit=LIMIT,
                complete_parameter_readback=False, original_operation_completed=self.report["completed"],
                pending=self.report["pending"], error_identity=value_identity(self.report["error"]),
                cleanup_allowed=False, raw_retained=True)
            write(self.out / "necessary-over-budget.json", fallback)
            print(json.dumps(fallback, ensure_ascii=True, separators=(",", ":")), flush=True)
            return 70
        nid = write(self.out / "necessary-summary.json", self.report)
        print("BEGIN_R437_CLOSED_PARAMETER_NECESSARY", flush=True)
        print(raw.decode("ascii"), end="", flush=True)
        print("END_R437_CLOSED_PARAMETER_NECESSARY", flush=True)
        print(json.dumps(dict(event="R437-necessary-summary-identity", **nid),
                         ensure_ascii=True, separators=(",", ":")), flush=True)
        if self.report["external_interruption"]:
            return 128+self.report["signal"]["number"]
        if self.report["resource_partial"]:
            return 75
        return 0 if self.report["completed"] else 2


def main(argv=None):
    actions()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--input-sha256", required=True)
    args = parser.parse_args(argv)
    spec, iid = read(args.input, args.input_sha256, small=True)
    temp = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    namespace = contained(spec["namespace"], temp)
    out = contained(spec["out"], namespace, exists=False)
    require(not out.exists(), "Use a fresh owned parameter-output directory")
    for key in ("computations", "origin_launch_directory", "checkpoint_directory", "radial_directory",
                "shared_directory", "proof_directory"):
        if key in spec:
            source = Path(spec[key]).resolve(strict=True)
            require(source != out and not source.is_relative_to(out), "Output may not own an input tree")
    out.mkdir(parents=True)
    context = Context(spec, iid, out)
    try:
        context.run()
    except BaseException as error:
        context.report.update(error=dict(type=type(error).__name__, message=str(error),
            traceback=traceback.format_exc(), no_mathematical_impossibility_inferred=True),
            resource_partial=isinstance(error, ResourceStop),
            external_interruption=isinstance(error, ExternalStop))
    return context.finish()


if __name__ == "__main__":
    raise SystemExit(main())
