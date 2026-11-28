"""Physical receivers of the complete joint Grassmann Green on the original WVC family."""
TRUE_LOW_KIND = "complete_R149_true_low193_joint_grassmann_and_source_maps_v1"
TRUE_LOW_TARGETS = (
    "complete_true_low193_joint_Grassmann_inverse",
    "complete_true_low193_joint_four_whole_source_maps",
)
TRUE_BASIS = "actual_joint_Grassmann_all_graphs_nodes_and_four_whole_maps"
GH5_KIND = "complete_actual_GH_Hthird_source_fees_v1"
GH4_KIND = "complete_actual_GH_saved_Hthird_head_response_v1"
WEIGHTED_KIND = "complete_actual_GH_radially_weighted_head_response_v1"
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
    """True GG maps plus the unchanged complete original full-family inputs.

    The owner first calls the GG validator on the actual whole byte triple.
    The shared source/identity qualifications below are the original B/GH
    qualifications; none of them is inferred from a comparison defect.
    """
    require(low["kind"] == TRUE_LOW_KIND and low["complete"] is True
            and low["proved"] is True and low["actual_returncode"] == 0
            and low_execution["scientific_complete"] is True
            and tuple(low["completed_targets"]) == TRUE_LOW_TARGETS,
            "whole genuinely complete GG low inverse and all four actual maps")
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
    source_bounds = {}
    for role in ROLES:
        actual = low["certificate"]["sources"][role]
        require(actual["actual_low_BVP_proved"] is True and actual["source_role"] == role
                and actual["complete_true_cells"] == 1424,
                "the same whole direct source map, without comparison inflation")
        source_bounds[role] = {
            "body": saved_upper(api, actual["actual_body_norm_upper"]),
            "atoms": saved_upper(api, actual["actual_atoms193_norm_upper"]),
            "complete": saved_upper(api, actual["actual_complete_source_norm_upper"]),
            "root_actual_squared": saved_upper(api, actual["root97_HS2_upper"]),
            "outer_actual_squared": saved_upper(api, actual["outer96_HS2_upper"])}
    admitted = {"private_token": object(), "reference_identity": identity,
        "low_inverse_basis": TRUE_BASIS, "source_bounds": source_bounds,
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
    require(admitted["low_inverse_basis"] == TRUE_BASIS,
            "direct actual GG receivers, never manufactured comparison fields")
    for role in ROLES:
        value = source[role]
        value["root"] = save(role+"_actual_root97_upper",
            root(api, value["root_actual_squared"]))
        value["outer"] = save(role+"_actual_outer96_upper",
            root(api, value["outer_actual_squared"]))
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
        "low_inverse_basis": TRUE_BASIS,
        "old_comparison_point_certificate_required": False,
        "direct_true_source_maps_used_without_comparison_inflation": True,
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
    require(metadata["low_inverse_basis"] == admitted["low_inverse_basis"] == TRUE_BASIS
            and metadata["direct_true_source_maps_used_without_comparison_inflation"] is True,
            "the paid physical gate used this same direct GG basis")
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
