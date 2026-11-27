"""ASR complete source192 alpha carrier after the ended zero-mode AS failure.

Local imports/admission are metadata only. The public owner restores the
original endpoint, runs one new2048-mode carrier and keeps complete tails.
"""
from __future__ import annotations
import argparse
import ast
import copy
import hashlib
import json
import os
import platform
import sys
import time
import textwrap
import traceback
import types
from fractions import Fraction
from pathlib import Path

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby/"
MANIFEST_KIND = "R149_complete_original_alpha_carrier_inputs_v1"
KIND = "R149_complete_original_alpha_signed_carrier_v1"
STAGE = "original_alpha_signed_carrier"
TARGETS = ["complete_alpha_trial_Linf_error_upper", "complete_alpha_trial_L2_error_upper"]
PARAMETERS = {
    "arithmetic_bits": 320, "power_series_cap": 9,
    "positive_modes": 2048, "grid_points": 8192, "physical_strip": "1/128",
    "physical_frequency_factor": 4, "original_SN_run": "43751213826/1",
    "original_SN_intervals": 3146, "original_SN_subcells": 12584,
    "original_SN_endpoint_modes": 128, "original_SN_radial_degree": 6,
    "complete_raw_source_positive_modes": 192, "selected_root_direction_modes": 96,
    "failed_zero_mode_parent_run": "45906100247/1",
    "both_physical_mean_slots_retained": True, "cohomological_divisor_constant": 17,
    "source_reflection_phase": "b=2*true_H(0)+Omega",
    "exact_rotation_numerator": 5831714953207175, "exact_rotation_sqrt5_coefficient": 1,
    "exact_rotation_denominator": 21212218271020390,
    "decimal_record_digits": 60, "private_ball_digits": 90,
    "maximum_scientific_wall_seconds": 16800,
    "completed_SN_residual_energy_norm_or_old_cohomology_targets_repeated": 0,
}
SCI_FIELDS = sorted([
    "identity", "complete", "proved", "actual_returncode", "failure", "stage",
    "completed_targets", "current_target", "candidate_record", "new_records", "saved_record_count",
    "parameters", "result", "whole_completed_inputs", "copied_original_records",
    "old_scientific_target_calls", "necessary_original_input_rematerializations",
    "new_arrays_published", "new_artifacts", "new_Releases", "wall_seconds", "runtime",
    "original_input_restoration", "original_endpoint_restoration", "progress",
    "private_raw_trial_receipt", "private_grid_receipt", "private_modes_receipt", "private_alpha_trial_receipt",
    "complete_mode_prefix", "global_bounds", "complete_tail_bounds",
])
SEI_EXECUTION_SHA = "b0088f831471f29d41624e487586fbb9f4801ef7837f9b4dd3c29a57e51b3d29"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def blob(raw):
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False)+"\n").encode()


def parse(raw):
    return json.loads(raw, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))


def atomic(path, raw):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".partial")
    temporary.write_bytes(raw)
    os.replace(temporary, path)


def definitions(raw, name):
    ast.parse(raw.decode())
    module = types.ModuleType(name)
    exec(compile(raw.decode(), name, "exec"), module.__dict__)
    return module


def admit_ended_zero_mode_failure(contents, specs):
    """Read the whole ended failed attempt; it completed no alpha mode/target."""
    identities = {
        "failed_AS_manifest": (11219, "16bf98e27c7f6bf1f7362d2840249368e342dc70ebed8c31344df87663c745fb"),
        "failed_AS_actual": (8886, "aac7d7db68e43bd22c68faced2f077012b3b9505c19122342323d69d15381d09"),
        "failed_AS_execution": (16401, "2052b326c1e96e3b676837f5a82bf4443f3ee62fc3100c3328324aa571b4e5dc"),
    }
    for role, (size, digest) in identities.items():
        require(len(contents[role]) == size and sha(contents[role]) == digest,
                "whole immutable ended zero-mode attempt: "+role)
    original = parse(contents["failed_AS_manifest"])
    by_path = {spec["path"]: role for role, spec in specs.items()}
    old_specs = {spec["role"]: spec for spec in original["files"]}
    require(original["historical_inputs"] == [] and len(old_specs) == 29,
            "all original AS current and inherited SN inputs")
    old_contents = {}
    for role, spec in old_specs.items():
        here = by_path[spec["path"]]
        require(dict(specs[here], role=role) == spec,
                "each complete old AS input is retained unchanged: "+role)
        old_contents[role] = contents[here]
    old_owner = definitions(old_contents["science"], "_ASR_original_failed_AS_owner")
    old_owner.admit_complete_inputs(old_contents, old_specs)
    require(original["parameters"] == old_owner.PARAMETERS
            and original["target_order"] == old_owner.TARGETS
            and original["allowed_scientific_fields"] == old_owner.SCI_FIELDS,
            "the entire old target contract, without a projected failure substitute")
    old_worker = definitions(old_contents["worker"], "_ASR_original_failed_AS_worker")
    space = dict(require=require, parse=parse, manifest=original, by_role=old_specs,
                 op=original["operation"], args=types.SimpleNamespace(
                     manifest_sha=identities["failed_AS_manifest"][1]),
                 run="45906100247", attempt="1")
    exec(compile(textwrap.dedent(old_worker.VALIDATOR), "_ASR_original_failed_validator", "exec"), space)
    actual = space["validate_output"](contents["failed_AS_actual"])
    receipt = parse(contents["failed_AS_execution"])
    endpoint = actual["original_endpoint_restoration"]
    require(actual["complete"] is actual["proved"] is False
            and type(actual["actual_returncode"]) is int and actual["actual_returncode"] == 1
            and actual["failure"]["type"] == "ValueError"
            and actual["failure"]["message"] == "whole finite original raw source support"
            and actual["stage"] == "whole_original_SN_endpoint_exact_SHA_recovered"
            and actual["completed_targets"] == [] and actual["new_records"] == {}
            and actual["saved_record_count"] == 0
            and actual["complete_mode_prefix"] == {"complete_modes": 0,
                "head_Linf_upper": None, "head_L2_square_upper": None,
                "whole_private_mode_prefix_sha256": None}
            and all(actual[key] is None for key in (
                "private_raw_trial_receipt", "private_grid_receipt", "private_modes_receipt",
                "private_alpha_trial_receipt", "global_bounds", "complete_tail_bounds", "result")),
            "the actual source-support failure preceded every new alpha mode and norm")
    require(endpoint["complete"] is True and endpoint["bytes"] == 245885
            and endpoint["sha256"] == "3048266ba668164d7d9b5475c5262f1f3568cfe32a6e42c7bb496e4bda6c62b6"
            and endpoint["original_intervals"] == 3146 and endpoint["complete_subcells"] == 12584
            and endpoint["original_candidate_pieces"] == 2550
            and endpoint["both_branches_all257_coefficients_retained"] is True
            and endpoint["original_runtime_source_helper_and_serial_rounding_preserved"] is True
            and endpoint["old_completed_residual_energy_norm_targets_replayed"] == 0,
            "the complete original endpoint was genuinely restored before the failure")
    require(receipt["kind"] == "R149_complete_original_alpha_carrier_execution_v1"
            and receipt["repository"] == REPO and receipt["run_id"] == "45906100247"
            and receipt["run_attempt"] == "1" and receipt["complete"] is False
            and type(receipt["actual_child_returncode"]) is int and receipt["actual_child_returncode"] == 1
            and isinstance(receipt["finished_utc"], str) and receipt["finished_utc"]
            and isinstance(receipt["scientific_finished_utc"], str) and receipt["scientific_finished_utc"]
            and receipt["child_timeout"] is False and receipt["scientific_children"] == 1
            and receipt["manifest_sha256"] == identities["failed_AS_manifest"][1]
            and receipt["current_input_receipts"] == original["files"]
            and receipt["actual_scientific_checkout"] == actual["identity"]["actual_checkout_commit"]
            and receipt["old_completed_targets_recomputed"] == 0
            and receipt["completed_original_alpha_modes"] == receipt["completed_new_scalar_targets"] == 0
            and receipt["original_scientific_complete"] is False
            and receipt["original_scientific_failure"] == actual["failure"]
            and receipt["necessary_original_SN_endpoint_restoration"] == endpoint
            and receipt["complete_original_SN_input_restoration"] == actual["original_input_restoration"],
            "the whole public worker ended, and preserves the same complete actual failure")
    require(receipt["scientific_files"] == [{"path": specs["failed_AS_actual"]["path"],
                "bytes": len(contents["failed_AS_actual"]), "sha256": sha(contents["failed_AS_actual"])}],
            "the complete failed scientific file is publicly retained with its exact identity")


def admit_complete_inputs(contents, specs):
    require(set(contents) == set(specs), "all whole AS current inputs")
    for role, raw in contents.items():
        spec = specs[role]
        require(spec["role"] == role and len(raw) == spec["bytes"]
                and sha(raw) == spec["sha256"] and blob(raw) == spec["git_blob_sha"],
                "whole immutable current AS input: "+role)
    restore = definitions(contents["SN_restore"], "_AS_metadata_SN_restore")
    admit_ended_zero_mode_failure(contents, specs)
    original, execution, science = restore.admit_complete_original(contents["SN_manifest"], contents["SN_execution"])
    snapshot_roles = {role for role in contents if role.startswith("SN_text_")}
    expected = {"SN_text_"+str(i).zfill(3): path for i, path in enumerate(original["current_text_paths"])}
    require(snapshot_roles == set(expected)
            and all(specs[role]["path"] == path
                    and sha(contents[role]) == original["files"][path] for role, path in expected.items()),
            "all original current texts, exact original paths and bytes")
    require(len(contents["SEI_execution"]) == 46192 and sha(contents["SEI_execution"]) == SEI_EXECUTION_SHA,
            "complete qualified SEI execution, including its original density scalar")
    sei_execution = parse(contents["SEI_execution"])
    sei = sei_execution["actual_scientific_receipt"]
    require(sei_execution["complete"] is True and sei_execution["actual_returncode"] == 0
            and str(sei_execution["run_id"]) == "43773319871" and str(sei_execution["run_attempt"]) == "1"
            and sei["complete"] is True and sei["proved"] is True and sei["actual_returncode"] == 0
            and sei["failure"] is None and len(sei["gates"]) == 20
            and all(g["passed"] is True for g in sei["gates"])
            and sei["complete_SN_terminal_conclusion_read_verbatim"]
                == science["complete_first_nonmean_coefficient_H3_conclusion"],
            "same entire successful selected SN conclusion consumed by SEI")
    density = sei["complete_new_individual_density_derivative_conclusion"]
    require(density["complete_derivative_orders"] == [0, 1, 2, 3]
            and isinstance(density["complete_sqrt_true_j_upper"]["ball"], str),
            "whole original density Jacobian square-root record")
    proof_words = {
        "WBN_proof": ("WBN.4", "WBN.7", "WBN.14"),
        "WPL_proof": ("WPL.9", "WPL.11", "WPL.12"),
        "RRF_proof": ("RRF.14", "RRF.18"),
        "W_proof": ("W.4", "W.5", "W.9"),
        "proof": ("AS.3", "AS.7", "AS.15"),
        "full_source_proof": ("ASR.1", "ASR.4", "ASR.7"),
    }
    for role, words in proof_words.items():
        text = contents[role].decode()
        require(all(word in text for word in words), "whole exact original operator proof: "+role)
    pure = definitions(contents["alpha_math"], "_AS_pure_original_alpha")
    require((pure.RAW_MODES, pure.MODES, pure.GRID, pure.STRIP_DENOMINATOR) == (192, 2048, 8192, 128),
            "one fixed whole carrier, never mode-cutoff testing")
    require(not any(name in sys.modules for name in ("flint", "numpy", "scipy")),
            "all admission remains metadata only")
    return original, science, density, restore, pure


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--manifest-sha", required=True)
    ap.add_argument("--input-map", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--checkout", required=True)
    args = ap.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPO
            and os.environ.get("GITHUB_RUN_ATTEMPT") == "1", "one first public complete AS execution")
    manifest_raw = args.manifest.read_bytes()
    require(sha(manifest_raw) == args.manifest_sha, "complete AS manifest")
    manifest = parse(manifest_raw)
    require(manifest["kind"] == MANIFEST_KIND and manifest["scientific_kind"] == KIND
            and manifest["stage"] == STAGE and manifest["parameters"] == PARAMETERS
            and manifest["target_order"] == TARGETS and manifest["complete_record_counts"] == [2]
            and manifest["allowed_scientific_fields"] == SCI_FIELDS
            and manifest["historical_inputs"] == [], "whole original-alpha target")
    specs = {spec["role"]: spec for spec in manifest["files"]}
    paths = parse(args.input_map.read_bytes())
    require(set(paths) == set(specs) and sha(Path(__file__).read_bytes()) == specs["science"]["sha256"],
            "all complete private role snapshots and original new owner")
    contents = {role: Path(path).read_bytes() for role, path in paths.items()}
    original, science, density, restore, pure = admit_complete_inputs(contents, specs)
    terminal = science["complete_first_nonmean_coefficient_H3_conclusion"]
    require(not args.output.exists(), "preserve any prior complete or partial actual result")
    document = {
        "identity": {"kind": KIND, "scalar_stage": STAGE, "source_sha256": specs["science"]["sha256"],
            "alpha_math_sha256": specs["alpha_math"]["sha256"], "SN_restore_sha256": specs["SN_restore"]["sha256"],
            "SN_manifest_sha256": restore.MANIFEST_SHA, "SN_execution_sha256": restore.EXECUTION_SHA,
            "manifest_sha256": args.manifest_sha, "run_id": os.environ["GITHUB_RUN_ID"], "run_attempt": "1",
            "event_commit": os.environ["GITHUB_SHA"], "actual_checkout_commit": args.checkout, "arithmetic_bits": 320},
        "complete": False, "proved": False, "actual_returncode": None, "failure": None,
        "stage": "whole_original_SN_SEI_and_phase_definitions_admitted", "completed_targets": [],
        "current_target": None, "candidate_record": None, "new_records": {}, "saved_record_count": 0,
        "parameters": copy.deepcopy(PARAMETERS), "result": None,
        "whole_completed_inputs": {role: {"bytes": spec["bytes"], "sha256": spec["sha256"]}
                                  for role, spec in specs.items()},
        "copied_original_records": {
            "complete_signed_mu": copy.deepcopy(terminal["complete_scalar_mu_copied"]),
            "both_complete_transport_error_columns": copy.deepcopy(science["complete_new_transport_conclusion"]["complete_error_columns"]),
            "complete_true_inverse_density_matrix": copy.deepcopy(terminal["true_angle_derivatives"]["inverse_density_matrix"]),
            "complete_true_sqrt_j_upper": copy.deepcopy(density["complete_sqrt_true_j_upper"])},
        "old_scientific_target_calls": 0, "necessary_original_input_rematerializations": 0,
        "new_arrays_published": 0, "new_artifacts": 0, "new_Releases": 0,
        "wall_seconds": 0.0, "runtime": {}, "original_input_restoration": None,
        "original_endpoint_restoration": None, "progress": {},
        "private_raw_trial_receipt": None, "private_grid_receipt": None, "private_modes_receipt": None,
        "private_alpha_trial_receipt": None,
        "complete_mode_prefix": {"complete_modes": 0, "head_Linf_upper": None,
            "head_L2_square_upper": None, "whole_private_mode_prefix_sha256": None},
        "global_bounds": None, "complete_tail_bounds": None,
    }
    require(sorted(document) == SCI_FIELDS, "entire original-alpha result schema")
    began = time.perf_counter()
    private = args.output.parent/"private-complete-original-alpha-carriers"
    private.mkdir()

    def save():
        document["wall_seconds"] = time.perf_counter()-began
        raw = canonical(document)
        require(len(raw) <= manifest["operation"]["maximum_scientific_bytes"], "one whole small complete AS result")
        atomic(args.output, raw)

    def progress(stage, data):
        document["stage"], document["progress"] = stage, data
        save()
        require(document["wall_seconds"] <= PARAMETERS["maximum_scientific_wall_seconds"],
                "preserved complete original-alpha prefix before time limit")
        print(json.dumps(dict(stage=stage, **data), sort_keys=True), flush=True)

    save()
    try:
        from importlib.metadata import version
        runtime = {"python": platform.python_version(),
                   "packages": {name: version(name) for name in ("numpy", "python-flint")}}
        require(runtime == manifest["runtime"], "unchanged original SN arithmetic runtime")
        document["runtime"] = runtime
        snapshot = {path: contents["SN_text_"+str(i).zfill(3)]
                    for i, path in enumerate(original["current_text_paths"])}
        original_root = private/"whole-original-SN-inputs"
        document["original_input_restoration"] = restore.restore_original_files(
            Path(os.environ["GITHUB_WORKSPACE"]), original_root, contents["SN_manifest"], snapshot, progress)
        document["necessary_original_input_rematerializations"] = 1
        save()
        inp, refs, helper, receipt = restore.rematerialize_original_endpoint(original_root, progress)
        document["original_endpoint_restoration"] = receipt
        progress("whole_original_SN_endpoint_exact_SHA_recovered", {"complete_modes_each_branch": 257})

        import flint
        arb, acb = flint.arb, flint.acb
        require(flint.ctx.prec == 320 and flint.ctx.cap == 9, "original directed point arithmetic retained")

        def rational(n, d=1):
            q = Fraction(n)/Fraction(d)
            return arb(q.numerator)/q.denominator

        api = types.SimpleNamespace(arb=arb, acb=acb, zero=arb(0), one=arb(1), rational=rational)

        def old_ball(record):
            require(isinstance(record, dict) and isinstance(record.get("ball"), str), "whole original formal record")
            value = (arb(record["lower"]).lower().union(arb(record["upper"]).upper())
                     if "lower" in record and "upper" in record else arb(record["ball"]))
            require(value.is_finite(), "whole original finite ball")
            return value

        def upper(record):
            value = old_ball(record)
            require(value.lower() >= 0, "complete nonnegative old upper")
            return value.upper()

        def encode(value, bound="upper"):
            point = value.lower() if bound == "lower" else value.upper()
            require(point.is_finite() and (bound == "lower" or point >= 0), "complete directed scalar record")
            body = {"ball": point.str(PARAMETERS["decimal_record_digits"]), "bound": bound}
            formal = arb(body["ball"])
            require(formal.contains(point), "complete new scalar round trip")
            return body, formal.lower() if bound == "lower" else formal.upper()

        def saved_upper(value):
            body, point = encode(value)
            return body

        # Original terminal chi and mean enter one complete raw signed field.
        # This calls only point algebra; every old norm/validation routine is disabled.
        chi = inp.root_data(1, True)["chi"].v.value().ne()/inp.rs.sqrt()
        raw = refs[1]+chi-inp.mu/2
        progress("whole_original_raw_source_support_formed", {
            "endpoint_support": [refs[1].lo, refs[1].hi],
            "complete_selected_chi_support": [chi.lo, chi.hi],
            "complete_raw_source_support": [raw.lo, raw.hi],
            "retained_raw_positive_modes": pure.RAW_MODES})
        require(pure.RAW_MODES == PARAMETERS["complete_raw_source_positive_modes"]
                and raw.lo >= -pure.RAW_MODES and raw.hi <= pure.RAW_MODES,
                "whole finite original raw source192 support")
        mean = rational(helper.rat(raw.mean()))
        positive, radius = [], [abs(raw.mean()-mean).upper(), arb(0), arb(0), arb(0)]
        exact_pairs = []
        for n in range(1, pure.RAW_MODES+1):
            z = (raw.coeff(n)+raw.coeff(-n).conjugate())/2
            a, b = helper.rat(z.real), helper.rat(z.imag)
            point = acb(rational(a), rational(b))
            positive.append(point)
            exact_pairs.append([str(a), str(b)])
            fee = abs(z-point).upper()
            for q in range(4):
                radius[q] = radius[q]+2*(4*n)**q*fee
        raw_trial = {"kind": "AS_complete_raw_signed_trial_v1", "positive_modes": pure.RAW_MODES,
                     "exact_mean": str(helper.rat(mean)), "all_positive_exact_pairs": exact_pairs,
                     "negative_modes_are_exact_conjugates": True}
        raw_trial_bytes = canonical(raw_trial)
        atomic(private/"complete-raw-trial.json", raw_trial_bytes)
        formal_raw = parse((private/"complete-raw-trial.json").read_bytes())
        require(canonical(formal_raw) == raw_trial_bytes, "whole exact raw finite carrier saved/read")
        positive = [acb(rational(Fraction(a)), rational(Fraction(b))) for a, b in formal_raw["all_positive_exact_pairs"]]
        mean = rational(Fraction(formal_raw["exact_mean"]))
        document["private_raw_trial_receipt"] = {"bytes": len(raw_trial_bytes), "sha256": sha(raw_trial_bytes),
                                                 "positive_modes": pure.RAW_MODES, "mean_retained": True}
        # Formalize all four new enclosure radii before dependent combinations.
        radius_records = [saved_upper(value) for value in radius]
        radius = [upper(value) for value in radius_records]
        original_errors = [upper(value) for value in terminal["branches"]["1"]["complete_transport_derivative_L2_error"]]
        matrix = [[upper(value) for value in row] for row in terminal["true_angle_derivatives"]["inverse_density_matrix"]]
        source_errors = pure.source_error_columns(api, original_errors, radius, matrix,
                                                 upper(density["complete_sqrt_true_j_upper"]))
        source_records = [saved_upper(value) for value in source_errors]
        source_errors = [upper(value) for value in source_records]
        T_record = saved_upper(pure.raw_trial_strip_norm(api, positive, mean))
        W = inp.strip
        analytic = pure.complete_analytic_data(api, upper(T_record),
            upper(W["selected"]["physical_true_conjugacy_minus_G_norm"]),
            upper(W["exact_G_derivative_norm"]),
            upper(W["selected"]["physical_true_conjugacy_derivative_Astrip_upper"]))
        document["global_bounds"] = {"raw_trial_radius_columns": radius_records,
            "complete_source_error_derivative_columns": source_records,
            "new_raw_trial_Astrip_upper": T_record,
            "complete_original_map_imaginary_lower": encode(analytic["m"], "lower")[0],
            "complete_original_H_minus_G_upper": copy.deepcopy(W["selected"]["physical_true_conjugacy_minus_G_norm"]),
            "complete_original_G_derivative_upper": copy.deepcopy(W["exact_G_derivative_norm"]),
            "complete_original_H_derivative_upper": copy.deepcopy(W["selected"]["physical_true_conjugacy_derivative_Astrip_upper"])}
        tail = pure.complete_tail(api, analytic, source_errors[3])
        tail_records = {key: saved_upper(value) for key, value in tail.items()}
        document["complete_tail_bounds"] = tail_records
        tail = {key: upper(value) for key, value in tail_records.items()}
        progress("complete_raw_trial_and_all_error_columns_saved", {"raw_positive_modes": pure.RAW_MODES})

        grid = pure.original_grid(api, positive, mean, inp.Hs, inp.Hc, inp.Ks, inp.Kc)
        grid_body = {"kind": "AS_complete_original_G_raw_t_grid_v1", "complete_count": 8192,
                     "all_pairs": [[t.str(90), g.str(90)] for t, g in grid]}
        grid_raw = canonical(grid_body)
        atomic(private/"complete-original-G-raw-t-grid.json", grid_raw)
        formal_grid = parse((private/"complete-original-G-raw-t-grid.json").read_bytes())
        grid_read = [(arb(t), arb(g)) for t, g in formal_grid["all_pairs"]]
        require(len(grid_read) == 8192 and all(t.contains(t0) and g.contains(g0)
                    for (t, g), (t0, g0) in zip(grid_read, grid)), "whole directed original grid saved/read")
        document["private_grid_receipt"] = {"bytes": len(grid_raw), "sha256": sha(grid_raw), "complete_count": 8192}
        omega, phase = pure.original_rotation_and_phase(api, grid_read[0][1], analytic["EH"])
        document["global_bounds"]["complete_exact_rotation_ball"] = omega.str(90)
        document["global_bounds"]["complete_original_source_phase_ball"] = phase.str(90)
        factory = pure.WholeQuadrature(api, grid_read)
        mode_path = private/"complete-original-alpha-modes.jsonl"
        digest = hashlib.sha256()
        head_W, head_square, carrier_bytes = arb(0), arb(0), 0
        with mode_path.open("w+b") as stream:
            for n in range(1, 2049):
                quadrature = factory.next()
                # Both real and imaginary full quadrature balls survive before use.
                integral_text = [quadrature.real.str(90), quadrature.imag.str(90)]
                formal_integral = acb(arb(integral_text[0]), arb(integral_text[1]))
                require(formal_integral.real.contains(quadrature.real)
                        and formal_integral.imag.contains(quadrature.imag), "complete signed integral round trip")
                data = pure.complete_mode_data(api, n, formal_integral, source_errors, analytic, omega, phase)
                coefficient = data.pop("coefficient")
                a, b = helper.rat(coefficient.real), helper.rat(coefficient.imag)
                trial = acb(rational(a), rational(b))
                error = (abs(coefficient-trial).upper()+data["extra_error"]).upper()
                error_record, error_formal = encode(error)
                mode = {"mode": n, "exact_trial": [str(a), str(b)], "negative_is_exact_conjugate": True,
                    "quadrature_ball": integral_text,
                    "full_phase_coefficient_ball": [coefficient.real.str(90), coefficient.imag.str(90)],
                    "complete_coefficient_error_upper": error_record,
                    "source_candidates": [saved_upper(value) for value in data["source_candidates"]],
                    "source_error": saved_upper(data["source"]), "map_error": saved_upper(data["model"]),
                    "all_alias_error": saved_upper(data["aliases"]),
                    "exact_divisor_lower": encode(data["divisor_lower"], "lower")[0]}
                mode_raw = canonical(mode)
                offset = stream.tell()
                stream.write(mode_raw)
                stream.flush()
                stream.seek(offset)
                read = stream.read(len(mode_raw))
                require(read == mode_raw, "whole natural mode written and read before accumulation")
                formal_mode = parse(read)
                error_formal = upper(formal_mode["complete_coefficient_error_upper"])
                digest.update(read)
                carrier_bytes += len(read)
                head_W = (head_W+2*error_formal).upper()
                head_square = (head_square+2*error_formal*error_formal).upper()
                if n % 32 == 0 or n == 2048:
                    W_record, head_W = encode(head_W)
                    square_record, head_square = encode(head_square)
                    document["complete_mode_prefix"] = {"complete_modes": n,
                        "head_Linf_upper": W_record, "head_L2_square_upper": square_record,
                        "whole_private_mode_prefix_sha256": digest.hexdigest()}
                    progress("complete_original_alpha_mode_prefix", {"complete_modes": n, "total_modes": 2048})
        require(mode_path.stat().st_size == carrier_bytes and sha(mode_path.read_bytes()) == digest.hexdigest(),
                "one whole private signed alpha carrier, every2048 natural mode")
        document["private_modes_receipt"] = {"bytes": carrier_bytes, "sha256": digest.hexdigest(),
            "positive_modes": 2048, "negative_modes_are_exact_conjugates": True, "mean_is_exactly_zero": True,
            "all_coefficients_errors_aliases_and_phase_records_present": True}
        # A DISTINCT whole trial identity allows later reconstruction of the
        # signed carrier alone, without repeating this run's completed norms.
        saved_modes = [parse(line) for line in mode_path.read_bytes().splitlines()]
        require(len(saved_modes) == 2048
                and [value["mode"] for value in saved_modes] == list(range(1, 2049)),
                "all original exact trial pairs in natural order")
        alpha_trial = {"kind": "AS_complete_original_alpha_dyadic_trial_v1", "positive_modes": 2048,
            "all_positive_exact_pairs": [value["exact_trial"] for value in saved_modes],
            "exact_mean": "0", "negative_modes_are_exact_conjugates": True}
        alpha_raw = canonical(alpha_trial)
        atomic(private/"complete-original-alpha-trial.json", alpha_raw)
        require((private/"complete-original-alpha-trial.json").read_bytes() == alpha_raw,
                "separate whole signed trial carrier saved and read")
        document["private_alpha_trial_receipt"] = {"bytes": len(alpha_raw), "sha256": sha(alpha_raw),
            "positive_modes": 2048, "exact_mean": "0", "negative_modes_are_exact_conjugates": True,
            "carrier_only_restoration_does_not_repeat_mode_error_norms": True}
        complete = pure.complete_errors(api, upper(document["complete_mode_prefix"]["head_Linf_upper"]),
            upper(document["complete_mode_prefix"]["head_L2_square_upper"]), tail)
        for name in TARGETS:
            body, value = encode(complete[name])
            document["current_target"], document["candidate_record"] = name, body
            save()
            persisted = parse(args.output.read_bytes())["candidate_record"]
            require(arb(persisted["ball"]).contains(value), "whole final new scalar saved/read")
            document["new_records"][name] = persisted
            document["completed_targets"].append(name)
            document["saved_record_count"] = len(document["completed_targets"])
            document["current_target"] = document["candidate_record"] = None
            save()
        document["result"] = {
            "complete_new_record_order": list(TARGETS), "complete_new_record_count": 2,
            "complete_positive_modes": 2048, "complete_raw_source_positive_modes": pure.RAW_MODES,
            "both_signed_modes_and_exact_zero_mean": True,
            "same_original_alpha_vi_minus_w": True, "actual_source_phase_b_a_plus_Omega_retained": True,
            "original_divisor_and_all_infinite_tails_paid": True,
            "both_full_Linf_and_L2_trial_errors_proved": True,
            "old_complete_SN_endpoint_SHA_required_and_verified": True,
            "all_old_SN_validation_norm_or_cohomology_targets_replayed": False,
            "physical_mean_slots_eliminated": False, "actual_Theta_or_full_Schur_proved": False,
            "topic_completion_proved": False}
        document["complete"] = document["proved"] = True
        document["actual_returncode"] = 0
        document["stage"] = "complete_"+STAGE+"_branch"
    except BaseException as exc:
        document["actual_returncode"] = 1
        document["failure"] = {"type": type(exc).__name__, "message": str(exc), "traceback": traceback.format_exc()}
        save()
        raise
    save()
    print(json.dumps(dict(complete=True, completed_modes=2048, new_targets=2,
                          old_scientific_target_calls=0, output_sha256=sha(args.output.read_bytes())), sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
