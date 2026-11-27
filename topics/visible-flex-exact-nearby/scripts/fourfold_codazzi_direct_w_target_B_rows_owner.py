"""DWT2 followed by the first complete BR7 original target inverse rows.

Only the complete original endpoint/raw192/8192-grid is restored. All new
signed w2048 coefficients and both full errors are saved before the seven
original whole-space row targets. No BW actual or old alpha restoration is
asserted, and the true w, both mean slots and full2240 residual are retained.
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
KIND = "R149_complete_direct_w_and_target_B_rows_v1"
STAGE = "direct_w_and_target_B_rows"
MANIFEST_KIND = "R149_complete_direct_w_and_target_B_rows_inputs_v1"
SOURCE_PATH = TOPIC+"scripts/fourfold_codazzi_direct_w_target_B_rows_owner.py"
WORKER_PATH = TOPIC+"scripts/fourfold_codazzi_direct_w_target_B_rows_public_worker.py"
GENERATOR_PATH = TOPIC+"scripts/make_direct_w_target_B_rows_manifest.py"
BR_TARGETS = ["complete_I_trial_Hilbert_Schmidt_upper", "complete_positive_I_trial_vector_Wiener_upper",
    "complete_finite_target_B_adjoint_energy_residual_upper", "complete_target_w_Linf_product_upper",
    "complete_target_w_L2_product_upper", "complete_target_B_adjoint_joint_energy_residual_upper",
    "complete_target_B_inverse96_joint_L2_row_error_upper"]
DWT_TARGETS = ["complete_direct_unit_disk_target_w_Linf_error_upper",
    "complete_direct_unit_disk_target_w_L2_error_upper"]
TARGETS = DWT_TARGETS+BR_TARGETS
PARAMETERS = {
    "arithmetic_bits": 320, "power_series_cap": 9, "decimal_record_digits": 60, "private_ball_digits": 90,
    "row_count": 96, "trial_positive_modes": 192, "w_positive_modes": 2048,
    "complete_residual_positive_modes": 2240, "physical_frequency_factor": 4, "physical_period": "pi/2",
    "target_normalizer": "B=Id+T_w I", "energy_adjoint": "Bdagger=Id-T_w I",
    "target_rows": "E96_a_star B_inverse", "target_basis": "sqrt(2)*cos(4*n*x-2*n*a)",
    "true_target_phase": "a=2*H(0)=b-Omega", "physical_mean_slots_eliminated": False,
    "whole_space_energy_inverse_norm_upper": "1", "whole_true_receiver_L2_norm_upper": "sqrt(96)",
    "whole_finite_and_infinite_residuals_retained": True,
    "original_grid_CORETYPE": "unset", "new_trial_CORETYPE": "Haswell", "all_threads": 1,
    "old_completed_scientific_targets_allowed": 0, "maximum_scientific_wall_seconds": 16800,
    "w_coefficient_input": "complete direct DWT w=vi-alpha with the original cohomological divisor",
    "complete_raw_source_positive_modes": 192, "new_unit_disk_grid_points": 8192,
    "complete_new_w_positive_modes": 2048, "both_whole_DWT_errors_before_BR": True,
    "old_AS_alpha_trial_materialized_or_used": False,
    "old_quadrature_or_cohomological_mode_calls": 0,
    "old_complete_ASR_tail_envelope_reused_without_recomputation": True,
}
SCI_FIELDS = sorted([
    "identity", "complete", "proved", "actual_returncode", "failure", "stage", "parameters",
    "completed_targets", "current_target", "candidate_record", "new_records", "saved_record_count",
    "result", "whole_completed_inputs", "copied_complete_parent_records", "runtime", "wall_seconds", "progress",
    "old_scientific_target_calls", "necessary_carrier_rematerializations", "carrier_restoration",
    "trial_selection", "private_trial_receipt", "private_row_trial_receipt", "private_residual_receipt",
    "complete_residual_row_count", "complete_true_phase_a_ball", "complete_product_choice",
    "new_arrays_published", "new_artifacts", "new_Releases",
    "unit_disk_input_receipt", "complete_w_mode_count", "complete_w_mode_prefix",
    "private_w_modes_receipt", "private_w_trial_receipt", "copied_original_tail_bounds",
    "complete_DWT_error_records",
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
    admission = definitions(contents["admission"], "_DWTB_complete_original_ASR_and_direct_w_admission")
    context = admission.admit_complete_inputs(contents, specs, manifest)
    require(context["DWT_math"].TARGETS == DWT_TARGETS, "both complete original direct-w error targets")
    return context


def restore_original_grid(context, original_owner_raw, destination, progress):
    """Whole original objects needed by DWT, before the old alpha-mode boundary."""
    require("OPENBLAS_CORETYPE" not in os.environ
            and all(os.environ.get(name) == "1" for name in THREAD_VARIABLES),
            "the complete original endpoint/raw/grid runtime schedule")
    return context["grid_restore"].restore_complete_original_grid(
        context, original_owner_raw, destination, progress)


def carrier_child(args, context, contents):
    require(args.carrier_directory is not None and args.carrier_receipt is not None
            and not args.carrier_directory.exists() and not args.carrier_receipt.exists(),
            "one new private original-grid-only child")
    args.carrier_directory.mkdir(parents=True)
    state = {"kind": "DWTB_necessary_original_grid_progress_v1", "complete": False,
             "failure": None, "stage": "complete_ASR_actual_admitted", "progress": {}, "result": None}
    began = time.perf_counter()

    def progress(stage, data):
        state["stage"], state["progress"], state["wall_seconds"] = stage, data, time.perf_counter()-began
        atomic(args.carrier_receipt, canonical(state))
        require(state["wall_seconds"] <= PARAMETERS["maximum_scientific_wall_seconds"],
                "the whole necessary-carrier prefix is saved before runtime expiry")

    progress(state["stage"], {})
    try:
        state["result"] = restore_original_grid(context, contents["carrier_original_owner"], args.carrier_directory, progress)
        state["complete"], state["stage"] = True, "whole_original_endpoint_raw_grid_SHA_restored"
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
            and manifest["target_order"] == TARGETS and manifest["complete_record_counts"] == [9]
            and manifest["allowed_scientific_fields"] == SCI_FIELDS, "both new complete direct-w errors followed by seven whole original row bounds")
    specs = {value["role"]: value for value in manifest["files"]+manifest["historical_inputs"]}
    paths = parse(args.input_map.read_bytes())
    require(set(paths) == set(specs) and sha(Path(__file__).read_bytes()) == specs["science"]["sha256"],
            "the whole immutable source snapshot and every declared original input")
    contents = {role: Path(path).read_bytes() for role, path in paths.items()}
    context = admit_complete_inputs(contents, specs, manifest)
    if args.carrier_only:
        carrier_child(args, context, contents)
        return
    require(not args.output.exists(), "retain all earlier scientific outcomes")
    parent, pure = context["AS"]["actual"], context["BR_math"]
    document = {
        "identity": {"kind": KIND, "scalar_stage": STAGE, "source_sha256": specs["science"]["sha256"],
            "manifest_sha256": args.manifest_sha, "AS_actual_sha256": specs["AS_actual"]["sha256"],
            "AS_execution_sha256": specs["AS_execution"]["sha256"], "AS_manifest_sha256": specs["AS_manifest"]["sha256"],
            "DWT_math_sha256": specs["DWT_math"]["sha256"], "UDR_math_sha256": specs["UDR_math"]["sha256"],
            "grid_restore_sha256": specs["grid_restore"]["sha256"],
            "BR_math_sha256": specs["BR_math"]["sha256"], "proposal_sha256": specs["proposal"]["sha256"],
            "arithmetic_bits": 320, "run_id": os.environ["GITHUB_RUN_ID"], "run_attempt": "1",
            "actual_checkout_commit": args.checkout},
        "complete": False, "proved": False, "actual_returncode": None, "failure": None,
        "stage": "whole_successful_ASR_actual_admitted", "parameters": PARAMETERS,
        "completed_targets": [], "current_target": None, "candidate_record": None,
        "new_records": {}, "saved_record_count": 0, "result": None,
        "whole_completed_inputs": {role: {"bytes": value["bytes"], "sha256": value["sha256"]}
                                   for role, value in specs.items()},
        "copied_complete_parent_records": {"AS_identity": copy.deepcopy(parent["identity"]),
            "AS_all_completed_error_records": copy.deepcopy(parent["new_records"]),
            "AS_global_bounds": copy.deepcopy(parent["global_bounds"]),
            "AS_original_records": copy.deepcopy(parent["copied_original_records"])},
        "runtime": None, "wall_seconds": 0, "progress": {}, "old_scientific_target_calls": 0,
        "necessary_carrier_rematerializations": 0, "carrier_restoration": None, "trial_selection": None,
        "private_trial_receipt": None, "private_row_trial_receipt": None, "private_residual_receipt": None,
        "complete_residual_row_count": 0, "complete_true_phase_a_ball": None, "complete_product_choice": None,
        "new_arrays_published": 0, "new_artifacts": 0, "new_Releases": 0,
        "unit_disk_input_receipt": None, "complete_w_mode_count": 0, "complete_w_mode_prefix": None,
        "private_w_modes_receipt": None, "private_w_trial_receipt": None,
        "copied_original_tail_bounds": copy.deepcopy(parent["complete_tail_bounds"]),
        "complete_DWT_error_records": None,
    }
    require(sorted(document) == SCI_FIELDS, "the complete original target-B rows result schema")
    began = time.perf_counter()
    private = args.output.parent/"private-direct-w-and-target-B-rows"
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
        carrier_dir, carrier_receipt = private/"whole-original-AS-grid", private/"whole-original-AS-grid-progress.json"
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
        with (private/"original-AS-grid-child.log").open("wb") as stream:
            child = subprocess.Popen(command, cwd=private, env=environment, stdout=stream, stderr=subprocess.STDOUT)
            last_sha = None
            try:
                while child.poll() is None:
                    if carrier_receipt.exists():
                        receipt_raw = carrier_receipt.read_bytes()
                        if sha(receipt_raw) != last_sha:
                            last_sha = sha(receipt_raw)
                            document["carrier_restoration"] = parse(receipt_raw)
                            progress("necessary_original_AS_grid_restoration", {
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
                and restored["result"]["whole_original_endpoint_raw_grid_SHA_required"] is True
                and restored["result"]["grid"] == parent["private_grid_receipt"]
                and restored["result"]["raw_trial"] == parent["private_raw_trial_receipt"]
                and restored["result"]["SN_endpoint"] == parent["original_endpoint_restoration"]
                and restored["result"]["old_alpha_trial_materialized_or_used"] is False
                and restored["result"]["old_quadrature_or_cohomological_mode_calls"] == 0,
                "every needed whole original input, without an invented alpha or BW restoration")
        progress("whole_original_endpoint_raw192_grid8192_restored", {"complete_grid_points": 8192})

        import flint
        import numpy as np
        flint.ctx.prec, flint.ctx.cap = 320, 9
        original_carrier = context["carrier"]
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
            require(name == TARGETS[document["saved_record_count"]], "the complete fixed DWT2 then BR7 natural target order")
            body, formal = encode(value)
            document["current_target"], document["candidate_record"] = name, body
            save()
            saved = parse(args.output.read_bytes())["candidate_record"]
            require(saved == body and api.arb(saved["ball"]).contains(value.upper()),
                    "whole new scalar contains its complete original upper after save/read")
            document["new_records"][name] = saved
            document["completed_targets"].append(name)
            document["saved_record_count"] = len(document["completed_targets"])
            document["current_target"] = document["candidate_record"] = None
            save()
            return upper(saved)

        # DWT is a first complete w carrier, directly from the exact unit-disk input.
        # The already completed alpha scalar/cohomology and UDR row targets do not run.
        DWT, UDR = context["DWT_math"], context["UDR_math"]
        api.midpoint_real = lambda value: value.mid()
        api.midpoint_complex = lambda value: api.acb(value.real.mid(), value.imag.mid())
        grid_raw = (carrier_dir/"complete-original-AS-grid.json").read_bytes()
        grid_sha = sha(grid_raw)
        require(len(grid_raw) == parent["private_grid_receipt"]["bytes"]
                and grid_sha == parent["private_grid_receipt"]["sha256"],
                "all original8192 raw192/map input balls retain their whole identity")
        grid_body = parse(grid_raw)
        require(grid_body["complete_count"] == 8192 and len(grid_body["all_pairs"]) == 8192,
                "every whole original grid point")
        grid = [(api.arb(a), api.arb(b)) for a, b in grid_body["all_pairs"]]
        kernel = UDR.UnitDiskPhaseInput(api, grid)

        def exact_point_string(value):
            require(value.is_finite() and value.is_exact(), "one complete exact dyadic point")
            numerator, exponent = map(int, value.mid().man_exp())
            point = (Fraction(numerator*(1 << exponent)) if exponent >= 0
                     else Fraction(numerator, 1 << (-exponent)))
            require(api.rational(point).is_exact() and api.rational(point) == value,
                    "the entire exact point survives its rational representation")
            return str(point)

        def saved_upper(value):
            return encode(value)[0]

        def saved_lower(value):
            point = value.lower()
            body = {"ball": point.str(60), "bound": "lower"}
            require(api.arb(body["ball"]).contains(point), "the entire strict lower survives saving")
            return body

        input_body = {"kind": "UDR_complete_unit_disk_dyadic_phase_input_v1",
            "whole_original_grid_sha256": grid_sha, "complete_nodes": 8192,
            "complete_mean_raw_radius_upper": saved_upper(kernel.raw_radius),
            "all_exact_u_sreal_simag_and_tau_balls": [
                [exact_point_string(kernel.u[m]), exact_point_string(kernel.s[m].real),
                 exact_point_string(kernel.s[m].imag), kernel.tau[m].str(90)] for m in range(8192)],
            "phase_modulus_one_is_exact": True, "old_rectangular_power_recurrence_used": False}
        input_raw = canonical(input_body)
        input_path = private/"complete-new-unit-disk-phase-input.json"
        atomic(input_path, input_raw)
        saved_input = parse(input_path.read_bytes())
        require(saved_input == input_body, "all8192 new disk input points and radii are saved/read")
        for index, (u, sr, si, tau) in enumerate(saved_input["all_exact_u_sreal_simag_and_tau_balls"]):
            formal_u = api.rational(Fraction(u))
            formal_s = api.acb(api.rational(Fraction(sr)), api.rational(Fraction(si)))
            formal_tau = api.arb(tau)
            require(formal_u == kernel.u[index] and formal_s == kernel.s[index]
                    and formal_tau.contains(kernel.tau[index]), "each whole saved exact disk input")
            kernel.u[index], kernel.uabs[index], kernel.s[index], kernel.tau[index] = (
                formal_u, abs(formal_u).upper(), formal_s, formal_tau.upper())
        kernel.raw_radius = upper(saved_input["complete_mean_raw_radius_upper"])
        input_sha = sha(input_raw)
        document["unit_disk_input_receipt"] = {"bytes": len(input_raw), "sha256": input_sha,
            "complete_nodes": 8192, "whole_original_grid_sha256": grid_sha,
            "every_complete_point_and_radius_saved_and_read": True}
        progress("all_new_DWT_unit_disk_inputs_saved_and_read", {"complete_nodes": 8192})
        global_bounds = document["copied_complete_parent_records"]["AS_global_bounds"]
        omega = api.arb(global_bounds["complete_exact_rotation_ball"])
        source_phase = api.arb(global_bounds["complete_original_source_phase_ball"])
        source_columns = [upper(value) for value in global_bounds["complete_source_error_derivative_columns"]]
        require(len(source_columns) == 4, "all four whole original source derivative columns")
        T = upper(global_bounds["new_raw_trial_Astrip_upper"])
        EH = upper(global_bounds["complete_original_H_minus_G_upper"])
        G1 = upper(global_bounds["complete_original_G_derivative_upper"])
        m_ball = original_carrier.whole_ball(api, global_bounds["complete_original_map_imaginary_lower"])
        require(m_ball.is_finite() and m_ball.lower() > 0, "the same complete original positive map lower")
        m_lower, sigma = m_ball.lower(), api.rational(1, 128)
        alias_ratio = (-4*sigma*8192).exp().upper()
        require(alias_ratio < 1, "the entire original8192 alias series converges")
        modes_path = private/"complete-new-direct-w-modes.jsonl"
        one_input_path = private/"current-complete-direct-w-mode-input.json"
        accum = DWT.WholeWErrors(api)
        mode_fields = {"complete_direct_w_coefficient_error_upper",
            "complete_disk_phase_trial_rounding_upper", "complete_source_model_alias_divisor_fee_upper"}
        with modes_path.open("wb") as stream:
            for n in range(1, 2049):
                disk = kernel.next()
                reference, divisor_lower = DWT.complete_w_reference(api, n, disk, omega, source_phase)
                exact_w = api.acb(reference.real.mid(), reference.imag.mid())
                pair = [exact_point_string(exact_w.real), exact_point_string(exact_w.imag)]
                source_candidates = [(value/(4*n)**r).upper() for r, value in enumerate(source_columns)]
                model = (4*n*EH*T*(-4*n*m_lower*sigma).exp()).upper()
                aliases = (2*T*(4*n*G1*sigma).exp()*alias_ratio/(1-alias_ratio)).upper()
                mode_input = {"kind": "DWT_complete_direct_mode_input_v1", "mode": n,
                    "complete_grid_points": 8192, "new_unit_disk_input_sha256": input_sha,
                    "whole_original_grid_sha256": grid_sha,
                    "all_exact_new_w_pair": pair,
                    "complete_reference_ball": [reference.real.str(90), reference.imag.str(90)],
                    "complete_original_divisor_lower": saved_lower(divisor_lower),
                    "all_four_source_candidate_uppers": [saved_upper(value) for value in source_candidates],
                    "complete_model_upper": saved_upper(model), "complete_alias_upper": saved_upper(aliases),
                    "complete_quadrature_disk_center": [disk["center"].real.str(90), disk["center"].imag.str(90)],
                    "complete_quadrature_disk_radius_upper": saved_upper(disk["radius"])}
                atomic(one_input_path, canonical(mode_input))
                formal_input = parse(one_input_path.read_bytes())
                require(formal_input == mode_input, "one entire natural coefficient input saved/read")
                formal_reference = api.acb(*(api.arb(value) for value in formal_input["complete_reference_ball"]))
                require(formal_reference.real.contains(reference.real)
                        and formal_reference.imag.contains(reference.imag),
                        "all phase/disk/reference rounding survives the formal input")
                formal_w = api.acb(*(api.rational(Fraction(value)) for value in formal_input["all_exact_new_w_pair"]))
                require(formal_w == exact_w, "the new trial coefficient was saved before its error target")
                full_source = min(upper(value) for value in formal_input["all_four_source_candidate_uppers"])
                values = DWT.complete_w_mode_error(api, formal_reference,
                    api.arb(formal_input["complete_original_divisor_lower"]["ball"]).lower(), formal_w,
                    full_source, upper(formal_input["complete_model_upper"]), upper(formal_input["complete_alias_upper"]))
                require(set(values) == mode_fields, "every complete direct-w error component")
                body = {"kind": "DWT_complete_direct_w_mode_record_v1", "mode": n,
                    "whole_mode_input": formal_input,
                    "complete_w_error_records": {name: saved_upper(value) for name, value in values.items()}}
                mode_raw = canonical(body)
                offset = stream.tell()
                stream.write(mode_raw)
                stream.flush()
                os.fsync(stream.fileno())
                with modes_path.open("rb") as check:
                    check.seek(offset)
                    saved_raw = check.readline()
                require(saved_raw == mode_raw, "each whole new w mode saved/read before accumulation")
                formal_mode = parse(saved_raw)
                accum.append(n, upper(formal_mode["complete_w_error_records"]["complete_direct_w_coefficient_error_upper"]))
                document["complete_w_mode_count"] = n
                if n % 64 == 0:
                    document["complete_w_mode_prefix"] = {
                        "complete_positive_modes": n,
                        "complete_nonnegative_Linf_head_upper": saved_upper(accum.head_Linf),
                        "complete_nonnegative_L2_head_squared_upper": saved_upper(accum.head_L2_squared),
                        "full_original_tail_not_yet_added": True,
                        "unfinished_head_is_not_a_whole_error_target": True}
                    progress("complete_new_direct_w_mode_prefix", {"complete_modes": n, "total_modes": 2048})
        whole_modes_raw = modes_path.read_bytes()
        whole_modes = [parse(line) for line in whole_modes_raw.splitlines()]
        require(len(whole_modes) == 2048 and [mode["mode"] for mode in whole_modes] == list(range(1, 2049)),
                "the entire natural new w carrier has no missing mode")
        formal_accum = DWT.WholeWErrors(api)
        exact_pairs = []
        for n, mode in enumerate(whole_modes, 1):
            inp = mode["whole_mode_input"]
            require(mode["kind"] == "DWT_complete_direct_w_mode_record_v1"
                    and inp["mode"] == n and inp["complete_grid_points"] == 8192
                    and inp["new_unit_disk_input_sha256"] == input_sha
                    and inp["whole_original_grid_sha256"] == grid_sha
                    and set(mode["complete_w_error_records"]) == mode_fields,
                    "every entire saved mode keeps all original and new input identities")
            pair = inp["all_exact_new_w_pair"]
            require(len(pair) == 2 and all(api.rational(Fraction(v)).is_exact() for v in pair),
                    "both exact dyadic components of every saved w coefficient")
            exact_pairs.append(pair)
            formal_accum.append(n, upper(mode["complete_w_error_records"]["complete_direct_w_coefficient_error_upper"]))
        wbody = {"kind": "DWT_complete_direct_true_target_w_exact_trial_v1",
            "positive_modes": 2048, "all_positive_exact_pairs": exact_pairs,
            "exact_mean": "0", "negative_modes_are_exact_conjugates": True,
            "same_original_w_equals_vi_minus_alpha": True,
            "whole_original_grid_sha256": grid_sha, "new_unit_disk_input_sha256": input_sha}
        wraw = canonical(wbody)
        wpath = private/"complete-new-direct-w-trial.json"
        atomic(wpath, wraw)
        require(wpath.read_bytes() == wraw and parse(wpath.read_bytes()) == wbody,
                "the entire first direct-w exact signed carrier is saved and read")
        document["private_w_trial_receipt"] = {"bytes": len(wraw), "sha256": sha(wraw),
            "positive_modes": 2048, "exact_mean": "0", "negative_modes_are_exact_conjugates": True,
            "same_original_w_equals_vi_minus_alpha": True, "whole_original_grid_sha256": grid_sha,
            "new_unit_disk_input_sha256": input_sha}
        document["private_w_modes_receipt"] = {"bytes": len(whole_modes_raw), "sha256": sha(whole_modes_raw),
            "complete_positive_modes": 2048, "complete_nodes_per_mode": 8192,
            "all_whole_mode_inputs_and_error_records_saved_read": True,
            "original_cohomological_divisor_phase_and_source192_retained": True,
            "new_unit_disk_input_sha256": input_sha, "whole_new_w_trial_sha256": sha(wraw)}
        save()
        tail = document["copied_original_tail_bounds"]
        errors = formal_accum.finish_with_original_whole_tail_envelope(
            upper(tail["complete_Linf_tail"]), upper(tail["complete_L2_tail"]))
        for name in DWT_TARGETS:
            record(name, errors[name])
        completed_DWT = parse(args.output.read_bytes())
        require(completed_DWT["saved_record_count"] == 2 and completed_DWT["completed_targets"] == DWT_TARGETS,
                "both whole new DWT errors are formal before the first BR target")
        document["complete_DWT_error_records"] = {
            name: completed_DWT["new_records"][name] for name in DWT_TARGETS}
        save()
        require(parse(args.output.read_bytes())["complete_DWT_error_records"] == document["complete_DWT_error_records"],
                "both complete direct-w errors are saved/read under their own source identity")
        progress("complete_DWT2_saved_before_first_original_BR7", {})

        wraw = (private/"complete-new-direct-w-trial.json").read_bytes()
        require(len(wraw) == document["private_w_trial_receipt"]["bytes"]
                and sha(wraw) == document["private_w_trial_receipt"]["sha256"], "the entire original signed w before use")
        wbody = parse(wraw)
        wpairs = wbody["all_positive_exact_pairs"]
        require(len(wpairs) == 2048 and wbody["exact_mean"] == "0"
                and wbody["negative_modes_are_exact_conjugates"] is True, "all original signs and the exact target mean")
        global_bounds = parent["global_bounds"]
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
        for name in BR_TARGETS[:2]:
            record(name, norms[name])
        record(BR_TARGETS[2], pure.complete_finite_energy_residual(api, formal_residuals))
        werrors = parse(args.output.read_bytes())["complete_DWT_error_records"]
        products = pure.complete_w_product_candidates(api, upper(werrors[DWT_TARGETS[0]]),
            upper(werrors[DWT_TARGETS[1]]), upper(document["new_records"][BR_TARGETS[0]]),
            upper(document["new_records"][BR_TARGETS[1]]))
        for name in BR_TARGETS[3:5]:
            record(name, products[name])
        candidates = [(upper(document["new_records"][name]), name) for name in BR_TARGETS[3:5]]
        selected, selected_name = min(candidates, key=lambda value: value[0])
        document["complete_product_choice"] = {"candidate_order": BR_TARGETS[3:5], "selected": selected_name,
            "selected_whole_upper": copy.deepcopy(document["new_records"][selected_name]),
            "selection_on_complete_saved_records": True}
        save()
        complete = pure.complete_target_row_error(api, upper(document["new_records"][BR_TARGETS[2]]), selected)
        energy = record(BR_TARGETS[5], complete[BR_TARGETS[5]])
        record(BR_TARGETS[6], (energy/2).upper())
        document["result"] = {
            "complete_new_record_order": list(TARGETS), "complete_new_record_count": 9,
            "complete_true_inverse_row_count": 96, "complete_finite_residual_positive_modes": 2240,
            "same_original_target_B_and_same_sign_projection_order": True,
            "whole_original_endpoint_raw_grid_restored_with_all_SHA": True,
            "complete_new_w2048_trial_with_original_phase_and_zero_mean": True,
            "both_complete_DWT_errors_saved_read_before_BR": True,
            "complete_old_ASR_tail_envelope_reused_without_recomputation": True,
            "old_alpha_trial_materialized_or_used": False,
            "BW_actual_claimed": False,
            "old_quadrature_or_cohomological_mode_calls": 0,
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
                          new_targets=9, old_scientific_target_calls=0,
                          output_sha256=sha(args.output.read_bytes())), sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
