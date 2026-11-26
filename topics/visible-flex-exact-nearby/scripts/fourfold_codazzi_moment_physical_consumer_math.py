"""R141 B4--B21 with explicit completed R142 low admission and weighted high inputs.

Pure definitions. No import-time numerical work, IO, old target, or fallback.
A future public owner pins every complete input and supplies emit(name,
value,bound), which saves a whole containing ball and returns its reread
upper/lower endpoint. Every new strict gate below uses those saved endpoints.
"""

LOW_KIND = "complete_R141_low193_directed_Green_certificate_v1"
MOMENT_LOW_KIND = "complete_R142_low193_parent_moment_continuation_v1"
MOMENT_TARGETS = (
    "complete_parent_moment_true_hybrid_low_coefficient_defect",
    "complete_ordinary_raw_low_source_and193_atoms",
    "complete_transformed_low_source_and193_atoms",
    "complete_low_second_kind_inverse_and193_atoms",
    "complete_high0_return_source_without_CFB",
    "complete_actual_whole_interval_low_transversality",
)
COERCIVE_LOW_KIND = "complete_R149_low193_coercive_source_point_continuation_v1"
COERCIVE_TARGETS = MOMENT_TARGETS[1:]
COERCIVITY_KIND = "complete_R149_low193_signed_loop_coercivity_v1"
COERCIVITY_TARGET = "complete_same_weighted_body_signed_trace_and_symmetric_part"
WEIGHTED_KIND = "complete_actual_GH_radially_weighted_head_response_v1"
GH5_KIND = "complete_actual_GH_Hthird_source_fees_v1"
GH4_KIND = "complete_actual_GH_saved_Hthird_head_response_v1"
D_KIND = "complete_fixed_WVC_reference_boundary_lifts_v1"
REPAIR_SHA = "440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
DIRECTION_SHA = "6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
ORIGINAL_MODULE_ROLES = ("science", "readonly_admission", "readonly_core",
                         "collar_math", "kernel_math", "assembly_math", "reference_math")
ROLES = ("ordinary_raw_low_source", "transformed_low_source",
         "low_second_kind_correction", "centre_high0_return_source")
NEGATIVE_INPUTS = ["root_stable_Y_port", "collar_ordinary_Hminus2over3_source",
    "body_ordinary_Hminus2over3_source", "body_outer_mean_head_and_Y_weighted_jumps",
    "collar_Y_weighted_affine_jumps", "cut_stable_Y_jump", "cut_unstable_Y_jump"]


def require(ok, message):
    if not ok:
        raise ValueError(message)


def upper(api, value):
    require(value.is_finite(), "finite complete directed scalar")
    point = value.upper()
    require(api.lower(point) >= 0, "nonnegative mathematical upper endpoint")
    return point


def root(api, value):
    return upper(api, api.sqrt(upper(api, value)))


def hypot(api, *values):
    points = [upper(api, value) for value in values]
    return root(api, sum((value*value for value in points), api.zero))


def saved_upper(api, record):
    if isinstance(record, dict) and record.get("kind") == "complete_decimal_ball_v1":
        exponent = int(record["decimal_exponent"])
        scale = api.rational(10**exponent) if exponent >= 0 else api.rational(1, 10**(-exponent))
        midpoint = api.rational(int(record["midpoint_integer"]))*scale
        radius = api.rational(int(record["radius_integer"]))*scale
        require(api.lower(radius) >= 0, "whole original enclosing decimal radius")
        return upper(api, api.interval(midpoint-radius, midpoint+radius))
    return upper(api, api.old_interval(record))


def saved_lower(api, record):
    require(isinstance(record, dict) and record.get("kind") == "complete_decimal_ball_v1",
            "whole saved directed lower scalar")
    exponent = int(record["decimal_exponent"])
    scale = api.rational(10**exponent) if exponent >= 0 else api.rational(1, 10**(-exponent))
    midpoint = api.rational(int(record["midpoint_integer"]))*scale
    radius = api.rational(int(record["radius_integer"]))*scale
    require(api.lower(radius) >= 0, "nonnegative original saved scalar radius")
    point = api.interval(midpoint-radius, midpoint+radius).lower()
    require(point.is_finite(), "finite whole saved lower endpoint")
    return point


def admit_complete_inputs(api, low, low_execution, gh5, gh5_execution,
                          gh4, gh4_execution, D, D_execution, L, L_execution,
                          negative, weighted=None, weighted_execution=None):
    """Additional same-object scope checks after the owner's whole-byte admission.

    The owner also admits both original high summary/process reports with
    the unchanged metadata helper. No unsuccessful/early two-target R141
    result can enter this consumer. No projected-only L bound is admitted.
    """
    require(low["kind"] in (LOW_KIND, MOMENT_LOW_KIND, COERCIVE_LOW_KIND)
            and low["complete"] is True and low["proved"] is True
            and low["failure"] is None and low["actual_returncode"] == 0
            and low_execution["scientific_complete"] is True
            and low_execution["actual_child_returncode"] == 0
            and low["run_id"] == low_execution["run_id"]
            and low["run_attempt"] == low_execution["run_attempt"],
            "whole genuinely successful original or explicit moment low certificate")
    if low["kind"] == LOW_KIND:
        require(len(low["completed_targets"]) == 7,
                "all seven targets of the original directed certificate")
    elif low["kind"] == MOMENT_LOW_KIND:
        prior = low["completed_prior_directed_prefix"]
        continuation = low["certificate"]["moment_continuation"]
        require(tuple(low["completed_targets"]) == MOMENT_TARGETS
                and low["certificate_parameters"]["completed_directed_Green_prefix_run"] == "44730452579/1"
                and prior["kind"] == "whole_existing_Green_success_and_defect_failure_prefix_v1"
                and prior["completed_Green_target_registered_again"] is False
                and prior["old_unfinished_defect_treated_as_full_false_gate"] is False
                and prior["private_carriers_were_published_or_restored"] is False
                and prior["same_defined_carriers_necessarily_materialized_for_new_target"] is True
                and continuation["whole_cell_signed_two_triangle_moments"] is True
                and continuation["parent_actual_coefficient_enclosures_narrowed"] is False
                and continuation["five_source_roles_and_independent_even_mean_retained"] is True,
                "six genuine R142 targets plus the whole already certified same Green prefix")
    else:
        prior = low["completed_prior_coercivity"]
        defect = low["completed_prior_low_defect"]
        continuation = low["certificate"]["coercive_continuation"]
        require(tuple(low["completed_targets"]) == COERCIVE_TARGETS
                and prior["kind"] == "whole_completed_independent_R149_coercivity_success_v1"
                and prior["completed_targets"] == [COERCIVITY_TARGET]
                and prior["old_signed_trace_or_theta_target_recomputed"] is False
                and defect["kind"] == "whole_completed_R142_epsilon_false_branch_v1"
                and defect["old_HS_target_recomputed"] is False
                and defect["old_epsilon_false_gate_retained"] is True
                and continuation["independent_complete_R149_coercivity_consumed"] is True
                and continuation["original_R142_epsilon_false_gate_retained"] is True
                and continuation["old_Green_HS_atoms_trace_or_theta_target_recomputed"] is False
                and continuation["whole_four_source_roles_and193_atoms_required"] is True
                and continuation["point_receiver_uses_actual_defect_covariances"] is True,
                "independent completed coercivity plus exactly four source and one point targets")
    lc = low["certificate"]
    if low["kind"] == COERCIVE_LOW_KIND:
        require(lc["strict_low_coefficient_gate_passed"] is False
                and lc["strict_symmetric_part_gate_passed"] is True
                and lc["resolvent"]["basis"] == "symmetric_part_coercivity",
                "new explicit coercive low kind preserves the old false epsilon gate")
    else:
        require(lc["strict_low_coefficient_gate_passed"] is True,
                "unchanged original contraction admission for original low kinds")
    require(lc["actual_low_hybrid_inverse_proved"] is True
            and lc["actual_complete_CFB_centre_proved"] is False
            and lc["actual_positive_family_inverse_proved"] is False
            and lc["original_finite_rho_bridge_proved"] is False
            and lc["original_seven_input_ports_proved"] is False
            and lc["either_original_RHS_proved"] is False,
            "exact low object and all original unpaid qualifications")
    model = lc["model"]
    require(model["comparison_BVP_verified"] is True and model["original_panels"] == 155
            and model["left_carrier"] == 97 and model["right_carrier"] == 96
            and model["whole_atoms"] == 193 and model["same_true_panel_lengths_retained"] is True
            and lc["whole_interval_transversality"]["every_real_radius_covered"] is True
            and lc["whole_interval_transversality"]["raw_nodes_only_diagnostic_used_as_certificate"] is False
            and lc["whole_interval_transversality"]["full_CFB_included"] is False,
            "complete comparison model, both carriers, and true whole-interval observation certificate")
    require(gh5["kind"] == GH5_KIND and gh5["complete"] is True and gh5["proved"] is True
            and gh5["actual_returncode"] == 0 and gh5_execution["scientific_complete"] is True
            and gh5_execution["actual_child_returncode"] == 0
            and gh5["run_id"] == gh5_execution["run_id"] == "44736533396"
            and gh5["run_attempt"] == gh5_execution["run_attempt"] == "1"
            and gh5["saved_record_count"] == 5
            and gh5["source_comparison"]["complete_five_source_rates_proved"] is True,
            "whole actual five-source result, not displayed point values")
    require(gh4["identity"]["kind"] == GH4_KIND and gh4["complete"] is True and gh4["proved"] is True
            and gh4["actual_returncode"] == 0 and gh4_execution["complete"] is True
            and gh4_execution["actual_child_returncode"] == 0
            and gh4["identity"]["run_id"] == gh4_execution["run_id"] == "44740105701"
            and gh4["identity"]["run_attempt"] == gh4_execution["run_attempt"] == "1"
            and gh4["saved_record_count"] == 4
            and gh4["scope"]["actual_complete_head_to_high_response_proved"] is True,
            "whole actual four high responses retained")
    require(D["kind"] == D_KIND and D["complete"] is True and D["proved"] is True
            and D["actual_returncode"] == 0 and D_execution["scientific_complete"] is True
            and D_execution["actual_child_returncode"] == 0
            and D["run_id"] == D_execution["run_id"]
            and D["run_attempt"] == D_execution["run_attempt"]
            and D["saved_record_count"] == 10 and len(D["completed_targets"]) == 2
            and D["boundary_lift"]["complete_reference_weighted_right97_lift_proved"] is True
            and D["boundary_lift"]["complete_reference_joint193_boundary_lift_proved"] is True
            and D["boundary_lift"]["actual_low_boundary_lift_proved"] is False,
            "both complete exact-reference boundary inputs, not a claimed actual lift")
    require(L["kind"] == "W2C_low_family_necessary_budget_diagnostic_v1"
            and L["complete"] is True and L["failure"] is None and L["actual_returncode"] == 0
            and L_execution["scientific_complete"] is True and L_execution["actual_child_returncode"] == 0
            and L["run_id"] == L_execution["run_id"] == "44724797559"
            and L["run_attempt"] == L_execution["run_attempt"] == "1"
            and L["saved_record_count"] == 3,
            "whole old continuous-kernel L certificate qualified by H6")
    identity = low["reference_identity"]
    require(all(item["reference_identity"] == identity for item in (gh5, gh4, D, L))
            and low["parameters"] == gh5["parameters"] == D["parameters"] == L["parameters"],
            "same complete D/S/true-root chains and original coefficient-family parameters")
    modules = gh5["scientific_modules"][:7]
    require(tuple(item["role"] for item in modules) == ORIGINAL_MODULE_ROLES
            and all(item["scientific_modules"][:7] == modules for item in (low, D, L)),
            "all seven complete original signed source definitions remain identical")
    require(negative["kind"] == "actual_full_real_delta_negative_one_positive_given_head_graph_v1"
            and negative["complete"] is True and negative["failure"] is None
            and negative["derived_definition_sha256"] == REPAIR_SHA
            and negative["explicit_direction_definition_sha256"] == DIRECTION_SHA
            and negative["exact_real_delta_radius"] == "1/100000000"
            and negative["input_order"] == NEGATIVE_INPUTS
            and negative["negative_one_source_window_proved"] is True
            and negative["complete_negative_order_physical_outer_graph_proved"] is True
            and negative["exterior_input_order"] == ["low_nonmean_y_Hminus5over6",
                "independent_outer_height_dotH_two_minus5over6", "ordinary_Robin_Hminus5over6", "independent_mean_residual"]
            and negative["exterior_mean_input_order"] == ["full_nonmean_y_Hminus5over6",
                "independent_outer_height_dotH_two_minus5over6", "independent_mean_residual"]
            and all(isinstance(row, list) and len(row) == 7 for row in negative["response_rows"].values())
            and negative["full_low_high_Schur_inverse_proved"] is False
            and negative["complete_infinite_BVP_inverse_proved"] is False,
            "complete whole-space Robin/mean chart and all original rough seven ports")
    epsilon = saved_upper(api, lc["defect"]["body_norm_upper"])
    if low["kind"] == COERCIVE_LOW_KIND:
        symmetric, resolvent = lc["symmetric_part"], lc["resolvent"]
        theta = saved_upper(api, symmetric["symmetric_part_norm_upper"])
        gamma = saved_lower(api, resolvent["coercivity_gap_lower"])
        R = saved_upper(api, resolvent["resolvent_norm_upper"])
        require(bool(epsilon >= api.one)
                and symmetric["kind"] == "R149_complete_weighted_body_symmetric_part_v1"
                and symmetric["source_role"] == "true_coefficient_defect"
                and symmetric["complete_signed_trace_of_square"] is True
                and symmetric["whole_saved_norm_readback_used"] is True
                and symmetric["complete_cells"] == model["refined_cells"]
                and resolvent["kind"] == "R142_same_model_symmetric_part_resolvent_v1"
                and resolvent["body_space"]
                    == "original_WVC_S_weighted_ordinary_L2_dr_all193_body_coordinates"
                and resolvent["complete_cells"] == model["refined_cells"]
                and resolvent["strict_low_coefficient_residual_passed"] is False
                and resolvent["strict_symmetric_part_gate_passed"] is True
                and resolvent["actual_low_BVP_proved"] is True
                and resolvent["symmetric_part_norm_upper"] == symmetric["symmetric_part_norm_upper"]
                and bool(theta < api.one) and bool(gamma > api.zero)
                and bool(gamma <= (api.one-theta).lower())
                and bool(R >= upper(api, api.one/gamma)),
                "whole saved symmetric coercivity/resolvent and unchanged false original epsilon")
    else:
        require(bool(epsilon < api.one), "the same saved strict low defect gate")
    source_bounds = {}
    for role in ROLES:
        actual = lc["sources"][role]["actual"]
        comparison = lc["sources"][role]["comparison"]
        require(actual["actual_low_BVP_proved"] is True
                and actual["source_role"] == comparison["source_role"] == role
                and comparison["complete_output_atoms"] == 193
                and comparison["complete_original_panels"] == 155
                and comparison["complete_refined_cells"] == model["refined_cells"],
                "one whole source role with all actual observations")
        if low["kind"] == COERCIVE_LOW_KIND:
            require(actual["low_resolvent_basis"] == "symmetric_part_coercivity"
                    and actual["strict_low_coefficient_residual_passed"] is False
                    and actual["strict_symmetric_part_gate_passed"] is True
                    and all(actual[key] == lc["resolvent"][key]
                            for key in ("symmetric_part_norm_upper", "coercivity_gap_lower",
                                        "resolvent_norm_upper", "comparison_defect_body_upper")),
                    "each completed source uses the same whole original saved resolvent")
        source_bounds[role] = {"body": saved_upper(api, actual["actual_body_norm_upper"]),
            "atoms": saved_upper(api, actual["actual_atoms193_norm_upper"]),
            "complete": saved_upper(api, actual["actual_complete_source_norm_upper"]),
            "root_model_squared": saved_upper(api, comparison["root97_HS2_upper"]),
            "outer_model_squared": saved_upper(api, comparison["outer96_HS2_upper"])}
    admitted = {"private_token": object(), "reference_identity": identity,
        "source_bounds": source_bounds,
        "root_defect_squared": saved_upper(api, lc["defect"]["root97_HS2_upper"]),
        "outer_defect_squared": saved_upper(api, lc["defect"]["outer96_HS2_upper"]),
        "L": saved_upper(api, L["new_records"]["complete_low_family_feedback_norm_upper"]),
        "delta_C": saved_upper(api, gh5["new_records"]["complete_family_BLH_raw_L2_upper"]),
        "HB": saved_upper(api, gh4["new_records"]["actual_GH_raw_L2_from_complete_head_upper"]),
        "tX": saved_upper(api, gh4["new_records"]["actual_GH_outer_even_Hminus5over6_from_complete_head_upper"]),
        "Hroot": saved_upper(api, gh4["new_records"]["actual_GH_root_outgoing_Z_from_complete_head_upper"]),
        "D": D["new_records"], "negative": negative,
        "old_scientific_targets_recomputed": 0}
    admitted["high_response_source_binding"] = {
        "kind": "whole_original_GH4_records", "run_id": "44740105701", "run_attempt": "1"}
    require((weighted is None) == (weighted_execution is None),
            "whole weighted scientific/execution pair or no weighted replacement")
    if weighted is not None:
        response = weighted["weighted_response"]
        require(weighted["kind"] == WEIGHTED_KIND
                and weighted["complete"] is True and weighted["proved"] is True
                and weighted["failure"] is None and weighted["actual_returncode"] == 0
                and weighted_execution["scientific_complete"] is True
                and weighted_execution["actual_child_returncode"] == 0
                and weighted["run_id"] == weighted_execution["run_id"] == "44746534556"
                and weighted["run_attempt"] == weighted_execution["run_attempt"] == "1"
                and weighted["reference_identity"] == identity
                and weighted["parameters"] == low["parameters"]
                and weighted["scientific_modules"][:7] == modules
                and weighted["saved_record_count"] == len(weighted["completed_targets"]) == 5
                and response["complete_actual_head_to_high_weighted_response_proved"] is True
                and response["same_full_family_mean_source_column_retained"] is True
                and response["original_infinite_high_unknown_truncated"] is False
                and response["actual_low_high_inverse_proved"] is False
                and response["actual_physical_outer_rows_proved"] is False,
                "entire genuine weighted high response in the identical original family")
        names = {
            "HB": "actual_GH_weighted_raw_L2_from_complete_head_upper",
            "tX": "actual_GH_weighted_outer_even_Hminus5over6_from_complete_head_upper",
            "Hroot": "actual_GH_weighted_root_outgoing_Z_from_complete_head_upper"}
        for variable, name in names.items():
            admitted[variable] = saved_upper(api, weighted["new_records"][name])
        admitted["high_response_source_binding"] = {
            "kind": "explicit_complete_weighted_GH_response", "run_id": "44746534556",
            "run_attempt": "1", "variable_to_whole_saved_record": names,
            "old_GH4_whole_result_retained_without_renaming": True,
            "new_bound_asserted_smaller_without_comparison": False}
    return admitted


def complete_new_scalar_closure(api, admitted, emit):
    """Complete first internal-gate branch and, if passed, true physical outer gate.

    emit must save/read back each full directed ball before returning it.
    False sufficient gates are returned as complete results, never singularity.
    Counts and all exact record names are retained by the future owner.
    """
    require("private_token" in admitted, "same complete previously admitted scalar objects")
    records = []

    def save(name, value, bound="upper"):
        require(bound in ("upper", "lower") and value.is_finite(), "directed scalar saving semantics")
        point = upper(api, value) if bound == "upper" else value.lower()
        read = emit(name, point, bound)
        require(read.is_finite(), "finite complete readback endpoint")
        if bound == "upper":
            require(bool(read >= point), "readback upper encloses the mathematical upper")
        else:
            require(bool(read <= point), "readback lower encloses the mathematical lower")
        records.append(name)
        return read

    source = {role: dict(value) for role, value in admitted["source_bounds"].items()}
    er, eo = root(api, admitted["root_defect_squared"]), root(api, admitted["outer_defect_squared"])
    for role in ROLES:
        value = source[role]
        value["root"] = save(role+"_actual_root97_upper",
            root(api, value["root_model_squared"])+er*value["body"])
        value["outer"] = save(role+"_actual_outer96_upper",
            root(api, value["outer_model_squared"])+eo*value["body"])
    correction = source["low_second_kind_correction"]
    centre = source["centre_high0_return_source"]
    raw = source["ordinary_raw_low_source"]
    L, HB, dC = admitted["L"], admitted["HB"], admitted["delta_C"]
    kappa, ell = {}, {}
    for name in ("body", "root", "outer", "atoms"):
        factor = api.one+correction[name] if name == "body" else hypot(api, api.one, correction[name])
        ell[name] = save("actual_low_family_"+name+"_upper", factor*L)
        kappa[name] = save("actual_internal_feedback_"+name+"_upper",
            ell[name]+(centre[name]+raw[name]*dC)*HB)
    result = {"kind": "complete_low_high_and_physical_outer_scalar_gate_v1",
        "reference_identity": admitted["reference_identity"],
        "same_actual_internal_gate_passed": bool(kappa["body"] < api.one),
        "same_actual_physical_outer_gate_passed": False,
        "actual_singularity_inferred": False, "original_finite_rho_bridge_proved": False,
        "old_WJK_F_replaced_without_paying_difference": False,
        "full_original_seven_port_response_matrix_proved": False,
        "either_original_WPN_RHS_proved": False, "negative_connection_or_nonlinear_family_proved": False,
        "topic_completion_proved": False, "old_scientific_targets_recomputed": 0,
        "complete_new_record_order": records, "source_receivers": source, "kappa": kappa}
    if not result["same_actual_internal_gate_passed"]:
        result["complete_branch"] = "complete_internal_sufficient_gate_not_passed"
        return result
    gap = save("actual_internal_body_gap_lower", api.one-kappa["body"], "lower")
    require(bool(gap > api.zero), "strict complete saved internal body gap")

    def close(prefix, start):
        body = save(prefix+"_body_upper", start["body"]/gap)
        values = {"body": body}
        for name in ("root", "outer", "atoms"):
            values[name] = save(prefix+"_"+name+"_upper", start[name]+kappa[name]*body)
        values["complete"] = save(prefix+"_complete_upper", hypot(api, values["body"], values["atoms"]))
        return values

    boundary = {}
    for kind, prefix in (("right", "reference_weighted_right97_"), ("joint", "reference_joint193_boundary_")):
        D = {name: saved_upper(api, admitted["D"][prefix+label+"_upper"])
             for name, label in (("body", "body"), ("root", "root97"),
                                 ("outer", "outer96"), ("atoms", "atoms193"))}
        low = {"body": save("actual_low_"+kind+"_boundary_body_upper", (api.one+correction["body"])*D["body"])}
        for name in ("root", "outer", "atoms"):
            low[name] = save("actual_low_"+kind+"_boundary_"+name+"_upper", D[name]+correction[name]*D["body"])
        boundary[kind] = close("actual_internal_"+kind+"_boundary", low)
    negative = admitted["negative"]
    beta = saved_upper(api, negative["exterior_affine_Y_output_coefficients"][0])
    Cminus = saved_upper(api, negative["response_rows"]["entire_positive_raw_L2r_Hminus1"][3])
    CY = saved_upper(api, negative["response_rows"]["body_Y_sup"][3])
    l160 = root(api, api.rational(1+16*160*160))
    l288 = root(api, api.rational(1+16*288*288))
    poisson_low = {}
    for name in ("body", "root", "outer", "atoms"):
        poisson_low[name] = save("actual_outer_b_Poisson_low_"+name+"_upper",
            (l160*centre[name]+l288*raw[name]*dC)*Cminus*beta)
    J = close("actual_internal_outer_b_Poisson_low", poisson_low)
    tb = save("actual_outer_b_high_even_trace_upper", 4*CY*beta)
    E = saved_upper(api, negative["actual_complete_negative_order_outer_constants"]["raw_Robin_bound"])
    mean = saved_upper(api, negative["exterior_mean_output_coefficients"][0])
    ab = save("actual_physical_low_to_right97_upper", hypot(api, api.rational(3, 80)+E, mean))
    ah = save("actual_physical_high_to_right97_upper", hypot(api, E, mean))
    P, tx = boundary["right"], admitted["tX"]
    u = save("actual_physical_right_from_right97_upper", ah*tx*P["body"])
    v = save("actual_physical_right_from_outer96_upper", ab+ah*(tb+tx*J["body"]))
    w = save("actual_physical_outer_from_right97_upper", P["outer"])
    z = save("actual_physical_outer_from_outer96_upper", J["outer"])
    result.update({"complete_new_record_order": records, "boundary": boundary, "outer_b_poisson_low": J,
        "positive_outer_block_upper": ((u, v), (w, z)), "all193_output_atoms_retained": True,
        "root97_and_outer96_receivers_retained_separately": True,
        "physical_Robin_mean_operators_used_on_complete_meanzero_space": True,
        "rho_C_keeps_original_mean_and_height_chart_units": True,
        "arbitrary_L2_trace_taken": False})
    if not bool(u < api.one) or not bool(z < api.one):
        result["complete_branch"] = "complete_physical_outer_diagonal_gate_not_passed"
        return result
    left = save("physical_right_diagonal_margin_lower", api.one-u, "lower")
    right = save("physical_outer_diagonal_margin_lower", api.one-z, "lower")
    if not bool(left > api.zero) or not bool(right > api.zero):
        result["complete_branch"] = "complete_saved_physical_outer_diagonal_margin_not_passed"
        return result
    det = save("physical_positive_two_block_determinant_lower", left*right-v*w, "lower")
    if not bool(det > api.zero):
        result["complete_branch"] = "complete_physical_outer_determinant_gate_not_passed"
        return result
    # Inverse numerator uses upper 1-z,1-u, not the lower margins above.
    # Using smaller lower margins there would reverse the desired norm bound.
    inverse = ((save("physical_block_inverse_right_from_right_upper", (api.one-z)/det),
                save("physical_block_inverse_right_from_outer_upper", v/det)),
               (save("physical_block_inverse_outer_from_right_upper", w/det),
                save("physical_block_inverse_outer_from_outer_upper", (api.one-u)/det)))
    result.update({"same_actual_physical_outer_gate_passed": True,
        "complete_branch": "complete_same_positive_physical_boundary_inverse_gate",
        "physical_block_inverse_majorant": inverse, "complete_new_record_order": records,
        "actual_positive_given_root_input_inverse_proved": True})
    return result


def restore_complete_gate_from_saved_records(api, admitted, gate):
    """Read the paid58 record endpoints; never rerun the previous closure."""
    require(gate["complete"] is True and gate["proved"] is True
            and gate["failure"] is None and gate["actual_returncode"] == 0
            and gate["saved_record_count"] == 58,
            "whole successfully completed58 gate supplied")
    metadata = gate["result"]
    require(metadata["kind"] == "complete_low_high_and_physical_outer_scalar_gate_v1"
            and metadata["reference_identity"] == admitted["reference_identity"]
            and metadata["same_actual_physical_outer_gate_passed"] is True
            and metadata["same_actual_internal_gate_passed"] is True
            and metadata["complete_branch"] == "complete_same_positive_physical_boundary_inverse_gate"
            and metadata["complete_new_record_order"] == gate["completed_targets"]
            and set(gate["new_records"]) == set(gate["completed_targets"]),
            "complete saved physical-gate identity and record layout")
    def read(name):
        return saved_upper(api, gate["new_records"][name])
    closed = dict(metadata)
    closed["source_receivers"] = {}
    for role in ROLES:
        closed["source_receivers"][role] = dict(admitted["source_bounds"][role])
        for output in ("root", "outer"):
            closed["source_receivers"][role][output] = read(role+"_actual_"+("root97" if output == "root" else "outer96")+"_upper")
    closed["kappa"] = {name: read("actual_internal_feedback_"+name+"_upper")
                       for name in ("body", "root", "outer", "atoms")}
    closed["boundary"] = {
        kind: {name: read("actual_internal_"+kind+"_boundary_"+name+"_upper")
               for name in ("body", "root", "outer", "atoms", "complete")}
        for kind in ("right", "joint")}
    closed["outer_b_poisson_low"] = {
        name: read("actual_internal_outer_b_Poisson_low_"+name+"_upper")
        for name in ("body", "root", "outer", "atoms", "complete")}
    closed["positive_outer_block_upper"] = tuple(tuple(read(
        "actual_physical_"+row+"_from_"+column+"_upper")
        for column in ("right97", "outer96")) for row in ("right", "outer"))
    closed["physical_block_inverse_majorant"] = tuple(tuple(read(
        "physical_block_inverse_"+row+"_from_"+column+"_upper")
        for column in ("right", "outer")) for row in ("right", "outer"))
    return closed
