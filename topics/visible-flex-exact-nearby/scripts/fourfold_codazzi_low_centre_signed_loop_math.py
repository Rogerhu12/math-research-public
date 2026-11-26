"""R149: signed trace(K^2) and a weighted-body symmetric-part bound.

Pure definitions only: no imports, IO, numerical library, entry point, or
scientific execution at import.  K is exactly the R141/R142 real operator
S Gbar (Atrue-Acomp) S^-1 on ordinary dr L2 with all193 coordinates.
The original source role is mandatory.  Its root97/outer96 conditions and
mean remain; atoms are NOT appended to the Hilbert space used for K*.

A future public owner supplies an admitted complete comparison model,
directed api/km/green objects, and whole-box coefficient/local factors.
Only the new signed loop is evaluated here.  A completed old HS bound is
read as an input; it is never recomputed or used to invent the loop sign.
The owner must save/read back the complete signed trace before quantities,
then save/read back the complete new norm before admit_saved_symmetric_part.
The independent R142 resolvent adapter consumes the resulting record.
"""

N = 193
LEFT = 97
RIGHT = 96
SOURCE_ROLE = "true_coefficient_defect"
KIND = "R149_complete_weighted_body_symmetric_part_v1"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def signed_upper(value):
    require(value.is_finite(), "finite complete signed scalar")
    return value.upper()


def finite_matrix(matrix):
    return all(value.is_finite() for row in matrix.values for value in row)


def rectangular_trace(api, first, second):
    """tr(first second), without constructing the dense product."""
    require(first.cols == second.rows and first.rows == second.cols,
            "complete compatible rectangular signed trace")
    total = api.zero
    for i in range(first.rows):
        for j in range(first.cols):
            total += first.values[i][j]*second.values[j][i]
    require(total.is_finite(), "finite complete signed trace product")
    return total


def validate_model(model):
    require(model.get("comparison_BVP_verified") is True,
            "complete same comparison Green, not a trial endpoint model")
    require("private_model_token" in model, "same-model private identity")
    count = len(model["context"].domain.cells)
    require(count > 0 and len(model["generators"]) == count,
            "all original actual comparison cells")
    require(len(model["Uinv"]) == count and len(model["Vinv"]) == count,
            "both ordered full-frame carrier sequences")
    for name in ("same_WVC_reference", "same_actual_S_and_all_seven_ports",
                 "all_coefficient_pieces_and_raw_identity_transmissions",
                 "true_signed_collar_not_zero_reference_packet",
                 "ordinary_dr_pairing_and_complete_Gf_atoms"):
        require(model["context"].qualifications[name] is True,
                "original whole comparison qualification: "+name)
    return count


def panel_loop_packet(api, km, green, model, panel, cuts,
                      source_provider=None, factor_provider=None):
    """Whole-cell a,b and ordered same-cell triangle from HL.9--HL.13.

    source_provider, when supplied, is an explicit admitted object with
    source_matrix(model, whole_box, SOURCE_ROLE).  A genuine-child provider
    is allowed only because it encloses this SAME actual defect function.
    A whole source box is never treated as a constant unknown source.

    factor_provider, when supplied, is an explicit callable
    (model, whole_box, raw_source_matrix) -> {OL, OR, IL, IR}.
    It may reuse directed exponentials, but these must be the original
    full physical factors SL, SR, ell*Delta*S^-1, rho*Delta*S^-1.
    It cannot substitute Gram matrices, scalar norms, or midpoint factors.
    """
    count = validate_model(model)
    require(type(panel) is int and 0 <= panel < count, "one genuine complete cell")
    domain = model["context"].domain
    require(len(cuts) >= 2 and cuts[0] == domain.fzero
            and cuts[-1] == domain.fone
            and all(cuts[j] < cuts[j+1] for j in range(len(cuts)-1)),
            "complete exact normalized closed-subbox partition")
    length = domain.full_length(panel)
    require(length.is_finite() and api.lower(length) > 0,
            "whole positive TRUE cell length, not an upper-only mass")
    a = km.zeros(api, RIGHT, LEFT)
    b = km.zeros(api, LEFT, RIGHT)
    terms = []
    for lo, hi in zip(cuts[:-1], cuts[1:]):
        box = (panel, lo, hi)
        domain.validate_box(box)
        if source_provider is None:
            source = green.source_matrix(api, km, model, box, SOURCE_ROLE)
        else:
            source = source_provider.source_matrix(model, box, SOURCE_ROLE)
        require(source.shape == (N, N) and finite_matrix(source),
                "whole193 same weighted-body defect source including mean")
        if factor_provider is None:
            factors = green.local_factors(api, km, model, box, source)
        else:
            factors = factor_provider(model, box, source)
        for key, shape in (("OL", (N, LEFT)), ("OR", (N, RIGHT)),
                           ("IL", (LEFT, N)), ("IR", (RIGHT, N))):
            require(factors[key].shape == shape and finite_matrix(factors[key]),
                    "whole signed original factor: "+key)
        # At each actual point: IR*OL=rho*Delta*L and IL*OR=ell*Delta*R.
        # The common S factors cancel in the mathematical definition.
        A = km.multiply(api, factors["IR"], factors["OL"])
        B = km.multiply(api, factors["IL"], factors["OR"])
        require(finite_matrix(A) and finite_matrix(B),
                "complete same-point signed cross matrices")
        mass = length*domain.exact(hi-lo)
        require(mass.is_finite() and api.lower(mass) > 0,
                "whole signed ordinary-dr mass retains true root length")
        a = km.add(api, a, km.scale(api, mass, A))
        b = km.add(api, b, km.scale(api, mass, B))
        terms.append((mass, A, B))

    triangle = api.zero
    for earlier, (mass_s, A, _) in enumerate(terms):
        # Both arguments range over this whole closed subbox.  Its ordered
        # triangle has exactly half the true square area; Delta may vary.
        triangle += (mass_s*mass_s/2)*rectangular_trace(
            api, A, terms[earlier][2])
        for later in range(earlier+1, len(terms)):
            mass_r, _, B = terms[later]
            triangle += (mass_s*mass_r)*rectangular_trace(api, A, B)
    require(triangle.is_finite() and finite_matrix(a) and finite_matrix(b),
            "complete signed ordinary-dr integrals")
    return {
        "panel": panel,
        "source_role": SOURCE_ROLE,
        "private_model_token": model["private_model_token"],
        "a_source_earlier": a,
        "b_output_later": b,
        "same_cell_ordered_loop_integral": triangle,
        "complete_subboxes": len(terms),
        "whole_closed_source_boxes_used": True,
        "signed_true_dr_masses_used": True,
        "same_cell_ordered_triangle_complete": True,
        "actual_coefficient_variation_retained": True,
        "mean_and_all_193_components_retained": True,
    }


def complete_loop_trace(api, km, model, packets):
    """Stream all cells; no unfinished prefix is a complete trace target.

    X is RIGHT by LEFT.  C=Uinv and D=Vinv appear in their exact order:
    X_next = D*(X+a)*C.  Only the current cell's private packet is needed.
    Returned signed scalars are complete real interval balls.  They are
    not absolute values, PSD majorants, or selected-point quadratures.
    """
    expected = validate_model(model)
    X = km.zeros(api, RIGHT, LEFT)
    loop = api.zero
    completed = subboxes = 0
    for packet in packets:
        require(completed < expected and packet["panel"] == completed,
                "complete ordered cells with no duplicate or omitted interval")
        require(packet["source_role"] == SOURCE_ROLE
                and packet["private_model_token"] is model["private_model_token"],
                "same full defect operator and comparison model")
        for key in ("whole_closed_source_boxes_used", "signed_true_dr_masses_used",
                    "same_cell_ordered_triangle_complete",
                    "actual_coefficient_variation_retained",
                    "mean_and_all_193_components_retained"):
            require(packet[key] is True, "whole signed packet qualification: "+key)
        a, b = packet["a_source_earlier"], packet["b_output_later"]
        require(a.shape == (RIGHT, LEFT) and b.shape == (LEFT, RIGHT),
                "complete original97/96 rectangular cross moments")
        loop += rectangular_trace(api, X, b)+packet["same_cell_ordered_loop_integral"]
        subboxes += packet["complete_subboxes"]
        completed += 1
        if completed < expected:
            i = completed-1
            X = km.product(api, model["Vinv"][i], km.add(api, X, a),
                           model["Uinv"][i])
            require(finite_matrix(X), "complete finite signed loop carrier")
    require(completed == expected and subboxes >= expected,
            "every original cell and both same-cell Green branches are complete")
    require(loop.is_finite(), "finite complete whole-domain ordered loop")
    trace_square = -2*loop
    require(trace_square.is_finite(), "finite complete signed trace(K^2)")
    return {
        "source_role": SOURCE_ROLE,
        "private_model_token": model["private_model_token"],
        "complete_signed_trace_of_square": True,
        "complete_cells": completed,
        "complete_subboxes": subboxes,
        "complete_ordered_loop_ball": loop,
        "complete_trace_square_ball": trace_square,
        "same_weighted_body_K": True,
        "same_real_193_ordinary_dr_Hilbert_space": True,
        "all_original_mean_and_boundary_coordinates_retained": True,
        "old_HS_target_recomputed": False,
    }


def coercivity_quantities(api, defect_norm, saved_loop, whole_saved_trace):
    """HL.3 using only a completed old HS upper and a new saved loop ball.

    The owner has already saved/read back complete_trace_square_ball and
    rebound its whole artifact to this model/source before calling.
    body_HS2_upper must have its ORIGINAL HS meaning, not merely be the
    square of an unrelated operator-norm estimate.
    No inverse or strict gate is granted by this function.
    """
    require(defect_norm["source_role"] == SOURCE_ROLE
            and saved_loop["source_role"] == SOURCE_ROLE
            and defect_norm["private_model_token"] is saved_loop["private_model_token"],
            "the old HS certificate and new trace concern exactly the same K")
    require(saved_loop["complete_signed_trace_of_square"] is True
            and saved_loop["same_weighted_body_K"] is True
            and saved_loop["same_real_193_ordinary_dr_Hilbert_space"] is True
            and saved_loop["all_original_mean_and_boundary_coordinates_retained"] is True
            and saved_loop["old_HS_target_recomputed"] is False,
            "the genuinely complete new signed trace and unchanged old target")
    old_hs2 = signed_upper(defect_norm["body_HS2_upper"])
    require(api.lower(old_hs2) >= 0, "complete old nonnegative HS-square upper")
    require(whole_saved_trace.is_finite()
            and whole_saved_trace.contains(saved_loop["complete_trace_square_ball"]),
            "entire completed signed trace is contained in saved/read-back ball")
    trace = whole_saved_trace
    trace_upper = signed_upper(trace)
    square_upper = signed_upper((old_hs2+trace_upper)/2)
    require(api.lower(square_upper) >= 0,
            "inconsistent enclosure: old HS upper plus trace upper is negative")
    norm_upper = signed_upper(api.sqrt(square_upper))
    require(api.lower(norm_upper) >= 0, "complete nonnegative symmetric-part norm")
    return {
        "source_role": SOURCE_ROLE,
        "private_model_token": saved_loop["private_model_token"],
        "complete_signed_trace_of_square": True,
        "complete_cells": saved_loop["complete_cells"],
        "complete_subboxes": saved_loop["complete_subboxes"],
        "old_body_HS2_upper": old_hs2,
        "complete_trace_square_ball": trace,
        "symmetric_part_HS2_upper": square_upper,
        "symmetric_part_norm_upper": norm_upper,
        "same_weighted_body_K": True,
        "same_real_193_ordinary_dr_Hilbert_space": True,
        "whole_saved_trace_readback_used": True,
    }


def admit_saved_symmetric_part(api, quantities, whole_saved_norm):
    """Bind the NEW complete saved/read-back norm; the binder checks theta<1.

    whole_saved_norm is the owner's decoded complete decimal ball from
    its new result file.  It must contain the entire computed directed
    upper, not only a displayed midpoint.  This routine does not perform IO.
    The independent R142 same-model symmetric-part resolvent adapter
    derives its own positive gap and resolvent upper from this record.
    """
    require(quantities["source_role"] == SOURCE_ROLE
            and quantities["complete_signed_trace_of_square"] is True
            and quantities["same_weighted_body_K"] is True
            and quantities["same_real_193_ordinary_dr_Hilbert_space"] is True
            and quantities["whole_saved_trace_readback_used"] is True,
            "complete same-Hilbert-space symmetric-part quantity")
    require(whole_saved_norm.is_finite()
            and whole_saved_norm.contains(quantities["symmetric_part_norm_upper"]),
            "entire computed symmetric-part upper is contained in saved ball")
    theta = signed_upper(whole_saved_norm)
    require(api.lower(theta) >= 0, "saved whole nonnegative symmetric-part upper")
    result = dict(quantities)
    result.update({
        "kind": KIND,
        "symmetric_part_norm_upper": theta,
        "complete_symmetric_part_norm_ball": whole_saved_norm,
        "whole_saved_norm_readback_used": True,
    })
    return result
