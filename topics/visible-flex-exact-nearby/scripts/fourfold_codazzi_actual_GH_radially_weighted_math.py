"""New radial source distribution functional for the same actual high inverse.

Pure definitions. Consume every original closed gap/frame row read only;
do not recompute Riccati, Volterra feedback, old ordinary-source gains,
the five completed source suprema, or any low/endpoint inverse target.
"""

from fractions import Fraction

KIND = "complete_actual_GH_radially_weighted_head_response_v1"
HEAD = tuple((0, j) for j in range(1, 97))+((1, 0),)+tuple((1, j) for j in range(1, 97))
HIGH0 = tuple((0, j) for j in range(97, 161))+tuple((1, j) for j in range(97, 161))
RECORDS = (
    "actual_GH_body_weighted_unperturbed_source_upper",
    "actual_GH_weighted_raw_L2_from_complete_head_upper",
    "actual_GH_weighted_body_Z_sup_from_complete_head_upper",
    "actual_GH_weighted_root_outgoing_Z_from_complete_head_upper",
    "actual_GH_weighted_outer_even_Hminus5over6_from_complete_head_upper",
)
BODY_NATIVE_SHA = "1f3e5fa630f39a667a96102f103ac8977d00e580f698a83904f361c5a05c6f3c"
REPAIR_SHA = "440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
DIRECTION_SHA = "6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
CUT = Fraction(1192029371497, 5000000000000)
OUTER = Fraction(25, 8)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def exact(api, value):
    value = Fraction(value)
    return api.rational(value.numerator, value.denominator)


def upper(api, value):
    require(value.is_finite(), "finite complete directed value")
    point = value.upper()
    require(api.lower(point) >= 0, "nonnegative mathematical upper endpoint")
    return point


def maximum(api, values):
    require(values, "nonempty complete set of directed uppers")
    return upper(api, api.hull([upper(api, item) for item in values]))


def root(api, value):
    return upper(api, api.sqrt(upper(api, value)))


def saved_upper(api, record):
    return upper(api, api.old_interval(record))


def hypot(api, values):
    points = [upper(api, item) for item in values]
    return root(api, sum((item*item for item in points), api.zero))


def _step(api, initial, forcing, damping, length):
    """New weighted forcing comparison on one exact common-refinement cell.

    All nonnegative inputs are directed points. Damping is a positive
    saved lower. Constant scalar flow is monotone toward forcing/damping,
    so the maximum of the two endpoints bounds the whole closed cell.
    """
    require(api.lower(initial) >= 0 and api.lower(forcing) >= 0
            and api.lower(damping) > 0 and api.lower(length) > 0,
            "complete nonnegative weighted comparison and positive true cell")
    decay = api.exp(-damping*length)
    endpoint = upper(api, decay*initial+(api.one-decay)*forcing/damping)
    return maximum(api, [initial, endpoint]), endpoint


def _complete_original_row_cover(admitted, base0):
    """Metadata and exact rational cover only, not a numerical old target."""
    native = admitted["native"]
    require(base0["kind"] == "actual_full_real_delta_root_to_regular_given_head_high_graph_v1"
            and base0["complete"] is True and base0["failure"] is None
            and base0["original_complete_body_native_sha256"] == BODY_NATIVE_SHA
            and base0["derived_definition_sha256"] == REPAIR_SHA
            and base0["explicit_direction_definition_sha256"] == DIRECTION_SHA
            and base0["exact_real_delta_radius"] == "1/100000000"
            and base0["fixed_body_cut"] == str(CUT),
            "same complete actual high graph and full original body")
    require(native["complete"] is True and native["failure"] is None
            and native["derived_definition_sha256"] == REPAIR_SHA
            and native["explicit_direction_definition_sha256"] == DIRECTION_SHA
            and native["exact_real_delta_radius"] == "1/100000000"
            and native["complete_original_rows"] == 4650
            and native["original_right_interfaces_preserved"] == 3594,
            "whole old body native retained after full byte admission")
    order = native["orders"][0]
    rows = admitted["kernels"]
    require(order["homogeneous_angular_order"] == 0 and order["complete"] is True
            and order["failure"] is None and order["actual_scalar_comparison_rows"] == 4650
            and order["canonical_exterior_feedback_closed"] is True
            and order["independent_right_high_port"] is False
            and order["full_unbounded_high_indices"] == "every |j|>=97"
            and order["physical_minimum"] == 388
            and order["every_original_closed_interval_and_both_complete_branches_retained"] is True
            and rows == order["complete_rows"] and len(rows) == 4650,
            "all original completed gap/frame rows and actual exterior feedback")
    cursor = CUT
    for index, row in enumerate(rows):
        left, right = map(Fraction, row["interval"])
        require(row["original_row"] == index and left == cursor and left < right,
                "entire original ordered closed radial cover")
        require("gap" in row["bounds"] and "frame" in row["bounds"],
                "original directed comparison facts present on every whole row")
        cursor = right
    require(cursor == OUTER, "the true regular endpoint remains in the old full cover")
    return rows, order


def _body_source_panels(api, km, context, progress):
    """Fresh inputs to this weighted integral, not the five old global suprema."""
    require(len(context.domain.cells) == 155 and len(context.parent_indices) == 155
            and set(context.parent_indices) == set(range(153))
            and context.parent_indices[0] == 0,
            "complete same original source cover and true collar")
    weights = [upper(api, api.rational(1+16*j*j)**api.rational(1, 6)) for _, j in HIGH0]
    family_weight = upper(api, api.rational(1+16*288*288)**api.rational(1, 6))
    panels = []
    previous = CUT
    parent_cache = {}
    for panel, cell in enumerate(context.domain.cells):
        parent = context.parent_indices[panel]
        if parent == 0:
            require(panel == 0 and cell["left"] is None and Fraction(cell["right"]) == CUT,
                    "the original whole collar is consumed only through saved GH5")
            continue
        left, right = Fraction(cell["left"]), Fraction(cell["right"])
        require(left == previous and left < right, "all whole actual source body panels")
        q = context.reference_qs[panel]
        require(api.lower(q) > 0, "same positive exact original S weight")
        if parent not in parent_cache:
            box = context.domain.whole_cell_box(panel)
            matrix = context.centre_matrix(HIGH0, HEAD, box)
            require(matrix.shape == (128, 193)
                    and all(row[96].lower() == 0 and row[96].upper() == 0 for row in matrix.values),
                    "complete signed centre source with its actual exact mean support")
            weighted = km.Matrix(128, 193,
                [[weights[i]*value/(q if HEAD[j][0] == 1 else api.one)
                  for j, value in enumerate(row)] for i, row in enumerate(matrix.values)])
            centre = upper(api, km.matrix_norm_upper(api, weighted))
            family = upper(api, family_weight*upper(api, context.family_fees["HL"][panel])
                           *maximum(api, [api.one, api.one/q]))
            parent_cache[parent] = {"q": q, "fee": context.family_fees["HL"][panel],
                                    "value": upper(api, centre+family)}
        cached = parent_cache[parent]
        require(bool(q == cached["q"])
                and context.family_fees["HL"][panel] is cached["fee"],
                "cache only identical original parent packet, exact q, and complete family fee")
        panels.append({"panel": panel, "parent": parent, "left": left, "right": right,
                       "source_upper": cached["value"]})
        previous = right
        if progress is not None and (len(panels) % 8 == 0 or panel == 154):
            progress("weighted_source_complete_body_panel", {
                "whole_source_body_panels_completed": len(panels),
                "whole_source_body_panels": 154,
                "distinct_source_body_parents_completed": len(parent_cache),
                "old_five_source_global_targets_recomputed": 0})
    require(previous == OUTER and len(panels) == 154 and len(parent_cache) == 152,
            "same complete body, both harmless cutoff splits, all152 original body parents")
    return panels


def _common_rows(api, panels, kernels):
    result = []
    cursor = 0
    old_seen, panel_seen = set(), set()
    old_bounds = {}
    for panel in panels:
        left, right = panel["left"], panel["right"]
        while cursor < len(kernels) and Fraction(kernels[cursor]["interval"][1]) <= left:
            cursor += 1
        index, covered = cursor, left
        while index < len(kernels) and Fraction(kernels[index]["interval"][0]) < right:
            row = kernels[index]
            lo = max(left, Fraction(row["interval"][0]))
            hi = min(right, Fraction(row["interval"][1]))
            require(covered == lo and lo < hi, "every exact closed source/kernel intersection")
            if index not in old_bounds:
                gap = api.old_interval(row["bounds"]["gap"]).lower()
                frame = saved_upper(api, row["bounds"]["frame"])
                require(api.lower(gap) > 0 and api.lower(frame) > 0,
                        "the saved whole-row true damping lower and source frame upper")
                old_bounds[index] = (gap, frame)
            gap, frame = old_bounds[index]
            factor = upper(api, frame*panel["source_upper"])
            result.append({"original_row": index, "panel": panel["panel"], "parent": panel["parent"],
                "left": lo, "right": hi, "length": exact(api, hi-lo),
                "forcing": upper(api, factor*factor), "damping": 2*gap})
            old_seen.add(index)
            panel_seen.add(panel["panel"])
            covered = hi
            if covered == right:
                break
            index += 1
        require(covered == right, "whole actual source panel intersects the whole old kernel cover")
        cursor = index
    require(len(old_seen) == 4650 and len(panel_seen) == 154
            and 4650 <= len(result) <= 4803 and len(old_bounds) == 4650
            and result[0]["left"] == CUT and result[-1]["right"] == OUTER
            and all(a["right"] == b["left"] for a, b in zip(result, result[1:])),
            "complete common refinement; no old row, source panel, seam, or endpoint omitted")
    return result


def _weighted_body_gain(api, rows, progress):
    maxima = []
    for direction, indices in (("forward", range(len(rows))),
                               ("backward", range(len(rows)-1, -1, -1))):
        value, whole = api.zero, api.zero
        count = 0
        for index in indices:
            row = rows[index]
            local, value = _step(api, value, row["forcing"], row["damping"], row["length"])
            whole = maximum(api, [whole, local])
            count += 1
            if progress is not None and (count % 256 == 0 or count == len(rows)):
                progress("weighted_source_complete_scalar_sweep", {
                    "direction": direction, "complete_common_cells": count,
                    "common_cells": len(rows), "all_bounds_are_whole_cell": True,
                    "old_unweighted_source_sweep_recomputed": False})
        require(count == len(rows), "every true cell in this complete weighted branch")
        maxima.append(whole)
    # At a fixed output radius the two input half-intervals are disjoint;
    # outputs are the two orthogonal Z branches. Thus max, not sum, applies.
    return root(api, maximum(api, maxima))


def _two_region_operator_upper(api, collar_row, body_row, collar_scale, body_scale):
    """Norm of a positive 2x2 receiving-region/source-region upper matrix."""
    first = [upper(api, collar_scale*x) for x in collar_row]
    second = [upper(api, body_scale*x) for x in body_row]
    a = upper(api, first[0]*first[0]+second[0]*second[0])
    b = upper(api, first[0]*first[1]+second[0]*second[1])
    d = upper(api, first[1]*first[1]+second[1]*second[1])
    discriminant = root(api, (a-d)*(a-d)+4*b*b)
    return root(api, (a+d+discriminant)/2)


def complete_weighted_head_response(api, km, context, admitted, base0, gh5, emit, progress=None):
    """Five genuinely new complete weighted functional/response bounds.

    The public owner admits original high summary/process reports and the
    full old natives before this call. emit saves a whole containing ball,
    rereads it, checks containment, and returns its nonnegative upper.
    It retains GH4 as a whole read-only prior result without replay.
    """
    kernels, old_order = _complete_original_row_cover(admitted, base0)
    require(gh5["kind"] == "complete_actual_GH_Hthird_source_fees_v1"
            and gh5["complete"] is True and gh5["proved"] is True
            and gh5["actual_returncode"] == 0 and gh5["saved_record_count"] == 5
            and gh5["run_id"] == "44736533396" and gh5["run_attempt"] == "1"
            and gh5["source_comparison"]["complete_five_source_rates_proved"] is True
            and gh5["reference_identity"] == context.reference_identity,
            "whole completed GH5 and same original source/reference object")
    panels = _body_source_panels(api, km, context, progress)
    rows = _common_rows(api, panels, kernels)
    weighted = _weighted_body_gain(api, rows, progress)
    saved = []

    def save(index, value):
        require(index == len(saved), "complete declared weighted output order")
        original = upper(api, value)
        reread = emit(RECORDS[index], original)
        require(reread.is_finite() and bool(reread >= original),
                "new saved whole ball has a conservative directed upper")
        saved.append(reread)
        return reread

    weighted = save(0, weighted)
    constants = base0["constants"]
    qc, rc, Bc, qb, rb, sigma = (saved_upper(api, constants[key]) for key in
        ("collar_resolvent", "collar_reflection_upper", "collar_ordinary_source_gain",
         "body_resolvent", "body_cut_reflection_upper", "interface_resolvent"))
    collar_source = upper(api,
        saved_upper(api, gh5["new_records"]["complete_centre_BHL_Hthird_collar_upper"])
        +saved_upper(api, gh5["new_records"]["complete_family_BHL_Hthird_collar_upper"]))
    # Source input order is (||x_c||_L2, ||x_b||_L2). All other original
    # ports vanish only for this homogeneous head response functional.
    X = [upper(api, sigma*qc*Bc*collar_source), upper(api, sigma*rc*qb*weighted)]
    Y = [upper(api, rb*X[0]), upper(api, rb*X[1]+qb*weighted)]
    body = [upper(api, qb*X[0]), upper(api, qb*(X[1]+weighted))]
    collar = [upper(api, qc*(Y[0]+Bc*collar_source)), upper(api, qc*Y[1])]
    outgoing = list(collar)
    reconstruction = saved_upper(api, old_order["bounds"]["raw_reconstruction_L2_multiplier"])
    collar_length = exact(api, Fraction(base0["collar_length_upper"]))
    require(Fraction(base0["collar_length_upper"]) == Fraction(9, 10**6),
            "same true-root collar reconstruction length upper")
    raw = save(1, _two_region_operator_upper(api, collar, body,
                                            3*root(api, collar_length), reconstruction))
    body_Z = save(2, hypot(api, body))
    root_Z = save(3, hypot(api, outgoing))
    outer = save(4, exact(api, Fraction(5, 388))*body_Z)
    require(len(saved) == len(RECORDS), "all five new weighted functionals saved whole")
    return {"kind": KIND, "reference_identity": context.reference_identity,
        "complete_new_record_order": list(RECORDS),
        "original_kernel_rows_consumed": 4650, "whole_source_body_panels": 154,
        "whole_original_body_parents": 152, "exact_common_refinement_cells": len(rows),
        "complete_sweep_cells": {"forward": len(rows), "backward": len(rows)},
        "all_true_body_radii_covered": True, "source_coefficient_balls_narrowed_by_refinement": False,
        "both_orthogonal_branches_and_disjoint_input_half_intervals_used": True,
        "complete_actual_head_to_high_weighted_response_proved": True,
        "whole_actual_GH_family_in_original_resolvent": True,
        "original_infinite_high_unknown_truncated": False,
        "same_full_family_mean_source_column_retained": True,
        "same_original_collar_consumed_from_saved_GH5": True,
        "same_whole_seven_port_high_reports_retained": True,
        "original_rough_ports_upgraded_to_raw_L2": False,
        "old_GH4_response_target_recomputed": False, "old_five_source_global_targets_recomputed": 0,
        "old_reference_Riccati_or_feedback_targets_recomputed": 0,
        "old_unweighted_source_sweep_recomputed": False,
        "actual_low_high_inverse_proved": False, "actual_physical_outer_rows_proved": False,
        "old_WJK_F_replaced_without_paying_difference": False,
        "original_finite_rho_bridge_proved": False, "original_seven_input_ports_proved": False,
        "either_original_RHS_proved": False, "topic_completion_proved": False,
        "private_bounds": {"weighted_body_source": weighted, "raw_L2": raw,
                           "body_Z": body_Z, "root_Z": root_Z, "outer_even": outer}}
