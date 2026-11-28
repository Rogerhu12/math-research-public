"""First WMT14 actual whole weighted-model Theta error.

Only the same original IR grid/trial and entire2240 model carrier are
restored. The derivative residual uses a new8192 grid and2048 head. Old
IR99, UACT21, scalar gaps, AS/SN and BFP targets are never evaluated.
"""
from __future__ import annotations
import argparse
import copy
import gzip
import hashlib
import importlib.util
import json
import math
import os
import platform
import struct
import subprocess
import sys
import time
import traceback
from fractions import Fraction
from pathlib import Path

REPO = "Rogerhu12/math-research-public"
KIND = "R149_complete_weighted_model_Theta_receiver_v1"
STAGE = "weighted_model_Theta_receiver"
MANIFEST_KIND = "R149_complete_weighted_model_Theta_receiver_inputs_v1"
RUNTIME = {"python": "3.12.14", "packages": {"numpy": "2.3.5", "python-flint": "0.9.0"}}
PARAMETERS = {"arithmetic_bits": 320, "decimal_record_digits": 60, "private_ball_digits": 110,
    "maximum_scientific_wall_seconds": 19500, "original_IR_trial_shape": [192, 96, 2],
    "original_grid_reused_nodes": 4096, "new_interleaved_grid_nodes": 4096,
    "complete_new_grid_nodes": 8192, "complete_new_residual_positive_head": 2048,
    "complete_original_model_modes": 2240, "complete_new_model_head": 1048576,
    "complete_Gram_entries_each": 9216, "new_Gram_count": 4, "new_scientific_target_count": 14,
    "physical_frequency": 4, "physical_period": "pi/2", "density_strip": "1/256",
    "original_AS_strip": "1/128", "source_modes": 96, "original_alpha_modes": 2048,
    "original_low_reference": "1", "old_completed_scientific_target_calls": 0,
    "true_phase_means_and_original_infinite_Cayley_scope_retained": True,
    "UACT_low96_error_used_as_global_error": False}
SCI_FIELDS = sorted(["identity", "parameters", "complete", "proved", "actual_returncode", "failure",
    "stage", "progress", "wall_seconds", "runtime", "completed_targets", "current_target",
    "saved_record_count", "new_records", "copied_complete_input_records", "carrier_restoration",
    "new_carrier_receipts", "original_model_carrier_receipt", "complete_model_head_count",
    "whole_Theta_candidate_choice", "result", "old_scientific_target_calls",
    "new_arrays_published", "new_artifacts", "new_Releases"])


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def parse(raw):
    return json.loads(raw, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                       allow_nan=False)+"\n").encode()


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


def hash_file(path):
    digest, count = hashlib.sha256(), 0
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            digest.update(block)
            count += len(block)
    return {"bytes": count, "sha256": digest.hexdigest()}


def admit_complete_inputs(contents, specs, manifest, paths):
    return load(paths["admission"], "_WMT_whole_input_admission").admit(contents, specs, manifest, paths)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("manifest", "input-map", "output"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--manifest-sha", required=True)
    parser.add_argument("--checkout", required=True)
    parser.add_argument("--carrier-mode", choices=("IR",))
    parser.add_argument("--carrier-directory", type=Path)
    parser.add_argument("--carrier-receipt", type=Path)
    args = parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true" and os.environ.get("GITHUB_REPOSITORY") == REPO
            and os.environ.get("GITHUB_RUN_ATTEMPT") == "1", "one new public WMT14 target group")
    raw_manifest = args.manifest.read_bytes()
    require(sha(raw_manifest) == args.manifest_sha, "the entire new fixed WMT manifest")
    manifest = parse(raw_manifest)
    require(manifest["kind"] == MANIFEST_KIND and manifest["scientific_kind"] == KIND
            and manifest["parameters"] == PARAMETERS and manifest["allowed_scientific_fields"] == SCI_FIELDS,
            "the whole new WMT14 contract")
    specs = {item["role"]: item for item in manifest["files"]+manifest["historical_inputs"]}
    paths = {role: Path(value) for role, value in parse(args.input_map.read_bytes()).items()}
    require(sha(Path(__file__).read_bytes()) == specs["science"]["sha256"], "the actual pinned new owner")
    contents = {role: path.read_bytes() for role, path in paths.items()}
    admitted = admit_complete_inputs(contents, specs, manifest, paths)
    uc, uact, pure = admitted["UACT_context"], admitted["UACT_actual"], admitted["pure"]
    old, ot_owner, ot_actual = uc["admitted"], uc["owner"], uc["actual"]
    if args.carrier_mode is not None:
        ot_owner.carrier_child(args, old)
        return
    require(not args.output.exists(), "retain every previous target outcome")
    ir, alpha = old["IR"]["actual"], old["AS"]["actual"]
    copied = {"IR_H": ir["new_records"]["complete_joint_energy_residual_upper"],
        "IR_L2": ir["new_records"]["complete_joint_L2_residual_upper"],
        "IR_complete_image_width": ir["global_bounds"]["complete_image_width"],
        "IR_inverse_lift_error": ir["global_bounds"]["inverse_lift_error"],
        "alpha_trial_W": ot_actual["new_records"]["complete_alpha_trial_Wiener_upper"],
        "positive_GY_W": ot_actual["new_records"]["complete_positive_G_trial_vector_Wiener_upper"],
        "original_VQ_H1_error": uact["new_records"]["complete_unit_disk_original_VQ_joint_H1_error_upper"],
        "original_global_Theta_error": uact["new_records"]["complete_unit_disk_original_Theta_joint_L2_error_upper"],
        "model_rounding": ot_actual["new_records"]["complete_model_action_joint_rounding_error_upper"],
        "original_all_four_whole_UACT_products": {name: uact["new_records"][name] for name in (
            "complete_unit_disk_alpha_finite_Linf_product_upper", "complete_unit_disk_alpha_finite_L2_product_upper",
            "complete_unit_disk_alpha_inverse_error_Linf_product_upper", "complete_unit_disk_alpha_inverse_error_L2_product_upper")},
        "original_AS_global_bounds": alpha["global_bounds"], "original_model_input_records": ot_actual["actual_model_input_records"]}
    document = {"identity": {"kind": KIND, "scalar_stage": STAGE, "source_sha256": specs["science"]["sha256"],
        "manifest_sha256": args.manifest_sha, "run_id": os.environ["GITHUB_RUN_ID"], "run_attempt": "1",
        "event_commit": os.environ["GITHUB_SHA"], "actual_checkout_commit": args.checkout,
        "whole_UACT_actual_sha256": specs["UACT_actual"]["sha256"]},
        "parameters": PARAMETERS, "complete": False, "proved": False, "actual_returncode": None, "failure": None,
        "stage": "all_whole_original_inputs_admitted", "progress": {}, "wall_seconds": 0, "runtime": {},
        "completed_targets": [], "current_target": None, "saved_record_count": 0, "new_records": {},
        "copied_complete_input_records": copy.deepcopy(copied), "carrier_restoration": None,
        "new_carrier_receipts": {}, "original_model_carrier_receipt": None,
        "complete_model_head_count": 0, "whole_Theta_candidate_choice": None, "result": None,
        "old_scientific_target_calls": 0, "new_arrays_published": 0, "new_artifacts": 0, "new_Releases": 0}
    require(sorted(document) == SCI_FIELDS, "the entire WMT small-output schema")
    private = args.output.parent/"private-complete-WMT"
    private.mkdir()
    began = time.monotonic()

    def save():
        document["wall_seconds"] = time.monotonic()-began
        raw = canonical(document)
        require(len(raw) < manifest["operation"]["maximum_scientific_bytes"], "the whole small WMT output")
        atomic(args.output, raw)

    def progress(stage, data):
        document["stage"], document["progress"] = stage, data
        save()
        require(document["wall_seconds"] <= PARAMETERS["maximum_scientific_wall_seconds"], "preserve whole new prefix before timeout")
        print(json.dumps({"stage": stage, **data}, sort_keys=True), flush=True)

    save()
    try:
        from importlib.metadata import version
        runtime = {"python": platform.python_version(), "packages": {name: version(name) for name in RUNTIME["packages"]}}
        require(runtime == RUNTIME and os.environ.get("OPENBLAS_CORETYPE") == "Haswell", "the same original arithmetic and proposal runtime")
        document["runtime"] = runtime
        directory, receipt_path = private/"original-IR", private/"IR-restoration.json"
        command = [sys.executable, str(Path(__file__)), "--manifest", str(args.manifest), "--manifest-sha", args.manifest_sha,
            "--input-map", str(args.input_map), "--output", str(args.output), "--checkout", args.checkout,
            "--carrier-mode", "IR", "--carrier-directory", str(directory), "--carrier-receipt", str(receipt_path)]
        with (private/"IR-restoration.log").open("wb") as log:
            child = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT)
            try:
                last = 0.0
                while child.poll() is None:
                    if time.monotonic()-last >= 30:
                        if receipt_path.exists():
                            document["carrier_restoration"] = parse(receipt_path.read_bytes())
                        progress("necessary_original_IR_grid_and_trial_only", {})
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
        document["carrier_restoration"] = receipt
        require(child.returncode == 0 and receipt["complete"] is True and receipt["failure"] is None
                and receipt["result"]["whole_original_SHA_required"] is True,
                "all original IR carrier bytes restored successfully")
        import flint
        flint.ctx.prec, flint.ctx.cap = 320, 9
        api = ot_owner.directed_api(flint)
        # Numerical functions of every old completed target remain disabled.
        old["IR"]["owner"].main = ot_owner.forbidden
        for name in ("complete_global_bounds", "complete_kernels", "complete_column_bounds", "complete_residual_norms",
                     "complete_joint_residual", "complete_directed_dft", "fft_tables", "entire_signed_head",
                     "CompletePrimitiveSampleFactory"):
            setattr(old["IR_math"], name, ot_owner.forbidden)

        def upper(record):
            return ot_owner.whole_upper(api, record)

        def whole_file(name, body):
            raw = canonical(body)
            path = private/name
            atomic(path, raw)
            require(path.read_bytes() == raw, "the complete new private object saved/read: "+name)
            document["new_carrier_receipts"][name] = {"bytes": len(raw), "sha256": sha(raw)}
            return parse(path.read_bytes())

        def emit(index, value):
            require(index == document["saved_record_count"] and value.is_finite() and value.upper() >= 0,
                    "the next complete new WMT target")
            name, point = pure.TARGETS[index], value.upper()
            record = {"ball": point.str(60), "bound": "upper"}
            require(api.arb(record["ball"]).contains(point), "the full directed new scalar round trip")
            document["current_target"] = name
            document["new_records"][name] = record
            document["completed_targets"].append(name)
            document["saved_record_count"] += 1
            document["current_target"] = None
            save()
            return upper(parse(args.output.read_bytes())["new_records"][name])

        def new_Gram_bound(name, columns, derivative, extent):
            gram = pure.whole_Gram(api, columns, derivative, extent)
            body = whole_file(name, {"kind": "WMT_complete_signed_Gram_v1", "shape": [96, 96],
                "positive_modes": extent, "physical_derivative_order": derivative,
                "both_frequency_signs_retained": True,
                "all_balls": [[value.str(110) for value in row] for row in gram]})
            formal = [[api.arb(text) for text in row] for row in body["all_balls"]]
            require(all(formal[j][k].contains(gram[j][k]) for j in range(96) for k in range(96)),
                    "every full signed Gram entry survives serialization")
            return pure.saved_Gram_operator_upper(api, formal)

        trial_raw = (directory/"complete-original-IR-trial.f64").read_bytes()
        expected = ir["private_trial_receipt"]
        require(len(trial_raw) == expected["bytes"] and sha(trial_raw) == expected["sha256"], "the full original IR trial")
        numbers = struct.unpack("<"+str(192*96*2)+"d", trial_raw)
        require(all(math.isfinite(value) for value in numbers), "all original dyadic coefficients")
        columns = [[api.acb(api.rational(Fraction(numbers[2*(n*96+j)])),
                          api.rational(Fraction(numbers[2*(n*96+j)+1]))) for n in range(192)] for j in range(96)]
        saved = {}
        for derivative in range(3):
            saved[derivative] = emit(derivative, new_Gram_bound("complete-Y-D%d-Gram.json" % derivative,
                                                               columns, derivative, 192))
        saved[3] = emit(3, pure.complete_primitive_vector_strip(api, columns, upper(copied["IR_complete_image_width"])))
        grid_raw = (directory/"complete-original-IR-grid.json").read_bytes()
        expected = ir["private_grid_receipt"]
        require(len(grid_raw) == expected["bytes"] and sha(grid_raw) == expected["sha256"], "all4096 original complete grid records")
        old_grid = [api.arb(text) for text in parse(grid_raw)["all_balls"]]
        grid = pure.complete_new_grid(api, old_grid, old["states"][1], old["prior"]["K_sines"], old["prior"]["K_cosines"])
        body = whole_file("complete-new-8192-grid.json", {"kind": "WMT_complete_8192_inverse_lift_grid_v1",
            "original4096_sha256": sha(grid_raw), "all_balls": [value.str(110) for value in grid]})
        formal_grid = [api.arb(text) for text in body["all_balls"]]
        require(len(formal_grid) == 8192 and all(a.contains(b) for a, b in zip(formal_grid, grid)), "all8192 full grid values")
        samples, tables = pure.new_primitive_samples(api, formal_grid, columns), pure.new_fft_tables(api)
        heads = []
        samples_chain = heads_chain = None
        for j in range(1, 97):
            values = [samples[k, j-1] for k in range(8192)]
            body = {"kind": "WMT_complete_8192_primitive_samples_v1", "row": j,
                    "all_balls": [[v.real.str(110), v.imag.str(110)] for v in values]}
            raw = canonical(body)
            sample_path = private/("complete-new-samples-%03d.json" % j)
            atomic(sample_path, raw)
            formal = [api.acb(api.arb(a), api.arb(b)) for a, b in parse(sample_path.read_bytes())["all_balls"]]
            require(all(a.real.contains(b.real) and a.imag.contains(b.imag) for a, b in zip(formal, values)), "each new whole sample record")
            samples_chain = sha(canonical({"previous": samples_chain, "row": j, "bytes": len(raw), "sha256": sha(raw)}))
            transformed = pure.whole_new_transform(api, formal, tables)
            row = pure.whole_new_head(api, j, transformed, saved[3])
            body = {"kind": "WMT_complete_2048_signed_residual_head_v1", "row": j,
                    "all_balls": [[v.real.str(110), v.imag.str(110)] for v in row]}
            raw = canonical(body)
            head_path = private/("complete-new-head-%03d.json" % j)
            atomic(head_path, raw)
            formal = [api.acb(api.arb(a), api.arb(b)) for a, b in parse(head_path.read_bytes())["all_balls"]]
            require(all(a.real.contains(b.real) and a.imag.contains(b.imag) for a, b in zip(formal, row)), "each new whole signed residual head")
            heads_chain = sha(canonical({"previous": heads_chain, "row": j, "bytes": len(raw), "sha256": sha(raw)}))
            heads.append(formal)
            progress("new_complete_8192_grid_derivative_residual_rows", {"rows_complete": j, "positive_modes_each": 2048})
        document["new_carrier_receipts"]["complete_all96_samples_and_heads"] = {
            "samples_chain_sha256": samples_chain, "heads_chain_sha256": heads_chain,
            "complete_rows": 96, "all8192_samples_and2048_signed_modes_each_retained": True}
        del samples
        saved[4] = emit(4, new_Gram_bound("complete-new-D1-residual-head-Gram.json", heads, 1, 2048))
        saved[5] = emit(5, pure.complete_D1_residual_tail(api, saved[3]))
        saved[6] = emit(6, pure.complete_D1_true_map_error(api, upper(copied["IR_inverse_lift_error"]), saved[0], saved[1], saved[2]))
        saved[7] = emit(7, pure.complete_D1_residual(saved[4], saved[5], saved[6]))
        H = upper(copied["IR_H"])
        S = pure.original_inverse_L2_error(api, H, upper(copied["IR_L2"]))
        saved[8] = emit(8, pure.complete_inverse_D1_error(api, saved[7], S))
        globals = copied["original_AS_global_bounds"]
        saved[9] = emit(9, pure.complete_alpha_D1_tail(api, upper(globals["new_raw_trial_Astrip_upper"]),
            upper(globals["complete_source_error_derivative_columns"][3]), ot_owner.whole_ball(api, globals["complete_original_map_imaginary_lower"])))
        products = copied["original_all_four_whole_UACT_products"]
        saved[10] = emit(10, pure.complete_VQ_D2_error(api, saved_inverse_D1=saved[8], original_H=H, original_S=S,
            original_alpha_trial_W=upper(copied["alpha_trial_W"]), original_positive_GY_W=upper(copied["positive_GY_W"]),
            whole_original_finite_L2_product=upper(products["complete_unit_disk_alpha_finite_L2_product_upper"]),
            whole_original_inverse_L2_product=upper(products["complete_unit_disk_alpha_inverse_error_L2_product_upper"]),
            saved_alpha_D1_tail=saved[9]))

        # Restore only the complete original scalar model carrier. No old row
        # multiplication, original gap target or previous norm is evaluated.
        omega = api.arb(globals["complete_exact_rotation_ball"])
        source_b = api.arb(globals["complete_original_source_phase_ball"])
        mu = ot_owner.whole_ball(api, alpha["copied_original_records"]["complete_signed_mu"])
        native = old["CYA"]["complete_original_scalar_input_conclusion"]["original_gap_coefficient_record_read_verbatim"]
        require(ot_owner.whole_ball(api, native).contains(-mu/4), "the entire actual mean lies in the original infinite Cayley scope")
        model = []
        for n in range(1, 2241):
            phase = 2*n*source_b+api.arb.pi()/4
            if n <= 96:
                denominator, reciprocal, kind = api.one, api.one, "original_Llow_reference"
            else:
                theta = 2*n*omega+api.arb.pi()/4
                denominator = theta.cos()-(-mu/2)*theta.sin()/(4*n)
                require(not denominator.contains(0), "original qualified signed model denominator")
                reciprocal, kind = 1/denominator, "original_Mnu_high_reciprocal"
            model.append({"mode": n, "kind": kind, "signed_denominator": denominator.str(90),
                          "signed_reciprocal": reciprocal.str(90), "true_source_phase": phase.str(90)})
        model_raw = canonical({"kind": "OT_complete_original_model_multipliers_v1", "complete_modes": 2240, "all_modes": model})
        ot_owner.verify_private(private/"complete-original-model-multipliers.json", model_raw,
                                ot_actual["private_model_multipliers_receipt"])
        document["original_model_carrier_receipt"] = copy.deepcopy(ot_actual["private_model_multipliers_receipt"])
        complete_model = parse((private/"complete-original-model-multipliers.json").read_bytes())["all_modes"]
        original_head = max((abs(api.arb(item["signed_reciprocal"])).upper()/(4*item["mode"])).upper()
                            for item in complete_model)
        model_path = private/"complete-new-model-weighted-head.jsonl.gz"
        with model_path.open("wb") as raw_stream:
            with gzip.GzipFile(filename="", mode="wb", fileobj=raw_stream, compresslevel=1, mtime=0) as stream:
                for n in range(2241, pure.MODEL_HEAD+1):
                    denominator, reciprocal, weighted = pure.new_model_record(api, n, omega, mu)
                    record = {"mode": n, "signed_denominator": denominator.str(60),
                        "signed_reciprocal": reciprocal.str(60), "complete_D1_weight_upper": weighted.str(60)}
                    require(api.arb(record["signed_denominator"]).contains(denominator)
                            and api.arb(record["signed_reciprocal"]).contains(reciprocal)
                            and api.arb(record["complete_D1_weight_upper"]).contains(weighted), "all whole new signed model records")
                    stream.write(canonical(record))
                    if n % 8192 == 0:
                        document["complete_model_head_count"] = n
                        progress("new_complete_model_head_after_all2240_original_modes", {"complete_modes": n, "total_modes": pure.MODEL_HEAD})
        before = hash_file(model_path)
        maximum, count = original_head, 2240
        with gzip.open(model_path, "rb") as stream:
            for line in stream:
                record = parse(line)
                count += 1
                require(record["mode"] == count, "every new whole model label in natural order")
                value = api.arb(record["complete_D1_weight_upper"])
                require(value.is_finite() and value.lower() > 0, "one complete saved positive model weight")
                maximum = max(maximum, value.upper())
        require(count == pure.MODEL_HEAD and hash_file(model_path) == before, "the entire first model head saved/read before reduction")
        document["complete_model_head_count"] = count
        document["new_carrier_receipts"][model_path.name] = {**before, "first_new_mode": 2241,
            "last_new_mode": pure.MODEL_HEAD, "new_complete_records": pure.MODEL_HEAD-2240,
            "all_original2240_modes_also_in_whole_maximum": True}
        saved[11] = emit(11, maximum)
        saved[12] = emit(12, pure.complete_model_infinite_D2_weight(api))
        saved[13] = emit(13, pure.complete_weighted_Theta_error(api, saved[11], upper(copied["original_VQ_H1_error"]),
            saved[12], saved[10], upper(copied["model_rounding"])))
        candidates = {"whole_original_UACT_global_error": copied["original_global_Theta_error"],
                      "whole_new_WMT_global_error": document["new_records"][pure.TARGETS[13]]}
        chosen = min(candidates, key=lambda name: upper(candidates[name]))
        document["whole_Theta_candidate_choice"] = {"selected": chosen, "both_complete_candidates": candidates,
            "low96_error_is_not_a_global_candidate": True, "same_original_Theta_and_trial": True}
        document["result"] = {"whole_original_Theta_global_error_proved": True,
            "complete_true_IR_D1_residual_proved": True, "complete_original_density_inverse_H1_bootstrap_used": True,
            "all_model_head_and_infinite_tail_terms_paid": True, "old_target_calls": 0,
            "BFP_actual_consumed_or_Theta_nu_column_claimed": False,
            "full_physical_Schur_proved": False, "topic_completion_proved": False}
        document["complete"] = document["proved"] = True
        document["actual_returncode"] = 0
        progress("all_fourteen_complete_weighted_model_targets_finished", {})
    except BaseException as error:
        document["complete"] = document["proved"] = False
        document["actual_returncode"] = 1
        document["failure"] = {"type": type(error).__name__, "message": str(error), "traceback": traceback.format_exc()}
        save()
        raise


if __name__ == "__main__":
    main()
