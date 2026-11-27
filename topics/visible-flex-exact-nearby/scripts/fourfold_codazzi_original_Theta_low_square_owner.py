"""First complete low96 original Theta square and its strict inverse gate.

The full OT result is a prerequisite. Necessary original carriers retain
all whole SHA identities; completed OT/IR/AS norm targets never execute.
The outcome is the finite coordinate gate only, including an explicit
false outcome when its complete directed residual does not lie below1.
"""
from __future__ import annotations
import argparse
import ast
import copy
import hashlib
import json
import math
import os
import platform
import struct
import subprocess
import sys
import time
import traceback
import types
from fractions import Fraction
from pathlib import Path

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby/"
KIND = "R149_complete_original_Theta_low_square_v1"
STAGE = "original_Theta_low_square"
MANIFEST_KIND = "R149_complete_original_Theta_low_square_inputs_v1"
SOURCE_PATH = TOPIC+"scripts/fourfold_codazzi_original_Theta_low_square_owner.py"
WORKER_PATH = TOPIC+"scripts/fourfold_codazzi_original_Theta_low_square_public_worker.py"
GENERATOR_PATH = TOPIC+"scripts/make_original_Theta_low_square_manifest.py"
NORM_SUFFIXES = ["complete_infinity_upper", "complete_one_upper",
                 "complete_Schur_two_candidate", "complete_Frobenius_candidate"]
TARGETS = ["complete_low_model_action_joint_radius_upper", "complete_low_Theta_square_error_upper"]+[
    prefix+suffix for prefix in ("trial_inverse_", "trial_residual_") for suffix in NORM_SUFFIXES]+[
    "complete_low_Theta_preconditioned_residual_upper"]
PARAMETERS = {
    "arithmetic_bits": 320, "decimal_record_digits": 60, "private_ball_digits": 90,
    "maximum_scientific_wall_seconds": 16800,
    "complete_original_rows": 96, "complete_original_modes_per_row": 2240,
    "complete_new_square_dimension": 96, "physical_frequency_factor": 4,
    "target_basis": "sqrt(2)*cos(4*n*x-2*n*a), true a=2*H(0)",
    "low_model_isometry": "Gbar E96a=E96b, b=a+Omega",
    "whole_low_and_global_error_candidates_saved_before_choice": True,
    "full_signed_matrix_product_before_absolute_values": True,
    "trial_inverse_proposal": "binary64 numpy.linalg.inv; singular or nonfinite gives exact zero and a false gate",
    "trial_inverse_CORETYPE": "Haswell", "all_carrier_threads": 1,
    "original_IR_carrier_CORETYPE": "Haswell", "original_AS_carrier_CORETYPE": "unset",
    "completed_original_norm_or_residual_targets_allowed": 0,
    "physical_PDE_inverse_or_full_Schur_claimed": False,
}
SCI_FIELDS = sorted([
    "identity", "complete", "proved", "actual_returncode", "failure", "stage",
    "completed_targets", "current_target", "candidate_record", "new_records", "saved_record_count",
    "parameters", "result", "whole_completed_inputs", "copied_complete_OT_records",
    "copied_model_input_records", "reference_identity", "selected_member_identity",
    "runtime", "wall_seconds", "progress", "old_scientific_target_calls",
    "necessary_carrier_rematerializations", "carrier_restorations", "original_Theta_carrier_restoration",
    "new_arrays_published", "new_artifacts", "new_Releases", "private_complete_row_count",
    "private_square_receipt", "private_trial_inverse_receipt", "private_signed_residual_receipt",
    "trial_inverse_proposal_status", "complete_square_error_choice", "complete_norm_choices",
    "complete_coordinate_inverse",
])


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def parse(raw):
    return json.loads(raw, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False)+"\n").encode()


def atomic(path, raw):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".partial")
    temporary.write_bytes(raw)
    os.replace(temporary, path)


def definitions(raw, name):
    ast.parse(raw.decode(), filename=name)
    module = types.ModuleType(name)
    module.__file__ = name
    exec(compile(raw, name, "exec"), module.__dict__)
    return module


def admit_complete_inputs(contents, specs, manifest):
    require(specs["science"]["path"] == SOURCE_PATH and specs["worker"]["path"] == WORKER_PATH
            and specs["generator"]["path"] == GENERATOR_PATH,
            "the exact first whole low-square owner/worker/generator")
    admission = definitions(contents["admission"], "_TQC_complete_original_parent_admission")
    return admission.admit_complete_inputs(contents, specs, manifest)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--manifest-sha", required=True)
    ap.add_argument("--input-map", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--checkout", required=True)
    ap.add_argument("--carrier-mode", choices=("IR", "AS"))
    ap.add_argument("--carrier-directory", type=Path)
    ap.add_argument("--carrier-receipt", type=Path)
    args = ap.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true" and os.environ.get("GITHUB_REPOSITORY") == REPO
            and os.environ.get("GITHUB_RUN_ATTEMPT") == "1", "one first public whole low-square execution")
    manifest_raw = args.manifest.read_bytes()
    require(sha(manifest_raw) == args.manifest_sha, "the entire original low-square manifest")
    manifest = parse(manifest_raw)
    require(manifest["kind"] == MANIFEST_KIND and manifest["scientific_kind"] == KIND
            and manifest["stage"] == STAGE and manifest["parameters"] == PARAMETERS
            and manifest["target_order"] == TARGETS and manifest["complete_record_counts"] == [11]
            and manifest["allowed_scientific_fields"] == SCI_FIELDS, "the complete new eleven-target contract")
    specs = {value["role"]: value for value in manifest["files"]+manifest["historical_inputs"]}
    paths = parse(args.input_map.read_bytes())
    require(set(paths) == set(specs) and sha(Path(__file__).read_bytes()) == specs["science"]["sha256"],
            "every complete current/native snapshot and the actual owner")
    contents = {role: Path(path).read_bytes() for role, path in paths.items()}
    context = admit_complete_inputs(contents, specs, manifest)
    original_owner, old = context["owner"], context["admitted"]
    if args.carrier_mode is not None:
        original_owner.carrier_child(args, old)
        return
    require(not args.output.exists(), "retain earlier actual conclusions or failed prefixes")
    original = context["actual"]
    document = {
        "identity": {"kind": KIND, "scalar_stage": STAGE, "source_sha256": specs["science"]["sha256"],
            "manifest_sha256": args.manifest_sha, "OT_actual_sha256": specs["OT_actual"]["sha256"],
            "TQ_math_sha256": specs["TQ_math"]["sha256"], "TQL_math_sha256": specs["TQL_math"]["sha256"],
            "carrier_restore_sha256": specs["carrier_restore"]["sha256"],
            "run_id": os.environ["GITHUB_RUN_ID"], "run_attempt": "1", "event_commit": os.environ["GITHUB_SHA"],
            "actual_checkout_commit": args.checkout, "arithmetic_bits": 320},
        "complete": False, "proved": False, "actual_returncode": None, "failure": None,
        "stage": "whole_original_OT_actual_and_all_prerequisites_admitted", "completed_targets": [],
        "current_target": None, "candidate_record": None, "new_records": {}, "saved_record_count": 0,
        "parameters": copy.deepcopy(PARAMETERS), "result": None,
        "whole_completed_inputs": {role: {"bytes": value["bytes"], "sha256": value["sha256"]}
                                   for role, value in specs.items()},
        "copied_complete_OT_records": copy.deepcopy(original["new_records"]),
        "copied_model_input_records": copy.deepcopy(original["actual_model_input_records"]),
        "reference_identity": copy.deepcopy(original["reference_identity"]),
        "selected_member_identity": copy.deepcopy(original["selected_member_identity"]),
        "runtime": {}, "wall_seconds": 0.0, "progress": {}, "old_scientific_target_calls": 0,
        "necessary_carrier_rematerializations": 0, "carrier_restorations": {},
        "original_Theta_carrier_restoration": None,
        "new_arrays_published": 0, "new_artifacts": 0, "new_Releases": 0,
        "private_complete_row_count": 0, "private_square_receipt": None,
        "private_trial_inverse_receipt": None, "private_signed_residual_receipt": None,
        "trial_inverse_proposal_status": None, "complete_square_error_choice": None,
        "complete_norm_choices": {}, "complete_coordinate_inverse": None,
    }
    require(sorted(document) == SCI_FIELDS, "the entire new scientific object schema")
    began = time.perf_counter()
    private = args.output.parent/"private-original-Theta-low-square"
    private.mkdir()

    def save():
        document["wall_seconds"] = time.perf_counter()-began
        raw = canonical(document)
        require(len(raw) <= manifest["operation"]["maximum_scientific_bytes"], "one whole small low-square result")
        atomic(args.output, raw)

    def progress(stage, data):
        document["stage"], document["progress"] = stage, data
        save()
        require(document["wall_seconds"] <= PARAMETERS["maximum_scientific_wall_seconds"],
                "whole actual prefix preserved before its runtime budget")
        print(json.dumps(dict(stage=stage, **data), sort_keys=True), flush=True)

    save()
    try:
        from importlib.metadata import version
        runtime = {"python": platform.python_version(),
                   "packages": {name: version(name) for name in ("numpy", "python-flint")}}
        require(runtime == manifest["runtime"], "the original immutable carrier arithmetic runtime")
        document["runtime"] = runtime
        for mode in ("AS", "IR"):
            directory, receipt_path = private/("original-"+mode), private/(mode+"-restoration.json")
            env = dict(os.environ)
            env.update({name: "1" for name in original_owner.THREAD_VARIABLES})
            if mode == "IR":
                env["OPENBLAS_CORETYPE"] = "Haswell"
            else:
                env.pop("OPENBLAS_CORETYPE", None)
            command = [sys.executable, str(Path(__file__).resolve()), "--manifest", str(args.manifest.resolve()),
                "--manifest-sha", args.manifest_sha, "--input-map", str(args.input_map.resolve()),
                "--output", str(args.output.resolve()), "--checkout", args.checkout,
                "--carrier-mode", mode, "--carrier-directory", str(directory.resolve()),
                "--carrier-receipt", str(receipt_path.resolve())]
            document["necessary_carrier_rematerializations"] += 1
            progress("necessary_original_"+mode+"_carrier_restoration_started", {})
            with (private/(mode+"-restoration.log")).open("wb") as out:
                process = subprocess.Popen(command, stdout=out, stderr=subprocess.STDOUT, env=env)
                try:
                    last = 0.0
                    while process.poll() is None:
                        if time.perf_counter()-last >= 15:
                            if receipt_path.exists():
                                document["carrier_restorations"][mode] = parse(receipt_path.read_bytes())
                            progress("necessary_original_"+mode+"_carrier_restoration_running", {})
                            last = time.perf_counter()
                        time.sleep(1)
                finally:
                    if process.poll() is None:
                        process.terminate()
                        try:
                            process.wait(timeout=10)
                        except subprocess.TimeoutExpired:
                            process.kill()
                            process.wait()
            require(receipt_path.exists(), "the whole necessary original-carrier child receipt")
            receipt = parse(receipt_path.read_bytes())
            document["carrier_restorations"][mode] = receipt
            save()
            require(process.returncode == 0 and receipt["complete"] is True and receipt["failure"] is None
                    and receipt["result"]["whole_original_SHA_required"] is True
                    and receipt["result"]["old_scientific_target_calls"] == 0,
                    "all original "+mode+" carrier bytes restored without a repeated norm target")

        import flint
        flint.ctx.prec = 320
        api = original_owner.directed_api(flint)
        arb = api.arb
        formal_rows, exact_rows, restoration = context["restore"].restore(api, old, original_owner,
            context["old_contents"]["science"], original, private, progress)
        document["original_Theta_carrier_restoration"] = restoration
        document["private_complete_row_count"] = 96
        progress("all_original_96x2240_carrier_whole_SHA_restored", {})

        def upper(record):
            return original_owner.whole_upper(api, record)

        def formal_record(value):
            point = value.upper()
            require(point.is_finite() and point >= 0, "one complete nonnegative directed new upper")
            body = {"ball": point.str(60), "bound": "upper"}
            formal = arb(body["ball"])
            require(formal.is_finite() and formal.contains(point), "whole complete formal upper round trip")
            return body

        def emit(name, value):
            require(name == TARGETS[document["saved_record_count"]]
                    and document["current_target"] is document["candidate_record"] is None,
                    "only the next complete natural low-square target")
            body = formal_record(value)
            document["current_target"], document["candidate_record"] = name, body
            save()
            read = parse(args.output.read_bytes())["candidate_record"]
            require(read == body, "whole new target saved/read before its dependent use")
            document["new_records"][name] = read
            document["completed_targets"].append(name)
            document["saved_record_count"] += 1
            document["current_target"] = document["candidate_record"] = None
            save()
            return upper(read)

        TQ, TQL = context["TQ"], context["TQL"]
        low_radius = emit(TARGETS[0], TQL.complete_low_model_radius(api, formal_rows, exact_rows))
        low_error = emit(TARGETS[1], TQL.complete_low_candidate(api,
            upper(document["copied_complete_OT_records"]["complete_original_VQ_joint_L2_error_upper"]), low_radius))
        # Both whole candidates already exist on disk before this selection.
        saved = parse(args.output.read_bytes())
        global_record = saved["copied_complete_OT_records"]["complete_original_Theta_joint_L2_error_upper"]
        low_record = saved["new_records"][TARGETS[1]]
        selected, square_error = TQL.select_whole_saved_candidate(upper(global_record), upper(low_record))
        document["complete_square_error_choice"] = {
            "selected_complete_candidate": selected,
            "both_complete_candidates": {"whole_original_global_Theta_error": global_record,
                                         "whole_exact_low_model_Theta_error": low_record},
            "choice_after_whole_save_readback": True, "same_complete_square": True,
            "all_infinite_errors_and_true_phases_retained": True,
            "extra_sqrt96_or_high_model512_on_low_isometry": False}
        save()

        theta_raw = (private/"complete-original-Theta-trial.f64").read_bytes()
        require(len(theta_raw) == original["private_Theta_trial_receipt"]["bytes"]
                and sha(theta_raw) == original["private_Theta_trial_receipt"]["sha256"],
                "the whole original dyadic matrix before extracting its low square")
        square_raw = b"".join(theta_raw[j*2240*8:j*2240*8+96*8] for j in range(96))
        atomic(private/"complete-original-low-square.f64", square_raw)
        require((private/"complete-original-low-square.f64").read_bytes() == square_raw,
                "the entire inherited 96x96 exact square saved/read")
        document["private_square_receipt"] = {"bytes": len(square_raw), "sha256": sha(square_raw),
            "shape": [96, 96], "dtype": "<f8", "order": "C", "same_original_OT_low_square": True}
        os.environ["OPENBLAS_CORETYPE"] = PARAMETERS["trial_inverse_CORETYPE"]
        for name in original_owner.THREAD_VARIABLES:
            os.environ[name] = "1"
        import numpy as np
        square_floats = np.frombuffer(square_raw, dtype="<f8").reshape(96, 96)
        require(np.isfinite(square_floats).all(), "the whole exact finite original low square")
        try:
            inverse = np.linalg.inv(square_floats)
            if np.isfinite(inverse).all():
                proposal_status = "one_complete_numpy_inverse_proposal"
            else:
                inverse = np.zeros((96, 96), dtype="<f8")
                proposal_status = "nonfinite_inverse_proposal_exact_zero_with_failed_gate"
        except np.linalg.LinAlgError:
            inverse = np.zeros((96, 96), dtype="<f8")
            proposal_status = "singular_inverse_proposal_exact_zero_with_failed_gate"
        inverse_raw = np.ascontiguousarray(inverse, dtype="<f8").tobytes(order="C")
        require(len(inverse_raw) == 96*96*8, "the entire new exact dyadic inverse proposal")
        atomic(private/"complete-new-low-square-trial-inverse.f64", inverse_raw)
        require((private/"complete-new-low-square-trial-inverse.f64").read_bytes() == inverse_raw,
                "the complete trial inverse saved/read before certification")
        document["trial_inverse_proposal_status"] = proposal_status
        document["private_trial_inverse_receipt"] = {"bytes": len(inverse_raw), "sha256": sha(inverse_raw),
            "shape": [96, 96], "dtype": "<f8", "order": "C", "exact_dyadic_trial": True}
        numbers = struct.unpack("<9216d", inverse_raw)
        require(all(math.isfinite(value) for value in numbers), "all signed inverse entries are exact finite dyadics")
        B = [[api.rational(Fraction(numbers[96*i+j])) for j in range(96)] for i in range(96)]
        ingredients = TQ.complete_constraint_gate_ingredients(api, exact_rows, B)
        residual_body = {"kind": "TQC_complete_signed_preconditioned_low_square_residual_v1",
            "rows": 96, "columns": 96,
            "all_real_balls": [[value.str(90) for value in row]
                for row in ingredients["complete_signed_preconditioned_residual"]]}
        residual_raw = canonical(residual_body)
        atomic(private/"complete-signed-low-square-residual.json", residual_raw)
        require((private/"complete-signed-low-square-residual.json").read_bytes() == residual_raw,
                "the entire signed product is saved, before publishing either complete norm candidate")
        formal_residual = parse((private/"complete-signed-low-square-residual.json").read_bytes())["all_real_balls"]
        require(len(formal_residual) == 96 and all(len(row) == 96 for row in formal_residual)
                and all(arb(formal_residual[i][j]).contains(value)
                    for i, row in enumerate(ingredients["complete_signed_preconditioned_residual"])
                    for j, value in enumerate(row)),
                "every saved signed residual ball contains the complete directed matrix entry")
        document["private_signed_residual_receipt"] = {"bytes": len(residual_raw), "sha256": sha(residual_raw),
            "shape": [96, 96], "all_entries_and_signed_sums_before_absolute_values": True}
        choices = {}
        for prefix, values in (("trial_inverse_", ingredients["trial_inverse_norm_candidates"]),
                               ("trial_residual_", ingredients["trial_residual_norm_candidates"])):
            for suffix in NORM_SUFFIXES:
                emit(prefix+suffix, values[suffix])
            saved = parse(args.output.read_bytes())["new_records"]
            names = [prefix+"complete_Schur_two_candidate", prefix+"complete_Frobenius_candidate"]
            chosen = min(names, key=lambda name: upper(saved[name]))
            choices[prefix] = upper(saved[chosen])
            document["complete_norm_choices"][prefix] = {"selected_complete_candidate": chosen,
                "both_complete_candidates": {name: saved[name] for name in names},
                "choice_after_whole_save_readback": True, "all_signed_entries_retained": True}
            save()
        b, r0 = choices["trial_inverse_"], choices["trial_residual_"]
        rho = emit(TARGETS[-1], TQ.complete_constraint_residual_from_saved_bounds(api, r0, b, square_error))
        gate = TQ.complete_constraint_inverse_from_saved_residual(api, rho, b)
        inverse_record = gate.pop("complete_coordinate_inverse_two_upper")
        gate["complete_coordinate_inverse_two_upper"] = (
            None if inverse_record is None else formal_record(inverse_record))
        gate.update(strict_whole_residual_upper_less_than_one=gate["finite_coordinate_inverse_proved"],
            complete_preconditioned_residual_record=copy.deepcopy(document["new_records"][TARGETS[-1]]),
            sufficient_gate_false_is_not_a_singularity_proof=True)
        document["complete_coordinate_inverse"] = gate
        save()
        require(parse(args.output.read_bytes())["complete_coordinate_inverse"] == gate,
                "the entire strict gate outcome and conditional inverse bound saved/read")
        document["result"] = {
            "complete_new_record_order": list(TARGETS), "complete_new_record_count": 11,
            "complete_square_dimension": 96, "all_original_carrier_rows": 96,
            "all_original_carrier_modes": 2240,
            "all_original_whole_carrier_SHA_identical": True,
            "complete_low_model_isometry_and_all9216_radii_used": True,
            "whole_global_and_low_error_candidates_saved_before_choice": True,
            "complete_signed_inverse_and_residual_norm_candidates_saved_before_choice": True,
            "full_source_phase_mean_and_infinite_errors_retained": True,
            "finite_coordinate_inverse_proved": gate["finite_coordinate_inverse_proved"],
            "strict_gate_completely_evaluated": True,
            "extra_sqrt96_or_high_model512_on_low_isometry": False,
            "completed_old_norm_residual_or_cohomology_targets_recomputed": False,
            "physical_mean_slots_eliminated": False,
            "actual_true_PDE_inverse_or_full_Schur_proved": False,
            "topic_completion_proved": False}
        document["complete"] = document["proved"] = True
        document["actual_returncode"] = 0
        document["stage"] = "complete_"+STAGE+"_branch"
    except BaseException as exc:
        document["actual_returncode"] = 1
        document["failure"] = {"type": type(exc).__name__, "message": str(exc), "traceback": traceback.format_exc()}
        save()
        raise
    finally:
        save()


if __name__ == "__main__":
    main()
