"""Whole actual BGR3+BNC7 to the same true96 target-coordinate column.

The only replacement is the complete joint inverse-row fee. All four
other original fees, exact96 centers, and both physical means are copied.
This object is E96^{a*} B^{-1} Fnu, not the different Theta-nu column.
"""
from __future__ import annotations
import argparse
import importlib.util
from fractions import Fraction
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
HELPER = TOPIC+"/scripts/fourfold_codazzi_weighted_Theta_nu_saved_consumer.py"
TARGETS = ["complete_Gram_refined_Bnu_row_fee_upper",
           "complete_Gram_refined_Bnu_joint_error_upper"]


def admit_relationship(core, gm, g, bm, b):
    require = core.require
    gs = {item["role"]: item for item in gm["files"]+gm["historical_inputs"]}
    for name in ("manifest", "actual", "execution"):
        require(gs["BNC_DW_"+name]["sha256"] == b["identity"]["whole_parent_identities"]["DW"][name],
                "both successful parents use the identical complete original DWTB9")
    old, copied = g["copied_complete_DWTB_records"], b["copied_prior_scalar_records"]
    require(old["complete_target_B_inverse96_joint_L2_row_error_upper"] == copied["eR"]
            and old["complete_I_trial_Hilbert_Schmidt_upper"] == copied["J"]
            and g["row_restoration"] == b["necessary_B_row_carrier_receipt"],
            "the same full96 row trial, true target phase and complete old error records")
    require(gm["target_order"][-1] == "complete_DWTB_inverse96_Gram_row_error_upper"
            and bm["target_order"][:5] == [
                "complete_target_B_row_error_on_NP_trial_upper",
                "complete_target_B_receiver_on_NP_PDE_error_upper",
                "complete_target_B_trial_compound_error_upper",
                "complete_target_B_trial_quadrature_alias_upper",
                "complete_target_B_trial_quadrature_rounding_upper"],
            "the whole original five-component order remains exact")


def consume_admitted(core, gm, g, gr, bm, b, br, save_row_fee=None):
    core.actions_only()
    admit_relationship(core, gm, g, bm, b)
    require, up = core.require, core.upper
    bt = bm["target_order"]
    copied, prior = b["copied_prior_scalar_records"], b["new_records"]
    lo, BH = core.exact_interval(copied["BH"]["ball"])
    require(lo > 0, "the entire original positive nonunitary density receiver ball")
    row = g["new_records"][gm["target_order"][2]]
    new_fee = up(row)*BH*up(copied["N0"])

    def exact_upper(value):
        return {"exact_rational": str(value), "outward_decimal_upper": core.decimal_outward(value, 1)}

    if save_row_fee is not None:
        saved = save_row_fee(TARGETS[0], exact_upper(new_fee))
        require(saved == exact_upper(new_fee), "the entire new exact row fee saved and read before the joint formula")
        new_fee = Fraction(saved["exact_rational"])
    # This is a new positive formula with one new whole BGR component.
    # The old complete sum is copied, never reconstructed or subtracted.
    other_four = {name: prior[name] for name in bt[1:5]}
    new_error = new_fee+sum((up(record) for record in other_four.values()), Fraction(0))

    old_error = up(prior[bt[5]])
    selected = "new_complete_Gram_candidate" if new_error < old_error else "original_complete_BNC_candidate"
    error = new_error if selected == "new_complete_Gram_candidate" else old_error
    signed = prior[bt[6]]
    centers = signed["all96_exact_signed_trial_rationals"]
    require(signed["rows"] == len(centers) == 96
            and all(isinstance(value, str) and str(Fraction(value)) == value for value in centers)
            and signed["physical_mean_slots_eliminated"] is False
            and signed["true_full_physical_high_forcing_retained"] is True
            and signed["whole_physical_column_used"] is True
            and signed["original_target_normalizer_and_true_phase_retained"] is True,
            "all96 exact signed centers and the whole true physical source, without zero-ball centers")
    return {
        "kind": "R147_complete_BGR_BNC_true_target_nu_saved_consequence_v1",
        "complete": True, "proved": True, "parent_receipts": {"BGR3": gr, "BNC7": br},
        "new_targets": TARGETS,
        "new_records": {TARGETS[0]: exact_upper(new_fee), TARGETS[1]: exact_upper(new_error)},
        "complete_joint_choice": {"selected": selected,
            "both_complete_candidates": {"new_complete_Gram_candidate": exact_upper(new_error),
                "original_complete_BNC_candidate": prior[bt[5]]}},
        "all_complete_original_BNC_scalar_and_signed_records": prior,
        "all_complete_new_BGR_records": g["new_records"],
        "all_four_unchanged_original_fees": other_four,
        "whole_original_density_receiver": copied["BH"],
        "whole_original_NP_source_L2": copied["N0"],
        "same_complete_original_row_carrier": b["necessary_B_row_carrier_receipt"],
        "new_signed_conclusion": {"rows": 96,
            "all_exact_centers_inherited_verbatim_from": "all_complete_original_BNC_scalar_and_signed_records/"+bt[6]+"/all96_exact_signed_trial_rationals",
            "whole_center_array_sha256": core.sha(core.encode(centers)),
            "joint_l2_error_upper": exact_upper(error),
            "each_real_coordinate_enclosed_by_its_exact_center_plus_minus_joint_error": True},
        "prior_two_independent_density_means": signed["prior_two_independent_density_mean_balls"],
        "whole_five_fee_positive_formula_preserved": True,
        "old_successful_targets_recomputed": 0, "old_upper_subtracted": False,
        "different_Theta_nu_column_claimed": False,
        "true_infinite_high_modes_set_to_zero": False,
        "nonlocal_phase_or_mean_height_column_claimed": False,
        "full_physical_Schur_proved": False, "topic_completion_proved": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    for prefix in ("bgr", "bnc"):
        for suffix in ("manifest", "actual", "execution"):
            parser.add_argument("--"+prefix+"-"+suffix, type=Path, required=True)
    args = parser.parse_args()
    path = args.root/HELPER
    spec = importlib.util.spec_from_file_location("_BGR_BNC_complete_saved_helper", path)
    core = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(core)
    gm, g, gr = core.read_complete_parent(args.root, args.bgr_manifest, args.bgr_actual, args.bgr_execution, 3)
    bm, b, br = core.read_complete_parent(args.root, args.bnc_manifest, args.bnc_actual, args.bnc_execution, 7)
    raw = core.encode(consume_admitted(core, gm, g, gr, bm, b, br))
    core.require(len(raw) < 100000, "the entire new consequence respects the per-file size rule")
    print(raw.decode(), end="")


if __name__ == "__main__":
    main()
