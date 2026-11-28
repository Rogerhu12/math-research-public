"""First complete DCP18: a new signed particular of the original Theta.

The entire successful BFP19 is mandatory. Necessary old input carriers
retain their original SHA; no old inverse row, residual or norm is run.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import importlib.util
import json
import os
import platform
import subprocess
import sys
import time
import traceback
from pathlib import Path

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
KIND = "R149_complete_particular_density_Theta_v1"
STAGE = "particular_density_Theta"
MANIFEST_KIND = "R149_complete_particular_density_Theta_inputs_v1"
RUNTIME = {"python": "3.12.14", "packages": {"numpy": "2.3.5", "python-flint": "0.9.0"}}
PARAMETERS = {
    "arithmetic_bits": 320, "private_ball_digits": 110, "decimal_record_digits": 60,
    "maximum_scientific_wall_seconds": 19500, "original_BFP_input_modes": 512,
    "original_alpha_modes": 2048, "new_finite_source_modes": 2560,
    "complete_new_grid_points": 8192, "positive_readout_modes": 96,
    "complete_opposite_head_modes": 2048, "physical_frequency_factor": 4,
    "physical_period": "pi/2", "physical_strip": "1/256",
    "actual_full_opposite_operator_upper": "4/25",
    "same_original_C_energy_adjoint_and_true_inverse": True,
    "all_true_source_target_phases_and_physical_means_retained": True,
    "old_IR96_DWT96_or_Theta96_trial_restored": False,
    "complete_positive_and_negative_alias_rays_paid": True,
    "old_completed_scientific_targets_allowed": 0,
}
SCI_FIELDS = sorted([
    "identity", "parameters", "complete", "proved", "actual_returncode", "failure",
    "stage", "progress", "wall_seconds", "runtime", "completed_targets", "current_target",
    "saved_record_count", "new_records", "whole_BFP_parent_identity", "whole_WMT_parent_identity", "copied_complete_input_records",
    "carrier_restorations", "new_carrier_receipts", "complete_strip_certificate",
    "whole_alpha_product_choice", "whole_global_Theta_choice", "result", "old_scientific_target_calls",
    "new_arrays_published", "new_artifacts", "new_Releases",
])


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                       allow_nan=False)+"\n").encode()


def parse(raw):
    return json.loads(raw, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))


def atomic(path, raw):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".partial")
    temporary.write_bytes(raw)
    os.replace(temporary, path)


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def admit_complete_inputs(contents, specs, manifest, snapshot_paths):
    return load(snapshot_paths["admission"], "_DCP_whole_original_admission").admit(
        contents, specs, manifest, snapshot_paths)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("manifest", "input-map", "output"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--manifest-sha", required=True)
    parser.add_argument("--checkout", required=True)
    parser.add_argument("--carrier-mode", choices=("GRID",))
    parser.add_argument("--carrier-directory", type=Path)
    parser.add_argument("--carrier-receipt", type=Path)
    args = parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true" and os.environ.get("GITHUB_REPOSITORY") == REPO
            and os.environ.get("GITHUB_RUN_ATTEMPT") == "1", "one first public DCP18 execution")
    raw_manifest = args.manifest.read_bytes()
    require(sha(raw_manifest) == args.manifest_sha, "the entire declared DCP manifest")
    manifest = parse(raw_manifest)
    require(manifest["kind"] == MANIFEST_KIND and manifest["scientific_kind"] == KIND
            and manifest["parameters"] == PARAMETERS and manifest["runtime"] == RUNTIME
            and manifest["allowed_scientific_fields"] == SCI_FIELDS,
            "the complete eighteen-target DCP contract")
    specs = {value["role"]: value for value in manifest["files"]+manifest["historical_inputs"]}
    paths = {role: Path(value) for role, value in parse(args.input_map.read_bytes()).items()}
    require(sha(Path(__file__).read_bytes()) == specs["science"]["sha256"], "the actual pinned new owner")
    contents = {role: path.read_bytes() for role, path in paths.items()}
    admitted = admit_complete_inputs(contents, specs, manifest, paths)
    bfp, actual, pure, carriers = (admitted[name] for name in ("BFP_context", "BFP_actual", "pure", "carriers"))
    bnc, uc, old = bfp["BNC"]["admitted"], bfp["UACT"]["admitted"], bfp["original_OT"]
    ot_owner, ot_actual = uc["owner"], uc["actual"]
    if args.carrier_mode is not None:
        bfp["BNC"]["owner"].carrier_child(args, bnc)
        return
    require(not args.output.exists(), "retain every earlier full or partial actual")
    ir, uact = old["IR"]["actual"], bfp["UACT_actual"]
    bt = admitted["BFP_manifest"]["target_order"]
    copied = {
        "IR_H": ir["new_records"]["complete_joint_energy_residual_upper"],
        "IR_L2": ir["new_records"]["complete_joint_L2_residual_upper"],
        "inverse_lift_error": ir["global_bounds"]["inverse_lift_error"],
        "whole_UACT_inverse_error_Linf_product": uact["new_records"]["complete_unit_disk_alpha_inverse_error_Linf_product_upper"],
        "whole_UACT_inverse_error_L2_product": uact["new_records"]["complete_unit_disk_alpha_inverse_error_L2_product_upper"],
        "original_global_Theta_error": actual["copied_complete_input_records"]["global_Theta_error"],
        "complete_WMT14_new_records": admitted["WMT_actual"]["new_records"],
        "complete_WMT14_global_error": admitted["WMT_actual"]["new_records"][admitted["WMT_manifest"]["target_order"][13]],
        "original_BFP_full_target_error": actual["new_records"][bt[13]],
        "original_BFP_Theta_trial_norm": actual["new_records"][bt[15]],
        "prior_two_independent_density_means": actual["new_records"][bt[18]]["prior_two_independent_density_means"],
    }
    document = {
        "identity": {"kind": KIND, "scalar_stage": STAGE, "source_sha256": specs["science"]["sha256"],
            "manifest_sha256": args.manifest_sha, "run_id": os.environ["GITHUB_RUN_ID"], "run_attempt": "1",
            "event_commit": os.environ["GITHUB_SHA"], "actual_checkout_commit": args.checkout,
            "whole_BFP_actual_sha256": specs["BFP_actual"]["sha256"],
            "whole_WMT_actual_sha256": specs["WMT_actual"]["sha256"],
            "whole_UACT_actual_sha256": actual["identity"]["whole_UACT_actual_sha256"]},
        "parameters": PARAMETERS, "complete": False, "proved": False, "actual_returncode": None, "failure": None,
        "stage": "all_complete_successful_BFP_inputs_admitted", "progress": {}, "wall_seconds": 0,
        "runtime": {}, "completed_targets": [], "current_target": None, "saved_record_count": 0, "new_records": {},
        "whole_BFP_parent_identity": copy.deepcopy(admitted["BFP_parent_identity"]),
        "whole_WMT_parent_identity": copy.deepcopy(admitted["WMT_parent_identity"]),
        "copied_complete_input_records": copy.deepcopy(copied), "carrier_restorations": {}, "new_carrier_receipts": {},
        "complete_strip_certificate": None, "whole_alpha_product_choice": None, "whole_global_Theta_choice": None, "result": None,
        "old_scientific_target_calls": 0, "new_arrays_published": 0, "new_artifacts": 0, "new_Releases": 0,
    }
    require(sorted(document) == SCI_FIELDS, "the full small DCP output schema")
    private = args.output.parent/"private-complete-DCP"
    private.mkdir()
    began = time.monotonic()

    def save():
        document["wall_seconds"] = time.monotonic()-began
        raw = canonical(document)
        require(len(raw) < manifest["operation"]["maximum_scientific_bytes"], "the complete small DCP actual")
        atomic(args.output, raw)

    def progress(stage, data):
        document["stage"], document["progress"] = stage, data
        save()
        require(document["wall_seconds"] <= PARAMETERS["maximum_scientific_wall_seconds"],
                "preserve the entire completed new target prefix before timeout")
        print(json.dumps({"stage": stage, **data}, sort_keys=True), flush=True)

    save()
    try:
        from importlib.metadata import version
        runtime = {"python": platform.python_version(), "packages": {name: version(name) for name in RUNTIME["packages"]}}
        require(runtime == RUNTIME and os.environ.get("OPENBLAS_CORETYPE") == "Haswell",
                "the original BFP finite-proposal arithmetic and runtime schedule")
        document["runtime"] = runtime
        directory, receipt_path = private/"original-AS", private/"GRID-restoration.json"
        command = [sys.executable, str(Path(__file__)), "--manifest", str(args.manifest), "--manifest-sha", args.manifest_sha,
            "--input-map", str(args.input_map), "--output", str(args.output), "--checkout", args.checkout,
            "--carrier-mode", "GRID", "--carrier-directory", str(directory), "--carrier-receipt", str(receipt_path)]
        environment = dict(os.environ)
        environment.pop("OPENBLAS_CORETYPE", None)
        with (private/"GRID-restoration.log").open("wb") as log:
            child = subprocess.Popen(command, env=environment, stdout=log, stderr=subprocess.STDOUT)
            try:
                last = 0.0
                while child.poll() is None:
                    if time.monotonic()-last >= 30:
                        if receipt_path.exists():
                            document["carrier_restorations"]["AS_grid"] = parse(receipt_path.read_bytes())
                        progress("necessary_original_AS_grid_only_reconstruction", {})
                        last = time.monotonic()
                    time.sleep(1)
            finally:
                if child.poll() is None:
                    child.terminate()
                    try:
                        child.wait(timeout=20)
                    except subprocess.TimeoutExpired:
                        child.kill()
                        child.wait()
        receipt = parse(receipt_path.read_bytes())
        document["carrier_restorations"]["AS_grid"] = receipt
        require(child.returncode == 0 and receipt["complete"] is True and receipt["failure"] is None,
                "the complete original endpoint/raw/grid carrier succeeded")
        import numpy as np
        import flint
        flint.ctx.prec, flint.ctx.cap = 320, 9
        api = ot_owner.directed_api(flint)
        api.midpoint_real = lambda value: value.mid()
        api.midpoint_complex = lambda value: api.acb(value.real.mid(), value.imag.mid())
        bfp["BFP_owner"] = admitted["BFP_owner"]
        admitted["BFP_owner"].main = ot_owner.forbidden

        def upper(record):
            return ot_owner.whole_upper(api, record)

        def whole_file(name, body):
            raw = canonical(body)
            path = private/name
            atomic(path, raw)
            require(path.read_bytes() == raw, "the whole new private object saved/read: "+name)
            document["new_carrier_receipts"][name] = {"bytes": len(raw), "sha256": sha(raw)}
            return parse(path.read_bytes())

        def complex_file(name, values, kind):
            body = whole_file(name, {"kind": kind, "complete_count": len(values),
                "all_balls": [[v.real.str(110), v.imag.str(110)] for v in values]})
            formal = [api.acb(api.arb(a), api.arb(b)) for a, b in body["all_balls"]]
            require(len(formal) == len(values) and all(a.real.contains(b.real) and a.imag.contains(b.imag)
                    for a, b in zip(formal, values)), "every complete complex ball survives serialization")
            return formal

        def emit(index, value):
            require(index == document["saved_record_count"] and index not in (15, 17)
                    and value.is_finite() and value.upper() >= 0, "the next complete new scalar")
            name, point = pure.TARGETS[index], value.upper()
            record = {"ball": point.str(60), "bound": "upper"}
            require(api.arb(record["ball"]).contains(point), "the whole directed scalar round trip")
            document["current_target"] = name
            document["new_records"][name] = record
            document["completed_targets"].append(name)
            document["saved_record_count"] += 1
            document["current_target"] = None
            save()
            return upper(parse(args.output.read_bytes())["new_records"][name])

        saved = {}
        global_candidates = {"whole_original_UACT_global": copied["original_global_Theta_error"],
                             "whole_actual_WMT14_global": copied["complete_WMT14_global_error"]}
        global_selected = min(global_candidates, key=lambda name: upper(global_candidates[name]))
        document["whole_global_Theta_choice"] = {"selected": global_selected,
            "both_complete_candidates": copy.deepcopy(global_candidates),
            "same_original_Theta_and_trial": True, "low96_error_used_globally": False}
        save()
        strip = pure.complete_p_hat_strip(api, old["states"][1], old["prior"]["K_sines"], old["prior"]["K_cosines"])
        document["complete_strip_certificate"] = {key: {"ball": value.str(60), "bound": "upper"}
            for key, value in strip.items()}
        saved[0] = emit(0, strip["compound_derivative_perturbation"])
        grid_raw = (directory/"complete-original-AS-grid.json").read_bytes()
        w_pairs, receipt = carriers.restore_needed_w(api, bnc, grid_raw, private/"same-original-w-only", progress)
        document["carrier_restorations"]["DWT_w_only"] = receipt
        coordinates, receipt = carriers.restore_BFP_reference(np, flint, api, bfp, actual, ot_owner,
            bnc, grid_raw, w_pairs, private/"same-complete-BFP512", progress, atomic)
        document["carrier_restorations"]["BFP_reference"] = receipt
        receipt = bfp["carriers"].restore_original_alpha_from_saved_grid(api, old, ot_owner, grid_raw, directory, progress)
        document["carrier_restorations"]["AS_alpha"] = receipt
        alpha_body = parse((directory/"complete-original-AS-alpha-trial.json").read_bytes())
        multipliers, source_b, receipt = carriers.restore_original_model(api, old, ot_owner, ot_actual, private)
        document["carrier_restorations"]["original_model"] = receipt
        source = pure.complete_model_source(api, coordinates, multipliers, source_b)
        source = complex_file("complete-new-model-source.json", source, "DCP_complete_original_model_source512_v1")
        v = pure.complete_v_coefficients(api, source, alpha_body["all_positive_exact_pairs"])
        v = complex_file("complete-new-normalized-source.json", v, "DCP_complete_normalized_source2560_v1")
        norms = pure.complete_source_norms(api, v, saved[0])
        for index in range(1, 5):
            saved[index] = emit(index, norms[pure.TARGETS[index]])
        norms = pure.complete_model_primitive_norms(api, source)
        for index in range(5, 7):
            saved[index] = emit(index, norms[pure.TARGETS[index]])
        products = pure.complete_alpha_source_products(api, upper(copied["IR_H"]), upper(copied["IR_L2"]),
            upper(copied["whole_UACT_inverse_error_Linf_product"]), upper(copied["whole_UACT_inverse_error_L2_product"]),
            saved[5], saved[6])
        for index in (7, 8):
            saved[index] = emit(index, products[pure.TARGETS[index]])
        selected = min((7, 8), key=saved.__getitem__)
        document["whole_alpha_product_choice"] = {"selected": pure.TARGETS[selected],
            "both_complete_candidates": {pure.TARGETS[i]: document["new_records"][pure.TARGETS[i]] for i in (7, 8)}}
        save()
        old_grid, receipt = carriers.restore_IR_grid_only(api, old, ot_owner, private, progress)
        document["carrier_restorations"]["IR_grid_only"] = receipt
        grid = pure.complete_new_grid(api, old_grid, old["states"][1], old["prior"]["K_sines"], old["prior"]["K_cosines"])
        body = whole_file("complete-new-particular-grid.json", {"kind": "DCP_complete_8192_inverse_density_grid_v1",
            "original4096_sha256": ir["private_grid_receipt"]["sha256"], "all_balls": [value.str(110) for value in grid]})
        formal_grid = [api.arb(text) for text in body["all_balls"]]
        require(len(formal_grid) == 8192 and all(a.contains(b) for a, b in zip(formal_grid, grid)),
                "all8192 full compound values saved/read")
        sampler = pure.CompletePrimitiveSamples(api, formal_grid)
        for n, coefficient in enumerate(v, 1):
            sampler.append(n, coefficient)
            if n % 64 == 0:
                progress("complete_new_particular_primitive_samples", {"complete_modes": n, "total_modes": 2560})
        samples = complex_file("complete-new-particular-samples.json", sampler.complete(),
                               "DCP_complete_8192_particular_primitive_samples_v1")
        transform = pure.complete_fft(api, samples)
        transform = complex_file("complete-new-particular-transform.json", transform,
                                 "DCP_complete_8192_particular_directed_DFT_v1")
        positive, opposite = pure.complete_signed_heads(api, transform, saved[3], saved[4])
        positive = complex_file("complete-new-particular-positive96.json", positive,
                                "DCP_complete_positive_density_readout96_v1")
        opposite = complex_file("complete-new-particular-opposite2048.json", opposite,
                                "DCP_complete_opposite_density_head2048_v1")
        saved[9] = emit(9, pure.complete_leakage_head(api, opposite))
        saved[10] = emit(10, pure.complete_leakage_tail(api, saved[3]))
        saved[11] = emit(11, pure.complete_true_map_energy_error(api, upper(copied["inverse_lift_error"]), saved[1], saved[2]))
        saved[12] = emit(12, pure.complete_true_leakage(saved[9], saved[10], saved[11]))
        readouts, centers, radius = pure.complete_readout_centers(api, positive)
        body = whole_file("complete-new-signed-root-readouts.json", {"kind": "DCP_complete_signed_root96_readouts_v1",
            "all_balls": [value.str(110) for value in readouts],
            "all_exact_centers": [str(bfp["carriers"].midpoint_fraction(value)) for value in centers]})
        formal_readouts = [api.arb(text) for text in body["all_balls"]]
        require(all(a.contains(b) for a, b in zip(formal_readouts, readouts)), "all complete signed root readouts")
        # Pay every full serialized readout radius, including its conversion.
        exact_centers = body["all_exact_centers"]
        centers = [api.rational(value) for value in exact_centers]
        radius = sum((abs(value-center).upper()**2 for value, center in zip(formal_readouts, centers)), api.zero).sqrt().upper()
        saved[13] = emit(13, radius)
        saved[14] = emit(14, pure.complete_finite_Theta_error(api, saved[12], saved[11], saved[selected], saved[13]))

        def emit_signed(index, error_index, finite):
            require(index == document["saved_record_count"], "the next complete signed conclusion")
            balls = [value+api.arb(0, saved[error_index]) for value in centers]
            texts = [value.str(60) for value in balls]
            require(all(api.arb(text).contains(value) for text, value in zip(texts, balls)),
                    "all96 complete signed enclosures formally saved")
            record = {"kind": "DCP_complete_signed_finite_Theta_reference_v1" if finite
                      else "DCP_complete_signed_true_Theta_nu_column_v1", "rows": 96,
                "all96_exact_signed_centers": exact_centers, "all96_signed_balls": texts,
                "joint_l2_error_upper": document["new_records"][pure.TARGETS[error_index]],
                "same_complete_original_BFP512_reference": True,
                "all_true_target_source_and_root_phases_retained": True,
                "true_infinite_high_modes_set_to_zero": False,
                "old_low96_Theta_error_used_globally": False,
                "full_physical_Schur_claimed": False}
            if not finite:
                record["prior_two_independent_density_means"] = copy.deepcopy(copied["prior_two_independent_density_means"])
                record["whole_BFP_target_column_error"] = copy.deepcopy(copied["original_BFP_full_target_error"])
                record["whole_global_Theta_error"] = copy.deepcopy(global_candidates[global_selected])
            document["current_target"] = pure.TARGETS[index]
            document["new_records"][pure.TARGETS[index]] = record
            document["completed_targets"].append(pure.TARGETS[index])
            document["saved_record_count"] += 1
            document["current_target"] = None
            save()
            require(parse(args.output.read_bytes())["new_records"][pure.TARGETS[index]] == record,
                    "the entire signed conclusion saved/read")

        emit_signed(15, 14, True)
        saved[16] = emit(16, pure.complete_full_true_nu_error(saved[14], upper(copied["original_BFP_Theta_trial_norm"]),
            upper(global_candidates[global_selected]), upper(copied["original_BFP_full_target_error"])))
        emit_signed(17, 16, False)
        document["result"] = {
            "complete_new_record_order": pure.TARGETS, "complete_new_record_count": 18,
            "true_entire_C_inverse_and_Krein_identity_used": True,
            "complete_new_particular_Theta_reference_proved": True,
            "complete_true_Theta_nu_column_proved": True,
            "all2560_source_8192_samples_and2048_opposite_modes_retained": True,
            "both_alias_rays_and_complete_infinite_tail_retained": True,
            "true_p_alpha_BFP_PDE_and_global_Theta_error_retained": True,
            "both_independent_physical_means_retained": True,
            "old_IR96_DWT96_or_Theta96_trial_restored": False,
            "old_completed_scientific_targets_recomputed": False,
            "full_physical_Schur_proved": False, "topic_completion_proved": False,
        }
        document["complete"] = document["proved"] = True
        document["actual_returncode"] = 0
        progress("complete_new_particular_density_Theta", {"completed_targets": 18})
    except BaseException as exc:
        document["complete"] = document["proved"] = False
        document["actual_returncode"] = 1
        document["failure"] = {"type": type(exc).__name__, "message": str(exc), "traceback": traceback.format_exc()}
        save()
        raise


if __name__ == "__main__":
    main()
