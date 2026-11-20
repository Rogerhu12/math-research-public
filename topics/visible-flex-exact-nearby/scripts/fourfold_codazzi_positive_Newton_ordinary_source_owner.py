"""Public one-shot owner of seven new complete positive Newton source bounds.

Restore and read only the original7296 raw container and4650 coefficient
container, plus complete successful small receipts. The old core, germ,
whole7721 source, delta envelope, Green, and inverse targets are never run.
Scientific imports occur only after whole metadata admission.
"""
from __future__ import annotations

import argparse
import ast
import copy
from fractions import Fraction
import gzip
import hashlib
import importlib.metadata
import importlib.util
import json
import os
from pathlib import Path
import platform
import sys
import time
import traceback

REPOSITORY = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
KIND = "complete_selected_member_positive_Newton_ordinary_source_v1"
MANIFEST_KIND = "complete_positive_Newton_ordinary_source_inputs_v1"
PROBLEM_ID = "R141_complete_positive_Newton_source_d10_v1"
MATH_NAME = "fourfold_codazzi_positive_Newton_ordinary_source_math.py"
RUNTIME = {"Python": "3.12.14", "python_flint": "0.9.0"}
PARAMETERS = {
    "arithmetic_bits": 320,
    "exact_new_tail": ["9/10", "25/8"],
    "old_core": ["0", "9/10"],
    "new_complete_positive_interval": ["true_original_root", "25/8"],
    "exact_true_root_interval": [
        "1191984371497/5000000000000",
        "2383968743003/10000000000000",
    ],
    "exact_direction_radius": "1/10000000000",
    "old_direction_envelope_radius": "1/100000000",
    "direction_envelope_scale": "1/100",
    "selected_member_run": "43588332723/1",
    "selected_member_loss": "1/250",
    "selected_parameter_absolute_upper": "0.00000000009368259853002",
    "selected_parameter_not_replaced_by_a_numeric_point": True,
    "exact_amplitude": "6890507429876859/9007199254740992",
    "exact_eta0": "-7789843107295549/4611686018427387904",
    "exact_nu0": "-2572625729470897/72057594037927936",
    "centre_definition": "440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47",
    "direction_definition": "6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04",
    "centre_repair_pair_A0": "0.000000000000000003861",
    "centre_repair_pair_A1": "0.00000000000000001970",
    "ordinary_radial_measure": "dr",
    "ordinary_angle_measure": "normalized original moving circle",
    "source_pair_norm": "Euclidean L2 with full independent even mean",
    "raw_rows": 7296,
    "raw_interfaces": 6143,
    "positive_rows": 4650,
    "positive_interfaces": 3594,
    "old_Z_rows": 7721,
    "old_core_germ_or_whole_Z_targets_recomputed": 0,
    "new_scalar_count": 7,
    "new_raw_tail_and_positive_tail_only": True,
    "source_support_last_quarter_index": 288,
    "unknown_solution_has_no_finite_angular_support_assumption": True,
    "scientific_wall_cap_seconds": 900,
    "single_threads": True,
}
TARGETS = (
    "new_outer_tail_raw_physical_residual_L2_upper",
    "new_outer_tail_continuous_centre_repair_L2_upper",
    "new_outer_tail_selected_nonlinear_remainder_L2_upper",
    "complete_outer_tail_selected_Newton_full_L2_upper",
    "complete_positive_selected_Newton_full_L2_upper",
    "complete_positive_selected_Newton_low193_L2_upper",
    "complete_positive_selected_Newton_high97_through288_L2_upper",
)
GATES = (
    "pinned_manifest_contract",
    "all_current_inputs_and_new_AST_exact",
    "seven_historical_parts_and_two_exact_containers",
    "old_CRA_execution_and_whole_core_bound",
    "old_Z_finish_execution_and_full_mean_source",
    "old_full_delta_body_execution_and_linear_envelopes",
    "same_selected_NIF_and_WOBSA_whole_receipts",
    "all7296_raw_rows_and6143_interfaces",
    "all4650_positive_rows_and3594_interfaces",
    "same_definitions_uniform_member_and_true_root_restriction",
    "declared_single_threads_and_pinned_public_runtime",
    "new_tail_metadata_partitions_complete",
    "whole_old_eight_balls_directed_read_only",
    "new_raw_tail_integral_complete",
    "new_positive_tail_repair_and_remainder_complete",
    "all_seven_targets_saved_readback_contains",
    "full_low_high_compatible_source_domains",
    "all_unpaid_boundary_inverse_and_RHS_scope_retained",
)
REQUIRED_ROLES = (
    "science",
    "math_core",
    "positive_Newton_source_proof",
    "raw_parts_index",
    "positive_parts_index",
    "core_actual",
    "core_execution",
    "z_summary",
    "z_process",
    "body_summary",
    "body_process",
    "nif_actual",
    "wobsa_actual",
    "body_delta_source",
    "core_actual_proof",
    "core_reuse_proof",
    "selected_residual_proof",
    "repair_proof",
    "nif_proof",
    "actual_physical_source_pair_proof",
)
RETAINED_SCOPE = {
    "same_selected_member_by_uniform_restriction_only": True,
    "selected_delta_is_not_zero_or_the_radius_point": True,
    "uniform_delta10_source_does_not_extend_WOBSA_to_a_conjugacy_family": True,
    "same_repaired_centre_direction_fixed_eta0_and_nu_delta": True,
    "full_independent_even_mean_and_physical_frequency4_retained": True,
    "true_root_and_whole_positive_interval_retained_via_old_core_restriction": True,
    "raw_physical_amplitude_applied_once_only": True,
    "original_closed_row_suprema_and_true_intersection_lengths_retained": True,
    "no_old_upper_subtraction_or_integral_length_ratio": True,
    "only_direction_delta_envelopes_scaled_by_one_over100": True,
    "centre_repair_is_not_scaled_by_parameter_radius": True,
    "old_whole7721_full_low_high_records_read_unchanged": True,
    "all_existing_core_Z_mean_and_continuity_fees_paid_once": True,
    "known_f0_is_low193_but_unknown_solution_is_not_truncated": True,
    "known_selected_high_source_through288_is_not_zeroed": True,
    "source_minus_f_delta_is_not_a_solution_or_inverse_bound": True,
    "independent_negative_root_and_interface_inputs_still_unpaid": True,
    "actual_Robin_physical_mean_and_height_residual_values_still_unpaid": True,
    "R141_low_inverse_and_complete_physical_outer_gate_not_claimed": True,
    "future224_future32_and_both_WPN_rhs_not_created": True,
    "no_old_producer_imports_or_old_scientific_targets": True,
    "no_new_arrays_artifacts_or_Releases": True,
}
NATIVES = {
    "raw": {
        "bytes": 4592623,
        "sha256": "6f52030b7954f049a8e42a5a513a1f69b553819065b0c8b2245fa173e514cbb1",
        "parts": 3,
    },
    "positive": {
        "bytes": 6223338,
        "sha256": "ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d",
        "parts": 4,
    },
}
SCIENTIFIC_FIELDS = (
    "actual_mathematical_wall_seconds", "actual_progress", "actual_returncode",
    "actual_scientific_checkout_commit", "all_saved_records_readback_verified",
    "automatic_scientific_retry", "complete", "complete_metadata",
    "complete_new_scalar_records", "complete_new_source_conclusion",
    "copied_old_source_records", "current_input_receipts", "failure",
    "gates", "input_manifest_sha256", "kind", "metadata_admission_complete",
    "new_arrays_published", "new_artifacts", "new_Releases",
    "old_numerical_producers_called", "old_scientific_source_imports",
    "old_successful_targets_recomputed", "parameters", "problem_id", "proved",
    "repository", "restoration_receipts", "retained_scope", "runtime",
    "run_attempt", "run_id", "saved_record_count", "source_sha256",
    "target_order", "whole_old_evidence",
)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False)+"\n").encode("utf-8")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def git_blob(raw):
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def parse(raw):
    return json.loads(raw, parse_constant=lambda value: (_ for _ in ()).throw(
        ValueError("nonfinite JSON token: "+value)))


def atomic(path, raw):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".tmp")
    with temporary.open("wb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)
    require(path.read_bytes() == raw, "complete atomic result did not read back")


def complete(document, gates):
    return (document.get("complete") is True
            and document.get("failure") is None
            and len(document.get("gates", [])) == gates
            and all(g.get("passed") is True for g in document["gates"]))


def load_native(path, expected):
    raw = Path(path).read_bytes()
    require(len(raw) == expected["bytes"] and sha(raw) == expected["sha256"],
            "whole restored native byte identity differs")
    require(raw[:2] == b"\x1f\x8b",
            "original complete compressed container was silently replaced")
    return parse(gzip.decompress(raw))


def load_new_math(path):
    spec = importlib.util.spec_from_file_location("_new_positive_Newton_source_math", path)
    require(spec is not None and spec.loader is not None,
            "new pure definition module has no loader")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class DirectedAPI:
    def __init__(self, arb):
        self.arb = arb

    def rational(self, value):
        value = Fraction(value)
        return self.arb(value.numerator)/value.denominator

    def old_interval(self, record):
        if isinstance(record, dict):
            if isinstance(record.get("lower"), str) and isinstance(record.get("upper"), str):
                value = self.arb(record["lower"]).lower().union(
                    self.arb(record["upper"]).upper())
            elif isinstance(record.get("ball"), str):
                value = self.arb(record["ball"])
            else:
                raise ValueError("old scalar lacks its whole interval")
        else:
            require(isinstance(record, str), "old scalar is not saved text")
            value = self.arb(record)
        require(value.is_finite(), "nonfinite complete saved interval")
        return value

    def upper(self, value):
        require(value.is_finite(), "nonfinite new directed expression")
        return value.upper()

    def magnitude(self, value):
        return self.upper(abs(value))

    def sqrt_upper(self, value):
        value = self.upper(value)
        require(value >= 0, "new nonnegative square root is unresolved")
        return self.upper(value.sqrt())

    def record(self, value):
        value = self.upper(value)
        return {"ball": value.str(80)}


def execute(args):
    root = Path(args.repo).resolve()
    output = Path(args.out)
    start = time.monotonic()
    math_start = None
    api = None
    document = {
        "kind": KIND, "repository": REPOSITORY, "problem_id": PROBLEM_ID,
        "input_manifest_sha256": args.manifest_sha,
        "source_sha256": sha(Path(__file__).read_bytes()),
        "run_id": os.environ.get("GITHUB_RUN_ID"),
        "run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT"),
        "actual_scientific_checkout_commit": os.environ.get("CURRENT_SCIENCE_COMMIT"),
        "parameters": copy.deepcopy(PARAMETERS),
        "retained_scope": copy.deepcopy(RETAINED_SCOPE),
        "runtime": None, "gates": [], "current_input_receipts": [],
        "restoration_receipts": None, "whole_old_evidence": {},
        "metadata_admission_complete": False, "complete_metadata": None,
        "copied_old_source_records": {},
        "target_order": list(TARGETS), "complete_new_scalar_records": {},
        "complete_new_source_conclusion": None,
        "actual_progress": {
            "stage": "not_started",
            "new_raw_tail_intersections": 0,
            "new_positive_tail_intersections": 0,
            "completed_targets": 0,
            "current_target": None,
            "last_whole_prefix_metadata": None,
            "unfinished_accumulator_prefix": {},
        },
        "saved_record_count": 0,
        "all_saved_records_readback_verified": False,
        "old_numerical_producers_called": 0,
        "old_scientific_source_imports": 0,
        "old_successful_targets_recomputed": 0,
        "new_arrays_published": 0, "new_artifacts": 0, "new_Releases": 0,
        "automatic_scientific_retry": False,
        "actual_mathematical_wall_seconds": 0,
        "actual_returncode": None, "complete": False, "proved": False,
        "failure": None,
    }

    def save():
        require(sorted(document) == sorted(SCIENTIFIC_FIELDS),
                "scientific result outer fields changed")
        if math_start is not None:
            document["actual_mathematical_wall_seconds"] = time.monotonic()-math_start
        raw = canonical(document)
        require(len(raw) <= 60000, "complete scalar result exceeds its fixed small cap")
        atomic(output, raw)

    def gate(name, ok=True):
        require(name == GATES[len(document["gates"])], "new admission gates reordered")
        document["gates"].append({"name": name, "passed": bool(ok)})
        save()
        require(ok, "new source gate failed: "+name)

    def wall_guard():
        require(time.monotonic()-start < PARAMETERS["scientific_wall_cap_seconds"],
                "fixed new source wall cap; complete saved prefix retained")

    try:
        save()
        require(os.environ.get("GITHUB_ACTIONS") == "true"
                and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
                "scientific numerical evaluation belongs to the authorized public Actions only")
        raw_manifest = Path(args.manifest).read_bytes()
        manifest = parse(raw_manifest)
        gate(GATES[0],
             sha(raw_manifest) == args.manifest_sha
             and manifest["kind"] == MANIFEST_KIND
             and manifest["repository"] == REPOSITORY
             and manifest["problem_id"] == PROBLEM_ID
             and manifest["parameters"] == PARAMETERS
             and manifest["runtime"] == RUNTIME
             and manifest["scope"] == RETAINED_SCOPE
             and manifest["scientific_kind"] == KIND
             and tuple(manifest["target_order"]) == TARGETS
             and tuple(manifest["gate_order"]) == GATES
             and sorted(manifest["allowed_scientific_fields"]) == sorted(SCIENTIFIC_FIELDS))
        by_role, contents = {}, {}
        for item in manifest["files"]:
            role, relative = item["role"], item["path"]
            require(role not in by_role
                    and relative.startswith(TOPIC+"/")
                    and all(part not in ("", ".", "..") for part in relative.split("/")),
                    "duplicate or unsafe current input role")
            path = (root/relative).resolve()
            require(path.is_relative_to(root), "current input left the repository")
            raw = path.read_bytes()
            require(len(raw) == item["bytes"] and sha(raw) == item["sha256"]
                    and git_blob(raw) == item["git_blob_sha"],
                    "whole current input identity differs: "+role)
            raw.decode("utf-8")
            if relative.endswith(".py"):
                ast.parse(raw, filename=relative)
            by_role[role] = item
            contents[role] = raw
            document["current_input_receipts"].append(copy.deepcopy(item))
        gate(GATES[1],
             len(by_role) == manifest["expected_current_input_count"]
             and set(REQUIRED_ROLES).issubset(by_role)
             and by_role["science"]["sha256"] == document["source_sha256"]
             and Path(by_role["math_core"]["path"]).name == MATH_NAME)
        restored = parse(Path(args.restoration_receipts).read_bytes())
        historical = manifest["historical_inputs"]
        require(len(historical) == 7
                and len({item["role"] for item in historical}) == 7,
                "only the exact three raw and four positive historical parts are allowed")
        receipts = restored["original_parts"]
        require(len(receipts) == 7, "complete seven-part restore receipts missing")
        receipt_by_role = {item["role"]: item for item in receipts}
        require(len(receipt_by_role) == 7, "historical receipts repeat a role")
        for item in historical:
            actual = receipt_by_role.get(item["role"])
            require(actual is not None
                    and all(actual.get(key) == item[key]
                            for key in ("path", "commit", "bytes", "sha256")),
                    "an original historical part receipt differs")
            if "git_blob_sha" in item:
                require(actual.get("git_blob_sha") == item["git_blob_sha"],
                        "an original historical blob receipt differs")
        for name, expected in NATIVES.items():
            actual = restored["restored_natives"][name]
            require(actual["bytes"] == expected["bytes"]
                    and actual["sha256"] == expected["sha256"]
                    and actual["parts"] == expected["parts"],
                    "two exact whole-container restoration identities differ")
        raw = load_native(args.raw, NATIVES["raw"])
        positive = load_native(args.positive, NATIVES["positive"])
        document["restoration_receipts"] = copy.deepcopy(restored)
        gate(GATES[2])

        old = {role: parse(contents[role]) for role in (
            "core_actual", "core_execution", "z_summary", "z_process",
            "body_summary", "body_process", "nif_actual", "wobsa_actual")}
        core, ce = old["core_actual"], old["core_execution"]
        cr = ce["scientific_conclusion"]
        gate(GATES[3],
             complete(core, 18) and core["proved"] is True
             and core["actual_returncode"] == 0
             and str(ce["run_id"]) == "43757468943"
             and str(ce["run_attempt"]) == "1"
             and ce["complete"] is True and ce["actual_returncode"] == 0
             and cr["complete"] is True and cr["actual_returncode"] == 0
             and cr["actual_gate_count"] == 18 and cr["actual_passed_gate_count"] == 18
             and cr["bytes"] == by_role["core_actual"]["bytes"]
             and cr["sha256"] == by_role["core_actual"]["sha256"])
        z, zp = old["z_summary"], old["z_process"]
        gate(GATES[4],
             complete(z, 6) and zp["complete"] is True and zp["phase"] == "finish"
             and str(zp["run_id"]) == "43613560173"
             and str(zp["run_attempt"]) == "1"
             and zp["actual_scientific_gates"] == 6
             and zp["complete_native_sha256"] ==
                 "365f0763d8f4c87182507c4372a3be055624607a77d818a084471b368b33d32e"
             and z["native_sha256"] == zp["complete_native_sha256"]
             and len(zp["children"]) == 1
             and zp["children"][0]["actual_returncode"] == 0
             and z["complete_source_bounds"] == zp["complete_source_bounds"])
        body, bp = old["body_summary"], old["body_process"]
        gate(GATES[5],
             complete(body, 11) and bp["complete"] is True
             and str(bp["run_id"]) == "43615531666"
             and str(bp["run_attempt"]) == "1"
             and bp["complete_native_sha256"] ==
                 "1f3e5fa630f39a667a96102f103ac8977d00e580f698a83904f361c5a05c6f3c"
             and body["native_sha256"] == bp["complete_native_sha256"]
             and bp["actual_full_delta_positive_closed_rows"] == 4650
             and bp["exact_real_delta_radius"] == "1/100000000"
             and len(bp["children"]) == 2
             and all(child["actual_returncode"] == 0 for child in bp["children"]))
        gate(GATES[6], complete(old["nif_actual"], 16)
             and complete(old["wobsa_actual"], 18)
             and old["wobsa_actual"]["parameters"]["same_selected_member_only"] is True
             and old["wobsa_actual"]["retained_scope"]["same_selected_member_same_physical_eta0"] is True)
        math = load_new_math(root/by_role["math_core"]["path"])
        require(math.KIND == KIND and math.TARGETS == TARGETS,
                "new pure mathematical contract differs")
        admitted = math.admit_metadata(raw, positive, core, z, body,
                                       old["nif_actual"], old["wobsa_actual"])
        gate(GATES[7])
        gate(GATES[8])
        gate(GATES[9])
        document["metadata_admission_complete"] = True
        document["complete_metadata"] = copy.deepcopy(admitted["metadata"])
        document["whole_old_evidence"] = {
            role: {
                "whole_file_identity": copy.deepcopy(by_role[role]),
                "complete": old[role].get("complete"),
                "kind": old[role].get("kind"),
                "whole_gates": copy.deepcopy(old[role].get("gates")),
                "retained_scope": copy.deepcopy(old[role].get("retained_scope")),
            }
            for role in ("core_actual", "z_summary", "body_summary", "nif_actual", "wobsa_actual")
        }
        runtime = {"Python": platform.python_version(),
                   "python_flint": importlib.metadata.version("python-flint")}
        document["runtime"] = runtime
        gate(GATES[10], runtime == RUNTIME
             and all(os.environ.get(key) == "1"
                     for key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS")))
        gate(GATES[11], admitted["raw_tail"] and admitted["positive_tail"]
             and admitted["raw_tail"][0][0] == Fraction("9/10")
             and admitted["raw_tail"][-1][1] == Fraction("25/8")
             and admitted["positive_tail"][0][0] == Fraction("9/10")
             and admitted["positive_tail"][-1][1] == Fraction("25/8"))
        # The only scientific import is after complete byte/process/partition admission.
        from flint import arb, ctx
        ctx.prec = 320
        api = DirectedAPI(arb)
        math_start = time.monotonic()
        copied = {
            "CRA_complete_choice": copy.deepcopy(admitted["core_choice"]),
            "CRA_complete_quadratic_contribution": copy.deepcopy(admitted["core_quadratic"]),
            "Z_complete_full_body": copy.deepcopy(admitted["z_whole"]),
            "full_delta_body_complete_input_envelopes": copy.deepcopy(admitted["direction_whole"]),
        }
        # Three core, three source and two direction bounds, all from the
        # same whole choices. No low/full upper bounds are subtracted.
        eight = [
            admitted["core_choice"]["uniform_selected_full_L2_upper"],
            admitted["core_choice"]["uniform_selected_low193_L2_upper"],
            admitted["core_quadratic"],
            *[admitted["z_whole"][species]["L2_L2_radial"]
              for species in ("full_through160", "low193", "high97_through160")],
            admitted["direction_whole"]["A0"],
            admitted["direction_whole"]["angular_A0"],
        ]
        for record in eight:
            require(api.upper(api.old_interval(record)) >= 0,
                    "old whole scientific upper is not nonnegative")
        document["copied_old_source_records"] = copied
        gate(GATES[12], len(eight) == 8)

        def progress(stage, metadata, accumulators):
            wall_guard()
            require(stage in ("new_raw_tail_prefix", "new_coefficient_tail_prefix"),
                    "undeclared new scientific stage")
            document["actual_progress"]["stage"] = stage
            document["actual_progress"]["last_whole_prefix_metadata"] = copy.deepcopy(metadata)
            document["actual_progress"]["unfinished_accumulator_prefix"] = {
                key: api.record(value) for key, value in accumulators.items()}
            target = TARGETS[0] if stage == "new_raw_tail_prefix" else TARGETS[1]
            document["actual_progress"]["current_target"] = target
            if stage == "new_raw_tail_prefix":
                document["actual_progress"]["new_raw_tail_intersections"] = metadata["completed_intersections"]
            else:
                document["actual_progress"]["new_positive_tail_intersections"] = metadata["completed_intersections"]
            save()
            print(json.dumps({"stage": stage, **metadata}, sort_keys=True), flush=True)

        def emit(name, value):
            wall_guard()
            count = document["saved_record_count"]
            require(count < len(TARGETS) and name == TARGETS[count],
                    "new complete source targets repeated or reordered")
            if count == 0:
                gate(GATES[13],
                     document["actual_progress"]["new_raw_tail_intersections"] ==
                     len(admitted["raw_tail"]))
            elif count == 1:
                gate(GATES[14],
                     document["actual_progress"]["new_positive_tail_intersections"] ==
                     len(admitted["positive_tail"]))
            original_upper = api.upper(value)
            proposed = api.record(original_upper)
            require(api.old_interval(proposed).contains(original_upper),
                    "complete decimal serialization does not contain original upper")
            document["complete_new_scalar_records"][name] = proposed
            document["saved_record_count"] += 1
            document["actual_progress"]["completed_targets"] = document["saved_record_count"]
            document["actual_progress"]["current_target"] = (
                TARGETS[document["saved_record_count"]]
                if document["saved_record_count"] < len(TARGETS) else None)
            save()
            reread = parse(output.read_bytes())
            saved_record = reread["complete_new_scalar_records"][name]
            require(saved_record == proposed, "saved complete scalar record changed")
            saved_ball = api.old_interval(saved_record)
            require(saved_ball.contains(original_upper),
                    "saved/read-back complete scalar lost outward containment")
            print(json.dumps({"complete_new_scalar": name,
                              "saved_complete_record": saved_record}, sort_keys=True), flush=True)
            return api.upper(saved_ball)

        conclusion = math.complete_bounds(api, raw, positive, admitted, emit, progress)
        gate(GATES[15],
             document["saved_record_count"] == len(TARGETS)
             and list(document["complete_new_scalar_records"]) == list(TARGETS)
             and conclusion["complete"] is True)
        document["all_saved_records_readback_verified"] = True
        gate(GATES[16],
             conclusion["independent_even_mean_retained"] is True
             and conclusion["known_centre_residual_last_quarter_index"] == 96
             and conclusion["known_complete_selected_source_last_quarter_index"] == 288
             and conclusion["high_source_is_not_set_to_zero"] is True)
        gate(GATES[17],
             conclusion["future224_or32_records_created"] is False
             and conclusion["physical_boundary_Robin_mean_height_values_proved"] is False
             and conclusion["two_WPN_rhs_completed"] is False
             and conclusion["full_inverse_proved"] is False
             and conclusion["nonlinear_solution_proved"] is False
             and document["old_successful_targets_recomputed"] == 0)
        document["complete_new_source_conclusion"] = conclusion
        document["complete"] = True
        document["proved"] = True
        document["actual_returncode"] = 0
        document["actual_progress"]["stage"] = "complete"
        document["actual_progress"]["current_target"] = None
        document["actual_progress"]["unfinished_accumulator_prefix"] = {}
        save()
    except BaseException as exc:
        document["failure"] = {
            "type": type(exc).__name__,
            "message": str(exc),
            "traceback": traceback.format_exc()[-12000:],
            "complete_saved_scalar_prefix_preserved": True,
            "unfinished_accumulators_are_not_complete_targets": True,
        }
        document["complete"] = False
        document["proved"] = False
        document["actual_returncode"] = 1
        save()
    final_raw = output.read_bytes()
    print("BEGIN COMPLETE POSITIVE NEWTON SOURCE RESULT bytes="+str(len(final_raw))
          +" sha256="+sha(final_raw), flush=True)
    sys.stdout.write(final_raw.decode("utf-8"))
    sys.stdout.flush()
    print("END COMPLETE POSITIVE NEWTON SOURCE RESULT", flush=True)
    return document["actual_returncode"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("repo", "manifest", "manifest-sha", "raw", "positive",
                 "restoration-receipts", "out"):
        parser.add_argument("--"+name, required=True)
    args = parser.parse_args()
    require(not Path(args.out).exists(),
            "preserve every prior complete or unfinished scientific result")
    return execute(args)


if __name__ == "__main__":
    raise SystemExit(main())
