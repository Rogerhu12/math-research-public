"""BW first signed target w=vi-alpha and four complete trial-error balls.

The complete successful ASR actual is the sole parent. Its old signed
carriers are restored once with all original SHA identities; the same
quadrature calls are observed without changing their return values.
Only the new vi/w errors are evaluated. Local admission is metadata only.
"""
from __future__ import annotations
import argparse
import ast
import copy
import hashlib
import json
import os
import platform
import time
import traceback
import types
from fractions import Fraction
from pathlib import Path

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby/"
KIND = "R149_complete_target_w_signed_carrier_v1"
STAGE = "target_w_signed_carrier"
MANIFEST_KIND = "R149_complete_target_w_signed_carrier_inputs_v1"
SOURCE_PATH = TOPIC+"scripts/fourfold_codazzi_target_w_signed_carrier_owner.py"
WORKER_PATH = TOPIC+"scripts/fourfold_codazzi_target_w_signed_carrier_public_worker.py"
GENERATOR_PATH = TOPIC+"scripts/make_target_w_signed_carrier_manifest.py"
TARGETS = ["complete_incoming_vi_trial_Linf_error_upper", "complete_incoming_vi_trial_L2_error_upper",
           "complete_target_w_trial_Linf_error_upper", "complete_target_w_trial_L2_error_upper"]
PARAMETERS = {
    "arithmetic_bits": 320, "power_series_cap": 9, "decimal_record_digits": 60,
    "private_ball_digits": 90, "positive_modes": 2048, "grid_points": 8192,
    "complete_raw_source_positive_modes": 192, "physical_strip": "1/128",
    "physical_frequency_factor": 4, "physical_period": "pi/2",
    "target_coefficient": "w=vi-alpha", "target_normalizer": "B=Id+T_w I",
    "target_reflection_phase": "a=2*true_H(0)", "source_reflection_phase": "b=a+Omega",
    "first_coefficient_mean": "-mu/2", "both_physical_mean_slots_retained": True,
    "new_vi_and_w_means": "exact zero", "whole_original_ASR_SHA_required": True,
    "original_carrier_CORETYPE": "unset", "all_carrier_threads": 1,
    "one_original_quadrature_pass_observed_without_changing_returns": True,
    "maximum_scientific_wall_seconds": 16800, "old_completed_scientific_targets_allowed": 0,
}
SCI_FIELDS = sorted([
    "identity", "complete", "proved", "actual_returncode", "failure", "stage",
    "completed_targets", "current_target", "candidate_record", "new_records", "saved_record_count",
    "parameters", "result", "whole_completed_inputs", "copied_complete_parent_records",
    "runtime", "wall_seconds", "progress", "old_scientific_target_calls",
    "necessary_carrier_rematerializations", "original_carrier_restoration",
    "private_quadrature_receipt", "private_vi_trial_receipt", "private_w_trial_receipt",
    "private_modes_receipt", "complete_mode_prefix", "complete_tail_bounds",
    "new_arrays_published", "new_artifacts", "new_Releases",
])
CARRIER_SHA = "acd0ebe5158bf143b7a85a14fdd3413fc2ff32aef13d90f8417ed7ef4e4254f4"
ADMISSION_SHA = "40c9893cf4a17399b0f913962eee68066b09e66f165a3d79e3654d6aa9d3e9fc"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def blob(raw):
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


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
    require(set(contents) == set(specs) and set(manifest["parent_roles"]) == {"AS"}
            and manifest["historical_inputs"] == [], "whole inherited ASR closure without a projected parent")
    for role, spec in specs.items():
        raw = contents[role]
        require(spec["role"] == role and type(raw) is bytes and 0 < len(raw) < 100000
                and len(raw) == spec["bytes"] and sha(raw) == spec["sha256"]
                and blob(raw) == spec["git_blob_sha"], "whole immutable BW input: "+role)
        raw.decode()
        if spec["path"].endswith(".py"):
            ast.parse(raw.decode(), filename=spec["path"])
    require(specs["science"]["path"] == SOURCE_PATH and specs["worker"]["path"] == WORKER_PATH
            and specs["generator"]["path"] == GENERATOR_PATH
            and sha(contents["carrier_original_owner"]) == CARRIER_SHA
            and sha(contents["parent_admission"]) == ADMISSION_SHA,
            "same original whole carrier restoration and complete actual admission")
    admission = definitions(contents["parent_admission"], "_BW_complete_ASR_admission")
    original, owner, admitted, old_specs, old_contents = admission.parent_closure("AS", contents, specs, manifest)
    actual, execution = admission.complete_actual("AS", original, owner, old_specs, old_contents, contents, specs)
    require(original["parameters"]["complete_raw_source_positive_modes"] == 192
            and old_specs["science"]["path"]
                == TOPIC+"scripts/fourfold_codazzi_original_alpha_full_source_owner.py"
            and actual["private_alpha_trial_receipt"]["positive_modes"] == 2048,
            "the complete successful source192 ASR, after its original ended-failure admission")
    parent = dict(manifest=original, owner=owner, admitted=admitted, specs=old_specs,
                  contents=old_contents, actual=actual, execution=execution)
    carrier = definitions(contents["carrier_original_owner"], "_BW_original_OT_carrier_restoration")
    pure = definitions(contents["BW_math"], "_BW_new_complete_signed_target_errors")
    require(pure.TARGETS == TARGETS and pure.MODES == 2048 and pure.GRID == 8192
            and pure.STRIP_DENOMINATOR == 128, "all new vi/w targets and complete natural mode range")
    return dict(AS=parent, AS_math=admitted[4], SN_restore=admitted[3], carrier=carrier, BW_math=pure)


def observe_original_quadrature(context, destination, progress):
    """One old carrier restoration; an observational wrapper returns each ball unchanged."""
    pure, carrier = context["AS_math"], context["carrier"]
    original_factory = pure.WholeQuadrature
    path = destination/"complete-original-quadrature.jsonl"
    require(not path.exists(), "one new private observation of the original quadrature pass")
    count, digest, size = 0, hashlib.sha256(), 0
    with path.open("w+b") as stream:
        class ObservedQuadrature(original_factory):
            def next(self):
                nonlocal count, size
                n = self.next_n
                value = super().next()
                require(n == count+1, "the same original natural quadrature order")
                pair = [value.real.str(90), value.imag.str(90)]
                formal = self.api.acb(self.api.arb(pair[0]), self.api.arb(pair[1]))
                require(formal.real.contains(value.real) and formal.imag.contains(value.imag),
                        "the full original returned ball is preserved by the read-only record")
                raw = canonical({"mode": n, "whole_original_quadrature_ball": pair})
                offset = stream.tell()
                stream.write(raw)
                stream.flush()
                stream.seek(offset)
                require(stream.read(len(raw)) == raw, "one complete observation saved and read")
                digest.update(raw)
                size += len(raw)
                count += 1
                return value
        pure.WholeQuadrature = ObservedQuadrature
        try:
            restored = carrier.restore_AS(context, destination, progress)
        finally:
            pure.WholeQuadrature = original_factory
    require(count == 2048 and path.stat().st_size == size and sha(path.read_bytes()) == digest.hexdigest(),
            "the entire2048 original integrals from exactly one original carrier pass")
    receipt = {"bytes": size, "sha256": digest.hexdigest(), "positive_modes": count,
               "original_return_values_unchanged": True, "quadrature_passes": 1,
               "old_norm_targets_called": 0}
    return restored, receipt


def exact_midpoint(value):
    a, exponent = map(int, value.mid().man_exp())
    return Fraction(a*2**exponent) if exponent >= 0 else Fraction(a, 2**(-exponent))


def restore_new_vi_w_trial_bytes(api, destination):
    """Only exact finite carriers; reusable later without any BW error/norm target."""
    quadratures = [parse(line) for line in (destination/"complete-original-quadrature.jsonl").read_bytes().splitlines()]
    alpha = parse((destination/"complete-original-AS-alpha-trial.json").read_bytes())
    require(len(quadratures) == 2048 and [value["mode"] for value in quadratures] == list(range(1, 2049))
            and alpha["positive_modes"] == 2048 and alpha["exact_mean"] == "0"
            and alpha["negative_modes_are_exact_conjugates"] is True,
            "whole restored original alpha and all natural quadrature records")
    vi_pairs, w_pairs = [], []
    for observed, alpha_pair in zip(quadratures, alpha["all_positive_exact_pairs"]):
        a, b = [exact_midpoint(api.arb(value)) for value in observed["whole_original_quadrature_ball"]]
        aa, ab = map(Fraction, alpha_pair)
        vi_pairs.append([str(a), str(b)])
        w_pairs.append([str(a-aa), str(b-ab)])
    receipts = {}
    for name, pairs in (("vi", vi_pairs), ("w", w_pairs)):
        body = {"kind": "BW_complete_original_"+name+"_exact_signed_trial_v1", "positive_modes": 2048,
                "all_positive_exact_pairs": pairs, "negative_modes_are_exact_conjugates": True,
                "exact_mean": "0"}
        raw = canonical(body)
        path = destination/("complete-original-"+name+"-trial.json")
        atomic(path, raw)
        require(path.read_bytes() == raw, "whole exact new "+name+" carrier saved/read")
        receipts[name] = {"bytes": len(raw), "sha256": sha(raw), "positive_modes": 2048,
                          "exact_mean": "0", "negative_modes_are_exact_conjugates": True,
                          "complete_trial_only_restoration_without_error_targets": True}
    return quadratures, vi_pairs, w_pairs, receipts


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--manifest-sha", required=True)
    ap.add_argument("--input-map", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--checkout", required=True)
    args = ap.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true" and os.environ.get("GITHUB_REPOSITORY") == REPO
            and os.environ.get("GITHUB_RUN_ATTEMPT") == "1", "one first public complete BW execution")
    raw = args.manifest.read_bytes()
    require(sha(raw) == args.manifest_sha, "the entire first signed-target manifest")
    manifest = parse(raw)
    require(manifest["kind"] == MANIFEST_KIND and manifest["scientific_kind"] == KIND
            and manifest["stage"] == STAGE and manifest["parameters"] == PARAMETERS
            and manifest["target_order"] == TARGETS and manifest["complete_record_counts"] == [4]
            and manifest["allowed_scientific_fields"] == SCI_FIELDS, "the complete new four-error target")
    specs = {value["role"]: value for value in manifest["files"]+manifest["historical_inputs"]}
    paths = parse(args.input_map.read_bytes())
    require(set(paths) == set(specs) and sha(Path(__file__).read_bytes()) == specs["science"]["sha256"],
            "all private whole snapshots and this exact new owner")
    contents = {role: Path(path).read_bytes() for role, path in paths.items()}
    context = admit_complete_inputs(contents, specs, manifest)
    parent, pure, carrier = context["AS"]["actual"], context["BW_math"], context["carrier"]
    require(not args.output.exists(), "retain every earlier actual object")
    document = {
        "identity": {"kind": KIND, "scalar_stage": STAGE, "source_sha256": specs["science"]["sha256"],
            "manifest_sha256": args.manifest_sha, "AS_actual_sha256": specs["AS_actual"]["sha256"],
            "AS_execution_sha256": specs["AS_execution"]["sha256"],
            "AS_manifest_sha256": specs["AS_manifest"]["sha256"], "BW_math_sha256": specs["BW_math"]["sha256"],
            "carrier_original_owner_sha256": specs["carrier_original_owner"]["sha256"],
            "arithmetic_bits": 320, "run_id": os.environ["GITHUB_RUN_ID"], "run_attempt": "1",
            "actual_checkout_commit": args.checkout},
        "complete": False, "proved": False, "actual_returncode": None, "failure": None,
        "stage": "whole_successful_ASR_actual_admitted", "completed_targets": [], "current_target": None,
        "candidate_record": None, "new_records": {}, "saved_record_count": 0, "parameters": PARAMETERS,
        "result": None, "whole_completed_inputs": {role: {"bytes": value["bytes"], "sha256": value["sha256"]}
                                                     for role, value in specs.items()},
        "copied_complete_parent_records": {"AS_identity": copy.deepcopy(parent["identity"]),
            "AS_global_bounds": copy.deepcopy(parent["global_bounds"]),
            "AS_complete_alpha_errors": copy.deepcopy(parent["new_records"]),
            "AS_original_records": copy.deepcopy(parent["copied_original_records"])},
        "runtime": None, "wall_seconds": 0, "progress": {}, "old_scientific_target_calls": 0,
        "necessary_carrier_rematerializations": 0, "original_carrier_restoration": None,
        "private_quadrature_receipt": None, "private_vi_trial_receipt": None, "private_w_trial_receipt": None,
        "private_modes_receipt": None, "complete_tail_bounds": None,
        "complete_mode_prefix": {"complete_modes": 0, "head_Linf_upper": None,
            "head_L2_square_upper": None, "whole_private_mode_prefix_sha256": None},
        "new_arrays_published": 0, "new_artifacts": 0, "new_Releases": 0,
    }
    require(sorted(document) == SCI_FIELDS, "the complete four-error public result schema")
    began = time.perf_counter()
    private = args.output.parent/"private-complete-target-w-carriers"
    private.mkdir()

    def save():
        document["wall_seconds"] = time.perf_counter()-began
        raw = canonical(document)
        require(len(raw) <= manifest["operation"]["maximum_scientific_bytes"], "whole small BW result")
        atomic(args.output, raw)

    def progress(stage, data):
        document["stage"], document["progress"] = stage, data
        save()
        require(document["wall_seconds"] <= PARAMETERS["maximum_scientific_wall_seconds"],
                "the complete finite prefix is saved before the runtime bound")
        print(json.dumps(dict(stage=stage, **data), sort_keys=True), flush=True)

    save()
    try:
        from importlib.metadata import version
        runtime = {"python": platform.python_version(),
                   "packages": {name: version(name) for name in ("numpy", "python-flint")}}
        require(runtime == manifest["runtime"], "the same whole immutable ASR/SN carrier runtime")
        document["runtime"] = runtime
        document["necessary_carrier_rematerializations"] = 1
        save()
        restored, observed = observe_original_quadrature(context, private, progress)
        document["original_carrier_restoration"] = restored
        document["private_quadrature_receipt"] = observed
        progress("all_original_ASR_carriers_and_observed_integrals_saved", {"complete_positive_modes": 2048})
        import flint
        require(flint.ctx.prec == 320 and flint.ctx.cap == 9, "all original directed arithmetic retained")
        api = carrier.directed_api(flint)

        def upper(record):
            return carrier.whole_upper(api, record)

        def encode(value):
            point = value.upper()
            require(point.is_finite() and point >= 0, "complete nonnegative new scalar upper")
            record = {"ball": point.str(60), "bound": "upper"}
            formal = api.arb(record["ball"])
            require(formal.contains(point), "whole directed new scalar round trip")
            return record, formal.upper()

        def saved(value):
            return encode(value)[0]

        quadratures, vi_pairs, w_pairs, receipts = restore_new_vi_w_trial_bytes(api, private)
        document["private_vi_trial_receipt"], document["private_w_trial_receipt"] = receipts["vi"], receipts["w"]
        global_bounds = document["copied_complete_parent_records"]["AS_global_bounds"]
        source_columns = [upper(value) for value in global_bounds["complete_source_error_derivative_columns"]]
        require(len(source_columns) == 4, "all complete old source derivative columns are consumed")
        analytic = pure.complete_analytic_parameters(api, upper(global_bounds["new_raw_trial_Astrip_upper"]),
            upper(global_bounds["complete_original_H_minus_G_upper"]),
            upper(global_bounds["complete_original_G_derivative_upper"]),
            carrier.whole_ball(api, global_bounds["complete_original_map_imaginary_lower"]))
        document["complete_tail_bounds"] = {key: saved(value) for key, value in
            pure.complete_vi_tail(api, analytic, source_columns[3]).items()}
        tail = {key: upper(value) for key, value in document["complete_tail_bounds"].items()}
        head, square, digest, total_bytes = api.zero, api.zero, hashlib.sha256(), 0
        mode_path = private/"complete-new-vi-w-mode-errors.jsonl"
        with mode_path.open("w+b") as stream:
            for n, (quadrature, vi_pair, w_pair) in enumerate(zip(quadratures, vi_pairs, w_pairs), 1):
                observed_ball = api.acb(*(api.arb(value) for value in quadrature["whole_original_quadrature_ball"]))
                exact_vi = api.acb(*(api.rational(Fraction(value)) for value in vi_pair))
                data = pure.complete_vi_mode_error(api, n, observed_ball, exact_vi, source_columns, analytic)
                row = {"mode": n, "whole_original_quadrature_ball": quadrature["whole_original_quadrature_ball"],
                       "exact_vi_trial": vi_pair, "exact_w_trial": w_pair,
                       "negative_modes_are_exact_conjugates": True,
                       "all_source_candidates": [saved(value) for value in data.pop("all_source_candidates")],
                       **{key: saved(value) for key, value in data.items()}}
                raw = canonical(row)
                offset = stream.tell()
                stream.write(raw)
                stream.flush()
                stream.seek(offset)
                read = stream.read(len(raw))
                require(read == raw, "whole new natural mode saved/read before positive accumulation")
                formal = parse(read)
                error = upper(formal["complete_vi_coefficient_error_upper"])
                digest.update(read)
                total_bytes += len(read)
                head, square = (head+2*error).upper(), (square+2*error*error).upper()
                if n % 32 == 0:
                    head_record, head = encode(head)
                    square_record, square = encode(square)
                    document["complete_mode_prefix"] = {"complete_modes": n, "head_Linf_upper": head_record,
                        "head_L2_square_upper": square_record, "whole_private_mode_prefix_sha256": digest.hexdigest()}
                    progress("complete_new_vi_w_mode_error_prefix", {"complete_modes": n, "total_modes": 2048})
        require(mode_path.stat().st_size == total_bytes and sha(mode_path.read_bytes()) == digest.hexdigest(),
                "all2048 complete new signed mode records and exact prefix identity")
        document["private_modes_receipt"] = {"bytes": total_bytes, "sha256": digest.hexdigest(),
            "positive_modes": 2048, "all_sources_aliases_model_and_rounding_fees_retained": True}
        complete = pure.complete_vi_errors(api, upper(document["complete_mode_prefix"]["head_Linf_upper"]),
            upper(document["complete_mode_prefix"]["head_L2_square_upper"]), tail)
        for index, name in enumerate(TARGETS):
            if index == 2:
                alpha = document["copied_complete_parent_records"]["AS_complete_alpha_errors"]
                complete.update(pure.complete_w_errors(upper(document["new_records"][TARGETS[0]]),
                    upper(document["new_records"][TARGETS[1]]), upper(alpha["complete_alpha_trial_Linf_error_upper"]),
                    upper(alpha["complete_alpha_trial_L2_error_upper"])))
            body, value = encode(complete[name])
            document["current_target"], document["candidate_record"] = name, body
            save()
            persisted = parse(args.output.read_bytes())["candidate_record"]
            require(api.arb(persisted["ball"]).contains(value), "whole final new scalar saved/read")
            document["new_records"][name] = persisted
            document["completed_targets"].append(name)
            document["saved_record_count"] = len(document["completed_targets"])
            document["current_target"] = document["candidate_record"] = None
            save()
        document["result"] = {
            "complete_new_record_order": list(TARGETS), "complete_new_record_count": 4,
            "complete_positive_modes": 2048, "same_original_target_w_vi_minus_alpha": True,
            "same_original_target_B_Id_plus_same_sign_Tw_I": True,
            "both_signed_modes_and_exact_zero_mean": True, "both_original_reflection_phases_retained": True,
            "whole_original_raw_grid_alpha_SHA_identical": True, "one_original_quadrature_pass_only": True,
            "all_infinite_tails_aliases_true_map_source_and_rounding_errors_retained": True,
            "exact_rational_vi_minus_alpha_without_new_midpoint": True,
            "both_full_vi_and_w_Linf_L2_errors_proved": True,
            "old_cohomology_alpha_error_SN_norm_or_transport_targets_recomputed": False,
            "physical_mean_slots_eliminated": False, "target_B_inverse_rows_certified": False,
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
    print(json.dumps(dict(complete=True, completed_modes=2048, new_targets=4,
                          old_scientific_target_calls=0, output_sha256=sha(args.output.read_bytes())), sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
