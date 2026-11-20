"""Exact finite-state realization of the continuous fixed-WVC WJK centre.

No entry point, IO, numerical dependency import, or scientific execution.
The centre is NOT replaced by a diagonal, a norm bound, or a Galerkin head.
The 1217 states below realize the continuous-r signed map before P_f radial
projection, with its 193 atomic input/output slots explicitly retained.
They supply a 609-dimensional endpoint test; they do not assert that it
passes or that the original finite Q_f/rho-normalizer gate has passed.

The API and Matrix operations are those of signed_semiseparable_kernel_math.
All returned matrices are signed whole-box enclosures.  A caller must keep
the fixed centre function distinct from its whole-box enclosure and from any
midpoint-based diagnostic.  All actual family, high error and port terms are
outside this centre realization and remain mandatory.
"""


def require(ok, message):
    if not ok:
        raise ValueError(message)


HEAD = (tuple((0, j) for j in range(1, 97)) + ((1, 0),)
        + tuple((1, j) for j in range(1, 97)))
HIGH0 = (tuple((0, j) for j in range(97, 161))
         + tuple((1, j) for j in range(97, 161)))
HIGH1 = (tuple((0, j) for j in range(97, 225))
         + tuple((1, j) for j in range(97, 225)))
HIGH0_IN_HIGH1 = tuple(HIGH1.index(c) for c in HIGH0)

# q is the raw low state, not S times that state.  For inversion of I-Hc,
# q denotes the correction to the given raw head input.
BLOCK_COORDINATES = (
    ("q", HEAD), ("y", HIGH0), ("z0", HIGH0), ("z1", HIGH1),
    ("yr", HIGH0), ("t0", HIGH1), ("t1", HIGH0),
)
BLOCK_SIZES = dict((name, len(coords)) for name, coords in BLOCK_COORDINATES)
STATE_DIMENSION = 1217
LEFT_ROW_COUNT = 608
RIGHT_ROW_COUNT = 609
FREE_INITIAL_DIMENSION = 609


def row_select(km, matrix, rows):
    return km.Matrix(len(rows), matrix.cols,
                     [list(matrix.values[i]) for i in rows])


def col_select(km, matrix, columns):
    return km.Matrix(matrix.rows, len(columns),
                     [[row[j] for j in columns] for row in matrix.values])


def high0_embed(api, km, matrix):
    """The genuine isometric inclusion K0 -> K1, with both parity rows."""
    require(matrix.rows == len(HIGH0), "complete high0 input")
    position = dict((i, k) for k, i in enumerate(HIGH0_IN_HIGH1))
    return km.Matrix(len(HIGH1), matrix.cols,
                     [list(matrix.values[position[i]]) if i in position
                      else [api.zero for _ in range(matrix.cols)]
                      for i in range(len(HIGH1))])


def high0_project(km, matrix):
    require(matrix.rows == len(HIGH1), "complete high1 input")
    return row_select(km, matrix, HIGH0_IN_HIGH1)


def high0_output_factor(api, km, matrix):
    """matrix Pi0, retaining the full K1 input carrier."""
    require(matrix.cols == len(HIGH0), "complete high0 output factor")
    position = dict((i, k) for k, i in enumerate(HIGH0_IN_HIGH1))
    return km.Matrix(matrix.rows, len(HIGH1),
                     [[row[position[j]] if j in position else api.zero
                       for j in range(len(HIGH1))] for row in matrix.values])


def _reference_matrix(api, km, coordinates, eta, q, diagonal=None):
    """Same raw D0 or Df as WVC; no S reset across a parent boundary."""
    values = []
    for component_out, j_out in coordinates:
        row = []
        for component_in, j_in in coordinates:
            value = api.zero
            if j_out == j_in and j_out:
                if component_out != component_in:
                    value = 4*j_out*eta*(q*q if component_out == 0 else api.one)
                elif diagonal is not None:
                    value = diagonal[j_out]
                    if component_out == 1:
                        value = -value
            row.append(value)
        values.append(row)
    return km.Matrix(len(coordinates), len(coordinates), values)


def complete_coefficients(api, km, ctx, box):
    """Read the exact same W2C packets/reference on one complete radial box.

    These are coefficient matrices, not old norm targets.  Only A11 is
    needed: A10 and A01 are its genuine coordinate submatrices.  Its use
    does not project the actual infinite high state or its residual.
    """
    qualifications = (
        "same_WVC_reference", "same_actual_S_and_all_seven_ports",
        "true_signed_collar_not_zero_reference_packet",
        "Bc_and_BLHc_external_support_160", "trial_support_224",
        "centre_residual_support_288", "whole_family_support_416",
    )
    require(all(ctx.qualifications.get(k) is True for k in qualifications),
            "complete same-object centre and support qualifications")
    i = ctx.domain.cell_index(box)
    chi, chip, psi, psip = ctx.cutoff(box)
    pc = api.one if ctx.parent_indices[i] == 0 else api.zero
    A11 = ctx.centre_matrix(HIGH1, HIGH1, box)
    eta, q = ctx.reference_etas[i], ctx.reference_qs[i]
    return {
        "AL": ctx.centre_matrix(HEAD, HEAD, box),
        "B": ctx.centre_matrix(HIGH0, HEAD, box),
        "C": ctx.centre_matrix(HEAD, HIGH0, box),
        "A11": A11,
        "A10": col_select(km, A11, HIGH0_IN_HIGH1),
        "A01": row_select(km, A11, HIGH0_IN_HIGH1),
        "D": _reference_matrix(api, km, HIGH0, eta, q),
        "Df": _reference_matrix(api, km, HEAD, eta, q,
                                  ctx.reference_diagonals[i]),
        "chi": chi, "chip": chip, "psi": psi, "psip": psip,
        "pc": pc, "pb": api.one-pc,
        "same_physical_S_even_weight": q,
        "same_parent_index": ctx.parent_indices[i],
    }


def complete_residual_factors(api, km, coefficients):
    """Pi_K1 (Lc p-f) with p=chi*y+psi*(Jf+JAJf).

    q enters f=Bq.  The result retains chi_prime and psi_prime.  It is a
    signed factorization, never a subtraction of separate positive norms.
    """
    c = coefficients
    E = high0_embed(api, km, km.eye(api, len(HIGH0)))
    chi, chip, psi, psip, pc, pb = (c[k] for k in
                                  ("chi", "chip", "psi", "psip", "pc", "pb"))
    return {
        "q": km.scale(api, chi*chi+psi*pc-api.one,
                      high0_embed(api, km, c["B"])),
        "y": km.add(api, km.scale(api, chip, E),
                    km.scale(api, chi, high0_embed(api, km, c["D"])),
                    km.scale(api, -chi, c["A10"])),
        "z0": km.add(api, km.scale(api, psip, E),
                     km.scale(api, -psi*pb, c["A10"])),
        "z1": km.add(api, km.scale(api, psip, km.eye(api, len(HIGH1))),
                     km.scale(api, -psi, c["A11"])),
    }


def complete_matrix_blocks(api, km, coefficients):
    """All blocks of the exact 1217-dimensional homogeneous centre ODE.

    A block list avoids allocating a dense 1217-square matrix.  Sparse
    conversion may omit only exact zero entries; no small-entry threshold
    is a mathematical projection.  The same list can act on a vector or
    on a full declared column panel.
    """
    c = coefficients
    r = complete_residual_factors(api, km, c)
    chi, psi, pc = c["chi"], c["psi"], c["pc"]
    CP = high0_output_factor(api, km, c["C"])
    blocks = [
        ("q", "q", c["AL"]),
        ("q", "y", km.scale(api, chi, c["C"])),
        ("q", "z0", km.scale(api, psi, c["C"])),
        ("q", "z1", km.scale(api, psi, CP)),
        ("q", "yr", km.scale(api, -chi, c["C"])),
        ("q", "t0", km.scale(api, pc, CP)),
        ("q", "t1", km.scale(api, -pc, c["C"])),
        ("y", "q", km.scale(api, chi, c["B"])),
        ("y", "y", c["D"]),
        ("z0", "q", km.scale(api, pc, c["B"])),
        ("z1", "z0", km.scale(api, pc, c["A10"])),
        ("yr", "yr", c["D"]),
        ("t1", "t0", km.scale(api, -pc, c["A01"])),
    ]
    for source in ("q", "y", "z0", "z1"):
        blocks.append(("yr", source,
                       km.scale(api, chi, high0_project(km, r[source]))))
        blocks.append(("t0", source, km.scale(api, -psi, r[source])))
    for target, source, matrix in blocks:
        require(matrix.shape == (BLOCK_SIZES[target], BLOCK_SIZES[source]),
                "complete finite-state block shape: " + target + "/" + source)
    return blocks


def complete_action(api, km, blocks, state):
    """Exact action on every declared input column; no quadrature is used."""
    require(set(state) == set(BLOCK_SIZES), "all seven states")
    ncol = state["q"].cols
    require(all(state[k].shape == (n, ncol) for k, n in BLOCK_SIZES.items()),
            "complete common column panel")
    outputs = {name: km.zeros(api, n, ncol) for name, n in BLOCK_SIZES.items()}
    for target, source, matrix in blocks:
        outputs[target] = km.add(api, outputs[target],
                                km.multiply(api, matrix, state[source]))
    return outputs


def paired_centre_inverse_forcing(api, km, coefficients, raw_head_input):
    """Forcing for q = raw(I-Hc_cont)^(-1)h - raw(h).

    The supplied head is S^-1 times the given transformed L2 input.  It
    need not have a radial derivative or trace.  Its source in the low
    equation is (AL-Df)h; the other occurrences enter f=B(q+h).  The d/b
    components of h are added unchanged at the output and are not hidden
    endpoint values of this arbitrary L2 function.
    """
    require(raw_head_input.rows == len(HEAD), "whole raw L2 head input")
    c = coefficients
    ncol = raw_head_input.cols
    out = {name: km.zeros(api, n, ncol) for name, n in BLOCK_SIZES.items()}
    out["q"] = km.multiply(api, km.add(api, c["AL"],
                                      km.scale(api, -api.one, c["Df"])),
                             raw_head_input)
    source = km.multiply(api, c["B"], raw_head_input)
    out["y"] = km.scale(api, c["chi"], source)
    out["z0"] = km.scale(api, c["pc"], source)
    residual = km.scale(api, c["chi"]*c["chi"]+c["psi"]*c["pc"]-api.one,
                        high0_embed(api, km, source))
    out["yr"] = km.scale(api, c["chi"], high0_project(km, residual))
    out["t0"] = km.scale(api, -c["psi"], residual)
    return out


def original_ordinary_source_forcing(api, km, low_source):
    """Ordinary source in the low equation, with every other state zero."""
    require(low_source.rows == len(HEAD), "whole ordinary low source")
    out = {name: km.zeros(api, n, low_source.cols) for name, n in BLOCK_SIZES.items()}
    out["q"] = low_source
    return out


def _row(api, km, state, block, indices):
    return row_select(km, state[block], indices)


def complete_left_rows(api, km, state):
    """608 actual separated homogeneous reference rows at the true root."""
    return km.vcat(
        _row(api, km, state, "q", tuple(range(97, 193))),
        _row(api, km, state, "y", tuple(range(64, 128))),
        state["z0"], state["z1"],
        _row(api, km, state, "yr", tuple(range(64, 128))),
    )


def complete_right_rows(api, km, state):
    """609 full terminal rows, including low physical mean and both J* rows."""
    p0 = api.rational(13, 80)

    def robin(block, odd, even):
        return km.add(api, _row(api, km, state, block, odd),
                      km.scale(api, p0, _row(api, km, state, block, even)))

    return km.vcat(
        robin("q", tuple(range(96)), tuple(range(97, 193))),
        _row(api, km, state, "q", (96,)),
        robin("y", tuple(range(64)), tuple(range(64, 128))),
        robin("yr", tuple(range(64)), tuple(range(64, 128))),
        state["t0"], state["t1"],
    )


def complete_left_kernel_injection(api, km):
    """The exact isometric 1217-by-609 initial frame; no numerical kernel."""
    free = (
        ("q", tuple(range(97))), ("y", tuple(range(64))),
        ("yr", tuple(range(64))), ("t0", tuple(range(256))),
        ("t1", tuple(range(128))),
    )
    state = {name: km.zeros(api, n, FREE_INITIAL_DIMENSION)
             for name, n in BLOCK_SIZES.items()}
    col = 0
    for name, indices in free:
        for row in indices:
            state[name].values[row][col] = api.one
            col += 1
    require(col == FREE_INITIAL_DIMENSION, "complete609 free initial coordinates")
    return state


def centre_output(api, km, state, coefficients):
    """Raw low state and the complete returned high0 Ff in original signs."""
    c = coefficients
    feedback = km.add(
        api, km.scale(api, c["chi"], state["y"]),
        km.scale(api, c["psi"], state["z0"]),
        km.scale(api, c["psi"], high0_project(km, state["z1"])),
        km.scale(api, -c["chi"], state["yr"]),
        km.scale(api, c["pc"], high0_project(km, state["t0"])),
        km.scale(api, -c["pc"], state["t1"]),
    )
    return {"raw_low_state": state["q"], "complete_returned_high0_Ff": feedback}


def state_layout():
    """Metadata only; a scientific caller owns integrations and certificates."""
    offset = 0
    result = []
    for name, coordinates in BLOCK_COORDINATES:
        result.append({"name": name, "offset": offset, "size": len(coordinates)})
        offset += len(coordinates)
    require(offset == STATE_DIMENSION, "complete1217 states")
    return {
        "kind": "same_WVC_WJK_complete_finite_state_realization_v1",
        "blocks": result,
        "state_dimension": STATE_DIMENSION,
        "left_rows": LEFT_ROW_COUNT,
        "right_rows": RIGHT_ROW_COUNT,
        "endpoint_matrix_dimension": FREE_INITIAL_DIMENSION,
        "all_low193_and_physical_mean": True,
        "reference_G0_used_twice_with_both_boundaries": True,
        "Jstar_integrates_to_actual_R": True,
        "raw_identity_transmissions_not_S_identity": True,
        "full_actual_high_state_truncated": False,
        "actual_family_inverse_proved": False,
        "centre_boundary_matrix_invertibility_proved": False,
        "original_finite_Qf_rho_gate_transferred": False,
        "scientific_targets_evaluated": 0,
    }
