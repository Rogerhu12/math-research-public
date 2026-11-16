#!/usr/bin/env python3
"""R464 R437/R452 first-definition registration for the complete-M material API.

This requestless consumer never creates a native/BVP/geometric acceptance.
The unique real inverse is part of the definition, not a tolerance-gated
numerical inverse.  Optional cell evaluation encloses that inverse and then
uses the complete source-bound R416/R441/R451 real-expression interpreter.  No field
arrays, old renderer, FFT reprojection or finite-Newton derivative replace it.

All defining arithmetic and optional evaluations belong to public Actions.
The caller supplies its existing absolute-clock/resource check; no clock is
started here.  No files are created/deleted and no process is started here.
Author: OpenAI ChatGPT /root/exact_refinement (AI), 2026-11-16.
Derived from the published R447 source; its existing 112 branches stay explicit.
"""
from __future__ import annotations

import copy
from fractions import Fraction as Q
import hashlib
import json
import math
import os
from pathlib import Path
import struct
import sys

REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "R464-current-C-incremental-M-common-material-phase-v1"
DEFINITION_SCHEMA = SCHEMA + "-definition"
CELL_SCHEMA = SCHEMA + "-complete-active-six-jets"
R437_SCHEMA = "R437-current-ten450-explicit-closed-parameter-policy-v1"
R437_SOURCE = "geometry_20261116_current_C_ten450_closed_parameter_policy.py"
R437_SHA = "d7d01460f5a22f4fa2ca75ad36475688d65a465ba488d9caff65cb5ef13fb871"
FIRST_RECORD_FAMILIES = {
    "original-R437": dict(schema=R437_SCHEMA, source=R437_SOURCE, sha256=R437_SHA),
    "actual202-R452": dict(schema="R452-actual202-ten450-explicit-closed-parameter-policy-v1",
        source="geometry_20261116_actual202_ten450_closed_parameter_policy.py", sha256="b49769f13f69bf30b82988b1ca57382c602d4b74bc3ae8a6c2b5d1e0ee3df7a8"),
}
ACTIVE_SOURCE = "geometry_20261115_shared_active_interval_balls.py"
ACTIVE_SHA = "675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b"
FIRST_SAVED_SOURCE = "geometry_20261115_continuous_ten_frozen450_saved_prefix.py"
FIRST_SAVED_SHA = "1c7a2e1c39b0066ae7149ef2e35ff6936a70601f0545369848f04716ad8b4520"
PHASE_RULE = ("For all real alpha, moving F_alpha(s,theta)=R_alpha F_0(s,theta-alpha); "
              "fixed caps are unchanged. alpha=pi*t/2 on t in [0,1].")
FAMILIES = {
    "R464-incremental-M": {'schema': 'R464-current-C-incremental-M-accurate-cut-atlas-field-v1',
 'cut_file': 'geometry_20261116_current_C_incremental_M_accurate_cut_patch.py',
 'cut_sha': '8105c8148d221b5ba10bc332631c88764d620dc59d30936bbe1067b6a54228e2',
 'saved_file': 'geometry_20261116_continuous_ten_incremental_M_saved_prefix.py',
 'saved_sha': '959b1a2b54fd0da8be14c2228d91ca1d1ef312966d6f4ba40be4bbeff4247ce9',
 'shared_file': 'geometry_20261116_current_C_incremental_M_shared_field.py',
 'shared_sha': '55a1fb95b574651bac6458034b5f85c46180172189d7a8010758e786087a4c04'},
    "R416-original-resolution": dict(
        schema="R416-current-C-ten450-accurate-cut-atlas-field-v1",
        cut_file="geometry_20261115_current_C_accurate_cut_patch.py",
        cut_sha="28417b93fc4fa7780e049ab7d8c4d98e4f51412afd1ced5fc36558ae1e0d837b",
        saved_file=FIRST_SAVED_SOURCE, saved_sha=FIRST_SAVED_SHA,
        shared_file="geometry_20261115_current_C_ten450_shared_field.py",
        shared_sha="6a5f949a0422d0a4794c270140a777af1b2e2f7c73f99ef99e0601fdc634d6f3"),
    "R441-current-resolution": dict(
        schema="R441-current-C-resolution450-accurate-cut-atlas-field-v1",
        cut_file="geometry_20261116_current_C_resolution_accurate_cut_patch.py",
        cut_sha="8811f89c7395bb4aed1adabe6c6825c801e1e41a9d80d416b0a4746596ae9a52",
        saved_file="geometry_20261116_continuous_ten_resolution_saved_prefix.py",
        saved_sha="fb6e181cd0ddfb34cc70c874c119ceb149850ce8756d1f2f0dd775175e99cffb",
        shared_file="geometry_20261116_current_C_ten450_resolution_shared_field.py",
        shared_sha="1ceda9d32cfcf50e28e737cd0aee981cb8dc2329027aa2967d08532a1ea6e935"),
    "R451-current-M": dict(
        schema="R451-current-C-complete-M-accurate-cut-atlas-field-v1",
        cut_file="geometry_20261116_current_C_M_accurate_cut_patch.py",
        cut_sha="747b9d1f77b307529aeb65e3ad31e831b9f54238916bcae23fa578efd6a76492",
        saved_file="geometry_20261116_continuous_ten_frozen_M_saved_prefix.py",
        saved_sha="86a88a66a57c05b64c21efa650374746ad42be272f0d741188ff81bdf4fed2f6",
        shared_file="geometry_20261116_current_C_ten_M_shared_field.py",
        shared_sha="db1f6fd39bef3d9ce2543276771cbcea1c2432a7221b8f295ed5b553b2171f87"),
}
JET_NAMES = ("value", "u", "q", "uu", "uq", "qq")
STRONGER_JETS = tuple((a, b) for a in range(3) for b in range(5-a))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
            "All defining arithmetic and field queries belong to this public Actions repository")


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=True, allow_nan=False) + "\n").encode("ascii")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def value_identity(value):
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


def same_payload(left, right):
    return (isinstance(left, dict) and isinstance(right, dict)
            and left.get("bytes") == right.get("bytes")
            and left.get("sha256") == right.get("sha256"))


def read_bound(path, expected):
    actual = receipt(path)
    if isinstance(expected, str):
        require(actual["sha256"] == expected, "Original file SHA differs: " + str(path))
    else:
        require(same_payload(actual, expected), "Original file bytes/SHA differ: " + str(path))
    return json.loads(Path(path).read_bytes()), actual


def exact(value):
    require(type(value) in (int, float, str, Q) and type(value) is not bool,
            "Use an exact rational text/integer or an explicitly defining finite binary64 word")
    if type(value) is float:
        require(math.isfinite(value), "A defining binary64 value must be finite")
        return Q.from_float(value)
    return Q(value)


def word(value):
    require(type(value) in (int, float) and math.isfinite(value),
            "Preserve an original finite JSON binary64 construction word")
    return struct.pack("<d", float(value)).hex()


def construction_words(plan):
    rows = plan["fixed_cap"]["markers"]
    require(isinstance(rows, list), "Keep the entire actual marker list")
    result = []
    for row in rows:
        require(set(row) == {"upper", "center", "radius", "height"}
                and type(row["upper"]) is bool and isinstance(row["center"], list)
                and len(row["center"]) == 2, "Keep each complete original marker")
        result.append(dict(upper=row["upper"],
            center_float64le=[word(v) for v in row["center"]],
            radius_float64le=word(row["radius"]), height_float64le=word(row["height"])))
    return dict(cut_correction_width_float64le=word(plan["cut_correction_width"]),
                cap_height_float64le=word(plan["cap_height"]), markers=result)


def module_identity(instance, filename, expected):
    """Follow the actual object's class module, not the first same-path import."""
    module = sys.modules.get(type(instance).__module__)
    require(module is not None and getattr(module, "__file__", None),
            "Keep the actual loaded class module")
    actual = receipt(module.__file__)
    require(Path(actual["file"]).name == filename and actual["sha256"] == expected,
            "Actual loaded object source differs: " + filename)
    return actual


def interval_pair(value, name):
    require(isinstance(value, (tuple, list)) and len(value) == 2,
            "Use a complete closed interval: " + name)
    a, b = map(exact, value)
    require(a <= b, "The exact interval is reversed: " + name)
    return a, b


def same_accurate_target(first_target, current_target, current_modes):
    """R442 representation fields are not a changed accurate scalar target.

    All remaining source-bound accurate C/root/factory/DAG/ten-word fields
    compare completely. The actual R442 driver and writer separately compare
    the full exported scalar specifications except field_modes/tail_modes.
    This does not transfer any old field or whole-surface certificate.
    """
    first = copy.deepcopy(first_target)
    current = copy.deepcopy(current_target)
    old_schema = "R400-current-continuous-C-ten-complete112-profile-and-freeze-binding-v1-same-point-identity"
    new_schema = "R442-current-continuous-C-ten-complete-M-profile-and-freeze-binding-v1-same-point-identity"
    require(first.pop("schema", None) == old_schema,
            "The first actual R437/R452 material record retains its complete112 target")
    current_schema = current.pop("schema", None)
    if current_schema == new_schema:
        require(current.pop("field_modes", None) == current_modes,
                "Current actual M target and complete loaded field dimensions differ")
    else:
        require(current_schema == old_schema and current_modes == 112
                and current_target == first_target,
                "The original registered112 branch keeps its unchanged complete identity")
    first.pop("complete_numeric_specification_sha256")
    current.pop("complete_numeric_specification_sha256")
    require(first == current,
            "Every remaining accurate target/C/root/factory/ten-word field must agree")
    return dict(common_accurate_target_identity=value_identity(first),
        first_actual_target_identity=value_identity(first_target),
        current_actual_target_identity=value_identity(current_target),
        first_field_modes=112, current_field_modes=current_modes,
        only_declared_M_representation_metadata_removed=(current_schema == new_schema),
        full_scalar_exports_compared_by_actual_R442_driver_and_writer=(current_schema == new_schema),
        old_field_metric_reach_or_held_certificate_transferred=False)


class MaterialAngle:
    """Exact full coefficients, and an optional outward Arb interpretation.

    theta(q) = Phi(2*pi*q).  beta is the already paid original rho lower
    bound, not a bound guessed from angle samples in this consumer.
    """
    def __init__(self, core, beta, identity):
        actions()
        self.core = tuple(map(exact, core))
        self.M = len(self.core)
        require(self.M > 0, "Keep every coefficient of the explicitly bound finite material family")
        self.beta = exact(beta)
        require(self.beta > 0, "The existing full-circle material-inverse premise remains unpaid")
        self.density = tuple((1-4*m*m)*v for m, v in enumerate(self.core, 1))
        self.sine = tuple(v/Q(2*m) for m, v in enumerate(self.density, 1))
        self.sine_bound = sum(map(abs, self.sine), Q(0))
        self.rho_upper = 1+sum(map(abs, self.density), Q(0))
        self.identity = copy.deepcopy(identity)

    @classmethod
    def from_first_definition(cls, definition, beta, identity, *, first_family):
        require(first_family in FIRST_RECORD_FAMILIES,
                "Use an explicit actual first-definition source family")
        selected = FIRST_RECORD_FAMILIES[first_family]
        require(definition.get("schema") == selected["schema"]+"-complete112-material-angle-definition-v1"
                and definition.get("coefficient_count") == 112
                and definition.get("frequencies") == [2*m for m in range(1, 113)]
                and definition.get("rounded_saved_density_not_substituted_for_exact_coefficients") is True,
                "Use the entire actual first R437/R452 material definition")
        words = definition["coefficient_float64le"]
        require(isinstance(words, list) and len(words) == 112,
                "Keep every first defining binary64 word")
        core = []
        for encoded in words:
            require(isinstance(encoded, str) and len(encoded) == 16,
                    "Keep the complete little-endian binary64 encoding")
            value = struct.unpack("<d", bytes.fromhex(encoded))[0]
            require(math.isfinite(value), "The first material coefficient must be finite")
            core.append(Q.from_float(value))
        require([str(v) for v in core] == definition["coefficient_exact_dyadics"]
                and [str((1-4*m*m)*v) for m, v in enumerate(core, 1)] ==
                    definition["exact_density_coefficients"]
                and [str(Q(1-4*m*m, 2*m)*v) for m, v in enumerate(core, 1)] ==
                    definition["exact_sine_coefficients"]
                and definition["exact_interpreter"] == dict(file=ACTIVE_SOURCE, sha256=ACTIVE_SHA)
                and definition["actual_prefix_loader"] ==
                    dict(file=FIRST_SAVED_SOURCE, sha256=FIRST_SAVED_SHA),
                "Bind the same exact coefficient interpretation, not rounded density coefficients")
        return cls(core, beta, identity)

    def describe(self):
        return dict(coefficient_count=self.M, core_definition_identity=self.identity,
            exact_rho_lower=str(self.beta), exact_global_rho_upper=str(self.rho_upper),
            exact_sine_absolute_sum=str(self.sine_bound),
            unique_real_inverse_defined=True, finite_Newton_map_used_as_exact_inverse=False,
            full_circle_positivity_is_original_loader_premise=True)

    def derivatives(self, Active, q, maximum=2):
        """All original modes, exact rational coefficients, no truncation."""
        require(type(maximum) is int and 0 <= maximum <= 4,
                "This explicit formula supports derivative orders zero through four")
        pi2 = 2*Active.arb.pi()
        theta = pi2*q
        d = [theta, pi2, Active.arb(0), Active.arb(0), Active.arb(0)]
        for m, density in enumerate(self.density, 1):
            a = Active.ball(density)
            frequency = 2*m
            phase = frequency*theta
            sine, cosine = phase.sin(), phase.cos()
            d[0] = d[0]+Active.ball(self.sine[m-1])*sine
            if maximum >= 1:
                d[1] = d[1]+pi2*a*cosine
            if maximum >= 2:
                d[2] = d[2]-pi2*pi2*frequency*a*sine
            if maximum >= 3:
                d[3] = d[3]-pi2**3*frequency**2*a*cosine
            if maximum >= 4:
                d[4] = d[4]+pi2**4*frequency**3*a*sine
        return tuple(d[:maximum+1])

    def global_derivative_interval(self, Active):
        result = (2*Active.arb.pi())*Active.interval(self.beta, self.rho_upper)
        require(Active.bounds(result)[0] > 0,
                "The current outward interpretation of the original positive denominator is unresolved")
        return result

    def inverse_enclosure(self, Active, target, max_steps, budget_check):
        """Finite inclusion refinement of the whole unique real inverse image.

        Every completed iterate remains a valid enclosure.  No width is an
        acceptance threshold.  No modulo/period branch is selected and no
        endpoint or midpoint is returned as an exact inverse value.
        """
        require(type(max_steps) is int and 0 <= max_steps <= 4096,
                "Use an explicit finite optional inverse-work count")
        require(callable(budget_check), "Reuse the host's original resource/absolute-clock check")
        budget_check()
        bracket = ((target+Active.interval(-self.sine_bound, self.sine_bound)) /
                   (2*Active.arb.pi()))
        lo, hi = Active.bounds(bracket)
        derivative = self.global_derivative_interval(Active)
        iterations, stop = 0, "explicit_optional_inverse_work_count"
        for index in range(max_steps):
            budget_check()
            centre = (lo+hi)/2
            value = self.derivatives(Active, Active.ball(centre), 0)[0]
            candidate = Active.ball(centre)+(target-value)/derivative
            left, right = Active.bounds(candidate)
            left, right = max(lo, left), min(hi, right)
            if left > right:
                raise ArithmeticError("Two sound closed inverse inclusions unexpectedly became disjoint")
            iterations = index+1
            if left == lo and right == hi:
                stop = "no_further_contraction_at_current_explicit_precision"
                break
            lo, hi = left, right
        budget_check()
        return Active.interval(lo, hi), dict(
            exact_inverse_closed_enclosure=[str(lo), str(hi)],
            initial_complete_inverse_enclosure=Active.encode_interval(bracket),
            exact_real_lift_no_period_branch_discarded=True,
            original_positive_derivative_bound=Active.encode_interval(derivative),
            finite_inclusion_iterations=iterations, requested_max_steps=max_steps, stop=stop,
            whole_unique_inverse_image_enclosed=True,
            inverse_value_selected_as_midpoint=False,
            inverse_resolution_or_machine_word_equality_claimed=False,
            optional_work_is_not_a_native_or_geometric_acceptance_gate=True)


class CommonMaterialPhase:
    """Bound first definition/current accurate field; no new scientific verdict.

    The caller has already used a registered R416/R441/R451 loader and owns every
    current field payload.  The first record, plan and assembly must still be
    actual available files; their hashes alone cannot reconstruct those files.
    The first record is explicitly the original R437 or actual202 R452 complete112 capture.
    The current R442/R451 branch removes only declared M representation fields;
    accurate C, root family, full scalar source/DAG and all ten words are fixed.
    Other cross-run or differently selected root equivalences are not inferred.
    """
    def __init__(self, current, first_material_transport, first_material_sha256,
                 first_plan, first_assembly, budget_check):
        actions()
        require(callable(budget_check), "Pass the host's original absolute-clock/resource check")
        self.check = budget_check
        self.check()
        choices = [(name, row) for name, row in FAMILIES.items()
                   if getattr(current, "schema", None) == row["schema"]]
        require(len(choices) == 1, "Use an explicitly bound current R416, R441 or complete-M R451 accurate bundle")
        self.family, family = choices[0]
        self.current = current
        sources = dict(current_cut=module_identity(current, family["cut_file"], family["cut_sha"]))
        require(same_payload(current.binding.get("source"), sources["current_cut"]),
                "The actual accurate bundle and its defining-source receipt differ")
        require(isinstance(current.source_bundle, (tuple, list)) and len(current.source_bundle) == 7,
                "Retain the complete loaded current seven-tuple")
        paths, plan, assembly, target, saved, A, bindings = current.source_bundle
        self.paths, self.plan, self.saved, self.field = paths, plan, saved, current.field
        require(current.field.saved is saved and current.field.A is A and A.saved is saved
                and A.plan is plan and type(current.field.M) is int and current.field.M > 0
                and current.field.M == saved.M == len(current.field.core) == len(saved.core),
                "Keep the actual field and every mode of its own complete finite owners")
        sources["current_saved"] = module_identity(saved, family["saved_file"], family["saved_sha"])
        sources["current_shared"] = module_identity(A, family["shared_file"], family["shared_sha"])
        self.Active = current.Active
        sources["complete_six_jet_interpreter"] = receipt(self.Active.__file__)
        require(Path(sources["complete_six_jet_interpreter"]["file"]).name == ACTIVE_SOURCE
                and sources["complete_six_jet_interpreter"]["sha256"] == ACTIVE_SHA,
                "Use the original complete exact six-jet interpreter")
        first, first_id = read_bound(first_material_transport, first_material_sha256)
        first_choices = [(name, row) for name, row in FIRST_RECORD_FAMILIES.items()
            if first.get("schema") == row["schema"]+"-actual-material-transport-record-v1"
            and first.get("source", {}).get("sha256") == row["sha256"]
            and Path(first.get("source", {}).get("file", "")).name == row["source"]]
        require(len(first_choices) == 1 and first.get("repository") == REPOSITORY
                and first.get("initial_capture") is True
                and first.get("definition_capture_complete") is True,
                "Consume one actual complete first R437/R452 transport record")
        first_family, first_source = first_choices[0]
        first_freeze_id = None
        if first_family == "actual202-R452":
            descriptor = first["first_construction_freeze"]
            freeze, first_freeze_id = read_bound(descriptor["file"], descriptor)
            require(freeze.get("schema") == first_source["schema"]+"-first-construction-freeze-v1"
                    and freeze.get("source", {}).get("sha256") == first_source["sha256"]
                    and Path(freeze.get("source", {}).get("file", "")).name == first_source["source"]
                    and freeze.get("repository") == REPOSITORY
                    and freeze.get("run_id") == os.environ["GITHUB_RUN_ID"]
                    and freeze.get("source_commit") == os.environ["GITHUB_SHA"]
                    and same_payload(freeze.get("original_deadline"), first["original_deadline"])
                    and same_payload(freeze.get("initial_checkpoint"), first["current_checkpoint"])
                    and freeze.get("current_target_identity") == first["current_target_identity"]
                    and freeze.get("complete_ten_float64le") == first["complete_ten_float64le"]
                    and freeze.get("complete_construction_words") == first["complete_construction_words"]
                    and construction_words(freeze["actual_construction"]) == first["complete_construction_words"]
                    and freeze.get("initial_complete112_material_definition") == first["complete112_material_definition"],
                    "Consume the actual R452 A and B together; do not synthesize either from a digest")
        cp = saved.checkpoint
        for value, label in ((first, "first transport"), (cp.manifest, "current checkpoint")):
            require(value.get("run_id") == os.environ["GITHUB_RUN_ID"]
                    and value.get("source_commit") == os.environ["GITHUB_SHA"],
                    "This explicit branch consumes real same-job data: " + label)
        first_files = first["actual_shared_expression_files"]
        first_plan_data, first_plan_id = read_bound(first_plan, first_files["plan"])
        first_assembly_data, first_assembly_id = read_bound(first_assembly, first_files["assembly"])
        first_prefix = first_assembly_data["large_core_prefix"]
        require(canonical(first_plan_data["large_core_prefix"]) == canonical(first_prefix)
                and first_prefix.get("source_sha256") == FIRST_SAVED_SHA
                and same_payload(first_prefix.get("complete_accepted_checkpoint"), first["current_checkpoint"])
                and first_prefix.get("material_circle_diffeomorphism_source") ==
                    "unchanged R237 complete-core rational triangle bound",
                "The first positive-material premise belongs to its actual original saved-prefix")
        fields = ("single_global_planar_registration", "inlet_normalization",
                  "mean_gauge", "core_and_hold_gauge")
        require(all(canonical(first[name]) == canonical(first_assembly_data[name]) for name in fields),
                "Preserve the full original first normalization/registration/gauge records")
        require(first["phase_rule"] == PHASE_RULE
                and first_plan_data.get("phase_rule") == PHASE_RULE
                and plan.get("phase_rule") == PHASE_RULE,
                "Keep the original physical-material-angle phase, not a substituted q shift")
        current_target = value_identity(cp.target_identity)
        first_target = first_prefix["current_target_identity"]
        require(first["current_target_identity"] == value_identity(first_target)
                and first["complete_ten_float64le"] == cp.manifest["complete_ten_float64le"],
                "Keep the complete actual first target receipt and all frozen ten words")
        target_comparison = same_accurate_target(first_target, cp.target_identity, self.field.M)
        first_construction = first["complete_construction_words"]
        require(construction_words(first_plan_data) == first_construction
                and construction_words(plan) == first_construction
                and word(first_plan_data["cuff"]) == word(plan["cuff"]),
                "Keep the complete first W/H/marker/cuff words, including negative zero")
        require(assembly["mean_gauge"]["whole_lower_sheet_reflected"] is True
                and assembly["core_and_hold_gauge"]["native_cap_rotation_axis_xy"] == [0., 0.],
                "Keep both reflected sheets and the original rotation axis")
        self.first_angle = MaterialAngle.from_first_definition(first["complete112_material_definition"],
            first_prefix["global_rho_lower_exact"],
            dict(record=first_id, exact_definition=value_identity(first["complete112_material_definition"]),
                 original_positive_bound_source=first_assembly_id), first_family=first_family)
        core = tuple(exact(v) for v in self.field.core)
        require(core == tuple(exact(float(v)) for v in saved.core)
                and exact(self.field.rho_lower) == exact(saved.rho_lower_exact),
                "Keep the current exact core and its original loader's positive bound")
        self.current_angle = MaterialAngle(core, self.field.rho_lower,
            dict(current_checkpoint=copy.deepcopy(cp.receipt),
                 complete_core_words=[word(float(v)) for v in saved.core],
                 actual_core_array_identity=copy.deepcopy(cp.arrays["array_identity"]["core"])))
        self.numeric_length = exact(self.field.x[-1])
        require(self.numeric_length > 0, "Keep the actual positive numerical prefix length")
        self.binding = dict(schema=SCHEMA, source=receipt(__file__), repository=REPOSITORY,
            run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
            current_family=self.family, registered_family=copy.deepcopy(family), sources=sources,
            actual_first_material_record=first_id, actual_first_plan=first_plan_id,
            actual_first_assembly=first_assembly_id,
            first_checkpoint_identity_only=copy.deepcopy(first["current_checkpoint"]),
            first_raw_checkpoint_and_other_payloads_read_here=False,
            current_checkpoint=copy.deepcopy(cp.receipt),
            current_accurate_binding_identity=value_identity(current.binding),
            current_target_identity=current_target,
            accurate_target_across_M=target_comparison,
            first_record_family=first_family, registered_first_record_source=copy.deepcopy(first_source),
            actual_first_construction_freeze=first_freeze_id,
            first_record_remains_complete112=True,
            first_record_remains_original_R437_complete112=(first_family == "original-R437"),
            first_record_is_actual_R452_complete112=(first_family == "actual202-R452"),
            current_field_modes=self.field.M,
            complete_ten_float64le=copy.deepcopy(cp.manifest["complete_ten_float64le"]),
            complete_construction_words=copy.deepcopy(first_construction),
            original_cuff_float64le=word(plan["cuff"]),
            first_material=self.first_angle.describe(), current_material=self.current_angle.describe(),
            original_current_numeric_prefix_length_exact=str(self.numeric_length),
            first_and_current_exact_core_equal=(self.first_angle.core == self.current_angle.core),
            first_and_current_core_equality_required=False,
            original_first_registration_and_gauge_identities={name:value_identity(first[name]) for name in fields},
            original_current_registration_and_gauge_identities={name:value_identity(assembly[name]) for name in fields},
            current_field_not_replaced_by_first_A_or_B=True,
            no_BVP_or_native_gate_changed=True, no_original_clock_restarted=True,
            original_metric_reach_held_certificates_not_manufactured=True)
        self.completed_queries = 0
        self.check()

    def describe(self):
        """Accurate definition contract, not a passed numerical certificate."""
        actions()
        self.check()
        return dict(schema=DEFINITION_SCHEMA, binding=copy.deepcopy(self.binding),
            optional_inverse_cell_queries_performed=self.completed_queries,
            shared_coordinate_definition="prefix u=s_numeric_current/L_numeric_current; original r elsewhere",
            material_definition="Theta_j(q)=Phi_j(2*pi*q), complete exact core; I_j is the unique real lift inverse",
            static_pullback="psi_j(q)=I_j(Theta_first(q)); caps use Cartesian identity",
            all_time_active_expression="R_alpha K_current(x,I_current(Theta_first(q)-alpha)), alpha=pi*t/2",
            common_q_is_not_shifted_directly=True,
            caps=dict(definition="(x,y,side*(H+b_side(x,y)))", unchanged_for_all_t=True,
                all_markers_in_binding=True, nonaxisymmetric_cap_rotation_symmetry_assumed=False,
                no_angular_inverse_extended_through_cap_centres=True),
            existing_cuff_and_all_radial_C2_gluing_premises_required=True,
            strong_C2_continuity=dict(scope="fixed actual current field, all t in [0,1]",
                required_spatial_derivative_order=2,
                time_twice_differentiable_into_C2_not_required_by_original_task=True,
                numerical_inverse_tolerance_not_an_acceptance_gate=True,
                across_refinement_C2_convergence_not_claimed=True,
                field_modes_may_differ_from_first_material_modes=True),
            conditional_certificate_transfer=dict(
                same_target="T_j^*g_j=g_first under complete accurate target/cap/gluing premises",
                Loewner="same eta under exact congruence; no new inverse tolerance test",
                whole_image="same current j,t image under static full-domain pullback",
                original_complete_certificate_actual_result_consumed=False,
                full_metric_reach_held_or_embedding_certified=False),
            optional_stronger_time_regularities=dict(
                original_required_six_jets=list(JET_NAMES),
                time_order_two_into_spatial_C2_requires_raw_jets=[list(v) for v in STRONGER_JETS],
                current_theta_derivative_order=4, first_theta_derivative_order=2,
                stronger_high_jet_values_produced=False,
                stronger_property_added_as_scientific_gate=False),
            actual_full_closed_sweep_performed=False, any_raw_payload_created_or_deleted=False)

    def _positive_current_derivative(self, q):
        Active = self.Active
        values = self.current_angle.derivatives(Active, q, 2)
        local = Active.bounds(values[1])
        global_interval = self.current_angle.global_derivative_interval(Active)
        global_bounds = Active.bounds(global_interval)
        lo, hi = max(local[0], global_bounds[0]), min(local[1], global_bounds[1])
        if lo > hi or lo <= 0:
            raise ArithmeticError("Original positive derivative and current complete local enclosure are incompatible")
        formed = Active.interval(lo, hi)
        if Active.bounds(formed)[0] <= 0:
            formed = global_interval
        return formed, values[2]

    def evaluate_active_cell(self, piece_index, radial, angular, time_interval, lower,
                             *, interval_bits, max_inverse_steps):
        """Enclose every spatial six-jet value on one complete closed cell.

        radial means common u for a prefix piece, and original r otherwise.
        angular is common first q in [0,1].  time_interval is the original
        t in [0,1], not alpha.  Raw result values are Arb objects owned by
        this same Actions process; the caller decides its necessary readback.
        No cell is accepted on inverse width, curvature, merit or a new gate.
        """
        actions()
        require(type(piece_index) is int and 0 <= piece_index < len(self.field.pieces),
                "Select one actual complete current piece")
        require(type(lower) is bool and type(interval_bits) is int and 64 <= interval_bits <= 8192,
                "Use an explicit side and original interval work precision")
        x0, x1 = interval_pair(radial, "radial/public-u")
        q0, q1 = interval_pair(angular, "first-material-q")
        t0, t1 = interval_pair(time_interval, "original-time")
        require(0 <= q0 <= q1 <= 1 and 0 <= t0 <= t1 <= 1,
                "Keep both closed common-circle endpoints and the original complete time range")
        piece = self.field.pieces[piece_index]
        scale = self.numeric_length if piece["kind"] == "prefix" else Q(1)
        r0, r1 = scale*x0, scale*x1
        require(piece["left"] <= r0 <= r1 <= piece["right"],
                "The common-coordinate cell must map into its actual complete original piece")
        Active = self.Active
        old_precision = Active.ctx.prec
        self.check()
        try:
            Active.ctx.prec = interval_bits
            q = Active.interval(q0, q1)
            alpha = Active.arb.pi()*Active.interval(t0, t1)/2
            first = self.first_angle.derivatives(Active, q, 2)
            target = first[0]-alpha
            inverse, inverse_record = self.current_angle.inverse_enclosure(
                Active, target, max_inverse_steps, self.check)
            denominator, second = self._positive_current_derivative(inverse)
            zq = first[1]/denominator
            zqq = (first[2]-second*zq*zq)/denominator
            raw_angle = Active.bounds(inverse)
            self.check()
            # The original exact expression uses integer trigonometric modes
            # and a complete material lift.  It is defined for every real q.
            # Calling field directly retains that full real lift, instead of
            # folding a box or discarding a q=0/1 seam at the bundle wrapper.
            raw = self.field.evaluate(piece, (r0, r1), raw_angle, lower)
            require(len(raw) == 3 and all(len(v.d) == 6 for v in raw),
                    "The current original expression must return every vector six-jet slot")
            vectors = tuple(tuple(component.d[k] for component in raw) for k in range(6))
            factor = Active.ball(scale)
            unrotated = (
                vectors[0],
                tuple(factor*v for v in vectors[1]),
                tuple(zq*v for v in vectors[2]),
                tuple(factor*factor*v for v in vectors[3]),
                tuple(factor*zq*v for v in vectors[4]),
                tuple(zq*zq*a+zqq*b for a,b in zip(vectors[5], vectors[2])),
            )
            cosine, sine = alpha.cos(), alpha.sin()
            def rotate(v):
                return (cosine*v[0]-sine*v[1], sine*v[0]+cosine*v[1], v[2])
            jets = {name:rotate(v) for name,v in zip(JET_NAMES, unrotated)}
            self.check()
            self.completed_queries += 1
            return dict(schema=CELL_SCHEMA,
                binding_identity=value_identity(self.binding),
                completed_query_ordinal=self.completed_queries-1,
                actual_piece_index=piece_index, actual_piece=copy.deepcopy(piece), lower=lower,
                first_coordinate="public-u" if piece["kind"] == "prefix" else "original-radius",
                closed_input_radial=[str(x0),str(x1)],
                original_evaluator_radial=[str(r0),str(r1)],
                radial_chain_factor_exact=str(scale),
                closed_common_q=[str(q0),str(q1)], closed_original_time=[str(t0),str(t1)],
                actual_interval_bits=interval_bits, exact_phase="alpha=pi*t/2",
                alpha_enclosure=Active.encode_interval(alpha),
                inverse=inverse_record,
                material_q_first_derivative=Active.encode_interval(zq),
                material_q_second_derivative=Active.encode_interval(zqq),
                six_jets=jets, current_complete_modes_and_both_means_retained=True,
                original_current_accurate_expression_used=True,
                rounded_renderer_or_finite_Newton_derivative_used=False,
                finite_Fourier_reprojection_after_composition=False,
                full_closed_coverage_or_geometric_acceptance=False)
        finally:
            Active.ctx.prec = old_precision

    def encode_active_cell(self, result):
        """Explicit serialization for the host's current temporary output.

        This does not print, split, upload, or write a scientific payload.
        It does not choose a summary cap or remove any derivative slot.
        """
        actions()
        require(result.get("schema") == CELL_SCHEMA, "Use this actual bound six-jet result")
        self.check()
        encoded = copy.deepcopy({key:value for key,value in result.items() if key != "six_jets"})
        encoded["six_jets"] = {name:[self.Active.encode_interval(v) for v in result["six_jets"][name]]
                               for name in JET_NAMES}
        for key in ("left", "right"):
            if key in encoded["actual_piece"]:
                encoded["actual_piece"][key] = str(encoded["actual_piece"][key])
        return encoded


def bind_loaded_common_material(current, *, first_material_transport,
                                first_material_sha256, first_plan, first_assembly,
                                budget_check):
    """No new solver, clock, process, output directory or acceptance test."""
    return CommonMaterialPhase(current, first_material_transport,
        first_material_sha256, first_plan, first_assembly, budget_check)
