"""R141: directed two-sided low193 Green and complete-observation Gram math.

No entry point, IO, numerical import or scientific work at import.  The
caller supplies the already-admitted WVC context, exact dyadic comparison
generators and exact dyadic chart proposals.  Proposals are not evidence:
all inverses/exponentials below use the owner's directed Arb API.  The
actual coefficient ball, true panel length and all193 output atoms remain.

Here "actual low" means the true varying WVC signed centre A_L^c: its
principal eta is the original full-family eta and its lower coefficients
are those of the repaired centre.  It is not silently DF(Q_repair).
This certifies only that continuous low193 mixed-boundary problem
when its strict returned residual condition is proved.  CFB, actual high
families, independent outer columns, the finite rho bridge and both full
original right sides are not thereby certified.  All evaluations belong in
a separately frozen public own-Actions owner, never in a local import test.
"""

HEAD = (tuple((0, j) for j in range(1, 97)) + ((1, 0),)
        + tuple((1, j) for j in range(1, 97)))
HIGH0 = tuple((0, j) for j in range(97, 161)) + tuple((1, j) for j in range(97, 161))
N = 193
P = 97
Q = 96


def require(ok, message):
    if not ok:
        raise ValueError(message)


def positive_upper(api, value):
    require(value.is_finite(), "finite directed bound")
    result = value.upper()
    require(api.lower(result) >= 0, "nonnegative mathematical upper")
    return result


def maximum_upper(api, values):
    require(values, "nonempty complete bound list")
    return positive_upper(api, api.hull([positive_upper(api, x) for x in values]))


def submatrix(km, matrix, rows, cols):
    return km.Matrix(len(rows), len(cols),
                     [[matrix.values[i][j] for j in cols] for i in rows])


def columns(km, matrix, cols):
    return submatrix(km, matrix, tuple(range(matrix.rows)), tuple(cols))


def rows(km, matrix, indices):
    return submatrix(km, matrix, tuple(indices), tuple(range(matrix.cols)))


def directed_inverse(api, km, matrix):
    require(matrix.rows == matrix.cols and matrix.rows > 0, "whole square inverse")
    value = api.arb_mat(matrix.values).inv()
    result = km.Matrix(matrix.rows, matrix.cols,
                       [[value[i, j] for j in range(matrix.cols)] for i in range(matrix.rows)])
    require(all(x.is_finite() for row in result.values for x in row),
            "directed inverse must be certified, never NaN or a pseudoinverse")
    return result


def directed_exp(api, km, generator, parameter):
    require(generator.shape == (N, N) and parameter.is_finite(), "complete local generator")
    if parameter.lower() == 0 and parameter.upper() == 0:
        return km.eye(api, N)
    scaled = km.scale(api, parameter, generator)
    value = api.arb_mat(scaled.values).exp()
    result = km.Matrix(N, N, [[value[i, j] for j in range(N)] for i in range(N)])
    require(all(x.is_finite() for row in result.values for x in row),
            "whole directed matrix exponential finite")
    return result


def congruence(api, km, left, middle):
    return km.product(api, left, middle, km.transpose(left))


def source_gram(api, km, matrix):
    return km.multiply(api, matrix, km.transpose(matrix))


def output_gram(api, km, matrix):
    return km.multiply(api, km.transpose(matrix), matrix)


def trace_product(api, left, right):
    require(left.rows == left.cols == right.rows == right.cols,
            "whole same-size covariance trace")
    n = left.rows
    if hasattr(api, "matrix_product"):
        first = [[left.values[i][j] for i in range(n) for j in range(n)]]
        second = [[right.values[j][i]] for i in range(n) for j in range(n)]
        return api.matrix_product(first, second)[0][0]
    return sum((left.values[i][j]*right.values[j][i]
                for i in range(n) for j in range(n)), api.zero)


def psd_operator_upper(api, matrix):
    """Gershgorin upper for a matrix already proved PSD by its Gram origin."""
    require(matrix.rows == matrix.cols, "whole PSD matrix")
    values = []
    for i, row in enumerate(matrix.values):
        value = row[i].upper() + sum((api.magnitude(x) for j, x in enumerate(row) if j != i), api.zero)
        values.append(positive_upper(api, value))
    return maximum_upper(api, values)


def operator_upper(api, km, matrix):
    return positive_upper(api, api.sqrt(psd_operator_upper(api, output_gram(api, km, matrix))))


def _install_exact_boundary_columns(api, km, proposal, first=False, last=False):
    require(proposal.shape == (N, N), "whole193 chart proposal")
    require(all(x.lower() == x.upper() for row in proposal.values for x in row),
            "proposal entries are exact dyadics, not independently uncertain coefficients")
    value = [list(row) for row in proposal.values]
    if first:
        for i in range(N):
            for j in range(P):
                value[i][j] = api.one if i == j else api.zero
    if last:
        p0 = api.rational(13, 80)
        for i in range(N):
            for j in range(Q):
                value[i][P+j] = (-p0 if i == j else
                                 api.one if i == 97+j else api.zero)
    return km.Matrix(N, N, value)


def build_comparison_model(api, km, context, generators, chart_proposals, progress=None):
    """Verified local charts; no full unstable fundamental matrix is formed.

    generators[i] is the exact constant normalized generator H_i^0, not an
    enclosure of the actual varying A_L.  The physical comparison generator
    is H_i^0/h_i with the TRUE h_i.  There is one whole original comparison
    panel per generator in this first adapter; a refined adapter must retain
    its exact parent/coordinate map rather than silently changing the domain.
    """
    count = len(context.domain.cells)
    require(len(generators) == count and len(chart_proposals) == count+1,
            "complete same-domain comparison arrays")
    require(all(g.shape == (N, N) and all(x.lower() == x.upper() for row in g.values for x in row)
                for g in generators), "exact dyadic normalized model generators")
    require(context.qualifications.get("same_WVC_reference") is True
            and context.qualifications.get("ordinary_dr_pairing_and_complete_Gf_atoms") is True,
            "same full WVC source and observation coordinates")
    charts = [_install_exact_boundary_columns(api, km, t, i == 0, i == count)
              for i, t in enumerate(chart_proposals)]
    inverses = [directed_inverse(api, km, t) for t in charts]
    forward, backward = [], []
    for i, generator in enumerate(generators):
        forward.append(km.product(api, inverses[i+1], directed_exp(api, km, generator, api.one), charts[i]))
        # exp(-H) avoids inverting an ill-conditioned complete exp(+H).
        backward.append(km.product(api, inverses[i], directed_exp(api, km, generator, -api.one), charts[i+1]))
        if progress is not None:
            progress("verified_comparison_transfer", {"panels_complete": i+1, "panels": count})
    ix, iy = tuple(range(P)), tuple(range(P, N))
    Z = [km.zeros(api, Q, P)]
    Uinv = []
    for transfer in forward:
        aa = submatrix(km, transfer, ix, ix)
        ab = submatrix(km, transfer, ix, iy)
        ba = submatrix(km, transfer, iy, ix)
        bb = submatrix(km, transfer, iy, iy)
        inverse = directed_inverse(api, km, km.add(api, aa, km.multiply(api, ab, Z[-1])))
        Uinv.append(inverse)
        Z.append(km.multiply(api, km.add(api, ba, km.multiply(api, bb, Z[-1])), inverse))
    Y = [None for _ in range(count)] + [km.zeros(api, P, Q)]
    Vinv = [None for _ in range(count)]
    for i in range(count-1, -1, -1):
        transfer = backward[i]
        aa = submatrix(km, transfer, ix, ix)
        ab = submatrix(km, transfer, ix, iy)
        ba = submatrix(km, transfer, iy, ix)
        bb = submatrix(km, transfer, iy, iy)
        inverse = directed_inverse(api, km, km.add(api, km.multiply(api, ba, Y[i+1]), bb))
        Vinv[i] = inverse
        Y[i] = km.multiply(api, km.add(api, km.multiply(api, aa, Y[i+1]), ab), inverse)
    nodes = []
    for i in range(count+1):
        joint = km.vcat(km.hcat(km.eye(api, P), Y[i]), km.hcat(Z[i], km.eye(api, Q)))
        frame = km.multiply(api, charts[i], joint)
        inverse = directed_inverse(api, km, frame)
        nodes.append({"left": columns(km, frame, ix), "right": columns(km, frame, iy),
                      "ell": rows(km, inverse, ix), "rho": rows(km, inverse, iy)})
    root_atoms = rows(km, nodes[0]["left"], tuple(range(P)))
    outer_values = rows(km, nodes[-1]["right"], tuple(range(97, N)))
    outer_atoms = km.Matrix(Q, Q, [
        [context.reference_thetas[j+1]*value for value in row]
        for j, row in enumerate(outer_values.values)])
    return {"context": context, "generators": generators, "nodes": nodes,
            "Uinv": Uinv, "Vinv": Vinv, "root_atoms": root_atoms, "outer_atoms": outer_atoms,
            "comparison_BVP_verified": True, "actual_low_BVP_verified": False,
            "reference_identity": context.reference_identity,
            "private_model_token": object()}


def physical_weight(api, km, model, panel, inverse=False):
    q = model["context"].reference_qs[panel]
    require(api.lower(q) > 0, "actual positive fixed WVC S weight")
    factors = [api.one if component == 0 else (api.one/q if inverse else q)
               for component, _ in HEAD]
    return km.Matrix(N, N, [[factors[i] if i == j else api.zero for j in range(N)] for i in range(N)])


def local_factors(api, km, model, box, source_matrix):
    context = model["context"]
    context.domain.validate_box(box)
    i, lo, hi = box
    tau = api.interval(context.domain.exact(lo), context.domain.exact(hi))
    plus = directed_exp(api, km, model["generators"][i], tau)
    minus = directed_exp(api, km, model["generators"][i], -tau)
    node = model["nodes"][i]
    S = physical_weight(api, km, model, i)
    require(source_matrix.rows == N, "whole raw source matrix")
    return {
        "OL": km.product(api, S, plus, node["left"]),
        "OR": km.product(api, S, plus, node["right"]),
        "IL": km.product(api, node["ell"], minus, source_matrix),
        "IR": km.product(api, node["rho"], minus, source_matrix),
    }


def source_matrix(api, km, model, box, role):
    """Explicit local source units; the high nonlocal feedback is not local W."""
    context = model["context"]
    i = context.domain.cell_index(box)
    if role == "ordinary_raw_low_source":
        return km.eye(api, N)
    if role == "transformed_low_source":
        return physical_weight(api, km, model, i, inverse=True)
    actual = context.centre_matrix(HEAD, HEAD, box)
    Sinv = physical_weight(api, km, model, i, inverse=True)
    if role == "true_coefficient_defect":
        length = context.domain.full_length(i)
        require(api.lower(length) > 0, "whole true panel length")
        difference = km.add(api, actual, km.scale(api, -api.one/length, model["generators"][i]))
        return km.multiply(api, difference, Sinv)
    if role == "low_second_kind_correction":
        eta, q = context.reference_etas[i], context.reference_qs[i]
        diagonal = context.reference_diagonals[i]
        reference = []
        for oc, j in HEAD:
            row = []
            for ic, k in HEAD:
                value = api.zero
                if j == k and j:
                    if oc != ic:
                        value = 4*j*eta*(q*q if oc == 0 else api.one)
                    else:
                        value = diagonal[j] if oc == 0 else -diagonal[j]
                row.append(value)
            reference.append(row)
        return km.multiply(api, km.add(api, actual, km.scale(api, -api.one, km.Matrix(N, N, reference))), Sinv)
    if role == "centre_high0_return_source":
        return context.centre_matrix(HEAD, HIGH0, box)
    raise ValueError("undeclared complete source role: " + str(role))


def panel_gram_packet(api, km, model, panel, cuts, source_role):
    """Whole-box integrals and both same-panel triangles; no sampled values.

    The cuts are exact fractions in [0,1] with both endpoints and strict
    increase.  Every integration box is evaluated on its whole continuum.
    All returned arrays are private inputs to a small complete norm result.
    """
    domain = model["context"].domain
    require(len(cuts) >= 2 and cuts[0] == domain.fzero and cuts[-1] == domain.fone
            and all(cuts[j] < cuts[j+1] for j in range(len(cuts)-1)),
            "one exact complete normalized panel partition")
    terms = []
    totals = {"IL": km.zeros(api, P, P), "IR": km.zeros(api, Q, Q),
              "OL": km.zeros(api, P, P), "OR": km.zeros(api, Q, Q)}
    length = domain.full_length(panel)
    for lo, hi in zip(cuts[:-1], cuts[1:]):
        box = (panel, lo, hi)
        factors = local_factors(api, km, model, box, source_matrix(api, km, model, box, source_role))
        grams = {"IL": source_gram(api, km, factors["IL"]),
                 "IR": source_gram(api, km, factors["IR"]),
                 "OL": output_gram(api, km, factors["OL"]),
                 "OR": output_gram(api, km, factors["OR"])}
        mass = length*domain.exact(hi-lo)
        require(api.lower(mass) > 0, "genuine positive ordinary-dr subbox mass")
        for name in totals:
            totals[name] = km.add(api, totals[name], km.scale(api, mass, grams[name]))
        terms.append({"mass_upper": positive_upper(api, mass), "grams": grams})
    triangle_left = api.zero
    triangle_right = api.zero
    for i, out in enumerate(terms):
        for j, source in enumerate(terms):
            if i < j:
                triangle_left += out["mass_upper"]*source["mass_upper"]*positive_upper(
                    api, trace_product(api, out["grams"]["OL"], source["grams"]["IL"]))
            elif i > j:
                triangle_right += out["mass_upper"]*source["mass_upper"]*positive_upper(
                    api, trace_product(api, out["grams"]["OR"], source["grams"]["IR"]))
            else:
                half_square = out["mass_upper"]*out["mass_upper"]/2
                triangle_left += half_square*positive_upper(
                    api, trace_product(api, out["grams"]["OL"], source["grams"]["IL"]))
                triangle_right += half_square*positive_upper(
                    api, trace_product(api, out["grams"]["OR"], source["grams"]["IR"]))
    return {"panel": panel, "source_role": source_role, "totals": totals,
            "private_model_token": model["private_model_token"],
            "same_panel_left_HS2_upper": positive_upper(api, triangle_left),
            "same_panel_right_HS2_upper": positive_upper(api, triangle_right),
            "complete_subboxes": len(terms)}


def require_complete_packets(model, packets, role=None):
    count = len(model["generators"])
    require(count > 0 and len(packets) == count
            and all(p["panel"] == i for i, p in enumerate(packets))
            and len({p["source_role"] for p in packets}) == 1
            and all(p["private_model_token"] is model["private_model_token"] for p in packets),
            "all panels of one source and the same verified comparison model")
    require(role is None or packets[0]["source_role"] == role,
            "the declared complete source role")
    return count


def complete_gram_norm(api, km, model, packets):
    """Complete body + root97 + outer96 Hilbert-Schmidt upper, O(M) states."""
    count = require_complete_packets(model, packets)
    left_body = [km.zeros(api, P, P)]
    right_body = [None for _ in range(count)] + [km.zeros(api, Q, Q)]
    for i, packet in enumerate(packets):
        left_body.append(congruence(api, km, km.transpose(model["Uinv"][i]),
                                    km.add(api, left_body[-1], packet["totals"]["OL"])))
    for i in range(count-1, -1, -1):
        right_body[i] = km.add(api, packets[i]["totals"]["OR"],
            congruence(api, km, km.transpose(model["Vinv"][i]), right_body[i+1]))
    root_carry = output_gram(api, km, model["root_atoms"])
    outer_carries = [None for _ in range(count)] + [output_gram(api, km, model["outer_atoms"])]
    for i in range(count-1, -1, -1):
        outer_carries[i] = congruence(api, km, km.transpose(model["Vinv"][i]), outer_carries[i+1])
    body_HS2 = root_HS2 = outer_HS2 = api.zero
    for i, packet in enumerate(packets):
        integral = packet["totals"]
        next_right = congruence(api, km, km.transpose(model["Vinv"][i]), right_body[i+1])
        body_HS2 += positive_upper(api, trace_product(api, left_body[i], integral["IL"]))
        body_HS2 += positive_upper(api, trace_product(api, next_right, integral["IR"]))
        body_HS2 += packet["same_panel_left_HS2_upper"] + packet["same_panel_right_HS2_upper"]
        root_HS2 += positive_upper(api, trace_product(api, root_carry, integral["IL"]))
        outer_HS2 += positive_upper(api, trace_product(api, outer_carries[i], integral["IR"]))
        root_carry = congruence(api, km, km.transpose(model["Uinv"][i]), root_carry)
    body_HS2, root_HS2, outer_HS2 = (positive_upper(api, x) for x in (body_HS2, root_HS2, outer_HS2))
    return {"source_role": packets[0]["source_role"],
            "private_model_token": model["private_model_token"],
            "body_HS2_upper": body_HS2, "root97_HS2_upper": root_HS2,
            "outer96_HS2_upper": outer_HS2,
            "body_norm_upper": positive_upper(api, api.sqrt(body_HS2)),
            "atoms193_norm_upper": positive_upper(api, api.sqrt(root_HS2+outer_HS2)),
            "complete_norm_upper": positive_upper(api, api.sqrt(body_HS2+root_HS2+outer_HS2)),
            "private_output_left_covariances": left_body,
            "private_output_right_covariances": right_body}


def source_covariances(api, km, model, packets):
    """Private point-receiver data; exact same directed source Gram integrals."""
    count = require_complete_packets(model, packets)
    left = [None for _ in range(count)] + [km.zeros(api, P, P)]
    right = [km.zeros(api, Q, Q)]
    for i in range(count-1, -1, -1):
        left[i] = km.add(api, packets[i]["totals"]["IL"],
                         congruence(api, km, model["Uinv"][i], left[i+1]))
    for i in range(count):
        right.append(congruence(api, km, model["Vinv"][i],
                                 km.add(api, right[-1], packets[i]["totals"]["IR"])))
    return {"left": left, "right": right,
            "source_role": packets[0]["source_role"],
            "private_model_token": model["private_model_token"]}


def actual_low_source_bound(api, defect_norm, source_norm):
    """Explicit true-coefficient lift, retaining all output atoms separately."""
    require(defect_norm["source_role"] == "true_coefficient_defect", "complete actual low defect")
    require(defect_norm["private_model_token"] is source_norm["private_model_token"],
            "actual defect and source norms use the same comparison model")
    epsilon = defect_norm["body_norm_upper"]
    passed = bool(epsilon < api.one)
    result = {"strict_low_coefficient_residual_passed": passed,
              "comparison_defect_body_upper": epsilon,
              "coefficient_object": "same_true_varying_WVC_hybrid_low_signed_centre",
              "high_feedback_or_full_positive_inverse_proved": False,
              "original_finite_Qf_rho_bridge_proved": False,
              "source_role": source_norm["source_role"]}
    if not passed:
        return result
    gap = (api.one-epsilon).lower()
    require(api.lower(gap) > 0, "strict directed actual low gap")
    body = positive_upper(api, source_norm["body_norm_upper"]/gap)
    atoms = positive_upper(api, source_norm["atoms193_norm_upper"]
                           + defect_norm["atoms193_norm_upper"]*body)
    result.update({"actual_low_BVP_proved": True, "gap_lower": gap,
                   "actual_body_norm_upper": body, "actual_atoms193_norm_upper": atoms,
                   "actual_complete_source_norm_upper": positive_upper(api, api.sqrt(body*body+atoms*atoms))})
    if source_norm["source_role"] == "low_second_kind_correction":
        result["actual_low_second_kind_inverse_upper"] = positive_upper(api,
            (api.sqrt((2+body)*(2+body)+atoms*atoms)+api.sqrt(body*body+atoms*atoms))/2)
    return result


def whole_box_projection_bound(api, km, model, panel, box, defect_packets,
                               defect_source_covariances, body_output_norm, epsilon):
    """Quantitative TRUE whole-box transversality after the strict low gate.

    Full local covariance integrals dominate their partial integrals in PSD
    order.  Thus this enclosure covers every point of box, not its endpoints.
    It is a separate point-receiver bound; an L2 input trace is never read.
    """
    require(bool(epsilon < api.one) and box[0] == panel, "strict whole actual low coefficient gate")
    require_complete_packets(model, defect_packets, "true_coefficient_defect")
    require(defect_source_covariances["source_role"] == "true_coefficient_defect"
            and body_output_norm["source_role"] == "true_coefficient_defect"
            and defect_source_covariances["private_model_token"] is model["private_model_token"]
            and body_output_norm["private_model_token"] is model["private_model_token"]
            and bool(epsilon >= body_output_norm["body_norm_upper"]),
            "point certificate consumes the same complete actual-defect upper")
    Sinv = physical_weight(api, km, model, panel, inverse=True)
    factors = local_factors(api, km, model, box, Sinv)
    totals = defect_packets[panel]["totals"]
    left_source = defect_source_covariances["left"][panel]
    right_source = km.add(api, defect_source_covariances["right"][panel], totals["IR"])
    receiver_gram = km.add(api, congruence(api, km, factors["OL"], left_source),
                          congruence(api, km, factors["OR"], right_source))
    receiver = positive_upper(api, api.sqrt(psd_operator_upper(api, receiver_gram)))
    # Output covariances depend only on S and the model; the source role used
    # to obtain them is irrelevant.  They include body only, no atom terms.
    left_output = km.add(api, body_output_norm["private_output_left_covariances"][panel], totals["OL"])
    right_output = body_output_norm["private_output_right_covariances"][panel]
    column_gram = km.add(api,
        congruence(api, km, km.transpose(factors["IL"]), left_output),
        congruence(api, km, km.transpose(factors["IR"]), right_output))
    column = positive_upper(api, api.sqrt(psd_operator_upper(api, column_gram)))
    left_projection = km.multiply(api, factors["OL"], factors["IL"])
    right_projection = km.multiply(api, factors["OR"], factors["IR"])
    model_projection = maximum_upper(api, [operator_upper(api, km, left_projection),
                                          operator_upper(api, km, right_projection)])
    total = positive_upper(api, model_projection + receiver*column/(api.one-epsilon).lower())
    q = model["context"].reference_qs[panel]
    Sbound = maximum_upper(api, [api.one, q])
    Sinvbound = maximum_upper(api, [api.one, api.one/q])
    raw_projection = positive_upper(api, Sbound*Sinvbound*total)
    angle = (api.one/(api.sqrt(api.rational(2))*raw_projection)).lower()
    require(api.lower(angle) > 0, "positive true whole-box combined-frame lower")
    return {"model_projection_upper": model_projection,
            "defect_point_receiver_upper": receiver,
            "model_point_column_upper": column,
            "actual_weighted_oblique_projection_upper": total,
            "actual_raw_oblique_projection_upper": raw_projection,
            "actual_raw_orthonormal_matching_singular_lower": angle,
            "covers_every_point_of_box": True, "whole_high_feedback_included": False}


def contract_metadata():
    return {"kind": "R141_complete_low193_verified_Green_Gram_contract_v1",
            "coefficient_object": "same_true_varying_WVC_hybrid_low_signed_centre",
            "largest_state_matrix": 193, "left_carrier": 97, "right_carrier": 96,
            "complete_output_atom_count": 193,
            "same_panel_triangular_integrals_retained": True,
            "true_root_length_retained": True,
            "whole_interval_projection_certificate_provided_conditionally": True,
            "dense_all_radial_state_matrix_required": False,
            "high_CFB_or_actual_high_inverse_certified_here": False,
            "finite_projection_rho_bridge_certified_here": False,
            "scientific_targets_evaluated": 0}
