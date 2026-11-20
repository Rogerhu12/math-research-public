"""Five new Hhalf body coefficients, and a conditional root allowance, from whole X/Y.

Only saved scalar arithmetic is new. No former source, native, frame, Fourier
array, radial propagation, or successful target is imported or recomputed.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import sys
import time
import traceback

REPO = "Rogerhu12/math-research-public"
KIND = "R138_same_Qrepair_capped_Hhalf_saved_body_budget_v1"
RECORD_NAMES = ["wE_half_upper", "wB_half_upper", "aEE_upper", "aEB_upper", "aBB_upper"]
OPTIONAL_RECORD_NAME = "C_allow_lower"
PARAMETERS = {
    "arithmetic_bits": 320, "decimal_record_digits": 75,
    "maximum_scientific_wall_seconds": 600,
    "mandatory_new_target_count": 5, "conditional_new_target_count": 1,
    "old_completed_target_calls": 0, "new_numerical_ODE_or_integral_calls": 0,
    "Grushin_energy_coefficient": "5/2",
    "Grushin_outer_trace_coefficient": "3/sqrt(2)",
    "complete_outer_rotation_coefficient": "8/5",
    "curvature_lower_comparison": "min(46*x,1/40)",
    "true_length_contract": ["14/5", "29/10"],
    "body_Sobolev_order": "1/2", "old_root_defect_Sobolev_order": "-1/3",
    "ordinary_radial_measure": "dr", "angular_measure": "unnormalised full 2*pi",
    "root_allowance_formula": "det(M)/(2*r^T*adj(M)*r)",
    "root_rE_rB_source": "whole completed Y; unchanged H^(2/3) path",
}
INPUTS = {
    "completed_X_budget": {
        "path": "notes/physical_energy_budget_ci/run-44737045152-1/physical-energy-conclusion.json",
        "bytes": 15024, "sha256": "1259c3687cea0af523dd52055e88d5ee9a7b77094c218101835b6c38dfbbc7ec"},
    "completed_X_execution": {
        "path": "notes/physical_energy_budget_ci/run-44737045152-1/execution.json",
        "bytes": 14233, "sha256": "999555eafb3c443266f1a8fed98056c9d4f448c0131ef5ffff93941b35040c92"},
    "completed_Y_budget": {
        "path": "notes/composed_physical_energy_budget_ci/run-44740320925-1/composed-physical-energy-conclusion.json",
        "bytes": 8482, "sha256": "19b489ce0b8b85d4223ea334f7e2397188755d42605bf7613d2023ac69cb2cf3"},
    "completed_Y_execution": {
        "path": "notes/composed_physical_energy_budget_ci/run-44740320925-1/execution.json",
        "bytes": 15211, "sha256": "2e4cea611a229dbf894bae1fb2478ebc2219f9c0282a84cae1abd32ceb54f084"},
}
OLD = {
    "X": {"kind": "R138_same_Qrepair_complete_physical_energy_budget_v1",
        "source_sha256": "716fde1b56617680898ed61e7ebc0da0177c086e1a0f8865e36a5d7ff9b6a2eb",
        "manifest_sha256": "5058a2fa68512524be46b9505a28513024e2f990231ff670de14b7876bfbea47",
        "run_id": "44737045152", "stage": "complete-new-physical-scalar-budget",
        "execution_kind": "R138_complete_physical_energy_public_execution_v1"},
    "Y": {"kind": "R138_same_Qrepair_composed_physical_energy_budget_v1",
        "source_sha256": "3fca5cd0b9da843bc8c56128c31f9c307456769952dc0f64b7c3f59f66a1aff1",
        "manifest_sha256": "c12794d7b0e817332ad57395ebbf206582b2779a02ee38292dec1e622fc8c197",
        "run_id": "44740320925", "stage": "complete-new-composed-physical-scalar-budget",
        "execution_kind": "R138_complete_composed_physical_energy_public_execution_v1"},
}
SCI_FIELDS = sorted([
    "identity", "complete", "proved", "actual_returncode", "failure", "stage",
    "completed_targets", "current_target", "new_records", "saved_record_count",
    "parameters", "scope", "whole_completed_inputs", "reference_identity",
    "old_comparison_outcomes", "reused_scalar_paths", "body_only_sufficient_comparison",
    "conditional_root_allowance", "old_scientific_target_calls", "old_scientific_source_imports",
    "new_numerical_ODE_or_integral_calls", "new_arrays_published", "new_artifacts",
    "new_Releases", "wall_seconds", "runtime",
])


def require(ok, message):
    if not ok:
        raise ValueError(message)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def git_blob(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False) + "\n").encode()


def parse(raw):
    return json.loads(raw, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))


def atomic(path, raw):
    temporary = path.with_name(path.name + ".partial")
    with temporary.open("wb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)
    require(path.read_bytes() == raw, "whole new scalar prefix exact byte readback")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--manifest-sha", required=True)
    parser.add_argument("--input-map", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--checkout", required=True)
    args = parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPO,
            "new directed scalar combinations only in this public Actions repository")
    manifest_raw = args.manifest.read_bytes()
    require(digest(manifest_raw) == args.manifest_sha, "whole pinned new consumer manifest")
    manifest = parse(manifest_raw)
    require(manifest["scientific_kind"] == KIND and manifest["parameters"] == PARAMETERS
            and manifest["target_order"] == RECORD_NAMES
            and manifest["conditional_target"] == OPTIONAL_RECORD_NAME
            and manifest["historical_inputs"] == [], "exact five new targets and conditional root allowance")
    specs = {item["role"]: item for item in manifest["files"]}
    paths = parse(args.input_map.read_bytes())
    require(set(paths) == set(specs), "all complete current input snapshots")
    complete_bytes = {}
    for role, item in specs.items():
        raw = Path(paths[role]).read_bytes()
        require(0 < len(raw) < 100000 and len(raw) == item["bytes"]
                and digest(raw) == item["sha256"] and git_blob(raw) == item["git_blob_sha"],
                "whole input byte identity: " + role)
        complete_bytes[role] = raw
    require(digest(Path(__file__).read_bytes()) == specs["science"]["sha256"],
            "the exact publicly pinned numerical source")
    for role, expected in INPUTS.items():
        require(specs[role]["path"] == "topics/visible-flex-exact-nearby/" + expected["path"]
                and specs[role]["bytes"] == expected["bytes"]
                and specs[role]["sha256"] == expected["sha256"], "same whole completed X/Y object: " + role)
    old = {}
    for label in ("X", "Y"):
        role = "completed_" + label + "_budget"
        doc = parse(complete_bytes[role])
        execution = parse(complete_bytes["completed_" + label + "_execution"])
        accepted = OLD[label]
        require(doc["complete"] is True and doc["proved"] is True and doc["failure"] is None
                and doc["completed_closed_cells"] == 4651 and doc["stage"] == accepted["stage"]
                and doc["identity"]["kind"] == accepted["kind"]
                and doc["identity"]["source_sha256"] == accepted["source_sha256"]
                and doc["identity"]["arithmetic_bits"] == 320
                and doc["identity"]["new_complete_closed_cell_count"] == 4651,
                "entire completed physical budget: " + label)
        require(execution["kind"] == accepted["execution_kind"]
                and execution["complete"] is True and execution["failure"] is None
                and execution["original_scientific_complete"] is True
                and execution["original_scientific_failure"] is None
                and execution["actual_child_returncode"] == 0
                and execution["scientific_children"] == 1
                and execution["completed_closed_cells"] == 4651
                and execution["run_id"] == accepted["run_id"] and execution["run_attempt"] == "1"
                and execution["manifest_sha256"] == accepted["manifest_sha256"]
                and execution["old_completed_targets_recomputed"] == 0
                and execution["old_numerical_producers_called"] == 0,
                "entire completed public execution: " + label)
        matching = [item for item in execution["scientific_files"] if item["path"] == specs[role]["path"]]
        require(len(matching) == 1 and matching[0]["bytes"] == len(complete_bytes[role])
                and matching[0]["sha256"] == digest(complete_bytes[role]),
                "old execution identifies the entire saved actual: " + label)
        for flag in ("same_fixed_eta_nu_and_Qrepair", "full_real_angular_circle",
                     "true_root_not_replaced_by_interval_endpoint", "complete_means_retained",
                     "complete_original_interfaces_retained", "actual_DF_not_WVC_hybrid"):
            require(doc["scope"][flag] is True, "same complete physical qualification: " + flag)
        for flag in ("root_boundary_form_constant_paid", "full_positive_inverse_proved", "final_topic_complete"):
            require(doc["scope"][flag] is False, "preserve original unpaid gate: " + flag)
        require(doc["old_scientific_target_calls"] == 0 and doc["published_Fourier_or_frame_arrays"] == 0,
                "original complete no-recomputation qualification")
        old[label] = doc
    X, Y = old["X"], old["Y"]
    for key, value in X["identity"].items():
        if key not in ("kind", "source_sha256"):
            require(Y["identity"][key] == value, "same full X/Y intrinsic and repaired identity: " + key)
    require(Y["identity"]["prior_complete_budget_sha256"] == INPUTS["completed_X_budget"]["sha256"]
            and Y["identity"]["prior_complete_execution_sha256"] == INPUTS["completed_X_execution"]["sha256"]
            and Y["identity"]["prior_source_sha256"] == OLD["X"]["source_sha256"]
            and Y["prior_complete_budget"]["whole_original_scope_and_false_gates_retained"] is True
            and Y["stage"] == OLD["Y"]["stage"], "the composed Y consumes exactly this entire X")
    require(not any(name in sys.modules for name in ("flint", "numpy", "scipy")),
            "whole completed admission precedes all numerical imports")
    run, attempt = os.environ["GITHUB_RUN_ID"], os.environ["GITHUB_RUN_ATTEMPT"]
    require(attempt == "1" and not args.output.exists(), "one new never-overwritten target occurrence")
    args.output.parent.mkdir(parents=True, exist_ok=True)

    document = {
        "identity": {"kind": KIND, "source_sha256": specs["science"]["sha256"],
            "manifest_sha256": args.manifest_sha, "run_id": run, "run_attempt": attempt,
            "event_commit": os.environ["GITHUB_SHA"], "actual_checkout_commit": args.checkout,
            "completed_X_budget_sha256": specs["completed_X_budget"]["sha256"],
            "completed_X_execution_sha256": specs["completed_X_execution"]["sha256"],
            "completed_Y_budget_sha256": specs["completed_Y_budget"]["sha256"],
            "completed_Y_execution_sha256": specs["completed_Y_execution"]["sha256"],
            "arithmetic_bits": PARAMETERS["arithmetic_bits"]},
        "complete": False, "proved": False, "actual_returncode": None, "failure": None,
        "stage": "whole_completed_XY_admitted", "completed_targets": [], "current_target": None,
        "new_records": {}, "saved_record_count": 0, "parameters": copy.deepcopy(PARAMETERS), "runtime": {},
        "whole_completed_inputs": {role: {"file": copy.deepcopy(specs[role]), "json_path": [],
            "whole_prior_conclusion_and_all_scopes_retained": True} for role in INPUTS},
        "reference_identity": copy.deepcopy(X["identity"]),
        "old_comparison_outcomes": {label: copy.deepcopy(old[label]["body_only_sufficient_comparison"])
                                    for label in ("X", "Y")},
        "reused_scalar_paths": {
            "X": [["new_scalar_suprema", k] for k in ("C_E", "C_H", "A_Theta")]
                 + [["complete_derived_energy_bounds", k] for k in ("Gamma", "h_B")],
            "Y": [["new_scalar_suprema", k] for k in ("E_0", "E_1")]
                 + [["complete_derived_energy_bounds", k] for k in ("h_E", "r_E", "r_B")]},
        "body_only_sufficient_comparison": None,
        "conditional_root_allowance": {"status": "not_reached", "actual_C_star_paid": False,
            "old_Y_root_rE_rB_unchanged": True, "half_matrix_margin": "1/2"},
        "old_scientific_target_calls": 0, "old_scientific_source_imports": 0,
        "new_numerical_ODE_or_integral_calls": 0,
        "new_arrays_published": 0, "new_artifacts": 0, "new_Releases": 0, "wall_seconds": 0.0,
        "scope": {"same_fixed_eta_nu_and_Qrepair": True, "full_real_angular_circle": True,
            "true_root_not_replaced_by_interval_endpoint": True, "complete_means_retained": True,
            "complete_original_interfaces_retained": True, "actual_DF_not_WVC_hybrid": True,
            "root_endpoint_condition_added": False, "whole_environment_zero_mode_retained": True,
            "new_body_Hhalf_bounds_proved": False, "root_Htwo_thirds_path_changed": False,
            "complete_prior_XY_outcomes_preserved": True, "root_boundary_form_constant_paid": False,
            "full_positive_inverse_proved": False, "either_original_RHS_proved": False,
            "final_topic_complete": False}}
    require(sorted(document) == SCI_FIELDS, "complete declared small scalar schema")
    began = time.perf_counter()

    def save():
        document["wall_seconds"] = time.perf_counter() - began
        raw = canonical(document)
        require(len(raw) <= manifest["operation"]["maximum_scientific_bytes"], "whole scalar prefix budget")
        atomic(args.output, raw)

    save()
    try:
        import flint
        import platform
        from importlib.metadata import version
        runtime = {"python": platform.python_version(), "packages": {"python-flint": version("python-flint")}}
        require(runtime == manifest["runtime"], "same completed public fixed directed runtime")
        document["runtime"] = runtime
        flint.ctx.prec = PARAMETERS["arithmetic_bits"]
        arb = flint.arb

        def unpack(record):
            require(isinstance(record, dict) and record.get("kind") == "complete_decimal_ball_v1",
                    "whole saved integer-decimal scalar ball")
            midpoint, radius, exponent = (int(record[k]) for k in
                                         ("midpoint_integer", "radius_integer", "decimal_exponent"))
            require(radius >= 0 and abs(exponent) <= 10000, "finite complete decimal scale and radius")
            lo = arb(str(midpoint-radius) + "e" + str(exponent)).lower()
            hi = arb(str(midpoint+radius) + "e" + str(exponent)).upper()
            value = lo.union(hi)
            require(value.is_finite(), "finite whole saved decimal enclosure")
            return value

        def upper(value):
            require(value.is_finite(), "finite complete directed scalar")
            endpoint = value.upper()
            require(endpoint.lower() >= 0, "nonnegative mathematical upper endpoint")
            return endpoint

        def old_upper(label, group, name):
            return upper(unpack(old[label][group][name]))

        def emit(name, value, direction="upper"):
            expected = RECORD_NAMES + [OPTIONAL_RECORD_NAME]
            require(expected[document["saved_record_count"]] == name, "declared whole scalar order")
            require(time.perf_counter()-began <= PARAMETERS["maximum_scientific_wall_seconds"],
                    "fixed small-target wall cap with full prefix preserved")
            document["current_target"] = name
            save()
            point = upper(value) if direction == "upper" else value.lower()
            require(point.is_finite() and point.lower() >= 0, "finite directed nonnegative saved endpoint")
            m, r, e = point.mid_rad_10exp(PARAMETERS["decimal_record_digits"])
            record = {"kind": "complete_decimal_ball_v1", "midpoint_integer": str(int(m)),
                      "radius_integer": str(int(r)), "decimal_exponent": str(int(e)),
                      "mathematical_direction": direction}
            require(unpack(record).contains(point), "whole new decimal record encloses its directed endpoint")
            document["new_records"][name] = record
            document["saved_record_count"] += 1
            document["completed_targets"].append(name)
            document["current_target"] = None
            document["stage"] = "complete_new_scalar_record_saved"
            save()
            reread = parse(args.output.read_bytes())["new_records"][name]
            require(reread == record and unpack(reread).contains(point),
                    "actual saved whole decimal exact readback and inclusion")
            print(canonical({"new_record_saved": name, "direction": direction,
                "completed_new_targets": document["saved_record_count"]}).decode(), end="", flush=True)
            return unpack(reread).upper() if direction == "upper" else unpack(reread).lower()

        CE = old_upper("X", "new_scalar_suprema", "C_E")
        CH = old_upper("X", "new_scalar_suprema", "C_H")
        AT = old_upper("X", "new_scalar_suprema", "A_Theta")
        Gamma = old_upper("X", "complete_derived_energy_bounds", "Gamma")
        hB = old_upper("X", "complete_derived_energy_bounds", "h_B")
        hE = old_upper("Y", "complete_derived_energy_bounds", "h_E")
        E0 = old_upper("Y", "new_scalar_suprema", "E_0")
        E1 = old_upper("Y", "new_scalar_suprema", "E_1")
        wE = emit(RECORD_NAMES[0], (arb(5)/2)*Gamma*AT.sqrt()*(CE.sqrt()+CH.sqrt()*hE))
        wB = emit(RECORD_NAMES[1], (arb(5)/2)*Gamma*(AT*CH).sqrt()*hB
                  + (arb(24)/(5*arb(2).sqrt()))*AT*Gamma.sqrt())
        aEE = emit(RECORD_NAMES[2], E0*wE*wE+E1*wE*hE)
        aEB = emit(RECORD_NAMES[3], 2*E0*wE*wB+E1*(wE*hB+wB*hE))
        aBB = emit(RECORD_NAMES[4], E0*wB*wB+E1*wB*hB)
        # Every gate consumes the upper endpoint read back from the saved ball.
        u, v, cross = arb(2)-aEE, arb(1)-aBB, aEB/2
        determinant = u*v-cross*cross
        gates = {"E_coefficient_less_than_2": bool(u.lower() > 0),
                 "B_coefficient_less_than_1": bool(v.lower() > 0),
                 "cross_discriminant_positive": bool(determinant.lower() > 0)}
        body_pass = all(gates.values())
        document["body_only_sufficient_comparison"] = {
            **gates, "all_body_gates_pass": body_pass,
            "root_constant_for_this_diagnostic": "0; actual root constant remains independent",
            "comparison_uses_saved_complete_upper_endpoints": True,
            "false_is_not_a_singularity_claim": True}
        save()
        if body_pass:
            rE = old_upper("Y", "complete_derived_energy_bounds", "r_E")
            rB = old_upper("Y", "complete_derived_energy_bounds", "r_B")
            denominator = 2*(v*rE*rE+2*cross*rE*rB+u*rB*rB)
            require(denominator.lower() > 0, "old nonzero root trace vector gives a positive denominator")
            allowance = emit(OPTIONAL_RECORD_NAME, determinant/denominator, direction="lower")
            require(allowance > 0, "saved complete root allowance has a strictly positive lower endpoint")
            document["conditional_root_allowance"].update(
                status="complete_positive_lower", comparison="actual C_star <= saved C_allow lower",
                saved_lower_is_strictly_positive=True)
        else:
            document["conditional_root_allowance"].update(status="not_computed_body_gate_false")
        require(document["completed_targets"] == RECORD_NAMES + ([OPTIONAL_RECORD_NAME] if body_pass else []),
                "all five mandatory bounds and exactly the qualified conditional target")
        document["scope"]["new_body_Hhalf_bounds_proved"] = True
        document.update(complete=True, proved=True, actual_returncode=0, failure=None,
                        stage="complete_capped_Hhalf_saved_body_budget")
        save()
    except BaseException as exc:
        document.update(complete=False, proved=False, actual_returncode=1,
                        failure={"type": type(exc).__name__, "message": str(exc),
                                 "traceback": traceback.format_exc()}, stage="failed_with_whole_scalar_prefix")
        save()
        raise


if __name__ == "__main__":
    main()
