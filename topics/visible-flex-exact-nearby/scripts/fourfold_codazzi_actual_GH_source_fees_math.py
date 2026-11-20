"""Five new complete source rates for the true given-head high inverse.

Pure definitions.  No numerical import, file access, old producer entry,
low inverse, Green action, or successful prior bound is evaluated here.
The original base0 and negative-one high reports are retained in full;
only finite pointwise centre/family source coefficients are new targets.
"""

N = 193
HEAD = tuple((0, j) for j in range(1, 97))+((1, 0),)+tuple((1, j) for j in range(1, 97))
HIGH0 = tuple((0, j) for j in range(97, 161))+tuple((1, j) for j in range(97, 161))
REPAIR_SHA = "440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
DIRECTION_SHA = "6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
BASE0_INPUTS = ["root_stable_Z_port", "collar_ordinary_Hthird_source",
    "body_ordinary_Hthird_source", "body_outer_mean_head_and_weighted_jumps",
    "collar_weighted_affine_jumps", "cut_stable_Z_jump", "cut_unstable_Z_jump"]
NEGATIVE_INPUTS = ["root_stable_Y_port", "collar_ordinary_Hminus2over3_source",
    "body_ordinary_Hminus2over3_source", "body_outer_mean_head_and_Y_weighted_jumps",
    "collar_Y_weighted_affine_jumps", "cut_stable_Y_jump", "cut_unstable_Y_jump"]


def require(ok, message):
    if not ok:
        raise ValueError(message)


def upper(api, value):
    require(value.is_finite(), "complete finite directed value")
    point = value.upper()
    require(api.lower(point) >= 0, "nonnegative true upper endpoint")
    return point


def maximum(api, values):
    require(values, "nonempty complete region")
    return upper(api, api.hull([upper(api, value) for value in values]))


def admit_original_high_reports(base0, base_process, negative, negative_process,
                                base_spec, negative_spec):
    """Metadata only, before flint; complete source/port rows are never copied partially."""
    for report, process, spec, kind, run, inputs in (
        (base0, base_process, base_spec,
         "actual_full_real_delta_root_to_regular_given_head_high_graph_v1",
         "43617150971", BASE0_INPUTS),
        (negative, negative_process, negative_spec,
         "actual_full_real_delta_negative_one_positive_given_head_graph_v1",
         "43627228225", NEGATIVE_INPUTS)):
        require(report["kind"] == kind and report["complete"] is True and report["failure"] is None
                and report["derived_definition_sha256"] == REPAIR_SHA
                and report["explicit_direction_definition_sha256"] == DIRECTION_SHA
                and report["exact_real_delta_radius"] == "1/100000000"
                and report["input_order"] == inputs
                and report["given_complete_head_positive_high_inverse_and_root_graph_proved"] is True
                and report["full_low_high_Schur_inverse_proved"] is False
                and report["complete_infinite_BVP_inverse_proved"] is False,
                "whole original same-family given-head high report and its precise false scope")
        require(process["complete"] is True and process["run_id"] == run
                and process["run_attempt"] == "1"
                and process["repository"] == "Rogerhu12/math-research-public"
                and process["all_pinned_inputs_verified"] is True
                and process["actual_complete_source_columns"] == 7
                and len(process["children"]) == 1
                and process["children"][0]["actual_returncode"] == 0
                and process["complete_native_sha256"] == report["native_sha256"]
                and process["actual_original_small_input_sha256"] == report["input_sha256"],
                "entire original successful high process and actual native/source receipts")
        matching = [item for item in process["native_files"]
                    if item["file"] == "evidence/"+spec["path"].split("/")[-1]]
        require(len(matching) == 1 and matching[0]["bytes"] == spec["bytes"]
                and matching[0]["sha256"] == spec["sha256"],
                "old process identifies exactly this whole saved high report")
        require(all(isinstance(row, list) and len(row) == 7
                    for row in report["response_rows"].values()),
                "all original seven source columns in every complete response row")
    for name in ("original_collar_native_sha256", "original_complete_body_native_sha256",
                 "original_complete_outer_native_sha256", "entire_positive_interval", "fixed_body_cut"):
        require(base0[name] == negative[name], "same actual high operator in both windows: "+name)
    require(negative["negative_one_source_window_proved"] is True
            and negative["complete_negative_order_physical_outer_graph_proved"] is True
            and "entire_positive_raw_L2" in base0["response_rows"]
            and "entire_positive_raw_L2r_Hminus1" in negative["response_rows"],
            "strong finite internal source and original rough external windows remain distinct")
    require(len(negative["exterior_mean_input_order"]) == len(negative["exterior_mean_output_coefficients"])
            and len(negative["exterior_input_order"]) == len(negative["exterior_affine_Y_output_coefficients"]),
            "all true exterior affine and independent mean columns retained")


def complete_source_fees(api, km, context, progress=None):
    """All155 whole panels; exactly five scalar outputs, no DeltaAL target.

    Output order: centre collar/body H^(1/3), full family difference
    collar/body H^(1/3), full Delta B_LH raw L2.  Every source is a
    pointwise map on the same physical head after exactly one S inverse.
    """
    require(len(context.domain.cells) == 155 and len(context.parent_indices) == 155
            and set(context.parent_indices) == set(range(153)),
            "complete original coefficient cover")
    weights = [upper(api, api.rational(1+16*j*j)**api.rational(1, 6)) for _, j in HIGH0]
    family_weight = upper(api, api.rational(1+16*288*288)**api.rational(1, 6))
    centre = {"collar": [], "body": []}
    family = {"collar": [], "body": []}
    returned = []
    mean_zeros = 0
    for panel in range(155):
        box = context.domain.whole_cell_box(panel)
        matrix = context.centre_matrix(HIGH0, HEAD, box)
        require(matrix.shape == (128, N), "complete signed normalized real source matrix")
        require(all(row[96].lower() == 0 and row[96].upper() == 0 for row in matrix.values),
                "centre pure mean to high zero proved by exact degree32 support")
        mean_zeros += 1
        q = context.reference_qs[panel]
        require(api.lower(q) > 0, "same positive original body weight")
        weighted = km.Matrix(128, N,
            [[weights[i]*value/(q if HEAD[j][0] == 1 else api.one)
              for j, value in enumerate(row)] for i, row in enumerate(matrix.values)])
        region = "collar" if context.parent_indices[panel] == 0 else "body"
        centre[region].append(upper(api, km.matrix_norm_upper(api, weighted)))
        sinverse = maximum(api, [api.one, api.one/q])
        family[region].append(upper(api,
            family_weight*upper(api, context.family_fees["HL"][panel])*sinverse))
        returned.append(upper(api, context.family_fees["LH"][panel]))
        if progress is not None and (panel % 8 == 7 or panel == 154):
            progress("complete_actual_GH_source_coefficients", {
                "comparison_panels_complete": panel+1, "comparison_panels": 155,
                "complete_original_parents": 153, "new_scalar_targets": 5,
                "old_bound_targets_recomputed": 0, "DeltaAL_source_target_evaluated": False})
    require(mean_zeros == 155 and all(centre[key] and family[key] for key in centre),
            "both full radial regions and all complete mean columns")
    return [maximum(api, centre["collar"]), maximum(api, centre["body"]),
            maximum(api, family["collar"]), maximum(api, family["body"]),
            maximum(api, returned)]
