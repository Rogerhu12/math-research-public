"""First full original Theta action from the whole completed IR and AS.

Two isolated carrier-only children preserve their original runtimes and
whole saved SHA identities. Old residuals, norm budgets and cohomology
targets are not executed. The parent evaluates only the new DT/TM/TP
finite action and its complete joint errors, retaining every signed row.
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
KIND = "R149_complete_original_Theta_rows_v1"
STAGE = "complete_original_Theta_rows"
MANIFEST_KIND = "R149_complete_original_Theta_rows_inputs_v1"
SOURCE_PATH = TOPIC+"scripts/fourfold_codazzi_complete_original_Theta_rows_owner.py"
WORKER_PATH = TOPIC+"scripts/fourfold_codazzi_complete_original_Theta_rows_public_worker.py"
GENERATOR_PATH = TOPIC+"scripts/make_complete_original_Theta_rows_manifest.py"
NORM_TARGETS = ["complete_G_trial_Hilbert_Schmidt_upper",
                "complete_positive_G_trial_vector_Wiener_upper",
                "complete_alpha_trial_Wiener_upper"]
PRODUCT_TARGETS = ["complete_alpha_Linf_product_upper", "complete_alpha_L2_product_upper"]
TARGETS = NORM_TARGETS+PRODUCT_TARGETS+[
    "complete_true_alpha_Linf_upper", "complete_original_VQ_joint_L2_error_upper",
    "complete_original_Theta_before_rounding_error_upper",
    "complete_model_action_joint_rounding_error_upper", "complete_original_Theta_joint_L2_error_upper"]
PARAMETERS = {
    "arithmetic_bits": 320, "decimal_record_digits": 60, "private_ball_digits": 90,
    "maximum_scientific_wall_seconds": 16800,
    "row_count": 96, "IR_positive_modes": 192, "AS_positive_modes": 2048,
    "complete_Theta_row_modes": 2240, "physical_frequency_factor": 4,
    "physical_period": "pi/2", "target_basis": "sqrt(2)*cos(4*n*x-2*n*a), true a=2*H(0)",
    "source_phase": "b=a+Omega", "first_coefficient_mean": "nu=-mu/2",
    "model_low_reference_modes": 96, "model_low_reference_multiplier": "1",
    "qualified_original_model_Hminus1_bound": "512",
    "original_same_sign_source_Toeplitz": True,
    "whole_infinite_IR_and_AS_errors_retained": True,
    "whole_Linf_and_L2_product_candidates_retained": True,
    "two_physical_mean_slots_eliminated": False,
    "exact_trial_encoding": "little-endian binary64 exact dyadics, row-major96x2240",
    "IR_carrier_CORETYPE": "Haswell", "AS_carrier_CORETYPE": "unset",
    "all_carrier_threads": 1,
    "old_completed_scientific_targets_allowed": 0,
}
SCI_FIELDS = sorted([
    "identity", "complete", "proved", "actual_returncode", "failure", "stage",
    "completed_targets", "current_target", "candidate_record", "new_records", "saved_record_count",
    "parameters", "result", "whole_completed_inputs", "copied_complete_parent_records",
    "reference_identity", "selected_member_identity", "runtime", "wall_seconds", "progress",
    "old_scientific_target_calls", "necessary_carrier_rematerializations", "carrier_restorations",
    "new_arrays_published", "new_artifacts", "new_Releases", "complete_product_choice",
    "private_complete_row_count", "private_DT_rows_receipt", "private_model_rows_receipt",
    "private_Theta_trial_receipt", "private_model_multipliers_receipt", "actual_model_input_records",
])
THREAD_VARIABLES = ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
                    "BLIS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS")


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
            "the actual new original-Theta owner/worker/generator")
    admission = definitions(contents["admission"], "_OT_complete_original_input_admission")
    return admission.admit_complete_inputs(contents, specs, manifest)


def directed_api(flint):
    arb, acb = flint.arb, flint.acb

    def rational(n, d=1):
        value = Fraction(n)/Fraction(d)
        return arb(value.numerator)/value.denominator

    return types.SimpleNamespace(arb=arb, acb=acb, acb_mat=flint.acb_mat,
        zero=arb(0), one=arb(1), rational=rational,
        lower=lambda value: value.lower(), magnitude=lambda value: abs(value).upper(),
        sqrt=lambda value: value.sqrt(), exp=lambda value: value.exp())


def whole_ball(api, record):
    require(isinstance(record, dict) and isinstance(record.get("ball"), str),
            "one entire original scalar ball")
    value = (api.arb(record["lower"]).lower().union(api.arb(record["upper"]).upper())
             if "lower" in record and "upper" in record else api.arb(record["ball"]))
    require(value.is_finite(), "whole original finite scalar")
    return value


def whole_upper(api, record):
    value = whole_ball(api, record)
    require(value.lower() >= 0, "whole qualified nonnegative upper")
    return value.upper()


def verify_private(path, raw, expected):
    require(len(raw) == expected["bytes"] and sha(raw) == expected["sha256"],
            "whole original private carrier SHA: "+Path(path).name)
    atomic(path, raw)
    require(Path(path).read_bytes() == raw, "the complete exact original carrier saved/read")


def forbidden(*args, **kwargs):
    raise RuntimeError("a completed scientific target cannot run during carrier-only restoration")


def restore_IR(context, destination, progress):
    require(os.environ.get("OPENBLAS_CORETYPE") == "Haswell"
            and all(os.environ.get(name) == "1" for name in THREAD_VARIABLES),
            "the original immutable IR runtime and complete BLAS schedule")
    import flint
    import numpy as np
    flint.ctx.prec = 320
    api = directed_api(flint)
    original, pure = context["IR"], context["IR_math"]
    actual = original["actual"]
    owner = original["owner"]
    owner.main = forbidden
    for name in ("fft_tables", "complete_directed_dft", "complete_global_bounds", "complete_kernels",
                 "complete_column_bounds", "entire_signed_head", "complete_residual_norms",
                 "complete_joint_residual", "CompletePrimitiveSampleFactory"):
        require(hasattr(pure, name), "every original completed IR target entrypoint is identified")
        setattr(pure, name, forbidden)
    grid = pure.exact_compound_grid(api, context["states"][1],
                                   context["prior"]["K_sines"], context["prior"]["K_cosines"])
    body = {"kind": "R149_complete_original_inverse_lift_grid_v1", "complete_count": len(grid),
            "all_balls": [value.str(80) for value in grid]}
    grid_raw = canonical(body)
    verify_private(destination/"complete-original-IR-grid.json", grid_raw, actual["private_grid_receipt"])
    saved = parse(grid_raw)
    formal = [api.arb(value) for value in saved["all_balls"]]
    require(len(formal) == 4096 and all(value.contains(old) for value, old in zip(formal, grid)),
            "the original whole formally saved IR grid")
    progress("original_IR_grid_whole_SHA_restored", {"complete_count": 4096})
    raw = owner.choose_complete_dyadic_trial_bytes(np, formal)
    verify_private(destination/"complete-original-IR-trial.f64", raw, actual["private_trial_receipt"])
    return {"complete": True, "kind": "OT_exact_original_IR_carrier_restoration_v1",
            "grid": copy.deepcopy(actual["private_grid_receipt"]),
            "trial": copy.deepcopy(actual["private_trial_receipt"]),
            "old_scientific_target_calls": 0, "necessary_finite_trial_rematerializations": 1,
            "whole_original_SHA_required": True, "CORETYPE": "Haswell"}


def restore_AS(context, destination, progress):
    require("OPENBLAS_CORETYPE" not in os.environ
            and all(os.environ.get(name) == "1" for name in THREAD_VARIABLES),
            "the original AS/SN point runtime, without an invented CORETYPE")
    parent, pure, restore = context["AS"], context["AS_math"], context["SN_restore"]
    actual = parent["actual"]
    original = parent["admitted"][0]
    for name in ("source_error_columns", "raw_trial_strip_norm", "complete_analytic_data",
                 "complete_mode_data", "complete_tail", "complete_errors"):
        setattr(pure, name, forbidden)
    parent["owner"].main = forbidden
    snapshot = {path: parent["contents"]["SN_text_"+str(i).zfill(3)]
                for i, path in enumerate(original["current_text_paths"])}
    root = destination/"whole-original-SN-inputs"
    inputs = restore.restore_original_files(Path(os.environ["GITHUB_WORKSPACE"]), root,
        parent["contents"]["SN_manifest"], snapshot, progress)
    inp, refs, helper, endpoint = restore.rematerialize_original_endpoint(root, progress)
    require(endpoint == actual["original_endpoint_restoration"],
            "all original endpoint restoration identities agree with the complete AS actual")
    import flint
    require(flint.ctx.prec == 320 and flint.ctx.cap == 9, "whole original point arithmetic")
    api = directed_api(flint)
    chi = inp.root_data(1, True)["chi"].v.value().ne()/inp.rs.sqrt()
    raw_source = refs[1]+chi-inp.mu/2
    require(raw_source.lo >= -128 and raw_source.hi <= 128, "the whole original raw source")
    mean = api.rational(helper.rat(raw_source.mean()))
    pairs = []
    for n in range(1, 129):
        coefficient = (raw_source.coeff(n)+raw_source.coeff(-n).conjugate())/2
        pairs.append([str(helper.rat(coefficient.real)), str(helper.rat(coefficient.imag))])
    raw_trial = {"kind": "AS_complete_raw_signed_trial_v1", "positive_modes": 128,
                 "exact_mean": str(helper.rat(mean)), "all_positive_exact_pairs": pairs,
                 "negative_modes_are_exact_conjugates": True}
    raw_bytes = canonical(raw_trial)
    verify_private(destination/"complete-original-AS-raw-trial.json", raw_bytes,
                   actual["private_raw_trial_receipt"])
    formal = parse(raw_bytes)
    positive = [api.acb(api.rational(Fraction(a)), api.rational(Fraction(b)))
                for a, b in formal["all_positive_exact_pairs"]]
    mean = api.rational(Fraction(formal["exact_mean"]))
    grid = pure.original_grid(api, positive, mean, inp.Hs, inp.Hc, inp.Ks, inp.Kc)
    body = {"kind": "AS_complete_original_G_raw_t_grid_v1", "complete_count": 8192,
            "all_pairs": [[t.str(90), g.str(90)] for t, g in grid]}
    grid_raw = canonical(body)
    verify_private(destination/"complete-original-AS-grid.json", grid_raw, actual["private_grid_receipt"])
    saved = parse(grid_raw)
    formal_grid = [(api.arb(t), api.arb(g)) for t, g in saved["all_pairs"]]
    require(len(formal_grid) == 8192 and all(t.contains(t0) and g.contains(g0)
            for (t, g), (t0, g0) in zip(formal_grid, grid)), "the whole original AS directed grid")
    EH = whole_upper(api, inp.strip["selected"]["physical_true_conjugacy_minus_G_norm"])
    omega, phase = pure.original_rotation_and_phase(api, formal_grid[0][1], EH)
    require(omega.str(90) == actual["global_bounds"]["complete_exact_rotation_ball"]
            and phase.str(90) == actual["global_bounds"]["complete_original_source_phase_ball"],
            "same full original rotation and moving source phase before carrier restoration")
    factory = pure.WholeQuadrature(api, formal_grid)
    alpha_pairs = []
    for n in range(1, 2049):
        integral = factory.next()
        formal_integral = api.acb(api.arb(integral.real.str(90)), api.arb(integral.imag.str(90)))
        coefficient, lower = pure.complete_mode_reference(api, n, formal_integral, omega, phase)
        alpha_pairs.append([str(helper.rat(coefficient.real)), str(helper.rat(coefficient.imag))])
        if n % 64 == 0:
            progress("necessary_original_AS_carrier_mode_restoration", {"complete_modes": n, "total_modes": 2048})
    trial = {"kind": "AS_complete_original_alpha_dyadic_trial_v1", "positive_modes": 2048,
             "all_positive_exact_pairs": alpha_pairs, "exact_mean": "0",
             "negative_modes_are_exact_conjugates": True}
    alpha_raw = canonical(trial)
    verify_private(destination/"complete-original-AS-alpha-trial.json", alpha_raw,
                   actual["private_alpha_trial_receipt"])
    return {"complete": True, "kind": "OT_exact_original_AS_carrier_restoration_v1",
            "original_inputs": inputs, "SN_endpoint": endpoint,
            "raw_trial": copy.deepcopy(actual["private_raw_trial_receipt"]),
            "grid": copy.deepcopy(actual["private_grid_receipt"]),
            "alpha_trial": copy.deepcopy(actual["private_alpha_trial_receipt"]),
            "old_scientific_target_calls": 0, "necessary_finite_trial_rematerializations": 1,
            "whole_original_SHA_required": True, "CORETYPE": "unset"}


def carrier_child(args, context):
    destination = args.carrier_directory
    require(destination is not None and args.carrier_receipt is not None
            and not destination.exists() and not args.carrier_receipt.exists(),
            "one new private carrier-only child, without replacing old evidence")
    destination.mkdir(parents=True)
    began = time.perf_counter()
    state = {"kind": "OT_necessary_original_carrier_restoration_progress_v1",
             "mode": args.carrier_mode, "complete": False, "failure": None,
             "stage": "whole_parent_actual_admitted", "progress": {}, "result": None}

    def progress(stage, data):
        state["stage"], state["progress"] = stage, data
        state["wall_seconds"] = time.perf_counter()-began
        atomic(args.carrier_receipt, canonical(state))
        require(state["wall_seconds"] <= PARAMETERS["maximum_scientific_wall_seconds"],
                "whole necessary-carrier prefix preserved before runtime limit")
        print(json.dumps(dict(stage=stage, **data), sort_keys=True), flush=True)

    progress("complete_parent_actual_admitted", {})
    try:
        result = (restore_IR if args.carrier_mode == "IR" else restore_AS)(context, destination, progress)
        state["result"], state["complete"], state["stage"] = result, True, "whole_original_carrier_SHA_restored"
        progress(state["stage"], {})
    except BaseException as exc:
        state["failure"] = {"type": type(exc).__name__, "message": str(exc), "traceback": traceback.format_exc()}
        atomic(args.carrier_receipt, canonical(state))
        raise


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
            and os.environ.get("GITHUB_RUN_ATTEMPT") == "1", "one first public whole original-Theta execution")
    raw = args.manifest.read_bytes()
    require(sha(raw) == args.manifest_sha, "whole exact first Theta manifest")
    manifest = parse(raw)
    require(manifest["kind"] == MANIFEST_KIND and manifest["scientific_kind"] == KIND
            and manifest["stage"] == STAGE and manifest["parameters"] == PARAMETERS
            and manifest["target_order"] == TARGETS and manifest["complete_record_counts"] == [10]
            and manifest["allowed_scientific_fields"] == SCI_FIELDS, "the entire new original Theta target")
    specs = {value["role"]: value for value in manifest["files"]+manifest["historical_inputs"]}
    paths = parse(args.input_map.read_bytes())
    require(set(paths) == set(specs) and sha(Path(__file__).read_bytes()) == specs["science"]["sha256"],
            "every whole source/native private snapshot and the exact new owner")
    contents = {role: Path(path).read_bytes() for role, path in paths.items()}
    context = admit_complete_inputs(contents, specs, manifest)
    if args.carrier_mode is not None:
        carrier_child(args, context)
        return
    require(not args.output.exists(), "retain every earlier actual complete or failed object")
    ir, alpha = context["IR"]["actual"], context["AS"]["actual"]
    document = {
        "identity": {"kind": KIND, "scalar_stage": STAGE, "source_sha256": specs["science"]["sha256"],
            "manifest_sha256": args.manifest_sha, "IR_actual_sha256": specs["IR_actual"]["sha256"],
            "AS_actual_sha256": specs["AS_actual"]["sha256"], "DT_math_sha256": specs["DT_math"]["sha256"],
            "TM_math_sha256": specs["TM_math"]["sha256"], "TP_math_sha256": specs["TP_math"]["sha256"],
            "run_id": os.environ["GITHUB_RUN_ID"], "run_attempt": "1", "event_commit": os.environ["GITHUB_SHA"],
            "actual_checkout_commit": args.checkout, "arithmetic_bits": 320},
        "complete": False, "proved": False, "actual_returncode": None, "failure": None,
        "stage": "whole_IR_AS_SDI_CYA_original_objects_admitted", "completed_targets": [],
        "current_target": None, "candidate_record": None, "new_records": {}, "saved_record_count": 0,
        "parameters": copy.deepcopy(PARAMETERS), "result": None,
        "whole_completed_inputs": {role: {"bytes": item["bytes"], "sha256": item["sha256"]}
                                   for role, item in specs.items()},
        "copied_complete_parent_records": {"IR_joint": {name: copy.deepcopy(ir["new_records"][name])
            for name in context["IR"]["owner"].JOINT_TARGETS}, "AS": copy.deepcopy(alpha["new_records"]),
            "IL": copy.deepcopy(context["IL"]["new_records"])},
        "reference_identity": copy.deepcopy(ir["reference_identity"]),
        "selected_member_identity": copy.deepcopy(ir["selected_member_identity"]),
        "runtime": {}, "wall_seconds": 0.0, "progress": {},
        "old_scientific_target_calls": 0, "necessary_carrier_rematerializations": 0,
        "carrier_restorations": {}, "new_arrays_published": 0, "new_artifacts": 0, "new_Releases": 0,
        "complete_product_choice": None, "private_complete_row_count": 0,
        "private_DT_rows_receipt": None, "private_model_rows_receipt": None,
        "private_Theta_trial_receipt": None, "private_model_multipliers_receipt": None,
        "actual_model_input_records": None,
    }
    require(sorted(document) == SCI_FIELDS, "one complete new Theta scientific schema")
    began = time.perf_counter()
    private = args.output.parent/"private-complete-original-Theta-carriers"
    private.mkdir()

    def save():
        document["wall_seconds"] = time.perf_counter()-began
        raw = canonical(document)
        require(len(raw) <= manifest["operation"]["maximum_scientific_bytes"], "whole small original Theta result")
        atomic(args.output, raw)

    def progress(stage, data):
        document["stage"], document["progress"] = stage, data
        save()
        require(document["wall_seconds"] <= PARAMETERS["maximum_scientific_wall_seconds"],
                "whole new Theta prefix preserved before runtime limit")
        print(json.dumps(dict(stage=stage, **data), sort_keys=True), flush=True)

    save()
    try:
        from importlib.metadata import version
        runtime = {"python": platform.python_version(),
                   "packages": {name: version(name) for name in ("numpy", "python-flint")}}
        require(runtime == manifest["runtime"], "the original immutable directed arithmetic runtime")
        document["runtime"] = runtime
        for mode in ("AS", "IR"):
            directory, receipt_path = private/("original-"+mode), private/(mode+"-restoration.json")
            env = dict(os.environ)
            env.update({name: "1" for name in THREAD_VARIABLES})
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
            require(receipt_path.exists(), "the complete original-carrier child receipt exists")
            receipt = parse(receipt_path.read_bytes())
            document["carrier_restorations"][mode] = receipt
            save()
            require(process.returncode == 0 and receipt["complete"] is True and receipt["failure"] is None
                    and receipt["result"]["whole_original_SHA_required"] is True
                    and receipt["result"]["old_scientific_target_calls"] == 0,
                    "necessary whole original "+mode+" carrier restored, no relaxed identity")
            progress("whole_original_"+mode+"_carrier_SHA_restored", {})

        import flint
        flint.ctx.prec = 320
        api = directed_api(flint)
        arb, acb, rational = api.arb, api.acb, api.rational
        raw = (private/"original-IR/complete-original-IR-trial.f64").read_bytes()
        require(len(raw) == ir["private_trial_receipt"]["bytes"]
                and sha(raw) == ir["private_trial_receipt"]["sha256"], "the whole original IR dyadic trial")
        numbers = struct.unpack("<"+str(192*96*2)+"d", raw)
        require(all(math.isfinite(value) for value in numbers), "every exact finite IR coefficient")
        columns = []
        for j in range(96):
            column = []
            for n in range(192):
                index = 2*(n*96+j)
                real = rational(Fraction(numbers[index]))
                imaginary = rational(Fraction(numbers[index+1]))
                column.append(acb(real, imaginary))
            columns.append(column)
        raw = (private/"original-AS/complete-original-AS-alpha-trial.json").read_bytes()
        require(len(raw) == alpha["private_alpha_trial_receipt"]["bytes"]
                and sha(raw) == alpha["private_alpha_trial_receipt"]["sha256"], "the whole original AS dyadic trial")
        alpha_trial = parse(raw)
        require(alpha_trial["exact_mean"] == "0" and alpha_trial["negative_modes_are_exact_conjugates"] is True,
                "the original complete real mean-zero alpha trial")
        coefficients = [acb(rational(Fraction(a)), rational(Fraction(b)))
                        for a, b in alpha_trial["all_positive_exact_pairs"]]

        def emit(name, value):
            require(name == TARGETS[document["saved_record_count"]]
                    and document["current_target"] is document["candidate_record"] is None,
                    "only the next complete new target may be saved")
            point = value.upper()
            require(point.is_finite() and point >= 0, "one whole directed new upper")
            body = {"ball": point.str(60), "bound": "upper"}
            document["current_target"], document["candidate_record"] = name, body
            save()
            read = parse(args.output.read_bytes())["candidate_record"]
            formal = arb(read["ball"])
            require(formal.is_finite() and formal.contains(point), "complete target saved/read before use")
            document["new_records"][name] = read
            document["completed_targets"].append(name)
            document["saved_record_count"] += 1
            document["current_target"] = document["candidate_record"] = None
            save()
            return formal.upper()

        TP, DT, TM = context["TP"], context["DT"], context["TM"]
        new_norms = TP.complete_new_finite_carrier_norms(api, columns, coefficients)
        norms = {name: emit(name, new_norms[name]) for name in NORM_TARGETS}
        einf, e2 = (whole_upper(api, alpha["new_records"][name])
                    for name in context["AS"]["owner"].TARGETS)
        products = TP.complete_product_candidates(api, alpha_Linf_error=einf, alpha_L2_error=e2,
            G_trial_HS=norms[NORM_TARGETS[0]], positive_G_vector_Wiener=norms[NORM_TARGETS[1]])
        product_values = {name: emit(name, products[name]) for name in PRODUCT_TARGETS}
        selected = PRODUCT_TARGETS[0]
        if product_values[PRODUCT_TARGETS[1]] < product_values[selected]:
            selected = PRODUCT_TARGETS[1]
        document["complete_product_choice"] = {"selected_complete_candidate": selected,
            "both_complete_candidates": {name: copy.deepcopy(document["new_records"][name]) for name in PRODUCT_TARGETS},
            "same_complete_joint_operator": True, "choice_after_whole_save_readback": True,
            "extra_sqrt96": False}
        A0 = emit("complete_true_alpha_Linf_upper", TP.complete_true_alpha_upper(api, norms[NORM_TARGETS[2]], einf))
        joint = TP.complete_original_joint_errors(api, true_alpha_upper=A0,
            whole_alpha_product=product_values[selected],
            whole_IR_energy_error=whole_upper(api, ir["new_records"]["complete_joint_energy_residual_upper"]),
            whole_IR_L2_error=whole_upper(api, ir["new_records"]["complete_joint_L2_residual_upper"]),
            original_model_one_loss_norm=rational(512))
        emit("complete_original_VQ_joint_L2_error_upper", joint["complete_original_VQ_joint_L2_error_upper"])
        E_DT = emit("complete_original_Theta_before_rounding_error_upper",
                    joint["complete_original_Theta_before_rounding_error_upper"])
        progress("complete_new_carrier_norms_and_both_alpha_products_saved", {})

        # Every coefficient of the original same-sign A*G action is retained.
        original_rows = DT.complete_finite_original_source_rows(api, columns, coefficients)
        dt_path = private/"complete-original-DT-rows.jsonl"
        with dt_path.open("wb") as stream:
            for j, row in enumerate(original_rows, 1):
                require(set(row) == set(range(-2240, 2241)), "all signs and the entire finite DT support")
                body = {"row": j, "complete_positive_modes": 2240, "exact_mean": "0",
                    "negative_modes_are_exact_conjugates": True,
                    "all_positive_balls": [[row[n].real.str(90), row[n].imag.str(90)] for n in range(1, 2241)]}
                stream.write(canonical(body))
        dt_raw = dt_path.read_bytes()
        dt_records = [parse(line) for line in dt_raw.splitlines()]
        require(len(dt_records) == 96 and [row["row"] for row in dt_records] == list(range(1, 97)),
                "all96 entire finite DT rows saved/read")
        finite_rows = [[acb(arb(a), arb(b)) for a, b in row["all_positive_balls"]] for row in dt_records]
        require(all(value.real.contains(original_rows[j][n+1].real)
                    and value.imag.contains(original_rows[j][n+1].imag)
                    for j, row in enumerate(finite_rows) for n, value in enumerate(row)),
                "every formal full finite DT coefficient contains its exact action")
        document["private_DT_rows_receipt"] = {"bytes": len(dt_raw), "sha256": sha(dt_raw),
            "complete_rows": 96, "positive_modes": 2240, "negative_modes_are_exact_conjugates": True,
            "original_same_sign_order": True}
        del original_rows
        omega = arb(alpha["global_bounds"]["complete_exact_rotation_ball"])
        phase = arb(alpha["global_bounds"]["complete_original_source_phase_ball"])
        mu_record = alpha["copied_original_records"]["complete_signed_mu"]
        mu = whole_ball(api, mu_record)
        native = context["CYA"]["complete_original_scalar_input_conclusion"]["original_gap_coefficient_record_read_verbatim"]
        native_interval = whole_ball(api, native)
        beta = -mu/4
        require(native_interval.contains(beta), "the same true mean belongs to the original CYA native infinite scope")
        document["actual_model_input_records"] = {
            "complete_original_source_phase_ball": alpha["global_bounds"]["complete_original_source_phase_ball"],
            "complete_exact_rotation_ball": alpha["global_bounds"]["complete_exact_rotation_ball"],
            "complete_signed_mu": copy.deepcopy(mu_record), "CYA_original_native_interval": copy.deepcopy(native),
            "same_full_beta_minus_mu_over4_inside_original_native": True,
            "true_target_basis_phase_a_retained": True, "low_reference_multiplier": "1"}
        balls, model = TM.complete_original_model_rows(api, finite_rows, omega, phase, mu)
        model_body = {"kind": "OT_complete_original_model_multipliers_v1", "complete_modes": 2240,
            "all_modes": [{"mode": value["mode"], "kind": value["kind"],
                "signed_denominator": value["signed_denominator"].str(90),
                "signed_reciprocal": value["signed_reciprocal"].str(90),
                "true_source_phase": value["true_source_phase"].str(90)} for value in model]}
        model_raw = canonical(model_body)
        model_path = private/"complete-original-model-multipliers.json"
        atomic(model_path, model_raw)
        require(model_path.read_bytes() == model_raw, "all signed model multipliers and true phases saved/read")
        document["private_model_multipliers_receipt"] = {"bytes": len(model_raw), "sha256": sha(model_raw),
            "complete_modes": 2240, "low_reference_modes": 96}
        ball_path, trial_path = private/"complete-original-Theta-balls.jsonl", private/"complete-original-Theta-trial.f64"
        formal_rows, exact_rows = [], []
        with ball_path.open("w+b") as stream, trial_path.open("w+b") as trial_stream:
            for j, row in enumerate(balls, 1):
                data = {"row": j, "complete_modes": 2240, "all_real_balls": [value.str(90) for value in row]}
                raw = canonical(data)
                offset = stream.tell()
                stream.write(raw)
                stream.flush()
                stream.seek(offset)
                read = stream.read(len(raw))
                require(read == raw, "entire formal signed Theta row saved/read")
                formal = [arb(value) for value in parse(read)["all_real_balls"]]
                require(len(formal) == 2240 and all(value.contains(old) for value, old in zip(formal, row)),
                        "every full real model-action ball includes the original action")
                selected_values = [float(value.mid()) for value in formal]
                require(all(math.isfinite(value) for value in selected_values), "all finite dyadic Theta trial entries")
                trial_raw = struct.pack("<2240d", *selected_values)
                offset = trial_stream.tell()
                trial_stream.write(trial_raw)
                trial_stream.flush()
                trial_stream.seek(offset)
                require(trial_stream.read(len(trial_raw)) == trial_raw, "entire exact finite Theta row saved/read")
                formal_rows.append(formal)
                exact_rows.append([rational(Fraction(value)) for value in struct.unpack("<2240d", trial_raw)])
                document["private_complete_row_count"] = j
                if j % 8 == 0:
                    progress("complete_original_signed_Theta_row_prefix", {"complete_rows": j, "total_rows": 96})
        ball_raw, trial_raw = ball_path.read_bytes(), trial_path.read_bytes()
        require(len(trial_raw) == 96*2240*8 and len(ball_raw.splitlines()) == 96,
                "the entire signed96x2240 trial and all matching formal balls")
        document["private_model_rows_receipt"] = {"bytes": len(ball_raw), "sha256": sha(ball_raw),
            "complete_rows": 96, "real_modes": 2240, "true_Ya_orthonormal_basis": True}
        document["private_Theta_trial_receipt"] = {"bytes": len(trial_raw), "sha256": sha(trial_raw),
            "shape": [96, 2240], "dtype": "<f8", "order": "C", "exact_dyadic_trial": True,
            "true_target_basis_phase_retained": True, "all_higher_modes_exactly_zero": True}
        rounding, row_squares = TM.complete_model_rounding_error(api, formal_rows, exact_rows)
        E_model = emit("complete_model_action_joint_rounding_error_upper", rounding)
        emit("complete_original_Theta_joint_L2_error_upper", TM.complete_original_Theta_error(api, E_DT, E_model))
        document["result"] = {
            "complete_new_record_order": list(TARGETS), "complete_new_record_count": 10,
            "complete_signed_row_count": 96, "complete_finite_row_modes": 2240,
            "whole_original_VQ_and_Theta_errors_proved": True,
            "same_true_model_low_reference_and_phases_retained": True,
            "both_complete_alpha_product_candidates_saved_before_choice": True,
            "all_aliases_infinite_tails_true_map_and_alpha_errors_retained": True,
            "all_original_carrier_whole_SHA_identical": True,
            "two_independent_original_carrier_runtimes_retained": True,
            "every_signed_model_action_ball_saved_and_read": True,
            "true_target_orthonormal_basis_used": True,
            "extra_sqrt96_applied": False, "physical_mean_slots_eliminated": False,
            "old_norm_residual_cohomology_or_gap_targets_recomputed": False,
            "actual_true_PDE_signed_square_or_full_Schur_proved": False,
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
