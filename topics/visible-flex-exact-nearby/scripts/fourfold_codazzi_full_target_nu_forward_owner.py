"""First BFP19 whole forward strict-nu column and original Theta consumer.

All19 targets are new. Whole original NP/DWTB/OT/UACT carrier identities
are retained; no completed BNC observation, old residual/norm or gap target
is rerun. Every new coefficient, point and signed column is saved/read in
full before its norm. Reconstructible arrays remain private to the job.
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
TOPIC = "topics/visible-flex-exact-nearby/"
KIND = "R147_complete_full_target_nu_forward_v1"
STAGE = "full_target_nu_forward"
MANIFEST_KIND = "R147_complete_full_target_nu_forward_inputs_v1"
RUNTIME = {"python": "3.12.14", "packages": {"numpy": "2.3.5", "python-flint": "0.9.0"}}
PARAMETERS = {"arithmetic_bits": 320, "decimal_record_digits": 60, "private_ball_digits": 110,
    "maximum_scientific_wall_seconds": 19500, "forward_trial_modes": 512, "original_w_modes": 2048,
    "whole_forward_image_modes": 2560, "whole_pullback_grid": 8192, "physical_source_modes": 96,
    "original_Theta_shape": [96, 2240], "new_signed_column_rows": 96, "new_complete_targets": 19,
    "physical_frequency": 4, "physical_period": "pi/2", "strip": "1/128",
    "physical_means_eliminated": False, "true_target_phase_replaced_by_midpoint": False,
    "old_completed_target_calls": 0, "old_BNC_observation_calls": 0,
    "proposal_only": "512 positive-block binary64 solve after periodic inverse resampling"}
SCI_FIELDS = sorted(["identity", "parameters", "complete", "proved", "actual_returncode", "failure",
    "stage", "progress", "wall_seconds", "runtime", "completed_targets", "current_target", "new_records",
    "saved_record_count", "copied_complete_input_records", "carrier_restorations", "row_restoration",
    "NP_restoration", "original_Theta_restoration", "new_carrier_receipts", "trial_proposal",
    "whole_w_product_choice", "result", "old_scientific_target_calls", "new_arrays_published", "new_artifacts", "new_Releases"])


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
    return load(snapshot_paths["admission"], "_BFP_full_original_input_admission").admit(
        contents, specs, manifest, snapshot_paths)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("manifest", "input-map", "output"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--manifest-sha", required=True)
    parser.add_argument("--checkout", required=True)
    parser.add_argument("--carrier-mode", choices=("GRID", "IR"))
    parser.add_argument("--carrier-directory", type=Path)
    parser.add_argument("--carrier-receipt", type=Path)
    args = parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true" and os.environ.get("GITHUB_REPOSITORY") == REPO
            and os.environ.get("GITHUB_RUN_ATTEMPT") == "1", "one first public complete BFP19 target group")
    raw = args.manifest.read_bytes()
    require(sha(raw) == args.manifest_sha, "the entire new BFP manifest")
    manifest = parse(raw)
    require(manifest["kind"] == MANIFEST_KIND and manifest["scientific_kind"] == KIND
            and manifest["parameters"] == PARAMETERS and manifest["allowed_scientific_fields"] == SCI_FIELDS,
            "the whole declared BFP19 contract")
    specs = {item["role"]: item for item in manifest["files"]+manifest["historical_inputs"]}
    paths = {role: Path(value) for role, value in parse(args.input_map.read_bytes()).items()}
    require(sha(Path(__file__).read_bytes()) == specs["science"]["sha256"], "the actual pinned BFP owner")
    contents = {role: path.read_bytes() for role, path in paths.items()}
    admitted = admit_complete_inputs(contents, specs, manifest, paths)
    bnc, uc, pure, carriers = admitted["BNC"]["admitted"], admitted["UACT"]["admitted"], admitted["pure"], admitted["carriers"]
    old, ot_owner, ot_actual = admitted["original_OT"], uc["owner"], uc["actual"]
    if args.carrier_mode is not None:
        if args.carrier_mode == "GRID":
            admitted["BNC"]["owner"].carrier_child(args, bnc)
        else:
            ot_owner.carrier_child(args, old)
        return
    require(not args.output.exists(), "retain every earlier complete or failed target outcome")
    np_actual, po_actual, sb_actual, dw = (bnc["parents"][key]["actual"] for key in ("NP", "PO", "SB", "DW"))
    jc, poi = bnc["PO_prior"]["JC"], bnc["PO_prior"]
    uact_actual = admitted["UACT_actual"]
    copied = {
        "N0": po_actual["new_records"]["complete_NP_even_physical_trial_L2_upper"],
        "Db": sb_actual["new_records"]["complete_true_NP_short_waist_density_error_upper"],
        "BH": poi["old_bounds"]["BH"], "m": jc["new_records"]["complete_interpolation_derivative_lower"],
        "EH": jc["copied_prior_scalar_records"]["EH"], "G0": jc["copied_prior_scalar_records"]["G0"],
        "G1": jc["copied_prior_scalar_records"]["G1"], "H1": jc["copied_prior_scalar_records"]["H1"],
        "w_Linf": dw["new_records"]["complete_direct_unit_disk_target_w_Linf_error_upper"],
        "w_L2": dw["new_records"]["complete_direct_unit_disk_target_w_L2_error_upper"],
        "global_Theta_error": uact_actual["new_records"]["complete_unit_disk_original_Theta_joint_L2_error_upper"],
        "VQ_error": uact_actual["new_records"]["complete_unit_disk_original_VQ_joint_L2_error_upper"],
        "model_rounding": ot_actual["new_records"]["complete_model_action_joint_rounding_error_upper"],
    }
    document = {"identity": {"kind": KIND, "scalar_stage": STAGE, "source_sha256": specs["science"]["sha256"],
        "manifest_sha256": args.manifest_sha, "run_id": os.environ["GITHUB_RUN_ID"], "run_attempt": "1",
        "event_commit": os.environ["GITHUB_SHA"], "actual_checkout_commit": args.checkout,
        "whole_BNC_manifest_sha256": specs["BNC_manifest"]["sha256"], "whole_UACT_actual_sha256": specs["UACT_actual"]["sha256"]},
        "parameters": PARAMETERS, "complete": False, "proved": False, "actual_returncode": None, "failure": None,
        "stage": "all_whole_original_inputs_admitted", "progress": {}, "wall_seconds": 0, "runtime": {},
        "completed_targets": [], "current_target": None, "new_records": {}, "saved_record_count": 0,
        "copied_complete_input_records": copy.deepcopy(copied), "carrier_restorations": {}, "row_restoration": None,
        "NP_restoration": None, "original_Theta_restoration": None, "new_carrier_receipts": {},
        "trial_proposal": None, "whole_w_product_choice": None, "result": None,
        "old_scientific_target_calls": 0, "new_arrays_published": 0, "new_artifacts": 0, "new_Releases": 0}
    require(sorted(document) == SCI_FIELDS, "the full BFP output schema")
    private = args.output.parent/"private-complete-BFP"
    private.mkdir()
    began = time.monotonic()

    def save():
        document["wall_seconds"] = time.monotonic()-began
        raw = canonical(document)
        require(len(raw) < manifest["operation"]["maximum_scientific_bytes"], "the complete BFP small result")
        atomic(args.output, raw)

    def progress(stage, details):
        document["stage"], document["progress"] = stage, details
        save()
        require(document["wall_seconds"] < PARAMETERS["maximum_scientific_wall_seconds"], "preserve whole BFP prefix before timeout")
        print(json.dumps({"stage": stage, **details}, sort_keys=True), flush=True)

    save()
    try:
        from importlib.metadata import version
        runtime = {"python": platform.python_version(), "packages": {name: version(name) for name in RUNTIME["packages"]}}
        require(runtime == RUNTIME and os.environ.get("OPENBLAS_CORETYPE") == "Haswell", "the same complete original numerical runtime")
        document["runtime"] = runtime
        for mode in ("GRID", "IR"):
            directory = private/("original-AS" if mode == "GRID" else "original-IR")
            receipt_path = private/(mode+"-restoration.json")
            command = [sys.executable, str(Path(__file__)), "--manifest", str(args.manifest), "--manifest-sha", args.manifest_sha,
                "--input-map", str(args.input_map), "--output", str(args.output), "--checkout", args.checkout,
                "--carrier-mode", mode, "--carrier-directory", str(directory), "--carrier-receipt", str(receipt_path)]
            environment = dict(os.environ)
            if mode == "GRID":
                environment.pop("OPENBLAS_CORETYPE", None)
            with (private/(mode+"-restoration.log")).open("wb") as log:
                child = subprocess.Popen(command, env=environment, stdout=log, stderr=subprocess.STDOUT)
                try:
                    last = 0.0
                    while child.poll() is None:
                        if time.monotonic()-last >= 45:
                            if receipt_path.exists():
                                document["carrier_restorations"][mode] = parse(receipt_path.read_bytes())
                            progress("necessary_original_"+mode+"_carrier_reconstruction", {})
                            last = time.monotonic()
                        time.sleep(2)
                finally:
                    if child.poll() is None:
                        child.terminate()
                        try:
                            child.wait(timeout=20)
                        except subprocess.TimeoutExpired:
                            child.kill()
                            child.wait()
            receipt = parse(receipt_path.read_bytes())
            document["carrier_restorations"][mode] = receipt
            require(child.returncode == 0 and receipt["complete"] is True and receipt["failure"] is None,
                    "the complete original "+mode+" carrier succeeded under its original SHA")
        import numpy as np
        import flint
        flint.ctx.prec, flint.ctx.cap = 320, 9
        api = ot_owner.directed_api(flint)
        api.midpoint_real = lambda value: value.mid()
        api.midpoint_complex = lambda value: api.acb(value.real.mid(), value.imag.mid())
        grid_raw = (private/"original-AS/complete-original-AS-grid.json").read_bytes()
        exact_rows, receipt = bnc["row_restore"].restore(np, api, bnc["DW_context"], dw, grid_raw,
            private/"same-complete-B-rows", progress)
        document["row_restoration"] = receipt
        del exact_rows
        wbody = parse((private/"same-complete-B-rows/input_original_DWTB_w.json").read_bytes())
        w_pairs = wbody["all_positive_exact_pairs"]
        f_coefficients, receipt = carriers.original_physical_coefficients(np, flint, api, bnc, private, progress, atomic)
        document["NP_restoration"] = receipt
        def whole_file(name, body):
            raw = canonical(body)
            path = private/name
            atomic(path, raw)
            require(path.read_bytes() == raw, "the entire new carrier is read before use: "+name)
            document["new_carrier_receipts"][name] = {"bytes": len(raw), "sha256": sha(raw)}
            return parse(path.read_bytes())

        physical_body = whole_file("complete-physical-source-coefficients.json", {
            "kind": "BFP_complete_original_physical_nu_source_v1", "positive_modes": 96,
            "exact_mean": "0", "all_positive_balls": [value.str(110) for value in f_coefficients],
            "negative_modes_are_real_conjugates": True})
        formal_f = [api.arb(text) for text in physical_body["all_positive_balls"]]
        require(all(new.contains(old) for new, old in zip(formal_f, f_coefficients)),
                "every full physical source coefficient is saved/read before any new norm")
        f_coefficients = formal_f
        points, point_identity = carriers.complete_physical_points(api, bnc, f_coefficients, grid_raw, progress)
        point_body = whole_file("complete-pullback-input-points.json", {"kind": "BFP_complete_f_G_Gprime_grid_v1",
            "complete_nodes": 8192, "original_grid_sha256": sha(grid_raw), **point_identity,
            "all_triples": [[f.str(110), g.str(110), gp.str(110)] for f, g, gp in points]})
        formal_points = [tuple(api.arb(text) for text in triple) for triple in point_body["all_triples"]]
        require(all(all(formal.contains(value) for formal, value in zip(saved, original))
                    for saved, original in zip(formal_points, points)), "all full point values survive serialization")
        points = formal_points
        trial, selection = carriers.choose_forward_trial(np, w_pairs, points)
        document["trial_proposal"] = selection
        trial_body = whole_file("complete-forward-trial.json", {"kind": "BFP_complete_forward_dyadic_trial_v1",
            "positive_modes": 512, "exact_mean": "0", "all_positive_exact_pairs": trial,
            "negative_modes_are_exact_conjugates": True, "proposal": selection})
        trial = trial_body["all_positive_exact_pairs"]
        image = pure.complete_exact_forward_image(w_pairs, trial)
        image_body = whole_file("complete-forward-image.json", {"kind": "BFP_complete_finite_forward_image_v1",
            "positive_modes": 2560, "all_positive_exact_pairs": image, "forward_B_sign": "+",
            "both_same_sign_blocks_retained": True})
        image = image_body["all_positive_exact_pairs"]

        def upper(record):
            return ot_owner.whole_upper(api, record)

        def ball(record):
            return ot_owner.whole_ball(api, record)

        def emit(name, value):
            require(name == pure.TARGETS[document["saved_record_count"]] and value.is_finite() and value.lower() >= 0,
                    "one whole new BFP bound in the declared order")
            point = value.upper()
            record = {"ball": point.str(60), "bound": "upper"}
            require(api.arb(record["ball"]).contains(point), "complete directed scalar round trip")
            document["current_target"] = name
            document["new_records"][name] = record
            document["completed_targets"].append(name)
            document["saved_record_count"] += 1
            document["current_target"] = None
            save()
            return upper(parse(args.output.read_bytes())["new_records"][name])

        targets, saved = pure.TARGETS, {}
        saved[0] = emit(targets[0], pure.complete_new_w_Wiener(api, w_pairs))
        saved[1] = emit(targets[1], pure.complete_true_B_inverse_L2(saved[0], upper(copied["w_Linf"])))
        norms = pure.complete_new_trial_norms(api, trial)
        for n in (2, 3, 4):
            saved[n] = emit(targets[n], norms[targets[n]])
        polynomial = pure.CompletePullbackPolynomial(api, points)
        for n, coefficient in enumerate(image, 1):
            polynomial.append(n, coefficient)
            if n % 64 == 0:
                progress("new_full_forward_pullback_polynomial", {"complete_modes": n, "total_modes": 2560})
        integrands = polynomial.whole_point_integrands()
        formal_body = whole_file("complete-pullback-integrands.json", {"kind": "BFP_complete_pullback_square_integrands_v1",
            "complete_nodes": 8192, "all_balls": [value.str(110) for value in integrands]})
        formal_integrands = [api.arb(text) for text in formal_body["all_balls"]]
        require(all(new.contains(old) for new, old in zip(formal_integrands, integrands)), "every full nonnegative-real square is enclosed")
        saved[5] = emit(targets[5], pure.complete_pullback_square_upper(api, formal_integrands))
        aliases = pure.complete_analytic_alias_square(api, image, f_coefficients, upper(copied["G0"]), upper(copied["G1"]))
        whole_file("complete-alias-components.json", {name: value.str(110) for name, value in aliases.items()})
        saved[6] = emit(targets[6], aliases[targets[6]])
        saved[7] = emit(targets[7], pure.complete_finite_forward_residual(saved[5], saved[6]))
        products = pure.complete_whole_w_products(api, upper(copied["w_Linf"]), upper(copied["w_L2"]), saved[3], saved[4])
        for n in (8, 9):
            saved[n] = emit(targets[n], products[targets[n]])
        chosen_name, chosen = pure.choose_whole_w_product(saved[8], saved[9])
        document["whole_w_product_choice"] = {"selected": chosen_name,
            "both_complete_candidates": {targets[n]: document["new_records"][targets[n]] for n in (8, 9)}}
        saved[10] = emit(targets[10], pure.complete_whole_flow_density_error(api, upper(copied["EH"]), upper(copied["N0"]),
            upper(copied["G1"]), upper(copied["H1"]), ball(copied["m"])))
        saved[11] = emit(targets[11], pure.complete_true_PDE_density_error(api, upper(copied["BH"]), upper(copied["Db"])))
        saved[12] = emit(targets[12], pure.complete_true_forward_residual(saved[7], chosen, saved[10], saved[11]))
        saved[13] = emit(targets[13], pure.complete_true_target_column_error(saved[1], saved[12]))
        progress("whole_true_B_forward_column_complete", {"complete_targets": 14})

        alpha_receipt = carriers.restore_original_alpha_from_saved_grid(api, old, ot_owner, grid_raw,
            private/"original-AS", progress)
        document["carrier_restorations"]["ALPHA"] = alpha_receipt
        unused_formal, theta, receipt = uc["restore"].restore(api, old, ot_owner, uc["old_contents"]["science"],
            ot_actual, private, progress)
        document["original_Theta_restoration"] = receipt
        true_a = api.arb(dw["complete_true_phase_a_ball"])
        coordinates = pure.complete_projected_target_coordinates(api, trial, true_a)
        coordinates_body = whole_file("complete-forward-target-coordinates.json", {"kind": "BFP_all_true_phase_target_coordinates_v1",
            "complete_modes": 512, "whole_true_a": true_a.str(110), "all_balls": [value.str(110) for value in coordinates]})
        formal_coordinates = [api.arb(text) for text in coordinates_body["all_balls"]]
        require(all(new.contains(old) for new, old in zip(formal_coordinates, coordinates)), "all true-phase coordinates are retained")
        model_raw = (private/"complete-original-model-multipliers.json").read_bytes()
        expected_model = ot_actual["private_model_multipliers_receipt"]
        require(len(model_raw) == expected_model["bytes"] and sha(model_raw) == expected_model["sha256"],
                "all2240 original signed model multipliers, not a new gap target")
        model = parse(model_raw)["all_modes"]
        require([value["mode"] for value in model] == list(range(1, 2241)), "every original model label")
        multipliers = [api.arb(value["signed_reciprocal"]) for value in model]
        saved[14] = emit(targets[14], pure.complete_finite_model_preimage(api, formal_coordinates, multipliers))
        saved[15] = emit(targets[15], pure.complete_original_Theta_trial_Frobenius(api, theta))
        pairings = pure.complete_true_phase_Theta_pairings(api, theta, formal_coordinates)
        pair_body = whole_file("complete-forward-Theta-pairings.json", {"kind": "BFP_all96_signed_Theta_trial_pairings_v1",
            "rows": 96, "all_balls": [value.str(110) for value in pairings]})
        formal_pairings = [api.arb(text) for text in pair_body["all_balls"]]
        require(all(new.contains(old) for new, old in zip(formal_pairings, pairings)), "every signed pairing is saved in full")
        centers, radius = pure.complete_pairing_centers_and_joint_radius(api, formal_pairings)
        saved[16] = emit(targets[16], radius)
        saved[17] = emit(targets[17], pure.complete_true_Theta_column_error(saved[15], upper(copied["global_Theta_error"]),
            saved[13], upper(copied["VQ_error"]), saved[14], upper(copied["model_rounding"]), saved[2], saved[16]))
        exact_centers = [str(carriers.midpoint_fraction(value)) for value in centers]
        signed_balls = [value+api.arb(0, saved[17]) for value in centers]
        signed_records = [value.str(60) for value in signed_balls]
        require(all(api.arb(text).contains(value) for text, value in zip(signed_records, signed_balls)),
                "each full true signed component is formally enclosed")
        signed = {"kind": "BFP_complete_true_Theta_strict_nu_column_v1", "rows": 96,
            "all96_exact_signed_centers": exact_centers, "all96_true_signed_balls": signed_records,
            "joint_l2_error_upper": document["new_records"][targets[17]],
            "whole_true_target_column_error_upper": document["new_records"][targets[13]],
            "prior_two_independent_density_means": copy.deepcopy(np_actual["new_records"][
                "complete_signed_strict_nu_waist_column"]["complete_signed_output_balls"]["independent_density_means"]),
            "true_infinite_source_or_output_high_modes_set_to_zero": False,
            "original_full_Theta_error_used": True, "low96_Theta_error_substituted": False,
            "physical_mean_phase_height_Schur_claimed": False}
        document["current_target"] = targets[18]
        document["new_records"][targets[18]] = signed
        document["completed_targets"].append(targets[18])
        document["saved_record_count"] = 19
        document["current_target"] = None
        save()
        require(parse(args.output.read_bytes())["new_records"][targets[18]] == signed, "the entire true signed96 column saved/read")
        document["result"] = {"whole_forward_B_column_error_proved": True, "whole_original_Theta_column_error_proved": True,
            "all512_trial_2560_image_8192_grid_and_96_pairings_retained": True,
            "all_original_global_errors_physical_means_and_phase_retained": True,
            "old_BNC_observation_or_other_completed_targets_recomputed": False,
            "full_homogeneous_inverse_or_physical_Schur_proved": False, "topic_completion_proved": False}
        document["complete"] = document["proved"] = True
        document["actual_returncode"] = 0
        progress("all_nineteen_complete_forward_targets_finished", {})
    except BaseException as exc:
        document["complete"] = document["proved"] = False
        document["failure"] = {"type": type(exc).__name__, "message": str(exc), "traceback": traceback.format_exc()}
        document["actual_returncode"] = 1
        save()
        raise


if __name__ == "__main__":
    main()
