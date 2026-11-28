"""Actual low193 ODE flow, finite transversality, and signed RHS response.

Pure definitions: no numerical import, IO, producer call, or work at import.
This is a NEW target on the original variable-coefficient WVC hybrid A_L^c.
It does not evaluate the old comparison-Green HS or signed-loop target.

The local Peano--Baker enclosure below is valid for a TIME-VARYING matrix
inside the supplied complete box.  An interval matrix exponential must NOT
be substituted for it.  Both orientations and every original mean remain.
"""


N, P, Q = 193, 97, 96
HEAD = (tuple((0, j) for j in range(1, 97)) + ((1, 0),)
        + tuple((1, j) for j in range(1, 97)))


def require(ok, message):
    if not ok:
        raise ValueError(message)


def _upper(api, value):
    require(value.is_finite(), "finite directed value")
    answer = value.upper()
    require(answer.is_finite() and api.lower(answer) >= 0,
            "nonnegative directed upper")
    return answer


def _maximum(api, values):
    answer = api.zero
    for value in values:
        value = _upper(api, value)
        if bool(value > answer):
            answer = value
    return answer


def infinity_upper(api, matrix):
    return _maximum(api, [sum((api.magnitude(x) for x in row), api.zero)
                          for row in matrix.values])


def one_upper(api, matrix):
    return _maximum(api, [sum((api.magnitude(matrix.values[i][j])
                              for i in range(matrix.rows)), api.zero)
                          for j in range(matrix.cols)])


def two_upper(api, matrix):
    """A complete induced-2 bound, with no Gram or old target recomputation."""
    return _upper(api, api.sqrt(one_upper(api, matrix)*infinity_upper(api, matrix)))


def _finite(matrix):
    return all(x.is_finite() for row in matrix.values for x in row)


def diagonal_similarity(km, matrix, diagonal, inverse=False):
    require(matrix.rows == matrix.cols == len(diagonal), "whole diagonal similarity")
    return km.Matrix(matrix.rows, matrix.cols, [
        [value*(diagonal[j]/diagonal[i] if inverse else diagonal[i]/diagonal[j])
         for j, value in enumerate(row)] for i, row in enumerate(matrix.values)])


def diagonal_left(km, matrix, diagonal, inverse=False):
    require(matrix.rows == len(diagonal), "whole left diagonal")
    return km.Matrix(matrix.rows, matrix.cols, [
        [value/diagonal[i] if inverse else value*diagonal[i] for value in row]
        for i, row in enumerate(matrix.values)])


def _inflate(api, km, matrix, radius):
    radius = _upper(api, radius)
    error = api.interval(-radius, radius)
    return km.Matrix(matrix.rows, matrix.cols,
                     [[x+error for x in row] for row in matrix.values])


def peano_box(api, km, coefficient, duration, order=24, forcing=None,
              include_prefix=False):
    """Full forward/backward flow and optionally a full affine source.

    coefficient encloses A(r) at EVERY point of the whole physical box;
    forcing, when supplied, similarly encloses all columns of f(r).
    duration is the COMPLETE positive length ball, not its midpoint/upper.
    For true variable A, each chronological k-fold product lies in the
    interval product coefficient**k; the simplex has mass duration**k/k!.
    This use of interval powers permits independent A at different times.

    The matrix tail is bounded in induced infinity norm before attaching
    its bound to each entry.  The source tail uses the same norm and all
    source columns jointly.  No source derivative is assumed.
    """
    n = coefficient.rows
    require(coefficient.cols == n and n > 0 and _finite(coefficient),
            "complete finite square coefficient box")
    require(type(order) is int and order >= 2,
            "declared Peano truncation order at least two")
    require(duration.is_finite() and api.lower(duration) >= 0,
            "complete nonnegative physical duration")
    if forcing is not None:
        require(forcing.rows == n and forcing.cols > 0 and _finite(forcing),
                "all declared signed forcing columns")
    generator = km.scale(api, duration, coefficient)
    beta = infinity_upper(api, generator)
    gap = (api.one-beta/(order+2)).lower()
    require(api.lower(gap) > 0,
            "positive Peano tail ratio; refine the actual local box if needed")
    # Native matrices avoid 24 repeated conversions of every scalar.  This
    # changes no expression and introduces no floating matrix dependency.
    native = hasattr(api, "arb_mat")
    convert = (lambda value: api.arb_mat(value.values)) if native else (lambda value: value)
    multiply = (lambda a, b: a*b) if native else (lambda a, b: km.multiply(api, a, b))
    add = (lambda a, b: a+b) if native else (lambda a, b: km.add(api, a, b))
    scale = (lambda a, b: b*a) if native else (lambda a, b: km.scale(api, a, b))
    unconvert = (lambda value, cols: km.Matrix(n, cols,
        [[value[i, j] for j in range(cols)] for i in range(n)])) if native else (lambda value, cols: value)
    generator_work = convert(generator)
    term = convert(km.eye(api, n))
    plus, minus = convert(km.eye(api, n)), convert(km.eye(api, n))
    if include_prefix:
        unit = api.interval(api.zero, api.one)
        span_plus, span_minus = convert(km.eye(api, n)), convert(km.eye(api, n))
    if forcing is not None:
        forcing_scaled = km.scale(api, duration, forcing)
        forcing_work = convert(forcing_scaled)
        dplus = forcing_work
        dminus = scale(-api.one, forcing_work)
    for k in range(1, order+1):
        term = scale(api.rational(1, k), multiply(generator_work, term))
        plus = add(plus, term)
        minus = add(minus, scale(-api.one if k % 2 else api.one, term))
        if include_prefix:
            span_term = scale(unit, term)
            span_plus = add(span_plus, span_term)
            span_minus = add(span_minus,
                             scale(-api.one if k % 2 else api.one, span_term))
        if forcing is not None:
            source_term = scale(api.rational(1, k+1), multiply(term, forcing_work))
            dplus = add(dplus, source_term)
            dminus = add(dminus, scale(-api.one if k % 2 == 0 else api.one, source_term))
    plus, minus = unconvert(plus, n), unconvert(minus, n)
    require(_finite(plus) and _finite(minus), "finite whole signed Peano polynomial")
    first = api.one
    for k in range(1, order+2):
        first = _upper(api, first*beta/k)
    tail = _upper(api, first/gap)
    plus, minus = _inflate(api, km, plus, tail), _inflate(api, km, minus, tail)
    result = {"forward": plus, "backward": minus, "beta_upper": beta,
              "beta2_upper": two_upper(api, generator),
              "flow_tail_upper": tail, "order": order,
              "time_varying_coefficient_included": True,
              "matrix_exponential_used_as_varying_flow": False}
    if include_prefix:
        result.update(forward_span=_inflate(api, km, unconvert(span_plus, n), tail),
                      backward_span=_inflate(api, km, unconvert(span_minus, n), tail))
    if forcing is not None:
        source_gap = (api.one-beta/(order+3)).lower()
        require(api.lower(source_gap) > 0, "positive affine-source tail ratio")
        source_tail = _upper(api,
            infinity_upper(api, forcing_scaled)*first/(order+2)/source_gap)
        result.update(forward_increment=_inflate(api, km, unconvert(dplus, forcing.cols), source_tail),
                      backward_increment=_inflate(api, km, unconvert(dminus, forcing.cols), source_tail),
                      source_tail_upper=source_tail,
                      complete_forcing_columns=forcing.cols)
    require(_finite(plus) and _finite(minus), "finite complete directed local flows")
    return result


def true_cell_packet(api, km, context, provider, panel, cuts, balance,
                     order=24, source_provider=None, source_roles=()):
    """New actual local transfer on one ORIGINAL refined physical cell."""
    domain = context.domain
    require(provider.context is context and tuple(provider.green.HEAD) == HEAD,
            "the admitted genuine-child provider on this exact domain")
    require(len(cuts) >= 2 and cuts[0] == domain.fzero and cuts[-1] == domain.fone
            and all(a < b for a, b in zip(cuts[:-1], cuts[1:])),
            "complete exact ordered normalized cell partition")
    require(balance.is_finite() and balance.lower() == balance.upper()
            and api.lower(balance) > 0, "exact positive INTERNAL balance")
    diagonal = [api.one]*96+[balance]*97
    total_forward, total_backward = km.eye(api, N), km.eye(api, N)
    total_increment = None
    beta_sum, beta2_sum, max_tail = api.zero, api.zero, api.zero
    require(len(set(source_roles)) == len(source_roles)
            and set(source_roles) <= {"ordinary_raw_low_source", "transformed_low_source",
                "low_second_kind_correction", "centre_high0_return_source"},
            "only declared complete true-inverse source roles, no old comparison defect")
    moments = ({"output": km.zeros(api, N, N),
                "inputs": {role: km.zeros(api, N, N) for role in source_roles}}
               if source_roles else None)
    source_model = {"context": context}
    for lo, hi in zip(cuts[:-1], cuts[1:]):
        box = (panel, lo, hi)
        domain.validate_box(box)
        coefficient = provider.centre_matrix(HEAD, HEAD, box)
        require(coefficient.shape == (N, N), "full actual low193 including its mean")
        balanced = diagonal_similarity(km, coefficient, diagonal)
        h = domain.full_length(panel)*domain.exact(hi-lo)
        require(api.lower(h) > 0, "complete positive true subcell length")
        forcing = None
        if source_provider is not None:
            forcing = source_provider(box)
            require(forcing.rows == N, "all physical forcing rows retained")
            forcing = diagonal_left(km, forcing, diagonal)
        local = peano_box(api, km, balanced, h, order, forcing, bool(source_roles))
        forward = diagonal_similarity(km, local["forward"], diagonal, inverse=True)
        backward = diagonal_similarity(km, local["backward"], diagonal, inverse=True)
        if moments is not None:
            span_forward = diagonal_similarity(km, local["forward_span"], diagonal, inverse=True)
            span_backward = diagonal_similarity(km, local["backward_span"], diagonal, inverse=True)
            prefix = km.multiply(api, span_forward, total_forward)
            reverse_prefix = km.multiply(api, total_backward, span_backward)
            q = context.reference_qs[panel]
            weighted = diagonal_left(km, prefix, [api.one]*96+[q]*97)
            moments["output"] = km.add(api, moments["output"],
                km.scale(api, h, km.multiply(api, km.transpose(weighted), weighted)))
            for role in source_roles:
                W = provider.source_matrix(source_model, box, role)
                require(W.rows == N and W.cols == (128 if role == "centre_high0_return_source" else N),
                        "complete actual source columns, including all original means")
                pulled = km.multiply(api, reverse_prefix, W)
                moments["inputs"][role] = km.add(api, moments["inputs"][role],
                    km.scale(api, h, km.multiply(api, pulled, km.transpose(pulled))))
        total_forward = km.multiply(api, forward, total_forward)
        total_backward = km.multiply(api, total_backward, backward)
        if forcing is not None:
            increment = diagonal_left(km, local["forward_increment"], diagonal, inverse=True)
            total_increment = (increment if total_increment is None else
                               km.add(api, km.multiply(api, forward, total_increment), increment))
        beta_sum = _upper(api, beta_sum+local["beta_upper"])
        beta2_sum = _upper(api, beta2_sum+local["beta2_upper"])
        max_tail = _maximum(api, [max_tail, local["flow_tail_upper"]])
    require(_finite(total_forward) and _finite(total_backward),
            "complete finite forward and reverse true-cell transitions")
    condition = _maximum(api, [balance, api.one/balance, api.one])
    prefix_flow = _upper(api, condition*beta2_sum.exp())
    return {"forward": total_forward, "backward": total_backward,
            "forward_increment": total_increment, "panel": panel,
            "subboxes": len(cuts)-1, "beta_sum_upper": beta_sum,
            "beta2_sum_upper": beta2_sum,
            "complete_raw_prefix_and_inverse_upper": prefix_flow,
            "largest_local_tail_upper": max_tail,
            "true_moments": moments,
            "actual_S_changed": False, "all193_coordinates_retained": True}


def _inverse(api, km, core, matrix, observer, phase, index):
    if observer is not None:
        observer("start", phase, index, matrix, None)
    try:
        inverse = core.directed_inverse(api, km, matrix)
    except Exception as error:
        raise ActualPivotFailure(phase, index, str(error)) from error
    if observer is not None:
        observer("complete", phase, index, matrix, inverse)
    return inverse


class ActualPivotFailure(Exception):
    """An unproved actual finite pivot; never an assertion of singularity."""
    def __init__(self, phase, index, message):
        super().__init__("actual "+phase+" pivot "+str(index)+": "+message)
        self.phase, self.index = phase, index


def _store_true_node(api, km, core, refined, store, index, chart, Z, Y, observer):
    """The unchanged full block inverse, exposing its actual96 pivot."""
    W = _inverse(api, km, core,
        km.add(api, km.eye(api, Q), km.scale(api, -api.one, km.multiply(api, Z, Y))),
        observer, "node_transversality", index)
    YW, WZ = km.multiply(api, Y, W), km.multiply(api, W, Z)
    left = refined.chart_left(api, km, chart, km.vcat(km.eye(api, P), Z))
    right = refined.chart_left(api, km, chart, km.vcat(Y, km.eye(api, Q)))
    ell = refined.chart_right(api, km,
        km.hcat(km.add(api, km.eye(api, P), km.multiply(api, YW, Z)),
                km.scale(api, -api.one, YW)), chart, inverse=True)
    rho = refined.chart_right(api, km,
        km.hcat(km.scale(api, -api.one, WZ), W), chart, inverse=True)
    for name, value in (("left", left), ("right", right), ("ell", ell), ("rho", rho)):
        store.put(("model", "node", index, name), value)


def certify_true_model(api, km, core, refined, context, provider, chart_specs,
                       balances, store, cuts_per_cell=4, order=24,
                       source_provider=None, source_roles=(), progress=None,
                       pivot_observer=None, maximum_cuts_per_cell=64):
    """Stream actual transfers, certify both finite graphs and every pivot.

    context is the exact RefinedContext from the admitted original155
    panels.  chart_specs may reuse the prior reference proposals; no old
    QR, Green integral, HS bound, or signed trace target is evaluated.
    `store` is a fresh existing PackedMatrices instance.  Its outward
    packing is included in each later propagation, as in R141.
    """
    require(provider.context is context and hasattr(context, "original")
            and len(context.original.domain.cells) == 155
            and len(balances) == 155, "same actual original155-panel hybrid")
    count = len(context.domain.cells)
    require(len(chart_specs) == count+1 and type(cuts_per_cell) is int
            and cuts_per_cell > 0 and type(maximum_cuts_per_cell) is int
            and maximum_cuts_per_cell >= cuts_per_cell,
            "complete node charts and positive local refinement plan")
    require(context.qualifications.get("same_WVC_reference") is True
            and context.qualifications.get("ordinary_dr_pairing_and_complete_Gf_atoms") is True,
            "same WVC source, full193 atoms and ordinary dr")
    ix, iy = tuple(range(P)), tuple(range(P, N))
    Z = km.zeros(api, Q, P)
    store.put(("true_temporary", "Z", 0), Z)
    local_stats = []
    for i, cell in enumerate(context.domain.cells):
        chart = refined._chart(api, chart_specs[i], first=i == 0)
        next_chart = refined._chart(api, chart_specs[i+1], last=i+1 == count)
        local_cuts = cuts_per_cell
        while True:
            cuts = [context.domain.fone*j/local_cuts for j in range(local_cuts+1)]
            try:
                local = true_cell_packet(api, km, context, provider, i, cuts,
                    balances[cell["parent_panel"]], order, source_provider, source_roles)
                forward = refined.chart_left(api, km, next_chart,
                    refined.chart_right(api, km, local["forward"], chart), inverse=True)
                backward = refined.chart_left(api, km, chart,
                    refined.chart_right(api, km, local["backward"], next_chart), inverse=True)
                aa, ab = core.submatrix(km, forward, ix, ix), core.submatrix(km, forward, ix, iy)
                ba, bb = core.submatrix(km, forward, iy, ix), core.submatrix(km, forward, iy, iy)
                inverse = _inverse(api, km, core, km.add(api, aa, km.multiply(api, ab, Z)),
                                   pivot_observer, "left97", i)
                break
            except Exception as error:
                local_failure = ((isinstance(error, ActualPivotFailure)
                    and error.phase == "left97" and error.index == i)
                    or (isinstance(error, ValueError) and str(error).startswith("positive Peano tail ratio")))
                if not local_failure or local_cuts*2 > maximum_cuts_per_cell:
                    raise
                if progress is not None:
                    progress("true_low193_refine_only_uncompleted_current_cell", {
                        "cell": i, "old_cuts": local_cuts, "new_cuts": local_cuts*2,
                        "failure": str(error), "completed_prefix_reused_cells": i,
                        "previous_successful_cells_recomputed": 0})
                local_cuts *= 2
        Z = km.multiply(api, km.add(api, ba, km.multiply(api, bb, Z)), inverse)
        store.put(("model", "C", i), inverse)
        store.put(("true_temporary", "backward", i), backward)
        store.put(("true_temporary", "Z", i+1), Z)
        Z = store.get(("true_temporary", "Z", i+1))
        if source_provider is not None:
            store.put(("true_source", "increment", i), local["forward_increment"])
        if source_roles:
            store.put(("true_moment", "output", i), local["true_moments"]["output"])
            for role in source_roles:
                store.put(("true_moment", role, i), local["true_moments"]["inputs"][role])
        local_stats.append({key: local[key] for key in
            ("panel", "subboxes", "beta_sum_upper", "beta2_sum_upper",
             "complete_raw_prefix_and_inverse_upper", "largest_local_tail_upper")})
        if progress is not None:
            progress("true_low193_local_transfer_and_left_graph", {
                "cells_complete": i+1, "cells": count,
                "old_HS_and_signed_trace_targets_called": False})
    Y = km.zeros(api, P, Q)
    _store_true_node(api, km, core, refined, store, count,
                        refined._chart(api, chart_specs[count], last=True),
                        store.get(("true_temporary", "Z", count)), Y, pivot_observer)
    store.remove(("true_temporary", "Z", count))
    for i in range(count-1, -1, -1):
        backward = store.get(("true_temporary", "backward", i))
        aa, ab = core.submatrix(km, backward, ix, ix), core.submatrix(km, backward, ix, iy)
        ba, bb = core.submatrix(km, backward, iy, ix), core.submatrix(km, backward, iy, iy)
        inverse = _inverse(api, km, core, km.add(api, km.multiply(api, ba, Y), bb),
                           pivot_observer, "right96", i)
        Y = km.multiply(api, km.add(api, km.multiply(api, aa, Y), ab), inverse)
        store.put(("model", "D", i), inverse)
        _store_true_node(api, km, core, refined, store, i,
                            refined._chart(api, chart_specs[i], first=i == 0),
                            store.get(("true_temporary", "Z", i)), Y, pivot_observer)
        store.remove(("true_temporary", "Z", i))
        store.remove(("true_temporary", "backward", i))
        if progress is not None:
            progress("true_low193_right_graph_and_transversality", {
                "cells_complete": count-i, "cells": count,
                "finite_actual_pivots_required": True})
    nodes = refined.NodeSequence(store, count+1)
    return {"kind": "R149_actual_low193_local_flow_and_finite_transversality_v1",
            "context": context, "nodes": nodes,
            "Uinv": refined.MatrixSequence(store, ("model", "C"), count),
            "Vinv": refined.MatrixSequence(store, ("model", "D"), count),
            "true_hybrid_BVP_verified": True,
            "comparison_BVP_verified_by_this_target": False,
            "complete_refined_cells": count, "local_statistics": local_stats,
            "private_store": store, "private_model_token": object(),
            "reference_identity": context.reference_identity,
            "all193_original_mean_and_boundary_coordinates_retained": True,
            "ordinary_dr_and_true_root_lengths_retained": True,
            "physical_S_replaced_by_internal_balance": False,
            "source_increments_complete": source_provider is not None,
            "complete_true_moment_source_roles": tuple(source_roles),
            "actual_complete_CFB_centre_proved": False,
            "actual_full_positive_family_inverse_proved": False,
            "original_finite_rho_bridge_proved": False,
            "original_seven_input_ports_proved": False,
            "topic_completion_proved": False}


def whole_kernel_upper(api, km, model):
    """Uniform true raw Green-kernel bound, all radii and both triangles.

    This is a new (possibly conservative) bound for the ACTUAL inverse.
    It is not the old HS/trace criterion and it is not used to decide
    transversality.  Every product is in the original physical order.
    """
    require(model["true_hybrid_BVP_verified"] is True,
            "complete finite true-flow transversality first")
    count, nodes = model["complete_refined_cells"], model["nodes"]
    minus_accumulator = plus_accumulator = api.zero
    answer = api.zero
    for i in range(count):
        node = nodes[i]
        p = model["local_statistics"][i]["complete_raw_prefix_and_inverse_upper"]
        left_output = _upper(api, p*two_upper(api, node["left"]))
        left_input = _upper(api, two_upper(api, node["ell"])*p)
        right_output = _upper(api, p*two_upper(api, node["right"]))
        right_input = _upper(api, two_upper(api, node["rho"])*p)
        if i:
            minus_accumulator = _upper(api,
                minus_accumulator*two_upper(api, model["Uinv"][i-1]))
            plus_accumulator = _upper(api,
                two_upper(api, model["Vinv"][i-1])*plus_accumulator)
        minus_accumulator = _maximum(api, [minus_accumulator, left_output])
        plus_accumulator = _maximum(api, [plus_accumulator, right_input])
        answer = _maximum(api, [answer, minus_accumulator*left_input,
                                right_output*plus_accumulator])
    return {"kind": "R149_actual_low193_whole_raw_Green_kernel_upper_v1",
            "private_model_token": model["private_model_token"],
            "whole_raw_kernel_upper": answer, "complete_cells": count,
            "ordinary_dr": True, "both_same_cell_triangles_retained": True,
            "all193_mean_and_boundary_coordinates_retained": True}


def complete_source_observation_upper(api, model, kernel, source_norm_upper):
    """Turn a complete ||W(r)||_2 bound into body/193-atom bounds.

    The owner must obtain source_norm_upper on the ENTIRE same true
    interval, in raw original source units; a projected or one-column
    bound is not a legal replacement.  No endpoint of an arbitrary L2
    source is evaluated.  The endpoint values belong only to its H1
    solution.  For direct signed RHS values use solve_signed_response.
    """
    require(model["true_hybrid_BVP_verified"] is True
            and kernel["private_model_token"] is model["private_model_token"]
            and kernel["complete_cells"] == model["complete_refined_cells"],
            "same complete true raw Green kernel")
    source_norm_upper = _upper(api, source_norm_upper)
    context = model["context"]
    length = sum((context.domain.full_length(i)
                  for i in range(model["complete_refined_cells"])), api.zero)
    require(api.lower(length) > 0, "whole true positive interval length")
    length = _upper(api, length)
    S = _maximum(api, [api.one]+list(context.reference_qs))
    W = _upper(api, kernel["whole_raw_kernel_upper"]*source_norm_upper)
    body = _upper(api, S*length*W)
    root = _upper(api, api.sqrt(length)*W)
    theta = _maximum(api, list(context.reference_thetas.values()))
    outer = _upper(api, theta*api.sqrt(length)*W)
    complete = _upper(api, api.sqrt(body*body+root*root+outer*outer))
    return {"kind": "R149_actual_low193_whole_source_and193atoms_upper_v1",
            "private_model_token": model["private_model_token"],
            "body_norm_upper": body, "root97_norm_upper": root,
            "outer96_norm_upper": outer, "complete_observation_norm_upper": complete,
            "whole_raw_point_response_upper": root,
            "true_source_global_2norm_upper": source_norm_upper,
            "full_CFB_or_positive_family_inverse_inferred": False}


def _quadratic(api, km, middle, sides):
    return km.multiply(api, km.transpose(sides), km.multiply(api, middle, sides))


def _trace_product(api, km, first, second):
    require(first.rows == first.cols == second.rows == second.cols,
            "complete square trace contraction")
    # This ordered signed contraction avoids a third dense multiplication.
    return sum((first.values[i][j]*second.values[j][i]
                for i in range(first.rows) for j in range(first.cols)), api.zero)


def complete_true_source_maps(api, km, core, model, progress=None):
    """Whole true-inverse body/root97/outer96 Hilbert--Schmidt bounds.

    Five private raw193 moments per true cell were already enclosed during
    its NEW actual local transfer.  Every cross-cell covariance is kept as
    a full signed97 or96 matrix.  Within a cell each triangular integral
    is bounded by its full positive square, once for each orientation;
    no same-cell triangle, source column, or original atom is omitted.
    These are bounds on the ACTUAL Green, never the old comparison target.
    """
    roles = model["complete_true_moment_source_roles"]
    require(model["true_hybrid_BVP_verified"] is True and len(roles) > 0,
            "actual all-pivot inverse and all requested raw moment families first")
    count, store, nodes = (model["complete_refined_cells"], model["private_store"], model["nodes"])
    root_output = core.rows(km, nodes[0]["left"], tuple(range(P)))
    root_accumulator = km.multiply(api, km.transpose(root_output), root_output)
    left_accumulator = km.zeros(api, P, P)
    right_accumulators = {role: km.zeros(api, Q, Q) for role in roles}
    body_squares = {role: api.zero for role in roles}
    root_squares = {role: api.zero for role in roles}
    for i in range(count):
        node, C, D = nodes[i], model["Uinv"][i], model["Vinv"][i]
        X = store.get(("true_moment", "output", i))
        OL, OR = _quadratic(api, km, X, node["left"]), _quadratic(api, km, X, node["right"])
        left_whole = km.add(api, left_accumulator, OL)
        for role in roles:
            J = store.get(("true_moment", role, i))
            IL = _quadratic(api, km, J, km.transpose(node["ell"]))
            IR = _quadratic(api, km, J, km.transpose(node["rho"]))
            right_whole = km.add(api, right_accumulators[role], IR)
            body_squares[role] += (_trace_product(api, km, left_whole, IL)
                                  +_trace_product(api, km, OR, right_whole))
            root_squares[role] += _trace_product(api, km, root_accumulator, IL)
            right_accumulators[role] = _quadratic(api, km, right_whole, km.transpose(D))
            store.remove(("true_moment", role, i))
        left_accumulator = _quadratic(api, km, left_whole, C)
        root_accumulator = _quadratic(api, km, root_accumulator, C)
        store.remove(("true_moment", "output", i))
        if progress is not None:
            progress("true_low193_complete_source_covariances", {
                "cells_complete": i+1, "cells": count, "complete_source_roles": list(roles),
                "all193_original_atoms_retained": True,
                "old_comparison_HS_and_trace_targets_called": False})
    outer_raw = core.rows(km, nodes[count]["right"], tuple(range(97, N)))
    outer_output = km.Matrix(Q, Q, [
        [model["context"].reference_thetas[j+1]*value for value in row]
        for j, row in enumerate(outer_raw.values)])
    outer_gram = km.multiply(api, km.transpose(outer_output), outer_output)
    answers = {}
    for role in roles:
        body, root = _upper(api, body_squares[role]), _upper(api, root_squares[role])
        outer = _upper(api, _trace_product(api, km, outer_gram, right_accumulators[role]))
        answers[role] = {
            "kind": "R149_actual_low193_complete_source_observation_map_v1",
            "source_role": role, "source_columns": 128 if role == "centre_high0_return_source" else N,
            "complete_true_cells": count, "ordinary_dr": True,
            "body_HS2_upper": body, "root97_HS2_upper": root, "outer96_HS2_upper": outer,
            "body_norm_upper": _upper(api, api.sqrt(body)),
            "atoms193_norm_upper": _upper(api, api.sqrt(root+outer)),
            "complete_norm_upper": _upper(api, api.sqrt(body+root+outer)),
            "body_source_has_no_radial_derivative_assumption": True,
            "same_cell_triangles_bounded_by_two_complete_positive_squares": True,
            "all193_mean_and_boundary_observations_retained": True,
            "high_return_is_original128_source_without_complete_CFB": True,
            "full_positive_inverse_or_original_RHS_claimed": False}
        answers[role].update(actual_low_BVP_proved=True,
            actual_body_norm_upper=answers[role]["body_norm_upper"],
            actual_atoms193_norm_upper=answers[role]["atoms193_norm_upper"],
            actual_complete_source_norm_upper=answers[role]["complete_norm_upper"])
        if role == "low_second_kind_correction":
            b, a = answers[role]["body_norm_upper"], answers[role]["atoms193_norm_upper"]
            answers[role]["actual_low_second_kind_inverse_upper"] = _upper(api,
                (api.sqrt((2+b)*(2+b)+a*a)+api.sqrt(b*b+a*a))/2)
            answers[role]["all193_independent_atom_inputs_keep_their_identity"] = True
    return {"kind": "R149_actual_low193_complete_true_source_maps_v1",
            "private_model_token": model["private_model_token"], "sources": answers,
            "same_actual_operator_and_full_original_observation_space": True}


def _outer_boundary(api, km, matrix):
    require(matrix.rows == N, "whole raw outer-boundary input")
    p0 = api.rational(13, 80)
    return km.Matrix(P, matrix.cols, [
        [a+p0*b for a, b in zip(matrix.values[j], matrix.values[97+j])]
        for j in range(Q)] + [list(matrix.values[96])])


def solve_signed_response(api, km, core, refined, model, left_data, right_data,
                          progress=None):
    """Direct true-Green response to the already integrated signed sources.

    left_data is the full96 root-even datum; right_data is the full97
    (outer odd+13/80 even, outer mean) datum.  Both can be zero.  They
    are independent boundary inputs, not the193 observation atoms.
    The arbitrary source columns are never replaced by one scalar norm.
    """
    require(model["true_hybrid_BVP_verified"] is True
            and model["source_increments_complete"] is True,
            "whole actual flow inverse and all declared source increments")
    count, store, nodes = (model["complete_refined_cells"], model["private_store"], model["nodes"])
    k = left_data.cols
    require(left_data.shape == (Q, k) and right_data.shape == (P, k),
            "all original boundary data, including the outer mean")
    root_right = core.rows(km, nodes[0]["right"], tuple(range(97, N)))
    outer_left = _outer_boundary(api, km, nodes[count]["left"])
    b = km.multiply(api, core.directed_inverse(api, km, root_right), left_data)
    a = km.multiply(api, core.directed_inverse(api, km, outer_left), right_data)
    store.put(("true_response", "a", count), a)
    for i in range(count-1, -1, -1):
        d = store.get(("true_source", "increment", i))
        require(d.shape == (N, k), "whole same-column true source increment")
        a = km.multiply(api, model["Uinv"][i],
            km.add(api, a, km.scale(api, -api.one, km.multiply(api, nodes[i+1]["ell"], d))))
        store.put(("true_response", "a", i), a)
        a = store.get(("true_response", "a", i))
    for i in range(count+1):
        node = nodes[i]
        a = store.get(("true_response", "a", i))
        x = km.add(api, km.multiply(api, node["left"], a),
                   km.multiply(api, node["right"], b))
        store.put(("true_response", "x", i), x)
        store.remove(("true_response", "a", i))
        if i < count:
            d = store.get(("true_source", "increment", i))
            b = km.add(api, km.multiply(api, model["Vinv"][i], b),
                       km.multiply(api, nodes[i+1]["rho"], d))
        if progress is not None:
            progress("true_low193_signed_response", {"nodes_complete": i+1, "nodes": count+1})
    values = refined.MatrixSequence(store, ("true_response", "x"), count+1)
    root_atoms = core.rows(km, values[0], tuple(range(P)))
    outer_raw = core.rows(km, values[count], tuple(range(97, N)))
    outer_atoms = km.Matrix(Q, k, [
        [model["context"].reference_thetas[j+1]*value for value in row]
        for j, row in enumerate(outer_raw.values)])
    return {"kind": "R149_actual_low193_complete_signed_node_response_v1",
            "private_model_token": model["private_model_token"],
            "nodes": values, "root97_atoms": root_atoms, "outer96_atoms": outer_atoms,
            "all193_original_observations_retained": True,
            "complete_forcing_columns": k,
            "full_cell_response_still_requires_local_prefix_flow": True,
            "actual_full_positive_family_inverse_proved": False}
