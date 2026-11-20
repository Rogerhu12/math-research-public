"""R141 exact same-cell two-triangle moments and shared output covariances.

Pure definitions: no imports, filesystem, numerical library, entry point,
old producer, or work at import.  A future public owner supplies directed
api/km/core objects and the unchanged complete comparison model.  This is
not an owner or a replacement for a currently running source.

Variable W(s) requires a pointwise constant PSD covariance upper.  An
entrywise source box is NEVER treated as a single constant unknown W.
The two same-cell triangles are retained through their exact signed sum.
"""

N = 193
P = 97
Q = 96


def require(ok, message):
    if not ok:
        raise ValueError(message)


def _transpose(km, value):
    return km.transpose(value)


def _scale(api, km, value, factor):
    return km.scale(api, factor, value)


def _add(api, km, *values):
    require(values, "nonempty complete matrix sum")
    result = values[0]
    for value in values[1:]:
        result = km.add(api, result, value)
    return result


def _infinity_upper(api, value):
    require(value.rows > 0 and value.cols > 0, "nonempty finite matrix")
    rows = [sum((api.magnitude(x) for x in row), api.zero).upper()
            for row in value.values]
    result = api.hull(rows).upper()
    require(result.is_finite() and api.lower(result) >= 0,
            "whole nonnegative matrix infinity upper")
    return result


def _dyadic_scale(api, bound):
    require(bound.is_finite() and api.lower(bound) >= 0,
            "finite nonnegative normalizing upper")
    result = api.one
    while not bool(result >= bound):
        result *= 2
        require(result.is_finite(), "finite exact dyadic normalization")
    require(result.lower() == result.upper(), "exact dyadic normalization")
    return result


def _inflate(api, km, value, radius):
    require(radius.is_finite() and api.lower(radius) >= 0,
            "nonnegative directed Taylor tail")
    error = api.interval(-radius, radius)
    return km.Matrix(value.rows, value.cols,
                     [[entry+error for entry in row] for row in value.values])


def _diagonal_left(km, values, matrix):
    require(len(values) == matrix.rows, "complete left diagonal")
    return km.Matrix(matrix.rows, matrix.cols,
                     [[values[i]*entry for entry in row]
                      for i, row in enumerate(matrix.values)])


def _diagonal_right(km, matrix, values):
    require(len(values) == matrix.cols, "complete right diagonal")
    return km.Matrix(matrix.rows, matrix.cols,
                     [[entry*values[j] for j, entry in enumerate(row)]
                      for row in matrix.values])


def _frobenius_inner(api, left, right):
    require(left.shape == right.shape, "complete same-shaped signed pairing")
    first = [[entry for row in left.values for entry in row]]
    second = [[entry] for row in right.values for entry in row]
    return api.matrix_product(first, second)[0][0]


def _trace(api, matrix):
    require(matrix.rows == matrix.cols, "whole square trace")
    return sum((matrix.values[i][i] for i in range(matrix.rows)), api.zero)


def _source_matrix_finite(matrix):
    return (matrix.rows == N and matrix.cols > 0
            and all(x.is_finite() for row in matrix.values for x in row))


def constant_source_covariance(api, km, source):
    """Only for one constant W, including its unchanged parameter balls."""
    require(_source_matrix_finite(source), "complete constant source matrix")
    return km.multiply(api, source, _transpose(km, source))


def whole_source_covariance_majorant(api, km, source_box):
    """GM.15: W(s)W(s)^T <= Vbar for every W(s) in the whole source box.

    source_box must enclose every point in the actual declared cell and
    every unchanged family parameter.  The exact entry midpoints define
    W0 only; they never replace the varying source.  All discarded width
    is explicitly paid in the PSD diagonal majorant.
    """
    require(_source_matrix_finite(source_box), "whole193 varying source box")
    midpoint = km.Matrix(N, source_box.cols,
        [[entry.mid() for entry in row] for row in source_box.values])
    require(all(x.lower() == x.upper() for row in midpoint.values for x in row),
            "one exact midpoint matrix, not a narrowed coefficient ball")
    radius = km.Matrix(N, source_box.cols, [
        [api.magnitude(source_box.values[i][j]-midpoint.values[i][j])
         for j in range(source_box.cols)] for i in range(N)])
    absolute = km.Matrix(N, source_box.cols,
        [[api.magnitude(entry) for entry in row] for row in midpoint.values])
    cross = km.multiply(api, absolute, _transpose(km, radius))
    covariance_error = _add(api, km, cross, _transpose(km, cross),
                            km.multiply(api, radius, _transpose(km, radius)))
    row_upper = [sum((entry.upper() for entry in row), api.zero).upper()
                 for row in covariance_error.values]
    require(all(value.is_finite() and api.lower(value) >= 0 for value in row_upper),
            "complete nonnegative covariance difference row upper")
    center_covariance = constant_source_covariance(api, km, midpoint)
    return km.Matrix(N, N, [
        [center_covariance.values[i][j]+(row_upper[i] if i == j else api.zero)
         for j in range(N)] for i in range(N)])


def prepare_moment_template(api, km, H, observation_covariance, degree=24):
    """GM.9--12 shared H/Q part; every dense multiplication is193 square.

    H encloses one fixed comparison generator, not a point-varying
    generator. Q encloses the fixed S^T S in the SAME balanced coordinates.
    Its PSD meaning is supplied by the original observation construction.
    The Taylor bound is for the complete3-block generator with both
    normalized off-diagonal infinity bounds <=1.
    """
    require(H.shape == observation_covariance.shape == (N, N),
            "whole193 generator and output covariance")
    require(type(degree) is int and degree >= 1, "declared Taylor degree")
    require(all(x.is_finite() for matrix in (H, observation_covariance)
                for row in matrix.values for x in row), "finite whole inputs")
    q_scale = _dyadic_scale(api, _infinity_upper(api, observation_covariance))
    Qnormalized = _scale(api, km, observation_covariance, api.one/q_scale)
    Htranspose = _transpose(km, H)
    hnorm = api.hull([_infinity_upper(api, H),
                     _infinity_upper(api, Htranspose)]).upper()
    divisions, denominator = 0, 1
    while not bool((hnorm+api.one)/denominator <= api.rational(1, 2)):
        divisions += 1
        denominator *= 2
    step = api.rational(1, denominator)
    lam = (step*(hnorm+api.one)).upper()
    require(bool(lam <= api.rational(1, 2)), "whole3-block short norm <=1/2")
    Hshort = _scale(api, km, H, step)
    Ashort = _scale(api, km, Htranspose, -step)
    Qshort = _scale(api, km, Qnormalized, step)
    plus_coefficients = [km.eye(api, N)]
    minus_sum = plus_sum = km.eye(api, N)
    xterm = xsum = km.zeros(api, N, N)
    for k in range(1, degree+1):
        old_plus = plus_coefficients[-1]
        next_plus = _scale(api, km, km.multiply(api, Hshort, old_plus),
                           api.rational(1, k))
        xterm = _scale(api, km, _add(api, km,
            km.multiply(api, Ashort, xterm),
            km.multiply(api, Qshort, old_plus)), api.rational(1, k))
        plus_coefficients.append(next_plus)
        minus_term = _scale(api, km, _transpose(km, next_plus),
                            -api.one if k % 2 else api.one)
        plus_sum = _add(api, km, plus_sum, next_plus)
        minus_sum = _add(api, km, minus_sum, minus_term)
        xsum = _add(api, km, xsum, xterm)
    scalar_term = api.one
    for k in range(1, degree+2):
        scalar_term = (scalar_term*lam/k).upper()
    tail_denominator = (api.one-lam/api.rational(degree+2)).lower()
    require(api.lower(tail_denominator) > 0, "positive complete Taylor-tail denominator")
    tail = (scalar_term/tail_denominator).upper()
    A = _inflate(api, km, minus_sum, tail)
    B = _inflate(api, km, plus_sum, tail)
    X = _inflate(api, km, xsum, tail)
    stages = [(A, B, X)]
    for _ in range(divisions):
        next_A = km.multiply(api, A, A)
        next_B = km.multiply(api, B, B)
        next_X = _add(api, km, km.multiply(api, A, X),
                       km.multiply(api, X, B))
        A, B, X = next_A, next_B, next_X
        stages.append((A, B, X))
    U = _scale(api, km, km.multiply(api, _transpose(km, B), X), q_scale)
    return {"Hshort": Hshort, "Ashort": Ashort, "Qshort": Qshort,
            "plus_coefficients": plus_coefficients, "stages": stages,
            "degree": degree, "divisions": divisions, "step": step,
            "tail": tail, "lambda_upper": lam, "Q_scale": q_scale,
            "U": U, "private_template_token": object()}


def source_moments(api, km, template, covariance):
    """GM.3/8 for a constant covariance, or its pointwise PSD majorant.

    PSD qualification is mathematical: callers must use a constant-source
    covariance or GM.15 for a genuinely whole source box.  This routine
    never infers PSD order from the signs of entrywise interval bounds.
    """
    require(covariance.shape == (N, N)
            and all(x.is_finite() for row in covariance.values for x in row),
            "whole constant193 source covariance")
    v_scale = _dyadic_scale(api, _infinity_upper(api, covariance))
    Vshort = _scale(api, km, covariance, template["step"]/v_scale)
    zterm = yterm = zsum = ysum = km.zeros(api, N, N)
    for k in range(1, template["degree"]+1):
        old_minus = _scale(api, km,
            _transpose(km, template["plus_coefficients"][k-1]),
            -api.one if (k-1) % 2 else api.one)
        next_z = _scale(api, km, _add(api, km,
            km.multiply(api, template["Hshort"], zterm),
            km.multiply(api, Vshort, old_minus)), api.rational(1, k))
        next_y = _scale(api, km, _add(api, km,
            km.multiply(api, template["Ashort"], yterm),
            km.multiply(api, template["Qshort"], zterm)), api.rational(1, k))
        zterm, yterm = next_z, next_y
        zsum, ysum = _add(api, km, zsum, zterm), _add(api, km, ysum, yterm)
    Z = _inflate(api, km, zsum, template["tail"])
    Y = _inflate(api, km, ysum, template["tail"])
    for A, B, X in template["stages"][:-1]:
        next_Z = _add(api, km, km.multiply(api, B, Z),
                       km.multiply(api, Z, A))
        next_Y = _add(api, km, km.multiply(api, A, Y),
                       km.multiply(api, X, Z), km.multiply(api, Y, A))
        Z, Y = next_Z, next_Y
    A, B, _ = template["stages"][-1]
    source_integral = _scale(api, km,
        km.multiply(api, _transpose(km, A), Z), v_scale)
    mixed_integral = _scale(api, km,
        km.multiply(api, _transpose(km, B), Y), template["Q_scale"]*v_scale)
    return {"U": template["U"], "Z": source_integral, "Y": mixed_integral,
            "private_template_token": template["private_template_token"]}


def prepare_model_template(api, km, core, model, panel, balance, degree=24):
    """Original exact parent model, actual S, and exact dyadic similarity."""
    require(model.get("comparison_BVP_verified") is True, "same verified model")
    require(balance.is_finite() and balance.lower() == balance.upper()
            and api.lower(balance) > 0, "exact positive dyadic internal balance")
    cells = model["context"].domain.cells
    cell = cells[panel]
    diagonal = [api.one]*96+[balance]*97
    inverse = [api.one]*96+[api.one/balance]*97
    H = _diagonal_right(km, _diagonal_left(km, diagonal,
                         model["generators"][panel]), inverse)
    actual_q = model["context"].reference_qs[panel]
    require(api.lower(actual_q) > 0, "unchanged actual physical q")
    weight = [api.one]*96+[actual_q/balance]*97
    Qmatrix = km.Matrix(N, N, [
        [weight[i]*weight[i] if i == j else api.zero for j in range(N)]
        for i in range(N)])
    result = prepare_moment_template(api, km, H, Qmatrix, degree)
    result.update({"diagonal": diagonal, "inverse_diagonal": inverse,
                   "private_model_token": model["private_model_token"],
                   "parent_key": (cell["parent_panel"], cell["count"])})
    return result


def model_source_covariance(api, km, template, source, constant=False):
    """Source matrix is supplied by the unchanged complete source role.

    For constant=False it MUST be a whole parent/cell enclosure, depending
    on where the owner reuses the result.  A shorter cell source box cannot
    be reused across the parent unless separately proved to cover it.
    """
    balanced = _diagonal_left(km, template["diagonal"], source)
    if constant:
        return constant_source_covariance(api, km, balanced)
    return whole_source_covariance_majorant(api, km, balanced)


def moment_panel_packet(api, km, core, model, panel, template, moments, source_role):
    """Complete whole-cell moments and signed sum of BOTH local triangles."""
    cell = model["context"].domain.cells[panel]
    require(template["private_model_token"] is model["private_model_token"]
            and template["parent_key"] == (cell["parent_panel"], cell["count"])
            and moments["private_template_token"] is template["private_template_token"],
            "same exact parent template and source moment definition")
    node = model["nodes"][panel]
    L = _diagonal_left(km, template["diagonal"], node["left"])
    R = _diagonal_left(km, template["diagonal"], node["right"])
    ell = _diagonal_right(km, node["ell"], template["inverse_diagonal"])
    rho = _diagonal_right(km, node["rho"], template["inverse_diagonal"])
    U, Z, Y = moments["U"], moments["Z"], moments["Y"]
    OL = core.congruence(api, km, _transpose(km, L), U)
    OR = core.congruence(api, km, _transpose(km, R), U)
    IL = core.congruence(api, km, ell, Z)
    IR = core.congruence(api, km, rho, Z)
    rectangle = core.trace_product(api, OL, IL)
    cross = _frobenius_inner(api, L, km.multiply(api, Y, _transpose(km, ell)))
    signed_same = rectangle+_trace(api, Y)-2*cross
    length = model["context"].domain.full_length(panel)
    require(api.lower(length) > 0, "same true positive ordinary-dr cell length")
    whole_same = core.positive_upper(api, length*length*signed_same)
    totals = {name: _scale(api, km, value, length)
              for name, value in (("OL", OL), ("OR", OR), ("IL", IL), ("IR", IR))}
    return {"panel": panel, "source_role": source_role, "totals": totals,
            "private_model_token": model["private_model_token"],
            "same_panel_complete_HS2_upper": whole_same,
            "same_panel_both_triangles_in_signed_complete_sum": True,
            "true_cell_length_retained": True,
            "whole_cell_covariance_moment_contract": "R141_GM1_through17"}


def prepare_shared_outputs(api, km, core, model, packets, prefix, progress=None):
    """GM.16 once for every source role, using original compact storage.

    Stores A/B/K using the original per-entry containment checks. Root J
    and D^T B_next D are streamed once per complete batch of source roles,
    not newly packed; thus reuse does not add a rounding step to those
    objects. All arrays are PRIVATE. Only small bounds are publishable.
    """
    count = core.require_complete_packets(model, packets)
    require(isinstance(prefix, tuple) and prefix, "private shared-output namespace")
    store = model["private_store"]
    keys = {name: prefix+(name,) for name in ("A", "B", "K")}
    A = km.zeros(api, P, P)
    store.put(keys["A"]+(0,), A)
    for i in range(count):
        Ctranspose = _transpose(km, model["Uinv"][i])
        A = core.congruence(api, km, Ctranspose,
                            _add(api, km, A, packets[i]["totals"]["OL"]))
        store.put(keys["A"]+(i+1,), A)
        A = store.get(keys["A"]+(i+1,))
        if progress is not None and (i % 64 == 63 or i+1 == count):
            progress("complete_shared_left_output_covariances",
                     {"cells_complete": i+1, "cells": count})
    B, K = km.zeros(api, Q, Q), core.output_gram(api, km, model["outer_atoms"])
    store.put(keys["B"]+(count,), B)
    store.put(keys["K"]+(count,), K)
    K = store.get(keys["K"]+(count,))
    for i in range(count-1, -1, -1):
        Dtranspose = _transpose(km, model["Vinv"][i])
        right = core.congruence(api, km, Dtranspose, B)
        B = _add(api, km, packets[i]["totals"]["OR"], right)
        K = core.congruence(api, km, Dtranspose, K)
        store.put(keys["B"]+(i,), B)
        store.put(keys["K"]+(i,), K)
        B, K = store.get(keys["B"]+(i,)), store.get(keys["K"]+(i,))
        if progress is not None and (i % 64 == 0 or i+1 == count):
            progress("complete_shared_right_and_outer96_covariances",
                     {"cells_complete": count-i, "cells": count})
    return {"prefix": prefix, "keys": keys, "cells": count,
            "private_model_token": model["private_model_token"],
            "original_root97_and_outer96_retained": True}


class _StoredSequence:
    def __init__(self, store, prefix, count):
        self.store, self.prefix, self.count = store, prefix, count

    def __len__(self):
        return self.count

    def __getitem__(self, index):
        if index < 0:
            index += self.count
        if not 0 <= index < self.count:
            raise IndexError(index)
        return self.store.get(self.prefix+(index,))


def complete_norms_with_shared_outputs(api, km, core, model, packet_families, shared,
                                      progress=None):
    """Complete batch; root J and right output congruence each stream once.

    A first one-role defect batch can precede its strict gate. If that gate
    passes, a four-role batch reuses the same stored A/B/K and performs ONE
    additional J/right stream. This respects the existing early-stop
    ordering and removes three of its five J/right streams.
    """
    require(packet_families, "nonempty batch of complete original source roles")
    counts = [core.require_complete_packets(model, packets)
              for packets in packet_families]
    count = counts[0]
    require(all(value == count for value in counts), "all complete cells for every role")
    require(shared["cells"] == count
            and shared["private_model_token"] is model["private_model_token"],
            "all source cells and the same complete shared output definition")
    roles = [packets[0]["source_role"] for packets in packet_families]
    require(len(set(roles)) == len(roles), "each complete role exactly once in this batch")
    require(all(packet.get("same_panel_both_triangles_in_signed_complete_sum") is True
                for packets in packet_families for packet in packets),
            "complete signed same-cell triangles")
    store, keys = model["private_store"], shared["keys"]
    sums = {role: [api.zero, api.zero, api.zero] for role in roles}
    root_carry = core.output_gram(api, km, model["root_atoms"])
    for i in range(count):
        left = store.get(keys["A"]+(i,))
        right = core.congruence(api, km, _transpose(km, model["Vinv"][i]),
                                 store.get(keys["B"]+(i+1,)))
        outer_carry = store.get(keys["K"]+(i,))
        for packets, role in zip(packet_families, roles):
            packet = packets[i]
            integral = packet["totals"]
            sums[role][0] += core.positive_upper(api, core.trace_product(api,
                left, integral["IL"]))
            sums[role][0] += core.positive_upper(api, core.trace_product(api,
                right, integral["IR"]))
            sums[role][0] += packet["same_panel_complete_HS2_upper"]
            sums[role][1] += core.positive_upper(api, core.trace_product(api,
                root_carry, integral["IL"]))
            sums[role][2] += core.positive_upper(api, core.trace_product(api,
                outer_carry, integral["IR"]))
        root_carry = core.congruence(api, km, _transpose(km, model["Uinv"][i]),
                                     root_carry)
        if progress is not None and (i % 64 == 63 or i+1 == count):
            progress("complete_exact_cell_moment_body_and193_atoms", {
                "complete_source_roles": roles,
                "cells_complete": i+1, "cells": count})
    results = {}
    for role in roles:
        body, root, outer = (core.positive_upper(api, value) for value in sums[role])
        results[role] = {"source_role": role,
            "private_model_token": model["private_model_token"],
            "body_HS2_upper": body, "root97_HS2_upper": root,
            "outer96_HS2_upper": outer,
            "body_norm_upper": core.positive_upper(api, api.sqrt(body)),
            "atoms193_norm_upper": core.positive_upper(api, api.sqrt(root+outer)),
            "complete_norm_upper": core.positive_upper(api, api.sqrt(body+root+outer)),
            "private_output_left_covariances": _StoredSequence(store, keys["A"], count+1),
            "private_output_right_covariances": _StoredSequence(store, keys["B"], count+1),
            "stored_body_and_outer_covariances_reused": True,
            "root97_stream_shared_by_all_batch_roles": True,
            "complete_refined_cells": count}
    return results


def complete_norm_with_shared_outputs(api, km, core, model, packets, shared,
                                     progress=None):
    """One-role adapter, used for the original first complete defect gate."""
    result = complete_norms_with_shared_outputs(api, km, core, model,
                                                [packets], shared, progress)
    return result[packets[0]["source_role"]]
