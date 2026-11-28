"""Whole successful WMT14+BFP19 receipts to the same signed Theta-nu column.

This is an exact saved-ball consequence, not a rerun of either producer.
It changes only the qualified global Theta slot in BFP.22/WMT.19 and
keeps every original exact signed center, all old fees and both means.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import re
import textwrap
import types
from fractions import Fraction
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
REPO = "Rogerhu12/math-research-public"
BALL = re.compile(r"^\[([^\[\]]+) \+/- ([^\[\]]+)\]$")
TARGET = "complete_weighted_model_true_Theta_nu_joint_error_upper"
PARENTS = {
    14: {"manifest_sha256": "4913fe4ce57cd579741b65090cd5e6dae22392956545196c888c3061b8974ffb", "validator_role": "worker",
         "kind": "R149_complete_weighted_model_Theta_receiver_v1"},
    19: {"manifest_sha256": "363c2116c8459e202209503bc40e379f40d502c89c92c3982971112f602e23ce", "validator_role": "worker",
         "kind": "R147_complete_full_target_nu_forward_v1"},
    3: {"manifest_sha256": "0205e488d6932e2348725306f7be7e13d9829461b84cdedfe170e3cadeab24d3", "validator_role": "worker",
        "kind": "R149_complete_target_B_Gram_v1"},
    7: {"manifest_sha256": "74bb82d9c9640d8ffd3a6350c3d56a0fa34b6bd7d7b451775f428786a5e35b9e", "validator_role": "original_BNC_worker",
        "kind": "R147_complete_target_normalized_strict_nu_column_v1"},
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def parse(raw):
    return json.loads(raw, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))


def encode(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                       allow_nan=False)+"\n").encode()


def exact_interval(text):
    require(isinstance(text, str), "one full saved native ball string")
    match = BALL.fullmatch(text.strip())
    if match:
        midpoint, radius = map(Fraction, match.groups())
        require(radius >= 0, "a whole nonnegative saved radius")
        return midpoint-radius, midpoint+radius
    value = Fraction(text.strip())
    return value, value


def upper(record):
    require(isinstance(record, dict) and record.get("bound") == "upper", "one whole original upper record")
    lo, hi = exact_interval(record["ball"])
    require(lo >= 0, "whole nonnegative directed saved upper")
    return hi


def actions_only():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPO
            and os.environ.get("GITHUB_RUN_ATTEMPT") == "1",
            "every new exact saved-ball consequence runs once in public Actions")


def decimal_outward(value, direction, digits=60):
    require(direction in (-1, 1), "a directed decimal endpoint")
    scale = 10**digits
    numerator = value.numerator*scale
    integer = numerator//value.denominator
    if direction > 0 and integer*value.denominator != numerator:
        integer += 1
    sign = "-" if integer < 0 else ""
    whole, fractional = divmod(abs(integer), scale)
    return sign+str(whole)+"."+str(fractional).zfill(digits)


def admit_parent_bytes(raw_manifest, raw_actual, raw_execution, raw_worker,
                       worker_filename, published_actual_path, count):
    """Only whole-file identity and original validation; no new arithmetic."""
    contract = PARENTS[count]
    require(sha(raw_manifest) == contract["manifest_sha256"], "the one whole original immutable parent manifest")
    manifest, actual, execution = map(parse, (raw_manifest, raw_actual, raw_execution))
    by_role = {item["role"]: item for item in manifest["files"]+manifest["historical_inputs"]}
    worker_spec = by_role[contract["validator_role"]]
    require(len(raw_worker) == worker_spec["bytes"] and sha(raw_worker) == worker_spec["sha256"],
            "the entire original parent validator source")
    space = {"__name__": "_whole_saved_parent_validator_source_"+str(count), "__file__": worker_filename}
    exec(compile(raw_worker, worker_filename, "exec"), space)
    run, attempt = execution["run_id"], execution["run_attempt"]
    require(attempt == "1", "the original unique actual attempt")
    validation = {"require": require, "parse": parse, "manifest": manifest, "by_role": by_role,
        "op": manifest["operation"], "args": types.SimpleNamespace(manifest_sha=sha(raw_manifest)),
        "run": run, "attempt": attempt}
    exec(compile(textwrap.dedent(space["VALIDATOR"]), "_entire_saved_parent_validator", "exec"), validation)
    require(validation["validate_output"](raw_actual) == actual
            and actual["identity"]["kind"] == contract["kind"]
            and actual["complete"] is actual["proved"] is True and actual["actual_returncode"] == 0
            and actual["failure"] is None and actual["saved_record_count"] == count
            and execution["complete"] is True and execution["failure"] is None
            and execution["actual_child_returncode"] == 0 and execution["child_timeout"] is False
            and execution["manifest_sha256"] == sha(raw_manifest)
            and execution["completed_new_scalar_targets"] == count
            and execution["original_scientific_complete"] is True
            and execution["original_scientific_failure"] is None
            and execution["old_completed_targets_recomputed"] == actual["old_scientific_target_calls"] == 0,
            "the entire actually completed parent result and execution")
    require([item for item in execution["scientific_files"] if item["path"] == published_actual_path] == [
        {"path": published_actual_path, "bytes": len(raw_actual), "sha256": sha(raw_actual)}],
        "the original successful execution saved this exact entire actual")
    return manifest, actual, {"run_id": run, "run_attempt": attempt,
        "manifest_sha256": sha(raw_manifest), "actual_sha256": sha(raw_actual),
        "execution_sha256": sha(raw_execution), "all_original_targets_admitted": count}


def read_complete_parent(root, manifest_path, actual_path, execution_path, count):
    raw_manifest, raw_actual, raw_execution = [Path(path).read_bytes() for path in
                                               (manifest_path, actual_path, execution_path)]
    manifest = parse(raw_manifest)
    by_role = {item["role"]: item for item in manifest["files"]+manifest["historical_inputs"]}
    worker_spec = by_role[PARENTS[count]["validator_role"]]
    worker_path = Path(root)/worker_spec["path"]
    raw_worker = worker_path.read_bytes()
    relative = str(Path(actual_path).resolve().relative_to(Path(root).resolve()))
    return admit_parent_bytes(raw_manifest, raw_actual, raw_execution, raw_worker, str(worker_path), relative, count)


def consume(root, wmt_manifest, wmt_actual, wmt_execution, bfp_manifest, bfp_actual, bfp_execution):
    wm, w, wr = read_complete_parent(root, wmt_manifest, wmt_actual, wmt_execution, 14)
    bm, b, br = read_complete_parent(root, bfp_manifest, bfp_actual, bfp_execution, 19)
    return consume_admitted(wm, w, wr, bm, b, br)


def admit_relationship(wm, w, bm, b):
    require(w["identity"]["kind"] == "R149_complete_weighted_model_Theta_receiver_v1"
            and b["identity"]["kind"] == "R147_complete_full_target_nu_forward_v1"
            and w["identity"]["whole_UACT_actual_sha256"] == b["identity"]["whole_UACT_actual_sha256"],
            "both complete parents use the same original global Theta certificate")
    wc, bc = w["copied_complete_input_records"], b["copied_complete_input_records"]
    require(wc["original_global_Theta_error"] == bc["global_Theta_error"]
            and wc["model_rounding"] == bc["model_rounding"],
            "the same whole original global error and model rounding slots")


def consume_admitted(wm, w, wr, bm, b, br):
    actions_only()
    admit_relationship(wm, w, bm, b)
    bc = b["copied_complete_input_records"]
    global_candidates = {"original_UACT_global": bc["global_Theta_error"],
        "new_WMT_global": w["new_records"][wm["target_order"][13]]}
    chosen = min(global_candidates, key=lambda key: upper(global_candidates[key]))
    r, targets = b["new_records"], bm["target_order"]
    norm_trial, error_target = upper(r[targets[15]]), upper(r[targets[13]])
    model_preimage, norm_x, pair_error = upper(r[targets[14]]), upper(r[targets[2]]), upper(r[targets[16]])
    VQ, model = upper(bc["VQ_error"]), upper(bc["model_rounding"])
    error = ((norm_trial+upper(global_candidates[chosen]))*error_target
             +VQ*model_preimage+model*norm_x+pair_error)
    old_signed = r[targets[18]]
    centers = old_signed["all96_exact_signed_centers"]
    require(len(centers) == 96 and old_signed["rows"] == 96
            and old_signed["original_full_Theta_error_used"] is True
            and old_signed["low96_Theta_error_substituted"] is False,
            "all96 exact original signed centers and the whole high-frequency scope")
    require(all(isinstance(center, str) and str(Fraction(center)) == center for center in centers),
            "all96 saved exact rational centers, not their printed symmetric balls")
    return {"kind": "R147_complete_WMT_BFP_true_Theta_nu_saved_consequence_v1",
        "complete": True, "proved": True, "parent_receipts": {"WMT14": wr, "BFP19": br},
        "new_target": TARGET, "new_joint_error_upper": {"exact_rational": str(error),
            "outward_decimal_upper": decimal_outward(error, 1)},
        "complete_global_choice": {"selected": chosen, "both_complete_candidates": global_candidates},
        "all_complete_original_BFP_scalar_and_signed_records": r,
        "new_signed_conclusion": {"rows": 96,
            "all_exact_centers_inherited_verbatim_from": "all_complete_original_BFP_scalar_and_signed_records/"+targets[18]+"/all96_exact_signed_centers",
            "whole_center_array_sha256": sha(encode(centers)),
            "joint_l2_error_upper": {"exact_rational": str(error), "outward_decimal_upper": decimal_outward(error, 1)},
            "each_real_coordinate_enclosed_by_its_exact_center_plus_minus_joint_error": True},
        "prior_two_independent_density_means": old_signed["prior_two_independent_density_means"],
        "same_true_target_phase_retained": True, "whole_original_global_errors_retained": True,
        "old_scientific_targets_recomputed": 0, "changed_global_slot_only": True,
        "low96_error_used_globally": False, "full_physical_Schur_proved": False,
        "topic_completion_proved": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    for prefix in ("wmt", "bfp"):
        for suffix in ("manifest", "actual", "execution"):
            parser.add_argument("--"+prefix+"-"+suffix, type=Path, required=True)
    args = parser.parse_args()
    result = consume(args.root, args.wmt_manifest, args.wmt_actual, args.wmt_execution,
                     args.bfp_manifest, args.bfp_actual, args.bfp_execution)
    raw = encode(result)
    require(len(raw) < 100000, "the complete saved consequence respects the per-file size rule")
    print(raw.decode(), end="")


if __name__ == "__main__":
    main()
