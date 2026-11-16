#!/usr/bin/env sage-python
"""R909: exact small-prime charts and compatible Dixon continuation for F.

Only the public research Actions may execute mathematics.  No coefficient
or matrix file is created.  Full rectangular residuals remain mandatory.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run only in the public research repository Actions.")

import gc
from sage.all import ZZ, PowerSeriesRing, matrix, vector
from original_newton_cm_germs import short_y_U
from original_padic_dixon_map import ResidueReducer, _hash_ints


def choose_first_factor_chart(arows, brows, fp, f0, eta_coeff,
                              low_order, progress):
    low_order = int(low_order)
    precision = low_order+1
    assert 6*low_order+1 < ZZ(fp.characteristic()) < 94906266
    da, db = len(arows), len(brows)
    ring = PowerSeriesRing(fp, "Q", default_prec=precision)
    progress("F Dixon base germ start", prime=int(fp.characteristic()),
             maximum=low_order)
    uu = ring(short_y_U(fp, f0, low_order)).add_bigoh(precision)
    ee = ring([fp(c) for c in eta_coeff[:precision]]).add_bigoh(precision)
    vv = (ee*uu).add_bigoh(precision)
    assert vv[0] == -1 and vv[1] == 5
    progress("F Dixon base germ complete",
             germ_sha256=_hash_ints([vv[i] for i in range(precision)]))
    am = [ring([fp(t) for t in row[:precision]]).add_bigoh(precision)
          for row in arows]
    bm = [ring([fp(t) for t in row[:precision]]).add_bigoh(precision)
          for row in brows]
    vb = [(vv*b).add_bigoh(precision) for b in bm]
    progress("F Dixon base full matrix start",
             rows=precision, columns=da+db)
    full = matrix(fp, precision, da+db,
                  lambda i, j: am[j][i] if j < da else -vb[j-da][i],
                  implementation="linbox-double")
    progress("F Dixon base full matrix constructed",
             rows=precision, columns=da+db,
             exact_matrix_backend=type(full).__module__+"."+type(full).__name__)
    assert "matrix_modn_dense_double" in type(full).__module__
    echelon = full.echelon_form()
    pivots = tuple(int(j) for j in echelon.pivots())
    rank = len(pivots)
    progress("F Dixon base full matrix echelon complete",
             rank=rank, columns=da+db)
    if rank == da+db:
        return {"rank": rank, "pivots": pivots, "solution": None}
    pivot_set = set(pivots)
    free = next(j for j in range(da+db) if j not in pivot_set)
    pivot_columns = full.matrix_from_columns(pivots)
    rows = tuple(int(i) for i in pivot_columns.transpose().pivots())
    assert len(rows) == rank
    square = matrix(fp, [[full[i, j] for j in pivots] for i in rows],
                    implementation="linbox-double")
    rhs = vector(fp, [-full[i, free] for i in rows])
    progress("F Dixon fixed square inverse start", rank=rank, free=free,
             pivot_columns_sha256=_hash_ints(pivots),
             pivot_rows_sha256=_hash_ints(rows))
    inverse = square.inverse()
    pivot_solution = inverse*rhs
    sol = vector(fp, da+db)
    sol[free] = fp.one()
    for j, value in zip(pivots, pivot_solution):
        sol[j] = value
    assert (full*sol).is_zero()
    aa = sum((sol[i]*am[i] for i in range(da)), ring.zero())
    bb = sum((sol[da+j]*bm[j] for j in range(db)), ring.zero())
    assert aa != 0 and bb != 0 and aa.valuation() == bb.valuation()
    val = int(bb.valuation())
    assert aa[val] == -bb[val]
    progress("F Dixon fixed square inverse complete",
             rank=rank, free=free, B_valuation=val,
             canonical_mod_prime_solution_sha256=_hash_ints(sol))
    return {"rank": rank, "pivots": pivots, "rows": rows, "free": free,
            "inverse": inverse, "solution": [ZZ(c) for c in sol],
            "B_valuation": val,
            "base_germ": [ZZ(vv[i]) for i in range(precision)]}


def lift_first_factor_chart(chart, arows, brows, f0, eta_coeff,
                            prime, digits, low_order, progress, stride=16,
                            previous_solution=None, previous_digits=0):
    prime, digits = ZZ(prime), int(digits)
    low_order, stride = int(low_order), int(stride)
    assert prime > 6*low_order+1 and digits >= 1 and stride >= 1
    reducer = ResidueReducer(prime, digits)
    rr, modulus = reducer.ring, reducer.modulus
    precision = low_order+1
    ring = PowerSeriesRing(rr, "Q", default_prec=precision)
    da, db, rank = len(arows), len(brows), chart["rank"]
    progress("F Dixon prime-power germ start", digits=digits,
             modulus_bits=int(modulus.nbits()), maximum=low_order)
    fm = [reducer.rational(c) for c in f0[:precision]]
    uu = ring(short_y_U(rr, fm, low_order)).add_bigoh(precision)
    ee = ring([reducer.rational(c) for c in eta_coeff[:precision]]
              ).add_bigoh(precision)
    vv = (ee*uu).add_bigoh(precision)
    assert all(ZZ(vv[i]) % prime == chart["base_germ"][i]
               for i in range(precision))
    assert vv[0] == -1 and vv[1] == 5
    progress("F Dixon prime-power germ complete", digits=digits,
             germ_sha256=_hash_ints([vv[i] for i in range(precision)]))
    rows, pivots, free = chart["rows"], chart["pivots"], chart["free"]
    progress("F Dixon high-precision square start", rank=rank,
             digits=digits, high_precision_rectangular_matrix=False)
    square = matrix(ZZ, rank, rank)
    rhs = vector(ZZ, rank)
    for column_index, original_column in enumerate(list(pivots)+[free]):
        if original_column < da:
            values = [reducer.rational(arows[original_column][i])
                      for i in rows]
        else:
            basis = ring([reducer.rational(c) for c in
                          brows[original_column-da][:precision]]
                         ).add_bigoh(precision)
            product = (vv*basis).add_bigoh(precision)
            values = [-product[i] for i in rows]
        if column_index < rank:
            for row_index, value in enumerate(values):
                square[row_index, column_index] = ZZ(value)
        else:
            rhs = vector(ZZ, [ZZ(-value) for value in values])
        if (column_index+1) % 128 == 0 or column_index+1 == rank+1:
            progress("F Dixon square columns",
                     columns_built=column_index+1, columns_total=rank+1)
    progress("F Dixon high-precision square complete",
             rank=rank, digits=digits)
    inverse = chart["inverse"]
    fp = inverse.base_ring()
    previous_digits = int(previous_digits)
    assert 0 <= previous_digits < digits
    if previous_solution is None:
        assert previous_digits == 0
        error = vector(ZZ, rhs)
        answer = vector(ZZ, rank)
        power = ZZ(1)
    else:
        assert previous_digits >= 1 and len(previous_solution) == da+db
        power = prime**previous_digits
        assert all(0 <= ZZ(z) < power for z in previous_solution)
        assert ZZ(previous_solution[free]) == 1
        pivot_set = set(pivots)
        assert all(ZZ(previous_solution[j]) == 0 for j in range(da+db)
                   if j != free and j not in pivot_set)
        answer = vector(ZZ, [ZZ(previous_solution[j]) for j in pivots])
        continuation_residual = rhs-square*answer
        assert all(value % power == 0 for value in continuation_residual)
        error = vector(ZZ, [value//power for value in continuation_residual])
        del continuation_residual
    progress("F Dixon continuation exact residual initialized",
             previous_digits=previous_digits, requested_digits=digits)
    for digit_index in range(previous_digits, digits):
        correction_fp = inverse*vector(fp, [fp(x % prime) for x in error])
        correction = vector(ZZ, [ZZ(x) for x in correction_fp])
        difference = error-square*correction
        assert all(x % prime == 0 for x in difference)
        answer += power*correction
        error = vector(ZZ, [x//prime for x in difference])
        power *= prime
        if (digit_index+1) % stride == 0 or digit_index+1 == digits:
            progress("F Dixon digits", digits_done=digit_index+1,
                     digits_total=digits, bits_done=int(power.nbits()))
    assert power == modulus
    sol = [ZZ(0) for _ in range(da+db)]
    sol[free] = ZZ(1)
    for j, value in zip(pivots, answer):
        sol[j] = value % modulus
    assert all(value % prime == old
               for value, old in zip(sol, chart["solution"]))
    if previous_solution is not None:
        old_modulus = prime**previous_digits
        assert all(value % old_modulus == ZZ(old)
                   for value, old in zip(sol, previous_solution))
    del square, rhs, error, answer, difference, correction, correction_fp
    gc.collect()
    progress("F Dixon full original finite-window residual start",
             rows=precision)
    aa, bb = ring.zero(), ring.zero()
    for j, row in enumerate(arows):
        coeff = rr(sol[j])
        if coeff:
            basis = ring([reducer.rational(c) for c in row[:precision]]
                         ).add_bigoh(precision)
            aa += coeff*basis
    for j, row in enumerate(brows):
        coeff = rr(sol[da+j])
        if coeff:
            basis = ring([reducer.rational(c) for c in row[:precision]]
                         ).add_bigoh(precision)
            bb += coeff*basis
    residual = (aa-vv*bb).add_bigoh(precision)
    first_bad = next((i for i in range(precision) if residual[i] != 0), None)
    info = {"prime": int(prime), "digits": digits,
            "previous_digits": previous_digits,
            "new_dixon_digits": digits-previous_digits,
            "modulus_bits": int(modulus.nbits()), "rank": rank,
            "pivot_columns_sha256": _hash_ints(pivots),
            "pivot_rows_sha256": _hash_ints(rows), "free": free,
            "B_valuation_mod_prime": chart["B_valuation"],
            "full_finite_window_rows": precision,
            "full_finite_window_residual_sha256":
                _hash_ints([residual[i] for i in range(precision)]),
            "full_finite_window_zero": first_bad is None,
            "lifted_solution_sha256": _hash_ints(sol)}
    if first_bad is not None:
        info["first_nonzero_row"] = first_bad
        info["first_nonzero_valuation"] = int(ZZ(residual[first_bad]).valuation(prime))
    progress("F Dixon full original finite-window residual complete", **info)
    return sol, modulus, info, first_bad is None
