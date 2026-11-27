"""BR first complete96 rows of the ORIGINAL target normalizer B inverse.

One isolated child restores only the whole completed BW signed carriers.
The parent selects one new192-mode exact-dyadic trial and certifies every
signed residual output through2240, including all true-w infinite error.
The original full-space WBP energy inverse supplies the exact row identity.
"""
from __future__ import annotations
import argparse
import ast
import copy
import hashlib
import json
import os
import platform
import subprocess
import sys
import time
import traceback
import types
from fractions import Fraction
from pathlib import Path

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby/"
KIND = "R149_complete_original_target_B_inverse_rows_v1"
STAGE = "original_target_B_inverse_rows"
MANIFEST_KIND = "R149_complete_original_target_B_inverse_rows_inputs_v1"
SOURCE_PATH = TOPIC+"scripts/fourfold_codazzi_target_B_inverse_rows_owner.py"
WORKER_PATH = TOPIC+"scripts/fourfold_codazzi_target_B_inverse_rows_public_worker.py"
GENERATOR_PATH = TOPIC+"scripts/make_target_B_inverse_rows_manifest.py"
TARGETS = ["complete_I_trial_Hilbert_Schmidt_upper", "complete_positive_I_trial_vector_Wiener_upper",
    "complete_finite_target_B_adjoint_energy_residual_upper", "complete_target_w_Linf_product_upper",
    "complete_target_w_L2_product_upper", "complete_target_B_adjoint_joint_energy_residual_upper",
    "complete_target_B_inverse96_joint_L2_row_error_upper"]
PARAMETERS = {
    "arithmetic_bits": 320, "power_series_cap": 9, "decimal_record_digits": 60, "private_ball_digits": 90,
    "row_count": 96, "trial_positive_modes": 192, "w_positive_modes": 2048,
    "complete_residual_positive_modes": 2240, "physical_frequency_factor": 4, "physical_period": "pi/2",
    "target_normalizer": "B=Id+T_w I", "energy_adjoint": "Bdagger=Id-T_w I",
    "target_rows": "E96_a_star B_inverse", "target_basis": "sqrt(2)*cos(4*n*x-2*n*a)",
    "true_target_phase": "a=2*H(0)=b-Omega", "physical_mean_slots_eliminated": False,
    "whole_space_energy_inverse_norm_upper": "1", "whole_true_receiver_L2_norm_upper": "sqrt(96)",
    "whole_finite_and_infinite_residuals_retained": True,
    "BW_carrier_CORETYPE": "unset", "new_trial_CORETYPE": "Haswell", "all_threads": 1,
    "old_completed_scientific_targets_allowed": 0, "maximum_scientific_wall_seconds": 16800,
}
SCI_FIELDS = sorted([
    "identity", "complete", "proved", "actual_returncode", "failure", "stage", "parameters",
    "completed_targets", "current_target", "candidate_record", "new_records", "saved_record_count",
    "result", "whole_completed_inputs", "copied_complete_parent_records", "runtime", "wall_seconds", "progress",
    "old_scientific_target_calls", "necessary_carrier_rematerializations", "carrier_restoration",
    "trial_selection", "private_trial_receipt", "private_row_trial_receipt", "private_residual_receipt",
    "complete_residual_row_count", "complete_true_phase_a_ball", "complete_product_choice",
    "new_arrays_published", "new_artifacts", "new_Releases",
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
            and specs["generator"]["path"] == GENERATOR_PATH, "the complete first original target-B row entry")
    admission = definitions(contents["admission"], "_BR_complete_BW_input_admission")
    return admission.admit_complete_inputs(contents, specs, manifest)


def forbidden(*args, **kwargs):
    raise RuntimeError("a completed BW or ASR scientific target cannot run during carrier-only recovery")


def restore_original_BW(context, destination, progress):
    """Reproduce only finite signed witnesses; require every original BW whole SHA."""
    require("OPENBLAS_CORETYPE" not in os.environ
            and all(os.environ.get(name) == "1" for name in THREAD_VARIABLES),
            "the complete original BW/ASR runtime schedule")
    old = context["BW"]
    owner, admitted, actual = old["owner"], old["admitted"], old["actual"]
    owner.main = forbidden
    for name in ("complete_analytic_parameters", "complete_vi_mode_error", "complete_vi_tail",
                 "complete_vi_errors", "complete_w_errors"):
        require(hasattr(admitted["BW_math"], name), "every original completed BW error entrypoint is identified")
        setattr(admitted["BW_math"], name, forbidden)
    restored, observed = owner.observe_original_quadrature(admitted, destination, progress)
    require(restored == actual["original_carrier_restoration"]
            and observed == actual["private_quadrature_receipt"],
            "the entire original endpoint/raw/grid/alpha and quadrature identities match")
    import flint
    require(flint.ctx.prec == 320 and flint.ctx.cap == 9, "the original complete directed finite arithmetic")
    api = admitted["carrier"].directed_api(flint)
    _, _, _, receipts = owner.restore_new_vi_w_trial_bytes(api, destination)
    require(receipts["vi"] == actual["private_vi_trial_receipt"]
            and receipts["w"] == actual["private_w_trial_receipt"],
            "the exact original entire vi and w signed carrier SHA identities")
    return {"kind": "BR_complete_original_BW_carrier_restoration_v1", "complete": True,
        "original_ASR_carriers": restored, "whole_quadrature": observed,
        "whole_vi_trial": receipts["vi"], "whole_w_trial": receipts["w"],
        "whole_original_SHA_required": True, "old_scientific_target_calls": 0,
        "necessary_finite_trial_rematerializations": 1, "CORETYPE": "unset"}


def carrier_child(args, context):
    require(args.carrier_directory is not None and args.carrier_receipt is not None
            and not args.carrier_directory.exists() and not args.carrier_receipt.exists(),
            "one new private BW carrier-only child")
    args.carrier_directory.mkdir(parents=True)
    state = {"kind": "BR_necessary_original_BW_carrier_progress_v1", "complete": False,
             "failure": None, "stage": "complete_BW_actual_admitted", "progress": {}, "result": None}
    began = time.perf_counter()

    def progress(stage, data):
        state["stage"], state["progress"], state["wall_seconds"] = stage, data, time.perf_counter()-began
        atomic(args.carrier_receipt, canonical(state))
        require(state["wall_seconds"] <= PARAMETERS["maximum_scientific_wall_seconds"],
                "the whole necessary-carrier prefix is saved before runtime expiry")

    progress(state["stage"], {})
    try:
        state["result"] = restore_original_BW(context, args.carrier_directory, progress)
        state["complete"], state["stage"] = True, "whole_original_BW_carrier_SHA_restored"
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
    ap.add_argument("--carrier-only", action="store_true")
    ap.add_argument("--carrier-directory", type=Path)
    ap.add_argument("--carrier-receipt", type=Path)
    args = ap.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true" and os.environ.get("GITHUB_REPOSITORY") == REPO
            and os.environ.get("GITHUB_RUN_ATTEMPT") == "1", "one first public original target-B row target")
    raw = args.manifest.read_bytes()
    require(sha(raw) == args.manifest_sha, "the complete first target-B rows manifest")
    manifest = parse(raw)
    require(manifest["kind"] == MANIFEST_KIND and manifest["scientific_kind"] == KIND
            and manifest["stage"] == STAGE and manifest["parameters"] == PARAMETERS
            and manifest["target_order"] == TARGETS and manifest["complete_record_counts"] == [7]
            and manifest["allowed_scientific_fields"] == SCI_FIELDS, "all seven new complete row bounds")
    specs = {value["role"]: value for value in manifest["files"]+manifest["historical_inputs"]}
    paths = parse(args.input_map.read_bytes())
    require(set(paths) == set(specs) and sha(Path(__file__).read_bytes()) == specs["science"]["sha256"],
            "the whole immutable source snapshot and every declared original input")
    contents = {role: Path(path).read_bytes() for role, path in paths.items()}
    context = admit_complete_inputs(contents, specs, manifest)
    if args.carrier_only:
        carrier_child(args, context)
        return
    require(not args.output.exists(), "retain all earlier scientific outcomes")
    parent, pure = context["BW"]["actual"], context["BR_math"]
    document = {
        "identity": {"kind": KIND, "scalar_stage": STAGE, "source_sha256": specs["science"]["sha256"],
            "manifest_sha256": args.manifest_sha, "BW_actual_sha256": specs["BW_actual"]["sha256"],
            "BW_execution_sha256": specs["BW_execution"]["sha256"], "BW_manifest_sha256": specs["BW_manifest"]["sha256"],
            "BR_math_sha256": specs["BR_math"]["sha256"], "proposal_sha256": specs["proposal"]["sha256"],
            "arithmetic_bits": 320, "run_id": os.environ["GITHUB_RUN_ID"], "run_attempt": "1",
            "actual_checkout_commit": args.checkout},
        "complete": False, "proved": False, "actual_returncode": None, "failure": None,
        "stage": "whole_successful_BW_actual_admitted", "parameters": PARAMETERS,
        "completed_targets": [], "current_target": None, "candidate_record": None,
        "new_records": {}, "saved_record_count": 0, "result": None,
        "whole_completed_inputs": {role: {"bytes": value["bytes"], "sha256": value["sha256"]}
                                   for role, value in specs.items()},
        "copied_complete_parent_records": {"BW_identity": copy.deepcopy(parent["identity"]),
            "BW_all_four_error_records": copy.deepcopy(parent["new_records"]),
            "BW_original_records": copy.deepcopy(parent["copied_complete_parent_records"])},
        "runtime": None, "wall_seconds": 0, "progress": {}, "old_scientific_target_calls": 0,
        "necessary_carrier_rematerializations": 0, "carrier_restoration": None, "trial_selection": None,
        "private_trial_receipt": None, "private_row_trial_receipt": None, "private_residual_receipt": None,
        "complete_residual_row_count": 0, "complete_true_phase_a_ball": None, "complete_product_choice": None,
        "new_arrays_published": 0, "new_artifacts": 0, "new_Releases": 0,
    }
    require(sorted(document) == SCI_FIELDS, "the complete original target-B rows result schema")
    began = time.perf_counter()
    private = args.output.parent/"private-complete-target-B-inverse-rows"
    private.mkdir()

    def save():
        document["wall_seconds"] = time.perf_counter()-began
        raw = canonical(document)
        require(len(raw) <= manifest["operation"]["maximum_scientific_bytes"], "whole small original B-row result")
        atomic(args.output, raw)

    def progress(stage, data):
        document["stage"], document["progress"] = stage, data
        save()
        require(document["wall_seconds"] <= PARAMETERS["maximum_scientific_wall_seconds"],
                "complete original target-row progress saved before runtime expiry")
        print(json.dumps(dict(stage=stage, **data), sort_keys=True), flush=True)

    save()
    try:
        from importlib.metadata import version
        runtime = {"python": platform.python_version(),
                   "packages": {name: version(name) for name in ("numpy", "python-flint")}}
        require(runtime == manifest["runtime"] and os.environ.get("OPENBLAS_CORETYPE") == "Haswell"
                and all(os.environ.get(name) == "1" for name in THREAD_VARIABLES),
                "the fixed new finite-solve runtime with all threads specified")
        document["runtime"] = runtime
        carrier_dir, carrier_receipt = private/"whole-original-BW", private/"whole-original-BW-progress.json"
        command = [sys.executable, str(Path(__file__).resolve()), "--manifest", str(args.manifest.resolve()),
            "--manifest-sha", args.manifest_sha, "--input-map", str(args.input_map.resolve()),
            "--output", str(args.output.resolve()), "--checkout", args.checkout,
            "--carrier-only", "--carrier-directory", str(carrier_dir), "--carrier-receipt", str(carrier_receipt)]
        environment = dict(os.environ)
        for name in ("OPENBLAS_CORETYPE", "GITHUB_TOKEN", "GIT_CONFIG_COUNT", "GIT_CONFIG_KEY_0", "GIT_CONFIG_VALUE_0"):
            environment.pop(name, None)
        environment.update(PYTHONDONTWRITEBYTECODE="1", **{name: "1" for name in THREAD_VARIABLES})
        document["necessary_carrier_rematerializations"] = 1
        save()
        with (private/"original-BW-carrier-child.log").open("wb") as stream:
            child = subprocess.Popen(command, cwd=private, env=environment, stdout=stream, stderr=subprocess.STDOUT)
            last_sha = None
            try:
                while child.poll() is None:
                    if carrier_receipt.exists():
                        receipt_raw = carrier_receipt.read_bytes()
                        if sha(receipt_raw) != last_sha:
                            last_sha = sha(receipt_raw)
                            document["carrier_restoration"] = parse(receipt_raw)
                            progress("necessary_original_BW_carrier_restoration", {
                                "original_stage": document["carrier_restoration"]["stage"],
                                **document["carrier_restoration"]["progress"]})
                    require(time.perf_counter()-began <= PARAMETERS["maximum_scientific_wall_seconds"],
                            "necessary carrier child exceeded the same fixed whole-target budget")
                    time.sleep(1)
            finally:
                if child.poll() is None:
                    child.kill()
                child.wait()
        require(carrier_receipt.exists(), "the whole necessary carrier child left its actual receipt")
        document["carrier_restoration"] = parse(carrier_receipt.read_bytes())
        restored = document["carrier_restoration"]
        require(child.returncode == 0 and restored["complete"] is True and restored["failure"] is None
                and restored["result"]["whole_original_SHA_required"] is True
                and restored["result"]["whole_w_trial"] == parent["private_w_trial_receipt"],
                "the complete exact original target-w carrier precedes every new row target")
        progress("whole_original_BW_signed_carrier_restored", {"complete_w_positive_modes": 2048})

        import flint
        import numpy as np
        flint.ctx.prec, flint.ctx.cap = 320, 9
        original_carrier = context["BW"]["admitted"]["carrier"]
        api = original_carrier.directed_api(flint)
        api.acb_poly = flint.acb_poly

        def upper(record):
            return original_carrier.whole_upper(api, record)

        def encode(value):
            point = value.upper()
            require(point.is_finite() and point >= 0, "one whole nonnegative directed new row bound")
            body = {"ball": point.str(60), "bound": "upper"}
            formal = api.arb(body["ball"])
            require(formal.contains(point), "whole directed row bound round trip")
            return body, formal.upper()

        def record(name, value):
            require(name == TARGETS[document["saved_record_count"]], "the complete fixed seven-target order")
            body, formal = encode(value)
            document["current_target"], document["candidate_record"] = name, body
            save()
            saved = parse(args.output.read_bytes())["candidate_record"]
            require(api.arb(saved["ball"]).contains(formal), "whole new row scalar saved/read before use")
            document["new_records"][name] = saved
            document["completed_targets"].append(name)
            document["saved_record_count"] = len(document["completed_targets"])
            document["current_target"] = document["candidate_record"] = None
            save()
            return upper(saved)

        wraw = (carrier_dir/"complete-original-w-trial.json").read_bytes()
        require(len(wraw) == parent["private_w_trial_receipt"]["bytes"]
                and sha(wraw) == parent["private_w_trial_receipt"]["sha256"], "the entire original signed w before use")
        wbody = parse(wraw)
        wpairs = wbody["all_positive_exact_pairs"]
        require(len(wpairs) == 2048 and wbody["exact_mean"] == "0"
                and wbody["negative_modes_are_exact_conjugates"] is True, "all original signs and the exact target mean")
        global_bounds = parent["copied_complete_parent_records"]["AS_global_bounds"]
        phase = api.arb(global_bounds["complete_original_source_phase_ball"])-api.arb(global_bounds["complete_exact_rotation_ball"])
        phase_text = phase.str(90)
        formal_phase = api.arb(phase_text)
        require(formal_phase.contains(phase), "the whole true target phase a=b-Omega is retained")
        document["complete_true_phase_a_ball"] = phase_text
        trial_raw, selection = context["proposal"].choose_trial_bytes(np, wpairs, float(formal_phase.mid()))
        trial_path = private/"complete-new-y-trial.f64"
        atomic(trial_path, trial_raw)
        require(trial_path.read_bytes() == trial_raw, "all192x96 exact dyadic trial coefficients saved/read")
        values = np.frombuffer(trial_path.read_bytes(), dtype="<f8").reshape(192, 96, 2)
        require(bool(np.isfinite(values).all()), "the entire saved trial is finite")
        document["trial_selection"] = selection
        document["private_trial_receipt"] = {"bytes": len(trial_raw), "sha256": sha(trial_raw),
            "shape": [192, 96, 2], "dtype": "<f8", "negative_modes_are_exact_conjugates": True,
            "exact_mean": "0", "finite_solve_is_a_certificate": False}
        columns, exact_rows = [], []
        for j in range(96):
            column, row = [], []
            for n in range(1, 193):
                a, b = (Fraction.from_float(float(value)) for value in values[n-1, j])
                column.append(api.acb(api.rational(a), api.rational(b)))
                row.append([str(a/(4*n)), str(b/(4*n))])
            columns.append(column)
            exact_rows.append(row)
        row_body = {"kind": "BR_complete_original_target_B_inverse_exact_row_trial_v1", "rows": 96,
            "positive_modes": 192, "all_positive_exact_pairs": exact_rows, "exact_mean": "0",
            "negative_modes_are_exact_conjugates": True, "row_definition": "G*y_j; coefficient multiplier1/(4*n)"}
        row_raw = canonical(row_body)
        row_path = private/"complete-new-target-B-row-trial.json"
        atomic(row_path, row_raw)
        require(row_path.read_bytes() == row_raw, "all96 exact rational row representatives saved/read")
        document["private_row_trial_receipt"] = {"bytes": len(row_raw), "sha256": sha(row_raw),
            "rows": 96, "positive_modes": 192, "exact_mean": "0", "negative_modes_are_exact_conjugates": True,
            "complete_trial_only_restoration_without_error_targets": True}
        positive_w = [api.acb(api.rational(Fraction(a)), api.rational(Fraction(b))) for a, b in wpairs]
        residuals = pure.complete_same_sign_residual(api, columns, positive_w, formal_phase)
        residual_path = private/"complete-new-target-B-residual-rows.jsonl"
        digest, size = hashlib.sha256(), 0
        formal_residuals = []
        with residual_path.open("w+b") as stream:
            for j, column in enumerate(residuals, 1):
                pairs = [[value.real.str(90), value.imag.str(90)] for value in column]
                body = {"row": j, "all2240_positive_residual_balls": pairs,
                        "negative_modes_are_exact_conjugates": True, "exact_mean": "0"}
                raw = canonical(body)
                offset = stream.tell()
                stream.write(raw)
                stream.flush()
                stream.seek(offset)
                read = stream.read(len(raw))
                require(read == raw, "every complete signed2240-mode residual saved/read")
                formal = [api.acb(api.arb(a), api.arb(b))
                          for a, b in parse(read)["all2240_positive_residual_balls"]]
                require(len(formal) == 2240 and all(value.real.contains(old.real) and value.imag.contains(old.imag)
                        for value, old in zip(formal, column)), "the entire finite residual ball survives storage")
                formal_residuals.append(formal)
                digest.update(read)
                size += len(read)
                document["complete_residual_row_count"] = j
                if j % 8 == 0:
                    progress("complete_original_target_B_residual_rows_saved", {"complete_rows": j, "total_rows": 96})
        require(residual_path.stat().st_size == size and sha(residual_path.read_bytes()) == digest.hexdigest(),
                "all96x2240 complete signed residual coefficients")
        document["private_residual_receipt"] = {"bytes": size, "sha256": digest.hexdigest(), "rows": 96,
            "positive_modes": 2240, "all_finite_tail_outputs193_through2240_retained": True,
            "negative_modes_are_exact_conjugates": True, "true_phase_and_all_finite_rounding_enclosed": True}
        norms = pure.complete_primitive_trial_norms(api, columns)
        for name in TARGETS[:2]:
            record(name, norms[name])
        record(TARGETS[2], pure.complete_finite_energy_residual(api, formal_residuals))
        werrors = document["copied_complete_parent_records"]["BW_all_four_error_records"]
        products = pure.complete_w_product_candidates(api, upper(werrors["complete_target_w_trial_Linf_error_upper"]),
            upper(werrors["complete_target_w_trial_L2_error_upper"]), upper(document["new_records"][TARGETS[0]]),
            upper(document["new_records"][TARGETS[1]]))
        for name in TARGETS[3:5]:
            record(name, products[name])
        candidates = [(upper(document["new_records"][name]), name) for name in TARGETS[3:5]]
        selected, selected_name = min(candidates, key=lambda value: value[0])
        document["complete_product_choice"] = {"candidate_order": TARGETS[3:5], "selected": selected_name,
            "selected_whole_upper": copy.deepcopy(document["new_records"][selected_name]),
            "selection_on_complete_saved_records": True}
        save()
        complete = pure.complete_target_row_error(api, upper(document["new_records"][TARGETS[2]]), selected)
        energy = record(TARGETS[5], complete[TARGETS[5]])
        record(TARGETS[6], (energy/2).upper())
        document["result"] = {
            "complete_new_record_order": list(TARGETS), "complete_new_record_count": 7,
            "complete_true_inverse_row_count": 96, "complete_finite_residual_positive_modes": 2240,
            "same_original_target_B_and_same_sign_projection_order": True,
            "whole_original_BW_carriers_restored_with_all_SHA": True,
            "all96_true_original_B_inverse_rows_enclosed_in_full_L2": True,
            "whole_space_energy_inverse_onto_and_norm_one_used": True,
            "true_target_phase_and_all_exact_rational_row_trials_retained": True,
            "all2240_outputs_and_complete_w_infinite_error_paid": True,
            "both_whole_w_product_candidates_saved_before_selection": True,
            "all_signed_residual_balls_saved_and_read": True,
            "old_BW_ASR_cohomology_norm_or_transport_targets_recomputed": False,
            "extra_sqrt96_applied_to_joint_row_error": False,
            "physical_mean_slots_eliminated": False, "finite_Galerkin_solve_used_as_full_inverse_certificate": False,
            "SC_raw96_pairings_used_as_full_physical_columns": False,
            "physical_PDE_or_full_Schur_proved": False, "topic_completion_proved": False,
        }
        document["complete"] = document["proved"] = True
        document["actual_returncode"] = 0
        document["stage"] = "complete_"+STAGE+"_branch"
    except BaseException as exc:
        document["actual_returncode"] = 1
        document["failure"] = {"type": type(exc).__name__, "message": str(exc), "traceback": traceback.format_exc()}
        save()
        raise
    save()
    print(json.dumps(dict(complete=True, original_B_inverse_rows=96, complete_residual_modes=2240,
                          new_targets=7, old_scientific_target_calls=0,
                          output_sha256=sha(args.output.read_bytes())), sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
