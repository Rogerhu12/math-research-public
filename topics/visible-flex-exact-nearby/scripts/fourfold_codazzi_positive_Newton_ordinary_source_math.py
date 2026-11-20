"""Seven new ordinary positive Newton-source bounds from saved whole inputs.

Only definitions and standard-library rational metadata occur at import.
No file I/O, old producer import, floating evaluation, or scientific entry
point is provided. The owner supplies a directed API and an atomic
save/readback/contains emitter. Numerical evaluation belongs to its own
public Actions run.
"""
from fractions import Fraction

KIND = "complete_selected_member_positive_Newton_ordinary_source_v1"
CANDIDATE = "ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
CENTRE = "440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
DIRECTION = "6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
OBJECT = "91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848"
RAW_SOURCE = "24ec0bf2b9d2b03ebfa07f4b39b8fdee3277f8e4b2aa14385c267122e6b8e81f"
RAW_PRODUCER = "98eb7034038d76a341e112927cff4bcb7bfd425bc56698305803a689060ac31e"
ALPHA = "6890507429876859/9007199254740992"
NU = "-2572625729470897/72057594037927936"
ETA = "-7789843107295549/4611686018427387904"
LEFT = "9/10"
RIGHT = "25/8"
BODY_LEFT = "1192029371497/5000000000000"
ROOT_LO = "1191984371497/5000000000000"
ROOT_HI = "2383968743003/10000000000000"
DELTA = "1/10000000000"
OLD_DELTA = "1/100000000"
EQ0 = "0.000000000000000003861"
EQ1 = "0.00000000000000001970"
SELECTED_UPPER = "0.00000000009368259853002"
TARGETS = (
    "new_outer_tail_raw_physical_residual_L2_upper",
    "new_outer_tail_continuous_centre_repair_L2_upper",
    "new_outer_tail_selected_nonlinear_remainder_L2_upper",
    "complete_outer_tail_selected_Newton_full_L2_upper",
    "complete_positive_selected_Newton_full_L2_upper",
    "complete_positive_selected_Newton_low193_L2_upper",
    "complete_positive_selected_Newton_high97_through288_L2_upper",
)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def completed(document, gate_count):
    return (document.get("complete") is True
            and document.get("failure") is None
            and len(document.get("gates", [])) == gate_count
            and all(g.get("passed") is True for g in document["gates"]))


def interval_record(record):
    """Structural check only; directed parsing occurs in the public child."""
    if isinstance(record, str):
        require(bool(record), "empty saved interval")
        return
    require(isinstance(record, dict), "saved interval is not a whole record")
    require(isinstance(record.get("ball"), str)
            or (isinstance(record.get("lower"), str)
                and isinstance(record.get("upper"), str)),
            "saved interval lacks its complete ball or two endpoint balls")


def whole_partition(rows, start, finish, interval_key="interval"):
    cursor = Fraction(start)
    result = []
    for index, row in enumerate(rows):
        left, right = map(Fraction, row[interval_key])
        require(left == cursor and left < right,
                "missing or reordered original closed row")
        result.append((left, right, index))
        cursor = right
    require(cursor == Fraction(finish), "whole original partition has a missing end")
    return result


def tail_partition(partition):
    cursor = Fraction(LEFT)
    result = []
    for old_left, old_right, index in partition:
        left = max(Fraction(LEFT), old_left)
        right = min(Fraction(RIGHT), old_right)
        if left >= right:
            continue
        require(left == cursor, "new ordinary tail has a gap or overlap")
        result.append((left, right, index))
        cursor = right
    require(result and cursor == Fraction(RIGHT),
            "new ordinary tail does not reach the true regular end")
    return result


def admit_metadata(raw, positive, core, z, body, nif, wobsa):
    """Validate entire saved mathematical objects without scientific arithmetic.

    Whole current/native byte identities and complete process receipts are
    additionally the owner's admission responsibility. This function never
    executes an old source nor evaluates an old scientific scalar.
    """
    require(raw.get("kind") ==
            "complete_actual_moving_residual_all_closed_rows_and_interfaces"
            and raw.get("complete") is True and raw.get("failure") is None
            and raw.get("source_sha256") == RAW_SOURCE
            and raw.get("original_producer_sha256") == RAW_PRODUCER
            and raw.get("candidate_sha256") == CANDIDATE
            and raw.get("object_sha256") == OBJECT
            and Fraction(raw["exact_amplitude"]) == Fraction(ALPHA)
            and Fraction(raw["exact_nu"]) == Fraction(NU)
            and Fraction(raw["common_parameter_half_width"]) == 0
            and raw.get("all_7296_closed_rows_reused_without_recomputation") is True
            and raw.get("all_6143_actual_interfaces_paid") is True
            and raw.get("complete_original_primitive_tail") is True
            and raw.get("complete_residual_support") == 96
            and raw.get("interval") == ["0", RIGHT]
            and len(raw["rows"]) == 7296
            and len(raw["complete_interface_jumps"]) == 6143,
            "the complete original7296 raw source identity changed")
    raw_partition = whole_partition(raw["rows"], "0", RIGHT)
    for index, row in enumerate(raw["rows"]):
        require(row.get("index") == index
                and row.get("exact_angular_support_index") == 96,
                "original raw support or row index changed")
        for key in ("U", "V"):
            interval_record(row["complete_residual_A0"][key])
    ident = positive["identity"]
    require(positive.get("complete") is True
            and positive.get("coefficient_cover_complete") is True
            and positive.get("failure") is None and len(positive["rows"]) == 4650
            and ident.get("candidate_sha256") == CANDIDATE
            and ident.get("object_sha256") == OBJECT
            and Fraction(ident["actual_alpha"]) == Fraction(ALPHA)
            and Fraction(ident["actual_nu"]) == Fraction(NU)
            and Fraction(ident["exact_eta_center"]) == Fraction(ETA)
            and positive.get("whole_original_eta") is True,
            "whole original4650 physical coefficient identity changed")
    positive_partition = whole_partition(positive["rows"], BODY_LEFT, RIGHT)
    interfaces = 0
    for row in positive["rows"]:
        require(row.get("physical_inverse_gap_certified") is True,
                "old whole-row physical domain qualification missing")
        interfaces += row["right_interface"] is not None
        for key in ("beta", "gamma", "K"):
            interval_record(row["intrinsic"][key])
        for key in ("U_A0", "V_A0", "U_phi_A0", "V_phi_A0"):
            interval_record(row["bounds"][key])
    require(interfaces == 3594, "old positive interfaces were omitted")
    require(completed(core, 18) and core.get("proved") is True
            and core.get("actual_returncode") == 0
            and core.get("complete_selected_ordinary_source_bounds_proved") is True
            and core.get("derived_continuous_centre_definition_sha256") == CENTRE
            and core.get("exact_continuous_direction_definition_sha256") == DIRECTION,
            "whole CRA actual source certificate missing")
    cp = core["parameters"]
    require(cp["exact_core_interval"] == ["0", LEFT]
            and Fraction(cp["exact_delta_half_width"]) == Fraction(DELTA)
            and Fraction(cp["exact_eta0"]) == Fraction(ETA)
            and Fraction(cp["exact_nu0"]) == Fraction(NU)
            and Fraction(cp["exact_amplitude"]) == Fraction(ALPHA)
            and cp["ordinary_radial_measure"] == "dr"
            and Fraction(cp["centre_repair_pair_A0"]) == Fraction(EQ0)
            and Fraction(cp["centre_repair_pair_A1"]) == Fraction(EQ1),
            "CRA member, source measure, or full repair differs")
    cs = core["complete_selected_source_conclusion"]
    choice = cs["complete_background_choices"]["new_core_restriction"]
    require(choice["full_even_mean_retained"] is True
            and choice["known_centre_residual_is_exactly_low193"] is True
            and choice["extra_Z_mean_or_384EZ_fee"] is False
            and cs["D_additional_source_not_misidentified_as_total_f_delta"] is True
            and Fraction(cs["exact_delta_half_width"]) == Fraction(DELTA),
            "same complete CRA choice and full quadratic source required")
    for key in ("uniform_selected_full_L2_upper",
                "uniform_selected_low193_L2_upper"):
        interval_record(choice[key])
    interval_record(cs["complete_quadratic_source_contribution"])
    require(completed(z, 6) and z.get("phase") == "finish"
            and z.get("candidate_sha256") == CANDIDATE
            and z.get("derived_continuous_centre_definition_sha256") == CENTRE
            and z.get("exact_continuous_direction_definition_sha256") == DIRECTION
            and z.get("exact_affine_parameter_offset") == "0"
            and z.get("whole_complete_source_interval") == ["0", RIGHT]
            and z.get("complete_rows") == 7721
            and z.get("complete_original_common_cells") == 7721
            and z.get("complete_valid_source_cover") is True
            and z.get("true_independent_even_mean_retained") is True
            and z.get("known_high_output_retained") is True,
            "whole7721 delta0 full-mean source certificate differs")
    for species in ("full_through160", "low193", "high97_through160"):
        interval_record(z["complete_source_bounds"]["full_body"][species]["L2_L2_radial"])
    require(completed(body, 11)
            and body.get("original_candidate_sha256") == CANDIDATE
            and body.get("derived_definition_sha256") == CENTRE
            and body.get("explicit_direction_definition_sha256") == DIRECTION
            and Fraction(body["exact_real_delta_radius"]) == Fraction(OLD_DELTA)
            and list(map(Fraction, body["exact_radial_interval"])) ==
                [Fraction(BODY_LEFT), Fraction(RIGHT)]
            and body.get("complete_original_rows") == 4650
            and body.get("complete_original_raw_response_envelope_rows") == 7721
            and body.get("original_right_interfaces_preserved") == 3594
            and body.get("actual_family_value_and_all_angular_derivative_jumps_zero") is True
            and body.get("all_original_affine_unknown_jumps_and_full_mean_ports_retained") is True,
            "same full-body linear-in-radius direction bounds missing")
    for key in ("A0", "angular_A0"):
        interval_record(body["complete_delta_input_bounds"][key])
    require(completed(nif, 16)
            and Fraction(nif["parameters"]["exact_intrinsic_parameter"]) == Fraction(ETA)
            and Fraction(nif["parameters"]["exact_real_delta_radius"]) == Fraction(OLD_DELTA)
            and Fraction(nif["parameters"]["fixed_selected_parameter_absolute_upper"]) ==
                Fraction(SELECTED_UPPER)
            and Fraction(SELECTED_UPPER) < Fraction(DELTA) < Fraction(OLD_DELTA)
            and nif["parameters"]["uniform_selected_conjugacy_family_claimed"] is False,
            "same frozen selected member range was not retained")
    require(completed(wobsa, 18)
            and wobsa.get("actual_returncode") == 0
            and wobsa["parameters"]["same_selected_member_only"] is True
            and Fraction(wobsa["parameters"]["exact_real_delta_radius"]) == Fraction(OLD_DELTA)
            and wobsa["retained_scope"]["same_selected_member_same_physical_eta0"] is True,
            "WOBSA selected-member qualification was silently changed")
    require(Fraction(ROOT_HI) < Fraction(LEFT)
            and Fraction(ROOT_LO) > Fraction(9, 50),
            "true root restriction or positive bump-free domain differs")
    raw_tail = tail_partition(raw_partition)
    positive_tail = tail_partition(positive_partition)
    return {
        "raw_tail": raw_tail,
        "positive_tail": positive_tail,
        "core_choice": choice,
        "core_quadratic": cs["complete_quadratic_source_contribution"],
        "z_whole": z["complete_source_bounds"]["full_body"],
        "direction_whole": body["complete_delta_input_bounds"],
        "metadata": {
            "original_raw_rows": 7296,
            "original_raw_interfaces": 6143,
            "original_positive_rows": 4650,
            "original_positive_interfaces": interfaces,
            "new_raw_tail_intersections": len(raw_tail),
            "new_positive_tail_intersections": len(positive_tail),
            "exact_new_tail": [LEFT, RIGHT],
            "exact_core_restriction": ["true_original_root", LEFT],
            "exact_new_tail_length": str(Fraction(RIGHT)-Fraction(LEFT)),
            "core_and_root_germ_scientific_targets_recomputed": 0,
            "whole7721_source_rows_recomputed": 0,
            "old_7296_whole_or_core_integrals_recomputed": 0,
            "selected_parameter_is_not_a_new_numeric_point": True,
        },
    }


def complete_bounds(api, raw, positive, admitted, emit, progress=None):
    """Evaluate exactly TARGETS in order using only new tail combinations.

    API: rational, old_interval, upper, magnitude, sqrt_upper.
    emit(name, value) MUST atomically save the complete ball, read it back,
    prove containment of the original upper, and return its directed upper.
    progress(stage, metadata, accumulators) preserves a small unfinished
    prefix; accumulators are never labelled complete target bounds.
    """
    q, up = api.rational, api.upper
    zero, one = q("0"), q("1")

    def old_upper(record):
        value = up(api.old_interval(record))
        require(value >= zero, "saved nonnegative bound has negative upper")
        return value

    def sqrt(value):
        value = up(value)
        require(value >= zero, "nonnegative new squared bound unresolved")
        return up(api.sqrt_upper(value))

    def hypot(a, b):
        return sqrt(up(a*a+b*b))

    def saved(name, value):
        result = emit(name, up(value))
        require(result >= zero, "saved/read-back directed upper is negative")
        return result

    square = zero
    for done, (left, right, index) in enumerate(admitted["raw_tail"], 1):
        row = raw["rows"][index]
        ru = old_upper(row["complete_residual_A0"]["U"])
        rv = old_upper(row["complete_residual_A0"]["V"])
        width = q(str(right-left))
        square = up(square+width*(ru*ru+rv*rv))
        if progress is not None and (done % 128 == 0 or done == len(admitted["raw_tail"])):
            progress("new_raw_tail_prefix", {
                "completed_intersections": done,
                "last_original_index": index,
                "exact_prefix_end": str(right),
                "entire_tail_complete": done == len(admitted["raw_tail"]),
            }, {"unscaled_pair_square_prefix": square})
    raw_tail = saved(TARGETS[0], up(q(ALPHA)*sqrt(square)))

    e0 = up(q("1/100")*old_upper(admitted["direction_whole"]["A0"]))
    e1 = up(q("1/100")*old_upper(admitted["direction_whole"]["angular_A0"]))
    eq0, eq1 = q(EQ0), q(EQ1)
    repair_square, nonlinear_square = zero, zero
    for done, (left, right, index) in enumerate(admitted["positive_tail"], 1):
        row = positive["rows"][index]
        intrinsic, bounds = row["intrinsic"], row["bounds"]
        curvature = up(api.magnitude(api.old_interval(intrinsic["K"])))
        kp = curvature if curvature > one else one
        beta = up(api.magnitude(api.old_interval(intrinsic["beta"])))
        gamma = up(api.magnitude(api.old_interval(intrinsic["gamma"])))
        b, g = up(beta*kp), up(gamma*kp)
        q0 = up(old_upper(bounds["U_A0"])+old_upper(bounds["V_A0"])+eq0)
        q1 = up(old_upper(bounds["U_phi_A0"])+old_upper(bounds["V_phi_A0"])+eq1)
        c0 = up(b*(one+3*q0*q0+q0*q1/2)+g*q1)
        c1 = up(b*q0*q0/4+g*q0)
        repair = up(c0*eq0+c1*eq1)
        nonlinear = up(b*(e0*e0*q1/4+q0*e0*e1/2+3*q0*e0*e0
                           +e0*e0*e1/4+e0*e0*e0)+g*e0*e1)
        width = q(str(right-left))
        repair_square = up(repair_square+width*repair*repair)
        nonlinear_square = up(nonlinear_square+width*nonlinear*nonlinear)
        if progress is not None and (done % 128 == 0 or done == len(admitted["positive_tail"])):
            progress("new_coefficient_tail_prefix", {
                "completed_intersections": done,
                "last_original_index": index,
                "exact_prefix_end": str(right),
                "entire_tail_complete": done == len(admitted["positive_tail"]),
            }, {
                "centre_repair_square_prefix": repair_square,
                "selected_nonlinear_square_prefix": nonlinear_square,
            })
    repair_tail = saved(TARGETS[1], sqrt(repair_square))
    nonlinear_tail = saved(TARGETS[2], sqrt(nonlinear_square))

    z = admitted["z_whole"]
    sf = old_upper(z["full_through160"]["L2_L2_radial"])
    sl = old_upper(z["low193"]["L2_L2_radial"])
    sh = old_upper(z["high97_through160"]["L2_L2_radial"])
    delta = q(DELTA)
    common_tail = up(raw_tail+repair_tail+nonlinear_tail)
    full_tail = saved(TARGETS[3], up(common_tail+delta*sf))
    core = admitted["core_choice"]
    cf = old_upper(core["uniform_selected_full_L2_upper"])
    cl = old_upper(core["uniform_selected_low193_L2_upper"])
    cq = old_upper(admitted["core_quadratic"])
    saved(TARGETS[4], hypot(cf, full_tail))
    low_tail = up(common_tail+delta*sl)
    saved(TARGETS[5], hypot(cl, low_tail))
    saved(TARGETS[6], up(delta*sh+hypot(cq, nonlinear_tail)))
    return {
        "complete": True,
        "completed_target_count": len(TARGETS),
        "same_selected_member_via_uniform_restriction": True,
        "source_sign": "Newton ordinary source is minus f_delta",
        "source_norm": "ordinary dr and normalized original moving-circle pair L2",
        "independent_even_mean_retained": True,
        "known_centre_residual_last_quarter_index": 96,
        "known_complete_selected_source_last_quarter_index": 288,
        "high_source_is_not_set_to_zero": True,
        "old_core_and_true_root_germ_source_recomputed": False,
        "future224_or32_records_created": False,
        "physical_boundary_Robin_mean_height_values_proved": False,
        "two_WPN_rhs_completed": False,
        "full_inverse_proved": False,
        "nonlinear_solution_proved": False,
    }
