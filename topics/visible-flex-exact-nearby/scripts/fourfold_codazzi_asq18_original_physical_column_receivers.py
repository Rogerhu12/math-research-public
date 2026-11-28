"""Use the proved ASQ18 slots on the complete original BFP and DCP signed columns."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess


TOPIC = "topics/visible-flex-exact-nearby"
N = TOPIC + "/notes/"
W = ".github/workflows/visible-exact-asq18-signed-physical-column-receivers.yml"
SOURCE = TOPIC + "/scripts/fourfold_codazzi_asq18_original_physical_column_receivers.py"
PROOF = TOPIC + "/results/R149-supplement-actual-signed-Theta-trial-and-finite-inverse-by-primitive-residual.md"
PROOF_SHA = "82d2beb80d2023c0747c6c0927f0c98dd3fcebcb9376333496e05e55b38ce0f4"
RULES = N + "2026-11-28-read-public-model-ultra-rules.json"
RULE_SHA = "32fa03fbdb357d7d5a98b7115a24acc10f218705a1ecdef2e756ff73284098ce"
GLOBAL_ERROR = Fraction(13, 50)
FINITE_ERROR = Fraction(1, 40)
FINITE_INVERSE = Fraction(1347, 500)
GROUPS = {
    "UACT": ("45933303391", 21, "2026-11-27-unit-disk-operator-Theta-low-square-inputs.json",
             "unit_disk_operator_Theta_low_square_ci", "actual-unit-disk-operator-Theta-low-square.json",
             "80dbfdf33a39c180159f930a288813ef16fabe04e61c81f175154f012b99dcee",
             "17c721993bb6488ec48918c50caf70c84785ca54cb004fbc51d11de1c6eb14bc",
             "de2b9e0f2a1f424cd4c644ab23839bf715590e4153058517e66706a3d79b768c"),
    "WMA": ("46122573619", 14, "2026-11-28-weighted-model-Theta-receiver-inputs.json",
            "weighted_model_Theta_receiver_ci", "actual-weighted-model-Theta-receiver.json",
            "4913fe4ce57cd579741b65090cd5e6dae22392956545196c888c3061b8974ffb",
            "587ec4c28e521c8b04a85d42fad02bd5a53b4468ac9fdf217206ef40f231e3ae",
            "1b022e585f9fc30968a3aaaa8167229891ba02e15e8ece1ea010fe317c856cdc"),
    "BFP": ("46118996598", 19, "2026-11-28-full-target-nu-forward-inputs.json",
            "full_target_nu_forward_ci", "actual-full-target-nu-forward.json",
            "363c2116c8459e202209503bc40e379f40d502c89c92c3982971112f602e23ce",
            "5ab3a6ed22e4f40b47777f0bdbdfef50f5e52f50f211ef889ebb3ecc406dac16",
            "0bcb393bb071503c23ee4ebb6d38a28ef40a64b61afaafde19dbad5b2fed6c38"),
    "DCP": ("46124617641", 18, "2026-11-28-particular-density-Theta-inputs.json",
            "particular_density_Theta_ci", "actual-particular-density-Theta.json",
            "d85c0d55f82e50d9f061756a4d132db6780992654f3c01fbf5ae9a03657c44df",
            "2f90550a3c44e3b2a6c434179992dec191da149d08cfdc7876d379d4522c5e5b",
            "5ceba0c5540deb7d010377ed4fc8d591a8f53bb53080cab549d5538a8d107335"),
    "WBN": ("46125286420", 1, "2026-11-28-saved-WBN-column-inputs.json",
            "saved_WBN_column_ci", "actual-saved-column-consequence.json",
            "696a280cc634b2ecf94cb1a3d2af90fc676024e9327dfc245f89e15fff4f9ab2",
            "1f972ee941633f7052454035596536aee9fc843452fe2b4395fe2c183e3bbb52",
            "1cd75afa628a42e2a069d96e649e34a358792b12057888cf3c37b5eefeaf32d9"),
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def encode(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                       allow_nan=False) + "\n").encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def whole(root, path, expected):
    raw = (root / path).read_bytes()
    require(sha(raw) == expected, "whole original input " + path)
    return raw


def paths(spec):
    run, _, manifest, directory, actual = spec[:5]
    prefix = N + directory + "/run-" + run + "-1/"
    return N + manifest, prefix + actual, prefix + "execution.json"


def admitted(root):
    """Metadata only, including all predecessor receipts and complete original result sets."""
    proof = whole(root, PROOF, PROOF_SHA)
    require(len(proof) == 7319, "entire mathematical slot proof")
    actuals, receipts = {}, {}
    for label, spec in GROUPS.items():
        run, count = spec[:2]
        names = paths(spec)
        raw = [whole(root, path, digest) for path, digest in zip(names, spec[5:], strict=True)]
        m, a, e = map(json.loads, raw)
        order = m["target_order"]
        require(a["complete"] is a["proved"] is e["complete"] is True
                and a["failure"] is e["failure"] is a["current_target"] is None
                and a["actual_returncode"] == e["actual_child_returncode"] == 0
                and e["child_timeout"] is False and e["scientific_children"] == 1
                and e["complete_new_response_target_set"] is True
                and e["complete_old_input_admission_before_target_reservation"] is True
                and a["old_scientific_target_calls"] == e["old_completed_targets_recomputed"] == 0
                and e["run_id"] == a["identity"]["run_id"] == run
                and e["run_attempt"] == a["identity"]["run_attempt"] == "1"
                and a["identity"]["manifest_sha256"] == e["manifest_sha256"] == spec[5]
                and a["completed_targets"] == order and set(a["new_records"]) == set(order)
                and a["saved_record_count"] == e["completed_new_scalar_targets"] == len(order) == count
                and e["scientific_files"] == [{"path": names[1], "bytes": len(raw[1]), "sha256": spec[6]}],
                "one complete original execution and every signed/scalar record " + label)
        curr = m["files"]
        rc = e["current_input_receipts"]
        if isinstance(rc, list):
            require(rc == curr, "all original current-input descriptors " + label)
        else:
            require(rc == {"complete_count": len(curr), "complete_descriptors_sha256": sha(encode(curr)),
                           "manifest_sha256": spec[5], "reconstruct_from": "whole manifest.files"},
                    "full original current-input descriptor commitment " + label)
        hist = m["historical_inputs"]
        h = e["historical_restoration"]
        require(h["complete_receipts"] == [dict(x, whole_original_bytes_restored=True,
                    new_numerical_computation=False) for x in hist]
                and h["only_whole_completed_original_inputs_read"] is True
                and h["scientific_targets_recomputed"] == 0
                and h["original_native_files_restored"] == len(hist),
                "all prior historical receipts with original whole identities " + label)
        actuals[label] = a
        receipts[label] = {"run": run + "/1", "counts": [count, len(curr), len(hist)],
                           "current_descriptor_sha256": sha(encode(curr)),
                           "historical_receipt_sha256": sha(encode(h["complete_receipts"])),
                           "event": e["event_commit"], "checkout": e["actual_scientific_checkout"],
                           "whole_files": [{"path": n, "bytes": len(b), "sha256": sha(b)}
                                           for n, b in zip(names, raw, strict=True)]}
    b, d, w, n = (actuals[key] for key in ("BFP", "DCP", "WMA", "WBN"))
    b_rec = b["new_records"]
    dw = d["copied_complete_input_records"]
    wn = n["new_records"][n["completed_targets"][0]]
    bs, ds = b_rec[b["completed_targets"][18]], d["new_records"][d["completed_targets"][17]]
    require(d["whole_BFP_parent_identity"]["actual_sha256"] == GROUPS["BFP"][6]
            and d["whole_WMT_parent_identity"]["actual_sha256"] == GROUPS["WMA"][6]
            and b["identity"]["whole_UACT_actual_sha256"] == GROUPS["UACT"][6]
            and wn["all_complete_original_BFP_scalar_and_signed_records"] == b_rec
            and dw["complete_WMT14_new_records"] == w["new_records"]
            and dw["original_BFP_Theta_trial_norm"] == b_rec[b["completed_targets"][15]]
            and dw["original_BFP_full_target_error"] == ds["whole_BFP_target_column_error"]
                == b_rec[b["completed_targets"][13]]
            and ds["whole_global_Theta_error"] == w["new_records"][w["completed_targets"][13]]
            and bs["prior_two_independent_density_means"] == ds["prior_two_independent_density_means"]
                == wn["prior_two_independent_density_means"]
            and all(len(x["all96_exact_signed_centers"]) == x["rows"] == 96 for x in (bs, ds))
            and ds["same_complete_original_BFP512_reference"] is True
            and ds["true_infinite_high_modes_set_to_zero"] is False,
            "exact same original model, 512 reference, both distinct signed96 readouts and both physical means")
    return actuals, receipts


def upper(record):
    require(record["bound"] == "upper", "one saved complete upper")
    match = re.fullmatch(r"\[([^ ]+) \+/- ([^ ]+)\]", record["ball"])
    if match:
        mid, rad = map(Fraction, match.groups())
        require(rad >= 0 and mid >= rad, "one nonnegative original budget and its entire radius")
        return mid + rad
    value = Fraction(record["ball"])
    require(value >= 0, "one exact nonnegative budget")
    return value


def scientific(actuals):
    require(os.environ.get("GITHUB_ACTIONS") == "true" and os.environ.get("GITHUB_RUN_ATTEMPT") == "1"
            and os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"
            and os.environ.get("GITHUB_EVENT_NAME") == "push", "new numerical conclusions only in public Actions")
    b, d, u = (actuals[key] for key in ("BFP", "DCP", "UACT"))
    br, dr = ([doc["new_records"][key] for key in doc["completed_targets"]] for doc in (b, d))
    bc = b["copied_complete_input_records"]
    paid = (upper(br[15]) + GLOBAL_ERROR) * upper(br[13])
    # Each original coefficient product is retained in its own source/window.
    b_error = paid + upper(bc["VQ_error"]) * upper(br[14]) + upper(bc["model_rounding"]) * upper(br[2]) + upper(br[16])
    d_error = upper(dr[14]) + paid
    outputs = {}
    for name, signed, error in (("BFP", br[18], b_error), ("DCP", dr[17], d_error)):
        centers = signed["all96_exact_signed_centers"]
        require(all(str(Fraction(x)) == x for x in centers), "all96 original exact rational centers " + name)
        outputs[name] = {"all96_exact_signed_centers": centers, "whole_center_array_sha256": sha(encode(centers)),
                         "original_signed_record_sha256": sha(encode(signed)),
                         "joint_l2_upper_exact": str(error),
                         "prior_two_independent_density_means": signed["prior_two_independent_density_means"]}
    return {"separate_original_signed_receivers": outputs,
            "unchanged_positive_terms": {"whole_target_error": br[13], "trial_Theta_norm": br[15],
                "BFP_VQ_error": bc["VQ_error"], "BFP_model_preimage": br[14],
                "BFP_model_rounding": bc["model_rounding"], "BFP_reference_norm": br[2],
                "BFP_pairing": br[16], "DCP_finite_Theta_error": dr[14]},
            "slots": {"whole_target_Theta_error": str(GLOBAL_ERROR), "finite_Theta_error": str(FINITE_ERROR),
                      "finite_Theta_inverse": str(FINITE_INVERSE),
                      "original_trial_inverse_receipt": u["private_trial_inverse_receipt"],
                      "original_UACT_inverse_bound": u["complete_coordinate_inverse"]["complete_coordinate_inverse_two_upper"],
                      "ASQ18_proof_sha256": PROOF_SHA},
            "old_scientific_targets_recomputed": 0, "old_native_arrays_rematerialized": 0,
            "independent_physical_border_retained": True, "full_physical_Schur_proved": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--source-sha", required=True)
    args = parser.parse_args()
    root = args.repo.resolve()
    event = os.environ["GITHUB_SHA"]

    def git(*args):
        return subprocess.check_output(["git", *args], cwd=root)

    require(os.environ.get("GITHUB_ACTIONS") == "true" and os.environ.get("GITHUB_EVENT_NAME") == "push"
            and os.environ.get("GITHUB_RUN_ATTEMPT") == "1" and os.environ.get("GITHUB_REPOSITORY")
                == "Rogerhu12/math-research-public", "the original public first-add receiver entry")
    require(git("rev-parse", "HEAD").decode().strip() == event
            and git("diff-tree", "--no-commit-id", "--name-status", "-r", event, "--", W).decode().strip() == "A\t"+W
            and git("log", "--full-history", "--diff-filter=A", "--format=%H", event, "--", W).decode().splitlines() == [event]
            and sha(whole(root, SOURCE, args.source_sha)) == sha(git("show", event+":"+SOURCE)),
            "unique original workflow addition and complete source bytes at its actual event")
    rules = json.loads(whole(root, RULES, RULE_SHA))
    data, receipts = admitted(root)
    git("fetch", "--quiet", "--no-tags", "--filter=blob:none", "origin", "main")
    head = git("rev-parse", "origin/main").decode().strip()
    for path, expected in rules["readme_sha256"].items():
        require(sha(git("show", head+":"+path)) == expected, "all current reviewed rules "+path)
    require(not git("diff", rules["read_commit"], head, "--", *rules["readme_sha256"]), "both reviewed complete READMEs")
    result = scientific(data)
    result.update(kind="R149_ASQ18_signed_physical_column_receivers_v1", complete=True, proved=True,
                  run=os.environ["GITHUB_RUN_ID"], attempt="1", actual_event=event, reviewed_head=head,
                  source_sha256=args.source_sha, original_whole_parent_receipts=receipts)
    raw = encode(result)
    require(len(raw) < 75000, "small complete natural signed conclusion")
    print("ASQ18_SIGNED_PHYSICAL_COLUMN_CONCLUSION", len(raw), sha(raw), flush=True)
    print(raw.decode(), end="")


if __name__ == "__main__":
    main()
