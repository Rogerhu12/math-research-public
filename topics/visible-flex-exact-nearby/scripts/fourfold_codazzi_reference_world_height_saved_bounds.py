"""WRC: new exact combinations for complete reference-world mean height.

Only already completed bounds occur.  These14 comparisons were evaluated
once when WRC was derived; this file records their reproducible formulas.
No old geometry, phase, residual, Fourier or RHI target is called.
"""
from __future__ import annotations
from fractions import Fraction as F
import json


def saved_bounds():
    b, rc, R = F(9,50), F(2333968743003,10**13), F(1,200)
    e, d = F(2,10**9), F(1,10**10)
    eQ, eF = F("0.000108594777739"), F("0.000232681812735")
    BM = F("15.736315")*e + F("0.304809")*d
    BF = F("30.196406")*e + F("0.105999")*d
    C0, C1 = F(19,5), F(25,2)
    relative_phi = (1152+36*b)*BM
    position_phi = ((1152+24*b)*BM*C0*b + BM*C1*b
                    + (1152+12*b)*BF)
    qb_phi = F("0.03181")+12*b
    W0 = F(27,8)
    W1 = F(11,2)/F(16,15)+W0*qb_phi
    W1_safe = F("12.554")
    C_test = 26*W0 + F(5,2)*(C0*b+1)*W1_safe
    C, ct = F(141), F(5,4)*F("0.05282")
    U, NI, Jin, q0 = F("173.872"), F("11.272695"), F("1.060693"), F(2669,5000)
    KD = U*NI/q0*(C*b+ct)
    KF = KD*F("0.070711")
    KS = U*Jin/q0*(C*b*F("0.337")+ct*F("0.484"))
    KJ = U*Jin/q0*(C*b+ct)
    comparisons = [
        ("reference_waist_height",eF+BF,F("0.000232743")),
        ("raw_vertical_covector_Landau_squared",2*eQ*F("4.646383"),F("0.03177")**2),
        ("raw_vertical_position_Landau_squared",2*eF*F("5.970523"),F("0.05272")**2),
        ("selected_vertical_covector_first_derivative",F("0.03177")+relative_phi,F("0.03181")),
        ("selected_vertical_position_first_derivative",F("0.05272")+position_phi,F("0.05282")),
        ("whole_weighted_position_test_first_derivative",W1,W1_safe),
        ("whole_weighted_position_H1_dual",C_test,C),
        ("root_length_square_bound",R,F("0.070711")**2),
        ("strict_Fubini_length_square_bound",rc-2*b/3,F("0.337")**2),
        ("strict_trace_length_square_bound",rc,F("0.484")**2),
        ("complete_reference_height_root_data_receiver",KD,F(94000)),
        ("complete_reference_height_root_source_receiver",KF,F(6650)),
        ("complete_reference_height_strict_source_receiver",KS,F(3000)),
        ("complete_reference_height_strict_jump_receiver",KJ,F(8850)),
    ]
    records = [{"name":name,"left":str(left),"right":str(right),
                "strict":left<right} for name,left,right in comparisons]
    if not all(value["strict"] for value in records):
        raise ValueError("one new WRC saved-bound combination failed")
    return {
        "kind":"WRC_complete_reference_world_height_saved_bounds_v1",
        "new_exact_rational_comparisons":len(records),"comparisons":records,
        "whole_connection_difference_integral":str(BM),
        "whole_position_and_direct_velocity_majorant":str(BF),
        "reference_waist_vertical_position_upper":"232743/1000000000",
        "reference_waist_vertical_covector_error":"108627/1000000000",
        "reference_waist_vertical_covector_first_derivative":"3181/100000",
        "reference_waist_vertical_position_first_derivative":"2641/50000",
        "reference_outer_covector_first_derivative":str(qb_phi),
        "complete_weighted_position_H1_dual_upper":"141",
        "complete_coordinate_endpoint_coefficient":str(ct),
        "complete_original_negative_receiver":{
            "true_root_state_and_root_jumps":"94000",
            "root_L2_dr_Hminus2thirds_Hminus1_source":"6650",
            "strict_L2_dr_Hminus1_pair_source":"3000",
            "strict_unweighted_jumps":"8850"},
        "all_Fourier_modes_and_both_means_retained":True,
        "actual_anchors_equal_reference_asserted":False,
        "old_scientific_target_calls":0,
        "RHI_or_TC_completion_asserted":False,
        "full_world_height_or_Schur_proved":False}


def full_reference_column_errors(*, upper, EA, EY, EJ, EG,
                                 Y2, G2, C2):
    """Combine entire admitted RHI/ASB balls with the new whole C2 norm."""
    EW = upper(F(27,8)*EY + EJ*Y2)
    UW = upper(C2+EW)
    ET = upper(EW+EA*C2)
    Gstar = upper(G2+EG)
    radius = upper(ET+F(108627,10**9)*UW+F(232743,10**9)*Gstar)
    return {
        "position_L2_error_upper":EW,
        "true_weighted_position_L2_upper":UW,
        "canonical_position_mean_error_upper":ET,
        "true_physical_J_variation_L2_upper":Gstar,
        "complete_reference_mean_height_radius_upper":radius,
        "independent_actual_frame_error_coefficient":upper(UW+F(171,250)*Gstar),
        "independent_actual_position_error_coefficient":Gstar}


if __name__ == "__main__":
    print(json.dumps(saved_bounds(),sort_keys=True,indent=2))
