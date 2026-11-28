"""First BGR3 whole signed Gram, new coefficient product and full row error.

Only original carriers are reconstructed. All DWTB9 scalar/error/residual
targets are completed inputs. BNC observations and BFP targets do not run.
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
SOURCE = TOPIC+"scripts/fourfold_codazzi_target_B_Gram_owner.py"
KIND = "R149_complete_target_B_Gram_v1"
STAGE = "target_B_Gram"
MANIFEST_KIND = "R149_complete_target_B_Gram_inputs_v1"
TARGETS = ["complete_DWTB_trial_primitive_Gram_operator_upper",
           "complete_DWTB_target_w_Linf_operator_product_upper",
           "complete_DWTB_inverse96_Gram_row_error_upper"]
PARAMETERS = {"arithmetic_bits": 320, "decimal_record_digits": 60,
              "private_ball_digits": 110, "rows": 96, "positive_modes": 192,
              "whole_signed_Gram_entries": 9216, "maximum_scientific_wall_seconds": 16800,
              "old_completed_target_calls": 0, "new_complete_targets": 3,
              "physical_frequency": 4, "physical_period": "pi/2",
              "normalized_L2_measure": True, "both_mean_slots_eliminated": False,
              "original_DWTB_run": "45935081577/1"}
RUNTIME = {"python": "3.12.14", "packages": {"numpy": "2.3.5", "python-flint": "0.9.0"}}
SCI_FIELDS = sorted(["identity", "parameters", "complete", "proved", "actual_returncode", "failure",
    "stage", "progress", "wall_seconds", "runtime", "completed_targets", "current_target",
    "new_records", "saved_record_count", "whole_completed_input_manifest_sha256",
    "copied_complete_DWTB_records", "carrier_restoration", "row_restoration",
    "complete_Gram_receipt", "complete_product_choice", "complete_operator_choice",
    "complete_row_error_choice", "result", "old_scientific_target_calls",
    "new_arrays_published", "new_artifacts", "new_Releases"])


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
    require(set(contents) == set(specs) == set(snapshot_paths), "every complete BGR input")
    for role, raw in contents.items():
        item = specs[role]
        require(len(raw) == item["bytes"] and sha(raw) == item["sha256"], "entire BGR input: "+role)
    original = parse(contents["BNC_manifest"])
    require(sha(contents["BNC_manifest"]) == "a6655051c571970a407fad139fa9485251f4091835db7b6e5e2468ea181ef42b",
            "the entire original necessary-carrier closure")
    by_path = {item["path"]: role for role, item in specs.items()}
    old_specs, old_contents, old_paths = {}, {}, {}
    for expected in original["files"]+original["historical_inputs"]:
        role, here = expected["role"], by_path[expected["path"]]
        require(dict(specs[here], role=role) == expected, "unchanged whole original carrier descriptor")
        old_specs[role], old_contents[role], old_paths[role] = expected, contents[here], snapshot_paths[here]
    original_owner = load(old_paths["science"], "_BGR_original_complete_carrier_owner")
    context = original_owner.admit_complete_inputs(old_contents, old_specs, original, old_paths)
    pure = load(snapshot_paths["Gram_math"], "_BGR_new_signed_Gram_formulas")
    require(pure.TARGETS == TARGETS == manifest["target_order"] and pure.ROWS == 96 and pure.MODES == 192,
            "only the three previously uncomputed complete BGR targets")
    require(sha(contents["Gram_math"]) == "32ab1b1ddb5f09ca42dca4e17cc9458ed6df9fe35c1e2ca343d698ebfa59b8a0"
            and sha(contents["Gram_proof"]) == "70023df23aa4375e67ced3070b04e6d6543b45f4e71ca3ebfe71458cd7f77daa",
            "the entire original BGR theorem and pure formulas")
    require(not any(name in sys.modules for name in ("numpy", "flint", "scipy")),
            "all complete old results admitted before numerical imports")
    return {"original_owner": original_owner, "original": context, "math": pure}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("manifest", "input-map", "output"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--manifest-sha", required=True)
    parser.add_argument("--checkout", required=True)
    parser.add_argument("--carrier-only", action="store_true")
    parser.add_argument("--carrier-directory", type=Path)
    parser.add_argument("--carrier-receipt", type=Path)
    args = parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true" and os.environ.get("GITHUB_REPOSITORY") == REPO
            and os.environ.get("GITHUB_RUN_ATTEMPT") == "1", "one first public BGR3 execution")
    raw = args.manifest.read_bytes()
    require(sha(raw) == args.manifest_sha, "the whole BGR3 manifest")
    manifest = parse(raw)
    require(manifest["kind"] == MANIFEST_KIND and manifest["scientific_kind"] == KIND
            and manifest["parameters"] == PARAMETERS and manifest["allowed_scientific_fields"] == SCI_FIELDS,
            "the complete declared BGR3 contract")
    specs = {item["role"]: item for item in manifest["files"]+manifest["historical_inputs"]}
    paths = {role: Path(path) for role, path in parse(args.input_map.read_bytes()).items()}
    require(sha(Path(__file__).read_bytes()) == specs["science"]["sha256"], "the actual immutable owner")
    contents = {role: path.read_bytes() for role, path in paths.items()}
    admitted = admit_complete_inputs(contents, specs, manifest, paths)
    context, pure = admitted["original"], admitted["math"]
    if args.carrier_only:
        admitted["original_owner"].carrier_child(args, context)
        return
    require(not args.output.exists(), "retain every previous complete or failed outcome")
    dw = context["parents"]["DW"]["actual"]
    document = {"identity": {"kind": KIND, "scalar_stage": STAGE, "source_sha256": specs["science"]["sha256"],
        "manifest_sha256": args.manifest_sha, "run_id": os.environ["GITHUB_RUN_ID"], "run_attempt": "1",
        "event_commit": os.environ["GITHUB_SHA"], "actual_checkout_commit": args.checkout},
        "parameters": PARAMETERS, "complete": False, "proved": False, "actual_returncode": None,
        "failure": None, "stage": "whole_original_DWTB9_admitted", "progress": {}, "wall_seconds": 0,
        "runtime": {}, "completed_targets": [], "current_target": None, "new_records": {}, "saved_record_count": 0,
        "whole_completed_input_manifest_sha256": specs["BNC_manifest"]["sha256"],
        "copied_complete_DWTB_records": copy.deepcopy(dw["new_records"]), "carrier_restoration": None,
        "row_restoration": None, "complete_Gram_receipt": None, "complete_product_choice": None,
        "complete_operator_choice": None, "complete_row_error_choice": None, "result": None,
        "old_scientific_target_calls": 0, "new_arrays_published": 0, "new_artifacts": 0, "new_Releases": 0}
    require(sorted(document) == SCI_FIELDS, "the entire small BGR3 output schema")
    began = time.monotonic()
    private = args.output.parent/"private-complete-BGR"
    private.mkdir()

    def save():
        document["wall_seconds"] = time.monotonic()-began
        raw = canonical(document)
        require(len(raw) < manifest["operation"]["maximum_scientific_bytes"], "whole BGR3 small result")
        atomic(args.output, raw)

    def progress(stage, details):
        document["stage"], document["progress"] = stage, details
        save()
        require(document["wall_seconds"] < PARAMETERS["maximum_scientific_wall_seconds"], "preserve complete BGR prefix")
        print(json.dumps({"stage": stage, **details}, sort_keys=True), flush=True)

    save()
    try:
        from importlib.metadata import version
        runtime = {"python": platform.python_version(), "packages": {name: version(name) for name in RUNTIME["packages"]}}
        require(runtime == RUNTIME and os.environ.get("OPENBLAS_CORETYPE") == "Haswell", "same original deterministic runtime")
        document["runtime"] = runtime
        grid_dir, grid_receipt = private/"whole-original-grid", private/"whole-original-grid-progress.json"
        command = [sys.executable, str(Path(__file__)), "--manifest", str(args.manifest), "--manifest-sha", args.manifest_sha,
            "--input-map", str(args.input_map), "--output", str(args.output), "--checkout", args.checkout,
            "--carrier-only", "--carrier-directory", str(grid_dir), "--carrier-receipt", str(grid_receipt)]
        environment = dict(os.environ)
        environment.pop("OPENBLAS_CORETYPE", None)
        with (private/"original-grid-child.log").open("wb") as log:
            child = subprocess.Popen(command, env=environment, stdout=log, stderr=subprocess.STDOUT)
            try:
                last = 0.0
                while child.poll() is None:
                    if time.monotonic()-last >= 45:
                        if grid_receipt.exists():
                            document["carrier_restoration"] = parse(grid_receipt.read_bytes())
                        progress("necessary_original_grid_reconstruction", {})
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
        document["carrier_restoration"] = parse(grid_receipt.read_bytes())
        restored = document["carrier_restoration"]
        require(child.returncode == 0 and restored["complete"] is True and restored["failure"] is None
                and restored["result"]["grid"] == context["DW_context"]["AS"]["actual"]["private_grid_receipt"],
                "the same original complete grid, never a new point set")
        grid_raw = (grid_dir/"complete-original-AS-grid.json").read_bytes()
        import numpy as np
        import flint
        flint.ctx.prec, flint.ctx.cap = 320, 9
        api = context["DW_context"]["carrier"].directed_api(flint)
        api.midpoint_real = lambda value: value.mid()
        api.midpoint_complex = lambda value: api.acb(value.real.mid(), value.imag.mid())
        exact_rows, receipt = context["row_restore"].restore(np, api, context["DW_context"], dw,
            grid_raw, private/"same-complete-B-rows", progress)
        document["row_restoration"] = receipt
        progress("forming_all_9216_new_signed_Gram_entries", {})
        whole = pure.complete_signed_Gram(api, exact_rows)
        body = {"kind": "BGR_whole_original_row_trial_signed_Gram_v1", "shape": [96, 96],
                "original_exact_rows_sha256": dw["private_row_trial_receipt"]["sha256"],
                "all_entries": [[value.str(110) for value in row] for row in whole]}
        gram_raw = canonical(body)
        gram_path = private/"complete-signed-Gram.json"
        atomic(gram_path, gram_raw)
        require(gram_path.read_bytes() == gram_raw, "the whole signed Gram saved before its first norm")
        formal = [[api.arb(text) for text in row] for row in parse(gram_path.read_bytes())["all_entries"]]
        require(all(formal[j][k].contains(whole[j][k]) for j in range(96) for k in range(96)),
                "every full saved signed entry contains its original directed value")
        document["complete_Gram_receipt"] = {"shape": [96, 96], "bytes": len(gram_raw), "sha256": sha(gram_raw),
            "all_signed_entries_saved_before_norm": True, "all_original_rows_and_both_frequency_signs": True}

        def old(name):
            return context["DW_context"]["carrier"].whole_upper(api, dw["new_records"][name])

        def emit(name, value):
            require(name == TARGETS[document["saved_record_count"]] and value.is_finite() and value.lower() >= 0,
                    "one new whole bound in the declared order")
            document["current_target"] = name
            point = value.upper()
            record = {"ball": point.str(60), "bound": "upper"}
            require(api.arb(record["ball"]).contains(point), "the entire directed bound survives its complete record")
            document["new_records"][name] = record
            document["completed_targets"].append(name)
            document["saved_record_count"] += 1
            document["current_target"] = None
            save()
            formal_record = parse(args.output.read_bytes())["new_records"][name]
            return context["DW_context"]["carrier"].whole_upper(api, formal_record)

        g = emit(TARGETS[0], pure.complete_Gram_operator_upper(api, formal))
        product = emit(TARGETS[1], pure.complete_new_infinity_product(
            old("complete_direct_unit_disk_target_w_Linf_error_upper"), g))
        choice, chosen = pure.choose_complete_product(product, old("complete_target_w_Linf_product_upper"),
                                                       old("complete_target_w_L2_product_upper"))
        document["complete_product_choice"] = {"selected": choice, "new_product": document["new_records"][TARGETS[1]],
            "original_Linf_product": dw["new_records"]["complete_target_w_Linf_product_upper"],
            "original_L2_product": dw["new_records"]["complete_target_w_L2_product_upper"]}
        error = emit(TARGETS[2], pure.complete_new_row_error(
            old("complete_finite_target_B_adjoint_energy_residual_upper"), chosen))
        choice, unused = pure.choose_complete_primitive_operator_upper(g, old("complete_I_trial_Hilbert_Schmidt_upper"))
        document["complete_operator_choice"] = {"selected": choice, "new_Gram_operator": document["new_records"][TARGETS[0]],
            "original_Hilbert_Schmidt": dw["new_records"]["complete_I_trial_Hilbert_Schmidt_upper"]}
        choice, unused = pure.choose_complete_row_error(error, old("complete_target_B_inverse96_joint_L2_row_error_upper"))
        document["complete_row_error_choice"] = {"selected": choice, "new_Gram_row_error": document["new_records"][TARGETS[2]],
            "original_complete_row_error": dw["new_records"]["complete_target_B_inverse96_joint_L2_row_error_upper"]}
        document["result"] = {"complete_whole_same_operator_row_bound_proved": True,
            "original_DWTB9_preserved_without_recomputation": True,
            "BNC_quadratures_or_BFP_forward_targets_executed": False,
            "physical_mean_phase_and_high_frequency_obligations_retained": True,
            "full_Schur_or_final_closed_family_proved": False}
        document["complete"] = document["proved"] = True
        document["actual_returncode"] = 0
        progress("all_three_new_whole_B_Gram_targets_complete", {})
    except BaseException as exc:
        document["failure"] = {"type": type(exc).__name__, "message": str(exc), "traceback": traceback.format_exc()}
        document["actual_returncode"] = 1
        save()
        raise


if __name__ == "__main__":
    main()
