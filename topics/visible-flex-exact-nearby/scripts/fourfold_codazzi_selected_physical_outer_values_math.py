"""Two actual physical outer residual values from complete saved certificates.

Definitions and standard-library rational metadata only at import. Directed
arithmetic belongs to the new public owner. Old endpoint/outer producers are
never imported. The height RHS is deliberately not a manufactured output.
"""
from fractions import Fraction

KIND = "complete_selected_member_physical_outer_residual_values_v1"
CANDIDATE = "ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
CENTRE = "440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
DIRECTION = "6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
RAW_SOURCE = "aa98cdd2289b13ac125a0bdb193faa9ae389b566d9a561c0b0e93208d29937f1"
REPAIR_SOURCE = "5d1e8a86aa268d4d98bc929264d706b418b88cb99518ca646d84258d3068ffbe"
FAMILY_SOURCE = "876bd34cf84eb481686461984f29c98420d3c75af6733363308ef97a8ee66667"
ENDPOINT_SOURCE = "0e8904d935d83596040fede599ca60cbe7acdf5aba5249c8ddaa4ec3167a976f"
REPAIR_NATIVE = "75e7c0e1447306a97971ee05dcb68b8d357cb4fffa5c1a37335a6fc29a473424"
FAMILY_NATIVE = "5ab1d1b85cb71556b051fd53f5579cb30260ebdda6a844df9a4b377508e057fc"
ENDPOINT_NATIVE = "8f6019cefaa96da64eadb3b19a98110dc81a0d5760a091e6fdffe538c971e606"
ALPHA = "6890507429876859/9007199254740992"
NU = "-2572625729470897/72057594037927936"
ETA = "-7789843107295549/4611686018427387904"
DELTA = "1/10000000000"
OLD_DELTA = "1/100000000"
SELECTED_UPPER = "0.00000000009368259853002"
MEAN_FLOOR = "29/5"
TARGETS = (
    "complete_selected_physical_Robin_Hminus5over6_upper",
    "complete_selected_independent_physical_mean_residual_upper",
)
RAW_GATES = (
    "exact_dyadic_endpoint", "whole_parameter_intrinsic_endpoint",
    "true_degree_one_physical_angle", "complete_analytic_alias",
    "all_unretained_physical_modes", "original_C_input_ball",
    "stated_smaller_C_input_ball", "true_q_proposal_error_paid",
    "complete_nonlinear_nonmean_port_paid", "true_C_mean_port_paid",
    "true_B_mean_exactly_zero", "independent_far_Dirichlet_preserved",
    "independent_mean_height_preserved",
)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def completed(document, count):
    gates = document.get("gates", [])
    return (document.get("complete") is True
            and document.get("failure") is None
            and len(gates) == count
            and all(g.get("passed") is True for g in gates))


def record_shape(record):
    require(isinstance(record, dict)
            and isinstance(record.get("ball"), str)
            and isinstance(record.get("lower"), str)
            and isinstance(record.get("upper"), str),
            "whole saved interval and both endpoint balls are required")


def admit_metadata(raw, repaired, family, endpoint, nif, wobsa):
    """Whole mathematical admission, without any scientific arithmetic.

    Byte/SHA/Git identities and the whole old process receipts must also be
    checked by the public owner. A copied summary is not admitted alone.
    """
    require(raw.get("kind") ==
            "actual_full_moving_candidate_complete_physical_R_boundary"
            and raw.get("complete") is True and raw.get("failure") is None
            and raw.get("source_sha256") == RAW_SOURCE
            and raw.get("candidate_sha256") == CANDIDATE
            and Fraction(raw["exact_amplitude"]) == Fraction(ALPHA)
            and Fraction(raw["exact_nu"]) == Fraction(NU)
            and Fraction(raw["exact_center_parameter"]) == Fraction(ETA)
            and Fraction(raw["parameter_half_width"]) == Fraction(1, 10**9)
            and raw.get("whole_affine_parameter_interval") is True
            and raw.get("whole_real_angular_circle") is True
            and raw.get("complete_original_intrinsic_tail") is True
            and raw.get("endpoint") == "25/8"
            and raw.get("finite_moving_modes") == 32
            and raw.get("physical_frequency_factor") == 4,
            "same whole raw physical endpoint certificate required")
    require(set(raw.get("gates", {})) == set(RAW_GATES)
            and all(raw["gates"][name] is True for name in RAW_GATES)
            and raw.get("full_nonlinear_physical_angle_used") is True
            and raw.get("no_finite_quadrature_exactness_assumed") is True
            and raw.get("all_physical_Fourier_modes_and_mean_retained") is True
            and len(raw.get("exact_normalized_endpoint_coefficients", [])) == 65
            and len(raw.get("rows", [])) == 128
            and Fraction(raw["strip"]) == Fraction(1, 8)
            and Fraction(raw["physical_output_width"]) == 0
            and Fraction(raw["local_long_ball_radius_chosen_before_run"]) ==
                Fraction(1, 10**12),
            "raw complete physical Fourier tail, mean, or fixed domain missing")
    for number, row in enumerate(raw["rows"], 1):
        require(row["index"] == number
                and row["physical_frequency"] == 4*number
                and row["retained_in_finite_BVP"] is (number <= 32),
                "a complete original physical row is absent or reordered")
    require(raw.get("full_far_regular_label_equation_solved") is False
            and raw.get("whole_body_PDE_certified") is False
            and raw.get("whole_body_inverse_certified") is False,
            "old incomplete scope was silently promoted")
    for document, source, native in (
            (repaired, REPAIR_SOURCE, REPAIR_NATIVE),
            (family, FAMILY_SOURCE, FAMILY_NATIVE)):
        require(completed(document, 25)
                and document.get("source_sha256") == source
                and document.get("native_sha256") == native
                and document.get("original_candidate_sha256") == CANDIDATE
                and document.get("derived_definition_sha256") == CENTRE
                and document.get("full_nonlinear_DN_Hs_derivative_proved") is True
                and document.get("full_Hone_sixth_Riccati_graph_proved") is True
                and document.get("independent_even_mean_and_all_head_and_affine_outer_columns_retained") is True
                and document.get("all_fourier_modes_including_infinite_physical_tail_retained") is True
                and document.get("no_original_endpoint_or_cap_matrix_or_target_recomputation") is True
                and document.get("complete_infinite_BVP_inverse_proved") is False,
                "same complete repaired and family outer graphs are required")
    require(Fraction(repaired["exact_affine_parameter_offset"]) == 0
            and family.get("explicit_direction_definition_sha256") == DIRECTION
            and Fraction(family["exact_real_delta_radius"]) == Fraction(OLD_DELTA)
            and family.get("full_family") == "Q_delta=Q0+delta*Z"
            and Fraction(family["fixed_intrinsic_affine_offset"]) == 0
            and family.get("full_real_delta_outer_graph_proved") is True
            and family.get("original_complete_endpoint_native_sha256") == ENDPOINT_NATIVE
            and family.get("original_complete_repaired_outer_native_sha256") == REPAIR_NATIVE,
            "whole same r-family or its original direction changed")
    require(endpoint.get("complete") is True and endpoint.get("failure") is None
            and endpoint.get("actual_returncode") == 0
            and str(endpoint.get("run_id")) == "43611611635"
            and str(endpoint.get("run_attempt")) == "1"
            and endpoint.get("mathematical_complete") is True
            and endpoint.get("mathematical_failure") is None
            and endpoint.get("mathematical_source_sha256") == ENDPOINT_SOURCE
            and endpoint.get("native_sha256") == ENDPOINT_NATIVE
            and endpoint.get("native_bytes") == 32287
            and endpoint.get("original_complete_outer_native_sha256") == REPAIR_NATIVE
            and endpoint.get("explicit_direction_definition_sha256") == DIRECTION
            and endpoint.get("complete_mean_retained") is True
            and endpoint.get("physical_direction_unscaled_by_alpha") is True
            and len(endpoint.get("mathematical_gates", [])) == 14
            and all(g.get("passed") is True for g in endpoint["mathematical_gates"]),
            "whole exact physical193 endpoint process is required")
    require(endpoint.get("original_response_solves_recomputed") == 0
            and endpoint.get("original_target_calls") == 0
            and endpoint.get("original_endpoint_certificates_recomputed") == 0,
            "unexpected old numerical retry in the endpoint receipt")
    diagnostics = endpoint["complete_parameter_radius_diagnostics"]
    require({Fraction(row["exact_parameter_radius"]) for row in diagnostics} ==
            {Fraction(DELTA), Fraction(OLD_DELTA)},
            "both original endpoint parameter radii must remain present")
    require(completed(nif, 16)
            and nif.get("actual_returncode") == 0 and nif.get("proved") is True
            and Fraction(nif["parameters"]["exact_intrinsic_parameter"]) == Fraction(ETA)
            and Fraction(nif["parameters"]["exact_real_delta_radius"]) == Fraction(OLD_DELTA)
            and Fraction(nif["parameters"]["fixed_selected_parameter_absolute_upper"]) ==
                Fraction(SELECTED_UPPER)
            and Fraction(SELECTED_UPPER) < Fraction(DELTA) < Fraction(OLD_DELTA)
            and nif["parameters"]["uniform_selected_conjugacy_family_claimed"] is False,
            "the original selected implicit member must be retained")
    require(completed(wobsa, 18) and wobsa.get("actual_returncode") == 0
            and wobsa["parameters"]["same_selected_member_only"] is True
            and Fraction(wobsa["parameters"]["exact_real_delta_radius"]) == Fraction(OLD_DELTA)
            and wobsa["retained_scope"]["same_selected_member_same_physical_eta0"] is True,
            "same-member WOBSA qualification cannot be replaced by a family")
    rb, cb, fb = raw["bounds"], repaired["bounds"], family["bounds"]
    require(fb["additional_full_physical_C_change_Aone_sixtyfourth"] ==
            fb["actual_fixed_physical_C_change_Aone_sixtyfourth"],
            "original same-homotopy C difference record changed")
    records = {
        "raw_Robin": rb["smaller_ball_complete_nonlinear_Robin_residual"],
        "raw_physical_mean": rb["smaller_ball_complete_mean_C_residual"],
        "raw_U": rb["u_real_A0_upper"],
        "raw_V": rb["v_nonmean_real_A0_upper"],
        "raw_Usigma": rb["u_full_finite_strip_A0_upper"],
        "raw_Vsigma": rb["v_nonmean_full_finite_strip_A0_upper"],
        "raw_mean_lower": rb["actual_mean_absolute_lower"],
        "raw_Z": rb["full_physical_C_nonmean_A0"],
        "repair_Eu": cb["right_eu_Aone_eighth"],
        "repair_Ev": cb["right_ev_nonmean_Aone_eighth"],
        "repair_Em": cb["right_mean_change"],
        "repair_DC": cb["actual_fixed_physical_C_change_Aone_sixtyfourth"],
        "direction_Zu": endpoint["norms"]["0"]["0"]["u"],
        "direction_Zv": endpoint["norms"]["0"]["0"]["v_nonmean"],
        "family_mean_lower": fb["corrected_endpoint_mean_absolute_lower"],
        "family_Z": fb["corrected_outer_physical_Z_A0"],
        "family_DC": fb["additional_full_physical_C_change_Aone_sixtyfourth"],
        "DN_Z_to_d_L2": family["actual_DN"]["Z_to_d_L2"],
        "DN_Z_to_mean": family["actual_DN"]["Z_to_mean"],
    }
    for record in records.values():
        record_shape(record)
    mean = Fraction(endpoint["exact_independent_mean"])
    require(len(records) == 19 and mean != 0,
            "all nineteen whole saved bounds and the nonzero direction mean are required")
    return {
        "records": records,
        "exact_direction_mean": str(mean),
        "raw_far_height_radius": raw["local_long_ball"]["independent_far_Dirichlet_radius"],
        "metadata": {
            "exact_new_delta_radius": DELTA,
            "old_complete_delta_radius": OLD_DELTA,
            "same_homotopy_C_difference_scale": "1/100",
            "old_interval_records": 19,
            "raw_complete_physical_rows": 128,
            "raw_gates": 13, "repaired_outer_gates": 25,
            "family_outer_gates": 25, "exact_direction_endpoint_gates": 14,
            "selected_NIF_gates": 16, "selected_WOBSA_gates": 18,
            "exact_direction_mean": str(mean),
            "height_background_radius": "1/1152921504606846976",
            "height_rhs_supplied": False,
        },
    }


def complete_bounds(api, admitted, emit, progress=None):
    """Evaluate O.3--12 and save exactly the two declared principal outputs.

    API: rational, old_interval, lower, upper. emit must atomically save and
    read back a containing complete ball, then return its directed upper.
    progress saves a named stage and whole directed intermediate enclosures;
    those are audit budgets, never fabricated old/future target results.
    """
    q, up, low = api.rational, api.upper, api.lower
    zero, one, mstar = q("0"), q("1"), q(MEAN_FLOOR)
    records = admitted["records"]

    def upper_old(key):
        value = up(api.old_interval(records[key]))
        require(value >= zero, "nonnegative saved bound is unresolved: "+key)
        return value

    for key in records:
        upper_old(key)
    require(low(api.old_interval(records["raw_mean_lower"])) > mstar
            and low(api.old_interval(records["family_mean_lower"])) > mstar,
            "the complete original and family mean lower bounds do not exceed29/5")
    radius = q("1/1000000000000")
    require(upper_old("raw_Z") < radius and upper_old("family_Z") < radius,
            "the whole straight physical Z segment is not inside the same small ball")
    require(api.old_interval(admitted["raw_far_height_radius"]).contains(q("1/1152921504606846976")),
            "original same independent background fB radius differs")
    d = q(DELTA)
    eu = up(upper_old("repair_Eu")+d*upper_old("direction_Zu"))
    ev = up(upper_old("repair_Ev")+d*upper_old("direction_Zv"))
    em = up(upper_old("repair_Em")+d*q(str(abs(Fraction(admitted["exact_direction_mean"])))))
    if progress is not None:
        progress("complete_moving_increment", {
            "E_u": eu, "E_v_nonmean": ev, "E_mean": em,
        })
    u, v = upper_old("raw_U"), upper_old("raw_V")
    us, vs = upper_old("raw_Usigma"), upper_old("raw_Vsigma")
    gap = low(mstar-v-ev)
    orientation = low(one-v/mstar)
    require(gap > zero and orientation > zero,
            "whole real inverse angle or actual v gap is not strictly positive")
    dtheta = up((ev+em*v/mstar)/(4*mstar))
    dphi = up(dtheta/orientation)
    if progress is not None:
        progress("complete_same_physical_angle", {
            "v_gap_lower": gap, "raw_angle_derivative_lower": orientation,
            "whole_angle_change_upper": dtheta,
            "whole_inverse_angle_change_upper": dphi,
        })
    db = up(eu/gap+u*(ev+em)/(gap*gap)
            +(8*us/gap+8*u*vs/(gap*gap))*dphi)
    dc = up(upper_old("repair_DC")+q("1/100")*upper_old("family_DC"))
    dmean = up(em/(mstar*mstar))
    if progress is not None:
        progress("complete_fixed_theta_state_difference", {
            "physical_B_Linfinity_difference_upper": db,
            "physical_C_Aone_sixtyfourth_difference_upper": dc,
            "physical_reciprocal_mean_difference_upper": dmean,
        })
    rb = up(upper_old("raw_Robin")+db+(one+upper_old("DN_Z_to_d_L2"))*dc)
    saved_rb = emit(TARGETS[0], rb)
    require(saved_rb >= rb, "saved Robin upper does not contain its original bound")
    rc = up(upper_old("raw_physical_mean")+dmean+upper_old("DN_Z_to_mean")*dc)
    saved_rc = emit(TARGETS[1], rc)
    require(saved_rc >= rc, "saved physical mean upper does not contain its original bound")
    return {
        "complete": True,
        "completed_target_count": 2,
        "same_selected_member_by_uniform_delta10_restriction": True,
        "same_fixed_physical_theta_and_complete_Fourier_tail": True,
        "same_background_fB_within_original_permitted_ball": True,
        "independent_physical_mean_is_reciprocal_moving_mean": True,
        "Robin_output_norm": "normalized physical-circle H^-5/6",
        "mean_output_norm": "absolute physical scalar",
        "raw_physical_amplitude_not_applied_again": True,
        "endpoint_Theta_weight_not_applied_to_physical_sources": True,
        "height_actual_rhs_value_proved": False,
        "far_regular_label_or_height_gauge_equation_proved": False,
        "actual_nu_response_boundary_discrepancy_of_Z_proved": False,
        "negative_germ_interface_and_root_inputs_proved": False,
        "both_complete_WPN_rhs_proved": False,
        "complete_infinite_inverse_proved": False,
        "nonlinear_solution_proved": False,
    }
