#!/usr/bin/env sage-python
"""R906: exact small-prime charts and continuation for the unchanged P map.

All mathematical execution occurs only in the public research Actions.
No coefficients, matrices, or certificates are persisted.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run only in the public research repository Actions.")

import gc
from sage.all import QQ, ZZ, PowerSeriesRing, matrix, vector
from original_newton_cm_germs import original_y_germ
from original_padic_dixon_map import ResidueReducer, _hash_ints

def choose_original_chart(qrows, fp, root, fm, vmod, low_order, embedding, progress):
    """Same full mod-p matrix and canonical free-coordinate rule as R892."""
    low_order = int(low_order)
    precision = low_order+2
    dim = len(qrows)
    prime = ZZ(fp.characteristic())
    assert 6*(low_order+1)+1 < prime < 94906266
    progress("Dixon base germ start", embedding=embedding,
             prime=int(prime), maximum=low_order+1)
    ring = PowerSeriesRing(fp, "Q", default_prec=precision)
    ycoeff = original_y_germ(fp, vmod, fm, 1, low_order+1)
    yy = ring(ycoeff).add_bigoh(precision)
    progress("Dixon base germ complete", embedding=embedding,
             germ_sha256=_hash_ints(ycoeff))
    basis = [ring([fp(c) for c in row]).add_bigoh(precision) for row in qrows]
    by = [yy*bb for bb in basis]
    progress("Dixon base full matrix start", embedding=embedding,
             rows=low_order+1, columns=2*dim)
    full = matrix(fp, low_order+1, 2*dim, lambda i, j:
                  (fp.zero() if i == 0 else basis[j][i-1])
                  if j < dim else -by[j-dim][i], implementation="linbox-double")
    progress("Dixon base full matrix constructed", embedding=embedding,
             rows=low_order+1, columns=2*dim,
             exact_matrix_backend=type(full).__module__+"."+type(full).__name__)
    assert "matrix_modn_dense_double" in type(full).__module__
    echelon = full.echelon_form()
    pivots = tuple(int(j) for j in echelon.pivots())
    rank = len(pivots)
    progress("Dixon base full matrix echelon complete", embedding=embedding,
             rank=rank, columns=2*dim)
    if rank == 2*dim:
        return {"rank": rank, "pivots": pivots, "solution": None,
                "embedding": int(embedding), "root": ZZ(root)}
    pivot_set = set(pivots)
    free = next(j for j in range(2*dim) if j not in pivot_set)
    # The row set may differ between embeddings.  Only the column/free chart
    # and B valuation must agree to recover the same original field vector.
    pivot_columns = full.matrix_from_columns(pivots)
    row_indices = tuple(int(i) for i in pivot_columns.transpose().pivots())
    assert len(row_indices) == rank
    square = matrix(fp, [[full[i, j] for j in pivots] for i in row_indices],
                    implementation="linbox-double")
    rhs = vector(fp, [-full[i, free] for i in row_indices])
    progress("Dixon fixed square inverse start", embedding=embedding,
             rank=rank, pivot_columns_sha256=_hash_ints(pivots),
             pivot_rows_sha256=_hash_ints(row_indices), free=int(free))
    inverse = square.inverse()
    pivot_solution = inverse*rhs
    solution = vector(fp, 2*dim)
    solution[free] = fp.one()
    for j, value in zip(pivots, pivot_solution):
        solution[j] = value
    assert (full*solution).is_zero()
    bseries = sum((solution[dim+j]*basis[j] for j in range(dim)), ring.zero())
    assert bseries != 0 and bseries.valuation() >= 1
    bvaluation = int(bseries.valuation())
    progress("Dixon fixed square inverse complete", embedding=embedding,
             rank=rank, free=int(free), B_valuation=bvaluation,
             canonical_mod_prime_solution_sha256=_hash_ints(solution))
    return {"rank": rank, "pivots": pivots, "rows": row_indices,
            "free": int(free), "inverse": inverse,
            "B_valuation": bvaluation, "solution": [ZZ(x) for x in solution],
            "root": ZZ(root), "embedding": int(embedding),
            "base_germ": [ZZ(x) for x in ycoeff]}


def lift_original_embedding(chart, qrows, ff, vnew, root_lift,
                            prime, digits, low_order, progress, stride=16,
                            previous_solution=None, previous_digits=0):
    """Continue the same chart from an earlier fully checked prime-power solution."""
    prime, digits, low_order = ZZ(prime), int(digits), int(low_order)
    stride = int(stride)
    assert digits >= 1 and stride >= 1
    maximum = low_order+1
    # Crucially the bound is on the residue prime, not characteristic p^N.
    assert prime > 6*maximum+1
    reducer = ResidueReducer(prime, digits)
    modulus, rr = reducer.modulus, reducer.ring
    root = rr(root_lift)
    assert root**3 == 17 and ZZ(root) % prime == chart["root"]
    embedding = chart["embedding"]
    rank, dim = chart["rank"], len(qrows)
    precision = low_order+2
    ring = PowerSeriesRing(rr, "Q", default_prec=precision)
    progress("Dixon prime-power germ start", embedding=embedding,
             digits=digits, modulus_bits=int(modulus.nbits()), maximum=maximum)
    fm = [reducer.element(c, root) for c in ff[:precision]]
    vv = reducer.element(vnew, root)
    # R889's Newton branch uses only the stated unit denominators and unit
    # series.  Its full two defining residuals remain enabled over this ring.
    ycoeff = original_y_germ(rr, vv, fm, 1, maximum)
    assert all(ZZ(c) % prime == old for c, old in zip(ycoeff, chart["base_germ"]))
    yy = ring(ycoeff).add_bigoh(precision)
    progress("Dixon prime-power germ complete", embedding=embedding,
             digits=digits, germ_sha256=_hash_ints(ycoeff))

    rows, pivots, free = chart["rows"], chart["pivots"], chart["free"]
    progress("Dixon high-precision square start", embedding=embedding,
             rank=rank, digits=digits, high_precision_rectangular_matrix=False)
    square = matrix(ZZ, rank, rank)
    rhs = vector(ZZ, rank)
    selected_columns = list(pivots)+[free]
    for jj, original_column in enumerate(selected_columns):
        if original_column < dim:
            values = [rr.zero() if i == 0 else
                      reducer.rational(qrows[original_column][i-1]) for i in rows]
        else:
            base = ring([reducer.rational(c) for c in
                         qrows[original_column-dim]]).add_bigoh(precision)
            product = (yy*base).add_bigoh(precision)
            values = [-product[i] for i in rows]
        if jj < rank:
            for ii, value in enumerate(values):
                square[ii, jj] = ZZ(value)
        else:
            rhs = vector(ZZ, [ZZ(-value) for value in values])
        if (jj+1) % 128 == 0 or jj+1 == rank+1:
            progress("Dixon square columns", embedding=embedding,
                     columns_built=jj+1, columns_total=rank+1)
    progress("Dixon high-precision square complete", embedding=embedding,
             rank=rank, digits=digits)

    fp = chart["inverse"].base_ring()
    previous_digits = int(previous_digits)
    assert 0 <= previous_digits < digits
    if previous_solution is None:
        assert previous_digits == 0
        error = vector(ZZ, rhs)
        answer = vector(ZZ, rank)
        power = ZZ(1)
    else:
        assert previous_digits >= 1 and len(previous_solution) == 2*dim
        power = prime**previous_digits
        assert all(0 <= ZZ(z) < power for z in previous_solution)
        assert ZZ(previous_solution[free]) == 1
        assert all(ZZ(previous_solution[j]) == 0
                   for j in range(2*dim) if j not in set(pivots) | {free})
        answer = vector(ZZ, [ZZ(previous_solution[j]) for j in pivots])
        continuation_residual = rhs-square*answer
        assert all(value % power == 0 for value in continuation_residual)
        error = vector(ZZ, [value//power for value in continuation_residual])
        del continuation_residual
    progress("Dixon continuation exact residual initialized", embedding=embedding,
             previous_digits=previous_digits, requested_digits=digits)
    inverse = chart["inverse"]
    for digit_index in range(previous_digits, digits):
        correction_fp = inverse*vector(fp, [fp(value % prime) for value in error])
        correction = vector(ZZ, [ZZ(value) for value in correction_fp])
        difference = error-square*correction
        assert all(value % prime == 0 for value in difference)
        answer += power*correction
        error = vector(ZZ, [value//prime for value in difference])
        power *= prime
        if (digit_index+1) % stride == 0 or digit_index+1 == digits:
            progress("Dixon digits", embedding=embedding, digits_done=digit_index+1,
                     digits_total=digits, bits_done=int(power.nbits()))
    assert power == modulus
    solution = [ZZ(0) for _ in range(2*dim)]
    solution[free] = ZZ(1)
    for j, value in zip(pivots, answer):
        solution[j] = value % modulus
    assert all(value % prime == old
               for value, old in zip(solution, chart["solution"]))
    if previous_solution is not None:
        old_modulus = prime**previous_digits
        assert all(value % old_modulus == ZZ(old)
                   for value, old in zip(solution, previous_solution))
    # Release the sole high-precision square before the full-window products.
    del square, rhs, error, answer, difference, correction, correction_fp
    gc.collect()
    progress("Dixon full original finite-window residual start",
             embedding=embedding, rows=low_order+1)

    aa, bb = ring.zero(), ring.zero()
    for j, row in enumerate(qrows):
        ca, cb = rr(solution[j]), rr(solution[dim+j])
        if ca == 0 and cb == 0:
            continue
        base = ring([reducer.rational(c) for c in row]).add_bigoh(precision)
        if ca != 0:
            aa += ca*base
        if cb != 0:
            bb += cb*base
    # These are precisely every row of R892's full rectangular matrix, not
    # merely the selected square and not only the cusp-leading coefficients.
    residual = (ring.gen()*aa-yy*bb).add_bigoh(low_order+1)
    failures = [i for i in range(low_order+1) if residual[i] != 0]
    info = {"embedding": int(embedding), "prime": int(prime),
            "root_mod_prime": int(chart["root"]), "digits": digits,
            "modulus_bits": int(modulus.nbits()), "rank": rank,
            "previous_digits": previous_digits,
            "new_dixon_digits": digits-previous_digits,
            "pivot_columns_sha256": _hash_ints(pivots),
            "pivot_rows_sha256": _hash_ints(rows), "free": int(free),
            "B_valuation_mod_prime": int(chart["B_valuation"]),
            "full_finite_window_rows": low_order+1,
            "full_finite_window_residual_sha256":
                _hash_ints(residual[i] for i in range(low_order+1)),
            "full_finite_window_zero": not failures,
            "solution_mod_prime_power_sha256": _hash_ints(solution)}
    if failures:
        info.update(first_nonzero_row=failures[0],
                    first_nonzero_p_valuation=int(ZZ(residual[failures[0]]).valuation(prime)),
                    status="fixed_chart_not_certified_at_requested_precision",
                    scope="No nonexistence conclusion for the original map.")
        progress("Dixon fixed-chart full window failed", **info)
        return None, info
    progress("Dixon full original finite-window residual complete",
             embedding=embedding, digits=digits, all_rows_zero=True,
             solution_sha256=info["solution_mod_prime_power_sha256"])
    return solution, info

