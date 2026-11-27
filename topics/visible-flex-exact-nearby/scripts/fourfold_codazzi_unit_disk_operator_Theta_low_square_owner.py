"""GYN3, UDR7 and the first whole TQC11 original low96 square gate.

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
KIND = "R149_complete_unit_disk_operator_Theta_low_square_v1"
STAGE = "unit_disk_operator_Theta_low_square"
MANIFEST_KIND = "R149_complete_unit_disk_operator_Theta_low_square_inputs_v1"
SOURCE_PATH = TOPIC+"scripts/fourfold_codazzi_unit_disk_operator_Theta_low_square_owner.py"
WORKER_PATH = TOPIC+"scripts/fourfold_codazzi_unit_disk_operator_Theta_low_square_public_worker.py"
GENERATOR_PATH = TOPIC+"scripts/make_unit_disk_operator_Theta_low_square_manifest.py"
NORM_SUFFIXES = ["complete_infinity_upper", "complete_one_upper",
                 "complete_Schur_two_candidate", "complete_Frobenius_candidate"]
TQC_TARGETS = ["complete_low_model_action_joint_radius_upper", "complete_low_Theta_square_error_upper"]+[
    prefix+suffix for prefix in ("trial_inverse_", "trial_residual_") for suffix in NORM_SUFFIXES]+[
    "complete_low_Theta_preconditioned_residual_upper"]
UDR_TARGETS = ["complete_unit_disk_alpha_finite_Linf_product_upper",
    "complete_unit_disk_alpha_finite_L2_product_upper",
    "complete_unit_disk_alpha_inverse_error_Linf_product_upper",
    "complete_unit_disk_alpha_inverse_error_L2_product_upper",
    "complete_unit_disk_original_VQ_joint_L2_error_upper",
    "complete_unit_disk_original_VQ_joint_H1_error_upper",
    "complete_unit_disk_original_Theta_joint_L2_error_upper"]
GYN_TARGETS = ["complete_G_trial_real_matrix_infinity_upper",
    "complete_G_trial_real_matrix_one_upper",
    "complete_G_trial_real_matrix_Schur_two_upper"]
TARGETS = GYN_TARGETS+UDR_TARGETS+TQC_TARGETS
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
    "new_unit_disk_grid_points": 8192, "complete_same_original_alpha_modes": 2048,
    "complete_new_GY_real_rows": 384, "complete_new_GY_columns": 96,
    "all36864_signed_GY_entries_saved_before_new_induced_norms": True,
    "new_GY_operator_candidate_and_old_HS_saved_before_selection": True,
    "old_GY_Hilbert_Schmidt_target_recomputed": False,
    "unit_disk_point_inputs_saved_and_read_before_use": True,
    "new_whole_joint_products_before_first_low_square_gate": True,
    "coefficient_error_on_full_infinite_inverse_error_paid": True,
    "old_ASR_scalar_error_targets_replaced": False,
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
    "complete_coordinate_inverse", "copied_complete_AS_global_bounds",
    "copied_complete_AS_tail_bounds", "copied_complete_IR_residuals",
    "complete_unit_disk_mode_count", "complete_unit_disk_weighted_prefix",
    "unit_disk_input_receipt", "private_unit_disk_modes_receipt", "unit_disk_product_choices",
    "private_GY_real_matrix_receipt", "complete_GY_operator_norm_choice",
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
    context = admission.admit_complete_inputs(contents, specs, manifest)
    require(len(contents["original_TQC_owner"]) == 23216
            and sha(contents["original_TQC_owner"]) == "59900c078f727c3d4ef32e976156fd36bb17f73813c0a1a0ab8f169155fa67ba",
            "the entire never-executed original low-square implementation is retained")
    original_UDRC = {
        "original_UDRC_owner": (38813, "711be9fb460b62865143256a37bb232f39bb5682bddb7549d929876010242f57"),
        "original_UDRC_worker": (17031, "a44cf730ebabf778bbc63bc1d0c1f5a303c0f59f39bcef919e23f7da7d66cc2f"),
        "original_UDRC_generator": (12272, "2ba87c2fd8c7d80b7b902b75861613b0930f8b9e1a7fb53c52941eb445bd4a54"),
        "original_UDRC_note": (6936, "f3c493d9ed7f6f32303ad102aa965d7d3e63a42b2ec1642e4ef010cc8f3b9ccd"),
    }
    require(all((len(contents[role]), sha(contents[role])) == expected
                for role, expected in original_UDRC.items()),
            "all four original never-executed UDRC18 files retain their complete identities")
    GYN_proof = contents["GYN_proof"].decode()
    require(all(tag in GYN_proof for tag in ("GYN.2", "GYN.3", "GYN.5", "GYN.6", "GYN.7")),
            "the complete normalized real primitive operator and same-trial joint theorem")
    context["GYN"] = definitions(contents["GYN_math"], "_GYN_complete_primitive_operator_products")
    require(context["GYN"].POSITIVE_MODES == 192 and context["GYN"].COLUMNS == 96
            and context["GYN"].REAL_ROWS == 384 and context["GYN"].TARGETS == GYN_TARGETS,
            "every original coefficient, both real Fourier halves and all three new whole norms")
    proof = contents["UDR_proof"].decode()
    require(all(tag in proof for tag in ("UDR.3", "UDR.7", "UDR.13", "UDR.15", "UDR.19")),
            "the complete new same-trial disk and infinite-inverse-error theorem")
    context["UDR"] = definitions(contents["UDR_math"], "_UDR_complete_unit_disk_joint_products")
    require(context["UDR"].GRID == 8192 and context["UDR"].MODES == 2048
            and context["UDR"].PRODUCT_ORDER == UDR_TARGETS[:4],
            "all original modes, all nodes and all four whole new product candidates")
    return context


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
            and manifest["target_order"] == TARGETS and manifest["complete_record_counts"] == [21]
            and manifest["allowed_scientific_fields"] == SCI_FIELDS, "three new whole operator norms, seven joint products/errors and eleven first low-square targets")
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
            "UDR_math_sha256": specs["UDR_math"]["sha256"],
            "GYN_math_sha256": specs["GYN_math"]["sha256"],
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
        "copied_complete_AS_global_bounds": copy.deepcopy(old["AS"]["actual"]["global_bounds"]),
        "copied_complete_AS_tail_bounds": copy.deepcopy(old["AS"]["actual"]["complete_tail_bounds"]),
        "copied_complete_IR_residuals": {key: copy.deepcopy(old["IR"]["actual"]["new_records"][key])
            for key in ("complete_joint_energy_residual_upper", "complete_joint_L2_residual_upper")},
        "complete_unit_disk_mode_count": 0, "complete_unit_disk_weighted_prefix": None,
        "unit_disk_input_receipt": None, "private_unit_disk_modes_receipt": None,
        "unit_disk_product_choices": {},
        "private_GY_real_matrix_receipt": None, "complete_GY_operator_norm_choice": None,
    }
    require(sorted(document) == SCI_FIELDS, "the entire new scientific object schema")
    began = time.perf_counter()
    private = args.output.parent/"private-unit-disk-operator-Theta-low-square"
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

        # GYN: three genuinely new induced-norm targets on the entire old IR trial.
        # The already completed OT Hilbert--Schmidt reducer is never called.
        GYN = context["GYN"]
        original_IR = old["IR"]["actual"]
        original_IR_raw = (private/"original-IR/complete-original-IR-trial.f64").read_bytes()
        original_IR_receipt = original_IR["private_trial_receipt"]
        require(len(original_IR_raw) == original_IR_receipt["bytes"] == 192*96*2*8
                and sha(original_IR_raw) == original_IR_receipt["sha256"],
                "the complete same original IR dyadic carrier before any new GY matrix")
        numbers = struct.unpack("<"+str(192*96*2)+"d", original_IR_raw)
        require(all(math.isfinite(value) for value in numbers),
                "every signed original IR coefficient is an exact finite dyadic")
        original_columns = [[api.acb(
            api.rational(Fraction(numbers[2*(n*96+j)])),
            api.rational(Fraction(numbers[2*(n*96+j)+1])))
            for n in range(192)] for j in range(96)]
        GY = GYN.complete_original_GY_real_matrix(api, original_columns)
        GY_body = {"kind": "GYN_complete_original_primitive_real_matrix_v1",
            "whole_original_IR_trial_sha256": sha(original_IR_raw),
            "shape": [384, 96], "normalized_measure": "2 dx/pi",
            "physical_frequency_factor": 4,
            "all_real_balls": [[value.str(90) for value in row] for row in GY]}
        GY_path = private/"complete-new-GY-real-matrix.json"
        GY_raw = canonical(GY_body)
        atomic(GY_path, GY_raw)
        saved_GY = parse(GY_path.read_bytes())
        require(saved_GY == GY_body, "the entire signed primitive matrix saved and read")
        formal_GY = [[arb(value) for value in row] for row in saved_GY["all_real_balls"]]
        require(len(formal_GY) == 384 and all(len(row) == 96 for row in formal_GY)
                and all(formal_GY[i][j].is_finite() and formal_GY[i][j].contains(GY[i][j])
                        for i in range(384) for j in range(96)),
                "all36864 formal signed balls include their complete original entries")
        document["private_GY_real_matrix_receipt"] = {
            "bytes": len(GY_raw), "sha256": sha(GY_raw), "shape": [384, 96],
            "whole_original_IR_trial_sha256": sha(original_IR_raw),
            "all36864_signed_entries_saved_read_before_absolute_values": True,
            "complete_normalized_real_basis_and_physical_frequency_factor": 4,
            "old_Hilbert_Schmidt_reducer_calls": 0}
        progress("complete_new_GY_real_matrix_saved_before_induced_norms", {})
        new_GY_norms = GYN.complete_induced_norms(api, formal_GY)
        require(set(new_GY_norms) == set(GYN_TARGETS[:2]), "both new complete induced norms")
        for name in GYN_TARGETS[:2]:
            emit(name, new_GY_norms[name])
        formal_GY_norms = parse(args.output.read_bytes())["new_records"]
        emit(GYN_TARGETS[2], GYN.complete_Schur_from_saved_norms(api,
            upper(formal_GY_norms[GYN_TARGETS[0]]), upper(formal_GY_norms[GYN_TARGETS[1]])))
        complete_GY_norms = parse(args.output.read_bytes())["new_records"]
        new_operator_record = complete_GY_norms[GYN_TARGETS[2]]
        old_HS_record = document["copied_complete_OT_records"]["complete_G_trial_Hilbert_Schmidt_upper"]
        GY_choice, unused_bound = GYN.select_whole_saved_operator_candidate(
            upper(new_operator_record), upper(old_HS_record))
        document["complete_GY_operator_norm_choice"] = {
            "selected_complete_candidate": GY_choice,
            "both_complete_candidates": {"new_complete_GY_operator_Schur": new_operator_record,
                                         "old_complete_GY_Hilbert_Schmidt": old_HS_record},
            "both_whole_candidates_formal_before_selection": True,
            "same_whole_original_GY_operator": True,
            "old_Hilbert_Schmidt_target_recomputed": False}
        save()
        formal_GY_choice = parse(args.output.read_bytes())["complete_GY_operator_norm_choice"]
        require(formal_GY_choice == document["complete_GY_operator_norm_choice"],
                "the entire new operator choice is saved/read before any joint product")
        refined_GY_operator = upper(formal_GY_choice["both_complete_candidates"][
            formal_GY_choice["selected_complete_candidate"]])

        # UDR changes the finite phase error input, never the original alpha trial.
        # Every old AS/IR/OT finite carrier is already restored under its whole SHA.
        UDR = context["UDR"]
        api.midpoint_real = lambda value: value.mid()
        api.midpoint_complex = lambda value: api.acb(value.real.mid(), value.imag.mid())
        alpha_actual = old["AS"]["actual"]
        grid_raw = (private/"original-AS/complete-original-AS-grid.json").read_bytes()
        trial_raw = (private/"original-AS/complete-original-AS-alpha-trial.json").read_bytes()
        for data, expected in ((grid_raw, alpha_actual["private_grid_receipt"]),
                               (trial_raw, alpha_actual["private_alpha_trial_receipt"])):
            require(len(data) == expected["bytes"] and sha(data) == expected["sha256"],
                    "the same entire original grid and signed alpha carrier before the new input")
        grid_doc, alpha_doc = parse(grid_raw), parse(trial_raw)
        require(grid_doc["complete_count"] == 8192 and len(grid_doc["all_pairs"]) == 8192
                and alpha_doc["positive_modes"] == 2048 and alpha_doc["exact_mean"] == "0"
                and alpha_doc["negative_modes_are_exact_conjugates"] is True
                and len(alpha_doc["all_positive_exact_pairs"]) == 2048,
                "the full raw192 grid and original2048 mean-zero signed coefficients")
        original_grid = [(arb(a), arb(b)) for a, b in grid_doc["all_pairs"]]
        original_alpha = [api.acb(api.rational(Fraction(a)), api.rational(Fraction(b)))
                          for a, b in alpha_doc["all_positive_exact_pairs"]]
        require(all(value.real.is_exact() and value.imag.is_exact() for value in original_alpha),
                "all original alpha trial coefficients remain exact dyadic points")
        kernel = UDR.UnitDiskPhaseInput(api, original_grid)

        def exact_point_string(value):
            require(value.is_finite() and value.is_exact(), "one complete exact dyadic center")
            numerator, exponent = map(int, value.mid().man_exp())
            point = (Fraction(numerator*(1 << exponent)) if exponent >= 0
                     else Fraction(numerator, 1 << (-exponent)))
            require(api.rational(point).is_exact() and api.rational(point) == value,
                    "the complete point has an exact saved rational representation")
            return str(point)

        input_body = {"kind": "UDR_complete_unit_disk_dyadic_phase_input_v1",
            "whole_original_grid_sha256": sha(grid_raw), "complete_nodes": 8192,
            "complete_mean_raw_radius_upper": formal_record(kernel.raw_radius),
            "all_exact_u_sreal_simag_and_tau_balls": [
                [exact_point_string(kernel.u[m]), exact_point_string(kernel.s[m].real),
                 exact_point_string(kernel.s[m].imag), kernel.tau[m].str(90)] for m in range(8192)],
            "phase_modulus_one_is_exact": True, "old_rectangular_power_recurrence_used": False}
        input_raw = canonical(input_body)
        input_sha, trial_sha = sha(input_raw), sha(trial_raw)
        input_path = private/"complete-new-unit-disk-phase-input.json"
        atomic(input_path, input_raw)
        saved_input = parse(input_path.read_bytes())
        require(saved_input == input_body and len(saved_input["all_exact_u_sreal_simag_and_tau_balls"]) == 8192,
                "the entire new8192-node finite input is saved and read before its first target")
        for m, (u, sr, si, tau) in enumerate(saved_input["all_exact_u_sreal_simag_and_tau_balls"]):
            saved_u = api.rational(Fraction(u))
            saved_s = api.acb(api.rational(Fraction(sr)), api.rational(Fraction(si)))
            saved_tau = arb(tau)
            require(saved_u == kernel.u[m] and saved_s == kernel.s[m]
                    and saved_tau.contains(kernel.tau[m]), "every new exact point and full phase disk is retained")
            kernel.u[m], kernel.uabs[m], kernel.s[m], kernel.tau[m] = (
                saved_u, abs(saved_u).upper(), saved_s, saved_tau.upper())
        kernel.raw_radius = upper(saved_input["complete_mean_raw_radius_upper"])
        document["unit_disk_input_receipt"] = {"bytes": len(input_raw), "sha256": input_sha,
            "complete_nodes": 8192, "whole_original_grid_sha256": sha(grid_raw),
            "every_complete_point_and_radius_saved_and_read": True}
        progress("complete_new_unit_disk_input_saved_and_read", {"complete_nodes": 8192})
        global_bounds = document["copied_complete_AS_global_bounds"]
        omega = arb(global_bounds["complete_exact_rotation_ball"])
        phase = arb(global_bounds["complete_original_source_phase_ball"])
        source_columns = [upper(record) for record in global_bounds["complete_source_error_derivative_columns"]]
        EH = upper(global_bounds["complete_original_H_minus_G_upper"])
        T = upper(global_bounds["new_raw_trial_Astrip_upper"])
        G1 = upper(global_bounds["complete_original_G_derivative_upper"])
        m_lower = original_owner.whole_ball(api, global_bounds["complete_original_map_imaginary_lower"])
        irH = upper(document["copied_complete_IR_residuals"]["complete_joint_energy_residual_upper"])
        ir0 = upper(document["copied_complete_IR_residuals"]["complete_joint_L2_residual_upper"])
        norm_records = document["copied_complete_OT_records"]
        J = refined_GY_operator
        W = upper(norm_records["complete_positive_G_trial_vector_Wiener_upper"])
        A = upper(norm_records["complete_alpha_trial_Wiener_upper"])
        mode_path = private/"complete-new-unit-disk-same-trial-mode-residuals.jsonl"
        mode_fields = {"complete_signed_trial_residual_upper", "new_finite_disk_to_old_trial_upper",
                       "complete_source_upper", "complete_model_upper", "complete_alias_upper",
                       "complete_original_divisor_lower"}
        accum = GYN.WholeContractedProducts(api, saved_G_operator=J, saved_G_positive_W=W,
                                          saved_IR_H=irH, saved_IR_L2=ir0)

        def save_weighted_prefix():
            document["complete_unit_disk_weighted_prefix"] = {
                "complete_modes": document["complete_unit_disk_mode_count"],
                "all_four_nonnegative_weighted_head_sums": [formal_record(value) for value in
                    (accum.finf, accum.f2square, accum.einf, accum.e2square)],
                "second_and_fourth_are_squared_candidates": True,
                "full_tail_not_yet_added": True,
                "incomplete_head_is_not_a_completed_whole_target": True}
            save()

        with mode_path.open("wb") as stream:
            for n in range(1, 2049):
                disk = kernel.next()
                values = UDR.complete_same_trial_mode_residual(api, n, disk, original_alpha[n-1],
                    omega=omega, source_phase=phase, source_columns=source_columns,
                    original_T=T, original_EH=EH, original_G1=G1, original_m=m_lower)
                require(set(values) == mode_fields, "each mode retains every old source/model/alias/divisor fee")
                records = {}
                for name, value in values.items():
                    if name.endswith("_lower"):
                        point = value.lower()
                        body = {"ball": point.str(60), "bound": "lower"}
                        require(arb(body["ball"]).contains(point), "whole divisor lower round trip")
                    else:
                        body = formal_record(value)
                    records[name] = body
                mode_body = {"kind": "UDR_complete_same_trial_mode_residual_v1", "mode": n,
                    "complete_grid_points": 8192, "new_input_sha256": input_sha,
                    "original_alpha_sha256": trial_sha, "complete_residual_records": records,
                    "complete_quadrature_disk_center": [disk["center"].real.str(90), disk["center"].imag.str(90)],
                    "complete_quadrature_disk_radius_upper": formal_record(disk["radius"])}
                mode_raw = canonical(mode_body)
                offset = stream.tell()
                stream.write(mode_raw)
                stream.flush()
                os.fsync(stream.fileno())
                with mode_path.open("rb") as check:
                    check.seek(offset)
                    saved_raw = check.readline()
                require(saved_raw == mode_raw, "the whole natural new mode is saved/read before accumulation")
                saved_mode = parse(saved_raw)
                accum.append(n, upper(saved_mode["complete_residual_records"]["complete_signed_trial_residual_upper"]))
                document["complete_unit_disk_mode_count"] = n
                if n % 64 == 0:
                    save_weighted_prefix()
                    progress("complete_unit_disk_same_trial_mode_prefix", {"complete_modes": n, "total_modes": 2048})
        # Read the ENTIRE new natural carrier, not only its last mode or counter.
        whole_mode_raw = mode_path.read_bytes()
        whole_modes = [parse(line) for line in whole_mode_raw.splitlines()]
        require(len(whole_modes) == 2048 and [value["mode"] for value in whole_modes] == list(range(1, 2049)),
                "all2048 whole natural residual records have no gap")
        formal_accum = GYN.WholeContractedProducts(api, saved_G_operator=J, saved_G_positive_W=W,
                                                  saved_IR_H=irH, saved_IR_L2=ir0)
        for n, mode in enumerate(whole_modes, 1):
            require(mode["kind"] == "UDR_complete_same_trial_mode_residual_v1"
                    and mode["complete_grid_points"] == 8192 and mode["new_input_sha256"] == input_sha
                    and mode["original_alpha_sha256"] == trial_sha
                    and set(mode["complete_residual_records"]) == mode_fields,
                    "every complete formal mode keeps the same whole new input and original signed trial")
            formal_accum.append(n, upper(mode["complete_residual_records"]["complete_signed_trial_residual_upper"]))
        document["private_unit_disk_modes_receipt"] = {"bytes": len(whole_mode_raw), "sha256": sha(whole_mode_raw),
            "complete_positive_modes": 2048, "complete_nodes_per_mode": 8192,
            "all_original_mean_phase_and_divisor_payments_retained": True,
            "new_input_sha256": input_sha, "same_original_alpha_sha256": trial_sha,
            "all_records_saved_read_before_complete_products": True}
        tail = document["copied_complete_AS_tail_bounds"]
        product_values = formal_accum.finish(upper(tail["complete_Linf_tail"]), upper(tail["complete_L2_tail"]))
        for name in UDR_TARGETS[:4]:
            emit(name, product_values[name])
        saved_products = parse(args.output.read_bytes())["new_records"]
        chosen_products = {}
        for label, names in (("finite_trial", UDR_TARGETS[:2]), ("whole_inverse_error", UDR_TARGETS[2:4])):
            choice = min(names, key=lambda name: upper(saved_products[name]))
            chosen_products[label] = upper(saved_products[choice])
            document["unit_disk_product_choices"][label] = {"selected_complete_candidate": choice,
                "both_complete_candidates": {name: saved_products[name] for name in names},
                "all2048_modes_and_complete_tail_retained": True,
                "choice_after_whole_save_readback": True, "extra_sqrt96": False}
        save()
        require(parse(args.output.read_bytes())["unit_disk_product_choices"] == document["unit_disk_product_choices"],
                "both whole candidate choices are formal before row bounds")
        joint = UDR.complete_original_row_errors(api, saved_original_alpha_trial_W=A,
            saved_IR_H=irH, saved_IR_L2=ir0, saved_finite_product=chosen_products["finite_trial"],
            saved_inverse_error_product=chosen_products["whole_inverse_error"],
            saved_whole_model_rounding=upper(norm_records["complete_model_action_joint_rounding_error_upper"]),
            original_whole_model_one_loss_norm=api.rational(512))
        for name in UDR_TARGETS[4:]:
            emit(name, joint[name])
        formal_UDR = parse(args.output.read_bytes())
        require(formal_UDR["completed_targets"] == GYN_TARGETS+UDR_TARGETS and formal_UDR["saved_record_count"] == 10,
                "all seven whole new disk products/errors precede the first low-square target")
        progress("all_complete_unit_disk_row_errors_saved_before_first_low_square", {})

        TQ, TQL = context["TQ"], context["TQL"]
        low_radius = emit(TQC_TARGETS[0], TQL.complete_low_model_radius(api, formal_rows, exact_rows))
        low_error = emit(TQC_TARGETS[1], TQL.complete_low_candidate(api,
            upper(formal_UDR["new_records"]["complete_unit_disk_original_VQ_joint_L2_error_upper"]), low_radius))
        # Both whole candidates already exist on disk before this selection.
        saved = parse(args.output.read_bytes())
        global_record = saved["new_records"]["complete_unit_disk_original_Theta_joint_L2_error_upper"]
        low_record = saved["new_records"][TQC_TARGETS[1]]
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
            "complete_new_record_order": list(TARGETS), "complete_new_record_count": 21,
            "complete_square_dimension": 96, "all_original_carrier_rows": 96,
            "all_original_carrier_modes": 2240,
            "all_original_whole_carrier_SHA_identical": True,
            "complete_low_model_isometry_and_all9216_radii_used": True,
            "whole_global_and_low_error_candidates_saved_before_choice": True,
            "complete_signed_inverse_and_residual_norm_candidates_saved_before_choice": True,
            "full_source_phase_mean_and_infinite_errors_retained": True,
            "finite_coordinate_inverse_proved": gate["finite_coordinate_inverse_proved"],
            "strict_gate_completely_evaluated": True,
            "complete_new_disk_modes": 2048, "complete_new_disk_grid_points": 8192,
            "all_four_new_products_saved_before_any_choice": True,
            "coefficient_error_on_infinite_inverse_error_paid": True,
            "all_seven_UDR_records_formal_before_first_TQC_target": True,
            "all_three_GYN_records_formal_before_first_UDR_target": True,
            "all36864_signed_GY_entries_before_new_induced_norms": True,
            "new_operator_and_old_HS_whole_candidates_formal_before_choice": True,
            "old_GY_Hilbert_Schmidt_target_recomputed": False,
            "old_ASR_scalar_targets_or_old_OT_norms_recomputed": False,
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
